"""
llm.py
-------
Handles communication with the OpenAI LLM.
"""

import os

from dotenv import load_dotenv
from openai import OpenAI

# Load environment variables
load_dotenv()

# Create OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_llm(system_prompt: str, user_prompt: str) -> str:
    """
    Send prompts to the LLM and return the response.

    Args:
        system_prompt (str): AI role/instructions
        user_prompt (str): User question

    Returns:
        str: AI response
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content