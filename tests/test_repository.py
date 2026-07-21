from job_tracker.database.models import Job
from job_tracker.database.repository import JobRepository


def make_repo() -> JobRepository:
    """Create a test repository using in-memory database."""
    return JobRepository(db_path=":memory:")


def test_save_and_retrieve():
    """Save a job and retrieve it."""
    repo = make_repo()
    job = Job(
        title="Python Developer",
        company="Infosys",
        location="Pune",
        description="Python and SQL required",
        fit_score=75,
    )
    job_id = repo.save(job)
    assert job_id == 1

    jobs = repo.get_all_jobs()
    assert len(jobs) == 1
    assert jobs[0].title == "Python Developer"
    assert jobs[0].fit_score == 75


def test_get_top_jobs():
    """Top jobs returned in score order."""
    repo = make_repo()
    repo.save(Job(title="Job A", company="X", location="Pune", fit_score=30))
    repo.save(Job(title="Job B", company="Y", location="Pune", fit_score=90))
    repo.save(Job(title="Job C", company="Z", location="Pune", fit_score=60))

    top = repo.get_top_jobs(limit=2)
    assert len(top) == 2
    assert top[0].title == "Job B"
    assert top[1].title == "Job C"


def test_status_counts():
    """Count jobs by status."""
    repo = make_repo()
    repo.save(Job(title="J1", company="A", location="P", status="new"))
    repo.save(Job(title="J2", company="B", location="P", status="new"))
    repo.save(Job(title="J3", company="C", location="P", status="applied"))

    counts = repo.get_status_counts()
    assert counts["new"] == 2
    assert counts["applied"] == 1


def test_empty_database():
    """Empty database returns empty lists."""
    repo = make_repo()
    assert repo.get_all_jobs() == []
    assert repo.get_top_jobs() == []
    assert repo.get_status_counts() == {}