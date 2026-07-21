import re


# Skills to look for (with their point values)
SKILL_KEYWORDS: dict[str, int] = {
    "python": 5,
    "sql": 5,
    "power bi": 5,
    "fastapi": 5,
    "firebase": 5,
}

# Job titles that match your target roles
TARGET_TITLES: list[str] = [
    "data analyst",
    "data engineer",
    "python developer",
    "software developer",
    "backend developer",
]

# Preferred location
TARGET_LOCATION: str = "pune"

# Penalty keywords
PENALTY_KEYWORDS: list[str] = [
    r"5\+?\s*years",
    r"6\+?\s*years",
    r"7\+?\s*years",
    r"8\+?\s*years",
    r"10\+?\s*years",
]


def calculate_fit_score(title: str, location: str, description: str) -> int:
    """Calculate how well a job matches your profile (0-100).

    Scoring breakdown:
        +20  if title matches target roles
        +15  if location is Pune
        +5   per matching skill in description
        -10  if senior experience required (5+ years)

    Args:
        title: The job title.
        location: The job location.
        description: The full job description text.

    Returns:
        An integer score between 0 and 100.
    """
    score = 0
    text = f"{title} {description}".lower()

    # +20 for matching job title
    title_lower = title.lower()
    for target in TARGET_TITLES:
        if target in title_lower:
            score += 20
            break

    # +15 for Pune location
    if TARGET_LOCATION in location.lower():
        score += 15

    # +5 per matching skill
    for skill, points in SKILL_KEYWORDS.items():
        if skill in text:
            score += points

    # -10 for high experience requirements
    for pattern in PENALTY_KEYWORDS:
        if re.search(pattern, text):
            score -= 10
            break

    # Clamp score between 0 and 100
    return max(0, min(100, score))