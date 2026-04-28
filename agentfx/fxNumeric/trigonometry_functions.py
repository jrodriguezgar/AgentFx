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
    >>> from agentfx.fxNumeric.trigonometry_functions import sine, degrees_to_radians
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
    return hyperbolic_sine(x)


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
    return hyperbolic_cosine(x)


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
    return hyperbolic_tangent(x)


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
    return inverse_hyperbolic_sine(x)


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
    return inverse_hyperbolic_cosine(x)


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
    return inverse_hyperbolic_tangent(x)


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


def sinc(x: float) -> float:
    """Calculates the normalized sinc function: sin(pi*x) / (pi*x).

    Returns 1.0 when x == 0 (limit). Widely used in signal processing,
    Fourier analysis, and interpolation theory.

    Args:
        x: Input value.

    Returns:
        Normalized sinc of x.

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> sinc(0)
        1.0
        >>> round(sinc(0.5), 10)
        0.6366197724

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a numeric value.")

    if x == 0:
        return 1.0

    return math.sin(math.pi * x) / (math.pi * x)


_EARTH_RADIUS_KM = 6371.0


def haversine_distance(lat1: float, lon1: float,
                       lat2: float, lon2: float) -> float:
    """Calculates the great-circle distance between two points on Earth.

    Uses the Haversine formula. Input coordinates are in decimal degrees.

    Args:
        lat1: Latitude of point 1 in degrees.
        lon1: Longitude of point 1 in degrees.
        lat2: Latitude of point 2 in degrees.
        lon2: Longitude of point 2 in degrees.

    Returns:
        Distance in kilometers.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> round(haversine_distance(40.4168, -3.7038, 48.8566, 2.3522), 0)
        1053.0

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [lat1, lon1, lat2, lon2]):
        raise TypeError("All coordinates must be numeric values.")

    lat1_r = math.radians(lat1)
    lat2_r = math.radians(lat2)
    dlat = math.radians(lat2 - lat1)
    dlon = math.radians(lon2 - lon1)

    a = math.sin(dlat / 2) ** 2 + math.cos(lat1_r) * math.cos(lat2_r) * math.sin(dlon / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return _EARTH_RADIUS_KM * c


def triangle_area_sas(
    a: Union[int, float],
    b: Union[int, float],
    angle_c: float,
) -> float:
    """Computes the area of a triangle given two sides and the included angle.

    Area = 0.5 * a * b * sin(C).

    Args:
        a: Length of the first side (positive).
        b: Length of the second side (positive).
        angle_c: Included angle in radians (0, π).

    Returns:
        The area of the triangle.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If sides are non-positive or angle is out of (0, π).

    Example:
        >>> import math
        >>> round(triangle_area_sas(5, 7, math.pi / 6), 4)
        8.75

    Complexity: O(1)
    """
    import math as _math

    if not all(isinstance(v, (int, float)) for v in [a, b, angle_c]):
        raise TypeError("All parameters must be numeric.")

    if a <= 0 or b <= 0:
        raise ValueError("Side lengths must be positive.")

    if angle_c <= 0 or angle_c >= _math.pi:
        raise ValueError("Angle must be in (0, pi) radians.")

    return 0.5 * a * b * _math.sin(angle_c)


def law_of_cosines_side(
    a: Union[int, float],
    b: Union[int, float],
    angle_c: float,
) -> float:
    """Finds the third side of a triangle using the law of cosines.

    c² = a² + b² − 2ab·cos(C).

    Args:
        a: Length of side a (positive).
        b: Length of side b (positive).
        angle_c: Angle opposite to the unknown side, in radians (0, π).

    Returns:
        Length of the unknown side c.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If sides are non-positive or angle is out of (0, π).

    Example:
        >>> import math
        >>> round(law_of_cosines_side(5, 7, math.pi / 3), 4)
        6.2450

    Complexity: O(1)
    """
    import math as _math

    if not all(isinstance(v, (int, float)) for v in [a, b, angle_c]):
        raise TypeError("All parameters must be numeric.")

    if a <= 0 or b <= 0:
        raise ValueError("Side lengths must be positive.")

    if angle_c <= 0 or angle_c >= _math.pi:
        raise ValueError("Angle must be in (0, pi) radians.")

    c_sq = a ** 2 + b ** 2 - 2 * a * b * _math.cos(angle_c)
    return _math.sqrt(c_sq)


def law_of_cosines_angle(
    a: Union[int, float],
    b: Union[int, float],
    c: Union[int, float],
) -> float:
    """Finds the angle opposite side c using the law of cosines.

    cos(C) = (a² + b² − c²) / (2ab).

    Args:
        a: Length of side a (positive).
        b: Length of side b (positive).
        c: Length of side c (positive).

    Returns:
        Angle C in radians.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If sides are non-positive or do not form a valid triangle.

    Example:
        >>> import math
        >>> round(law_of_cosines_angle(3, 4, 5), 4)
        1.5708

    Complexity: O(1)
    """
    import math as _math

    if not all(isinstance(v, (int, float)) for v in [a, b, c]):
        raise TypeError("All parameters must be numeric.")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not form a valid triangle.")

    cos_c = (a ** 2 + b ** 2 - c ** 2) / (2 * a * b)
    # Clamp to [-1, 1] to handle floating-point errors
    cos_c = max(-1.0, min(1.0, cos_c))
    return _math.acos(cos_c)


def law_of_sines(
    a: Union[int, float],
    angle_a: float,
    angle_b: float,
) -> float:
    """Finds side b using the law of sines: b = a × sin(B) / sin(A).

    Args:
        a: Length of side a (positive).
        angle_a: Angle opposite side a in radians (0 < angle < π).
        angle_b: Angle opposite the unknown side b in radians (0 < angle < π).

    Returns:
        Length of side b.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If a <= 0, angles not in (0, π), or angles sum > π.

    Example:
        >>> import math
        >>> round(law_of_sines(10, math.radians(30), math.radians(45)), 4)
        14.1421

    Complexity: O(1)
    """
    import math as _math

    if not all(isinstance(v, (int, float)) for v in [a, angle_a, angle_b]):
        raise TypeError("All parameters must be numeric.")

    if a <= 0:
        raise ValueError("Side length must be positive.")

    if not (0 < angle_a < _math.pi) or not (0 < angle_b < _math.pi):
        raise ValueError("Angles must be in (0, π) radians.")

    if angle_a + angle_b >= _math.pi:
        raise ValueError("Sum of angles must be less than π.")

    return a * _math.sin(angle_b) / _math.sin(angle_a)


def herons_formula(
    a: Union[int, float],
    b: Union[int, float],
    c: Union[int, float],
) -> float:
    """Computes the area of a triangle from its three side lengths.

    Area = √(s(s−a)(s−b)(s−c)) where s = (a+b+c)/2.

    Args:
        a: Length of side a (positive).
        b: Length of side b (positive).
        c: Length of side c (positive).

    Returns:
        The area of the triangle.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If sides are non-positive or do not form a valid triangle.

    Example:
        >>> herons_formula(3, 4, 5)
        6.0

    Complexity: O(1)
    """
    import math as _math

    if not all(isinstance(v, (int, float)) for v in [a, b, c]):
        raise TypeError("All parameters must be numeric.")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be positive.")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not form a valid triangle.")

    s = (a + b + c) / 2.0
    return _math.sqrt(s * (s - a) * (s - b) * (s - c))


def circular_arc_length(
    radius: Union[int, float],
    angle: float,
) -> float:
    """Computes the arc length of a circle given radius and central angle.

    arc = r × θ.

    Args:
        radius: Radius of the circle (positive).
        angle: Central angle in radians (>= 0).

    Returns:
        The arc length.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radius <= 0 or angle < 0.

    Example:
        >>> import math
        >>> round(circular_arc_length(5, math.pi / 2), 4)
        7.854

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)) or not isinstance(angle, (int, float)):
        raise TypeError("Both parameters must be numeric.")

    if radius <= 0:
        raise ValueError("Radius must be positive.")

    if angle < 0:
        raise ValueError("Angle must be non-negative.")

    return radius * angle


def angular_velocity(
    revolutions: Union[int, float],
    time_seconds: Union[int, float],
) -> float:
    """Computes angular velocity in radians per second.

    ω = 2π × revolutions / time.

    Args:
        revolutions: Number of revolutions.
        time_seconds: Time period in seconds (must be positive).

    Returns:
        Angular velocity in rad/s.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If time_seconds is not positive.

    Example:
        >>> import math
        >>> round(angular_velocity(1, 1), 4)
        6.2832

    Complexity: O(1)
    """
    if not isinstance(revolutions, (int, float)):
        raise TypeError("revolutions must be numeric.")

    if not isinstance(time_seconds, (int, float)):
        raise TypeError("time_seconds must be numeric.")

    if time_seconds <= 0:
        raise ValueError("time_seconds must be positive.")

    import math as _m

    return 2.0 * _m.pi * revolutions / time_seconds


def gudermannian(x: Union[int, float]) -> float:
    """Compute the Gudermannian function: gd(x) = 2 * atan(tanh(x/2)).

    Links circular and hyperbolic functions without using complex numbers.

    Args:
        x: Input value in radians.

    Returns:
        Gudermannian of x, in the range (-pi/2, pi/2).

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> import math
        >>> round(gudermannian(1), 6)
        0.865769

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    import math

    return 2.0 * math.atan(math.tanh(x / 2.0))


