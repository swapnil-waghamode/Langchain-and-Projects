from agent import get_agent
import streamlit as st

# UI
st.subheader(" :rainbow[Google Search Agent ⌕]")

st.caption(":rainbow[Search anything with google search capability and get realtime weather details as well.]")

if "messages" not in st.session_state:
  st.session_state.messages = []

# This is to avoid agent and InMemorySaver recreation for every re-run.
if "agent" not in st.session_state:
  st.session_state.agent = get_agent()

for msg in st.session_state.messages:
  st.chat_message(msg.get("role")).markdown(msg.get("content"))

query = st.chat_input("Ask anything...")

if query:

  st.session_state.messages.append({"role":"user","content":query})
  st.chat_message("user").markdown(query)

  # Note for checkpointer we need to pass thread_id in configurable
  res = st.session_state.agent.invoke(
    {"messages":[{"role":"user","content":query}]},
    {"configurable":{"thread_id":"chat_1"}}
    )
  ans = res["messages"][-1].content

  st.session_state.messages.append({"role":"ai","content":ans})
  st.chat_message("ai").markdown(ans)