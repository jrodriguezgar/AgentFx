"""Safe scientific expression evaluator.

Evaluates mathematical expressions from string input using AST-based
parsing. NEVER uses ``eval()`` — instead, it parses the expression into
an Abstract Syntax Tree and walks it, only allowing whitelisted
mathematical operations and functions.

Key Features:
    - Safe evaluation without ``eval()`` or ``exec()``
    - Supports arithmetic operators: +, -, *, /, //, %, **
    - Supports unary operators: +, -
    - Built-in scientific functions: sin, cos, tan, log, sqrt, etc.
    - Built-in constants: pi, e, tau, phi, inf
    - Parenthesized sub-expressions
    - Clear error messages for invalid input

Example:
    >>> from shortfx.fxNumeric.calculator_functions import evaluate_expression
    >>> evaluate_expression("sin(pi/4) + sqrt(2)")
    3.1213203435596424
    >>> evaluate_expression("log(100, 10)")
    2.0
"""

import ast
import math
import operator
from typing import Any, Union

from shortfx.fxNumeric.constants_functions import (
    PI, E, TAU, PHI, INF, NAN, SQRT2, SQRT3, LN2, LN10,
)

_MAX_FACTORIAL = 170  # math.factorial(171) overflows float


def _safe_factorial(n: int) -> int:
    """Factorial with input-size guard to prevent DoS.

    Args:
        n: Non-negative integer.

    Returns:
        int: n!

    Raises:
        ValueError: If *n* exceeds ``_MAX_FACTORIAL``.

    Complexity: O(n)
    """
    if n > _MAX_FACTORIAL:
        raise ValueError(
            f"factorial argument {n} exceeds maximum ({_MAX_FACTORIAL})."
        )
    return math.factorial(n)


# ── Allowed Functions ───────────────────────────────────────────────────────

_FUNCTIONS: dict[str, Any] = {
    # Trigonometric
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "atan2": math.atan2,
    # Hyperbolic
    "sinh": math.sinh,
    "cosh": math.cosh,
    "tanh": math.tanh,
    "asinh": math.asinh,
    "acosh": math.acosh,
    "atanh": math.atanh,
    # Logarithmic
    "log": math.log,
    "log2": math.log2,
    "log10": math.log10,
    "log1p": math.log1p,
    "ln": math.log,
    # Exponential
    "exp": math.exp,
    "expm1": math.expm1,
    # Power / roots
    "sqrt": math.sqrt,
    "cbrt": getattr(math, "cbrt", lambda x: x ** (1 / 3)),
    "pow": math.pow,
    # Rounding
    "ceil": math.ceil,
    "floor": math.floor,
    "trunc": math.trunc,
    "round": round,
    # Absolute / sign
    "abs": abs,
    "fabs": math.fabs,
    # Combinatorics
    "factorial": _safe_factorial,
    "comb": math.comb,
    "perm": math.perm,
    "gcd": math.gcd,
    "lcm": math.lcm,
    # Special
    "gamma": math.gamma,
    "lgamma": math.lgamma,
    "erf": math.erf,
    "erfc": math.erfc,
    # Utility
    "degrees": math.degrees,
    "radians": math.radians,
    "hypot": math.hypot,
    "fmod": math.fmod,
    "copysign": math.copysign,
    "remainder": math.remainder,
    "isfinite": math.isfinite,
    "isinf": math.isinf,
    "isnan": math.isnan,
    # Aggregation (multi-arg)
    "max": max,
    "min": min,
    "sum": sum,
}

# ── Allowed Constants ───────────────────────────────────────────────────────

_CONSTANTS: dict[str, float] = {
    "pi": PI,
    "e": E,
    "tau": TAU,
    "phi": PHI,
    "inf": INF,
    "nan": NAN,
    "sqrt2": SQRT2,
    "sqrt3": SQRT3,
    "ln2": LN2,
    "ln10": LN10,
}

# ── Binary Operators ────────────────────────────────────────────────────────

_BINARY_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_UNARY_OPS = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}

# Maximum expression length to prevent DoS
_MAX_EXPRESSION_LENGTH = 1000
_MAX_POWER = 10000


def _safe_power(base: Union[int, float], exponent: Union[int, float]) -> float:
    """Power operator with overflow protection.

    Args:
        base: The base value.
        exponent: The exponent value.

    Returns:
        float: The result of base ** exponent.

    Raises:
        ValueError: If the exponent is unreasonably large.

    Complexity: O(1)
    """
    if isinstance(exponent, (int, float)) and abs(exponent) > _MAX_POWER:
        raise ValueError(
            f"Exponent {exponent} exceeds maximum allowed ({_MAX_POWER})."
        )

    return operator.pow(base, exponent)


