from dotenv import load_dotenv
from groq import Groq

import os

load_dotenv()
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("PETER6767")
client=Groq(api_key=api_key)

while True:
    user_message=input("you: ")

    if user_message.lower()=="bye":
        print("goodbye the bot is saying googbye") 
        break

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    print("Bot:", response.choices[0].message.content)
    