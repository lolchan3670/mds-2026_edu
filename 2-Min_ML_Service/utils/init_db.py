import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="postgres",
    user="postgres",
    password="sql112358"
)

cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS training_results (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(255) NOT NULL,
    algorithm VARCHAR(100) NOT NULL,
    dataset_name VARCHAR(255),
    accuracy FLOAT,
    model_path TEXT,
    train_size FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)
""")

conn.commit()

cur.close()
conn.close()

print("Database initialized")