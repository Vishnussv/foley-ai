
import os
import sys

# Change to backend dir to match app.py loading
os.chdir('backend')
sys.path.append(os.getcwd())

import ai_engine
import importlib
importlib.reload(ai_engine)

engine = ai_engine.AIEngine()
print(f"Loaded from: {ai_engine.__file__}")
print(f"Key used: {engine.api_key[:20]}...")
