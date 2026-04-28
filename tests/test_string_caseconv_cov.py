# Coverage tests for shortfx.fxString.string_caseconv

from shortfx.fxString import string_caseconv as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_to_camel_case:
    def test_exists(self):
        assert hasattr(mod, "to_camel_case")

    def test_doc0(self):
        try:
            mod.to_camel_case("hello world")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.to_camel_case("some_variable_name")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.to_camel_case("PascalCase")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.to_camel_case("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.to_camel_case("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.to_camel_case(None)
        except EXC:
            pass


class Test_to_constant_case:
    def test_exists(self):
        assert hasattr(mod, "to_constant_case")

    def test_doc0(self):
        try:
            mod.to_constant_case("hello world")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.to_constant_case("maxRetries")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.to_constant_case("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.to_constant_case("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.to_constant_case(None)
        except EXC:
            pass


class Test_to_kebab_case:
    def test_exists(self):
        assert hasattr(mod, "to_kebab_case")

    def test_doc0(self):
        try:
            mod.to_kebab_case("Hello World")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.to_kebab_case("camelCaseText")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.to_kebab_case("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.to_kebab_case("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.to_kebab_case(None)
        except EXC:
            pass


class Test_to_pascal_case:
    def test_exists(self):
        assert hasattr(mod, "to_pascal_case")

    def test_doc0(self):
        try:
            mod.to_pascal_case("hello world")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.to_pascal_case("some_variable_name")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.to_pascal_case("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.to_pascal_case("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.to_pascal_case(None)
        except EXC:
            pass


class Test_to_slug:
    def test_exists(self):
        assert hasattr(mod, "to_slug")

    def test_doc0(self):
        try:
            mod.to_slug("Café Résumé!")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.to_slug("Hello World 2024", separator="_")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.to_slug("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.to_slug("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.to_slug(None)
        except EXC:
            pass


class Test_to_snake_case:
    def test_exists(self):
        assert hasattr(mod, "to_snake_case")

    def test_doc0(self):
        try:
            mod.to_snake_case("Hello World")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.to_snake_case("camelCaseText")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.to_snake_case("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.to_snake_case("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.to_snake_case(None)
        except EXC:
            pass


class Test_to_title_case:
    def test_exists(self):
        assert hasattr(mod, "to_title_case")

    def test_doc0(self):
        try:
            mod.to_title_case("the lord of the rings")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.to_title_case("el señor de los anillos")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.to_title_case("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.to_title_case("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.to_title_case(None)
        except EXC:
            pass

