"""Rounding Functions Module.

Provides multiple rounding strategies including standard rounding, truncation,
ceiling, floor, banker's rounding, even/odd rounding, significance-based
rounding, quantization, and high-precision Decimal arithmetic.

Example:
    >>> from formulite.fxNumeric.rounding_functions import round_to_n_decimals, round_half_even
    >>> round_to_n_decimals(3.14159, 2)
    3.14
"""

import math
import decimal
from decimal import Decimal, ROUND_HALF_EVEN
from typing import Union


def truncate_float(number: float) -> int:
    """Truncates a floating-point number, removing the decimal part.

    Similar to int(), but semantically clearer for truncation operations.

    Args:
        number (float): The floating-point number to truncate.

    Returns:
        int: The resulting integer with decimals removed (truncated towards zero).

    Example:
        >>> truncate_float(3.9)
        3
        >>> truncate_float(-3.9)
        -3
        >>> truncate_float(5.0)
        5
        >>> truncate_float(3.1)
        3

    **Cost:** O(1), truncation using math.trunc.
    """
    return math.trunc(number)


def round_to_n_decimals(number: float, decimals: int) -> float:
    """Rounds a floating-point number to a specific number of decimals.

    Args:
        number (float): The floating-point number to round.
        decimals (int): The number of decimal places to round to.

    Returns:
        float: The rounded number.

    Example:
        >>> round_to_n_decimals(3.14159, 2)
        3.14
        >>> round_to_n_decimals(123.4567, 1)
        123.5
        >>> round_to_n_decimals(9.999, 2)
        10.0

    **Cost:** O(1), Python built-in rounding.
    """
    return round(number, decimals)


def round_up(number: float) -> int:
    """Rounds a floating-point number always up to the nearest integer.

    Args:
        number (float): The floating-point number to round up.

    Returns:
        int: The smallest integer that is greater than or equal to 'number'.

    Example:
        >>> round_up(3.1)
        4
        >>> round_up(3.9)
        4
        >>> round_up(3.0)
        3
        >>> round_up(-3.1)
        -3

    **Cost:** O(1), ceiling calculation using math.ceil.
    """
    return math.ceil(number)


def round_down(number: float) -> int:
    """Rounds a floating-point number always down to the nearest integer.

    Args:
        number (float): The floating-point number to round down.

    Returns:
        int: The largest integer that is less than or equal to 'number'.

    Example:
        >>> round_down(3.9)
        3
        >>> round_down(3.1)
        3
        >>> round_down(3.0)
        3
        >>> round_down(-3.9)
        -4

    **Cost:** O(1), floor calculation using math.floor.
    """
    return math.floor(number)


def add_with_exact_precision(num1: Union[float, str], num2: Union[float, str]) -> Decimal:
    """Adds two numbers using the Decimal type to avoid precision errors.

    Args:
        num1 (Union[float, str]): The first number, can be a float or a string.
                                  Using strings is recommended for total precision in input.
        num2 (Union[float, str]): The second number, can be a float or a string.

    Returns:
        Decimal: The sum result with exact decimal precision.

    Example:
        >>> # Example with float (demonstrating inherent float imprecision)
        >>> 0.1 + 0.2
        0.30000000000000004

        >>> # Example with Decimal for exact precision
        >>> add_with_exact_precision("0.1", "0.2")
        Decimal('0.3')
        >>> add_with_exact_precision(Decimal('0.1'), Decimal('0.2'))
        Decimal('0.3')
        >>> add_with_exact_precision(1.23, 4.56) # Even with float input, internal operation is precise
        Decimal('5.79')

    **Cost:** O(1), addition with decimal precision arithmetic.
    """
    return Decimal(str(num1)) + Decimal(str(num2))


