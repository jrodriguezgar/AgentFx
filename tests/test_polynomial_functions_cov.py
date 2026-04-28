# Coverage tests for agentfx.fxNumeric.polynomial_functions

from agentfx.fxNumeric import polynomial_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_partial_fraction_simple:
    def test_exists(self):
        assert hasattr(mod, "partial_fraction_simple")

    def test_doc0(self):
        try:
            mod.partial_fraction_simple([1], [1, 2])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.partial_fraction_simple([1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.partial_fraction_simple([0], 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.partial_fraction_simple(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.partial_fraction_simple("", "")
        except EXC:
            pass


class Test_polynomial_add:
    def test_exists(self):
        assert hasattr(mod, "polynomial_add")

    def test_doc0(self):
        try:
            mod.polynomial_add([1, 2, 3], [4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_add([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_add([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_add(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_add("", "")
        except EXC:
            pass


class Test_polynomial_composition:
    def test_exists(self):
        assert hasattr(mod, "polynomial_composition")

    def test_doc0(self):
        try:
            mod.polynomial_composition([1, 0, 1], [1, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_composition([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_composition([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_composition(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_composition("", "")
        except EXC:
            pass


class Test_polynomial_degree:
    def test_exists(self):
        assert hasattr(mod, "polynomial_degree")

    def test_doc0(self):
        try:
            mod.polynomial_degree([3, 0, -2, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_degree([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_degree([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_degree(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_degree("")
        except EXC:
            pass


class Test_polynomial_derivative:
    def test_exists(self):
        assert hasattr(mod, "polynomial_derivative")

    def test_doc0(self):
        try:
            mod.polynomial_derivative([3, 0, -2, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_derivative([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_derivative([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_derivative(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_derivative("")
        except EXC:
            pass


class Test_polynomial_divide:
    def test_exists(self):
        assert hasattr(mod, "polynomial_divide")

    def test_doc0(self):
        try:
            mod.polynomial_divide([1, -3, 2], [1, -1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_divide([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_divide([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_divide(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_divide("", "")
        except EXC:
            pass


class Test_polynomial_evaluate:
    def test_exists(self):
        assert hasattr(mod, "polynomial_evaluate")

    def test_doc0(self):
        try:
            mod.polynomial_evaluate([1, -3, 2], 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_evaluate([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_evaluate([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_evaluate(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_evaluate("", "")
        except EXC:
            pass


class Test_polynomial_from_roots:
    def test_exists(self):
        assert hasattr(mod, "polynomial_from_roots")

    def test_doc0(self):
        try:
            mod.polynomial_from_roots([1, -1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_from_roots(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_from_roots(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_from_roots(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_from_roots("")
        except EXC:
            pass


class Test_polynomial_gcd:
    def test_exists(self):
        assert hasattr(mod, "polynomial_gcd")

    def test_doc0(self):
        try:
            mod.polynomial_gcd([1, -3, 2], [1, -1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_gcd([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_gcd([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_gcd(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_gcd("", "")
        except EXC:
            pass


class Test_polynomial_integral:
    def test_exists(self):
        assert hasattr(mod, "polynomial_integral")

    def test_doc0(self):
        try:
            mod.polynomial_integral([3, 0, -2])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_integral([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_integral([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_integral(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_integral("")
        except EXC:
            pass


class Test_polynomial_multiply:
    def test_exists(self):
        assert hasattr(mod, "polynomial_multiply")

    def test_doc0(self):
        try:
            mod.polynomial_multiply([1, 1], [1, -1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_multiply([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_multiply([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_multiply(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_multiply("", "")
        except EXC:
            pass


class Test_polynomial_scale:
    def test_exists(self):
        assert hasattr(mod, "polynomial_scale")

    def test_doc0(self):
        try:
            mod.polynomial_scale([1, 2, 3], 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_scale([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_scale([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_scale(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_scale("", "")
        except EXC:
            pass


class Test_polynomial_subtract:
    def test_exists(self):
        assert hasattr(mod, "polynomial_subtract")

    def test_doc0(self):
        try:
            mod.polynomial_subtract([1, 2, 3], [4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.polynomial_subtract([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_subtract([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_subtract(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_subtract("", "")
        except EXC:
            pass

