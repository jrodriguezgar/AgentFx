"""Tests for fxNumeric.trigonometry_functions."""

import math
from datetime import datetime

import pytest

from shortfx.fxNumeric import (
    along_track_distance,
    angle_bisector_length,
    angular_deficiency,
    annular_sector_area,
    annulus_area,
    arbelos_area,
    arc_length,
    cartesian_to_cylindrical,
    cartesian_to_polar,
    cartesian_to_spherical,
    chord_length,
    circular_ring_area,
    circular_sector_area,
    circular_segment_area,
    circular_segment_chord,
    circular_segment_height,
    cone_slant_height,
    coversine,
    cross_track_distance,
    cyclic_polygon_radius,
    cylindrical_to_cartesian,
    damped_oscillation,
    ellipse_circumference_approx,
    ellipsoid_volume,
    epicycloid_arc_length,
    frustum_lateral_area,
    geodesic_area,
    gudermannian,
    hacoverversine,
    haversine_angle,
    haversine_distance,
    hexagon_area,
    hyperbolic_distance,
    hypocycloid_arc_length,
    inscribed_angle,
    inverse_gudermannian,
    lens_area,
    normalize_angle,
    paraboloid_volume,
    parallelogram_area,
    polar_to_cartesian,
    power_of_point,
    regular_polygon_apothem,
    regular_polygon_exterior_angle,
    regular_polygon_interior_angle,
    regular_polygon_perimeter,
    reuleaux_triangle_area,
    rhombus_area,
    sagitta,
    salinon_area,
    sector_arc_length,
    sector_area,
    segment_area,
    sinc,
    sinusoidal_wave,
    solar_elevation,
    spherical_law_of_cosines,
    spherical_lune_area,
    spherical_sector_volume,
    spherical_to_cartesian,
    spherical_wedge_volume,
    spherical_zone_area,
    spheroid_volume,
    stadium_area,
    stadium_perimeter,
    trapezoid_area,
    vincenty_distance,
    wedge_volume,
)
from shortfx.fxNumeric.conversion_functions import radiation_dose_convert
from shortfx.fxNumeric.finance_functions import profitability_index


class TestProfitabilityIndex:

    def test_basic(self):
        result = profitability_index(0.10, 1000, [300, 400, 500, 200])
        assert result == pytest.approx(1.1156, rel=1e-3)

    def test_zero_rate(self):
        result = profitability_index(0, 1000, [500, 600])
        assert result == pytest.approx(1.1)

    def test_negative_investment_raises(self):
        with pytest.raises(ValueError):
            profitability_index(0.10, -1000, [500])

    def test_invalid_type(self):
        with pytest.raises(TypeError):
            profitability_index(0.10, 1000, "not a list")


# ── Trigonometry ─────────────────────────────────────────────────────────────


class TestSinc:

    def test_zero(self):
        assert sinc(0) == 1.0

    def test_half(self):
        assert sinc(0.5) == pytest.approx(0.6366197724, rel=1e-8)

    def test_integer(self):
        assert sinc(1) == pytest.approx(0.0, abs=1e-15)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sinc("0")

class TestPolarCartesian:

    def test_polar_to_cartesian(self):
        x, y = polar_to_cartesian(1.0, math.pi / 2)
        assert x == pytest.approx(0.0, abs=1e-10)
        assert y == pytest.approx(1.0, abs=1e-10)

    def test_cartesian_to_polar(self):
        r, theta = cartesian_to_polar(0, 1)
        assert r == pytest.approx(1.0)
        assert theta == pytest.approx(math.pi / 2)

    def test_roundtrip(self):
        r, theta = 5.0, 0.7
        x, y = polar_to_cartesian(r, theta)
        r2, theta2 = cartesian_to_polar(x, y)
        assert r2 == pytest.approx(r, rel=1e-10)
        assert theta2 == pytest.approx(theta, rel=1e-10)

class TestSpherical:

    def test_north_pole(self):
        x, y, z = spherical_to_cartesian(1, 0, 0)
        assert x == pytest.approx(0.0, abs=1e-10)
        assert y == pytest.approx(0.0, abs=1e-10)
        assert z == pytest.approx(1.0, abs=1e-10)

    def test_roundtrip(self):
        r, theta, phi = 3.0, 0.5, 1.2
        x, y, z = spherical_to_cartesian(r, theta, phi)
        r2, theta2, phi2 = cartesian_to_spherical(x, y, z)
        assert r2 == pytest.approx(r, rel=1e-10)
        assert theta2 == pytest.approx(theta, rel=1e-10)
        assert phi2 == pytest.approx(phi, rel=1e-10)

    def test_origin(self):
        r, theta, phi = cartesian_to_spherical(0, 0, 0)
        assert r == 0.0

    def test_negative_r(self):
        # New implementation does not raise for negative r
        x, y, z = spherical_to_cartesian(-1, 0, 0)
        assert z == pytest.approx(-1.0, abs=1e-10)

