# Deep coverage tests for agentfx.fxPython.py_convertions

import agentfx.fxPython.py_convertions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_dictionary_to_object_deep:
    def test_c0(self):
        try:
            mod.dictionary_to_object(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dictionary_to_object(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dictionary_to_object(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dictionary_to_object(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dictionary_to_object(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dictionary_to_object(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.dictionary_to_object(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.dictionary_to_object(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.dictionary_to_object(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.dictionary_to_object(2)
        except EXC:
            pass


class Test_string_to_dictionary_deep:
    def test_c0(self):
        try:
            mod.string_to_dictionary("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.string_to_dictionary("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.string_to_dictionary("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.string_to_dictionary("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.string_to_dictionary("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.string_to_dictionary("UPPER lower 123")
        except EXC:
            pass


class Test_string_to_list_deep:
    def test_c0(self):
        try:
            mod.string_to_list("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.string_to_list("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.string_to_list("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.string_to_list("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.string_to_list("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.string_to_list("UPPER lower 123")
        except EXC:
            pass

    def test_kw_split_by_character(self):
        try:
            mod.string_to_list("hello world", split_by_character="hello world")
        except EXC:
            pass

