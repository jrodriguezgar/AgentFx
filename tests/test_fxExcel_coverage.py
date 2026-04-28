"""Coverage tests for fxExcel modules."""
import pytest

from agentfx.fxExcel.lookup_formulas import (
    VLOOKUP, HLOOKUP, INDEX, MATCH, CHOOSE,
)

class TestLookupFormulas:
    def test_vlookup(self):
        table = [[1, "a"], [2, "b"], [3, "c"]]
        assert VLOOKUP(2, table, 2) == "b"
    def test_hlookup(self):
        table = [[1, 2, 3], ["a", "b", "c"]]
        assert HLOOKUP(2, table, 2) == "b"
    def test_index(self):
        assert INDEX([[1,2],[3,4]], 1, 2) == 2
    def test_match(self):
        assert MATCH(3, [1, 2, 3, 4]) == 3
    def test_choose(self):
        assert CHOOSE(2, "a", "b", "c") == "b"

from agentfx.fxExcel.text_formulas import (
    CONCATENATE, LEFT, RIGHT, MID, LEN, LOWER, UPPER,
    PROPER, TRIM, SUBSTITUTE, REPT, FIND, SEARCH,
    VALUE, EXACT, REPLACE as EXCEL_REPLACE, CLEAN,
    CHAR, CODE,
)

class TestTextFormulas:
    def test_concatenate(self):
        assert CONCATENATE("a", "b", "c") == "abc"
    def test_left(self):
        assert LEFT("hello", 3) == "hel"
    def test_right(self):
        assert RIGHT("hello", 3) == "llo"
    def test_mid(self):
        assert MID("hello", 2, 3) == "ell"
    def test_len(self):
        assert LEN("hello") == 5
    def test_lower(self):
        assert LOWER("HELLO") == "hello"
    def test_upper(self):
        assert UPPER("hello") == "HELLO"
    def test_proper(self):
        assert PROPER("hello world") == "Hello World"
    def test_trim(self):
        assert TRIM("  hello  ") == "hello"
    def test_substitute(self):
        assert SUBSTITUTE("hello", "l", "r") == "herro"
    def test_rept(self):
        assert REPT("ab", 3) == "ababab"
    def test_find(self):
        assert FIND("l", "hello") == 3
    def test_search(self):
        assert SEARCH("L", "hello") == 3
    def test_value(self):
        assert VALUE("42") == 42
    def test_exact(self):
        assert EXACT("hello", "hello") is True
    def test_replace(self):
        assert EXCEL_REPLACE("hello", 2, 3, "XY") == "hXYo"
    def test_clean(self):
        r = CLEAN("hello\x00world")
        assert isinstance(r, str)
    def test_char(self):
        assert CHAR(65) == "A"
    def test_code(self):
        assert CODE("A") == 65

from agentfx.fxExcel.math_formulas import (
    SUM, ABS as EXCEL_ABS,
    ROUND as EXCEL_ROUND, ROUNDUP, ROUNDDOWN, INT as EXCEL_INT,
    MOD, POWER, SQRT, LOG as EXCEL_LOG, LN, EXP as EXCEL_EXP,
    FACT, SUMPRODUCT, SUMIF,
    CEILING, FLOOR as EXCEL_FLOOR, RAND, RANDBETWEEN,
    SIGN, TRUNC, GCD, LCM, COMBIN,
    PI, DEGREES, RADIANS,
)

