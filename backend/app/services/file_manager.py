import os
import shutil
from typing import Optional

class FileManager:
    def __init__(self, upload_path: str = "./storage/local/uploads"):
        self.upload_path = upload_path
        os.makedirs(upload_path, exist_ok=True)
    
    def save_file(self, file_name: str, content: bytes) -> str:
        """Save uploaded file"""
        file_path = os.path.join(self.upload_path, file_name)
        with open(file_path, 'wb') as f:
            f.write(content)
        return file_path
    
    def read_file(self, file_name: str) -> Optional[bytes]:
        """Read file content"""
        file_path = os.path.join(self.upload_path, file_name)
        if not os.path.exists(file_path):
            return None
        with open(file_path, 'rb') as f:
            return f.read()
    
    def delete_file(self, file_name: str) -> bool:
        """Delete a file"""
        file_path = os.path.join(self.upload_path, file_name)
        if os.path.exists(file_path):
            os.remove(file_path)
            return True
        return False
    
    def list_files(self) -> list:
        """List all uploaded files"""
        return os.listdir(self.upload_path)
