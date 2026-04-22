from fastapi import APIRouter

router = APIRouter()


@router.get("/summary")
def get_summary() -> dict[str, int]:
    return {"active_sources": 3, "new_tenders_today": 12, "high_priority": 4}
