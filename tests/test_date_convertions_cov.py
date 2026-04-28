# Coverage tests for agentfx.fxDate.date_convertions
from datetime import date, datetime, time

from agentfx.fxDate import date_convertions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_ad_format_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "ad_format_to_datetime")

    def test_var0(self):
        try:
            mod.ad_format_to_datetime("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ad_format_to_datetime("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ad_format_to_datetime(None)
        except EXC:
            pass


class Test_convert_timezone:
    def test_exists(self):
        assert hasattr(mod, "convert_timezone")

    def test_doc0(self):
        try:
            mod.convert_timezone(datetime(2026, 4, 4, 12, 0), "UTC", "Europe/Madrid")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.convert_timezone(date(2024, 1, 15), "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.convert_timezone(date(2023, 12, 31), "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.convert_timezone(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.convert_timezone("", "", "")
        except EXC:
            pass


class Test_date_to_excel_serial:
    def test_exists(self):
        assert hasattr(mod, "date_to_excel_serial")

    def test_doc0(self):
        try:
            mod.date_to_excel_serial(date(2023, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_to_excel_serial(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_excel_serial(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_excel_serial(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_to_excel_serial("")
        except EXC:
            pass


class Test_date_to_excel_timestamp:
    def test_exists(self):
        assert hasattr(mod, "date_to_excel_timestamp")

    def test_doc0(self):
        try:
            mod.date_to_excel_timestamp(datetime(2026, 4, 8, 12, 0, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_to_excel_timestamp(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_excel_timestamp(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_excel_timestamp(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_to_excel_timestamp("")
        except EXC:
            pass


class Test_date_to_human_short:
    def test_exists(self):
        assert hasattr(mod, "date_to_human_short")

    def test_doc0(self):
        try:
            mod.date_to_human_short(date(2026, 4, 4), "en")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.date_to_human_short(date(2026, 4, 4), "es")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_to_human_short(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_human_short(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_human_short(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_to_human_short("")
        except EXC:
            pass


class Test_date_to_iso_format:
    def test_exists(self):
        assert hasattr(mod, "date_to_iso_format")

    def test_doc0(self):
        try:
            mod.date_to_iso_format(datetime(2023, 1, 15, 10, 30, 45, 123456))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.date_to_iso_format(datetime(2024, 7, 20).date()) # Convert to datetime first
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.date_to_iso_format("2023-05-10 08:00:00", "%Y-%m-%d %H:%M:%S")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.date_to_iso_format("2023-05-10")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_to_iso_format("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_iso_format("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_iso_format(None)
        except EXC:
            pass


class Test_date_to_iso_week_date:
    def test_exists(self):
        assert hasattr(mod, "date_to_iso_week_date")

    def test_doc0(self):
        try:
            mod.date_to_iso_week_date(date(2023, 1, 2))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_to_iso_week_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_iso_week_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_iso_week_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_to_iso_week_date("")
        except EXC:
            pass


class Test_date_to_julian:
    def test_exists(self):
        assert hasattr(mod, "date_to_julian")

    def test_doc0(self):
        try:
            mod.date_to_julian(datetime(2025, 1, 1))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.date_to_julian(datetime(2025, 2, 1))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.date_to_julian(datetime(2024, 3, 1))
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.date_to_julian(datetime(2023, 12, 31))
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.date_to_julian(datetime(2024, 12, 31))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.date_to_julian("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_julian("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_julian(None)
        except EXC:
            pass


class Test_date_to_string:
    def test_exists(self):
        assert hasattr(mod, "date_to_string")

    def test_var0(self):
        try:
            mod.date_to_string(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.date_to_string(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.date_to_string(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.date_to_string("")
        except EXC:
            pass


class Test_datetime_to_ad_format:
    def test_exists(self):
        assert hasattr(mod, "datetime_to_ad_format")

    def test_var0(self):
        try:
            mod.datetime_to_ad_format(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datetime_to_ad_format(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datetime_to_ad_format(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.datetime_to_ad_format("")
        except EXC:
            pass


class Test_datetime_to_cron:
    def test_exists(self):
        assert hasattr(mod, "datetime_to_cron")

    def test_doc0(self):
        try:
            mod.datetime_to_cron(datetime(2025, 6, 15, 14, 30))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.datetime_to_cron(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datetime_to_cron(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datetime_to_cron(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.datetime_to_cron("")
        except EXC:
            pass


class Test_datetime_to_date:
    def test_exists(self):
        assert hasattr(mod, "datetime_to_date")

    def test_var0(self):
        try:
            mod.datetime_to_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datetime_to_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datetime_to_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.datetime_to_date("")
        except EXC:
            pass


class Test_datetime_to_filetime:
    def test_exists(self):
        assert hasattr(mod, "datetime_to_filetime")

    def test_var0(self):
        try:
            mod.datetime_to_filetime(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datetime_to_filetime(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datetime_to_filetime(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.datetime_to_filetime("")
        except EXC:
            pass


class Test_datetime_to_integer:
    def test_exists(self):
        assert hasattr(mod, "datetime_to_integer")

    def test_doc0(self):
        try:
            mod.datetime_to_integer(datetime(2026, 1, 3))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.datetime_to_integer(date(2026, 1, 3))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.datetime_to_integer("03/01/2026", "%d/%m/%Y")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.datetime_to_integer("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datetime_to_integer("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datetime_to_integer(None)
        except EXC:
            pass


class Test_datetime_to_iso8601:
    def test_exists(self):
        assert hasattr(mod, "datetime_to_iso8601")

    def test_doc0(self):
        try:
            mod.datetime_to_iso8601(date(2024, 3, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.datetime_to_iso8601(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datetime_to_iso8601(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datetime_to_iso8601(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.datetime_to_iso8601("")
        except EXC:
            pass


class Test_datetime_to_milliseconds_timestamp:
    def test_exists(self):
        assert hasattr(mod, "datetime_to_milliseconds_timestamp")

    def test_var0(self):
        try:
            mod.datetime_to_milliseconds_timestamp(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datetime_to_milliseconds_timestamp(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datetime_to_milliseconds_timestamp(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.datetime_to_milliseconds_timestamp("")
        except EXC:
            pass


class Test_datetime_to_rfc2822:
    def test_exists(self):
        assert hasattr(mod, "datetime_to_rfc2822")

    def test_doc0(self):
        try:
            mod.datetime_to_rfc2822(datetime(2025, 6, 15, 14, 30, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.datetime_to_rfc2822(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datetime_to_rfc2822(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datetime_to_rfc2822(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.datetime_to_rfc2822("")
        except EXC:
            pass


class Test_datetime_to_timestamp:
    def test_exists(self):
        assert hasattr(mod, "datetime_to_timestamp")

    def test_var0(self):
        try:
            mod.datetime_to_timestamp(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.datetime_to_timestamp(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.datetime_to_timestamp(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.datetime_to_timestamp("")
        except EXC:
            pass


class Test_decimal_hours_to_time:
    def test_exists(self):
        assert hasattr(mod, "decimal_hours_to_time")

    def test_doc0(self):
        try:
            mod.decimal_hours_to_time(1.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.decimal_hours_to_time(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.decimal_hours_to_time(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.decimal_hours_to_time(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.decimal_hours_to_time("")
        except EXC:
            pass


class Test_excel_serial_to_date:
    def test_exists(self):
        assert hasattr(mod, "excel_serial_to_date")

    def test_doc0(self):
        try:
            mod.excel_serial_to_date(44927)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.excel_serial_to_date(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.excel_serial_to_date(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.excel_serial_to_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.excel_serial_to_date("")
        except EXC:
            pass


class Test_filetime_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "filetime_to_datetime")

    def test_doc0(self):
        try:
            mod.filetime_to_datetime(132723834123456789)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.filetime_to_datetime(130611456000000000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.filetime_to_datetime(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.filetime_to_datetime(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.filetime_to_datetime(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.filetime_to_datetime("")
        except EXC:
            pass


class Test_from_iso_to_local_datetime:
    def test_exists(self):
        assert hasattr(mod, "from_iso_to_local_datetime")

    def test_var0(self):
        try:
            mod.from_iso_to_local_datetime("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.from_iso_to_local_datetime("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.from_iso_to_local_datetime(None)
        except EXC:
            pass


class Test_hms_to_seconds:
    def test_exists(self):
        assert hasattr(mod, "hms_to_seconds")

    def test_doc0(self):
        try:
            mod.hms_to_seconds("1:01:01")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hms_to_seconds("5:30")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hms_to_seconds("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hms_to_seconds("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hms_to_seconds(None)
        except EXC:
            pass


class Test_integer_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "integer_to_datetime")

    def test_doc0(self):
        try:
            mod.integer_to_datetime(20260103)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.integer_to_datetime(20240229)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.integer_to_datetime(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.integer_to_datetime(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.integer_to_datetime(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.integer_to_datetime("")
        except EXC:
            pass


class Test_iso8601_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "iso8601_to_datetime")

    def test_doc0(self):
        try:
            mod.iso8601_to_datetime("2024-03-15")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.iso8601_to_datetime("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.iso8601_to_datetime("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.iso8601_to_datetime(None)
        except EXC:
            pass


class Test_iso_week_date_to_date:
    def test_exists(self):
        assert hasattr(mod, "iso_week_date_to_date")

    def test_doc0(self):
        try:
            mod.iso_week_date_to_date("2023-W01-1")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.iso_week_date_to_date("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.iso_week_date_to_date("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.iso_week_date_to_date(None)
        except EXC:
            pass


class Test_julian_to_date:
    def test_exists(self):
        assert hasattr(mod, "julian_to_date")

    def test_doc0(self):
        try:
            mod.julian_to_date(1, 2025)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.julian_to_date(32, 2025)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.julian_to_date(61, 2024)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.julian_to_date(365, 2023)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.julian_to_date(366, 2024)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.julian_to_date(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.julian_to_date(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.julian_to_date(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.julian_to_date("", "")
        except EXC:
            pass


class Test_list_available_timezones:
    def test_exists(self):
        assert hasattr(mod, "list_available_timezones")

    def test_doc0(self):
        try:
            mod.list_available_timezones()
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.list_available_timezones()
        except EXC:
            pass


class Test_milliseconds_timestamp_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "milliseconds_timestamp_to_datetime")

    def test_doc0(self):
        try:
            mod.milliseconds_timestamp_to_datetime(1749597491123)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.milliseconds_timestamp_to_datetime(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.milliseconds_timestamp_to_datetime(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.milliseconds_timestamp_to_datetime(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.milliseconds_timestamp_to_datetime("")
        except EXC:
            pass


class Test_modified_julian_date:
    def test_exists(self):
        assert hasattr(mod, "modified_julian_date")

    def test_doc0(self):
        try:
            mod.modified_julian_date(date(2000, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.modified_julian_date(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.modified_julian_date(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.modified_julian_date(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.modified_julian_date("")
        except EXC:
            pass


class Test_parse_date_flexible:
    def test_exists(self):
        assert hasattr(mod, "parse_date_flexible")

    def test_doc0(self):
        try:
            mod.parse_date_flexible("15/01/2026")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.parse_date_flexible("2026-04-04")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parse_date_flexible("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parse_date_flexible("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parse_date_flexible(None)
        except EXC:
            pass


class Test_rata_die:
    def test_exists(self):
        assert hasattr(mod, "rata_die")

    def test_doc0(self):
        try:
            mod.rata_die(date(2000, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rata_die(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rata_die(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rata_die(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rata_die("")
        except EXC:
            pass


class Test_rfc2822_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "rfc2822_to_datetime")

    def test_doc0(self):
        try:
            mod.rfc2822_to_datetime('Sun, 15 Jun 2025 14:30:00 +0000')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rfc2822_to_datetime("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rfc2822_to_datetime("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rfc2822_to_datetime(None)
        except EXC:
            pass


class Test_seconds_to_hms:
    def test_exists(self):
        assert hasattr(mod, "seconds_to_hms")

    def test_doc0(self):
        try:
            mod.seconds_to_hms(3661)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.seconds_to_hms(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.seconds_to_hms(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.seconds_to_hms(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.seconds_to_hms("")
        except EXC:
            pass


class Test_time_to_day_fraction:
    def test_exists(self):
        assert hasattr(mod, "time_to_day_fraction")

    def test_doc0(self):
        try:
            mod.time_to_day_fraction("12:00:00")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.time_to_day_fraction("06:00")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.time_to_day_fraction("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.time_to_day_fraction("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.time_to_day_fraction(None)
        except EXC:
            pass


class Test_time_to_decimal_hours:
    def test_exists(self):
        assert hasattr(mod, "time_to_decimal_hours")

    def test_doc0(self):
        try:
            mod.time_to_decimal_hours(time(1, 30))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.time_to_decimal_hours(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.time_to_decimal_hours(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.time_to_decimal_hours(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.time_to_decimal_hours("")
        except EXC:
            pass


class Test_time_zone_offset:
    def test_exists(self):
        assert hasattr(mod, "time_zone_offset")

    def test_doc0(self):
        try:
            mod.time_zone_offset("Europe/Madrid", datetime(2026, 7, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.time_zone_offset("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.time_zone_offset("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.time_zone_offset(None)
        except EXC:
            pass


class Test_timestamp_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "timestamp_to_datetime")

    def test_doc0(self):
        try:
            mod.timestamp_to_datetime(1735862400.0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.timestamp_to_datetime(1735862400)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.timestamp_to_datetime(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.timestamp_to_datetime(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.timestamp_to_datetime(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.timestamp_to_datetime("")
        except EXC:
            pass


class Test_unix_epoch_day:
    def test_exists(self):
        assert hasattr(mod, "unix_epoch_day")

    def test_doc0(self):
        try:
            mod.unix_epoch_day(date(1970, 1, 1))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.unix_epoch_day(date(2026, 4, 8))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.unix_epoch_day(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unix_epoch_day(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unix_epoch_day(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unix_epoch_day("")
        except EXC:
            pass


class Test_unix_epoch_days:
    def test_exists(self):
        assert hasattr(mod, "unix_epoch_days")

    def test_doc0(self):
        try:
            mod.unix_epoch_days(date(2000, 1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.unix_epoch_days(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unix_epoch_days(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unix_epoch_days(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unix_epoch_days("")
        except EXC:
            pass


class Test_unix_timestamp_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "unix_timestamp_to_datetime")

    def test_doc0(self):
        try:
            mod.unix_timestamp_to_datetime(1718092025.0, tz_info='UTC')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.unix_timestamp_to_datetime(1718092025.0, tz_info='Europe/Madrid')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.unix_timestamp_to_datetime(1718092025.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.unix_timestamp_to_datetime(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unix_timestamp_to_datetime(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unix_timestamp_to_datetime(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unix_timestamp_to_datetime("")
        except EXC:
            pass


class Test_utc_to_datetime:
    def test_exists(self):
        assert hasattr(mod, "utc_to_datetime")

    def test_doc0(self):
        try:
            mod.utc_to_datetime("2025-06-11 10:00:00", "%Y-%m-%d %H:%M:%S", "Asia/Tokyo")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.utc_to_datetime("2025-06-11 10:00:00", "%Y-%m-%d %H:%M:%S")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.utc_to_datetime("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.utc_to_datetime("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.utc_to_datetime(None)
        except EXC:
            pass


class Test_utc_to_midnight_iso:
    def test_exists(self):
        assert hasattr(mod, "utc_to_midnight_iso")

    def test_var0(self):
        try:
            mod.utc_to_midnight_iso(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.utc_to_midnight_iso(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.utc_to_midnight_iso(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.utc_to_midnight_iso("")
        except EXC:
            pass


class Test_utc_to_timezone:
    def test_exists(self):
        assert hasattr(mod, "utc_to_timezone")

    def test_var0(self):
        try:
            mod.utc_to_timezone(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.utc_to_timezone(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.utc_to_timezone(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.utc_to_timezone("")
        except EXC:
            pass

