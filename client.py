from openai import OpenAI

client = OpenAI(
    api_key="YOUR_NEW_OPENAI_API_KEY_HERE",
)
completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
        {"role": "user", "content": "What is programming?"}
    ]
)

print(completion.choices[0].message.content)