"""Excel-compatible mathematical and trigonometric functions."""

import math
from typing import List, Union

from shortfx.fxNumeric.arithmetic_functions import (
    absolute_value as _core_abs,
    combinations as _core_combin,
    combinations_with_repetition as _core_combina,
    double_factorial as _core_double_factorial,
    exp as _core_exp,
    factorial as _core_factorial,
    gcd_list as _core_gcd_list,
    lcm_list as _core_lcm_list,
    modulo as _core_mod,
    natural_log as _core_ln,
    common_log as _core_log10,
    log_base_n as _core_log,
    matrix_determinant as _core_mdeterm,
    matrix_inverse as _core_minverse,
    matrix_multiply as _core_mmult,
    identity_matrix as _core_munit,
    power as _core_power,
    quotient as _core_quotient,
    series_sum as _core_series_sum,
    sign as _core_sign,
    square_root as _core_sqrt,
    sqrt_pi as _core_sqrtpi,
    sum_x2my2 as _core_sum_x2my2,
    sum_x2py2 as _core_sum_x2py2,
    sum_xmy2 as _core_sum_xmy2,
    matrix_transpose as _core_transpose,
)
from shortfx.fxNumeric.conversion_functions import (
    int_to_roman as _core_int_to_roman,
    roman_to_int as _core_roman_to_int,
    number_to_base as _core_number_to_base,
    base_to_decimal as _core_base_to_decimal,
)
from shortfx.fxNumeric.trigonometry_functions import (
    arccosine as _core_acos,
    arcsine as _core_asin,
    arctangent as _core_atan,
    arctangent2 as _core_atan2,
    cosecant as _core_csc,
    cosine as _core_cos,
    cotangent as _core_cot,
    degrees_to_radians as _core_radians,
    hyperbolic_cosecant as _core_csch,
    hyperbolic_cosine as _core_cosh,
    hyperbolic_cotangent as _core_coth,
    hyperbolic_secant as _core_sech,
    hyperbolic_sine as _core_sinh,
    hyperbolic_tangent as _core_tanh,
    inverse_hyperbolic_cosine as _core_acosh,
    inverse_hyperbolic_cotangent as _core_acoth,
    inverse_hyperbolic_sine as _core_asinh,
    inverse_hyperbolic_tangent as _core_atanh,
    radians_to_degrees as _core_degrees,
    secant as _core_sec,
    sine as _core_sin,
    tangent as _core_tan,
)
from shortfx.fxNumeric.rounding_functions import (
    ceiling_significance as _core_ceiling,
    ceiling_math as _core_ceiling_math,
    ceiling_precise as _core_ceiling_precise,
    even as _core_even,
    floor_significance as _core_floor,
    floor_math as _core_floor_math,
    floor_precise as _core_floor_precise,
    odd as _core_odd,
    round_to_n_decimals as _core_round,
    round_to_nearest_multiple as _core_mround,
)
from shortfx.fxNumeric.random_functions import (
    random_array as _core_random_array,
    random_float as _core_random_float,
    random_int as _core_random_int,
)
from shortfx.fxNumeric.statistics_functions import (
    calculate_standard_deviation as _core_std_dev,
    calculate_variance as _core_variance,
    aggregate as _core_aggregate,
    sum_if as _core_sum_if,
)


def ABS(number: float) -> float:
    """Returns the absolute value of a number.
    
    Description:
        Returns the absolute (positive) value of a number. Equivalent to
        Excel's ABS function.
    
    Args:
        number (float): The number for which to calculate the absolute value.
    
    Returns:
        float: The absolute value of the number.
    
    Usage Example:
        >>> ABS(-5.5)
        5.5
        >>> ABS(3)
        3
    
    Cost: O(1)
    """
    return _core_abs(number)


def ACOS(number: float) -> float:
    """Returns the arccosine of a number in radians.
    
    Description:
        Returns the inverse cosine (arccosine) of a number. The result is
        in radians between 0 and π. Equivalent to Excel's ACOS function.
    
    Args:
        number (float): The cosine value, must be between -1 and 1.
    
    Returns:
        float: The arccosine in radians.
    
    Raises:
        ValueError: If number is not between -1 and 1.
    
    Usage Example:
        >>> ACOS(0.5)
        1.0471975511965979
        >>> ACOS(1)
        0.0
    
    Cost: O(1)
    """
    if not -1 <= number <= 1:
        raise ValueError("Input must be between -1 and 1")
    return _core_acos(number)


def ACOSH(number: float) -> float:
    """Returns the inverse hyperbolic cosine of a number.
    
    Description:
        Returns the inverse hyperbolic cosine. Equivalent to Excel's
        ACOSH function.
    
    Args:
        number (float): A number greater than or equal to 1.
    
    Returns:
        float: The inverse hyperbolic cosine.
    
    Raises:
        ValueError: If number is less than 1.
    
    Usage Example:
        >>> ACOSH(1)
        0.0
        >>> ACOSH(10)
        2.993222846126381
    
    Cost: O(1)
    """
    if number < 1:
        raise ValueError("Input must be >= 1")
    return _core_acosh(number)


def ACOT(number: float) -> float:
    """Returns the arccotangent of a number in radians.
    
    Description:
        Returns the inverse cotangent (arccotangent) of a number.
        Equivalent to Excel's ACOT function.
    
    Args:
        number (float): The cotangent value.
    
    Returns:
        float: The arccotangent in radians.
    
    Usage Example:
        >>> ACOT(1)
        0.7853981633974483
        >>> ACOT(2)
        0.4636476090008061
    
    Cost: O(1)
    """
    return _core_atan(1 / number) if number != 0 else math.pi / 2


def ACOTH(number: float) -> float:
    """Returns the inverse hyperbolic cotangent of a number.
    
    Description:
        Returns the inverse hyperbolic cotangent. Equivalent to Excel's
        ACOTH function.
    
    Args:
        number (float): A number where |number| > 1.
    
    Returns:
        float: The inverse hyperbolic cotangent.
    
    Raises:
        ValueError: If |number| <= 1.
    
    Usage Example:
        >>> ACOTH(2)
        0.5493061443340548
        >>> ACOTH(-2)
        -0.5493061443340548
    
    Cost: O(1)
    """
    if abs(number) <= 1:
        raise ValueError("Input must satisfy |x| > 1")
    return _core_acoth(number)


def AGGREGATE(data: List[Union[int, float]], operation: str = "sum") -> float:
    """Returns an aggregate calculation from a list.
    
    Description:
        Performs aggregate operations on a list of numbers. Similar to
        Excel's AGGREGATE function (simplified version).
    
    Args:
        data (List[Union[int, float]]): List of numbers to aggregate.
        operation (str): Operation type: 'sum', 'avg', 'max', or 'min'.
    
    Returns:
        float: The aggregated result.
    
    Raises:
        ValueError: If list is empty or operation is invalid.
    
    Usage Example:
        >>> AGGREGATE([1, 2, 3, 4, 5], "sum")
        15
        >>> AGGREGATE([1, 2, 3, 4, 5], "avg")
        3.0
        >>> AGGREGATE([1, 2, 3, 4, 5], "max")
        5
    
    Cost: O(n) where n is the length of data
    """
    return _core_aggregate(data, operation)


def ASIN(number: float) -> float:
    """Returns the arcsine of a number in radians.
    
    Description:
        Returns the inverse sine (arcsine) of a number. The result is
        in radians between -π/2 and π/2. Equivalent to Excel's ASIN.
    
    Args:
        number (float): The sine value, must be between -1 and 1.
    
    Returns:
        float: The arcsine in radians.
    
    Raises:
        ValueError: If number is not between -1 and 1.
    
    Usage Example:
        >>> ASIN(0.5)
        0.5235987755982989
        >>> ASIN(1)
        1.5707963267948966
    
    Cost: O(1)
    """
    if not -1 <= number <= 1:
        raise ValueError("Input must be between -1 and 1")
    return _core_asin(number)


