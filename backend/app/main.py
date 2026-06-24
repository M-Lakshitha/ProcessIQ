from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.health import router as health_router
from app.api.workflows import router as workflows_router
from app.core.config import settings

app = FastAPI(
    title=settings.app_name,
    version="0.1.0",
    description="Deterministic civic workflow planning API."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://processiq.in"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"]
)

app.include_router(health_router)
app.include_router(workflows_router)
