"""Excel-style date functions.

This module provides Excel-compatible date and time functions for Python.
All functions follow Excel's naming conventions and behaviors, including
Excel's serial number date system (days since December 30, 1899).
"""

from datetime import datetime, timedelta
from typing import Union, Optional, List

from shortfx.fxDate.date_convertions import (
    date_to_excel_serial as _core_date_to_excel_serial,
    time_to_day_fraction as _core_time_to_day_fraction,
)
from shortfx.fxDate.date_operations import (
    add_months as _core_add_months,
    days_360 as _core_days_360,
    days_between as _core_days_between,
    datedif as _core_datedif,
    end_of_month_offset as _core_end_of_month_offset,
    iso_week_number as _core_iso_week_number,
    networkdays as _core_networkdays,
    networkdays_intl as _core_networkdays_intl,
    week_number as _core_week_number,
    workday as _core_workday,
    workday_intl as _core_workday_intl,
    year_fraction as _core_year_fraction,
)


def DAYS(end_date: datetime, start_date: datetime) -> int:
    """Returns the number of days between two dates.
    
    Description:
        Calculates the difference in days between two dates. This is equivalent
        to Excel's DAYS function. The result can be negative if end_date is
        before start_date.
    
    Args:
        end_date (datetime): The end date.
        start_date (datetime): The start date.
    
    Returns:
        int: The number of days between the dates (can be negative).
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import DAYS
        >>> start = datetime(2025, 1, 1)
        >>> end = datetime(2025, 1, 15)
        >>> DAYS(end, start)
        14
        >>> DAYS(start, end)
        -14
    
    Cost: O(1)
    """
    return _core_days_between(start_date, end_date)


def DAYS360(start_date: datetime, end_date: datetime, method: bool = False) -> int:
    """Calculates days between two dates based on a 360-day year.
    
    Description:
        Equivalent to Excel's DAYS360 function. This function calculates the
        number of days between two dates using a 360-day year (12 months of 30 days).
        This is commonly used in financial calculations.
    
    Args:
        start_date (datetime): The start date.
        end_date (datetime): The end date.
        method (bool, optional): False for US method (NASD), True for European method.
                                Defaults to False.
    
    Returns:
        int: Number of days based on 360-day year calculation.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import DAYS360
        >>> start = datetime(2025, 1, 30)
        >>> end = datetime(2025, 2, 28)
        >>> DAYS360(start, end)  # US method
        28
        >>> DAYS360(start, end, method=True)  # European method
        28
    
    Cost: O(1)
    """
    return _core_days_360(start_date, end_date, method='eu' if method else 'us')


def NETWORKDAYS(start_date: datetime, end_date: datetime, holidays: Optional[List[datetime]] = None) -> int:
    """Returns the number of working days between two dates.
    
    Description:
        Equivalent to Excel's NETWORKDAYS function. Calculates the number of
        working days (Monday-Friday) between two dates, excluding weekends
        and optional holidays.
    
    Args:
        start_date (datetime): The start date.
        end_date (datetime): The end date.
        holidays (Optional[List[datetime]], optional): List of holiday dates to exclude.
                                                       Defaults to None.
    
    Returns:
        int: Number of working days.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import NETWORKDAYS
        >>> start = datetime(2025, 1, 6)  # Monday
        >>> end = datetime(2025, 1, 10)   # Friday
        >>> NETWORKDAYS(start, end)
        5
        >>> holidays = [datetime(2025, 1, 8)]
        >>> NETWORKDAYS(start, end, holidays)
        4
    
    Cost: O(n) where n is the number of days between dates
    """
    return _core_networkdays(start_date, end_date, holidays)


def NETWORKDAYS_INTL(start_date: datetime, end_date: datetime, weekend: Union[int, str] = 1, holidays: Optional[List[datetime]] = None) -> int:
    """Returns working days between two dates with custom weekend parameters.
    
    Description:
        Equivalent to Excel's NETWORKDAYS.INTL function. Calculates the number
        of working days between two dates, allowing customization of which days
        are considered weekends.
    
    Args:
        start_date (datetime): The start date.
        end_date (datetime): The end date.
        weekend (Union[int, str], optional): Weekend definition. Int 1-7 for preset patterns,
                                            or string of 0s and 1s where 1=weekend. Defaults to 1.
        holidays (Optional[List[datetime]], optional): List of holiday dates. Defaults to None.
    
    Returns:
        int: Number of working days.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import NETWORKDAYS_INTL
        >>> start = datetime(2025, 1, 6)
        >>> end = datetime(2025, 1, 10)
        >>> NETWORKDAYS_INTL(start, end)  # Standard Sat-Sun weekend
        5
        >>> NETWORKDAYS_INTL(start, end, weekend=2)  # Sun-Mon weekend
        4
    
    Cost: O(n) where n is the number of days between dates
    """
    return _core_networkdays_intl(start_date, end_date, weekend, holidays)


