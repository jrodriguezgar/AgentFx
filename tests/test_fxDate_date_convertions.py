"""Tests for fxDate.date_convertions."""

from datetime import date, datetime, time

import pytest

from agentfx.fxDate.date_convertions import (
    date_to_iso_week_date,
    datetime_to_iso8601,
    decimal_hours_to_time,
    excel_serial_to_date,
    iso8601_to_datetime,
    iso_week_date_to_date,
    modified_julian_date,
    rata_die,
    seconds_to_hms,
    time_to_decimal_hours,
    unix_epoch_days,
)
from agentfx.fxString.string_convertions import hex_to_text, ordinal_suffix, text_to_hex
from agentfx.fxString.string_operations import normalize_unicode


class TestUnixEpochDay:

    def test_epoch_zero(self):
        from agentfx.fxDate.date_convertions import unix_epoch_day

        assert unix_epoch_day(date(1970, 1, 1)) == 0

    def test_known_date(self):
        from agentfx.fxDate.date_convertions import unix_epoch_day

        # 2026-04-08 is 20551 days after 1970-01-01
        assert unix_epoch_day(date(2026, 4, 8)) == (date(2026, 4, 8) - date(1970, 1, 1)).days

class TestDateToExcelTimestamp:

    def test_noon(self):
        from agentfx.fxDate.date_convertions import date_to_excel_timestamp

        result = date_to_excel_timestamp(datetime(2026, 4, 8, 12, 0, 0))
        # Integer part = date serial, fractional = 0.5 (noon)
        assert result == int(result) + 0.5
        assert result > 40000  # sanity check

class TestTimeZoneOffset:

    def test_madrid_summer(self):
        from agentfx.fxDate.date_convertions import time_zone_offset

        result = time_zone_offset("Europe/Madrid", datetime(2026, 7, 1))
        assert result == "+02:00"

    def test_utc(self):
        from agentfx.fxDate.date_convertions import time_zone_offset

        result = time_zone_offset("UTC", datetime(2026, 1, 1))
        assert result == "+00:00"

class TestModifiedJulianDate:

    def test_j2000(self):
        assert modified_julian_date(date(2000, 1, 1)) == pytest.approx(51544.0, abs=0.5)

    def test_type_error(self):

        with pytest.raises(TypeError):
            modified_julian_date("2000-01-01")

class TestRataDie:

    def test_j2000(self):
        assert rata_die(date(2000, 1, 1)) == 730120

    def test_epoch(self):
        assert rata_die(date(1, 1, 1)) == 1

class TestUnixEpochDays:

    def test_j2000(self):
        assert unix_epoch_days(date(2000, 1, 1)) == 10957

    def test_epoch_itself(self):
        assert unix_epoch_days(date(1970, 1, 1)) == 0

    def test_before_epoch(self):
        assert unix_epoch_days(date(1969, 12, 31)) == -1


# ── fxDate ── date_operations ───────────────────────────────────────────

class TestOrdinalSuffix:

    def test_first(self):
        assert ordinal_suffix(1) == "1st"

    def test_second(self):
        assert ordinal_suffix(2) == "2nd"

    def test_third(self):
        assert ordinal_suffix(3) == "3rd"

    def test_fourth(self):
        assert ordinal_suffix(4) == "4th"

    def test_eleventh(self):
        assert ordinal_suffix(11) == "11th"

    def test_twelfth(self):
        assert ordinal_suffix(12) == "12th"

    def test_thirteenth(self):
        assert ordinal_suffix(13) == "13th"

    def test_twenty_first(self):
        assert ordinal_suffix(21) == "21st"

    def test_twenty_second(self):
        assert ordinal_suffix(22) == "22nd"

    def test_hundred_thirteenth(self):
        assert ordinal_suffix(113) == "113th"

    def test_type_error(self):
        with pytest.raises(TypeError):
            ordinal_suffix(1.5)


# ---------------------------------------------------------------------------
# fxDate — date_convertions.py
# ---------------------------------------------------------------------------


class TestTimeToDecimalHours:

    def test_one_thirty(self):
        assert time_to_decimal_hours(time(1, 30)) == 1.5

    def test_midnight(self):
        assert time_to_decimal_hours(time(0, 0)) == 0.0

    def test_noon(self):
        assert time_to_decimal_hours(time(12, 0)) == 12.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            time_to_decimal_hours("12:00")

