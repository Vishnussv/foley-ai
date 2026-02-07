
import openai
import os

key = "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"

client = openai.OpenAI(api_key=key)

try:
    print("Testing image generation...")
    response = client.images.generate(
        model="dall-e-3",
        prompt="a small tech banana",
        n=1,
        size="1024x1024"
    )
    print(f"Success! URL: {response.data[0].url}")
except Exception as e:
    print(f"Failed: {e}")
