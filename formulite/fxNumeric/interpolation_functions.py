"""Interpolation utilities module.

Provides linear interpolation functions for mapping values between ranges,
performing piecewise interpolation over datasets, and computing inverse
interpolation factors.
"""

from typing import List, Union


def linear_interpolate(x: float, x0: float, y0: float,
                       x1: float, y1: float) -> float:
    """Linearly interpolate between two points.

    Computes the y value at position x on the line passing through
    (x0, y0) and (x1, y1). Extrapolates if x is outside [x0, x1].

    Args:
        x: The x position to evaluate.
        x0: x coordinate of the first point.
        y0: y coordinate of the first point.
        x1: x coordinate of the second point.
        y1: y coordinate of the second point.

    Returns:
        Interpolated y value.

    Raises:
        ValueError: If x0 == x1 (undefined slope).

    Example:
        >>> linear_interpolate(5, 0, 0, 10, 100)
        50.0

    Complexity: O(1)
    """

    if x0 == x1:
        raise ValueError("x0 and x1 must be different (division by zero).")

    t = (x - x0) / (x1 - x0)
    return y0 + t * (y1 - y0)


def clamp_interpolate(x: float, x0: float, y0: float,
                      x1: float, y1: float) -> float:
    """Linearly interpolate between two points, clamped to the output range.

    Same as :func:`linear_interpolate` but the result is clamped to
    [min(y0, y1), max(y0, y1)].

    Args:
        x: The x position to evaluate.
        x0: x coordinate of the first point.
        y0: y coordinate of the first point.
        x1: x coordinate of the second point.
        y1: y coordinate of the second point.

    Returns:
        Clamped interpolated y value.

    Raises:
        ValueError: If x0 == x1.

    Example:
        >>> clamp_interpolate(15, 0, 0, 10, 100)
        100.0

    Complexity: O(1)
    """

    y = linear_interpolate(x, x0, y0, x1, y1)
    lo, hi = min(y0, y1), max(y0, y1)
    return max(lo, min(hi, y))


def inverse_interpolate(y: float, y0: float, y1: float) -> float:
    """Compute the interpolation factor t such that lerp(y0, y1, t) == y.

    Args:
        y: The target value.
        y0: Start of the range.
        y1: End of the range.

    Returns:
        Factor t in [0, 1] when y is within [y0, y1], or outside
        when y is extrapolated.

    Raises:
        ValueError: If y0 == y1 (zero-length range).

    Example:
        >>> inverse_interpolate(50, 0, 100)
        0.5

    Complexity: O(1)
    """

    if y0 == y1:
        raise ValueError("y0 and y1 must be different (zero-length range).")

    return (y - y0) / (y1 - y0)


def piecewise_interpolate(x: float,
                          xs: List[Union[int, float]],
                          ys: List[Union[int, float]]) -> float:
    """Linearly interpolate over a piecewise-defined dataset.

    Given sorted breakpoints *xs* and corresponding values *ys*, find the
    segment containing *x* and interpolate. Clamps to the first/last
    segment if *x* is outside the range.

    Args:
        x: The x position to evaluate.
        xs: Sorted list of x breakpoints (at least 2).
        ys: Corresponding y values (same length as xs).

    Returns:
        Interpolated y value.

    Raises:
        ValueError: If xs and ys have different lengths or fewer than 2 points.

    Example:
        >>> piecewise_interpolate(15, [0, 10, 20, 30], [0, 100, 100, 200])
        100.0

    Complexity: O(n) where n = len(xs)
    """

    if len(xs) != len(ys):
        raise ValueError("xs and ys must have the same length.")

    if len(xs) < 2:
        raise ValueError("At least 2 breakpoints are required.")

    # Clamp to range
    if x <= xs[0]:
        return float(ys[0])

    if x >= xs[-1]:
        return float(ys[-1])

    # Find the segment
    for i in range(len(xs) - 1):

        if xs[i] <= x <= xs[i + 1]:
            return linear_interpolate(x, xs[i], ys[i], xs[i + 1], ys[i + 1])

    # Fallback (should not reach here with sorted xs)
    return float(ys[-1])


