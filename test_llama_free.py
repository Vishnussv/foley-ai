
import openai

key = "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"
client = openai.OpenAI(
    api_key=key,
    base_url="https://openrouter.ai/api/v1"
)

try:
    completion = client.chat.completions.create(
        model="meta-llama/llama-3.2-3b-instruct:free",
        messages=[{"role": "user", "content": "hello"}],
        max_tokens=10
    )
    print(f"Success! Response: {completion.choices[0].message.content}")
except Exception as e:
    print(f"Failed: {e}")
