import streamlit as st
import google.generativeai as genai

st.title("HI THERE ! IT'S NANDS HERE")

genai.configure(api_key="AIzaSyAuRvJW_U07AUx3BACR8NggK0L1ZAxcA-g")

text=st.text_input("Enter your question") 

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click Here"):
    response = chat.send_message(text)
    st.write(response.text)
