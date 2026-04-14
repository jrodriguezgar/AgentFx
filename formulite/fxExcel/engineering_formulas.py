"""
FormuLite - fxExcel: Engineering Functions Module

This module provides Excel-compatible engineering functions for FormuLite.
It includes functions for:
- Bessel functions (BESSELI, BESSELJ, BESSELK, BESSELY)
- Number base conversions (binary, decimal, hexadecimal, octal)
- Bitwise operations (shifts, AND, OR, XOR)
- Complex number operations
- Error functions
- Unit conversions

All functions follow Excel's naming conventions and behavior.
"""

import cmath
from typing import Union


from formulite.fxNumeric.arithmetic_functions import (
    bessel_i as _core_bessel_i,
    bessel_j as _core_bessel_j,
    bessel_k as _core_bessel_k,
    bessel_y as _core_bessel_y,
    bit_lshift as _core_bit_lshift,
    bit_rshift as _core_bit_rshift,
    bitwise_and as _core_bitwise_and,
    bitwise_or as _core_bitwise_or,
    bitwise_xor as _core_bitwise_xor,
    complementary_error_function as _core_erfc,
    delta as _core_delta,
    error_function as _core_erf,
    gestep as _core_gestep,
)
from formulite.fxNumeric.conversion_functions import (
    convert_units as _core_convert_units,
)


# ========== BESSEL FUNCTIONS ==========

def BESSELI(n: Union[int, float], x: Union[int, float]) -> float:
    """
    Returns the modified Bessel function In(x).

    Args:
        n (Union[int, float]): Order of the Bessel function.
        x (Union[int, float]): Value at which to evaluate the function.

    Returns:
        float: The modified Bessel function In(x).

    Raises:
        ValueError: If the computation fails.

    Example:
        >>> BESSELI(1, 1.5)
        0.981666428

    **Cost:** O(1), Bessel function computation.
    """
    return float(_core_bessel_i(x, n))


def BESSELJ(n: Union[int, float], x: Union[int, float]) -> float:
    """
    Returns the Bessel function Jn(x).

    Args:
        n (Union[int, float]): Order of the Bessel function.
        x (Union[int, float]): Value at which to evaluate the function.

    Returns:
        float: The Bessel function Jn(x).

    Raises:
        ValueError: If the computation fails.

    Example:
        >>> BESSELJ(1, 1.5)
        0.557936507

    **Cost:** O(1), Bessel function computation.
    """
    return float(_core_bessel_j(x, n))


def BESSELK(n: Union[int, float], x: Union[int, float]) -> float:
    """
    Returns the modified Bessel function Kn(x).

    Args:
        n (Union[int, float]): Order of the Bessel function.
        x (Union[int, float]): Value at which to evaluate the function. Must be positive.

    Returns:
        float: The modified Bessel function Kn(x).

    Raises:
        ValueError: If x is not positive or computation fails.

    Example:
        >>> BESSELK(1, 1.5)
        0.277387804

    **Cost:** O(1), Bessel function computation.
    """
    if x <= 0:
        raise ValueError("x must be positive for BESSELK")

    return float(_core_bessel_k(x, n))


def BESSELY(n: Union[int, float], x: Union[int, float]) -> float:
    """
    Returns the Bessel function Yn(x).

    Args:
        n (Union[int, float]): Order of the Bessel function.
        x (Union[int, float]): Value at which to evaluate the function. Must be positive.

    Returns:
        float: The Bessel function Yn(x).

    Raises:
        ValueError: If x is not positive or computation fails.

    Example:
        >>> BESSELY(1, 1.5)
        -0.412308627

    **Cost:** O(1), Bessel function computation.
    """
    if x <= 0:
        raise ValueError("x must be positive for BESSELY")

    return float(_core_bessel_y(x, n))


# ========== BITWISE OPERATIONS ==========

def BITRSHIFT(number: int, shift: int) -> int:
    """
    Performs a right shift on a number by shift bits.

    Args:
        number (int): Number to shift.
        shift (int): Number of bits to shift right.

    Returns:
        int: Result of right shift operation.

    Raises:
        ValueError: If arguments are not integers.

    Example:
        >>> BITRSHIFT(8, 2)
        2

    **Cost:** O(1), bitwise operation.
    """
    return _core_bit_rshift(number, shift)


