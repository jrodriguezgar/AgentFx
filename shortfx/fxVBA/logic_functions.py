"""
Access Logic and Selection Functions Module.

Description
    Funciones de lógica, evaluación condicional y selección de VBA/Access.
"""

from typing import Any, Optional
from datetime import datetime

from shortfx.fxPython.py_operations import choose as _core_choose
from shortfx.fxPython.py_logic import if_then_else as _core_iif
from shortfx.fxString.string_evaluations import is_numeric as _core_is_numeric

__all__ = [
    "Choose",
    "IIf",
    "IsArray",
    "IsDate",
    "IsEmpty",
    "IsError",
    "IsMissing",
    "IsNull",
    "IsNumeric",
    "IsObject",
    "Switch",
]


def Choose(index_num: int, *values: Any) -> Optional[Any]:
    """
    Description
        Elige valor de lista según índice.

    Args
        index_num: Índice (1-based) del valor a elegir.
        *values: Lista de valores.

    Returns
        Any: Valor en la posición index_num o None si fuera de rango.

    Usage Example
        >>> choose(2, "rojo", "azul", "verde")
        'azul'
        >>> choose(1, 10, 20, 30)
        10

    Cost
        O(1)
    """
    try:
        return _core_choose(index_num, *values)
    except (ValueError, IndexError):
        return None


def IIf(expression: bool, true_part: Any, false_part: Any) -> Any:
    """
    Description
        Evalúa Expression, retorna TruePart si verdadero, FalsePart si falso.

    Args
        expression: Expresión booleana a evaluar.
        true_part: Valor a retornar si True.
        false_part: Valor a retornar si False.

    Returns
        Any: true_part o false_part según evaluación.

    Usage Example
        >>> iif(5 > 3, "mayor", "menor")
        'mayor'
        >>> iif(True, 100, 200)
        100

    Cost
        O(1)
    """
    return _core_iif(expression, true_part, false_part)


def IsDate(expression: Any) -> bool:
    """
    Description
        Evalúa si Expression es una fecha.

    Args
        expression: Expresión a evaluar.

    Returns
        bool: True si es fecha, False si no.

    Usage Example
        >>> isdate(datetime(2024, 1, 1))
        True
        >>> isdate("2024-01-01")
        False
        >>> isdate(42)
        False

    Cost
        O(1)
    """
    return isinstance(expression, datetime)


def IsError(number: Any) -> bool:
    """
    Description
        Comprueba si cifra es número de Error de Access.
        En Python, simplemente verifica si es excepción.

    Args
        number: Valor a evaluar.

    Returns
        bool: True si es error/excepción.

    Usage Example
        >>> iserror(Exception("test"))
        True
        >>> iserror(42)
        False

    Cost
        O(1)
    """
    return isinstance(number, Exception)


def IsNull(expression: Any) -> bool:
    """
    Description
        Retorna True si Expression tiene valor nulo.

    Args
        expression: Expresión a evaluar.

    Returns
        bool: True si es None, False si no.

    Usage Example
        >>> isnull(None)
        True
        >>> isnull("")
        False
        >>> isnull(0)
        False

    Cost
        O(1)
    """
    return expression is None


def IsNumeric(expression: Any) -> bool:
    """
    Description
        Retorna verdadero si resultado de evaluar expresión es valor numérico.

    Args
        expression: Expresión a evaluar.

    Returns
        bool: True si es numérico, False si no.

    Usage Example
        >>> isnumeric(42)
        True
        >>> isnumeric("123")
        True
        >>> isnumeric("abc")
        False

    Cost
        O(1)
    """
    if isinstance(expression, (int, float, complex)):
        return True

    if isinstance(expression, str):
        return _core_is_numeric(expression)

    return False


def Switch(*args: Any) -> Optional[Any]:
    """
    Description
        Evalúa parejas Expresión/Valor, retorna valor de primera expresión verdadera.

    Args
        *args: Parejas (expresión, valor) alternadas.

    Returns
        Any: Valor asociado a primera expresión verdadera o None.

    Usage Example
        >>> switch(False, "A", True, "B", False, "C")
        'B'
        >>> switch(1 == 2, "iguales", 1 < 2, "menor", True, "otro")
        'menor'

    Cost
        O(n) donde n es número de parejas
    """
    if len(args) % 2 != 0:
        raise ValueError("Switch requiere número par de argumentos (parejas expresión/valor)")
    
    for i in range(0, len(args), 2):
        if args[i]:
            return args[i + 1]
    
    return None


def IsArray(variable: Any) -> bool:
    """
    Description
        Verifica si variable es array (lista, tupla).

    Args
        variable: Variable a verificar.

    Returns
        bool: True si es array/lista, False caso contrario.

    Usage Example
        >>> isarray([1, 2, 3])
        True
        >>> isarray((1, 2, 3))
        True
        >>> isarray("texto")
        False

    Cost
        O(1)
    """
    return isinstance(variable, (list, tuple))


def IsEmpty(variable: Any) -> bool:
    """
    Description
        Verifica si variable está vacía o no inicializada.

    Args
        variable: Variable a verificar.

    Returns
        bool: True si está vacía, False caso contrario.

    Usage Example
        >>> isempty(None)
        True
        >>> isempty("")
        True
        >>> isempty([])
        True
        >>> isempty("texto")
        False

    Cost
        O(1)
    """
    if variable is None:
        return True
    
    if isinstance(variable, (str, list, dict, tuple, set)):
        return len(variable) == 0
    
    # Para números, False y otros valores escalares
    return False


def IsObject(variable: Any) -> bool:
    """
    Description
        Verifica si variable es objeto (tiene atributos/métodos).

    Args
        variable: Variable a verificar.

    Returns
        bool: True si es objeto, False caso contrario.

    Usage Example
        >>> class MiClase: pass
        >>> obj = MiClase()
        >>> isobject(obj)
        True
        >>> isobject(42)
        False

    Cost
        O(1)
    """
    # En Python casi todo es objeto, pero seguimos convención VBA
    # donde objeto significa instancia de clase personalizada
    if variable is None:
        return False
    
    # Tipos primitivos no son "objetos" en sentido VBA
    if isinstance(variable, (bool, int, float, str, list, tuple, dict, set)):
        return False
    
    # Verificar si tiene __dict__ (es instancia de clase)
    return hasattr(variable, '__dict__')


def IsMissing(argument: Any) -> bool:
    """
    Description
        Verifica si argumento opcional está ausente/no proporcionado.

    Args
        argument: Argumento a verificar.

    Returns
        bool: True si es None (faltante), False caso contrario.

    Usage Example
        >>> def funcion(opcional=None):
        ...     return IsMissing(opcional)
        >>> funcion()
        True
        >>> funcion(42)
        False

    Cost
        O(1)
    """
    return argument is None
