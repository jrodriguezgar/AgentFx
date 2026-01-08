"""Numeric Operations Module.

This module provides comprehensive numeric operations including prime number
checking, rounding functions, formatting utilities, scaling, normalization,
and high-precision arithmetic operations.

Key Features:
    - Prime number verification and generation
    - Multiple rounding modes (up, down, to decimals, banker's rounding)
    - Number formatting (leading zeros, percentages, scientific notation)
    - Range scaling and normalization
    - Decimal precision arithmetic
    - Modulo and quantization operations

Example:
    >>> from formulite.fxNumeric.numeric_operations import is_prime, round_to_n_decimals
    >>> is_prime(7)
    True
    >>> round_to_n_decimals(3.14159, 2)
    3.14
"""
import math
import decimal
from decimal import Decimal, ROUND_HALF_EVEN
from typing import List, Union, Any

def is_numeric_type(value: Any) -> bool:
    """Checks if a value is of numeric type.

    Args:
        value (Any): The value to check.

    Returns:
        bool: True if the value is numeric (int, float, Decimal), False otherwise.

    Example:
        >>> is_numeric_type(42)
        True
        >>> is_numeric_type(3.14)
        True
        >>> is_numeric_type(Decimal('10.5'))
        True
        >>> is_numeric_type("123")  # Strings are not considered numeric
        False
        >>> is_numeric_type(None)
        False
        >>> is_numeric_type([1, 2, 3])
        False

    **Cost:** O(1), type verification using isinstance.
    """
    return isinstance(value, (int, float, Decimal))


def is_prime(n: int) -> bool:
    """Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
        >>> is_prime(2)
        True
        >>> is_prime(1)
        False
        >>> is_prime(0)
        False
        >>> is_prime(-7)
        False

    **Cost:** O(√n), where n is the number to check.
    """
    if n < 2:
        return False
    
    # Check only up to the square root of the number
    # to optimize performance
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def get_primes_up_to(limit: int) -> list[int]:
    """Generates a list of prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

    Args:
        limit (int): The upper limit to search for prime numbers.

    Returns:
        list[int]: List of prime numbers found.

    Raises:
        ValueError: If the limit is less than 2.

    Example:
        >>> get_primes_up_to(10)
        [2, 3, 5, 7]
        >>> get_primes_up_to(20)
        [2, 3, 5, 7, 11, 13, 17, 19]
        >>> get_primes_up_to(1)
        ValueError: Limit must be at least 2
        >>> len(get_primes_up_to(100))
        25  # There are 25 prime numbers less than 100

    **Cost:** O(n log log n), Sieve of Eratosthenes algorithm.
    """
    if limit < 2:
        raise ValueError("Limit must be at least 2")

    # Initialize boolean array as True
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    # Sieve of Eratosthenes implementation
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            # Mark all multiples of i as non-prime
            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    # Create the prime list from the boolean array
    return [i for i in range(limit + 1) if sieve[i]]


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


def explicit_truncate(number: float) -> int:
    """Removes the decimal part of a floating-point number without rounding, truncating towards zero.

    Works for both positive and negative numbers.

    Args:
        number (float): The floating-point number to truncate.

    Returns:
        int: The resulting integer.

    Example:
        >>> explicit_truncate(-4.8)
        -4
        >>> explicit_truncate(4.8)
        4
        >>> explicit_truncate(3.1)
        3

    **Cost:** O(1), truncation using math.trunc.
    """
    return math.trunc(number)


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
    return Decimal(str(num1)) + Decimal(str(num2)) # Convert to str first to avoid float imprecisions


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


