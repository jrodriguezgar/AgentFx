"""fxVBA — VBA/Access-compatible functions for arrays, dates, math, strings, and more.

Re-exports all public functions from submodules. Submodules with
uninstalled optional dependencies are silently skipped.
"""

from agentfx._loader import auto_export

_SUBMODULES = [
    "array_functions",
    "conversion_functions",
    "date_functions",
    "financial_functions",
    "format_functions",
    "logic_functions",
    "math_functions",
    "misc_functions",
    "string_functions",
    "system_functions",
]

auto_export("agentfx.fxVBA", _SUBMODULES, globals())

