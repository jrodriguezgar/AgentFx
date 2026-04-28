"""Date evaluation functions.

This module provides utility functions for validating and checking date-related
types and temporal properties such as past, future, and same-day comparisons.
"""

from datetime import datetime, date
from typing import Union
import calendar
import math
import zoneinfo


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
        >>> from shortfx.fxDate.date_evaluations import is_dateclass
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


def is_past(date_input: Union[datetime, date]) -> bool:
    """Checks if a date is strictly in the past.

    Description:
        Returns True when *date_input* is earlier than the current date/time.
        For ``date`` objects the comparison is date-only; for ``datetime``
        objects it includes the time component.

    Args:
        date_input: The date or datetime to evaluate.

    Returns:
        bool: True if the date is in the past, False otherwise.

    Raises:
        TypeError: If *date_input* is not a date or datetime.

    Example:
        >>> from datetime import datetime, date, timedelta
        >>> is_past(datetime(2020, 1, 1))
        True
        >>> is_past(datetime(2099, 12, 31))
        False

    Complexity: O(1)
    """
    if isinstance(date_input, datetime):
        return date_input < datetime.now()

    if isinstance(date_input, date):
        return date_input < date.today()

    raise TypeError("Input 'date_input' must be a date or datetime object.")


def is_future(date_input: Union[datetime, date]) -> bool:
    """Checks if a date is strictly in the future.

    Description:
        Returns True when *date_input* is later than the current date/time.

    Args:
        date_input: The date or datetime to evaluate.

    Returns:
        bool: True if the date is in the future, False otherwise.

    Raises:
        TypeError: If *date_input* is not a date or datetime.

    Example:
        >>> from datetime import datetime
        >>> is_future(datetime(2099, 12, 31))
        True
        >>> is_future(datetime(2020, 1, 1))
        False

    Complexity: O(1)
    """
    if isinstance(date_input, datetime):
        return date_input > datetime.now()

    if isinstance(date_input, date):
        return date_input > date.today()

    raise TypeError("Input 'date_input' must be a date or datetime object.")


def is_today(date_input: Union[datetime, date]) -> bool:
    """Checks if a date falls on today's calendar date.

    Description:
        Compares only the date portion, ignoring any time component.

    Args:
        date_input: The date or datetime to evaluate.

    Returns:
        bool: True if the date is today, False otherwise.

    Raises:
        TypeError: If *date_input* is not a date or datetime.

    Example:
        >>> from datetime import datetime, date
        >>> is_today(datetime.now())
        True
        >>> is_today(date(2000, 1, 1))
        False

    Complexity: O(1)
    """
    if isinstance(date_input, datetime):
        return date_input.date() == date.today()

    if isinstance(date_input, date):
        return date_input == date.today()

    raise TypeError("Input 'date_input' must be a date or datetime object.")


def is_same_day(date1: Union[datetime, date], date2: Union[datetime, date]) -> bool:
    """Checks if two dates fall on the same calendar day.

    Description:
        Compares only the date portion of both inputs, ignoring time.

    Args:
        date1: First date or datetime.
        date2: Second date or datetime.

    Returns:
        bool: True if both dates share the same year, month, and day.

    Raises:
        TypeError: If either argument is not a date or datetime.

    Example:
        >>> from datetime import datetime
        >>> is_same_day(datetime(2025, 6, 15, 8, 0), datetime(2025, 6, 15, 23, 59))
        True
        >>> is_same_day(datetime(2025, 6, 15), datetime(2025, 6, 16))
        False

    Complexity: O(1)
    """
    def _to_date(val: Union[datetime, date]) -> date:
        if isinstance(val, datetime):
            return val.date()

        if isinstance(val, date):
            return val

        raise TypeError("Arguments must be date or datetime objects.")

    return _to_date(date1) == _to_date(date2)


def is_same_month(date1: Union[datetime, date], date2: Union[datetime, date]) -> bool:
    """Checks if two dates fall in the same month and year.

    Args:
        date1: First date or datetime.
        date2: Second date or datetime.

    Returns:
        bool: True if both dates share the same year and month.

    Raises:
        TypeError: If either argument is not a date or datetime.

    Example:
        >>> from datetime import datetime
        >>> is_same_month(datetime(2025, 6, 1), datetime(2025, 6, 30))
        True
        >>> is_same_month(datetime(2025, 6, 1), datetime(2025, 7, 1))
        False

    Complexity: O(1)
    """
    if not isinstance(date1, (datetime, date)) or not isinstance(date2, (datetime, date)):
        raise TypeError("Arguments must be date or datetime objects.")

    return date1.year == date2.year and date1.month == date2.month


def is_same_year(date1: Union[datetime, date], date2: Union[datetime, date]) -> bool:
    """Checks if two dates fall in the same year.

    Args:
        date1: First date or datetime.
        date2: Second date or datetime.

    Returns:
        bool: True if both dates share the same year.

    Raises:
        TypeError: If either argument is not a date or datetime.

    Example:
        >>> from datetime import datetime
        >>> is_same_year(datetime(2025, 1, 1), datetime(2025, 12, 31))
        True
        >>> is_same_year(datetime(2025, 1, 1), datetime(2026, 1, 1))
        False

    Complexity: O(1)
    """
    if not isinstance(date1, (datetime, date)) or not isinstance(date2, (datetime, date)):
        raise TypeError("Arguments must be date or datetime objects.")

    return date1.year == date2.year


def is_same_week(date1: Union[datetime, date], date2: Union[datetime, date]) -> bool:
    """Checks if two dates fall in the same ISO week and year.

    Args:
        date1: First date or datetime.
        date2: Second date or datetime.

    Returns:
        bool: True if both dates share the same ISO year and week number.

    Raises:
        TypeError: If either argument is not a date or datetime.

    Example:
        >>> from datetime import datetime
        >>> is_same_week(datetime(2026, 4, 6), datetime(2026, 4, 10))
        True
        >>> is_same_week(datetime(2026, 4, 5), datetime(2026, 4, 6))
        False

    Complexity: O(1)
    """
    if not isinstance(date1, (datetime, date)) or not isinstance(date2, (datetime, date)):
        raise TypeError("Arguments must be date or datetime objects.")

    iso1 = date1.isocalendar()
    iso2 = date2.isocalendar()

    return iso1[0] == iso2[0] and iso1[1] == iso2[1]


def is_same_quarter(date1: Union[datetime, date], date2: Union[datetime, date]) -> bool:
    """Checks if two dates fall in the same quarter and year.

    Args:
        date1: First date or datetime.
        date2: Second date or datetime.

    Returns:
        bool: True if both dates share the same year and quarter (Q1-Q4).

    Raises:
        TypeError: If either argument is not a date or datetime.

    Example:
        >>> from datetime import datetime
        >>> is_same_quarter(datetime(2026, 1, 15), datetime(2026, 3, 31))
        True
        >>> is_same_quarter(datetime(2026, 3, 31), datetime(2026, 4, 1))
        False

    Complexity: O(1)
    """
    if not isinstance(date1, (datetime, date)) or not isinstance(date2, (datetime, date)):
        raise TypeError("Arguments must be date or datetime objects.")

    return date1.year == date2.year and (date1.month - 1) // 3 == (date2.month - 1) // 3


