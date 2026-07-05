from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

from config import OPENAI_API_KEY, MODEL_NAME

llm = ChatOpenAI(
    api_key=OPENAI_API_KEY,
    model=MODEL_NAME
)

prompt = ChatPromptTemplate.from_messages(

    [

        ("system",
         "You are a {role}. Answer politely."),

        ("human",
         "{question}")

    ]

)

chain = prompt | llm


def ask_llm(role, question):

    response = chain.invoke(

        {

            "role": role,

            "question": question

        }

    )

    return response.content