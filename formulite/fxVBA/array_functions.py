"""
VBA Array Manipulation Functions Module.

Description
    Funciones para manipulación de arrays compatibles con VBA.
    Incluye Split, Join, Filter, LBound, UBound y Array.
"""

from typing import Any, List

__all__ = [
    "Array_",
    "Filter_",
    "Join_",
    "LBound",
    "Split",
    "UBound",
]


def Split(
    expression: str,
    delimiter: str = " ",
    limit: int = -1,
    compare: int = 0
) -> List[str]:
    """
    Description
        Divide cadena en array de subcadenas usando delimitador.

    Args
        expression: Cadena a dividir.
        delimiter: Delimitador (por defecto espacio).
        limit: Máximo número de subcadenas (-1 = todas).
        compare: Tipo de comparación (0=binaria, 1=texto).

    Returns
        List[str]: Array de subcadenas.

    Usage Example
        >>> split("uno,dos,tres", ",")
        ['uno', 'dos', 'tres']
        >>> split("a b c d", " ", 2)
        ['a', 'b c d']

    Cost
        O(n) donde n es longitud de expression
    """
    if not expression:
        return []
    
    if limit == -1:
        return expression.split(delimiter)
    else:
        # Python split con maxsplit genera limit+1 elementos
        return expression.split(delimiter, limit - 1)


def Join_(
    source_array: List[Any],
    delimiter: str = " "
) -> str:
    """
    Description
        Une elementos de array en string usando delimitador.

    Args
        source_array: Array de elementos a unir.
        delimiter: Delimitador entre elementos (por defecto espacio).

    Returns
        str: String resultante de unir elementos.

    Usage Example
        >>> join_(["uno", "dos", "tres"], ",")
        'uno,dos,tres'
        >>> join_([1, 2, 3], "-")
        '1-2-3'

    Cost
        O(n) donde n es número de elementos
    """
    if not source_array:
        return ""
    
    return delimiter.join(str(item) for item in source_array)


def Filter_(
    source_array: List[Any],
    match: str,
    include: bool = True,
    compare: int = 0
) -> List[Any]:
    """
    Description
        Filtra elementos de array que contienen (o no) cadena específica.

    Args
        source_array: Array fuente.
        match: Cadena a buscar.
        include: True para incluir coincidencias, False para excluir.
        compare: Tipo de comparación (0=binaria, 1=texto/case-insensitive).

    Returns
        List[Any]: Array filtrado.

    Usage Example
        >>> filter_(["apple", "banana", "apricot"], "ap")
        ['apple', 'apricot']
        >>> filter_(["apple", "banana", "apricot"], "ap", False)
        ['banana']

    Cost
        O(n*m) donde n es tamaño array, m longitud de match
    """
    if not source_array:
        return []
    
    result = []
    case_sensitive = (compare == 0)
    
    for item in source_array:
        item_str = str(item)
        match_str = match
        
        if not case_sensitive:
            item_str = item_str.lower()
            match_str = match_str.lower()
        
        contains_match = match_str in item_str
        
        if (include and contains_match) or (not include and not contains_match):
            result.append(item)
    
    return result


def LBound(array_var: List[Any], dimension: int = 1) -> int:
    """
    Description
        Retorna índice inferior (mínimo) de array en dimensión especificada.

    Args
        array_var: Array.
        dimension: Dimensión (1-based, por defecto 1).

    Returns
        int: Índice inferior (siempre 0 en Python).

    Usage Example
        >>> lbound([1, 2, 3, 4, 5])
        0
        >>> lbound(["a", "b", "c"])
        0

    Cost
        O(1)
    """
    if not array_var:
        raise ValueError("Array vacío")
    
    # En VBA los arrays pueden empezar en diferentes índices
    # En Python siempre empiezan en 0
    return 0


def UBound(array_var: List[Any], dimension: int = 1) -> int:
    """
    Description
        Retorna índice superior (máximo) de array en dimensión especificada.

    Args
        array_var: Array.
        dimension: Dimensión (1-based, por defecto 1).

    Returns
        int: Índice superior (length - 1 en Python).

    Usage Example
        >>> ubound([1, 2, 3, 4, 5])
        4
        >>> ubound(["a", "b", "c"])
        2

    Cost
        O(1)
    """
    if not array_var:
        raise ValueError("Array vacío")
    
    return len(array_var) - 1


def Array_(*values: Any) -> List[Any]:
    """
    Description
        Crea array (lista) con valores proporcionados.

    Args
        *values: Valores para incluir en array.

    Returns
        List[Any]: Array con los valores.

    Usage Example
        >>> array_(1, 2, 3, 4, 5)
        [1, 2, 3, 4, 5]
        >>> array_("rojo", "verde", "azul")
        ['rojo', 'verde', 'azul']

    Cost
        O(n) donde n es número de valores
    """
    return list(values)
