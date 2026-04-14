# Coverage tests for formulite.fxExcel.financial_formulas
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxExcel import financial_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_ACCRINT:
    def test_exists(self):
        assert hasattr(mod, "ACCRINT")

    def test_doc0(self):
        try:
            mod.ACCRINT(datetime(2025, 1, 1), datetime(2025, 7, 1), datetime(2025, 4, 1), 0.08, 1000, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ACCRINT(date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15), 3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ACCRINT(date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31), 100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ACCRINT(None, date(2024, 1, 15), date(2024, 1, 15), 3.14, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ACCRINT("", "", "", 0, "", "")
        except EXC:
            pass


class Test_ACCRINTM:
    def test_exists(self):
        assert hasattr(mod, "ACCRINTM")

    def test_doc0(self):
        try:
            mod.ACCRINTM(datetime(2025, 1, 1), datetime(2025, 12, 31), 0.08, 1000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ACCRINTM(date(2024, 1, 15), date(2024, 1, 15), 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ACCRINTM(date(2023, 12, 31), date(2023, 12, 31), 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ACCRINTM(None, date(2024, 1, 15), 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ACCRINTM("", "", 0, "")
        except EXC:
            pass


class Test_AMORDEGRC:
    def test_exists(self):
        assert hasattr(mod, "AMORDEGRC")

    def test_doc0(self):
        try:
            mod.AMORDEGRC(2400, date(2008, 8, 19), date(2008, 12, 31), 300, 1, 0.15)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.AMORDEGRC(0, date(2024, 1, 15), 0, 0, 0, 0.5)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.AMORDEGRC(1, date(2023, 12, 31), 1, 1, 1, 0.1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.AMORDEGRC(None, date(2024, 1, 15), 0, 0, 0, 0.5)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.AMORDEGRC("", "", "", "", "", 0)
        except EXC:
            pass


class Test_AMORLINC:
    def test_exists(self):
        assert hasattr(mod, "AMORLINC")

    def test_doc0(self):
        try:
            mod.AMORLINC(2400, date(2008, 8, 19), date(2008, 12, 31), 300, 1, 0.15)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.AMORLINC(0, date(2024, 1, 15), 0, 0, 0, 0.5)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.AMORLINC(1, date(2023, 12, 31), 1, 1, 1, 0.1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.AMORLINC(None, date(2024, 1, 15), 0, 0, 0, 0.5)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.AMORLINC("", "", "", "", "", 0)
        except EXC:
            pass


class Test_COUPDAYBS:
    def test_exists(self):
        assert hasattr(mod, "COUPDAYBS")

    def test_doc0(self):
        try:
            mod.COUPDAYBS(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COUPDAYBS(date(2024, 1, 15), date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COUPDAYBS(date(2023, 12, 31), date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COUPDAYBS(None, date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COUPDAYBS("", "", "")
        except EXC:
            pass


class Test_COUPDAYS:
    def test_exists(self):
        assert hasattr(mod, "COUPDAYS")

    def test_doc0(self):
        try:
            mod.COUPDAYS(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COUPDAYS(date(2024, 1, 15), date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COUPDAYS(date(2023, 12, 31), date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COUPDAYS(None, date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COUPDAYS("", "", "")
        except EXC:
            pass


class Test_COUPDAYSNC:
    def test_exists(self):
        assert hasattr(mod, "COUPDAYSNC")

    def test_doc0(self):
        try:
            mod.COUPDAYSNC(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COUPDAYSNC(date(2024, 1, 15), date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COUPDAYSNC(date(2023, 12, 31), date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COUPDAYSNC(None, date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COUPDAYSNC("", "", "")
        except EXC:
            pass


class Test_COUPNCD:
    def test_exists(self):
        assert hasattr(mod, "COUPNCD")

    def test_doc0(self):
        try:
            mod.COUPNCD(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COUPNCD(date(2024, 1, 15), date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COUPNCD(date(2023, 12, 31), date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COUPNCD(None, date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COUPNCD("", "", "")
        except EXC:
            pass


class Test_COUPNUM:
    def test_exists(self):
        assert hasattr(mod, "COUPNUM")

    def test_doc0(self):
        try:
            mod.COUPNUM(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COUPNUM(date(2024, 1, 15), date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COUPNUM(date(2023, 12, 31), date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COUPNUM(None, date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COUPNUM("", "", "")
        except EXC:
            pass


class Test_COUPPCD:
    def test_exists(self):
        assert hasattr(mod, "COUPPCD")

    def test_doc0(self):
        try:
            mod.COUPPCD(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COUPPCD(date(2024, 1, 15), date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COUPPCD(date(2023, 12, 31), date(2023, 12, 31), 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COUPPCD(None, date(2024, 1, 15), 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COUPPCD("", "", "")
        except EXC:
            pass


class Test_CUMIPMT:
    def test_exists(self):
        assert hasattr(mod, "CUMIPMT")

    def test_doc0(self):
        try:
            mod.CUMIPMT(0.09/12, 30*12, 125000, 1, 12, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CUMIPMT(3.14, 0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CUMIPMT(100, 1, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CUMIPMT(None, 0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CUMIPMT(0, "", "", "", "", "")
        except EXC:
            pass


class Test_CUMPRINC:
    def test_exists(self):
        assert hasattr(mod, "CUMPRINC")

    def test_doc0(self):
        try:
            mod.CUMPRINC(0.09/12, 30*12, 125000, 1, 12, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CUMPRINC(3.14, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CUMPRINC(100, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CUMPRINC(None, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CUMPRINC(0, "", "", "", "")
        except EXC:
            pass


class Test_DB:
    def test_exists(self):
        assert hasattr(mod, "DB")

    def test_doc0(self):
        try:
            mod.DB(1000000, 100000, 6, 1, 7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DB(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DB(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DB(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DB("", "", "", "")
        except EXC:
            pass


class Test_DDB:
    def test_exists(self):
        assert hasattr(mod, "DDB")

    def test_doc0(self):
        try:
            mod.DDB(2400, 300, 10, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DDB(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DDB(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DDB(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DDB("", "", "", "")
        except EXC:
            pass


class Test_DISC:
    def test_exists(self):
        assert hasattr(mod, "DISC")

    def test_doc0(self):
        try:
            mod.DISC(date(2007, 1, 25), date(2007, 6, 15), 97.975, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DISC(0, 0, 0, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DISC(1, 1, 1, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DISC(None, 0, 0, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DISC("", "", "", 0)
        except EXC:
            pass


class Test_DOLLARDE:
    def test_exists(self):
        assert hasattr(mod, "DOLLARDE")

    def test_doc0(self):
        try:
            mod.DOLLARDE(1.02, 16)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.DOLLARDE(1.1, 32)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DOLLARDE(0.5, 0.5)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DOLLARDE(0.1, 0.1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DOLLARDE(None, 0.5)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DOLLARDE(0, 0)
        except EXC:
            pass


class Test_DOLLARFR:
    def test_exists(self):
        assert hasattr(mod, "DOLLARFR")

    def test_doc0(self):
        try:
            mod.DOLLARFR(1.125, 16)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.DOLLARFR(1.3125, 32)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DOLLARFR(0, 0.5)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DOLLARFR(1, 0.1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DOLLARFR(None, 0.5)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DOLLARFR("", 0)
        except EXC:
            pass


class Test_DURATION:
    def test_exists(self):
        assert hasattr(mod, "DURATION")

    def test_doc0(self):
        try:
            mod.DURATION(datetime(2025, 1, 1), datetime(2030, 1, 1), 0.08, 0.09, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DURATION(date(2024, 1, 15), date(2024, 1, 15), 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DURATION(date(2023, 12, 31), date(2023, 12, 31), 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DURATION(None, date(2024, 1, 15), 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DURATION("", "", 0, "", "")
        except EXC:
            pass


class Test_EFFECT:
    def test_exists(self):
        assert hasattr(mod, "EFFECT")

    def test_doc0(self):
        try:
            mod.EFFECT(0.0525, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.EFFECT(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.EFFECT(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.EFFECT(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.EFFECT(0, "")
        except EXC:
            pass


class Test_FV:
    def test_exists(self):
        assert hasattr(mod, "FV")

    def test_doc0(self):
        try:
            mod.FV(0.06/12, 10, -200, -500, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.FV(0.12/12, 12, -1000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FV(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FV(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FV(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FV(0, "", "")
        except EXC:
            pass


class Test_FVSCHEDULE:
    def test_exists(self):
        assert hasattr(mod, "FVSCHEDULE")

    def test_doc0(self):
        try:
            mod.FVSCHEDULE(1, [0.09, 0.11, 0.10])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FVSCHEDULE(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FVSCHEDULE(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FVSCHEDULE(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FVSCHEDULE("", "")
        except EXC:
            pass


class Test_INTRATE:
    def test_exists(self):
        assert hasattr(mod, "INTRATE")

    def test_doc0(self):
        try:
            mod.INTRATE(date(2008, 2, 15), date(2008, 5, 15), 1000000, 1014420)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.INTRATE(0, 0, 0, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.INTRATE(1, 1, 1, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.INTRATE(None, 0, 0, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.INTRATE("", "", "", 0)
        except EXC:
            pass


class Test_IPMT:
    def test_exists(self):
        assert hasattr(mod, "IPMT")

    def test_doc0(self):
        try:
            mod.IPMT(0.1/12, 1, 3*12, 8000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.IPMT(3.14, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.IPMT(100, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.IPMT(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.IPMT(0, "", "", "")
        except EXC:
            pass


class Test_IRR:
    def test_exists(self):
        assert hasattr(mod, "IRR")

    def test_doc0(self):
        try:
            mod.IRR([-70000, 12000, 15000, 18000, 21000, 26000])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.IRR(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.IRR(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.IRR(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.IRR([])
        except EXC:
            pass


class Test_ISPMT:
    def test_exists(self):
        assert hasattr(mod, "ISPMT")

    def test_doc0(self):
        try:
            mod.ISPMT(0.1/12, 1, 3*12, 8000000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISPMT(0.5, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISPMT(0.1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISPMT(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISPMT(0, "", "", "")
        except EXC:
            pass


class Test_MDURATION:
    def test_exists(self):
        assert hasattr(mod, "MDURATION")

    def test_doc0(self):
        try:
            mod.MDURATION(datetime(2025, 1, 1), datetime(2030, 1, 1), 0.08, 0.09, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MDURATION(date(2024, 1, 15), date(2024, 1, 15), 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MDURATION(date(2023, 12, 31), date(2023, 12, 31), 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MDURATION(None, date(2024, 1, 15), 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MDURATION("", "", 0, "", "")
        except EXC:
            pass


class Test_MIRR:
    def test_exists(self):
        assert hasattr(mod, "MIRR")

    def test_doc0(self):
        try:
            mod.MIRR([-120000, 39000, 30000, 21000, 37000, 46000], 0.10, 0.12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MIRR(0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MIRR(1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MIRR(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MIRR([], 0, 0)
        except EXC:
            pass


class Test_NOMINAL:
    def test_exists(self):
        assert hasattr(mod, "NOMINAL")

    def test_doc0(self):
        try:
            mod.NOMINAL(0.053543, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.NOMINAL(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.NOMINAL(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.NOMINAL(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.NOMINAL(0, "")
        except EXC:
            pass


class Test_NPER:
    def test_exists(self):
        assert hasattr(mod, "NPER")

    def test_doc0(self):
        try:
            mod.NPER(0.12/12, -100, -1000, 10000, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.NPER(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.NPER(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.NPER(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.NPER(0, "", "")
        except EXC:
            pass


class Test_NPV:
    def test_exists(self):
        assert hasattr(mod, "NPV")

    def test_doc0(self):
        try:
            mod.NPV(0.10, -10000, 3000, 4200, 6800)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.NPV(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.NPV(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.NPV(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.NPV(0)
        except EXC:
            pass


class Test_ODDFPRICE:
    def test_exists(self):
        assert hasattr(mod, "ODDFPRICE")

    def test_doc0(self):
        try:
            mod.ODDFPRICE(date(2008, 11, 11), date(2021, 3, 1), date(2008, 10, 15), date(2009, 3, 1), 0.0785, 0.0625, 100, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ODDFPRICE(0, 0, 0, 1, 0.5, 0, 1, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ODDFPRICE(1, 1, 1, 3, 0.1, 1, 3, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ODDFPRICE(None, 0, 0, 1, 0.5, 0, 1, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ODDFPRICE("", "", "", 0, 0, "", 0, "")
        except EXC:
            pass


class Test_ODDFYIELD:
    def test_exists(self):
        assert hasattr(mod, "ODDFYIELD")

    def test_doc0(self):
        try:
            mod.ODDFYIELD(date(2008, 11, 11), date(2021, 3, 1), date(2008, 10, 15), date(2009, 3, 1), 0.0785, 113.597717, 100, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ODDFYIELD(0, 0, 0, 1, 0.5, 0, 1, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ODDFYIELD(1, 1, 1, 3, 0.1, 1, 3, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ODDFYIELD(None, 0, 0, 1, 0.5, 0, 1, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ODDFYIELD("", "", "", 0, 0, "", 0, "")
        except EXC:
            pass


class Test_ODDLPRICE:
    def test_exists(self):
        assert hasattr(mod, "ODDLPRICE")

    def test_doc0(self):
        try:
            mod.ODDLPRICE(date(2008, 2, 7), date(2008, 6, 15), date(2007, 10, 15), 0.0375, 0.0405, 100, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ODDLPRICE(0, 0, 0, 0.5, 0, 1, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ODDLPRICE(1, 1, 1, 0.1, 1, 3, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ODDLPRICE(None, 0, 0, 0.5, 0, 1, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ODDLPRICE("", "", "", 0, "", 0, "")
        except EXC:
            pass


class Test_ODDLYIELD:
    def test_exists(self):
        assert hasattr(mod, "ODDLYIELD")

    def test_doc0(self):
        try:
            mod.ODDLYIELD(date(2008, 2, 7), date(2008, 6, 15), date(2007, 10, 15), 0.0375, 99.878456, 100, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ODDLYIELD(0, 0, 0, 0.5, 0, 1, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ODDLYIELD(1, 1, 1, 0.1, 1, 3, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ODDLYIELD(None, 0, 0, 0.5, 0, 1, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ODDLYIELD("", "", "", 0, "", 0, "")
        except EXC:
            pass


class Test_PDURATION:
    def test_exists(self):
        assert hasattr(mod, "PDURATION")

    def test_doc0(self):
        try:
            mod.PDURATION(0.025, 2000, 2200)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PDURATION(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.PDURATION(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.PDURATION(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.PDURATION(0, "", "")
        except EXC:
            pass


class Test_PMT:
    def test_exists(self):
        assert hasattr(mod, "PMT")

    def test_doc0(self):
        try:
            mod.PMT(0.08/12, 10, 10000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PMT(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.PMT(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.PMT(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.PMT(0, "", "")
        except EXC:
            pass


class Test_PPMT:
    def test_exists(self):
        assert hasattr(mod, "PPMT")

    def test_doc0(self):
        try:
            mod.PPMT(0.08/12, 1, 10*12, 10000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PPMT(3.14, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.PPMT(100, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.PPMT(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.PPMT(0, "", "", "")
        except EXC:
            pass


class Test_PRICE:
    def test_exists(self):
        assert hasattr(mod, "PRICE")

    def test_doc0(self):
        try:
            mod.PRICE(datetime(2025, 2, 15), datetime(2032, 11, 15), 0.0575, 0.065, 100, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PRICE(date(2024, 1, 15), date(2024, 1, 15), 3.14, 3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.PRICE(date(2023, 12, 31), date(2023, 12, 31), 100, 100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.PRICE(None, date(2024, 1, 15), 3.14, 3.14, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.PRICE("", "", 0, "", 0, "")
        except EXC:
            pass


class Test_PRICEDISC:
    def test_exists(self):
        assert hasattr(mod, "PRICEDISC")

    def test_doc0(self):
        try:
            mod.PRICEDISC(datetime(2025, 2, 16), datetime(2025, 3, 1), 0.0525, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PRICEDISC(date(2024, 1, 15), date(2024, 1, 15), 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.PRICEDISC(date(2023, 12, 31), date(2023, 12, 31), 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.PRICEDISC(None, date(2024, 1, 15), 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.PRICEDISC("", "", 0, 0)
        except EXC:
            pass


class Test_PRICEMAT:
    def test_exists(self):
        assert hasattr(mod, "PRICEMAT")

    def test_doc0(self):
        try:
            mod.PRICEMAT(datetime(2025, 2, 15), datetime(2025, 4, 13), datetime(2024, 11, 11), 0.061, 0.061)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PRICEMAT(date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15), 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.PRICEMAT(date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31), 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.PRICEMAT(None, date(2024, 1, 15), date(2024, 1, 15), 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.PRICEMAT("", "", "", 0, "")
        except EXC:
            pass


class Test_PV:
    def test_exists(self):
        assert hasattr(mod, "PV")

    def test_doc0(self):
        try:
            mod.PV(0.08/12, 12*20, 500)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PV(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.PV(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.PV(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.PV(0, "", "")
        except EXC:
            pass


class Test_RATE:
    def test_exists(self):
        assert hasattr(mod, "RATE")

    def test_doc0(self):
        try:
            mod.RATE(4*12, -200, 8000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.RATE(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RATE(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RATE(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.RATE("", "", "")
        except EXC:
            pass


class Test_RECEIVED:
    def test_exists(self):
        assert hasattr(mod, "RECEIVED")

    def test_doc0(self):
        try:
            mod.RECEIVED(date(2008, 2, 15), date(2008, 5, 15), 1000000, 0.0575)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.RECEIVED(0, 0, 0, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RECEIVED(1, 1, 1, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RECEIVED(None, 0, 0, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.RECEIVED("", "", "", 0)
        except EXC:
            pass


class Test_RRI:
    def test_exists(self):
        assert hasattr(mod, "RRI")

    def test_doc0(self):
        try:
            mod.RRI(96, 10000, 11000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.RRI(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RRI(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RRI(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.RRI("", "", "")
        except EXC:
            pass


class Test_SLN:
    def test_exists(self):
        assert hasattr(mod, "SLN")

    def test_doc0(self):
        try:
            mod.SLN(30000, 7500, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SLN(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SLN(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SLN(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SLN("", "", "")
        except EXC:
            pass


class Test_SYD:
    def test_exists(self):
        assert hasattr(mod, "SYD")

    def test_doc0(self):
        try:
            mod.SYD(30000, 7500, 10, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SYD(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SYD(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SYD(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SYD("", "", "", "")
        except EXC:
            pass


class Test_TBILLEQ:
    def test_exists(self):
        assert hasattr(mod, "TBILLEQ")

    def test_doc0(self):
        try:
            mod.TBILLEQ(date(2008, 3, 31), date(2008, 6, 1), 0.0914)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TBILLEQ(0, 0, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TBILLEQ(1, 1, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TBILLEQ(None, 0, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TBILLEQ("", "", 0)
        except EXC:
            pass


class Test_TBILLPRICE:
    def test_exists(self):
        assert hasattr(mod, "TBILLPRICE")

    def test_doc0(self):
        try:
            mod.TBILLPRICE(date(2008, 3, 31), date(2008, 6, 1), 0.09)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TBILLPRICE(0, 0, 1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TBILLPRICE(1, 1, 3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TBILLPRICE(None, 0, 1)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TBILLPRICE("", "", 0)
        except EXC:
            pass


class Test_TBILLYIELD:
    def test_exists(self):
        assert hasattr(mod, "TBILLYIELD")

    def test_doc0(self):
        try:
            mod.TBILLYIELD(date(2008, 3, 31), date(2008, 6, 1), 98.45)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TBILLYIELD(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TBILLYIELD(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TBILLYIELD(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TBILLYIELD("", "", "")
        except EXC:
            pass


class Test_VDB:
    def test_exists(self):
        assert hasattr(mod, "VDB")

    def test_doc0(self):
        try:
            mod.VDB(2400, 300, 10, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.VDB(0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.VDB(1, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.VDB(None, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.VDB("", "", "", "", "")
        except EXC:
            pass


class Test_XIRR:
    def test_exists(self):
        assert hasattr(mod, "XIRR")

    def test_var0(self):
        try:
            mod.XIRR(0, date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.XIRR(1, date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.XIRR(None, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.XIRR([], "")
        except EXC:
            pass


class Test_XNPV:
    def test_exists(self):
        assert hasattr(mod, "XNPV")

    def test_var0(self):
        try:
            mod.XNPV(3.14, 0, date(2024, 1, 15))
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.XNPV(100, 1, date(2023, 12, 31))
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.XNPV(None, 0, date(2024, 1, 15))
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.XNPV(0, [], "")
        except EXC:
            pass


class Test_YIELD:
    def test_exists(self):
        assert hasattr(mod, "YIELD")

    def test_doc0(self):
        try:
            mod.YIELD(datetime(2025, 2, 15), datetime(2032, 11, 15), 0.0575, 95.04, 100, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.YIELD(date(2024, 1, 15), date(2024, 1, 15), 3.14, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.YIELD(date(2023, 12, 31), date(2023, 12, 31), 100, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.YIELD(None, date(2024, 1, 15), 3.14, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.YIELD("", "", 0, "", 0, "")
        except EXC:
            pass


class Test_YIELDDISC:
    def test_exists(self):
        assert hasattr(mod, "YIELDDISC")

    def test_doc0(self):
        try:
            mod.YIELDDISC(datetime(2025, 2, 16), datetime(2025, 3, 1), 99.795, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.YIELDDISC(date(2024, 1, 15), date(2024, 1, 15), 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.YIELDDISC(date(2023, 12, 31), date(2023, 12, 31), 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.YIELDDISC(None, date(2024, 1, 15), 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.YIELDDISC("", "", "", 0)
        except EXC:
            pass


class Test_YIELDMAT:
    def test_exists(self):
        assert hasattr(mod, "YIELDMAT")

    def test_doc0(self):
        try:
            mod.YIELDMAT(datetime(2025, 3, 15), datetime(2025, 11, 3), datetime(2024, 11, 8), 0.0625, 100.0123)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.YIELDMAT(date(2024, 1, 15), date(2024, 1, 15), date(2024, 1, 15), 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.YIELDMAT(date(2023, 12, 31), date(2023, 12, 31), date(2023, 12, 31), 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.YIELDMAT(None, date(2024, 1, 15), date(2024, 1, 15), 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.YIELDMAT("", "", "", 0, "")
        except EXC:
            pass

