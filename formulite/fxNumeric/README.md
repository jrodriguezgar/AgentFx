# FormuLite - fxNumeric Module

Documentation of the available functions in the `fxNumeric` module of FormuLite.

## Overview

The fxNumeric module provides comprehensive numeric manipulation functions for FormuLite, including:
- **Arithmetic Operations**: Logarithms, powers, roots, factorials, GCD/LCM, combinatorics, matrices, bitwise, boolean arithmetic
- **Scientific Calculator**: Safe expression evaluator (AST-based, no eval)
- **Complex Numbers**: Complex arithmetic, polar form, De Moivre, roots of unity, complex exp/ln/trig (Spiegel)
- **Scientific Constants**: Mathematical and physical constants catalog
- **Numeric Conversions**: Type conversions, base conversions, cross-base conversions, formatting
- **Coordinate Systems**: Cylindrical, parabolic, elliptic, spheroidal, bipolar, toroidal conversions (Spiegel)
- **Rounding Functions**: Truncation, round up/down, banker's rounding, nearest multiple, significance rounding
- **Format Functions**: Number type checking, leading zeros, percentage, scientific notation, float comparison
- **Geometry**: Plane & solid geometry, conic sections, spherical trigonometry (Spiegel)
- **Inequalities**: AM-GM, Cauchy-Schwarz, Minkowski, Hölder, Jensen, Bernoulli, Young (Spiegel)
- **Number Theory**: Primes, Fibonacci, digital root, divisors, perfect numbers, Collatz
- **Numerical Methods**: Quadrature (trapezoidal, Simpson, Gauss, Romberg), differentiation, root-finding (bisection, Newton), ODE solvers (Euler, RK4, RK45) (Spiegel)
- **Mechanics**: Centroids, area/mass moments of inertia, parallel axis theorem, section modulus (Spiegel)
- **Statistical Functions**: Mean, median, correlation, variance, regression, kurtosis, skewness
- **Probability Distributions**: Normal, t, chi-squared, F, binomial, Poisson, exponential
- **Pure-Python Distributions**: Bernoulli, geometric, Cauchy, uniform, Pareto, Rayleigh, Maxwell-Boltzmann, log-logistic (Spiegel)
- **Conformal Mappings**: Möbius, Joukowski, power, exponential, Cayley, Koebe transforms (Spiegel)
- **Polynomial Algebra**: Addition, multiplication, division, derivative, integral, GCD, composition, partial fractions (Spiegel)
- **Finite Differences**: Difference tables, Newton forward/backward, Stirling, Bessel, Gauss interpolation (Spiegel)
- **Tensor Analysis**: Kronecker delta, Levi-Civita, metric tensors, Christoffel symbols, index raising/lowering (Spiegel)
- **Series & Expansions**: Arithmetic/geometric/harmonic series, Taylor/Maclaurin, Fourier, binomial (Spiegel)
- **Special Functions**: Legendre, Hermite, Laguerre, Chebyshev polynomials, elliptic integrals, Bessel J/Y/I/K, Bernoulli/Euler numbers, Fresnel integrals, polylogarithm (Spiegel)
- **Trigonometric Functions**: Standard and hyperbolic trig functions, versine, haversine
- **Integral Transforms**: DFT/IDFT, Laplace, Fourier transforms, convolution, Z-transform, Hartley, Abel (Spiegel)
- **Vector Analysis**: Gradient, divergence, curl, Laplacian, Jacobian, Hessian (Spiegel)
- **Curves & Curvature**: Cycloid, epicycloid, cardioid, lemniscate, spirals, astroid, nephroid, deltoid, limaçon, Cassini, conchoid, Lissajous, piriform, curvature, arc length (Spiegel)
- **Financial Functions**: Present value, future value, payments, depreciation, XIRR, MIRR
- **Interpolation**: Linear interpolation, clamped interpolation, piecewise interpolation, normalization, scaling
- **Random Generation**: Random integers, floats, choices, UUIDs, Gaussian distributions

## Module Structure

