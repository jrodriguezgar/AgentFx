"""Tests for formulite.fxNumeric low-coverage modules."""
import math
import pytest

# -- rounding_functions --
from formulite.fxNumeric.rounding_functions import (
    round_to_n_decimals, round_up, round_down, round_half_even,
    truncate_float, round_to_nearest_multiple,
    ceiling_math, floor_math, even, odd,
)

class TestRounding:
    def test_round_decimals(self):
        assert round_to_n_decimals(3.456, 2) == pytest.approx(3.46)
    def test_round_up(self):
        assert round_up(3.1) == 4
    def test_round_down(self):
        assert round_down(3.9) == 3
    def test_round_half_even(self):
        assert round_half_even(2.5) == 2
    def test_truncate(self):
        assert truncate_float(3.789) == 3.0
    def test_round_nearest(self):
        assert round_to_nearest_multiple(17, 5) == 15
    def test_ceiling_math(self):
        assert ceiling_math(2.3) == 3
    def test_floor_math(self):
        assert floor_math(2.7) == 2
    def test_even(self):
        assert even(3) == 4 and even(4) == 4
    def test_odd(self):
        assert odd(4) == 5 and odd(5) == 5

# -- random_functions --
from formulite.fxNumeric.random_functions import (
    random_int, random_float, random_choice, random_bool,
    random_uuid, random_array,
)

class TestRandom:
    def test_random_int(self):
        r = random_int(1, 10)
        assert 1 <= r <= 10
    def test_random_float(self):
        r = random_float(0.0, 1.0)
        assert 0.0 <= r <= 1.0
    def test_random_choice(self):
        assert random_choice([1, 2, 3]) in [1, 2, 3]
    def test_random_bool(self):
        assert isinstance(random_bool(), bool)
    def test_random_uuid(self):
        u = random_uuid()
        assert len(u) == 36
    def test_random_array(self):
        r = random_array(5)
        assert len(r) == 5

# -- format_functions --
from formulite.fxNumeric.format_functions import (
    format_as_percentage, format_as_scientific_notation,
    format_with_leading_zeros, percent_change,
)

class TestNumericFormat:
    def test_percentage(self):
        r = format_as_percentage(0.25)
        assert "25" in r
    def test_scientific(self):
        r = format_as_scientific_notation(1234.5)
        assert "e" in r.lower() or "E" in r
    def test_leading_zeros(self):
        r = format_with_leading_zeros(42, 6)
        assert r == "000042"
    def test_percent_change(self):
        assert percent_change(100, 110) == pytest.approx(10.0)


# -- interpolation_functions --
from formulite.fxNumeric.interpolation_functions import (
    linear_interpolation, lagrange_interpolation,
    map_range, clip_number,
)

class TestInterpolation:
    def test_linear(self):
        assert linear_interpolation(5.0, [0.0, 10.0], [0.0, 10.0]) == pytest.approx(5.0)
    def test_lagrange(self):
        xs = [0.0, 1.0, 2.0]
        ys = [0.0, 1.0, 4.0]
        assert lagrange_interpolation(xs, ys, 1.5) == pytest.approx(2.25)
    def test_map_range(self):
        assert map_range(5, 0, 10, 0, 100) == pytest.approx(50.0)
    def test_clip(self):
        assert clip_number(15, 0, 10) == 10
        assert clip_number(-5, 0, 10) == 0