def ASINH(number: float) -> float:
    """Returns the inverse hyperbolic sine of a number.
    
    Description:
        Returns the inverse hyperbolic sine. Equivalent to Excel's
        ASINH function.
    
    Args:
        number (float): Any real number.
    
    Returns:
        float: The inverse hyperbolic sine.
    
    Usage Example:
        >>> ASINH(1)
        0.881373587019543
        >>> ASINH(-1)
        -0.881373587019543
    
    Cost: O(1)
    """
    return _core_asinh(number)


def ATAN(number: float) -> float:
    """Returns the arctangent of a number in radians.
    
    Description:
        Returns the inverse tangent (arctangent) of a number. The result
        is in radians between -π/2 and π/2. Equivalent to Excel's ATAN.
    
    Args:
        number (float): The tangent value.
    
    Returns:
        float: The arctangent in radians.
    
    Usage Example:
        >>> ATAN(1)
        0.7853981633974483
        >>> ATAN(0)
        0.0
    
    Cost: O(1)
    """
    return _core_atan(number)


def ATAN2(x: float, y: float) -> float:
    """Returns the arctangent from x and y coordinates.
    
    Description:
        Returns the arctangent of the specified x and y coordinates.
        Equivalent to Excel's ATAN2 function (note: Excel uses x, y order).
    
    Args:
        x (float): The x-coordinate.
        y (float): The y-coordinate.
    
    Returns:
        float: The arctangent in radians.
    
    Usage Example:
        >>> ATAN2(1, 1)
        0.7853981633974483
        >>> ATAN2(1, 0)
        1.5707963267948966
    
    Cost: O(1)
    """
    return _core_atan2(y, x)


def ATANH(number: float) -> float:
    """Returns the inverse hyperbolic tangent of a number.
    
    Description:
        Returns the inverse hyperbolic tangent. Equivalent to Excel's
        ATANH function.
    
    Args:
        number (float): A number between -1 and 1 (exclusive).
    
    Returns:
        float: The inverse hyperbolic tangent.
    
    Raises:
        ValueError: If number is not in the range (-1, 1).
    
    Usage Example:
        >>> ATANH(0.5)
        0.5493061443340548
        >>> ATANH(-0.5)
        -0.5493061443340548
    
    Cost: O(1)
    """
    if not -1 < number < 1:
        raise ValueError("Input must be between -1 and 1 (exclusive)")
    return _core_atanh(number)


def BASE(number: int, radix: int, min_length: int = 0) -> str:
    """Converts a number to text representation with a given base.
    
    Description:
        Converts a number into a text representation with the specified base.
        Equivalent to Excel's BASE function.
    
    Args:
        number (int): The number to convert (must be non-negative).
        radix (int): The base to convert to (between 2 and 36).
        min_length (int): Minimum length of returned string (pads with zeros).
    
    Returns:
        str: Text representation in the specified base.
    
    Raises:
        ValueError: If base is not between 2 and 36, or number is negative.
    
    Usage Example:
        >>> BASE(7, 2)
        '111'
        >>> BASE(100, 16)
        '64'
        >>> BASE(15, 2, 8)
        '00001111'
    
    Cost: O(log n) where n is the number
    """
    return _core_number_to_base(number, radix, min_length)


def CEILING(number: float, significance: float = 1) -> float:
    """Rounds a number up to the nearest multiple of significance.
    
    Description:
        Rounds a number up, away from zero, to the nearest multiple of
        significance. Equivalent to Excel's CEILING function.
    
    Args:
        number (float): The value to round.
        significance (float): The multiple to which to round.
    
    Returns:
        float: The rounded value.
    
    Usage Example:
        >>> CEILING(2.5, 1)
        3.0
        >>> CEILING(4.3, 0.5)
        4.5
        >>> CEILING(-2.5, -1)
        -2.0
    
    Cost: O(1)
    """
    if significance == 0:
        return 0
    return _core_ceiling(number, significance)


def CEILING_MATH(number: float, significance: float = 1, mode: int = 0) -> float:
    """Rounds a number up to nearest multiple with mode control.
    
    Description:
        Rounds a number up to the nearest integer or multiple of significance.
        Equivalent to Excel's CEILING.MATH function.
    
    Args:
        number (float): The value to round.
        significance (float): The multiple to which to round (default 1).
        mode (int): For negative numbers: 0 = away from zero, 1 = toward zero.
    
    Returns:
        float: The rounded value.
    
    Usage Example:
        >>> CEILING_MATH(2.5)
        3.0
        >>> CEILING_MATH(-2.5, 1, 0)
        -2.0
        >>> CEILING_MATH(-2.5, 1, 1)
        -3.0
    
    Cost: O(1)
    """
    return _core_ceiling_math(number, significance, mode)


def CEILING_PRECISE(number: float, significance: float = 1) -> float:
    """Rounds a number up to nearest multiple (always away from zero).
    
    Description:
        Rounds a number up to the nearest integer or multiple of significance,
        regardless of sign. Equivalent to Excel's CEILING.PRECISE.
    
    Args:
        number (float): The value to round.
        significance (float): The multiple to which to round (default 1).
    
    Returns:
        float: The rounded value.
    
    Usage Example:
        >>> CEILING_PRECISE(2.5, 1)
        3.0
        >>> CEILING_PRECISE(-2.5, 1)
        -2.0
    
    Cost: O(1)
    """
    return _core_ceiling_precise(number, significance)


def COMBIN(n: int, k: int) -> int:
    """Returns the number of combinations for given items.
    
    Description:
        Returns the number of combinations (without repetition) for a given
        number of items. Equivalent to Excel's COMBIN function.
    
    Args:
        n (int): Total number of items (must be >= 0).
        k (int): Number of items in each combination (must be 0 <= k <= n).
    
    Returns:
        int: The number of combinations.
    
    Raises:
        ValueError: If n < 0, k < 0, or k > n.
    
    Usage Example:
        >>> COMBIN(5, 2)
        10
        >>> COMBIN(10, 3)
        120
    
    Cost: O(k)
    """
    if n < 0 or k < 0 or k > n:
        raise ValueError("Invalid inputs: must have 0 <= k <= n and n >= 0")
    return _core_combin(n, k)


def COMBINA(n: int, k: int) -> int:
    """Returns the number of combinations with repetitions.
    
    Description:
        Returns the number of combinations (with repetition) for a given
        number of items. Equivalent to Excel's COMBINA function.
    
    Args:
        n (int): Total number of items (must be >= 0).
        k (int): Number of items in each combination (must be >= 0).
    
    Returns:
        int: The number of combinations with repetition.
    
    Raises:
        ValueError: If n < 0 or k < 0.
    
    Usage Example:
        >>> COMBINA(4, 3)
        20
        >>> COMBINA(3, 2)
        6
    
    Cost: O(k)
    """
    if n < 0 or k < 0:
        raise ValueError("Inputs must be non-negative")
    return _core_combina(n, k)


def COS(number: float) -> float:
    """Returns the cosine of an angle in radians.
    
    Description:
        Returns the cosine of the specified angle. Equivalent to Excel's
        COS function.
    
    Args:
        number (float): The angle in radians.
    
    Returns:
        float: The cosine of the angle.
    
    Usage Example:
        >>> COS(0)
        1.0
        >>> COS(math.pi)
        -1.0
    
    Cost: O(1)
    """
    return _core_cos(number)


