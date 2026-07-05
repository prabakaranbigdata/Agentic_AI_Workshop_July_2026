from llm import ask_llm, ask_final_response
from tool_executor import execute_tool

question = input("You: ")

response = ask_llm(question)

if response.tool_calls:

    tool_result = execute_tool(response.tool_calls[0])

    final_answer = ask_final_response(
        question,
        tool_result
    )

    print("\nAI:\n")

    print(final_answer)

else:

    print(response.content)