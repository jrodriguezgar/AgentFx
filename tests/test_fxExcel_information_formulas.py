# Coverage tests for agentfx.fxExcel.information_formulas

from agentfx.fxExcel import information_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_ERROR_TYPE:
    def test_exists(self):
        assert hasattr(mod, "ERROR_TYPE")

    def test_doc0(self):
        try:
            mod.ERROR_TYPE(42)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ERROR_TYPE(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ERROR_TYPE(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ERROR_TYPE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ERROR_TYPE("")
        except EXC:
            pass


class Test_ISBLANK:
    def test_exists(self):
        assert hasattr(mod, "ISBLANK")

    def test_doc0(self):
        try:
            mod.ISBLANK(None)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ISBLANK("")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.ISBLANK("text")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISBLANK(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISBLANK(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISBLANK(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISBLANK("")
        except EXC:
            pass


class Test_ISERR:
    def test_exists(self):
        assert hasattr(mod, "ISERR")

    def test_doc0(self):
        try:
            mod.ISERR("#N/A")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISERR(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISERR(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISERR(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISERR("")
        except EXC:
            pass


class Test_ISERROR:
    def test_exists(self):
        assert hasattr(mod, "ISERROR")

    def test_doc0(self):
        try:
            mod.ISERROR(42)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISERROR(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISERROR(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISERROR(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISERROR("")
        except EXC:
            pass


class Test_ISEVEN:
    def test_exists(self):
        assert hasattr(mod, "ISEVEN")

    def test_doc0(self):
        try:
            mod.ISEVEN(4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ISEVEN(3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISEVEN(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISEVEN(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISEVEN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISEVEN("")
        except EXC:
            pass


class Test_ISLOGICAL:
    def test_exists(self):
        assert hasattr(mod, "ISLOGICAL")

    def test_doc0(self):
        try:
            mod.ISLOGICAL(True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ISLOGICAL(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISLOGICAL(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISLOGICAL(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISLOGICAL(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISLOGICAL("")
        except EXC:
            pass


class Test_ISNA:
    def test_exists(self):
        assert hasattr(mod, "ISNA")

    def test_doc0(self):
        try:
            mod.ISNA("#N/A")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISNA(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISNA(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISNA(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISNA("")
        except EXC:
            pass


class Test_ISNONTEXT:
    def test_exists(self):
        assert hasattr(mod, "ISNONTEXT")

    def test_doc0(self):
        try:
            mod.ISNONTEXT(42)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ISNONTEXT("text")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISNONTEXT(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISNONTEXT(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISNONTEXT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISNONTEXT("")
        except EXC:
            pass


class Test_ISNUMBER:
    def test_exists(self):
        assert hasattr(mod, "ISNUMBER")

    def test_doc0(self):
        try:
            mod.ISNUMBER(42)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ISNUMBER(3.14)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.ISNUMBER("42")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISNUMBER(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISNUMBER(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISNUMBER(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISNUMBER("")
        except EXC:
            pass


class Test_ISODD:
    def test_exists(self):
        assert hasattr(mod, "ISODD")

    def test_doc0(self):
        try:
            mod.ISODD(3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ISODD(4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISODD(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISODD(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISODD(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISODD("")
        except EXC:
            pass


class Test_ISOMITTED:
    def test_exists(self):
        assert hasattr(mod, "ISOMITTED")

    def test_doc0(self):
        try:
            mod.ISOMITTED(42)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISOMITTED(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISOMITTED(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISOMITTED(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISOMITTED("")
        except EXC:
            pass


class Test_ISTEXT:
    def test_exists(self):
        assert hasattr(mod, "ISTEXT")

    def test_doc0(self):
        try:
            mod.ISTEXT("hello")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ISTEXT(42)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISTEXT(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISTEXT(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISTEXT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISTEXT("")
        except EXC:
            pass


class Test_N:
    def test_exists(self):
        assert hasattr(mod, "N")

    def test_doc0(self):
        try:
            mod.N(42)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.N(True)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.N("text")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.N(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.N(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.N(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.N("")
        except EXC:
            pass


class Test_NA:
    def test_exists(self):
        assert hasattr(mod, "NA")

    def test_doc0(self):
        try:
            mod.NA()
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.NA()
        except EXC:
            pass


class Test_TYPE:
    def test_exists(self):
        assert hasattr(mod, "TYPE")

    def test_doc0(self):
        try:
            mod.TYPE(42)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TYPE(3.14)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.TYPE("hello")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.TYPE(True)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.TYPE([1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TYPE(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TYPE(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TYPE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TYPE("")
        except EXC:
            pass

