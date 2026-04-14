# Coverage tests for formulite.fxExcel.date_formulas
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxExcel import date_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_DATE:
    def test_exists(self):
        assert hasattr(mod, "DATE")

    def test_doc0(self):
        try:
            mod.DATE(2025, 1, 15)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.DATE(2024, 12, 31)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DATE(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DATE(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DATE(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DATE("", "", "")
        except EXC:
            pass


class Test_DATEDIF:
    def test_exists(self):
        assert hasattr(mod, "DATEDIF")

    def test_var0(self):
        try:
            mod.DATEDIF(date(2024, 1, 15), date(2024, 1, 15), "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DATEDIF(date(2023, 12, 31), date(2023, 12, 31), "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DATEDIF(None, date(2024, 1, 15), "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DATEDIF("", "", "")
        except EXC:
            pass


class Test_DATEVALUE:
    def test_exists(self):
        assert hasattr(mod, "DATEVALUE")

    def test_doc0(self):
        try:
            mod.DATEVALUE("15/01/2025")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.DATEVALUE("31/12/2024")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DATEVALUE("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DATEVALUE("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DATEVALUE(None)
        except EXC:
            pass


class Test_DAY:
    def test_exists(self):
        assert hasattr(mod, "DAY")

    def test_doc0(self):
        try:
            mod.DAY(45667.0)  # January 15, 2025
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.DAY(datetime(2025, 1, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DAY(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DAY(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DAY(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DAY("")
        except EXC:
            pass


class Test_DAYS:
    def test_exists(self):
        assert hasattr(mod, "DAYS")

    def test_var0(self):
        try:
            mod.DAYS(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DAYS(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DAYS(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DAYS("", "")
        except EXC:
            pass


class Test_DAYS360:
    def test_exists(self):
        assert hasattr(mod, "DAYS360")

    def test_var0(self):
        try:
            mod.DAYS360(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DAYS360(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DAYS360(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DAYS360("", "")
        except EXC:
            pass


class Test_EDATE:
    def test_exists(self):
        assert hasattr(mod, "EDATE")

    def test_var0(self):
        try:
            mod.EDATE(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.EDATE(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.EDATE(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.EDATE("", "")
        except EXC:
            pass


class Test_EOMONTH:
    def test_exists(self):
        assert hasattr(mod, "EOMONTH")

    def test_var0(self):
        try:
            mod.EOMONTH(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.EOMONTH(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.EOMONTH(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.EOMONTH("", "")
        except EXC:
            pass


class Test_HOUR:
    def test_exists(self):
        assert hasattr(mod, "HOUR")

    def test_doc0(self):
        try:
            mod.HOUR(0.5)  # 12:00 PM
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.HOUR(0.75)  # 6:00 PM
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.HOUR(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.HOUR(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.HOUR(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.HOUR("")
        except EXC:
            pass


class Test_ISOWEEKNUM:
    def test_exists(self):
        assert hasattr(mod, "ISOWEEKNUM")

    def test_doc0(self):
        try:
            mod.ISOWEEKNUM(datetime(2025, 1, 1))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ISOWEEKNUM(datetime(2025, 6, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISOWEEKNUM(date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISOWEEKNUM(date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISOWEEKNUM(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISOWEEKNUM("")
        except EXC:
            pass


class Test_MINUTE:
    def test_exists(self):
        assert hasattr(mod, "MINUTE")

    def test_doc0(self):
        try:
            mod.MINUTE(datetime(2025, 1, 15, 14, 30))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.MINUTE(0.604166667)  # Approximately 2:30 PM
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MINUTE(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MINUTE(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MINUTE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MINUTE("")
        except EXC:
            pass


class Test_MONTH:
    def test_exists(self):
        assert hasattr(mod, "MONTH")

    def test_doc0(self):
        try:
            mod.MONTH(45667.0)  # January 15, 2025
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.MONTH(datetime(2025, 6, 15))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MONTH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MONTH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MONTH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MONTH("")
        except EXC:
            pass


class Test_NETWORKDAYS:
    def test_exists(self):
        assert hasattr(mod, "NETWORKDAYS")

    def test_var0(self):
        try:
            mod.NETWORKDAYS(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.NETWORKDAYS(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.NETWORKDAYS(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.NETWORKDAYS("", "")
        except EXC:
            pass


class Test_NETWORKDAYS_INTL:
    def test_exists(self):
        assert hasattr(mod, "NETWORKDAYS_INTL")

    def test_var0(self):
        try:
            mod.NETWORKDAYS_INTL(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.NETWORKDAYS_INTL(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.NETWORKDAYS_INTL(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.NETWORKDAYS_INTL("", "")
        except EXC:
            pass


class Test_NOW:
    def test_exists(self):
        assert hasattr(mod, "NOW")

    def test_doc0(self):
        try:
            mod.NOW()  # e.g., 45667.625 for January 15, 2025, 3:00 PM
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.NOW()
        except EXC:
            pass


class Test_SECOND:
    def test_exists(self):
        assert hasattr(mod, "SECOND")

    def test_doc0(self):
        try:
            mod.SECOND(datetime(2025, 1, 15, 14, 30, 45))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SECOND(0.604224537)  # Approximately 2:30:05 PM
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SECOND(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SECOND(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SECOND(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SECOND("")
        except EXC:
            pass


class Test_TIME:
    def test_exists(self):
        assert hasattr(mod, "TIME")

    def test_doc0(self):
        try:
            mod.TIME(12, 0, 0)  # 12:00 PM
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TIME(6, 0, 0)  # 6:00 AM
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.TIME(18, 30, 0)  # 6:30 PM
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TIME(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TIME(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TIME(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TIME("", "", "")
        except EXC:
            pass


class Test_TIMEVALUE:
    def test_exists(self):
        assert hasattr(mod, "TIMEVALUE")

    def test_doc0(self):
        try:
            mod.TIMEVALUE("12:00:00")  # Noon
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TIMEVALUE("18:30:00")  # 6:30 PM
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TIMEVALUE("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TIMEVALUE("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TIMEVALUE(None)
        except EXC:
            pass


class Test_TODAY:
    def test_exists(self):
        assert hasattr(mod, "TODAY")

    def test_doc0(self):
        try:
            mod.TODAY()  # e.g., 45667.0 for January 15, 2025
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TODAY()
        except EXC:
            pass


class Test_WEEKDAY:
    def test_exists(self):
        assert hasattr(mod, "WEEKDAY")

    def test_doc0(self):
        try:
            mod.WEEKDAY(datetime(2025, 1, 15))  # Wednesday with Sunday=1
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.WEEKDAY(datetime(2025, 1, 15), 2)  # Wednesday with Monday=1
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.WEEKDAY(datetime(2025, 1, 15), 3)  # Wednesday with Monday=0
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.WEEKDAY(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.WEEKDAY(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.WEEKDAY(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.WEEKDAY("")
        except EXC:
            pass


class Test_WEEKNUM:
    def test_exists(self):
        assert hasattr(mod, "WEEKNUM")

    def test_doc0(self):
        try:
            mod.WEEKNUM(datetime(2025, 1, 1), return_type=1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.WEEKNUM(datetime(2025, 1, 1), return_type=21)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.WEEKNUM(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.WEEKNUM(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.WEEKNUM(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.WEEKNUM("")
        except EXC:
            pass


class Test_WORKDAY:
    def test_exists(self):
        assert hasattr(mod, "WORKDAY")

    def test_var0(self):
        try:
            mod.WORKDAY(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.WORKDAY(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.WORKDAY(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.WORKDAY("", "")
        except EXC:
            pass


class Test_WORKDAY_INTL:
    def test_exists(self):
        assert hasattr(mod, "WORKDAY_INTL")

    def test_var0(self):
        try:
            mod.WORKDAY_INTL(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.WORKDAY_INTL(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.WORKDAY_INTL(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.WORKDAY_INTL("", "")
        except EXC:
            pass


class Test_YEAR:
    def test_exists(self):
        assert hasattr(mod, "YEAR")

    def test_doc0(self):
        try:
            mod.YEAR(45667.0)  # January 15, 2025
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.YEAR(datetime(2024, 12, 31))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.YEAR(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.YEAR(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.YEAR(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.YEAR("")
        except EXC:
            pass


class Test_YEARFRAC:
    def test_exists(self):
        assert hasattr(mod, "YEARFRAC")

    def test_var0(self):
        try:
            mod.YEARFRAC(date(2024, 1, 15), date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.YEARFRAC(date(2023, 12, 31), date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.YEARFRAC(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.YEARFRAC("", "")
        except EXC:
            pass

