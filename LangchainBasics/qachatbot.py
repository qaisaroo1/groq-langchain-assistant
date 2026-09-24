import streamlit as st
from langchain.chat_models import init_chat_model
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage,AIMessage
from langchain_core.prompts import ChatPromptTemplate
import os



#Page config
st.set_page_config(page_title="Simple Langchain Chat wth Groq", page_icon="Start")

#Title
st.title("Simple Langchain Chat with Groq")
st.markdown("Learn Langchain Basics with Groq ultra-fast inference!")

with st.sidebar:
    st.header("Settings")

    #Api Key
    api_key= st.text_input("Groq API Key", type="password", help="Get free API key from concole.groq.com")

    #Model Selection
    model_name = st.select_slider(
        "Model",
        ["openai/gpt-oss-20b", "qwen/qwen3.8-27b"]
    )
    #Clear button
    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()
 #Initialize chat history
if "messages" not in  st.session_state:
    st.session_state.messages = []

#Initialize LLm
@st.cache_resource
def get_chain(api_key,model_name):
    if not api_key:
        return None

    #Initialize the groq model
    llm = ChatGroq(
             model_name = model_name,
             temperature=0.7,
             streaming =True)

    #Initialize prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system","You are an helpful assistant powered by Groq. Answer the question clearly and concisely"),
            ("user","{question}")
        ]
    )

    #Initialize Chain
    chat = prompt |llm | StrOutputParser()
    return chat

#get chain
chain= get_chain(api_key,model_name)
if not chain:
    st.warning("Please enter your groq API key")
    st.markdown("[Get your free API key here](https://console.groq.com)")

else:
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    #Input chat
    if question:=st.chat_input("Ask me anything"):
        #add user message to session state
        st.session_state.messages.append({"role":"user","content":question})
        with st.chat_message("user"):
            st.write(question)

    #Generate response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""

        try:
            #Stream response from Groq
            for chunk in chain.stream({"question":question}):
                full_response += chunk
                message_placeholder.markdown(full_response + " ")

            message_placeholder.markdown(full_response)

            #Add to history
            st.session_state.messages.append({"role":"assistant", "content":full_response})

        except Exception as e:
            st.error(f"Error: {str(e)}")    


