from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api.auth import routes as auth_routes
from app.api.notebooks import routes as notebook_routes
from app.api.execution import routes as execution_routes
from app.config import settings

app = FastAPI(title="C/C++ Notebook API", version="1.0.0")

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Configure appropriately in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_routes.router, prefix="/auth", tags=["auth"])
app.include_router(notebook_routes.router, prefix="/notebooks", tags=["notebooks"])
app.include_router(execution_routes.router, prefix="/execution", tags=["execution"])

@app.get("/")
async def root():
    return {"message": "C/C++ Notebook API"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
