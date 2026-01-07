"""
Access Mathematical Functions Module.

Description
    Funciones matemáticas compatibles con VBA/Access.
"""

import math
import random

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
    return abs(number)


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
    return math.atan(number)


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
    return math.cos(number)


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
    return math.exp(number)


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
    return int(number)


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
    return math.floor(number)


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
    return math.log(number)


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
    return random.random()


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
    return round(number, num_digits_after_decimal)


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
    if number > 0:
        return 1
    elif number == 0:
        return 0
    else:
        return -1


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
    return math.sin(number)


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
    return math.sqrt(number)


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
    return math.tan(number)