def manual_round_and_cast(number: float) -> int:
    """Performs manual rounding to the nearest integer and then casts to int.

    This method can be used as an alternative to round() if you want to avoid
    Python 3's 'round half to even' behavior.

    Args:
        number (float): The floating-point number to round and cast.

    Returns:
        int: The resulting integer from manual rounding.

    Example:
        >>> manual_round_and_cast(3.6)
        4
        >>> manual_round_and_cast(3.2)
        3
        >>> manual_round_and_cast(3.5) # Always rounds up for .5
        4
        >>> manual_round_and_cast(2.5) # Always rounds up for .5, resulting in 3
        3
        >>> manual_round_and_cast(-3.6)
        -4
        >>> manual_round_and_cast(-3.5) # Rounds to the integer farthest from zero
        -4

    **Cost:** O(1), manual rounding and conversion.
    """
    if number >= 0:
        return int(number + 0.5)
    else:
        return int(number - 0.5)


def manual_round_up_to_int(number: float) -> int:
    """Rounds a floating-point number to the nearest integer, always upwards.

    Works for both positive and negative numbers.

    Args:
        number (float): The floating-point number to round.

    Returns:
        int: The resulting integer, always rounded upwards.

    Example:
        >>> manual_round_up_to_int(3.1)
        4
        >>> manual_round_up_to_int(3.9)
        4
        >>> manual_round_up_to_int(3.0)
        3
        >>> manual_round_up_to_int(-3.1)
        -3 # Rounds from -3.1 to -3 (greater than or equal to -3.1)
        >>> manual_round_up_to_int(-3.9)
        -3

    **Cost:** O(1), rounding upwards.
    """
    if number == int(number):
        return int(number)

    if number > 0:
        return int(number + 0.9999999999999999)
    else:
        return int(number) if number == int(number) else int(number + 0.9999999999999999)


def manual_round_down_to_int(number: float) -> int:
    """Rounds a floating-point number to the nearest integer, always downwards.

    Works for both positive and negative numbers.

    Args:
        number (float): The floating-point number to round.

    Returns:
        int: The resulting integer, always rounded downwards.

    Example:
        >>> manual_round_down_to_int(3.9)
        3
        >>> manual_round_down_to_int(3.1)
        3
        >>> manual_round_down_to_int(3.0)
        3
        >>> manual_round_down_to_int(-3.1)
        -4 # Rounds from -3.1 to -4 (less than or equal to -3.1)
        >>> manual_round_down_to_int(-3.9)
        -4

    **Cost:** O(1), rounding downwards.
    """
    if number >= 0:
        return int(number)
    else:
        return int(number - 0.0000000000000001)


def round_half_even(number: Union[float, str, Decimal], target_precision: str = "1") -> Decimal:
    """Performs banker's rounding (ROUND_HALF_EVEN) of a number to a specific precision.

    In banker's rounding, when the digit to round is 5, the number is rounded to the
    nearest even number. For example, 2.5 rounds to 2, while 3.5 rounds to 4.
    This avoids cumulative bias in financial or scientific calculations.

    The target precision defines which decimal place to round to. For example,
    "1" for rounding to an integer, "0.1" for one decimal, "0.01" for two decimals, etc.

    Args:
        number (Union[float, str, Decimal]): The number to round. Passing it as a string
                                             or Decimal is recommended to avoid binary
                                             float imprecisions.
        target_precision (str): A string representing the desired precision.
                                Example: "1" to round to an integer, "0.1" for one decimal,
                                "0.01" for two decimals, etc. Default is "1" (round to integer).

    Returns:
        Decimal: The rounded number with the specified precision and ROUND_HALF_EVEN policy.

    Raises:
        TypeError: If 'number' or 'target_precision' are not of valid types.
        decimal.InvalidOperation: If 'target_precision' is not a string representing a valid number.

    Example:
        >>> round_half_even(Decimal("2.5"))
        Decimal('2')
        >>> round_half_even(Decimal("3.5"))
        Decimal('4')
        >>> round_half_even(2.6)
        Decimal('3')
        >>> round_half_even(Decimal("2.25"), "0.1")
        Decimal('2.2')
        >>> round_half_even("2.5")
        Decimal('2')

    **Cost:** O(1), banker's rounding with Decimal.
    """
    if not isinstance(target_precision, str):
        raise TypeError("'target_precision' must be a string (e.g., '1', '0.1', '0.01').")

    if isinstance(number, float):
        number_decimal = Decimal(str(number))
    elif isinstance(number, (str, Decimal)):
        number_decimal = Decimal(number)
    else:
        raise TypeError("'number' must be a float, str, or Decimal object.")

    try:
        quantization_precision = Decimal(target_precision)
    except Exception as e:
        raise decimal.InvalidOperation(f"Invalid 'target_precision' string: {target_precision}. Error: {e}")

    return number_decimal.quantize(quantization_precision, rounding=ROUND_HALF_EVEN)


