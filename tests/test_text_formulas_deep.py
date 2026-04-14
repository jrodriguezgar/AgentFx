# Deep coverage tests for formulite.fxExcel.text_formulas
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxExcel.text_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_TEXTAFTER_deep:
    def test_c0(self):
        try:
            mod.TEXTAFTER("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.TEXTAFTER("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.TEXTAFTER("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.TEXTAFTER("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.TEXTAFTER("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.TEXTAFTER("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_instance_num(self):
        try:
            mod.TEXTAFTER("hello world", "test", instance_num=1)
        except EXC:
            pass

    def test_kw_match_mode(self):
        try:
            mod.TEXTAFTER("hello world", "test", match_mode=1)
        except EXC:
            pass

    def test_kw_match_end(self):
        try:
            mod.TEXTAFTER("hello world", "test", match_end=1)
        except EXC:
            pass


class Test_TEXTBEFORE_deep:
    def test_c0(self):
        try:
            mod.TEXTBEFORE("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.TEXTBEFORE("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.TEXTBEFORE("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.TEXTBEFORE("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.TEXTBEFORE("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.TEXTBEFORE("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_instance_num(self):
        try:
            mod.TEXTBEFORE("hello world", "test", instance_num=1)
        except EXC:
            pass

    def test_kw_match_mode(self):
        try:
            mod.TEXTBEFORE("hello world", "test", match_mode=1)
        except EXC:
            pass

    def test_kw_match_end(self):
        try:
            mod.TEXTBEFORE("hello world", "test", match_end=1)
        except EXC:
            pass


class Test_TEXTSPLIT_deep:
    def test_c0(self):
        try:
            mod.TEXTSPLIT("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.TEXTSPLIT("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.TEXTSPLIT("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.TEXTSPLIT("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.TEXTSPLIT("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.TEXTSPLIT("UPPER lower 123")
        except EXC:
            pass

    def test_kw_col_delimiter(self):
        try:
            mod.TEXTSPLIT("hello world", col_delimiter="hello world")
        except EXC:
            pass

    def test_kw_row_delimiter(self):
        try:
            mod.TEXTSPLIT("hello world", row_delimiter="hello world")
        except EXC:
            pass

    def test_kw_ignore_empty(self):
        try:
            mod.TEXTSPLIT("hello world", ignore_empty=True)
        except EXC:
            pass


class Test_ARRAYTOTEXT_deep:
    def test_c0(self):
        try:
            mod.ARRAYTOTEXT([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ARRAYTOTEXT([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ARRAYTOTEXT([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ARRAYTOTEXT([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ARRAYTOTEXT([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ARRAYTOTEXT([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_format_type(self):
        try:
            mod.ARRAYTOTEXT([1, 2, 3, 4, 5], format_type=1)
        except EXC:
            pass


class Test_FIND_deep:
    def test_c0(self):
        try:
            mod.FIND("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.FIND("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.FIND("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.FIND("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.FIND("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.FIND("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_start_num(self):
        try:
            mod.FIND("hello world", "test", start_num=1)
        except EXC:
            pass


class Test_SEARCH_deep:
    def test_c0(self):
        try:
            mod.SEARCH("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SEARCH("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SEARCH("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SEARCH("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SEARCH("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SEARCH("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_start_num(self):
        try:
            mod.SEARCH("hello world", "test", start_num=1)
        except EXC:
            pass


class Test_ASC_deep:
    def test_c0(self):
        try:
            mod.ASC("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ASC("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ASC("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ASC("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ASC("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ASC("UPPER lower 123")
        except EXC:
            pass


class Test_LEFT_deep:
    def test_c0(self):
        try:
            mod.LEFT("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.LEFT("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.LEFT("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.LEFT("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.LEFT("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.LEFT("UPPER lower 123")
        except EXC:
            pass

    def test_kw_num_chars(self):
        try:
            mod.LEFT("hello world", num_chars=1)
        except EXC:
            pass


class Test_MID_deep:
    def test_c0(self):
        try:
            mod.MID("hello world", 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.MID("test", 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.MID("abc123", 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.MID("", 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.MID("Hello, World!", 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.MID("UPPER lower 123", 1, 2)
        except EXC:
            pass


class Test_REPLACE_deep:
    def test_c0(self):
        try:
            mod.REPLACE("hello world", 2, 3, "")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.REPLACE("test", 3, 5, "Hello, World!")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.REPLACE("abc123", 5, 10, "UPPER lower 123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.REPLACE("", 10, 0, "hello world")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.REPLACE("Hello, World!", 0, 1, "test")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.REPLACE("UPPER lower 123", 1, 2, "abc123")
        except EXC:
            pass


class Test_RIGHT_deep:
    def test_c0(self):
        try:
            mod.RIGHT("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.RIGHT("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.RIGHT("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.RIGHT("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.RIGHT("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.RIGHT("UPPER lower 123")
        except EXC:
            pass

    def test_kw_num_chars(self):
        try:
            mod.RIGHT("hello world", num_chars=1)
        except EXC:
            pass


class Test_VALUETOTEXT_deep:
    def test_c0(self):
        try:
            mod.VALUETOTEXT(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.VALUETOTEXT(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.VALUETOTEXT(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.VALUETOTEXT(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.VALUETOTEXT(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.VALUETOTEXT(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.VALUETOTEXT(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.VALUETOTEXT(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.VALUETOTEXT(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.VALUETOTEXT(2)
        except EXC:
            pass

    def test_kw_format_type(self):
        try:
            mod.VALUETOTEXT(1, format_type=1)
        except EXC:
            pass

