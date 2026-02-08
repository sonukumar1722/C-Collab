# core/protocol/schemas.py

from pydantic import BaseModel
from typing import Optional
from core.protocol.message_types import MessageType

class ExecuteRequest(BaseModel):
    type: MessageType
    request_id: str
    session_id: str
    language: str
    code: str
    timeout: Optional[int] = 3

class ExecuteResponse(BaseModel):
    type: MessageType
    request_id: str
    execution_count: int
    status: str
    stdout: str
    stderr: str
