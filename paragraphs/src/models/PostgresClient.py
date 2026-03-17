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

    def pop_last_five_sentences(self):
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
            are_five_sentences_available = self._check_for_five_sentences(cursor)

            if are_five_sentences_available is False:
                cursor.close()
                return []

            query = """
                DELETE FROM generated_sentences
                WHERE id IN (
                    SELECT id
                    FROM generated_sentences
                    ORDER BY created_at DESC
                    LIMIT 5
                )
                RETURNING sentence_text, generated_by, created_at;
            """

            cursor.execute(query)
            rows = cursor.fetchall()

            conn.commit()
            cursor.close()

            print("\nCollected 5 sentences:")
            for r in rows:
                print(f"{r[2]} | {r[1]} | {r[0]}")

            return rows

        except psycopg2.Error as e:
            print(f"Postgres Error: {e}")
            return []

        finally:
            if conn:
                conn.close()


    def _check_for_five_sentences(self, cursor):
        cursor.execute("SELECT COUNT(*) FROM generated_sentences")
        count = cursor.fetchone()[0]

        if count < 5:
            return False

        return True
        