def EDATE(start_date: Union[datetime, float], months: int) -> float:
    """Returns the serial number of a date months before or after.
    
    Description:
        Equivalent to Excel's EDATE function. Returns the Excel serial number
        representing a date that is the indicated number of months before or
        after the start date.
    
    Args:
        start_date (Union[datetime, float]): Starting date as datetime or Excel serial number.
        months (int): Number of months to add (positive) or subtract (negative).
    
    Returns:
        float: Excel serial number of the resulting date.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import EDATE
        >>> start = datetime(2025, 1, 31)
        >>> EDATE(start, 1)  # One month later (Feb 28, 2025)
        45688.0
        >>> EDATE(start, -1)  # One month earlier (Dec 31, 2024)
        45627.0
    
    Cost: O(1)
    """
    if isinstance(start_date, (int, float)):
        start_date = datetime(1899, 12, 30) + timedelta(days=start_date)
    
    result = _core_add_months(start_date, months)
    return _int_date_to_excel_serial(result.year, result.month, result.day)


def EOMONTH(start_date: Union[datetime, float], months: int) -> float:
    """Returns the serial number of the last day of the month.
    
    Description:
        Equivalent to Excel's EOMONTH function. Returns the Excel serial number
        for the last day of the month that is the indicated number of months
        before or after start_date.
    
    Args:
        start_date (Union[datetime, float]): Starting date as datetime or Excel serial number.
        months (int): Number of months to add (positive) or subtract (negative).
    
    Returns:
        float: Excel serial number of the last day of the resulting month.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import EOMONTH
        >>> start = datetime(2025, 1, 15)
        >>> EOMONTH(start, 0)  # Last day of January 2025
        45658.0
        >>> EOMONTH(start, 1)  # Last day of February 2025
        45686.0
    
    Cost: O(1)
    """
    if isinstance(start_date, (int, float)):
        start_date = datetime(1899, 12, 30) + timedelta(days=start_date)
    
    result = _core_end_of_month_offset(start_date, months)
    
    return _int_date_to_excel_serial(result.year, result.month, result.day)


def YEARFRAC(start_date: datetime, end_date: datetime, basis: int = 0) -> float:
    """Returns the fraction of year between two dates.
    
    Description:
        Equivalent to Excel's YEARFRAC function. Calculates the fraction of the
        year represented by the number of whole days between two dates.
    
    Args:
        start_date (datetime): The start date.
        end_date (datetime): The end date.
        basis (int, optional): Day count basis to use (0=US 30/360, 1=Actual/Actual).
                              Defaults to 0.
    
    Returns:
        float: Fraction of year between the dates.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import YEARFRAC
        >>> start = datetime(2025, 1, 1)
        >>> end = datetime(2025, 7, 1)
        >>> YEARFRAC(start, end, basis=0)  # US 30/360
        0.5
        >>> YEARFRAC(start, end, basis=1)  # Actual/Actual
        0.4958904109589041
    
    Cost: O(1)
    """
    return _core_year_fraction(start_date, end_date, basis)


def ISOWEEKNUM(date: datetime) -> int:
    """Returns the ISO week number.
    
    Description:
        Equivalent to Excel's ISOWEEKNUM function. Returns the ISO week number
        of the year for a given date (1-53).
    
    Args:
        date (datetime): The date to evaluate.
    
    Returns:
        int: ISO week number (1-53).
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import ISOWEEKNUM
        >>> ISOWEEKNUM(datetime(2025, 1, 1))
        1
        >>> ISOWEEKNUM(datetime(2025, 6, 15))
        24
    
    Cost: O(1)
    """
    return _core_iso_week_number(date)


def DATEDIF(start_date: datetime, end_date: datetime, unit: str) -> int:
    """Calculates the difference between dates in various units.
    
    Description:
        Equivalent to Excel's DATEDIF function. Calculates the difference between
        two dates in complete years, months, days, or partial combinations.
    
    Args:
        start_date (datetime): The start date.
        end_date (datetime): The end date.
        unit (str): Unit to return:
            - ``'Y'``  — complete years between the dates.
            - ``'M'``  — complete months between the dates.
            - ``'D'``  — total days between the dates.
            - ``'MD'`` — days difference ignoring months and years.
            - ``'YM'`` — months difference ignoring years.
            - ``'YD'`` — days difference ignoring years.
    
    Returns:
        int: The difference in the specified unit.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import DATEDIF
        >>> start = datetime(2020, 1, 15)
        >>> end = datetime(2025, 3, 20)
        >>> DATEDIF(start, end, "Y")
        5
        >>> DATEDIF(start, end, "MD")
        5
        >>> DATEDIF(start, end, "YM")
        2
        >>> DATEDIF(start, end, "YD")
        64
    
    Cost: O(1)
    """
    return _core_datedif(start_date, end_date, unit)


def TIMEVALUE(time_text: str) -> float:
    """Converts a time in text format to a serial number.
    
    Description:
        Equivalent to Excel's TIMEVALUE function. Converts a time represented
        as text into an Excel serial number (fraction of a 24-hour day).
    
    Args:
        time_text (str): Time in "HH:MM:SS" format.
    
    Returns:
        float: Excel serial number representing the time.
    
    Usage Example:
        >>> from shortfx.fxExcel.date_formulas import TIMEVALUE
        >>> TIMEVALUE("12:00:00")  # Noon
        0.5
        >>> TIMEVALUE("18:30:00")  # 6:30 PM
        0.7708333333333334
    
    Cost: O(1)
    """
    return _core_time_to_day_fraction(time_text)


