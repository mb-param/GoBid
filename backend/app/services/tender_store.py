import json
from pathlib import Path
from threading import Lock

from app.schemas.tender import TenderRead

_LOCK = Lock()
_STORE_PATH = Path(__file__).resolve().parents[2] / "data" / "africagateway_tenders.json"


def _ensure_store_path() -> None:
    _STORE_PATH.parent.mkdir(parents=True, exist_ok=True)
    if not _STORE_PATH.exists():
        _STORE_PATH.write_text("[]", encoding="utf-8")


def load_tenders() -> list[TenderRead]:
    _ensure_store_path()
    with _LOCK:
        raw = json.loads(_STORE_PATH.read_text(encoding="utf-8"))
    return [TenderRead.model_validate(item) for item in raw]


def save_tenders(tenders: list[TenderRead]) -> None:
    _ensure_store_path()
    payload = [tender.model_dump() for tender in tenders]
    with _LOCK:
        _STORE_PATH.write_text(json.dumps(payload, indent=2), encoding="utf-8")
