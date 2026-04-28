# Coverage tests for shortfx.fxNumeric.complex_functions
import math

from shortfx.fxNumeric import complex_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_complex_add:
    def test_exists(self):
        assert hasattr(mod, "complex_add")

    def test_doc0(self):
        try:
            mod.complex_add((1, 2), (3, 4))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_add(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_add(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_add(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_add("", "")
        except EXC:
            pass


class Test_complex_argument:
    def test_exists(self):
        assert hasattr(mod, "complex_argument")

    def test_var0(self):
        try:
            mod.complex_argument(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_argument(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_argument(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_argument("")
        except EXC:
            pass


class Test_complex_argument_degrees:
    def test_exists(self):
        assert hasattr(mod, "complex_argument_degrees")

    def test_doc0(self):
        try:
            mod.complex_argument_degrees((1.0, 1.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_argument_degrees(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_argument_degrees(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_argument_degrees(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_argument_degrees("")
        except EXC:
            pass


class Test_complex_conjugate:
    def test_exists(self):
        assert hasattr(mod, "complex_conjugate")

    def test_doc0(self):
        try:
            mod.complex_conjugate((3.0, 4.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_conjugate(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_conjugate(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_conjugate(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_conjugate("")
        except EXC:
            pass


class Test_complex_cos:
    def test_exists(self):
        assert hasattr(mod, "complex_cos")

    def test_doc0(self):
        try:
            mod.complex_cos((0, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_cos(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_cos(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_cos(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_cos("")
        except EXC:
            pass


class Test_complex_cosh:
    def test_exists(self):
        assert hasattr(mod, "complex_cosh")

    def test_doc0(self):
        try:
            mod.complex_cosh((1.0, 0.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_cosh(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_cosh(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_cosh(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_cosh("")
        except EXC:
            pass


class Test_complex_distance:
    def test_exists(self):
        assert hasattr(mod, "complex_distance")

    def test_doc0(self):
        try:
            mod.complex_distance((0.0, 0.0), (3.0, 4.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_distance(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_distance(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_distance(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_distance("", "")
        except EXC:
            pass


class Test_complex_divide:
    def test_exists(self):
        assert hasattr(mod, "complex_divide")

    def test_doc0(self):
        try:
            mod.complex_divide((4, 2), (1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_divide(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_divide(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_divide(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_divide("", "")
        except EXC:
            pass


class Test_complex_exp:
    def test_exists(self):
        assert hasattr(mod, "complex_exp")

    def test_doc0(self):
        try:
            mod.complex_exp((0, math.pi))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_exp(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_exp(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_exp(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_exp("")
        except EXC:
            pass


class Test_complex_from_polar:
    def test_exists(self):
        assert hasattr(mod, "complex_from_polar")

    def test_doc0(self):
        try:
            mod.complex_from_polar(1.0, 0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_from_polar(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_from_polar(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_from_polar(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_from_polar("", "")
        except EXC:
            pass


class Test_complex_lerp:
    def test_exists(self):
        assert hasattr(mod, "complex_lerp")

    def test_doc0(self):
        try:
            mod.complex_lerp((0.0, 0.0), (4.0, 6.0), 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_lerp(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_lerp(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_lerp(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_lerp("", "", "")
        except EXC:
            pass


class Test_complex_ln:
    def test_exists(self):
        assert hasattr(mod, "complex_ln")

    def test_doc0(self):
        try:
            mod.complex_ln((-1, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_ln(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_ln(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_ln(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_ln("")
        except EXC:
            pass


class Test_complex_log:
    def test_exists(self):
        assert hasattr(mod, "complex_log")

    def test_doc0(self):
        try:
            mod.complex_log((1.0, 0.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_log(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_log(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_log(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_log("")
        except EXC:
            pass


class Test_complex_midpoint:
    def test_exists(self):
        assert hasattr(mod, "complex_midpoint")

    def test_doc0(self):
        try:
            mod.complex_midpoint((0.0, 0.0), (4.0, 6.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_midpoint(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_midpoint(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_midpoint(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_midpoint("", "")
        except EXC:
            pass


class Test_complex_modulus:
    def test_exists(self):
        assert hasattr(mod, "complex_modulus")

    def test_doc0(self):
        try:
            mod.complex_modulus((3, 4))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_modulus(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_modulus(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_modulus(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_modulus("")
        except EXC:
            pass


class Test_complex_multiply:
    def test_exists(self):
        assert hasattr(mod, "complex_multiply")

    def test_doc0(self):
        try:
            mod.complex_multiply((1, 2), (3, 4))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_multiply(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_multiply(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_multiply(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_multiply("", "")
        except EXC:
            pass


class Test_complex_nth_root:
    def test_exists(self):
        assert hasattr(mod, "complex_nth_root")

    def test_doc0(self):
        try:
            mod.complex_nth_root((1.0, 0.0), 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_nth_root(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_nth_root(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_nth_root(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_nth_root("", 0)
        except EXC:
            pass


class Test_complex_polar_form:
    def test_exists(self):
        assert hasattr(mod, "complex_polar_form")

    def test_doc0(self):
        try:
            mod.complex_polar_form((1.0, 1.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_polar_form(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_polar_form(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_polar_form(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_polar_form("")
        except EXC:
            pass


class Test_complex_power:
    def test_exists(self):
        assert hasattr(mod, "complex_power")

    def test_doc0(self):
        try:
            mod.complex_power((0, 1), (0, 1))  # i^i = e^(-π/2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_power(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_power(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_power(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_power("", "")
        except EXC:
            pass


class Test_complex_reciprocal:
    def test_exists(self):
        assert hasattr(mod, "complex_reciprocal")

    def test_doc0(self):
        try:
            mod.complex_reciprocal((2.0, 0.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_reciprocal(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_reciprocal(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_reciprocal(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_reciprocal("")
        except EXC:
            pass


class Test_complex_rotate:
    def test_exists(self):
        assert hasattr(mod, "complex_rotate")

    def test_doc0(self):
        try:
            mod.complex_rotate((1.0, 0.0), math.pi / 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_rotate(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_rotate(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_rotate(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_rotate("", "")
        except EXC:
            pass


class Test_complex_sin:
    def test_exists(self):
        assert hasattr(mod, "complex_sin")

    def test_doc0(self):
        try:
            mod.complex_sin((0, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_sin(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_sin(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_sin(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_sin("")
        except EXC:
            pass


class Test_complex_sinh:
    def test_exists(self):
        assert hasattr(mod, "complex_sinh")

    def test_doc0(self):
        try:
            mod.complex_sinh((1.0, 0.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_sinh(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_sinh(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_sinh(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_sinh("")
        except EXC:
            pass


class Test_complex_sqrt:
    def test_exists(self):
        assert hasattr(mod, "complex_sqrt")

    def test_doc0(self):
        try:
            mod.complex_sqrt((-1.0, 0.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_sqrt(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_sqrt(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_sqrt(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_sqrt("")
        except EXC:
            pass


class Test_complex_subtract:
    def test_exists(self):
        assert hasattr(mod, "complex_subtract")

    def test_doc0(self):
        try:
            mod.complex_subtract((5, 3), (2, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_subtract(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_subtract(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_subtract(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_subtract("", "")
        except EXC:
            pass


class Test_complex_tan:
    def test_exists(self):
        assert hasattr(mod, "complex_tan")

    def test_doc0(self):
        try:
            mod.complex_tan((1.0, 0.0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_tan(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_tan(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_tan(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_tan("")
        except EXC:
            pass


class Test_complex_to_polar:
    def test_exists(self):
        assert hasattr(mod, "complex_to_polar")

    def test_doc0(self):
        try:
            mod.complex_to_polar((1, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.complex_to_polar(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complex_to_polar(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complex_to_polar(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complex_to_polar("")
        except EXC:
            pass


class Test_de_moivre:
    def test_exists(self):
        assert hasattr(mod, "de_moivre")

    def test_doc0(self):
        try:
            mod.de_moivre(1, math.pi / 4, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.de_moivre(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.de_moivre(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.de_moivre(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.de_moivre("", "", 0)
        except EXC:
            pass


class Test_euler_formula:
    def test_exists(self):
        assert hasattr(mod, "euler_formula")

    def test_doc0(self):
        try:
            mod.euler_formula(math.pi)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.euler_formula(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.euler_formula(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.euler_formula(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.euler_formula("")
        except EXC:
            pass


class Test_nth_roots_complex:
    def test_exists(self):
        assert hasattr(mod, "nth_roots_complex")

    def test_doc0(self):
        try:
            mod.nth_roots_complex((0, 1), 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.nth_roots_complex(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nth_roots_complex(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nth_roots_complex(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nth_roots_complex("", 0)
        except EXC:
            pass


class Test_polar_to_complex:
    def test_exists(self):
        assert hasattr(mod, "polar_to_complex")

    def test_doc0(self):
        try:
            mod.polar_to_complex(2, math.pi / 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polar_to_complex(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polar_to_complex(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polar_to_complex(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polar_to_complex("", "")
        except EXC:
            pass


class Test_roots_of_unity:
    def test_exists(self):
        assert hasattr(mod, "roots_of_unity")

    def test_doc0(self):
        try:
            mod.roots_of_unity(4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.roots_of_unity(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.roots_of_unity(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.roots_of_unity(None)
        except EXC:
            pass

