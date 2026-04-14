"""
Access System and File Functions Module.

Description
    Funciones de sistema, archivos y entorno de VBA/Access.
    Algunas requieren contexto Windows/Access y lanzan NotImplementedError.
"""

import os
import sys
from typing import Optional
from datetime import datetime

__all__ = [
    "BuildCriteria",
    "Command",
    "CurDir",
    "Dir_",
    "Environ",
    "Error",
    "FileDateTime",
    "FileLen",
    "GetAttr_",
    "InputBox",
    "MsgBox",
    "Nz",
    "Partition",
    "TypeName",
    "VarType",
]


def BuildCriteria(field: str, field_type: int, expression: str) -> str:
    """
    Description
        Construye expresión utilizable como criterio en filtro o cláusula WHERE.
        Función Access-specific, implementación simplificada.

    Args
        field: Nombre del campo.
        field_type: Tipo de campo (1=Si/No, 2=Byte, 3=Integer, etc.).
        expression: Expresión de criterio.

    Returns
        str: Expresión de criterio formateada.

    Usage Example
        >>> buildcriteria("CustomerID", 3, "42")
        '[CustomerID] = 42'

    Cost
        O(1)
    """
    if field_type in (1, 2, 3, 4, 5, 6, 7):
        return f"[{field}] = {expression}"
    else:
        return f"[{field}] = '{expression}'"


def CurDir(drive: Optional[str] = None) -> str:
    """
    Description
        Retorna ruta a unidad especificada o ruta actual.

    Args
        drive: Letra de unidad (opcional).

    Returns
        str: Ruta actual.

    Usage Example
        >>> curdir()
        'C:\\Users\\...'

    Cost
        O(1)
    """
    return os.getcwd()


def Dir_(pathname: str = "", attributes: int = 0) -> str:
    """
    Description
        Retorna nombre de archivo o directorio que coincide con patrón.

    Args
        pathname: Patrón de búsqueda (opcional).
        attributes: Atributos de archivo (0-64).

    Returns
        str: Nombre de archivo encontrado o cadena vacía.

    Usage Example
        >>> dir_("*.txt")
        'archivo.txt'

    Cost
        O(n) donde n es número de archivos en directorio
    """
    import glob
    
    if not pathname:
        pathname = "*"
    
    files = glob.glob(pathname)
    return files[0] if files else ""


def Environ(expression: str) -> str:
    """
    Description
        Retorna información del sistema según valor de Expression.

    Args
        expression: Variable de entorno o número.

    Returns
        str: Valor de variable de entorno.

    Usage Example
        >>> environ("PATH")
        'C:\\Windows\\...'

    Cost
        O(1)
    """
    if expression.isdigit():
        env_vars = list(os.environ.keys())
        idx = int(expression) - 1
        if 0 <= idx < len(env_vars):
            key = env_vars[idx]
            return f"{key}={os.environ[key]}"
        return ""
    return os.environ.get(expression, "")
def Error(err_number: int) -> str:
    """
    Description
        Retorna texto explicativo de un error.

    Args
        err_number: Número de error.

    Returns
        str: Descripción del error.

    Usage Example
        >>> error(5)
        'Invalid procedure call or argument'

    Cost
        O(1)
    """
    error_messages = {
        5: "Invalid procedure call or argument",
        6: "Overflow",
        7: "Out of memory",
        9: "Subscript out of range",
        11: "Division by zero",
        13: "Type mismatch",
        53: "File not found",
        91: "Object variable or With block variable not set",
    }
    return error_messages.get(err_number, f"Error {err_number}")


def FileDateTime(pathname: str) -> datetime:
    """
    Description
        Retorna fecha y hora cuando archivo se creó o modificó por última vez.

    Args
        pathname: Ruta del archivo.

    Returns
        datetime: Fecha y hora de modificación.

    Raises
        FileNotFoundError: Si archivo no existe.

    Usage Example
        >>> filedatetime("file.txt")
        datetime.datetime(2024, 1, 15, 14, 30, 0)

    Cost
        O(1)
    """
    timestamp = os.path.getmtime(pathname)
    return datetime.fromtimestamp(timestamp)


def FileLen(pathname: str) -> int:
    """
    Description
        Retorna número de bytes de archivo que no está abierto.

    Args
        pathname: Ruta del archivo.

    Returns
        int: Tamaño en bytes.

    Raises
        FileNotFoundError: Si archivo no existe.

    Usage Example
        >>> filelen("file.txt")
        1024

    Cost
        O(1)
    """
    return os.path.getsize(pathname)


