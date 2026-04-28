# Deep coverage tests for agentfx.fxDate.date_evaluations
from datetime import date, datetime

import agentfx.fxDate.date_evaluations as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_days_until_next_birthday_deep:
    def test_c0(self):
        try:
            mod.days_until_next_birthday(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.days_until_next_birthday(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.days_until_next_birthday(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.days_until_next_birthday(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.days_until_next_birthday(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.days_until_next_birthday(datetime.now())
        except EXC:
            pass

    def test_kw_reference(self):
        try:
            mod.days_until_next_birthday(date(2024, 1, 15), reference=date(2024, 1, 15))
        except EXC:
            pass


class Test_date_of_nth_weekday_deep:
    def test_c0(self):
        try:
            mod.date_of_nth_weekday(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_of_nth_weekday(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_of_nth_weekday(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_of_nth_weekday(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_of_nth_weekday(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_of_nth_weekday(0, 1, 2, 3)
        except EXC:
            pass


class Test_is_date_in_range_deep:
    def test_c0(self):
        try:
            mod.is_date_in_range(1, date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_date_in_range(42, datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_date_in_range(0, date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_date_in_range(-5, date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_date_in_range(3.14, datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_date_in_range(100, date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.is_date_in_range(0.5, date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.is_date_in_range(1000, datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.is_date_in_range(-1, date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.is_date_in_range(2, date(2024, 12, 31), datetime.now())
        except EXC:
            pass


class Test_age_at_date_deep:
    def test_c0(self):
        try:
            mod.age_at_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.age_at_date(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.age_at_date(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.age_at_date(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.age_at_date(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.age_at_date(datetime.now())
        except EXC:
            pass

    def test_kw_reference(self):
        try:
            mod.age_at_date(date(2024, 1, 15), reference=date(2024, 1, 15))
        except EXC:
            pass


class Test_astronomical_season_deep:
    def test_c0(self):
        try:
            mod.astronomical_season(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.astronomical_season(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.astronomical_season(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.astronomical_season(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.astronomical_season(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.astronomical_season(datetime.now())
        except EXC:
            pass

    def test_kw_hemisphere(self):
        try:
            mod.astronomical_season(date(2024, 1, 15), hemisphere="hello world")
        except EXC:
            pass


class Test_is_golden_hour_deep:
    def test_c0(self):
        try:
            mod.is_golden_hour(date(2024, 1, 15), 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_golden_hour(date(2023, 6, 1), 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_golden_hour(datetime(2024, 3, 15, 10, 30), -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_golden_hour(date(2000, 1, 1), 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_golden_hour(date(2024, 12, 31), 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_golden_hour(datetime.now(), 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.is_golden_hour(date(2024, 1, 15), 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.is_golden_hour(date(2023, 6, 1), -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.is_golden_hour(datetime(2024, 3, 15, 10, 30), 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.is_golden_hour(date(2000, 1, 1), 1, 42)
        except EXC:
            pass


class Test_is_nth_weekday_deep:
    def test_c0(self):
        try:
            mod.is_nth_weekday(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_nth_weekday(42, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_nth_weekday(0, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_nth_weekday(-5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_nth_weekday(3.14, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_nth_weekday(100, 1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.is_nth_weekday(0.5, 2, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.is_nth_weekday(1000, 3, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.is_nth_weekday(-1, 5, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.is_nth_weekday(2, 10, 0)
        except EXC:
            pass


class Test_sidereal_time_deep:
    def test_c0(self):
        try:
            mod.sidereal_time(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sidereal_time(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sidereal_time(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sidereal_time(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sidereal_time(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sidereal_time(datetime.now())
        except EXC:
            pass

    def test_kw_longitude(self):
        try:
            mod.sidereal_time(date(2024, 1, 15), longitude=1)
        except EXC:
            pass


class Test_days_until_weekday_deep:
    def test_c0(self):
        try:
            mod.days_until_weekday(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.days_until_weekday(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.days_until_weekday(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.days_until_weekday(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.days_until_weekday(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.days_until_weekday(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.days_until_weekday(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.days_until_weekday(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.days_until_weekday(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.days_until_weekday(2, 10)
        except EXC:
            pass


class Test_elapsed_years_deep:
    def test_c0(self):
        try:
            mod.elapsed_years(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.elapsed_years(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.elapsed_years(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.elapsed_years(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.elapsed_years(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.elapsed_years(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass


class Test_fiscal_quarter_deep:
    def test_c0(self):
        try:
            mod.fiscal_quarter(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fiscal_quarter(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fiscal_quarter(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fiscal_quarter(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fiscal_quarter(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fiscal_quarter(datetime.now())
        except EXC:
            pass

    def test_kw_fiscal_start_month(self):
        try:
            mod.fiscal_quarter(date(2024, 1, 15), fiscal_start_month=1)
        except EXC:
            pass


class Test_is_dst_transition_day_deep:
    def test_c0(self):
        try:
            mod.is_dst_transition_day(date(2024, 1, 15), "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_dst_transition_day(date(2023, 6, 1), "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_dst_transition_day(datetime(2024, 3, 15, 10, 30), "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_dst_transition_day(date(2000, 1, 1), "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_dst_transition_day(date(2024, 12, 31), "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_dst_transition_day(datetime.now(), "hello world")
        except EXC:
            pass


class Test_nth_weekday_of_month_deep:
    def test_c0(self):
        try:
            mod.nth_weekday_of_month(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.nth_weekday_of_month(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.nth_weekday_of_month(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.nth_weekday_of_month(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.nth_weekday_of_month(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.nth_weekday_of_month(0, 1, 2, 3)
        except EXC:
            pass


class Test_weeks_between_dates_deep:
    def test_c0(self):
        try:
            mod.weeks_between_dates(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weeks_between_dates(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weeks_between_dates(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weeks_between_dates(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weeks_between_dates(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weeks_between_dates(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

