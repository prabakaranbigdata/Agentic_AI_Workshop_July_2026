from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage

from config import OPENAI_API_KEY, MODEL_NAME
from tools import get_current_time

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=MODEL_NAME
)

llm_with_tools = llm.bind_tools([get_current_time])


def ask_llm(question):

    response = llm_with_tools.invoke(question)

    return response

def ask_final_response(question, tool_result):

    prompt = f"""
The user asked:

{question}

The tool returned:

{tool_result}

Generate a natural language response for the user.
"""

    response = llm.invoke([HumanMessage(content=prompt)])

    return response.content
