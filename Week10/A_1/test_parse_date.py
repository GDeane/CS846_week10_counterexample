"""
Example tests for parse_date.py.
"""

import pytest
from datetime import datetime
from parse_date import parse_date, days_until


def test_valid_date_returns_datetime():
    result = parse_date("2026-06-15")
    assert isinstance(result, datetime)
    assert result.year == 2026
    assert result.month == 6
    assert result.day == 15


def test_invalid_date_returns_none():
    result = parse_date("not-a-date")
    assert result is None


def test_none_input_returns_none():
    result = parse_date(None)
    assert result is None


def test_days_until_valid_date():
    # Should return an integer without error for a valid future date
    result = days_until("2099-01-01")
    assert isinstance(result, int)
    assert result > 0


def test_days_until_invalid_date_raises():
    # Demonstrates the downstream AttributeError caused by the None return:
    # parse_date("bad") returns None, then None - datetime raises AttributeError.
    with pytest.raises(AttributeError):
        days_until("bad-date")
