from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
    dimension=32,
)

documents = [
        "LangChain is a framework for developing applications powered by language models.",
        "LangChain provides a standard interface for all LLMs, as well as a toolkit for developers to build applications with LLMs."
    ]

result = embeddings.embed_documents(documents)
# For single quey
# result = embeddings.embed_query("Tibet is the part of India")

print(str(result))