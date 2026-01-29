from typing import Dict, Any
from enum import Enum

class MessageType(Enum):
    """Types of messages in the kernel protocol"""
    EXECUTE_REQUEST = "execute_request"
    EXECUTE_REPLY = "execute_reply"
    STREAM = "stream"
    ERROR = "error"
    STATUS = "status"

class KernelProtocol:
    """Protocol for kernel communication"""
    
    @staticmethod
    def create_execute_request(code: str, stdin: str = "") -> Dict[str, Any]:
        """Create an execute request message"""
        return {
            "msg_type": MessageType.EXECUTE_REQUEST.value,
            "content": {
                "code": code,
                "stdin": stdin
            }
        }
    
    @staticmethod
    def create_execute_reply(
        status: str,
        execution_count: int,
        output: str = "",
        error: str = ""
    ) -> Dict[str, Any]:
        """Create an execute reply message"""
        return {
            "msg_type": MessageType.EXECUTE_REPLY.value,
            "content": {
                "status": status,
                "execution_count": execution_count,
                "output": output,
                "error": error
            }
        }
    
    @staticmethod
    def create_stream_message(name: str, text: str) -> Dict[str, Any]:
        """Create a stream message"""
        return {
            "msg_type": MessageType.STREAM.value,
            "content": {
                "name": name,
                "text": text
            }
        }
    
    @staticmethod
    def create_error_message(ename: str, evalue: str, traceback: list) -> Dict[str, Any]:
        """Create an error message"""
        return {
            "msg_type": MessageType.ERROR.value,
            "content": {
                "ename": ename,
                "evalue": evalue,
                "traceback": traceback
            }
        }
