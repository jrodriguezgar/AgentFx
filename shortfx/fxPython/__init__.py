"""fxPython — Pythonic utilities for conversions, itertools, logic, and operations.

Re-exports all public functions from submodules. Submodules with
uninstalled optional dependencies are silently skipped.
"""

from shortfx._loader import auto_export

_SUBMODULES = [
    "py_convertions",
    "py_itertools",
    "py_logic",
    "py_operations",
    "py_tools",
]

auto_export("shortfx.fxPython", _SUBMODULES, globals())

