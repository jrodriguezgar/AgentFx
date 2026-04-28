"""Tests for fxString.string_convertions."""


import pytest

from shortfx.fxString.string_convertions import (
    base64_decode,
    base64_encode,
    hex_color_to_rgb,
    nato_phonetic_to_text,
    rgb_to_hex_color,
    text_to_hex,
    text_to_nato_phonetic,
    text_to_phonetic_ipa,
)
from shortfx.fxString.string_evaluations import is_balanced_brackets
from shortfx.fxString.string_operations import extract_domain_from_url


class TestIsBalancedBrackets:
    def test_balanced(self):
        assert is_balanced_brackets("(a + [b * {c}])") is True

    def test_unbalanced(self):
        assert is_balanced_brackets("(a + [b)") is False

    def test_empty(self):
        assert is_balanced_brackets("") is True

    def test_no_brackets(self):
        assert is_balanced_brackets("hello world") is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_balanced_brackets(123)


# ---------------------------------------------------------------------------
# fxString — string_convertions.py
# ---------------------------------------------------------------------------


class TestTextToNatoPhonetic:
    def test_basic(self):
        result = text_to_nato_phonetic("AB")
        assert result == "Alpha Bravo"

    def test_with_space(self):
        result = text_to_nato_phonetic("A B")
        assert "Alpha" in result
        assert "Bravo" in result

    def test_type_error(self):
        with pytest.raises(TypeError):
            text_to_nato_phonetic(42)

class TestNatoPhoneticToText:
    def test_basic(self):
        assert nato_phonetic_to_text("Alpha Bravo") == "AB"

    def test_roundtrip(self):
        original = "SOS"
        encoded = text_to_nato_phonetic(original)
        decoded = nato_phonetic_to_text(encoded)
        assert decoded == original.upper()

    def test_type_error(self):
        with pytest.raises(TypeError):
            nato_phonetic_to_text(42)

class TestTextToPhoneticIpa:

    def test_basic(self):
        result = text_to_phonetic_ipa("hello")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_type_error(self):

        with pytest.raises(TypeError):
            text_to_phonetic_ipa(42)

class TestHexColorRgb:

    def test_hex_to_rgb(self):
        assert hex_color_to_rgb("#FF8800") == (255, 136, 0)

    def test_hex_to_rgb_short(self):
        assert hex_color_to_rgb("#F00") == (255, 0, 0)

    def test_rgb_to_hex(self):
        assert rgb_to_hex_color(255, 136, 0) == "#FF8800"

    def test_roundtrip(self):
        r, g, b = hex_color_to_rgb("#1A2B3C")
        assert rgb_to_hex_color(r, g, b) == "#1A2B3C"

    def test_invalid_hex(self):

        with pytest.raises(ValueError):
            hex_color_to_rgb("#ZZZ")

    def test_rgb_out_of_range(self):

        with pytest.raises(ValueError):
            rgb_to_hex_color(256, 0, 0)


# ── fxDate ── date_operations ───────────────────────────────────────────

class TestBase64:

    def test_encode(self):
        assert base64_encode("Hello World") == "SGVsbG8gV29ybGQ="

    def test_decode(self):
        assert base64_decode("SGVsbG8gV29ybGQ=") == "Hello World"

    def test_roundtrip(self):
        original = "shortfx rocks!"
        assert base64_decode(base64_encode(original)) == original

    def test_decode_invalid(self):

        with pytest.raises(ValueError):
            base64_decode("not-valid!!!")


# ── fxDate ── date_convertions ──────────────────────────────────────────

class TestExtractDomainFromUrl:

    def test_with_www(self):
        assert extract_domain_from_url("https://www.example.com/path") == "example.com"

    def test_without_scheme(self):
        assert extract_domain_from_url("example.com/path") == "example.com"

    def test_with_port(self):
        assert extract_domain_from_url("https://example.com:8080/path") == "example.com"

    def test_empty(self):
        with pytest.raises(ValueError):
            extract_domain_from_url("")

    def test_type_error(self):
        with pytest.raises(TypeError):
            extract_domain_from_url(123)


# ── fxString · string_convertions ─────────────────────────────────────────


class TestTextToHex:

    def test_hello(self):
        assert text_to_hex("Hello") == "48656c6c6f"

    def test_empty(self):
        assert text_to_hex("") == ""

    def test_unicode(self):
        result = text_to_hex("ñ")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            text_to_hex(123)
