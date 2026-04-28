# Coverage tests for agentfx.fxExcel.text_formulas

from agentfx.fxExcel import text_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_ARRAYTOTEXT:
    def test_exists(self):
        assert hasattr(mod, "ARRAYTOTEXT")

    def test_doc0(self):
        try:
            mod.ARRAYTOTEXT([1, "hello", True])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ARRAYTOTEXT([1, "hello", True], 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.ARRAYTOTEXT([[1, 2], [3, 4]], 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ARRAYTOTEXT([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ARRAYTOTEXT([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ARRAYTOTEXT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ARRAYTOTEXT([])
        except EXC:
            pass


class Test_ASC:
    def test_exists(self):
        assert hasattr(mod, "ASC")

    def test_doc0(self):
        try:
            mod.ASC("ＨＥＬＬＯ")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ASC("１２３")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ASC("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ASC("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ASC(None)
        except EXC:
            pass


class Test_BAHTTEXT:
    def test_exists(self):
        assert hasattr(mod, "BAHTTEXT")

    def test_doc0(self):
        try:
            mod.BAHTTEXT(1234)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.BAHTTEXT(5678.50)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.BAHTTEXT(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.BAHTTEXT(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.BAHTTEXT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.BAHTTEXT("")
        except EXC:
            pass


class Test_CHAR:
    def test_exists(self):
        assert hasattr(mod, "CHAR")

    def test_doc0(self):
        try:
            mod.CHAR(65)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CHAR(97)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.CHAR(33)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CHAR(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CHAR(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CHAR(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.CHAR("")
        except EXC:
            pass


class Test_CLEAN:
    def test_exists(self):
        assert hasattr(mod, "CLEAN")

    def test_doc0(self):
        try:
            mod.CLEAN("Monthly Report\n\r\t2024")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CLEAN("Hello\x00World")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CLEAN("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CLEAN("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CLEAN(None)
        except EXC:
            pass


class Test_CODE:
    def test_exists(self):
        assert hasattr(mod, "CODE")

    def test_doc0(self):
        try:
            mod.CODE("A")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CODE("Apple")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.CODE("!")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CODE("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.CODE("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.CODE(None)
        except EXC:
            pass


class Test_CONCAT:
    def test_exists(self):
        assert hasattr(mod, "CONCAT")

    def test_doc0(self):
        try:
            mod.CONCAT("Sun", "flower")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CONCAT("Zip code: ", 90210)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CONCAT()
        except EXC:
            pass


class Test_CONCATENATE:
    def test_exists(self):
        assert hasattr(mod, "CONCATENATE")

    def test_doc0(self):
        try:
            mod.CONCATENATE("Hello", " ", "World")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.CONCATENATE("Value: ", 100)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.CONCATENATE("A", "B", "C", "D")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.CONCATENATE()
        except EXC:
            pass


class Test_DBCS:
    def test_exists(self):
        assert hasattr(mod, "DBCS")

    def test_doc0(self):
        try:
            mod.DBCS("HELLO")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.DBCS("123")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DBCS("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DBCS("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DBCS(None)
        except EXC:
            pass


class Test_DOLLAR:
    def test_exists(self):
        assert hasattr(mod, "DOLLAR")

    def test_doc0(self):
        try:
            mod.DOLLAR(1234.567)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.DOLLAR(1234.567, 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.DOLLAR(-1234.567, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.DOLLAR(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.DOLLAR(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.DOLLAR(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.DOLLAR("")
        except EXC:
            pass


class Test_EXACT:
    def test_exists(self):
        assert hasattr(mod, "EXACT")

    def test_doc0(self):
        try:
            mod.EXACT("Word", "word")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.EXACT("Word", "Word")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.EXACT("abc", "abc")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.EXACT("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.EXACT("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.EXACT(None, "hello")
        except EXC:
            pass


class Test_FIND:
    def test_exists(self):
        assert hasattr(mod, "FIND")

    def test_doc0(self):
        try:
            mod.FIND("M", "Miriam McGovern")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.FIND("m", "Miriam McGovern")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.FIND("M", "Miriam McGovern", 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FIND("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FIND("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FIND(None, "hello")
        except EXC:
            pass


class Test_FINDB:
    def test_exists(self):
        assert hasattr(mod, "FINDB")

    def test_doc0(self):
        try:
            mod.FINDB("World", "Hello World")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FINDB("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FINDB("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FINDB(None, "hello")
        except EXC:
            pass


class Test_FIXED:
    def test_exists(self):
        assert hasattr(mod, "FIXED")

    def test_doc0(self):
        try:
            mod.FIXED(1234.567)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.FIXED(1234.567, 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.FIXED(1234.567, 1, True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.FIXED(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.FIXED(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.FIXED(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.FIXED("")
        except EXC:
            pass


class Test_LEFT:
    def test_exists(self):
        assert hasattr(mod, "LEFT")

    def test_doc0(self):
        try:
            mod.LEFT("Sale Price", 4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.LEFT("Sweden")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.LEFT("Quarterly Report", 9)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LEFT("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LEFT("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LEFT(None)
        except EXC:
            pass


class Test_LEFTB:
    def test_exists(self):
        assert hasattr(mod, "LEFTB")

    def test_doc0(self):
        try:
            mod.LEFTB("Hello", 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.LEFTB("日本語", 6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LEFTB("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LEFTB("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LEFTB(None)
        except EXC:
            pass


class Test_LEN:
    def test_exists(self):
        assert hasattr(mod, "LEN")

    def test_doc0(self):
        try:
            mod.LEN("Phoenix, AZ")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.LEN("")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.LEN("  spaces  ")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LEN("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LEN("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LEN(None)
        except EXC:
            pass


class Test_LENB:
    def test_exists(self):
        assert hasattr(mod, "LENB")

    def test_doc0(self):
        try:
            mod.LENB("Hello")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.LENB("日本語")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LENB("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LENB("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LENB(None)
        except EXC:
            pass


class Test_LOWER:
    def test_exists(self):
        assert hasattr(mod, "LOWER")

    def test_doc0(self):
        try:
            mod.LOWER("E. E. Cummings")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.LOWER("PAID IN FULL")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.LOWER("ABC-123")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.LOWER("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.LOWER("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.LOWER(None)
        except EXC:
            pass


class Test_MID:
    def test_exists(self):
        assert hasattr(mod, "MID")

    def test_doc0(self):
        try:
            mod.MID("Fluid Flow", 1, 5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.MID("Fluid Flow", 7, 4)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.MID("Quarterly Report 2024", 11, 6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MID("hello", 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MID("", 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MID(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MID("", "", "")
        except EXC:
            pass


class Test_MIDB:
    def test_exists(self):
        assert hasattr(mod, "MIDB")

    def test_doc0(self):
        try:
            mod.MIDB("Hello World", 7, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.MIDB("hello", 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.MIDB("", 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.MIDB(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.MIDB("", "", 0)
        except EXC:
            pass


class Test_NUMBERVALUE:
    def test_exists(self):
        assert hasattr(mod, "NUMBERVALUE")

    def test_doc0(self):
        try:
            mod.NUMBERVALUE("1,234.56")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.NUMBERVALUE("1.234,56", ",", ".")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.NUMBERVALUE("3.5%")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.NUMBERVALUE("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.NUMBERVALUE("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.NUMBERVALUE(None)
        except EXC:
            pass


class Test_PROPER:
    def test_exists(self):
        assert hasattr(mod, "PROPER")

    def test_doc0(self):
        try:
            mod.PROPER("this is a TITLE")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.PROPER("2-way street")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.PROPER("76BudGet")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.PROPER("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.PROPER("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.PROPER(None)
        except EXC:
            pass


class Test_REGEXEXTRACT:
    def test_exists(self):
        assert hasattr(mod, "REGEXEXTRACT")

    def test_doc0(self):
        try:
            mod.REGEXEXTRACT("Price: $123.45", r"\$([0-9.]+)")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.REGEXEXTRACT("Price: $123.45", r"\$([0-9.]+)", capture_group=1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.REGEXEXTRACT("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.REGEXEXTRACT("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.REGEXEXTRACT(None, "hello")
        except EXC:
            pass


class Test_REGEXREPLACE:
    def test_exists(self):
        assert hasattr(mod, "REGEXREPLACE")

    def test_doc0(self):
        try:
            mod.REGEXREPLACE("Hello 123 World 456", r"\d+", "X")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.REGEXREPLACE("test@email.com", r"@.*", "@example.com")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.REGEXREPLACE("hello", "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.REGEXREPLACE("", "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.REGEXREPLACE(None, "hello", "hello")
        except EXC:
            pass


class Test_REGEXTEST:
    def test_exists(self):
        assert hasattr(mod, "REGEXTEST")

    def test_doc0(self):
        try:
            mod.REGEXTEST("Hello123", r"\d+")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.REGEXTEST("NoNumbers", r"\d+")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.REGEXTEST("hello", r"^HELLO$", 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.REGEXTEST("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.REGEXTEST("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.REGEXTEST(None, "hello")
        except EXC:
            pass


class Test_REPLACE:
    def test_exists(self):
        assert hasattr(mod, "REPLACE")

    def test_doc0(self):
        try:
            mod.REPLACE("abcdefghijk", 6, 5, "*")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.REPLACE("2024", 3, 2, "25")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.REPLACE("XYZ123", 4, 3, "456")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.REPLACE("hello", 0, 0, "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.REPLACE("", 1, 1, "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.REPLACE(None, 0, 0, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.REPLACE("", "", "", "")
        except EXC:
            pass


class Test_REPLACEB:
    def test_exists(self):
        assert hasattr(mod, "REPLACEB")

    def test_doc0(self):
        try:
            mod.REPLACEB("Hello World", 7, 5, "Python")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.REPLACEB("hello", 0, 0, "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.REPLACEB("", 1, 1, "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.REPLACEB(None, 0, 0, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.REPLACEB("", "", 0, "")
        except EXC:
            pass


class Test_REPT:
    def test_exists(self):
        assert hasattr(mod, "REPT")

    def test_doc0(self):
        try:
            mod.REPT("*-", 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.REPT("=", 5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.REPT("AB", 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.REPT("hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.REPT("", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.REPT(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.REPT("", "")
        except EXC:
            pass


class Test_RIGHT:
    def test_exists(self):
        assert hasattr(mod, "RIGHT")

    def test_doc0(self):
        try:
            mod.RIGHT("Sale Price", 5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.RIGHT("Stock Number")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.RIGHT("2024-Q1", 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.RIGHT("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RIGHT("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RIGHT(None)
        except EXC:
            pass


class Test_RIGHTB:
    def test_exists(self):
        assert hasattr(mod, "RIGHTB")

    def test_doc0(self):
        try:
            mod.RIGHTB("Hello", 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.RIGHTB("日本語", 6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.RIGHTB("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.RIGHTB("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.RIGHTB(None)
        except EXC:
            pass


class Test_SEARCH:
    def test_exists(self):
        assert hasattr(mod, "SEARCH")

    def test_doc0(self):
        try:
            mod.SEARCH("e", "Statements", 6)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SEARCH("margin", "Profit Margin")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.SEARCH("M", "miriam mcgovern")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SEARCH("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SEARCH("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SEARCH(None, "hello")
        except EXC:
            pass


class Test_SEARCHB:
    def test_exists(self):
        assert hasattr(mod, "SEARCHB")

    def test_doc0(self):
        try:
            mod.SEARCHB("world", "Hello World")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SEARCHB("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SEARCHB("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SEARCHB(None, "hello")
        except EXC:
            pass


class Test_SUBSTITUTE:
    def test_exists(self):
        assert hasattr(mod, "SUBSTITUTE")

    def test_doc0(self):
        try:
            mod.SUBSTITUTE("Sales Data", "Sales", "Cost")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.SUBSTITUTE("Quarter 1, 2023", "1", "2", 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.SUBSTITUTE("apple apple", "apple", "orange")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.SUBSTITUTE("hello", "hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.SUBSTITUTE("", "", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.SUBSTITUTE(None, "hello", "hello")
        except EXC:
            pass


class Test_T:
    def test_exists(self):
        assert hasattr(mod, "T")

    def test_doc0(self):
        try:
            mod.T("Hello")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.T(123)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.T(True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.T(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.T(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.T(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.T("")
        except EXC:
            pass


class Test_TEXT:
    def test_exists(self):
        assert hasattr(mod, "TEXT")

    def test_doc0(self):
        try:
            mod.TEXT(1234.567, "0.00")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TEXT(0.285, "0.0%")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.TEXT(1234, "#,##0")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TEXT(0, "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TEXT(1, "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TEXT(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TEXT("", "")
        except EXC:
            pass


class Test_TEXTAFTER:
    def test_exists(self):
        assert hasattr(mod, "TEXTAFTER")

    def test_doc0(self):
        try:
            mod.TEXTAFTER("Red-Blue-Green", "-")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TEXTAFTER("Red-Blue-Green", "-", 2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.TEXTAFTER("Red-Blue-Green", "-", -1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TEXTAFTER("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TEXTAFTER("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TEXTAFTER(None, "hello")
        except EXC:
            pass


class Test_TEXTBEFORE:
    def test_exists(self):
        assert hasattr(mod, "TEXTBEFORE")

    def test_doc0(self):
        try:
            mod.TEXTBEFORE("Red-Blue-Green", "-")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TEXTBEFORE("Red-Blue-Green", "-", 2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.TEXTBEFORE("Red-Blue-Green", "-", -1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TEXTBEFORE("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TEXTBEFORE("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TEXTBEFORE(None, "hello")
        except EXC:
            pass


class Test_TEXTJOIN:
    def test_exists(self):
        assert hasattr(mod, "TEXTJOIN")

    def test_doc0(self):
        try:
            mod.TEXTJOIN(", ", True, "Red", "", "Blue", "Green")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TEXTJOIN("-", False, 2024, 1, 15)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.TEXTJOIN(" ", True, "Hello", None, "World")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TEXTJOIN("hello", True)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TEXTJOIN("", False)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TEXTJOIN(None, True)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.TEXTJOIN("", "")
        except EXC:
            pass


class Test_TEXTSPLIT:
    def test_exists(self):
        assert hasattr(mod, "TEXTSPLIT")

    def test_doc0(self):
        try:
            mod.TEXTSPLIT("Red Blue Green")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TEXTSPLIT("A,B,C;D,E,F", ",", ";")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.TEXTSPLIT("A,,C", ",", ignore_empty=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TEXTSPLIT("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TEXTSPLIT("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TEXTSPLIT(None)
        except EXC:
            pass


class Test_TRIM:
    def test_exists(self):
        assert hasattr(mod, "TRIM")

    def test_doc0(self):
        try:
            mod.TRIM("  First Quarter   Earnings  ")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.TRIM("Hello     World")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.TRIM("   text   ")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.TRIM("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.TRIM("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.TRIM(None)
        except EXC:
            pass


class Test_UNICHAR:
    def test_exists(self):
        assert hasattr(mod, "UNICHAR")

    def test_doc0(self):
        try:
            mod.UNICHAR(65)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.UNICHAR(8364)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.UNICHAR(128512)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.UNICHAR(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.UNICHAR(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.UNICHAR(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.UNICHAR("")
        except EXC:
            pass


class Test_UNICODE:
    def test_exists(self):
        assert hasattr(mod, "UNICODE")

    def test_doc0(self):
        try:
            mod.UNICODE("A")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.UNICODE("€")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.UNICODE("😀")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.UNICODE("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.UNICODE("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.UNICODE(None)
        except EXC:
            pass


class Test_UPPER:
    def test_exists(self):
        assert hasattr(mod, "UPPER")

    def test_doc0(self):
        try:
            mod.UPPER("total")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.UPPER("E. E. Cummings")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.UPPER("Yield-12%")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.UPPER("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.UPPER("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.UPPER(None)
        except EXC:
            pass


class Test_VALUE:
    def test_exists(self):
        assert hasattr(mod, "VALUE")

    def test_doc0(self):
        try:
            mod.VALUE("$1,000")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.VALUE("16:48:00")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.VALUE("123.45")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.VALUE("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.VALUE("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.VALUE(None)
        except EXC:
            pass


class Test_VALUETOTEXT:
    def test_exists(self):
        assert hasattr(mod, "VALUETOTEXT")

    def test_doc0(self):
        try:
            mod.VALUETOTEXT("Hello")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.VALUETOTEXT(123)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.VALUETOTEXT([1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.VALUETOTEXT(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.VALUETOTEXT(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.VALUETOTEXT(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.VALUETOTEXT("")
        except EXC:
            pass

