from fastapi import APIRouter, Query

from app.schemas.scrape import ScrapeRunResponse
from app.schemas.tender import TenderRead
from app.services.pipeline_service import run_africagateway_pipeline
from app.services.tender_store import load_tenders

router = APIRouter()


@router.get("", response_model=list[TenderRead])
def list_tenders(min_relevance: float = Query(default=0.0, ge=0.0, le=1.0)) -> list[TenderRead]:
    tenders = load_tenders()
    return [item for item in tenders if item.relevance >= min_relevance]


@router.post("/scrape/africagateway", response_model=ScrapeRunResponse)
def scrape_africagateway() -> ScrapeRunResponse:
    return run_africagateway_pipeline()