def is_business_hours(
    dt: datetime,
    start_hour: int = 9,
    end_hour: int = 17,
) -> bool:
    """Checks if a datetime falls within business hours on a weekday.

    A datetime is considered business hours when the day is Monday–Friday
    and the time is between ``start_hour`` (inclusive) and ``end_hour``
    (exclusive).

    Args:
        dt: The datetime to evaluate.
        start_hour: Opening hour in 24-h format (default 9).
        end_hour: Closing hour in 24-h format (default 17).

    Returns:
        True if dt is within business hours, False otherwise.

    Raises:
        TypeError: If dt is not a datetime object.

    Example:
        >>> from datetime import datetime
        >>> is_business_hours(datetime(2026, 4, 6, 10, 30))  # Monday 10:30
        True
        >>> is_business_hours(datetime(2026, 4, 5, 10, 30))  # Sunday 10:30
        False
        >>> is_business_hours(datetime(2026, 4, 6, 18, 0))   # Monday 18:00
        False

    Complexity: O(1)
    """
    if not isinstance(dt, datetime):
        raise TypeError("Input must be a datetime object.")

    # Monday=0 ... Sunday=6; weekdays are 0-4
    if dt.weekday() > 4:
        return False

    return start_hour <= dt.hour < end_hour


def is_anniversary(
    reference: Union[datetime, date],
    target: Union[datetime, date],
) -> bool:
    """Checks if target falls on the same month and day as reference.

    Useful for detecting birthdays, founding dates, or recurring
    annual events regardless of year.

    Args:
        reference: The original date (anniversary origin).
        target: The date to check.

    Returns:
        True if month and day match, False otherwise.

    Raises:
        TypeError: If arguments are not date/datetime objects.

    Example:
        >>> from datetime import date
        >>> is_anniversary(date(1990, 7, 4), date(2026, 7, 4))
        True
        >>> is_anniversary(date(1990, 7, 4), date(2026, 7, 5))
        False

    Complexity: O(1)
    """
    if not isinstance(reference, (datetime, date)) or not isinstance(target, (datetime, date)):
        raise TypeError("Arguments must be date or datetime objects.")

    return reference.month == target.month and reference.day == target.day


def is_last_day_of_month(d: Union[datetime, date]) -> bool:
    """Checks if a date is the last day of its month.

    Args:
        d: The date to evaluate.

    Returns:
        True if d is the last day of its month, False otherwise.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_last_day_of_month(date(2024, 2, 29))
        True
        >>> is_last_day_of_month(date(2024, 2, 28))
        False
        >>> is_last_day_of_month(date(2023, 2, 28))
        True

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("Input must be a date or datetime object.")

    last_day = calendar.monthrange(d.year, d.month)[1]
    return d.day == last_day


def is_dst(dt: datetime, tz_name: str = "UTC") -> bool:
    """Checks if a datetime falls within Daylight Saving Time.

    Uses a simple rule-based approach for common time zones.
    For 'US/Eastern', 'US/Central', 'US/Mountain', 'US/Pacific':
    DST starts second Sunday of March at 2:00 AM, ends first Sunday
    of November at 2:00 AM.  For 'Europe/London', 'Europe/Berlin',
    'Europe/Paris', 'Europe/Madrid': DST starts last Sunday of March
    at 1:00 AM UTC, ends last Sunday of October at 1:00 AM UTC.

    Args:
        dt: The datetime to check (naive; interpreted in the named zone).
        tz_name: Time zone identifier.

    Returns:
        True if the datetime is within DST, False otherwise.

    Raises:
        TypeError: If dt is not a datetime.
        ValueError: If tz_name is not supported.

    Example:
        >>> from datetime import datetime
        >>> is_dst(datetime(2026, 7, 15, 12, 0), "US/Eastern")
        True
        >>> is_dst(datetime(2026, 1, 15, 12, 0), "US/Eastern")
        False

    Complexity: O(1)
    """
    if not isinstance(dt, datetime):
        raise TypeError("Input must be a datetime object.")

    us_zones = {"US/Eastern", "US/Central", "US/Mountain", "US/Pacific"}
    eu_zones = {"Europe/London", "Europe/Berlin", "Europe/Paris", "Europe/Madrid"}

    if tz_name == "UTC":
        return False

    if tz_name in us_zones:
        # Second Sunday of March
        march_first = datetime(dt.year, 3, 1)
        days_to_sun = (6 - march_first.weekday()) % 7
        second_sun = march_first.replace(day=1 + days_to_sun + 7, hour=2)

        # First Sunday of November
        nov_first = datetime(dt.year, 11, 1)
        days_to_sun_nov = (6 - nov_first.weekday()) % 7
        first_sun_nov = nov_first.replace(day=1 + days_to_sun_nov, hour=2)

        return second_sun <= dt < first_sun_nov

    if tz_name in eu_zones:

        # Last Sunday of March
        march_last = 31 - (datetime(dt.year, 3, 31).weekday() + 1) % 7
        dst_start = datetime(dt.year, 3, march_last, 1)

        # Last Sunday of October
        oct_last = 31 - (datetime(dt.year, 10, 31).weekday() + 1) % 7
        dst_end = datetime(dt.year, 10, oct_last, 1)

        return dst_start <= dt < dst_end

    raise ValueError(
        f"Unsupported timezone '{tz_name}'. Supported: UTC, "
        f"{', '.join(sorted(us_zones | eu_zones))}"
    )


def zodiac_sign(d: Union[datetime, date]) -> str:
    """Returns the Western zodiac sign for a date.

    Args:
        d: A date or datetime.

    Returns:
        Zodiac sign name in English (e.g. ``"Aries"``).

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> zodiac_sign(date(2024, 8, 15))
        'Leo'

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a datetime or date object.")

    dt = d.date() if isinstance(d, datetime) else d
    md = (dt.month, dt.day)

    # (end_month, end_day, sign_name)
    _SIGNS = [
        (1, 19, "Capricorn"), (2, 18, "Aquarius"), (3, 20, "Pisces"),
        (4, 19, "Aries"), (5, 20, "Taurus"), (6, 20, "Gemini"),
        (7, 22, "Cancer"), (8, 22, "Leo"), (9, 22, "Virgo"),
        (10, 22, "Libra"), (11, 21, "Scorpio"), (12, 21, "Sagittarius"),
    ]

    for end_m, end_d, name in _SIGNS:

        if md <= (end_m, end_d):
            return name

    return "Capricorn"


def chinese_zodiac(year: int) -> str:
    """Returns the Chinese zodiac animal for a given year.

    Args:
        year: A calendar year (e.g. 2024).

    Returns:
        Animal name in English (e.g. ``"Dragon"``).

    Raises:
        TypeError: If year is not an integer.

    Example:
        >>> chinese_zodiac(2024)
        'Dragon'

    Complexity: O(1)
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer.")

    _ANIMALS = [
        "Monkey", "Rooster", "Dog", "Pig",
        "Rat", "Ox", "Tiger", "Rabbit",
        "Dragon", "Snake", "Horse", "Goat",
    ]

    return _ANIMALS[year % 12]


def is_first_of_month(d: Union[datetime, date]) -> bool:
    """Check if a date falls on the first day of the month.

    Args:
        d: Date or datetime to check.

    Returns:
        True if d is the first day of the month.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_first_of_month(date(2024, 1, 1))
        True
        >>> is_first_of_month(date(2024, 1, 15))
        False

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    return d.day == 1


