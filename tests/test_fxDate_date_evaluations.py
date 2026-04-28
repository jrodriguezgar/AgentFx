"""Tests for fxDate.date_evaluations."""

from datetime import date, datetime

import pytest

from shortfx.fxDate.date_evaluations import (
    astronomical_season,
    bimester_of_date,
    century_of_date,
    date_grade,
    date_of_easter,
    date_of_nth_weekday,
    date_to_julian_day,
    day_name_of_date,
    days_until_end_of_year,
    days_until_weekday,
    elapsed_years,
    fortnight_of_year,
    generation_name,
    is_blue_moon,
    is_century_year,
    is_date_in_range,
    is_end_of_month,
    is_end_of_quarter,
    is_equinox_or_solstice,
    is_first_day_of_month,
    is_first_of_month,
    is_friday_13th,
    is_holiday,
    is_iso_long_year,
    is_last_day_of_year,
    is_millennium_year,
    is_nth_weekday,
    is_palindrome_date,
    is_start_of_quarter,
    millennium_of_date,
    next_month_same_day,
    ordinal_date_string,
    previous_month_same_day,
    quarter_end_date,
    quarter_start_date,
    semester_of_date,
    trimester_of_date,
    week_parity,
    weeks_between_dates,
)
from shortfx.fxDate.date_operations import business_days_until


class TestIsDstTransitionDay:

    def test_transition_day(self):
        from shortfx.fxDate.date_evaluations import is_dst_transition_day

        assert is_dst_transition_day(date(2026, 3, 29), "Europe/Madrid") is True

    def test_normal_day(self):
        from shortfx.fxDate.date_evaluations import is_dst_transition_day

        assert is_dst_transition_day(date(2026, 6, 15), "Europe/Madrid") is False

class TestMoonPhase:

    def test_returns_tuple(self):
        from shortfx.fxDate.date_evaluations import moon_phase

        phase, name = moon_phase(date(2026, 4, 8))
        assert 0.0 <= phase <= 1.0
        assert isinstance(name, str)

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import moon_phase

        with pytest.raises(TypeError):
            moon_phase("2026-04-08")


# ── fxNumeric — Finance ──────────────────────────────────────────────────

class TestIsAnniversary:

    def test_same_day(self):
        from shortfx.fxDate.date_evaluations import is_anniversary
        assert is_anniversary(date(1990, 7, 4), date(2026, 7, 4)) is True

    def test_different_day(self):
        from shortfx.fxDate.date_evaluations import is_anniversary
        assert is_anniversary(date(1990, 7, 4), date(2026, 7, 5)) is False

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import is_anniversary

        with pytest.raises(TypeError):
            is_anniversary("2020-01-01", date(2026, 1, 1))

class TestIsLastDayOfMonth:

    def test_leap_feb_29(self):
        from shortfx.fxDate.date_evaluations import is_last_day_of_month
        assert is_last_day_of_month(date(2024, 2, 29)) is True

    def test_non_leap_feb_28(self):
        from shortfx.fxDate.date_evaluations import is_last_day_of_month
        assert is_last_day_of_month(date(2023, 2, 28)) is True

    def test_leap_feb_28(self):
        from shortfx.fxDate.date_evaluations import is_last_day_of_month
        assert is_last_day_of_month(date(2024, 2, 28)) is False

    def test_dec_31(self):
        from shortfx.fxDate.date_evaluations import is_last_day_of_month
        assert is_last_day_of_month(date(2026, 12, 31)) is True

class TestIsDst:

    def test_us_summer(self):
        from shortfx.fxDate.date_evaluations import is_dst
        assert is_dst(datetime(2026, 7, 15, 12, 0), "US/Eastern") is True

    def test_us_winter(self):
        from shortfx.fxDate.date_evaluations import is_dst
        assert is_dst(datetime(2026, 1, 15, 12, 0), "US/Eastern") is False

    def test_utc_always_false(self):
        from shortfx.fxDate.date_evaluations import is_dst
        assert is_dst(datetime(2026, 7, 15, 12, 0), "UTC") is False

    def test_europe_summer(self):
        from shortfx.fxDate.date_evaluations import is_dst
        assert is_dst(datetime(2026, 6, 15, 12, 0), "Europe/Madrid") is True

    def test_unsupported_raises(self):
        from shortfx.fxDate.date_evaluations import is_dst

        with pytest.raises(ValueError):
            is_dst(datetime(2026, 7, 15), "Asia/Tokyo")

