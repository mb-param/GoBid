## Tender Intelligence Platform (`tender-platform/`)

Additive Node.js service on top of the existing Crawlee monorepo — **never replaces framework internals**.

### Stack
Playwright · Crawlee `PlaywrightCrawler` · BullMQ · Redis · MongoDB · Mongoose · Express

### Prerequisites
1. Node 18+
2. **MongoDB** listening on `MONGO_URI`
3. **Redis** listening for BullMQ
4. `npm install` inside `tender-platform/`

### Environment
Copy `.env.example` to project root **`tender-platform/.env`** (the loader also reads `src/.env` if present). Encrypted **dotenvx** files are supported via **`@dotenvx/dotenvx`** (decryption needs **`DOTENV_PRIVATE_KEY`** or a local **`.env.keys`** — never commit keys).

| Variable | Purpose |
|----------|---------|
| `MONGO_URI` | Mongoose connection string |
| `REDIS_URL` | BullMQ backing store (`redis://` or `rediss://`; defaults to `redis://127.0.0.1:6379` if unset) |
| `BROWSERLESS_WS_ENDPOINT` | Optional `wss://` CDP websocket (Browserless) |
| `HEADLESS` | `true`/`false` — headed manual login flows force `false` in CLI scripts |
| `MAX_BROWSER_CONCURRENCY` | Per crawler `maxConcurrency` ceiling |
| `PORTAL_REPEAT_CRON` | BullMQ repeatable job CRON |

Portal toggles use `ENABLE_PORTAL_*`; seeds use `SAMGOV_SEARCH_URL`, `BONFIRE_BASE_URL`, etc. (see `src/core/portalRegistry.js`).

### Auth JSON (mandatory persistence)
Interactive login (**once**) writes isolated Playwright `storageState`:
```bash
cd tender-platform
npm run login -- samgov
```
Artifacts (git-ignored recommended): `auth/samgov.json`, `auth/bonfire.json`, `auth/southafrica.json`, `auth/kenya.json`.

### One-shot crawl (`Promise.all` multi-portal)
```bash
npm run crawl -- --portal samgov --portal kenya   # omit flags → all enabled + seeded portals
```
Each portal = **distinct** crawler session, RequestQueue prefix, **`auth/*.json`** path, **`prePageCreateHooks` storageState**.

### Queue / workers / API
Terminal A:
```bash
npm run worker
```
Terminal B (register repeatable fan-out — exits after enqueue metadata write):
```bash
npm run scheduler
```
Dashboard HTTP triggers:
```bash
npm run api
curl -X POST http://localhost:3800/jobs/scrape
```

### MongoDB schema & backups
`tenders` collection — see `src/db/tenderModel.js`. Every upsert mirrors NDJSON backups under `downloads/backups/tenders-{portal}-{date}.ndjson`.

### Docker/Browserless
Set `BROWSERLESS_WS_ENDPOINT` to your cluster websocket; **`browserPool.js`** swaps `chromium.launch` for `chromium.connect`.

### Troubleshooting
- Error screenshots → `logs/error_*.png` (via `retryHandler.js` failed requests)
- Tune selectors per SPA drift under each portal folder (`selectors.js` only).
