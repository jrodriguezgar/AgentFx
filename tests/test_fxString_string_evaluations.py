"""Tests for fxString.string_evaluations."""


import pytest

from agentfx.fxString.string_evaluations import (
    automated_readability_index,
    avg_word_length,
    coleman_liau_index,
    flesch_reading_ease,
    gunning_fog_index,
    is_heterogram,
    is_isogram,
    is_lipogram,
    is_tautogram,
    is_valid_base64,
    is_valid_cron,
    is_valid_cusip,
    is_valid_ean,
    is_valid_hex_color,
    is_valid_iban,
    is_valid_ipv4,
    is_valid_ipv6,
    is_valid_isbn,
    is_valid_isin,
    is_valid_luhn,
    is_valid_mac_address,
    is_valid_mime_type,
    is_valid_regex,
    is_valid_sedol,
    is_valid_semver,
    is_valid_uuid,
    is_valid_vin,
    smog_index,
)
from agentfx.fxString.string_operations import extract_mentions


class TestTextEntropy:

    def test_uniform(self):
        from agentfx.fxString.string_evaluations import text_entropy

        assert round(text_entropy("abcd"), 2) == 2.0

    def test_all_same(self):
        from agentfx.fxString.string_evaluations import text_entropy

        assert text_entropy("aaaa") == 0.0

    def test_empty(self):
        from agentfx.fxString.string_evaluations import text_entropy

        assert text_entropy("") == 0.0

    def test_type_error(self):
        from agentfx.fxString.string_evaluations import text_entropy

        with pytest.raises(TypeError):
            text_entropy(123)


# ── fxDate ────────────────────────────────────────────────────────────────

class TestIsValidHexColor:

    def test_valid_6_digit(self):
        assert is_valid_hex_color("#FF8800") is True

    def test_valid_3_digit(self):
        assert is_valid_hex_color("#F80") is True

    def test_valid_8_digit_rgba(self):
        assert is_valid_hex_color("#FF8800AA") is True

    def test_valid_4_digit_rgba(self):
        assert is_valid_hex_color("#F80A") is True

    def test_invalid_no_hash(self):
        assert is_valid_hex_color("FF8800") is False

    def test_invalid_chars(self):
        assert is_valid_hex_color("#GGHHII") is False

    def test_invalid_length(self):
        assert is_valid_hex_color("#FF88F") is False

class TestIsValidCron:

    def test_valid_standard(self):
        assert is_valid_cron("0 12 * * 1-5") is True

    def test_valid_all_stars(self):
        assert is_valid_cron("* * * * *") is True

    def test_invalid_field_count(self):
        assert is_valid_cron("* * *") is False

    def test_invalid_range(self):
        assert is_valid_cron("70 * * * *") is False

    def test_valid_step(self):
        assert is_valid_cron("*/5 * * * *") is True


# ── fxString ── string_operations ───────────────────────────────────────

class TestIsValidIpv4:

    def test_valid(self):
        assert is_valid_ipv4("192.168.1.1") is True

    def test_valid_zeros(self):
        assert is_valid_ipv4("0.0.0.0") is True

    def test_invalid_octet(self):
        assert is_valid_ipv4("256.0.0.1") is False

    def test_leading_zeros(self):
        assert is_valid_ipv4("192.168.01.1") is False

    def test_too_few_parts(self):
        assert is_valid_ipv4("192.168.1") is False

    def test_type_error(self):

        with pytest.raises(TypeError):
            is_valid_ipv4(123)

class TestIsValidIpv6:

    def test_full(self):
        assert is_valid_ipv6("2001:0db8:85a3:0000:0000:8a2e:0370:7334") is True

    def test_compressed(self):
        assert is_valid_ipv6("2001:db8::8a2e:370:7334") is True

    def test_loopback(self):
        assert is_valid_ipv6("::1") is True

    def test_invalid(self):
        assert is_valid_ipv6("2001:db8::zzzz") is False

class TestIsValidUuid:

    def test_valid(self):
        assert is_valid_uuid("550e8400-e29b-41d4-a716-446655440000") is True

    def test_invalid_no_dashes(self):
        assert is_valid_uuid("550e8400e29b41d4a716446655440000") is False

    def test_invalid_chars(self):
        assert is_valid_uuid("550e8400-e29b-41d4-a716-44665544000g") is False

    def test_type_error(self):

        with pytest.raises(TypeError):
            is_valid_uuid(42)

class TestIsValidSemver:

    def test_basic(self):
        assert is_valid_semver("1.2.3") is True

    def test_with_prerelease(self):
        assert is_valid_semver("1.0.0-alpha.1") is True

    def test_with_build(self):
        assert is_valid_semver("1.0.0+build.42") is True

    def test_full(self):
        assert is_valid_semver("1.2.3-alpha.1+build.42") is True

    def test_leading_zero(self):
        assert is_valid_semver("01.2.3") is False

    def test_two_parts(self):
        assert is_valid_semver("1.2") is False

