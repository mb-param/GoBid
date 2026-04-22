# GoBID Africa - Tender Intelligence Platform (Budget-First)

This project is an Africa-first implementation of your GoBID strategy, structured to closely mirror the GeM Bid Aggregation working model while staying low-cost and practical for an MVP.

Current scope is only:
- Government tender discovery
- Document/information extraction
- AI intelligence for bid relevance
- IT / AI / Software opportunity prioritization

Auto bid submission is intentionally not included in v1.

## Strategic Merge (Doc 1 + GeM Model)

- **From your GoBID strategy document:** Africa-first rollout, IT/AI/software-only filtering, intelligent scoring, multi-country extensibility.
- **From GeM platform plan:** modular architecture, agent-like processing flow, auditable pipeline, role-based operations, and frontend workspace pattern.
- **Merged result:** GeM-style structured workflow adapted to African procurement portals with a free-tier-first stack.

## v1 Workflow (GeM-Like, Africa Focused)

1. Source schedulers trigger portal connectors by country.
2. Ingestion captures tender notices + documents (PDF/HTML).
3. Extraction parses title, agency, deadline, budget, scope.
4. AI intelligence scores relevance for IT/AI/software services.
5. Deduplication removes reposted or mirrored tenders.
6. Ranked shortlist is shown in the dashboard + alert channels.

## Low-Cost Architecture (Near-Free)

- **Frontend:** React + Vite (already scaffolded in `frontend`)
- **Backend (recommended next):** FastAPI (single service)
- **Database:** PostgreSQL with `pgvector` (Supabase free tier or local Docker)
- **Queue/Scheduler:** APScheduler/Cron first, Redis optional later
- **Scraping:** Playwright + BeautifulSoup (robots-compliant)
- **AI:** low-cost LLM model routing (OpenAI/Anthropic optional switch)
- **Storage:** local filesystem initially, then Cloudflare R2/S3-compatible low-cost bucket
- **Hosting (MVP):** Render/Railway/Fly free tiers + GitHub Actions

## Folder Structure

- `frontend` - React UI for sources, pipeline status, and opportunity board
- `backend` - backend starter docs and environment template
- `config` - africa source onboarding configs
- `docs` - architecture and implementation documents

## Required Credentials

Minimum required now:
- `OPENAI_API_KEY` (or another supported LLM API key)
- `DATABASE_URL` (PostgreSQL connection string)
- `JWT_SECRET`
- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS` (for alerts)

Depending on sources:
- Country portal credentials (if login is required by specific portal)
- Proxy API key (optional; only when a portal rate-limits heavily)
- OCR API key (optional, if you choose cloud OCR instead of Tesseract)

## Africa Rollout Plan

Phase A (pilot):
- South Africa public procurement portals

Phase B:
- Kenya + Nigeria connectors

Phase C:
- Rwanda + Ghana + Egypt (or priority countries as decided)

All phases maintain strict IT/AI/software relevance filtering.

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

Then open the local URL shown by Vite.

## Next Build Steps (recommended)

1. Create FastAPI backend skeleton with extraction and scoring endpoints.
2. Add `config/africa-sources.json` driven connector architecture.
3. Add PostgreSQL schema for tenders, runs, alerts, and source health.
4. Add scheduled ingestion jobs and first live portal connector.
5. Connect frontend to backend APIs and replace sample cards with live data.