def is_end_of_quarter(d: Union[datetime, date]) -> bool:
    """Check if a date falls on the last day of a calendar quarter.

    Quarter end dates: Mar 31, Jun 30, Sep 30, Dec 31.

    Args:
        d: Date or datetime to check.

    Returns:
        True if d is the last day of a quarter.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_end_of_quarter(date(2024, 3, 31))
        True
        >>> is_end_of_quarter(date(2024, 4, 15))
        False

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    _QUARTER_ENDS = {(3, 31), (6, 30), (9, 30), (12, 31)}

    return (d.month, d.day) in _QUARTER_ENDS


def is_start_of_quarter(d: Union[datetime, date]) -> bool:
    """Check if a date falls on the first day of a calendar quarter.

    Quarter start dates: Jan 1, Apr 1, Jul 1, Oct 1.

    Args:
        d: Date or datetime to check.

    Returns:
        True if d is the first day of a quarter.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_start_of_quarter(date(2024, 1, 1))
        True
        >>> is_start_of_quarter(date(2024, 2, 1))
        False

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    _QUARTER_STARTS = {(1, 1), (4, 1), (7, 1), (10, 1)}

    return (d.month, d.day) in _QUARTER_STARTS


def is_century_year(year: int) -> bool:
    """Check if a year is a century year (divisible by 100).

    Args:
        year: Year to check.

    Returns:
        True if year is divisible by 100.

    Raises:
        TypeError: If year is not an integer.

    Example:
        >>> is_century_year(2000)
        True
        >>> is_century_year(2024)
        False

    Complexity: O(1)
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer.")

    return year % 100 == 0


def is_millennium_year(year: int) -> bool:
    """Check if a year is a millennium year (divisible by 1000).

    Args:
        year: Year to check.

    Returns:
        True if year is divisible by 1000.

    Raises:
        TypeError: If year is not an integer.

    Example:
        >>> is_millennium_year(2000)
        True
        >>> is_millennium_year(2024)
        False

    Complexity: O(1)
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer.")

    return year % 1000 == 0


def is_palindrome_date(d: Union[datetime, date]) -> bool:
    """Check if a date is a palindrome in YYYYMMDD format.

    A palindrome date reads the same forwards and backwards, e.g. 2021-12-02
    → "20211202" is a palindrome.

    Args:
        d: Date or datetime to check.

    Returns:
        True if the YYYYMMDD string is a palindrome.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_palindrome_date(date(2021, 12, 2))
        True
        >>> is_palindrome_date(date(2024, 1, 1))
        False

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d
    s = f"{dt.year:04d}{dt.month:02d}{dt.day:02d}"

    return s == s[::-1]


def week_parity(d: Union[datetime, date]) -> str:
    """Return whether the ISO week number is even or odd.

    Args:
        d: Date or datetime.

    Returns:
        ``"even"`` or ``"odd"``.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> week_parity(date(2025, 1, 6))
        'even'

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d
    iso_week = dt.isocalendar()[1]

    return "even" if iso_week % 2 == 0 else "odd"


def generation_name(year: int) -> str:
    """Return the generational cohort name for a birth year.

    Ranges (approximate, commonly used):
    - Silent Generation: 1928-1945
    - Baby Boomers: 1946-1964
    - Generation X: 1965-1980
    - Millennials (Gen Y): 1981-1996
    - Generation Z: 1997-2012
    - Generation Alpha: 2013-2025

    Args:
        year: Birth year.

    Returns:
        Generation name as a string.

    Raises:
        TypeError: If year is not an integer.
        ValueError: If year is before 1928 or after 2025.

    Example:
        >>> generation_name(1990)
        'Millennial'

    Complexity: O(1)
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer.")

    if year < 1928 or year > 2025:
        raise ValueError("year must be between 1928 and 2025.")

    if year <= 1945:
        return "Silent Generation"

    if year <= 1964:
        return "Baby Boomer"

    if year <= 1980:
        return "Generation X"

    if year <= 1996:
        return "Millennial"

    if year <= 2012:
        return "Generation Z"

    return "Generation Alpha"


def is_weekday(d: Union[datetime, date]) -> bool:
    """Check if a date falls on a weekday (Monday–Friday).

    Args:
        d: Date or datetime to check.

    Returns:
        True if the date is Monday through Friday, False otherwise.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_weekday(date(2025, 6, 9))
        True
        >>> is_weekday(date(2025, 6, 8))
        False

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return dt.weekday() < 5


def days_until_next_birthday(
    birth_date: Union[datetime, date],
    reference: Union[datetime, date, None] = None,
) -> int:
    """Calculate the number of days until the next birthday.

    Args:
        birth_date: The person's date of birth.
        reference: Reference date (default: today).

    Returns:
        Days remaining until the next birthday (0 if today is the birthday).

    Raises:
        TypeError: If inputs are not date or datetime.

    Example:
        >>> from datetime import date
        >>> days_until_next_birthday(date(1990, 6, 15), date(2025, 6, 10))
        5

    Complexity: O(1)
    """
    if not isinstance(birth_date, (datetime, date)):
        raise TypeError("birth_date must be a date or datetime.")

    bd = birth_date.date() if isinstance(birth_date, datetime) else birth_date

    if reference is None:
        ref = date.today()
    elif isinstance(reference, datetime):
        ref = reference.date()
    elif isinstance(reference, date):
        ref = reference
    else:
        raise TypeError("reference must be a date or datetime.")

    next_bday = date(ref.year, bd.month, bd.day) if bd.month != 2 or bd.day != 29 else None

    if next_bday is None:
        # Handle Feb 29 birthdays
        if calendar.isleap(ref.year):
            next_bday = date(ref.year, 2, 29)
        elif calendar.isleap(ref.year + 1):
            next_bday = date(ref.year + 1, 2, 29)
        else:
            # Next leap year
            year = ref.year + 1

            while not calendar.isleap(year):
                year += 1

            next_bday = date(year, 2, 29)

    if next_bday < ref:
        # Birthday already passed this year
        if bd.month == 2 and bd.day == 29:
            year = ref.year + 1

            while not calendar.isleap(year):
                year += 1

            next_bday = date(year, 2, 29)
        else:
            next_bday = date(ref.year + 1, bd.month, bd.day)

    return (next_bday - ref).days


def fiscal_quarter(d: Union[datetime, date], fiscal_start_month: int = 1) -> int:
    """Return the fiscal quarter (1-4) for a given date.

    Args:
        d: Date or datetime.
        fiscal_start_month: Month when the fiscal year starts (1-12, default 1 = Jan).

    Returns:
        Fiscal quarter number (1-4).

    Raises:
        TypeError: If d is not a date or datetime.
        ValueError: If fiscal_start_month is not between 1 and 12.

    Example:
        >>> from datetime import date
        >>> fiscal_quarter(date(2025, 3, 15))
        1
        >>> fiscal_quarter(date(2025, 3, 15), fiscal_start_month=4)
        4

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    if not isinstance(fiscal_start_month, int) or not 1 <= fiscal_start_month <= 12:
        raise ValueError("fiscal_start_month must be between 1 and 12.")

    dt = d.date() if isinstance(d, datetime) else d
    adjusted_month = (dt.month - fiscal_start_month) % 12

    return adjusted_month // 3 + 1


def iso_day_name(d: Union[datetime, date]) -> str:
    """Return the English name of the day of the week.

    Args:
        d: Date or datetime.

    Returns:
        Day name (e.g. ``"Monday"``).

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> iso_day_name(date(2025, 6, 9))
        'Monday'

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    names = ("Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday")
    dt = d.date() if isinstance(d, datetime) else d

    return names[dt.weekday()]


