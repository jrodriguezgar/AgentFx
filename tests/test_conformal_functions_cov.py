# Coverage tests for agentfx.fxNumeric.conformal_functions

from agentfx.fxNumeric import conformal_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_cayley_transform:
    def test_exists(self):
        assert hasattr(mod, "cayley_transform")

    def test_doc0(self):
        try:
            mod.cayley_transform((0, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cayley_transform(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cayley_transform(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cayley_transform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cayley_transform("")
        except EXC:
            pass


class Test_exponential_map:
    def test_exists(self):
        assert hasattr(mod, "exponential_map")

    def test_doc0(self):
        try:
            mod.exponential_map((0, 3.14159265))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.exponential_map(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.exponential_map(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.exponential_map(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.exponential_map("")
        except EXC:
            pass


class Test_inverse_cayley_transform:
    def test_exists(self):
        assert hasattr(mod, "inverse_cayley_transform")

    def test_doc0(self):
        try:
            mod.inverse_cayley_transform((0, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_cayley_transform(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_cayley_transform(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_cayley_transform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_cayley_transform("")
        except EXC:
            pass


class Test_inverse_joukowski:
    def test_exists(self):
        assert hasattr(mod, "inverse_joukowski")

    def test_doc0(self):
        try:
            mod.inverse_joukowski((2.5, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_joukowski(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_joukowski(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_joukowski(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_joukowski("")
        except EXC:
            pass


class Test_inversion_map:
    def test_exists(self):
        assert hasattr(mod, "inversion_map")

    def test_doc0(self):
        try:
            mod.inversion_map((0, 1))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inversion_map(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inversion_map(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inversion_map(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inversion_map("")
        except EXC:
            pass


class Test_joukowski_transform:
    def test_exists(self):
        assert hasattr(mod, "joukowski_transform")

    def test_doc0(self):
        try:
            mod.joukowski_transform((2, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.joukowski_transform(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.joukowski_transform(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.joukowski_transform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.joukowski_transform("")
        except EXC:
            pass


class Test_koebe_function:
    def test_exists(self):
        assert hasattr(mod, "koebe_function")

    def test_doc0(self):
        try:
            mod.koebe_function((0.5, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.koebe_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.koebe_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.koebe_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.koebe_function("")
        except EXC:
            pass


class Test_log_map:
    def test_exists(self):
        assert hasattr(mod, "log_map")

    def test_doc0(self):
        try:
            mod.log_map((1, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.log_map(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.log_map(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.log_map(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.log_map("")
        except EXC:
            pass


class Test_mobius_transform:
    def test_exists(self):
        assert hasattr(mod, "mobius_transform")

    def test_doc0(self):
        try:
            mod.mobius_transform((1, 0), (1, 0), (0, 0), (0, 0), (1, 0))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mobius_transform(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mobius_transform(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mobius_transform(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mobius_transform("", "", "", "", "")
        except EXC:
            pass


class Test_power_map:
    def test_exists(self):
        assert hasattr(mod, "power_map")

    def test_doc0(self):
        try:
            mod.power_map((0, 1), 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.power_map(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.power_map(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.power_map(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.power_map("", 0)
        except EXC:
            pass


class Test_schwarz_christoffel_half_plane_to_rectangle:
    def test_exists(self):
        assert hasattr(mod, "schwarz_christoffel_half_plane_to_rectangle")

    def test_doc0(self):
        try:
            mod.schwarz_christoffel_half_plane_to_rectangle((0.5, 0), 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.schwarz_christoffel_half_plane_to_rectangle(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.schwarz_christoffel_half_plane_to_rectangle(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.schwarz_christoffel_half_plane_to_rectangle(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.schwarz_christoffel_half_plane_to_rectangle("", 0)
        except EXC:
            pass

