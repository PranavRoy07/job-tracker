import logging
from pathlib import Path


def setup_logger(
    name: str = "job_tracker",
    log_file: str = "scraper.log",
    level: int = logging.INFO,
) -> logging.Logger:
    """Set up a logger that writes to both file and terminal.

    Creates a logger that:
    - Writes detailed logs to scraper.log (for debugging later)
    - Shows important messages in the terminal (so you see what's happening)

    Args:
        name: Name of the logger.
        log_file: Path to the log file.
        level: Minimum log level (DEBUG, INFO, WARNING, ERROR).

    Returns:
        A configured Logger instance.
    """
    logger = logging.getLogger(name)

    # Don't add handlers twice if called again
    if logger.handlers:
        return logger

    logger.setLevel(level)

    # Format: timestamp - level - message
    formatter = logging.Formatter(
        "%(asctime)s  %(levelname)-8s  %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # Handler 1: Write to file (scraper.log)
    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Handler 2: Print to terminal
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger