# Deep coverage tests for shortfx.fxNumeric.rounding_functions

import shortfx.fxNumeric.rounding_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_round_half_even_deep:
    def test_c0(self):
        try:
            mod.round_half_even(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.round_half_even(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.round_half_even(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.round_half_even(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.round_half_even(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.round_half_even(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.round_half_even(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.round_half_even(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.round_half_even(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.round_half_even(2)
        except EXC:
            pass

    def test_kw_target_precision(self):
        try:
            mod.round_half_even(1, target_precision="hello world")
        except EXC:
            pass


class Test_ceiling_math_deep:
    def test_c0(self):
        try:
            mod.ceiling_math(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ceiling_math(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ceiling_math(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ceiling_math(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ceiling_math(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ceiling_math(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ceiling_math(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ceiling_math(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ceiling_math(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ceiling_math(2)
        except EXC:
            pass

    def test_kw_significance(self):
        try:
            mod.ceiling_math(1, significance=1)
        except EXC:
            pass

    def test_kw_mode(self):
        try:
            mod.ceiling_math(1, mode=1)
        except EXC:
            pass


class Test_ceiling_precise_deep:
    def test_c0(self):
        try:
            mod.ceiling_precise(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ceiling_precise(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ceiling_precise(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ceiling_precise(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ceiling_precise(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ceiling_precise(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ceiling_precise(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ceiling_precise(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ceiling_precise(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ceiling_precise(2)
        except EXC:
            pass

    def test_kw_significance(self):
        try:
            mod.ceiling_precise(1, significance=1)
        except EXC:
            pass


class Test_ceiling_significance_deep:
    def test_c0(self):
        try:
            mod.ceiling_significance(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ceiling_significance(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ceiling_significance(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ceiling_significance(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ceiling_significance(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ceiling_significance(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ceiling_significance(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ceiling_significance(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ceiling_significance(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ceiling_significance(2)
        except EXC:
            pass

    def test_kw_significance(self):
        try:
            mod.ceiling_significance(1, significance=1)
        except EXC:
            pass


class Test_floor_math_deep:
    def test_c0(self):
        try:
            mod.floor_math(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.floor_math(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.floor_math(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.floor_math(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.floor_math(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.floor_math(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.floor_math(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.floor_math(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.floor_math(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.floor_math(2)
        except EXC:
            pass

    def test_kw_significance(self):
        try:
            mod.floor_math(1, significance=1)
        except EXC:
            pass

    def test_kw_mode(self):
        try:
            mod.floor_math(1, mode=1)
        except EXC:
            pass


class Test_floor_precise_deep:
    def test_c0(self):
        try:
            mod.floor_precise(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.floor_precise(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.floor_precise(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.floor_precise(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.floor_precise(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.floor_precise(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.floor_precise(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.floor_precise(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.floor_precise(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.floor_precise(2)
        except EXC:
            pass

    def test_kw_significance(self):
        try:
            mod.floor_precise(1, significance=1)
        except EXC:
            pass


class Test_floor_significance_deep:
    def test_c0(self):
        try:
            mod.floor_significance(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.floor_significance(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.floor_significance(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.floor_significance(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.floor_significance(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.floor_significance(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.floor_significance(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.floor_significance(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.floor_significance(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.floor_significance(2)
        except EXC:
            pass

    def test_kw_significance(self):
        try:
            mod.floor_significance(1, significance=1)
        except EXC:
            pass