def days_in_year(year: int) -> int:
    """Return the number of days in a given year (365 or 366).

    Args:
        year: Calendar year.

    Returns:
        365 for common years, 366 for leap years.

    Raises:
        TypeError: If year is not an integer.

    Example:
        >>> days_in_year(2024)
        366
        >>> days_in_year(2025)
        365

    Complexity: O(1)
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer.")

    return 366 if calendar.isleap(year) else 365


def nth_weekday_of_month(
    year: int,
    month: int,
    weekday: int,
    n: int,
) -> date:
    """Return the date of the n-th occurrence of a weekday in a month.

    Useful for holidays like "3rd Monday of January" (MLK Day).

    Args:
        year: Calendar year.
        month: Month (1-12).
        weekday: ISO weekday (1=Monday … 7=Sunday).
        n: Occurrence (1 = first, 2 = second, etc.).

    Returns:
        The date of the n-th weekday.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If month, weekday, or n are out of range, or
            the n-th occurrence does not exist.

    Example:
        >>> nth_weekday_of_month(2025, 1, 1, 3)
        datetime.date(2025, 1, 20)

    Complexity: O(1)
    """
    if not all(isinstance(v, int) for v in (year, month, weekday, n)):
        raise TypeError("all arguments must be integers.")

    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12.")

    if not 1 <= weekday <= 7:
        raise ValueError("weekday must be between 1 (Monday) and 7 (Sunday).")

    if n < 1:
        raise ValueError("n must be a positive integer.")

    # weekday: ISO 1=Mon..7=Sun → Python 0=Mon..6=Sun
    target_wd = weekday - 1

    first_day = date(year, month, 1)
    first_wd = first_day.weekday()

    # Days until first occurrence of target weekday
    days_ahead = (target_wd - first_wd) % 7
    first_occurrence = 1 + days_ahead
    target_day = first_occurrence + 7 * (n - 1)

    _, month_length = calendar.monthrange(year, month)

    if target_day > month_length:
        raise ValueError(
            f"The {n}-th occurrence of weekday {weekday} does not exist "
            f"in {year}-{month:02d}."
        )

    return date(year, month, target_day)


def age_at_date(
    birth_date: Union[datetime, date],
    reference: Union[datetime, date, None] = None,
) -> int:
    """Calculate age in complete years at a reference date.

    Args:
        birth_date: Date of birth.
        reference: Reference date (default: today).

    Returns:
        Age in complete years.

    Raises:
        TypeError: If inputs are not date or datetime.
        ValueError: If birth_date is in the future relative to reference.

    Example:
        >>> from datetime import date
        >>> age_at_date(date(1990, 6, 15), date(2025, 6, 14))
        34
        >>> age_at_date(date(1990, 6, 15), date(2025, 6, 15))
        35

    Complexity: O(1)
    """
    if not isinstance(birth_date, (datetime, date)):
        raise TypeError("birth_date must be a date or datetime.")

    bd = birth_date.date() if isinstance(birth_date, datetime) else birth_date

    if reference is None:
        ref = date.today()
    elif isinstance(reference, datetime):
        ref = reference.date()
    elif isinstance(reference, date):
        ref = reference
    else:
        raise TypeError("reference must be a date or datetime.")

    if bd > ref:
        raise ValueError("birth_date must not be in the future.")

    age = ref.year - bd.year

    if (ref.month, ref.day) < (bd.month, bd.day):
        age -= 1

    return age


def workdays_in_month(year: int, month: int) -> int:
    """Count the number of weekdays (Mon-Fri) in a given month.

    Args:
        year: Calendar year.
        month: Month (1-12).

    Returns:
        Number of weekdays.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If month is out of range.

    Example:
        >>> workdays_in_month(2025, 6)
        21

    Complexity: O(days_in_month)
    """
    if not isinstance(year, int) or not isinstance(month, int):
        raise TypeError("year and month must be integers.")

    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12.")

    _, days = calendar.monthrange(year, month)
    count = 0

    for day in range(1, days + 1):

        if date(year, month, day).weekday() < 5:
            count += 1

    return count


def semester_of_year(d: Union[datetime, date]) -> int:
    """Return the semester (1 or 2) of the year.

    Jan–Jun → 1, Jul–Dec → 2.

    Args:
        d: Date or datetime.

    Returns:
        1 or 2.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> semester_of_year(date(2025, 3, 15))
        1
        >>> semester_of_year(date(2025, 9, 15))
        2

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return 1 if dt.month <= 6 else 2


def weeks_between_dates(
    date1: Union[datetime, date],
    date2: Union[datetime, date],
) -> int:
    """Calculate the number of complete weeks between two dates.

    Args:
        date1: Start date.
        date2: End date.

    Returns:
        Number of complete weeks (absolute value).

    Raises:
        TypeError: If inputs are not date or datetime.

    Example:
        >>> from datetime import date
        >>> weeks_between_dates(date(2025, 1, 1), date(2025, 3, 1))
        8

    Complexity: O(1)
    """
    if not isinstance(date1, (datetime, date)):
        raise TypeError("date1 must be a date or datetime.")

    if not isinstance(date2, (datetime, date)):
        raise TypeError("date2 must be a date or datetime.")

    d1 = date1.date() if isinstance(date1, datetime) else date1
    d2 = date2.date() if isinstance(date2, datetime) else date2

    return abs((d2 - d1).days) // 7


def quarter_start_date(year: int, quarter: int) -> date:
    """Return the first day of a given quarter.

    Args:
        year: Calendar year.
        quarter: Quarter number (1-4).

    Returns:
        First day of the quarter.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If quarter not in 1-4.

    Example:
        >>> quarter_start_date(2025, 2)
        datetime.date(2025, 4, 1)

    Complexity: O(1)
    """
    if not isinstance(year, int) or not isinstance(quarter, int):
        raise TypeError("year and quarter must be integers.")

    if not 1 <= quarter <= 4:
        raise ValueError("quarter must be between 1 and 4.")

    month = 3 * (quarter - 1) + 1

    return date(year, month, 1)


def quarter_end_date(year: int, quarter: int) -> date:
    """Return the last day of a given quarter.

    Args:
        year: Calendar year.
        quarter: Quarter number (1-4).

    Returns:
        Last day of the quarter.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If quarter not in 1-4.

    Example:
        >>> quarter_end_date(2025, 1)
        datetime.date(2025, 3, 31)

    Complexity: O(1)
    """
    if not isinstance(year, int) or not isinstance(quarter, int):
        raise TypeError("year and quarter must be integers.")

    if not 1 <= quarter <= 4:
        raise ValueError("quarter must be between 1 and 4.")

    end_month = 3 * quarter
    _, last_day = calendar.monthrange(year, end_month)

    return date(year, end_month, last_day)