def BITLSHIFT(number: int, shift: int) -> int:
    """
    Performs a left shift on a number by shift bits.

    Args:
        number (int): Number to shift.
        shift (int): Number of bits to shift left.

    Returns:
        int: Result of left shift operation.

    Raises:
        ValueError: If arguments are not integers.

    Example:
        >>> BITLSHIFT(2, 2)
        8

    **Cost:** O(1), bitwise operation.
    """
    return _core_bit_lshift(number, shift)


def BITOR(number1: int, number2: int) -> int:
    """
    Performs a bitwise OR on two numbers.

    Args:
        number1 (int): First number.
        number2 (int): Second number.

    Returns:
        int: Result of bitwise OR.

    Raises:
        ValueError: If arguments are not integers.

    Example:
        >>> BITOR(5, 3)
        7

    **Cost:** O(1), bitwise operation.
    """
    return _core_bitwise_or(number1, number2)


def BITXOR(number1: int, number2: int) -> int:
    """
    Performs a bitwise XOR on two numbers.

    Args:
        number1 (int): First number.
        number2 (int): Second number.

    Returns:
        int: Result of bitwise XOR.

    Raises:
        ValueError: If arguments are not integers.

    Example:
        >>> BITXOR(5, 3)
        6

    **Cost:** O(1), bitwise operation.
    """
    return _core_bitwise_xor(number1, number2)


def BITAND(number1: int, number2: int) -> int:
    """
    Performs a bitwise AND on two numbers.

    Args:
        number1 (int): First number.
        number2 (int): Second number.

    Returns:
        int: Result of bitwise AND.

    Raises:
        ValueError: If arguments are not integers.

    Example:
        >>> BITAND(5, 3)
        1

    **Cost:** O(1), bitwise operation.
    """
    return _core_bitwise_and(number1, number2)


# ========== COMPLEX NUMBER OPERATIONS ==========

def COMPLEX(real: Union[int, float], imag: Union[int, float], suffix: str = "i") -> complex:
    """
    Creates a complex number from real and imaginary coefficients.

    Args:
        real (Union[int, float]): Real coefficient.
        imag (Union[int, float]): Imaginary coefficient.
        suffix (str): Suffix character ("i" or "j"). Defaults to "i".

    Returns:
        complex: Complex number.

    Raises:
        ValueError: If creation fails.

    Example:
        >>> COMPLEX(3, 4)
        (3+4j)

    **Cost:** O(1), complex number creation.
    """
    try:
        return complex(real, imag)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error creating complex number: {e}")


def IMABS(complex_num: complex) -> float:
    """
    Returns the absolute value (modulus) of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        float: Absolute value.

    Example:
        >>> IMABS(3+4j)
        5.0

    **Cost:** O(1), modulus calculation.
    """
    try:
        return abs(complex_num)
    except TypeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMARGUMENT(complex_num: complex) -> float:
    """
    Returns the argument (angle in radians) of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        float: Argument in radians.

    Example:
        >>> round(IMARGUMENT(3+4j), 4)
        0.9273

    **Cost:** O(1), phase calculation.
    """
    try:
        return cmath.phase(complex_num)
    except TypeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMCONJUGATE(complex_num: complex) -> complex:
    """
    Returns the complex conjugate of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Complex conjugate.

    Example:
        >>> IMCONJUGATE(3+4j)
        (3-4j)

    **Cost:** O(1), conjugate operation.
    """
    try:
        return complex_num.conjugate()
    except AttributeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMCOS(complex_num: complex) -> complex:
    """
    Returns the cosine of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Cosine of the complex number.

    Example:
        >>> IMCOS(1+1j)
        (0.8337300251311491-0.9888977057628651j)

    **Cost:** O(1), complex cosine.
    """
    try:
        return cmath.cos(complex_num)
    except TypeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMCOSH(complex_num: complex) -> complex:
    """
    Returns the hyperbolic cosine of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Hyperbolic cosine.

    Example:
        >>> IMCOSH(1+1j)
        (0.8337300251311491+0.9888977057628651j)

    **Cost:** O(1), complex hyperbolic cosine.
    """
    try:
        return cmath.cosh(complex_num)
    except TypeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMCOT(complex_num: complex) -> complex:
    """
    Returns the cotangent of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Cotangent.

    Example:
        >>> IMCOT(1+1j)
        (0.21762156185440268-0.8680141428959249j)

    **Cost:** O(1), complex cotangent.
    """
    try:
        return 1 / cmath.tan(complex_num)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Error computing IMCOT: {e}")


