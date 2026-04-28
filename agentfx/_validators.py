"""Shared input-validation helpers for AgentFx modules.

Centralises repetitive ``isinstance`` / range-check patterns so every
module raises consistent error messages with minimal boilerplate.
"""

from typing import Any, Tuple, Type, Union


def ensure_type(
    value: Any,
    expected: Union[Type, Tuple[Type, ...]],
    name: str,
) -> None:
    """Raise ``TypeError`` when *value* is not an instance of *expected*.

    Args:
        value: The value to check.
        expected: Accepted type(s).
        name: Parameter name shown in the error message.

    Raises:
        TypeError: If *value* is not an instance of *expected*.

    Example:
        >>> ensure_type(3.14, (int, float), "rate")  # passes
        >>> ensure_type("x", (int, float), "rate")
        Traceback (most recent call last):
        ...
        TypeError: rate must be of type (int, float), got str

    Complexity: O(1)
    """
    if not isinstance(value, expected):
        exp_name = (
            expected.__name__
            if isinstance(expected, type)
            else ", ".join(t.__name__ for t in expected)
        )
        raise TypeError(
            f"{name} must be of type ({exp_name}), got {type(value).__name__}"
        )


def ensure_numeric(value: Any, name: str) -> None:
    """Raise ``TypeError`` when *value* is not ``int`` or ``float``.

    Args:
        value: The value to check.
        name: Parameter name shown in the error message.

    Raises:
        TypeError: If *value* is not numeric.

    Example:
        >>> ensure_numeric(42, "count")  # passes
        >>> ensure_numeric("x", "count")
        Traceback (most recent call last):
        ...
        TypeError: count must be numeric (int or float), got str

    Complexity: O(1)
    """
    if not isinstance(value, (int, float)):
        raise TypeError(
            f"{name} must be numeric (int or float), got {type(value).__name__}"
        )


def ensure_positive(value: Union[int, float], name: str) -> None:
    """Raise ``ValueError`` when *value* is not strictly positive.

    Args:
        value: The numeric value to check.
        name: Parameter name shown in the error message.

    Raises:
        ValueError: If *value* <= 0.

    Example:
        >>> ensure_positive(5, "life")  # passes
        >>> ensure_positive(0, "life")
        Traceback (most recent call last):
        ...
        ValueError: life must be positive, got 0

    Complexity: O(1)
    """
    if value <= 0:
        raise ValueError(f"{name} must be positive, got {value}")


def ensure_non_negative(value: Union[int, float], name: str) -> None:
    """Raise ``ValueError`` when *value* is negative.

    Args:
        value: The numeric value to check.
        name: Parameter name shown in the error message.

    Raises:
        ValueError: If *value* < 0.

    Example:
        >>> ensure_non_negative(0, "count")  # passes
        >>> ensure_non_negative(-1, "count")
        Traceback (most recent call last):
        ...
        ValueError: count must be non-negative, got -1

    Complexity: O(1)
    """
    if value < 0:
        raise ValueError(f"{name} must be non-negative, got {value}")


def ensure_not_empty(value: str, name: str) -> None:
    """Raise ``ValueError`` when *value* is an empty string.

    Args:
        value: The string to check.
        name: Parameter name shown in the error message.

    Raises:
        ValueError: If *value* is empty.

    Example:
        >>> ensure_not_empty("hello", "text")  # passes
        >>> ensure_not_empty("", "text")
        Traceback (most recent call last):
        ...
        ValueError: text must not be empty

    Complexity: O(1)
    """
    if not value:
        raise ValueError(f"{name} must not be empty")
