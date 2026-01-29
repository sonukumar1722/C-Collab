from abc import ABC, abstractmethod
from typing import Dict, Any, List, Optional

class StorageAdapter(ABC):
    """Abstract base class for storage adapters"""
    
    @abstractmethod
    def save(self, key: str, data: Any) -> bool:
        """Save data to storage"""
        pass
    
    @abstractmethod
    def load(self, key: str) -> Optional[Any]:
        """Load data from storage"""
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        """Delete data from storage"""
        pass
    
    @abstractmethod
    def list(self) -> List[str]:
        """List all keys in storage"""
        pass
    
    @abstractmethod
    def exists(self, key: str) -> bool:
        """Check if key exists in storage"""
        pass

class LocalStorageAdapter(StorageAdapter):
    """Local filesystem storage adapter"""
    
    def __init__(self, base_path: str = "./storage/local"):
        import os
        self.base_path = base_path
        os.makedirs(base_path, exist_ok=True)
    
    def save(self, key: str, data: Any) -> bool:
        """Save data to local filesystem"""
        import json
        import os
        
        file_path = os.path.join(self.base_path, key)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        try:
            with open(file_path, 'w') as f:
                json.dump(data, f, indent=2)
            return True
        except Exception:
            return False
    
    def load(self, key: str) -> Optional[Any]:
        """Load data from local filesystem"""
        import json
        import os
        
        file_path = os.path.join(self.base_path, key)
        if not os.path.exists(file_path):
            return None
        
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except Exception:
            return None
    
    def delete(self, key: str) -> bool:
        """Delete data from local filesystem"""
        import os
        
        file_path = os.path.join(self.base_path, key)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    
    def list(self) -> List[str]:
        """List all files in storage"""
        import os
        
        files = []
        for root, dirs, filenames in os.walk(self.base_path):
            for filename in filenames:
                rel_path = os.path.relpath(os.path.join(root, filename), self.base_path)
                files.append(rel_path)
        return files
    
    def exists(self, key: str) -> bool:
        """Check if file exists"""
        import os
        file_path = os.path.join(self.base_path, key)
        return os.path.exists(file_path)
