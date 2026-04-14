"""Finite differences and interpolation formulas.

Classical finite-difference methods from Murray R. Spiegel's
*Mathematical Handbook of Formulas and Tables*: difference tables,
Newton forward/backward interpolation, Stirling and Bessel central-
difference interpolation formulas.
"""

from typing import List


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _validate_numeric_list(values: list, name: str = "values") -> list:
    """Validate that *values* is a non-empty list of numbers."""

    if not isinstance(values, (list, tuple)):
        raise TypeError(f"{name} must be a list.")

    if not values:
        raise ValueError(f"{name} must not be empty.")

    for v in values:

        if not isinstance(v, (int, float)):
            raise TypeError(f"All elements of {name} must be numeric.")

    return list(values)


# ---------------------------------------------------------------------------
# Difference tables
# ---------------------------------------------------------------------------


def forward_difference_table(y: list) -> List[list]:
    """Builds a forward-difference table Δⁿy.

    Args:
        y: Equally-spaced function values [y0, y1, y2, ...].

    Returns:
        List of lists: ``table[k]`` contains the k-th order forward differences.
        ``table[0]`` is the original values.

    Example:
        >>> forward_difference_table([1, 4, 9, 16])
        [[1, 4, 9, 16], [3, 5, 7], [2, 2], [0]]

    Complexity: O(n^2)
    """
    y = _validate_numeric_list(y, "y")
    table = [list(y)]

    while len(table[-1]) > 1:
        prev = table[-1]
        table.append([prev[i + 1] - prev[i] for i in range(len(prev) - 1)])

    return table


def backward_difference_table(y: list) -> List[list]:
    """Builds a backward-difference table ∇ⁿy.

    Args:
        y: Equally-spaced function values [y0, y1, y2, ...].

    Returns:
        List of lists: ``table[k]`` contains the k-th order backward differences.
        Differences are aligned to the *last* element.

    Example:
        >>> backward_difference_table([1, 4, 9, 16])
        [[1, 4, 9, 16], [3, 5, 7], [2, 2], [0]]

    Complexity: O(n^2)
    """
    # Note: backward difference values are the same as forward,
    # but conventionally indexed from the end.
    return forward_difference_table(y)


def central_difference_table(y: list) -> List[list]:
    """Builds a central-difference table δⁿy.

    Central differences are stored with half-integer indexing.
    For even order k, δ^k y_i lives at integer nodes;
    for odd k, at half-integer nodes.

    Args:
        y: Equally-spaced function values.

    Returns:
        List of lists: ``table[k]`` holds k-th order central differences.

    Example:
        >>> central_difference_table([1, 4, 9, 16, 25])
        [[1, 4, 9, 16, 25], [3, 5, 7, 9], [2, 2, 2], [0, 0], [0]]

    Complexity: O(n^2)
    """
    # Central differences are numerically identical to forward differences.
    return forward_difference_table(y)


# ---------------------------------------------------------------------------
# Newton forward interpolation
# ---------------------------------------------------------------------------


