from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver
from langchain_groq import ChatGroq
from tools import *
from database import init_db

from dotenv import load_dotenv
load_dotenv()

# create table if not exist
init_db()

llm = ChatGroq(model="openai/gpt-oss-20b")

ALL_TOOLS = [create_todo,list_todos,updated_todo,delete_todo]

SYSTEM_PROMPT = """You are a smart and friendly Todo Manager AI assistant.

You help users manage their tasks using a database. You can:
  - Create new tasks
  - List / filter tasks by status or priority
  - Update any field of a task (title, description, status, priority, due date)
  - Delete tasks by ID

Guidelines:
- Always confirm what action you took after each tool call.
- When listing todos, present them in a readable table format.
- "mark as done"      → update with status='done'
- "start working on"  → update with status='in_progress'
- "show pending"      → list with status='pending'
- "high priority"     → list with priority='high'
- Be concise and friendly.

Status values:   pending | in_progress | done

Use Status Icons with staus value: 
  pending - 🕣 Pnding 
  in_progress - ⏳ In Progress
  done - ✅ Done
Priority values: low | medium | high
"""

memory = InMemorySaver()

def createAgent():

  agent = create_agent(
    model=llm,
    tools= ALL_TOOLS,
    system_prompt=SYSTEM_PROMPT,
    checkpointer= memory
  )

  return agent


# Calling agent
def call_agent(query:str):

  agent = createAgent()

  res = agent.invoke(
    {
      "messages":[{"role":"user","content":query}]
    },
    {"configurable":{"thread_id":"1"}}
  )

  answer = res["messages"][-1].content
  return answer