def map_range(value: Union[int, float],
              in_min: Union[int, float], in_max: Union[int, float],
              out_min: Union[int, float], out_max: Union[int, float]) -> float:
    """Re-map a value from one range to another (Arduino-style).

    Unlike :func:`~formulite.fxNumeric.interpolation_functions.scale_to_new_range`
    this function does **not** clamp and is intentionally minimal.

    Args:
        value: Input value.
        in_min: Lower bound of the input range.
        in_max: Upper bound of the input range.
        out_min: Lower bound of the output range.
        out_max: Upper bound of the output range.

    Returns:
        Value mapped to the output range.

    Raises:
        ValueError: If in_min == in_max.

    Example:
        >>> map_range(5, 0, 10, 0, 100)
        50.0

    Complexity: O(1)
    """

    if in_min == in_max:
        raise ValueError("in_min and in_max must be different.")

    return float(out_min + (value - in_min) * (out_max - out_min) / (in_max - in_min))


# ---------------------------------------------------------------------------
# Normalization and scaling helpers
# ---------------------------------------------------------------------------


def normalize_to_0_1_range(x: Union[int, float], min_val: Union[int, float], max_val: Union[int, float]) -> float:
    """Normalizes a number to scale it to a range between 0 and 1.

    Args:
        x (Union[int, float]): The numeric value to normalize.
        min_val (Union[int, float]): The expected minimum value in the original range.
        max_val (Union[int, float]): The expected maximum value in the original range.

    Returns:
        float: The normalized value between 0 and 1. If min_val == max_val, returns 0.0.

    Raises:
        ValueError: If 'min_val' is greater than 'max_val'.

    Example:
        >>> normalize_to_0_1_range(50, 0, 100)
        0.5
        >>> normalize_to_0_1_range(75, 50, 100)
        0.5

    **Cost:** O(1), normalization calculation.
    """
    if min_val > max_val:
        raise ValueError("min_val cannot be greater than max_val.")

    if max_val == min_val:
        return 0.0

    return map_range(x, min_val, max_val, 0, 1)


def scale_to_new_range(x: Union[int, float], min_x: Union[int, float], max_x: Union[int, float], new_min: Union[int, float], new_max: Union[int, float]) -> float:
    """Scales a number from an original range to a new range.

    Args:
        x (Union[int, float]): The numeric value to scale.
        min_x (Union[int, float]): The minimum value of the original range.
        max_x (Union[int, float]): The maximum value of the original range.
        new_min (Union[int, float]): The minimum value of the new range.
        new_max (Union[int, float]): The maximum value of the new range.

    Returns:
        float: The scaled value in the new range.

    Raises:
        ValueError: If 'min_x' is greater than 'max_x'.

    Example:
        >>> scale_to_new_range(50, 0, 100, 0, 10)
        5.0
        >>> scale_to_new_range(50, 0, 100, 100, 200)
        150.0

    **Cost:** O(1), linear scaling.
    """
    if min_x > max_x:
        raise ValueError("min_x cannot be greater than max_x.")

    if max_x == min_x:
        return float(new_min)

    return map_range(x, min_x, max_x, new_min, new_max)


def clip_number(x: Union[int, float], min_val: Union[int, float], max_val: Union[int, float]) -> Union[int, float]:
    """Forces a number to be within a specific range [min_val, max_val].

    Args:
        x (Union[int, float]): The number to clip.
        min_val (Union[int, float]): The minimum allowed value.
        max_val (Union[int, float]): The maximum allowed value.

    Returns:
        Union[int, float]: The number adjusted to the range.

    Raises:
        ValueError: If 'min_val' is greater than 'max_val'.

    Example:
        >>> clip_number(10, 0, 100)
        10
        >>> clip_number(-5, 0, 100)
        0
        >>> clip_number(150, 0, 100)
        100

    **Cost:** O(1), comparisons and value adjustment.
    """
    if min_val > max_val:
        raise ValueError("min_val cannot be greater than max_val.")

    return max(min(x, max_val), min_val)