def WEEKNUM(serial_number: Union[float, datetime], return_type: int = 1) -> int:
    """Converts a serial number to a week number.
    
    Description:
        Equivalent to Excel's WEEKNUM function. Returns the week number for a
        date. The week number indicates where the week falls numerically within a year.
    
    Args:
        serial_number (Union[float, datetime]): Date as Excel serial number or datetime.
        return_type (int, optional): System to use (1=week starts Sunday, 21=ISO week).
                                    Defaults to 1.
    
    Returns:
        int: Week number of the year.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxExcel.date_formulas import WEEKNUM
        >>> WEEKNUM(datetime(2025, 1, 1), return_type=1)
        1
        >>> WEEKNUM(datetime(2025, 1, 1), return_type=21)
        1
    
    Cost: O(1)
    """
    if isinstance(serial_number, float):
        dt = datetime(1899, 12, 30) + timedelta(days=serial_number)
    else:
        dt = serial_number

    return _core_week_number(dt, system=21 if return_type == 21 else 1)


def WORKDAY(start_date: Union[float, datetime], days: int, holidays: Optional[List[datetime]] = None) -> float:
    """Returns the date after a number of working days.
    
    Description:
        Equivalent to Excel's WORKDAY function. Returns the Excel serial number
        of the date before or after a specified number of working days.
    
    Args:
        start_date (Union[float, datetime]): Starting date.
        days (int): Number of working days (positive for future, negative for past).
        holidays (Optional[List[datetime]], optional): List of holiday dates to exclude.
                                                       Defaults to None.
    
    Returns:
        float: Excel serial number of the resulting date.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxDate.date_excel import WORKDAY
        >>> start = datetime(2025, 1, 6)  # Monday
        >>> WORKDAY(start, 5)  # 5 working days later
        45662.0
        >>> WORKDAY(start, -5)  # 5 working days earlier
        45652.0
    
    Cost: O(n) where n is the number of days
    """
    return _core_workday(start_date, days, holidays)


def WORKDAY_INTL(start_date: Union[float, datetime], days: int, weekend: Union[int, str] = 1, holidays: Optional[List[datetime]] = None) -> float:
    """Returns the date after working days with custom weekend.
    
    Description:
        Equivalent to Excel's WORKDAY.INTL function. Returns the Excel serial number
        of the date before or after a specified number of working days with custom
        weekend parameters.
    
    Args:
        start_date (Union[float, datetime]): Starting date.
        days (int): Number of working days to add or subtract.
        weekend (Union[int, str], optional): Weekend definition. Defaults to 1 (Sat-Sun).
        holidays (Optional[List[datetime]], optional): List of holiday dates. Defaults to None.
    
    Returns:
        float: Excel serial number of the resulting date.
    
    Usage Example:
        >>> from datetime import datetime
        >>> from shortfx.fxDate.date_excel import WORKDAY_INTL
        >>> start = datetime(2025, 1, 6)  # Monday
        >>> WORKDAY_INTL(start, 5)  # 5 working days later
        45662.0
        >>> WORKDAY_INTL(start, 5, weekend=2)  # With Sun-Mon weekend
        45663.0
    
    Cost: O(n) where n is the number of days
    """
    return _core_workday_intl(start_date, days, weekend, holidays)


def _excel_serial_to_year(serial_number: Union[float, datetime]) -> int:
    """Extracts the year from an Excel-style serial number or a datetime object.
    equivalent to Excel's YEAR function.

    This function is equivalent to Excel's YEAR function. It takes a date
    represented as an Excel serial number (number of days since December 30, 1899)
    or a standard Python datetime object, and returns the corresponding year.

    Args:
        serial_number (Union[float, datetime]): The date value, either as an
                                                  Excel serial number (float) or
                                                  a datetime object.

    Returns:
        int: The year as an integer.

    Raises:
        TypeError: If 'serial_number' is not a float or a datetime object.

    Example:
        >>> _excel_serial_to_year(44361.0) # Represents June 15, 2021
        2021
        >>> _excel_serial_to_year(datetime(2023, 10, 26))
        2023
    
    Cost: O(1)
    """
    # Convert Excel serial numbers to a datetime object.
    # Excel's date system effectively starts from December 30, 1899.
    if isinstance(serial_number, float):
        date_object = datetime(1899, 12, 30) + timedelta(days=serial_number)
    elif isinstance(serial_number, datetime):
        date_object = serial_number
    else:
        # Ensure that the input type is valid to prevent unexpected errors later.
        raise TypeError("Input 'serial_number' must be a float or a datetime object.")

    # Return the year component of the datetime object.
    return date_object.year


