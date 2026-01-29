from kernels.base.kernel import BaseKernel
from kernels.c.compiler import CCompiler
from typing import Dict, Any

class CKernel(BaseKernel):
    """Kernel for C language execution"""
    
    def __init__(self):
        super().__init__("c")
        self.compiler = CCompiler()
    
    async def execute(self, code: str, stdin: str = "") -> Dict[str, Any]:
        """Execute C code"""
        self.execution_count += 1
        
        # Compile the code
        success, message = self.compile(code)
        if not success:
            return {
                "status": "error",
                "execution_count": self.execution_count,
                "output": "",
                "error": message
            }
        
        # Execute compiled code (to be implemented with execution engine)
        return {
            "status": "ok",
            "execution_count": self.execution_count,
            "output": "Code compiled successfully",
            "error": ""
        }
    
    def compile(self, code: str) -> tuple[bool, str]:
        """Compile C code"""
        return self.compiler.compile(code)
