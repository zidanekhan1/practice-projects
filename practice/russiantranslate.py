from dotenv import load_dotenv
load_dotenv()
import os
from groq import Groq
from langchain_groq import ChatGroq
from IPython.display import Markdown
from langchain_core.messages import HumanMessage,SystemMessage
import streamlit as st

groq_key = os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama-3.3-70b-versatile",api_key=groq_key)
st.title("ENGLISH TO RUSSIAN TRANSLATION")
text_input = st.text_input("input in english only!!")
if text_input:
    message = [
    SystemMessage(content="Translate the following from english to russian"),
    HumanMessage(content=text_input)
    ]



    outputa = model.invoke(message)
    russian_output = outputa.content

    st.markdown(f"### 🪄 Translation:\n\n<span style='font-size:22px;'>{russian_output}</span>", unsafe_allow_html=True)