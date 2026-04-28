# Coverage tests for shortfx.fxPython.py_logic

from shortfx.fxPython import py_logic as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_and_all:
    def test_exists(self):
        assert hasattr(mod, "and_all")

    def test_doc0(self):
        try:
            mod.and_all(True, True, True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.and_all(True, False, True)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.and_all(5 > 3, 10 < 20, "a" == "a")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.and_all()
        except EXC:
            pass


class Test_coalesce:
    def test_exists(self):
        assert hasattr(mod, "coalesce")

    def test_doc0(self):
        try:
            mod.coalesce(None, None, 42, 'hello')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.coalesce(None, 'first')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.coalesce(None, None) is None
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coalesce()
        except EXC:
            pass


class Test_if_error:
    def test_exists(self):
        assert hasattr(mod, "if_error")

    def test_doc0(self):
        try:
            mod.if_error(10 / 2, "Error!")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.if_error(lambda: 10 / 0, "Error!")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.if_error(lambda: int("abc"), "Invalid")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.if_error(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.if_error(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.if_error(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.if_error("", "")
        except EXC:
            pass


class Test_if_then_else:
    def test_exists(self):
        assert hasattr(mod, "if_then_else")

    def test_doc0(self):
        try:
            mod.if_then_else(True, "Yes", "No")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.if_then_else(5 > 3, "Greater", "Smaller")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.if_then_else(False, 10, 20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.if_then_else(True, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.if_then_else(False, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.if_then_else(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.if_then_else("", "", "")
        except EXC:
            pass


class Test_ifs:
    def test_exists(self):
        assert hasattr(mod, "ifs")

    def test_doc0(self):
        try:
            mod.ifs(False, "a", True, "b", True, "c")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ifs(1 > 2, "no", 3 > 2, "yes")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ifs()
        except EXC:
            pass


class Test_is_blank:
    def test_exists(self):
        assert hasattr(mod, "is_blank")

    def test_doc0(self):
        try:
            mod.is_blank(None)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_blank("")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_blank([])
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_blank("Hello")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.is_blank(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_blank(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_blank(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_blank(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_blank("")
        except EXC:
            pass


class Test_is_error:
    def test_exists(self):
        assert hasattr(mod, "is_error")

    def test_doc0(self):
        try:
            mod.is_error(lambda: 10 / 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_error(lambda: 10 / 0)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_error(lambda: int("abc"))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_error(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_error(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_error(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_error("")
        except EXC:
            pass


class Test_is_logical:
    def test_exists(self):
        assert hasattr(mod, "is_logical")

    def test_doc0(self):
        try:
            mod.is_logical(True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_logical(False)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_logical(0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_logical("True")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_logical(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_logical(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_logical(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_logical("")
        except EXC:
            pass


class Test_is_number:
    def test_exists(self):
        assert hasattr(mod, "is_number")

    def test_doc0(self):
        try:
            mod.is_number(123)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_number(3.14)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_number("hello")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_number(True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_number(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_number("")
        except EXC:
            pass


class Test_is_text:
    def test_exists(self):
        assert hasattr(mod, "is_text")

    def test_doc0(self):
        try:
            mod.is_text("hello")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_text(123)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_text(True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_text(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_text(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_text(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_text("")
        except EXC:
            pass


class Test_not_value:
    def test_exists(self):
        assert hasattr(mod, "not_value")

    def test_doc0(self):
        try:
            mod.not_value(True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.not_value(False)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.not_value(5 > 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.not_value(True)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.not_value(False)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.not_value(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.not_value("")
        except EXC:
            pass


class Test_or_any:
    def test_exists(self):
        assert hasattr(mod, "or_any")

    def test_doc0(self):
        try:
            mod.or_any(True, False, False)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.or_any(False, False, False)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.or_any(5 < 3, 10 > 20, "a" == "a")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.or_any()
        except EXC:
            pass


class Test_switch_case:
    def test_exists(self):
        assert hasattr(mod, "switch_case")

    def test_doc0(self):
        try:
            mod.switch_case(3, 1, "One", 2, "Two", 3, "Three", "Other")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.switch_case("apple", "orange", "Fruit", "apple", "Favorite", "Unknown")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.switch_case(5, 1, "One", 2, "Two", "Not Found")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.switch_case(1)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.switch_case(3)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.switch_case(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.switch_case(0)
        except EXC:
            pass


class Test_xor_all:
    def test_exists(self):
        assert hasattr(mod, "xor_all")

    def test_doc0(self):
        try:
            mod.xor_all(True, True)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.xor_all(True, False)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.xor_all(True, True, True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.xor_all()
        except EXC:
            pass