class TestIsoDayName:

    def test_monday(self):
        from shortfx.fxDate.date_evaluations import iso_day_name

        assert iso_day_name(date(2025, 6, 9)) == "Monday"

    def test_sunday(self):
        from shortfx.fxDate.date_evaluations import iso_day_name

        assert iso_day_name(date(2025, 6, 8)) == "Sunday"

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import iso_day_name

        with pytest.raises(TypeError):
            iso_day_name("2025-06-09")

class TestDaysInYear:

    def test_leap(self):
        from shortfx.fxDate.date_evaluations import days_in_year

        assert days_in_year(2024) == 366

    def test_common(self):
        from shortfx.fxDate.date_evaluations import days_in_year

        assert days_in_year(2025) == 365

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import days_in_year

        with pytest.raises(TypeError):
            days_in_year(2025.0)

class TestNthWeekdayOfMonth:

    def test_mlk_day(self):
        from shortfx.fxDate.date_evaluations import nth_weekday_of_month

        # 3rd Monday of January 2025
        assert nth_weekday_of_month(2025, 1, 1, 3) == date(2025, 1, 20)

    def test_first_friday(self):
        from shortfx.fxDate.date_evaluations import nth_weekday_of_month

        assert nth_weekday_of_month(2025, 6, 5, 1) == date(2025, 6, 6)

    def test_nonexistent(self):
        from shortfx.fxDate.date_evaluations import nth_weekday_of_month

        with pytest.raises(ValueError):
            nth_weekday_of_month(2025, 2, 1, 5)  # 5th Monday of Feb

    def test_invalid_weekday(self):
        from shortfx.fxDate.date_evaluations import nth_weekday_of_month

        with pytest.raises(ValueError):
            nth_weekday_of_month(2025, 1, 0, 1)

class TestAgeAtDate:

    def test_before_birthday(self):
        from shortfx.fxDate.date_evaluations import age_at_date

        assert age_at_date(date(1990, 6, 15), date(2025, 6, 14)) == 34

    def test_on_birthday(self):
        from shortfx.fxDate.date_evaluations import age_at_date

        assert age_at_date(date(1990, 6, 15), date(2025, 6, 15)) == 35

    def test_future_birth(self):
        from shortfx.fxDate.date_evaluations import age_at_date

        with pytest.raises(ValueError):
            age_at_date(date(2030, 1, 1), date(2025, 1, 1))

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import age_at_date

        with pytest.raises(TypeError):
            age_at_date("1990-06-15")

class TestWorkdaysInMonth:

    def test_june_2025(self):
        from shortfx.fxDate.date_evaluations import workdays_in_month

        assert workdays_in_month(2025, 6) == 21

    def test_invalid_month(self):
        from shortfx.fxDate.date_evaluations import workdays_in_month

        with pytest.raises(ValueError):
            workdays_in_month(2025, 13)

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import workdays_in_month

        with pytest.raises(TypeError):
            workdays_in_month(2025, 6.0)

class TestSemesterOfYear:

    def test_first(self):
        from shortfx.fxDate.date_evaluations import semester_of_year

        assert semester_of_year(date(2025, 3, 15)) == 1

    def test_second(self):
        from shortfx.fxDate.date_evaluations import semester_of_year

        assert semester_of_year(date(2025, 9, 15)) == 2

    def test_boundary(self):
        from shortfx.fxDate.date_evaluations import semester_of_year

        assert semester_of_year(date(2025, 6, 30)) == 1
        assert semester_of_year(date(2025, 7, 1)) == 2

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import semester_of_year

        with pytest.raises(TypeError):
            semester_of_year("2025-03-15")

class TestWeeksBetweenDates:

    def test_basic(self):
        assert weeks_between_dates(date(2025, 1, 1), date(2025, 3, 1)) == 8

    def test_same_date(self):
        assert weeks_between_dates(date(2025, 6, 1), date(2025, 6, 1)) == 0

    def test_reversed_order(self):
        assert weeks_between_dates(date(2025, 3, 1), date(2025, 1, 1)) == 8

    def test_type_error(self):
        with pytest.raises(TypeError):
            weeks_between_dates("2025-01-01", date(2025, 3, 1))

