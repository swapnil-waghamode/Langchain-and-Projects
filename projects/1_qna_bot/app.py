from dotenv import load_dotenv

load_dotenv() 

from langchain_groq import ChatGroq

import streamlit as st

llm = ChatGroq(model="openai/gpt-oss-20b")

# history 

if "messages" not in st.session_state:
  st.session_state.messages = []

# UI

st.subheader("🤖 QnA BOT")

for msg in st.session_state.messages:
  st.chat_message(msg.get("role")).markdown(msg.get("content"))

query = st.chat_input("Ask anything....")

if query:

  st.session_state.messages.append({"role":"user","content":query})

  st.chat_message("user").markdown(query)

  response = llm.invoke(st.session_state.messages)

  st.session_state.messages.append({"role":"ai","content":response.content})

  st.chat_message("ai").markdown(response.content)