def is_first_day_of_month(d: Union[datetime, date]) -> bool:
    """Check if a date is the first day of its month.

    Args:
        d: Date or datetime to check.

    Returns:
        True if d is the 1st of its month.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_first_day_of_month(date(2025, 6, 1))
        True

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return dt.day == 1


def is_end_of_month(d: Union[datetime, date]) -> bool:
    """Check if a date is the last day of its month.

    Args:
        d: Date or datetime to check.

    Returns:
        True if d is the last day of its month.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_end_of_month(date(2025, 2, 28))
        True

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d
    _, last_day = calendar.monthrange(dt.year, dt.month)

    return dt.day == last_day


def next_month_same_day(d: Union[datetime, date]) -> date:
    """Return the same day number in the next month.

    If the day does not exist in the next month, the last day of
    the next month is returned.

    Args:
        d: Date or datetime.

    Returns:
        A date in the following month.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> next_month_same_day(date(2025, 1, 31))
        datetime.date(2025, 2, 28)

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    if dt.month == 12:
        next_year = dt.year + 1
        next_m = 1
    else:
        next_year = dt.year
        next_m = dt.month + 1

    _, last_day = calendar.monthrange(next_year, next_m)
    day = min(dt.day, last_day)

    return date(next_year, next_m, day)


def is_last_day_of_year(d: Union[datetime, date]) -> bool:
    """Check if a date is December 31st.

    Args:
        d: Date or datetime to check.

    Returns:
        True if d is December 31.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_last_day_of_year(date(2025, 12, 31))
        True

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return dt.month == 12 and dt.day == 31


def date_of_easter(year: int) -> date:
    """Calculate the date of Easter Sunday using the Anonymous Gregorian algorithm.

    Args:
        year: Gregorian calendar year (≥ 1583).

    Returns:
        Date of Easter Sunday.

    Raises:
        TypeError: If year is not an integer.
        ValueError: If year < 1583.

    Example:
        >>> date_of_easter(2025)
        datetime.date(2025, 4, 20)

    Complexity: O(1)
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer.")

    if year < 1583:
        raise ValueError("year must be at least 1583 (Gregorian calendar).")

    a = year % 19
    b, c = divmod(year, 100)
    d, e = divmod(b, 4)
    f = (b + 8) // 25
    g = (b - f + 1) // 3
    h = (19 * a + b - d - g + 15) % 30
    i, k = divmod(c, 4)
    el = (32 + 2 * e + 2 * i - h - k) % 7
    m = (a + 11 * h + 22 * el) // 451
    month, day = divmod(h + el - 7 * m + 114, 31)

    return date(year, month, day + 1)


def previous_month_same_day(d: Union[datetime, date]) -> date:
    """Return the same day number in the previous month.

    If the day does not exist in the previous month, the last day of
    the previous month is returned.

    Args:
        d: Date or datetime.

    Returns:
        A date in the preceding month.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> previous_month_same_day(date(2025, 3, 31))
        datetime.date(2025, 2, 28)

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    if dt.month == 1:
        prev_year = dt.year - 1
        prev_m = 12
    else:
        prev_year = dt.year
        prev_m = dt.month - 1

    _, last_day = calendar.monthrange(prev_year, prev_m)
    day = min(dt.day, last_day)

    return date(prev_year, prev_m, day)


def century_of_date(d: Union[datetime, date]) -> int:
    """Return the century number of a date.

    The 21st century covers years 2001-2100.

    Args:
        d: Date or datetime.

    Returns:
        Century number (e.g. 21 for year 2025).

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> century_of_date(date(2025, 6, 15))
        21

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return (dt.year - 1) // 100 + 1


def millennium_of_date(d: Union[datetime, date]) -> int:
    """Return the millennium number of a date.

    The 3rd millennium covers years 2001-3000.

    Args:
        d: Date or datetime.

    Returns:
        Millennium number (e.g. 3 for year 2025).

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> millennium_of_date(date(2025, 1, 1))
        3

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return (dt.year - 1) // 1000 + 1


def day_name_of_date(d: Union[datetime, date]) -> str:
    """Return the English weekday name for a date.

    Args:
        d: Date or datetime.

    Returns:
        Weekday name (e.g. "Monday").

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> day_name_of_date(date(2025, 4, 20))
        'Sunday'

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d
    names = ("Monday", "Tuesday", "Wednesday", "Thursday",
             "Friday", "Saturday", "Sunday")

    return names[dt.weekday()]


def days_until_end_of_year(d: Union[datetime, date]) -> int:
    """Return the number of days remaining until the end of the year.

    Args:
        d: Date or datetime.

    Returns:
        Number of remaining days (31 Dec → 0).

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> days_until_end_of_year(date(2025, 12, 1))
        30

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return (date(dt.year, 12, 31) - dt).days


def date_of_nth_weekday(
    year: int,
    month: int,
    weekday: int,
    n: int,
) -> datetime:
    """Return the date of the *n*-th occurrence of a weekday in a month.

    Args:
        year: Calendar year.
        month: Month (1–12).
        weekday: Day of the week (0 = Monday … 6 = Sunday).
        n: Occurrence number (1 = first, 2 = second, …).

    Returns:
        A datetime for the requested date.

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If parameters are out of range or the *n*-th
            occurrence does not exist in the month.

    Example:
        >>> date_of_nth_weekday(2025, 11, 3, 4)
        datetime.datetime(2025, 11, 27, 0, 0)

    Complexity: O(1)
    """
    if not isinstance(year, int):
        raise TypeError("year must be an integer.")

    if not isinstance(month, int):
        raise TypeError("month must be an integer.")

    if not isinstance(weekday, int):
        raise TypeError("weekday must be an integer.")

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not 1 <= month <= 12:
        raise ValueError("month must be between 1 and 12.")

    if not 0 <= weekday <= 6:
        raise ValueError("weekday must be between 0 (Monday) and 6 (Sunday).")

    if n < 1:
        raise ValueError("n must be at least 1.")

    first_day = datetime(year, month, 1)
    first_weekday = first_day.weekday()

    days_ahead = (weekday - first_weekday) % 7
    first_occurrence = 1 + days_ahead
    target_day = first_occurrence + (n - 1) * 7

    _, days_in_month = calendar.monthrange(year, month)

    if target_day > days_in_month:
        raise ValueError(
            f"The {n}-th occurrence of weekday {weekday} "
            f"does not exist in {year}-{month:02d}."
        )

    return datetime(year, month, target_day)


def semester_of_date(d: Union[datetime, date]) -> int:
    """Return the semester of the year for a given date.

    Semester 1 covers January–June, semester 2 covers July–December.

    Args:
        d: Date or datetime.

    Returns:
        1 or 2.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> semester_of_date(date(2025, 3, 15))
        1

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return 1 if dt.month <= 6 else 2


def fortnight_of_year(d: Union[datetime, date]) -> int:
    """Return the fortnight number of the year (1-based).

    Each fortnight spans 14 days.  Day 1–14 → fortnight 1,
    day 15–28 → fortnight 2, and so on (up to 27).

    Args:
        d: Date or datetime.

    Returns:
        Fortnight number (1–27).

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> fortnight_of_year(date(2025, 1, 15))
        2

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d
    day_of_year = (dt - date(dt.year, 1, 1)).days + 1

    return (day_of_year - 1) // 14 + 1