def IMCSC(complex_num: complex) -> complex:
    """
    Returns the cosecant of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Cosecant.

    Example:
        >>> IMCSC(1+1j)
        (0.6215180171704284-0.30393100162842646j)

    **Cost:** O(1), complex cosecant.
    """
    try:
        return 1 / cmath.sin(complex_num)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Error computing IMCSC: {e}")


def IMCSCH(complex_num: complex) -> complex:
    """
    Returns the hyperbolic cosecant of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Hyperbolic cosecant.

    Example:
        >>> IMCSCH(1+1j)
        (0.30393100162842646-0.6215180171704284j)

    **Cost:** O(1), complex hyperbolic cosecant.
    """
    try:
        return 1 / cmath.sinh(complex_num)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Error computing IMCSCH: {e}")


def IMEXP(complex_num: complex) -> complex:
    """
    Returns the exponential of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: e^(complex_num).

    Example:
        >>> IMEXP(1+1j)
        (1.4686939399158851+2.2873552871788423j)

    **Cost:** O(1), complex exponential.
    """
    try:
        return cmath.exp(complex_num)
    except TypeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMLN(complex_num: complex) -> complex:
    """
    Returns the natural logarithm of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Natural logarithm.

    Example:
        >>> IMLN(3+4j)
        (1.6094379124341003+0.9272952180016122j)

    **Cost:** O(1), complex logarithm.
    """
    try:
        return cmath.log(complex_num)
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error computing IMLN: {e}")


def IMPOWER(complex_num: complex, n: Union[int, float]) -> complex:
    """
    Returns a complex number raised to a power.

    Args:
        complex_num (complex): Complex number base.
        n (Union[int, float]): Exponent.

    Returns:
        complex: Result of complex_num^n.

    Example:
        >>> IMPOWER(2+3j, 2)
        (-5+12j)

    **Cost:** O(1), complex exponentiation.
    """
    try:
        return complex_num ** n
    except (TypeError, ValueError) as e:
        raise ValueError(f"Error computing IMPOWER: {e}")


def IMPRODUCT(*complex_nums: complex) -> complex:
    """
    Returns the product of complex numbers.

    Args:
        *complex_nums (complex): Variable number of complex numbers.

    Returns:
        complex: Product of all complex numbers.

    Example:
        >>> IMPRODUCT(2+3j, 1+2j)
        (-4+7j)

    **Cost:** O(n), where n is the number of arguments.
    """
    try:
        result = 1
        for num in complex_nums:
            result *= num
        return result
    except TypeError:
        raise ValueError("All arguments must be complex numbers")


def IMREAL(complex_num: complex) -> float:
    """
    Returns the real part of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        float: Real part.

    Example:
        >>> IMREAL(3+4j)
        3.0

    **Cost:** O(1), real part extraction.
    """
    try:
        return complex_num.real
    except AttributeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMSQRT(complex_num: complex) -> complex:
    """
    Returns the square root of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Square root.

    Example:
        >>> IMSQRT(-1)
        1j

    **Cost:** O(1), complex square root.
    """
    try:
        return cmath.sqrt(complex_num)
    except TypeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMSEC(complex_num: complex) -> complex:
    """
    Returns the secant of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Secant.

    Example:
        >>> IMSEC(1+1j)
        (0.4983370305551868+0.591083841721045j)

    **Cost:** O(1), complex secant.
    """
    try:
        return 1 / cmath.cos(complex_num)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Error computing IMSEC: {e}")


def IMSECH(complex_num: complex) -> complex:
    """
    Returns the hyperbolic secant of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Hyperbolic secant.

    Example:
        >>> IMSECH(1+1j)
        (0.4983370305551868-0.591083841721045j)

    **Cost:** O(1), complex hyperbolic secant.
    """
    try:
        return 1 / cmath.cosh(complex_num)
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Error computing IMSECH: {e}")


