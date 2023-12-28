from dotenv import load_dotenv
import os
import streamlit as st
from PIL import Image
from IPython.display import Markdown
import google.generativeai as genai
load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")
# Use the API key as needed
genai.configure(api_key=api_key)

print("Starting")
# for m in genai.list_models():
#   print(m.name)
#   if 'generateContent' in m.supported_generation_methods:
#     print(m.name)
model = genai.GenerativeModel('gemini-pro')

response = model.generate_content("What is the meaning of life?")
# print(response.text)

# def to_markdown(text):
#   text = text.replace('•', '  *')
#   return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))


print(response.text)