def bimester_of_date(d: Union[datetime, date]) -> int:
    """Return the bimester number for a date.

    A bimester is a two-month period.  Jan–Feb → 1, Mar–Apr → 2, …,
    Nov–Dec → 6.

    Args:
        d: Date or datetime.

    Returns:
        Bimester number (1–6).

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> bimester_of_date(date(2025, 5, 10))
        3

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return (dt.month - 1) // 2 + 1


def trimester_of_date(d: Union[datetime, date]) -> int:
    """Return the trimester number for a date.

    A trimester is a four-month period.  Jan–Apr → 1,
    May–Aug → 2, Sep–Dec → 3.

    Args:
        d: Date or datetime.

    Returns:
        Trimester number (1–3).

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> trimester_of_date(date(2025, 9, 1))
        3

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d

    return (dt.month - 1) // 4 + 1


def elapsed_years(
    start: Union[datetime, date],
    end: Union[datetime, date],
) -> int:
    """Return the number of full years between two dates.

    A "full year" means the anniversary date has been reached.

    Args:
        start: Start date.
        end: End date (must be ≥ start).

    Returns:
        Number of complete years as an integer.

    Raises:
        TypeError: If start or end is not a date or datetime.
        ValueError: If end is before start.

    Example:
        >>> from datetime import date
        >>> elapsed_years(date(2000, 6, 15), date(2025, 4, 8))
        24

    Complexity: O(1)
    """
    if not isinstance(start, (datetime, date)):
        raise TypeError("start must be a date or datetime.")

    if not isinstance(end, (datetime, date)):
        raise TypeError("end must be a date or datetime.")

    d1 = start.date() if isinstance(start, datetime) else start
    d2 = end.date() if isinstance(end, datetime) else end

    if d2 < d1:
        raise ValueError("end must not be before start.")

    years = d2.year - d1.year

    if (d2.month, d2.day) < (d1.month, d1.day):
        years -= 1

    return years


