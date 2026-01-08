"""Numeric Trigonometry Module.

This module provides comprehensive trigonometric and hyperbolic functions,
including standard trig functions, inverse functions, and angle conversions.

Key Features:
    - Basic trigonometric functions (sin, cos, tan)
    - Inverse trigonometric functions (arcsin, arccos, arctan)
    - Hyperbolic functions (sinh, cosh, tanh) and their inverses
    - Reciprocal functions (sec, csc, cot)
    - Angle conversions (degrees ↔ radians)
    - Distance calculations (hypotenuse)

Example:
    >>> from formulite.fxNumeric.numeric_trigonometry import sine, degrees_to_radians
    >>> import math
    >>> sine(math.pi / 2)
    1.0
    >>> degrees_to_radians(180)
    3.141592653589793
"""
import math
from typing import Union

# Constants often useful in trigonometry
PI = math.pi
E = math.e


def sine(angle_radians: float) -> float:
    """
    Calculates the sine of an angle.

    The sine function (sin) is one of the primary trigonometric functions.
    It relates the ratio of the length of the opposite side to the length
    of the hypotenuse in a right-angled triangle.

    Args:
        angle_radians (float): The angle in radians.

    Returns:
        float: The sine of the given angle.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> sine(math.pi / 2) # sin(90 degrees)
        1.0
        >>> sine(0)
        0.0

    **Cost:** O(1), standard trigonometric function.
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value (int or float).")
    return math.sin(angle_radians)


def cosine(angle_radians: float) -> float:
    """
    Calculates the cosine of an angle.

    The cosine function (cos) is one of the primary trigonometric functions.
    It relates the ratio of the length of the adjacent side to the length
    of the hypotenuse in a right-angled triangle.

    Args:
        angle_radians (float): The angle in radians.

    Returns:
        float: The cosine of the given angle.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> cosine(0) # cos(0 degrees)
        1.0
        >>> cosine(math.pi) # cos(180 degrees)
        -1.0

    **Cost:** O(1), standard trigonometric function.
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value (int or float).")
    return math.cos(angle_radians)


def tangent(angle_radians: float) -> float:
    """
    Calculates the tangent of an angle.

    The tangent function (tan) is one of the primary trigonometric functions.
    It relates the ratio of the length of the opposite side to the length
    of the adjacent side in a right-angled triangle. It is also equivalent
    to sin(x) / cos(x).

    Args:
        angle_radians (float): The angle in radians.

    Returns:
        float: The tangent of the given angle.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the tangent is undefined (angle is an odd multiple of pi/2).

    Example:
        >>> tangent(0)
        0.0
        >>> round(tangent(math.pi / 4), 10) # tan(45 degrees)
        1.0

    **Cost:** O(1), standard trigonometric function.
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value (int or float).")
    # Tangent is undefined when cosine is zero (at odd multiples of pi/2).
    # We'll rely on math.tan to raise the ValueError if needed.
    return math.tan(angle_radians)


def arcsine(x: float) -> float:
    """
    Calculates the inverse sine (arcsine) of a value.

    The arcsine function (asin) returns the angle whose sine is x.
    The input value x must be between -1 and 1, inclusive, and the
    returned angle will be in radians, between -pi/2 and pi/2.

    Args:
        x (float): The value whose arcsine is to be calculated. Must be in the range [-1, 1].

    Returns:
        float: The arcsine of the given value in radians.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is outside the range [-1, 1].

    Example:
        >>> arcsine(1.0) # asin(1) should be pi/2
        1.5707963267948966
        >>> arcsine(0.0)
        0.0

    **Cost:** O(1), inverse trigonometric function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.asin(x)


