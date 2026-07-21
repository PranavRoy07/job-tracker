from job_tracker.database.models import Job
from job_tracker.logger import setup_logger

logger = setup_logger()


def notify_top_jobs(jobs: list[Job], min_score: int = 70) -> list[Job]:
    """Send desktop notifications for high-scoring jobs.

    Filters jobs with fit_score above min_score and sends
    a desktop popup notification for each one.

    Args:
        jobs: List of Job objects to check.
        min_score: Minimum score to trigger notification.

    Returns:
        List of jobs that triggered notifications.
    """
    hot_jobs = [job for job in jobs if job.fit_score > min_score]

    if not hot_jobs:
        logger.info("📭 No jobs above score %d found", min_score)
        return []

    for job in hot_jobs:
        _send_notification(
            title="🔥 Hot Job Alert!",
            message=f"{job.title} at {job.company} — Score: {job.fit_score}",
        )
        logger.info(
            "🔔 Notification: %s at %s (Score: %d)",
            job.title,
            job.company,
            job.fit_score,
        )

    return hot_jobs


def _send_notification(title: str, message: str) -> None:
    """Send a desktop notification.

    Uses plyer library for cross-platform notifications.
    Falls back to logging if plyer is not available.

    Args:
        title: Notification title.
        message: Notification body text.
    """
    try:
        from plyer import notification

        notification.notify(
            title=title,
            message=message,
            app_name="Job Tracker",
            timeout=10,
        )
    except Exception as e:
        # If plyer fails (e.g., no desktop environment), just log it
        logger.debug("Could not send notification: %s", e)