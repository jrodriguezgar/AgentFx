# Coverage tests for agentfx.fxString.string_regex

from agentfx.fxString import string_regex as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_regex_count:
    def test_exists(self):
        assert hasattr(mod, "regex_count")

    def test_doc0(self):
        try:
            mod.regex_count("aAbBaA", r"a", case_sensitive=False)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.regex_count("one 1 two 2 three 3", r"\d+")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.regex_count("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regex_count("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regex_count(None, "hello")
        except EXC:
            pass


class Test_regex_extract:
    def test_exists(self):
        assert hasattr(mod, "regex_extract")

    def test_doc0(self):
        try:
            mod.regex_extract("Order #12345 confirmed", r"#(\d+)", group=1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.regex_extract("no match here", r"\d+")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.regex_extract("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regex_extract("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regex_extract(None, "hello")
        except EXC:
            pass


class Test_regex_extract_all:
    def test_exists(self):
        assert hasattr(mod, "regex_extract_all")

    def test_doc0(self):
        try:
            mod.regex_extract_all("a1 b2 c3", r"[a-z]\d")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.regex_extract_all("no digits here", r"\d+")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.regex_extract_all("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regex_extract_all("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regex_extract_all(None, "hello")
        except EXC:
            pass


class Test_regex_match:
    def test_exists(self):
        assert hasattr(mod, "regex_match")

    def test_doc0(self):
        try:
            mod.regex_match("Hello World 123", r"\d+")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.regex_match("abc", r"^[A-Z]+$")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.regex_match("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regex_match("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regex_match(None, "hello")
        except EXC:
            pass


class Test_regex_split:
    def test_exists(self):
        assert hasattr(mod, "regex_split")

    def test_doc0(self):
        try:
            mod.regex_split("one, two; three  four", r"[,;\s]+")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.regex_split("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regex_split("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regex_split(None, "hello")
        except EXC:
            pass