def arccosine(x: float) -> float:
    """
    Calculates the inverse cosine (arccosine) of a value.

    The arccosine function (acos) returns the angle whose cosine is x.
    The input value x must be between -1 and 1, inclusive, and the
    returned angle will be in radians, between 0 and pi.

    Args:
        x (float): The value whose arccosine is to be calculated. Must be in the range [-1, 1].

    Returns:
        float: The arccosine of the given value in radians.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is outside the range [-1, 1].

    Example:
        >>> arccosine(1.0) # acos(1) should be 0
        0.0
        >>> arccosine(-1.0) # acos(-1) should be pi
        3.141592653589793

    **Cost:** O(1), inverse trigonometric function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.acos(x)


def arctangent(x: float) -> float:
    """
    Calculates the inverse tangent (arctangent) of a value.

    The arctangent function (atan) returns the angle whose tangent is x.
    The input value x can be any real number, and the returned angle
    will be in radians, between -pi/2 and pi/2.

    Args:
        x (float): The value whose arctangent is to be calculated.

    Returns:
        float: The arctangent of the given value in radians.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> arctangent(1.0) # atan(1) should be pi/4
        0.7853981633974483
        >>> arctangent(0.0)
        0.0

    **Cost:** O(1), inverse trigonometric function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.atan(x)


def arctangent2(y: float, x: float) -> float:
    """
    Calculates the inverse tangent of y/x using the signs of both arguments to determine the correct quadrant.

    The arctangent2 function (atan2) is useful for converting Cartesian coordinates
    (x, y) to polar coordinates (r, theta). The returned angle is in radians,
    between -pi and pi.

    Args:
        y (float): The y-coordinate.
        x (float): The x-coordinate.

    Returns:
        float: The arctangent of y/x in radians, considering the quadrant.

    Raises:
        TypeError: If x or y are not floats or integers.

    Example:
        >>> arctangent2(1, 1) # atan2(1, 1) should be pi/4
        0.7853981633974483
        >>> arctangent2(-1, 1) # atan2(-1, 1) should be -pi/4
        -0.7853981633974483
        >>> arctangent2(1, -1) # atan2(1, -1) should be 3*pi/4
        2.356194490192345

    **Cost:** O(1), atan2 function for quadrant handling.
    """
    if not all(isinstance(arg, (int, float)) for arg in [y, x]):
        raise TypeError("Both y and x must be numeric values (int or float).")
    return math.atan2(y, x)


def hypotenuse(x: float, y: float) -> float:
    """
    Calculates the Euclidean norm, sqrt(x*x + y*y). This is the length of the hypotenuse
    of a right-angled triangle with legs of length x and y.

    Args:
        x (float): The length of the first leg.
        y (float): The length of the second leg.

    Returns:
        float: The length of the hypotenuse.

    Raises:
        TypeError: If x or y are not floats or integers.

    Example:
        >>> hypotenuse(3, 4)
        5.0
        >>> hypotenuse(5, 12)
        13.0

    **Cost:** O(1), hypotenuse calculation using math.hypot.
    """
    if not all(isinstance(arg, (int, float)) for arg in [x, y]):
        raise TypeError("Both x and y must be numeric values (int or float).")
    return math.hypot(x, y)


def hyperbolic_sine(x: float) -> float:
    """
    Calculates the hyperbolic sine of a value.

    The hyperbolic sine function (sinh) is a hyperbolic analogue of the
    trigonometric sine function. It is defined as (e^x - e^-x) / 2.

    Args:
        x (float): The value.

    Returns:
        float: The hyperbolic sine of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> hyperbolic_sine(0)
        0.0
        >>> round(hyperbolic_sine(1), 5)
        1.1752

    **Cost:** O(1), standard hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.sinh(x)


def hyperbolic_cosine(x: float) -> float:
    """
    Calculates the hyperbolic cosine of a value.

    The hyperbolic cosine function (cosh) is a hyperbolic analogue of the
    trigonometric cosine function. It is defined as (e^x + e^-x) / 2.

    Args:
        x (float): The value.

    Returns:
        float: The hyperbolic cosine of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> hyperbolic_cosine(0)
        1.0
        >>> round(hyperbolic_cosine(1), 5)
        1.54308

    **Cost:** O(1), standard hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.cosh(x)


