"""Polynomial algebra and manipulation.

Pure-Python polynomial operations from Murray R. Spiegel's
*Mathematical Handbook of Formulas and Tables*: addition, multiplication,
division, differentiation, integration, GCD, evaluation, and partial-fraction
decomposition.

Polynomials are represented as lists of coefficients in *descending* order
of degree: ``[a_n, a_{n-1}, ..., a_1, a_0]``.
"""

from typing import List, Tuple, Union


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _strip_leading_zeros(p: list) -> list:
    """Remove leading zero coefficients, preserving at least [0]."""

    i = 0

    while i < len(p) - 1 and p[i] == 0:
        i += 1

    return p[i:]


def _validate_poly(p, name: str = "polynomial") -> list:
    """Validate and return a clean polynomial coefficient list."""

    if not isinstance(p, (list, tuple)):
        raise TypeError(f"{name} must be a list of coefficients.")

    if not p:
        raise ValueError(f"{name} must not be empty.")

    for c in p:

        if not isinstance(c, (int, float)):
            raise TypeError(f"All coefficients in {name} must be numeric.")

    return list(p)


# ---------------------------------------------------------------------------
# Basic arithmetic
# ---------------------------------------------------------------------------


def polynomial_add(p: list, q: list) -> list:
    """Adds two polynomials.

    Args:
        p: Coefficients of first polynomial (descending degree).
        q: Coefficients of second polynomial (descending degree).

    Returns:
        Coefficients of the sum polynomial.

    Example:
        >>> polynomial_add([1, 2, 3], [4, 5])
        [1, 6, 8]

    Complexity: O(max(len(p), len(q)))
    """
    p = _validate_poly(p, "p")
    q = _validate_poly(q, "q")

    # Pad shorter to same length
    diff = len(p) - len(q)

    if diff > 0:
        q = [0] * diff + q
    elif diff < 0:
        p = [0] * (-diff) + p

    result = [a + b for a, b in zip(p, q)]
    return _strip_leading_zeros(result)


def polynomial_subtract(p: list, q: list) -> list:
    """Subtracts polynomial q from p.

    Args:
        p: Coefficients of first polynomial (descending degree).
        q: Coefficients of second polynomial (descending degree).

    Returns:
        Coefficients of the difference polynomial p - q.

    Example:
        >>> polynomial_subtract([1, 2, 3], [4, 5])
        [1, -2, -2]

    Complexity: O(max(len(p), len(q)))
    """
    q = _validate_poly(q, "q")
    neg_q = [-c for c in q]
    return polynomial_add(p, neg_q)


def polynomial_multiply(p: list, q: list) -> list:
    """Multiplies two polynomials.

    Args:
        p: Coefficients of first polynomial (descending degree).
        q: Coefficients of second polynomial (descending degree).

    Returns:
        Coefficients of the product polynomial.

    Example:
        >>> polynomial_multiply([1, 1], [1, -1])
        [1, 0, -1]

    Complexity: O(len(p) * len(q))
    """
    p = _validate_poly(p, "p")
    q = _validate_poly(q, "q")

    n = len(p) + len(q) - 1
    result = [0.0] * n

    for i, a in enumerate(p):

        for j, b in enumerate(q):
            result[i + j] += a * b

    # Clean rounding noise
    result = [round(c, 14) if isinstance(c, float) else c for c in result]
    return _strip_leading_zeros(result)


def polynomial_scale(p: list, scalar: Union[int, float]) -> list:
    """Scales a polynomial by a scalar factor.

    Args:
        p: Coefficients (descending degree).
        scalar: Scalar multiplier.

    Returns:
        Scaled polynomial coefficients.

    Example:
        >>> polynomial_scale([1, 2, 3], 2)
        [2, 4, 6]

    Complexity: O(n)
    """
    p = _validate_poly(p, "p")

    if not isinstance(scalar, (int, float)):
        raise TypeError("scalar must be numeric.")

    return [c * scalar for c in p]


