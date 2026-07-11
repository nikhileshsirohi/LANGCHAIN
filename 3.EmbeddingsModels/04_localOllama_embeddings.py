from langchain_ollama import OllamaEmbeddings

embeddings = OllamaEmbeddings(
    model = "nomic-embed-text:latest",
)

text = "Delhi is the capital of India"

vector = embeddings.embed_query(text)
# embed_documents

print(len(vector))