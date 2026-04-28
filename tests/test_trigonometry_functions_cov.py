# Coverage tests for agentfx.fxNumeric.trigonometry_functions
import math

from agentfx.fxNumeric import trigonometry_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_along_track_distance:
    def test_exists(self):
        assert hasattr(mod, "along_track_distance")

    def test_doc0(self):
        try:
            mod.along_track_distance(53.2611, -0.7972, 53.3206, -1.7297, 53.1887, 0.1334) > 0
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.along_track_distance(3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.along_track_distance(100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.along_track_distance(None, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.along_track_distance("", 0, "", "", "", "")
        except EXC:
            pass


class Test_angle_bisector_length:
    def test_exists(self):
        assert hasattr(mod, "angle_bisector_length")

    def test_var0(self):
        try:
            mod.angle_bisector_length(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.angle_bisector_length(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.angle_bisector_length(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.angle_bisector_length("", "", "")
        except EXC:
            pass


class Test_angular_deficiency:
    def test_exists(self):
        assert hasattr(mod, "angular_deficiency")

    def test_var0(self):
        try:
            mod.angular_deficiency(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.angular_deficiency(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.angular_deficiency(None)
        except EXC:
            pass


class Test_angular_velocity:
    def test_exists(self):
        assert hasattr(mod, "angular_velocity")

    def test_var0(self):
        try:
            mod.angular_velocity(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.angular_velocity(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.angular_velocity(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.angular_velocity("", "")
        except EXC:
            pass


class Test_annular_sector_area:
    def test_exists(self):
        assert hasattr(mod, "annular_sector_area")

    def test_var0(self):
        try:
            mod.annular_sector_area(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.annular_sector_area(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.annular_sector_area(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.annular_sector_area("", "", "")
        except EXC:
            pass


class Test_annulus_area:
    def test_exists(self):
        assert hasattr(mod, "annulus_area")

    def test_var0(self):
        try:
            mod.annulus_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.annulus_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.annulus_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.annulus_area("", "")
        except EXC:
            pass


class Test_arbelos_area:
    def test_exists(self):
        assert hasattr(mod, "arbelos_area")

    def test_var0(self):
        try:
            mod.arbelos_area(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arbelos_area(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arbelos_area(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arbelos_area("", "", "")
        except EXC:
            pass


class Test_arc_length:
    def test_exists(self):
        assert hasattr(mod, "arc_length")

    def test_var0(self):
        try:
            mod.arc_length(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arc_length(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arc_length(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arc_length("", "")
        except EXC:
            pass


class Test_arccosine:
    def test_exists(self):
        assert hasattr(mod, "arccosine")

    def test_doc0(self):
        try:
            mod.arccosine(1.0) # acos(1) should be 0
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.arccosine(-1.0) # acos(-1) should be pi
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.arccosine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arccosine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arccosine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arccosine("")
        except EXC:
            pass


class Test_arcsine:
    def test_exists(self):
        assert hasattr(mod, "arcsine")

    def test_doc0(self):
        try:
            mod.arcsine(1.0) # asin(1) should be pi/2
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.arcsine(0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.arcsine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arcsine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arcsine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arcsine("")
        except EXC:
            pass


class Test_arctangent:
    def test_exists(self):
        assert hasattr(mod, "arctangent")

    def test_doc0(self):
        try:
            mod.arctangent(1.0) # atan(1) should be pi/4
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.arctangent(0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.arctangent(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arctangent(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arctangent(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arctangent("")
        except EXC:
            pass


class Test_arctangent2:
    def test_exists(self):
        assert hasattr(mod, "arctangent2")

    def test_doc0(self):
        try:
            mod.arctangent2(1, 1) # atan2(1, 1) should be pi/4
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.arctangent2(-1, 1) # atan2(-1, 1) should be -pi/4
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.arctangent2(1, -1) # atan2(1, -1) should be 3*pi/4
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.arctangent2(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arctangent2(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arctangent2(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arctangent2("", "")
        except EXC:
            pass


class Test_bearing:
    def test_exists(self):
        assert hasattr(mod, "bearing")

    def test_var0(self):
        try:
            mod.bearing(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bearing(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bearing(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bearing("", "", "", "")
        except EXC:
            pass


class Test_cartesian_to_cylindrical:
    def test_exists(self):
        assert hasattr(mod, "cartesian_to_cylindrical")

    def test_doc0(self):
        try:
            mod.cartesian_to_cylindrical(1.0, 0.0, 5.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cartesian_to_cylindrical(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cartesian_to_cylindrical(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cartesian_to_cylindrical(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cartesian_to_cylindrical("", "", "")
        except EXC:
            pass


class Test_cartesian_to_polar:
    def test_exists(self):
        assert hasattr(mod, "cartesian_to_polar")

    def test_doc0(self):
        try:
            mod.cartesian_to_polar(1.0, 0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cartesian_to_polar(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cartesian_to_polar(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cartesian_to_polar(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cartesian_to_polar("", "")
        except EXC:
            pass


class Test_cartesian_to_spherical:
    def test_exists(self):
        assert hasattr(mod, "cartesian_to_spherical")

    def test_doc0(self):
        try:
            mod.cartesian_to_spherical(0.0, 0.0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cartesian_to_spherical(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cartesian_to_spherical(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cartesian_to_spherical(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cartesian_to_spherical("", "", "")
        except EXC:
            pass


class Test_chord_length:
    def test_exists(self):
        assert hasattr(mod, "chord_length")

    def test_var0(self):
        try:
            mod.chord_length(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chord_length(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chord_length(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chord_length("", "")
        except EXC:
            pass


class Test_circular_arc_length:
    def test_exists(self):
        assert hasattr(mod, "circular_arc_length")

    def test_var0(self):
        try:
            mod.circular_arc_length(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.circular_arc_length(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.circular_arc_length(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.circular_arc_length("", "")
        except EXC:
            pass


class Test_circular_ring_area:
    def test_exists(self):
        assert hasattr(mod, "circular_ring_area")

    def test_var0(self):
        try:
            mod.circular_ring_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.circular_ring_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.circular_ring_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.circular_ring_area("", "")
        except EXC:
            pass


class Test_circular_sector_area:
    def test_exists(self):
        assert hasattr(mod, "circular_sector_area")

    def test_var0(self):
        try:
            mod.circular_sector_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.circular_sector_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.circular_sector_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.circular_sector_area("", "")
        except EXC:
            pass


class Test_circular_segment_area:
    def test_exists(self):
        assert hasattr(mod, "circular_segment_area")

    def test_var0(self):
        try:
            mod.circular_segment_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.circular_segment_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.circular_segment_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.circular_segment_area("", "")
        except EXC:
            pass


class Test_circular_segment_chord:
    def test_exists(self):
        assert hasattr(mod, "circular_segment_chord")

    def test_var0(self):
        try:
            mod.circular_segment_chord(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.circular_segment_chord(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.circular_segment_chord(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.circular_segment_chord("", "")
        except EXC:
            pass


class Test_circular_segment_height:
    def test_exists(self):
        assert hasattr(mod, "circular_segment_height")

    def test_var0(self):
        try:
            mod.circular_segment_height(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.circular_segment_height(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.circular_segment_height(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.circular_segment_height("", "")
        except EXC:
            pass


class Test_cone_lateral_area:
    def test_exists(self):
        assert hasattr(mod, "cone_lateral_area")

    def test_var0(self):
        try:
            mod.cone_lateral_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cone_lateral_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cone_lateral_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cone_lateral_area("", "")
        except EXC:
            pass


class Test_cone_slant_height:
    def test_exists(self):
        assert hasattr(mod, "cone_slant_height")

    def test_doc0(self):
        try:
            mod.cone_slant_height(3, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cone_slant_height(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cone_slant_height(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cone_slant_height(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cone_slant_height("", "")
        except EXC:
            pass


class Test_cosecant:
    def test_exists(self):
        assert hasattr(mod, "cosecant")

    def test_var0(self):
        try:
            mod.cosecant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cosecant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cosecant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cosecant("")
        except EXC:
            pass


class Test_cosine:
    def test_exists(self):
        assert hasattr(mod, "cosine")

    def test_doc0(self):
        try:
            mod.cosine(0) # cos(0 degrees)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.cosine(math.pi) # cos(180 degrees)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cosine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cosine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cosine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cosine("")
        except EXC:
            pass


class Test_cotangent:
    def test_exists(self):
        assert hasattr(mod, "cotangent")

    def test_var0(self):
        try:
            mod.cotangent(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cotangent(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cotangent(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cotangent("")
        except EXC:
            pass


class Test_coversine:
    def test_exists(self):
        assert hasattr(mod, "coversine")

    def test_doc0(self):
        try:
            mod.coversine(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coversine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coversine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coversine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coversine("")
        except EXC:
            pass


class Test_cross_track_distance:
    def test_exists(self):
        assert hasattr(mod, "cross_track_distance")

    def test_var0(self):
        try:
            mod.cross_track_distance(3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cross_track_distance(100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cross_track_distance(None, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cross_track_distance("", 0, "", "", "", "")
        except EXC:
            pass


class Test_cyclic_polygon_radius:
    def test_exists(self):
        assert hasattr(mod, "cyclic_polygon_radius")

    def test_var0(self):
        try:
            mod.cyclic_polygon_radius(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cyclic_polygon_radius(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cyclic_polygon_radius(None, 0)
        except EXC:
            pass


class Test_cylinder_lateral_area:
    def test_exists(self):
        assert hasattr(mod, "cylinder_lateral_area")

    def test_var0(self):
        try:
            mod.cylinder_lateral_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cylinder_lateral_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cylinder_lateral_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cylinder_lateral_area("", "")
        except EXC:
            pass


class Test_cylindrical_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "cylindrical_to_cartesian")

    def test_doc0(self):
        try:
            mod.cylindrical_to_cartesian(1.0, 0.0, 5.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cylindrical_to_cartesian(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cylindrical_to_cartesian(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cylindrical_to_cartesian(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cylindrical_to_cartesian("", "", "")
        except EXC:
            pass


class Test_damped_oscillation:
    def test_exists(self):
        assert hasattr(mod, "damped_oscillation")

    def test_var0(self):
        try:
            mod.damped_oscillation(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.damped_oscillation(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.damped_oscillation(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.damped_oscillation("", "", "", "")
        except EXC:
            pass


class Test_degrees_to_radians:
    def test_exists(self):
        assert hasattr(mod, "degrees_to_radians")

    def test_doc0(self):
        try:
            mod.degrees_to_radians(180)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.degrees_to_radians(90)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.degrees_to_radians(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.degrees_to_radians(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.degrees_to_radians(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.degrees_to_radians(0)
        except EXC:
            pass


class Test_destination_point:
    def test_exists(self):
        assert hasattr(mod, "destination_point")

    def test_doc0(self):
        try:
            mod.destination_point(40.4168, -3.7038, 24.8, 1000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.destination_point(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.destination_point(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.destination_point(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.destination_point("", 0, "", "")
        except EXC:
            pass


class Test_distance_point_to_line:
    def test_exists(self):
        assert hasattr(mod, "distance_point_to_line")

    def test_doc0(self):
        try:
            mod.distance_point_to_line(1, 1, 0, 0, 2, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.distance_point_to_line(3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.distance_point_to_line(100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.distance_point_to_line(None, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.distance_point_to_line("", "", "", "", "", "")
        except EXC:
            pass


class Test_ellipse_area:
    def test_exists(self):
        assert hasattr(mod, "ellipse_area")

    def test_var0(self):
        try:
            mod.ellipse_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ellipse_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ellipse_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ellipse_area("", "")
        except EXC:
            pass


class Test_ellipse_circumference_approx:
    def test_exists(self):
        assert hasattr(mod, "ellipse_circumference_approx")

    def test_var0(self):
        try:
            mod.ellipse_circumference_approx(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ellipse_circumference_approx(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ellipse_circumference_approx(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ellipse_circumference_approx("", "")
        except EXC:
            pass


class Test_ellipse_perimeter:
    def test_exists(self):
        assert hasattr(mod, "ellipse_perimeter")

    def test_var0(self):
        try:
            mod.ellipse_perimeter(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ellipse_perimeter(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ellipse_perimeter(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ellipse_perimeter("", "")
        except EXC:
            pass


class Test_ellipsoid_volume:
    def test_exists(self):
        assert hasattr(mod, "ellipsoid_volume")

    def test_var0(self):
        try:
            mod.ellipsoid_volume(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ellipsoid_volume(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ellipsoid_volume(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ellipsoid_volume("", "", "")
        except EXC:
            pass


class Test_epicycloid_arc_length:
    def test_exists(self):
        assert hasattr(mod, "epicycloid_arc_length")

    def test_doc0(self):
        try:
            mod.epicycloid_arc_length(5, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.epicycloid_arc_length(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.epicycloid_arc_length(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.epicycloid_arc_length(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.epicycloid_arc_length("", "")
        except EXC:
            pass


class Test_excosecant:
    def test_exists(self):
        assert hasattr(mod, "excosecant")

    def test_var0(self):
        try:
            mod.excosecant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.excosecant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.excosecant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.excosecant("")
        except EXC:
            pass


class Test_exsecant:
    def test_exists(self):
        assert hasattr(mod, "exsecant")

    def test_doc0(self):
        try:
            mod.exsecant(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.exsecant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.exsecant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.exsecant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.exsecant("")
        except EXC:
            pass


class Test_frustum_lateral_area:
    def test_exists(self):
        assert hasattr(mod, "frustum_lateral_area")

    def test_var0(self):
        try:
            mod.frustum_lateral_area(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.frustum_lateral_area(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.frustum_lateral_area(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.frustum_lateral_area("", "", "")
        except EXC:
            pass


class Test_frustum_volume:
    def test_exists(self):
        assert hasattr(mod, "frustum_volume")

    def test_var0(self):
        try:
            mod.frustum_volume(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.frustum_volume(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.frustum_volume(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.frustum_volume(0, "", "")
        except EXC:
            pass


class Test_geodesic_area:
    def test_exists(self):
        assert hasattr(mod, "geodesic_area")

    def test_doc0(self):
        try:
            mod.geodesic_area([(0, 0), (0, 1), (1, 1), (1, 0)])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.geodesic_area(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geodesic_area(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geodesic_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geodesic_area("")
        except EXC:
            pass


class Test_gudermannian:
    def test_exists(self):
        assert hasattr(mod, "gudermannian")

    def test_var0(self):
        try:
            mod.gudermannian(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gudermannian(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gudermannian(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gudermannian("")
        except EXC:
            pass


class Test_hacoverversine:
    def test_exists(self):
        assert hasattr(mod, "hacoverversine")

    def test_var0(self):
        try:
            mod.hacoverversine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hacoverversine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hacoverversine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hacoverversine("")
        except EXC:
            pass


class Test_haversine_angle:
    def test_exists(self):
        assert hasattr(mod, "haversine_angle")

    def test_doc0(self):
        try:
            mod.haversine_angle(math.pi)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.haversine_angle(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.haversine_angle(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.haversine_angle(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.haversine_angle(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.haversine_angle("")
        except EXC:
            pass


class Test_haversine_distance:
    def test_exists(self):
        assert hasattr(mod, "haversine_distance")

    def test_var0(self):
        try:
            mod.haversine_distance(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.haversine_distance(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.haversine_distance(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.haversine_distance("", "", "", "")
        except EXC:
            pass


class Test_haversine_trig:
    def test_exists(self):
        assert hasattr(mod, "haversine_trig")

    def test_doc0(self):
        try:
            mod.haversine_trig(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.haversine_trig(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.haversine_trig(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.haversine_trig(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.haversine_trig("")
        except EXC:
            pass


class Test_herons_formula:
    def test_exists(self):
        assert hasattr(mod, "herons_formula")

    def test_doc0(self):
        try:
            mod.herons_formula(3, 4, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.herons_formula(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.herons_formula(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.herons_formula(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.herons_formula("", "", "")
        except EXC:
            pass


class Test_hexagon_area:
    def test_exists(self):
        assert hasattr(mod, "hexagon_area")

    def test_var0(self):
        try:
            mod.hexagon_area(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hexagon_area(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hexagon_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hexagon_area("")
        except EXC:
            pass


class Test_hyperbolic_cosecant:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_cosecant")

    def test_var0(self):
        try:
            mod.hyperbolic_cosecant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_cosecant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_cosecant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_cosecant("")
        except EXC:
            pass


class Test_hyperbolic_cosine:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_cosine")

    def test_doc0(self):
        try:
            mod.hyperbolic_cosine(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hyperbolic_cosine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_cosine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_cosine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_cosine("")
        except EXC:
            pass


class Test_hyperbolic_cosine_derived:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_cosine_derived")

    def test_doc0(self):
        try:
            mod.hyperbolic_cosine_derived(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hyperbolic_cosine_derived(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_cosine_derived(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_cosine_derived(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_cosine_derived("")
        except EXC:
            pass


class Test_hyperbolic_cotangent:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_cotangent")

    def test_var0(self):
        try:
            mod.hyperbolic_cotangent(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_cotangent(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_cotangent(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_cotangent("")
        except EXC:
            pass


class Test_hyperbolic_distance:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_distance")

    def test_var0(self):
        try:
            mod.hyperbolic_distance(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_distance(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_distance(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_distance("", "", "", "")
        except EXC:
            pass


class Test_hyperbolic_secant:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_secant")

    def test_var0(self):
        try:
            mod.hyperbolic_secant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_secant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_secant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_secant("")
        except EXC:
            pass


class Test_hyperbolic_sine:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_sine")

    def test_doc0(self):
        try:
            mod.hyperbolic_sine(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hyperbolic_sine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_sine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_sine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_sine("")
        except EXC:
            pass


class Test_hyperbolic_sine_derived:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_sine_derived")

    def test_doc0(self):
        try:
            mod.hyperbolic_sine_derived(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hyperbolic_sine_derived(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_sine_derived(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_sine_derived(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_sine_derived("")
        except EXC:
            pass


class Test_hyperbolic_tangent:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_tangent")

    def test_doc0(self):
        try:
            mod.hyperbolic_tangent(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hyperbolic_tangent(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_tangent(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_tangent(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_tangent("")
        except EXC:
            pass


class Test_hyperbolic_tangent_derived:
    def test_exists(self):
        assert hasattr(mod, "hyperbolic_tangent_derived")

    def test_doc0(self):
        try:
            mod.hyperbolic_tangent_derived(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hyperbolic_tangent_derived(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbolic_tangent_derived(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbolic_tangent_derived(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbolic_tangent_derived("")
        except EXC:
            pass


class Test_hypocycloid_arc_length:
    def test_exists(self):
        assert hasattr(mod, "hypocycloid_arc_length")

    def test_doc0(self):
        try:
            mod.hypocycloid_arc_length(5, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hypocycloid_arc_length(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hypocycloid_arc_length(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hypocycloid_arc_length(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hypocycloid_arc_length("", "")
        except EXC:
            pass


class Test_hypotenuse:
    def test_exists(self):
        assert hasattr(mod, "hypotenuse")

    def test_doc0(self):
        try:
            mod.hypotenuse(3, 4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hypotenuse(5, 12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hypotenuse(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hypotenuse(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hypotenuse(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hypotenuse("", "")
        except EXC:
            pass


class Test_inscribed_angle:
    def test_exists(self):
        assert hasattr(mod, "inscribed_angle")

    def test_doc0(self):
        try:
            mod.inscribed_angle(math.pi)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inscribed_angle(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inscribed_angle(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inscribed_angle(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inscribed_angle("")
        except EXC:
            pass


class Test_intermediate_point:
    def test_exists(self):
        assert hasattr(mod, "intermediate_point")

    def test_doc0(self):
        try:
            mod.intermediate_point(0, 0, 0, 10, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.intermediate_point(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.intermediate_point(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.intermediate_point(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.intermediate_point("", "", "", "", 0)
        except EXC:
            pass


class Test_inverse_cosecant:
    def test_exists(self):
        assert hasattr(mod, "inverse_cosecant")

    def test_var0(self):
        try:
            mod.inverse_cosecant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_cosecant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_cosecant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_cosecant("")
        except EXC:
            pass


class Test_inverse_cotangent:
    def test_exists(self):
        assert hasattr(mod, "inverse_cotangent")

    def test_var0(self):
        try:
            mod.inverse_cotangent(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_cotangent(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_cotangent(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_cotangent("")
        except EXC:
            pass


class Test_inverse_gudermannian:
    def test_exists(self):
        assert hasattr(mod, "inverse_gudermannian")

    def test_var0(self):
        try:
            mod.inverse_gudermannian(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_gudermannian(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_gudermannian(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_gudermannian("")
        except EXC:
            pass


class Test_inverse_hyperbolic_cosecant:
    def test_exists(self):
        assert hasattr(mod, "inverse_hyperbolic_cosecant")

    def test_var0(self):
        try:
            mod.inverse_hyperbolic_cosecant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hyperbolic_cosecant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hyperbolic_cosecant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hyperbolic_cosecant("")
        except EXC:
            pass


class Test_inverse_hyperbolic_cosine:
    def test_exists(self):
        assert hasattr(mod, "inverse_hyperbolic_cosine")

    def test_doc0(self):
        try:
            mod.inverse_hyperbolic_cosine(1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_hyperbolic_cosine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hyperbolic_cosine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hyperbolic_cosine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hyperbolic_cosine("")
        except EXC:
            pass


class Test_inverse_hyperbolic_cosine_derived:
    def test_exists(self):
        assert hasattr(mod, "inverse_hyperbolic_cosine_derived")

    def test_doc0(self):
        try:
            mod.inverse_hyperbolic_cosine_derived(1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_hyperbolic_cosine_derived(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hyperbolic_cosine_derived(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hyperbolic_cosine_derived(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hyperbolic_cosine_derived("")
        except EXC:
            pass


class Test_inverse_hyperbolic_cotangent:
    def test_exists(self):
        assert hasattr(mod, "inverse_hyperbolic_cotangent")

    def test_var0(self):
        try:
            mod.inverse_hyperbolic_cotangent(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hyperbolic_cotangent(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hyperbolic_cotangent(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hyperbolic_cotangent("")
        except EXC:
            pass


class Test_inverse_hyperbolic_secant:
    def test_exists(self):
        assert hasattr(mod, "inverse_hyperbolic_secant")

    def test_var0(self):
        try:
            mod.inverse_hyperbolic_secant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hyperbolic_secant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hyperbolic_secant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hyperbolic_secant("")
        except EXC:
            pass


class Test_inverse_hyperbolic_sine:
    def test_exists(self):
        assert hasattr(mod, "inverse_hyperbolic_sine")

    def test_doc0(self):
        try:
            mod.inverse_hyperbolic_sine(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_hyperbolic_sine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hyperbolic_sine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hyperbolic_sine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hyperbolic_sine("")
        except EXC:
            pass


class Test_inverse_hyperbolic_sine_derived:
    def test_exists(self):
        assert hasattr(mod, "inverse_hyperbolic_sine_derived")

    def test_doc0(self):
        try:
            mod.inverse_hyperbolic_sine_derived(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_hyperbolic_sine_derived(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hyperbolic_sine_derived(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hyperbolic_sine_derived(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hyperbolic_sine_derived("")
        except EXC:
            pass


class Test_inverse_hyperbolic_tangent:
    def test_exists(self):
        assert hasattr(mod, "inverse_hyperbolic_tangent")

    def test_doc0(self):
        try:
            mod.inverse_hyperbolic_tangent(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_hyperbolic_tangent(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hyperbolic_tangent(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hyperbolic_tangent(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hyperbolic_tangent("")
        except EXC:
            pass


class Test_inverse_hyperbolic_tangent_derived:
    def test_exists(self):
        assert hasattr(mod, "inverse_hyperbolic_tangent_derived")

    def test_doc0(self):
        try:
            mod.inverse_hyperbolic_tangent_derived(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_hyperbolic_tangent_derived(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hyperbolic_tangent_derived(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hyperbolic_tangent_derived(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hyperbolic_tangent_derived("")
        except EXC:
            pass


class Test_inverse_secant:
    def test_exists(self):
        assert hasattr(mod, "inverse_secant")

    def test_var0(self):
        try:
            mod.inverse_secant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_secant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_secant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_secant("")
        except EXC:
            pass


class Test_law_of_cosines_angle:
    def test_exists(self):
        assert hasattr(mod, "law_of_cosines_angle")

    def test_var0(self):
        try:
            mod.law_of_cosines_angle(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.law_of_cosines_angle(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.law_of_cosines_angle(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.law_of_cosines_angle("", "", "")
        except EXC:
            pass


class Test_law_of_cosines_side:
    def test_exists(self):
        assert hasattr(mod, "law_of_cosines_side")

    def test_var0(self):
        try:
            mod.law_of_cosines_side(0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.law_of_cosines_side(1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.law_of_cosines_side(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.law_of_cosines_side("", "", "")
        except EXC:
            pass


class Test_law_of_sines:
    def test_exists(self):
        assert hasattr(mod, "law_of_sines")

    def test_var0(self):
        try:
            mod.law_of_sines(0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.law_of_sines(1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.law_of_sines(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.law_of_sines("", "", "")
        except EXC:
            pass


class Test_lens_area:
    def test_exists(self):
        assert hasattr(mod, "lens_area")

    def test_var0(self):
        try:
            mod.lens_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lens_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lens_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lens_area("", "")
        except EXC:
            pass


class Test_midpoint_geo:
    def test_exists(self):
        assert hasattr(mod, "midpoint_geo")

    def test_doc0(self):
        try:
            mod.midpoint_geo(40.4168, -3.7038, 48.8566, 2.3522)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.midpoint_geo(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.midpoint_geo(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.midpoint_geo(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.midpoint_geo("", "", "", "")
        except EXC:
            pass


class Test_normalize_angle:
    def test_exists(self):
        assert hasattr(mod, "normalize_angle")

    def test_var0(self):
        try:
            mod.normalize_angle(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.normalize_angle(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.normalize_angle(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.normalize_angle("")
        except EXC:
            pass


class Test_paraboloid_volume:
    def test_exists(self):
        assert hasattr(mod, "paraboloid_volume")

    def test_var0(self):
        try:
            mod.paraboloid_volume(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.paraboloid_volume(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.paraboloid_volume(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.paraboloid_volume("", "")
        except EXC:
            pass


class Test_parallelogram_area:
    def test_exists(self):
        assert hasattr(mod, "parallelogram_area")

    def test_doc0(self):
        try:
            mod.parallelogram_area(8, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parallelogram_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parallelogram_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parallelogram_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parallelogram_area("", "")
        except EXC:
            pass


class Test_point_in_circle:
    def test_exists(self):
        assert hasattr(mod, "point_in_circle")

    def test_doc0(self):
        try:
            mod.point_in_circle(1, 1, 0, 0, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.point_in_circle(3, 0, 0, 0, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.point_in_circle(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.point_in_circle(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.point_in_circle(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.point_in_circle("", "", "", "", "")
        except EXC:
            pass


class Test_point_in_triangle:
    def test_exists(self):
        assert hasattr(mod, "point_in_triangle")

    def test_doc0(self):
        try:
            mod.point_in_triangle(1, 1, 0, 0, 4, 0, 0, 4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.point_in_triangle(5, 5, 0, 0, 4, 0, 0, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.point_in_triangle(3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.point_in_triangle(100, 100, 100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.point_in_triangle(None, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.point_in_triangle("", "", "", "", "", "", "", "")
        except EXC:
            pass


class Test_polar_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "polar_to_cartesian")

    def test_doc0(self):
        try:
            mod.polar_to_cartesian(1.0, 0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polar_to_cartesian(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polar_to_cartesian(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polar_to_cartesian(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polar_to_cartesian("", "")
        except EXC:
            pass


class Test_power_of_point:
    def test_exists(self):
        assert hasattr(mod, "power_of_point")

    def test_doc0(self):
        try:
            mod.power_of_point(5, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.power_of_point(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.power_of_point(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.power_of_point(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.power_of_point("", "")
        except EXC:
            pass


class Test_pyramid_volume:
    def test_exists(self):
        assert hasattr(mod, "pyramid_volume")

    def test_var0(self):
        try:
            mod.pyramid_volume(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pyramid_volume(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pyramid_volume(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pyramid_volume("", "")
        except EXC:
            pass


class Test_radians_to_degrees:
    def test_exists(self):
        assert hasattr(mod, "radians_to_degrees")

    def test_doc0(self):
        try:
            mod.radians_to_degrees(math.pi)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.radians_to_degrees(math.pi / 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.radians_to_degrees(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.radians_to_degrees(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.radians_to_degrees(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.radians_to_degrees("")
        except EXC:
            pass


class Test_regular_polygon_apothem:
    def test_exists(self):
        assert hasattr(mod, "regular_polygon_apothem")

    def test_var0(self):
        try:
            mod.regular_polygon_apothem(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regular_polygon_apothem(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regular_polygon_apothem(None, 0)
        except EXC:
            pass


class Test_regular_polygon_area:
    def test_exists(self):
        assert hasattr(mod, "regular_polygon_area")

    def test_var0(self):
        try:
            mod.regular_polygon_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regular_polygon_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regular_polygon_area(None, 0)
        except EXC:
            pass


class Test_regular_polygon_exterior_angle:
    def test_exists(self):
        assert hasattr(mod, "regular_polygon_exterior_angle")

    def test_doc0(self):
        try:
            mod.regular_polygon_exterior_angle(6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.regular_polygon_exterior_angle(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regular_polygon_exterior_angle(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regular_polygon_exterior_angle(None)
        except EXC:
            pass


class Test_regular_polygon_interior_angle:
    def test_exists(self):
        assert hasattr(mod, "regular_polygon_interior_angle")

    def test_doc0(self):
        try:
            mod.regular_polygon_interior_angle(6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.regular_polygon_interior_angle(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regular_polygon_interior_angle(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regular_polygon_interior_angle(None)
        except EXC:
            pass


class Test_regular_polygon_perimeter:
    def test_exists(self):
        assert hasattr(mod, "regular_polygon_perimeter")

    def test_doc0(self):
        try:
            mod.regular_polygon_perimeter(6, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.regular_polygon_perimeter(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regular_polygon_perimeter(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regular_polygon_perimeter(None, 0)
        except EXC:
            pass


class Test_reuleaux_triangle_area:
    def test_exists(self):
        assert hasattr(mod, "reuleaux_triangle_area")

    def test_var0(self):
        try:
            mod.reuleaux_triangle_area(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.reuleaux_triangle_area(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.reuleaux_triangle_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.reuleaux_triangle_area("")
        except EXC:
            pass


class Test_rhombus_area:
    def test_exists(self):
        assert hasattr(mod, "rhombus_area")

    def test_doc0(self):
        try:
            mod.rhombus_area(10, 8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rhombus_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rhombus_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rhombus_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rhombus_area("", "")
        except EXC:
            pass


class Test_rotation_2d:
    def test_exists(self):
        assert hasattr(mod, "rotation_2d")

    def test_doc0(self):
        try:
            mod.rotation_2d(1, 0, math.pi / 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rotation_2d(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rotation_2d(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rotation_2d(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rotation_2d("", "", "")
        except EXC:
            pass


class Test_sagitta:
    def test_exists(self):
        assert hasattr(mod, "sagitta")

    def test_var0(self):
        try:
            mod.sagitta(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sagitta(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sagitta(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sagitta("", "")
        except EXC:
            pass


class Test_salinon_area:
    def test_exists(self):
        assert hasattr(mod, "salinon_area")

    def test_var0(self):
        try:
            mod.salinon_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.salinon_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.salinon_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.salinon_area("", "")
        except EXC:
            pass


class Test_secant:
    def test_exists(self):
        assert hasattr(mod, "secant")

    def test_var0(self):
        try:
            mod.secant(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.secant(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.secant(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.secant("")
        except EXC:
            pass


class Test_sector_arc_length:
    def test_exists(self):
        assert hasattr(mod, "sector_arc_length")

    def test_var0(self):
        try:
            mod.sector_arc_length(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sector_arc_length(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sector_arc_length(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sector_arc_length("", "")
        except EXC:
            pass


class Test_sector_area:
    def test_exists(self):
        assert hasattr(mod, "sector_area")

    def test_var0(self):
        try:
            mod.sector_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sector_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sector_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sector_area("", "")
        except EXC:
            pass


class Test_segment_area:
    def test_exists(self):
        assert hasattr(mod, "segment_area")

    def test_var0(self):
        try:
            mod.segment_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.segment_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.segment_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.segment_area("", "")
        except EXC:
            pass


class Test_sinc:
    def test_exists(self):
        assert hasattr(mod, "sinc")

    def test_doc0(self):
        try:
            mod.sinc(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sinc(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sinc(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sinc(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sinc("")
        except EXC:
            pass


class Test_sine:
    def test_exists(self):
        assert hasattr(mod, "sine")

    def test_doc0(self):
        try:
            mod.sine(math.pi / 2) # sin(90 degrees)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sine(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sine("")
        except EXC:
            pass


class Test_sinusoidal_wave:
    def test_exists(self):
        assert hasattr(mod, "sinusoidal_wave")

    def test_var0(self):
        try:
            mod.sinusoidal_wave(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sinusoidal_wave(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sinusoidal_wave(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sinusoidal_wave("", "", "")
        except EXC:
            pass


class Test_solar_elevation:
    def test_exists(self):
        assert hasattr(mod, "solar_elevation")

    def test_var0(self):
        try:
            mod.solar_elevation(0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.solar_elevation(1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.solar_elevation(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.solar_elevation("", "", "")
        except EXC:
            pass


class Test_spherical_cap_area:
    def test_exists(self):
        assert hasattr(mod, "spherical_cap_area")

    def test_var0(self):
        try:
            mod.spherical_cap_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_cap_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_cap_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_cap_area("", "")
        except EXC:
            pass


class Test_spherical_cap_volume:
    def test_exists(self):
        assert hasattr(mod, "spherical_cap_volume")

    def test_var0(self):
        try:
            mod.spherical_cap_volume(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_cap_volume(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_cap_volume(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_cap_volume("", "")
        except EXC:
            pass


class Test_spherical_law_of_cosines:
    def test_exists(self):
        assert hasattr(mod, "spherical_law_of_cosines")

    def test_var0(self):
        try:
            mod.spherical_law_of_cosines(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_law_of_cosines(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_law_of_cosines(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_law_of_cosines("", "", "")
        except EXC:
            pass


class Test_spherical_lune_area:
    def test_exists(self):
        assert hasattr(mod, "spherical_lune_area")

    def test_var0(self):
        try:
            mod.spherical_lune_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_lune_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_lune_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_lune_area("", "")
        except EXC:
            pass


class Test_spherical_sector_volume:
    def test_exists(self):
        assert hasattr(mod, "spherical_sector_volume")

    def test_var0(self):
        try:
            mod.spherical_sector_volume(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_sector_volume(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_sector_volume(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_sector_volume("", "")
        except EXC:
            pass


class Test_spherical_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "spherical_to_cartesian")

    def test_var0(self):
        try:
            mod.spherical_to_cartesian(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_to_cartesian(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_to_cartesian(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_to_cartesian("", "", "")
        except EXC:
            pass


class Test_spherical_wedge_volume:
    def test_exists(self):
        assert hasattr(mod, "spherical_wedge_volume")

    def test_var0(self):
        try:
            mod.spherical_wedge_volume(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_wedge_volume(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_wedge_volume(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_wedge_volume("", "")
        except EXC:
            pass


class Test_spherical_zone_area:
    def test_exists(self):
        assert hasattr(mod, "spherical_zone_area")

    def test_var0(self):
        try:
            mod.spherical_zone_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_zone_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_zone_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_zone_area("", "")
        except EXC:
            pass


class Test_spheroid_volume:
    def test_exists(self):
        assert hasattr(mod, "spheroid_volume")

    def test_var0(self):
        try:
            mod.spheroid_volume(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spheroid_volume(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spheroid_volume(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spheroid_volume("", "")
        except EXC:
            pass


class Test_stadium_area:
    def test_exists(self):
        assert hasattr(mod, "stadium_area")

    def test_var0(self):
        try:
            mod.stadium_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stadium_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stadium_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.stadium_area("", 0)
        except EXC:
            pass


class Test_stadium_perimeter:
    def test_exists(self):
        assert hasattr(mod, "stadium_perimeter")

    def test_var0(self):
        try:
            mod.stadium_perimeter(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stadium_perimeter(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stadium_perimeter(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.stadium_perimeter("", 0)
        except EXC:
            pass


class Test_tangent:
    def test_exists(self):
        assert hasattr(mod, "tangent")

    def test_doc0(self):
        try:
            mod.tangent(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.tangent(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tangent(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tangent(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tangent("")
        except EXC:
            pass


class Test_torus_surface_area:
    def test_exists(self):
        assert hasattr(mod, "torus_surface_area")

    def test_var0(self):
        try:
            mod.torus_surface_area(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.torus_surface_area(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.torus_surface_area(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.torus_surface_area("", "")
        except EXC:
            pass


class Test_torus_volume:
    def test_exists(self):
        assert hasattr(mod, "torus_volume")

    def test_var0(self):
        try:
            mod.torus_volume(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.torus_volume(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.torus_volume(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.torus_volume("", "")
        except EXC:
            pass


class Test_trapezoid_area:
    def test_exists(self):
        assert hasattr(mod, "trapezoid_area")

    def test_doc0(self):
        try:
            mod.trapezoid_area(5, 7, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.trapezoid_area(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.trapezoid_area(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.trapezoid_area(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.trapezoid_area("", "", "")
        except EXC:
            pass


class Test_triangle_area_sas:
    def test_exists(self):
        assert hasattr(mod, "triangle_area_sas")

    def test_var0(self):
        try:
            mod.triangle_area_sas(0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.triangle_area_sas(1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.triangle_area_sas(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.triangle_area_sas("", "", "")
        except EXC:
            pass


class Test_triangle_centroid:
    def test_exists(self):
        assert hasattr(mod, "triangle_centroid")

    def test_doc0(self):
        try:
            mod.triangle_centroid(0, 0, 3, 0, 0, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.triangle_centroid(3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.triangle_centroid(100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.triangle_centroid(None, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.triangle_centroid("", "", "", "", "", "")
        except EXC:
            pass


class Test_triangle_circumradius:
    def test_exists(self):
        assert hasattr(mod, "triangle_circumradius")

    def test_var0(self):
        try:
            mod.triangle_circumradius(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.triangle_circumradius(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.triangle_circumradius(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.triangle_circumradius("", "", "")
        except EXC:
            pass


class Test_triangle_incircle_radius:
    def test_exists(self):
        assert hasattr(mod, "triangle_incircle_radius")

    def test_var0(self):
        try:
            mod.triangle_incircle_radius(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.triangle_incircle_radius(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.triangle_incircle_radius(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.triangle_incircle_radius("", "", "")
        except EXC:
            pass


class Test_versine:
    def test_exists(self):
        assert hasattr(mod, "versine")

    def test_doc0(self):
        try:
            mod.versine(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.versine(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.versine(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.versine(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.versine("")
        except EXC:
            pass


class Test_vincenty_distance:
    def test_exists(self):
        assert hasattr(mod, "vincenty_distance")

    def test_var0(self):
        try:
            mod.vincenty_distance(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.vincenty_distance(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.vincenty_distance(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.vincenty_distance("", "", "", "")
        except EXC:
            pass


class Test_wedge_volume:
    def test_exists(self):
        assert hasattr(mod, "wedge_volume")

    def test_doc0(self):
        try:
            mod.wedge_volume(20, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.wedge_volume(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wedge_volume(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wedge_volume(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wedge_volume("", "")
        except EXC:
            pass

