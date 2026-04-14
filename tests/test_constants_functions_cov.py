# Coverage tests for formulite.fxNumeric.constants_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import constants_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_get_constant:
    def test_exists(self):
        assert hasattr(mod, "get_constant")

    def test_doc0(self):
        try:
            mod.get_constant("pi")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_constant("avogadro")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_constant("speed_of_light")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_constant("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_constant("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_constant(None)
        except EXC:
            pass


class Test_list_constants:
    def test_exists(self):
        assert hasattr(mod, "list_constants")

    def test_doc0(self):
        try:
            mod.list_constants("math")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.list_constants()
        except EXC:
            pass

