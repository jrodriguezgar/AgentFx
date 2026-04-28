"""Tests for fxNumeric.tensor_functions."""

import math

from agentfx.fxNumeric import (
    christoffel_symbols_diagonal,
    geodesic_equation_rhs,
    kronecker_delta,
    levi_civita,
    levi_civita_nd,
    lower_index,
    metric_tensor_cylindrical,
    metric_tensor_from_jacobian,
    metric_tensor_spherical,
    raise_index,
    riemann_christoffel_check_2d,
    tensor_contract,
    tensor_outer_product,
)


class TestKroneckerDelta:
    def test_equal(self):
        assert kronecker_delta(1, 1) == 1

    def test_not_equal(self):
        assert kronecker_delta(1, 2) == 0

class TestLeviCivita:
    def test_even(self):
        assert levi_civita(1, 2, 3) == 1

    def test_odd(self):
        assert levi_civita(1, 3, 2) == -1

    def test_repeated(self):
        assert levi_civita(1, 1, 2) == 0

class TestLeviCivitaNd:
    def test_4d_identity(self):
        assert levi_civita_nd([1, 2, 3, 4]) == 1

    def test_4d_swap(self):
        assert levi_civita_nd([2, 1, 3, 4]) == -1

    def test_repeated(self):
        assert levi_civita_nd([1, 1, 3, 4]) == 0

class TestMetricTensor:
    def test_identity_jacobian(self):
        g = metric_tensor_from_jacobian([[1, 0], [0, 1]])
        assert g == [[1, 0], [0, 1]]

    def test_spherical(self):
        g = metric_tensor_spherical(2.0, math.pi / 2)
        assert g[0][0] == 1
        assert round(g[1][1], 6) == 4.0
        assert round(g[2][2], 6) == 4.0

    def test_cylindrical(self):
        g = metric_tensor_cylindrical(3.0)
        assert g[1][1] == 9.0

class TestChristoffelSymbols:
    def test_flat_space(self):
        gamma = christoffel_symbols_diagonal([1, 1, 1], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        for k in range(3):
            for i in range(3):
                for j in range(3):
                    assert gamma[k][i][j] == 0.0

class TestTensorContract:
    def test_trace(self):
        assert tensor_contract([[1, 2], [3, 4]]) == 5

class TestTensorOuterProduct:
    def test_basic(self):
        assert tensor_outer_product([1, 2], [3, 4]) == [[3, 4], [6, 8]]

class TestRaiseLowerIndex:
    def test_raise(self):
        result = raise_index([3, 8], [1, 0.25])
        assert result == [3.0, 2.0]

    def test_lower(self):
        result = lower_index([3, 2], [1, 4])
        assert result == [3, 8]

class TestRiemann2d:
    def test_flat(self):
        gamma = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
        assert riemann_christoffel_check_2d(gamma) == 0.0

class TestGeodesicRhs:
    def test_flat(self):
        gamma = [[[0, 0], [0, 0]], [[0, 0], [0, 0]]]
        assert geodesic_equation_rhs(gamma, [1, 0]) == [0.0, 0.0]


# ===================================================================
# Special functions extensions
# ===================================================================