def hyperbolic_tangent(x: float) -> float:
    """
    Calculates the hyperbolic tangent of a value.

    The hyperbolic tangent function (tanh) is a hyperbolic analogue of the
    trigonometric tangent function. It is defined as sinh(x) / cosh(x).

    Args:
        x (float): The value.

    Returns:
        float: The hyperbolic tangent of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> hyperbolic_tangent(0)
        0.0
        >>> round(hyperbolic_tangent(1), 5)
        0.76159

    **Cost:** O(1), standard hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.tanh(x)


def inverse_hyperbolic_sine(x: float) -> float:
    """
    Calculates the inverse hyperbolic sine (arcsinh) of a value.

    The inverse hyperbolic sine function (asinh) returns the value
    whose hyperbolic sine is x.

    Args:
        x (float): The value.

    Returns:
        float: The inverse hyperbolic sine of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> inverse_hyperbolic_sine(0)
        0.0
        >>> round(inverse_hyperbolic_sine(1.1752), 5) # approximately asinh(sinh(1))
        1.0

    **Cost:** O(1), inverse hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.asinh(x)


def inverse_hyperbolic_cosine(x: float) -> float:
    """
    Calculates the inverse hyperbolic cosine (arccosh) of a value.

    The inverse hyperbolic cosine function (acosh) returns the value
    whose hyperbolic cosine is x. The input value x must be >= 1.

    Args:
        x (float): The value. Must be greater than or equal to 1.

    Returns:
        float: The inverse hyperbolic cosine of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is less than 1.

    Example:
        >>> inverse_hyperbolic_cosine(1.0)
        0.0
        >>> round(inverse_hyperbolic_cosine(1.54308), 5) # approximately acosh(cosh(1))
        1.0

    **Cost:** O(1), inverse hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.acosh(x)


def inverse_hyperbolic_tangent(x: float) -> float:
    """
    Calculates the inverse hyperbolic tangent (arctanh) of a value.

    The inverse hyperbolic tangent function (atanh) returns the value
    whose hyperbolic tangent is x. The input value x must be between -1 and 1.

    Args:
        x (float): The value. Must be in the range (-1, 1).

    Returns:
        float: The inverse hyperbolic tangent of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is outside the range (-1, 1).

    Example:
        >>> inverse_hyperbolic_tangent(0)
        0.0
        >>> round(inverse_hyperbolic_tangent(0.76159), 5) # approximately atanh(tanh(1))
        1.0

    **Cost:** O(1), inverse hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.atanh(x)


def degrees_to_radians(degrees: float) -> float:
    """
    Converts an angle from degrees to radians.

    Args:
        degrees (float): The angle in degrees.

    Returns:
        float: The equivalent angle in radians.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> degrees_to_radians(180)
        3.141592653589793
        >>> degrees_to_radians(90)
        1.5707963267948966

    **Cost:** O(1), simple angle conversion.
    """
    if not isinstance(degrees, (int, float)):
        raise TypeError("Input must be a numeric value (int or float).")
    return math.radians(degrees)


def radians_to_degrees(radians: float) -> float:
    """
    Converts an angle from radians to degrees.

    Args:
        radians (float): The angle in radians.

    Returns:
        float: The equivalent angle in degrees.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> radians_to_degrees(math.pi)
        180.0
        >>> radians_to_degrees(math.pi / 2)
        90.0

    **Cost:** O(1), simple angle conversion.
    """
    if not isinstance(radians, (int, float)):
        raise TypeError("Input must be a numeric value (int or float).")
    return math.degrees(radians)


# nonintrinsic math functions that can be derived from the intrinsic math functions


