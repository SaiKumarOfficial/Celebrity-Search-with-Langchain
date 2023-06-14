# Integrate chatgpt

from dotenv import load_dotenv
from langchain.llms import OpenAI
import streamlit as st
import os


load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#streamlit framework

st.title("LangChain Demo with OPENAI API")
input_text = st.text_input("Search the topic u want")

# OPENAI LLMS
llm = OpenAI(temperature = 0.8) 
#temperature - defult=0.7, it has the values b/w 0 to 1. This is just suggesting like how much control the agent should
 #have while providing the response

if input_text:
    st.write(llm(input_text))