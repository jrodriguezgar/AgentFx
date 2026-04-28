"""fxNumeric — Numeric arithmetic, conversions, finance, statistics, and trigonometry.

Re-exports all public functions from submodules. Submodules with
uninstalled optional dependencies are silently skipped.
"""

from shortfx._loader import auto_export

_SUBMODULES = [
    "arithmetic_functions",
    "calculator_functions",
    "complex_functions",
    "conformal_functions",
    "constants_functions",
    "conversion_functions",
    "coordinate_systems_functions",
    "curves_functions",
    "distribution_functions",
    "finance_functions",
    "finite_differences_functions",
    "format_functions",
    "geometry_functions",
    "inequalities_functions",
    "interpolation_functions",
    "mechanics_functions",
    "number_theory_functions",
    "numerical_methods_functions",
    "polynomial_functions",
    "probability_extra_functions",
    "random_functions",
    "rounding_functions",
    "series_functions",
    "special_functions",
    "statistics_functions",
    "tensor_functions",
    "transform_functions",
    "trigonometry_functions",
    "vector_analysis_functions",
]

auto_export("shortfx.fxNumeric", _SUBMODULES, globals())