def round_to_nearest_multiple(number: Union[int, float], base: Union[int, float]) -> Union[int, float]:
    """Rounds a number to the nearest multiple of a given base.

    Args:
        number (Union[int, float]): The number to round.
        base (Union[int, float]): The base or multiple to round to.

    Returns:
        Union[int, float]: The number rounded to the nearest multiple of the base.

    Raises:
        ValueError: If 'base' is zero.

    Example:
        >>> round_to_nearest_multiple(7, 5)
        5
        >>> round_to_nearest_multiple(8, 5)
        10
        >>> round_to_nearest_multiple(10.25, 0.5)
        10.5

    **Cost:** O(1), division and rounding.
    """
    if base == 0:
        raise ValueError("The 'base' for rounding cannot be zero.")

    return quantize_number(number, abs(base))


def even(number: float) -> int:
    """Rounds a number up to the nearest even integer.

    Positive numbers round away from zero to the next even integer.
    Negative numbers round away from zero to the next even integer.

    Args:
        number: The number to round.

    Returns:
        The nearest even integer away from zero.

    Example:
        >>> even(1.5)
        2
        >>> even(3)
        4
        >>> even(-1.5)
        -2

    Complexity: O(1)
    """
    if number >= 0:
        result = math.ceil(number)

        if result % 2 != 0:
            result += 1

    else:
        result = math.floor(number)

        if result % 2 != 0:
            result -= 1

    return result


def odd(number: float) -> int:
    """Rounds a number up to the nearest odd integer.

    Positive numbers round away from zero to the next odd integer.
    Negative numbers round away from zero to the next odd integer.

    Args:
        number: The number to round.

    Returns:
        The nearest odd integer away from zero.

    Example:
        >>> odd(1.5)
        3
        >>> odd(2)
        3
        >>> odd(-1.5)
        -3

    Complexity: O(1)
    """
    if number >= 0:
        result = math.ceil(number)

        if result % 2 == 0:
            result += 1

    else:
        result = math.floor(number)

        if result % 2 == 0:
            result -= 1

    return result


def ceiling_significance(number: float, significance: float = 1.0) -> float:
    """Rounds a number up to the nearest multiple of significance.

    Args:
        number: The number to round.
        significance: The multiple to round up to. Default 1.

    Returns:
        The rounded value.

    Raises:
        ValueError: If significance is zero.

    Example:
        >>> ceiling_significance(2.5, 1)
        3.0
        >>> ceiling_significance(4.42, 0.05)
        4.45

    Complexity: O(1)
    """
    if significance == 0:
        raise ValueError("Significance cannot be zero.")

    return math.ceil(number / significance) * significance


def floor_significance(number: float, significance: float = 1.0) -> float:
    """Rounds a number down to the nearest multiple of significance.

    Args:
        number: The number to round.
        significance: The multiple to round down to. Default 1.

    Returns:
        The rounded value.

    Raises:
        ValueError: If significance is zero.

    Example:
        >>> floor_significance(2.5, 1)
        2.0
        >>> floor_significance(4.42, 0.05)
        4.4

    Complexity: O(1)
    """
    if significance == 0:
        raise ValueError("Significance cannot be zero.")

    return math.floor(number / significance) * significance