def ordinal_date_string(d: Union[datetime, date]) -> str:
    """Return the ISO ordinal date string for a date.

    Format: "YYYY-DDD" where DDD is the day-of-year (001–366).

    Args:
        d: Date or datetime.

    Returns:
        Ordinal date string (e.g. "2025-001").

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> ordinal_date_string(date(2025, 3, 1))
        '2025-060'

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d
    doy = dt.timetuple().tm_yday

    return f"{dt.year:04d}-{doy:03d}"


def date_to_julian_day(d: Union[datetime, date]) -> int:
    """Return the Julian Day Number for a date.

    Uses the algorithm for the proleptic Gregorian calendar.

    Args:
        d: Date or datetime.

    Returns:
        Julian Day Number as an integer.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> date_to_julian_day(date(2000, 1, 1))
        2451545

    Complexity: O(1)
    """
    if not isinstance(d, (datetime, date)):
        raise TypeError("d must be a date or datetime.")

    dt = d.date() if isinstance(d, datetime) else d
    y = dt.year
    m = dt.month
    day = dt.day

    a = (14 - m) // 12
    y2 = y + 4800 - a
    m2 = m + 12 * a - 3

    return (
        day
        + (153 * m2 + 2) // 5
        + 365 * y2
        + y2 // 4
        - y2 // 100
        + y2 // 400
        - 32045
    )


def is_dst_transition_day(
    d: Union[date, datetime], tz_name: str
) -> bool:
    """Returns True if the given date has a DST (Daylight Saving Time) transition.

    Checks whether the UTC offset changes between the start and end of
    the day in the specified timezone.

    Args:
        d: The date to check.
        tz_name: IANA timezone name (e.g. ``"Europe/Madrid"``).

    Returns:
        True if a DST transition occurs on that day.

    Raises:
        TypeError: If d is not a date/datetime or tz_name is not a string.
        ValueError: If tz_name is not a valid timezone.

    Example:
        >>> from datetime import date
        >>> is_dst_transition_day(date(2026, 3, 29), "Europe/Madrid")
        True
        >>> is_dst_transition_day(date(2026, 6, 15), "Europe/Madrid")
        False

    Complexity: O(1)
    """
    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    if not isinstance(tz_name, str):
        raise TypeError("tz_name must be a string")

    try:
        tz = zoneinfo.ZoneInfo(tz_name)
    except (KeyError, zoneinfo.ZoneInfoNotFoundError) as exc:
        raise ValueError(f"Invalid timezone: {tz_name}") from exc

    dt_date = d.date() if isinstance(d, datetime) else d
    start_of_day = datetime(dt_date.year, dt_date.month, dt_date.day, 0, 0, 0, tzinfo=tz)
    end_of_day = datetime(dt_date.year, dt_date.month, dt_date.day, 23, 59, 59, tzinfo=tz)
    return start_of_day.utcoffset() != end_of_day.utcoffset()


def moon_phase(d: Union[date, datetime]) -> tuple:
    """Returns the approximate lunar phase for a given date.

    Uses the Trig2 approximation based on the date's offset from a
    known new-moon reference (January 6, 2000).

    Args:
        d: The date to evaluate.

    Returns:
        Tuple of (phase_ratio, phase_name) where phase_ratio is
        0.0–1.0 (0 ≈ new moon, 0.5 ≈ full moon) and phase_name
        is one of ``"New Moon"``, ``"Waxing Crescent"``,
        ``"First Quarter"``, ``"Waxing Gibbous"``, ``"Full Moon"``,
        ``"Waning Gibbous"``, ``"Last Quarter"``, ``"Waning Crescent"``.

    Raises:
        TypeError: If d is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> phase, name = moon_phase(date(2026, 4, 8))
        >>> 0.0 <= phase <= 1.0
        True

    Complexity: O(1)
    """
    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    dt_date = d.date() if isinstance(d, datetime) else d
    # Reference new moon: January 6, 2000
    ref = date(2000, 1, 6)
    days_since = (dt_date - ref).days
    synodic_month = 29.53058770576
    phase_ratio = (days_since % synodic_month) / synodic_month

    names = [
        "New Moon",
        "Waxing Crescent",
        "First Quarter",
        "Waxing Gibbous",
        "Full Moon",
        "Waning Gibbous",
        "Last Quarter",
        "Waning Crescent",
    ]
    index = int(phase_ratio * 8) % 8
    return (round(phase_ratio, 4), names[index])


# Country holiday sets (simplified — major public holidays)
_HOLIDAYS: dict[str, dict[int, list[tuple[int, int]]]] = {
    "ES": {0: [(1, 1), (1, 6), (5, 1), (8, 15), (10, 12), (11, 1), (12, 6), (12, 8), (12, 25)]},
    "US": {0: [(1, 1), (7, 4), (11, 11), (12, 25)]},
    "GB": {0: [(1, 1), (12, 25), (12, 26)]},
    "FR": {0: [(1, 1), (5, 1), (5, 8), (7, 14), (8, 15), (11, 1), (11, 11), (12, 25)]},
    "DE": {0: [(1, 1), (5, 1), (10, 3), (12, 25), (12, 26)]},
}


def is_holiday(d: date | datetime, country: str = "ES") -> bool:
    """Check if a date is a public holiday in the given country.

    Supports simplified holiday sets for ES, US, GB, FR, DE.

    Args:
        d: Date to check.
        country: ISO 3166-1 alpha-2 country code.

    Returns:
        ``True`` if the date is a public holiday.

    Raises:
        TypeError: If *d* is not a date/datetime.
        ValueError: If *country* is not supported.

    Example:
        >>> from datetime import date
        >>> is_holiday(date(2026, 12, 25), "ES")
        True
        >>> is_holiday(date(2026, 4, 8), "ES")
        False

    Complexity: O(H), H = holidays in the country.
    """
    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    country = country.upper()

    if country not in _HOLIDAYS:
        raise ValueError(f"Unsupported country: {country!r}. Supported: {list(_HOLIDAYS.keys())}")

    dt_date = d.date() if isinstance(d, datetime) else d
    year_holidays = _HOLIDAYS[country].get(0, [])

    return (dt_date.month, dt_date.day) in year_holidays


def astronomical_season(d: date | datetime, hemisphere: str = "north") -> str:
    """Determine the astronomical season based on equinox/solstice dates.

    Uses approximate fixed dates for equinoxes and solstices.

    Args:
        d: Date to evaluate.
        hemisphere: ``"north"`` or ``"south"``.

    Returns:
        Season name: ``"spring"``, ``"summer"``, ``"autumn"``, ``"winter"``.

    Raises:
        TypeError: If *d* is not a date/datetime.
        ValueError: If *hemisphere* is invalid.

    Example:
        >>> from datetime import date
        >>> astronomical_season(date(2026, 7, 15))
        'summer'
        >>> astronomical_season(date(2026, 7, 15), "south")
        'winter'

    Complexity: O(1)
    """
    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    hemisphere = hemisphere.lower()

    if hemisphere not in ("north", "south"):
        raise ValueError("hemisphere must be 'north' or 'south'")

    dt_date = d.date() if isinstance(d, datetime) else d
    year = dt_date.year

    # Approximate equinox/solstice dates
    spring_equinox = date(year, 3, 20)
    summer_solstice = date(year, 6, 21)
    autumn_equinox = date(year, 9, 22)
    winter_solstice = date(year, 12, 21)

    if dt_date < spring_equinox:
        north_season = "winter"
    elif dt_date < summer_solstice:
        north_season = "spring"
    elif dt_date < autumn_equinox:
        north_season = "summer"
    elif dt_date < winter_solstice:
        north_season = "autumn"
    else:
        north_season = "winter"

    if hemisphere == "north":
        return north_season

    flip = {"spring": "autumn", "summer": "winter", "autumn": "spring", "winter": "summer"}
    return flip[north_season]


def is_golden_hour(
    d: datetime,
    latitude: float,
    longitude: float,
) -> bool:
    """Approximate whether a datetime falls within the golden hour.

    Golden hour is roughly the first/last hour of sunlight. Uses a
    simplified sunrise/sunset calculation.

    Args:
        d: Datetime to check (should include time component).
        latitude: Latitude in decimal degrees.
        longitude: Longitude in decimal degrees.

    Returns:
        ``True`` if the time is within ~1 hour of sunrise or sunset.

    Raises:
        TypeError: If *d* is not a datetime.
        ValueError: If latitude/longitude out of range.

    Example:
        >>> from datetime import datetime
        >>> is_golden_hour(datetime(2026, 6, 21, 6, 30), 40.0, -3.7)
        True

    Complexity: O(1)
    """
    if not isinstance(d, datetime):
        raise TypeError("d must be a datetime")

    if not isinstance(latitude, (int, float)) or not isinstance(longitude, (int, float)):
        raise TypeError("latitude and longitude must be numeric")

    if latitude < -90 or latitude > 90:
        raise ValueError("latitude must be between -90 and 90")

    if longitude < -180 or longitude > 180:
        raise ValueError("longitude must be between -180 and 180")

    day_of_year = d.timetuple().tm_yday
    # Solar declination
    decl = 23.45 * math.sin(math.radians((360 / 365) * (day_of_year - 81)))
    lat_rad = math.radians(latitude)
    decl_rad = math.radians(decl)

    cos_ha = -math.tan(lat_rad) * math.tan(decl_rad)
    cos_ha = max(-1.0, min(1.0, cos_ha))
    ha = math.degrees(math.acos(cos_ha))

    solar_noon = 12.0 - longitude / 15.0
    sunrise_h = solar_noon - ha / 15.0
    sunset_h = solar_noon + ha / 15.0

    current_h = d.hour + d.minute / 60.0

    # Within 1 hour of sunrise or sunset
    return (
        (sunrise_h <= current_h <= sunrise_h + 1.0)
        or (sunset_h - 1.0 <= current_h <= sunset_h)
    )


def is_friday_13th(d: date | datetime) -> bool:
    """Check whether a date falls on Friday the 13th.

    Args:
        d: Date to check.

    Returns:
        ``True`` if *d* is a Friday and the day of the month is 13.

    Raises:
        TypeError: If *d* is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_friday_13th(date(2026, 2, 13))
        True

    Complexity: O(1)
    """
    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    target = d.date() if isinstance(d, datetime) else d

    return target.day == 13 and target.weekday() == 4


def is_equinox_or_solstice(d: date | datetime) -> str | None:
    """Return the astronomical event name if *d* falls on one, else ``None``.

    Uses approximate fixed dates for the Northern Hemisphere:
    - March 20: vernal equinox
    - June 21: summer solstice
    - September 22: autumnal equinox
    - December 21: winter solstice

    Args:
        d: Date to check.

    Returns:
        Name of the event or ``None``.

    Raises:
        TypeError: If *d* is not a date or datetime.

    Example:
        >>> from datetime import date
        >>> is_equinox_or_solstice(date(2026, 6, 21))
        'summer_solstice'

    Complexity: O(1)
    """
    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    target = d.date() if isinstance(d, datetime) else d
    key = (target.month, target.day)

    events: dict[tuple[int, int], str] = {
        (3, 20): "vernal_equinox",
        (6, 21): "summer_solstice",
        (9, 22): "autumnal_equinox",
        (12, 21): "winter_solstice",
    }

    return events.get(key)


def is_blue_moon(year: int, month: int) -> bool:
    """Check whether a given month contains a blue moon.

    A blue moon is the second full moon in a calendar month.  This
    function uses a simplified mean-synodic-month calculation (29.53
    days) anchored to a known full moon (2000-01-06 18:14 UTC).

    Args:
        year: Calendar year.
        month: Calendar month (1-12).

    Returns:
        ``True`` if the month contains two full moons.

    Raises:
        TypeError: If arguments are not integers.
        ValueError: If *month* is outside [1, 12].

    Example:
        >>> is_blue_moon(2026, 5)
        True

    Complexity: O(1)
    """
    if not isinstance(year, int) or not isinstance(month, int):
        raise TypeError("year and month must be integers")

    if month < 1 or month > 12:
        raise ValueError("month must be between 1 and 12")

    # Known full moon: 2000-01-06 18:14 UTC
    known_full = datetime(2000, 1, 6, 18, 14)
    synodic = 29.53058867

    month_start = datetime(year, month, 1)
    days_in_month = calendar.monthrange(year, month)[1]
    month_end = datetime(year, month, days_in_month, 23, 59, 59)

    diff_start = (month_start - known_full).total_seconds() / 86400.0
    diff_end = (month_end - known_full).total_seconds() / 86400.0

    # Number of full moons elapsed before month_start / month_end
    n_start = math.ceil(diff_start / synodic)
    n_end = math.floor(diff_end / synodic)

    return (n_end - n_start + 1) >= 2


def is_iso_long_year(year: int) -> bool:
    """Check if an ISO year has 53 weeks.

    Description:
        An ISO year has 53 weeks when December 31 of the Gregorian
        year or January 1 of the next year falls in ISO week 53.
        Equivalent to checking that the Gregorian year starts on
        Thursday, or is a leap year starting on Wednesday.

    Args:
        year: The ISO year to check.

    Returns:
        True if the ISO year has 53 weeks (a "long" ISO year).

    Raises:
        TypeError: If *year* is not an integer.

    Usage Example:
        >>> is_iso_long_year(2020)
        True
        >>> is_iso_long_year(2023)
        False

    Complexity: O(1)
    """
    if not isinstance(year, int) or isinstance(year, bool):
        raise TypeError("year must be an integer")

    # Dec 31 of this year — if it's in week 53, it's a long year
    dec31 = date(year, 12, 31)

    return dec31.isocalendar()[1] == 53


def week_year(d: Union[date, datetime]) -> int:
    """Return the ISO week-numbering year for a date.

    Description:
        The ISO week-numbering year can differ from the Gregorian
        calendar year for dates near the year boundary.  For example,
        2025-12-29 (Monday) belongs to ISO year 2026 week 1.

    Args:
        d: A ``date`` or ``datetime`` instance.

    Returns:
        The ISO week-numbering year.

    Raises:
        TypeError: If *d* is not a date or datetime.

    Usage Example:
        >>> from datetime import date
        >>> week_year(date(2025, 12, 29))
        2026
        >>> week_year(date(2025, 6, 15))
        2025

    Complexity: O(1)
    """
    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    target = d.date() if isinstance(d, datetime) else d

    return target.isocalendar()[0]


def sidereal_time(d: Union[date, datetime], longitude: float = 0.0) -> float:
    """Approximate local sidereal time in hours.

    Description:
        Computes Greenwich Mean Sidereal Time (GMST) at 0h UT for the
        given date using the IAU simplified formula, then adds the
        observer's longitude converted to hours.

        GMST = 6.697374558 + 0.06570982441908 × D₀
        where D₀ is the number of days from J2000.0 (2000-01-01 12:00 UT).

    Args:
        d: A date or datetime for which to compute sidereal time.
        longitude: Observer longitude in degrees (−180 to +180).
            Positive = East. Default 0.0 (Greenwich).

    Returns:
        Local sidereal time in hours [0, 24).

    Raises:
        TypeError: If *d* is not a date/datetime or *longitude* is not numeric.
        ValueError: If *longitude* is outside [−180, 180].

    Usage Example:
        >>> from datetime import date
        >>> round(sidereal_time(date(2000, 1, 1), 0.0), 4)
        6.6645

    Complexity: O(1)
    """
    if not isinstance(d, (date, datetime)):
        raise TypeError("d must be a date or datetime")

    if not isinstance(longitude, (int, float)):
        raise TypeError("longitude must be numeric.")

    if longitude < -180 or longitude > 180:
        raise ValueError("longitude must be in [-180, 180].")

    # Convert to datetime at 0h UT
    if isinstance(d, datetime):
        dt_ut = datetime(d.year, d.month, d.day)
    else:
        dt_ut = datetime(d.year, d.month, d.day)

    # Days from J2000.0 (2000-01-01 12:00 UT)
    j2000 = datetime(2000, 1, 1, 12, 0, 0)
    d0 = (dt_ut - j2000).total_seconds() / 86400.0

    # GMST at 0h UT
    gmst = 6.697374558 + 0.06570982441908 * d0

    # Add observer longitude (degrees → hours)
    lst = gmst + longitude / 15.0

    # Normalise to [0, 24)
    lst = lst % 24.0

    return float(lst)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 36: Date Evaluations
# ---------------------------------------------------------------------------

def is_date_in_range(d, start, end) -> bool:
    """Check if a date falls within [start, end] inclusive.

    Args:
        d: Date to check.
        start: Range start (date or datetime).
        end: Range end (date or datetime).

    Returns:
        True if d is in [start, end].

    Raises:
        TypeError: If arguments are not date/datetime.

    Example:
        >>> from datetime import date
        >>> is_date_in_range(date(2024, 6, 15), date(2024, 1, 1), date(2024, 12, 31))
        True

    Complexity: O(1)
    """
    for name, val in [("d", d), ("start", start), ("end", end)]:
        if not isinstance(val, (date, datetime)):
            raise TypeError(f"{name} must be a date or datetime.")
    if isinstance(d, datetime):
        d = d.date()
    if isinstance(start, datetime):
        start = start.date()
    if isinstance(end, datetime):
        end = end.date()
    return start <= d <= end


def days_until_weekday(d, target_weekday: int) -> int:
    """Return the number of days from *d* until the next occurrence of *target_weekday*.

    Args:
        d: Starting date (date or datetime).
        target_weekday: ISO weekday (1=Monday … 7=Sunday).

    Returns:
        Days until next occurrence (0 if d is already that weekday).

    Raises:
        TypeError: If d is not a date/datetime.
        ValueError: If target_weekday is not 1–7.

    Example:
        >>> from datetime import date
        >>> days_until_weekday(date(2024, 1, 1), 5)
        4

    Complexity: O(1)
    """
    if isinstance(d, datetime):
        d = d.date()
    if not isinstance(d, date):
        raise TypeError("d must be a date or datetime.")
    if not isinstance(target_weekday, int) or not 1 <= target_weekday <= 7:
        raise ValueError("target_weekday must be 1–7 (ISO: 1=Mon, 7=Sun).")
    current = d.isoweekday()
    diff = (target_weekday - current) % 7
    return diff


def is_nth_weekday(d, n: int, weekday: int) -> bool:
    """Check if *d* is the n-th occurrence of a weekday in its month.

    Args:
        d: Date to check (date or datetime).
        n: Which occurrence (1 = first, 2 = second, etc.).
        weekday: ISO weekday (1=Monday … 7=Sunday).

    Returns:
        True if d is the n-th weekday in its month.

    Raises:
        TypeError: If d is not a date/datetime.
        ValueError: If n < 1 or weekday not 1–7.

    Example:
        >>> from datetime import date
        >>> is_nth_weekday(date(2024, 1, 8), 2, 1)
        True

    Complexity: O(1)
    """
    if isinstance(d, datetime):
        d = d.date()
    if not isinstance(d, date):
        raise TypeError("d must be a date or datetime.")
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer.")
    if not isinstance(weekday, int) or not 1 <= weekday <= 7:
        raise ValueError("weekday must be 1–7 (ISO: 1=Mon, 7=Sun).")
    if d.isoweekday() != weekday:
        return False
    return (d.day - 1) // 7 + 1 == n


def date_grade(d) -> str:
    """Classify a date into a period label: 'ancient', 'medieval', 'modern', or 'contemporary'.

    Uses simplified thresholds:
    - ancient: before 476 AD
    - medieval: 476–1453
    - modern: 1453–1945
    - contemporary: 1945+

    Args:
        d: Date to classify (date or datetime).

    Returns:
        Period label string.

    Raises:
        TypeError: If d is not a date/datetime.

    Example:
        >>> from datetime import date
        >>> date_grade(date(2024, 1, 1))
        'contemporary'

    Complexity: O(1)
    """
    if isinstance(d, datetime):
        d = d.date()
    if not isinstance(d, date):
        raise TypeError("d must be a date or datetime.")
    year = d.year
    if year < 476:
        return "ancient"
    if year < 1453:
        return "medieval"
    if year < 1945:
        return "modern"
    return "contemporary"

