
import os
import sys

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), 'backend'))

from ai_engine import AIEngine

engine = AIEngine()
print(f"Current API Key: {engine.api_key[:10]}...")
print(f"Current OR Key: {engine.or_key[:10] if engine.or_key else 'None'}...")

response = engine.get_response("tell me about sql")
print(f"AI Response: {response}")