def IMSIN(complex_num: complex) -> complex:
    """
    Returns the sine of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Sine.

    Example:
        >>> IMSIN(1+1j)
        (1.2984575814159773+0.6349639147847361j)

    **Cost:** O(1), complex sine.
    """
    try:
        return cmath.sin(complex_num)
    except TypeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMSINH(complex_num: complex) -> complex:
    """
    Returns the hyperbolic sine of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Hyperbolic sine.

    Example:
        >>> IMSINH(1+1j)
        (0.6349639147847361+1.2984575814159773j)

    **Cost:** O(1), complex hyperbolic sine.
    """
    try:
        return cmath.sinh(complex_num)
    except TypeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMSUM(*complex_nums: complex) -> complex:
    """
    Returns the sum of complex numbers.

    Args:
        *complex_nums (complex): Variable number of complex numbers.

    Returns:
        complex: Sum of all complex numbers.

    Example:
        >>> IMSUM(2+3j, 1+2j, 3+4j)
        (6+9j)

    **Cost:** O(n), where n is the number of arguments.
    """
    try:
        return sum(complex_nums)
    except TypeError:
        raise ValueError("All arguments must be complex numbers")


def IMSUB(complex_num1: complex, complex_num2: complex) -> complex:
    """
    Returns the difference between two complex numbers.

    Args:
        complex_num1 (complex): First complex number.
        complex_num2 (complex): Second complex number.

    Returns:
        complex: Difference complex_num1 - complex_num2.

    Example:
        >>> IMSUB(5+6j, 2+3j)
        (3+3j)

    **Cost:** O(1), complex subtraction.
    """
    try:
        return complex_num1 - complex_num2
    except TypeError:
        raise ValueError("Both arguments must be complex numbers")


def IMTAN(complex_num: complex) -> complex:
    """
    Returns the tangent of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Tangent.

    Example:
        >>> IMTAN(1+1j)
        (0.27175258531951174+1.0839233273386948j)

    **Cost:** O(1), complex tangent.
    """
    try:
        return cmath.tan(complex_num)
    except TypeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMAGINARY(complex_num: complex) -> float:
    """
    Returns the imaginary part of a complex number.

    Args:
        complex_num (complex): Complex number.

    Returns:
        float: Imaginary part.

    Example:
        >>> IMAGINARY(3+4j)
        4.0

    **Cost:** O(1), imaginary part extraction.
    """
    try:
        return complex_num.imag
    except AttributeError:
        raise ValueError(f"Invalid complex number: {complex_num}")


def IMDIV(complex_num1: complex, complex_num2: complex) -> complex:
    """
    Returns the quotient of two complex numbers.

    Args:
        complex_num1 (complex): Numerator.
        complex_num2 (complex): Denominator.

    Returns:
        complex: Quotient complex_num1 / complex_num2.

    Example:
        >>> IMDIV(6+8j, 2+0j)
        (3+4j)

    **Cost:** O(1), complex division.
    """
    try:
        return complex_num1 / complex_num2
    except (TypeError, ZeroDivisionError) as e:
        raise ValueError(f"Error computing IMDIV: {e}")


# ========== ERROR FUNCTIONS ==========

def ERF(x: Union[int, float]) -> float:
    """
    Returns the error function erf(x).

    Args:
        x (Union[int, float]): Value at which to evaluate.

    Returns:
        float: Error function value.

    Example:
        >>> round(ERF(1), 5)
        0.84270

    **Cost:** O(1), error function computation.
    """
    return float(_core_erf(x))


def ERFC(x: Union[int, float]) -> float:
    """
    Returns the complementary error function erfc(x).

    Args:
        x (Union[int, float]): Value at which to evaluate.

    Returns:
        float: Complementary error function value.

    Example:
        >>> round(ERFC(1), 5)
        0.15730

    **Cost:** O(1), complementary error function computation.
    """
    return float(_core_erfc(x))


def ERF_PRECISE(x: Union[int, float]) -> float:
    """
    Returns the error function erf(x) with precise calculation.

    Args:
        x (Union[int, float]): Value at which to evaluate.

    Returns:
        float: Error function value.

    Example:
        >>> round(ERF_PRECISE(1), 5)
        0.84270

    **Cost:** O(1), error function computation.
    """
    return ERF(x)


def ERFC_PRECISE(x: Union[int, float]) -> float:
    """
    Returns the complementary error function erfc(x) with precise calculation.

    Args:
        x (Union[int, float]): Value at which to evaluate.

    Returns:
        float: Complementary error function value.

    Example:
        >>> round(ERFC_PRECISE(1), 5)
        0.15730

    **Cost:** O(1), complementary error function computation.
    """
    return ERFC(x)


