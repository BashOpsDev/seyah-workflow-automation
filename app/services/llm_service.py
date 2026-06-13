import json
import logging
from groq import AsyncGroq
from app.config import settings

logger = logging.getLogger(__name__)

# Fallback in-memory cache if Redis isn't configured for the demo
_cache = {}

class LLMService:
    def __init__(self):
        # We use Groq for fast inference, perfect for workflow execution
        self.client = AsyncGroq(api_key=settings.GROQ_API_KEY)
        self.model = "mixtral-8x7b-32768" # Fast and capable model

    async def execute_task(self, task_description: str) -> dict:
        """Executes a general AI task with structured JSON output."""
        cache_key = f"task_{hash(task_description)}"
        if cache_key in _cache:
            return _cache[cache_key]

        system_prompt = (
            "You are an intelligent workflow automation assistant. "
            "Execute tasks efficiently and return ONLY valid JSON. "
            "Structure: {'summary': '...', 'action_items': [], 'confidence_score': 0.0}"
        )
        
        try:
            response = await self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": task_description}
                ],
                model=self.model,
                response_format={"type": "json_object"}
            )
            
            result = json.loads(response.choices[0].message.content)
            _cache[cache_key] = result
            return result
        except Exception as e:
            logger.error(f"LLM Task Execution failed: {str(e)}")
            raise e

    async def process_document(self, content: str) -> dict:
        """Extracts key information from documents."""
        system_prompt = (
            "Analyze the following text. Extract the main entities, "
            "summarize the core message in one sentence, and categorize it. "
            "Return ONLY JSON: {'category': '...', 'summary': '...', 'entities': []}"
        )
        
        try:
            response = await self.client.chat.completions.create(
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": content}
                ],
                model=self.model,
                response_format={"type": "json_object"}
            )
            return json.loads(response.choices[0].message.content)
        except Exception as e:
            logger.error(f"Document processing failed: {str(e)}")
            raise e
          
