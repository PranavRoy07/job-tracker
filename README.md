# ⚡ Job Intelligence Engine

An automated Python-based job tracking system that **collects real job listings**, evaluates them against your skills, and presents the results in a **modern, interactive terminal dashboard**.

> **Built as a production-ready Python package, not just a script.**

---

## ✨ Features

- 🌐 **Real Job Scraping**
  - Fetches live job listings from:
    - RemoteOK API
    - Adzuna API (Pune technology jobs)

- 📊 **Smart Job Scoring**
  - Calculates a **0–100 compatibility score** based on your skill set.

- 💾 **Persistent Data Storage**
  - Uses **SQLite** with the **Repository Pattern** for clean data management.

- 🎨 **Interactive Terminal Dashboard**
  - Built using **Rich** for a clean and visually appealing command-line interface.

- 🔔 **Desktop Notifications**
  - Sends instant alerts for high-scoring opportunities (Score ≥ 70).

- ⏰ **Automated Scheduling**
  - Runs automatically every day at **9:00 AM** using APScheduler.

- 📝 **Comprehensive Logging**
  - Records all application activity in `scraper.log`.

---

# 🖥️ Dashboard Preview

```text
╔══════════════════════════════════════════════════════════════╗
║                    ⚡ JOB INTELLIGENCE ENGINE                ║
╚══════════════════════════════════════════════════════════════╝

╭────────────── 🏆 Top 10 Jobs by Fit Score ───────────────╮
│ #   Score   Title                 Company                │
├──────────────────────────────────────────────────────────┤
│ 1    90     Data Engineer         Persistent             │
│ 2    85     Python Developer      Infosys                │
│ 3    75     Data Analyst          TCS                    │
│                                                          │
│              ████████████████░░░░   85%                  │
╰──────────────────────────────────────────────────────────╯

╭────────────── 📊 Application Status ─────────────────────╮
│ 🆕 New Jobs        12   ████████████░░░░░░░░             │
│ 📤 Applied          3   ███░░░░░░░░░░░░░░░░             │
│ 🎯 Interview        1   █░░░░░░░░░░░░░░░░░░             │
╰──────────────────────────────────────────────────────────╯
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| **Python 3.12+** | Core programming language |
| **Rich** | Interactive terminal dashboard |
| **SQLite** | Local database storage |
| **APScheduler** | Automated daily scheduling |
| **Requests** | Fetching job listings via APIs |
| **Plyer** | Desktop notifications |
| **Pytest** | Unit testing and Test-Driven Development (TDD) |

---

# 📂 Project Structure

```text
job-tracker/
│
├── src/
│   ├── scraper/
│   ├── database/
│   ├── dashboard/
│   ├── notifications/
│   ├── scheduler/
│   └── scoring/
│
├── tests/
├── scraper.log
├── requirements.txt
├── README.md
└── main.py
```

---

# 🚀 Getting Started

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/PranavRoy07/job-tracker.git
cd job-tracker
```

## 2️⃣ Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

## 4️⃣ Run the Application

```bash
python main.py
```

---

# 📊 How It Works

```text
Job APIs
   │
   ▼
Job Scraper
   │
   ▼
SQLite Database
   │
   ▼
Skill Scoring Engine
   │
   ▼
Rich Dashboard
   │
   ├── Desktop Notifications
   └── Daily Scheduler
```

---

# 🧪 Testing

Run the test suite using:

```bash
pytest
```

---

# 📄 Logging

Application logs are stored in:

```text
scraper.log
```

These logs include:

- Job scraping activity
- API responses
- Scheduler execution
- Notification events
- Errors and exceptions

---

# 🎯 Future Improvements

- AI-powered resume matching
- Email job alerts
- Multi-location job search
- Company insights and ratings
- ATS resume compatibility scoring
- Web dashboard (Flask/FastAPI)
- PostgreSQL support
- Docker deployment

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Open a Pull Request

---

# 📜 License

This project is licensed under the **MIT License**.

---

# 👨‍💻 Author

**Pranav Roy**

If you found this project useful, consider giving it a ⭐ on GitHub.
