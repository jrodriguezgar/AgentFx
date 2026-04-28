"""Tests for shortfx._validators."""
import pytest
from shortfx._validators import (
    ensure_type, ensure_numeric, ensure_positive,
    ensure_non_negative, ensure_not_empty,
)

class TestEnsureType:
    def test_pass(self):
        ensure_type(3.14, (int, float), "rate")
    def test_fail(self):
        with pytest.raises(TypeError, match="rate"):
            ensure_type("x", (int, float), "rate")
    def test_single_type(self):
        ensure_type("hello", str, "name")
    def test_single_type_fail(self):
        with pytest.raises(TypeError):
            ensure_type(42, str, "name")

class TestEnsureNumeric:
    def test_int(self):
        ensure_numeric(42, "count")
    def test_float(self):
        ensure_numeric(3.14, "rate")
    def test_fail(self):
        with pytest.raises(TypeError, match="count"):
            ensure_numeric("x", "count")

class TestEnsurePositive:
    def test_pass(self):
        ensure_positive(5, "life")
    def test_zero_fail(self):
        with pytest.raises(ValueError, match="life"):
            ensure_positive(0, "life")
    def test_negative_fail(self):
        with pytest.raises(ValueError):
            ensure_positive(-1, "life")

class TestEnsureNonNegative:
    def test_zero_pass(self):
        ensure_non_negative(0, "count")
    def test_positive_pass(self):
        ensure_non_negative(5, "count")
    def test_fail(self):
        with pytest.raises(ValueError, match="count"):
            ensure_non_negative(-1, "count")

class TestEnsureNotEmpty:
    def test_pass(self):
        ensure_not_empty("hello", "text")
    def test_fail(self):
        with pytest.raises(ValueError, match="text"):
            ensure_not_empty("", "text")
