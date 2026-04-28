"""fxDate — Date operations, evaluations, conversions, and system queries.

Re-exports all public functions from submodules. Submodules with
uninstalled optional dependencies are silently skipped.
"""

from agentfx._loader import auto_export

_SUBMODULES = [
    "date_convertions",
    "date_evaluations",
    "date_operations",
    "date_sys",
]

auto_export("agentfx.fxDate", _SUBMODULES, globals())

