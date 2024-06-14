#made by shambhavi tiwari @2024

from dotenv import load_dotenv
load_dotenv() #loads the env vars from .env
import streamlit as st
import os #picking up env vars
from PIL import Image
import google.generativeai as genai

genai.configure(api_key="YOUR_GEMINI_API_KEY") #config.

#function to load gemini pro vision
model=genai.GenerativeModel('gemini-1.5-flash')
def get_gemini_response(Input,Image,prompt):
    response=model.generate_content((Input,Image[0],prompt))
    return response.text
def input_image_details(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts=[
            {
                "mime_type":uploaded_file.type,
                "data":bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("no file uploaded")

#init streamlit
st.set_page_config(page_title="Multilanguage Invoice Extractor")
st.sidebar.header("RoboBill🦾")
st.sidebar.write("Made by Shambhavi Tiwari.")
st.sidebar.write("Assistant used is Gemini Pro Vision.")
st.header("RoboBill 🦾")
st.subheader("Manage your expenses with the help of the robot!")
input=st.text_input("What do you want me to do? ",key="input")
uploaded_file = st.file_uploader("Choose an image.", type=["jpg","jpeg","png"])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image", use_column_width=True)

ssubmit=st.button("Let's go!")

Input_prompt="""
You are an expert in understanding invoices. 
We will upload a image as invoices 
and you will have to answer any questions based on the uploaded invoice image
Make sure to greet the user first and then provide the information as suited.
Make sure to keep the font uniform and give the items list in a point-wise format.
At the end, make sure to repeat the name of our app "RoboBill 🦾" and ask the user to use it again.
"""

#button prog
if ssubmit:
    image_data=input_image_details(uploaded_file)
    response=get_gemini_response(Input_prompt,image_data,input)
    st.subheader("Here's what you need to know:")
    st.write(response)

#thanks for visiting!
