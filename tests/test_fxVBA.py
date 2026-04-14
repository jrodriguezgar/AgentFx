"""Tests for formulite.fxVBA - VBA/Access-compatible functions."""
import math
import os
from datetime import datetime
import pytest

# -- Array Functions --
from formulite.fxVBA.array_functions import Split, Join_, Filter_, LBound, UBound, Array_

class TestSplit:
    def test_default(self):
        assert Split("a b c") == ["a", "b", "c"]
    def test_comma(self):
        assert Split("a,b,c", ",") == ["a", "b", "c"]
    def test_limit(self):
        assert Split("a,b,c,d", ",", 2) == ["a", "b,c,d"]

class TestJoin:
    def test_default(self):
        assert Join_(["a", "b", "c"]) == "a b c"
    def test_custom(self):
        assert Join_(["a", "b"], ",") == "a,b"

class TestFilter:
    def test_include(self):
        assert Filter_(["apple", "banana", "grape"], "an") == ["banana"]
    def test_exclude(self):
        r = Filter_(["apple", "banana", "grape"], "an", include=False)
        assert "banana" not in r

class TestBounds:
    def test_lbound(self):
        assert LBound([1, 2, 3]) == 0
    def test_ubound(self):
        assert UBound([1, 2, 3]) == 2
    def test_array(self):
        assert Array_(1, 2, 3) == [1, 2, 3]

# -- Conversion Functions --
from formulite.fxVBA.conversion_functions import (
    CBool, CByte, CCur, CDbl, CInt, CLng, CSng, CStr, CVar, Val,
)

class TestConversions:
    def test_cbool_true(self):
        assert CBool(1) is True
    def test_cbool_false(self):
        assert CBool(0) is False
    def test_cbyte(self):
        assert CByte(42) == 42
    def test_ccur(self):
        assert isinstance(CCur(1234.5678), float)
    def test_cdbl(self):
        assert CDbl("3.14") == pytest.approx(3.14)
    def test_cint(self):
        assert CInt(3.7) == 4
    def test_clng(self):
        assert CLng(3.7) == 3
    def test_csng(self):
        assert isinstance(CSng(3.14), float)
    def test_cstr(self):
        assert CStr(42) == "42"
    def test_cvar(self):
        assert CVar(42) == 42
    def test_val_num(self):
        assert Val("123.45") == pytest.approx(123.45)
    def test_val_text(self):
        assert Val("123abc") == pytest.approx(123.0)

# -- Date Functions --
from formulite.fxVBA.date_functions import (
    DateAdd, DateDiff, DateSerial, Day, Hour, Minute,
    Month, MonthName, Second, TimeSerial, WeekDay, Year,
)

class TestDateFunctions:
    def test_dateadd(self):
        r = DateAdd("d", 10, datetime(2026, 1, 1))
        assert r.day == 11
    def test_datediff(self):
        assert DateDiff("d", datetime(2026, 1, 1), datetime(2026, 1, 11)) == 10
    def test_dateserial(self):
        r = DateSerial(2026, 4, 13)
        assert r.year == 2026 and r.month == 4 and r.day == 13
    def test_day(self):
        assert Day(datetime(2026, 4, 13)) == 13
    def test_hour(self):
        assert Hour(datetime(2026, 1, 1, 14)) == 14
    def test_minute(self):
        assert Minute(datetime(2026, 1, 1, 14, 30)) == 30
    def test_month(self):
        assert Month(datetime(2026, 4, 13)) == 4
    def test_monthname(self):
        assert isinstance(MonthName(1), str) and len(MonthName(1)) > 0
    def test_second(self):
        assert Second(datetime(2026, 1, 1, 0, 0, 45)) == 45
    def test_timeserial(self):
        r = TimeSerial(14, 30, 45)
        assert r.hour == 14 and r.minute == 30
    def test_weekday(self):
        assert isinstance(WeekDay(datetime(2026, 4, 13)), int)
    def test_year(self):
        assert Year(datetime(2026, 4, 13)) == 2026

# -- Financial Functions --
from formulite.fxVBA.financial_functions import DDB, FV, IPmt, Pmt, PPmt, PV, SLN, SYD, NPer

class TestFinancial:
    def test_pmt(self):
        assert Pmt(0.08/12, 10, 10000) < 0
    def test_fv(self):
        assert isinstance(FV(0.06/12, 10, -200), float)
    def test_pv(self):
        assert isinstance(PV(0.08/12, 240, 500), float)
    def test_ipmt(self):
        assert isinstance(IPmt(0.1/12, 1, 36, 8000), float)
    def test_ppmt(self):
        assert isinstance(PPmt(0.1/12, 1, 36, 8000), float)
    def test_ddb(self):
        assert isinstance(DDB(2400, 300, 10, 1), float)
    def test_sln(self):
        assert SLN(30000, 7500, 10) == pytest.approx(2250.0)
    def test_syd(self):
        assert SYD(30000, 7500, 10, 1) > 0
    def test_nper(self):
        assert NPer(0.08/12, -200, 10000) > 0

# -- Format Functions --
from formulite.fxVBA.format_functions import FormatCurrency, FormatNumber, FormatPercent

class TestFormat:
    def test_currency(self):
        assert isinstance(FormatCurrency(1234.56), str)
    def test_number(self):
        r = FormatNumber(1234.5678, 2)
        assert isinstance(r, str)
    def test_percent(self):
        assert "%" in FormatPercent(0.25)

