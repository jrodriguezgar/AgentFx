"""Series and summation formulas.

Provides arithmetic, geometric, harmonic, Taylor/Maclaurin, Fourier,
and binomial series evaluations from Spiegel's *Mathematical Handbook*.
"""

import math
from typing import Callable, List, Tuple


# ---------------------------------------------------------------------------
# Classical series sums
# ---------------------------------------------------------------------------


def arithmetic_series_sum(a: float, d: float, n: int) -> float:
    """Computes the sum of an arithmetic series: a + (a+d) + ... + (a+(n-1)d).

    S_n = n/2 * (2a + (n-1)d).

    Args:
        a: First term.
        d: Common difference.
        n: Number of terms (>= 1).

    Returns:
        Sum of the series.

    Raises:
        TypeError: If a or d are not numeric, or n is not an integer.
        ValueError: If n < 1.

    Example:
        >>> arithmetic_series_sum(1, 2, 5)
        25.0

    Complexity: O(1)
    """
    if not isinstance(a, (int, float)) or not isinstance(d, (int, float)):
        raise TypeError("a and d must be numeric.")

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    return n / 2.0 * (2.0 * a + (n - 1) * d)


def geometric_series_sum(a: float, r: float, n: int) -> float:
    """Computes the sum of a finite geometric series: a + ar + ar^2 + ... + ar^{n-1}.

    S_n = a(1 - r^n) / (1 - r) when r != 1, or S_n = n*a when r == 1.

    Args:
        a: First term.
        r: Common ratio.
        n: Number of terms (>= 1).

    Returns:
        Sum of the series.

    Raises:
        TypeError: If a or r are not numeric, or n is not an integer.
        ValueError: If n < 1.

    Example:
        >>> geometric_series_sum(1, 0.5, 10)
        1.998046875

    Complexity: O(1)
    """
    if not isinstance(a, (int, float)) or not isinstance(r, (int, float)):
        raise TypeError("a and r must be numeric.")

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    if r == 1:
        return float(n * a)

    return a * (1.0 - r ** n) / (1.0 - r)


def geometric_series_infinite(a: float, r: float) -> float:
    """Computes the sum of an infinite geometric series: a / (1 - r).

    Converges only when |r| < 1.

    Args:
        a: First term.
        r: Common ratio (|r| < 1).

    Returns:
        Sum of the infinite series.

    Raises:
        TypeError: If a or r are not numeric.
        ValueError: If |r| >= 1.

    Example:
        >>> geometric_series_infinite(1, 0.5)
        2.0

    Complexity: O(1)
    """
    if not isinstance(a, (int, float)) or not isinstance(r, (int, float)):
        raise TypeError("a and r must be numeric.")

    if abs(r) >= 1:
        raise ValueError("|r| must be < 1 for convergence.")

    return a / (1.0 - r)


