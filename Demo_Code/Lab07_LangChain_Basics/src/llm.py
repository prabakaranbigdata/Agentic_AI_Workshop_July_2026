from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from config import OPENAI_API_KEY, MODEL_NAME

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=MODEL_NAME
)

def ask_llm(system_prompt, user_question):

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=user_question)
    ]

    response = llm.invoke(messages)

    return response.content