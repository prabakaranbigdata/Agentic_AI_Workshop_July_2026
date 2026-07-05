from prompt_loader import load_prompt
from memory import add_message, get_memory
from agent import run_agent

system_prompt = load_prompt("assistant.txt")

add_message("user", "Create file notes.txt containing Hello Agent")


answer = run_agent(system_prompt, get_memory())

print(answer)