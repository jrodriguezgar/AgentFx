"""Tests for fxNumeric.conformal_functions."""

import math

import pytest

from agentfx.fxNumeric import (
    cayley_transform,
    exponential_map,
    inverse_cayley_transform,
    inverse_joukowski,
    inversion_map,
    joukowski_transform,
    koebe_function,
    log_map,
    mobius_transform,
    power_map,
    schwarz_christoffel_half_plane_to_rectangle,
)


class TestConformalMappings:

    def test_mobius_identity(self):
        # Identity: a=d=(1,0), b=c=(0,0) → w = z
        w = mobius_transform((3, 4), (1, 0), (0, 0), (0, 0), (1, 0))
        assert abs(w[0] - 3) < 1e-10
        assert abs(w[1] - 4) < 1e-10

    def test_joukowski_real(self):
        # z = 2 → w = 2 + 0.5 = 2.5
        assert joukowski_transform((2, 0)) == (2.5, 0.0)

    def test_joukowski_zero(self):
        with pytest.raises(ValueError):
            joukowski_transform((0, 0))

    def test_inverse_joukowski(self):
        z1, z2 = inverse_joukowski((2.5, 0))
        # One should be 2, the other 0.5
        values = sorted([z1[0], z2[0]])
        assert abs(values[0] - 0.5) < 1e-4
        assert abs(values[1] - 2.0) < 1e-4

    def test_power_map_square(self):
        # i^2 = -1
        re, im = power_map((0, 1), 2)
        assert abs(re - (-1)) < 1e-10
        assert abs(im) < 1e-10

    def test_exponential_map_pi_i(self):
        # e^(i*pi) = -1
        re, im = exponential_map((0, math.pi))
        assert abs(re - (-1)) < 1e-10
        assert abs(im) < 1e-10

    def test_log_map_e(self):
        re, im = log_map((math.e, 0))
        assert abs(re - 1) < 1e-10
        assert abs(im) < 1e-10

    def test_inversion_map(self):
        assert inversion_map((0, 1)) == (0.0, -1.0)

    def test_cayley_roundtrip(self):
        z = (1, 2)
        w = cayley_transform(z)
        z_back = inverse_cayley_transform(w)
        assert abs(z_back[0] - z[0]) < 1e-10
        assert abs(z_back[1] - z[1]) < 1e-10

    def test_koebe_at_half(self):
        re, im = koebe_function((0.5, 0))
        assert abs(re - 2.0) < 1e-4
        assert abs(im) < 1e-10

    def test_schwarz_christoffel(self):
        re, im = schwarz_christoffel_half_plane_to_rectangle((0.5, 0), 0.5)
        assert isinstance(re, float)


# ===================================================================
# Arithmetic extensions (Cholesky, QR, matrix power, adjugate, solve)
# ===================================================================
