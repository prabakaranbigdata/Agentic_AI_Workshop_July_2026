from agent import agent
from langchain_core.messages import HumanMessage

response = agent.invoke(
    {
        "messages": [
            HumanMessage(content="Hello")
        ]
    }
)

print(response)