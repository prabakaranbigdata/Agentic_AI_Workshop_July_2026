from tools import get_current_time

tools = {
    "get_current_time": get_current_time
}


def execute_tool(tool_call):

    tool_name = tool_call["name"]

    tool = tools[tool_name]

    return tool.invoke(tool_call["args"])