def quantize_number(x: Union[int, float], step: Union[int, float]) -> Union[int, float]:
    """Quantizes a number, forcing it to take only certain discrete values (multiples of 'step').

    Args:
        x (Union[int, float]): The number to quantize.
        step (Union[int, float]): The increment size or "step" for quantization.
                                  Must be a positive number.

    Returns:
        Union[int, float]: The number quantized to the nearest multiple of 'step'.

    Raises:
        ValueError: If 'step' is zero or negative.

    Example:
        >>> quantize_number(1.23, 0.25)
        1.25
        >>> quantize_number(1.10, 0.25)
        1.0
        >>> quantize_number(23, 10)
        20

    **Cost:** O(1), quantization through division and rounding.
    """
    if step <= 0:
        raise ValueError("The 'step' for quantization cannot be zero or negative.")

    return round(x / step) * step


def ceiling_math(
    number: float, significance: float = 1.0, mode: int = 0,
) -> float:
    """Round *number* up to the nearest multiple of *significance*.

    For negative numbers, *mode* controls direction:
    ``0`` → away from zero (toward positive infinity),
    ``1`` → toward zero (toward negative infinity).
    Equivalent to Excel ``CEILING.MATH``.

    Args:
        number: Value to round.
        significance: Rounding multiple (default ``1``).
        mode: Negative-number mode (``0`` or ``1``).

    Returns:
        Rounded value.

    Example:
        >>> ceiling_math(2.5)
        3.0
        >>> ceiling_math(-2.5, 1, 1)
        -3.0

    Complexity: O(1)
    """
    if significance == 0:
        return 0.0

    s = abs(significance)

    if number >= 0 or mode == 0:
        return math.ceil(number / s) * s

    return math.floor(number / s) * s


def ceiling_precise(number: float, significance: float = 1.0) -> float:
    """Round *number* up to the nearest multiple of *significance*.

    Always rounds toward positive infinity regardless of sign.
    Equivalent to Excel ``CEILING.PRECISE``.

    Args:
        number: Value to round.
        significance: Rounding multiple (default ``1``).

    Returns:
        Rounded value.

    Example:
        >>> ceiling_precise(2.5, 1)
        3.0
        >>> ceiling_precise(-2.5, 1)
        -2.0

    Complexity: O(1)
    """
    if significance == 0:
        return 0.0

    return math.ceil(number / abs(significance)) * abs(significance)


def floor_math(
    number: float, significance: float = 1.0, mode: int = 0,
) -> float:
    """Round *number* down to the nearest multiple of *significance*.

    For negative numbers, *mode* controls direction:
    ``0`` → toward negative infinity,
    ``1`` → toward zero (away from negative infinity).
    Equivalent to Excel ``FLOOR.MATH``.

    Args:
        number: Value to round.
        significance: Rounding multiple (default ``1``).
        mode: Negative-number mode (``0`` or ``1``).

    Returns:
        Rounded value.

    Example:
        >>> floor_math(3.7)
        3.0
        >>> floor_math(-2.5, 1, 1)
        -2.0

    Complexity: O(1)
    """
    if significance == 0:
        return 0.0

    s = abs(significance)

    if number >= 0 or mode == 0:
        return math.floor(number / s) * s

    return math.ceil(number / s) * s


def floor_precise(number: float, significance: float = 1.0) -> float:
    """Round *number* down to the nearest multiple of *significance*.

    Always rounds toward negative infinity regardless of sign.
    Equivalent to Excel ``FLOOR.PRECISE``.

    Args:
        number: Value to round.
        significance: Rounding multiple (default ``1``).

    Returns:
        Rounded value.

    Example:
        >>> floor_precise(3.7, 1)
        3.0
        >>> floor_precise(-2.5, 1)
        -3.0

    Complexity: O(1)
    """
    if significance == 0:
        return 0.0

    return math.floor(number / abs(significance)) * abs(significance)
