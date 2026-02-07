
import requests
import json

key = "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"
prompt = "a small tech banana"

response = requests.post(
  url="https://openrouter.ai/api/v1/chat/completions",
  headers={
    "Authorization": f"Bearer {key}",
    "Content-Type": "application/json",
  },
  data=json.dumps({
    "model": "google/gemini-2.5-flash-image",
    "modalities": ["image"],
    "messages": [
      {"role": "user", "content": prompt}
    ],
    "max_tokens": 1500
  })
)

print(f"Status: {response.status_code}")
print(response.text)
