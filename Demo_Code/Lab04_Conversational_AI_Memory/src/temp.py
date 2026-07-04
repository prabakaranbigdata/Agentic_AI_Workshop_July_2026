from prompt_loader import load_prompt
from memory import *

from llm import ask_llm

system_prompt = load_prompt("assistant.txt")

add_message("user", "My name is Prabakaran.")
print(ask_llm(system_prompt, get_memory()))

add_message("assistant", "Nice to meet you.")

add_message("user", "Who am I?")

print(ask_llm(system_prompt, get_memory()))