import psycopg2
import os

class PostgresClient():
    def __init__(self):
        self.host     = os.getenv("POSTGRES_HOST")
        self.port     = os.getenv("POSTGRES_PORT")
        self.dbname   = os.getenv("POSTGRES_DB")
        self.user     = os.getenv("POSTGRES_USER")
        self.password = os.getenv("POSTGRES_PASSWORD")
        
    def persist_amq_message(self, message):
        conn = None
        try:
            conn = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.dbname,
                user=self.user,
                password=self.password
            )
            cursor = conn.cursor()
            
            insert_query = """
            INSERT INTO generated_sentences (SENTENCE_TEXT, GENERATED_BY, CREATED_AT)
            VALUES (%s, %s, NOW())
            """
            
            cursor.execute(insert_query, (message, "ActiveMQ-Listener"))
            conn.commit()
            cursor.close()
            
            print(f"Persisted successfully: {message}")
            
        except psycopg2.Error as e:
            print(f"Postgres Error: {e}")
        finally:
            if conn:
                conn.close()
