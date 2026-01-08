"""System date and time operations module.

This module provides functions to retrieve current system date and time information,
including current datetime, date, time, year, month, day, weekday, and timezone-aware
operations. All 'current_*' functions return information based on the system's local time.
"""

from datetime import datetime, timedelta
from typing import Union, Optional
import calendar
import zoneinfo

#import date_operations as date_ops
from . import date_operations as date_ops

def current_datetime() -> datetime:
    """Gets the current local date and time.
    
    Description:
        Returns the current date and time according to the system's local timezone.
        The returned datetime object is timezone-naive.
    
    Returns:
        datetime: A datetime object representing the current local date and time.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_datetime
        >>> now = current_datetime()
        >>> print(now.strftime('%Y-%m-%d %H:%M:%S'))  # Output varies
        2026-01-03 14:30:45
    
    Cost: O(1)
    """
    # The datetime.now() method returns the current local date and time.
    return datetime.now()


def current_date() -> datetime:
    """Gets the current local date (without the time component).
    
    Description:
        Returns a datetime object representing only the current date with time
        components (hour, minute, second, microsecond) set to zero.
    
    Returns:
        datetime: A datetime object representing the current local date at midnight.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_date
        >>> today = current_date()
        >>> print(today.strftime('%Y-%m-%d'))  # Output varies
        2026-01-03
        >>> print(today.strftime('%Y-%m-%d %H:%M:%S'))
        2026-01-03 00:00:00
    
    Cost: O(1)
    """
    # We get the current datetime and then extract only the date part using .date().
    # To return a datetime object, we reconstruct it with time components set to zero.
    return datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)


def current_time() -> datetime:
    """Gets the current local time (without the date component).
    
    Description:
        Returns a datetime object with the current time but using a minimal
        date (datetime.min.date()). Useful for time-only comparisons.
    
    Returns:
        datetime: A datetime object with current time and minimal date (0001-01-01).
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_time
        >>> time_now = current_time()
        >>> print(time_now.strftime('%H:%M:%S'))  # Output varies
        14:30:45
        >>> print(time_now.strftime('%Y-%m-%d %H:%M:%S'))
        0001-01-01 14:30:45
    
    Cost: O(1)
    """
    # We get the current datetime and then extract only the time part using .time().
    # To return a datetime object with only time information, we use a default date.
    return datetime.combine(datetime.min.date(), datetime.now().time())


def current_year() -> int:
    """Gets the current year.
    
    Description:
        Returns the year component from the current system date.
    
    Returns:
        int: The current year as a four-digit integer.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_year
        >>> year = current_year()
        >>> print(year)  # Output varies
        2026
    
    Cost: O(1)
    """
    # Extract the year attribute from the current datetime.
    return datetime.now().year


def current_month() -> int:
    """Gets the current month (1-12).
    
    Description:
        Returns the month component from the current system date as a number
        from 1 (January) to 12 (December).
    
    Returns:
        int: The current month as an integer (1 for January, 12 for December).
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_month
        >>> month = current_month()
        >>> print(month)  # Output varies
        1
    
    Cost: O(1)
    """
    # Extract the month attribute from the current datetime.
    return datetime.now().month


def current_day() -> int:
    """Gets the current day of the month (1-31).
    
    Description:
        Returns the day component from the current system date as a number
        from 1 to 31 (depending on the month).
    
    Returns:
        int: The current day of the month as an integer.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_day
        >>> day = current_day()
        >>> print(day)  # Output varies
        3
    
    Cost: O(1)
    """
    # Extract the day attribute from the current datetime.
    return datetime.now().day


