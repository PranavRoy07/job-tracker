# Job Intelligence Engine

An automated Python job tracking system that scrapes live job listings, scores them against your skillset, and presents results in an interactive terminal dashboard — with desktop notifications for high-fit opportunities and automated daily scheduling.

> Built as a production-ready Python package, not just a script.

---

## Features

| Feature | Details |
|---|---|
| **Live job scraping** | Fetches from RemoteOK API and Adzuna API (Pune technology listings) |
| **Skill-match scoring** | 0–100 compatibility score calculated per listing against your skill profile |
| **Desktop notifications** | Instant alerts for jobs scoring ≥ 70 via `plyer` |
| **Automated scheduling** | Runs daily at 9:00 AM via `APScheduler` — no manual trigger needed |
| **Rich terminal dashboard** | Top 10 jobs by fit score + application pipeline status, rendered with `Rich` |
| **SQLite + Repository Pattern** | Clean data separation — storage logic never bleeds into business logic |
| **Full test suite** | `pytest` with TDD approach; activity logged to `scraper.log` |

---

## Dashboard preview

```
╔══════════════════════════════════════════════════════════════╗
║                    ⚡ JOB INTELLIGENCE ENGINE                ║
╚══════════════════════════════════════════════════════════════╝

╭────────────── 🏆 Top 10 Jobs by Fit Score ───────────────╮
│ #   Score   Title                 Company                │
├──────────────────────────────────────────────────────────┤
│ 1    90     Data Engineer         Persistent             │
│ 2    85     Python Developer      Infosys                │
│ 3    75     Data Analyst          TCS                    │
│              ████████████████░░░░   85%                  │
╰──────────────────────────────────────────────────────────╯

╭────────────── 📊 Application Status ─────────────────────╮
│ 🆕 New Jobs        12   ████████████░░░░░░░░             │
│ 📤 Applied          3   ███░░░░░░░░░░░░░░░░             │
│ 🎯 Interview        1   █░░░░░░░░░░░░░░░░░░             │
╰──────────────────────────────────────────────────────────╯
```

---

## How it works

```
Job APIs (RemoteOK, Adzuna)
        │
        ▼
    Job Scraper
        │
        ▼
  SQLite Database (Repository Pattern)
        │
        ▼
  Skill Scoring Engine (0–100)
        │
        ▼
    Rich Dashboard
        │
        ├── Desktop Notifications (score ≥ 70)
        └── Daily Scheduler (9:00 AM via APScheduler)
```

---

## Project structure

```
job-tracker/
├── src/
│   ├── scraper/        — RemoteOK + Adzuna API clients
│   ├── database/       — SQLite setup + Repository Pattern
│   ├── dashboard/      — Rich terminal UI
│   ├── notifications/  — plyer desktop alerts
│   ├── scheduler/      — APScheduler daily job
│   └── scoring/        — skill-match compatibility engine
├── tests/              — pytest test suite
├── scraper.log         — full activity log
├── jobs.db             — SQLite database
├── pyproject.toml
└── README.md
```

---

## Getting started

### 1. Clone the repository
```bash
git clone https://github.com/PranavRoy07/job-tracker.git
cd job-tracker
```

### 2. Create a virtual environment
```bash
# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate

# Windows
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the application
```bash
python main.py
```

---

## Running tests
```bash
pytest
```

---

## Tech stack

| Technology | Purpose |
|---|---|
| Python 3.12+ | Core language |
| Rich | Interactive terminal dashboard |
| SQLite | Local persistent storage |
| APScheduler | Daily automated scheduling |
| Requests | HTTP client for job APIs |
| Plyer | Cross-platform desktop notifications |
| Pytest | Unit testing + TDD |

---

## Logging

All activity is recorded in `scraper.log`:
- Job scraping events and API responses
- Scheduler execution timestamps
- Notification dispatches
- Errors and exceptions

---

## License

MIT