def COSH(number: float) -> float:
    """Returns the hyperbolic cosine of a number.
    
    Description:
        Returns the hyperbolic cosine. Equivalent to Excel's COSH function.
    
    Args:
        number (float): Any real number.
    
    Returns:
        float: The hyperbolic cosine.
    
    Usage Example:
        >>> COSH(0)
        1.0
        >>> COSH(1)
        1.5430806348152437
    
    Cost: O(1)
    """
    return _core_cosh(number)


def COT(number: float) -> float:
    """Returns the cotangent of an angle in radians.
    
    Description:
        Returns the cotangent of the specified angle. Equivalent to Excel's
        COT function.
    
    Args:
        number (float): The angle in radians.
    
    Returns:
        float: The cotangent of the angle.
    
    Raises:
        ValueError: If cotangent is undefined at this angle.
    
    Usage Example:
        >>> COT(math.pi/4)
        1.0
        >>> COT(math.pi/6)
        1.7320508075688772
    
    Cost: O(1)
    """
    return _core_cot(number)


def COTH(number: float) -> float:
    """Returns the hyperbolic cotangent of a number.
    
    Description:
        Returns the hyperbolic cotangent. Equivalent to Excel's COTH function.
    
    Args:
        number (float): Any real number (except 0).
    
    Returns:
        float: The hyperbolic cotangent.
    
    Raises:
        ValueError: If number is 0.
    
    Usage Example:
        >>> COTH(1)
        1.3130352854993313
        >>> COTH(2)
        1.0373147207275482
    
    Cost: O(1)
    """
    return _core_coth(number)


def CSC(number: float) -> float:
    """Returns the cosecant of an angle in radians.
    
    Description:
        Returns the cosecant of the specified angle. Equivalent to Excel's
        CSC function.
    
    Args:
        number (float): The angle in radians.
    
    Returns:
        float: The cosecant of the angle.
    
    Raises:
        ValueError: If cosecant is undefined at this angle.
    
    Usage Example:
        >>> CSC(math.pi/2)
        1.0
        >>> CSC(math.pi/6)
        2.0
    
    Cost: O(1)
    """
    return _core_csc(number)


def CSCH(number: float) -> float:
    """Returns the hyperbolic cosecant of a number.
    
    Description:
        Returns the hyperbolic cosecant. Equivalent to Excel's CSCH function.
    
    Args:
        number (float): Any real number (except 0).
    
    Returns:
        float: The hyperbolic cosecant.
    
    Raises:
        ValueError: If number is 0.
    
    Usage Example:
        >>> CSCH(1)
        0.8509181282393216
        >>> CSCH(2)
        0.27572056477178325
    
    Cost: O(1)
    """
    return _core_csch(number)


def DECIMAL(text: str, radix: int) -> int:
    """Converts text representation of number in given base to decimal.
    
    Description:
        Converts a text string that represents a number in a given base
        to its decimal (base 10) equivalent. Equivalent to Excel's DECIMAL.
    
    Args:
        text (str): The text representation of the number.
        radix (int): The base of the number (between 2 and 36).
    
    Returns:
        int: The decimal equivalent.
    
    Raises:
        ValueError: If base is not between 2 and 36, or text is invalid.
    
    Usage Example:
        >>> DECIMAL("111", 2)
        7
        >>> DECIMAL("FF", 16)
        255
    
    Cost: O(n) where n is the length of text
    """
    return _core_base_to_decimal(text, radix)


def DEGREES(angle: float) -> float:
    """Converts radians to degrees.
    
    Description:
        Converts an angle in radians to degrees. Equivalent to Excel's
        DEGREES function.
    
    Args:
        angle (float): An angle in radians.
    
    Returns:
        float: The angle in degrees.
    
    Usage Example:
        >>> DEGREES(math.pi)
        180.0
        >>> DEGREES(math.pi/2)
        90.0
    
    Cost: O(1)
    """
    return _core_degrees(angle)


def EVEN(number: float) -> int:
    """Rounds a number up to the nearest even integer.
    
    Description:
        Rounds a number up to the nearest even integer. Positive numbers
        round up, negative numbers round down (away from zero).
        Equivalent to Excel's EVEN function.
    
    Args:
        number (float): The value to round.
    
    Returns:
        int: The nearest even integer.
    
    Usage Example:
        >>> EVEN(1.5)
        2
        >>> EVEN(3)
        4
        >>> EVEN(-1)
        -2
    
    Cost: O(1)
    """
    return _core_even(number)


def EXP(number: float) -> float:
    """Returns e raised to the power of a number.
    
    Description:
        Returns the constant e (approximately 2.71828) raised to the power
        of a number. Equivalent to Excel's EXP function.
    
    Args:
        number (float): The exponent.
    
    Returns:
        float: e^number.
    
    Usage Example:
        >>> EXP(1)
        2.718281828459045
        >>> EXP(0)
        1.0
    
    Cost: O(1)
    """
    return _core_exp(number)


def FACT(number: int) -> int:
    """Returns the factorial of a number.
    
    Description:
        Returns the factorial of a number (n!). Equivalent to Excel's
        FACT function.
    
    Args:
        number (int): A non-negative integer.
    
    Returns:
        int: The factorial.
    
    Raises:
        ValueError: If number is negative.
    
    Usage Example:
        >>> FACT(5)
        120
        >>> FACT(0)
        1
    
    Cost: O(n)
    """
    return _core_factorial(number)


def FACTDOUBLE(number: int) -> int:
    """Returns the double factorial of a number.
    
    Description:
        Returns the double factorial of a number (n!!). For even numbers,
        multiplies all even integers; for odd, multiplies all odd integers.
        Equivalent to Excel's FACTDOUBLE function.
    
    Args:
        number (int): A non-negative integer.
    
    Returns:
        int: The double factorial.
    
    Raises:
        ValueError: If number is negative.
    
    Usage Example:
        >>> FACTDOUBLE(6)
        48
        >>> FACTDOUBLE(5)
        15
    
    Cost: O(n)
    """
    return _core_double_factorial(number)


def FLOOR(number: float, significance: float = 1) -> float:
    """Rounds a number down to the nearest multiple of significance.
    
    Description:
        Rounds a number down, toward zero, to the nearest multiple of
        significance. Equivalent to Excel's FLOOR function.
    
    Args:
        number (float): The value to round.
        significance (float): The multiple to which to round.
    
    Returns:
        float: The rounded value.
    
    Usage Example:
        >>> FLOOR(3.7, 1)
        3.0
        >>> FLOOR(2.5, 0.1)
        2.5
    
    Cost: O(1)
    """
    if significance == 0:
        return 0
    return _core_floor(number, significance)


def FLOOR_MATH(number: float, significance: float = 1, mode: int = 0) -> float:
    """Rounds a number down to nearest multiple with mode control.
    
    Description:
        Rounds a number down to the nearest integer or multiple of significance.
        Equivalent to Excel's FLOOR.MATH function.
    
    Args:
        number (float): The value to round.
        significance (float): The multiple to which to round (default 1).
        mode (int): For negative numbers: 0 = toward zero, 1 = away from zero.
    
    Returns:
        float: The rounded value.
    
    Usage Example:
        >>> FLOOR_MATH(3.7)
        3.0
        >>> FLOOR_MATH(-2.5, 1, 0)
        -2.0
        >>> FLOOR_MATH(-2.5, 1, 1)
        -3.0
    
    Cost: O(1)
    """
    return _core_floor_math(number, significance, mode)


