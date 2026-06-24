# ProcessIQ

ProcessIQ is a goal-oriented civic workflow planning platform. It converts user goals into deterministic, source-backed government workflow guidance.

It provides informational workflow guidance only. It does not provide legal advice, eligibility determination, document verification, application submission, or certificate validation.

## Stack

- Frontend: Next.js 15, TailwindCSS, Framer Motion, Zustand, Lucide, react-hot-toast
- Backend: FastAPI, SQLAlchemy, Alembic, Pydantic, JWT-ready settings, NetworkX
- Database target: PostgreSQL/Supabase
- Deployment targets: Vercel frontend, Render backend

## Local Development

```bash
npm install
npm run dev
```

Backend:

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
pytest
```

## Guardrails

- Workflows are deterministic and generated from predefined rules.
- LLMs are only for intent and attribute extraction fallback.
- User prompts are not stored; only SHA256 hashes are retained for 30 days.
