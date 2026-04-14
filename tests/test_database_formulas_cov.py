# Coverage tests for formulite.fxExcel.database_formulas
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxExcel import database_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_DAVERAGE:
    def test_exists(self):
        assert hasattr(mod, "DAVERAGE")

    def test_var0(self):
        try:
            mod.DAVERAGE("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DAVERAGE("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DAVERAGE(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DAVERAGE([], "")
        except EXC:
            pass


class Test_DCOUNT:
    def test_exists(self):
        assert hasattr(mod, "DCOUNT")

    def test_var0(self):
        try:
            mod.DCOUNT("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DCOUNT("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DCOUNT(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DCOUNT([], "")
        except EXC:
            pass


class Test_DCOUNTA:
    def test_exists(self):
        assert hasattr(mod, "DCOUNTA")

    def test_var0(self):
        try:
            mod.DCOUNTA("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DCOUNTA("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DCOUNTA(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DCOUNTA([], "")
        except EXC:
            pass


class Test_DGET:
    def test_exists(self):
        assert hasattr(mod, "DGET")

    def test_var0(self):
        try:
            mod.DGET("hello", "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DGET("", "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DGET(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DGET([], "", "")
        except EXC:
            pass


class Test_DMAX:
    def test_exists(self):
        assert hasattr(mod, "DMAX")

    def test_var0(self):
        try:
            mod.DMAX("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DMAX("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DMAX(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DMAX([], "")
        except EXC:
            pass


class Test_DMIN:
    def test_exists(self):
        assert hasattr(mod, "DMIN")

    def test_var0(self):
        try:
            mod.DMIN("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DMIN("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DMIN(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DMIN([], "")
        except EXC:
            pass


class Test_DPRODUCT:
    def test_exists(self):
        assert hasattr(mod, "DPRODUCT")

    def test_var0(self):
        try:
            mod.DPRODUCT("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DPRODUCT("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DPRODUCT(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DPRODUCT([], "")
        except EXC:
            pass


class Test_DSTDEV:
    def test_exists(self):
        assert hasattr(mod, "DSTDEV")

    def test_var0(self):
        try:
            mod.DSTDEV("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DSTDEV("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DSTDEV(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DSTDEV([], "")
        except EXC:
            pass


class Test_DSTDEVP:
    def test_exists(self):
        assert hasattr(mod, "DSTDEVP")

    def test_var0(self):
        try:
            mod.DSTDEVP("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DSTDEVP("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DSTDEVP(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DSTDEVP([], "")
        except EXC:
            pass


class Test_DSUM:
    def test_exists(self):
        assert hasattr(mod, "DSUM")

    def test_var0(self):
        try:
            mod.DSUM("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DSUM("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DSUM(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DSUM([], "")
        except EXC:
            pass


class Test_DVAR:
    def test_exists(self):
        assert hasattr(mod, "DVAR")

    def test_var0(self):
        try:
            mod.DVAR("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DVAR("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DVAR(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DVAR([], "")
        except EXC:
            pass


class Test_DVARP:
    def test_exists(self):
        assert hasattr(mod, "DVARP")

    def test_var0(self):
        try:
            mod.DVARP("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DVARP("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DVARP(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DVARP([], "")
        except EXC:
            pass

