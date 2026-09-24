# AI-Powered University Knowledge Assistant

A full-stack, self-contained chatbot that answers student questions about a university
(admissions, fees, courses, exams, library, hostels, placements, IT support, contacts)
using a **built-in AI retrieval engine** — no API keys, no external AI services required.

## How the AI works
1. Your question is tokenized and cleaned (stopword removal, lowercase).
2. A **TF-IDF vector** is built over the knowledge base (30+ curated Q&A entries).
3. The engine ranks entries with **cosine similarity** and boosts exact keyword hits.
4. If confidence is too low, the assistant honestly says so and suggests popular
   questions instead of hallucinating an answer.

## Project structure
```
university-knowledge-assistant/
├── run.py                     # one-command launcher
├── requirements.txt
├── backend/
│   ├── app.py                 # Flask app: serves frontend + REST API
│   ├── ai_engine.py           # TF-IDF retrieval engine (pure Python)
│   └── knowledge_base.json    # university Q&A data (edit to customize)
└── frontend/
    ├── index.html
    ├── css/style.css
    └── js/app.js
```

## Quick start
```bash
pip install -r requirements.txt
python run.py
```
Then open **http://localhost:5000**

## API
| Endpoint | Method | Description |
|---|---|---|
| `/api/chat` | POST | `{message, category?}` -> answer + confidence + suggestions |
| `/api/categories` | GET | list of knowledge-base categories |
| `/api/health` | GET | engine stats |
| `/api/feedback` | POST | stores thumbs up/down in `feedback_log.jsonl` |

## Customizing for your university
1. Edit `backend/knowledge_base.json` — replace questions/answers with your own.
2. The engine rebuilds its TF-IDF index automatically at startup; no retraining needed.
3. Restart with `python run.py`.
