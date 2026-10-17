# 🤖 AI Task Manager Agent

A Streamlit chat app where you manage your to-do list in plain English. A LangChain agent turns your messages into database operations on a local SQLite database.

This is project 5 in the **Langchain_With_Projects** repository.

## Features

- **Create** tasks with a title, description, priority and due date
- **List and filter** tasks by status or priority
- **Update** any field of a task
- **Delete** tasks by ID
- **Memory**: `InMemorySaver` keeps the conversation context
- **Persistent storage**: tasks are saved in a SQLite database (`todos.db`), so they survive restarts
- **Status icons** in the answers: 🕣 Pending, ⏳ In Progress, ✅ Done

## How It Works

1. `database.py` defines the `Todo` model with SQLAlchemy and creates the table if it doesn't exist.
2. `tools.py` defines four tools the agent can call: `create_todo`, `list_todos`, `updated_todo` and `delete_todo`.
3. `agent.py` builds the agent with `create_agent`, a Groq model, the tools, a system prompt and an `InMemorySaver`. `call_agent()` sends a message and returns the reply.
4. `app.py` is the Streamlit chat UI.

### Task fields

| Field | Values |
|-------|--------|
| `title` | Short text (required) |
| `description` | Optional note |
| `status` | `pending`, `in_progress`, `done` |
| `priority` | `low`, `medium`, `high` |
| `due_date` | Optional date, e.g. `18-10-2026` |
| `created_at` | Set automatically |

## Requirements

- Python 3.9+
- A [Groq](https://console.groq.com/keys) API key

## Setup

1. **Create and activate a virtual environment** (from the repository root)

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Copy `.env.example` to `.env` and add your key:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Run the App

```bash
cd projects/5_ai_task_manager_agent
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

> The database path is `sqlite:///todos.db`, which is relative to the folder you run the command from. Always start the app from the same folder, or you will end up with several separate `todos.db` files.

## Example Prompts

- "Add a task: finish the LangChain project, high priority, due 20-10-2026"
- "Show all pending tasks"
- "Show high priority tasks"
- "Start working on task 3"
- "Mark task 3 as done"
- "Change the due date of task 2 to 25-10-2026"
- "Delete task 4"

## Project Structure

```
Langchain_With_Projects/
├── projects/
│   ├── 1_qna_bot/
│   ├── 2_blog_generator/
│   ├── 3_search_weather_agent/
│   ├── 4_email_agent/
│   ├── 5_ai_task_manager_agent/
│   │   ├── agent.py      # Agent setup, prompt and memory
│   │   ├── tools.py      # Create, list, update and delete tools
│   │   ├── database.py   # SQLAlchemy model and DB setup
│   │   ├── app.py        # Streamlit UI
│   │   ├── todos.db      # SQLite database (created automatically)
│   │   └── README.md     # This file
├── .env                  # Your API key (do not commit)
├── .env.example
└── requirements.txt
```

> **Note:** Keep `.env` and `todos.db` in your `.gitignore` so your API key and personal tasks are not pushed to GitHub.