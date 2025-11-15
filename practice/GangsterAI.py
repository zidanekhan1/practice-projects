import streamlit as st
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import groq
import openai

load_dotenv()

## Tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with Groq"

# Correct prompt
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "Respond to user queries like a tough mob boss."),
        ("user", "Question: {question}")
    ]
)

def generate_response(question, api_key, llm_name,temperature,max_tokens):
    model = ChatGroq(
        model=llm_name,
        api_key=api_key
    )

    output_parser = StrOutputParser()
    chain = prompt | model | output_parser

    answer = chain.invoke({"question": question})
    return answer

st.title("enhanced Q&A Chatbot with groq")

st.sidebar.title("Settings")
api_key=st.sidebar.text_input("Enter yout groq API Key : ", type="password")

llm = st.sidebar.selectbox(
    "Select Groq Model",
    [
        "llama-3.3-70b-versatile",          # best quality
        "llama-3.1-8b-instant",             # fastest
        "meta-llama/llama-4-scout-17b-16e-instruct",     # works for you
        "meta-llama/llama-4-maverick-17b-128e-instruct", # also works
        "qwen/qwen3-32b",                   # strong Chinese/English model
        "openai/gpt-oss-20b",               # open-source GPT LLM
        "openai/gpt-oss-120b",              # extremely powerful (if available)
        "moonshotai/kimi-k2-instruct-0905",
        "moonshotai/kimi-k2-instruct"
    ]
)
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=1.0,value=0.7)
max_tokens=st.sidebar.slider("Max Tokens",min_value=50,max_value=300,value=150)

st.write("Ask me something")
user_input=st.text_input("You:")
if user_input:
    response=generate_response(user_input,api_key,llm,temperature,max_tokens)
    st.write(response)
else:
    st.write("please provide a question")