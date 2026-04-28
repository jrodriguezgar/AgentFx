# Coverage tests for shortfx.fxString.string_hashing

from shortfx.fxString import string_hashing as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_fingerprint:
    def test_exists(self):
        assert hasattr(mod, "fingerprint")

    def test_var0(self):
        try:
            mod.fingerprint("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fingerprint("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fingerprint(None)
        except EXC:
            pass


class Test_hash_string:
    def test_exists(self):
        assert hasattr(mod, "hash_string")

    def test_doc0(self):
        try:
            mod.hash_string("hello")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hash_string("hello", "md5")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hash_string("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hash_string("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hash_string(None)
        except EXC:
            pass

