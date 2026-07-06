from agent import agent
from langchain_core.messages import HumanMessage

while True:

    question = input("You: ")

    if question.lower() == "exit":
        break

    response = agent.invoke(

        {

            "messages":[

                HumanMessage(content=question)

            ]

        }

    )

    print()

    print("AI:")

    print(response["messages"][-1].content)

    print()