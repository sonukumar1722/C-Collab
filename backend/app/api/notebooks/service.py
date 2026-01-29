from typing import List, Optional
from datetime import datetime
import uuid

class NotebookService:
    def __init__(self):
        self.notebooks = {}
    
    def get_all_notebooks(self):
        return list(self.notebooks.values())
    
    def get_notebook(self, notebook_id: str):
        return self.notebooks.get(notebook_id)
    
    def create_notebook(self, notebook_data):
        notebook_id = str(uuid.uuid4())
        notebook = {
            "id": notebook_id,
            "title": notebook_data.title,
            "cells": [],
            "created_at": datetime.utcnow().isoformat(),
            "updated_at": datetime.utcnow().isoformat()
        }
        self.notebooks[notebook_id] = notebook
        return notebook
    
    def update_notebook(self, notebook_id: str, notebook_data):
        if notebook_id not in self.notebooks:
            return None
        self.notebooks[notebook_id].update({
            "title": notebook_data.title,
            "updated_at": datetime.utcnow().isoformat()
        })
        return self.notebooks[notebook_id]
    
    def delete_notebook(self, notebook_id: str):
        if notebook_id in self.notebooks:
            del self.notebooks[notebook_id]
            return True
        return False
