from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

MODEL_ID = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
LOCAL_MODEL_DIR = "/Volumes/NIKHILESH/Projects/LANGCHAIN/Models/TinyLlama"


# LangChain LLM
llm = HuggingFacePipeline.from_model_id(
    model_id=MODEL_ID,
    task="text-generation",
    model_kwargs={
        "cache_dir": LOCAL_MODEL_DIR,
    },
    pipeline_kwargs=dict(
        temperature=0.4,
        max_new_tokens=100,
    )
)

response = llm.invoke("Tell me about yourself")

print(response)