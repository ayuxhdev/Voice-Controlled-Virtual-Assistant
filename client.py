from google import genai

client = genai.Client(
    api_key="YOUR_GEMINI_API_KEY_HERE",
)
completion = client.chat.completions.create(
    model="gemini-3.5-flash-lite",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named Jarvis, skilled in general tasks like Alexa and Google Assistant."},
        {"role": "user", "content": "What is programming?"}
    ]
)

print(completion.choices[0].message.content)