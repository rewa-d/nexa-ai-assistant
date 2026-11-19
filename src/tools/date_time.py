from datetime import datetime
from zoneinfo import ZoneInfo

def get_current_datetime(timezone: str = "local") -> str:
    """Return the current date and time for a given timezone."""

    if timezone.lower() == "local":
        now = datetime.now().astimezone()
    else:
        try:
            now = datetime.now(ZoneInfo(timezone))
        except (KeyError, ValueError):
            return f"Invalid timezone: {timezone}"

    return now.strftime(
        "%A, %d %B %Y, %I:%M %p (%Z)"
    )