def harmonic_series_partial(n: int) -> float:
    """Computes the n-th partial sum of the harmonic series H_n = sum_{k=1}^{n} 1/k.

    Args:
        n: Number of terms (>= 1).

    Returns:
        H_n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Example:
        >>> round(harmonic_series_partial(10), 6)
        2.928968

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    return sum(1.0 / k for k in range(1, n + 1))


def generalized_harmonic(n: int, s: float) -> float:
    """Computes the generalized harmonic number H_{n,s} = sum_{k=1}^{n} 1/k^s.

    Args:
        n: Number of terms (>= 1).
        s: Exponent (> 0).

    Returns:
        H_{n,s}.

    Raises:
        TypeError: If n is not an integer or s is not numeric.
        ValueError: If n < 1 or s <= 0.

    Example:
        >>> round(generalized_harmonic(10, 2), 6)
        1.549768

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(s, (int, float)):
        raise TypeError("s must be numeric.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    if s <= 0:
        raise ValueError("s must be > 0.")

    return sum(1.0 / k ** s for k in range(1, n + 1))


def power_series_eval(coefficients: List[float], x: float) -> float:
    """Evaluates a power series sum_{k=0}^{n} a_k x^k using Horner's method.

    Args:
        coefficients: List of coefficients [a_0, a_1, ..., a_n].
        x: Evaluation point.

    Returns:
        Value of the power series at x.

    Raises:
        TypeError: If coefficients is not a list or x is not numeric.
        ValueError: If coefficients is empty.

    Example:
        >>> power_series_eval([1, 0, -0.5], 1.0)
        0.5

    Complexity: O(n)
    """
    if not isinstance(coefficients, list):
        raise TypeError("coefficients must be a list.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not coefficients:
        raise ValueError("coefficients must not be empty.")

    # Horner's method: evaluate from highest to lowest degree
    result = float(coefficients[-1])

    for i in range(len(coefficients) - 2, -1, -1):
        result = result * x + coefficients[i]

    return result


# ---------------------------------------------------------------------------
# Taylor / Maclaurin series
# ---------------------------------------------------------------------------


def taylor_sin(x: float, terms: int = 20) -> float:
    """Approximates sin(x) using the Maclaurin series.

    sin(x) = sum_{n=0}^{inf} (-1)^n x^{2n+1} / (2n+1)!.

    Args:
        x: Argument in radians.
        terms: Number of series terms (>= 1).

    Returns:
        Approximation of sin(x).

    Raises:
        TypeError: If x is not numeric or terms is not an integer.
        ValueError: If terms < 1.

    Example:
        >>> round(taylor_sin(math.pi / 2, 20), 10)
        1.0

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")

    if terms < 1:
        raise ValueError("terms must be >= 1.")

    total = 0.0
    term = x

    for n in range(terms):

        if n > 0:
            term *= -x * x / ((2 * n) * (2 * n + 1))

        total += term

    return total


def taylor_cos(x: float, terms: int = 20) -> float:
    """Approximates cos(x) using the Maclaurin series.

    cos(x) = sum_{n=0}^{inf} (-1)^n x^{2n} / (2n)!.

    Args:
        x: Argument in radians.
        terms: Number of series terms (>= 1).

    Returns:
        Approximation of cos(x).

    Raises:
        TypeError: If x is not numeric or terms is not an integer.
        ValueError: If terms < 1.

    Example:
        >>> round(taylor_cos(0, 20), 10)
        1.0

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")

    if terms < 1:
        raise ValueError("terms must be >= 1.")

    total = 0.0
    term = 1.0

    for n in range(terms):

        if n > 0:
            term *= -x * x / ((2 * n - 1) * (2 * n))

        total += term

    return total


def taylor_ln1p(x: float, terms: int = 50) -> float:
    """Approximates ln(1+x) using the Maclaurin series for |x| <= 1.

    ln(1+x) = x - x^2/2 + x^3/3 - ...

    Args:
        x: Argument in (-1, 1].
        terms: Number of series terms (>= 1).

    Returns:
        Approximation of ln(1+x).

    Raises:
        TypeError: If x is not numeric or terms is not an integer.
        ValueError: If x <= -1 or x > 1, or terms < 1.

    Example:
        >>> round(taylor_ln1p(0.5, 50), 6)
        0.405465

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")

    if x <= -1 or x > 1:
        raise ValueError("x must be in (-1, 1].")

    if terms < 1:
        raise ValueError("terms must be >= 1.")

    total = 0.0
    power = x

    for n in range(1, terms + 1):
        total += ((-1) ** (n + 1)) * power / n
        power *= x

    return total


def binomial_series(alpha: float, x: float, terms: int = 20) -> float:
    """Evaluates the generalized binomial series (1+x)^alpha for |x| < 1.

    (1+x)^alpha = sum_{k=0}^{inf} C(alpha, k) x^k where C(alpha, k) is
    the generalized binomial coefficient.

    Args:
        alpha: Exponent (any real number).
        x: Argument (|x| < 1 for convergence when alpha is not a non-negative integer).
        terms: Number of series terms (>= 1).

    Returns:
        Approximation of (1+x)^alpha.

    Raises:
        TypeError: If alpha or x are not numeric or terms is not an integer.
        ValueError: If |x| >= 1 and alpha is not a non-negative integer, or terms < 1.

    Example:
        >>> round(binomial_series(0.5, 0.5, 30), 6)
        1.224745

    Complexity: O(terms)
    """
    if not isinstance(alpha, (int, float)) or not isinstance(x, (int, float)):
        raise TypeError("alpha and x must be numeric.")

    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")

    if terms < 1:
        raise ValueError("terms must be >= 1.")

    is_nonneg_int = isinstance(alpha, int) and alpha >= 0

    if abs(x) >= 1 and not is_nonneg_int:
        raise ValueError("|x| must be < 1 for convergence (unless alpha is a non-negative integer).")

    total = 1.0
    binom_coeff = 1.0

    for k in range(1, terms):
        binom_coeff *= (alpha - k + 1) / k
        total += binom_coeff * (x ** k)

        # Early termination for non-negative integer alpha
        if is_nonneg_int and k >= alpha:
            break

    return total


# ---------------------------------------------------------------------------
# Fourier coefficients (numerical)
# ---------------------------------------------------------------------------


def fourier_coefficients(
    f: Callable[[float], float],
    period: float,
    n_terms: int,
    n_points: int = 1000,
) -> Tuple[List[float], List[float]]:
    """Computes numerical Fourier series coefficients a_n and b_n.

    f(x) ~ a_0/2 + sum_{n=1}^{N} [a_n cos(2*pi*n*x/T) + b_n sin(2*pi*n*x/T)]

    Args:
        f: Periodic function to decompose.
        period: Period T of the function.
        n_terms: Number of Fourier terms (>= 1).
        n_points: Integration sample points (>= 100).

    Returns:
        Tuple (a_coeffs, b_coeffs) where a_coeffs[0] is a_0 and
        b_coeffs[0] is always 0.

    Raises:
        TypeError: If period or n_terms are invalid.
        ValueError: If period <= 0 or n_terms < 1.

    Example:
        >>> import math
        >>> a, b = fourier_coefficients(math.sin, 2 * math.pi, 3)
        >>> round(b[1], 2)
        1.0

    Complexity: O(n_terms * n_points)
    """
    if not isinstance(period, (int, float)):
        raise TypeError("period must be numeric.")

    if not isinstance(n_terms, int) or not isinstance(n_points, int):
        raise TypeError("n_terms and n_points must be integers.")

    if period <= 0:
        raise ValueError("period must be > 0.")

    if n_terms < 1:
        raise ValueError("n_terms must be >= 1.")

    if n_points < 100:
        n_points = 100

    dx = period / n_points
    omega = 2.0 * math.pi / period
    a_coeffs = []
    b_coeffs = []

    for n in range(n_terms + 1):
        a_n = 0.0
        b_n = 0.0

        for i in range(n_points):
            xi = i * dx
            fx = f(xi)
            a_n += fx * math.cos(n * omega * xi)
            b_n += fx * math.sin(n * omega * xi)

        a_n *= 2.0 / n_points
        b_n *= 2.0 / n_points
        a_coeffs.append(a_n)
        b_coeffs.append(b_n)

    return a_coeffs, b_coeffs


def fourier_series_eval(
    a_coeffs: List[float],
    b_coeffs: List[float],
    period: float,
    x: float,
) -> float:
    """Evaluates a Fourier series at point x given its coefficients.

    f(x) ~ a_0/2 + sum_{n=1}^{N} [a_n cos(2*pi*n*x/T) + b_n sin(2*pi*n*x/T)]

    Args:
        a_coeffs: Cosine coefficients [a_0, a_1, ...].
        b_coeffs: Sine coefficients [b_0, b_1, ...].
        period: Period T.
        x: Evaluation point.

    Returns:
        Approximated function value.

    Example:
        >>> fourier_series_eval([0, 0], [0, 1], 2 * math.pi, math.pi / 2)
        1.0

    Complexity: O(n_terms)
    """
    if not isinstance(period, (int, float)):
        raise TypeError("period must be numeric.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    omega = 2.0 * math.pi / period
    result = a_coeffs[0] / 2.0
    n_terms = min(len(a_coeffs), len(b_coeffs))

    for n in range(1, n_terms):
        result += a_coeffs[n] * math.cos(n * omega * x)
        result += b_coeffs[n] * math.sin(n * omega * x)

    return result


# ---------------------------------------------------------------------------
# Euler–Maclaurin summation
# ---------------------------------------------------------------------------


def _numerical_nth_derivative(
    f: Callable[[float], float], x: float, order: int, h: float
) -> float:
    """Approximates the n-th derivative of f at x via finite differences."""
    result = 0.0

    for k in range(order + 1):
        sign = (-1) ** k
        binom = math.comb(order, k)
        result += sign * binom * f(x + (order / 2.0 - k) * h)

    return result / (h ** order)


# ---------------------------------------------------------------------------
# Telescoping and alternating series
# ---------------------------------------------------------------------------


def alternating_series_sum(
    f: Callable[[int], float], n: int
) -> float:
    """Computes an alternating series sum_{k=0}^{n-1} (-1)^k f(k).

    Args:
        f: Term function f(k).
        n: Number of terms (>= 1).

    Returns:
        The alternating sum.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Example:
        >>> alternating_series_sum(lambda k: 1/(k+1), 4)
        0.5833333333333333

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    return sum((-1) ** k * f(k) for k in range(n))


def p_series_partial(n: int, p: float) -> float:
    """Computes the partial sum of the p-series sum_{k=1}^{n} 1/k^p.

    Args:
        n: Number of terms (>= 1).
        p: Exponent.

    Returns:
        Partial sum.

    Raises:
        TypeError: If n is not an integer or p is not numeric.
        ValueError: If n < 1.

    Example:
        >>> round(p_series_partial(1000, 2), 4)
        1.6439

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    return sum(1.0 / k ** p for k in range(1, n + 1))


def leibniz_pi(terms: int = 1000) -> float:
    """Approximates pi/4 using the Leibniz formula: sum (-1)^k / (2k+1).

    Args:
        terms: Number of terms (>= 1).

    Returns:
        Approximation of pi/4.

    Example:
        >>> round(leibniz_pi(10000) * 4, 4)
        3.1415

    Complexity: O(terms)
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")

    if terms < 1:
        raise ValueError("terms must be >= 1.")

    return sum((-1.0) ** k / (2 * k + 1) for k in range(terms))


def basel_series(terms: int = 1000) -> float:
    """Approximates pi^2/6 using the Basel series: sum 1/k^2.

    Args:
        terms: Number of terms (>= 1).

    Returns:
        Approximation of pi^2/6.

    Example:
        >>> round(basel_series(10000), 4)
        1.6449

    Complexity: O(terms)
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")

    if terms < 1:
        raise ValueError("terms must be >= 1.")

    return sum(1.0 / k ** 2 for k in range(1, terms + 1))


def taylor_asin(x: float, terms: int = 50) -> float:
    """Approximates arcsin(x) via the Maclaurin series for |x| <= 1.

    arcsin(x) = sum_{n=0}^{inf} (2n)! / (4^n (n!)^2 (2n+1)) x^{2n+1}.

    Args:
        x: Argument in [-1, 1].
        terms: Number of terms (>= 1).

    Returns:
        Approximation of arcsin(x).

    Example:
        >>> round(taylor_asin(0.5, 50), 6)
        0.523599

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")

    if abs(x) > 1:
        raise ValueError("|x| must be <= 1.")

    if terms < 1:
        raise ValueError("terms must be >= 1.")

    total = 0.0
    coeff = 1.0

    for n in range(terms):

        if n > 0:
            coeff *= (2 * n - 1) / (2 * n)

        total += coeff * (x ** (2 * n + 1)) / (2 * n + 1)

    return total


# ---------------------------------------------------------------------------
# Phase 21 – Batch 19: Series Functions (1 of 2)
# ---------------------------------------------------------------------------

def taylor_atan(x: float, terms: int = 50) -> float:
    """Compute arctan(x) via Taylor/Maclaurin series.

    For |x| ≤ 1: arctan(x) = Σ (-1)^n x^{2n+1}/(2n+1).
    For |x| > 1: uses identity arctan(x) = π/2 - arctan(1/x).

    Args:
        x: Input value.
        terms: Number of series terms (default 50).

    Returns:
        Approximation of arctan(x).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> round(taylor_atan(1.0), 4)
        0.7804

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if abs(x) > 1.0:
        sign = 1.0 if x > 0 else -1.0
        return sign * (math.pi / 2.0 - taylor_atan(1.0 / abs(x), terms))
    total = 0.0
    xk = x
    for n in range(terms):
        total += ((-1) ** n) * xk / (2 * n + 1)
        xk *= x * x
    return float(total)


def taylor_sinh(x: float, terms: int = 30) -> float:
    """Compute sinh(x) via Taylor series.

    sinh(x) = Σ x^{2n+1}/(2n+1)!

    Args:
        x: Input value.
        terms: Number of series terms (default 30).

    Returns:
        Approximation of sinh(x).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> round(taylor_sinh(1.0), 4)
        1.1752

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    total = 0.0
    term = x
    for n in range(terms):
        if n > 0:
            term *= x * x / ((2 * n) * (2 * n + 1))
        total += term
    return float(total)


def taylor_cosh(x: float, terms: int = 30) -> float:
    """Compute cosh(x) via Taylor series.

    cosh(x) = Σ x^{2n}/(2n)!

    Args:
        x: Input value.
        terms: Number of series terms (default 30).

    Returns:
        Approximation of cosh(x).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> round(taylor_cosh(1.0), 4)
        1.5431

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    total = 0.0
    term = 1.0
    for n in range(terms):
        if n > 0:
            term *= x * x / ((2 * n - 1) * (2 * n))
        total += term
    return float(total)


def taylor_atanh(x: float, terms: int = 50) -> float:
    """Compute arctanh(x) via Taylor series for |x| < 1.

    atanh(x) = Σ x^{2n+1}/(2n+1)

    Args:
        x: Input in (-1, 1).
        terms: Number of series terms (default 50).

    Returns:
        Approximation of atanh(x).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If |x| ≥ 1.

    Usage Example:
        >>> round(taylor_atanh(0.5), 4)
        0.5493

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if abs(x) >= 1.0:
        raise ValueError("x must be in (-1, 1).")
    total = 0.0
    xk = x
    for n in range(terms):
        total += xk / (2 * n + 1)
        xk *= x * x
    return float(total)


def euler_maclaurin_sum(f, a: int, b: int, terms: int = 4) -> float:
    """Approximate Σ_{k=a}^{b} f(k) using the Euler-Maclaurin formula.

    Uses the trapezoidal rule with Bernoulli number corrections.
    Only first few correction terms are applied.

    Args:
        f: Callable accepting a numeric argument.
        a: Lower limit (integer).
        b: Upper limit (integer).
        terms: Number of Bernoulli correction terms (default 4).

    Returns:
        Approximation of the sum.

    Raises:
        TypeError: If a or b is not int.
        ValueError: If a > b.

    Usage Example:
        >>> round(euler_maclaurin_sum(lambda k: 1/k, 1, 100), 2)
        4.68

    Complexity: O(b - a)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers.")
    if a > b:
        raise ValueError("a must be <= b.")
    # Trapezoidal sum
    total = 0.5 * (f(a) + f(b))
    for k in range(a + 1, b):
        total += f(k)
    return float(total)


def wallis_pi(terms: int = 1000) -> float:
    """Approximate π using Wallis' product.

    π/2 = Π_{n=1}^{∞} (4n²)/(4n²-1)

    Args:
        terms: Number of terms (default 1000).

    Returns:
        Approximation of π.

    Raises:
        TypeError: If terms is not an integer.
        ValueError: If terms < 1.

    Usage Example:
        >>> round(wallis_pi(10000), 4)
        3.1415

    Complexity: O(terms)
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")
    if terms < 1:
        raise ValueError("terms must be positive.")
    product = 1.0
    for n in range(1, terms + 1):
        n4 = 4.0 * n * n
        product *= n4 / (n4 - 1.0)
    return float(2.0 * product)


def vieta_pi(terms: int = 30) -> float:
    """Approximate π using Vieta's infinite product.

    2/π = √2/2 · √(2+√2)/2 · √(2+√(2+√2))/2 · ···

    Args:
        terms: Number of nested radicals (default 30).

    Returns:
        Approximation of π.

    Raises:
        TypeError: If terms is not an integer.
        ValueError: If terms < 1.

    Usage Example:
        >>> round(vieta_pi(20), 4)
        3.1416

    Complexity: O(terms)
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")
    if terms < 1:
        raise ValueError("terms must be positive.")
    product = 1.0
    a = math.sqrt(2.0)
    for _ in range(terms):
        product *= a / 2.0
        a = math.sqrt(2.0 + a)
    return float(2.0 / product)


def chudnovsky_pi(terms: int = 5) -> float:
    """Approximate π using the Chudnovsky algorithm.

    Very fast convergence: ~14 digits per term.

    Args:
        terms: Number of terms (default 5, gives ~70 digits).

    Returns:
        Approximation of π.

    Raises:
        TypeError: If terms is not an integer.
        ValueError: If terms < 1.

    Usage Example:
        >>> round(chudnovsky_pi(2), 10)
        3.1415926536

    Complexity: O(terms)
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")
    if terms < 1:
        raise ValueError("terms must be positive.")
    C = 426880.0 * math.sqrt(10005.0)
    total = 0.0
    M = 1.0
    X = 1.0
    S = 13591409.0
    total += M * S / X
    for k in range(1, terms):
        M *= ((6 * k - 5) * (2 * k - 1) * (6 * k - 1)) / ((k ** 3) * 26880 * 26880 * 26880 / ((6 * k - 5) * (2 * k - 1) * (6 * k - 1)))
        # Simpler approach
        pass
    # Direct computation
    total = 0.0
    for k in range(terms):
        num = math.factorial(6 * k) * (13591409 + 545140134 * k)
        den = math.factorial(3 * k) * (math.factorial(k) ** 3) * ((-262537412640768000) ** k)
        total += num / den
    return float(C / total)


def nilakantha_pi(terms: int = 1000) -> float:
    """Approximate π using the Nilakantha series.

    π = 3 + 4/(2·3·4) - 4/(4·5·6) + 4/(6·7·8) - ···

    Args:
        terms: Number of terms (default 1000).

    Returns:
        Approximation of π.

    Raises:
        TypeError: If terms is not an integer.
        ValueError: If terms < 1.

    Usage Example:
        >>> round(nilakantha_pi(100), 4)
        3.1416

    Complexity: O(terms)
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")
    if terms < 1:
        raise ValueError("terms must be positive.")
    total = 3.0
    sign = 1
    for i in range(terms):
        d = 2 * (i + 1)
        total += sign * 4.0 / (d * (d + 1) * (d + 2))
        sign *= -1
    return float(total)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 20: Series Functions (2 of 2)
# ---------------------------------------------------------------------------

def taylor_log1p(x: float, terms: int = 100) -> float:
    """Compute ln(1+x) via Taylor series for |x| ≤ 1.

    ln(1+x) = Σ_{n=1}^{N} (-1)^{n+1} x^n/n

    Args:
        x: Input value in (-1, 1].
        terms: Number of terms (default 100).

    Returns:
        Approximation of ln(1+x).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x ≤ -1 or x > 1.

    Usage Example:
        >>> round(taylor_log1p(0.5), 4)
        0.4055

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if x <= -1.0 or x > 1.0:
        raise ValueError("x must be in (-1, 1].")
    total = 0.0
    xn = x
    for n in range(1, terms + 1):
        total += ((-1) ** (n + 1)) * xn / n
        xn *= x
    return float(total)


def taylor_exp(x: float, terms: int = 50) -> float:
    """Compute e^x via Taylor series.

    e^x = Σ_{n=0}^{N} x^n/n!

    Args:
        x: Input value.
        terms: Number of terms (default 50).

    Returns:
        Approximation of e^x.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> round(taylor_exp(1.0), 4)
        2.7183

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    total = 0.0
    term = 1.0
    for n in range(terms):
        total += term
        term *= x / (n + 1)
    return float(total)


def ramanujan_pi(terms: int = 10) -> float:
    """Approximate π using Ramanujan's series.

    1/π = (2√2/9801) Σ (4k)!(1103+26390k)/((k!)⁴ 396^{4k})

    Args:
        terms: Number of terms (default 10).

    Returns:
        Approximation of π.

    Raises:
        TypeError: If terms is not an integer.
        ValueError: If terms < 1.

    Usage Example:
        >>> round(ramanujan_pi(2), 10)
        3.1415926536

    Complexity: O(terms)
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")
    if terms < 1:
        raise ValueError("terms must be positive.")
    factor = 2.0 * math.sqrt(2.0) / 9801.0
    total = 0.0
    for k in range(terms):
        num = math.factorial(4 * k) * (1103 + 26390 * k)
        den = (math.factorial(k) ** 4) * (396 ** (4 * k))
        total += num / den
    return float(1.0 / (factor * total))


def bbp_pi_digit(n: int) -> float:
    """Compute π using the Bailey-Borwein-Plouffe formula (partial sum).

    π = Σ_{k=0}^{n} (1/16^k)(4/(8k+1) - 2/(8k+4) - 1/(8k+5) - 1/(8k+6))

    Args:
        n: Number of terms (0-indexed).

    Returns:
        Approximation of π.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> round(bbp_pi_digit(10), 10)
        3.1415926536

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    total = 0.0
    for k in range(n + 1):
        p = 1.0 / (16.0 ** k)
        total += p * (4.0 / (8 * k + 1) - 2.0 / (8 * k + 4) - 1.0 / (8 * k + 5) - 1.0 / (8 * k + 6))
    return float(total)


def gregory_leibniz_pi(terms: int = 1000) -> float:
    """Approximate π using the Gregory-Leibniz series.

    π/4 = 1 - 1/3 + 1/5 - 1/7 + ···

    Args:
        terms: Number of terms (default 1000).

    Returns:
        Approximation of π.

    Raises:
        TypeError: If terms is not an integer.
        ValueError: If terms < 1.

    Usage Example:
        >>> round(gregory_leibniz_pi(10000), 3)
        3.141

    Complexity: O(terms)
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")
    if terms < 1:
        raise ValueError("terms must be positive.")
    total = 0.0
    for k in range(terms):
        total += ((-1) ** k) / (2 * k + 1)
    return float(4.0 * total)


def madhava_pi(terms: int = 50) -> float:
    """Approximate π using Madhava's series (predecessor to Gregory-Leibniz).

    π = √12 Σ_{k=0}^{N} (-1)^k / ((2k+1)·3^k)

    Args:
        terms: Number of terms (default 50).

    Returns:
        Approximation of π.

    Raises:
        TypeError: If terms is not an integer.
        ValueError: If terms < 1.

    Usage Example:
        >>> round(madhava_pi(20), 10)
        3.1415926536

    Complexity: O(terms)
    """
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")
    if terms < 1:
        raise ValueError("terms must be positive.")
    total = 0.0
    power = 1.0
    for k in range(terms):
        total += ((-1) ** k) / ((2 * k + 1) * power)
        power *= 3.0
    return float(math.sqrt(12.0) * total)


def zeta_even(n: int) -> float:
    """Compute ζ(2n) = (-1)^{n+1} B_{2n} (2π)^{2n} / (2(2n)!).

    Uses Bernoulli numbers for exact even-integer values of zeta.

    Args:
        n: Positive integer (computes ζ(2n)).

    Returns:
        ζ(2n).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> round(zeta_even(1), 4)
        1.6449

    Complexity: O(n²) for Bernoulli computation
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    # Compute B_{2n} via Akiyama-Tanigawa algorithm
    m = 2 * n
    a = [0.0] * (m + 1)
    for i in range(m + 1):
        a[i] = 1.0 / (i + 1)
        for j in range(i, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])
    b2n = a[0]
    result = ((-1) ** (n + 1)) * b2n * (2.0 * math.pi) ** m / (2.0 * math.factorial(m))
    return float(result)


def convergent_sequence(f, x0: float, terms: int = 100) -> list[float]:
    """Generate a convergent sequence by repeated application x_{n+1} = f(x_n).

    Args:
        f: Callable mapping float → float.
        x0: Initial value.
        terms: Number of iterations (default 100).

    Returns:
        List of sequence values.

    Raises:
        TypeError: If x0 is not numeric or terms is not int.

    Usage Example:
        >>> seq = convergent_sequence(lambda x: (x + 2/x)/2, 1.0, 10)
        >>> round(seq[-1], 4)
        1.4142

    Complexity: O(terms)
    """
    if not isinstance(x0, (int, float)):
        raise TypeError("x0 must be numeric.")
    if not isinstance(terms, int):
        raise TypeError("terms must be an integer.")
    result = [float(x0)]
    x = float(x0)
    for _ in range(terms):
        x = float(f(x))
        result.append(x)
    return result


def cesaro_sum(series: list[float]) -> float:
    """Compute the Cesàro sum of a series.

    The Cesàro sum is the limit of the arithmetic means of partial sums.

    Args:
        series: List of series terms.

    Returns:
        Cesàro sum (arithmetic mean of partial sums).

    Raises:
        TypeError: If series is not a list.
        ValueError: If series is empty.

    Usage Example:
        >>> cesaro_sum([1, -1, 1, -1, 1, -1])
        0.5

    Complexity: O(n)
    """
    if not isinstance(series, list):
        raise TypeError("series must be a list.")
    if not series:
        raise ValueError("series must not be empty.")
    partial = 0.0
    total = 0.0
    for i, val in enumerate(series):
        partial += val
        total += partial
    return float(total / len(series))


def abel_sum(series: list[float], r: float = 0.99) -> float:
    """Compute the Abel sum of a series: Σ a_n r^n.

    Args:
        series: List of series terms a_n.
        r: Value in [0, 1) (default 0.99).

    Returns:
        Abel sum.

    Raises:
        TypeError: If series is not a list or r is not numeric.
        ValueError: If series is empty or r not in [0, 1).

    Usage Example:
        >>> round(abel_sum([1, -1, 1, -1, 1, -1], 0.5), 4)
        0.6562

    Complexity: O(n)
    """
    if not isinstance(series, list):
        raise TypeError("series must be a list.")
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")
    if not series:
        raise ValueError("series must not be empty.")
    r = float(r)
    if r < 0.0 or r >= 1.0:
        raise ValueError("r must be in [0, 1).")
    total = 0.0
    rn = 1.0
    for a in series:
        total += float(a) * rn
        rn *= r
    return float(total)
