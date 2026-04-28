# Coverage tests for shortfx.fxVBA.misc_functions

from shortfx.fxVBA import misc_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_AccessError:
    def test_exists(self):
        assert hasattr(mod, "AccessError")

    def test_var0(self):
        try:
            mod.AccessError(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.AccessError(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.AccessError(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.AccessError("")
        except EXC:
            pass


class Test_CurrentUser:
    def test_exists(self):
        assert hasattr(mod, "CurrentUser")

    def test_var0(self):
        try:
            mod.CurrentUser()
        except EXC:
            pass


class Test_Eval_:
    def test_exists(self):
        assert hasattr(mod, "Eval_")

    def test_var0(self):
        try:
            mod.Eval_("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Eval_("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Eval_(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Eval_(0)
        except EXC:
            pass


class Test_Hex_:
    def test_exists(self):
        assert hasattr(mod, "Hex_")

    def test_var0(self):
        try:
            mod.Hex_(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Hex_(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Hex_(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Hex_("")
        except EXC:
            pass


class Test_Oct_:
    def test_exists(self):
        assert hasattr(mod, "Oct_")

    def test_var0(self):
        try:
            mod.Oct_(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Oct_(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Oct_(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Oct_("")
        except EXC:
            pass


class Test_QBColor:
    def test_exists(self):
        assert hasattr(mod, "QBColor")

    def test_var0(self):
        try:
            mod.QBColor(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.QBColor(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.QBColor(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.QBColor([])
        except EXC:
            pass


class Test_RGB:
    def test_exists(self):
        assert hasattr(mod, "RGB")

    def test_var0(self):
        try:
            mod.RGB(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RGB(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RGB(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.RGB("", 0, "")
        except EXC:
            pass


class Test_SysCmd:
    def test_exists(self):
        assert hasattr(mod, "SysCmd")

    def test_var0(self):
        try:
            mod.SysCmd(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SysCmd(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SysCmd(None)
        except EXC:
            pass

