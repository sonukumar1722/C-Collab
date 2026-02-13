from typing import Dict, List, Optional
import json
import os

class NotebookManager:
    def __init__(self, storage_path: str = "./storage/local/notebooks"):
        self.storage_path = storage_path
        os.makedirs(storage_path, exist_ok=True)
    
    def save_notebook(self, notebook_id: str, data: dict):
        """Save notebook to disk"""
        file_path = os.path.join(self.storage_path, f"{notebook_id}.json")
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=2)
    
    def load_notebook(self, notebook_id: str) -> Optional[dict]:
        """Load notebook from disk"""
        file_path = os.path.join(self.storage_path, f"{notebook_id}.json")
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'r') as f:
            return json.load(f)
    
    def list_notebooks(self) -> List[dict]:
        """List all notebooks"""
        notebooks = []
        for filename in os.listdir(self.storage_path):
            if filename.endswith('.json'):
                notebook_id = filename[:-5]
                notebook = self.load_notebook(notebook_id)
                if notebook:
                    notebooks.append(notebook)
        return notebooks
    
    def delete_notebook(self, notebook_id: str) -> bool:
        """Delete a notebook"""
        file_path = os.path.join(self.storage_path, f"{notebook_id}.json")
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
