"""fxPython — Pythonic utilities for conversions, itertools, logic, and operations.

Re-exports all public functions from submodules. Submodules with
uninstalled optional dependencies are silently skipped.
"""

from formulite._loader import auto_export

_SUBMODULES = [
    "py_convertions",
    "py_itertools",
    "py_logic",
    "py_operations",
    "py_tools",
]

auto_export("formulite.fxPython", _SUBMODULES, globals())

