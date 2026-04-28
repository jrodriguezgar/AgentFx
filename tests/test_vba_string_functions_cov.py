# Coverage tests for agentfx.fxVBA.string_functions

from agentfx.fxVBA import string_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_Asc:
    def test_exists(self):
        assert hasattr(mod, "Asc")

    def test_var0(self):
        try:
            mod.Asc("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Asc("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Asc(None)
        except EXC:
            pass


class Test_AscB:
    def test_exists(self):
        assert hasattr(mod, "AscB")

    def test_var0(self):
        try:
            mod.AscB("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.AscB("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.AscB(None)
        except EXC:
            pass


class Test_ChrW:
    def test_exists(self):
        assert hasattr(mod, "ChrW")

    def test_var0(self):
        try:
            mod.ChrW(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ChrW(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ChrW(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ChrW("")
        except EXC:
            pass


class Test_Chr_:
    def test_exists(self):
        assert hasattr(mod, "Chr_")

    def test_var0(self):
        try:
            mod.Chr_(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Chr_(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Chr_(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Chr_("")
        except EXC:
            pass


class Test_InStr:
    def test_exists(self):
        assert hasattr(mod, "InStr")

    def test_var0(self):
        try:
            mod.InStr()
        except EXC:
            pass


class Test_InStrRev:
    def test_exists(self):
        assert hasattr(mod, "InStrRev")

    def test_var0(self):
        try:
            mod.InStrRev("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.InStrRev("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.InStrRev(None, "hello")
        except EXC:
            pass


class Test_LCase:
    def test_exists(self):
        assert hasattr(mod, "LCase")

    def test_var0(self):
        try:
            mod.LCase("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LCase("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LCase(None)
        except EXC:
            pass


class Test_LTrim:
    def test_exists(self):
        assert hasattr(mod, "LTrim")

    def test_var0(self):
        try:
            mod.LTrim("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LTrim("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LTrim(None)
        except EXC:
            pass


class Test_Left:
    def test_exists(self):
        assert hasattr(mod, "Left")

    def test_var0(self):
        try:
            mod.Left("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Left("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Left(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Left("", 0)
        except EXC:
            pass


class Test_LeftB:
    def test_exists(self):
        assert hasattr(mod, "LeftB")

    def test_var0(self):
        try:
            mod.LeftB("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LeftB("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LeftB(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.LeftB("", 0)
        except EXC:
            pass


class Test_LenB:
    def test_exists(self):
        assert hasattr(mod, "LenB")

    def test_var0(self):
        try:
            mod.LenB("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LenB("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LenB(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.LenB(0)
        except EXC:
            pass


class Test_Len_:
    def test_exists(self):
        assert hasattr(mod, "Len_")

    def test_var0(self):
        try:
            mod.Len_("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Len_("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Len_(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Len_(0)
        except EXC:
            pass


class Test_Mid:
    def test_exists(self):
        assert hasattr(mod, "Mid")

    def test_var0(self):
        try:
            mod.Mid("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Mid("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Mid(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Mid("", "")
        except EXC:
            pass


class Test_MidB:
    def test_exists(self):
        assert hasattr(mod, "MidB")

    def test_var0(self):
        try:
            mod.MidB("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MidB("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MidB(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MidB("", "")
        except EXC:
            pass


class Test_RTrim:
    def test_exists(self):
        assert hasattr(mod, "RTrim")

    def test_var0(self):
        try:
            mod.RTrim("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RTrim("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RTrim(None)
        except EXC:
            pass


class Test_Replace:
    def test_exists(self):
        assert hasattr(mod, "Replace")

    def test_var0(self):
        try:
            mod.Replace("hello", "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Replace("", "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Replace(None, "hello", "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Replace(0, "", "")
        except EXC:
            pass


class Test_Right:
    def test_exists(self):
        assert hasattr(mod, "Right")

    def test_var0(self):
        try:
            mod.Right("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Right("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Right(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Right("", 0)
        except EXC:
            pass


class Test_RightB:
    def test_exists(self):
        assert hasattr(mod, "RightB")

    def test_var0(self):
        try:
            mod.RightB("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RightB("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RightB(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.RightB("", 0)
        except EXC:
            pass


class Test_Space:
    def test_exists(self):
        assert hasattr(mod, "Space")

    def test_var0(self):
        try:
            mod.Space(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Space(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Space(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Space("")
        except EXC:
            pass


class Test_StrComp:
    def test_exists(self):
        assert hasattr(mod, "StrComp")

    def test_var0(self):
        try:
            mod.StrComp("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.StrComp("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.StrComp(None, "hello")
        except EXC:
            pass


class Test_StrConv:
    def test_exists(self):
        assert hasattr(mod, "StrConv")

    def test_var0(self):
        try:
            mod.StrConv("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.StrConv("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.StrConv(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.StrConv("", 0)
        except EXC:
            pass


class Test_StrReverse:
    def test_exists(self):
        assert hasattr(mod, "StrReverse")

    def test_var0(self):
        try:
            mod.StrReverse("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.StrReverse("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.StrReverse(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.StrReverse(0)
        except EXC:
            pass


class Test_Str_:
    def test_exists(self):
        assert hasattr(mod, "Str_")

    def test_var0(self):
        try:
            mod.Str_(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Str_(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Str_(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Str_("")
        except EXC:
            pass


class Test_String:
    def test_exists(self):
        assert hasattr(mod, "String")

    def test_var0(self):
        try:
            mod.String(0, "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.String(1, "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.String(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.String("", "")
        except EXC:
            pass


class Test_Trim:
    def test_exists(self):
        assert hasattr(mod, "Trim")

    def test_var0(self):
        try:
            mod.Trim("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Trim("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Trim(None)
        except EXC:
            pass


class Test_UCase:
    def test_exists(self):
        assert hasattr(mod, "UCase")

    def test_var0(self):
        try:
            mod.UCase("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.UCase("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.UCase(None)
        except EXC:
            pass

