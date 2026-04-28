"""Arithmetic operations module.

This module provides fundamental arithmetic operations including logarithms,
exponentiation, root calculations, factorials, combinatorics, special
mathematical functions, and numerical analysis (derivatives, integration,
root finding, polynomial evaluation).
"""

import math
from typing import List, Union, Callable, Tuple


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
        >>> from agentfx.fxNumeric.arithmetic_functions import natural_log
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
        >>> from agentfx.fxNumeric.arithmetic_functions import common_log
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
        >>> from agentfx.fxNumeric.arithmetic_functions import log_base_n
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
        >>> from agentfx.fxNumeric.arithmetic_functions import log1p
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
        >>> from agentfx.fxNumeric.arithmetic_functions import power
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
        >>> from agentfx.fxNumeric.arithmetic_functions import square_root
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
        >>> from agentfx.fxNumeric.arithmetic_functions import cube_root
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
        >>> from agentfx.fxNumeric.arithmetic_functions import nth_root
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


def absolute_value(x: Union[int, float]) -> Union[int, float]:
    """Returns the absolute (non-negative) value of a number.

    Description:
        Computes |x|, removing the sign of the number. Preserves the
        original type (int stays int, float stays float).

    Args:
        x (Union[int, float]): The number.

    Returns:
        Union[int, float]: The absolute value of x.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> absolute_value(-7)
        7
        >>> absolute_value(-3.14)
        3.14
        >>> absolute_value(0)
        0

    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")

    return abs(x)


def sign(x: Union[int, float]) -> int:
    """Returns the sign of a number as -1, 0, or 1.

    Description:
        Returns -1 for negative numbers, 0 for zero, and 1 for positive
        numbers. Useful for branching logic based on value polarity.

    Args:
        x (Union[int, float]): The number to inspect.

    Returns:
        int: -1, 0, or 1.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> sign(-42)
        -1
        >>> sign(0)
        0
        >>> sign(3.14)
        1

    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")

    if x > 0:
        return 1
    elif x < 0:
        return -1

    return 0


def factorial(n: int) -> int:
    """Calculates the factorial of a non-negative integer.

    Description:
        Computes n! = 1 * 2 * 3 * ... * n. Factorial of 0 is 1 by
        convention.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The factorial of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Usage Example:
        >>> factorial(5)
        120
        >>> factorial(0)
        1

    Cost: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if n > 170:
        raise ValueError(
            f"factorial argument {n} exceeds maximum supported (170)."
        )

    return math.factorial(n)


def greatest_common_divisor(a: int, b: int) -> int:
    """Calculates the greatest common divisor (GCD) of two integers.

    Description:
        Computes the largest positive integer that divides both a and b
        without remainder, using the Euclidean algorithm.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The GCD of a and b.

    Raises:
        TypeError: If a or b are not integers.

    Usage Example:
        >>> greatest_common_divisor(12, 8)
        4
        >>> greatest_common_divisor(100, 75)
        25
        >>> greatest_common_divisor(7, 13)
        1

    Cost: O(log(min(a, b)))
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both 'a' and 'b' must be integers.")

    return math.gcd(a, b)


def least_common_multiple(a: int, b: int) -> int:
    """Calculates the least common multiple (LCM) of two integers.

    Description:
        Computes the smallest positive integer that is divisible by
        both a and b. Uses the relationship LCM(a, b) = |a * b| / GCD(a, b).

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The LCM of a and b.

    Raises:
        TypeError: If a or b are not integers.
        ValueError: If both a and b are zero.

    Usage Example:
        >>> least_common_multiple(4, 6)
        12
        >>> least_common_multiple(3, 7)
        21
        >>> least_common_multiple(12, 18)
        36

    Cost: O(log(min(a, b)))
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both 'a' and 'b' must be integers.")

    if a == 0 and b == 0:
        raise ValueError("LCM is not defined when both values are zero.")

    return lcm(a, b)


def double_factorial(n: int) -> int:
    """Calculates the double factorial of a non-negative integer.

    Description:
        Computes n!! = n × (n-2) × (n-4) × ... down to 1 or 2.
        For example, 7!! = 7 × 5 × 3 × 1 = 105 and 6!! = 6 × 4 × 2 = 48.
        By convention, 0!! = 1 and 1!! = 1.

    Args:
        n (int): A non-negative integer.

    Returns:
        int: The double factorial of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import double_factorial
        >>> double_factorial(7)
        105
        >>> double_factorial(6)
        48
        >>> double_factorial(0)
        1

    Cost: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Input 'n' must be an integer.")

    if n < 0:
        raise ValueError("Double factorial is not defined for negative numbers.")

    if n <= 1:
        return 1

    result = 1

    for i in range(n, 0, -2):
        result *= i

    return result


def gamma(x: float) -> float:
    """Calculates the Gamma function Γ(x).

    Description:
        Computes Γ(x), the extension of factorial to real numbers.
        For positive integers, Γ(n) = (n-1)!. The Gamma function is
        defined for all real numbers except non-positive integers.

    Args:
        x (float): A real number (not zero or a negative integer).

    Returns:
        float: The value of the Gamma function at x.

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is zero or a negative integer.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import gamma
        >>> gamma(5)
        24.0
        >>> round(gamma(0.5), 10)
        1.7724538509

    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")

    if x <= 0 and x == int(x):
        raise ValueError("Gamma function is not defined for zero or negative integers.")

    return math.gamma(x)


def log_gamma(x: float) -> float:
    """Calculates the natural logarithm of the absolute value of Γ(x).

    Description:
        Computes ln|Γ(x)|, useful when Γ(x) is too large for direct
        computation but its logarithm is needed (e.g., in combinatorics
        and statistical distributions).

    Args:
        x (float): A positive real number.

    Returns:
        float: The natural logarithm of the absolute Gamma function at x.

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is not positive.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import log_gamma
        >>> round(log_gamma(5), 10)
        3.1780538303

    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")

    if x <= 0:
        raise ValueError("log_gamma requires a positive argument.")

    return math.lgamma(x)


def lcm(a: int, b: int) -> int:
    """Calculates the Least Common Multiple of two integers.

    Description:
        Computes LCM(a, b) = |a × b| / GCD(a, b). The LCM is the smallest
        positive integer that is divisible by both a and b.

    Args:
        a (int): First integer.
        b (int): Second integer.

    Returns:
        int: The least common multiple of a and b.

    Raises:
        TypeError: If a or b are not integers.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import lcm
        >>> lcm(4, 6)
        12
        >>> lcm(3, 7)
        21
        >>> lcm(0, 5)
        0

    Cost: O(log(min(a, b)))
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both 'a' and 'b' must be integers.")

    return math.lcm(a, b)


def gcd_list(numbers: List[int]) -> int:
    """Calculates the GCD of a list of integers.

    Description:
        Computes the Greatest Common Divisor of all integers in the list
        by iteratively applying GCD pairwise.

    Args:
        numbers (List[int]): A list of integers (at least one element).

    Returns:
        int: The GCD of all numbers in the list.

    Raises:
        TypeError: If input is not a list or contains non-integers.
        ValueError: If the list is empty.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import gcd_list
        >>> gcd_list([12, 18, 24])
        6
        >>> gcd_list([7, 14, 21])
        7

    Cost: O(n × log(min))
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    if not numbers:
        raise ValueError("Input list cannot be empty.")

    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("All elements must be integers.")

    return math.gcd(*numbers)


def lcm_list(numbers: List[int]) -> int:
    """Calculates the LCM of a list of integers.

    Description:
        Computes the Least Common Multiple of all integers in the list
        by iteratively applying LCM pairwise.

    Args:
        numbers (List[int]): A list of integers (at least one element).

    Returns:
        int: The LCM of all numbers in the list.

    Raises:
        TypeError: If input is not a list or contains non-integers.
        ValueError: If the list is empty.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import lcm_list
        >>> lcm_list([4, 6, 10])
        60
        >>> lcm_list([3, 5, 7])
        105

    Cost: O(n × log(min))
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    if not numbers:
        raise ValueError("Input list cannot be empty.")

    if not all(isinstance(n, int) for n in numbers):
        raise TypeError("All elements must be integers.")

    return math.lcm(*numbers)


def exp(x: float) -> float:
    """Calculates e raised to the power of x.

    Description:
        Computes e^x where e is Euler's number (≈ 2.71828). Uses the
        optimized ``math.exp`` for numerical stability.

    Args:
        x (float): The exponent.

    Returns:
        float: The value of e^x.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import exp
        >>> round(exp(1), 10)
        2.7182818285
        >>> exp(0)
        1.0

    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")

    return math.exp(x)


def expm1(x: float) -> float:
    """Calculates e^x - 1 with high precision for small x.

    Description:
        Computes e^x - 1 accurately for values of x close to zero,
        where direct computation of exp(x) - 1 would lose precision.
        Complementary to ``log1p``.

    Args:
        x (float): The exponent value.

    Returns:
        float: The value of e^x - 1.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import expm1
        >>> expm1(0)
        0.0
        >>> round(expm1(1e-10), 20)
        1e-10

    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")

    return math.expm1(x)


def error_function(x: float) -> float:
    """Calculates the error function erf(x).

    Description:
        Computes the Gauss error function, commonly used in probability,
        statistics, and partial differential equations. Values range
        from -1 to 1.

    Args:
        x (float): A real number.

    Returns:
        float: The error function value at x.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import error_function
        >>> error_function(0)
        0.0
        >>> round(error_function(1), 10)
        0.8427007929

    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")

    return math.erf(x)


def complementary_error_function(x: float) -> float:
    """Calculates the complementary error function erfc(x) = 1 - erf(x).

    Description:
        Computes 1 - erf(x) with high accuracy, especially for large x
        where direct subtraction would lose precision. Commonly used in
        statistics and signal processing.

    Args:
        x (float): A real number.

    Returns:
        float: The complementary error function value at x.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import complementary_error_function
        >>> complementary_error_function(0)
        1.0
        >>> round(complementary_error_function(1), 10)
        0.1572992071

    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")

    return math.erfc(x)


def combinations(n: int, k: int) -> int:
    """Calculates the number of combinations C(n, k).

    Description:
        Computes the binomial coefficient "n choose k", the number of
        ways to choose k items from n items without regard to order.
        C(n, k) = n! / (k! × (n-k)!)

    Args:
        n (int): Total number of items (non-negative).
        k (int): Number of items to choose (0 ≤ k ≤ n).

    Returns:
        int: The number of combinations.

    Raises:
        TypeError: If n or k are not integers.
        ValueError: If n or k are negative, or if k > n.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import combinations
        >>> combinations(10, 3)
        120
        >>> combinations(5, 0)
        1

    Cost: O(min(k, n-k))
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both 'n' and 'k' must be integers.")

    if n < 0 or k < 0:
        raise ValueError("Both 'n' and 'k' must be non-negative.")

    if k > n:
        raise ValueError("'k' cannot be greater than 'n'.")

    return math.comb(n, k)


def permutations(n: int, k: int) -> int:
    """Calculates the number of permutations P(n, k).

    Description:
        Computes the number of ways to arrange k items from n items
        where order matters. P(n, k) = n! / (n-k)!

    Args:
        n (int): Total number of items (non-negative).
        k (int): Number of items to arrange (0 ≤ k ≤ n).

    Returns:
        int: The number of permutations.

    Raises:
        TypeError: If n or k are not integers.
        ValueError: If n or k are negative, or if k > n.

    Usage Example:
        >>> from agentfx.fxNumeric.arithmetic_functions import permutations
        >>> permutations(5, 3)
        60
        >>> permutations(4, 4)
        24

    Cost: O(k)
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both 'n' and 'k' must be integers.")

    if n < 0 or k < 0:
        raise ValueError("Both 'n' and 'k' must be non-negative.")

    if k > n:
        raise ValueError("'k' cannot be greater than 'n'.")

    return math.perm(n, k)


def fibonacci(n: int) -> int:
    """Returns the n-th Fibonacci number (0-indexed).

    Uses iterative computation for efficiency and avoids recursion limits.

    Args:
        n: The position in the Fibonacci sequence (must be >= 0).

    Returns:
        The n-th Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Usage Example:
        >>> fibonacci(0)
        0
        >>> fibonacci(1)
        1
        >>> fibonacci(10)
        55
        >>> fibonacci(20)
        6765

    Cost: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("'n' must be an integer.")

    if n < 0:
        raise ValueError("'n' must be non-negative.")

    if n <= 1:
        return n

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


