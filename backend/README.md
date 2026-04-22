# Backend Starter Notes (Africa MVP)

This folder is prepared for the FastAPI backend that will power:
- Portal ingestion
- Tender extraction
- AI relevance scoring
- Deduplication and ranking
- Alert dispatch

## Recommended Initial Modules

- `app/api/tenders.py` - list/search/filter tenders
- `app/api/sources.py` - source health, onboarding, schedules
- `app/api/runs.py` - ingestion run history and logs
- `app/services/extract.py` - parse notice fields from HTML/PDF
- `app/services/score.py` - IT/AI/software relevance scoring
- `app/services/dedupe.py` - semantic + rule-based duplicate detection
- `app/jobs/scheduler.py` - country portal schedule runner

## Free-First Build Notes

- Start with one service and one Postgres database.
- Use local files for raw payload storage first.
- Add Redis only if ingestion volume increases.
- Keep all connectors configuration-driven via `config/africa-sources.json`.
