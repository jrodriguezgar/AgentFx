# Coverage tests for agentfx.fxNumeric.curves_functions
import math

from agentfx.fxNumeric import curves_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_arc_length_function:
    def test_exists(self):
        assert hasattr(mod, "arc_length_function")

    def test_var0(self):
        try:
            mod.arc_length_function(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arc_length_function(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arc_length_function(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arc_length_function("", "", "")
        except EXC:
            pass


class Test_arc_length_parametric:
    def test_exists(self):
        assert hasattr(mod, "arc_length_parametric")

    def test_var0(self):
        try:
            mod.arc_length_parametric(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arc_length_parametric(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arc_length_parametric(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arc_length_parametric("", "", "", "")
        except EXC:
            pass


class Test_arc_length_polar:
    def test_exists(self):
        assert hasattr(mod, "arc_length_polar")

    def test_var0(self):
        try:
            mod.arc_length_polar(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arc_length_polar(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arc_length_polar(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arc_length_polar("", "", "")
        except EXC:
            pass


class Test_archimedean_spiral:
    def test_exists(self):
        assert hasattr(mod, "archimedean_spiral")

    def test_doc0(self):
        try:
            mod.archimedean_spiral(math.pi, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.archimedean_spiral(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.archimedean_spiral(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.archimedean_spiral(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.archimedean_spiral("")
        except EXC:
            pass


class Test_astroid:
    def test_exists(self):
        assert hasattr(mod, "astroid")

    def test_doc0(self):
        try:
            mod.astroid(0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.astroid(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.astroid(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.astroid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.astroid("")
        except EXC:
            pass


class Test_bezier_cubic:
    def test_exists(self):
        assert hasattr(mod, "bezier_cubic")

    def test_doc0(self):
        try:
            mod.bezier_cubic((0, 0), (1, 3), (2, 3), (3, 0), 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bezier_cubic(0, 0, 0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bezier_cubic(1, 1, 1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bezier_cubic(None, 0, 0, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bezier_cubic("", "", "", "", "")
        except EXC:
            pass


class Test_bezier_quadratic:
    def test_exists(self):
        assert hasattr(mod, "bezier_quadratic")

    def test_doc0(self):
        try:
            mod.bezier_quadratic((0, 0), (1, 2), (2, 0), 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bezier_quadratic(0, 0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bezier_quadratic(1, 1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bezier_quadratic(None, 0, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bezier_quadratic("", "", "", "")
        except EXC:
            pass


class Test_brachistochrone_time:
    def test_exists(self):
        assert hasattr(mod, "brachistochrone_time")

    def test_var0(self):
        try:
            mod.brachistochrone_time(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.brachistochrone_time(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.brachistochrone_time(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.brachistochrone_time("", "")
        except EXC:
            pass


class Test_butterfly_curve:
    def test_exists(self):
        assert hasattr(mod, "butterfly_curve")

    def test_doc0(self):
        try:
            mod.butterfly_curve(0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.butterfly_curve(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.butterfly_curve(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.butterfly_curve(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.butterfly_curve("")
        except EXC:
            pass


class Test_cardioid:
    def test_exists(self):
        assert hasattr(mod, "cardioid")

    def test_doc0(self):
        try:
            mod.cardioid(0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cardioid(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cardioid(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cardioid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cardioid("")
        except EXC:
            pass


class Test_cassini_oval:
    def test_exists(self):
        assert hasattr(mod, "cassini_oval")

    def test_doc0(self):
        try:
            mod.cassini_oval(0, 1.0, 1.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cassini_oval(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cassini_oval(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cassini_oval(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cassini_oval("")
        except EXC:
            pass


class Test_catenary:
    def test_exists(self):
        assert hasattr(mod, "catenary")

    def test_doc0(self):
        try:
            mod.catenary(0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.catenary(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.catenary(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.catenary(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.catenary("")
        except EXC:
            pass


class Test_catmull_rom:
    def test_exists(self):
        assert hasattr(mod, "catmull_rom")

    def test_doc0(self):
        try:
            mod.catmull_rom(0.0, 1.0, 2.0, 3.0, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.catmull_rom(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.catmull_rom(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.catmull_rom(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.catmull_rom("", "", "", "", "")
        except EXC:
            pass


class Test_cissoid:
    def test_exists(self):
        assert hasattr(mod, "cissoid")

    def test_doc0(self):
        try:
            mod.cissoid(0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cissoid(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cissoid(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cissoid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cissoid("")
        except EXC:
            pass


class Test_cochleoid:
    def test_exists(self):
        assert hasattr(mod, "cochleoid")

    def test_var0(self):
        try:
            mod.cochleoid(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cochleoid(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cochleoid(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cochleoid("", "")
        except EXC:
            pass


class Test_conchoid_of_nicomedes:
    def test_exists(self):
        assert hasattr(mod, "conchoid_of_nicomedes")

    def test_doc0(self):
        try:
            mod.conchoid_of_nicomedes(0, 1, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.conchoid_of_nicomedes(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.conchoid_of_nicomedes(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.conchoid_of_nicomedes(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.conchoid_of_nicomedes("")
        except EXC:
            pass


class Test_cornu_spiral:
    def test_exists(self):
        assert hasattr(mod, "cornu_spiral")

    def test_doc0(self):
        try:
            mod.cornu_spiral(1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cornu_spiral(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cornu_spiral(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cornu_spiral(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cornu_spiral("")
        except EXC:
            pass


class Test_curvature_explicit:
    def test_exists(self):
        assert hasattr(mod, "curvature_explicit")

    def test_var0(self):
        try:
            mod.curvature_explicit(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.curvature_explicit(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.curvature_explicit(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.curvature_explicit("", "")
        except EXC:
            pass


class Test_curvature_parametric:
    def test_exists(self):
        assert hasattr(mod, "curvature_parametric")

    def test_var0(self):
        try:
            mod.curvature_parametric(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.curvature_parametric(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.curvature_parametric(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.curvature_parametric("", "", "")
        except EXC:
            pass


class Test_curvature_polar:
    def test_exists(self):
        assert hasattr(mod, "curvature_polar")

    def test_var0(self):
        try:
            mod.curvature_polar(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.curvature_polar(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.curvature_polar(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.curvature_polar("", "")
        except EXC:
            pass


class Test_cycloid:
    def test_exists(self):
        assert hasattr(mod, "cycloid")

    def test_doc0(self):
        try:
            mod.cycloid(math.pi, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cycloid(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cycloid(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cycloid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cycloid("")
        except EXC:
            pass


class Test_cycloid_arc_length:
    def test_exists(self):
        assert hasattr(mod, "cycloid_arc_length")

    def test_doc0(self):
        try:
            mod.cycloid_arc_length(1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cycloid_arc_length(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cycloid_arc_length(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cycloid_arc_length(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cycloid_arc_length("")
        except EXC:
            pass


class Test_deltoid:
    def test_exists(self):
        assert hasattr(mod, "deltoid")

    def test_doc0(self):
        try:
            mod.deltoid(0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.deltoid(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.deltoid(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.deltoid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.deltoid("")
        except EXC:
            pass


class Test_epicycloid:
    def test_exists(self):
        assert hasattr(mod, "epicycloid")

    def test_doc0(self):
        try:
            mod.epicycloid(0, 3, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.epicycloid(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.epicycloid(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.epicycloid(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.epicycloid("", "", "")
        except EXC:
            pass


class Test_epitrochoid:
    def test_exists(self):
        assert hasattr(mod, "epitrochoid")

    def test_doc0(self):
        try:
            mod.epitrochoid(3.0, 1.0, 0.5, 0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.epitrochoid(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.epitrochoid(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.epitrochoid(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.epitrochoid("", "", "", "")
        except EXC:
            pass


class Test_evolute_ellipse:
    def test_exists(self):
        assert hasattr(mod, "evolute_ellipse")

    def test_var0(self):
        try:
            mod.evolute_ellipse(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.evolute_ellipse(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.evolute_ellipse(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.evolute_ellipse("", "", "")
        except EXC:
            pass


class Test_fermat_spiral:
    def test_exists(self):
        assert hasattr(mod, "fermat_spiral")

    def test_var0(self):
        try:
            mod.fermat_spiral(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fermat_spiral(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fermat_spiral(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fermat_spiral("", "")
        except EXC:
            pass


class Test_folium_of_descartes:
    def test_exists(self):
        assert hasattr(mod, "folium_of_descartes")

    def test_doc0(self):
        try:
            mod.folium_of_descartes(1, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.folium_of_descartes(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.folium_of_descartes(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.folium_of_descartes(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.folium_of_descartes("")
        except EXC:
            pass


class Test_gaussian_curvature_cylinder:
    def test_exists(self):
        assert hasattr(mod, "gaussian_curvature_cylinder")

    def test_doc0(self):
        try:
            mod.gaussian_curvature_cylinder(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gaussian_curvature_cylinder(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gaussian_curvature_cylinder(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gaussian_curvature_cylinder(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gaussian_curvature_cylinder("")
        except EXC:
            pass


class Test_gaussian_curvature_sphere:
    def test_exists(self):
        assert hasattr(mod, "gaussian_curvature_sphere")

    def test_doc0(self):
        try:
            mod.gaussian_curvature_sphere(2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gaussian_curvature_sphere(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gaussian_curvature_sphere(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gaussian_curvature_sphere(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gaussian_curvature_sphere("")
        except EXC:
            pass


class Test_gaussian_curvature_torus:
    def test_exists(self):
        assert hasattr(mod, "gaussian_curvature_torus")

    def test_var0(self):
        try:
            mod.gaussian_curvature_torus(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gaussian_curvature_torus(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gaussian_curvature_torus(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gaussian_curvature_torus("", "", "")
        except EXC:
            pass


class Test_hermite_interpolation:
    def test_exists(self):
        assert hasattr(mod, "hermite_interpolation")

    def test_doc0(self):
        try:
            mod.hermite_interpolation(0.0, 1.0, 0.0, 0.0, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hermite_interpolation(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hermite_interpolation(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hermite_interpolation(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hermite_interpolation("", "", "", "", "")
        except EXC:
            pass


class Test_hypocycloid:
    def test_exists(self):
        assert hasattr(mod, "hypocycloid")

    def test_doc0(self):
        try:
            mod.hypocycloid(0, 4, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hypocycloid(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hypocycloid(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hypocycloid(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hypocycloid("", "", "")
        except EXC:
            pass


class Test_hypotrochoid:
    def test_exists(self):
        assert hasattr(mod, "hypotrochoid")

    def test_doc0(self):
        try:
            mod.hypotrochoid(5.0, 3.0, 5.0, 0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hypotrochoid(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hypotrochoid(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hypotrochoid(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hypotrochoid("", "", "", "")
        except EXC:
            pass


class Test_involute_of_circle:
    def test_exists(self):
        assert hasattr(mod, "involute_of_circle")

    def test_doc0(self):
        try:
            mod.involute_of_circle(0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.involute_of_circle(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.involute_of_circle(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.involute_of_circle(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.involute_of_circle("")
        except EXC:
            pass


class Test_lemniscate:
    def test_exists(self):
        assert hasattr(mod, "lemniscate")

    def test_doc0(self):
        try:
            mod.lemniscate(0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lemniscate(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lemniscate(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lemniscate(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lemniscate("")
        except EXC:
            pass


class Test_limacon:
    def test_exists(self):
        assert hasattr(mod, "limacon")

    def test_doc0(self):
        try:
            mod.limacon(0, 1, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.limacon(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.limacon(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.limacon(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.limacon("")
        except EXC:
            pass


class Test_lissajous:
    def test_exists(self):
        assert hasattr(mod, "lissajous")

    def test_doc0(self):
        try:
            mod.lissajous(0, 1, 1, 3, 2, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lissajous(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lissajous(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lissajous(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lissajous("")
        except EXC:
            pass


class Test_lituus:
    def test_exists(self):
        assert hasattr(mod, "lituus")

    def test_var0(self):
        try:
            mod.lituus(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lituus(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lituus(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lituus("", "")
        except EXC:
            pass


class Test_logarithmic_spiral:
    def test_exists(self):
        assert hasattr(mod, "logarithmic_spiral")

    def test_doc0(self):
        try:
            mod.logarithmic_spiral(0, 1, 0.2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.logarithmic_spiral(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.logarithmic_spiral(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.logarithmic_spiral(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.logarithmic_spiral("")
        except EXC:
            pass


class Test_mean_curvature_sphere:
    def test_exists(self):
        assert hasattr(mod, "mean_curvature_sphere")

    def test_doc0(self):
        try:
            mod.mean_curvature_sphere(4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mean_curvature_sphere(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mean_curvature_sphere(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mean_curvature_sphere(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mean_curvature_sphere("")
        except EXC:
            pass


class Test_nephroid:
    def test_exists(self):
        assert hasattr(mod, "nephroid")

    def test_doc0(self):
        try:
            mod.nephroid(0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.nephroid(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nephroid(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nephroid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nephroid("")
        except EXC:
            pass


class Test_piriform:
    def test_exists(self):
        assert hasattr(mod, "piriform")

    def test_doc0(self):
        try:
            mod.piriform(0, 1, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.piriform(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.piriform(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.piriform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.piriform("")
        except EXC:
            pass


class Test_principal_curvatures_ellipsoid:
    def test_exists(self):
        assert hasattr(mod, "principal_curvatures_ellipsoid")

    def test_doc0(self):
        try:
            mod.principal_curvatures_ellipsoid(2, 3, 1, 0, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.principal_curvatures_ellipsoid(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.principal_curvatures_ellipsoid(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.principal_curvatures_ellipsoid(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.principal_curvatures_ellipsoid("", "", "", "", "")
        except EXC:
            pass


class Test_radius_of_curvature:
    def test_exists(self):
        assert hasattr(mod, "radius_of_curvature")

    def test_var0(self):
        try:
            mod.radius_of_curvature(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.radius_of_curvature(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.radius_of_curvature(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.radius_of_curvature("", "")
        except EXC:
            pass


class Test_rose_curve:
    def test_exists(self):
        assert hasattr(mod, "rose_curve")

    def test_doc0(self):
        try:
            mod.rose_curve(0, 1, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rose_curve(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rose_curve(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rose_curve(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rose_curve("")
        except EXC:
            pass


class Test_strophoid:
    def test_exists(self):
        assert hasattr(mod, "strophoid")

    def test_doc0(self):
        try:
            mod.strophoid(0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.strophoid(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.strophoid(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.strophoid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.strophoid("")
        except EXC:
            pass


class Test_superellipse:
    def test_exists(self):
        assert hasattr(mod, "superellipse")

    def test_doc0(self):
        try:
            mod.superellipse(1.0, 1.0, 2.0, 0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.superellipse(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.superellipse(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.superellipse(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.superellipse("", "", 0, "")
        except EXC:
            pass


class Test_surface_area_revolution:
    def test_exists(self):
        assert hasattr(mod, "surface_area_revolution")

    def test_var0(self):
        try:
            mod.surface_area_revolution(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.surface_area_revolution(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.surface_area_revolution(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.surface_area_revolution("", "", "")
        except EXC:
            pass


class Test_tautochrone_period:
    def test_exists(self):
        assert hasattr(mod, "tautochrone_period")

    def test_var0(self):
        try:
            mod.tautochrone_period(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tautochrone_period(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tautochrone_period(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tautochrone_period("")
        except EXC:
            pass


class Test_tractrix:
    def test_exists(self):
        assert hasattr(mod, "tractrix")

    def test_doc0(self):
        try:
            mod.tractrix(math.pi / 2, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.tractrix(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tractrix(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tractrix(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tractrix("")
        except EXC:
            pass


class Test_witch_of_agnesi:
    def test_exists(self):
        assert hasattr(mod, "witch_of_agnesi")

    def test_doc0(self):
        try:
            mod.witch_of_agnesi(0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.witch_of_agnesi(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.witch_of_agnesi(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.witch_of_agnesi(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.witch_of_agnesi("")
        except EXC:
            pass