def _excel_serial_to_month(serial_number: Union[float, datetime]) -> int:
    """Extracts the month from an Excel-style serial number or a datetime object.
    Equivalent to Excel's MONTH function.

    This function takes a date value, represented either as an Excel serial number
    (a float where the integer part denotes days since December 30, 1899) or a
    standard Python datetime object, and returns the corresponding month.

    Args:
        serial_number (Union[float, datetime]): The date value, either as an
                                                  Excel serial number (float) or
                                                  a datetime object.

    Returns:
        int: The month (1-12) as an integer.

    Raises:
        TypeError: If 'serial_number' is not a float or a datetime object.

    Example:
        >>> # Assuming serial_number 44361.0 corresponds to June 15, 2021
        >>> _excel_serial_to_month(44361.0)
        6
        >>> _excel_serial_to_month(datetime(2023, 10, 26))
        10
    
    Cost: O(1)
    """
    # Convert Excel serial numbers to a datetime object.
    # Excel's date system effectively starts from December 30, 1899.
    if isinstance(serial_number, float):
        date_object = datetime(1899, 12, 30) + timedelta(days=serial_number)
    elif isinstance(serial_number, datetime):
        date_object = serial_number
    else:
        # Raise an error for invalid input types, ensuring robust behavior.
        raise TypeError("Input 'serial_number' must be a float or a datetime object.")

    # Return the month component of the datetime object.
    return date_object.month


def _excel_serial_to_weekday(serial_number: Union[float, datetime], return_type: int = 1) -> int:
    """Converts a serial number or datetime object to the day of the week.
    Equivalent to Excel's WEEKDAY function.

    This function is equivalent to Excel's WEEKDAY function, returning an
    integer representing the day of the week. The behavior changes based on
    the `return_type` argument, mimicking Excel's options:

    - `return_type = 1` (default): Sunday = 1, Monday = 2, ..., Saturday = 7.
      (Excel's default)
    - `return_type = 2`: Monday = 1, Tuesday = 2, ..., Saturday = 6, Sunday = 7.
    - `return_type = 3`: Monday = 0, Tuesday = 1, ..., Saturday = 5, Sunday = 6.

    Args:
        serial_number (Union[float, datetime]): The date value, either as an
                                                  Excel serial number (float) or
                                                  a datetime object.
        return_type (int, optional): An integer specifying the return type.
                                      Defaults to 1. Valid values are 1, 2, or 3.

    Returns:
        int: The day of the week as an integer based on the `return_type`.

    Raises:
        TypeError: If 'serial_number' is not a float or a datetime object.
        ValueError: If 'return_type' is not 1, 2, or 3.

    Example:
        >>> # Assuming serial_number 44361.0 corresponds to Tuesday, June 15, 2021
        >>> _excel_serial_to_weekday(44361.0, return_type=1)
        3
        >>> _excel_serial_to_weekday(datetime(2023, 10, 26), return_type=2) # 2023-10-26 was a Thursday
        4
        >>> _excel_serial_to_weekday(datetime(2023, 10, 29), return_type=3) # 2023-10-29 was a Sunday
        6
    
    Cost: O(1)
    """
    # Convert Excel serial numbers to a datetime object.
    # Excel's date system effectively starts from December 30, 1899.
    if isinstance(serial_number, float):
        date_object = datetime(1899, 12, 30) + timedelta(days=serial_number)
    elif isinstance(serial_number, datetime):
        date_object = serial_number
    else:
        # Raise an error for invalid input types, ensuring robust behavior.
        raise TypeError("Input 'serial_number' must be a float or a datetime object.")

    # Get the weekday (Monday=0, Sunday=6) from the datetime object.
    # This is Python's default representation for weekday.
    weekday_index = date_object.weekday()

    # Adjust the weekday based on the specified return_type, mirroring Excel's behavior.
    if return_type == 1:
        # Excel Type 1: Sunday (0) = 1, Monday (1) = 2, ..., Saturday (6) = 7
        # Python's weekday_index starts from Monday=0, so add 1 to align.
        return weekday_index + 1
    elif return_type == 2:
        # Excel Type 2: Monday (0) = 1, Tuesday (1) = 2, ..., Sunday (6) = 7
        # If weekday_index is 6 (Sunday), return 7. Otherwise, add 1.
        return weekday_index + 2 if weekday_index < 6 else 1
    elif return_type == 3:
        # Excel Type 3: Monday (0) = 0, Tuesday (1) = 1, ..., Sunday (6) = 6
        # This directly matches Python's default weekday_index.
        return weekday_index
    else:
        # Raise an error for invalid return_type to ensure proper usage.
        raise ValueError("Invalid 'return_type'. Must be 1, 2, or 3.")
    

def _excel_serial_to_day(serial_number: Union[int, float, datetime]) -> int:
    """Converts a serial number or datetime object into the day of the month.
    Equivalent to Excel's DAY function.

    This function is equivalent to the DAY function in Excel, extracting the day
    component from a given date representation. If a serial number (integer or float)
    is provided, it's treated as the number of days since '1899-12-30', which is
    Excel's epoch for date calculations.

    Args:
        serial_number (Union[int, float, datetime]): The date represented as an
                                                      Excel-like serial number
                                                      or a datetime object.

    Returns:
        int: The day of the month (1 to 31) for the given date.

    Raises:
        TypeError: If the input 'serial_number' is not an int, float, or datetime object.

    Example:
        >>> _excel_serial_to_day(44361) # Equivalent to '2021-06-15'
        15
        >>> _excel_serial_to_day(datetime(2023, 10, 26))
        26
    
    Cost: O(1)
    """
    # Convert Excel serial numbers to datetime objects.
    # Excel's epoch is '1899-12-30', so we add the serial number of days to this date.
    if isinstance(serial_number, (int, float)):
        date_object = datetime(1899, 12, 30) + timedelta(days=serial_number)
    elif isinstance(serial_number, datetime):
        date_object = serial_number
    else:
        # Raise an error to ensure type safety and clear usage.
        raise TypeError("Input 'serial_number' must be an int, float, or datetime object.")

    # Extract and return the day component from the datetime object.
    return date_object.day


