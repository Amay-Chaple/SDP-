# rzFaqrq2VhO2lUQGX4Fhzsg87srE3Zyn - mistral api

import os;
import streamlit as st;
from mistralai import Mistral
st.title("Free Mistral API Chatbot");

# Load api key
MISTRAL_API_KEY = st.secrets["MISTRAL"]["api_key"];

if not MISTRAL_API_KEY:
    st.error("! Add your key in .streamlit/secrets.toml");
    st.stop();

client = Mistral(api_key="rzFaqrq2VhO2lUQGX4Fhzsg87srE3Zyn");

# Chat History in session
if "history" not in st.session_state:
    st.session_state["history"] = [];

# User Input

user_input = st.text_input("Enter your message:")

def get_mistral_response(user_message):
    message=[
        {"role": "system","content":"You are a helpful assistant."}
         {"role": "user","content":user_message}
    ]
    
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=messages,
        response_format={"type":"text"}
    )
    return response

if user_input:
    st.session_state.history.append({"role":"user","content": user_input})
    
    with st.spinner("Thinking..."):
        reply = get_mistral_response(user_input)
        st.session_state.history.append({"role":"assistant","content": reply})
        
        for chat in st.session_state.history:
            if chat["role"]=="user":
                st.markdown(f"**You:**{chat['content']}")
            else:
                st.markdown(f"**AI:**{chat['content']}")
                