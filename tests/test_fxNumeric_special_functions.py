"""Tests for fxNumeric.special_functions."""

import math

import pytest

from shortfx.fxNumeric import (
    abel_polynomial,
    anger_j,
    bell_number,
    catalan_number,
    central_binomial_coefficient,
    clausen_function,
    complementary_error_function,
    debye_function,
    dedekind_eta,
    digamma,
    dirichlet_integral,
    double_factorial,
    error_function,
    euler_reflection_formula,
    fibonacci_polynomial,
    gamma_duplication_formula,
    gaussian_integral,
    gegenbauer_polynomial,
    generalized_harmonic_number,
    harmonic_number,
    heaviside_step,
    hexagonal_number,
    inverse_error_function,
    jacobi_polynomial,
    jacobi_theta_1,
    jacobi_theta_2,
    jacobi_theta_3,
    jacobi_theta_4,
    kelvin_bei,
    kelvin_ber,
    lambert_w,
    lanczos_gamma,
    log_gamma,
    lucas_polynomial,
    mittag_leffler,
    partition_number,
    pentagonal_number,
    polygamma,
    ramp_function,
    reciprocal_gamma,
    rectangular_function,
    sinc_function,
    softplus_function,
    stirling_approximation,
    struve_h,
    touchard_polynomial,
    triangular_function,
    trigamma,
    wallis_product,
    weierstrass_p,
)
from shortfx.fxNumeric import special_functions as sf


class TestCatalanNumber:

    @pytest.mark.parametrize("n, expected", [
        (0, 1), (1, 1), (2, 2), (3, 5), (4, 14), (5, 42), (10, 16796),
    ])
    def test_values(self, n, expected):
        assert catalan_number(n) == expected

    def test_negative(self):
        with pytest.raises(ValueError):
            catalan_number(-1)

class TestPentagonalNumber:
    def test_known_values(self):
        assert pentagonal_number(0) == 0
        assert pentagonal_number(1) == 1
        assert pentagonal_number(2) == 5
        assert pentagonal_number(3) == 12
        assert pentagonal_number(4) == 22
        assert pentagonal_number(5) == 35

    def test_type_error(self):
        with pytest.raises(TypeError):
            pentagonal_number(1.5)

    def test_negative(self):
        with pytest.raises(ValueError):
            pentagonal_number(-1)

class TestBellNumber:
    def test_known_values(self):
        assert bell_number(0) == 1
        assert bell_number(1) == 1
        assert bell_number(2) == 2
        assert bell_number(3) == 5
        assert bell_number(4) == 15
        assert bell_number(5) == 52
        assert bell_number(6) == 203

    def test_type_error(self):
        with pytest.raises(TypeError):
            bell_number(1.5)

    def test_negative(self):
        with pytest.raises(ValueError):
            bell_number(-1)


# ---------------------------------------------------------------------------
# Date
# ---------------------------------------------------------------------------

class TestPartitionNumber:
    def test_known(self):
        assert partition_number(0) == 1
        assert partition_number(1) == 1
        assert partition_number(2) == 2
        assert partition_number(3) == 3
        assert partition_number(4) == 5
        assert partition_number(5) == 7
        assert partition_number(10) == 42

    def test_type_error(self):
        with pytest.raises(TypeError):
            partition_number(1.5)

    def test_negative(self):
        with pytest.raises(ValueError):
            partition_number(-1)


# ---------------------------------------------------------------------------
# Date
# ---------------------------------------------------------------------------

class TestBernsteinPolynomial:
    """Bernstein basis polynomial."""

    def test_bernstein_basic(self):
        from shortfx.fxNumeric.special_functions import bernstein_polynomial

        assert bernstein_polynomial(3, 1, 0.5) == 0.375

    def test_bernstein_boundary_zero(self):
        from shortfx.fxNumeric.special_functions import bernstein_polynomial

        assert bernstein_polynomial(5, 0, 0.0) == 1.0

    def test_bernstein_boundary_one(self):
        from shortfx.fxNumeric.special_functions import bernstein_polynomial

        assert bernstein_polynomial(5, 5, 1.0) == 1.0

    def test_bernstein_partition_of_unity(self):
        from shortfx.fxNumeric.special_functions import bernstein_polynomial

        n = 4
        t = 0.3
        total = sum(bernstein_polynomial(n, k, t) for k in range(n + 1))
        assert abs(total - 1.0) < 1e-10

    def test_bernstein_invalid_k(self):
        from shortfx.fxNumeric.special_functions import bernstein_polynomial

        with pytest.raises(ValueError):
            bernstein_polynomial(3, 5, 0.5)


