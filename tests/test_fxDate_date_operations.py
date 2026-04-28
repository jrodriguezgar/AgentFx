"""Tests for fxDate.date_operations."""

from datetime import date, datetime

import pytest

from agentfx.fxDate.date_convertions import hms_to_seconds
from agentfx.fxDate.date_operations import (
    academic_year,
    add_months,
    business_quarter_label,
    clamp_date,
    date_to_ordinal,
    days_360,
    end_of_month_offset,
    format_date_iso,
    format_datetime_iso,
    iso_week_number,
    iso_week_start,
    midpoint_date,
    network_days_intl,
    next_full_moon,
    next_occurrence,
    quarters_between_dates,
    time_overlap,
    time_zone_abbreviation,
    trading_days_between,
    week_number,
    workday,
    workday_intl,
    working_hours_in_month,
    year_fraction,
)
from agentfx.fxString.string_convertions import text_to_braille


class TestDays360:

    def test_us_method_basic(self):
        assert days_360(datetime(2025, 1, 1), datetime(2025, 7, 1)) == 180

    def test_us_method_end_of_month(self):
        assert days_360(datetime(2025, 1, 30), datetime(2025, 2, 28)) == 28

    def test_eu_method(self):
        assert days_360(datetime(2025, 1, 31), datetime(2025, 2, 28), method='eu') == 28

    def test_same_date_returns_zero(self):
        d = datetime(2025, 6, 15)
        assert days_360(d, d) == 0

    def test_negative_result(self):
        assert days_360(datetime(2025, 3, 1), datetime(2025, 1, 1)) < 0

    def test_invalid_method_raises(self):
        with pytest.raises(ValueError):
            days_360(datetime(2025, 1, 1), datetime(2025, 2, 1), method='xx')

    def test_type_error(self):
        with pytest.raises(TypeError):
            days_360("2025-01-01", datetime(2025, 2, 1))

class TestNetworkDaysIntl:

    def test_standard_weekend(self):
        # Mon Jan 6 to Fri Jan 10 = 5 working days
        assert network_days_intl(datetime(2025, 1, 6), datetime(2025, 1, 10)) == 5

    def test_with_holiday(self):
        holidays = [datetime(2025, 1, 8)]
        assert network_days_intl(
            datetime(2025, 1, 6), datetime(2025, 1, 10), holidays=holidays
        ) == 4

    def test_string_weekend(self):
        # Weekend = Fri-Sat = '0000110'
        # Mon-Thu = working days
        # Jan 6 (Mon) to Jan 12 (Sun): Mon,Tue,Wed,Thu,Sun = 5
        assert network_days_intl(
            datetime(2025, 1, 6), datetime(2025, 1, 12), weekend='0000110'
        ) == 5

    def test_custom_int_weekend(self):
        # weekend=2 means Sun-Mon are off
        # Jan 6 (Mon) to Jan 10 (Fri): Tue,Wed,Thu,Fri = 4
        assert network_days_intl(
            datetime(2025, 1, 6), datetime(2025, 1, 10), weekend=2
        ) == 4

    def test_start_after_end_raises(self):
        with pytest.raises(ValueError):
            network_days_intl(datetime(2025, 1, 10), datetime(2025, 1, 6))

class TestWorkday:

    def test_forward(self):
        # Mon Jan 6 + 5 working days = Mon Jan 13
        assert workday(datetime(2025, 1, 6), 5) == datetime(2025, 1, 13)

    def test_backward(self):
        # Mon Jan 6 - 1 working day = Fri Jan 3
        assert workday(datetime(2025, 1, 6), -1) == datetime(2025, 1, 3)

    def test_zero_days(self):
        d = datetime(2025, 1, 6)
        assert workday(d, 0) == d.replace(hour=0, minute=0, second=0, microsecond=0)

    def test_skip_holidays(self):
        holidays = [datetime(2025, 1, 7), datetime(2025, 1, 8)]
        # Mon Jan 6 + 1 day, skip Tue 7 & Wed 8 → Thu Jan 9
        assert workday(datetime(2025, 1, 6), 1, holidays=holidays) == datetime(2025, 1, 9)

class TestWorkdayIntl:

    def test_custom_weekend(self):
        # weekend=2 means Sun-Mon off. Start Tue Jan 7.
        # +5 working days: Tue7, Wed8, Thu9, Fri10, Sat11 → result Sat Jan 11
        result = workday_intl(datetime(2025, 1, 6), 5, weekend=2)
        assert result == datetime(2025, 1, 11)

