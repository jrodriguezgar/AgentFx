"""Tests for fxNumeric.polynomial_functions."""


from agentfx.fxNumeric import (
    partial_fraction_simple,
    polynomial_add,
    polynomial_composition,
    polynomial_degree,
    polynomial_derivative,
    polynomial_divide,
    polynomial_evaluate,
    polynomial_from_roots,
    polynomial_gcd,
    polynomial_integral,
    polynomial_multiply,
    polynomial_scale,
    polynomial_subtract,
)


class TestPolynomialAdd:
    def test_basic(self):
        assert polynomial_add([1, 2, 3], [4, 5]) == [1, 6, 8]

    def test_same_degree(self):
        assert polynomial_add([1, 0], [0, 1]) == [1, 1]

    def test_zero_result(self):
        assert polynomial_add([1, 2], [-1, -2]) == [0]

class TestPolynomialSubtract:
    def test_basic(self):
        assert polynomial_subtract([1, 2, 3], [4, 5]) == [1, -2, -2]

class TestPolynomialMultiply:
    def test_binomial(self):
        assert polynomial_multiply([1, 1], [1, -1]) == [1, 0, -1]

    def test_square(self):
        assert polynomial_multiply([1, 1], [1, 1]) == [1, 2, 1]

class TestPolynomialScale:
    def test_double(self):
        assert polynomial_scale([1, 2, 3], 2) == [2, 4, 6]

class TestPolynomialDivide:
    def test_exact(self):
        q, r = polynomial_divide([1, -3, 2], [1, -1])
        assert [round(c, 6) for c in q] == [1, -2]
        assert [round(c, 6) for c in r] == [0]

    def test_with_remainder(self):
        q, r = polynomial_divide([1, 0, 0], [1, 1])
        assert [round(c, 6) for c in q] == [1, -1]
        assert [round(c, 6) for c in r] == [1]

class TestPolynomialDerivative:
    def test_cubic(self):
        assert polynomial_derivative([3, 0, -2, 1]) == [9, 0, -2]

    def test_constant(self):
        assert polynomial_derivative([5]) == [0]

class TestPolynomialIntegral:
    def test_quadratic(self):
        result = polynomial_integral([3, 0, -2])
        assert [round(c, 6) for c in result] == [1, 0, -2, 0]

class TestPolynomialEvaluate:
    def test_at_root(self):
        assert polynomial_evaluate([1, -3, 2], 2) == 0

    def test_at_root2(self):
        assert polynomial_evaluate([1, -3, 2], 1) == 0

class TestPolynomialGcd:
    def test_common_factor(self):
        # (x-1)(x-2) and (x-1) → gcd = (x-1) i.e. [1, -1]
        gcd = polynomial_gcd([1, -3, 2], [1, -1])
        assert [round(c, 6) for c in gcd] == [1, -1]

class TestPolynomialComposition:
    def test_square_of_linear(self):
        # p = x^2 + 1 composed with q = x + 1 → (x+1)^2 + 1 = x^2 + 2x + 2
        result = polynomial_composition([1, 0, 1], [1, 1])
        assert result == [1, 2, 2]

class TestPartialFractionSimple:
    def test_two_roots(self):
        # 1 / ((x-1)(x-2)) → A/(x-1) + B/(x-2)
        # A = 1/(-1) = -1, B = 1/(1) = 1
        coeffs = partial_fraction_simple([1], [1, 2])
        assert [round(c, 6) for c in coeffs] == [-1, 1]

class TestPolynomialFromRoots:
    def test_two_roots(self):
        assert polynomial_from_roots([1, -1]) == [1, 0, -1]

    def test_single_root(self):
        assert polynomial_from_roots([3]) == [1, -3]

class TestPolynomialDegree:
    def test_cubic(self):
        assert polynomial_degree([3, 0, -2, 1]) == 3

    def test_constant(self):
        assert polynomial_degree([5]) == 0


# ===================================================================
# Finite differences
# ===================================================================
