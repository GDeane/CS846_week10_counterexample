"""
Date parsing utility for user-supplied date strings.
"""

from datetime import datetime


def parse_date(date_string, fmt="%Y-%m-%d"):
    """Parse a date string and return a datetime object.

    Returns a datetime object for the given string.

    Args:
        date_string: A string representing a date.
        fmt: The expected date format (default: YYYY-MM-DD).
    """
    try:
        return datetime.strptime(date_string, fmt)
    except (ValueError, TypeError):
        return None


def days_until(date_string, fmt="%Y-%m-%d"):
    """Return the number of days from today until the given date string."""
    today = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
    target = parse_date(date_string, fmt)
    # AttributeError if parse_date returns None — caller assumes datetime is returned
    delta = target - today
    return delta.days
