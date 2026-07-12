from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "llama3.1:8b",
    temperature=0.4
)

chat_template = ChatPromptTemplate([
    ('system', "you are a helpful {domain} expert"),
    ('human', "Explain in simple term, what is {topic}"),
])

prompt = chat_template.invoke({'domain':'cricket', 'topic':'Chinaman'})

response = llm.invoke(prompt)
print(response.content)