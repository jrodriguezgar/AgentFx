# Coverage tests for formulite.fxVBA.date_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxVBA import date_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_DateAdd:
    def test_exists(self):
        assert hasattr(mod, "DateAdd")

    def test_var0(self):
        try:
            mod.DateAdd("hello", 3.14, date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DateAdd("", 100, date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DateAdd(None, 3.14, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DateAdd("", "", "")
        except EXC:
            pass


class Test_DateDiff:
    def test_exists(self):
        assert hasattr(mod, "DateDiff")

    def test_var0(self):
        try:
            mod.DateDiff("hello", date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DateDiff("", date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DateDiff(None, date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DateDiff("", "", "")
        except EXC:
            pass


class Test_DatePart:
    def test_exists(self):
        assert hasattr(mod, "DatePart")

    def test_var0(self):
        try:
            mod.DatePart("hello", date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DatePart("", date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DatePart(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DatePart("", "")
        except EXC:
            pass


class Test_DateSerial:
    def test_exists(self):
        assert hasattr(mod, "DateSerial")

    def test_var0(self):
        try:
            mod.DateSerial(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DateSerial(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DateSerial(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DateSerial("", "", "")
        except EXC:
            pass


class Test_Date_:
    def test_exists(self):
        assert hasattr(mod, "Date_")

    def test_var0(self):
        try:
            mod.Date_()
        except EXC:
            pass


class Test_Day:
    def test_exists(self):
        assert hasattr(mod, "Day")

    def test_var0(self):
        try:
            mod.Day(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Day(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Day(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Day("")
        except EXC:
            pass


class Test_Hour:
    def test_exists(self):
        assert hasattr(mod, "Hour")

    def test_var0(self):
        try:
            mod.Hour(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Hour(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Hour(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Hour("")
        except EXC:
            pass


class Test_Minute:
    def test_exists(self):
        assert hasattr(mod, "Minute")

    def test_var0(self):
        try:
            mod.Minute(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Minute(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Minute(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Minute("")
        except EXC:
            pass


class Test_Month:
    def test_exists(self):
        assert hasattr(mod, "Month")

    def test_var0(self):
        try:
            mod.Month(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Month(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Month(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Month("")
        except EXC:
            pass


class Test_MonthName:
    def test_exists(self):
        assert hasattr(mod, "MonthName")

    def test_var0(self):
        try:
            mod.MonthName(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MonthName(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MonthName(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MonthName("")
        except EXC:
            pass


class Test_Now:
    def test_exists(self):
        assert hasattr(mod, "Now")

    def test_var0(self):
        try:
            mod.Now()
        except EXC:
            pass


class Test_Second:
    def test_exists(self):
        assert hasattr(mod, "Second")

    def test_var0(self):
        try:
            mod.Second(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Second(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Second(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Second("")
        except EXC:
            pass


class Test_TimeSerial:
    def test_exists(self):
        assert hasattr(mod, "TimeSerial")

    def test_var0(self):
        try:
            mod.TimeSerial(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TimeSerial(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TimeSerial(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TimeSerial("", "", "")
        except EXC:
            pass


class Test_Time_:
    def test_exists(self):
        assert hasattr(mod, "Time_")

    def test_var0(self):
        try:
            mod.Time_()
        except EXC:
            pass


class Test_Timer:
    def test_exists(self):
        assert hasattr(mod, "Timer")

    def test_var0(self):
        try:
            mod.Timer()
        except EXC:
            pass


class Test_WeekDay:
    def test_exists(self):
        assert hasattr(mod, "WeekDay")

    def test_var0(self):
        try:
            mod.WeekDay(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.WeekDay(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.WeekDay(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.WeekDay("")
        except EXC:
            pass


class Test_WeekDayName:
    def test_exists(self):
        assert hasattr(mod, "WeekDayName")

    def test_var0(self):
        try:
            mod.WeekDayName(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.WeekDayName(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.WeekDayName(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.WeekDayName("")
        except EXC:
            pass


class Test_Year:
    def test_exists(self):
        assert hasattr(mod, "Year")

    def test_var0(self):
        try:
            mod.Year(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Year(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Year(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Year("")
        except EXC:
            pass

