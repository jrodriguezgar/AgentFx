"""
Access Miscellaneous Functions Module.

Description
    Funciones varias de VBA/Access: conversiones hex/oct,
    funciones Access-específicas (AccessError, CurrentUser, Eval, SysCmd).
"""

from typing import Optional, Any

__all__ = [
    "AccessError",
    "CallByName",
    "CurrentUser",
    "Eval_",
    "Hex_",
    "Oct_",
    "QBColor",
    "RGB",
    "SysCmd",
]


def _access_only(function_name: str) -> None:
    """
    Description
        Helper interno para funciones que requieren Access.

    Args
        function_name: Nombre de función.

    Raises
        NotImplementedError: Siempre.

    Cost
        O(1)
    """
    raise NotImplementedError(
        f"{function_name} solo disponible en Microsoft Access."
    )


def AccessError(error_number: int) -> str:
    """
    Description
        Retorna descripción asociada a error Access/DAO.

    Args
        error_number: Código de error Access/DAO.

    Returns
        str: Descripción del error.

    Raises
        NotImplementedError: Cuando no se ejecuta en Access/DAO.

    Usage Example
        >>> accesserror(3024)
        NotImplementedError

    Cost
        N/A - Solo Access
    """
    _access_only("AccessError")


def CallByName(obj: Any, proc_name: str, call_type: int, *args: Any) -> Any:
    """
    Description
        Call a method or access a property on an object by name string.
        call_type: 1=vbGet, 2=vbLet, 4=vbMethod.

    Args
        obj: The object to operate on.
        proc_name: Name of the method or property.
        call_type: 1 (Get), 2 (Let/Set), or 4 (Method).
        *args: Arguments to pass to the method.

    Returns
        Any: Return value of the method or property.

    Raises
        AttributeError: If the object does not have the named attribute.
        ValueError: If call_type is invalid.

    Usage Example
        >>> CallByName("hello", "upper", 4)
        'HELLO'
        >>> CallByName([1, 2, 3], "__len__", 4)
        3

    Cost
        O(1)
    """
    VB_GET = 1
    VB_LET = 2
    VB_METHOD = 4

    if call_type == VB_GET:
        return getattr(obj, proc_name)
    elif call_type == VB_LET:

        if not args:
            raise ValueError("CallByName with vbLet requires a value argument")

        setattr(obj, proc_name, args[0])
        return None
    elif call_type == VB_METHOD:
        method = getattr(obj, proc_name)
        return method(*args)
    else:
        raise ValueError(f"Invalid call_type: {call_type}. Use 1 (Get), 2 (Let), or 4 (Method)")


def CurrentUser() -> str:
    """
    Description
        Retorna nombre del usuario actual de base de datos Access.

    Returns
        str: Nombre de usuario.

    Raises
        NotImplementedError: Cuando no se ejecuta en Access.

    Usage Example
        >>> currentuser()
        NotImplementedError

    Cost
        N/A - Solo Access
    """
    _access_only("CurrentUser")


def Eval_(expression: str) -> Any:
    """
    Description
        Interpreta/evalúa expresión numérica o función embebida.
        Retorna valor de referencia a objeto Access.

    Args
        expression: Expresión VBA/Access a evaluar.

    Returns
        Any: Resultado de evaluación.

    Raises
        NotImplementedError: Cuando no se ejecuta en Access.

    Usage Example
        >>> eval_("Forms!Main!Caption")
        NotImplementedError

    Cost
        N/A - Solo Access
    """
    _access_only("Eval")


def Hex_(number: int) -> str:
    """
    Description
        Retorna cadena equivalente a valor hexadecimal de número.

    Args
        number: Número a convertir.

    Returns
        str: Representación hexadecimal (sin prefijo 0x).

    Usage Example
        >>> hex_(255)
        'FF'
        >>> hex_(16)
        '10'

    Cost
        O(log n) donde n es el número
    """
    return hex(int(number))[2:].upper()
def Oct_(number: int) -> str:
    """
    Description
        Retorna cadena representando valor octal de número.

    Args
        number: Número a convertir.

    Returns
        str: Representación octal (sin prefijo 0o).

    Usage Example
        >>> oct_(8)
        '10'
        >>> oct_(64)
        '100'

    Cost
        O(log n) donde n es el número
    """
    return oct(int(number))[2:]
def SysCmd(
    action: int,
    argument2: Optional[int] = None,
    argument3: Optional[str] = None
) -> Any:
    """
    Description
        Ejecuta comando de sistema Access.

    Args
        action: Código de acción SysCmd Access.
        argument2: Argumento entero opcional.
        argument3: Argumento cadena opcional.

    Returns
        Any: Resultado según acción.

    Raises
        NotImplementedError: Cuando no se ejecuta en Access.

    Usage Example
        >>> syscmd(7)  # Versión Access
        NotImplementedError

    Cost
        N/A - Solo Access
    """
    _access_only("SysCmd")


def RGB(red: int, green: int, blue: int) -> int:
    """
    Description
        Retorna valor entero que representa color RGB.

    Args
        red: Componente rojo (0-255).
        green: Componente verde (0-255).
        blue: Componente azul (0-255).

    Returns
        int: Valor RGB como entero (formato VBA).

    Usage Example
        >>> rgb(255, 0, 0)  # Rojo
        255
        >>> rgb(0, 255, 0)  # Verde
        65280
        >>> rgb(0, 0, 255)  # Azul
        16711680

    Cost
        O(1)
    """
    # VBA usa formato: R + (G * 256) + (B * 65536)
    if not (0 <= red <= 255 and 0 <= green <= 255 and 0 <= blue <= 255):
        raise ValueError("Valores RGB deben estar entre 0 y 255")
    
    return red + (green << 8) + (blue << 16)


def QBColor(color: int) -> int:
    """
    Description
        Retorna valor RGB correspondiente a código de color QuickBasic.

    Args
        color: Código de color QuickBasic (0-15).

    Returns
        int: Valor RGB.

    Usage Example
        >>> qbcolor(0)  # Negro
        0
        >>> qbcolor(4)  # Rojo
        255
        >>> qbcolor(15)  # Blanco brillante
        16777215

    Cost
        O(1)
    """
    # Paleta de 16 colores QuickBasic
    qb_colors = {
        0: RGB(0, 0, 0),           # Negro
        1: RGB(0, 0, 128),         # Azul
        2: RGB(0, 128, 0),         # Verde
        3: RGB(0, 128, 128),       # Cyan
        4: RGB(128, 0, 0),         # Rojo
        5: RGB(128, 0, 128),       # Magenta
        6: RGB(128, 128, 0),       # Amarillo/Marrón
        7: RGB(192, 192, 192),     # Blanco/Gris claro
        8: RGB(128, 128, 128),     # Gris
        9: RGB(0, 0, 255),         # Azul brillante
        10: RGB(0, 255, 0),        # Verde brillante
        11: RGB(0, 255, 255),      # Cyan brillante
        12: RGB(255, 0, 0),        # Rojo brillante
        13: RGB(255, 0, 255),      # Magenta brillante
        14: RGB(255, 255, 0),      # Amarillo brillante
        15: RGB(255, 255, 255),    # Blanco brillante
    }
    
    if color not in qb_colors:
        raise ValueError(f"Código de color QB debe estar entre 0 y 15, recibido: {color}")
    
    return qb_colors[color]

