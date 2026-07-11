# from langchain_openai import OpenAI
from langchain_ollama import Ollama
from dotenv import load_dotenv
import os

load_dotenv()

# llm = OpenAI(
#     model="gpt-4o-mini",
#     temperature=0.4,
# )

llm = Ollama(
    model="qwen2.5:14b",
    temperature=0.4
)

response = llm.invoke("Tell me about yourself")

print(response)