- **arithmetic_functions.py**: Logarithms, powers, roots, factorials, GCD/LCM, combinatorics, error functions, boolean arithmetic, division helpers, matrix operations (determinant, inverse, multiply, transpose, trace, LU decomposition, eigenvalues, norms, rank, Cholesky, QR, matrix power, adjugate, linear system solver), engineering functions, bitwise operations
- **calculator_functions.py**: Safe mathematical expression evaluator (AST-based)
- **complex_functions.py**: Complex number arithmetic (`+`, `-`, `×`, `÷`), modulus, argument, conjugate, polar/rectangular conversion, De Moivre, roots of unity, n-th roots, Euler formula, complex exp/ln/sin/cos/power (Spiegel)
- **conformal_functions.py**: Conformal mappings — Möbius transform, Joukowski airfoil, power/exponential/log maps, inversion, Schwarz-Christoffel, Cayley transform, Koebe function (Spiegel)
- **constants_functions.py**: Mathematical and physical constants catalog
- **conversion_functions.py**: Functions for converting between numeric types, formats, radix bases, and cross-base conversions
- **coordinate_systems_functions.py**: Curvilinear coordinate conversions — cylindrical, parabolic cylindrical, paraboloidal, elliptic cylindrical, prolate/oblate spheroidal, bipolar, toroidal (Spiegel)
- **curves_functions.py**: Parametric curves (cycloid, epicycloid, hypocycloid, cardioid, lemniscate, spirals, astroid, nephroid, deltoid, limaçon, Cassini oval, conchoid, Lissajous, piriform), curvature, arc length, differential geometry (Gaussian/mean curvature, principal curvatures, surface area of revolution) (Spiegel)
- **distribution_functions.py**: Probability distribution functions (requires scipy)
- **probability_extra_functions.py**: Pure-Python probability distributions — Bernoulli, geometric, Cauchy, uniform (continuous/discrete), Pareto, Rayleigh, Maxwell-Boltzmann, log-logistic; PDFs, CDFs, means, variances, entropies (Spiegel)
- **finance_functions.py**: Financial calculations and investment functions
- **finite_differences_functions.py**: Forward/backward/central difference tables, Newton forward/backward interpolation, Stirling, Bessel, Gauss interpolation, divided differences (Spiegel)
- **format_functions.py**: Number type checking, formatting (leading zeros, percentage, scientific notation), float comparison, percent change
- **interpolation_functions.py**: Linear interpolation, clamped, inverse, piecewise, range mapping, normalization, scaling, clipping
- **mechanics_functions.py**: Centroids (triangle, polygon, semicircle, sector, cone, hemisphere), area moments of inertia (rectangle, circle, annulus, triangle, semicircle, ellipse), mass moments (sphere, hollow sphere, cylinder, rod, disk, cone), parallel axis theorem, radius of gyration, section modulus, polar moment (Spiegel)
- **inequalities_functions.py**: AM-GM, AM-HM, power mean, Cauchy-Schwarz, triangle, Minkowski, Hölder, Young, Jensen, Chebyshev sum, rearrangement, Bernoulli inequalities (Spiegel)
- **number_theory_functions.py**: Primes, Fibonacci sequence, digital root, divisors, prime factors, perfect numbers, Collatz, Euler totient, palindrome numbers, modular arithmetic, Lucas numbers, Catalan numbers, partition function, Liouville/Carmichael lambda, sum of squares count, squarefree part
- **numerical_methods_functions.py**: Numerical integration (trapezoidal, Simpson, Gauss, Romberg, Monte Carlo), differentiation (forward/backward/central), root-finding (bisection, Newton-Raphson, secant), ODE solvers (Euler, RK2, RK4, adaptive RK45) (Spiegel)
- **random_functions.py**: Random number generation, samples, shuffles, UUIDs, Gaussian
- **polynomial_functions.py**: Polynomial algebra — addition, subtraction, multiplication, division, derivative, integral, evaluation (Horner), GCD (Euclidean), composition, partial fractions, polynomial from roots (Spiegel)
- **rounding_functions.py**: Rounding strategies (truncate, round up/down, banker's, nearest multiple, even/odd, ceiling/floor significance, quantize)
- **statistics_functions.py**: Statistical calculations, regression, data analysis, RMS, weighted variance, autocorrelation, Kendall tau, quantiles
- **tensor_functions.py**: Kronecker delta, Levi-Civita symbol, metric tensors (spherical, cylindrical, from Jacobian), Christoffel symbols, tensor contraction, outer product, index raising/lowering, Riemann curvature check, geodesic equation (Spiegel)
- **trigonometry_functions.py**: Trigonometric and hyperbolic functions, coordinate conversions (polar, spherical), haversine distance, sinc, versine, haversine, coversine
- **geometry_functions.py**: Plane geometry (distances, midpoints, lines, triangles, circles, ellipses, polygons), solid geometry (sphere, cylinder, cone, torus, ellipsoid, frustum), spherical trigonometry, conic sections (Spiegel)
- **series_functions.py**: Arithmetic/geometric/harmonic series, Taylor/Maclaurin expansions (exp, sin, cos, ln, arctan, sinh, cosh), binomial series, Fourier coefficients, Euler–Maclaurin summation (Spiegel)
- **special_functions.py**: Orthogonal polynomials (Legendre, Hermite, Laguerre, Chebyshev), Bernoulli/Euler numbers & polynomials, beta function, elliptic integrals, hypergeometric functions, Airy, Bessel J/Y/I/K, spherical Bessel, spherical harmonics, Riemann zeta, digamma, Lanczos gamma, exponential/sine/cosine integrals, Fresnel integrals, Dawson, polylogarithm, Stirling approximation, Wallis product, Gaussian/Dirichlet integrals, Jacobi theta functions, Dedekind eta, Weierstrass ℘, trigamma, polygamma (Spiegel)
- **transform_functions.py**: DFT/IDFT, numerical Laplace & Fourier transforms, convolution, cross-correlation, Z-transform, Hilbert transform, Mellin & Hankel transforms, DCT/IDCT, DST (Spiegel)
- **vector_analysis_functions.py**: Triple products, vector projection, gradient, divergence, curl, Laplacian, directional derivative, Jacobian, Hessian, line integral, surface integral, flux integral, divergence theorem verification (Spiegel)

---

## Table of Contents

- [Function Categories](#function-categories)
  - [Arithmetic Operations](#arithmetic-operations)
  - [Complex Numbers](#complex-numbers)
  - [Numeric Conversions](#numeric-conversions)
  - [Coordinate Systems](#coordinate-systems)
  - [Rounding Functions](#rounding-functions)
  - [Format Functions](#format-functions)
  - [Inequalities](#inequalities)
  - [Number Theory](#number-theory)
  - [Statistical Functions](#statistical-functions)
  - [Probability Distributions](#probability-distributions)
  - [Trigonometric Functions](#trigonometric-functions)
  - [Geometry](#geometry)
  - [Mechanics](#mechanics)
  - [Series & Expansions](#series--expansions)
  - [Special Functions](#special-functions)
  - [Integral Transforms](#integral-transforms)
  - [Vector Analysis](#vector-analysis)
  - [Numerical Methods](#numerical-methods)
  - [Curves & Curvature](#curves--curvature)
  - [Financial Functions](#financial-functions)
- [Function Index](#function-index)
- [Credits](#credits)

---

## Function Categories

### Arithmetic Operations
- [natural_log()](#natural_log) - Calculates natural logarithm base e of a positive number
- [common_log()](#common_log) - Calculates common logarithm base 10 of a positive number
- [log_base_n()](#log_base_n) - Calculates logarithm of a number to specified base N
- [log1p()](#log1p) - Calculates natural logarithm of 1+x with high precision near zero
- [power()](#power) - Calculates value of base raised to specified exponent
- [square_root()](#square_root) - Calculates square root of a non-negative number
- [cube_root()](#cube_root) - Calculates cube root of a number
- [nth_root()](#nth_root) - Calculates nth root of a number
- [factorial()](#factorial) - Calculates factorial of non-negative integer n!
- [double_factorial()](#double_factorial) - Calculates double factorial n!!
- [gamma()](#gamma) - Calculates Gamma function Γ(x)
- [log_gamma()](#log_gamma) - Calculates natural log of |Γ(x)|
- [greatest_common_divisor()](#greatest_common_divisor) - Calculates greatest common divisor of two integers
- [lcm()](#lcm) - Calculates least common multiple of two integers
- [gcd_list()](#gcd_list) - Calculates GCD of a list of integers
- [lcm_list()](#lcm_list) - Calculates LCM of a list of integers
- [absolute_value()](#absolute_value) - Returns absolute value of a number
- [sign()](#sign) - Returns sign of number as -1, 0, or 1
- [exp()](#exp) - Calculates e raised to power x
- [expm1()](#expm1) - Calculates e^x - 1 with high precision near zero
- [entropy()](#entropy) - Shannon entropy in bits (information theory)
- [error_function()](#error_function) - Calculates Gauss error function erf(x)
- [complementary_error_function()](#complementary_error_function) - Calculates erfc(x) = 1 - erf(x)
- [combinations()](#combinations) - Calculates binomial coefficient C(n, k)
- [permutations()](#permutations) - Calculates permutations P(n, k)
- [permutations_with_repetition()](#permutations_with_repetition) - Permutations with repetition n^k (PERMUTATIONA)
- [fibonacci()](#fibonacci) - Returns n-th Fibonacci number (0-indexed)
- [quotient()](#quotient) - Integer quotient (truncated division)
- [multinomial_coefficient()](#multinomial_coefficient) - Multinomial coefficient n!/(k1!·k2!·...·km!)
- [series_sum()](#series_sum) - Power series Σ(a_i · x^(n + i·step))

### Scientific Calculator
- [evaluate_expression()](#evaluate_expression) - Safely evaluate math expression from string
- [list_available_functions()](#list_available_functions) - List functions for expression evaluator
- [list_available_constants()](#list_available_constants) - List constants for expression evaluator

### Scientific Constants
- [get_constant()](#get_constant) - Look up scientific or mathematical constant by name
- [list_constants()](#list_constants) - List all available constants with metadata

### Numeric Conversions
- [float_to_int_truncated()](#float_to_int_truncated) - Converts float to integer truncating decimals towards zero
- [int_to_float()](#int_to_float) - Converts integer to floating-point number
- [number_to_complex()](#number_to_complex) - Converts number to complex with zero imaginary part
- [number_to_bool()](#number_to_bool) - Converts number to boolean, zero becomes False
- [bool_to_int()](#bool_to_int) - Converts boolean to integer, True=1 False=0
- [bool_to_float()](#bool_to_float) - Converts boolean to float, True=1.0 False=0.0
- [number_to_string()](#number_to_string) - Converts integer or float to string representation
- [round_float_to_int()](#round_float_to_int) - Rounds float to nearest integer
- [hex_to_int()](#hex_to_int) - Converts hexadecimal string to decimal integer
- [bin_to_int()](#bin_to_int) - Converts binary string to decimal integer
- [octal_to_int()](#octal_to_int) - Converts octal string to decimal integer
- [int_to_binary_clean()](#int_to_binary_clean) - Converts integer to binary string without prefix
- [int_to_hex_clean()](#int_to_hex_clean) - Converts integer to hexadecimal string without prefix
- [int_to_binary_with_prefix()](#int_to_binary_with_prefix) - Converts integer to binary string with 0b prefix
- [int_to_hex_with_prefix()](#int_to_hex_with_prefix) - Converts integer to hexadecimal string with 0x prefix
- [int_to_octal_with_prefix()](#int_to_octal_with_prefix) - Converts integer to octal string with 0o prefix
- [to_js_safe_integer()](#to_js_safe_integer) - Converts number to JavaScript safe integer range
- [safe_convert_number()](#safe_convert_number) - Safely converts value to numeric type with fallback
- [convert_string_to_float_with_locale()](#convert_string_to_float_with_locale) - Converts numeric string to float using locale separators
- [decimal_to_fraction()](#decimal_to_fraction) - Decimal to (numerator, denominator) tuple
- [fraction_to_decimal()](#fraction_to_decimal) - Fraction to float
- [int_to_roman()](#int_to_roman) - Integer (1-3999) to Roman numeral string
- [roman_to_int()](#roman_to_int) - Roman numeral string to integer
- [number_to_words()](#number_to_words) - Integer to words in English or Spanish
- [add_bool_to_int()](#add_bool_to_int) - Adds boolean value to integer treating True=1
- [is_numeric_type()](#is_numeric_type) - Verifies if value is numeric type
- [number_to_base()](#number_to_base) - Decimal to base 2–36 string (BASE)
- [base_to_decimal()](#base_to_decimal) - Base 2–36 string to decimal integer (DECIMAL)
- [ph_to_h_concentration()](#ph_to_h_concentration) - pH to hydrogen ion concentration [H⁺]
- [h_concentration_to_ph()](#h_concentration_to_ph) - Hydrogen ion concentration [H⁺] to pH
- [nusselt_number()](#nusselt_number) - Nusselt number Nu = hL/k (convective heat transfer)
- [strouhal_number()](#strouhal_number) - Strouhal number St = fL/v (vortex shedding)
- [knudsen_number()](#knudsen_number) - Knudsen number Kn = λ/L (molecular flow regime)

### Cross-Base Conversions
- [bin_to_hex()](#bin_to_hex) - Binary to hexadecimal (BIN2HEX)
- [bin_to_oct()](#bin_to_oct) - Binary to octal (BIN2OCT)
- [dec_to_oct()](#dec_to_oct) - Decimal to octal (DEC2OCT)
- [hex_to_bin()](#hex_to_bin) - Hexadecimal to binary (HEX2BIN)
- [hex_to_oct()](#hex_to_oct) - Hexadecimal to octal (HEX2OCT)
- [oct_to_bin()](#oct_to_bin) - Octal to binary (OCT2BIN)
- [oct_to_hex()](#oct_to_hex) - Octal to hexadecimal (OCT2HEX)

### Interpolation
- [linear_interpolate()](#linear_interpolate) - Linear interpolation between two points
- [clamp_interpolate()](#clamp_interpolate) - Clamped linear interpolation bounded to [y0, y1]
- [inverse_interpolate()](#inverse_interpolate) - Inverse lerp: find t in [0,1] such that lerp(t)==y
- [piecewise_interpolate()](#piecewise_interpolate) - Piecewise linear interpolation over sorted breakpoints
- [map_range()](#map_range) - Map value from one range to another
- [linear_interpolation()](#linear_interpolation) - Piecewise linear interpolation and extrapolation
- [normalize_list()](#normalize_list) - Min-max normalization to [0, 1] range

### Random Generation
- [set_random_seed()](#set_random_seed) - Set reproducible random seed
- [random_int()](#random_int) - Random integer in [low, high]
- [random_float()](#random_float) - Random float in [low, high)
- [random_choice()](#random_choice) - Random element from sequence
- [random_sample()](#random_sample) - K unique random elements from sequence
- [random_shuffle()](#random_shuffle) - Return new shuffled copy of sequence
- [random_gaussian()](#random_gaussian) - Random value from normal distribution
- [random_weighted_choice()](#random_weighted_choice) - Weighted random selection
- [random_uuid()](#random_uuid) - Generate random UUID4 string
- [random_bool()](#random_bool) - Random boolean with given probability of True
- [random_array()](#random_array) - 2-D array of random numbers (RANDARRAY)

### Rounding Functions
- [truncate_float()](#truncate_float) - Truncates float eliminating decimal part towards zero
- [round_to_n_decimals()](#round_to_n_decimals) - Rounds float to specific number of decimal places
- [round_up()](#round_up) - Rounds float upward to nearest integer ceiling
- [round_down()](#round_down) - Rounds float downward to nearest integer floor
- [add_with_exact_precision()](#add_with_exact_precision) - Adds two numbers using Decimal for exact precision
- [manual_round_and_cast()](#manual_round_and_cast) - Performs manual rounding to nearest integer then casts
- [manual_round_up_to_int()](#manual_round_up_to_int) - Rounds float to nearest integer always upwards
- [manual_round_down_to_int()](#manual_round_down_to_int) - Rounds float to nearest integer always downwards
- [round_half_even()](#round_half_even) - Performs banker's rounding with ROUND_HALF_EVEN policy
- [round_to_nearest_multiple()](#round_to_nearest_multiple) - Rounds number to nearest multiple of base
- [even()](#even) - Rounds up to nearest even integer
- [odd()](#odd) - Rounds up to nearest odd integer
- [ceiling_significance()](#ceiling_significance) - Rounds up to significance multiple
- [floor_significance()](#floor_significance) - Rounds down to significance multiple
- [quantize_number()](#quantize_number) - Quantizes number to discrete multiples of step

### Format Functions
- [format_with_leading_zeros()](#format_with_leading_zeros) - Formats integer with leading zeros to width
- [format_as_percentage()](#format_as_percentage) - Formats float as percentage string with decimals
- [format_as_scientific_notation()](#format_as_scientific_notation) - Formats float in scientific notation
- [compare_floats_with_tolerance()](#compare_floats_with_tolerance) - Compares floats within relative and absolute tolerance
- [percent_change()](#percent_change) - Percentage change between two values
- [percent_of()](#percent_of) - What percentage part is of whole

### Number Theory
- [is_prime()](#is_prime) - Verifies if number is prime
- [is_even()](#is_even) - True if integer is even (ISEVEN)
- [is_odd()](#is_odd) - True if integer is odd (ISODD)
- [get_primes_up_to()](#get_primes_up_to) - Generates list of primes up to limit using sieve
- [fibonacci_sequence()](#fibonacci_sequence) - Returns the first n Fibonacci numbers
- [digital_root()](#digital_root) - Computes the digital root (repeated digit sum until single digit)
- [divisors()](#divisors) - Returns all positive divisors of n in ascending order
- [prime_factors()](#prime_factors) - Returns the prime factorization of n in ascending order
- [sum_of_divisors()](#sum_of_divisors) - Returns the sum of proper divisors of n
- [is_perfect_number()](#is_perfect_number) - Checks whether n is a perfect number
- [collatz_length()](#collatz_length) - Counts steps in the Collatz sequence until reaching 1
- [is_fibonacci_number()](#is_fibonacci_number) - True if n belongs to the Fibonacci sequence
- [carmichael_lambda()](#carmichael_lambda) - Carmichael function λ(n) — smallest universal exponent
- [is_lychrel_candidate()](#is_lychrel_candidate) - True if reverse-and-add never produces palindrome
- [digit_factorial_sum()](#digit_factorial_sum) - Sum of factorials of digits (factorion check)

### Arithmetic Helpers
- [combinations_with_repetition()](#combinations_with_repetition) - Combinations with repetition C(n+k-1, k)
- [product_list()](#product_list) - Calculates product of all values in list
- [force_float_division()](#force_float_division) - Performs division ensuring float result always
- [true_division()](#true_division) - Performs floating-point division always returning float
- [floor_division()](#floor_division) - Performs integer division truncating result downwards
- [safe_division_for_context()](#safe_division_for_context) - Performs division selecting float or integer based context
- [modulo()](#modulo) - Returns remainder of division (MOD)
- [sqrt_pi()](#sqrt_pi) - Calculates square root of number times pi
- [safe_sum_with_none()](#safe_sum_with_none) - Adds two numbers safely treating None as zero
- [reduce_to_modulo_range()](#reduce_to_modulo_range) - Converts value to cyclic range using modulo

### Matrix & Engineering Functions
- [matrix_determinant()](#matrix_determinant) - Determinant of a square matrix (MDETERM)
- [matrix_inverse()](#matrix_inverse) - Inverse of a square matrix (MINVERSE)
- [matrix_multiply()](#matrix_multiply) - Matrix multiplication A × B (MMULT)
- [identity_matrix()](#identity_matrix) - Identity matrix of size n (MUNIT)
- [delta()](#delta) - Kronecker delta, 1 if equal else 0 (DELTA)
- [gestep()](#gestep) - Heaviside step, 1 if number >= step else 0 (GESTEP)

### Interpolation Helpers
- [normalize_to_0_1_range()](#normalize_to_0_1_range) - Normalizes number to scale within 0-1 range
- [scale_to_new_range()](#scale_to_new_range) - Scales number from original range to new range
- [clip_number()](#clip_number) - Forces number within specific minimum-maximum range
- [map_range()](#map_range) - Maps value from one numeric range to another

### Statistical Functions
- [calculate_frecuency()](#calculate_frecuency) - Calculates frequency of each value in list
- [calculate_mean()](#calculate_mean) - Calculates arithmetic mean average of list
- [calculate_median()](#calculate_median) - Calculates median middle value of list
- [calculate_mode()](#calculate_mode) - Calculates mode most frequent values in list
- [calculate_range()](#calculate_range) - Calculates range difference between max and min
- [calculate_variance()](#calculate_variance) - Calculates variance of list sample or population
- [calculate_standard_deviation()](#calculate_standard_deviation) - Calculates standard deviation of list sample or population
- [calculate_interquartile_range()](#calculate_interquartile_range) - Calculates IQR Q3 minus Q1 of list
- [calculate_covariance()](#calculate_covariance) - Calculates covariance between two lists sample or population
- [calculate_pearson_correlation()](#calculate_pearson_correlation) - Calculates Pearson correlation coefficient between two lists
- [calculate_percentile()](#calculate_percentile) - Calculates specified percentile value of list
- [sum_of_squares()](#sum_of_squares) - Calculates sum of squares of list values

### Cumulative, Rolling & Window Functions
- [cumulative_sum()](#cumulative_sum) - Cumulative sum (running total) of list values
- [cumulative_product()](#cumulative_product) - Cumulative product of list values
- [cumulative_max()](#cumulative_max) - Cumulative maximum of list values
- [cumulative_min()](#cumulative_min) - Cumulative minimum of list values
- [rolling_mean()](#rolling_mean) - Rolling mean over a sliding window
- [rolling_sum()](#rolling_sum) - Rolling sum over a sliding window
- [rolling_median()](#rolling_median) - Rolling median over a sliding window
- [diff()](#diff) - Successive differences between elements
- [lag()](#lag) - Shift values forward (lag) by N periods
- [lead()](#lead) - Shift values backward (lead) by N periods
- [argmax()](#argmax) - Index of maximum value in list
- [argmin()](#argmin) - Index of minimum value in list
- [fillna()](#fillna) - Replace None/NaN with a fill value
- [ffill()](#ffill) - Forward-fill None/NaN gaps in list
- [bfill()](#bfill) - Backward-fill None/NaN gaps in list
- [rank()](#rank) - Rank of each value (average, min, max, dense, ordinal)
- [describe()](#describe) - Summary statistics dict (count, mean, std, min, q25, q50, q75, max)
- [geometric_mean()](#geometric_mean) - Calculates geometric mean of positive numbers
- [harmonic_mean()](#harmonic_mean) - Calculates harmonic mean of positive numbers
- [trimmed_mean()](#trimmed_mean) - Calculates mean after trimming percent from each end
- [weighted_mean()](#weighted_mean) - Calculates weighted arithmetic mean
- [average_deviation()](#average_deviation) - Calculates mean absolute deviation from the mean
- [deviation_squared()](#deviation_squared) - Calculates sum of squared deviations (DEVSQ)
- [kurtosis()](#kurtosis) - Calculates kurtosis (peakedness) of distribution
- [skewness()](#skewness) - Calculates skewness (asymmetry) of distribution
- [large()](#large) - Returns K-th largest value in a dataset
- [small()](#small) - Returns K-th smallest value in a dataset
- [slope()](#slope) - Calculates slope of linear regression line
- [intercept()](#intercept) - Calculates Y-intercept of linear regression line
- [forecast_linear()](#forecast_linear) - Predicts Y for X using linear regression
- [fisher()](#fisher) - Calculates Fisher transformation
- [fisher_inv()](#fisher_inv) - Calculates inverse Fisher transformation
- [z_score()](#z_score) - Standardizes value to z-score
- [confidence_norm()](#confidence_norm) - Calculates normal confidence interval half-width
- [confidence_t()](#confidence_t) - Calculates Student-t confidence interval half-width
- [frequency_bins()](#frequency_bins) - Calculates frequency distribution into bins
- [sum_product()](#sum_product) - Sum of element-wise products of arrays
- [count_true_with_sum()](#count_true_with_sum) - Counts True values in boolean list using sum
- [sum_list()](#sum_list) - Calculates sum of all values in list
- [covariance_matrix()](#covariance_matrix) - Computes sample covariance matrix for multiple variables
- [exponential_moving_average()](#exponential_moving_average) - Calculates exponential moving average (EMA)
- [coefficient_of_variation()](#coefficient_of_variation) - CV: standard deviation as ratio of the mean
- [standard_error()](#standard_error) - Standard error of the mean (SEM)
- [median_absolute_deviation()](#median_absolute_deviation) - Robust dispersion measure resistant to outliers
- [winsorize()](#winsorize) - Cap extreme values at percentile boundaries
- [spearman_correlation()](#spearman_correlation) - Non-parametric rank correlation coefficient
- [r_squared()](#r_squared) - Coefficient of determination R² for linear regression
- [mean_squared_error()](#mean_squared_error) - MSE between observed and predicted values
- [pct_change()](#pct_change) - Percentage change between consecutive elements
- [rolling_std()](#rolling_std) - Rolling standard deviation over fixed window
- [outliers_iqr()](#outliers_iqr) - Detect outliers using IQR fences method
- [entropy()](#entropy) - Shannon entropy in bits (information theory)
- [weighted_median()](#weighted_median) - Weighted median for robust central tendency
- [standard_error_estimate()](#standard_error_estimate) - Standard error of predicted y in regression (STEYX)
- [probability_range()](#probability_range) - Sum of probabilities in value range (PROB)
- [quartile_deviation()](#quartile_deviation) - Semi-interquartile range (Q3−Q1)/2
- [bowley_skewness()](#bowley_skewness) - Bowley coefficient of skewness from quartiles
- [coefficient_of_quartile_deviation()](#coefficient_of_quartile_deviation) - CQD = (Q3−Q1)/(Q3+Q1)
- [tukey_trimean()](#tukey_trimean) - Tukey's trimean: (Q1 + 2·Q2 + Q3) / 4
- [midrange()](#midrange) - Midrange: (max + min) / 2
- [midhinge()](#midhinge) - Midhinge: (Q1 + Q3) / 2
- [contraharmonic_mean()](#contraharmonic_mean) - Contraharmonic mean: Σx² / Σx

### Probability Distributions
- [norm_dist()](#norm_dist) - Normal distribution CDF or PDF
- [norm_inv()](#norm_inv) - Inverse normal distribution
- [norm_s_dist()](#norm_s_dist) - Standard normal distribution
- [norm_s_inv()](#norm_s_inv) - Inverse standard normal distribution
- [t_dist()](#t_dist) - Student's t-distribution CDF or PDF
- [t_inv()](#t_inv) - Inverse Student's t-distribution
- [binom_dist()](#binom_dist) - Binomial distribution PMF or CDF
- [poisson_dist()](#poisson_dist) - Poisson distribution PMF or CDF
- [chisq_dist()](#chisq_dist) - Chi-squared distribution CDF or PDF
- [chisq_inv()](#chisq_inv) - Inverse chi-squared distribution
- [f_dist()](#f_dist) - F-distribution CDF or PDF
- [f_inv()](#f_inv) - Inverse F-distribution
- [expon_dist()](#expon_dist) - Exponential distribution CDF or PDF
- [gauss()](#gauss) - P(0 < Z < z) for standard normal (GAUSS)
- [phi()](#phi) - Standard normal PDF φ(x) (PHI)

### Trigonometric Functions
- [sine()](#sine) - Calculates sine of angle in radians
- [cosine()](#cosine) - Calculates cosine of angle in radians
- [tangent()](#tangent) - Calculates tangent of angle in radians
- [arcsine()](#arcsine) - Calculates inverse sine in radians from value
- [arccosine()](#arccosine) - Calculates inverse cosine in radians from value
- [arctangent()](#arctangent) - Calculates inverse tangent in radians from value
- [arctangent2()](#arctangent2) - Calculates inverse tangent of y/x considering quadrant
- [hypotenuse()](#hypotenuse) - Calculates Euclidean norm length of right triangle hypotenuse
- [hyperbolic_sine()](#hyperbolic_sine) - Calculates hyperbolic sine of value
- [hyperbolic_cosine()](#hyperbolic_cosine) - Calculates hyperbolic cosine of value
- [hyperbolic_tangent()](#hyperbolic_tangent) - Calculates hyperbolic tangent of value
- [inverse_hyperbolic_sine()](#inverse_hyperbolic_sine) - Calculates inverse hyperbolic sine arcsinh of value
- [inverse_hyperbolic_cosine()](#inverse_hyperbolic_cosine) - Calculates inverse hyperbolic cosine arccosh of value
- [inverse_hyperbolic_tangent()](#inverse_hyperbolic_tangent) - Calculates inverse hyperbolic tangent arctanh of value
- [inverse_secant()](#inverse_secant) - Calculates inverse secant arcsec in radians
- [inverse_cosecant()](#inverse_cosecant) - Calculates inverse cosecant arccosec in radians
- [inverse_cotangent()](#inverse_cotangent) - Calculates inverse cotangent arccotan in radians
- [inverse_hyperbolic_secant()](#inverse_hyperbolic_secant) - Calculates inverse hyperbolic secant arcsech of value
- [inverse_hyperbolic_cosecant()](#inverse_hyperbolic_cosecant) - Calculates inverse hyperbolic cosecant arccosech of value
- [inverse_hyperbolic_cotangent()](#inverse_hyperbolic_cotangent) - Calculates inverse hyperbolic cotangent arccotanh of value
- [degrees_to_radians()](#degrees_to_radians) - Converts angle from degrees to radians
- [radians_to_degrees()](#radians_to_degrees) - Converts angle from radians to degrees
- [secant()](#secant) - Calculates secant of angle one over cosine
- [cosecant()](#cosecant) - Calculates cosecant of angle one over sine
- [cotangent()](#cotangent) - Calculates cotangent of angle one over tangent
- [versine()](#versine) - Calculates versine (1 − cos θ) of angle in radians
- [haversine_trig()](#haversine_trig) - Calculates haversine ((1 − cos θ)/2) of angle in radians
- [exsecant()](#exsecant) - Calculates exsecant (sec θ − 1) of angle in radians
- [excosecant()](#excosecant) - Calculates excosecant (csc θ − 1) of angle in radians
- [coversine()](#coversine) - Calculates coversine (1 − sin θ) of angle in radians

### Geometry
- [distance_2d()](#distance_2d) - Euclidean distance between two 2D points
- [distance_3d()](#distance_3d) - Euclidean distance between two 3D points
- [midpoint_2d()](#midpoint_2d) - Midpoint of two 2D points
- [midpoint_3d()](#midpoint_3d) - Midpoint of two 3D points
- [slope()](#slope) - Slope of line through two 2D points
- [line_equation()](#line_equation) - Line equation coefficients (Ax + By + C = 0)
- [point_to_line_distance()](#point_to_line_distance) - Distance from point to line Ax + By + C = 0
- [triangle_area_vertices()](#triangle_area_vertices) - Triangle area using Shoelace formula
- [triangle_area_heron()](#triangle_area_heron) - Triangle area using Heron's formula
- [triangle_perimeter()](#triangle_perimeter) - Triangle perimeter from three side lengths
- [law_of_cosines_side()](#law_of_cosines_side) - Side from two sides and included angle
- [law_of_cosines_angle()](#law_of_cosines_angle) - Angle from three side lengths
- [law_of_sines_side()](#law_of_sines_side) - Side from angle-side-angle using law of sines
- [law_of_sines_angle()](#law_of_sines_angle) - Angle from side-side-angle using law of sines
- [circle_area()](#circle_area) - Area of circle from radius
- [circle_circumference()](#circle_circumference) - Circumference of circle from radius
- [circle_arc_length()](#circle_arc_length) - Arc length from radius and central angle
- [circle_sector_area()](#circle_sector_area) - Sector area from radius and central angle
- [circle_segment_area()](#circle_segment_area) - Segment area from radius and central angle
- [ellipse_area()](#ellipse_area) - Area of ellipse from semi-axes
- [ellipse_circumference_approx()](#ellipse_circumference_approx) - Approximate ellipse circumference (Ramanujan)
- [regular_polygon_area()](#regular_polygon_area) - Area of regular polygon from side count and length
- [regular_polygon_perimeter()](#regular_polygon_perimeter) - Perimeter of regular polygon
- [regular_polygon_interior_angle()](#regular_polygon_interior_angle) - Interior angle of regular polygon
- [sphere_volume()](#sphere_volume) - Volume of sphere
- [sphere_surface_area()](#sphere_surface_area) - Surface area of sphere
- [cylinder_volume()](#cylinder_volume) - Volume of cylinder
- [cylinder_surface_area()](#cylinder_surface_area) - Total surface area of cylinder
- [cone_volume()](#cone_volume) - Volume of cone
- [cone_surface_area()](#cone_surface_area) - Total surface area of cone
- [cone_slant_height()](#cone_slant_height) - Slant height of cone
- [pyramid_volume()](#pyramid_volume) - Volume of right pyramid
- [torus_volume()](#torus_volume) - Volume of torus
- [torus_surface_area()](#torus_surface_area) - Surface area of torus
- [frustum_volume()](#frustum_volume) - Volume of frustum of a cone
- [ellipsoid_volume()](#ellipsoid_volume) - Volume of ellipsoid
- [spherical_cap_volume()](#spherical_cap_volume) - Volume of spherical cap
- [spherical_cap_surface_area()](#spherical_cap_surface_area) - Surface area of spherical cap
- [haversine_distance()](#haversine_distance) - Great-circle distance between lat/lon points
- [spherical_law_of_cosines()](#spherical_law_of_cosines) - Spherical law of cosines for side
- [spherical_excess()](#spherical_excess) - Spherical excess (area of spherical triangle)
- [parabola_focus()](#parabola_focus) - Focus of parabola y = ax² + bx + c
- [parabola_directrix()](#parabola_directrix) - Directrix of parabola y = ax² + bx + c
- [hyperbola_eccentricity()](#hyperbola_eccentricity) - Eccentricity of hyperbola
- [hyperbola_asymptotes()](#hyperbola_asymptotes) - Asymptote slopes of hyperbola

### Series & Expansions
- [arithmetic_series_sum()](#arithmetic_series_sum) - Sum of arithmetic series
- [geometric_series_sum()](#geometric_series_sum) - Sum of finite geometric series
- [geometric_series_infinite()](#geometric_series_infinite) - Sum of infinite geometric series |r| < 1
- [harmonic_series_partial()](#harmonic_series_partial) - Partial sum of harmonic series
- [generalized_harmonic()](#generalized_harmonic) - Generalized harmonic number H(n, m)
- [power_series_eval()](#power_series_eval) - Evaluate power series from coefficients at point x
- [taylor_exp()](#taylor_exp) - Taylor expansion of exp(x) to n terms
- [taylor_sin()](#taylor_sin) - Taylor expansion of sin(x) to n terms
- [taylor_cos()](#taylor_cos) - Taylor expansion of cos(x) to n terms
- [taylor_ln1p()](#taylor_ln1p) - Taylor expansion of ln(1+x) to n terms
- [taylor_atan()](#taylor_atan) - Taylor expansion of arctan(x) to n terms
- [taylor_sinh()](#taylor_sinh) - Taylor expansion of sinh(x) to n terms
- [taylor_cosh()](#taylor_cosh) - Taylor expansion of cosh(x) to n terms
- [taylor_asin()](#taylor_asin) - Taylor expansion of arcsin(x) to n terms
- [binomial_series()](#binomial_series) - Binomial series expansion (1+x)^α to n terms
- [fourier_coefficients()](#fourier_coefficients) - Numerical Fourier coefficients a_k, b_k
- [fourier_series_eval()](#fourier_series_eval) - Evaluate Fourier series at point x
- [euler_maclaurin_sum()](#euler_maclaurin_sum) - Euler–Maclaurin summation formula
- [alternating_series_sum()](#alternating_series_sum) - Partial sum of alternating series
- [p_series_partial()](#p_series_partial) - Partial sum of p-series Σ 1/k^p
- [leibniz_pi()](#leibniz_pi) - Leibniz formula for π/4 to n terms
- [basel_series()](#basel_series) - Basel series partial sum (π²/6)

### Special Functions
- [legendre_polynomial()](#legendre_polynomial) - Legendre polynomial P_n(x) via recurrence
- [associated_legendre()](#associated_legendre) - Associated Legendre function P_n^m(x)
- [hermite_polynomial()](#hermite_polynomial) - Hermite polynomial H_n(x) (physicist's convention)
- [laguerre_polynomial()](#laguerre_polynomial) - Laguerre polynomial L_n(x)
- [generalized_laguerre_polynomial()](#generalized_laguerre_polynomial) - Generalized Laguerre L_n^α(x)
- [chebyshev_polynomial_first()](#chebyshev_polynomial_first) - Chebyshev polynomial T_n(x) of first kind
- [chebyshev_polynomial_second()](#chebyshev_polynomial_second) - Chebyshev polynomial U_n(x) of second kind
- [bernoulli_number()](#bernoulli_number) - Bernoulli number B_n
- [euler_number()](#euler_number) - Euler number E_n
- [bernoulli_polynomial()](#bernoulli_polynomial) - Bernoulli polynomial B_n(x)
- [euler_polynomial()](#euler_polynomial) - Euler polynomial E_n(x)
- [beta_function()](#beta_function) - Beta function B(a, b)
- [incomplete_gamma_lower()](#incomplete_gamma_lower) - Lower incomplete gamma function γ(a, x)
- [incomplete_beta_regularized()](#incomplete_beta_regularized) - Regularized incomplete beta I_x(a, b)
- [digamma()](#digamma) - Digamma function ψ(x) = d/dx ln Γ(x)
- [riemann_zeta()](#riemann_zeta) - Riemann zeta function ζ(s)
- [elliptic_k()](#elliptic_k) - Complete elliptic integral of the first kind K(k)
- [elliptic_e()](#elliptic_e) - Complete elliptic integral of the second kind E(k)
- [elliptic_f()](#elliptic_f) - Incomplete elliptic integral of the first kind F(φ, k)
- [elliptic_e_incomplete()](#elliptic_e_incomplete) - Incomplete elliptic integral of the second kind E(φ, k)
- [elliptic_pi()](#elliptic_pi) - Complete elliptic integral of the third kind Π(n, k)
- [hypergeometric_2f1()](#hypergeometric_2f1) - Gauss hypergeometric function ₂F₁(a, b; c; z)
- [hypergeometric_1f1()](#hypergeometric_1f1) - Confluent hypergeometric function ₁F₁(a; b; z)
- [airy_ai()](#airy_ai) - Airy function Ai(x)
- [airy_bi()](#airy_bi) - Airy function Bi(x)
- [spherical_bessel_j()](#spherical_bessel_j) - Spherical Bessel function j_n(x)
- [spherical_bessel_y()](#spherical_bessel_y) - Spherical Bessel function y_n(x)
- [spherical_harmonic_real()](#spherical_harmonic_real) - Real spherical harmonic Y_l^m(θ, φ)
- [bessel_j()](#bessel_j) - Bessel function of the first kind J_n(x)
- [bessel_y()](#bessel_y) - Bessel function of the second kind Y_n(x)
- [modified_bessel_i()](#modified_bessel_i) - Modified Bessel function I_n(x)
- [modified_bessel_k()](#modified_bessel_k) - Modified Bessel function K_n(x)
- [exponential_integral_ei()](#exponential_integral_ei) - Exponential integral Ei(x)
- [sine_integral()](#sine_integral) - Sine integral Si(x)
- [cosine_integral()](#cosine_integral) - Cosine integral Ci(x)
- [fresnel_s()](#fresnel_s) - Fresnel sine integral S(x)
- [fresnel_c()](#fresnel_c) - Fresnel cosine integral C(x)
- [dawson_function()](#dawson_function) - Dawson's function D(x)
- [polylogarithm()](#polylogarithm) - Polylogarithm Li_s(z)
- [dilogarithm()](#dilogarithm) - Dilogarithm Li_2(z)
- [upper_incomplete_gamma()](#upper_incomplete_gamma) - Upper incomplete gamma Γ(a,x)
- [hurwitz_zeta()](#hurwitz_zeta) - Hurwitz zeta function ζ(s,a)
- [rising_factorial()](#rising_factorial) - Rising factorial (Pochhammer) x^(n)
- [falling_factorial()](#falling_factorial) - Falling factorial x_(n)
- [subfactorial()](#subfactorial) - Subfactorial !n (derangements)
- [stirling_number_first()](#stirling_number_first) - Stirling number first kind |s(n,k)|
- [multinomial_coefficient()](#multinomial_coefficient) - Multinomial coefficient

### Integral Transforms
- [dft()](#dft) - Discrete Fourier Transform of sequence
- [idft()](#idft) - Inverse Discrete Fourier Transform
- [laplace_transform_numerical()](#laplace_transform_numerical) - Numerical Laplace transform L{f}(s)
- [inverse_laplace_gaver_stehfest()](#inverse_laplace_gaver_stehfest) - Inverse Laplace via Gaver–Stehfest
- [fourier_transform_numerical()](#fourier_transform_numerical) - Numerical Fourier transform F{f}(ω)
- [convolution()](#convolution) - Linear convolution of two real sequences
- [cross_correlation()](#cross_correlation) - Cross-correlation of two real sequences
- [auto_correlation()](#auto_correlation) - Auto-correlation of a sequence
- [z_transform_eval()](#z_transform_eval) - Z-transform evaluated at complex z
- [hilbert_transform()](#hilbert_transform) - Hilbert transform of a sequence

### Vector Analysis
- [scalar_triple_product()](#scalar_triple_product) - Scalar triple product a · (b × c)
- [vector_triple_product()](#vector_triple_product) - Vector triple product a × (b × c)
- [vector_projection()](#vector_projection) - Projection of vector a onto b
- [gradient_numerical()](#gradient_numerical) - Numerical gradient of scalar field
- [divergence_numerical()](#divergence_numerical) - Numerical divergence of vector field
- [curl_numerical()](#curl_numerical) - Numerical curl of 3D vector field
- [laplacian_numerical()](#laplacian_numerical) - Numerical Laplacian of scalar field
- [directional_derivative()](#directional_derivative) - Directional derivative of scalar field
- [jacobian_numerical()](#jacobian_numerical) - Numerical Jacobian matrix
- [hessian_numerical()](#hessian_numerical) - Numerical Hessian matrix
- [line_integral_numerical()](#line_integral_numerical) - Numerical line integral of scalar field

### Numerical Methods
- [trapezoidal_rule()](#trapezoidal_rule) - Numerical integration via trapezoidal rule
- [simpsons_rule()](#simpsons_rule) - Numerical integration via Simpson's 1/3 rule
- [simpsons_38_rule()](#simpsons_38_rule) - Numerical integration via Simpson's 3/8 rule
- [midpoint_rule()](#midpoint_rule) - Numerical integration via midpoint rule
- [gaussian_quadrature()](#gaussian_quadrature) - Gauss-Legendre quadrature (2-5 points)
- [romberg_integration()](#romberg_integration) - Romberg integration (Richardson extrapolation)
- [monte_carlo_integration()](#monte_carlo_integration) - Monte Carlo integration
- [forward_difference()](#forward_difference) - Forward difference derivative approximation
- [backward_difference()](#backward_difference) - Backward difference derivative approximation
- [central_difference()](#central_difference) - Central difference derivative O(h²)
- [second_derivative_central()](#second_derivative_central) - Second derivative via central differences
- [richardson_extrapolation()](#richardson_extrapolation) - Richardson extrapolation for derivatives
- [bisection_method()](#bisection_method) - Bisection root-finding method
- [newton_raphson()](#newton_raphson) - Newton-Raphson root-finding
- [secant_method()](#secant_method) - Secant root-finding method
- [regula_falsi()](#regula_falsi) - False position root-finding
- [fixed_point_iteration()](#fixed_point_iteration) - Fixed-point iteration x = g(x)
- [euler_method()](#euler_method) - Euler's method for ODE y' = f(t,y)
- [runge_kutta_2()](#runge_kutta_2) - 2nd-order Runge-Kutta (midpoint)
- [runge_kutta_4()](#runge_kutta_4) - Classic 4th-order Runge-Kutta
- [adaptive_rk45()](#adaptive_rk45) - Adaptive Runge-Kutta-Fehlberg (RK45)
- [ode_system_rk4()](#ode_system_rk4) - RK4 for systems of ODEs

### Curves & Curvature
- [cycloid()](#cycloid) - Cycloid coordinates at parameter t
- [epicycloid()](#epicycloid) - Epicycloid coordinates at parameter t
- [hypocycloid()](#hypocycloid) - Hypocycloid coordinates at parameter t
- [cardioid()](#cardioid) - Cardioid coordinates at parameter t
- [lemniscate()](#lemniscate) - Lemniscate of Bernoulli coordinates
- [archimedean_spiral()](#archimedean_spiral) - Archimedean spiral coordinates
- [logarithmic_spiral()](#logarithmic_spiral) - Logarithmic spiral coordinates
- [involute_of_circle()](#involute_of_circle) - Involute of a circle coordinates
- [rose_curve()](#rose_curve) - Rose (rhodonea) curve coordinates
- [astroid()](#astroid) - Astroid coordinates
- [curvature_explicit()](#curvature_explicit) - Curvature κ of y = f(x)
- [curvature_parametric()](#curvature_parametric) - Curvature of parametric curve
- [curvature_polar()](#curvature_polar) - Curvature of polar curve r = f(θ)
- [radius_of_curvature()](#radius_of_curvature) - Radius of curvature R = 1/κ
- [arc_length_parametric()](#arc_length_parametric) - Arc length of parametric curve
- [arc_length_polar()](#arc_length_polar) - Arc length of polar curve
- [arc_length_function()](#arc_length_function) - Arc length of y = f(x)
- [cycloid_arc_length()](#cycloid_arc_length) - Arc length of one cycloid arch (8r)
- [catenary()](#catenary) - Catenary curve y = a·cosh(x/a)
- [tractrix()](#tractrix) - Tractrix coordinates
- [cissoid()](#cissoid) - Cissoid of Diocles coordinates
- [strophoid()](#strophoid) - Right strophoid coordinates
- [witch_of_agnesi()](#witch_of_agnesi) - Witch of Agnesi curve
- [folium_of_descartes()](#folium_of_descartes) - Folium of Descartes coordinates

### Financial Functions
- [future_value()](#future_value) - Calculates future value of investment with periodic payments
- [present_value()](#present_value) - Calculates present value of future payments series
- [pmt()](#pmt) - Calculates payment for loan with constant payments rate
- [nper()](#nper) - Calculates number of periods for investment with payments
- [rate()](#rate) - Calculates interest rate per period using iteration
- [irr()](#irr) - Calculates internal rate of return for cash flows
- [npv()](#npv) - Calculates net present value of investment cash flows
- [sln()](#sln) - Calculates straight-line depreciation of asset per period
- [db()](#db) - Calculates depreciation using fixed-declining balance method
- [mirr()](#mirr) - Calculates modified internal rate of return
- [xnpv()](#xnpv) - Calculates net present value with irregular dates
- [xirr()](#xirr) - Calculates internal rate of return with irregular dates
- [ipmt()](#ipmt) - Calculates interest portion of a payment
- [ppmt()](#ppmt) - Calculates principal portion of a payment
- [cumipmt()](#cumipmt) - Calculates cumulative interest between periods
- [cumprinc()](#cumprinc) - Calculates cumulative principal between periods
- [effect()](#effect) - Calculates effective annual interest rate
- [nominal()](#nominal) - Calculates nominal annual interest rate
- [ddb()](#ddb) - Calculates double-declining balance depreciation
- [syd()](#syd) - Calculates sum-of-years' digits depreciation
- [fvschedule()](#fvschedule) - Calculates future value with variable rates
- [pduration()](#pduration) - Calculates periods to reach target value
- [simple_interest()](#simple_interest) - Calculates simple interest
- [compound_interest()](#compound_interest) - Calculates compound interest
- [roi()](#roi) - Calculates Return on Investment as a percentage
- [cagr()](#cagr) - Calculates the Compound Annual Growth Rate
- [break_even_units()](#break_even_units) - Calculates the break-even point in units
- [loan_amortization_table()](#loan_amortization_table) - Generates a loan amortization table with fixed payments
- [net_asset_value()](#net_asset_value) - Calculates Net Asset Value (NAV) per share
- [unlevered_beta()](#unlevered_beta) - Unlevered (asset) beta via Hamada equation
- [levered_beta()](#levered_beta) - Levered (equity) beta via inverse Hamada
- [bond_current_yield()](#bond_current_yield) - Current yield of a bond
- [cost_of_debt_after_tax()](#cost_of_debt_after_tax) - After-tax cost of debt
- [modified_dietz_return()](#modified_dietz_return) - Modified Dietz time-weighted return
- [omega_ratio()](#omega_ratio) - Omega ratio (gain vs loss weighted)
- [ulcer_index()](#ulcer_index) - Ulcer Index (drawdown severity measure)
- [effective_duration()](#effective_duration) - Effective bond duration
- [convexity_adjustment()](#convexity_adjustment) - Convexity adjustment for price change

---

## Function Index

**A**
- [add_bool_to_int()](#add_bool_to_int) - Adds boolean value to integer treating True=1
- [add_with_exact_precision()](#add_with_exact_precision) - Adds two numbers using Decimal for exact precision
- [arccosine()](#arccosine) - Calculates inverse cosine in radians from value
- [arcsine()](#arcsine) - Calculates inverse sine in radians from value
- [arctangent()](#arctangent) - Calculates inverse tangent in radians from value
- [arctangent2()](#arctangent2) - Calculates inverse tangent of y/x considering quadrant

**B**
- [base_to_decimal()](#base_to_decimal) - Base 2–36 string to decimal integer (DECIMAL)
- [bin_to_hex()](#bin_to_hex) - Binary to hexadecimal (BIN2HEX)
- [bin_to_int()](#bin_to_int) - Converts binary string to decimal integer
- [bin_to_oct()](#bin_to_oct) - Binary to octal (BIN2OCT)
- [bit_count()](#bit_count) - Count set bits / population count (BITCOUNT)
- [bitwise_and()](#bitwise_and) - Bitwise AND (BITAND)
- [bitwise_not()](#bitwise_not) - Bitwise NOT (BITNOT)
- [bitwise_or()](#bitwise_or) - Bitwise OR (BITOR)
- [bitwise_xor()](#bitwise_xor) - Bitwise XOR (BITXOR)
- [bool_to_float()](#bool_to_float) - Converts boolean to float
- [bool_to_float()](#bool_to_float) - Converts boolean to float, True=1.0 False=0.0
- [bool_to_int()](#bool_to_int) - Converts boolean to integer, True=1 False=0
- [break_even_units()](#break_even_units) - Calculates the break-even point in units

**C**
- [cagr()](#cagr) - Calculates the Compound Annual Growth Rate
- [calculate_covariance()](#calculate_covariance) - Calculates covariance between two lists sample or population
- [calculate_frecuency()](#calculate_frecuency) - Calculates frequency of each value in list
- [calculate_interquartile_range()](#calculate_interquartile_range) - Calculates IQR Q3 minus Q1 of list
- [calculate_mean()](#calculate_mean) - Calculates arithmetic mean average of list
- [calculate_median()](#calculate_median) - Calculates median middle value of list
- [calculate_mode()](#calculate_mode) - Calculates mode most frequent values in list
- [calculate_pearson_correlation()](#calculate_pearson_correlation) - Calculates Pearson correlation coefficient between two lists
- [calculate_percentile()](#calculate_percentile) - Calculates specified percentile value of list
- [calculate_range()](#calculate_range) - Calculates range difference between max and min
- [calculate_standard_deviation()](#calculate_standard_deviation) - Calculates standard deviation of list sample or population
- [calculate_variance()](#calculate_variance) - Calculates variance of list sample or population
- [clip_number()](#clip_number) - Forces number within specific minimum-maximum range
- [common_log()](#common_log) - Calculates common logarithm base 10 of a positive number
- [ceiling_significance()](#ceiling_significance) - Rounds up to significance multiple
- [chisq_dist()](#chisq_dist) - Chi-squared distribution CDF or PDF
- [chisq_inv()](#chisq_inv) - Inverse chi-squared distribution
- [combinations_with_repetition()](#combinations_with_repetition) - Combinations with repetition C(n+k-1, k)
- [collatz_length()](#collatz_length) - Counts steps in the Collatz sequence until reaching 1
- [compare_floats_with_tolerance()](#compare_floats_with_tolerance) - Compares floats within relative and absolute tolerance
- [compound_interest()](#compound_interest) - Calculates compound interest
- [confidence_norm()](#confidence_norm) - Normal confidence interval half-width
- [confidence_t()](#confidence_t) - Student-t confidence interval half-width
- [convert_string_to_float_with_locale()](#convert_string_to_float_with_locale) - Converts numeric string to float using locale separators
- [cosecant()](#cosecant) - Calculates cosecant of angle one over sine
- [cosine()](#cosine) - Calculates cosine of angle in radians
- [cotangent()](#cotangent) - Calculates cotangent of angle one over tangent
- [count_true_with_sum()](#count_true_with_sum) - Counts True values in boolean list using sum
- [covariance_matrix()](#covariance_matrix) - Sample covariance matrix for multiple variables
- [cube_root()](#cube_root) - Calculates cube root of a number
- [cumipmt()](#cumipmt) - Cumulative interest between periods
- [cumprinc()](#cumprinc) - Cumulative principal between periods

**D**
- [db()](#db) - Calculates depreciation using fixed-declining balance method
- [ddb()](#ddb) - Double-declining balance depreciation
- [dec_to_oct()](#dec_to_oct) - Decimal to octal (DEC2OCT)
- [degrees_to_radians()](#degrees_to_radians) - Converts angle from degrees to radians
- [delta()](#delta) - Kronecker delta, 1 if equal else 0 (DELTA)
- [deviation_squared()](#deviation_squared) - Sum of squared deviations
- [digital_root()](#digital_root) - Computes the digital root (repeated digit sum until single digit)
- [divisors()](#divisors) - Returns all positive divisors of n in ascending order

**E**
- [effect()](#effect) - Effective annual interest rate
- [even()](#even) - Round up to nearest even integer
- [expon_dist()](#expon_dist) - Exponential distribution CDF or PDF
- [exponential_moving_average()](#exponential_moving_average) - Exponential moving average (EMA)

**F**
- [f_dist()](#f_dist) - F-distribution CDF or PDF
- [f_inv()](#f_inv) - Inverse F-distribution
- [fibonacci()](#fibonacci) - Returns n-th Fibonacci number (0-indexed)
- [fibonacci_sequence()](#fibonacci_sequence) - Returns the first n Fibonacci numbers
- [fisher()](#fisher) - Fisher transformation
- [fisher_inv()](#fisher_inv) - Inverse Fisher transformation
- [float_to_int_truncated()](#float_to_int_truncated) - Converts float to integer truncating decimals towards zero
- [floor_division()](#floor_division) - Performs integer division truncating result downwards
- [floor_significance()](#floor_significance) - Rounds down to significance multiple
- [force_float_division()](#force_float_division) - Performs division ensuring float result always
- [forecast_linear()](#forecast_linear) - Predicts Y for X using linear regression
- [format_as_percentage()](#format_as_percentage) - Formats float as percentage string with decimals
- [format_as_scientific_notation()](#format_as_scientific_notation) - Formats float in scientific notation
- [format_with_leading_zeros()](#format_with_leading_zeros) - Formats integer with leading zeros to width
- [frequency_bins()](#frequency_bins) - Frequency distribution into bins
- [future_value()](#future_value) - Calculates future value of investment with periodic payments
- [fvschedule()](#fvschedule) - Future value with variable rates

**G**
- [geometric_mean()](#geometric_mean) - Geometric mean of positive numbers
- [get_primes_up_to()](#get_primes_up_to) - Generates list of primes up to limit using sieve
- [gestep()](#gestep) - Heaviside step, 1 if number >= step else 0 (GESTEP)
- [gauss()](#gauss) - P(0 < Z < z) for standard normal (GAUSS)

**H**
- [harmonic_mean()](#harmonic_mean) - Harmonic mean of positive numbers
- [hex_to_bin()](#hex_to_bin) - Hexadecimal to binary (HEX2BIN)
- [hex_to_int()](#hex_to_int) - Converts hexadecimal string to decimal integer
- [hex_to_oct()](#hex_to_oct) - Hexadecimal to octal (HEX2OCT)
- [hyperbolic_cosine()](#hyperbolic_cosine) - Calculates hyperbolic cosine of value
- [hyperbolic_sine()](#hyperbolic_sine) - Calculates hyperbolic sine of value
- [hyperbolic_tangent()](#hyperbolic_tangent) - Calculates hyperbolic tangent of value
- [hypotenuse()](#hypotenuse) - Calculates Euclidean norm length of right triangle hypotenuse

**I**
- [identity_matrix()](#identity_matrix) - Identity matrix of size n (MUNIT)
- [int_to_binary_clean()](#int_to_binary_clean) - Converts integer to binary string without prefix
- [int_to_binary_with_prefix()](#int_to_binary_with_prefix) - Converts integer to binary string with 0b prefix
- [int_to_float()](#int_to_float) - Converts integer to floating-point number
- [int_to_hex_clean()](#int_to_hex_clean) - Converts integer to hexadecimal string without prefix
- [int_to_hex_with_prefix()](#int_to_hex_with_prefix) - Converts integer to hexadecimal string with 0x prefix
- [int_to_octal_with_prefix()](#int_to_octal_with_prefix) - Converts integer to octal string with 0o prefix
- [inverse_cosecant()](#inverse_cosecant) - Calculates inverse cosecant arccosec in radians
- [inverse_cotangent()](#inverse_cotangent) - Calculates inverse cotangent arccotan in radians
- [inverse_hyperbolic_cosecant()](#inverse_hyperbolic_cosecant) - Calculates inverse hyperbolic cosecant arccosech of value
- [inverse_hyperbolic_cosine()](#inverse_hyperbolic_cosine) - Calculates inverse hyperbolic cosine arccosh of value
- [inverse_hyperbolic_cotangent()](#inverse_hyperbolic_cotangent) - Calculates inverse hyperbolic cotangent arccotanh of value
- [inverse_hyperbolic_secant()](#inverse_hyperbolic_secant) - Calculates inverse hyperbolic secant arcsech of value
- [inverse_hyperbolic_sine()](#inverse_hyperbolic_sine) - Calculates inverse hyperbolic sine arcsinh of value
- [inverse_hyperbolic_tangent()](#inverse_hyperbolic_tangent) - Calculates inverse hyperbolic tangent arctanh of value
- [inverse_secant()](#inverse_secant) - Calculates inverse secant arcsec in radians
- [ipmt()](#ipmt) - Interest portion of a payment
- [irr()](#irr) - Calculates internal rate of return for cash flows
- [is_numeric_type()](#is_numeric_type) - Verifies if value is numeric type
- [is_perfect_number()](#is_perfect_number) - Checks whether n is a perfect number
- [is_prime()](#is_prime) - Verifies if number is prime
- [is_even()](#is_even) - True if integer is even (ISEVEN)
- [is_odd()](#is_odd) - True if integer is odd (ISODD)

**J**

**K**
- [kurtosis()](#kurtosis) - Kurtosis (peakedness) of distribution

**L**
- [large()](#large) - K-th largest value in dataset
- [linear_interpolation()](#linear_interpolation) - Piecewise linear interpolation and extrapolation
- [loan_amortization_table()](#loan_amortization_table) - Generates a loan amortization table with fixed payments
- [log1p()](#log1p) - Calculates natural logarithm of 1+x with high precision near zero
- [log_base_n()](#log_base_n) - Calculates logarithm of a number to specified base N

**M**
- [manual_round_and_cast()](#manual_round_and_cast) - Performs manual rounding to nearest integer then casts
- [manual_round_down_to_int()](#manual_round_down_to_int) - Rounds float to nearest integer always downwards
- [manual_round_up_to_int()](#manual_round_up_to_int) - Rounds float to nearest integer always upwards
- [map_range()](#map_range) - Maps value from one numeric range to another
- [matrix_determinant()](#matrix_determinant) - Determinant of a square matrix (MDETERM)
- [matrix_inverse()](#matrix_inverse) - Inverse of a square matrix (MINVERSE)
- [matrix_multiply()](#matrix_multiply) - Matrix multiplication A × B (MMULT)
- [mirr()](#mirr) - Modified internal rate of return
- [modulo()](#modulo) - Remainder of division (MOD)

**N**
- [natural_log()](#natural_log) - Calculates natural logarithm base e of a positive number
- [nominal()](#nominal) - Nominal annual interest rate
- [norm_dist()](#norm_dist) - Normal distribution CDF or PDF
- [norm_inv()](#norm_inv) - Inverse normal distribution
- [norm_s_dist()](#norm_s_dist) - Standard normal distribution
- [norm_s_inv()](#norm_s_inv) - Inverse standard normal distribution
- [normalize_list()](#normalize_list) - Min-max normalization to [0, 1] range
- [normalize_to_0_1_range()](#normalize_to_0_1_range) - Normalizes number to scale within 0-1 range
- [nper()](#nper) - Calculates number of periods for investment with payments
- [npv()](#npv) - Calculates net present value of investment cash flows
- [nth_root()](#nth_root) - Calculates nth root of a number
- [number_to_bool()](#number_to_bool) - Converts number to boolean, zero becomes False
- [number_to_base()](#number_to_base) - Decimal to base 2–36 string (BASE)
- [number_to_complex()](#number_to_complex) - Converts number to complex with zero imaginary part
- [number_to_string()](#number_to_string) - Converts integer or float to string representation
- [oct_to_bin()](#oct_to_bin) - Octal to binary (OCT2BIN)
- [oct_to_hex()](#oct_to_hex) - Octal to hexadecimal (OCT2HEX)

**O**
- [octal_to_int()](#octal_to_int) - Converts octal string to decimal integer
- [odd()](#odd) - Round up to nearest odd integer
- [outliers_iqr()](#outliers_iqr) - Detect outliers using IQR fences method

**P**
- [pct_change()](#pct_change) - Percentage change between consecutive elements
- [pduration()](#pduration) - Periods to reach target investment value
- [percent_change()](#percent_change) - Percentage change between two values
- [percent_of()](#percent_of) - What percentage part is of whole
- [permutations_with_repetition()](#permutations_with_repetition) - Permutations with repetition n^k (PERMUTATIONA)
- [phi()](#phi) - Standard normal PDF φ(x) (PHI)
- [pmt()](#pmt) - Calculates payment for loan with constant payments rate
- [poisson_dist()](#poisson_dist) - Poisson distribution PMF or CDF
- [power()](#power) - Calculates value of base raised to specified exponent
- [ppmt()](#ppmt) - Principal portion of a payment
- [present_value()](#present_value) - Calculates present value of future payments series
- [prime_factors()](#prime_factors) - Returns the prime factorization of n in ascending order
- [product_list()](#product_list) - Product of all values in list
- [probability_range()](#probability_range) - Sum of probabilities in value range (PROB)

**Q**
- [quantize_number()](#quantize_number) - Quantizes number to discrete multiples of step

**R**
- [r_squared()](#r_squared) - Coefficient of determination R² for linear regression
- [radians_to_degrees()](#radians_to_degrees) - Converts angle from radians to degrees
- [random_array()](#random_array) - 2-D array of random numbers (RANDARRAY)
- [rate()](#rate) - Calculates interest rate per period using iteration
- [roi()](#roi) - Calculates Return on Investment as a percentage
- [rolling_std()](#rolling_std) - Rolling standard deviation over fixed window
- [rolling_median()](#rolling_median) - Rolling median over fixed window
- [reduce_to_modulo_range()](#reduce_to_modulo_range) - Converts value to cyclic range using modulo
- [round_down()](#round_down) - Rounds float downward to nearest integer floor
- [round_float_to_int()](#round_float_to_int) - Rounds float to nearest integer
- [round_half_even()](#round_half_even) - Performs banker's rounding with ROUND_HALF_EVEN policy
- [round_to_n_decimals()](#round_to_n_decimals) - Rounds float to specific number of decimal places
- [round_to_nearest_multiple()](#round_to_nearest_multiple) - Rounds number to nearest multiple of base
- [round_up()](#round_up) - Rounds float upward to nearest integer ceiling

**S**
- [safe_convert_number()](#safe_convert_number) - Safely converts value to numeric type with fallback
- [safe_division_for_context()](#safe_division_for_context) - Performs division selecting float or integer based context
- [safe_sum_with_none()](#safe_sum_with_none) - Adds two numbers safely treating None as zero
- [scale_to_new_range()](#scale_to_new_range) - Scales number from original range to new range
- [secant()](#secant) - Calculates secant of angle one over cosine
- [simple_interest()](#simple_interest) - Calculates simple interest
- [sine()](#sine) - Calculates sine of angle in radians
- [skewness()](#skewness) - Skewness (asymmetry) of distribution
- [spearman_correlation()](#spearman_correlation) - Non-parametric rank correlation coefficient
- [standard_error()](#standard_error) - Standard error of the mean (SEM)
- [standard_error_estimate()](#standard_error_estimate) - Standard error of predicted y in regression (STEYX)
- [sln()](#sln) - Calculates straight-line depreciation of asset per period
- [slope()](#slope) - Slope of linear regression line
- [small()](#small) - K-th smallest value in dataset
- [sqrt_pi()](#sqrt_pi) - Square root of number times pi
- [square_root()](#square_root) - Calculates square root of a non-negative number
- [sum_list()](#sum_list) - Sum of all values in list
- [sum_of_divisors()](#sum_of_divisors) - Returns the sum of proper divisors of n
- [sum_of_squares()](#sum_of_squares) - Calculates sum of squares of list values
- [sum_x2my2()](#sum_x2my2) - Sum of xᵢ²-yᵢ² for paired arrays (SUMX2MY2)
- [sum_x2py2()](#sum_x2py2) - Sum of xᵢ²+yᵢ² for paired arrays (SUMX2PY2)
- [sum_xmy2()](#sum_xmy2) - Sum of (xᵢ-yᵢ)² for paired arrays (SUMXMY2)
- [syd()](#syd) - Sum-of-years' digits depreciation

**T**
- [t_dist()](#t_dist) - Student's t-distribution CDF or PDF
- [t_inv()](#t_inv) - Inverse Student's t-distribution
- [tangent()](#tangent) - Calculates tangent of angle in radians
- [to_js_safe_integer()](#to_js_safe_integer) - Converts number to JavaScript safe integer range
- [true_division()](#true_division) - Performs floating-point division always returning float
- [truncate_float()](#truncate_float) - Truncates float eliminating decimal part towards zero
- [trimmed_mean()](#trimmed_mean) - Mean after trimming percent from each end

**U**

**V**

**W**
- [weighted_mean()](#weighted_mean) - Weighted arithmetic mean
- [weighted_median()](#weighted_median) - Weighted median for robust central tendency
- [winsorize()](#winsorize) - Cap extreme values at percentile boundaries

**X**
- [xirr()](#xirr) - Internal rate of return with irregular dates
- [xnpv()](#xnpv) - Net present value with irregular dates

**X**

**Y**

**Z**

---

## Arithmetic Operations

### `natural_log()`

Calculates the natural logarithm (base e) of a number.

**Parameters:**
- `x` (float): The number for which to calculate the natural logarithm. Must be positive.

**Returns:**
- `float`: The natural logarithm of x.

**Example:**
```python
import math
from formulite.fxNumeric.arithmetic_functions import natural_log

natural_log(math.e)  # 1.0
round(natural_log(10), 10)  # 2.302585093
```

**Cost:** O(1)

---

### `common_log()`

Calculates the common logarithm (base 10) of a number.

**Parameters:**
- `x` (float): The number for which to calculate the common logarithm. Must be positive.

**Returns:**
- `float`: The common logarithm of x.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import common_log

common_log(10)  # 1.0
round(common_log(100), 10)  # 2.0
```

**Cost:** O(1)

---

### `log_base_n()`

Calculates the logarithm of a number to a specified base N.

**Parameters:**
- `x` (float): The number for which to calculate the logarithm. Must be positive.
- `base` (Union[int, float]): The base of the logarithm. Must be positive and not 1.

**Returns:**
- `float`: The logarithm of x to the given base.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import log_base_n

log_base_n(100, 10)  # 2.0
round(log_base_n(8, 2), 10)  # 3.0
```

**Cost:** O(1)

---

### `log1p()`

Calculates the natural logarithm of (1 + x) with high precision for values close to zero.

**Parameters:**
- `x` (float): The number for which to calculate log(1 + x). Must be greater than -1.

**Returns:**
- `float`: The natural logarithm of (1 + x).

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import log1p

round(log1p(0), 10)  # 0.0
small_x = 1e-9
round(log1p(small_x), 15)  # 0.000000001000000
```

**Cost:** O(1)

---

### `power()`

Calculates the value of a base raised to a specified exponent (base^exponent).

**Parameters:**
- `base` (Union[int, float]): The base number.
- `exponent` (Union[int, float]): The exponent to which the base is raised.

**Returns:**
- `float`: The result of base raised to the power of exponent.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import power

power(2, 3)  # 8.0
power(9, 0.5)  # 3.0 (square root)
power(-2, 3)  # -8.0
```

**Cost:** O(1)

---

### `square_root()`

Calculates the square root of a non-negative number.

**Parameters:**
- `x` (Union[int, float]): The number for which to calculate the square root. Must be non-negative.

**Returns:**
- `float`: The square root of x.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import square_root

square_root(9)  # 3.0
square_root(25.0)  # 5.0
```

**Cost:** O(1)

---

### `cube_root()`

Calculates the cube root of a number.

**Parameters:**
- `x` (Union[int, float]): The number for which to calculate the cube root.

**Returns:**
- `float`: The cube root of x.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import cube_root

cube_root(8)  # 2.0
cube_root(27)  # 3.0
cube_root(-8)  # -2.0
```

**Cost:** O(1)

---

### `nth_root()`

Calculates the nth root of a number (x^(1/n)).

**Parameters:**
- `x` (Union[int, float]): The number for which to calculate the root.
- `n` (Union[int, float]): The degree of the root. Must be non-zero.

**Returns:**
- `float`: The nth root of x.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import nth_root

nth_root(81, 4)  # 3.0 (fourth root)
nth_root(1000, 3)  # 10.0 (cube root)
nth_root(-27, 3)  # -3.0
```

**Cost:** O(1)

---

## Numeric Conversions

### `float_to_int_truncated()`

Converts a floating-point number to an integer, truncating the decimals (towards zero).

**Parameters:**
- `number` (float): The floating-point number to convert.

**Returns:**
- `int`: The resulting integer without the decimal part.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import float_to_int_truncated

float_to_int_truncated(3.9)  # 3
float_to_int_truncated(-3.9)  # -3
```

**Cost:** O(1)

---

### `int_to_float()`

Converts an integer to a floating-point number.

**Parameters:**
- `number` (int): The integer to convert.

**Returns:**
- `float`: The resulting decimal number.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import int_to_float

int_to_float(5)  # 5.0
int_to_float(-10)  # -10.0
```

**Cost:** O(1)

---

### `number_to_complex()`

Converts an integer or float to a complex number with zero imaginary part.

**Parameters:**
- `number` (Union[int, float]): The number to convert.

**Returns:**
- `complex`: The resulting complex number.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import number_to_complex

number_to_complex(4.2)  # (4.2+0j)
number_to_complex(7)  # (7+0j)
```

**Cost:** O(1)

---

### `number_to_bool()`

Converts an integer or float to a boolean value.

**Parameters:**
- `number` (Union[int, float]): The number to convert.

**Returns:**
- `bool`: The resulting boolean value. 0 or 0.0 becomes False; any other number becomes True.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import number_to_bool

number_to_bool(0)  # False
number_to_bool(3.5)  # True
number_to_bool(-1)  # True
```

**Cost:** O(1)

---

### `bool_to_int()`

Converts a boolean value to an integer.

**Parameters:**
- `value` (bool): The boolean value to convert.

**Returns:**
- `int`: The resulting integer. True becomes 1; False becomes 0.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import bool_to_int

bool_to_int(True)  # 1
bool_to_int(False)  # 0
```

**Cost:** O(1)

---

### `bool_to_float()`

Converts a boolean value to a floating-point number.

**Parameters:**
- `value` (bool): The boolean value to convert.

**Returns:**
- `float`: The resulting decimal number. True becomes 1.0; False becomes 0.0.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import bool_to_float

bool_to_float(True)  # 1.0
bool_to_float(False)  # 0.0
```

**Cost:** O(1)

---

### `number_to_string()`

Converts an integer or float to its string representation.

**Parameters:**
- `number` (Union[int, float]): The number to convert.

**Returns:**
- `str`: The resulting text string.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import number_to_string

number_to_string(3.14)  # '3.14'
number_to_string(100)  # '100'
```

**Cost:** O(1)

---

### `round_float_to_int()`

Rounds a floating-point number to the nearest integer.

**Parameters:**
- `number` (float): The floating-point number to round.

**Returns:**
- `int`: The nearest integer to the given number.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import round_float_to_int

round_float_to_int(3.6)  # 4
round_float_to_int(3.2)  # 3
round_float_to_int(3.5)  # 4 (rounds to even)
```

**Cost:** O(1)

---

### `hex_to_int()`

Converts a hexadecimal string to an integer.

**Parameters:**
- `hex_string` (str): The hexadecimal string (may have '0x' prefix).

**Returns:**
- `int`: The decimal integer number.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import hex_to_int

hex_to_int("0xff")  # 255
hex_to_int("FF")  # 255
hex_to_int("a")  # 10
```

**Cost:** O(n) where n is the length of the string

---

### `bin_to_int()`

Converts a binary string to an integer.

**Parameters:**
- `bin_string` (str): The binary string (may have '0b' prefix).

**Returns:**
- `int`: The decimal integer number.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import bin_to_int

bin_to_int("0b1010")  # 10
bin_to_int("111")  # 7
```

**Cost:** O(n) where n is the length of the string

---

### `octal_to_int()`

Converts an octal string to an integer.

**Parameters:**
- `octal_string` (str): The octal string (may have '0o' prefix).

**Returns:**
- `int`: The decimal integer number.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import octal_to_int

octal_to_int("0o17")  # 15
octal_to_int("77")  # 63
```

**Cost:** O(n) where n is the length of the string

---

### `int_to_binary_clean()`

Converts an integer to its binary representation as a string, without the '0b' prefix.

**Parameters:**
- `number` (int): The integer to convert.

**Returns:**
- `str`: The binary string.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import int_to_binary_clean

int_to_binary_clean(10)  # '1010'
int_to_binary_clean(5)  # '101'
```

**Cost:** O(log n) where n is the number

---

### `int_to_hex_clean()`

Converts an integer to its hexadecimal representation as a string, without the '0x' prefix.

**Parameters:**
- `number` (int): The integer to convert.

**Returns:**
- `str`: The hexadecimal string (lowercase).

**Example:**
```python
from formulite.fxNumeric.conversion_functions import int_to_hex_clean

int_to_hex_clean(255)  # 'ff'
int_to_hex_clean(10)  # 'a'
```

**Cost:** O(log n) where n is the number

---

### `int_to_binary_with_prefix()`

Converts an integer to its binary representation as a string, including the '0b' prefix.

**Parameters:**
- `number` (int): The integer to convert.

**Returns:**
- `str`: The binary string with prefix.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import int_to_binary_with_prefix

int_to_binary_with_prefix(255)  # '0b11111111'
int_to_binary_with_prefix(10)  # '0b1010'
```

**Cost:** O(log n) where n is the number

---

### `int_to_hex_with_prefix()`

Converts an integer to its hexadecimal representation as a string, including the '0x' prefix.

**Parameters:**
- `number` (int): The integer to convert.

**Returns:**
- `str`: The hexadecimal string with prefix (lowercase).

**Example:**
```python
from formulite.fxNumeric.conversion_functions import int_to_hex_with_prefix

int_to_hex_with_prefix(255)  # '0xff'
int_to_hex_with_prefix(10)  # '0xa'
```

**Cost:** O(log n) where n is the number

---

### `int_to_octal_with_prefix()`

Converts an integer to its octal representation as a string, including the '0o' prefix.

**Parameters:**
- `number` (int): The integer to convert.

**Returns:**
- `str`: The octal string with prefix.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import int_to_octal_with_prefix

int_to_octal_with_prefix(255)  # '0o377'
int_to_octal_with_prefix(15)  # '0o17'
```

**Cost:** O(log n) where n is the number

---

### `to_js_safe_integer()`

Converts a number to a safe integer for JavaScript.

**Parameters:**
- `number` (Union[int, float]): The number to convert.

**Returns:**
- `Union[int, str]`: The number as an int if within JavaScript's safe range, or as a string if it exceeds that range.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import to_js_safe_integer

to_js_safe_integer(100)  # 100
to_js_safe_integer(9007199254740992)  # '9007199254740992'
```

**Cost:** O(1)

---

### `safe_convert_number()`

Safely converts an input value to a numeric type (float or int), using a try-except pattern to handle errors and provide a fallback value.

**Parameters:**
- `value` (Any): The input value to attempt conversion.
- `default_value` (Union[int, float]): The value to return if conversion fails. Default is 0.
- `target_type` (type): The numeric type to convert to (int or float). Default is float.

**Returns:**
- `Union[int, float]`: The converted value or `default_value` if conversion fails.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import safe_convert_number

# Conversion to float
safe_convert_number("3.14")  # 3.14
safe_convert_number("10")  # 10.0
safe_convert_number("abc")  # 0.0
safe_convert_number("hello", default_value=-1.0)  # -1.0

# Conversion to int
safe_convert_number("5", target_type=int)  # 5
safe_convert_number("7.8", target_type=int)  # 7
safe_convert_number("not_a_num", default_value=99, target_type=int)  # 99
```

**Cost:** O(1)

---

### `convert_string_to_float_with_locale()`

Converts a numeric string to a float, interpreting decimal and thousands separators according to a specific locale.

**Parameters:**
- `number_string` (str): The numeric string.
- `target_locale` (Optional[str]): Locale configuration (e.g., 'es_ES').

**Returns:**
- `float`: The floating-point number.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import convert_string_to_float_with_locale

convert_string_to_float_with_locale("1.234,56", "de_DE")  # 1234.56
```

**Cost:** O(n) where n is the length of the string

---

## Numeric Operations

### `is_numeric_type()`

Verifies if a value is of numeric type.

**Parameters:**
- `value` (Any): The value to verify.

**Returns:**
- `bool`: True if the value is numeric (int, float, Decimal), False otherwise.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import is_numeric_type

is_numeric_type(42)  # True
is_numeric_type(3.14)  # True
is_numeric_type("123")  # False
```

**Cost:** O(1)

---

### `is_prime()`

Verifies if a number is prime.

**Parameters:**
- `n` (int): The number to verify.

**Returns:**
- `bool`: True if the number is prime, False otherwise.

**Example:**
```python
from formulite.fxNumeric.number_theory_functions import is_prime

is_prime(7)  # True
is_prime(4)  # False
is_prime(2)  # True
```

**Cost:** O(√n)

---

### `get_primes_up_to()`

Generates a list of prime numbers up to a given limit using the Sieve of Eratosthenes algorithm.

**Parameters:**
- `limit` (int): The upper limit for prime search.

**Returns:**
- `list[int]`: List of prime numbers found.

**Example:**
```python
from formulite.fxNumeric.number_theory_functions import get_primes_up_to

get_primes_up_to(10)  # [2, 3, 5, 7]
get_primes_up_to(20)  # [2, 3, 5, 7, 11, 13, 17, 19]
```

**Cost:** O(n log log n) where n is the limit

---

### `truncate_float()`

Truncates a floating-point number, eliminating the decimal part.

**Parameters:**
- `number` (float): The floating-point number to truncate.

**Returns:**
- `int`: The resulting integer with decimals removed (truncated towards zero).

**Example:**
```python
from formulite.fxNumeric.rounding_functions import truncate_float

truncate_float(3.9)  # 3
truncate_float(-3.9)  # -3
```

**Cost:** O(1)

---

### `round_to_n_decimals()`

Rounds a floating-point number to a specific number of decimals.

**Parameters:**
- `number` (float): The floating-point number to round.
- `decimals` (int): The number of decimal places to round to.

**Returns:**
- `float`: The rounded number.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import round_to_n_decimals

round_to_n_decimals(3.14159, 2)  # 3.14
round_to_n_decimals(123.4567, 1)  # 123.5
```

**Cost:** O(1)

---

### `round_up()`

Rounds a floating-point number always upward to the nearest integer.

**Parameters:**
- `number` (float): The floating-point number to round up.

**Returns:**
- `int`: The smallest integer that is greater than or equal to 'number'.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import round_up

round_up(3.1)  # 4
round_up(3.9)  # 4
round_up(-3.1)  # -3
```

**Cost:** O(1)

---

### `round_down()`

Rounds a floating-point number always downward to the nearest integer.

**Parameters:**
- `number` (float): The floating-point number to round down.

**Returns:**
- `int`: The largest integer that is less than or equal to 'number'.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import round_down

round_down(3.9)  # 3
round_down(3.1)  # 3
round_down(-3.9)  # -4
```

**Cost:** O(1)

---

### `manual_round_and_cast()`

Performs manual rounding to the nearest integer and then casts to int.

**Parameters:**
- `number` (float): The floating-point number to round and cast.

**Returns:**
- `int`: The resulting integer from manual rounding.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import manual_round_and_cast

manual_round_and_cast(3.6)  # 4
manual_round_and_cast(3.2)  # 3
manual_round_and_cast(3.5)  # 4  # Always rounds up for .5
manual_round_and_cast(2.5)  # 3
manual_round_and_cast(-3.6)  # -4
manual_round_and_cast(-3.5)  # -4
```

**Cost:** O(1)

---

### `manual_round_up_to_int()`

Rounds a floating-point number to the nearest integer, always upwards.

**Parameters:**
- `number` (float): The floating-point number to round.

**Returns:**
- `int`: The resulting integer, always rounded upwards.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import manual_round_up_to_int

manual_round_up_to_int(3.1)  # 4
manual_round_up_to_int(3.9)  # 4
manual_round_up_to_int(3.0)  # 3
manual_round_up_to_int(-3.1)  # -3
manual_round_up_to_int(-3.9)  # -3
```

**Cost:** O(1)

---

### `manual_round_down_to_int()`

Rounds a floating-point number to the nearest integer, always downwards.

**Parameters:**
- `number` (float): The floating-point number to round.

**Returns:**
- `int`: The resulting integer, always rounded downwards.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import manual_round_down_to_int

manual_round_down_to_int(3.9)  # 3
manual_round_down_to_int(3.1)  # 3
manual_round_down_to_int(3.0)  # 3
manual_round_down_to_int(-3.1)  # -4
manual_round_down_to_int(-3.9)  # -4
```

**Cost:** O(1)

---

### `round_half_even()`

Performs banker's rounding (ROUND_HALF_EVEN) of a number to a specific precision.

**Parameters:**
- `number` (Union[float, str, Decimal]): The number to round.
- `target_precision` (str): The desired precision (e.g., "1" for integer, "0.1" for one decimal, "0.01" for two decimals). Default is "1".

**Returns:**
- `Decimal`: The rounded number with the specified precision and ROUND_HALF_EVEN policy.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import round_half_even
from decimal import Decimal

round_half_even(Decimal("2.5"))  # Decimal('2')  # 2.5 -> 2 (2 is even)
round_half_even(Decimal("3.5"))  # Decimal('4')  # 3.5 -> 4 (4 is even)
round_half_even(Decimal("2.25"), "0.1")  # Decimal('2.2')
round_half_even(Decimal("2.35"), "0.1")  # Decimal('2.4')
round_half_even("2.5")  # Decimal('2')
round_half_even("3.5")  # Decimal('4')
```

**Cost:** O(1)

---

### `round_to_nearest_multiple()`

Rounds a number to the nearest multiple of a given base.

**Parameters:**
- `number` (Union[int, float]): The number to round.
- `base` (Union[int, float]): The base or multiple to round to.

**Returns:**
- `Union[int, float]`: The number rounded to the nearest multiple of the base.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import round_to_nearest_multiple

round_to_nearest_multiple(7, 5)  # 5
round_to_nearest_multiple(8, 5)  # 10
round_to_nearest_multiple(10.25, 0.5)  # 10.5
round_to_nearest_multiple(23, 10)  # 20
round_to_nearest_multiple(25, 10)  # 20  # round half to even
round_to_nearest_multiple(35, 10)  # 40
```

**Cost:** O(1)

---

### `add_with_exact_precision()`

Adds two numbers using the Decimal type to avoid precision errors.

**Parameters:**
- `num1` (Union[float, str]): The first number.
- `num2` (Union[float, str]): The second number.

**Returns:**
- `Decimal`: The result of the sum with exact decimal precision.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import add_with_exact_precision

add_with_exact_precision("0.1", "0.2")  # Decimal('0.3')
add_with_exact_precision(1.23, 4.56)  # Decimal('5.79')
```

**Cost:** O(1)

---

### `format_with_leading_zeros()`

Formats an integer as a string, padding with leading zeros up to a specific width.

**Parameters:**
- `number` (int): The integer to format.
- `width` (int): The total desired width of the resulting string.

**Returns:**
- `str`: The string of the number with leading zeros.

**Example:**
```python
from formulite.fxNumeric.format_functions import format_with_leading_zeros

format_with_leading_zeros(5, 3)  # '005'
format_with_leading_zeros(123, 5)  # '00123'
```

**Cost:** O(1)

---

### `format_as_percentage()`

Formats a floating-point number as a percentage string.

**Parameters:**
- `number` (float): The number to format (e.g., 0.1234).
- `decimals` (int): The number of decimal places to show in the percentage. Default is 2.

**Returns:**
- `str`: The formatted percentage string (e.g., "12.34%").

**Example:**
```python
from formulite.fxNumeric.format_functions import format_as_percentage

format_as_percentage(0.1234)  # '12.34%'
format_as_percentage(0.5, 0)  # '50%'
```

**Cost:** O(1)

---

### `format_as_scientific_notation()`

Formats a floating-point number in scientific notation.

**Parameters:**
- `number` (float): The number to format.
- `decimals` (int): The number of decimal places for the mantissa. Default is 2.

**Returns:**
- `str`: The string of the number in scientific notation (e.g., "1.23e+06").

**Example:**
```python
from formulite.fxNumeric.format_functions import format_as_scientific_notation

format_as_scientific_notation(1230000)  # '1.23e+06'
format_as_scientific_notation(0.0000000000456, 1)  # '4.6e-11'
```

**Cost:** O(1)

---

### `force_float_division()`

Performs a division ensuring the result is always a float, even if both operands are integers.

**Parameters:**
- `numerator` (Union[int, float]): The numerator.
- `denominator` (Union[int, float]): The denominator.

**Returns:**
- `float`: The result of the division as a floating-point number.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import force_float_division

force_float_division(5, 2)  # 2.5
force_float_division(10, 3)  # 3.3333333333333335
```

**Cost:** O(1)

---

### `round_half_even()`

Performs banker's rounding (ROUND_HALF_EVEN) to a specific precision.

**Parameters:**
- `number` (Union[float, str, Decimal]): The number to round.
- `target_precision` (str): The desired precision (e.g., "1" for integer, "0.1" for one decimal). Default is "1".

**Returns:**
- `Decimal`: The rounded number with the specified precision.

**Example:**
```python
from decimal import Decimal
from formulite.fxNumeric.rounding_functions import round_half_even

round_half_even(Decimal("2.5"))  # Decimal('2')
round_half_even(Decimal("3.5"))  # Decimal('4')
round_half_even(Decimal("2.25"), "0.1")  # Decimal('2.2')
```

**Cost:** O(1)

---

### `normalize_to_0_1_range()`

Normalizes a number to scale it to the [0, 1] range.

**Parameters:**
- `value` (Union[int, float]): The value to normalize.
- `min_value` (Union[int, float]): The minimum value of the original range.
- `max_value` (Union[int, float]): The maximum value of the original range.

**Returns:**
- `float`: The normalized value.

**Example:**
```python
from formulite.fxNumeric.interpolation_functions import normalize_to_0_1_range

normalize_to_0_1_range(50, 0, 100)  # 0.5
normalize_to_0_1_range(25, 0, 100)  # 0.25
```

**Cost:** O(1)

---

### `scale_to_new_range()`

Scales a number from an original range to a new range.

**Parameters:**
- `value` (Union[int, float]): The value to scale.
- `old_min` (Union[int, float]): Minimum value of the original range.
- `old_max` (Union[int, float]): Maximum value of the original range.
- `new_min` (Union[int, float]): Minimum value of the new range.
- `new_max` (Union[int, float]): Maximum value of the new range.

**Returns:**
- `float`: The scaled value.

**Example:**
```python
from formulite.fxNumeric.interpolation_functions import scale_to_new_range

scale_to_new_range(50, 0, 100, 0, 10)  # 5.0
scale_to_new_range(75, 0, 100, 0, 10)  # 7.5
```

**Cost:** O(1)

---

### `clip_number()`

Forces a number to be within a specific range.

**Parameters:**
- `value` (Union[int, float]): The number.
- `min_value` (Union[int, float]): Minimum allowed value.
- `max_value` (Union[int, float]): Maximum allowed value.

**Returns:**
- `Union[int, float]`: The number adjusted to the range.

**Example:**
```python
from formulite.fxNumeric.interpolation_functions import clip_number

clip_number(150, 0, 100)  # 100
clip_number(-10, 0, 100)  # 0
clip_number(50, 0, 100)  # 50
```

**Cost:** O(1)

---

### `reduce_to_modulo_range()`

Converts a value to a cyclic range using the modulo operation.

**Parameters:**
- `x` (Union[int, float]): The numeric value to reduce.
- `base` (Union[int, float]): The cycle base (the range size). Must be a positive number.

**Returns:**
- `Union[int, float]`: The value reduced to the cyclic range.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import reduce_to_modulo_range

reduce_to_modulo_range(25, 24)  # 1 (25 hours is 1 AM the next day)
reduce_to_modulo_range(370, 360)  # 10 (370 degrees is equivalent to 10 degrees)
reduce_to_modulo_range(-5, 10)  # 5
```

**Cost:** O(1)

---

### `quantize_number()`

Quantizes a number, forcing it to take only certain discrete values (multiples of 'step').

**Parameters:**
- `x` (Union[int, float]): The number to quantize.
- `step` (Union[int, float]): The increment size or "step" for quantization. Must be a positive number.

**Returns:**
- `Union[int, float]`: The number quantized to the nearest multiple of 'step'.

**Example:**
```python
from formulite.fxNumeric.rounding_functions import quantize_number

quantize_number(1.23, 0.25)  # 1.25
quantize_number(1.10, 0.25)  # 1.0
quantize_number(23, 10)  # 20
quantize_number(27, 10)  # 30
```

**Cost:** O(1)

---

### `add_bool_to_int()`

Adds a boolean value to an integer (True = 1, False = 0).

**Parameters:**
- `boolean_value` (bool): The boolean value (True or False).
- `int_value` (int): The integer to which the boolean will be added.

**Returns:**
- `int`: The result of the addition.

**Example:**
```python
from formulite.fxNumeric.conversion_functions import add_bool_to_int

add_bool_to_int(True, 2)  # 3
add_bool_to_int(False, 5)  # 5
add_bool_to_int(True, 0)  # 1
```

**Cost:** O(1)

---

### `safe_sum_with_none()`

Performs addition of two numbers, safely handling None values (treating None as 0).

**Parameters:**
- `num1` (Union[int, float, None]): The first number (or None).
- `num2` (Union[int, float, None]): The second number (or None).

**Returns:**
- `Union[int, float]`: The result of the addition.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import safe_sum_with_none

safe_sum_with_none(3, 5)  # 8
safe_sum_with_none(3, None)  # 3
safe_sum_with_none(None, 5)  # 5
safe_sum_with_none(None, None)  # 0
```

**Cost:** O(1)

---

### `count_true_with_sum()`

Counts the number of True values in a boolean list using the sum() function.

**Parameters:**
- `boolean_list` (List[bool]): A list containing True or False values.

**Returns:**
- `int`: The total number of True values in the list.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import count_true_with_sum

count_true_with_sum([True, False, True, True])  # 3
count_true_with_sum([False, False, False])  # 0
count_true_with_sum([True, False])  # 1
```

**Cost:** O(n)

---

### `true_division()`

Performs "true" (floating-point) division, always returning a floating-point number.

**Parameters:**
- `numerator` (Union[int, float]): The dividend.
- `denominator` (Union[int, float]): The divisor.

**Returns:**
- `float`: The division result as a float.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import true_division

true_division(5, 2)  # 2.5
true_division(10, 4)  # 2.5
true_division(6, 2)  # 3.0
```

**Cost:** O(1)

---

### `floor_division()`

Performs integer (floor) division, truncating the result downwards.

**Parameters:**
- `numerator` (Union[int, float]): The dividend.
- `denominator` (Union[int, float]): The divisor.

**Returns:**
- `Union[int, float]`: The integer part of the quotient.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import floor_division

floor_division(5, 2)  # 2
floor_division(10, 4)  # 2
floor_division(-5, 2)  # -3
```

**Cost:** O(1)

---

### `safe_division_for_context()`

Performs division selecting the appropriate operator based on context needs.

**Parameters:**
- `numerator` (Union[int, float]): The dividend.
- `denominator` (Union[int, float]): The divisor.
- `return_float` (bool): If True, performs floating-point division. If False, performs integer division. Default is True.

**Returns:**
- `Union[int, float]`: The division result, either a float or a truncated int/float.

**Example:**
```python
from formulite.fxNumeric.arithmetic_functions import safe_division_for_context

safe_division_for_context(5, 2, return_float=True)  # 2.5
safe_division_for_context(5, 2, return_float=False)  # 2
safe_division_for_context(10, 3, return_float=True)  # 3.3333333333333335
safe_division_for_context(10, 3, return_float=False)  # 3
```

**Cost:** O(1)

---

### `compare_floats_with_tolerance()`

Compares two floats to determine if they are "close" within a tolerance.

**Parameters:**
- `a` (float): First number.
- `b` (float): Second number.
- `rel_tol` (float): Relative tolerance. Default is 1e-9.
- `abs_tol` (float): Absolute tolerance. Default is 1e-5.

**Returns:**
- `bool`: True if they are close.

**Example:**
```python
from formulite.fxNumeric.format_functions import compare_floats_with_tolerance

compare_floats_with_tolerance(0.1 + 0.2, 0.3)  # True
compare_floats_with_tolerance(1.0000001, 1.0)  # True
```

**Cost:** O(1)

---

## Statistical Functions

### `calculate_frecuency()`

Calculates the frequency of each value in a list of numbers.

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values.

**Returns:**
- `dict`: A dictionary where keys are unique values and values are their frequencies.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_frecuency

calculate_frecuency([1, 2, 2, 3, 3, 3])  # {1: 1, 2: 2, 3: 3}
```

**Cost:** O(n) where n is the length of the list

---

### `calculate_mean()`

Calculates the arithmetic mean (average) of a list of numbers.

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values.

**Returns:**
- `float`: The arithmetic mean of the data.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_mean

calculate_mean([1, 2, 3, 4, 5])  # 3.0
calculate_mean([10, 20, 30])  # 20.0
```

**Cost:** O(n) where n is the length of the list

---

### `calculate_median()`

Calculates the median (middle value) of a list of numbers.

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values.

**Returns:**
- `Union[int, float]`: The median of the data.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_median

calculate_median([1, 2, 3, 4, 5])  # 3
calculate_median([1, 2, 3, 4])  # 2.5
```

**Cost:** O(n log n) due to sorting

---

### `calculate_mode()`

Calculates the mode(s) of a list of numbers.

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values.

**Returns:**
- `List[Union[int, float]]`: A list of mode(s). Returns an empty list if no mode.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_mode

calculate_mode([1, 2, 2, 3, 4])  # [2]
calculate_mode([1, 2, 2, 3, 3, 4])  # [2, 3]
```

**Cost:** O(n) where n is the length of the list

---

### `calculate_range()`

Calculates the range of a list of numbers (difference between maximum and minimum).

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values.

**Returns:**
- `float`: The range of the data.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_range

calculate_range([1, 5, 2, 8, 3])  # 7.0
calculate_range([10, 10, 10])  # 0.0
```

**Cost:** O(n) where n is the length of the list

---

### `calculate_variance()`

Calculates the variance of a list of numbers.

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values.
- `sample` (bool, optional): If True, calculates sample variance (divides by n-1). If False, calculates population variance (divides by n). Defaults to True.

**Returns:**
- `float`: The variance of the data.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_variance

calculate_variance([1, 2, 3, 4, 5])  # 2.5 (sample variance)
calculate_variance([1, 2, 3, 4, 5], sample=False)  # 2.0 (population variance)
```

**Cost:** O(n) where n is the length of the list

---

### `calculate_standard_deviation()`

Calculates the standard deviation of a list of numbers.

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values.
- `sample` (bool, optional): If True, calculates sample standard deviation. If False, calculates population standard deviation. Defaults to True.

**Returns:**
- `float`: The standard deviation of the data.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_standard_deviation

round(calculate_standard_deviation([1, 2, 3, 4, 5]), 2)  # 1.58 (sample std dev)
round(calculate_standard_deviation([1, 2, 3, 4, 5], sample=False), 2)  # 1.41 (population)
```

**Cost:** O(n) where n is the length of the list

---

### `calculate_interquartile_range()`

Calculates the Interquartile Range (IQR) of a list of numbers.

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values (minimum 4 elements).

**Returns:**
- `float`: The Interquartile Range (IQR = Q3 - Q1).

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_interquartile_range

calculate_interquartile_range([1, 2, 3, 4, 5, 6, 7, 8, 9])  # 4.0
calculate_interquartile_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])  # 5.0
```

**Cost:** O(n log n) due to sorting

---

### `calculate_covariance()`

Calculates the covariance between two lists of numbers.

**Parameters:**
- `data1` (List[Union[int, float]]): The first list of numeric values.
- `data2` (List[Union[int, float]]): The second list of numeric values.
- `sample` (bool, optional): If True, calculates sample covariance (divides by n-1). If False, calculates population covariance (divides by n). Defaults to True.

**Returns:**
- `float`: The covariance between the two datasets.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_covariance

calculate_covariance([1, 2, 3], [2, 4, 6])  # 2.0 (positive correlation)
calculate_covariance([1, 2, 3], [6, 4, 2])  # -2.0 (negative correlation)
```

**Cost:** O(n) where n is the length of the lists

---

### `calculate_pearson_correlation()`

Calculates the Pearson product-moment correlation coefficient between two lists of numbers.

**Parameters:**
- `data1` (List[Union[int, float]]): The first list of numeric values.
- `data2` (List[Union[int, float]]): The second list of numeric values.

**Returns:**
- `float`: The Pearson correlation coefficient (value ranges from -1 to 1).

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_pearson_correlation

calculate_pearson_correlation([1, 2, 3], [2, 4, 6])  # 1.0 (perfect positive)
calculate_pearson_correlation([1, 2, 3], [6, 4, 2])  # -1.0 (perfect negative)
```

**Cost:** O(n) where n is the length of the lists

---

### `calculate_percentile()`

Calculates the specified percentile of a list of numbers.

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values.
- `percentile` (float): The desired percentile, a value between 0 and 100.

**Returns:**
- `float`: The value at the specified percentile.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import calculate_percentile

calculate_percentile([10, 20, 30, 40, 50], 50)  # 30.0 (median)
calculate_percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 90)  # 9.0
```

**Cost:** O(n log n) due to sorting

---

### `sum_of_squares()`

Calculates the sum of squares of a list of numbers.

**Parameters:**
- `data` (List[Union[int, float]]): A list of numeric values.

**Returns:**
- `float`: The sum of squares.

**Example:**
```python
from formulite.fxNumeric.statistics_functions import sum_of_squares

sum_of_squares([1, 2, 3])  # 14.0 (1² + 2² + 3² = 1 + 4 + 9)
```

**Cost:** O(n) where n is the length of the list

---

## Trigonometric Functions

### `sine()`

Calculates the sine of an angle.

**Parameters:**
- `angle_radians` (float): The angle in radians.

**Returns:**
- `float`: The sine of the given angle.

**Example:**
```python
import math
from formulite.fxNumeric.trigonometry_functions import sine

sine(math.pi / 2)  # 1.0 (sin(90 degrees))
sine(0)  # 0.0
```

**Cost:** O(1)

---

### `cosine()`

Calculates the cosine of an angle.

**Parameters:**
- `angle_radians` (float): The angle in radians.

**Returns:**
- `float`: The cosine of the given angle.

**Example:**
```python
import math
from formulite.fxNumeric.trigonometry_functions import cosine

cosine(0)  # 1.0 (cos(0 degrees))
cosine(math.pi)  # -1.0 (cos(180 degrees))
```

**Cost:** O(1)

---

### `tangent()`

Calculates the tangent of an angle.

**Parameters:**
- `angle_radians` (float): The angle in radians.

**Returns:**
- `float`: The tangent of the given angle.

**Example:**
```python
import math
from formulite.fxNumeric.trigonometry_functions import tangent

tangent(0)  # 0.0
round(tangent(math.pi / 4), 10)  # 1.0 (tan(45 degrees))
```

**Cost:** O(1)

---

### `arcsine()`

Calculates the inverse sine (arcsine) of a value.

**Parameters:**
- `x` (float): The value whose arcsine is to be calculated. Must be in the range [-1, 1].

**Returns:**
- `float`: The arcsine of the given value in radians.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import arcsine

arcsine(1.0)  # 1.5707963267948966 (pi/2)
arcsine(0.0)  # 0.0
```

**Cost:** O(1)

---

### `arccosine()`

Calculates the inverse cosine (arccosine) of a value.

**Parameters:**
- `x` (float): The value whose arccosine is to be calculated. Must be in the range [-1, 1].

**Returns:**
- `float`: The arccosine of the given value in radians.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import arccosine

arccosine(1.0)  # 0.0
arccosine(-1.0)  # 3.141592653589793 (pi)
```

**Cost:** O(1)

---

### `fibonacci_sequence()`

Returns the first *n* Fibonacci numbers.

**Parameters:**
- `n` (int): How many numbers to generate (>= 0).

**Returns:**
- `list[int]`: A list with the first *n* Fibonacci numbers.

**Raises:**
- `ValueError`: If *n* is negative.

**Example:**
```python
from formulite.fxNumeric.number_theory_functions import fibonacci_sequence

fibonacci_sequence(7)  # [0, 1, 1, 2, 3, 5, 8]
```

**Cost:** O(n)

---

### `digital_root()`

Computes the digital root (repeated digit sum until single digit).

**Parameters:**
- `n` (int): A non-negative integer.

**Returns:**
- `int`: The single-digit result.

**Example:**
```python
from formulite.fxNumeric.number_theory_functions import digital_root

digital_root(493)  # 7
```

**Cost:** O(1)

---

### `divisors()`

Returns all positive divisors of *n* in ascending order.

**Parameters:**
- `n` (int): A positive integer.

**Returns:**
- `list[int]`: Sorted list of divisors.

**Raises:**
- `ValueError`: If *n* < 1.

**Example:**
```python
from formulite.fxNumeric.number_theory_functions import divisors

divisors(12)  # [1, 2, 3, 4, 6, 12]
```

**Cost:** O(√n)

---

### `prime_factors()`

Returns the prime factorization of *n* in ascending order.

**Parameters:**
- `n` (int): An integer >= 2.

**Returns:**
- `list[int]`: List of prime factors (with repetition).

**Raises:**
- `ValueError`: If *n* < 2.

**Example:**
```python
from formulite.fxNumeric.number_theory_functions import prime_factors

prime_factors(60)  # [2, 2, 3, 5]
```

**Cost:** O(√n)

---

### `sum_of_divisors()`

Returns the sum of proper divisors of *n* (excluding *n* itself).

**Parameters:**
- `n` (int): A positive integer.

**Returns:**
- `int`: Sum of divisors less than *n*.

**Example:**
```python
from formulite.fxNumeric.number_theory_functions import sum_of_divisors

sum_of_divisors(12)  # 16
```

**Cost:** O(√n)

---

### `is_perfect_number()`

Checks whether *n* is a perfect number (equal to the sum of its proper divisors).

**Parameters:**
- `n` (int): A positive integer.

**Returns:**
- `bool`: `True` if *n* is perfect.

**Example:**
```python
from formulite.fxNumeric.number_theory_functions import is_perfect_number

is_perfect_number(6)   # True
is_perfect_number(10)  # False
```

**Cost:** O(√n)

---

### `collatz_length()`

Counts the number of steps in the Collatz sequence until reaching 1.

**Parameters:**
- `n` (int): A positive integer.

**Returns:**
- `int`: Number of steps.

**Raises:**
- `ValueError`: If *n* < 1.

**Example:**
```python
from formulite.fxNumeric.number_theory_functions import collatz_length

collatz_length(6)  # 8
```

**Cost:** O(?) — conjectured to terminate for all n

---

### `simple_interest()`

Calculates simple interest.

**Parameters:**
- `principal` (float): The initial amount.
- `rate` (float): Annual interest rate (as decimal, e.g. 0.05 for 5%).
- `time_periods` (float): Number of periods (years).

**Returns:**
- `float`: The interest earned.

**Example:**
```python
from formulite.fxNumeric.finance_functions import simple_interest

simple_interest(1000, 0.05, 3)  # 150.0
```

**Cost:** O(1)

---

### `compound_interest()`

Calculates compound interest (total amount minus principal).

**Parameters:**
- `principal` (float): Initial amount.
- `rate` (float): Annual interest rate.
- `n` (int): Compounding periods per year.
- `t` (float): Number of years.

**Returns:**
- `float`: The interest earned (total − principal).

**Example:**
```python
from formulite.fxNumeric.finance_functions import compound_interest

compound_interest(1000, 0.05, 12, 1)  # 51.16
```

**Cost:** O(1)

---

### `roi()`

Calculates Return on Investment as a percentage.

**Parameters:**
- `gain` (float): Total return.
- `cost` (float): Total cost.

**Returns:**
- `float`: ROI percentage.

**Raises:**
- `ValueError`: If *cost* is zero.

**Example:**
```python
from formulite.fxNumeric.finance_functions import roi

roi(1500, 1000)  # 50.0
```

**Cost:** O(1)

---

### `cagr()`

Calculates the Compound Annual Growth Rate.

**Parameters:**
- `beginning` (float): Starting value.
- `ending` (float): Ending value.
- `years` (float): Number of years.

**Returns:**
- `float`: CAGR as a decimal.

**Raises:**
- `ValueError`: If *beginning* <= 0 or *years* <= 0.

**Example:**
```python
from formulite.fxNumeric.finance_functions import cagr

cagr(1000, 2000, 5)  # 0.1487
```

**Cost:** O(1)

---

### `break_even_units()`

Calculates the break-even point in units.

**Parameters:**
- `fixed_costs` (float): Total fixed costs.
- `price_per_unit` (float): Selling price per unit.
- `variable_cost_per_unit` (float): Variable cost per unit.

**Returns:**
- `float`: Number of units needed to break even.

**Raises:**
- `ValueError`: If price equals variable cost.

**Example:**
```python
from formulite.fxNumeric.finance_functions import break_even_units

break_even_units(10000, 50, 30)  # 500.0
```

**Cost:** O(1)

---

### `loan_amortization_table()`

Generates a loan amortization table with fixed payments.

**Parameters:**
- `principal` (float): Loan principal.
- `annual_rate` (float): Annual interest rate.
- `periods` (int): Monthly payment periods.

**Returns:**
- `list[dict]`: A list of dicts with keys `period`, `payment`, `interest`, `principal_paid` and `balance`.

**Raises:**
- `ValueError`: If *principal* <= 0, *annual_rate* < 0 or *periods* < 1.

**Example:**
```python
from formulite.fxNumeric.finance_functions import loan_amortization_table

table = loan_amortization_table(1200, 0.12, 3)
# [{'period': 1, 'payment': 408.49, 'interest': 12.0, ...}, ...]
```

**Cost:** O(periods)

**Cost:** O(1)

---

### `arctangent()`

Calculates the inverse tangent (arctangent) of a value.

**Parameters:**
- `x` (float): The value whose arctangent is to be calculated.

**Returns:**
- `float`: The arctangent of the given value in radians.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import arctangent

arctangent(1.0)  # 0.7853981633974483 (pi/4)
arctangent(0.0)  # 0.0
```

**Cost:** O(1)

---

### `arctangent2()`

Calculates the inverse tangent of y/x using the signs of both arguments to determine the correct quadrant.

**Parameters:**
- `y` (float): The y-coordinate.
- `x` (float): The x-coordinate.

**Returns:**
- `float`: The arctangent of y/x in radians, considering the quadrant.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import arctangent2

arctangent2(1, 1)  # 0.7853981633974483 (pi/4)
arctangent2(-1, 1)  # -0.7853981633974483 (-pi/4)
arctangent2(1, -1)  # 2.356194490192345 (3*pi/4)
```

**Cost:** O(1)

---

### `hypotenuse()`

Calculates the Euclidean norm, sqrt(x*x + y*y). This is the length of the hypotenuse of a right-angled triangle.

**Parameters:**
- `x` (float): The length of the first leg.
- `y` (float): The length of the second leg.

**Returns:**
- `float`: The length of the hypotenuse.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import hypotenuse

hypotenuse(3, 4)  # 5.0
hypotenuse(5, 12)  # 13.0
```

**Cost:** O(1)

---

### `hyperbolic_sine()`

Calculates the hyperbolic sine of a value.

**Parameters:**
- `x` (float): The value.

**Returns:**
- `float`: The hyperbolic sine of the given value.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import hyperbolic_sine

hyperbolic_sine(0)  # 0.0
round(hyperbolic_sine(1), 5)  # 1.1752
```

**Cost:** O(1)

---

### `hyperbolic_cosine()`

Calculates the hyperbolic cosine of a value.

**Parameters:**
- `x` (float): The value.

**Returns:**
- `float`: The hyperbolic cosine of the given value.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import hyperbolic_cosine

hyperbolic_cosine(0)  # 1.0
round(hyperbolic_cosine(1), 5)  # 1.54308
```

**Cost:** O(1)

---

### `hyperbolic_tangent()`

Calculates the hyperbolic tangent of a value.

**Parameters:**
- `x` (float): The value.

**Returns:**
- `float`: The hyperbolic tangent of the given value.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import hyperbolic_tangent

hyperbolic_tangent(0)  # 0.0
round(hyperbolic_tangent(1), 5)  # 0.76159
```

**Cost:** O(1)

---

### `inverse_hyperbolic_sine()`

Calculates the inverse hyperbolic sine (arcsinh) of a value.

**Parameters:**
- `x` (float): The value.

**Returns:**
- `float`: The inverse hyperbolic sine of the given value.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import inverse_hyperbolic_sine

inverse_hyperbolic_sine(0)  # 0.0
round(inverse_hyperbolic_sine(1.1752), 5)  # 1.0
```

**Cost:** O(1)

---

### `inverse_hyperbolic_cosine()`

Calculates the inverse hyperbolic cosine (arccosh) of a value.

**Parameters:**
- `x` (float): The value. Must be greater than or equal to 1.

**Returns:**
- `float`: The inverse hyperbolic cosine of the given value.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import inverse_hyperbolic_cosine

inverse_hyperbolic_cosine(1.0)  # 0.0
round(inverse_hyperbolic_cosine(1.54308), 5)  # 1.0
```

**Cost:** O(1)

---

### `inverse_hyperbolic_tangent()`

Calculates the inverse hyperbolic tangent (arctanh) of a value.

**Parameters:**
- `x` (float): The value. Must be in the range (-1, 1).

**Returns:**
- `float`: The inverse hyperbolic tangent of the given value.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import inverse_hyperbolic_tangent

inverse_hyperbolic_tangent(0)  # 0.0
round(inverse_hyperbolic_tangent(0.76159), 5)  # 1.0
```

**Cost:** O(1)

---

### `inverse_secant()`

Calculates the inverse secant (arcsec) of a value.

**Parameters:**
- `x` (float): The value whose inverse secant is to be calculated. Domain: |x| >= 1.

**Returns:**
- `float`: The inverse secant of the given value in radians.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import inverse_secant

round(inverse_secant(1.0), 10)  # 0.0
round(inverse_secant(-1.0), 10)  # 3.1415926536
round(inverse_secant(2.0), 10)  # 1.0471975512
```

**Cost:** O(1)

---

### `inverse_cosecant()`

Calculates the inverse cosecant (arccosec) of a value.

**Parameters:**
- `x` (float): The value whose inverse cosecant is to be calculated. Domain: |x| >= 1.

**Returns:**
- `float`: The inverse cosecant of the given value in radians.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import inverse_cosecant

round(inverse_cosecant(1.0), 10)  # 1.5707963268
round(inverse_cosecant(-1.0), 10)  # -1.5707963268
round(inverse_cosecant(2.0), 10)  # 0.5235987756
```

**Cost:** O(1)

---

### `inverse_cotangent()`

Calculates the inverse cotangent (arccotan) of a value.

**Parameters:**
- `x` (float): The value whose inverse cotangent is to be calculated.

**Returns:**
- `float`: The inverse cotangent of the given value in radians.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import inverse_cotangent

round(inverse_cotangent(1.0), 10)  # 0.7853981634
round(inverse_cotangent(0.0), 10)  # 1.5707963268
round(inverse_cotangent(-1.0), 10)  # 2.3561944902
```

**Cost:** O(1)

---

### `inverse_hyperbolic_secant()`

Calculates the inverse hyperbolic secant (arcsech) of a value.

**Parameters:**
- `x` (float): The value. Must be in the range (0, 1].

**Returns:**
- `float`: The inverse hyperbolic secant of the given value.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import inverse_hyperbolic_secant

round(inverse_hyperbolic_secant(1.0), 10)  # 0.0
round(inverse_hyperbolic_secant(0.5), 10)  # 1.3169578969
```

**Cost:** O(1)

---

### `inverse_hyperbolic_cosecant()`

Calculates the inverse hyperbolic cosecant (arccosech) of a value.

**Parameters:**
- `x` (float): The value. Must not be 0.

**Returns:**
- `float`: The inverse hyperbolic cosecant of the given value.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import inverse_hyperbolic_cosecant

round(inverse_hyperbolic_cosecant(1.0), 10)  # 0.881373587
round(inverse_hyperbolic_cosecant(-1.0), 10)  # -0.881373587
```

**Cost:** O(1)

---

### `inverse_hyperbolic_cotangent()`

Calculates the inverse hyperbolic cotangent (arccotanh) of a value.

**Parameters:**
- `x` (float): The value. Must be |X| > 1.

**Returns:**
- `float`: The inverse hyperbolic cotangent of the given value.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import inverse_hyperbolic_cotangent

round(inverse_hyperbolic_cotangent(2.0), 10)  # 0.5493061443
round(inverse_hyperbolic_cotangent(-2.0), 10)  # -0.5493061443
```

**Cost:** O(1)

---

### `degrees_to_radians()`

Converts an angle from degrees to radians.

**Parameters:**
- `degrees` (float): The angle in degrees.

**Returns:**
- `float`: The equivalent angle in radians.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import degrees_to_radians

degrees_to_radians(180)  # 3.141592653589793
degrees_to_radians(90)  # 1.5707963267948966
```

**Cost:** O(1)

---

### `radians_to_degrees()`

Converts an angle from radians to degrees.

**Parameters:**
- `radians` (float): The angle in radians.

**Returns:**
- `float`: The equivalent angle in degrees.

**Example:**
```python
import math
from formulite.fxNumeric.trigonometry_functions import radians_to_degrees

radians_to_degrees(math.pi)  # 180.0
radians_to_degrees(math.pi / 2)  # 90.0
```

**Cost:** O(1)

---

### `secant()`

Calculates the secant of an angle (1/cos).

**Parameters:**
- `angle_radians` (float): The angle in radians.

**Returns:**
- `float`: The secant of the given angle.

**Example:**
```python
from formulite.fxNumeric.trigonometry_functions import secant

round(secant(0), 10)  # 1.0 (sec(0 degrees))
round(secant(math.pi), 10)  # -1.0 (sec(180 degrees))
```

**Cost:** O(1)

---

### `cosecant()`

Calculates the cosecant of an angle (1/sin).

**Parameters:**
- `angle_radians` (float): The angle in radians.

**Returns:**
- `float`: The cosecant of the given angle.

**Example:**
```python
import math
from formulite.fxNumeric.trigonometry_functions import cosecant

round(cosecant(math.pi / 2), 10)  # 1.0 (cosec(90 degrees))
round(cosecant(3 * math.pi / 2), 10)  # -1.0 (cosec(270 degrees))
```

**Cost:** O(1)

---

### `cotangent()`

Calculates the cotangent of an angle (1/tan).

**Parameters:**
- `angle_radians` (float): The angle in radians.

**Returns:**
- `float`: The cotangent of the given angle.

**Example:**
```python
import math
from formulite.fxNumeric.trigonometry_functions import cotangent

round(cotangent(math.pi / 4), 10)  # 1.0 (cot(45 degrees))
```

**Cost:** O(1)

---

## Financial Functions

### `future_value()`

Calculates the Future Value (FV) of an investment based on periodic constant payments and a constant interest rate.

**Parameters:**
- `rate` (float): The interest rate per period (e.g., 0.05 for 5% annual rate).
- `nper` (Union[int, float]): The total number of payment periods in an investment.
- `pmt` (float): The payment made each period. Payments are typically negative (cash outflow).
- `pv` (float): The Present Value (PV). Typically negative (cash outflow).
- `type` (int, optional): When payments are due. 0 = at the end of the period (default). 1 = at the beginning of the period.

**Returns:**
- `float`: The Future Value of the investment.

**Example:**
```python
from formulite.fxNumeric.finance_functions import future_value

# FV of $1000 invested for 5 years at 5% annual interest
future_value(rate=0.05, nper=5, pmt=0, pv=-1000)  # 1276.2815625000003

# FV of $100 payments at end of each year for 5 years at 5%
future_value(rate=0.05, nper=5, pmt=-100, pv=0)  # 552.5631250000001
```

**Cost:** O(1)

---

### `present_value()`

Calculates the Present Value (PV) of an investment based on a series of future payments and a constant interest rate.

**Parameters:**
- `rate` (float): The interest rate per period.
- `nper` (Union[int, float]): The total number of payment periods.
- `pmt` (float): The payment made each period.
- `fv` (float, optional): The Future Value. Defaults to 0.0.
- `type` (int, optional): When payments are due. 0 = end (default), 1 = beginning.

**Returns:**
- `float`: The Present Value of the investment.

**Example:**
```python
from formulite.fxNumeric.finance_functions import present_value

# PV of $1276.28 received in 5 years at 5% annual interest
present_value(rate=0.05, nper=5, pmt=0, fv=1276.28)  # -999.9989807559194

# PV of $100 payments received at end of each year for 5 years at 5%
present_value(rate=0.05, nper=5, pmt=100, fv=0)  # -432.94766060133177
```

**Cost:** O(1)

---

### `pmt()`

Calculates the payment for a loan based on constant payments and a constant interest rate.

**Parameters:**
- `rate` (float): The interest rate per period.
- `nper` (Union[int, float]): The total number of payments for the loan.
- `pv` (float): The Present Value, or the principal amount of the loan.
- `fv` (float, optional): The Future Value. Defaults to 0.0.
- `type` (int, optional): When payments are due. 0 = end (default), 1 = beginning.

**Returns:**
- `float`: The payment made each period (will be negative as cash outflow).

**Example:**
```python
from formulite.fxNumeric.finance_functions import pmt

# Monthly payment for a $100,000 loan at 5% annual interest for 30 years
# Monthly rate = 0.05 / 12, NPER = 30 * 12 = 360
round(pmt(rate=0.05/12, nper=360, pv=100000), 2)  # -536.82
```

**Cost:** O(1)

---

### `nper()`

Calculates the number of periods for an investment based on periodic, constant payments and a constant interest rate.

**Parameters:**
- `rate` (float): The interest rate per period.
- `pmt` (float): The payment made each period.
- `pv` (float): The Present Value.
- `fv` (float, optional): The Future Value. Defaults to 0.0.
- `type` (int, optional): When payments are due (0 for end, 1 for beginning).

**Returns:**
- `float`: The number of periods.

**Example:**
```python
from formulite.fxNumeric.finance_functions import nper

# Number of months to pay off $10,000 loan with $100 monthly payments at 5% annual
# Monthly rate = 0.05 / 12
round(nper(rate=0.05/12, pmt=-100, pv=10000), 2)  # 122.09
```

**Cost:** O(1)

---

### `rate()`

Calculates the interest rate per period of an annuity using an iterative approach.

**Parameters:**
- `nper` (Union[int, float]): The total number of payment periods.
- `pmt` (float): The payment made each period.
- `pv` (float): The Present Value.
- `fv` (float, optional): The Future Value. Defaults to 0.0.
- `type` (int, optional): When payments are due (0 for end, 1 for beginning).
- `guess` (float, optional): Your guess for the rate. Defaults to 0.1 (10%).

**Returns:**
- `float`: The interest rate per period.

**Example:**
```python
from formulite.fxNumeric.finance_functions import rate

# If you pay $536.82 monthly for 360 months on a $100,000 loan
# Result will be monthly rate, multiply by 12 for annual
monthly_rate = rate(nper=360, pmt=-536.82, pv=100000)
round(monthly_rate * 12, 4)  # 0.05

# If you invest $1000 and it grows to $1276.28 in 5 years
round(rate(nper=5, pmt=0, pv=-1000, fv=1276.28), 4)  # 0.05
```

**Cost:** O(n) where n is the number of iterations to converge

---

### `irr()`

Calculates the Internal Rate of Return (IRR) for a series of cash flows.

**Parameters:**
- `cash_flows` (List[float]): A list of cash flows, where the first cash flow is typically the initial investment (negative).
- `guess` (float, optional): An optional initial guess for the IRR. Defaults to 0.1 (10%).

**Returns:**
- `float`: The Internal Rate of Return.

**Example:**
```python
from formulite.fxNumeric.finance_functions import irr

# Initial investment of -$100, followed by $20, $30, $40, $50, $60
irr([-100, 20, 30, 40, 50, 60])  # 0.2809484834920677
```

**Cost:** O(n × m) where n is the number of cash flows and m is iterations to converge

---

### `npv()`

Calculates the Net Present Value (NPV) of an investment.

**Parameters:**
- `rate` (float): The discount rate per period (e.g., 0.05 for 5%).
- `values` (List[float]): A list of cash flows, starting with the initial investment.

**Returns:**
- `float`: The Net Present Value.

**Example:**
```python
from formulite.fxNumeric.finance_functions import npv

# NPV of initial -$100, followed by $20, $30, $40, $50, $60 at 10% discount
round(npv(rate=0.10, values=[-100, 20, 30, 40, 50, 60]), 2)  # 60.85
```

**Cost:** O(n) where n is the number of cash flows

---

### `sln()`

Calculates the straight-line depreciation of an asset for one period.

**Parameters:**
- `cost` (float): The initial cost of the asset.
- `salvage` (float): The salvage value at the end of useful life.
- `life` (Union[int, float]): The number of periods over which the asset is depreciated.

**Returns:**
- `float`: The depreciation per period.

**Example:**
```python
from formulite.fxNumeric.finance_functions import sln

# Asset costs $10,000, salvage value $2,000, useful life 5 years
sln(cost=10000, salvage=2000, life=5)  # 1600.0
```

**Cost:** O(1)

---

### `db()`

Calculates the depreciation of an asset using the fixed-declining balance method.

**Parameters:**
- `cost` (float): The initial cost of the asset.
- `salvage` (float): The salvage value.
- `life` (Union[int, float]): The number of periods over which the asset is depreciated.
- `period` (Union[int, float]): The period for which to calculate the depreciation.
- `month` (int, optional): The number of months in the first year. Defaults to 12.

**Returns:**
- `float`: The depreciation for the specified period.

**Example:**
```python
from formulite.fxNumeric.finance_functions import db

# Asset costs $10,000, salvage $1,000, useful life 5 years, period 1
db(cost=10000, salvage=1000, life=5, period=1)  # 3333.333333333333
```

**Cost:** O(1)

---

## Missing Functions from fxExcel and fxVBA

Functions available in `fxExcel` or `fxVBA` that do **not** have an equivalent in `fxNumeric`.
Organized by target file and functional category.

> **Legend:**
> - **Source** column shows where the function exists today (`fxExcel` file or `fxVBA` file).
> - Functions already covered by an existing `fxNumeric` equivalent are **excluded**.

---

### Missing in `arithmetic_functions.py` — Math & Arithmetic

| Function | Source | Description |
|----------|--------|-------------|
| `absolute_value(number)` | `fxExcel/math_formulas.ABS`, `fxVBA/math_functions.Abs_` | Returns the absolute value of a number. |
| `sign(number)` | `fxExcel/math_formulas.SIGN`, `fxVBA/math_functions.Sgn` | Returns 1 (positive), 0 (zero), or −1 (negative). |
| `exponential(number)` | `fxExcel/math_formulas.EXP`, `fxVBA/math_functions.Exp` | Returns $e$ raised to the power of a number. |
| `factorial(n)` | `fxExcel/math_formulas.FACT` | Returns $n!$ (factorial of a non-negative integer). |
| `double_factorial(n)` | `fxExcel/math_formulas.FACTDOUBLE` | Returns the double factorial $n!!$. |
| `gcd(*numbers)` | `fxExcel/math_formulas.GCD` | Returns the greatest common divisor of one or more integers. |
| `lcm(*numbers)` | `fxExcel/math_formulas.LCM` | Returns the least common multiple of one or more integers. |
| `modulo(number, divisor)` | `fxExcel/math_formulas.MOD` | Returns the remainder after division. |
| `combinations(n, k)` | `fxExcel/math_formulas.COMBIN` | Returns the number of combinations $C(n,k)$. |
| `combinations_with_repetition(n, k)` | `fxExcel/math_formulas.COMBINA` | Returns combinations with repetition $\binom{n+k-1}{k}$. |
| `permutations(n, k)` | `fxExcel/statistic_formulas.PERMUT` | Returns the number of permutations $P(n,k)$. |
| `permutations_with_repetition(n, k)` | `fxExcel/statistic_formulas.PERMUTATIONA` | Returns $n^k$ (permutations with repetition). |
| `multinomial(*numbers)` | `fxExcel/math_formulas.MULTINOMIAL` | Returns the multinomial coefficient. |
| `product(*numbers)` | `fxExcel/math_formulas.PRODUCT` | Returns the product of all numbers. |
| `sum_values(*numbers)` | `fxExcel/math_formulas.SUM` | Returns the sum of all numbers. |
| `sum_product(*arrays)` | `fxExcel/math_formulas.SUMPRODUCT` | Returns sum of element-wise products of arrays. |
| `pi_constant()` | `fxExcel/math_formulas.PI` | Returns the value of $\pi$. |
| `sqrt_pi(number)` | `fxExcel/math_formulas.SQRTPI` | Returns $\sqrt{number \times \pi}$. |
| `series_sum(x, n, m, coefficients)` | `fxExcel/math_formulas.SERIESSUM` | Returns the sum of a power series. |
| `random_number()` | `fxExcel/math_formulas.RAND`, `fxVBA/math_functions.Rnd` | Returns a random float between 0 and 1. |
| `random_between(bottom, top)` | `fxExcel/math_formulas.RANDBETWEEN` | Returns a random integer between bottom and top. |
| `random_array(rows, columns, min_val, max_val, whole_number)` | `fxExcel/math_formulas.RANDARRAY` | Returns a 2D array of random numbers. |
| `sequence(rows, columns, start, step)` | `fxExcel/math_formulas.SEQUENCE` | Generates a sequence of numbers in a 2D array. |

---

### Missing in `rounding_functions.py` / `format_functions.py` — Rounding & Matrix

| Function | Source | Description |
|----------|--------|-------------|
| `ceiling_to_significance(number, significance)` | `fxExcel/math_formulas.CEILING` | Rounds a number up to the nearest multiple of significance. |
| `ceiling_math(number, significance, mode)` | `fxExcel/math_formulas.CEILING_MATH` | Rounds up with mode control for negatives (mode=1 rounds toward zero). |
| `ceiling_precise(number, significance)` | `fxExcel/math_formulas.CEILING_PRECISE` | Rounds up to the nearest multiple (always away from zero). |
| `floor_to_significance(number, significance)` | `fxExcel/math_formulas.FLOOR` | Rounds a number down to the nearest multiple of significance. |
| `floor_math(number, significance, mode)` | `fxExcel/math_formulas.FLOOR_MATH` | Rounds down with mode control for negatives. |
| `floor_precise(number, significance)` | `fxExcel/math_formulas.FLOOR_PRECISE` | Rounds down to the nearest multiple (always toward zero). |
| `round_to_even(number)` | `fxExcel/math_formulas.EVEN` | Rounds a number up to the nearest even integer. |
| `round_to_odd(number)` | `fxExcel/math_formulas.ODD` | Rounds a number up to the nearest odd integer. |
| `truncate(number, num_digits)` | `fxExcel/math_formulas.TRUNC` | Truncates a number to the specified number of digits. |
| `matrix_determinant(matrix)` | `fxExcel/math_formulas.MDETERM` | Returns the determinant of a square matrix. |
| `matrix_inverse(matrix)` | `fxExcel/math_formulas.MINVERSE` | Returns the inverse of a square matrix. |
| `matrix_multiply(matrix1, matrix2)` | `fxExcel/math_formulas.MMULT` | Returns the product of two matrices. |
| `identity_matrix(dimension)` | `fxExcel/math_formulas.MUNIT` | Returns an identity matrix of given dimension. |
| `integer_quotient(numerator, denominator)` | `fxExcel/math_formulas.QUOTIENT` | Returns the integer portion of a division. |
| `aggregate(data, operation)` | `fxExcel/math_formulas.AGGREGATE` | Performs aggregate operations (sum, avg, max, min) on a list. |
| `subtotal(function_num, *values)` | `fxExcel/math_formulas.SUBTOTAL` | Applies a numbered function (1-11) to values. |
| `sum_x2_minus_y2(array_x, array_y)` | `fxExcel/math_formulas.SUMX2MY2` | Returns $\sum(x_i^2 - y_i^2)$. |
| `sum_x2_plus_y2(array_x, array_y)` | `fxExcel/math_formulas.SUMX2PY2` | Returns $\sum(x_i^2 + y_i^2)$. |
| `sum_xmy2(array_x, array_y)` | `fxExcel/math_formulas.SUMXMY2` | Returns $\sum(x_i - y_i)^2$. |

---

### Missing in `conversion_functions.py` — Base & Numeral Conversions

| Function | Source | Description |
|----------|--------|-------------|
| `number_to_base(number, radix, min_length)` | `fxExcel/math_formulas.BASE` | Converts a number to text representation in a given base (2-36). |
| `base_to_decimal(text, radix)` | `fxExcel/math_formulas.DECIMAL` | Converts text representation in a given base to decimal. |
| `arabic_from_roman(roman)` | `fxExcel/math_formulas.ARABIC` | Converts a Roman numeral string to an integer. |
| `roman_from_number(number, form)` | `fxExcel/math_formulas.ROMAN` | Converts an integer to a Roman numeral string. |

---

### Missing in `statistics_functions.py` — Descriptive Statistics

| Function | Source | Description |
|----------|--------|-------------|
| `geometric_mean(values)` | `fxExcel/statistic_formulas.GEOMEAN` | Returns the geometric mean of positive values. |
| `harmonic_mean(values)` | `fxExcel/statistic_formulas.HARMEAN` | Returns the harmonic mean of positive values. |
| `trimmed_mean(array, fraction)` | `fxExcel/statistic_formulas.TRIMMEAN` | Returns the mean after trimming a fraction from both tails. |
| `average_deviation(values)` | `fxExcel/statistic_formulas.AVEDEV` | Returns the average of absolute deviations from the mean. |
| `sum_of_squared_deviations(values)` | `fxExcel/statistic_formulas.DEVSQ` | Returns the sum of squared deviations from the mean. |
| `kurtosis(values)` | `fxExcel/statistic_formulas.KURT` | Returns the excess kurtosis of a data set. |
| `skewness(values)` | `fxExcel/statistic_formulas.SKEW` | Returns the sample skewness of a data set. |
| `skewness_population(values)` | `—` | Returns the population skewness of a data set. |
| `standardize(x, mean, standard_dev)` | `fxExcel/statistic_formulas.STANDARDIZE` | Returns a standardized z-score: $(x - \mu) / \sigma$. |
| `large_kth(array, k)` | `fxExcel/statistic_formulas.LARGE` | Returns the $k$-th largest value in a data set. |
| `small_kth(array, k)` | `fxExcel/statistic_formulas.SMALL` | Returns the $k$-th smallest value in a data set. |
| `percentile_rank(array, x, significance)` | `fxExcel/statistic_formulas.PERCENTRANK_INC` | Returns the percentile rank of a value within a data set. |
| `count_numbers(*values)` | `fxExcel/statistic_formulas.COUNT` | Counts the number of numeric values. |
| `count_non_empty(*values)` | `fxExcel/statistic_formulas.COUNTA` | Counts the number of non-empty values. |
| `count_blank(range_values)` | `fxExcel/statistic_formulas.COUNTBLANK` | Counts the number of blank values. |
| `count_if(range_values, criteria)` | `fxExcel/statistic_formulas.COUNTIF` | Counts values meeting a criteria. |
| `max_if(values, criteria_range, criteria)` | `fxExcel/statistic_formulas.MAXIFS` | Maximum of values where criteria range meets criteria. |
| `min_if(values, criteria_range, criteria)` | `fxExcel/statistic_formulas.MINIFS` | Minimum of values where criteria range meets criteria. |
| `sum_if(values, criteria_range, criteria)` | `fxExcel/math_formulas.SUMIF` | Sum of values where criteria range meets criteria. |
| `average_if(values, criteria_range, criteria)` | `fxExcel/statistic_formulas.AVERAGEIF` | Average of values where criteria range meets criteria. |

---

### Missing in `statistics_functions.py` — Regression & Forecasting

| Function | Source | Description |
|----------|--------|-------------|
| `linear_regression(known_y, known_x, const, stats_flag)` | `fxExcel/statistic_formulas.LINEST` | Returns slope, intercept, and optional regression statistics. |
| `exponential_regression(known_y, known_x, const, stats_flag)` | `fxExcel/statistic_formulas.LOGEST` | Returns exponential regression coefficients. |
| `slope(known_y, known_x)` | `fxExcel/statistic_formulas.SLOPE` | Returns the slope of the linear regression line. |
| `intercept(known_y, known_x)` | `fxExcel/statistic_formulas.INTERCEPT` | Returns the y-intercept of the linear regression line. |
| `standard_error_estimate(known_y, known_x)` | `fxExcel/statistic_formulas.STEYX` | Returns the standard error of the predicted y. |
| `forecast_linear(x, known_y, known_x)` | `fxExcel/statistic_formulas.FORECAST_LINEAR` | Predicts a value along a linear trend. |
| `growth_exponential(known_y, known_x, new_x, const)` | `fxExcel/statistic_formulas.GROWTH` | Returns predicted values along an exponential trend. |
| `fisher_transform(x)` | `fxExcel/statistic_formulas.FISHER` | Returns the Fisher transformation: $\frac{1}{2} \ln\frac{1+x}{1-x}$. |
| `fisher_inverse(y)` | `fxExcel/statistic_formulas.FISHERINV` | Returns the inverse of the Fisher transformation. |
| `gamma_function(number)` | `fxExcel/statistic_formulas.GAMMA` | Returns $\Gamma(n)$ (the gamma function). |
| `gamma_ln(x)` | `fxExcel/statistic_formulas.GAMMALN` | Returns $\ln(\Gamma(x))$. |
| `gauss(z)` | `fxExcel/statistic_formulas.GAUSS` | Returns 0.5 less than the standard normal cumulative distribution. |
| `phi(x)` | `fxExcel/statistic_formulas.PHI` | Returns the density of the standard normal distribution. |
| `confidence_norm(alpha, standard_dev, size)` | `fxExcel/statistic_formulas.CONFIDENCE_NORM` | Returns confidence interval half-width using normal distribution. |
| `confidence_t(alpha, standard_dev, size)` | `fxExcel/statistic_formulas.CONFIDENCE_T` | Returns confidence interval half-width using t-distribution. |

---

### Missing in `distribution_functions.py` — Probability Distributions

> ✅ **All distributions now implemented** — `beta_dist`, `beta_inv`, `gamma_dist`, `gamma_inv`, `lognorm_dist`, `lognorm_inv`, `negbinom_dist`, `weibull_dist`, `hypgeom_dist`, `binom_dist_range`, `binom_inv`, `t_dist_rt`, `t_dist_2t`, `t_inv_2t`, `chisq_dist_rt`, `chisq_inv_rt`, `f_dist_rt`, `f_inv_rt` (18 functions) plus previously existing `norm_dist`, `norm_inv`, `norm_s_dist`, `norm_s_inv`, `t_dist`, `t_inv`, `binom_dist`, `poisson_dist`, `chisq_dist`, `chisq_inv`, `f_dist`, `f_inv`, `expon_dist`, `gauss`, `phi`.

---

### Missing in `statistics_functions.py` — Hypothesis Tests

> ✅ **All hypothesis tests and advanced stats now implemented** — `chisq_test`, `f_test`, `t_test`, `z_test`, `percentile_exc`, `quartile_exc`, `percentrank_exc`, `mode_mult`, `mode_single`, `trend`, `growth`, `linest`, `logest` (13 functions).

---

### Added in `statistics_functions.py` — Population Skewness, Standardization & ETS Forecasting

| Function | Source | Description |
|----------|--------|-------------|
| `skew_p(data)` | `—` | Population skewness of a distribution. |
| `standardize(x, mean, standard_dev)` | `fxExcel/statistic_formulas.STANDARDIZE` | Returns z-value: $(x - \mu) / \sigma$. |
| `forecast_ets(target, values, timeline, ...)` | `fxExcel/statistic_formulas.FORECAST_ETS` | Forecast using exponential smoothing (Holt's method). |

---

### Added in `arithmetic_functions.py` — Bessel Functions & Bit Shifts

| Function | Source | Description |
|----------|--------|-------------|
| `bessel_i(x, n)` | `fxExcel/engineering_formulas.BESSELI` | Modified Bessel function of the first kind Iₙ(x). |
| `bessel_j(x, n)` | `fxExcel/engineering_formulas.BESSELJ` | Bessel function of the first kind Jₙ(x). |
| `bessel_k(x, n)` | `fxExcel/engineering_formulas.BESSELK` | Modified Bessel function of the second kind Kₙ(x). |
| `bessel_y(x, n)` | `fxExcel/engineering_formulas.BESSELY` | Bessel function of the second kind Yₙ(x). |
| `bit_lshift(number, shift_amount)` | `fxExcel/engineering_formulas.BITLSHIFT` | Left bit shift. |
| `bit_rshift(number, shift_amount)` | `fxExcel/engineering_formulas.BITRSHIFT` | Right bit shift. |

---

### Added in `finance_functions.py` — Equivalent Rate

| Function | Source | Description |
|----------|--------|-------------|
| `rri(nper, pv, fv)` | `fxExcel/financial_formulas.RRI` | Equivalent interest rate for investment growth. |

---

### Added in `conversion_functions.py` — Unit Conversion, Decibels, Physics & Electrical Engineering

| Function | Source | Description |
|----------|--------|-------------|
| `convert_units(number, from_unit, to_unit)` | `fxExcel/engineering_formulas.CONVERT` | General unit converter (13 categories). |
| `power_to_db(ratio)` | `—` | Power ratio → decibels. |
| `db_to_power(decibels)` | `—` | Decibels → power ratio. |
| `voltage_to_db(ratio)` | `—` | Voltage ratio → decibels. |
| `db_to_voltage(decibels)` | `—` | Decibels → voltage ratio. |
| `wavelength(freq, velocity)` | `—` | Frequency → wavelength. |
| `freq_from_wavelength(wl, velocity)` | `—` | Wavelength → frequency. |
| `doppler_freq(source_freq, velocity, wave_speed)` | `—` | Doppler effect observed frequency. |
| `shannon_capacity(bandwidth, snr)` | `—` | Shannon channel capacity. |
| `thermal_noise(bandwidth, temperature)` | `—` | Johnson-Nyquist thermal noise. |
| `free_space_path_loss(freq, distance)` | `—` | Free-space path loss (dB). |
| `friis_transmission(pt, gt, gr, wl, distance)` | `—` | Friis received power. |
| `impedance_series(r, l, c, freq)` | `—` | Series RLC impedance. |
| `impedance_parallel(z1, z2)` | `—` | Parallel impedance. |
| `resonant_freq(l, c)` | `—` | LC resonant frequency. |
| `skin_depth(freq, resistivity, permeability)` | `—` | AC skin depth. |

---

### Missing in `finance_functions.py` — Depreciation

> ✅ **All depreciation now implemented** — `ddb`, `syd`, `vdb`, `amorlinc` plus previously existing `sln`, `db`.

---

### Missing in `finance_functions.py` — Payments & Interest

> ✅ **All payments & interest now implemented** — `ispmt`, `dollarde`, `dollarfr` plus previously existing `ipmt`, `ppmt`, `cumipmt`, `cumprinc`, `mirr`, `xirr`, `xnpv`, `fvschedule`, `effect`, `nominal`, `pduration`.

---

### Missing in `finance_functions.py` — Bonds & Securities

> ✅ **All bonds & securities now implemented** — `duration`, `mduration`, `accrint`, `accrintm`, `price`, `pricedisc`, `pricemat`, `yield_bond`, `yielddisc`, `yieldmat`, `coupdays`, `coupdaybs`, `coupdaysnc`, `coupncd`, `couppcd`, `coupnum`, `disc`, `intrate`, `received`, `tbilleq`, `tbillprice`, `tbillyield` (22 functions).

---

### Summary by File

| Target file | Missing functions | Category |
|-------------|:-----------------:|----------|
| `arithmetic_functions.py` | 23 | Math, combinatorics, random, sequences |
| `rounding_functions.py` / `format_functions.py` | 19 | Rounding with significance, matrices, aggregates |
| `conversion_functions.py` | 4 | General base conversion, Roman numerals |
| `statistics_functions.py` / `distribution_functions.py` | ✅ Done | Descriptive stats, regression, distributions, tests |
| `finance_functions.py` | ✅ Done | Depreciation, payments, bonds, securities |
| **Total** | **143** | |

---

### `absolute_value()`

Returns the absolute (non-negative) value of a number.

**Parameters:**
- x (Union[int, float]): The number.

**Returns:**
- Union[int, float]: The absolute value of x.

**Raises:**
- TypeError: If x is not numeric.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import absolute_value

result = absolute_value(...)
```

---

### `argmax()`

Returns the index of the maximum value in a list.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- Zero-based index of the first maximum value.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import argmax

result = argmax(...)
```

---

### `argmin()`

Returns the index of the minimum value in a list.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- Zero-based index of the first minimum value.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import argmin

result = argmin(...)
```

---

### `average_deviation()`

Calculates the average of absolute deviations from the mean.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- The average absolute deviation.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import average_deviation

result = average_deviation(...)
```

---

### `base_to_decimal()`

Converts a string representation from the specified base to decimal.

**Parameters:**
- text: The string representing the number in the given base.
- radix: The base of the input number (2 to 36).

**Returns:**
- The decimal integer value.

**Raises:**
- TypeError: If text is not a string or radix is not an integer.
- ValueError: If the text contains invalid digits for the given base,
- or the radix is outside 2–36.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import base_to_decimal

result = base_to_decimal(...)
```

---

### `bfill()`

Backward-fills None values with the next non-None value.

**Parameters:**
- data: A list that may contain None values.

**Returns:**
- A new list with None values replaced by the next non-None value.

**Raises:**
- TypeError: If input is not a list.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import bfill

result = bfill(...)
```

---

### `bin_to_hex()`

Converts a binary string to hexadecimal.

**Parameters:**
- binary: A string of 0s and 1s (optional '0b' prefix).

**Returns:**
- Uppercase hexadecimal string without prefix.

**Raises:**
- TypeError: If input is not a string.
- ValueError: If the string contains invalid binary digits.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import bin_to_hex

result = bin_to_hex(...)
```

---

### `bin_to_oct()`

Converts a binary string to octal.

**Parameters:**
- binary: A string of 0s and 1s (optional '0b' prefix).

**Returns:**
- Octal string without prefix.

**Raises:**
- TypeError: If input is not a string.
- ValueError: If the string contains invalid binary digits.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import bin_to_oct

result = bin_to_oct(...)
```

---

### `binom_dist()`

Binomial distribution PMF or CDF.

**Parameters:**
- number_s: Number of successes.
- trials: Number of independent trials.
- probability_s: Probability of success on each trial.
- cumulative: If True return CDF, else PMF.

**Returns:**
- Probability value.

**Raises:**
- TypeError: If inputs are not of expected types.
- ValueError: If parameters are out of valid ranges.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import binom_dist

result = binom_dist(...)
```

---

### `bit_count()`

Counts the number of set bits (1-bits) in a non-negative integer.

**Parameters:**
- number: A non-negative integer.

**Returns:**
- The number of 1-bits.

**Raises:**
- TypeError: If input is not an integer.
- ValueError: If input is negative.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import bit_count

result = bit_count(...)
```

---

### `bitwise_and()`

Returns the bitwise AND of two non-negative integers.

**Parameters:**
- a: First non-negative integer.
- b: Second non-negative integer.

**Returns:**
- The bitwise AND result.

**Raises:**
- TypeError: If inputs are not integers.
- ValueError: If inputs are negative.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import bitwise_and

result = bitwise_and(...)
```

---

### `bitwise_not()`

Returns the bitwise NOT of a non-negative integer within a given bit width.

**Parameters:**
- number: A non-negative integer.
- bit_width: The number of bits to consider (default 32).

**Returns:**
- The bitwise NOT result within the bit width.

**Raises:**
- TypeError: If inputs are not integers.
- ValueError: If number is negative or bit_width < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import bitwise_not

result = bitwise_not(...)
```

---

### `bitwise_or()`

Returns the bitwise OR of two non-negative integers.

**Parameters:**
- a: First non-negative integer.
- b: Second non-negative integer.

**Returns:**
- The bitwise OR result.

**Raises:**
- TypeError: If inputs are not integers.
- ValueError: If inputs are negative.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import bitwise_or

result = bitwise_or(...)
```

---

### `bitwise_xor()`

Returns the bitwise XOR of two non-negative integers.

**Parameters:**
- a: First non-negative integer.
- b: Second non-negative integer.

**Returns:**
- The bitwise XOR result.

**Raises:**
- TypeError: If inputs are not integers.
- ValueError: If inputs are negative.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import bitwise_xor

result = bitwise_xor(...)
```

---

### `ceiling_significance()`

Rounds a number up to the nearest multiple of significance.

**Parameters:**
- number: The number to round.
- significance: The multiple to round up to. Default 1.

**Returns:**
- The rounded value.

**Raises:**
- ValueError: If significance is zero.

**Ejemplo:**
```python
from formulite.fxNumeric.rounding_functions import ceiling_significance

result = ceiling_significance(...)
```

---

### `chisq_dist()`

Chi-squared distribution PDF or CDF.

**Parameters:**
- x: The value at which to evaluate (must be >= 0).
- deg_freedom: Degrees of freedom (must be >= 1).
- cumulative: If True return CDF, else PDF.

**Returns:**
- Probability value.

**Raises:**
- TypeError: If inputs are not of expected types.
- ValueError: If parameters are out of valid ranges.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import chisq_dist

result = chisq_dist(...)
```

---

### `chisq_inv()`

Inverse of the chi-squared cumulative distribution.

**Parameters:**
- probability: A probability in (0, 1).
- deg_freedom: Degrees of freedom (must be >= 1).

**Returns:**
- The chi-squared value.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import chisq_inv

result = chisq_inv(...)
```

---

### `clamp_interpolate()`

Linearly interpolate between two points, clamped to the output range.

**Parameters:**
- x: The x position to evaluate.
- x0: x coordinate of the first point.
- y0: y coordinate of the first point.
- x1: x coordinate of the second point.
- y1: y coordinate of the second point.

**Returns:**
- Clamped interpolated y value.

**Raises:**
- ValueError: If x0 == x1.

**Ejemplo:**
```python
from formulite.fxNumeric.interpolation_functions import clamp_interpolate

result = clamp_interpolate(...)
```

---

### `coefficient_of_variation()`

Calculates the coefficient of variation (CV) of a dataset.

**Parameters:**
- data: A list of numeric values.
- sample: If True, uses sample std deviation; otherwise population.

**Returns:**
- The coefficient of variation as a ratio (e.g. 0.25 means 25 %).

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty, has fewer than 2 elements for
- sample mode, or if the mean is zero.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import coefficient_of_variation

result = coefficient_of_variation(...)
```

---

### `combinations()`

Calculates the number of combinations C(n, k).

**Parameters:**
- n (int): Total number of items (non-negative).
- k (int): Number of items to choose (0 ≤ k ≤ n).

**Returns:**
- int: The number of combinations.

**Raises:**
- TypeError: If n or k are not integers.
- ValueError: If n or k are negative, or if k > n.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import combinations

result = combinations(...)
```

---

### `combinations_with_repetition()`

Calculates combinations with repetition (multiset coefficient).

**Parameters:**
- n: Number of types to choose from.
- k: Number of items to choose.

**Returns:**
- Number of combinations with repetition.

**Raises:**
- TypeError: If n or k are not integers.
- ValueError: If n < 1 or k < 0.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import combinations_with_repetition

result = combinations_with_repetition(...)
```

---

### `complementary_error_function()`

Calculates the complementary error function erfc(x) = 1 - erf(x).

**Parameters:**
- x (float): A real number.

**Returns:**
- float: The complementary error function value at x.

**Raises:**
- TypeError: If x is not numeric.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import complementary_error_function

result = complementary_error_function(...)
```

---

### `confidence_norm()`

Calculates the confidence interval half-width using the normal distribution.

**Parameters:**
- alpha: Significance level (e.g. 0.05 for 95% confidence).
- standard_dev: Population standard deviation.
- size: Sample size.

**Returns:**
- The margin of error (half-width of the confidence interval).

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If alpha is not in (0, 1), standard_dev <= 0, or size < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import confidence_norm

result = confidence_norm(...)
```

---

### `confidence_t()`

Calculates the confidence interval half-width using the Student's t-distribution.

**Parameters:**
- alpha: Significance level (e.g. 0.05 for 95% confidence).
- standard_dev: Sample standard deviation.
- size: Sample size.

**Returns:**
- The margin of error (half-width of the confidence interval).

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If alpha is not in (0, 1), standard_dev <= 0, or size < 2.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import confidence_t

result = confidence_t(...)
```

---

### `covariance_matrix()`

Computes the sample covariance matrix for a set of variables.

**Parameters:**
- data: A list of lists where ``data[i]`` is the observation series
- for variable *i*. Must contain at least 2 variables and
- at least 2 observations each.

**Returns:**
- A square matrix (list of lists) where element ``[i][j]`` is the
- sample covariance between variable *i* and variable *j*.

**Raises:**
- TypeError: If *data* is not a list of numeric lists.
- ValueError: If fewer than 2 variables or observations are given,
- or if observation lengths differ.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import covariance_matrix

result = covariance_matrix(...)
```

---

### `cumipmt()`

Calculates cumulative interest paid between two periods.

**Parameters:**
- rate: Interest rate per period.
- nper: Total number of periods.
- pv: Present value (loan amount).
- start_period: First period (1-based).
- end_period: Last period (1-based).
- type: 0 = end of period, 1 = beginning. Default 0.

**Returns:**
- Cumulative interest paid.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import cumipmt

result = cumipmt(...)
```

---

### `cumprinc()`

Calculates cumulative principal paid between two periods.

**Parameters:**
- rate: Interest rate per period.
- nper: Total number of periods.
- pv: Present value (loan amount).
- start_period: First period (1-based).
- end_period: Last period (1-based).
- type: 0 = end of period, 1 = beginning. Default 0.

**Returns:**
- Cumulative principal paid.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import cumprinc

result = cumprinc(...)
```

---

### `cumulative_max()`

Returns the running cumulative maximum of a list.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- A list of the same length with cumulative maxima.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import cumulative_max

result = cumulative_max(...)
```

---

### `cumulative_min()`

Returns the running cumulative minimum of a list.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- A list of the same length with cumulative minima.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import cumulative_min

result = cumulative_min(...)
```

---

### `cumulative_product()`

Returns the running cumulative product of a list.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- A list of the same length with cumulative products.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import cumulative_product

result = cumulative_product(...)
```

---

### `cumulative_sum()`

Returns the running cumulative sum of a list.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- A list of the same length with cumulative sums.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import cumulative_sum

result = cumulative_sum(...)
```

---

### `ddb()`

Calculates depreciation using the double-declining balance method.

**Parameters:**
- cost: Initial cost of the asset.
- salvage: Salvage value at end of life.
- life: Number of periods.
- period: Period for which to calculate (1-based).
- factor: Depreciation factor. Default 2.0 (double).

**Returns:**
- Depreciation for the specified period.

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If parameters are out of valid ranges.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import ddb

result = ddb(...)
```

---

### `dec_to_oct()`

Converts a decimal integer to octal.

**Parameters:**
- number: A non-negative integer.

**Returns:**
- Octal string without prefix.

**Raises:**
- TypeError: If input is not an integer.
- ValueError: If input is negative.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import dec_to_oct

result = dec_to_oct(...)
```

---

### `decimal_to_fraction()`

Convert a decimal number to a fraction (numerator, denominator).

**Parameters:**
- number: Decimal value to convert.
- max_denominator: Maximum denominator allowed. Defaults to 1000.

**Returns:**
- Tuple (numerator, denominator).

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import decimal_to_fraction

result = decimal_to_fraction(...)
```

---

### `delta()`

Tests whether two values are equal (Kronecker delta).

**Parameters:**
- number_1: The first number.
- number_2: The second number (defaults to 0).

**Returns:**
- 1 if the values are equal, 0 otherwise.

**Raises:**
- TypeError: If inputs are not numeric.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import delta

result = delta(...)
```

---

### `describe()`

Returns a summary of descriptive statistics for a list (like pandas describe).

**Parameters:**
- data: A list of numeric values.

**Returns:**
- A dict with keys: ``count``, ``mean``, ``std``, ``min``, ``25%``,
- ``50%`` (median), ``75%``, ``max``.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import describe

result = describe(...)
```

---

### `deviation_squared()`

Calculates the sum of squared deviations from the mean.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- Sum of squared deviations.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import deviation_squared

result = deviation_squared(...)
```

---

### `diff()`

Calculates consecutive differences in a list (like pandas Series.diff).

**Parameters:**
- data: A list of numeric values.
- periods: Number of positions to shift for the difference (default 1).

**Returns:**
- A list of the same length. The first *periods* entries are ``None``.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty or periods < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import diff

result = diff(...)
```

---

### `double_factorial()`

Calculates the double factorial of a non-negative integer.

**Parameters:**
- n (int): A non-negative integer.

**Returns:**
- int: The double factorial of n.

**Raises:**
- TypeError: If n is not an integer.
- ValueError: If n is negative.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import double_factorial

result = double_factorial(...)
```

---

### `effect()`

Calculates the effective annual interest rate.

**Parameters:**
- nominal_rate: Nominal annual interest rate.
- npery: Number of compounding periods per year.

**Returns:**
- The effective annual rate.

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If nominal_rate <= 0 or npery < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import effect

result = effect(...)
```

---

### `entropy()`

Calculates the Shannon entropy of a discrete dataset.

**Parameters:**
- data: A list of categorical or numeric values.

**Returns:**
- The Shannon entropy in bits (log base 2).

**Raises:**
- TypeError: If input is not a list.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import entropy

result = entropy(...)
```

---

### `error_function()`

Calculates the error function erf(x).

**Parameters:**
- x (float): A real number.

**Returns:**
- float: The error function value at x.

**Raises:**
- TypeError: If x is not numeric.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import error_function

result = error_function(...)
```

---

### `evaluate_expression()`

Safely evaluates a mathematical expression from a string.

**Parameters:**
- expression (str): A mathematical expression string.
- Examples: "sin(pi/4) + sqrt(2)", "log(100, 10)", "2**10 + 1"

**Returns:**
- Union[int, float]: The numeric result of the expression.

**Raises:**
- TypeError: If expression is not a string.
- ValueError: If the expression is empty, too long, contains syntax
- errors, or uses unsupported operations.

**Ejemplo:**
```python
from formulite.fxNumeric.calculator_functions import evaluate_expression

result = evaluate_expression(...)
```

---

### `even()`

Rounds a number up to the nearest even integer.

**Parameters:**
- number: The number to round.

**Returns:**
- The nearest even integer away from zero.

**Ejemplo:**
```python
from formulite.fxNumeric.rounding_functions import even

result = even(...)
```

---

### `exp()`

Calculates e raised to the power of x.

**Parameters:**
- x (float): The exponent.

**Returns:**
- float: The value of e^x.

**Raises:**
- TypeError: If x is not numeric.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import exp

result = exp(...)
```

---

### `expm1()`

Calculates e^x - 1 with high precision for small x.

**Parameters:**
- x (float): The exponent value.

**Returns:**
- float: The value of e^x - 1.

**Raises:**
- TypeError: If x is not numeric.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import expm1

result = expm1(...)
```

---

### `expon_dist()`

Exponential distribution PDF or CDF.

**Parameters:**
- x: The value at which to evaluate (must be >= 0).
- lambda_: Rate parameter (must be > 0).
- cumulative: If True return CDF, else PDF.

**Returns:**
- Probability value.

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If parameters are out of valid ranges.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import expon_dist

result = expon_dist(...)
```

---

### `exponential_moving_average()`

Calculates the exponential moving average (EMA) of a data series.

**Parameters:**
- data: A list of numeric values.
- span: The span window for the EMA. Must be >= 1.

**Returns:**
- A list of EMA values with the same length as *data*.

**Raises:**
- TypeError: If *data* is not a list of numbers or *span* is not int.
- ValueError: If *data* is empty or *span* < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import exponential_moving_average

result = exponential_moving_average(...)
```

---

### `f_dist()`

F-distribution PDF or CDF.

**Parameters:**
- x: The value at which to evaluate (must be >= 0).
- deg_freedom1: Numerator degrees of freedom (>= 1).
- deg_freedom2: Denominator degrees of freedom (>= 1).
- cumulative: If True return CDF, else PDF.

**Returns:**
- Probability value.

**Raises:**
- TypeError: If inputs are not of expected types.
- ValueError: If parameters are out of valid ranges.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import f_dist

result = f_dist(...)
```

---

### `f_inv()`

Inverse of the F cumulative distribution.

**Parameters:**
- probability: A probability in (0, 1).
- deg_freedom1: Numerator degrees of freedom (>= 1).
- deg_freedom2: Denominator degrees of freedom (>= 1).

**Returns:**
- The F-value.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import f_inv

result = f_inv(...)
```

---

### `factorial()`

Calculates the factorial of a non-negative integer.

**Parameters:**
- n (int): A non-negative integer.

**Returns:**
- int: The factorial of n.

**Raises:**
- TypeError: If n is not an integer.
- ValueError: If n is negative.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import factorial

result = factorial(...)
```

---

### `ffill()`

Forward-fills None values with the last non-None value.

**Parameters:**
- data: A list that may contain None values.

**Returns:**
- A new list with None values replaced by the previous non-None value.

**Raises:**
- TypeError: If input is not a list.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import ffill

result = ffill(...)
```

---

### `fillna()`

Replaces None values in a list with a specified fill value.

**Parameters:**
- data: A list that may contain None values.
- value: The replacement value (default 0).

**Returns:**
- A new list with None values replaced.

**Raises:**
- TypeError: If input is not a list.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import fillna

result = fillna(...)
```

---

### `fisher()`

Calculates the Fisher transformation.

**Parameters:**
- x: A value in the range (-1, 1).

**Returns:**
- The Fisher transformation value.

**Raises:**
- TypeError: If x is not numeric.
- ValueError: If x is not in (-1, 1).

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import fisher

result = fisher(...)
```

---

### `fisher_inv()`

Calculates the inverse Fisher transformation.

**Parameters:**
- y: A Fisher-transformed value.

**Returns:**
- The corresponding correlation coefficient in (-1, 1).

**Raises:**
- TypeError: If y is not numeric.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import fisher_inv

result = fisher_inv(...)
```

---

### `floor_significance()`

Rounds a number down to the nearest multiple of significance.

**Parameters:**
- number: The number to round.
- significance: The multiple to round down to. Default 1.

**Returns:**
- The rounded value.

**Raises:**
- ValueError: If significance is zero.

**Ejemplo:**
```python
from formulite.fxNumeric.rounding_functions import floor_significance

result = floor_significance(...)
```

---

### `forecast_linear()`

Predicts a value using linear regression.

**Parameters:**
- x: The independent value for which to predict y.
- known_y: Known dependent data values.
- known_x: Known independent data values.

**Returns:**
- The predicted y value.

**Raises:**
- TypeError: If inputs are invalid.
- ValueError: If data is insufficient.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import forecast_linear

result = forecast_linear(...)
```

---

### `fraction_to_decimal()`

Convert a fraction to its decimal representation.

**Parameters:**
- numerator: Numerator of the fraction.
- denominator: Denominator of the fraction.

**Returns:**
- Float result of numerator / denominator.

**Raises:**
- ZeroDivisionError: If denominator is 0.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import fraction_to_decimal

result = fraction_to_decimal(...)
```

---

### `frequency_bins()`

Calculates frequency distribution of data across bin boundaries.

**Parameters:**
- data: A list of numeric values.
- bins: A sorted list of bin upper boundaries.

**Returns:**
- A list of counts per bin.

**Raises:**
- TypeError: If inputs are not lists of numbers.
- ValueError: If data is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import frequency_bins

result = frequency_bins(...)
```

---

### `fvschedule()`

Calculates future value with a variable schedule of interest rates.

**Parameters:**
- principal: The initial investment amount.
- schedule: List of interest rates for each period.

**Returns:**
- The future value.

**Raises:**
- TypeError: If inputs are invalid.
- ValueError: If schedule is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import fvschedule

result = fvschedule(...)
```

---

### `gamma()`

Calculates the Gamma function Γ(x).

**Parameters:**
- x (float): A real number (not zero or a negative integer).

**Returns:**
- float: The value of the Gamma function at x.

**Raises:**
- TypeError: If x is not numeric.
- ValueError: If x is zero or a negative integer.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import gamma

result = gamma(...)
```

---

### `gauss()`

Probability that a standard normal variable falls between 0 and z.

**Parameters:**
- z: The z-score value.

**Returns:**
- float: The probability in the range (0, z).

**Raises:**
- TypeError: If z is not a number.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import gauss

result = gauss(...)
```

---

### `gcd_list()`

Calculates the GCD of a list of integers.

**Parameters:**
- numbers (List[int]): A list of integers (at least one element).

**Returns:**
- int: The GCD of all numbers in the list.

**Raises:**
- TypeError: If input is not a list or contains non-integers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import gcd_list

result = gcd_list(...)
```

---

### `geometric_mean()`

Calculates the geometric mean of a list of positive numbers.

**Parameters:**
- data: A list of positive numeric values.

**Returns:**
- The geometric mean.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty or contains non-positive values.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import geometric_mean

result = geometric_mean(...)
```

---

### `gestep()`

Tests whether a number is greater than or equal to a step value.

**Parameters:**
- number: The value to test.
- step: The threshold value (defaults to 0).

**Returns:**
- 1 if number >= step, 0 otherwise.

**Raises:**
- TypeError: If inputs are not numeric.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import gestep

result = gestep(...)
```

---

### `get_constant()`

Returns the value of a scientific or mathematical constant by name.

**Parameters:**
- name (str): The name of the constant (e.g. "pi", "avogadro", "c").

**Returns:**
- float: The numeric value of the constant.

**Raises:**
- TypeError: If name is not a string.
- KeyError: If the constant name is not found.

**Ejemplo:**
```python
from formulite.fxNumeric.constants_functions import get_constant

result = get_constant(...)
```

---

### `greatest_common_divisor()`

Calculates the greatest common divisor (GCD) of two integers.

**Parameters:**
- a (int): First integer.
- b (int): Second integer.

**Returns:**
- int: The GCD of a and b.

**Raises:**
- TypeError: If a or b are not integers.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import greatest_common_divisor

result = greatest_common_divisor(...)
```

---

### `harmonic_mean()`

Calculates the harmonic mean of a list of positive numbers.

**Parameters:**
- data: A list of positive numeric values.

**Returns:**
- The harmonic mean.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty or contains non-positive values.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import harmonic_mean

result = harmonic_mean(...)
```

---

### `hex_to_bin()`

Converts a hexadecimal string to binary.

**Parameters:**
- hexadecimal: A hexadecimal string (optional '0x' prefix).

**Returns:**
- Binary string without prefix.

**Raises:**
- TypeError: If input is not a string.
- ValueError: If the string contains invalid hex digits.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import hex_to_bin

result = hex_to_bin(...)
```

---

### `hex_to_oct()`

Converts a hexadecimal string to octal.

**Parameters:**
- hexadecimal: A hexadecimal string (optional '0x' prefix).

**Returns:**
- Octal string without prefix.

**Raises:**
- TypeError: If input is not a string.
- ValueError: If the string contains invalid hex digits.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import hex_to_oct

result = hex_to_oct(...)
```

---

### `identity_matrix()`

Creates an identity matrix of the given size.

**Parameters:**
- size: The dimension of the square identity matrix.

**Returns:**
- An identity matrix as a list of lists.

**Raises:**
- TypeError: If size is not an integer.
- ValueError: If size is less than 1.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import identity_matrix

result = identity_matrix(...)
```

---

### `int_to_roman()`

Convert a positive integer to a Roman numeral string.

**Parameters:**
- number: Integer in [1, 3999].

**Returns:**
- Roman numeral string.

**Raises:**
- ValueError: If number is outside [1, 3999].

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import int_to_roman

result = int_to_roman(...)
```

---

### `intercept()`

Calculates the y-intercept of the linear regression line.

**Parameters:**
- known_y: Dependent data values.
- known_x: Independent data values.

**Returns:**
- The y-intercept (b) of the best-fit line y = mx + b.

**Raises:**
- TypeError: If inputs are not lists of numbers.
- ValueError: If lists differ in length or have < 2 elements.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import intercept

result = intercept(...)
```

---

### `inverse_interpolate()`

Compute the interpolation factor t such that lerp(y0, y1, t) == y.

**Parameters:**
- y: The target value.
- y0: Start of the range.
- y1: End of the range.

**Returns:**
- Factor t in [0, 1] when y is within [y0, y1], or outside
- when y is extrapolated.

**Raises:**
- ValueError: If y0 == y1 (zero-length range).

**Ejemplo:**
```python
from formulite.fxNumeric.interpolation_functions import inverse_interpolate

result = inverse_interpolate(...)
```

---

### `ipmt()`

Calculates the interest portion of a payment for a specific period.

**Parameters:**
- rate: Interest rate per period.
- per: The period (1-based).
- nper: Total number of periods.
- pv: Present value.
- fv: Future value. Default 0.
- type: 0 = end of period, 1 = beginning. Default 0.

**Returns:**
- The interest portion of the payment.

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If per is out of range or nper <= 0.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import ipmt

result = ipmt(...)
```

---

### `is_even()`

Checks whether an integer is even.

**Parameters:**
- n: The integer to test.

**Returns:**
- bool: True if n is even, False otherwise.

**Raises:**
- TypeError: If n is not an integer.

**Ejemplo:**
```python
from formulite.fxNumeric.number_theory_functions import is_even

result = is_even(...)
```

---

### `is_odd()`

Checks whether an integer is odd.

**Parameters:**
- n: The integer to test.

**Returns:**
- bool: True if n is odd, False otherwise.

**Raises:**
- TypeError: If n is not an integer.

**Ejemplo:**
```python
from formulite.fxNumeric.number_theory_functions import is_odd

result = is_odd(...)
```

---

### `kurtosis()`

Calculates the kurtosis of a dataset.

**Parameters:**
- data: A list of numeric values (at least 4 elements).
- excess: If True, returns excess kurtosis (Fisher). Default True.

**Returns:**
- The kurtosis value.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list has fewer than 4 elements or zero variance.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import kurtosis

result = kurtosis(...)
```

---

### `lag()`

Shifts values forward (access previous values), like SQL LAG.

**Parameters:**
- data: A list of values.
- periods: Number of positions to lag (default 1).
- default: Value to fill for positions without a predecessor.

**Returns:**
- A list of the same length, shifted forward.

**Raises:**
- TypeError: If input is not a list.
- ValueError: If periods < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import lag

result = lag(...)
```

---

### `large()`

Returns the k-th largest value in a dataset.

**Parameters:**
- data: A list of numeric values.
- k: The rank (1 = largest, 2 = second largest, etc.).

**Returns:**
- The k-th largest value.

**Raises:**
- TypeError: If input is not a list of numbers or k is not int.
- ValueError: If the list is empty or k is out of range.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import large

result = large(...)
```

---

### `lcm()`

Calculates the Least Common Multiple of two integers.

**Parameters:**
- a (int): First integer.
- b (int): Second integer.

**Returns:**
- int: The least common multiple of a and b.

**Raises:**
- TypeError: If a or b are not integers.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import lcm

result = lcm(...)
```

---

### `lcm_list()`

Calculates the LCM of a list of integers.

**Parameters:**
- numbers (List[int]): A list of integers (at least one element).

**Returns:**
- int: The LCM of all numbers in the list.

**Raises:**
- TypeError: If input is not a list or contains non-integers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import lcm_list

result = lcm_list(...)
```

---

### `lead()`

Shifts values backward (access subsequent values), like SQL LEAD.

**Parameters:**
- data: A list of values.
- periods: Number of positions to lead (default 1).
- default: Value to fill for positions without a successor.

**Returns:**
- A list of the same length, shifted backward.

**Raises:**
- TypeError: If input is not a list.
- ValueError: If periods < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import lead

result = lead(...)
```

---

### `linear_interpolate()`

Linearly interpolate between two points.

**Parameters:**
- x: The x position to evaluate.
- x0: x coordinate of the first point.
- y0: y coordinate of the first point.
- x1: x coordinate of the second point.
- y1: y coordinate of the second point.

**Returns:**
- Interpolated y value.

**Raises:**
- ValueError: If x0 == x1 (undefined slope).

**Ejemplo:**
```python
from formulite.fxNumeric.interpolation_functions import linear_interpolate

result = linear_interpolate(...)
```

---

### `linear_interpolation()`

Estimates a Y value for *x* via piecewise linear interpolation.

**Parameters:**
- x: The X value to interpolate.
- x_points: Known X coordinates (sorted ascending).
- y_points: Known Y coordinates, same length as *x_points*.

**Returns:**
- The interpolated (or extrapolated) Y value.

**Raises:**
- TypeError: If inputs are not numeric / lists of numbers.
- ValueError: If lists are empty or have different lengths, or if
- fewer than 2 data points are provided.

**Ejemplo:**
```python
from formulite.fxNumeric.interpolation_functions import linear_interpolation

result = linear_interpolation(...)
```

---

### `list_available_constants()`

Lists all constants available in the expression evaluator.

**Returns:**
- list[str]: Sorted list of available constant names.

**Ejemplo:**
```python
from formulite.fxNumeric.calculator_functions import list_available_constants

result = list_available_constants(...)
```

---

### `list_available_functions()`

Lists all functions available in the expression evaluator.

**Returns:**
- list[str]: Sorted list of available function names.

**Ejemplo:**
```python
from formulite.fxNumeric.calculator_functions import list_available_functions

result = list_available_functions(...)
```

---

### `list_constants()`

Lists all available scientific and mathematical constants.

**Parameters:**
- category (Optional[str]): Filter by "math" or "physical".
- None returns all constants.

**Returns:**
- list[dict[str, str]]: List of constant info dicts with keys
- name, symbol, value, description.

**Raises:**
- ValueError: If category is not "math", "physical", or None.

**Ejemplo:**
```python
from formulite.fxNumeric.constants_functions import list_constants

result = list_constants(...)
```

---

### `log_gamma()`

Calculates the natural logarithm of the absolute value of Γ(x).

**Parameters:**
- x (float): A positive real number.

**Returns:**
- float: The natural logarithm of the absolute Gamma function at x.

**Raises:**
- TypeError: If x is not numeric.
- ValueError: If x is not positive.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import log_gamma

result = log_gamma(...)
```

---

### `map_range()`

Re-map a value from one range to another (Arduino-style).

**Parameters:**
- value: Input value.
- in_min: Lower bound of the input range.
- in_max: Upper bound of the input range.
- out_min: Lower bound of the output range.
- out_max: Upper bound of the output range.

**Returns:**
- Value mapped to the output range.

**Raises:**
- ValueError: If in_min == in_max.

**Ejemplo:**
```python
from formulite.fxNumeric.interpolation_functions import map_range

result = map_range(...)
```

---

### `matrix_determinant()`

Computes the determinant of a square matrix.

**Parameters:**
- matrix: A square matrix represented as a list of lists.

**Returns:**
- The determinant value.

**Raises:**
- TypeError: If input is not a list of lists of numbers.
- ValueError: If the matrix is not square or is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import matrix_determinant

result = matrix_determinant(...)
```

---

### `matrix_inverse()`

Computes the inverse of a square matrix.

**Parameters:**
- matrix: A square, non-singular matrix as a list of lists.

**Returns:**
- The inverse matrix as a list of lists of floats.

**Raises:**
- TypeError: If input is not a list of lists of numbers.
- ValueError: If the matrix is not square, empty, or singular.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import matrix_inverse

result = matrix_inverse(...)
```

---

### `matrix_multiply()`

Multiplies two matrices.

**Parameters:**
- matrix_a: First matrix (m × n).
- matrix_b: Second matrix (n × p).

**Returns:**
- The resulting matrix (m × p) as a list of lists.

**Raises:**
- TypeError: If inputs are not lists of lists of numbers.
- ValueError: If matrices are empty or dimensions are incompatible.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import matrix_multiply

result = matrix_multiply(...)
```

---

### `mean_squared_error()`

Calculates the mean squared error (MSE) between observed and predicted values.

**Parameters:**
- observed: A list of actual values.
- predicted: A list of predicted values.

**Returns:**
- The mean squared error.

**Raises:**
- TypeError: If inputs are not lists of numbers.
- ValueError: If lists differ in length or are empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import mean_squared_error

result = mean_squared_error(...)
```

---

### `median_absolute_deviation()`

Calculates the Median Absolute Deviation (MAD).

**Parameters:**
- data: A list of numeric values.

**Returns:**
- The MAD value.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import median_absolute_deviation

result = median_absolute_deviation(...)
```

---

### `mirr()`

Calculates the Modified Internal Rate of Return (MIRR).

**Parameters:**
- cash_flows: Series of cash flows (first is typically negative).
- finance_rate: Interest rate paid on negative cash flows.
- reinvest_rate: Interest rate earned on positive cash flows.

**Returns:**
- The modified internal rate of return.

**Raises:**
- TypeError: If inputs are invalid types.
- ValueError: If cash_flows is empty or has no sign change.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import mirr

result = mirr(...)
```

---

### `modulo()`

Returns the remainder after dividing number by divisor.

**Parameters:**
- number: The dividend.
- divisor: The divisor (must not be zero).

**Returns:**
- The remainder of number / divisor.

**Raises:**
- ZeroDivisionError: If divisor is zero.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import modulo

result = modulo(...)
```

---

### `multinomial_coefficient()`

Compute the multinomial coefficient n! / (k1! * k2! * ... * km!).

**Parameters:**
- *args: Non-negative integers k1, k2, ..., km.

**Returns:**
- Multinomial coefficient as integer.

**Raises:**
- ValueError: If any argument is negative.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import multinomial_coefficient

result = multinomial_coefficient(...)
```

---

### `nominal()`

Calculates the nominal annual interest rate from effective rate.

**Parameters:**
- effect_rate: Effective annual interest rate.
- npery: Number of compounding periods per year.

**Returns:**
- The nominal annual rate.

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If effect_rate <= 0 or npery < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import nominal

result = nominal(...)
```

---

### `norm_dist()`

Normal (Gaussian) distribution PDF or CDF.

**Parameters:**
- x: The value at which to evaluate.
- mean: Distribution mean. Default 0.
- std_dev: Standard deviation (must be > 0). Default 1.
- cumulative: If True return CDF, else PDF.

**Returns:**
- Probability value.

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If std_dev <= 0.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import norm_dist

result = norm_dist(...)
```

---

### `norm_inv()`

Inverse of the normal cumulative distribution (quantile function).

**Parameters:**
- probability: A probability in (0, 1).
- mean: Distribution mean. Default 0.
- std_dev: Standard deviation (must be > 0). Default 1.

**Returns:**
- The value x such that P(X <= x) = probability.

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If probability is not in (0, 1) or std_dev <= 0.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import norm_inv

result = norm_inv(...)
```

---

### `norm_s_dist()`

Standard normal distribution (mean=0, std=1).

**Parameters:**
- z: The z-value.
- cumulative: If True return CDF, else PDF.

**Returns:**
- Probability value.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import norm_s_dist

result = norm_s_dist(...)
```

---

### `norm_s_inv()`

Inverse of the standard normal cumulative distribution.

**Parameters:**
- probability: A probability in (0, 1).

**Returns:**
- The z-value.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import norm_s_inv

result = norm_s_inv(...)
```

---

### `normalize_list()`

Normalizes a list to the [0, 1] range using min-max scaling.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- A new list with values scaled to [0, 1]. If all values are equal,
- returns a list of 0.0.

**Raises:**
- TypeError: If *data* is not a list of numbers.
- ValueError: If *data* is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.interpolation_functions import normalize_list

result = normalize_list(...)
```

---

### `number_to_base()`

Converts a decimal integer to a string in the specified base.

**Parameters:**
- number: The non-negative integer to convert.
- radix: The target base (2 to 36).
- min_length: Minimum length of the result, zero-padded if needed.

**Returns:**
- The string representation of the number in the given base.

**Raises:**
- TypeError: If number or radix are not integers.
- ValueError: If number is negative or radix is outside 2–36.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import number_to_base

result = number_to_base(...)
```

---

### `number_to_words()`

Convert an integer to its written-word representation.

**Parameters:**
- number: Integer to convert.
- lang: Language code (``'en'`` or ``'es'``). Defaults to ``'en'``.

**Returns:**
- Written representation as string.

**Raises:**
- ValueError: If number is out of supported range or lang is unsupported.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import number_to_words

result = number_to_words(...)
```

---

### `oct_to_bin()`

Converts an octal string to binary.

**Parameters:**
- octal: An octal string (optional '0o' prefix).

**Returns:**
- Binary string without prefix.

**Raises:**
- TypeError: If input is not a string.
- ValueError: If the string contains invalid octal digits.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import oct_to_bin

result = oct_to_bin(...)
```

---

### `oct_to_hex()`

Converts an octal string to hexadecimal.

**Parameters:**
- octal: An octal string (optional '0o' prefix).

**Returns:**
- Uppercase hexadecimal string without prefix.

**Raises:**
- TypeError: If input is not a string.
- ValueError: If the string contains invalid octal digits.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import oct_to_hex

result = oct_to_hex(...)
```

---

### `odd()`

Rounds a number up to the nearest odd integer.

**Parameters:**
- number: The number to round.

**Returns:**
- The nearest odd integer away from zero.

**Ejemplo:**
```python
from formulite.fxNumeric.rounding_functions import odd

result = odd(...)
```

---

### `outliers_iqr()`

Detects outliers using the Interquartile Range (IQR) method.

**Parameters:**
- data: A list of numeric values (at least 4 elements).
- factor: Multiplier for the IQR to set the fences (default 1.5).

**Returns:**
- A list containing only the outlier values (preserving order).

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list has fewer than 4 elements or factor <= 0.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import outliers_iqr

result = outliers_iqr(...)
```

---

### `pct_change()`

Calculates the percentage change between consecutive elements.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- A list of the same length with fractional changes (0.1 = 10 %).

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import pct_change

result = pct_change(...)
```

---

### `pduration()`

Calculates the number of periods to reach a target future value.

**Parameters:**
- rate: Interest rate per period (must be > 0).
- pv: Present value (must be > 0).
- fv: Target future value (must be > 0).

**Returns:**
- Number of periods needed.

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If rate, pv, or fv are not positive.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import pduration

result = pduration(...)
```

---

### `percent_change()`

Calculates the percentage change between two values.

**Parameters:**
- old_value: The original value (must not be zero).
- new_value: The new value.

**Returns:**
- The percentage change as a float (e.g. 50.0 for a 50% increase).

**Raises:**
- ValueError: If old_value is zero.

**Ejemplo:**
```python
from formulite.fxNumeric.format_functions import percent_change

result = percent_change(...)
```

---

### `percent_of()`

Calculates what percentage ``part`` is of ``whole``.

**Parameters:**
- part: The partial value.
- whole: The total value (must not be zero).

**Returns:**
- The percentage as a float.

**Raises:**
- ValueError: If whole is zero.

**Ejemplo:**
```python
from formulite.fxNumeric.format_functions import percent_of

result = percent_of(...)
```

---

### `permutations()`

Calculates the number of permutations P(n, k).

**Parameters:**
- n (int): Total number of items (non-negative).
- k (int): Number of items to arrange (0 ≤ k ≤ n).

**Returns:**
- int: The number of permutations.

**Raises:**
- TypeError: If n or k are not integers.
- ValueError: If n or k are negative, or if k > n.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import permutations

result = permutations(...)
```

---

### `permutations_with_repetition()`

Returns the number of permutations with repetition.

**Parameters:**
- n: The number of distinct items.
- k: The number of items to choose.

**Returns:**
- n raised to the power k.

**Raises:**
- TypeError: If inputs are not integers.
- ValueError: If n or k is negative, or n is 0 and k > 0.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import permutations_with_repetition

result = permutations_with_repetition(...)
```

---

### `phi()`

Standard normal probability density function φ(x).

**Parameters:**
- x: The point to evaluate.

**Returns:**
- float: The PDF value at x.

**Raises:**
- TypeError: If x is not a number.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import phi

result = phi(...)
```

---

### `piecewise_interpolate()`

Linearly interpolate over a piecewise-defined dataset.

**Parameters:**
- x: The x position to evaluate.
- xs: Sorted list of x breakpoints (at least 2).
- ys: Corresponding y values (same length as xs).

**Returns:**
- Interpolated y value.

**Raises:**
- ValueError: If xs and ys have different lengths or fewer than 2 points.

**Ejemplo:**
```python
from formulite.fxNumeric.interpolation_functions import piecewise_interpolate

result = piecewise_interpolate(...)
```

---

### `poisson_dist()`

Poisson distribution PMF or CDF.

**Parameters:**
- x: Number of events.
- mean: Expected number of events (lambda, must be > 0).
- cumulative: If True return CDF, else PMF.

**Returns:**
- Probability value.

**Raises:**
- TypeError: If inputs are not of expected types.
- ValueError: If parameters are out of valid ranges.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import poisson_dist

result = poisson_dist(...)
```

---

### `ppmt()`

Calculates the principal portion of a payment for a specific period.

**Parameters:**
- rate: Interest rate per period.
- per: The period (1-based).
- nper: Total number of periods.
- pv: Present value.
- fv: Future value. Default 0.
- type: 0 = end of period, 1 = beginning. Default 0.

**Returns:**
- The principal portion of the payment.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import ppmt

result = ppmt(...)
```

---

### `probability_range()`

Sum of probabilities for values within a range.

**Parameters:**
- x_range: Array of discrete values.
- prob_range: Corresponding probabilities (must sum to ≈ 1).
- lower_limit: Lower bound of the range.
- upper_limit: Upper bound (defaults to lower_limit for exact match).

**Returns:**
- float: Sum of matching probabilities.

**Raises:**
- TypeError: If inputs are not lists of numbers.
- ValueError: If arrays differ in length, probabilities are negative,
- or they don't sum to approximately 1.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import probability_range

result = probability_range(...)
```

---

### `product_list()`

Calculates the product of all values in a list.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- The product of all values.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import product_list

result = product_list(...)
```

---

### `quotient()`

Return the integer portion of a division (truncated toward zero).

**Parameters:**
- dividend: The number to be divided.
- divisor: The number to divide by.

**Returns:**
- Integer result of division truncated toward zero.

**Raises:**
- ZeroDivisionError: If divisor is 0.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import quotient

result = quotient(...)
```

---

### `r_squared()`

Calculates the coefficient of determination (R²) for a linear regression.

**Parameters:**
- known_y: Dependent (observed) data values.
- known_x: Independent data values.

**Returns:**
- The R² value between 0 and 1.

**Raises:**
- TypeError: If inputs are not lists of numbers.
- ValueError: If lists differ in length, have < 2 elements, or if y
- has zero variance.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import r_squared

result = r_squared(...)
```

---

### `random_array()`

Returns an array of random numbers.

**Parameters:**
- rows: Number of rows (default 1).
- columns: Number of columns (default 1).
- min_value: Minimum value (default 0.0).
- max_value: Maximum value (default 1.0).
- whole_number: If True, return integers; if False, return floats.

**Returns:**
- A list of lists of random numbers.

**Raises:**
- ValueError: If rows or columns < 1, or min_value > max_value.

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_array

result = random_array(...)
```

---

### `random_bool()`

Return a random boolean with the given probability of True.

**Parameters:**
- probability: Probability of returning True, in [0, 1]. Defaults to 0.5.

**Returns:**
- True with the given probability, False otherwise.

**Raises:**
- ValueError: If probability is not in [0, 1].

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_bool

result = random_bool(...)
```

---

### `random_choice()`

Return a random element from a non-empty sequence.

**Parameters:**
- items: Non-empty sequence to choose from.

**Returns:**
- A randomly selected element.

**Raises:**
- ValueError: If items is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_choice

result = random_choice(...)
```

---

### `random_float()`

Return a random float in the range [low, high).

**Parameters:**
- low: Lower bound (inclusive). Defaults to 0.0.
- high: Upper bound (exclusive). Defaults to 1.0.

**Returns:**
- Random float between low (inclusive) and high (exclusive).

**Raises:**
- ValueError: If low >= high.

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_float

result = random_float(...)
```

---

### `random_gaussian()`

Return a random float from a Gaussian (normal) distribution.

**Parameters:**
- mean: Mean of the distribution. Defaults to 0.0.
- std: Standard deviation. Defaults to 1.0.

**Returns:**
- Random float drawn from N(mean, std^2).

**Raises:**
- ValueError: If std < 0.

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_gaussian

result = random_gaussian(...)
```

---

### `random_int()`

Return a random integer in the inclusive range [low, high].

**Parameters:**
- low: Lower bound (inclusive).
- high: Upper bound (inclusive).

**Returns:**
- Random integer between low and high.

**Raises:**
- ValueError: If low > high.

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_int

result = random_int(...)
```

---

### `random_sample()`

Return k unique elements chosen from the sequence without replacement.

**Parameters:**
- items: Sequence to sample from.
- k: Number of elements to sample.

**Returns:**
- List of k unique randomly selected elements.

**Raises:**
- ValueError: If k > len(items) or k < 0.

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_sample

result = random_sample(...)
```

---

### `random_shuffle()`

Return a new list with the elements randomly shuffled.

**Parameters:**
- items: Sequence to shuffle.

**Returns:**
- New list with elements in random order.

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_shuffle

result = random_shuffle(...)
```

---

### `random_uuid()`

Generate a random UUID version 4 as a string.

**Returns:**
- UUID v4 string (e.g. ``'550e8400-e29b-41d4-a716-446655440000'``).

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_uuid

result = random_uuid(...)
```

---

### `random_weighted_choice()`

Return a random element using weighted probabilities.

**Parameters:**
- items: Non-empty sequence of items.
- weights: Corresponding positive weights (same length as items).

**Returns:**
- A single randomly selected element.

**Raises:**
- ValueError: If items is empty or lengths mismatch.

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import random_weighted_choice

result = random_weighted_choice(...)
```

---

### `rank()`

Assigns a rank to each value in a list.

**Parameters:**
- data: A list of numeric values.
- method: How to handle ties — ``"average"``, ``"min"``, ``"max"``,
- ``"dense"``, or ``"ordinal"``.
- ascending: If ``True`` (default) smallest value gets rank 1.

**Returns:**
- A list of floats with the rank for each position.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty or method is invalid.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import rank

result = rank(...)
```

---

### `rolling_mean()`

Calculates the rolling (moving) average over a fixed window size.

**Parameters:**
- data: A list of numeric values.
- window: Number of consecutive elements per window (must be >= 1).

**Returns:**
- A list of the same length; each entry is the mean of the preceding
- *window* elements or ``None`` when not enough data exists.

**Raises:**
- TypeError: If input is not a list of numbers or window is not int.
- ValueError: If the list is empty or window < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import rolling_mean

result = rolling_mean(...)
```

---

### `rolling_median()`

Calculates a rolling (moving) median over a dataset.

**Parameters:**
- data: A list of numeric values.
- window: The size of the rolling window (must be >= 1).

**Returns:**
- A list of the same length as ``data`` with rolling median values
- (or None where the window is incomplete).

**Raises:**
- TypeError: If data is not a list or contains non-numeric values.
- ValueError: If window is less than 1 or data is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import rolling_median

result = rolling_median(...)
```

---

### `rolling_std()`

Calculates the rolling (moving) standard deviation over a fixed window.

**Parameters:**
- data: A list of numeric values.
- window: Number of consecutive elements per window (>= 2).
- sample: If True, uses sample std dev (n-1); otherwise population.

**Returns:**
- A list of the same length; each entry is the standard deviation of
- the preceding *window* elements or ``None``.

**Raises:**
- TypeError: If input is not a list of numbers or window is not int.
- ValueError: If the list is empty or window < 2.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import rolling_std

result = rolling_std(...)
```

---

### `rolling_sum()`

Calculates the rolling (moving) sum over a fixed window size.

**Parameters:**
- data: A list of numeric values.
- window: Number of consecutive elements per window (must be >= 1).

**Returns:**
- A list of the same length; each entry is the sum of the preceding
- *window* elements or ``None`` when not enough data exists.

**Raises:**
- TypeError: If input is not a list of numbers or window is not int.
- ValueError: If the list is empty or window < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import rolling_sum

result = rolling_sum(...)
```

---

### `roman_to_int()`

Convert a Roman numeral string to an integer.

**Parameters:**
- roman: String with valid Roman numeral characters (I, V, X, L, C, D, M).

**Returns:**
- Integer value.

**Raises:**
- ValueError: If roman contains invalid characters.

**Ejemplo:**
```python
from formulite.fxNumeric.conversion_functions import roman_to_int

result = roman_to_int(...)
```

---

### `series_sum()`

Compute a power series sum: sum(a_i * x^(n + i*m)).

**Parameters:**
- x: Base value.
- n: Initial power of x.
- m: Step increment for each term's power.
- coefficients: List of coefficients [a_0, a_1, ...].

**Returns:**
- Sum of the power series.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import series_sum

result = series_sum(...)
```

---

### `set_random_seed()`

Set the random seed for reproducible generation.

**Parameters:**
- seed: Integer seed value.

**Returns:**
- None.

**Ejemplo:**
```python
from formulite.fxNumeric.random_functions import set_random_seed

result = set_random_seed(...)
```

---

### `sign()`

Returns the sign of a number as -1, 0, or 1.

**Parameters:**
- x (Union[int, float]): The number to inspect.

**Returns:**
- int: -1, 0, or 1.

**Raises:**
- TypeError: If x is not numeric.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import sign

result = sign(...)
```

---

### `skewness()`

Calculates the skewness of a dataset.

**Parameters:**
- data: A list of numeric values (at least 3 elements).

**Returns:**
- The skewness value.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list has fewer than 3 elements or zero variance.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import skewness

result = skewness(...)
```

---

### `slope()`

Calculates the slope of the linear regression line.

**Parameters:**
- known_y: Dependent data values.
- known_x: Independent data values.

**Returns:**
- The slope (m) of the best-fit line y = mx + b.

**Raises:**
- TypeError: If inputs are not lists of numbers.
- ValueError: If lists differ in length, have < 2 elements, or x has zero variance.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import slope

result = slope(...)
```

---

### `small()`

Returns the k-th smallest value in a dataset.

**Parameters:**
- data: A list of numeric values.
- k: The rank (1 = smallest, 2 = second smallest, etc.).

**Returns:**
- The k-th smallest value.

**Raises:**
- TypeError: If input is not a list of numbers or k is not int.
- ValueError: If the list is empty or k is out of range.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import small

result = small(...)
```

---

### `spearman_correlation()`

Calculates the Spearman rank correlation coefficient.

**Parameters:**
- data1: The first list of numeric values.
- data2: The second list of numeric values.

**Returns:**
- The Spearman correlation coefficient between -1 and 1.

**Raises:**
- TypeError: If inputs are not lists of numbers.
- ValueError: If lists differ in length or have fewer than 3 elements.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import spearman_correlation

result = spearman_correlation(...)
```

---

### `sqrt_pi()`

Calculates the square root of (number * pi).

**Parameters:**
- number: A non-negative number.

**Returns:**
- sqrt(number * pi).

**Raises:**
- ValueError: If number is negative.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import sqrt_pi

result = sqrt_pi(...)
```

---

### `standard_error()`

Calculates the standard error of the mean (SEM).

**Parameters:**
- data: A list of numeric values (at least 2 elements).

**Returns:**
- The standard error of the mean.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list has fewer than 2 elements.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import standard_error

result = standard_error(...)
```

---

### `standard_error_estimate()`

Returns the standard error of the predicted y-value for each x.

**Parameters:**
- known_y: The dependent data (observed y-values).
- known_x: The independent data (observed x-values).

**Returns:**
- The standard error of the estimate.

**Raises:**
- ValueError: If arrays differ in length, have fewer than 3 points,
- or are empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import standard_error_estimate

result = standard_error_estimate(...)
```

---

### `sum_list()`

Calculates the sum of all values in a list.

**Parameters:**
- data: A list of numeric values.

**Returns:**
- The sum of all values.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import sum_list

result = sum_list(...)
```

---

### `sum_product()`

Return the sum of element-wise products of two lists.

**Parameters:**
- list1: First numeric list.
- list2: Second numeric list (same length).

**Returns:**
- Sum of list1[i] * list2[i] for all i.

**Raises:**
- ValueError: If lists have different lengths.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import sum_product

result = sum_product(...)
```

---

### `sum_x2my2()`

Returns the sum of the difference of squares of corresponding values.

**Parameters:**
- array_x: First array of numbers.
- array_y: Second array of numbers (same length as array_x).

**Returns:**
- The sum of xᵢ² - yᵢ² for each pair.

**Raises:**
- ValueError: If arrays have different lengths or are empty.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import sum_x2my2

result = sum_x2my2(...)
```

---

### `sum_x2py2()`

Returns the sum of the sum of squares of corresponding values.

**Parameters:**
- array_x: First array of numbers.
- array_y: Second array of numbers (same length as array_x).

**Returns:**
- The sum of xᵢ² + yᵢ² for each pair.

**Raises:**
- ValueError: If arrays have different lengths or are empty.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import sum_x2py2

result = sum_x2py2(...)
```

---

### `sum_xmy2()`

Returns the sum of squares of differences of corresponding values.

**Parameters:**
- array_x: First array of numbers.
- array_y: Second array of numbers (same length as array_x).

**Returns:**
- The sum of (xᵢ - yᵢ)² for each pair.

**Raises:**
- ValueError: If arrays have different lengths or are empty.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import sum_xmy2

result = sum_xmy2(...)
```

---

### `syd()`

Calculates depreciation using the sum-of-years' digits method.

**Parameters:**
- cost: Initial cost of the asset.
- salvage: Salvage value at end of life.
- life: Useful life in periods.
- per: Period for which to calculate (1-based).

**Returns:**
- Depreciation for the specified period.

**Raises:**
- TypeError: If inputs are not numeric.
- ValueError: If parameters are out of valid ranges.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import syd

result = syd(...)
```

---

### `t_dist()`

Student's t-distribution PDF or CDF.

**Parameters:**
- x: The value at which to evaluate.
- deg_freedom: Degrees of freedom (must be >= 1).
- cumulative: If True return CDF, else PDF.

**Returns:**
- Probability value.

**Raises:**
- TypeError: If inputs are not of expected types.
- ValueError: If deg_freedom < 1.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import t_dist

result = t_dist(...)
```

---

### `t_inv()`

Inverse of the Student's t cumulative distribution.

**Parameters:**
- probability: A probability in (0, 1).
- deg_freedom: Degrees of freedom (must be >= 1).

**Returns:**
- The t-value.

**Ejemplo:**
```python
from formulite.fxNumeric.distribution_functions import t_inv

result = t_inv(...)
```

---

### `trimmed_mean()`

Calculates the mean excluding a percentage of outliers from each end.

**Parameters:**
- data: A list of numeric values.
- percent: Fraction of data to exclude from each end (0 to 0.5).

**Returns:**
- The trimmed mean.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty or percent is out of range.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import trimmed_mean

result = trimmed_mean(...)
```

---

### `weighted_mean()`

Calculates the weighted arithmetic mean of a list of numbers.

**Parameters:**
- data: A list of numeric values.
- weights: A list of corresponding weights (must be positive).

**Returns:**
- The weighted mean.

**Raises:**
- TypeError: If inputs are not lists of numbers.
- ValueError: If lists differ in length, are empty, or weights are non-positive.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import weighted_mean

result = weighted_mean(...)
```

---

### `weighted_median()`

Calculates the weighted median of a dataset.

**Parameters:**
- data: A list of numeric values.
- weights: A list of corresponding positive weights.

**Returns:**
- The weighted median value.

**Raises:**
- TypeError: If inputs are not lists of numbers.
- ValueError: If lists differ in length, are empty, or weights
- are non-positive.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import weighted_median

result = weighted_median(...)
```

---

### `winsorize()`

Replaces extreme values with the corresponding percentile boundaries.

**Parameters:**
- data: A list of numeric values.
- percent: Fraction of data to replace on each end (0 to 0.5 exclusive).

**Returns:**
- A new list with extreme values capped.

**Raises:**
- TypeError: If input is not a list of numbers.
- ValueError: If the list is empty or percent is out of range.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import winsorize

result = winsorize(...)
```

---

### `xirr()`

Calculates Internal Rate of Return for irregularly spaced cash flows.

**Parameters:**
- values: Cash flow amounts.
- dates: Corresponding dates (datetime objects).
- guess: Initial rate guess. Default 0.1.

**Returns:**
- The XIRR rate.

**Raises:**
- TypeError: If inputs are invalid types.
- ValueError: If convergence fails or inputs are invalid.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import xirr

result = xirr(...)
```

---

### `xnpv()`

Calculates Net Present Value for irregularly spaced cash flows.

**Parameters:**
- rate: Discount rate.
- values: Cash flow amounts.
- dates: Corresponding dates (datetime objects).

**Returns:**
- Net present value.

**Raises:**
- TypeError: If inputs are invalid types.
- ValueError: If lengths differ or lists are empty.

**Ejemplo:**
```python
from formulite.fxNumeric.finance_functions import xnpv

result = xnpv(...)
```

---

### `z_score()`

Calculates the z-score (standard score) of a value relative to a dataset.

**Parameters:**
- value: The value to standardize.
- data: The reference dataset.

**Returns:**
- The z-score (number of standard deviations from the mean).

**Raises:**
- TypeError: If inputs are invalid.
- ValueError: If data has fewer than 2 elements or zero variance.

**Ejemplo:**
```python
from formulite.fxNumeric.statistics_functions import z_score

result = z_score(...)
```

---


### `fibonacci()`

Returns the n-th Fibonacci number (0-indexed).

**Parameters:**
- n: The position in the Fibonacci sequence (must be >= 0).

**Returns:**
- The n-th Fibonacci number.

**Ejemplo:**
```python
from formulite.fxNumeric.arithmetic_functions import fibonacci

result = fibonacci(...)
```

---

