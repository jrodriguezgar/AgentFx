"""Tests for fxExcel.engineering_formulas."""


import pytest

from agentfx.fxExcel.engineering_formulas import (
    BIN2DEC,
    BIN2HEX,
    BIN2OCT,
    DEC2BIN,
    DEC2HEX,
    DEC2OCT,
    HEX2BIN,
    HEX2DEC,
    HEX2OCT,
    OCT2BIN,
    OCT2DEC,
    OCT2HEX,
)
from agentfx.fxNumeric.statistics_functions import quantile


class TestQuantile:

    def test_median(self):
        assert quantile([1, 2, 3, 4, 5], 0.5) == 3.0

    def test_q25(self):
        assert quantile([1, 2, 3, 4, 5], 0.25) == 2.0

    def test_bounds(self):
        assert quantile([10, 20, 30], 0) == 10.0
        assert quantile([10, 20, 30], 1) == 30.0

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            quantile([1, 2], 1.5)


# ── Excel Engineering Base Conversions ───────────────────────────────────────


class TestBIN2DEC:

    def test_positive(self):
        assert BIN2DEC("1100100") == 100

    def test_negative(self):
        assert BIN2DEC("1111111111") == -1

    def test_zero(self):
        assert BIN2DEC("0") == 0

    def test_invalid_chars(self):
        with pytest.raises(ValueError):
            BIN2DEC("102")

    def test_too_long(self):
        with pytest.raises(ValueError):
            BIN2DEC("11111111111")

class TestDEC2BIN:

    def test_positive(self):
        assert DEC2BIN(100) == "1100100"

    def test_negative(self):
        assert DEC2BIN(-1) == "1111111111"

    def test_with_places(self):
        assert DEC2BIN(10, 8) == "00001010"

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            DEC2BIN(600)

class TestHEX:

    def test_hex2dec(self):
        assert HEX2DEC("FF") == 255

    def test_hex2dec_negative(self):
        assert HEX2DEC("FFFFFFFFFF") == -1

    def test_dec2hex(self):
        assert DEC2HEX(255) == "FF"

    def test_dec2hex_negative(self):
        assert DEC2HEX(-1) == "FFFFFFFFFF"

    def test_hex2bin(self):
        assert HEX2BIN("A", 8) == "00001010"

    def test_hex2oct(self):
        assert HEX2OCT("FF") == "377"

class TestOCT:

    def test_oct2dec(self):
        assert OCT2DEC("144") == 100

    def test_oct2dec_negative(self):
        assert OCT2DEC("7777777777") == -1

    def test_dec2oct(self):
        assert DEC2OCT(100) == "144"

    def test_oct2bin(self):
        assert OCT2BIN("11", 8) == "00001001"

    def test_oct2hex(self):
        assert OCT2HEX("144") == "64"

class TestBIN2HEX:

    def test_basic(self):
        assert BIN2HEX("11111011") == "FB"

    def test_with_places(self):
        assert BIN2HEX("1010", 4) == "000A"

class TestBIN2OCT:

    def test_basic(self):
        assert BIN2OCT("1001") == "11"

    def test_with_places(self):
        assert BIN2OCT("1100100", 4) == "0144"
