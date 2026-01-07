# FormuLite - fxNumeric Module

Documentation of the available functions in the `fxNumeric` module of FormuLite.

## Overview

The fxNumeric module provides comprehensive numeric manipulation functions for FormuLite, including:
- **Arithmetic Operations**: Logarithms, powers, roots
- **Numeric Conversions**: Type conversions, base conversions, formatting
- **Numeric Operations**: Rounding, scaling, comparisons, precision handling
- **Statistical Functions**: Mean, median, correlation, variance
- **Trigonometric Functions**: Standard and hyperbolic trig functions
- **Financial Functions**: Present value, future value, payments, depreciation

## Module Structure

- **numeric_arithmetic.py**: Basic arithmetic and logarithmic operations
- **numeric_convertions.py**: Functions for converting between numeric types and formats
- **numeric_operations.py**: Advanced numeric operations, rounding, and formatting
- **numeric_statistics.py**: Statistical calculations and data analysis functions
- **numeric_trigonometry.py**: Trigonometric and hyperbolic functions
- **numeric_finance.py**: Financial calculations and investment functions

---

## Table of Contents

- [Function Categories](#function-categories)
  - [Arithmetic Operations](#arithmetic-operations)
  - [Numeric Conversions](#numeric-conversions)
  - [Numeric Operations](#numeric-operations)
  - [Statistical Functions](#statistical-functions)
  - [Trigonometric Functions](#trigonometric-functions)
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

### Numeric Operations
- [is_numeric_type()](#is_numeric_type) - Verifies if value is numeric type
- [is_prime()](#is_prime) - Verifies if number is prime
- [get_primes_up_to()](#get_primes_up_to) - Generates list of primes up to limit using sieve
- [truncate_float()](#truncate_float) - Truncates float eliminating decimal part towards zero
- [round_to_n_decimals()](#round_to_n_decimals) - Rounds float to specific number of decimal places
- [round_up()](#round_up) - Rounds float upward to nearest integer ceiling
- [round_down()](#round_down) - Rounds float downward to nearest integer floor
- [explicit_truncate()](#explicit_truncate) - Eliminates decimal part without rounding towards zero
- [manual_round_and_cast()](#manual_round_and_cast) - Performs manual rounding to nearest integer then casts
- [manual_round_up_to_int()](#manual_round_up_to_int) - Rounds float to nearest integer always upwards
- [manual_round_down_to_int()](#manual_round_down_to_int) - Rounds float to nearest integer always downwards
- [round_half_even()](#round_half_even) - Performs banker's rounding with ROUND_HALF_EVEN policy
- [round_to_nearest_multiple()](#round_to_nearest_multiple) - Rounds number to nearest multiple of base
- [add_with_exact_precision()](#add_with_exact_precision) - Adds two numbers using Decimal for exact precision
- [format_with_leading_zeros()](#format_with_leading_zeros) - Formats integer with leading zeros to width
- [format_as_percentage()](#format_as_percentage) - Formats float as percentage string with decimals
- [format_as_scientific_notation()](#format_as_scientific_notation) - Formats float in scientific notation
- [force_float_division()](#force_float_division) - Performs division ensuring float result always
- [normalize_to_0_1_range()](#normalize_to_0_1_range) - Normalizes number to scale within 0-1 range
- [scale_to_new_range()](#scale_to_new_range) - Scales number from original range to new range
- [clip_number()](#clip_number) - Forces number within specific minimum-maximum range
- [reduce_to_modulo_range()](#reduce_to_modulo_range) - Converts value to cyclic range using modulo
- [quantize_number()](#quantize_number) - Quantizes number to discrete multiples of step
- [add_bool_to_int()](#add_bool_to_int) - Adds boolean value to integer treating True=1
- [safe_sum_with_none()](#safe_sum_with_none) - Adds two numbers safely treating None as zero
- [count_true_with_sum()](#count_true_with_sum) - Counts True values in boolean list using sum
- [true_division()](#true_division) - Performs floating-point division always returning float
- [floor_division()](#floor_division) - Performs integer division truncating result downwards
- [safe_division_for_context()](#safe_division_for_context) - Performs division selecting float or integer based context
- [compare_floats_with_tolerance()](#compare_floats_with_tolerance) - Compares floats within relative and absolute tolerance

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
- [bin_to_int()](#bin_to_int) - Converts binary string to decimal integer
- [bool_to_float()](#bool_to_float) - Converts boolean to float, True=1.0 False=0.0
- [bool_to_int()](#bool_to_int) - Converts boolean to integer, True=1 False=0

**C**
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
- [compare_floats_with_tolerance()](#compare_floats_with_tolerance) - Compares floats within relative and absolute tolerance
- [convert_string_to_float_with_locale()](#convert_string_to_float_with_locale) - Converts numeric string to float using locale separators
- [cosecant()](#cosecant) - Calculates cosecant of angle one over sine
- [cosine()](#cosine) - Calculates cosine of angle in radians
- [cotangent()](#cotangent) - Calculates cotangent of angle one over tangent
- [count_true_with_sum()](#count_true_with_sum) - Counts True values in boolean list using sum
- [cube_root()](#cube_root) - Calculates cube root of a number

**D**
- [db()](#db) - Calculates depreciation using fixed-declining balance method
- [degrees_to_radians()](#degrees_to_radians) - Converts angle from degrees to radians

**E**
- [explicit_truncate()](#explicit_truncate) - Eliminates decimal part without rounding towards zero

**F**
- [float_to_int_truncated()](#float_to_int_truncated) - Converts float to integer truncating decimals towards zero
- [floor_division()](#floor_division) - Performs integer division truncating result downwards
- [force_float_division()](#force_float_division) - Performs division ensuring float result always
- [format_as_percentage()](#format_as_percentage) - Formats float as percentage string with decimals
- [format_as_scientific_notation()](#format_as_scientific_notation) - Formats float in scientific notation
- [format_with_leading_zeros()](#format_with_leading_zeros) - Formats integer with leading zeros to width
- [future_value()](#future_value) - Calculates future value of investment with periodic payments

**G**
- [get_primes_up_to()](#get_primes_up_to) - Generates list of primes up to limit using sieve

**H**
- [hex_to_int()](#hex_to_int) - Converts hexadecimal string to decimal integer
- [hyperbolic_cosine()](#hyperbolic_cosine) - Calculates hyperbolic cosine of value
- [hyperbolic_sine()](#hyperbolic_sine) - Calculates hyperbolic sine of value
- [hyperbolic_tangent()](#hyperbolic_tangent) - Calculates hyperbolic tangent of value
- [hypotenuse()](#hypotenuse) - Calculates Euclidean norm length of right triangle hypotenuse

**I**
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
- [irr()](#irr) - Calculates internal rate of return for cash flows
- [is_numeric_type()](#is_numeric_type) - Verifies if value is numeric type
- [is_prime()](#is_prime) - Verifies if number is prime

**J**

**K**

**L**
- [log1p()](#log1p) - Calculates natural logarithm of 1+x with high precision near zero
- [log_base_n()](#log_base_n) - Calculates logarithm of a number to specified base N

**M**
- [manual_round_and_cast()](#manual_round_and_cast) - Performs manual rounding to nearest integer then casts
- [manual_round_down_to_int()](#manual_round_down_to_int) - Rounds float to nearest integer always downwards
- [manual_round_up_to_int()](#manual_round_up_to_int) - Rounds float to nearest integer always upwards

**N**
- [natural_log()](#natural_log) - Calculates natural logarithm base e of a positive number
- [normalize_to_0_1_range()](#normalize_to_0_1_range) - Normalizes number to scale within 0-1 range
- [nper()](#nper) - Calculates number of periods for investment with payments
- [npv()](#npv) - Calculates net present value of investment cash flows
- [nth_root()](#nth_root) - Calculates nth root of a number
- [number_to_bool()](#number_to_bool) - Converts number to boolean, zero becomes False
- [number_to_complex()](#number_to_complex) - Converts number to complex with zero imaginary part
- [number_to_string()](#number_to_string) - Converts integer or float to string representation

**O**
- [octal_to_int()](#octal_to_int) - Converts octal string to decimal integer

**P**
- [pmt()](#pmt) - Calculates payment for loan with constant payments rate
- [power()](#power) - Calculates value of base raised to specified exponent
- [present_value()](#present_value) - Calculates present value of future payments series

**Q**
- [quantize_number()](#quantize_number) - Quantizes number to discrete multiples of step

**R**
- [radians_to_degrees()](#radians_to_degrees) - Converts angle from radians to degrees
- [rate()](#rate) - Calculates interest rate per period using iteration
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
- [sine()](#sine) - Calculates sine of angle in radians
- [sln()](#sln) - Calculates straight-line depreciation of asset per period
- [square_root()](#square_root) - Calculates square root of a non-negative number
- [sum_of_squares()](#sum_of_squares) - Calculates sum of squares of list values

**T**
- [tangent()](#tangent) - Calculates tangent of angle in radians
- [to_js_safe_integer()](#to_js_safe_integer) - Converts number to JavaScript safe integer range
- [true_division()](#true_division) - Performs floating-point division always returning float
- [truncate_float()](#truncate_float) - Truncates float eliminating decimal part towards zero

**U**

**V**

**W**

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
from formulite.fxNumeric.numeric_arithmetic import natural_log

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
from formulite.fxNumeric.numeric_arithmetic import common_log

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
from formulite.fxNumeric.numeric_arithmetic import log_base_n

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
from formulite.fxNumeric.numeric_arithmetic import log1p

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
from formulite.fxNumeric.numeric_arithmetic import power

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
from formulite.fxNumeric.numeric_arithmetic import square_root

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
from formulite.fxNumeric.numeric_arithmetic import cube_root

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
from formulite.fxNumeric.numeric_arithmetic import nth_root

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
from formulite.fxNumeric.numeric_convertions import float_to_int_truncated

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
from formulite.fxNumeric.numeric_convertions import int_to_float

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
from formulite.fxNumeric.numeric_convertions import number_to_complex

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
from formulite.fxNumeric.numeric_convertions import number_to_bool

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
from formulite.fxNumeric.numeric_convertions import bool_to_int

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
from formulite.fxNumeric.numeric_convertions import bool_to_float

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
from formulite.fxNumeric.numeric_convertions import number_to_string

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
from formulite.fxNumeric.numeric_convertions import round_float_to_int

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
from formulite.fxNumeric.numeric_convertions import hex_to_int

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
from formulite.fxNumeric.numeric_convertions import bin_to_int

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
from formulite.fxNumeric.numeric_convertions import octal_to_int

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
from formulite.fxNumeric.numeric_convertions import int_to_binary_clean

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
from formulite.fxNumeric.numeric_convertions import int_to_hex_clean

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
from formulite.fxNumeric.numeric_convertions import int_to_binary_with_prefix

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
from formulite.fxNumeric.numeric_convertions import int_to_hex_with_prefix

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
from formulite.fxNumeric.numeric_convertions import int_to_octal_with_prefix

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
from formulite.fxNumeric.numeric_convertions import to_js_safe_integer

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
from formulite.fxNumeric.numeric_convertions import safe_convert_number

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
from formulite.fxNumeric.numeric_convertions import convert_string_to_float_with_locale

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
from formulite.fxNumeric.numeric_operations import is_numeric_type

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
from formulite.fxNumeric.numeric_operations import is_prime

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
from formulite.fxNumeric.numeric_operations import get_primes_up_to

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
from formulite.fxNumeric.numeric_operations import truncate_float

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
from formulite.fxNumeric.numeric_operations import round_to_n_decimals

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
from formulite.fxNumeric.numeric_operations import round_up

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
from formulite.fxNumeric.numeric_operations import round_down

round_down(3.9)  # 3
round_down(3.1)  # 3
round_down(-3.9)  # -4
```

**Cost:** O(1)

---

### `explicit_truncate()`

Eliminates the decimal part of a floating-point number without rounding, truncating towards zero.

**Parameters:**
- `number` (float): The floating-point number to truncate.

**Returns:**
- `int`: The resulting integer.

**Example:**
```python
from formulite.fxNumeric.numeric_operations import explicit_truncate

explicit_truncate(-4.8)  # -4
explicit_truncate(4.8)  # 4
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
from formulite.fxNumeric.numeric_operations import manual_round_and_cast

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
from formulite.fxNumeric.numeric_operations import manual_round_up_to_int

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
from formulite.fxNumeric.numeric_operations import manual_round_down_to_int

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
from formulite.fxNumeric.numeric_operations import round_half_even
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
from formulite.fxNumeric.numeric_operations import round_to_nearest_multiple

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
from formulite.fxNumeric.numeric_operations import add_with_exact_precision

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
from formulite.fxNumeric.numeric_operations import format_with_leading_zeros

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
from formulite.fxNumeric.numeric_operations import format_as_percentage

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
from formulite.fxNumeric.numeric_operations import format_as_scientific_notation

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
from formulite.fxNumeric.numeric_operations import force_float_division

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
from formulite.fxNumeric.numeric_operations import round_half_even

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
from formulite.fxNumeric.numeric_operations import normalize_to_0_1_range

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
from formulite.fxNumeric.numeric_operations import scale_to_new_range

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
from formulite.fxNumeric.numeric_operations import clip_number

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
from formulite.fxNumeric.numeric_operations import reduce_to_modulo_range

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
from formulite.fxNumeric.numeric_operations import quantize_number

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
from formulite.fxNumeric.numeric_operations import add_bool_to_int

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
from formulite.fxNumeric.numeric_operations import safe_sum_with_none

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
from formulite.fxNumeric.numeric_operations import count_true_with_sum

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
from formulite.fxNumeric.numeric_operations import true_division

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
from formulite.fxNumeric.numeric_operations import floor_division

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
from formulite.fxNumeric.numeric_operations import safe_division_for_context

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
from formulite.fxNumeric.numeric_operations import compare_floats_with_tolerance

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
from formulite.fxNumeric.numeric_statistics import calculate_frecuency

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
from formulite.fxNumeric.numeric_statistics import calculate_mean

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
from formulite.fxNumeric.numeric_statistics import calculate_median

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
from formulite.fxNumeric.numeric_statistics import calculate_mode

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
from formulite.fxNumeric.numeric_statistics import calculate_range

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
from formulite.fxNumeric.numeric_statistics import calculate_variance

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
from formulite.fxNumeric.numeric_statistics import calculate_standard_deviation

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
from formulite.fxNumeric.numeric_statistics import calculate_interquartile_range

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
from formulite.fxNumeric.numeric_statistics import calculate_covariance

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
from formulite.fxNumeric.numeric_statistics import calculate_pearson_correlation

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
from formulite.fxNumeric.numeric_statistics import calculate_percentile

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
from formulite.fxNumeric.numeric_statistics import sum_of_squares

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
from formulite.fxNumeric.numeric_trigonometry import sine

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
from formulite.fxNumeric.numeric_trigonometry import cosine

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
from formulite.fxNumeric.numeric_trigonometry import tangent

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
from formulite.fxNumeric.numeric_trigonometry import arcsine

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
from formulite.fxNumeric.numeric_trigonometry import arccosine

arccosine(1.0)  # 0.0
arccosine(-1.0)  # 3.141592653589793 (pi)
```

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
from formulite.fxNumeric.numeric_trigonometry import arctangent

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
from formulite.fxNumeric.numeric_trigonometry import arctangent2

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
from formulite.fxNumeric.numeric_trigonometry import hypotenuse

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
from formulite.fxNumeric.numeric_trigonometry import hyperbolic_sine

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
from formulite.fxNumeric.numeric_trigonometry import hyperbolic_cosine

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
from formulite.fxNumeric.numeric_trigonometry import hyperbolic_tangent

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
from formulite.fxNumeric.numeric_trigonometry import inverse_hyperbolic_sine

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
from formulite.fxNumeric.numeric_trigonometry import inverse_hyperbolic_cosine

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
from formulite.fxNumeric.numeric_trigonometry import inverse_hyperbolic_tangent

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
from formulite.fxNumeric.numeric_trigonometry import inverse_secant

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
from formulite.fxNumeric.numeric_trigonometry import inverse_cosecant

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
from formulite.fxNumeric.numeric_trigonometry import inverse_cotangent

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
from formulite.fxNumeric.numeric_trigonometry import inverse_hyperbolic_secant

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
from formulite.fxNumeric.numeric_trigonometry import inverse_hyperbolic_cosecant

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
from formulite.fxNumeric.numeric_trigonometry import inverse_hyperbolic_cotangent

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
from formulite.fxNumeric.numeric_trigonometry import degrees_to_radians

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
from formulite.fxNumeric.numeric_trigonometry import radians_to_degrees

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
from formulite.fxNumeric.numeric_trigonometry import secant

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
from formulite.fxNumeric.numeric_trigonometry import cosecant

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
from formulite.fxNumeric.numeric_trigonometry import cotangent

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
from formulite.fxNumeric.numeric_finance import future_value

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
from formulite.fxNumeric.numeric_finance import present_value

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
from formulite.fxNumeric.numeric_finance import pmt

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
from formulite.fxNumeric.numeric_finance import nper

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
from formulite.fxNumeric.numeric_finance import rate

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
from formulite.fxNumeric.numeric_finance import irr

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
from formulite.fxNumeric.numeric_finance import npv

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
from formulite.fxNumeric.numeric_finance import sln

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
from formulite.fxNumeric.numeric_finance import db

# Asset costs $10,000, salvage $1,000, useful life 5 years, period 1
db(cost=10000, salvage=1000, life=5, period=1)  # 3333.333333333333
```

**Cost:** O(1)

---

## Summary

The **fxNumeric** module provides **145 functions** across 6 categories:

- **Arithmetic Operations**: 8 functions (logarithms, powers, roots)
- **Numeric Conversions**: 24 functions (type conversions, base conversions, timestamps)
- **Numeric Operations**: 31 functions (rounding, formatting, comparisons, primes)
- **Statistical Functions**: 13 functions (mean, median, variance, correlation, percentiles)
- **Trigonometric Functions**: 41 functions (basic trig, hyperbolic, inverse functions)
- **Financial Functions**: 8 functions (FV, PV, PMT, NPV, IRR, depreciation)

All functions follow Python best practices with type hints, comprehensive documentation, and error handling.
