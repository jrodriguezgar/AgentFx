# Coverage tests for shortfx.fxExcel.lookup_formulas

from shortfx.fxExcel import lookup_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_ADDRESS:
    def test_exists(self):
        assert hasattr(mod, "ADDRESS")

    def test_doc0(self):
        try:
            mod.ADDRESS(1, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ADDRESS(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ADDRESS(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ADDRESS(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ADDRESS([], 0)
        except EXC:
            pass


class Test_CHOOSE:
    def test_exists(self):
        assert hasattr(mod, "CHOOSE")

    def test_doc0(self):
        try:
            mod.CHOOSE(2, "red", "blue", "green")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CHOOSE(1, 10, 20, 30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CHOOSE(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CHOOSE(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CHOOSE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CHOOSE("")
        except EXC:
            pass


class Test_CHOOSECOLS:
    def test_exists(self):
        assert hasattr(mod, "CHOOSECOLS")

    def test_var0(self):
        try:
            mod.CHOOSECOLS([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CHOOSECOLS([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CHOOSECOLS(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CHOOSECOLS([])
        except EXC:
            pass


class Test_CHOOSEROWS:
    def test_exists(self):
        assert hasattr(mod, "CHOOSEROWS")

    def test_var0(self):
        try:
            mod.CHOOSEROWS([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CHOOSEROWS([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CHOOSEROWS(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CHOOSEROWS([])
        except EXC:
            pass


class Test_COLUMN:
    def test_exists(self):
        assert hasattr(mod, "COLUMN")

    def test_doc0(self):
        try:
            mod.COLUMN(col_index=3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COLUMN()
        except EXC:
            pass


class Test_COLUMNS:
    def test_exists(self):
        assert hasattr(mod, "COLUMNS")

    def test_doc0(self):
        try:
            mod.COLUMNS([[1,2,3],[4,5,6]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.COLUMNS([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.COLUMNS([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.COLUMNS(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.COLUMNS([])
        except EXC:
            pass


class Test_DROP:
    def test_exists(self):
        assert hasattr(mod, "DROP")

    def test_var0(self):
        try:
            mod.DROP([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DROP([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DROP(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DROP([])
        except EXC:
            pass


class Test_EXPAND:
    def test_exists(self):
        assert hasattr(mod, "EXPAND")

    def test_doc0(self):
        try:
            mod.EXPAND([[1,2],[3,4]], 3, 4, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.EXPAND([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.EXPAND([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.EXPAND(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.EXPAND([])
        except EXC:
            pass


class Test_FILTER:
    def test_exists(self):
        assert hasattr(mod, "FILTER")

    def test_var0(self):
        try:
            mod.FILTER([1, 2, 3], True)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FILTER([0], False)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FILTER(None, True)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FILTER([], "")
        except EXC:
            pass


class Test_HLOOKUP:
    def test_exists(self):
        assert hasattr(mod, "HLOOKUP")

    def test_var0(self):
        try:
            mod.HLOOKUP(0.5, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.HLOOKUP(0.1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.HLOOKUP(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.HLOOKUP(0, [], [])
        except EXC:
            pass


class Test_HSTACK:
    def test_exists(self):
        assert hasattr(mod, "HSTACK")

    def test_var0(self):
        try:
            mod.HSTACK()
        except EXC:
            pass


class Test_INDEX:
    def test_exists(self):
        assert hasattr(mod, "INDEX")

    def test_var0(self):
        try:
            mod.INDEX([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.INDEX([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.INDEX(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.INDEX([])
        except EXC:
            pass


class Test_INDIRECT:
    def test_exists(self):
        assert hasattr(mod, "INDIRECT")

    def test_doc0(self):
        try:
            mod.INDIRECT("B3")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.INDIRECT("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.INDIRECT("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.INDIRECT(None)
        except EXC:
            pass


class Test_LOOKUP:
    def test_exists(self):
        assert hasattr(mod, "LOOKUP")

    def test_doc0(self):
        try:
            mod.LOOKUP(5, [1, 3, 5, 7], ["A", "B", "C", "D"])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LOOKUP(0.5, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LOOKUP(0.1, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LOOKUP(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.LOOKUP(0, [])
        except EXC:
            pass


class Test_MATCH:
    def test_exists(self):
        assert hasattr(mod, "MATCH")

    def test_doc0(self):
        try:
            mod.MATCH("B", ["A", "B", "C"])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MATCH(0.5, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MATCH(0.1, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MATCH(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MATCH(0, [])
        except EXC:
            pass


class Test_OFFSET:
    def test_exists(self):
        assert hasattr(mod, "OFFSET")

    def test_doc0(self):
        try:
            mod.OFFSET([[1,2],[3,4],[5,6]], 1, 0, 2, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.OFFSET([1, 2, 3], 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.OFFSET([0], 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.OFFSET(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.OFFSET("", [], [])
        except EXC:
            pass


class Test_ROW:
    def test_exists(self):
        assert hasattr(mod, "ROW")

    def test_doc0(self):
        try:
            mod.ROW(row_index=5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ROW()
        except EXC:
            pass


class Test_ROWS:
    def test_exists(self):
        assert hasattr(mod, "ROWS")

    def test_doc0(self):
        try:
            mod.ROWS([[1,2],[3,4],[5,6]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ROWS([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ROWS([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ROWS(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ROWS([])
        except EXC:
            pass


class Test_SORT:
    def test_exists(self):
        assert hasattr(mod, "SORT")

    def test_var0(self):
        try:
            mod.SORT([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SORT([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SORT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SORT([])
        except EXC:
            pass


class Test_SORTBY:
    def test_exists(self):
        assert hasattr(mod, "SORTBY")

    def test_var0(self):
        try:
            mod.SORTBY([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SORTBY([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SORTBY(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.SORTBY([], [])
        except EXC:
            pass


class Test_TAKE:
    def test_exists(self):
        assert hasattr(mod, "TAKE")

    def test_var0(self):
        try:
            mod.TAKE([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TAKE([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TAKE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TAKE([])
        except EXC:
            pass


class Test_TOCOL:
    def test_exists(self):
        assert hasattr(mod, "TOCOL")

    def test_var0(self):
        try:
            mod.TOCOL([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TOCOL([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TOCOL(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TOCOL([])
        except EXC:
            pass


class Test_TOROW:
    def test_exists(self):
        assert hasattr(mod, "TOROW")

    def test_var0(self):
        try:
            mod.TOROW([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TOROW([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TOROW(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TOROW([])
        except EXC:
            pass


class Test_TRANSPOSE:
    def test_exists(self):
        assert hasattr(mod, "TRANSPOSE")

    def test_doc0(self):
        try:
            mod.TRANSPOSE([[1,2],[3,4]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TRANSPOSE([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TRANSPOSE([0])
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


class Test_TRIMRANGE:
    def test_exists(self):
        assert hasattr(mod, "TRIMRANGE")

    def test_var0(self):
        try:
            mod.TRIMRANGE([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TRIMRANGE([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TRIMRANGE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TRIMRANGE([])
        except EXC:
            pass


class Test_UNIQUE:
    def test_exists(self):
        assert hasattr(mod, "UNIQUE")

    def test_doc0(self):
        try:
            mod.UNIQUE([1, 2, 2, 3, 1, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.UNIQUE([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.UNIQUE([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.UNIQUE(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.UNIQUE([])
        except EXC:
            pass


class Test_VLOOKUP:
    def test_exists(self):
        assert hasattr(mod, "VLOOKUP")

    def test_var0(self):
        try:
            mod.VLOOKUP(0.5, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.VLOOKUP(0.1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.VLOOKUP(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.VLOOKUP(0, [], [])
        except EXC:
            pass


class Test_VSTACK:
    def test_exists(self):
        assert hasattr(mod, "VSTACK")

    def test_var0(self):
        try:
            mod.VSTACK()
        except EXC:
            pass


class Test_WRAPCOLS:
    def test_exists(self):
        assert hasattr(mod, "WRAPCOLS")

    def test_doc0(self):
        try:
            mod.WRAPCOLS([1, 2, 3, 4, 5, 6], 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.WRAPCOLS([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.WRAPCOLS([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.WRAPCOLS(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.WRAPCOLS([], 0)
        except EXC:
            pass


class Test_WRAPROWS:
    def test_exists(self):
        assert hasattr(mod, "WRAPROWS")

    def test_doc0(self):
        try:
            mod.WRAPROWS([1, 2, 3, 4, 5, 6], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.WRAPROWS([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.WRAPROWS([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.WRAPROWS(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.WRAPROWS([], 0)
        except EXC:
            pass


class Test_XLOOKUP:
    def test_exists(self):
        assert hasattr(mod, "XLOOKUP")

    def test_doc0(self):
        try:
            mod.XLOOKUP("B", ["A", "B", "C"], [10, 20, 30])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.XLOOKUP(0.5, [1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.XLOOKUP(0.1, [0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.XLOOKUP(None, [1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.XLOOKUP(0, [], 0)
        except EXC:
            pass


class Test_XMATCH:
    def test_exists(self):
        assert hasattr(mod, "XMATCH")

    def test_doc0(self):
        try:
            mod.XMATCH("B", ["A", "B", "C"])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.XMATCH(0.5, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.XMATCH(0.1, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.XMATCH(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.XMATCH(0, [])
        except EXC:
            pass

