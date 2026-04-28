"""Numeric Conversions Module.

This module provides comprehensive functionality for numeric type conversions,
including conversions between numeric types, string representations, different
number bases, and specialized conversions for JavaScript interoperability.

Key Features:
    - Basic type conversions (int, float, bool, complex, string)
    - Number base conversions (binary, hexadecimal, octal)
    - Timestamp and datetime conversions
    - Locale-aware string to number conversions
    - JavaScript safe integer handling
    - IEEE 754 and bytes conversions

Example:
    >>> from shortfx.fxNumeric.conversion_functions import hex_to_int, float_to_int_truncated
    >>> hex_to_int("0xFF")
    255
    >>> float_to_int_truncated(3.9)
    3
"""
import json
import math
from decimal import Decimal
import locale
from typing import Any, Union, Optional

# JavaScript's safe integer limit
JS_MAX_SAFE_INTEGER = 2**53 - 1
JS_MIN_SAFE_INTEGER = -(2**53 - 1)


def float_to_int_truncated(number: float) -> int:
    """
    Converts a float to an integer by truncating the decimal part (towards zero).

    Args:
        number (float): The float number to convert.

    Returns:
        int: The resulting integer without the decimal part.

    Example:
        >>> float_to_int_truncated(3.9)
        3
        >>> float_to_int_truncated(-3.9)
        -3
        >>> float_to_int_truncated(5.0)
        5

    **Cost:** O(1), direct type conversion via truncation.
    """
    return int(number)


def int_to_float(number: int) -> float:
    """
    Converts an integer to a floating-point number.

    Args:
        number (int): The integer number to convert.

    Returns:
        float: The resulting float number.

    Example:
        >>> int_to_float(5)
        5.0
        >>> int_to_float(-10)
        -10.0

    **Cost:** O(1), direct integer to float conversion.
    """
    return float(number)


def number_to_complex(number: Union[int, float]) -> complex:
    """
    Converts an integer or float to a complex number with zero imaginary part.

    Args:
        number (Union[int, float]): The number to convert.

    Returns:
        complex: The resulting complex number.

    Example:
        >>> number_to_complex(4.2)
        (4.2+0j)
        >>> number_to_complex(7)
        (7+0j)

    **Cost:** O(1), direct conversion to complex number.
    """
    return complex(number)


def number_to_bool(number: Union[int, float]) -> bool:
    """
    Converts an integer or float to a boolean value.
    0 or 0.0 converts to False; any other number converts to True.

    Args:
        number (Union[int, float]): The number to convert.

    Returns:
        bool: The resulting boolean value.

    Example:
        >>> number_to_bool(0)
        False
        >>> number_to_bool(3.5)
        True
        >>> number_to_bool(-1)
        True
        >>> number_to_bool(0.0)
        False

    **Cost:** O(1), direct conversion to boolean value.
    """
    return bool(number)


def bool_to_int(value: bool) -> int:
    """
    Converts a boolean value to an integer.
    True converts to 1; False converts to 0.

    Args:
        value (bool): The boolean value to convert.

    Returns:
        int: The resulting integer.

    Example:
        >>> bool_to_int(True)
        1
        >>> bool_to_int(False)
        0

    **Cost:** O(1), direct boolean to integer conversion.
    """
    return int(value)


def bool_to_float(value: bool) -> float:
    """
    Converts a boolean value to a floating-point number.
    True converts to 1.0; False converts to 0.0.

    Args:
        value (bool): The boolean value to convert.

    Returns:
        float: The resulting float number.

    Example:
        >>> bool_to_float(True)
        1.0
        >>> bool_to_float(False)
        0.0

    **Cost:** O(1), direct boolean to float conversion.
    """
    return float(value)


def number_to_string(number: Union[int, float]) -> str:
    """
    Converts an integer or float to its string representation.

    Args:
        number (Union[int, float]): The number to convert.

    Returns:
        str: The resulting string.

    Example:
        >>> number_to_string(3.14)
        '3.14'
        >>> number_to_string(100)
        '100'
        >>> number_to_string(-0.5)
        '-0.5'

    **Cost:** O(1), direct string conversion.
    """
    return str(number)


def round_float_to_int(number: float) -> int:
    """
    Rounds a float to the nearest integer.

    Args:
        number (float): The float number to round.

    Returns:
        int: The nearest integer to the given number.
             If the number is exactly halfway between two integers (e.g., X.5),
             Python 3.x rounds to the nearest even integer ("banker's rounding").

    Example:
        >>> round_float_to_int(3.6)
        4
        >>> round_float_to_int(3.2)
        3
        >>> round_float_to_int(3.5)  # Rounds to nearest even (4)
        4
        >>> round_float_to_int(2.5)  # Rounds to nearest even (2)
        2
        >>> round_float_to_int(-3.6)
        -4
        >>> round_float_to_int(-3.5)  # Rounds to nearest even (-4)
        -4

    **Cost:** O(1), rounding via built-in function.
    """
    return round(number)


def hex_to_int(hex_string: str) -> int:
    """
    Converts a hexadecimal string to an integer.

    Args:
        hex_string (str): The hexadecimal string (may have '0x' prefix).

    Returns:
        int: The decimal integer.

    Example:
        >>> hex_to_int("0xff")
        255
        >>> hex_to_int("FF")
        255
        >>> hex_to_int("a")
        10

    **Cost:** O(n), where n is the length of the hexadecimal string.
    """
    return int(hex_string, 16)


def bin_to_int(bin_string: str) -> int:
    """
    Converts a binary string to an integer.

    Args:
        bin_string (str): The binary string (may have '0b' prefix).

    Returns:
        int: The decimal integer.

    Example:
        >>> bin_to_int("0b1010")
        10
        >>> bin_to_int("111")
        7

    **Cost:** O(n), where n is the length of the binary string.
    """
    return int(bin_string, 2)


def octal_to_int(octal_string: str) -> int:
    """
    Converts an octal string to an integer.

    Args:
        octal_string (str): The octal string (may have '0o' prefix).

    Returns:
        int: The decimal integer.

    Example:
        >>> octal_to_int("0o17")
        15
        >>> octal_to_int("77")
        63

    **Cost:** O(n), where n is the length of the octal string.
    """
    return int(octal_string, 8)


def int_to_binary_clean(number: int) -> str:
    """
    Converts an integer to its binary representation as a string, without the '0b' prefix.

    Args:
        number (int): The integer to convert.

    Returns:
        str: The binary string.

    Example:
        >>> int_to_binary_clean(10)
        '1010'
        >>> int_to_binary_clean(5)
        '101'

    **Cost:** O(log n), where n is the value of the number.
    """
    return format(number, 'b')


def int_to_hex_clean(number: int) -> str:
    """
    Converts an integer to its hexadecimal representation as a string, without the '0x' prefix.

    Args:
        number (int): The integer to convert.

    Returns:
        str: The hexadecimal string (lowercase).

    Example:
        >>> int_to_hex_clean(255)
        'ff'
        >>> int_to_hex_clean(10)
        'a'

    **Cost:** O(log n), where n is the value of the number.
    """
    return format(number, 'x')


def int_to_binary_with_prefix(number: int) -> str:
    """
    Converts an integer to its binary representation as a string, including the '0b' prefix.

    Args:
        number (int): The integer to convert.

    Returns:
        str: The binary string with prefix.

    Example:
        >>> int_to_binary_with_prefix(255)
        '0b11111111'
        >>> int_to_binary_with_prefix(10)
        '0b1010'

    **Cost:** O(log n), where n is the value of the number.
    """
    return format(number, '#b')


def int_to_hex_with_prefix(number: int) -> str:
    """
    Converts an integer to its hexadecimal representation as a string, including the '0x' prefix.

    Args:
        number (int): The integer to convert.

    Returns:
        str: The hexadecimal string with prefix (lowercase).

    Example:
        >>> int_to_hex_with_prefix(255)
        '0xff'
        >>> int_to_hex_with_prefix(10)
        '0xa'

    **Cost:** O(log n), where n is the value of the number.
    """
    return format(number, '#x')


def int_to_octal_with_prefix(number: int) -> str:
    """
    Converts an integer to its octal representation as a string, including the '0o' prefix.

    Args:
        number (int): The integer to convert.

    Returns:
        str: The octal string with prefix.

    Example:
        >>> int_to_octal_with_prefix(255)
        '0o377'
        >>> int_to_octal_with_prefix(15)
        '0o17'

    **Cost:** O(log n), where n is the value of the number.
    """
    return format(number, '#o')


def to_js_safe_integer(number: Union[int, float]) -> Union[int, str]:
    """
    Converts a number to a JavaScript-safe integer.

    If the number is within JavaScript's safe integer range (-(2^53-1) to 2^53-1),
    it returns a Python int. If it exceeds this range, it returns a string to avoid
    precision loss in JavaScript, requiring JavaScript to handle it as BigInt or
    another large number representation.

    Args:
        number (Union[int, float]): The integer or float to convert.
                                    If float, it will be truncated to integer before checking.

    Returns:
        Union[int, str]: The number as int if within JS safe range,
                         or as string if it exceeds that range.

    Raises:
        TypeError: If 'number' is not an int or float.

    Example:
        >>> to_js_safe_integer(100)
        100
        >>> to_js_safe_integer(9007199254740991) # JS_MAX_SAFE_INTEGER
        9007199254740991
        >>> to_js_safe_integer(9007199254740992) # JS_MAX_SAFE_INTEGER + 1
        '9007199254740992'
        >>> to_js_safe_integer(-9007199254740991) # JS_MIN_SAFE_INTEGER
        -9007199254740991
        >>> to_js_safe_integer(-9007199254740992) # JS_MIN_SAFE_INTEGER - 1
        '-9007199254740992'
        >>> to_js_safe_integer(3.14) # Floats are truncated to integers
        3
        >>> to_js_safe_integer(9007199254740991.99)
        9007199254740991

    **Cost:** O(1), integer comparison and conversion.
    """
    if not isinstance(number, (int, float)):
        raise TypeError("'number' must be an int or float.")
    
    # Truncate floats to integers for checking
    num_int = int(number)

    if JS_MIN_SAFE_INTEGER <= num_int <= JS_MAX_SAFE_INTEGER:
        return num_int
    else:
        return str(num_int)


def convert_string_to_float_with_locale(number_string: str, target_locale: Optional[str] = None) -> float:
    """
    Converts a numeric string to a float, interpreting decimal and thousands separators
    according to a specific regional configuration (locale).

    This function handles number input from different world regions where decimal and
    thousands separators may vary (e.g., ',' vs '.'). It uses Python's `locale` module
    to optionally set a specific `target_locale` for conversion. If `target_locale` is
    provided, the function saves the current system locale, temporarily sets the new
    locale, performs the conversion with `locale.atof()`, and then restores the
    original locale.

    Args:
        number_string (str): The string representing the number to convert.
        target_locale (Optional[str]): The locale string to use for conversion
                                       (e.g., 'es_ES', 'de_DE', 'en_US'). If None,
                                       uses the current system locale.

    Returns:
        float: The resulting floating-point number.

    Raises:
        TypeError: If 'number_string' is not a string.
        ValueError: If the string cannot be interpreted as a valid number within
                    the specified locale, or if the locale is not valid.

    Example:
        >>> # Configuration for a locale using comma as decimal (e.g., Spanish from Spain)
        >>> convert_string_to_float_with_locale("1.234,56", 'es_ES')
        1234.56
        >>> convert_string_to_float_with_locale("123,45", 'es_ES')
        123.45

        >>> # Configuration for a locale using dot as decimal (e.g., US English)
        >>> convert_string_to_float_with_locale("1,234.56", 'en_US')
        1234.56
        >>> convert_string_to_float_with_locale("123.45", 'en_US')
        123.45

    **Cost:** O(n), where n is the length of the string. Includes locale operations.
    """
    if not isinstance(number_string, str):
        raise TypeError("'number_string' must be a string.")

    original_locale = None
    try:
        # Guarda el locale actual para restaurarlo después
        original_locale = locale.getlocale(locale.LC_ALL)
        
        if target_locale:
            # Establece el locale temporalmente
            # locale.setlocale puede lanzar un locale.Error si el locale no es válido o no está instalado
            locale.setlocale(locale.LC_ALL, target_locale)
        else:
            # Asegúrate de que el locale numérico esté configurado, si no, usa el predeterminado del sistema
            locale.setlocale(locale.LC_ALL, '') # '' usa el locale predeterminado del usuario/sistema

        # Realiza la conversión usando locale.atof()
        return locale.atof(number_string)
    except locale.Error as e:
        raise ValueError(f"Could not set locale '{target_locale}'. Error: {e}. Check if the locale is installed on your system.")
    except ValueError as e:
        # Re-lanzar ValueError si la cadena no es un número válido en el locale especificado
        raise ValueError(f"Could not convert string '{number_string}' to float using locale '{target_locale or 'current'}'. Error: {e}")
    finally:
        # Asegura que el locale original siempre se restaure
        if original_locale:
            locale.setlocale(locale.LC_ALL, original_locale)


def safe_convert_number(value: Any, default_value: Union[int, float] = 0, target_type: type = float) -> Union[int, float]:
    """
    Safely converts an input value to a numeric type (float or int), using a
    try-except pattern to handle errors and provide a fallback value.

    This function handles data input from users or external sources that often
    contains values that cannot be directly converted to numbers. It prevents
    program crashes and improves resilience when processing uncertain data.

    Args:
        value (Any): The input value to attempt conversion (can be str, int, float, None, etc.).
        default_value (Union[int, float]): The value to return if conversion fails.
                                          Default is 0.
        target_type (type): The numeric type to convert to (int or float).
                            Default is float.

    Returns:
        Union[int, float]: The converted value or `default_value` if conversion fails.

    Raises:
        ValueError: If 'target_type' is neither 'int' nor 'float'.

    Example:
        >>> # Conversion to float
        >>> safe_convert_number("3.14")
        3.14
        >>> safe_convert_number("10")
        10.0
        >>> safe_convert_number("abc")
        0.0
        >>> safe_convert_number("")
        0.0
        >>> safe_convert_number(None)
        0.0
        >>> safe_convert_number("hello", default_value=-1.0)
        -1.0

        >>> # Conversion to int
        >>> safe_convert_number("5", target_type=int)
        5
        >>> safe_convert_number("7.8", target_type=int)
        7
        >>> safe_convert_number("not_a_num", default_value=99, target_type=int)
        99
        >>> safe_convert_number(None, default_value=1, target_type=int)
        1
        >>> safe_convert_number(True, target_type=int) # Booleans work
        1

    **Cost:** O(1), type conversion with exception handling.
    """
    if target_type not in [int, float]:
        raise ValueError("target_type must be 'int' or 'float'.")

    try:
        # Intentar convertir el valor al tipo deseado
        return target_type(value)
    except (ValueError, TypeError):
        # Si la conversión falla, devolver el valor por defecto
        return default_value


def ieee754_hex_representation(numero: float) -> str:
    """
    Returns the hexadecimal representation of a floating-point number
    according to the IEEE 754 standard.

    This method shows the actual IEEE (underlying binary) value of a float,
    which can be useful for debugging or understanding how floating-point
    numbers are stored.

    Args:
        numero (float): The floating-point number for which to obtain
                        the hexadecimal representation.

    Returns:
        str: A string representing the IEEE 754 hexadecimal value of the number.
             The format is '0x<mantissa>p<exponent>'.

    Example:
        >>> ieee754_hex_representation(3.14)
        '0x1.91eb851eb851fp+1'
        >>> ieee754_hex_representation(0.5)
        '0x1.0p-1'
        >>> ieee754_hex_representation(1.0)
        '0x1.0p+0'
        >>> ieee754_hex_representation(-1.0)
        '-0x1.0p+0'
        >>> ieee754_hex_representation(float('inf'))
        'inf'
        >>> ieee754_hex_representation(float('-inf'))
        '-inf'
        >>> ieee754_hex_representation(float('nan'))
        'nan'

    **Cost:** O(1), call to the float's hex() method.
    """
    return numero.hex()


def int_to_bytes(integer_value: int, num_bytes: int, byteorder: str = 'big') -> bytes:
    """Converts an integer to a byte sequence.

    Description:
        Useful for binary data transmission, communication protocols,
        or storing data in binary formats.

    Args:
        integer_value (int): The integer to convert.
        num_bytes (int): The desired number of bytes for the representation.
        byteorder (str): Byte order ('big' or 'little'). Default is 'big'.

    Returns:
        bytes: The byte representation of the integer.

    Raises:
        OverflowError: If the integer is too large for the specified number of bytes.

    Usage Example:
        >>> int_to_bytes(123, 2, byteorder='big')
        b'\x00{'
        >>> int_to_bytes(256, 2, byteorder='little')
        b'\x00\x01'

    Cost: O(1)
    """
    return integer_value.to_bytes(num_bytes, byteorder=byteorder)


def bytes_to_int(byte_sequence: bytes, byteorder: str = 'big') -> int:
    """Converts a byte sequence to an integer.

    Description:
        Useful for decoding data received through a binary protocol
        or reading numeric values from binary files.

    Args:
        byte_sequence (bytes): The byte sequence to convert.
        byteorder (str): Byte order ('big' or 'little'). Default is 'big'.

    Returns:
        int: The integer represented by the byte sequence.

    Usage Example:
        >>> bytes_to_int(b'\x00{', 'big')
        123
        >>> bytes_to_int(b'\x00\x01', 'little')
        256

    Cost: O(1)
    """
    return int.from_bytes(byte_sequence, byteorder=byteorder)


def float_to_json_safe(float_value: float) -> str:
    """Converts a floating-point number to a JSON-safe representation.

    Description:
        JSON does not support NaN or Infinity. This function converts
        them to string representations before serialization.

    Args:
        float_value (float): The input floating-point number.

    Returns:
        str: The number as a valid JSON string.

    Usage Example:
        >>> float_to_json_safe(3.14)
        '3.14'
        >>> float_to_json_safe(float('nan'))
        '"NaN"'

    Cost: O(1)
    """
    if math.isnan(float_value):
        return json.dumps(str(float_value))
    elif math.isinf(float_value):
        return json.dumps(str(float_value))
    else:
        return json.dumps(float_value)


def convert_bytes_to(unit: str, value: Union[int, float, str]) -> float:
    """Converts a byte value to a specified target unit.

    This function takes a byte value and converts it into a more readable
    unit (e.g., KB, MB, GB, KiB, MiB, GiB). It supports both SI (powers of 1000)
    and IEC (powers of 1024) units.

    Args:
        unit: The target unit for conversion (e.g., 'KB', 'MB', 'GB', 'TB',
              'PB' for SI units, or 'KiB', 'MiB', 'GiB', 'TiB', 'PiB' for IEC units).
        value: The byte value to convert. Can be an int, float, or a string
               that can be converted to a number.

    Returns:
        The converted value as a float.

    Raises:
        TypeError: If 'value' cannot be converted to a numeric type.
        ValueError: If 'unit' is not a recognized conversion unit.

    Example:
        >>> convert_bytes_to('KB', 1024)
        1.024
        >>> convert_bytes_to('GiB', 1073741824) # 1 GiB
        1.0
        >>> convert_bytes_to('GB', 1000000000) # 1 GB
        1.0
        >>> convert_bytes_to('MB', 5242880) # 5 MiB
        5.24288
        >>> convert_bytes_to('MiB', 5242880) # 5 MiB
        5.0
        >>> convert_bytes_to('TB', 2_000_000_000_000)
        2.0
        >>> convert_bytes_to('KiB', "2048")
        2.0

    **Cost:** O(1), conversión aritmética simple.
    """
    # Why: Attempt to convert the input value to a float.
    # This makes the function robust to string inputs that represent numbers.
    try:
        numeric_value = float(value)
    except (ValueError, TypeError) as e:
        raise TypeError(f"Value '{value}' cannot be converted to a numeric type. Original error: {e}")

    # Why: Define conversion constants directly within the function scope.
    # While they could be global constants, keeping them here ensures all conversion
    # logic is self-contained.
    KIBI = 1024**1
    MEBI = 1024**2
    GIBI = 1024**3
    TEBI = 1024**4
    PEBI = 1024**5

    KILO = 1000**1
    MEGA = 1000**2
    GIGA = 1000**3
    TERA = 1000**4
    PETA = 1000**5

    # Why: Standardize the unit string for case-insensitive comparison.
    normalized_unit = unit.strip().upper()

    # Why: Use a dictionary for cleaner mapping of units to their respective divisors.
    # This avoids long if/elif chains and is easily extensible.
    conversion_factors = {
        'KB': KILO, 'MB': MEGA, 'GB': GIGA, 'TB': TERA, 'PB': PETA,
        'KIB': KIBI, 'MIB': MEBI, 'GIB': GIBI, 'TIB': TEBI, 'PIB': PEBI
    }

    # Why: Retrieve the appropriate divisor. If the unit is not found, raise a ValueError.
    divisor = conversion_factors.get(normalized_unit)
    if divisor is None:
        raise ValueError(
            f"Unsupported unit: '{unit}'. "
            f"Supported units are: {', '.join(conversion_factors.keys())}"
        )

    # Why: Perform the actual division to convert bytes to the target unit.
    return numeric_value / divisor


def number_to_hexadecimal(number_input: Union[int, float]) -> str:
    """
    Returns a string representing the hexadecimal value of a number.

    This function converts an integer or float to its hexadecimal string representation.
    For integers, it uses Python's built-in `hex()` function, which prefixes the
    output with '0x'. For floats, it first converts the float to an integer
    (by truncating its decimal part) before converting to hexadecimal.

    Args:
        number_input (Union[int, float]): The number to convert.

    Returns:
        str: A string representing the hexadecimal value, prefixed with '0x'.

    Raises:
        TypeError: If the input is not an integer or a float.
        ValueError: If the input number is too large to be converted to an integer
                    for hexadecimal representation (relevant for very large floats).

    Example:
        >>> number_to_hexadecimal(255)
        '0xff'
        >>> number_to_hexadecimal(10)
        '0xa'
        >>> number_to_hexadecimal(0)
        '0x0'
        >>> number_to_hexadecimal(25.75)
        '0x19'
        >>> number_to_hexadecimal(-10)
        '-0xa'

    **Cost:** O(log n), donde n es el valor absoluto del número.
    """
    if not isinstance(number_input, (int, float)):
        raise TypeError("Input must be an integer or a float.")

    # Convert float to integer by truncating, as hexadecimal is typically for integers.
    # We maintain the sign before conversion and apply it back if needed.
    if isinstance(number_input, float):
        # We need to handle the sign before casting to int, as int() truncates towards zero.
        if number_input < 0:
            integer_part = int(abs(number_input))
            hex_value = hex(integer_part)
            return f"-{hex_value}"
        else:
            integer_part = int(number_input)
            return hex(integer_part)
    else: # It's an integer
        return hex(number_input)
    

def number_to_octal(number_input: Union[int, float]) -> str:
    """
    Returns a string representing the octal value of a number.

    This function converts an integer or float to its octal string representation.
    For integers, it uses Python's built-in `oct()` function, which prefixes the
    output with '0o'. For floats, it first converts the float to an integer
    (by truncating its decimal part) before converting to octal.

    Args:
        number_input (Union[int, float]): The number to convert.

    Returns:
        str: A string representing the octal value, prefixed with '0o'.

    Raises:
        TypeError: If the input is not an integer or a float.
        ValueError: If the input number is too large to be converted to an integer
                    for octal representation (relevant for very large floats).

    Example:
        >>> number_to_octal(8)
        '0o10'
        >>> number_to_octal(15)
        '0o17'
        >>> number_to_octal(0)
        '0o0'
        >>> number_to_octal(10.99)
        '0o12'
        >>> number_to_octal(-7)
        '-0o7'

    **Cost:** O(log n), donde n es el valor absoluto del número.
    """
    if not isinstance(number_input, (int, float)):
        raise TypeError("Input must be an integer or a float.")

    # Convert float to integer by truncating, as octal is typically for integers.
    # We maintain the sign before conversion and apply it back if needed.
    if isinstance(number_input, float):
        # We need to handle the sign before casting to int, as int() truncates towards zero.
        if number_input < 0:
            integer_part = int(abs(number_input))
            octal_value = oct(integer_part)
            return f"-{octal_value}"
        else:
            integer_part = int(number_input)
            return oct(integer_part)
    else: # It's an integer
        return oct(number_input)


# ---------------------------------------------------------------------------
# Fraction, Roman numeral, and natural-language conversions
# ---------------------------------------------------------------------------


def decimal_to_fraction(number: float,
                        max_denominator: int = 1000) -> tuple:
    """Convert a decimal number to a fraction (numerator, denominator).

    Uses the standard library ``fractions.Fraction`` for best rational
    approximation up to *max_denominator*.

    Args:
        number: Decimal value to convert.
        max_denominator: Maximum denominator allowed. Defaults to 1000.

    Returns:
        Tuple (numerator, denominator).

    Example:
        >>> decimal_to_fraction(0.75)
        (3, 4)
        >>> decimal_to_fraction(3.14159, 100)
        (22, 7)

    Complexity: O(log(max_denominator))
    """

    from fractions import Fraction
    frac = Fraction(number).limit_denominator(max_denominator)
    return (frac.numerator, frac.denominator)


def fraction_to_decimal(numerator: int, denominator: int) -> float:
    """Convert a fraction to its decimal representation.

    Args:
        numerator: Numerator of the fraction.
        denominator: Denominator of the fraction.

    Returns:
        Float result of numerator / denominator.

    Raises:
        ZeroDivisionError: If denominator is 0.

    Example:
        >>> fraction_to_decimal(3, 4)
        0.75
        >>> fraction_to_decimal(22, 7)
        3.142857142857143

    Complexity: O(1)
    """

    if denominator == 0:
        raise ZeroDivisionError("denominator must not be zero.")

    return numerator / denominator


def int_to_roman(number: int) -> str:
    """Convert a positive integer to a Roman numeral string.

    Args:
        number: Integer in [1, 3999].

    Returns:
        Roman numeral string.

    Raises:
        ValueError: If number is outside [1, 3999].

    Example:
        >>> int_to_roman(14)
        'XIV'
        >>> int_to_roman(2024)
        'MMXXIV'

    Complexity: O(1)
    """

    if not 1 <= number <= 3999:
        raise ValueError(f"number ({number}) must be in [1, 3999].")

    values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I"),
    ]
    result = []

    for val, sym in values:

        while number >= val:
            result.append(sym)
            number -= val

    return "".join(result)


def roman_to_int(roman: str) -> int:
    """Convert a Roman numeral string to an integer.

    Args:
        roman: String with valid Roman numeral characters (I, V, X, L, C, D, M).

    Returns:
        Integer value.

    Raises:
        ValueError: If roman contains invalid characters.

    Example:
        >>> roman_to_int('XIV')
        14
        >>> roman_to_int('MMXXIV')
        2024

    Complexity: O(n) where n = len(roman)
    """

    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50,
                 "C": 100, "D": 500, "M": 1000}
    roman = roman.upper().strip()
    result = 0
    prev = 0

    for ch in reversed(roman):

        if ch not in roman_map:
            raise ValueError(f"Invalid Roman numeral character: '{ch}'.")

        val = roman_map[ch]

        if val < prev:
            result -= val
        else:
            result += val

        prev = val

    return result