# ---------------------------------------------------------------------------
# Excel-compatible arithmetic helpers
# ---------------------------------------------------------------------------


def quotient(dividend: Union[int, float],
             divisor: Union[int, float]) -> int:
    """Return the integer portion of a division (truncated toward zero).

    Equivalent to Excel's QUOTIENT function.

    Args:
        dividend: The number to be divided.
        divisor: The number to divide by.

    Returns:
        Integer result of division truncated toward zero.

    Raises:
        ZeroDivisionError: If divisor is 0.

    Example:
        >>> quotient(7, 2)
        3
        >>> quotient(-7, 2)
        -3

    Complexity: O(1)
    """

    if divisor == 0:
        raise ZeroDivisionError("divisor must not be zero.")

    return int(dividend / divisor)


def multinomial_coefficient(*args: int) -> int:
    """Compute the multinomial coefficient n! / (k1! * k2! * ... * km!).

    Where n = sum(args). Equivalent to Excel's MULTINOMIAL.

    Args:
        *args: Non-negative integers k1, k2, ..., km.

    Returns:
        Multinomial coefficient as integer.

    Raises:
        ValueError: If any argument is negative.

    Example:
        >>> multinomial_coefficient(2, 3, 4)
        1260
        >>> multinomial_coefficient(5)
        1

    Complexity: O(sum(args))
    """

    for k in args:

        if k < 0:
            raise ValueError(f"All arguments must be non-negative, got {k}.")

    n = sum(args)

    if n > 170:
        raise ValueError(
            f"Sum of arguments ({n}) exceeds maximum factorial input (170)."
        )

    result = math.factorial(n)

    for k in args:
        result //= math.factorial(k)

    return result


def series_sum(x: float, n: int, m: int,
               coefficients: List[Union[int, float]]) -> float:
    """Compute a power series sum: sum(a_i * x^(n + i*m)).

    Equivalent to Excel's SERIESSUM.

    Args:
        x: Base value.
        n: Initial power of x.
        m: Step increment for each term's power.
        coefficients: List of coefficients [a_0, a_1, ...].

    Returns:
        Sum of the power series.

    Example:
        >>> series_sum(2, 0, 1, [1, 2, 3])
        17.0
        >>> series_sum(3, 1, 2, [1, 1])
        30.0

    Complexity: O(len(coefficients))
    """

    return float(sum(
        a * (x ** (n + i * m)) for i, a in enumerate(coefficients)
    ))


# ---------------------------------------------------------------------------
# Division and modulo helpers
# ---------------------------------------------------------------------------


def force_float_division(numerator: Union[int, float], denominator: Union[int, float]) -> float:
    """Performs division ensuring the result is always a float.

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

    **Cost:** O(1), arithmetic division.
    """
    return true_division(numerator, denominator)


def true_division(numerator: Union[int, float], denominator: Union[int, float]) -> float:
    """Performs "true" (floating-point) division, always returning a float.

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
        >>> true_division(6, 2)
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
        Union[int, float]: The integer part of the quotient.

    Raises:
        ZeroDivisionError: If the divisor is zero.

    Example:
        >>> floor_division(5, 2)
        2
        >>> floor_division(-5, 2)
        -3

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
    """Performs division selecting the appropriate operator based on context.

    Args:
        numerator (Union[int, float]): The dividend.
        denominator (Union[int, float]): The divisor.
        return_float (bool): If True, performs float division; if False, floor division.

    Returns:
        Union[int, float]: The division result.

    Raises:
        ZeroDivisionError: If the divisor is zero.

    Example:
        >>> safe_division_for_context(5, 2, return_float=True)
        2.5
        >>> safe_division_for_context(5, 2, return_float=False)
        2

    **Cost:** O(1), division according to specified type.
    """
    if denominator == 0:
        raise ZeroDivisionError("Cannot divide by zero.")

    if return_float:
        return numerator / denominator
    else:
        return numerator // denominator


def modulo(number: Union[int, float], divisor: Union[int, float]) -> Union[int, float]:
    """Returns the remainder after dividing number by divisor.

    Args:
        number: The dividend.
        divisor: The divisor (must not be zero).

    Returns:
        The remainder of number / divisor.

    Raises:
        ZeroDivisionError: If divisor is zero.

    Example:
        >>> modulo(10, 3)
        1
        >>> modulo(7.5, 2.0)
        1.5

    Complexity: O(1)
    """
    if divisor == 0:
        raise ZeroDivisionError("Divisor cannot be zero.")

    return number % divisor


def sqrt_pi(number: float) -> float:
    """Calculates the square root of (number * pi).

    Args:
        number: A non-negative number.

    Returns:
        sqrt(number * pi).

    Raises:
        ValueError: If number is negative.

    Example:
        >>> round(sqrt_pi(1), 6)
        1.772454
        >>> round(sqrt_pi(2), 6)
        2.506628

    Complexity: O(1)
    """
    if number < 0:
        raise ValueError("Input must be non-negative.")

    return math.sqrt(number * math.pi)


def safe_sum_with_none(num1: Union[int, float, None], num2: Union[int, float, None]) -> Union[int, float]:
    """Performs addition of two numbers, safely handling None values.

    Each argument is verified; None is replaced with 0.

    Args:
        num1 (Union[int, float, None]): The first number (or None).
        num2 (Union[int, float, None]): The second number (or None).

    Returns:
        Union[int, float]: The result of the addition.

    Example:
        >>> safe_sum_with_none(3, 5)
        8
        >>> safe_sum_with_none(3, None)
        3
        >>> safe_sum_with_none(None, None)
        0

    **Cost:** O(1), addition with None handling.
    """
    val1 = num1 if num1 is not None else 0
    val2 = num2 if num2 is not None else 0

    return val1 + val2


def reduce_to_modulo_range(x: Union[int, float], base: Union[int, float]) -> Union[int, float]:
    """Converts a value to a cyclic range using the modulo operation.

    The result will be in the range [0, base) for positive numbers.

    Args:
        x (Union[int, float]): The numeric value to reduce.
        base (Union[int, float]): The cycle base (the range size). Must be positive.

    Returns:
        Union[int, float]: The value reduced to the cyclic range.

    Raises:
        ValueError: If 'base' is zero or negative.

    Example:
        >>> reduce_to_modulo_range(25, 24)
        1
        >>> reduce_to_modulo_range(370, 360)
        10

    **Cost:** O(1), modulo operation.
    """
    if base <= 0:
        raise ValueError("The 'base' must be a positive number.")

    return modulo(x, base)


def combinations_with_repetition(n: int, k: int) -> int:
    """Calculates combinations with repetition (multiset coefficient).

    C(n+k-1, k) = (n+k-1)! / (k! * (n-1)!)

    Args:
        n: Number of types to choose from.
        k: Number of items to choose.

    Returns:
        Number of combinations with repetition.

    Raises:
        TypeError: If n or k are not integers.
        ValueError: If n < 1 or k < 0.

    Example:
        >>> combinations_with_repetition(3, 2)
        6
        >>> combinations_with_repetition(4, 3)
        20

    Complexity: O(1)
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both 'n' and 'k' must be integers.")

    if n < 1:
        raise ValueError("'n' must be at least 1.")

    if k < 0:
        raise ValueError("'k' must be non-negative.")

    return math.comb(n + k - 1, k)


def product_list(data: List[Union[int, float]]) -> Union[int, float]:
    """Calculates the product of all values in a list.

    Args:
        data: A list of numeric values.

    Returns:
        The product of all values.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> product_list([1, 2, 3, 4])
        24
        >>> product_list([2.0, 3.0])
        6.0

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

    return math.prod(data)


def matrix_determinant(matrix: List[List[float]]) -> float:
    """Computes the determinant of a square matrix.

    Description:
        Calculates the determinant using LU decomposition via recursive
        cofactor expansion. Equivalent to Excel MDETERM.

    Args:
        matrix: A square matrix represented as a list of lists.

    Returns:
        The determinant value.

    Raises:
        TypeError: If input is not a list of lists of numbers.
        ValueError: If the matrix is not square or is empty.

    Example:
        >>> matrix_determinant([[1, 2], [3, 4]])
        -2.0
        >>> matrix_determinant([[6, 1, 1], [4, -2, 5], [2, 8, 7]])
        -306.0

    Complexity: O(n^3)
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a list of lists.")

    n = len(matrix)

    if n == 0:
        raise ValueError("Matrix cannot be empty.")

    for row in matrix:

        if len(row) != n:
            raise ValueError("Matrix must be square.")

        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("All matrix elements must be numeric.")

    # Base cases
    if n == 1:
        return float(matrix[0][0])

    if n == 2:
        return float(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])

    # LU decomposition approach for efficiency
    # Copy matrix to avoid mutation
    a = [row[:] for row in matrix]
    det = 1.0

    for col in range(n):
        # Partial pivoting
        max_row = col

        for row in range(col + 1, n):

            if abs(a[row][col]) > abs(a[max_row][col]):
                max_row = row

        if max_row != col:
            a[col], a[max_row] = a[max_row], a[col]
            det *= -1

        if a[col][col] == 0:
            return 0.0

        det *= a[col][col]

        for row in range(col + 1, n):
            factor = a[row][col] / a[col][col]

            for k in range(col + 1, n):
                a[row][k] -= factor * a[col][k]

    return det


