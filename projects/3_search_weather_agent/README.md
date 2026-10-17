# 🔎 Google Search + Weather Agent

A Streamlit chat app backed by a LangChain agent that can search the web in real time and look up weather details. The agent remembers the conversation, so you can ask follow-up questions.

This is project 3 in the **Langchain_With_Projects** repository.

## Features

- **Web search tool** (`google_search`): uses Nimble search to fetch the top 5 results with deep search enabled, returned as markdown
- **Weather tool** (`weather_tool`): looks up a city through the OpenWeather API
- **Conversation memory**: `InMemorySaver` keeps the chat history for the session
- **Streamlit chat UI** with message history

## How It Works

1. `tools.py` defines the two tools and exposes them as `ALL_TOOLS`.
2. `agent.py` builds the agent with `create_agent`, a Groq model, the tools, a system prompt and an `InMemorySaver` checkpointer.
3. `app.py` is the Streamlit UI. It creates the agent once and stores it in `st.session_state`, so the agent and its memory aren't recreated on every rerun. Each request is sent with a `thread_id` so the checkpointer can keep the conversation together.

The model decides on its own which tool to call: search for general questions, weather for temperature, humidity, wind and similar questions.

## Requirements

- Python 3.9+
- A [Groq](https://console.groq.com/keys) API key
- A [Nimble](https://www.nimbleway.com/) API key for web search
- An [OpenWeather](https://openweathermap.org/api) API key

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

   Copy `.env.example` to `.env` and fill in your keys:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   MODEL=openai/gpt-oss-20b
   NIMBLE_API_KEY=your_nimble_api_key_here
   WEATHER_API_KEY=your_openweather_api_key_here
   ```

## Run the App

The imports in `app.py` are relative to its own folder, so run it from inside the project folder:

```bash
cd projects/3_search_weather_agent
streamlit run app.py
```

The app opens in your browser at `http://localhost:8501`.

## Example Prompts

- "What are the latest updates on the Chandrayaan mission?"
- "What's the weather in Chennai right now?"
- "Search for the best Python libraries for agents, then tell me the weather in Trichy."

## Project Structure

```
Langchain_With_Projects/
├── projects/
│   ├── 1_qna_bot/
│   ├── 2_blog_generator/
│   ├── 3_search_weather_agent/
│   │   ├── agent.py      # Agent setup, model, prompt and memory
│   │   ├── tools.py      # Search and weather tools
│   │   ├── app.py        # Streamlit UI
│   │   └── README.md     # This file
│   ├── 4_email_agent/
│   └── 5_ai_task_manager_agent/
├── .env                  # Your API keys (do not commit)
├── .env.example
└── requirements.txt
```

> **Note:** Keep `.env` in your `.gitignore` so your API keys are never pushed to GitHub.