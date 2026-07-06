from langchain_openai import ChatOpenAI
from langgraph.prebuilt import create_react_agent

from config import OPENAI_API_KEY, MODEL_NAME
from tools import get_current_time, multiply, greet

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=MODEL_NAME
)

tools = [
    get_current_time,
    multiply,
    greet
]

agent = create_react_agent(
    model=llm,
    tools=tools
)