def polynomial_divide(p: list, q: list) -> Tuple[list, list]:
    """Divides polynomial p by q, returning (quotient, remainder).

    Uses synthetic long division.

    Args:
        p: Dividend coefficients (descending degree).
        q: Divisor coefficients (descending degree).

    Returns:
        Tuple (quotient_coefficients, remainder_coefficients).

    Raises:
        ValueError: If divisor is zero polynomial.

    Example:
        >>> polynomial_divide([1, -3, 2], [1, -1])
        ([1.0, -2.0], [0.0])

    Complexity: O(n * m) where n = deg(p), m = deg(q)
    """
    p = _validate_poly(p, "p")
    q = _validate_poly(q, "q")
    q = _strip_leading_zeros(q)

    if q == [0]:
        raise ValueError("Cannot divide by zero polynomial.")

    dividend = [float(c) for c in p]
    divisor = [float(c) for c in q]

    if len(dividend) < len(divisor):
        return [0.0], dividend

    quotient = []

    for i in range(len(dividend) - len(divisor) + 1):
        coeff = dividend[i] / divisor[0]
        quotient.append(coeff)

        for j in range(len(divisor)):
            dividend[i + j] -= coeff * divisor[j]

    remainder = _strip_leading_zeros(dividend[len(quotient):]) or [0.0]
    quotient = _strip_leading_zeros(quotient) or [0.0]

    return quotient, remainder


# ---------------------------------------------------------------------------
# Calculus on polynomials
# ---------------------------------------------------------------------------


def polynomial_derivative(p: list) -> list:
    """Computes the derivative of a polynomial.

    Args:
        p: Coefficients (descending degree).

    Returns:
        Coefficients of the derivative polynomial.

    Example:
        >>> polynomial_derivative([3, 0, -2, 1])
        [9, 0, -2]

    Complexity: O(n)
    """
    p = _validate_poly(p, "p")
    n = len(p) - 1

    if n == 0:
        return [0]

    result = []

    for i, c in enumerate(p[:-1]):
        deg = n - i
        result.append(c * deg)

    return _strip_leading_zeros(result)


def polynomial_integral(p: list, constant: Union[int, float] = 0) -> list:
    """Computes the indefinite integral of a polynomial.

    Args:
        p: Coefficients (descending degree).
        constant: Integration constant (default 0).

    Returns:
        Coefficients of the integral polynomial.

    Example:
        >>> polynomial_integral([3, 0, -2])
        [1.0, 0.0, -2.0, 0]

    Complexity: O(n)
    """
    p = _validate_poly(p, "p")

    if not isinstance(constant, (int, float)):
        raise TypeError("constant must be numeric.")

    n = len(p) - 1
    result = []

    for i, c in enumerate(p):
        deg = n - i + 1
        result.append(c / deg)

    result.append(constant)
    return result


def polynomial_evaluate(p: list, x: Union[int, float]) -> float:
    """Evaluates a polynomial at x using Horner's method.

    Args:
        p: Coefficients (descending degree).
        x: Point at which to evaluate.

    Returns:
        Value of p(x).

    Example:
        >>> polynomial_evaluate([1, -3, 2], 2)
        0

    Complexity: O(n)
    """
    p = _validate_poly(p, "p")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    result = 0.0

    for c in p:
        result = result * x + c

    return result


# ---------------------------------------------------------------------------
# GCD and related
# ---------------------------------------------------------------------------


def polynomial_gcd(p: list, q: list) -> list:
    """Computes the GCD of two polynomials using the Euclidean algorithm.

    The result is monic (leading coefficient 1).

    Args:
        p: Coefficients of first polynomial (descending degree).
        q: Coefficients of second polynomial (descending degree).

    Returns:
        Coefficients of the GCD polynomial (monic).

    Example:
        >>> polynomial_gcd([1, -3, 2], [1, -1])
        [1.0, -1.0]

    Complexity: O(n * m) per division, iterated
    """
    p = _validate_poly(p, "p")
    q = _validate_poly(q, "q")

    a = [float(c) for c in p]
    b = [float(c) for c in q]

    while _strip_leading_zeros(b) != [0]:
        _, r = polynomial_divide(a, b)
        a = b
        b = r

    a = _strip_leading_zeros(a)

    # Make monic
    if a[0] != 0:
        lead = a[0]
        a = [c / lead for c in a]

    return a