def _excel_serial_to_hour(serial_number: Union[float, datetime]) -> int:
    """Extracts the hour component from an Excel-style serial number or a datetime object.
    Equivalent to Excel's HOUR function.

    This function takes a date and/or time value, represented either as an
    Excel serial number (a float where the fractional part denotes time) or a
    standard Python datetime object, and returns the corresponding hour (0-23).

    Args:
        serial_number (Union[float, datetime]): The date/time value, either as an
                                                  Excel serial number (float) or
                                                  a datetime object.

    Returns:
        int: The hour (0-23) as an integer.

    Raises:
        TypeError: If 'serial_number' is not a float or a datetime object.

    Example:
        >>> # Assuming serial_number 44361.771354166667 represents 2021-06-15 18:30:45
        >>> _excel_serial_to_hour(44361.771354166667)
        18
        >>> _excel_serial_to_hour(datetime(2023, 10, 26, 9, 15, 30))
        9
    
    Cost: O(1)
    """
    # Convert Excel serial numbers to a datetime object.
    # Excel's date system effectively starts from December 30, 1899.
    if isinstance(serial_number, float):
        date_time_object = datetime(1899, 12, 30) + timedelta(days=serial_number)
    elif isinstance(serial_number, datetime):
        date_time_object = serial_number
    else:
        # Raise an error for invalid input types, ensuring robust behavior.
        raise TypeError("Input 'serial_number' must be a float or a datetime object.")

    # Return the hour component of the datetime object.
    return date_time_object.hour


def _excel_serial_to_minute(serial_number: Union[float, datetime]) -> int:
    """Extracts the minute component from an Excel-style serial number or a datetime object.
    Equivalent to Excel's MINUTE function.

    This function takes a date and/or time value, represented either as an
    Excel serial number (a float where the fractional part denotes time) or a
    standard Python datetime object, and returns the corresponding minute.

    Args:
        serial_number (Union[float, datetime]): The date/time value, either as an
                                                  Excel serial number (float) or
                                                  a datetime object.

    Returns:
        int: The minute (0-59) as an integer.

    Raises:
        TypeError: If 'serial_number' is not a float or a datetime object.

    Example:
        >>> # Assuming serial_number 44361.771354166667 represents 2021-06-15 18:30:45
        >>> _excel_serial_to_minute(44361.771354166667)
        30
        >>> _excel_serial_to_minute(datetime(2023, 10, 26, 15, 45, 10))
        45
    
    Cost: O(1)
    """
    # Convert Excel serial numbers to a datetime object.
    # Excel's date system effectively starts from December 30, 1899.
    if isinstance(serial_number, float):
        date_time_object = datetime(1899, 12, 30) + timedelta(days=serial_number)
    elif isinstance(serial_number, datetime):
        date_time_object = serial_number
    else:
        # Raise an error for invalid input types, ensuring robust behavior.
        raise TypeError("Input 'serial_number' must be a float or a datetime object.")

    # Return the minute component of the datetime object.
    return date_time_object.minute


def _excel_serial_to_second(serial_number: Union[float, datetime]) -> int:
    """Extracts the second component from an Excel-style serial number or a datetime object.
    Equivalent to Excel's SECOND function.

    This function takes a date and/or time value, represented either as an
    Excel serial number (a float where the fractional part denotes time) or a
    standard Python datetime object, and returns the corresponding second.

    Args:
        serial_number (Union[float, datetime]): The date/time value, either as an
                                                  Excel serial number (float) or
                                                  a datetime object.

    Returns:
        int: The second (0-59) as an integer.

    Raises:
        TypeError: If 'serial_number' is not a float or a datetime object.

    Example:
        >>> _excel_serial_to_second(44361.771354166667) # Represents 2021-06-15 18:30:45
        45
        >>> _excel_serial_to_second(datetime(2023, 10, 26, 15, 30, 10))
        10
    
    Cost: O(1)
    """
    # Convert Excel serial numbers to a datetime object.
    # Excel's date system effectively starts from December 30, 1899.
    if isinstance(serial_number, float):
        date_time_object = datetime(1899, 12, 30) + timedelta(days=serial_number)
    elif isinstance(serial_number, datetime):
        date_time_object = serial_number
    else:
        # Ensure the input type is valid to prevent unexpected errors.
        raise TypeError("Input 'serial_number' must be a float or a datetime object.")

    # Return the second component of the datetime object.
    return date_time_object.second


