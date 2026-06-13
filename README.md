# Seyah Space - Smart Workflow Automation System

This is a production-ready demonstration backend built for the **Seyah Space** application. It showcases a modern, scalable approach to AI-powered workflow optimization, utilizing a high-performance stack designed for fast iteration and reliability.

## 🚀 Features
- **Intelligent Workflow Engine:** Create, store, and execute multi-step automations.
- **AI Task Automation:** Native integration with LLMs (Groq `mixtral-8x7b-32768`) for complex reasoning and summarization returning structured JSON.
- **Asynchronous Architecture:** Built from the ground up with FastAPI and `asyncio` for high concurrency.
- **Production-Grade DB Abstraction:** SQLAlchemy ORM with async drivers, easily toggleable between SQLite (for rapid local testing) and PostgreSQL.
- **Security:** API Key authentication and robust Pydantic validation.

## 🛠️ Tech Stack
- **Framework:** FastAPI, Python 3.10+
- **Database:** PostgreSQL / SQLite (via SQLAlchemy Async)
- **AI Integration:** Groq API
- **Validation:** Pydantic V2

## 📦 Installation & Immediate Run

1. **Clone & Install Dependencies**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
