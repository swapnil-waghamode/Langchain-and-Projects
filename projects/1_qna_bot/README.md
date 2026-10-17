# 🤖 QnA Bot

A simple chatbot built with [Streamlit](https://streamlit.io/) and [LangChain](https://www.langchain.com/), powered by the `openai/gpt-oss-20b` model through [Groq](https://groq.com/).

This is project 1 in the **Langchain_With_Projects** repository.

## Features

- Chat interface with a text input at the bottom
- Conversation history kept for the whole session
- Fast responses from Groq-hosted models

## Requirements

- Python 3.9+
- A Groq API key ([get one here](https://console.groq.com/keys))

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

3. **Add your API key**

   Copy `.env.example` to `.env` and fill in your key:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Run the App

```bash
streamlit run projects/1_qna_bot/app.py
```

The app opens in your browser at `http://localhost:8501`.

## How It Works

1. Chat messages are stored in `st.session_state.messages`.
2. Each time you send a question, the full history is passed to the model through `ChatGroq`.
3. The reply is added to the history and shown in the chat window.

## Project Structure

```
Langchain_With_Projects/
├── projects/
│   ├── 1_qna_bot/
│   │   ├── app.py        # Streamlit app
│   │   └── README.md     # This file
│   ├── 2_blog_generator/
│   ├── 3_search_weather_agent/
│   ├── 4_email_agent/
│   └── 5_ai_task_manager_agent/
├── .env                  # Your API keys (do not commit)
├── .env.example
├── requirements.txt
└── basic_langchain.ipynb
```

> **Note:** Make sure `.env` is listed in `.gitignore` so your API key is never pushed to GitHub.