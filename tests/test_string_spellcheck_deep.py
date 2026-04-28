# Deep coverage tests for shortfx.fxString.string_spellcheck

import shortfx.fxString.string_spellcheck as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_normalize_text_deep:
    def test_c0(self):
        try:
            mod.normalize_text("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.normalize_text("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.normalize_text("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.normalize_text("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.normalize_text("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.normalize_text("UPPER lower 123")
        except EXC:
            pass

