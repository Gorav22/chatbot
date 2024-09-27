import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
from PIL import Image
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


def get_gemini_response(input_prompt,input):
    model=genai.GenerativeModel('gemini-1.5-flash-002')
    response=model.generate_content([input_prompt,input])
    return response.text

st.header("DisasBot")

input=st.text_input("Enter the prompt here")

submit=st.button("Tell me Solution ")

input_prompt="""
You are an disaster related chatbot that can give advice related to chatbot and can tell precaution do's and don'ts etc related to disasters.
  give me the solution of the following question. and if the question is not related  to disaster then just say sorry but i can't help you for the following question.
  
"""

if submit:
    response=get_gemini_response(input_prompt,input)
    st.write(response)

