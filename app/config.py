import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    PROJECT_NAME: str = "Smart Workflow Automation System"
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./seyah_demo.db")
    GROQ_API_KEY: str = os.getenv("GROQ_API_KEY", "dummy_key")
    API_KEY: str = os.getenv("API_KEY", "seyah-demo-key-2026")

    class Config:
        env_file = ".env"

settings = Settings()
