from tool_executor import execute_tool

print(execute_tool("time"))

print(execute_tool(
    "calculate",
    expression="25*8"
))

print(execute_tool(
    "create_file",
    filename="demo.txt",
    content="Hello Agentic AI"
))

print(execute_tool(
    "read_file",
    filename="demo.txt"
))

print(execute_tool("list_files"))