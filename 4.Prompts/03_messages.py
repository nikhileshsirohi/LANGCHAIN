from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0.4
)

messages = [
    SystemMessage(content="You are a helpful assistant"),
    HumanMessage(content="who is greater between 1 and 2"),
]

response = llm.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)