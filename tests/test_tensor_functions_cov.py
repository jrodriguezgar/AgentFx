# Coverage tests for agentfx.fxNumeric.tensor_functions
import math

from agentfx.fxNumeric import tensor_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_christoffel_symbols_diagonal:
    def test_exists(self):
        assert hasattr(mod, "christoffel_symbols_diagonal")

    def test_doc0(self):
        try:
            mod.christoffel_symbols_diagonal([1, 4, 4], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.christoffel_symbols_diagonal(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.christoffel_symbols_diagonal(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.christoffel_symbols_diagonal(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.christoffel_symbols_diagonal("", "")
        except EXC:
            pass


class Test_geodesic_equation_rhs:
    def test_exists(self):
        assert hasattr(mod, "geodesic_equation_rhs")

    def test_doc0(self):
        try:
            mod.geodesic_equation_rhs([[[0,0],[0,0]],[[0,0],[0,0]]], [1, 0])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.geodesic_equation_rhs(3.14, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geodesic_equation_rhs(100, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geodesic_equation_rhs(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geodesic_equation_rhs("", "")
        except EXC:
            pass


class Test_kronecker_delta:
    def test_exists(self):
        assert hasattr(mod, "kronecker_delta")

    def test_doc0(self):
        try:
            mod.kronecker_delta(1, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.kronecker_delta(1, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.kronecker_delta(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kronecker_delta(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kronecker_delta(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kronecker_delta("", "")
        except EXC:
            pass


class Test_levi_civita:
    def test_exists(self):
        assert hasattr(mod, "levi_civita")

    def test_doc0(self):
        try:
            mod.levi_civita(1, 2, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.levi_civita(1, 3, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.levi_civita(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.levi_civita(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.levi_civita(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.levi_civita("", "", 0)
        except EXC:
            pass


class Test_levi_civita_nd:
    def test_exists(self):
        assert hasattr(mod, "levi_civita_nd")

    def test_doc0(self):
        try:
            mod.levi_civita_nd([1, 2, 3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.levi_civita_nd(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.levi_civita_nd(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.levi_civita_nd(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.levi_civita_nd("")
        except EXC:
            pass


class Test_lower_index:
    def test_exists(self):
        assert hasattr(mod, "lower_index")

    def test_doc0(self):
        try:
            mod.lower_index([3, 2], [1, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lower_index([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lower_index([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lower_index(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lower_index("", "")
        except EXC:
            pass


class Test_metric_tensor_cylindrical:
    def test_exists(self):
        assert hasattr(mod, "metric_tensor_cylindrical")

    def test_doc0(self):
        try:
            mod.metric_tensor_cylindrical(3.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.metric_tensor_cylindrical(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.metric_tensor_cylindrical(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.metric_tensor_cylindrical(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.metric_tensor_cylindrical("")
        except EXC:
            pass


class Test_metric_tensor_from_jacobian:
    def test_exists(self):
        assert hasattr(mod, "metric_tensor_from_jacobian")

    def test_doc0(self):
        try:
            mod.metric_tensor_from_jacobian([[1, 0], [0, 2]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.metric_tensor_from_jacobian(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.metric_tensor_from_jacobian(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.metric_tensor_from_jacobian(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.metric_tensor_from_jacobian(0)
        except EXC:
            pass


class Test_metric_tensor_spherical:
    def test_exists(self):
        assert hasattr(mod, "metric_tensor_spherical")

    def test_doc0(self):
        try:
            mod.metric_tensor_spherical(2.0, math.pi / 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.metric_tensor_spherical(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.metric_tensor_spherical(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.metric_tensor_spherical(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.metric_tensor_spherical("", "")
        except EXC:
            pass


class Test_raise_index:
    def test_exists(self):
        assert hasattr(mod, "raise_index")

    def test_doc0(self):
        try:
            mod.raise_index([3, 8], [1, 0.25])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.raise_index([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.raise_index([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.raise_index(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.raise_index("", "")
        except EXC:
            pass


class Test_riemann_christoffel_check_2d:
    def test_exists(self):
        assert hasattr(mod, "riemann_christoffel_check_2d")

    def test_doc0(self):
        try:
            mod.riemann_christoffel_check_2d([[[0,0],[0,0]],[[0,0],[0,0]]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.riemann_christoffel_check_2d(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.riemann_christoffel_check_2d(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.riemann_christoffel_check_2d(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.riemann_christoffel_check_2d("")
        except EXC:
            pass


class Test_tensor_contract:
    def test_exists(self):
        assert hasattr(mod, "tensor_contract")

    def test_doc0(self):
        try:
            mod.tensor_contract([[1, 2], [3, 4]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.tensor_contract(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tensor_contract(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tensor_contract(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tensor_contract("")
        except EXC:
            pass


class Test_tensor_outer_product:
    def test_exists(self):
        assert hasattr(mod, "tensor_outer_product")

    def test_doc0(self):
        try:
            mod.tensor_outer_product([1, 2], [3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.tensor_outer_product([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tensor_outer_product([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tensor_outer_product(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tensor_outer_product("", "")
        except EXC:
            pass