def FLOOR_PRECISE(number: float, significance: float = 1) -> float:
    """Rounds a number down to nearest multiple (always toward zero).
    
    Description:
        Rounds a number down to the nearest integer or multiple of significance,
        regardless of sign. Equivalent to Excel's FLOOR.PRECISE.
    
    Args:
        number (float): The value to round.
        significance (float): The multiple to which to round (default 1).
    
    Returns:
        float: The rounded value.
    
    Usage Example:
        >>> FLOOR_PRECISE(3.7, 1)
        3.0
        >>> FLOOR_PRECISE(-2.5, 1)
        -2.0
    
    Cost: O(1)
    """
    return _core_floor_precise(number, significance)


def GCD(*numbers: int) -> int:
    """Returns the greatest common divisor of integers.
    
    Description:
        Returns the greatest common divisor of two or more integers.
        Equivalent to Excel's GCD function.
    
    Args:
        *numbers (int): One or more integers.
    
    Returns:
        int: The greatest common divisor.
    
    Raises:
        ValueError: If no numbers are provided.
    
    Usage Example:
        >>> GCD(12, 18)
        6
        >>> GCD(15, 25, 35)
        5
    
    Cost: O(n * log(min)) where n is number count
    """
    if not numbers:
        raise ValueError("At least one number required")
    return _core_gcd_list(list(numbers))


def INT(number: float) -> int:
    """Rounds a number down to the nearest integer.
    
    Description:
        Rounds a number down to the nearest integer (toward negative infinity).
        Equivalent to Excel's INT function.
    
    Args:
        number (float): The value to round.
    
    Returns:
        int: The nearest integer (rounded down).
    
    Usage Example:
        >>> INT(8.9)
        8
        >>> INT(-8.9)
        -9
    
    Cost: O(1)
    """
    return int(_core_floor(number, 1))


def ISO_CEILING(number: float, significance: float = 1) -> float:
    """Rounds a number up to nearest multiple (ISO standard).
    
    Description:
        Rounds a number up to the nearest integer or multiple of significance.
        Equivalent to Excel's ISO.CEILING function.
    
    Args:
        number (float): The value to round.
        significance (float): The multiple to which to round (default 1).
    
    Returns:
        float: The rounded value.
    
    Usage Example:
        >>> ISO_CEILING(2.5)
        3.0
        >>> ISO_CEILING(-2.5)
        -2.0
    
    Cost: O(1)
    """
    return CEILING_PRECISE(number, significance)


def LCM(*numbers: int) -> int:
    """Returns the least common multiple of integers.
    
    Description:
        Returns the least common multiple of two or more integers.
        Equivalent to Excel's LCM function.
    
    Args:
        *numbers (int): One or more integers.
    
    Returns:
        int: The least common multiple.
    
    Raises:
        ValueError: If no numbers are provided.
    
    Usage Example:
        >>> LCM(12, 18)
        36
        >>> LCM(4, 6, 8)
        24
    
    Cost: O(n * log(min)) where n is number count
    """
    if not numbers:
        raise ValueError("At least one number required")
    return _core_lcm_list(list(numbers))


def LN(number: float) -> float:
    """Returns the natural logarithm of a number.
    
    Description:
        Returns the natural logarithm (base e) of a number.
        Equivalent to Excel's LN function.
    
    Args:
        number (float): A positive number.
    
    Returns:
        float: The natural logarithm.
    
    Raises:
        ValueError: If number is not positive.
    
    Usage Example:
        >>> LN(math.e)
        1.0
        >>> LN(10)
        2.302585092994046
    
    Cost: O(1)
    """
    if number <= 0:
        raise ValueError("Input must be positive")
    return _core_ln(number)


def LOG(number: float, base: float = 10) -> float:
    """Returns the logarithm of a number to a specified base.
    
    Description:
        Returns the logarithm of a number to the specified base.
        Equivalent to Excel's LOG function.
    
    Args:
        number (float): A positive number.
        base (float): The base of the logarithm (default 10).
    
    Returns:
        float: The logarithm.
    
    Raises:
        ValueError: If number <= 0, base <= 0, or base = 1.
    
    Usage Example:
        >>> LOG(100, 10)
        2.0
        >>> LOG(8, 2)
        3.0
    
    Cost: O(1)
    """
    if number <= 0 or base <= 0 or base == 1:
        raise ValueError("Invalid inputs for logarithm")
    return _core_log(number, base)


def LOG10(number: float) -> float:
    """Returns the base-10 logarithm of a number.
    
    Description:
        Returns the common (base 10) logarithm of a number.
        Equivalent to Excel's LOG10 function.
    
    Args:
        number (float): A positive number.
    
    Returns:
        float: The base-10 logarithm.
    
    Raises:
        ValueError: If number is not positive.
    
    Usage Example:
        >>> LOG10(100)
        2.0
        >>> LOG10(1000)
        3.0
    
    Cost: O(1)
    """
    if number <= 0:
        raise ValueError("Input must be positive")
    return _core_log10(number)


def MOD(number: float, divisor: float) -> float:
    """Returns the remainder from division.
    
    Description:
        Returns the remainder after a number is divided by a divisor.
        The result has the same sign as the divisor.
        Equivalent to Excel's MOD function.
    
    Args:
        number (float): The number to divide.
        divisor (float): The divisor (cannot be zero).
    
    Returns:
        float: The remainder.
    
    Raises:
        ValueError: If divisor is zero.
    
    Usage Example:
        >>> MOD(10, 3)
        1.0
        >>> MOD(-10, 3)
        2.0
    
    Cost: O(1)
    """
    if divisor == 0:
        raise ValueError("Divisor cannot be zero")
    return _core_mod(number, divisor)


def MDETERM(matrix: List[List[float]]) -> float:
    """Returns the matrix determinant of an array.
    
    Description:
        Returns the determinant of a square matrix. Equivalent to Excel's
        MDETERM function.
    
    Args:
        matrix (List[List[float]]): A square matrix.
    
    Returns:
        float: The determinant.
    
    Raises:
        ValueError: If matrix is not square.
    
    Usage Example:
        >>> MDETERM([[1, 2], [3, 4]])
        -2.0
        >>> MDETERM([[2, 0], [0, 2]])
        4.0
    
    Cost: O(n³) where n is matrix dimension
    """
    return _core_mdeterm(matrix)


def MINVERSE(matrix: List[List[float]]) -> List[List[float]]:
    """Returns the inverse of a square matrix.
    
    Description:
        Returns the inverse matrix of a given square matrix.
        Equivalent to Excel's MINVERSE function.
    
    Args:
        matrix (List[List[float]]): A square, invertible matrix.
    
    Returns:
        List[List[float]]: The inverse matrix.
    
    Raises:
        ValueError: If matrix is not square or not invertible.
    
    Usage Example:
        >>> MINVERSE([[1, 2], [3, 4]])
        [[-2.0, 1.0], [1.5, -0.5]]
    
    Cost: O(n³) where n is matrix dimension
    """
    return _core_minverse(matrix)


def ODD(number: float) -> int:
    """Rounds a number up to the nearest odd integer.
    
    Description:
        Rounds a number up to the nearest odd integer. Positive numbers
        round up, negative numbers round down (away from zero).
        Equivalent to Excel's ODD function.
    
    Args:
        number (float): The value to round.
    
    Returns:
        int: The nearest odd integer.
    
    Usage Example:
        >>> ODD(1.5)
        3
        >>> ODD(2)
        3
        >>> ODD(-2)
        -3
    
    Cost: O(1)
    """
    return _core_odd(number)


def PI() -> float:
    """Returns the value of pi (π).
    
    Description:
        Returns the mathematical constant π (pi), accurate to 15 digits.
        Equivalent to Excel's PI function.
    
    Returns:
        float: The value of π.
    
    Usage Example:
        >>> PI()
        3.141592653589793
    
    Cost: O(1)
    """
    return math.pi


