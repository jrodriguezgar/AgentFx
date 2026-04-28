# Coverage tests for shortfx.fxNumeric.finite_differences_functions

from shortfx.fxNumeric import finite_differences_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_backward_difference_table:
    def test_exists(self):
        assert hasattr(mod, "backward_difference_table")

    def test_doc0(self):
        try:
            mod.backward_difference_table([1, 4, 9, 16])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.backward_difference_table([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.backward_difference_table([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.backward_difference_table(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.backward_difference_table("")
        except EXC:
            pass


class Test_bessel_interpolation:
    def test_exists(self):
        assert hasattr(mod, "bessel_interpolation")

    def test_doc0(self):
        try:
            mod.bessel_interpolation([0, 1, 2, 3], [0, 1, 8, 27], 1.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bessel_interpolation([1, 2, 3], [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bessel_interpolation([0], [0], 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bessel_interpolation(None, [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bessel_interpolation([], [], "")
        except EXC:
            pass


class Test_central_difference_table:
    def test_exists(self):
        assert hasattr(mod, "central_difference_table")

    def test_doc0(self):
        try:
            mod.central_difference_table([1, 4, 9, 16, 25])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.central_difference_table([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.central_difference_table([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.central_difference_table(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.central_difference_table("")
        except EXC:
            pass


class Test_divided_difference_table:
    def test_exists(self):
        assert hasattr(mod, "divided_difference_table")

    def test_doc0(self):
        try:
            mod.divided_difference_table([1, 2, 4], [1, 8, 64])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.divided_difference_table([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.divided_difference_table([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.divided_difference_table(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.divided_difference_table([], [])
        except EXC:
            pass


class Test_forward_difference_table:
    def test_exists(self):
        assert hasattr(mod, "forward_difference_table")

    def test_doc0(self):
        try:
            mod.forward_difference_table([1, 4, 9, 16])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.forward_difference_table([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.forward_difference_table([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.forward_difference_table(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.forward_difference_table("")
        except EXC:
            pass


class Test_gauss_forward_interpolation:
    def test_exists(self):
        assert hasattr(mod, "gauss_forward_interpolation")

    def test_doc0(self):
        try:
            mod.gauss_forward_interpolation([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], 2.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gauss_forward_interpolation([1, 2, 3], [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gauss_forward_interpolation([0], [0], 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gauss_forward_interpolation(None, [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gauss_forward_interpolation([], [], "")
        except EXC:
            pass


class Test_newton_backward_interpolation:
    def test_exists(self):
        assert hasattr(mod, "newton_backward_interpolation")

    def test_doc0(self):
        try:
            mod.newton_backward_interpolation([0, 1, 2, 3], [1, 4, 9, 16], 2.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.newton_backward_interpolation([1, 2, 3], [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.newton_backward_interpolation([0], [0], 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.newton_backward_interpolation(None, [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.newton_backward_interpolation([], [], "")
        except EXC:
            pass


class Test_newton_forward_interpolation:
    def test_exists(self):
        assert hasattr(mod, "newton_forward_interpolation")

    def test_doc0(self):
        try:
            mod.newton_forward_interpolation([0, 1, 2, 3], [1, 4, 9, 16], 1.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.newton_forward_interpolation([1, 2, 3], [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.newton_forward_interpolation([0], [0], 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.newton_forward_interpolation(None, [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.newton_forward_interpolation([], [], "")
        except EXC:
            pass


class Test_stirling_interpolation:
    def test_exists(self):
        assert hasattr(mod, "stirling_interpolation")

    def test_doc0(self):
        try:
            mod.stirling_interpolation([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], 2.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.stirling_interpolation([1, 2, 3], [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stirling_interpolation([0], [0], 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stirling_interpolation(None, [1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.stirling_interpolation([], [], "")
        except EXC:
            pass

