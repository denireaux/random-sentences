import stomp
import os
import queue
import threading
import logging
import signal
import time

from models.PostgresClient import PostgresClient

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s"
)

class AMQClient(stomp.ConnectionListener):

    WORKER_COUNT = 3
    QUEUE_SIZE = 1000

    def __init__(self):
        self.host = os.getenv("ACTIVEMQ_HOST", "activemq")
        self.port = int(os.getenv("ACTIVEMQ_STOMP_PORT", 61613))
        self.topic = f"/topic/{os.getenv('ACTIVEMQ_SENTENCE_TOPIC', 'sentences')}"

        self.msg_queue = queue.Queue(maxsize=self.QUEUE_SIZE)

        self.conn = stomp.Connection([(self.host, self.port)])
        self.conn.set_listener('', self)

        self.pg_client = PostgresClient()

        self.running = True

    # -----------------------------
    # STOMP LISTENER METHODS
    # -----------------------------

    def on_message(self, frame):
        try:
            self.msg_queue.put(frame.body, timeout=2)
        except queue.Full:
            logging.warning("Message queue full — dropping message")

    def on_error(self, frame):
        logging.error(f"Broker error: {frame.body}")

    def on_disconnected(self):
        logging.warning("Disconnected from ActiveMQ")
        if self.running:
            self._reconnect()

    # -----------------------------
    # CONNECTION MANAGEMENT
    # -----------------------------

    def connect(self):
        logging.info(f"Connecting to {self.host}:{self.port}")

        self.conn.connect("admin", "admin", wait=True)

        self.conn.subscribe(
            destination=self.topic,
            id=1,
            ack="auto"
        )

        logging.info(f"Subscribed to {self.topic}")

    def _reconnect(self):
        while self.running:
            try:
                logging.info("Attempting reconnect...")
                time.sleep(5)
                self.connect()
                logging.info("Reconnected successfully")
                return
            except Exception as e:
                logging.error(f"Reconnect failed: {e}")

    # -----------------------------
    # WORKER PROCESSING
    # -----------------------------

    def worker(self):
        while self.running:
            try:
                message = self.msg_queue.get(timeout=1)

                self.pg_client.persist_amq_message(message)

                rows = self.pg_client.pop_last_five_sentences()
                paragraph = self.pg_client._arrange_paragraph(rows) # NOTE: This is as far as I got with the paragraphs
                print(f"Resulting paragraph: {paragraph}") if paragraph else print("Waiting for enough sentences to parse into paragraph...")

                if rows:
                    print("\nCollected 5 sentences:")
                    for r in rows:
                        print(r)

                self.msg_queue.task_done()

            except queue.Empty:
                continue
            except Exception as e:
                logging.error(f"Worker error: {e}")

    # -----------------------------
    # STARTUP / SHUTDOWN
    # -----------------------------

    def start(self):
        self.connect()

        logging.info("AMQ Client started successfully")
        logging.info("Starting worker threads")

        for _ in range(self.WORKER_COUNT):
            t = threading.Thread(target=self.worker, daemon=True)
            t.start()

        signal.signal(signal.SIGINT, self._shutdown)

        while self.running:
            time.sleep(1)

    def _shutdown(self, signum, frame):

        logging.info("Shutting down consumer")

        self.running = False

        try:
            if self.conn.is_connected():
                self.conn.disconnect()
        except Exception:
            pass
        
    def _process_loop(self):
        while True:
            try:
                message = self.msg_queue.get(timeout=2)

                self.pg_client.persist_amq_message(message)

                rows = self.pg_client.pop_last_five_sentences()

                if rows:
                    print("\nCollected 5 sentences:")
                    for r in rows:
                        print(r)

                self.msg_queue.task_done()

            except queue.Empty:
                continue
