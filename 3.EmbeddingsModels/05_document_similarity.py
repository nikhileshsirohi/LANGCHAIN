from langchain_ollama import OllamaEmbeddings
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

documents = [
    "Arunachal is present in the north-eastern part of India",
    "Delhi is the capital of India",
    "Mumbai is the financial capital of India",
    ]

embeddings = OllamaEmbeddings(
    model = "nomic-embed-text:latest",
)
query = "Tell me about Arunachal Pradesh"
query_embedding = embeddings.embed_query(query)
vectors = embeddings.embed_documents(documents)

# Compute cosine similarity between the query embedding and document embeddings
similarities = cosine_similarity([query_embedding], vectors)[0]

index, score = sorted(list(enumerate(similarities)), key = lambda x: x[1], reverse = True)[0]
# print(index)
print("Question: ", query)
print("Most Similar Answer: ", documents[index])
print("Similarity Score: ", score)
