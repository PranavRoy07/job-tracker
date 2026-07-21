import sys
from job_tracker.logger import setup_logger

logger = setup_logger()


def run_pipeline() -> None:
    """Run the complete job tracking pipeline.

    Steps:
        1. Scrape job listings
        2. Score each job
        3. Save to database
        4. Send notifications for hot jobs
        5. Display the dashboard
    """
    from job_tracker.scraper.sample import SampleScraper
    from job_tracker.scorer import calculate_fit_score
    from job_tracker.database.repository import JobRepository
    from job_tracker.notifier import notify_top_jobs
    from job_tracker.dashboard import render_dashboard

    # Step 1: Scrape
    logger.info("🔍 Scraping job listings...")
    scraper = SampleScraper()
    jobs = scraper.scrape(query="Python Developer", location="Pune")
    logger.info("   Found %d jobs", len(jobs))

    # Step 2: Score each job
    logger.info("📊 Scoring jobs...")
    for job in jobs:
        job.fit_score = calculate_fit_score(
            title=job.title,
            location=job.location,
            description=job.description,
        )

    # Sort by score (highest first)
    jobs.sort(key=lambda j: j.fit_score, reverse=True)

    # Step 3: Save to database
    logger.info("💾 Saving to database...")
    repo = JobRepository(db_path="jobs.db")
    for job in jobs:
        repo.save(job)
    logger.info("   Saved %d jobs", len(jobs))

    # Step 4: Notify for hot jobs (score > 70)
    logger.info("🔔 Checking for hot jobs...")
    hot_jobs = notify_top_jobs(jobs, min_score=70)
    if hot_jobs:
        logger.info("   🔥 %d hot jobs found!", len(hot_jobs))

    # Step 5: Show dashboard
    top_jobs = repo.get_top_jobs(limit=10)
    status_counts = repo.get_status_counts()
    today_jobs = repo.get_today_jobs()

    render_dashboard(
        top_jobs=top_jobs,
        status_counts=status_counts,
        today_jobs=today_jobs,
    )

    repo.close()
    logger.info("✅ Pipeline complete!")


def show_dashboard() -> None:
    """Show the dashboard with existing data (no scraping)."""
    from job_tracker.database.repository import JobRepository
    from job_tracker.dashboard import render_dashboard

    repo = JobRepository(db_path="jobs.db")
    top_jobs = repo.get_top_jobs(limit=10)
    status_counts = repo.get_status_counts()
    today_jobs = repo.get_today_jobs()

    render_dashboard(
        top_jobs=top_jobs,
        status_counts=status_counts,
        today_jobs=today_jobs,
    )
    repo.close()


def start_schedule() -> None:
    """Start the daily scheduler (runs at 9 AM)."""
    from job_tracker.scheduler import start_scheduler

    logger.info("🚀 Starting Job Tracker Scheduler...")
    start_scheduler(job_function=run_pipeline)


def main() -> None:
    """Entry point for the job-tracker CLI command.

    Usage:
        job-tracker run        - Scrape jobs and show dashboard
        job-tracker dashboard  - Show dashboard only
        job-tracker schedule   - Start scheduled daily runs
    """
    if len(sys.argv) < 2:
        _show_help()
        return

    command = sys.argv[1]

    if command == "run":
        run_pipeline()
    elif command == "dashboard":
        show_dashboard()
    elif command == "schedule":
        start_schedule()
    elif command == "help":
        _show_help()
    else:
        print(f"❌ Unknown command: {command}")
        _show_help()


def _show_help() -> None:
    """Display help message with available commands."""
    from rich.console import Console
    from rich.panel import Panel
    from rich import box

    console = Console()

    help_text = (
        "[bold cyan]job-tracker run[/bold cyan]"
        "        Scrape jobs, score them, show dashboard\n"
        "[bold cyan]job-tracker dashboard[/bold cyan]"
        "  Show the dashboard (no scraping)\n"
        "[bold cyan]job-tracker schedule[/bold cyan]"
        "   Start daily scheduled runs (9 AM)\n"
        "[bold cyan]job-tracker help[/bold cyan]"
        "       Show this help message"
    )

    panel = Panel(
        help_text,
        title="⚡ Job Tracker — Commands",
        border_style="bright_blue",
        box=box.ROUNDED,
        padding=(1, 2),
    )
    console.print(panel)


if __name__ == "__main__":
    main()