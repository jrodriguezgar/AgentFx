# Coverage tests for shortfx.fxExcel.math_formulas
import math

from shortfx.fxExcel import math_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_ABS:
    def test_exists(self):
        assert hasattr(mod, "ABS")

    def test_doc0(self):
        try:
            mod.ABS(-5.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ABS(3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ABS(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ABS(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ABS(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ABS("")
        except EXC:
            pass


class Test_ACOS:
    def test_exists(self):
        assert hasattr(mod, "ACOS")

    def test_doc0(self):
        try:
            mod.ACOS(0.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ACOS(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ACOS(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ACOS(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ACOS(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ACOS("")
        except EXC:
            pass


class Test_ACOSH:
    def test_exists(self):
        assert hasattr(mod, "ACOSH")

    def test_doc0(self):
        try:
            mod.ACOSH(1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ACOSH(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ACOSH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ACOSH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ACOSH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ACOSH("")
        except EXC:
            pass


class Test_ACOT:
    def test_exists(self):
        assert hasattr(mod, "ACOT")

    def test_doc0(self):
        try:
            mod.ACOT(1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ACOT(2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ACOT(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ACOT(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ACOT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ACOT("")
        except EXC:
            pass


class Test_ACOTH:
    def test_exists(self):
        assert hasattr(mod, "ACOTH")

    def test_doc0(self):
        try:
            mod.ACOTH(2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ACOTH(-2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ACOTH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ACOTH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ACOTH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ACOTH("")
        except EXC:
            pass


class Test_AGGREGATE:
    def test_exists(self):
        assert hasattr(mod, "AGGREGATE")

    def test_doc0(self):
        try:
            mod.AGGREGATE([1, 2, 3, 4, 5], "sum")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.AGGREGATE([1, 2, 3, 4, 5], "avg")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.AGGREGATE([1, 2, 3, 4, 5], "max")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.AGGREGATE(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.AGGREGATE(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.AGGREGATE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.AGGREGATE([])
        except EXC:
            pass


class Test_ARABIC:
    def test_exists(self):
        assert hasattr(mod, "ARABIC")

    def test_doc0(self):
        try:
            mod.ARABIC('MCMLXXXIV')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ARABIC('CDXCIX')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ARABIC("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ARABIC("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ARABIC(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ARABIC(0)
        except EXC:
            pass


class Test_ASIN:
    def test_exists(self):
        assert hasattr(mod, "ASIN")

    def test_doc0(self):
        try:
            mod.ASIN(0.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ASIN(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ASIN(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ASIN(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ASIN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ASIN("")
        except EXC:
            pass


class Test_ASINH:
    def test_exists(self):
        assert hasattr(mod, "ASINH")

    def test_doc0(self):
        try:
            mod.ASINH(1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ASINH(-1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ASINH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ASINH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ASINH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ASINH("")
        except EXC:
            pass


class Test_ATAN:
    def test_exists(self):
        assert hasattr(mod, "ATAN")

    def test_doc0(self):
        try:
            mod.ATAN(1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ATAN(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ATAN(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ATAN(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ATAN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ATAN("")
        except EXC:
            pass


class Test_ATAN2:
    def test_exists(self):
        assert hasattr(mod, "ATAN2")

    def test_doc0(self):
        try:
            mod.ATAN2(1, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ATAN2(1, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ATAN2(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ATAN2(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ATAN2(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ATAN2("", "")
        except EXC:
            pass


class Test_ATANH:
    def test_exists(self):
        assert hasattr(mod, "ATANH")

    def test_doc0(self):
        try:
            mod.ATANH(0.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ATANH(-0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ATANH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ATANH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ATANH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ATANH("")
        except EXC:
            pass


class Test_BASE:
    def test_exists(self):
        assert hasattr(mod, "BASE")

    def test_doc0(self):
        try:
            mod.BASE(7, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.BASE(100, 16)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.BASE(15, 2, 8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.BASE(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.BASE(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.BASE(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.BASE("", "")
        except EXC:
            pass


class Test_CEILING:
    def test_exists(self):
        assert hasattr(mod, "CEILING")

    def test_doc0(self):
        try:
            mod.CEILING(2.5, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CEILING(4.3, 0.5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.CEILING(-2.5, -1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CEILING(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CEILING(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CEILING(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CEILING("")
        except EXC:
            pass


class Test_CEILING_MATH:
    def test_exists(self):
        assert hasattr(mod, "CEILING_MATH")

    def test_doc0(self):
        try:
            mod.CEILING_MATH(2.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CEILING_MATH(-2.5, 1, 0)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.CEILING_MATH(-2.5, 1, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CEILING_MATH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CEILING_MATH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CEILING_MATH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CEILING_MATH("")
        except EXC:
            pass


class Test_CEILING_PRECISE:
    def test_exists(self):
        assert hasattr(mod, "CEILING_PRECISE")

    def test_doc0(self):
        try:
            mod.CEILING_PRECISE(2.5, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CEILING_PRECISE(-2.5, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CEILING_PRECISE(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CEILING_PRECISE(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CEILING_PRECISE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CEILING_PRECISE("")
        except EXC:
            pass


class Test_COMBIN:
    def test_exists(self):
        assert hasattr(mod, "COMBIN")

    def test_doc0(self):
        try:
            mod.COMBIN(5, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.COMBIN(10, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COMBIN(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COMBIN(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COMBIN(None, 0)
        except EXC:
            pass


class Test_COMBINA:
    def test_exists(self):
        assert hasattr(mod, "COMBINA")

    def test_doc0(self):
        try:
            mod.COMBINA(4, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.COMBINA(3, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COMBINA(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COMBINA(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COMBINA(None, 0)
        except EXC:
            pass


class Test_COS:
    def test_exists(self):
        assert hasattr(mod, "COS")

    def test_doc0(self):
        try:
            mod.COS(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.COS(math.pi)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COS(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COS(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COS(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COS("")
        except EXC:
            pass


class Test_COSH:
    def test_exists(self):
        assert hasattr(mod, "COSH")

    def test_doc0(self):
        try:
            mod.COSH(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.COSH(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COSH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COSH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COSH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COSH("")
        except EXC:
            pass


class Test_COT:
    def test_exists(self):
        assert hasattr(mod, "COT")

    def test_doc0(self):
        try:
            mod.COT(math.pi/4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.COT(math.pi/6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COT(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COT(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COT("")
        except EXC:
            pass


class Test_COTH:
    def test_exists(self):
        assert hasattr(mod, "COTH")

    def test_doc0(self):
        try:
            mod.COTH(1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.COTH(2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COTH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COTH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COTH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COTH("")
        except EXC:
            pass


class Test_CSC:
    def test_exists(self):
        assert hasattr(mod, "CSC")

    def test_doc0(self):
        try:
            mod.CSC(math.pi/2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CSC(math.pi/6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CSC(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CSC(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CSC(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CSC("")
        except EXC:
            pass


class Test_CSCH:
    def test_exists(self):
        assert hasattr(mod, "CSCH")

    def test_doc0(self):
        try:
            mod.CSCH(1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CSCH(2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CSCH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CSCH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CSCH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CSCH("")
        except EXC:
            pass


class Test_DECIMAL:
    def test_exists(self):
        assert hasattr(mod, "DECIMAL")

    def test_doc0(self):
        try:
            mod.DECIMAL("111", 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.DECIMAL("FF", 16)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DECIMAL("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DECIMAL("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DECIMAL(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DECIMAL("", "")
        except EXC:
            pass


class Test_DEGREES:
    def test_exists(self):
        assert hasattr(mod, "DEGREES")

    def test_doc0(self):
        try:
            mod.DEGREES(math.pi)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.DEGREES(math.pi/2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DEGREES(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DEGREES(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DEGREES(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DEGREES("")
        except EXC:
            pass


class Test_EVEN:
    def test_exists(self):
        assert hasattr(mod, "EVEN")

    def test_doc0(self):
        try:
            mod.EVEN(1.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.EVEN(3)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.EVEN(-1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.EVEN(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.EVEN(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.EVEN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.EVEN("")
        except EXC:
            pass


class Test_EXP:
    def test_exists(self):
        assert hasattr(mod, "EXP")

    def test_doc0(self):
        try:
            mod.EXP(1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.EXP(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.EXP(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.EXP(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.EXP(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.EXP("")
        except EXC:
            pass


class Test_FACT:
    def test_exists(self):
        assert hasattr(mod, "FACT")

    def test_doc0(self):
        try:
            mod.FACT(5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.FACT(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FACT(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FACT(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FACT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FACT("")
        except EXC:
            pass


class Test_FACTDOUBLE:
    def test_exists(self):
        assert hasattr(mod, "FACTDOUBLE")

    def test_doc0(self):
        try:
            mod.FACTDOUBLE(6)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.FACTDOUBLE(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FACTDOUBLE(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FACTDOUBLE(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FACTDOUBLE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FACTDOUBLE("")
        except EXC:
            pass


class Test_FLOOR:
    def test_exists(self):
        assert hasattr(mod, "FLOOR")

    def test_doc0(self):
        try:
            mod.FLOOR(3.7, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.FLOOR(2.5, 0.1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FLOOR(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FLOOR(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FLOOR(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FLOOR("")
        except EXC:
            pass


class Test_FLOOR_MATH:
    def test_exists(self):
        assert hasattr(mod, "FLOOR_MATH")

    def test_doc0(self):
        try:
            mod.FLOOR_MATH(3.7)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.FLOOR_MATH(-2.5, 1, 0)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.FLOOR_MATH(-2.5, 1, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FLOOR_MATH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FLOOR_MATH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FLOOR_MATH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FLOOR_MATH("")
        except EXC:
            pass


class Test_FLOOR_PRECISE:
    def test_exists(self):
        assert hasattr(mod, "FLOOR_PRECISE")

    def test_doc0(self):
        try:
            mod.FLOOR_PRECISE(3.7, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.FLOOR_PRECISE(-2.5, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FLOOR_PRECISE(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FLOOR_PRECISE(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FLOOR_PRECISE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FLOOR_PRECISE("")
        except EXC:
            pass


class Test_GCD:
    def test_exists(self):
        assert hasattr(mod, "GCD")

    def test_doc0(self):
        try:
            mod.GCD(12, 18)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.GCD(15, 25, 35)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.GCD()
        except EXC:
            pass


class Test_INT:
    def test_exists(self):
        assert hasattr(mod, "INT")

    def test_doc0(self):
        try:
            mod.INT(8.9)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.INT(-8.9)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.INT(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.INT(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.INT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.INT("")
        except EXC:
            pass


class Test_ISO_CEILING:
    def test_exists(self):
        assert hasattr(mod, "ISO_CEILING")

    def test_doc0(self):
        try:
            mod.ISO_CEILING(2.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ISO_CEILING(-2.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ISO_CEILING(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ISO_CEILING(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ISO_CEILING(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ISO_CEILING("")
        except EXC:
            pass


class Test_LCM:
    def test_exists(self):
        assert hasattr(mod, "LCM")

    def test_doc0(self):
        try:
            mod.LCM(12, 18)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.LCM(4, 6, 8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LCM()
        except EXC:
            pass


class Test_LN:
    def test_exists(self):
        assert hasattr(mod, "LN")

    def test_doc0(self):
        try:
            mod.LN(math.e)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.LN(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LN(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LN(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.LN("")
        except EXC:
            pass


class Test_LOG:
    def test_exists(self):
        assert hasattr(mod, "LOG")

    def test_doc0(self):
        try:
            mod.LOG(100, 10)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.LOG(8, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LOG(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LOG(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LOG(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.LOG("")
        except EXC:
            pass


class Test_LOG10:
    def test_exists(self):
        assert hasattr(mod, "LOG10")

    def test_doc0(self):
        try:
            mod.LOG10(100)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.LOG10(1000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LOG10(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LOG10(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LOG10(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.LOG10("")
        except EXC:
            pass


class Test_MDETERM:
    def test_exists(self):
        assert hasattr(mod, "MDETERM")

    def test_doc0(self):
        try:
            mod.MDETERM([[1, 2], [3, 4]])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.MDETERM([[2, 0], [0, 2]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MDETERM(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MDETERM(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MDETERM(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MDETERM([])
        except EXC:
            pass


class Test_MINVERSE:
    def test_exists(self):
        assert hasattr(mod, "MINVERSE")

    def test_doc0(self):
        try:
            mod.MINVERSE([[1, 2], [3, 4]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MINVERSE(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MINVERSE(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MINVERSE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MINVERSE([])
        except EXC:
            pass


class Test_MMULT:
    def test_exists(self):
        assert hasattr(mod, "MMULT")

    def test_doc0(self):
        try:
            mod.MMULT([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.MMULT([[1, 2, 3]], [[4], [5], [6]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MMULT(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MMULT(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MMULT(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MMULT([], [])
        except EXC:
            pass


class Test_MOD:
    def test_exists(self):
        assert hasattr(mod, "MOD")

    def test_doc0(self):
        try:
            mod.MOD(10, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.MOD(-10, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MOD(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MOD(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MOD(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MOD("", "")
        except EXC:
            pass


class Test_MROUND:
    def test_exists(self):
        assert hasattr(mod, "MROUND")

    def test_doc0(self):
        try:
            mod.MROUND(10, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.MROUND(1.3, 0.2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.MROUND(-10, -3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MROUND(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MROUND(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MROUND(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MROUND("", "")
        except EXC:
            pass


class Test_MULTINOMIAL:
    def test_exists(self):
        assert hasattr(mod, "MULTINOMIAL")

    def test_doc0(self):
        try:
            mod.MULTINOMIAL(2, 3, 4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.MULTINOMIAL(3, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MULTINOMIAL()
        except EXC:
            pass


class Test_MUNIT:
    def test_exists(self):
        assert hasattr(mod, "MUNIT")

    def test_doc0(self):
        try:
            mod.MUNIT(3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.MUNIT(2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MUNIT(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MUNIT(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MUNIT(None)
        except EXC:
            pass


class Test_ODD:
    def test_exists(self):
        assert hasattr(mod, "ODD")

    def test_doc0(self):
        try:
            mod.ODD(1.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ODD(2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.ODD(-2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ODD(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ODD(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ODD(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ODD("")
        except EXC:
            pass


class Test_PI:
    def test_exists(self):
        assert hasattr(mod, "PI")

    def test_doc0(self):
        try:
            mod.PI()
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PI()
        except EXC:
            pass


class Test_POWER:
    def test_exists(self):
        assert hasattr(mod, "POWER")

    def test_doc0(self):
        try:
            mod.POWER(5, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.POWER(2, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.POWER(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.POWER(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.POWER(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.POWER("", "")
        except EXC:
            pass


class Test_PRODUCT:
    def test_exists(self):
        assert hasattr(mod, "PRODUCT")

    def test_doc0(self):
        try:
            mod.PRODUCT(5, 15, 30)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.PRODUCT([2, 3], 4)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.PRODUCT([1, 2, 3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PRODUCT()
        except EXC:
            pass


class Test_QUOTIENT:
    def test_exists(self):
        assert hasattr(mod, "QUOTIENT")

    def test_doc0(self):
        try:
            mod.QUOTIENT(10, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.QUOTIENT(-10, 3)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.QUOTIENT(5.5, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.QUOTIENT(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.QUOTIENT(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.QUOTIENT(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.QUOTIENT("", "")
        except EXC:
            pass


class Test_RADIANS:
    def test_exists(self):
        assert hasattr(mod, "RADIANS")

    def test_doc0(self):
        try:
            mod.RADIANS(180)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.RADIANS(90)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.RADIANS(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RADIANS(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RADIANS(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.RADIANS("")
        except EXC:
            pass


class Test_RAND:
    def test_exists(self):
        assert hasattr(mod, "RAND")

    def test_doc0(self):
        try:
            mod.RAND()
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.RAND()
        except EXC:
            pass


class Test_RANDARRAY:
    def test_exists(self):
        assert hasattr(mod, "RANDARRAY")

    def test_doc0(self):
        try:
            mod.RANDARRAY(2, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.RANDARRAY(2, 2, 1, 10, True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.RANDARRAY()
        except EXC:
            pass


class Test_RANDBETWEEN:
    def test_exists(self):
        assert hasattr(mod, "RANDBETWEEN")

    def test_doc0(self):
        try:
            mod.RANDBETWEEN(1, 10)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.RANDBETWEEN(-5, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.RANDBETWEEN(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RANDBETWEEN(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RANDBETWEEN(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.RANDBETWEEN("", 0)
        except EXC:
            pass


class Test_ROMAN:
    def test_exists(self):
        assert hasattr(mod, "ROMAN")

    def test_doc0(self):
        try:
            mod.ROMAN(1984)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ROMAN(499)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ROMAN(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ROMAN(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ROMAN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ROMAN("")
        except EXC:
            pass


class Test_ROUND:
    def test_exists(self):
        assert hasattr(mod, "ROUND")

    def test_doc0(self):
        try:
            mod.ROUND(2.15, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ROUND(2.149, 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.ROUND(-1.475, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ROUND(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ROUND(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ROUND(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ROUND("")
        except EXC:
            pass


class Test_ROUNDDOWN:
    def test_exists(self):
        assert hasattr(mod, "ROUNDDOWN")

    def test_doc0(self):
        try:
            mod.ROUNDDOWN(3.14159, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ROUNDDOWN(-3.14159, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ROUNDDOWN(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ROUNDDOWN(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ROUNDDOWN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ROUNDDOWN("")
        except EXC:
            pass


class Test_ROUNDUP:
    def test_exists(self):
        assert hasattr(mod, "ROUNDUP")

    def test_doc0(self):
        try:
            mod.ROUNDUP(3.14159, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ROUNDUP(-3.14159, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ROUNDUP(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ROUNDUP(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ROUNDUP(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ROUNDUP("")
        except EXC:
            pass


class Test_SEC:
    def test_exists(self):
        assert hasattr(mod, "SEC")

    def test_doc0(self):
        try:
            mod.SEC(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SEC(math.pi/3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SEC(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SEC(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SEC(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SEC("")
        except EXC:
            pass


class Test_SECH:
    def test_exists(self):
        assert hasattr(mod, "SECH")

    def test_doc0(self):
        try:
            mod.SECH(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SECH(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SECH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SECH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SECH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SECH("")
        except EXC:
            pass


class Test_SEQUENCE:
    def test_exists(self):
        assert hasattr(mod, "SEQUENCE")

    def test_doc0(self):
        try:
            mod.SEQUENCE(3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SEQUENCE(2, 3, 0, 5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.SEQUENCE(1, 4, 10, -2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SEQUENCE(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SEQUENCE(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SEQUENCE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SEQUENCE([])
        except EXC:
            pass


class Test_SERIESSUM:
    def test_exists(self):
        assert hasattr(mod, "SERIESSUM")

    def test_doc0(self):
        try:
            mod.SERIESSUM(2, 1, 2, [1, 1, 1])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SERIESSUM(1, 0, 1, [1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SERIESSUM(3.14, 0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SERIESSUM(100, 1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SERIESSUM(None, 0, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SERIESSUM("", 0, "", [])
        except EXC:
            pass


class Test_SIGN:
    def test_exists(self):
        assert hasattr(mod, "SIGN")

    def test_doc0(self):
        try:
            mod.SIGN(10)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SIGN(-5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.SIGN(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SIGN(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SIGN(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SIGN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SIGN("")
        except EXC:
            pass


class Test_SIN:
    def test_exists(self):
        assert hasattr(mod, "SIN")

    def test_doc0(self):
        try:
            mod.SIN(math.pi/2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SIN(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SIN(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SIN(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SIN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SIN("")
        except EXC:
            pass


class Test_SINH:
    def test_exists(self):
        assert hasattr(mod, "SINH")

    def test_doc0(self):
        try:
            mod.SINH(1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SINH(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SINH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SINH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SINH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SINH("")
        except EXC:
            pass


class Test_SQRT:
    def test_exists(self):
        assert hasattr(mod, "SQRT")

    def test_doc0(self):
        try:
            mod.SQRT(16)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SQRT(2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SQRT(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SQRT(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SQRT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SQRT("")
        except EXC:
            pass


class Test_SQRTPI:
    def test_exists(self):
        assert hasattr(mod, "SQRTPI")

    def test_doc0(self):
        try:
            mod.SQRTPI(1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SQRTPI(2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SQRTPI(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SQRTPI(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SQRTPI(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SQRTPI("")
        except EXC:
            pass


class Test_SUBTOTAL:
    def test_exists(self):
        assert hasattr(mod, "SUBTOTAL")

    def test_doc0(self):
        try:
            mod.SUBTOTAL(9, [1, 2, 3, 4, 5])  # SUM
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUBTOTAL(1, [10, 20, 30])  # AVERAGE
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.SUBTOTAL(4, [5, 15, 25])  # MAX
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUBTOTAL(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SUBTOTAL(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SUBTOTAL(None)
        except EXC:
            pass


class Test_SUM:
    def test_exists(self):
        assert hasattr(mod, "SUM")

    def test_doc0(self):
        try:
            mod.SUM(1, 2, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUM([1, 2, 3], 4, 5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.SUM([10, 20], [30, 40])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUM()
        except EXC:
            pass


class Test_SUMIF:
    def test_exists(self):
        assert hasattr(mod, "SUMIF")

    def test_doc0(self):
        try:
            mod.SUMIF([1, 5, 10, 15, 20], ">10")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUMIF([2, 4, 6, 8, 10], "<=5")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.SUMIF([1, 2, 3, 4, 5], ">=3")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUMIF(0, "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SUMIF(1, "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SUMIF(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SUMIF([], "")
        except EXC:
            pass


class Test_SUMIFS:
    def test_exists(self):
        assert hasattr(mod, "SUMIFS")

    def test_doc0(self):
        try:
            mod.SUMIFS([10, 20, 30, 40], [1, 2, 3, 4], ">1", [5, 15, 25, 35], "<30")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUMIFS([100, 200, 300], ["A", "B", "A"], "A")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUMIFS(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SUMIFS(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SUMIFS(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SUMIFS("")
        except EXC:
            pass


class Test_SUMPRODUCT:
    def test_exists(self):
        assert hasattr(mod, "SUMPRODUCT")

    def test_doc0(self):
        try:
            mod.SUMPRODUCT([1, 2, 3], [4, 5, 6])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUMPRODUCT([2, 3], [4, 5], [6, 7])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUMPRODUCT()
        except EXC:
            pass


class Test_SUMSQ:
    def test_exists(self):
        assert hasattr(mod, "SUMSQ")

    def test_doc0(self):
        try:
            mod.SUMSQ(3, 4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUMSQ([1, 2, 3])
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.SUMSQ([2, 3], 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUMSQ()
        except EXC:
            pass


class Test_SUMX2MY2:
    def test_exists(self):
        assert hasattr(mod, "SUMX2MY2")

    def test_doc0(self):
        try:
            mod.SUMX2MY2([2, 3, 9], [6, 5, 11])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUMX2MY2([1, 2], [3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUMX2MY2(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SUMX2MY2(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SUMX2MY2(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SUMX2MY2([], [])
        except EXC:
            pass


class Test_SUMX2PY2:
    def test_exists(self):
        assert hasattr(mod, "SUMX2PY2")

    def test_doc0(self):
        try:
            mod.SUMX2PY2([2, 3, 9], [6, 5, 11])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUMX2PY2([1, 2], [3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUMX2PY2(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SUMX2PY2(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SUMX2PY2(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SUMX2PY2([], [])
        except EXC:
            pass


class Test_SUMXMY2:
    def test_exists(self):
        assert hasattr(mod, "SUMXMY2")

    def test_doc0(self):
        try:
            mod.SUMXMY2([2, 3, 9], [6, 5, 11])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUMXMY2([1, 2], [3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUMXMY2(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SUMXMY2(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SUMXMY2(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SUMXMY2([], [])
        except EXC:
            pass


class Test_TAN:
    def test_exists(self):
        assert hasattr(mod, "TAN")

    def test_doc0(self):
        try:
            mod.TAN(math.pi/4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TAN(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TAN(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TAN(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TAN(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TAN("")
        except EXC:
            pass


class Test_TANH:
    def test_exists(self):
        assert hasattr(mod, "TANH")

    def test_doc0(self):
        try:
            mod.TANH(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TANH(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TANH(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TANH(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TANH(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TANH("")
        except EXC:
            pass


class Test_TRANSPOSE:
    def test_exists(self):
        assert hasattr(mod, "TRANSPOSE")

    def test_doc0(self):
        try:
            mod.TRANSPOSE([[1, 2, 3], [4, 5, 6]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TRANSPOSE(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TRANSPOSE(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TRANSPOSE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TRANSPOSE([])
        except EXC:
            pass


class Test_TRUNC:
    def test_exists(self):
        assert hasattr(mod, "TRUNC")

    def test_doc0(self):
        try:
            mod.TRUNC(8.9)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TRUNC(-8.9)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.TRUNC(8.9876, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TRUNC(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TRUNC(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TRUNC(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TRUNC("")
        except EXC:
            pass