def current_weekday_number(start_day: str = 'european') -> int:
    """Retrieves the current day of the week as a number.
    
    Description:
        Returns the current weekday as an integer, supporting both European
        (Monday=0) and US (Sunday=0) conventions. Uses datetime.weekday()
        as the base and adjusts for US convention when requested.
    
    Args:
        start_day (str): Week start convention. Accepted values:
                        'european' (Monday=0, ..., Sunday=6) or
                        'us' (Sunday=0, Monday=1, ..., Saturday=6).
                        Defaults to 'european'.
    
    Returns:
        int: The current day of the week as an integer (0-6).
    
    Raises:
        ValueError: If 'start_day' is not 'european' or 'us'.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_weekday_number
        >>> current_weekday_number(start_day='european')  # For Friday
        4
        >>> current_weekday_number(start_day='us')  # For Friday
        5
    
    Cost: O(1)
    """
    if start_day not in ['european', 'us']:
        raise ValueError("Invalid value for 'start_day'. Must be 'european' or 'us'.")

    # Get the current weekday using the default datetime.weekday() method,
    # which returns Monday=0, ..., Sunday=6 (European standard).
    current_weekday_index = datetime.now().weekday()

    # If the US convention is requested, adjust the index.
    # The US convention starts with Sunday as 0. Since Python's weekday()
    # returns Sunday as 6, we shift it to 0 by adding 1 and taking modulo 7.
    if start_day == 'us':
        return (current_weekday_index + 1) % 7
    return current_weekday_index


def current_weekday_name(language: str = 'en') -> str:
    """Gets the current weekday name for the current date.
    
    Description:
        Returns the name of the current weekday in the specified language.
        Delegates to date_operations.weekday_name() for name resolution.
    
    Args:
        language (str, optional): Language code for the weekday name.
                                 Supports 'en' (English) and 'es' (Spanish).
                                 Defaults to 'en'.
    
    Returns:
        str: The name of the current day of the week.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_weekday_name
        >>> current_weekday_name('en')  # For Friday
        'Friday'
        >>> current_weekday_name('es')  # For Friday
        'Viernes'
    
    Cost: O(1)
    """
    return date_ops.weekday_name(datetime.now(), language)


def current_last_day_of_month() -> datetime:
    """Gets the last day of the current month.
    
    Description:
        Returns a datetime object representing the last calendar day of the
        current month at midnight. Delegates to date_operations.last_day_of_month().
    
    Returns:
        datetime: A datetime object for the last day of the current month.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_last_day_of_month
        >>> last_day = current_last_day_of_month()  # If current month is January 2026
        >>> print(last_day.strftime('%Y-%m-%d'))
        2026-01-31
    
    Cost: O(1)
    """
    return date_ops.last_day_of_month(datetime.now())


def current_last_friday_of_month() -> datetime:
    """Gets the last Friday of the current month.
    
    Description:
        Returns a datetime object representing the last Friday occurring in
        the current month. Delegates to date_operations.last_weekday_of_month().
    
    Returns:
        datetime: A datetime object for the last Friday of the current month.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_last_friday_of_month
        >>> last_fri = current_last_friday_of_month()  # For January 2026
        >>> print(last_fri.strftime('%Y-%m-%d %A'))
        2026-01-30 Friday
    
    Cost: O(1)
    """
    return date_ops.last_weekday_of_month(datetime.now(), calendar.FRIDAY)


def current_next_friday() -> datetime:
    """Gets the next Friday after the current date.
    
    Description:
        Returns a datetime object representing the next Friday that occurs
        after today. If today is Friday, returns next week's Friday.
        Delegates to date_operations.next_weekday().
    
    Returns:
        datetime: A datetime object for the next Friday after today.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_next_friday
        >>> next_fri = current_next_friday()  # If today is Friday 2026-01-03
        >>> print(next_fri.strftime('%Y-%m-%d %A'))
        2026-01-10 Friday
    
    Cost: O(1)
    """
    return date_ops.next_weekday(datetime.now(), calendar.FRIDAY)


def current_previous_friday() -> datetime:
    """Gets the previous Friday before the current date.
    
    Description:
        Returns a datetime object representing the most recent Friday that
        occurred before today. If today is Friday, returns last week's Friday.
        Delegates to date_operations.previous_weekday().
    
    Returns:
        datetime: A datetime object for the previous Friday before today.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_previous_friday
        >>> prev_fri = current_previous_friday()  # If today is Friday 2026-01-03
        >>> print(prev_fri.strftime('%Y-%m-%d %A'))
        2025-12-27 Friday
    
    Cost: O(1)
    """
    return date_ops.previous_weekday(datetime.now(), calendar.FRIDAY)