class TestQuarterStartDate:

    def test_q1(self):
        assert quarter_start_date(2025, 1) == date(2025, 1, 1)

    def test_q2(self):
        assert quarter_start_date(2025, 2) == date(2025, 4, 1)

    def test_q3(self):
        assert quarter_start_date(2025, 3) == date(2025, 7, 1)

    def test_q4(self):
        assert quarter_start_date(2025, 4) == date(2025, 10, 1)

    def test_invalid_quarter(self):
        with pytest.raises(ValueError):
            quarter_start_date(2025, 5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            quarter_start_date("2025", 1)

class TestQuarterEndDate:

    def test_q1(self):
        assert quarter_end_date(2025, 1) == date(2025, 3, 31)

    def test_q2(self):
        assert quarter_end_date(2025, 2) == date(2025, 6, 30)

    def test_q3(self):
        assert quarter_end_date(2025, 3) == date(2025, 9, 30)

    def test_q4(self):
        assert quarter_end_date(2025, 4) == date(2025, 12, 31)

    def test_leap_year_q1(self):
        assert quarter_end_date(2024, 1) == date(2024, 3, 31)

    def test_invalid_quarter(self):
        with pytest.raises(ValueError):
            quarter_end_date(2025, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            quarter_end_date("2025", 1)

class TestIsFirstDayOfMonth:

    def test_true(self):
        assert is_first_day_of_month(date(2025, 6, 1)) is True

    def test_false(self):
        assert is_first_day_of_month(date(2025, 6, 15)) is False

    def test_datetime_input(self):
        assert is_first_day_of_month(datetime(2025, 1, 1, 12, 0)) is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_first_day_of_month("2025-06-01")

class TestIsEndOfMonth:

    def test_feb_28(self):
        assert is_end_of_month(date(2025, 2, 28)) is True

    def test_feb_28_leap(self):
        assert is_end_of_month(date(2024, 2, 28)) is False

    def test_feb_29_leap(self):
        assert is_end_of_month(date(2024, 2, 29)) is True

    def test_not_end(self):
        assert is_end_of_month(date(2025, 3, 15)) is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_end_of_month("2025-02-28")

class TestNextMonthSameDay:

    def test_basic(self):
        assert next_month_same_day(date(2025, 1, 15)) == date(2025, 2, 15)

    def test_clamp_feb(self):
        assert next_month_same_day(date(2025, 1, 31)) == date(2025, 2, 28)

    def test_december_to_january(self):
        assert next_month_same_day(date(2025, 12, 15)) == date(2026, 1, 15)

    def test_leap_year(self):
        assert next_month_same_day(date(2024, 1, 29)) == date(2024, 2, 29)

    def test_type_error(self):
        with pytest.raises(TypeError):
            next_month_same_day("2025-01-15")

class TestIsLastDayOfYear:

    def test_true(self):
        assert is_last_day_of_year(date(2025, 12, 31)) is True

    def test_false(self):
        assert is_last_day_of_year(date(2025, 12, 30)) is False
        assert is_last_day_of_year(date(2025, 6, 30)) is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_last_day_of_year("2025-12-31")

class TestDateOfEaster:

    def test_2025(self):
        assert date_of_easter(2025) == date(2025, 4, 20)

    def test_2024(self):
        assert date_of_easter(2024) == date(2024, 3, 31)

    def test_2000(self):
        assert date_of_easter(2000) == date(2000, 4, 23)

    def test_too_old_raises(self):
        with pytest.raises(ValueError):
            date_of_easter(1500)

    def test_type_error(self):
        with pytest.raises(TypeError):
            date_of_easter(2025.0)

class TestPreviousMonthSameDay:

    def test_basic(self):
        assert previous_month_same_day(date(2025, 3, 15)) == date(2025, 2, 15)

    def test_clamp_feb(self):
        assert previous_month_same_day(date(2025, 3, 31)) == date(2025, 2, 28)

    def test_january_to_december(self):
        assert previous_month_same_day(date(2025, 1, 15)) == date(2024, 12, 15)

    def test_leap_year(self):
        assert previous_month_same_day(date(2024, 3, 29)) == date(2024, 2, 29)

    def test_type_error(self):
        with pytest.raises(TypeError):
            previous_month_same_day("2025-03-15")

class TestCenturyOfDate:

    def test_21st(self):
        assert century_of_date(date(2025, 6, 15)) == 21

    def test_20th(self):
        assert century_of_date(date(1999, 12, 31)) == 20

    def test_year_2000(self):
        assert century_of_date(date(2000, 1, 1)) == 20

    def test_type_error(self):
        with pytest.raises(TypeError):
            century_of_date("2025-06-15")

class TestMillenniumOfDate:

    def test_3rd(self):
        assert millennium_of_date(date(2025, 1, 1)) == 3

    def test_2nd(self):
        assert millennium_of_date(date(1500, 6, 1)) == 2

    def test_year_2000(self):
        assert millennium_of_date(date(2000, 1, 1)) == 2

    def test_type_error(self):
        with pytest.raises(TypeError):
            millennium_of_date("2025-01-01")

class TestDayNameOfDate:

    def test_sunday(self):
        assert day_name_of_date(date(2025, 4, 20)) == "Sunday"

    def test_monday(self):
        assert day_name_of_date(date(2025, 4, 21)) == "Monday"

    def test_datetime_input(self):
        assert day_name_of_date(datetime(2025, 4, 20, 10, 0)) == "Sunday"

    def test_type_error(self):
        with pytest.raises(TypeError):
            day_name_of_date("2025-04-20")

class TestDaysUntilEndOfYear:
    def test_dec_1(self):
        assert days_until_end_of_year(date(2025, 12, 1)) == 30

    def test_dec_31(self):
        assert days_until_end_of_year(date(2025, 12, 31)) == 0

    def test_jan_1(self):
        assert days_until_end_of_year(date(2025, 1, 1)) == 364

    def test_leap_year(self):
        assert days_until_end_of_year(date(2024, 1, 1)) == 365

    def test_datetime_input(self):
        assert days_until_end_of_year(datetime(2025, 6, 15)) == 199

    def test_type_error(self):
        with pytest.raises(TypeError):
            days_until_end_of_year("2025-01-01")

class TestDateOfNthWeekday:
    def test_4th_thursday_nov_2025(self):
        result = date_of_nth_weekday(2025, 11, 3, 4)
        assert result == datetime(2025, 11, 27)

    def test_1st_monday_jan_2025(self):
        result = date_of_nth_weekday(2025, 1, 0, 1)
        assert result == datetime(2025, 1, 6)

    def test_type_error(self):
        with pytest.raises(TypeError):
            date_of_nth_weekday(2025.0, 1, 0, 1)

    def test_invalid_month(self):
        with pytest.raises(ValueError):
            date_of_nth_weekday(2025, 13, 0, 1)

    def test_nonexistent_occurrence(self):
        with pytest.raises(ValueError):
            date_of_nth_weekday(2025, 2, 0, 5)

class TestSemesterOfDate:
    def test_first_semester(self):
        assert semester_of_date(date(2025, 3, 15)) == 1
        assert semester_of_date(date(2025, 6, 30)) == 1

    def test_second_semester(self):
        assert semester_of_date(date(2025, 7, 1)) == 2
        assert semester_of_date(date(2025, 12, 31)) == 2

    def test_datetime_input(self):
        assert semester_of_date(datetime(2025, 1, 1)) == 1

    def test_type_error(self):
        with pytest.raises(TypeError):
            semester_of_date("2025-01-01")

class TestFortnightOfYear:
    def test_first_fortnight(self):
        assert fortnight_of_year(date(2025, 1, 1)) == 1
        assert fortnight_of_year(date(2025, 1, 14)) == 1

    def test_second_fortnight(self):
        assert fortnight_of_year(date(2025, 1, 15)) == 2

    def test_last_day(self):
        result = fortnight_of_year(date(2025, 12, 31))
        assert result >= 26

    def test_datetime_input(self):
        assert fortnight_of_year(datetime(2025, 1, 15)) == 2

    def test_type_error(self):
        with pytest.raises(TypeError):
            fortnight_of_year("2025-01-01")

class TestBimesterOfDate:
    def test_known_values(self):
        assert bimester_of_date(date(2025, 1, 15)) == 1
        assert bimester_of_date(date(2025, 2, 28)) == 1
        assert bimester_of_date(date(2025, 3, 1)) == 2
        assert bimester_of_date(date(2025, 5, 10)) == 3
        assert bimester_of_date(date(2025, 11, 1)) == 6
        assert bimester_of_date(date(2025, 12, 31)) == 6

    def test_type_error(self):
        with pytest.raises(TypeError):
            bimester_of_date("2025-01-01")

class TestTrimesterOfDate:
    def test_known_values(self):
        assert trimester_of_date(date(2025, 1, 1)) == 1
        assert trimester_of_date(date(2025, 4, 30)) == 1
        assert trimester_of_date(date(2025, 5, 1)) == 2
        assert trimester_of_date(date(2025, 8, 31)) == 2
        assert trimester_of_date(date(2025, 9, 1)) == 3
        assert trimester_of_date(date(2025, 12, 31)) == 3

    def test_type_error(self):
        with pytest.raises(TypeError):
            trimester_of_date("2025-01-01")

class TestElapsedYears:
    def test_basic(self):
        assert elapsed_years(date(2000, 6, 15), date(2025, 4, 8)) == 24

    def test_exact_anniversary(self):
        assert elapsed_years(date(2000, 4, 8), date(2025, 4, 8)) == 25

    def test_same_date(self):
        assert elapsed_years(date(2025, 1, 1), date(2025, 1, 1)) == 0

    def test_datetime_input(self):
        assert elapsed_years(datetime(2000, 1, 1), datetime(2025, 1, 1)) == 25

    def test_type_error(self):
        with pytest.raises(TypeError):
            elapsed_years("2000-01-01", date(2025, 1, 1))

    def test_end_before_start(self):
        with pytest.raises(ValueError):
            elapsed_years(date(2025, 1, 1), date(2000, 1, 1))

class TestOrdinalDateString:
    def test_basic(self):
        assert ordinal_date_string(date(2025, 3, 1)) == "2025-060"

    def test_jan_1(self):
        assert ordinal_date_string(date(2025, 1, 1)) == "2025-001"

    def test_dec_31(self):
        assert ordinal_date_string(date(2025, 12, 31)) == "2025-365"

    def test_leap_year(self):
        assert ordinal_date_string(date(2024, 12, 31)) == "2024-366"

    def test_type_error(self):
        with pytest.raises(TypeError):
            ordinal_date_string("2025-01-01")

class TestDateToJulianDay:
    def test_j2000(self):
        assert date_to_julian_day(date(2000, 1, 1)) == 2451545

    def test_known_date(self):
        # 2025-01-01 → JDN 2460677
        assert date_to_julian_day(date(2025, 1, 1)) == 2460677

    def test_datetime_input(self):
        assert date_to_julian_day(datetime(2000, 1, 1)) == 2451545

    def test_type_error(self):
        with pytest.raises(TypeError):
            date_to_julian_day("2000-01-01")

class TestBusinessDaysUntil:
    def test_full_week(self):
        start = date(2024, 1, 1)  # Monday
        end = date(2024, 1, 8)    # Monday
        assert business_days_until(start, end) == 5

    def test_same_day(self):
        d = date(2024, 1, 1)
        assert business_days_until(d, d) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            business_days_until("2024-01-01", date(2024, 1, 8))


# ---------------------------------------------------------------------------
# fxDate — date_evaluations.py
# ---------------------------------------------------------------------------


class TestIsHoliday:
    def test_new_year_spain(self):
        assert is_holiday(date(2024, 1, 1), "ES") is True

    def test_christmas_us(self):
        assert is_holiday(date(2024, 12, 25), "US") is True

    def test_non_holiday(self):
        assert is_holiday(date(2024, 3, 15), "ES") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_holiday("2024-01-01")

    def test_invalid_country(self):
        with pytest.raises(ValueError):
            is_holiday(date(2024, 1, 1), "XX")

class TestAstronomicalSeason:
    def test_summer_north(self):
        assert astronomical_season(date(2024, 7, 15)) == "summer"

    def test_winter_north(self):
        assert astronomical_season(date(2024, 1, 15)) == "winter"

    def test_summer_south(self):
        assert astronomical_season(date(2024, 1, 15), "south") == "summer"

    def test_type_error(self):
        with pytest.raises(TypeError):
            astronomical_season("2024-07-15")

    def test_invalid_hemisphere(self):
        with pytest.raises(ValueError):
            astronomical_season(date(2024, 7, 15), "east")

class TestIsFriday13th:

    def test_true(self):
        assert is_friday_13th(date(2026, 2, 13)) is True

    def test_false_not_friday(self):
        assert is_friday_13th(date(2026, 1, 13)) is False

class TestIsEquinoxOrSolstice:

    def test_summer_solstice(self):
        assert is_equinox_or_solstice(date(2026, 6, 21)) == "summer_solstice"

    def test_none(self):
        assert is_equinox_or_solstice(date(2026, 7, 15)) is None

class TestIsBlueMoon:

    def test_blue_moon_month(self):
        assert is_blue_moon(2024, 12) is True

    def test_no_blue_moon(self):
        assert is_blue_moon(2026, 4) is False

    def test_type_error(self):

        with pytest.raises(TypeError):
            is_blue_moon(2026.5, 1)


# ── fxNumeric ── finance_functions ──────────────────────────────────────

class TestSiderealTime:
    """Local sidereal time computation."""

    def test_sidereal_time_j2000(self):
        from datetime import date
        from shortfx.fxDate.date_evaluations import sidereal_time

        result = sidereal_time(date(2000, 1, 1), 0.0)
        assert 6.0 < result < 7.0

    def test_sidereal_time_with_longitude(self):
        from datetime import date
        from shortfx.fxDate.date_evaluations import sidereal_time

        lst_greenwich = sidereal_time(date(2026, 4, 9), 0.0)
        lst_madrid = sidereal_time(date(2026, 4, 9), -3.7)
        expected_diff = 3.7 / 15.0
        diff = (lst_greenwich - lst_madrid) % 24
        assert abs(diff - expected_diff) < 0.01

    def test_sidereal_time_type_error(self):
        from shortfx.fxDate.date_evaluations import sidereal_time

        with pytest.raises(TypeError):
            sidereal_time("2026-04-09")

    def test_sidereal_time_longitude_error(self):
        from datetime import date
        from shortfx.fxDate.date_evaluations import sidereal_time

        with pytest.raises(ValueError):
            sidereal_time(date(2026, 1, 1), 200.0)

    def test_sidereal_time_range(self):
        from datetime import date
        from shortfx.fxDate.date_evaluations import sidereal_time

        result = sidereal_time(date(2026, 6, 21), 45.0)
        assert 0.0 <= result < 24.0

class TestIsDateInRange:
    def test_in_range(self):
        assert is_date_in_range(date(2024, 6, 15), date(2024, 1, 1), date(2024, 12, 31)) is True

    def test_before_range(self):
        assert is_date_in_range(date(2023, 12, 31), date(2024, 1, 1), date(2024, 12, 31)) is False

    def test_on_boundary(self):
        assert is_date_in_range(date(2024, 1, 1), date(2024, 1, 1), date(2024, 12, 31)) is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_date_in_range("2024-01-01", date(2024, 1, 1), date(2024, 12, 31))

class TestDaysUntilWeekday:
    def test_basic(self):
        # 2024-01-01 is Monday (1), target Friday (5) → 4 days
        assert days_until_weekday(date(2024, 1, 1), 5) == 4

    def test_same_weekday(self):
        assert days_until_weekday(date(2024, 1, 1), 1) == 0

    def test_next_day(self):
        # Monday → Tuesday
        assert days_until_weekday(date(2024, 1, 1), 2) == 1

    def test_type_error(self):
        with pytest.raises(TypeError):
            days_until_weekday("2024-01-01", 5)

    def test_value_error(self):
        with pytest.raises(ValueError):
            days_until_weekday(date(2024, 1, 1), 8)

class TestIsNthWeekday:
    def test_true(self):
        # 2024-01-08 is the 2nd Monday
        assert is_nth_weekday(date(2024, 1, 8), 2, 1) is True

    def test_false_wrong_n(self):
        assert is_nth_weekday(date(2024, 1, 8), 1, 1) is False

    def test_false_wrong_weekday(self):
        assert is_nth_weekday(date(2024, 1, 8), 2, 2) is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_nth_weekday("2024-01-08", 2, 1)

    def test_value_error(self):
        with pytest.raises(ValueError):
            is_nth_weekday(date(2024, 1, 8), 0, 1)

class TestDateGrade:
    def test_contemporary(self):
        assert date_grade(date(2024, 1, 1)) == "contemporary"

    def test_modern(self):
        assert date_grade(date(1900, 1, 1)) == "modern"

    def test_medieval(self):
        assert date_grade(date(1000, 6, 1)) == "medieval"

    def test_ancient(self):
        assert date_grade(date(100, 1, 1)) == "ancient"

    def test_datetime_input(self):
        assert date_grade(datetime(2024, 1, 1, 12, 0)) == "contemporary"

    def test_type_error(self):
        with pytest.raises(TypeError):
            date_grade("2024-01-01")

class TestIsIsoLongYear:

    def test_2020_is_long(self):
        assert is_iso_long_year(2020) is True

    def test_2023_is_not_long(self):
        assert is_iso_long_year(2023) is False

    def test_2015_is_long(self):
        assert is_iso_long_year(2015) is True

    def test_2024_is_not_long(self):
        assert is_iso_long_year(2024) is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_iso_long_year("2020")

    def test_bool_error(self):
        with pytest.raises(TypeError):
            is_iso_long_year(True)

class TestIsWeekday:

    def test_monday(self):
        from shortfx.fxDate.date_evaluations import is_weekday
        assert is_weekday(date(2026, 4, 6)) is True  # Monday

    def test_saturday(self):
        from shortfx.fxDate.date_evaluations import is_weekday
        assert is_weekday(date(2026, 4, 4)) is False  # Saturday

    def test_sunday(self):
        from shortfx.fxDate.date_evaluations import is_weekday
        assert is_weekday(date(2026, 4, 5)) is False  # Sunday

    def test_friday(self):
        from shortfx.fxDate.date_evaluations import is_weekday
        assert is_weekday(date(2026, 4, 10)) is True  # Friday

    def test_datetime_input(self):
        from shortfx.fxDate.date_evaluations import is_weekday
        assert is_weekday(datetime(2026, 4, 6, 10, 30)) is True

class TestZodiacSign:

    def test_leo(self):
        from shortfx.fxDate.date_evaluations import zodiac_sign
        assert zodiac_sign(date(2024, 8, 15)) == "Leo"

    def test_capricorn_dec(self):
        from shortfx.fxDate.date_evaluations import zodiac_sign
        assert zodiac_sign(date(2024, 12, 25)) == "Capricorn"

    def test_capricorn_jan(self):
        from shortfx.fxDate.date_evaluations import zodiac_sign
        assert zodiac_sign(date(2024, 1, 5)) == "Capricorn"

    def test_aries(self):
        from shortfx.fxDate.date_evaluations import zodiac_sign
        assert zodiac_sign(date(2024, 4, 10)) == "Aries"

class TestChineseZodiac:

    def test_dragon(self):
        from shortfx.fxDate.date_evaluations import chinese_zodiac
        assert chinese_zodiac(2024) == "Dragon"

    def test_rat(self):
        from shortfx.fxDate.date_evaluations import chinese_zodiac
        assert chinese_zodiac(2020) == "Rat"

    def test_snake(self):
        from shortfx.fxDate.date_evaluations import chinese_zodiac
        assert chinese_zodiac(2025) == "Snake"

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import chinese_zodiac
        with pytest.raises(TypeError):
            chinese_zodiac(2024.5)

class TestIsFirstOfMonth:

    def test_true(self):
        assert is_first_of_month(date(2024, 1, 1)) is True

    def test_false(self):
        assert is_first_of_month(date(2024, 1, 15)) is False

    def test_datetime_input(self):
        assert is_first_of_month(datetime(2024, 3, 1, 12, 0)) is True


# ──────────────────────────────────────────────
# Date: is_end_of_quarter
# ──────────────────────────────────────────────

class TestIsEndOfQuarter:

    def test_q1_end(self):
        assert is_end_of_quarter(date(2024, 3, 31)) is True

    def test_q2_end(self):
        assert is_end_of_quarter(date(2024, 6, 30)) is True

    def test_q3_end(self):
        assert is_end_of_quarter(date(2024, 9, 30)) is True

    def test_q4_end(self):
        assert is_end_of_quarter(date(2024, 12, 31)) is True

    def test_non_quarter_end(self):
        assert is_end_of_quarter(date(2024, 4, 15)) is False


# ──────────────────────────────────────────────
# Date: is_start_of_quarter
# ──────────────────────────────────────────────

class TestIsStartOfQuarter:

    def test_q1_start(self):
        assert is_start_of_quarter(date(2024, 1, 1)) is True

    def test_q2_start(self):
        assert is_start_of_quarter(date(2024, 4, 1)) is True

    def test_non_quarter_start(self):
        assert is_start_of_quarter(date(2024, 2, 1)) is False


# ──────────────────────────────────────────────
# Date: is_century_year
# ──────────────────────────────────────────────

class TestIsCenturyYear:

    def test_true(self):
        assert is_century_year(2000) is True
        assert is_century_year(1900) is True

    def test_false(self):
        assert is_century_year(2024) is False


# ──────────────────────────────────────────────
# Date: is_millennium_year
# ──────────────────────────────────────────────

class TestIsMillenniumYear:

    def test_true(self):
        assert is_millennium_year(2000) is True

    def test_false(self):
        assert is_millennium_year(2024) is False
        assert is_millennium_year(1900) is False

class TestIsPalindromeDate:

    def test_true(self):
        assert is_palindrome_date(date(2021, 12, 2)) is True  # 20211202

    def test_false(self):
        assert is_palindrome_date(date(2024, 1, 1)) is False

    def test_datetime_input(self):
        assert is_palindrome_date(datetime(2021, 12, 2, 10, 30)) is True


# ──────────────────────────────────────────────
# Date: week_parity
# ──────────────────────────────────────────────

class TestWeekParity:

    def test_even(self):
        assert week_parity(date(2025, 1, 6)) == "even"  # ISO week 2

    def test_odd(self):
        assert week_parity(date(2025, 1, 1)) == "odd"  # ISO week 1


# ──────────────────────────────────────────────
# Date: generation_name
# ──────────────────────────────────────────────

class TestGenerationName:

    def test_silent(self):
        assert generation_name(1940) == "Silent Generation"

    def test_boomer(self):
        assert generation_name(1955) == "Baby Boomer"

    def test_gen_x(self):
        assert generation_name(1975) == "Generation X"

    def test_millennial(self):
        assert generation_name(1990) == "Millennial"

    def test_gen_z(self):
        assert generation_name(2005) == "Generation Z"

    def test_gen_alpha(self):
        assert generation_name(2020) == "Generation Alpha"

    def test_out_of_range_raises(self):
        with pytest.raises(ValueError):
            generation_name(1900)

class TestIsWeekdayV2:

    def test_monday(self):
        from shortfx.fxDate.date_evaluations import is_weekday

        assert is_weekday(date(2025, 6, 9)) is True  # Monday

    def test_sunday(self):
        from shortfx.fxDate.date_evaluations import is_weekday

        assert is_weekday(date(2025, 6, 8)) is False  # Sunday

    def test_saturday(self):
        from shortfx.fxDate.date_evaluations import is_weekday

        assert is_weekday(date(2025, 6, 7)) is False  # Saturday

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import is_weekday

        with pytest.raises(TypeError):
            is_weekday("2025-01-01")

class TestDaysUntilNextBirthday:

    def test_basic(self):
        from shortfx.fxDate.date_evaluations import days_until_next_birthday

        assert days_until_next_birthday(date(1990, 6, 15), date(2025, 6, 10)) == 5

    def test_birthday_today(self):
        from shortfx.fxDate.date_evaluations import days_until_next_birthday

        assert days_until_next_birthday(date(1990, 6, 15), date(2025, 6, 15)) == 0

    def test_birthday_passed(self):
        from shortfx.fxDate.date_evaluations import days_until_next_birthday

        result = days_until_next_birthday(date(1990, 6, 15), date(2025, 6, 20))

        assert result > 300  # next year

    def test_type_error(self):
        from shortfx.fxDate.date_evaluations import days_until_next_birthday

        with pytest.raises(TypeError):
            days_until_next_birthday("1990-06-15")
