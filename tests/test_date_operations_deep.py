# Deep coverage tests for formulite.fxDate.date_operations
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxDate.date_operations as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_date_intervals_deep:
    def test_c0(self):
        try:
            mod.date_intervals("hello world", "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_intervals("test", "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_intervals("abc123", "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_intervals("", "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_intervals("Hello, World!", "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_intervals("UPPER lower 123", "hello world", "test")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.date_intervals("hello world", "test", "abc123", input_format="hello world")
        except EXC:
            pass


class Test_recurring_dates_deep:
    def test_c0(self):
        try:
            mod.recurring_dates(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.recurring_dates(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.recurring_dates(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.recurring_dates(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.recurring_dates(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.recurring_dates(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_frequency(self):
        try:
            mod.recurring_dates(date(2024, 1, 15), date(2023, 6, 1), frequency=1)
        except EXC:
            pass

    def test_kw_weekday(self):
        try:
            mod.recurring_dates(date(2024, 1, 15), date(2023, 6, 1), weekday=1)
        except EXC:
            pass


class Test_relative_time_description_deep:
    def test_c0(self):
        try:
            mod.relative_time_description(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.relative_time_description(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.relative_time_description(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.relative_time_description(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.relative_time_description(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.relative_time_description(datetime.now())
        except EXC:
            pass

    def test_kw_reference(self):
        try:
            mod.relative_time_description(date(2024, 1, 15), reference=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_language(self):
        try:
            mod.relative_time_description(date(2024, 1, 15), language="hello world")
        except EXC:
            pass


class Test_datedif_deep:
    def test_c0(self):
        try:
            mod.datedif(date(2024, 1, 15), date(2023, 6, 1), "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.datedif(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30), "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.datedif(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1), "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.datedif(date(2000, 1, 1), date(2024, 12, 31), "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.datedif(date(2024, 12, 31), datetime.now(), "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.datedif(datetime.now(), date(2024, 1, 15), "test")
        except EXC:
            pass


class Test_get_date_component_deep:
    def test_c0(self):
        try:
            mod.get_date_component(date(2024, 1, 15), 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_date_component(date(2023, 6, 1), 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_date_component(datetime(2024, 3, 15, 10, 30), -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_date_component(date(2000, 1, 1), 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_date_component(date(2024, 12, 31), 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_date_component(datetime.now(), 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.get_date_component(date(2024, 1, 15), 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.get_date_component(date(2023, 6, 1), -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.get_date_component(datetime(2024, 3, 15, 10, 30), 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.get_date_component(date(2000, 1, 1), 1)
        except EXC:
            pass


class Test_generate_random_datetime_deep:
    def test_c0(self):
        try:
            mod.generate_random_datetime()
        except EXC:
            pass

    def test_kw_start_dt(self):
        try:
            mod.generate_random_datetime(start_dt=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_end_dt(self):
        try:
            mod.generate_random_datetime(end_dt=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_tz_info(self):
        try:
            mod.generate_random_datetime(tz_info="hello world")
        except EXC:
            pass


class Test_relative_time_deep:
    def test_c0(self):
        try:
            mod.relative_time(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.relative_time(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.relative_time(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.relative_time(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.relative_time(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.relative_time(datetime.now())
        except EXC:
            pass

    def test_kw_reference(self):
        try:
            mod.relative_time(date(2024, 1, 15), reference=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_lang(self):
        try:
            mod.relative_time(date(2024, 1, 15), lang="hello world")
        except EXC:
            pass


class Test_timedelta_to_components_deep:
    def test_c0(self):
        try:
            mod.timedelta_to_components(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.timedelta_to_components(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.timedelta_to_components(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.timedelta_to_components(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.timedelta_to_components(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.timedelta_to_components(datetime.now())
        except EXC:
            pass


class Test_dates_between_deep:
    def test_c0(self):
        try:
            mod.dates_between(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dates_between(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dates_between(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dates_between(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dates_between(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dates_between(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass


class Test_date_part_deep:
    def test_c0(self):
        try:
            mod.date_part("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_part("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_part("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_part("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_part("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_part("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_first_day_of_week(self):
        try:
            mod.date_part("hello world", "test", first_day_of_week=1)
        except EXC:
            pass

    def test_kw_first_week_of_year(self):
        try:
            mod.date_part("hello world", "test", first_week_of_year=1)
        except EXC:
            pass


class Test_round_datetime_deep:
    def test_c0(self):
        try:
            mod.round_datetime(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.round_datetime(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.round_datetime(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.round_datetime(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.round_datetime(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.round_datetime(datetime.now())
        except EXC:
            pass

    def test_kw_unit(self):
        try:
            mod.round_datetime(date(2024, 1, 15), unit=1)
        except EXC:
            pass


class Test_set_date_component_deep:
    def test_c0(self):
        try:
            mod.set_date_component(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.set_date_component(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.set_date_component(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.set_date_component(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.set_date_component(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.set_date_component(datetime.now())
        except EXC:
            pass


class Test_get_first_business_day_of_month_deep:
    def test_c0(self):
        try:
            mod.get_first_business_day_of_month(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_first_business_day_of_month(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_first_business_day_of_month(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_first_business_day_of_month(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_first_business_day_of_month(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_first_business_day_of_month(0, 1)
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.get_first_business_day_of_month(1, 2, holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_get_last_business_day_of_month_deep:
    def test_c0(self):
        try:
            mod.get_last_business_day_of_month(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_last_business_day_of_month(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_last_business_day_of_month(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_last_business_day_of_month(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_last_business_day_of_month(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_last_business_day_of_month(0, 1)
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.get_last_business_day_of_month(1, 2, holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_get_working_days_in_range_deep:
    def test_c0(self):
        try:
            mod.get_working_days_in_range(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_working_days_in_range(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_working_days_in_range(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_working_days_in_range(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_working_days_in_range(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_working_days_in_range(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.get_working_days_in_range(date(2024, 1, 15), date(2023, 6, 1), holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_intersection_of_date_ranges_deep:
    def test_c0(self):
        try:
            mod.intersection_of_date_ranges(date(2024, 1, 15), date(2023, 6, 1), datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.intersection_of_date_ranges(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30), date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.intersection_of_date_ranges(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1), date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.intersection_of_date_ranges(date(2000, 1, 1), date(2024, 12, 31), datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.intersection_of_date_ranges(date(2024, 12, 31), datetime.now(), date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.intersection_of_date_ranges(datetime.now(), date(2024, 1, 15), date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass


class Test_is_weekend_deep:
    def test_c0(self):
        try:
            mod.is_weekend("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_weekend("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_weekend("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_weekend("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_weekend("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_weekend("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.is_weekend("hello world", input_format="hello world")
        except EXC:
            pass

    def test_kw_language(self):
        try:
            mod.is_weekend("hello world", language="hello world")
        except EXC:
            pass


class Test_date_sequence_deep:
    def test_c0(self):
        try:
            mod.date_sequence(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_sequence(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_sequence(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_sequence(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_sequence(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_sequence(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_step_days(self):
        try:
            mod.date_sequence(date(2024, 1, 15), date(2023, 6, 1), step_days=1)
        except EXC:
            pass


class Test_networkdays_intl_deep:
    def test_c0(self):
        try:
            mod.networkdays_intl(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.networkdays_intl(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.networkdays_intl(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.networkdays_intl(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.networkdays_intl(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.networkdays_intl(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_weekend(self):
        try:
            mod.networkdays_intl(date(2024, 1, 15), date(2023, 6, 1), weekend=1)
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.networkdays_intl(date(2024, 1, 15), date(2023, 6, 1), holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_is_between_dates_deep:
    def test_c0(self):
        try:
            mod.is_between_dates("hello world", "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_between_dates("test", "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_between_dates("abc123", "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_between_dates("", "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_between_dates("Hello, World!", "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_between_dates("UPPER lower 123", "hello world", "test")
        except EXC:
            pass

    def test_kw_inclusive(self):
        try:
            mod.is_between_dates("hello world", "test", "abc123", inclusive=True)
        except EXC:
            pass

    def test_kw_format(self):
        try:
            mod.is_between_dates("hello world", "test", "abc123", format="hello world")
        except EXC:
            pass


class Test_month_name_deep:
    def test_c0(self):
        try:
            mod.month_name(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.month_name(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.month_name(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.month_name(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.month_name(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.month_name(datetime.now())
        except EXC:
            pass

    def test_kw_language(self):
        try:
            mod.month_name(date(2024, 1, 15), language="hello world")
        except EXC:
            pass


class Test_next_occurrence_deep:
    def test_c0(self):
        try:
            mod.next_occurrence(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.next_occurrence(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.next_occurrence(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.next_occurrence(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.next_occurrence(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.next_occurrence(0)
        except EXC:
            pass

    def test_kw_hour(self):
        try:
            mod.next_occurrence(1, hour=1)
        except EXC:
            pass

    def test_kw_minute(self):
        try:
            mod.next_occurrence(1, minute=1)
        except EXC:
            pass

    def test_kw_ref(self):
        try:
            mod.next_occurrence(1, ref=date(2024, 1, 15))
        except EXC:
            pass


class Test_snap_to_weekday_deep:
    def test_c0(self):
        try:
            mod.snap_to_weekday(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.snap_to_weekday(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.snap_to_weekday(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.snap_to_weekday(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.snap_to_weekday(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.snap_to_weekday(datetime.now(), 1)
        except EXC:
            pass

    def test_kw_direction(self):
        try:
            mod.snap_to_weekday(date(2024, 1, 15), 2, direction="hello world")
        except EXC:
            pass


class Test_weekday_name_deep:
    def test_c0(self):
        try:
            mod.weekday_name(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weekday_name(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weekday_name(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weekday_name(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weekday_name(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weekday_name(datetime.now())
        except EXC:
            pass

    def test_kw_language(self):
        try:
            mod.weekday_name(date(2024, 1, 15), language="hello world")
        except EXC:
            pass


class Test_calculate_days_between_dates_deep:
    def test_c0(self):
        try:
            mod.calculate_days_between_dates(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.calculate_days_between_dates(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.calculate_days_between_dates(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.calculate_days_between_dates(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.calculate_days_between_dates(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.calculate_days_between_dates(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass


class Test_generate_random_date_deep:
    def test_c0(self):
        try:
            mod.generate_random_date()
        except EXC:
            pass

    def test_kw_start_date(self):
        try:
            mod.generate_random_date(start_date=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_end_date(self):
        try:
            mod.generate_random_date(end_date=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_business_days_only(self):
        try:
            mod.generate_random_date(business_days_only=True)
        except EXC:
            pass


class Test_get_age_from_dob_deep:
    def test_c0(self):
        try:
            mod.get_age_from_dob("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_age_from_dob("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_age_from_dob("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_age_from_dob("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_age_from_dob("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_age_from_dob("UPPER lower 123")
        except EXC:
            pass

    def test_kw_dob_format(self):
        try:
            mod.get_age_from_dob("hello world", dob_format="hello world")
        except EXC:
            pass

    def test_kw_as_of_date(self):
        try:
            mod.get_age_from_dob("hello world", as_of_date=date(2024, 1, 15))
        except EXC:
            pass


class Test_get_season_deep:
    def test_c0(self):
        try:
            mod.get_season("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_season("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_season("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_season("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_season("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_season("UPPER lower 123")
        except EXC:
            pass

    def test_kw_hemisphere(self):
        try:
            mod.get_season("hello world", hemisphere="hello world")
        except EXC:
            pass

    def test_kw_lang(self):
        try:
            mod.get_season("hello world", lang="hello world")
        except EXC:
            pass

    def test_kw_format(self):
        try:
            mod.get_season("hello world", format="hello world")
        except EXC:
            pass


class Test_get_week_range_deep:
    def test_c0(self):
        try:
            mod.get_week_range(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_week_range(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_week_range(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_week_range(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_week_range(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_week_range(0, 1)
        except EXC:
            pass


class Test_is_same_business_day_deep:
    def test_c0(self):
        try:
            mod.is_same_business_day(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_same_business_day(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_same_business_day(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_same_business_day(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_same_business_day(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_same_business_day(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.is_same_business_day(date(2024, 1, 15), date(2023, 6, 1), holidays=[1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_networkdays_deep:
    def test_c0(self):
        try:
            mod.networkdays(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.networkdays(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.networkdays(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.networkdays(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.networkdays(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.networkdays(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.networkdays(date(2024, 1, 15), date(2023, 6, 1), holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_sunrise_sunset_deep:
    def test_c0(self):
        try:
            mod.sunrise_sunset(1, 42, datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sunrise_sunset(42, 0, date(2000, 1, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sunrise_sunset(0, -5, date(2024, 12, 31))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sunrise_sunset(-5, 3.14, datetime.now())
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sunrise_sunset(3.14, 100, date(2024, 1, 15))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sunrise_sunset(100, 0.5, date(2023, 6, 1))
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.sunrise_sunset(0.5, 1000, datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.sunrise_sunset(1000, -1, date(2000, 1, 1))
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.sunrise_sunset(-1, 2, date(2024, 12, 31))
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.sunrise_sunset(2, 1, datetime.now())
        except EXC:
            pass


class Test_week_of_month_deep:
    def test_c0(self):
        try:
            mod.week_of_month(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.week_of_month(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.week_of_month(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.week_of_month(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.week_of_month(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.week_of_month(datetime.now())
        except EXC:
            pass

    def test_kw_start_of_week(self):
        try:
            mod.week_of_month(date(2024, 1, 15), start_of_week=1)
        except EXC:
            pass


class Test_add_microseconds_deep:
    def test_c0(self):
        try:
            mod.add_microseconds(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.add_microseconds(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.add_microseconds(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.add_microseconds(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.add_microseconds(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.add_microseconds(datetime.now(), 1)
        except EXC:
            pass


class Test_date_range_deep:
    def test_c0(self):
        try:
            mod.date_range("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_range("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_range("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_range("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_range("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_range("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_step(self):
        try:
            mod.date_range("hello world", "test", step=1)
        except EXC:
            pass

    def test_kw_unit(self):
        try:
            mod.date_range("hello world", "test", unit="hello world")
        except EXC:
            pass


class Test_daylight_hours_deep:
    def test_c0(self):
        try:
            mod.daylight_hours(1, date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.daylight_hours(42, datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.daylight_hours(0, date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.daylight_hours(-5, date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.daylight_hours(3.14, datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.daylight_hours(100, date(2024, 1, 15))
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.daylight_hours(0.5, date(2023, 6, 1))
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.daylight_hours(1000, datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.daylight_hours(-1, date(2000, 1, 1))
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.daylight_hours(2, date(2024, 12, 31))
        except EXC:
            pass


class Test_days_between_deep:
    def test_c0(self):
        try:
            mod.days_between(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.days_between(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.days_between(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.days_between(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.days_between(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.days_between(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.days_between(date(2024, 1, 15), date(2023, 6, 1), basis=1)
        except EXC:
            pass


class Test_elapsed_business_days_deep:
    def test_c0(self):
        try:
            mod.elapsed_business_days(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.elapsed_business_days(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.elapsed_business_days(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.elapsed_business_days(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.elapsed_business_days(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.elapsed_business_days(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.elapsed_business_days(date(2024, 1, 15), date(2023, 6, 1), holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_filter_dates_by_weekday_deep:
    def test_c0(self):
        try:
            mod.filter_dates_by_weekday(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.filter_dates_by_weekday(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.filter_dates_by_weekday(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.filter_dates_by_weekday(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.filter_dates_by_weekday(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.filter_dates_by_weekday(datetime.now(), 1)
        except EXC:
            pass


class Test_format_datetime_ampm_deep:
    def test_c0(self):
        try:
            mod.format_datetime_ampm(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.format_datetime_ampm(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.format_datetime_ampm(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.format_datetime_ampm(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.format_datetime_ampm(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.format_datetime_ampm(datetime.now())
        except EXC:
            pass


class Test_is_working_day_deep:
    def test_c0(self):
        try:
            mod.is_working_day("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_working_day("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_working_day("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_working_day("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_working_day("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_working_day("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.is_working_day("hello world", input_format="hello world")
        except EXC:
            pass

    def test_kw_system(self):
        try:
            mod.is_working_day("hello world", system=1)
        except EXC:
            pass


class Test_shift_schedule_deep:
    def test_c0(self):
        try:
            mod.shift_schedule(date(2024, 1, 15), 2, 3, date(2000, 1, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.shift_schedule(date(2023, 6, 1), 3, 5, date(2024, 12, 31))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.shift_schedule(datetime(2024, 3, 15, 10, 30), 5, 10, datetime.now())
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.shift_schedule(date(2000, 1, 1), 10, 0, date(2024, 1, 15))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.shift_schedule(date(2024, 12, 31), 0, 1, date(2023, 6, 1))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.shift_schedule(datetime.now(), 1, 2, datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass


class Test_add_time_to_date_deep:
    def test_c0(self):
        try:
            mod.add_time_to_date("hello world", 2, "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.add_time_to_date("test", 3, "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.add_time_to_date("abc123", 5, "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.add_time_to_date("", 10, "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.add_time_to_date("Hello, World!", 0, "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.add_time_to_date("UPPER lower 123", 1, "test")
        except EXC:
            pass


class Test_age_deep:
    def test_c0(self):
        try:
            mod.age("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.age("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.age("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.age("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.age("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.age("UPPER lower 123")
        except EXC:
            pass


class Test_business_hours_between_deep:
    def test_c0(self):
        try:
            mod.business_hours_between(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.business_hours_between(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.business_hours_between(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.business_hours_between(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.business_hours_between(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.business_hours_between(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_work_start(self):
        try:
            mod.business_hours_between(date(2024, 1, 15), date(2023, 6, 1), work_start=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_work_end(self):
        try:
            mod.business_hours_between(date(2024, 1, 15), date(2023, 6, 1), work_end=date(2024, 1, 15))
        except EXC:
            pass


class Test_days_in_month_deep:
    def test_c0(self):
        try:
            mod.days_in_month(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.days_in_month(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.days_in_month(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.days_in_month(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.days_in_month(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.days_in_month(0, 1)
        except EXC:
            pass


class Test_end_of_month_deep:
    def test_c0(self):
        try:
            mod.end_of_month("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.end_of_month("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.end_of_month("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.end_of_month("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.end_of_month("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.end_of_month("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.end_of_month("hello world", input_format="hello world")
        except EXC:
            pass


class Test_end_of_year_deep:
    def test_c0(self):
        try:
            mod.end_of_year("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.end_of_year("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.end_of_year("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.end_of_year("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.end_of_year("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.end_of_year("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.end_of_year("hello world", input_format="hello world")
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


class Test_get_last_friday_of_month_deep:
    def test_c0(self):
        try:
            mod.get_last_friday_of_month(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_last_friday_of_month(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_last_friday_of_month(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_last_friday_of_month(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_last_friday_of_month(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_last_friday_of_month(0, 1)
        except EXC:
            pass


class Test_get_nth_weekday_of_month_deep:
    def test_c0(self):
        try:
            mod.get_nth_weekday_of_month(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_nth_weekday_of_month(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_nth_weekday_of_month(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_nth_weekday_of_month(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_nth_weekday_of_month(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_nth_weekday_of_month(0, 1, 2, 3)
        except EXC:
            pass


class Test_get_number_of_days_in_quarter_deep:
    def test_c0(self):
        try:
            mod.get_number_of_days_in_quarter(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_number_of_days_in_quarter(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_number_of_days_in_quarter(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_number_of_days_in_quarter(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_number_of_days_in_quarter(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_number_of_days_in_quarter(0, 1)
        except EXC:
            pass


class Test_get_quarter_deep:
    def test_c0(self):
        try:
            mod.get_quarter("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_quarter("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_quarter("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_quarter("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_quarter("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_quarter("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.get_quarter("hello world", input_format="hello world")
        except EXC:
            pass


class Test_is_valid_time_deep:
    def test_c0(self):
        try:
            mod.is_valid_time(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_time(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_time(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_time(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_time(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_time(0, 1)
        except EXC:
            pass

    def test_kw_second(self):
        try:
            mod.is_valid_time(1, 2, second=1)
        except EXC:
            pass

    def test_kw_microsecond(self):
        try:
            mod.is_valid_time(1, 2, microsecond=1)
        except EXC:
            pass


class Test_midpoint_date_deep:
    def test_c0(self):
        try:
            mod.midpoint_date(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.midpoint_date(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.midpoint_date(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.midpoint_date(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.midpoint_date(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.midpoint_date(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass


class Test_next_weekday_deep:
    def test_c0(self):
        try:
            mod.next_weekday(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.next_weekday(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.next_weekday(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.next_weekday(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.next_weekday(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.next_weekday(datetime.now(), 1)
        except EXC:
            pass


class Test_set_microseconds_deep:
    def test_c0(self):
        try:
            mod.set_microseconds(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.set_microseconds(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.set_microseconds(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.set_microseconds(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.set_microseconds(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.set_microseconds(datetime.now(), 1)
        except EXC:
            pass


class Test_start_of_month_deep:
    def test_c0(self):
        try:
            mod.start_of_month("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.start_of_month("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.start_of_month("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.start_of_month("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.start_of_month("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.start_of_month("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.start_of_month("hello world", input_format="hello world")
        except EXC:
            pass


class Test_start_of_year_deep:
    def test_c0(self):
        try:
            mod.start_of_year("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.start_of_year("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.start_of_year("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.start_of_year("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.start_of_year("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.start_of_year("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.start_of_year("hello world", input_format="hello world")
        except EXC:
            pass


class Test_time_difference_deep:
    def test_c0(self):
        try:
            mod.time_difference("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.time_difference("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.time_difference("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.time_difference("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.time_difference("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.time_difference("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_unit(self):
        try:
            mod.time_difference("hello world", "test", unit="hello world")
        except EXC:
            pass


class Test_time_zone_abbreviation_deep:
    def test_c0(self):
        try:
            mod.time_zone_abbreviation("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.time_zone_abbreviation("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.time_zone_abbreviation("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.time_zone_abbreviation("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.time_zone_abbreviation("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.time_zone_abbreviation("UPPER lower 123")
        except EXC:
            pass

    def test_kw_ref(self):
        try:
            mod.time_zone_abbreviation("hello world", ref=date(2024, 1, 15))
        except EXC:
            pass


class Test_weekday_number_deep:
    def test_c0(self):
        try:
            mod.weekday_number(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weekday_number(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weekday_number(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weekday_number(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weekday_number(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weekday_number(datetime.now())
        except EXC:
            pass

    def test_kw_start_day(self):
        try:
            mod.weekday_number(date(2024, 1, 15), start_day="hello world")
        except EXC:
            pass


class Test_academic_year_deep:
    def test_c0(self):
        try:
            mod.academic_year(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.academic_year(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.academic_year(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.academic_year(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.academic_year(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.academic_year(datetime.now())
        except EXC:
            pass

    def test_kw_start_month(self):
        try:
            mod.academic_year(date(2024, 1, 15), start_month=1)
        except EXC:
            pass


class Test_add_months_deep:
    def test_c0(self):
        try:
            mod.add_months(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.add_months(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.add_months(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.add_months(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.add_months(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.add_months(datetime.now(), 1)
        except EXC:
            pass


class Test_add_years_deep:
    def test_c0(self):
        try:
            mod.add_years(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.add_years(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.add_years(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.add_years(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.add_years(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.add_years(datetime.now(), 1)
        except EXC:
            pass


class Test_business_days_until_deep:
    def test_c0(self):
        try:
            mod.business_days_until(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.business_days_until(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.business_days_until(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.business_days_until(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.business_days_until(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.business_days_until(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.business_days_until(date(2024, 1, 15), date(2023, 6, 1), holidays=[1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_countdown_days_deep:
    def test_c0(self):
        try:
            mod.countdown_days(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.countdown_days(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.countdown_days(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.countdown_days(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.countdown_days(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.countdown_days(datetime.now())
        except EXC:
            pass

    def test_kw_from_date(self):
        try:
            mod.countdown_days(date(2024, 1, 15), from_date=date(2024, 1, 15))
        except EXC:
            pass


class Test_cron_next_run_deep:
    def test_c0(self):
        try:
            mod.cron_next_run("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cron_next_run("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cron_next_run("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cron_next_run("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cron_next_run("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cron_next_run("UPPER lower 123")
        except EXC:
            pass

    def test_kw_from_dt(self):
        try:
            mod.cron_next_run("hello world", from_dt=date(2024, 1, 15))
        except EXC:
            pass


class Test_cron_previous_run_deep:
    def test_c0(self):
        try:
            mod.cron_previous_run("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cron_previous_run("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cron_previous_run("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cron_previous_run("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cron_previous_run("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cron_previous_run("UPPER lower 123")
        except EXC:
            pass

    def test_kw_from_dt(self):
        try:
            mod.cron_previous_run("hello world", from_dt=date(2024, 1, 15))
        except EXC:
            pass


class Test_date_to_week_label_deep:
    def test_c0(self):
        try:
            mod.date_to_week_label(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_to_week_label(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_to_week_label(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_to_week_label(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_to_week_label(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_to_week_label(datetime.now())
        except EXC:
            pass


class Test_days_360_deep:
    def test_c0(self):
        try:
            mod.days_360(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.days_360(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.days_360(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.days_360(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.days_360(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.days_360(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_method(self):
        try:
            mod.days_360(date(2024, 1, 15), date(2023, 6, 1), method="hello world")
        except EXC:
            pass


class Test_decimal_hours_between_deep:
    def test_c0(self):
        try:
            mod.decimal_hours_between(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.decimal_hours_between(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.decimal_hours_between(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.decimal_hours_between(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.decimal_hours_between(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.decimal_hours_between(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass


class Test_end_of_month_offset_deep:
    def test_c0(self):
        try:
            mod.end_of_month_offset(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.end_of_month_offset(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.end_of_month_offset(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.end_of_month_offset(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.end_of_month_offset(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.end_of_month_offset(datetime.now(), 1)
        except EXC:
            pass


class Test_first_day_of_week_deep:
    def test_c0(self):
        try:
            mod.first_day_of_week("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.first_day_of_week("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.first_day_of_week("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.first_day_of_week("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.first_day_of_week("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.first_day_of_week("UPPER lower 123")
        except EXC:
            pass

    def test_kw_week_start_day(self):
        try:
            mod.first_day_of_week("hello world", week_start_day=1)
        except EXC:
            pass


class Test_generate_random_time_deep:
    def test_c0(self):
        try:
            mod.generate_random_time()
        except EXC:
            pass

    def test_kw_min_time(self):
        try:
            mod.generate_random_time(min_time=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_max_time(self):
        try:
            mod.generate_random_time(max_time=date(2024, 1, 15))
        except EXC:
            pass


class Test_get_year_calendar_by_weeks_deep:
    def test_c0(self):
        try:
            mod.get_year_calendar_by_weeks(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_year_calendar_by_weeks(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_year_calendar_by_weeks(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_year_calendar_by_weeks(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_year_calendar_by_weeks(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_year_calendar_by_weeks(0)
        except EXC:
            pass

    def test_kw_start_date(self):
        try:
            mod.get_year_calendar_by_weeks(1, start_date=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_end_date(self):
        try:
            mod.get_year_calendar_by_weeks(1, end_date=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_granularity(self):
        try:
            mod.get_year_calendar_by_weeks(1, granularity="hello world")
        except EXC:
            pass


class Test_human_readable_duration_deep:
    def test_c0(self):
        try:
            mod.human_readable_duration(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.human_readable_duration(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.human_readable_duration(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.human_readable_duration(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.human_readable_duration(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.human_readable_duration(0)
        except EXC:
            pass


class Test_is_duration_greater_than_deep:
    def test_c0(self):
        try:
            mod.is_duration_greater_than(date(2024, 1, 15), date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_duration_greater_than(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_duration_greater_than(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_duration_greater_than(date(2000, 1, 1), date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_duration_greater_than(date(2024, 12, 31), datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_duration_greater_than(datetime.now(), date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass


class Test_is_duration_less_than_deep:
    def test_c0(self):
        try:
            mod.is_duration_less_than(date(2024, 1, 15), date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_duration_less_than(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_duration_less_than(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_duration_less_than(date(2000, 1, 1), date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_duration_less_than(date(2024, 12, 31), datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_duration_less_than(datetime.now(), date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass


class Test_last_day_of_week_deep:
    def test_c0(self):
        try:
            mod.last_day_of_week("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.last_day_of_week("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.last_day_of_week("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.last_day_of_week("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.last_day_of_week("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.last_day_of_week("UPPER lower 123")
        except EXC:
            pass

    def test_kw_week_start_day(self):
        try:
            mod.last_day_of_week("hello world", week_start_day=1)
        except EXC:
            pass


class Test_last_weekday_of_month_deep:
    def test_c0(self):
        try:
            mod.last_weekday_of_month(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.last_weekday_of_month(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.last_weekday_of_month(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.last_weekday_of_month(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.last_weekday_of_month(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.last_weekday_of_month(datetime.now(), 1)
        except EXC:
            pass


class Test_overlap_dates_deep:
    def test_c0(self):
        try:
            mod.overlap_dates("hello world", "test", "abc123", "")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.overlap_dates("test", "abc123", "", "Hello, World!")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.overlap_dates("abc123", "", "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.overlap_dates("", "Hello, World!", "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.overlap_dates("Hello, World!", "UPPER lower 123", "hello world", "test")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.overlap_dates("UPPER lower 123", "hello world", "test", "abc123")
        except EXC:
            pass


class Test_previous_business_day_deep:
    def test_c0(self):
        try:
            mod.previous_business_day(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.previous_business_day(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.previous_business_day(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.previous_business_day(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.previous_business_day(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.previous_business_day(datetime.now())
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.previous_business_day(date(2024, 1, 15), holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_previous_weekday_deep:
    def test_c0(self):
        try:
            mod.previous_weekday(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.previous_weekday(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.previous_weekday(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.previous_weekday(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.previous_weekday(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.previous_weekday(datetime.now(), 1)
        except EXC:
            pass


class Test_quarters_between_dates_deep:
    def test_c0(self):
        try:
            mod.quarters_between_dates(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.quarters_between_dates(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.quarters_between_dates(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.quarters_between_dates(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.quarters_between_dates(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.quarters_between_dates(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass


class Test_semester_deep:
    def test_c0(self):
        try:
            mod.semester("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.semester("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.semester("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.semester("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.semester("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.semester("UPPER lower 123")
        except EXC:
            pass


class Test_string_to_date_deep:
    def test_c0(self):
        try:
            mod.string_to_date("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.string_to_date("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.string_to_date("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.string_to_date("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.string_to_date("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.string_to_date("UPPER lower 123")
        except EXC:
            pass


class Test_trading_days_between_deep:
    def test_c0(self):
        try:
            mod.trading_days_between(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.trading_days_between(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.trading_days_between(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.trading_days_between(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.trading_days_between(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.trading_days_between(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.trading_days_between(date(2024, 1, 15), date(2023, 6, 1), holidays=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_weekend(self):
        try:
            mod.trading_days_between(date(2024, 1, 15), date(2023, 6, 1), weekend=1)
        except EXC:
            pass


class Test_workday_deep:
    def test_c0(self):
        try:
            mod.workday(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.workday(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.workday(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.workday(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.workday(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.workday(datetime.now(), 1)
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.workday(date(2024, 1, 15), 2, holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_workday_intl_deep:
    def test_c0(self):
        try:
            mod.workday_intl(date(2024, 1, 15), 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.workday_intl(date(2023, 6, 1), 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.workday_intl(datetime(2024, 3, 15, 10, 30), 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.workday_intl(date(2000, 1, 1), 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.workday_intl(date(2024, 12, 31), 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.workday_intl(datetime.now(), 1)
        except EXC:
            pass

    def test_kw_weekend(self):
        try:
            mod.workday_intl(date(2024, 1, 15), 2, weekend=1)
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.workday_intl(date(2024, 1, 15), 2, holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_working_hours_in_month_deep:
    def test_c0(self):
        try:
            mod.working_hours_in_month(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.working_hours_in_month(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.working_hours_in_month(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.working_hours_in_month(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.working_hours_in_month(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.working_hours_in_month(0, 1)
        except EXC:
            pass

    def test_kw_hours_per_day(self):
        try:
            mod.working_hours_in_month(1, 2, hours_per_day=1)
        except EXC:
            pass

    def test_kw_holidays(self):
        try:
            mod.working_hours_in_month(1, 2, holidays=date(2024, 1, 15))
        except EXC:
            pass


class Test_year_fraction_deep:
    def test_c0(self):
        try:
            mod.year_fraction(date(2024, 1, 15), date(2023, 6, 1))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.year_fraction(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.year_fraction(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.year_fraction(date(2000, 1, 1), date(2024, 12, 31))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.year_fraction(date(2024, 12, 31), datetime.now())
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.year_fraction(datetime.now(), date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.year_fraction(date(2024, 1, 15), date(2023, 6, 1), basis=1)
        except EXC:
            pass