class TestDecimalHoursToTime:

    def test_one_five(self):
        assert decimal_hours_to_time(1.5) == time(1, 30)

    def test_zero(self):
        assert decimal_hours_to_time(0) == time(0, 0)

    def test_negative(self):
        with pytest.raises(ValueError):
            decimal_hours_to_time(-1)

    def test_over_24(self):
        with pytest.raises(ValueError):
            decimal_hours_to_time(24)

class TestSecondsToHms:

    def test_basic(self):
        assert seconds_to_hms(3661) == "1:01:01"

    def test_zero(self):
        assert seconds_to_hms(0) == "0:00:00"

    def test_negative(self):
        with pytest.raises(ValueError):
            seconds_to_hms(-1)

class TestHexToText:

    def test_hello(self):
        assert hex_to_text("48656c6c6f") == "Hello"

    def test_roundtrip(self):
        original = "AgentFx 2024!"
        assert hex_to_text(text_to_hex(original)) == original

    def test_invalid_hex(self):
        with pytest.raises(ValueError):
            hex_to_text("ZZZZ")

    def test_type_error(self):
        with pytest.raises(TypeError):
            hex_to_text(123)


# ── fxDate · date_convertions ─────────────────────────────────────────────


class TestDatetimeToIso8601:

    def test_date(self):
        assert datetime_to_iso8601(date(2024, 3, 15)) == "2024-03-15"

    def test_datetime(self):
        result = datetime_to_iso8601(datetime(2024, 3, 15, 10, 30, 0))
        assert "2024-03-15" in result
        assert "10:30:00" in result

    def test_type_error(self):
        with pytest.raises(TypeError):
            datetime_to_iso8601("2024-03-15")

class TestIso8601ToDatetime:

    def test_date_only(self):
        result = iso8601_to_datetime("2024-03-15")
        assert result == date(2024, 3, 15)

    def test_datetime_with_t(self):
        result = iso8601_to_datetime("2024-03-15T10:30:00")
        assert isinstance(result, datetime)
        assert result.hour == 10

    def test_type_error(self):
        with pytest.raises(TypeError):
            iso8601_to_datetime(20240315)

class TestExcelSerialToDate:

    def test_known_date(self):
        # 2023-01-01 = serial 44927
        assert excel_serial_to_date(44927) == date(2023, 1, 1)

    def test_serial_1(self):
        assert excel_serial_to_date(1) == date(1900, 1, 1)

    def test_serial_60_raises(self):
        with pytest.raises(ValueError):
            excel_serial_to_date(60)

    def test_serial_61(self):
        # Serial 61 = 1900-03-01
        assert excel_serial_to_date(61) == date(1900, 3, 1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            excel_serial_to_date("100")

class TestNormalizeUnicode:

    def test_nfc(self):
        import unicodedata
        # Composed vs decomposed
        composed = unicodedata.normalize("NFC", "café")
        decomposed = unicodedata.normalize("NFD", "café")
        result = normalize_unicode(decomposed, "NFC")
        assert result == composed

    def test_invalid_form(self):
        with pytest.raises(ValueError):
            normalize_unicode("hello", "INVALID")

    def test_type_error(self):
        with pytest.raises(TypeError):
            normalize_unicode(123)


# ── fxDate · date_convertions ────────────────────────────────────────


class TestDateToIsoWeekDate:

    def test_basic(self):
        assert date_to_iso_week_date(date(2023, 1, 2)) == "2023-W01-1"

    def test_sunday(self):
        assert date_to_iso_week_date(date(2023, 1, 1)) == "2022-W52-7"

    def test_datetime_input(self):
        assert date_to_iso_week_date(datetime(2023, 1, 2, 12, 0)) == "2023-W01-1"

    def test_type_error(self):
        with pytest.raises(TypeError):
            date_to_iso_week_date("2023-01-02")

class TestIsoWeekDateToDate:

    def test_basic(self):
        assert iso_week_date_to_date("2023-W01-1") == date(2023, 1, 2)

    def test_roundtrip(self):
        d = date(2025, 12, 29)
        iso_str = date_to_iso_week_date(d)
        assert iso_week_date_to_date(iso_str) == d

    def test_invalid_format(self):
        with pytest.raises(ValueError):
            iso_week_date_to_date("2023-01-02")

    def test_invalid_week(self):
        with pytest.raises(ValueError):
            iso_week_date_to_date("2023-W54-1")

    def test_invalid_day(self):
        with pytest.raises(ValueError):
            iso_week_date_to_date("2023-W01-8")

    def test_type_error(self):
        with pytest.raises(TypeError):
            iso_week_date_to_date(20230102)


# ── fxDate · date_evaluations ────────────────────────────────────────