def POWER(number: float, power: float) -> float:
    """Returns the result of a number raised to a power.
    
    Description:
        Returns the result of a number raised to a power.
        Equivalent to Excel's POWER function.
    
    Args:
        number (float): The base number.
        power (float): The exponent.
    
    Returns:
        float: number^power.
    
    Usage Example:
        >>> POWER(5, 2)
        25.0
        >>> POWER(2, 0.5)
        1.4142135623730951
    
    Cost: O(1)
    """
    return _core_power(number, power)


def RADIANS(angle: float) -> float:
    """Converts degrees to radians.
    
    Description:
        Converts an angle in degrees to radians. Equivalent to Excel's
        RADIANS function.
    
    Args:
        angle (float): An angle in degrees.
    
    Returns:
        float: The angle in radians.
    
    Usage Example:
        >>> RADIANS(180)
        3.141592653589793
        >>> RADIANS(90)
        1.5707963267948966
    
    Cost: O(1)
    """
    return _core_radians(angle)


def ARABIC(roman: str) -> int:
    """Converts a Roman numeral to an Arabic number.
    
    Description:
        Converts text in Roman numeral format to an Arabic numeral.
        Equivalent to Excel's ARABIC function.
    
    Args:
        roman (str): A valid Roman numeral string.
    
    Returns:
        int: The Arabic numeral equivalent.
    
    Raises:
        ValueError: If the string is not a valid Roman numeral.
    
    Usage Example:
        >>> ARABIC('MCMLXXXIV')
        1984
        >>> ARABIC('CDXCIX')
        499
    
    Cost: O(n) where n is the length of the Roman numeral
    """
    return _core_roman_to_int(roman)


def ROMAN(number: int, form: int = 0) -> str:
    """Converts an Arabic number to Roman numeral as text.
    
    Description:
        Converts an Arabic numeral to Roman numeral format.
        Equivalent to Excel's ROMAN function.
    
    Args:
        number (int): The number to convert (1 to 3999).
        form (int): Simplification level (0-4, default 0 = classic).
    
    Returns:
        str: The Roman numeral.
    
    Raises:
        ValueError: If number is not in range 1-3999.
    
    Usage Example:
        >>> ROMAN(1984)
        'MCMLXXXIV'
        >>> ROMAN(499)
        'CDXCIX'
    
    Cost: O(1)
    """
    return _core_int_to_roman(number)


def ROUND(number: float, num_digits: int = 0) -> float:
    """Rounds a number to a specified number of digits.
    
    Description:
        Rounds a number to the specified number of decimal places.
        Equivalent to Excel's ROUND function.
    
    Args:
        number (float): The number to round.
        num_digits (int): Number of decimal places (can be negative).
    
    Returns:
        float: The rounded number.
    
    Usage Example:
        >>> ROUND(2.15, 1)
        2.1
        >>> ROUND(2.149, 1)
        2.1
        >>> ROUND(-1.475, 2)
        -1.48
    
    Cost: O(1)
    """
    return _core_round(number, num_digits)


def ROUNDDOWN(number: float, num_digits: int = 0) -> float:
    """Rounds a number down (toward zero).
    
    Description:
        Rounds a number down, toward zero, to a specified number of digits.
        Equivalent to Excel's ROUNDDOWN function.
    
    Args:
        number (float): The number to round down.
        num_digits (int): Number of decimal places (can be negative).
    
    Returns:
        float: The rounded down number.
    
    Usage Example:
        >>> ROUNDDOWN(3.14159, 2)
        3.14
        >>> ROUNDDOWN(-3.14159, 2)
        -3.14
    
    Cost: O(1)
    """
    multiplier = 10 ** num_digits
    return math.floor(number * multiplier) / multiplier if number > 0 else math.ceil(number * multiplier) / multiplier


def ROUNDUP(number: float, num_digits: int = 0) -> float:
    """Rounds a number up (away from zero).
    
    Description:
        Rounds a number up, away from zero, to a specified number of digits.
        Equivalent to Excel's ROUNDUP function.
    
    Args:
        number (float): The number to round up.
        num_digits (int): Number of decimal places (can be negative).
    
    Returns:
        float: The rounded up number.
    
    Usage Example:
        >>> ROUNDUP(3.14159, 2)
        3.15
        >>> ROUNDUP(-3.14159, 2)
        -3.15
    
    Cost: O(1)
    """
    multiplier = 10 ** num_digits
    return math.ceil(number * multiplier) / multiplier if number > 0 else math.floor(number * multiplier) / multiplier


def SEC(number: float) -> float:
    """Returns the secant of an angle in radians.
    
    Description:
        Returns the secant of the specified angle. Equivalent to Excel's
        SEC function.
    
    Args:
        number (float): The angle in radians.
    
    Returns:
        float: The secant of the angle.
    
    Raises:
        ValueError: If secant is undefined at this angle.
    
    Usage Example:
        >>> SEC(0)
        1.0
        >>> SEC(math.pi/3)
        2.0
    
    Cost: O(1)
    """
    return _core_sec(number)


def SECH(number: float) -> float:
    """Returns the hyperbolic secant of a number.
    
    Description:
        Returns the hyperbolic secant. Equivalent to Excel's SECH function.
    
    Args:
        number (float): Any real number.
    
    Returns:
        float: The hyperbolic secant.
    
    Usage Example:
        >>> SECH(0)
        1.0
        >>> SECH(1)
        0.6480542736638855
    
    Cost: O(1)
    """
    return _core_sech(number)


def SIGN(number: float) -> int:
    """Returns the sign of a number.
    
    Description:
        Returns 1 if number is positive, -1 if negative, 0 if zero.
        Equivalent to Excel's SIGN function.
    
    Args:
        number (float): Any real number.
    
    Returns:
        int: The sign (-1, 0, or 1).
    
    Usage Example:
        >>> SIGN(10)
        1
        >>> SIGN(-5)
        -1
        >>> SIGN(0)
        0
    
    Cost: O(1)
    """
    return _core_sign(number)


def SIN(number: float) -> float:
    """Returns the sine of an angle in radians.
    
    Description:
        Returns the sine of the specified angle. Equivalent to Excel's
        SIN function.
    
    Args:
        number (float): The angle in radians.
    
    Returns:
        float: The sine of the angle.
    
    Usage Example:
        >>> SIN(math.pi/2)
        1.0
        >>> SIN(0)
        0.0
    
    Cost: O(1)
    """
    return _core_sin(number)


def SINH(number: float) -> float:
    """Returns the hyperbolic sine of a number.
    
    Description:
        Returns the hyperbolic sine. Equivalent to Excel's SINH function.
    
    Args:
        number (float): Any real number.
    
    Returns:
        float: The hyperbolic sine.
    
    Usage Example:
        >>> SINH(1)
        1.1752011936438014
        >>> SINH(0)
        0.0
    
    Cost: O(1)
    """
    return _core_sinh(number)


def SQRT(number: float) -> float:
    """Returns the positive square root of a number.
    
    Description:
        Returns the square root of a number. Equivalent to Excel's SQRT.
    
    Args:
        number (float): A non-negative number.
    
    Returns:
        float: The square root.
    
    Raises:
        ValueError: If number is negative.
    
    Usage Example:
        >>> SQRT(16)
        4.0
        >>> SQRT(2)
        1.4142135623730951
    
    Cost: O(1)
    """
    if number < 0:
        raise ValueError("Cannot compute square root of negative number")
    return _core_sqrt(number)


