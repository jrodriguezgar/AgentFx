"""Tests for fxNumeric.finite_differences_functions."""


from agentfx.fxNumeric import (
    bessel_interpolation,
    divided_difference_table,
    forward_difference_table,
    gauss_forward_interpolation,
    newton_backward_interpolation,
    newton_forward_interpolation,
    stirling_interpolation,
)


class TestForwardDifferenceTable:
    def test_squares(self):
        table = forward_difference_table([1, 4, 9, 16])
        assert table[0] == [1, 4, 9, 16]
        assert table[1] == [3, 5, 7]
        assert table[2] == [2, 2]
        assert table[3] == [0]

class TestNewtonForward:
    def test_interpolate_squares(self):
        result = newton_forward_interpolation([0, 1, 2, 3], [0, 1, 4, 9], 1.5)
        assert round(result, 6) == 2.25

    def test_exact_node(self):
        result = newton_forward_interpolation([0, 1, 2, 3], [0, 1, 4, 9], 2.0)
        assert round(result, 6) == 4.0

class TestNewtonBackward:
    def test_interpolate_squares(self):
        result = newton_backward_interpolation([0, 1, 2, 3], [0, 1, 4, 9], 2.5)
        assert round(result, 6) == 6.25

class TestStirlingInterpolation:
    def test_at_center(self):
        result = stirling_interpolation([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], 2.0)
        assert round(result, 1) == 8.0

class TestBesselInterpolation:
    def test_cubes(self):
        result = bessel_interpolation([0, 1, 2, 3], [0, 1, 8, 27], 1.5)
        assert round(result, 1) == 3.4  # approximate

class TestGaussForward:
    def test_cubes(self):
        result = gauss_forward_interpolation([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], 2.5)
        assert round(result, 1) == 15.6  # approximate

class TestDividedDifferenceTable:
    def test_basic(self):
        table = divided_difference_table([1, 2, 4], [1, 8, 64])
        assert table[0] == [1, 8, 64]
        assert table[1] == [7.0, 28.0]
        assert table[2] == [7.0]


# ===================================================================
# Tensor analysis
# ===================================================================
