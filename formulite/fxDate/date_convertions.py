"""Date and time conversion module.

This module provides comprehensive functions for converting between different date/time
formats including: datetime objects, strings, timestamps, ISO formats, timezones, Julian
dates, Windows FILETIME, and Active Directory formats. All functions handle timezone-aware
and timezone-naive datetime objects appropriately.
"""

from datetime import date, datetime, timezone, timedelta
from typing import Union, Optional, Tuple, List
import zoneinfo

    
def datetime_to_date(datetime_obj: datetime) -> date:
    """Converts a datetime object to a date object, discarding time components.
    
    Description:
        Extracts only the date portion (year, month, day) from a datetime object,
        removing all time information (hour, minute, second, microsecond).
        Useful for date-only comparisons and storage.
    
    Args:
        datetime_obj (datetime): The datetime object to convert.
    
    Returns:
        date: A new date object representing the date part of the input datetime.
    
    Raises:
        TypeError: If 'datetime_obj' is not a datetime object.
    
    Usage Example:
        >>> from datetime import datetime, date
        >>> from formulite.fxDate.date_convertions import datetime_to_date
        >>> dt_with_time = datetime(2026, 1, 3, 14, 30, 45)
        >>> date_only = datetime_to_date(dt_with_time)
        >>> print(date_only)
        2026-01-03
        >>> print(type(date_only))
        <class 'datetime.date'>
    
    Cost: O(1)
    """
    # Validate that the input is indeed a datetime object.
    # This ensures the '.date()' method can be safely called and
    # provides clear feedback for incorrect usage.
    if not isinstance(datetime_obj, datetime):
        raise TypeError("Input 'datetime_obj' must be a datetime object.")

    # The .date() method of a datetime object directly returns a date object
    # containing only the year, month, and day components.
    return datetime_obj.date()


def date_to_string(date_input: datetime, format_code: str = '%Y-%m-%d') -> str:
    """Converts a datetime object into a formatted string.
    
    Description:
        Formats a datetime object as a string using Python's strftime format codes.
        Useful for displaying dates in human-readable formats or for system
        integration requiring specific date string conventions.
    
    Args:
        date_input (datetime): The datetime object to convert to a string.
        format_code (str, optional): The format code string (e.g., '%Y-%m-%d',
                                    '%d/%m/%Y %H:%M:%S'). Defaults to '%Y-%m-%d'.
    
    Returns:
        str: The formatted date string.
    
    Raises:
        TypeError: If 'date_input' is not a datetime object.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from formulite.fxDate.date_convertions import date_to_string
        >>> my_date = datetime(2026, 1, 3, 14, 30, 45)
        >>> date_to_string(my_date)  # Default format
        '2026-01-03'
        >>> date_to_string(my_date, '%d/%m/%Y')  # European format
        '03/01/2026'
        >>> date_to_string(my_date, '%Y-%m-%d %H:%M:%S')  # With time
        '2026-01-03 14:30:45'
    
    Cost: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # Use the strftime method to format the datetime object into a string.
    return date_input.strftime(format_code)


def datetime_to_integer(date_input: Union[datetime, date, str], input_format: str = None) -> int:
    """Converts a date to an integer in YYYYMMDD format, ignoring time.
    
    Description:
        Transforms a date into an integer representation (YYYYMMDD) for
        compact storage and easy numerical comparisons. Time components
        are ignored. Accepts datetime, date objects, or strings.
    
    Args:
        date_input (Union[datetime, date, str]): The date to convert.
                                                 Can be datetime, date, or string.
        input_format (str, optional): Format code if 'date_input' is a string.
                                     Required when 'date_input' is a string.
    
    Returns:
        int: The date as YYYYMMDD integer (e.g., 20260103).
    
    Raises:
        TypeError: If 'date_input' is not datetime, date, or string.
        ValueError: If 'date_input' is string and 'input_format' not provided,
                   or if parsing fails.
    
    Usage Example:
        >>> from datetime import datetime, date
        >>> from formulite.fxDate.date_convertions import datetime_to_integer
        >>> datetime_to_integer(datetime(2026, 1, 3))
        20260103
        >>> datetime_to_integer(date(2026, 1, 3))
        20260103
        >>> datetime_to_integer("03/01/2026", "%d/%m/%Y")
        20260103
    
    Cost: O(1)
    """
    parsed_dt: Union[datetime, date]

    if isinstance(date_input, str):
        if input_format is None:
            raise ValueError("'input_format' is required when 'date_input' is a string.")
        try:
            parsed_dt = datetime.strptime(date_input, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_input}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_input, (datetime, date)):
        parsed_dt = date_input
    else:
        raise TypeError("Input 'date_input' must be a datetime object, date object or a string.")

    # The conversion naturally only uses year, month, and day, ignoring time
    yyyymmdd_integer = parsed_dt.year * 10000 + parsed_dt.month * 100 + parsed_dt.day

    return yyyymmdd_integer


def datetime_to_timestamp(date_input: datetime) -> float:
    """Converts a datetime object to a Unix timestamp.
    
    Description:
        Converts a datetime to Unix timestamp (seconds since epoch:
        January 1, 1970, 00:00:00 UTC). Best used with timezone-aware
        datetime objects in UTC. Naive datetimes are treated as local time.
    
    Args:
        date_input (datetime): The datetime object to convert. Recommended to be
                              timezone-aware (preferably UTC) for accuracy.
    
    Returns:
        float: The Unix timestamp as a float (seconds since epoch).
    
    Raises:
        TypeError: If 'date_input' is not a datetime object.
    
    Usage Example:
        >>> from datetime import datetime, timezone
        >>> from formulite.fxDate.date_convertions import datetime_to_timestamp
        >>> dt_utc = datetime(2026, 1, 3, 0, 0, 0, tzinfo=timezone.utc)
        >>> datetime_to_timestamp(dt_utc)
        1735862400.0
    
    Cost: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # The .timestamp() method on a datetime object returns the Unix timestamp.
    # It handles timezone-aware objects correctly by converting to UTC first.
    # For naive objects, it assumes local time.
    return date_input.timestamp()


def timestamp_to_datetime(timestamp_input: Union[int, float]) -> datetime:
    """Converts a Unix timestamp back to a datetime object.
    
    Description:
        Converts a Unix timestamp (seconds since epoch: January 1, 1970, 00:00:00 UTC)
        to a timezone-aware datetime object in UTC. Complements datetime_to_timestamp().
    
    Args:
        timestamp_input (Union[int, float]): The Unix timestamp to convert.
    
    Returns:
        datetime: A timezone-aware datetime object in UTC.
    
    Raises:
        TypeError: If 'timestamp_input' is not an integer or float.
        ValueError: If timestamp is outside valid range for datetime conversion.
    
    Usage Example:
        >>> from formulite.fxDate.date_convertions import timestamp_to_datetime
        >>> timestamp_to_datetime(1735862400.0)
        datetime.datetime(2026, 1, 3, 0, 0, tzinfo=datetime.timezone.utc)
        >>> timestamp_to_datetime(1735862400)
        datetime.datetime(2026, 1, 3, 0, 0, tzinfo=datetime.timezone.utc)
    
    Cost: O(1)
    """
    if not isinstance(timestamp_input, (int, float)):
        raise TypeError("Input 'timestamp_input' must be an integer or a float.")

    try:
        # datetime.fromtimestamp() creates a datetime object from a Unix timestamp.
        # It's important to specify tz=timezone.utc to get a UTC-aware datetime,
        # otherwise, it defaults to the local timezone, which can be ambiguous.
        return datetime.fromtimestamp(timestamp_input, tz=timezone.utc)
    except ValueError as e:
        raise ValueError(f"Invalid timestamp value '{timestamp_input}': {e}") from e
    