class TestYearFraction:

    def test_basis_0_half_year(self):
        result = year_fraction(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=0)
        assert result == pytest.approx(0.5, abs=1e-6)

    def test_basis_1_half_year(self):
        result = year_fraction(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=1)
        assert 0.49 < result < 0.51

    def test_invalid_basis_raises(self):
        with pytest.raises(ValueError):
            year_fraction(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=3)


# ── B. Week Number ──────────────────────────────────────────────────────────

class TestWeekNumber:

    def test_iso_system(self):
        assert week_number(datetime(2025, 1, 1), system=21) == 1

    def test_sunday_start(self):
        result = week_number(datetime(2025, 1, 1), system=1)
        assert isinstance(result, int)
        assert result >= 1

    def test_invalid_system_raises(self):
        with pytest.raises(ValueError):
            week_number(datetime(2025, 1, 1), system=99)

class TestIsoWeekNumber:

    def test_basic(self):
        assert iso_week_number(datetime(2025, 6, 15)) == 24

    def test_first_day_of_year(self):
        assert iso_week_number(datetime(2025, 1, 1)) == 1

    def test_type_error(self):
        with pytest.raises(TypeError):
            iso_week_number("2025-01-01")


# ── C. Quarter / Timer ──────────────────────────────────────────────────────

class TestQuartersBetweenDates:

    def test_three_quarters(self):
        assert quarters_between_dates(datetime(2025, 1, 1), datetime(2025, 10, 1)) == 3

    def test_zero_quarters_incomplete(self):
        # Less than 3 months difference
        assert quarters_between_dates(datetime(2025, 1, 15), datetime(2025, 4, 14)) == 0

    def test_one_full_quarter(self):
        assert quarters_between_dates(datetime(2025, 1, 1), datetime(2025, 4, 1)) == 1

    def test_negative_direction(self):
        result = quarters_between_dates(datetime(2025, 10, 1), datetime(2025, 1, 1))
        assert result == -3

    def test_type_error(self):
        with pytest.raises(TypeError):
            quarters_between_dates("2025-01-01", datetime(2025, 4, 1))

class TestAddMonths:

    def test_add_one_month(self):
        assert add_months(datetime(2025, 1, 15), 1) == datetime(2025, 2, 15)

    def test_subtract_one_month(self):
        assert add_months(datetime(2025, 3, 15), -1) == datetime(2025, 2, 15)

    def test_clamp_to_end_of_shorter_month(self):
        # Jan 31 + 1 month → Feb 28 (2025 not a leap year)
        assert add_months(datetime(2025, 1, 31), 1) == datetime(2025, 2, 28)

    def test_leap_year_feb(self):
        # Jan 31 + 1 month in 2024 → Feb 29
        assert add_months(datetime(2024, 1, 31), 1) == datetime(2024, 2, 29)

    def test_cross_year_boundary(self):
        assert add_months(datetime(2025, 11, 15), 3) == datetime(2026, 2, 15)

    def test_preserve_time(self):
        dt = datetime(2025, 1, 15, 10, 30, 45)
        result = add_months(dt, 1)
        assert result.hour == 10
        assert result.minute == 30
        assert result.second == 45

    def test_type_error(self):
        with pytest.raises(TypeError):
            add_months("2025-01-15", 1)

class TestEndOfMonthOffset:

    def test_current_month(self):
        result = end_of_month_offset(datetime(2025, 1, 15), 0)
        assert result == datetime(2025, 1, 31, 23, 59, 59, 999999)

    def test_next_month(self):
        result = end_of_month_offset(datetime(2025, 1, 15), 1)
        assert result == datetime(2025, 2, 28, 23, 59, 59, 999999)

    def test_leap_year(self):
        result = end_of_month_offset(datetime(2024, 1, 15), 1)
        assert result == datetime(2024, 2, 29, 23, 59, 59, 999999)

    def test_backward(self):
        result = end_of_month_offset(datetime(2025, 3, 10), -1)
        assert result == datetime(2025, 2, 28, 23, 59, 59, 999999)

    def test_cross_year(self):
        result = end_of_month_offset(datetime(2025, 11, 1), 3)
        assert result == datetime(2026, 2, 28, 23, 59, 59, 999999)

    def test_type_error(self):
        with pytest.raises(TypeError):
            end_of_month_offset("2025-01-15", 1)

