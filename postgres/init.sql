CREATE TABLE IF NOT EXISTS generated_sentences (
    id SERIAL PRIMARY KEY,
    sentence_text TEXT NOT NULL,
    generated_by VARCHAR(50),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- TODO: Delete this seed data once connectivity is validated
INSERT INTO generated_sentences (sentence_text, generated_by)
VALUES ('The quick brown fox jumps over the lazy dog', 'system-init');
