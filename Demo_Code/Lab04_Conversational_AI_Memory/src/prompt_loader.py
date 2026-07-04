"""
prompt_loader.py
----------------
Loads prompt templates from the prompts folder.
"""

from pathlib import Path


PROMPT_FOLDER = Path(__file__).parent.parent / "prompts"


def load_prompt(filename: str) -> str:
    """
    Load a prompt file and return its contents.

    Args:
        filename (str): Prompt file name

    Returns:
        str: Prompt text
    """

    prompt_path = PROMPT_FOLDER / filename

    with open(prompt_path, "r", encoding="utf-8") as file:
        return file.read().strip()