def date_to_iso_format(date_input: Union[datetime, str], input_format: str = None) -> str:
    """Converts a datetime object to an ISO 8601 formatted string.

    ISO 8601 is an international standard for representing dates and times,
    ensuring clarity and interoperability across different systems and locales.
    The common format is YYYY-MM-DDTHH:MM:SS.ffffff+HH:MM (date, 'T', time, microseconds, and timezone offset).

    Args:
        date_input (Union[datetime, str]): The date to convert.
                                            Can be a datetime object (e.g., `datetime(2023, 10, 26, 15, 30)`)
                                            or a string (e.g., `"26/10/2023 15:30:00"`).
        input_format (str, optional): The format code string for `date_input` if it's a string.
                                      This is **required** if `date_input` is a string.
                                      Example: `'%d/%m/%Y %H:%M:%S'` for `"26/10/2023 15:30:00"`.
                                      Not used if `date_input` is a `datetime` object.

    Returns:
        str: The date represented as an ISO 8601 formatted string.

    Raises:
        TypeError: If `date_input` is not a `datetime` object or a string.
        ValueError: If `date_input` is a string and `input_format` is not provided,
                    or if the string cannot be parsed with the given format.

    Example:
        >>> from datetime import datetime, timezone

        >>> # Example with a naive datetime object (no timezone)
        >>> date_to_iso_format(datetime(2023, 1, 15, 10, 30, 45, 123456))
        '2023-01-15T10:30:45.123456'

        >>> # Example with a timezone-aware datetime object (recommended for robustness)
        >>> dt_utc = datetime(2023, 1, 15, 10, 30, 45, 123456, tzinfo=timezone.utc)
        >>> date_to_iso_format(dt_utc)
        '2023-01-15T10:30:45.123456+00:00'

        >>> # Example with a date-only datetime object
        >>> date_to_iso_format(datetime(2024, 7, 20).date()) # Convert to datetime first
        '2024-07-20T00:00:00'

        >>> # Example with string input
        >>> date_to_iso_format("2023-05-10 08:00:00", "%Y-%m-%d %H:%M:%S")
        '2023-05-10T08:00:00'

        >>> # Example of an invalid input (string without format)
        >>> try:
        >>>     date_to_iso_format("2023-05-10")
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: 'input_format' is required when 'date_input' is a string.
    
    Cost: O(1)
    """
    # First, ensure we have a datetime object to work with.
    parsed_dt: datetime
    if isinstance(date_input, str):
        if input_format is None:
            raise ValueError("'input_format' is required when 'date_input' is a string.")
        try:
            parsed_dt = datetime.strptime(date_input, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_input}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_input, datetime):
        parsed_dt = date_input
    elif isinstance(date_input, datetime.date):
        # If it's a date object, convert it to a datetime at midnight
        parsed_dt = datetime(date_input.year, date_input.month, date_input.day)
    else:
        raise TypeError("Input 'date_input' must be a datetime object, date object, or a string.")

    # The datetime object's .isoformat() method handles the conversion directly.
    return parsed_dt.isoformat()


def from_iso_to_local_datetime(iso_string: str) -> datetime:
    """Converts an ISO 8601 formatted string to a datetime object in the local timezone.

    This function is designed to handle ISO 8601 strings that may or may not
    contain timezone information (e.g., 'Z' for UTC or a '+HH:MM' offset).
    It will parse the string and then convert the resulting datetime object
    to the system's local timezone.

    Args:
        iso_string (str): The date and time as an ISO 8601 formatted string.
                          Examples:
                          - '2023-10-26T15:30:45.123456' (naive, assumed local or UTC)
                          - '2023-10-26T15:30:45Z' (UTC)
                          - '2023-10-26T15:30:45+02:00' (UTC+2 offset)

    Returns:
        datetime: A timezone-aware datetime object representing the input date
                  and time, adjusted to the system's local timezone.

    Raises:
        TypeError: If `iso_string` is not a string.
        ValueError: If `iso_string` is not a valid ISO 8601 format that
                    `datetime.fromisoformat()` can parse, or if the local
                    timezone cannot be determined.

    Example:
        >>> from datetime import datetime, timezone, timedelta

        >>> # Example 1: ISO string with UTC 'Z' (Zulu time)
        >>> iso_utc_string = "2023-10-26T15:30:00Z"
        >>> local_dt = from_iso_to_local_datetime(iso_utc_string)
        >>> print(f"UTC string '{iso_utc_string}' -> Local: {local_dt}")
        # On a system in CEST (UTC+2), this would show: 2023-10-26 17:30:00+02:00

        >>> # Example 2: ISO string with an explicit offset (+02:00)
        >>> iso_offset_string = "2023-10-26T15:30:00+02:00"
        >>> local_dt = from_iso_to_local_datetime(iso_offset_string)
        >>> print(f"Offset string '{iso_offset_string}' -> Local: {local_dt}")
        # On a system in CEST (UTC+2), this would show: 2023-10-26 15:30:00+02:00

        >>> # Example 3: ISO string without timezone info (naive)
        >>> # datetime.fromisoformat() treats naive strings as local by default,
        # but it's safer to make it aware first for consistent conversion.
        >>> iso_naive_string = "2023-10-26T15:30:00"
        >>> local_dt = from_iso_to_local_datetime(iso_naive_string)
        >>> print(f"Naive string '{iso_naive_string}' -> Local: {local_dt}")
        # On a system in CEST (UTC+2), this would show: 2023-10-26 15:30:00+02:00
    
    Cost: O(1)
    """
    if not isinstance(iso_string, str):
        raise TypeError("Input 'iso_string' must be a string.")

    # 1. Parse the ISO string into a datetime object
    try:
        # Python 3.10's datetime.fromisoformat() doesn't support 'Z' suffix for UTC
        # Replace 'Z' with '+00:00' for compatibility
        normalized_string = iso_string.replace('Z', '+00:00') if iso_string.endswith('Z') else iso_string
        
        # datetime.fromisoformat() handles various ISO 8601 formats,
        # including those with explicit offsets like '+02:00'.
        dt_object = datetime.fromisoformat(normalized_string)
    except ValueError as e:
        raise ValueError(f"Invalid ISO 8601 string format: '{iso_string}'. Error: {e}") from e

    # 2. Handle timezone conversion using datetime.astimezone() which automatically
    #    determines the local timezone without needing explicit ZoneInfo("localtime")
    if dt_object.tzinfo is None:
        # If the parsed datetime object is naive (no timezone info),
        # assume it's in UTC, then convert it to local timezone.
        # This is a common and safe assumption for naive ISO strings from APIs.
        dt_object = dt_object.replace(tzinfo=timezone.utc)
    
    # Convert to local timezone using astimezone() without argument
    # This automatically uses the system's local timezone and works on all platforms
    return dt_object.astimezone()
    

