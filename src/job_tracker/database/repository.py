import sqlite3
from datetime import date
from job_tracker.database.models import Job


class JobRepository:
    """Handles all database operations for job listings.

    Uses SQLite to store jobs in a local file. Follows the
    repository pattern — all database logic stays in this class.

    Args:
        db_path: Path to the SQLite database file.
    """

    def __init__(self, db_path: str = "jobs.db") -> None:
        """Initialize the repository and create table if needed.

        Args:
            db_path: Path to the SQLite database file.
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(db_path)
        self.conn.row_factory = sqlite3.Row
        self._create_table()

    def _create_table(self) -> None:
        """Create the jobs table if it doesn't exist."""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS jobs (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                company TEXT NOT NULL,
                location TEXT NOT NULL,
                description TEXT,
                url TEXT,
                source TEXT,
                fit_score INTEGER DEFAULT 0,
                status TEXT DEFAULT 'new',
                scraped_at TEXT
            )
        """)
        self.conn.commit()

    def save(self, job: Job) -> int:
        """Save a job to the database.

        Args:
            job: The Job object to save.

        Returns:
            The ID of the saved job.
        """
        cursor = self.conn.execute(
            """
            INSERT INTO jobs (title, company, location, description,
                              url, source, fit_score, status, scraped_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                job.title, job.company, job.location,
                job.description, job.url, job.source,
                job.fit_score, job.status, job.scraped_at,
            ),
        )
        self.conn.commit()
        return cursor.lastrowid

    def get_top_jobs(self, limit: int = 10) -> list[Job]:
        """Get the top jobs sorted by fit_score (highest first).

        Args:
            limit: Maximum number of jobs to return.

        Returns:
            A list of Job objects sorted by score descending.
        """
        rows = self.conn.execute(
            "SELECT * FROM jobs ORDER BY fit_score DESC LIMIT ?",
            (limit,),
        ).fetchall()
        return [self._row_to_job(row) for row in rows]

    def get_today_jobs(self) -> list[Job]:
        """Get all jobs scraped today.

        Returns:
            A list of Job objects scraped today.
        """
        rows = self.conn.execute(
            "SELECT * FROM jobs WHERE scraped_at LIKE ? ORDER BY fit_score DESC",
            (f"{date.today()}%",),
        ).fetchall()
        return [self._row_to_job(row) for row in rows]

    def get_status_counts(self) -> dict[str, int]:
        """Count jobs grouped by application status.

        Returns:
            A dictionary like {"new": 15, "applied": 3}.
        """
        rows = self.conn.execute(
            "SELECT status, COUNT(*) as count FROM jobs GROUP BY status"
        ).fetchall()
        return {row[0]: row[1] for row in rows}

    def get_all_jobs(self) -> list[Job]:
        """Get all jobs from the database.

        Returns:
            A list of all Job objects.
        """
        rows = self.conn.execute(
            "SELECT * FROM jobs ORDER BY fit_score DESC"
        ).fetchall()
        return [self._row_to_job(row) for row in rows]

    def close(self) -> None:
        """Close the database connection."""
        self.conn.close()

    @staticmethod
    def _row_to_job(row: sqlite3.Row) -> Job:
        """Convert a database row to a Job object.

        Args:
            row: A database row.

        Returns:
            A Job object.
        """
        return Job(
            id=row["id"],
            title=row["title"],
            company=row["company"],
            location=row["location"],
            description=row["description"],
            url=row["url"],
            source=row["source"],
            fit_score=row["fit_score"],
            status=row["status"],
            scraped_at=row["scraped_at"],
        )