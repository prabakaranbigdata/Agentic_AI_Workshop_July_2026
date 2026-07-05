"""
app.py
-------
AI Agent with Manual Tool Calling
"""

from prompt_loader import load_prompt
from llm import ask_llm
from memory import add_message, get_memory, clear_memory
from tool_executor import execute_tool

system_prompt = load_prompt("assistant.txt")

print("=" * 60)
print("        AI Agent - Tool Calling")
print("=" * 60)

print("\nAvailable Commands")
print("--------------------------")
print("time")
print("calculate <expression>")
print("create <filename> <content>")
print("read <filename>")
print("list")
print("clear")
print("exit")

while True:

    user_input = input("\nYou : ")

    if user_input.lower() == "exit":
        print("\nGoodbye!")
        break

    if user_input.lower() == "clear":
        clear_memory()
        print("Memory Cleared.")
        continue

    # -------------------------------
    # Tool : Time
    # -------------------------------

    if user_input.lower() == "time":

        result = execute_tool("time")

        print("\nTool :", result)

        continue

    # -------------------------------
    # Tool : Calculator
    # -------------------------------

    if user_input.lower().startswith("calculate"):

        expression = user_input.replace("calculate", "").strip()

        result = execute_tool(
            "calculate",
            expression=expression
        )

        print("\nTool :", result)

        continue

    # -------------------------------
    # Tool : Create File
    # -------------------------------

    if user_input.lower().startswith("create"):

        parts = user_input.split(maxsplit=2)

        if len(parts) < 3:
            print("Usage: create filename content")
            continue

        filename = parts[1]
        content = parts[2]

        result = execute_tool(
            "create_file",
            filename=filename,
            content=content
        )

        print("\nTool :", result)

        continue

    # -------------------------------
    # Tool : Read File
    # -------------------------------

    if user_input.lower().startswith("read"):

        parts = user_input.split(maxsplit=1)

        if len(parts) < 2:
            print("Usage: read filename")
            continue

        filename = parts[1]

        result = execute_tool(
            "read_file",
            filename=filename
        )

        print("\nTool :", result)

        continue

    # -------------------------------
    # Tool : List Files
    # -------------------------------

    if user_input.lower() == "list":

        result = execute_tool("list_files")

        print("\nTool :")
        print(result)

        continue

    # -------------------------------
    # Otherwise use LLM
    # -------------------------------

    add_message("user", user_input)

    answer = ask_llm(
        system_prompt,
        get_memory()
    )

    add_message("assistant", answer)

    print("\nAI :", answer)