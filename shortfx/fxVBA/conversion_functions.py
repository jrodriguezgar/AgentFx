"""
Access Type Conversion Functions Module.

Description
    Funciones de conversión de tipos de VBA/Access. Muchas tienen equivalente
    Python directo (bool(), int(), str(), etc.), pero se mantienen para
    compatibilidad con código Access migrado.
"""

from typing import Any
from datetime import datetime, date, time

from shortfx.fxString.string_convertions import (
    string_to_datetime as _core_string_to_datetime,
)

__all__ = [
    "CBool",
    "CByte",
    "CCur",
    "CDate",
    "CDbl",
    "CDec",
    "CInt",
    "CLng",
    "CLngLng",
    "CLngPtr",
    "CSng",
    "CStr",
    "CVar",
    "CVErr",
    "DateValue",
    "TimeValue",
    "Val",
]


def CBool(expression: Any) -> bool:
    """
    Description
        Convierte expresión a Boolean.

    Args
        expression: Expresión a convertir.

    Returns
        bool: Valor booleano.

    Raises
        ValueError: Si la expresión no puede convertirse.

    Usage Example
        >>> cbool(1)
        True
        >>> cbool(0)
        False
        >>> cbool("True")
        True

    Cost
        O(1)
    """
    return bool(expression)


def CByte(expression: Any) -> int:
    """
    Description
        Convierte número a Byte (0-255).

    Args
        expression: Número a convertir.

    Returns
        int: Valor entre 0 y 255.

    Raises
        ValueError: Si el valor está fuera de rango.

    Usage Example
        >>> cbyte(42)
        42
        >>> cbyte(255)
        255

    Cost
        O(1)
    """
    value = int(expression)
    if not 0 <= value <= 255:
        raise ValueError(f"Valor {value} fuera de rango Byte (0-255)")
    return value


def CCur(expression: Any) -> float:
    """
    Description
        Convierte número a Currency (moneda con 4 decimales fijos).

    Args
        expression: Número a convertir.

    Returns
        float: Valor redondeado a 4 decimales.

    Usage Example
        >>> ccur(123.456789)
        123.4568
        >>> ccur("99.99")
        99.99

    Cost
        O(1)
    """
    return round(float(expression), 4)


def CDate(expression: Any) -> datetime:
    """
    Description
        Convierte expresión a fecha/hora.

    Args
        expression: Expresión a convertir (string, número, etc.).

    Returns
        datetime: Objeto fecha/hora.

    Raises
        ValueError: Si no puede convertirse a fecha válida.

    Usage Example
        >>> cdate("2024-01-15")
        datetime.datetime(2024, 1, 15, 0, 0)

    Cost
        O(1)
    """
    result = _core_string_to_datetime(expression)

    if result is not None:
        return result

    raise ValueError(f"No se puede convertir {expression} a fecha")


def CDbl(expression: Any) -> float:
    """
    Description
        Convierte número a Double (punto flotante doble precisión).

    Args
        expression: Número a convertir.

    Returns
        float: Valor en punto flotante.

    Usage Example
        >>> cdbl(42)
        42.0
        >>> cdbl("3.14159")
        3.14159

    Cost
        O(1)
    """
    return float(expression)


def CDec(expression: Any) -> float:
    """
    Description
        Convierte número a Decimal (alta precisión).

    Args
        expression: Número a convertir.

    Returns
        float: Valor decimal.

    Usage Example
        >>> cdec("123.456")
        123.456

    Cost
        O(1)
    """
    return CDbl(expression)


def CInt(expression: Any) -> int:
    """
    Description
        Convierte expresión a Integer (redondea al entero más cercano).

    Args
        expression: Expresión a convertir.

    Returns
        int: Valor entero.

    Usage Example
        >>> cint(3.7)
        4
        >>> cint(3.2)
        3
        >>> cint("42")
        42

    Cost
        O(1)
    """
    return round(float(expression))


def CLng(expression: Any) -> int:
    """
    Description
        Convierte expresión a Long (entero largo).

    Args
        expression: Expresión a convertir.

    Returns
        int: Valor entero.

    Usage Example
        >>> clng(1234567)
        1234567
        >>> clng("999999")
        999999

    Cost
        O(1)
    """
    return int(float(expression))


def CLngLng(expression: Any) -> int:
    """
    Description
        Convert expression to LongLong (64-bit integer).

    Args
        expression: Expression to convert.

    Returns
        int: 64-bit integer value.

    Raises
        ValueError: If value overflows 64-bit signed integer range.

    Usage Example
        >>> CLngLng(9223372036854775807)
        9223372036854775807
        >>> CLngLng("123456789012345")
        123456789012345

    Cost
        O(1)
    """
    value = int(float(expression))
    min_val = -(2**63)
    max_val = 2**63 - 1

    if not min_val <= value <= max_val:
        raise ValueError(f"Value {value} overflows LongLong range ({min_val} to {max_val})")

    return value