# -- Logic Functions --
from formulite.fxVBA.logic_functions import (
    Choose, IIf, IsDate, IsError, IsNull, IsNumeric, Switch,
    IsArray, IsEmpty, IsObject, IsMissing,
)

class TestLogic:
    def test_choose(self):
        assert Choose(2, "a", "b", "c") == "b"
    def test_choose_oor(self):
        assert Choose(10, "a", "b") is None
    def test_iif_true(self):
        assert IIf(True, "y", "n") == "y"
    def test_iif_false(self):
        assert IIf(False, "y", "n") == "n"
    def test_isdate_true(self):
        assert IsDate(datetime(2026, 1, 1)) is True
    def test_isdate_false(self):
        assert IsDate(42) is False
    def test_iserror(self):
        assert IsError(ValueError()) is True
    def test_iserror_false(self):
        assert IsError(42) is False
    def test_isnull(self):
        assert IsNull(None) is True and IsNull(42) is False
    def test_isnumeric(self):
        assert IsNumeric(42) is True and IsNumeric("abc") is False
    def test_switch(self):
        assert Switch(False, "a", True, "b") == "b"
    def test_isarray(self):
        assert IsArray([1]) is True and IsArray(42) is False
    def test_isempty(self):
        assert IsEmpty(None) is True and IsEmpty(42) is False
    def test_isobject(self):
        assert IsObject(42) is False
    def test_ismissing(self):
        assert IsMissing(None) is True

# -- Math Functions --
from formulite.fxVBA.math_functions import (
    Abs_, Atn, Cos, Exp, Fix, Int_, Log, Round_, Sgn, Sin, Sqr, Tan,
)

class TestMath:
    def test_abs(self):
        assert Abs_(-42) == 42
    def test_atn(self):
        assert Atn(1) == pytest.approx(math.atan(1))
    def test_cos(self):
        assert Cos(0) == pytest.approx(1.0)
    def test_exp(self):
        assert Exp(1) == pytest.approx(math.e)
    def test_fix_pos(self):
        assert Fix(3.7) == 3
    def test_fix_neg(self):
        assert Fix(-3.7) == -3
    def test_int_pos(self):
        assert Int_(3.7) == 3
    def test_int_neg(self):
        assert Int_(-3.7) == -4
    def test_log(self):
        assert Log(math.e) == pytest.approx(1.0)
    def test_round(self):
        assert Round_(3.456, 2) == pytest.approx(3.46)
    def test_sgn(self):
        assert Sgn(42) == 1 and Sgn(-42) == -1 and Sgn(0) == 0
    def test_sin(self):
        assert Sin(0) == pytest.approx(0.0)
    def test_sqr(self):
        assert Sqr(4) == pytest.approx(2.0)
    def test_tan(self):
        assert Tan(0) == pytest.approx(0.0)

# -- String Functions --
from formulite.fxVBA.string_functions import (
    Asc, Chr_, InStr, InStrRev, LCase, Left, Len_, LTrim,
    Mid, Replace, Right, RTrim, Space, StrComp, StrReverse, Trim, UCase,
)

class TestString:
    def test_asc(self):
        assert Asc("A") == 65
    def test_chr(self):
        assert Chr_(65) == "A"
    def test_instr(self):
        r = InStr("Hello World", "World")
        assert isinstance(r, int)
    def test_instr_not_found(self):
        assert InStr("Hello", "xyz") == 0
    def test_instrrev(self):
        assert InStrRev("abcabc", "bc") > 0
    def test_lcase(self):
        assert LCase("HELLO") == "hello"
    def test_left(self):
        assert Left("Hello", 3) == "Hel"
    def test_len(self):
        assert Len_("Hello") == 5
    def test_ltrim(self):
        assert LTrim("  Hello") == "Hello"
    def test_mid(self):
        assert Mid("Hello World", 7) == "World"
    def test_mid_length(self):
        assert Mid("Hello World", 1, 5) == "Hello"
    def test_replace(self):
        assert Replace("Hello World", "World", "Python") == "Hello Python"
    def test_right(self):
        assert Right("Hello", 3) == "llo"
    def test_rtrim(self):
        assert RTrim("Hello  ") == "Hello"
    def test_space(self):
        assert Space(5) == "     "
    def test_strcomp(self):
        assert StrComp("abc", "abc") == 0
    def test_strreverse(self):
        assert StrReverse("Hello") == "olleH"
    def test_trim(self):
        assert Trim("  Hello  ") == "Hello"
    def test_ucase(self):
        assert UCase("hello") == "HELLO"

# -- Misc Functions --
from formulite.fxVBA.misc_functions import Hex_, Oct_, RGB, CurrentUser

class TestMisc:
    def test_hex(self):
        assert Hex_(255) == "FF"
    def test_oct(self):
        assert Oct_(8) == "10"
    def test_rgb(self):
        assert isinstance(RGB(255, 0, 0), int)
    def test_currentuser(self):
        import pytest
        with pytest.raises(NotImplementedError):
            CurrentUser()

# -- System Functions --
from formulite.fxVBA.system_functions import CurDir, Environ, Nz, TypeName, VarType, Partition

class TestSystem:
    def test_curdir(self):
        assert os.path.isdir(CurDir())
    def test_environ(self):
        assert isinstance(Environ("PATH"), str)
    def test_nz_null(self):
        assert Nz(None, "default") == "default"
    def test_nz_value(self):
        assert Nz(42, "default") == 42
    def test_typename(self):
        assert TypeName(42) == "int"
    def test_vartype(self):
        assert isinstance(VarType(42), int)
    def test_partition(self):
        assert isinstance(Partition(20, 0, 100, 10), str)
