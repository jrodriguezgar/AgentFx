"""fxExcel — Excel-compatible formulas for math, text, lookup, finance, and more.

Re-exports all public functions from submodules. Submodules with
uninstalled optional dependencies are silently skipped.
"""

from formulite._loader import auto_export

_SUBMODULES = [
    "database_formulas",
    "date_formulas",
    "engineering_formulas",
    "financial_formulas",
    "information_formulas",
    "logic_formulas",
    "lookup_formulas",
    "math_formulas",
    "statistic_formulas",
    "text_formulas",
]

auto_export("formulite.fxExcel", _SUBMODULES, globals())

