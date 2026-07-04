"""
app.py
-------
AI Assistant with Memory
"""

from prompt_loader import load_prompt
from memory import add_message, get_memory, clear_memory
from llm import ask_llm

print("=" * 60)
print("        AI Assistant with Memory")
print("=" * 60)

system_prompt = load_prompt("assistant.txt")

print("\nType 'exit' to quit")
print("Type 'clear' to clear conversation memory\n")

while True:

    user_input = input("You : ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    if user_input.lower() == "clear":
        clear_memory()
        print("\nMemory Cleared.\n")
        continue

    # Store user message
    add_message("user", user_input)

    # Ask LLM
    answer = ask_llm(system_prompt, get_memory())

    # Store AI response
    add_message("assistant", answer)

    print("\nAI :", answer)
    print("-" * 60)