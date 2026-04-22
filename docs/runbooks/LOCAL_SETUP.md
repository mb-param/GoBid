# Local Setup

## Frontend
- cd frontend
- npm install
- npm run dev

## Backend
- cd backend
- python -m venv .venv
- .venv\Scripts\activate
- pip install -e .
- uvicorn app.main:app --reload
