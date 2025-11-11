from dotenv import load_dotenv
import streamlit as st
from langchain_community.llms import Ollama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv(dotenv_path=".env",override=True)

os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system","respond to the questions asked in a sharp and pinpoint way"),
        ("user","Question:{question}")
    ]
)

st.title("OLLAMA 1 BILLION PARAMETER CHATBOT")
texts = st.text_input("whachu got in mind boy")

llm = Ollama(model="gemma3:1b")
output_parser = StrOutputParser()
chain = prompt|llm|output_parser

if texts:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": texts})
    st.markdown(f"**Response:** {response}")
