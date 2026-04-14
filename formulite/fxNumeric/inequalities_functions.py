"""Classical mathematical inequalities.

Implementations of fundamental inequalities from Murray R. Spiegel's
*Mathematical Handbook of Formulas and Tables*: AM-GM, Cauchy-Schwarz,
Minkowski, Hölder, Jensen, Chebyshev, and triangle inequality.
"""

import math
from typing import Callable, List, Tuple


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_nonempty(data: list, name: str = "data") -> None:
    if not data:
        raise ValueError(f"{name} must not be empty.")


def _check_positive_values(data: list, name: str = "data") -> None:
    if any(x <= 0 for x in data):
        raise ValueError(f"All values in {name} must be positive.")


# ---------------------------------------------------------------------------
# Mean inequalities
# ---------------------------------------------------------------------------


def am_gm_inequality(values: List[float]) -> Tuple[float, float, bool]:
    """Verifies the AM-GM inequality: AM >= GM for positive values.

    Arithmetic mean >= Geometric mean, with equality iff all values are equal.

    Args:
        values: List of positive numbers.

    Returns:
        Tuple (arithmetic_mean, geometric_mean, holds) where holds is always True.

    Raises:
        ValueError: If values is empty or contains non-positive numbers.

    Example:
        >>> am, gm, holds = am_gm_inequality([4, 1])
        >>> (am, gm, holds)
        (2.5, 2.0, True)

    Complexity: O(n)
    """
    _check_nonempty(values)
    _check_positive_values(values)

    n = len(values)
    am = sum(values) / n
    log_sum = sum(math.log(x) for x in values)
    gm = math.exp(log_sum / n)
    return (am, gm, am >= gm - 1e-15)


def am_hm_inequality(values: List[float]) -> Tuple[float, float, bool]:
    """Verifies the AM-HM inequality: AM >= HM for positive values.

    Arithmetic mean >= Harmonic mean.

    Args:
        values: List of positive numbers.

    Returns:
        Tuple (arithmetic_mean, harmonic_mean, holds).

    Example:
        >>> am, hm, holds = am_hm_inequality([1, 4])
        >>> (am, round(hm, 4), holds)
        (2.5, 1.6, True)

    Complexity: O(n)
    """
    _check_nonempty(values)
    _check_positive_values(values)

    n = len(values)
    am = sum(values) / n
    hm = n / sum(1.0 / x for x in values)
    return (am, hm, am >= hm - 1e-15)


def power_mean(values: List[float], p: float) -> float:
    """Computes the generalized power mean M_p of positive values.

    M_p = (Σ x_i^p / n)^(1/p). Special cases: p→0 is GM, p=-1 is HM, p=1 is AM.

    Args:
        values: List of positive numbers.
        p: Power parameter.

    Returns:
        Power mean M_p.

    Example:
        >>> round(power_mean([1, 4], 2), 6)  # Quadratic mean
        2.915476

    Complexity: O(n)
    """
    _check_nonempty(values)
    _check_positive_values(values)

    n = len(values)

    if abs(p) < 1e-15:
        return math.exp(sum(math.log(x) for x in values) / n)

    return (sum(x ** p for x in values) / n) ** (1.0 / p)


# ---------------------------------------------------------------------------
# Product / sum inequalities
# ---------------------------------------------------------------------------


def cauchy_schwarz_inequality(
    a: List[float], b: List[float]
) -> Tuple[float, float, bool]:
    """Verifies the Cauchy-Schwarz inequality: (Σ a_i b_i)² <= (Σ a_i²)(Σ b_i²).

    Args:
        a: First list of numbers.
        b: Second list of numbers (same length as a).

    Returns:
        Tuple (lhs, rhs, holds) where lhs = (Σ a_i b_i)², rhs = (Σ a_i²)(Σ b_i²).

    Raises:
        ValueError: If lists have different lengths or are empty.

    Example:
        >>> lhs, rhs, holds = cauchy_schwarz_inequality([1, 2], [3, 4])
        >>> (lhs, rhs, holds)
        (121, 55, True)

    Complexity: O(n)
    """
    _check_nonempty(a, "a")

    if len(a) != len(b):
        raise ValueError("Lists must have the same length.")

    dot = sum(ai * bi for ai, bi in zip(a, b))
    lhs = dot * dot
    sum_a2 = sum(ai * ai for ai in a)
    sum_b2 = sum(bi * bi for bi in b)
    rhs = sum_a2 * sum_b2
    return (lhs, rhs, lhs <= rhs + 1e-10)


