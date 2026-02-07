
import openai

key = "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"
client = openai.OpenAI(
    api_key=key,
    base_url="https://openrouter.ai/api/v1"
)

models = ["google/gemma-3-27b-it:free", "qwen/qwen3-coder:free", "mistralai/mistral-small-3.1-24b-instruct:free"]

for model in models:
    print(f"Testing model: {model}")
    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": "hello"}],
            max_tokens=10
        )
        print(f"Success! Response: {completion.choices[0].message.content}")
        break
    except Exception as e:
        print(f"Failed {model}: {e}")