def SQRTPI(number: float) -> float:
    """Returns the square root of (number * pi).
    
    Description:
        Returns the square root of a number multiplied by π.
        Equivalent to Excel's SQRTPI function.
    
    Args:
        number (float): A non-negative number.
    
    Returns:
        float: The square root of (number * π).
    
    Raises:
        ValueError: If number is negative.
    
    Usage Example:
        >>> SQRTPI(1)
        1.7724538509055159
        >>> SQRTPI(2)
        2.5066282746310002
    
    Cost: O(1)
    """
    if number < 0:
        raise ValueError("Number must be non-negative")
    return _core_sqrtpi(number)


def TAN(number: float) -> float:
    """Returns the tangent of an angle in radians.
    
    Description:
        Returns the tangent of the specified angle. Equivalent to Excel's
        TAN function.
    
    Args:
        number (float): The angle in radians.
    
    Returns:
        float: The tangent of the angle.
    
    Usage Example:
        >>> TAN(math.pi/4)
        1.0
        >>> TAN(0)
        0.0
    
    Cost: O(1)
    """
    return _core_tan(number)


def TANH(number: float) -> float:
    """Returns the hyperbolic tangent of a number.
    
    Description:
        Returns the hyperbolic tangent. Equivalent to Excel's TANH function.
    
    Args:
        number (float): Any real number.
    
    Returns:
        float: The hyperbolic tangent.
    
    Usage Example:
        >>> TANH(0)
        0.0
        >>> TANH(1)
        0.7615941559557649
    
    Cost: O(1)
    """
    return _core_tanh(number)


def TRUNC(number: float, num_digits: int = 0) -> float:
    """Truncates a number to an integer by removing decimals.
    
    Description:
        Truncates a number to an integer by removing the fractional part.
        Equivalent to Excel's TRUNC function.
    
    Args:
        number (float): The number to truncate.
        num_digits (int): Number of decimal places to preserve (default 0).
    
    Returns:
        float: The truncated number.
    
    Usage Example:
        >>> TRUNC(8.9)
        8.0
        >>> TRUNC(-8.9)
        -8.0
        >>> TRUNC(8.9876, 2)
        8.98
    
    Cost: O(1)
    """
    multiplier = 10 ** num_digits
    return math.trunc(number * multiplier) / multiplier


def SUM(*numbers: Union[float, List[float]]) -> float:
    """Returns the sum of numbers.
    
    Description:
        Adds all the numbers in a range of cells or provided as arguments.
        Equivalent to Excel's SUM function.
    
    Args:
        *numbers: One or more numbers or lists of numbers to sum.
    
    Returns:
        float: The sum of all numbers.
    
    Usage Example:
        >>> SUM(1, 2, 3)
        6
        >>> SUM([1, 2, 3], 4, 5)
        15
        >>> SUM([10, 20], [30, 40])
        100
    
    Cost: O(n) where n is total number of values
    """
    total = 0
    for item in numbers:
        if isinstance(item, (list, tuple)):
            total += sum(x for x in item if isinstance(x, (int, float)))
        elif isinstance(item, (int, float)):
            total += item
    return total


def SUMIF(values: List[Union[int, float]], criteria: str) -> float:
    """Sums numbers that meet a specified criterion.
    
    Description:
        Adds the cells specified by a given criteria. Equivalent to
        Excel's SUMIF function.
    
    Args:
        values (List[Union[int, float]]): List of numbers to evaluate.
        criteria (str): Condition as string (e.g., ">10", "<=5", "=3").
    
    Returns:
        float: Sum of numbers that meet the criterion.
    
    Raises:
        ValueError: If criteria format is invalid.
    
    Usage Example:
        >>> SUMIF([1, 5, 10, 15, 20], ">10")
        35
        >>> SUMIF([2, 4, 6, 8, 10], "<=5")
        6
        >>> SUMIF([1, 2, 3, 4, 5], ">=3")
        12
    
    Cost: O(n) where n is the length of values
    """
    return _core_sum_if(values, values, criteria)


def MMULT(matrix1: List[List[float]], matrix2: List[List[float]]) -> List[List[float]]:
    """Returns the matrix product of two arrays.
    
    Description:
        Returns the matrix product of two arrays. The result is an array with
        the same number of rows as matrix1 and columns as matrix2.
        Equivalent to Excel's MMULT function.
    
    Args:
        matrix1 (List[List[float]]): The first matrix.
        matrix2 (List[List[float]]): The second matrix.
    
    Returns:
        List[List[float]]: The matrix product.
    
    Raises:
        ValueError: If matrices cannot be multiplied (columns of matrix1 must equal rows of matrix2).
    
    Usage Example:
        >>> MMULT([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        [[19, 22], [43, 50]]
        >>> MMULT([[1, 2, 3]], [[4], [5], [6]])
        [[32]]
    
    Cost: O(n * m * p) where n, m, p are matrix dimensions
    """
    return _core_mmult(matrix1, matrix2)


def MROUND(number: float, multiple: float) -> float:
    """Rounds a number to the nearest multiple.
    
    Description:
        Rounds a number to the nearest multiple of a specified value.
        Equivalent to Excel's MROUND function.
    
    Args:
        number (float): The number to round.
        multiple (float): The multiple to which to round.
    
    Returns:
        float: The rounded number.
    
    Raises:
        ValueError: If number and multiple have different signs.
    
    Usage Example:
        >>> MROUND(10, 3)
        9.0
        >>> MROUND(1.3, 0.2)
        1.4
        >>> MROUND(-10, -3)
        -9.0
    
    Cost: O(1)
    """
    if multiple == 0:
        return 0
    
    if (number > 0 and multiple < 0) or (number < 0 and multiple > 0):
        raise ValueError("Number and multiple must have the same sign")
    
    return _core_mround(number, multiple)


def MULTINOMIAL(*numbers: int) -> int:
    """Returns the multinomial of a set of numbers.
    
    Description:
        Returns the ratio of the factorial of a sum of values to the product
        of factorials. Equivalent to Excel's MULTINOMIAL function.
    
    Args:
        *numbers (int): One or more non-negative integers.
    
    Returns:
        int: The multinomial coefficient.
    
    Raises:
        ValueError: If any number is negative.
    
    Usage Example:
        >>> MULTINOMIAL(2, 3, 4)
        1260
        >>> MULTINOMIAL(3, 3)
        20
    
    Cost: O(n) where n is the sum of all numbers
    """
    from shortfx.fxPython.py_itertools import multinomial as _core_multinomial

    return _core_multinomial(*numbers)


def MUNIT(dimension: int) -> List[List[float]]:
    """Returns the identity matrix for the specified dimension.
    
    Description:
        Returns a square identity matrix of the specified size.
        Equivalent to Excel's MUNIT function.
    
    Args:
        dimension (int): The size of the identity matrix (must be positive).
    
    Returns:
        List[List[float]]: The identity matrix.
    
    Raises:
        ValueError: If dimension is not positive.
    
    Usage Example:
        >>> MUNIT(3)
        [[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]]
        >>> MUNIT(2)
        [[1.0, 0.0], [0.0, 1.0]]
    
    Cost: O(n²) where n is the dimension
    """
    return _core_munit(dimension)


def PRODUCT(*numbers: Union[float, List[float]]) -> float:
    """Returns the product of numbers.
    
    Description:
        Multiplies all the numbers given as arguments and returns the product.
        Equivalent to Excel's PRODUCT function.
    
    Args:
        *numbers: One or more numbers or lists of numbers to multiply.
    
    Returns:
        float: The product of all numbers.
    
    Usage Example:
        >>> PRODUCT(5, 15, 30)
        2250
        >>> PRODUCT([2, 3], 4)
        24
        >>> PRODUCT([1, 2, 3, 4])
        24
    
    Cost: O(n) where n is total number of values
    """
    result = 1
    for item in numbers:
        if isinstance(item, (list, tuple)):
            for x in item:
                if isinstance(x, (int, float)):
                    result *= x
        elif isinstance(item, (int, float)):
            result *= item
    return result


