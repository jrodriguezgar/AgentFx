"""Tests for fxNumeric.transform_functions."""

import math

import pytest

from shortfx.fxNumeric import (
    abel_transform_numerical,
    discrete_cosine_transform,
    discrete_sine_transform,
    hartley_transform,
    inverse_discrete_cosine_transform,
    inverse_hartley_transform,
    mellin_transform_numerical,
)
from shortfx.fxNumeric.statistics_functions import auto_correlation


class TestAutoCorrelation:

    def test_lag_zero(self):
        assert auto_correlation([1, 2, 3], 0) == 1.0

    def test_linear_series(self):
        result = auto_correlation([1, 2, 3, 4, 5, 6, 7], 1)
        assert result == pytest.approx(0.571429, rel=1e-3)

    def test_invalid_lag(self):
        with pytest.raises(ValueError):
            auto_correlation([1, 2, 3], 3)

class TestDFT:

    def test_constant_signal(self):
        from shortfx.fxNumeric.transform_functions import dft
        result = dft([1, 1, 1, 1])
        assert result[0][0] == pytest.approx(4.0)

        for k in range(1, 4):
            assert abs(result[k][0]) < 1e-10

    def test_roundtrip(self):
        from shortfx.fxNumeric.transform_functions import dft, idft
        signal = [1, 2, 3, 4]
        recovered = idft(dft(signal))
        assert recovered == pytest.approx(signal, abs=1e-10)

class TestLaplaceTransform:

    def test_unit_step(self):
        from shortfx.fxNumeric.transform_functions import laplace_transform_numerical
        # L{1} = 1/s
        result = laplace_transform_numerical(lambda t: 1, 1.0)
        assert result == pytest.approx(1.0, rel=0.05)

    def test_inverse(self):
        from shortfx.fxNumeric.transform_functions import inverse_laplace_gaver_stehfest
        # L^{-1}{1/s} = 1
        result = inverse_laplace_gaver_stehfest(lambda s: 1 / s, 1.0)
        assert result == pytest.approx(1.0, rel=0.01)

class TestConvolution:

    def test_basic(self):
        from shortfx.fxNumeric.transform_functions import convolution
        result = convolution([1, 2, 3], [1, 1])
        assert result == pytest.approx([1, 3, 5, 3])

class TestCrossCorrelation:

    def test_autocorrelation_peak(self):
        from shortfx.fxNumeric.transform_functions import auto_correlation
        signal = [1, 0, 1]
        result = auto_correlation(signal)
        # Peak at center
        assert result[2] == pytest.approx(2.0)

class TestZTransform:

    def test_basic(self):
        from shortfx.fxNumeric.transform_functions import z_transform_eval
        # x = [1, 1, 1], z = 2: X(z) = 1 + z^{-1} + z^{-2} = 1 + 0.5 + 0.25
        re, im = z_transform_eval([1, 1, 1], 2.0, 0.0)
        assert re == pytest.approx(1.75)
        assert abs(im) < 1e-10


# ---------------------------------------------------------------------------
# Trig additions
# ---------------------------------------------------------------------------

class TestMellinTransform:

    def test_exp_s2(self):
        # M{e^(-x)}(2) = Gamma(2) = 1! = 1
        val = mellin_transform_numerical(lambda x: math.exp(-x), 2)
        assert abs(val - 1.0) < 0.1

    def test_exp_s1(self):
        # M{e^(-x)}(1) = Gamma(1) = 1
        val = mellin_transform_numerical(lambda x: math.exp(-x), 1)
        assert abs(val - 1.0) < 0.1

class TestDCT:

    def test_constant_signal(self):
        dct = discrete_cosine_transform([1, 1, 1, 1])
        assert abs(dct[0] - 4.0) < 1e-10
        # All other coefficients should be ~0
        for k in range(1, 4):
            assert abs(dct[k]) < 1e-10

    def test_roundtrip(self):
        signal = [1, 2, 3, 4]
        dct = discrete_cosine_transform(signal)
        recovered = inverse_discrete_cosine_transform(dct)

        for i in range(4):
            assert abs(recovered[i] - signal[i]) < 1e-8

class TestDST:

    def test_basic(self):
        dst = discrete_sine_transform([1, 1, 1])
        assert len(dst) == 3
        assert dst[0] > 0


# ===================================================================
# Vector analysis extensions
# ===================================================================

class TestHartley:
    def test_delta(self):
        dht = hartley_transform([1, 0, 0, 0])
        assert [round(v, 4) for v in dht] == [1.0, 1.0, 1.0, 1.0]

    def test_roundtrip(self):
        original = [1, 2, 3, 4]
        dht = hartley_transform(original)
        recovered = inverse_hartley_transform(dht)
        assert [round(v, 4) for v in recovered] == [1.0, 2.0, 3.0, 4.0]

class TestAbel:
    def test_gaussian(self):
        # Abel transform of exp(-r^2) at y=0 should be √π ≈ 1.7725
        result = abel_transform_numerical(lambda r: math.exp(-r * r), 0.0)
        assert round(result, 2) == 1.77
