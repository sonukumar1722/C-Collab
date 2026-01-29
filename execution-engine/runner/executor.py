import asyncio
import time
from typing import Dict, Optional
from .container_manager import ContainerManager
from .resource_limiter import ResourceLimiter
from .output_collector import OutputCollector

class Executor:
    def __init__(self):
        self.container_manager = ContainerManager()
        self.resource_limiter = ResourceLimiter()
        self.output_collector = OutputCollector()
    
    async def execute(
        self,
        code: str,
        language: str,
        stdin: str = "",
        timeout: int = 30,
        memory_limit: str = "512m"
    ) -> Dict:
        """Execute code in a sandboxed container"""
        start_time = time.time()
        
        # Select appropriate image
        image = f"c-notebook-{language}:latest"
        
        try:
            # Create container with resource limits
            container_id = self.container_manager.create_container(
                image=image,
                command="/bin/sh -c 'echo \"$CODE\" > /tmp/code && gcc /tmp/code -o /tmp/program && /tmp/program'",
                environment={"CODE": code},
                mem_limit=memory_limit,
                network_disabled=True
            )
            
            # Wait for execution with timeout
            await asyncio.sleep(min(timeout, 30))
            
            # Collect output
            output = self.container_manager.get_container_logs(container_id)
            
            # Cleanup
            self.container_manager.stop_container(container_id)
            
            execution_time = time.time() - start_time
            
            return {
                "output": output,
                "error": "",
                "execution_time": execution_time,
                "exit_code": 0
            }
        except Exception as e:
            return {
                "output": "",
                "error": str(e),
                "execution_time": time.time() - start_time,
                "exit_code": 1
            }
