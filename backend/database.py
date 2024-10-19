import psycopg2

def get_db_connection():
    return psycopg2.connect(
        host="localhost",
        database="rule_engine",
        user="your_username",
        password="your_password"
    )

def setup_database():
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS rules (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    rule_string TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS attributes (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(255) NOT NULL,
                    data_type VARCHAR(50) NOT NULL,
                    UNIQUE(name)
                );
            """)
            cur.execute("""
                CREATE TABLE IF NOT EXISTS rule_attributes (
                    rule_id INTEGER REFERENCES rules(id),
                    attribute_id INTEGER REFERENCES attributes(id),
                    PRIMARY KEY (rule_id, attribute_id)
                );
            """)
            # Insert sample data if needed
