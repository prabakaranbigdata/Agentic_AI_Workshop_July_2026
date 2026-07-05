"""
tool_executor.py
----------------
Executes AI tools.
"""

from tools import (
    get_current_time,
    calculate,
    create_file,
    read_file,
    list_files,
)


def execute_tool(tool_name: str, **kwargs):
    """
    Execute the requested tool.
    """

    if tool_name == "time":
        return get_current_time()

    elif tool_name == "calculate":
        return calculate(kwargs.get("expression", ""))

    elif tool_name == "create_file":
        return create_file(
            kwargs.get("filename", ""),
            kwargs.get("content", "")
        )

    elif tool_name == "read_file":
        return read_file(kwargs.get("filename", ""))

    elif tool_name == "list_files":
        return list_files()

    else:
        return f"Unknown Tool: {tool_name}"