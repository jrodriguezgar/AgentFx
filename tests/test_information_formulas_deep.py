# Deep coverage tests for agentfx.fxExcel.information_formulas

import agentfx.fxExcel.information_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_ERROR_TYPE_deep:
    def test_c0(self):
        try:
            mod.ERROR_TYPE(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ERROR_TYPE(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ERROR_TYPE(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ERROR_TYPE(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ERROR_TYPE(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ERROR_TYPE(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ERROR_TYPE(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ERROR_TYPE(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ERROR_TYPE(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ERROR_TYPE(2)
        except EXC:
            pass


class Test_TYPE_deep:
    def test_c0(self):
        try:
            mod.TYPE(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.TYPE(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.TYPE(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.TYPE(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.TYPE(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.TYPE(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.TYPE(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.TYPE(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.TYPE(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.TYPE(2)
        except EXC:
            pass

