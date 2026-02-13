from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from runner.executor import Executor

app = FastAPI(title="Execution Engine API")
executor = Executor()

class ExecutionRequest(BaseModel):
    code: str
    language: str
    stdin: str = ""

@app.post("/execute")
async def execute_code(request: ExecutionRequest):
    """Execute code in a sandboxed environment"""
    try:
        result = await executor.execute(
            code=request.code,
            language=request.language,
            stdin=request.stdin
        )
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/health")
async def health():
    return {"status": "healthy"}

@app.get("/status/{execution_id}")
async def get_status(execution_id: str):
    """Get execution status"""
    # TODO: Implement execution status tracking
    return {"execution_id": execution_id, "status": "completed"}