class TestIsValidMacAddress:

    def test_colon(self):
        assert is_valid_mac_address("00:1A:2B:3C:4D:5E") is True

    def test_dash(self):
        assert is_valid_mac_address("00-1A-2B-3C-4D-5E") is True

    def test_dot(self):
        assert is_valid_mac_address("001A.2B3C.4D5E") is True

    def test_no_separator(self):
        assert is_valid_mac_address("001A2B3C4D5E") is True

    def test_invalid_short(self):
        assert is_valid_mac_address("00:1A:2B") is False

class TestIsValidBase64:

    def test_valid(self):
        assert is_valid_base64("SGVsbG8gV29ybGQ=") is True

    def test_no_padding(self):
        assert is_valid_base64("SGVsbG8=") is True

    def test_invalid_chars(self):
        assert is_valid_base64("SGVs bG8=") is False

    def test_bad_padding(self):
        assert is_valid_base64("SGV") is False


# ── fxString ── string_operations ───────────────────────────────────────

class TestStringValidationsPhase20b:
    """E.164 phone and password strength."""

    def test_is_valid_e164_phone_valid(self):
        from agentfx.fxString.string_evaluations import is_valid_e164_phone

        assert is_valid_e164_phone("+34612345678") is True

    def test_is_valid_e164_phone_no_plus(self):
        from agentfx.fxString.string_evaluations import is_valid_e164_phone

        assert is_valid_e164_phone("34612345678") is False

    def test_is_valid_e164_phone_too_long(self):
        from agentfx.fxString.string_evaluations import is_valid_e164_phone

        assert is_valid_e164_phone("+1234567890123456") is False

    def test_is_valid_e164_phone_leading_zero(self):
        from agentfx.fxString.string_evaluations import is_valid_e164_phone

        assert is_valid_e164_phone("+0123456789") is False

    def test_is_valid_e164_phone_type_error(self):
        from agentfx.fxString.string_evaluations import is_valid_e164_phone

        with pytest.raises(TypeError):
            is_valid_e164_phone(123)

    def test_check_password_strength_empty(self):
        from agentfx.fxString.string_evaluations import check_password_strength

        assert check_password_strength("") == 0

    def test_check_password_strength_weak(self):
        from agentfx.fxString.string_evaluations import check_password_strength

        score = check_password_strength("abc")
        assert 0 < score < 50

    def test_check_password_strength_strong(self):
        from agentfx.fxString.string_evaluations import check_password_strength

        score = check_password_strength("C0mpl3x!Pass#2026")
        assert score >= 80

    def test_check_password_strength_type_error(self):
        from agentfx.fxString.string_evaluations import check_password_strength

        with pytest.raises(TypeError):
            check_password_strength(12345)


# =====================================================================
# fxString — string_operations (password generator)
# =====================================================================

class TestIsIsogram:
    def test_true(self):
        assert is_isogram("subdermatoglyphic") is True

    def test_false(self):
        assert is_isogram("hello") is False

    def test_empty(self):
        assert is_isogram("") is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_isogram(123)

class TestIsHeterogram:
    def test_true(self):
        assert is_heterogram("abcde") is True

    def test_false(self):
        assert is_heterogram("aab") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_heterogram(123)

class TestIsTautogram:
    def test_true(self):
        assert is_tautogram("Peter Piper picked peppers") is True

    def test_false(self):
        assert is_tautogram("The quick brown fox") is False

    def test_empty(self):
        assert is_tautogram("") is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_tautogram(123)

class TestIsLipogram:
    def test_absent(self):
        assert is_lipogram("The quick brown fox", "z") is True

    def test_present(self):
        assert is_lipogram("The quick brown fox jumps over the lazy dog", "z") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_lipogram(123, "a")

    def test_value_error(self):
        with pytest.raises(ValueError):
            is_lipogram("hello", "ab")

class TestFleschReadingEase:
    def test_basic(self):
        assert round(flesch_reading_ease("The cat sat on the mat."), 1) == 116.1

    def test_type_error(self):
        with pytest.raises(TypeError):
            flesch_reading_ease(123)

    def test_empty(self):
        with pytest.raises(ValueError):
            flesch_reading_ease("")

class TestGunningFogIndex:
    def test_basic(self):
        assert round(gunning_fog_index("The cat sat on the mat."), 1) == 2.4

    def test_type_error(self):
        with pytest.raises(TypeError):
            gunning_fog_index(123)

    def test_empty(self):
        with pytest.raises(ValueError):
            gunning_fog_index("")

class TestAutomatedReadabilityIndex:
    def test_basic(self):
        assert round(automated_readability_index("The cat sat on the mat."), 1) == -5.1

    def test_type_error(self):
        with pytest.raises(TypeError):
            automated_readability_index(123)

class TestColemanLiauIndex:
    def test_basic(self):
        assert round(coleman_liau_index("The cat sat on the mat."), 1) == -4.1

    def test_type_error(self):
        with pytest.raises(TypeError):
            coleman_liau_index(123)

