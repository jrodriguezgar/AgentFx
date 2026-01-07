"""FormuLite fxExcel Module

Excel-compatible functions for FormuLite including:
- Date and Time Functions
- Engineering Functions  
- Database Functions
- Financial Functions
- Information Functions
- Logic Functions
- Statistical Functions
- Text & Data Functions

Description
    Each submodule defines its own `__all__` list. This __init__ uses
    wildcard imports to re-export all functions automatically, avoiding
    manual maintenance of long function lists.
"""

# Re-export all functions from submodules
from . import (
    date_formulas as _date_formulas,
    text_formulas as _text_formulas,
    engineering_formulas as _engineering_formulas,
    database_formulas as _database_formulas,
    financial_formulas as _financial_formulas,
    information_formulas as _information_formulas,
    lookup_formulas as _lookup_formulas,
    math_formulas as _math_formulas,
    statistic_formulas as _statistic_formulas,
    logic_formulas as _logic_formulas,
)

# Re-export all functions according to each submodule's __all__
from .date_formulas import *
from .text_formulas import *
from .engineering_formulas import *
from .database_formulas import *
from .financial_formulas import *
from .information_formulas import *
from .lookup_formulas import *
from .math_formulas import *
from .statistic_formulas import *
from .logic_formulas import *

# Build consolidated __all__ to keep star imports predictable
__all__ = []
for _mod in (
    _date_formulas,
    _text_formulas,
    _engineering_formulas,
    _database_formulas,
    _financial_formulas,
    _information_formulas,
    _lookup_formulas,
    _math_formulas,
    _statistic_formulas,
    _logic_formulas,
):
    names = getattr(_mod, "__all__", [n for n in dir(_mod) if not n.startswith("_")])
    __all__.extend(names)