class TestHaversineDistance:

    def test_madrid_paris(self):
        d = haversine_distance(40.4168, -3.7038, 48.8566, 2.3522)
        assert d == pytest.approx(1053.0, abs=5)

    def test_same_point(self):
        assert haversine_distance(0, 0, 0, 0) == pytest.approx(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            haversine_distance("40", 0, 0, 0)

class TestBearing:

    def test_madrid_to_paris(self):
        from shortfx.fxNumeric.trigonometry_functions import bearing

        b = bearing(40.4168, -3.7038, 48.8566, 2.3522)
        assert 20 < b < 30

class TestDestinationPoint:

    def test_northward(self):
        from shortfx.fxNumeric.trigonometry_functions import destination_point

        lat, lon = destination_point(0, 0, 0, 111.195)  # ~1 degree north
        assert lat == pytest.approx(1.0, abs=0.1)

class TestMidpointGeo:

    def test_symmetry(self):
        from shortfx.fxNumeric.trigonometry_functions import midpoint_geo

        mlat, mlon = midpoint_geo(0, 0, 0, 10)
        assert mlon == pytest.approx(5.0, abs=0.1)

class TestPointInCircle:

    def test_inside(self):
        from shortfx.fxNumeric.trigonometry_functions import point_in_circle

        assert point_in_circle(1, 1, 0, 0, 2) is True

    def test_outside(self):
        from shortfx.fxNumeric.trigonometry_functions import point_in_circle

        assert point_in_circle(3, 0, 0, 0, 2) is False

class TestPointInTriangle:

    def test_inside(self):
        from shortfx.fxNumeric.trigonometry_functions import point_in_triangle

        assert point_in_triangle(1, 1, 0, 0, 4, 0, 0, 4) is True

    def test_outside(self):
        from shortfx.fxNumeric.trigonometry_functions import point_in_triangle

        assert point_in_triangle(5, 5, 0, 0, 4, 0, 0, 4) is False

class TestTriangleCentroid:

    def test_right_triangle(self):
        from shortfx.fxNumeric.trigonometry_functions import triangle_centroid

        cx, cy = triangle_centroid(0, 0, 3, 0, 0, 3)
        assert (cx, cy) == (1.0, 1.0)

class TestTriangleIncircleRadius:

    def test_345_triangle(self):
        from shortfx.fxNumeric.trigonometry_functions import triangle_incircle_radius

        assert round(triangle_incircle_radius(3, 4, 5), 6) == 1.0

class TestTriangleCircumradius:

    def test_345_triangle(self):
        from shortfx.fxNumeric.trigonometry_functions import triangle_circumradius

        assert round(triangle_circumradius(3, 4, 5), 6) == 2.5

class TestRotation2D:

    def test_90_degrees(self):
        from shortfx.fxNumeric.trigonometry_functions import rotation_2d

        rx, ry = rotation_2d(1, 0, math.pi / 2)
        assert round(rx, 10) == 0.0
        assert round(ry, 10) == 1.0

class TestDistancePointToLine:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import distance_point_to_line

        assert distance_point_to_line(1, 1, 0, 0, 2, 0) == 1.0

class TestTriangleAreaSas:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import triangle_area_sas
        assert round(triangle_area_sas(5, 7, math.pi / 6), 4) == 8.75

    def test_right_angle(self):
        from shortfx.fxNumeric.trigonometry_functions import triangle_area_sas
        assert round(triangle_area_sas(3, 4, math.pi / 2), 4) == 6.0

    def test_zero_side(self):
        from shortfx.fxNumeric.trigonometry_functions import triangle_area_sas

        with pytest.raises(ValueError):
            triangle_area_sas(0, 5, 1.0)

class TestLawOfCosinesSide:

    def test_equilateral_hint(self):
        from shortfx.fxNumeric.trigonometry_functions import law_of_cosines_side
        # Equilateral triangle: a=b=5, angle=60° → c=5
        assert round(law_of_cosines_side(5, 5, math.pi / 3), 4) == 5.0

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import law_of_cosines_side
        assert round(law_of_cosines_side(5, 7, math.pi / 3), 4) == 6.2450

class TestLawOfCosinesAngle:

    def test_right_triangle(self):
        from shortfx.fxNumeric.trigonometry_functions import law_of_cosines_angle
        # 3-4-5 right triangle: angle opposite 5 = pi/2
        assert round(law_of_cosines_angle(3, 4, 5), 4) == 1.5708

    def test_invalid_triangle(self):
        from shortfx.fxNumeric.trigonometry_functions import law_of_cosines_angle

        with pytest.raises(ValueError):
            law_of_cosines_angle(1, 1, 10)


# ── Number Theory ────────────────────────────────────────────────

class TestRegularPolygonArea:

    def test_hexagon(self):
        from shortfx.fxNumeric.trigonometry_functions import regular_polygon_area

        assert round(regular_polygon_area(6, 2), 4) == 10.3923

    def test_too_few_sides(self):
        from shortfx.fxNumeric.trigonometry_functions import regular_polygon_area

        with pytest.raises(ValueError):
            regular_polygon_area(2, 1)

class TestFrustumVolume:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import frustum_volume

        assert round(frustum_volume(2, 4, 5), 4) == 146.6077

    def test_negative_height(self):
        from shortfx.fxNumeric.trigonometry_functions import frustum_volume

        with pytest.raises(ValueError):
            frustum_volume(2, 4, -1)

class TestTorusVolume:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import torus_volume

        assert round(torus_volume(5, 2), 4) == 394.7842

    def test_minor_ge_major(self):
        from shortfx.fxNumeric.trigonometry_functions import torus_volume

        with pytest.raises(ValueError):
            torus_volume(2, 5)

class TestTorusSurfaceArea:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import torus_surface_area

        assert round(torus_surface_area(5, 2), 4) == 394.7842

    def test_type_error(self):
        from shortfx.fxNumeric.trigonometry_functions import torus_surface_area

        with pytest.raises(TypeError):
            torus_surface_area("a", 2)

class TestConeLateralArea:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import cone_lateral_area

        assert round(cone_lateral_area(3, 5), 4) == 47.1239

    def test_negative_radius(self):
        from shortfx.fxNumeric.trigonometry_functions import cone_lateral_area

        with pytest.raises(ValueError):
            cone_lateral_area(-3, 5)


# ── Number Theory ────────────────────────────────────────────────────

class TestSphericalCapVolume:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import spherical_cap_volume

        assert round(spherical_cap_volume(5, 2), 4) == 54.4543

    def test_height_too_large(self):
        from shortfx.fxNumeric.trigonometry_functions import spherical_cap_volume

        with pytest.raises(ValueError):
            spherical_cap_volume(5, 11)

class TestSphericalCapArea:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import spherical_cap_area

        assert round(spherical_cap_area(5, 2), 4) == 62.8319

    def test_negative(self):
        from shortfx.fxNumeric.trigonometry_functions import spherical_cap_area

        with pytest.raises(ValueError):
            spherical_cap_area(5, -1)

class TestPyramidVolume:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import pyramid_volume

        assert pyramid_volume(25, 6) == pytest.approx(50.0)

    def test_negative_height(self):
        from shortfx.fxNumeric.trigonometry_functions import pyramid_volume

        with pytest.raises(ValueError):
            pyramid_volume(25, -1)

class TestCylinderLateralArea:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import cylinder_lateral_area

        assert round(cylinder_lateral_area(3, 5), 4) == 94.2478

    def test_type_error(self):
        from shortfx.fxNumeric.trigonometry_functions import cylinder_lateral_area

        with pytest.raises(TypeError):
            cylinder_lateral_area("a", 5)

class TestRhombusArea:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import rhombus_area

        assert rhombus_area(10, 8) == 40.0

    def test_negative_diagonal(self):
        from shortfx.fxNumeric.trigonometry_functions import rhombus_area

        with pytest.raises(ValueError):
            rhombus_area(-10, 8)


# ── Number Theory ────────────────────────────────────────────────────

class TestTrapezoidArea:

    def test_basic(self):
        assert trapezoid_area(5, 8, 4) == pytest.approx(26.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            trapezoid_area("5", 8, 4)

class TestParallelogramArea:

    def test_basic(self):
        assert parallelogram_area(10, 6) == pytest.approx(60.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            parallelogram_area("10", 6)

class TestRegularPolygonPerimeter:

    def test_basic(self):
        assert regular_polygon_perimeter(6, 5) == pytest.approx(30.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            regular_polygon_perimeter("6", 5)

class TestSectorArcLength:

    def test_basic(self):
        assert sector_arc_length(3, math.pi / 3) == pytest.approx(math.pi, rel=1e-5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sector_arc_length("3", 60)

class TestCircularRingArea:

    def test_basic(self):
        assert circular_ring_area(5, 3) == pytest.approx(50.26548, rel=1e-4)

    def test_inner_larger_raises(self):
        with pytest.raises(ValueError):
            circular_ring_area(3, 5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            circular_ring_area("5", 3)


# ── Number Theory ────────────────────────────────────────────────────────────

class TestCircularSegmentArea:

    def test_basic(self):
        assert circular_segment_area(5, math.pi) == pytest.approx(39.2699, rel=1e-4)

    def test_invalid_angle_raises(self):
        with pytest.raises(ValueError):
            circular_segment_area(5, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            circular_segment_area("5", math.pi)

class TestEllipseCircumferenceApprox:

    def test_basic(self):
        assert ellipse_circumference_approx(5, 3) == pytest.approx(25.5270, rel=1e-3)

    def test_circle(self):
        # Circle: a=b=r -> C = 2πr
        assert ellipse_circumference_approx(5, 5) == pytest.approx(2 * math.pi * 5, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            ellipse_circumference_approx("5", 3)

class TestSphericalSectorVolume:

    def test_basic(self):
        assert spherical_sector_volume(5, 2) == pytest.approx(104.7198, rel=1e-4)

    def test_height_exceeds_raises(self):
        with pytest.raises(ValueError):
            spherical_sector_volume(5, 11)

    def test_type_error(self):
        with pytest.raises(TypeError):
            spherical_sector_volume("5", 2)

class TestHexagonArea:

    def test_basic(self):
        assert hexagon_area(4) == pytest.approx(41.5692, rel=1e-4)

    def test_unit(self):
        assert hexagon_area(1) == pytest.approx(3 * math.sqrt(3) / 2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            hexagon_area("4")

class TestWedgeVolume:

    def test_basic(self):
        assert wedge_volume(20, 5) == pytest.approx(50.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            wedge_volume("20", 5)


# ── Number Theory ────────────────────────────────────────────────────────────

class TestRegularPolygonInteriorAngle:

    def test_hexagon(self):
        assert regular_polygon_interior_angle(6) == pytest.approx(120.0)

    def test_triangle(self):
        assert regular_polygon_interior_angle(3) == pytest.approx(60.0)

    def test_too_few_sides_raises(self):
        with pytest.raises(ValueError):
            regular_polygon_interior_angle(2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            regular_polygon_interior_angle(6.0)

class TestRegularPolygonExteriorAngle:

    def test_hexagon(self):
        assert regular_polygon_exterior_angle(6) == pytest.approx(60.0)

    def test_square(self):
        assert regular_polygon_exterior_angle(4) == pytest.approx(90.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            regular_polygon_exterior_angle(6.0)

class TestSphericalZoneArea:

    def test_basic(self):
        assert spherical_zone_area(5, 3) == pytest.approx(94.2478, rel=1e-4)

    def test_height_exceeds_raises(self):
        with pytest.raises(ValueError):
            spherical_zone_area(5, 11)

    def test_type_error(self):
        with pytest.raises(TypeError):
            spherical_zone_area("5", 3)

class TestCircularSectorArea:

    def test_quarter(self):
        assert circular_sector_area(5, math.pi / 2) == pytest.approx(19.635, rel=1e-3)

    def test_invalid_angle_raises(self):
        with pytest.raises(ValueError):
            circular_sector_area(5, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            circular_sector_area("5", math.pi / 2)

class TestEllipsoidVolume:

    def test_basic(self):
        assert ellipsoid_volume(3, 4, 5) == pytest.approx(251.3274, rel=1e-4)

    def test_sphere(self):
        assert ellipsoid_volume(5, 5, 5) == pytest.approx((4 / 3) * math.pi * 125, rel=1e-5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            ellipsoid_volume("3", 4, 5)


# ── Number Theory ────────────────────────────────────────────────────────────

class TestParaboloidVolume:

    def test_basic(self):
        assert paraboloid_volume(3, 4) == pytest.approx(56.5487, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            paraboloid_volume("3", 4)

class TestInscribedAngle:

    def test_basic(self):
        assert inscribed_angle(math.pi) == pytest.approx(math.pi / 2)

    def test_invalid_raises(self):
        with pytest.raises(ValueError):
            inscribed_angle(0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            inscribed_angle("pi")

class TestConeSlantHeight:

    def test_345(self):
        assert cone_slant_height(3, 4) == pytest.approx(5.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cone_slant_height("3", 4)

class TestSphericalWedgeVolume:

    def test_basic(self):
        assert spherical_wedge_volume(5, math.pi / 2) == pytest.approx(130.8997, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            spherical_wedge_volume("5", math.pi / 2)

class TestLensArea:

    def test_basic(self):
        assert lens_area(5, 6) == pytest.approx(22.3648, rel=1e-3)

    def test_coincident(self):
        # d=0 -> full overlap = area of one circle
        assert lens_area(5, 0) == pytest.approx(math.pi * 25, rel=1e-4)

    def test_too_far_raises(self):
        with pytest.raises(ValueError):
            lens_area(5, 10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            lens_area("5", 6)


# ── Number Theory ────────────────────────────────────────────────────────────

class TestFrustumLateralArea:
    def test_basic(self):
        assert frustum_lateral_area(2, 4, 5) == pytest.approx(94.2478, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            frustum_lateral_area("a", 1, 1)

    def test_negative_r(self):
        with pytest.raises(ValueError):
            frustum_lateral_area(-1, 4, 5)

class TestCyclicPolygonRadius:
    def test_hexagon(self):
        assert cyclic_polygon_radius(1, 6) == pytest.approx(1.0, rel=1e-4)

    def test_square(self):
        assert cyclic_polygon_radius(1, 4) == pytest.approx(
            1 / (2 * math.sin(math.pi / 4)), rel=1e-4
        )

    def test_type_error(self):
        with pytest.raises(TypeError):
            cyclic_polygon_radius("a", 3)

    def test_too_few_sides(self):
        with pytest.raises(ValueError):
            cyclic_polygon_radius(1, 2)

class TestPowerOfPoint:
    def test_outside(self):
        assert power_of_point(5, 3) == pytest.approx(16.0)

    def test_on_circle(self):
        assert power_of_point(3, 3) == pytest.approx(0.0)

    def test_inside(self):
        assert power_of_point(2, 3) == pytest.approx(-5.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            power_of_point("a", 1)

class TestAnnularSectorArea:
    def test_basic(self):
        assert annular_sector_area(2, 5, math.pi / 2) == pytest.approx(16.4934, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            annular_sector_area("a", 1, 1)

    def test_inner_ge_outer(self):
        with pytest.raises(ValueError):
            annular_sector_area(5, 3, 1)

class TestSphericalLuneArea:
    def test_basic(self):
        assert spherical_lune_area(5, math.pi / 3) == pytest.approx(52.3599, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            spherical_lune_area("a", 1)

    def test_negative_radius(self):
        with pytest.raises(ValueError):
            spherical_lune_area(-1, 1)


# ---------------------------------------------------------------------------
# Number Theory
# ---------------------------------------------------------------------------

class TestRegularPolygonApothem:
    def test_hexagon(self):
        assert regular_polygon_apothem(1, 6) == pytest.approx(0.866025, rel=1e-4)

    def test_square(self):
        assert regular_polygon_apothem(2, 4) == pytest.approx(1.0, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            regular_polygon_apothem("a", 3)

    def test_too_few_sides(self):
        with pytest.raises(ValueError):
            regular_polygon_apothem(1, 2)

class TestSpheroidVolume:
    def test_earth_approx(self):
        assert spheroid_volume(6378, 6357) == pytest.approx(1083202991015.0, rel=1e-3)

    def test_sphere(self):
        assert spheroid_volume(5, 5) == pytest.approx(4 / 3 * math.pi * 125, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            spheroid_volume("a", 1)

    def test_negative_radius(self):
        with pytest.raises(ValueError):
            spheroid_volume(-1, 1)

class TestStadiumArea:
    def test_basic(self):
        assert stadium_area(5, 10) == pytest.approx(178.5398, rel=1e-4)

    def test_zero_straight(self):
        # Becomes a circle
        assert stadium_area(5, 0) == pytest.approx(math.pi * 25, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            stadium_area("a", 1)

    def test_negative_straight(self):
        with pytest.raises(ValueError):
            stadium_area(5, -1)

class TestStadiumPerimeter:
    def test_basic(self):
        assert stadium_perimeter(5, 10) == pytest.approx(51.4159, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            stadium_perimeter("a", 1)

class TestCircularSegmentChord:
    def test_right_angle(self):
        assert circular_segment_chord(5, math.pi / 2) == pytest.approx(7.071068, rel=1e-4)

    def test_full_diameter(self):
        assert circular_segment_chord(5, math.pi) == pytest.approx(10.0, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            circular_segment_chord("a", 1)

    def test_zero_angle(self):
        with pytest.raises(ValueError):
            circular_segment_chord(5, 0)


# ---------------------------------------------------------------------------
# Number Theory
# ---------------------------------------------------------------------------

class TestReuleauxTriangleArea:
    def test_unit(self):
        assert reuleaux_triangle_area(1) == pytest.approx(0.704771, rel=1e-4)

    def test_scaled(self):
        assert reuleaux_triangle_area(2) == pytest.approx(
            (math.pi - math.sqrt(3)) / 2 * 4, rel=1e-4
        )

    def test_type_error(self):
        with pytest.raises(TypeError):
            reuleaux_triangle_area("a")

    def test_negative(self):
        with pytest.raises(ValueError):
            reuleaux_triangle_area(-1)

class TestArbelosArea:
    def test_basic(self):
        assert arbelos_area(5, 3, 2) == pytest.approx(9.424778, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            arbelos_area("a", 1, 1)

    def test_radii_mismatch(self):
        with pytest.raises(ValueError):
            arbelos_area(5, 2, 2)  # 5 ≠ 2+2

class TestSalinonArea:
    def test_basic(self):
        assert salinon_area(4, 2) == pytest.approx(28.274334, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            salinon_area("a", 1)

    def test_r1_ge_r(self):
        with pytest.raises(ValueError):
            salinon_area(3, 3)

class TestEpicycloidArcLength:
    def test_basic(self):
        assert epicycloid_arc_length(5, 1) == pytest.approx(9.6)

    def test_type_error(self):
        with pytest.raises(TypeError):
            epicycloid_arc_length("a", 1)

    def test_negative(self):
        with pytest.raises(ValueError):
            epicycloid_arc_length(5, -1)

class TestHypocycloidArcLength:
    def test_basic(self):
        assert hypocycloid_arc_length(5, 1) == pytest.approx(6.4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            hypocycloid_arc_length("a", 1)

    def test_r_ge_R(self):
        with pytest.raises(ValueError):
            hypocycloid_arc_length(5, 5)


# ---------------------------------------------------------------------------
# Number Theory
# ---------------------------------------------------------------------------

class TestRadiationDoseConvert:
    def test_sv_to_rem(self):
        assert radiation_dose_convert(1, "sv", "rem") == pytest.approx(100.0)

    def test_roundtrip(self):
        result = radiation_dose_convert(radiation_dose_convert(1, "gy", "rad"), "rad", "gy")
        assert result == pytest.approx(1.0, abs=1e-8)

    def test_type_error(self):
        with pytest.raises(TypeError):
            radiation_dose_convert("hot", "sv", "rem")

    def test_unknown_unit(self):
        with pytest.raises(ValueError):
            radiation_dose_convert(1, "sv", "banana")


# ---------------------------------------------------------------------------
# fxNumeric — trigonometry_functions.py
# ---------------------------------------------------------------------------


class TestCrossTrackDistance:
    def test_on_path(self):
        result = cross_track_distance(40.0, -3.0, 40.0, -3.0, 41.0, -2.0)
        assert abs(result) < 1.0  # point is on the path

    def test_type_error(self):
        with pytest.raises(TypeError):
            cross_track_distance("a", -3, 40, -3, 41, -2)

class TestAlongTrackDistance:
    def test_start_point(self):
        result = along_track_distance(40.0, -3.0, 40.0, -3.0, 41.0, -2.0)
        assert abs(result) < 1.0  # at the start of the path

    def test_type_error(self):
        with pytest.raises(TypeError):
            along_track_distance("a", -3, 40, -3, 41, -2)

class TestVincentyDistance:

    def test_madrid_paris(self):
        d = vincenty_distance(40.4168, -3.7038, 48.8566, 2.3522)
        assert abs(d - 1052744) < 500

class TestGeodesicArea:

    def test_one_degree_square(self):
        area = geodesic_area([(0, 0), (0, 1), (1, 1), (1, 0)])
        assert abs(area / 1e6 - 12309) < 100

    def test_too_few_vertices(self):

        with pytest.raises(ValueError):
            geodesic_area([(0, 0), (1, 1)])

class TestSolarElevation:

    def test_noon_summer(self):
        elev = solar_elevation(datetime(2026, 6, 21, 12, 0), 40.0, -3.7)
        assert 70 < elev < 80


# ── fxNumeric ── number_theory_functions ────────────────────────────────

class TestGudermannian:
    def test_one(self):
        assert round(gudermannian(1.0), 4) == 0.8658

    def test_zero(self):
        assert gudermannian(0) == pytest.approx(0.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            gudermannian("abc")

class TestInverseGudermannian:
    def test_basic(self):
        assert round(inverse_gudermannian(0.8658), 4) == 1.0

    def test_zero(self):
        assert inverse_gudermannian(0.0) == pytest.approx(0.0, abs=1e-10)

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            inverse_gudermannian(math.pi / 2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            inverse_gudermannian("abc")

class TestHacoverversine:
    def test_basic(self):
        assert round(hacoverversine(0.5), 4) == 0.7397

    def test_zero(self):
        assert hacoverversine(0) == 0.5

    def test_type_error(self):
        with pytest.raises(TypeError):
            hacoverversine("abc")

class TestChordLength:
    def test_basic(self):
        assert round(chord_length(1.0, 1.0), 4) == 0.9589

    def test_zero_angle(self):
        assert chord_length(1.0, 0.0) == pytest.approx(0.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            chord_length("abc", 1.0)

class TestSagitta:
    def test_basic(self):
        assert round(sagitta(1.0, 1.0), 4) == 0.1224

    def test_zero_angle(self):
        assert sagitta(1.0, 0.0) == pytest.approx(0.0, abs=1e-10)

class TestArcLength:
    def test_basic(self):
        assert round(arc_length(5.0, 1.0), 4) == 5.0

    def test_full_circle(self):
        assert arc_length(1.0, 2 * math.pi) == pytest.approx(2 * math.pi, rel=1e-8)

class TestSectorArea:
    def test_basic(self):
        assert round(sector_area(5.0, 1.0), 4) == 12.5

    def test_full_circle(self):
        assert sector_area(1.0, 2 * math.pi) == pytest.approx(math.pi, rel=1e-8)

class TestSegmentArea:
    def test_basic(self):
        assert round(segment_area(5.0, 1.0), 4) == 1.9816

    def test_zero(self):
        assert segment_area(5.0, 0.0) == pytest.approx(0.0, abs=1e-10)

class TestHyperbolicDistance:
    def test_basic(self):
        assert round(hyperbolic_distance(0, 1, 0, 2), 4) == 0.6931

    def test_same_point(self):
        assert hyperbolic_distance(1, 1, 1, 1) == pytest.approx(0.0, abs=1e-10)

    def test_invalid_y(self):
        with pytest.raises(ValueError):
            hyperbolic_distance(0, 0, 0, 1)

class TestSphericalLawOfCosines:
    def test_basic(self):
        assert round(spherical_law_of_cosines(1.0, 1.0, 1.0), 4) == 0.8305

    def test_zero_angle(self):
        # C=0 → c = |a - b|
        c = spherical_law_of_cosines(0.5, 0.3, 0)
        assert c == pytest.approx(0.2, abs=1e-8)

    def test_type_error(self):
        with pytest.raises(TypeError):
            spherical_law_of_cosines("abc", 1.0, 1.0)

class TestPolarToCartesian:
    def test_basic(self):
        x, y = polar_to_cartesian(1.0, 0.0)
        assert x == pytest.approx(1.0)
        assert y == pytest.approx(0.0, abs=1e-10)

    def test_quarter_turn(self):
        x, y = polar_to_cartesian(1.0, math.pi / 2)
        assert x == pytest.approx(0.0, abs=1e-10)
        assert y == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            polar_to_cartesian("a", 0)

class TestCartesianToPolar:
    def test_basic(self):
        r, theta = cartesian_to_polar(1.0, 0.0)
        assert r == pytest.approx(1.0)
        assert theta == pytest.approx(0.0)

    def test_origin(self):
        r, theta = cartesian_to_polar(0, 0)
        assert r == pytest.approx(0.0)

    def test_roundtrip(self):
        x, y = polar_to_cartesian(3.0, 1.2)
        r, theta = cartesian_to_polar(x, y)
        assert r == pytest.approx(3.0)
        assert theta == pytest.approx(1.2)

class TestSphericalToCartesian:
    def test_north_pole(self):
        x, y, z = spherical_to_cartesian(1.0, 0.0, 0.0)
        assert x == pytest.approx(0.0, abs=1e-10)
        assert y == pytest.approx(0.0, abs=1e-10)
        assert z == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            spherical_to_cartesian("a", 0, 0)

class TestCartesianToSpherical:
    def test_north_pole(self):
        r, theta, phi = cartesian_to_spherical(0.0, 0.0, 1.0)
        assert r == pytest.approx(1.0)
        assert theta == pytest.approx(0.0)

    def test_origin(self):
        r, theta, phi = cartesian_to_spherical(0, 0, 0)
        assert r == pytest.approx(0.0)

    def test_roundtrip(self):
        x, y, z = spherical_to_cartesian(2.0, 0.5, 1.0)
        r, theta, phi = cartesian_to_spherical(x, y, z)
        assert r == pytest.approx(2.0)
        assert theta == pytest.approx(0.5)
        assert phi == pytest.approx(1.0)

class TestCylindricalToCartesian:
    def test_basic(self):
        x, y, z = cylindrical_to_cartesian(1.0, 0.0, 5.0)
        assert x == pytest.approx(1.0)
        assert y == pytest.approx(0.0, abs=1e-10)
        assert z == pytest.approx(5.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cylindrical_to_cartesian("a", 0, 0)

class TestCartesianToCylindrical:
    def test_basic(self):
        rho, phi, z = cartesian_to_cylindrical(1.0, 0.0, 5.0)
        assert rho == pytest.approx(1.0)
        assert phi == pytest.approx(0.0)
        assert z == pytest.approx(5.0)

    def test_roundtrip(self):
        x, y, z = cylindrical_to_cartesian(3.0, 1.5, 7.0)
        rho, phi, z2 = cartesian_to_cylindrical(x, y, z)
        assert rho == pytest.approx(3.0)
        assert phi == pytest.approx(1.5)
        assert z2 == pytest.approx(7.0)

class TestAngleBisectorLength:
    def test_basic(self):
        assert round(angle_bisector_length(3.0, 4.0, 1.0), 4) == 3.0089

    def test_equal_sides(self):
        # For isoceles triangle with equal sides, bisector length
        val = angle_bisector_length(5.0, 5.0, math.pi / 3)
        assert val == pytest.approx(5.0 * math.cos(math.pi / 6), rel=1e-8)

    def test_negative_side(self):
        with pytest.raises(ValueError):
            angle_bisector_length(-1, 4, 1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            angle_bisector_length("a", 4, 1.0)

class TestCircularSegmentHeight:
    def test_basic(self):
        assert round(circular_segment_height(10.0, 1.0), 4) == 1.2242

    def test_zero_angle(self):
        assert circular_segment_height(10.0, 0) == pytest.approx(0.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            circular_segment_height("a", 1.0)

class TestSinusoidalWave:
    def test_peak(self):
        assert round(sinusoidal_wave(1.0, 1.0, 0.25), 4) == 1.0

    def test_zero_at_origin(self):
        assert sinusoidal_wave(1.0, 1.0, 0.0) == pytest.approx(0.0, abs=1e-10)

    def test_with_phase(self):
        val = sinusoidal_wave(2.0, 1.0, 0.0, math.pi / 2)
        assert val == pytest.approx(2.0, rel=1e-8)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sinusoidal_wave("a", 1, 0)

class TestDampedOscillation:
    def test_basic(self):
        assert round(damped_oscillation(1.0, 0.5, 1.0, 1.0), 4) == 0.6065

    def test_no_decay(self):
        val = damped_oscillation(1.0, 0.0, 1.0, 0.0)
        assert val == pytest.approx(1.0)

    def test_negative_decay(self):
        with pytest.raises(ValueError):
            damped_oscillation(1.0, -1, 1.0, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            damped_oscillation("a", 0.5, 1.0, 1.0)

class TestAngularDeficiency:
    def test_hexagon(self):
        assert round(angular_deficiency(6), 4) == 1.0472

    def test_triangle(self):
        assert angular_deficiency(3) == pytest.approx(2 * math.pi / 3)

    def test_square(self):
        assert angular_deficiency(4) == pytest.approx(math.pi / 2)

    def test_below_3(self):
        with pytest.raises(ValueError):
            angular_deficiency(2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            angular_deficiency(3.5)

class TestNormalizeAngle:
    def test_basic(self):
        assert round(normalize_angle(7.0), 4) == 0.7168

    def test_negative(self):
        val = normalize_angle(-1.0)
        assert val == pytest.approx(2 * math.pi - 1.0, rel=1e-8)

    def test_degrees(self):
        assert normalize_angle(370.0, 360.0) == pytest.approx(10.0)

    def test_zero(self):
        assert normalize_angle(0.0) == pytest.approx(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            normalize_angle("a")

class TestAnnulusArea:
    def test_basic(self):
        assert round(annulus_area(5.0, 3.0), 4) == 50.2655

    def test_invalid_inner(self):
        with pytest.raises(ValueError):
            annulus_area(3.0, 5.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            annulus_area("a", 3.0)

class TestRhombusAreaV2:
    def test_basic(self):
        assert rhombus_area(6.0, 8.0) == 24.0

    def test_negative_diagonal(self):
        with pytest.raises(ValueError):
            rhombus_area(-1, 8)

    def test_type_error(self):
        with pytest.raises(TypeError):
            rhombus_area("a", 8)

class TestRegularPolygonPerimeterV2:
    def test_hexagon(self):
        assert regular_polygon_perimeter(6, 5.0) == 30.0

    def test_triangle(self):
        assert regular_polygon_perimeter(3, 10.0) == 30.0

    def test_invalid_n(self):
        with pytest.raises(ValueError):
            regular_polygon_perimeter(2, 5.0)

class TestRegularPolygonInteriorAngleV2:
    def test_hexagon(self):
        assert regular_polygon_interior_angle(6) == 120.0

    def test_triangle(self):
        assert regular_polygon_interior_angle(3) == 60.0

    def test_square(self):
        assert regular_polygon_interior_angle(4) == 90.0

    def test_invalid(self):
        with pytest.raises(ValueError):
            regular_polygon_interior_angle(2)

class TestStadiumAreaV2:
    def test_basic(self):
        assert round(stadium_area(2.0, 5.0), 4) == 32.5664

    def test_zero_straight(self):
        # Stadium with no straight section = circle
        assert stadium_area(3.0, 0.0) == pytest.approx(math.pi * 9.0, rel=1e-8)

    def test_negative_length(self):
        with pytest.raises(ValueError):
            stadium_area(2.0, -1.0)

class TestConeSlantHeightV2:
    def test_345(self):
        assert cone_slant_height(3.0, 4.0) == 5.0

    def test_negative(self):
        with pytest.raises(ValueError):
            cone_slant_height(-1, 4)

class TestLawOfSines:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import law_of_sines
        result = law_of_sines(10, math.radians(30), math.radians(45))
        assert result == pytest.approx(14.1421, rel=1e-3)

    def test_symmetric(self):
        from shortfx.fxNumeric.trigonometry_functions import law_of_sines
        result = law_of_sines(5, math.radians(60), math.radians(60))
        assert result == pytest.approx(5.0, rel=1e-6)

    def test_invalid_angle_sum_raises(self):
        from shortfx.fxNumeric.trigonometry_functions import law_of_sines
        with pytest.raises(ValueError):
            law_of_sines(10, math.radians(100), math.radians(100))

class TestHeronsFormula:

    def test_345_triangle(self):
        from shortfx.fxNumeric.trigonometry_functions import herons_formula
        assert herons_formula(3, 4, 5) == pytest.approx(6.0)

    def test_equilateral(self):
        from shortfx.fxNumeric.trigonometry_functions import herons_formula
        result = herons_formula(6, 6, 6)
        assert result == pytest.approx(9.0 * math.sqrt(3), rel=1e-6)

    def test_invalid_triangle_raises(self):
        from shortfx.fxNumeric.trigonometry_functions import herons_formula
        with pytest.raises(ValueError):
            herons_formula(1, 2, 10)

class TestCircularArcLength:

    def test_quarter_circle(self):
        from shortfx.fxNumeric.trigonometry_functions import circular_arc_length
        result = circular_arc_length(5, math.pi / 2)
        assert result == pytest.approx(7.854, rel=1e-3)

    def test_full_circle(self):
        from shortfx.fxNumeric.trigonometry_functions import circular_arc_length
        result = circular_arc_length(1, 2 * math.pi)
        assert result == pytest.approx(2 * math.pi)

    def test_zero_angle(self):
        from shortfx.fxNumeric.trigonometry_functions import circular_arc_length
        assert circular_arc_length(10, 0) == 0.0


# ── Number Theory ───────────────────────────────────────────────────────────

class TestSectorAreaV2:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import sector_area
        result = sector_area(5, math.pi / 2)
        assert round(result, 4) == 19.635

    def test_zero_angle(self):
        from shortfx.fxNumeric.trigonometry_functions import sector_area
        result = sector_area(5, 0)
        assert result == 0.0

class TestChordLengthV2:

    def test_60_degrees(self):
        from shortfx.fxNumeric.trigonometry_functions import chord_length
        result = chord_length(5, math.pi / 3)
        assert round(result, 4) == 5.0

    def test_180_degrees(self):
        from shortfx.fxNumeric.trigonometry_functions import chord_length
        result = chord_length(5, math.pi)
        assert round(result, 4) == 10.0


# ============================================================================
# DATE CORE
# ============================================================================

class TestVersine:

    def test_pi_over_3(self):
        from shortfx.fxNumeric.trigonometry_functions import versine
        assert round(versine(math.pi / 3), 4) == 0.5

    def test_zero(self):
        from shortfx.fxNumeric.trigonometry_functions import versine
        assert versine(0) == 0.0

class TestExsecant:

    def test_pi_over_3(self):
        from shortfx.fxNumeric.trigonometry_functions import exsecant
        assert round(exsecant(math.pi / 3), 4) == 1.0

    def test_zero(self):
        from shortfx.fxNumeric.trigonometry_functions import exsecant
        assert exsecant(0) == 0.0

    def test_undefined(self):
        from shortfx.fxNumeric.trigonometry_functions import exsecant
        with pytest.raises(ValueError):
            exsecant(math.pi / 2)

class TestAngularVelocity:

    def test_one_rev(self):
        from shortfx.fxNumeric.trigonometry_functions import angular_velocity
        assert round(angular_velocity(1, 1), 4) == 6.2832

    def test_zero_time(self):
        from shortfx.fxNumeric.trigonometry_functions import angular_velocity
        with pytest.raises(ValueError):
            angular_velocity(1, 0)


# =====================================================================
# Number Theory
# =====================================================================

class TestGudermannianV2:

    def test_basic(self):
        assert round(gudermannian(1), 6) == 0.865769

    def test_zero(self):
        assert gudermannian(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            gudermannian("1")


# ──────────────────────────────────────────────
# Trigonometry: inverse_gudermannian
# ──────────────────────────────────────────────

class TestInverseGudermannianV2:

    def test_roundtrip(self):
        val = gudermannian(1.0)
        assert round(inverse_gudermannian(val), 4) == 1.0

    def test_zero(self):
        assert inverse_gudermannian(0) == 0.0

    def test_out_of_range_raises(self):
        with pytest.raises(ValueError):
            inverse_gudermannian(math.pi)


# ──────────────────────────────────────────────
# Trigonometry: coversine
# ──────────────────────────────────────────────

class TestCoversine:

    def test_basic(self):
        assert round(coversine(math.pi / 6), 1) == 0.5

    def test_zero(self):
        assert coversine(0) == 1.0

    def test_pi_half(self):
        assert round(coversine(math.pi / 2), 10) == 0.0


# ──────────────────────────────────────────────
# Number Theory: is_perfect_power
# ──────────────────────────────────────────────

class TestHaversineAngle:

    def test_zero(self):
        assert haversine_angle(0) == 0.0

    def test_pi(self):
        assert haversine_angle(math.pi) == pytest.approx(1.0)

    def test_pi_half(self):
        assert haversine_angle(math.pi / 2) == pytest.approx(0.5)


# ──────────────────────────────────────────────
# Trigonometry: sagitta
# ──────────────────────────────────────────────

class TestSagittaV2:

    def test_basic(self):
        assert round(sagitta(10, 1.0), 4) == 1.2242

    def test_full_radius(self):
        assert sagitta(5, math.pi) == pytest.approx(5.0)

    def test_negative_radius_raises(self):
        with pytest.raises(ValueError):
            sagitta(-10, 1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sagitta("10", 1.0)


# ──────────────────────────────────────────────
# Trigonometry: segment_area
# ──────────────────────────────────────────────

class TestSegmentAreaV2:

    def test_pi(self):
        assert round(segment_area(5, math.pi), 4) == 39.2699

    def test_negative_radius_raises(self):
        with pytest.raises(ValueError):
            segment_area(-5, 1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            segment_area("5", math.pi)


# ──────────────────────────────────────────────
# Number Theory: is_cube_number
# ──────────────────────────────────────────────

class TestAnnulusAreaV2:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import annulus_area

        assert round(annulus_area(5, 3), 4) == 50.2655

    def test_inner_ge_outer(self):
        from shortfx.fxNumeric.trigonometry_functions import annulus_area

        with pytest.raises(ValueError):
            annulus_area(3, 5)

class TestEllipseArea:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import ellipse_area

        assert round(ellipse_area(5, 3), 4) == 47.1239

    def test_negative_axis(self):
        from shortfx.fxNumeric.trigonometry_functions import ellipse_area

        with pytest.raises(ValueError):
            ellipse_area(-5, 3)

class TestEllipsePerimeter:

    def test_basic(self):
        from shortfx.fxNumeric.trigonometry_functions import ellipse_perimeter

        assert round(ellipse_perimeter(5, 3), 3) == 25.527

    def test_type_error(self):
        from shortfx.fxNumeric.trigonometry_functions import ellipse_perimeter

        with pytest.raises(TypeError):
            ellipse_perimeter("a", 3)


# ── Number Theory ────────────────────────────────────────────────────

class TestEllipseFormulas:

    def test_area(self):
        from shortfx.fxNumeric.geometry_functions import ellipse_area
        assert ellipse_area(3, 2) == pytest.approx(6 * math.pi)

    def test_eccentricity(self):
        from shortfx.fxNumeric.geometry_functions import ellipse_eccentricity
        assert ellipse_eccentricity(5, 3) == pytest.approx(0.8)

class TestPolygonFormulas:

    def test_polygon_area(self):
        from shortfx.fxNumeric.geometry_functions import polygon_area
        assert polygon_area([(0, 0), (4, 0), (4, 3), (0, 3)]) == pytest.approx(12.0)

    def test_regular_polygon(self):
        from shortfx.fxNumeric.geometry_functions import regular_polygon_area
        # Regular hexagon with side 1
        assert regular_polygon_area(6, 1) == pytest.approx(
            3 * math.sqrt(3) / 2, rel=1e-6
        )

    def test_trapezoid(self):
        from shortfx.fxNumeric.geometry_functions import trapezoid_area
        assert trapezoid_area(3, 5, 4) == pytest.approx(16.0)

class TestSphericalTrig:

    def test_haversine_distance(self):
        from shortfx.fxNumeric.geometry_functions import haversine_distance
        d = haversine_distance(40.7128, -74.0060, 51.5074, -0.1278)
        assert d == pytest.approx(5570, rel=0.01)

    def test_spherical_law_of_cosines(self):
        from shortfx.fxNumeric.geometry_functions import spherical_law_of_cosines
        c = spherical_law_of_cosines(0.5, 0.6, 1.0)
        # cos(c)=cos(0.5)cos(0.6)+sin(0.5)sin(0.6)cos(1.0) ≈ 0.8706 => c ≈ 0.5145
        assert c == pytest.approx(0.5145, rel=1e-3)

class TestVersineV2:

    def test_zero(self):
        from shortfx.fxNumeric.trigonometry_functions import versine
        assert versine(0) == pytest.approx(0.0)

    def test_pi(self):
        from shortfx.fxNumeric.trigonometry_functions import versine
        assert versine(math.pi) == pytest.approx(2.0)

class TestHaversineTrig:

    def test_zero(self):
        from shortfx.fxNumeric.trigonometry_functions import haversine_trig
        assert haversine_trig(0) == pytest.approx(0.0)

    def test_pi(self):
        from shortfx.fxNumeric.trigonometry_functions import haversine_trig
        assert haversine_trig(math.pi) == pytest.approx(1.0)

class TestExsecantV2:

    def test_zero(self):
        from shortfx.fxNumeric.trigonometry_functions import exsecant
        assert exsecant(0) == pytest.approx(0.0)

class TestCoversineV2:

    def test_zero(self):
        from shortfx.fxNumeric.trigonometry_functions import coversine
        assert coversine(0) == pytest.approx(1.0)

    def test_pi_half(self):
        from shortfx.fxNumeric.trigonometry_functions import coversine
        assert coversine(math.pi / 2) == pytest.approx(0.0, abs=1e-10)