class TestMathFormulas:
    def test_sum(self):
        assert SUM(1, 2, 3) == 6
    def test_abs(self):
        assert EXCEL_ABS(-5) == 5
    def test_round(self):
        assert EXCEL_ROUND(3.456, 2) == pytest.approx(3.46)
    def test_roundup(self):
        assert ROUNDUP(3.421, 1) == pytest.approx(3.5)
    def test_rounddown(self):
        assert ROUNDDOWN(3.489, 1) == pytest.approx(3.4)
    def test_int(self):
        assert EXCEL_INT(3.7) == 3
    def test_mod(self):
        assert MOD(10, 3) == 1
    def test_power(self):
        assert POWER(2, 3) == 8
    def test_sqrt(self):
        assert SQRT(9) == pytest.approx(3.0)
    def test_log(self):
        assert EXCEL_LOG(100, 10) == pytest.approx(2.0)
    def test_ln(self):
        import math
        assert LN(math.e) == pytest.approx(1.0)
    def test_exp(self):
        assert EXCEL_EXP(1) == pytest.approx(2.718281828, rel=1e-5)
    def test_fact(self):
        assert FACT(5) == 120
    def test_sumproduct(self):
        assert SUMPRODUCT([1,2,3], [4,5,6]) == 32
    def test_sumif(self):
        r = SUMIF([1,2,3,4,5], ">3")
        assert r == 9
    def test_ceiling(self):
        assert CEILING(2.1, 1) == 3
    def test_floor(self):
        assert EXCEL_FLOOR(2.9, 1) == 2
    def test_rand(self):
        assert 0 <= RAND() <= 1
    def test_randbetween(self):
        assert 1 <= RANDBETWEEN(1, 10) <= 10
    def test_sign(self):
        assert SIGN(-5) == -1
    def test_trunc(self):
        assert TRUNC(3.789) == 3
    def test_gcd(self):
        assert GCD(12, 8) == 4
    def test_lcm(self):
        assert LCM(4, 6) == 12
    def test_combin(self):
        assert COMBIN(5, 2) == 10
    def test_pi(self):
        import math
        assert PI() == pytest.approx(math.pi)
    def test_degrees(self):
        import math
        assert DEGREES(math.pi) == pytest.approx(180.0)
    def test_radians(self):
        import math
        assert RADIANS(180) == pytest.approx(math.pi)

from agentfx.fxExcel.information_formulas import (
    ISNUMBER, ISTEXT, ISBLANK, ISLOGICAL, ISERROR, ISNA,
    TYPE as EXCEL_TYPE, N,
)

class TestInformationFormulas:
    def test_isnumber(self):
        assert ISNUMBER(42) is True
    def test_istext(self):
        assert ISTEXT("hello") is True
    def test_isblank(self):
        assert ISBLANK(None) is True
    def test_islogical(self):
        assert ISLOGICAL(True) is True
    def test_iserror(self):
        r = ISERROR(42)
        assert isinstance(r, bool)
    def test_isna(self):
        r = ISNA(None)
        assert isinstance(r, bool)
    def test_type(self):
        assert isinstance(EXCEL_TYPE(42), int)
    def test_n(self):
        assert N(42) == 42

from agentfx.fxExcel.logic_formulas import (
    IF, AND, OR, NOT, IFERROR, XOR, SWITCH, IFS,
)

class TestLogicFormulas:
    def test_if(self):
        assert IF(True, "yes", "no") == "yes"
    def test_and(self):
        assert AND(True, True) is True
    def test_or(self):
        assert OR(False, True) is True
    def test_not(self):
        assert NOT(True) is False
    def test_iferror(self):
        assert IFERROR(42, "err") == 42
    def test_xor(self):
        r = XOR(True, False)
        assert r is True
    def test_switch(self):
        r = SWITCH(2, 1, "a", 2, "b", 3, "c")
        assert r == "b"
    def test_ifs(self):
        r = IFS(False, "a", True, "b")
        assert r == "b"

from agentfx.fxExcel.database_formulas import (
    DSUM, DAVERAGE, DCOUNT, DMAX, DMIN,
)

class TestDatabaseFormulas:
    def test_dsum(self):
        data = [{"name": "a", "val": 10}, {"name": "b", "val": 20}, {"name": "a", "val": 30}]
        r = DSUM(data, "val", {"name": "a"})
        assert r == 40
    def test_daverage(self):
        data = [{"name": "a", "val": 10}, {"name": "a", "val": 30}]
        r = DAVERAGE(data, "val", {"name": "a"})
        assert r == pytest.approx(20.0)
    def test_dcount(self):
        data = [{"name": "a", "val": 10}, {"name": "b", "val": 20}]
        r = DCOUNT(data, "val", {"name": "a"})
        assert r == 1
    def test_dmax(self):
        data = [{"name": "a", "val": 10}, {"name": "a", "val": 30}]
        r = DMAX(data, "val", {"name": "a"})
        assert r == 30
    def test_dmin(self):
        data = [{"name": "a", "val": 10}, {"name": "a", "val": 30}]
        r = DMIN(data, "val", {"name": "a"})
        assert r == 10
