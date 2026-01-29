import asyncio
from typing import Optional

class OutputCollector:
    """Collect and manage output from code execution"""
    
    def __init__(self, max_output_size: int = 1024 * 1024):  # 1MB default
        self.max_output_size = max_output_size
    
    def collect_output(self, output: str) -> str:
        """Collect and truncate output if needed"""
        if len(output) > self.max_output_size:
            return output[:self.max_output_size] + "\n... (output truncated)"
        return output
    
    def parse_output(self, raw_output: str) -> dict:
        """Parse raw output into structured format"""
        lines = raw_output.split('\n')
        
        stdout = []
        stderr = []
        
        for line in lines:
            if line.startswith('[STDERR]'):
                stderr.append(line[8:])
            else:
                stdout.append(line)
        
        return {
            "stdout": '\n'.join(stdout),
            "stderr": '\n'.join(stderr)
        }
    
    def format_error(self, error: Exception) -> str:
        """Format error message"""
        return f"Error: {type(error).__name__}: {str(error)}"
