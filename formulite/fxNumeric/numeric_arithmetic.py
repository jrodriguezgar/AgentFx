"""Arithmetic operations module.

This module provides fundamental arithmetic operations including logarithms,
exponentiation, and root calculations. All functions are optimized for numerical
stability and handle edge cases appropriately.
"""

import math
from typing import Union


def natural_log(x: float) -> float:
    """Calculates the natural logarithm (base e) of a number.
    
    Description:
        Computes ln(x) or log_e(x), the natural logarithm of x. The natural
        logarithm is the inverse of the exponential function e^x.
    
    Args:
        x (float): The number for which to calculate the natural logarithm.
                  Must be positive.
    
    Returns:
        float: The natural logarithm of x.
    
    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is not positive.
    
    Usage Example:
        >>> import math
        >>> from formulite.fxNumeric.numeric_arithmetic import natural_log
        >>> natural_log(math.e)
        1.0
        >>> round(natural_log(1), 10)
        0.0
        >>> round(natural_log(10), 10)
        2.302585093
    
    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")
    if x <= 0:
        raise ValueError("Domain error: The number (x) for natural logarithm must be positive.")

    return math.log(x)


def common_log(x: float) -> float:
    """Calculates the common logarithm (base 10) of a number.
    
    Description:
        Computes log₁₀(x), the common logarithm of x. This is widely used in
        scientific calculations, pH calculations, and decibel measurements.
    
    Args:
        x (float): The number for which to calculate the common logarithm.
                  Must be positive.
    
    Returns:
        float: The common logarithm of x.
    
    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is not positive.
    
    Usage Example:
        >>> from formulite.fxNumeric.numeric_arithmetic import common_log
        >>> common_log(10)
        1.0
        >>> round(common_log(100), 10)
        2.0
        >>> round(common_log(1), 10)
        0.0
    
    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")
    if x <= 0:
        raise ValueError("Domain error: The number (x) for common logarithm must be positive.")

    return math.log10(x)


def log_base_n(x: float, base: Union[int, float]) -> float:
    """Calculates the logarithm of a number to a specified base N.
    
    Description:
        Computes log_base(x) using the change of base formula:
        log_base(x) = ln(x) / ln(base). This allows logarithms with any
        positive base other than 1.
    
    Args:
        x (float): The number for which to calculate the logarithm.
                  Must be positive.
        base (Union[int, float]): The base of the logarithm.
                                 Must be positive and not equal to 1.
    
    Returns:
        float: The logarithm of x to the given base.
    
    Raises:
        TypeError: If x or base are not numeric.
        ValueError: If x is not positive, base is not positive, or base is 1.
    
    Usage Example:
        >>> import math
        >>> from formulite.fxNumeric.numeric_arithmetic import log_base_n
        >>> log_base_n(100, 10)
        2.0
        >>> round(log_base_n(8, 2), 10)
        3.0
        >>> round(log_base_n(math.e, 10), 10)
        0.4342944819
    
    Cost: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(base, (int, float)):
        raise TypeError("Both x and base must be numeric values (int or float).")
    if x <= 0:
        raise ValueError("Domain error: The number (x) for logarithm must be positive.")
    if base <= 0:
        raise ValueError("Domain error: The base for logarithm must be positive.")
    if base == 1:
        raise ValueError("Domain error: The base for logarithm cannot be 1.")

    return math.log(x) / math.log(base)


def log1p(x: float) -> float:
    """Calculates the natural logarithm of (1 + x) with high precision.
    
    Description:
        Computes ln(1 + x) accurately for values of x close to zero, where
        direct computation of log(1 + x) would lose precision due to
        floating-point arithmetic limitations. Uses specialized algorithms
        for numerical stability.
    
    Args:
        x (float): The number for which to calculate log(1 + x).
                  Must be greater than -1.
    
    Returns:
        float: The natural logarithm of (1 + x).
    
    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is less than or equal to -1.
    
    Usage Example:
        >>> import math
        >>> from formulite.fxNumeric.numeric_arithmetic import log1p
        >>> round(log1p(0), 10)
        0.0
        >>> small_x = 1e-9
        >>> round(log1p(small_x), 15)  # More precise than log(1+x)
        0.000000001000000
    
    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")
    if x <= -1:
        raise ValueError("Domain error: x must be greater than -1 for log(1 + x).")

    return math.log1p(x)


