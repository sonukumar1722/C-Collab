from abc import ABC, abstractmethod
from typing import Dict, Any

class BaseKernel(ABC):
    """Base class for all language kernels"""
    
    def __init__(self, language: str):
        self.language = language
        self.execution_count = 0
    
    @abstractmethod
    async def execute(self, code: str, stdin: str = "") -> Dict[str, Any]:
        """Execute code and return results"""
        pass
    
    @abstractmethod
    def compile(self, code: str) -> tuple[bool, str]:
        """Compile code and return success status and error message"""
        pass
    
    def reset(self):
        """Reset kernel state"""
        self.execution_count = 0
    
    def get_info(self) -> Dict[str, Any]:
        """Get kernel information"""
        return {
            "language": self.language,
            "execution_count": self.execution_count
        }
