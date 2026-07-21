import random
from job_tracker.scraper.base import BaseScraper
from job_tracker.database.models import Job


# Realistic fake job data for Pune tech market
SAMPLE_JOBS: list[dict[str, str]] = [
    {
        "title": "Python Developer",
        "company": "Infosys",
        "location": "Pune, Maharashtra",
        "description": "Looking for Python developer with SQL, FastAPI experience. 2+ years required. Work on data pipelines and REST APIs.",
        "url": "https://example.com/jobs/1",
    },
    {
        "title": "Data Analyst",
        "company": "TCS",
        "location": "Pune, India",
        "description": "Data Analyst role. Must know Python, SQL, Power BI. Create dashboards and reports. Freshers welcome.",
        "url": "https://example.com/jobs/2",
    },
    {
        "title": "Senior Backend Engineer",
        "company": "Wipro",
        "location": "Pune",
        "description": "Senior backend role. Java, Spring Boot, microservices. 5+ years required. Cloud experience preferred.",
        "url": "https://example.com/jobs/3",
    },
    {
        "title": "Data Engineer",
        "company": "Persistent Systems",
        "location": "Pune, Maharashtra",
        "description": "Build data pipelines using Python, SQL, Apache Spark. Firebase for real-time data. 1-3 years experience.",
        "url": "https://example.com/jobs/4",
    },
    {
        "title": "Full Stack Developer",
        "company": "Zensar Technologies",
        "location": "Pune",
        "description": "React + Node.js developer. MongoDB, Express. No Python required. 2 years experience.",
        "url": "https://example.com/jobs/5",
    },
    {
        "title": "Software Developer - Python",
        "company": "Amdocs",
        "location": "Pune, India",
        "description": "Python, FastAPI, SQL, REST APIs. Build automation tools. Firebase integration. Freshers to 2 years.",
        "url": "https://example.com/jobs/6",
    },
    {
        "title": "Business Analyst",
        "company": "Cognizant",
        "location": "Mumbai, Maharashtra",
        "description": "Business analysis, requirements gathering. Power BI dashboards. SQL queries. 3 years experience.",
        "url": "https://example.com/jobs/7",
    },
    {
        "title": "DevOps Engineer",
        "company": "Tech Mahindra",
        "location": "Pune",
        "description": "CI/CD pipelines, Docker, Kubernetes. AWS or Azure. 5+ years required. No Python needed.",
        "url": "https://example.com/jobs/8",
    },
    {
        "title": "Python Data Analyst",
        "company": "Cybage",
        "location": "Pune, Maharashtra",
        "description": "Analyze data using Python, SQL, Power BI. Build automated reports. FastAPI for internal tools. 0-2 years.",
        "url": "https://example.com/jobs/9",
    },
    {
        "title": "Machine Learning Engineer",
        "company": "NVIDIA",
        "location": "Pune",
        "description": "ML models, Python, TensorFlow. Deep learning research. 3+ years required. PhD preferred.",
        "url": "https://example.com/jobs/10",
    },
    {
        "title": "Junior Python Developer",
        "company": "Accenture",
        "location": "Pune, India",
        "description": "Entry level Python role. Learn FastAPI, SQL databases. Firebase for mobile backends. Freshers welcome.",
        "url": "https://example.com/jobs/11",
    },
    {
        "title": "Data Analyst - Power BI",
        "company": "Deloitte",
        "location": "Hyderabad",
        "description": "Power BI dashboards, SQL, Excel. Some Python scripting. 2-4 years experience required.",
        "url": "https://example.com/jobs/12",
    },
    {
        "title": "Backend Developer",
        "company": "ThoughtWorks",
        "location": "Pune, Maharashtra",
        "description": "Python, FastAPI, PostgreSQL. Build microservices. 1-3 years. Agile methodology.",
        "url": "https://example.com/jobs/13",
    },
    {
        "title": "Senior Data Analyst",
        "company": "Capgemini",
        "location": "Pune",
        "description": "Lead data analytics team. Python, SQL, Power BI. 7+ years required. Management experience needed.",
        "url": "https://example.com/jobs/14",
    },
    {
        "title": "Software Engineer",
        "company": "Qualcomm",
        "location": "Chennai",
        "description": "C++ and embedded systems. RTOS development. 3+ years. No Python.",
        "url": "https://example.com/jobs/15",
    },
]


class SampleScraper(BaseScraper):
    """A scraper that returns realistic sample job data.

    Used for development and testing. Returns jobs from a
    curated list of realistic Pune tech job listings.
    Replace this with real scrapers (Indeed, LinkedIn) later.
    """

    def __init__(self) -> None:
        """Initialize the sample scraper."""
        super().__init__(source="Sample")

    def scrape(self, query: str, location: str) -> list[Job]:
        """Return sample job listings.

        Randomly selects 8-12 jobs from the sample data
        to simulate a real scraping session.

        Args:
            query: Job search query (used for filtering).
            location: Location to search in.

        Returns:
            A list of Job objects from sample data.
        """
        # Randomly pick 8-12 jobs to simulate real scraping
        count = random.randint(8, min(12, len(SAMPLE_JOBS)))
        selected = random.sample(SAMPLE_JOBS, count)

        jobs: list[Job] = []
        for data in selected:
            job = Job(
                title=data["title"],
                company=data["company"],
                location=data["location"],
                description=data["description"],
                url=data["url"],
                source=self.source,
            )
            jobs.append(job)

        return jobs