"""Tests for fxNumeric.series_functions."""

import math

import pytest

from agentfx.fxNumeric import (
    abel_sum,
    bbp_pi_digit,
    cesaro_sum,
    chudnovsky_pi,
    convergent_sequence,
    euler_maclaurin_sum,
    gregory_leibniz_pi,
    madhava_pi,
    nilakantha_pi,
    ramanujan_pi,
    taylor_atan,
    taylor_atanh,
    taylor_cosh,
    taylor_exp,
    taylor_log1p,
    taylor_sinh,
    vieta_pi,
    wallis_pi,
    zeta_even,
)


class TestTaylorAtan:
    def test_one(self):
        assert abs(taylor_atan(1.0) - math.pi / 4) < 0.01

    def test_zero(self):
        assert taylor_atan(0) == pytest.approx(0.0, abs=1e-10)

    def test_large(self):
        # arctan(10) should be close to π/2
        assert abs(taylor_atan(10.0) - math.pi / 2) < 0.1

    def test_type_error(self):
        with pytest.raises(TypeError):
            taylor_atan("abc")

class TestTaylorSinh:
    def test_one(self):
        assert round(taylor_sinh(1.0), 4) == 1.1752

    def test_zero(self):
        assert taylor_sinh(0) == pytest.approx(0.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            taylor_sinh("abc")

class TestTaylorCosh:
    def test_one(self):
        assert round(taylor_cosh(1.0), 4) == 1.5431

    def test_zero(self):
        assert taylor_cosh(0) == pytest.approx(1.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            taylor_cosh("abc")

class TestTaylorAtanh:
    def test_half(self):
        assert round(taylor_atanh(0.5), 4) == 0.5493

    def test_zero(self):
        assert taylor_atanh(0) == pytest.approx(0.0, abs=1e-10)

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            taylor_atanh(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            taylor_atanh("abc")

class TestEulerMaclaurinSum:
    def test_harmonic(self):
        result = euler_maclaurin_sum(lambda k: 1 / k, 1, 100)
        # Trapezoidal approximation (no correction terms)
        assert 4.0 < result < 6.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            euler_maclaurin_sum(lambda k: k, 1.5, 10)

class TestWallisPi:
    def test_convergence(self):
        assert round(wallis_pi(10000), 4) == 3.1415

    def test_type_error(self):
        with pytest.raises(TypeError):
            wallis_pi(1.5)

class TestVietaPi:
    def test_convergence(self):
        assert round(vieta_pi(20), 4) == 3.1416

    def test_type_error(self):
        with pytest.raises(TypeError):
            vieta_pi(1.5)

class TestChudnovskyPi:
    def test_convergence(self):
        assert round(chudnovsky_pi(2), 10) == 3.1415926536

    def test_type_error(self):
        with pytest.raises(TypeError):
            chudnovsky_pi(1.5)

class TestNilakanthaPi:
    def test_convergence(self):
        assert round(nilakantha_pi(100), 4) == 3.1416

    def test_type_error(self):
        with pytest.raises(TypeError):
            nilakantha_pi(1.5)

class TestTaylorLog1p:
    def test_half(self):
        assert round(taylor_log1p(0.5), 4) == 0.4055

    def test_zero(self):
        assert taylor_log1p(0.0) == pytest.approx(0.0, abs=1e-10)

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            taylor_log1p(-1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            taylor_log1p("abc")

class TestTaylorExp:
    def test_one(self):
        assert round(taylor_exp(1.0), 4) == 2.7183

    def test_zero(self):
        assert taylor_exp(0.0) == pytest.approx(1.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            taylor_exp("abc")

class TestRamanujanPi:
    def test_convergence(self):
        assert round(ramanujan_pi(2), 10) == 3.1415926536

    def test_type_error(self):
        with pytest.raises(TypeError):
            ramanujan_pi(1.5)

class TestBbpPiDigit:
    def test_convergence(self):
        assert round(bbp_pi_digit(10), 10) == 3.1415926536

    def test_zero(self):
        result = bbp_pi_digit(0)
        assert abs(result - math.pi) < 0.2

class TestGregoryLeibnizPi:
    def test_convergence(self):
        assert round(gregory_leibniz_pi(10000), 3) == 3.141

    def test_type_error(self):
        with pytest.raises(TypeError):
            gregory_leibniz_pi(1.5)

class TestMadhavaPi:
    def test_convergence(self):
        assert round(madhava_pi(20), 10) == 3.1415926536

    def test_type_error(self):
        with pytest.raises(TypeError):
            madhava_pi(1.5)

class TestZetaEven:
    def test_zeta_2(self):
        assert round(zeta_even(1), 4) == 1.6449

    def test_zeta_4(self):
        expected = math.pi ** 4 / 90.0
        assert abs(zeta_even(2) - expected) < 1e-8

    def test_type_error(self):
        with pytest.raises(TypeError):
            zeta_even(1.5)

class TestConvergentSequence:
    def test_sqrt2(self):
        seq = convergent_sequence(lambda x: (x + 2 / x) / 2, 1.0, 10)
        assert round(seq[-1], 4) == 1.4142

    def test_length(self):
        seq = convergent_sequence(lambda x: x / 2, 1.0, 5)
        assert len(seq) == 6  # initial + 5 iterations

    def test_type_error(self):
        with pytest.raises(TypeError):
            convergent_sequence(lambda x: x, "abc", 5)

class TestCesaroSum:
    def test_alternating(self):
        assert cesaro_sum([1, -1, 1, -1, 1, -1]) == 0.5

    def test_single(self):
        assert cesaro_sum([5.0]) == 5.0

    def test_empty(self):
        with pytest.raises(ValueError):
            cesaro_sum([])

class TestAbelSum:
    def test_alternating(self):
        assert round(abel_sum([1, -1, 1, -1, 1, -1], 0.5), 4) == 0.6562

    def test_empty(self):
        with pytest.raises(ValueError):
            abel_sum([], 0.5)

    def test_range(self):
        with pytest.raises(ValueError):
            abel_sum([1], 1.0)

class TestArithmeticSeries:

    def test_basic(self):
        from agentfx.fxNumeric.series_functions import arithmetic_series_sum
        # 1 + 3 + 5 + 7 + 9 = 25
        assert arithmetic_series_sum(1, 2, 5) == 25.0

    def test_single_term(self):
        from agentfx.fxNumeric.series_functions import arithmetic_series_sum
        assert arithmetic_series_sum(5, 3, 1) == 5.0

class TestGeometricSeries:

    def test_finite(self):
        from agentfx.fxNumeric.series_functions import geometric_series_sum
        # 1 + 0.5 + 0.25 + ... (10 terms)
        assert geometric_series_sum(1, 0.5, 10) == pytest.approx(1.998046875)

    def test_infinite(self):
        from agentfx.fxNumeric.series_functions import geometric_series_infinite
        assert geometric_series_infinite(1, 0.5) == pytest.approx(2.0)

    def test_r_equal_1(self):
        from agentfx.fxNumeric.series_functions import geometric_series_sum
        assert geometric_series_sum(3, 1, 5) == 15.0

class TestHarmonicSeries:

    def test_h10(self):
        from agentfx.fxNumeric.series_functions import harmonic_series_partial
        assert harmonic_series_partial(10) == pytest.approx(2.928968, rel=1e-4)

    def test_generalized(self):
        from agentfx.fxNumeric.series_functions import generalized_harmonic
        assert generalized_harmonic(10, 2) == pytest.approx(1.549768, rel=1e-4)

class TestTaylorSeries:

    def test_exp(self):
        from agentfx.fxNumeric.series_functions import taylor_exp
        assert taylor_exp(1.0) == pytest.approx(math.e, rel=1e-10)

    def test_sin(self):
        from agentfx.fxNumeric.series_functions import taylor_sin
        assert taylor_sin(math.pi / 2) == pytest.approx(1.0, rel=1e-10)

    def test_cos(self):
        from agentfx.fxNumeric.series_functions import taylor_cos
        assert taylor_cos(0) == pytest.approx(1.0)

    def test_ln1p(self):
        from agentfx.fxNumeric.series_functions import taylor_ln1p
        assert taylor_ln1p(0.5, 50) == pytest.approx(math.log(1.5), rel=1e-6)

    def test_atan(self):
        from agentfx.fxNumeric.series_functions import taylor_atan
        assert taylor_atan(1.0, 500) == pytest.approx(math.pi / 4, rel=1e-2)

    def test_sinh(self):
        from agentfx.fxNumeric.series_functions import taylor_sinh
        assert taylor_sinh(1.0) == pytest.approx(math.sinh(1.0), rel=1e-10)

    def test_cosh(self):
        from agentfx.fxNumeric.series_functions import taylor_cosh
        assert taylor_cosh(1.0) == pytest.approx(math.cosh(1.0), rel=1e-10)

class TestBinomialSeries:

    def test_sqrt(self):
        from agentfx.fxNumeric.series_functions import binomial_series
        # (1+0.5)^0.5 = sqrt(1.5)
        assert binomial_series(0.5, 0.5, 30) == pytest.approx(math.sqrt(1.5), rel=1e-6)

class TestFourierCoefficients:

    def test_sin_fundamental(self):
        from agentfx.fxNumeric.series_functions import fourier_coefficients
        a, b = fourier_coefficients(math.sin, 2 * math.pi, 3, 2000)
        assert b[1] == pytest.approx(1.0, rel=1e-2)
        assert abs(a[1]) < 0.05

class TestLeibnizBasel:

    def test_leibniz(self):
        from agentfx.fxNumeric.series_functions import leibniz_pi
        assert leibniz_pi(10000) * 4 == pytest.approx(math.pi, rel=1e-3)

    def test_basel(self):
        from agentfx.fxNumeric.series_functions import basel_series
        assert basel_series(10000) == pytest.approx(math.pi ** 2 / 6, rel=1e-3)


# ---------------------------------------------------------------------------
# Geometry functions
# ---------------------------------------------------------------------------
