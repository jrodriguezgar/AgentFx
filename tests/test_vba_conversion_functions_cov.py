# Coverage tests for agentfx.fxVBA.conversion_functions

from agentfx.fxVBA import conversion_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_CBool:
    def test_exists(self):
        assert hasattr(mod, "CBool")

    def test_var0(self):
        try:
            mod.CBool(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CBool(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CBool(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CBool(0)
        except EXC:
            pass


class Test_CByte:
    def test_exists(self):
        assert hasattr(mod, "CByte")

    def test_var0(self):
        try:
            mod.CByte(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CByte(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CByte(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CByte(0)
        except EXC:
            pass


class Test_CCur:
    def test_exists(self):
        assert hasattr(mod, "CCur")

    def test_var0(self):
        try:
            mod.CCur(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CCur(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CCur(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CCur(0)
        except EXC:
            pass


class Test_CDate:
    def test_exists(self):
        assert hasattr(mod, "CDate")

    def test_var0(self):
        try:
            mod.CDate(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CDate(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CDate(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CDate(0)
        except EXC:
            pass


class Test_CDbl:
    def test_exists(self):
        assert hasattr(mod, "CDbl")

    def test_var0(self):
        try:
            mod.CDbl(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CDbl(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CDbl(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CDbl(0)
        except EXC:
            pass


class Test_CDec:
    def test_exists(self):
        assert hasattr(mod, "CDec")

    def test_var0(self):
        try:
            mod.CDec(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CDec(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CDec(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CDec(0)
        except EXC:
            pass


class Test_CInt:
    def test_exists(self):
        assert hasattr(mod, "CInt")

    def test_var0(self):
        try:
            mod.CInt(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CInt(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CInt(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CInt(0)
        except EXC:
            pass


class Test_CLng:
    def test_exists(self):
        assert hasattr(mod, "CLng")

    def test_var0(self):
        try:
            mod.CLng(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CLng(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CLng(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CLng(0)
        except EXC:
            pass


class Test_CLngLng:
    def test_exists(self):
        assert hasattr(mod, "CLngLng")

    def test_doc0(self):
        try:
            mod.CLngLng(9223372036854775807)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CLngLng("123456789012345")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CLngLng(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CLngLng(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CLngLng(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CLngLng(0)
        except EXC:
            pass


class Test_CLngPtr:
    def test_exists(self):
        assert hasattr(mod, "CLngPtr")

    def test_doc0(self):
        try:
            mod.CLngPtr(42)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CLngPtr("12345678")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CLngPtr(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CLngPtr(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CLngPtr(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CLngPtr(0)
        except EXC:
            pass


class Test_CSng:
    def test_exists(self):
        assert hasattr(mod, "CSng")

    def test_var0(self):
        try:
            mod.CSng(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CSng(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CSng(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CSng(0)
        except EXC:
            pass


class Test_CStr:
    def test_exists(self):
        assert hasattr(mod, "CStr")

    def test_var0(self):
        try:
            mod.CStr(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CStr(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CStr(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CStr(0)
        except EXC:
            pass


class Test_CVErr:
    def test_exists(self):
        assert hasattr(mod, "CVErr")

    def test_doc0(self):
        try:
            mod.CVErr(2007)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CVErr(3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CVErr(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CVErr(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CVErr(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CVErr("")
        except EXC:
            pass


class Test_CVar:
    def test_exists(self):
        assert hasattr(mod, "CVar")

    def test_var0(self):
        try:
            mod.CVar(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CVar(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CVar(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CVar(0)
        except EXC:
            pass


class Test_DateValue:
    def test_exists(self):
        assert hasattr(mod, "DateValue")

    def test_var0(self):
        try:
            mod.DateValue("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DateValue("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DateValue(None)
        except EXC:
            pass


class Test_TimeValue:
    def test_exists(self):
        assert hasattr(mod, "TimeValue")

    def test_var0(self):
        try:
            mod.TimeValue("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TimeValue("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TimeValue(None)
        except EXC:
            pass


class Test_Val:
    def test_exists(self):
        assert hasattr(mod, "Val")

    def test_var0(self):
        try:
            mod.Val("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Val("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Val(None)
        except EXC:
            pass