def number_to_words(number: int, lang: str = "en") -> str:
    """Convert an integer to its written-word representation.

    Supports English (``'en'``) and Spanish (``'es'``) for integers in
    [-999_999_999_999, 999_999_999_999].

    Args:
        number: Integer to convert.
        lang: Language code (``'en'`` or ``'es'``). Defaults to ``'en'``.

    Returns:
        Written representation as string.

    Raises:
        ValueError: If number is out of supported range or lang is unsupported.

    Example:
        >>> number_to_words(42)
        'forty-two'
        >>> number_to_words(42, 'es')
        'cuarenta y dos'
        >>> number_to_words(0)
        'zero'

    Complexity: O(1)
    """

    if lang not in ("en", "es"):
        raise ValueError(f"Unsupported language: '{lang}'. Use 'en' or 'es'.")

    if not -999_999_999_999 <= number <= 999_999_999_999:
        raise ValueError("number must be in [-999999999999, 999999999999].")

    if lang == "en":
        return _number_to_words_en(number)

    return _number_to_words_es(number)


# --- English helpers ---

_ONES_EN = ["", "one", "two", "three", "four", "five", "six", "seven",
            "eight", "nine", "ten", "eleven", "twelve", "thirteen",
            "fourteen", "fifteen", "sixteen", "seventeen", "eighteen",
            "nineteen"]
_TENS_EN = ["", "", "twenty", "thirty", "forty", "fifty", "sixty",
            "seventy", "eighty", "ninety"]


