# Africa Tender Intelligence MVP - Implementation Blueprint

## Objective

Replicate the GeM bid aggregation workflow pattern for African government portals, limited to IT/AI/software tender intelligence and extraction.

## GeM-to-Africa Mapping

- **GeM Scraper Agent** -> Africa connector workers per country
- **GeM Analyzer Agent** -> requirement extraction + relevance scoring
- **GeM Compliance Agent** -> mandatory field completeness checks
- **GeM Dashboard** -> Africa shortlist and source health workspace

## v1 Feature Scope

Included:
- Source onboarding and scheduling
- Tender listing ingestion
- PDF/notice extraction
- AI category and relevance scoring
- Deduplication
- User alert dispatch

Excluded:
- CAPTCHA bypassing
- Unattended form auto-submission
- Full bid-authoring automation

## AI Intelligence Design (Budget-Friendly)

- Use compact model by default (`gpt-4o-mini` or equivalent)
- Cache repeated prompts and responses
- Run embeddings only for high-confidence candidates
- Add deterministic keyword gate before LLM call to cut token costs

## Relevance Logic (IT/AI/Software only)

1. Keyword and taxonomy pre-filter
2. LLM category classification
3. Confidence threshold scoring
4. Business rule boosts (deadline urgency, strategic country, value)
5. Final shortlist decision

## Credentials Checklist

- LLM API key
- PostgreSQL credentials
- SMTP credentials
- JWT secret
- Portal credentials (only where required)
- Optional proxy/OCR keys

## Success Criteria

- Fresh tenders visible in dashboard within schedule window
- >85% precision for IT/AI/software classification after tuning
- Duplicate tenders reduced to a single canonical record
- Alert notifications dispatched for high-priority matches
