from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from psycopg2 import pool
import uvicorn
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

db_pool = pool.SimpleConnectionPool(
    1, 10,
    host=os.getenv("POSTGRES_HOST"),
    dbname=os.getenv("POSTGRES_SENTENCE_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

def query_one(sql):
    conn = db_pool.getconn()
    try:
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        cur.close()
        return result[0] if result else None
    finally:
        db_pool.putconn(conn)

@app.get("/api/last-sentence")
def get_last_sentence():
    result = query_one("SELECT sentence_text FROM generated_sentences ORDER BY created_at DESC LIMIT 1")
    return {"sentence": result or None}

@app.get("/api/last-paragraph")
def get_last_paragraph():
    result = query_one("SELECT paragraph_text FROM generated_paragraphs ORDER BY created_at DESC LIMIT 1")
    return {"paragraph": result or None}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8095)