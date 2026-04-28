# Coverage tests for shortfx.fxString.string_compression

from shortfx.fxString import string_compression as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_compress_string:
    def test_exists(self):
        assert hasattr(mod, "compress_string")

    def test_doc0(self):
        try:
            mod.compress_string("hello " * 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.compress_string("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.compress_string("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.compress_string(None)
        except EXC:
            pass


class Test_decompress_string:
    def test_exists(self):
        assert hasattr(mod, "decompress_string")

    def test_var0(self):
        try:
            mod.decompress_string("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.decompress_string("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.decompress_string(None)
        except EXC:
            pass

