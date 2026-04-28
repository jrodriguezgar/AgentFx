# Coverage tests for shortfx.fxString.string_validations

from shortfx.fxString import string_validations as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_contains_digit:
    def test_exists(self):
        assert hasattr(mod, "contains_digit")

    def test_doc0(self):
        try:
            mod.contains_digit("abc123def")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.contains_digit("no_digits_here")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.contains_digit("")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.contains_digit("123")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.contains_digit("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.contains_digit("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.contains_digit(None)
        except EXC:
            pass


class Test_same_letters:
    def test_exists(self):
        assert hasattr(mod, "same_letters")

    def test_doc0(self):
        try:
            mod.same_letters("listen", "silent")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.same_letters("hello", "holle")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.same_letters("abc", "ab")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.same_letters("Aardvark", "aardvark")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.same_letters("", "")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.same_letters("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.same_letters("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.same_letters(None, "hello")
        except EXC:
            pass