def _chunk_en(n: int) -> str:
    """Convert 0–999 to English words."""

    if n == 0:
        return ""

    parts = []

    if n >= 100:
        parts.append(_ONES_EN[n // 100] + " hundred")
        n %= 100

    if n >= 20:
        word = _TENS_EN[n // 10]

        if n % 10:
            word += "-" + _ONES_EN[n % 10]

        parts.append(word)
    elif n >= 1:
        parts.append(_ONES_EN[n])

    return " ".join(parts)


def _number_to_words_en(n: int) -> str:

    if n == 0:
        return "zero"

    prefix = ""

    if n < 0:
        prefix = "negative "
        n = -n

    groups = [
        (1_000_000_000, "billion"),
        (1_000_000, "million"),
        (1_000, "thousand"),
    ]
    parts = []

    for divisor, label in groups:

        if n >= divisor:
            parts.append(_chunk_en(n // divisor) + " " + label)
            n %= divisor

    if n > 0:
        parts.append(_chunk_en(n))

    return prefix + " ".join(parts)


# --- Spanish helpers ---

_ONES_ES = ["", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete",
            "ocho", "nueve", "diez", "once", "doce", "trece", "catorce",
            "quince", "dieciséis", "diecisiete", "dieciocho", "diecinueve",
            "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro",
            "veinticinco", "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
_TENS_ES = ["", "diez", "veinte", "treinta", "cuarenta", "cincuenta",
            "sesenta", "setenta", "ochenta", "noventa"]
_HUNDREDS_ES = ["", "ciento", "doscientos", "trescientos", "cuatrocientos",
                "quinientos", "seiscientos", "setecientos", "ochocientos",
                "novecientos"]


def _chunk_es(n: int) -> str:
    """Convert 0–999 to Spanish words."""

    if n == 0:
        return ""

    if n == 100:
        return "cien"

    parts = []

    if n >= 100:
        parts.append(_HUNDREDS_ES[n // 100])
        n %= 100

    if n <= 29:

        if n > 0:
            parts.append(_ONES_ES[n])

    else:
        word = _TENS_ES[n // 10]

        if n % 10:
            word += " y " + _ONES_ES[n % 10]

        parts.append(word)

    return " ".join(parts)


def _number_to_words_es(n: int) -> str:

    if n == 0:
        return "cero"

    prefix = ""

    if n < 0:
        prefix = "menos "
        n = -n

    groups = [
        (1_000_000_000, "mil millones"),
        (1_000_000, "millón", "millones"),
        (1_000, "mil"),
    ]
    parts = []

    for item in groups:
        divisor = item[0]

        if n >= divisor:
            count = n // divisor

            if divisor == 1_000_000:
                singular, plural = item[1], item[2]

                if count == 1:
                    parts.append("un " + singular)
                else:
                    parts.append(_chunk_es(count) + " " + plural)
            elif divisor == 1_000:

                if count == 1:
                    parts.append("mil")
                else:
                    parts.append(_chunk_es(count) + " mil")
            else:
                parts.append(_chunk_es(count) + " " + item[1])

            n %= divisor

    if n > 0:
        parts.append(_chunk_es(n))

    return prefix + " ".join(parts)


def add_bool_to_int(boolean_value: bool, int_value: int) -> int:
    """Adds a boolean value to an integer.

    In Python, True evaluates to 1 and False to 0 in numeric contexts.

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

    **Cost:** O(1), boolean addition as integer.
    """
    if not isinstance(boolean_value, bool):
        raise TypeError("'boolean_value' must be a boolean.")

    if not isinstance(int_value, int):
        raise TypeError("'int_value' must be an integer.")

    return boolean_value + int_value


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
        >>> is_numeric_type("123")
        False
        >>> is_numeric_type(None)
        False

    **Cost:** O(1), type verification using isinstance.
    """
    return isinstance(value, (int, float, Decimal))


def number_to_base(number: int, radix: int, min_length: int = 0) -> str:
    """Converts a decimal integer to a string in the specified base.

    Description:
        Converts a non-negative integer to its representation in the given
        radix (2–36). Optionally pads the result to a minimum length.
        Equivalent to Excel BASE.

    Args:
        number: The non-negative integer to convert.
        radix: The target base (2 to 36).
        min_length: Minimum length of the result, zero-padded if needed.

    Returns:
        The string representation of the number in the given base.

    Raises:
        TypeError: If number or radix are not integers.
        ValueError: If number is negative or radix is outside 2–36.

    Example:
        >>> number_to_base(255, 16)
        'FF'
        >>> number_to_base(10, 2, 8)
        '00001010'
        >>> number_to_base(100, 8)
        '144'

    Complexity: O(log_radix(number))
    """
    if not isinstance(number, int) or not isinstance(radix, int):
        raise TypeError("Both 'number' and 'radix' must be integers.")

    if number < 0:
        raise ValueError("Number must be non-negative.")

    if radix < 2 or radix > 36:
        raise ValueError("Radix must be between 2 and 36.")

    if not isinstance(min_length, int) or min_length < 0:
        raise TypeError("'min_length' must be a non-negative integer.")

    if number == 0:
        return "0".zfill(max(min_length, 1))

    digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = []

    while number > 0:
        result.append(digits[number % radix])
        number //= radix

    text = "".join(reversed(result))
    return text.zfill(min_length) if min_length > 0 else text


def base_to_decimal(text: str, radix: int) -> int:
    """Converts a string representation from the specified base to decimal.

    Description:
        Parses a string as a number in the given radix (2–36) and returns
        the equivalent decimal integer. Equivalent to Excel DECIMAL.

    Args:
        text: The string representing the number in the given base.
        radix: The base of the input number (2 to 36).

    Returns:
        The decimal integer value.

    Raises:
        TypeError: If text is not a string or radix is not an integer.
        ValueError: If the text contains invalid digits for the given base,
            or the radix is outside 2–36.

    Example:
        >>> base_to_decimal('FF', 16)
        255
        >>> base_to_decimal('1010', 2)
        10
        >>> base_to_decimal('144', 8)
        100

    Complexity: O(n) where n is the length of the text.
    """
    if not isinstance(text, str):
        raise TypeError("'text' must be a string.")

    if not isinstance(radix, int):
        raise TypeError("'radix' must be an integer.")

    if radix < 2 or radix > 36:
        raise ValueError("Radix must be between 2 and 36.")

    text = text.strip().upper()

    if not text:
        raise ValueError("Input text cannot be empty.")

    try:
        return int(text, radix)
    except ValueError:
        raise ValueError(
            f"Invalid digits in '{text}' for base {radix}."
        )


def bin_to_hex(binary: str) -> str:
    """Converts a binary string to hexadecimal.

    Description:
        Parses a binary string and returns its hexadecimal representation.
        Equivalent to Excel BIN2HEX.

    Args:
        binary: A string of 0s and 1s (optional '0b' prefix).

    Returns:
        Uppercase hexadecimal string without prefix.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the string contains invalid binary digits.

    Example:
        >>> bin_to_hex('11111111')
        'FF'
        >>> bin_to_hex('1010')
        'A'

    Complexity: O(n)
    """
    if not isinstance(binary, str):
        raise TypeError("Input must be a string.")

    decimal = int(binary.strip().replace("0b", ""), 2)
    return format(decimal, "X")


def bin_to_oct(binary: str) -> str:
    """Converts a binary string to octal.

    Description:
        Parses a binary string and returns its octal representation.
        Equivalent to Excel BIN2OCT.

    Args:
        binary: A string of 0s and 1s (optional '0b' prefix).

    Returns:
        Octal string without prefix.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the string contains invalid binary digits.

    Example:
        >>> bin_to_oct('11111111')
        '377'
        >>> bin_to_oct('1000')
        '10'

    Complexity: O(n)
    """
    if not isinstance(binary, str):
        raise TypeError("Input must be a string.")

    decimal = int(binary.strip().replace("0b", ""), 2)
    return format(decimal, "o")


def dec_to_oct(number: int) -> str:
    """Converts a decimal integer to octal.

    Description:
        Returns the octal string representation of a non-negative integer.
        Equivalent to Excel DEC2OCT.

    Args:
        number: A non-negative integer.

    Returns:
        Octal string without prefix.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If input is negative.

    Example:
        >>> dec_to_oct(100)
        '144'
        >>> dec_to_oct(8)
        '10'

    Complexity: O(log n)
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")

    if number < 0:
        raise ValueError("Input must be non-negative.")

    return format(number, "o")


def hex_to_bin(hexadecimal: str) -> str:
    """Converts a hexadecimal string to binary.

    Description:
        Parses a hexadecimal string and returns its binary representation.
        Equivalent to Excel HEX2BIN.

    Args:
        hexadecimal: A hexadecimal string (optional '0x' prefix).

    Returns:
        Binary string without prefix.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the string contains invalid hex digits.

    Example:
        >>> hex_to_bin('FF')
        '11111111'
        >>> hex_to_bin('A')
        '1010'

    Complexity: O(n)
    """
    if not isinstance(hexadecimal, str):
        raise TypeError("Input must be a string.")

    decimal = int(hexadecimal.strip().replace("0x", "").replace("0X", ""), 16)
    return format(decimal, "b")


def hex_to_oct(hexadecimal: str) -> str:
    """Converts a hexadecimal string to octal.

    Description:
        Parses a hexadecimal string and returns its octal representation.
        Equivalent to Excel HEX2OCT.

    Args:
        hexadecimal: A hexadecimal string (optional '0x' prefix).

    Returns:
        Octal string without prefix.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the string contains invalid hex digits.

    Example:
        >>> hex_to_oct('FF')
        '377'
        >>> hex_to_oct('1F')
        '37'

    Complexity: O(n)
    """
    if not isinstance(hexadecimal, str):
        raise TypeError("Input must be a string.")

    decimal = int(hexadecimal.strip().replace("0x", "").replace("0X", ""), 16)
    return format(decimal, "o")


def oct_to_bin(octal: str) -> str:
    """Converts an octal string to binary.

    Description:
        Parses an octal string and returns its binary representation.
        Equivalent to Excel OCT2BIN.

    Args:
        octal: An octal string (optional '0o' prefix).

    Returns:
        Binary string without prefix.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the string contains invalid octal digits.

    Example:
        >>> oct_to_bin('377')
        '11111111'
        >>> oct_to_bin('10')
        '1000'

    Complexity: O(n)
    """
    if not isinstance(octal, str):
        raise TypeError("Input must be a string.")

    decimal = int(octal.strip().replace("0o", "").replace("0O", ""), 8)
    return format(decimal, "b")


def oct_to_hex(octal: str) -> str:
    """Converts an octal string to hexadecimal.

    Description:
        Parses an octal string and returns its hexadecimal representation.
        Equivalent to Excel OCT2HEX.

    Args:
        octal: An octal string (optional '0o' prefix).

    Returns:
        Uppercase hexadecimal string without prefix.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the string contains invalid octal digits.

    Example:
        >>> oct_to_hex('377')
        'FF'
        >>> oct_to_hex('37')
        '1F'

    Complexity: O(n)
    """
    if not isinstance(octal, str):
        raise TypeError("Input must be a string.")

    decimal = int(octal.strip().replace("0o", "").replace("0O", ""), 8)
    return format(decimal, "X")


# ========== UNIT CONVERSIONS ==========


def convert_units(
    number: Union[int, float], from_unit: str, to_unit: str,
) -> float:
    """Convert a value from one measurement unit to another.

    Description:
        Supports 13 categories: length, mass, time, temperature, pressure,
        force, energy, power, volume, area, speed, angle, and information.
        Equivalent to Excel CONVERT.

    Args:
        number: Value to convert.
        from_unit: Source unit abbreviation.
        to_unit: Target unit abbreviation.

    Returns:
        float: Converted value.

    Raises:
        TypeError: If number is not numeric.
        ValueError: If conversion is not supported.

    Example:
        >>> convert_units(100, 'cm', 'm')
        1.0
        >>> convert_units(1, 'kg', 'g')
        1000.0
        >>> convert_units(0, 'C', 'F')
        32.0

    Complexity: O(1)
    """
    if not isinstance(number, (int, float)):
        raise TypeError("number must be numeric.")

    categories: dict[str, dict[str, float]] = {
        "length": {
            "m": 1.0, "cm": 0.01, "mm": 0.001, "km": 1000.0,
            "in": 0.0254, "ft": 0.3048, "yd": 0.9144, "mi": 1609.344,
            "Nmi": 1852.0, "um": 1e-6, "nm": 1e-9, "ang": 1e-10,
            "Pica": 0.0254 / 6,
        },
        "mass": {
            "kg": 1.0, "g": 0.001, "mg": 1e-6, "lbm": 0.45359237,
            "ozm": 0.028349523125, "ton": 1000.0, "sg": 14.593903,
            "u": 1.66053906660e-27,
        },
        "time": {
            "sec": 1.0, "min": 60.0, "hr": 3600.0, "day": 86400.0,
            "yr": 365.25 * 86400.0, "ms": 0.001, "us": 1e-6, "ns": 1e-9,
        },
        "temperature": {"C": None, "F": None, "K": None, "Rank": None},
        "pressure": {
            "Pa": 1.0, "atm": 101325.0, "mmHg": 133.322,
            "Torr": 133.322, "psi": 6894.757, "bar": 100000.0,
            "mbar": 100.0, "kPa": 1000.0, "MPa": 1e6,
        },
        "force": {
            "N": 1.0, "dyn": 1e-5, "lbf": 4.4482216152605,
            "kgf": 9.80665, "pond": 9.80665e-3,
        },
        "energy": {
            "J": 1.0, "kJ": 1000.0, "cal": 4.1868, "kcal": 4186.8,
            "eV": 1.602176634e-19, "BTU": 1055.06, "Wh": 3600.0,
            "kWh": 3.6e6, "HPh": 2684519.5377,
        },
        "power": {
            "W": 1.0, "kW": 1000.0, "MW": 1e6, "HP": 745.69987158227,
            "PS": 735.49875, "BTU_s": 1055.06,
        },
        "volume": {
            "l": 1.0, "ml": 0.001, "gal": 3.785411784,
            "qt": 0.946352946, "pt": 0.473176473,
            "cup": 0.2365882365, "oz": 0.0295735295625,
            "tbs": 0.01478676478125, "tsp": 0.00492892159375,
            "m3": 1000.0, "cm3": 0.001, "ft3": 28.316846592,
            "in3": 0.016387064, "uk_gal": 4.54609,
        },
        "area": {
            "m2": 1.0, "cm2": 1e-4, "km2": 1e6, "ft2": 0.09290304,
            "in2": 6.4516e-4, "yd2": 0.83612736,
            "mi2": 2589988.110336, "ha": 10000.0,
            "acre": 4046.8564224, "Morgen": 2500.0,
        },
        "speed": {
            "m/s": 1.0, "km/h": 1 / 3.6, "mph": 0.44704,
            "kn": 1852.0 / 3600.0, "ft/s": 0.3048,
        },
        "angle": {
            "deg": 1.0, "rad": 57.29577951308232, "grad": 0.9,
        },
        "information": {
            "bit": 1.0, "byte": 8.0, "kbit": 1000.0,
            "Mbit": 1e6, "Gbit": 1e9,
            "kB": 8000.0, "MB": 8e6, "GB": 8e9, "TB": 8e12,
            "KiB": 8 * 1024.0, "MiB": 8 * 1024**2,
            "GiB": 8 * 1024**3, "TiB": 8 * 1024**4,
        },
    }


    def _convert_temperature(value: float, src: str, dst: str) -> float:
        if src == "C":
            k = value + 273.15
        elif src == "F":
            k = (value - 32) * 5 / 9 + 273.15
        elif src == "K":
            k = value
        elif src == "Rank":
            k = value * 5 / 9
        else:
            raise ValueError(f"Unknown temperature unit: {src}")

        if dst == "C":
            return k - 273.15

        if dst == "F":
            return (k - 273.15) * 9 / 5 + 32

        if dst == "K":
            return k

        if dst == "Rank":
            return k * 9 / 5

        raise ValueError(f"Unknown temperature unit: {dst}")

    for category, units in categories.items():

        if from_unit in units and to_unit in units:

            if category == "temperature":
                return _convert_temperature(number, from_unit, to_unit)

            return number * (units[from_unit] / units[to_unit])

    raise ValueError(
        f"Conversion from '{from_unit}' to '{to_unit}' not supported. "
        "Units must belong to the same category."
    )


# ========== DECIBEL CONVERSIONS ==========


def power_to_db(ratio: Union[int, float]) -> float:
    """Convert a power ratio to decibels.

    Description:
        Computes 10 × log₁₀(ratio). Equivalent to POWER2DB.

    Args:
        ratio: Power ratio (must be positive).

    Returns:
        float: Value in decibels.

    Raises:
        ValueError: If ratio is not positive.

    Example:
        >>> power_to_db(100)
        20.0

    Complexity: O(1)
    """
    if not isinstance(ratio, (int, float)) or ratio <= 0:
        raise ValueError("ratio must be a positive number.")

    return 10 * math.log10(ratio)


def db_to_power(decibels: Union[int, float]) -> float:
    """Convert decibels to a power ratio.

    Description:
        Computes 10^(dB/10). Inverse of power_to_db.

    Args:
        decibels: Value in decibels.

    Returns:
        float: Power ratio.

    Example:
        >>> db_to_power(20)
        100.0

    Complexity: O(1)
    """
    if not isinstance(decibels, (int, float)):
        raise TypeError("decibels must be numeric.")

    return 10 ** (decibels / 10)


def voltage_to_db(ratio: Union[int, float]) -> float:
    """Convert a voltage/amplitude ratio to decibels.

    Description:
        Computes 20 × log₁₀(ratio). Equivalent to VOLTAGE2DB.

    Args:
        ratio: Voltage/amplitude ratio (must be positive).

    Returns:
        float: Value in decibels.

    Raises:
        ValueError: If ratio is not positive.

    Example:
        >>> voltage_to_db(10)
        20.0

    Complexity: O(1)
    """
    if not isinstance(ratio, (int, float)) or ratio <= 0:
        raise ValueError("ratio must be a positive number.")

    return 20 * math.log10(ratio)


def db_to_voltage(decibels: Union[int, float]) -> float:
    """Convert decibels to a voltage/amplitude ratio.

    Description:
        Computes 10^(dB/20). Inverse of voltage_to_db.

    Args:
        decibels: Value in decibels.

    Returns:
        float: Voltage/amplitude ratio.

    Example:
        >>> db_to_voltage(20)
        10.0

    Complexity: O(1)
    """
    if not isinstance(decibels, (int, float)):
        raise TypeError("decibels must be numeric.")

    return 10 ** (decibels / 20)


# ========== WAVE / PHYSICS CONVERSIONS ==========


def wavelength(
    freq: Union[int, float], velocity: Union[int, float] = 299792458.0,
) -> float:
    """Calculate wavelength from frequency.

    Description:
        λ = velocity / frequency. Defaults to speed of light in vacuum.

    Args:
        freq: Frequency in hertz (must be positive).
        velocity: Propagation speed in m/s (default: speed of light).

    Returns:
        float: Wavelength in meters.

    Raises:
        ValueError: If freq is not positive.

    Example:
        >>> wavelength(1e9)
        0.299792458

    Complexity: O(1)
    """
    if not isinstance(freq, (int, float)) or freq <= 0:
        raise ValueError("freq must be a positive number.")

    return velocity / freq


def freq_from_wavelength(
    wavelength_m: Union[int, float],
    velocity: Union[int, float] = 299792458.0,
) -> float:
    """Calculate frequency from wavelength.

    Description:
        f = velocity / wavelength. Inverse of wavelength().

    Args:
        wavelength_m: Wavelength in meters (must be positive).
        velocity: Propagation speed in m/s (default: speed of light).

    Returns:
        float: Frequency in hertz.

    Raises:
        ValueError: If wavelength_m is not positive.

    Example:
        >>> freq_from_wavelength(0.299792458)
        1000000000.0

    Complexity: O(1)
    """
    if not isinstance(wavelength_m, (int, float)) or wavelength_m <= 0:
        raise ValueError("wavelength_m must be a positive number.")

    return velocity / wavelength_m


def doppler_freq(
    source_freq: Union[int, float],
    velocity: Union[int, float],
    wave_speed: Union[int, float] = 343.0,
) -> float:
    """Calculate observed frequency due to the Doppler effect.

    Description:
        f_obs = f_src × (v_wave / (v_wave − v_source)).
        Positive velocity means the source approaches the observer.

    Args:
        source_freq: Emitted frequency in hertz (must be positive).
        velocity: Source velocity in m/s (positive = approaching).
        wave_speed: Medium wave speed in m/s (default: 343, sound in air).

    Returns:
        float: Observed frequency in hertz.

    Raises:
        ValueError: If source_freq or wave_speed is not positive,
            or velocity equals wave_speed.

    Example:
        >>> round(doppler_freq(440, 30), 2)
        482.17

    Complexity: O(1)
    """
    if not isinstance(source_freq, (int, float)) or source_freq <= 0:
        raise ValueError("source_freq must be positive.")

    if not isinstance(wave_speed, (int, float)) or wave_speed <= 0:
        raise ValueError("wave_speed must be positive.")

    denominator = wave_speed - velocity

    if denominator == 0:
        raise ValueError("velocity cannot equal wave_speed (sonic barrier).")

    return source_freq * (wave_speed / denominator)


# ========== INFORMATION THEORY / TELECOM ==========


def shannon_capacity(
    bandwidth: Union[int, float], snr: Union[int, float],
) -> float:
    """Calculate Shannon channel capacity.

    Description:
        C = B × log₂(1 + SNR). Theoretical maximum data rate for a
        communication channel with given bandwidth and signal-to-noise ratio.

    Args:
        bandwidth: Channel bandwidth in hertz (must be positive).
        snr: Signal-to-noise ratio (linear, not dB; must be non-negative).

    Returns:
        float: Channel capacity in bits per second.

    Raises:
        ValueError: If bandwidth is not positive or SNR is negative.

    Example:
        >>> round(shannon_capacity(1e6, 100), 0)
        6658211.0

    Complexity: O(1)
    """
    if not isinstance(bandwidth, (int, float)) or bandwidth <= 0:
        raise ValueError("bandwidth must be positive.")

    if not isinstance(snr, (int, float)) or snr < 0:
        raise ValueError("snr must be non-negative.")

    return bandwidth * math.log2(1 + snr)


def thermal_noise(
    bandwidth: Union[int, float], temperature: Union[int, float] = 290.0,
) -> float:
    """Calculate Johnson-Nyquist thermal noise power.

    Description:
        P = kB × T × B, where kB is the Boltzmann constant.
        Fundamental noise floor in electronic systems.

    Args:
        bandwidth: Bandwidth in hertz (must be positive).
        temperature: Absolute temperature in kelvin (default: 290 K).

    Returns:
        float: Noise power in watts.

    Raises:
        ValueError: If bandwidth or temperature is not positive.

    Example:
        >>> thermal_noise(1e6, 290)
        4.00388105e-15

    Complexity: O(1)
    """
    if not isinstance(bandwidth, (int, float)) or bandwidth <= 0:
        raise ValueError("bandwidth must be positive.")

    if not isinstance(temperature, (int, float)) or temperature <= 0:
        raise ValueError("temperature must be positive.")

    k_b = 1.380649e-23
    return k_b * temperature * bandwidth


def free_space_path_loss(
    freq: Union[int, float], distance: Union[int, float],
) -> float:
    """Calculate free-space path loss in decibels.

    Description:
        FSPL(dB) = 20·log₁₀(d) + 20·log₁₀(f) + 20·log₁₀(4π/c).
        Used for radio link budget planning.

    Args:
        freq: Frequency in hertz (must be positive).
        distance: Distance in meters (must be positive).

    Returns:
        float: Path loss in decibels.

    Raises:
        ValueError: If freq or distance is not positive.

    Example:
        >>> round(free_space_path_loss(2.4e9, 100), 2)
        80.05

    Complexity: O(1)
    """
    if not isinstance(freq, (int, float)) or freq <= 0:
        raise ValueError("freq must be positive.")

    if not isinstance(distance, (int, float)) or distance <= 0:
        raise ValueError("distance must be positive.")

    c = 299792458.0
    return (
        20 * math.log10(distance)
        + 20 * math.log10(freq)
        + 20 * math.log10(4 * math.pi / c)
    )


def friis_transmission(
    pt: Union[int, float],
    gt: Union[int, float],
    gr: Union[int, float],
    wavelength_m: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Calculate received power using the Friis transmission equation.

    Description:
        Pr = Pt × Gt × Gr × (λ / (4πd))².
        Fundamental equation for free-space radio link budget.

    Args:
        pt: Transmitted power in watts (must be positive).
        gt: Transmit antenna gain (linear, not dB).
        gr: Receive antenna gain (linear, not dB).
        wavelength_m: Signal wavelength in meters (must be positive).
        distance: Distance between antennas in meters (must be positive).

    Returns:
        float: Received power in watts.

    Raises:
        ValueError: If any parameter is not positive.

    Example:
        >>> round(friis_transmission(1.0, 1.0, 1.0, 0.03, 1000), 12)
        6e-12

    Complexity: O(1)
    """
    if any(
        not isinstance(v, (int, float)) or v <= 0
        for v in [pt, gt, gr, wavelength_m, distance]
    ):
        raise ValueError("All parameters must be positive numbers.")

    return pt * gt * gr * (wavelength_m / (4 * math.pi * distance)) ** 2


# ========== ELECTRICAL ENGINEERING ==========


def impedance_series(
    r: Union[int, float],
    l: Union[int, float],  # noqa: E741 — standard RLC notation
    c: Union[int, float],
    freq: Union[int, float],
) -> complex:
    """Calculate impedance of a series RLC circuit.

    Description:
        Z = R + j(2πfL − 1/(2πfC)).

    Args:
        r: Resistance in ohms.
        l: Inductance in henrys.
        c: Capacitance in farads (must be positive).
        freq: Frequency in hertz (must be positive).

    Returns:
        complex: Impedance in ohms.

    Raises:
        ValueError: If freq or c is not positive.

    Example:
        >>> z = impedance_series(100, 0.01, 1e-6, 1000)
        >>> round(z.real, 2)
        100.0

    Complexity: O(1)
    """
    if not isinstance(freq, (int, float)) or freq <= 0:
        raise ValueError("freq must be positive.")

    if not isinstance(c, (int, float)) or c <= 0:
        raise ValueError("c (capacitance) must be positive.")

    omega = 2 * math.pi * freq
    x_l = omega * l
    x_c = 1 / (omega * c)
    return complex(r, x_l - x_c)


def impedance_parallel(z1: complex, z2: complex) -> complex:
    """Calculate parallel combination of two impedances.

    Description:
        Z_total = (Z1 × Z2) / (Z1 + Z2).

    Args:
        z1: First impedance (complex, in ohms).
        z2: Second impedance (complex, in ohms).

    Returns:
        complex: Equivalent parallel impedance.

    Raises:
        ValueError: If sum of impedances is zero.

    Example:
        >>> impedance_parallel(100+0j, 100+0j)
        (50+0j)

    Complexity: O(1)
    """
    total = z1 + z2

    if abs(total) == 0:
        raise ValueError("Sum of impedances must not be zero.")

    return (z1 * z2) / total


def resonant_freq(
    l: Union[int, float], c: Union[int, float],  # noqa: E741 — standard LC notation
) -> float:
    """Calculate resonant frequency of an LC circuit.

    Description:
        f = 1 / (2π√(LC)).

    Args:
        l: Inductance in henrys (must be positive).
        c: Capacitance in farads (must be positive).

    Returns:
        float: Resonant frequency in hertz.

    Raises:
        ValueError: If l or c is not positive.

    Example:
        >>> round(resonant_freq(0.01, 1e-6), 2)
        1591.55

    Complexity: O(1)
    """
    if not isinstance(l, (int, float)) or l <= 0:
        raise ValueError("l (inductance) must be positive.")

    if not isinstance(c, (int, float)) or c <= 0:
        raise ValueError("c (capacitance) must be positive.")

    return 1 / (2 * math.pi * math.sqrt(l * c))


def skin_depth(
    freq: Union[int, float],
    resistivity: Union[int, float],
    permeability: Union[int, float] = 1.2566370614359173e-06,
) -> float:
    """Calculate skin depth in a conductor.

    Description:
        δ = √(2ρ / (ωμ)). Determines how far AC penetrates a conductor.

    Args:
        freq: Frequency in hertz (must be positive).
        resistivity: Electrical resistivity in ohm-meters (must be positive).
        permeability: Magnetic permeability in H/m (default: μ₀).

    Returns:
        float: Skin depth in meters.

    Raises:
        ValueError: If any parameter is not positive.

    Example:
        >>> round(skin_depth(1e6, 1.68e-8), 6)
        6.5e-05

    Complexity: O(1)
    """
    if any(
        not isinstance(v, (int, float)) or v <= 0
        for v in [freq, resistivity, permeability]
    ):
        raise ValueError("All parameters must be positive.")

    omega = 2 * math.pi * freq
    return math.sqrt(2 * resistivity / (omega * permeability))


def temperature_convert(
    value: Union[int, float],
    from_unit: str,
    to_unit: str,
) -> float:
    """Converts a temperature between Celsius, Fahrenheit, and Kelvin.

    Args:
        value: The temperature value.
        from_unit: Source unit ("C", "F", or "K").
        to_unit: Target unit ("C", "F", or "K").

    Returns:
        The converted temperature.

    Raises:
        TypeError: If value is not numeric.
        ValueError: If units are invalid or result is below absolute zero.

    Example:
        >>> temperature_convert(100, "C", "F")
        212.0
        >>> temperature_convert(32, "F", "C")
        0.0
        >>> temperature_convert(0, "C", "K")
        273.15

    Complexity: O(1)
    """
    if not isinstance(value, (int, float)):
        raise TypeError("value must be numeric.")

    valid = {"C", "F", "K"}

    if from_unit not in valid or to_unit not in valid:
        raise ValueError(f"Units must be one of {valid}.")

    if from_unit == to_unit:
        return float(value)

    # Convert to Celsius first
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    else:
        celsius = value - 273.15

    # Convert from Celsius to target
    if to_unit == "C":
        result = celsius
    elif to_unit == "F":
        result = celsius * 9 / 5 + 32
    else:
        result = celsius + 273.15

    if to_unit == "K" and result < 0:
        raise ValueError("Result is below absolute zero.")

    return float(result)


def angle_convert(
    value: Union[int, float],
    from_unit: str,
    to_unit: str,
) -> float:
    """Converts an angle between degrees, radians, and gradians.

    Args:
        value: The angle value.
        from_unit: Source unit ("deg", "rad", or "grad").
        to_unit: Target unit ("deg", "rad", or "grad").

    Returns:
        The converted angle.

    Raises:
        TypeError: If value is not numeric.
        ValueError: If units are invalid.

    Example:
        >>> import math
        >>> angle_convert(180, "deg", "rad") == math.pi
        True
        >>> angle_convert(200, "grad", "deg")
        180.0

    Complexity: O(1)
    """
    if not isinstance(value, (int, float)):
        raise TypeError("value must be numeric.")

    valid = {"deg", "rad", "grad"}

    if from_unit not in valid or to_unit not in valid:
        raise ValueError(f"Units must be one of {valid}.")

    if from_unit == to_unit:
        return float(value)

    # Convert to degrees first
    if from_unit == "deg":
        degrees = value
    elif from_unit == "rad":
        degrees = math.degrees(value)
    else:
        degrees = value * 0.9

    # Convert from degrees to target
    if to_unit == "deg":
        return float(degrees)
    elif to_unit == "rad":
        return math.radians(degrees)
    else:
        return float(degrees / 0.9)


def coordinate_dms_to_decimal(
    degrees: int,
    minutes: int,
    seconds: Union[int, float],
    direction: str = "N",
) -> float:
    """Converts geographic coordinates from DMS to decimal degrees.

    Args:
        degrees: Degree component (0–180 for lon, 0–90 for lat).
        minutes: Minutes component (0–59).
        seconds: Seconds component (0–59.999…).
        direction: Cardinal direction ("N", "S", "E", "W").

    Returns:
        Decimal degrees (negative for S and W).

    Raises:
        TypeError: If degrees/minutes are not ints or seconds not numeric.
        ValueError: If components are out of range or direction invalid.

    Example:
        >>> round(coordinate_dms_to_decimal(40, 26, 46, "N"), 4)
        40.4461
        >>> round(coordinate_dms_to_decimal(79, 58, 56, "W"), 4)
        -79.9822

    Complexity: O(1)
    """
    if not isinstance(degrees, int) or not isinstance(minutes, int):
        raise TypeError("degrees and minutes must be integers.")

    if not isinstance(seconds, (int, float)):
        raise TypeError("seconds must be numeric.")

    direction = direction.upper()

    if direction not in {"N", "S", "E", "W"}:
        raise ValueError("direction must be one of 'N', 'S', 'E', 'W'.")

    if degrees < 0 or minutes < 0 or seconds < 0:
        raise ValueError("DMS components must be non-negative.")

    if minutes >= 60 or seconds >= 60:
        raise ValueError("minutes and seconds must be < 60.")

    decimal = degrees + minutes / 60 + seconds / 3600

    if direction in {"S", "W"}:
        decimal = -decimal

    return float(decimal)


def coordinate_decimal_to_dms(
    decimal_degrees: Union[int, float],
    is_longitude: bool = False,
) -> tuple:
    """Converts decimal degrees to DMS (degrees, minutes, seconds, direction).

    Args:
        decimal_degrees: The coordinate in decimal degrees.
        is_longitude: True for longitude (E/W), False for latitude (N/S).

    Returns:
        A tuple (degrees, minutes, seconds, direction).

    Raises:
        TypeError: If decimal_degrees is not numeric.
        ValueError: If latitude not in [-90,90] or longitude not in [-180,180].

    Example:
        >>> coordinate_decimal_to_dms(40.4461)
        (40, 26, 45.96, 'N')
        >>> coordinate_decimal_to_dms(-79.9822, is_longitude=True)
        (79, 58, 55.92, 'W')

    Complexity: O(1)
    """
    if not isinstance(decimal_degrees, (int, float)):
        raise TypeError("decimal_degrees must be numeric.")

    limit = 180 if is_longitude else 90

    if abs(decimal_degrees) > limit:
        kind = "Longitude" if is_longitude else "Latitude"
        raise ValueError(f"{kind} must be in [-{limit}, {limit}].")

    if is_longitude:
        direction = "E" if decimal_degrees >= 0 else "W"
    else:
        direction = "N" if decimal_degrees >= 0 else "S"

    dd = abs(decimal_degrees)
    deg = int(dd)
    minutes_full = (dd - deg) * 60
    mins = int(minutes_full)
    secs = round((minutes_full - mins) * 60, 2)

    return (deg, mins, secs, direction)


# ---------------------------------------------------------------------------
# Pressure / Energy / Speed conversions
# ---------------------------------------------------------------------------

_PRESSURE_TO_PA: dict = {
    "pa": 1.0,
    "hpa": 100.0,
    "kpa": 1_000.0,
    "mpa": 1_000_000.0,
    "bar": 100_000.0,
    "mbar": 100.0,
    "atm": 101_325.0,
    "torr": 133.322368421,
    "mmhg": 133.322368421,
    "psi": 6_894.757293168,
    "inhg": 3_386.389,
}


def pressure_convert(
    value: Union[int, float],
    from_unit: str,
    to_unit: str,
) -> float:
    """Converts a pressure value between common units.

    Supported units: pa, hpa, kpa, mpa, bar, mbar, atm, torr, mmhg, psi, inhg.

    Args:
        value: The numeric value to convert.
        from_unit: Source unit (case-insensitive).
        to_unit: Target unit (case-insensitive).

    Returns:
        The converted pressure value.

    Raises:
        TypeError: If value is not numeric or units are not strings.
        ValueError: If a unit is not recognised.

    Example:
        >>> round(pressure_convert(1, 'atm', 'psi'), 4)
        14.696

    Complexity: O(1)
    """
    if not isinstance(value, (int, float)):
        raise TypeError("value must be numeric.")

    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Units must be strings.")

    fu = from_unit.strip().lower()
    tu = to_unit.strip().lower()

    if fu not in _PRESSURE_TO_PA:
        raise ValueError(f"Unknown source unit: {from_unit}")

    if tu not in _PRESSURE_TO_PA:
        raise ValueError(f"Unknown target unit: {to_unit}")

    return value * _PRESSURE_TO_PA[fu] / _PRESSURE_TO_PA[tu]


_ENERGY_TO_J: dict = {
    "j": 1.0,
    "kj": 1_000.0,
    "mj": 1_000_000.0,
    "cal": 4.184,
    "kcal": 4_184.0,
    "wh": 3_600.0,
    "kwh": 3_600_000.0,
    "btu": 1_055.06,
    "ev": 1.602176634e-19,
    "ft_lbf": 1.355818,
    "erg": 1e-7,
}


def energy_convert(
    value: Union[int, float],
    from_unit: str,
    to_unit: str,
) -> float:
    """Converts an energy value between common units.

    Supported units: j, kj, mj, cal, kcal, wh, kwh, btu, ev, ft_lbf, erg.

    Args:
        value: The numeric value to convert.
        from_unit: Source unit (case-insensitive).
        to_unit: Target unit (case-insensitive).

    Returns:
        The converted energy value.

    Raises:
        TypeError: If value is not numeric or units are not strings.
        ValueError: If a unit is not recognised.

    Example:
        >>> round(energy_convert(1, 'kwh', 'j'))
        3600000

    Complexity: O(1)
    """
    if not isinstance(value, (int, float)):
        raise TypeError("value must be numeric.")

    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Units must be strings.")

    fu = from_unit.strip().lower()
    tu = to_unit.strip().lower()

    if fu not in _ENERGY_TO_J:
        raise ValueError(f"Unknown source unit: {from_unit}")

    if tu not in _ENERGY_TO_J:
        raise ValueError(f"Unknown target unit: {to_unit}")

    return value * _ENERGY_TO_J[fu] / _ENERGY_TO_J[tu]


_SPEED_TO_MS: dict = {
    "m/s": 1.0,
    "km/h": 1.0 / 3.6,
    "mph": 0.44704,
    "ft/s": 0.3048,
    "knot": 0.514444,
    "mach": 343.0,
    "c": 299_792_458.0,
}


def speed_convert(
    value: Union[int, float],
    from_unit: str,
    to_unit: str,
) -> float:
    """Converts a speed value between common units.

    Supported units: m/s, km/h, mph, ft/s, knot, mach, c.

    Args:
        value: The numeric value to convert.
        from_unit: Source unit (case-insensitive).
        to_unit: Target unit (case-insensitive).

    Returns:
        The converted speed value.

    Raises:
        TypeError: If value is not numeric or units are not strings.
        ValueError: If a unit is not recognised.

    Example:
        >>> round(speed_convert(100, 'km/h', 'mph'), 4)
        62.1371

    Complexity: O(1)
    """
    if not isinstance(value, (int, float)):
        raise TypeError("value must be numeric.")

    if not isinstance(from_unit, str) or not isinstance(to_unit, str):
        raise TypeError("Units must be strings.")

    fu = from_unit.strip().lower()
    tu = to_unit.strip().lower()

    if fu not in _SPEED_TO_MS:
        raise ValueError(f"Unknown source unit: {from_unit}")

    if tu not in _SPEED_TO_MS:
        raise ValueError(f"Unknown target unit: {to_unit}")

    return value * _SPEED_TO_MS[fu] / _SPEED_TO_MS[tu]


# ---------------------------------------------------------------------------
# Physics / Engineering scalar functions
# ---------------------------------------------------------------------------

_COULOMB_CONSTANT: float = 8.9875517873681764e9  # N⋅m²/C²
_GRAVITATIONAL_CONSTANT: float = 6.67430e-11  # m³/(kg⋅s²)
_SPEED_OF_LIGHT: float = 299_792_458.0  # m/s


def ohms_law(
    voltage: Union[int, float, None] = None,
    current: Union[int, float, None] = None,
    resistance: Union[int, float, None] = None,
) -> float:
    """Solves Ohm's law V = I × R for the missing variable.

    Provide exactly two of the three parameters; the third is computed.

    Args:
        voltage: Voltage in volts (V).
        current: Current in amperes (A).
        resistance: Resistance in ohms (Ω).

    Returns:
        The missing quantity.

    Raises:
        TypeError: If provided values are not numeric.
        ValueError: If not exactly two parameters are supplied, or divisor is zero.

    Example:
        >>> ohms_law(voltage=12, resistance=4)
        3.0

    Complexity: O(1)
    """
    given = [(n, v) for n, v in [("voltage", voltage), ("current", current), ("resistance", resistance)] if v is not None]

    if len(given) != 2:
        raise ValueError("Provide exactly two of voltage, current, resistance.")

    for name, val in given:

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if voltage is None:
        return current * resistance  # type: ignore[operator]

    if current is None:

        if resistance == 0:
            raise ValueError("resistance must not be zero when solving for current.")

        return voltage / resistance  # type: ignore[operator]

    # resistance is None
    if current == 0:
        raise ValueError("current must not be zero when solving for resistance.")

    return voltage / current  # type: ignore[operator]


def coulombs_law(
    q1: Union[int, float],
    q2: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Computes electrostatic force via Coulomb's law.

    F = k × |q1 × q2| / d².

    Args:
        q1: Charge 1 in coulombs.
        q2: Charge 2 in coulombs.
        distance: Distance between charges in metres (must be positive).

    Returns:
        Force magnitude in newtons.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If distance is zero or negative.

    Example:
        >>> round(coulombs_law(1e-6, 2e-6, 0.05), 4)
        7.19

    Complexity: O(1)
    """
    if not isinstance(q1, (int, float)):
        raise TypeError("q1 must be numeric.")

    if not isinstance(q2, (int, float)):
        raise TypeError("q2 must be numeric.")

    if not isinstance(distance, (int, float)):
        raise TypeError("distance must be numeric.")

    if distance <= 0:
        raise ValueError("distance must be positive.")

    return _COULOMB_CONSTANT * abs(q1 * q2) / (distance * distance)


def gravitational_force(
    m1: Union[int, float],
    m2: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Computes gravitational force via Newton's law.

    F = G × m1 × m2 / d².

    Args:
        m1: Mass 1 in kilograms.
        m2: Mass 2 in kilograms.
        distance: Distance between centres in metres (must be positive).

    Returns:
        Force in newtons.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If distance is zero or negative, or masses are negative.

    Example:
        >>> round(gravitational_force(5.972e24, 80, 6.371e6), 2)
        789.54

    Complexity: O(1)
    """
    if not isinstance(m1, (int, float)):
        raise TypeError("m1 must be numeric.")

    if not isinstance(m2, (int, float)):
        raise TypeError("m2 must be numeric.")

    if not isinstance(distance, (int, float)):
        raise TypeError("distance must be numeric.")

    if m1 < 0 or m2 < 0:
        raise ValueError("Masses must be non-negative.")

    if distance <= 0:
        raise ValueError("distance must be positive.")

    return _GRAVITATIONAL_CONSTANT * m1 * m2 / (distance * distance)


def kinetic_energy(
    mass: Union[int, float],
    velocity: Union[int, float],
) -> float:
    """Computes kinetic energy.

    KE = 0.5 × m × v².

    Args:
        mass: Mass in kilograms (non-negative).
        velocity: Velocity in m/s.

    Returns:
        Kinetic energy in joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass is negative.

    Example:
        >>> kinetic_energy(10, 3)
        45.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be numeric.")

    if not isinstance(velocity, (int, float)):
        raise TypeError("velocity must be numeric.")

    if mass < 0:
        raise ValueError("mass must be non-negative.")

    return 0.5 * mass * velocity * velocity


def potential_energy(
    mass: Union[int, float],
    height: Union[int, float],
    g: Union[int, float] = 9.80665,
) -> float:
    """Computes gravitational potential energy.

    PE = m × g × h.

    Args:
        mass: Mass in kilograms (non-negative).
        height: Height in metres.
        g: Gravitational acceleration (default 9.80665 m/s²).

    Returns:
        Potential energy in joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass is negative.

    Example:
        >>> round(potential_energy(10, 5), 4)
        490.3325

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be numeric.")

    if not isinstance(height, (int, float)):
        raise TypeError("height must be numeric.")

    if not isinstance(g, (int, float)):
        raise TypeError("g must be numeric.")

    if mass < 0:
        raise ValueError("mass must be non-negative.")

    return mass * g * height


def escape_velocity(
    mass: Union[int, float],
    radius: Union[int, float],
) -> float:
    """Computes the escape velocity from a celestial body.

    v = √(2 × G × M / r).

    Args:
        mass: Mass of the body in kilograms.
        radius: Radius (distance from centre) in metres (must be positive).

    Returns:
        Escape velocity in m/s.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass is negative or radius is not positive.

    Example:
        >>> round(escape_velocity(5.972e24, 6.371e6), 0)
        11185.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be numeric.")

    if not isinstance(radius, (int, float)):
        raise TypeError("radius must be numeric.")

    if mass < 0:
        raise ValueError("mass must be non-negative.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    return math.sqrt(2 * _GRAVITATIONAL_CONSTANT * mass / radius)


def snells_law(
    n1: Union[int, float],
    theta1: Union[int, float],
    n2: Union[int, float],
) -> float:
    """Computes the refraction angle via Snell's law.

    n1 × sin(θ1) = n2 × sin(θ2) → θ2 = arcsin(n1 × sin(θ1) / n2).

    Args:
        n1: Refractive index of first medium.
        theta1: Angle of incidence in radians.
        n2: Refractive index of second medium (must be positive).

    Returns:
        Angle of refraction in radians.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If n2 is not positive or total internal reflection occurs.

    Example:
        >>> import math
        >>> round(snells_law(1.0, math.radians(30), 1.5), 6)
        0.339837

    Complexity: O(1)
    """
    if not isinstance(n1, (int, float)):
        raise TypeError("n1 must be numeric.")

    if not isinstance(theta1, (int, float)):
        raise TypeError("theta1 must be numeric.")

    if not isinstance(n2, (int, float)):
        raise TypeError("n2 must be numeric.")

    if n2 <= 0:
        raise ValueError("n2 must be positive.")

    sin_theta2 = n1 * math.sin(theta1) / n2

    if abs(sin_theta2) > 1:
        raise ValueError("Total internal reflection — no refracted ray.")

    return math.asin(sin_theta2)


def bmi(
    weight_kg: Union[int, float],
    height_m: Union[int, float],
) -> float:
    """Calculate Body Mass Index (BMI).

    Args:
        weight_kg: Weight in kilograms.
        height_m: Height in meters.

    Returns:
        BMI value as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If weight_kg or height_m is not positive.

    Example:
        >>> round(bmi(70, 1.75), 2)
        22.86

    Complexity: O(1)
    """
    if not isinstance(weight_kg, (int, float)):
        raise TypeError("weight_kg must be numeric.")

    if not isinstance(height_m, (int, float)):
        raise TypeError("height_m must be numeric.")

    if weight_kg <= 0:
        raise ValueError("weight_kg must be positive.")

    if height_m <= 0:
        raise ValueError("height_m must be positive.")

    return weight_kg / (height_m ** 2)


def wind_chill(
    temperature_c: Union[int, float],
    wind_speed_kmh: Union[int, float],
) -> float:
    """Calculate wind chill index using the North American formula.

    Valid for temperatures at or below 10 °C and wind speeds above 4.8 km/h.

    Args:
        temperature_c: Air temperature in Celsius.
        wind_speed_kmh: Wind speed in km/h.

    Returns:
        Wind chill temperature in Celsius.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If temperature > 10 or wind speed <= 4.8.

    Example:
        >>> round(wind_chill(-5, 30), 2)
        -13.0

    Complexity: O(1)
    """
    if not isinstance(temperature_c, (int, float)):
        raise TypeError("temperature_c must be numeric.")

    if not isinstance(wind_speed_kmh, (int, float)):
        raise TypeError("wind_speed_kmh must be numeric.")

    if temperature_c > 10:
        raise ValueError("temperature_c must be at most 10 °C.")

    if wind_speed_kmh <= 4.8:
        raise ValueError("wind_speed_kmh must be greater than 4.8 km/h.")

    v_exp = wind_speed_kmh ** 0.16
    return 13.12 + 0.6215 * temperature_c - 11.37 * v_exp + 0.3965 * temperature_c * v_exp


def heat_index(
    temperature_c: Union[int, float],
    relative_humidity: Union[int, float],
) -> float:
    """Calculate heat index (feels-like temperature) in Celsius.

    Uses the Rothfusz regression equation.

    Args:
        temperature_c: Air temperature in Celsius (>= 27).
        relative_humidity: Relative humidity in percent (0-100).

    Returns:
        Heat index in Celsius.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If temperature < 27 or humidity not in [0, 100].

    Example:
        >>> round(heat_index(35, 75), 1)
        53.3

    Complexity: O(1)
    """
    if not isinstance(temperature_c, (int, float)):
        raise TypeError("temperature_c must be numeric.")

    if not isinstance(relative_humidity, (int, float)):
        raise TypeError("relative_humidity must be numeric.")

    if temperature_c < 27:
        raise ValueError("temperature_c must be at least 27 °C.")

    if relative_humidity < 0 or relative_humidity > 100:
        raise ValueError("relative_humidity must be in [0, 100].")

    # Convert to Fahrenheit for the Rothfusz equation
    t = temperature_c * 9 / 5 + 32
    r = relative_humidity

    hi = (
        -42.379
        + 2.04901523 * t
        + 10.14333127 * r
        - 0.22475541 * t * r
        - 0.00683783 * t * t
        - 0.05481717 * r * r
        + 0.00122874 * t * t * r
        + 0.00085282 * t * r * r
        - 0.00000199 * t * t * r * r
    )

    # Convert back to Celsius
    return (hi - 32) * 5 / 9


def dew_point(
    temperature_c: Union[int, float],
    relative_humidity: Union[int, float],
) -> float:
    """Calculate dew point temperature using the Magnus formula.

    Args:
        temperature_c: Air temperature in Celsius.
        relative_humidity: Relative humidity in percent (0-100).

    Returns:
        Dew point in Celsius.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If humidity not in (0, 100].

    Example:
        >>> round(dew_point(25, 50), 2)
        13.84

    Complexity: O(1)
    """
    if not isinstance(temperature_c, (int, float)):
        raise TypeError("temperature_c must be numeric.")

    if not isinstance(relative_humidity, (int, float)):
        raise TypeError("relative_humidity must be numeric.")

    if relative_humidity <= 0 or relative_humidity > 100:
        raise ValueError("relative_humidity must be in (0, 100].")

    a = 17.27
    b = 237.7
    alpha = (a * temperature_c) / (b + temperature_c) + math.log(relative_humidity / 100)

    return (b * alpha) / (a - alpha)


def decibel_add(
    db1: Union[int, float],
    db2: Union[int, float],
) -> float:
    """Add two sound levels in decibels.

    The result accounts for logarithmic combination of sound intensities.

    Args:
        db1: First sound level in dB.
        db2: Second sound level in dB.

    Returns:
        Combined sound level in dB.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> round(decibel_add(90, 90), 2)
        93.01

    Complexity: O(1)
    """
    if not isinstance(db1, (int, float)):
        raise TypeError("db1 must be numeric.")

    if not isinstance(db2, (int, float)):
        raise TypeError("db2 must be numeric.")

    return 10 * math.log10(10 ** (db1 / 10) + 10 ** (db2 / 10))


def terminal_velocity(
    mass: Union[int, float],
    drag_coefficient: Union[int, float],
    area: Union[int, float],
    air_density: Union[int, float] = 1.225,
) -> float:
    """Calculate terminal velocity of a falling object.

    v = sqrt(2 * m * g / (Cd * A * rho))

    Args:
        mass: Object mass in kg.
        drag_coefficient: Dimensionless drag coefficient.
        area: Cross-sectional area in m².
        air_density: Air density in kg/m³ (default 1.225 at sea level).

    Returns:
        Terminal velocity in m/s.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any input is not positive.

    Example:
        >>> round(terminal_velocity(80, 1.0, 0.7), 2)
        42.78

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be numeric.")

    if not isinstance(drag_coefficient, (int, float)):
        raise TypeError("drag_coefficient must be numeric.")

    if not isinstance(area, (int, float)):
        raise TypeError("area must be numeric.")

    if not isinstance(air_density, (int, float)):
        raise TypeError("air_density must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    if drag_coefficient <= 0:
        raise ValueError("drag_coefficient must be positive.")

    if area <= 0:
        raise ValueError("area must be positive.")

    if air_density <= 0:
        raise ValueError("air_density must be positive.")

    g = 9.80665
    return math.sqrt(2 * mass * g / (drag_coefficient * area * air_density))


def elastic_modulus(
    stress: Union[int, float],
    strain: Union[int, float],
) -> float:
    """Calculate Young's modulus (elastic modulus): E = stress / strain.

    Args:
        stress: Applied stress in Pascals.
        strain: Resulting strain (dimensionless, > 0).

    Returns:
        Young's modulus in Pascals.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If strain is zero.

    Example:
        >>> elastic_modulus(200e6, 0.001)
        200000000000.0

    Complexity: O(1)
    """
    if not isinstance(stress, (int, float)):
        raise TypeError("stress must be numeric.")

    if not isinstance(strain, (int, float)):
        raise TypeError("strain must be numeric.")

    if strain == 0:
        raise ValueError("strain must not be zero.")

    return float(stress / strain)


def hookes_law(
    spring_constant: Union[int, float],
    displacement: Union[int, float],
) -> float:
    """Calculate the restoring force of a spring using Hooke's law: F = -k * x.

    Args:
        spring_constant: Spring constant k in N/m (positive).
        displacement: Displacement x in meters.

    Returns:
        Restoring force in Newtons (negative sign indicates opposite direction).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If spring_constant is not positive.

    Example:
        >>> hookes_law(100, 0.05)
        -5.0

    Complexity: O(1)
    """
    if not isinstance(spring_constant, (int, float)):
        raise TypeError("spring_constant must be numeric.")

    if not isinstance(displacement, (int, float)):
        raise TypeError("displacement must be numeric.")

    if spring_constant <= 0:
        raise ValueError("spring_constant must be positive.")

    return float(-spring_constant * displacement)


def ideal_gas_pressure(
    moles: Union[int, float],
    temperature_k: Union[int, float],
    volume_m3: Union[int, float],
) -> float:
    """Calculate pressure using the ideal gas law: P = nRT / V.

    Args:
        moles: Amount of substance in moles.
        temperature_k: Temperature in Kelvin.
        volume_m3: Volume in cubic meters.

    Returns:
        Pressure in Pascals.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any input is not positive.

    Example:
        >>> round(ideal_gas_pressure(1, 273.15, 0.0224), 0)
        101388.0

    Complexity: O(1)
    """
    if not isinstance(moles, (int, float)):
        raise TypeError("moles must be numeric.")

    if not isinstance(temperature_k, (int, float)):
        raise TypeError("temperature_k must be numeric.")

    if not isinstance(volume_m3, (int, float)):
        raise TypeError("volume_m3 must be numeric.")

    if moles <= 0:
        raise ValueError("moles must be positive.")

    if temperature_k <= 0:
        raise ValueError("temperature_k must be positive.")

    if volume_m3 <= 0:
        raise ValueError("volume_m3 must be positive.")

    R = 8.314462618  # J/(mol·K)
    return moles * R * temperature_k / volume_m3


def momentum(
    mass: Union[int, float],
    velocity: Union[int, float],
) -> float:
    """Calculate linear momentum: p = m * v.

    Args:
        mass: Mass in kg.
        velocity: Velocity in m/s (can be negative for direction).

    Returns:
        Momentum in kg·m/s.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass is not positive.

    Example:
        >>> momentum(10, 5)
        50.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be numeric.")

    if not isinstance(velocity, (int, float)):
        raise TypeError("velocity must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    return float(mass * velocity)


def impulse(
    force: Union[int, float],
    time_seconds: Union[int, float],
) -> float:
    """Calculate impulse: J = F * Δt.

    Args:
        force: Applied force in Newtons.
        time_seconds: Duration in seconds.

    Returns:
        Impulse in Newton-seconds (N·s).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If time_seconds is not positive.

    Example:
        >>> impulse(100, 0.5)
        50.0

    Complexity: O(1)
    """
    if not isinstance(force, (int, float)):
        raise TypeError("force must be numeric.")

    if not isinstance(time_seconds, (int, float)):
        raise TypeError("time_seconds must be numeric.")

    if time_seconds <= 0:
        raise ValueError("time_seconds must be positive.")

    return float(force * time_seconds)


def wave_speed(
    frequency: Union[int, float],
    wavelength_m: Union[int, float],
) -> float:
    """Calculate wave speed: v = f * λ.

    Args:
        frequency: Wave frequency in Hz.
        wavelength_m: Wavelength in meters.

    Returns:
        Wave speed in m/s.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If either input is not positive.

    Example:
        >>> wave_speed(440, 0.78)
        343.2

    Complexity: O(1)
    """
    if not isinstance(frequency, (int, float)):
        raise TypeError("frequency must be numeric.")

    if not isinstance(wavelength_m, (int, float)):
        raise TypeError("wavelength_m must be numeric.")

    if frequency <= 0:
        raise ValueError("frequency must be positive.")

    if wavelength_m <= 0:
        raise ValueError("wavelength_m must be positive.")

    return float(frequency * wavelength_m)


def reynolds_number(
    density: Union[int, float],
    velocity: Union[int, float],
    length: Union[int, float],
    viscosity: Union[int, float],
) -> float:
    """Calculate the Reynolds number: Re = ρ * v * L / μ.

    Predicts flow patterns: laminar (Re < 2300) or turbulent (Re > 4000).

    Args:
        density: Fluid density in kg/m³.
        velocity: Flow velocity in m/s.
        length: Characteristic length in meters.
        viscosity: Dynamic viscosity in Pa·s.

    Returns:
        Reynolds number (dimensionless).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If density, length, or viscosity is not positive.

    Example:
        >>> reynolds_number(1000, 1, 0.01, 0.001)
        10000.0

    Complexity: O(1)
    """
    if not isinstance(density, (int, float)):
        raise TypeError("density must be numeric.")

    if not isinstance(velocity, (int, float)):
        raise TypeError("velocity must be numeric.")

    if not isinstance(length, (int, float)):
        raise TypeError("length must be numeric.")

    if not isinstance(viscosity, (int, float)):
        raise TypeError("viscosity must be numeric.")

    if density <= 0:
        raise ValueError("density must be positive.")

    if length <= 0:
        raise ValueError("length must be positive.")

    if viscosity <= 0:
        raise ValueError("viscosity must be positive.")

    return float(density * velocity * length / viscosity)


def mach_number(
    velocity: Union[int, float],
    speed_of_sound: Union[int, float] = 343.0,
) -> float:
    """Calculate the Mach number: M = v / c.

    Args:
        velocity: Object velocity in m/s.
        speed_of_sound: Speed of sound in the medium in m/s (default 343 for air at 20 °C).

    Returns:
        Mach number (dimensionless).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If speed_of_sound is not positive.

    Example:
        >>> round(mach_number(680), 2)
        1.98

    Complexity: O(1)
    """
    if not isinstance(velocity, (int, float)):
        raise TypeError("velocity must be numeric.")

    if not isinstance(speed_of_sound, (int, float)):
        raise TypeError("speed_of_sound must be numeric.")

    if speed_of_sound <= 0:
        raise ValueError("speed_of_sound must be positive.")

    return float(velocity / speed_of_sound)


def power_physics(
    work: Union[int, float],
    time_seconds: Union[int, float],
) -> float:
    """Calculate mechanical power: P = W / t.

    Args:
        work: Work done in Joules.
        time_seconds: Time interval in seconds.

    Returns:
        Power in Watts.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If time_seconds is not positive.

    Example:
        >>> power_physics(1000, 5)
        200.0

    Complexity: O(1)
    """
    if not isinstance(work, (int, float)):
        raise TypeError("work must be numeric.")

    if not isinstance(time_seconds, (int, float)):
        raise TypeError("time_seconds must be numeric.")

    if time_seconds <= 0:
        raise ValueError("time_seconds must be positive.")

    return float(work / time_seconds)


def specific_heat_energy(
    mass: Union[int, float],
    specific_heat: Union[int, float],
    temperature_change: Union[int, float],
) -> float:
    """Calculate thermal energy: Q = m * c * ΔT.

    Args:
        mass: Mass in kg.
        specific_heat: Specific heat capacity in J/(kg·K).
        temperature_change: Temperature change in Kelvin (or Celsius).

    Returns:
        Thermal energy in Joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass or specific_heat is not positive.

    Example:
        >>> specific_heat_energy(1, 4186, 10)
        41860.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be numeric.")

    if not isinstance(specific_heat, (int, float)):
        raise TypeError("specific_heat must be numeric.")

    if not isinstance(temperature_change, (int, float)):
        raise TypeError("temperature_change must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    if specific_heat <= 0:
        raise ValueError("specific_heat must be positive.")

    return float(mass * specific_heat * temperature_change)


def buoyant_force(
    fluid_density: Union[int, float],
    displaced_volume: Union[int, float],
    gravity: Union[int, float] = 9.80665,
) -> float:
    """Calculate buoyant force using Archimedes' principle: F = ρ * V * g.

    Args:
        fluid_density: Density of the fluid in kg/m³.
        displaced_volume: Volume of fluid displaced in m³.
        gravity: Gravitational acceleration in m/s² (default 9.80665).

    Returns:
        Buoyant force in Newtons.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If fluid_density or displaced_volume is not positive.

    Example:
        >>> round(buoyant_force(1000, 0.01), 2)
        98.07

    Complexity: O(1)
    """
    if not isinstance(fluid_density, (int, float)):
        raise TypeError("fluid_density must be numeric.")

    if not isinstance(displaced_volume, (int, float)):
        raise TypeError("displaced_volume must be numeric.")

    if not isinstance(gravity, (int, float)):
        raise TypeError("gravity must be numeric.")

    if fluid_density <= 0:
        raise ValueError("fluid_density must be positive.")

    if displaced_volume <= 0:
        raise ValueError("displaced_volume must be positive.")

    return float(fluid_density * displaced_volume * gravity)


def friction_force(
    normal_force: Union[int, float],
    coefficient: Union[int, float],
) -> float:
    """Calculate friction force: F_f = μ * N.

    Args:
        normal_force: Normal force in Newtons.
        coefficient: Coefficient of friction (static or kinetic).

    Returns:
        Friction force in Newtons.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If coefficient is negative.

    Example:
        >>> friction_force(100, 0.5)
        50.0

    Complexity: O(1)
    """
    if not isinstance(normal_force, (int, float)):
        raise TypeError("normal_force must be numeric.")

    if not isinstance(coefficient, (int, float)):
        raise TypeError("coefficient must be numeric.")

    if coefficient < 0:
        raise ValueError("coefficient must be non-negative.")

    return float(abs(normal_force) * coefficient)


def photon_energy(
    frequency: Union[int, float],
) -> float:
    """Calculate the energy of a photon: E = h * f.

    Args:
        frequency: Frequency in Hz.

    Returns:
        Energy in Joules.

    Raises:
        TypeError: If frequency is not numeric.
        ValueError: If frequency is not positive.

    Example:
        >>> round(photon_energy(5e14), 20)
        3.31e-19

    Complexity: O(1)
    """
    if not isinstance(frequency, (int, float)):
        raise TypeError("frequency must be numeric.")

    if frequency <= 0:
        raise ValueError("frequency must be positive.")

    h = 6.62607015e-34  # Planck constant in J·s
    return h * frequency


def de_broglie_wavelength(
    mass: Union[int, float],
    velocity: Union[int, float],
) -> float:
    """Calculate de Broglie wavelength: λ = h / (m * v).

    Args:
        mass: Particle mass in kg.
        velocity: Particle velocity in m/s.

    Returns:
        Wavelength in meters.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass or velocity is not positive.

    Example:
        >>> round(de_broglie_wavelength(9.109e-31, 1e6), 13)
        7.274e-10

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be numeric.")

    if not isinstance(velocity, (int, float)):
        raise TypeError("velocity must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    if velocity <= 0:
        raise ValueError("velocity must be positive.")

    h = 6.62607015e-34
    return h / (mass * velocity)


def focal_length(
    object_distance: Union[int, float],
    image_distance: Union[int, float],
) -> float:
    """Calculate focal length using the thin lens equation: 1/f = 1/do + 1/di.

    Args:
        object_distance: Distance from lens to object in meters.
        image_distance: Distance from lens to image in meters.

    Returns:
        Focal length in meters.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If the sum of reciprocals is zero (no focal point).

    Example:
        >>> round(focal_length(0.3, 0.6), 1)
        0.2

    Complexity: O(1)
    """
    if not isinstance(object_distance, (int, float)):
        raise TypeError("object_distance must be numeric.")

    if not isinstance(image_distance, (int, float)):
        raise TypeError("image_distance must be numeric.")

    if object_distance == 0 or image_distance == 0:
        raise ValueError("distances must not be zero.")

    reciprocal_sum = 1.0 / object_distance + 1.0 / image_distance

    if reciprocal_sum == 0:
        raise ValueError("No finite focal length (parallel rays).")

    return 1.0 / reciprocal_sum


def lens_magnification(
    image_distance: Union[int, float],
    object_distance: Union[int, float],
) -> float:
    """Calculate the magnification of a thin lens: M = -di / do.

    Args:
        image_distance: Distance from lens to image.
        object_distance: Distance from lens to object.

    Returns:
        Magnification (negative = inverted image).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If object_distance is zero.

    Example:
        >>> lens_magnification(0.6, 0.3)
        -2.0

    Complexity: O(1)
    """
    if not isinstance(image_distance, (int, float)):
        raise TypeError("image_distance must be numeric.")

    if not isinstance(object_distance, (int, float)):
        raise TypeError("object_distance must be numeric.")

    if object_distance == 0:
        raise ValueError("object_distance must not be zero.")

    return float(-image_distance / object_distance)


def half_life_remaining(
    initial_quantity: Union[int, float],
    half_life: Union[int, float],
    elapsed_time: Union[int, float],
) -> float:
    """Calculate remaining quantity after radioactive/exponential decay.

    N(t) = N₀ * (1/2)^(t / t½)

    Args:
        initial_quantity: Initial amount.
        half_life: Half-life period (same time units as elapsed_time).
        elapsed_time: Time elapsed.

    Returns:
        Remaining quantity.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If initial_quantity or half_life is not positive, or elapsed_time is negative.

    Example:
        >>> half_life_remaining(100, 5, 10)
        25.0

    Complexity: O(1)
    """
    if not isinstance(initial_quantity, (int, float)):
        raise TypeError("initial_quantity must be numeric.")

    if not isinstance(half_life, (int, float)):
        raise TypeError("half_life must be numeric.")

    if not isinstance(elapsed_time, (int, float)):
        raise TypeError("elapsed_time must be numeric.")

    if initial_quantity <= 0:
        raise ValueError("initial_quantity must be positive.")

    if half_life <= 0:
        raise ValueError("half_life must be positive.")

    if elapsed_time < 0:
        raise ValueError("elapsed_time must be non-negative.")

    return initial_quantity * (0.5 ** (elapsed_time / half_life))


def capacitor_energy(
    capacitance: Union[int, float],
    voltage: Union[int, float],
) -> float:
    """Calculate energy stored in a capacitor: E = 0.5 * C * V².

    Args:
        capacitance: Capacitance in Farads.
        voltage: Voltage across the capacitor in Volts.

    Returns:
        Energy in Joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If capacitance is not positive.

    Example:
        >>> capacitor_energy(0.001, 10)
        0.05

    Complexity: O(1)
    """
    if not isinstance(capacitance, (int, float)):
        raise TypeError("capacitance must be numeric.")

    if not isinstance(voltage, (int, float)):
        raise TypeError("voltage must be numeric.")

    if capacitance <= 0:
        raise ValueError("capacitance must be positive.")

    return float(0.5 * capacitance * voltage * voltage)


def coulomb_force(
    charge1: Union[int, float],
    charge2: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Calculate electrostatic force: F = k * |q₁·q₂| / r².

    Args:
        charge1: First charge in Coulombs.
        charge2: Second charge in Coulombs.
        distance: Distance between charges in meters.

    Returns:
        Force magnitude in Newtons.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If distance is not positive.

    Example:
        >>> round(coulomb_force(1e-6, 2e-6, 0.05), 4)
        7.1928

    Complexity: O(1)
    """
    if not isinstance(charge1, (int, float)):
        raise TypeError("charge1 must be numeric.")

    if not isinstance(charge2, (int, float)):
        raise TypeError("charge2 must be numeric.")

    if not isinstance(distance, (int, float)):
        raise TypeError("distance must be numeric.")

    if distance <= 0:
        raise ValueError("distance must be positive.")

    k = 8.9875517873681764e9  # Coulomb constant N·m²/C²
    return float(k * abs(charge1 * charge2) / (distance * distance))


def schwarzschild_radius(
    mass: Union[int, float],
) -> float:
    """Calculate the Schwarzschild radius: r_s = 2GM / c².

    Args:
        mass: Mass in kg.

    Returns:
        Schwarzschild radius in meters.

    Raises:
        TypeError: If mass is not numeric.
        ValueError: If mass is not positive.

    Example:
        >>> round(schwarzschild_radius(1.989e30), 0)
        2953.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)):
        raise TypeError("mass must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    G = 6.67430e-11  # gravitational constant m³/(kg·s²)
    c = 299792458.0  # speed of light m/s
    return float(2 * G * mass / (c * c))


def doppler_shift(
    source_frequency: Union[int, float],
    relative_velocity: Union[int, float],
    wave_speed: Union[int, float] = 343.0,
) -> float:
    """Calculate observed frequency due to Doppler effect (source moving).

    f_obs = f_src * v / (v + v_s)  (positive v_s = moving away).

    Args:
        source_frequency: Source frequency in Hz.
        relative_velocity: Source velocity relative to observer (m/s, positive = receding).
        wave_speed: Speed of the wave medium in m/s (default 343 for sound).

    Returns:
        Observed frequency in Hz.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If source_frequency or wave_speed not positive, or denominator ≤ 0.

    Example:
        >>> round(doppler_shift(440, 30), 2)
        393.03

    Complexity: O(1)
    """
    if not isinstance(source_frequency, (int, float)):
        raise TypeError("source_frequency must be numeric.")

    if not isinstance(relative_velocity, (int, float)):
        raise TypeError("relative_velocity must be numeric.")

    if not isinstance(wave_speed, (int, float)):
        raise TypeError("wave_speed must be numeric.")

    if source_frequency <= 0:
        raise ValueError("source_frequency must be positive.")

    if wave_speed <= 0:
        raise ValueError("wave_speed must be positive.")

    denom = wave_speed + relative_velocity

    if denom <= 0:
        raise ValueError("wave_speed + relative_velocity must be positive.")

    return float(source_frequency * wave_speed / denom)


def stefan_boltzmann_power(
    emissivity: Union[int, float],
    area: Union[int, float],
    temperature: Union[int, float],
) -> float:
    """Calculate radiated power using Stefan-Boltzmann law: P = ε·σ·A·T⁴.

    Args:
        emissivity: Surface emissivity (0 < ε ≤ 1).
        area: Surface area in m².
        temperature: Absolute temperature in Kelvin.

    Returns:
        Radiated power in Watts.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If emissivity not in (0,1], area or temperature not positive.

    Example:
        >>> round(stefan_boltzmann_power(1.0, 1.0, 300), 2)
        459.27

    Complexity: O(1)
    """
    if not isinstance(emissivity, (int, float)):
        raise TypeError("emissivity must be numeric.")

    if not isinstance(area, (int, float)):
        raise TypeError("area must be numeric.")

    if not isinstance(temperature, (int, float)):
        raise TypeError("temperature must be numeric.")

    if not 0 < emissivity <= 1:
        raise ValueError("emissivity must be in (0, 1].")

    if area <= 0:
        raise ValueError("area must be positive.")

    if temperature <= 0:
        raise ValueError("temperature must be positive.")

    sigma = 5.670374419e-8  # Stefan-Boltzmann constant W/(m²·K⁴)
    return float(emissivity * sigma * area * temperature ** 4)


def spring_potential_energy(
    spring_constant: Union[int, float],
    displacement: Union[int, float],
) -> float:
    """Calculate elastic potential energy: U = ½·k·x².

    Args:
        spring_constant: Spring constant in N/m.
        displacement: Displacement from equilibrium in meters.

    Returns:
        Potential energy in Joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If spring_constant is not positive.

    Example:
        >>> spring_potential_energy(200, 0.1)
        1.0

    Complexity: O(1)
    """
    if not isinstance(spring_constant, (int, float)):
        raise TypeError("spring_constant must be numeric.")

    if not isinstance(displacement, (int, float)):
        raise TypeError("displacement must be numeric.")

    if spring_constant <= 0:
        raise ValueError("spring_constant must be positive.")

    return float(0.5 * spring_constant * displacement * displacement)


def lorentz_factor(
    velocity: Union[int, float],
) -> float:
    """Calculate the Lorentz factor: γ = 1 / √(1 - v²/c²).

    Args:
        velocity: Object velocity in m/s (must be less than c).

    Returns:
        Lorentz factor (≥ 1).

    Raises:
        TypeError: If velocity is not numeric.
        ValueError: If velocity is negative or ≥ speed of light.

    Example:
        >>> round(lorentz_factor(2.0e8), 4)
        1.3416

    Complexity: O(1)
    """
    if not isinstance(velocity, (int, float)):
        raise TypeError("velocity must be numeric.")

    c = 299792458.0

    if velocity < 0:
        raise ValueError("velocity must be non-negative.")

    if velocity >= c:
        raise ValueError("velocity must be less than the speed of light.")

    return float(1.0 / math.sqrt(1.0 - (velocity * velocity) / (c * c)))


def magnetic_force_on_wire(
    current: Union[int, float],
    length: Union[int, float],
    magnetic_field: Union[int, float],
    angle: Union[int, float] = 1.5707963267948966,
) -> float:
    """Calculate force on a current-carrying wire: F = I·L·B·sin(θ).

    Args:
        current: Current in Amperes.
        length: Wire length in the field in meters.
        magnetic_field: Magnetic field strength in Tesla.
        angle: Angle between wire and field in radians (default π/2).

    Returns:
        Force in Newtons.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If length or magnetic_field is negative.

    Example:
        >>> magnetic_force_on_wire(5, 0.2, 0.3)
        0.3

    Complexity: O(1)
    """
    if not isinstance(current, (int, float)):
        raise TypeError("current must be numeric.")

    if not isinstance(length, (int, float)):
        raise TypeError("length must be numeric.")

    if not isinstance(magnetic_field, (int, float)):
        raise TypeError("magnetic_field must be numeric.")

    if not isinstance(angle, (int, float)):
        raise TypeError("angle must be numeric.")

    if length < 0:
        raise ValueError("length must be non-negative.")

    if magnetic_field < 0:
        raise ValueError("magnetic_field must be non-negative.")

    return float(abs(current) * length * magnetic_field * math.sin(angle))


def inductor_energy(
    inductance: Union[int, float],
    current: Union[int, float],
) -> float:
    """Calculate energy stored in an inductor: E = ½·L·I².

    Args:
        inductance: Inductance in Henrys.
        current: Current in Amperes.

    Returns:
        Energy in Joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inductance is not positive.

    Example:
        >>> inductor_energy(0.01, 5)
        0.125

    Complexity: O(1)
    """
    if not isinstance(inductance, (int, float)):
        raise TypeError("inductance must be numeric.")

    if not isinstance(current, (int, float)):
        raise TypeError("current must be numeric.")

    if inductance <= 0:
        raise ValueError("inductance must be positive.")

    return float(0.5 * inductance * current * current)


def drag_force(
    drag_coefficient: Union[int, float],
    fluid_density: Union[int, float],
    velocity: Union[int, float],
    reference_area: Union[int, float],
) -> float:
    """Calculate aerodynamic drag force: F_d = ½·C_d·ρ·v²·A.

    Args:
        drag_coefficient: Dimensionless drag coefficient.
        fluid_density: Fluid density in kg/m³.
        velocity: Velocity in m/s.
        reference_area: Reference area in m².

    Returns:
        Drag force in Newtons.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If drag_coefficient, fluid_density, or reference_area is not positive.

    Example:
        >>> drag_force(0.47, 1.225, 10, 0.01)
        0.028787500000000002

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (drag_coefficient, fluid_density, velocity, reference_area)):
        raise TypeError("all inputs must be numeric.")

    if drag_coefficient <= 0:
        raise ValueError("drag_coefficient must be positive.")

    if fluid_density <= 0:
        raise ValueError("fluid_density must be positive.")

    if reference_area <= 0:
        raise ValueError("reference_area must be positive.")

    return float(0.5 * drag_coefficient * fluid_density * velocity ** 2 * reference_area)


def kinetic_energy_relativistic(
    rest_mass: Union[int, float],
    velocity: Union[int, float],
) -> float:
    """Calculate relativistic kinetic energy: KE = (γ - 1)·m·c².

    Args:
        rest_mass: Rest mass in kg.
        velocity: Velocity in m/s (must be < c).

    Returns:
        Kinetic energy in Joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If rest_mass not positive or velocity not in [0, c).

    Example:
        >>> round(kinetic_energy_relativistic(1.0, 0), 1)
        0.0

    Complexity: O(1)
    """
    if not isinstance(rest_mass, (int, float)):
        raise TypeError("rest_mass must be numeric.")

    if not isinstance(velocity, (int, float)):
        raise TypeError("velocity must be numeric.")

    if rest_mass <= 0:
        raise ValueError("rest_mass must be positive.")

    c = 299792458.0

    if velocity < 0 or velocity >= c:
        raise ValueError("velocity must be in [0, c).")

    gamma = 1.0 / math.sqrt(1.0 - (velocity ** 2) / (c ** 2))

    return float((gamma - 1.0) * rest_mass * c ** 2)


def electric_field_point(
    charge: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Calculate the electric field magnitude from a point charge: E = k·|q|/r².

    Args:
        charge: Charge in Coulombs.
        distance: Distance from charge in meters.

    Returns:
        Electric field magnitude in N/C (= V/m).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If distance is not positive.

    Example:
        >>> round(electric_field_point(1e-6, 0.1), 2)
        898755.18

    Complexity: O(1)
    """
    if not isinstance(charge, (int, float)):
        raise TypeError("charge must be numeric.")

    if not isinstance(distance, (int, float)):
        raise TypeError("distance must be numeric.")

    if distance <= 0:
        raise ValueError("distance must be positive.")

    k = 8.9875517873681764e9
    return float(k * abs(charge) / (distance ** 2))


def magnetic_flux(
    magnetic_field: Union[int, float],
    area: Union[int, float],
    angle: Union[int, float] = 0.0,
) -> float:
    """Calculate magnetic flux: Φ = B·A·cos(θ).

    Args:
        magnetic_field: Magnetic field strength in Tesla.
        area: Area in m².
        angle: Angle between field and area normal in radians (default 0).

    Returns:
        Magnetic flux in Weber.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If area is negative.

    Example:
        >>> magnetic_flux(0.5, 0.02)
        0.01

    Complexity: O(1)
    """
    if not isinstance(magnetic_field, (int, float)):
        raise TypeError("magnetic_field must be numeric.")

    if not isinstance(area, (int, float)):
        raise TypeError("area must be numeric.")

    if not isinstance(angle, (int, float)):
        raise TypeError("angle must be numeric.")

    if area < 0:
        raise ValueError("area must be non-negative.")

    return float(magnetic_field * area * math.cos(angle))


def resistors_parallel_pair(
    r1: Union[int, float],
    r2: Union[int, float],
) -> float:
    """Calculate equivalent resistance of two resistors in parallel.

    R_eq = (R₁·R₂) / (R₁ + R₂)

    Args:
        r1: First resistance in Ohms.
        r2: Second resistance in Ohms.

    Returns:
        Equivalent resistance in Ohms.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If either resistance is not positive.

    Example:
        >>> resistors_parallel_pair(100, 100)
        50.0

    Complexity: O(1)
    """
    if not isinstance(r1, (int, float)):
        raise TypeError("r1 must be numeric.")

    if not isinstance(r2, (int, float)):
        raise TypeError("r2 must be numeric.")

    if r1 <= 0 or r2 <= 0:
        raise ValueError("resistances must be positive.")

    return float((r1 * r2) / (r1 + r2))


def rc_time_constant(
    resistance: Union[int, float],
    capacitance: Union[int, float],
) -> float:
    """Calculate the RC time constant: τ = R·C.

    Args:
        resistance: Resistance in Ohms.
        capacitance: Capacitance in Farads.

    Returns:
        Time constant in seconds.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If either value is not positive.

    Example:
        >>> rc_time_constant(1000, 0.001)
        1.0

    Complexity: O(1)
    """
    if not isinstance(resistance, (int, float)):
        raise TypeError("resistance must be numeric.")

    if not isinstance(capacitance, (int, float)):
        raise TypeError("capacitance must be numeric.")

    if resistance <= 0:
        raise ValueError("resistance must be positive.")

    if capacitance <= 0:
        raise ValueError("capacitance must be positive.")

    return float(resistance * capacitance)


def thermal_resistance(
    length: Union[int, float],
    thermal_conductivity: Union[int, float],
    area: Union[int, float],
) -> float:
    """Calculate thermal resistance for conduction: R_th = L / (k·A).

    Args:
        length: Material thickness in meters.
        thermal_conductivity: Thermal conductivity in W/(m·K).
        area: Cross-sectional area in m².

    Returns:
        Thermal resistance in K/W.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any value is not positive.

    Example:
        >>> thermal_resistance(0.1, 200, 0.01)
        0.05

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (length, thermal_conductivity, area)):
        raise TypeError("all inputs must be numeric.")

    if length <= 0:
        raise ValueError("length must be positive.")

    if thermal_conductivity <= 0:
        raise ValueError("thermal_conductivity must be positive.")

    if area <= 0:
        raise ValueError("area must be positive.")

    return float(length / (thermal_conductivity * area))


def heat_transfer_conduction(
    thermal_conductivity: Union[int, float],
    area: Union[int, float],
    temperature_diff: Union[int, float],
    thickness: Union[int, float],
) -> float:
    """Calculate heat transfer rate by conduction (Fourier's law): Q = k·A·ΔT/L.

    Args:
        thermal_conductivity: Thermal conductivity in W/(m·K).
        area: Cross-sectional area in m².
        temperature_diff: Temperature difference in K.
        thickness: Material thickness in meters.

    Returns:
        Heat transfer rate in Watts.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If thermal_conductivity, area, or thickness not positive.

    Example:
        >>> heat_transfer_conduction(200, 0.01, 50, 0.1)
        1000.0

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (thermal_conductivity, area, temperature_diff, thickness)):
        raise TypeError("all inputs must be numeric.")

    if thermal_conductivity <= 0:
        raise ValueError("thermal_conductivity must be positive.")

    if area <= 0:
        raise ValueError("area must be positive.")

    if thickness <= 0:
        raise ValueError("thickness must be positive.")

    return float(thermal_conductivity * area * temperature_diff / thickness)


def pendulum_period(
    length: Union[int, float],
    gravity: Union[int, float] = 9.80665,
) -> float:
    """Calculate the period of a simple pendulum: T = 2π√(L/g).

    Args:
        length: Pendulum length in meters.
        gravity: Gravitational acceleration in m/s² (default 9.80665).

    Returns:
        Period in seconds.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If length or gravity is not positive.

    Example:
        >>> round(pendulum_period(1.0), 4)
        2.0064

    Complexity: O(1)
    """
    if not isinstance(length, (int, float)):
        raise TypeError("length must be numeric.")

    if not isinstance(gravity, (int, float)):
        raise TypeError("gravity must be numeric.")

    if length <= 0:
        raise ValueError("length must be positive.")

    if gravity <= 0:
        raise ValueError("gravity must be positive.")

    return float(2 * math.pi * math.sqrt(length / gravity))


def projectile_range(
    velocity: Union[int, float],
    angle: Union[int, float],
    gravity: Union[int, float] = 9.80665,
) -> float:
    """Calculate the horizontal range of a projectile (flat ground).

    R = v²·sin(2θ) / g

    Args:
        velocity: Launch velocity in m/s.
        angle: Launch angle in radians.
        gravity: Gravitational acceleration in m/s².

    Returns:
        Horizontal range in meters.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If velocity or gravity is not positive.

    Example:
        >>> import math
        >>> round(projectile_range(20, math.radians(45)), 2)
        40.77

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (velocity, angle, gravity)):
        raise TypeError("all inputs must be numeric.")

    if velocity <= 0:
        raise ValueError("velocity must be positive.")

    if gravity <= 0:
        raise ValueError("gravity must be positive.")

    return float(velocity ** 2 * math.sin(2 * angle) / gravity)


def projectile_max_height(
    velocity: Union[int, float],
    angle: Union[int, float],
    gravity: Union[int, float] = 9.80665,
) -> float:
    """Calculate the maximum height of a projectile: H = v²·sin²(θ) / (2g).

    Args:
        velocity: Launch velocity in m/s.
        angle: Launch angle in radians.
        gravity: Gravitational acceleration in m/s².

    Returns:
        Maximum height in meters.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If velocity or gravity is not positive.

    Example:
        >>> import math
        >>> round(projectile_max_height(20, math.radians(45)), 2)
        10.19

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (velocity, angle, gravity)):
        raise TypeError("all inputs must be numeric.")

    if velocity <= 0:
        raise ValueError("velocity must be positive.")

    if gravity <= 0:
        raise ValueError("gravity must be positive.")

    return float((velocity * math.sin(angle)) ** 2 / (2 * gravity))


def projectile_time_of_flight(
    velocity: Union[int, float],
    angle: Union[int, float],
    gravity: Union[int, float] = 9.80665,
) -> float:
    """Calculate time of flight for a projectile: T = 2v·sin(θ) / g.

    Args:
        velocity: Launch velocity in m/s.
        angle: Launch angle in radians.
        gravity: Gravitational acceleration in m/s².

    Returns:
        Time of flight in seconds.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If velocity or gravity is not positive.

    Example:
        >>> import math
        >>> round(projectile_time_of_flight(20, math.radians(45)), 4)
        2.8837

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (velocity, angle, gravity)):
        raise TypeError("all inputs must be numeric.")

    if velocity <= 0:
        raise ValueError("velocity must be positive.")

    if gravity <= 0:
        raise ValueError("gravity must be positive.")

    return float(2 * velocity * math.sin(angle) / gravity)


def pressure_at_depth(
    fluid_density: Union[int, float],
    depth: Union[int, float],
    gravity: Union[int, float] = 9.80665,
    surface_pressure: Union[int, float] = 101325.0,
) -> float:
    """Calculate pressure at a depth in a fluid: P = P₀ + ρ·g·h.

    Args:
        fluid_density: Fluid density in kg/m³.
        depth: Depth below surface in meters.
        gravity: Gravitational acceleration in m/s² (default 9.80665).
        surface_pressure: Atmospheric pressure in Pa (default 101325).

    Returns:
        Pressure in Pascals.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If density, depth, or gravity is not positive.

    Example:
        >>> pressure_at_depth(1000, 10)
        199391.5

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (fluid_density, depth, gravity, surface_pressure)):
        raise TypeError("all inputs must be numeric.")

    if fluid_density <= 0:
        raise ValueError("fluid_density must be positive.")

    if depth < 0:
        raise ValueError("depth must be non-negative.")

    if gravity <= 0:
        raise ValueError("gravity must be positive.")

    return float(surface_pressure + fluid_density * gravity * depth)


def bernoulli_velocity(
    pressure_diff: Union[int, float],
    fluid_density: Union[int, float],
) -> float:
    """Calculate flow velocity from pressure difference (Bernoulli's eq.).

    v = √(2·ΔP / ρ)

    Args:
        pressure_diff: Pressure difference in Pa.
        fluid_density: Fluid density in kg/m³.

    Returns:
        Flow velocity in m/s.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If pressure_diff is negative or density not positive.

    Example:
        >>> round(bernoulli_velocity(500, 1.225), 4)
        28.5714

    Complexity: O(1)
    """
    if not isinstance(pressure_diff, (int, float)):
        raise TypeError("pressure_diff must be numeric.")

    if not isinstance(fluid_density, (int, float)):
        raise TypeError("fluid_density must be numeric.")

    if pressure_diff < 0:
        raise ValueError("pressure_diff must be non-negative.")

    if fluid_density <= 0:
        raise ValueError("fluid_density must be positive.")

    return float(math.sqrt(2 * pressure_diff / fluid_density))


def work_done(
    force: Union[int, float],
    displacement: Union[int, float],
    angle: Union[int, float] = 0.0,
) -> float:
    """Calculate work done: W = F·d·cos(θ).

    Args:
        force: Force in Newtons.
        displacement: Displacement in meters.
        angle: Angle between force and displacement in radians (default 0).

    Returns:
        Work in Joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If displacement is negative.

    Example:
        >>> work_done(50, 10)
        500.0

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (force, displacement, angle)):
        raise TypeError("all inputs must be numeric.")

    if displacement < 0:
        raise ValueError("displacement must be non-negative.")

    return float(force * displacement * math.cos(angle))


def gravitational_potential_energy(
    mass: Union[int, float],
    height: Union[int, float],
    gravity: Union[int, float] = 9.80665,
) -> float:
    """Calculate gravitational potential energy: U = m·g·h.

    Args:
        mass: Mass in kg.
        height: Height above reference in meters.
        gravity: Gravitational acceleration in m/s² (default 9.80665).

    Returns:
        Potential energy in Joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass or gravity is not positive.

    Example:
        >>> gravitational_potential_energy(10, 5)
        490.3325

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (mass, height, gravity)):
        raise TypeError("all inputs must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    if gravity <= 0:
        raise ValueError("gravity must be positive.")

    return float(mass * gravity * height)


def centripetal_acceleration(
    velocity: Union[int, float],
    radius: Union[int, float],
) -> float:
    """Calculate centripetal acceleration a = v² / r.

    Args:
        velocity: Tangential velocity (m/s).
        radius: Radius of circular path (m).

    Returns:
        Centripetal acceleration in m/s².

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If radius is not positive.

    Example:
        >>> centripetal_acceleration(10, 5)
        20.0

    Complexity: O(1)
    """
    if not isinstance(velocity, (int, float)) or not isinstance(radius, (int, float)):
        raise TypeError("velocity and radius must be numeric.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    return float(velocity ** 2 / radius)


def orbital_period(
    semi_major_axis: Union[int, float],
    central_mass: Union[int, float],
) -> float:
    """Calculate orbital period using Kepler's third law.

    T = 2π √(a³ / (G·M))

    Args:
        semi_major_axis: Semi-major axis in meters.
        central_mass: Mass of central body in kg.

    Returns:
        Orbital period in seconds.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive.

    Example:
        >>> round(orbital_period(6.371e6 + 408000, 5.972e24))
        5554

    Complexity: O(1)
    """
    if not isinstance(semi_major_axis, (int, float)) or not isinstance(central_mass, (int, float)):
        raise TypeError("semi_major_axis and central_mass must be numeric.")

    if semi_major_axis <= 0 or central_mass <= 0:
        raise ValueError("semi_major_axis and central_mass must be positive.")

    G = 6.67430e-11

    return float(2 * math.pi * math.sqrt(semi_major_axis ** 3 / (G * central_mass)))


def power_mechanical(
    work: Union[int, float],
    time: Union[int, float],
) -> float:
    """Calculate mechanical power P = W / t.

    Args:
        work: Work done in joules.
        time: Time in seconds.

    Returns:
        Power in watts.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If time is not positive.

    Example:
        >>> power_mechanical(1000, 5)
        200.0

    Complexity: O(1)
    """
    if not isinstance(work, (int, float)) or not isinstance(time, (int, float)):
        raise TypeError("work and time must be numeric.")

    if time <= 0:
        raise ValueError("time must be positive.")

    return float(work / time)


def angular_momentum(
    mass: Union[int, float],
    velocity: Union[int, float],
    radius: Union[int, float],
) -> float:
    """Calculate angular momentum L = m·v·r.

    Args:
        mass: Mass in kg.
        velocity: Tangential velocity in m/s.
        radius: Radius in meters.

    Returns:
        Angular momentum in kg·m²/s.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass or radius is not positive.

    Example:
        >>> angular_momentum(2, 3, 4)
        24.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)) or not isinstance(velocity, (int, float)) or not isinstance(radius, (int, float)):
        raise TypeError("mass, velocity, radius must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    return float(mass * velocity * radius)


def moment_of_inertia_point(
    mass: Union[int, float],
    radius: Union[int, float],
) -> float:
    """Calculate moment of inertia for a point mass I = m·r².

    Args:
        mass: Mass in kg.
        radius: Distance from rotation axis in meters.

    Returns:
        Moment of inertia in kg·m².

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass is not positive.

    Example:
        >>> moment_of_inertia_point(5, 3)
        45.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)) or not isinstance(radius, (int, float)):
        raise TypeError("mass and radius must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    return float(mass * radius ** 2)


def sound_intensity_level(
    intensity: Union[int, float],
    reference: Union[int, float] = 1e-12,
) -> float:
    """Calculate sound intensity level in decibels.

    β = 10 · log₁₀(I / I₀)

    Args:
        intensity: Sound intensity in W/m².
        reference: Reference intensity (default 1e-12 W/m²).

    Returns:
        Sound level in decibels.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive.

    Example:
        >>> sound_intensity_level(1e-6)
        60.0

    Complexity: O(1)
    """
    if not isinstance(intensity, (int, float)) or not isinstance(reference, (int, float)):
        raise TypeError("intensity and reference must be numeric.")

    if intensity <= 0 or reference <= 0:
        raise ValueError("intensity and reference must be positive.")

    return float(10 * math.log10(intensity / reference))


def bulk_modulus_pressure(
    bulk_modulus: Union[int, float],
    volume_change: Union[int, float],
    original_volume: Union[int, float],
) -> float:
    """Calculate pressure change from bulk modulus.

    ΔP = -K · (ΔV / V₀)

    Args:
        bulk_modulus: Bulk modulus in pascals.
        volume_change: Change in volume (negative for compression).
        original_volume: Original volume.

    Returns:
        Pressure change in pascals.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If bulk_modulus or original_volume is not positive.

    Example:
        >>> bulk_modulus_pressure(2.2e9, -0.001, 1.0)
        2200000.0

    Complexity: O(1)
    """
    if not isinstance(bulk_modulus, (int, float)) or not isinstance(volume_change, (int, float)) or not isinstance(original_volume, (int, float)):
        raise TypeError("All inputs must be numeric.")

    if bulk_modulus <= 0:
        raise ValueError("bulk_modulus must be positive.")

    if original_volume <= 0:
        raise ValueError("original_volume must be positive.")

    return float(-bulk_modulus * (volume_change / original_volume))


def centripetal_force(
    mass: Union[int, float],
    velocity: Union[int, float],
    radius: Union[int, float],
) -> float:
    """Calculate centripetal force F = m·v²/r.

    Args:
        mass: Mass in kg.
        velocity: Tangential velocity in m/s.
        radius: Radius of circular path in m.

    Returns:
        Centripetal force in newtons.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass or radius is not positive.

    Example:
        >>> centripetal_force(2, 10, 5)
        40.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)) or not isinstance(velocity, (int, float)) or not isinstance(radius, (int, float)):
        raise TypeError("mass, velocity, radius must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    if radius <= 0:
        raise ValueError("radius must be positive.")

    return float(mass * velocity ** 2 / radius)


def torque(
    force: Union[int, float],
    lever_arm: Union[int, float],
    angle: Union[int, float] = 1.5707963267948966,
) -> float:
    """Calculate torque τ = F·r·sin(θ).

    Args:
        force: Applied force in newtons.
        lever_arm: Distance from pivot in meters.
        angle: Angle between force and lever arm in radians (default π/2).

    Returns:
        Torque in N·m.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If force or lever_arm is negative.

    Example:
        >>> torque(100, 0.5)
        50.0

    Complexity: O(1)
    """
    if not isinstance(force, (int, float)) or not isinstance(lever_arm, (int, float)) or not isinstance(angle, (int, float)):
        raise TypeError("force, lever_arm, angle must be numeric.")

    if force < 0:
        raise ValueError("force must be non-negative.")

    if lever_arm < 0:
        raise ValueError("lever_arm must be non-negative.")

    return float(force * lever_arm * math.sin(angle))


def elastic_potential_energy(
    k: Union[int, float],
    x: Union[int, float],
) -> float:
    """Calculate elastic potential energy U = ½·k·x².

    Args:
        k: Spring constant in N/m.
        x: Displacement from equilibrium in meters.

    Returns:
        Elastic PE in joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If k is not positive.

    Example:
        >>> elastic_potential_energy(200, 0.1)
        1.0

    Complexity: O(1)
    """
    if not isinstance(k, (int, float)) or not isinstance(x, (int, float)):
        raise TypeError("k and x must be numeric.")

    if k <= 0:
        raise ValueError("k must be positive.")

    return float(0.5 * k * x ** 2)


def electric_potential(
    charge: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Calculate electric potential V = k·q/r.

    Args:
        charge: Point charge in coulombs.
        distance: Distance from charge in meters.

    Returns:
        Electric potential in volts.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If distance is not positive.

    Example:
        >>> round(electric_potential(1e-6, 0.1), 2)
        89875.52

    Complexity: O(1)
    """
    if not isinstance(charge, (int, float)) or not isinstance(distance, (int, float)):
        raise TypeError("charge and distance must be numeric.")

    if distance <= 0:
        raise ValueError("distance must be positive.")

    K = 8.9875517873681764e9

    return float(K * charge / distance)


def capacitance_parallel_plate(
    area: Union[int, float],
    distance: Union[int, float],
    epsilon_r: Union[int, float] = 1.0,
) -> float:
    """Calculate parallel plate capacitance C = ε₀·εᵣ·A/d.

    Args:
        area: Plate area in m².
        distance: Plate separation in meters.
        epsilon_r: Relative permittivity (default 1.0 for vacuum).

    Returns:
        Capacitance in farads.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If area, distance, or epsilon_r not positive.

    Example:
        >>> round(capacitance_parallel_plate(0.01, 0.001), 14)
        8.854187817e-11

    Complexity: O(1)
    """
    if not isinstance(area, (int, float)) or not isinstance(distance, (int, float)) or not isinstance(epsilon_r, (int, float)):
        raise TypeError("area, distance, epsilon_r must be numeric.")

    if area <= 0 or distance <= 0 or epsilon_r <= 0:
        raise ValueError("area, distance, epsilon_r must be positive.")

    EPSILON_0 = 8.8541878128e-12

    return float(EPSILON_0 * epsilon_r * area / distance)


def magnetic_field_solenoid(
    n_turns: Union[int, float],
    current: Union[int, float],
    length: Union[int, float],
) -> float:
    """Calculate magnetic field inside a solenoid B = μ₀·(N/L)·I.

    Args:
        n_turns: Number of turns.
        current: Current in amperes.
        length: Length of solenoid in meters.

    Returns:
        Magnetic field in tesla.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If n_turns, current, or length not positive.

    Example:
        >>> round(magnetic_field_solenoid(1000, 2, 0.5), 6)
        0.005027

    Complexity: O(1)
    """
    if not isinstance(n_turns, (int, float)) or not isinstance(current, (int, float)) or not isinstance(length, (int, float)):
        raise TypeError("n_turns, current, length must be numeric.")

    if n_turns <= 0 or current <= 0 or length <= 0:
        raise ValueError("n_turns, current, length must be positive.")

    MU_0 = 4 * math.pi * 1e-7

    return float(MU_0 * (n_turns / length) * current)


def snells_law_angle(
    n1: Union[int, float],
    n2: Union[int, float],
    theta1: Union[int, float],
) -> float:
    """Calculate refracted angle using Snell's law: n₁·sin(θ₁) = n₂·sin(θ₂).

    Args:
        n1: Refractive index of first medium.
        n2: Refractive index of second medium.
        theta1: Incident angle in radians.

    Returns:
        Refracted angle in radians.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If indices not positive or total internal reflection occurs.

    Example:
        >>> import math
        >>> round(snells_law_angle(1.0, 1.5, math.pi / 4), 6)
        0.488342

    Complexity: O(1)
    """
    if not isinstance(n1, (int, float)) or not isinstance(n2, (int, float)) or not isinstance(theta1, (int, float)):
        raise TypeError("n1, n2, theta1 must be numeric.")

    if n1 <= 0 or n2 <= 0:
        raise ValueError("Refractive indices must be positive.")

    sin_theta2 = n1 * math.sin(theta1) / n2

    if abs(sin_theta2) > 1:
        raise ValueError("Total internal reflection; no refracted angle exists.")

    return float(math.asin(sin_theta2))


def drift_velocity(
    current: Union[int, float],
    n_density: Union[int, float],
    charge: Union[int, float],
    area: Union[int, float],
) -> float:
    """Calculate charge carrier drift velocity v = I / (n·q·A).

    Args:
        current: Electric current in amperes.
        n_density: Number density of carriers (m⁻³).
        charge: Charge per carrier in coulombs.
        area: Cross-sectional area in m².

    Returns:
        Drift velocity in m/s.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If n_density, charge, or area not positive.

    Example:
        >>> drift_velocity(10, 8.5e28, 1.6e-19, 1e-6)
        0.0007352941176470589

    Complexity: O(1)
    """
    if not isinstance(current, (int, float)) or not isinstance(n_density, (int, float)) or not isinstance(charge, (int, float)) or not isinstance(area, (int, float)):
        raise TypeError("All inputs must be numeric.")

    if n_density <= 0 or charge <= 0 or area <= 0:
        raise ValueError("n_density, charge, area must be positive.")

    return float(current / (n_density * charge * area))


def kinematic_displacement(
    initial_velocity: Union[int, float],
    time: Union[int, float],
    acceleration: Union[int, float],
) -> float:
    """Calculate displacement using kinematic equation s = v₀·t + ½·a·t².

    Args:
        initial_velocity: Initial velocity in m/s.
        time: Elapsed time in seconds.
        acceleration: Constant acceleration in m/s².

    Returns:
        Displacement in meters.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If time is negative.

    Example:
        >>> kinematic_displacement(10, 5, 2)
        75.0

    Complexity: O(1)
    """
    if not isinstance(initial_velocity, (int, float)) or not isinstance(time, (int, float)) or not isinstance(acceleration, (int, float)):
        raise TypeError("initial_velocity, time, acceleration must be numeric.")

    if time < 0:
        raise ValueError("time must be non-negative.")

    return float(initial_velocity * time + 0.5 * acceleration * time ** 2)


def heat_capacity(
    mass: Union[int, float],
    specific_heat: Union[int, float],
    temperature_change: Union[int, float],
) -> float:
    """Calculate heat energy Q = m·c·ΔT.

    Args:
        mass: Mass in kg.
        specific_heat: Specific heat capacity in J/(kg·K).
        temperature_change: Temperature change in K.

    Returns:
        Heat energy in joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass or specific_heat is not positive.

    Example:
        >>> heat_capacity(2, 4186, 10)
        83720.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)) or not isinstance(specific_heat, (int, float)) or not isinstance(temperature_change, (int, float)):
        raise TypeError("All inputs must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    if specific_heat <= 0:
        raise ValueError("specific_heat must be positive.")

    return float(mass * specific_heat * temperature_change)


def adiabatic_index_pressure(
    p1: Union[int, float],
    v1: Union[int, float],
    v2: Union[int, float],
    gamma: Union[int, float],
) -> float:
    """Calculate final pressure in an adiabatic process.

    P₂ = P₁ · (V₁/V₂)^γ

    Args:
        p1: Initial pressure in Pa.
        v1: Initial volume.
        v2: Final volume.
        gamma: Adiabatic index (heat capacity ratio).

    Returns:
        Final pressure in Pa.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If p1, v1, v2, or gamma not positive.

    Example:
        >>> round(adiabatic_index_pressure(100000, 1.0, 0.5, 1.4), 2)
        263901.58

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (p1, v1, v2, gamma)):
        raise TypeError("All inputs must be numeric.")

    if p1 <= 0 or v1 <= 0 or v2 <= 0 or gamma <= 0:
        raise ValueError("All inputs must be positive.")

    return float(p1 * (v1 / v2) ** gamma)


def magnetic_force_charge(
    charge: Union[int, float],
    velocity: Union[int, float],
    magnetic_field: Union[int, float],
    angle: Union[int, float] = 1.5707963267948966,
) -> float:
    """Calculate magnetic force on a moving charge F = q·v·B·sin(θ).

    Args:
        charge: Charge in coulombs.
        velocity: Speed in m/s.
        magnetic_field: Magnetic field in tesla.
        angle: Angle between v and B in radians (default π/2).

    Returns:
        Force in newtons.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> magnetic_force_charge(1.6e-19, 1e6, 0.5)
        8e-14

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (charge, velocity, magnetic_field, angle)):
        raise TypeError("All inputs must be numeric.")

    return float(abs(charge) * velocity * magnetic_field * math.sin(angle))


def electric_field_parallel_plate(
    voltage: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Calculate uniform electric field between parallel plates E = V/d.

    Args:
        voltage: Potential difference in volts.
        distance: Plate separation in meters.

    Returns:
        Electric field in V/m.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If distance is not positive.

    Example:
        >>> electric_field_parallel_plate(1000, 0.01)
        100000.0

    Complexity: O(1)
    """
    if not isinstance(voltage, (int, float)) or not isinstance(distance, (int, float)):
        raise TypeError("voltage and distance must be numeric.")

    if distance <= 0:
        raise ValueError("distance must be positive.")

    return float(voltage / distance)


def resistivity_resistance(
    resistivity: Union[int, float],
    length: Union[int, float],
    area: Union[int, float],
) -> float:
    """Calculate resistance from resistivity R = ρ·L/A.

    Args:
        resistivity: Resistivity in Ω·m.
        length: Conductor length in meters.
        area: Cross-sectional area in m².

    Returns:
        Resistance in ohms.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive.

    Example:
        >>> resistivity_resistance(1.68e-8, 100, 1e-6)
        1.68

    Complexity: O(1)
    """
    if not isinstance(resistivity, (int, float)) or not isinstance(length, (int, float)) or not isinstance(area, (int, float)):
        raise TypeError("All inputs must be numeric.")

    if resistivity <= 0 or length <= 0 or area <= 0:
        raise ValueError("All inputs must be positive.")

    return float(resistivity * length / area)


def wave_frequency(
    wave_speed: Union[int, float],
    wavelength: Union[int, float],
) -> float:
    """Calculate wave frequency f = v/λ.

    Args:
        wave_speed: Speed of the wave in m/s.
        wavelength: Wavelength in meters.

    Returns:
        Frequency in Hz.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inputs are not positive.

    Example:
        >>> wave_frequency(340, 0.5)
        680.0

    Complexity: O(1)
    """
    if not isinstance(wave_speed, (int, float)) or not isinstance(wavelength, (int, float)):
        raise TypeError("wave_speed and wavelength must be numeric.")

    if wave_speed <= 0 or wavelength <= 0:
        raise ValueError("wave_speed and wavelength must be positive.")

    return float(wave_speed / wavelength)


def photon_momentum(
    wavelength: Union[int, float],
) -> float:
    """Calculate photon momentum p = h/λ.

    Args:
        wavelength: Wavelength in meters.

    Returns:
        Momentum in kg·m/s.

    Raises:
        TypeError: If input is not numeric.
        ValueError: If wavelength is not positive.

    Example:
        >>> round(photon_momentum(500e-9), 30)
        1.325e-27

    Complexity: O(1)
    """
    if not isinstance(wavelength, (int, float)):
        raise TypeError("wavelength must be numeric.")

    if wavelength <= 0:
        raise ValueError("wavelength must be positive.")

    H = 6.62607015e-34

    return float(H / wavelength)


def relativistic_energy(
    mass: Union[int, float],
    velocity: Union[int, float],
) -> float:
    """Calculate total relativistic energy E = γ·m·c².

    Args:
        mass: Rest mass in kg.
        velocity: Speed in m/s (must be < c).

    Returns:
        Total energy in joules.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If mass not positive or velocity ≥ c.

    Example:
        >>> round(relativistic_energy(1, 0), 2)
        89875517873681764.0

    Complexity: O(1)
    """
    if not isinstance(mass, (int, float)) or not isinstance(velocity, (int, float)):
        raise TypeError("mass and velocity must be numeric.")

    if mass <= 0:
        raise ValueError("mass must be positive.")

    C = 299792458.0

    if abs(velocity) >= C:
        raise ValueError("velocity must be less than the speed of light.")

    gamma = 1 / math.sqrt(1 - (velocity / C) ** 2)

    return float(gamma * mass * C ** 2)


def coulombs_force(
    q1: Union[int, float],
    q2: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Return the electrostatic force between two point charges.

    F = k · |q₁ · q₂| / r²,  where k ≈ 8.9876 × 10⁹ N·m²/C².

    Args:
        q1: First charge in coulombs.
        q2: Second charge in coulombs.
        distance: Distance between charges in metres (must be > 0).

    Returns:
        Electrostatic force magnitude in newtons.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If distance is zero or negative.

    Example:
        >>> round(coulombs_force(1e-6, 2e-6, 0.05), 4)
        7.19

    Complexity: O(1)
    """
    K = 8.9875517873681764e9

    if not isinstance(q1, (int, float)):
        raise TypeError("q1 must be numeric.")

    if not isinstance(q2, (int, float)):
        raise TypeError("q2 must be numeric.")

    if not isinstance(distance, (int, float)):
        raise TypeError("distance must be numeric.")

    if distance <= 0:
        raise ValueError("distance must be positive.")

    return float(K * abs(q1 * q2) / distance ** 2)


def rl_time_constant(
    inductance: Union[int, float],
    resistance: Union[int, float],
) -> float:
    """Return the RL circuit time constant.

    τ = L / R.  The time for current to reach ≈ 63.2 %
    of its final value when a voltage is applied.

    Args:
        inductance: Inductance in henries (must be > 0).
        resistance: Resistance in ohms (must be > 0).

    Returns:
        Time constant in seconds.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If inductance or resistance is not positive.

    Example:
        >>> rl_time_constant(0.5, 100)
        0.005

    Complexity: O(1)
    """
    if not isinstance(inductance, (int, float)):
        raise TypeError("inductance must be numeric.")

    if not isinstance(resistance, (int, float)):
        raise TypeError("resistance must be numeric.")

    if inductance <= 0:
        raise ValueError("inductance must be positive.")

    if resistance <= 0:
        raise ValueError("resistance must be positive.")

    return float(inductance / resistance)


def doppler_frequency(
    source_freq: Union[int, float],
    wave_speed: Union[int, float],
    observer_speed: Union[int, float] = 0.0,
    source_speed: Union[int, float] = 0.0,
) -> float:
    """Return the observed frequency due to the Doppler effect.

    f' = f_s · (v + v_o) / (v − v_s).  Positive observer speed
    means moving toward the source; positive source speed means
    moving toward the observer.

    Args:
        source_freq: Frequency emitted by the source in Hz (> 0).
        wave_speed: Speed of the wave in the medium in m/s (> 0).
        observer_speed: Observer speed in m/s (toward source > 0).
        source_speed: Source speed in m/s (toward observer > 0).

    Returns:
        Observed frequency in Hz.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If source_freq ≤ 0, wave_speed ≤ 0, or
            (wave_speed − source_speed) ≤ 0.

    Example:
        >>> round(doppler_frequency(440, 343, 0, 30), 2)
        482.17

    Complexity: O(1)
    """
    for name, val in (("source_freq", source_freq), ("wave_speed", wave_speed),
                      ("observer_speed", observer_speed), ("source_speed", source_speed)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if source_freq <= 0:
        raise ValueError("source_freq must be positive.")

    if wave_speed <= 0:
        raise ValueError("wave_speed must be positive.")

    denominator = wave_speed - source_speed

    if denominator <= 0:
        raise ValueError("source_speed must be less than wave_speed.")

    return float(source_freq * (wave_speed + observer_speed) / denominator)


def thermal_expansion_length(
    original_length: Union[int, float],
    alpha: Union[int, float],
    delta_temp: Union[int, float],
) -> float:
    """Return the change in length due to thermal expansion.

    ΔL = L₀ · α · ΔT.

    Args:
        original_length: Original length in metres (must be > 0).
        alpha: Coefficient of linear thermal expansion (1/K).
        delta_temp: Temperature change in kelvins or °C.

    Returns:
        Change in length in metres.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If original_length is not positive.

    Example:
        >>> thermal_expansion_length(2.0, 1.2e-5, 100)
        0.0024

    Complexity: O(1)
    """
    if not isinstance(original_length, (int, float)):
        raise TypeError("original_length must be numeric.")

    if not isinstance(alpha, (int, float)):
        raise TypeError("alpha must be numeric.")

    if not isinstance(delta_temp, (int, float)):
        raise TypeError("delta_temp must be numeric.")

    if original_length <= 0:
        raise ValueError("original_length must be positive.")

    return float(original_length * alpha * delta_temp)


def wien_displacement_peak(
    temperature: Union[int, float],
) -> float:
    """Return the peak wavelength from Wien's displacement law.

    λ_max = b / T,  where b ≈ 2.8978 × 10⁻³ m·K.

    Args:
        temperature: Absolute temperature in kelvins (must be > 0).

    Returns:
        Peak wavelength in metres.

    Raises:
        TypeError: If temperature is not numeric.
        ValueError: If temperature is not positive.

    Example:
        >>> round(wien_displacement_peak(5778), 10)
        5.015e-07

    Complexity: O(1)
    """
    WIEN_B = 2.8977719e-3

    if not isinstance(temperature, (int, float)):
        raise TypeError("temperature must be numeric.")

    if temperature <= 0:
        raise ValueError("temperature must be positive.")

    return float(WIEN_B / temperature)


def compton_wavelength_shift(
    angle: Union[int, float],
) -> float:
    """Return the Compton wavelength shift for photon scattering.

    Δλ = (h / (mₑ · c)) · (1 − cos θ),  where θ is the
    scattering angle in radians.

    Args:
        angle: Scattering angle in radians.

    Returns:
        Wavelength shift in metres.

    Raises:
        TypeError: If angle is not numeric.

    Example:
        >>> round(compton_wavelength_shift(math.pi), 15)
        4.853e-12

    Complexity: O(1)
    """
    H = 6.62607015e-34
    M_E = 9.1093837015e-31
    C = 299792458.0

    if not isinstance(angle, (int, float)):
        raise TypeError("angle must be numeric.")

    compton_wl = H / (M_E * C)

    return float(compton_wl * (1 - math.cos(angle)))


def parallel_resistance(
    r1: Union[int, float],
    r2: Union[int, float],
) -> float:
    """Return the equivalent resistance of two resistors in parallel.

    R = (R₁ · R₂) / (R₁ + R₂).

    Args:
        r1: First resistance in ohms (must be > 0).
        r2: Second resistance in ohms (must be > 0).

    Returns:
        Equivalent parallel resistance in ohms.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If r1 or r2 is not positive.

    Example:
        >>> round(parallel_resistance(100, 200), 4)
        66.6667

    Complexity: O(1)
    """
    if not isinstance(r1, (int, float)):
        raise TypeError("r1 must be numeric.")

    if not isinstance(r2, (int, float)):
        raise TypeError("r2 must be numeric.")

    if r1 <= 0:
        raise ValueError("r1 must be positive.")

    if r2 <= 0:
        raise ValueError("r2 must be positive.")

    return float((r1 * r2) / (r1 + r2))


def voltage_divider(
    vin: Union[int, float],
    r1: Union[int, float],
    r2: Union[int, float],
) -> float:
    """Return the output voltage of a resistive voltage divider.

    V_out = V_in · R₂ / (R₁ + R₂).

    Args:
        vin: Input voltage in volts.
        r1: First (series) resistance in ohms (must be > 0).
        r2: Second (shunt) resistance in ohms (must be > 0).

    Returns:
        Output voltage in volts.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If r1 or r2 is not positive.

    Example:
        >>> voltage_divider(12, 8000, 4000)
        4.0

    Complexity: O(1)
    """
    if not isinstance(vin, (int, float)):
        raise TypeError("vin must be numeric.")

    if not isinstance(r1, (int, float)):
        raise TypeError("r1 must be numeric.")

    if not isinstance(r2, (int, float)):
        raise TypeError("r2 must be numeric.")

    if r1 <= 0:
        raise ValueError("r1 must be positive.")

    if r2 <= 0:
        raise ValueError("r2 must be positive.")

    return float(vin * r2 / (r1 + r2))


def specific_impulse(
    thrust: Union[int, float],
    mass_flow_rate: Union[int, float],
    gravity: float = 9.80665,
) -> float:
    """Return the specific impulse of a rocket engine.

    Isp = F / (ṁ · g₀).  A measure of propellant efficiency.

    Args:
        thrust: Thrust force in newtons (must be > 0).
        mass_flow_rate: Propellant mass flow rate in kg/s (> 0).
        gravity: Standard gravity in m/s² (default 9.80665).

    Returns:
        Specific impulse in seconds.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If thrust, mass_flow_rate, or gravity ≤ 0.

    Example:
        >>> round(specific_impulse(2_000_000, 700), 2)
        291.35

    Complexity: O(1)
    """
    for name, val in (("thrust", thrust), ("mass_flow_rate", mass_flow_rate),
                      ("gravity", gravity)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if thrust <= 0:
        raise ValueError("thrust must be positive.")

    if mass_flow_rate <= 0:
        raise ValueError("mass_flow_rate must be positive.")

    if gravity <= 0:
        raise ValueError("gravity must be positive.")

    return float(thrust / (mass_flow_rate * gravity))


def capacitive_reactance(
    frequency: Union[int, float],
    capacitance: Union[int, float],
) -> float:
    """Return the capacitive reactance of a capacitor.

    X_C = 1 / (2π · f · C).

    Args:
        frequency: Frequency in hertz (must be > 0).
        capacitance: Capacitance in farads (must be > 0).

    Returns:
        Capacitive reactance in ohms.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If frequency or capacitance ≤ 0.

    Example:
        >>> round(capacitive_reactance(60, 10e-6), 2)
        265.26

    Complexity: O(1)
    """
    if not isinstance(frequency, (int, float)):
        raise TypeError("frequency must be numeric.")

    if not isinstance(capacitance, (int, float)):
        raise TypeError("capacitance must be numeric.")

    if frequency <= 0:
        raise ValueError("frequency must be positive.")

    if capacitance <= 0:
        raise ValueError("capacitance must be positive.")

    return float(1 / (2 * math.pi * frequency * capacitance))


def inductive_reactance(
    frequency: Union[int, float],
    inductance: Union[int, float],
) -> float:
    """Return the inductive reactance of an inductor.

    X_L = 2π · f · L.

    Args:
        frequency: Frequency in hertz (must be > 0).
        inductance: Inductance in henries (must be > 0).

    Returns:
        Inductive reactance in ohms.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If frequency or inductance ≤ 0.

    Example:
        >>> round(inductive_reactance(60, 0.5), 4)
        188.4956

    Complexity: O(1)
    """
    if not isinstance(frequency, (int, float)):
        raise TypeError("frequency must be numeric.")

    if not isinstance(inductance, (int, float)):
        raise TypeError("inductance must be numeric.")

    if frequency <= 0:
        raise ValueError("frequency must be positive.")

    if inductance <= 0:
        raise ValueError("inductance must be positive.")

    return float(2 * math.pi * frequency * inductance)


def magnetic_flux_density(
    permeability: Union[int, float],
    current: Union[int, float],
    distance: Union[int, float],
) -> float:
    """Return the magnetic flux density around a long straight wire.

    B = μ · I / (2π · r).

    Args:
        permeability: Magnetic permeability of the medium (H/m, > 0).
        current: Current in amperes (must be > 0).
        distance: Distance from the wire in metres (must be > 0).

    Returns:
        Magnetic flux density in tesla.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0.

    Example:
        >>> round(magnetic_flux_density(1.2566370614e-6, 10, 0.05), 8)
        4e-05

    Complexity: O(1)
    """
    for name, val in (("permeability", permeability), ("current", current),
                      ("distance", distance)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val <= 0:
            raise ValueError(f"{name} must be positive.")

    return float(permeability * current / (2 * math.pi * distance))


def current_divider(
    total_current: Union[int, float],
    r_branch: Union[int, float],
    r_other: Union[int, float],
) -> float:
    """Return the branch current in a two-resistor current divider.

    I_branch = I_total · R_other / (R_branch + R_other).

    Args:
        total_current: Total current in amperes.
        r_branch: Resistance of the branch of interest (> 0).
        r_other: Resistance of the other branch (> 0).

    Returns:
        Branch current in amperes.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If either resistance ≤ 0.

    Example:
        >>> current_divider(10, 200, 100)
        3.3333333333333335

    Complexity: O(1)
    """
    for name, val in (("total_current", total_current),
                      ("r_branch", r_branch), ("r_other", r_other)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if r_branch <= 0:
        raise ValueError("r_branch must be positive.")

    if r_other <= 0:
        raise ValueError("r_other must be positive.")

    return float(total_current * r_other / (r_branch + r_other))


def buoyancy_force(
    fluid_density: Union[int, float],
    displaced_volume: Union[int, float],
    gravity: float = 9.80665,
) -> float:
    """Return the buoyancy force on an immersed object (Archimedes).

    F_b = ρ · V · g.

    Args:
        fluid_density: Density of the fluid in kg/m³ (must be > 0).
        displaced_volume: Displaced volume in m³ (must be > 0).
        gravity: Gravitational acceleration in m/s² (default 9.80665).

    Returns:
        Buoyancy force in newtons.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0.

    Example:
        >>> round(buoyancy_force(1000, 0.01), 4)
        98.0665

    Complexity: O(1)
    """
    for name, val in (("fluid_density", fluid_density),
                      ("displaced_volume", displaced_volume),
                      ("gravity", gravity)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val <= 0:
            raise ValueError(f"{name} must be positive.")

    return float(fluid_density * displaced_volume * gravity)


def grashof_number(
    gravity: Union[int, float],
    beta_coeff: Union[int, float],
    delta_temp: Union[int, float],
    length: Union[int, float],
    kinematic_viscosity: Union[int, float],
) -> float:
    """Return the Grashof number for natural convection.

    Gr = g · β · ΔT · L³ / ν².

    Args:
        gravity: Gravitational acceleration in m/s² (> 0).
        beta_coeff: Thermal expansion coefficient in 1/K (> 0).
        delta_temp: Temperature difference in K (must be > 0).
        length: Characteristic length in metres (> 0).
        kinematic_viscosity: Kinematic viscosity in m²/s (> 0).

    Returns:
        Grashof number (dimensionless).

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0.

    Example:
        >>> round(grashof_number(9.81, 3.41e-3, 20, 0.5, 1.5e-5), 0)
        371690000.0

    Complexity: O(1)
    """
    for name, val in (("gravity", gravity), ("beta_coeff", beta_coeff),
                      ("delta_temp", delta_temp), ("length", length),
                      ("kinematic_viscosity", kinematic_viscosity)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val <= 0:
            raise ValueError(f"{name} must be positive.")

    return float(
        gravity * beta_coeff * delta_temp * length ** 3
        / kinematic_viscosity ** 2
    )


def boyle_law_volume(
    p1: Union[int, float],
    v1: Union[int, float],
    p2: Union[int, float],
) -> float:
    """Return the new volume using Boyle's law.

    At constant temperature: P₁ · V₁ = P₂ · V₂  ⟹  V₂ = P₁ · V₁ / P₂.

    Args:
        p1: Initial pressure (must be > 0).
        v1: Initial volume (must be > 0).
        p2: Final pressure (must be > 0).

    Returns:
        Final volume as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0.

    Example:
        >>> boyle_law_volume(2, 10, 4)
        5.0

    Complexity: O(1)
    """
    for name, val in (("p1", p1), ("v1", v1), ("p2", p2)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val <= 0:
            raise ValueError(f"{name} must be positive.")

    return float(p1 * v1 / p2)


def charles_law_volume(
    v1: Union[int, float],
    t1: Union[int, float],
    t2: Union[int, float],
) -> float:
    """Return the new volume using Charles's law.

    At constant pressure: V₁ / T₁ = V₂ / T₂  ⟹  V₂ = V₁ · T₂ / T₁.
    Temperatures must be in kelvins.

    Args:
        v1: Initial volume (must be > 0).
        t1: Initial temperature in K (must be > 0).
        t2: Final temperature in K (must be > 0).

    Returns:
        Final volume as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0.

    Example:
        >>> charles_law_volume(10, 300, 600)
        20.0

    Complexity: O(1)
    """
    for name, val in (("v1", v1), ("t1", t1), ("t2", t2)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val <= 0:
            raise ValueError(f"{name} must be positive.")

    return float(v1 * t2 / t1)


def gay_lussac_pressure(
    p1: Union[int, float],
    t1: Union[int, float],
    t2: Union[int, float],
) -> float:
    """Return the new pressure using Gay-Lussac's law.

    At constant volume: P₁ / T₁ = P₂ / T₂  ⟹  P₂ = P₁ · T₂ / T₁.
    Temperatures in kelvins.

    Args:
        p1: Initial pressure (must be > 0).
        t1: Initial temperature in K (must be > 0).
        t2: Final temperature in K (must be > 0).

    Returns:
        Final pressure as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0.

    Example:
        >>> gay_lussac_pressure(100_000, 300, 600)
        200000.0

    Complexity: O(1)
    """
    for name, val in (("p1", p1), ("t1", t1), ("t2", t2)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val <= 0:
            raise ValueError(f"{name} must be positive.")

    return float(p1 * t2 / t1)


def rms_voltage(
    peak_voltage: Union[int, float],
) -> float:
    """Return the root-mean-square voltage from a sinusoidal peak.

    V_rms = V_peak / √2.

    Args:
        peak_voltage: Peak voltage in volts (must be ≥ 0).

    Returns:
        RMS voltage in volts.

    Raises:
        TypeError: If peak_voltage is not numeric.
        ValueError: If peak_voltage is negative.

    Example:
        >>> round(rms_voltage(325), 2)
        229.81

    Complexity: O(1)
    """
    if not isinstance(peak_voltage, (int, float)):
        raise TypeError("peak_voltage must be numeric.")

    if peak_voltage < 0:
        raise ValueError("peak_voltage must be non-negative.")

    return float(peak_voltage / math.sqrt(2))


def impedance_series_rlc(
    resistance: Union[int, float],
    inductive_react: Union[int, float],
    capacitive_react: Union[int, float],
) -> float:
    """Return the total impedance of a series RLC circuit.

    Z = √(R² + (X_L − X_C)²).

    Args:
        resistance: Resistance in ohms (must be ≥ 0).
        inductive_react: Inductive reactance X_L in ohms (≥ 0).
        capacitive_react: Capacitive reactance X_C in ohms (≥ 0).

    Returns:
        Impedance magnitude in ohms.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument is negative.

    Example:
        >>> impedance_series_rlc(100, 150, 50)
        141.42135623730951

    Complexity: O(1)
    """
    for name, val in (("resistance", resistance),
                      ("inductive_react", inductive_react),
                      ("capacitive_react", capacitive_react)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val < 0:
            raise ValueError(f"{name} must be non-negative.")

    return float(math.sqrt(resistance ** 2 + (inductive_react - capacitive_react) ** 2))


def nernst_potential(
    z: int,
    concentration_out: Union[int, float],
    concentration_in: Union[int, float],
    temperature: Union[int, float] = 310.15,
) -> float:
    """Return the Nernst equilibrium potential for an ion.

    E = (R · T) / (z · F) · ln(C_out / C_in).

    Args:
        z: Ion valence (charge number, ≠ 0).
        concentration_out: Extracellular concentration (> 0).
        concentration_in: Intracellular concentration (> 0).
        temperature: Temperature in kelvins (default 310.15 = 37 °C).

    Returns:
        Equilibrium potential in volts.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If concentrations ≤ 0 or z is zero.

    Example:
        >>> round(nernst_potential(1, 145, 12) * 1000, 1)
        66.6

    Complexity: O(1)
    """
    R_GAS = 8.314462618
    FARADAY = 96485.33212

    if not isinstance(z, int):
        raise TypeError("z must be an integer.")

    if z == 0:
        raise ValueError("z must not be zero.")

    for name, val in (("concentration_out", concentration_out),
                      ("concentration_in", concentration_in),
                      ("temperature", temperature)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val <= 0:
            raise ValueError(f"{name} must be positive.")

    return float(
        (R_GAS * temperature) / (z * FARADAY)
        * math.log(concentration_out / concentration_in)
    )


def heat_engine_efficiency(
    t_hot: Union[int, float],
    t_cold: Union[int, float],
) -> float:
    """Return the Carnot efficiency of a heat engine.

    η = 1 − T_cold / T_hot.  Temperatures in kelvins.

    Args:
        t_hot: Hot reservoir temperature in K (must be > 0).
        t_cold: Cold reservoir temperature in K (must be ≥ 0).

    Returns:
        Carnot efficiency as a float (0–1).

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If t_hot ≤ 0, t_cold < 0, or t_cold ≥ t_hot.

    Example:
        >>> round(heat_engine_efficiency(600, 300), 2)
        0.5

    Complexity: O(1)
    """
    if not isinstance(t_hot, (int, float)):
        raise TypeError("t_hot must be numeric.")

    if not isinstance(t_cold, (int, float)):
        raise TypeError("t_cold must be numeric.")

    if t_hot <= 0:
        raise ValueError("t_hot must be positive.")

    if t_cold < 0:
        raise ValueError("t_cold must be non-negative.")

    if t_cold >= t_hot:
        raise ValueError("t_cold must be less than t_hot.")

    return float(1 - t_cold / t_hot)


def biot_number(
    h: Union[int, float],
    l_c: Union[int, float],
    k: Union[int, float],
) -> float:
    """Return the Biot number for conductive heat transfer.

    Bi = h · L_c / k.  Used to determine whether a lumped-system
    analysis is valid (Bi < 0.1).

    Args:
        h: Convective heat transfer coefficient W/(m²·K) (> 0).
        l_c: Characteristic length in metres (> 0).
        k: Thermal conductivity of the solid W/(m·K) (> 0).

    Returns:
        Biot number (dimensionless).

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0.

    Example:
        >>> biot_number(50, 0.01, 200)
        0.0025

    Complexity: O(1)
    """
    for name, val in (("h", h), ("l_c", l_c), ("k", k)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val <= 0:
            raise ValueError(f"{name} must be positive.")

    return float(h * l_c / k)


def planck_radiation_peak(
    temperature: Union[int, float],
) -> float:
    """Return the spectral radiance at the Wien peak wavelength.

    Combines Wien's displacement law with the Planck function to
    give the peak spectral radiance B(λ_max, T).

    B_max ≈ 1.2865 × 10⁻⁵ · T⁵  (W/(m²·sr·m)).

    Args:
        temperature: Temperature in kelvins (must be > 0).

    Returns:
        Peak spectral radiance in W/(m²·sr·m).

    Raises:
        TypeError: If temperature is not numeric.
        ValueError: If temperature is not positive.

    Example:
        >>> round(planck_radiation_peak(5778), 0)
        82850947237685.0

    Complexity: O(1)
    """
    COEFF = 1.2865e-5

    if not isinstance(temperature, (int, float)):
        raise TypeError("temperature must be numeric.")

    if temperature <= 0:
        raise ValueError("temperature must be positive.")

    return float(COEFF * temperature ** 5)


def adiabatic_temperature(
    t1: Union[int, float],
    v1: Union[int, float],
    v2: Union[int, float],
    gamma: Union[int, float] = 1.4,
) -> float:
    """Return the final temperature after adiabatic expansion/compression.

    T₂ = T₁ · (V₁ / V₂)^(γ − 1).

    Args:
        t1: Initial temperature in K (must be > 0).
        v1: Initial volume (must be > 0).
        v2: Final volume (must be > 0).
        gamma: Heat capacity ratio (default 1.4 for air, > 1).

    Returns:
        Final temperature in kelvins.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any argument ≤ 0 or gamma ≤ 1.

    Example:
        >>> round(adiabatic_temperature(300, 1, 0.5), 2)
        395.85

    Complexity: O(1)
    """
    for name, val in (("t1", t1), ("v1", v1), ("v2", v2), ("gamma", gamma)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val <= 0:
            raise ValueError(f"{name} must be positive.")

    if gamma <= 1:
        raise ValueError("gamma must be greater than 1.")

    return float(t1 * (v1 / v2) ** (gamma - 1))


# ---------------------------------------------------------------------------
# Signal processing & engineering
# ---------------------------------------------------------------------------


def dft_magnitude(signal: list, k: int) -> float:
    """Computes the magnitude of the k-th DFT coefficient (standalone, no FFT).

    |X[k]| = |Σ x[n] · e^(−j2πkn/N)|

    Args:
        signal: List of real-valued samples.
        k: Frequency bin index (0 ≤ k < N).

    Returns:
        Magnitude of the k-th DFT coefficient.

    Raises:
        TypeError: If signal is not a list or k is not an integer.
        ValueError: If signal is empty or k is out of range.

    Example:
        >>> round(dft_magnitude([1, 0, -1, 0], 1), 6)
        2.0

    Complexity: O(N)
    """
    if not isinstance(signal, list):
        raise TypeError("signal must be a list")

    if not signal:
        raise ValueError("signal must not be empty")

    if not isinstance(k, int):
        raise TypeError("k must be an integer")

    n = len(signal)

    if k < 0 or k >= n:
        raise ValueError(f"k must be between 0 and {n - 1}")

    real_part = 0.0
    imag_part = 0.0

    for idx in range(n):
        angle = 2 * math.pi * k * idx / n
        real_part += signal[idx] * math.cos(angle)
        imag_part -= signal[idx] * math.sin(angle)

    return float(math.sqrt(real_part ** 2 + imag_part ** 2))


def dft_phase(signal: list, k: int) -> float:
    """Computes the phase (in radians) of the k-th DFT coefficient.

    Args:
        signal: List of real-valued samples.
        k: Frequency bin index (0 ≤ k < N).

    Returns:
        Phase in radians (−π to π).

    Raises:
        TypeError: If signal is not a list or k is not an integer.
        ValueError: If signal is empty or k is out of range.

    Example:
        >>> round(dft_phase([1, 0, -1, 0], 1), 6)
        -1.570796

    Complexity: O(N)
    """
    if not isinstance(signal, list):
        raise TypeError("signal must be a list")

    if not signal:
        raise ValueError("signal must not be empty")

    if not isinstance(k, int):
        raise TypeError("k must be an integer")

    n = len(signal)

    if k < 0 or k >= n:
        raise ValueError(f"k must be between 0 and {n - 1}")

    real_part = 0.0
    imag_part = 0.0

    for idx in range(n):
        angle = 2 * math.pi * k * idx / n
        real_part += signal[idx] * math.cos(angle)
        imag_part -= signal[idx] * math.sin(angle)

    return float(math.atan2(imag_part, real_part))


def signal_rms(samples: list) -> float:
    """Computes the RMS (Root Mean Square) of a discrete signal.

    RMS = √(Σx²/N)

    Args:
        samples: List of numeric sample values.

    Returns:
        RMS value of the signal.

    Raises:
        TypeError: If samples is not a list.
        ValueError: If samples is empty.

    Example:
        >>> round(signal_rms([1, -1, 1, -1]), 6)
        1.0

    Complexity: O(N)
    """
    if not isinstance(samples, list):
        raise TypeError("samples must be a list")

    if not samples:
        raise ValueError("samples must not be empty")

    sq_sum = sum(x ** 2 for x in samples)
    return float(math.sqrt(sq_sum / len(samples)))


def signal_snr_db(signal_power: float, noise_power: float) -> float:
    """Computes the signal-to-noise ratio in decibels.

    SNR(dB) = 10 · log₁₀(signal_power / noise_power)

    Args:
        signal_power: Signal power (positive).
        noise_power: Noise power (positive).

    Returns:
        SNR in decibels.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If either power is not positive.

    Example:
        >>> round(signal_snr_db(100, 1), 2)
        20.0

    Complexity: O(1)
    """
    if not isinstance(signal_power, (int, float)):
        raise TypeError("signal_power must be numeric")

    if not isinstance(noise_power, (int, float)):
        raise TypeError("noise_power must be numeric")

    if signal_power <= 0 or noise_power <= 0:
        raise ValueError("signal_power and noise_power must be positive")

    return float(10 * math.log10(signal_power / noise_power))


def nyquist_frequency(sample_rate: float) -> float:
    """Returns the Nyquist frequency for a given sample rate.

    f_Nyquist = sample_rate / 2

    Args:
        sample_rate: Sampling frequency in Hz (positive).

    Returns:
        Nyquist frequency in Hz.

    Raises:
        TypeError: If sample_rate is not numeric.
        ValueError: If sample_rate is not positive.

    Example:
        >>> nyquist_frequency(44100)
        22050.0

    Complexity: O(1)
    """
    if not isinstance(sample_rate, (int, float)):
        raise TypeError("sample_rate must be numeric")

    if sample_rate <= 0:
        raise ValueError("sample_rate must be positive")

    return float(sample_rate / 2)


def decibel_sum(db_a: float, db_b: float) -> float:
    """Logarithmic addition of two sound levels in decibels.

    dB_total = 10 · log₁₀(10^(dB_a/10) + 10^(dB_b/10))

    Args:
        db_a: First sound level in dB.
        db_b: Second sound level in dB.

    Returns:
        Combined sound level in dB.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> round(decibel_sum(90, 90), 2)
        93.01

    Complexity: O(1)
    """
    if not isinstance(db_a, (int, float)):
        raise TypeError("db_a must be numeric")

    if not isinstance(db_b, (int, float)):
        raise TypeError("db_b must be numeric")

    return float(10 * math.log10(10 ** (db_a / 10) + 10 ** (db_b / 10)))


def stefan_boltzmann_temperature(
    power: float, emissivity: float, area: float
) -> float:
    """Calculates temperature from radiated power (inverse Stefan-Boltzmann).

    T = (P / (ε · σ · A))^(1/4)

    Args:
        power: Radiated power in Watts.
        emissivity: Surface emissivity (0 < ε ≤ 1).
        area: Surface area in m².

    Returns:
        Temperature in Kelvin.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If parameters are not positive or emissivity > 1.

    Example:
        >>> round(stefan_boltzmann_temperature(500, 0.9, 1.0), 1)
        306.4

    Complexity: O(1)
    """
    sigma = 5.670374419e-8  # Stefan-Boltzmann constant

    for name, val in (("power", power), ("emissivity", emissivity), ("area", area)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if power <= 0 or area <= 0:
        raise ValueError("power and area must be positive")

    if not 0 < emissivity <= 1:
        raise ValueError("emissivity must be in (0, 1]")

    return float((power / (emissivity * sigma * area)) ** 0.25)


def bending_moment(force: float, distance: float) -> float:
    """Calculates the bending moment M = F × d.

    Args:
        force: Applied force in Newtons.
        distance: Perpendicular distance from pivot in metres.

    Returns:
        Bending moment in N·m.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> bending_moment(100, 2.5)
        250.0

    Complexity: O(1)
    """
    if not isinstance(force, (int, float)):
        raise TypeError("force must be numeric")

    if not isinstance(distance, (int, float)):
        raise TypeError("distance must be numeric")

    return float(force * distance)


def stress(force: float, area: float) -> float:
    """Calculates mechanical stress σ = F / A.

    Args:
        force: Applied force in Newtons.
        area: Cross-sectional area in m².

    Returns:
        Stress in Pascals (N/m²).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If area is not positive.

    Example:
        >>> stress(1000, 0.01)
        100000.0

    Complexity: O(1)
    """
    if not isinstance(force, (int, float)):
        raise TypeError("force must be numeric")

    if not isinstance(area, (int, float)):
        raise TypeError("area must be numeric")

    if area <= 0:
        raise ValueError("area must be positive")

    return float(force / area)


def strain(change_in_length: float, original_length: float) -> float:
    """Calculates engineering strain ε = ΔL / L₀.

    Args:
        change_in_length: Change in length ΔL.
        original_length: Original length L₀ (positive).

    Returns:
        Dimensionless strain.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If original_length is not positive.

    Example:
        >>> strain(0.005, 1.0)
        0.005

    Complexity: O(1)
    """
    if not isinstance(change_in_length, (int, float)):
        raise TypeError("change_in_length must be numeric")

    if not isinstance(original_length, (int, float)):
        raise TypeError("original_length must be numeric")

    if original_length <= 0:
        raise ValueError("original_length must be positive")

    return float(change_in_length / original_length)


def luminous_flux(candela: float, solid_angle_sr: float = 4 * 3.141592653589793) -> float:
    """Convert luminous intensity (candela) to luminous flux (lumens).

    Φ = I × Ω, where Ω is the solid angle in steradians.
    Default Ω = 4π (full sphere).

    Args:
        candela: Luminous intensity in candela.
        solid_angle_sr: Solid angle in steradians (default 4π).

    Returns:
        Luminous flux in lumens.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If *candela* or *solid_angle_sr* is negative.

    Example:
        >>> round(luminous_flux(1.0), 2)
        12.57

    Complexity: O(1)
    """
    if not isinstance(candela, (int, float)):
        raise TypeError("candela must be numeric")

    if not isinstance(solid_angle_sr, (int, float)):
        raise TypeError("solid_angle_sr must be numeric")

    if candela < 0 or solid_angle_sr < 0:
        raise ValueError("candela and solid_angle_sr must be non-negative")

    return float(candela * solid_angle_sr)


def noise_figure_to_temperature(nf_db: float, t0: float = 290.0) -> float:
    """Convert noise figure (dB) to equivalent noise temperature (Kelvin).

    T_e = T₀ × (10^(NF/10) − 1).

    Args:
        nf_db: Noise figure in decibels.
        t0: Reference temperature in Kelvin (default 290 K).

    Returns:
        Noise temperature in Kelvin.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If *t0* is not positive.

    Example:
        >>> round(noise_figure_to_temperature(3.0), 1)
        288.6

    Complexity: O(1)
    """
    if not isinstance(nf_db, (int, float)):
        raise TypeError("nf_db must be numeric")

    if not isinstance(t0, (int, float)):
        raise TypeError("t0 must be numeric")

    if t0 <= 0:
        raise ValueError("t0 must be positive")

    return float(t0 * (10 ** (nf_db / 10) - 1))


def antenna_gain_to_effective_area(
    gain_dbi: float,
    frequency_hz: float,
) -> float:
    """Convert antenna gain (dBi) to effective aperture area (m²).

    A_e = (λ² × G) / (4π), where G is linear gain.

    Args:
        gain_dbi: Antenna gain in dBi.
        frequency_hz: Operating frequency in Hz.

    Returns:
        Effective area in square meters.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If *frequency_hz* is not positive.

    Example:
        >>> round(antenna_gain_to_effective_area(10, 1e9), 4)
        0.7162

    Complexity: O(1)
    """
    if not isinstance(gain_dbi, (int, float)):
        raise TypeError("gain_dbi must be numeric")

    if not isinstance(frequency_hz, (int, float)):
        raise TypeError("frequency_hz must be numeric")

    if frequency_hz <= 0:
        raise ValueError("frequency_hz must be positive")

    c = 299_792_458.0
    lam = c / frequency_hz
    g_linear = 10 ** (gain_dbi / 10)
    return float((lam ** 2 * g_linear) / (4 * math.pi))


_DOSE_TO_SV: dict[str, float] = {
    "sv": 1.0,
    "msv": 1e-3,
    "usv": 1e-6,
    "rem": 0.01,
    "mrem": 1e-5,
    "gy": 1.0,          # assuming radiation weighting factor = 1
    "mgy": 1e-3,
    "rad": 0.01,
}


def radiation_dose_convert(
    value: float,
    from_unit: str,
    to_unit: str,
) -> float:
    """Convert between radiation dose units.

    Supported units: ``sv``, ``msv``, ``usv``, ``rem``, ``mrem``,
    ``gy``, ``mgy``, ``rad``.

    Note: Gy-to-Sv conversion assumes a radiation weighting factor of 1
    (photons / electrons).

    Args:
        value: Numeric dose value.
        from_unit: Source unit (case-insensitive).
        to_unit: Target unit (case-insensitive).

    Returns:
        Converted value.

    Raises:
        TypeError: If *value* is not numeric.
        ValueError: If units are not recognized.

    Example:
        >>> radiation_dose_convert(1, "sv", "rem")
        100.0
        >>> radiation_dose_convert(500, "mrem", "msv")
        5.0

    Complexity: O(1)
    """
    if not isinstance(value, (int, float)):
        raise TypeError("value must be numeric")

    f = from_unit.lower()
    t = to_unit.lower()

    if f not in _DOSE_TO_SV:
        raise ValueError(f"Unknown from_unit: {from_unit!r}")

    if t not in _DOSE_TO_SV:
        raise ValueError(f"Unknown to_unit: {to_unit!r}")

    sv = value * _DOSE_TO_SV[f]
    return float(sv / _DOSE_TO_SV[t])


def color_temperature_to_rgb(kelvin: float) -> tuple[int, int, int]:
    """Convert a colour temperature (Kelvin) to an approximate RGB tuple.

    Uses Tanner Helland's algorithm for the range 1000-40000 K.

    Args:
        kelvin: Colour temperature in Kelvin.

    Returns:
        Tuple ``(R, G, B)`` with values in [0, 255].

    Raises:
        TypeError: If *kelvin* is not numeric.
        ValueError: If *kelvin* < 1000 or > 40000.

    Example:
        >>> color_temperature_to_rgb(6500)
        (255, 254, 250)

    Complexity: O(1)
    """
    if not isinstance(kelvin, (int, float)):
        raise TypeError("kelvin must be numeric")

    if kelvin < 1000 or kelvin > 40000:
        raise ValueError("kelvin must be between 1000 and 40000")

    temp = kelvin / 100.0

    # Red
    if temp <= 66:
        red = 255
    else:
        red = 329.698727446 * ((temp - 60) ** -0.1332047592)

    # Green
    if temp <= 66:
        green = 99.4708025861 * math.log(temp) - 161.1195681661
    else:
        green = 288.1221695283 * ((temp - 60) ** -0.0755148492)

    # Blue
    if temp >= 66:
        blue = 255
    elif temp <= 19:
        blue = 0
    else:
        blue = 138.5177312231 * math.log(temp - 10) - 305.0447927307

    def _clamp(v: float) -> int:
        return max(0, min(255, round(v)))

    return (_clamp(red), _clamp(green), _clamp(blue))


def rgb_to_hsl(r: int, g: int, b: int) -> tuple[float, float, float]:
    """Convert RGB colour to HSL.

    Args:
        r: Red (0-255).
        g: Green (0-255).
        b: Blue (0-255).

    Returns:
        Tuple ``(h, s, l)`` where *h* is in [0, 360) and *s*, *l* in [0, 1].

    Raises:
        TypeError: If arguments are not integers.
        ValueError: If values are outside [0, 255].

    Example:
        >>> rgb_to_hsl(255, 0, 0)
        (0.0, 1.0, 0.5)

    Complexity: O(1)
    """
    for name, val in (("r", r), ("g", g), ("b", b)):

        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer")

        if val < 0 or val > 255:
            raise ValueError(f"{name} must be 0-255, got {val}")

    r_n, g_n, b_n = r / 255.0, g / 255.0, b / 255.0
    c_max = max(r_n, g_n, b_n)
    c_min = min(r_n, g_n, b_n)
    delta = c_max - c_min

    # Lightness
    lightness = (c_max + c_min) / 2.0

    if delta == 0:
        h = 0.0
        s = 0.0
    else:
        s = delta / (1 - abs(2 * lightness - 1))

        if c_max == r_n:
            h = 60.0 * (((g_n - b_n) / delta) % 6)
        elif c_max == g_n:
            h = 60.0 * (((b_n - r_n) / delta) + 2)
        else:
            h = 60.0 * (((r_n - g_n) / delta) + 4)

    return (round(h, 4), round(s, 4), round(lightness, 4))


def hsl_to_rgb(h: float, s: float, lightness: float) -> tuple[int, int, int]:
    """Convert HSL colour to RGB.

    Args:
        h: Hue in [0, 360).
        s: Saturation in [0, 1].
        lightness: Lightness in [0, 1].

    Returns:
        Tuple ``(R, G, B)`` with values in [0, 255].

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If values are out of range.

    Example:
        >>> hsl_to_rgb(0.0, 1.0, 0.5)
        (255, 0, 0)

    Complexity: O(1)
    """
    for name, val in (("h", h), ("s", s), ("lightness", lightness)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if h < 0 or h >= 360:
        raise ValueError("h must be in [0, 360)")

    if s < 0 or s > 1:
        raise ValueError("s must be in [0, 1]")

    if lightness < 0 or lightness > 1:
        raise ValueError("lightness must be in [0, 1]")

    c = (1 - abs(2 * lightness - 1)) * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = lightness - c / 2

    if h < 60:
        r1, g1, b1 = c, x, 0.0
    elif h < 120:
        r1, g1, b1 = x, c, 0.0
    elif h < 180:
        r1, g1, b1 = 0.0, c, x
    elif h < 240:
        r1, g1, b1 = 0.0, x, c
    elif h < 300:
        r1, g1, b1 = x, 0.0, c
    else:
        r1, g1, b1 = c, 0.0, x

    return (round((r1 + m) * 255), round((g1 + m) * 255), round((b1 + m) * 255))


def signal_to_noise_ratio(
    signal_power: float,
    noise_power: float,
) -> float:
    """Compute the signal-to-noise ratio in decibels.

    SNR(dB) = 10 × log₁₀(signal_power / noise_power)

    Args:
        signal_power: Signal power (positive).
        noise_power: Noise power (positive).

    Returns:
        SNR in dB.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If either power is not positive.

    Example:
        >>> round(signal_to_noise_ratio(100, 1), 2)
        20.0

    Complexity: O(1)
    """
    for name, val in (("signal_power", signal_power), ("noise_power", noise_power)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

        if val <= 0:
            raise ValueError(f"{name} must be positive")

    return float(round(10.0 * math.log10(signal_power / noise_power), 4))


def wavelength_to_frequency(wavelength_m: float) -> float:
    """Convert electromagnetic wavelength to frequency.

    f = c / λ, where c = 299 792 458 m/s (speed of light in vacuum).

    Args:
        wavelength_m: Wavelength in metres (positive).

    Returns:
        Frequency in hertz.

    Raises:
        TypeError: If *wavelength_m* is not numeric.
        ValueError: If *wavelength_m* <= 0.

    Example:
        >>> wavelength_to_frequency(0.5e-6)
        599584916000000.0

    Complexity: O(1)
    """
    if not isinstance(wavelength_m, (int, float)):
        raise TypeError("wavelength_m must be numeric")

    if wavelength_m <= 0:
        raise ValueError("wavelength_m must be positive")

    c = 299_792_458.0
    return float(c / wavelength_m)


def frequency_to_wavelength(frequency_hz: float) -> float:
    """Convert electromagnetic frequency to wavelength.

    λ = c / f, where c = 299 792 458 m/s.

    Args:
        frequency_hz: Frequency in hertz (positive).

    Returns:
        Wavelength in metres.

    Raises:
        TypeError: If *frequency_hz* is not numeric.
        ValueError: If *frequency_hz* <= 0.

    Example:
        >>> round(frequency_to_wavelength(100e6), 4)
        2.9979

    Complexity: O(1)
    """
    if not isinstance(frequency_hz, (int, float)):
        raise TypeError("frequency_hz must be numeric")

    if frequency_hz <= 0:
        raise ValueError("frequency_hz must be positive")

    c = 299_792_458.0
    return float(c / frequency_hz)


def prandtl_number(
    cp: Union[int, float],
    mu: Union[int, float],
    k: Union[int, float],
) -> float:
    """Calculate the Prandtl number Pr = Cp · μ / k.

    Dimensionless number relating momentum diffusivity to thermal
    diffusivity in heat-transfer problems.

    Args:
        cp: Specific heat capacity (J/(kg·K)).
        mu: Dynamic viscosity (Pa·s).
        k: Thermal conductivity (W/(m·K)).

    Returns:
        Prandtl number (dimensionless).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If k is zero or any value is negative.

    Example:
        >>> prandtl_number(4182, 0.001, 0.6)
        6.97

    Complexity: O(1)
    """
    for name, val in (("cp", cp), ("mu", mu), ("k", k)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val < 0:
            raise ValueError(f"{name} must be non-negative.")

    if k == 0:
        raise ValueError("k must not be zero.")

    return float(round(cp * mu / k, 2))


def froude_number(
    v: Union[int, float],
    g: Union[int, float],
    length: Union[int, float],
) -> float:
    """Calculate the Froude number Fr = v / √(g · L).

    Dimensionless number comparing flow inertia to gravity effects
    in open-channel hydraulics and ship hydrodynamics.

    Args:
        v: Flow velocity (m/s).
        g: Gravitational acceleration (m/s²).
        length: Characteristic length (m).

    Returns:
        Froude number (dimensionless).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If g or length are non-positive.

    Example:
        >>> round(froude_number(5, 9.81, 2), 4)
        1.1288

    Complexity: O(1)
    """
    for name, val in (("v", v), ("g", g), ("length", length)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if g <= 0:
        raise ValueError("g must be positive.")

    if length <= 0:
        raise ValueError("length must be positive.")

    return float(v / math.sqrt(g * length))


def weber_number(
    rho: Union[int, float],
    v: Union[int, float],
    length: Union[int, float],
    sigma: Union[int, float],
) -> float:
    """Calculate the Weber number We = ρ · v² · L / σ.

    Dimensionless number relating inertia to surface tension,
    important in droplet formation and atomisation.

    Args:
        rho: Fluid density (kg/m³).
        v: Flow velocity (m/s).
        length: Characteristic length (m).
        sigma: Surface tension (N/m).

    Returns:
        Weber number (dimensionless).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If sigma is zero or any value is negative.

    Example:
        >>> weber_number(1000, 2, 0.01, 0.072)
        555.5555555555555

    Complexity: O(1)
    """
    for name, val in (("rho", rho), ("v", v), ("length", length), ("sigma", sigma)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if sigma == 0:
        raise ValueError("sigma must not be zero.")

    return float(rho * v ** 2 * length / sigma)


def ph_to_h_concentration(ph: float) -> float:
    """Convert pH to hydrogen ion concentration [H⁺].

    Description:
        [H⁺] = 10^(−pH).  Fundamental conversion in chemistry.

    Args:
        ph: The pH value.

    Returns:
        Hydrogen ion concentration in mol/L.

    Raises:
        TypeError: If *ph* is not numeric.

    Usage Example:
        >>> ph_to_h_concentration(7.0)
        1e-07

    Complexity: O(1)
    """
    if not isinstance(ph, (int, float)):
        raise TypeError("ph must be numeric.")

    return float(10 ** (-ph))


def h_concentration_to_ph(concentration: float) -> float:
    """Convert hydrogen ion concentration [H⁺] to pH.

    Description:
        pH = −log₁₀([H⁺]).  Inverse of ``ph_to_h_concentration``.

    Args:
        concentration: Hydrogen ion concentration in mol/L (> 0).

    Returns:
        pH value.

    Raises:
        TypeError: If *concentration* is not numeric.
        ValueError: If *concentration* is not positive.

    Usage Example:
        >>> h_concentration_to_ph(1e-7)
        7.0

    Complexity: O(1)
    """
    if not isinstance(concentration, (int, float)):
        raise TypeError("concentration must be numeric.")

    if concentration <= 0:
        raise ValueError("concentration must be positive.")

    return float(-math.log10(concentration))


def nusselt_number(h: float, length: float, k: float) -> float:
    """Compute the Nusselt number for convective heat transfer.

    Description:
        Nu = h × L / k, where *h* is the convective heat transfer
        coefficient, *L* is the characteristic length, and *k* is
        the thermal conductivity of the fluid.

    Args:
        h: Convective heat transfer coefficient (W/(m²·K)).
        length: Characteristic length (m).
        k: Thermal conductivity (W/(m·K)).

    Returns:
        Dimensionless Nusselt number.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If *k* is zero.

    Usage Example:
        >>> nusselt_number(50.0, 0.5, 0.6)
        41.666666666666664

    Complexity: O(1)
    """
    for name, val in (("h", h), ("length", length), ("k", k)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if k == 0:
        raise ValueError("k (thermal conductivity) must not be zero.")

    return float(h * length / k)


def strouhal_number(freq: float, length: float, velocity: float) -> float:
    """Compute the Strouhal number for oscillating flow.

    Description:
        St = f × L / v, a dimensionless number describing vortex
        shedding and oscillating flow mechanisms.

    Args:
        freq: Frequency of vortex shedding (Hz).
        length: Characteristic length (m).
        velocity: Flow velocity (m/s).

    Returns:
        Dimensionless Strouhal number.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If *velocity* is zero.

    Usage Example:
        >>> strouhal_number(10.0, 0.1, 5.0)
        0.2

    Complexity: O(1)
    """
    for name, val in (("freq", freq), ("length", length), ("velocity", velocity)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if velocity == 0:
        raise ValueError("velocity must not be zero.")

    return float(freq * length / velocity)


def knudsen_number(mean_free_path: float, length: float) -> float:
    """Compute the Knudsen number for rarefied gas dynamics.

    Description:
        Kn = λ / L, the ratio of the molecular mean free path to
        the characteristic physical length.  Determines the flow
        regime: Kn < 0.01 continuum, 0.01–0.1 slip, 0.1–10
        transitional, Kn > 10 free molecular.

    Args:
        mean_free_path: Molecular mean free path (m).
        length: Characteristic length (m).

    Returns:
        Dimensionless Knudsen number.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If *length* is zero.

    Usage Example:
        >>> knudsen_number(6.8e-8, 0.001)
        6.8e-05

    Complexity: O(1)
    """
    for name, val in (("mean_free_path", mean_free_path), ("length", length)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if length == 0:
        raise ValueError("length must not be zero.")

    return float(mean_free_path / length)


# ---------------------------------------------------------------------------
# Colour-space conversions (standalone, no numpy/PIL)
# ---------------------------------------------------------------------------


def rgb_to_hsv(r: int, g: int, b: int) -> tuple:
    """Convert RGB colour to HSV (Hue, Saturation, Value).

    Description:
        H in [0, 360), S in [0, 1], V in [0, 1].

    Args:
        r: Red channel (0–255).
        g: Green channel (0–255).
        b: Blue channel (0–255).

    Returns:
        Tuple (h, s, v).

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If any channel is outside 0–255.

    Usage Example:
        >>> rgb_to_hsv(255, 128, 0)
        (30.11764705882353, 1.0, 1.0)

    Complexity: O(1)
    """
    for name, val in (("r", r), ("g", g), ("b", b)):

        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer.")

        if val < 0 or val > 255:
            raise ValueError(f"{name} must be in [0, 255].")

    rn, gn, bn = r / 255.0, g / 255.0, b / 255.0
    c_max = max(rn, gn, bn)
    c_min = min(rn, gn, bn)
    delta = c_max - c_min

    # Hue
    if delta == 0:
        h = 0.0
    elif c_max == rn:
        h = 60.0 * (((gn - bn) / delta) % 6)
    elif c_max == gn:
        h = 60.0 * (((bn - rn) / delta) + 2)
    else:
        h = 60.0 * (((rn - gn) / delta) + 4)

    # Saturation
    s = 0.0 if c_max == 0 else delta / c_max

    return (h, s, c_max)


def hsv_to_rgb(h: float, s: float, v: float) -> tuple:
    """Convert HSV colour to RGB.

    Args:
        h: Hue in [0, 360).
        s: Saturation in [0, 1].
        v: Value in [0, 1].

    Returns:
        Tuple (r, g, b) with values in 0–255.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If values are out of range.

    Usage Example:
        >>> hsv_to_rgb(30.0, 1.0, 1.0)
        (255, 128, 0)

    Complexity: O(1)
    """
    for name, val in (("h", h), ("s", s), ("v", v)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if h < 0 or h >= 360:
        raise ValueError("h must be in [0, 360).")

    if s < 0 or s > 1 or v < 0 or v > 1:
        raise ValueError("s and v must be in [0, 1].")

    c = v * s
    x = c * (1 - abs((h / 60) % 2 - 1))
    m = v - c

    if h < 60:
        rp, gp, bp = c, x, 0.0
    elif h < 120:
        rp, gp, bp = x, c, 0.0
    elif h < 180:
        rp, gp, bp = 0.0, c, x
    elif h < 240:
        rp, gp, bp = 0.0, x, c
    elif h < 300:
        rp, gp, bp = x, 0.0, c
    else:
        rp, gp, bp = c, 0.0, x

    return (round((rp + m) * 255), round((gp + m) * 255), round((bp + m) * 255))


def rgb_to_cmyk(r: int, g: int, b: int) -> tuple:
    """Convert RGB colour to CMYK (Cyan, Magenta, Yellow, Key/Black).

    Description:
        All output channels in [0, 1].

    Args:
        r: Red channel (0–255).
        g: Green channel (0–255).
        b: Blue channel (0–255).

    Returns:
        Tuple (c, m, y, k).

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If any channel is outside 0–255.

    Usage Example:
        >>> rgb_to_cmyk(255, 0, 0)
        (0.0, 1.0, 1.0, 0.0)

    Complexity: O(1)
    """
    for name, val in (("r", r), ("g", g), ("b", b)):

        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer.")

        if val < 0 or val > 255:
            raise ValueError(f"{name} must be in [0, 255].")

    rn, gn, bn = r / 255.0, g / 255.0, b / 255.0
    k = 1.0 - max(rn, gn, bn)

    if k == 1.0:
        return (0.0, 0.0, 0.0, 1.0)

    c = (1.0 - rn - k) / (1.0 - k)
    m = (1.0 - gn - k) / (1.0 - k)
    y = (1.0 - bn - k) / (1.0 - k)

    return (c, m, y, k)


def cmyk_to_rgb(c: float, m: float, y: float, k: float) -> tuple:
    """Convert CMYK colour to RGB.

    Args:
        c: Cyan in [0, 1].
        m: Magenta in [0, 1].
        y: Yellow in [0, 1].
        k: Key/Black in [0, 1].

    Returns:
        Tuple (r, g, b) with values in 0–255.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If any channel is outside [0, 1].

    Usage Example:
        >>> cmyk_to_rgb(0.0, 1.0, 1.0, 0.0)
        (255, 0, 0)

    Complexity: O(1)
    """
    for name, val in (("c", c), ("m", m), ("y", y), ("k", k)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

        if val < 0 or val > 1:
            raise ValueError(f"{name} must be in [0, 1].")

    r = round(255 * (1 - c) * (1 - k))
    g = round(255 * (1 - m) * (1 - k))
    b = round(255 * (1 - y) * (1 - k))

    return (r, g, b)


def color_luminance(r: int, g: int, b: int) -> float:
    """Relative luminance of an sRGB colour per WCAG 2.1.

    Description:
        L = 0.2126 R + 0.7152 G + 0.0722 B, where each channel is
        linearised from the sRGB gamma curve.

    Args:
        r: Red channel (0–255).
        g: Green channel (0–255).
        b: Blue channel (0–255).

    Returns:
        Relative luminance in [0, 1].

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If any channel is outside 0–255.

    Usage Example:
        >>> round(color_luminance(255, 255, 255), 1)
        1.0
        >>> round(color_luminance(0, 0, 0), 1)
        0.0

    Complexity: O(1)
    """
    for name, val in (("r", r), ("g", g), ("b", b)):

        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer.")

        if val < 0 or val > 255:
            raise ValueError(f"{name} must be in [0, 255].")

    def _linearise(channel: int) -> float:
        c = channel / 255.0
        return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4

    return 0.2126 * _linearise(r) + 0.7152 * _linearise(g) + 0.0722 * _linearise(b)


def color_contrast_ratio(r1: int, g1: int, b1: int,
                         r2: int, g2: int, b2: int) -> float:
    """WCAG 2.1 contrast ratio between two sRGB colours.

    Description:
        Ratio = (L_lighter + 0.05) / (L_darker + 0.05), ranging
        from 1:1 (identical) to 21:1 (black vs white).

    Args:
        r1, g1, b1: First colour RGB channels (0–255 each).
        r2, g2, b2: Second colour RGB channels (0–255 each).

    Returns:
        Contrast ratio as a float (>= 1.0).

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If any channel is outside 0–255.

    Usage Example:
        >>> color_contrast_ratio(0, 0, 0, 255, 255, 255)
        21.0
        >>> color_contrast_ratio(255, 255, 255, 255, 255, 255)
        1.0

    Complexity: O(1)
    """
    l1 = color_luminance(r1, g1, b1)
    l2 = color_luminance(r2, g2, b2)
    lighter = max(l1, l2)
    darker = min(l1, l2)

    return float((lighter + 0.05) / (darker + 0.05))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 9: Unit Conversions (scientific, flow, data, density)
# ---------------------------------------------------------------------------

def pascals_to_atmospheres(pa: float) -> float:
    """Convert pascals to standard atmospheres.

    Args:
        pa: Pressure in pascals.

    Returns:
        Pressure in atmospheres.

    Raises:
        TypeError: If pa is not numeric.

    Usage Example:
        >>> round(pascals_to_atmospheres(101325), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(pa, (int, float)):
        raise TypeError("pa must be numeric.")
    return float(pa / 101325.0)


def atmospheres_to_pascals(atm: float) -> float:
    """Convert standard atmospheres to pascals.

    Args:
        atm: Pressure in atmospheres.

    Returns:
        Pressure in pascals.

    Raises:
        TypeError: If atm is not numeric.

    Usage Example:
        >>> atmospheres_to_pascals(1)
        101325.0

    Complexity: O(1)
    """
    if not isinstance(atm, (int, float)):
        raise TypeError("atm must be numeric.")
    return float(atm * 101325.0)


def bars_to_pascals(bars: float) -> float:
    """Convert bars to pascals.

    Args:
        bars: Pressure in bars.

    Returns:
        Pressure in pascals.

    Raises:
        TypeError: If bars is not numeric.

    Usage Example:
        >>> bars_to_pascals(1)
        100000.0

    Complexity: O(1)
    """
    if not isinstance(bars, (int, float)):
        raise TypeError("bars must be numeric.")
    return float(bars * 100000.0)


def pascals_to_bars(pa: float) -> float:
    """Convert pascals to bars.

    Args:
        pa: Pressure in pascals.

    Returns:
        Pressure in bars.

    Raises:
        TypeError: If pa is not numeric.

    Usage Example:
        >>> pascals_to_bars(100000)
        1.0

    Complexity: O(1)
    """
    if not isinstance(pa, (int, float)):
        raise TypeError("pa must be numeric.")
    return float(pa / 100000.0)


def psi_to_pascals(psi: float) -> float:
    """Convert pounds per square inch (PSI) to pascals.

    Args:
        psi: Pressure in PSI.

    Returns:
        Pressure in pascals.

    Raises:
        TypeError: If psi is not numeric.

    Usage Example:
        >>> round(psi_to_pascals(14.696), 0)
        101325.0

    Complexity: O(1)
    """
    if not isinstance(psi, (int, float)):
        raise TypeError("psi must be numeric.")
    return float(psi * 6894.757293168)


def pascals_to_psi(pa: float) -> float:
    """Convert pascals to pounds per square inch (PSI).

    Args:
        pa: Pressure in pascals.

    Returns:
        Pressure in PSI.

    Raises:
        TypeError: If pa is not numeric.

    Usage Example:
        >>> round(pascals_to_psi(101325), 3)
        14.696

    Complexity: O(1)
    """
    if not isinstance(pa, (int, float)):
        raise TypeError("pa must be numeric.")
    return float(pa / 6894.757293168)


def liters_per_minute_to_cubic_meters_per_second(lpm: float) -> float:
    """Convert liters per minute to cubic meters per second.

    Args:
        lpm: Flow rate in liters per minute.

    Returns:
        Flow rate in m³/s.

    Raises:
        TypeError: If lpm is not numeric.

    Usage Example:
        >>> round(liters_per_minute_to_cubic_meters_per_second(60), 6)
        0.001

    Complexity: O(1)
    """
    if not isinstance(lpm, (int, float)):
        raise TypeError("lpm must be numeric.")
    return float(lpm / 60000.0)


def cubic_meters_per_second_to_liters_per_minute(cms: float) -> float:
    """Convert cubic meters per second to liters per minute.

    Args:
        cms: Flow rate in m³/s.

    Returns:
        Flow rate in liters per minute.

    Raises:
        TypeError: If cms is not numeric.

    Usage Example:
        >>> cubic_meters_per_second_to_liters_per_minute(0.001)
        60.0

    Complexity: O(1)
    """
    if not isinstance(cms, (int, float)):
        raise TypeError("cms must be numeric.")
    return float(cms * 60000.0)


def bytes_to_human_readable(size_bytes: int) -> str:
    """Convert bytes to human-readable string (B, KB, MB, GB, TB).

    Uses binary prefixes (1 KB = 1024 B).

    Args:
        size_bytes: Size in bytes (≥ 0).

    Returns:
        Formatted string like ``'1.50 MB'``.

    Raises:
        TypeError: If size_bytes is not an integer.
        ValueError: If size_bytes is negative.

    Usage Example:
        >>> bytes_to_human_readable(1572864)
        '1.50 MB'

    Complexity: O(1)
    """
    if not isinstance(size_bytes, int):
        raise TypeError("size_bytes must be an integer.")
    if size_bytes < 0:
        raise ValueError("size_bytes must be non-negative.")

    for unit in ("B", "KB", "MB", "GB"):
        if abs(size_bytes) < 1024:
            return f"{size_bytes:.2f} {unit}" if unit != "B" else f"{size_bytes} B"
        size_bytes /= 1024.0
    return f"{size_bytes:.2f} TB"


def density_to_specific_gravity(density: float, reference: float = 997.0) -> float:
    """Convert density to specific gravity relative to a reference.

    SG = ρ / ρ_ref.  Default reference is water at 25 °C (997 kg/m³).

    Args:
        density: Material density in kg/m³.
        reference: Reference density in kg/m³ (default 997.0, > 0).

    Returns:
        Specific gravity as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If reference is not positive.

    Usage Example:
        >>> round(density_to_specific_gravity(7874), 2)
        7.9

    Complexity: O(1)
    """
    if not isinstance(density, (int, float)):
        raise TypeError("density must be numeric.")
    if not isinstance(reference, (int, float)):
        raise TypeError("reference must be numeric.")
    if reference <= 0:
        raise ValueError("reference must be positive.")
    return float(density / reference)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 10: Energy, Power, Angle & Misc Conversions
# ---------------------------------------------------------------------------

def joules_to_calories(joules: float) -> float:
    """Convert joules to thermochemical calories.

    Args:
        joules: Energy in joules.

    Returns:
        Energy in calories.

    Raises:
        TypeError: If joules is not numeric.

    Usage Example:
        >>> round(joules_to_calories(4184), 2)
        1000.0

    Complexity: O(1)
    """
    if not isinstance(joules, (int, float)):
        raise TypeError("joules must be numeric.")
    return float(joules / 4.184)


def calories_to_joules(cal: float) -> float:
    """Convert thermochemical calories to joules.

    Args:
        cal: Energy in calories.

    Returns:
        Energy in joules.

    Raises:
        TypeError: If cal is not numeric.

    Usage Example:
        >>> calories_to_joules(1000)
        4184.0

    Complexity: O(1)
    """
    if not isinstance(cal, (int, float)):
        raise TypeError("cal must be numeric.")
    return float(cal * 4.184)


def kwh_to_joules(kwh: float) -> float:
    """Convert kilowatt-hours to joules.

    Args:
        kwh: Energy in kWh.

    Returns:
        Energy in joules.

    Raises:
        TypeError: If kwh is not numeric.

    Usage Example:
        >>> kwh_to_joules(1)
        3600000.0

    Complexity: O(1)
    """
    if not isinstance(kwh, (int, float)):
        raise TypeError("kwh must be numeric.")
    return float(kwh * 3600000.0)


def joules_to_kwh(joules: float) -> float:
    """Convert joules to kilowatt-hours.

    Args:
        joules: Energy in joules.

    Returns:
        Energy in kWh.

    Raises:
        TypeError: If joules is not numeric.

    Usage Example:
        >>> round(joules_to_kwh(3600000), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(joules, (int, float)):
        raise TypeError("joules must be numeric.")
    return float(joules / 3600000.0)


def btu_to_joules(btu: float) -> float:
    """Convert British thermal units to joules.

    Args:
        btu: Energy in BTU.

    Returns:
        Energy in joules.

    Raises:
        TypeError: If btu is not numeric.

    Usage Example:
        >>> round(btu_to_joules(1), 2)
        1055.06

    Complexity: O(1)
    """
    if not isinstance(btu, (int, float)):
        raise TypeError("btu must be numeric.")
    return float(btu * 1055.05585)


def joules_to_btu(joules: float) -> float:
    """Convert joules to British thermal units.

    Args:
        joules: Energy in joules.

    Returns:
        Energy in BTU.

    Raises:
        TypeError: If joules is not numeric.

    Usage Example:
        >>> round(joules_to_btu(1055.06), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(joules, (int, float)):
        raise TypeError("joules must be numeric.")
    return float(joules / 1055.05585)


def watts_to_horsepower(watts: float) -> float:
    """Convert watts to mechanical horsepower.

    Args:
        watts: Power in watts.

    Returns:
        Power in horsepower.

    Raises:
        TypeError: If watts is not numeric.

    Usage Example:
        >>> round(watts_to_horsepower(745.7), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(watts, (int, float)):
        raise TypeError("watts must be numeric.")
    return float(watts / 745.69987158)


def horsepower_to_watts(hp: float) -> float:
    """Convert mechanical horsepower to watts.

    Args:
        hp: Power in horsepower.

    Returns:
        Power in watts.

    Raises:
        TypeError: If hp is not numeric.

    Usage Example:
        >>> round(horsepower_to_watts(1), 2)
        745.7

    Complexity: O(1)
    """
    if not isinstance(hp, (int, float)):
        raise TypeError("hp must be numeric.")
    return float(hp * 745.69987158)


def gradians_to_degrees(grad: float) -> float:
    """Convert gradians (gon) to degrees.

    Args:
        grad: Angle in gradians.

    Returns:
        Angle in degrees.

    Raises:
        TypeError: If grad is not numeric.

    Usage Example:
        >>> gradians_to_degrees(100)
        90.0

    Complexity: O(1)
    """
    if not isinstance(grad, (int, float)):
        raise TypeError("grad must be numeric.")
    return float(grad * 0.9)


def degrees_to_gradians(deg: float) -> float:
    """Convert degrees to gradians (gon).

    Args:
        deg: Angle in degrees.

    Returns:
        Angle in gradians.

    Raises:
        TypeError: If deg is not numeric.

    Usage Example:
        >>> round(degrees_to_gradians(90), 4)
        100.0

    Complexity: O(1)
    """
    if not isinstance(deg, (int, float)):
        raise TypeError("deg must be numeric.")
    return float(deg / 0.9)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 11: Speed, Torque, Frequency, Luminance Conversions
# ---------------------------------------------------------------------------

def knots_to_kmh(knots: float) -> float:
    """Convert knots to kilometres per hour.

    Args:
        knots: Speed in knots.

    Returns:
        Speed in km/h.

    Raises:
        TypeError: If knots is not numeric.

    Usage Example:
        >>> round(knots_to_kmh(1), 4)
        1.852

    Complexity: O(1)
    """
    if not isinstance(knots, (int, float)):
        raise TypeError("knots must be numeric.")
    return float(knots * 1.852)


def kmh_to_knots(kmh: float) -> float:
    """Convert kilometres per hour to knots.

    Args:
        kmh: Speed in km/h.

    Returns:
        Speed in knots.

    Raises:
        TypeError: If kmh is not numeric.

    Usage Example:
        >>> round(kmh_to_knots(1.852), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(kmh, (int, float)):
        raise TypeError("kmh must be numeric.")
    return float(kmh / 1.852)


def mach_to_ms(mach: float, speed_of_sound: float = 343.0) -> float:
    """Convert Mach number to metres per second.

    Args:
        mach: Mach number.
        speed_of_sound: Speed of sound in m/s (default 343 at sea level).

    Returns:
        Speed in m/s.

    Raises:
        TypeError: If mach or speed_of_sound is not numeric.

    Usage Example:
        >>> mach_to_ms(1)
        343.0

    Complexity: O(1)
    """
    if not isinstance(mach, (int, float)):
        raise TypeError("mach must be numeric.")
    if not isinstance(speed_of_sound, (int, float)):
        raise TypeError("speed_of_sound must be numeric.")
    return float(mach * speed_of_sound)


def ms_to_mach(ms: float, speed_of_sound: float = 343.0) -> float:
    """Convert metres per second to Mach number.

    Args:
        ms: Speed in m/s.
        speed_of_sound: Speed of sound in m/s (default 343 at sea level).

    Returns:
        Mach number.

    Raises:
        TypeError: If ms or speed_of_sound is not numeric.
        ValueError: If speed_of_sound is zero.

    Usage Example:
        >>> ms_to_mach(343)
        1.0

    Complexity: O(1)
    """
    if not isinstance(ms, (int, float)):
        raise TypeError("ms must be numeric.")
    if not isinstance(speed_of_sound, (int, float)):
        raise TypeError("speed_of_sound must be numeric.")
    if speed_of_sound == 0:
        raise ValueError("speed_of_sound cannot be zero.")
    return float(ms / speed_of_sound)


def newton_meters_to_foot_pounds(nm: float) -> float:
    """Convert newton-metres to foot-pounds (torque).

    Args:
        nm: Torque in N·m.

    Returns:
        Torque in ft·lbf.

    Raises:
        TypeError: If nm is not numeric.

    Usage Example:
        >>> round(newton_meters_to_foot_pounds(1), 4)
        0.7376

    Complexity: O(1)
    """
    if not isinstance(nm, (int, float)):
        raise TypeError("nm must be numeric.")
    return float(nm * 0.7375621493)


def foot_pounds_to_newton_meters(ftlb: float) -> float:
    """Convert foot-pounds to newton-metres (torque).

    Args:
        ftlb: Torque in ft·lbf.

    Returns:
        Torque in N·m.

    Raises:
        TypeError: If ftlb is not numeric.

    Usage Example:
        >>> round(foot_pounds_to_newton_meters(0.7376), 4)
        1.0001

    Complexity: O(1)
    """
    if not isinstance(ftlb, (int, float)):
        raise TypeError("ftlb must be numeric.")
    return float(ftlb / 0.7375621493)


def hertz_to_rpm(hz: float) -> float:
    """Convert hertz to revolutions per minute.

    Args:
        hz: Frequency in Hz.

    Returns:
        Frequency in RPM.

    Raises:
        TypeError: If hz is not numeric.

    Usage Example:
        >>> hertz_to_rpm(1)
        60.0

    Complexity: O(1)
    """
    if not isinstance(hz, (int, float)):
        raise TypeError("hz must be numeric.")
    return float(hz * 60.0)


def rpm_to_hertz(rpm: float) -> float:
    """Convert revolutions per minute to hertz.

    Args:
        rpm: Frequency in RPM.

    Returns:
        Frequency in Hz.

    Raises:
        TypeError: If rpm is not numeric.

    Usage Example:
        >>> round(rpm_to_hertz(60), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(rpm, (int, float)):
        raise TypeError("rpm must be numeric.")
    return float(rpm / 60.0)


def candela_to_lumens(cd: float, solid_angle_sr: float = 12.566370614359172) -> float:
    """Convert luminous intensity (candela) to luminous flux (lumens).

    Lumens = candela × solid angle (steradians).
    Default solid angle is 4π sr (full sphere).

    Args:
        cd: Luminous intensity in candela.
        solid_angle_sr: Solid angle in steradians (default 4π).

    Returns:
        Luminous flux in lumens.

    Raises:
        TypeError: If cd or solid_angle_sr is not numeric.

    Usage Example:
        >>> round(candela_to_lumens(1), 2)
        12.57

    Complexity: O(1)
    """
    if not isinstance(cd, (int, float)):
        raise TypeError("cd must be numeric.")
    if not isinstance(solid_angle_sr, (int, float)):
        raise TypeError("solid_angle_sr must be numeric.")
    return float(cd * solid_angle_sr)


def lumens_to_candela(lm: float, solid_angle_sr: float = 12.566370614359172) -> float:
    """Convert luminous flux (lumens) to luminous intensity (candela).

    Candela = lumens / solid angle (steradians).
    Default solid angle is 4π sr (full sphere).

    Args:
        lm: Luminous flux in lumens.
        solid_angle_sr: Solid angle in steradians (default 4π).

    Returns:
        Luminous intensity in candela.

    Raises:
        TypeError: If lm or solid_angle_sr is not numeric.
        ValueError: If solid_angle_sr is zero.

    Usage Example:
        >>> round(lumens_to_candela(12.57), 4)
        1.0003

    Complexity: O(1)
    """
    if not isinstance(lm, (int, float)):
        raise TypeError("lm must be numeric.")
    if not isinstance(solid_angle_sr, (int, float)):
        raise TypeError("solid_angle_sr must be numeric.")
    if solid_angle_sr == 0:
        raise ValueError("solid_angle_sr cannot be zero.")
    return float(lm / solid_angle_sr)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 12: Area, Volume, Force & Misc Conversions
# ---------------------------------------------------------------------------

def acres_to_hectares(acres: float) -> float:
    """Convert acres to hectares.

    Args:
        acres: Area in acres.

    Returns:
        Area in hectares.

    Raises:
        TypeError: If acres is not numeric.

    Usage Example:
        >>> round(acres_to_hectares(1), 4)
        0.4047

    Complexity: O(1)
    """
    if not isinstance(acres, (int, float)):
        raise TypeError("acres must be numeric.")
    return float(acres * 0.40468564224)


def hectares_to_acres(hectares: float) -> float:
    """Convert hectares to acres.

    Args:
        hectares: Area in hectares.

    Returns:
        Area in acres.

    Raises:
        TypeError: If hectares is not numeric.

    Usage Example:
        >>> round(hectares_to_acres(1), 4)
        2.4711

    Complexity: O(1)
    """
    if not isinstance(hectares, (int, float)):
        raise TypeError("hectares must be numeric.")
    return float(hectares / 0.40468564224)


def gallons_to_liters(gallons: float, us: bool = True) -> float:
    """Convert gallons to litres.

    Args:
        gallons: Volume in gallons.
        us: If True use US gallon (3.78541), else imperial (4.54609).

    Returns:
        Volume in litres.

    Raises:
        TypeError: If gallons is not numeric.

    Usage Example:
        >>> round(gallons_to_liters(1), 4)
        3.7854

    Complexity: O(1)
    """
    if not isinstance(gallons, (int, float)):
        raise TypeError("gallons must be numeric.")
    factor = 3.78541 if us else 4.54609
    return float(gallons * factor)


def liters_to_gallons(liters: float, us: bool = True) -> float:
    """Convert litres to gallons.

    Args:
        liters: Volume in litres.
        us: If True use US gallon (3.78541), else imperial (4.54609).

    Returns:
        Volume in gallons.

    Raises:
        TypeError: If liters is not numeric.

    Usage Example:
        >>> round(liters_to_gallons(3.78541), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(liters, (int, float)):
        raise TypeError("liters must be numeric.")
    factor = 3.78541 if us else 4.54609
    return float(liters / factor)


def newtons_to_pounds_force(newtons: float) -> float:
    """Convert newtons to pounds-force.

    Args:
        newtons: Force in newtons.

    Returns:
        Force in lbf.

    Raises:
        TypeError: If newtons is not numeric.

    Usage Example:
        >>> round(newtons_to_pounds_force(4.44822), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(newtons, (int, float)):
        raise TypeError("newtons must be numeric.")
    return float(newtons / 4.4482216152605)


def pounds_force_to_newtons(lbf: float) -> float:
    """Convert pounds-force to newtons.

    Args:
        lbf: Force in lbf.

    Returns:
        Force in newtons.

    Raises:
        TypeError: If lbf is not numeric.

    Usage Example:
        >>> round(pounds_force_to_newtons(1), 4)
        4.4482

    Complexity: O(1)
    """
    if not isinstance(lbf, (int, float)):
        raise TypeError("lbf must be numeric.")
    return float(lbf * 4.4482216152605)


def troy_ounces_to_grams(oz_t: float) -> float:
    """Convert troy ounces to grams.

    Args:
        oz_t: Mass in troy ounces.

    Returns:
        Mass in grams.

    Raises:
        TypeError: If oz_t is not numeric.

    Usage Example:
        >>> round(troy_ounces_to_grams(1), 4)
        31.1035

    Complexity: O(1)
    """
    if not isinstance(oz_t, (int, float)):
        raise TypeError("oz_t must be numeric.")
    return float(oz_t * 31.1034768)


def grams_to_troy_ounces(grams: float) -> float:
    """Convert grams to troy ounces.

    Args:
        grams: Mass in grams.

    Returns:
        Mass in troy ounces.

    Raises:
        TypeError: If grams is not numeric.

    Usage Example:
        >>> round(grams_to_troy_ounces(31.1035), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(grams, (int, float)):
        raise TypeError("grams must be numeric.")
    return float(grams / 31.1034768)


def light_years_to_kilometers(ly: float) -> float:
    """Convert light-years to kilometres.

    Args:
        ly: Distance in light-years.

    Returns:
        Distance in kilometres.

    Raises:
        TypeError: If ly is not numeric.

    Usage Example:
        >>> light_years_to_kilometers(1)
        9460730472580.8

    Complexity: O(1)
    """
    if not isinstance(ly, (int, float)):
        raise TypeError("ly must be numeric.")
    return float(ly * 9460730472580.8)


def kilometers_to_light_years(km: float) -> float:
    """Convert kilometres to light-years.

    Args:
        km: Distance in kilometres.

    Returns:
        Distance in light-years.

    Raises:
        TypeError: If km is not numeric.

    Usage Example:
        >>> round(kilometers_to_light_years(9460730472580.8), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(km, (int, float)):
        raise TypeError("km must be numeric.")
    return float(km / 9460730472580.8)
