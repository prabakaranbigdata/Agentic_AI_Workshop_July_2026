from prompt_loader import load_prompt
from llm import ask_llm

system_prompt = load_prompt("system_prompt.txt")

print("Type 'exit' to quit.\n")

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    answer = ask_llm(system_prompt, question)

    print("\nAI:", answer)
    print()