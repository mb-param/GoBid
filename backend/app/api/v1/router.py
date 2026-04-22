from fastapi import APIRouter

from app.api.v1.routes import dashboard, sources, tenders

api_router = APIRouter()
api_router.include_router(dashboard.router, prefix="/dashboard", tags=["dashboard"])
api_router.include_router(sources.router, prefix="/sources", tags=["sources"])
api_router.include_router(tenders.router, prefix="/tenders", tags=["tenders"])