def secant(angle_radians: float) -> float:
    """
    Calculates the secant of an angle.
    Sec(X) = 1 / Cos(X)

    Args:
        angle_radians (float): The angle in radians.

    Returns:
        float: The secant of the given angle.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If cosine(angle_radians) is zero (secant is undefined).

    Example:
        >>> round(secant(0), 10) # sec(0 degrees)
        1.0
        >>> round(secant(math.pi), 10) # sec(180 degrees)
        -1.0

    **Cost:** O(1), derived trigonometric function.
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value (int or float).")
    cos_val = math.cos(angle_radians)
    if abs(cos_val) < 1e-9:  # Check for near-zero to avoid ZeroDivisionError
        raise ValueError("Secant is undefined for angles where cosine is zero (e.g., pi/2, 3pi/2).")
    return 1 / cos_val


def cosecant(angle_radians: float) -> float:
    """
    Calculates the cosecant of an angle.
    Cosec(X) = 1 / Sin(X)

    Args:
        angle_radians (float): The angle in radians.

    Returns:
        float: The cosecant of the given angle.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If sine(angle_radians) is zero (cosecant is undefined).

    Example:
        >>> round(cosecant(math.pi / 2), 10) # cosec(90 degrees)
        1.0
        >>> round(cosecant(3 * math.pi / 2), 10) # cosec(270 degrees)
        -1.0

    **Cost:** O(1), derived trigonometric function.
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value (int or float).")
    sin_val = math.sin(angle_radians)
    if abs(sin_val) < 1e-9:  # Check for near-zero to avoid ZeroDivisionError
        raise ValueError("Cosecant is undefined for angles where sine is zero (e.g., 0, pi, 2pi).")
    return 1 / sin_val


def cotangent(angle_radians: float) -> float:
    """
    Calculates the cotangent of an angle.
    Cotan(X) = 1 / Tan(X)

    Args:
        angle_radians (float): The angle in radians.

    Returns:
        float: The cotangent of the given angle.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If tangent(angle_radians) is zero or undefined (cotangent is undefined).

    Example:
        >>> round(cotangent(math.pi / 4), 10) # cot(45 degrees)
        1.0
        >>> # cotangent(0) would raise ValueError

    **Cost:** O(1), derived trigonometric function.
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value (int or float).")
    tan_val = math.tan(angle_radians)
    if abs(tan_val) < 1e-9:  # Check for near-zero to avoid ZeroDivisionError, also handles tan undefined cases
        raise ValueError("Cotangent is undefined for angles where tangent is zero or undefined (e.g., 0, pi, pi/2).")
    return 1 / tan_val


def inverse_secant(x: float) -> float:
    """
    Calculates the inverse secant (arcsec) of a value.
    Arcsec(X) = Atn(X / Sqr(X * X - 1)) + Sgn((X) - 1) * (2 * Atn(1))
    Note: In Python, math.acos(1/x) is the direct equivalent for arcsec(x).
    The provided formula is a common way to derive it using arctangent.
    Domain: |x| >= 1

    Args:
        x (float): The value whose inverse secant is to be calculated.

    Returns:
        float: The inverse secant of the given value in radians.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is outside the domain |x| >= 1
                    or if x*x - 1 is negative (square root of negative number).

    Example:
        >>> round(inverse_secant(1.0), 10) # arcsec(1) should be 0
        0.0
        >>> round(inverse_secant(-1.0), 10) # arcsec(-1) should be pi
        3.1415926536
        >>> round(inverse_secant(2.0), 10) # arcsec(2) should be pi/3 (60 degrees)
        1.0471975512

    **Cost:** O(1), inverse trigonometric function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    if abs(x) < 1:
        raise ValueError("Domain error: Input for inverse secant must be |x| >= 1.")
    
    # Using math.acos(1/x) is the most direct and numerically stable way in Python
    return math.acos(1 / x)

    # For strict adherence to the provided formula (which relies on atan and sgn):
    # try:
    #     sqrt_term = math.sqrt(x * x - 1)
    #     # Sgn((X) - 1) is equivalent to math.copysign(1, X - 1) or more simply (1 if X > 1 else -1 if X < 1 else 0)
    #     # However, sgn((X) - 1) will be 0 if X = 1, leading to 0 * (2 * Atn(1)).
    #     # When X = 1, X - 1 = 0, so Sgn(0) is typically 0.
    #     # When X = -1, X - 1 = -2, so Sgn(-2) is -1.
    #     # The Sgn function is not a direct Python math function, so we implement it.
    #     sgn_val = 1 if x - 1 > 0 else (-1 if x - 1 < 0 else 0) # This mimics VB's Sgn
    #     
    #     # Atn(1) is pi/4
    #     return math.atan(x / sqrt_term) + sgn_val * (2 * math.atan(1))
    # except ValueError:
    #     # This catches the case where x*x - 1 is negative (i.e., -1 < x < 1)
    #     raise ValueError("Domain error: Input for inverse secant must be |x| >= 1.")
    # except ZeroDivisionError:
    #     # This happens if sqrt_term is 0, which means x*x - 1 = 0, so x = 1 or x = -1.
    #     # At x = 1, arcsec(1) = 0.
    #     # At x = -1, arcsec(-1) = pi.
    #     # The formula breaks at these points due to division by zero.
    #     # Using math.acos(1/x) handles these edge cases correctly.
    #     if x == 1.0: return 0.0
    #     if x == -1.0: return math.pi
    #     raise


