from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging

from app.database import engine, Base, AsyncSessionLocal
from app.routers import api
from app.models import Workflow, User

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def seed_database():
    """Seeds the DB with realistic automation scenarios for Seyah Space."""
    async with AsyncSessionLocal() as db:
        # Check if empty
        from sqlalchemy.future import select
        res = await db.execute(select(User).limit(1))
        if res.scalar_one_or_none():
            return # Already seeded

        logger.info("Seeding database with default Seyah Space workflows...")
        user = User(email="demo@seyah.space", name="Seyah Evaluator")
        db.add(user)

        # Seed Workflow
        wf1 = Workflow(
            name="Daily News Summary",
            description="Aggregates and summarizes top AI news",
            steps_json=[
                {"step_id": "1", "action": "fetch_rss", "parameters": {"url": "ai-news"}},
                {"step_id": "2", "action": "summarize", "parameters": {"text": "AI startup raises $10M for workflow automation tools..."}}
            ]
        )
        db.add(wf1)
        await db.commit()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Create tables on startup (bypassing Alembic for immediate run requirements)
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    await seed_database()
    yield
    # Cleanup
    await engine.dispose()

app = FastAPI(
    title="Seyah Space - Smart Workflow Automation",
    description="Production-ready API for AI-powered workflow orchestration.",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api.router)

@app.get("/")
async def root():
    return {"message": "Seyah Space Automation API is running. Check /docs for endpoints."}
  
