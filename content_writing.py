import openai
from openai import OpenAI
import streamlit as st
import pandas as pd
import os
 
st.header("Content generation / Essay Writing")

with st.sidebar:
  usr_title = st.text_input("Title : ","Financial Literacy for Board of Directors")
  inp_context = st.radio("",["Indian context","Global context"],horizontal = True)
  inp_level = st.radio("",["Detailed","Simple"],horizontal = True)
  st.header("Sub titles")
  sub_heading = ["Project objective and Goal", "Introduction and Context", "Project Scope- how its implementation will help the organization", "The Project-specific details of the project and its implementation strategy", "Description of the deliverables, the timeframe and estimates of resources for execution", "Conclusion- Key findings & recommendations", "Acknowledgements", "Appendices and References"]
  prompt_inp = []
  key = os.environ.get('API_KEY')
  st.write("Key-"+str(key))
  for i in sub_heading:
    inp = st.text_input("",i,label_visibility="collapsed")
    prompt_inp.append(inp)

client = OpenAI(api_key = "")
context = "I am preparing a dissertation on "+usr_title

gen_content = []

for i in range(len(prompt_inp)):
  usr_input = "Give me detailed, atleast 300 words of content for " + usr_title + " under the subheading " + prompt_inp[i] + " under the " + inp_context + ". Don't include the conclusion"
  completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
      {"role": "system", "content": context},
      {"role": "user", "content": usr_input},
  ]
  )
  st.header(prompt_inp[i])
  st.write(completion.choices[0].message.content)
  gen_content.append(completion.choices[0].message.content)
