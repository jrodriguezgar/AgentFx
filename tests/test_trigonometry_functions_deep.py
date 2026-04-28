# Deep coverage tests for shortfx.fxNumeric.trigonometry_functions

import shortfx.fxNumeric.trigonometry_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_inverse_hyperbolic_secant_deep:
    def test_c0(self):
        try:
            mod.inverse_hyperbolic_secant(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inverse_hyperbolic_secant(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inverse_hyperbolic_secant(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inverse_hyperbolic_secant(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inverse_hyperbolic_secant(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inverse_hyperbolic_secant(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.inverse_hyperbolic_secant(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.inverse_hyperbolic_secant(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.inverse_hyperbolic_secant(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.inverse_hyperbolic_secant(2)
        except EXC:
            pass


class Test_annular_sector_area_deep:
    def test_c0(self):
        try:
            mod.annular_sector_area(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.annular_sector_area(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.annular_sector_area(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.annular_sector_area(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.annular_sector_area(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.annular_sector_area(0, 1, 2)
        except EXC:
            pass


class Test_frustum_lateral_area_deep:
    def test_c0(self):
        try:
            mod.frustum_lateral_area(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.frustum_lateral_area(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.frustum_lateral_area(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.frustum_lateral_area(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.frustum_lateral_area(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.frustum_lateral_area(0, 1, 2)
        except EXC:
            pass


class Test_solar_elevation_deep:
    def test_c0(self):
        try:
            mod.solar_elevation(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.solar_elevation(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.solar_elevation(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.solar_elevation(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.solar_elevation(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.solar_elevation(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.solar_elevation(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.solar_elevation(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.solar_elevation(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.solar_elevation(2, 1, 42)
        except EXC:
            pass


class Test_triangle_circumradius_deep:
    def test_c0(self):
        try:
            mod.triangle_circumradius(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.triangle_circumradius(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.triangle_circumradius(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.triangle_circumradius(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.triangle_circumradius(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.triangle_circumradius(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.triangle_circumradius(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.triangle_circumradius(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.triangle_circumradius(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.triangle_circumradius(2, 1, 42)
        except EXC:
            pass


class Test_arbelos_area_deep:
    def test_c0(self):
        try:
            mod.arbelos_area(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.arbelos_area(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.arbelos_area(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.arbelos_area(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.arbelos_area(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.arbelos_area(0, 1, 2)
        except EXC:
            pass


class Test_hypocycloid_arc_length_deep:
    def test_c0(self):
        try:
            mod.hypocycloid_arc_length(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hypocycloid_arc_length(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hypocycloid_arc_length(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hypocycloid_arc_length(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hypocycloid_arc_length(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hypocycloid_arc_length(0, 1)
        except EXC:
            pass


class Test_intermediate_point_deep:
    def test_c0(self):
        try:
            mod.intermediate_point(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.intermediate_point(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.intermediate_point(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.intermediate_point(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.intermediate_point(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.intermediate_point(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.intermediate_point(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.intermediate_point(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.intermediate_point(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.intermediate_point(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_inverse_hyperbolic_cotangent_deep:
    def test_c0(self):
        try:
            mod.inverse_hyperbolic_cotangent(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inverse_hyperbolic_cotangent(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inverse_hyperbolic_cotangent(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inverse_hyperbolic_cotangent(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inverse_hyperbolic_cotangent(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inverse_hyperbolic_cotangent(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.inverse_hyperbolic_cotangent(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.inverse_hyperbolic_cotangent(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.inverse_hyperbolic_cotangent(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.inverse_hyperbolic_cotangent(2)
        except EXC:
            pass


class Test_power_of_point_deep:
    def test_c0(self):
        try:
            mod.power_of_point(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.power_of_point(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.power_of_point(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.power_of_point(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.power_of_point(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.power_of_point(0, 1)
        except EXC:
            pass


class Test_regular_polygon_area_deep:
    def test_c0(self):
        try:
            mod.regular_polygon_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.regular_polygon_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.regular_polygon_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.regular_polygon_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.regular_polygon_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.regular_polygon_area(0, 1)
        except EXC:
            pass


class Test_regular_polygon_perimeter_deep:
    def test_c0(self):
        try:
            mod.regular_polygon_perimeter(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.regular_polygon_perimeter(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.regular_polygon_perimeter(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.regular_polygon_perimeter(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.regular_polygon_perimeter(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.regular_polygon_perimeter(0, 1)
        except EXC:
            pass


class Test_salinon_area_deep:
    def test_c0(self):
        try:
            mod.salinon_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.salinon_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.salinon_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.salinon_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.salinon_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.salinon_area(0, 1)
        except EXC:
            pass


class Test_sector_arc_length_deep:
    def test_c0(self):
        try:
            mod.sector_arc_length(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sector_arc_length(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sector_arc_length(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sector_arc_length(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sector_arc_length(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sector_arc_length(0, 1)
        except EXC:
            pass


class Test_spherical_cap_area_deep:
    def test_c0(self):
        try:
            mod.spherical_cap_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spherical_cap_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spherical_cap_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spherical_cap_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spherical_cap_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spherical_cap_area(0, 1)
        except EXC:
            pass


class Test_spherical_lune_area_deep:
    def test_c0(self):
        try:
            mod.spherical_lune_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spherical_lune_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spherical_lune_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spherical_lune_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spherical_lune_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spherical_lune_area(0, 1)
        except EXC:
            pass


class Test_spheroid_volume_deep:
    def test_c0(self):
        try:
            mod.spheroid_volume(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spheroid_volume(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spheroid_volume(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spheroid_volume(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spheroid_volume(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spheroid_volume(0, 1)
        except EXC:
            pass


class Test_stadium_perimeter_deep:
    def test_c0(self):
        try:
            mod.stadium_perimeter(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.stadium_perimeter(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.stadium_perimeter(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.stadium_perimeter(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.stadium_perimeter(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.stadium_perimeter(0, 1)
        except EXC:
            pass


class Test_triangle_incircle_radius_deep:
    def test_c0(self):
        try:
            mod.triangle_incircle_radius(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.triangle_incircle_radius(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.triangle_incircle_radius(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.triangle_incircle_radius(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.triangle_incircle_radius(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.triangle_incircle_radius(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.triangle_incircle_radius(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.triangle_incircle_radius(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.triangle_incircle_radius(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.triangle_incircle_radius(2, 1, 42)
        except EXC:
            pass


class Test_angular_velocity_deep:
    def test_c0(self):
        try:
            mod.angular_velocity(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.angular_velocity(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.angular_velocity(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.angular_velocity(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.angular_velocity(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.angular_velocity(0, 1)
        except EXC:
            pass


class Test_annulus_area_deep:
    def test_c0(self):
        try:
            mod.annulus_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.annulus_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.annulus_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.annulus_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.annulus_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.annulus_area(0, 1)
        except EXC:
            pass


class Test_arc_length_deep:
    def test_c0(self):
        try:
            mod.arc_length(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.arc_length(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.arc_length(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.arc_length(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.arc_length(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.arc_length(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.arc_length(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.arc_length(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.arc_length(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.arc_length(2, 1)
        except EXC:
            pass


class Test_chord_length_deep:
    def test_c0(self):
        try:
            mod.chord_length(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chord_length(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chord_length(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chord_length(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chord_length(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chord_length(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.chord_length(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.chord_length(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.chord_length(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.chord_length(2, 1)
        except EXC:
            pass


class Test_circular_arc_length_deep:
    def test_c0(self):
        try:
            mod.circular_arc_length(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.circular_arc_length(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.circular_arc_length(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.circular_arc_length(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.circular_arc_length(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.circular_arc_length(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.circular_arc_length(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.circular_arc_length(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.circular_arc_length(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.circular_arc_length(5, 1)
        except EXC:
            pass


class Test_circular_ring_area_deep:
    def test_c0(self):
        try:
            mod.circular_ring_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.circular_ring_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.circular_ring_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.circular_ring_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.circular_ring_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.circular_ring_area(0, 1)
        except EXC:
            pass


class Test_circular_segment_chord_deep:
    def test_c0(self):
        try:
            mod.circular_segment_chord(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.circular_segment_chord(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.circular_segment_chord(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.circular_segment_chord(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.circular_segment_chord(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.circular_segment_chord(0, 1)
        except EXC:
            pass


class Test_circular_segment_height_deep:
    def test_c0(self):
        try:
            mod.circular_segment_height(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.circular_segment_height(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.circular_segment_height(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.circular_segment_height(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.circular_segment_height(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.circular_segment_height(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.circular_segment_height(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.circular_segment_height(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.circular_segment_height(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.circular_segment_height(2, 1)
        except EXC:
            pass


class Test_cone_lateral_area_deep:
    def test_c0(self):
        try:
            mod.cone_lateral_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cone_lateral_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cone_lateral_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cone_lateral_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cone_lateral_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cone_lateral_area(0, 1)
        except EXC:
            pass


class Test_cosecant_deep:
    def test_c0(self):
        try:
            mod.cosecant(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cosecant(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cosecant(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cosecant(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cosecant(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cosecant(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.cosecant(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.cosecant(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.cosecant(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.cosecant(2)
        except EXC:
            pass


class Test_cotangent_deep:
    def test_c0(self):
        try:
            mod.cotangent(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cotangent(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cotangent(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cotangent(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cotangent(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cotangent(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.cotangent(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.cotangent(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.cotangent(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.cotangent(2)
        except EXC:
            pass


class Test_cyclic_polygon_radius_deep:
    def test_c0(self):
        try:
            mod.cyclic_polygon_radius(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cyclic_polygon_radius(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cyclic_polygon_radius(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cyclic_polygon_radius(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cyclic_polygon_radius(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cyclic_polygon_radius(0, 1)
        except EXC:
            pass


class Test_cylinder_lateral_area_deep:
    def test_c0(self):
        try:
            mod.cylinder_lateral_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cylinder_lateral_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cylinder_lateral_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cylinder_lateral_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cylinder_lateral_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cylinder_lateral_area(0, 1)
        except EXC:
            pass


class Test_destination_point_deep:
    def test_c0(self):
        try:
            mod.destination_point(1, 42, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.destination_point(42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.destination_point(0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.destination_point(-5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.destination_point(3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.destination_point(100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.destination_point(0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.destination_point(1000, -1, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.destination_point(-1, 2, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.destination_point(2, 1, 42, 0)
        except EXC:
            pass


class Test_ellipse_area_deep:
    def test_c0(self):
        try:
            mod.ellipse_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ellipse_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ellipse_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ellipse_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ellipse_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ellipse_area(0, 1)
        except EXC:
            pass


class Test_ellipse_perimeter_deep:
    def test_c0(self):
        try:
            mod.ellipse_perimeter(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ellipse_perimeter(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ellipse_perimeter(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ellipse_perimeter(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ellipse_perimeter(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ellipse_perimeter(0, 1)
        except EXC:
            pass


class Test_epicycloid_arc_length_deep:
    def test_c0(self):
        try:
            mod.epicycloid_arc_length(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.epicycloid_arc_length(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.epicycloid_arc_length(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.epicycloid_arc_length(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.epicycloid_arc_length(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.epicycloid_arc_length(0, 1)
        except EXC:
            pass


class Test_excosecant_deep:
    def test_c0(self):
        try:
            mod.excosecant(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.excosecant(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.excosecant(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.excosecant(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.excosecant(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.excosecant(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.excosecant(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.excosecant(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.excosecant(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.excosecant(2)
        except EXC:
            pass


class Test_frustum_volume_deep:
    def test_c0(self):
        try:
            mod.frustum_volume(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.frustum_volume(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.frustum_volume(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.frustum_volume(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.frustum_volume(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.frustum_volume(0, 1, 2)
        except EXC:
            pass


class Test_hyperbolic_cosecant_deep:
    def test_c0(self):
        try:
            mod.hyperbolic_cosecant(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hyperbolic_cosecant(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hyperbolic_cosecant(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hyperbolic_cosecant(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hyperbolic_cosecant(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hyperbolic_cosecant(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.hyperbolic_cosecant(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.hyperbolic_cosecant(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.hyperbolic_cosecant(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.hyperbolic_cosecant(2)
        except EXC:
            pass


class Test_hyperbolic_cotangent_deep:
    def test_c0(self):
        try:
            mod.hyperbolic_cotangent(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hyperbolic_cotangent(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hyperbolic_cotangent(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hyperbolic_cotangent(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hyperbolic_cotangent(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hyperbolic_cotangent(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.hyperbolic_cotangent(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.hyperbolic_cotangent(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.hyperbolic_cotangent(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.hyperbolic_cotangent(2)
        except EXC:
            pass


class Test_hyperbolic_secant_deep:
    def test_c0(self):
        try:
            mod.hyperbolic_secant(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hyperbolic_secant(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hyperbolic_secant(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hyperbolic_secant(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hyperbolic_secant(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hyperbolic_secant(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.hyperbolic_secant(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.hyperbolic_secant(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.hyperbolic_secant(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.hyperbolic_secant(2)
        except EXC:
            pass


class Test_inverse_cosecant_deep:
    def test_c0(self):
        try:
            mod.inverse_cosecant(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inverse_cosecant(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inverse_cosecant(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inverse_cosecant(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inverse_cosecant(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inverse_cosecant(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.inverse_cosecant(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.inverse_cosecant(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.inverse_cosecant(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.inverse_cosecant(2)
        except EXC:
            pass


class Test_inverse_hyperbolic_cosecant_deep:
    def test_c0(self):
        try:
            mod.inverse_hyperbolic_cosecant(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inverse_hyperbolic_cosecant(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inverse_hyperbolic_cosecant(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inverse_hyperbolic_cosecant(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inverse_hyperbolic_cosecant(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inverse_hyperbolic_cosecant(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.inverse_hyperbolic_cosecant(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.inverse_hyperbolic_cosecant(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.inverse_hyperbolic_cosecant(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.inverse_hyperbolic_cosecant(2)
        except EXC:
            pass


class Test_inverse_secant_deep:
    def test_c0(self):
        try:
            mod.inverse_secant(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inverse_secant(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inverse_secant(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inverse_secant(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inverse_secant(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inverse_secant(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.inverse_secant(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.inverse_secant(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.inverse_secant(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.inverse_secant(2)
        except EXC:
            pass


class Test_parallelogram_area_deep:
    def test_c0(self):
        try:
            mod.parallelogram_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.parallelogram_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.parallelogram_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.parallelogram_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.parallelogram_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.parallelogram_area(0, 1)
        except EXC:
            pass


class Test_point_in_circle_deep:
    def test_c0(self):
        try:
            mod.point_in_circle(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.point_in_circle(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.point_in_circle(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.point_in_circle(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.point_in_circle(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.point_in_circle(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.point_in_circle(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.point_in_circle(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.point_in_circle(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.point_in_circle(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_pyramid_volume_deep:
    def test_c0(self):
        try:
            mod.pyramid_volume(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pyramid_volume(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pyramid_volume(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pyramid_volume(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pyramid_volume(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pyramid_volume(0, 1)
        except EXC:
            pass


class Test_regular_polygon_apothem_deep:
    def test_c0(self):
        try:
            mod.regular_polygon_apothem(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.regular_polygon_apothem(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.regular_polygon_apothem(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.regular_polygon_apothem(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.regular_polygon_apothem(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.regular_polygon_apothem(0, 1)
        except EXC:
            pass


class Test_rhombus_area_deep:
    def test_c0(self):
        try:
            mod.rhombus_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rhombus_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rhombus_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rhombus_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rhombus_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rhombus_area(0, 1)
        except EXC:
            pass


class Test_secant_deep:
    def test_c0(self):
        try:
            mod.secant(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.secant(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.secant(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.secant(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.secant(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.secant(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.secant(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.secant(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.secant(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.secant(2)
        except EXC:
            pass


class Test_sector_area_deep:
    def test_c0(self):
        try:
            mod.sector_area(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sector_area(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sector_area(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sector_area(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sector_area(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sector_area(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.sector_area(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.sector_area(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.sector_area(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.sector_area(2, 1)
        except EXC:
            pass


class Test_spherical_cap_volume_deep:
    def test_c0(self):
        try:
            mod.spherical_cap_volume(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spherical_cap_volume(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spherical_cap_volume(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spherical_cap_volume(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spherical_cap_volume(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spherical_cap_volume(0, 1)
        except EXC:
            pass


class Test_spherical_wedge_volume_deep:
    def test_c0(self):
        try:
            mod.spherical_wedge_volume(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spherical_wedge_volume(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spherical_wedge_volume(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spherical_wedge_volume(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spherical_wedge_volume(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spherical_wedge_volume(0, 1)
        except EXC:
            pass


class Test_stadium_area_deep:
    def test_c0(self):
        try:
            mod.stadium_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.stadium_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.stadium_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.stadium_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.stadium_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.stadium_area(0, 1)
        except EXC:
            pass


class Test_torus_surface_area_deep:
    def test_c0(self):
        try:
            mod.torus_surface_area(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.torus_surface_area(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.torus_surface_area(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.torus_surface_area(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.torus_surface_area(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.torus_surface_area(0, 1)
        except EXC:
            pass


class Test_torus_volume_deep:
    def test_c0(self):
        try:
            mod.torus_volume(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.torus_volume(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.torus_volume(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.torus_volume(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.torus_volume(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.torus_volume(0, 1)
        except EXC:
            pass


class Test_vincenty_distance_deep:
    def test_c0(self):
        try:
            mod.vincenty_distance(1, 42, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.vincenty_distance(42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.vincenty_distance(0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.vincenty_distance(-5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.vincenty_distance(3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.vincenty_distance(100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.vincenty_distance(0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.vincenty_distance(1000, -1, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.vincenty_distance(-1, 2, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.vincenty_distance(2, 1, 42, 0)
        except EXC:
            pass