class TestCronNextRun:

    def test_next_hour(self):
        from agentfx.fxDate.date_operations import cron_next_run

        result = cron_next_run("0 9 * * *", datetime(2026, 4, 8, 10, 0))
        assert result == datetime(2026, 4, 9, 9, 0)

    def test_same_day(self):
        from agentfx.fxDate.date_operations import cron_next_run

        result = cron_next_run("30 14 * * *", datetime(2026, 4, 8, 10, 0))
        assert result == datetime(2026, 4, 8, 14, 30)

    def test_invalid_fields(self):
        from agentfx.fxDate.date_operations import cron_next_run

        with pytest.raises(ValueError):
            cron_next_run("0 9 *", datetime(2026, 4, 8))

class TestCronPreviousRun:

    def test_previous_hour(self):
        from agentfx.fxDate.date_operations import cron_previous_run

        result = cron_previous_run("0 9 * * *", datetime(2026, 4, 8, 10, 0))
        assert result == datetime(2026, 4, 8, 9, 0)

class TestSunriseSunset:

    def test_madrid_summer(self):
        from agentfx.fxDate.date_operations import sunrise_sunset

        sr, ss = sunrise_sunset(40.4168, -3.7038, date(2026, 6, 21))
        # Sunrise should be before sunset
        assert sr < ss
        # Approximate daylight duration check (~15 hours in summer Madrid)
        delta_hours = (ss - sr).total_seconds() / 3600
        assert 13 < delta_hours < 17

    def test_type_error(self):
        from agentfx.fxDate.date_operations import sunrise_sunset

        with pytest.raises(TypeError):
            sunrise_sunset("invalid", 0, date(2026, 1, 1))

class TestDaylightHours:

    def test_summer_longer(self):
        from agentfx.fxDate.date_operations import daylight_hours

        summer = daylight_hours(40.4168, date(2026, 6, 21))
        winter = daylight_hours(40.4168, date(2026, 12, 21))
        assert summer > winter

    def test_equator(self):
        from agentfx.fxDate.date_operations import daylight_hours

        hours = daylight_hours(0.0, date(2026, 3, 20))
        assert 11.5 < hours < 12.5

class TestShiftSchedule:

    def test_work_day(self):
        from agentfx.fxDate.date_operations import shift_schedule

        assert shift_schedule(date(2026, 1, 1), 4, 2, date(2026, 1, 4)) == "work"

    def test_rest_day(self):
        from agentfx.fxDate.date_operations import shift_schedule

        assert shift_schedule(date(2026, 1, 1), 4, 2, date(2026, 1, 5)) == "rest"

    def test_cycle_wraps(self):
        from agentfx.fxDate.date_operations import shift_schedule

        # Day 6 (index 5) mod 6 = 5 → rest
        assert shift_schedule(date(2026, 1, 1), 4, 2, date(2026, 1, 7)) == "work"

class TestNextBusinessDay:

    def test_friday_to_monday(self):
        from agentfx.fxDate.date_operations import next_business_day
        assert next_business_day(date(2026, 4, 3)) == date(2026, 4, 6)

    def test_saturday_to_monday(self):
        from agentfx.fxDate.date_operations import next_business_day
        assert next_business_day(date(2026, 4, 4)) == date(2026, 4, 6)

    def test_with_holiday(self):
        from agentfx.fxDate.date_operations import next_business_day
        # Monday is holiday, skip to Tuesday
        result = next_business_day(date(2026, 4, 3), holidays=[date(2026, 4, 6)])
        assert result == date(2026, 4, 7)

class TestPreviousBusinessDay:

    def test_monday_to_friday(self):
        from agentfx.fxDate.date_operations import previous_business_day
        assert previous_business_day(date(2026, 4, 6)) == date(2026, 4, 3)

    def test_sunday_to_friday(self):
        from agentfx.fxDate.date_operations import previous_business_day
        assert previous_business_day(date(2026, 4, 5)) == date(2026, 4, 3)

