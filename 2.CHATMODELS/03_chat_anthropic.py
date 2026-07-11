from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(
    model="claude-3.0",
    temperature=0.4
)

reponse = llm.invoke("Tell me about yourself")

print(reponse.content)