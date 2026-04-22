from hashlib import md5

from app.schemas.scrape import ScrapeRunResponse
from app.schemas.tender import TenderRead
from app.services.africagateway_scraper import fetch_homepage, parse_tender_links
from app.services.intelligence_service import score_relevance
from app.services.tender_store import load_tenders, save_tenders


AFRICAN_COUNTRIES = [
    "South Africa",
    "Kenya",
    "Nigeria",
    "Ghana",
    "Rwanda",
    "Uganda",
    "Tanzania",
    "Egypt",
    "Morocco",
    "Namibia",
    "Ethiopia",
]


def _infer_country(text: str) -> str:
    lowered = text.lower()
    for country in AFRICAN_COUNTRIES:
        if country.lower() in lowered:
            return country
    return "Africa"


def _compute_priority(score: float) -> str:
    if score >= 0.85:
        return "high"
    if score >= 0.7:
        return "medium"
    return "low"


def run_africagateway_pipeline() -> ScrapeRunResponse:
    html = fetch_homepage()
    raw_tenders = parse_tender_links(html)

    existing = load_tenders()
    existing_by_url = {item.source_url: item for item in existing}

    stored_tenders: list[TenderRead] = []
    skipped = 0

    for raw in raw_tenders:
        relevance = score_relevance(raw.title, raw.snippet)
        if relevance < 0.6:
            skipped += 1
            continue

        tender = TenderRead(
            id=md5(raw.source_url.encode("utf-8")).hexdigest()[:12],
            title=raw.title,
            country=_infer_country(raw.title + " " + raw.snippet),
            relevance=round(relevance, 2),
            deadline=raw.deadline,
            priority=_compute_priority(relevance),
            source_portal="AfricaGateway",
            source_url=raw.source_url,
            tags=["it", "ai", "software"],
        )
        existing_by_url[tender.source_url] = tender
        stored_tenders.append(tender)

    merged = list(existing_by_url.values())
    save_tenders(merged)

    return ScrapeRunResponse(
        source="africagateway",
        fetched=len(raw_tenders),
        stored=len(stored_tenders),
        skipped=skipped,
        tenders=stored_tenders,
    )