class TestDateSequence:

    def test_basic(self):
        from agentfx.fxDate.date_operations import date_sequence
        result = date_sequence(date(2026, 1, 1), date(2026, 1, 5))
        assert len(result) == 5
        assert result[0] == date(2026, 1, 1)
        assert result[-1] == date(2026, 1, 5)

    def test_step_2(self):
        from agentfx.fxDate.date_operations import date_sequence
        result = date_sequence(date(2026, 1, 1), date(2026, 1, 10), step_days=2)
        assert result == [date(2026, 1, 1), date(2026, 1, 3), date(2026, 1, 5),
                          date(2026, 1, 7), date(2026, 1, 9)]

    def test_zero_step_raises(self):
        from agentfx.fxDate.date_operations import date_sequence

        with pytest.raises(ValueError):
            date_sequence(date(2026, 1, 1), date(2026, 1, 5), step_days=0)

class TestTextToBraille:
    def test_basic(self):
        result = text_to_braille("a")
        assert isinstance(result, str)
        assert len(result) == 1

    def test_type_error(self):
        with pytest.raises(TypeError):
            text_to_braille(42)


# ---------------------------------------------------------------------------
# fxDate — date_operations.py
# ---------------------------------------------------------------------------


class TestTimeZoneAbbreviation:
    def test_utc(self):
        result = time_zone_abbreviation("UTC")
        assert result == "UTC"

    def test_type_error(self):
        with pytest.raises(TypeError):
            time_zone_abbreviation(123)

    def test_invalid_timezone(self):
        with pytest.raises(ValueError):
            time_zone_abbreviation("Not/A/Timezone")

class TestNextOccurrence:
    def test_returns_future(self):
        ref = datetime(2024, 1, 1, 12, 0)  # Monday
        result = next_occurrence(3, ref=ref)  # Wednesday
        assert result > ref
        assert result.isoweekday() == 3

    def test_type_error(self):
        with pytest.raises(TypeError):
            next_occurrence("monday")

    def test_invalid_weekday(self):
        with pytest.raises(ValueError):
            next_occurrence(8)

class TestTradingDaysBetween:

    def test_standard_week(self):
        result = trading_days_between(date(2026, 4, 6), date(2026, 4, 13))
        assert result == 5

    def test_custom_weekend(self):
        result = trading_days_between(
            date(2026, 4, 6), date(2026, 4, 13), weekend=(4, 5),
        )
        assert result == 5

    def test_type_error(self):

        with pytest.raises(TypeError):
            trading_days_between("2026-01-01", date(2026, 1, 5))

class TestIsoWeekStart:

    def test_week_1_2026(self):
        result = iso_week_start(2026, 1)
        assert result == date(2025, 12, 29)

    def test_type_error(self):

        with pytest.raises(TypeError):
            iso_week_start(2026, 1.5)

    def test_invalid_week(self):

        with pytest.raises(ValueError):
            iso_week_start(2026, 0)

class TestTimeOverlap:

    def test_partial_overlap(self):
        a = datetime(2026, 1, 1, 8, 0)
        b = datetime(2026, 1, 1, 12, 0)
        c = datetime(2026, 1, 1, 10, 0)
        d = datetime(2026, 1, 1, 14, 0)
        assert time_overlap(a, b, c, d) == 7200.0

    def test_no_overlap(self):
        a = datetime(2026, 1, 1, 8, 0)
        b = datetime(2026, 1, 1, 9, 0)
        c = datetime(2026, 1, 1, 10, 0)
        d = datetime(2026, 1, 1, 11, 0)
        assert time_overlap(a, b, c, d) == 0.0


# ── fxDate ── date_evaluations ──────────────────────────────────────────

class TestNextFullMoon:

    def test_returns_date(self):
        result = next_full_moon(date(2026, 1, 1))
        assert isinstance(result, date)
        assert result >= date(2026, 1, 1)

    def test_type_error(self):

        with pytest.raises(TypeError):
            next_full_moon("2026-01-01")

class TestWorkingHoursInMonth:

    def test_jan_2026(self):
        # January 2026 has 22 weekdays
        assert working_hours_in_month(2026, 1) == 176.0

    def test_custom_hours(self):
        result = working_hours_in_month(2026, 1, hours_per_day=7.5)
        assert result == 22 * 7.5

    def test_invalid_month(self):

        with pytest.raises(ValueError):
            working_hours_in_month(2026, 13)


# ── fxNumeric ── finance_functions ──────────────────────────────────────

