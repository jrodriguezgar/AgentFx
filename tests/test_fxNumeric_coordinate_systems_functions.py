"""Tests for fxNumeric.coordinate_systems_functions."""

import math

from agentfx.fxNumeric import (
    bipolar_to_cartesian,
    cartesian_to_cylindrical,
    cartesian_to_parabolic_cylindrical,
    cylindrical_to_cartesian,
    elliptic_cylindrical_to_cartesian,
    oblate_spheroidal_to_cartesian,
    parabolic_cylindrical_to_cartesian,
    paraboloidal_to_cartesian,
    prolate_spheroidal_to_cartesian,
    toroidal_to_cartesian,
)


class TestCoordinateSystems:

    def test_cylindrical_roundtrip(self):
        rho, phi, z = cartesian_to_cylindrical(1, 1, 5)
        x, y, z2 = cylindrical_to_cartesian(rho, phi, z)
        assert abs(x - 1) < 1e-10
        assert abs(y - 1) < 1e-10
        assert abs(z2 - 5) < 1e-10

    def test_parabolic_cylindrical_roundtrip(self):
        x, y, z = parabolic_cylindrical_to_cartesian(2, 3, 7)
        u, v, z2 = cartesian_to_parabolic_cylindrical(x, y, z)
        assert abs(u - 2) < 1e-6
        assert abs(v - 3) < 1e-6
        assert abs(z2 - 7) < 1e-10

    def test_paraboloidal(self):
        x, y, z = paraboloidal_to_cartesian(1, 1, 0)
        assert isinstance(x, float)

    def test_elliptic_cylindrical(self):
        x, y, z = elliptic_cylindrical_to_cartesian(1, 0, 5, 2)
        # u=1, v=0 → x = a*cosh(1), y = 0
        assert abs(y) < 1e-10
        assert abs(z - 5) < 1e-10

    def test_prolate_spheroidal(self):
        x, y, z = prolate_spheroidal_to_cartesian(2, math.pi / 2, 0, 1)
        assert isinstance(x, float)

    def test_oblate_spheroidal(self):
        x, y, z = oblate_spheroidal_to_cartesian(2, math.pi / 2, 0, 1)
        assert isinstance(x, float)

    def test_bipolar(self):
        x, y = bipolar_to_cartesian(1, math.pi / 2, 1)
        assert isinstance(x, float)

    def test_toroidal(self):
        x, y, z = toroidal_to_cartesian(1, math.pi / 4, 0, 2)
        assert isinstance(x, float)


# ===================================================================
# Mechanics (centroids, moments of inertia)
# ===================================================================