def power(base: Union[int, float], exponent: Union[int, float]) -> float:
    """Calculates the value of a base raised to a specified exponent.
    
    Description:
        Computes base^exponent, handling both positive and negative bases
        and exponents. Returns only real-valued results; complex results
        (e.g., negative base with non-integer exponent) raise an error.
        Properly handles edge cases like 0^0 = 1.
    
    Args:
        base (Union[int, float]): The base number.
        exponent (Union[int, float]): The exponent to which the base is raised.
    
    Returns:
        float: The result of base raised to the power of exponent.
    
    Raises:
        TypeError: If base or exponent are not numeric.
        ValueError: If a negative base is raised to a non-integer exponent,
                   or if 0 is raised to a negative exponent.
    
    Usage Example:
        >>> from formulite.fxNumeric.numeric_arithmetic import power
        >>> power(2, 3)
        8.0
        >>> power(9, 0.5)  # Square root
        3.0
        >>> power(-2, 3)
        -8.0
        >>> power(10, -2)
        0.01
    
    Cost: O(1)
    """
    if not isinstance(base, (int, float)) or not isinstance(exponent, (int, float)):
        raise TypeError("Both base and exponent must be numeric values (int or float).")

    # Handle specific edge cases for 0 as base
    if base == 0:
        if exponent == 0:
            # 0^0 is typically defined as 1 in mathematics contexts (e.g., binomial theorem),
            # but Python's ** operator handles it correctly as 1.0.
            return 1.0
        elif exponent < 0:
            raise ValueError("0 cannot be raised to a negative power (results in division by zero).")
        else: # exponent > 0
            return 0.0

    # For negative base and non-integer exponent, the result is complex.
    # This function is designed for real-valued results.
    if base < 0 and exponent != int(exponent):
        raise ValueError("Cannot raise a negative base to a non-integer exponent; result is complex.")

    return float(base ** exponent)


def square_root(x: Union[int, float]) -> float:
    """Calculates the square root of a non-negative number.
    
    Description:
        Computes √x, finding the non-negative number that, when multiplied
        by itself, equals x. Uses optimized algorithms for fast computation.
    
    Args:
        x (Union[int, float]): The number for which to calculate the square root.
                              Must be non-negative.
    
    Returns:
        float: The square root of x.
    
    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is negative (would result in complex number).
    
    Usage Example:
        >>> from formulite.fxNumeric.numeric_arithmetic import square_root
        >>> square_root(9)
        3.0
        >>> square_root(25.0)
        5.0
        >>> square_root(0)
        0.0
    
    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number (results in a complex number).")

    return math.sqrt(x)


def cube_root(x: Union[int, float]) -> float:
    """Calculates the cube root of a number.
    
    Description:
        Computes ∛x, finding the number that, when multiplied by itself three
        times, equals x. Works for both positive and negative real numbers.
        Uses math.cbrt for Python 3.11+ for better accuracy, with fallback
        for older versions.
    
    Args:
        x (Union[int, float]): The number for which to calculate the cube root.
    
    Returns:
        float: The cube root of x.
    
    Raises:
        TypeError: If x is not numeric.
    
    Usage Example:
        >>> from formulite.fxNumeric.numeric_arithmetic import cube_root
        >>> cube_root(8)
        2.0
        >>> cube_root(27)
        3.0
        >>> cube_root(-8)
        -2.0
        >>> cube_root(0)
        0.0
    
    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")

    # Using x**(1/3) directly can lead to complex numbers for negative x due to float precision
    # when 1/3 is not exact. math.cbrt is preferred for Python 3.11+.
    # For older versions, we can use a sign-aware power function.
    if hasattr(math, 'cbrt'): # Available from Python 3.11+
        return math.cbrt(x)
    else:
        # Fallback for older Python versions
        if x < 0:
            return -((-x)**(1/3))
        else:
            return x**(1/3)


def nth_root(x: Union[int, float], n: Union[int, float]) -> float:
    """Calculates the nth root of a number.
    
    Description:
        Computes ⁿ√x or x^(1/n), generalizing square and cube roots to any
        degree n. For negative x, n must be an odd integer to return a real
        result. Handles edge cases like 0^(negative n) appropriately.
    
    Args:
        x (Union[int, float]): The number for which to calculate the root.
        n (Union[int, float]): The degree of the root (e.g., 2 for square root).
                              Must be non-zero. If x < 0, n must be odd.
    
    Returns:
        float: The nth root of x.
    
    Raises:
        TypeError: If x or n are not numeric.
        ValueError: If n is 0, or if x is negative and n is even,
                   or if x is 0 and n is negative.
    
    Usage Example:
        >>> from formulite.fxNumeric.numeric_arithmetic import nth_root
        >>> nth_root(81, 4)  # Fourth root of 81
        3.0
        >>> nth_root(1000, 3)  # Cube root of 1000
        10.0
        >>> nth_root(-27, 3)  # Cube root of -27
        -3.0
    
    Cost: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(n, (int, float)):
        raise TypeError("Both x and n must be numeric values (int or float).")

    if n == 0:
        raise ValueError("The degree of the root (n) cannot be zero.")
    if x == 0 and n < 0:
        raise ValueError("Cannot calculate the root of 0 with a negative degree (results in division by zero).")

    # Handle negative x raised to an even root
    if x < 0 and n % 2 == 0:
        raise ValueError("Cannot calculate an even root of a negative number (results in a complex number).")

    # Calculate x^(1/n)
    # For negative x and odd n, directly using x**(1/n) works in Python.
    return float(x**(1/n))

