"""Coverage tests for fxDate modules."""
import pytest
from datetime import date, datetime, timedelta, time

# date_convertions
from formulite.fxDate.date_convertions import (
    date_to_string, date_to_iso_format, date_to_julian,
    julian_to_date, date_to_excel_serial, excel_serial_to_date,
    seconds_to_hms, hms_to_seconds, datetime_to_date,
    datetime_to_timestamp, timestamp_to_datetime,
    datetime_to_iso8601, iso8601_to_datetime,
    datetime_to_milliseconds_timestamp, milliseconds_timestamp_to_datetime,
    parse_date_flexible, decimal_hours_to_time, time_to_decimal_hours,
    datetime_to_integer, integer_to_datetime,
    modified_julian_date, rata_die, unix_epoch_day,
)

class TestDateConvertions:

    def test_date_to_excel_serial(self):
        assert isinstance(date_to_excel_serial(date(2026, 1, 1)), (int, float))
    def test_excel_serial_to_date(self):
        s = date_to_excel_serial(date(2026, 1, 1))
        r = excel_serial_to_date(s)
        assert r is not None
    def test_seconds_to_hms(self):
        r = seconds_to_hms(3661)
        assert r is not None

    def test_datetime_to_date(self):
        assert datetime_to_date(datetime(2026, 1, 15, 10, 30)) == date(2026, 1, 15)
    def test_datetime_to_timestamp(self):
        ts = datetime_to_timestamp(datetime(2026, 1, 1))
        assert isinstance(ts, (int, float))
    def test_timestamp_to_datetime(self):
        ts = datetime_to_timestamp(datetime(2026, 1, 1))
        r = timestamp_to_datetime(ts)
        assert r is not None
    def test_datetime_to_iso8601(self):
        r = datetime_to_iso8601(datetime(2026, 1, 15, 10, 30))
        assert isinstance(r, str)
    def test_iso8601_to_datetime(self):
        r = iso8601_to_datetime("2026-01-15T10:30:00")
        assert r is not None
    def test_datetime_to_millis(self):
        ms = datetime_to_milliseconds_timestamp(datetime(2026, 1, 1))
        assert isinstance(ms, (int, float))
    def test_millis_to_datetime(self):
        ms = datetime_to_milliseconds_timestamp(datetime(2026, 1, 1))
        r = milliseconds_timestamp_to_datetime(ms)
        assert r is not None
    def test_parse_date_flexible(self):
        r = parse_date_flexible("2026-01-15")
        assert r is not None
    def test_decimal_hours_to_time(self):
        r = decimal_hours_to_time(10.5)
        assert r is not None
    def test_time_to_decimal_hours(self):
        r = time_to_decimal_hours(time(10, 30))
        assert r == pytest.approx(10.5)
    def test_datetime_to_integer(self):
        r = datetime_to_integer(datetime(2026, 1, 15))
        assert isinstance(r, int)
    def test_integer_to_datetime(self):
        n = datetime_to_integer(datetime(2026, 1, 15))
        r = integer_to_datetime(n)
        assert r is not None
    def test_modified_julian_date(self):
        r = modified_julian_date(date(2026, 1, 1))
        assert isinstance(r, (int, float))
    def test_rata_die(self):
        r = rata_die(date(2026, 1, 1))
        assert isinstance(r, int)
    def test_unix_epoch_day(self):
        r = unix_epoch_day(date(2026, 1, 1))
        assert isinstance(r, (int, float))

# date_operations
from formulite.fxDate.date_operations import (
    add_months, add_years, add_time_to_date,
    calculate_days_between_dates, days_between, months_between_dates,
    day_of_year, days_in_month, days_remaining_in_year,
    end_of_month, start_of_month, start_of_quarter, end_of_quarter,
    start_of_year, end_of_year, first_day_of_week, last_day_of_week,
    next_business_day, previous_business_day,
    get_nth_weekday_of_month, last_weekday_of_month,
    clamp_date, date_range, fiscal_quarter,
    is_leap_year, is_weekend, is_working_day,
    week_number, weekday_name, weekday_number, month_name,
    get_quarter, get_season, age,
    string_to_date, string_to_datetime,
    networkdays, workday, date_part,
    human_readable_duration,
)

