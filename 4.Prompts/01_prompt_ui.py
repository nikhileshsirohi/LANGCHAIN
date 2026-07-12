from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate, load_prompt
import streamlit as st

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0.4
)
st.header("Research Tool")

paper_input = st.selectbox("Select a research paper", ["Attention Is all you need", "Word2vec", "GPT3: Language Models are Few-Shot Learners"])
style_input = st.selectbox("Select Explaination style", ["Beginner Friendly", "Technical oriented", "Mathematical oriented"])
length_input = st.selectbox("Select Explaination length", ["Short (1-2 paragraphs)", "Medium (3-4 paragraphs)", "Long (deatail explanation)"])

template = load_prompt('4.Prompts/template.json')

prompt = template.invoke(
    {'paper_input': paper_input, 
     'style_input': style_input, 
     'length_input': length_input
    }
)

# print(prompt)
# user_input = st.text_input("Enter your prompt here")
if st.button("Send"):
    response = llm.invoke(prompt)
    st.write(response.content)
    # print(response)