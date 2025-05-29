from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()

client = OpenAI()

initial_message = [
        {"role": "system","content":"You are a trip planner,you are an expert in world tourism,food,location,events.hotels etc;you are able to guide users plan their trips;you should respong professionally;your name is dubai Tripzy;response shouldn't exceed 200 words;first ask questions to users and help regarding their dates,number of people,preferences etc to help them plan their trip;analyze the answers to the queations,finally give a daywise itinenary;deal with user professionaly"},
        {
            "role":"assistant",
            "content":"Hi there!,i'm Tripzy,your expert trip planner,Ready to help you plan the perfect getaway- where are we headed?"
        }
   ]

def get_response_from_llm(messages):
    completion = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=messages
)

    return completion.choices[0].message.content


   
if "messages" not in st.session_state:
    st.session_state.messages = initial_message

st.title("TRAVELEXA")

for message in st.session_state.messages:
 if message["role"]!="system":
     with st.chat_message(message["role"]):
      st.markdown(message["content"])

user_message = st.chat_input("enter your message")
if user_message:
    new_message={
            "role":"user",
            "content":user_message
        }
    st.session_state.messages.append(new_message)
    with st.chat_message(new_message["role"]):
      st.markdown(new_message["content"])


    response = get_response_from_llm(st.session_state.messages)
    if response:
        response_message={
            "role":"assistant",
            "content":response
        }
        st.session_state.messages.append(response_message)
        with st.chat_message(response_message["role"]):
           st.markdown(response_message["content"])
