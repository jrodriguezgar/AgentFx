"""Tests for fxNumeric.numerical_methods_functions."""

import math

import pytest

from formulite.fxNumeric.arithmetic_functions import (
    euler_method,
    fixed_point_iteration,
    gaussian_quadrature,
    secant_method,
)
from formulite.fxNumeric.statistics_functions import ewma_variance
from formulite.fxNumeric import numerical_methods_functions as nm


class TestRootFinding:

    def test_newton_sqrt2(self):
        from formulite.fxNumeric.arithmetic_functions import newton_raphson

        root = newton_raphson(lambda x: x ** 2 - 2, lambda x: 2 * x, 1.0)
        assert root == pytest.approx(math.sqrt(2), abs=1e-10)

    def test_bisection_sqrt2(self):
        from formulite.fxNumeric.arithmetic_functions import bisection_method

        root = bisection_method(lambda x: x ** 2 - 2, 1, 2)
        assert root == pytest.approx(math.sqrt(2), abs=1e-8)

    def test_bisection_same_sign_raises(self):
        from formulite.fxNumeric.arithmetic_functions import bisection_method

        with pytest.raises(ValueError):
            bisection_method(lambda x: x ** 2 + 1, 0, 3)

class TestEwmaVariance:
    def test_basic(self):
        data = [10, 12, 11, 13, 15]
        result = ewma_variance(data)
        assert len(result) == len(data)
        assert result[0] == 0.0

    def test_empty(self):
        with pytest.raises(ValueError):
            ewma_variance([])

    def test_invalid_alpha(self):
        with pytest.raises(ValueError):
            ewma_variance([1, 2, 3], alpha=0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            ewma_variance("abc")


# ---------------------------------------------------------------------------
# fxNumeric — arithmetic_functions.py
# ---------------------------------------------------------------------------

from formulite.fxNumeric.arithmetic_functions import (
    secant_method,
    fixed_point_iteration,
    romberg_integrate,
    adaptive_simpson,
)

class TestSecantMethod:
    def test_square_root_of_2(self):
        f = lambda x: x**2 - 2
        result = secant_method(f, 1.0, 2.0)
        assert result == pytest.approx(math.sqrt(2), abs=1e-8)

    def test_type_error(self):
        with pytest.raises(TypeError):
            secant_method("not_a_func", 1.0, 2.0)

class TestFixedPointIteration:
    def test_cos_fixed_point(self):
        g = lambda x: math.cos(x)
        result = fixed_point_iteration(g, 1.0)
        assert result == pytest.approx(0.7390851332, abs=1e-6)

    def test_type_error(self):
        with pytest.raises(TypeError):
            fixed_point_iteration("not_a_func", 1.0)

class TestGaussianQuadrature:

    def test_sin_integral(self):
        result = gaussian_quadrature(math.sin, 0, math.pi, 5)
        assert abs(result - 2.0) < 0.001

class TestEulerMethod:

    def test_exponential(self):
        pts = euler_method(lambda t, y: y, 1.0, 0.0, 1.0, 1000)
        assert abs(pts[-1][1] - math.e) < 0.01

    def test_invalid_steps(self):

        with pytest.raises(ValueError):
            euler_method(lambda t, y: y, 1, 0, 1, 0)


# ── fxNumeric ── conversion_functions ───────────────────────────────────

class TestTrapezoidalRule:

    def test_sin_integral(self):
        result = nm.trapezoidal_rule(math.sin, 0, math.pi, 10000)
        assert abs(result - 2.0) < 1e-6

    def test_polynomial(self):
        result = nm.trapezoidal_rule(lambda x: x ** 2, 0, 1, 10000)
        assert abs(result - 1 / 3) < 1e-5

    def test_type_error(self):
        with pytest.raises(TypeError):
            nm.trapezoidal_rule("not callable", 0, 1)

class TestSimpsonsRule:

    def test_sin_integral(self):
        result = nm.simpsons_rule(math.sin, 0, math.pi, 100)
        assert abs(result - 2.0) < 1e-7

    def test_cubic(self):
        result = nm.simpsons_rule(lambda x: x ** 3, 0, 1, 100)
        assert abs(result - 0.25) < 1e-10

    def test_odd_n_raises(self):
        with pytest.raises(ValueError):
            nm.simpsons_rule(math.sin, 0, 1, 3)

class TestSimpsons38Rule:

    def test_sin_integral(self):
        result = nm.simpsons_38_rule(math.sin, 0, math.pi, 999)
        assert abs(result - 2.0) < 1e-6

    def test_divisibility_error(self):
        with pytest.raises(ValueError):
            nm.simpsons_38_rule(math.sin, 0, 1, 4)

class TestMidpointRule:

    def test_sin_integral(self):
        result = nm.midpoint_rule(math.sin, 0, math.pi, 10000)
        assert abs(result - 2.0) < 1e-5

    def test_constant(self):
        result = nm.midpoint_rule(lambda x: 5.0, 0, 3, 100)
        assert abs(result - 15.0) < 1e-10

class TestGaussianQuadratureV2:

    def test_sin_integral(self):
        result = nm.gaussian_quadrature(math.sin, 0, math.pi, 5)
        assert abs(result - 2.0) < 1e-6

    def test_invalid_n(self):
        with pytest.raises(ValueError):
            nm.gaussian_quadrature(math.sin, 0, 1, 7)

class TestRomberg:

    def test_sin_integral(self):
        result = nm.romberg_integration(math.sin, 0, math.pi)
        assert abs(result - 2.0) < 1e-10

    def test_exponential(self):
        result = nm.romberg_integration(math.exp, 0, 1)
        assert abs(result - (math.e - 1)) < 1e-10

class TestMonteCarloIntegration:

    def test_sin_integral(self):
        result = nm.monte_carlo_integration(math.sin, 0, math.pi, 200000, seed=42)
        assert abs(result - 2.0) < 0.05


# ===================================================================
# Numerical Differentiation
# ===================================================================

class TestForwardDifference:

    def test_sin_at_zero(self):
        assert abs(nm.forward_difference(math.sin, 0) - 1.0) < 1e-5

    def test_x_squared(self):
        assert abs(nm.forward_difference(lambda x: x ** 2, 3) - 6.0) < 1e-4

class TestBackwardDifference:

    def test_sin_at_zero(self):
        assert abs(nm.backward_difference(math.sin, 0) - 1.0) < 1e-5

class TestCentralDifference:

    def test_sin_at_zero(self):
        assert abs(nm.central_difference(math.sin, 0) - 1.0) < 1e-10

    def test_cos_at_pi(self):
        assert abs(nm.central_difference(math.cos, math.pi) - 0.0) < 1e-6

class TestSecondDerivativeCentral:

    def test_sin_at_zero(self):
        assert abs(nm.second_derivative_central(math.sin, 0)) < 1e-5

    def test_x_squared(self):
        assert abs(nm.second_derivative_central(lambda x: x ** 2, 1) - 2.0) < 1e-4

class TestRichardsonExtrapolation:

    def test_sin_at_zero(self):
        result = nm.richardson_extrapolation(math.sin, 0, 0.1, 4)
        assert abs(result - 1.0) < 1e-10


# ===================================================================
# Root-Finding Methods
# ===================================================================

class TestBisection:

    def test_sqrt2(self):
        result = nm.bisection_method(lambda x: x ** 2 - 2, 1, 2)
        assert abs(result - math.sqrt(2)) < 1e-10

    def test_same_sign_error(self):
        with pytest.raises(ValueError):
            nm.bisection_method(lambda x: x ** 2 + 1, 0, 1)

class TestNewtonRaphson:

    def test_sqrt2(self):
        result = nm.newton_raphson(lambda x: x ** 2 - 2, lambda x: 2 * x, 1.0)
        assert abs(result - math.sqrt(2)) < 1e-10

    def test_cube_root(self):
        result = nm.newton_raphson(lambda x: x ** 3 - 8, lambda x: 3 * x ** 2, 1.0)
        assert abs(result - 2.0) < 1e-10

class TestSecantMethodV2:

    def test_sqrt2(self):
        result = nm.secant_method(lambda x: x ** 2 - 2, 1.0, 2.0)
        assert abs(result - math.sqrt(2)) < 1e-10

class TestRegulaFalsi:

    def test_sqrt2(self):
        result = nm.regula_falsi(lambda x: x ** 2 - 2, 1, 2)
        assert abs(result - math.sqrt(2)) < 1e-10

class TestFixedPoint:

    def test_cos_fixed_point(self):
        result = nm.fixed_point_iteration(math.cos, 1.0)
        assert abs(result - 0.7390851332) < 1e-6


# ===================================================================
# ODE Solvers
# ===================================================================

class TestEulerMethodV2:

    def test_exponential_growth(self):
        result = nm.euler_method(lambda t, y: y, 1.0, 0, 1, 10000)
        assert abs(result[-1][1] - math.e) < 0.01

class TestRungeKutta2:

    def test_exponential_growth(self):
        result = nm.runge_kutta_2(lambda t, y: y, 1.0, 0, 1, 1000)
        assert abs(result[-1][1] - math.e) < 0.001

class TestRungeKutta4:

    def test_exponential_growth(self):
        result = nm.runge_kutta_4(lambda t, y: y, 1.0, 0, 1, 100)
        assert abs(result[-1][1] - math.e) < 1e-8

    def test_linear_ode(self):
        # y' = 1, y(0) = 0 → y(1) = 1
        result = nm.runge_kutta_4(lambda t, y: 1.0, 0.0, 0, 1, 100)
        assert abs(result[-1][1] - 1.0) < 1e-10

class TestAdaptiveRK45:

    def test_exponential_growth(self):
        result = nm.adaptive_rk45(lambda t, y: y, 1.0, 0, 1)
        assert abs(result[-1][1] - math.e) < 1e-6

class TestODESystemRK4:

    def test_harmonic_oscillator(self):
        # y'' + y = 0 as [y, y']; y(0)=0, y'(0)=1 → y = sin(t)
        result = nm.ode_system_rk4(
            lambda t, y: [y[1], -y[0]], [0.0, 1.0], 0, math.pi, 1000
        )
        assert abs(result[-1][1][0]) < 0.001  # sin(pi) ≈ 0
        assert abs(result[-1][1][1] - (-1.0)) < 0.001  # cos(pi) ≈ -1


# ===================================================================
# Parametric Curves
# ===================================================================
