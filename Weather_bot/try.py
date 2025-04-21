from openai import OpenAI

client = OpenAI(
  api_key="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"
)

completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": "what is the weather in New York?"},
  ]
)

print(completion.choices[0].message);