def triangle_inequality_vector(v: List[float]) -> Tuple[float, float, bool]:
    """Verifies the triangle inequality for a vector: |Σ v_i| <= Σ |v_i|.

    Args:
        v: List of numbers.

    Returns:
        Tuple (abs_sum, sum_abs, holds).

    Example:
        >>> abs_s, sum_a, holds = triangle_inequality_vector([3, -4, 1])
        >>> (abs_s, sum_a, holds)
        (0, 8, True)

    Complexity: O(n)
    """
    _check_nonempty(v)
    abs_sum = abs(sum(v))
    sum_abs = sum(abs(x) for x in v)
    return (abs_sum, sum_abs, abs_sum <= sum_abs + 1e-10)


def minkowski_inequality(
    a: List[float], b: List[float], p: float = 2.0
) -> Tuple[float, float, bool]:
    """Verifies Minkowski's inequality: ||a+b||_p <= ||a||_p + ||b||_p.

    Args:
        a: First list of numbers.
        b: Second list of numbers (same length).
        p: Norm parameter (p >= 1).

    Returns:
        Tuple (lhs, rhs, holds).

    Raises:
        ValueError: If p < 1 or lists have different lengths.

    Example:
        >>> lhs, rhs, holds = minkowski_inequality([1, 0], [0, 1], 2)
        >>> (round(lhs, 6), round(rhs, 6), holds)
        (1.414214, 2.0, True)

    Complexity: O(n)
    """
    if p < 1:
        raise ValueError("p must be >= 1.")

    if len(a) != len(b):
        raise ValueError("Lists must have the same length.")

    _check_nonempty(a, "a")

    norm_sum = sum(abs(ai + bi) ** p for ai, bi in zip(a, b)) ** (1.0 / p)
    norm_a = sum(abs(ai) ** p for ai in a) ** (1.0 / p)
    norm_b = sum(abs(bi) ** p for bi in b) ** (1.0 / p)
    return (norm_sum, norm_a + norm_b, norm_sum <= norm_a + norm_b + 1e-10)


def holder_inequality(
    a: List[float], b: List[float], p: float = 2.0
) -> Tuple[float, float, bool]:
    """Verifies Hölder's inequality: Σ|a_i b_i| <= ||a||_p · ||b||_q where 1/p + 1/q = 1.

    Args:
        a: First list of numbers.
        b: Second list of numbers (same length).
        p: First exponent (p > 1).

    Returns:
        Tuple (lhs, rhs, holds).

    Example:
        >>> lhs, rhs, holds = holder_inequality([1, 2], [3, 4], 2)
        >>> holds
        True

    Complexity: O(n)
    """
    if p <= 1:
        raise ValueError("p must be > 1.")

    if len(a) != len(b):
        raise ValueError("Lists must have the same length.")

    _check_nonempty(a, "a")

    q = p / (p - 1.0)
    lhs = sum(abs(ai * bi) for ai, bi in zip(a, b))
    norm_a = sum(abs(ai) ** p for ai in a) ** (1.0 / p)
    norm_b = sum(abs(bi) ** q for bi in b) ** (1.0 / q)
    rhs = norm_a * norm_b
    return (lhs, rhs, lhs <= rhs + 1e-10)


def young_inequality(a: float, b: float, p: float = 2.0) -> Tuple[float, float, bool]:
    """Verifies Young's inequality: ab <= a^p/p + b^q/q where 1/p + 1/q = 1.

    Args:
        a: First positive number.
        b: Second positive number.
        p: Exponent (p > 1).

    Returns:
        Tuple (lhs, rhs, holds) where lhs = ab, rhs = a^p/p + b^q/q.

    Example:
        >>> lhs, rhs, holds = young_inequality(2, 3, 2)
        >>> (lhs, rhs, holds)
        (6, 6.5, True)

    Complexity: O(1)
    """
    if p <= 1:
        raise ValueError("p must be > 1.")

    if a < 0 or b < 0:
        raise ValueError("a and b must be non-negative.")

    q = p / (p - 1.0)
    lhs = a * b
    rhs = a ** p / p + b ** q / q
    return (lhs, rhs, lhs <= rhs + 1e-10)