class TestSmogIndex:
    def test_basic(self):
        assert round(smog_index("The cat sat on the mat."), 1) == 3.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            smog_index(123)

class TestAvgWordLength:
    def test_basic(self):
        assert avg_word_length("The cat sat") == 3.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            avg_word_length(123)

    def test_empty(self):
        with pytest.raises(ValueError):
            avg_word_length("")


# ── Date Operations ──────────────────────────────────────────────────────

class TestExtractMentions:

    def test_basic(self):
        assert extract_mentions("Hi @alice and @bob!") == ["@alice", "@bob"]

    def test_none(self):
        assert extract_mentions("no mentions") == []


# ---------------------------------------------------------------------------
# fxString — string_evaluations.py
# ---------------------------------------------------------------------------


class TestIsValidRegex:

    def test_valid(self):
        assert is_valid_regex(r"\d{3}-\d{4}") is True

    def test_invalid(self):
        assert is_valid_regex("[unclosed") is False

    def test_empty(self):
        assert is_valid_regex("") is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_regex(123)

class TestIsValidMimeType:

    def test_json(self):
        assert is_valid_mime_type("application/json") is True

    def test_html(self):
        assert is_valid_mime_type("text/html") is True

    def test_invalid(self):
        assert is_valid_mime_type("not-a-mime") is False

    def test_image(self):
        assert is_valid_mime_type("image/png") is True


# ---------------------------------------------------------------------------
# fxString — string_convertions.py
# ---------------------------------------------------------------------------


class TestIsValidIban:

    def test_valid_gb(self):
        assert is_valid_iban("GB29 NWBK 6016 1331 9268 19") is True

    def test_valid_de(self):
        assert is_valid_iban("DE89 3704 0044 0532 0130 00") is True

    def test_valid_es(self):
        assert is_valid_iban("ES91 2100 0418 4502 0005 1332") is True

    def test_invalid_check_digit(self):
        assert is_valid_iban("GB29 NWBK 6016 1331 9268 18") is False

    def test_too_short(self):
        assert is_valid_iban("GB29") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_iban(123)

class TestIsValidIsbn:

    def test_isbn13_valid(self):
        assert is_valid_isbn("978-3-16-148410-0") is True

    def test_isbn10_valid(self):
        assert is_valid_isbn("0-306-40615-2") is True

    def test_isbn10_with_x(self):
        assert is_valid_isbn("0-19-853453-1") is True

    def test_isbn13_invalid(self):
        assert is_valid_isbn("978-3-16-148410-1") is False

    def test_wrong_length(self):
        assert is_valid_isbn("12345") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_isbn(978)

class TestIsValidLuhn:

    def test_valid_card(self):
        assert is_valid_luhn("4539148803436467") is True

    def test_invalid_card(self):
        assert is_valid_luhn("1234567890") is False

    def test_with_spaces(self):
        assert is_valid_luhn("4539 1488 0343 6467") is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_luhn(4539)

class TestIsValidEan:

    def test_ean13_valid(self):
        assert is_valid_ean("4006381333931") is True

    def test_ean8_valid(self):
        assert is_valid_ean("96385074") is True

    def test_ean13_invalid(self):
        assert is_valid_ean("4006381333932") is False

    def test_wrong_length(self):
        assert is_valid_ean("12345") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_ean(123)

class TestIsValidIsin:

    def test_valid_us(self):
        assert is_valid_isin("US0378331005") is True

    def test_valid_gb(self):
        assert is_valid_isin("GB0002634946") is True

    def test_invalid_check_digit(self):
        assert is_valid_isin("US0378331006") is False

    def test_wrong_length(self):
        assert is_valid_isin("US037833100") is False

    def test_strips_whitespace(self):
        assert is_valid_isin("  US0378331005  ") is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_isin(123)

    def test_lowercase_accepted(self):
        assert is_valid_isin("us0378331005") is True

class TestIsValidCusip:

    def test_valid_apple(self):
        assert is_valid_cusip("037833100") is True

    def test_invalid_check(self):
        assert is_valid_cusip("037833101") is False

    def test_wrong_length(self):
        assert is_valid_cusip("03783310") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_cusip(37833100)

class TestIsValidSedol:

    def test_valid(self):
        assert is_valid_sedol("0263494") is True

    def test_invalid(self):
        assert is_valid_sedol("0263495") is False

    def test_wrong_length(self):
        assert is_valid_sedol("026349") is False

    def test_vowel_rejected(self):
        # SEDOL chars exclude vowels
        assert is_valid_sedol("A263494") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_sedol(263494)

class TestIsValidVin:

    def test_valid(self):
        assert is_valid_vin("1M8GDM9AXKP042788") is True

    def test_invalid_check(self):
        assert is_valid_vin("1M8GDM9A1KP042788") is False

    def test_wrong_length(self):
        assert is_valid_vin("1M8GDM9AXK") is False

    def test_forbidden_chars(self):
        # I, O, Q are not allowed
        assert is_valid_vin("1M8GDM9AIKP042788") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_vin(12345)
