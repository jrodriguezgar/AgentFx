"""Tests for fxNumeric.calculator_functions."""

import math

import pytest

from agentfx.fxNumeric.calculator_functions import evaluate_expression, list_available_constants, list_available_functions


class TestEvaluateExpression:

    # Arithmetic
    @pytest.mark.parametrize("expr, expected", [
        ("2 + 3", 5),
        ("10 - 4", 6),
        ("3 * 7", 21),
        ("15 / 4", 3.75),
        ("15 // 4", 3),
        ("17 % 5", 2),
        ("2 ** 10", 1024),
        ("-5 + 3", -2),
        ("(2 + 3) * 4", 20),
    ])
    def test_arithmetic(self, expr: str, expected):
        assert evaluate_expression(expr) == pytest.approx(expected)

    # Functions
    def test_sin_pi_half(self):
        result = evaluate_expression("sin(pi / 2)")
        assert result == pytest.approx(1.0)

    def test_cos_zero(self):
        result = evaluate_expression("cos(0)")
        assert result == pytest.approx(1.0)

    def test_sqrt(self):
        result = evaluate_expression("sqrt(144)")
        assert result == pytest.approx(12.0)

    def test_log_base_10(self):
        result = evaluate_expression("log(100, 10)")
        assert result == pytest.approx(2.0)

    def test_log10(self):
        result = evaluate_expression("log10(1000)")
        assert result == pytest.approx(3.0)

    def test_factorial_expr(self):
        result = evaluate_expression("factorial(5)")
        assert result == 120

    def test_comb_expr(self):
        result = evaluate_expression("comb(10, 3)")
        assert result == 120

    def test_complex_expression(self):
        # sin²(pi/6) + cos²(pi/6) should ≈ 1
        result = evaluate_expression("sin(pi/6)**2 + cos(pi/6)**2")
        assert result == pytest.approx(1.0)

    def test_nested_functions(self):
        result = evaluate_expression("sqrt(abs(-16))")
        assert result == pytest.approx(4.0)

    # Constants
    def test_pi_constant(self):
        result = evaluate_expression("pi")
        assert result == pytest.approx(math.pi)

    def test_e_constant(self):
        result = evaluate_expression("e")
        assert result == pytest.approx(math.e)

    # Error handling
    def test_empty_expression_raises(self):

        with pytest.raises(ValueError):
            evaluate_expression("")

    def test_syntax_error_raises(self):

        with pytest.raises(ValueError):
            evaluate_expression("2 +* 3")

    def test_unknown_function_raises(self):

        with pytest.raises(ValueError):
            evaluate_expression("foo(42)")

    def test_unknown_variable_raises(self):

        with pytest.raises(ValueError):
            evaluate_expression("x + 1")

    def test_non_string_raises(self):

        with pytest.raises(TypeError):
            evaluate_expression(42)

    def test_too_large_exponent_raises(self):

        with pytest.raises(ValueError):
            evaluate_expression("2 ** 100000")

    # Utility listings
    def test_list_available_functions(self):
        funcs = list_available_functions()
        assert "sin" in funcs
        assert "sqrt" in funcs
        assert "factorial" in funcs

    def test_list_available_constants(self):
        consts = list_available_constants()
        assert "pi" in consts
        assert "e" in consts
