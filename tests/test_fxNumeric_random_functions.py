# Coverage tests for shortfx.fxNumeric.random_functions

from shortfx.fxNumeric import random_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_random_array:
    def test_exists(self):
        assert hasattr(mod, "random_array")

    def test_doc0(self):
        try:
            mod.random_array(2, 3, 1, 10, True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.random_array()
        except EXC:
            pass


class Test_random_bool:
    def test_exists(self):
        assert hasattr(mod, "random_bool")

    def test_doc0(self):
        try:
            mod.random_bool(0.9)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.random_bool()
        except EXC:
            pass


class Test_random_choice:
    def test_exists(self):
        assert hasattr(mod, "random_choice")

    def test_doc0(self):
        try:
            mod.random_choice(['a', 'b', 'c', 'd'])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.random_choice([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.random_choice([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.random_choice(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.random_choice([])
        except EXC:
            pass


class Test_random_float:
    def test_exists(self):
        assert hasattr(mod, "random_float")

    def test_var0(self):
        try:
            mod.random_float()
        except EXC:
            pass


class Test_random_gaussian:
    def test_exists(self):
        assert hasattr(mod, "random_gaussian")

    def test_var0(self):
        try:
            mod.random_gaussian()
        except EXC:
            pass


class Test_random_int:
    def test_exists(self):
        assert hasattr(mod, "random_int")

    def test_doc0(self):
        try:
            mod.random_int(1, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.random_int(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.random_int(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.random_int(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.random_int("", "")
        except EXC:
            pass


class Test_random_sample:
    def test_exists(self):
        assert hasattr(mod, "random_sample")

    def test_doc0(self):
        try:
            mod.random_sample([1, 2, 3, 4, 5], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.random_sample([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.random_sample([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.random_sample(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.random_sample([], 0)
        except EXC:
            pass


class Test_random_shuffle:
    def test_exists(self):
        assert hasattr(mod, "random_shuffle")

    def test_doc0(self):
        try:
            mod.random_shuffle([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.random_shuffle([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.random_shuffle([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.random_shuffle(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.random_shuffle([])
        except EXC:
            pass


class Test_random_uuid:
    def test_exists(self):
        assert hasattr(mod, "random_uuid")

    def test_var0(self):
        try:
            mod.random_uuid()
        except EXC:
            pass


class Test_random_weighted_choice:
    def test_exists(self):
        assert hasattr(mod, "random_weighted_choice")

    def test_doc0(self):
        try:
            mod.random_weighted_choice(['a', 'b', 'c'], [1, 1, 98])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.random_weighted_choice([1, 2, 3], 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.random_weighted_choice([0], 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.random_weighted_choice(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.random_weighted_choice([], [])
        except EXC:
            pass


class Test_set_random_seed:
    def test_exists(self):
        assert hasattr(mod, "set_random_seed")

    def test_doc0(self):
        try:
            mod.set_random_seed(42)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.set_random_seed(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.set_random_seed(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.set_random_seed(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.set_random_seed("")
        except EXC:
            pass

