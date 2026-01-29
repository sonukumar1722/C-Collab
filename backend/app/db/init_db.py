from app.db.session import engine
from app.models.user import Base as UserBase
from app.models.notebook import Base as NotebookBase

def init_db():
    """Initialize database tables"""
    UserBase.metadata.create_all(bind=engine)
    NotebookBase.metadata.create_all(bind=engine)
    print("Database initialized successfully")

if __name__ == "__main__":
    init_db()