def linear_interpolation(
    x: Union[int, float],
    x_points: List[Union[int, float]],
    y_points: List[Union[int, float]],
) -> float:
    """Estimates a Y value for *x* via piecewise linear interpolation.

    *x_points* must be sorted in ascending order. If *x* is outside the
    range of *x_points* it is linearly extrapolated from the nearest segment.

    Args:
        x: The X value to interpolate.
        x_points: Known X coordinates (sorted ascending).
        y_points: Known Y coordinates, same length as *x_points*.

    Returns:
        The interpolated (or extrapolated) Y value.

    Raises:
        TypeError: If inputs are not numeric / lists of numbers.
        ValueError: If lists are empty or have different lengths, or if
                    fewer than 2 data points are provided.

    Example:
        >>> linear_interpolation(2.5, [1, 2, 3], [10, 20, 30])
        25.0
        >>> linear_interpolation(0, [1, 3], [10, 30])
        0.0

    Complexity: O(n) for a linear scan; O(log n) with bisect optimization.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(x_points, list) or not isinstance(y_points, list):
        raise TypeError("x_points and y_points must be lists.")

    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length.")

    if len(x_points) < 2:
        raise ValueError("At least 2 data points are required.")

    if not all(isinstance(v, (int, float)) for v in x_points):
        raise TypeError("All x_points must be numeric.")

    if not all(isinstance(v, (int, float)) for v in y_points):
        raise TypeError("All y_points must be numeric.")

    # Find the interval containing x
    for i in range(len(x_points) - 1):

        if x_points[i] <= x <= x_points[i + 1]:
            dx = x_points[i + 1] - x_points[i]

            if dx == 0:
                return float(y_points[i])

            t = (x - x_points[i]) / dx
            return float(y_points[i] + t * (y_points[i + 1] - y_points[i]))

    # Extrapolation: use first or last segment
    if x < x_points[0]:
        dx = x_points[1] - x_points[0]

        if dx == 0:
            return float(y_points[0])

        slope = (y_points[1] - y_points[0]) / dx
        return float(y_points[0] + slope * (x - x_points[0]))

    dx = x_points[-1] - x_points[-2]

    if dx == 0:
        return float(y_points[-1])

    slope = (y_points[-1] - y_points[-2]) / dx
    return float(y_points[-1] + slope * (x - x_points[-1]))


def normalize_list(data: List[Union[int, float]]) -> List[float]:
    """Normalizes a list to the [0, 1] range using min-max scaling.

    Args:
        data: A list of numeric values.

    Returns:
        A new list with values scaled to [0, 1]. If all values are equal,
        returns a list of 0.0.

    Raises:
        TypeError: If *data* is not a list of numbers.
        ValueError: If *data* is empty.

    Example:
        >>> normalize_list([1, 2, 3, 4, 5])
        [0.0, 0.25, 0.5, 0.75, 1.0]
        >>> normalize_list([10, 10, 10])
        [0.0, 0.0, 0.0]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

    min_val = min(data)
    max_val = max(data)
    rng = max_val - min_val

    if rng == 0:
        return [0.0] * len(data)

    return [(x - min_val) / rng for x in data]


