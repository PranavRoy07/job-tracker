from abc import ABC, abstractmethod
from job_tracker.database.models import Job


class BaseScraper(ABC):
    """Abstract base class that all scrapers must follow.

    Every scraper (Indeed, LinkedIn, etc.) must implement
    the scrape() method. This ensures all scrapers work
    the same way — you can swap one for another easily.

    Attributes:
        source: Name of the job site being scraped.
    """

    def __init__(self, source: str) -> None:
        """Initialize the scraper with a source name.

        Args:
            source: The name of the job site (e.g., "Indeed").
        """
        self.source = source

    @abstractmethod
    def scrape(self, query: str, location: str) -> list[Job]:
        """Scrape job listings from the source.

        This method MUST be implemented by every scraper.

        Args:
            query: Job search query (e.g., "Python Developer").
            location: Location to search (e.g., "Pune").

        Returns:
            A list of Job objects found.
        """
        pass