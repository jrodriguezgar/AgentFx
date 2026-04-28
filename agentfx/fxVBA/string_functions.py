"""
Access String Manipulation Functions Module.

Description
    Funciones de manipulación de cadenas VBA/Access. Incluye versiones con
    sufijo $ que retornan String directamente (más rápidas en VBA).
    En Python ambas versiones son funcionalmente idénticas.
"""

from agentfx.fxString.string_operations import (
    left_substring as _core_left,
    right_substring as _core_right,
    substring as _core_mid,
    reverse_string as _core_reverse,
    left_bytes as _core_left_bytes,
    mid_bytes as _core_mid_bytes,
    right_bytes as _core_right_bytes,
    repeat_string as _core_repeat_string,
)
from agentfx.fxString.string_convertions import (
    char_from_code as _core_chr,
    code_from_char as _core_ord,
)
from agentfx.fxString.string_evaluations import (
    compare_strings as _core_compare_strings,
)
from agentfx.fxString.string_format import (
    to_upper as _core_upper,
    to_lower as _core_lower,
)
from agentfx.fxString.string_operations import (
    erase_lspaces as _core_ltrim,
    erase_rspaces as _core_rtrim,
    erase_lrspaces as _core_trim,
)
from agentfx.fxNumeric.conversion_functions import (
    number_to_string as _core_number_to_string,
)

__all__ = [
    "Asc",
    "AscB",
    "Chr_",
    "ChrW",
    "InStr",
    "InStrRev",
    "LCase",
    "Left",
    "LeftB",
    "Len_",
    "LenB",
    "LTrim",
    "Mid",
    "MidB",
    "Replace",
    "Right",
    "RightB",
    "RTrim",
    "Space",
    "Str_",
    "StrComp",
    "StrConv",
    "String",
    "StrReverse",
    "Trim",
    "UCase",
]


def Asc(string: str) -> int:
    """
    Description
        Retorna código de carácter del primer carácter de la cadena.

    Args
        string: Cadena de entrada.

    Returns
        int: Código ASCII/Unicode del primer carácter.

    Raises
        ValueError: Si la cadena está vacía.

    Usage Example
        >>> asc("A")
        65
        >>> asc("Hola")
        72

    Cost
        O(1)
    """
    if not string:
        raise ValueError("Cadena vacía")
    return _core_ord(string[0])


def AscB(string: str) -> int:
    """
    Description
        Retorna código del primer byte de la cadena.

    Args
        string: Cadena de entrada.

    Returns
        int: Código del primer byte.

    Usage Example
        >>> ascb("A")
        65

    Cost
        O(1)
    """
    if not string:
        raise ValueError("Cadena vacía")
    return ord(string[0]) & 0xFF


def Chr_(char_code: int) -> str:
    """
    Description
        Retorna carácter asociado con código de carácter especificado.

    Args
        char_code: Código ASCII/Unicode.

    Returns
        str: Carácter correspondiente.

    Usage Example
        >>> chr_(65)
        'A'
        >>> chr_(72)
        'H'

    Cost
        O(1)
    """
    return _core_chr(char_code)
def ChrW(char_code: int) -> str:
    """
    Description
        Retorna carácter Unicode asociado con código especificado.

    Args
        char_code: Código Unicode.

    Returns
        str: Carácter Unicode.

    Usage Example
        >>> chrw(8364)
        '€'

    Cost
        O(1)
    """
    return Chr_(char_code)
def InStr(
    start: int = 1,
    string1: str = "",
    string2: str = "",
    compare: int = 0
) -> int:
    """
    Description
        Retorna posición de una cadena dentro de otra (1-based).

    Args
        start: Posición inicial (1-based).
        string1: Cadena donde buscar.
        string2: Cadena a buscar.
        compare: Tipo de comparación (0=binario, 1=texto).

    Returns
        int: Posición donde se encuentra (1-based) o 0 si no se encuentra.

    Usage Example
        >>> instr(1, "Hola mundo", "mundo")
        6
        >>> instr(1, "Hola", "x")
        0

    Cost
        O(n*m) donde n=len(string1), m=len(string2)
    """
    if not string1 or not string2 or start < 1:
        return 0
    
    search_str = string1[start - 1:]
    
    if compare == 1:
        search_str = search_str.lower()
        string2 = string2.lower()
    
    pos = search_str.find(string2)
    return (start + pos) if pos != -1 else 0


def InStrRev(
    string1: str,
    string2: str,
    start: int = -1,
    compare: int = 0
) -> int:
    """
    Description
        Retorna posición de cadena buscando desde el final.

    Args
        string1: Cadena donde buscar.
        string2: Cadena a buscar.
        start: Posición inicial desde final (-1 = desde el final).
        compare: Tipo de comparación (0=binario, 1=texto).

    Returns
        int: Posición donde se encuentra (1-based) o 0.

    Usage Example
        >>> instrrev("Hola mundo mundo", "mundo")
        12

    Cost
        O(n*m) donde n=len(string1), m=len(string2)
    """
    if not string1 or not string2:
        return 0
    
    if start == -1:
        search_str = string1
    else:
        search_str = string1[:start]
    
    if compare == 1:
        search_str = search_str.lower()
        string2 = string2.lower()
    
    pos = search_str.rfind(string2)
    return (pos + 1) if pos != -1 else 0


