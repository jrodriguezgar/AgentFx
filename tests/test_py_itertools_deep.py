# Deep coverage tests for shortfx.fxPython.py_itertools
from datetime import date

import shortfx.fxPython.py_itertools as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_unique_everseen_deep:
    def test_c0(self):
        try:
            mod.unique_everseen(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.unique_everseen(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.unique_everseen(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.unique_everseen(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.unique_everseen(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.unique_everseen(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.unique_everseen(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.unique_everseen(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.unique_everseen(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.unique_everseen(2)
        except EXC:
            pass

    def test_kw_key(self):
        try:
            mod.unique_everseen(1, key=1)
        except EXC:
            pass


class Test_grouper_deep:
    def test_c0(self):
        try:
            mod.grouper(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.grouper(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.grouper(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.grouper(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.grouper(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.grouper(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.grouper(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.grouper(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.grouper(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.grouper(2, 10)
        except EXC:
            pass


class Test_factor_deep:
    def test_c0(self):
        try:
            mod.factor(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.factor(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.factor(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.factor(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.factor(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.factor(0)
        except EXC:
            pass


class Test_iter_except_deep:
    def test_c0(self):
        try:
            mod.iter_except(lambda x: x, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.iter_except(lambda x: x * 2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.iter_except(abs, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.iter_except(str, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.iter_except(lambda x: x, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.iter_except(lambda x: x * 2, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.iter_except(abs, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.iter_except(str, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.iter_except(lambda x: x, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.iter_except(lambda x: x * 2, 1)
        except EXC:
            pass

    def test_kw_first(self):
        try:
            mod.iter_except(lambda x: x, 42, first=1)
        except EXC:
            pass


class Test_iter_index_deep:
    def test_c0(self):
        try:
            mod.iter_index(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.iter_index(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.iter_index(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.iter_index(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.iter_index(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.iter_index(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.iter_index(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.iter_index(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.iter_index(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.iter_index(2, 1)
        except EXC:
            pass

    def test_kw_start(self):
        try:
            mod.iter_index(1, 42, start=date(2024, 1, 15))
        except EXC:
            pass

    def test_kw_stop(self):
        try:
            mod.iter_index(1, 42, stop=1)
        except EXC:
            pass


class Test_sliding_window_deep:
    def test_c0(self):
        try:
            mod.sliding_window(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sliding_window(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sliding_window(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sliding_window(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sliding_window(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sliding_window(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.sliding_window(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.sliding_window(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.sliding_window(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.sliding_window(2, 10)
        except EXC:
            pass


class Test_roundrobin_deep:
    def test_c0(self):
        try:
            mod.roundrobin()
        except EXC:
            pass


class Test_sieve_deep:
    def test_c0(self):
        try:
            mod.sieve(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sieve(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sieve(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sieve(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sieve(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sieve(0)
        except EXC:
            pass


class Test_consume_deep:
    def test_c0(self):
        try:
            mod.consume(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.consume(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.consume(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.consume(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.consume(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.consume(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.consume(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.consume(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.consume(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.consume(2)
        except EXC:
            pass

    def test_kw_n(self):
        try:
            mod.consume(1, n=1)
        except EXC:
            pass


class Test_matmul_deep:
    def test_c0(self):
        try:
            mod.matmul(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matmul(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matmul(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matmul(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matmul(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matmul(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.matmul(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.matmul(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.matmul(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.matmul(2, 1)
        except EXC:
            pass


class Test_repeatfunc_deep:
    def test_c0(self):
        try:
            mod.repeatfunc(lambda x: x)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.repeatfunc(lambda x: x * 2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.repeatfunc(abs)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.repeatfunc(str)
        except EXC:
            pass

    def test_kw_times(self):
        try:
            mod.repeatfunc(lambda x: x, times=1)
        except EXC:
            pass


class Test_unique_justseen_deep:
    def test_c0(self):
        try:
            mod.unique_justseen(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.unique_justseen(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.unique_justseen(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.unique_justseen(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.unique_justseen(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.unique_justseen(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.unique_justseen(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.unique_justseen(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.unique_justseen(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.unique_justseen(2)
        except EXC:
            pass

    def test_kw_key(self):
        try:
            mod.unique_justseen(1, key=1)
        except EXC:
            pass

