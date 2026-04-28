"""fxString — Text manipulation, formatting, validation, similarity, and Spanish NLP.

Re-exports all public functions from submodules. Submodules with
uninstalled optional dependencies are silently skipped.
"""

from shortfx._loader import auto_export

_SUBMODULES = [
    "string_convertions",
    "string_evaluations",
    "string_format",
    "string_operations",
    "string_similarity",
    "string_spanish",
    "string_spellcheck",
    "string_validations",
    "string_encoding",
    "string_caseconv",
    "string_regex",
    "string_hashing",
    "string_compression",
]

auto_export("shortfx.fxString", _SUBMODULES, globals())

