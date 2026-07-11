from langchain_huggingface import HuggingFaceEndpointEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEndpointEmbeddings(
    model="sentence-transformers/all-MiniLM-L6-v2",
)

text = "Arunachal is present in the north-eastern part of India."

vector = embeddings.embed_query(text)
# embed_documents

print(len(vector))
