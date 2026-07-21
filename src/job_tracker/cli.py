import sys


def main() -> None:
    """Entry point for the job-tracker CLI command.

    Usage:
        job-tracker run        - Scrape jobs and show dashboard
        job-tracker dashboard  - Show dashboard only
        job-tracker schedule   - Start scheduled daily runs
    """
    if len(sys.argv) < 2:
        print("Usage: job-tracker <command>")
        print("")
        print("Commands:")
        print("  run        Scrape jobs, score them, show dashboard")
        print("  dashboard  Show the dashboard only")
        print("  schedule   Start daily scheduled runs (9 AM)")
        return

    command = sys.argv[1]

    if command == "run":
        print("🚀 Job Tracker is running!")
        print("   (We'll add real functionality step by step)")
    elif command == "dashboard":
        print("📊 Dashboard coming soon!")
    elif command == "schedule":
        print("⏰ Scheduler coming soon!")
    else:
        print(f"❌ Unknown command: {command}")
        print("   Use: job-tracker run | dashboard | schedule")


if __name__ == "__main__":
    main()