def LCase(string: str) -> str:
    """
    Description
        Convierte cadena a minúsculas.

    Args
        string: Cadena de entrada.

    Returns
        str: Cadena en minúsculas.

    Usage Example
        >>> lcase("HOLA")
        'hola'

    Cost
        O(n) donde n es longitud de la cadena
    """
    return _core_lower(string)
def Left(string: str, length: int) -> str:
    """
    Description
        Retorna porción de cadena desde la izquierda.

    Args
        string: Cadena de entrada.
        length: Número de caracteres a extraer.

    Returns
        str: Subcadena desde la izquierda.

    Usage Example
        >>> left("Hola mundo", 4)
        'Hola'

    Cost
        O(n) donde n es length
    """
    return _core_left(string, length)
def LeftB(string: str, length: int) -> str:
    """
    Description
        Retorna porción de cadena (en bytes) desde la izquierda.

    Args
        string: Cadena de entrada.
        length: Número de bytes a extraer.

    Returns
        str: Subcadena.

    Usage Example
        >>> leftb("Hola", 4)
        'Hol'

    Cost
        O(n) donde n es length
    """
    return _core_left_bytes(string, length)
def Len_(expression: str) -> int:
    """
    Description
        Cuenta número de caracteres de una cadena.

    Args
        expression: Cadena a medir.

    Returns
        int: Longitud en caracteres.

    Usage Example
        >>> len_("Hola mundo")
        10

    Cost
        O(1)
    """
    return len(expression)


def LenB(expression: str) -> int:
    """
    Description
        Cuenta número de bytes de una cadena.

    Args
        expression: Cadena a medir.

    Returns
        int: Longitud en bytes.

    Usage Example
        >>> lenb("Hola")
        8

    Cost
        O(n) donde n es longitud de la cadena
    """
    return len(expression.encode('utf-16-le'))


def LTrim(string: str) -> str:
    """
    Description
        Retorna cadena sin espacios a la izquierda.

    Args
        string: Cadena de entrada.

    Returns
        str: Cadena sin espacios a la izquierda.

    Usage Example
        >>> ltrim("   Hola")
        'Hola'

    Cost
        O(n) donde n es longitud de la cadena
    """
    return _core_ltrim(string)
def Mid(string: str, start: int, length: int = None) -> str:
    """
    Description
        Retorna fracción de cadena definida por posición inicio y longitud.

    Args
        string: Cadena de entrada.
        start: Posición inicial (1-based).
        length: Longitud a extraer (None = hasta el final).

    Returns
        str: Subcadena.

    Usage Example
        >>> mid("Hola mundo", 6, 5)
        'mundo'

    Cost
        O(n) donde n es length
    """
    if length is None:
        return string[start - 1:]
    return _core_mid(string, start, length)
def MidB(string: str, start: int, length: int = None) -> str:
    """
    Description
        Retorna fracción (byte) de cadena.

    Args
        string: Cadena de entrada.
        start: Posición inicial en bytes (1-based).
        length: Longitud en bytes.

    Returns
        str: Subcadena.

    Usage Example
        >>> midb("Hola", 3, 4)
        'la'

    Cost
        O(n) donde n es length
    """
    return _core_mid_bytes(string, start, length)
def Replace(
    expression: str,
    find: str,
    replace_with: str,
    start: int = 1,
    count: int = -1,
    compare: int = 0
) -> str:
    """
    Description
        Retorna cadena donde subcadena se reemplaza por otra.

    Args
        expression: Cadena original.
        find: Subcadena a buscar.
        replace_with: Subcadena de reemplazo.
        start: Posición inicial (1-based).
        count: Número de reemplazos (-1 = todos).
        compare: Tipo de comparación (0=binario, 1=texto).

    Returns
        str: Cadena con reemplazos.

    Usage Example
        >>> replace("Hola mundo mundo", "mundo", "Python")
        'Hola Python Python'

    Cost
        O(n*m) donde n=len(expression), m=número de reemplazos
    """
    if start > 1:
        prefix = expression[:start - 1]
        expression = expression[start - 1:]
    else:
        prefix = ""
    
    if compare == 1:
        import re
        pattern = re.escape(find)
        if count == -1:
            result = re.sub(pattern, replace_with, expression, flags=re.IGNORECASE)
        else:
            result = re.sub(pattern, replace_with, expression, count=count, flags=re.IGNORECASE)
    else:
        if count == -1:
            result = expression.replace(find, replace_with)
        else:
            result = expression.replace(find, replace_with, count)
    
    return prefix + result


