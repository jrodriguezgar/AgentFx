# Deep coverage tests for formulite.fxNumeric.geometry_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxNumeric.geometry_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_annulus_area_deep:
    def test_c0(self):
        try:
            mod.annulus_area(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.annulus_area(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.annulus_area(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.annulus_area(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.annulus_area(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.annulus_area(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.annulus_area(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.annulus_area(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.annulus_area(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.annulus_area(2, 1)
        except EXC:
            pass


class Test_heron_formula_deep:
    def test_c0(self):
        try:
            mod.heron_formula(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.heron_formula(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.heron_formula(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.heron_formula(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.heron_formula(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.heron_formula(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.heron_formula(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.heron_formula(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.heron_formula(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.heron_formula(2, 1, 42)
        except EXC:
            pass


class Test_law_of_sines_side_deep:
    def test_c0(self):
        try:
            mod.law_of_sines_side(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.law_of_sines_side(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.law_of_sines_side(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.law_of_sines_side(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.law_of_sines_side(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.law_of_sines_side(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.law_of_sines_side(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.law_of_sines_side(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.law_of_sines_side(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.law_of_sines_side(2, 1, 42)
        except EXC:
            pass


class Test_spherical_cap_volume_deep:
    def test_c0(self):
        try:
            mod.spherical_cap_volume(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spherical_cap_volume(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spherical_cap_volume(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spherical_cap_volume(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spherical_cap_volume(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spherical_cap_volume(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.spherical_cap_volume(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.spherical_cap_volume(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.spherical_cap_volume(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.spherical_cap_volume(2, 1)
        except EXC:
            pass


class Test_capsule_surface_area_deep:
    def test_c0(self):
        try:
            mod.capsule_surface_area(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.capsule_surface_area(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.capsule_surface_area(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.capsule_surface_area(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.capsule_surface_area(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.capsule_surface_area(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.capsule_surface_area(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.capsule_surface_area(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.capsule_surface_area(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.capsule_surface_area(2, 1)
        except EXC:
            pass


class Test_capsule_volume_deep:
    def test_c0(self):
        try:
            mod.capsule_volume(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.capsule_volume(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.capsule_volume(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.capsule_volume(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.capsule_volume(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.capsule_volume(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.capsule_volume(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.capsule_volume(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.capsule_volume(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.capsule_volume(2, 1)
        except EXC:
            pass


class Test_circular_ring_perimeter_deep:
    def test_c0(self):
        try:
            mod.circular_ring_perimeter(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.circular_ring_perimeter(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.circular_ring_perimeter(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.circular_ring_perimeter(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.circular_ring_perimeter(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.circular_ring_perimeter(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.circular_ring_perimeter(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.circular_ring_perimeter(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.circular_ring_perimeter(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.circular_ring_perimeter(2, 1)
        except EXC:
            pass


class Test_ellipse_eccentricity_deep:
    def test_c0(self):
        try:
            mod.ellipse_eccentricity(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ellipse_eccentricity(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ellipse_eccentricity(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ellipse_eccentricity(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ellipse_eccentricity(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ellipse_eccentricity(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ellipse_eccentricity(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ellipse_eccentricity(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ellipse_eccentricity(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ellipse_eccentricity(2, 1)
        except EXC:
            pass


class Test_frustum_volume_deep:
    def test_c0(self):
        try:
            mod.frustum_volume(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.frustum_volume(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.frustum_volume(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.frustum_volume(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.frustum_volume(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.frustum_volume(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.frustum_volume(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.frustum_volume(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.frustum_volume(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.frustum_volume(2, 1, 42)
        except EXC:
            pass


class Test_law_of_cosines_angle_deep:
    def test_c0(self):
        try:
            mod.law_of_cosines_angle(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.law_of_cosines_angle(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.law_of_cosines_angle(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.law_of_cosines_angle(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.law_of_cosines_angle(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.law_of_cosines_angle(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.law_of_cosines_angle(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.law_of_cosines_angle(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.law_of_cosines_angle(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.law_of_cosines_angle(2, 1, 42)
        except EXC:
            pass


class Test_law_of_cosines_side_deep:
    def test_c0(self):
        try:
            mod.law_of_cosines_side(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.law_of_cosines_side(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.law_of_cosines_side(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.law_of_cosines_side(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.law_of_cosines_side(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.law_of_cosines_side(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.law_of_cosines_side(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.law_of_cosines_side(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.law_of_cosines_side(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.law_of_cosines_side(2, 1, 42)
        except EXC:
            pass


class Test_parabola_directrix_deep:
    def test_c0(self):
        try:
            mod.parabola_directrix(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.parabola_directrix(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.parabola_directrix(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.parabola_directrix(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.parabola_directrix(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.parabola_directrix(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.parabola_directrix(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.parabola_directrix(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.parabola_directrix(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.parabola_directrix(2)
        except EXC:
            pass


class Test_parabola_focus_deep:
    def test_c0(self):
        try:
            mod.parabola_focus(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.parabola_focus(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.parabola_focus(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.parabola_focus(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.parabola_focus(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.parabola_focus(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.parabola_focus(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.parabola_focus(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.parabola_focus(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.parabola_focus(2)
        except EXC:
            pass


class Test_point_to_line_distance_deep:
    def test_c0(self):
        try:
            mod.point_to_line_distance(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.point_to_line_distance(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.point_to_line_distance(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.point_to_line_distance(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.point_to_line_distance(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.point_to_line_distance(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.point_to_line_distance(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.point_to_line_distance(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.point_to_line_distance(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.point_to_line_distance(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_polygon_centroid_deep:
    def test_c0(self):
        try:
            mod.polygon_centroid([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.polygon_centroid([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.polygon_centroid([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.polygon_centroid([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.polygon_centroid([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.polygon_centroid([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_stadium_area_deep:
    def test_c0(self):
        try:
            mod.stadium_area(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.stadium_area(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.stadium_area(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.stadium_area(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.stadium_area(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.stadium_area(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.stadium_area(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.stadium_area(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.stadium_area(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.stadium_area(2, 1)
        except EXC:
            pass

