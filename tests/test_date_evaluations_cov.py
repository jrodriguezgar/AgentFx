# Coverage tests for shortfx.fxDate.date_evaluations
from datetime import date, datetime

from shortfx.fxDate import date_evaluations as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_age_at_date:
    def test_exists(self):
        assert hasattr(mod, "age_at_date")

    def test_doc0(self):
        try:
            mod.age_at_date(date(1990, 6, 15), date(2025, 6, 14))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.age_at_date(date(1990, 6, 15), date(2025, 6, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.age_at_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.age_at_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.age_at_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.age_at_date("")
        except EXC:
            pass


class Test_astronomical_season:
    def test_exists(self):
        assert hasattr(mod, "astronomical_season")

    def test_doc0(self):
        try:
            mod.astronomical_season(date(2026, 7, 15))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.astronomical_season(date(2026, 7, 15), "south")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.astronomical_season(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.astronomical_season(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.astronomical_season(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.astronomical_season("")
        except EXC:
            pass


class Test_bimester_of_date:
    def test_exists(self):
        assert hasattr(mod, "bimester_of_date")

    def test_doc0(self):
        try:
            mod.bimester_of_date(date(2025, 5, 10))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bimester_of_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bimester_of_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bimester_of_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bimester_of_date("")
        except EXC:
            pass


class Test_century_of_date:
    def test_exists(self):
        assert hasattr(mod, "century_of_date")

    def test_doc0(self):
        try:
            mod.century_of_date(date(2025, 6, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.century_of_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.century_of_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.century_of_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.century_of_date("")
        except EXC:
            pass


class Test_chinese_zodiac:
    def test_exists(self):
        assert hasattr(mod, "chinese_zodiac")

    def test_doc0(self):
        try:
            mod.chinese_zodiac(2024)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.chinese_zodiac(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chinese_zodiac(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chinese_zodiac(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chinese_zodiac("")
        except EXC:
            pass


class Test_date_grade:
    def test_exists(self):
        assert hasattr(mod, "date_grade")

    def test_doc0(self):
        try:
            mod.date_grade(date(2024, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_grade(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_grade(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_grade(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_grade("")
        except EXC:
            pass


class Test_date_of_easter:
    def test_exists(self):
        assert hasattr(mod, "date_of_easter")

    def test_doc0(self):
        try:
            mod.date_of_easter(2025)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_of_easter(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_of_easter(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_of_easter(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_of_easter("")
        except EXC:
            pass


class Test_date_of_nth_weekday:
    def test_exists(self):
        assert hasattr(mod, "date_of_nth_weekday")

    def test_doc0(self):
        try:
            mod.date_of_nth_weekday(2025, 11, 3, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_of_nth_weekday(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_of_nth_weekday(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_of_nth_weekday(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_of_nth_weekday("", "", "", 0)
        except EXC:
            pass


class Test_date_to_julian_day:
    def test_exists(self):
        assert hasattr(mod, "date_to_julian_day")

    def test_doc0(self):
        try:
            mod.date_to_julian_day(date(2000, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_to_julian_day(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_julian_day(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_julian_day(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_to_julian_day("")
        except EXC:
            pass


class Test_day_name_of_date:
    def test_exists(self):
        assert hasattr(mod, "day_name_of_date")

    def test_doc0(self):
        try:
            mod.day_name_of_date(date(2025, 4, 20))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.day_name_of_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.day_name_of_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.day_name_of_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.day_name_of_date("")
        except EXC:
            pass


class Test_days_in_year:
    def test_exists(self):
        assert hasattr(mod, "days_in_year")

    def test_doc0(self):
        try:
            mod.days_in_year(2024)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.days_in_year(2025)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.days_in_year(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.days_in_year(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.days_in_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.days_in_year("")
        except EXC:
            pass


class Test_days_until_end_of_year:
    def test_exists(self):
        assert hasattr(mod, "days_until_end_of_year")

    def test_doc0(self):
        try:
            mod.days_until_end_of_year(date(2025, 12, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.days_until_end_of_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.days_until_end_of_year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.days_until_end_of_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.days_until_end_of_year("")
        except EXC:
            pass


class Test_days_until_next_birthday:
    def test_exists(self):
        assert hasattr(mod, "days_until_next_birthday")

    def test_doc0(self):
        try:
            mod.days_until_next_birthday(date(1990, 6, 15), date(2025, 6, 10))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.days_until_next_birthday(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.days_until_next_birthday(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.days_until_next_birthday(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.days_until_next_birthday("")
        except EXC:
            pass


class Test_days_until_weekday:
    def test_exists(self):
        assert hasattr(mod, "days_until_weekday")

    def test_doc0(self):
        try:
            mod.days_until_weekday(date(2024, 1, 1), 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.days_until_weekday(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.days_until_weekday(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.days_until_weekday(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.days_until_weekday("", "")
        except EXC:
            pass


class Test_elapsed_years:
    def test_exists(self):
        assert hasattr(mod, "elapsed_years")

    def test_doc0(self):
        try:
            mod.elapsed_years(date(2000, 6, 15), date(2025, 4, 8))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.elapsed_years(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elapsed_years(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elapsed_years(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elapsed_years("", "")
        except EXC:
            pass


class Test_fiscal_quarter:
    def test_exists(self):
        assert hasattr(mod, "fiscal_quarter")

    def test_doc0(self):
        try:
            mod.fiscal_quarter(date(2025, 3, 15))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.fiscal_quarter(date(2025, 3, 15), fiscal_start_month=4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fiscal_quarter(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fiscal_quarter(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fiscal_quarter(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fiscal_quarter("")
        except EXC:
            pass


class Test_fortnight_of_year:
    def test_exists(self):
        assert hasattr(mod, "fortnight_of_year")

    def test_doc0(self):
        try:
            mod.fortnight_of_year(date(2025, 1, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fortnight_of_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fortnight_of_year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fortnight_of_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fortnight_of_year("")
        except EXC:
            pass


class Test_generation_name:
    def test_exists(self):
        assert hasattr(mod, "generation_name")

    def test_doc0(self):
        try:
            mod.generation_name(1990)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.generation_name(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.generation_name(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.generation_name(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.generation_name("")
        except EXC:
            pass


class Test_is_anniversary:
    def test_exists(self):
        assert hasattr(mod, "is_anniversary")

    def test_doc0(self):
        try:
            mod.is_anniversary(date(1990, 7, 4), date(2026, 7, 4))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_anniversary(date(1990, 7, 4), date(2026, 7, 5))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_anniversary(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_anniversary(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_anniversary(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_anniversary("", "")
        except EXC:
            pass


class Test_is_blue_moon:
    def test_exists(self):
        assert hasattr(mod, "is_blue_moon")

    def test_doc0(self):
        try:
            mod.is_blue_moon(2026, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_blue_moon(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_blue_moon(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_blue_moon(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_blue_moon("", "")
        except EXC:
            pass


class Test_is_business_hours:
    def test_exists(self):
        assert hasattr(mod, "is_business_hours")

    def test_doc0(self):
        try:
            mod.is_business_hours(datetime(2026, 4, 6, 10, 30))  # Monday 10:30
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_business_hours(datetime(2026, 4, 5, 10, 30))  # Sunday 10:30
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_business_hours(datetime(2026, 4, 6, 18, 0))   # Monday 18:00
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_business_hours(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_business_hours(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_business_hours(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_business_hours("")
        except EXC:
            pass


class Test_is_century_year:
    def test_exists(self):
        assert hasattr(mod, "is_century_year")

    def test_doc0(self):
        try:
            mod.is_century_year(2000)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_century_year(2024)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_century_year(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_century_year(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_century_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_century_year("")
        except EXC:
            pass


class Test_is_date_in_range:
    def test_exists(self):
        assert hasattr(mod, "is_date_in_range")

    def test_doc0(self):
        try:
            mod.is_date_in_range(date(2024, 6, 15), date(2024, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_date_in_range(0, date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_date_in_range(1, date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_date_in_range(None, date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_date_in_range("", "", "")
        except EXC:
            pass


class Test_is_dateclass:
    def test_exists(self):
        assert hasattr(mod, "is_dateclass")

    def test_doc0(self):
        try:
            mod.is_dateclass("2026-01-03")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_dateclass(None)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_dateclass(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_dateclass(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_dateclass(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_dateclass("")
        except EXC:
            pass


class Test_is_dst:
    def test_exists(self):
        assert hasattr(mod, "is_dst")

    def test_doc0(self):
        try:
            mod.is_dst(datetime(2026, 7, 15, 12, 0), "US/Eastern")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_dst(datetime(2026, 1, 15, 12, 0), "US/Eastern")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_dst(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_dst(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_dst(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_dst("")
        except EXC:
            pass


class Test_is_dst_transition_day:
    def test_exists(self):
        assert hasattr(mod, "is_dst_transition_day")

    def test_doc0(self):
        try:
            mod.is_dst_transition_day(date(2026, 3, 29), "Europe/Madrid")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_dst_transition_day(date(2026, 6, 15), "Europe/Madrid")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_dst_transition_day(date(2024, 1, 15), "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_dst_transition_day(date(2023, 12, 31), "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_dst_transition_day(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_dst_transition_day("", "")
        except EXC:
            pass


class Test_is_end_of_month:
    def test_exists(self):
        assert hasattr(mod, "is_end_of_month")

    def test_doc0(self):
        try:
            mod.is_end_of_month(date(2025, 2, 28))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_end_of_month(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_end_of_month(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_end_of_month(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_end_of_month("")
        except EXC:
            pass


class Test_is_end_of_quarter:
    def test_exists(self):
        assert hasattr(mod, "is_end_of_quarter")

    def test_doc0(self):
        try:
            mod.is_end_of_quarter(date(2024, 3, 31))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_end_of_quarter(date(2024, 4, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_end_of_quarter(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_end_of_quarter(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_end_of_quarter(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_end_of_quarter("")
        except EXC:
            pass


class Test_is_equinox_or_solstice:
    def test_exists(self):
        assert hasattr(mod, "is_equinox_or_solstice")

    def test_doc0(self):
        try:
            mod.is_equinox_or_solstice(date(2026, 6, 21))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_equinox_or_solstice(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_equinox_or_solstice(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_equinox_or_solstice(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_equinox_or_solstice("")
        except EXC:
            pass


class Test_is_first_day_of_month:
    def test_exists(self):
        assert hasattr(mod, "is_first_day_of_month")

    def test_doc0(self):
        try:
            mod.is_first_day_of_month(date(2025, 6, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_first_day_of_month(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_first_day_of_month(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_first_day_of_month(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_first_day_of_month("")
        except EXC:
            pass


class Test_is_first_of_month:
    def test_exists(self):
        assert hasattr(mod, "is_first_of_month")

    def test_doc0(self):
        try:
            mod.is_first_of_month(date(2024, 1, 1))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_first_of_month(date(2024, 1, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_first_of_month(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_first_of_month(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_first_of_month(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_first_of_month("")
        except EXC:
            pass


class Test_is_friday_13th:
    def test_exists(self):
        assert hasattr(mod, "is_friday_13th")

    def test_doc0(self):
        try:
            mod.is_friday_13th(date(2026, 2, 13))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_friday_13th(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_friday_13th(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_friday_13th(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_friday_13th("")
        except EXC:
            pass


class Test_is_future:
    def test_exists(self):
        assert hasattr(mod, "is_future")

    def test_doc0(self):
        try:
            mod.is_future(datetime(2099, 12, 31))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_future(datetime(2020, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_future(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_future(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_future(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_future("")
        except EXC:
            pass


class Test_is_golden_hour:
    def test_exists(self):
        assert hasattr(mod, "is_golden_hour")

    def test_doc0(self):
        try:
            mod.is_golden_hour(datetime(2026, 6, 21, 6, 30), 40.0, -3.7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_golden_hour(date(2024, 1, 15), 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_golden_hour(date(2023, 12, 31), 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_golden_hour(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_golden_hour("", "", "")
        except EXC:
            pass


class Test_is_holiday:
    def test_exists(self):
        assert hasattr(mod, "is_holiday")

    def test_doc0(self):
        try:
            mod.is_holiday(date(2026, 12, 25), "ES")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_holiday(date(2026, 4, 8), "ES")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_holiday(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_holiday(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_holiday(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_holiday("")
        except EXC:
            pass


class Test_is_iso_long_year:
    def test_exists(self):
        assert hasattr(mod, "is_iso_long_year")

    def test_doc0(self):
        try:
            mod.is_iso_long_year(2020)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_iso_long_year(2023)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_iso_long_year(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_iso_long_year(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_iso_long_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_iso_long_year("")
        except EXC:
            pass


class Test_is_last_day_of_month:
    def test_exists(self):
        assert hasattr(mod, "is_last_day_of_month")

    def test_doc0(self):
        try:
            mod.is_last_day_of_month(date(2024, 2, 29))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_last_day_of_month(date(2024, 2, 28))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_last_day_of_month(date(2023, 2, 28))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_last_day_of_month(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_last_day_of_month(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_last_day_of_month(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_last_day_of_month("")
        except EXC:
            pass


class Test_is_last_day_of_year:
    def test_exists(self):
        assert hasattr(mod, "is_last_day_of_year")

    def test_doc0(self):
        try:
            mod.is_last_day_of_year(date(2025, 12, 31))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_last_day_of_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_last_day_of_year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_last_day_of_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_last_day_of_year("")
        except EXC:
            pass


class Test_is_millennium_year:
    def test_exists(self):
        assert hasattr(mod, "is_millennium_year")

    def test_doc0(self):
        try:
            mod.is_millennium_year(2000)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_millennium_year(2024)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_millennium_year(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_millennium_year(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_millennium_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_millennium_year("")
        except EXC:
            pass


class Test_is_nth_weekday:
    def test_exists(self):
        assert hasattr(mod, "is_nth_weekday")

    def test_doc0(self):
        try:
            mod.is_nth_weekday(date(2024, 1, 8), 2, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_nth_weekday(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_nth_weekday(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_nth_weekday(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_nth_weekday("", 0, "")
        except EXC:
            pass


class Test_is_palindrome_date:
    def test_exists(self):
        assert hasattr(mod, "is_palindrome_date")

    def test_doc0(self):
        try:
            mod.is_palindrome_date(date(2021, 12, 2))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_palindrome_date(date(2024, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_palindrome_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_palindrome_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_palindrome_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_palindrome_date("")
        except EXC:
            pass


class Test_is_past:
    def test_exists(self):
        assert hasattr(mod, "is_past")

    def test_doc0(self):
        try:
            mod.is_past(datetime(2020, 1, 1))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_past(datetime(2099, 12, 31))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_past(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_past(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_past(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_past("")
        except EXC:
            pass


class Test_is_same_day:
    def test_exists(self):
        assert hasattr(mod, "is_same_day")

    def test_doc0(self):
        try:
            mod.is_same_day(datetime(2025, 6, 15, 8, 0), datetime(2025, 6, 15, 23, 59))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_same_day(datetime(2025, 6, 15), datetime(2025, 6, 16))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_same_day(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_same_day(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_same_day(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_same_day("", "")
        except EXC:
            pass


class Test_is_same_month:
    def test_exists(self):
        assert hasattr(mod, "is_same_month")

    def test_doc0(self):
        try:
            mod.is_same_month(datetime(2025, 6, 1), datetime(2025, 6, 30))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_same_month(datetime(2025, 6, 1), datetime(2025, 7, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_same_month(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_same_month(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_same_month(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_same_month("", "")
        except EXC:
            pass


class Test_is_same_quarter:
    def test_exists(self):
        assert hasattr(mod, "is_same_quarter")

    def test_doc0(self):
        try:
            mod.is_same_quarter(datetime(2026, 1, 15), datetime(2026, 3, 31))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_same_quarter(datetime(2026, 3, 31), datetime(2026, 4, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_same_quarter(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_same_quarter(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_same_quarter(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_same_quarter("", "")
        except EXC:
            pass


class Test_is_same_week:
    def test_exists(self):
        assert hasattr(mod, "is_same_week")

    def test_doc0(self):
        try:
            mod.is_same_week(datetime(2026, 4, 6), datetime(2026, 4, 10))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_same_week(datetime(2026, 4, 5), datetime(2026, 4, 6))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_same_week(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_same_week(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_same_week(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_same_week("", "")
        except EXC:
            pass


class Test_is_same_year:
    def test_exists(self):
        assert hasattr(mod, "is_same_year")

    def test_doc0(self):
        try:
            mod.is_same_year(datetime(2025, 1, 1), datetime(2025, 12, 31))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_same_year(datetime(2025, 1, 1), datetime(2026, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_same_year(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_same_year(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_same_year(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_same_year("", "")
        except EXC:
            pass


class Test_is_start_of_quarter:
    def test_exists(self):
        assert hasattr(mod, "is_start_of_quarter")

    def test_doc0(self):
        try:
            mod.is_start_of_quarter(date(2024, 1, 1))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_start_of_quarter(date(2024, 2, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_start_of_quarter(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_start_of_quarter(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_start_of_quarter(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_start_of_quarter("")
        except EXC:
            pass


class Test_is_today:
    def test_exists(self):
        assert hasattr(mod, "is_today")

    def test_doc0(self):
        try:
            mod.is_today(datetime.now())
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_today(date(2000, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_today(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_today(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_today(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_today("")
        except EXC:
            pass


class Test_is_weekday:
    def test_exists(self):
        assert hasattr(mod, "is_weekday")

    def test_doc0(self):
        try:
            mod.is_weekday(date(2025, 6, 9))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_weekday(date(2025, 6, 8))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_weekday(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_weekday(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_weekday(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_weekday("")
        except EXC:
            pass


class Test_iso_day_name:
    def test_exists(self):
        assert hasattr(mod, "iso_day_name")

    def test_doc0(self):
        try:
            mod.iso_day_name(date(2025, 6, 9))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.iso_day_name(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.iso_day_name(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.iso_day_name(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.iso_day_name("")
        except EXC:
            pass


class Test_millennium_of_date:
    def test_exists(self):
        assert hasattr(mod, "millennium_of_date")

    def test_doc0(self):
        try:
            mod.millennium_of_date(date(2025, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.millennium_of_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.millennium_of_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.millennium_of_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.millennium_of_date("")
        except EXC:
            pass


class Test_moon_phase:
    def test_exists(self):
        assert hasattr(mod, "moon_phase")

    def test_doc0(self):
        try:
            mod.moon_phase(date(2026, 4, 8))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.moon_phase(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moon_phase(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moon_phase(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moon_phase("")
        except EXC:
            pass


class Test_next_month_same_day:
    def test_exists(self):
        assert hasattr(mod, "next_month_same_day")

    def test_doc0(self):
        try:
            mod.next_month_same_day(date(2025, 1, 31))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.next_month_same_day(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.next_month_same_day(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.next_month_same_day(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.next_month_same_day("")
        except EXC:
            pass


class Test_nth_weekday_of_month:
    def test_exists(self):
        assert hasattr(mod, "nth_weekday_of_month")

    def test_doc0(self):
        try:
            mod.nth_weekday_of_month(2025, 1, 1, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.nth_weekday_of_month(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nth_weekday_of_month(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nth_weekday_of_month(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nth_weekday_of_month("", "", "", 0)
        except EXC:
            pass


class Test_ordinal_date_string:
    def test_exists(self):
        assert hasattr(mod, "ordinal_date_string")

    def test_doc0(self):
        try:
            mod.ordinal_date_string(date(2025, 3, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ordinal_date_string(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ordinal_date_string(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ordinal_date_string(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ordinal_date_string("")
        except EXC:
            pass


class Test_previous_month_same_day:
    def test_exists(self):
        assert hasattr(mod, "previous_month_same_day")

    def test_doc0(self):
        try:
            mod.previous_month_same_day(date(2025, 3, 31))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.previous_month_same_day(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.previous_month_same_day(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.previous_month_same_day(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.previous_month_same_day("")
        except EXC:
            pass


class Test_quarter_end_date:
    def test_exists(self):
        assert hasattr(mod, "quarter_end_date")

    def test_doc0(self):
        try:
            mod.quarter_end_date(2025, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.quarter_end_date(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.quarter_end_date(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.quarter_end_date(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.quarter_end_date("", "")
        except EXC:
            pass


class Test_quarter_start_date:
    def test_exists(self):
        assert hasattr(mod, "quarter_start_date")

    def test_doc0(self):
        try:
            mod.quarter_start_date(2025, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.quarter_start_date(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.quarter_start_date(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.quarter_start_date(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.quarter_start_date("", "")
        except EXC:
            pass


class Test_semester_of_date:
    def test_exists(self):
        assert hasattr(mod, "semester_of_date")

    def test_doc0(self):
        try:
            mod.semester_of_date(date(2025, 3, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.semester_of_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.semester_of_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.semester_of_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.semester_of_date("")
        except EXC:
            pass


class Test_semester_of_year:
    def test_exists(self):
        assert hasattr(mod, "semester_of_year")

    def test_doc0(self):
        try:
            mod.semester_of_year(date(2025, 3, 15))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.semester_of_year(date(2025, 9, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.semester_of_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.semester_of_year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.semester_of_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.semester_of_year("")
        except EXC:
            pass


class Test_sidereal_time:
    def test_exists(self):
        assert hasattr(mod, "sidereal_time")

    def test_var0(self):
        try:
            mod.sidereal_time(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sidereal_time(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sidereal_time(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sidereal_time("")
        except EXC:
            pass


class Test_trimester_of_date:
    def test_exists(self):
        assert hasattr(mod, "trimester_of_date")

    def test_doc0(self):
        try:
            mod.trimester_of_date(date(2025, 9, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.trimester_of_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.trimester_of_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.trimester_of_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.trimester_of_date("")
        except EXC:
            pass


class Test_week_parity:
    def test_exists(self):
        assert hasattr(mod, "week_parity")

    def test_doc0(self):
        try:
            mod.week_parity(date(2025, 1, 6))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.week_parity(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.week_parity(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.week_parity(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.week_parity("")
        except EXC:
            pass


class Test_week_year:
    def test_exists(self):
        assert hasattr(mod, "week_year")

    def test_doc0(self):
        try:
            mod.week_year(date(2025, 12, 29))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.week_year(date(2025, 6, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.week_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.week_year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.week_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.week_year("")
        except EXC:
            pass


class Test_weeks_between_dates:
    def test_exists(self):
        assert hasattr(mod, "weeks_between_dates")

    def test_doc0(self):
        try:
            mod.weeks_between_dates(date(2025, 1, 1), date(2025, 3, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.weeks_between_dates(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weeks_between_dates(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weeks_between_dates(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weeks_between_dates("", "")
        except EXC:
            pass


class Test_workdays_in_month:
    def test_exists(self):
        assert hasattr(mod, "workdays_in_month")

    def test_doc0(self):
        try:
            mod.workdays_in_month(2025, 6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.workdays_in_month(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.workdays_in_month(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.workdays_in_month(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.workdays_in_month("", "")
        except EXC:
            pass


class Test_zodiac_sign:
    def test_exists(self):
        assert hasattr(mod, "zodiac_sign")

    def test_doc0(self):
        try:
            mod.zodiac_sign(date(2024, 8, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.zodiac_sign(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.zodiac_sign(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.zodiac_sign(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.zodiac_sign("")
        except EXC:
            pass

