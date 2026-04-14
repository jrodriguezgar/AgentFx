"""Tests for fxNumeric.curves_functions."""

import math

import pytest

from formulite.fxNumeric import (
    bezier_cubic,
    bezier_quadratic,
    brachistochrone_time,
    butterfly_curve,
    cassini_oval,
    catmull_rom,
    cochleoid,
    conchoid_of_nicomedes,
    cornu_spiral,
    deltoid,
    epitrochoid,
    evolute_ellipse,
    fermat_spiral,
    gaussian_curvature_cylinder,
    gaussian_curvature_sphere,
    gaussian_curvature_torus,
    hermite_interpolation,
    hypotrochoid,
    limacon,
    lissajous,
    lituus,
    mean_curvature_sphere,
    nephroid,
    piriform,
    principal_curvatures_ellipsoid,
    superellipse,
    surface_area_revolution,
    tautochrone_period,
)
from formulite.fxNumeric import curves_functions as cf


class TestFermatSpiral:
    def test_basic(self):
        assert round(fermat_spiral(1.0, 4.0), 4) == 2.0

    def test_zero_theta(self):
        assert fermat_spiral(1.0, 0.0) == 0.0

    def test_negative_theta(self):
        with pytest.raises(ValueError):
            fermat_spiral(1.0, -1.0)

class TestCochleoid:
    def test_basic(self):
        assert round(cochleoid(1.0, 1.0), 4) == 0.8415

    def test_zero_theta(self):
        with pytest.raises(ValueError):
            cochleoid(1.0, 0.0)

