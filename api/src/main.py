from fastapi import FastAPI
import psycopg2
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
import os

app = FastAPI()

# Allow React (running on a different port) to talk to this API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/last-sentence")
def get_last_sentence():
    conn = psycopg2.connect(
        host=os.getenv("POSTGRES_HOST"),
        dbname=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute("SELECT sentence_text FROM generated_sentences ORDER BY created_at DESC LIMIT 1")
    result = cur.fetchone()
    cur.close()
    conn.close()
    return {"sentence": result[0] if result else "No sentences found"}

if __name__ == "__main__":
    # This actually starts the server
    uvicorn.run(app, host="0.0.0.0", port=8095)