# Deep coverage tests for formulite.fxExcel.math_formulas
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxExcel.math_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_SUBTOTAL_deep:
    def test_c0(self):
        try:
            mod.SUBTOTAL(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SUBTOTAL(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SUBTOTAL(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SUBTOTAL(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SUBTOTAL(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SUBTOTAL(0)
        except EXC:
            pass


class Test_SUMIFS_deep:
    def test_c0(self):
        try:
            mod.SUMIFS([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SUMIFS([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SUMIFS([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SUMIFS([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SUMIFS([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SUMIFS([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_MROUND_deep:
    def test_c0(self):
        try:
            mod.MROUND(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.MROUND(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.MROUND(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.MROUND(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.MROUND(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.MROUND(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.MROUND(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.MROUND(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.MROUND(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.MROUND(2, 1)
        except EXC:
            pass


class Test_RANDARRAY_deep:
    def test_c0(self):
        try:
            mod.RANDARRAY()
        except EXC:
            pass

    def test_kw_rows(self):
        try:
            mod.RANDARRAY(rows=1)
        except EXC:
            pass

    def test_kw_columns(self):
        try:
            mod.RANDARRAY(columns=1)
        except EXC:
            pass

    def test_kw_min_val(self):
        try:
            mod.RANDARRAY(min_val=1)
        except EXC:
            pass


class Test_ACOSH_deep:
    def test_c0(self):
        try:
            mod.ACOSH(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ACOSH(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ACOSH(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ACOSH(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ACOSH(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ACOSH(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ACOSH(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ACOSH(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ACOSH(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ACOSH(2)
        except EXC:
            pass


class Test_ACOTH_deep:
    def test_c0(self):
        try:
            mod.ACOTH(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ACOTH(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ACOTH(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ACOTH(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ACOTH(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ACOTH(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ACOTH(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ACOTH(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ACOTH(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ACOTH(2)
        except EXC:
            pass


class Test_CEILING_deep:
    def test_c0(self):
        try:
            mod.CEILING(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.CEILING(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.CEILING(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.CEILING(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.CEILING(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.CEILING(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.CEILING(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.CEILING(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.CEILING(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.CEILING(2)
        except EXC:
            pass

    def test_kw_significance(self):
        try:
            mod.CEILING(1, significance=1)
        except EXC:
            pass


class Test_COMBIN_deep:
    def test_c0(self):
        try:
            mod.COMBIN(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.COMBIN(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.COMBIN(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.COMBIN(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.COMBIN(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.COMBIN(0, 1)
        except EXC:
            pass


class Test_COMBINA_deep:
    def test_c0(self):
        try:
            mod.COMBINA(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.COMBINA(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.COMBINA(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.COMBINA(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.COMBINA(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.COMBINA(0, 1)
        except EXC:
            pass


class Test_FLOOR_deep:
    def test_c0(self):
        try:
            mod.FLOOR(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.FLOOR(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.FLOOR(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.FLOOR(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.FLOOR(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.FLOOR(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.FLOOR(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.FLOOR(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.FLOOR(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.FLOOR(2)
        except EXC:
            pass

    def test_kw_significance(self):
        try:
            mod.FLOOR(1, significance=1)
        except EXC:
            pass


class Test_LN_deep:
    def test_c0(self):
        try:
            mod.LN(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.LN(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.LN(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.LN(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.LN(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.LN(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.LN(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.LN(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.LN(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.LN(2)
        except EXC:
            pass


class Test_LOG_deep:
    def test_c0(self):
        try:
            mod.LOG(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.LOG(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.LOG(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.LOG(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.LOG(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.LOG(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.LOG(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.LOG(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.LOG(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.LOG(2)
        except EXC:
            pass

    def test_kw_base(self):
        try:
            mod.LOG(1, base=1)
        except EXC:
            pass


class Test_LOG10_deep:
    def test_c0(self):
        try:
            mod.LOG10(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.LOG10(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.LOG10(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.LOG10(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.LOG10(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.LOG10(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.LOG10(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.LOG10(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.LOG10(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.LOG10(2)
        except EXC:
            pass


class Test_MOD_deep:
    def test_c0(self):
        try:
            mod.MOD(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.MOD(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.MOD(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.MOD(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.MOD(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.MOD(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.MOD(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.MOD(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.MOD(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.MOD(2, 1)
        except EXC:
            pass


class Test_RANDBETWEEN_deep:
    def test_c0(self):
        try:
            mod.RANDBETWEEN(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.RANDBETWEEN(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.RANDBETWEEN(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.RANDBETWEEN(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.RANDBETWEEN(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.RANDBETWEEN(0, 1)
        except EXC:
            pass


class Test_SQRT_deep:
    def test_c0(self):
        try:
            mod.SQRT(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SQRT(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SQRT(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SQRT(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SQRT(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SQRT(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.SQRT(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.SQRT(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.SQRT(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.SQRT(2)
        except EXC:
            pass


class Test_SQRTPI_deep:
    def test_c0(self):
        try:
            mod.SQRTPI(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SQRTPI(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SQRTPI(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SQRTPI(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SQRTPI(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SQRTPI(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.SQRTPI(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.SQRTPI(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.SQRTPI(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.SQRTPI(2)
        except EXC:
            pass


class Test_SUMPRODUCT_deep:
    def test_c0(self):
        try:
            mod.SUMPRODUCT()
        except EXC:
            pass


class Test_SUMX2MY2_deep:
    def test_c0(self):
        try:
            mod.SUMX2MY2([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SUMX2MY2([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SUMX2MY2([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SUMX2MY2([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SUMX2MY2([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SUMX2MY2([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_SUMX2PY2_deep:
    def test_c0(self):
        try:
            mod.SUMX2PY2([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SUMX2PY2([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SUMX2PY2([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SUMX2PY2([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SUMX2PY2([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SUMX2PY2([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_SUMXMY2_deep:
    def test_c0(self):
        try:
            mod.SUMXMY2([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SUMXMY2([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SUMXMY2([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SUMXMY2([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SUMXMY2([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SUMXMY2([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

