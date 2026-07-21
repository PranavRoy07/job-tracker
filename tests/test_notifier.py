from job_tracker.database.models import Job
from job_tracker.notifier import notify_top_jobs


def make_job(title: str, company: str, score: int) -> Job:
    """Helper to create a test job quickly."""
    return Job(
        title=title,
        company=company,
        location="Pune",
        fit_score=score,
    )


def test_filters_high_scoring_jobs():
    """Only jobs above min_score are returned."""
    jobs = [
        make_job("Job A", "Company A", 90),
        make_job("Job B", "Company B", 50),
        make_job("Job C", "Company C", 75),
    ]
    result = notify_top_jobs(jobs, min_score=70)
    assert len(result) == 2
    assert result[0].title == "Job A"
    assert result[1].title == "Job C"


def test_no_high_scoring_jobs():
    """Returns empty list when no jobs meet threshold."""
    jobs = [
        make_job("Job A", "Company A", 30),
        make_job("Job B", "Company B", 50),
    ]
    result = notify_top_jobs(jobs, min_score=70)
    assert result == []


def test_empty_job_list():
    """Handles empty list gracefully."""
    result = notify_top_jobs([], min_score=70)
    assert result == []


def test_custom_min_score():
    """Custom threshold works correctly."""
    jobs = [
        make_job("Job A", "Company A", 45),
        make_job("Job B", "Company B", 30),
    ]
    result = notify_top_jobs(jobs, min_score=40)
    assert len(result) == 1
    assert result[0].title == "Job A"