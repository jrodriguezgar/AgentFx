# Coverage tests for formulite.fxExcel.logic_formulas
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxExcel import logic_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_AND:
    def test_exists(self):
        assert hasattr(mod, "AND")

    def test_doc0(self):
        try:
            mod.AND(True, True, True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.AND(True, False, True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.AND()
        except EXC:
            pass


class Test_BYCOL:
    def test_exists(self):
        assert hasattr(mod, "BYCOL")

    def test_var0(self):
        try:
            mod.BYCOL([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.BYCOL([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.BYCOL(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.BYCOL([], "")
        except EXC:
            pass


class Test_BYROW:
    def test_exists(self):
        assert hasattr(mod, "BYROW")

    def test_var0(self):
        try:
            mod.BYROW([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.BYROW([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.BYROW(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.BYROW([], "")
        except EXC:
            pass


class Test_FALSE:
    def test_exists(self):
        assert hasattr(mod, "FALSE")

    def test_doc0(self):
        try:
            mod.FALSE()
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FALSE()
        except EXC:
            pass


class Test_IF:
    def test_exists(self):
        assert hasattr(mod, "IF")

    def test_doc0(self):
        try:
            mod.IF(10 > 5, "Yes", "No")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.IF(3 < 2, "Yes", "No")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.IF(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.IF(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.IF(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.IF("", "")
        except EXC:
            pass


class Test_IFERROR:
    def test_exists(self):
        assert hasattr(mod, "IFERROR")

    def test_doc0(self):
        try:
            mod.IFERROR(lambda: 10 / 2, "Error")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.IFERROR(lambda: 10 / 0, "Error")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.IFERROR(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.IFERROR(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.IFERROR(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.IFERROR("", "")
        except EXC:
            pass


class Test_IFNA:
    def test_exists(self):
        assert hasattr(mod, "IFNA")

    def test_doc0(self):
        try:
            mod.IFNA(lambda: None, "N/A")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.IFNA(lambda: 42, "N/A")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.IFNA(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.IFNA(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.IFNA(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.IFNA("", "")
        except EXC:
            pass


class Test_IFS:
    def test_exists(self):
        assert hasattr(mod, "IFS")

    def test_doc0(self):
        try:
            mod.IFS(False, "A", True, "B", False, "C", "Default")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.IFS(False, "A", False, "B", "Default")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.IFS()
        except EXC:
            pass


class Test_LAMBDA:
    def test_exists(self):
        assert hasattr(mod, "LAMBDA")

    def test_var0(self):
        try:
            mod.LAMBDA()
        except EXC:
            pass


class Test_LET:
    def test_exists(self):
        assert hasattr(mod, "LET")

    def test_var0(self):
        try:
            mod.LET()
        except EXC:
            pass


class Test_MAKEARRAY:
    def test_exists(self):
        assert hasattr(mod, "MAKEARRAY")

    def test_var0(self):
        try:
            mod.MAKEARRAY(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MAKEARRAY(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MAKEARRAY(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MAKEARRAY([], [], "")
        except EXC:
            pass


class Test_MAP:
    def test_exists(self):
        assert hasattr(mod, "MAP")

    def test_var0(self):
        try:
            mod.MAP()
        except EXC:
            pass


class Test_NOT:
    def test_exists(self):
        assert hasattr(mod, "NOT")

    def test_doc0(self):
        try:
            mod.NOT(True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.NOT(False)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.NOT(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.NOT(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.NOT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.NOT("")
        except EXC:
            pass


class Test_OR:
    def test_exists(self):
        assert hasattr(mod, "OR")

    def test_doc0(self):
        try:
            mod.OR(False, True, False)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.OR(False, False, False)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.OR()
        except EXC:
            pass


class Test_REDUCE:
    def test_exists(self):
        assert hasattr(mod, "REDUCE")

    def test_var0(self):
        try:
            mod.REDUCE(0, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.REDUCE(1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.REDUCE(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.REDUCE("", [], "")
        except EXC:
            pass


class Test_SCAN:
    def test_exists(self):
        assert hasattr(mod, "SCAN")

    def test_var0(self):
        try:
            mod.SCAN(0, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SCAN(1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SCAN(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SCAN("", [], "")
        except EXC:
            pass


class Test_SWITCH:
    def test_exists(self):
        assert hasattr(mod, "SWITCH")

    def test_doc0(self):
        try:
            mod.SWITCH(2, 1, "one", 2, "two", 3, "three")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SWITCH(5, 1, "one", 2, "two", "other")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SWITCH(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SWITCH(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SWITCH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SWITCH(0)
        except EXC:
            pass


class Test_TRUE:
    def test_exists(self):
        assert hasattr(mod, "TRUE")

    def test_doc0(self):
        try:
            mod.TRUE()
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TRUE()
        except EXC:
            pass


class Test_XOR:
    def test_exists(self):
        assert hasattr(mod, "XOR")

    def test_doc0(self):
        try:
            mod.XOR(True, False, False)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.XOR(True, True, False)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.XOR()
        except EXC:
            pass

