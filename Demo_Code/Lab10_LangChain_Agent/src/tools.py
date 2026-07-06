from datetime import datetime
from langchain_core.tools import tool


@tool
def get_current_time():
    """Returns current date and time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


@tool
def multiply(a: int, b: int):
    """Multiply two numbers."""
    return a * b


@tool
def greet(name: str):
    """Greets the user."""
    return f"Hello {name}! Welcome to Agentic AI."