def jensen_inequality(
    f: Callable[[float], float],
    values: List[float],
    weights: List[float] = None,
    convex: bool = True
) -> Tuple[float, float, bool]:
    """Verifies Jensen's inequality for convex/concave functions.

    Convex: f(Σ w_i x_i) <= Σ w_i f(x_i)
    Concave: f(Σ w_i x_i) >= Σ w_i f(x_i)

    Args:
        f: The function to evaluate.
        values: List of domain points.
        weights: Optional weights (must sum to 1). Defaults to uniform.
        convex: True if f is convex, False if concave.

    Returns:
        Tuple (f_of_mean, mean_of_f, holds).

    Example:
        >>> lhs, rhs, holds = jensen_inequality(lambda x: x**2, [1, 3])
        >>> (lhs, rhs, holds)
        (4.0, 5.0, True)

    Complexity: O(n)
    """
    _check_nonempty(values)

    n = len(values)

    if weights is None:
        weights = [1.0 / n] * n

    if len(weights) != n:
        raise ValueError("weights must have the same length as values.")

    if abs(sum(weights) - 1.0) > 1e-10:
        raise ValueError("weights must sum to 1.")

    weighted_mean = sum(w * x for w, x in zip(weights, values))
    f_of_mean = f(weighted_mean)
    mean_of_f = sum(w * f(x) for w, x in zip(weights, values))

    if convex:
        holds = f_of_mean <= mean_of_f + 1e-10
    else:
        holds = f_of_mean >= mean_of_f - 1e-10

    return (f_of_mean, mean_of_f, holds)


def chebyshev_sum_inequality(
    a: List[float], b: List[float]
) -> Tuple[float, float, bool]:
    """Verifies Chebyshev's sum inequality for similarly ordered sequences.

    If a and b are both sorted in the same order:
    n·Σ(a_i·b_i) >= (Σ a_i)(Σ b_i)

    Args:
        a: First sorted (ascending) list.
        b: Second sorted (ascending) list (same length).

    Returns:
        Tuple (lhs, rhs, holds) where lhs = n·Σ(a_i·b_i), rhs = (Σ a_i)(Σ b_i).

    Example:
        >>> lhs, rhs, holds = chebyshev_sum_inequality([1, 2, 3], [1, 2, 3])
        >>> (lhs, rhs, holds)
        (42, 36, True)

    Complexity: O(n)
    """
    _check_nonempty(a, "a")

    if len(a) != len(b):
        raise ValueError("Lists must have the same length.")

    n = len(a)
    lhs = n * sum(ai * bi for ai, bi in zip(a, b))
    rhs = sum(a) * sum(b)
    return (lhs, rhs, lhs >= rhs - 1e-10)


def rearrangement_inequality(
    a: List[float], b: List[float]
) -> Tuple[float, float, float]:
    """Computes the rearrangement inequality bounds.

    For sorted a and b: Σ(a_i·b_(n-i)) <= Σ(a_σ(i)·b_i) <= Σ(a_i·b_i).
    The sum is maximized when both are similarly sorted and minimized when
    oppositely sorted.

    Args:
        a: First list of numbers.
        b: Second list of numbers (same length).

    Returns:
        Tuple (min_sum, any_perm_sum, max_sum) where any_perm_sum uses original order.

    Example:
        >>> mn, mid, mx = rearrangement_inequality([1, 2, 3], [1, 2, 3])
        >>> (mn, mid, mx)
        (10, 14, 14)

    Complexity: O(n log n)
    """
    _check_nonempty(a, "a")

    if len(a) != len(b):
        raise ValueError("Lists must have the same length.")

    a_sorted = sorted(a)
    b_sorted = sorted(b)
    n = len(a)

    max_sum = sum(ai * bi for ai, bi in zip(a_sorted, b_sorted))
    min_sum = sum(a_sorted[i] * b_sorted[n - 1 - i] for i in range(n))
    curr_sum = sum(ai * bi for ai, bi in zip(a, b))
    return (min_sum, curr_sum, max_sum)


def bernoulli_inequality(x: float, n: int) -> Tuple[float, float, bool]:
    """Verifies Bernoulli's inequality: (1+x)^n >= 1 + nx for x >= -1, n >= 1.

    Args:
        x: Value (x >= -1).
        n: Positive integer exponent.

    Returns:
        Tuple (lhs, rhs, holds) where lhs = (1+x)^n, rhs = 1+nx.

    Raises:
        ValueError: If x < -1 or n < 1.

    Example:
        >>> lhs, rhs, holds = bernoulli_inequality(0.5, 3)
        >>> (round(lhs, 4), rhs, holds)
        (3.375, 2.5, True)

    Complexity: O(1)
    """
    if x < -1:
        raise ValueError("x must be >= -1.")

    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer.")

    lhs = (1.0 + x) ** n
    rhs = 1.0 + n * x
    return (lhs, rhs, lhs >= rhs - 1e-10)
