# 🦜 Langchain With Projects

A hands-on collection of small LangChain projects, from a basic chatbot to tool-using agents with memory and a database. Every project has a Streamlit chat UI and runs on a [Groq](https://groq.com/) model.

## Projects

| # | Project | What it does | Key concepts |
|---|---------|--------------|--------------|
| 1 | [QnA Bot](projects/1_qna_bot) | Simple chatbot that remembers the conversation | `ChatGroq`, Streamlit session state |
| 2 | [Blog Generator](projects/2_blog_generator) | Turns a title and tone into a finished blog post | Prompt templates, chains, `StrOutputParser` |
| 3 | [Search & Weather Agent](projects/3_search_weather_agent) | Searches the web and checks the weather in real time | Agents, tools, `InMemorySaver` memory |
| 4 | [Email Agent](projects/4_email_agent) | Drafts an email, asks for approval, then sends it via Gmail | Tool calling, human-in-the-loop approval, SMTP |
| 5 | [AI Task Manager Agent](projects/5_ai_task_manager_agent) | Manages a to-do list in plain English | Agent with CRUD tools, SQLAlchemy, SQLite |

The notebook `basic_langchain.ipynb` covers the LangChain basics used across the projects.

## Tech Stack

- [LangChain](https://www.langchain.com/) and [LangGraph](https://www.langchain.com/langgraph) for chains, agents and memory
- [Groq](https://groq.com/) for fast LLM inference
- [Streamlit](https://streamlit.io/) for the chat interfaces
- [SQLAlchemy](https://www.sqlalchemy.org/) with SQLite for storage (project 5)
- Nimble search and OpenWeather APIs (project 3)

## Getting Started

1. **Clone the repository**

   ```bash
   git clone https://github.com/swapnil-waghamode/Langchain-and-Projects.git
   cd Langchain-and-Projects
   ```

2. **Create and activate a virtual environment**

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up your environment variables**

   Copy `.env.example` to `.env` and fill in the keys you need:

   ```env
   GROQ_API_KEY=your_groq_api_key_here
   MODEL=openai/gpt-oss-20b

   # Project 3: Search & Weather Agent
   NIMBLE_API_KEY=your_nimble_api_key_here
   WEATHER_API_KEY=your_openweather_api_key_here

   # Project 4: Email Agent
   EMAIL_SENDER=your_gmail_address@gmail.com
   EMAIL_APP_PASSWORD=your_gmail_app_password
   ```

   Only `GROQ_API_KEY` is needed for every project. The others are needed only by the project noted above them.

## Running a Project

Go into a project folder and start it with Streamlit:

```bash
cd projects/1_qna_bot
streamlit run app.py
```

Replace `1_qna_bot` with any project folder. The app opens at `http://localhost:8501`.

## Where to Get API Keys

| Key | Link |
|-----|------|
| Groq | https://console.groq.com/keys |
| Nimble | https://www.nimbleway.com/ |
| OpenWeather | https://openweathermap.org/api |
| Gmail App Password | https://myaccount.google.com/apppasswords |

## Repository Structure

```
Langchain-and-Projects/
├── projects/
│   ├── 1_qna_bot/
│   ├── 2_blog_generator/
│   ├── 3_search_weather_agent/
│   ├── 4_email_agent/
│   ├── 5_ai_task_manager_agent/
│   └── todos.db
├── basic_langchain.ipynb
├── requirements.txt
├── .env.example
└── .gitignore
```

## Security Notes

- Never commit your `.env` file. Keep it listed in `.gitignore`.
- Use a Gmail **App Password** for project 4, never your real password.
- `todos.db` holds your personal tasks, so consider adding it to `.gitignore` as well.

## Learning Path

If you are following along, the order of the projects builds up step by step: a plain chat model (1), then prompt chains (2), then agents with tools and memory (3), then actions with side effects (4), and finally agents backed by a database (5).
