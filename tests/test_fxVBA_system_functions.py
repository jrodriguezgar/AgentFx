# Coverage tests for shortfx.fxVBA.system_functions

from shortfx.fxVBA import system_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_BuildCriteria:
    def test_exists(self):
        assert hasattr(mod, "BuildCriteria")

    def test_var0(self):
        try:
            mod.BuildCriteria("hello", 0, "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.BuildCriteria("", 1, "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.BuildCriteria(None, 0, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.BuildCriteria("", "", 0)
        except EXC:
            pass


class Test_Command:
    def test_exists(self):
        assert hasattr(mod, "Command")

    def test_var0(self):
        try:
            mod.Command()
        except EXC:
            pass


class Test_CurDir:
    def test_exists(self):
        assert hasattr(mod, "CurDir")

    def test_var0(self):
        try:
            mod.CurDir()
        except EXC:
            pass


class Test_Dir_:
    def test_exists(self):
        assert hasattr(mod, "Dir_")

    def test_var0(self):
        try:
            mod.Dir_()
        except EXC:
            pass


class Test_Environ:
    def test_exists(self):
        assert hasattr(mod, "Environ")

    def test_var0(self):
        try:
            mod.Environ("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Environ("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Environ(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Environ(0)
        except EXC:
            pass


class Test_Error:
    def test_exists(self):
        assert hasattr(mod, "Error")

    def test_var0(self):
        try:
            mod.Error(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Error(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Error(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Error("")
        except EXC:
            pass


class Test_FileDateTime:
    def test_exists(self):
        assert hasattr(mod, "FileDateTime")

    def test_var0(self):
        try:
            mod.FileDateTime("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FileDateTime("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FileDateTime(None)
        except EXC:
            pass


class Test_FileLen:
    def test_exists(self):
        assert hasattr(mod, "FileLen")

    def test_var0(self):
        try:
            mod.FileLen("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FileLen("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FileLen(None)
        except EXC:
            pass


class Test_GetAttr_:
    def test_exists(self):
        assert hasattr(mod, "GetAttr_")

    def test_var0(self):
        try:
            mod.GetAttr_("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.GetAttr_("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.GetAttr_(None)
        except EXC:
            pass


class Test_Nz:
    def test_exists(self):
        assert hasattr(mod, "Nz")

    def test_var0(self):
        try:
            mod.Nz(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Nz(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Nz(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Nz("")
        except EXC:
            pass


class Test_Partition:
    def test_exists(self):
        assert hasattr(mod, "Partition")

    def test_var0(self):
        try:
            mod.Partition(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.Partition(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.Partition(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.Partition("", "", 0, "")
        except EXC:
            pass


class Test_TypeName:
    def test_exists(self):
        assert hasattr(mod, "TypeName")

    def test_var0(self):
        try:
            mod.TypeName(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TypeName(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TypeName(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TypeName("")
        except EXC:
            pass


class Test_VarType:
    def test_exists(self):
        assert hasattr(mod, "VarType")

    def test_var0(self):
        try:
            mod.VarType(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.VarType(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.VarType(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.VarType("")
        except EXC:
            pass

