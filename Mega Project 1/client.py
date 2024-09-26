from openai import OpenAI

client = OpenAI(
    api_key = "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",
)

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named 'Jarvis'. You are skilled in general tasks."},
        {
            "role": "user","content": "What is coding?"
        }
    ]
)

print(completion.choices[0].message)
