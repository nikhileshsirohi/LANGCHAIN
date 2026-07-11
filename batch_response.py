from langchain_ollama import ChatOllama

llm = ChatOllama(model="llama3.1:8b")

prompts = [f"Tell me a joke #{i}" for i in range(10)]

responses = llm.batch(prompts)

for r in responses:
    print(r.content)