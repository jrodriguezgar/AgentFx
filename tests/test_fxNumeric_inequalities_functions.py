"""Tests for fxNumeric.inequalities_functions."""

import math

import pytest

from shortfx.fxNumeric import (
    am_gm_inequality,
    am_hm_inequality,
    bernoulli_inequality,
    cauchy_schwarz_inequality,
    chebyshev_sum_inequality,
    holder_inequality,
    jensen_inequality,
    minkowski_inequality,
    power_mean,
    rearrangement_inequality,
    triangle_inequality_vector,
    young_inequality,
)


class TestInequalities:

    def test_am_gm(self):
        am, gm, holds = am_gm_inequality([1, 2, 3, 4])
        assert holds
        assert am >= gm

    def test_am_hm(self):
        am, hm, holds = am_hm_inequality([1, 2, 3])
        assert holds
        assert am >= hm

    def test_power_mean(self):
        # p=1 → arithmetic mean
        assert abs(power_mean([2, 4, 6], 1) - 4.0) < 1e-10
        # p=2 → quadratic mean
        assert power_mean([3, 4], 2) == pytest.approx(math.sqrt(12.5), abs=1e-6)

    def test_cauchy_schwarz(self):
        lhs, rhs, holds = cauchy_schwarz_inequality([1, 2], [3, 4])
        assert holds
        assert lhs <= rhs + 1e-10

    def test_triangle_inequality_vector(self):
        lhs, rhs, holds = triangle_inequality_vector([3, -4, 1])
        assert holds
        assert lhs <= rhs + 1e-10

    def test_minkowski(self):
        lhs, rhs, holds = minkowski_inequality([1, 2], [3, 4], 2)
        assert holds

    def test_holder(self):
        lhs, rhs, holds = holder_inequality([1, 2], [3, 4], 2)
        assert holds

    def test_young(self):
        lhs, rhs, holds = young_inequality(2, 3, 2)
        assert holds

    def test_jensen(self):
        # log is concave: f(mean) >= mean(f)
        lhs, rhs, holds = jensen_inequality(lambda x: x ** 2, [1, 3])
        assert holds

    def test_chebyshev_sum(self):
        lhs, rhs, holds = chebyshev_sum_inequality([1, 2, 3], [1, 2, 3])
        assert holds

    def test_rearrangement(self):
        min_s, mid_s, max_s = rearrangement_inequality([1, 2, 3], [1, 2, 3])
        assert max_s >= min_s

    def test_bernoulli(self):
        lhs, rhs, holds = bernoulli_inequality(0.5, 3)
        assert holds


# ===================================================================
# Coordinate systems
# ===================================================================
