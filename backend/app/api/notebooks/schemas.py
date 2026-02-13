from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class CellBase(BaseModel):
    type: str
    content: str
    output: Optional[str] = None

class NotebookBase(BaseModel):
    title: str

class NotebookCreate(NotebookBase):
    pass

class NotebookResponse(NotebookBase):
    id: str
    cells: List[CellBase] = []
    created_at: str
    updated_at: str
    
    class Config:
        from_attributes = True
