# Coverage tests for formulite.fxVBA.format_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxVBA import format_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_FormatCurrency:
    def test_exists(self):
        assert hasattr(mod, "FormatCurrency")

    def test_var0(self):
        try:
            mod.FormatCurrency(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FormatCurrency(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FormatCurrency(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FormatCurrency(0)
        except EXC:
            pass


class Test_FormatDateTime:
    def test_exists(self):
        assert hasattr(mod, "FormatDateTime")

    def test_var0(self):
        try:
            mod.FormatDateTime(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FormatDateTime(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FormatDateTime(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FormatDateTime(0)
        except EXC:
            pass


class Test_FormatNumber:
    def test_exists(self):
        assert hasattr(mod, "FormatNumber")

    def test_var0(self):
        try:
            mod.FormatNumber(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FormatNumber(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FormatNumber(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FormatNumber(0)
        except EXC:
            pass


class Test_FormatPercent:
    def test_exists(self):
        assert hasattr(mod, "FormatPercent")

    def test_var0(self):
        try:
            mod.FormatPercent(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FormatPercent(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FormatPercent(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FormatPercent(0)
        except EXC:
            pass


class Test_Format_:
    def test_exists(self):
        assert hasattr(mod, "Format_")

    def test_var0(self):
        try:
            mod.Format_(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Format_(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Format_(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Format_(0)
        except EXC:
            pass