def current_is_working_day() -> bool:
    """Checks if the current date is a working day (Monday to Friday).
    
    Description:
        Returns True if today is a weekday (Monday through Friday), False
        if it's a weekend (Saturday or Sunday). Does not consider holidays.
        Delegates to date_operations.is_working_day().
    
    Returns:
        bool: True if current date is Monday-Friday, False otherwise.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_is_working_day
        >>> current_is_working_day()  # For Friday 2026-01-03
        True
        >>> # For Saturday 2026-01-04
        False
    
    Cost: O(1)
    """
    return date_ops.is_working_day(datetime.now())


def current_is_weekend() -> bool:
    """Checks if the current date is a weekend (Saturday or Sunday).
    
    Description:
        Returns True if today is Saturday or Sunday, False if it's a weekday.
        Delegates to date_operations.is_weekend().
    
    Returns:
        bool: True if current date is Saturday or Sunday, False otherwise.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import current_is_weekend
        >>> current_is_weekend()  # For Friday 2026-01-03
        False
        >>> # For Saturday 2026-01-04
        True
    
    Cost: O(1)
    """
    return date_ops.is_weekend(datetime.now())


def get_local_now(tz: Optional[str] = None) -> datetime:
    """Gets the current date and time in a specified timezone.
    
    Description:
        Returns a timezone-aware datetime object representing the current time
        in the specified timezone. If no timezone is specified, returns the
        current time in the system's local timezone. Timezone names must follow
        the IANA timezone database format (e.g., 'America/New_York', 'Europe/Madrid').
    
    Args:
        tz (Optional[str]): IANA timezone name (e.g., 'America/New_York').
                           If None, uses the system's local timezone.
    
    Returns:
        datetime: A timezone-aware datetime object in the specified timezone.
    
    Raises:
        TypeError: If 'tz' is not a string when provided.
        ValueError: If 'tz' is not a valid IANA timezone name.
    
    Usage Example:
        >>> from formulite.fxDate.date_sys import get_local_now
        >>> tokyo_now = get_local_now('Asia/Tokyo')
        >>> print(tokyo_now.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
        2026-01-03 23:30:45 JST+0900
        >>> 
        >>> local_now = get_local_now()
        >>> print(local_now.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
        2026-01-03 15:30:45 CET+0100
        >>> 
        >>> ny_now = get_local_now('America/New_York')
        >>> print(ny_now.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
        2026-01-03 09:30:45 EST-0500
    
    Cost: O(1)
    """
    if tz is None:
        # Si no se especifica una zona horaria, se devuelve la hora actual
        # localizada en la zona horaria del sistema.
        return datetime.now().astimezone()
    else:
        # Si se especifica una zona horaria, se valida y se usa.
        if not isinstance(tz, str):
            raise TypeError("Input 'tz' must be a string representing a timezone.")
        try:
            # Cargar la información de la zona horaria IANA.
            target_tz_info = zoneinfo.ZoneInfo(tz)
            
            # Obtener la hora UTC actual. Es el punto de partida más seguro para conversiones.
            # Se usa zoneinfo.ZoneInfo('UTC') para consistencia.
            utc_now = datetime.now(zoneinfo.ZoneInfo('UTC'))
            
            # Convertir la hora UTC a la zona horaria objetivo.
            return utc_now.astimezone(target_tz_info)
        except zoneinfo.ZoneInfoNotFoundError:
            # Capturar errores si el nombre de la zona horaria no es válido.
            raise ValueError(f"Invalid or unknown timezone: '{tz}'.")
        except Exception as e:
            # Capturar cualquier otro error inesperado.
            raise RuntimeError(f"An unexpected error occurred while getting local time for timezone '{tz}': {e}")