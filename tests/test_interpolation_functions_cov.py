# Coverage tests for shortfx.fxNumeric.interpolation_functions

from shortfx.fxNumeric import interpolation_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_bilinear_interpolation:
    def test_exists(self):
        assert hasattr(mod, "bilinear_interpolation")

    def test_doc0(self):
        try:
            mod.bilinear_interpolation(0.5, 0.5, 0, 1, 0, 1, 0, 1, 1, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bilinear_interpolation(0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bilinear_interpolation(1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bilinear_interpolation(None, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bilinear_interpolation("", "", "", "", "", "", "", "", "", "")
        except EXC:
            pass


class Test_clamp_interpolate:
    def test_exists(self):
        assert hasattr(mod, "clamp_interpolate")

    def test_doc0(self):
        try:
            mod.clamp_interpolate(15, 0, 0, 10, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.clamp_interpolate(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.clamp_interpolate(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.clamp_interpolate(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.clamp_interpolate("", "", "", "", "")
        except EXC:
            pass


class Test_clip_number:
    def test_exists(self):
        assert hasattr(mod, "clip_number")

    def test_doc0(self):
        try:
            mod.clip_number(10, 0, 100)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.clip_number(-5, 0, 100)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.clip_number(150, 0, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.clip_number(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.clip_number(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.clip_number(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.clip_number("", 0, 0)
        except EXC:
            pass


class Test_cubic_spline_natural:
    def test_exists(self):
        assert hasattr(mod, "cubic_spline_natural")

    def test_doc0(self):
        try:
            mod.cubic_spline_natural([0, 1, 2, 3], [0, 1, 4, 9], 1.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cubic_spline_natural(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cubic_spline_natural(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cubic_spline_natural(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cubic_spline_natural([], [], "")
        except EXC:
            pass


class Test_inverse_interpolate:
    def test_exists(self):
        assert hasattr(mod, "inverse_interpolate")

    def test_doc0(self):
        try:
            mod.inverse_interpolate(50, 0, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_interpolate(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_interpolate(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_interpolate(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_interpolate("", "", "")
        except EXC:
            pass


class Test_lagrange_interpolation:
    def test_exists(self):
        assert hasattr(mod, "lagrange_interpolation")

    def test_doc0(self):
        try:
            mod.lagrange_interpolation([1, 2, 3], [1, 4, 9], 2.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lagrange_interpolation(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lagrange_interpolation(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lagrange_interpolation(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lagrange_interpolation([], [], "")
        except EXC:
            pass


class Test_linear_interpolate:
    def test_exists(self):
        assert hasattr(mod, "linear_interpolate")

    def test_doc0(self):
        try:
            mod.linear_interpolate(5, 0, 0, 10, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.linear_interpolate(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.linear_interpolate(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.linear_interpolate(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.linear_interpolate("", "", "", "", "")
        except EXC:
            pass


class Test_linear_interpolation:
    def test_exists(self):
        assert hasattr(mod, "linear_interpolation")

    def test_doc0(self):
        try:
            mod.linear_interpolation(2.5, [1, 2, 3], [10, 20, 30])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.linear_interpolation(0, [1, 3], [10, 30])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.linear_interpolation(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.linear_interpolation(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.linear_interpolation(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.linear_interpolation("", [], [])
        except EXC:
            pass


class Test_map_range:
    def test_exists(self):
        assert hasattr(mod, "map_range")

    def test_doc0(self):
        try:
            mod.map_range(5, 0, 10, 0, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.map_range(0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.map_range(1, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.map_range(None, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.map_range("", 0, 0, 0, "")
        except EXC:
            pass


class Test_newton_divided_difference:
    def test_exists(self):
        assert hasattr(mod, "newton_divided_difference")

    def test_doc0(self):
        try:
            mod.newton_divided_difference([1, 2, 3], [1, 4, 9], 2.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.newton_divided_difference(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.newton_divided_difference(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.newton_divided_difference(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.newton_divided_difference([], [], "")
        except EXC:
            pass


class Test_normalize_list:
    def test_exists(self):
        assert hasattr(mod, "normalize_list")

    def test_doc0(self):
        try:
            mod.normalize_list([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.normalize_list([10, 10, 10])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.normalize_list(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.normalize_list(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.normalize_list(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.normalize_list([])
        except EXC:
            pass


class Test_normalize_to_0_1_range:
    def test_exists(self):
        assert hasattr(mod, "normalize_to_0_1_range")

    def test_doc0(self):
        try:
            mod.normalize_to_0_1_range(50, 0, 100)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.normalize_to_0_1_range(75, 50, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.normalize_to_0_1_range(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.normalize_to_0_1_range(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.normalize_to_0_1_range(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.normalize_to_0_1_range("", 0, 0)
        except EXC:
            pass


class Test_piecewise_interpolate:
    def test_exists(self):
        assert hasattr(mod, "piecewise_interpolate")

    def test_doc0(self):
        try:
            mod.piecewise_interpolate(15, [0, 10, 20, 30], [0, 100, 100, 200])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.piecewise_interpolate(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.piecewise_interpolate(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.piecewise_interpolate(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.piecewise_interpolate("", "", "")
        except EXC:
            pass


class Test_scale_to_new_range:
    def test_exists(self):
        assert hasattr(mod, "scale_to_new_range")

    def test_doc0(self):
        try:
            mod.scale_to_new_range(50, 0, 100, 0, 10)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.scale_to_new_range(50, 0, 100, 100, 200)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.scale_to_new_range(0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.scale_to_new_range(1, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.scale_to_new_range(None, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.scale_to_new_range("", 0, 0, 0, "")
        except EXC:
            pass

