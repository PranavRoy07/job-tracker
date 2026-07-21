from apscheduler.schedulers.blocking import BlockingScheduler
from job_tracker.logger import setup_logger

logger = setup_logger()


def start_scheduler(job_function: callable) -> None:
    """Start the APScheduler to run a job daily at 9 AM.

    The scheduler runs in the foreground (blocking) and
    will keep running until you press Ctrl+C to stop it.

    Args:
        job_function: The function to run daily (e.g., scrape + score).
    """
    scheduler = BlockingScheduler()

    # Schedule the job for every day at 9:00 AM
    scheduler.add_job(
        job_function,
        trigger="cron",
        hour=9,
        minute=0,
        id="daily_scrape",
        name="Daily Job Scraper",
    )

    logger.info("⏰ Scheduler started! Will run daily at 9:00 AM")
    logger.info("   Press Ctrl+C to stop")

    try:
        scheduler.start()
    except KeyboardInterrupt:
        logger.info("⏹️  Scheduler stopped by user")
        scheduler.shutdown()