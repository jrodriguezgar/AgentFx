"""Tests for fxNumeric.geometry_functions."""

import math

import pytest

from formulite.fxNumeric import (
    capsule_surface_area,
    capsule_volume,
    circular_ring_perimeter,
    cuboid_space_diagonal,
    dodecahedron_surface_area,
    dodecahedron_volume,
    icosahedron_surface_area,
    icosahedron_volume,
    octahedron_surface_area,
    octahedron_volume,
    polygon_centroid,
    prism_surface_area,
    prism_volume,
    pyramid_surface_area,
    rhombus_perimeter,
    shoelace_area,
    spherical_cap_surface_area,
    tetrahedron_surface_area,
    tetrahedron_volume,
)


class TestCircularRingPerimeter:
    def test_basic(self):
        assert round(circular_ring_perimeter(5.0, 3.0), 4) == 50.2655

    def test_invalid(self):
        with pytest.raises(ValueError):
            circular_ring_perimeter(3.0, 5.0)

class TestRhombusPerimeter:
    def test_basic(self):
        assert rhombus_perimeter(5.0) == 20.0

    def test_negative(self):
        with pytest.raises(ValueError):
            rhombus_perimeter(-1)

class TestTetrahedronSurfaceArea:
    def test_unit(self):
        assert round(tetrahedron_surface_area(1.0), 4) == 1.7321

    def test_edge_2(self):
        assert round(tetrahedron_surface_area(2.0), 4) == 6.9282

    def test_negative(self):
        with pytest.raises(ValueError):
            tetrahedron_surface_area(-1)

class TestPrismVolume:
    def test_basic(self):
        assert prism_volume(25.0, 10.0) == 250.0

    def test_negative(self):
        with pytest.raises(ValueError):
            prism_volume(-1, 10)

class TestPrismSurfaceArea:
    def test_basic(self):
        assert prism_surface_area(25.0, 20.0, 10.0) == 250.0

    def test_negative(self):
        with pytest.raises(ValueError):
            prism_surface_area(-1, 20, 10)

class TestTetrahedronVolume:
    def test_unit(self):
        assert round(tetrahedron_volume(1.0), 4) == 0.1179

    def test_edge_2(self):
        # V = 8/(6*sqrt(2)) = 8/8.485 = 0.9428
        assert round(tetrahedron_volume(2.0), 4) == 0.9428

    def test_negative(self):
        with pytest.raises(ValueError):
            tetrahedron_volume(-1)

class TestOctahedronVolume:
    def test_unit(self):
        assert round(octahedron_volume(1.0), 4) == 0.4714

    def test_edge_2(self):
        assert round(octahedron_volume(2.0), 4) == 3.7712

    def test_negative(self):
        with pytest.raises(ValueError):
            octahedron_volume(-1)

class TestOctahedronSurfaceArea:
    def test_unit(self):
        assert round(octahedron_surface_area(1.0), 4) == 3.4641

    def test_negative(self):
        with pytest.raises(ValueError):
            octahedron_surface_area(-1)

class TestDodecahedronVolume:
    def test_unit(self):
        assert round(dodecahedron_volume(1.0), 4) == 7.6631

    def test_negative(self):
        with pytest.raises(ValueError):
            dodecahedron_volume(-1)

class TestDodecahedronSurfaceArea:
    def test_unit(self):
        assert round(dodecahedron_surface_area(1.0), 4) == 20.6457

    def test_negative(self):
        with pytest.raises(ValueError):
            dodecahedron_surface_area(-1)

class TestIcosahedronVolume:
    def test_unit(self):
        assert round(icosahedron_volume(1.0), 4) == 2.1817

    def test_negative(self):
        with pytest.raises(ValueError):
            icosahedron_volume(-1)

class TestIcosahedronSurfaceArea:
    def test_unit(self):
        assert round(icosahedron_surface_area(1.0), 4) == 8.6603

    def test_negative(self):
        with pytest.raises(ValueError):
            icosahedron_surface_area(-1)

class TestCapsuleVolume:
    def test_basic(self):
        assert round(capsule_volume(2.0, 5.0), 4) == 96.3422

    def test_zero_length(self):
        # Capsule with no cylinder = sphere
        assert capsule_volume(3.0, 0.0) == pytest.approx(4.0 / 3.0 * math.pi * 27.0, rel=1e-8)

    def test_negative(self):
        with pytest.raises(ValueError):
            capsule_volume(-1, 5)

class TestCapsuleSurfaceArea:
    def test_basic(self):
        assert round(capsule_surface_area(2.0, 5.0), 4) == 113.0973

    def test_zero_length(self):
        # Sphere
        assert capsule_surface_area(3.0, 0.0) == pytest.approx(4.0 * math.pi * 9.0, rel=1e-8)

class TestShoelaceArea:
    def test_rectangle(self):
        assert shoelace_area([(0, 0), (4, 0), (4, 3), (0, 3)]) == 12.0

    def test_triangle(self):
        assert shoelace_area([(0, 0), (6, 0), (3, 4)]) == 12.0

    def test_too_few_vertices(self):
        with pytest.raises(ValueError):
            shoelace_area([(0, 0), (1, 1)])

    def test_type_error(self):
        with pytest.raises(TypeError):
            shoelace_area("not a list")

