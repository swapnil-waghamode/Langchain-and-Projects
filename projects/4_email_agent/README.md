# 📧 Email Agent

A Streamlit chat app backed by a LangChain agent that writes and sends emails through Gmail. You tell it who to email and why, it drafts the message, shows it to you, and only sends after you approve.

This is project 4 in the **Langchain_With_Projects** repository.

## Features

- **Conversational flow**: the agent asks for the recipient's address and the reason for the email, one thing at a time
- **Draft and approval**: it shows you the draft, applies your edits, and sends only after you approve
- **Memory**: `InMemorySaver` keeps the conversation, so it won't ask for details you already gave
- **Gmail sending**: uses `smtplib` over SSL with a Gmail App Password
- **Streamlit chat UI** with message history

## How It Works

1. `tools.py` defines the `send_email` tool, which sends mail through Gmail's SMTP server.
2. `agent.py` builds the agent with `create_agent`, a Groq model, the tool, a system prompt and an `InMemorySaver` checkpointer.
3. `app.py` is the Streamlit UI. It creates the agent once and keeps it in `st.session_state`, and sends each message with a `thread_id` so the conversation stays together.

The agent never invents an email address or a reason. If either is missing, it asks.

## Requirements

- Python 3.9+
- A [Groq](https://console.groq.com/keys) API key
- A Gmail account with 2-Step Verification turned on
- A Gmail [App Password](https://myaccount.google.com/apppasswords) (your normal Gmail password will not work)

## Setup

All commands are run from the **repository root** (`Langchain_With_Projects`).

1. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # On Windows: .venv\Scripts\activate
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment variables**

   Copy `.env.example` to `.env` and fill in your values:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   MODEL=openai/gpt-oss-20b
   EMAIL_SENDER=your_gmail_address@gmail.com
   EMAIL_APP_PASSWORD=your_16_character_app_password
   ```

   > Never hardcode the sender address or password in `tools.py`, and never commit them to GitHub.

## Run the App

The imports in `app.py` are relative to its own folder, so run it from inside the project folder:

```bash
cd projects/4_email_agent
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

## Example Conversation

```
You:   Send an email to alex@example.com
Agent: What is the email about?
You:   Ask him to move tomorrow's meeting to 4 PM
Agent: [shows subject and body draft] Want any changes?
You:   Looks good, send it
Agent: Sent to alex@example.com: "Moving tomorrow's meeting to 4 PM"
```

## Project Structure

```
Langchain_With_Projects/
├── projects/
│   ├── 1_qna_bot/
│   ├── 2_blog_generator/
│   ├── 3_search_weather_agent/
│   ├── 4_email_agent/
│   │   ├── agent.py      # Agent setup, model, prompt and memory
│   │   ├── tools.py      # Gmail send_email tool
│   │   ├── app.py        # Streamlit UI
│   │   └── README.md     # This file
│   └── 5_ai_task_manager_agent/
├── .env                  # Your API keys (do not commit)
├── .env.example
└── requirements.txt
```

> **Note:** Keep `.env` in your `.gitignore` so your credentials are never pushed to GitHub.