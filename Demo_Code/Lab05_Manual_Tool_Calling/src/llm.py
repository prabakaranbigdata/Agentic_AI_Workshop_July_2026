"""
llm.py
-------
Handles communication with the OpenAI LLM.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

from config import MODEL_NAME, TEMPERATURE

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_llm(system_prompt: str, conversation_history: list):

    messages = [
        {
            "role": "system",
            "content": system_prompt
        }
    ]

    # Add previous conversation
    messages.extend(conversation_history)

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=messages,
        temperature=TEMPERATURE
    )

    return response.choices[0].message.content