def matrix_inverse(matrix: List[List[float]]) -> List[List[float]]:
    """Computes the inverse of a square matrix.

    Description:
        Calculates the matrix inverse using Gauss-Jordan elimination
        with partial pivoting. Equivalent to Excel MINVERSE.

    Args:
        matrix: A square, non-singular matrix as a list of lists.

    Returns:
        The inverse matrix as a list of lists of floats.

    Raises:
        TypeError: If input is not a list of lists of numbers.
        ValueError: If the matrix is not square, empty, or singular.

    Example:
        >>> result = matrix_inverse([[4, 7], [2, 6]])
        >>> [[round(x, 4) for x in row] for row in result]
        [[0.6, -0.7], [-0.2, 0.4]]

    Complexity: O(n^3)
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a list of lists.")

    n = len(matrix)

    if n == 0:
        raise ValueError("Matrix cannot be empty.")

    for row in matrix:

        if len(row) != n:
            raise ValueError("Matrix must be square.")

        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("All matrix elements must be numeric.")

    # Augmented matrix [A | I]
    aug = [row[:] + [1.0 if i == j else 0.0 for j in range(n)] for i, row in enumerate(matrix)]

    for col in range(n):
        # Partial pivoting
        max_row = col

        for row in range(col + 1, n):

            if abs(aug[row][col]) > abs(aug[max_row][col]):
                max_row = row

        aug[col], aug[max_row] = aug[max_row], aug[col]

        if abs(aug[col][col]) < 1e-12:
            raise ValueError("Matrix is singular and cannot be inverted.")

        # Scale pivot row
        pivot = aug[col][col]

        for j in range(2 * n):
            aug[col][j] /= pivot

        # Eliminate column
        for row in range(n):

            if row == col:
                continue

            factor = aug[row][col]

            for j in range(2 * n):
                aug[row][j] -= factor * aug[col][j]

    return [row[n:] for row in aug]


def matrix_multiply(
    matrix_a: List[List[float]], matrix_b: List[List[float]]
) -> List[List[float]]:
    """Multiplies two matrices.

    Description:
        Performs matrix multiplication A × B. The number of columns in A
        must equal the number of rows in B. Equivalent to Excel MMULT.

    Args:
        matrix_a: First matrix (m × n).
        matrix_b: Second matrix (n × p).

    Returns:
        The resulting matrix (m × p) as a list of lists.

    Raises:
        TypeError: If inputs are not lists of lists of numbers.
        ValueError: If matrices are empty or dimensions are incompatible.

    Example:
        >>> matrix_multiply([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]

    Complexity: O(m × n × p)
    """
    if (
        not isinstance(matrix_a, list)
        or not isinstance(matrix_b, list)
        or not all(isinstance(r, list) for r in matrix_a)
        or not all(isinstance(r, list) for r in matrix_b)
    ):
        raise TypeError("Both inputs must be lists of lists.")

    if not matrix_a or not matrix_b or not matrix_a[0] or not matrix_b[0]:
        raise ValueError("Matrices cannot be empty.")

    rows_a, cols_a = len(matrix_a), len(matrix_a[0])
    rows_b, cols_b = len(matrix_b), len(matrix_b[0])

    for row in matrix_a:

        if len(row) != cols_a:
            raise ValueError("All rows in matrix_a must have the same length.")

        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("All matrix elements must be numeric.")

    for row in matrix_b:

        if len(row) != cols_b:
            raise ValueError("All rows in matrix_b must have the same length.")

        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("All matrix elements must be numeric.")

    if cols_a != rows_b:
        raise ValueError(
            f"Incompatible dimensions: matrix_a has {cols_a} columns, "
            f"matrix_b has {rows_b} rows."
        )

    result = [[0.0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):

        for j in range(cols_b):

            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result


def identity_matrix(size: int) -> List[List[float]]:
    """Creates an identity matrix of the given size.

    Description:
        Returns an n × n identity matrix with 1.0 on the main diagonal
        and 0.0 elsewhere. Equivalent to Excel MUNIT.

    Args:
        size: The dimension of the square identity matrix.

    Returns:
        An identity matrix as a list of lists.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 1.

    Example:
        >>> identity_matrix(3)
        [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]

    Complexity: O(n^2)
    """
    if not isinstance(size, int):
        raise TypeError("Size must be an integer.")

    if size < 1:
        raise ValueError("Size must be at least 1.")

    return [[1.0 if i == j else 0.0 for j in range(size)] for i in range(size)]


def delta(number_1: float, number_2: float = 0) -> int:
    """Tests whether two values are equal (Kronecker delta).

    Description:
        Returns 1 if number_1 equals number_2, otherwise 0.
        Equivalent to Excel DELTA.

    Args:
        number_1: The first number.
        number_2: The second number (defaults to 0).

    Returns:
        1 if the values are equal, 0 otherwise.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> delta(5, 5)
        1
        >>> delta(5, 4)
        0
        >>> delta(0)
        1

    Complexity: O(1)
    """
    if not isinstance(number_1, (int, float)) or not isinstance(number_2, (int, float)):
        raise TypeError("Both arguments must be numeric.")

    return 1 if number_1 == number_2 else 0


def gestep(number: float, step: float = 0) -> int:
    """Tests whether a number is greater than or equal to a step value.

    Description:
        Returns 1 if number >= step, otherwise 0. Implements the
        Heaviside step function. Equivalent to Excel GESTEP.

    Args:
        number: The value to test.
        step: The threshold value (defaults to 0).

    Returns:
        1 if number >= step, 0 otherwise.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> gestep(5, 4)
        1
        >>> gestep(3, 4)
        0
        >>> gestep(0)
        1

    Complexity: O(1)
    """
    if not isinstance(number, (int, float)) or not isinstance(step, (int, float)):
        raise TypeError("Both arguments must be numeric.")

    return 1 if number >= step else 0


def bitwise_and(a: int, b: int) -> int:
    """Returns the bitwise AND of two non-negative integers.

    Description:
        Performs a bitwise AND operation. Equivalent to Excel BITAND.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.

    Returns:
        The bitwise AND result.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If inputs are negative.

    Example:
        >>> bitwise_and(13, 25)
        9
        >>> bitwise_and(0b1100, 0b1010)
        8

    Complexity: O(1)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")

    if a < 0 or b < 0:
        raise ValueError("Both arguments must be non-negative.")

    return a & b


def bitwise_or(a: int, b: int) -> int:
    """Returns the bitwise OR of two non-negative integers.

    Description:
        Performs a bitwise OR operation. Equivalent to Excel BITOR.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.

    Returns:
        The bitwise OR result.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If inputs are negative.

    Example:
        >>> bitwise_or(13, 25)
        29
        >>> bitwise_or(0b1100, 0b1010)
        14

    Complexity: O(1)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")

    if a < 0 or b < 0:
        raise ValueError("Both arguments must be non-negative.")

    return a | b


def bitwise_xor(a: int, b: int) -> int:
    """Returns the bitwise XOR of two non-negative integers.

    Description:
        Performs a bitwise exclusive OR operation. Equivalent to Excel BITXOR.

    Args:
        a: First non-negative integer.
        b: Second non-negative integer.

    Returns:
        The bitwise XOR result.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If inputs are negative.

    Example:
        >>> bitwise_xor(13, 25)
        20
        >>> bitwise_xor(0b1100, 0b1010)
        6

    Complexity: O(1)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")

    if a < 0 or b < 0:
        raise ValueError("Both arguments must be non-negative.")

    return a ^ b


def bitwise_not(number: int, bit_width: int = 32) -> int:
    """Returns the bitwise NOT of a non-negative integer within a given bit width.

    Description:
        Flips all bits of the number within the specified bit width.
        Equivalent to Excel BITNOT.

    Args:
        number: A non-negative integer.
        bit_width: The number of bits to consider (default 32).

    Returns:
        The bitwise NOT result within the bit width.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If number is negative or bit_width < 1.

    Example:
        >>> bitwise_not(0, 8)
        255
        >>> bitwise_not(13, 8)
        242

    Complexity: O(1)
    """
    if not isinstance(number, int) or not isinstance(bit_width, int):
        raise TypeError("Both arguments must be integers.")

    if number < 0:
        raise ValueError("Number must be non-negative.")

    if bit_width < 1:
        raise ValueError("Bit width must be at least 1.")

    mask = (1 << bit_width) - 1
    return number ^ mask


def bit_count(number: int) -> int:
    """Counts the number of set bits (1-bits) in a non-negative integer.

    Description:
        Returns the population count (Hamming weight). Equivalent to
        Excel BITCOUNT.

    Args:
        number: A non-negative integer.

    Returns:
        The number of 1-bits.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.

    Example:
        >>> bit_count(13)
        3
        >>> bit_count(255)
        8
        >>> bit_count(0)
        0

    Complexity: O(1)
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    if number < 0:
        raise ValueError("Input must be non-negative.")

    return bin(number).count("1")


def sum_x2my2(
    array_x: List[Union[int, float]], array_y: List[Union[int, float]]
) -> float:
    """Returns the sum of the difference of squares of corresponding values.

    Description:
        Computes Σ(xᵢ² - yᵢ²) for paired arrays.
        Equivalent to Excel SUMX2MY2.

    Args:
        array_x: First array of numbers.
        array_y: Second array of numbers (same length as array_x).

    Returns:
        The sum of xᵢ² - yᵢ² for each pair.

    Raises:
        ValueError: If arrays have different lengths or are empty.

    Example:
        >>> sum_x2my2([2, 3, 9, 1, 8], [6, 5, 11, 7, 5])
        -55
        >>> sum_x2my2([1, 2], [3, 4])
        -20.0

    Complexity: O(n)
    """
    if len(array_x) != len(array_y):
        raise ValueError("Arrays must have the same length.")

    if not array_x:
        raise ValueError("Arrays cannot be empty.")

    return float(sum(x ** 2 - y ** 2 for x, y in zip(array_x, array_y)))


def sum_x2py2(
    array_x: List[Union[int, float]], array_y: List[Union[int, float]]
) -> float:
    """Returns the sum of the sum of squares of corresponding values.

    Description:
        Computes Σ(xᵢ² + yᵢ²) for paired arrays.
        Equivalent to Excel SUMX2PY2.

    Args:
        array_x: First array of numbers.
        array_y: Second array of numbers (same length as array_x).

    Returns:
        The sum of xᵢ² + yᵢ² for each pair.

    Raises:
        ValueError: If arrays have different lengths or are empty.

    Example:
        >>> sum_x2py2([2, 3, 9, 1, 8], [6, 5, 11, 7, 5])
        521
        >>> sum_x2py2([1, 2], [3, 4])
        30.0

    Complexity: O(n)
    """
    if len(array_x) != len(array_y):
        raise ValueError("Arrays must have the same length.")

    if not array_x:
        raise ValueError("Arrays cannot be empty.")

    return float(sum(x ** 2 + y ** 2 for x, y in zip(array_x, array_y)))


def sum_xmy2(
    array_x: List[Union[int, float]], array_y: List[Union[int, float]]
) -> float:
    """Returns the sum of squares of differences of corresponding values.

    Description:
        Computes Σ(xᵢ - yᵢ)² for paired arrays.
        Equivalent to Excel SUMXMY2.

    Args:
        array_x: First array of numbers.
        array_y: Second array of numbers (same length as array_x).

    Returns:
        The sum of (xᵢ - yᵢ)² for each pair.

    Raises:
        ValueError: If arrays have different lengths or are empty.

    Example:
        >>> sum_xmy2([2, 3, 9, 1, 8], [6, 5, 11, 7, 5])
        79
        >>> sum_xmy2([1, 2], [3, 4])
        8.0

    Complexity: O(n)
    """
    if len(array_x) != len(array_y):
        raise ValueError("Arrays must have the same length.")

    if not array_x:
        raise ValueError("Arrays cannot be empty.")

    return float(sum((x - y) ** 2 for x, y in zip(array_x, array_y)))


def permutations_with_repetition(n: int, k: int) -> int:
    """Returns the number of permutations with repetition.

    Description:
        Computes n^k — the number of ways to arrange k items chosen from
        n items where repetition is allowed. Equivalent to Excel PERMUTATIONA.

    Args:
        n: The number of distinct items.
        k: The number of items to choose.

    Returns:
        n raised to the power k.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If n or k is negative, or n is 0 and k > 0.

    Example:
        >>> permutations_with_repetition(3, 2)
        9
        >>> permutations_with_repetition(10, 3)
        1000

    Complexity: O(log k) via exponentiation
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("Both arguments must be integers.")

    if n < 0 or k < 0:
        raise ValueError("Both arguments must be non-negative.")

    if n == 0 and k > 0:
        raise ValueError("n must be positive when k > 0.")

    return n ** k


def bessel_i(x: float, n: int) -> float:
    """Modified Bessel function of the first kind, order n.

    Description:
        Returns Iₙ(x). Equivalent to Excel BESSELI.

    Args:
        x: Value at which to evaluate.
        n: Non-negative integer order.

    Returns:
        float: Iₙ(x).

    Raises:
        TypeError: If x is not numeric or n is not int.
        ValueError: If n < 0.

    Example:
        >>> round(bessel_i(1.5, 1), 6)
        0.981666

    Complexity: O(1) — delegates to scipy
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    from scipy.special import iv

    return float(iv(n, x))


def bessel_j(x: float, n: int) -> float:
    """Bessel function of the first kind, order n.

    Description:
        Returns Jₙ(x). Equivalent to Excel BESSELJ.

    Args:
        x: Value at which to evaluate.
        n: Non-negative integer order.

    Returns:
        float: Jₙ(x).

    Raises:
        TypeError: If x is not numeric or n is not int.
        ValueError: If n < 0.

    Example:
        >>> round(bessel_j(1.9, 2), 6)
        0.329926

    Complexity: O(1) — delegates to scipy
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    from scipy.special import jv

    return float(jv(n, x))


def bessel_k(x: float, n: int) -> float:
    """Modified Bessel function of the second kind, order n.

    Description:
        Returns Kₙ(x). Equivalent to Excel BESSELK.

    Args:
        x: Positive value at which to evaluate.
        n: Non-negative integer order.

    Returns:
        float: Kₙ(x).

    Raises:
        TypeError: If x is not numeric or n is not int.
        ValueError: If n < 0 or x ≤ 0.

    Example:
        >>> round(bessel_k(1.5, 1), 6)
        0.277388

    Complexity: O(1) — delegates to scipy
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    if x <= 0:
        raise ValueError("x must be positive for BESSELK.")

    from scipy.special import kv

    return float(kv(n, x))


def bessel_y(x: float, n: int) -> float:
    """Bessel function of the second kind, order n.

    Description:
        Returns Yₙ(x). Equivalent to Excel BESSELY.

    Args:
        x: Positive value at which to evaluate.
        n: Non-negative integer order.

    Returns:
        float: Yₙ(x).

    Raises:
        TypeError: If x is not numeric or n is not int.
        ValueError: If n < 0 or x ≤ 0.

    Example:
        >>> round(bessel_y(2.5, 1), 6)
        0.145918

    Complexity: O(1) — delegates to scipy
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    if x <= 0:
        raise ValueError("x must be positive for BESSELY.")

    from scipy.special import yv

    return float(yv(n, x))


def bit_lshift(number: int, shift_amount: int) -> int:
    """Shift number left by shift_amount bits.

    Description:
        Returns number × 2^shift_amount. Equivalent to Excel BITLSHIFT.

    Args:
        number: Non-negative integer (0 to 2^48 - 1).
        shift_amount: Number of bit positions to shift (can be negative).

    Returns:
        int: Left-shifted result.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If number < 0 or number > 2^48 - 1.

    Example:
        >>> bit_lshift(4, 2)
        16

    Complexity: O(1)
    """
    if not isinstance(number, int) or not isinstance(shift_amount, int):
        raise TypeError("Both arguments must be integers.")

    if number < 0 or number > (2**48 - 1):
        raise ValueError("number must be between 0 and 2^48 - 1.")

    if shift_amount < 0:
        return number >> (-shift_amount)

    return number << shift_amount


def bit_rshift(number: int, shift_amount: int) -> int:
    """Shift number right by shift_amount bits.

    Description:
        Returns number ÷ 2^shift_amount (integer). Equivalent to Excel BITRSHIFT.

    Args:
        number: Non-negative integer (0 to 2^48 - 1).
        shift_amount: Number of bit positions to shift (can be negative).

    Returns:
        int: Right-shifted result.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If number < 0 or number > 2^48 - 1.

    Example:
        >>> bit_rshift(13, 2)
        3

    Complexity: O(1)
    """
    if not isinstance(number, int) or not isinstance(shift_amount, int):
        raise TypeError("Both arguments must be integers.")

    if number < 0 or number > (2**48 - 1):
        raise ValueError("number must be between 0 and 2^48 - 1.")

    if shift_amount < 0:
        return number << (-shift_amount)

    return number >> shift_amount


def matrix_transpose(matrix: List[List[float]]) -> List[List[float]]:
    """Transposes a matrix (swaps rows and columns).

    Args:
        matrix: A non-empty rectangular matrix as a list of lists.

    Returns:
        The transposed matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is empty or rows have inconsistent lengths.

    Example:
        >>> matrix_transpose([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]

    Complexity: O(m * n)
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a list of lists.")

    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty.")

    row_len = len(matrix[0])

    if any(len(row) != row_len for row in matrix):
        raise ValueError("All rows must have the same length.")

    return [[matrix[r][c] for r in range(len(matrix))] for c in range(row_len)]


def dot_product(
    vec_a: List[Union[int, float]],
    vec_b: List[Union[int, float]],
) -> float:
    """Computes the dot product of two vectors.

    result = Σ(aᵢ × bᵢ).

    Args:
        vec_a: First numeric vector.
        vec_b: Second numeric vector (same length).

    Returns:
        The scalar dot product.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If vectors are empty or have different lengths.

    Example:
        >>> dot_product([1, 2, 3], [4, 5, 6])
        32

    Complexity: O(n)
    """
    if not isinstance(vec_a, list) or not isinstance(vec_b, list):
        raise TypeError("Both inputs must be lists.")

    if not vec_a or not vec_b:
        raise ValueError("Vectors cannot be empty.")

    if len(vec_a) != len(vec_b):
        raise ValueError("Vectors must have the same length.")

    if not all(isinstance(v, (int, float)) for v in vec_a):
        raise TypeError("All elements of vec_a must be numeric.")

    if not all(isinstance(v, (int, float)) for v in vec_b):
        raise TypeError("All elements of vec_b must be numeric.")

    return sum(a * b for a, b in zip(vec_a, vec_b))


def cross_product(
    vec_a: List[Union[int, float]],
    vec_b: List[Union[int, float]],
) -> List[float]:
    """Computes the cross product of two 3D vectors.

    a × b = [a₂b₃−a₃b₂, a₃b₁−a₁b₃, a₁b₂−a₂b₁].

    Args:
        vec_a: First 3D vector [x, y, z].
        vec_b: Second 3D vector [x, y, z].

    Returns:
        The resulting 3D cross-product vector.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If vectors are not exactly 3 elements.

    Example:
        >>> cross_product([1, 0, 0], [0, 1, 0])
        [0, 0, 1]

    Complexity: O(1)
    """
    if not isinstance(vec_a, list) or not isinstance(vec_b, list):
        raise TypeError("Both inputs must be lists.")

    if len(vec_a) != 3 or len(vec_b) != 3:
        raise ValueError("Both vectors must have exactly 3 elements.")

    if not all(isinstance(v, (int, float)) for v in vec_a):
        raise TypeError("All elements of vec_a must be numeric.")

    if not all(isinstance(v, (int, float)) for v in vec_b):
        raise TypeError("All elements of vec_b must be numeric.")

    return [
        vec_a[1] * vec_b[2] - vec_a[2] * vec_b[1],
        vec_a[2] * vec_b[0] - vec_a[0] * vec_b[2],
        vec_a[0] * vec_b[1] - vec_a[1] * vec_b[0],
    ]


def vector_magnitude(vec: List[Union[int, float]]) -> float:
    """Computes the Euclidean magnitude (L2 norm) of a vector.

    ‖v‖ = √(Σvᵢ²).

    Args:
        vec: A numeric vector.

    Returns:
        The magnitude as a non-negative float.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If vector is empty.

    Example:
        >>> vector_magnitude([3, 4])
        5.0

    Complexity: O(n)
    """
    if not isinstance(vec, list):
        raise TypeError("Input must be a list.")

    if not vec:
        raise ValueError("Vector cannot be empty.")

    if not all(isinstance(v, (int, float)) for v in vec):
        raise TypeError("All elements must be numeric.")

    return math.sqrt(sum(v * v for v in vec))


def matrix_trace(matrix: List[List[float]]) -> float:
    """Computes the trace of a square matrix (sum of diagonal elements).

    Args:
        matrix: A square matrix as a list of lists.

    Returns:
        The trace (sum of main diagonal).

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If matrix is empty or not square.

    Example:
        >>> matrix_trace([[1, 2], [3, 4]])
        5

    Complexity: O(n)
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a list of lists.")

    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty.")

    n = len(matrix)

    if any(len(row) != n for row in matrix):
        raise ValueError("Matrix must be square.")

    return sum(matrix[i][i] for i in range(n))


def vector_normalize(vec: List[Union[int, float]]) -> List[float]:
    """Normalizes a vector to unit length (L2 norm = 1).

    Args:
        vec: A numeric vector.

    Returns:
        The unit vector in the same direction.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If vector is empty or is a zero vector.

    Example:
        >>> vector_normalize([3, 4])
        [0.6, 0.8]

    Complexity: O(n)
    """
    if not isinstance(vec, list):
        raise TypeError("Input must be a list.")

    if not vec:
        raise ValueError("Vector cannot be empty.")

    if not all(isinstance(v, (int, float)) for v in vec):
        raise TypeError("All elements must be numeric.")

    mag = math.sqrt(sum(v * v for v in vec))

    if mag == 0:
        raise ValueError("Cannot normalize a zero vector.")

    return [v / mag for v in vec]


def vector_angle(
    vec_a: List[Union[int, float]],
    vec_b: List[Union[int, float]],
) -> float:
    """Computes the angle in radians between two vectors.

    θ = arccos((A · B) / (‖A‖ × ‖B‖)).

    Args:
        vec_a: First numeric vector.
        vec_b: Second numeric vector (same length).

    Returns:
        Angle in radians in [0, π].

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If vectors are empty, different lengths, or either is zero.

    Example:
        >>> import math
        >>> round(vector_angle([1, 0], [0, 1]), 4)
        1.5708

    Complexity: O(n)
    """
    if not isinstance(vec_a, list) or not isinstance(vec_b, list):
        raise TypeError("Both inputs must be lists.")

    if not vec_a or not vec_b:
        raise ValueError("Vectors cannot be empty.")

    if len(vec_a) != len(vec_b):
        raise ValueError("Vectors must have the same length.")

    if not all(isinstance(v, (int, float)) for v in vec_a):
        raise TypeError("All elements of vec_a must be numeric.")

    if not all(isinstance(v, (int, float)) for v in vec_b):
        raise TypeError("All elements of vec_b must be numeric.")

    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    mag_a = math.sqrt(sum(a * a for a in vec_a))
    mag_b = math.sqrt(sum(b * b for b in vec_b))

    if mag_a == 0 or mag_b == 0:
        raise ValueError("Cannot compute angle for a zero vector.")

    cos_theta = max(-1.0, min(1.0, dot / (mag_a * mag_b)))
    return math.acos(cos_theta)


def matrix_add(
    matrix_a: List[List[Union[int, float]]],
    matrix_b: List[List[Union[int, float]]],
) -> List[List[float]]:
    """Adds two matrices element-wise.

    Args:
        matrix_a: First matrix.
        matrix_b: Second matrix (same dimensions).

    Returns:
        The sum matrix.

    Raises:
        TypeError: If inputs are not lists of lists.
        ValueError: If matrices are empty or have different dimensions.

    Example:
        >>> matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[6, 8], [10, 12]]

    Complexity: O(m × n)
    """
    if not isinstance(matrix_a, list) or not isinstance(matrix_b, list):
        raise TypeError("Both inputs must be lists of lists.")

    if not matrix_a or not matrix_a[0]:
        raise ValueError("Matrices cannot be empty.")

    if not all(isinstance(row, list) for row in matrix_a):
        raise TypeError("matrix_a must be a list of lists.")

    if not all(isinstance(row, list) for row in matrix_b):
        raise TypeError("matrix_b must be a list of lists.")

    if len(matrix_a) != len(matrix_b):
        raise ValueError("Matrices must have the same number of rows.")

    if any(len(ra) != len(rb) for ra, rb in zip(matrix_a, matrix_b)):
        raise ValueError("Matrices must have the same dimensions.")

    return [
        [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
        for i in range(len(matrix_a))
    ]


def matrix_scalar_multiply(
    matrix: List[List[Union[int, float]]],
    scalar: Union[int, float],
) -> List[List[float]]:
    """Multiplies every element of a matrix by a scalar.

    Args:
        matrix: A rectangular matrix.
        scalar: The scalar multiplier.

    Returns:
        The scaled matrix.

    Raises:
        TypeError: If matrix is not a list of lists or scalar is not numeric.
        ValueError: If matrix is empty.

    Example:
        >>> matrix_scalar_multiply([[1, 2], [3, 4]], 3)
        [[3, 6], [9, 12]]

    Complexity: O(m × n)
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("Input must be a list of lists.")

    if not isinstance(scalar, (int, float)):
        raise TypeError("scalar must be numeric.")

    if not matrix or not matrix[0]:
        raise ValueError("Matrix cannot be empty.")

    return [
        [matrix[i][j] * scalar for j in range(len(matrix[0]))]
        for i in range(len(matrix))
    ]


# ---------------------------------------------------------------------------
# Numerical analysis — Derivatives, Integration, Root finding, Polynomials
# ---------------------------------------------------------------------------


def numerical_derivative(
    f: Callable[[float], float], x: float, h: float = 1e-8
) -> float:
    """Computes the numerical derivative using the central difference method.

    f'(x) ≈ (f(x+h) − f(x−h)) / (2h)

    Args:
        f: A callable that takes a float and returns a float.
        x: The point at which to evaluate the derivative.
        h: Step size (default 1e-8).

    Returns:
        Approximate value of f'(x).

    Raises:
        TypeError: If f is not callable or x/h are not numeric.
        ValueError: If h is zero.

    Example:
        >>> import math
        >>> round(numerical_derivative(math.sin, 0), 6)
        1.0

    Complexity: O(1) — two function evaluations
    """
    if not callable(f):
        raise TypeError("f must be callable")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")

    if not isinstance(h, (int, float)) or h == 0:
        raise ValueError("h must be a non-zero number")

    return float((f(x + h) - f(x - h)) / (2 * h))


def trapezoidal_integrate(
    f: Callable[[float], float], a: float, b: float, n: int = 1000
) -> float:
    """Numerically integrates f(x) from a to b using the trapezoidal rule.

    Args:
        f: A callable that takes a float and returns a float.
        a: Lower bound of integration.
        b: Upper bound of integration.
        n: Number of sub-intervals (default 1000).

    Returns:
        Approximate value of ∫f(x)dx from a to b.

    Raises:
        TypeError: If f is not callable or bounds/n have wrong types.
        ValueError: If n is not positive.

    Example:
        >>> import math
        >>> round(trapezoidal_integrate(math.sin, 0, math.pi, 10000), 6)
        2.0

    Complexity: O(n)
    """
    if not callable(f):
        raise TypeError("f must be callable")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numeric")

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")

    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        total += f(a + i * h)

    return float(total * h)


def simpsons_integrate(
    f: Callable[[float], float], a: float, b: float, n: int = 1000
) -> float:
    """Numerically integrates f(x) from a to b using Simpson's 1/3 rule.

    Args:
        f: A callable that takes a float and returns a float.
        a: Lower bound of integration.
        b: Upper bound of integration.
        n: Number of sub-intervals (must be even, default 1000).

    Returns:
        Approximate value of ∫f(x)dx from a to b.

    Raises:
        TypeError: If f is not callable or bounds/n have wrong types.
        ValueError: If n is not a positive even integer.

    Example:
        >>> import math
        >>> round(simpsons_integrate(math.sin, 0, math.pi, 100), 10)
        2.0

    Complexity: O(n)
    """
    if not callable(f):
        raise TypeError("f must be callable")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numeric")

    if not isinstance(n, int) or n <= 0 or n % 2 != 0:
        raise ValueError("n must be a positive even integer")

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n, 2):
        total += 4 * f(a + i * h)

    for i in range(2, n, 2):
        total += 2 * f(a + i * h)

    return float(total * h / 3)


def newton_raphson(
    f: Callable[[float], float],
    df: Callable[[float], float],
    x0: float,
    tol: float = 1e-10,
    max_iter: int = 100,
) -> float:
    """Finds a root of f(x) = 0 using the Newton-Raphson method.

    Requires the derivative df(x). Converges quadratically near simple roots.

    Args:
        f: The function whose root is sought.
        df: The derivative of f.
        x0: Initial guess.
        tol: Convergence tolerance on |f(x)|.
        max_iter: Maximum number of iterations.

    Returns:
        Approximate root x where f(x) ≈ 0.

    Raises:
        TypeError: If f or df are not callable.
        ValueError: If derivative is zero (division by zero) or convergence fails.

    Example:
        >>> round(newton_raphson(lambda x: x**2 - 2, lambda x: 2*x, 1.0), 10)
        1.4142135624

    Complexity: O(max_iter)
    """
    if not callable(f) or not callable(df):
        raise TypeError("f and df must be callable")

    if not isinstance(x0, (int, float)):
        raise TypeError("x0 must be numeric")

    x = float(x0)

    for _ in range(max_iter):
        fx = f(x)

        if abs(fx) < tol:
            return x

        dfx = df(x)

        if dfx == 0:
            raise ValueError("Derivative is zero — Newton-Raphson cannot continue")

        x = x - fx / dfx

    raise ValueError(f"Newton-Raphson did not converge within {max_iter} iterations")


def bisection_method(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-10,
    max_iter: int = 100,
) -> float:
    """Finds a root of f(x) = 0 in [a, b] using the bisection method.

    Requires that f(a) and f(b) have opposite signs.

    Args:
        f: The function whose root is sought.
        a: Lower bound of the interval.
        b: Upper bound of the interval.
        tol: Convergence tolerance on interval width.
        max_iter: Maximum number of iterations.

    Returns:
        Approximate root x where f(x) ≈ 0.

    Raises:
        TypeError: If f is not callable.
        ValueError: If f(a) and f(b) have the same sign.

    Example:
        >>> round(bisection_method(lambda x: x**2 - 2, 1, 2), 8)
        1.41421356

    Complexity: O(max_iter) = O(log₂((b−a)/tol))
    """
    if not callable(f):
        raise TypeError("f must be callable")

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numeric")

    fa, fb = f(a), f(b)

    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs")

    for _ in range(max_iter):
        mid = (a + b) / 2.0
        fm = f(mid)

        if abs(fm) < tol or (b - a) / 2 < tol:
            return float(mid)

        if fa * fm < 0:
            b = mid
        else:
            a = mid
            fa = fm

    return float((a + b) / 2.0)


def polynomial_evaluate(coefficients: List[float], x: float) -> float:
    """Evaluates a polynomial at x using Horner's method.

    Coefficients are ordered from highest degree to lowest:
    ``[aₙ, aₙ₋₁, …, a₁, a₀]`` represents aₙxⁿ + … + a₁x + a₀.

    Args:
        coefficients: List of coefficients [aₙ, …, a₀].
        x: The point at which to evaluate.

    Returns:
        Polynomial value at x.

    Raises:
        TypeError: If coefficients is not a list or x is not numeric.
        ValueError: If coefficients is empty.

    Example:
        >>> polynomial_evaluate([1, -3, 2], 2)  # x²-3x+2 at x=2
        0

    Complexity: O(n) where n = len(coefficients)
    """
    if not isinstance(coefficients, list):
        raise TypeError("coefficients must be a list")

    if not coefficients:
        raise ValueError("coefficients must not be empty")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")

    result = 0.0

    for c in coefficients:

        if not isinstance(c, (int, float)):
            raise TypeError("All coefficients must be numeric")

        result = result * x + c

    return float(result)


def polynomial_roots_quadratic(
    a: float, b: float, c: float
) -> Tuple[complex, complex]:
    """Finds the two roots of a quadratic equation ax² + bx + c = 0.

    Returns complex roots when the discriminant is negative.

    Args:
        a: Coefficient of x² (must not be zero).
        b: Coefficient of x.
        c: Constant term.

    Returns:
        Tuple of two roots (may be complex).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If a is zero.

    Example:
        >>> polynomial_roots_quadratic(1, -3, 2)
        (2.0, 1.0)
        >>> polynomial_roots_quadratic(1, 0, 1)
        (1j, -1j)

    Complexity: O(1)
    """
    for name, val in (("a", a), ("b", b), ("c", c)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if a == 0:
        raise ValueError("a must not be zero (not a quadratic equation)")

    disc = b * b - 4 * a * c

    if disc >= 0:
        sqrt_disc = math.sqrt(disc)
        return ((-b + sqrt_disc) / (2 * a), (-b - sqrt_disc) / (2 * a))
    else:
        real_part = -b / (2 * a)
        imag_part = math.sqrt(-disc) / (2 * a)
        return (complex(real_part, imag_part), complex(real_part, -imag_part))


def polynomial_roots_cubic(
    a: float, b: float, c: float, d: float
) -> Tuple:
    """Finds the three roots of a cubic equation ax³ + bx² + cx + d = 0.

    Uses Cardano's method. Returns a tuple of three roots (may be complex).

    Args:
        a: Coefficient of x³ (must not be zero).
        b: Coefficient of x².
        c: Coefficient of x.
        d: Constant term.

    Returns:
        Tuple of three roots.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If a is zero.

    Example:
        >>> roots = polynomial_roots_cubic(1, -6, 11, -6)  # (x-1)(x-2)(x-3)
        >>> sorted([round(r.real, 6) for r in roots])
        [1.0, 2.0, 3.0]

    Complexity: O(1)
    """
    for name, val in (("a", a), ("b", b), ("c", c), ("d", d)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if a == 0:
        raise ValueError("a must not be zero (not a cubic equation)")

    # Depress: substitute x = t − b/(3a)
    p = (3 * a * c - b * b) / (3 * a * a)
    q = (2 * b ** 3 - 9 * a * b * c + 27 * a * a * d) / (27 * a ** 3)

    offset = -b / (3 * a)

    # Use complex cube root approach for all cases
    det = (q / 2) ** 2 + (p / 3) ** 3
    det_c = complex(det, 0)
    sqrt_det = det_c ** 0.5

    u = (-q / 2 + sqrt_det) ** (1 / 3)
    v = (-q / 2 - sqrt_det) ** (1 / 3)

    omega = complex(-0.5, math.sqrt(3) / 2)
    omega2 = complex(-0.5, -math.sqrt(3) / 2)

    r1 = u + v + offset
    r2 = omega * u + omega2 * v + offset
    r3 = omega2 * u + omega * v + offset

    def _clean(r: complex) -> Union[float, complex]:
        if abs(r.imag) < 1e-10:
            return round(r.real, 10)

        return r

    return (_clean(r1), _clean(r2), _clean(r3))


def continued_fraction(
    numerator: int, denominator: int, max_terms: int = 20
) -> List[int]:
    """Computes the continued fraction representation of a rational number.

    Returns the list ``[a₀; a₁, a₂, …]`` such that
    ``numerator/denominator = a₀ + 1/(a₁ + 1/(a₂ + …))``.

    Args:
        numerator: Integer numerator.
        denominator: Integer denominator (must not be zero).
        max_terms: Maximum number of terms to compute.

    Returns:
        List of continued fraction coefficients.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If denominator is zero.

    Example:
        >>> continued_fraction(355, 113)
        [3, 7, 16]

    Complexity: O(min(max_terms, log(denominator)))
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("numerator and denominator must be integers")

    if denominator == 0:
        raise ValueError("denominator must not be zero")

    result: List[int] = []
    a, b = numerator, denominator

    for _ in range(max_terms):

        if b == 0:
            break

        q, r = divmod(a, b)
        result.append(q)
        a, b = b, r

    return result


def runge_kutta_4_step(
    f: Callable[[float, float], float],
    t: float,
    y: float,
    h: float,
) -> Tuple[float, float]:
    """Performs one step of the classic 4th-order Runge-Kutta method.

    Solves dy/dt = f(t, y) advancing from (t, y) to (t+h, y_new).

    Args:
        f: The ODE function f(t, y).
        t: Current time.
        y: Current state value.
        h: Step size.

    Returns:
        Tuple of (t + h, y_new).

    Raises:
        TypeError: If f is not callable or t/y/h are not numeric.

    Example:
        >>> # dy/dt = y, y(0) = 1 → solution is e^t
        >>> t1, y1 = runge_kutta_4_step(lambda t, y: y, 0, 1.0, 0.1)
        >>> round(y1, 6)
        1.105171

    Complexity: O(1) — four function evaluations per step
    """
    if not callable(f):
        raise TypeError("f must be callable")

    for name, val in (("t", t), ("y", y), ("h", h)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    k1 = h * f(t, y)
    k2 = h * f(t + h / 2, y + k1 / 2)
    k3 = h * f(t + h / 2, y + k2 / 2)
    k4 = h * f(t + h, y + k3)
    y_new = y + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    return (t + h, float(y_new))


def secant_method(
    f: Callable[[float], float],
    x0: float,
    x1: float,
    tol: float = 1e-10,
    max_iter: int = 100,
) -> float:
    """Find a root of *f* using the secant method.

    Unlike Newton-Raphson, does not require the derivative.

    Args:
        f: Continuous function f(x).
        x0: First initial guess.
        x1: Second initial guess.
        tol: Convergence tolerance.
        max_iter: Maximum iterations.

    Returns:
        Approximate root.

    Raises:
        TypeError: If *f* is not callable.
        RuntimeError: If convergence fails.

    Example:
        >>> round(secant_method(lambda x: x**2 - 2, 1.0, 2.0), 6)
        1.414214

    Complexity: O(max_iter)
    """
    if not callable(f):
        raise TypeError("f must be callable")

    for name, val in (("x0", x0), ("x1", x1)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    a, b = float(x0), float(x1)
    fa, fb = f(a), f(b)

    for _ in range(max_iter):

        if abs(fb - fa) < 1e-30:
            raise RuntimeError("Secant method: division by near-zero difference")

        c = b - fb * (b - a) / (fb - fa)

        if abs(c - b) < tol:
            return float(c)

        a, fa = b, fb
        b, fb = c, f(c)

    raise RuntimeError(f"Secant method did not converge in {max_iter} iterations")


def fixed_point_iteration(
    g: Callable[[float], float],
    x0: float,
    tol: float = 1e-10,
    max_iter: int = 100,
) -> float:
    """Find a fixed point of *g*, i.e. x such that g(x) = x.

    Args:
        g: Iteration function g(x).
        x0: Initial guess.
        tol: Convergence tolerance.
        max_iter: Maximum iterations.

    Returns:
        Approximate fixed point.

    Raises:
        TypeError: If *g* is not callable.
        RuntimeError: If convergence fails.

    Example:
        >>> round(fixed_point_iteration(lambda x: (x + 2/x) / 2, 1.0), 6)
        1.414214

    Complexity: O(max_iter)
    """
    if not callable(g):
        raise TypeError("g must be callable")

    if not isinstance(x0, (int, float)):
        raise TypeError("x0 must be numeric")

    x = float(x0)

    for _ in range(max_iter):
        x_new = g(x)

        if abs(x_new - x) < tol:
            return float(x_new)

        x = x_new

    raise RuntimeError(f"Fixed-point iteration did not converge in {max_iter} iterations")


def romberg_integrate(
    f: Callable[[float], float],
    a: float,
    b: float,
    max_order: int = 10,
    tol: float = 1e-12,
) -> float:
    """Romberg integration — recursive Richardson extrapolation on the trapezoid rule.

    Args:
        f: Function to integrate, f(x).
        a: Lower bound.
        b: Upper bound.
        max_order: Maximum Richardson extrapolation order.
        tol: Convergence tolerance.

    Returns:
        Approximate definite integral.

    Raises:
        TypeError: If *f* is not callable.

    Example:
        >>> import math
        >>> round(romberg_integrate(math.sin, 0, math.pi), 10)
        2.0

    Complexity: O(2^max_order)
    """
    if not callable(f):
        raise TypeError("f must be callable")

    for name, val in (("a", a), ("b", b)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    R: list[list[float]] = [[0.0] * (max_order + 1) for _ in range(max_order + 1)]

    h = float(b - a)
    R[0][0] = h * (f(a) + f(b)) / 2.0

    for n in range(1, max_order + 1):
        h /= 2.0
        total = sum(f(a + (2 * k - 1) * h) for k in range(1, 2 ** (n - 1) + 1))
        R[n][0] = R[n - 1][0] / 2.0 + h * total

        for m in range(1, n + 1):
            R[n][m] = R[n][m - 1] + (R[n][m - 1] - R[n - 1][m - 1]) / (4 ** m - 1)

        if n >= 2 and abs(R[n][n] - R[n - 1][n - 1]) < tol:
            return float(R[n][n])

    return float(R[max_order][max_order])


def adaptive_simpson(
    f: Callable[[float], float],
    a: float,
    b: float,
    tol: float = 1e-10,
    max_depth: int = 50,
) -> float:
    """Adaptive Simpson's rule for numerical integration.

    Recursively subdivides intervals where error is above tolerance.

    Args:
        f: Function to integrate, f(x).
        a: Lower bound.
        b: Upper bound.
        tol: Error tolerance.
        max_depth: Maximum recursion depth.

    Returns:
        Approximate definite integral.

    Raises:
        TypeError: If *f* is not callable.

    Example:
        >>> import math
        >>> round(adaptive_simpson(math.sin, 0, math.pi), 10)
        2.0

    Complexity: O(n) where n depends on function smoothness.
    """
    if not callable(f):
        raise TypeError("f must be callable")

    for name, val in (("a", a), ("b", b)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    def _simpson(fa: float, fb: float, fc: float, a: float, b: float) -> float:
        return (b - a) / 6.0 * (fa + 4.0 * fc + fb)

    def _recursive(
        a: float, b: float, fa: float, fb: float, fc: float,
        whole: float, tol: float, depth: int,
    ) -> float:
        mid = (a + b) / 2.0
        f_left_mid = f((a + mid) / 2.0)
        f_right_mid = f((mid + b) / 2.0)
        left = _simpson(fa, fc, f_left_mid, a, mid)
        right = _simpson(fc, fb, f_right_mid, mid, b)

        if depth <= 0 or abs(left + right - whole) <= 15.0 * tol:
            return left + right + (left + right - whole) / 15.0

        return (
            _recursive(a, mid, fa, fc, f_left_mid, left, tol / 2, depth - 1)
            + _recursive(mid, b, fc, fb, f_right_mid, right, tol / 2, depth - 1)
        )

    fa_val = f(a)
    fb_val = f(b)
    fc_val = f((a + b) / 2.0)
    whole = _simpson(fa_val, fb_val, fc_val, a, b)

    return float(_recursive(a, b, fa_val, fb_val, fc_val, whole, tol, max_depth))


def chebyshev_nodes(n: int, a: float = -1.0, b: float = 1.0) -> list[float]:
    """Generate *n* Chebyshev nodes on the interval [a, b].

    Chebyshev nodes minimize the Runge phenomenon, making them ideal
    for polynomial interpolation.

    Args:
        n: Number of nodes (≥ 1).
        a: Left endpoint.
        b: Right endpoint.

    Returns:
        List of Chebyshev node locations.

    Raises:
        TypeError: If *n* is not an int or endpoints are not numeric.
        ValueError: If *n* < 1 or *a* >= *b*.

    Example:
        >>> [round(x, 4) for x in chebyshev_nodes(3)]
        [0.866, 0.0, -0.866]

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    if n < 1:
        raise ValueError("n must be at least 1")

    for name, val in (("a", a), ("b", b)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if a >= b:
        raise ValueError("a must be less than b")

    nodes: list[float] = []

    for k in range(n):
        xk = math.cos(math.pi * (2 * k + 1) / (2 * n))
        # Map from [-1, 1] to [a, b]
        mapped = 0.5 * (a + b) + 0.5 * (b - a) * xk
        nodes.append(round(mapped, 10))

    return nodes


def gaussian_quadrature(
    f: callable,
    a: float,
    b: float,
    n: int = 5,
) -> float:
    """Numerical integration via Gauss-Legendre quadrature.

    Uses pre-computed nodes and weights for *n* = 1-5. For general *n*
    falls back to the midpoint rule (n subintervals).

    Args:
        f: Integrand function.
        a: Lower bound.
        b: Upper bound.
        n: Number of quadrature points (1-5 for exact GL).

    Returns:
        Approximate integral value.

    Raises:
        TypeError: If *f* is not callable or bounds not numeric.
        ValueError: If *n* < 1.

    Example:
        >>> import math
        >>> round(gaussian_quadrature(math.sin, 0, math.pi, 5), 6)
        2.000011

    Complexity: O(n)
    """

    if not callable(f):
        raise TypeError("f must be callable")

    for name, val in (("a", a), ("b", b)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer")

    # Pre-computed Gauss-Legendre nodes/weights on [-1, 1]
    _gl: dict[int, list[tuple[float, float]]] = {
        1: [(0.0, 2.0)],
        2: [(-0.5773502692, 1.0), (0.5773502692, 1.0)],
        3: [(-0.7745966692, 0.5555555556), (0.0, 0.8888888889),
            (0.7745966692, 0.5555555556)],
        4: [(-0.8611363116, 0.3478548451), (-0.3399810436, 0.6521451549),
            (0.3399810436, 0.6521451549), (0.8611363116, 0.3478548451)],
        5: [(-0.9061798459, 0.2369268851), (-0.5384693101, 0.4786286705),
            (0.0, 0.5688888889), (0.5384693101, 0.4786286705),
            (0.9061798459, 0.2369268851)],
    }

    if n in _gl:
        half_len = (b - a) / 2.0
        mid = (a + b) / 2.0

        return float(half_len * sum(w * f(half_len * xi + mid) for xi, w in _gl[n]))

    # Fallback: composite midpoint rule
    h = (b - a) / n

    return float(h * sum(f(a + (i + 0.5) * h) for i in range(n)))


def euler_method(
    f: callable,
    y0: float,
    t0: float,
    t_end: float,
    steps: int = 100,
) -> list[tuple[float, float]]:
    """Solve an ODE y' = f(t, y) using Euler's method.

    Args:
        f: Function ``f(t, y)`` returning the derivative.
        y0: Initial value y(t0).
        t0: Start time.
        t_end: End time.
        steps: Number of integration steps.

    Returns:
        List of ``(t, y)`` pairs.

    Raises:
        TypeError: If *f* is not callable or other args not numeric.
        ValueError: If *steps* < 1.

    Example:
        >>> pts = euler_method(lambda t, y: y, 1.0, 0.0, 1.0, 1000)
        >>> round(pts[-1][1], 2)
        2.72

    Complexity: O(steps)
    """
    if not callable(f):
        raise TypeError("f must be callable")

    for name, val in (("y0", y0), ("t0", t0), ("t_end", t_end)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if not isinstance(steps, int) or steps < 1:
        raise ValueError("steps must be a positive integer")

    h = (t_end - t0) / steps
    t = float(t0)
    y = float(y0)
    result: list[tuple[float, float]] = [(round(t, 10), round(y, 10))]

    for _ in range(steps):
        y += h * f(t, y)
        t += h
        result.append((round(t, 10), round(y, 10)))

    return result


# ---------------------------------------------------------------------------
# Matrix decompositions and norms (Spiegel Ch. Algebra / Linear Algebra)
# ---------------------------------------------------------------------------


def lu_decomposition(
    matrix: List[List[float]],
) -> Tuple[List[List[float]], List[List[float]]]:
    """Performs LU decomposition of a square matrix (Doolittle algorithm).

    Decomposes A into L (lower triangular with unit diagonal) and U (upper triangular)
    such that A = L * U.

    Args:
        matrix: Square matrix as list of lists.

    Returns:
        Tuple (L, U).

    Raises:
        TypeError: If input is not a list of lists of numbers.
        ValueError: If matrix is not square, empty, or pivot is zero.

    Example:
        >>> L, U = lu_decomposition([[2, 1], [4, 3]])
        >>> L
        [[1.0, 0.0], [2.0, 1.0]]
        >>> U
        [[2.0, 1.0], [0.0, 1.0]]

    Complexity: O(n^3)
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("Input must be a list of lists.")

    n = len(matrix)

    if n == 0:
        raise ValueError("Matrix cannot be empty.")

    for row in matrix:

        if len(row) != n:
            raise ValueError("Matrix must be square.")

        for v in row:

            if not isinstance(v, (int, float)):
                raise TypeError("All elements must be numeric.")

    lower = [[0.0] * n for _ in range(n)]
    upper = [[0.0] * n for _ in range(n)]

    for i in range(n):
        # Upper triangular
        for k in range(i, n):
            s = sum(lower[i][j] * upper[j][k] for j in range(i))
            upper[i][k] = float(matrix[i][k]) - s

        # Lower triangular
        for k in range(i, n):

            if i == k:
                lower[i][i] = 1.0
            else:

                if abs(upper[i][i]) < 1e-15:
                    raise ValueError("Zero pivot encountered; LU decomposition failed.")

                s = sum(lower[k][j] * upper[j][i] for j in range(i))
                lower[k][i] = (float(matrix[k][i]) - s) / upper[i][i]

    return lower, upper


def matrix_eigenvalues_2x2(matrix: List[List[float]]) -> Tuple[complex, complex]:
    """Computes the eigenvalues of a 2×2 matrix using the characteristic equation.

    For [[a, b], [c, d]], eigenvalues are roots of λ² - (a+d)λ + (ad - bc) = 0.

    Args:
        matrix: A 2×2 matrix.

    Returns:
        Tuple of two eigenvalues (may be complex).

    Raises:
        TypeError: If input is not a 2×2 list of lists of numbers.
        ValueError: If matrix is not 2×2.

    Example:
        >>> matrix_eigenvalues_2x2([[2, 1], [1, 2]])
        (3.0, 1.0)

    Complexity: O(1)
    """
    if not isinstance(matrix, list) or len(matrix) != 2:
        raise ValueError("Matrix must be 2x2.")

    for row in matrix:

        if not isinstance(row, list) or len(row) != 2:
            raise ValueError("Matrix must be 2x2.")

        for v in row:

            if not isinstance(v, (int, float)):
                raise TypeError("All elements must be numeric.")

    a, b = float(matrix[0][0]), float(matrix[0][1])
    c, d = float(matrix[1][0]), float(matrix[1][1])

    trace = a + d
    det = a * d - b * c
    discriminant = trace * trace - 4.0 * det

    if discriminant >= 0:
        sqrt_disc = math.sqrt(discriminant)
        return ((trace + sqrt_disc) / 2.0, (trace - sqrt_disc) / 2.0)

    sqrt_disc = math.sqrt(-discriminant)
    real = trace / 2.0
    return (complex(real, sqrt_disc / 2.0), complex(real, -sqrt_disc / 2.0))


def matrix_frobenius_norm(matrix: List[List[float]]) -> float:
    """Computes the Frobenius norm of a matrix: sqrt(sum of squares of all elements).

    Args:
        matrix: Matrix as list of lists.

    Returns:
        Frobenius norm.

    Raises:
        TypeError: If input is not a list of lists of numbers.

    Example:
        >>> round(matrix_frobenius_norm([[1, 2], [3, 4]]), 6)
        5.477226

    Complexity: O(m*n)
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("Input must be a list of lists.")

    total = 0.0

    for row in matrix:

        for v in row:

            if not isinstance(v, (int, float)):
                raise TypeError("All elements must be numeric.")

            total += v * v

    return math.sqrt(total)


def matrix_infinity_norm(matrix: List[List[float]]) -> float:
    """Computes the infinity norm of a matrix: max row-sum of absolute values.

    Args:
        matrix: Matrix as list of lists.

    Returns:
        Infinity norm.

    Raises:
        TypeError: If input is not a list of lists of numbers.
        ValueError: If matrix is empty.

    Example:
        >>> matrix_infinity_norm([[1, -2], [3, 4]])
        7

    Complexity: O(m*n)
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("Input must be a list of lists.")

    if not matrix:
        raise ValueError("Matrix cannot be empty.")

    max_sum = 0.0

    for row in matrix:
        row_sum = 0.0

        for v in row:

            if not isinstance(v, (int, float)):
                raise TypeError("All elements must be numeric.")

            row_sum += abs(v)

        if row_sum > max_sum:
            max_sum = row_sum

    return max_sum


def matrix_one_norm(matrix: List[List[float]]) -> float:
    """Computes the 1-norm of a matrix: max column-sum of absolute values.

    Args:
        matrix: Matrix as list of lists.

    Returns:
        1-norm.

    Raises:
        TypeError: If input is not a list of lists of numbers.
        ValueError: If matrix is empty.

    Example:
        >>> matrix_one_norm([[1, -2], [3, 4]])
        6

    Complexity: O(m*n)
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("Input must be a list of lists.")

    if not matrix:
        raise ValueError("Matrix cannot be empty.")

    n_cols = len(matrix[0])
    max_sum = 0.0

    for j in range(n_cols):
        col_sum = 0.0

        for row in matrix:

            if j < len(row):

                if not isinstance(row[j], (int, float)):
                    raise TypeError("All elements must be numeric.")

                col_sum += abs(row[j])

        if col_sum > max_sum:
            max_sum = col_sum

    return max_sum


def matrix_rank(matrix: List[List[float]], tol: float = 1e-10) -> int:
    """Computes the rank of a matrix via Gaussian elimination.

    Args:
        matrix: Matrix as list of lists.
        tol: Tolerance for considering a pivot as zero.

    Returns:
        Rank of the matrix.

    Raises:
        TypeError: If input is not a list of lists of numbers.
        ValueError: If matrix is empty.

    Example:
        >>> matrix_rank([[1, 2], [2, 4]])
        1
        >>> matrix_rank([[1, 0], [0, 1]])
        2

    Complexity: O(m*n*min(m,n))
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("Input must be a list of lists.")

    if not matrix:
        raise ValueError("Matrix cannot be empty.")

    m = len(matrix)
    n = len(matrix[0])

    # Make a copy
    a = [[float(matrix[i][j]) for j in range(n)] for i in range(m)]

    rank = 0

    for col in range(n):

        # Find pivot
        pivot_row = None

        for row in range(rank, m):

            if abs(a[row][col]) > tol:
                pivot_row = row
                break

        if pivot_row is None:
            continue

        # Swap
        a[rank], a[pivot_row] = a[pivot_row], a[rank]

        # Eliminate
        for row in range(rank + 1, m):
            factor = a[row][col] / a[rank][col]

            for j in range(col, n):
                a[row][j] -= factor * a[rank][j]

        rank += 1

    return rank


# ---------------------------------------------------------------------------
# Cholesky, QR, matrix power, adjugate (Spiegel Ch. Linear Algebra)
# ---------------------------------------------------------------------------


def cholesky_decomposition(matrix: List[List[float]]) -> List[List[float]]:
    """Performs Cholesky decomposition of a symmetric positive-definite matrix.

    Decomposes A into L such that A = L * L^T, where L is lower triangular.

    Args:
        matrix: Symmetric positive-definite square matrix.

    Returns:
        Lower triangular matrix L.

    Raises:
        TypeError: If input is not a list of lists of numbers.
        ValueError: If matrix is not square, not symmetric, or not positive-definite.

    Example:
        >>> cholesky_decomposition([[4, 2], [2, 5]])
        [[2.0, 0.0], [1.0, 2.0]]

    Complexity: O(n^3)
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("Input must be a list of lists.")

    n = len(matrix)

    if n == 0:
        raise ValueError("Matrix cannot be empty.")

    for i in range(n):

        if len(matrix[i]) != n:
            raise ValueError("Matrix must be square.")

        for j in range(n):

            if not isinstance(matrix[i][j], (int, float)):
                raise TypeError("All elements must be numeric.")

    # Symmetry check
    for i in range(n):

        for j in range(i + 1, n):

            if abs(matrix[i][j] - matrix[j][i]) > 1e-10:
                raise ValueError("Matrix must be symmetric.")

    lower = [[0.0] * n for _ in range(n)]

    for i in range(n):

        for j in range(i + 1):
            s = sum(lower[i][k] * lower[j][k] for k in range(j))

            if i == j:
                val = matrix[i][i] - s

                if val <= 0:
                    raise ValueError("Matrix is not positive-definite.")

                lower[i][j] = math.sqrt(val)
            else:
                lower[i][j] = (matrix[i][j] - s) / lower[j][j]

    return lower


def qr_decomposition(
    matrix: List[List[float]],
) -> Tuple[List[List[float]], List[List[float]]]:
    """Performs QR decomposition via modified Gram-Schmidt orthogonalization.

    Decomposes A (m×n, m >= n) into Q (m×n orthogonal) and R (n×n upper triangular)
    such that A = Q * R.

    Args:
        matrix: Matrix with m >= n as list of lists.

    Returns:
        Tuple (Q, R).

    Raises:
        TypeError: If input is not a list of lists of numbers.
        ValueError: If matrix is empty, or m < n, or columns are linearly dependent.

    Example:
        >>> Q, R = qr_decomposition([[1, 1], [0, 1], [1, 0]])
        >>> len(Q), len(R)
        (3, 2)

    Complexity: O(m*n^2)
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("Input must be a list of lists.")

    m = len(matrix)

    if m == 0:
        raise ValueError("Matrix cannot be empty.")

    n = len(matrix[0])

    if m < n:
        raise ValueError("Matrix must have m >= n (more rows than columns).")

    for row in matrix:

        if len(row) != n:
            raise ValueError("All rows must have the same length.")

        for v in row:

            if not isinstance(v, (int, float)):
                raise TypeError("All elements must be numeric.")

    # Extract columns
    cols = [[float(matrix[i][j]) for i in range(m)] for j in range(n)]

    q_cols: List[List[float]] = []
    r_matrix = [[0.0] * n for _ in range(n)]

    for j in range(n):
        v = cols[j][:]

        for i in range(j):
            r_ij = sum(q_cols[i][k] * v[k] for k in range(m))
            r_matrix[i][j] = r_ij

            for k in range(m):
                v[k] -= r_ij * q_cols[i][k]

        norm = math.sqrt(sum(x * x for x in v))

        if norm < 1e-12:
            raise ValueError("Columns are linearly dependent.")

        r_matrix[j][j] = norm
        q_cols.append([x / norm for x in v])

    # Build Q as list of rows
    q_out = [[q_cols[j][i] for j in range(n)] for i in range(m)]
    return (q_out, r_matrix)


def matrix_power(matrix: List[List[float]], n: int) -> List[List[float]]:
    """Computes the n-th power of a square matrix A^n by repeated multiplication.

    Args:
        matrix: Square matrix.
        n: Non-negative integer exponent.

    Returns:
        A^n as list of lists.

    Raises:
        TypeError: If input is not a list of lists, or n is not an int.
        ValueError: If matrix is not square or n < 0.

    Example:
        >>> matrix_power([[1, 1], [0, 1]], 3)
        [[1, 3], [0, 1]]

    Complexity: O(k^3 * log(n)) where k is matrix size.
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("Input must be a list of lists.")

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    k = len(matrix)

    if k == 0:
        raise ValueError("Matrix cannot be empty.")

    for row in matrix:

        if len(row) != k:
            raise ValueError("Matrix must be square.")

    def _mat_mul(a: List[List[float]], b: List[List[float]]) -> List[List[float]]:
        size = len(a)
        result = [[0.0] * size for _ in range(size)]

        for i in range(size):

            for j in range(size):
                s = 0.0

                for p in range(size):
                    s += a[i][p] * b[p][j]

                result[i][j] = s

        return result

    # Identity matrix
    result = [[1 if i == j else 0 for j in range(k)] for i in range(k)]
    base = [row[:] for row in matrix]

    # Binary exponentiation
    exp = n

    while exp > 0:

        if exp % 2 == 1:
            result = _mat_mul(result, base)

        base = _mat_mul(base, base)
        exp //= 2

    return result


def adjugate_matrix(matrix: List[List[float]]) -> List[List[float]]:
    """Computes the adjugate (classical adjoint) of a square matrix.

    adj(A)_ij = (-1)^(i+j) * M_ji where M_ji is the (j,i) minor.

    Args:
        matrix: Square matrix.

    Returns:
        Adjugate matrix.

    Raises:
        TypeError: If input is not a list of lists of numbers.
        ValueError: If matrix is not square or is empty.

    Example:
        >>> adjugate_matrix([[1, 2], [3, 4]])
        [[4.0, -2.0], [-3.0, 1.0]]

    Complexity: O(n^2 * n!) — practical only for small matrices.
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("Input must be a list of lists.")

    n = len(matrix)

    if n == 0:
        raise ValueError("Matrix cannot be empty.")

    for row in matrix:

        if len(row) != n:
            raise ValueError("Matrix must be square.")

        for v in row:

            if not isinstance(v, (int, float)):
                raise TypeError("All elements must be numeric.")

    if n == 1:
        return [[1.0]]

    def _minor(mat: List[List[float]], row: int, col: int) -> List[List[float]]:
        return [
            [mat[r][c] for c in range(len(mat)) if c != col]
            for r in range(len(mat)) if r != row
        ]

    def _det(mat: List[List[float]]) -> float:
        sz = len(mat)

        if sz == 1:
            return float(mat[0][0])

        if sz == 2:
            return float(mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0])

        d = 0.0

        for j in range(sz):
            d += ((-1) ** j) * mat[0][j] * _det(_minor(mat, 0, j))

        return d

    adj = [[0.0] * n for _ in range(n)]

    for i in range(n):

        for j in range(n):
            # Note: adj[i][j] = cofactor(j, i) = (-1)^(i+j) * det(minor(j, i))
            cofactor = ((-1) ** (i + j)) * _det(_minor(matrix, j, i))
            adj[i][j] = cofactor

    return adj


def solve_linear_system(
    a: List[List[float]], b: List[float]
) -> List[float]:
    """Solves Ax = b via Gaussian elimination with partial pivoting.

    Args:
        a: Coefficient matrix (n×n).
        b: Right-hand side vector (length n).

    Returns:
        Solution vector x.

    Raises:
        TypeError: If inputs are not numeric lists.
        ValueError: If matrix is singular or dimensions mismatch.

    Example:
        >>> solve_linear_system([[2, 1], [1, 3]], [5, 10])
        [1.0, 3.0]

    Complexity: O(n^3)
    """
    if not isinstance(a, list) or not all(isinstance(r, list) for r in a):
        raise TypeError("a must be a list of lists.")

    if not isinstance(b, list):
        raise TypeError("b must be a list.")

    n = len(a)

    if n == 0:
        raise ValueError("System cannot be empty.")

    if len(b) != n:
        raise ValueError("b must have the same length as rows in a.")

    # Augmented matrix
    aug = [[float(a[i][j]) for j in range(n)] + [float(b[i])] for i in range(n)]

    for col in range(n):
        # Partial pivoting
        max_row = col

        for row in range(col + 1, n):

            if abs(aug[row][col]) > abs(aug[max_row][col]):
                max_row = row

        aug[col], aug[max_row] = aug[max_row], aug[col]

        if abs(aug[col][col]) < 1e-15:
            raise ValueError("Matrix is singular.")

        # Eliminate
        for row in range(col + 1, n):
            factor = aug[row][col] / aug[col][col]

            for j in range(col, n + 1):
                aug[row][j] -= factor * aug[col][j]

    # Back substitution
    x = [0.0] * n

    for i in range(n - 1, -1, -1):
        x[i] = (aug[i][n] - sum(aug[i][j] * x[j] for j in range(i + 1, n))) / aug[i][i]

    return x


# ---------------------------------------------------------------------------
# Phase 21 – Batch 21: Arithmetic Functions (1 of 2)
# ---------------------------------------------------------------------------

def digital_sum(n: int) -> int:
    """Compute the digit sum of an integer.

    Args:
        n: Non-negative integer.

    Returns:
        Sum of digits.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> digital_sum(12345)
        15

    Complexity: O(log n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return sum(int(d) for d in str(n))


def digit_product(n: int) -> int:
    """Compute the product of digits of a positive integer.

    Args:
        n: Non-negative integer.

    Returns:
        Product of digits (0 if any digit is 0).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> digit_product(234)
        24

    Complexity: O(log n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    result = 1
    for d in str(n):
        result *= int(d)
    return result


def multiplicative_persistence(n: int) -> int:
    """Count iterations to reduce n to a single digit by multiplying its digits.

    Args:
        n: Non-negative integer.

    Returns:
        Number of iterations.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> multiplicative_persistence(39)
        3

    Complexity: O(log(n) × iterations)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    count = 0
    while n >= 10:
        product = 1
        for d in str(n):
            product *= int(d)
        n = product
        count += 1
    return count


def additive_persistence(n: int) -> int:
    """Count iterations to reduce n to a single digit by summing its digits.

    Args:
        n: Non-negative integer.

    Returns:
        Number of iterations.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> additive_persistence(199)
        3

    Complexity: O(log(n) × iterations)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    count = 0
    while n >= 10:
        n = sum(int(d) for d in str(n))
        count += 1
    return count


def collatz_steps(n: int) -> int:
    """Count the number of Collatz steps to reach 1.

    If n is even: n → n/2. If odd: n → 3n + 1.

    Args:
        n: Positive integer.

    Returns:
        Number of steps to reach 1.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> collatz_steps(27)
        111

    Complexity: Depends on the Collatz sequence length
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    count = 0
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        count += 1
    return count


def collatz_sequence(n: int) -> list[int]:
    """Generate the Collatz sequence starting from n.

    Args:
        n: Positive integer.

    Returns:
        The full Collatz sequence ending at 1.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> collatz_sequence(6)
        [6, 3, 10, 5, 16, 8, 4, 2, 1]

    Complexity: Depends on the Collatz sequence length
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    seq = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        seq.append(n)
    return seq


def integer_partition_distinct(n: int) -> int:
    """Count partitions of n into distinct parts using DP.

    Args:
        n: Non-negative integer.

    Returns:
        Number of partitions with distinct parts.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> integer_partition_distinct(10)
        10

    Complexity: O(n²)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for i in range(n, k - 1, -1):
            dp[i] += dp[i - k]
    return dp[n]


def sum_first_n_squares(n: int) -> int:
    """Compute 1² + 2² + ··· + n².

    Uses closed form: n(n+1)(2n+1)/6.

    Args:
        n: Non-negative integer.

    Returns:
        Sum of squares from 1 to n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> sum_first_n_squares(10)
        385

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return n * (n + 1) * (2 * n + 1) // 6


def sum_first_n_cubes(n: int) -> int:
    """Compute 1³ + 2³ + ··· + n³.

    Uses closed form: [n(n+1)/2]².

    Args:
        n: Non-negative integer.

    Returns:
        Sum of cubes from 1 to n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> sum_first_n_cubes(10)
        3025

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    s = n * (n + 1) // 2
    return s * s


def sum_first_n_powers(n: int, k: int) -> int:
    """Compute 1^k + 2^k + ··· + n^k.

    Args:
        n: Non-negative integer.
        k: Non-negative exponent.

    Returns:
        Sum of k-th powers from 1 to n.

    Raises:
        TypeError: If n or k is not an integer.
        ValueError: If n < 0 or k < 0.

    Usage Example:
        >>> sum_first_n_powers(5, 3)
        225

    Complexity: O(n)
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers.")
    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative.")
    return sum(i ** k for i in range(1, n + 1))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 22: Arithmetic Functions (2 of 2)
# ---------------------------------------------------------------------------

def triangular_number(n: int) -> int:
    """Compute the n-th triangular number T_n = n(n+1)/2.

    Args:
        n: Non-negative integer.

    Returns:
        The n-th triangular number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> triangular_number(10)
        55

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return n * (n + 1) // 2


def tetrahedral_number(n: int) -> int:
    """Compute the n-th tetrahedral number T_n = n(n+1)(n+2)/6.

    Args:
        n: Non-negative integer.

    Returns:
        The n-th tetrahedral number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> tetrahedral_number(5)
        35

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return n * (n + 1) * (n + 2) // 6


def square_pyramidal_number(n: int) -> int:
    """Compute the n-th square pyramidal number = n(n+1)(2n+1)/6.

    Sum of first n perfect squares.

    Args:
        n: Non-negative integer.

    Returns:
        The n-th square pyramidal number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> square_pyramidal_number(5)
        55

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return n * (n + 1) * (2 * n + 1) // 6


def is_narcissistic(n: int) -> bool:
    """Check if n is a narcissistic (Armstrong) number.

    A k-digit number where sum of each digit raised to k equals n.

    Args:
        n: Non-negative integer.

    Returns:
        True if n is narcissistic.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> is_narcissistic(153)
        True

    Complexity: O(log n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    digits = [int(d) for d in str(n)]
    k = len(digits)
    return sum(d ** k for d in digits) == n


def is_automorphic(n: int) -> bool:
    """Check if n is an automorphic number (n² ends with n).

    Args:
        n: Non-negative integer.

    Returns:
        True if n is automorphic.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> is_automorphic(76)
        True

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    sq = n * n
    return str(sq).endswith(str(n))


def is_happy_number(n: int) -> bool:
    """Check if n is a happy number.

    A number where iterated sum of squares of digits reaches 1.

    Args:
        n: Positive integer.

    Returns:
        True if n is happy.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> is_happy_number(19)
        True

    Complexity: O(log n × iterations)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))
    return n == 1


def cantor_pairing(a: int, b: int) -> int:
    """Compute the Cantor pairing function for two non-negative integers.

    π(a, b) = (a + b)(a + b + 1)/2 + b

    Args:
        a: Non-negative integer.
        b: Non-negative integer.

    Returns:
        Cantor pair number.

    Raises:
        TypeError: If a or b is not an integer.
        ValueError: If a < 0 or b < 0.

    Usage Example:
        >>> cantor_pairing(3, 4)
        32

    Complexity: O(1)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers.")
    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative.")
    return (a + b) * (a + b + 1) // 2 + b


def cantor_unpairing(z: int) -> tuple[int, int]:
    """Invert the Cantor pairing function.

    Args:
        z: Non-negative integer (Cantor pair number).

    Returns:
        Tuple (a, b) such that cantor_pairing(a, b) = z.

    Raises:
        TypeError: If z is not an integer.
        ValueError: If z < 0.

    Usage Example:
        >>> cantor_unpairing(32)
        (3, 4)

    Complexity: O(1)
    """
    if not isinstance(z, int):
        raise TypeError("z must be an integer.")
    if z < 0:
        raise ValueError("z must be non-negative.")
    w = int((math.sqrt(8 * z + 1) - 1) / 2)
    t = w * (w + 1) // 2
    b = z - t
    a = w - b
    return (a, b)


def stern_brocot(n: int) -> list[int]:
    """Generate the first n terms of the Stern-Brocot sequence.

    s(0)=0, s(1)=1, s(2k)=s(k), s(2k+1)=s(k)+s(k+1).

    Args:
        n: Number of terms to generate (≥ 1).

    Returns:
        List of first n terms.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> stern_brocot(10)
        [0, 1, 1, 2, 1, 3, 2, 3, 1, 4]

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    if n == 1:
        return [0]
    seq = [0, 1]
    for i in range(2, n):
        if i % 2 == 0:
            seq.append(seq[i // 2])
        else:
            seq.append(seq[i // 2] + seq[i // 2 + 1])
    return seq


def look_and_say(seed: str = "1", iterations: int = 5) -> str:
    """Generate the look-and-say sequence.

    Each term describes the digits of the previous term
    (e.g., "1" → "11" → "21" → "1211" → ...).

    Args:
        seed: Initial string (default "1").
        iterations: Number of iterations (default 5).

    Returns:
        The resulting string after iterations.

    Raises:
        TypeError: If seed is not a string or iterations is not int.
        ValueError: If iterations < 0.

    Usage Example:
        >>> look_and_say("1", 4)
        '111221'

    Complexity: O(iterations × len(string))
    """
    if not isinstance(seed, str):
        raise TypeError("seed must be a string.")
    if not isinstance(iterations, int):
        raise TypeError("iterations must be an integer.")
    if iterations < 0:
        raise ValueError("iterations must be non-negative.")
    current = seed
    for _ in range(iterations):
        result = []
        i = 0
        while i < len(current):
            ch = current[i]
            count = 1
            while i + count < len(current) and current[i + count] == ch:
                count += 1
            result.append(str(count) + ch)
            i += count
        current = "".join(result)
    return current