class _ExpressionEvaluator(ast.NodeVisitor):
    """AST-based safe evaluator for mathematical expressions.

    Walks the parsed AST and only evaluates whitelisted operations.
    All other node types raise a ValueError.

    Complexity: O(n) where n is the number of AST nodes.
    """

    def visit(self, node: ast.AST) -> Any:
        """Dispatch to the appropriate visit method.

        Args:
            node: An AST node.

        Returns:
            The evaluated result.

        Raises:
            ValueError: If the node type is not supported.
        """
        return super().visit(node)

    def visit_Expression(self, node: ast.Expression) -> Any:
        return self.visit(node.body)

    def visit_Constant(self, node: ast.Constant) -> Union[int, float]:

        if isinstance(node.value, (int, float)):
            return node.value

        raise ValueError(f"Unsupported constant type: {type(node.value).__name__}")

    def visit_Name(self, node: ast.Name) -> float:
        name = node.id.lower()

        if name in _CONSTANTS:
            return _CONSTANTS[name]

        raise ValueError(
            f"Unknown variable '{node.id}'. "
            f"Available constants: {', '.join(sorted(_CONSTANTS.keys()))}"
        )

    def visit_BinOp(self, node: ast.BinOp) -> Union[int, float]:
        left = self.visit(node.left)
        right = self.visit(node.right)
        op_type = type(node.op)

        if op_type == ast.Pow:
            return _safe_power(left, right)

        if op_type not in _BINARY_OPS:
            raise ValueError(f"Unsupported operator: {op_type.__name__}")

        return _BINARY_OPS[op_type](left, right)

    def visit_UnaryOp(self, node: ast.UnaryOp) -> Union[int, float]:
        operand = self.visit(node.operand)
        op_type = type(node.op)

        if op_type not in _UNARY_OPS:
            raise ValueError(f"Unsupported unary operator: {op_type.__name__}")

        return _UNARY_OPS[op_type](operand)

    def visit_Call(self, node: ast.Call) -> Any:

        if not isinstance(node.func, ast.Name):
            raise ValueError("Only direct function calls are allowed (e.g. sin(x)).")

        func_name = node.func.id.lower()

        if func_name not in _FUNCTIONS:
            raise ValueError(
                f"Unknown function '{node.func.id}'. "
                f"Available: {', '.join(sorted(_FUNCTIONS.keys()))}"
            )

        # Keyword arguments not allowed
        if node.keywords:
            raise ValueError("Keyword arguments are not supported in expressions.")

        args = [self.visit(arg) for arg in node.args]
        func = _FUNCTIONS[func_name]

        return func(*args)

    def visit_List(self, node: ast.List) -> list:
        # Allow list literals for functions like max([1,2,3])
        return [self.visit(el) for el in node.elts]

    def visit_Tuple(self, node: ast.Tuple) -> tuple:
        return tuple(self.visit(el) for el in node.elts)

    def generic_visit(self, node: ast.AST) -> None:
        raise ValueError(
            f"Unsupported expression element: {type(node).__name__}. "
            "Only arithmetic operations and math functions are allowed."
        )


def evaluate_expression(expression: str) -> Union[int, float]:
    """Safely evaluates a mathematical expression from a string.

    Description:
        Parses and evaluates a mathematical expression using AST-based
        parsing. Supports arithmetic operators, scientific functions,
        and mathematical constants. Does NOT use ``eval()`` — only
        whitelisted operations are allowed.

    Args:
        expression (str): A mathematical expression string.
            Examples: "sin(pi/4) + sqrt(2)", "log(100, 10)", "2**10 + 1"

    Returns:
        Union[int, float]: The numeric result of the expression.

    Raises:
        TypeError: If expression is not a string.
        ValueError: If the expression is empty, too long, contains syntax
            errors, or uses unsupported operations.

    Usage Example:
        >>> from shortfx.fxNumeric.calculator_functions import evaluate_expression
        >>> evaluate_expression("2 + 3 * 4")
        14
        >>> evaluate_expression("sin(pi/2)")
        1.0
        >>> evaluate_expression("sqrt(2) ** 2")
        2.0000000000000004
        >>> evaluate_expression("log(1000, 10)")
        2.9999999999999996
        >>> evaluate_expression("factorial(5)")
        120
        >>> evaluate_expression("comb(10, 3)")
        120

    Cost: O(n) where n is the expression length.
    """
    if not isinstance(expression, str):
        raise TypeError("Expression must be a string.")

    expression = expression.strip()

    if not expression:
        raise ValueError("Expression cannot be empty.")

    if len(expression) > _MAX_EXPRESSION_LENGTH:
        raise ValueError(
            f"Expression too long ({len(expression)} chars). "
            f"Maximum allowed: {_MAX_EXPRESSION_LENGTH}."
        )

    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as exc:
        raise ValueError(f"Invalid expression syntax: {exc.msg}") from exc

    evaluator = _ExpressionEvaluator()
    return evaluator.visit(tree)


def list_available_functions() -> list[str]:
    """Lists all functions available in the expression evaluator.

    Description:
        Returns the names of all mathematical functions that can be
        used inside ``evaluate_expression()``.

    Returns:
        list[str]: Sorted list of available function names.

    Usage Example:
        >>> from shortfx.fxNumeric.calculator_functions import list_available_functions
        >>> "sin" in list_available_functions()
        True

    Cost: O(n log n)
    """
    return sorted(_FUNCTIONS.keys())


def list_available_constants() -> list[str]:
    """Lists all constants available in the expression evaluator.

    Description:
        Returns the names of all mathematical constants that can be
        used inside ``evaluate_expression()``.

    Returns:
        list[str]: Sorted list of available constant names.

    Usage Example:
        >>> from shortfx.fxNumeric.calculator_functions import list_available_constants
        >>> "pi" in list_available_constants()
        True

    Cost: O(n log n)
    """
    return sorted(_CONSTANTS.keys())
