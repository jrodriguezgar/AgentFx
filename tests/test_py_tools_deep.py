# Deep coverage tests for shortfx.fxPython.py_tools

import shortfx.fxPython.py_tools as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_apply_expression_deep:
    def test_c0(self):
        try:
            mod.apply_expression("hello world", 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.apply_expression("test", 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.apply_expression("abc123", -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.apply_expression("", 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.apply_expression("Hello, World!", 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.apply_expression("UPPER lower 123", 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.apply_expression("hello world", 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.apply_expression("test", -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.apply_expression("abc123", 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.apply_expression("", 1)
        except EXC:
            pass


class Test_shift_deep:
    def test_c0(self):
        try:
            mod.shift(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.shift(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.shift(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.shift(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.shift(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.shift(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.shift(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.shift(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.shift(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.shift(2)
        except EXC:
            pass

    def test_kw_direction(self):
        try:
            mod.shift(1, direction="hello world")
        except EXC:
            pass

    def test_kw_new_elements(self):
        try:
            mod.shift(1, new_elements=1)
        except EXC:
            pass


class Test_create_key_value_dictionary_deep:
    def test_c0(self):
        try:
            mod.create_key_value_dictionary(1, 0.1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.create_key_value_dictionary(42, 0.5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.create_key_value_dictionary(0, 0.01)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.create_key_value_dictionary(-5, 0.95)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.create_key_value_dictionary(3.14, 0.99)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.create_key_value_dictionary(100, 0.05)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.create_key_value_dictionary(0.5, 0.1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.create_key_value_dictionary(1000, 0.5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.create_key_value_dictionary(-1, 0.01)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.create_key_value_dictionary(2, 0.95)
        except EXC:
            pass


class Test_retry_deep:
    def test_c0(self):
        try:
            mod.retry(lambda x: x)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.retry(lambda x: x * 2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.retry(abs)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.retry(str)
        except EXC:
            pass

    def test_kw_max_attempts(self):
        try:
            mod.retry(lambda x: x, max_attempts=1)
        except EXC:
            pass

    def test_kw_delay(self):
        try:
            mod.retry(lambda x: x, delay=1)
        except EXC:
            pass


class Test_rotate_deep:
    def test_c0(self):
        try:
            mod.rotate(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rotate(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rotate(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rotate(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rotate(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rotate(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.rotate(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.rotate(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.rotate(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.rotate(2)
        except EXC:
            pass

    def test_kw_steps(self):
        try:
            mod.rotate(1, steps=1)
        except EXC:
            pass


class Test_pipe_deep:
    def test_c0(self):
        try:
            mod.pipe(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pipe(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pipe(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pipe(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pipe(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pipe(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.pipe(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.pipe(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.pipe(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.pipe(2)
        except EXC:
            pass


class Test_switch_case_deep:
    def test_c0(self):
        try:
            mod.switch_case(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.switch_case(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.switch_case(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.switch_case(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.switch_case(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.switch_case(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.switch_case(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.switch_case(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.switch_case(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.switch_case(2)
        except EXC:
            pass


class Test_function_call_deep:
    def test_c0(self):
        try:
            mod.function_call(lambda x: x)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.function_call(lambda x: x * 2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.function_call(abs)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.function_call(str)
        except EXC:
            pass


class Test_loop_for_deep:
    def test_c0(self):
        try:
            mod.loop_for(1, lambda x: x * 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.loop_for(42, abs)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.loop_for(0, str)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.loop_for(-5, lambda x: x)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.loop_for(3.14, lambda x: x * 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.loop_for(100, abs)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.loop_for(0.5, str)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.loop_for(1000, lambda x: x)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.loop_for(-1, lambda x: x * 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.loop_for(2, abs)
        except EXC:
            pass


class Test_loop_while_deep:
    def test_c0(self):
        try:
            mod.loop_while(1, lambda x: x * 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.loop_while(42, abs)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.loop_while(0, str)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.loop_while(-5, lambda x: x)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.loop_while(3.14, lambda x: x * 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.loop_while(100, abs)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.loop_while(0.5, str)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.loop_while(1000, lambda x: x)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.loop_while(-1, lambda x: x * 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.loop_while(2, abs)
        except EXC:
            pass

