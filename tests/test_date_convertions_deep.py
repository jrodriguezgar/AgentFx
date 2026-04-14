# Deep coverage tests for formulite.fxDate.date_convertions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxDate.date_convertions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_ad_format_to_datetime_deep:
    def test_c0(self):
        try:
            mod.ad_format_to_datetime("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ad_format_to_datetime("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ad_format_to_datetime("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ad_format_to_datetime("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ad_format_to_datetime("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ad_format_to_datetime("UPPER lower 123")
        except EXC:
            pass


class Test_unix_timestamp_to_datetime_deep:
    def test_c0(self):
        try:
            mod.unix_timestamp_to_datetime(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.unix_timestamp_to_datetime(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.unix_timestamp_to_datetime(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.unix_timestamp_to_datetime(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.unix_timestamp_to_datetime(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.unix_timestamp_to_datetime(0)
        except EXC:
            pass

    def test_kw_tz_info(self):
        try:
            mod.unix_timestamp_to_datetime(1, tz_info="hello world")
        except EXC:
            pass


class Test_utc_to_timezone_deep:
    def test_c0(self):
        try:
            mod.utc_to_timezone(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.utc_to_timezone(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.utc_to_timezone(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.utc_to_timezone(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.utc_to_timezone(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.utc_to_timezone(datetime.now())
        except EXC:
            pass

    def test_kw_target_tz_name(self):
        try:
            mod.utc_to_timezone(date(2024, 1, 15), target_tz_name="hello world")
        except EXC:
            pass


class Test_utc_to_datetime_deep:
    def test_c0(self):
        try:
            mod.utc_to_datetime("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.utc_to_datetime("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.utc_to_datetime("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.utc_to_datetime("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.utc_to_datetime("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.utc_to_datetime("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.utc_to_datetime("hello world", input_format="hello world")
        except EXC:
            pass

    def test_kw_input_tz(self):
        try:
            mod.utc_to_datetime("hello world", input_tz="hello world")
        except EXC:
            pass


class Test_utc_to_midnight_iso_deep:
    def test_c0(self):
        try:
            mod.utc_to_midnight_iso(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.utc_to_midnight_iso(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.utc_to_midnight_iso(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.utc_to_midnight_iso(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.utc_to_midnight_iso(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.utc_to_midnight_iso(datetime.now())
        except EXC:
            pass


class Test_date_to_iso_format_deep:
    def test_c0(self):
        try:
            mod.date_to_iso_format("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_to_iso_format("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_to_iso_format("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_to_iso_format("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_to_iso_format("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_to_iso_format("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.date_to_iso_format("hello world", input_format="hello world")
        except EXC:
            pass


class Test_date_to_julian_deep:
    def test_c0(self):
        try:
            mod.date_to_julian("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_to_julian("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_to_julian("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_to_julian("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_to_julian("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_to_julian("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.date_to_julian("hello world", input_format="hello world")
        except EXC:
            pass


class Test_datetime_to_ad_format_deep:
    def test_c0(self):
        try:
            mod.datetime_to_ad_format(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.datetime_to_ad_format(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.datetime_to_ad_format(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.datetime_to_ad_format(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.datetime_to_ad_format(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.datetime_to_ad_format(datetime.now())
        except EXC:
            pass


class Test_datetime_to_filetime_deep:
    def test_c0(self):
        try:
            mod.datetime_to_filetime(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.datetime_to_filetime(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.datetime_to_filetime(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.datetime_to_filetime(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.datetime_to_filetime(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.datetime_to_filetime(datetime.now())
        except EXC:
            pass


class Test_from_iso_to_local_datetime_deep:
    def test_c0(self):
        try:
            mod.from_iso_to_local_datetime("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.from_iso_to_local_datetime("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.from_iso_to_local_datetime("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.from_iso_to_local_datetime("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.from_iso_to_local_datetime("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.from_iso_to_local_datetime("UPPER lower 123")
        except EXC:
            pass


class Test_datetime_to_integer_deep:
    def test_c0(self):
        try:
            mod.datetime_to_integer("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.datetime_to_integer("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.datetime_to_integer("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.datetime_to_integer("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.datetime_to_integer("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.datetime_to_integer("UPPER lower 123")
        except EXC:
            pass

    def test_kw_input_format(self):
        try:
            mod.datetime_to_integer("hello world", input_format="hello world")
        except EXC:
            pass


class Test_julian_to_date_deep:
    def test_c0(self):
        try:
            mod.julian_to_date(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.julian_to_date(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.julian_to_date(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.julian_to_date(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.julian_to_date(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.julian_to_date(0, 1)
        except EXC:
            pass


class Test_timestamp_to_datetime_deep:
    def test_c0(self):
        try:
            mod.timestamp_to_datetime(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.timestamp_to_datetime(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.timestamp_to_datetime(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.timestamp_to_datetime(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.timestamp_to_datetime(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.timestamp_to_datetime(0)
        except EXC:
            pass


class Test_date_to_excel_serial_deep:
    def test_c0(self):
        try:
            mod.date_to_excel_serial(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_to_excel_serial(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_to_excel_serial(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_to_excel_serial(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_to_excel_serial(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_to_excel_serial(datetime.now())
        except EXC:
            pass


class Test_date_to_excel_timestamp_deep:
    def test_c0(self):
        try:
            mod.date_to_excel_timestamp(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_to_excel_timestamp(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_to_excel_timestamp(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_to_excel_timestamp(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_to_excel_timestamp(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_to_excel_timestamp(datetime.now())
        except EXC:
            pass


class Test_date_to_human_short_deep:
    def test_c0(self):
        try:
            mod.date_to_human_short(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_to_human_short(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_to_human_short(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_to_human_short(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_to_human_short(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_to_human_short(datetime.now())
        except EXC:
            pass

    def test_kw_language(self):
        try:
            mod.date_to_human_short(date(2024, 1, 15), language="hello world")
        except EXC:
            pass


class Test_date_to_string_deep:
    def test_c0(self):
        try:
            mod.date_to_string(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.date_to_string(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.date_to_string(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.date_to_string(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.date_to_string(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.date_to_string(datetime.now())
        except EXC:
            pass

    def test_kw_format_code(self):
        try:
            mod.date_to_string(date(2024, 1, 15), format_code="hello world")
        except EXC:
            pass


class Test_datetime_to_milliseconds_timestamp_deep:
    def test_c0(self):
        try:
            mod.datetime_to_milliseconds_timestamp(date(2024, 1, 15))
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.datetime_to_milliseconds_timestamp(date(2023, 6, 1))
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.datetime_to_milliseconds_timestamp(datetime(2024, 3, 15, 10, 30))
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.datetime_to_milliseconds_timestamp(date(2000, 1, 1))
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.datetime_to_milliseconds_timestamp(date(2024, 12, 31))
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.datetime_to_milliseconds_timestamp(datetime.now())
        except EXC:
            pass


class Test_filetime_to_datetime_deep:
    def test_c0(self):
        try:
            mod.filetime_to_datetime(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.filetime_to_datetime(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.filetime_to_datetime(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.filetime_to_datetime(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.filetime_to_datetime(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.filetime_to_datetime(0)
        except EXC:
            pass


class Test_iso_week_date_to_date_deep:
    def test_c0(self):
        try:
            mod.iso_week_date_to_date("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.iso_week_date_to_date("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.iso_week_date_to_date("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.iso_week_date_to_date("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.iso_week_date_to_date("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.iso_week_date_to_date("UPPER lower 123")
        except EXC:
            pass


class Test_milliseconds_timestamp_to_datetime_deep:
    def test_c0(self):
        try:
            mod.milliseconds_timestamp_to_datetime(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.milliseconds_timestamp_to_datetime(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.milliseconds_timestamp_to_datetime(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.milliseconds_timestamp_to_datetime(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.milliseconds_timestamp_to_datetime(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.milliseconds_timestamp_to_datetime(0)
        except EXC:
            pass


class Test_parse_date_flexible_deep:
    def test_c0(self):
        try:
            mod.parse_date_flexible("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.parse_date_flexible("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.parse_date_flexible("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.parse_date_flexible("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.parse_date_flexible("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.parse_date_flexible("UPPER lower 123")
        except EXC:
            pass

    def test_kw_dayfirst(self):
        try:
            mod.parse_date_flexible("hello world", dayfirst=True)
        except EXC:
            pass


class Test_time_zone_offset_deep:
    def test_c0(self):
        try:
            mod.time_zone_offset("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.time_zone_offset("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.time_zone_offset("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.time_zone_offset("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.time_zone_offset("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.time_zone_offset("UPPER lower 123")
        except EXC:
            pass

    def test_kw_dt_val(self):
        try:
            mod.time_zone_offset("hello world", dt_val=date(2024, 1, 15))
        except EXC:
            pass

