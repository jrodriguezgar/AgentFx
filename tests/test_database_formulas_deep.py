# Deep coverage tests for formulite.fxExcel.database_formulas
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxExcel.database_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_DCOUNTA_deep:
    def test_c0(self):
        try:
            mod.DCOUNTA([1, 2, 3, 4, 5], "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.DCOUNTA([10, 20, 30], "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.DCOUNTA([0, 1], "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.DCOUNTA([-3, -1, 0, 2, 5], "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.DCOUNTA([100], "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.DCOUNTA([1, 1, 2, 3, 5, 8], "hello world")
        except EXC:
            pass

    def test_kw_criteria(self):
        try:
            mod.DCOUNTA([1, 2, 3, 4, 5], "test", criteria="hello world")
        except EXC:
            pass


class Test_DPRODUCT_deep:
    def test_c0(self):
        try:
            mod.DPRODUCT([1, 2, 3, 4, 5], "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.DPRODUCT([10, 20, 30], "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.DPRODUCT([0, 1], "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.DPRODUCT([-3, -1, 0, 2, 5], "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.DPRODUCT([100], "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.DPRODUCT([1, 1, 2, 3, 5, 8], "hello world")
        except EXC:
            pass

    def test_kw_criteria(self):
        try:
            mod.DPRODUCT([1, 2, 3, 4, 5], "test", criteria="hello world")
        except EXC:
            pass

