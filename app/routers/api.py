from fastapi import APIRouter, Depends, HTTPException, Security
from fastapi.security import APIKeyHeader
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
import json

from app.database import get_db
from app.models import Workflow, Task
from app.schemas import WorkflowCreate, WorkflowResponse, TaskRequest, TaskResponse, DocumentRequest
from app.services.llm_service import LLMService
from app.config import settings

router = APIRouter(prefix="/api/v1")
api_key_header = APIKeyHeader(name="X-API-Key")

def get_api_key(api_key: str = Security(api_key_header)):
    """Simple API Key validation."""
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Could not validate credentials")
    return api_key

@router.post("/workflows/create", response_model=WorkflowResponse)
async def create_workflow(
    workflow_in: WorkflowCreate, 
    db: AsyncSession = Depends(get_db),
    api_key: str = Depends(get_api_key)
):
    """Creates and stores a new automation workflow."""
    steps_dict = [step.model_dump() for step in workflow_in.steps]
    new_workflow = Workflow(
        name=workflow_in.name,
        description=workflow_in.description,
        steps_json=steps_dict
    )
    db.add(new_workflow)
    await db.commit()
    await db.refresh(new_workflow)
    return new_workflow

@router.post("/automate/task", response_model=TaskResponse)
async def automate_task(
    request: TaskRequest,
    db: AsyncSession = Depends(get_db),
    api_key: str = Depends(get_api_key)
):
    """Executes a single AI-powered task and tracks it in DB."""
    # 1. Create pending task
    task = Task(task_type="ai_automation", input_data=request.description)
    db.add(task)
    await db.commit()
    
    # 2. Execute via LLM
    llm = LLMService()
    try:
        result = await llm.execute_task(request.description)
        task.output_data = result
        task.status = "completed"
    except Exception as e:
        task.status = "failed"
        task.output_data = {"error": str(e)}
        
    task.completed_at = datetime.utcnow()
    await db.commit()
    await db.refresh(task)
    
    return task

@router.post("/process/document")
async def process_document(
    request: DocumentRequest,
    api_key: str = Depends(get_api_key)
):
    """Intelligently processes and structures document text."""
    llm = LLMService()
    try:
        return await llm.process_document(request.content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Processing failed: {str(e)}")

@router.post("/workflows/{workflow_id}/execute")
async def execute_workflow(
    workflow_id: str,
    db: AsyncSession = Depends(get_db),
    api_key: str = Depends(get_api_key)
):
    """Executes a sequenced workflow."""
    result = await db.execute(select(Workflow).where(Workflow.id == workflow_id))
    workflow = result.scalar_one_or_none()
    
    if not workflow:
        raise HTTPException(status_code=404, detail="Workflow not found")
        
    # In a real distributed system, this would push to Celery/RabbitMQ
    # For this fast-paced demo, we execute sequentially
    execution_results = []
    llm = LLMService()
    
    for step in workflow.steps_json:
        if step['action'] == 'summarize':
            res = await llm.execute_task(f"Summarize this: {step['parameters'].get('text', '')}")
            execution_results.append({step['step_id']: res})
            
    return {
        "workflow_id": workflow_id,
        "status": "completed",
        "results": execution_results
    }
  