class TestDateOperations:

    def test_day_of_year(self):
        assert day_of_year(date(2026, 2, 1)) == 32
    def test_days_in_month(self):
        assert days_in_month(2026, 1) == 31
    def test_days_remaining(self):
        r = days_remaining_in_year(date(2026, 12, 30))
        assert r == 1

    def test_next_business_day(self):
        r = next_business_day(date(2026, 1, 9))
        assert r.weekday() < 5
    def test_previous_business_day(self):
        r = previous_business_day(date(2026, 1, 12))
        assert r.weekday() < 5
    def test_nth_weekday_of_month(self):
        r = get_nth_weekday_of_month(2026, 1, 0, 1)
        assert r.weekday() == 0

    def test_clamp_date(self):
        r = clamp_date(date(2026, 6, 15), date(2026, 1, 1), date(2026, 3, 31))
        assert r == date(2026, 3, 31)
    def test_date_range(self):
        r = date_range(date(2026, 1, 1), date(2026, 1, 5))
        assert len(list(r)) >= 4
    def test_fiscal_quarter(self):
        assert isinstance(fiscal_quarter(date(2026, 6, 15)), int)
    def test_is_leap_year(self):
        assert is_leap_year(2024) is True

    def test_age(self):
        assert isinstance(age(date(1990, 5, 15)), int)
    def test_string_to_date(self):
        r = string_to_date("2026-01-15")
        assert r is not None
    def test_string_to_datetime(self):
        r = string_to_datetime("2026-01-15 10:30:00")
        assert r is not None
    def test_networkdays(self):
        r = networkdays(date(2026, 1, 5), date(2026, 1, 9))
        assert isinstance(r, int)

# date_evaluations  
from formulite.fxDate.date_evaluations import (
    is_weekday, is_future, is_past, is_today,
    is_same_day, is_same_month, is_same_year,
    is_first_day_of_month, is_last_day_of_month,
    is_first_of_month, is_end_of_month, is_end_of_quarter,
    is_date_in_range, is_friday_13th, is_palindrome_date,
    zodiac_sign, chinese_zodiac, moon_phase,
    days_until_next_birthday, fiscal_quarter as eval_fiscal_quarter,
    century_of_date, generation_name,
)

class TestDateEvaluations:
    def test_is_weekday(self):
        assert is_weekday(date(2026, 1, 12)) is True
    def test_is_future(self):
        assert is_future(date(2099, 1, 1)) is True
    def test_is_past(self):
        assert is_past(date(2000, 1, 1)) is True
    def test_is_today(self):
        assert is_today(date.today()) is True
    def test_is_same_day(self):
        assert is_same_day(date(2026, 1, 1), date(2026, 1, 1)) is True
    def test_is_same_month(self):
        assert is_same_month(date(2026, 1, 1), date(2026, 1, 31)) is True
    def test_is_same_year(self):
        assert is_same_year(date(2026, 1, 1), date(2026, 12, 31)) is True
    def test_is_first_day_of_month(self):
        assert is_first_day_of_month(date(2026, 1, 1)) is True
    def test_is_last_day_of_month(self):
        assert is_last_day_of_month(date(2026, 1, 31)) is True
    def test_is_first_of_month(self):
        assert is_first_of_month(date(2026, 1, 1)) is True
    def test_is_end_of_month(self):
        assert is_end_of_month(date(2026, 1, 31)) is True
    def test_is_end_of_quarter(self):
        assert is_end_of_quarter(date(2026, 3, 31)) is True
    def test_is_date_in_range(self):
        assert is_date_in_range(date(2026, 1, 15), date(2026, 1, 1), date(2026, 1, 31)) is True
    def test_is_friday_13th(self):
        r = is_friday_13th(date(2026, 2, 13))
        assert isinstance(r, bool)
    def test_is_palindrome_date(self):
        r = is_palindrome_date(date(2020, 2, 2))
        assert isinstance(r, bool)
    def test_zodiac_sign(self):
        r = zodiac_sign(date(2026, 3, 21))
        assert isinstance(r, str)
    def test_chinese_zodiac(self):
        r = chinese_zodiac(2026)
        assert isinstance(r, str)

    def test_days_until_birthday(self):
        r = days_until_next_birthday(date(1990, 5, 15))
        assert isinstance(r, int)
    def test_fiscal_quarter(self):
        r = eval_fiscal_quarter(date(2026, 6, 15))
        assert isinstance(r, int)
    def test_century_of_date(self):
        assert century_of_date(date(2026, 1, 1)) == 21

# date_sys
from formulite.fxDate.date_sys import (
    current_date, current_time, current_datetime, current_year,
    current_month, current_day, current_quarter, current_season,
    current_week_number, current_weekday_name,
    current_is_leap_year, current_is_weekend,
    seconds_since_midnight,
)

class TestDateSys:

    def test_current_time(self):
        assert current_time() is not None
    def test_current_datetime(self):
        assert current_datetime() is not None
    def test_current_year(self):
        assert current_year() == date.today().year
    def test_current_month(self):
        assert 1 <= current_month() <= 12
    def test_current_day(self):
        assert 1 <= current_day() <= 31
    def test_current_quarter(self):
        assert 1 <= current_quarter() <= 4
    def test_current_season(self):
        assert isinstance(current_season(), str)
    def test_current_week_number(self):
        assert isinstance(current_week_number(), int)
    def test_current_weekday_name(self):
        assert isinstance(current_weekday_name(), str)
    def test_current_is_leap_year(self):
        assert isinstance(current_is_leap_year(), bool)
    def test_current_is_weekend(self):
        assert isinstance(current_is_weekend(), bool)
    def test_seconds_since_midnight(self):
        assert isinstance(seconds_since_midnight(), (int, float))
