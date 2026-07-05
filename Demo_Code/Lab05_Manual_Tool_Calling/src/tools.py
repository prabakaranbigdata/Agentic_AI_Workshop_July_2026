"""
tools.py
---------
Collection of tools that the AI Agent can use.
"""

from datetime import datetime
import os


def get_current_time():
    """
    Return the current date and time.
    """

    return datetime.now().strftime("%d-%m-%Y %H:%M:%S")


def calculate(expression: str):
    """
    Evaluate a mathematical expression.

    Example:
        25 * 8
    """

    try:
        result = eval(expression)
        return str(result)

    except Exception as e:
        return f"Calculation Error: {e}"


def create_file(filename: str, content: str):
    """
    Create a text file.
    """

    try:

        with open(filename, "w", encoding="utf-8") as file:
            file.write(content)

        return f"File '{filename}' created successfully."

    except Exception as e:
        return f"File Creation Error: {e}"


def read_file(filename: str):
    """
    Read a text file.
    """

    try:

        with open(filename, "r", encoding="utf-8") as file:
            return file.read()

    except Exception as e:
        return f"File Read Error: {e}"


def list_files():
    """
    List files in current directory.
    """

    files = os.listdir()

    if not files:
        return "No files found."

    return "\n".join(files)