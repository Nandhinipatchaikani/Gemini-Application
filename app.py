import streamlit as st
import google.generativeai as genai

st.title("HI WELCOME TO THE APP - SURYA")

genai.configure(api_key="AIzaSyAuRvJW_U07AUx3BACR8NggK0L1ZAxcA-g")

text=st.text_input("Ask your query here") 

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click Here"):
    response = chat.send_message(text)
    st.write(response.text)
