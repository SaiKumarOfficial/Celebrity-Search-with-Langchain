# Integrate chatgpt 

import os
from dotenv import load_dotenv
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain # LLMChain is responsible for executing those prompt template
from langchain.chains import SimpleSequentialChain # it is used to combine the chains
from langchain.memory import ConversationBufferMemory # to store the conversation in the memory



import streamlit as st

load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

#streamlit framework

st.title("Celebrity Search Results")
input_text = st.text_input("Search the topic u want")

# Prompt Templates
first_input_prompt = PromptTemplate(
    #what fixed kind of words you are trying to search for
    input_variables = ['name'],
    template = "Tell me about celebrity {name}"
)
#Now, with respect to every prompte template, over here you will specifically have an llm chain because you need to execute thos things

# Memory

person_memory = ConversationBufferMemory(input_key = "name", memory_key = "chat_history")
dob_memory = ConversationBufferMemory(input_key = "person", memory_key = "chat_history")
descr_memory = ConversationBufferMemory(input_key = "dob", memory_key = "description_history")
# everthing is stored in LLMChain




# OPENAI LLMS
llm = OpenAI(temperature = 0.8) 
#temperature - defult=0.7, it has the value b/w 0 to 1. This is just suggesting like how much control the agent should
 #have while providing the response
chain1 = LLMChain(llm = llm, prompt = first_input_prompt, verbose = True, output_key ="person" ,memory = person_memory)
# output_key - to give the output as the next input  to give me multiple results

#Prompt Templates

second_input_prompt = PromptTemplate(
    input_variables = ['person'],
    template = "When was {person} born ?"
)
chain2 = LLMChain(llm = llm, prompt = second_input_prompt, verbose = True, output_key ="dob",memory = dob_memory )

#Prompt Templates

third_input_prompt = PromptTemplate(
    input_variables = ['dob'],
    template = "Mention 5 major events happened around {dob} in the world "
)
chain3 = LLMChain(llm = llm, prompt = third_input_prompt, verbose = True, output_key ="description",memory = descr_memory )
# if you want to combine these two chain either you can run the chain one after the other, otherwise you can combine the chain and then probably set a sequence for that.
# parent_chain = SimpleSequentialChain(chains =[chain1, chain2],verbose = True)
#Problem with SimpleSequentialChain - As we keep on getting the input, it will show you the last input
parent_chain = SimpleSequentialChain(chains =[chain1, chain2,chain3],input_variables = ['name'],output_variables = ['person','dob','description'],verbose = True)


if input_text:
    st.write(parent_chain({"name":input_text}))

    with st.expander("Person Name"):
        st.info(person_memory.buffer)
    
    with st.expander("Major Events"):
        st.info(descr_memory.buffer)