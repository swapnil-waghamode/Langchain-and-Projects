# ✍️ AI Blog Generator

A Streamlit app that turns a blog title and a tone into a finished blog post using three chained LangChain prompts, powered by a [Groq](https://groq.com/) model.

This is project 2 in the **Langchain_With_Projects** repository.

## How It Works

The app runs three chains one after another, each feeding the next:

```
Title + Tone  →  Outline  →  Draft  →  Polish  →  Final blog post
```

1. **Outline**: creates an opening line, 4 section headings and 5 key points.
2. **Draft**: writes the full post from the outline in a human, non-robotic style.
3. **Polish**: improves the draft, adds a `#` title and returns clean markdown.

A shared style guide (`HUMAN_STYLE`) is added to the draft and polish prompts. It asks for varied sentence length, contractions, concrete examples, and bans common AI phrases like "delve" and "game-changer".

## Features

- Pick any blog title and one of three tones: `direct`, `normal` or `friendly`
- Spinners show which step is running
- Final post is rendered as markdown
- A "Raw Blog" expander lets you copy the markdown source

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

3. **Configure environment variables**

   Copy `.env.example` to `.env` and set both values:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   MODEL=openai/gpt-oss-20b
   ```

   `MODEL` can be any chat model available on Groq.

## Run the App

```bash
streamlit run projects/2_blog_generator/app.py
```

The app opens in your browser at `http://localhost:8501`.

## Usage

1. Enter a blog title (default: *Why we need to learn Gen-AI in 2026*).
2. Choose a tone.
3. Click **Generate** and wait for the three steps to finish.
4. Read the post, or open **Raw Blog** to copy the markdown.

## Project Structure

```
Langchain_With_Projects/
├── projects/
│   ├── 1_qna_bot/
│   ├── 2_blog_generator/
│   │   ├── app.py        # Streamlit app
│   │   └── README.md     # This file
│   ├── 3_search_weather_agent/
│   ├── 4_email_agent/
│   └── 5_ai_task_manager_agent/
├── .env                  # Your API keys (do not commit)
├── .env.example
└── requirements.txt
```

> **Note:** Keep `.env` in your `.gitignore` so your API key is never pushed to GitHub.