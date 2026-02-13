from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.services.execution_client import ExecutionClient

router = APIRouter()
execution_client = ExecutionClient()

class ExecutionRequest(BaseModel):
    code: str
    language: str
    stdin: str = ""

class ExecutionResponse(BaseModel):
    output: str
    error: str = ""
    execution_time: float
    exit_code: int

@router.post("/run", response_model=ExecutionResponse)
async def execute_code(request: ExecutionRequest):
    """Execute code in a sandboxed environment"""
    try:
        result = await execution_client.execute(
            code=request.code,
            language=request.language,
            stdin=request.stdin
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/{execution_id}")
async def get_execution_status(execution_id: str):
    """Get execution status"""
    # TODO: Implement execution status tracking
    return {"execution_id": execution_id, "status": "completed"}
