from pydantic import BaseModel, Field
from typing import List, Dict, Any, Optional
from datetime import datetime

class WorkflowStep(BaseModel):
    step_id: str
    action: str
    parameters: Dict[str, Any]

class WorkflowCreate(BaseModel):
    name: str
    description: str
    steps: List[WorkflowStep]

class WorkflowResponse(BaseModel):
    id: str
    name: str
    description: str
    steps_json: List[Dict[str, Any]]
    created_at: datetime
    
    class Config:
        from_attributes = True

class TaskRequest(BaseModel):
    description: str

class DocumentRequest(BaseModel):
    content: str = Field(..., description="Text content or URL to process")

class TaskResponse(BaseModel):
    id: str
    status: str
    output_data: Optional[Dict[str, Any]]
    
    class Config:
        from_attributes = True
      
