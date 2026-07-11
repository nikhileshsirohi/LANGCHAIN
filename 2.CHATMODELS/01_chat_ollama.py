from langchain_ollama import ChatOllama
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0.4
)

response = llm.invoke("Tell me about yourself")

print(response.content)