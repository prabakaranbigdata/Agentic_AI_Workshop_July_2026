from prompt_loader import load_prompt
from llm import ask_llm

system_prompt = load_prompt("system_prompt.txt")

question = input("You: ")

answer = ask_llm(system_prompt, question)

print("\nAI:", answer)