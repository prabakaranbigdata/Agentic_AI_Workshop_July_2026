from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage

from config import OPENAI_API_KEY, MODEL_NAME
from memory import memory

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=MODEL_NAME
)

def ask_llm(system_prompt, question):

    # Store user message
    memory.add_user_message(question)

    # Build message list
    messages = [SystemMessage(content=system_prompt)]
    messages.extend(memory.messages)

    # Call LLM
    response = llm.invoke(messages)

    # Store AI response
    memory.add_ai_message(response.content)

    return response.content