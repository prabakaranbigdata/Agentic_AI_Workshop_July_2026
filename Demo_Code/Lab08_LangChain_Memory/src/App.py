from llm import ask_llm

role = input("Role : ")

question = input("Question : ")

answer = ask_llm(role, question)

print()

print(answer)