def _int_date_to_excel_serial(year: int, month: int, day: int) -> float:
    """Converts a given date into its Excel serial number equivalent.
    Equivalent to Excel's DATE function.

    This function is analogous to the DATE function in Excel. Excel stores dates
    as serial numbers, representing the number of days since January 1, 1900
    (with an intentional error where 1900 is treated as a leap year, making
    December 30, 1899, the effective epoch for calculations).

    Args:
        year (int): The year of the date (e.g., 2023).
        month (int): The month of the date (1-12).
        day (int): The day of the month (1-31).

    Returns:
        float: The Excel serial number representing the date. This can include
               a fractional part if time components were considered (though this
               function only handles full days).

    Raises:
        ValueError: If the provided year, month, or day form an invalid date.

    Example:
        >>> _int_date_to_excel_serial(2023, 10, 26)
        45227.0
        >>> _int_date_to_excel_serial(1900, 1, 1) # Excel's day 1
        1.0
    
    Cost: O(1)
    """
    # Create a datetime object for the input date.
    # This will automatically raise a ValueError if the date is invalid (e.g., February 30).
    input_date = datetime(year, month, day)

    # Define Excel's epoch date.
    # Excel's date system starts effectively from December 30, 1899, due to how it handles leap years.
    excel_epoch = datetime(1899, 12, 30)

    # Calculate the difference in days.
    # The .days attribute gives the whole number of days.
    # The fractional part accounts for any time component, though here it will be 0
    # since we are only dealing with full days.
    time_difference = input_date - excel_epoch
    serial_number = time_difference.days + time_difference.seconds / 86400.0

    return serial_number


def _date_to_excel_serial(date_input: Union[str, datetime]) -> float:
    """Converts a date, provided as a text string or a datetime object,
    into its Excel serial number equivalent.
    Equivalent to Excel's DATEVALUE function.

    This function is a versatile tool for converting dates into Excel's numerical
    representation. If a string is provided, it must be in the "DD/MM/YYYY" format.
    If a datetime object is provided, it's used directly. The Excel serial number
    represents the number of days since December 30, 1899, which is Excel's
    effective epoch for date calculations.

    Args:
        date_input (Union[str, datetime]): The date value to convert.
                                           Can be a string (e.g., "26/10/2023")
                                           or a datetime object (e.g., datetime(2023, 10, 26)).

    Returns:
        float: The Excel serial number representing the parsed date.

    Raises:
        ValueError: If 'date_input' is a string that does not match the expected
                    "DD/MM/YYYY" format or represents an invalid date.
        TypeError: If 'date_input' is neither a string nor a datetime object.

    Example:
        >>> _date_to_excel_serial("15/06/2021")
        44361.0
        >>> from datetime import datetime
        >>> _date_to_excel_serial(datetime(2023, 10, 26))
        45227.0
        >>> _date_to_excel_serial("01/01/1900") # Excel's day 1
        1.0
    
    Cost: O(1)
    """
    return _core_date_to_excel_serial(date_input)


def _time_to_excel_serial(hour: int, minute: int, second: int) -> float:
    """Converts a given time into its Excel serial number equivalent.
    Equivalent to Excel's TIME function.

    This function is analogous to the TIME function in Excel. It takes
    hours, minutes, and seconds, and returns a serial number that
    represents the fraction of a 24-hour day that has elapsed. For instance,
    6:00 AM would be 0.25, 12:00 PM would be 0.5, and 6:00 PM would be 0.75.

    Args:
        hour (int): The hour component of the time (0-23).
        minute (int): The minute component of the time (0-59).
        second (int): The second component of the time (0-59).

    Returns:
        float: The Excel serial number representing the time as a fraction of a day.

    Raises:
        ValueError: If the provided hour, minute, or second are outside
                    their valid ranges.

    Example:
        >>> _time_to_excel_serial(12, 0, 0) # 12:00 PM
        0.5
        >>> _time_to_excel_serial(6, 0, 0)  # 6:00 AM
        0.25
        >>> _time_to_excel_serial(18, 30, 45) # 6:30:45 PM
        0.7713541666666667
    
    Cost: O(1)
    """
    # Validate input ranges to ensure a meaningful time is being converted.
    if not (0 <= hour <= 23):
        raise ValueError("Hour must be between 0 and 23.")
    if not (0 <= minute <= 59):
        raise ValueError("Minute must be between 0 and 59.")
    if not (0 <= second <= 59):
        raise ValueError("Second must be between 0 and 59.")

    # Calculate the total number of seconds in the given time.
    # We multiply hours by 3600 (seconds in an hour) and minutes by 60 (seconds in a minute).
    total_seconds = (hour * 3600) + (minute * 60) + second

    # Divide by the total number of seconds in a day (24 hours * 60 minutes * 60 seconds)
    # to get the fractional part of the day.
    seconds_in_a_day = 86400.0
    serial_time = total_seconds / seconds_in_a_day

    return serial_time


