"""
memory.py
----------
Simple conversation memory.
"""

from config import MAX_MEMORY_MESSAGES


conversation_history = []


def add_message(role: str, content: str):
    """
    Store a conversation message.
    """

    conversation_history.append({
        "role": role,
        "content": content
    })

    # Keep only recent messages
    if len(conversation_history) > MAX_MEMORY_MESSAGES:
        conversation_history.pop(0)


def get_memory():
    """
    Return conversation history.
    """

    return conversation_history


def clear_memory():
    """
    Clear all memory.
    """

    conversation_history.clear()