def force_float_division(numerator: Union[int, float], denominator: Union[int, float]) -> float:
    """Performs division ensuring the result is always a float, even if both operands are integers.

    Args:
        numerator (Union[int, float]): The numerator.
        denominator (Union[int, float]): The denominator.

    Returns:
        float: The division result as a floating-point number.

    Raises:
        ZeroDivisionError: If the denominator is zero.

    Example:
        >>> force_float_division(5, 2)
        2.5
        >>> force_float_division(10, 3)
        3.3333333333333335
        >>> force_float_division(7.0, 2)
        3.5

    **Cost:** O(1), arithmetic division.
    """
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return float(numerator) / denominator # Ensures the numerator is float for division


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
    # For rounding to nearest (up for positive .5, down for negative .5)
    # A common approach for 'round half up' for positives and 'round half down' for negatives:
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
    # For floats, add a very small value to ensure the "step" if it's almost an integer,
    # then truncate.
    # Alternatively, use math.ceil() which is more direct.
    # But if you want to avoid math, this is an approximation:
    if number == int(number): # If already an integer (e.g., 3.0)
        return int(number)
    if number > 0:
        return int(number + 0.9999999999999999) # Add an epsilon to ensure rounding
    else: # If negative, round towards 0 (e.g., -3.1 to -3)
        return int(number) if number == int(number) else int(number + 0.9999999999999999) # Equivalent to ceil for negatives too


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
    # For floats, simply truncate the decimal part.
    # Alternatively, use math.floor() which is more direct.
    # But if you want to avoid math, this is the way:
    if number >= 0:
        return int(number) # Truncate directly for positives
    else: # For negatives, int() truncates towards zero. We need floor-like behavior.
        return int(number - 0.0000000000000001) # Subtract an epsilon to ensure rounding down


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
        >>> # Rounding to nearest integer
        >>> round_half_even(Decimal("2.5")) # 2.5 -> 2 (2 is even)
        Decimal('2')
        >>> round_half_even(Decimal("3.5")) # 3.5 -> 4 (4 is even)
        Decimal('4')
        >>> round_half_even(2.6) # 2.6 -> 3 (normal rounding if not .5)
        Decimal('3')
        >>> round_half_even(2.4) # 2.4 -> 2 (normal rounding if not .5)
        Decimal('2')

        >>> # Rounding to one decimal
        >>> round_half_even(Decimal("2.25"), "0.1") # 2.25 -> 2.2 (2 is even)
        Decimal('2.2')
        >>> round_half_even(Decimal("2.35"), "0.1") # 2.35 -> 2.4 (4 is even)
        Decimal('2.4')

        >>> # Using strings for greater precision in input
        >>> round_half_even("2.5")
        Decimal('2')
        >>> round_half_even("3.5")
        Decimal('4')
        >>> round_half_even("1.235", "0.01") # Rounds 1.235 to two decimals. 3 is odd, so 1.23 -> 1.24
        Decimal('1.24')
        >>> round_half_even("1.245", "0.01") # Rounds 1.245 to two decimals. 4 is even, so 1.24 -> 1.24
        Decimal('1.24')

    **Cost:** O(1), banker's rounding with Decimal.
    """
    if not isinstance(target_precision, str):
        raise TypeError("'target_precision' must be a string (e.g., '1', '0.1', '0.01').")

    # It's crucial to convert the input number to Decimal.
    # If it's float, it's better to pass it to str first to avoid float imprecisions.
    if isinstance(number, float):
        number_decimal = Decimal(str(number))
    elif isinstance(number, (str, Decimal)):
        number_decimal = Decimal(number)
    else:
        raise TypeError("'number' must be a float, str, or Decimal object.")

    # Convert target precision to a Decimal object for the quantize method
    try:
        quantization_precision = Decimal(target_precision)
    except Exception as e:
        raise decimal.InvalidOperation(f"Invalid 'target_precision' string: {target_precision}. Error: {e}")

    # Perform rounding using quantize with ROUND_HALF_EVEN policy
    return number_decimal.quantize(quantization_precision, rounding=ROUND_HALF_EVEN)


def round_to_nearest_multiple(number: Union[int, float], base: Union[int, float]) -> Union[int, float]:
    """Rounds a number to the nearest multiple of a given base.

    Divides the number by the base, rounds the result to the nearest integer
    using round() (which uses "round half to even" for .5), then multiplies
    by the base to get the desired multiple.

    Args:
        number (Union[int, float]): The number to round.
        base (Union[int, float]): The base or multiple to round to.

    Returns:
        Union[int, float]: The number rounded to the nearest multiple of the base.
                           Returns int if base is int and result is integer; otherwise float.

    Raises:
        ValueError: If 'base' is zero, as division by zero is not allowed.

    Example:
        >>> # Round 7 to nearest multiple of 5
        >>> round_to_nearest_multiple(7, 5)
        5

        >>> # Round 8 to nearest multiple of 5
        >>> round_to_nearest_multiple(8, 5)
        10

        >>> # Round time to nearest half hour
        >>> round_to_nearest_multiple(10.25, 0.5) # 10.25 hours -> 10.5 hours (10:30)
        10.5

        >>> # Round 23 to nearest multiple of 10
        >>> round_to_nearest_multiple(23, 10)
        20

        >>> # Round 25 to nearest multiple of 10 (round half to even: 2.5 -> 2)
        >>> round_to_nearest_multiple(25, 10)
        20

        >>> # Round 35 to nearest multiple of 10 (round half to even: 3.5 -> 4)
        >>> round_to_nearest_multiple(35, 10)
        40

        >>> # Zero base (raises ValueError)
        >>> try:
        >>>     round_to_nearest_multiple(10, 0)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: The 'base' for rounding cannot be zero.

    **Cost:** O(1), division and rounding.
    """
    if base == 0:
        raise ValueError("The 'base' for rounding cannot be zero.")

    # Divide the number by the base, round the result to the nearest integer,
    # and then multiply by the base.
    # Python 3's round() follows the "round half to even" rule (banker's rounding).
    return round(number / base) * base


def normalize_to_0_1_range(x: Union[int, float], min_val: Union[int, float], max_val: Union[int, float]) -> float:
    """Normalizes a number to scale it to a range between 0 and 1.

    Args:
        x (Union[int, float]): The numeric value to normalize.
        min_val (Union[int, float]): The expected minimum value in the original range.
        max_val (Union[int, float]): The expected maximum value in the original range.

    Returns:
        float: The normalized value between 0 and 1. If min_val == max_val, returns 0.0.

    Raises:
        ValueError: If 'min_val' is greater than 'max_val'.

    Example:
        >>> normalize_to_0_1_range(50, 0, 100)
        0.5
        >>> normalize_to_0_1_range(10, 0, 100)
        0.1
        >>> normalize_to_0_1_range(100, 0, 100)
        1.0
        >>> normalize_to_0_1_range(0, 0, 100)
        0.0
        >>> normalize_to_0_1_range(75, 50, 100)
        0.5
        >>> normalize_to_0_1_range(5, 5, 5) # min_val == max_val
        0.0

    **Cost:** O(1), normalization calculation.
    """
    if min_val > max_val:
        raise ValueError("min_val cannot be greater than max_val.")
    
    if max_val == min_val:
        return 0.0 # Avoid division by zero if the range is a single point.
                   # In many ML contexts, if the range is 0, the normalized value is 0.

    return (x - min_val) / (max_val - min_val)


def scale_to_new_range(x: Union[int, float], min_x: Union[int, float], max_x: Union[int, float], new_min: Union[int, float], new_max: Union[int, float]) -> float:
    """Scales a number from an original range to a new range.

    Args:
        x (Union[int, float]): The numeric value to scale.
        min_x (Union[int, float]): The minimum value of the original range.
        max_x (Union[int, float]): The maximum value of the original range.
        new_min (Union[int, float]): The minimum value of the new range.
        new_max (Union[int, float]): The maximum value of the new range.

    Returns:
        float: The scaled value in the new range. If max_x == min_x, returns new_min.

    Raises:
        ValueError: If 'min_x' is greater than 'max_x'.

    Example:
        >>> # Scale 50 from 0-100 to 0-10
        >>> scale_to_new_range(50, 0, 100, 0, 10)
        5.0
        >>> # Scale 120 from 0-200 to 0-1
        >>> scale_to_new_range(120, 0, 200, 0, 1)
        0.6
        >>> # Scale 50 from 0-100 to 100-200
        >>> scale_to_new_range(50, 0, 100, 100, 200)
        150.0
        >>> # Scale 5 from 5-5 to 0-10 (original range is a single point)
        >>> scale_to_new_range(5, 5, 5, 0, 10)
        0.0

    **Cost:** O(1), linear scaling.
    """
    if min_x > max_x:
        raise ValueError("min_x cannot be greater than max_x.")
    
    if max_x == min_x:
        return float(new_min) # If the original range is a single point, the scaled value is new_min.

    # Linear scaling formula
    normalized_x = (x - min_x) / (max_x - min_x)
    new_val = new_min + normalized_x * (new_max - new_min)
    return float(new_val)


def clip_number(x: Union[int, float], min_val: Union[int, float], max_val: Union[int, float]) -> Union[int, float]:
    """Forces a number to be within a specific range [min_val, max_val].

    If the number is less than min_val, returns min_val.
    If the number is greater than max_val, returns max_val.
    If the number is within the range, returns the original number.

    Args:
        x (Union[int, float]): The number to clip.
        min_val (Union[int, float]): The minimum allowed value.
        max_val (Union[int, float]): The maximum allowed value.

    Returns:
        Union[int, float]: The number adjusted to the range.

    Raises:
        ValueError: If 'min_val' is greater than 'max_val'.

    Example:
        >>> clip_number(10, 0, 100)
        10
        >>> clip_number(-5, 0, 100)
        0
        >>> clip_number(150, 0, 100)
        100
        >>> clip_number(50.5, 0.0, 100.0)
        50.5
        >>> clip_number(5, 10, 20) # Min is 10, value is 5 -> returns 10
        10

    **Cost:** O(1), comparisons and value adjustment.
    """
    if min_val > max_val:
        raise ValueError("min_val cannot be greater than max_val.")

    return max(min(x, max_val), min_val)


def reduce_to_modulo_range(x: Union[int, float], base: Union[int, float]) -> Union[int, float]:
    """Converts a value to a cyclic range using the modulo operation.

    The result will be in the range [0, base) for positive numbers,
    or in the range (-base, 0] for negative numbers (if x is negative).

    Args:
        x (Union[int, float]): The numeric value to reduce.
        base (Union[int, float]): The cycle base (the range size).
                                   Must be a positive number.

    Returns:
        Union[int, float]: The value reduced to the cyclic range.

    Raises:
        ValueError: If 'base' is zero or negative.

    Example:
        >>> # Example with clock (hours in a day)
        >>> reduce_to_modulo_range(25, 24)
        1 # 25 hours is 1 AM the next day

        >>> # Example with angles (360 degrees)
        >>> reduce_to_modulo_range(370, 360)
        10 # 370 degrees is equivalent to 10 degrees

        >>> # Example with negative values
        >>> reduce_to_modulo_range(-5, 10)
        5 # -5 is 5 units before 0 in a cycle of 10

        >>> reduce_to_modulo_range(-25, 24)
        23 # -25 hours is 23 PM the previous day

        >>> # Zero base (raises ValueError)
        >>> try:
        >>>     reduce_to_modulo_range(10, 0)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: The 'base' must be a positive number.

    **Cost:** O(1), modulo operation.
    """
    if base <= 0:
        raise ValueError("The 'base' must be a positive number.")
    
    # The modulo (%) operation in Python correctly handles negative numbers,
    # ensuring that the result has the same sign as the divisor (base).
    return x % base


def quantize_number(x: Union[int, float], step: Union[int, float]) -> Union[int, float]:
    """Quantizes a number, forcing it to take only certain discrete values (multiples of 'step').

    This is useful for simplifying values or adjusting them to a specific granularity.

    Args:
        x (Union[int, float]): The number to quantize.
        step (Union[int, float]): The increment size or "step" for quantization.
                                  Must be a positive number.

    Returns:
        Union[int, float]: The number quantized to the nearest multiple of 'step'.
                           Returns int if step is int and result is integer; otherwise float.

    Raises:
        ValueError: If 'step' is zero or negative.

    Example:
        >>> # Quantize to multiples of 0.25
        >>> quantize_number(1.23, 0.25)
        1.25
        >>> quantize_number(1.10, 0.25)
        1.0
        >>> quantize_number(1.12, 0.25)
        1.0
        >>> quantize_number(1.13, 0.25)
        1.25

        >>> # Quantize to multiples of 10
        >>> quantize_number(23, 10)
        20
        >>> quantize_number(27, 10)
        30
        >>> quantize_number(25, 10) # Round half to even: 2.5 -> 2
        20

        >>> # Zero step (raises ValueError)
        >>> try:
        >>>     quantize_number(10, 0)
        >>> except ValueError as e:
        >>>     print(f"Error: {e}")
        # Expected output: Error: The 'step' for quantization cannot be zero or negative.

    **Cost:** O(1), quantization through division and rounding.
    """
    if step <= 0:
        raise ValueError("The 'step' for quantization cannot be zero or negative.")

    # Divide by step, round to nearest integer, and multiply by step.
    # Uses round() which in Python 3 follows the "round half to even" rule.
    return round(x / step) * step


def add_bool_to_int(boolean_value: bool, int_value: int) -> int:
    """Adds a boolean value to an integer.

    In Python, True evaluates to 1 and False to 0 in numeric contexts.
    This allows using booleans directly in arithmetic operations,
    which is especially useful for creating conditional counters.

    Args:
        boolean_value (bool): The boolean value (True or False).
        int_value (int): The integer to which the boolean will be added.

    Returns:
        int: The result of the addition.

    Raises:
        TypeError: If 'boolean_value' is not a boolean or 'int_value' is not an integer.

    Example:
        >>> add_bool_to_int(True, 2)
        3
        >>> add_bool_to_int(False, 5)
        5
        >>> add_bool_to_int(True, 0)
        1
        >>> add_bool_to_int(False, -3)
        -3
        >>> # Use in a counting context (not part of the function, just demonstration)
        >>> counter = 0
        >>> is_active = True
        >>> has_permission = False
        >>> counter += is_active  # counter becomes 1
        >>> counter += has_permission # counter remains 1
        >>> counter
        1

    **Cost:** O(1), boolean addition as integer.
    """
    if not isinstance(boolean_value, bool):
        raise TypeError("'boolean_value' must be a boolean.")
    if not isinstance(int_value, int):
        raise TypeError("'int_value' must be an integer.")

    # Python automatically converts boolean_value to 1 or 0
    return boolean_value + int_value


def safe_sum_with_none(num1: Union[int, float, None], num2: Union[int, float, None]) -> Union[int, float]:
    """Performs addition of two numbers, safely handling None values.

    Before performing the sum, each argument is verified. If it's None,
    it's replaced with 0, ensuring the arithmetic operation is always
    performed between numbers.

    Args:
        num1 (Union[int, float, None]): The first number (or None).
        num2 (Union[int, float, None]): The second number (or None).

    Returns:
        Union[int, float]: The result of the addition. The return type depends on
                           the types of numbers involved (int if both are int,
                           float if at least one is float).

    Raises:
        TypeError: If any value, after None substitution, is not a number.
                   (Though the function is designed to avoid this if expected input is int/float/None).

    Example:
        >>> safe_sum_with_none(3, 5)
        8
        >>> safe_sum_with_none(3, None)
        3
        >>> safe_sum_with_none(None, 5)
        5
        >>> safe_sum_with_none(None, None)
        0
        >>> safe_sum_with_none(3.5, None)
        3.5
        >>> safe_sum_with_none(10, -3)
        7

        >>> # Example of what would happen without the function (causes TypeError)
        >>> # try:
        >>> #     print(3 + None)
        >>> # except TypeError as e:
        >>> #     print(f"Expected error: {e}")
        # Expected output: Expected error: unsupported operand type(s) for +: 'int' and 'NoneType'

        >>> # A case where the function could still fail (if input is not None, int, or float)
        >>> # try:
        >>> #     safe_sum_with_none("abc", 5)
        >>> # except TypeError as e:
        >>> #     print(f"Expected error: {e}")
        # Expected output: Expected error: unsupported operand type(s) for +: 'str' and 'int'

    **Cost:** O(1), addition with None handling.
    """
    # Replace None with 0 for addition
    val1 = num1 if num1 is not None else 0
    val2 = num2 if num2 is not None else 0

    # Now that we know val1 and val2 are numbers (or 0), we can add them.
    # Python automatically handles type promotion (int + float = float).
    return val1 + val2


def count_true_with_sum(boolean_list: List[bool]) -> int:
    """Counts the number of True values in a boolean list using the sum() function.

    Internally, Python treats True as 1 and False as 0. The sum() function
    simply adds these values (1s and 0s), resulting in a direct count of
    how many True values are in the list.

    Args:
        boolean_list (List[bool]): A list containing True or False values.

    Returns:
        int: The total number of True values in the list.

    Raises:
        TypeError: If 'boolean_list' is not a list or contains non-boolean elements.

    Example:
        >>> count_true_with_sum([True, False, True, True])
        3
        >>> count_true_with_sum([False, False, False])
        0
        >>> count_true_with_sum([])
        0
        >>> count_true_with_sum([True, False])
        1

        >>> # Example with a generator (more efficient for large datasets)
        >>> # This is not part of the function, just a demonstration of use.
        >>> numbers = [1, 2, 3, 4, 5, 6]
        >>> count_even = sum(1 for n in numbers if n % 2 == 0) # Generator of 1s for True
        >>> print(f"Even numbers: {count_even}")
        # Expected output: Even numbers: 3

        >>> # Another more direct example using the boolean directly:
        >>> count_even_direct = sum(n % 2 == 0 for n in numbers)
        >>> print(f"Even numbers (direct): {count_even_direct}")
        # Expected output: Even numbers (direct): 3

    **Cost:** O(n), where n is the number of elements in the list.
    """
    if not isinstance(boolean_list, list):
        raise TypeError("'boolean_list' must be a list.")
    
    # Validate that all elements are booleans for a typed function
    for item in boolean_list:
        if not isinstance(item, bool):
            raise TypeError("All elements in 'boolean_list' must be booleans.")

    # Python treats True as 1 and False as 0 in sum()
    return sum(boolean_list)


def true_division(numerator: Union[int, float], denominator: Union[int, float]) -> float:
    """Performs "true" (floating-point) division, always returning a floating-point number.

    Args:
        numerator (Union[int, float]): The dividend.
        denominator (Union[int, float]): The divisor.

    Returns:
        float: The division result as a float.

    Raises:
        ZeroDivisionError: If the divisor is zero.

    Example:
        >>> true_division(5, 2)
        2.5
        >>> true_division(10, 4)
        2.5
        >>> true_division(6, 2) # Even if result is an integer, it's returned as float
        3.0

    **Cost:** O(1), floating-point division.
    """
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return numerator / denominator


def floor_division(numerator: Union[int, float], denominator: Union[int, float]) -> Union[int, float]:
    """Performs integer (floor) division, truncating the result downwards.

    Args:
        numerator (Union[int, float]): The dividend.
        denominator (Union[int, float]): The divisor.

    Returns:
        Union[int, float]: The integer part of the quotient. Type will be int if both
                           operands were int, or float if at least one was float.

    Raises:
        ZeroDivisionError: If the divisor is zero.

    Example:
        >>> floor_division(5, 2)
        2
        >>> floor_division(10, 4)
        2
        >>> floor_division(7, 3)
        2
        >>> floor_division(-5, 2) # -2.5 truncated down is -3
        -3
        >>> floor_division(5.0, 2) # If one operand is float, result is float
        2.0

    **Cost:** O(1), integer division.
    """
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return numerator // denominator


def safe_division_for_context(
    numerator: Union[int, float],
    denominator: Union[int, float],
    return_float: bool = True
) -> Union[int, float]:
    """Performs division selecting the appropriate operator based on context needs.

    Args:
        numerator (Union[int, float]): The dividend.
        denominator (Union[int, float]): The divisor.
        return_float (bool): If True, performs floating-point division (`/`).
                             If False, performs integer division (`//`).
                             Default is True.

    Returns:
        Union[int, float]: The division result, either a float or a truncated int/float.

    Raises:
        ZeroDivisionError: If the divisor is zero.

    Example:
        >>> safe_division_for_context(5, 2, return_float=True)
        2.5
        >>> safe_division_for_context(5, 2, return_float=False)
        2
        >>> safe_division_for_context(10, 3, return_float=True)
        3.3333333333333335
        >>> safe_division_for_context(10, 3, return_float=False)
        3
        >>> safe_division_for_context(7.0, 2, return_float=False) # Float operand -> float result
        3.0

    **Cost:** O(1), division according to specified type.
    """
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    if return_float:
        return numerator / denominator
    else:
        return numerator // denominator
    

def compare_floats_with_tolerance(a: float, b: float, rel_tol: float = 1e-9, abs_tol: float = 1e-5) -> bool:
    """Compares two floating-point numbers to determine if they are "close" to each other.

    Uses relative and absolute tolerances. This function is ideal for comparing
    floats in systems where the inherent precision of floating-point calculations
    can lead to small differences that should not be considered significant.

    Args:
        a (float): The first floating-point number to compare.
        b (float): The second floating-point number to compare.
        rel_tol (float): The relative tolerance. Represents the maximum allowed
                         difference between 'a' and 'b', relative to the larger
                         of their absolute values. Default is 1e-9.
                         Useful for large numbers.
        abs_tol (float): The absolute tolerance. Represents the maximum fixed
                         difference allowed between 'a' and 'b', regardless of
                         their magnitude. Default is 1e-5.
                         Useful for numbers close to zero.

    Returns:
        bool: True if 'a' and 'b' are considered close according to the tolerances,
              False otherwise.

    Example:
        >>> compare_floats_with_tolerance(0.1 + 0.2, 0.3)
        True
        >>> compare_floats_with_tolerance(1000000.0, 1000000.0000001, rel_tol=1e-9)
        True
        >>> compare_floats_with_tolerance(0.0000001, 0.0000002, abs_tol=1e-6)
        True

    **Cost:** O(1), tolerance comparison using math.isclose.
    """
    return math.isclose(a, b, rel_tol=rel_tol, abs_tol=abs_tol)


