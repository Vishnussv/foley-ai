#!/usr/bin/env python3
"""
Setup NGROK auth token for tunnel configuration.
Run this once to enable NGROK public URL access.
"""

import sys
import os

# Add backend to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'backend'))

from database_manager import DatabaseManager

def setup_ngrok():
    db = DatabaseManager()
    
    print("=" * 60)
    print("NGROK TUNNEL SETUP")
    print("=" * 60)
    print()
    print("To enable public access tunneling, you need an NGROK auth token.")
    print("Get a free token at: https://dashboard.ngrok.com/signup")
    print()
    
    current_token = db.get_setting("ngrok_authtoken")
    if current_token:
        print(f"Current token: {current_token[:20]}...")
        update = input("Update token? (y/n): ").strip().lower()
        if update != 'y':
            print("Token unchanged.")
            return
    
    token = input("Enter your NGROK auth token: ").strip()
    if not token:
        print("No token provided. Skipping setup.")
        return
    
    db.set_setting("ngrok_authtoken", token)
    print(f"✓ NGROK token saved: {token[:20]}...")
    print()
    print("Restart the app to activate the tunnel.")
    print()

if __name__ == "__main__":
    setup_ngrok()