# ========== OTHER FUNCTIONS ==========

def DELTA(value1: Union[int, float], value2: Union[int, float] = 0) -> int:
    """
    Tests whether two values are equal. Returns 1 if equal, 0 otherwise.

    Args:
        value1 (Union[int, float]): First value.
        value2 (Union[int, float]): Second value. Defaults to 0.

    Returns:
        int: 1 if value1 == value2, 0 otherwise.

    Example:
        >>> DELTA(5, 5)
        1
        >>> DELTA(5, 3)
        0

    **Cost:** O(1), equality comparison.
    """
    return _core_delta(value1, value2)


def GESTEP(number: Union[int, float], threshold: Union[int, float] = 0) -> int:
    """
    Tests whether a number is greater than or equal to a threshold.
    Returns 1 if number >= threshold, 0 otherwise.

    Args:
        number (Union[int, float]): Number to test.
        threshold (Union[int, float]): Threshold value. Defaults to 0.

    Returns:
        int: 1 if number >= threshold, 0 otherwise.

    Example:
        >>> GESTEP(5, 3)
        1
        >>> GESTEP(2, 3)
        0

    **Cost:** O(1), comparison operation.
    """
    return _core_gestep(number, threshold)


def CONVERT(number: Union[int, float], from_unit: str, to_unit: str) -> float:
    """
    Converts a number from one measurement unit to another.

    Args:
        number (Union[int, float]): Value to convert.
        from_unit (str): Source unit.
        to_unit (str): Target unit.

    Returns:
        float: Converted value.

    Raises:
        ValueError: If conversion is not supported.

    Example:
        >>> CONVERT(100, 'cm', 'm')
        1.0
        >>> CONVERT(1, 'kg', 'g')
        1000.0

    **Cost:** O(1), unit conversion lookup.
    """
    return float(_core_convert_units(number, from_unit, to_unit))


# ========== BASE CONVERSION FUNCTIONS ==========

def BIN2DEC(binary: str) -> int:
    """
    Converts a binary string to decimal.
    Excel function: BIN2DEC (Spanish: BIN.A.DEC)

    Args:
        binary (str): Binary string (up to 10 characters).

    Returns:
        int: Decimal equivalent.

    Raises:
        ValueError: If binary string is invalid or too long.

    Example:
        >>> BIN2DEC('1010')
        10
        >>> BIN2DEC('11111111')
        255

    **Cost:** O(n) where n is the length of binary string.
    """
    if not isinstance(binary, str):
        raise ValueError("Binary input must be a string")
    if len(binary) > 10:
        raise ValueError("Binary string must be 10 characters or less")
    if not all(c in '01' for c in binary):
        raise ValueError("Invalid binary string")
    
    # Handle two's complement for negative numbers (first bit is sign)
    if len(binary) == 10 and binary[0] == '1':
        # Negative number in two's complement
        return int(binary, 2) - 1024
    return int(binary, 2)


def BIN2HEX(binary: str, places: int = None) -> str:
    """
    Converts a binary string to hexadecimal.
    Excel function: BIN2HEX (Spanish: BIN.A.HEX)

    Args:
        binary (str): Binary string (up to 10 characters).
        places (int, optional): Number of characters to use. If None, uses minimum needed.

    Returns:
        str: Hexadecimal equivalent.

    Raises:
        ValueError: If binary string is invalid.

    Example:
        >>> BIN2HEX('1010')
        'A'
        >>> BIN2HEX('1010', 4)
        '000A'

    **Cost:** O(n) where n is the length of binary string.
    """
    decimal = BIN2DEC(binary)
    if decimal < 0:
        # For negative numbers, use two's complement representation
        hex_value = hex(decimal & 0x3FF)[2:].upper()
    else:
        hex_value = hex(decimal)[2:].upper()
    
    if places is not None:
        if len(hex_value) > places:
            raise ValueError("Result exceeds specified places")
        hex_value = hex_value.zfill(places)
    
    return hex_value


