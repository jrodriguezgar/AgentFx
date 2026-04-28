# fxNumeric — Numeric & Mathematical Operations

The largest module in shortfx with 1,602 functions covering finance, statistics, geometry, transforms, series, number theory, and more.

## Submodules

| Submodule | Purpose |
|-----------|---------|
| [`arithmetic_functions`](../reference/fxNumeric/arithmetic_functions.md) | Basic arithmetic, GCD, LCM, factorial, modular arithmetic |
| [`calculator_functions`](../reference/fxNumeric/calculator_functions.md) | Expression evaluation, scientific calculator |
| [`complex_functions`](../reference/fxNumeric/complex_functions.md) | Complex number operations |
| [`conformal_functions`](../reference/fxNumeric/conformal_functions.md) | Conformal mappings |
| [`constants_functions`](../reference/fxNumeric/constants_functions.md) | Mathematical and physical constants |
| [`conversion_functions`](../reference/fxNumeric/conversion_functions.md) | Unit conversions (temperature, length, weight, etc.) |
| [`coordinate_systems_functions`](../reference/fxNumeric/coordinate_systems_functions.md) | Cartesian, polar, spherical, cylindrical conversions |
| [`curves_functions`](../reference/fxNumeric/curves_functions.md) | Parametric curves and curve analysis |
| [`distribution_functions`](../reference/fxNumeric/distribution_functions.md) | Probability distributions (normal, binomial, Poisson, etc.) |
| [`finance_functions`](../reference/fxNumeric/finance_functions.md) | Financial calculations (PV, FV, NPV, IRR, amortization) |
| [`finite_differences_functions`](../reference/fxNumeric/finite_differences_functions.md) | Finite difference methods |
| [`format_functions`](../reference/fxNumeric/format_functions.md) | Number formatting and display |
| [`geometry_functions`](../reference/fxNumeric/geometry_functions.md) | 2D/3D geometry, areas, volumes, distances |
| [`inequalities_functions`](../reference/fxNumeric/inequalities_functions.md) | Mathematical inequalities |
| [`interpolation_functions`](../reference/fxNumeric/interpolation_functions.md) | Linear, polynomial, spline interpolation |
| [`mechanics_functions`](../reference/fxNumeric/mechanics_functions.md) | Classical mechanics formulas |
| [`number_theory_functions`](../reference/fxNumeric/number_theory_functions.md) | Primes, divisors, modular arithmetic |
| [`numerical_methods_functions`](../reference/fxNumeric/numerical_methods_functions.md) | Root finding, numerical integration |
| [`polynomial_functions`](../reference/fxNumeric/polynomial_functions.md) | Polynomial operations and evaluation |
| [`probability_extra_functions`](../reference/fxNumeric/probability_extra_functions.md) | Advanced probability calculations |
| [`random_functions`](../reference/fxNumeric/random_functions.md) | Random number generation |
| [`rounding_functions`](../reference/fxNumeric/rounding_functions.md) | Rounding, truncation, ceiling, floor |
| [`series_functions`](../reference/fxNumeric/series_functions.md) | Mathematical series and summations |
| [`special_functions`](../reference/fxNumeric/special_functions.md) | Gamma, beta, Bessel, error functions |
| [`statistics_functions`](../reference/fxNumeric/statistics_functions.md) | Mean, median, std dev, regression, correlation |
| [`tensor_functions`](../reference/fxNumeric/tensor_functions.md) | Tensor operations |
| [`transform_functions`](../reference/fxNumeric/transform_functions.md) | Fourier, Laplace, Z-transforms |
| [`trigonometry_functions`](../reference/fxNumeric/trigonometry_functions.md) | Trigonometric and hyperbolic functions |
| [`vector_analysis_functions`](../reference/fxNumeric/vector_analysis_functions.md) | Vector operations, dot/cross product, gradients |

## Quick Examples

```python
from shortfx.fxNumeric import finance_functions, statistics_functions, geometry_functions

# Future Value
fv = finance_functions.future_value(rate=0.05, nper=10, pmt=-100, pv=-1000)

# Standard deviation
std = statistics_functions.standard_deviation([10, 20, 30, 40, 50])

# Circle area
area = geometry_functions.circle_area(radius=5)
```