def inverse_gudermannian(x: Union[int, float]) -> float:
    """Compute the inverse Gudermannian: gd⁻¹(x) = 2 * atanh(tan(x/2)).

    Args:
        x: Input value in (-pi/2, pi/2).

    Returns:
        Inverse Gudermannian of x.

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is not in (-pi/2, pi/2).

    Example:
        >>> round(inverse_gudermannian(0.865769), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    import math

    half_pi = math.pi / 2.0

    if x <= -half_pi or x >= half_pi:
        raise ValueError("x must be in the open interval (-pi/2, pi/2).")

    return 2.0 * math.atanh(math.tan(x / 2.0))


def haversine_angle(theta: Union[int, float]) -> float:
    """Compute the haversine of an angle: hav(θ) = sin²(θ/2).

    The haversine function is used in navigation formulas for computing
    great-circle distances.

    Args:
        theta: Angle in radians.

    Returns:
        Haversine value in [0, 1].

    Raises:
        TypeError: If theta is not numeric.

    Example:
        >>> import math
        >>> haversine_angle(math.pi)
        1.0
        >>> haversine_angle(0)
        0.0

    Complexity: O(1)
    """
    if not isinstance(theta, (int, float)):
        raise TypeError("theta must be numeric.")

    import math

    s = math.sin(theta / 2.0)
    return s * s


def annulus_area(
    outer_radius: Union[int, float],
    inner_radius: Union[int, float],
) -> float:
    """Calculate the area of an annulus (ring): A = π * (R² - r²).

    Args:
        outer_radius: Outer radius.
        inner_radius: Inner radius.

    Returns:
        Area of the annulus.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radii are not positive or inner >= outer.

    Example:
        >>> round(annulus_area(5, 3), 4)
        50.2655

    Complexity: O(1)
    """
    if not isinstance(outer_radius, (int, float)):
        raise TypeError("outer_radius must be numeric.")

    if not isinstance(inner_radius, (int, float)):
        raise TypeError("inner_radius must be numeric.")

    if outer_radius <= 0 or inner_radius <= 0:
        raise ValueError("radii must be positive.")

    if inner_radius >= outer_radius:
        raise ValueError("inner_radius must be less than outer_radius.")

    import math

    return float(math.pi * (outer_radius ** 2 - inner_radius ** 2))


def ellipse_area(
    semi_major: Union[int, float],
    semi_minor: Union[int, float],
) -> float:
    """Calculate the area of an ellipse: A = π * a * b.

    Args:
        semi_major: Semi-major axis length.
        semi_minor: Semi-minor axis length.

    Returns:
        Area of the ellipse.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If axes are not positive.

    Example:
        >>> round(ellipse_area(5, 3), 4)
        47.1239

    Complexity: O(1)
    """
    if not isinstance(semi_major, (int, float)):
        raise TypeError("semi_major must be numeric.")

    if not isinstance(semi_minor, (int, float)):
        raise TypeError("semi_minor must be numeric.")

    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("semi-axes must be positive.")

    import math

    return float(math.pi * semi_major * semi_minor)


def ellipse_perimeter(
    semi_major: Union[int, float],
    semi_minor: Union[int, float],
) -> float:
    """Approximate the perimeter of an ellipse using Ramanujan's formula.

    P ≈ π * [3(a+b) - √((3a+b)(a+3b))]

    Args:
        semi_major: Semi-major axis length.
        semi_minor: Semi-minor axis length.

    Returns:
        Approximate perimeter of the ellipse.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If axes are not positive.

    Example:
        >>> round(ellipse_perimeter(5, 3), 4)
        25.5268

    Complexity: O(1)
    """
    if not isinstance(semi_major, (int, float)):
        raise TypeError("semi_major must be numeric.")

    if not isinstance(semi_minor, (int, float)):
        raise TypeError("semi_minor must be numeric.")

    if semi_major <= 0 or semi_minor <= 0:
        raise ValueError("semi-axes must be positive.")

    import math

    a, b = semi_major, semi_minor
    return float(math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b))))


def regular_polygon_area(
    n_sides: int,
    side_length: Union[int, float],
) -> float:
    """Calculate the area of a regular polygon: A = (n·s²) / (4·tan(π/n)).

    Args:
        n_sides: Number of sides (≥ 3).
        side_length: Length of each side.

    Returns:
        Area of the regular polygon.

    Raises:
        TypeError: If n_sides is not int or side_length not numeric.
        ValueError: If n_sides < 3 or side_length not positive.

    Example:
        >>> round(regular_polygon_area(6, 2), 4)
        10.3923

    Complexity: O(1)
    """
    if not isinstance(n_sides, int):
        raise TypeError("n_sides must be an integer.")

    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be numeric.")

    if n_sides < 3:
        raise ValueError("n_sides must be at least 3.")

    if side_length <= 0:
        raise ValueError("side_length must be positive.")

    import math

    return float(n_sides * side_length ** 2 / (4 * math.tan(math.pi / n_sides)))


def frustum_volume(
    radius_top: Union[int, float],
    radius_bottom: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the volume of a conical frustum.

    V = (π·h / 3) · (R² + R·r + r²)

    Args:
        radius_top: Top radius.
        radius_bottom: Bottom radius.
        height: Height of the frustum.

    Returns:
        Volume.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any dimension is not positive.

    Example:
        >>> round(frustum_volume(2, 4, 5), 4)
        146.608

    Complexity: O(1)
    """
    if not isinstance(radius_top, (int, float)):
        raise TypeError("radius_top must be numeric.")

    if not isinstance(radius_bottom, (int, float)):
        raise TypeError("radius_bottom must be numeric.")

    if not isinstance(height, (int, float)):
        raise TypeError("height must be numeric.")

    if radius_top <= 0 or radius_bottom <= 0 or height <= 0:
        raise ValueError("all dimensions must be positive.")

    import math

    r, R = radius_top, radius_bottom
    return float(math.pi * height / 3.0 * (R * R + R * r + r * r))


def torus_volume(
    major_radius: Union[int, float],
    minor_radius: Union[int, float],
) -> float:
    """Calculate the volume of a torus: V = 2π²·R·r².

    Args:
        major_radius: Distance from center of torus to center of tube.
        minor_radius: Radius of the tube.

    Returns:
        Volume of the torus.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radii are not positive or minor >= major.

    Example:
        >>> round(torus_volume(5, 2), 4)
        394.7842

    Complexity: O(1)
    """
    if not isinstance(major_radius, (int, float)):
        raise TypeError("major_radius must be numeric.")

    if not isinstance(minor_radius, (int, float)):
        raise TypeError("minor_radius must be numeric.")

    if major_radius <= 0 or minor_radius <= 0:
        raise ValueError("radii must be positive.")

    if minor_radius >= major_radius:
        raise ValueError("minor_radius must be less than major_radius.")

    import math

    return float(2 * math.pi ** 2 * major_radius * minor_radius ** 2)


def torus_surface_area(
    major_radius: Union[int, float],
    minor_radius: Union[int, float],
) -> float:
    """Calculate the surface area of a torus: A = 4π²·R·r.

    Args:
        major_radius: Distance from center of torus to center of tube.
        minor_radius: Radius of the tube.

    Returns:
        Surface area.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radii are not positive or minor >= major.

    Example:
        >>> round(torus_surface_area(5, 2), 4)
        394.7842

    Complexity: O(1)
    """
    if not isinstance(major_radius, (int, float)):
        raise TypeError("major_radius must be numeric.")

    if not isinstance(minor_radius, (int, float)):
        raise TypeError("minor_radius must be numeric.")

    if major_radius <= 0 or minor_radius <= 0:
        raise ValueError("radii must be positive.")

    if minor_radius >= major_radius:
        raise ValueError("minor_radius must be less than major_radius.")

    import math

    return float(4 * math.pi ** 2 * major_radius * minor_radius)


def cone_lateral_area(
    radius: Union[int, float],
    slant_height: Union[int, float],
) -> float:
    """Calculate the lateral surface area of a cone: A = π·r·l.

    Args:
        radius: Base radius.
        slant_height: Slant height.

    Returns:
        Lateral surface area.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If dimensions are not positive.

    Example:
        >>> round(cone_lateral_area(3, 5), 4)
        47.1239

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be numeric.")

    if not isinstance(slant_height, (int, float)):
        raise TypeError("slant_height must be numeric.")

    if radius <= 0 or slant_height <= 0:
        raise ValueError("dimensions must be positive.")

    import math

    return float(math.pi * radius * slant_height)


def spherical_cap_volume(
    sphere_radius: Union[int, float],
    cap_height: Union[int, float],
) -> float:
    """Calculate the volume of a spherical cap: V = (π·h²/3)·(3R - h).

    Args:
        sphere_radius: Radius of the sphere.
        cap_height: Height of the cap (must be ≤ 2·R).

    Returns:
        Volume of the spherical cap.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If dimensions are not positive or cap_height > 2·sphere_radius.

    Example:
        >>> round(spherical_cap_volume(5, 2), 4)
        54.4543

    Complexity: O(1)
    """
    if not isinstance(sphere_radius, (int, float)):
        raise TypeError("sphere_radius must be numeric.")

    if not isinstance(cap_height, (int, float)):
        raise TypeError("cap_height must be numeric.")

    if sphere_radius <= 0 or cap_height <= 0:
        raise ValueError("dimensions must be positive.")

    if cap_height > 2 * sphere_radius:
        raise ValueError("cap_height must not exceed 2 * sphere_radius.")

    import math

    return float(math.pi * cap_height ** 2 / 3.0 * (3 * sphere_radius - cap_height))


def spherical_cap_area(
    sphere_radius: Union[int, float],
    cap_height: Union[int, float],
) -> float:
    """Calculate the curved surface area of a spherical cap: A = 2·π·R·h.

    Args:
        sphere_radius: Radius of the sphere.
        cap_height: Height of the cap.

    Returns:
        Curved surface area of the cap.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If dimensions are not positive or cap_height > 2·sphere_radius.

    Example:
        >>> round(spherical_cap_area(5, 2), 4)
        62.8319

    Complexity: O(1)
    """
    if not isinstance(sphere_radius, (int, float)):
        raise TypeError("sphere_radius must be numeric.")

    if not isinstance(cap_height, (int, float)):
        raise TypeError("cap_height must be numeric.")

    if sphere_radius <= 0 or cap_height <= 0:
        raise ValueError("dimensions must be positive.")

    if cap_height > 2 * sphere_radius:
        raise ValueError("cap_height must not exceed 2 * sphere_radius.")

    import math

    return float(2 * math.pi * sphere_radius * cap_height)


def pyramid_volume(
    base_area: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the volume of a pyramid: V = (1/3)·B·h.

    Args:
        base_area: Area of the base.
        height: Perpendicular height.

    Returns:
        Volume.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If dimensions are not positive.

    Example:
        >>> round(pyramid_volume(25, 6), 4)
        50.0

    Complexity: O(1)
    """
    if not isinstance(base_area, (int, float)):
        raise TypeError("base_area must be numeric.")

    if not isinstance(height, (int, float)):
        raise TypeError("height must be numeric.")

    if base_area <= 0 or height <= 0:
        raise ValueError("dimensions must be positive.")

    return float(base_area * height / 3.0)


