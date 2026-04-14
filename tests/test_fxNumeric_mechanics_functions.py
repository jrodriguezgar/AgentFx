"""Tests for fxNumeric.mechanics_functions."""

import math

import pytest

from formulite.fxNumeric import (
    centroid_circular_sector,
    centroid_cone,
    centroid_hemisphere,
    centroid_polygon,
    centroid_semicircle,
    centroid_triangle,
    mass_moment_cone,
    mass_moment_cylinder,
    mass_moment_cylinder_transverse,
    mass_moment_disk,
    mass_moment_hollow_sphere,
    mass_moment_rod,
    mass_moment_sphere,
    moment_of_inertia_annulus,
    moment_of_inertia_circle,
    moment_of_inertia_ellipse,
    moment_of_inertia_rectangle,
    moment_of_inertia_semicircle,
    moment_of_inertia_triangle,
    moment_of_inertia_triangle_centroidal,
    parallel_axis_theorem,
    polar_moment_of_inertia,
    radius_of_gyration,
    section_modulus,
)


class TestCentroids:

    def test_centroid_triangle(self):
        cx, cy = centroid_triangle((0, 0), (6, 0), (0, 6))
        assert abs(cx - 2) < 1e-10
        assert abs(cy - 2) < 1e-10

    def test_centroid_polygon_square(self):
        cx, cy = centroid_polygon([(0, 0), (4, 0), (4, 4), (0, 4)])
        assert abs(cx - 2) < 1e-10
        assert abs(cy - 2) < 1e-10

    def test_centroid_polygon_too_few_vertices(self):
        with pytest.raises(ValueError):
            centroid_polygon([(0, 0), (1, 0)])

    def test_centroid_semicircle(self):
        _, y = centroid_semicircle(3)
        assert abs(y - 4 / math.pi) < 1e-6

    def test_centroid_circular_sector(self):
        x, _ = centroid_circular_sector(3, math.pi / 2)
        expected = 2 * 3 * math.sin(math.pi / 2) / (3 * math.pi / 2)
        assert abs(x - expected) < 1e-10

    def test_centroid_cone(self):
        assert centroid_cone(12) == 3.0

    def test_centroid_hemisphere(self):
        assert centroid_hemisphere(4) == 1.5

class TestMomentsOfInertia:

    def test_rectangle(self):
        ix, iy = moment_of_inertia_rectangle(4, 6)
        assert abs(ix - 72) < 1e-10
        assert abs(iy - 32) < 1e-10

    def test_circle(self):
        assert abs(moment_of_inertia_circle(2) - math.pi * 16 / 4) < 1e-10

    def test_annulus(self):
        val = moment_of_inertia_annulus(3, 2)
        expected = math.pi * (81 - 16) / 4
        assert abs(val - expected) < 1e-6

    def test_annulus_invalid(self):
        with pytest.raises(ValueError):
            moment_of_inertia_annulus(2, 3)

    def test_triangle(self):
        assert abs(moment_of_inertia_triangle(6, 4) - 32) < 1e-10

    def test_triangle_centroidal(self):
        assert abs(moment_of_inertia_triangle_centroidal(6, 4) - 32 / 3) < 1e-6

    def test_semicircle(self):
        assert abs(moment_of_inertia_semicircle(2) - math.pi * 16 / 8) < 1e-10

    def test_ellipse(self):
        ix, iy = moment_of_inertia_ellipse(3, 2)
        assert abs(ix - math.pi * 3 * 8 / 4) < 1e-6
        assert abs(iy - math.pi * 27 * 2 / 4) < 1e-6

class TestMassMoments:

    def test_sphere(self):
        assert mass_moment_sphere(10, 2) == 16.0

    def test_hollow_sphere(self):
        assert abs(mass_moment_hollow_sphere(10, 2) - 80 / 3) < 1e-6

    def test_cylinder(self):
        assert mass_moment_cylinder(10, 2) == 20.0

    def test_cylinder_transverse(self):
        # m(3r² + h²)/12 = 10*(12+36)/12 = 10*48/12 = 40
        assert mass_moment_cylinder_transverse(10, 2, 6) == 40.0

    def test_rod(self):
        assert mass_moment_rod(6, 4) == 8.0

    def test_disk(self):
        assert mass_moment_disk(10, 3) == 45.0

    def test_cone(self):
        assert mass_moment_cone(10, 2) == 12.0

class TestMechanicsTheorems:

    def test_parallel_axis(self):
        assert parallel_axis_theorem(8, 6, 3) == 62.0

    def test_radius_of_gyration(self):
        assert radius_of_gyration(48, 12) == 2.0

    def test_section_modulus(self):
        assert section_modulus(72, 3) == 24.0

    def test_polar_moment(self):
        assert polar_moment_of_inertia(72, 32) == 104


# ===================================================================
# Special functions extensions
# ===================================================================
