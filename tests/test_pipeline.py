from job_tracker.scraper.sample import SampleScraper
from job_tracker.scorer import calculate_fit_score
from job_tracker.database.repository import JobRepository
from job_tracker.database.models import Job


def test_full_pipeline():
    """Test the complete scrape → score → save pipeline."""
    # Step 1: Scrape
    scraper = SampleScraper()
    jobs = scraper.scrape("Python", "Pune")
    assert len(jobs) >= 8

    # Step 2: Score
    for job in jobs:
        job.fit_score = calculate_fit_score(
            title=job.title,
            location=job.location,
            description=job.description,
        )
    assert all(0 <= job.fit_score <= 100 for job in jobs)

    # Step 3: Save to in-memory database
    repo = JobRepository(db_path=":memory:")
    for job in jobs:
        repo.save(job)

    # Step 4: Retrieve and verify
    saved_jobs = repo.get_all_jobs()
    assert len(saved_jobs) == len(jobs)

    top_jobs = repo.get_top_jobs(limit=3)
    assert len(top_jobs) <= 3
    assert top_jobs[0].fit_score >= top_jobs[-1].fit_score

    status_counts = repo.get_status_counts()
    assert "new" in status_counts

    repo.close()


def test_scoring_integration():
    """Jobs get different scores based on content."""
    perfect_job = Job(
        title="Python Data Analyst",
        company="TCS",
        location="Pune",
        description="Python, SQL, Power BI, FastAPI, Firebase needed",
    )
    bad_job = Job(
        title="Chef",
        company="Restaurant",
        location="Delhi",
        description="Cook Italian food",
    )

    perfect_job.fit_score = calculate_fit_score(
        perfect_job.title, perfect_job.location, perfect_job.description
    )
    bad_job.fit_score = calculate_fit_score(
        bad_job.title, bad_job.location, bad_job.description
    )

    assert perfect_job.fit_score > bad_job.fit_score
    assert bad_job.fit_score == 0