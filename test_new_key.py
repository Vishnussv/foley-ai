
import openai

key = "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"

client = openai.OpenAI(api_key=key)

try:
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": "hi"}],
        max_tokens=5
    )
    print(f"Success: {completion.choices[0].message.content}")
except Exception as e:
    print(f"Error: {e}")
