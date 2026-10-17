from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent
from langchain_groq import ChatGroq
from tools import ALL_TOOLS

# for providing memory to our agent will import InMemorySaver
from langgraph.checkpoint.memory import InMemorySaver

import os

MODEL = os.getenv("MODEL")

# Creating agent

def get_agent():
  """Get Agent with google search and weather search abilities."""
  return create_agent(
    model=ChatGroq(model = MODEL),
    tools= ALL_TOOLS,
    system_prompt= (
       "You are a research assistant with google search and weather tools."
       "Use 'google_search' for quick search on google"
       "for deep search that may take several minutes"
       "If user is looking for weather details like temperature, humidity, wind speed, air quality or any other weather details then call the 'weather_tool' to get the real time weather data."
    ),
    checkpointer = InMemorySaver()
  )

# agent = get_agent()

# while True:

#   query = input("User: ")

#   if query == "exit":
#     break 

#   res = agent.invoke({"messages":[{"role":"user", "content":query}]})

#   ans = res["messages"][-1].content

#   print("AI: ",ans)