def _now_to_excel_serial() -> float:
    """Returns the current date and time as an Excel serial number.
    
    Description:
        Equivalent to Excel's NOW function. Combines the current date and time
        and converts it into an Excel-compatible floating-point serial number.
        The integer part represents days since December 30, 1899, and the
        fractional part represents time as a proportion of a 24-hour day.

    Returns:
        float: The current date and time as an Excel serial number.

    Usage Example:
        >>> from shortfx.fxDate.date_excel import _now_to_excel_serial
        >>> # Output varies based on when called
        >>> _now_to_excel_serial()
        45811.88552199074
    
    Cost: O(1)
    """
    current_datetime = datetime.now()
    excel_epoch = datetime(1899, 12, 30)
    time_difference = current_datetime - excel_epoch
    total_seconds_in_day = 86400.0
    excel_serial = time_difference.days + (time_difference.seconds / total_seconds_in_day)
    return excel_serial


# Excel-compatible date/time functions with official names

def DATE(year: int, month: int, day: int) -> float:
    """
    Returns the Excel serial number corresponding to a particular date.
    Excel/Spanish name: FECHA
    
    **Description:**
    Converts a given year, month, and day into an Excel serial number.
    The serial number is the number of days since December 30, 1899.
    
    **Args:**
        year: The year (1900-9999).
        month: The month (1-12).
        day: The day of the month (1-31).
    
    **Returns:**
        float: The Excel serial number representing the date.
    
    **Raises:**
        ValueError: If the date values are invalid.
    
    **Usage Example:**
        >>> DATE(2025, 1, 15)
        45667.0
        >>> DATE(2024, 12, 31)
        45657.0
    
    **Cost:** O(1)
    """
    return _int_date_to_excel_serial(year, month, day)


def DATEVALUE(date_text: str) -> float:
    """
    Converts a date in text format to an Excel serial number.
    Excel/Spanish name: FECHANUMERO
    
    **Description:**
    Converts a text representation of a date into an Excel serial number.
    Accepts dates in DD/MM/YYYY format.
    
    **Args:**
        date_text: A date string in DD/MM/YYYY format.
    
    **Returns:**
        float: The Excel serial number representing the date.
    
    **Raises:**
        ValueError: If the date format is invalid.
    
    **Usage Example:**
        >>> DATEVALUE("15/01/2025")
        45667.0
        >>> DATEVALUE("31/12/2024")
        45657.0
    
    **Cost:** O(1)
    """
    return _date_to_excel_serial(date_text)


def DAY(serial_number: Union[float, datetime]) -> int:
    """
    Converts an Excel serial number to a day of the month.
    Excel/Spanish name: DAY (DIA in Spanish contexts)
    
    **Description:**
    Extracts the day component (1-31) from an Excel serial number or datetime object.
    
    **Args:**
        serial_number: An Excel serial number or datetime object.
    
    **Returns:**
        int: The day of the month (1-31).
    
    **Raises:**
        ValueError: If the serial number is invalid.
    
    **Usage Example:**
        >>> from datetime import datetime
        >>> DAY(45667.0)  # January 15, 2025
        15
        >>> DAY(datetime(2025, 1, 15))
        15
    
    **Cost:** O(1)
    """
    return _excel_serial_to_day(serial_number)


def HOUR(serial_number: Union[float, datetime]) -> int:
    """
    Converts an Excel serial number to an hour value.
    Excel/Spanish name: HOUR (HORA as function name in Spanish)
    
    **Description:**
    Extracts the hour component (0-23) from an Excel serial number or datetime object.
    
    **Args:**
        serial_number: An Excel serial number or datetime object.
    
    **Returns:**
        int: The hour (0-23).
    
    **Raises:**
        ValueError: If the serial number is invalid.
    
    **Usage Example:**
        >>> HOUR(0.5)  # 12:00 PM
        12
        >>> HOUR(0.75)  # 6:00 PM
        18
    
    **Cost:** O(1)
    """
    return _excel_serial_to_hour(serial_number)


def MINUTE(serial_number: Union[float, datetime]) -> int:
    """
    Converts an Excel serial number to a minute value.
    Excel/Spanish name: MINUTE (MINUTO in Spanish)
    
    **Description:**
    Extracts the minute component (0-59) from an Excel serial number or datetime object.
    
    **Args:**
        serial_number: An Excel serial number or datetime object.
    
    **Returns:**
        int: The minute (0-59).
    
    **Raises:**
        ValueError: If the serial number is invalid.
    
    **Usage Example:**
        >>> from datetime import datetime
        >>> MINUTE(datetime(2025, 1, 15, 14, 30))
        30
        >>> MINUTE(0.604166667)  # Approximately 2:30 PM
        30
    
    **Cost:** O(1)
    """
    return _excel_serial_to_minute(serial_number)


def MONTH(serial_number: Union[float, datetime]) -> int:
    """
    Converts an Excel serial number to a month value.
    Excel/Spanish name: MONTH (MES in Spanish)
    
    **Description:**
    Extracts the month component (1-12) from an Excel serial number or datetime object.
    
    **Args:**
        serial_number: An Excel serial number or datetime object.
    
    **Returns:**
        int: The month (1-12).
    
    **Raises:**
        ValueError: If the serial number is invalid.
    
    **Usage Example:**
        >>> from datetime import datetime
        >>> MONTH(45667.0)  # January 15, 2025
        1
        >>> MONTH(datetime(2025, 6, 15))
        6
    
    **Cost:** O(1)
    """
    return _excel_serial_to_month(serial_number)


