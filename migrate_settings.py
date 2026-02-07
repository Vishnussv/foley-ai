
import sqlite3
import os

source_db = "backend/foleydraco.db"
target_db = "backend/foley.db"

if os.path.exists(source_db) and os.path.exists(target_db):
    s_conn = sqlite3.connect(source_db)
    t_conn = sqlite3.connect(target_db)
    
    s_cursor = s_conn.cursor()
    t_cursor = t_conn.cursor()
    
    s_cursor.execute("SELECT key, value FROM settings")
    settings = s_cursor.fetchall()
    
    for key, value in settings:
        print(f"Migrating {key}...")
        t_cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", (key, value))
    
    t_conn.commit()
    s_conn.close()
    t_conn.close()
    print("Migration complete.")
else:
    print("Databases not found.")