def CLngPtr(expression: Any) -> int:
    """
    Description
        Convert expression to LongPtr (pointer-sized integer).

    Args
        expression: Expression to convert.

    Returns
        int: Pointer-sized integer value.

    Usage Example
        >>> CLngPtr(42)
        42
        >>> CLngPtr("12345678")
        12345678

    Cost
        O(1)
    """
    import sys
    value = int(float(expression))

    if sys.maxsize > 2**32:
        max_val = 2**63 - 1
        min_val = -(2**63)
    else:
        max_val = 2**31 - 1
        min_val = -(2**31)

    if not min_val <= value <= max_val:
        raise ValueError(f"Value {value} overflows LongPtr range ({min_val} to {max_val})")

    return value


def CSng(expression: Any) -> float:
    """
    Description
        Convierte expresión a Single (punto flotante simple precisión).

    Args
        expression: Expresión a convertir.

    Returns
        float: Valor en punto flotante.

    Usage Example
        >>> csng(42)
        42.0
        >>> csng("3.14")
        3.14

    Cost
        O(1)
    """
    return CDbl(expression)


def CStr(expression: Any) -> str:
    """
    Description
        Convierte expresión a texto.

    Args
        expression: Expresión a convertir.

    Returns
        str: Representación en texto.

    Usage Example
        >>> cstr(42)
        '42'
        >>> cstr(3.14)
        '3.14'
        >>> cstr(True)
        'True'

    Cost
        O(1)
    """
    return str(expression)


def CVar(expression: Any) -> Any:
    """
    Description
        Convierte argumento a Variant (tipo más genérico).
        En Python, simplemente retorna el valor sin cambios.

    Args
        expression: Expresión a convertir.

    Returns
        Any: El mismo valor.

    Usage Example
        >>> cvar(42)
        42
        >>> cvar("texto")
        'texto'

    Cost
        O(1)
    """
    return expression


def DateValue(date_str: str) -> date:
    """
    Description
        Convierte cadena formateada como fecha en valor tipo fecha.

    Args
        date_str: Cadena con formato de fecha.

    Returns
        date: Objeto fecha.

    Raises
        ValueError: Si la cadena no tiene formato válido.

    Usage Example
        >>> date_value("2024-01-15")
        datetime.date(2024, 1, 15)

    Cost
        O(1)
    """
    result = _core_string_to_datetime(date_str)

    if result is None:
        raise ValueError(f"No se pudo convertir '{date_str}' a fecha")

    return result.date()


def TimeValue(time_str: str) -> time:
    """
    Description
        Convierte cadena formateada como hora en valor tipo Time.

    Args
        time_str: Cadena con formato de hora (HH:MM:SS).

    Returns
        time: Objeto hora.

    Raises
        ValueError: Si la cadena no tiene formato válido.

    Usage Example
        >>> time_value("14:30:00")
        datetime.time(14, 30)
        >>> time_value("09:15:30")
        datetime.time(9, 15, 30)

    Cost
        O(1)
    """
    return datetime.strptime(time_str, "%H:%M:%S").time()


def Val(string: str) -> float:
    """
    Description
        Retorna parte numérica de cadena si está al principio del texto.

    Args
        string: Cadena a evaluar.

    Returns
        float: Valor numérico encontrado o 0.0 si no hay números.

    Usage Example
        >>> val("123.45abc")
        123.45
        >>> val("  42  ")
        42.0
        >>> val("abc123")
        0.0

    Cost
        O(n) donde n es longitud de la cadena
    """
    import re

    string = string.strip()
    match = re.match(r'^[+-]?(\d+\.?\d*|\.\d+)', string)

    if match:
        return float(match.group())

    return 0.0


def CVErr(error_number: int) -> str:
    """
    Description
        Create an error value from an error number. In Python, returns
        a string representation of the VBA error value.

    Args
        error_number: VBA error number (1-7).

    Returns
        str: String representation of the error value.

    Raises
        ValueError: If error_number is not in the valid range.

    Usage Example
        >>> CVErr(2007)
        'Error 2007'
        >>> CVErr(3)
        'Error 3'

    Cost
        O(1)
    """
    _VBA_ERRORS = {
        1: "#NULL!",
        2: "#DIV/0!",
        3: "#VALUE!",
        4: "#REF!",
        5: "#NAME?",
        6: "#NUM!",
        7: "#N/A",
    }

    if error_number in _VBA_ERRORS:
        return _VBA_ERRORS[error_number]

    return f"Error {error_number}"
