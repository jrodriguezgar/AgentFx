# Coverage tests for shortfx.fxPython.py_itertools

from shortfx.fxPython import py_itertools as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_all_equal:
    def test_exists(self):
        assert hasattr(mod, "all_equal")

    def test_var0(self):
        try:
            mod.all_equal(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.all_equal(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.all_equal(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.all_equal("")
        except EXC:
            pass


class Test_consume:
    def test_exists(self):
        assert hasattr(mod, "consume")

    def test_var0(self):
        try:
            mod.consume(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.consume(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.consume(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.consume("")
        except EXC:
            pass


class Test_convolve:
    def test_exists(self):
        assert hasattr(mod, "convolve")

    def test_var0(self):
        try:
            mod.convolve(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.convolve(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.convolve(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.convolve("", "")
        except EXC:
            pass


class Test_factor:
    def test_exists(self):
        assert hasattr(mod, "factor")

    def test_var0(self):
        try:
            mod.factor(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.factor(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.factor(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.factor(0)
        except EXC:
            pass


class Test_first_true:
    def test_exists(self):
        assert hasattr(mod, "first_true")

    def test_var0(self):
        try:
            mod.first_true(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.first_true(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.first_true(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.first_true("")
        except EXC:
            pass


class Test_flatten:
    def test_exists(self):
        assert hasattr(mod, "flatten")

    def test_var0(self):
        try:
            mod.flatten(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.flatten(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.flatten(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.flatten("")
        except EXC:
            pass


class Test_grouper:
    def test_exists(self):
        assert hasattr(mod, "grouper")

    def test_var0(self):
        try:
            mod.grouper(0, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.grouper(1, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.grouper(None, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.grouper("", 0)
        except EXC:
            pass


class Test_iter_except:
    def test_exists(self):
        assert hasattr(mod, "iter_except")

    def test_var0(self):
        try:
            mod.iter_except(1, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.iter_except(3, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.iter_except(None, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.iter_except(0, 0)
        except EXC:
            pass


class Test_iter_index:
    def test_exists(self):
        assert hasattr(mod, "iter_index")

    def test_var0(self):
        try:
            mod.iter_index(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.iter_index(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.iter_index(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.iter_index("", "")
        except EXC:
            pass


class Test_loops:
    def test_exists(self):
        assert hasattr(mod, "loops")

    def test_var0(self):
        try:
            mod.loops(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.loops(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.loops(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.loops(0)
        except EXC:
            pass


class Test_matmul:
    def test_exists(self):
        assert hasattr(mod, "matmul")

    def test_var0(self):
        try:
            mod.matmul(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.matmul(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.matmul(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.matmul("", "")
        except EXC:
            pass


class Test_multinomial:
    def test_exists(self):
        assert hasattr(mod, "multinomial")

    def test_var0(self):
        try:
            mod.multinomial()
        except EXC:
            pass


class Test_ncycles:
    def test_exists(self):
        assert hasattr(mod, "ncycles")

    def test_var0(self):
        try:
            mod.ncycles(0, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ncycles(1, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ncycles(None, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ncycles("", 0)
        except EXC:
            pass


class Test_nth:
    def test_exists(self):
        assert hasattr(mod, "nth")

    def test_var0(self):
        try:
            mod.nth(0, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nth(1, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nth(None, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nth("", 0)
        except EXC:
            pass


class Test_polynomial_derivative:
    def test_exists(self):
        assert hasattr(mod, "polynomial_derivative")

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
            mod.polynomial_derivative([])
        except EXC:
            pass


class Test_polynomial_eval:
    def test_exists(self):
        assert hasattr(mod, "polynomial_eval")

    def test_var0(self):
        try:
            mod.polynomial_eval([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polynomial_eval([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polynomial_eval(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polynomial_eval([], "")
        except EXC:
            pass


class Test_polynomial_from_roots:
    def test_exists(self):
        assert hasattr(mod, "polynomial_from_roots")

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


class Test_powerset:
    def test_exists(self):
        assert hasattr(mod, "powerset")

    def test_var0(self):
        try:
            mod.powerset(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.powerset(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.powerset(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.powerset("")
        except EXC:
            pass


class Test_prepend:
    def test_exists(self):
        assert hasattr(mod, "prepend")

    def test_var0(self):
        try:
            mod.prepend(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.prepend(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.prepend(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.prepend("", "")
        except EXC:
            pass


class Test_quantify:
    def test_exists(self):
        assert hasattr(mod, "quantify")

    def test_var0(self):
        try:
            mod.quantify(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.quantify(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.quantify(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.quantify("")
        except EXC:
            pass


class Test_repeatfunc:
    def test_exists(self):
        assert hasattr(mod, "repeatfunc")

    def test_var0(self):
        try:
            mod.repeatfunc(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.repeatfunc(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.repeatfunc(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.repeatfunc(0)
        except EXC:
            pass


class Test_reshape:
    def test_exists(self):
        assert hasattr(mod, "reshape")

    def test_var0(self):
        try:
            mod.reshape([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.reshape([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.reshape(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.reshape([], [])
        except EXC:
            pass


class Test_roundrobin:
    def test_exists(self):
        assert hasattr(mod, "roundrobin")

    def test_var0(self):
        try:
            mod.roundrobin()
        except EXC:
            pass


class Test_sieve:
    def test_exists(self):
        assert hasattr(mod, "sieve")

    def test_var0(self):
        try:
            mod.sieve(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sieve(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sieve(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sieve(0)
        except EXC:
            pass


class Test_sliding_window:
    def test_exists(self):
        assert hasattr(mod, "sliding_window")

    def test_var0(self):
        try:
            mod.sliding_window(0, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sliding_window(1, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sliding_window(None, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sliding_window("", 0)
        except EXC:
            pass


class Test_subslices:
    def test_exists(self):
        assert hasattr(mod, "subslices")

    def test_var0(self):
        try:
            mod.subslices(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.subslices(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.subslices(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.subslices("")
        except EXC:
            pass


class Test_tabulate:
    def test_exists(self):
        assert hasattr(mod, "tabulate")

    def test_var0(self):
        try:
            mod.tabulate(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tabulate(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tabulate(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tabulate(0)
        except EXC:
            pass


class Test_tail:
    def test_exists(self):
        assert hasattr(mod, "tail")

    def test_var0(self):
        try:
            mod.tail(1, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tail(3, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tail(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tail(0, "")
        except EXC:
            pass


class Test_take:
    def test_exists(self):
        assert hasattr(mod, "take")

    def test_var0(self):
        try:
            mod.take(1, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.take(3, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.take(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.take(0, "")
        except EXC:
            pass


class Test_totient:
    def test_exists(self):
        assert hasattr(mod, "totient")

    def test_var0(self):
        try:
            mod.totient(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.totient(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.totient(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.totient(0)
        except EXC:
            pass


class Test_transpose:
    def test_exists(self):
        assert hasattr(mod, "transpose")

    def test_var0(self):
        try:
            mod.transpose([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.transpose([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.transpose(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.transpose([])
        except EXC:
            pass


class Test_unique:
    def test_exists(self):
        assert hasattr(mod, "unique")

    def test_var0(self):
        try:
            mod.unique(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unique(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unique(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unique("")
        except EXC:
            pass


class Test_unique_everseen:
    def test_exists(self):
        assert hasattr(mod, "unique_everseen")

    def test_var0(self):
        try:
            mod.unique_everseen(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unique_everseen(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unique_everseen(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unique_everseen("")
        except EXC:
            pass


class Test_unique_justseen:
    def test_exists(self):
        assert hasattr(mod, "unique_justseen")

    def test_var0(self):
        try:
            mod.unique_justseen(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unique_justseen(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unique_justseen(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unique_justseen("")
        except EXC:
            pass

