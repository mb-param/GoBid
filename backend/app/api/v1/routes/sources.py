from fastapi import APIRouter

from app.schemas.source import SourceStatusRead

router = APIRouter()


@router.get("", response_model=list[SourceStatusRead])
def list_sources() -> list[SourceStatusRead]:
    return [
        SourceStatusRead(
            country="Africa (Multi-country)",
            portal="AfricaGateway",
            status="pilot",
            cadence="6h",
        ),
        SourceStatusRead(country="South Africa", portal="eTenders", status="planned", cadence="6h"),
        SourceStatusRead(country="Kenya", portal="PPIP", status="planned", cadence="24h"),
    ]
