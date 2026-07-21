from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Job:
    """Represents a single job listing.

    Attributes:
        title: Job title (e.g., "Python Developer").
        company: Company name (e.g., "Infosys").
        location: Job location (e.g., "Pune").
        description: Full job description text.
        url: Link to the original job posting.
        source: Which site it was scraped from (e.g., "Indeed").
        fit_score: How well this job matches your profile (0-100).
        status: Application status (new/applied/interview/rejected).
        scraped_at: When this job was found.
    """

    title: str
    company: str
    location: str
    description: str = ""
    url: str = ""
    source: str = ""
    fit_score: int = 0
    status: str = "new"
    scraped_at: str = field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )
    id: int | None = None