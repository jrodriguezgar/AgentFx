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
    >>> from formulite.fxNumeric.numeric_convertions import hex_to_int, float_to_int_truncated
    >>> hex_to_int("0xFF")
    255
    >>> float_to_int_truncated(3.9)
    3
"""
import json
from decimal import Decimal, getcontext
import locale
from typing import Any, Union, Optional

# JavaScript's safe integer limit
JS_MAX_SAFE_INTEGER = 2**53 - 1
JS_MIN_SAFE_INTEGER = -(2**53 - 1)

from datetime import datetime, timezone

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


def int_a_bytes(numero_entero: int, num_bytes: int, byteorder: str = 'big') -> bytes:
    """
    Converts an integer to a byte sequence.

    Useful for binary data transmission, communication protocols,
    or storing data in binary formats.

    Args:
        numero_entero (int): The integer to convert.
        num_bytes (int): The desired number of bytes for the representation.
                         Must be sufficient to contain the integer.
        byteorder (str): The byte order ('big' for network byte order,
                         'little' for reverse order). Default is 'big'.

    Returns:
        bytes: The byte representation of the integer.

    Raises:
        OverflowError: If the integer is too large for the specified number of bytes.

    Example:
        >>> int_a_bytes(123, 2, byteorder='big')
        b'\x00{'
        >>> int_a_bytes(256, 2, byteorder='little')
        b'\x00\x01'
        >>> int_a_bytes(65535, 2, byteorder='big') # Max value for 2 bytes unsigned
        b'\xff\xff'

    **Cost:** O(1), conversion to bytes.
    """
    return numero_entero.to_bytes(num_bytes, byteorder=byteorder)


def bytes_a_int(secuencia_bytes: bytes, byteorder: str = 'big') -> int:
    """
    Converts a byte sequence to an integer.

    Useful for decoding data received through a binary protocol
    or reading numeric values from binary files.

    Args:
        secuencia_bytes (bytes): The byte sequence to convert.
        byteorder (str): The byte order ('big' for network byte order,
                         'little' for reverse order). Default is 'big'.

    Returns:
        int: The integer represented by the byte sequence.

    Example:
        >>> bytes_a_int(b'\x00{', 'big')
        123
        >>> bytes_a_int(b'\x00\x01', 'little')
        256
        >>> bytes_a_int(b'\xff\xff', 'big')
        65535

    **Cost:** O(1), conversion from bytes.
    """
    return int.from_bytes(secuencia_bytes, byteorder=byteorder)


def float_a_json_safe(numero_float: float) -> str:
    """
    Converts a floating-point number to a JSON-safe representation.

    JSON standards do not directly support values like NaN (Not a Number)
    or Infinity. This function converts them to their corresponding string
    representation ('NaN', 'Infinity', '-Infinity') before JSON serialization,
    while regular numbers are handled as standard JSON floats.

    Args:
        numero_float (float): The input floating-point number.

    Returns:
        str: The representation of the number as a valid JSON string.

    Example:
        >>> float_a_json_safe(3.14)
        '3.14'
        >>> float_a_json_safe(float('nan'))
        '"NaN"'
        >>> float_a_json_safe(float('inf'))
        '"Infinity"'
        >>> float_a_json_safe(float('-inf'))
        '"-Infinity"'

    **Cost:** O(1), verification and JSON serialization.
    """
    if math.isnan(numero_float):
        # Convert NaN to the string "NaN"
        return json.dumps(str(numero_float))
    elif math.isinf(numero_float):
        # Convert Infinity to the string "Infinity" or "-Infinity"
        return json.dumps(str(numero_float))
    else:
        # For normal numbers, let json.dumps handle them directly
        # or convert to Decimal first for greater precision if desired
        return json.dumps(numero_float)


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
    

import math
from typing import Union

def power(base: Union[int, float], exponent: Union[int, float]) -> float:
    """
    Calculates the value of a base raised to a specified exponent (base^exponent).

    This function handles both positive and negative bases and exponents,
    returning a float. It uses the standard exponentiation operator `**`.

    Args:
        base (Union[int, float]): The base number.
        exponent (Union[int, float]): The exponent to which the base is raised.

    Returns:
        float: The result of base raised to the power of exponent.

    Raises:
        TypeError: If base or exponent are not numeric.
        ValueError: If a negative base is raised to a non-integer exponent
                    (which results in a complex number, not handled here),
                    or if 0 is raised to a negative or zero exponent.

    Example:
        >>> power(2, 3)
        8.0
        >>> power(9, 0.5) # Square root
        3.0
        >>> power(-2, 3)
        -8.0
        >>> power(10, -2)
        0.01

    **Cost:** O(1), operación de exponenciación.
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
    """
    Calculates the square root of a non-negative number.

    The square root function finds a number that, when multiplied by itself,
    equals the input number.

    Args:
        x (Union[int, float]): The number for which to calculate the square root. Must be non-negative.

    Returns:
        float: The square root of x.

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is negative.

    Example:
        >>> square_root(9)
        3.0
        >>> square_root(25.0)
        5.0
        >>> square_root(0)
        0.0

    **Cost:** O(1), cálculo de raíz cuadrada mediante función math.sqrt.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input 'x' must be a numeric value (int or float).")
    if x < 0:
        raise ValueError("Cannot calculate the square root of a negative number (results in a complex number).")

    return math.sqrt(x)

def cube_root(x: Union[int, float]) -> float:
    """
    Calculates the cube root of a number.

    The cube root function finds a number that, when multiplied by itself
    three times, equals the input number. It works for both positive and negative
    real numbers.

    Args:
        x (Union[int, float]): The number for which to calculate the cube root.

    Returns:
        float: The cube root of x.

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> cube_root(8)
        2.0
        >>> cube_root(27)
        3.0
        >>> cube_root(-8)
        -2.0
        >>> cube_root(0)
        0.0

    **Cost:** O(1), cálculo de raíz cúbica.
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
    """
    Calculates the nth root of a number (x^(1/n)).

    This function generalizes the square and cube roots to any positive integer n.
    For negative x, n must be an odd integer to return a real result.

    Args:
        x (Union[int, float]): The number for which to calculate the root.
        n (Union[int, float]): The degree of the root (e.g., 2 for square root, 3 for cube root).
                                Must be a non-zero number. If x < 0, n must be an odd integer.

    Returns:
        float: The nth root of x.

    Raises:
        TypeError: If x or n are not numeric.
        ValueError: If n is 0, or if x is negative and n is an even number,
                    or if x is 0 and n is negative.

    Example:
        >>> nth_root(81, 4) # Fourth root of 81
        3.0
        >>> nth_root(1000, 3) # Cube root of 1000
        10.0
        >>> nth_root(-27, 3) # Cube root of -27
        -3.0
        >>> # nth_root(-16, 2) would raise ValueError (even root of negative number)

    **Cost:** O(1), cálculo de raíz n-ésima mediante exponenciación.
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


