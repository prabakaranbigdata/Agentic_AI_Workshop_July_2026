"""
agent.py
---------
AI Agent
"""

from llm import ask_llm
from tool_executor import execute_tool


def run_agent(system_prompt, memory):
    """
    Run the AI Agent.
    """

    response = ask_llm(system_prompt, memory)

    # Normal AI response
    if not response.startswith("TOOL:"):
        return response

    # ----------------------------------
    # Parse TOOL response
    # ----------------------------------

    parts = response.split(":")

    tool_name = parts[1]

    # Time
    if tool_name == "time":

        return execute_tool("time")

    # Calculator
    elif tool_name == "calculate":

        expression = parts[2]

        return execute_tool(
            "calculate",
            expression=expression
        )

    # Create File
    elif tool_name == "create_file":

        filename = parts[2]
        content = parts[3]

        return execute_tool(
            "create_file",
            filename=filename,
            content=content
        )

    # Read File
    elif tool_name == "read_file":

        filename = parts[2]

        return execute_tool(
            "read_file",
            filename=filename
        )

    # List Files
    elif tool_name == "list_files":

        return execute_tool("list_files")

    else:

        return "Unknown Tool."