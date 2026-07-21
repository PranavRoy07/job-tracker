from job_tracker.scorer import calculate_fit_score


def test_perfect_match():
    """Job matching title, location, and skills scores high."""
    score = calculate_fit_score(
        title="Python Data Analyst",
        location="Pune, Maharashtra",
        description="Need Python, SQL, Power BI experience"
    )
    assert score == 50  # 20 + 15 + 5 + 5 + 5


def test_title_match_only():
    """Only title matches."""
    score = calculate_fit_score(
        title="Data Engineer",
        location="Mumbai",
        description="Java and Spring Boot required"
    )
    assert score == 20


def test_location_match_only():
    """Only location matches."""
    score = calculate_fit_score(
        title="Receptionist",
        location="Pune",
        description="Front desk management"
    )
    assert score == 15


def test_penalty_for_experience():
    """High experience requirement reduces score."""
    score = calculate_fit_score(
        title="Data Analyst",
        location="Pune",
        description="Requires 5+ years of experience in Python"
    )
    # 20 (title) + 15 (location) + 5 (python) - 10 (5+ years) = 30
    assert score == 30


def test_no_match():
    """Nothing matches, score is 0."""
    score = calculate_fit_score(
        title="Chef",
        location="Delhi",
        description="Cooking Italian food"
    )
    assert score == 0


def test_score_never_negative():
    """Score should never go below 0."""
    score = calculate_fit_score(
        title="Manager",
        location="Delhi",
        description="Requires 10+ years of management"
    )
    assert score >= 0


def test_all_skills_match():
    """All skills found in description."""
    score = calculate_fit_score(
        title="Backend Developer",
        location="Pune",
        description="Python, SQL, Power BI, FastAPI, Firebase stack"
    )
    # 20 (title) + 15 (location) + 25 (5 skills × 5) = 60
    assert score == 60