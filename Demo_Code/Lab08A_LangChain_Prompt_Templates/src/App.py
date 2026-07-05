from llm import ask_llm

role = input("Enter Role : ")

question = input("Question : ")

answer = ask_llm(role, question)

print("\nAI:\n")

print(answer)