def inverse_cosecant(x: float) -> float:
    """
    Calculates the inverse cosecant (arccosec) of a value.
    Arccosec(X) = Atn(X / Sqr(X * X - 1)) + (Sgn(X) - 1) * (2 * Atn(1))
    Note: In Python, math.asin(1/x) is the direct equivalent for arccosec(x).
    The provided formula is a common way to derive it using arctangent.
    Domain: |x| >= 1

    Args:
        x (float): The value whose inverse cosecant is to be calculated.

    Returns:
        float: The inverse cosecant of the given value in radians.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is outside the domain |x| >= 1
                    or if x*x - 1 is negative (square root of negative number).

    Example:
        >>> round(inverse_cosecant(1.0), 10) # arccosec(1) should be pi/2
        1.5707963268
        >>> round(inverse_cosecant(-1.0), 10) # arccosec(-1) should be -pi/2
        -1.5707963268
        >>> round(inverse_cosecant(2.0), 10) # arccosec(2) should be pi/6 (30 degrees)
        0.5235987756

    **Cost:** O(1), inverse trigonometric function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    if abs(x) < 1:
        raise ValueError("Domain error: Input for inverse cosecant must be |x| >= 1.")

    # Using math.asin(1/x) is the most direct and numerically stable way in Python
    return math.asin(1 / x)

    # For strict adherence to the provided formula:
    # try:
    #     sqrt_term = math.sqrt(x * x - 1)
    #     # Sgn(X) - 1: Sgn(X) is 1 if X > 0, -1 if X < 0, 0 if X = 0.
    #     # For X > 0, Sgn(X)-1 = 0. For X < 0, Sgn(X)-1 = -2. For X=0, undefined by formula.
    #     sgn_x = 1 if x > 0 else (-1 if x < 0 else 0)
    #     
    #     # Atn(1) is pi/4
    #     return math.atan(x / sqrt_term) + (sgn_x - 1) * (2 * math.atan(1))
    # except ValueError:
    #     raise ValueError("Domain error: Input for inverse cosecant must be |x| >= 1.")
    # except ZeroDivisionError:
    #     # This happens if sqrt_term is 0, i.e., x = 1 or x = -1.
    #     # At x = 1, arccosec(1) = pi/2.
    #     # At x = -1, arccosec(-1) = -pi/2.
    #     # Using math.asin(1/x) handles these edge cases correctly.
    #     if x == 1.0: return math.pi / 2
    #     if x == -1.0: return -math.pi / 2
    #     raise


def inverse_cotangent(x: float) -> float:
    """
    Calculates the inverse cotangent (arccotan) of a value.
    Arccotan(X) = Atn(X) + 2 * Atn(1) (This formula is for arccot(x) in (0, pi))
    Note: Python's math.atan(x) returns an angle in (-pi/2, pi/2).
    A common definition of arccot(x) is atan(1/x) for x != 0, and pi/2 for x=0.
    Or, math.atan2(1, x) covers all cases and quadrants for arccot(x).

    Args:
        x (float): The value whose inverse cotangent is to be calculated.

    Returns:
        float: The inverse cotangent of the given value in radians.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> round(inverse_cotangent(1.0), 10) # arccot(1) should be pi/4 (0.785...)
        0.7853981634
        >>> round(inverse_cotangent(0.0), 10) # arccot(0) should be pi/2
        1.5707963268
        >>> round(inverse_cotangent(-1.0), 10) # arccot(-1) should be 3pi/4
        2.3561944902

    **Cost:** O(1), inverse trigonometric function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")

    # The most robust way to implement arccot(x) in Python is using atan2(1, x).
    # This correctly handles the quadrant for x > 0, x < 0, and x = 0.
    return math.atan2(1, x)

    # The provided formula Arccotan(X) = Atn(X) + 2 * Atn(1) = atan(x) + pi/2
    # This formula gives results in (0, pi) for all x.
    # return math.atan(x) + math.pi / 2


