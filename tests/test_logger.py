import os
import logging
from job_tracker.logger import setup_logger


TEST_LOG = "test_scraper.log"


def test_logger_creates_file():
    """Logger creates a log file."""
    if os.path.exists(TEST_LOG):
        os.remove(TEST_LOG)

    logger = setup_logger(name="test1", log_file=TEST_LOG)
    logger.info("Test message")

    assert os.path.exists(TEST_LOG)

    # Clean up
    logger.handlers.clear()
    os.remove(TEST_LOG)


def test_logger_returns_logger():
    """setup_logger returns a Logger object."""
    logger = setup_logger(name="test2", log_file=TEST_LOG)
    assert isinstance(logger, logging.Logger)
    logger.handlers.clear()
    if os.path.exists(TEST_LOG):
        os.remove(TEST_LOG)


def test_logger_writes_to_file():
    """Logger writes messages to the log file."""
    if os.path.exists(TEST_LOG):
        os.remove(TEST_LOG)

    logger = setup_logger(name="test3", log_file=TEST_LOG)
    logger.info("Hello from test")

    with open(TEST_LOG, "r") as f:
        content = f.read()
    assert "Hello from test" in content

    logger.handlers.clear()
    os.remove(TEST_LOG)