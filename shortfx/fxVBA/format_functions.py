"""
Access Format Functions Module.

Description
    Funciones de formato de VBA/Access para fechas, números, moneda y porcentajes.
"""

from datetime import datetime
from typing import Any
from shortfx.fxString.string_format import (
    format_with_pattern as _core_format_with_pattern,
    format_as_currency as _core_format_as_currency,
    format_as_number as _core_format_as_number,
    format_as_percent as _core_format_as_percent,
)

__all__ = [
    "Format_",
    "FormatCurrency",
    "FormatDateTime",
    "FormatNumber",
    "FormatPercent",
]


def Format_(
    expression: Any,
    format_str: str = "",
    first_day_of_week: int = 0,
    first_week_of_year: int = 0
) -> str:
    """
    Description
        Muestra expresión con formato determinado.

    Args
        expression: Expresión a formatear.
        format_str: Cadena de formato.
        first_day_of_week: Primer día semana (0-7).
        first_week_of_year: Primera semana año (0-3).

    Returns
        str: Expresión formateada.

    Usage Example
        >>> format_(datetime(2024, 1, 15), "yyyy-mm-dd")
        '2024-01-15'
        >>> format_(1234.56, "0.00")
        '1234.56'

    Cost
        O(n) donde n es longitud del formato
    """
    if not format_str:
        return str(expression)

    return _core_format_with_pattern(expression, format_str)


def FormatCurrency(
    expression: float,
    num_decimals: int = 2,
    include_leading_digit: int = -2,
    use_parens_for_negative: int = -2,
    group_digits: int = -2
) -> str:
    """
    Description
        Retorna expresión formateada como valor de moneda.

    Args
        expression: Número a formatear.
        num_decimals: Número de decimales.
        include_leading_digit: Incluir dígito inicial (-1=True, 0=False, -2=config).
        use_parens_for_negative: Paréntesis en negativos.
        group_digits: Usar separadores de miles.

    Returns
        str: Valor formateado como moneda.

    Usage Example
        >>> formatcurrency(1234.56)
        '$1,234.56'
        >>> formatcurrency(-42.5)
        '($42.50)'

    Cost
        O(1)
    """
    use_parens = use_parens_for_negative != 0
    result = _core_format_as_currency(float(expression), num_decimals)

    if float(expression) < 0 and use_parens:
        return f"(${result.lstrip('-$')})"

    return result


def FormatDateTime(expression: datetime, named_format: int = 0) -> str:
    """
    Description
        Retorna cadena basada en expresión, formateada como fecha.

    Args
        expression: Fecha a formatear.
        named_format: Formato (0=general, 1=long date, 2=short date, 3=long time, 4=short time).

    Returns
        str: Fecha formateada.

    Usage Example
        >>> formatdatetime(datetime(2024, 1, 15, 14, 30), 0)
        '2024-01-15 14:30:00'
        >>> formatdatetime(datetime(2024, 1, 15), 2)
        '01/15/2024'

    Cost
        O(1)
    """
    if named_format == 0:
        return str(expression)
    elif named_format == 1:
        return expression.strftime("%A, %B %d, %Y")
    elif named_format == 2:
        return expression.strftime("%m/%d/%Y")
    elif named_format == 3:
        return expression.strftime("%I:%M:%S %p")
    elif named_format == 4:
        return expression.strftime("%H:%M")
    else:
        return str(expression)


def FormatNumber(
    expression: float,
    num_decimals: int = 2,
    include_leading_digit: int = -2,
    use_parens_for_negative: int = -2,
    group_digits: int = -2
) -> str:
    """
    Description
        Retorna expresión formateada como número.

    Args
        expression: Número a formatear.
        num_decimals: Número de decimales.
        include_leading_digit: Incluir dígito inicial.
        use_parens_for_negative: Paréntesis en negativos.
        group_digits: Usar separadores de miles.

    Returns
        str: Número formateado.

    Usage Example
        >>> formatnumber(1234.5678, 2)
        '1,234.57'
        >>> formatnumber(-42.5)
        '(42.50)'

    Cost
        O(1)
    """
    return _core_format_as_number(
        float(expression), num_decimals, use_parens_for_negative != 0
    )


def FormatPercent(
    expression: float,
    num_decimals: int = 2,
    include_leading_digit: int = -2,
    use_parens_for_negative: int = -2,
    group_digits: int = -2
) -> str:
    """
    Description
        Retorna expresión formateada como porcentaje (multiplicado por 100).

    Args
        expression: Número a formatear (0.25 = 25%).
        num_decimals: Número de decimales.
        include_leading_digit: Incluir dígito inicial.
        use_parens_for_negative: Paréntesis en negativos.
        group_digits: Usar separadores de miles.

    Returns
        str: Porcentaje formateado.

    Usage Example
        >>> formatpercent(0.25)
        '25.00%'
        >>> formatpercent(-0.1234, 1)
        '(12.3%)'

    Cost
        O(1)
    """
    return _core_format_as_percent(
        float(expression), num_decimals, use_parens_for_negative != 0
    )
