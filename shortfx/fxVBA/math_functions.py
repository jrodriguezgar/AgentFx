"""
Access Mathematical Functions Module.

Description
    Funciones matemáticas compatibles con VBA/Access.
"""

from shortfx.fxNumeric.arithmetic_functions import (
    absolute_value as _core_abs,
    exp as _core_exp,
    natural_log as _core_log,
    sign as _core_sign,
    square_root as _core_sqrt,
)
from shortfx.fxNumeric.random_functions import (
    random_float as _core_random_float,
)
from shortfx.fxNumeric.trigonometry_functions import (
    arctangent as _core_atan,
    cosine as _core_cos,
    sine as _core_sin,
    tangent as _core_tan,
)
from shortfx.fxNumeric.rounding_functions import (
    round_down as _core_floor,
    round_to_n_decimals as _core_round,
    truncate_float as _core_trunc,
)

__all__ = [
    "Abs_",
    "Atn",
    "Cos",
    "Exp",
    "Fix",
    "Int_",
    "Log",
    "Rnd",
    "Round_",
    "Sgn",
    "Sin",
    "Sqr",
    "Tan",
]


def Abs_(number: float) -> float:
    """
    Description
        Retorna valor absoluto de un número (omite el signo).

    Args
        number: Número.

    Returns
        float: Valor absoluto.

    Usage Example
        >>> abs_(-42)
        42
        >>> abs_(3.14)
        3.14

    Cost
        O(1)
    """
    return _core_abs(number)


def Atn(number: float) -> float:
    """
    Description
        Retorna arco tangente de un número (expresada en radianes).

    Args
        number: Número.

    Returns
        float: Arco tangente en radianes.

    Usage Example
        >>> atn(1)
        0.7853981633974483

    Cost
        O(1)
    """
    return _core_atan(number)


def Cos(number: float) -> float:
    """
    Description
        Retorna coseno de un ángulo.

    Args
        number: Ángulo en radianes.

    Returns
        float: Coseno del ángulo.

    Usage Example
        >>> cos(0)
        1.0

    Cost
        O(1)
    """
    return _core_cos(number)


def Exp(number: float) -> float:
    """
    Description
        Retorna base de logaritmos naturales (e) elevada a potencia.

    Args
        number: Exponente.

    Returns
        float: e elevado a number.

    Usage Example
        >>> exp(1)
        2.718281828459045

    Cost
        O(1)
    """
    return _core_exp(number)


def Fix(number: float) -> int:
    """
    Description
        Retorna parte entera de número, truncando decimales (no redondea).

    Args
        number: Número.

    Returns
        int: Parte entera.

    Usage Example
        >>> fix(3.7)
        3
        >>> fix(-3.7)
        -3

    Cost
        O(1)
    """
    return _core_trunc(number)


def Int_(number: float) -> int:
    """
    Description
        Retorna parte entera de número, truncando decimales (no redondea).

    Args
        number: Número.

    Returns
        int: Parte entera.

    Usage Example
        >>> int_(3.7)
        3
        >>> int_(-3.7)
        -4

    Cost
        O(1)
    """
    return _core_floor(number)


def Log(number: float) -> float:
    """
    Description
        Retorna logaritmo natural de un número.

    Args
        number: Número (debe ser positivo).

    Returns
        float: Logaritmo natural.

    Raises
        ValueError: Si number <= 0.

    Usage Example
        >>> log(2.718281828459045)
        1.0

    Cost
        O(1)
    """
    return _core_log(number)


def Rnd(number: int = None) -> float:
    """
    Description
        Retorna número aleatorio entre 0 y 1.

    Args
        number: Parámetro opcional (ignorado en Python).

    Returns
        float: Número aleatorio [0, 1).

    Usage Example
        >>> rnd()
        0.234567

    Cost
        O(1)
    """
    return _core_random_float(0.0, 1.0)


def Round_(number: float, num_digits_after_decimal: int = 0) -> float:
    """
    Description
        Retorna cifra redondeada al número de decimales definido.

    Args
        number: Número a redondear.
        num_digits_after_decimal: Número de decimales.

    Returns
        float: Número redondeado.

    Usage Example
        >>> round_(3.14159, 2)
        3.14
        >>> round_(42.7)
        43.0

    Cost
        O(1)
    """
    return _core_round(number, num_digits_after_decimal)


def Sgn(number: float) -> int:
    """
    Description
        Retorna entero indicando signo de Number.

    Args
        number: Número a evaluar.

    Returns
        int: 1 si positivo, 0 si cero, -1 si negativo.

    Usage Example
        >>> sgn(42)
        1
        >>> sgn(0)
        0
        >>> sgn(-3.14)
        -1

    Cost
        O(1)
    """
    return _core_sign(number)


def Sin(number: float) -> float:
    """
    Description
        Retorna seno de un ángulo.

    Args
        number: Ángulo en radianes.

    Returns
        float: Seno del ángulo.

    Usage Example
        >>> sin(0)
        0.0

    Cost
        O(1)
    """
    return _core_sin(number)


def Sqr(number: float) -> float:
    """
    Description
        Retorna raíz cuadrada de un número.

    Args
        number: Número (debe ser no negativo).

    Returns
        float: Raíz cuadrada.

    Raises
        ValueError: Si number < 0.

    Usage Example
        >>> sqr(16)
        4.0
        >>> sqr(2)
        1.4142135623730951

    Cost
        O(1)
    """
    return _core_sqrt(number)


def Tan(number: float) -> float:
    """
    Description
        Retorna tangente de un ángulo.

    Args
        number: Ángulo en radianes.

    Returns
        float: Tangente del ángulo.

    Usage Example
        >>> tan(0)
        0.0

    Cost
        O(1)
    """
    return _core_tan(number)