def BIN2OCT(binary: str, places: int = None) -> str:
    """
    Converts a binary string to octal.
    Excel function: BIN2OCT (Spanish: BIN.A.OCT)

    Args:
        binary (str): Binary string (up to 10 characters).
        places (int, optional): Number of characters to use. If None, uses minimum needed.

    Returns:
        str: Octal equivalent.

    Raises:
        ValueError: If binary string is invalid.

    Example:
        >>> BIN2OCT('1010')
        '12'
        >>> BIN2OCT('1010', 4)
        '0012'

    **Cost:** O(n) where n is the length of binary string.
    """
    decimal = BIN2DEC(binary)
    if decimal < 0:
        # For negative numbers, use two's complement representation
        oct_value = oct(decimal & 0x3FF)[2:]
    else:
        oct_value = oct(decimal)[2:]
    
    if places is not None:
        if len(oct_value) > places:
            raise ValueError("Result exceeds specified places")
        oct_value = oct_value.zfill(places)
    
    return oct_value


def DEC2BIN(decimal: int, places: int = None) -> str:
    """
    Converts a decimal number to binary.
    Excel function: DEC2BIN (Spanish: BDCONTAR - error in original file, should be DEC.A.BIN)

    Args:
        decimal (int): Decimal number (must be between -512 and 511).
        places (int, optional): Number of characters to use. If None, uses minimum needed.

    Returns:
        str: Binary equivalent.

    Raises:
        ValueError: If decimal is out of range.

    Example:
        >>> DEC2BIN(10)
        '1010'
        >>> DEC2BIN(10, 8)
        '00001010'

    **Cost:** O(log n) where n is the decimal value.
    """
    if not isinstance(decimal, (int, float)):
        raise ValueError("Decimal input must be a number")
    
    decimal = int(decimal)
    if decimal < -512 or decimal > 511:
        raise ValueError("Decimal must be between -512 and 511")
    
    if decimal < 0:
        # Two's complement for negative numbers (10 bits)
        binary = bin(decimal & 0x3FF)[2:]
    else:
        binary = bin(decimal)[2:]
    
    if places is not None:
        if len(binary) > places:
            raise ValueError("Result exceeds specified places")
        binary = binary.zfill(places)
    
    return binary


def DEC2HEX(decimal: int, places: int = None) -> str:
    """
    Converts a decimal number to hexadecimal.
    Excel function: DEC2HEX (Spanish: DEC.A.HEX)

    Args:
        decimal (int): Decimal number.
        places (int, optional): Number of characters to use. If None, uses minimum needed.

    Returns:
        str: Hexadecimal equivalent.

    Raises:
        ValueError: If decimal is out of range.

    Example:
        >>> DEC2HEX(100)
        '64'
        >>> DEC2HEX(100, 4)
        '0064'

    **Cost:** O(log n) where n is the decimal value.
    """
    if not isinstance(decimal, (int, float)):
        raise ValueError("Decimal input must be a number")
    
    decimal = int(decimal)
    if decimal < -549755813888 or decimal > 549755813887:
        raise ValueError("Decimal out of valid range")
    
    if decimal < 0:
        # Two's complement for negative numbers
        hex_value = hex(decimal & 0xFFFFFFFFFF)[2:].upper()
    else:
        hex_value = hex(decimal)[2:].upper()
    
    if places is not None:
        if len(hex_value) > places:
            raise ValueError("Result exceeds specified places")
        hex_value = hex_value.zfill(places)
    
    return hex_value


def DEC2OCT(decimal: int, places: int = None) -> str:
    """
    Converts a decimal number to octal.
    Excel function: DEC2OCT (Spanish: DEC.A.OCT)

    Args:
        decimal (int): Decimal number (must be between -536870912 and 536870911).
        places (int, optional): Number of characters to use. If None, uses minimum needed.

    Returns:
        str: Octal equivalent.

    Raises:
        ValueError: If decimal is out of range.

    Example:
        >>> DEC2OCT(100)
        '144'
        >>> DEC2OCT(100, 5)
        '00144'

    **Cost:** O(log n) where n is the decimal value.
    """
    if not isinstance(decimal, (int, float)):
        raise ValueError("Decimal input must be a number")
    
    decimal = int(decimal)
    if decimal < -536870912 or decimal > 536870911:
        raise ValueError("Decimal must be between -536870912 and 536870911")
    
    if decimal < 0:
        # Two's complement for negative numbers
        oct_value = oct(decimal & 0x3FFFFFFF)[2:]
    else:
        oct_value = oct(decimal)[2:]
    
    if places is not None:
        if len(oct_value) > places:
            raise ValueError("Result exceeds specified places")
        oct_value = oct_value.zfill(places)
    
    return oct_value


