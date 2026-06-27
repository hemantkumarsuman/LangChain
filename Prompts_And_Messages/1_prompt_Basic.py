from langchain_google_genai import ChatGoogleGenerativeAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

user_input = st.text_input("Enter your query:")

if st.button("Generate"):
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0.2)

    result = model.invoke(user_input)
    st.write(result.content)