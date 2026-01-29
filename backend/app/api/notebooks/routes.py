from fastapi import APIRouter, HTTPException
from typing import List
from app.api.notebooks.schemas import NotebookCreate, NotebookResponse
from app.api.notebooks.service import NotebookService

router = APIRouter()
notebook_service = NotebookService()

@router.get("/", response_model=List[NotebookResponse])
async def get_notebooks():
    """Get all notebooks"""
    return notebook_service.get_all_notebooks()

@router.post("/", response_model=NotebookResponse)
async def create_notebook(notebook: NotebookCreate):
    """Create a new notebook"""
    return notebook_service.create_notebook(notebook)

@router.get("/{notebook_id}", response_model=NotebookResponse)
async def get_notebook(notebook_id: str):
    """Get a specific notebook"""
    notebook = notebook_service.get_notebook(notebook_id)
    if not notebook:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return notebook

@router.put("/{notebook_id}", response_model=NotebookResponse)
async def update_notebook(notebook_id: str, notebook: NotebookCreate):
    """Update a notebook"""
    updated = notebook_service.update_notebook(notebook_id, notebook)
    if not updated:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return updated

@router.delete("/{notebook_id}")
async def delete_notebook(notebook_id: str):
    """Delete a notebook"""
    deleted = notebook_service.delete_notebook(notebook_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Notebook not found")
    return {"message": "Notebook deleted successfully"}
