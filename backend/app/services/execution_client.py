import httpx
from app.config import settings

class ExecutionClient:
    def __init__(self):
        self.base_url = settings.EXECUTION_ENGINE_URL
    
    async def execute(self, code: str, language: str, stdin: str = ""):
        """Send code to execution engine for execution"""
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{self.base_url}/execute",
                json={
                    "code": code,
                    "language": language,
                    "stdin": stdin
                },
                timeout=settings.MAX_EXECUTION_TIME
            )
            response.raise_for_status()
            return response.json()
    
    async def get_status(self, execution_id: str):
        """Get execution status"""
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{self.base_url}/status/{execution_id}")
            response.raise_for_status()
            return response.json()
