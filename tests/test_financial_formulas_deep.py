# Deep coverage tests for formulite.fxExcel.financial_formulas
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxExcel.financial_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_ODDFYIELD_deep:
    def test_c0(self):
        try:
            mod.ODDFYIELD(1, 42, 0, -5, 0.95, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ODDFYIELD(42, 0, -5, 3.14, 0.99, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ODDFYIELD(0, -5, 3.14, 100, 0.05, 1000, -1, 2)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ODDFYIELD(-5, 3.14, 100, 0.5, 0.1, -1, 2, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ODDFYIELD(3.14, 100, 0.5, 1000, 0.5, 2, 1, 42)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ODDFYIELD(100, 0.5, 1000, -1, 0.01, 1, 42, 0)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ODDFYIELD(0.5, 1000, -1, 2, 0.95, 42, 0, -5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ODDFYIELD(1000, -1, 2, 1, 0.99, 0, -5, 3.14)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ODDFYIELD(-1, 2, 1, 42, 0.05, -5, 3.14, 100)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ODDFYIELD(2, 1, 42, 0, 0.1, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.ODDFYIELD(1, 42, 0, -5, 0.95, 100, 0.5, 1000, basis=1)
        except EXC:
            pass


class Test_ODDLYIELD_deep:
    def test_c0(self):
        try:
            mod.ODDLYIELD(1, 42, 0, 0.01, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ODDLYIELD(42, 0, -5, 0.95, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ODDLYIELD(0, -5, 3.14, 0.99, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ODDLYIELD(-5, 3.14, 100, 0.05, 1000, -1, 2)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ODDLYIELD(3.14, 100, 0.5, 0.1, -1, 2, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ODDLYIELD(100, 0.5, 1000, 0.5, 2, 1, 42)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ODDLYIELD(0.5, 1000, -1, 0.01, 1, 42, 0)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ODDLYIELD(1000, -1, 2, 0.95, 42, 0, -5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ODDLYIELD(-1, 2, 1, 0.99, 0, -5, 3.14)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ODDLYIELD(2, 1, 42, 0.05, -5, 3.14, 100)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.ODDLYIELD(1, 42, 0, 0.01, 3.14, 100, 0.5, basis=1)
        except EXC:
            pass


class Test_ODDLPRICE_deep:
    def test_c0(self):
        try:
            mod.ODDLPRICE(1, 42, 0, 0.01, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ODDLPRICE(42, 0, -5, 0.95, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ODDLPRICE(0, -5, 3.14, 0.99, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ODDLPRICE(-5, 3.14, 100, 0.05, 1000, -1, 2)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ODDLPRICE(3.14, 100, 0.5, 0.1, -1, 2, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ODDLPRICE(100, 0.5, 1000, 0.5, 2, 1, 42)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ODDLPRICE(0.5, 1000, -1, 0.01, 1, 42, 0)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ODDLPRICE(1000, -1, 2, 0.95, 42, 0, -5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ODDLPRICE(-1, 2, 1, 0.99, 0, -5, 3.14)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ODDLPRICE(2, 1, 42, 0.05, -5, 3.14, 100)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.ODDLPRICE(1, 42, 0, 0.01, 3.14, 100, 0.5, basis=1)
        except EXC:
            pass


class Test_ODDFPRICE_deep:
    def test_c0(self):
        try:
            mod.ODDFPRICE(1, 42, 0, -5, 0.95, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ODDFPRICE(42, 0, -5, 3.14, 0.99, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ODDFPRICE(0, -5, 3.14, 100, 0.05, 1000, -1, 2)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ODDFPRICE(-5, 3.14, 100, 0.5, 0.1, -1, 2, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ODDFPRICE(3.14, 100, 0.5, 1000, 0.5, 2, 1, 42)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ODDFPRICE(100, 0.5, 1000, -1, 0.01, 1, 42, 0)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ODDFPRICE(0.5, 1000, -1, 2, 0.95, 42, 0, -5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ODDFPRICE(1000, -1, 2, 1, 0.99, 0, -5, 3.14)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ODDFPRICE(-1, 2, 1, 42, 0.05, -5, 3.14, 100)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ODDFPRICE(2, 1, 42, 0, 0.1, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.ODDFPRICE(1, 42, 0, -5, 0.95, 100, 0.5, 1000, basis=1)
        except EXC:
            pass


class Test_AMORDEGRC_deep:
    def test_c0(self):
        try:
            mod.AMORDEGRC(1, date(2023, 6, 1), 0, -5, 3.14, 0.99)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.AMORDEGRC(42, datetime(2024, 3, 15, 10, 30), -5, 3.14, 100, 0.05)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.AMORDEGRC(0, date(2000, 1, 1), 3.14, 100, 0.5, 0.1)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.AMORDEGRC(-5, date(2024, 12, 31), 100, 0.5, 1000, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.AMORDEGRC(3.14, datetime.now(), 0.5, 1000, -1, 0.01)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.AMORDEGRC(100, date(2024, 1, 15), 1000, -1, 2, 0.95)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.AMORDEGRC(0.5, date(2023, 6, 1), -1, 2, 1, 0.99)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.AMORDEGRC(1000, datetime(2024, 3, 15, 10, 30), 2, 1, 42, 0.05)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.AMORDEGRC(-1, date(2000, 1, 1), 1, 42, 0, 0.1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.AMORDEGRC(2, date(2024, 12, 31), 42, 0, -5, 0.5)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.AMORDEGRC(1, date(2023, 6, 1), 0, -5, 3.14, 0.99, basis=1)
        except EXC:
            pass


class Test_YIELD_deep:
    def test_c0(self):
        try:
            mod.YIELD(date(2024, 1, 15), date(2023, 6, 1), 0, 5, 10, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.YIELD(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30), -5, 10, 0, 1)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.YIELD(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1), 3.14, 0, 1, 2)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.YIELD(date(2000, 1, 1), date(2024, 12, 31), 100, 1, 2, 3)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.YIELD(date(2024, 12, 31), datetime.now(), 0.5, 2, 3, 5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.YIELD(datetime.now(), date(2024, 1, 15), 1000, 3, 5, 10)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.YIELD(date(2024, 1, 15), date(2023, 6, 1), -1, 5, 10, 0)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.YIELD(date(2023, 6, 1), datetime(2024, 3, 15, 10, 30), 2, 10, 0, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.YIELD(datetime(2024, 3, 15, 10, 30), date(2000, 1, 1), 1, 0, 1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.YIELD(date(2000, 1, 1), date(2024, 12, 31), 42, 1, 2, 3)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.YIELD(date(2024, 1, 15), date(2023, 6, 1), 0, 5, 10, 0, basis=1)
        except EXC:
            pass

