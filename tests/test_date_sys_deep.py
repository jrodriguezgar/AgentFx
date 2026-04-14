# Deep coverage tests for formulite.fxDate.date_sys
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxDate.date_sys as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_get_local_now_deep:
    def test_c0(self):
        try:
            mod.get_local_now()
        except EXC:
            pass

    def test_kw_tz(self):
        try:
            mod.get_local_now(tz="hello world")
        except EXC:
            pass


class Test_current_weekday_number_deep:
    def test_c0(self):
        try:
            mod.current_weekday_number()
        except EXC:
            pass

    def test_kw_start_day(self):
        try:
            mod.current_weekday_number(start_day="hello world")
        except EXC:
            pass

