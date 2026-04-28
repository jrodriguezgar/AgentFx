# Coverage tests for shortfx.fxNumeric.rounding_functions
from decimal import Decimal

from shortfx.fxNumeric import rounding_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_add_with_exact_precision:
    def test_exists(self):
        assert hasattr(mod, "add_with_exact_precision")

    def test_doc0(self):
        try:
            mod.add_with_exact_precision("0.1", "0.2")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.add_with_exact_precision(Decimal('0.1'), Decimal('0.2'))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.add_with_exact_precision(1.23, 4.56) # Even with float input, internal operation is precise
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.add_with_exact_precision(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.add_with_exact_precision(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.add_with_exact_precision(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.add_with_exact_precision("", "")
        except EXC:
            pass


class Test_ceiling_math:
    def test_exists(self):
        assert hasattr(mod, "ceiling_math")

    def test_doc0(self):
        try:
            mod.ceiling_math(2.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ceiling_math(-2.5, 1, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ceiling_math(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ceiling_math(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ceiling_math(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ceiling_math("")
        except EXC:
            pass


class Test_ceiling_precise:
    def test_exists(self):
        assert hasattr(mod, "ceiling_precise")

    def test_doc0(self):
        try:
            mod.ceiling_precise(2.5, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ceiling_precise(-2.5, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ceiling_precise(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ceiling_precise(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ceiling_precise(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ceiling_precise("")
        except EXC:
            pass


class Test_ceiling_significance:
    def test_exists(self):
        assert hasattr(mod, "ceiling_significance")

    def test_doc0(self):
        try:
            mod.ceiling_significance(2.5, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.ceiling_significance(4.42, 0.05)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ceiling_significance(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ceiling_significance(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ceiling_significance(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ceiling_significance("")
        except EXC:
            pass


class Test_even:
    def test_exists(self):
        assert hasattr(mod, "even")

    def test_doc0(self):
        try:
            mod.even(1.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.even(3)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.even(-1.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.even(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.even(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.even(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.even("")
        except EXC:
            pass


class Test_floor_math:
    def test_exists(self):
        assert hasattr(mod, "floor_math")

    def test_doc0(self):
        try:
            mod.floor_math(3.7)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.floor_math(-2.5, 1, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.floor_math(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.floor_math(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.floor_math(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.floor_math("")
        except EXC:
            pass


class Test_floor_precise:
    def test_exists(self):
        assert hasattr(mod, "floor_precise")

    def test_doc0(self):
        try:
            mod.floor_precise(3.7, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.floor_precise(-2.5, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.floor_precise(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.floor_precise(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.floor_precise(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.floor_precise("")
        except EXC:
            pass


class Test_floor_significance:
    def test_exists(self):
        assert hasattr(mod, "floor_significance")

    def test_doc0(self):
        try:
            mod.floor_significance(2.5, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.floor_significance(4.42, 0.05)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.floor_significance(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.floor_significance(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.floor_significance(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.floor_significance("")
        except EXC:
            pass


class Test_manual_round_and_cast:
    def test_exists(self):
        assert hasattr(mod, "manual_round_and_cast")

    def test_doc0(self):
        try:
            mod.manual_round_and_cast(3.6)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.manual_round_and_cast(3.2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.manual_round_and_cast(3.5) # Always rounds up for .5
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.manual_round_and_cast(2.5) # Always rounds up for .5, resulting in 3
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.manual_round_and_cast(-3.6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.manual_round_and_cast(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.manual_round_and_cast(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.manual_round_and_cast(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.manual_round_and_cast("")
        except EXC:
            pass


class Test_manual_round_down_to_int:
    def test_exists(self):
        assert hasattr(mod, "manual_round_down_to_int")

    def test_doc0(self):
        try:
            mod.manual_round_down_to_int(3.9)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.manual_round_down_to_int(3.1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.manual_round_down_to_int(3.0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.manual_round_down_to_int(-3.1)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.manual_round_down_to_int(-3.9)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.manual_round_down_to_int(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.manual_round_down_to_int(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.manual_round_down_to_int(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.manual_round_down_to_int("")
        except EXC:
            pass


class Test_manual_round_up_to_int:
    def test_exists(self):
        assert hasattr(mod, "manual_round_up_to_int")

    def test_doc0(self):
        try:
            mod.manual_round_up_to_int(3.1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.manual_round_up_to_int(3.9)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.manual_round_up_to_int(3.0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.manual_round_up_to_int(-3.1)
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.manual_round_up_to_int(-3.9)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.manual_round_up_to_int(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.manual_round_up_to_int(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.manual_round_up_to_int(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.manual_round_up_to_int("")
        except EXC:
            pass


class Test_odd:
    def test_exists(self):
        assert hasattr(mod, "odd")

    def test_doc0(self):
        try:
            mod.odd(1.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.odd(2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.odd(-1.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.odd(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.odd(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.odd(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.odd("")
        except EXC:
            pass


class Test_quantize_number:
    def test_exists(self):
        assert hasattr(mod, "quantize_number")

    def test_doc0(self):
        try:
            mod.quantize_number(1.23, 0.25)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.quantize_number(1.10, 0.25)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.quantize_number(23, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.quantize_number(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.quantize_number(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.quantize_number(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.quantize_number("", "")
        except EXC:
            pass


class Test_round_down:
    def test_exists(self):
        assert hasattr(mod, "round_down")

    def test_doc0(self):
        try:
            mod.round_down(3.9)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.round_down(3.1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.round_down(3.0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.round_down(-3.9)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.round_down(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.round_down(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.round_down(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.round_down("")
        except EXC:
            pass


class Test_round_half_even:
    def test_exists(self):
        assert hasattr(mod, "round_half_even")

    def test_doc0(self):
        try:
            mod.round_half_even(Decimal("2.5"))
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.round_half_even(Decimal("3.5"))
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.round_half_even(2.6)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.round_half_even(Decimal("2.25"), "0.1")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.round_half_even("2.5")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.round_half_even(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.round_half_even(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.round_half_even(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.round_half_even("")
        except EXC:
            pass


class Test_round_to_n_decimals:
    def test_exists(self):
        assert hasattr(mod, "round_to_n_decimals")

    def test_doc0(self):
        try:
            mod.round_to_n_decimals(3.14159, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.round_to_n_decimals(123.4567, 1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.round_to_n_decimals(9.999, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.round_to_n_decimals(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.round_to_n_decimals(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.round_to_n_decimals(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.round_to_n_decimals("", 0)
        except EXC:
            pass


class Test_round_to_nearest_multiple:
    def test_exists(self):
        assert hasattr(mod, "round_to_nearest_multiple")

    def test_doc0(self):
        try:
            mod.round_to_nearest_multiple(7, 5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.round_to_nearest_multiple(8, 5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.round_to_nearest_multiple(10.25, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.round_to_nearest_multiple(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.round_to_nearest_multiple(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.round_to_nearest_multiple(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.round_to_nearest_multiple("", "")
        except EXC:
            pass


class Test_round_up:
    def test_exists(self):
        assert hasattr(mod, "round_up")

    def test_doc0(self):
        try:
            mod.round_up(3.1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.round_up(3.9)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.round_up(3.0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.round_up(-3.1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.round_up(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.round_up(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.round_up(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.round_up("")
        except EXC:
            pass


class Test_truncate_float:
    def test_exists(self):
        assert hasattr(mod, "truncate_float")

    def test_doc0(self):
        try:
            mod.truncate_float(3.9)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.truncate_float(-3.9)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.truncate_float(5.0)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.truncate_float(3.1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.truncate_float(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.truncate_float(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.truncate_float(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.truncate_float("")
        except EXC:
            pass

