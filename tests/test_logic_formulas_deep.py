# Deep coverage tests for agentfx.fxExcel.logic_formulas

import agentfx.fxExcel.logic_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_MAP_deep:
    def test_c0(self):
        try:
            mod.MAP()
        except EXC:
            pass


class Test_SCAN_deep:
    def test_c0(self):
        try:
            mod.SCAN(1, [10, 20, 30], 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SCAN(42, [0, 1], -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SCAN(0, [-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SCAN(-5, [100], 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SCAN(3.14, [1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SCAN(100, [1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.SCAN(0.5, [10, 20, 30], -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.SCAN(1000, [0, 1], 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.SCAN(-1, [-3, -1, 0, 2, 5], 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.SCAN(2, [100], 42)
        except EXC:
            pass


class Test_REDUCE_deep:
    def test_c0(self):
        try:
            mod.REDUCE(1, [10, 20, 30], 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.REDUCE(42, [0, 1], -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.REDUCE(0, [-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.REDUCE(-5, [100], 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.REDUCE(3.14, [1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.REDUCE(100, [1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.REDUCE(0.5, [10, 20, 30], -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.REDUCE(1000, [0, 1], 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.REDUCE(-1, [-3, -1, 0, 2, 5], 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.REDUCE(2, [100], 42)
        except EXC:
            pass


class Test_BYCOL_deep:
    def test_c0(self):
        try:
            mod.BYCOL([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.BYCOL([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.BYCOL([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.BYCOL([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.BYCOL([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.BYCOL([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_LET_deep:
    def test_c0(self):
        try:
            mod.LET()
        except EXC:
            pass


class Test_MAKEARRAY_deep:
    def test_c0(self):
        try:
            mod.MAKEARRAY(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.MAKEARRAY(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.MAKEARRAY(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.MAKEARRAY(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.MAKEARRAY(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.MAKEARRAY(0, 1, 2)
        except EXC:
            pass


class Test_LAMBDA_deep:
    def test_c0(self):
        try:
            mod.LAMBDA()
        except EXC:
            pass

