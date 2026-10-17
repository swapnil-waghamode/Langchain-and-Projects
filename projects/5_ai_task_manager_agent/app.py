from agent import call_agent
import streamlit as st

st.subheader(":rainbow[🤖 AI Task Manager]")
st.caption(":rainbow[manage your task with AI]")

if "messages" not in st.session_state:
  st.session_state.messages = []

for msg in st.session_state.messages:
  st.chat_message(msg.get("role")).markdown(msg.get("content"))

query = st.chat_input("manage your task..")

if query:

  st.session_state.messages.append({"role":"user","content":query})
  st.chat_message("user").markdown(query)

  ans = call_agent(query)

  st.chat_message("ai").markdown(ans)
  st.session_state.messages.append({"role":"ai","content":ans})