class TestFormatDateIso:
    def test_basic(self):
        assert format_date_iso(date(2024, 3, 15)) == "2024-03-15"

    def test_from_datetime(self):
        assert format_date_iso(datetime(2024, 3, 15, 10, 0)) == "2024-03-15"

    def test_type_error(self):
        with pytest.raises(TypeError):
            format_date_iso("2024-03-15")

class TestFormatDatetimeIso:
    def test_basic(self):
        assert format_datetime_iso(datetime(2024, 3, 15, 10, 30, 0)) == "2024-03-15T10:30:00"

    def test_type_error(self):
        with pytest.raises(TypeError):
            format_datetime_iso(date(2024, 3, 15))

class TestClampDate:
    def test_above(self):
        assert clamp_date(date(2024, 6, 15), date(2024, 1, 1), date(2024, 3, 31)) == date(2024, 3, 31)

    def test_below(self):
        assert clamp_date(date(2023, 6, 1), date(2024, 1, 1), date(2024, 12, 31)) == date(2024, 1, 1)

    def test_in_range(self):
        assert clamp_date(date(2024, 2, 15), date(2024, 1, 1), date(2024, 3, 31)) == date(2024, 2, 15)

    def test_type_error(self):
        with pytest.raises(TypeError):
            clamp_date("2024-01-01", date(2024, 1, 1), date(2024, 12, 31))