def list_available_timezones() -> List[str]:
    """Retrieves and returns a sorted list of all available IANA time zone names.

    These names are used by the 'zoneinfo' module (and other timezone libraries)
    to accurately handle time conversions, daylight saving rules, and historical offsets.

    Returns:
        List[str]: A sorted list of strings, where each string is a valid IANA time zone name.

    Example:
        >>> timezones = list_available_timezones()
        >>> # The exact output depends on your system's timezone data, but will include many.
        >>> print(timezones[:5]) # Print the first 5 for brevity
        # Expected output might look like: ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara']
        >>> print('Europe/Madrid' in timezones)
        True
    
    Cost: O(n log n) where n is the number of available timezones
    """
    # zoneinfo.available_timezones() returns a set of all available timezone keys.
    # We convert it to a list and sort it for consistent, readable output.
    return sorted(list(zoneinfo.available_timezones()))


def convert_timezone(date_input: datetime, target_tz_name: str) -> datetime:
    """Converts a timezone-aware datetime object from its current timezone to a target timezone.

    This function is crucial for ensuring that date and time information is displayed
    and processed correctly across different geographical regions and their respective
    timezones. The input datetime MUST be timezone-aware.

    Args:
        date_input (datetime): The timezone-aware datetime object to convert.
                                It must have `tzinfo` set (e.g., `datetime.now(timezone.utc)`).
        target_tz_name (str): The name of the target timezone (e.g., 'America/New_York',
                              'Europe/Madrid', 'Asia/Tokyo', 'UTC'). These are
                              typically IANA timezone database names.

    Returns:
        datetime: A new datetime object representing the same moment in time,
                  but localized to the `target_tz_name`.

    Raises:
        TypeError: If `date_input` is not a datetime object.
        ValueError: If `date_input` is a naive datetime object (missing timezone info).
        zoneinfo.ZoneInfoNotFoundError: If `target_tz_name` is not a recognized timezone
                                        in the system's timezone database.

    Example:
        >>> from datetime import datetime
        >>> import zoneinfo

        >>> # 1. Define a UTC datetime
        >>> utc_now = datetime(2025, 6, 11, 1, 1, 45, tzinfo=timezone.utc)
        >>> print(f"Original UTC: {utc_now}")
        Original UTC: 2025-06-11 01:01:45+00:00

        >>> # 2. Convert to Madrid Time (CEST = UTC+2)
        >>> madrid_time = convert_timezone(utc_now, 'Europe/Madrid')
        >>> print(f"In Madrid: {madrid_time}")
        In Madrid: 2025-06-11 03:01:45+02:00

        >>> # 3. Convert to New York Time (EDT = UTC-4 in summer)
        >>> ny_time = convert_timezone(utc_now, 'America/New_York')
        >>> print(f"In New York: {ny_time}")
        In New York: 2025-06-10 21:01:45-04:00

        >>> # Example of trying to convert a naive datetime (will raise ValueError)
        >>> naive_dt = datetime(2025, 6, 11, 10, 0, 0)
        >>> try:
        >>>     convert_timezone(naive_dt, 'Europe/London')
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Input datetime object must be timezone-aware.
    
    Cost: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # Crucial check: Ensure the input datetime is timezone-aware.
    if date_input.tzinfo is None:
        raise ValueError("Input datetime object must be timezone-aware (have tzinfo set) for conversion.")

    # 1. Get the target timezone object
    try:
        target_tz = zoneinfo.ZoneInfo(target_tz_name)
    except zoneinfo.ZoneInfoNotFoundError:
        # Re-raise with a more informative message if the timezone name is not found.
        raise zoneinfo.ZoneInfoNotFoundError(
            f"Timezone '{target_tz_name}' not found. "
            "Please use a valid IANA timezone name (e.g., 'America/New_York', 'Europe/London')."
        )

    # 2. Convert the datetime object to the target timezone
    # The .astimezone() method performs the conversion correctly.
    # If the input is already in UTC, this will convert it to the target_tz.
    # If the input is in another timezone, it will first convert it to UTC implicitly, then to target_tz.
    return date_input.astimezone(target_tz)


def utc_to_datetime(
    date_input: Union[datetime, str],
    input_format: Optional[str] = None,
    input_tz: Optional[str] = None
) -> datetime:
    """Converts any datetime object (aware or naive) or date string to its equivalent UTC representation.

    Problem/User Need: The best practice for storing dates is in UTC to avoid
    timezone and daylight saving issues. Users need a simple way to normalize
    any date to UTC before saving or processing it.

    Product Goals: Promote consistency in date storage and processing, simplifying
    business logic and preventing timezone-related errors.

    Description: Given a date input, this function performs the following:
    1. If `date_input` is a string, it parses it into a datetime object.
    2. If the resulting datetime object is naive (has no timezone info):
       a. If `input_tz` is provided, it assumes the naive datetime is in that timezone.
       b. If `input_tz` is NOT provided, it assumes the naive datetime is in the
          system's **local timezone**.
    3. If the resulting datetime object is already timezone-aware, it uses its
       existing timezone information.
    4. Finally, it converts the datetime object to UTC.

    Args:
        date_input (Union[datetime, str]): The date to convert to UTC.
                                            Can be a datetime object (e.g., `datetime(2025, 6, 11, 10, 0, 0)`)
                                            or a string (e.g., `"2025-06-11 10:00:00"`).
        input_format (Optional[str], optional): The format code string for `date_input` if it's a string.
                                                This is **required** if `date_input` is a string.
                                                Example: `'%Y-%m-%d %H:%M:%S'`.
        input_tz (Optional[str], optional): The IANA timezone name of the `date_input`
                                            if it's a naive `datetime` object or a string
                                            that doesn't contain timezone info. If `None`
                                            and `date_input` is naive, the system's local
                                            timezone is assumed. Example: `'America/Los_Angeles'`, `'Europe/Madrid'`.

    Returns:
        datetime: A timezone-aware datetime object representing the input date
                  and time in UTC.

    Raises:
        TypeError: If `date_input` is not a `datetime` object or a string.
        ValueError: If `date_input` is a string and `input_format` is not provided,
                    or if the string cannot be parsed with the given format.
                    If `input_tz` is provided but is not a recognized timezone.
                    If the local timezone cannot be determined.

    Example:
        >>> from datetime import datetime, timezone
        >>> import zoneinfo

        >>> # Scenario 1: Input is a naive datetime object (system local time is CEST = UTC+2)
        >>> # Assuming the system's local timezone is Europe/Madrid (currently CEST, UTC+2)
        >>> naive_dt_local = datetime(2025, 6, 11, 10, 0, 0) # 10:00 AM local time
        >>> utc_dt = utc_to_datetime(naive_dt_local)
        >>> print(f"Naive local (10:00 CEST) -> UTC: {utc_dt}")
        # Expected: 2025-06-11 08:00:00+00:00 (10:00 CEST - 2 hours = 08:00 UTC)

        >>> # Scenario 2: Input is an aware datetime object (e.g., in 'America/Los_Angeles')
        >>> la_tz = zoneinfo.ZoneInfo('America/Los_Angeles')
        >>> aware_dt_la = datetime(2025, 6, 11, 10, 0, 0, tzinfo=la_tz) # 10:00 AM in LA (PDT, UTC-7)
        >>> utc_dt = utc_to_datetime(aware_dt_la)
        >>> print(f"Aware LA (10:00 PDT) -> UTC: {utc_dt}")
        # Expected: 2025-06-11 17:00:00+00:00 (10:00 PDT + 7 hours = 17:00 UTC)

        >>> # Scenario 3: Input is a string, and we specify its original timezone
        >>> # Date string "2025-06-11 10:00:00" is in 'Asia/Tokyo' (JST, UTC+9)
        >>> utc_dt = utc_to_datetime("2025-06-11 10:00:00", "%Y-%m-%d %H:%M:%S", "Asia/Tokyo")
        >>> print(f"String Tokyo (10:00 JST) -> UTC: {utc_dt}")
        # Expected: 2025-06-11 01:00:00+00:00 (10:00 JST - 9 hours = 01:00 UTC)

        >>> # Scenario 4: Input is a string with no explicit timezone provided, assumes local
        >>> # Assuming local system is CEST (UTC+2)
        >>> utc_dt = utc_to_datetime("2025-06-11 10:00:00", "%Y-%m-%d %H:%M:%S")
        >>> print(f"String local (10:00 CEST) -> UTC: {utc_dt}")
        # Expected: 2025-06-11 08:00:00+00:00
    
    Cost: O(1)
    """
    # 1. Parse the input into a datetime object
    parsed_dt: datetime
    if isinstance(date_input, str):
        if input_format is None:
            raise ValueError("'input_format' is required when 'date_input' is a string.")
        try:
            parsed_dt = datetime.strptime(date_input, input_format)
        except ValueError as e:
            raise ValueError(f"Could not parse date string '{date_input}' with format '{input_format}'. Error: {e}") from e
    elif isinstance(date_input, datetime):
        parsed_dt = date_input
    else:
        raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # 2. Make the datetime object timezone-aware if it's naive
    if parsed_dt.tzinfo is None:
        # Determine the timezone to assume for the naive input
        assumed_tz: zoneinfo.ZoneInfo
        if input_tz:
            try:
                assumed_tz = zoneinfo.ZoneInfo(input_tz)
            except zoneinfo.ZoneInfoNotFoundError:
                raise ValueError(f"Specified 'input_tz' timezone '{input_tz}' not found.")
        else:
            # If no input_tz is provided, assume the system's local timezone.
            try:
                assumed_tz = zoneinfo.ZoneInfo("localtime")
            except zoneinfo.ZoneInfoNotFoundError:
                raise ValueError(
                    "Could not determine local timezone for naive input. "
                    "Please provide 'input_tz' or ensure system timezone is configured."
                )
        
        # Localize the naive datetime to the assumed timezone
        parsed_dt = parsed_dt.replace(tzinfo=assumed_tz)
        # Note: For historical dates and timezones with complex rules (like DST transitions),
        # using `assumed_tz.localize(parsed_dt)` from dateutil or pytz is sometimes
        # more robust than `.replace(tzinfo=...)` for ambiguity resolution.
        # However, for general normalization, .replace() followed by .astimezone() is often sufficient.
    
    # 3. Convert the (now timezone-aware) datetime object to UTC
    # .astimezone(timezone.utc) ensures it's converted to UTC.
    return parsed_dt.astimezone(timezone.utc)


def utc_to_timezone(input_datetime: datetime, target_tz_name: str = "Europe/Madrid") -> datetime:
    """Localizes a naive datetime object to the target timezone or validates an aware datetime,
    then returns it localized to the target timezone.

    This function is used when you have a datetime that might be naive (without tzinfo)
    and you need to assume a specific timezone for it, or when you have an aware datetime
    and want to ensure it's converted to the target timezone. If the input datetime is naive,
    it will be localized directly to the `target_tz_name`. If it's already timezone-aware,
    it will be converted to the `target_tz_name`.

    Args:
        input_datetime (datetime): The datetime object to process. If it's naive,
                                   it will be localized to `target_tz_name`. If it's
                                   already timezone-aware, it will be converted
                                   to `target_tz_name`.
        target_tz_name (str): The name of the target timezone to localize/convert to (e.g.,
                               'America/New_York', 'Europe/Madrid', 'Asia/Tokyo').
                               These are typically IANA timezone database names.

    Returns:
        datetime: A new timezone-aware datetime object representing the same moment in time,
                  but localized to the `target_tz_name`.

    Raises:
        TypeError: If `input_datetime` is not a datetime object.
        zoneinfo.ZoneInfoNotFoundError: If `target_tz_name` is not a recognized timezone
                                        in the system's timezone database.

    Example:
        >>> from datetime import datetime, timezone
        >>> import zoneinfo

        >>> # 1. Define a target timezone (e.g., Europe/Madrid)
        >>> madrid_tz = zoneinfo.ZoneInfo('Europe/Madrid')

        >>> # 2. Define a naive datetime
        >>> naive_dt = datetime(2025, 6, 11, 10, 0, 0) # 10:00 AM, but in which timezone?
        >>> print(f"Original Naive: {naive_dt}")

        >>> # Localize naive_dt directly to Madrid time (assumes 10:00 AM Madrid time)
        >>> localized_to_madrid = utc_to_timezone(naive_dt, 'Europe/Madrid')
        >>> print(f"Localized to Madrid: {localized_to_madrid}")
        # Expected: 2025-06-11 10:00:00+02:00 (since June in Madrid is UTC+2)

        >>> # Now convert the Madrid-localized time to New York time (PDT = UTC-4 in June for NY)
        >>> madrid_to_ny = utc_to_timezone(localized_to_madrid, 'America/New_York')
        >>> print(f"Madrid time converted to New York: {madrid_to_ny}")
        # Expected: 2025-06-11 04:00:00-04:00 (10:00 Madrid is 08:00 UTC, which is 04:00 NY)

        >>> # 3. Define an already aware datetime (e.g., in UTC)
        >>> utc_aware_dt = datetime(2025, 6, 11, 8, 0, 0, tzinfo=timezone.utc) # 8:00 AM UTC
        >>> print(f"\nOriginal UTC Aware: {utc_aware_dt}")

        >>> # Convert the UTC aware datetime to Madrid time
        >>> utc_to_madrid = utc_to_timezone(utc_aware_dt, 'Europe/Madrid')
        >>> print(f"UTC Aware converted to Madrid: {utc_to_madrid}")
        # Expected: 2025-06-11 10:00:00+02:00
    
    Cost: O(1)
    """
    if not isinstance(input_datetime, datetime):
        raise TypeError("Input 'input_datetime' must be a datetime object.")

    # 1. Get the target timezone object
    try:
        target_tz = zoneinfo.ZoneInfo(target_tz_name)
    except zoneinfo.ZoneInfoNotFoundError:
        raise zoneinfo.ZoneInfoNotFoundError(
            f"Timezone '{target_tz_name}' not found. "
            "Please use a valid IANA timezone name (e.g., 'America/New_York', 'Europe/London')."
        )

    # If the datetime object is naive (tzinfo is None), localize it directly to the target timezone.
    # This means we are assuming that the naive datetime represents a time in `target_tz_name`.
    if input_datetime.tzinfo is None:
        return input_datetime.replace(tzinfo=target_tz)
    # If it's already timezone-aware, convert it to the target timezone.
    else:
        return input_datetime.astimezone(target_tz)
   

def date_to_julian(date_input: Union[datetime, str], input_format: Optional[str] = None) -> int:
    """Convierte una fecha estándar a su representación de fecha Juliana (día del año).

    Problema/Necesidad del Usuario: Para ciertos sistemas antiguos o en astronomía,
    las fechas se representan como el número de día del año (ej. el día 32 es el 1 de Febrero).
    Es necesario convertir fechas comunes a este formato.

    Objetivos del Producto: Proporcionar una forma sencilla de obtener el "día del año"
    para una fecha dada, facilitando la integración con sistemas que utilizan este formato.

    Descripción: Dada una fecha (como objeto `datetime` o cadena de texto),
    esta función devuelve el número del día dentro de ese año. Enero 1 es el día 1,
    Febrero 1 es el día 32 (o 33 en un año bisiesto), etc.

    Args:
        date_input (Union[datetime, str]): La fecha a convertir. Puede ser un objeto
                                            `datetime` o una cadena de fecha.
        input_format (str, optional): El formato de cadena de fecha (ej. '%Y-%m-%d')
                                      si 'date_input' es una cadena. Es **obligatorio**
                                      si 'date_input' es una cadena.

    Returns:
        int: El número del día del año (1 a 365 o 366).

    Raises:
        TypeError: Si 'date_input' no es un objeto `datetime` o una cadena.
        ValueError: Si 'date_input' es una cadena y 'input_format' es `None`,
                    o si la cadena no puede ser parseada con el formato dado.

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: Enero 1, 2025 (siempre día 1)
        >>> date_to_julian(datetime(2025, 1, 1))
        1

        >>> # Ejemplo 2: Febrero 1, 2025 (año no bisiesto)
        >>> date_to_julian(datetime(2025, 2, 1))
        32 # 31 días de Enero + 1 día de Febrero

        >>> # Ejemplo 3: Marzo 1, 2024 (año bisiesto)
        >>> date_to_julian(datetime(2024, 3, 1))
        61 # 31 (Ene) + 29 (Feb 2024) + 1 (Mar) = 61

        >>> # Ejemplo 4: 31 de Diciembre de un año común
        >>> date_to_julian(datetime(2023, 12, 31))
        365

        >>> # Ejemplo 5: 31 de Diciembre de un año bisiesto
        >>> date_to_julian(datetime(2024, 12, 31))
        366

        >>> # Ejemplo 6: Usando cadena de fecha
        >>> date_to_julian("2025-06-15", "%Y-%m-%d")
        166 # Día 166 del año 2025
    
    Cost: O(1)
    """
    # Función auxiliar interna para parsear la entrada de fecha (datetime o string)
    def _parse_date_input_internal(date_val: Union[datetime, str], input_fmt: Optional[str]) -> datetime:
        if isinstance(date_val, str):
            if input_fmt is None:
                raise ValueError("'input_format' is required when 'date_input' is a string.")
            try:
                return datetime.strptime(date_val, input_fmt)
            except ValueError as e:
                raise ValueError(f"Could not parse date string '{date_val}' with format '{input_fmt}'. Error: {e}") from e
        elif isinstance(date_val, datetime):
            return date_val
        else:
            raise TypeError("Input 'date_input' must be a datetime object or a string.")

    # Parsear la fecha de entrada
    parsed_date = _parse_date_input_internal(date_input, input_format)

    # El atributo tm_yday del resultado de .timetuple() da directamente el día del año (1-indexed)
    return parsed_date.timetuple().tm_yday


def julian_to_date(julian_date: int, year: int) -> datetime:
    """Convierte una fecha Juliana (día del año) a un objeto datetime estándar.

    Problema/Necesidad del Usuario: Cuando se reciben fechas en formato Julian (día del año)
    desde sistemas externos, es necesario convertirlas a un formato de fecha estándar
    para su manipulación y visualización.

    Objetivos del Producto: Proporcionar una forma directa de construir una fecha
    estándar a partir de su número de día del año, manejando correctamente los años bisiestos.

    Descripción: Dada un número de día del año (fecha Juliana, de 1 a 366) y un año,
    esta función reconstruye y devuelve el objeto `datetime` correspondiente.
    La fecha devuelta tendrá su componente de tiempo establecido a medianoche (00:00:00).

    Args:
        julian_date (int): El número del día del año (1 a 365 o 366).
                           Debe ser un entero positivo.
        year (int): El año al que pertenece la fecha Juliana.

    Returns:
        datetime: Un objeto `datetime` representando la fecha calculada (a medianoche).

    Raises:
        TypeError: Si 'julian_date' o 'year' no son enteros.
        ValueError: Si 'year' está fuera del rango válido (1-9999),
                    o si 'julian_date' está fuera del rango válido (1 a 365/366
                    dependiendo del año bisiesto).

    Example:
        >>> from datetime import datetime

        >>> # Ejemplo 1: Día 1 del año 2025
        >>> julian_to_date(1, 2025)
        datetime.datetime(2025, 1, 1, 0, 0)

        >>> # Ejemplo 2: Día 32 del año 2025 (Febrero 1)
        >>> julian_to_date(32, 2025)
        datetime.datetime(2025, 2, 1, 0, 0)

        >>> # Ejemplo 3: Día 61 del año 2024 (Marzo 1, año bisiesto)
        >>> julian_to_date(61, 2024)
        datetime.datetime(2024, 3, 1, 0, 0) # 31 (Ene) + 29 (Feb 2024) + 1 (Mar) = 61

        >>> # Ejemplo 4: Día 365 del año 2023 (Diciembre 31, año no bisiesto)
        >>> julian_to_date(365, 2023)
        datetime.datetime(2023, 12, 31, 0, 0)

        >>> # Ejemplo 5: Día 366 del año 2024 (Diciembre 31, año bisiesto)
        >>> julian_to_date(366, 2024)
        datetime.datetime(2024, 12, 31, 0, 0)

        >>> # Día Juliana inválido para un año (levantará ValueError)
        >>> try:
        >>>     julian_to_date(366, 2023) # 2023 no es bisiesto, solo tiene 365 días
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: Julian date must be between 1 and 365 for year 2023.
    
    Cost: O(1)
    """
    # 1. Validación de entradas
    if not isinstance(julian_date, int):
        raise TypeError("Input 'julian_date' must be an integer.")
    if not isinstance(year, int):
        raise TypeError("Input 'year' must be an integer.")
    
    if not (1 <= year <= 9999): # Rango común de años para objetos datetime
        raise ValueError("Year is out of valid range (1-9999).")

    # Determinar el número máximo de días en el año para validar julian_date
    max_days_in_year = 366 if calendar.isleap(year) else 365
    if not (1 <= julian_date <= max_days_in_year):
        raise ValueError(f"Julian date must be between 1 and {max_days_in_year} for year {year}.")

    # Crear una fecha para el 1 de enero del año dado
    start_of_year = datetime(year, 1, 1)

    # Añadir (julian_date - 1) días a la fecha del 1 de enero para obtener la fecha deseada.
    # Se resta 1 porque julian_date es 1-indexed (día 1 es Enero 1).
    target_date = start_of_year + timedelta(days=julian_date - 1)

    # Devolver la fecha con la hora a medianoche para consistencia
    return target_date.replace(hour=0, minute=0, second=0, microsecond=0)


def datetime_to_milliseconds_timestamp(date_input: datetime) -> int:
    """Convierte un objeto datetime a un sello de tiempo Unix en milisegundos.

    Problema/Necesidad del Usuario: Muchos sistemas modernos (APIs, bases de datos NoSQL,
    sistemas de logging de alto rendimiento) utilizan sellos de tiempo en milisegundos
    en lugar de segundos para una mayor granularidad. Es crucial poder convertir
    datetime a este formato.

    Objetivos del Producto: Facilitar la integración con sistemas que requieren sellos
    de tiempo de milisegundos, mejorando la compatibilidad y la precisión en el registro de eventos.

    Descripción: Esta función toma un objeto `datetime` y lo convierte en el número de
    milisegundos transcurridos desde la Época Unix (1 de enero de 1970, 00:00:00 UTC).
    Asegúrate de que tu objeto `datetime` tenga información de zona horaria (UTC preferiblemente)
    para evitar ambigüedades.

    Args:
        date_input (datetime): El objeto `datetime` a convertir. Preferiblemente con `tzinfo=timezone.utc`.

    Returns:
        int: El sello de tiempo Unix en milisegundos.

    Raises:
        TypeError: Si 'date_input' no es un objeto `datetime`.

    Example:
        >>> from datetime import datetime, timezone
        >>> dt_utc = datetime(2025, 6, 11, 1, 58, 11, 123456, tzinfo=timezone.utc)
        >>> datetime_to_milliseconds_timestamp(dt_utc)
        1749597491123
        >>> # Si el datetime no tiene información de zona horaria, se asume UTC
        >>> dt_naive = datetime(2025, 6, 11, 1, 58, 11, 123456)
        >>> datetime_to_milliseconds_timestamp(dt_naive) # Se comportará como si fuera UTC
        1749597491123
    
    Cost: O(1)
    """
    if not isinstance(date_input, datetime):
        raise TypeError("Input 'date_input' must be a datetime object.")

    # Aseguramos que el datetime es consciente de la zona horaria y en UTC para el timestamp Unix
    # Si date_input no tiene tzinfo, se asume UTC por defecto para el timestamp() de Python.
    # Pero para claridad y robustez, es buena práctica hacerla explícitamente UTC.
    if date_input.tzinfo is None:
        # Consideramos naive datetime como UTC para la conversión a timestamp Unix
        utc_dt = date_input.replace(tzinfo=timezone.utc)
    else:
        # Convertimos a UTC si ya es consciente de la zona horaria pero no es UTC
        utc_dt = date_input.astimezone(timezone.utc)

    # Convertir a segundos desde la época Unix y luego a milisegundos,
    # incluyendo los microsegundos del datetime.
    # El método timestamp() devuelve un float en segundos. Multiplicamos por 1000
    # y redondeamos a entero.
    return int(utc_dt.timestamp() * 1000)


def milliseconds_timestamp_to_datetime(timestamp_ms: int) -> datetime:
    """Convierte un sello de tiempo Unix en milisegundos a un objeto datetime.

    Problema/Necesidad del Usuario: La contraparte de la anterior. Poder tomar
    un sello de tiempo en milisegundos y convertirlo de nuevo a un objeto datetime
    para su manipulación y visualización.

    Objetivos del Producto: Completar el ciclo de conversión con sellos de tiempo
    de milisegundos, permitiendo el procesamiento bidireccional de datos de alta resolución.

    Descripción: Esta función toma un entero que representa un sello de tiempo Unix
    en milisegundos y lo convierte en un objeto `datetime` consciente de la zona horaria,
    establecido en UTC.

    Args:
        timestamp_ms (int): El sello de tiempo Unix en milisegundos a convertir.

    Returns:
        datetime: Un objeto `datetime` que representa la fecha y hora del sello de tiempo,
                  con información de zona horaria UTC.

    Raises:
        TypeError: Si 'timestamp_ms' no es un entero.
        ValueError: Si el sello de tiempo es negativo, lo que no es válido en el contexto Unix.

    Example:
        >>> from datetime import datetime, timezone
        >>> milliseconds_timestamp_to_datetime(1749597491123)
        datetime.datetime(2025, 6, 11, 1, 58, 11, 123000, tzinfo=datetime.timezone.utc)
    
    Cost: O(1)
    """
    if not isinstance(timestamp_ms, int):
        raise TypeError("Input 'timestamp_ms' must be an integer.")
    if timestamp_ms < 0:
        raise ValueError("Timestamp in milliseconds cannot be negative.")

    # Convertir milisegundos a segundos (float)
    timestamp_s = timestamp_ms / 1000.0

    # Crear el objeto datetime a partir del timestamp en segundos, asegurando que sea UTC.
    # El método fromtimestamp() por defecto usa la zona horaria local.
    # Para obtener un datetime UTC, es mejor usar utcfromtimestamp() en versiones anteriores a Python 3.3,
    # o de forma más robusta, datetime.fromtimestamp(timestamp, tz=timezone.utc) en Python 3.3+.
    return datetime.fromtimestamp(timestamp_s, tz=timezone.utc)


def utc_to_midnight_iso(p_datetime: datetime) -> datetime:
    """Convierte un datetime a su equivalente a medianoche UTC.

    Problem/User Need: Es común necesitar normalizar fechas a medianoche UTC 
    para comparaciones consistentes o para asegurar que todos los eventos 
    empiecen al inicio del día.

    Product Goals: Proporcionar una forma sencilla de normalizar cualquier 
    datetime a medianoche UTC manteniendo la fecha.

    Args:
        p_datetime (datetime): El objeto datetime a convertir.

    Returns:
        datetime: Un nuevo objeto datetime establecido a medianoche UTC (00:00:00)
                 para la fecha dada.

    Raises:
        TypeError: Si p_datetime no es un objeto datetime.

    Example:
        >>> from datetime import datetime, timezone
        >>> # Datetime con hora específica
        >>> dt = datetime(2025, 6, 11, 15, 30, 45, tzinfo=timezone.utc)
        >>> midnight_dt = utc_to_midnight_iso(dt)
        >>> print(midnight_dt)
        2025-06-11 00:00:00+00:00

        >>> # Datetime sin zona horaria
        >>> naive_dt = datetime(2025, 6, 11, 15, 30, 45)
        >>> midnight_dt = utc_to_midnight_iso(naive_dt)
        >>> print(midnight_dt)
        2025-06-11 00:00:00+00:00
    
    Cost: O(1)
    """
    if not isinstance(p_datetime, datetime):
        raise TypeError("Input must be a datetime object")

    # Si el datetime es naive (sin zona horaria), asumimos que es UTC
    if p_datetime.tzinfo is None:
        p_datetime = p_datetime.replace(tzinfo=timezone.utc)
    else:
        # Si tiene zona horaria, convertimos a UTC
        p_datetime = p_datetime.astimezone(timezone.utc)

    # Establecer la hora a medianoche manteniendo la fecha y la zona UTC
    midnight_datetime = p_datetime.replace(
        hour=0, 
        minute=0, 
        second=0, 
        microsecond=0
    )

    return midnight_datetime


def filetime_to_datetime(filetime: int) -> Tuple[datetime, str]:
    """Converts a Windows FILETIME value to a datetime object and its string representation.

    Problem/User Need: Windows systems store timestamps in FILETIME format 
    (100-nanosecond intervals since January 1, 1601 UTC). These need to be 
    converted to standard datetime objects for processing.

    Product Goals: Provide accurate conversion of Windows FILETIME values while 
    handling both pre-Unix epoch (before 1970) and modern dates correctly.

    Description: This function converts a 64-bit integer representing Windows FILETIME 
    (number of 100-nanosecond intervals since January 1, 1601 UTC) to:
    1. A timezone-aware datetime object
    2. Its ISO format string representation

    Args:
        filetime (int): The Windows FILETIME value to convert.
                       Must be a positive integer.

    Returns:
        Tuple[datetime, str]: A tuple containing:
            - datetime: The converted datetime object (UTC)
            - str: The ISO formatted string representation

    Raises:
        TypeError: If filetime is not an integer
        ValueError: If filetime is negative

    Example:
        >>> # Modern date (post-1970)
        >>> dt, dt_str = filetime_to_datetime(132723834123456789)
        >>> print(dt)
        2022-01-15 12:30:12.345678+00:00
        >>> print(dt_str)
        2022-01-15 12:30:12.345678

        >>> # Historical date (pre-1970)
        >>> dt, dt_str = filetime_to_datetime(130611456000000000)
        >>> print(dt)
        1601-01-01 00:00:00+00:00
        >>> print(dt_str)
        1601-01-01 00:00:00.000000
    """
    # Input validation
    if not isinstance(filetime, int):
        raise TypeError("FILETIME must be an integer")
    if filetime < 0:
        raise ValueError("FILETIME cannot be negative")

    # Constants
    FILETIME_EPOCH_DIFFERENCE = 116444736000000000  # Difference between Windows and Unix epochs in 100ns intervals

    # Convert based on whether the date is before or after Unix epoch
    if filetime < FILETIME_EPOCH_DIFFERENCE:
        # Pre-1970 dates: Calculate directly from Windows epoch (1601-01-01)
        seconds = filetime / 10_000_000  # Convert 100ns intervals to seconds
        dt = datetime(1601, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=seconds)
    else:
        # Post-1970 dates: Calculate from Unix epoch
        unix_epoch_100ns = filetime - FILETIME_EPOCH_DIFFERENCE
        seconds_since_unix_epoch = unix_epoch_100ns / 10_000_000
        dt = datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=seconds_since_unix_epoch)

    # Return both the datetime object and its string representation
    return dt, dt.isoformat(sep=' ', timespec='microseconds')


def datetime_to_filetime(p_dt: Union[datetime, date]) -> int:
    """
    Convierte un objeto datetime o date de Python a un valor FILETIME de Windows.

    FILETIME es el número de intervalos de 100 nanosegundos transcurridos
    desde el 1 de enero de 1601, 00:00:00 UTC.

    Args:
        p_dt (Union[datetime, date]): El objeto datetime o date a convertir.
                                      Si es un objeto date, se tratará como medianoche (00:00:00) UTC de ese día.
                                      Si es un objeto datetime naive, se asumirá que está en UTC.
                                      Si es un objeto datetime timezone-aware, se convertirá a UTC.

    Returns:
        int: El valor FILETIME como un entero de 64 bits.

    Raises:
        TypeError: Si p_dt no es un objeto datetime ni date.
    """
    if not isinstance(p_dt, (datetime, date)): # Aceptar tanto datetime como date
        raise TypeError("La entrada 'p_dt' debe ser un objeto datetime o date.")

    dt_utc: datetime

    # Si es un objeto date, convertirlo a datetime a medianoche UTC
    if isinstance(p_dt, date) and not isinstance(p_dt, datetime):
        dt_utc = datetime(p_dt.year, p_dt.month, p_dt.day, 0, 0, 0, 0, tzinfo=timezone.utc)
    # Si ya es un objeto datetime, manejar su timezone
    elif p_dt.tzinfo is None:
        # Si es naive, asumimos que ya representa una hora UTC.
        dt_utc = p_dt.replace(tzinfo=timezone.utc)
    else:
        # Si ya es consciente de la zona horaria, lo convertimos a UTC.
        dt_utc = p_dt.astimezone(timezone.utc)

    # Definir el epoch de FILETIME (1 de enero de 1601, 00:00:00 UTC)
    filetime_epoch = datetime(1601, 1, 1, 0, 0, 0, tzinfo=timezone.utc)

    # Calcular la diferencia de tiempo entre la fecha dada y el epoch de FILETIME
    delta = dt_utc - filetime_epoch

    # Convertir la diferencia total a segundos y luego a intervalos de 100 nanosegundos.
    # Cada segundo tiene 10,000,000 de intervalos de 100 nanosegundos.
    filetime_value = int(delta.total_seconds() * 10_000_000)

    return filetime_value


def datetime_to_ad_format(p_dt_input: Union[datetime, date]) -> str:
    """
    Convierte un objeto datetime o date a la cadena de formato
    'YYYYMMDDHHMMSS.0Z' utilizada en Active Directory para atributos
    como 'whenCreated'.

    Args:
        p_dt_input (Union[datetime, date]): El objeto datetime o date a convertir.
                                             Si es un objeto `date`, se asumirá medianoche (00:00:00) UTC.
                                             Si es un objeto `datetime` naive, se asumirá que es UTC.
                                             Si es un objeto `datetime` timezone-aware, se convertirá a UTC.

    Returns:
        str: La fecha y hora formateada como 'YYYYMMDDHHMMSS.0Z'.

    Raises:
        TypeError: Si la entrada no es un objeto datetime ni date.
    """
    if not isinstance(p_dt_input, (datetime, date)):
        raise TypeError("La entrada debe ser un objeto 'datetime' o 'date'.")

    dt_utc: datetime

    # Si es un objeto date, lo convertimos a datetime a medianoche UTC
    if isinstance(p_dt_input, date) and not isinstance(p_dt_input, datetime):
        dt_utc = datetime(p_dt_input.year, p_dt_input.month, p_dt_input.day, 0, 0, 0, 0, tzinfo=timezone.utc)
    # Si es un objeto datetime, lo convertimos a UTC si es necesario
    elif p_dt_input.tzinfo is None:
        # Si es naive (sin información de zona horaria), asumimos que es UTC.
        dt_utc = p_dt_input.replace(tzinfo=timezone.utc)
    else:
        # Si ya es consciente de la zona horaria, lo convertimos a UTC.
        dt_utc = p_dt_input.astimezone(timezone.utc)

    # Formatear el objeto datetime final al formato 'YYYYMMDDHHMMSS.0Z'
    # strftime para la parte numérica y concatenar ".0Z"
    return dt_utc.strftime("%Y%m%d%H%M%S") + ".0Z"


def ad_format_to_datetime(p_ad_date_str: str) -> datetime:
    """
    Convierte una cadena de fecha/hora en formato 'YYYYMMDDHHMMSS.0Z' (usado en Active Directory)
    a un objeto datetime de Python (timezone-aware y en UTC).

    Args:
        p_ad_date_str (str): La cadena de fecha/hora en formato 'YYYYMMDDHHMMSS.0Z'.

    Returns:
        datetime: Un objeto datetime que representa la fecha y hora en UTC.

    Raises:
        ValueError: Si la cadena de entrada no coincide con el formato esperado.
        TypeError: Si la entrada no es una cadena.
    """
    if not isinstance(p_ad_date_str, str):
        raise TypeError("La entrada debe ser una cadena.")

    # El formato esperado es "YYYYMMDDHHMMSS.0Z"
    # Quitamos ".0Z" y usamos el formato de strptime
    # Aseguramos que termina en ".0Z" para una validación más estricta
    if not p_ad_date_str.endswith(".0Z"):
        raise ValueError(f"Formato de cadena incorrecto. Se esperaba 'YYYYMMDDHHMMSS.0Z'. "
                         f"Recibido: '{p_ad_date_str}'")

    # Quitamos los últimos 3 caracteres (".0Z") para que strptime pueda parsear
    clean_date_str = p_ad_date_str[:-3]

    # Formato de strptime para "YYYYMMDDHHMMSS"
    format_strptime = "%Y%m%d%H%M%S"

    try:
        # Parsear la cadena a un datetime naive
        dt_naive = datetime.strptime(clean_date_str, format_strptime)
        # Asignar la zona horaria UTC
        dt_utc = dt_naive.replace(tzinfo=timezone.utc)
        return dt_utc
    except ValueError:
        # Esto capturaría errores si la parte de la fecha/hora no es válida
        raise ValueError(f"No se pudo parsear la fecha/hora '{p_ad_date_str}'. "
                         f"Asegúrate de que los componentes numéricos sean válidos.")


def datetime_to_unix_timestamp(dt: datetime) -> float:
    """
    Converts a datetime object to its corresponding UNIX timestamp (float).
    The timestamp represents seconds elapsed since the Epoch (January 1, 1970, 00:00:00 UTC).

    Args:
        dt (datetime): The datetime object to convert.

    Returns:
        float: The UNIX timestamp as a floating-point number.

    Raises:
        TypeError: If 'dt' is not a datetime object.

    Example:
        >>> from datetime import datetime, timezone
        >>> # Using a specific date and time (ensuring it's UTC or aware)
        >>> dt_utc = datetime(2025, 6, 11, 10, 27, 5, 0, tzinfo=timezone.utc)
        >>> datetime_to_unix_timestamp(dt_utc)
        1718092025.0

        >>> # Using current date and time (UTC recommended for timestamps)
        >>> import time
        >>> current_dt_utc = datetime.now(timezone.utc)
        >>> current_timestamp = datetime_to_unix_timestamp(current_dt_utc)
        >>> # Compare with time.time() to verify (time.time() returns float seconds since epoch)
        >>> # abs(current_timestamp - time.time()) < 1.0 # Should be True

    **Cost:** O(1), direct timestamp calculation.
    """
    if not isinstance(dt, datetime):
        raise TypeError("'dt' must be a datetime object.")
    
    # The .timestamp() method correctly handles timezones if the datetime is "aware".
    # If it's "naive" (without tzinfo), it assumes system local time.
    return dt.timestamp()


def unix_timestamp_to_datetime(timestamp: Union[int, float], tz_info: Optional[str] = None) -> datetime:
    """
    Converts a UNIX timestamp (seconds since the Epoch) to a datetime object.

    Args:
        timestamp (Union[int, float]): The UNIX timestamp.
        tz_info (Optional[str]): An IANA timezone string (e.g., 'America/New_York', 'Europe/Madrid').
                                 If provided, the resulting datetime will be "aware" (with timezone).
                                 If None, the datetime will be "naive" (without timezone, assuming local).

    Returns:
        datetime: The resulting datetime object.

    Raises:
        TypeError: If 'timestamp' is not an int or float, or if 'tz_info' is not a string.
        zoneinfo.ZoneInfoNotFoundError: If the 'tz_info' string doesn't correspond to a valid timezone.

    Example:
        >>> from datetime import datetime
        >>> # Convert a timestamp to UTC datetime
        >>> unix_timestamp_to_datetime(1718092025.0, tz_info='UTC')
        datetime.datetime(2025, 6, 11, 10, 27, 5, tzinfo=datetime.timezone.utc)

        >>> # Convert to datetime in Madrid timezone
        >>> madrid_dt = unix_timestamp_to_datetime(1718092025.0, tz_info='Europe/Madrid')
        >>> madrid_dt # Note the +02:00 offset for CEST
        datetime.datetime(2025, 6, 11, 12, 27, 5, tzinfo=zoneinfo.ZoneInfo(key='Europe/Madrid'))

        >>> # Convert to naive datetime (local time)
        >>> unix_timestamp_to_datetime(1718092025.0)
        datetime.datetime(2025, 6, 11, 12, 27, 5) # Output assumes local timezone is CEST+2 for this example

    **Cost:** O(1), direct conversion from timestamp to datetime.
    """
    if not isinstance(timestamp, (int, float)):
        raise TypeError("'timestamp' must be an int or float.")
    
    target_tz = None
    if tz_info:
        try:
            target_tz = zoneinfo.ZoneInfo(tz_info)
        except ImportError:
            # Fallback for Python < 3.9 or if zoneinfo is not available
            print("Warning: 'zoneinfo' module not found. Timezone awareness might be limited.")
            from datetime import timedelta, tzinfo
            if tz_info.upper() == 'UTC':
                target_tz = timezone.utc
            else:
                # Basic timezone handling if zoneinfo not available (e.g., fixed offset)
                # This is a simplification; full TZ handling needs zoneinfo/pytz
                raise NotImplementedError("Specific timezone conversion without 'zoneinfo' is not fully implemented. Please install 'zoneinfo' or use Python 3.9+ for full timezone support.")
        except zoneinfo.ZoneInfoNotFoundError:
            raise ValueError(f"Invalid or unknown timezone: '{tz_info}'.")

    if target_tz:
        # fromtimestamp with tz argument available in Python 3.3+
        return datetime.fromtimestamp(timestamp, tz=target_tz)
    else:
        # If no tz_info, return a naive datetime from local timestamp
        return datetime.fromtimestamp(timestamp)