def newton_forward_interpolation(
    x_values: list,
    y_values: list,
    x: float,
) -> float:
    """Newton's forward-difference interpolation formula.

    Uses equally-spaced nodes x0, x0+h, x0+2h, ... with values y_i.
    Computes: p(x) = Σ C(s,k) Δ^k y_0 where s = (x - x0) / h.

    Args:
        x_values: Equally-spaced x nodes.
        y_values: Corresponding y values.
        x: Point at which to interpolate.

    Returns:
        Interpolated value at x.

    Raises:
        ValueError: If lengths don't match or fewer than 2 points.

    Example:
        >>> newton_forward_interpolation([0, 1, 2, 3], [1, 4, 9, 16], 1.5)
        6.25

    Complexity: O(n^2)
    """
    x_values = _validate_numeric_list(x_values, "x_values")
    y_values = _validate_numeric_list(y_values, "y_values")

    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have equal length.")

    if len(x_values) < 2:
        raise ValueError("At least 2 data points required.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    n = len(x_values)
    h = x_values[1] - x_values[0]

    if h == 0:
        raise ValueError("x_values must have non-zero spacing.")

    s = (x - x_values[0]) / h

    # Build forward difference table (first column of each order)
    table = forward_difference_table(y_values)

    result = 0.0
    binom = 1.0  # C(s, k)

    for k in range(n):

        if k < len(table):
            result += binom * table[k][0]

        if k < n - 1:
            binom *= (s - k) / (k + 1)

    return result


# ---------------------------------------------------------------------------
# Newton backward interpolation
# ---------------------------------------------------------------------------


def newton_backward_interpolation(
    x_values: list,
    y_values: list,
    x: float,
) -> float:
    """Newton's backward-difference interpolation formula.

    Uses equally-spaced nodes with values y_i.
    Computes: p(x) = Σ C(s,k)·(-1)^k · Δ^k y_{n-k} where s = (x - x_n) / h.
    Equivalent to using backward differences ∇^k y_n.

    Args:
        x_values: Equally-spaced x nodes.
        y_values: Corresponding y values.
        x: Point at which to interpolate.

    Returns:
        Interpolated value at x.

    Example:
        >>> newton_backward_interpolation([0, 1, 2, 3], [1, 4, 9, 16], 2.5)
        12.25

    Complexity: O(n^2)
    """
    x_values = _validate_numeric_list(x_values, "x_values")
    y_values = _validate_numeric_list(y_values, "y_values")

    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have equal length.")

    if len(x_values) < 2:
        raise ValueError("At least 2 data points required.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    n = len(x_values)
    h = x_values[1] - x_values[0]

    if h == 0:
        raise ValueError("x_values must have non-zero spacing.")

    s = (x - x_values[-1]) / h  # s <= 0 for backward

    # Build forward difference table
    table = forward_difference_table(y_values)

    result = 0.0
    binom = 1.0  # C(-s, k) adjusted for backward

    for k in range(n):

        if k < len(table):
            # Use last element of each difference order
            result += binom * table[k][-1]

        if k < n - 1:
            binom *= (s + k) / (k + 1)

    return result


# ---------------------------------------------------------------------------
# Stirling's central-difference interpolation
# ---------------------------------------------------------------------------


def stirling_interpolation(
    x_values: list,
    y_values: list,
    x: float,
) -> float:
    """Stirling's central-difference interpolation formula.

    Best for interpolating near the centre of the data. Uses the average
    of forward and backward differences at the central node.

    f(x) ≈ y_0 + s·μδy_0 + s²/2!·δ²y_0 + s(s²-1)/3!·μδ³y_0 + ...

    where s = (x - x_center) / h and μδ^k y_0 = (Δ^k + Δ^k shifted)/2
    for odd k.

    Args:
        x_values: Equally-spaced x nodes (odd count preferred for symmetric center).
        y_values: Corresponding y values.
        x: Point at which to interpolate.

    Returns:
        Interpolated value.

    Example:
        >>> stirling_interpolation([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], 2.0)
        8.0

    Complexity: O(n^2)
    """
    x_values = _validate_numeric_list(x_values, "x_values")
    y_values = _validate_numeric_list(y_values, "y_values")

    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have equal length.")

    n = len(x_values)

    if n < 3:
        raise ValueError("At least 3 data points required for Stirling interpolation.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    h = x_values[1] - x_values[0]

    if h == 0:
        raise ValueError("x_values must have non-zero spacing.")

    center = n // 2
    s = (x - x_values[center]) / h

    table = forward_difference_table(y_values)

    # Stirling's formula (explicit low-order terms):
    # f ≈ y0 + s·μδ + s²/2!·δ² + s·(s²-1)/3!·μδ³ + s²(s²-1)/4!·δ⁴ + ...
    # where μδ^{2k+1} = average of two forward differences around center
    # and δ^{2k} = forward difference centered at the node

    result = table[0][center]

    # Order 1: s * μδ¹y₀
    if len(table) > 1:
        i1 = center - 1
        i2 = center

        if 0 <= i1 < len(table[1]) and i2 < len(table[1]):
            mu_d1 = (table[1][i1] + table[1][i2]) / 2.0
            result += s * mu_d1

    # Order 2: s²/2! * δ²y₀
    if len(table) > 2:
        i_e = center - 1

        if 0 <= i_e < len(table[2]):
            result += s * s / 2.0 * table[2][i_e]

    # Order 3: s(s²-1)/3! * μδ³y₀
    if len(table) > 3:
        i1 = center - 2
        i2 = center - 1

        if 0 <= i1 < len(table[3]) and 0 <= i2 < len(table[3]):
            mu_d3 = (table[3][i1] + table[3][i2]) / 2.0
            result += s * (s * s - 1.0) / 6.0 * mu_d3

    # Order 4: s²(s²-1)/4! * δ⁴y₀
    if len(table) > 4:
        i_e = center - 2

        if 0 <= i_e < len(table[4]):
            result += s * s * (s * s - 1.0) / 24.0 * table[4][i_e]

    return result


# ---------------------------------------------------------------------------
# Bessel's interpolation formula
# ---------------------------------------------------------------------------


def bessel_interpolation(
    x_values: list,
    y_values: list,
    x: float,
) -> float:
    """Bessel's central-difference interpolation formula.

    Best for interpolating at or near the midpoint between two central nodes.
    Uses averages of function values and differences.

    Args:
        x_values: Equally-spaced x nodes (even count preferred).
        y_values: Corresponding y values.
        x: Point at which to interpolate.

    Returns:
        Interpolated value.

    Example:
        >>> bessel_interpolation([0, 1, 2, 3], [0, 1, 8, 27], 1.5)
        3.375

    Complexity: O(n^2)
    """
    x_values = _validate_numeric_list(x_values, "x_values")
    y_values = _validate_numeric_list(y_values, "y_values")

    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have equal length.")

    n = len(x_values)

    if n < 4:
        raise ValueError("At least 4 data points required for Bessel interpolation.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    h = x_values[1] - x_values[0]

    if h == 0:
        raise ValueError("x_values must have non-zero spacing.")

    # Find the two central nodes
    center = n // 2 - 1  # index of x_0 (left of center pair)
    s = (x - x_values[center]) / h  # s typically near 0.5

    table = forward_difference_table(y_values)

    # Bessel: B(x) = (y0 + y1)/2 + (s - 1/2)Δy0 + s(s-1)/2! · (Δ²y_{-1}+Δ²y_0)/2 + ...
    result = (table[0][center] + table[0][center + 1]) / 2.0

    if len(table) > 1 and center < len(table[1]):
        result += (s - 0.5) * table[1][center]

    if len(table) > 2:
        idx = center - 1

        if 0 <= idx < len(table[2]) and idx + 1 < len(table[2]):
            avg_d2 = (table[2][idx] + table[2][idx + 1]) / 2.0
            result += s * (s - 1) / 2.0 * avg_d2

    if len(table) > 3:
        idx = center - 1

        if 0 <= idx < len(table[3]):
            result += s * (s - 1) * (s - 0.5) / 6.0 * table[3][idx]

    return result


# ---------------------------------------------------------------------------
# Gauss forward/backward interpolation
# ---------------------------------------------------------------------------


def gauss_forward_interpolation(
    x_values: list,
    y_values: list,
    x: float,
) -> float:
    """Gauss's forward central-difference interpolation formula.

    Args:
        x_values: Equally-spaced x nodes.
        y_values: Corresponding y values.
        x: Point at which to interpolate.

    Returns:
        Interpolated value.

    Example:
        >>> gauss_forward_interpolation([0, 1, 2, 3, 4], [0, 1, 8, 27, 64], 2.5)
        15.625

    Complexity: O(n^2)
    """
    x_values = _validate_numeric_list(x_values, "x_values")
    y_values = _validate_numeric_list(y_values, "y_values")

    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have equal length.")

    n = len(x_values)

    if n < 3:
        raise ValueError("At least 3 data points required.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    h = x_values[1] - x_values[0]

    if h == 0:
        raise ValueError("x_values must have non-zero spacing.")

    center = n // 2
    s = (x - x_values[center]) / h

    table = forward_difference_table(y_values)

    result = table[0][center]
    term = s

    # Order 1: s * Δy_center
    if len(table) > 1 and center < len(table[1]):
        result += term * table[1][center]

    # Order 2: s(s-1)/2 * Δ²y_{center-1}
    if len(table) > 2:
        term = s * (s - 1) / 2.0
        idx = center - 1

        if 0 <= idx < len(table[2]):
            result += term * table[2][idx]

    # Order 3: s(s-1)(s+1)/6 * Δ³y_{center-1}
    if len(table) > 3:
        term = s * (s - 1) * (s + 1) / 6.0
        idx = center - 1

        if 0 <= idx < len(table[3]):
            result += term * table[3][idx]

    # Order 4: s(s-1)(s+1)(s-2)/24 * Δ⁴y_{center-2}
    if len(table) > 4:
        term = s * (s - 1) * (s + 1) * (s - 2) / 24.0
        idx = center - 2

        if 0 <= idx < len(table[4]):
            result += term * table[4][idx]

    return result


# ---------------------------------------------------------------------------
# Divided differences (for unequal spacing)
# ---------------------------------------------------------------------------


def divided_difference_table(
    x_values: list,
    y_values: list,
) -> List[list]:
    """Builds a divided-difference table for Newton's general interpolation.

    Args:
        x_values: Distinct x nodes (not necessarily equally spaced).
        y_values: Corresponding y values.

    Returns:
        Table where ``table[k][i]`` is f[x_i, x_{i+1}, ..., x_{i+k}].

    Example:
        >>> divided_difference_table([1, 2, 4], [1, 8, 64])
        [[1, 8, 64], [7.0, 28.0], [7.0]]

    Complexity: O(n^2)
    """
    x_values = _validate_numeric_list(x_values, "x_values")
    y_values = _validate_numeric_list(y_values, "y_values")

    if len(x_values) != len(y_values):
        raise ValueError("x_values and y_values must have equal length.")

    n = len(x_values)
    table = [list(y_values)]

    for k in range(1, n):
        prev = table[-1]
        row = []

        for i in range(len(prev) - 1):
            denom = x_values[i + k] - x_values[i]

            if abs(denom) < 1e-15:
                raise ValueError("x_values must be distinct.")

            row.append((prev[i + 1] - prev[i]) / denom)

        table.append(row)

    return table
