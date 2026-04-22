from typing import Literal

from pydantic import BaseModel


class TenderRead(BaseModel):
    id: str
    title: str
    country: str
    relevance: float
    deadline: str | None = None
    priority: Literal["high", "medium", "low"]
    source_portal: str
    source_url: str
    tags: list[str] = []