def SECOND(serial_number: Union[float, datetime]) -> int:
    """
    Converts an Excel serial number to a second value.
    Excel/Spanish name: SECOND (SEGUNDO in Spanish)
    
    **Description:**
    Extracts the second component (0-59) from an Excel serial number or datetime object.
    
    **Args:**
        serial_number: An Excel serial number or datetime object.
    
    **Returns:**
        int: The second (0-59).
    
    **Raises:**
        ValueError: If the serial number is invalid.
    
    **Usage Example:**
        >>> from datetime import datetime
        >>> SECOND(datetime(2025, 1, 15, 14, 30, 45))
        45
        >>> SECOND(0.604224537)  # Approximately 2:30:05 PM
        5
    
    **Cost:** O(1)
    """
    return _excel_serial_to_second(serial_number)


def TIME(hour: int, minute: int, second: int) -> float:
    """
    Returns the Excel serial number for a particular time.
    Excel/Spanish name: HORA (as noun in Spanish)
    
    **Description:**
    Converts hours, minutes, and seconds into an Excel serial number representing
    the time as a fraction of a day.
    
    **Args:**
        hour: The hour (0-23).
        minute: The minute (0-59).
        second: The second (0-59).
    
    **Returns:**
        float: The Excel serial number representing the time (fraction of a day).
    
    **Raises:**
        ValueError: If hour, minute, or second are out of range.
    
    **Usage Example:**
        >>> TIME(12, 0, 0)  # 12:00 PM
        0.5
        >>> TIME(6, 0, 0)  # 6:00 AM
        0.25
        >>> TIME(18, 30, 0)  # 6:30 PM
        0.7708333333333334
    
    **Cost:** O(1)
    """
    return _time_to_excel_serial(hour, minute, second)


def TODAY() -> float:
    """
    Returns the Excel serial number of the current date.
    Excel/Spanish name: HOY
    
    **Description:**
    Returns the current date as an Excel serial number (integer part only, no time).
    
    **Returns:**
        float: The Excel serial number representing today's date.
    
    **Raises:**
        None
    
    **Usage Example:**
        >>> # Output depends on current date
        >>> TODAY()  # e.g., 45667.0 for January 15, 2025
        45667.0
    
    **Cost:** O(1)
    """
    today = datetime.now().date()
    return _int_date_to_excel_serial(today.year, today.month, today.day)


def NOW() -> float:
    """
    Returns the Excel serial number of the current date and time.
    Excel/Spanish name: AHORA
    
    **Description:**
    Returns the current date and time as an Excel serial number.
    Integer part is the date, fractional part is the time.
    
    **Returns:**
        float: The Excel serial number representing the current date and time.
    
    **Raises:**
        None
    
    **Usage Example:**
        >>> # Output depends on current date and time
        >>> NOW()  # e.g., 45667.625 for January 15, 2025, 3:00 PM
        45667.625
    
    **Cost:** O(1)
    """
    return _now_to_excel_serial()


def WEEKDAY(serial_number: Union[float, datetime], return_type: int = 1) -> int:
    """
    Converts an Excel serial number to a day of the week.
    Excel/Spanish name: DIASEM
    
    **Description:**
    Returns the day of the week for a given date. The return_type parameter
    determines how the week is numbered (1-7 or 0-6).
    
    **Args:**
        serial_number: An Excel serial number or datetime object.
        return_type: Determines the week numbering system:
            - 1 (default): Sunday=1 through Saturday=7
            - 2: Monday=1 through Sunday=7
            - 3: Monday=0 through Sunday=6
    
    **Returns:**
        int: The day of the week according to the return_type.
    
    **Raises:**
        ValueError: If return_type is not 1, 2, or 3.
    
    **Usage Example:**
        >>> from datetime import datetime
        >>> # January 15, 2025 is a Wednesday
        >>> WEEKDAY(datetime(2025, 1, 15))  # Wednesday with Sunday=1
        4
        >>> WEEKDAY(datetime(2025, 1, 15), 2)  # Wednesday with Monday=1
        3
        >>> WEEKDAY(datetime(2025, 1, 15), 3)  # Wednesday with Monday=0
        2
    
    **Cost:** O(1)
    """
    return _excel_serial_to_weekday(serial_number, return_type)


def YEAR(serial_number: Union[float, datetime]) -> int:
    """
    Converts an Excel serial number to a year value.
    Excel/Spanish name: YEAR (AÑO in Spanish)
    
    **Description:**
    Extracts the year component from an Excel serial number or datetime object.
    
    **Args:**
        serial_number: An Excel serial number or datetime object.
    
    **Returns:**
        int: The year (e.g., 2025).
    
    **Raises:**
        ValueError: If the serial number is invalid.
    
    **Usage Example:**
        >>> from datetime import datetime
        >>> YEAR(45667.0)  # January 15, 2025
        2025
        >>> YEAR(datetime(2024, 12, 31))
        2024
    
    **Cost:** O(1)
    """
    return _excel_serial_to_year(serial_number)

