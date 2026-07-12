from langchain_ollama import ChatOllama
from langchain_core.prompts import PromptTemplate
import streamlit as st

llm = ChatOllama(
    model="llama3.1:8b",
    temperature=0.4
)
st.header("Research Tool")

paper_input = st.selectbox("Select a research paper", ["Attention Is all you need", "Word2vec", "GPT3: Language Models are Few-Shot Learners"])
style_input = st.selectbox("Select Explaination style", ["Beginner Friendly", "Technical oriented", "Mathematical oriented"])
length_input = st.selectbox("Select Explaination length", ["Short (1-2 paragraphs)", "Medium (3-4 paragraphs)", "Long (deatail explanation)"])

template = PromptTemplate(
    template = """
    Please summarize the research paper titled "{paper_input}" with the following specifications:
    Explanation Style: {style_input}
    Explanation Length: {length_input}
    1. Mathematical Details:
    - Include relevant mathematical equations if present in the paper.
    - Explain the mathematical concepts using simple, intuitive code snippets where applicable.
    2. Analogies:
    - Use relatable analogies to simplify complex ideas.
    If certain information is not available in the paper, respond with: "Insufficient information available" instead of guessing.
    Ensure the summary is clear, accurate, and aligned with the provided style and length.
    """,

    input_variables = ["paper_input", "style_input", "length_input"],
    validate_template=True 
)

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