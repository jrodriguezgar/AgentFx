"""Tests for fxNumeric.interpolation_functions."""


import pytest


class TestLagrangeInterpolation:

    def test_quadratic(self):
        from shortfx.fxNumeric.interpolation_functions import lagrange_interpolation
        assert lagrange_interpolation([1, 2, 3], [1, 4, 9], 2.5) == 6.25

    def test_linear(self):
        from shortfx.fxNumeric.interpolation_functions import lagrange_interpolation
        assert lagrange_interpolation([0, 10], [0, 100], 5) == 50.0

    def test_empty_raises(self):
        from shortfx.fxNumeric.interpolation_functions import lagrange_interpolation

        with pytest.raises(ValueError):
            lagrange_interpolation([], [], 1)

    def test_duplicate_x_raises(self):
        from shortfx.fxNumeric.interpolation_functions import lagrange_interpolation

        with pytest.raises(ValueError):
            lagrange_interpolation([1, 1], [2, 3], 1)

class TestBilinearInterpolation:

    def test_center(self):
        from shortfx.fxNumeric.interpolation_functions import bilinear_interpolation
        assert bilinear_interpolation(0.5, 0.5, 0, 1, 0, 1, 0, 1, 1, 2) == 1.0

    def test_corner(self):
        from shortfx.fxNumeric.interpolation_functions import bilinear_interpolation
        assert bilinear_interpolation(0, 0, 0, 1, 0, 1, 10, 20, 30, 40) == 10.0

    def test_same_x_raises(self):
        from shortfx.fxNumeric.interpolation_functions import bilinear_interpolation

        with pytest.raises(ValueError):
            bilinear_interpolation(0.5, 0.5, 1, 1, 0, 1, 0, 1, 1, 2)


# ── Conversions ─────────────────────────────────────────────────

class TestNewtonDividedDifference:

    def test_quadratic(self):
        from shortfx.fxNumeric.interpolation_functions import newton_divided_difference
        result = newton_divided_difference([1, 2, 3], [1, 4, 9], 2.5)
        assert result == pytest.approx(6.25)

    def test_linear(self):
        from shortfx.fxNumeric.interpolation_functions import newton_divided_difference
        result = newton_divided_difference([0, 10], [0, 100], 5)
        assert result == pytest.approx(50.0)

    def test_exact_point(self):
        from shortfx.fxNumeric.interpolation_functions import newton_divided_difference
        result = newton_divided_difference([1, 2, 3], [1, 4, 9], 2)
        assert result == pytest.approx(4.0)

class TestCubicSplineNatural:

    def test_quadratic_data(self):
        from shortfx.fxNumeric.interpolation_functions import cubic_spline_natural
        result = cubic_spline_natural([0, 1, 2, 3], [0, 1, 4, 9], 1.5)
        assert result == pytest.approx(2.25, rel=0.1)

    def test_linear_data(self):
        from shortfx.fxNumeric.interpolation_functions import cubic_spline_natural
        result = cubic_spline_natural([0, 1, 2], [0, 1, 2], 0.5)
        assert result == pytest.approx(0.5, rel=0.01)

    def test_two_points(self):
        from shortfx.fxNumeric.interpolation_functions import cubic_spline_natural
        result = cubic_spline_natural([0, 10], [0, 100], 5)
        assert result == pytest.approx(50.0)

    def test_unsorted_raises(self):
        from shortfx.fxNumeric.interpolation_functions import cubic_spline_natural
        with pytest.raises(ValueError):
            cubic_spline_natural([3, 1, 2], [9, 1, 4], 2)


# ── Date Functions ─────────────────────────────────────────────────────────
