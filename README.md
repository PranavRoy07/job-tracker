# ⚡ Job Intelligence Engine
An automated job tracking tool that **scrapes real job listings**, scores them against your skill profile, and displays results in a **beautiful terminal dashboard**.
> Built as a production Python package — not a script, real software.
---
## ✨ Features
- 🌐 **Real job scraping** — RemoteOK API + Adzuna API (Pune tech jobs)
- 📊 **Smart scoring** — Rates each job 0-100 based on your skills
- 💾 **SQLite database** — Persistent storage with repository pattern
- 🎨 **Rich dashboard** — Beautiful terminal UI with score bars
- 🔔 **Desktop notifications** — Alerts for high-scoring jobs (score > 70)
- ⏰ **Daily scheduler** — Runs automatically at 9 AM via APScheduler
- 📝 **Logging** — All activity logged to `scraper.log`
---
## 🖥️ Dashboard Preview
╔══════════════════════════════════════════════╗ ║ ⚡ JOB INTELLIGENCE ENGINE ║ ╚══════════════════════════════════════════════╝

╭──────── 🏆 Top 10 Jobs by Fit Score ────────╮ │ # │ Score │ Title │ Company │ │ 1 │ 90 │ Data Engineer │ Persistent │ │ 2 │ 85 │ Python Developer │ Infosys │ │ 3 │ 75 │ Data Analyst │ TCS │ │ │ │ ████████████████░░░░ 85% │ ╰─────────────────────────────────────────────╯

╭──────── 📊 Application Status ──────────────╮ │ 🆕 New │ 12 │ ████████████░░░░░░░░ │ │ 📤 Applied │ 3 │ ███░░░░░░░░░░░░░░░░░ │ │ 🎯 Interview │ 1 │ █░░░░░░░░░░░░░░░░░░░ │ ╰─────────────────────────────────────────────╯



---
## 🛠️ Tech Stack
| Technology | Purpose |
|---|---|
| Python 3.12+ | Core language |
| Rich | Terminal dashboard UI |
| SQLite | Local database |
| APScheduler | Daily scheduled runs |
| requests | API calls for job scraping |
| plyer | Desktop notifications |
| pytest | Test-driven development |
---
## 🚀 Getting Started
### 1. Clone the repository
```bash
git clone https://github.com/PranavRoy07/job-tracker.git
cd job-tracker
