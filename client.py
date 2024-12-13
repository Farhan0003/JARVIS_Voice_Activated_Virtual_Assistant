
from openai import OpenAI
client = OpenAI(
    api_key="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",
)
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a Virtual  assistant names jarvis skilled in general task like alexa and Google cloud"},
        {
            "role": "user",
            "content": "What is coding."
        }
    ]
)

print(completion.choices[0].message.content)