class TestMidpointDate:
    def test_basic(self):
        assert midpoint_date(date(2024, 1, 1), date(2024, 1, 11)) == date(2024, 1, 6)

    def test_same_date(self):
        assert midpoint_date(date(2024, 1, 1), date(2024, 1, 1)) == date(2024, 1, 1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            midpoint_date("2024-01-01", date(2024, 1, 1))

class TestDateToOrdinal:
    def test_basic(self):
        assert date_to_ordinal(date(2024, 1, 1)) == 738886

    def test_from_datetime(self):
        assert date_to_ordinal(datetime(2024, 1, 1, 12, 0)) == 738886

    def test_type_error(self):
        with pytest.raises(TypeError):
            date_to_ordinal("2024-01-01")

class TestHmsToSeconds:

    def test_hms(self):
        assert hms_to_seconds("1:01:01") == 3661

    def test_ms(self):
        assert hms_to_seconds("5:30") == 330

    def test_invalid(self):
        with pytest.raises(ValueError):
            hms_to_seconds("bad")


# ---------------------------------------------------------------------------
# fxDate — date_operations.py
# ---------------------------------------------------------------------------


class TestBusinessQuarterLabel:

    def test_q1(self):
        assert business_quarter_label(date(2024, 3, 15)) == "Q1 2024"

    def test_q4(self):
        assert business_quarter_label(date(2024, 12, 1)) == "Q4 2024"

    def test_datetime_input(self):
        assert business_quarter_label(datetime(2024, 6, 15, 10, 0)) == "Q2 2024"

class TestAcademicYear:

    def test_spring(self):
        assert academic_year(date(2024, 2, 1)) == "2023/2024"

    def test_fall(self):
        assert academic_year(date(2024, 9, 15)) == "2024/2025"

    def test_custom_start(self):
        assert academic_year(date(2024, 2, 1), start_month=1) == "2024/2025"

class TestFiscalQuarter:

    def test_calendar_q1(self):
        from agentfx.fxDate.date_operations import fiscal_quarter
        assert fiscal_quarter(date(2026, 3, 15)) == 1

    def test_calendar_q4(self):
        from agentfx.fxDate.date_operations import fiscal_quarter
        assert fiscal_quarter(date(2026, 12, 1)) == 4

    def test_fiscal_april_start(self):
        from agentfx.fxDate.date_operations import fiscal_quarter
        assert fiscal_quarter(date(2026, 3, 15), fiscal_start_month=4) == 4

    def test_fiscal_april_start_july(self):
        from agentfx.fxDate.date_operations import fiscal_quarter
        assert fiscal_quarter(date(2026, 7, 1), fiscal_start_month=4) == 2

    def test_fiscal_october_start(self):
        from agentfx.fxDate.date_operations import fiscal_quarter
        assert fiscal_quarter(date(2026, 10, 1), fiscal_start_month=10) == 1
        assert fiscal_quarter(date(2026, 1, 1), fiscal_start_month=10) == 2

class TestCountdownDays:

    def test_future(self):
        from agentfx.fxDate.date_operations import countdown_days
        result = countdown_days(date(2026, 12, 31), date(2026, 1, 1))
        assert result == 364

    def test_past(self):
        from agentfx.fxDate.date_operations import countdown_days
        result = countdown_days(date(2026, 1, 1), date(2026, 12, 31))
        assert result == -364

    def test_same_day(self):
        from agentfx.fxDate.date_operations import countdown_days
        result = countdown_days(date(2026, 6, 15), date(2026, 6, 15))
        assert result == 0

class TestDecimalHoursBetween:

    def test_basic(self):
        from agentfx.fxDate.date_operations import decimal_hours_between
        result = decimal_hours_between(
            datetime(2024, 1, 1, 8, 0),
            datetime(2024, 1, 1, 9, 30),
        )
        assert result == 1.5

    def test_negative(self):
        from agentfx.fxDate.date_operations import decimal_hours_between
        result = decimal_hours_between(
            datetime(2024, 1, 1, 10, 0),
            datetime(2024, 1, 1, 8, 0),
        )
        assert result == -2.0

class TestSemester:

    def test_first(self):
        from agentfx.fxDate.date_operations import semester
        assert semester(date(2024, 3, 15)) == 1

    def test_second(self):
        from agentfx.fxDate.date_operations import semester
        assert semester(date(2024, 7, 1)) == 2

    def test_iso_string(self):
        from agentfx.fxDate.date_operations import semester
        assert semester("2024-06-30") == 1

class TestElapsedBusinessDays:

    def test_full_week(self):
        from agentfx.fxDate.date_operations import elapsed_business_days
        # Mon 2024-01-01 to Fri 2024-01-05
        result = elapsed_business_days(date(2024, 1, 1), date(2024, 1, 5))
        assert result == 5

    def test_with_weekend(self):
        from agentfx.fxDate.date_operations import elapsed_business_days
        # Mon 2024-01-01 to Sun 2024-01-07
        result = elapsed_business_days(date(2024, 1, 1), date(2024, 1, 7))
        assert result == 5

    def test_with_holiday(self):
        from agentfx.fxDate.date_operations import elapsed_business_days
        result = elapsed_business_days(
            date(2024, 1, 1),
            date(2024, 1, 5),
            holidays=[date(2024, 1, 3)],
        )
        assert result == 4

class TestDayOfYear:

    def test_march_1_leap(self):
        from agentfx.fxDate.date_operations import day_of_year
        assert day_of_year(date(2024, 3, 1)) == 61

    def test_jan_1(self):
        from agentfx.fxDate.date_operations import day_of_year
        assert day_of_year(date(2024, 1, 1)) == 1

    def test_dec_31(self):
        from agentfx.fxDate.date_operations import day_of_year
        assert day_of_year(date(2024, 12, 31)) == 366

class TestDaysRemainingInYear:

    def test_dec_30(self):
        from agentfx.fxDate.date_operations import days_remaining_in_year
        assert days_remaining_in_year(date(2024, 12, 30)) == 1

    def test_dec_31(self):
        from agentfx.fxDate.date_operations import days_remaining_in_year
        assert days_remaining_in_year(date(2024, 12, 31)) == 0

    def test_jan_1(self):
        from agentfx.fxDate.date_operations import days_remaining_in_year
        assert days_remaining_in_year(date(2024, 1, 1)) == 365


# =====================================================================
# Date Evaluations
# =====================================================================

class TestFiscalQuarterV2:

    def test_calendar_year(self):
        from agentfx.fxDate.date_evaluations import fiscal_quarter

        assert fiscal_quarter(date(2025, 3, 15)) == 1
        assert fiscal_quarter(date(2025, 6, 15)) == 2
        assert fiscal_quarter(date(2025, 9, 15)) == 3
        assert fiscal_quarter(date(2025, 12, 15)) == 4

    def test_april_fiscal_year(self):
        from agentfx.fxDate.date_evaluations import fiscal_quarter

        assert fiscal_quarter(date(2025, 3, 15), fiscal_start_month=4) == 4
        assert fiscal_quarter(date(2025, 4, 15), fiscal_start_month=4) == 1

    def test_type_error(self):
        from agentfx.fxDate.date_evaluations import fiscal_quarter

        with pytest.raises(TypeError):
            fiscal_quarter("2025-03-15")