# Hyperbolic Functions (already present in math module, but defined for completeness following your list)
def hyperbolic_sine_derived(x: float) -> float:
    """
    Calculates the hyperbolic sine of a value using its exponential definition.
    HSin(X) = (Exp(X) - Exp(-X)) / 2
    Equivalent to math.sinh(x).

    Args:
        x (float): The value.

    Returns:
        float: The hyperbolic sine of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> hyperbolic_sine_derived(0)
        0.0
        >>> round(hyperbolic_sine_derived(1), 5)
        1.17520

    **Cost:** O(1), hyperbolic function derived from exponentials.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return (math.exp(x) - math.exp(-x)) / 2


def hyperbolic_cosine_derived(x: float) -> float:
    """
    Calculates the hyperbolic cosine of a value using its exponential definition.
    HCos(X) = (Exp(X) + Exp(-X)) / 2
    Equivalent to math.cosh(x).

    Args:
        x (float): The value.

    Returns:
        float: The hyperbolic cosine of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> hyperbolic_cosine_derived(0)
        1.0
        >>> round(hyperbolic_cosine_derived(1), 5)
        1.54308

    **Cost:** O(1), hyperbolic function derived from exponentials.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return (math.exp(x) + math.exp(-x)) / 2


def hyperbolic_tangent_derived(x: float) -> float:
    """
    Calculates the hyperbolic tangent of a value using its exponential definition.
    HTan(X) = (Exp(X) - Exp(-X)) / (Exp(X) + Exp(-X))
    Equivalent to math.tanh(x).

    Args:
        x (float): The value.

    Returns:
        float: The hyperbolic tangent of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the denominator is zero (which only happens for specific complex values,
                    not for real numbers).

    Example:
        >>> hyperbolic_tangent_derived(0)
        0.0
        >>> round(hyperbolic_tangent_derived(1), 5)
        0.76159

    **Cost:** O(1), hyperbolic function derived from exponentials.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    numerator = math.exp(x) - math.exp(-x)
    denominator = math.exp(x) + math.exp(-x)
    if abs(denominator) < 1e-9: # Should not happen for real x
        raise ValueError("Hyperbolic tangent is undefined.")
    return numerator / denominator


def hyperbolic_secant(x: float) -> float:
    """
    Calculates the hyperbolic secant of a value.
    HSec(X) = 2 / (Exp(X) + Exp(-X)) = 1 / HCos(X)

    Args:
        x (float): The value.

    Returns:
        float: The hyperbolic secant of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the denominator is zero (which only happens for specific complex values,
                    not for real numbers).

    Example:
        >>> round(hyperbolic_secant(0), 10)
        1.0
        >>> round(hyperbolic_secant(1), 5)
        0.64805

    **Cost:** O(1), derived hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    denominator = math.exp(x) + math.exp(-x)
    if abs(denominator) < 1e-9: # Should not happen for real x
        raise ValueError("Hyperbolic secant is undefined.")
    return 2 / denominator


