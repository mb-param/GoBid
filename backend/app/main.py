from fastapi import FastAPI

from app.api.v1.router import api_router
from app.core.settings import get_settings

settings = get_settings()

app = FastAPI(
    title="GoBID Africa API",
    version="0.1.0",
    description="Tender extraction and AI intelligence for African government portals.",
)
app.include_router(api_router, prefix=settings.api_prefix)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}
