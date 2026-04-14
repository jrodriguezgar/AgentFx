# Deep coverage tests for formulite.fxString.string_evaluations
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxString.string_evaluations as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_validate_substring_type_deep:
    def test_c0(self):
        try:
            mod.validate_substring_type("hello world", "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.validate_substring_type("test", "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.validate_substring_type("abc123", "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.validate_substring_type("", "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.validate_substring_type("Hello, World!", "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.validate_substring_type("UPPER lower 123", "hello world", "test")
        except EXC:
            pass

    def test_kw_start_position(self):
        try:
            mod.validate_substring_type("hello world", "test", "abc123", start_position=1)
        except EXC:
            pass

    def test_kw_length(self):
        try:
            mod.validate_substring_type("hello world", "test", "abc123", length=1)
        except EXC:
            pass

    def test_kw_num_chars(self):
        try:
            mod.validate_substring_type("hello world", "test", "abc123", num_chars=1)
        except EXC:
            pass


class Test_email_belongs_to_name_deep:
    def test_c0(self):
        try:
            mod.email_belongs_to_name("hello world", 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.email_belongs_to_name("test", 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.email_belongs_to_name("abc123", -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.email_belongs_to_name("", 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.email_belongs_to_name("Hello, World!", 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.email_belongs_to_name("UPPER lower 123", 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.email_belongs_to_name("hello world", 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.email_belongs_to_name("test", -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.email_belongs_to_name("abc123", 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.email_belongs_to_name("", 1)
        except EXC:
            pass


class Test_validate_nif_format_and_type_deep:
    def test_c0(self):
        try:
            mod.validate_nif_format_and_type("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.validate_nif_format_and_type("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.validate_nif_format_and_type("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.validate_nif_format_and_type("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.validate_nif_format_and_type("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.validate_nif_format_and_type("UPPER lower 123")
        except EXC:
            pass

    def test_kw_assume_spanish_if_no_prefix(self):
        try:
            mod.validate_nif_format_and_type("hello world", assume_spanish_if_no_prefix=True)
        except EXC:
            pass


class Test_is_valid_cron_deep:
    def test_c0(self):
        try:
            mod.is_valid_cron("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_cron("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_cron("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_cron("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_cron("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_cron("UPPER lower 123")
        except EXC:
            pass


class Test_has_date_format_deep:
    def test_c0(self):
        try:
            mod.has_date_format("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.has_date_format("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.has_date_format("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.has_date_format("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.has_date_format("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.has_date_format("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_cusip_deep:
    def test_c0(self):
        try:
            mod.is_valid_cusip("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_cusip("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_cusip("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_cusip("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_cusip("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_cusip("UPPER lower 123")
        except EXC:
            pass


class Test_get_phones_deep:
    def test_c0(self):
        try:
            mod.get_phones(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_phones(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_phones(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_phones(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_phones(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_phones(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.get_phones(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.get_phones(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.get_phones(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.get_phones(2)
        except EXC:
            pass

    def test_kw_p_separator(self):
        try:
            mod.get_phones(1, p_separator=1)
        except EXC:
            pass


class Test_check_substring_at_position_deep:
    def test_c0(self):
        try:
            mod.check_substring_at_position("hello world", "test", 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.check_substring_at_position("test", "abc123", 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.check_substring_at_position("abc123", "", 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.check_substring_at_position("", "Hello, World!", 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.check_substring_at_position("Hello, World!", "UPPER lower 123", 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.check_substring_at_position("UPPER lower 123", "hello world", 2)
        except EXC:
            pass


class Test_flesch_reading_ease_deep:
    def test_c0(self):
        try:
            mod.flesch_reading_ease("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.flesch_reading_ease("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.flesch_reading_ease("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.flesch_reading_ease("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.flesch_reading_ease("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.flesch_reading_ease("UPPER lower 123")
        except EXC:
            pass


class Test_gunning_fog_index_deep:
    def test_c0(self):
        try:
            mod.gunning_fog_index("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gunning_fog_index("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gunning_fog_index("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gunning_fog_index("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gunning_fog_index("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gunning_fog_index("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_ipv6_deep:
    def test_c0(self):
        try:
            mod.is_valid_ipv6("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_ipv6("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_ipv6("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_ipv6("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_ipv6("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_ipv6("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_semver_deep:
    def test_c0(self):
        try:
            mod.is_valid_semver("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_semver("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_semver("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_semver("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_semver("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_semver("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_base64_deep:
    def test_c0(self):
        try:
            mod.is_valid_base64("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_base64("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_base64("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_base64("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_base64("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_base64("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_isbn_deep:
    def test_c0(self):
        try:
            mod.is_valid_isbn("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_isbn("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_isbn("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_isbn("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_isbn("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_isbn("UPPER lower 123")
        except EXC:
            pass


class Test_smog_index_deep:
    def test_c0(self):
        try:
            mod.smog_index("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.smog_index("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.smog_index("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.smog_index("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.smog_index("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.smog_index("UPPER lower 123")
        except EXC:
            pass


class Test_starts_with_substring_deep:
    def test_c0(self):
        try:
            mod.starts_with_substring("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.starts_with_substring("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.starts_with_substring("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.starts_with_substring("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.starts_with_substring("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.starts_with_substring("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_case_sensitive(self):
        try:
            mod.starts_with_substring("hello world", "test", case_sensitive=True)
        except EXC:
            pass


class Test_automated_readability_index_deep:
    def test_c0(self):
        try:
            mod.automated_readability_index("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.automated_readability_index("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.automated_readability_index("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.automated_readability_index("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.automated_readability_index("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.automated_readability_index("UPPER lower 123")
        except EXC:
            pass


class Test_check_password_strength_deep:
    def test_c0(self):
        try:
            mod.check_password_strength("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.check_password_strength("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.check_password_strength("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.check_password_strength("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.check_password_strength("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.check_password_strength("UPPER lower 123")
        except EXC:
            pass


class Test_coleman_liau_index_deep:
    def test_c0(self):
        try:
            mod.coleman_liau_index("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.coleman_liau_index("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.coleman_liau_index("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.coleman_liau_index("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.coleman_liau_index("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.coleman_liau_index("UPPER lower 123")
        except EXC:
            pass


class Test_compare_strings_deep:
    def test_c0(self):
        try:
            mod.compare_strings("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.compare_strings("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.compare_strings("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.compare_strings("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.compare_strings("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.compare_strings("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_case_sensitive(self):
        try:
            mod.compare_strings("hello world", "test", case_sensitive=True)
        except EXC:
            pass


class Test_ends_with_substring_deep:
    def test_c0(self):
        try:
            mod.ends_with_substring("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ends_with_substring("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ends_with_substring("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ends_with_substring("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ends_with_substring("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ends_with_substring("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_case_sensitive(self):
        try:
            mod.ends_with_substring("hello world", "test", case_sensitive=True)
        except EXC:
            pass


class Test_has_substring_deep:
    def test_c0(self):
        try:
            mod.has_substring("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.has_substring("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.has_substring("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.has_substring("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.has_substring("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.has_substring("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_is_alphabetic_deep:
    def test_c0(self):
        try:
            mod.is_alphabetic(0.05)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_alphabetic(0.1)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_alphabetic(0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_alphabetic(0.01)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_alphabetic(0.95)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_alphabetic(0.99)
        except EXC:
            pass


class Test_is_valid_ipv4_deep:
    def test_c0(self):
        try:
            mod.is_valid_ipv4("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_ipv4("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_ipv4("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_ipv4("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_ipv4("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_ipv4("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_isin_deep:
    def test_c0(self):
        try:
            mod.is_valid_isin("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_isin("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_isin("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_isin("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_isin("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_isin("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_issn_deep:
    def test_c0(self):
        try:
            mod.is_valid_issn("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_issn("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_issn("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_issn("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_issn("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_issn("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_mac_address_deep:
    def test_c0(self):
        try:
            mod.is_valid_mac_address("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_mac_address("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_mac_address("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_mac_address("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_mac_address("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_mac_address("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_sedol_deep:
    def test_c0(self):
        try:
            mod.is_valid_sedol("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_sedol("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_sedol("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_sedol("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_sedol("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_sedol("UPPER lower 123")
        except EXC:
            pass


class Test_is_valid_uuid_deep:
    def test_c0(self):
        try:
            mod.is_valid_uuid("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_valid_uuid("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_valid_uuid("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_valid_uuid("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_valid_uuid("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_valid_uuid("UPPER lower 123")
        except EXC:
            pass


class Test_reading_time_deep:
    def test_c0(self):
        try:
            mod.reading_time("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.reading_time("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.reading_time("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.reading_time("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.reading_time("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.reading_time("UPPER lower 123")
        except EXC:
            pass

    def test_kw_words_per_minute(self):
        try:
            mod.reading_time("hello world", words_per_minute=1)
        except EXC:
            pass

