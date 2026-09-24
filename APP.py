import streamlit as st
import ollama

st.title("My AI Chatbot")

prompt = st.text_input("Ask something:")

if st.button("Send"):
    response = ollama.chat(
        model="llama3.2",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    st.write(response["message"]["content"])