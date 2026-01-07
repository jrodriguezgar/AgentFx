"""Formulite package

Description
    High-level functions grouped by domain: strings, dates, numbers,
    Python helpers, Excel-compatible formulas, VBA-compatible functions,
    and Access-compatible formulas. This package exposes subpackages as
    namespaces; import concrete functions from their respective modules
    for clarity and faster imports.
"""

from . import fxString, fxDate, fxNumeric, fxPython, fxExcel, fxVBA

__all__ = [
    "fxString",
    "fxDate",
    "fxNumeric",
    "fxPython",
    "fxExcel",
    "fxVBA",
]
