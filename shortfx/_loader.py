"""Shared module-loading helper for shortfx sub-packages.

Centralises the dynamic re-export pattern used by every ``fx*``
package so the logic lives in a single place.
"""

import importlib
from typing import Dict, List


def auto_export(
    package_name: str,
    submodules: List[str],
    target_globals: Dict[str, object],
) -> None:
    """Import all public callables from *submodules* into *target_globals*.

    Args:
        package_name: Fully-qualified package name (e.g. ``"shortfx.fxDate"``).
        submodules: List of submodule names to scan.
        target_globals: The caller's ``globals()`` dict — public names are
            injected here so they appear at the package level.

    Example:
        >>> # inside shortfx/fxDate/__init__.py
        >>> from shortfx._loader import auto_export
        >>> auto_export("shortfx.fxDate", ["date_operations", ...], globals())

    Complexity: O(s·n) where s = submodules, n = names per module.
    """
    for mod_name in submodules:

        try:
            mod = importlib.import_module(f"{package_name}.{mod_name}")

            for attr in dir(mod):

                if not attr.startswith("_"):
                    obj = getattr(mod, attr)

                    if callable(obj):
                        target_globals[attr] = obj

        except ImportError:
            pass
