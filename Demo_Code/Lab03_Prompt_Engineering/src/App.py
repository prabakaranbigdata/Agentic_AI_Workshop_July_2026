"""
app.py
-------
Prompt Engineering Demo
"""

from prompt_loader import load_prompt
from llm import ask_llm


ROLES = {
    "1": ("Normal Chat", "normal.txt"),
    "2": ("Python Trainer", "python_trainer.txt"),
    "3": ("Technical Interviewer", "interviewer.txt"),
    "4": ("Data Engineering Architect", "architect.txt"),
    "5": ("AI Career Mentor", "mentor.txt"),
}


print("=" * 50)
print("      Prompt Engineering Lab")
print("=" * 50)

print("\nChoose AI Role\n")

for key, (role, _) in ROLES.items():
    print(f"{key}. {role}")

choice = input("\nEnter your choice: ")

if choice not in ROLES:
    print("\nInvalid choice!")
    exit()

role_name, prompt_file = ROLES[choice]

print(f"\nSelected Role : {role_name}")

system_prompt = load_prompt(prompt_file)

while True:

    question = input("\nAsk your question ('exit' to quit): ")

    if question.lower() == "exit":
        print("\nThank you for using Prompt Engineering Lab!")
        break

    answer = ask_llm(system_prompt, question)

    print("\nAI Response\n")
    print(answer)