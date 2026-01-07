"""FormuLite fxVBA Module

Visual Basic for Applications (VBA) compatible functions for FormuLite including:
- Type Conversion Functions (CBool, CInt, CDate, CStr, etc.)
- String Manipulation Functions (Left, Right, Mid, InStr, Replace, etc.)
- Date and Time Functions (DateAdd, DateDiff, DatePart, etc.)
- Mathematical Functions (Abs, Sin, Cos, Sqr, Round, etc.)
- Financial Functions (Pmt, Fv, Pv, Rate, NPer, etc.)
- Logic and Selection Functions (IIf, Choose, Switch, IsNull, etc.)
- System and File Functions (Dir, Environ, FileLen, GetAttr, etc.)
- Format Functions (Format, FormatCurrency, FormatNumber, etc.)
- Miscellaneous Functions (Hex, Oct, RGB, etc.)

Description
    Funciones compatibles con Visual Basic for Applications (VBA).
    Implementaciones Python funcionales de las funciones VBA más comunes.
    
    Las funciones usan los nombres originales de VBA en PascalCase:
    - Left(), Right(), Mid(), InStr()
    - DateAdd(), DateDiff(), DatePart()
    - IsNull(), IsArray(), IIf(), Choose()
    - CBool(), CInt(), CStr(), CDate()
    
    Notas especiales:
    - Funciones con sufijo $ en VBA (Chr$, Left$) tienen sufijo S en PascalCase
      (ChrS, LeftS, etc.)
    - Funciones con nombre de palabra reservada Python tienen sufijo _
      (Chr_, Int_, Str_, Len_, etc.)
    - Algunas funciones VBA sin guión bajo tienen alias sin _:
      Join (alias de Join_), Array (alias de Array_), Filter (alias de Filter_)
"""

from . import (
    array_functions as _array_functions,
    conversion_functions as _conversion_functions,
    string_functions as _string_functions,
    date_functions as _date_functions,
    math_functions as _math_functions,
    financial_functions as _financial_functions,
    logic_functions as _logic_functions,
    system_functions as _system_functions,
    format_functions as _format_functions,
    misc_functions as _misc_functions,
)

# Re-export all functions
from .array_functions import *
from .conversion_functions import *
from .string_functions import *
from .date_functions import *
from .math_functions import *
from .financial_functions import *
from .logic_functions import *
from .system_functions import *
from .format_functions import *
from .misc_functions import *

# Build consolidated __all__
__all__ = []
for _mod in (
    _array_functions,
    _conversion_functions,
    _string_functions,
    _date_functions,
    _math_functions,
    _financial_functions,
    _logic_functions,
    _system_functions,
    _format_functions,
    _misc_functions,
):
    names = getattr(_mod, "__all__", [n for n in dir(_mod) if not n.startswith("_")])
    __all__.extend(names)


# ============================================================================
# VBA Aliases (without underscore for reserved Python words)
# Aliases VBA sin guión bajo para palabras reservadas Python
# ============================================================================

# Estas funciones tienen _ porque son palabras reservadas en Python
# Pero en VBA no tienen el guión bajo
Join = Join_      # VBA: Join (Python usa join_ por palabra reservada)
Array = Array_    # VBA: Array (Python usa array_ por convención)
Filter = Filter_  # VBA: Filter (Python usa filter_ por palabra reservada)

# Agregar aliases VBA a __all__
__all__.extend(['Join', 'Array', 'Filter'])


