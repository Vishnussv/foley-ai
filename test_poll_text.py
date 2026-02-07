
import requests

prompt = "Hello, tell me about SQL in 20 words."
url = "https://text.pollinations.ai/"
data = {
    "messages": [
        {"role": "user", "content": prompt}
    ],
    "model": "openai" # Pollinations uses 'openai' as a generic name for their text models
}

print("Testing Pollinations Text Gen...")
try:
    response = requests.post(url, json=data)
    print(f"Status: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")
