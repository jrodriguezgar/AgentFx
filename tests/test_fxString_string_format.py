"""Tests for fxString.string_format."""


import pytest

from shortfx.fxString.string_format import format_file_size


class TestFormatFileSize:
    def test_zero(self):
        assert format_file_size(0) == "0 B"

    def test_binary_kib(self):
        assert format_file_size(1536) == "1.50 KiB"

    def test_decimal_kb(self):
        assert format_file_size(1500, binary=False) == "1.50 KB"

    def test_type_error(self):
        with pytest.raises(TypeError):
            format_file_size("big")

    def test_negative(self):
        with pytest.raises(ValueError):
            format_file_size(-1)


# ---------------------------------------------------------------------------
# fxString — string_evaluations.py
# ---------------------------------------------------------------------------

