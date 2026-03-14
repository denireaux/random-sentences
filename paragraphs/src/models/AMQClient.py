import stomp
import sys
import os
import queue

from models.PostgresClient import PostgresClient

class AMQClient(stomp.ConnectionListener):
    def __init__(self):
        self.host = os.getenv("ACTIVEMQ_HOST", "activemq")
        self.port = int(os.getenv("ACTIVEMQ_STOMP_PORT", 61613))
        self.topic = f"/topic/{os.getenv('ACTIVEMQ_SENTENCE_TOPIC', 'sentences')}"
        
        self.msg_queue = queue.Queue()
        self.conn = stomp.Connection([(self.host, self.port)])
        self.conn.set_listener('', self)
        
        self.pg_client = PostgresClient()

    def on_message(self, frame):
        # print(f'Listener: Received message: "{frame}"')
        self.msg_queue.put(frame.body)

    def on_error(self, frame):
        print(f'Listener: Received an error: "{frame.body}"')

    def on_disconnected(self):
        print('Listener: Disconnected from ActiveMQ')

    def start(self):
        try:
            print(f"Main: Connecting to {self.host}:{self.port}...")
            self.conn.connect('admin', 'admin', wait=True)
            self.conn.subscribe(destination=self.topic, id='1', ack='auto')
            print(f"Main: Subscribed to {self.topic}. Waiting for messages...")
            
            self._process_loop()

        except KeyboardInterrupt:
            print("\nMain: Stopping subscriber...")
            if self.conn.is_connected():
                self.conn.disconnect()
        except Exception as e:
            print(f"Main: Connection failed: {e}")
            sys.exit(1)

    def _process_loop(self):
        while True:
            try:
                message = self.msg_queue.get(timeout=2)
                self.pg_client.persist_amq_message(message)
                self.msg_queue.task_done()

            except queue.Empty:
                continue
