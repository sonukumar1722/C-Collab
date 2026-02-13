import docker
from typing import Dict, Optional

class ContainerManager:
    def __init__(self):
        self.client = docker.from_env()
        self.containers: Dict[str, docker.models.containers.Container] = {}
    
    def create_container(self, image: str, command: str, **kwargs) -> str:
        """Create and start a container"""
        container = self.client.containers.run(
            image,
            command,
            detach=True,
            **kwargs
        )
        container_id = container.id
        self.containers[container_id] = container
        return container_id
    
    def stop_container(self, container_id: str):
        """Stop and remove a container"""
        if container_id in self.containers:
            container = self.containers[container_id]
            container.stop()
            container.remove()
            del self.containers[container_id]
    
    def get_container_logs(self, container_id: str) -> str:
        """Get container logs"""
        if container_id in self.containers:
            container = self.containers[container_id]
            return container.logs().decode('utf-8')
        return ""
    
    def cleanup(self):
        """Clean up all containers"""
        for container_id in list(self.containers.keys()):
            self.stop_container(container_id)