class TestPolygonCentroid:
    def test_rectangle(self):
        cx, cy = polygon_centroid([(0, 0), (4, 0), (4, 3), (0, 3)])
        assert cx == pytest.approx(2.0)
        assert cy == pytest.approx(1.5)

    def test_triangle(self):
        cx, cy = polygon_centroid([(0, 0), (6, 0), (0, 6)])
        assert cx == pytest.approx(2.0, rel=1e-8)
        assert cy == pytest.approx(2.0, rel=1e-8)

    def test_too_few(self):
        with pytest.raises(ValueError):
            polygon_centroid([(0, 0), (1, 1)])

class TestSphericalCapSurfaceArea:
    def test_basic(self):
        assert round(spherical_cap_surface_area(5.0, 2.0), 4) == 62.8319

    def test_hemisphere(self):
        # Full hemisphere: h = R → SA = 2πR²
        sa = spherical_cap_surface_area(3.0, 3.0)
        assert sa == pytest.approx(2.0 * math.pi * 9.0, rel=1e-8)

    def test_invalid_height(self):
        with pytest.raises(ValueError):
            spherical_cap_surface_area(5.0, 11.0)

class TestPyramidSurfaceArea:
    def test_basic(self):
        assert pyramid_surface_area(16.0, 16.0, 5.0) == 56.0

    def test_negative(self):
        with pytest.raises(ValueError):
            pyramid_surface_area(-1, 16, 5)

class TestCuboidSpaceDiagonal:
    def test_basic(self):
        assert round(cuboid_space_diagonal(3.0, 4.0, 5.0), 4) == 7.0711

    def test_cube(self):
        d = cuboid_space_diagonal(1.0, 1.0, 1.0)
        assert d == pytest.approx(math.sqrt(3.0))

class TestDistance:

    def test_2d(self):
        from formulite.fxNumeric.geometry_functions import distance_2d
        assert distance_2d(0, 0, 3, 4) == pytest.approx(5.0)

    def test_3d(self):
        from formulite.fxNumeric.geometry_functions import distance_3d
        assert distance_3d(0, 0, 0, 1, 2, 2) == pytest.approx(3.0)

class TestMidpoint:

    def test_2d(self):
        from formulite.fxNumeric.geometry_functions import midpoint_2d
        assert midpoint_2d(0, 0, 4, 6) == (2.0, 3.0)

    def test_3d(self):
        from formulite.fxNumeric.geometry_functions import midpoint_3d
        assert midpoint_3d(0, 0, 0, 2, 4, 6) == (1.0, 2.0, 3.0)

class TestTriangleFormulas:

    def test_area_vertices(self):
        from formulite.fxNumeric.geometry_functions import triangle_area_vertices
        assert triangle_area_vertices(0, 0, 4, 0, 0, 3) == pytest.approx(6.0)

    def test_heron(self):
        from formulite.fxNumeric.geometry_functions import heron_formula
        assert heron_formula(3, 4, 5) == pytest.approx(6.0)

    def test_law_of_cosines_side(self):
        from formulite.fxNumeric.geometry_functions import law_of_cosines_side
        assert law_of_cosines_side(3, 4, math.pi / 2) == pytest.approx(5.0)

    def test_law_of_cosines_angle(self):
        from formulite.fxNumeric.geometry_functions import law_of_cosines_angle
        assert law_of_cosines_angle(3, 4, 5) == pytest.approx(math.pi / 2, rel=1e-6)

class TestCircleFormulas:

    def test_area(self):
        from formulite.fxNumeric.geometry_functions import circle_area
        assert circle_area(1) == pytest.approx(math.pi)

    def test_circumference(self):
        from formulite.fxNumeric.geometry_functions import circle_circumference
        assert circle_circumference(1) == pytest.approx(2 * math.pi)

    def test_sector_area(self):
        from formulite.fxNumeric.geometry_functions import sector_area
        assert sector_area(2, math.pi / 2) == pytest.approx(math.pi)

    def test_arc_length(self):
        from formulite.fxNumeric.geometry_functions import arc_length
        assert arc_length(2, math.pi) == pytest.approx(2 * math.pi)

class TestSolidGeometry:

    def test_sphere_volume(self):
        from formulite.fxNumeric.geometry_functions import sphere_volume
        assert sphere_volume(1) == pytest.approx(4 * math.pi / 3)

    def test_sphere_surface(self):
        from formulite.fxNumeric.geometry_functions import sphere_surface_area
        assert sphere_surface_area(1) == pytest.approx(4 * math.pi)

    def test_cylinder_volume(self):
        from formulite.fxNumeric.geometry_functions import cylinder_volume
        assert cylinder_volume(2, 5) == pytest.approx(20 * math.pi)

    def test_cone_volume(self):
        from formulite.fxNumeric.geometry_functions import cone_volume
        assert cone_volume(3, 4) == pytest.approx(12 * math.pi)

    def test_ellipsoid_volume(self):
        from formulite.fxNumeric.geometry_functions import ellipsoid_volume
        assert ellipsoid_volume(2, 3, 4) == pytest.approx(32 * math.pi)

    def test_torus_volume(self):
        from formulite.fxNumeric.geometry_functions import torus_volume
        assert torus_volume(3, 1) == pytest.approx(6 * math.pi ** 2)

class TestConicSections:

    def test_parabola_focus(self):
        from formulite.fxNumeric.geometry_functions import parabola_focus
        assert parabola_focus(1) == (0, 0.25)

    def test_hyperbola_eccentricity(self):
        from formulite.fxNumeric.geometry_functions import hyperbola_eccentricity
        assert hyperbola_eccentricity(3, 4) == pytest.approx(5 / 3)


# ---------------------------------------------------------------------------
# Vector analysis functions
# ---------------------------------------------------------------------------