def Right(string: str, length: int) -> str:
    """
    Description
        Retorna porción de cadena desde la derecha.

    Args
        string: Cadena de entrada.
        length: Número de caracteres a extraer.

    Returns
        str: Subcadena desde la derecha.

    Usage Example
        >>> right("Hola mundo", 5)
        'mundo'

    Cost
        O(n) donde n es length
    """
    return _core_right(string, length)
def RightB(string: str, length: int) -> str:
    """
    Description
        Retorna porción de cadena (en bytes) desde la derecha.

    Args
        string: Cadena de entrada.
        length: Número de bytes a extraer.

    Returns
        str: Subcadena.

    Usage Example
        >>> rightb("Hola", 4)
        'la'

    Cost
        O(n) donde n es length
    """
    return _core_right_bytes(string, length)
def RTrim(string: str) -> str:
    """
    Description
        Recorta espacios a la derecha de una cadena.

    Args
        string: Cadena de entrada.

    Returns
        str: Cadena sin espacios a la derecha.

    Usage Example
        >>> rtrim("Hola   ")
        'Hola'

    Cost
        O(n) donde n es longitud de la cadena
    """
    return _core_rtrim(string)
def Space(number: int) -> str:
    """
    Description
        Retorna cadena con número de espacios indicado.

    Args
        number: Número de espacios.

    Returns
        str: Cadena con espacios.

    Usage Example
        >>> space(5)
        '     '

    Cost
        O(n) donde n es number
    """
    return _core_repeat_string(" ", number)


def Str_(number: float) -> str:
    """
    Description
        Convierte número en cadena.

    Args
        number: Número a convertir.

    Returns
        str: Representación en cadena.

    Usage Example
        >>> str_(42)
        '42'

    Cost
        O(1)
    """
    return _core_number_to_string(number)
def StrComp(string1: str, string2: str, compare: int = 0) -> int:
    """
    Description
        Compara dos cadenas y retorna resultado.

    Args
        string1: Primera cadena.
        string2: Segunda cadena.
        compare: Tipo de comparación (0=binario, 1=texto).

    Returns
        int: -1 si string1<string2, 0 si iguales, 1 si string1>string2.

    Usage Example
        >>> strcomp("abc", "ABC", 0)
        1
        >>> strcomp("abc", "ABC", 1)
        0

    Cost
        O(n) donde n es longitud mínima de las cadenas
    """
    return _core_compare_strings(string1, string2, case_sensitive=(compare != 1))


def StrConv(string: str, conversion: int, lcid: int = None) -> str:
    """
    Description
        Convierte cadena según parámetro de conversión.

    Args
        string: Cadena a convertir.
        conversion: Tipo conversión (1=mayús, 2=minús, 3=primera letra mayús, 64=Unicode, 128=desde Unicode).
        lcid: ID de configuración regional (opcional).

    Returns
        str: Cadena convertida.

    Usage Example
        >>> strconv("hola mundo", 1)
        'HOLA MUNDO'
        >>> strconv("HOLA MUNDO", 2)
        'hola mundo'
        >>> strconv("hola mundo", 3)
        'Hola Mundo'

    Cost
        O(n) donde n es longitud de la cadena
    """
    if conversion == 1:
        return string.upper()
    elif conversion == 2:
        return string.lower()
    elif conversion == 3:
        return string.title()
    elif conversion == 64:
        return string
    elif conversion == 128:
        return string
    return string


def String(number: int, character: str) -> str:
    """
    Description
        Retorna carácter o cadena que se repite n veces.

    Args
        number: Número de repeticiones.
        character: Carácter o cadena a repetir.

    Returns
        str: Cadena repetida.

    Usage Example
        >>> string(5, "x")
        'xxxxx'
        >>> string(3, "AB")
        'ABABAB'

    Cost
        O(n) donde n es number
    """
    if isinstance(character, int):
        character = chr(character)
    return _core_repeat_string(character, number)


def StrReverse(expression: str) -> str:
    """
    Description
        Retorna cadena invertida.

    Args
        expression: Cadena a invertir.

    Returns
        str: Cadena invertida.

    Usage Example
        >>> strreverse("Hola")
        'aloH'

    Cost
        O(n) donde n es longitud de la cadena
    """
    return _core_reverse(expression)


def Trim(string: str) -> str:
    """
    Description
        Recorta espacios a izquierda y derecha de cadena.

    Args
        string: Cadena de entrada.

    Returns
        str: Cadena sin espacios en los extremos.

    Usage Example
        >>> trim("  Hola  ")
        'Hola'

    Cost
        O(n) donde n es longitud de la cadena
    """
    return _core_trim(string)
def UCase(string: str) -> str:
    """
    Description
        Convierte cadena a mayúsculas.

    Args
        string: Cadena de entrada.

    Returns
        str: Cadena en mayúsculas.

    Usage Example
        >>> ucase("hola")
        'HOLA'

    Cost
        O(n) donde n es longitud de la cadena
    """
    return _core_upper(string)