def lagrange_interpolation(
    x_points: List[Union[int, float]],
    y_points: List[Union[int, float]],
    x: Union[int, float],
) -> float:
    """Evaluates the Lagrange interpolating polynomial at a given x.

    Constructs the unique polynomial of degree ≤ n-1 that passes through
    all n data points and returns its value at x.

    Args:
        x_points: The x coordinates of the data points (must be distinct).
        y_points: The y coordinates of the data points (same length as x_points).
        x: The x position to evaluate.

    Returns:
        The interpolated y value.

    Raises:
        TypeError: If inputs are not lists/numbers.
        ValueError: If lists are empty, different lengths, or x_points not distinct.

    Example:
        >>> lagrange_interpolation([1, 2, 3], [1, 4, 9], 2.5)
        6.25

    Complexity: O(n²)
    """
    if not isinstance(x_points, list) or not isinstance(y_points, list):
        raise TypeError("x_points and y_points must be lists.")

    if not x_points:
        raise ValueError("Data points cannot be empty.")

    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length.")

    if not all(isinstance(v, (int, float)) for v in x_points + y_points):
        raise TypeError("All coordinates must be numeric.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if len(set(x_points)) != len(x_points):
        raise ValueError("x_points must contain distinct values.")

    n = len(x_points)
    result = 0.0

    for i in range(n):
        basis = 1.0

        for j in range(n):

            if i != j:
                basis *= (x - x_points[j]) / (x_points[i] - x_points[j])

        result += y_points[i] * basis

    return result


def bilinear_interpolation(
    x: Union[int, float],
    y: Union[int, float],
    x1: Union[int, float],
    x2: Union[int, float],
    y1: Union[int, float],
    y2: Union[int, float],
    q11: Union[int, float],
    q21: Union[int, float],
    q12: Union[int, float],
    q22: Union[int, float],
) -> float:
    """Performs bilinear interpolation on a 2D grid.

    Given four corner values Q(x1,y1), Q(x2,y1), Q(x1,y2), Q(x2,y2),
    estimates the value at (x, y).

    Args:
        x: The x coordinate to evaluate.
        y: The y coordinate to evaluate.
        x1: Lower x boundary.
        x2: Upper x boundary.
        y1: Lower y boundary.
        y2: Upper y boundary.
        q11: Value at (x1, y1).
        q21: Value at (x2, y1).
        q12: Value at (x1, y2).
        q22: Value at (x2, y2).

    Returns:
        The interpolated value at (x, y).

    Raises:
        TypeError: If any input is not numeric.
        ValueError: If x1 == x2 or y1 == y2.

    Example:
        >>> bilinear_interpolation(0.5, 0.5, 0, 1, 0, 1, 0, 1, 1, 2)
        1.0

    Complexity: O(1)
    """
    params = [x, y, x1, x2, y1, y2, q11, q21, q12, q22]

    if not all(isinstance(v, (int, float)) for v in params):
        raise TypeError("All parameters must be numeric.")

    if x1 == x2:
        raise ValueError("x1 and x2 must be different.")

    if y1 == y2:
        raise ValueError("y1 and y2 must be different.")

    dx = x2 - x1
    dy = y2 - y1

    r1 = ((x2 - x) / dx) * q11 + ((x - x1) / dx) * q21
    r2 = ((x2 - x) / dx) * q12 + ((x - x1) / dx) * q22

    return ((y2 - y) / dy) * r1 + ((y - y1) / dy) * r2


def newton_divided_difference(
    x_points: List[Union[int, float]],
    y_points: List[Union[int, float]],
    x: Union[int, float],
) -> float:
    """Evaluates a polynomial at x using Newton's divided-difference form.

    Builds the divided-difference table and evaluates the resulting
    polynomial at the given x.

    Args:
        x_points: Known x-values (must be distinct).
        y_points: Known y-values (same length as x_points).
        x: The x-value to interpolate.

    Returns:
        The interpolated y-value at x.

    Raises:
        TypeError: If inputs are not lists of numbers / a number.
        ValueError: If lists are empty, have different lengths, or
            x_points contains duplicates.

    Example:
        >>> newton_divided_difference([1, 2, 3], [1, 4, 9], 2.5)
        6.25

    Complexity: O(n²)
    """
    if not isinstance(x_points, list) or not isinstance(y_points, list):
        raise TypeError("x_points and y_points must be lists.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not x_points:
        raise ValueError("Point lists cannot be empty.")

    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length.")

    if not all(isinstance(v, (int, float)) for v in x_points):
        raise TypeError("All x_points must be numeric.")

    if not all(isinstance(v, (int, float)) for v in y_points):
        raise TypeError("All y_points must be numeric.")

    if len(set(x_points)) != len(x_points):
        raise ValueError("x_points must contain distinct values.")

    n = len(x_points)
    coeff = list(y_points)

    for j in range(1, n):

        for i in range(n - 1, j - 1, -1):
            coeff[i] = (coeff[i] - coeff[i - 1]) / (x_points[i] - x_points[i - j])

    # Evaluate using Horner's method
    result = coeff[-1]

    for i in range(n - 2, -1, -1):
        result = result * (x - x_points[i]) + coeff[i]

    return result


def cubic_spline_natural(
    x_points: List[Union[int, float]],
    y_points: List[Union[int, float]],
    x: Union[int, float],
) -> float:
    """Evaluates a natural cubic spline at x.

    Uses natural boundary conditions (second derivative = 0 at endpoints).
    Solves the tridiagonal system for spline coefficients using the
    Thomas algorithm.

    Args:
        x_points: Sorted, distinct known x-values (>= 2 points).
        y_points: Known y-values (same length as x_points).
        x: The x-value to interpolate.

    Returns:
        The interpolated y-value at x.

    Raises:
        TypeError: If inputs are not lists of numbers / a number.
        ValueError: If fewer than 2 points, different lengths,
            duplicates, or x_points not sorted ascending.

    Example:
        >>> cubic_spline_natural([0, 1, 2, 3], [0, 1, 4, 9], 1.5)
        2.25

    Complexity: O(n)
    """
    if not isinstance(x_points, list) or not isinstance(y_points, list):
        raise TypeError("x_points and y_points must be lists.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if len(x_points) < 2:
        raise ValueError("At least 2 points are required.")

    if len(x_points) != len(y_points):
        raise ValueError("x_points and y_points must have the same length.")

    if not all(isinstance(v, (int, float)) for v in x_points):
        raise TypeError("All x_points must be numeric.")

    if not all(isinstance(v, (int, float)) for v in y_points):
        raise TypeError("All y_points must be numeric.")

    for i in range(1, len(x_points)):

        if x_points[i] <= x_points[i - 1]:
            raise ValueError("x_points must be sorted in strictly ascending order.")

    n = len(x_points) - 1  # number of intervals
    h = [x_points[i + 1] - x_points[i] for i in range(n)]

    # Natural spline: second derivatives at endpoints are 0
    # Build the tridiagonal system for interior knots
    if n == 1:
        # Linear interpolation for 2 points
        t = (x - x_points[0]) / h[0]
        return y_points[0] + t * (y_points[1] - y_points[0])

    # Right-hand side
    alpha = [0.0] * (n + 1)

    for i in range(1, n):
        alpha[i] = (3.0 / h[i]) * (y_points[i + 1] - y_points[i]) - \
                   (3.0 / h[i - 1]) * (y_points[i] - y_points[i - 1])

    # Thomas algorithm
    diag = [0.0] * (n + 1)
    mu = [0.0] * (n + 1)
    z = [0.0] * (n + 1)
    diag[0] = 1.0

    for i in range(1, n):
        diag[i] = 2.0 * (x_points[i + 1] - x_points[i - 1]) - h[i - 1] * mu[i - 1]
        mu[i] = h[i] / diag[i]
        z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / diag[i]

    diag[n] = 1.0
    c = [0.0] * (n + 1)
    b = [0.0] * n
    d = [0.0] * n

    for j in range(n - 1, -1, -1):
        c[j] = z[j] - mu[j] * c[j + 1]
        b[j] = (y_points[j + 1] - y_points[j]) / h[j] - \
               h[j] * (c[j + 1] + 2.0 * c[j]) / 3.0
        d[j] = (c[j + 1] - c[j]) / (3.0 * h[j])

    # Find the interval
    idx = n - 1

    for i in range(n):

        if x <= x_points[i + 1]:
            idx = i
            break

    dx = x - x_points[idx]
    return y_points[idx] + b[idx] * dx + c[idx] * dx ** 2 + d[idx] * dx ** 3
