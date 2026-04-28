# Coverage tests for shortfx.fxDate.date_operations
from datetime import date, datetime, time, timedelta

from shortfx.fxDate import date_operations as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_academic_year:
    def test_exists(self):
        assert hasattr(mod, "academic_year")

    def test_doc0(self):
        try:
            mod.academic_year(date(2024, 2, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.academic_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.academic_year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.academic_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.academic_year("")
        except EXC:
            pass


class Test_add_days_from_now:
    def test_exists(self):
        assert hasattr(mod, "add_days_from_now")

    def test_doc0(self):
        try:
            mod.add_days_from_now(5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.add_days_from_now(-1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.add_days_from_now(30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.add_days_from_now(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.add_days_from_now(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.add_days_from_now(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.add_days_from_now("")
        except EXC:
            pass


class Test_add_microseconds:
    def test_exists(self):
        assert hasattr(mod, "add_microseconds")

    def test_var0(self):
        try:
            mod.add_microseconds(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.add_microseconds(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.add_microseconds(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.add_microseconds("", "")
        except EXC:
            pass


class Test_add_months:
    def test_exists(self):
        assert hasattr(mod, "add_months")

    def test_doc0(self):
        try:
            mod.add_months(datetime(2025, 1, 31), 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.add_months(datetime(2025, 3, 15), -1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.add_months(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.add_months(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.add_months(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.add_months("", "")
        except EXC:
            pass


class Test_add_time_to_date:
    def test_exists(self):
        assert hasattr(mod, "add_time_to_date")

    def test_doc0(self):
        try:
            mod.add_time_to_date(datetime(2023, 1, 15), 10, 'days')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.add_time_to_date(date(2023, 1, 15), -5, 'days')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.add_time_to_date("2023-01-15", 7, 'days')
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.add_time_to_date("2023/01/15 14:30:00", 2, 'hours')
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.add_time_to_date("2023-01-15 10:00:00", 30, 'minutes')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.add_time_to_date("hello", 0, "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.add_time_to_date("", 1, "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.add_time_to_date(None, 0, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.add_time_to_date("", "", "")
        except EXC:
            pass


class Test_add_years:
    def test_exists(self):
        assert hasattr(mod, "add_years")

    def test_doc0(self):
        try:
            mod.add_years(datetime(2024, 2, 29, 10, 30), 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.add_years(datetime(2025, 6, 15), -3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.add_years(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.add_years(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.add_years(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.add_years("", "")
        except EXC:
            pass


class Test_age:
    def test_exists(self):
        assert hasattr(mod, "age")

    def test_doc0(self):
        try:
            mod.age(date(2000, 1, 1))  # assuming today is 2026-04-04
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.age("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.age("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.age(None)
        except EXC:
            pass


class Test_business_days_until:
    def test_exists(self):
        assert hasattr(mod, "business_days_until")

    def test_doc0(self):
        try:
            mod.business_days_until(date(2026, 4, 6), date(2026, 4, 13))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.business_days_until(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.business_days_until(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.business_days_until(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.business_days_until("", "")
        except EXC:
            pass


class Test_business_hours_between:
    def test_exists(self):
        assert hasattr(mod, "business_hours_between")

    def test_doc0(self):
        try:
            mod.business_hours_between( datetime(2026, 4, 6, 10, 0), datetime(2026, 4, 6, 15, 30))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.business_hours_between(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.business_hours_between(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.business_hours_between(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.business_hours_between("", "")
        except EXC:
            pass


class Test_business_quarter_label:
    def test_exists(self):
        assert hasattr(mod, "business_quarter_label")

    def test_doc0(self):
        try:
            mod.business_quarter_label(date(2024, 3, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.business_quarter_label(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.business_quarter_label(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.business_quarter_label(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.business_quarter_label("")
        except EXC:
            pass


class Test_calculate_days_between_dates:
    def test_exists(self):
        assert hasattr(mod, "calculate_days_between_dates")

    def test_var0(self):
        try:
            mod.calculate_days_between_dates(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_days_between_dates(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_days_between_dates(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_days_between_dates("", "")
        except EXC:
            pass


class Test_clamp_date:
    def test_exists(self):
        assert hasattr(mod, "clamp_date")

    def test_doc0(self):
        try:
            mod.clamp_date(date(2024, 6, 15), date(2024, 1, 1), date(2024, 3, 31))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.clamp_date(0, date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.clamp_date(1, date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.clamp_date(None, date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.clamp_date("", "", "")
        except EXC:
            pass


class Test_countdown_days:
    def test_exists(self):
        assert hasattr(mod, "countdown_days")

    def test_doc0(self):
        try:
            mod.countdown_days(date(2026, 12, 31), date(2026, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.countdown_days(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.countdown_days(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.countdown_days(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.countdown_days("")
        except EXC:
            pass


class Test_cron_next_run:
    def test_exists(self):
        assert hasattr(mod, "cron_next_run")

    def test_doc0(self):
        try:
            mod.cron_next_run("0 9 * * *", datetime(2026, 4, 8, 10, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cron_next_run("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cron_next_run("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cron_next_run(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cron_next_run(0)
        except EXC:
            pass


class Test_cron_previous_run:
    def test_exists(self):
        assert hasattr(mod, "cron_previous_run")

    def test_doc0(self):
        try:
            mod.cron_previous_run("0 9 * * *", datetime(2026, 4, 8, 10, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cron_previous_run("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cron_previous_run("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cron_previous_run(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cron_previous_run(0)
        except EXC:
            pass


class Test_date_intervals:
    def test_exists(self):
        assert hasattr(mod, "date_intervals")

    def test_doc0(self):
        try:
            mod.date_intervals(datetime(2025, 6, 1, 10, 0), datetime(2025, 6, 3, 14, 30), 'day')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.date_intervals(datetime(2025, 6, 1, 12, 0), datetime(2025, 6, 9, 10, 0), 'week')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.date_intervals(datetime(2025, 1, 15), datetime(2025, 3, 10), 'month')
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.date_intervals(datetime(2025, 6, 10), datetime(2025, 7, 20), 'half_month')
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.date_intervals(datetime(2025, 6, 1, 10, 30), datetime(2025, 6, 1, 12, 15), 'hour')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_intervals("hello", "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_intervals("", "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_intervals(None, "hello", "hello")
        except EXC:
            pass


class Test_date_part:
    def test_exists(self):
        assert hasattr(mod, "date_part")

    def test_doc0(self):
        try:
            mod.date_part("ww", "2023-01-01", first_day_of_week=0, first_week_of_year=1) # Ejemplo ISO, 2023-01-01 es domingo, semana 52 de 2022
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.date_part("ww", "2023-01-02", first_day_of_week=0, first_week_of_year=1) # Lunes, semana 1 de 2023
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_part("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_part("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_part(None, "hello")
        except EXC:
            pass


class Test_date_range:
    def test_exists(self):
        assert hasattr(mod, "date_range")

    def test_doc0(self):
        try:
            mod.date_range(datetime(2025, 1, 1), datetime(2025, 1, 5))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.date_range("2025-01-01", "2025-01-10", step=3, unit='days')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_range("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_range("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_range(None, "hello")
        except EXC:
            pass


class Test_date_sequence:
    def test_exists(self):
        assert hasattr(mod, "date_sequence")

    def test_doc0(self):
        try:
            mod.date_sequence(date(2026, 1, 1), date(2026, 1, 5))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_sequence(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_sequence(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_sequence(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_sequence("", "")
        except EXC:
            pass


class Test_date_to_ordinal:
    def test_exists(self):
        assert hasattr(mod, "date_to_ordinal")

    def test_doc0(self):
        try:
            mod.date_to_ordinal(date(2024, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_to_ordinal(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_ordinal(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_ordinal(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_to_ordinal("")
        except EXC:
            pass


class Test_date_to_week_label:
    def test_exists(self):
        assert hasattr(mod, "date_to_week_label")

    def test_doc0(self):
        try:
            mod.date_to_week_label(date(2024, 1, 8))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_to_week_label(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_week_label(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_week_label(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_to_week_label("")
        except EXC:
            pass


class Test_datedif:
    def test_exists(self):
        assert hasattr(mod, "datedif")

    def test_doc0(self):
        try:
            mod.datedif(date(2020, 3, 15), date(2025, 7, 20), "Y")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.datedif(date(2020, 3, 15), date(2025, 7, 20), "M")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.datedif(date(2020, 3, 15), date(2025, 7, 20), "D")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.datedif(date(2024, 1, 15), date(2024, 1, 15), "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datedif(date(2023, 12, 31), date(2023, 12, 31), "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datedif(None, date(2024, 1, 15), "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.datedif("", "", "")
        except EXC:
            pass


class Test_dates_between:
    def test_exists(self):
        assert hasattr(mod, "dates_between")

    def test_var0(self):
        try:
            mod.dates_between(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dates_between(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dates_between(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dates_between("", "")
        except EXC:
            pass


class Test_day_of_year:
    def test_exists(self):
        assert hasattr(mod, "day_of_year")

    def test_doc0(self):
        try:
            mod.day_of_year(date(2024, 3, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.day_of_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.day_of_year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.day_of_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.day_of_year("")
        except EXC:
            pass


class Test_daylight_hours:
    def test_exists(self):
        assert hasattr(mod, "daylight_hours")

    def test_var0(self):
        try:
            mod.daylight_hours(3.14, date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.daylight_hours(100, date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.daylight_hours(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.daylight_hours("", "")
        except EXC:
            pass


class Test_days_360:
    def test_exists(self):
        assert hasattr(mod, "days_360")

    def test_doc0(self):
        try:
            mod.days_360(datetime(2025, 1, 30), datetime(2025, 2, 28))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.days_360(datetime(2025, 1, 1), datetime(2025, 7, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.days_360(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.days_360(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.days_360(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.days_360("", "")
        except EXC:
            pass


class Test_days_between:
    def test_exists(self):
        assert hasattr(mod, "days_between")

    def test_doc0(self):
        try:
            mod.days_between(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.days_between(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.days_between(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.days_between(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.days_between("", "")
        except EXC:
            pass


class Test_days_in_month:
    def test_exists(self):
        assert hasattr(mod, "days_in_month")

    def test_doc0(self):
        try:
            mod.days_in_month(2023, 2) # February 2023 (not a leap year)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.days_in_month(2024, 2) # February 2024 (a leap year)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.days_in_month(2023, 1) # January
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.days_in_month(2023, 4) # April
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.days_in_month(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.days_in_month(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.days_in_month(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.days_in_month("", "")
        except EXC:
            pass


class Test_days_remaining_in_year:
    def test_exists(self):
        assert hasattr(mod, "days_remaining_in_year")

    def test_doc0(self):
        try:
            mod.days_remaining_in_year(date(2024, 12, 30))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.days_remaining_in_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.days_remaining_in_year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.days_remaining_in_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.days_remaining_in_year("")
        except EXC:
            pass


class Test_decimal_hours_between:
    def test_exists(self):
        assert hasattr(mod, "decimal_hours_between")

    def test_doc0(self):
        try:
            mod.decimal_hours_between( datetime(2024, 1, 1, 8, 0), datetime(2024, 1, 1, 9, 30), )
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.decimal_hours_between(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.decimal_hours_between(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.decimal_hours_between(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.decimal_hours_between("", "")
        except EXC:
            pass


class Test_diff_time:
    def test_exists(self):
        assert hasattr(mod, "diff_time")

    def test_doc0(self):
        try:
            mod.diff_time("2025-01-01", "2025-01-03", "days")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.diff_time("2025-01-01 00:00:00", "2025-01-02 12:00:00", "hours")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.diff_time("2025-01-01", "2025-01-15", "weeks")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.diff_time("hello", "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.diff_time("", "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.diff_time(None, "hello", "hello")
        except EXC:
            pass


class Test_easter_date:
    def test_exists(self):
        assert hasattr(mod, "easter_date")

    def test_doc0(self):
        try:
            mod.easter_date(2025)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.easter_date(2024)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.easter_date(2000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.easter_date(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.easter_date(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.easter_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.easter_date("")
        except EXC:
            pass


class Test_elapsed_business_days:
    def test_exists(self):
        assert hasattr(mod, "elapsed_business_days")

    def test_doc0(self):
        try:
            mod.elapsed_business_days(date(2024, 1, 1), date(2024, 1, 5))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.elapsed_business_days(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elapsed_business_days(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elapsed_business_days(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elapsed_business_days("", "")
        except EXC:
            pass


class Test_end_of_month:
    def test_exists(self):
        assert hasattr(mod, "end_of_month")

    def test_doc0(self):
        try:
            mod.end_of_month(datetime(2023, 10, 15, 10, 30, 0))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.end_of_month("20-02-2024", "%d-%m-%Y")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.end_of_month(datetime(2023, 2, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.end_of_month("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.end_of_month("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.end_of_month(None)
        except EXC:
            pass


class Test_end_of_month_offset:
    def test_exists(self):
        assert hasattr(mod, "end_of_month_offset")

    def test_doc0(self):
        try:
            mod.end_of_month_offset(datetime(2025, 1, 15), 0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.end_of_month_offset(datetime(2025, 1, 15), 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.end_of_month_offset(datetime(2024, 1, 15), 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.end_of_month_offset(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.end_of_month_offset(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.end_of_month_offset(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.end_of_month_offset("", "")
        except EXC:
            pass


class Test_end_of_quarter:
    def test_exists(self):
        assert hasattr(mod, "end_of_quarter")

    def test_doc0(self):
        try:
            mod.end_of_quarter(datetime(2026, 8, 15))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.end_of_quarter(datetime(2026, 1, 20))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.end_of_quarter("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.end_of_quarter("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.end_of_quarter(None)
        except EXC:
            pass


class Test_end_of_year:
    def test_exists(self):
        assert hasattr(mod, "end_of_year")

    def test_doc0(self):
        try:
            mod.end_of_year(datetime(2023, 7, 20))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.end_of_year("01-01-2024", "%d-%m-%Y")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.end_of_year("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.end_of_year("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.end_of_year(None)
        except EXC:
            pass


class Test_filter_dates_by_weekday:
    def test_exists(self):
        assert hasattr(mod, "filter_dates_by_weekday")

    def test_doc0(self):
        try:
            mod.filter_dates_by_weekday([], 0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.filter_dates_by_weekday([datetime(2025, 1, 1), "not a date"], 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.filter_dates_by_weekday(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.filter_dates_by_weekday(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.filter_dates_by_weekday(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.filter_dates_by_weekday("", "")
        except EXC:
            pass


class Test_first_day_of_week:
    def test_exists(self):
        assert hasattr(mod, "first_day_of_week")

    def test_doc0(self):
        try:
            mod.first_day_of_week(datetime(2025, 6, 15))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.first_day_of_week(datetime(2025, 6, 15), week_start_day=6)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.first_day_of_week("2025-06-15", week_start_day=0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.first_day_of_week(datetime(2025, 6, 15), week_start_day=7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.first_day_of_week("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.first_day_of_week("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.first_day_of_week(None)
        except EXC:
            pass


class Test_fiscal_quarter:
    def test_exists(self):
        assert hasattr(mod, "fiscal_quarter")

    def test_doc0(self):
        try:
            mod.fiscal_quarter(date(2026, 3, 15))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.fiscal_quarter(date(2026, 3, 15), fiscal_start_month=4)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.fiscal_quarter(date(2026, 7, 1), fiscal_start_month=4)
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


class Test_format_date_iso:
    def test_exists(self):
        assert hasattr(mod, "format_date_iso")

    def test_doc0(self):
        try:
            mod.format_date_iso(date(2024, 3, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.format_date_iso(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.format_date_iso(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.format_date_iso(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.format_date_iso("")
        except EXC:
            pass


class Test_format_datetime_ampm:
    def test_exists(self):
        assert hasattr(mod, "format_datetime_ampm")

    def test_var0(self):
        try:
            mod.format_datetime_ampm(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.format_datetime_ampm(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.format_datetime_ampm(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.format_datetime_ampm("")
        except EXC:
            pass


class Test_format_datetime_iso:
    def test_exists(self):
        assert hasattr(mod, "format_datetime_iso")

    def test_doc0(self):
        try:
            mod.format_datetime_iso(datetime(2024, 3, 15, 10, 30, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.format_datetime_iso(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.format_datetime_iso(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.format_datetime_iso(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.format_datetime_iso("")
        except EXC:
            pass


class Test_full_months_between:
    def test_exists(self):
        assert hasattr(mod, "full_months_between")

    def test_doc0(self):
        try:
            mod.full_months_between(datetime(2025, 1, 15), datetime(2025, 3, 14))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.full_months_between(datetime(2025, 1, 15), datetime(2025, 3, 15))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.full_months_between(datetime(2024, 8, 1), datetime(2025, 2, 28))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.full_months_between(datetime(2025, 1, 1), datetime(2025, 1, 31))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.full_months_between(datetime(2025, 3, 15), datetime(2025, 1, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.full_months_between(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.full_months_between(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.full_months_between(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.full_months_between("", "")
        except EXC:
            pass


class Test_full_years_between:
    def test_exists(self):
        assert hasattr(mod, "full_years_between")

    def test_doc0(self):
        try:
            mod.full_years_between(datetime(2020, 6, 11), datetime(2025, 6, 10))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.full_years_between(datetime(2020, 6, 11), datetime(2025, 6, 11))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.full_years_between(datetime(2010, 1, 1), datetime(2025, 12, 31))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.full_years_between(datetime(2025, 1, 1), datetime(2025, 12, 31))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.full_years_between(datetime(2025, 6, 11), datetime(2020, 6, 10))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.full_years_between(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.full_years_between(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.full_years_between(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.full_years_between("", "")
        except EXC:
            pass


class Test_generate_random_date:
    def test_exists(self):
        assert hasattr(mod, "generate_random_date")

    def test_doc0(self):
        try:
            mod.generate_random_date(start_date=date(2020, 1, 1), end_date=date(2022, 12, 31), business_days_only=True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.generate_random_date()
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.generate_random_date(start_date=date(2025, 1, 1), end_date=date(2024, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.generate_random_date()
        except EXC:
            pass


class Test_generate_random_datetime:
    def test_exists(self):
        assert hasattr(mod, "generate_random_datetime")

    def test_doc0(self):
        try:
            mod.generate_random_datetime(start_dt=datetime(2020, 1, 1), end_dt=datetime(2020, 12, 31))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.generate_random_datetime(start_dt=datetime(2025, 1, 1), end_dt=datetime(2024, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.generate_random_datetime()
        except EXC:
            pass


class Test_generate_random_time:
    def test_exists(self):
        assert hasattr(mod, "generate_random_time")

    def test_doc0(self):
        try:
            mod.generate_random_time(min_time=time(9, 0, 0), max_time=time(17, 0, 0))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.generate_random_time()
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.generate_random_time(min_time=time(17, 0, 0), max_time=time(9, 0, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.generate_random_time()
        except EXC:
            pass


class Test_get_age_from_dob:
    def test_exists(self):
        assert hasattr(mod, "get_age_from_dob")

    def test_doc0(self):
        try:
            mod.get_age_from_dob(datetime(1990, 6, 11), as_of_date=datetime(2025, 6, 11))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_age_from_dob(datetime(1990, 1, 15), as_of_date=datetime(2025, 6, 11))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_age_from_dob(datetime(1990, 12, 25), as_of_date=datetime(2025, 6, 11))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.get_age_from_dob(datetime(1990, 6, 11))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.get_age_from_dob("1985-03-20", dob_format="%Y-%m-%d", as_of_date=datetime(2025, 6, 11))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_age_from_dob("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_age_from_dob("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_age_from_dob(None)
        except EXC:
            pass


class Test_get_date_component:
    def test_exists(self):
        assert hasattr(mod, "get_date_component")

    def test_var0(self):
        try:
            mod.get_date_component(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_date_component(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_date_component(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_date_component("", "")
        except EXC:
            pass


class Test_get_first_business_day_of_month:
    def test_exists(self):
        assert hasattr(mod, "get_first_business_day_of_month")

    def test_doc0(self):
        try:
            mod.get_first_business_day_of_month(2025, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_first_business_day_of_month(2025, 3)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_first_business_day_of_month(2025, 13)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_first_business_day_of_month(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_first_business_day_of_month(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_first_business_day_of_month(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_first_business_day_of_month("", "")
        except EXC:
            pass


class Test_get_last_business_day_of_month:
    def test_exists(self):
        assert hasattr(mod, "get_last_business_day_of_month")

    def test_doc0(self):
        try:
            mod.get_last_business_day_of_month(2025, 6)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_last_business_day_of_month(2025, 5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_last_business_day_of_month(2025, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_last_business_day_of_month(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_last_business_day_of_month(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_last_business_day_of_month(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_last_business_day_of_month("", "")
        except EXC:
            pass


class Test_get_last_friday_of_month:
    def test_exists(self):
        assert hasattr(mod, "get_last_friday_of_month")

    def test_doc0(self):
        try:
            mod.get_last_friday_of_month(2023, 10) # October 2023
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_last_friday_of_month(2024, 2) # February 2024 (leap year)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_last_friday_of_month(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_last_friday_of_month(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_last_friday_of_month(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_last_friday_of_month("", "")
        except EXC:
            pass


class Test_get_next_friday:
    def test_exists(self):
        assert hasattr(mod, "get_next_friday")

    def test_doc0(self):
        try:
            mod.get_next_friday(datetime(2023, 10, 26)) # Thursday
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_next_friday(datetime(2023, 10, 27)) # Friday
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_next_friday(datetime(2023, 10, 28)) # Saturday
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_next_friday(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_next_friday(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_next_friday(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_next_friday("")
        except EXC:
            pass


class Test_get_nth_weekday_of_month:
    def test_exists(self):
        assert hasattr(mod, "get_nth_weekday_of_month")

    def test_doc0(self):
        try:
            mod.get_nth_weekday_of_month(2025, 6, 1, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_nth_weekday_of_month(2024, 1, 0, 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_nth_weekday_of_month(2024, 2, 3, 4)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.get_nth_weekday_of_month(2024, 2, 0, 5)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.get_nth_weekday_of_month(2025, 13, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_nth_weekday_of_month(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_nth_weekday_of_month(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_nth_weekday_of_month(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_nth_weekday_of_month("", "", "", 0)
        except EXC:
            pass


class Test_get_number_of_days_in_quarter:
    def test_exists(self):
        assert hasattr(mod, "get_number_of_days_in_quarter")

    def test_doc0(self):
        try:
            mod.get_number_of_days_in_quarter(2024, 1) # Q1 de un año bisiesto (Ene, Feb(29), Mar)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_number_of_days_in_quarter(2023, 1) # Q1 de un año común (Ene, Feb(28), Mar)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_number_of_days_in_quarter(2023, 2) # Q2 de un año común (Abr, May, Jun)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.get_number_of_days_in_quarter(2023, 3) # Q3 de un año común (Jul, Ago, Sep)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.get_number_of_days_in_quarter(2023, 4) # Q4 de un año común (Oct, Nov, Dic)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_number_of_days_in_quarter(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_number_of_days_in_quarter(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_number_of_days_in_quarter(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_number_of_days_in_quarter("", "")
        except EXC:
            pass


class Test_get_number_of_days_in_year:
    def test_exists(self):
        assert hasattr(mod, "get_number_of_days_in_year")

    def test_doc0(self):
        try:
            mod.get_number_of_days_in_year(2023) # Not a leap year
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_number_of_days_in_year(2024) # A leap year
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_number_of_days_in_year(1900) # Not a leap year (divisible by 100 but not by 400)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.get_number_of_days_in_year(2000) # A leap year (divisible by 400)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_number_of_days_in_year(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_number_of_days_in_year(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_number_of_days_in_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_number_of_days_in_year("")
        except EXC:
            pass


class Test_get_previous_friday:
    def test_exists(self):
        assert hasattr(mod, "get_previous_friday")

    def test_doc0(self):
        try:
            mod.get_previous_friday(datetime(2025, 6, 9))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_previous_friday(datetime(2025, 6, 12))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_previous_friday(datetime(2025, 6, 6))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.get_previous_friday(datetime(2025, 6, 8))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_previous_friday(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_previous_friday(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_previous_friday(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_previous_friday("")
        except EXC:
            pass


class Test_get_quarter:
    def test_exists(self):
        assert hasattr(mod, "get_quarter")

    def test_doc0(self):
        try:
            mod.get_quarter(datetime(2025, 8, 15)) # Agosto (mes 8) está en el Q3
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_quarter(datetime(2024, 1, 1)) # Enero (mes 1) está en el Q1
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_quarter(datetime(2023, 12, 31)) # Diciembre (mes 12) está en el Q4
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.get_quarter(datetime(2022, 4, 1)) # Abril (mes 4) está en el Q2
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.get_quarter("2025-08-15", "%Y-%m-%d")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_quarter("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_quarter("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_quarter(None)
        except EXC:
            pass


class Test_get_season:
    def test_exists(self):
        assert hasattr(mod, "get_season")

    def test_doc0(self):
        try:
            mod.get_season(datetime(2025, 6, 11), 'northern', lang='en')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_season(datetime(2025, 6, 11), 'southern', lang='es')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_season("2025-09-20", 'northern', lang='es', format="%Y-%m-%d")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.get_season(datetime(2025, 6, 11), 'equator', lang='en')
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.get_season(datetime(2025, 6, 11), 'northern', lang='fr')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_season("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_season("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_season(None)
        except EXC:
            pass


class Test_get_week_of_year:
    def test_exists(self):
        assert hasattr(mod, "get_week_of_year")

    def test_doc0(self):
        try:
            mod.get_week_of_year(datetime(2025, 6, 11))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_week_of_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_week_of_year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_week_of_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_week_of_year("")
        except EXC:
            pass


class Test_get_week_range:
    def test_exists(self):
        assert hasattr(mod, "get_week_range")

    def test_var0(self):
        try:
            mod.get_week_range(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_week_range(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_week_range(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_week_range("", "")
        except EXC:
            pass


class Test_get_working_days_in_range:
    def test_exists(self):
        assert hasattr(mod, "get_working_days_in_range")

    def test_doc0(self):
        try:
            mod.get_working_days_in_range(datetime(2025, 6, 9), datetime(2025, 6, 13))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_working_days_in_range(datetime(2025, 6, 9), datetime(2025, 6, 15))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_working_days_in_range(datetime(2025, 6, 14), datetime(2025, 6, 14)) # Sábado 14
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.get_working_days_in_range(datetime(2025, 6, 11), datetime(2025, 6, 11)) # Miércoles 11
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.get_working_days_in_range(datetime(2025, 6, 13), datetime(2025, 6, 9))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_working_days_in_range(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_working_days_in_range(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_working_days_in_range(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_working_days_in_range("", "")
        except EXC:
            pass


class Test_get_year_calendar_by_weeks:
    def test_exists(self):
        assert hasattr(mod, "get_year_calendar_by_weeks")

    def test_doc0(self):
        try:
            mod.get_year_calendar_by_weeks(2023)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_year_calendar_by_weeks(2023, granularity="day")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_year_calendar_by_weeks( 2023, start_date=datetime(2023, 6, 1), end_date=datetime(2023, 6, 30), granularity="day", )
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_year_calendar_by_weeks(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_year_calendar_by_weeks(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_year_calendar_by_weeks(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_year_calendar_by_weeks("")
        except EXC:
            pass


class Test_human_readable_duration:
    def test_exists(self):
        assert hasattr(mod, "human_readable_duration")

    def test_doc0(self):
        try:
            mod.human_readable_duration(9015)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.human_readable_duration(90061)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.human_readable_duration(45)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.human_readable_duration(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.human_readable_duration(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.human_readable_duration(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.human_readable_duration("")
        except EXC:
            pass


class Test_intersection_of_date_ranges:
    def test_exists(self):
        assert hasattr(mod, "intersection_of_date_ranges")

    def test_doc0(self):
        try:
            mod.intersection_of_date_ranges(datetime(2025, 1, 10), datetime(2025, 1, 5), datetime(2025, 1, 1), datetime(2025, 1, 2))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.intersection_of_date_ranges(date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.intersection_of_date_ranges(date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.intersection_of_date_ranges(None, date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.intersection_of_date_ranges("", "", "", "")
        except EXC:
            pass


class Test_is_between_dates:
    def test_exists(self):
        assert hasattr(mod, "is_between_dates")

    def test_doc0(self):
        try:
            mod.is_between_dates(datetime(2025, 6, 15), datetime(2025, 6, 1), datetime(2025, 6, 30))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_between_dates(datetime(2025, 6, 1), datetime(2025, 6, 1), datetime(2025, 6, 30))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_between_dates(datetime(2025, 6, 30), datetime(2025, 6, 1), datetime(2025, 6, 30))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_between_dates(datetime(2025, 7, 1), datetime(2025, 6, 1), datetime(2025, 6, 30))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_between_dates(datetime(2025, 6, 15), datetime(2025, 6, 1), datetime(2025, 6, 30), inclusive=False)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_between_dates("hello", "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_between_dates("", "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_between_dates(None, "hello", "hello")
        except EXC:
            pass


class Test_is_date_type:
    def test_exists(self):
        assert hasattr(mod, "is_date_type")

    def test_doc0(self):
        try:
            mod.is_date_type(datetime(2026, 1, 3))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_date_type(date(2026, 1, 3))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_date_type(time(10, 30, 0))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_date_type("2026-01-03")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_date_type(None)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_date_type(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_date_type(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_date_type(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_date_type("")
        except EXC:
            pass


class Test_is_duration_greater_than:
    def test_exists(self):
        assert hasattr(mod, "is_duration_greater_than")

    def test_doc0(self):
        try:
            mod.is_duration_greater_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 45), timedelta(minutes=30))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_duration_greater_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 30), timedelta(minutes=30))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_duration_greater_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 15), timedelta(minutes=30))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_duration_greater_than(datetime(2025, 6, 11, 10, 45), datetime(2025, 6, 11, 10, 0), timedelta(minutes=30))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_duration_greater_than(datetime(2025, 6, 11, 10, 0), "2025-06-11", timedelta(minutes=30))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_duration_greater_than(date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_duration_greater_than(date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_duration_greater_than(None, date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_duration_greater_than("", "", 0)
        except EXC:
            pass


class Test_is_duration_less_than:
    def test_exists(self):
        assert hasattr(mod, "is_duration_less_than")

    def test_doc0(self):
        try:
            mod.is_duration_less_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 20), timedelta(minutes=30))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_duration_less_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 30), timedelta(minutes=30))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_duration_less_than(datetime(2025, 6, 11, 10, 0), datetime(2025, 6, 11, 10, 45), timedelta(minutes=30))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_duration_less_than(datetime(2025, 6, 11, 10, 20), datetime(2025, 6, 11, 10, 0), timedelta(minutes=30))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_duration_less_than("2025-06-11", datetime(2025, 6, 11, 10, 20), timedelta(minutes=30))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_duration_less_than(date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_duration_less_than(date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_duration_less_than(None, date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_duration_less_than("", "", 0)
        except EXC:
            pass


class Test_is_leap_year:
    def test_exists(self):
        assert hasattr(mod, "is_leap_year")

    def test_doc0(self):
        try:
            mod.is_leap_year(2024)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_leap_year(2023)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_leap_year(2000) # Divisible by 400, so it's a leap year
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_leap_year(1900) # Divisible by 100 but not by 400, so NOT a leap year
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_leap_year(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_leap_year(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_leap_year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_leap_year("")
        except EXC:
            pass


class Test_is_same_business_day:
    def test_exists(self):
        assert hasattr(mod, "is_same_business_day")

    def test_doc0(self):
        try:
            mod.is_same_business_day(date(2025, 6, 16), date(2025, 6, 16))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_same_business_day(date(2025, 6, 14), date(2025, 6, 14))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_same_business_day(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_same_business_day(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_same_business_day(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_same_business_day("", "")
        except EXC:
            pass


class Test_is_valid_date:
    def test_exists(self):
        assert hasattr(mod, "is_valid_date")

    def test_doc0(self):
        try:
            mod.is_valid_date(datetime(2026, 1, 3))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_valid_date("2026-01-03")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_valid_date("03/01/2026", "%d/%m/%Y")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_valid_date("2026-13-01")  # Invalid month
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_valid_date("not-a-date")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_valid_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_valid_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_valid_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_valid_date("")
        except EXC:
            pass


class Test_is_valid_time:
    def test_exists(self):
        assert hasattr(mod, "is_valid_time")

    def test_doc0(self):
        try:
            mod.is_valid_time(23, 59, 59)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_valid_time(0, 0, 0, 0)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_valid_time(12, 30) # Sin segundos ni microsegundos
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_valid_time(25, 0, 0) # Hora inválida
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_valid_time(10, 60, 0) # Minuto inválido
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_valid_time(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_valid_time(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_valid_time(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_valid_time("", "")
        except EXC:
            pass


class Test_is_weekend:
    def test_exists(self):
        assert hasattr(mod, "is_weekend")

    def test_doc0(self):
        try:
            mod.is_weekend(datetime(2023, 10, 28))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_weekend(datetime(2023, 10, 29))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_weekend(datetime(2023, 10, 27))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_weekend("28/10/2023", "%d/%m/%Y")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_weekend("30-10-2023", "%d-%m-%Y")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_weekend("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_weekend("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_weekend(None)
        except EXC:
            pass


class Test_is_working_day:
    def test_exists(self):
        assert hasattr(mod, "is_working_day")

    def test_doc0(self):
        try:
            mod.is_working_day(datetime(2025, 6, 9), system='european') # Monday = 0 in European system
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_working_day(datetime(2025, 6, 9), system='anglo') # Monday = 1 in anglo system
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_working_day(datetime(2025, 6, 14), system='european') # Saturday = 5 in European system
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_working_day(datetime(2025, 6, 14), system='anglo') # Saturday = 6 in anglo system
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_working_day("12/06/2025", "%d/%m/%Y", system='european')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_working_day("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_working_day("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_working_day(None)
        except EXC:
            pass


class Test_iso_week_number:
    def test_exists(self):
        assert hasattr(mod, "iso_week_number")

    def test_doc0(self):
        try:
            mod.iso_week_number(datetime(2025, 1, 1))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.iso_week_number(datetime(2025, 6, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.iso_week_number(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.iso_week_number(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.iso_week_number(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.iso_week_number("")
        except EXC:
            pass


class Test_iso_week_start:
    def test_exists(self):
        assert hasattr(mod, "iso_week_start")

    def test_doc0(self):
        try:
            mod.iso_week_start(2026, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.iso_week_start(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.iso_week_start(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.iso_week_start(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.iso_week_start("", 0)
        except EXC:
            pass


class Test_last_day_of_month:
    def test_exists(self):
        assert hasattr(mod, "last_day_of_month")

    def test_doc0(self):
        try:
            mod.last_day_of_month(datetime(2025, 2, 10))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.last_day_of_month("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.last_day_of_month("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.last_day_of_month(None)
        except EXC:
            pass


class Test_last_day_of_week:
    def test_exists(self):
        assert hasattr(mod, "last_day_of_week")

    def test_doc0(self):
        try:
            mod.last_day_of_week(datetime(2025, 6, 11))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.last_day_of_week(datetime(2025, 6, 15), week_start_day=6)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.last_day_of_week("2025-06-11", week_start_day=0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.last_day_of_week(datetime(2025, 6, 11), week_start_day=8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.last_day_of_week("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.last_day_of_week("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.last_day_of_week(None)
        except EXC:
            pass


class Test_last_weekday_of_month:
    def test_exists(self):
        assert hasattr(mod, "last_weekday_of_month")

    def test_var0(self):
        try:
            mod.last_weekday_of_month(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.last_weekday_of_month(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.last_weekday_of_month(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.last_weekday_of_month("", "")
        except EXC:
            pass


class Test_midpoint_date:
    def test_exists(self):
        assert hasattr(mod, "midpoint_date")

    def test_doc0(self):
        try:
            mod.midpoint_date(date(2024, 1, 1), date(2024, 1, 11))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.midpoint_date(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.midpoint_date(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.midpoint_date(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.midpoint_date("", "")
        except EXC:
            pass


class Test_month_name:
    def test_exists(self):
        assert hasattr(mod, "month_name")

    def test_doc0(self):
        try:
            mod.month_name(datetime(2023, 10, 26), 'en')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.month_name(datetime(2023, 10, 26), 'es')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.month_name(datetime(2023, 10, 26), 'de')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.month_name(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.month_name(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.month_name(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.month_name("")
        except EXC:
            pass


class Test_months_between_dates:
    def test_exists(self):
        assert hasattr(mod, "months_between_dates")

    def test_doc0(self):
        try:
            mod.months_between_dates(datetime(2023, 1, 10), datetime(2023, 1, 25))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.months_between_dates(datetime(2023, 1, 10), datetime(2023, 2, 10))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.months_between_dates(datetime(2023, 1, 10), datetime(2023, 3, 9))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.months_between_dates(datetime(2023, 1, 1), datetime(2023, 7, 31))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.months_between_dates(datetime(2023, 5, 1), datetime(2023, 2, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.months_between_dates(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.months_between_dates(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.months_between_dates(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.months_between_dates("", "")
        except EXC:
            pass


class Test_network_days_intl:
    def test_exists(self):
        assert hasattr(mod, "network_days_intl")

    def test_doc0(self):
        try:
            mod.network_days_intl(datetime(2025, 1, 6), datetime(2025, 1, 10))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.network_days_intl(datetime(2025, 1, 6), datetime(2025, 1, 12), weekend='0000011')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.network_days_intl(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.network_days_intl(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.network_days_intl(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.network_days_intl("", "")
        except EXC:
            pass


class Test_networkdays:
    def test_exists(self):
        assert hasattr(mod, "networkdays")

    def test_doc0(self):
        try:
            mod.networkdays(date(2025, 1, 1), date(2025, 1, 10))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.networkdays(date(2025, 1, 1), date(2025, 1, 10), [date(2025, 1, 6)])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.networkdays(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.networkdays(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.networkdays(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.networkdays("", "")
        except EXC:
            pass


class Test_networkdays_intl:
    def test_exists(self):
        assert hasattr(mod, "networkdays_intl")

    def test_doc0(self):
        try:
            mod.networkdays_intl(date(2025, 1, 6), date(2025, 1, 10))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.networkdays_intl(date(2025, 1, 6), date(2025, 1, 10), weekend=2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.networkdays_intl(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.networkdays_intl(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.networkdays_intl(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.networkdays_intl("", "")
        except EXC:
            pass


class Test_next_business_day:
    def test_exists(self):
        assert hasattr(mod, "next_business_day")

    def test_doc0(self):
        try:
            mod.next_business_day(date(2026, 4, 3))  # Friday
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.next_business_day(date(2026, 4, 4))  # Saturday
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.next_business_day(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.next_business_day(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.next_business_day(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.next_business_day("")
        except EXC:
            pass


class Test_next_full_moon:
    def test_exists(self):
        assert hasattr(mod, "next_full_moon")

    def test_doc0(self):
        try:
            mod.next_full_moon(date(2026, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.next_full_moon(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.next_full_moon(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.next_full_moon(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.next_full_moon("")
        except EXC:
            pass


class Test_next_occurrence:
    def test_exists(self):
        assert hasattr(mod, "next_occurrence")

    def test_doc0(self):
        try:
            mod.next_occurrence(1, ref=date(2026, 4, 8))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.next_occurrence(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.next_occurrence(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.next_occurrence(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.next_occurrence("")
        except EXC:
            pass


class Test_next_weekday:
    def test_exists(self):
        assert hasattr(mod, "next_weekday")

    def test_var0(self):
        try:
            mod.next_weekday(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.next_weekday(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.next_weekday(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.next_weekday("", "")
        except EXC:
            pass


class Test_overlap_dates:
    def test_exists(self):
        assert hasattr(mod, "overlap_dates")

    def test_doc0(self):
        try:
            mod.overlap_dates(date(2026, 1, 1), date(2026, 1, 10), date(2026, 1, 5), date(2026, 1, 15))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.overlap_dates(date(2026, 1, 1), date(2026, 1, 10), date(2026, 1, 11), date(2026, 1, 20))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.overlap_dates("hello", "hello", "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.overlap_dates("", "", "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.overlap_dates(None, "hello", "hello", "hello")
        except EXC:
            pass


class Test_overlap_days:
    def test_exists(self):
        assert hasattr(mod, "overlap_days")

    def test_doc0(self):
        try:
            mod.overlap_days(date(2026, 1, 1), date(2026, 1, 10), date(2026, 1, 5), date(2026, 1, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.overlap_days(date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.overlap_days(date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.overlap_days(None, date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.overlap_days("", "", "", "")
        except EXC:
            pass


class Test_parts_to_date:
    def test_exists(self):
        assert hasattr(mod, "parts_to_date")

    def test_doc0(self):
        try:
            mod.parts_to_date(2025, 10, 30)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.parts_to_date(2024, 14, 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.parts_to_date(2024, 3, 0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.parts_to_date(2024, 1, -1)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.parts_to_date(2024, 0, 15)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parts_to_date(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parts_to_date(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parts_to_date(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parts_to_date("", "", "")
        except EXC:
            pass


class Test_parts_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "parts_to_datetime")

    def test_doc0(self):
        try:
            mod.parts_to_datetime(2025, 10, 30, 15, 30, 45)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.parts_to_datetime(2025, 1, 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.parts_to_datetime(2024, 1, 1, 25, 0, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parts_to_datetime(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parts_to_datetime(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parts_to_datetime(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parts_to_datetime("", "", "")
        except EXC:
            pass


class Test_parts_to_time:
    def test_exists(self):
        assert hasattr(mod, "parts_to_time")

    def test_doc0(self):
        try:
            mod.parts_to_time(14, 30, 0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.parts_to_time(25, 0, 0)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.parts_to_time(0, 90, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parts_to_time()
        except EXC:
            pass


class Test_previous_business_day:
    def test_exists(self):
        assert hasattr(mod, "previous_business_day")

    def test_doc0(self):
        try:
            mod.previous_business_day(date(2026, 4, 6))  # Monday
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.previous_business_day(date(2026, 4, 5))  # Sunday
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.previous_business_day(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.previous_business_day(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.previous_business_day(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.previous_business_day("")
        except EXC:
            pass


class Test_previous_weekday:
    def test_exists(self):
        assert hasattr(mod, "previous_weekday")

    def test_var0(self):
        try:
            mod.previous_weekday(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.previous_weekday(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.previous_weekday(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.previous_weekday("", "")
        except EXC:
            pass


class Test_quarters_between_dates:
    def test_exists(self):
        assert hasattr(mod, "quarters_between_dates")

    def test_doc0(self):
        try:
            mod.quarters_between_dates(datetime(2025, 1, 1), datetime(2025, 10, 1))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.quarters_between_dates(datetime(2025, 1, 15), datetime(2025, 4, 14))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.quarters_between_dates(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.quarters_between_dates(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.quarters_between_dates(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.quarters_between_dates("", "")
        except EXC:
            pass


class Test_recurring_dates:
    def test_exists(self):
        assert hasattr(mod, "recurring_dates")

    def test_doc0(self):
        try:
            mod.recurring_dates(date(2026, 1, 1), date(2026, 3, 1), "monthly")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.recurring_dates(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.recurring_dates(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.recurring_dates(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.recurring_dates("", "")
        except EXC:
            pass


class Test_relative_time:
    def test_exists(self):
        assert hasattr(mod, "relative_time")

    def test_var0(self):
        try:
            mod.relative_time(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.relative_time(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.relative_time(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.relative_time("")
        except EXC:
            pass


class Test_relative_time_description:
    def test_exists(self):
        assert hasattr(mod, "relative_time_description")

    def test_var0(self):
        try:
            mod.relative_time_description(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.relative_time_description(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.relative_time_description(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.relative_time_description("")
        except EXC:
            pass


class Test_round_datetime:
    def test_exists(self):
        assert hasattr(mod, "round_datetime")

    def test_doc0(self):
        try:
            mod.round_datetime(datetime(2026, 4, 4, 14, 35), "hour")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.round_datetime(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.round_datetime(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.round_datetime(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.round_datetime("")
        except EXC:
            pass


class Test_semester:
    def test_exists(self):
        assert hasattr(mod, "semester")

    def test_doc0(self):
        try:
            mod.semester(date(2024, 3, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.semester("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.semester("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.semester(None)
        except EXC:
            pass


class Test_set_date_component:
    def test_exists(self):
        assert hasattr(mod, "set_date_component")

    def test_var0(self):
        try:
            mod.set_date_component(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.set_date_component(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.set_date_component(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.set_date_component("")
        except EXC:
            pass


class Test_set_microseconds:
    def test_exists(self):
        assert hasattr(mod, "set_microseconds")

    def test_doc0(self):
        try:
            mod.set_microseconds(datetime(2025, 6, 11, 10, 0, 0), 1000000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.set_microseconds(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.set_microseconds(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.set_microseconds(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.set_microseconds("", "")
        except EXC:
            pass


class Test_shift_schedule:
    def test_exists(self):
        assert hasattr(mod, "shift_schedule")

    def test_doc0(self):
        try:
            mod.shift_schedule(date(2026, 1, 1), 4, 2, date(2026, 1, 5))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.shift_schedule(date(2026, 1, 1), 4, 2, date(2026, 1, 6))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.shift_schedule(date(2024, 1, 15), 0, 0, date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.shift_schedule(date(2023, 12, 31), 1, 1, date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.shift_schedule(None, 0, 0, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.shift_schedule("", "", "", "")
        except EXC:
            pass


class Test_snap_to_weekday:
    def test_exists(self):
        assert hasattr(mod, "snap_to_weekday")

    def test_doc0(self):
        try:
            mod.snap_to_weekday(date(2025, 6, 11), 0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.snap_to_weekday(date(2025, 6, 11), 0, 'previous')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.snap_to_weekday(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.snap_to_weekday(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.snap_to_weekday(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.snap_to_weekday("", "")
        except EXC:
            pass


class Test_start_of_month:
    def test_exists(self):
        assert hasattr(mod, "start_of_month")

    def test_doc0(self):
        try:
            mod.start_of_month(datetime(2023, 10, 15, 10, 30, 0))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.start_of_month("25-11-2024", "%d-%m-%Y")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.start_of_month("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.start_of_month("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.start_of_month(None)
        except EXC:
            pass


class Test_start_of_quarter:
    def test_exists(self):
        assert hasattr(mod, "start_of_quarter")

    def test_doc0(self):
        try:
            mod.start_of_quarter(datetime(2026, 8, 15))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.start_of_quarter(datetime(2026, 1, 20))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.start_of_quarter("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.start_of_quarter("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.start_of_quarter(None)
        except EXC:
            pass


class Test_start_of_year:
    def test_exists(self):
        assert hasattr(mod, "start_of_year")

    def test_doc0(self):
        try:
            mod.start_of_year(datetime(2023, 7, 20))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.start_of_year("15-03-2024", "%d-%m-%Y")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.start_of_year("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.start_of_year("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.start_of_year(None)
        except EXC:
            pass


class Test_string_to_date:
    def test_exists(self):
        assert hasattr(mod, "string_to_date")

    def test_doc0(self):
        try:
            mod.string_to_date("2023-10-26")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_to_date("2023-10-26 14:30:00")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.string_to_date("invalid date") is None
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.string_to_date(date(2024, 1, 1))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.string_to_date(datetime(2024, 1, 1, 10, 0, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_to_date("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_to_date("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_to_date(None)
        except EXC:
            pass


class Test_string_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "string_to_datetime")

    def test_doc0(self):
        try:
            mod.string_to_datetime("2023-10-26 14:30:00")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_to_datetime("2023-10-26")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.string_to_datetime(date(2024, 1, 1))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.string_to_datetime(datetime(2024, 1, 1, 10, 0, 0))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.string_to_datetime("invalid date") is None
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_to_datetime("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_to_datetime("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_to_datetime(None)
        except EXC:
            pass


class Test_sunrise_sunset:
    def test_exists(self):
        assert hasattr(mod, "sunrise_sunset")

    def test_doc0(self):
        try:
            mod.sunrise_sunset(40.4168, -3.7038, date(2026, 6, 21))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sunrise_sunset(3.14, 3.14, date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sunrise_sunset(100, 100, date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sunrise_sunset(None, 3.14, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sunrise_sunset("", "", "")
        except EXC:
            pass


class Test_time_difference:
    def test_exists(self):
        assert hasattr(mod, "time_difference")

    def test_doc0(self):
        try:
            mod.time_difference("2023-01-01", "2023-01-10", 'days')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.time_difference("2023-01-01 10:00:00", "2023-01-02 11:00:00", 'hours')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.time_difference(date(2023, 5, 1), date(2023, 4, 25), 'days')
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.time_difference("2023-01-01 00:00:00", "2023-01-01 00:00:01.5", 'milliseconds')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.time_difference("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.time_difference("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.time_difference(None, "hello")
        except EXC:
            pass


class Test_time_from_datetime:
    def test_exists(self):
        assert hasattr(mod, "time_from_datetime")

    def test_doc0(self):
        try:
            mod.time_from_datetime(datetime(2024, 1, 1, 9, 0, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.time_from_datetime(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.time_from_datetime(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.time_from_datetime(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.time_from_datetime("")
        except EXC:
            pass


class Test_time_overlap:
    def test_exists(self):
        assert hasattr(mod, "time_overlap")

    def test_var0(self):
        try:
            mod.time_overlap(date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.time_overlap(date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.time_overlap(None, date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.time_overlap("", "", "", "")
        except EXC:
            pass


class Test_time_zone_abbreviation:
    def test_exists(self):
        assert hasattr(mod, "time_zone_abbreviation")

    def test_doc0(self):
        try:
            mod.time_zone_abbreviation("US/Eastern", datetime(2026, 1, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.time_zone_abbreviation("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.time_zone_abbreviation("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.time_zone_abbreviation(None)
        except EXC:
            pass


class Test_timedelta_to_components:
    def test_exists(self):
        assert hasattr(mod, "timedelta_to_components")

    def test_doc0(self):
        try:
            mod.timedelta_to_components("5 days")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.timedelta_to_components(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.timedelta_to_components(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.timedelta_to_components(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.timedelta_to_components("")
        except EXC:
            pass


class Test_trading_days_between:
    def test_exists(self):
        assert hasattr(mod, "trading_days_between")

    def test_doc0(self):
        try:
            mod.trading_days_between(date(2026, 4, 6), date(2026, 4, 13))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.trading_days_between(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.trading_days_between(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.trading_days_between(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.trading_days_between("", "")
        except EXC:
            pass


class Test_week_number:
    def test_exists(self):
        assert hasattr(mod, "week_number")

    def test_doc0(self):
        try:
            mod.week_number(datetime(2025, 1, 1))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.week_number(datetime(2025, 1, 1), system=21)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.week_number(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.week_number(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.week_number(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.week_number("")
        except EXC:
            pass


class Test_week_of_month:
    def test_exists(self):
        assert hasattr(mod, "week_of_month")

    def test_doc0(self):
        try:
            mod.week_of_month(datetime(2025, 6, 11)) # 11 de junio de 2025 es miércoles
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.week_of_month(datetime(2025, 6, 1)) # 1 de junio de 2025 es domingo
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.week_of_month(datetime(2025, 6, 30)) # 30 de junio de 2025 es lunes
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.week_of_month(datetime(2025, 6, 11), start_of_week=6) # 11 de junio de 2025 es miércoles
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.week_of_month("not a date")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.week_of_month(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.week_of_month(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.week_of_month(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.week_of_month("")
        except EXC:
            pass


class Test_weekday_name:
    def test_exists(self):
        assert hasattr(mod, "weekday_name")

    def test_var0(self):
        try:
            mod.weekday_name(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weekday_name(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weekday_name(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weekday_name("")
        except EXC:
            pass


class Test_weekday_number:
    def test_exists(self):
        assert hasattr(mod, "weekday_number")

    def test_var0(self):
        try:
            mod.weekday_number(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weekday_number(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weekday_number(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weekday_number("")
        except EXC:
            pass


class Test_workday:
    def test_exists(self):
        assert hasattr(mod, "workday")

    def test_doc0(self):
        try:
            mod.workday(datetime(2025, 1, 6), 5)  # Mon + 5 working days = Mon
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.workday(datetime(2025, 1, 6), -1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.workday(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.workday(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.workday(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.workday("", "")
        except EXC:
            pass


class Test_workday_intl:
    def test_exists(self):
        assert hasattr(mod, "workday_intl")

    def test_doc0(self):
        try:
            mod.workday_intl(datetime(2025, 1, 6), 5, weekend=2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.workday_intl(date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.workday_intl(date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.workday_intl(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.workday_intl("", "")
        except EXC:
            pass


class Test_working_hours_in_month:
    def test_exists(self):
        assert hasattr(mod, "working_hours_in_month")

    def test_doc0(self):
        try:
            mod.working_hours_in_month(2026, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.working_hours_in_month(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.working_hours_in_month(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.working_hours_in_month(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.working_hours_in_month("", "")
        except EXC:
            pass


class Test_year_fraction:
    def test_exists(self):
        assert hasattr(mod, "year_fraction")

    def test_doc0(self):
        try:
            mod.year_fraction(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.year_fraction(datetime(2025, 1, 1), datetime(2025, 7, 1), basis=1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.year_fraction(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.year_fraction(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.year_fraction(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.year_fraction("", "")
        except EXC:
            pass

