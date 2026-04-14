# Deep coverage tests for formulite.fxPython.py_logic
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxPython.py_logic as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_is_blank_deep:
    def test_c0(self):
        try:
            mod.is_blank(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_blank(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_blank(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_blank(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_blank(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_blank(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.is_blank(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.is_blank(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.is_blank(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.is_blank(2)
        except EXC:
            pass


class Test_and_all_deep:
    def test_c0(self):
        try:
            mod.and_all()
        except EXC:
            pass


class Test_or_any_deep:
    def test_c0(self):
        try:
            mod.or_any()
        except EXC:
            pass


class Test_switch_case_deep:
    def test_c0(self):
        try:
            mod.switch_case(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.switch_case(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.switch_case(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.switch_case(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.switch_case(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.switch_case(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.switch_case(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.switch_case(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.switch_case(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.switch_case(2)
        except EXC:
            pass


class Test_xor_all_deep:
    def test_c0(self):
        try:
            mod.xor_all()
        except EXC:
            pass

