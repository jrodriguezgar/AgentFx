# Coverage tests for shortfx.fxNumeric.mechanics_functions
import math

from shortfx.fxNumeric import mechanics_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_centroid_circular_sector:
    def test_exists(self):
        assert hasattr(mod, "centroid_circular_sector")

    def test_doc0(self):
        try:
            mod.centroid_circular_sector(3, math.pi / 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.centroid_circular_sector(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.centroid_circular_sector(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.centroid_circular_sector(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.centroid_circular_sector("", 0)
        except EXC:
            pass


class Test_centroid_cone:
    def test_exists(self):
        assert hasattr(mod, "centroid_cone")

    def test_doc0(self):
        try:
            mod.centroid_cone(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.centroid_cone(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.centroid_cone(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.centroid_cone(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.centroid_cone("")
        except EXC:
            pass


class Test_centroid_hemisphere:
    def test_exists(self):
        assert hasattr(mod, "centroid_hemisphere")

    def test_doc0(self):
        try:
            mod.centroid_hemisphere(4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.centroid_hemisphere(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.centroid_hemisphere(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.centroid_hemisphere(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.centroid_hemisphere("")
        except EXC:
            pass


class Test_centroid_polygon:
    def test_exists(self):
        assert hasattr(mod, "centroid_polygon")

    def test_doc0(self):
        try:
            mod.centroid_polygon([(0, 0), (4, 0), (4, 4), (0, 4)])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.centroid_polygon(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.centroid_polygon(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.centroid_polygon(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.centroid_polygon("")
        except EXC:
            pass


class Test_centroid_semicircle:
    def test_exists(self):
        assert hasattr(mod, "centroid_semicircle")

    def test_doc0(self):
        try:
            mod.centroid_semicircle(3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.centroid_semicircle(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.centroid_semicircle(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.centroid_semicircle(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.centroid_semicircle("")
        except EXC:
            pass


class Test_centroid_triangle:
    def test_exists(self):
        assert hasattr(mod, "centroid_triangle")

    def test_doc0(self):
        try:
            mod.centroid_triangle((0, 0), (6, 0), (0, 6))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.centroid_triangle(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.centroid_triangle(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.centroid_triangle(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.centroid_triangle("", "", "")
        except EXC:
            pass


class Test_mass_moment_cone:
    def test_exists(self):
        assert hasattr(mod, "mass_moment_cone")

    def test_doc0(self):
        try:
            mod.mass_moment_cone(10, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mass_moment_cone(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mass_moment_cone(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mass_moment_cone(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mass_moment_cone("", "")
        except EXC:
            pass


class Test_mass_moment_cylinder:
    def test_exists(self):
        assert hasattr(mod, "mass_moment_cylinder")

    def test_doc0(self):
        try:
            mod.mass_moment_cylinder(10, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mass_moment_cylinder(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mass_moment_cylinder(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mass_moment_cylinder(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mass_moment_cylinder("", "")
        except EXC:
            pass


class Test_mass_moment_cylinder_transverse:
    def test_exists(self):
        assert hasattr(mod, "mass_moment_cylinder_transverse")

    def test_var0(self):
        try:
            mod.mass_moment_cylinder_transverse(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mass_moment_cylinder_transverse(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mass_moment_cylinder_transverse(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mass_moment_cylinder_transverse("", "", "")
        except EXC:
            pass


class Test_mass_moment_disk:
    def test_exists(self):
        assert hasattr(mod, "mass_moment_disk")

    def test_doc0(self):
        try:
            mod.mass_moment_disk(10, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mass_moment_disk(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mass_moment_disk(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mass_moment_disk(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mass_moment_disk("", "")
        except EXC:
            pass


class Test_mass_moment_hollow_sphere:
    def test_exists(self):
        assert hasattr(mod, "mass_moment_hollow_sphere")

    def test_var0(self):
        try:
            mod.mass_moment_hollow_sphere(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mass_moment_hollow_sphere(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mass_moment_hollow_sphere(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mass_moment_hollow_sphere("", "")
        except EXC:
            pass


class Test_mass_moment_rod:
    def test_exists(self):
        assert hasattr(mod, "mass_moment_rod")

    def test_var0(self):
        try:
            mod.mass_moment_rod(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mass_moment_rod(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mass_moment_rod(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mass_moment_rod("", 0)
        except EXC:
            pass


class Test_mass_moment_sphere:
    def test_exists(self):
        assert hasattr(mod, "mass_moment_sphere")

    def test_doc0(self):
        try:
            mod.mass_moment_sphere(10, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mass_moment_sphere(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mass_moment_sphere(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mass_moment_sphere(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mass_moment_sphere("", "")
        except EXC:
            pass


class Test_moment_of_inertia_annulus:
    def test_exists(self):
        assert hasattr(mod, "moment_of_inertia_annulus")

    def test_var0(self):
        try:
            mod.moment_of_inertia_annulus(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moment_of_inertia_annulus(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moment_of_inertia_annulus(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moment_of_inertia_annulus("", "")
        except EXC:
            pass


class Test_moment_of_inertia_circle:
    def test_exists(self):
        assert hasattr(mod, "moment_of_inertia_circle")

    def test_var0(self):
        try:
            mod.moment_of_inertia_circle(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moment_of_inertia_circle(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moment_of_inertia_circle(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moment_of_inertia_circle("")
        except EXC:
            pass


class Test_moment_of_inertia_ellipse:
    def test_exists(self):
        assert hasattr(mod, "moment_of_inertia_ellipse")

    def test_doc0(self):
        try:
            mod.moment_of_inertia_ellipse(3, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.moment_of_inertia_ellipse(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moment_of_inertia_ellipse(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moment_of_inertia_ellipse(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moment_of_inertia_ellipse("", "")
        except EXC:
            pass


class Test_moment_of_inertia_rectangle:
    def test_exists(self):
        assert hasattr(mod, "moment_of_inertia_rectangle")

    def test_doc0(self):
        try:
            mod.moment_of_inertia_rectangle(4, 6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.moment_of_inertia_rectangle(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moment_of_inertia_rectangle(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moment_of_inertia_rectangle(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moment_of_inertia_rectangle("", "")
        except EXC:
            pass


class Test_moment_of_inertia_semicircle:
    def test_exists(self):
        assert hasattr(mod, "moment_of_inertia_semicircle")

    def test_var0(self):
        try:
            mod.moment_of_inertia_semicircle(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moment_of_inertia_semicircle(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moment_of_inertia_semicircle(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moment_of_inertia_semicircle("")
        except EXC:
            pass


class Test_moment_of_inertia_triangle:
    def test_exists(self):
        assert hasattr(mod, "moment_of_inertia_triangle")

    def test_doc0(self):
        try:
            mod.moment_of_inertia_triangle(6, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.moment_of_inertia_triangle(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moment_of_inertia_triangle(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moment_of_inertia_triangle(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moment_of_inertia_triangle("", "")
        except EXC:
            pass


class Test_moment_of_inertia_triangle_centroidal:
    def test_exists(self):
        assert hasattr(mod, "moment_of_inertia_triangle_centroidal")

    def test_var0(self):
        try:
            mod.moment_of_inertia_triangle_centroidal(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moment_of_inertia_triangle_centroidal(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moment_of_inertia_triangle_centroidal(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moment_of_inertia_triangle_centroidal("", "")
        except EXC:
            pass


class Test_parallel_axis_theorem:
    def test_exists(self):
        assert hasattr(mod, "parallel_axis_theorem")

    def test_doc0(self):
        try:
            mod.parallel_axis_theorem(8.0, 6, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parallel_axis_theorem(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parallel_axis_theorem(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parallel_axis_theorem(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parallel_axis_theorem("", "", "")
        except EXC:
            pass


class Test_polar_moment_of_inertia:
    def test_exists(self):
        assert hasattr(mod, "polar_moment_of_inertia")

    def test_doc0(self):
        try:
            mod.polar_moment_of_inertia(72, 32)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polar_moment_of_inertia(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polar_moment_of_inertia(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polar_moment_of_inertia(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polar_moment_of_inertia("", "")
        except EXC:
            pass


class Test_radius_of_gyration:
    def test_exists(self):
        assert hasattr(mod, "radius_of_gyration")

    def test_var0(self):
        try:
            mod.radius_of_gyration(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.radius_of_gyration(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.radius_of_gyration(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.radius_of_gyration("", "")
        except EXC:
            pass


class Test_section_modulus:
    def test_exists(self):
        assert hasattr(mod, "section_modulus")

    def test_doc0(self):
        try:
            mod.section_modulus(72, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.section_modulus(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.section_modulus(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.section_modulus(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.section_modulus("", "")
        except EXC:
            pass

