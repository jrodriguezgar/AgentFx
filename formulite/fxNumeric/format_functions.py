"""Format Functions Module.

Provides number formatting utilities, float comparison,
and percentage calculations.

Example:
    >>> from formulite.fxNumeric.format_functions import format_as_percentage
    >>> format_as_percentage(0.1234)
    '12.34%'
"""

import math


def format_with_leading_zeros(number: int, width: int) -> str:
    """Formats an integer as a string, padding with leading zeros to a specific width.

    Args:
        number (int): The integer to format.
        width (int): The desired total width of the resulting string.

    Returns:
        str: The number string with leading zeros.

    Example:
        >>> format_with_leading_zeros(5, 3)
        '005'
        >>> format_with_leading_zeros(123, 5)
        '00123'

    **Cost:** O(1), string formatting.
    """
    return format(number, f'0{width}')


def format_as_percentage(number: float, decimals: int = 2) -> str:
    """Formats a floating-point number as a percentage string.

    Args:
        number (float): The number to format (e.g., 0.1234).
        decimals (int): The number of decimal places to display in the percentage. Default is 2.

    Returns:
        str: The formatted percentage string (e.g., "12.34%").

    Example:
        >>> format_as_percentage(0.1234)
        '12.34%'
        >>> format_as_percentage(0.5, 0)
        '50%'
        >>> format_as_percentage(0.005, 1)
        '0.5%'

    **Cost:** O(1), string formatting.
    """
    return f"{number:.{decimals}%}"


def format_as_scientific_notation(number: float, decimals: int = 2) -> str:
    """Formats a floating-point number in scientific notation.

    Args:
        number (float): The number to format.
        decimals (int): The number of decimal places for the mantissa. Default is 2.

    Returns:
        str: The number string in scientific notation (e.g., "1.23e+06").

    Example:
        >>> format_as_scientific_notation(1230000)
        '1.23e+06'
        >>> format_as_scientific_notation(0.0000000000456, 1)
        '4.6e-11'
        >>> format_as_scientific_notation(1.0, 0)
        '1e+00'

    **Cost:** O(1), scientific notation formatting.
    """
    return f"{number:.{decimals}e}"


def compare_floats_with_tolerance(a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 1e-5) -> bool:
    """Compares two floating-point numbers to determine if they are "close" to each other.

    Uses relative and absolute tolerances. This function is ideal for comparing
    floats in systems where the inherent precision of floating-point calculations
    can lead to small differences that should not be considered significant.

    Args:
        a (float): The first floating-point number to compare.
        b (float): The second floating-point number to compare.
        rel_tol (float): The relative tolerance. Default is 1e-9.
        abs_tol (float): The absolute tolerance. Default is 1e-5.

    Returns:
        bool: True if 'a' and 'b' are considered close according to the tolerances.

    Example:
        >>> compare_floats_with_tolerance(0.1 + 0.2, 0.3)
        True
        >>> compare_floats_with_tolerance(1000000.0, 1000000.0000001, rel_tol=1e-9)
        True

    **Cost:** O(1), tolerance comparison using math.isclose.
    """
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


def percent_change(old_value: float, new_value: float) -> float:
    """Calculates the percentage change between two values.

    Args:
        old_value: The original value (must not be zero).
        new_value: The new value.

    Returns:
        The percentage change as a float (e.g. 50.0 for a 50% increase).

    Raises:
        ValueError: If old_value is zero.

    Example:
        >>> percent_change(100, 150)
        50.0
        >>> percent_change(200, 150)
        -25.0

    Complexity: O(1)
    """
    if old_value == 0:
        raise ValueError("old_value cannot be zero.")

    return ((new_value - old_value) / old_value) * 100


def percent_of(part: float, whole: float) -> float:
    """Calculates what percentage ``part`` is of ``whole``.

    Args:
        part: The partial value.
        whole: The total value (must not be zero).

    Returns:
        The percentage as a float.

    Raises:
        ValueError: If whole is zero.

    Example:
        >>> percent_of(25, 200)
        12.5
        >>> percent_of(3, 4)
        75.0

    Complexity: O(1)
    """
    if whole == 0:
        raise ValueError("whole cannot be zero.")

    return (part / whole) * 100
