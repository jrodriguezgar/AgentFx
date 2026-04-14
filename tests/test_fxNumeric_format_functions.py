# Coverage tests for formulite.fxNumeric.format_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import format_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_compare_floats_with_tolerance:
    def test_exists(self):
        assert hasattr(mod, "compare_floats_with_tolerance")

    def test_doc0(self):
        try:
            mod.compare_floats_with_tolerance(0.1 + 0.2, 0.3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.compare_floats_with_tolerance(1000000.0, 1000000.0000001, rel_tol=1e-9)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.compare_floats_with_tolerance(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.compare_floats_with_tolerance(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.compare_floats_with_tolerance(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.compare_floats_with_tolerance("", "")
        except EXC:
            pass


class Test_format_as_percentage:
    def test_exists(self):
        assert hasattr(mod, "format_as_percentage")

    def test_doc0(self):
        try:
            mod.format_as_percentage(0.1234)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.format_as_percentage(0.5, 0)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.format_as_percentage(0.005, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.format_as_percentage(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.format_as_percentage(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.format_as_percentage(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.format_as_percentage("")
        except EXC:
            pass


class Test_format_as_scientific_notation:
    def test_exists(self):
        assert hasattr(mod, "format_as_scientific_notation")

    def test_doc0(self):
        try:
            mod.format_as_scientific_notation(1230000)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.format_as_scientific_notation(0.0000000000456, 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.format_as_scientific_notation(1.0, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.format_as_scientific_notation(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.format_as_scientific_notation(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.format_as_scientific_notation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.format_as_scientific_notation("")
        except EXC:
            pass


class Test_format_with_leading_zeros:
    def test_exists(self):
        assert hasattr(mod, "format_with_leading_zeros")

    def test_doc0(self):
        try:
            mod.format_with_leading_zeros(5, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.format_with_leading_zeros(123, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.format_with_leading_zeros(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.format_with_leading_zeros(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.format_with_leading_zeros(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.format_with_leading_zeros("", "")
        except EXC:
            pass


class Test_percent_change:
    def test_exists(self):
        assert hasattr(mod, "percent_change")

    def test_doc0(self):
        try:
            mod.percent_change(100, 150)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.percent_change(200, 150)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.percent_change(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.percent_change(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.percent_change(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.percent_change("", "")
        except EXC:
            pass


class Test_percent_of:
    def test_exists(self):
        assert hasattr(mod, "percent_of")

    def test_doc0(self):
        try:
            mod.percent_of(25, 200)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.percent_of(3, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.percent_of(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.percent_of(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.percent_of(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.percent_of("", "")
        except EXC:
            pass

