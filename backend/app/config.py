import os
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv("DATABASE_URL", "sqlite:///./c_collab.db")
    SECRET_KEY: str = os.getenv("SECRET_KEY", "your-secret-key-change-in-production")
    JWT_SECRET_KEY: str = os.getenv("JWT_SECRET_KEY", "your-jwt-secret-key")
    JWT_ALGORITHM: str = os.getenv("JWT_ALGORITHM", "HS256")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
    
    EXECUTION_ENGINE_URL: str = os.getenv("EXECUTION_ENGINE_URL", "http://localhost:8001")
    MAX_EXECUTION_TIME: int = int(os.getenv("MAX_EXECUTION_TIME", "30"))
    MAX_MEMORY_MB: int = int(os.getenv("MAX_MEMORY_MB", "512"))
    
    class Config:
        env_file = ".env"

settings = Settings()