def QUOTIENT(numerator: float, denominator: float) -> int:
    """Returns the integer portion of a division.
    
    Description:
        Returns the integer portion of a division, discarding the remainder.
        Equivalent to Excel's QUOTIENT function.
    
    Args:
        numerator (float): The dividend.
        denominator (float): The divisor.
    
    Returns:
        int: The integer part of the division.
    
    Raises:
        ValueError: If denominator is zero.
    
    Usage Example:
        >>> QUOTIENT(10, 3)
        3
        >>> QUOTIENT(-10, 3)
        -3
        >>> QUOTIENT(5.5, 2)
        2
    
    Cost: O(1)
    """
    return _core_quotient(numerator, denominator)


def RAND() -> float:
    """Returns a random number between 0 and 1.
    
    Description:
        Returns an evenly distributed random real number greater than or
        equal to 0 and less than 1. Equivalent to Excel's RAND function.
    
    Returns:
        float: A random number between 0 and 1.
    
    Usage Example:
        >>> result = RAND()
        >>> 0 <= result < 1
        True
    
    Cost: O(1)
    """
    return _core_random_float(0.0, 1.0)


def RANDBETWEEN(bottom: int, top: int) -> int:
    """Returns a random integer between two numbers.
    
    Description:
        Returns a random integer between the numbers you specify.
        Equivalent to Excel's RANDBETWEEN function.
    
    Args:
        bottom (int): The smallest integer to return.
        top (int): The largest integer to return.
    
    Returns:
        int: A random integer between bottom and top (inclusive).
    
    Raises:
        ValueError: If bottom > top.
    
    Usage Example:
        >>> result = RANDBETWEEN(1, 10)
        >>> 1 <= result <= 10
        True
        >>> result = RANDBETWEEN(-5, 5)
        >>> -5 <= result <= 5
        True
    
    Cost: O(1)
    """
    if bottom > top:
        raise ValueError("Bottom must be less than or equal to top")
    
    return _core_random_int(bottom, top)


def RANDARRAY(rows: int = 1, columns: int = 1, min_val: float = 0, 
              max_val: float = 1, whole_number: bool = False) -> List[List[float]]:
    """Returns an array of random numbers.
    
    Description:
        Returns an array of random numbers between 0 and 1. You can specify
        the number of rows and columns, minimum and maximum values, and
        whether to return whole numbers or decimal values.
        Equivalent to Excel's RANDARRAY function.
    
    Args:
        rows (int): Number of rows (default 1).
        columns (int): Number of columns (default 1).
        min_val (float): Minimum value (default 0).
        max_val (float): Maximum value (default 1).
        whole_number (bool): Return integers if True, decimals if False (default False).
    
    Returns:
        List[List[float]]: Array of random numbers.
    
    Raises:
        ValueError: If rows or columns are not positive, or min_val >= max_val.
    
    Usage Example:
        >>> result = RANDARRAY(2, 3)
        >>> len(result) == 2 and len(result[0]) == 3
        True
        >>> result = RANDARRAY(2, 2, 1, 10, True)
        >>> all(1 <= x <= 10 and isinstance(x, (int, float)) for row in result for x in row)
        True
    
    Cost: O(rows * columns)
    """
    if rows <= 0 or columns <= 0:
        raise ValueError("Rows and columns must be positive")
    if min_val >= max_val:
        raise ValueError("Min value must be less than max value")
    
    return _core_random_array(rows, columns, min_val, max_val, whole_number)


def SEQUENCE(rows: int, columns: int = 1, start: float = 1, step: float = 1) -> List[List[float]]:
    """Generates a list of sequential numbers in an array.
    
    Description:
        Generates a list of sequential numbers in an array, such as 1, 2, 3, 4.
        Equivalent to Excel's SEQUENCE function.
    
    Args:
        rows (int): Number of rows to return.
        columns (int): Number of columns to return (default 1).
        start (float): First number in the sequence (default 1).
        step (float): Amount to increment each value (default 1).
    
    Returns:
        List[List[float]]: Array of sequential numbers.
    
    Raises:
        ValueError: If rows or columns are not positive.
    
    Usage Example:
        >>> SEQUENCE(3)
        [[1], [2], [3]]
        >>> SEQUENCE(2, 3, 0, 5)
        [[0, 5, 10], [15, 20, 25]]
        >>> SEQUENCE(1, 4, 10, -2)
        [[10, 8, 6, 4]]
    
    Cost: O(rows * columns)
    """
    from shortfx.fxPython.py_operations import sequence as _core_sequence

    return _core_sequence(rows, columns, start, step)


def SERIESSUM(x: float, n: int, m: int, coefficients: List[float]) -> float:
    """Returns the sum of a power series.
    
    Description:
        Returns the sum of a power series based on the formula:
        SERIESSUM(x,n,m,a) = a1*x^n + a2*x^(n+m) + a3*x^(n+2m) + ... + ai*x^(n+(i-1)m)
        Equivalent to Excel's SERIESSUM function.
    
    Args:
        x (float): The input value to the power series.
        n (int): The initial power to which x is raised.
        m (int): The step by which to increase n for each term.
        coefficients (List[float]): Array of coefficients.
    
    Returns:
        float: The sum of the power series.
    
    Usage Example:
        >>> SERIESSUM(2, 1, 2, [1, 1, 1])
        42.0
        >>> SERIESSUM(1, 0, 1, [1, 2, 3])
        6.0
    
    Cost: O(k) where k is the number of coefficients
    """
    return float(_core_series_sum(x, n, m, coefficients))


def SUBTOTAL(function_num: int, *values: Union[float, List[float]]) -> float:
    """Returns a subtotal in a list or database.
    
    Description:
        Returns a subtotal in a list or database using a specified function.
        Equivalent to Excel's SUBTOTAL function.
        Function numbers: 1=AVERAGE, 2=COUNT, 3=COUNTA, 4=MAX, 5=MIN,
        6=PRODUCT, 7=STDEV, 8=STDEVP, 9=SUM, 10=VAR, 11=VARP
    
    Args:
        function_num (int): Number specifying which function to use (1-11).
        *values: One or more numbers or lists to process.
    
    Returns:
        float: The calculated subtotal.
    
    Raises:
        ValueError: If function_num is not between 1 and 11.
    
    Usage Example:
        >>> SUBTOTAL(9, [1, 2, 3, 4, 5])  # SUM
        15
        >>> SUBTOTAL(1, [10, 20, 30])  # AVERAGE
        20.0
        >>> SUBTOTAL(4, [5, 15, 25])  # MAX
        25
    
    Cost: O(n) where n is total number of values
    """
    # Flatten all values
    all_numbers = []
    for item in values:
        if isinstance(item, (list, tuple)):
            all_numbers.extend(x for x in item if isinstance(x, (int, float)))
        elif isinstance(item, (int, float)):
            all_numbers.append(item)
    
    if not all_numbers:
        raise ValueError("No numbers to process")
    
    # Execute function based on function_num
    if function_num == 1:  # AVERAGE
        return sum(all_numbers) / len(all_numbers)
    elif function_num == 2:  # COUNT
        return len(all_numbers)
    elif function_num == 3:  # COUNTA
        return len(all_numbers)
    elif function_num == 4:  # MAX
        return max(all_numbers)
    elif function_num == 5:  # MIN
        return min(all_numbers)
    elif function_num == 6:  # PRODUCT
        result = 1
        for num in all_numbers:
            result *= num
        return result
    elif function_num == 7:  # STDEV (sample)
        return _core_std_dev(all_numbers, sample=True)
    elif function_num == 8:  # STDEVP (population)
        return _core_std_dev(all_numbers, sample=False)
    elif function_num == 9:  # SUM
        return sum(all_numbers)
    elif function_num == 10:  # VAR (sample)
        return _core_variance(all_numbers, sample=True)
    elif function_num == 11:  # VARP (population)
        return _core_variance(all_numbers, sample=False)
    else:
        raise ValueError("Function number must be between 1 and 11")