class TestEvoluteEllipse:
    def test_basic(self):
        x, y = evolute_ellipse(5.0, 3.0, 0.0)
        assert x == pytest.approx(3.2)
        assert y == pytest.approx(0.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            evolute_ellipse("a", 3.0, 0.0)

class TestTautchronePeriod:
    def test_basic(self):
        assert round(tautochrone_period(1.0), 4) == 2.0064

    def test_negative(self):
        with pytest.raises(ValueError):
            tautochrone_period(-1)

class TestBrachistochroneTime:
    def test_basic(self):
        assert round(brachistochrone_time(1.0, 1.0), 3) == 0.493

    def test_large_drop(self):
        t = brachistochrone_time(1.0, 10.0)
        assert t > 0

    def test_negative(self):
        with pytest.raises(ValueError):
            brachistochrone_time(-1, 1)

class TestCornuSpiral:
    def test_basic(self):
        x, y = cornu_spiral(1.0)
        assert round(x, 4) == 0.7798

    def test_zero(self):
        x, y = cornu_spiral(0.0)
        assert x == pytest.approx(0.0, abs=1e-10)
        assert y == pytest.approx(0.0, abs=1e-10)

class TestSuperellipse:
    def test_circle(self):
        x, y = superellipse(1.0, 1.0, 2.0, 0.0)
        assert x == pytest.approx(1.0)
        assert y == pytest.approx(0.0, abs=1e-10)

    def test_quarter(self):
        x, y = superellipse(1.0, 1.0, 2.0, math.pi / 2)
        assert x == pytest.approx(0.0, abs=1e-10)
        assert y == pytest.approx(1.0)

    def test_negative_exponent(self):
        with pytest.raises(ValueError):
            superellipse(1, 1, -1, 0)

class TestHypotrochoid:
    def test_basic(self):
        x, y = hypotrochoid(5.0, 3.0, 5.0, 0.0)
        assert round(x, 4) == 7.0
        assert round(y, 4) == 0.0

    def test_negative_R(self):
        with pytest.raises(ValueError):
            hypotrochoid(-1, 3, 5, 0)

class TestEpitrochoid:
    def test_basic(self):
        x, y = epitrochoid(3.0, 1.0, 0.5, 0.0)
        assert round(x, 4) == 3.5
        assert round(y, 4) == 0.0

class TestBezierQuadratic:
    def test_midpoint(self):
        assert bezier_quadratic((0, 0), (1, 2), (2, 0), 0.5) == (1.0, 1.0)

    def test_start(self):
        assert bezier_quadratic((0, 0), (1, 2), (2, 0), 0.0) == (0.0, 0.0)

    def test_end(self):
        x, y = bezier_quadratic((0, 0), (1, 2), (2, 0), 1.0)
        assert x == pytest.approx(2.0)
        assert y == pytest.approx(0.0)

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            bezier_quadratic((0, 0), (1, 2), (2, 0), 1.5)

class TestBezierCubic:
    def test_midpoint(self):
        x, y = bezier_cubic((0, 0), (1, 3), (2, 3), (3, 0), 0.5)
        assert x == pytest.approx(1.5)
        assert y == pytest.approx(2.25)

    def test_start(self):
        assert bezier_cubic((0, 0), (1, 3), (2, 3), (3, 0), 0.0) == (0.0, 0.0)

class TestHermiteInterpolation:
    def test_midpoint(self):
        assert hermite_interpolation(0, 1, 0, 0, 0.5) == 0.5

    def test_start(self):
        assert hermite_interpolation(0, 1, 0, 0, 0.0) == 0.0

    def test_end(self):
        assert hermite_interpolation(0, 1, 0, 0, 1.0) == pytest.approx(1.0)

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            hermite_interpolation(0, 1, 0, 0, 2.0)

class TestCatmullRom:
    def test_linear(self):
        assert catmull_rom(0, 1, 2, 3, 0.5) == 1.5

    def test_start(self):
        assert catmull_rom(0, 1, 2, 3, 0.0) == pytest.approx(1.0)

    def test_end(self):
        assert catmull_rom(0, 1, 2, 3, 1.0) == pytest.approx(2.0)

class TestLituus:
    def test_unit(self):
        assert round(lituus(1.0, 1.0), 4) == 1.0

    def test_larger_theta(self):
        assert round(lituus(1.0, 4.0), 4) == 0.5

    def test_negative(self):
        with pytest.raises(ValueError):
            lituus(-1, 1)

class TestButterflyCurve:
    def test_at_zero(self):
        x, y = butterfly_curve(0.0)
        assert x == pytest.approx(0.0, abs=1e-10)
        assert round(y, 4) == 0.7183

    def test_type_error(self):
        with pytest.raises(TypeError):
            butterfly_curve("abc")

class TestCycloid:

    def test_top_of_arch(self):
        x, y = cf.cycloid(math.pi, 1.0)
        assert abs(y - 2.0) < 1e-10

    def test_origin(self):
        x, y = cf.cycloid(0, 1.0)
        assert abs(x) < 1e-10 and abs(y) < 1e-10

class TestEpicycloid:

    def test_start_point(self):
        x, y = cf.epicycloid(0, 3, 1)
        assert abs(x - 3.0) < 1e-10  # (R+r) - r = R
        assert abs(y) < 1e-10

class TestHypocycloid:

    def test_start_point(self):
        x, y = cf.hypocycloid(0, 4, 1)
        assert abs(x - 4.0) < 1e-10
        assert abs(y) < 1e-10

class TestCardioid:

    def test_rightmost_point(self):
        x, y = cf.cardioid(0, 1.0)
        assert abs(x - 2.0) < 1e-10

class TestLemniscate:

    def test_origin_point(self):
        # At t = pi/4, cos(2t) = 0, boundary
        x, y = cf.lemniscate(0, 1.0)
        assert abs(x - 1.0) < 1e-10

    def test_undefined_raises(self):
        with pytest.raises(ValueError):
            cf.lemniscate(math.pi / 2, 1.0)

class TestArchimedeanSpiral:

    def test_at_pi(self):
        x, y = cf.archimedean_spiral(math.pi, 0, 1)
        assert abs(x - (-math.pi)) < 1e-4

class TestLogarithmicSpiral:

    def test_at_zero(self):
        x, y = cf.logarithmic_spiral(0, 1, 0.2)
        assert abs(x - 1.0) < 1e-10

class TestInvoluteOfCircle:

    def test_at_zero(self):
        x, y = cf.involute_of_circle(0, 1)
        assert abs(x - 1.0) < 1e-10
        assert abs(y) < 1e-10

class TestRoseCurve:

    def test_at_zero(self):
        x, y = cf.rose_curve(0, 1, 3)
        assert abs(x - 1.0) < 1e-10

class TestAstroid:

    def test_at_zero(self):
        x, y = cf.astroid(0, 1)
        assert abs(x - 1.0) < 1e-10
        assert abs(y) < 1e-10

class TestCatenary:

    def test_at_zero(self):
        assert cf.catenary(0, 1) == 1.0

class TestTractrix:

    def test_at_pi_half(self):
        x, y = cf.tractrix(math.pi / 2, 1.0)
        assert abs(y - 1.0) < 1e-10  # y = a * sin(pi/2) = 1

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            cf.tractrix(0, 1.0)

class TestCissoid:

    def test_at_zero(self):
        x, y = cf.cissoid(0, 1.0)
        assert abs(x) < 1e-10 and abs(y) < 1e-10

class TestFoliumOfDescartes:

    def test_at_one(self):
        x, y = cf.folium_of_descartes(1, 1.0)
        assert abs(x - 1.5) < 1e-10
        assert abs(y - 1.5) < 1e-10

class TestWitchOfAgnesi:

    def test_at_zero(self):
        assert cf.witch_of_agnesi(0, 1.0) == 2.0


# ===================================================================
# Curvature and Arc Length
# ===================================================================

class TestCurvatureExplicit:

    def test_parabola_vertex(self):
        # y = x^2, κ(0) = |2| / (1 + 0)^1.5 = 2
        assert abs(cf.curvature_explicit(lambda x: x ** 2, 0) - 2.0) < 0.01

class TestCurvatureParametric:

    def test_unit_circle(self):
        # Circle curvature = 1/radius = 1
        k = cf.curvature_parametric(math.cos, math.sin, 0)
        assert abs(k - 1.0) < 0.01

class TestCurvaturePolar:

    def test_unit_circle(self):
        k = cf.curvature_polar(lambda t: 1.0, 0)
        assert abs(k - 1.0) < 0.01

class TestRadiusOfCurvature:

    def test_parabola_vertex(self):
        assert abs(cf.radius_of_curvature(lambda x: x ** 2, 0) - 0.5) < 0.01

class TestArcLengthParametric:

    def test_semicircle(self):
        length = cf.arc_length_parametric(math.cos, math.sin, 0, math.pi, 100000)
        assert abs(length - math.pi) < 0.01

class TestArcLengthPolar:

    def test_full_circle(self):
        length = cf.arc_length_polar(lambda t: 1.0, 0, 2 * math.pi, 100000)
        assert abs(length - 2 * math.pi) < 0.01

class TestArcLengthFunction:

    def test_straight_line(self):
        # y = x from 0 to 1, length = sqrt(2)
        length = cf.arc_length_function(lambda x: x, 0, 1, 10000)
        assert abs(length - math.sqrt(2)) < 0.01

class TestCycloidArcLength:

    def test_one_arch(self):
        assert cf.cycloid_arc_length(1.0) == 8.0
        assert cf.cycloid_arc_length(2.0) == 16.0


# ===================================================================
# Bessel Functions
# ===================================================================

class TestCurvesExtensions:

    def test_gaussian_curvature_sphere(self):
        assert gaussian_curvature_sphere(2) == 0.25

    def test_mean_curvature_sphere(self):
        assert mean_curvature_sphere(4) == 0.25

    def test_gaussian_curvature_cylinder(self):
        assert gaussian_curvature_cylinder(5) == 0.0

    def test_gaussian_curvature_torus(self):
        # At theta=0: cos(0)/(r(R+r)) = 1/(1*(3+1)) = 0.25
        assert abs(gaussian_curvature_torus(3, 1, 0) - 0.25) < 1e-10

    def test_principal_curvatures_sphere(self):
        # Sphere of radius 2 at equator (u=pi/2): both curvatures = 1/2
        k1, k2 = principal_curvatures_ellipsoid(2, 2, 2, math.pi / 2, 0)
        assert abs(abs(k1) - 0.5) < 0.05
        assert abs(abs(k2) - 0.5) < 0.05

    def test_surface_area_revolution_cylinder(self):
        # f(x) = 1 from 0 to 1 → 2*pi*1*1 = 2*pi
        area = surface_area_revolution(lambda x: 1.0, 0, 1, 1000)
        assert abs(area - 2 * math.pi) < 0.01

    def test_surface_area_revolution_sphere(self):
        # f(x) = sqrt(1 - x^2) from -1 to 1 → sphere surface = 4*pi
        area = surface_area_revolution(
            lambda x: math.sqrt(max(1 - x * x, 1e-15)), -0.999, 0.999, 2000
        )
        assert abs(area - 4 * math.pi) < 0.5

class TestNephroid:
    def test_at_0(self):
        x, y = nephroid(0, 1.0)
        assert round(x, 6) == 2.0
        assert round(y, 6) == 0.0

class TestDeltoid:
    def test_at_0(self):
        x, y = deltoid(0, 1.0)
        assert round(x, 6) == 3.0
        assert round(y, 6) == 0.0

class TestLimacon:
    def test_at_0(self):
        x, y = limacon(0, 1, 0.5)
        assert round(x, 6) == 1.5
        assert round(y, 6) == 0.0

class TestCassiniOval:
    def test_at_0(self):
        x, y = cassini_oval(0, 1.0, 1.5)
        assert x > 0

class TestConchoid:
    def test_at_0(self):
        x, y = conchoid_of_nicomedes(0, 1, 2)
        assert round(x, 6) == 3.0
        assert round(y, 6) == 0.0

class TestLissajous:
    def test_origin(self):
        x, y = lissajous(0, 1, 1, 3, 2, 0)
        assert round(x, 6) == 0.0
        assert round(y, 6) == 0.0

class TestPiriform:
    def test_at_0(self):
        x, y = piriform(0, 1, 1)
        assert round(x, 6) == 1.0
        assert round(y, 6) == 1.0


# ===================================================================
# Transform extensions
# ===================================================================
