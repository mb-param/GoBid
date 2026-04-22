from pydantic import BaseModel

from app.schemas.tender import TenderRead


class ScrapeRunResponse(BaseModel):
    source: str
    fetched: int
    stored: int
    skipped: int
    tenders: list[TenderRead]