def SUMPRODUCT(*arrays: List[Union[int, float]]) -> float:
    """Returns the sum of the products of corresponding array components.
    
    Description:
        Multiplies corresponding components in the given arrays, and returns
        the sum of those products. Equivalent to Excel's SUMPRODUCT function.
    
    Args:
        *arrays: Two or more arrays of the same length.
    
    Returns:
        float: The sum of products.
    
    Raises:
        ValueError: If arrays have different lengths or no arrays provided.
    
    Usage Example:
        >>> SUMPRODUCT([1, 2, 3], [4, 5, 6])
        32
        >>> SUMPRODUCT([2, 3], [4, 5], [6, 7])
        69
    
    Cost: O(n * m) where n is array length and m is number of arrays
    """
    if not arrays:
        raise ValueError("At least one array required")
    
    # Check all arrays have same length
    length = len(arrays[0])
    for arr in arrays[1:]:
        if len(arr) != length:
            raise ValueError("All arrays must have the same length")
    
    # Multiply all arrays element-wise and sum
    result = 0.0
    for i in range(length):
        product = 1.0

        for arr in arrays:
            product *= arr[i]

        result += product

    return result


def SUMSQ(*numbers: Union[float, List[float]]) -> float:
    """Returns the sum of the squares of the arguments.
    
    Description:
        Returns the sum of the squares of the arguments.
        Equivalent to Excel's SUMSQ function.
    
    Args:
        *numbers: One or more numbers or lists of numbers.
    
    Returns:
        float: The sum of squares.
    
    Usage Example:
        >>> SUMSQ(3, 4)
        25
        >>> SUMSQ([1, 2, 3])
        14
        >>> SUMSQ([2, 3], 4)
        29
    
    Cost: O(n) where n is total number of values
    """
    all_numbers = []
    for item in numbers:
        if isinstance(item, (list, tuple)):
            all_numbers.extend(x for x in item if isinstance(x, (int, float)))
        elif isinstance(item, (int, float)):
            all_numbers.append(item)
    
    return sum(x ** 2 for x in all_numbers)


def SUMX2MY2(array_x: List[float], array_y: List[float]) -> float:
    """Returns the sum of the difference of squares.
    
    Description:
        Returns the sum of the difference of squares of corresponding values
        in two arrays. Formula: Σ(x² - y²)
        Equivalent to Excel's SUMX2MY2 function.
    
    Args:
        array_x (List[float]): The first array.
        array_y (List[float]): The second array.
    
    Returns:
        float: The sum of the difference of squares.
    
    Raises:
        ValueError: If arrays have different lengths.
    
    Usage Example:
        >>> SUMX2MY2([2, 3, 9], [6, 5, 11])
        -156
        >>> SUMX2MY2([1, 2], [3, 4])
        -16
    
    Cost: O(n) where n is array length
    """
    if len(array_x) != len(array_y):
        raise ValueError("Arrays must have the same length")

    return _core_sum_x2my2(array_x, array_y)


def SUMX2PY2(array_x: List[float], array_y: List[float]) -> float:
    """Returns the sum of the sum of squares.
    
    Description:
        Returns the sum of the sum of squares of corresponding values
        in two arrays. Formula: Σ(x² + y²)
        Equivalent to Excel's SUMX2PY2 function.
    
    Args:
        array_x (List[float]): The first array.
        array_y (List[float]): The second array.
    
    Returns:
        float: The sum of the sum of squares.
    
    Raises:
        ValueError: If arrays have different lengths.
    
    Usage Example:
        >>> SUMX2PY2([2, 3, 9], [6, 5, 11])
        344
        >>> SUMX2PY2([1, 2], [3, 4])
        30
    
    Cost: O(n) where n is array length
    """
    if len(array_x) != len(array_y):
        raise ValueError("Arrays must have the same length")

    return _core_sum_x2py2(array_x, array_y)


def SUMXMY2(array_x: List[float], array_y: List[float]) -> float:
    """Returns the sum of squares of differences.
    
    Description:
        Returns the sum of squares of differences of corresponding values
        in two arrays. Formula: Σ(x - y)²
        Equivalent to Excel's SUMXMY2 function.
    
    Args:
        array_x (List[float]): The first array.
        array_y (List[float]): The second array.
    
    Returns:
        float: The sum of squares of differences.
    
    Raises:
        ValueError: If arrays have different lengths.
    
    Usage Example:
        >>> SUMXMY2([2, 3, 9], [6, 5, 11])
        24
        >>> SUMXMY2([1, 2], [3, 4])
        8
    
    Cost: O(n) where n is array length
    """
    if len(array_x) != len(array_y):
        raise ValueError("Arrays must have the same length")

    return _core_sum_xmy2(array_x, array_y)


def SUMIFS(sum_range: List[Union[int, float]], *criteria_pairs) -> float:
    """Sums values that meet multiple criteria.

    Description:
        Adds cells in a range that meet multiple criteria specified as
        pairs of (criteria_range, criterion). Equivalent to Excel's
        SUMIFS function.

    Args:
        sum_range (List[Union[int, float]]): Range of values to sum.
        *criteria_pairs: Alternating criteria_range and criterion pairs.
            Each criteria_range is a list and each criterion is a string
            (e.g., ">10", "<=5") or a direct value for equality.

    Returns:
        float: Sum of values meeting all criteria.

    Raises:
        ValueError: If criteria are not provided as pairs or ranges differ
            in length.

    Usage Example:
        >>> SUMIFS([10, 20, 30, 40], [1, 2, 3, 4], ">1", [5, 15, 25, 35], "<30")
        50
        >>> SUMIFS([100, 200, 300], ["A", "B", "A"], "A")
        400

    Cost: O(n * m) where n is range length and m is number of criteria
    """
    if len(criteria_pairs) % 2 != 0:
        raise ValueError("Criteria must be provided as pairs of (range, criterion).")

    if len(criteria_pairs) == 2:
        return _core_sum_if(sum_range, criteria_pairs[0], criteria_pairs[1])

    # Multiple criteria pairs — intersect matches
    criteria_list = []

    for i in range(0, len(criteria_pairs), 2):
        criteria_range = criteria_pairs[i]
        criterion = criteria_pairs[i + 1]

        if len(criteria_range) != len(sum_range):
            raise ValueError("All ranges must have the same length.")

        criteria_list.append((criteria_range, criterion))

    from shortfx.fxNumeric.statistics_functions import _parse_criteria

    preds = [_parse_criteria(crit) for _, crit in criteria_list]
    total = 0.0

    for i in range(len(sum_range)):

        if not isinstance(sum_range[i], (int, float)):
            continue

        if all(pred(criteria_list[j][0][i]) for j, pred in enumerate(preds)):
            total += sum_range[i]

    return total


def TRANSPOSE(array: List[List[float]]) -> List[List[float]]:
    """Transposes a matrix (swaps rows and columns).

    Excel function: TRANSPOSE

    Args:
        array: Input matrix.

    Returns:
        List[List[float]]: The transposed matrix.

    Usage Example:
        >>> TRANSPOSE([[1, 2, 3], [4, 5, 6]])
        [[1, 4], [2, 5], [3, 6]]

    Cost: O(m * n)
    """
    return _core_transpose(array)

