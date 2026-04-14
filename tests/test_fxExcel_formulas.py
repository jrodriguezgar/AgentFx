'''Tests for formulite.fxExcel modules (excluding engineering/statistic).'''
import pytest
from datetime import datetime

# -- database_formulas --
from formulite.fxExcel.database_formulas import (
    DAVERAGE, DCOUNT, DMAX, DMIN, DSUM, DGET,
)

DB = [
    {"name": "Alice", "dept": "Sales", "salary": 50000},
    {"name": "Bob", "dept": "Sales", "salary": 60000},
    {"name": "Charlie", "dept": "Engineering", "salary": 70000},
    {"name": "Diana", "dept": "Engineering", "salary": 80000},
]

class TestDatabase:
    def test_daverage(self):
        assert DAVERAGE(DB, "salary") == pytest.approx(65000)
    def test_dcount(self):
        assert DCOUNT(DB, "salary") == 4
    def test_dcount_criteria(self):
        assert DCOUNT(DB, "salary", {"dept": "Sales"}) == 2
    def test_dmax(self):
        assert DMAX(DB, "salary") == 80000
    def test_dmin(self):
        assert DMIN(DB, "salary") == 50000
    def test_dsum(self):
        assert DSUM(DB, "salary") == 260000
    def test_dget(self):
        r = DGET(DB, "name", {"dept": "Sales"})
        assert r == "Alice"

# -- information_formulas --
from formulite.fxExcel.information_formulas import (
    ISBLANK, ISERROR, ISLOGICAL, ISNUMBER, ISTEXT, TYPE,
)

class TestInformation:
    def test_isblank(self):
        assert ISBLANK(None) is True and ISBLANK(0) is False
    def test_iserror(self):
        assert ISERROR(ValueError()) is True
    def test_islogical(self):
        assert ISLOGICAL(True) is True and ISLOGICAL(1) is False
    def test_isnumber(self):
        assert ISNUMBER(42) is True and ISNUMBER("x") is False
    def test_istext(self):
        assert ISTEXT("hello") is True and ISTEXT(42) is False
    def test_type(self):
        assert TYPE(1) == 1

# -- logic_formulas --
from formulite.fxExcel.logic_formulas import (
    AND, OR, NOT, IF, IFERROR, XOR,
)

class TestLogicFormulas:
    def test_and(self):
        assert AND(True, True) is True
        assert AND(True, False) is False
    def test_or(self):
        assert OR(False, True) is True
        assert OR(False, False) is False
    def test_not(self):
        assert NOT(True) is False
    def test_if(self):
        assert IF(True, "y", "n") == "y"
    def test_iferror(self):
        assert IFERROR(42, "err") == 42
    def test_xor(self):
        assert XOR(True, False) is True
        assert XOR(True, True) is False

# -- math_formulas --
from formulite.fxExcel.math_formulas import (
    ABS, CEILING, FLOOR, INT, MOD, POWER, ROUND,
    SQRT, SUM, SUMPRODUCT, PRODUCT, SIGN,
)

class TestMathFormulas:
    def test_abs(self):
        assert ABS(-5) == 5
    def test_ceiling(self):
        assert CEILING(2.3, 1) == 3
    def test_floor(self):
        assert FLOOR(2.7, 1) == 2
    def test_int(self):
        assert INT(3.7) == 3
    def test_mod(self):
        assert MOD(10, 3) == 1
    def test_power(self):
        assert POWER(2, 3) == 8
    def test_round(self):
        assert ROUND(3.456, 2) == pytest.approx(3.46)
    def test_sqrt(self):
        assert SQRT(9) == pytest.approx(3.0)
    def test_sum(self):
        assert SUM(1, 2, 3) == 6
    def test_sumproduct(self):
        assert SUMPRODUCT([1, 2, 3], [4, 5, 6]) == 32
    def test_product(self):
        assert PRODUCT(2, 3, 4) == 24
    def test_sign(self):
        assert SIGN(5) == 1 and SIGN(-5) == -1 and SIGN(0) == 0

# -- text_formulas --
from formulite.fxExcel.text_formulas import (
    CONCATENATE, LEFT, RIGHT, MID, LEN, LOWER, UPPER, TRIM,
    FIND, SEARCH, SUBSTITUTE, REPT, TEXT,
)

class TestTextFormulas:
    def test_concatenate(self):
        assert CONCATENATE("Hello", " ", "World") == "Hello World"
    def test_left(self):
        assert LEFT("Hello", 3) == "Hel"
    def test_right(self):
        assert RIGHT("Hello", 3) == "llo"
    def test_mid(self):
        assert MID("Hello World", 7, 5) == "World"
    def test_len(self):
        assert LEN("Hello") == 5
    def test_lower(self):
        assert LOWER("HELLO") == "hello"
    def test_upper(self):
        assert UPPER("hello") == "HELLO"
    def test_trim(self):
        assert TRIM("  Hello  ") == "Hello"
    def test_find(self):
        assert FIND("World", "Hello World") == 7
    def test_search(self):
        assert SEARCH("world", "Hello World") == 7
    def test_substitute(self):
        assert SUBSTITUTE("Hello World", "World", "Python") == "Hello Python"
    def test_rept(self):
        assert REPT("ab", 3) == "ababab"
    def test_text(self):
        r = TEXT(1234.5, "#,##0.00")
        assert isinstance(r, str)

# -- lookup_formulas --
from formulite.fxExcel.lookup_formulas import (
    VLOOKUP, HLOOKUP, INDEX, MATCH, CHOOSE,
)

class TestLookup:
    def test_vlookup(self):
        table = [[1, "a"], [2, "b"], [3, "c"]]
        assert VLOOKUP(2, table, 2) == "b"
    def test_hlookup(self):
        table = [[1, 2, 3], ["a", "b", "c"]]
        assert HLOOKUP(2, table, 2) == "b"
    def test_index(self):
        data = [[1, 2], [3, 4]]
        assert INDEX(data, 2, 2) == 4
    def test_match(self):
        assert MATCH(3, [1, 2, 3, 4]) == 3
    def test_choose(self):
        assert CHOOSE(2, "a", "b", "c") == "b"

# -- date_formulas --
from formulite.fxExcel.date_formulas import (
    TODAY, NOW, YEAR, MONTH, DAY, DATE, EDATE, EOMONTH,
    WEEKDAY, WEEKNUM, DAYS,
)

class TestDateFormulas:
    def test_today(self):
        r = TODAY()
        assert r is not None
    def test_now(self):
        r = NOW()
        assert r is not None
    def test_year(self):
        assert YEAR(datetime(2026, 4, 13)) == 2026
    def test_month(self):
        assert MONTH(datetime(2026, 4, 13)) == 4
    def test_day(self):
        assert DAY(datetime(2026, 4, 13)) == 13
    def test_date(self):
        r = DATE(2026, 4, 13)
        assert r is not None
    def test_edate(self):
        r = EDATE(datetime(2026, 1, 15), 2)
        assert r is not None
    def test_eomonth(self):
        r = EOMONTH(datetime(2026, 1, 15), 0)
        assert r is not None
    def test_weekday(self):
        assert isinstance(WEEKDAY(datetime(2026, 4, 13)), int)
    def test_weeknum(self):
        assert isinstance(WEEKNUM(datetime(2026, 4, 13)), int)
    def test_days(self):
        assert DAYS(datetime(2026, 1, 11), datetime(2026, 1, 1)) == 10