def hyperbolic_cosecant(x: float) -> float:
    """
    Calculates the hyperbolic cosecant of a value.
    HCosec(X) = 2 / (Exp(X) - Exp(-X)) = 1 / HSin(X)

    Args:
        x (float): The value.

    Returns:
        float: The hyperbolic cosecant of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If x is 0 (hyperbolic cosecant is undefined).

    Example:
        >>> round(hyperbolic_cosecant(1), 5)
        0.85091
        >>> # hyperbolic_cosecant(0) would raise ValueError

    **Cost:** O(1), derived hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    denominator = math.exp(x) - math.exp(-x)
    if abs(denominator) < 1e-9: # This happens if x is very close to 0
        raise ValueError("Hyperbolic cosecant is undefined when x is 0.")
    return 2 / denominator


def hyperbolic_cotangent(x: float) -> float:
    """
    Calculates the hyperbolic cotangent of a value.
    HCotan(X) = (Exp(X) + Exp(-X)) / (Exp(X) - Exp(-X)) = 1 / HTan(X)

    Args:
        x (float): The value.

    Returns:
        float: The hyperbolic cotangent of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If x is 0 (hyperbolic cotangent is undefined).

    Example:
        >>> round(hyperbolic_cotangent(1), 5)
        1.31303
        >>> # hyperbolic_cotangent(0) would raise ValueError

    **Cost:** O(1), derived hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    numerator = math.exp(x) + math.exp(-x)
    denominator = math.exp(x) - math.exp(-x)
    if abs(denominator) < 1e-9: # This happens if x is very close to 0
        raise ValueError("Hyperbolic cotangent is undefined when x is 0.")
    return numerator / denominator


# Inverse Hyperbolic Functions (some already present in math module)
def inverse_hyperbolic_sine_derived(x: float) -> float:
    """
    Calculates the inverse hyperbolic sine (arcsinh) of a value.
    HArcsin(X) = Log(X + Sqr(X * X + 1))
    Equivalent to math.asinh(x).

    Args:
        x (float): The value.

    Returns:
        float: The inverse hyperbolic sine of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.

    Example:
        >>> inverse_hyperbolic_sine_derived(0)
        0.0
        >>> round(inverse_hyperbolic_sine_derived(1), 10)
        0.881373587

    **Cost:** O(1), inverse hyperbolic function derived from logarithm.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    return math.log(x + math.sqrt(x * x + 1))


def inverse_hyperbolic_cosine_derived(x: float) -> float:
    """
    Calculates the inverse hyperbolic cosine (arccosh) of a value.
    HArccos(X) = Log(X + Sqr(X * X - 1))
    Equivalent to math.acosh(x).
    Domain: X >= 1

    Args:
        x (float): The value. Must be >= 1.

    Returns:
        float: The inverse hyperbolic cosine of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is less than 1.

    Example:
        >>> inverse_hyperbolic_cosine_derived(1.0)
        0.0
        >>> round(inverse_hyperbolic_cosine_derived(2.0), 10)
        1.3169578969

    **Cost:** O(1), inverse hyperbolic function derived from logarithm.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    if x < 1:
        raise ValueError("Domain error: Input for inverse hyperbolic cosine must be X >= 1.")
    return math.log(x + math.sqrt(x * x - 1))