def GetAttr_(pathname: str) -> int:
    """
    Description
        Retorna atributos de archivo, directorio o carpeta.

    Args
        pathname: Ruta del archivo/directorio.

    Returns
        int: Atributos (0=Normal, 1=ReadOnly, 2=Hidden, 4=System, 16=Directory, 32=Archive).

    Usage Example
        >>> getattr_("file.txt")
        0

    Cost
        O(1)
    """
    if not os.path.exists(pathname):
        raise FileNotFoundError(f"Archivo no encontrado: {pathname}")
    
    attrs = 0
    if os.path.isdir(pathname):
        attrs |= 16
    
    return attrs


def InputBox(
    prompt: str,
    title: str = "",
    default: str = "",
    xpos: int = None,
    ypos: int = None,
    helpfile: str = "",
    context: int = 0
) -> str:
    """
    Description
        Muestra cuadro de diálogo para solicitar datos (simulado con input).

    Args
        prompt: Texto del mensaje.
        title: Título del cuadro.
        default: Valor por defecto.
        xpos: Posición X (ignorado en Python).
        ypos: Posición Y (ignorado en Python).
        helpfile: Archivo de ayuda (ignorado).
        context: Contexto de ayuda (ignorado).

    Returns
        str: Texto ingresado.

    Usage Example
        >>> inputbox("Ingrese nombre:")
        'Juan'

    Cost
        O(1)
    """
    return input(f"{prompt} [{default}]: ") or default


def MsgBox(
    prompt: str,
    buttons: int = 0,
    title: str = "",
    helpfile: str = "",
    context: int = 0
) -> int:
    """
    Description
        Muestra cuadro de mensaje (simulado con print, retorna siempre OK).

    Args
        prompt: Cuerpo del mensaje.
        buttons: Estilo del MsgBox.
        title: Título.
        helpfile: Archivo de ayuda (ignorado).
        context: Contexto (ignorado).

    Returns
        int: Valor del botón pulsado (1=OK siempre).

    Usage Example
        >>> msgbox("Operación exitosa")
        1

    Cost
        O(1)
    """
    print(f"{title}\n{prompt}")
    return 1


def Nz(value: any, value_null: any = "") -> any:
    """
    Description
        Retorna Value, o si es nulo, el valor alternativo.

    Args
        value: Valor a evaluar.
        value_null: Valor alternativo si value es None.

    Returns
        Any: value o value_null.

    Usage Example
        >>> nz(None, "N/A")
        'N/A'
        >>> nz(42, 0)
        42

    Cost
        O(1)
    """
    return value_null if value is None else value


def Partition(number: float, start: float, stop: float, interval: float) -> str:
    """
    Description
        Retorna cadena representando rango donde se encuentra número.

    Args
        number: Cifra a evaluar.
        start: Límite inferior.
        stop: Límite superior.
        interval: Tamaño de intervalo.

    Returns
        str: Rango como cadena "inicio:fin".

    Usage Example
        >>> partition(75, 0, 100, 10)
        ' 70: 79'

    Cost
        O(1)
    """
    if number < start:
        return f" :{start - 1:3d}"
    elif number > stop:
        return f"{stop + 1:3d}: "
    else:
        range_start = int((number - start) // interval) * int(interval) + int(start)
        range_end = range_start + int(interval) - 1
        return f"{range_start:3d}:{range_end:3d}"


def TypeName(value: any) -> str:
    """
    Description
        Retorna cadena describiendo tipo de datos de valor.

    Args
        value: Valor a analizar.

    Returns
        str: Nombre del tipo.

    Usage Example
        >>> typename(42)
        'int'
        >>> typename("texto")
        'str'

    Cost
        O(1)
    """
    return type(value).__name__


def VarType(value: any) -> int:
    """
    Description
        Retorna entero según tipo de datos de Value.

    Args
        value: Valor a analizar.

    Returns
        int: Código de tipo (0=Empty, 1=Null, 2=Integer, 3=Long, 4=Single, 5=Double, 7=Date, 8=String, etc.).

    Usage Example
        >>> vartype(42)
        2
        >>> vartype("texto")
        8

    Cost
        O(1)
    """
    if value is None:
        return 1
    elif isinstance(value, bool):
        return 11
    elif isinstance(value, int):
        return 2
    elif isinstance(value, float):
        return 5
    elif isinstance(value, str):
        return 8
    elif isinstance(value, datetime):
        return 7
    else:
        return 0


def Command() -> str:
    """
    Description
        Retorna argumentos de línea de comandos pasados al programa.

    Returns
        str: Cadena con argumentos de línea de comandos.

    Usage Example
        >>> command()  # Si se ejecutó: python script.py arg1 arg2
        'arg1 arg2'

    Cost
        O(n) donde n es número de argumentos
    """
    # sys.argv[0] es el nombre del script, el resto son argumentos
    return " ".join(sys.argv[1:])
