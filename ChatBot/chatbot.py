from langchain_ollama import ChatOllama
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

# llm = ChatOllama(
#     model="llama3.1:8b",
#     temperature=0.4
# )
load_dotenv()
llm = ChatOpenAI()
chat_history = [
    SystemMessage(content="You are a helpful AI Assistant")
     
]

while(True):
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    # chat_history.append({"role": "user", "content": user_input})
    if(user_input.lower() == 'exit'):
        break
    response = llm.invoke(chat_history)
    # chat_history.append({"role": "assistant", "content": response.content})
    chat_history.append(AIMessage(content=response.content))
    print("AI: ", response.content)
    print("\n")

print(chat_history)