def polynomial_composition(p: list, q: list) -> list:
    """Computes the composition p(q(x)).

    Args:
        p: Outer polynomial coefficients (descending degree).
        q: Inner polynomial coefficients (descending degree).

    Returns:
        Coefficients of the composed polynomial.

    Example:
        >>> polynomial_composition([1, 0, 1], [1, 1])
        [1, 2, 2]

    Complexity: O(n^2 * m) where n = deg(p), m = deg(q)
    """
    p = _validate_poly(p, "p")
    q = _validate_poly(q, "q")

    result = [0]

    for c in p:
        result = polynomial_multiply(result, q)
        result = polynomial_add(result, [c])

    return result


# ---------------------------------------------------------------------------
# Partial fraction decomposition
# ---------------------------------------------------------------------------


def partial_fraction_simple(
    numerator: list,
    denominator_roots: List[float],
) -> List[float]:
    """Partial-fraction coefficients for simple (non-repeated) linear factors.

    Given N(x) and roots r1, r2, ..., rn of the denominator D(x) = (x-r1)(x-r2)...(x-rn),
    returns coefficients [A1, A2, ..., An] such that
    N(x)/D(x) = A1/(x-r1) + A2/(x-r2) + ... + An/(x-rn).

    The degree of numerator must be less than the number of roots.

    Args:
        numerator: Coefficients of the numerator polynomial (descending degree).
        denominator_roots: List of distinct real roots of the denominator.

    Returns:
        List of partial-fraction coefficients [A1, A2, ...].

    Raises:
        ValueError: If numerator degree >= number of roots or roots are not distinct.

    Example:
        >>> partial_fraction_simple([1], [1, 2])
        [-1.0, 1.0]

    Complexity: O(n^2)
    """
    numerator = _validate_poly(numerator, "numerator")

    if not isinstance(denominator_roots, (list, tuple)):
        raise TypeError("denominator_roots must be a list.")

    n = len(denominator_roots)

    if len(numerator) - 1 >= n:
        raise ValueError("Numerator degree must be less than number of roots.")

    # Check distinct
    for i in range(n):

        for j in range(i + 1, n):

            if abs(denominator_roots[i] - denominator_roots[j]) < 1e-14:
                raise ValueError("All roots must be distinct.")

    coefficients = []

    for i, ri in enumerate(denominator_roots):
        num_val = polynomial_evaluate(numerator, ri)
        denom_val = 1.0

        for j, rj in enumerate(denominator_roots):

            if i != j:
                denom_val *= (ri - rj)

        coefficients.append(num_val / denom_val)

    return coefficients


# ---------------------------------------------------------------------------
# Polynomial from roots
# ---------------------------------------------------------------------------


def polynomial_from_roots(roots: List[Union[int, float]]) -> list:
    """Constructs a monic polynomial from its roots.

    Given roots [r1, r2, ..., rn], returns coefficients of
    (x - r1)(x - r2)...(x - rn).

    Args:
        roots: List of real roots.

    Returns:
        Polynomial coefficients (descending degree, monic).

    Example:
        >>> polynomial_from_roots([1, -1])
        [1, 0, -1]

    Complexity: O(n^2)
    """

    if not isinstance(roots, (list, tuple)):
        raise TypeError("roots must be a list.")

    if not roots:
        return [1]

    result = [1]

    for r in roots:

        if not isinstance(r, (int, float)):
            raise TypeError("All roots must be numeric.")

        result = polynomial_multiply(result, [1, -r])

    return result


def polynomial_degree(p: list) -> int:
    """Returns the degree of a polynomial.

    Args:
        p: Coefficients (descending degree).

    Returns:
        Degree of the polynomial.

    Example:
        >>> polynomial_degree([3, 0, -2, 1])
        3

    Complexity: O(n)
    """
    p = _validate_poly(p, "p")
    p = _strip_leading_zeros(p)
    return len(p) - 1
