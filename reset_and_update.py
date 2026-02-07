
import sqlite3
import os

# Paths
DB_PATH = "backend/foley.db"
KEY_FILE = r"c:\Users\User\OneDrive\Documents\jarvis v16.8\api key"

def update_system():
    print("--- Resetting and Updating Foley System ---")
    
    # 1. Ensure DB exists and is initialized
    if not os.path.exists(os.path.dirname(DB_PATH)):
        os.makedirs(os.path.dirname(DB_PATH))
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Initialize tables (matching database_manager.py logic)
    cursor.execute('CREATE TABLE IF NOT EXISTS settings (key TEXT PRIMARY KEY, value TEXT)')
    cursor.execute('CREATE TABLE IF NOT EXISTS logs (id INTEGER PRIMARY KEY AUTOINCREMENT, query TEXT, response TEXT, timestamp DATETIME DEFAULT CURRENT_TIMESTAMP)')
    
    # 2. Update API Key from the specific file
    try:
        if os.path.exists(KEY_FILE):
            with open(KEY_FILE, 'r') as f:
                lines = f.readlines()
                # Line 3 is the OpenRouter key
                if len(lines) >= 3:
                    or_key = lines[2].strip()
                    cursor.execute("INSERT OR REPLACE INTO settings (key, value) VALUES (?, ?)", ("openai_api_key", or_key))
                    print(f"Updated OpenRouter key from source file.")
                # Line 1 is the Project key
                if len(lines) >= 1:
                    proj_key = lines[0].strip()
                    # If we already set OR key, maybe we don't overwrite if it's the preferred one? 
                    # Actually, the user might prefer the project key. 
                    # Let's set the OpenRouter one as it was used before.
                    pass
    except Exception as e:
        print(f"Error reading key file: {e}")

    # 3. Optional: Clear history if "reset" means fresh start
    # cursor.execute("DELETE FROM logs")
    # print("Interaction logs cleared.")

    conn.commit()
    conn.close()
    print("System update complete.")

if __name__ == "__main__":
    update_system()
