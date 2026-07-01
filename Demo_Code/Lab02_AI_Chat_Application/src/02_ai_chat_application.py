from openai import OpenAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Read API Key
api_key = os.getenv("OPENAI_API_KEY")

# Create OpenAI Client
client = OpenAI(api_key=api_key)

print("=" * 60)
print("🤖 AI Chat Application")
print("Type 'exit' to quit")
print("=" * 60)

while True:

    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        print("\n👋 Thank you! Have a great day.")
        break

    try:

        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {
                    "role": "user",
                    "content": user_input
                }
            ]
        )

        print("\nAI :")
        print(response.choices[0].message.content)

    except Exception as ex:
        print("\nError :", ex)

    print("\n" + "-" * 60)