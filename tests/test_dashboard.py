from job_tracker.database.models import Job
from job_tracker.dashboard import (
    _make_score_bar,
    _get_score_color,
    _get_status_color,
)


def test_score_bar_full():
    """100% score shows full bar."""
    bar = _make_score_bar(100)
    assert "100%" in bar


def test_score_bar_empty():
    """0% score shows empty bar."""
    bar = _make_score_bar(0)
    assert "0%" in bar


def test_score_color_high():
    """High scores get green color."""
    assert "green" in _get_score_color(90)


def test_score_color_low():
    """Low scores get red color."""
    assert _get_score_color(20) == "red"


def test_status_colors():
    """Each status has a color."""
    assert _get_status_color("new") == "bright_cyan"
    assert _get_status_color("applied") == "yellow"
    assert _get_status_color("interview") == "green"
    assert _get_status_color("rejected") == "red"