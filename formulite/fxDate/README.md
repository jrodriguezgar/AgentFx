# FormuLite - fxDate Module

Documentation of the available functions in the `fxDate` module of FormuLite.

## Overview

The fxDate module provides comprehensive date and time manipulation functions for FormuLite, including:
- **Date Conversions**: Format transformations, timezone handling, Julian dates
- **System Functions**: Current date/time queries
- **Date Operations**: Calculations, validations, business day logic
- **Evaluations**: Type checking

## Module Structure

- **date_convertions.py**: Functions for converting between date formats and types
- **date_evaluations.py**: Functions for validating and checking date properties
- **date_operations.py**: Functions for date arithmetic and manipulation
- **date_sys.py**: System-level date and time functions

---

## Table of Contents

- [Function Categories](#function-categories)
  - [Date Conversions](#date-conversions)
  - [System Functions](#system-functions)
  - [Date Operations](#date-operations)
  - [Evaluations](#evaluations)
- [Function Index](#function-index)
- [Credits](#credits)

---

## Function Categories

### Date Conversions
- [datetime_to_date()](#datetime_to_date) - Converts datetime object to date object, discarding time components
- [date_to_string()](#date_to_string) - Converts datetime object into a formatted string
- [datetime_to_integer()](#datetime_to_integer) - Converts date to integer in YYYYMMDD format, ignoring time
- [datetime_to_timestamp()](#datetime_to_timestamp) - Converts datetime object to Unix timestamp
- [timestamp_to_datetime()](#timestamp_to_datetime) - Converts Unix timestamp back to datetime object
- [date_to_iso_format()](#date_to_iso_format) - Converts datetime object to ISO 8601 formatted string
- [from_iso_to_local_datetime()](#from_iso_to_local_datetime) - Converts ISO 8601 string to datetime in local timezone
- [list_available_timezones()](#list_available_timezones) - Retrieves sorted list of all available IANA timezone names
- [convert_timezone()](#convert_timezone) - Converts timezone-aware datetime from current to target timezone
- [utc_to_datetime()](#utc_to_datetime) - Converts any datetime or date string to UTC representation
- [utc_to_timezone()](#utc_to_timezone) - Localizes naive datetime or converts aware datetime to target timezone
- [date_to_julian()](#date_to_julian) - Converts standard date to Julian date representation (day of year)
- [julian_to_date()](#julian_to_date) - Converts Julian date (day of year) to standard datetime object
- [datetime_to_milliseconds_timestamp()](#datetime_to_milliseconds_timestamp) - Converts datetime object to Unix timestamp in milliseconds
- [milliseconds_timestamp_to_datetime()](#milliseconds_timestamp_to_datetime) - Converts Unix timestamp in milliseconds to datetime object
- [utc_to_midnight_iso()](#utc_to_midnight_iso) - Converts datetime to equivalent at midnight UTC
- [filetime_to_datetime()](#filetime_to_datetime) - Converts Windows FILETIME value to datetime object and string
- [datetime_to_filetime()](#datetime_to_filetime) - Converts Python datetime or date to Windows FILETIME value
- [datetime_to_ad_format()](#datetime_to_ad_format) - Converts datetime or date to Active Directory format string
- [ad_format_to_datetime()](#ad_format_to_datetime) - Converts Active Directory format string to Python datetime object
- [unix_timestamp_to_datetime()](#unix_timestamp_to_datetime) - Converts UNIX timestamp to datetime object with optional timezone
- [integer_to_datetime()](#integer_to_datetime) - Converts YYYYMMDD integer back to datetime object
- [date_to_excel_serial()](#date_to_excel_serial) - Date to Excel serial number (days since 1899-12-30)
- [excel_serial_to_date()](#excel_serial_to_date) - Excel serial number to date object
- [datetime_to_cron()](#datetime_to_cron) - Datetime to cron expression (minute hour day month weekday)
- [datetime_to_rfc2822()](#datetime_to_rfc2822) - Datetime to RFC 2822 email format string
- [rfc2822_to_datetime()](#rfc2822_to_datetime) - Parse RFC 2822 string to datetime
- [parse_date_flexible()](#parse_date_flexible) - Parses a date string by trying multiple common formats
- [date_to_human_short()](#date_to_human_short) - Formats a date as a short human-readable string
- [datetime_to_iso8601()](#datetime_to_iso8601) - Converts date/datetime to ISO 8601 string
- [iso8601_to_datetime()](#iso8601_to_datetime) - Parses ISO 8601 string to date/datetime
- [date_to_iso_week_date()](#date_to_iso_week_date) - Date to ISO 8601 week date string (YYYY-Www-D)
- [iso_week_date_to_date()](#iso_week_date_to_date) - Parse ISO week date string to date object

### System Functions
- [current_datetime()](#current_datetime) - Gets current local date and time
- [current_date()](#current_date) - Gets current local date without time component
- [current_time()](#current_time) - Gets current local time without date component
- [current_year()](#current_year) - Gets current year as integer
- [current_month()](#current_month) - Gets current month (1-12)
- [current_day()](#current_day) - Gets current day of month (1-31)
- [current_weekday_number()](#current_weekday_number) - Gets current weekday number with European or US convention
- [current_weekday_name()](#current_weekday_name) - Gets name of current weekday in specified language
- [current_last_day_of_month()](#current_last_day_of_month) - Gets last day of current month
- [current_last_friday_of_month()](#current_last_friday_of_month) - Gets last Friday of current month
- [current_next_friday()](#current_next_friday) - Gets next Friday after current date
- [current_previous_friday()](#current_previous_friday) - Gets previous Friday before current date
- [current_is_working_day()](#current_is_working_day) - Checks if current date is working day (Monday-Friday)
- [current_is_weekend()](#current_is_weekend) - Checks if current date is weekend (Saturday/Sunday)
- [get_local_now()](#get_local_now) - Gets current date/time localized to specified timezone
- [seconds_since_midnight()](#seconds_since_midnight) - Returns seconds elapsed since midnight of current day
- [current_quarter()](#current_quarter) - Returns current quarter of the year (1-4)
- [current_week_number()](#current_week_number) - Returns current ISO week number (1-53)
- [current_month_name()](#current_month_name) - Returns name of current month in specified language
- [current_first_day_of_month()](#current_first_day_of_month) - Returns first day of current month at midnight
- [current_is_leap_year()](#current_is_leap_year) - Checks if current year is a leap year
- [current_days_in_month()](#current_days_in_month) - Returns number of days in current month
- [current_season()](#current_season) - Returns current season of the year

### Date Operations
- [is_date_type()](#is_date_type) - Checks if object is date type (date, datetime, time)
- [is_valid_date()](#is_valid_date) - Validates if input parameter is valid date
- [weekday_number()](#weekday_number) - Gets day of week as number for given date
- [weekday_name()](#weekday_name) - Gets name of weekday for given date in language
- [first_day_of_week()](#first_day_of_week) - Calculates first day of week for given date
- [last_day_of_week()](#last_day_of_week) - Calculates last day of week for given date
- [month_name()](#month_name) - Gets name of month for given date in language
- [months_between_dates()](#months_between_dates) - Calculates number of complete months between two dates
- [days_in_month()](#days_in_month) - Returns number of days in given month and year
- [calculate_days_between_dates()](#calculate_days_between_dates) - Calculates absolute number of days between two dates
- [get_nth_weekday_of_month()](#get_nth_weekday_of_month) - Calculates date of n-th occurrence of specific weekday
- [add_days_from_now()](#add_days_from_now) - Adds or subtracts days from current date and time
- [add_time_to_date()](#add_time_to_date) - Adds or subtracts specified quantity of time to/from date
- [time_difference()](#time_difference) - Calculates difference between two dates in specified unit
 - [diff_time()](#diff_time) - Whole-unit difference between two dates (supported units)
- [date_part()](#date_part) - Extracts specific part from date/time, similar to VBA DatePart
- [parts_to_date()](#parts_to_date) - Creates date object from year, month, day components
- [parts_to_datetime()](#parts_to_datetime) - Creates datetime object from numeric components
- [is_between_dates()](#is_between_dates) - Checks if date falls within date range
- [is_valid_time()](#is_valid_time) - Verifies if hour, minute, second, microsecond represent valid time
- [time_from_datetime()](#time_from_datetime) - Extracts time component from datetime object
- [get_date_component()](#get_date_component) - Extracts specific component (day, month, year, etc.) from date
- [set_date_component()](#set_date_component) - Returns new datetime with specified components modified
- [is_leap_year()](#is_leap_year) - Checks if given year is leap year
- [get_number_of_days_in_year()](#get_number_of_days_in_year) - Calculates total number of days in given year
- [get_week_range()](#get_week_range) - Retrieves start and end dates for specific ISO week
- [get_year_calendar_by_weeks()](#get_year_calendar_by_weeks) - Generates complete list of ISO weeks for year
- [get_quarter()](#get_quarter) - Extracts quarter number (1-4) from date
- [get_number_of_days_in_quarter()](#get_number_of_days_in_quarter) - Calculates total days in specific quarter of year
- [start_of_month()](#start_of_month) - Returns first day of month for given date
- [end_of_month()](#end_of_month) - Returns last day of month for given date
- [start_of_year()](#start_of_year) - Returns first day of year for given date
- [end_of_year()](#end_of_year) - Returns last day of year for given date
- [get_last_friday_of_month()](#get_last_friday_of_month) - Calculates last Friday of given month
- [get_next_friday()](#get_next_friday) - Calculates next upcoming Friday from given date
- [get_previous_friday()](#get_previous_friday) - Calculates immediately preceding Friday from given date
- [next_weekday()](#next_weekday) - Returns next occurrence of a specific weekday after a given date
- [previous_weekday()](#previous_weekday) - Returns most recent occurrence of a specific weekday before a given date
- [last_weekday_of_month()](#last_weekday_of_month) - Returns last occurrence of a specific weekday in the month
- [last_day_of_month()](#last_day_of_month) - Returns last day of the month for a given date (alias for end_of_month)
- [add_years()](#add_years) - Shifts a date forward or backward by a given number of years
- [get_working_days_in_range()](#get_working_days_in_range) - Calculates working days (excluding weekends/holidays) within date range
- [get_first_business_day_of_month()](#get_first_business_day_of_month) - Returns first working day of month
- [get_last_business_day_of_month()](#get_last_business_day_of_month) - Returns last working day of month
- [is_working_day()](#is_working_day) - Checks if date is working day (Monday-Friday)
- [is_weekend()](#is_weekend) - Determines if date is Saturday or Sunday
- [get_age_from_dob()](#get_age_from_dob) - Calculates age in full years from date of birth
- [get_season()](#get_season) - Returns season of year for given date
- [format_datetime_ampm()](#format_datetime_ampm) - Formats datetime into 12-hour (AM/PM) string representation
- [timedelta_to_components()](#timedelta_to_components) - Converts timedelta object into dictionary of its components
- [intersection_of_date_ranges()](#intersection_of_date_ranges) - Returns intersection period if two date ranges overlap
- [dates_between()](#dates_between) - Generates list of all dates between two dates, inclusive
- [date_intervals()](#date_intervals) - Generates list of date intervals for specific granularity
- [add_microseconds()](#add_microseconds) - Adds or subtracts microseconds to/from datetime
- [set_microseconds()](#set_microseconds) - Sets microseconds of datetime to specific value
- [is_duration_less_than()](#is_duration_less_than) - Checks if duration between dates is less than threshold
- [is_duration_greater_than()](#is_duration_greater_than) - Checks if duration between dates is greater than threshold
- [full_years_between()](#full_years_between) - Returns number of complete years between two dates
- [full_months_between()](#full_months_between) - Returns number of complete months between two dates
- [generate_random_date()](#generate_random_date) - Generates random date within specified range
- [generate_random_time()](#generate_random_time) - Generates random time within optional range
- [generate_random_datetime()](#generate_random_datetime) - Generates random datetime within range, optionally localized
- [get_week_of_year()](#get_week_of_year) - Returns ISO week number of year for date
- [week_of_month()](#week_of_month) - Returns week number of month for given date
- [filter_dates_by_weekday()](#filter_dates_by_weekday) - Filters list of dates, returning only specific weekday
- [days_360()](#days_360) - Calculates days between two dates based on 360-day year
- [network_days_intl()](#network_days_intl) - Calculates working days between dates with custom weekend definition
- [networkdays()](#networkdays) - Working days between dates excluding weekends/holidays (NETWORKDAYS)
- [workday()](#workday) - Returns date after a given number of working days (Mon-Fri)
- [workday_intl()](#workday_intl) - Returns date after working days with custom weekend definition
- [year_fraction()](#year_fraction) - Calculates fraction of year between two dates
- [week_number()](#week_number) - Returns week number of year for a given date
- [iso_week_number()](#iso_week_number) - Returns ISO 8601 week number for a given date
- [datedif()](#datedif) - Date difference in Y/M/D/YM/MD/YD units (DATEDIF)
- [quarters_between_dates()](#quarters_between_dates) - Calculates complete quarters between two dates
- [add_months()](#add_months) - Shifts a date forward or backward by months
- [end_of_month_offset()](#end_of_month_offset) - Returns last day of month N months from date
- [start_of_quarter()](#start_of_quarter) - Returns first day of the quarter for a given date
- [end_of_quarter()](#end_of_quarter) - Returns last day of the quarter for a given date
- [next_business_day()](#next_business_day) - Returns next working day (Mon-Fri) after a given date
- [previous_business_day()](#previous_business_day) - Returns previous working day (Mon-Fri) before a given date
- [date_range()](#date_range) - Generates list of dates between start and end at regular intervals
- [easter_date()](#easter_date) - Computes Easter Sunday date for a given year
- [age()](#age) - Calculates age in complete years from a birth date
- [overlap_dates()](#overlap_dates) - Checks whether two date ranges overlap
- [human_readable_duration()](#human_readable_duration) - Seconds to human-readable string (e.g. "2h 30m 15s")
- [relative_time()](#relative_time) - Human-friendly relative time (e.g. "3 hours ago", en/es)
- [overlap_days()](#overlap_days) - Count overlapping days between two date ranges
- [is_same_business_day()](#is_same_business_day) - Check if two datetimes fall on the same business day
- [snap_to_weekday()](#snap_to_weekday) - Snap date to nearest/next/previous given weekday
- [relative_time_description()](#relative_time_description) - Returns a human-readable relative time string
- [round_datetime()](#round_datetime) - Rounds a datetime to the nearest unit
- [recurring_dates()](#recurring_dates) - Generates recurring dates within a range
- [business_hours_between()](#business_hours_between) - Calculates business hours between two datetimes

### Evaluations
- [is_dateclass()](#is_dateclass) - Checks if object is of datetime type
- [is_past()](#is_past) - Checks if a date is strictly in the past
- [is_future()](#is_future) - Checks if a date is strictly in the future
- [is_today()](#is_today) - Checks if a date falls on today's calendar date
- [is_same_day()](#is_same_day) - Checks if two dates fall on the same calendar day
- [is_same_month()](#is_same_month) - Checks if two dates fall in the same month and year
- [is_same_year()](#is_same_year) - Checks if two dates fall in the same year
- [is_same_week()](#is_same_week) - Checks if two dates fall in the same ISO week
- [is_same_quarter()](#is_same_quarter) - Checks if two dates fall in the same quarter
- [is_business_hours()](#is_business_hours) - Checks if datetime falls within business hours on a weekday
- [is_iso_long_year()](#is_iso_long_year) - True if the ISO year has 53 weeks
- [week_year()](#week_year) - ISO week-numbering year (may differ at year boundaries)

---

## Function Index

**A**
- [add_days_from_now()](#add_days_from_now) - Adds or subtracts days from current date and time
- [add_microseconds()](#add_microseconds) - Adds or subtracts microseconds to/from datetime
- [add_months()](#add_months) - Shifts a date forward or backward by months
- [add_time_to_date()](#add_time_to_date) - Adds or subtracts specified quantity of time to/from date
- [add_years()](#add_years) - Shifts a date forward or backward by years
- [ad_format_to_datetime()](#ad_format_to_datetime) - Converts Active Directory format string to Python datetime object
- [age()](#age) - Calculates age in complete years from a birth date

**B**
- [business_hours_between()](#business_hours_between) - Calculates business hours between two datetimes

**C**
- [calculate_days_between_dates()](#calculate_days_between_dates) - Calculates absolute number of days between two dates
- [convert_timezone()](#convert_timezone) - Converts timezone-aware datetime from current to target timezone
- [current_date()](#current_date) - Gets current local date without time component
- [current_datetime()](#current_datetime) - Gets current local date and time
- [current_day()](#current_day) - Gets current day of month (1-31)
- [current_days_in_month()](#current_days_in_month) - Returns number of days in current month
- [current_first_day_of_month()](#current_first_day_of_month) - Returns first day of current month at midnight
- [current_is_leap_year()](#current_is_leap_year) - Checks if current year is a leap year
- [current_is_weekend()](#current_is_weekend) - Checks if current date is weekend (Saturday/Sunday)
- [current_is_working_day()](#current_is_working_day) - Checks if current date is working day (Monday-Friday)
- [current_last_day_of_month()](#current_last_day_of_month) - Gets last day of current month
- [current_last_friday_of_month()](#current_last_friday_of_month) - Gets last Friday of current month
- [current_month()](#current_month) - Gets current month (1-12)
- [current_month_name()](#current_month_name) - Returns name of current month in specified language
- [current_next_friday()](#current_next_friday) - Gets next Friday after current date
- [current_previous_friday()](#current_previous_friday) - Gets previous Friday before current date
- [current_quarter()](#current_quarter) - Returns current quarter of the year (1-4)
- [current_season()](#current_season) - Returns current season of the year
- [current_time()](#current_time) - Gets current local time without date component
- [current_weekday_name()](#current_weekday_name) - Gets name of current weekday in specified language
- [current_weekday_number()](#current_weekday_number) - Gets current weekday number with European or US convention
- [current_week_number()](#current_week_number) - Returns current ISO week number (1-53)
- [current_year()](#current_year) - Gets current year as integer

**D**
- [date_intervals()](#date_intervals) - Generates list of date intervals for specific granularity
 - [date_range()](#date_range) - Generates list of dates between start and end at regular intervals
 - [diff_time()](#diff_time) - Whole-unit difference between two dates (supported units)
- [date_part()](#date_part) - Extracts specific part from date/time, similar to VBA DatePart
- [date_to_iso_format()](#date_to_iso_format) - Converts datetime object to ISO 8601 formatted string
- [date_to_julian()](#date_to_julian) - Converts standard date to Julian date representation (day of year)
- [date_to_string()](#date_to_string) - Converts datetime object into a formatted string
- [datedif()](#datedif) - Date difference in Y/M/D/YM/MD/YD units (DATEDIF)
- [dates_between()](#dates_between) - Generates list of all dates between two dates, inclusive
- [datetime_to_ad_format()](#datetime_to_ad_format) - Converts datetime or date to Active Directory format string
- [datetime_to_date()](#datetime_to_date) - Converts datetime object to date object, discarding time components
- [datetime_to_filetime()](#datetime_to_filetime) - Converts Python datetime or date to Windows FILETIME value
- [datetime_to_integer()](#datetime_to_integer) - Converts date to integer in YYYYMMDD format, ignoring time
- [datetime_to_milliseconds_timestamp()](#datetime_to_milliseconds_timestamp) - Converts datetime object to Unix timestamp in milliseconds
- [datetime_to_timestamp()](#datetime_to_timestamp) - Converts datetime object to Unix timestamp
- [date_to_human_short()](#date_to_human_short) - Formats a date as a short human-readable string
- [days_in_month()](#days_in_month) - Returns number of days in given month and year

**E**
- [easter_date()](#easter_date) - Computes Easter Sunday date for a given year
- [end_of_month()](#end_of_month) - Returns last day of month for given date
- [end_of_month_offset()](#end_of_month_offset) - Returns last day of month N months from date
- [end_of_quarter()](#end_of_quarter) - Returns last day of the quarter for a given date
- [end_of_year()](#end_of_year) - Returns last day of year for given date

**F**
- [filetime_to_datetime()](#filetime_to_datetime) - Converts Windows FILETIME value to datetime object and string
- [filter_dates_by_weekday()](#filter_dates_by_weekday) - Filters list of dates, returning only specific weekday
- [first_day_of_week()](#first_day_of_week) - Calculates first day of week for given date
- [format_datetime_ampm()](#format_datetime_ampm) - Formats datetime into 12-hour (AM/PM) string representation
- [from_iso_to_local_datetime()](#from_iso_to_local_datetime) - Converts ISO 8601 string to datetime in local timezone
- [full_months_between()](#full_months_between) - Returns number of complete months between two dates
- [full_years_between()](#full_years_between) - Returns number of complete years between two dates

**G**
- [generate_random_date()](#generate_random_date) - Generates random date within specified range
- [generate_random_datetime()](#generate_random_datetime) - Generates random datetime within range, optionally localized
- [generate_random_time()](#generate_random_time) - Generates random time within optional range
- [get_age_from_dob()](#get_age_from_dob) - Calculates age in full years from date of birth
- [get_date_component()](#get_date_component) - Extracts specific component (day, month, year, etc.) from date
- [get_first_business_day_of_month()](#get_first_business_day_of_month) - Returns first working day of month
- [get_last_business_day_of_month()](#get_last_business_day_of_month) - Returns last working day of month
- [get_last_friday_of_month()](#get_last_friday_of_month) - Calculates last Friday of given month
- [get_local_now()](#get_local_now) - Gets current date/time localized to specified timezone
- [get_next_friday()](#get_next_friday) - Calculates next upcoming Friday from given date
- [get_nth_weekday_of_month()](#get_nth_weekday_of_month) - Calculates date of n-th occurrence of specific weekday
- [get_number_of_days_in_quarter()](#get_number_of_days_in_quarter) - Calculates total days in specific quarter of year
- [get_number_of_days_in_year()](#get_number_of_days_in_year) - Calculates total number of days in given year
- [get_previous_friday()](#get_previous_friday) - Calculates immediately preceding Friday from given date
- [get_quarter()](#get_quarter) - Extracts quarter number (1-4) from date
- [get_season()](#get_season) - Returns season of year for given date
- [get_week_of_year()](#get_week_of_year) - Returns ISO week number of year for date
- [get_week_range()](#get_week_range) - Retrieves start and end dates for specific ISO week
- [get_working_days_in_range()](#get_working_days_in_range) - Calculates working days (excluding weekends/holidays) within date range
- [get_year_calendar_by_weeks()](#get_year_calendar_by_weeks) - Generates complete list of ISO weeks for year

**I**
- [integer_to_datetime()](#integer_to_datetime) - Converts YYYYMMDD integer back to datetime object
- [intersection_of_date_ranges()](#intersection_of_date_ranges) - Returns intersection period if two date ranges overlap
- [is_between_dates()](#is_between_dates) - Checks if date falls within date range
- [is_business_hours()](#is_business_hours) - Checks if datetime falls within business hours on a weekday
- [is_date_type()](#is_date_type) - Checks if object is date type (date, datetime, time)
- [is_dateclass()](#is_dateclass) - Checks if object is of datetime type
- [is_duration_greater_than()](#is_duration_greater_than) - Checks if duration between dates is greater than threshold
- [is_duration_less_than()](#is_duration_less_than) - Checks if duration between dates is less than threshold
- [is_future()](#is_future) - Checks if a date is strictly in the future
- [is_leap_year()](#is_leap_year) - Checks if given year is leap year
- [is_past()](#is_past) - Checks if a date is strictly in the past
- [is_same_day()](#is_same_day) - Checks if two dates fall on the same calendar day
- [is_same_month()](#is_same_month) - Checks if two dates fall in the same month and year
- [is_same_quarter()](#is_same_quarter) - Checks if two dates fall in the same quarter
- [is_same_week()](#is_same_week) - Checks if two dates fall in the same ISO week
- [is_same_year()](#is_same_year) - Checks if two dates fall in the same year
- [is_today()](#is_today) - Checks if a date falls on today's calendar date
- [iso_week_number()](#iso_week_number) - Returns ISO 8601 week number for a given date
- [is_valid_date()](#is_valid_date) - Validates if input parameter is valid date
- [is_valid_time()](#is_valid_time) - Verifies if hour, minute, second, microsecond represent valid time
- [is_weekend()](#is_weekend) - Determines if date is Saturday or Sunday
- [is_working_day()](#is_working_day) - Checks if date is working day (Monday-Friday)

**J**
- [julian_to_date()](#julian_to_date) - Converts Julian date (day of year) to standard datetime object

**L**
- [last_day_of_month()](#last_day_of_month) - Returns last day of the month for a given date
- [last_day_of_week()](#last_day_of_week) - Calculates last day of week for given date
- [last_weekday_of_month()](#last_weekday_of_month) - Returns last occurrence of a specific weekday in the month
- [list_available_timezones()](#list_available_timezones) - Retrieves sorted list of all available IANA timezone names

**M**
- [milliseconds_timestamp_to_datetime()](#milliseconds_timestamp_to_datetime) - Converts Unix timestamp in milliseconds to datetime object
- [month_name()](#month_name) - Gets name of month for given date in language
- [months_between_dates()](#months_between_dates) - Calculates number of complete months between two dates

**N**
- [network_days_intl()](#network_days_intl) - Calculates working days between dates with custom weekend definition
- [networkdays()](#networkdays) - Working days between dates excluding weekends/holidays (NETWORKDAYS)
- [next_business_day()](#next_business_day) - Returns next working day (Mon-Fri) after a given date
- [next_weekday()](#next_weekday) - Returns next occurrence of a specific weekday after a given date

**O**
- [overlap_dates()](#overlap_dates) - Checks whether two date ranges overlap
- [overlap_days()](#overlap_days) - Count overlapping days between two date ranges

**P**
- [parse_date_flexible()](#parse_date_flexible) - Parses a date string by trying multiple common formats
- [parts_to_date()](#parts_to_date) - Creates date object from year, month, day components
- [parts_to_datetime()](#parts_to_datetime) - Creates datetime object from numeric components
- [previous_business_day()](#previous_business_day) - Returns previous working day (Mon-Fri) before a given date
- [previous_weekday()](#previous_weekday) - Returns most recent occurrence of a specific weekday before a given date

**Q**
- [quarters_between_dates()](#quarters_between_dates) - Calculates complete quarters between two dates

**R**
- [recurring_dates()](#recurring_dates) - Generates recurring dates within a range
- [relative_time_description()](#relative_time_description) - Returns a human-readable relative time string
- [round_datetime()](#round_datetime) - Rounds a datetime to the nearest unit

**S**
- [seconds_since_midnight()](#seconds_since_midnight) - Returns seconds elapsed since midnight of current day
- [set_date_component()](#set_date_component) - Returns new datetime with specified components modified
- [set_microseconds()](#set_microseconds) - Sets microseconds of datetime to specific value
- [start_of_month()](#start_of_month) - Returns first day of month for given date
- [start_of_quarter()](#start_of_quarter) - Returns first day of the quarter for a given date
- [start_of_year()](#start_of_year) - Returns first day of year for given date

**T**
- [time_difference()](#time_difference) - Calculates difference between two dates in specified unit
- [time_from_datetime()](#time_from_datetime) - Extracts time component from datetime object
- [timedelta_to_components()](#timedelta_to_components) - Converts timedelta object into dictionary of its components
- [timestamp_to_datetime()](#timestamp_to_datetime) - Converts Unix timestamp back to datetime object

**U**
- [unix_timestamp_to_datetime()](#unix_timestamp_to_datetime) - Converts UNIX timestamp to datetime object with optional timezone
- [utc_to_datetime()](#utc_to_datetime) - Converts any datetime or date string to UTC representation
- [utc_to_midnight_iso()](#utc_to_midnight_iso) - Converts datetime to equivalent at midnight UTC
- [utc_to_timezone()](#utc_to_timezone) - Localizes naive datetime or converts aware datetime to target timezone

**W**
- [week_number()](#week_number) - Returns week number of year for a given date
- [weekday_name()](#weekday_name) - Gets name of weekday for given date in language
- [weekday_number()](#weekday_number) - Gets day of week as number for given date
- [week_of_month()](#week_of_month) - Returns week number of month for given date
- [workday()](#workday) - Returns date after a given number of working days (Mon-Fri)
- [workday_intl()](#workday_intl) - Returns date after working days with custom weekend definition

**Y**
- [year_fraction()](#year_fraction) - Calculates fraction of year between two dates

---

## Date Conversions

### `datetime_to_date()`

Converts a datetime object to a date object, discarding the time components.

**Parameters:**
- `datetime_obj` (datetime): The datetime object to convert.

**Returns:**
- `date`: A new date object representing the date part of the input datetime.

**Ejemplo:**
```python
from datetime import datetime, date
from formulite.fxDate.date_convertions import datetime_to_date

dt_with_time = datetime(2025, 6, 12, 10, 30, 45)
date_only = datetime_to_date(dt_with_time)
print(date_only)  # 2025-06-12
print(type(date_only))  # <class 'datetime.date'>
```

**Cost:** O(1)

---

### `date_to_string()`

Converts a datetime object into a formatted string.

**Parameters:**
- `date_input` (datetime): The datetime object to convert.
- `format_code` (str, optional): The format code string (e.g., '%Y-%m-%d', '%d/%m/%Y %H:%M:%S'). Defaults to '%Y-%m-%d'.

**Returns:**
- `str`: The formatted date string.

**Ejemplo:**
```python
from datetime import datetime
from formulite.fxDate.date_convertions import date_to_string

my_date = datetime(2023, 10, 26, 15, 30, 45)

# Default format
print(date_to_string(my_date))  # '2023-10-26'

# European format
print(date_to_string(my_date, '%d/%m/%Y'))  # '26/10/2023'

# Date and time
print(date_to_string(my_date, '%Y-%m-%d %H:%M:%S'))  # '2023-10-26 15:30:45'

# Full descriptive format
print(date_to_string(my_date, '%A, %d %B %Y'))  # 'Thursday, 26 October 2023'
```

**Cost:** O(1)

---

### `datetime_to_integer()`

Converts a date to an integer in YYYYMMDD format, ignoring time components.

**Parameters:**
- `date_input` (Union[datetime, date, str]): The date to convert.
- `input_format` (str, optional): The format code if date_input is a string.

**Returns:**
- `int`: The date converted to integer in YYYYMMDD format.

**Ejemplo:**
```python
from datetime import datetime, date
from formulite.fxDate.date_convertions import datetime_to_integer

# Using datetime object
print(datetime_to_integer(datetime(2025, 2, 1)))  # 20250201

# Using date object
print(datetime_to_integer(date(2025, 2, 1)))  # 20250201

# Using string
print(datetime_to_integer("01/02/2025", "%d/%m/%Y"))  # 20250201
```

**Cost:** O(1)

---

### `datetime_to_timestamp()`

Converts a datetime object to a Unix timestamp.

**Parameters:**
- `date_input` (datetime): The datetime object to convert (preferably timezone-aware in UTC).

**Returns:**
- `float`: The Unix timestamp as a float (seconds since epoch).

**Ejemplo:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import datetime_to_timestamp

# Example with UTC-aware datetime (recommended)
dt_utc = datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)
print(datetime_to_timestamp(dt_utc))  # 1672531200.0

# Example with naive datetime (treated as local time)
dt_naive = datetime(2023, 1, 1, 0, 0, 0)
print(datetime_to_timestamp(dt_naive))  # Will vary based on local timezone
```

**Cost:** O(1)

---

### `timestamp_to_datetime()`

Converts a Unix timestamp back to a datetime object.

**Parameters:**
- `timestamp_input` (Union[int, float]): The Unix timestamp to convert.

**Returns:**
- `datetime`: A timezone-aware datetime object in UTC.

**Ejemplo:**
```python
from formulite.fxDate.date_convertions import timestamp_to_datetime

# With float timestamp
print(timestamp_to_datetime(1672531200.0))
# datetime.datetime(2023, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)

# With int timestamp
print(timestamp_to_datetime(1672531200))
# datetime.datetime(2023, 1, 1, 0, 0, tzinfo=datetime.timezone.utc)
```

**Cost:** O(1)

---

### `date_to_iso_format()`

Converts a datetime object to an ISO 8601 formatted string.

**Parameters:**
- `date_input` (Union[datetime, str]): The date to convert.
- `input_format` (str, optional): The format code if date_input is a string (required if it's a string).

**Returns:**
- `str`: The date represented as an ISO 8601 formatted string.

**Ejemplo:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import date_to_iso_format

# With naive datetime
print(date_to_iso_format(datetime(2023, 1, 15, 10, 30, 45, 123456)))
# '2023-01-15T10:30:45.123456'

# With timezone-aware datetime (recommended)
dt_utc = datetime(2023, 1, 15, 10, 30, 45, 123456, tzinfo=timezone.utc)
print(date_to_iso_format(dt_utc))
# '2023-01-15T10:30:45.123456+00:00'

# With string input
print(date_to_iso_format("2023-05-10 08:00:00", "%Y-%m-%d %H:%M:%S"))
# '2023-05-10T08:00:00'
```

**Cost:** O(1)

---

### `from_iso_to_local_datetime()`

Converts an ISO 8601 formatted string to a datetime object in local timezone.

**Parameters:**
- `iso_string` (str): The date and time as an ISO 8601 formatted string.

**Returns:**
- `datetime`: A timezone-aware datetime object adjusted to the system's local timezone.

**Ejemplo:**
```python
from formulite.fxDate.date_convertions import from_iso_to_local_datetime

# With UTC 'Z' string
iso_utc_string = "2023-10-26T15:30:00Z"
local_dt = from_iso_to_local_datetime(iso_utc_string)
print(f"UTC: {iso_utc_string} -> Local: {local_dt}")

# With explicit offset
iso_offset_string = "2023-10-26T15:30:00+02:00"
local_dt = from_iso_to_local_datetime(iso_offset_string)
print(f"Offset: {iso_offset_string} -> Local: {local_dt}")

# Without timezone information (naive)
iso_naive_string = "2023-10-26T15:30:00"
local_dt = from_iso_to_local_datetime(iso_naive_string)
print(f"Naive: {iso_naive_string} -> Local: {local_dt}")
```

**Cost:** O(1)

---

### `list_available_timezones()`

Retrieves and returns a sorted list of all available IANA timezone names.

**Returns:**
- `List[str]`: A sorted list of strings, where each string is a valid IANA timezone name.

**Example:**
```python
from formulite.fxDate.date_convertions import list_available_timezones

timezones = list_available_timezones()
print(timezones[:5])  # Print first 5 for brevity
# ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara']

print('Europe/Madrid' in timezones)  # True
```

**Cost:** O(1)

---

### `convert_timezone()`

Converts a timezone-aware datetime object from its current timezone to a target timezone.

**Parameters:**
- `date_input` (datetime): The timezone-aware datetime object to convert. Must have `tzinfo` set.
- `target_tz_name` (str): The name of the target timezone (e.g., 'America/New_York', 'Europe/Madrid', 'Asia/Tokyo', 'UTC').

**Returns:**
- `datetime`: A new datetime object representing the same moment in time, but localized to the target timezone.

**Example:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import convert_timezone

# Define a UTC datetime
utc_now = datetime(2025, 6, 11, 1, 1, 45, tzinfo=timezone.utc)
print(f"Original UTC: {utc_now}")
# Original UTC: 2025-06-11 01:01:45+00:00

# Convert to Madrid Time (CEST = UTC+2)
madrid_time = convert_timezone(utc_now, 'Europe/Madrid')
print(f"In Madrid: {madrid_time}")
# In Madrid: 2025-06-11 03:01:45+02:00

# Convert to New York Time (EDT = UTC-4)
ny_time = convert_timezone(utc_now, 'America/New_York')
print(f"In New York: {ny_time}")
# In New York: 2025-06-10 21:01:45-04:00
```

**Cost:** O(1)

---

### `utc_to_datetime()`

Converts any datetime object (aware or naive) or date string to its equivalent UTC representation.

**Parameters:**
- `date_input` (Union[datetime, str]): The date to convert to UTC. Can be a datetime object or a string.
- `input_format` (Optional[str], optional): The format code string for `date_input` if it's a string. Required if `date_input` is a string.
- `input_tz` (Optional[str], optional): The IANA timezone name of the `date_input` if it's a naive datetime or string without timezone info. If None and `date_input` is naive, the system's local timezone is assumed.

**Returns:**
- `datetime`: A timezone-aware datetime object representing the input date and time in UTC.

**Example:**
```python
from datetime import datetime, timezone
import zoneinfo
from formulite.fxDate.date_convertions import utc_to_datetime

# Scenario 1: Naive datetime (assumes local time if no input_tz specified)
naive_dt_local = datetime(2025, 6, 11, 10, 0, 0)
utc_dt = utc_to_datetime(naive_dt_local)
print(f"Naive local -> UTC: {utc_dt}")

# Scenario 2: Aware datetime in 'America/Los_Angeles'
la_tz = zoneinfo.ZoneInfo('America/Los_Angeles')
aware_dt_la = datetime(2025, 6, 11, 10, 0, 0, tzinfo=la_tz)
utc_dt = utc_to_datetime(aware_dt_la)
print(f"Aware LA (10:00 PDT) -> UTC: {utc_dt}")
# Expected: 2025-06-11 17:00:00+00:00

# Scenario 3: String with explicit timezone
utc_dt = utc_to_datetime("2025-06-11 10:00:00", "%Y-%m-%d %H:%M:%S", "Asia/Tokyo")
print(f"String Tokyo (10:00 JST) -> UTC: {utc_dt}")
# Expected: 2025-06-11 01:00:00+00:00
```

**Cost:** O(1)

---

### `utc_to_timezone()`

Localizes a naive datetime to the target timezone or converts an aware datetime to the target timezone.

**Parameters:**
- `input_datetime` (datetime): The datetime object to process.
- `target_tz_name` (str): The name of the target timezone to localize/convert to. Defaults to "Europe/Madrid".

**Returns:**
- `datetime`: A timezone-aware datetime object localized to the target timezone.

**Example:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import utc_to_timezone

# Localize naive datetime to Madrid time
naive_dt = datetime(2025, 6, 11, 10, 0, 0)
localized_to_madrid = utc_to_timezone(naive_dt, 'Europe/Madrid')
print(f"Localized to Madrid: {localized_to_madrid}")
# Expected: 2025-06-11 10:00:00+02:00

# Convert Madrid time to New York time
madrid_to_ny = utc_to_timezone(localized_to_madrid, 'America/New_York')
print(f"Madrid to New York: {madrid_to_ny}")
# Expected: 2025-06-11 04:00:00-04:00
```

**Cost:** O(1)

---

### `date_to_julian()`

Converts a standard date to its Julian date representation (day of the year).

**Parameters:**
- `date_input` (Union[datetime, str]): The date to convert. Can be a datetime object or a date string.
- `input_format` (Optional[str], optional): The format code if `date_input` is a string. Required if it's a string.

**Returns:**
- `int`: The day number of the year (1 to 365 or 366).

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_convertions import date_to_julian

# January 1, 2025 (always day 1)
print(date_to_julian(datetime(2025, 1, 1)))  # 1

# February 1, 2025 (non-leap year)
print(date_to_julian(datetime(2025, 2, 1)))  # 32

# March 1, 2024 (leap year)
print(date_to_julian(datetime(2024, 3, 1)))  # 61

# December 31, 2024 (leap year)
print(date_to_julian(datetime(2024, 12, 31)))  # 366

# Using string
print(date_to_julian("2025-06-15", "%Y-%m-%d"))  # 166
```

**Cost:** O(1)

---

### `julian_to_date()`

Converts a Julian date (day of the year) to a standard datetime object.

**Parameters:**
- `julian_date` (int): The day number of the year (1 to 365 or 366). Must be a positive integer.
- `year` (int): The year to which the Julian date belongs.

**Returns:**
- `datetime`: A datetime object representing the calculated date (at midnight).

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_convertions import julian_to_date

# Day 1 of year 2025
print(julian_to_date(1, 2025))
# datetime.datetime(2025, 1, 1, 0, 0)

# Day 32 of year 2025 (February 1)
print(julian_to_date(32, 2025))
# datetime.datetime(2025, 2, 1, 0, 0)

# Day 61 of year 2024 (March 1, leap year)
print(julian_to_date(61, 2024))
# datetime.datetime(2024, 3, 1, 0, 0)

# Day 366 of year 2024 (December 31, leap year)
print(julian_to_date(366, 2024))
# datetime.datetime(2024, 12, 31, 0, 0)
```

**Cost:** O(1)

---

### `datetime_to_milliseconds_timestamp()`

Converts a datetime object to a Unix timestamp in milliseconds.

**Parameters:**
- `date_input` (datetime): The datetime object to convert. Preferably with `tzinfo=timezone.utc`.

**Returns:**
- `int`: The Unix timestamp in milliseconds.

**Example:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import datetime_to_milliseconds_timestamp

dt_utc = datetime(2025, 6, 11, 1, 58, 11, 123456, tzinfo=timezone.utc)
print(datetime_to_milliseconds_timestamp(dt_utc))
# 1749597491123

# Naive datetime is assumed to be UTC
dt_naive = datetime(2025, 6, 11, 1, 58, 11, 123456)
print(datetime_to_milliseconds_timestamp(dt_naive))
# 1749597491123
```

**Cost:** O(1)

---

### `milliseconds_timestamp_to_datetime()`

Converts a Unix timestamp in milliseconds back to a datetime object.

**Parameters:**
- `timestamp_ms` (int): The Unix timestamp in milliseconds to convert.

**Returns:**
- `datetime`: A timezone-aware datetime object representing the timestamp in UTC.

**Example:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import milliseconds_timestamp_to_datetime

print(milliseconds_timestamp_to_datetime(1749597491123))
# datetime.datetime(2025, 6, 11, 1, 58, 11, 123000, tzinfo=datetime.timezone.utc)
```

**Cost:** O(1)

---

### `utc_to_midnight_iso()`

Converts a datetime to its equivalent at midnight UTC.

**Parameters:**
- `p_datetime` (datetime): The datetime object to convert.

**Returns:**
- `datetime`: A new datetime object set to midnight UTC (00:00:00) for the given date.

**Example:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import utc_to_midnight_iso

# Datetime with specific time
dt = datetime(2025, 6, 11, 15, 30, 45, tzinfo=timezone.utc)
midnight_dt = utc_to_midnight_iso(dt)
print(midnight_dt)
# 2025-06-11 00:00:00+00:00

# Naive datetime (assumed UTC)
naive_dt = datetime(2025, 6, 11, 15, 30, 45)
midnight_dt = utc_to_midnight_iso(naive_dt)
print(midnight_dt)
# 2025-06-11 00:00:00+00:00
```

**Cost:** O(1)

---

### `filetime_to_datetime()`

Converts a Windows FILETIME value to a datetime object and its string representation.

**Parameters:**
- `filetime` (int): The Windows FILETIME value to convert (100-nanosecond intervals since January 1, 1601 UTC). Must be a positive integer.

**Returns:**
- `Tuple[datetime, str]`: A tuple containing the converted datetime object (UTC) and its ISO formatted string representation.

**Example:**
```python
from formulite.fxDate.date_convertions import filetime_to_datetime

# Modern date (post-1970)
dt, dt_str = filetime_to_datetime(132723834123456789)
print(dt)
# 2022-01-15 12:30:12.345678+00:00
print(dt_str)
# 2022-01-15 12:30:12.345678

# Historical date (pre-1970)
dt, dt_str = filetime_to_datetime(130611456000000000)
print(dt)
# 1601-01-01 00:00:00+00:00
```

**Cost:** O(1)

---

### `datetime_to_filetime()`

Converts a Python datetime or date object to a Windows FILETIME value.

**Parameters:**
- `p_dt` (Union[datetime, date]): The datetime or date object to convert. If it's a date object, it will be treated as midnight (00:00:00) UTC of that day. If it's a naive datetime, it will be assumed to be in UTC.

**Returns:**
- `int`: The FILETIME value as a 64-bit integer.

**Example:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import datetime_to_filetime

# Convert a datetime to FILETIME
dt = datetime(2022, 1, 15, 12, 30, 12, 345678, tzinfo=timezone.utc)
filetime = datetime_to_filetime(dt)
print(filetime)
# 132723834123456780 (approximately)

# Convert a date to FILETIME (treated as midnight UTC)
from datetime import date
d = date(2022, 1, 15)
filetime = datetime_to_filetime(d)
print(filetime)
```

**Cost:** O(1)

---

### `datetime_to_ad_format()`

Converts a datetime or date object to Active Directory format string 'YYYYMMDDHHMMSS.0Z'.

**Parameters:**
- `p_dt_input` (Union[datetime, date]): The datetime or date object to convert. If it's a date object, midnight (00:00:00) UTC will be assumed. If it's a naive datetime, it will be assumed to be UTC.

**Returns:**
- `str`: The date and time formatted as 'YYYYMMDDHHMMSS.0Z'.

**Example:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import datetime_to_ad_format

# Convert datetime to AD format
dt = datetime(2025, 6, 11, 15, 30, 45, tzinfo=timezone.utc)
ad_str = datetime_to_ad_format(dt)
print(ad_str)
# 20250611153045.0Z

# Convert date to AD format (assumes midnight)
from datetime import date
d = date(2025, 6, 11)
ad_str = datetime_to_ad_format(d)
print(ad_str)
# 20250611000000.0Z
```

**Cost:** O(1)

---

### `ad_format_to_datetime()`

Converts an Active Directory format date/time string 'YYYYMMDDHHMMSS.0Z' to a Python datetime object.

**Parameters:**
- `p_ad_date_str` (str): The date/time string in format 'YYYYMMDDHHMMSS.0Z'.

**Returns:**
- `datetime`: A timezone-aware datetime object representing the date and time in UTC.

**Example:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_convertions import ad_format_to_datetime

# Parse AD format string
ad_str = "20250611153045.0Z"
dt = ad_format_to_datetime(ad_str)
print(dt)
# datetime.datetime(2025, 6, 11, 15, 30, 45, tzinfo=datetime.timezone.utc)
```

**Cost:** O(1)

---

## System Functions

### `current_datetime()`

Gets the current local date and time.

**Returns:**
- `datetime`: Datetime object representing the current local date and time.

**Example:**
```python
from formulite.fxDate.date_sys import current_datetime

now = current_datetime()
print(now.strftime('%Y-%m-%d %H:%M:%S'))  # E.g.: 2025-06-10 21:46:04
```

**Cost:** O(1)

---

### `current_date()`

Gets the current local date (without time component).

**Returns:**
- `datetime`: Datetime object representing the current local date.

**Example:**
```python
from formulite.fxDate.date_sys import current_date

today = current_date()
print(today.strftime('%Y-%m-%d'))  # E.g.: 2025-06-10
```

**Cost:** O(1)

---

### `current_time()`

Gets the current local time (without date component).

**Returns:**
- `datetime`: Datetime object representing the current local time.

**Example:**
```python
from formulite.fxDate.date_sys import current_time

time_now = current_time()
print(time_now.strftime('%H:%M:%S'))  # E.g.: 21:46:04
```

**Cost:** O(1)

---

### `current_year()`

Gets the current year.

**Returns:**
- `int`: The current year as an integer.

**Example:**
```python
from formulite.fxDate.date_sys import current_year

year = current_year()
print(year)  # E.g.: 2025
```

**Cost:** O(1)

---

### `current_month()`

Gets the current month (1-12).

**Returns:**
- `int`: The current month as an integer (1 for January, 12 for December).

**Example:**
```python
from formulite.fxDate.date_sys import current_month

month = current_month()
print(month)  # E.g.: 6
```

**Cost:** O(1)

---

### `current_day()`

Gets the current day of the month (1-31).

**Returns:**
- `int`: The current day of the month as an integer.

**Example:**
```python
from formulite.fxDate.date_sys import current_day

day = current_day()
print(day)  # E.g.: 10
```

**Cost:** O(1)

---

### `current_weekday_number()`

Gets the current weekday as a number, allowing European (Monday=0) or US (Sunday=0) convention.

**Parameters:**
- `start_day` (str): 'european' (Monday=0) or 'us' (Sunday=0). Defaults to 'european'.

**Returns:**
- `int`: The day of the week as an integer.

**Example:**
```python
from formulite.fxDate.date_sys import current_weekday_number

# European convention
print(current_weekday_number(start_day='european'))  # E.g.: 2 (Wednesday)

# US convention
print(current_weekday_number(start_day='us'))  # E.g.: 3 (Wednesday)
```

**Cost:** O(1)

---

### `current_weekday_name()`

Gets the name of the current weekday in the specified language.

**Parameters:**
- `language` (str, optional): Two-letter language code. Defaults to 'en'. Supports 'en' and 'es'.

**Returns:**
- `str`: The name of the current weekday.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_weekday_name

print(current_weekday_name('en'))  # 'Thursday'
print(current_weekday_name('es'))  # 'Jueves'
```

**Cost:** O(1)

---

### `current_last_day_of_month()`

Gets the last day of the current month.

**Returns:**
- `datetime`: Datetime object representing the last day of the current month.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_last_day_of_month

last_day = current_last_day_of_month()
print(last_day)  # datetime.datetime(2023, 10, 31, 0, 0)
```

**Cost:** O(1)

---

### `current_last_friday_of_month()`

Gets the last Friday of the current month.

**Returns:**
- `datetime`: Datetime object representing the last Friday of the current month.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_last_friday_of_month

last_friday = current_last_friday_of_month()
print(last_friday)  # datetime.datetime(2023, 10, 27, 0, 0)
```

**Cost:** O(1)

---

### `current_next_friday()`

Gets the next Friday after the current date.

**Returns:**
- `datetime`: Datetime object representing the next Friday.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_next_friday

next_friday = current_next_friday()
print(next_friday)  # datetime.datetime(2023, 10, 13, 0, 0)
```

**Cost:** O(1)

---

### `current_previous_friday()`

Gets the previous Friday before the current date.

**Returns:**
- `datetime`: Datetime object representing the previous Friday.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_previous_friday

prev_friday = current_previous_friday()
print(prev_friday)  # datetime.datetime(2023, 10, 6, 0, 0)
```

**Cost:** O(1)

---

### `current_is_working_day()`

Checks if the current date is a working day (Monday to Friday).

**Returns:**
- `bool`: True if the current date is a working day, False otherwise.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_is_working_day

is_workday = current_is_working_day()
print(is_workday)  # True
```

**Cost:** O(1)

---

### `current_is_weekend()`

Checks if the current date is a weekend (Saturday or Sunday).

**Returns:**
- `bool`: True if the current date is a weekend, False otherwise.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_is_weekend

is_weekend = current_is_weekend()
print(is_weekend)  # False
```

**Cost:** O(1)

---

### `get_local_now()`

Gets the current date and time, localized to the specified timezone.

**Parameters:**
- `tz` (str, optional): IANA timezone name (e.g., 'America/New_York'). If None, uses the system timezone.

**Returns:**
- `datetime`: Timezone-aware datetime object, localized to the specified timezone.

**Example:**
```python
from formulite.fxDate.date_sys import get_local_now

# Current time in Tokyo
tokyo_now = get_local_now('Asia/Tokyo')
print(f"Time in Tokyo: {tokyo_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

# Current time in system timezone
local_now = get_local_now()
print(f"Local time: {local_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}")

# Current time in New York
ny_now = get_local_now('America/New_York')
print(f"Time in NY: {ny_now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"))
```

**Cost:** O(1)

---

## Date Operations

### `is_date_type()`

Checks if an object is of date type (date, datetime, or time).

**Parameters:**
- `value` (Any): The value to check.

**Returns:**
- `bool`: True if the value is date, datetime, or time; False otherwise.

**Ejemplo:**
```python
from datetime import date, datetime, time
from formulite.fxDate.date_operations import is_date_type

print(is_date_type(datetime(2025, 6, 11)))  # True
print(is_date_type(date(2025, 6, 11)))  # True
print(is_date_type(time(10, 30, 0)))  # True
print(is_date_type("2025-06-11"))  # False
print(is_date_type(123))  # False
print(is_date_type(None))  # False
```

**Cost:** O(1)

---

### `is_valid_date()`

Validates if the input parameter is a valid date.

**Parameters:**
- `date_input` (Any): The parameter to validate. Can be a datetime object or a string.
- `date_format` (str): The expected format if date_input is a string. Defaults to "%Y-%m-%d".

**Returns:**
- `bool`: True if date_input is a valid date, False otherwise.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import is_valid_date

print(is_valid_date(datetime(2023, 1, 1)))  # True
print(is_valid_date("2023-01-01"))  # True
print(is_valid_date("01/01/2023", "%m/%d/%Y"))  # True
print(is_valid_date("2023-13-01"))  # False (invalid month)
print(is_valid_date("not-a-date"))  # False
print(is_valid_date(12345))  # False
print(is_valid_date(None))  # False
```

**Cost:** O(1)

---

### `weekday_number()`

Gets the day of the week as a number for a given date, supporting European and US conventions.

**Parameters:**
- `date_input` (datetime): The date for which to get the weekday number.
- `start_day` (str): 'european' (Monday=0) or 'anglo' (Sunday=0). Defaults to 'european'.

**Returns:**
- `int`: The day of the week as an integer.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import weekday_number

# Thursday
date_thursday = datetime(2023, 10, 26)
print(weekday_number(date_thursday, start_day='european'))  # 3
print(weekday_number(date_thursday, start_day='anglo'))  # 4

# Sunday
date_sunday = datetime(2023, 10, 29)
print(weekday_number(date_sunday, start_day='european'))  # 6
print(weekday_number(date_sunday, start_day='anglo'))  # 0
```

**Cost:** O(1)

---

### `weekday_name()`

Gets the name of the weekday for a given date in the specified language.

**Parameters:**
- `date_input` (datetime): The datetime object for which to get the weekday name.
- `language` (str, optional): Two-letter ISO 639-1 language code. Defaults to 'en'.

**Returns:**
- `str`: The full name of the weekday.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import weekday_name

# Thursday
date_to_check = datetime(2023, 10, 26)

# In English
print(weekday_name(date_to_check, 'en'))  # 'Thursday'

# In Spanish (requires locale installed)
try:
    print(weekday_name(date_to_check, 'es'))  # 'jueves' or 'Jueves'
except ValueError as e:
    print(f"Error: {e}")
```

**Cost:** O(1)

---

### `first_day_of_week()`

Calculates the first day of the week for a given date, allowing customization of the week's starting day.

**Parameters:**
- `date_input` (Union[datetime, str]): The date for which to find the first day of the week.
- `week_start_day` (int, optional): Day considered as the start of the week (0=Monday, 1=Tuesday, ..., 6=Sunday). Defaults to 0.

**Returns:**
- `datetime`: Datetime object representing the first day of the week, with time at midnight.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import first_day_of_week

# Sunday, June 15, 2025
date = datetime(2025, 6, 15)

# First day of the week (Monday by default)
print(first_day_of_week(date))  # datetime.datetime(2025, 6, 9, 0, 0)

# First day of the week (Sunday)
print(first_day_of_week(date, week_start_day=6))  # datetime.datetime(2025, 6, 15, 0, 0)

# Using string
print(first_day_of_week("2025-06-15", week_start_day=0))  # datetime.datetime(2025, 6, 9, 0, 0)
```

**Cost:** O(1)

---

### `last_day_of_week()`

Calculates the last day of the week for a given date.

**Parameters:**
- `date_input` (Union[datetime, str]): The date for which to find the last day of the week.
- `week_start_day` (int, optional): Day considered as the start of the week (0=Monday, ..., 6=Sunday). Defaults to 0.

**Returns:**
- `datetime`: Datetime object representing the last day of the week, with time at end of day.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import last_day_of_week

# Wednesday, June 11, 2025
date = datetime(2025, 6, 11)

# Last day of the week (Monday as start)
print(last_day_of_week(date))  # datetime.datetime(2025, 6, 15, 23, 59, 59, 999999)

# Last day of the week (Sunday as start)
print(last_day_of_week(date, week_start_day=6))  # datetime.datetime(2025, 6, 21, 23, 59, 59, 999999)
```

**Cost:** O(1)

---

### `month_name()`

Gets the name of the month for a given date in the specified language.

**Parameters:**
- `date_input` (datetime): The datetime object for which to get the month name.
- `language` (str, optional): Two-letter ISO 639-1 language code. Defaults to 'en'.

**Returns:**
- `str`: The full name of the month in the specified language.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import month_name

dt = datetime(2023, 10, 26)
print(month_name(dt, 'en'))  # 'October'
print(month_name(dt, 'es'))  # 'octubre'
```

**Cost:** O(1)

---

### `months_between_dates()`

Calculates the number of complete months between two dates.

**Parameters:**
- `start_date` (datetime): The start date.
- `end_date` (datetime): The end date.

**Returns:**
- `int`: Number of complete months. Negative if end_date is before start_date.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import months_between_dates

print(months_between_dates(datetime(2023, 1, 10), datetime(2023, 2, 10)))  # 1
print(months_between_dates(datetime(2023, 1, 10), datetime(2023, 3, 9)))   # 1
print(months_between_dates(datetime(2023, 5, 1), datetime(2023, 2, 1)))    # -3
```

**Cost:** O(1)

---

### `days_in_month()`

Returns the number of days in a given month and year.

**Parameters:**
- `year` (int): The year (e.g., 2023).
- `month` (int): The month (1 for January, 12 for December).

**Returns:**
- `int`: The number of days in the specified month.

**Example:**
```python
from formulite.fxDate.date_operations import days_in_month

print(days_in_month(2023, 2))  # 28
print(days_in_month(2024, 2))  # 29 (leap year)
print(days_in_month(2023, 4))  # 30
```

**Cost:** O(1)

---

### `calculate_days_between_dates()`

Calculates the absolute number of days between two dates.

**Parameters:**
- `start_date` (datetime.date): The first date.
- `end_date` (datetime.date): The second date.

**Returns:**
- `int`: The number of days between the two dates.

**Example:**
```python
from datetime import date
from formulite.fxDate.date_operations import calculate_days_between_dates

date1 = date(2023, 1, 1)
date2 = date(2023, 1, 31)
print(calculate_days_between_dates(date1, date2))  # 30
```

**Cost:** O(1)

---

### `get_nth_weekday_of_month()`

Calculates the date of the n-th occurrence of a specific weekday in a given month.

**Parameters:**
- `year` (int): The year (e.g., 2025).
- `month` (int): The month (1-12).
- `weekday` (int): The day of the week (0=Monday, 6=Sunday).
- `n` (int): The occurrence number (1 for first, 2 for second, etc.).

**Returns:**
- `Optional[datetime]`: The date of the n-th occurrence, or None if it doesn't exist.

**Example:**
```python
from formulite.fxDate.date_operations import get_nth_weekday_of_month

# Second Tuesday of June 2025
print(get_nth_weekday_of_month(2025, 6, 1, 2))  # datetime.datetime(2025, 6, 10, 0, 0)

# Fifth Monday of February 2024 (doesn't exist)
print(get_nth_weekday_of_month(2024, 2, 0, 5))  # None
```

**Cost:** O(1)

---

### `add_days_from_now()`

Adds or subtracts days from the current date and time.

**Parameters:**
- `days` (int): Number of days to add (positive) or subtract (negative).

**Returns:**
- `datetime`: New datetime after adding/subtracting days.

**Example:**
```python
from formulite.fxDate.date_operations import add_days_from_now

future_date = add_days_from_now(5)
past_date = add_days_from_now(-1)
```

**Cost:** O(1)

---

### `add_time_to_date()`

Adds or subtracts a specified quantity of time to/from a date.

**Parameters:**
- `original_date` (Union[datetime, str, date]): The starting date.
- `quantity` (int): The number of units to add (positive) or subtract (negative).
- `unit` (str): Time unit ('microseconds', 'milliseconds', 'seconds', 'minutes', 'hours', 'days', 'weeks').

**Returns:**
- `datetime`: New datetime after the operation.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import add_time_to_date

dt = datetime(2023, 1, 15)
print(add_time_to_date(dt, 10, 'days'))     # datetime.datetime(2023, 1, 25, 0, 0)
print(add_time_to_date(dt, 2, 'hours'))     # datetime.datetime(2023, 1, 15, 2, 0)
print(add_time_to_date("2023-01-15", 7, 'days'))  # datetime.datetime(2023, 1, 22, 0, 0)
```

**Cost:** O(1)

---

### `time_difference()`

Calculates the difference between two dates in a specified unit of time.

**Parameters:**
- `start_date` (Union[datetime, str, date]): The starting date.
- `end_date` (Union[datetime, str, date]): The ending date.
- `unit` (str, optional): Time unit. Defaults to 'days'.

**Returns:**
- `float`: The difference in the specified unit (can be negative).

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import time_difference

date1 = datetime(2023, 1, 1, 10, 0, 0)
date2 = datetime(2023, 1, 1, 12, 30, 0)
print(time_difference(date1, date2, 'minutes'))  # 150.0
print(time_difference("2023-01-01", "2023-01-10", 'days'))  # 9.0
```

**Cost:** O(1)

---

### `diff_time()`

Returns the whole-unit difference between two dates using units aligned with `add_time_to_date()`.

**Parameters:**
- `start_date` (Union[datetime, str, date]): Start date/time.
- `end_date` (Union[datetime, str, date]): End date/time.
- `unit` (str): Supported units: `'microseconds'`, `'milliseconds'`, `'seconds'`, `'minutes'`, `'hours'`, `'days'`, `'weeks'`.

**Returns:**
- `int`: Whole-unit difference according to the specified interval.

**Example:**
```python
from formulite.fxDate.date_operations import diff_time

print(diff_time("2025-01-01", "2025-01-03", "days"))  # 2
print(diff_time("2025-01-01 00:00:00", "2025-01-02 12:00:00", "hours"))  # 36
print(diff_time("2025-01-01", "2025-01-15", "weeks"))  # 2
```

**Notes:**
- For all supported units, this function leverages `time_difference()` and returns the integer part of the difference.
- Prefer `time_difference()` for fractional differences (e.g., 1.5 hours).

**Cost:** O(1)

---

### `date_part()`

Extracts a specific part from a date and time, similar to VBA's DatePart function.

**Parameters:**
- `part` (str): Part to extract ('d', 'y', 'h', 'n', 's', 'm', 'yyyy', 'w', 'ww').
- `my_date` (Union[datetime, str, date]): The date/time to extract from.
- `first_day_of_week` (int, optional): First day of week for 'w' and 'ww'. Defaults to 0 (Monday).
- `first_week_of_year` (int, optional): How first week is determined for 'ww'. Defaults to 1.

**Returns:**
- `int`: The requested part value.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import date_part

dt = datetime(2024, 10, 25, 15, 35, 45)
print(date_part("d", dt))     # 25 (day)
print(date_part("m", dt))     # 10 (month)
print(date_part("yyyy", dt))  # 2024 (year)
print(date_part("h", dt))     # 15 (hour)
```

**Cost:** O(1)

---

### `parts_to_date()`

Creates a date object from year, month, and day components.

**Parameters:**
- `year` (int): The year (e.g., 2025).
- `month` (int): The month (1-12).
- `day` (int): The day (1-31).

**Returns:**
- `date`: A new date object.

**Example:**
```python
from formulite.fxDate.date_operations import parts_to_date

dt = parts_to_date(2025, 10, 30)
print(dt)  # datetime.date(2025, 10, 30)
```

**Cost:** O(1)

---

### `parts_to_datetime()`

Creates a datetime object from its numeric components.

**Parameters:**
- `year` (int): The year.
- `month` (int): The month (1-12).
- `day` (int): The day (1-31).
- `hour` (int, optional): The hour (0-23). Defaults to 0.
- `minute` (int, optional): The minute (0-59). Defaults to 0.
- `second` (int, optional): The second (0-59). Defaults to 0.
- `microsecond` (int, optional): The microsecond (0-999999). Defaults to 0.

**Returns:**
- `datetime`: A new datetime object.

**Example:**
```python
from formulite.fxDate.date_operations import parts_to_datetime

dt = parts_to_datetime(2025, 10, 30, 15, 30, 45)
print(dt)  # datetime.datetime(2025, 10, 30, 15, 30, 45)
```

**Cost:** O(1)

---

### `is_between_dates()`

Checks if a date falls within a date range.

**Parameters:**
- `target_date` (Union[datetime, str]): The date to check.
- `start_date` (Union[datetime, str]): Range start date.
- `end_date` (Union[datetime, str]): Range end date.
- `inclusive` (bool, optional): Include boundaries. Defaults to True.
- `format` (Optional[str]): Date format if using strings.

**Returns:**
- `bool`: True if target_date is within the range.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import is_between_dates

print(is_between_dates(datetime(2025, 6, 15), datetime(2025, 6, 1), datetime(2025, 6, 30)))  # True
print(is_between_dates(datetime(2025, 7, 1), datetime(2025, 6, 1), datetime(2025, 6, 30)))   # False
```

**Cost:** O(1)

---

### `is_valid_time()`

Verifies if hour, minute, second, and microsecond represent a valid time.

**Parameters:**
- `hour` (int): Hour (0-23).
- `minute` (int): Minute (0-59).
- `second` (int, optional): Second (0-59). Defaults to 0.
- `microsecond` (int, optional): Microsecond (0-999999). Defaults to 0.

**Returns:**
- `bool`: True if all components are valid.

**Example:**
```python
from formulite.fxDate.date_operations import is_valid_time

print(is_valid_time(23, 59, 59))  # True
print(is_valid_time(25, 0, 0))    # False (invalid hour)
```

**Cost:** O(1)

---

### `time_from_datetime()`

Extracts the time component from a datetime object.

**Parameters:**
- `datetime_object` (datetime): The datetime object.

**Returns:**
- `time`: Time component.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import time_from_datetime

dt = datetime(2023, 10, 26, 15, 30, 45, 123456)
print(time_from_datetime(dt))  # datetime.time(15, 30, 45, 123456)
```

**Cost:** O(1)

---

### `get_date_component()`

Extracts a specific component (day, month, year, hour, minute, second) from a date.

**Parameters:**
- `date_input` (datetime): The datetime object.
- `component` (Literal["day", "month", "year", "hour", "minute", "second"]): Component to extract.

**Returns:**
- `int`: The requested component value.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_date_component

dt = datetime(2023, 10, 26, 15, 30, 45)
print(get_date_component(dt, "day"))    # 26
print(get_date_component(dt, "month"))  # 10
print(get_date_component(dt, "hour"))   # 15
```

**Cost:** O(1)

---

### `set_date_component()`

Returns a new datetime with specified components modified.

**Parameters:**
- `date_input` (datetime): The original datetime.
- `**kwargs`: Keyword arguments for components to change (year, month, day, hour, etc.).

**Returns:**
- `datetime`: New datetime with modified components.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import set_date_component

dt = datetime(2025, 6, 11, 15, 30, 45)
print(set_date_component(dt, day=1))  # datetime.datetime(2025, 6, 1, 15, 30, 45)
print(set_date_component(dt, hour=0, minute=0, second=0))  # datetime.datetime(2025, 6, 11, 0, 0, 0)
```

**Cost:** O(1)

---

### `is_leap_year()`

Checks if a given year is a leap year.

**Parameters:**
- `year` (int): The year to check.

**Returns:**
- `bool`: True if the year is a leap year.

**Example:**
```python
from formulite.fxDate.date_operations import is_leap_year

print(is_leap_year(2024))  # True
print(is_leap_year(2023))  # False
print(is_leap_year(2000))  # True
print(is_leap_year(1900))  # False
```

**Cost:** O(1)

---

### `get_number_of_days_in_year()`

Calculates the total number of days in a given year.

**Parameters:**
- `year` (int): The year.

**Returns:**
- `int`: 365 or 366 days.

**Example:**
```python
from formulite.fxDate.date_operations import get_number_of_days_in_year

print(get_number_of_days_in_year(2023))  # 365
print(get_number_of_days_in_year(2024))  # 366
```

**Cost:** O(1)

---

### `get_week_range()`

Retrieves the start and end dates (Monday to Sunday) for a specific ISO week.

**Parameters:**
- `year` (int): The year.
- `week_number` (int): ISO week number (1-53).

**Returns:**
- `Tuple[datetime, datetime]`: Start and end dates of the week.

**Example:**
```python
from formulite.fxDate.date_operations import get_week_range

start, end = get_week_range(2025, 24)
print(f"{start} to {end}")  # Week 24 of 2025
```

**Cost:** O(1)

---

### `get_year_calendar_by_weeks()`

Generates a complete list of ISO weeks for a year with their start and end dates.

**Parameters:**
- `year` (int): The calendar year.

**Returns:**
- `List[Tuple[int, datetime, datetime]]`: List of (week_number, start_date, end_date).

**Example:**
```python
from formulite.fxDate.date_operations import get_year_calendar_by_weeks

calendar = get_year_calendar_by_weeks(2023)
print(f"First week: {calendar[0]}")
print(f"Last week: {calendar[-1]}")
print(f"Total weeks: {len(calendar)}")
```

**Cost:** O(1)

---

### `get_quarter()`

Extracts the quarter number (1-4) from a date.

**Parameters:**
- `date_input` (Union[datetime, str]): The date.
- `input_format` (Optional[str]): Format for string input.

**Returns:**
- `int`: Quarter number (1, 2, 3, or 4).

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_quarter

print(get_quarter(datetime(2025, 8, 15)))  # 3 (Q3)
print(get_quarter(datetime(2024, 1, 1)))   # 1 (Q1)
print(get_quarter("2025-08-15", "%Y-%m-%d"))  # 3
```

**Cost:** O(1)

---

### `get_number_of_days_in_quarter()`

Calculates the total days in a specific quarter of a year.

**Parameters:**
- `year` (int): The year.
- `quarter` (int): Quarter number (1-4).

**Returns:**
- `int`: Total days in the quarter.

**Example:**
```python
from formulite.fxDate.date_operations import get_number_of_days_in_quarter

print(get_number_of_days_in_quarter(2024, 1))  # 91 (leap year, Q1)
print(get_number_of_days_in_quarter(2023, 1))  # 90 (Q1)
print(get_number_of_days_in_quarter(2023, 2))  # 91 (Q2)
```

**Cost:** O(1)

---

### `start_of_month()`

Returns the first day of the month for a given date.

**Parameters:**
- `date_input` (Union[datetime, str]): The date.
- `input_format` (str, optional): Format for string input.

**Returns:**
- `datetime`: First day of the month at 00:00:00.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import start_of_month

dt = datetime(2023, 10, 15)
print(start_of_month(dt))  # datetime.datetime(2023, 10, 1, 0, 0)
```

**Cost:** O(1)

---

### `end_of_month()`

Returns the last day of the month for a given date.

**Parameters:**
- `date_input` (Union[datetime, str]): The date.
- `input_format` (str, optional): Format for string input.

**Returns:**
- `datetime`: Last day of the month at 23:59:59.999999.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import end_of_month

dt = datetime(2023, 10, 15)
print(end_of_month(dt))  # datetime.datetime(2023, 10, 31, 23, 59, 59, 999999)
```

**Cost:** O(1)

---

### `start_of_year()`

Returns the first day of the year for a given date.

**Parameters:**
- `date_input` (Union[datetime, str]): The date.
- `input_format` (str, optional): Format for string input.

**Returns:**
- `datetime`: January 1st at 00:00:00.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import start_of_year

dt = datetime(2023, 7, 20)
print(start_of_year(dt))  # datetime.datetime(2023, 1, 1, 0, 0)
```

**Cost:** O(1)

---

### `end_of_year()`

Returns the last day of the year for a given date.

**Parameters:**
- `date_input` (Union[datetime, str]): The date.
- `input_format` (str, optional): Format for string input.

**Returns:**
- `datetime`: December 31st at 23:59:59.999999.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import end_of_year

dt = datetime(2023, 7, 20)
print(end_of_year(dt))  # datetime.datetime(2023, 12, 31, 23, 59, 59, 999999)
```

**Cost:** O(1)

---

### `get_last_friday_of_month()`

Calculates the last Friday of a given month.

**Parameters:**
- `year` (int): The year.
- `month` (int): The month (1-12).

**Returns:**
- `datetime`: Last Friday of the month at midnight.

**Example:**
```python
from formulite.fxDate.date_operations import get_last_friday_of_month

print(get_last_friday_of_month(2023, 10))  # datetime.datetime(2023, 10, 27, 0, 0)
```

**Cost:** O(1)

---

### `get_next_friday()`

Calculates the next upcoming Friday from a given date.

**Parameters:**
- `date_input` (datetime): The starting date.

**Returns:**
- `datetime`: Next Friday at midnight.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_next_friday

dt = datetime(2023, 10, 26)  # Thursday
print(get_next_friday(dt))  # datetime.datetime(2023, 10, 27, 0, 0)
```

**Cost:** O(1)

---

### `get_previous_friday()`

Calculates the immediately preceding Friday from a given date.

**Parameters:**
- `date_input` (datetime): The starting date.

**Returns:**
- `datetime`: Previous Friday at midnight (or same date if it's Friday).

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_previous_friday

dt = datetime(2025, 6, 9)  # Monday
print(get_previous_friday(dt))  # datetime.datetime(2025, 6, 6, 0, 0)
```

**Cost:** O(1)

---

### `get_working_days_in_range()`

Calculates working days (excluding weekends and holidays) within a date range.

**Parameters:**
- `start_date` (datetime): Range start date (inclusive).
- `end_date` (datetime): Range end date (inclusive).
- `holidays` (Optional[List[datetime]]): Optional list of holiday dates to exclude.

**Returns:**
- `int`: Number of working days.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_working_days_in_range

# Monday to Friday (5 working days)
start = datetime(2025, 6, 9)
end = datetime(2025, 6, 13)
print(get_working_days_in_range(start, end))  # 5
```

**Cost:** O(n)

---

### `parse_date_flexible()`

Parses a date string by trying multiple common formats.

**Parameters:**
- `text` (str): The date string to parse.
- `dayfirst` (bool): When ambiguous, treat the first number as the day. Defaults to `True`.

**Returns:**
- `Optional[Union[date, datetime]]`: A `date` or `datetime` object, or `None` if no format matches.

**Example:**
```python
from formulite.fxDate.date_convertions import parse_date_flexible

parse_date_flexible("15/01/2026")   # datetime(2026, 1, 15, 0, 0)
parse_date_flexible("2026-04-04")   # datetime(2026, 4, 4, 0, 0)
```

**Cost:** O(f) where f is the number of formats tried

---

### `date_to_human_short()`

Formats a date as a short human-readable string.

**Parameters:**
- `dt_value` (Union[date, datetime]): The date or datetime to format.
- `language` (str): `"en"` for `"Apr 4, 2026"`, `"es"` for `"4 abr. 2026"`. Defaults to `"en"`.

**Returns:**
- `str`: A short formatted date string.

**Example:**
```python
from datetime import date
from formulite.fxDate.date_convertions import date_to_human_short

date_to_human_short(date(2026, 4, 4), "en")  # 'Apr 4, 2026'
date_to_human_short(date(2026, 4, 4), "es")  # '4 abr. 2026'
```

**Cost:** O(1)

---

### `relative_time_description()`

Returns a human-readable relative time string such as `"2 hours ago"` or `"hace 3 días"`.

**Parameters:**
- `dt_value` (datetime): The target datetime.
- `reference` (Optional[datetime]): The baseline datetime (defaults to `datetime.now()`).
- `language` (str): `"en"` for English, `"es"` for Spanish.

**Returns:**
- `str`: A human-readable relative time string.

**Raises:**
- `TypeError`: If `dt_value` is not a datetime.

**Example:**
```python
from datetime import datetime, timedelta
from formulite.fxDate.date_operations import relative_time_description

ref = datetime(2026, 4, 4, 12, 0)
relative_time_description(ref - timedelta(hours=2), ref)  # '2 hours ago'
```

**Cost:** O(1)

---

### `round_datetime()`

Rounds a datetime to the nearest unit.

**Parameters:**
- `dt_value` (datetime): The datetime to round.
- `unit` (str): `"minute"`, `"hour"` or `"day"`.

**Returns:**
- `datetime`: The rounded datetime.

**Raises:**
- `TypeError`: If `dt_value` is not a datetime.
- `ValueError`: If `unit` is invalid.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import round_datetime

round_datetime(datetime(2026, 4, 4, 14, 35), "hour")  # datetime(2026, 4, 4, 15, 0)
```

**Cost:** O(1)

---

### `recurring_dates()`

Generates recurring dates within a range.

**Parameters:**
- `start` (date): First date of the range (inclusive).
- `end` (date): Last date of the range (inclusive).
- `frequency` (str): One of `"daily"`, `"weekly"`, `"biweekly"`, `"monthly"` or `"yearly"`.
- `weekday` (Optional[int]): For `"weekly"`/`"biweekly"` — ISO weekday (1=Monday ... 7=Sunday). Defaults to the weekday of `start`.

**Returns:**
- `List[date]`: A sorted list of dates matching the recurrence rule.

**Raises:**
- `ValueError`: If `start` > `end` or frequency is invalid.

**Example:**
```python
from datetime import date
from formulite.fxDate.date_operations import recurring_dates

recurring_dates(date(2026, 1, 1), date(2026, 3, 1), "monthly")
# [date(2026, 1, 1), date(2026, 2, 1), date(2026, 3, 1)]
```

**Cost:** O(n) where n is the number of occurrences

---

### `business_hours_between()`

Calculates the number of business hours between two datetimes. Counts only Mon–Fri hours within the `[work_start, work_end)` window.

**Parameters:**
- `start_dt` (datetime): Start datetime.
- `end_dt` (datetime): End datetime.
- `work_start` (time): Daily work-start time (default 09:00).
- `work_end` (time): Daily work-end time (default 17:00).

**Returns:**
- `float`: Total business hours.

**Raises:**
- `ValueError`: If `start_dt` > `end_dt` or `work_start` >= `work_end`.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import business_hours_between

business_hours_between(
    datetime(2026, 4, 6, 10, 0),
    datetime(2026, 4, 6, 15, 30))  # 5.5
```

**Cost:** O(d) where d is the number of calendar days spanned

# Monday to Friday (5 working days)
print(get_working_days_in_range(datetime(2025, 6, 9), datetime(2025, 6, 13)))  # 5

# With holidays
holidays = [datetime(2025, 6, 10), datetime(2025, 6, 12)]
print(get_working_days_in_range(datetime(2025, 6, 9), datetime(2025, 6, 13), holidays))  # 3
```

**Cost:** O(1)

---

### `get_first_business_day_of_month()`

Returns the first working day of a month.

**Parameters:**
- `year` (int): The year.
- `month` (int): The month (1-12).
- `holidays` (Optional[List[datetime]]): Optional holiday list.

**Returns:**
- `datetime`: First business day at midnight.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_first_business_day_of_month

print(get_first_business_day_of_month(2025, 1))  # datetime.datetime(2025, 1, 1, 0, 0)

holidays = [datetime(2025, 12, 1), datetime(2025, 12, 2)]
print(get_first_business_day_of_month(2025, 12, holidays))  # datetime.datetime(2025, 12, 3, 0, 0)
```

**Cost:** O(1)

---

### `get_last_business_day_of_month()`

Returns the last working day of a month.

**Parameters:**
- `year` (int): The year.
- `month` (int): The month (1-12).
- `holidays` (Optional[List[datetime]]): Optional holiday list.

**Returns:**
- `datetime`: Last business day at midnight.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_last_business_day_of_month

print(get_last_business_day_of_month(2025, 6))  # datetime.datetime(2025, 6, 30, 0, 0)

holidays = [datetime(2025, 1, 31)]
print(get_last_business_day_of_month(2025, 1, holidays))  # datetime.datetime(2025, 1, 30, 0, 0)
```

**Cost:** O(1)

---

### `is_working_day()`

Checks if a date is a working day (Monday-Friday).

**Parameters:**
- `date_input` (Union[datetime, str]): The date to check.
- `input_format` (str, optional): Format for string input.
- `system` (Literal['european', 'anglo'], optional): Week numbering system. Defaults to 'european'.

**Returns:**
- `bool`: True if it's a working day.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import is_working_day

dt_monday = datetime(2025, 6, 9)
dt_saturday = datetime(2025, 6, 14)
print(is_working_day(dt_monday))    # True
print(is_working_day(dt_saturday))  # False
```

**Cost:** O(1)

---

### `is_weekend()`

Determines if a date is Saturday or Sunday.

**Parameters:**
- `date_input` (Union[datetime, str]): The date to check.
- `input_format` (str, optional): Format for string input.
- `language` (str, optional): Language code. Defaults to 'en'.

**Returns:**
- `bool`: True if it's a weekend.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import is_weekend

dt_saturday = datetime(2023, 10, 28)
dt_friday = datetime(2023, 10, 27)
print(is_weekend(dt_saturday))  # True
print(is_weekend(dt_friday))    # False
```

**Cost:** O(1)

---

### `get_age_from_dob()`

Calculates age in full years from a date of birth.

**Parameters:**
- `dob` (Union[datetime, str]): Date of birth.
- `dob_format` (str, optional): Format for string DOB.
- `as_of_date` (Optional[datetime], optional): Reference date. Defaults to current date.

**Returns:**
- `int`: Age in complete years.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_age_from_dob

dob = datetime(1990, 6, 11)
print(get_age_from_dob(dob, as_of_date=datetime(2025, 6, 11)))  # 35
print(get_age_from_dob("1985-03-20", dob_format="%Y-%m-%d", as_of_date=datetime(2025, 6, 11)))  # 40
```

**Cost:** O(1)

---

### `get_season()`

Returns the season of the year for a given date.

**Parameters:**
- `date_input` (Union[datetime, str]): The date.
- `hemisphere` (str, optional): 'northern' or 'southern'. Defaults to 'northern'.
- `lang` (str, optional): Language code. Defaults to 'en'.
- `format` (Optional[str]): Format for string input.

**Returns:**
- `str`: Season name in specified language.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_season

print(get_season(datetime(2025, 6, 11), 'northern', lang='en'))  # 'Summer'
print(get_season(datetime(2025, 6, 11), 'southern', lang='es'))  # 'Invierno'
```

**Cost:** O(1)

---

### `format_datetime_ampm()`

Formats a datetime into 12-hour (AM/PM) string representation.

**Parameters:**
- `dt_object` (datetime): The datetime to format.

**Returns:**
- `str`: Formatted string 'YYYY-MM-DD HH:MM:SS AM/PM'.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import format_datetime_ampm

dt = datetime(2025, 6, 29, 15, 30, 0)
print(format_datetime_ampm(dt))  # '2025-06-29 03:30:00 PM'
```

**Cost:** O(1)

---

### `timedelta_to_components()`

Converts a timedelta object into a dictionary of its components.

**Parameters:**
- `timedelta_obj` (timedelta): The timedelta to convert.

**Returns:**
- `Dict[str, Union[int, float]]`: Dictionary with 'days', 'hours', 'minutes', 'seconds', 'microseconds'.

**Example:**
```python
from datetime import datetime, timedelta
from formulite.fxDate.date_operations import timedelta_to_components

dt_future = datetime(2025, 6, 12, 10, 0, 0)
dt_past = datetime(2025, 6, 11, 8, 30, 0)
td = dt_future - dt_past
print(timedelta_to_components(td))  # {'days': 1, 'hours': 1, 'minutes': 30, 'seconds': 0, 'microseconds': 0}
```

**Cost:** O(1)

---

### `intersection_of_date_ranges()`

Returns the intersection period if two date ranges overlap, None otherwise.

**Parameters:**
- `start1` (datetime): First range start.
- `end1` (datetime): First range end.
- `start2` (datetime): Second range start.
- `end2` (datetime): Second range end.

**Returns:**
- `Optional[Tuple[datetime, datetime]]`: Intersection range or None.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import intersection_of_date_ranges

r1_start = datetime(2025, 6, 10)
r1_end = datetime(2025, 6, 15)
r2_start = datetime(2025, 6, 13)
r2_end = datetime(2025, 6, 18)
print(intersection_of_date_ranges(r1_start, r1_end, r2_start, r2_end))
# (datetime.datetime(2025, 6, 13, 0, 0), datetime.datetime(2025, 6, 15, 0, 0))
```

**Cost:** O(1)

---

### `dates_between()`

Generates a list of all dates between two dates, inclusive.

**Parameters:**
- `start_date` (datetime.date): Initial date.
- `end_date` (datetime.date): Final date.

**Returns:**
- `list[datetime.date]`: List of all dates in the range.

**Example:**
```python
from datetime import date
from formulite.fxDate.date_operations import dates_between

start = date(2023, 1, 1)
end = date(2023, 1, 5)
print(dates_between(start, end))
# [datetime.date(2023, 1, 1), ..., datetime.date(2023, 1, 5)]
```

**Cost:** O(1)

---

### `date_intervals()`

Generates a list of date intervals for a specific granularity.

**Parameters:**
- `start_date` (Union[datetime, str]): Range start date.
- `end_date` (Union[datetime, str]): Range end date.
- `granularity` (str): Unit ('year', 'quarter', 'month', 'half_month', 'week', 'day', 'hour', 'minute', 'second').
- `input_format` (Optional[str]): Format for string dates.

**Returns:**
- `List[Tuple[datetime, datetime]]`: List of (interval_start, interval_end) tuples.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import date_intervals

intervals = date_intervals(datetime(2025, 6, 1), datetime(2025, 6, 3), 'day')
for start, end in intervals:
    print(f"{start} to {end}")
```

**Cost:** O(1)

---

### `add_microseconds()`

Adds or subtracts microseconds to/from a datetime.

**Parameters:**
- `date_input` (datetime): The original datetime.
- `microseconds` (int): Microseconds to add (positive) or subtract (negative).

**Returns:**
- `datetime`: New datetime with adjusted microseconds.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import add_microseconds

dt = datetime(2025, 6, 11, 10, 0, 0, 100)
print(add_microseconds(dt, 50))  # datetime.datetime(2025, 6, 11, 10, 0, 0, 150)
```

**Cost:** O(1)

---

### `set_microseconds()`

Sets the microseconds of a datetime to a specific value.

**Parameters:**
- `date_input` (datetime): The original datetime.
- `microseconds` (int): Microseconds value (0-999999).

**Returns:**
- `datetime`: New datetime with set microseconds.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import set_microseconds

dt = datetime(2025, 6, 11, 10, 0, 0, 123456)
print(set_microseconds(dt, 789))  # datetime.datetime(2025, 6, 11, 10, 0, 0, 789)
```

**Cost:** O(1)

---

### `is_duration_less_than()`

Checks if the duration between two dates is less than a threshold.

**Parameters:**
- `start_date` (datetime): Start date.
- `end_date` (datetime): End date.
- `threshold_duration` (timedelta): Duration threshold.

**Returns:**
- `bool`: True if duration is strictly less than threshold.

**Example:**
```python
from datetime import datetime, timedelta
from formulite.fxDate.date_operations import is_duration_less_than

print(is_duration_less_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 20), timedelta(minutes=30)))  # True
```

**Cost:** O(1)

---

### `is_duration_greater_than()`

Checks if the duration between two dates is greater than a threshold.

**Parameters:**
- `start_date` (datetime): Start date.
- `end_date` (datetime): End date.
- `threshold_duration` (timedelta): Duration threshold.

**Returns:**
- `bool`: True if duration is strictly greater than threshold.

**Example:**
```python
from datetime import datetime, timedelta
from formulite.fxDate.date_operations import is_duration_greater_than

print(is_duration_greater_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 45), timedelta(minutes=30)))  # True
```

**Cost:** O(1)

---

### `full_years_between()`

Returns the number of complete years between two dates.

**Parameters:**
- `start_date` (datetime): Start date.
- `end_date` (datetime): End date.

**Returns:**
- `int`: Complete years (negative if start > end).

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import full_years_between

print(full_years_between(datetime(2020, 6, 11), datetime(2025, 6, 11)))  # 5
print(full_years_between(datetime(2020, 6, 11), datetime(2025, 6, 10)))  # 4
```

**Cost:** O(1)

---

### `full_months_between()`

Returns the number of complete months between two dates.

**Parameters:**
- `start_date` (datetime): Start date.
- `end_date` (datetime): End date.

**Returns:**
- `int`: Complete months (negative if start > end).

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import full_months_between

print(full_months_between(datetime(2025, 1, 15), datetime(2025, 3, 15)))  # 2
print(full_months_between(datetime(2025, 1, 15), datetime(2025, 3, 14)))  # 1
```

**Cost:** O(1)

---

### `generate_random_date()`

Generates a random date within a specified range.

**Parameters:**
- `start_date` (Optional[date]): Earliest date. Defaults to 1900-01-01.
- `end_date` (Optional[date]): Latest date. Defaults to 2100-12-31.
- `business_days_only` (bool, optional): Only business days. Defaults to False.

**Returns:**
- `date`: A random date.

**Example:**
```python
from datetime import date
from formulite.fxDate.date_operations import generate_random_date

random_date = generate_random_date(start_date=date(2020, 1, 1), end_date=date(2025, 12, 31))
print(random_date)
```

**Cost:** O(1)

---

### `generate_random_time()`

Generates a random time within an optional range.

**Parameters:**
- `min_time` (Optional[time]): Earliest time. Defaults to 00:00:00.
- `max_time` (Optional[time]): Latest time. Defaults to 23:59:59.999999.

**Returns:**
- `time`: A random time.

**Example:**
```python
from datetime import time
from formulite.fxDate.date_operations import generate_random_time

random_time = generate_random_time(min_time=time(9, 0, 0), max_time=time(17, 0, 0))
print(random_time)
```

**Cost:** O(1)

---

### `generate_random_datetime()`

Generates a random datetime within a range, optionally localized.

**Parameters:**
- `start_dt` (Optional[datetime]): Earliest datetime. Defaults to 1900-01-01 UTC.
- `end_dt` (Optional[datetime]): Latest datetime. Defaults to 2100-12-31 UTC.
- `tz_info` (Optional[str]): IANA timezone string.

**Returns:**
- `datetime`: A random datetime.

**Example:**
```python
from datetime import datetime, timezone
from formulite.fxDate.date_operations import generate_random_datetime

random_dt = generate_random_datetime(start_dt=datetime.now(timezone.utc), 
                                      end_dt=datetime(2026, 12, 31, tzinfo=timezone.utc), 
                                      tz_info='UTC')
print(random_dt)
```

**Cost:** O(1)

---

### `get_week_of_year()`

Returns the ISO week number of the year for a given date.

**Parameters:**
- `date_input` (datetime): The datetime object.

**Returns:**
- `int`: ISO week number (1-53).

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import get_week_of_year

print(get_week_of_year(datetime(2025, 6, 11)))  # 24
```

**Cost:** O(1)

---

### `week_of_month()`

Returns the week number of the month for a given date.

**Parameters:**
- `date_input` (datetime): The date.
- `start_of_week` (int, optional): Week start day (0=Monday). Defaults to 0.

**Returns:**
- `int`: Week number of the month (1-6).

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import week_of_month

dt = datetime(2025, 6, 11)
print(week_of_month(dt))  # 2
```

**Cost:** O(1)

---

### `filter_dates_by_weekday()`

Filters a list of dates, returning only those on a specific weekday.

**Parameters:**
- `dates` (List[datetime]): List of datetime objects.
- `weekday` (int): Weekday to filter (0=Monday, 6=Sunday).

**Returns:**
- `List[datetime]`: Filtered list.

**Example:**
```python
from datetime import datetime
from formulite.fxDate.date_operations import filter_dates_by_weekday

dates = [datetime(2025, 6, 9), datetime(2025, 6, 10), datetime(2025, 6, 16)]
monday_dates = filter_dates_by_weekday(dates, 0)  # Filter Mondays
print(monday_dates)  # [datetime.datetime(2025, 6, 9, 0, 0), datetime.datetime(2025, 6, 16, 0, 0)]
```

**Cost:** O(1)

---

## Evaluations

### `is_dateclass()`

Checks if an object is of datetime type.

**Parameters:**
- `p_datetime`: The object to check.

**Returns:**
- `bool`: True if it's datetime, False otherwise.

**Ejemplo:**
```python
from datetime import datetime
from formulite.fxDate.date_evaluations import is_dateclass

print(is_dateclass(datetime.now()))  # True
print(is_dateclass("2025-01-01"))  # False
```

**Cost:** O(1)

---

## Additional Notes

### Timezone Considerations

Many functions in the fxDate module are more robust when using timezone-aware datetime objects (especially in UTC). This prevents ambiguity problems and ensures correct conversions.

```python
from datetime import datetime, timezone

# Recommended: timezone-aware datetime in UTC
dt_utc = datetime(2023, 1, 1, 0, 0, 0, tzinfo=timezone.utc)

# Less recommended: naive datetime (can cause ambiguity)
dt_naive = datetime(2023, 1, 1, 0, 0, 0)
```

### Locale Dependencies

Some functions like `weekday_name()` depend on locales installed on the operating system. If a language is not available, a `ValueError` will be raised. To check available locales:

- **Linux/macOS:** `locale -a`
- **Windows:** Control Panel → Region

### Excel Compatibility

Functions with the `excel_` prefix or names like `DIAS`, `FECHA_MES`, etc., are designed to emulate Excel's behavior, including:
- Serial number system (days since 1899-12-30)
- 30/360 calculation methods
- Working day functions with weekend customization

---

### `unix_timestamp_to_datetime()`

Converts a UNIX timestamp (seconds since the Epoch) to a datetime object.

**Parameters:**
- `timestamp` (Union[int, float]): The UNIX timestamp.
- `tz_info` (Optional[str]): An IANA timezone string (e.g., 'America/New_York'). If provided, the datetime will be "aware" (with timezone).

**Returns:**
- `datetime`: The resulting datetime object.

**Example:**
```python
from formulite.fxDate.date_convertions import unix_timestamp_to_datetime

unix_timestamp_to_datetime(1718092025.0, tz_info='UTC')
# datetime.datetime(2025, 6, 11, 10, 27, 5, tzinfo=datetime.timezone.utc)
```

**Cost:** O(1)

---

### `days_360()`

Calculates days between two dates based on a 360-day year (12 months of 30 days). Commonly used in financial calculations such as bond pricing and interest accrual.

**Parameters:**
- `start_date` (datetime): The start date.
- `end_date` (datetime): The end date.
- `method` (str, optional): Calculation method — `'us'` for US/NASD or `'eu'` for European. Defaults to `'us'`.

**Returns:**
- `int`: Number of days based on the 360-day year convention.

**Example:**
```python
from formulite.fxDate.date_operations import days_360

days_360(datetime(2025, 1, 1), datetime(2025, 7, 1))   # 180
days_360(datetime(2025, 1, 30), datetime(2025, 2, 28))  # 28
days_360(datetime(2025, 1, 31), datetime(2025, 2, 28), method='eu')  # 28
```

**Cost:** O(1)

---

### `network_days_intl()`

Calculates working days between two dates with a custom weekend definition. Extension of `get_working_days_in_range` that allows specifying which days are considered weekends.

**Parameters:**
- `start_date` (datetime): The start date (inclusive).
- `end_date` (datetime): The end date (inclusive).
- `weekend` (Union[int, str], optional): Weekend definition. Integer presets: 1 = Sat-Sun (default), 2 = Sun-Mon, 3 = Mon-Tue, 4 = Tue-Wed, 5 = Wed-Thu, 6 = Thu-Fri, 7 = Fri-Sat. Or a 7-char string of `'0'`/`'1'` (Mon-Sun), where `'1'` = weekend day.
- `holidays` (Optional[List[datetime]], optional): List of holiday dates to exclude.

**Returns:**
- `int`: Number of working days.

**Example:**
```python
from formulite.fxDate.date_operations import network_days_intl

network_days_intl(datetime(2025, 1, 6), datetime(2025, 1, 10))              # 5
network_days_intl(datetime(2025, 1, 6), datetime(2025, 1, 10), weekend=2)   # 4 (Sun-Mon off)
network_days_intl(datetime(2025, 1, 6), datetime(2025, 1, 12), weekend='0000011')  # 5
```

**Cost:** O(n) where n is the number of days in the range

---

### `workday()`

Returns the date after a given number of working days (Monday-Friday), skipping weekends and optional holidays. The start date itself is not counted.

**Parameters:**
- `start_date` (datetime): The starting date.
- `days` (int): Number of working days to advance (positive) or go back (negative).
- `holidays` (Optional[List[datetime]], optional): List of holiday dates to skip.

**Returns:**
- `datetime`: The resulting date.

**Example:**
```python
from formulite.fxDate.date_operations import workday

workday(datetime(2025, 1, 6), 5)   # datetime(2025, 1, 13) — Mon + 5 working days
workday(datetime(2025, 1, 6), -1)  # datetime(2025, 1, 3)  — previous Friday
```

**Cost:** O(n) where n is abs(days)

---

### `workday_intl()`

Returns the date after a given number of working days with a custom weekend definition.

**Parameters:**
- `start_date` (datetime): The starting date.
- `days` (int): Number of working days to advance (positive) or go back (negative).
- `weekend` (Union[int, str], optional): Weekend definition (see `network_days_intl` for details). Defaults to 1 (Sat-Sun).
- `holidays` (Optional[List[datetime]], optional): List of holiday dates to skip.

**Returns:**
- `datetime`: The resulting date.

**Example:**
```python
from formulite.fxDate.date_operations import workday_intl

workday_intl(datetime(2025, 1, 6), 5, weekend=2)  # datetime(2025, 1, 11) — Sun-Mon off
```

**Cost:** O(n) where n is abs(days)

---

### `year_fraction()`

Calculates the fraction of year between two dates. Useful for financial calculations such as bond accrued interest or prorated payments.

**Parameters:**
- `start_date` (datetime): The start date.
- `end_date` (datetime): The end date.
- `basis` (int, optional): Day-count basis. `0` = US 30/360 (default), `1` = Actual/Actual.

**Returns:**
- `float`: Fraction of the year between the dates.

**Example:**
```python
from formulite.fxDate.date_operations import year_fraction

year_fraction(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=0)  # 0.5
year_fraction(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=1)  # ~0.4959
```

**Cost:** O(1)

---

### `week_number()`

Returns the week number of the year for a given date.

**Parameters:**
- `date_input` (datetime): The date to evaluate.
- `system` (int, optional): `1` = week begins on Sunday (default), `21` = ISO week number.

**Returns:**
- `int`: Week number (1-53).

**Example:**
```python
from formulite.fxDate.date_operations import week_number

week_number(datetime(2025, 1, 1))             # 1
week_number(datetime(2025, 1, 1), system=21)  # 1 (ISO)
```

**Cost:** O(1)

---

### `iso_week_number()`

Returns the ISO 8601 week number for a given date. Week 1 is the week containing the first Thursday of the year.

**Parameters:**
- `date_input` (datetime): The date to evaluate.

**Returns:**
- `int`: ISO week number (1-53).

**Example:**
```python
from formulite.fxDate.date_operations import iso_week_number

iso_week_number(datetime(2025, 1, 1))   # 1
iso_week_number(datetime(2025, 6, 15))  # 24
```

**Cost:** O(1)

---

### `quarters_between_dates()`

Calculates the number of complete quarters between two dates.

**Parameters:**
- `start_date` (datetime): The start date.
- `end_date` (datetime): The end date.

**Returns:**
- `int`: Number of quarters (positive if end > start, negative otherwise).

**Example:**
```python
from formulite.fxDate.date_operations import quarters_between_dates

quarters_between_dates(datetime(2025, 1, 1), datetime(2025, 10, 1))   # 3
quarters_between_dates(datetime(2025, 1, 15), datetime(2025, 4, 14))  # 0
```

**Cost:** O(1)

---

### `seconds_since_midnight()`

Returns the number of seconds elapsed since midnight of the current day. Equivalent to VBA's `Timer` function.

**Parameters:**
- None.

**Returns:**
- `float`: Seconds (with fractional microseconds) since 00:00:00 today.

**Example:**
```python
from formulite.fxDate.date_sys import seconds_since_midnight

secs = seconds_since_midnight()
print(secs)  # e.g. 52200.5
```

**Cost:** O(1)

---

### `add_months()`

Shifts a date forward or backward by a given number of months. Preserves the day-of-month when possible; clamps to the last day of the target month if it has fewer days.

**Parameters:**
- `date_input` (datetime): The starting date.
- `months` (int): Number of months to add (positive) or subtract (negative).

**Returns:**
- `datetime`: The resulting date with time components preserved.

**Example:**
```python
from formulite.fxDate.date_operations import add_months

add_months(datetime(2025, 1, 31), 1)   # datetime(2025, 2, 28) — clamped
add_months(datetime(2025, 3, 15), -1)  # datetime(2025, 2, 15)
add_months(datetime(2024, 1, 31), 1)   # datetime(2024, 2, 29) — leap year
```

**Cost:** O(1)

---

### `end_of_month_offset()`

Returns the last day of the month that is N months from the reference date. Useful for calculating payment due dates, contract expirations, or any scenario requiring the last calendar day of a future/past month.

**Parameters:**
- `date_input` (datetime): The reference date.
- `months` (int): Number of months to offset (positive = forward, negative = back).

**Returns:**
- `datetime`: A datetime set to the last day of the target month at 23:59:59.999999.

**Example:**
```python
from formulite.fxDate.date_operations import end_of_month_offset

end_of_month_offset(datetime(2025, 1, 15), 0)   # datetime(2025, 1, 31, 23, 59, 59, 999999)
end_of_month_offset(datetime(2025, 1, 15), 1)   # datetime(2025, 2, 28, 23, 59, 59, 999999)
end_of_month_offset(datetime(2024, 1, 15), 1)   # datetime(2024, 2, 29, 23, 59, 59, 999999)
end_of_month_offset(datetime(2025, 3, 10), -1)  # datetime(2025, 2, 28, 23, 59, 59, 999999)
```

**Cost:** O(1)

---

### `add_years()`

Shifts a date forward or backward by a given number of years.

**Parameters:**
- date_input: The starting datetime.
- years: Number of years to add (positive) or subtract (negative).

**Returns:**
- datetime: The resulting date with time components preserved.

**Raises:**
- TypeError: If *date_input* is not a datetime or *years* is not an int.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import add_years

result = add_years(...)
```

---

### `age()`

Calculates the age in complete years from a birth date to today.

**Parameters:**
- birthdate: A date, datetime, or parseable date string.

**Returns:**
- The number of complete years elapsed.

**Raises:**
- TypeError: If birthdate cannot be interpreted as a date.
- ValueError: If birthdate is in the future.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import age

result = age(...)
```

---

### `current_first_day_of_month()`

Returns the first day of the current month at midnight.

**Returns:**
- datetime: First day of the current month at 00:00:00.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_first_day_of_month

result = current_first_day_of_month(...)
```

---

### `current_is_leap_year()`

Checks if the current year is a leap year.

**Returns:**
- bool: True if the current year is a leap year, False otherwise.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_is_leap_year

result = current_is_leap_year(...)
```

---

### `current_quarter()`

Returns the current quarter of the year (1-4).

**Returns:**
- int: Quarter number (1 for Jan-Mar, 4 for Oct-Dec).

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_quarter

result = current_quarter(...)
```

---

### `current_season()`

Returns the current season of the year.

**Parameters:**
- hemisphere: ``'northern'`` or ``'southern'``. Defaults to ``'northern'``.
- lang: Two-letter ISO 639-1 language code. Defaults to ``'en'``.

**Returns:**
- str: Season name (e.g. ``'Spring'``, ``'Primavera'``).

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_season

result = current_season(...)
```

---

### `current_week_number()`

Returns the current ISO week number (1-53).

**Returns:**
- int: ISO 8601 week number.

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_week_number

result = current_week_number(...)
```

---

### `date_range()`

Generates a list of dates between *start* and *end* at regular intervals.

**Parameters:**
- start: Start date (inclusive). Accepts datetime, date, or ISO string.
- end: End date (inclusive). Accepts datetime, date, or ISO string.
- step: Number of *unit* between each generated date. Must be positive.
- unit: Time unit for the step. Supported: 'days', 'weeks', 'hours',
- 'minutes', 'seconds'.

**Returns:**
- List of datetime objects from *start* up to (and including) *end*.

**Raises:**
- TypeError: If inputs cannot be converted to datetime.
- ValueError: If *step* < 1 or *unit* is unsupported.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import date_range

result = date_range(...)
```

---

### `date_to_excel_serial()`

Convert a Python date to an Excel serial date number.

**Parameters:**
- date_input: Date or datetime to convert.

**Returns:**
- Excel serial day number.

**Ejemplo:**
```python
from formulite.fxDate.date_convertions import date_to_excel_serial

result = date_to_excel_serial(...)
```

---

### `datedif()`

Calculates the difference between two dates in specified units.

**Parameters:**
- start_date: The earlier date.
- end_date: The later date.
- unit: One of "Y", "M", "D", "YM", "MD", "YD".

**Returns:**
- int: The difference in the requested unit.

**Raises:**
- TypeError: If dates are not date/datetime objects.
- ValueError: If start_date > end_date or unit is invalid.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import datedif

result = datedif(...)
```

---

### `datetime_to_cron()`

Convert a datetime to a cron schedule expression.

**Parameters:**
- dt_input: Datetime (or date, which defaults to midnight).

**Returns:**
- Cron expression string ``"minute hour day month *"``.

**Ejemplo:**
```python
from formulite.fxDate.date_convertions import datetime_to_cron

result = datetime_to_cron(...)
```

---

### `datetime_to_rfc2822()`

Format a datetime as an RFC 2822 string (email header format).

**Parameters:**
- dt_input: Datetime or date to format.

**Returns:**
- RFC 2822 formatted string (e.g. ``"Sun, 15 Jun 2025 14:30:00 +0000"``).

**Ejemplo:**
```python
from formulite.fxDate.date_convertions import datetime_to_rfc2822

result = datetime_to_rfc2822(...)
```

---

### `easter_date()`

Computes the date of Easter Sunday for a given year.

**Parameters:**
- year: The calendar year (e.g. 2025).

**Returns:**
- A ``date`` object for Easter Sunday.

**Raises:**
- TypeError: If *year* is not an integer.
- ValueError: If *year* < 1.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import easter_date

result = easter_date(...)
```

---

### `end_of_quarter()`

Returns the last day of the quarter for a given date.

**Parameters:**
- date_input: The date for which to get the end of the quarter.
- input_format: Format string if date_input is a string.

**Returns:**
- datetime: Last day of the quarter at 23:59:59.999999.

**Raises:**
- TypeError: If date_input is not a datetime or string.
- ValueError: If date_input is a string and input_format is not provided.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import end_of_quarter

result = end_of_quarter(...)
```

---

### `excel_serial_to_date()`

Convert an Excel serial date number to a Python date.

**Parameters:**
- serial: Excel serial day number (>= 1).

**Returns:**
- Corresponding Python date object.

**Raises:**
- ValueError: If serial < 1 or serial == 60 (non-existent Feb 29 1900).

**Ejemplo:**
```python
from formulite.fxDate.date_convertions import excel_serial_to_date

result = excel_serial_to_date(...)
```

---

### `human_readable_duration()`

Format a number of seconds as a human-readable duration string.

**Parameters:**
- seconds: Total seconds (can be float for sub-second precision).

**Returns:**
- Human-readable duration string.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import human_readable_duration

result = human_readable_duration(...)
```

---

### `integer_to_datetime()`

Converts a YYYYMMDD integer back to a datetime object.

**Parameters:**
- yyyymmdd: Date encoded as integer (e.g. 20260103 → 2026-01-03).

**Returns:**
- datetime: The parsed date at 00:00:00.

**Raises:**
- TypeError: If *yyyymmdd* is not an integer.
- ValueError: If the integer does not represent a valid date.

**Ejemplo:**
```python
from formulite.fxDate.date_convertions import integer_to_datetime

result = integer_to_datetime(...)
```

---

### `is_business_hours()`

Checks if a datetime falls within business hours on a weekday.

**Parameters:**
- dt: The datetime to evaluate.
- start_hour: Opening hour in 24-h format (default 9).
- end_hour: Closing hour in 24-h format (default 17).

**Returns:**
- True if dt is within business hours, False otherwise.

**Raises:**
- TypeError: If dt is not a datetime object.

**Ejemplo:**
```python
from formulite.fxDate.date_evaluations import is_business_hours

result = is_business_hours(...)
```

---

### `is_future()`

Checks if a date is strictly in the future.

**Parameters:**
- date_input: The date or datetime to evaluate.

**Returns:**
- bool: True if the date is in the future, False otherwise.

**Raises:**
- TypeError: If *date_input* is not a date or datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_evaluations import is_future

result = is_future(...)
```

---

### `is_past()`

Checks if a date is strictly in the past.

**Parameters:**
- date_input: The date or datetime to evaluate.

**Returns:**
- bool: True if the date is in the past, False otherwise.

**Raises:**
- TypeError: If *date_input* is not a date or datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_evaluations import is_past

result = is_past(...)
```

---

### `is_same_business_day()`

Check whether two dates fall on the same business day.

**Parameters:**
- date1: First date.
- date2: Second date.
- holidays: Optional list of holiday dates.

**Returns:**
- True if both dates share the same business day.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import is_same_business_day

result = is_same_business_day(...)
```

---

### `is_same_day()`

Checks if two dates fall on the same calendar day.

**Parameters:**
- date1: First date or datetime.
- date2: Second date or datetime.

**Returns:**
- bool: True if both dates share the same year, month, and day.

**Raises:**
- TypeError: If either argument is not a date or datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_evaluations import is_same_day

result = is_same_day(...)
```

---

### `is_same_month()`

Checks if two dates fall in the same month and year.

**Parameters:**
- date1: First date or datetime.
- date2: Second date or datetime.

**Returns:**
- bool: True if both dates share the same year and month.

**Raises:**
- TypeError: If either argument is not a date or datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_evaluations import is_same_month

result = is_same_month(...)
```

---

### `is_same_quarter()`

Checks if two dates fall in the same quarter and year.

**Parameters:**
- date1: First date or datetime.
- date2: Second date or datetime.

**Returns:**
- bool: True if both dates share the same year and quarter (Q1-Q4).

**Raises:**
- TypeError: If either argument is not a date or datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_evaluations import is_same_quarter

result = is_same_quarter(...)
```

---

### `is_same_week()`

Checks if two dates fall in the same ISO week and year.

**Parameters:**
- date1: First date or datetime.
- date2: Second date or datetime.

**Returns:**
- bool: True if both dates share the same ISO year and week number.

**Raises:**
- TypeError: If either argument is not a date or datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_evaluations import is_same_week

result = is_same_week(...)
```

---

### `is_same_year()`

Checks if two dates fall in the same year.

**Parameters:**
- date1: First date or datetime.
- date2: Second date or datetime.

**Returns:**
- bool: True if both dates share the same year.

**Raises:**
- TypeError: If either argument is not a date or datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_evaluations import is_same_year

result = is_same_year(...)
```

---

### `is_today()`

Checks if a date falls on today's calendar date.

**Parameters:**
- date_input: The date or datetime to evaluate.

**Returns:**
- bool: True if the date is today, False otherwise.

**Raises:**
- TypeError: If *date_input* is not a date or datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_evaluations import is_today

result = is_today(...)
```

---

### `last_day_of_month()`

Returns the last day of the month for a given date.

**Parameters:**
- date_input: A datetime object or date string.
- input_format: Format string when *date_input* is a string.

**Returns:**
- datetime: Last day of the month at end-of-day (23:59:59.999999).

**Ejemplo:**
```python
from formulite.fxDate.date_operations import last_day_of_month

result = last_day_of_month(...)
```

---

### `last_weekday_of_month()`

Returns the last occurrence of a specific weekday in the month of a given date.

**Parameters:**
- date_input: Any date within the target month.
- target_weekday: Weekday as integer (0=Monday … 6=Sunday).

**Returns:**
- datetime: The last matching weekday of the month at midnight.

**Raises:**
- TypeError: If *date_input* is not a datetime object.
- ValueError: If *target_weekday* is not in 0‑6.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import last_weekday_of_month

result = last_weekday_of_month(...)
```

---

### `networkdays()`

Counts working days (Mon-Fri) between two dates, excluding holidays.

**Parameters:**
- start_date: The start date.
- end_date: The end date.
- holidays: Optional list of holiday dates to exclude.

**Returns:**
- int: Number of working days.

**Raises:**
- TypeError: If dates are not date/datetime objects.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import networkdays

result = networkdays(...)
```

---

### `next_business_day()`

Returns the next business day (Mon-Fri) after the given date.

**Parameters:**
- date_input: The reference date.
- holidays: Optional list of holiday datetimes to skip.

**Returns:**
- datetime: The next working day.

**Raises:**
- TypeError: If date_input is not a datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import next_business_day

result = next_business_day(...)
```

---

### `next_weekday()`

Returns the next occurrence of a specific weekday after a given date.

**Parameters:**
- date_input: The starting date.
- target_weekday: Weekday as integer (0=Monday … 6=Sunday). Constants
- from the ``calendar`` module (e.g. ``calendar.FRIDAY``)
- are accepted.

**Returns:**
- datetime: The next occurrence at midnight.

**Raises:**
- TypeError: If *date_input* is not a datetime object.
- ValueError: If *target_weekday* is not in 0‑6.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import next_weekday

result = next_weekday(...)
```

---

### `overlap_dates()`

Checks whether two date ranges overlap.

**Parameters:**
- start1: Start of the first range.
- end1: End of the first range.
- start2: Start of the second range.
- end2: End of the second range.

**Returns:**
- True if the ranges share at least one common day.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import overlap_dates

result = overlap_dates(...)
```

---

### `overlap_days()`

Counts the overlapping days between two date ranges.

**Parameters:**
- start1: Start of the first range.
- end1: End of the first range.
- start2: Start of the second range.
- end2: End of the second range.

**Returns:**
- Number of overlapping days (0 if no overlap).

**Ejemplo:**
```python
from formulite.fxDate.date_operations import overlap_days

result = overlap_days(...)
```

---

### `previous_business_day()`

Returns the previous business day (Mon-Fri) before the given date.

**Parameters:**
- date_input: The reference date.
- holidays: Optional list of holiday datetimes to skip.

**Returns:**
- datetime: The previous working day.

**Raises:**
- TypeError: If date_input is not a datetime.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import previous_business_day

result = previous_business_day(...)
```

---

### `previous_weekday()`

Returns the most recent occurrence of a specific weekday before a given date.

**Parameters:**
- date_input: The starting date.
- target_weekday: Weekday as integer (0=Monday … 6=Sunday).

**Returns:**
- datetime: The previous (or current) occurrence at midnight.

**Raises:**
- TypeError: If *date_input* is not a datetime object.
- ValueError: If *target_weekday* is not in 0‑6.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import previous_weekday

result = previous_weekday(...)
```

---

### `rfc2822_to_datetime()`

Parse an RFC 2822 date string to a datetime object.

**Parameters:**
- text: RFC 2822 formatted date string.

**Returns:**
- Timezone-aware datetime.

**Raises:**
- ValueError: If the string cannot be parsed.

**Ejemplo:**
```python
from formulite.fxDate.date_convertions import rfc2822_to_datetime

result = rfc2822_to_datetime(...)
```

---

### `snap_to_weekday()`

Snap a date to the nearest specified weekday.

**Parameters:**
- date_input: Starting date.
- target_weekday: Target weekday (0=Monday … 6=Sunday).
- direction: ``'next'`` to move forward or ``'previous'`` to move backward.
- If date_input is already on the target weekday, returns as-is.

**Returns:**
- Date snapped to the target weekday (same type as input).

**Raises:**
- ValueError: If target_weekday is not in [0, 6] or direction is invalid.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import snap_to_weekday

result = snap_to_weekday(...)
```

---

### `start_of_quarter()`

Returns the first day of the quarter for a given date.

**Parameters:**
- date_input: The date for which to get the start of the quarter.
- input_format: Format string if date_input is a string.

**Returns:**
- datetime: First day of the quarter at midnight.

**Raises:**
- TypeError: If date_input is not a datetime or string.
- ValueError: If date_input is a string and input_format is not provided.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import start_of_quarter

result = start_of_quarter(...)
```

---


### `current_month_name()`

Returns the name of the current month in the specified language.

**Parameters:**
- language: Two-letter ISO 639-1 language code. Defaults to ``'en'``.

**Returns:**
- str: Full month name (e.g. ``'January'``, ``'Enero'``).

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_month_name

result = current_month_name(...)
```

---

### `current_days_in_month()`

Returns the number of days in the current month.

**Returns:**
- int: Number of days in the current month (28-31).

**Ejemplo:**
```python
from formulite.fxDate.date_sys import current_days_in_month

result = current_days_in_month(...)
```

---

### `relative_time()`

Describe a datetime relative to a reference point.

**Parameters:**
- dt_input: Target date/datetime.
- reference: Reference point (defaults to now).
- lang: Language code (``'en'`` or ``'es'``). Defaults to ``'en'``.

**Returns:**
- Human-readable relative time string.

**Ejemplo:**
```python
from formulite.fxDate.date_operations import relative_time

result = relative_time(...)
```

---