def HEX2BIN(hexadecimal: str, places: int = None) -> str:
    """
    Converts a hexadecimal string to binary.
    Excel function: HEX2BIN (Spanish: HEX.A.BIN)

    Args:
        hexadecimal (str): Hexadecimal string (up to 10 characters).
        places (int, optional): Number of characters to use. If None, uses minimum needed.

    Returns:
        str: Binary equivalent.

    Raises:
        ValueError: If hexadecimal string is invalid.

    Example:
        >>> HEX2BIN('A')
        '1010'
        >>> HEX2BIN('F', 8)
        '00001111'

    **Cost:** O(n) where n is the length of hexadecimal string.
    """
    if not isinstance(hexadecimal, str):
        raise ValueError("Hexadecimal input must be a string")
    if len(hexadecimal) > 10:
        raise ValueError("Hexadecimal string must be 10 characters or less")
    
    try:
        decimal = int(hexadecimal, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal string")
    
    # Convert to binary (handle two's complement for large values)
    if decimal >= 512:
        # Treat as negative in 10-bit two's complement
        decimal = decimal - 1024
    
    if decimal < -512 or decimal > 511:
        raise ValueError("Result out of valid binary range")
    
    if decimal < 0:
        binary = bin(decimal & 0x3FF)[2:]
    else:
        binary = bin(decimal)[2:]
    
    if places is not None:
        if len(binary) > places:
            raise ValueError("Result exceeds specified places")
        binary = binary.zfill(places)
    
    return binary


def HEX2DEC(hexadecimal: str) -> int:
    """
    Converts a hexadecimal string to decimal.
    Excel function: HEX2DEC (Spanish: HEX.A.DEC)

    Args:
        hexadecimal (str): Hexadecimal string (up to 10 characters).

    Returns:
        int: Decimal equivalent.

    Raises:
        ValueError: If hexadecimal string is invalid.

    Example:
        >>> HEX2DEC('A')
        10
        >>> HEX2DEC('FF')
        255

    **Cost:** O(n) where n is the length of hexadecimal string.
    """
    if not isinstance(hexadecimal, str):
        raise ValueError("Hexadecimal input must be a string")
    if len(hexadecimal) > 10:
        raise ValueError("Hexadecimal string must be 10 characters or less")
    
    try:
        decimal = int(hexadecimal, 16)
    except ValueError:
        raise ValueError("Invalid hexadecimal string")
    
    # Handle two's complement for large values (40 bits)
    if decimal >= 0x8000000000:
        decimal = decimal - 0x10000000000
    
    return decimal


def HEX2OCT(hexadecimal: str, places: int = None) -> str:
    """
    Converts a hexadecimal string to octal.
    Excel function: HEX2OCT (Spanish: HEX.A.OCT)

    Args:
        hexadecimal (str): Hexadecimal string.
        places (int, optional): Number of characters to use. If None, uses minimum needed.

    Returns:
        str: Octal equivalent.

    Raises:
        ValueError: If hexadecimal string is invalid.

    Example:
        >>> HEX2OCT('F')
        '17'
        >>> HEX2OCT('A', 4)
        '0012'

    **Cost:** O(n) where n is the length of hexadecimal string.
    """
    decimal = HEX2DEC(hexadecimal)
    
    # Convert to octal with proper range for Excel compatibility
    if decimal < -536870912 or decimal > 536870911:
        raise ValueError("Result out of valid octal range")
    
    if decimal < 0:
        oct_value = oct(decimal & 0x3FFFFFFF)[2:]
    else:
        oct_value = oct(decimal)[2:]
    
    if places is not None:
        if len(oct_value) > places:
            raise ValueError("Result exceeds specified places")
        oct_value = oct_value.zfill(places)
    
    return oct_value


def OCT2BIN(octal: str, places: int = None) -> str:
    """
    Converts an octal string to binary.
    Excel function: OCT2BIN (Spanish: OCT.A.BIN)

    Args:
        octal (str): Octal string (up to 10 characters).
        places (int, optional): Number of characters to use. If None, uses minimum needed.

    Returns:
        str: Binary equivalent.

    Raises:
        ValueError: If octal string is invalid.

    Example:
        >>> OCT2BIN('12')
        '1010'
        >>> OCT2BIN('7', 4)
        '0111'

    **Cost:** O(n) where n is the length of octal string.
    """
    if not isinstance(octal, str):
        raise ValueError("Octal input must be a string")
    if len(octal) > 10:
        raise ValueError("Octal string must be 10 characters or less")
    
    try:
        decimal = int(octal, 8)
    except ValueError:
        raise ValueError("Invalid octal string")
    
    # Handle two's complement
    if decimal >= 512:
        decimal = decimal - 1024
    
    if decimal < -512 or decimal > 511:
        raise ValueError("Result out of valid binary range")
    
    if decimal < 0:
        binary = bin(decimal & 0x3FF)[2:]
    else:
        binary = bin(decimal)[2:]
    
    if places is not None:
        if len(binary) > places:
            raise ValueError("Result exceeds specified places")
        binary = binary.zfill(places)
    
    return binary


def OCT2DEC(octal: str) -> int:
    """
    Converts an octal string to decimal.
    Excel function: OCT2DEC (Spanish: OCT.A.DEC)

    Args:
        octal (str): Octal string (up to 10 characters).

    Returns:
        int: Decimal equivalent.

    Raises:
        ValueError: If octal string is invalid.

    Example:
        >>> OCT2DEC('12')
        10
        >>> OCT2DEC('144')
        100

    **Cost:** O(n) where n is the length of octal string.
    """
    if not isinstance(octal, str):
        raise ValueError("Octal input must be a string")
    if len(octal) > 10:
        raise ValueError("Octal string must be 10 characters or less")
    
    try:
        decimal = int(octal, 8)
    except ValueError:
        raise ValueError("Invalid octal string")
    
    # Handle two's complement for large values (30 bits)
    if decimal >= 0x20000000:
        decimal = decimal - 0x40000000
    
    return decimal


def OCT2HEX(octal: str, places: int = None) -> str:
    """
    Converts an octal string to hexadecimal.
    Excel function: OCT2HEX (Spanish: OCT.A.HEX)

    Args:
        octal (str): Octal string.
        places (int, optional): Number of characters to use. If None, uses minimum needed.

    Returns:
        str: Hexadecimal equivalent.

    Raises:
        ValueError: If octal string is invalid.

    Example:
        >>> OCT2HEX('12')
        'A'
        >>> OCT2HEX('144', 4)
        '0064'

    **Cost:** O(n) where n is the length of octal string.
    """
    decimal = OCT2DEC(octal)
    
    if decimal < 0:
        hex_value = hex(decimal & 0xFFFFFFFFFF)[2:].upper()
    else:
        hex_value = hex(decimal)[2:].upper()
    
    if places is not None:
        if len(hex_value) > places:
            raise ValueError("Result exceeds specified places")
        hex_value = hex_value.zfill(places)
    
    return hex_value


def IMLOG10(complex_num: complex) -> complex:
    """
    Returns the common logarithm (base 10) of a complex number.
    Excel function: IMLOG10 (Spanish: IM.LOG10)

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Common logarithm of the complex number.

    Raises:
        ValueError: If input is invalid.

    Example:
        >>> z = 3 + 4j
        >>> result = IMLOG10(z)
        >>> round(result.real, 5), round(result.imag, 5)
        (0.69897, 0.42785)

    **Cost:** O(1), logarithm computation.
    """
    if not isinstance(complex_num, complex):
        raise ValueError("Input must be a complex number")
    try:
        return cmath.log10(complex_num)
    except (ValueError, ZeroDivisionError) as e:
        raise ValueError(f"Error computing IMLOG10: {e}")


def IMLOG2(complex_num: complex) -> complex:
    """
    Returns the base-2 logarithm of a complex number.
    Excel function: IMLOG2 (Spanish: IM.LOG2)

    Args:
        complex_num (complex): Complex number.

    Returns:
        complex: Base-2 logarithm of the complex number.

    Raises:
        ValueError: If input is invalid.

    Example:
        >>> z = 4 + 0j
        >>> result = IMLOG2(z)
        >>> round(result.real, 5)
        2.0

    **Cost:** O(1), logarithm computation.
    """
    if not isinstance(complex_num, complex):
        raise ValueError("Input must be a complex number")
    try:
        return cmath.log(complex_num) / cmath.log(2)
    except (ValueError, ZeroDivisionError) as e:
        raise ValueError(f"Error computing IMLOG2: {e}")

