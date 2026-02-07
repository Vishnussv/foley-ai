
import sqlite3
import os

db_path = os.path.join('backend', 'foley.db')
conn = sqlite3.connect(db_path)
c = conn.cursor()
c.execute("SELECT value FROM settings WHERE key='openai_api_key'")
print(f"Database Key: {c.fetchone()}")
conn.close()
