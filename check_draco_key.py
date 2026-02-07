
import sqlite3
import os

db_path = os.path.join('backend', 'foleydraco.db')
if os.path.exists(db_path):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("SELECT value FROM settings WHERE key='openai_api_key'")
    print(f"Foleydraco Database Key: {c.fetchone()}")
    conn.close()
else:
    print("foleydraco.db not found")