# =====================================================================
# fxString — string_evaluations (validations)
# =====================================================================

class TestErrorFunction:
    def test_one(self):
        assert round(error_function(1.0), 4) == 0.8427

    def test_zero(self):
        assert error_function(0) == 0.0

    def test_negative(self):
        assert round(error_function(-1.0), 4) == -0.8427

    def test_type_error(self):
        with pytest.raises(TypeError):
            error_function("abc")

class TestComplementaryErrorFunction:
    def test_one(self):
        assert round(complementary_error_function(1.0), 4) == 0.1573

    def test_zero(self):
        assert complementary_error_function(0) == 1.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            complementary_error_function("abc")

class TestInverseErrorFunction:
    def test_basic(self):
        assert round(inverse_error_function(0.8427), 2) == 1.0

    def test_zero(self):
        assert inverse_error_function(0.0) == pytest.approx(0.0, abs=1e-10)

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            inverse_error_function(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            inverse_error_function("abc")

class TestLogGamma:
    def test_five(self):
        assert round(log_gamma(5.0), 4) == 3.1781

    def test_one(self):
        assert log_gamma(1.0) == pytest.approx(0.0, abs=1e-8)

    def test_negative(self):
        with pytest.raises(ValueError):
            log_gamma(-1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            log_gamma("abc")

class TestCatalanNumberV2:
    def test_five(self):
        assert catalan_number(5) == 42

    def test_zero(self):
        assert catalan_number(0) == 1

    def test_negative(self):
        with pytest.raises(ValueError):
            catalan_number(-1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            catalan_number(1.5)

class TestBellNumberV2:
    def test_five(self):
        assert bell_number(5) == 52

    def test_zero(self):
        assert bell_number(0) == 1

    def test_sequence(self):
        assert [bell_number(i) for i in range(6)] == [1, 1, 2, 5, 15, 52]

    def test_type_error(self):
        with pytest.raises(TypeError):
            bell_number(1.5)

class TestPartitionNumberV2:
    def test_ten(self):
        assert partition_number(10) == 42

    def test_zero(self):
        assert partition_number(0) == 1

    def test_five(self):
        assert partition_number(5) == 7

    def test_type_error(self):
        with pytest.raises(TypeError):
            partition_number(1.5)

class TestHarmonicNumber:
    def test_ten(self):
        assert round(harmonic_number(10), 4) == 2.9290

    def test_one(self):
        assert harmonic_number(1) == 1.0

    def test_zero(self):
        with pytest.raises(ValueError):
            harmonic_number(0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            harmonic_number(1.5)

class TestGeneralizedHarmonicNumber:
    def test_basic(self):
        assert round(generalized_harmonic_number(10, 2), 4) == 1.5498

    def test_order_one(self):
        assert round(generalized_harmonic_number(10, 1), 4) == 2.9290

    def test_type_error(self):
        with pytest.raises(TypeError):
            generalized_harmonic_number("abc", 2)

class TestSincFunction:
    def test_zero(self):
        assert sinc_function(0) == 1.0

    def test_pi(self):
        assert sinc_function(math.pi) == pytest.approx(0.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sinc_function("abc")

class TestClausenFunction:
    def test_basic(self):
        assert round(clausen_function(1.0), 4) == 1.0139

    def test_zero(self):
        assert clausen_function(0.0) == pytest.approx(0.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            clausen_function("abc")

class TestDebyeFunction:
    def test_basic(self):
        assert round(debye_function(3, 1.0), 4) == 0.6788

    def test_order_one(self):
        result = debye_function(1, 1.0)
        assert 0.0 < result < 1.0

    def test_invalid_n(self):
        with pytest.raises(ValueError):
            debye_function(0, 1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            debye_function(3, "abc")

class TestHeavisideStep:
    def test_positive(self):
        assert heaviside_step(5) == 1.0

    def test_zero(self):
        assert heaviside_step(0) == 0.5

    def test_negative(self):
        assert heaviside_step(-3) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            heaviside_step("abc")

class TestRectangularFunction:
    def test_inside(self):
        assert rectangular_function(0.3) == 1.0

    def test_edge(self):
        assert rectangular_function(0.5) == 0.5

    def test_outside(self):
        assert rectangular_function(1.0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            rectangular_function("abc")

class TestTriangularFunction:
    def test_basic(self):
        assert triangular_function(0.3) == 0.7

    def test_zero(self):
        assert triangular_function(0.0) == 1.0

    def test_outside(self):
        assert triangular_function(2.0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            triangular_function("abc")

class TestRampFunction:
    def test_positive(self):
        assert ramp_function(3.5) == 3.5

    def test_negative(self):
        assert ramp_function(-2.0) == 0.0

    def test_zero(self):
        assert ramp_function(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            ramp_function("abc")

class TestSoftplusFunction:
    def test_zero(self):
        assert round(softplus_function(0), 4) == 0.6931

    def test_large(self):
        assert softplus_function(800) == 800.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            softplus_function("abc")

class TestLambertW:
    def test_one(self):
        assert round(lambert_w(1.0), 4) == 0.5671

    def test_roundtrip(self):
        w = lambert_w(1.0)
        assert w * math.exp(w) == pytest.approx(1.0, rel=1e-8)

    def test_below_range(self):
        with pytest.raises(ValueError):
            lambert_w(-1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            lambert_w("abc")

class TestDoubleFactorial:
    def test_seven(self):
        assert double_factorial(7) == 105

    def test_six(self):
        assert double_factorial(6) == 48

    def test_zero(self):
        assert double_factorial(0) == 1

    def test_negative(self):
        with pytest.raises(ValueError):
            double_factorial(-1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            double_factorial(1.5)

class TestCentralBinomialCoefficient:
    def test_five(self):
        assert central_binomial_coefficient(5) == 252

    def test_zero(self):
        assert central_binomial_coefficient(0) == 1

    def test_type_error(self):
        with pytest.raises(TypeError):
            central_binomial_coefficient(1.5)

class TestPentagonalNumberV2:
    def test_five(self):
        assert pentagonal_number(5) == 35

    def test_zero(self):
        assert pentagonal_number(0) == 0

    def test_sequence(self):
        assert [pentagonal_number(i) for i in range(6)] == [0, 1, 5, 12, 22, 35]

class TestHexagonalNumber:
    def test_five(self):
        assert hexagonal_number(5) == 45

    def test_zero(self):
        assert hexagonal_number(0) == 0

    def test_sequence(self):
        assert [hexagonal_number(i) for i in range(6)] == [0, 1, 6, 15, 28, 45]

class TestFibonacciPolynomial:
    def test_at_one(self):
        assert fibonacci_polynomial(5, 1.0) == 5.0

    def test_zero_order(self):
        assert fibonacci_polynomial(0, 2.0) == 0.0

    def test_first_order(self):
        assert fibonacci_polynomial(1, 3.0) == 1.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            fibonacci_polynomial(5, "abc")

class TestLucasPolynomial:
    def test_at_one(self):
        assert lucas_polynomial(5, 1.0) == 11.0

    def test_zero_order(self):
        assert lucas_polynomial(0, 2.0) == 2.0

    def test_first_order(self):
        assert lucas_polynomial(1, 3.0) == 3.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            lucas_polynomial(5, "abc")

class TestTouchardPolynomial:
    def test_three(self):
        assert touchard_polynomial(3, 1.0) == 5.0

    def test_zero(self):
        assert touchard_polynomial(0, 5.0) == 1.0

    def test_bell_numbers(self):
        # T_n(1) = B_n (Bell numbers)
        expected_bells = [1, 1, 2, 5, 15, 52]
        for n, b in enumerate(expected_bells):
            assert touchard_polynomial(n, 1.0) == float(b)

class TestAbelPolynomial:
    def test_basic(self):
        assert abel_polynomial(3, 2.0) == 2.0

    def test_zero_order(self):
        assert abel_polynomial(0, 5.0) == 1.0

    def test_first_order(self):
        # p_1(x; 1) = x(x - 1)^0 = x
        assert abel_polynomial(1, 3.0) == 3.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            abel_polynomial(3, "abc")

class TestDoubleFactorialV2:

    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (5, 15),
        (6, 48),
        (7, 105),
    ])
    def test_double_factorial_valid(self, n: int, expected: int):
        assert double_factorial(n) == expected

    def test_double_factorial_negative_raises(self):

        with pytest.raises(ValueError):
            double_factorial(-1)


# ── Gamma ────────────────────────────────────────────────────────────────────

class TestLogGammaV2:

    def test_log_gamma_positive(self):
        # lgamma(5) = ln(24) ≈ 3.178
        assert log_gamma(5) == pytest.approx(math.lgamma(5))

    def test_log_gamma_non_positive_raises(self):

        with pytest.raises(ValueError):
            log_gamma(0)


# ── GCD / LCM ───────────────────────────────────────────────────────────────

class TestErrorFunctions:

    def test_erf_zero(self):
        assert error_function(0) == 0.0

    def test_erf_one(self):
        assert error_function(1) == pytest.approx(math.erf(1))

    def test_erfc_zero(self):
        assert complementary_error_function(0) == 1.0


# ── Constants ────────────────────────────────────────────────────────────────

class TestLegendrePolynomial:

    def test_p0(self):
        from shortfx.fxNumeric.special_functions import legendre_polynomial
        assert legendre_polynomial(0, 0.5) == 1.0

    def test_p1(self):
        from shortfx.fxNumeric.special_functions import legendre_polynomial
        assert legendre_polynomial(1, 0.5) == 0.5

    def test_p2(self):
        from shortfx.fxNumeric.special_functions import legendre_polynomial
        assert legendre_polynomial(2, 0.5) == pytest.approx(-0.125)

    def test_p3(self):
        from shortfx.fxNumeric.special_functions import legendre_polynomial
        assert legendre_polynomial(3, 0.0) == pytest.approx(0.0, abs=1e-10)

    def test_negative_n_raises(self):
        from shortfx.fxNumeric.special_functions import legendre_polynomial

        with pytest.raises(ValueError):
            legendre_polynomial(-1, 0.5)

class TestAssociatedLegendre:

    def test_p10(self):
        from shortfx.fxNumeric.special_functions import associated_legendre
        assert associated_legendre(1, 0, 0.5) == pytest.approx(0.5)

    def test_p11(self):
        from shortfx.fxNumeric.special_functions import associated_legendre
        assert associated_legendre(1, 1, 0.5) == pytest.approx(-math.sqrt(0.75))

    def test_m_greater_than_n_raises(self):
        from shortfx.fxNumeric.special_functions import associated_legendre

        with pytest.raises(ValueError):
            associated_legendre(1, 2, 0.5)

class TestHermitePolynomial:

    def test_h0(self):
        from shortfx.fxNumeric.special_functions import hermite_polynomial
        assert hermite_polynomial(0, 1.0) == 1.0

    def test_h1(self):
        from shortfx.fxNumeric.special_functions import hermite_polynomial
        assert hermite_polynomial(1, 2.0) == 4.0

    def test_h3(self):
        from shortfx.fxNumeric.special_functions import hermite_polynomial
        # H_3(2) = 8*8 - 12*2 = 40
        assert hermite_polynomial(3, 2.0) == pytest.approx(40.0)

class TestLaguerrePolynomial:

    def test_l0(self):
        from shortfx.fxNumeric.special_functions import laguerre_polynomial
        assert laguerre_polynomial(0, 1.0) == 1.0

    def test_l1(self):
        from shortfx.fxNumeric.special_functions import laguerre_polynomial
        assert laguerre_polynomial(1, 1.0) == pytest.approx(0.0)

    def test_l2(self):
        from shortfx.fxNumeric.special_functions import laguerre_polynomial
        # L_2(x) = (x^2 - 4x + 2)/2 => L_2(1) = -0.5
        assert laguerre_polynomial(2, 1.0) == pytest.approx(-0.5)

class TestChebyshevPolynomials:

    def test_t0(self):
        from shortfx.fxNumeric.special_functions import chebyshev_polynomial_first
        assert chebyshev_polynomial_first(0, 0.5) == 1.0

    def test_t2(self):
        from shortfx.fxNumeric.special_functions import chebyshev_polynomial_first
        # T_2(x) = 2x^2 - 1
        assert chebyshev_polynomial_first(2, 0.5) == pytest.approx(-0.5)

    def test_u0(self):
        from shortfx.fxNumeric.special_functions import chebyshev_polynomial_second
        assert chebyshev_polynomial_second(0, 0.5) == 1.0

    def test_u2(self):
        from shortfx.fxNumeric.special_functions import chebyshev_polynomial_second
        # U_2(x) = 4x^2 - 1
        assert chebyshev_polynomial_second(2, 0.5) == pytest.approx(0.0)

class TestBernoulliNumbers:

    def test_b0(self):
        from shortfx.fxNumeric.special_functions import bernoulli_number
        assert bernoulli_number(0) == pytest.approx(1.0)

    def test_b1(self):
        from shortfx.fxNumeric.special_functions import bernoulli_number
        assert bernoulli_number(1) == pytest.approx(-0.5)

    def test_b2(self):
        from shortfx.fxNumeric.special_functions import bernoulli_number
        assert bernoulli_number(2) == pytest.approx(1.0 / 6.0)

    def test_odd_zero(self):
        from shortfx.fxNumeric.special_functions import bernoulli_number
        assert bernoulli_number(3) == 0.0
        assert bernoulli_number(5) == 0.0

class TestEulerNumbers:

    def test_e0(self):
        from shortfx.fxNumeric.special_functions import euler_number
        assert euler_number(0) == 1

    def test_e2(self):
        from shortfx.fxNumeric.special_functions import euler_number
        assert euler_number(2) == -1

    def test_e4(self):
        from shortfx.fxNumeric.special_functions import euler_number
        assert euler_number(4) == 5

    def test_odd_zero(self):
        from shortfx.fxNumeric.special_functions import euler_number
        assert euler_number(1) == 0
        assert euler_number(3) == 0

class TestDigamma:

    def test_at_1(self):
        from shortfx.fxNumeric.special_functions import digamma
        # psi(1) = -gamma (Euler-Mascheroni constant)
        assert digamma(1.0) == pytest.approx(-0.5772156649, rel=1e-5)

    def test_at_2(self):
        from shortfx.fxNumeric.special_functions import digamma
        # psi(2) = 1 - gamma
        assert digamma(2.0) == pytest.approx(1.0 - 0.5772156649, rel=1e-5)

class TestRiemannZeta:

    def test_zeta_2(self):
        from shortfx.fxNumeric.special_functions import riemann_zeta
        assert riemann_zeta(2) == pytest.approx(math.pi ** 2 / 6, rel=1e-6)

    def test_zeta_4(self):
        from shortfx.fxNumeric.special_functions import riemann_zeta
        assert riemann_zeta(4) == pytest.approx(math.pi ** 4 / 90, rel=1e-5)

class TestEllipticIntegrals:

    def test_k_zero(self):
        from shortfx.fxNumeric.special_functions import elliptic_k
        assert elliptic_k(0) == pytest.approx(math.pi / 2)

    def test_e_zero(self):
        from shortfx.fxNumeric.special_functions import elliptic_e
        assert elliptic_e(0) == pytest.approx(math.pi / 2)

    def test_e_one(self):
        from shortfx.fxNumeric.special_functions import elliptic_e
        assert elliptic_e(1) == pytest.approx(1.0)

    def test_f_complete(self):
        from shortfx.fxNumeric.special_functions import elliptic_f, elliptic_k
        # F(pi/2, k) == K(k)
        assert elliptic_f(math.pi / 2, 0.5) == pytest.approx(elliptic_k(0.5), rel=1e-3)

class TestHypergeometric:

    def test_2f1_basic(self):
        from shortfx.fxNumeric.special_functions import hypergeometric_2f1
        # 2F1(1,1;2;0.5) = -ln(0.5)/0.5 = ln(2)/0.5? Actually = -ln(1-x)/x
        # 2F1(1,1;2;x) = -ln(1-x)/x
        assert hypergeometric_2f1(1, 1, 2, 0.5) == pytest.approx(
            -math.log(0.5) / 0.5, rel=1e-4
        )

    def test_1f1_exp(self):
        from shortfx.fxNumeric.special_functions import hypergeometric_1f1
        # 1F1(1;1;1) = e
        assert hypergeometric_1f1(1, 1, 1) == pytest.approx(math.e, rel=1e-6)

class TestAiryFunctions:

    def test_ai_zero(self):
        from shortfx.fxNumeric.special_functions import airy_ai
        assert airy_ai(0) == pytest.approx(0.355028, rel=1e-3)

    def test_bi_zero(self):
        from shortfx.fxNumeric.special_functions import airy_bi
        assert airy_bi(0) == pytest.approx(0.614927, rel=1e-3)

class TestSphericalBessel:

    def test_j0(self):
        from shortfx.fxNumeric.special_functions import spherical_bessel_j
        # j_0(x) = sin(x)/x
        assert spherical_bessel_j(0, 1.0) == pytest.approx(math.sin(1.0), rel=1e-10)

    def test_y0(self):
        from shortfx.fxNumeric.special_functions import spherical_bessel_y
        # y_0(x) = -cos(x)/x
        assert spherical_bessel_y(0, 1.0) == pytest.approx(-math.cos(1.0), rel=1e-10)

class TestSphericalHarmonic:

    def test_y00(self):
        from shortfx.fxNumeric.special_functions import spherical_harmonic_real
        # Y_0^0 = 1/sqrt(4pi)
        assert spherical_harmonic_real(0, 0, 0, 0) == pytest.approx(
            1.0 / math.sqrt(4 * math.pi), rel=1e-6
        )


# ---------------------------------------------------------------------------
# Series functions
# ---------------------------------------------------------------------------

class TestBesselJ:

    def test_j0_at_zero(self):
        assert sf.bessel_j(0, 0) == 1.0

    def test_j1_at_zero(self):
        assert sf.bessel_j(1, 0) == 0.0

    def test_j0_at_one(self):
        assert abs(sf.bessel_j(0, 1.0) - 0.7651976866) < 1e-4

    def test_j1_at_one(self):
        assert abs(sf.bessel_j(1, 1.0) - 0.4400505857) < 1e-4

    def test_negative_order_error(self):
        with pytest.raises(ValueError):
            sf.bessel_j(-1, 1.0)

class TestBesselY:

    def test_y0_at_one(self):
        assert abs(sf.bessel_y(0, 1.0) - 0.0883) < 0.01

    def test_negative_x_error(self):
        with pytest.raises(ValueError):
            sf.bessel_y(0, -1.0)

class TestModifiedBesselI:

    def test_i0_at_zero(self):
        assert sf.modified_bessel_i(0, 0) == 1.0

    def test_i0_at_one(self):
        assert abs(sf.modified_bessel_i(0, 1.0) - 1.2660658) < 1e-4

class TestModifiedBesselK:

    def test_k0_at_one(self):
        assert abs(sf.modified_bessel_k(0, 1.0) - 0.4210) < 0.01


# ===================================================================
# Special Integrals
# ===================================================================

class TestExponentialIntegral:

    def test_ei_at_one(self):
        assert abs(sf.exponential_integral_ei(1.0) - 1.8951) < 0.01

    def test_negative_x_error(self):
        with pytest.raises(ValueError):
            sf.exponential_integral_ei(-1.0)

class TestSineIntegral:

    def test_si_at_one(self):
        assert abs(sf.sine_integral(1.0) - 0.946083) < 1e-4

class TestCosineIntegral:

    def test_ci_at_one(self):
        assert abs(sf.cosine_integral(1.0) - 0.337404) < 1e-4

    def test_negative_x_error(self):
        with pytest.raises(ValueError):
            sf.cosine_integral(-1.0)

class TestFresnelS:

    def test_at_one(self):
        assert abs(sf.fresnel_s(1.0) - 0.4383) < 0.01

    def test_at_zero(self):
        assert sf.fresnel_s(0) == 0.0

class TestFresnelC:

    def test_at_one(self):
        assert abs(sf.fresnel_c(1.0) - 0.7799) < 0.01

class TestDawsonFunction:

    def test_at_one(self):
        assert abs(sf.dawson_function(1.0) - 0.5381) < 0.01

class TestPolylogarithm:

    def test_li2_at_half(self):
        assert abs(sf.polylogarithm(2, 0.5) - 0.582241) < 1e-4

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            sf.polylogarithm(2, 2.0)

class TestDilogarithm:

    def test_at_one(self):
        # Li_2(1) = π²/6 (series converges slowly at z=1)
        assert abs(sf.dilogarithm(1.0) - math.pi ** 2 / 6) < 0.01

class TestUpperIncompleteGamma:

    def test_gamma_1_1(self):
        # Γ(1, 1) = e^(-1)
        assert abs(sf.upper_incomplete_gamma(1, 1) - math.exp(-1)) < 1e-4

class TestHurwitzZeta:

    def test_zeta_2_1(self):
        # ζ(2, 1) = π²/6
        assert abs(sf.hurwitz_zeta(2, 1) - math.pi ** 2 / 6) < 0.01


# ===================================================================
# Combinatorial Special Values
# ===================================================================

class TestRisingFactorial:

    def test_basic(self):
        assert sf.rising_factorial(3, 4) == 360.0  # 3*4*5*6

    def test_one_base(self):
        assert sf.rising_factorial(1, 5) == 120.0  # 5!

    def test_zero_n(self):
        assert sf.rising_factorial(5, 0) == 1.0

class TestFallingFactorial:

    def test_basic(self):
        assert sf.falling_factorial(5, 3) == 60.0  # 5*4*3

    def test_factorial(self):
        assert sf.falling_factorial(5, 5) == 120.0

    def test_zero_n(self):
        assert sf.falling_factorial(5, 0) == 1.0

class TestSubfactorial:

    def test_values(self):
        assert sf.subfactorial(0) == 1
        assert sf.subfactorial(1) == 0
        assert sf.subfactorial(2) == 1
        assert sf.subfactorial(3) == 2
        assert sf.subfactorial(4) == 9
        assert sf.subfactorial(5) == 44

class TestStirlingFirst:

    def test_basic(self):
        assert sf.stirling_number_first(4, 2) == 11
        assert sf.stirling_number_first(3, 1) == 2

    def test_boundary(self):
        assert sf.stirling_number_first(0, 0) == 1
        assert sf.stirling_number_first(5, 0) == 0
        assert sf.stirling_number_first(3, 5) == 0

class TestMultinomialCoefficient:

    def test_basic(self):
        assert sf.multinomial_coefficient(6, 2, 2, 2) == 90
        assert sf.multinomial_coefficient(4, 2, 1, 1) == 12

    def test_invalid_sum(self):
        with pytest.raises(ValueError):
            sf.multinomial_coefficient(5, 2, 2)

class TestSpecialExtensions:

    def test_stirling_small(self):
        # 10! = 3628800; Stirling ≈ 3598695
        approx = stirling_approximation(10)
        assert abs(approx - 3628800) / 3628800 < 0.01

    def test_stirling_zero(self):
        assert stirling_approximation(0) == 1.0

    def test_stirling_invalid(self):
        with pytest.raises(ValueError):
            stirling_approximation(-1)

    def test_wallis(self):
        val = wallis_product(10000)
        assert abs(val - math.pi / 2) < 0.001

    def test_gaussian_integral(self):
        assert abs(gaussian_integral() - math.sqrt(math.pi)) < 1e-15

    def test_dirichlet_integral(self):
        assert abs(dirichlet_integral() - math.pi / 2) < 1e-15

    def test_lanczos_gamma_5(self):
        # Gamma(5) = 4! = 24
        assert abs(lanczos_gamma(5.0) - 24.0) < 1e-6

    def test_lanczos_gamma_half(self):
        # Gamma(0.5) = sqrt(pi)
        assert abs(lanczos_gamma(0.5) - math.sqrt(math.pi)) < 1e-6

    def test_lanczos_invalid(self):
        with pytest.raises(ValueError):
            lanczos_gamma(0)

    def test_digamma_1(self):
        # psi(1) = -euler_gamma ≈ -0.5772
        assert abs(digamma(1) - (-0.5772156649)) < 1e-4

    def test_digamma_invalid(self):
        with pytest.raises(ValueError):
            digamma(0)


# ===================================================================
# Arithmetic / matrix extensions
# ===================================================================

class TestThetaFunctions:

    def test_theta3_at_zero(self):
        # θ₃(0, 0.1) = 1 + 2*0.1 + 2*0.1^4 + ... ≈ 1.2
        val = jacobi_theta_3(0, 0.1)
        assert abs(val - 1.2) < 0.01

    def test_theta1_odd(self):
        # θ₁ is odd in z: θ₁(0, q) = 0
        assert abs(jacobi_theta_1(0, 0.1)) < 1e-10

    def test_theta2_at_zero(self):
        val = jacobi_theta_2(0, 0.1)
        assert val > 0

    def test_theta4_at_zero(self):
        # θ₄(0, q) = 1 - 2q + 2q^4 - ...
        val = jacobi_theta_4(0, 0.1)
        assert abs(val - 0.8) < 0.01

    def test_invalid_q(self):
        with pytest.raises(ValueError):
            jacobi_theta_3(0, 1.0)

class TestDedekindEta:

    def test_eta_1(self):
        val = dedekind_eta(1)
        assert abs(val - 0.7682254) < 0.001

    def test_eta_positive(self):
        assert dedekind_eta(2) > 0

    def test_invalid(self):
        with pytest.raises(ValueError):
            dedekind_eta(0)

class TestWeierstrass:

    def test_basic(self):
        val = weierstrass_p(0.5, 1.0, 1.0, 5)
        assert isinstance(val, float)

    def test_lattice_point(self):
        with pytest.raises(ValueError):
            weierstrass_p(0, 1.0, 1.0)

class TestTrigammaPolygamma:

    def test_trigamma_1(self):
        # ψ₁(1) = π²/6
        assert abs(trigamma(1) - math.pi ** 2 / 6) < 1e-4

    def test_trigamma_positive(self):
        assert trigamma(2) > 0

    def test_polygamma_0(self):
        # ψ^(0)(1) = digamma(1) ≈ -0.5772
        assert abs(polygamma(0, 1) - (-0.5772156649)) < 1e-3

    def test_polygamma_1(self):
        # Should equal trigamma
        assert abs(polygamma(1, 1) - trigamma(1)) < 1e-3


# ===================================================================
# Transform extensions
# ===================================================================

class TestGegenbauer:
    def test_c0(self):
        assert gegenbauer_polynomial(0, 1.0, 0.5) == 1.0

    def test_c1(self):
        assert gegenbauer_polynomial(1, 1.0, 0.5) == 1.0

    def test_c2_alpha1(self):
        # C_2^1(0.5) = U_2(0.5) = 4(0.25)-1 = 0
        assert round(gegenbauer_polynomial(2, 1.0, 0.5), 10) == 0.0

    def test_c2_alpha_half(self):
        # C_2^0.5(x) = P_2(x) = (3x^2-1)/2 at x=0.5 → -0.125
        assert round(gegenbauer_polynomial(2, 0.5, 0.5), 6) == -0.125

class TestJacobiPolynomial:
    def test_p0(self):
        assert jacobi_polynomial(0, 1, 1, 0.5) == 1.0

    def test_p2_00(self):
        # P_2^(0,0)(x) = Legendre P_2(x) = (3x^2-1)/2
        # at x=0.5: (0.75-1)/2 = -0.125
        assert round(jacobi_polynomial(2, 0, 0, 0.5), 6) == -0.125

class TestStruve:
    def test_h0_at_1(self):
        assert round(struve_h(0, 1.0), 4) == 0.5687

    def test_h0_at_0(self):
        assert round(struve_h(0, 0.0), 6) == 0.0

class TestKelvin:
    def test_ber_at_0(self):
        assert round(kelvin_ber(0.0), 6) == 1.0

    def test_bei_at_0(self):
        assert round(kelvin_bei(0.0), 6) == 0.0

    def test_ber_at_1(self):
        assert round(kelvin_ber(1.0), 4) == 0.9844

    def test_bei_at_1(self):
        assert round(kelvin_bei(1.0), 3) == 0.250

class TestAnger:
    def test_j0_at_0(self):
        assert round(anger_j(0, 0.0), 6) == 1.0

class TestMittagLeffler:
    def test_exp(self):
        # E_{1,1}(1) = e
        assert round(mittag_leffler(1.0, 1.0, 1.0), 4) == round(math.e, 4)

class TestReciprocalGamma:
    def test_at_1(self):
        assert reciprocal_gamma(1.0) == 1.0

    def test_at_0(self):
        assert reciprocal_gamma(0.0) == 0.0

    def test_at_neg_int(self):
        assert reciprocal_gamma(-1.0) == 0.0

class TestEulerReflection:
    def test_half(self):
        # Γ(1/2) = √π
        assert round(euler_reflection_formula(0.5), 6) == round(math.sqrt(math.pi), 6)

class TestGammaDuplication:
    def test_at_1(self):
        # Γ(1.5) = √π / 2
        assert round(gamma_duplication_formula(1.0), 6) == round(math.sqrt(math.pi) / 2.0, 6)


# ===================================================================
# Curves extensions
# ===================================================================
