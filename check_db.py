
import sqlite3
import os

databases = ["backend/foley.db", "backend/foleydraco.db", "foleydraco.db"]

for db_path in databases:
    if os.path.exists(db_path):
        print(f"--- Checking {db_path} ---")
        try:
            conn = sqlite3.connect(db_path)
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = cursor.fetchall()
            print(f"Tables: {tables}")
            
            for table in tables:
                if table[0] == 'settings':
                    cursor.execute("SELECT key, value FROM settings")
                    rows = cursor.fetchall()
                    for row in rows:
                        print(f"  {row[0]}: {row[1]}")
            conn.close()
        except Exception as e:
            print(f"Error checking {db_path}: {e}")
    else:
        print(f"Database {db_path} not found.")
