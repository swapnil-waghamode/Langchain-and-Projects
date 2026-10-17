from agent import get_agent
import streamlit as st

st.subheader(":rainbow[📧 EMAIL AGENT]")
st.caption(":rainbow[Send an email to any email address.]")

if "messages" not in st.session_state:
  st.session_state.messages = []

if "agent" not in st.session_state:
  st.session_state.agent = get_agent()

for msg in st.session_state.messages:
  st.chat_message(msg.get("role")).markdown(msg.get("content"))


query = st.chat_input("email context...")

if query:

  st.session_state.messages.append({"role":"user","content":query})
  st.chat_message("user").markdown(query)

  response = st.session_state.agent.invoke(
    {"messages":[{"role":"user","content":query}]},
    {"configurable":{"thread_id":"email_1"}}
  )

  ans = response["messages"][-1].content
  
  st.session_state.messages.append({"role":"ai","content":ans})
  st.chat_message("ai").markdown(ans)



