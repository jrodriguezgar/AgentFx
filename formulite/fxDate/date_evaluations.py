"""Date evaluation functions.

This module provides utility functions for validating and checking date-related types.
"""

from datetime import datetime


def is_dateclass(p_datetime: datetime) -> bool:
    """Checks if the provided object is a datetime instance.

    Description:
        This function validates whether the input parameter is an instance of the
        datetime class. It provides a simple type check for datetime objects,
        which is useful for input validation and type verification.

    Args:
        p_datetime: The object to check. Expected to be a datetime instance.

    Returns:
        bool: True if the object is a datetime instance, False otherwise.

    Usage Example:
        >>> from datetime import datetime
        >>> from formulite.fxDate.date_evaluations import is_dateclass
        >>> dt = datetime(2026, 1, 3, 10, 30, 0)
        >>> is_dateclass(dt)
        True
        >>> is_dateclass("2026-01-03")
        False
        >>> is_dateclass(None)
        False

    Cost: O(1)
    """
    return isinstance(p_datetime, datetime)

