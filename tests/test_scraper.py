import pytest
from job_tracker.scraper.base import BaseScraper
from job_tracker.scraper.sample import SampleScraper
from job_tracker.database.models import Job


def test_sample_scraper_returns_jobs():
    """Sample scraper returns a list of jobs."""
    scraper = SampleScraper()
    jobs = scraper.scrape("Python", "Pune")
    assert len(jobs) >= 8
    assert len(jobs) <= 12


def test_sample_scraper_returns_job_objects():
    """Each result is a proper Job object."""
    scraper = SampleScraper()
    jobs = scraper.scrape("Python", "Pune")
    for job in jobs:
        assert isinstance(job, Job)
        assert job.title != ""
        assert job.company != ""
        assert job.source == "Sample"


def test_sample_scraper_inherits_base():
    """SampleScraper properly extends BaseScraper."""
    scraper = SampleScraper()
    assert isinstance(scraper, BaseScraper)


def test_cannot_instantiate_base_scraper():
    """BaseScraper cannot be used directly (it's abstract)."""
    with pytest.raises(TypeError):
        BaseScraper("test")