from prompt_loader import load_prompt
from memory import add_message, get_memory
from llm import ask_llm

system_prompt = load_prompt("assistant.txt")

#add_message("user", "What time is it?")
#add_message("user", "Calculate 125*845")
add_message("user", "Create a file notes.txt containing Hello Agent")

answer = ask_llm(system_prompt, get_memory())

print(answer)