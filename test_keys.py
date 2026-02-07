import openai
import os

KEY_OPENAI = "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"
KEY_OPENROUTER = "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"

def test_key(name, key, base_url=None):
    print(f"Testing {name}...")
    try:
        client = openai.OpenAI(api_key=key, base_url=base_url)
        response = client.chat.completions.create(
            model="gpt-4o" if not base_url else "openai/gpt-4o", # Model name for OpenRouter
            messages=[{"role": "user", "content": "Say hello"}],
            max_tokens=10
        )
        print(f"  Success: {response.choices[0].message.content.strip()}")
        return True
    except Exception as e:
        print(f"  Error: {e}")
        return False

print("--- API Key Connectivity Test ---")
test_key("OpenAI (sk-proj)", KEY_OPENAI)
test_key("OpenRouter", KEY_OPENROUTER, base_url="https://openrouter.ai/api/v1")
