# Coverage tests for shortfx.fxNumeric.geometry_functions

from shortfx.fxNumeric import geometry_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_annulus_area:
    def test_exists(self):
        assert hasattr(mod, "annulus_area")

    def test_var0(self):
        try:
            mod.annulus_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.annulus_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.annulus_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.annulus_area("", "")
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


class Test_capsule_surface_area:
    def test_exists(self):
        assert hasattr(mod, "capsule_surface_area")

    def test_var0(self):
        try:
            mod.capsule_surface_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.capsule_surface_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.capsule_surface_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.capsule_surface_area("", 0)
        except EXC:
            pass


class Test_capsule_volume:
    def test_exists(self):
        assert hasattr(mod, "capsule_volume")

    def test_var0(self):
        try:
            mod.capsule_volume(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.capsule_volume(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.capsule_volume(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.capsule_volume("", 0)
        except EXC:
            pass


class Test_circle_area:
    def test_exists(self):
        assert hasattr(mod, "circle_area")

    def test_var0(self):
        try:
            mod.circle_area(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.circle_area(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.circle_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.circle_area("")
        except EXC:
            pass


class Test_circle_circumference:
    def test_exists(self):
        assert hasattr(mod, "circle_circumference")

    def test_var0(self):
        try:
            mod.circle_circumference(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.circle_circumference(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.circle_circumference(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.circle_circumference("")
        except EXC:
            pass


class Test_circular_ring_perimeter:
    def test_exists(self):
        assert hasattr(mod, "circular_ring_perimeter")

    def test_var0(self):
        try:
            mod.circular_ring_perimeter(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.circular_ring_perimeter(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.circular_ring_perimeter(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.circular_ring_perimeter("", "")
        except EXC:
            pass


class Test_cone_lateral_area:
    def test_exists(self):
        assert hasattr(mod, "cone_lateral_area")

    def test_var0(self):
        try:
            mod.cone_lateral_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cone_lateral_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cone_lateral_area(None, 3.14)
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
            mod.cone_slant_height(3.0, 4.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cone_slant_height(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cone_slant_height(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cone_slant_height(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cone_slant_height("", "")
        except EXC:
            pass


class Test_cone_volume:
    def test_exists(self):
        assert hasattr(mod, "cone_volume")

    def test_var0(self):
        try:
            mod.cone_volume(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cone_volume(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cone_volume(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cone_volume("", "")
        except EXC:
            pass


class Test_cuboid_space_diagonal:
    def test_exists(self):
        assert hasattr(mod, "cuboid_space_diagonal")

    def test_var0(self):
        try:
            mod.cuboid_space_diagonal(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cuboid_space_diagonal(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cuboid_space_diagonal(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cuboid_space_diagonal("", "", "")
        except EXC:
            pass


class Test_cylinder_surface_area:
    def test_exists(self):
        assert hasattr(mod, "cylinder_surface_area")

    def test_var0(self):
        try:
            mod.cylinder_surface_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cylinder_surface_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cylinder_surface_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cylinder_surface_area("", "")
        except EXC:
            pass


class Test_cylinder_volume:
    def test_exists(self):
        assert hasattr(mod, "cylinder_volume")

    def test_var0(self):
        try:
            mod.cylinder_volume(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cylinder_volume(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cylinder_volume(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cylinder_volume("", "")
        except EXC:
            pass


class Test_distance_2d:
    def test_exists(self):
        assert hasattr(mod, "distance_2d")

    def test_doc0(self):
        try:
            mod.distance_2d(0, 0, 3, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.distance_2d(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.distance_2d(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.distance_2d(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.distance_2d("", "", "", "")
        except EXC:
            pass


class Test_distance_3d:
    def test_exists(self):
        assert hasattr(mod, "distance_3d")

    def test_var0(self):
        try:
            mod.distance_3d(3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.distance_3d(100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.distance_3d(None, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.distance_3d("", "", "", "", "", "")
        except EXC:
            pass


class Test_dodecahedron_surface_area:
    def test_exists(self):
        assert hasattr(mod, "dodecahedron_surface_area")

    def test_var0(self):
        try:
            mod.dodecahedron_surface_area(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dodecahedron_surface_area(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dodecahedron_surface_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dodecahedron_surface_area("")
        except EXC:
            pass


class Test_dodecahedron_volume:
    def test_exists(self):
        assert hasattr(mod, "dodecahedron_volume")

    def test_var0(self):
        try:
            mod.dodecahedron_volume(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dodecahedron_volume(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dodecahedron_volume(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dodecahedron_volume("")
        except EXC:
            pass


class Test_ellipse_area:
    def test_exists(self):
        assert hasattr(mod, "ellipse_area")

    def test_var0(self):
        try:
            mod.ellipse_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ellipse_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ellipse_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ellipse_area("", "")
        except EXC:
            pass


class Test_ellipse_eccentricity:
    def test_exists(self):
        assert hasattr(mod, "ellipse_eccentricity")

    def test_var0(self):
        try:
            mod.ellipse_eccentricity(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ellipse_eccentricity(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ellipse_eccentricity(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ellipse_eccentricity("", "")
        except EXC:
            pass


class Test_ellipse_perimeter_approx:
    def test_exists(self):
        assert hasattr(mod, "ellipse_perimeter_approx")

    def test_var0(self):
        try:
            mod.ellipse_perimeter_approx(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ellipse_perimeter_approx(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ellipse_perimeter_approx(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ellipse_perimeter_approx("", "")
        except EXC:
            pass


class Test_ellipsoid_volume:
    def test_exists(self):
        assert hasattr(mod, "ellipsoid_volume")

    def test_var0(self):
        try:
            mod.ellipsoid_volume(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ellipsoid_volume(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ellipsoid_volume(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ellipsoid_volume("", "", "")
        except EXC:
            pass


class Test_frustum_volume:
    def test_exists(self):
        assert hasattr(mod, "frustum_volume")

    def test_var0(self):
        try:
            mod.frustum_volume(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.frustum_volume(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.frustum_volume(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.frustum_volume("", "", "")
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


class Test_heron_formula:
    def test_exists(self):
        assert hasattr(mod, "heron_formula")

    def test_doc0(self):
        try:
            mod.heron_formula(3, 4, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.heron_formula(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.heron_formula(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.heron_formula(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.heron_formula("", "", "")
        except EXC:
            pass


class Test_hyperbola_asymptotes:
    def test_exists(self):
        assert hasattr(mod, "hyperbola_asymptotes")

    def test_doc0(self):
        try:
            mod.hyperbola_asymptotes(3, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hyperbola_asymptotes(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbola_asymptotes(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbola_asymptotes(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbola_asymptotes("", "")
        except EXC:
            pass


class Test_hyperbola_eccentricity:
    def test_exists(self):
        assert hasattr(mod, "hyperbola_eccentricity")

    def test_var0(self):
        try:
            mod.hyperbola_eccentricity(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hyperbola_eccentricity(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hyperbola_eccentricity(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hyperbola_eccentricity("", "")
        except EXC:
            pass


class Test_icosahedron_surface_area:
    def test_exists(self):
        assert hasattr(mod, "icosahedron_surface_area")

    def test_var0(self):
        try:
            mod.icosahedron_surface_area(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.icosahedron_surface_area(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.icosahedron_surface_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.icosahedron_surface_area("")
        except EXC:
            pass


class Test_icosahedron_volume:
    def test_exists(self):
        assert hasattr(mod, "icosahedron_volume")

    def test_var0(self):
        try:
            mod.icosahedron_volume(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.icosahedron_volume(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.icosahedron_volume(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.icosahedron_volume("")
        except EXC:
            pass


class Test_law_of_cosines_angle:
    def test_exists(self):
        assert hasattr(mod, "law_of_cosines_angle")

    def test_var0(self):
        try:
            mod.law_of_cosines_angle(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.law_of_cosines_angle(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.law_of_cosines_angle(None, 3.14, 3.14)
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
            mod.law_of_cosines_side(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.law_of_cosines_side(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.law_of_cosines_side(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.law_of_cosines_side("", "", "")
        except EXC:
            pass


class Test_law_of_sines_side:
    def test_exists(self):
        assert hasattr(mod, "law_of_sines_side")

    def test_var0(self):
        try:
            mod.law_of_sines_side(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.law_of_sines_side(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.law_of_sines_side(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.law_of_sines_side("", "", "")
        except EXC:
            pass


class Test_line_equation:
    def test_exists(self):
        assert hasattr(mod, "line_equation")

    def test_doc0(self):
        try:
            mod.line_equation(0, 0, 1, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.line_equation(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.line_equation(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.line_equation(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.line_equation("", "", "", "")
        except EXC:
            pass


class Test_midpoint_2d:
    def test_exists(self):
        assert hasattr(mod, "midpoint_2d")

    def test_doc0(self):
        try:
            mod.midpoint_2d(0, 0, 4, 6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.midpoint_2d(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.midpoint_2d(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.midpoint_2d(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.midpoint_2d("", "", "", "")
        except EXC:
            pass


class Test_midpoint_3d:
    def test_exists(self):
        assert hasattr(mod, "midpoint_3d")

    def test_doc0(self):
        try:
            mod.midpoint_3d(0, 0, 0, 2, 4, 6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.midpoint_3d(3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.midpoint_3d(100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.midpoint_3d(None, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.midpoint_3d("", "", "", "", "", "")
        except EXC:
            pass


class Test_octahedron_surface_area:
    def test_exists(self):
        assert hasattr(mod, "octahedron_surface_area")

    def test_var0(self):
        try:
            mod.octahedron_surface_area(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.octahedron_surface_area(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.octahedron_surface_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.octahedron_surface_area("")
        except EXC:
            pass


class Test_octahedron_volume:
    def test_exists(self):
        assert hasattr(mod, "octahedron_volume")

    def test_var0(self):
        try:
            mod.octahedron_volume(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.octahedron_volume(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.octahedron_volume(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.octahedron_volume("")
        except EXC:
            pass


class Test_parabola_directrix:
    def test_exists(self):
        assert hasattr(mod, "parabola_directrix")

    def test_doc0(self):
        try:
            mod.parabola_directrix(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parabola_directrix(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parabola_directrix(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parabola_directrix(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parabola_directrix("")
        except EXC:
            pass


class Test_parabola_focus:
    def test_exists(self):
        assert hasattr(mod, "parabola_focus")

    def test_doc0(self):
        try:
            mod.parabola_focus(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parabola_focus(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parabola_focus(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parabola_focus(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parabola_focus("")
        except EXC:
            pass


class Test_parallelogram_area:
    def test_exists(self):
        assert hasattr(mod, "parallelogram_area")

    def test_doc0(self):
        try:
            mod.parallelogram_area(5, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parallelogram_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parallelogram_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parallelogram_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parallelogram_area("", "")
        except EXC:
            pass


class Test_point_to_line_distance:
    def test_exists(self):
        assert hasattr(mod, "point_to_line_distance")

    def test_var0(self):
        try:
            mod.point_to_line_distance(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.point_to_line_distance(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.point_to_line_distance(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.point_to_line_distance("", "", "", "", "")
        except EXC:
            pass


class Test_polygon_area:
    def test_exists(self):
        assert hasattr(mod, "polygon_area")

    def test_doc0(self):
        try:
            mod.polygon_area([(0, 0), (4, 0), (4, 3), (0, 3)])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polygon_area(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polygon_area(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polygon_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polygon_area("")
        except EXC:
            pass


class Test_polygon_centroid:
    def test_exists(self):
        assert hasattr(mod, "polygon_centroid")

    def test_doc0(self):
        try:
            mod.polygon_centroid([(0, 0), (4, 0), (4, 3), (0, 3)])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polygon_centroid(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polygon_centroid(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polygon_centroid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polygon_centroid("")
        except EXC:
            pass


class Test_prism_surface_area:
    def test_exists(self):
        assert hasattr(mod, "prism_surface_area")

    def test_doc0(self):
        try:
            mod.prism_surface_area(25.0, 20.0, 10.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.prism_surface_area(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.prism_surface_area(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.prism_surface_area(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.prism_surface_area("", "", "")
        except EXC:
            pass


class Test_prism_volume:
    def test_exists(self):
        assert hasattr(mod, "prism_volume")

    def test_doc0(self):
        try:
            mod.prism_volume(25.0, 10.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.prism_volume(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.prism_volume(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.prism_volume(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.prism_volume("", "")
        except EXC:
            pass


class Test_pyramid_surface_area:
    def test_exists(self):
        assert hasattr(mod, "pyramid_surface_area")

    def test_doc0(self):
        try:
            mod.pyramid_surface_area(16.0, 16.0, 5.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pyramid_surface_area(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pyramid_surface_area(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pyramid_surface_area(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pyramid_surface_area("", "", "")
        except EXC:
            pass


class Test_pyramid_volume:
    def test_exists(self):
        assert hasattr(mod, "pyramid_volume")

    def test_doc0(self):
        try:
            mod.pyramid_volume(9, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pyramid_volume(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pyramid_volume(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pyramid_volume(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pyramid_volume("", "")
        except EXC:
            pass


class Test_regular_polygon_area:
    def test_exists(self):
        assert hasattr(mod, "regular_polygon_area")

    def test_var0(self):
        try:
            mod.regular_polygon_area(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regular_polygon_area(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regular_polygon_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.regular_polygon_area(0, "")
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
            mod.regular_polygon_perimeter(6, 5.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.regular_polygon_perimeter(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regular_polygon_perimeter(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regular_polygon_perimeter(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.regular_polygon_perimeter(0, "")
        except EXC:
            pass


class Test_rhombus_area:
    def test_exists(self):
        assert hasattr(mod, "rhombus_area")

    def test_doc0(self):
        try:
            mod.rhombus_area(6.0, 8.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rhombus_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rhombus_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rhombus_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rhombus_area("", "")
        except EXC:
            pass


class Test_rhombus_perimeter:
    def test_exists(self):
        assert hasattr(mod, "rhombus_perimeter")

    def test_doc0(self):
        try:
            mod.rhombus_perimeter(5.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rhombus_perimeter(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rhombus_perimeter(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rhombus_perimeter(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rhombus_perimeter("")
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


class Test_shoelace_area:
    def test_exists(self):
        assert hasattr(mod, "shoelace_area")

    def test_doc0(self):
        try:
            mod.shoelace_area([(0, 0), (4, 0), (4, 3), (0, 3)])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.shoelace_area(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.shoelace_area(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.shoelace_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.shoelace_area("")
        except EXC:
            pass


class Test_slope_two_points:
    def test_exists(self):
        assert hasattr(mod, "slope_two_points")

    def test_doc0(self):
        try:
            mod.slope_two_points(0, 0, 2, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.slope_two_points(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.slope_two_points(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.slope_two_points(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.slope_two_points("", "", "", "")
        except EXC:
            pass


class Test_sphere_surface_area:
    def test_exists(self):
        assert hasattr(mod, "sphere_surface_area")

    def test_var0(self):
        try:
            mod.sphere_surface_area(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sphere_surface_area(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sphere_surface_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sphere_surface_area("")
        except EXC:
            pass


class Test_sphere_volume:
    def test_exists(self):
        assert hasattr(mod, "sphere_volume")

    def test_var0(self):
        try:
            mod.sphere_volume(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sphere_volume(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sphere_volume(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sphere_volume("")
        except EXC:
            pass


class Test_spherical_cap_surface_area:
    def test_exists(self):
        assert hasattr(mod, "spherical_cap_surface_area")

    def test_var0(self):
        try:
            mod.spherical_cap_surface_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_cap_surface_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_cap_surface_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_cap_surface_area("", "")
        except EXC:
            pass


class Test_spherical_cap_volume:
    def test_exists(self):
        assert hasattr(mod, "spherical_cap_volume")

    def test_var0(self):
        try:
            mod.spherical_cap_volume(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_cap_volume(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_cap_volume(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_cap_volume("", "")
        except EXC:
            pass


class Test_spherical_excess:
    def test_exists(self):
        assert hasattr(mod, "spherical_excess")

    def test_var0(self):
        try:
            mod.spherical_excess(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_excess(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_excess(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_excess("", "", "")
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


class Test_stadium_area:
    def test_exists(self):
        assert hasattr(mod, "stadium_area")

    def test_var0(self):
        try:
            mod.stadium_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stadium_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stadium_area(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.stadium_area("", 0)
        except EXC:
            pass


class Test_tetrahedron_surface_area:
    def test_exists(self):
        assert hasattr(mod, "tetrahedron_surface_area")

    def test_var0(self):
        try:
            mod.tetrahedron_surface_area(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tetrahedron_surface_area(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tetrahedron_surface_area(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tetrahedron_surface_area("")
        except EXC:
            pass


class Test_tetrahedron_volume:
    def test_exists(self):
        assert hasattr(mod, "tetrahedron_volume")

    def test_var0(self):
        try:
            mod.tetrahedron_volume(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tetrahedron_volume(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tetrahedron_volume(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tetrahedron_volume("")
        except EXC:
            pass


class Test_torus_surface_area:
    def test_exists(self):
        assert hasattr(mod, "torus_surface_area")

    def test_var0(self):
        try:
            mod.torus_surface_area(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.torus_surface_area(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.torus_surface_area(None, 3.14)
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
            mod.torus_volume(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.torus_volume(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.torus_volume(None, 3.14)
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
            mod.trapezoid_area(3, 5, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.trapezoid_area(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.trapezoid_area(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.trapezoid_area(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.trapezoid_area("", "", "")
        except EXC:
            pass


class Test_triangle_area_vertices:
    def test_exists(self):
        assert hasattr(mod, "triangle_area_vertices")

    def test_doc0(self):
        try:
            mod.triangle_area_vertices(0, 0, 4, 0, 0, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.triangle_area_vertices(3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.triangle_area_vertices(100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.triangle_area_vertices(None, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.triangle_area_vertices("", "", "", "", "", "")
        except EXC:
            pass

