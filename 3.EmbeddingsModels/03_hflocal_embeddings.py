from langchain_huggingface import HuggingFaceEmbeddings

LOCAL_MODEL_DIR = "/Volumes/NIKHILESH/Projects/LANGCHAIN/Models/TinyLlama"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2",
    cache_folder=LOCAL_MODEL_DIR
)

vector = embeddings.embed_query("Arunachal is present in the north-eastern part of India")
# embed_documents

print(len(vector))