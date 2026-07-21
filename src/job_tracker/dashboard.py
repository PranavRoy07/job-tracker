from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text
from rich import box

from job_tracker.database.models import Job


console = Console()


def render_dashboard(
    top_jobs: list[Job],
    status_counts: dict[str, int],
    today_jobs: list[Job],
) -> None:
    """Render the complete job tracker dashboard in terminal.

    Displays three sections:
    1. Top 10 jobs by fit score with visual score bars
    2. Application status summary
    3. Today's new listings

    Args:
        top_jobs: List of top-scoring jobs to display.
        status_counts: Dictionary of status -> count.
        today_jobs: List of jobs scraped today.
    """
    console.clear()
    console.print()

    # Header
    header = Text("⚡ JOB INTELLIGENCE ENGINE", style="bold white")
    header_panel = Panel(
        header,
        style="bold cyan",
        box=box.DOUBLE_EDGE,
        padding=(1, 2),
        subtitle="[dim]Powered by Python[/dim]",
    )
    console.print(header_panel, justify="center")
    console.print()

    # Section 1: Top Jobs Table
    _render_top_jobs(top_jobs)
    console.print()

    # Section 2: Status Counts
    _render_status_counts(status_counts)
    console.print()

    # Section 3: Today's Listings
    _render_today_summary(today_jobs)
    console.print()


def _render_top_jobs(jobs: list[Job]) -> None:
    """Render the top jobs table with score bars.

    Args:
        jobs: List of top-scoring jobs.
    """
    table = Table(
        title="🏆 Top 10 Jobs by Fit Score",
        box=box.ROUNDED,
        title_style="bold yellow",
        header_style="bold magenta",
        border_style="bright_blue",
        show_lines=True,
        padding=(0, 1),
    )

    table.add_column("#", style="dim", width=3, justify="center")
    table.add_column("Score", width=7, justify="center")
    table.add_column("Title", style="bold white", min_width=25)
    table.add_column("Company", style="cyan", min_width=15)
    table.add_column("Location", style="green", min_width=12)
    table.add_column("Fit Bar", min_width=22)
    table.add_column("Status", justify="center", width=10)

    for i, job in enumerate(jobs[:10], 1):
        score_color = _get_score_color(job.fit_score)
        score_text = f"[{score_color}]{job.fit_score}[/{score_color}]"
        bar = _make_score_bar(job.fit_score)
        status_text = _format_status(job.status)

        table.add_row(
            str(i),
            score_text,
            job.title,
            job.company,
            job.location,
            bar,
            status_text,
        )

    if not jobs:
        table.add_row(
            "-", "-", "[dim]No jobs found yet[/dim]",
            "-", "-", "-", "-",
        )

    console.print(table)


def _render_status_counts(counts: dict[str, int]) -> None:
    """Render application status summary.

    Args:
        counts: Dictionary of status -> count.
    """
    table = Table(
        title="📊 Application Status",
        box=box.ROUNDED,
        title_style="bold yellow",
        header_style="bold magenta",
        border_style="bright_blue",
    )

    table.add_column("Status", style="bold", min_width=15)
    table.add_column("Count", justify="center", min_width=8)
    table.add_column("Visual", min_width=30)

    status_icons: dict[str, str] = {
        "new": "🆕",
        "applied": "📤",
        "interview": "🎯",
        "rejected": "❌",
        "offer": "🎉",
    }

    total = sum(counts.values()) if counts else 0

    for status, count in sorted(counts.items()):
        icon = status_icons.get(status, "📋")
        bar_width = int((count / max(total, 1)) * 20)
        bar = "█" * bar_width + "░" * (20 - bar_width)
        color = _get_status_color(status)
        table.add_row(
            f"{icon} [{color}]{status.capitalize()}[/{color}]",
            f"[bold]{count}[/bold]",
            f"[{color}]{bar}[/{color}] {count}/{total}",
        )

    if not counts:
        table.add_row("[dim]No data yet[/dim]", "-", "-")

    console.print(table)


def _render_today_summary(jobs: list[Job]) -> None:
    """Render today's new listings summary.

    Args:
        jobs: List of jobs scraped today.
    """
    if not jobs:
        panel = Panel(
            "[dim]No jobs scraped today. Run [bold]job-tracker run[/bold] to fetch new listings![/dim]",
            title="📅 Today's New Listings",
            title_align="left",
            border_style="bright_blue",
            box=box.ROUNDED,
        )
        console.print(panel)
        return

    lines: list[str] = []
    lines.append(f"[bold green]Found {len(jobs)} new listings today![/bold green]\n")

    # Show top 5 from today
    for job in jobs[:5]:
        score_color = _get_score_color(job.fit_score)
        lines.append(
            f"  [{score_color}]●[/{score_color}] "
            f"[bold]{job.title}[/bold] at [cyan]{job.company}[/cyan] "
            f"— [{score_color}]Score: {job.fit_score}[/{score_color}]"
        )

    if len(jobs) > 5:
        lines.append(f"\n  [dim]...and {len(jobs) - 5} more[/dim]")

    panel = Panel(
        "\n".join(lines),
        title="📅 Today's New Listings",
        title_align="left",
        border_style="bright_blue",
        box=box.ROUNDED,
    )
    console.print(panel)

def _format_status(status: str) -> str:
    """Format status with color and icon.

    Args:
        status: The application status string.

    Returns:
        A Rich-formatted status string.
    """
    icons: dict[str, str] = {
        "new": "🆕",
        "applied": "📤",
        "interview": "🎯",
        "rejected": "❌",
        "offer": "🎉",
    }
    icon = icons.get(status, "📋")
    color = _get_status_color(status)
    return f"{icon} [{color}]{status}[/{color}]"

def _make_score_bar(score: int) -> str:
    """Create a visual ASCII bar for a score.

    Args:
        score: The score value (0-100).

    Returns:
        A colored ASCII bar string.
    """
    filled = score // 5           # 20 blocks max
    empty = 20 - filled
    color = _get_score_color(score)
    return f"[{color}]{'█' * filled}[/{color}][dim]{'░' * empty}[/dim] {score}%"


def _get_score_color(score: int) -> str:
    """Get color based on score value.

    Args:
        score: The score value (0-100).

    Returns:
        A Rich color string.
    """
    if score >= 80:
        return "bold green"
    elif score >= 60:
        return "yellow"
    elif score >= 40:
        return "dark_orange"
    else:
        return "red"


def _get_status_color(status: str) -> str:
    """Get color for application status.

    Args:
        status: The status string.

    Returns:
        A Rich color string.
    """
    colors: dict[str, str] = {
        "new": "bright_cyan",
        "applied": "yellow",
        "interview": "green",
        "rejected": "red",
        "offer": "bold green",
    }
    return colors.get(status, "white")