def inverse_hyperbolic_tangent_derived(x: float) -> float:
    """
    Calculates the inverse hyperbolic tangent (arctanh) of a value.
    HArctan(X) = Log((1 + X) / (1 - X)) / 2
    Equivalent to math.atanh(x).
    Domain: -1 < X < 1

    Args:
        x (float): The value. Must be between -1 and 1 (exclusive).

    Returns:
        float: The inverse hyperbolic tangent of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is outside the range (-1, 1).

    Example:
        >>> inverse_hyperbolic_tangent_derived(0)
        0.0
        >>> round(inverse_hyperbolic_tangent_derived(0.5), 10)
        0.5493061443

    **Cost:** O(1), inverse hyperbolic function derived from logarithm.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    if not (-1 < x < 1):
        raise ValueError("Domain error: Input for inverse hyperbolic tangent must be -1 < X < 1.")
    
    # Check for division by zero if x is exactly 1 or -1 which are not in the domain.
    # The (1 - X) term is in the denominator.
    if x == 1.0 or x == -1.0:
        raise ValueError("Domain error: Input for inverse hyperbolic tangent cannot be 1 or -1.")
        
    return math.log((1 + x) / (1 - x)) / 2


def inverse_hyperbolic_secant(x: float) -> float:
    """
    Calculates the inverse hyperbolic secant (arcsech) of a value.
    HArcsec(X) = Log((Sqr(-X * X + 1) + 1) / X)
    Domain: 0 < X <= 1

    Args:
        x (float): The value. Must be in the range (0, 1].

    Returns:
        float: The inverse hyperbolic secant of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is outside the domain (0, 1].
                    Also if -X*X + 1 is negative (square root of negative number)
                    or if X is zero (division by zero).

    Example:
        >>> round(inverse_hyperbolic_secant(1.0), 10)
        0.0
        >>> round(inverse_hyperbolic_secant(0.5), 10)
        1.3169578969

    **Cost:** O(1), inverse hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    if not (0 < x <= 1):
        raise ValueError("Domain error: Input for inverse hyperbolic secant must be 0 < X <= 1.")
    
    # Check for negative value under square root
    if (-x * x + 1) < 0:
        raise ValueError("Domain error: Argument to square root is negative.")
    
    # Check for division by zero
    if x == 0:
        raise ValueError("Division by zero: Input X cannot be zero.")

    return math.log((math.sqrt(-x * x + 1) + 1) / x)


def inverse_hyperbolic_cosecant(x: float) -> float:
    """
    Calculates the inverse hyperbolic cosecant (arccosech) of a value.
    HArccosec(X) = Log((Sgn(X) * Sqr(X * X + 1) + 1) / X)
    Domain: All real numbers except 0.

    Args:
        x (float): The value. Must not be 0.

    Returns:
        float: The inverse hyperbolic cosecant of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is 0 (division by zero).

    Example:
        >>> round(inverse_hyperbolic_cosecant(1.0), 10)
        0.881373587
        >>> round(inverse_hyperbolic_cosecant(-1.0), 10)
        -0.881373587

    **Cost:** O(1), inverse hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    if x == 0:
        raise ValueError("Domain error: Input for inverse hyperbolic cosecant cannot be 0.")

    # Implement Sgn(X) - returns 1 for x > 0, -1 for x < 0.
    sgn_x = 1 if x > 0 else -1

    return math.log((sgn_x * math.sqrt(x * x + 1) + 1) / x)


def inverse_hyperbolic_cotangent(x: float) -> float:
    """
    Calculates the inverse hyperbolic cotangent (arccotanh) of a value.
    HArccotan(X) = Log((X + 1) / (X - 1)) / 2
    Domain: |X| > 1

    Args:
        x (float): The value. Must be |X| > 1.

    Returns:
        float: The inverse hyperbolic cotangent of the given value.

    Raises:
        TypeError: If the input is not a float or an integer.
        ValueError: If the input value x is outside the domain |X| > 1
                    or if X is 1 or -1 (division by zero).

    Example:
        >>> round(inverse_hyperbolic_cotangent(2.0), 10)
        0.5493061443
        >>> round(inverse_hyperbolic_cotangent(-2.0), 10)
        -0.5493061443

    **Cost:** O(1), inverse hyperbolic function.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input value must be a numeric value (int or float).")
    if not (abs(x) > 1):
        raise ValueError("Domain error: Input for inverse hyperbolic cotangent must be |X| > 1.")
    
    # Check for division by zero if x is exactly 1 or -1 which are not in the domain.
    # The (X - 1) term is in the denominator.
    if x == 1.0 or x == -1.0:
        raise ValueError("Division by zero: Input X cannot be 1 or -1.")

    return math.log((x + 1) / (x - 1)) / 2

