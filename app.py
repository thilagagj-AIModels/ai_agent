
import streamlit as st
import ollama
from pathlib import Path

css_path = Path(__file__).parent / "static" / "style.css"

with open(css_path, "r", encoding="utf-8") as css_file:
    css = css_file.read()

st.markdown(
    f"<style>{css}</style>",
    unsafe_allow_html=True
)

st.title("My Local AI Chatbot")
st.write("Ask a question and get an AI-generated answer.")

question = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if question.strip():
        with st.spinner("Generating answer..."):
            try:
                response = ollama.chat(
                    model="llama3.2:1b",
                    messages=[
                        {
                            "role": "user",
                            "content": question
                        }
                    ]
                )

                st.subheader("AI Answer")
                st.write(response["message"]["content"])

            except Exception as e:
                st.error(f"Error: {e}")