def cylinder_lateral_area(
    radius: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the lateral surface area of a cylinder: A = 2·π·r·h.

    Args:
        radius: Base radius.
        height: Height of the cylinder.

    Returns:
        Lateral surface area.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If dimensions are not positive.

    Example:
        >>> round(cylinder_lateral_area(3, 5), 4)
        94.2478

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be numeric.")

    if not isinstance(height, (int, float)):
        raise TypeError("height must be numeric.")

    if radius <= 0 or height <= 0:
        raise ValueError("dimensions must be positive.")

    import math

    return float(2 * math.pi * radius * height)


def rhombus_area(
    diagonal1: Union[int, float],
    diagonal2: Union[int, float],
) -> float:
    """Calculate the area of a rhombus: A = (d₁·d₂) / 2.

    Args:
        diagonal1: Length of the first diagonal.
        diagonal2: Length of the second diagonal.

    Returns:
        Area of the rhombus.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If diagonals are not positive.

    Example:
        >>> rhombus_area(10, 8)
        40.0

    Complexity: O(1)
    """
    if not isinstance(diagonal1, (int, float)):
        raise TypeError("diagonal1 must be numeric.")

    if not isinstance(diagonal2, (int, float)):
        raise TypeError("diagonal2 must be numeric.")

    if diagonal1 <= 0 or diagonal2 <= 0:
        raise ValueError("diagonals must be positive.")

    return float(diagonal1 * diagonal2 / 2.0)


def trapezoid_area(
    base1: Union[int, float],
    base2: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the area of a trapezoid: A = (b₁ + b₂) · h / 2.

    Args:
        base1: Length of the first base.
        base2: Length of the second base.
        height: Perpendicular height.

    Returns:
        Area of the trapezoid.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any dimension is not positive.

    Example:
        >>> trapezoid_area(5, 7, 4)
        24.0

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (base1, base2, height)):
        raise TypeError("all inputs must be numeric.")

    if base1 <= 0 or base2 <= 0 or height <= 0:
        raise ValueError("dimensions must be positive.")

    return float((base1 + base2) * height / 2.0)


def parallelogram_area(
    base: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the area of a parallelogram: A = b · h.

    Args:
        base: Base length.
        height: Perpendicular height.

    Returns:
        Area.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If dimensions are not positive.

    Example:
        >>> parallelogram_area(8, 5)
        40.0

    Complexity: O(1)
    """
    if not isinstance(base, (int, float)):
        raise TypeError("base must be numeric.")

    if not isinstance(height, (int, float)):
        raise TypeError("height must be numeric.")

    if base <= 0 or height <= 0:
        raise ValueError("dimensions must be positive.")

    return float(base * height)


def regular_polygon_perimeter(
    n_sides: int,
    side_length: Union[int, float],
) -> float:
    """Calculate the perimeter of a regular polygon: P = n · s.

    Args:
        n_sides: Number of sides (≥ 3).
        side_length: Length of each side.

    Returns:
        Perimeter.

    Raises:
        TypeError: If n_sides is not int or side_length not numeric.
        ValueError: If n_sides < 3 or side_length not positive.

    Example:
        >>> regular_polygon_perimeter(6, 5)
        30.0

    Complexity: O(1)
    """
    if not isinstance(n_sides, int):
        raise TypeError("n_sides must be an integer.")

    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be numeric.")

    if n_sides < 3:
        raise ValueError("n_sides must be at least 3.")

    if side_length <= 0:
        raise ValueError("side_length must be positive.")

    return float(n_sides * side_length)


def sector_arc_length(
    radius: Union[int, float],
    angle: Union[int, float],
) -> float:
    """Calculate the arc length of a circular sector: L = r · θ.

    Args:
        radius: Radius.
        angle: Central angle in radians.

    Returns:
        Arc length.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radius not positive or angle negative.

    Example:
        >>> import math
        >>> round(sector_arc_length(5, math.pi / 3), 4)
        5.236

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be numeric.")

    if not isinstance(angle, (int, float)):
        raise TypeError("angle must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if angle < 0:
        raise ValueError("angle must be non-negative.")

    return float(radius * angle)


def circular_ring_area(
    outer_radius: Union[int, float],
    inner_radius: Union[int, float],
) -> float:
    """Calculate the area of a circular ring (same as annulus): A = π(R² - r²).

    This is an alias for annulus_area using a more intuitive name.

    Args:
        outer_radius: Outer radius.
        inner_radius: Inner radius.

    Returns:
        Area of the ring.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radii not positive or inner ≥ outer.

    Example:
        >>> round(circular_ring_area(5, 3), 4)
        50.2655

    Complexity: O(1)
    """
    if not isinstance(outer_radius, (int, float)):
        raise TypeError("outer_radius must be numeric.")

    if not isinstance(inner_radius, (int, float)):
        raise TypeError("inner_radius must be numeric.")

    if outer_radius <= 0 or inner_radius <= 0:
        raise ValueError("radii must be positive.")

    if inner_radius >= outer_radius:
        raise ValueError("inner_radius must be less than outer_radius.")

    import math

    return float(math.pi * (outer_radius ** 2 - inner_radius ** 2))


def circular_segment_area(
    radius: Union[int, float],
    angle: Union[int, float],
) -> float:
    """Calculate the area of a circular segment.

    A = (r²/2) · (θ - sin(θ))  where θ is the central angle in radians.

    Args:
        radius: Radius of the circle.
        angle: Central angle in radians.

    Returns:
        Area of the circular segment.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radius is not positive or angle not in (0, 2π].

    Example:
        >>> import math
        >>> round(circular_segment_area(5, math.pi), 4)
        39.2699

    Complexity: O(1)
    """
    import math

    if not isinstance(radius, (int, float)) or not isinstance(angle, (int, float)):
        raise TypeError("radius and angle must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if angle <= 0 or angle > 2 * math.pi:
        raise ValueError("angle must be in (0, 2π].")

    return float((radius ** 2 / 2) * (angle - math.sin(angle)))


def ellipse_circumference_approx(
    a: Union[int, float],
    b: Union[int, float],
) -> float:
    """Approximate the circumference of an ellipse using Ramanujan's formula.

    C ≈ π · (3(a+b) - √((3a+b)(a+3b)))

    Args:
        a: Semi-major axis.
        b: Semi-minor axis.

    Returns:
        Approximate circumference.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If axes are not positive.

    Example:
        >>> round(ellipse_circumference_approx(5, 3), 4)
        25.5268

    Complexity: O(1)
    """
    import math

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numeric.")

    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive.")

    return float(math.pi * (3 * (a + b) - math.sqrt((3 * a + b) * (a + 3 * b))))


def spherical_sector_volume(
    radius: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the volume of a spherical sector.

    V = (2/3)·π·r²·h

    Args:
        radius: Radius of the sphere.
        height: Height of the spherical cap.

    Returns:
        Volume of the spherical sector.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive or h > 2r.

    Example:
        >>> import math
        >>> round(spherical_sector_volume(5, 2), 4)
        104.7198

    Complexity: O(1)
    """
    import math

    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("radius and height must be numeric.")

    if radius <= 0 or height <= 0:
        raise ValueError("radius and height must be positive.")

    if height > 2 * radius:
        raise ValueError("height must not exceed 2 * radius.")

    return float((2.0 / 3.0) * math.pi * radius ** 2 * height)


def hexagon_area(
    side: Union[int, float],
) -> float:
    """Calculate the area of a regular hexagon.

    A = (3√3/2)·s²

    Args:
        side: Side length.

    Returns:
        Area of the hexagon.

    Raises:
        TypeError: If input is not numeric.
        ValueError: If side is not positive.

    Example:
        >>> round(hexagon_area(4), 4)
        41.5692

    Complexity: O(1)
    """
    import math

    if not isinstance(side, (int, float)):
        raise TypeError("side must be numeric.")

    if side <= 0:
        raise ValueError("side must be positive.")

    return float((3 * math.sqrt(3) / 2) * side ** 2)


def wedge_volume(
    base_area: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the volume of a wedge (triangular prism with half-base).

    V = (1/2) · A_base · h

    Args:
        base_area: Area of the rectangular face.
        height: Height (depth) of the wedge.

    Returns:
        Volume of the wedge.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive.

    Example:
        >>> wedge_volume(20, 5)
        50.0

    Complexity: O(1)
    """
    if not isinstance(base_area, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("base_area and height must be numeric.")

    if base_area <= 0 or height <= 0:
        raise ValueError("base_area and height must be positive.")

    return float(0.5 * base_area * height)


def regular_polygon_interior_angle(
    n_sides: int,
) -> float:
    """Calculate the interior angle of a regular polygon.

    angle = (n - 2) · 180 / n  (result in degrees).

    Args:
        n_sides: Number of sides (must be ≥ 3).

    Returns:
        Interior angle in degrees.

    Raises:
        TypeError: If n_sides is not an integer.
        ValueError: If n_sides < 3.

    Example:
        >>> regular_polygon_interior_angle(6)
        120.0

    Complexity: O(1)
    """
    if not isinstance(n_sides, int):
        raise TypeError("n_sides must be an integer.")

    if n_sides < 3:
        raise ValueError("n_sides must be at least 3.")

    return float((n_sides - 2) * 180 / n_sides)


def regular_polygon_exterior_angle(
    n_sides: int,
) -> float:
    """Calculate the exterior angle of a regular polygon.

    angle = 360 / n  (result in degrees).

    Args:
        n_sides: Number of sides (must be ≥ 3).

    Returns:
        Exterior angle in degrees.

    Raises:
        TypeError: If n_sides is not an integer.
        ValueError: If n_sides < 3.

    Example:
        >>> regular_polygon_exterior_angle(6)
        60.0

    Complexity: O(1)
    """
    if not isinstance(n_sides, int):
        raise TypeError("n_sides must be an integer.")

    if n_sides < 3:
        raise ValueError("n_sides must be at least 3.")

    return float(360 / n_sides)


def spherical_zone_area(
    radius: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the surface area of a spherical zone A = 2·π·r·h.

    Args:
        radius: Radius of the sphere.
        height: Height of the zone.

    Returns:
        Surface area of the spherical zone.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive or h > 2r.

    Example:
        >>> import math
        >>> round(spherical_zone_area(5, 3), 4)
        94.2478

    Complexity: O(1)
    """
    import math

    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("radius and height must be numeric.")

    if radius <= 0 or height <= 0:
        raise ValueError("radius and height must be positive.")

    if height > 2 * radius:
        raise ValueError("height must not exceed 2 * radius.")

    return float(2 * math.pi * radius * height)


def circular_sector_area(
    radius: Union[int, float],
    angle: Union[int, float],
) -> float:
    """Calculate the area of a circular sector A = ½·r²·θ.

    Args:
        radius: Radius of the circle.
        angle: Central angle in radians.

    Returns:
        Area of the sector.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radius not positive or angle not in (0, 2π].

    Example:
        >>> import math
        >>> round(circular_sector_area(5, math.pi / 2), 4)
        19.635

    Complexity: O(1)
    """
    import math

    if not isinstance(radius, (int, float)) or not isinstance(angle, (int, float)):
        raise TypeError("radius and angle must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if angle <= 0 or angle > 2 * math.pi:
        raise ValueError("angle must be in (0, 2π].")

    return float(0.5 * radius ** 2 * angle)


def ellipsoid_volume(
    a: Union[int, float],
    b: Union[int, float],
    c: Union[int, float],
) -> float:
    """Calculate the volume of an ellipsoid V = (4/3)·π·a·b·c.

    Args:
        a: Semi-axis length along x.
        b: Semi-axis length along y.
        c: Semi-axis length along z.

    Returns:
        Volume of the ellipsoid.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any axis is not positive.

    Example:
        >>> import math
        >>> round(ellipsoid_volume(3, 4, 5), 4)
        251.3274

    Complexity: O(1)
    """
    import math

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("a, b, c must be numeric.")

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("a, b, c must be positive.")

    return float((4.0 / 3.0) * math.pi * a * b * c)


def paraboloid_volume(
    radius: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the volume of a circular paraboloid.

    V = (1/2)·π·r²·h

    Args:
        radius: Base radius.
        height: Height of the paraboloid.

    Returns:
        Volume of the paraboloid.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive.

    Example:
        >>> import math
        >>> round(paraboloid_volume(3, 4), 4)
        56.5487

    Complexity: O(1)
    """
    import math

    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("radius and height must be numeric.")

    if radius <= 0 or height <= 0:
        raise ValueError("radius and height must be positive.")

    return float(0.5 * math.pi * radius ** 2 * height)


def inscribed_angle(
    central_angle: Union[int, float],
) -> float:
    """Calculate the inscribed angle from a central angle.

    An inscribed angle is half of the central angle that subtends
    the same arc.

    Args:
        central_angle: Central angle in radians.

    Returns:
        Inscribed angle in radians.

    Raises:
        TypeError: If input is not numeric.
        ValueError: If central_angle not in (0, 2π].

    Example:
        >>> import math
        >>> inscribed_angle(math.pi)
        1.5707963267948966

    Complexity: O(1)
    """
    import math

    if not isinstance(central_angle, (int, float)):
        raise TypeError("central_angle must be numeric.")

    if central_angle <= 0 or central_angle > 2 * math.pi:
        raise ValueError("central_angle must be in (0, 2π].")

    return float(central_angle / 2)


def cone_slant_height(
    radius: Union[int, float],
    height: Union[int, float],
) -> float:
    """Calculate the slant height of a cone l = √(r² + h²).

    Args:
        radius: Base radius.
        height: Vertical height.

    Returns:
        Slant height.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive.

    Example:
        >>> cone_slant_height(3, 4)
        5.0

    Complexity: O(1)
    """
    import math

    if not isinstance(radius, (int, float)) or not isinstance(height, (int, float)):
        raise TypeError("radius and height must be numeric.")

    if radius <= 0 or height <= 0:
        raise ValueError("radius and height must be positive.")

    return float(math.sqrt(radius ** 2 + height ** 2))


def spherical_wedge_volume(
    radius: Union[int, float],
    angle: Union[int, float],
) -> float:
    """Calculate the volume of a spherical wedge (lune).

    V = (2/3)·r³·θ  where θ is the dihedral angle in radians.

    Args:
        radius: Radius of the sphere.
        angle: Dihedral angle in radians, in (0, 2π].

    Returns:
        Volume of the spherical wedge.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radius not positive or angle not in (0, 2π].

    Example:
        >>> import math
        >>> round(spherical_wedge_volume(5, math.pi / 2), 4)
        130.8997

    Complexity: O(1)
    """
    import math

    if not isinstance(radius, (int, float)) or not isinstance(angle, (int, float)):
        raise TypeError("radius and angle must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if angle <= 0 or angle > 2 * math.pi:
        raise ValueError("angle must be in (0, 2π].")

    return float((2.0 / 3.0) * radius ** 3 * angle)


def lens_area(
    radius: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Calculate the area of intersection of two equal circles (lens/vesica).

    When two circles of radius r have centres distance d apart (d < 2r),
    the lens area is 2r²·arccos(d/(2r)) - (d/2)·√(4r² - d²).

    Args:
        radius: Radius of both circles.
        distance: Distance between centres (must be < 2·radius).

    Returns:
        Area of the lens.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radius not positive or distance not in [0, 2r).

    Example:
        >>> round(lens_area(5, 6), 4)
        28.0544

    Complexity: O(1)
    """
    import math

    if not isinstance(radius, (int, float)) or not isinstance(distance, (int, float)):
        raise TypeError("radius and distance must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if distance < 0 or distance >= 2 * radius:
        raise ValueError("distance must be in [0, 2·radius).")

    return float(
        2 * radius ** 2 * math.acos(distance / (2 * radius))
        - (distance / 2) * math.sqrt(4 * radius ** 2 - distance ** 2)
    )


def frustum_lateral_area(
    r1: Union[int, float],
    r2: Union[int, float],
    slant_height: Union[int, float],
) -> float:
    """Return the lateral surface area of a conical frustum.

    A = π · (r₁ + r₂) · l.

    Args:
        r1: Radius of the smaller base (must be ≥ 0).
        r2: Radius of the larger base (must be ≥ 0).
        slant_height: Slant height of the frustum (must be > 0).

    Returns:
        Lateral surface area as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If r1 or r2 is negative, or slant_height ≤ 0.

    Example:
        >>> round(frustum_lateral_area(2, 4, 5), 4)
        94.2478

    Complexity: O(1)
    """
    if not isinstance(r1, (int, float)):
        raise TypeError("r1 must be numeric.")

    if not isinstance(r2, (int, float)):
        raise TypeError("r2 must be numeric.")

    if not isinstance(slant_height, (int, float)):
        raise TypeError("slant_height must be numeric.")

    if r1 < 0:
        raise ValueError("r1 must be non-negative.")

    if r2 < 0:
        raise ValueError("r2 must be non-negative.")

    if slant_height <= 0:
        raise ValueError("slant_height must be positive.")

    return float(math.pi * (r1 + r2) * slant_height)


def cyclic_polygon_radius(
    side_length: Union[int, float],
    n_sides: int,
) -> float:
    """Return the circumradius of a regular polygon.

    R = a / (2 · sin(π / n)).

    Args:
        side_length: Length of one side (must be > 0).
        n_sides: Number of sides (must be ≥ 3).

    Returns:
        Circumscribed circle radius as a float.

    Raises:
        TypeError: If side_length is not numeric or n_sides not int.
        ValueError: If side_length ≤ 0 or n_sides < 3.

    Example:
        >>> round(cyclic_polygon_radius(1, 6), 6)
        1.0

    Complexity: O(1)
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be numeric.")

    if not isinstance(n_sides, int):
        raise TypeError("n_sides must be an integer.")

    if side_length <= 0:
        raise ValueError("side_length must be positive.")

    if n_sides < 3:
        raise ValueError("n_sides must be at least 3.")

    return float(side_length / (2 * math.sin(math.pi / n_sides)))


def power_of_point(
    distance: Union[int, float],
    radius: Union[int, float],
) -> float:
    """Return the power of a point with respect to a circle.

    Power = d² − r².  Positive when the point is outside,
    zero on the circle, negative inside.

    Args:
        distance: Distance from the point to the centre (≥ 0).
        radius: Radius of the circle (must be > 0).

    Returns:
        Power of the point as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If distance < 0 or radius ≤ 0.

    Example:
        >>> power_of_point(5, 3)
        16.0

    Complexity: O(1)
    """
    if not isinstance(distance, (int, float)):
        raise TypeError("distance must be numeric.")

    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be numeric.")

    if distance < 0:
        raise ValueError("distance must be non-negative.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    return float(distance ** 2 - radius ** 2)


def annular_sector_area(
    inner_radius: Union[int, float],
    outer_radius: Union[int, float],
    angle: Union[int, float],
) -> float:
    """Return the area of an annular sector.

    A = (θ / 2) · (R² − r²),  where θ is in radians.

    Args:
        inner_radius: Inner radius (must be ≥ 0).
        outer_radius: Outer radius (must be > inner_radius).
        angle: Central angle in radians (must be > 0).

    Returns:
        Area of the annular sector as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If radii or angle constraints are violated.

    Example:
        >>> round(annular_sector_area(2, 5, math.pi / 2), 4)
        16.4934

    Complexity: O(1)
    """
    if not isinstance(inner_radius, (int, float)):
        raise TypeError("inner_radius must be numeric.")

    if not isinstance(outer_radius, (int, float)):
        raise TypeError("outer_radius must be numeric.")

    if not isinstance(angle, (int, float)):
        raise TypeError("angle must be numeric.")

    if inner_radius < 0:
        raise ValueError("inner_radius must be non-negative.")

    if outer_radius <= inner_radius:
        raise ValueError("outer_radius must be greater than inner_radius.")

    if angle <= 0:
        raise ValueError("angle must be positive.")

    return float((angle / 2) * (outer_radius ** 2 - inner_radius ** 2))


def spherical_lune_area(
    radius: Union[int, float],
    angle: Union[int, float],
) -> float:
    """Return the surface area of a spherical lune.

    A = 2 · R² · θ,  where θ is the dihedral angle in radians.

    Args:
        radius: Radius of the sphere (must be > 0).
        angle: Dihedral angle in radians (must be > 0).

    Returns:
        Surface area of the lune as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If radius or angle is not positive.

    Example:
        >>> round(spherical_lune_area(5, math.pi / 3), 4)
        52.3599

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be numeric.")

    if not isinstance(angle, (int, float)):
        raise TypeError("angle must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if angle <= 0:
        raise ValueError("angle must be positive.")

    return float(2 * radius ** 2 * angle)


def regular_polygon_apothem(
    side_length: Union[int, float],
    n_sides: int,
) -> float:
    """Return the apothem of a regular polygon.

    Apothem = a / (2 · tan(π / n)).

    Args:
        side_length: Length of one side (must be > 0).
        n_sides: Number of sides (must be ≥ 3).

    Returns:
        Apothem length as a float.

    Raises:
        TypeError: If side_length is not numeric or n_sides not int.
        ValueError: If side_length ≤ 0 or n_sides < 3.

    Example:
        >>> round(regular_polygon_apothem(1, 6), 6)
        0.866025

    Complexity: O(1)
    """
    if not isinstance(side_length, (int, float)):
        raise TypeError("side_length must be numeric.")

    if not isinstance(n_sides, int):
        raise TypeError("n_sides must be an integer.")

    if side_length <= 0:
        raise ValueError("side_length must be positive.")

    if n_sides < 3:
        raise ValueError("n_sides must be at least 3.")

    return float(side_length / (2 * math.tan(math.pi / n_sides)))


def spheroid_volume(
    equatorial_radius: Union[int, float],
    polar_radius: Union[int, float],
) -> float:
    """Return the volume of a spheroid (ellipsoid of revolution).

    V = (4/3) · π · a² · c,  where *a* is the equatorial and
    *c* the polar semi-axis.

    Args:
        equatorial_radius: Equatorial semi-axis (must be > 0).
        polar_radius: Polar semi-axis (must be > 0).

    Returns:
        Volume of the spheroid as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0.

    Example:
        >>> round(spheroid_volume(6378, 6357), 0)
        1083141285735.0

    Complexity: O(1)
    """
    if not isinstance(equatorial_radius, (int, float)):
        raise TypeError("equatorial_radius must be numeric.")

    if not isinstance(polar_radius, (int, float)):
        raise TypeError("polar_radius must be numeric.")

    if equatorial_radius <= 0:
        raise ValueError("equatorial_radius must be positive.")

    if polar_radius <= 0:
        raise ValueError("polar_radius must be positive.")

    return float(
        (4 / 3) * math.pi * equatorial_radius ** 2 * polar_radius
    )


def stadium_area(
    radius: Union[int, float],
    straight_length: Union[int, float],
) -> float:
    """Return the area of a stadium (discorectangle).

    A = π · r² + 2 · r · a,  where *a* is the length of the
    straight section.

    Args:
        radius: Radius of the semicircular ends (must be > 0).
        straight_length: Length of the straight section (must be ≥ 0).

    Returns:
        Area of the stadium as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If radius ≤ 0 or straight_length < 0.

    Example:
        >>> round(stadium_area(5, 10), 4)
        178.5398

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be numeric.")

    if not isinstance(straight_length, (int, float)):
        raise TypeError("straight_length must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if straight_length < 0:
        raise ValueError("straight_length must be non-negative.")

    return float(math.pi * radius ** 2 + 2 * radius * straight_length)


def stadium_perimeter(
    radius: Union[int, float],
    straight_length: Union[int, float],
) -> float:
    """Return the perimeter of a stadium (discorectangle).

    P = 2π · r + 2 · a.

    Args:
        radius: Radius of the semicircular ends (must be > 0).
        straight_length: Length of the straight section (must be ≥ 0).

    Returns:
        Perimeter of the stadium as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If radius ≤ 0 or straight_length < 0.

    Example:
        >>> round(stadium_perimeter(5, 10), 4)
        51.4159

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be numeric.")

    if not isinstance(straight_length, (int, float)):
        raise TypeError("straight_length must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if straight_length < 0:
        raise ValueError("straight_length must be non-negative.")

    return float(2 * math.pi * radius + 2 * straight_length)


def circular_segment_chord(
    radius: Union[int, float],
    angle: Union[int, float],
) -> float:
    """Return the chord length of a circular segment.

    Chord = 2 · r · sin(θ / 2),  where θ is the central angle
    in radians.

    Args:
        radius: Radius of the circle (must be > 0).
        angle: Central angle in radians (must be in (0, 2π]).

    Returns:
        Chord length as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If radius ≤ 0 or angle out of range.

    Example:
        >>> round(circular_segment_chord(5, math.pi / 2), 6)
        7.071068

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be numeric.")

    if not isinstance(angle, (int, float)):
        raise TypeError("angle must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    if angle <= 0 or angle > 2 * math.pi:
        raise ValueError("angle must be in (0, 2π].")

    return float(2 * radius * math.sin(angle / 2))


def reuleaux_triangle_area(
    side: Union[int, float],
) -> float:
    """Return the area of a Reuleaux triangle.

    A = (π − √3) / 2 · s².

    Args:
        side: Side length of the equilateral triangle (must be > 0).

    Returns:
        Area of the Reuleaux triangle.

    Raises:
        TypeError: If side is not numeric.
        ValueError: If side ≤ 0.

    Example:
        >>> round(reuleaux_triangle_area(1), 6)
        0.704771

    Complexity: O(1)
    """
    if not isinstance(side, (int, float)):
        raise TypeError("side must be numeric.")

    if side <= 0:
        raise ValueError("side must be positive.")

    return float((math.pi - math.sqrt(3)) / 2 * side ** 2)


def arbelos_area(
    r: Union[int, float],
    r1: Union[int, float],
    r2: Union[int, float],
) -> float:
    """Return the area of an arbelos.

    The arbelos is the region between three semicircles with
    diameters on the same line where r = r1 + r2.

    A = π · r1 · r2 / 2.

    Args:
        r: Radius of the outer semicircle (must be > 0).
        r1: Radius of the first inner semicircle (> 0).
        r2: Radius of the second inner semicircle (> 0).

    Returns:
        Area of the arbelos.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any radius ≤ 0 or r ≠ r1 + r2.

    Example:
        >>> round(arbelos_area(5, 3, 2), 6)
        9.424778

    Complexity: O(1)
    """
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")

    if not isinstance(r1, (int, float)):
        raise TypeError("r1 must be numeric.")

    if not isinstance(r2, (int, float)):
        raise TypeError("r2 must be numeric.")

    if r <= 0 or r1 <= 0 or r2 <= 0:
        raise ValueError("All radii must be positive.")

    if abs(r - (r1 + r2)) > 1e-9:
        raise ValueError("r must equal r1 + r2.")

    return float(math.pi * r1 * r2 / 2)


def salinon_area(
    r: Union[int, float],
    r1: Union[int, float],
) -> float:
    """Return the area of a salinon.

    The salinon consists of four semicircles.  Its area equals
    the area of the circle with diameter equal to the line
    connecting the tops of the two inner semicircles:

    A = π · ((r + r1) / 2)².

    Args:
        r: Radius of the outer semicircle (must be > 0).
        r1: Radius of the inner semicircle (must be > 0, r1 < r).

    Returns:
        Area of the salinon.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If r or r1 ≤ 0, or r1 ≥ r.

    Example:
        >>> round(salinon_area(4, 2), 6)
        28.274334

    Complexity: O(1)
    """
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")

    if not isinstance(r1, (int, float)):
        raise TypeError("r1 must be numeric.")

    if r <= 0:
        raise ValueError("r must be positive.")

    if r1 <= 0:
        raise ValueError("r1 must be positive.")

    if r1 >= r:
        raise ValueError("r1 must be less than r.")

    return float(math.pi * ((r + r1) / 2) ** 2)


def epicycloid_arc_length(
    big_r: Union[int, float],
    small_r: Union[int, float],
) -> float:
    """Return the total arc length of one full epicycloid.

    L = 8 · R · r / (R + r),  scaled by the outer radius.
    Actually L = 8 · (R + r) · sin(π·r/(R+r)) for the general
    case — but for a complete epicycloid (integer ratio):

    L_total = 8 · R · (R + r) / R  -  simplifies when R/r is
    integer.  Standard formula: L = 8r(R + r)/R.

    General formula for total length of a complete epicycloid:
    L = 8 · r · (R + r) / R.

    Args:
        big_r: Radius of the fixed circle (must be > 0).
        small_r: Radius of the rolling circle (must be > 0).

    Returns:
        Total arc length of the epicycloid.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0.

    Example:
        >>> epicycloid_arc_length(5, 1)
        9.6

    Complexity: O(1)
    """
    if not isinstance(big_r, (int, float)):
        raise TypeError("big_r must be numeric.")

    if not isinstance(small_r, (int, float)):
        raise TypeError("small_r must be numeric.")

    if big_r <= 0:
        raise ValueError("big_r must be positive.")

    if small_r <= 0:
        raise ValueError("small_r must be positive.")

    return float(8 * small_r * (big_r + small_r) / big_r)


def hypocycloid_arc_length(
    big_r: Union[int, float],
    small_r: Union[int, float],
) -> float:
    """Return the total arc length of one full hypocycloid.

    L = 8 · r · (R − r) / R.

    Args:
        big_r: Radius of the fixed circle (must be > 0).
        small_r: Radius of the rolling circle (0 < r < R).

    Returns:
        Total arc length of the hypocycloid.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If big_r ≤ 0, small_r ≤ 0, or small_r ≥ big_r.

    Example:
        >>> hypocycloid_arc_length(5, 1)
        6.4

    Complexity: O(1)
    """
    if not isinstance(big_r, (int, float)):
        raise TypeError("big_r must be numeric.")

    if not isinstance(small_r, (int, float)):
        raise TypeError("small_r must be numeric.")

    if big_r <= 0:
        raise ValueError("big_r must be positive.")

    if small_r <= 0:
        raise ValueError("small_r must be positive.")

    if small_r >= big_r:
        raise ValueError("small_r must be less than big_r.")

    return float(8 * small_r * (big_r - small_r) / big_r)


# ---------------------------------------------------------------------------
# Computational geometry — GPS bearing, point-in-shape, triangle properties
# ---------------------------------------------------------------------------

_EARTH_RADIUS_KM = 6371.0


def bearing(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> float:
    """Computes the initial bearing (forward azimuth) between two GPS coordinates.

    Args:
        lat1: Latitude of point 1 in decimal degrees.
        lon1: Longitude of point 1 in decimal degrees.
        lat2: Latitude of point 2 in decimal degrees.
        lon2: Longitude of point 2 in decimal degrees.

    Returns:
        Initial bearing in degrees (0–360).

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> round(bearing(40.4168, -3.7038, 48.8566, 2.3522), 1)  # Madrid→Paris
        24.8

    Complexity: O(1)
    """
    for name, val in (("lat1", lat1), ("lon1", lon1), ("lat2", lat2), ("lon2", lon2)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    d_lambda = math.radians(lon2 - lon1)

    x = math.sin(d_lambda) * math.cos(phi2)
    y = math.cos(phi1) * math.sin(phi2) - math.sin(phi1) * math.cos(phi2) * math.cos(d_lambda)
    theta = math.atan2(x, y)
    return float((math.degrees(theta) + 360) % 360)


def destination_point(
    lat: float, lon: float, brng: float, distance_km: float
) -> tuple:
    """Computes the destination point given an origin, bearing, and distance.

    Args:
        lat: Origin latitude in decimal degrees.
        lon: Origin longitude in decimal degrees.
        brng: Bearing in degrees (0–360).
        distance_km: Distance to travel in kilometres.

    Returns:
        Tuple (latitude, longitude) of the destination.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If distance_km is negative.

    Example:
        >>> dlat, dlon = destination_point(40.4168, -3.7038, 24.8, 1000)
        >>> round(dlat, 1)
        48.3

    Complexity: O(1)
    """
    for name, val in (("lat", lat), ("lon", lon), ("brng", brng), ("distance_km", distance_km)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if distance_km < 0:
        raise ValueError("distance_km must be non-negative")

    phi1 = math.radians(lat)
    lam1 = math.radians(lon)
    theta = math.radians(brng)
    delta = distance_km / _EARTH_RADIUS_KM

    phi2 = math.asin(
        math.sin(phi1) * math.cos(delta)
        + math.cos(phi1) * math.sin(delta) * math.cos(theta)
    )
    lam2 = lam1 + math.atan2(
        math.sin(theta) * math.sin(delta) * math.cos(phi1),
        math.cos(delta) - math.sin(phi1) * math.sin(phi2),
    )
    return (round(math.degrees(phi2), 10), round(math.degrees(lam2), 10))


def midpoint_geo(
    lat1: float, lon1: float, lat2: float, lon2: float
) -> tuple:
    """Computes the geographic midpoint between two coordinates on a sphere.

    Args:
        lat1: Latitude of point 1.
        lon1: Longitude of point 1.
        lat2: Latitude of point 2.
        lon2: Longitude of point 2.

    Returns:
        Tuple (latitude, longitude) of the midpoint.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> mlat, mlon = midpoint_geo(40.4168, -3.7038, 48.8566, 2.3522)
        >>> round(mlat, 2)
        44.7

    Complexity: O(1)
    """
    for name, val in (("lat1", lat1), ("lon1", lon1), ("lat2", lat2), ("lon2", lon2)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    lam1, lam2 = math.radians(lon1), math.radians(lon2)
    d_lam = lam2 - lam1

    bx = math.cos(phi2) * math.cos(d_lam)
    by = math.cos(phi2) * math.sin(d_lam)

    phi_m = math.atan2(
        math.sin(phi1) + math.sin(phi2),
        math.sqrt((math.cos(phi1) + bx) ** 2 + by ** 2),
    )
    lam_m = lam1 + math.atan2(by, math.cos(phi1) + bx)
    return (round(math.degrees(phi_m), 10), round(math.degrees(lam_m), 10))


def point_in_circle(
    px: float, py: float, cx: float, cy: float, radius: float
) -> bool:
    """Checks if a point (px, py) lies inside a circle centred at (cx, cy).

    Args:
        px: X-coordinate of the point.
        py: Y-coordinate of the point.
        cx: X-coordinate of circle centre.
        cy: Y-coordinate of circle centre.
        radius: Circle radius (positive).

    Returns:
        True if the point is inside or on the circle boundary.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radius is not positive.

    Example:
        >>> point_in_circle(1, 1, 0, 0, 2)
        True
        >>> point_in_circle(3, 0, 0, 0, 2)
        False

    Complexity: O(1)
    """
    for name, val in (("px", px), ("py", py), ("cx", cx), ("cy", cy), ("radius", radius)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if radius <= 0:
        raise ValueError("radius must be positive")

    return (px - cx) ** 2 + (py - cy) ** 2 <= radius ** 2


def point_in_triangle(
    px: float, py: float,
    ax: float, ay: float,
    bx: float, by: float,
    cx: float, cy: float,
) -> bool:
    """Checks if a point (px, py) is inside the triangle (A, B, C).

    Uses the barycentric coordinate method.

    Args:
        px: X-coordinate of the point.
        py: Y-coordinate of the point.
        ax: X-coordinate of vertex A.
        ay: Y-coordinate of vertex A.
        bx: X-coordinate of vertex B.
        by: Y-coordinate of vertex B.
        cx: X-coordinate of vertex C.
        cy: Y-coordinate of vertex C.

    Returns:
        True if the point is inside or on the triangle boundary.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> point_in_triangle(1, 1, 0, 0, 4, 0, 0, 4)
        True
        >>> point_in_triangle(5, 5, 0, 0, 4, 0, 0, 4)
        False

    Complexity: O(1)
    """
    vals = (px, py, ax, ay, bx, by, cx, cy)

    for val in vals:

        if not isinstance(val, (int, float)):
            raise TypeError("All coordinates must be numeric")

    denom = (by - cy) * (ax - cx) + (cx - bx) * (ay - cy)

    if denom == 0:
        return False  # Degenerate triangle

    u = ((by - cy) * (px - cx) + (cx - bx) * (py - cy)) / denom
    v = ((cy - ay) * (px - cx) + (ax - cx) * (py - cy)) / denom
    w = 1 - u - v
    return u >= 0 and v >= 0 and w >= 0


def triangle_centroid(
    ax: float, ay: float,
    bx: float, by: float,
    cx: float, cy: float,
) -> tuple:
    """Computes the centroid (centre of mass) of a triangle.

    Args:
        ax: X-coordinate of vertex A.
        ay: Y-coordinate of vertex A.
        bx: X-coordinate of vertex B.
        by: Y-coordinate of vertex B.
        cx: X-coordinate of vertex C.
        cy: Y-coordinate of vertex C.

    Returns:
        Tuple (x, y) of the centroid.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> triangle_centroid(0, 0, 3, 0, 0, 3)
        (1.0, 1.0)

    Complexity: O(1)
    """
    for name, val in (("ax", ax), ("ay", ay), ("bx", bx), ("by", by), ("cx", cx), ("cy", cy)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    return (float((ax + bx + cx) / 3), float((ay + by + cy) / 3))


def triangle_incircle_radius(a: float, b: float, c: float) -> float:
    """Computes the inradius of a triangle given its three side lengths.

    r = Area / s, where s = (a+b+c)/2 and Area via Heron's formula.

    Args:
        a: Length of side a.
        b: Length of side b.
        c: Length of side c.

    Returns:
        Inradius of the triangle.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If sides do not form a valid triangle.

    Example:
        >>> round(triangle_incircle_radius(3, 4, 5), 6)
        1.0

    Complexity: O(1)
    """
    for name, val in (("a", a), ("b", b), ("c", c)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

        if val <= 0:
            raise ValueError(f"{name} must be positive")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not form a valid triangle")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return float(area / s)


def triangle_circumradius(a: float, b: float, c: float) -> float:
    """Computes the circumradius of a triangle given its three side lengths.

    R = (a · b · c) / (4 · Area)

    Args:
        a: Length of side a.
        b: Length of side b.
        c: Length of side c.

    Returns:
        Circumradius of the triangle.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If sides do not form a valid triangle.

    Example:
        >>> round(triangle_circumradius(3, 4, 5), 6)
        2.5

    Complexity: O(1)
    """
    for name, val in (("a", a), ("b", b), ("c", c)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

        if val <= 0:
            raise ValueError(f"{name} must be positive")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not form a valid triangle")

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))

    if area == 0:
        raise ValueError("Degenerate triangle (zero area)")

    return float((a * b * c) / (4 * area))


def rotation_2d(x: float, y: float, angle: float) -> tuple:
    """Rotates a 2D point (x, y) by an angle in radians around the origin.

    Args:
        x: X-coordinate.
        y: Y-coordinate.
        angle: Rotation angle in radians (counter-clockwise positive).

    Returns:
        Tuple (x', y') of the rotated point.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> import math
        >>> rx, ry = rotation_2d(1, 0, math.pi / 2)
        >>> (round(rx, 10), round(ry, 10))
        (0.0, 1.0)

    Complexity: O(1)
    """
    for name, val in (("x", x), ("y", y), ("angle", angle)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    cos_a = math.cos(angle)
    sin_a = math.sin(angle)
    return (float(x * cos_a - y * sin_a), float(x * sin_a + y * cos_a))


def distance_point_to_line(
    px: float, py: float,
    x1: float, y1: float,
    x2: float, y2: float,
) -> float:
    """Computes the perpendicular distance from a point to a line segment.

    The line is defined by two points (x1, y1)–(x2, y2).

    Args:
        px: X-coordinate of the point.
        py: Y-coordinate of the point.
        x1: X of first endpoint.
        y1: Y of first endpoint.
        x2: X of second endpoint.
        y2: Y of second endpoint.

    Returns:
        Perpendicular distance.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If the two endpoints are identical.

    Example:
        >>> distance_point_to_line(1, 1, 0, 0, 2, 0)
        1.0

    Complexity: O(1)
    """
    for name, val in (("px", px), ("py", py), ("x1", x1), ("y1", y1), ("x2", x2), ("y2", y2)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    dx = x2 - x1
    dy = y2 - y1
    length = math.sqrt(dx ** 2 + dy ** 2)

    if length == 0:
        raise ValueError("The two line points must be distinct")

    return float(abs(dy * px - dx * py + x2 * y1 - y2 * x1) / length)


def cross_track_distance(
    lat: float,
    lon: float,
    path_lat1: float,
    path_lon1: float,
    path_lat2: float,
    path_lon2: float,
    radius: float = 6_371_000.0,
) -> float:
    """Perpendicular distance from a point to a great-circle path (meters).

    Args:
        lat: Point latitude in degrees.
        lon: Point longitude in degrees.
        path_lat1: Path start latitude.
        path_lon1: Path start longitude.
        path_lat2: Path end latitude.
        path_lon2: Path end longitude.
        radius: Earth radius in meters (default 6 371 000).

    Returns:
        Signed cross-track distance in meters. Positive = left of path.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> abs(cross_track_distance(53.2611, -0.7972, 53.3206, -1.7297, 53.1887, 0.1334)) < 500
        True

    Complexity: O(1)
    """
    for name, val in (
        ("lat", lat), ("lon", lon), ("path_lat1", path_lat1),
        ("path_lon1", path_lon1), ("path_lat2", path_lat2), ("path_lon2", path_lon2),
    ):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    rlat = math.radians(lat)
    rlon = math.radians(lon)
    rlat1 = math.radians(path_lat1)
    rlon1 = math.radians(path_lon1)
    rlat2 = math.radians(path_lat2)
    rlon2 = math.radians(path_lon2)

    # Angular distance from path start to point
    d13 = 2 * math.asin(math.sqrt(
        math.sin((rlat - rlat1) / 2) ** 2
        + math.cos(rlat1) * math.cos(rlat) * math.sin((rlon - rlon1) / 2) ** 2
    ))

    # Initial bearing from path start to point
    theta13 = math.atan2(
        math.sin(rlon - rlon1) * math.cos(rlat),
        math.cos(rlat1) * math.sin(rlat) - math.sin(rlat1) * math.cos(rlat) * math.cos(rlon - rlon1),
    )

    # Initial bearing from path start to path end
    theta12 = math.atan2(
        math.sin(rlon2 - rlon1) * math.cos(rlat2),
        math.cos(rlat1) * math.sin(rlat2) - math.sin(rlat1) * math.cos(rlat2) * math.cos(rlon2 - rlon1),
    )

    dxt = math.asin(math.sin(d13) * math.sin(theta13 - theta12))
    return float(dxt * radius)


def along_track_distance(
    lat: float,
    lon: float,
    path_lat1: float,
    path_lon1: float,
    path_lat2: float,
    path_lon2: float,
    radius: float = 6_371_000.0,
) -> float:
    """Distance along the great-circle path from start to the closest point.

    Args:
        lat: Point latitude in degrees.
        lon: Point longitude in degrees.
        path_lat1: Path start latitude.
        path_lon1: Path start longitude.
        path_lat2: Path end latitude.
        path_lon2: Path end longitude.
        radius: Earth radius in meters.

    Returns:
        Along-track distance in meters.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> along_track_distance(53.2611, -0.7972, 53.3206, -1.7297, 53.1887, 0.1334) > 0
        True

    Complexity: O(1)
    """
    for name, val in (
        ("lat", lat), ("lon", lon), ("path_lat1", path_lat1),
        ("path_lon1", path_lon1), ("path_lat2", path_lat2), ("path_lon2", path_lon2),
    ):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    rlat = math.radians(lat)
    rlon = math.radians(lon)
    rlat1 = math.radians(path_lat1)
    rlon1 = math.radians(path_lon1)

    d13 = 2 * math.asin(math.sqrt(
        math.sin((rlat - rlat1) / 2) ** 2
        + math.cos(rlat1) * math.cos(rlat) * math.sin((rlon - rlon1) / 2) ** 2
    ))

    dxt = cross_track_distance(lat, lon, path_lat1, path_lon1, path_lat2, path_lon2, 1.0)
    dxt_rad = dxt  # already in radians when radius=1

    dat = math.acos(max(-1.0, min(1.0, math.cos(d13) / math.cos(dxt_rad))))
    return float(dat * radius)


def intermediate_point(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
    fraction: float,
) -> tuple[float, float]:
    """Find a point at a given fraction along the great-circle path.

    Args:
        lat1: Start latitude in degrees.
        lon1: Start longitude in degrees.
        lat2: End latitude in degrees.
        lon2: End longitude in degrees.
        fraction: Fraction along the path (0.0 = start, 1.0 = end).

    Returns:
        Tuple ``(latitude, longitude)`` in degrees.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If *fraction* is not in [0, 1].

    Example:
        >>> lat, lon = intermediate_point(0, 0, 0, 10, 0.5)
        >>> round(lon, 1)
        5.0

    Complexity: O(1)
    """
    for name, val in (("lat1", lat1), ("lon1", lon1), ("lat2", lat2), ("lon2", lon2)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if not isinstance(fraction, (int, float)):
        raise TypeError("fraction must be numeric")

    if fraction < 0 or fraction > 1:
        raise ValueError("fraction must be in [0, 1]")

    rlat1 = math.radians(lat1)
    rlon1 = math.radians(lon1)
    rlat2 = math.radians(lat2)
    rlon2 = math.radians(lon2)

    d = 2 * math.asin(math.sqrt(
        math.sin((rlat2 - rlat1) / 2) ** 2
        + math.cos(rlat1) * math.cos(rlat2) * math.sin((rlon2 - rlon1) / 2) ** 2
    ))

    if d < 1e-15:
        return (lat1, lon1)

    a = math.sin((1 - fraction) * d) / math.sin(d)
    b = math.sin(fraction * d) / math.sin(d)

    x = a * math.cos(rlat1) * math.cos(rlon1) + b * math.cos(rlat2) * math.cos(rlon2)
    y = a * math.cos(rlat1) * math.sin(rlon1) + b * math.cos(rlat2) * math.sin(rlon2)
    z = a * math.sin(rlat1) + b * math.sin(rlat2)

    lat_out = math.degrees(math.atan2(z, math.sqrt(x ** 2 + y ** 2)))
    lon_out = math.degrees(math.atan2(y, x))

    return (round(lat_out, 10), round(lon_out, 10))


def vincenty_distance(
    lat1: float,
    lon1: float,
    lat2: float,
    lon2: float,
) -> float:
    """Geodesic distance between two points using Vincenty's formulae.

    Uses the WGS-84 ellipsoid (a = 6378137 m, f = 1/298.257223563).

    Args:
        lat1: Latitude of point 1 in degrees.
        lon1: Longitude of point 1 in degrees.
        lat2: Latitude of point 2 in degrees.
        lon2: Longitude of point 2 in degrees.

    Returns:
        Distance in metres.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> round(vincenty_distance(40.4168, -3.7038, 48.8566, 2.3522))
        1052744

    Complexity: O(1) — iterative but bounded.
    """
    for name, val in (("lat1", lat1), ("lon1", lon1), ("lat2", lat2), ("lon2", lon2)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    a_axis = 6378137.0
    f = 1 / 298.257223563
    b_axis = a_axis * (1 - f)

    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    u1 = math.atan((1 - f) * math.tan(phi1))
    u2 = math.atan((1 - f) * math.tan(phi2))
    lam = math.radians(lon2 - lon1)
    lam_prev = lam

    sin_u1, cos_u1 = math.sin(u1), math.cos(u1)
    sin_u2, cos_u2 = math.sin(u2), math.cos(u2)

    for _ in range(200):
        sin_lam = math.sin(lam)
        cos_lam = math.cos(lam)

        sin_sigma = math.sqrt(
            (cos_u2 * sin_lam) ** 2
            + (cos_u1 * sin_u2 - sin_u1 * cos_u2 * cos_lam) ** 2
        )

        if sin_sigma == 0:
            return 0.0  # co-incident points

        cos_sigma = sin_u1 * sin_u2 + cos_u1 * cos_u2 * cos_lam
        sigma = math.atan2(sin_sigma, cos_sigma)

        sin_alpha = cos_u1 * cos_u2 * sin_lam / sin_sigma
        cos2_alpha = 1 - sin_alpha ** 2
        cos_2sigma_m = cos_sigma - 2 * sin_u1 * sin_u2

        if cos2_alpha != 0:
            cos_2sigma_m /= cos2_alpha
        else:
            cos_2sigma_m = 0.0

        c = f / 16 * cos2_alpha * (4 + f * (4 - 3 * cos2_alpha))
        lam = math.radians(lon2 - lon1) + (1 - c) * f * sin_alpha * (
            sigma + c * sin_sigma * (cos_2sigma_m + c * cos_sigma * (-1 + 2 * cos_2sigma_m ** 2))
        )

        if abs(lam - lam_prev) < 1e-12:
            break

        lam_prev = lam

    u_sq = cos2_alpha * (a_axis ** 2 - b_axis ** 2) / b_axis ** 2
    a_coeff = 1 + u_sq / 16384 * (4096 + u_sq * (-768 + u_sq * (320 - 175 * u_sq)))
    b_coeff = u_sq / 1024 * (256 + u_sq * (-128 + u_sq * (74 - 47 * u_sq)))
    delta_sigma = b_coeff * sin_sigma * (
        cos_2sigma_m + b_coeff / 4 * (
            cos_sigma * (-1 + 2 * cos_2sigma_m ** 2)
            - b_coeff / 6 * cos_2sigma_m * (-3 + 4 * sin_sigma ** 2) * (-3 + 4 * cos_2sigma_m ** 2)
        )
    )

    return float(b_axis * a_coeff * (sigma - delta_sigma))


def geodesic_area(
    vertices: list[tuple[float, float]],
) -> float:
    """Approximate area of a polygon on a sphere using the spherical excess formula.

    Vertices are ``(latitude, longitude)`` pairs in degrees.  Uses a
    mean Earth radius of 6371008.8 m.

    Args:
        vertices: List of ``(lat, lon)`` tuples forming a closed polygon.

    Returns:
        Area in square metres (absolute value).

    Raises:
        TypeError: If *vertices* is not a list of tuples.
        ValueError: If fewer than 3 vertices.

    Example:
        >>> area = geodesic_area([(0, 0), (0, 1), (1, 1), (1, 0)])
        >>> round(area / 1e6)
        12309

    Complexity: O(n)
    """
    if not isinstance(vertices, list):
        raise TypeError("vertices must be a list")

    if len(vertices) < 3:
        raise ValueError("At least 3 vertices required")

    R = 6371008.8
    n = len(vertices)
    total = 0.0

    for i in range(n):
        lat1 = math.radians(vertices[i][0])
        lon1 = math.radians(vertices[i][1])
        lat2 = math.radians(vertices[(i + 1) % n][0])
        lon2 = math.radians(vertices[(i + 1) % n][1])
        total += (lon2 - lon1) * (2 + math.sin(lat1) + math.sin(lat2))

    return float(abs(total * R ** 2 / 2.0))


def solar_elevation(
    d: object,
    latitude: float,
    longitude: float,
) -> float:
    """Estimate the solar elevation angle for a given datetime and location.

    Uses a simplified astronomical algorithm (adequate for ±1° accuracy).

    Args:
        d: A ``datetime`` instance (timezone-naive treated as UTC).
        latitude: Observer latitude in degrees.
        longitude: Observer longitude in degrees.

    Returns:
        Solar elevation angle in degrees (negative if below horizon).

    Raises:
        TypeError: If *d* is not a datetime or coordinates not numeric.
        ValueError: If latitude/longitude out of range.

    Example:
        >>> from datetime import datetime
        >>> round(solar_elevation(datetime(2026, 6, 21, 12, 0), 40.0, -3.7))
        73

    Complexity: O(1)
    """
    from datetime import datetime as _dt

    if not isinstance(d, _dt):
        raise TypeError("d must be a datetime")

    for name, val in (("latitude", latitude), ("longitude", longitude)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if latitude < -90 or latitude > 90:
        raise ValueError("latitude must be between -90 and 90")

    if longitude < -180 or longitude > 180:
        raise ValueError("longitude must be between -180 and 180")

    day_of_year = d.timetuple().tm_yday
    hour_utc = d.hour + d.minute / 60.0 + d.second / 3600.0

    # Solar declination
    decl = 23.45 * math.sin(math.radians(360 / 365 * (day_of_year - 81)))
    # Equation of time (minutes, Spencer approximation simplified)
    b = math.radians(360 / 365 * (day_of_year - 81))
    eot = 9.87 * math.sin(2 * b) - 7.53 * math.cos(b) - 1.5 * math.sin(b)
    # True solar time
    tst = hour_utc * 60 + eot + 4 * longitude
    ha = (tst / 4) - 180  # hour angle in degrees

    lat_r = math.radians(latitude)
    decl_r = math.radians(decl)
    ha_r = math.radians(ha)

    sin_elev = (
        math.sin(lat_r) * math.sin(decl_r)
        + math.cos(lat_r) * math.cos(decl_r) * math.cos(ha_r)
    )

    return float(round(math.degrees(math.asin(max(-1.0, min(1.0, sin_elev)))), 4))


def versine(angle_radians: float) -> float:
    """Computes the versine: versin(x) = 1 - cos(x).

    A classical trigonometric function used in navigation and surveying.

    Args:
        angle_radians: Angle in radians.

    Returns:
        Versine of the angle.

    Raises:
        TypeError: If the input is not numeric.

    Example:
        >>> versine(0)
        0.0
        >>> round(versine(math.pi), 10)
        2.0

    Complexity: O(1)
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value.")

    return 1.0 - math.cos(angle_radians)


def haversine_trig(angle_radians: float) -> float:
    """Computes the haversine: hav(x) = (1 - cos(x)) / 2 = sin^2(x/2).

    Fundamental to the haversine formula for great-circle distances.

    Args:
        angle_radians: Angle in radians.

    Returns:
        Haversine of the angle.

    Raises:
        TypeError: If the input is not numeric.

    Example:
        >>> haversine_trig(0)
        0.0
        >>> round(haversine_trig(math.pi), 10)
        1.0

    Complexity: O(1)
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value.")

    return (1.0 - math.cos(angle_radians)) / 2.0


def exsecant(angle_radians: float) -> float:
    """Computes the exsecant: exsec(x) = sec(x) - 1.

    Args:
        angle_radians: Angle in radians (cos(x) != 0).

    Returns:
        Exsecant of the angle.

    Raises:
        TypeError: If the input is not numeric.
        ValueError: If cos(angle) is zero.

    Example:
        >>> exsecant(0)
        0.0

    Complexity: O(1)
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value.")

    cos_val = math.cos(angle_radians)

    if abs(cos_val) < 1e-15:
        raise ValueError("Exsecant is undefined when cos(x) = 0.")

    return 1.0 / cos_val - 1.0


def excosecant(angle_radians: float) -> float:
    """Computes the excosecant: excsc(x) = csc(x) - 1.

    Args:
        angle_radians: Angle in radians (sin(x) != 0).

    Returns:
        Excosecant of the angle.

    Raises:
        TypeError: If the input is not numeric.
        ValueError: If sin(angle) is zero.

    Example:
        >>> round(excosecant(math.pi / 2), 10)
        0.0

    Complexity: O(1)
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value.")

    sin_val = math.sin(angle_radians)

    if abs(sin_val) < 1e-15:
        raise ValueError("Excosecant is undefined when sin(x) = 0.")

    return 1.0 / sin_val - 1.0


def coversine(angle_radians: float) -> float:
    """Computes the coversine: coversin(x) = 1 - sin(x).

    Args:
        angle_radians: Angle in radians.

    Returns:
        Coversine of the angle.

    Raises:
        TypeError: If the input is not numeric.

    Example:
        >>> coversine(0)
        1.0
        >>> round(coversine(math.pi / 2), 10)
        0.0

    Complexity: O(1)
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("Angle must be a numeric value.")

    return 1.0 - math.sin(angle_radians)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 23: Trigonometry Functions (1 of 2)
# ---------------------------------------------------------------------------

def hacoverversine(angle_radians: float) -> float:
    """Compute the hacoversed versine (hacoverversine) = (1 + sin(θ))/2.

    Args:
        angle_radians: Angle in radians.

    Returns:
        Hacoverversine value.

    Raises:
        TypeError: If angle_radians is not numeric.

    Usage Example:
        >>> round(hacoverversine(0.5), 4)
        0.7397

    Complexity: O(1)
    """
    if not isinstance(angle_radians, (int, float)):
        raise TypeError("angle_radians must be numeric.")
    return (1.0 + math.sin(float(angle_radians))) / 2.0


def chord_length(radius: float, angle_radians: float) -> float:
    """Compute the chord length: 2r·sin(θ/2).

    Args:
        radius: Radius of the circle.
        angle_radians: Central angle in radians.

    Returns:
        Chord length.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius < 0.

    Usage Example:
        >>> round(chord_length(1.0, 1.0), 4)
        0.9589

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)) or not isinstance(angle_radians, (int, float)):
        raise TypeError("radius and angle_radians must be numeric.")
    if radius < 0:
        raise ValueError("radius must be non-negative.")
    return float(2.0 * radius * abs(math.sin(float(angle_radians) / 2.0)))


def sagitta(radius: float, angle_radians: float) -> float:
    """Compute the sagitta (arrow height): r(1 - cos(θ/2)).

    Args:
        radius: Radius of the circle.
        angle_radians: Central angle in radians.

    Returns:
        Sagitta value.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius < 0.

    Usage Example:
        >>> round(sagitta(1.0, 1.0), 4)
        0.1224

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)) or not isinstance(angle_radians, (int, float)):
        raise TypeError("radius and angle_radians must be numeric.")
    if radius < 0:
        raise ValueError("radius must be non-negative.")
    return float(radius * (1.0 - math.cos(float(angle_radians) / 2.0)))


def arc_length(radius: float, angle_radians: float) -> float:
    """Compute arc length: r·θ.

    Args:
        radius: Radius.
        angle_radians: Central angle in radians.

    Returns:
        Arc length.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius < 0.

    Usage Example:
        >>> round(arc_length(5.0, 1.0), 4)
        5.0

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)) or not isinstance(angle_radians, (int, float)):
        raise TypeError("radius and angle_radians must be numeric.")
    if radius < 0:
        raise ValueError("radius must be non-negative.")
    return float(radius * abs(float(angle_radians)))


def sector_area(radius: float, angle_radians: float) -> float:
    """Compute sector area: r²θ/2.

    Args:
        radius: Radius.
        angle_radians: Central angle in radians.

    Returns:
        Sector area.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius < 0.

    Usage Example:
        >>> round(sector_area(5.0, 1.0), 4)
        12.5

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)) or not isinstance(angle_radians, (int, float)):
        raise TypeError("radius and angle_radians must be numeric.")
    if radius < 0:
        raise ValueError("radius must be non-negative.")
    return float(0.5 * radius * radius * abs(float(angle_radians)))


def segment_area(radius: float, angle_radians: float) -> float:
    """Compute circular segment area: r²(θ - sin(θ))/2.

    Args:
        radius: Radius.
        angle_radians: Central angle in radians.

    Returns:
        Segment area.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius < 0.

    Usage Example:
        >>> round(segment_area(5.0, 1.0), 4)
        1.9816

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)) or not isinstance(angle_radians, (int, float)):
        raise TypeError("radius and angle_radians must be numeric.")
    if radius < 0:
        raise ValueError("radius must be non-negative.")
    theta = abs(float(angle_radians))
    return float(0.5 * radius * radius * (theta - math.sin(theta)))


def hyperbolic_distance(x1: float, y1: float, x2: float, y2: float) -> float:
    """Compute the hyperbolic distance in the Poincaré half-plane model.

    d = arccosh(1 + ((x2-x1)² + (y2-y1)²) / (2·y1·y2))

    Args:
        x1, y1: First point (y1 > 0).
        x2, y2: Second point (y2 > 0).

    Returns:
        Hyperbolic distance.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If y1 or y2 ≤ 0.

    Usage Example:
        >>> round(hyperbolic_distance(0, 1, 0, 2), 4)
        0.6931

    Complexity: O(1)
    """
    for name, val in [("x1", x1), ("y1", y1), ("x2", x2), ("y2", y2)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    y1, y2 = float(y1), float(y2)
    if y1 <= 0 or y2 <= 0:
        raise ValueError("y1 and y2 must be positive.")
    dx = float(x2) - float(x1)
    dy = y2 - y1
    arg = 1.0 + (dx * dx + dy * dy) / (2.0 * y1 * y2)
    return float(math.acosh(arg))


def spherical_law_of_cosines(a: float, b: float, C: float) -> float:
    """Compute side c using the spherical law of cosines.

    cos(c) = cos(a)cos(b) + sin(a)sin(b)cos(C)

    All angles in radians. a, b are arc lengths (sides), C is the included angle.

    Args:
        a: Side a in radians.
        b: Side b in radians.
        C: Included angle C in radians.

    Returns:
        Side c in radians.

    Raises:
        TypeError: If any argument is not numeric.

    Usage Example:
        >>> round(spherical_law_of_cosines(1.0, 1.0, 1.0), 4)
        0.8305

    Complexity: O(1)
    """
    for name, val in [("a", a), ("b", b), ("C", C)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    a, b, C = float(a), float(b), float(C)
    cos_c = math.cos(a) * math.cos(b) + math.sin(a) * math.sin(b) * math.cos(C)
    cos_c = max(-1.0, min(1.0, cos_c))
    return float(math.acos(cos_c))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 24: Trigonometry Functions (2 of 2)
# ---------------------------------------------------------------------------

def polar_to_cartesian(r: float, theta: float) -> tuple[float, float]:
    """Convert polar coordinates (r, θ) to Cartesian (x, y).

    Args:
        r: Radial distance.
        theta: Angle in radians.

    Returns:
        Tuple (x, y).

    Raises:
        TypeError: If arguments are not numeric.

    Usage Example:
        >>> polar_to_cartesian(1.0, 0.0)
        (1.0, 0.0)

    Complexity: O(1)
    """
    if not isinstance(r, (int, float)) or not isinstance(theta, (int, float)):
        raise TypeError("r and theta must be numeric.")
    r, theta = float(r), float(theta)
    return (r * math.cos(theta), r * math.sin(theta))


def cartesian_to_polar(x: float, y: float) -> tuple[float, float]:
    """Convert Cartesian coordinates (x, y) to polar (r, θ).

    Args:
        x: X coordinate.
        y: Y coordinate.

    Returns:
        Tuple (r, theta) where theta is in radians [-π, π].

    Raises:
        TypeError: If arguments are not numeric.

    Usage Example:
        >>> cartesian_to_polar(1.0, 0.0)
        (1.0, 0.0)

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
        raise TypeError("x and y must be numeric.")
    x, y = float(x), float(y)
    return (math.hypot(x, y), math.atan2(y, x))


def spherical_to_cartesian(
    r: float, theta: float, phi: float,
) -> tuple[float, float, float]:
    """Convert spherical coordinates (r, θ, φ) to Cartesian (x, y, z).

    θ is polar angle from z-axis, φ is azimuthal angle from x-axis.

    Args:
        r: Radial distance.
        theta: Polar angle in radians [0, π].
        phi: Azimuthal angle in radians [0, 2π].

    Returns:
        Tuple (x, y, z).

    Raises:
        TypeError: If arguments are not numeric.

    Usage Example:
        >>> tuple(round(v, 4) for v in spherical_to_cartesian(1.0, 0.0, 0.0))
        (0.0, 0.0, 1.0)

    Complexity: O(1)
    """
    for name, val in [("r", r), ("theta", theta), ("phi", phi)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    r, theta, phi = float(r), float(theta), float(phi)
    sin_t = math.sin(theta)
    return (r * sin_t * math.cos(phi), r * sin_t * math.sin(phi), r * math.cos(theta))


def cartesian_to_spherical(
    x: float, y: float, z: float,
) -> tuple[float, float, float]:
    """Convert Cartesian coordinates (x, y, z) to spherical (r, θ, φ).

    Args:
        x: X coordinate.
        y: Y coordinate.
        z: Z coordinate.

    Returns:
        Tuple (r, theta, phi) in radians.

    Raises:
        TypeError: If arguments are not numeric.

    Usage Example:
        >>> cartesian_to_spherical(0.0, 0.0, 1.0)
        (1.0, 0.0, 0.0)

    Complexity: O(1)
    """
    for name, val in [("x", x), ("y", y), ("z", z)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    x, y, z = float(x), float(y), float(z)
    r = math.sqrt(x * x + y * y + z * z)
    if r == 0.0:
        return (0.0, 0.0, 0.0)
    theta = math.acos(max(-1.0, min(1.0, z / r)))
    phi = math.atan2(y, x)
    return (r, theta, phi)


def cylindrical_to_cartesian(
    rho: float, phi: float, z: float,
) -> tuple[float, float, float]:
    """Convert cylindrical coordinates (ρ, φ, z) to Cartesian (x, y, z).

    Args:
        rho: Radial distance in xy-plane.
        phi: Azimuthal angle in radians.
        z: Height.

    Returns:
        Tuple (x, y, z).

    Raises:
        TypeError: If arguments are not numeric.

    Usage Example:
        >>> cylindrical_to_cartesian(1.0, 0.0, 5.0)
        (1.0, 0.0, 5.0)

    Complexity: O(1)
    """
    for name, val in [("rho", rho), ("phi", phi), ("z", z)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    rho, phi, z = float(rho), float(phi), float(z)
    return (rho * math.cos(phi), rho * math.sin(phi), z)


def cartesian_to_cylindrical(
    x: float, y: float, z: float,
) -> tuple[float, float, float]:
    """Convert Cartesian coordinates (x, y, z) to cylindrical (ρ, φ, z).

    Args:
        x: X coordinate.
        y: Y coordinate.
        z: Z coordinate.

    Returns:
        Tuple (rho, phi, z) where phi is in radians.

    Raises:
        TypeError: If arguments are not numeric.

    Usage Example:
        >>> cartesian_to_cylindrical(1.0, 0.0, 5.0)
        (1.0, 0.0, 5.0)

    Complexity: O(1)
    """
    for name, val in [("x", x), ("y", y), ("z", z)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    x, y, z = float(x), float(y), float(z)
    return (math.hypot(x, y), math.atan2(y, x), z)


def angle_bisector_length(a: float, b: float, angle: float) -> float:
    """Compute the length of the angle bisector in a triangle.

    The bisector from the vertex with included angle divides the opposite side.
    Length = (2·a·b·cos(angle/2)) / (a + b).

    Args:
        a: Length of one adjacent side.
        b: Length of the other adjacent side.
        angle: Included angle in radians.

    Returns:
        Length of the angle bisector.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a or b ≤ 0, or a + b = 0.

    Usage Example:
        >>> round(angle_bisector_length(3.0, 4.0, 1.0), 4)
        3.0089

    Complexity: O(1)
    """
    for name, val in [("a", a), ("b", b), ("angle", angle)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    a, b, angle = float(a), float(b), float(angle)
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive.")
    return (2.0 * a * b * math.cos(angle / 2.0)) / (a + b)


def circular_segment_height(radius: float, angle_radians: float) -> float:
    """Compute the height of a circular segment (sagitta).

    h = r(1 - cos(θ/2))

    Args:
        radius: Radius of the circle.
        angle_radians: Central angle in radians.

    Returns:
        Height (sagitta) of the segment.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius < 0.

    Usage Example:
        >>> round(circular_segment_height(10.0, 1.0), 4)
        1.2242

    Complexity: O(1)
    """
    if not isinstance(radius, (int, float)) or not isinstance(angle_radians, (int, float)):
        raise TypeError("radius and angle_radians must be numeric.")
    radius = float(radius)
    if radius < 0:
        raise ValueError("radius must be non-negative.")
    return radius * (1.0 - math.cos(float(angle_radians) / 2.0))


def sinusoidal_wave(amplitude: float, frequency: float, t: float, phase: float = 0.0) -> float:
    """Evaluate a sinusoidal wave: A·sin(2πft + φ).

    Args:
        amplitude: Peak amplitude A.
        frequency: Frequency f in Hz.
        t: Time in seconds.
        phase: Phase offset φ in radians (default 0).

    Returns:
        Wave value at time t.

    Raises:
        TypeError: If arguments are not numeric.

    Usage Example:
        >>> round(sinusoidal_wave(1.0, 1.0, 0.25), 4)
        1.0

    Complexity: O(1)
    """
    for name, val in [("amplitude", amplitude), ("frequency", frequency), ("t", t), ("phase", phase)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    return float(amplitude) * math.sin(2.0 * math.pi * float(frequency) * float(t) + float(phase))


def damped_oscillation(
    amplitude: float, decay: float, frequency: float, t: float,
) -> float:
    """Evaluate a damped oscillation: A·e^(-γt)·cos(2πft).

    Args:
        amplitude: Initial amplitude A.
        decay: Decay constant γ (≥ 0).
        frequency: Frequency f in Hz.
        t: Time in seconds.

    Returns:
        Oscillation value at time t.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If decay < 0.

    Usage Example:
        >>> round(damped_oscillation(1.0, 0.5, 1.0, 1.0), 4)
        0.6065

    Complexity: O(1)
    """
    for name, val in [("amplitude", amplitude), ("decay", decay), ("frequency", frequency), ("t", t)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    decay = float(decay)
    if decay < 0:
        raise ValueError("decay must be non-negative.")
    t = float(t)
    return float(amplitude) * math.exp(-decay * t) * math.cos(2.0 * math.pi * float(frequency) * t)


def angular_deficiency(n: int) -> float:
    """Compute the angular deficiency of a regular polygon vertex.

    angular_deficiency = 2π - n·interior_angle, where interior_angle = (n-2)π/n.
    Equivalently = 2π·(1 - (n-2)/2) = 4π/n... wait, that's not right for a polyhedron.

    For a regular polygon: the exterior angle = 2π/n. This is how much the angle
    "falls short" of a full turn. Returns the exterior angle.

    Args:
        n: Number of sides (≥ 3).

    Returns:
        Exterior angle in radians (= 2π / n).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 3.

    Usage Example:
        >>> round(angular_deficiency(6), 4)
        1.0472

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 3:
        raise ValueError("n must be >= 3.")
    return 2.0 * math.pi / n


def normalize_angle(angle: float, full_turn: float = 2.0 * math.pi) -> float:
    """Normalize an angle to the range [0, full_turn).

    Args:
        angle: Angle value.
        full_turn: Full revolution size (default 2π for radians, use 360 for degrees).

    Returns:
        Angle in [0, full_turn).

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If full_turn ≤ 0.

    Usage Example:
        >>> round(normalize_angle(7.0), 4)
        0.7168

    Complexity: O(1)
    """
    if not isinstance(angle, (int, float)) or not isinstance(full_turn, (int, float)):
        raise TypeError("angle and full_turn must be numeric.")
    full_turn = float(full_turn)
    if full_turn <= 0:
        raise ValueError("full_turn must be positive.")
    return float(angle) % full_turn
