"""Special mathematical functions and orthogonal polynomials.

This module implements classical special functions from Murray R. Spiegel's
*Mathematical Handbook of Formulas and Tables*: orthogonal polynomials
(Legendre, Hermite, Laguerre, Chebyshev), Bernoulli/Euler numbers,
elliptic integrals, the Riemann zeta function, and related functions.
"""

import math


# ---------------------------------------------------------------------------
# Orthogonal polynomials
# ---------------------------------------------------------------------------


def legendre_polynomial(n: int, x: float) -> float:
    """Evaluates the Legendre polynomial P_n(x) via Bonnet's recurrence.

    Args:
        n: Degree of the polynomial (>= 0).
        x: Evaluation point, typically in [-1, 1].

    Returns:
        Value of P_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> legendre_polynomial(0, 0.5)
        1.0
        >>> legendre_polynomial(2, 0.5)
        -0.125

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Degree n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("Degree n must be >= 0.")

    if n == 0:
        return 1.0

    if n == 1:
        return float(x)

    p_prev, p_curr = 1.0, float(x)

    for k in range(2, n + 1):
        p_next = ((2 * k - 1) * x * p_curr - (k - 1) * p_prev) / k
        p_prev, p_curr = p_curr, p_next

    return p_curr


def associated_legendre(n: int, m: int, x: float) -> float:
    """Evaluates the associated Legendre function P_n^m(x).

    Uses the recurrence relation starting from P_m^m.

    Args:
        n: Degree (>= 0).
        m: Order (0 <= m <= n).
        x: Evaluation point in [-1, 1].

    Returns:
        Value of P_n^m(x).

    Raises:
        TypeError: If n or m are not integers or x is not numeric.
        ValueError: If n < 0, m < 0, m > n, or |x| > 1.

    Example:
        >>> associated_legendre(1, 1, 0.5)
        -0.8660254037844386

    Complexity: O(n)
    """
    if not isinstance(n, int) or not isinstance(m, int):
        raise TypeError("n and m must be integers.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0 or m < 0:
        raise ValueError("n and m must be >= 0.")

    if m > n:
        raise ValueError("m must be <= n.")

    if abs(x) > 1:
        raise ValueError("x must be in [-1, 1].")

    # P_m^m = (-1)^m (2m-1)!! (1-x^2)^(m/2)
    pmm = 1.0
    if m > 0:
        somx2 = math.sqrt(1.0 - x * x)
        fact = 1.0

        for i in range(1, m + 1):
            pmm *= -fact * somx2
            fact += 2.0

    if n == m:
        return pmm

    # P_{m+1}^m = x(2m+1) P_m^m
    pmm1 = x * (2 * m + 1) * pmm

    if n == m + 1:
        return pmm1

    p_prev, p_curr = pmm, pmm1

    for k in range(m + 2, n + 1):
        p_next = ((2 * k - 1) * x * p_curr - (k + m - 1) * p_prev) / (k - m)
        p_prev, p_curr = p_curr, p_next

    return p_curr


def hermite_polynomial(n: int, x: float) -> float:
    """Evaluates the (physicist's) Hermite polynomial H_n(x).

    Uses the recurrence H_{n+1}(x) = 2x H_n(x) - 2n H_{n-1}(x).

    Args:
        n: Degree (>= 0).
        x: Evaluation point.

    Returns:
        Value of H_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> hermite_polynomial(0, 1.0)
        1.0
        >>> hermite_polynomial(3, 2.0)
        40.0

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Degree n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("Degree n must be >= 0.")

    if n == 0:
        return 1.0

    if n == 1:
        return 2.0 * x

    h_prev, h_curr = 1.0, 2.0 * x

    for k in range(2, n + 1):
        h_next = 2.0 * x * h_curr - 2.0 * (k - 1) * h_prev
        h_prev, h_curr = h_curr, h_next

    return h_curr


def laguerre_polynomial(n: int, x: float) -> float:
    """Evaluates the Laguerre polynomial L_n(x).

    Uses the recurrence L_{n+1}(x) = ((2n+1-x) L_n(x) - n L_{n-1}(x))/(n+1).

    Args:
        n: Degree (>= 0).
        x: Evaluation point (>= 0 for standard applications).

    Returns:
        Value of L_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> laguerre_polynomial(0, 1.0)
        1.0
        >>> laguerre_polynomial(2, 1.0)
        0.5

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Degree n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("Degree n must be >= 0.")

    if n == 0:
        return 1.0

    if n == 1:
        return 1.0 - x

    l_prev, l_curr = 1.0, 1.0 - x

    for k in range(1, n):
        l_next = ((2 * k + 1 - x) * l_curr - k * l_prev) / (k + 1)
        l_prev, l_curr = l_curr, l_next

    return l_curr


def generalized_laguerre_polynomial(n: int, alpha: float, x: float) -> float:
    """Evaluates the generalized (associated) Laguerre polynomial L_n^alpha(x).

    Args:
        n: Degree (>= 0).
        alpha: Parameter (> -1).
        x: Evaluation point.

    Returns:
        Value of L_n^alpha(x).

    Raises:
        TypeError: If n is not an integer or x/alpha is not numeric.
        ValueError: If n < 0 or alpha <= -1.

    Example:
        >>> generalized_laguerre_polynomial(2, 0, 1.0)
        0.5

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Degree n must be an integer.")

    if not isinstance(x, (int, float)) or not isinstance(alpha, (int, float)):
        raise TypeError("x and alpha must be numeric.")

    if n < 0:
        raise ValueError("Degree n must be >= 0.")

    if alpha <= -1:
        raise ValueError("alpha must be > -1.")

    if n == 0:
        return 1.0

    if n == 1:
        return 1.0 + alpha - x

    l_prev = 1.0
    l_curr = 1.0 + alpha - x

    for k in range(1, n):
        l_next = ((2 * k + 1 + alpha - x) * l_curr - (k + alpha) * l_prev) / (k + 1)
        l_prev, l_curr = l_curr, l_next

    return l_curr


def chebyshev_polynomial_first(n: int, x: float) -> float:
    """Evaluates the Chebyshev polynomial of the first kind T_n(x).

    Uses the recurrence T_{n+1}(x) = 2x T_n(x) - T_{n-1}(x).

    Args:
        n: Degree (>= 0).
        x: Evaluation point, typically in [-1, 1].

    Returns:
        Value of T_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> chebyshev_polynomial_first(0, 0.5)
        1.0
        >>> chebyshev_polynomial_first(2, 0.5)
        -0.5

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Degree n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("Degree n must be >= 0.")

    if n == 0:
        return 1.0

    if n == 1:
        return float(x)

    t_prev, t_curr = 1.0, float(x)

    for _ in range(2, n + 1):
        t_next = 2.0 * x * t_curr - t_prev
        t_prev, t_curr = t_curr, t_next

    return t_curr


def chebyshev_polynomial_second(n: int, x: float) -> float:
    """Evaluates the Chebyshev polynomial of the second kind U_n(x).

    Uses the recurrence U_{n+1}(x) = 2x U_n(x) - U_{n-1}(x).

    Args:
        n: Degree (>= 0).
        x: Evaluation point, typically in [-1, 1].

    Returns:
        Value of U_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> chebyshev_polynomial_second(0, 0.5)
        1.0
        >>> chebyshev_polynomial_second(2, 0.5)
        0.0

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("Degree n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("Degree n must be >= 0.")

    if n == 0:
        return 1.0

    if n == 1:
        return 2.0 * x

    u_prev, u_curr = 1.0, 2.0 * x

    for _ in range(2, n + 1):
        u_next = 2.0 * x * u_curr - u_prev
        u_prev, u_curr = u_curr, u_next

    return u_curr


# ---------------------------------------------------------------------------
# Bernoulli and Euler numbers
# ---------------------------------------------------------------------------


def bernoulli_number(n: int) -> float:
    """Computes the n-th Bernoulli number B_n using the Akiyama-Tanigawa algorithm.

    Args:
        n: Index (>= 0).

    Returns:
        The n-th Bernoulli number as a float.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> bernoulli_number(0)
        1.0
        >>> bernoulli_number(1)
        -0.5
        >>> bernoulli_number(2)
        0.16666666666666666

    Complexity: O(n^2)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be >= 0.")

    # Odd Bernoulli numbers (except B_1) are zero
    if n > 1 and n % 2 == 1:
        return 0.0

    a = [0.0] * (n + 1)

    for m in range(n + 1):
        a[m] = 1.0 / (m + 1)

        for j in range(m, 0, -1):
            a[j - 1] = j * (a[j - 1] - a[j])

    # Akiyama–Tanigawa yields B_1^+ = +1/2; standard convention is B_1 = -1/2
    if n == 1:
        return -a[0]

    return a[0]


def euler_number(n: int) -> int:
    """Computes the n-th Euler number E_n.

    Euler numbers E_n are defined by the generating function
    1/cosh(t) = sum_{n>=0} E_n t^n / n!. Odd Euler numbers are zero.

    Args:
        n: Index (>= 0).

    Returns:
        The n-th Euler number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> euler_number(0)
        1
        >>> euler_number(2)
        -1
        >>> euler_number(4)
        5

    Complexity: O(n^2)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be >= 0.")

    if n % 2 == 1:
        return 0

    # Recurrence: sum_{k=0}^{m} C(2m, 2k) E_{2k} = 0 for m >= 1
    half = n // 2
    e_even = [0] * (half + 1)
    e_even[0] = 1  # E_0 = 1

    for m in range(1, half + 1):
        s = 0

        for k in range(m):
            s += math.comb(2 * m, 2 * k) * e_even[k]

        e_even[m] = -s

    return e_even[half]


def bernoulli_polynomial(n: int, x: float) -> float:
    """Evaluates the n-th Bernoulli polynomial B_n(x).

    B_n(x) = sum_{k=0}^{n} C(n,k) B_k x^{n-k}.

    Args:
        n: Degree (>= 0).
        x: Evaluation point.

    Returns:
        Value of B_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> bernoulli_polynomial(0, 0.5)
        1.0
        >>> bernoulli_polynomial(1, 0.5)
        0.0

    Complexity: O(n^2) due to Bernoulli numbers.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("n must be >= 0.")

    result = 0.0
    binom = 1

    for k in range(n + 1):
        result += binom * bernoulli_number(k) * (x ** (n - k))

        if k < n:
            binom = binom * (n - k) // (k + 1)

    return result


def euler_polynomial(n: int, x: float) -> float:
    """Evaluates the n-th Euler polynomial E_n(x).

    E_n(x) = sum_{k=0}^{n} C(n,k) (E_k / 2^k) (x - 1/2)^{n-k}.

    Args:
        n: Degree (>= 0).
        x: Evaluation point.

    Returns:
        Value of E_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> euler_polynomial(0, 1.0)
        1.0
        >>> euler_polynomial(1, 0.5)
        0.0

    Complexity: O(n^2)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("n must be >= 0.")

    result = 0.0
    binom = 1

    for k in range(n + 1):
        ek = euler_number(k)
        result += binom * (ek / (2.0 ** k)) * ((x - 0.5) ** (n - k))

        if k < n:
            binom = binom * (n - k) // (k + 1)

    return result


# ---------------------------------------------------------------------------
# Beta, incomplete gamma/beta, digamma
# ---------------------------------------------------------------------------


def beta_function(a: float, b: float) -> float:
    """Computes the beta function B(a, b) = Gamma(a)*Gamma(b)/Gamma(a+b).

    Args:
        a: First parameter (> 0).
        b: Second parameter (> 0).

    Returns:
        Value of B(a, b).

    Raises:
        TypeError: If a or b are not numeric.
        ValueError: If a <= 0 or b <= 0.

    Example:
        >>> round(beta_function(2, 3), 10)
        0.0833333333

    Complexity: O(1)
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numeric.")

    if a <= 0 or b <= 0:
        raise ValueError("a and b must be > 0.")

    return math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))


def incomplete_gamma_lower(a: float, x: float) -> float:
    """Computes the regularized lower incomplete gamma function P(a, x).

    Uses the series expansion for convergence.

    Args:
        a: Shape parameter (> 0).
        x: Upper limit of integration (>= 0).

    Returns:
        Regularized lower incomplete gamma P(a, x) in [0, 1].

    Raises:
        TypeError: If a or x are not numeric.
        ValueError: If a <= 0 or x < 0.

    Example:
        >>> round(incomplete_gamma_lower(1.0, 1.0), 6)
        0.632121

    Complexity: O(a + x) iterations typically.
    """
    if not isinstance(a, (int, float)) or not isinstance(x, (int, float)):
        raise TypeError("a and x must be numeric.")

    if a <= 0:
        raise ValueError("a must be > 0.")

    if x < 0:
        raise ValueError("x must be >= 0.")

    if x == 0:
        return 0.0

    # Series expansion: P(a,x) = e^{-x} x^a sum_{n=0}^{inf} x^n / Gamma(a+n+1)
    max_iter = 200
    tolerance = 1e-15
    term = 1.0 / a
    total = term

    for n in range(1, max_iter):
        term *= x / (a + n)
        total += term

        if abs(term) < tolerance:
            break

    return total * math.exp(-x + a * math.log(x) - math.lgamma(a))


def incomplete_beta_regularized(a: float, b: float, x: float) -> float:
    """Computes the regularized incomplete beta function I_x(a, b).

    Uses the continued-fraction representation for numerical stability.

    Args:
        a: First parameter (> 0).
        b: Second parameter (> 0).
        x: Evaluation point in [0, 1].

    Returns:
        I_x(a, b) in [0, 1].

    Raises:
        TypeError: If a, b, or x are not numeric.
        ValueError: If a <= 0, b <= 0, or x not in [0, 1].

    Example:
        >>> round(incomplete_beta_regularized(2, 3, 0.5), 6)
        0.6875

    Complexity: O(max_iterations) with continued fraction convergence.
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numeric.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if a <= 0 or b <= 0:
        raise ValueError("a and b must be > 0.")

    if x < 0 or x > 1:
        raise ValueError("x must be in [0, 1].")

    if x == 0:
        return 0.0

    if x == 1:
        return 1.0

    # Use symmetry relation for better convergence
    if x > (a + 1) / (a + b + 2):
        return 1.0 - incomplete_beta_regularized(b, a, 1.0 - x)

    log_prefix = (
        math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
        + a * math.log(x) + b * math.log(1.0 - x)
    )

    # Lentz's continued fraction
    max_iter = 200
    tolerance = 1e-15
    qab = a + b
    qap = a + 1.0
    qam = a - 1.0
    c = 1.0
    d = 1.0 - qab * x / qap

    if abs(d) < 1e-30:
        d = 1e-30

    d = 1.0 / d
    h = d

    for m in range(1, max_iter + 1):
        m2 = 2 * m
        # Even step
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d

        if abs(d) < 1e-30:
            d = 1e-30

        c = 1.0 + aa / c

        if abs(c) < 1e-30:
            c = 1e-30

        d = 1.0 / d
        h *= d * c

        # Odd step
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d

        if abs(d) < 1e-30:
            d = 1e-30

        c = 1.0 + aa / c

        if abs(c) < 1e-30:
            c = 1e-30

        d = 1.0 / d
        delta = d * c
        h *= delta

        if abs(delta - 1.0) < tolerance:
            break

    return math.exp(log_prefix) * h / a


def riemann_zeta(s: float) -> float:
    """Computes the Riemann zeta function zeta(s) for real s > 1.

    Uses the Borwein algorithm (Dirichlet-series acceleration) for convergence.

    Args:
        s: Real argument (> 1 for convergence of the standard series).

    Returns:
        Value of zeta(s).

    Raises:
        TypeError: If s is not numeric.
        ValueError: If s <= 1.

    Example:
        >>> round(riemann_zeta(2), 6)
        1.644934

    Complexity: O(n) where n is the number of Borwein terms.
    """
    if not isinstance(s, (int, float)):
        raise TypeError("s must be numeric.")

    if s <= 1:
        raise ValueError("s must be > 1.")

    # Direct series + integral tail: zeta(s) ≈ sum_{k=1}^{N} 1/k^s + N^{1-s}/(s-1) + 0.5/N^s
    big_n = 100000
    total = sum(1.0 / k ** s for k in range(1, big_n + 1))
    # Euler–Maclaurin first-order correction
    total += big_n ** (1.0 - s) / (s - 1.0) + 0.5 / big_n ** s
    return total


# ---------------------------------------------------------------------------
# Elliptic integrals
# ---------------------------------------------------------------------------


def elliptic_k(k: float) -> float:
    """Computes the complete elliptic integral of the first kind K(k).

    Uses the arithmetic-geometric mean (AGM) method.

    Args:
        k: Modulus in [0, 1).

    Returns:
        Value of K(k).

    Raises:
        TypeError: If k is not numeric.
        ValueError: If k is not in [0, 1).

    Example:
        >>> round(elliptic_k(0.0), 10)
        1.5707963268
        >>> round(elliptic_k(0.5), 6)
        1.854075

    Complexity: O(log(1/epsilon)) — converges quadratically.
    """
    if not isinstance(k, (int, float)):
        raise TypeError("k must be numeric.")

    if k < 0 or k >= 1:
        raise ValueError("k must be in [0, 1).")

    a, b = 1.0, math.sqrt(1.0 - k * k)

    while abs(a - b) > 1e-15:
        a, b = (a + b) / 2.0, math.sqrt(a * b)

    return math.pi / (2.0 * a)


def elliptic_e(k: float) -> float:
    """Computes the complete elliptic integral of the second kind E(k).

    Uses the AGM method with the auxiliary series.

    Args:
        k: Modulus in [0, 1].

    Returns:
        Value of E(k).

    Raises:
        TypeError: If k is not numeric.
        ValueError: If k is not in [0, 1].

    Example:
        >>> round(elliptic_e(0.0), 10)
        1.5707963268
        >>> round(elliptic_e(0.5), 6)
        1.350644

    Complexity: O(log(1/epsilon))
    """
    if not isinstance(k, (int, float)):
        raise TypeError("k must be numeric.")

    if k < 0 or k > 1:
        raise ValueError("k must be in [0, 1].")

    if k == 1:
        return 1.0

    a, b = 1.0, math.sqrt(1.0 - k * k)
    c_sq_sum = k * k
    power_of_two = 1.0

    while abs(a - b) > 1e-15:
        a_new = (a + b) / 2.0
        b_new = math.sqrt(a * b)
        c = (a - b) / 2.0
        power_of_two *= 2.0
        c_sq_sum += power_of_two * c * c
        a, b = a_new, b_new

    return (math.pi / (2.0 * a)) * (1.0 - c_sq_sum / 2.0)


def elliptic_f(phi: float, k: float) -> float:
    """Computes the incomplete elliptic integral of the first kind F(phi, k).

    Uses numerical integration (Gauss-Legendre quadrature).

    Args:
        phi: Amplitude angle in radians [0, pi/2].
        k: Modulus in [0, 1).

    Returns:
        Value of F(phi, k).

    Raises:
        TypeError: If phi or k are not numeric.
        ValueError: If phi not in [0, pi/2] or k not in [0, 1).

    Example:
        >>> round(elliptic_f(math.pi / 2, 0.5), 6)
        1.854075

    Complexity: O(n) for n quadrature points.
    """
    if not isinstance(phi, (int, float)) or not isinstance(k, (int, float)):
        raise TypeError("phi and k must be numeric.")

    if phi < 0 or phi > math.pi / 2:
        raise ValueError("phi must be in [0, pi/2].")

    if k < 0 or k >= 1:
        raise ValueError("k must be in [0, 1).")

    if phi == 0:
        return 0.0

    # Gauss-Legendre 20-point quadrature
    n = 20
    total = 0.0

    for i in range(1, n + 1):
        theta = phi * (2 * i - 1) / (2 * n)
        sin_theta = math.sin(theta)
        total += 1.0 / math.sqrt(1.0 - k * k * sin_theta * sin_theta)

    return phi * total / n


def elliptic_e_incomplete(phi: float, k: float) -> float:
    """Computes the incomplete elliptic integral of the second kind E(phi, k).

    Args:
        phi: Amplitude angle in radians [0, pi/2].
        k: Modulus in [0, 1].

    Returns:
        Value of E(phi, k).

    Raises:
        TypeError: If phi or k are not numeric.
        ValueError: If phi not in [0, pi/2] or k not in [0, 1].

    Example:
        >>> round(elliptic_e_incomplete(math.pi / 2, 0.5), 6)
        1.350644

    Complexity: O(n) for n quadrature points.
    """
    if not isinstance(phi, (int, float)) or not isinstance(k, (int, float)):
        raise TypeError("phi and k must be numeric.")

    if phi < 0 or phi > math.pi / 2:
        raise ValueError("phi must be in [0, pi/2].")

    if k < 0 or k > 1:
        raise ValueError("k must be in [0, 1].")

    if phi == 0:
        return 0.0

    n = 20
    total = 0.0

    for i in range(1, n + 1):
        theta = phi * (2 * i - 1) / (2 * n)
        sin_theta = math.sin(theta)
        total += math.sqrt(1.0 - k * k * sin_theta * sin_theta)

    return phi * total / n


def elliptic_pi(n_param: float, k: float) -> float:
    """Computes the complete elliptic integral of the third kind Pi(n, k).

    Uses numerical quadrature.

    Args:
        n_param: Characteristic parameter (n < 1).
        k: Modulus in [0, 1).

    Returns:
        Value of Pi(n, k).

    Raises:
        TypeError: If n_param or k are not numeric.
        ValueError: If n_param >= 1 or k not in [0, 1).

    Example:
        >>> round(elliptic_pi(0.5, 0.3), 4)
        2.8015

    Complexity: O(n) quadrature points.
    """
    if not isinstance(n_param, (int, float)) or not isinstance(k, (int, float)):
        raise TypeError("n_param and k must be numeric.")

    if n_param >= 1:
        raise ValueError("n_param must be < 1.")

    if k < 0 or k >= 1:
        raise ValueError("k must be in [0, 1).")

    num_points = 40
    total = 0.0
    half_pi = math.pi / 2.0

    for i in range(1, num_points + 1):
        theta = half_pi * (2 * i - 1) / (2 * num_points)
        sin_theta = math.sin(theta)
        sin2 = sin_theta * sin_theta
        total += 1.0 / ((1.0 - n_param * sin2) * math.sqrt(1.0 - k * k * sin2))

    return half_pi * total / num_points


# ---------------------------------------------------------------------------
# Hypergeometric function
# ---------------------------------------------------------------------------


def hypergeometric_2f1(a: float, b: float, c: float, z: float) -> float:
    """Computes the Gauss hypergeometric function 2F1(a, b; c; z).

    Uses the series expansion sum_{n=0}^{inf} (a)_n (b)_n / ((c)_n n!) z^n.

    Args:
        a: First numerator parameter.
        b: Second numerator parameter.
        c: Denominator parameter (must not be 0 or a negative integer).
        z: Argument (|z| < 1 for convergence).

    Returns:
        Value of 2F1(a, b; c; z).

    Raises:
        TypeError: If parameters are not numeric.
        ValueError: If c is 0 or a negative integer, or |z| >= 1.

    Example:
        >>> round(hypergeometric_2f1(1, 1, 2, 0.5), 6)
        1.386294

    Complexity: O(max_terms)
    """
    if not all(isinstance(v, (int, float)) for v in (a, b, c, z)):
        raise TypeError("All parameters must be numeric.")

    if c == 0 or (c < 0 and c == int(c)):
        raise ValueError("c must not be 0 or a negative integer.")

    if abs(z) >= 1:
        raise ValueError("|z| must be < 1 for series convergence.")

    max_terms = 500
    tolerance = 1e-15
    total = 1.0
    term = 1.0

    for n in range(1, max_terms):
        term *= (a + n - 1) * (b + n - 1) / ((c + n - 1) * n) * z
        total += term

        if abs(term) < tolerance:
            break

    return total


# ---------------------------------------------------------------------------
# Airy functions
# ---------------------------------------------------------------------------


def airy_ai(x: float) -> float:
    """Computes the Airy function Ai(x) via power-series/asymptotic expansion.

    Args:
        x: Evaluation point.

    Returns:
        Value of Ai(x).

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> round(airy_ai(0), 6)
        0.355028

    Complexity: O(n) series terms.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    # Ai(0) = 1 / (3^{2/3} Gamma(2/3))
    # Use the Maclaurin series
    c1 = 1.0 / (3.0 ** (2.0 / 3.0) * math.gamma(2.0 / 3.0))
    c2 = -1.0 / (3.0 ** (1.0 / 3.0) * math.gamma(1.0 / 3.0))

    f_sum = 0.0
    g_sum = 0.0
    f_term = 1.0
    g_term = x

    max_terms = 100

    for k in range(max_terms):

        if k == 0:
            f_term = 1.0
            g_term = x
        else:
            f_term *= x * x * x / ((3 * k - 1) * (3 * k))
            g_term *= x * x * x / ((3 * k) * (3 * k + 1))

        f_sum += f_term
        g_sum += g_term

        if abs(f_term) < 1e-15 and abs(g_term) < 1e-15:
            break

    return c1 * f_sum + c2 * g_sum


def airy_bi(x: float) -> float:
    """Computes the Airy function Bi(x) via power-series expansion.

    Args:
        x: Evaluation point.

    Returns:
        Value of Bi(x).

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> round(airy_bi(0), 6)
        0.614927

    Complexity: O(n) series terms.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    c1 = 1.0 / (3.0 ** (1.0 / 6.0) * math.gamma(2.0 / 3.0))
    c2 = 3.0 ** (1.0 / 6.0) / math.gamma(1.0 / 3.0)

    f_sum = 0.0
    g_sum = 0.0
    f_term = 1.0
    g_term = x

    max_terms = 100

    for k in range(max_terms):

        if k == 0:
            f_term = 1.0
            g_term = x
        else:
            f_term *= x * x * x / ((3 * k - 1) * (3 * k))
            g_term *= x * x * x / ((3 * k) * (3 * k + 1))

        f_sum += f_term
        g_sum += g_term

        if abs(f_term) < 1e-15 and abs(g_term) < 1e-15:
            break

    return c1 * f_sum + c2 * g_sum


# ---------------------------------------------------------------------------
# Spherical Bessel functions
# ---------------------------------------------------------------------------


def spherical_bessel_j(n: int, x: float) -> float:
    """Computes the spherical Bessel function of the first kind j_n(x).

    j_n(x) = sqrt(pi/(2x)) J_{n+1/2}(x).

    Args:
        n: Order (>= 0).
        x: Evaluation point.

    Returns:
        Value of j_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> round(spherical_bessel_j(0, 1.0), 6)
        0.841471

    Complexity: O(n) via forward recurrence.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("n must be >= 0.")

    if x == 0:
        return 1.0 if n == 0 else 0.0

    # j_0(x) = sin(x)/x, j_1(x) = sin(x)/x^2 - cos(x)/x
    if n == 0:
        return math.sin(x) / x

    if n == 1:
        return math.sin(x) / (x * x) - math.cos(x) / x

    j_prev = math.sin(x) / x
    j_curr = math.sin(x) / (x * x) - math.cos(x) / x

    for k in range(2, n + 1):
        j_next = (2 * k - 1) / x * j_curr - j_prev
        j_prev, j_curr = j_curr, j_next

    return j_curr


def spherical_bessel_y(n: int, x: float) -> float:
    """Computes the spherical Bessel function of the second kind y_n(x).

    y_n(x) = sqrt(pi/(2x)) Y_{n+1/2}(x).

    Args:
        n: Order (>= 0).
        x: Evaluation point (> 0).

    Returns:
        Value of y_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0 or x <= 0.

    Example:
        >>> round(spherical_bessel_y(0, 1.0), 6)
        -0.540302

    Complexity: O(n) via forward recurrence.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("n must be >= 0.")

    if x <= 0:
        raise ValueError("x must be > 0.")

    # y_0(x) = -cos(x)/x, y_1(x) = -cos(x)/x^2 - sin(x)/x
    if n == 0:
        return -math.cos(x) / x

    if n == 1:
        return -math.cos(x) / (x * x) - math.sin(x) / x

    y_prev = -math.cos(x) / x
    y_curr = -math.cos(x) / (x * x) - math.sin(x) / x

    for k in range(2, n + 1):
        y_next = (2 * k - 1) / x * y_curr - y_prev
        y_prev, y_curr = y_curr, y_next

    return y_curr


# ---------------------------------------------------------------------------
# Confluent hypergeometric (Kummer) function
# ---------------------------------------------------------------------------


def hypergeometric_1f1(a: float, b: float, z: float) -> float:
    """Computes the confluent hypergeometric function 1F1(a; b; z) (Kummer's M).

    M(a, b, z) = sum_{n=0}^{inf} (a)_n z^n / ((b)_n n!).

    Args:
        a: Numerator parameter.
        b: Denominator parameter (must not be 0 or a negative integer).
        z: Argument.

    Returns:
        Value of M(a, b, z).

    Raises:
        TypeError: If parameters are not numeric.
        ValueError: If b is 0 or a negative integer.

    Example:
        >>> round(hypergeometric_1f1(1, 1, 1), 6)
        2.718282

    Complexity: O(max_terms)
    """
    if not all(isinstance(v, (int, float)) for v in (a, b, z)):
        raise TypeError("All parameters must be numeric.")

    if b == 0 or (b < 0 and b == int(b)):
        raise ValueError("b must not be 0 or a negative integer.")

    max_terms = 500
    tolerance = 1e-15
    total = 1.0
    term = 1.0

    for n in range(1, max_terms):
        term *= (a + n - 1) / ((b + n - 1) * n) * z
        total += term

        if abs(term) < tolerance:
            break

    return total


# ---------------------------------------------------------------------------
# Spherical harmonics (real form, magnitude only)
# ---------------------------------------------------------------------------


def spherical_harmonic_real(l: int, m: int, theta: float, phi: float) -> float:  # noqa: E741 — standard physics notation
    """Computes the real spherical harmonic Y_l^m(theta, phi).

    Args:
        l: Degree (>= 0).
        m: Order (-l <= m <= l).
        theta: Polar angle in [0, pi].
        phi: Azimuthal angle in [0, 2*pi].

    Returns:
        Real-valued spherical harmonic.

    Raises:
        TypeError: If l or m are not integers or angles are not numeric.
        ValueError: If l < 0 or |m| > l.

    Example:
        >>> round(spherical_harmonic_real(0, 0, 0, 0), 6)
        0.282095

    Complexity: O(l)
    """
    if not isinstance(l, int) or not isinstance(m, int):
        raise TypeError("l and m must be integers.")

    if not isinstance(theta, (int, float)) or not isinstance(phi, (int, float)):
        raise TypeError("theta and phi must be numeric.")

    if l < 0:
        raise ValueError("l must be >= 0.")

    if abs(m) > l:
        raise ValueError("|m| must be <= l.")

    abs_m = abs(m)

    # Normalization factor
    norm = math.sqrt(
        (2 * l + 1) / (4 * math.pi)
        * math.factorial(l - abs_m) / math.factorial(l + abs_m)
    )

    plm = associated_legendre(l, abs_m, math.cos(theta))

    if m > 0:
        return norm * math.sqrt(2) * plm * math.cos(m * phi)
    elif m < 0:
        return norm * math.sqrt(2) * plm * math.sin(abs_m * phi)
    else:
        return norm * plm


# ---------------------------------------------------------------------------
# Bessel functions (cylindrical)
# ---------------------------------------------------------------------------


def bessel_j(n: int, x: float, terms: int = 80) -> float:
    """Computes the Bessel function of the first kind J_n(x) via power series.

    Args:
        n: Order of the Bessel function (>= 0).
        x: Evaluation point.
        terms: Number of series terms (default 80).

    Returns:
        Value of J_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> round(bessel_j(0, 0), 6)
        1.0
        >>> round(bessel_j(1, 0), 6)
        0.0

    Complexity: O(terms)
    """
    if not isinstance(n, int):
        raise TypeError("Order n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("Order n must be >= 0.")

    total = 0.0

    for k in range(terms):
        sign = (-1) ** k
        num = (x / 2.0) ** (2 * k + n)
        denom = math.factorial(k) * math.factorial(k + n)
        term = sign * num / denom
        total += term

        if abs(term) < 1e-16:
            break

    return total


def bessel_y(n: int, x: float, terms: int = 80) -> float:
    """Computes the Bessel function of the second kind Y_n(x) (Neumann function).

    Uses the relation Y_n(x) = (J_n(x) cos(nπ) - J_{-n}(x)) / sin(nπ)
    for non-integer-like computation, with direct series for integer n.

    For integer n, uses the limiting form via numerical differentiation.

    Args:
        n: Order of the Bessel function (>= 0).
        x: Evaluation point (x > 0).
        terms: Number of series terms (default 80).

    Returns:
        Value of Y_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0 or x <= 0.

    Example:
        >>> round(bessel_y(0, 1.0), 4)
        0.0883

    Complexity: O(terms * n)
    """
    if not isinstance(n, int):
        raise TypeError("Order n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("Order n must be >= 0.")

    if x <= 0:
        raise ValueError("x must be > 0 for Y_n.")

    # Compute via finite difference on Bessel J w.r.t. order
    eps = 1e-6
    nu_plus = n + eps
    nu_minus = n - eps

    # J_nu for non-integer nu
    def _bessel_j_real(nu: float, xv: float) -> float:
        total = 0.0

        for k in range(terms):
            sign = (-1) ** k
            num = (xv / 2.0) ** (2 * k + nu)
            denom = math.factorial(k) * math.gamma(k + nu + 1)
            t = sign * num / denom
            total += t

            if abs(t) < 1e-16:
                break

        return total

    j_plus = _bessel_j_real(nu_plus, x)
    j_minus = _bessel_j_real(nu_minus, x)

    return (j_plus * math.cos(nu_plus * math.pi) - j_minus) / math.sin(nu_plus * math.pi)


def modified_bessel_i(n: int, x: float, terms: int = 80) -> float:
    """Computes the modified Bessel function of the first kind I_n(x).

    I_n(x) = Σ (x/2)^(2k+n) / (k! * (k+n)!)

    Args:
        n: Order (>= 0).
        x: Evaluation point.
        terms: Number of series terms (default 80).

    Returns:
        Value of I_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0.

    Example:
        >>> round(modified_bessel_i(0, 0), 6)
        1.0

    Complexity: O(terms)
    """
    if not isinstance(n, int):
        raise TypeError("Order n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("Order n must be >= 0.")

    total = 0.0

    for k in range(terms):
        num = (x / 2.0) ** (2 * k + n)
        denom = math.factorial(k) * math.factorial(k + n)
        term = num / denom
        total += term

        if abs(term) < 1e-16:
            break

    return total


def modified_bessel_k(n: int, x: float) -> float:
    """Computes the modified Bessel function of the second kind K_n(x).

    Uses K_n(x) = (π/2) * (I_{-n}(x) - I_n(x)) / sin(nπ) via limiting form.
    For integer n, uses numerical differentiation w.r.t. order.

    Args:
        n: Order (>= 0).
        x: Evaluation point (x > 0).

    Returns:
        Value of K_n(x).

    Raises:
        TypeError: If n is not an integer or x is not numeric.
        ValueError: If n < 0 or x <= 0.

    Example:
        >>> round(modified_bessel_k(0, 1.0), 4)
        0.4210

    Complexity: O(terms)
    """
    if not isinstance(n, int):
        raise TypeError("Order n must be an integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n < 0:
        raise ValueError("Order n must be >= 0.")

    if x <= 0:
        raise ValueError("x must be > 0 for K_n.")

    eps = 1e-6

    def _bessel_i_real(nu: float, xv: float, terms: int = 80) -> float:
        total = 0.0

        for k in range(terms):
            num = (xv / 2.0) ** (2 * k + nu)
            denom = math.factorial(k) * math.gamma(k + nu + 1)
            term = num / denom
            total += term

            if abs(term) < 1e-16:
                break

        return total

    nu = n + eps
    i_minus = _bessel_i_real(-nu, x)
    i_plus = _bessel_i_real(nu, x)

    return (math.pi / 2.0) * (i_minus - i_plus) / math.sin(nu * math.pi)


# ---------------------------------------------------------------------------
# Special integrals (exponential, sine, cosine, Fresnel)
# ---------------------------------------------------------------------------


def exponential_integral_ei(x: float, terms: int = 200) -> float:
    """Computes the exponential integral Ei(x) for x > 0.

    Ei(x) = γ + ln(x) + Σ x^k / (k * k!) for k = 1, 2, ...

    Args:
        x: Evaluation point (x > 0).
        terms: Number of series terms (default 200).

    Returns:
        Value of Ei(x).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x <= 0.

    Example:
        >>> round(exponential_integral_ei(1.0), 4)
        1.8951

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if x <= 0:
        raise ValueError("x must be > 0 for Ei.")

    euler_gamma = 0.5772156649015329
    total = euler_gamma + math.log(x)
    term = 0.0

    for k in range(1, terms + 1):
        term = x ** k / (k * math.factorial(k))
        total += term

        if abs(term) < 1e-16:
            break

    return total


def sine_integral(x: float, terms: int = 200) -> float:
    """Computes the sine integral Si(x) = ∫₀ˣ sin(t)/t dt.

    Uses the Taylor series: Si(x) = Σ (-1)^k x^(2k+1) / ((2k+1)(2k+1)!).

    Args:
        x: Evaluation point.
        terms: Number of series terms (default 200).

    Returns:
        Value of Si(x).

    Example:
        >>> round(sine_integral(1.0), 6)
        0.946083

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    total = 0.0

    for k in range(terms):
        n = 2 * k + 1
        term = ((-1) ** k) * x ** n / (n * math.factorial(n))
        total += term

        if abs(term) < 1e-16:
            break

    return total


def cosine_integral(x: float, terms: int = 200) -> float:
    """Computes the cosine integral Ci(x) = γ + ln(x) + ∫₀ˣ (cos(t)-1)/t dt.

    Uses the series: Ci(x) = γ + ln(x) + Σ (-1)^k x^(2k) / ((2k)(2k)!).

    Args:
        x: Evaluation point (x > 0).
        terms: Number of series terms (default 200).

    Returns:
        Value of Ci(x).

    Raises:
        ValueError: If x <= 0.

    Example:
        >>> round(cosine_integral(1.0), 6)
        0.337404

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if x <= 0:
        raise ValueError("x must be > 0 for Ci.")

    euler_gamma = 0.5772156649015329
    total = euler_gamma + math.log(x)

    for k in range(1, terms + 1):
        n = 2 * k
        term = ((-1) ** k) * x ** n / (n * math.factorial(n))
        total += term

        if abs(term) < 1e-16:
            break

    return total


def fresnel_s(x: float, terms: int = 100) -> float:
    """Computes the Fresnel sine integral S(x) = ∫₀ˣ sin(π t²/2) dt.

    Uses the Taylor series expansion.

    Args:
        x: Evaluation point.
        terms: Number of series terms (default 100).

    Returns:
        Value of S(x).

    Example:
        >>> round(fresnel_s(1.0), 6)
        0.438259

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    total = 0.0
    half_pi = math.pi / 2.0

    for k in range(terms):
        n = 2 * k + 1
        exponent = 4 * k + 3
        term = ((-1) ** k * half_pi ** n * x ** exponent) / (
            math.factorial(n) * exponent
        )
        total += term

        if abs(term) < 1e-16:
            break

    return total


def fresnel_c(x: float, terms: int = 100) -> float:
    """Computes the Fresnel cosine integral C(x) = ∫₀ˣ cos(π t²/2) dt.

    Uses the Taylor series expansion.

    Args:
        x: Evaluation point.
        terms: Number of series terms (default 100).

    Returns:
        Value of C(x).

    Example:
        >>> round(fresnel_c(1.0), 6)
        0.779893

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    total = 0.0
    half_pi = math.pi / 2.0

    for k in range(terms):
        n = 2 * k
        exponent = 4 * k + 1
        term = ((-1) ** k * half_pi ** n * x ** exponent) / (
            math.factorial(n) * exponent
        )
        total += term

        if abs(term) < 1e-16:
            break

    return total


def dawson_function(x: float, terms: int = 100) -> float:
    """Computes Dawson's function D(x) = e^(-x^2) ∫₀ˣ e^(t^2) dt.

    Uses the series: D(x) = x - 2x^3/3 + 4x^5/15 - ...

    Args:
        x: Evaluation point.
        terms: Number of series terms (default 100).

    Returns:
        Value of D(x).

    Example:
        >>> round(dawson_function(1.0), 6)
        0.538080

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    total = 0.0

    for k in range(terms):
        term = ((-1) ** k * 2 ** k * x ** (2 * k + 1)) / (
            1 * 3  # product of odd numbers 1*3*5*..*(2k+1)
        )
        # Use the proper formula: D(x) = Σ (-2)^k x^(2k+1) / (1·3·5···(2k+1))
        denom = 1.0

        for j in range(1, 2 * k + 2):

            if j % 2 == 1:
                denom *= j

        term = ((-2) ** k * x ** (2 * k + 1)) / denom
        total += term

        if abs(term) < 1e-16 and k > 0:
            break

    return total


def polylogarithm(s: float, z: float, terms: int = 500) -> float:
    """Computes the polylogarithm Li_s(z) = Σ z^k / k^s for |z| <= 1.

    Args:
        s: Order of the polylogarithm.
        z: Argument (|z| <= 1 for convergence).
        terms: Number of series terms (default 500).

    Returns:
        Value of Li_s(z).

    Raises:
        ValueError: If |z| > 1.

    Example:
        >>> round(polylogarithm(2, 0.5), 6)
        0.582241

    Complexity: O(terms)
    """
    if not isinstance(s, (int, float)):
        raise TypeError("s must be numeric.")

    if not isinstance(z, (int, float)):
        raise TypeError("z must be numeric.")

    if abs(z) > 1.0 + 1e-10:
        raise ValueError("|z| must be <= 1 for Li_s(z) convergence.")

    total = 0.0

    for k in range(1, terms + 1):
        term = z ** k / k ** s
        total += term

        if abs(term) < 1e-16:
            break

    return total


def dilogarithm(z: float) -> float:
    """Computes the dilogarithm (Spence's function) Li_2(z) for z <= 1.

    Li_2(z) = -∫₀ᶻ ln(1-t)/t dt = Σ z^k / k^2.

    Args:
        z: Argument (z <= 1).

    Returns:
        Value of Li_2(z).

    Example:
        >>> round(dilogarithm(1.0), 6)  # pi^2/6
        1.644934

    Complexity: O(terms)
    """
    return polylogarithm(2, z)


def upper_incomplete_gamma(a: float, x: float, terms: int = 200) -> float:
    """Computes the upper incomplete gamma function Γ(a, x) = ∫ₓ^∞ t^(a-1) e^(-t) dt.

    Γ(a, x) = Γ(a) - γ(a, x) where γ is the lower incomplete gamma.

    Args:
        a: Shape parameter (a > 0).
        x: Lower limit (x >= 0).
        terms: Number of series terms (default 200).

    Returns:
        Value of Γ(a, x).

    Example:
        >>> round(upper_incomplete_gamma(1, 1), 6)  # e^(-1)
        0.367879

    Complexity: O(terms)
    """
    if not isinstance(a, (int, float)) or not isinstance(x, (int, float)):
        raise TypeError("a and x must be numeric.")

    if a <= 0:
        raise ValueError("a must be > 0.")

    if x < 0:
        raise ValueError("x must be >= 0.")

    # γ(a, x) = Σ (-1)^k x^(a+k) / (k! (a+k))
    lower = 0.0

    for k in range(terms):
        term = ((-1) ** k * x ** (a + k)) / (math.factorial(k) * (a + k))
        lower += term

        if k > 0 and abs(term) < 1e-16:
            break

    return math.gamma(a) - lower


def hurwitz_zeta(s: float, a: float, terms: int = 100000) -> float:
    """Computes the Hurwitz zeta function ζ(s, a) = Σ 1/(n+a)^s for n=0,1,2,...

    Args:
        s: Exponent (s > 1 for convergence).
        a: Shift parameter (a > 0).
        terms: Number of series terms (default 100000).

    Returns:
        Value of ζ(s, a).

    Raises:
        ValueError: If s <= 1 or a <= 0.

    Example:
        >>> round(hurwitz_zeta(2, 1), 4)  # ζ(2,1) = π²/6
        1.6449

    Complexity: O(terms)
    """
    if not isinstance(s, (int, float)) or not isinstance(a, (int, float)):
        raise TypeError("s and a must be numeric.")

    if s <= 1:
        raise ValueError("s must be > 1.")

    if a <= 0:
        raise ValueError("a must be > 0.")

    total = 0.0

    for n in range(terms):
        term = 1.0 / (n + a) ** s
        total += term

        if term < 1e-15:
            break

    return total


# ---------------------------------------------------------------------------
# Combinatorial special values
# ---------------------------------------------------------------------------


def rising_factorial(x: float, n: int) -> float:
    """Computes the rising factorial (Pochhammer symbol) x^(n) = x(x+1)(x+2)...(x+n-1).

    Args:
        x: Base value.
        n: Number of factors (>= 0).

    Returns:
        Value of (x)_n.

    Example:
        >>> rising_factorial(3, 4)  # 3*4*5*6
        360.0
        >>> rising_factorial(1, 5)  # 5!
        120.0

    Complexity: O(n)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(n, int) or n < 0:
        raise TypeError("n must be a non-negative integer.")

    result = 1.0

    for i in range(n):
        result *= (x + i)

    return result


def falling_factorial(x: float, n: int) -> float:
    """Computes the falling factorial x_(n) = x(x-1)(x-2)...(x-n+1).

    Args:
        x: Base value.
        n: Number of factors (>= 0).

    Returns:
        Value of x_(n).

    Example:
        >>> falling_factorial(5, 3)  # 5*4*3
        60.0
        >>> falling_factorial(5, 5)  # 5!
        120.0

    Complexity: O(n)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(n, int) or n < 0:
        raise TypeError("n must be a non-negative integer.")

    result = 1.0

    for i in range(n):
        result *= (x - i)

    return result


def subfactorial(n: int) -> int:
    """Computes the subfactorial !n (number of derangements of n elements).

    !n = n! Σ (-1)^k / k! for k = 0 to n.

    Args:
        n: Non-negative integer.

    Returns:
        Number of derangements.

    Example:
        >>> subfactorial(0)
        1
        >>> subfactorial(3)
        2
        >>> subfactorial(5)
        44

    Complexity: O(n)
    """
    if not isinstance(n, int) or n < 0:
        raise TypeError("n must be a non-negative integer.")

    if n == 0:
        return 1

    if n == 1:
        return 0

    d_prev2 = 1  # !0
    d_prev1 = 0  # !1

    for i in range(2, n + 1):
        d = (i - 1) * (d_prev1 + d_prev2)
        d_prev2 = d_prev1
        d_prev1 = d

    return d_prev1


def stirling_number_first(n: int, k: int) -> int:
    """Computes the unsigned Stirling number of the first kind |s(n, k)|.

    Counts the number of permutations of n elements with exactly k cycles.

    Args:
        n: Total elements (>= 0).
        k: Number of cycles (>= 0).

    Returns:
        Unsigned Stirling number |s(n, k)|.

    Raises:
        TypeError: If n or k are not non-negative integers.
        ValueError: If k > n.

    Example:
        >>> stirling_number_first(4, 2)
        11
        >>> stirling_number_first(3, 1)
        2

    Complexity: O(n * k)
    """
    if not isinstance(n, int) or n < 0:
        raise TypeError("n must be a non-negative integer.")

    if not isinstance(k, int) or k < 0:
        raise TypeError("k must be a non-negative integer.")

    if k > n:
        return 0

    if n == 0 and k == 0:
        return 1

    if k == 0:
        return 0

    # DP table
    s = [[0] * (k + 1) for _ in range(n + 1)]
    s[0][0] = 1

    for i in range(1, n + 1):

        for j in range(1, min(i, k) + 1):
            s[i][j] = (i - 1) * s[i - 1][j] + s[i - 1][j - 1]

    return s[n][k]


def multinomial_coefficient(n: int, *groups: int) -> int:
    """Computes the multinomial coefficient n! / (k1! * k2! * ... * km!).

    Args:
        n: Total number of items.
        *groups: Sizes of each group (must sum to n).

    Returns:
        Multinomial coefficient.

    Raises:
        ValueError: If groups don't sum to n.

    Example:
        >>> multinomial_coefficient(6, 2, 2, 2)
        90
        >>> multinomial_coefficient(4, 2, 1, 1)
        12

    Complexity: O(n)
    """
    if not isinstance(n, int) or n < 0:
        raise TypeError("n must be a non-negative integer.")

    if sum(groups) != n:
        raise ValueError("Groups must sum to n.")

    result = math.factorial(n)

    for g in groups:

        if not isinstance(g, int) or g < 0:
            raise TypeError("Each group size must be a non-negative integer.")

        result //= math.factorial(g)

    return result


# ---------------------------------------------------------------------------
# Stirling, Wallis, Gaussian and Dirichlet integrals
# ---------------------------------------------------------------------------


def stirling_approximation(n: int) -> float:
    """Computes Stirling's approximation for n!: sqrt(2πn) * (n/e)^n.

    Args:
        n: Non-negative integer.

    Returns:
        Approximation of n!.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> round(stirling_approximation(10), 0)
        3598695.0

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 1.0

    return math.sqrt(2.0 * math.pi * n) * (n / math.e) ** n


def wallis_product(n: int) -> float:
    """Computes the Wallis product approximation for pi/2 using n terms.

    pi/2 = product_{k=1}^{n} (4k^2) / (4k^2 - 1).

    Args:
        n: Number of terms (positive integer).

    Returns:
        Approximation of pi/2.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Example:
        >>> round(wallis_product(10000), 4)
        1.5707

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be at least 1.")

    result = 1.0

    for k in range(1, n + 1):
        four_k2 = 4.0 * k * k
        result *= four_k2 / (four_k2 - 1.0)

    return result


def gaussian_integral() -> float:
    """Returns the exact value of the Gaussian integral: integral_{-inf}^{inf} e^{-x^2} dx = sqrt(pi).

    Returns:
        sqrt(pi).

    Example:
        >>> round(gaussian_integral(), 6)
        1.772454

    Complexity: O(1)
    """
    return math.sqrt(math.pi)


def dirichlet_integral() -> float:
    """Returns the exact value of the Dirichlet integral: integral_{0}^{inf} sin(x)/x dx = pi/2.

    Returns:
        pi/2.

    Example:
        >>> round(dirichlet_integral(), 6)
        1.570796

    Complexity: O(1)
    """
    return math.pi / 2.0


def lanczos_gamma(z: float) -> float:
    """Computes the Gamma function using the Lanczos approximation.

    Complements ``math.gamma`` with higher precision for edge cases.

    Args:
        z: Real argument (z > 0 or non-integer negative).

    Returns:
        Gamma(z).

    Raises:
        TypeError: If z is not numeric.
        ValueError: If z is a non-positive integer.

    Example:
        >>> round(lanczos_gamma(5.5), 6)
        52.342778

    Complexity: O(1)
    """
    if not isinstance(z, (int, float)):
        raise TypeError("z must be numeric.")

    if z <= 0 and z == int(z):
        raise ValueError("Gamma undefined for non-positive integers.")

    # Reflection formula for z < 0.5
    if z < 0.5:
        return math.pi / (math.sin(math.pi * z) * lanczos_gamma(1.0 - z))

    z -= 1.0
    g = 7
    coeff = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7,
    ]

    x = coeff[0]

    for i in range(1, g + 2):
        x += coeff[i] / (z + i)

    t = z + g + 0.5
    return math.sqrt(2.0 * math.pi) * t ** (z + 0.5) * math.exp(-t) * x


def digamma(x: float) -> float:
    """Computes the digamma (psi) function: derivative of ln(Gamma(x)).

    Uses the asymptotic expansion with recurrence for small x.

    Args:
        x: Real positive argument.

    Returns:
        psi(x).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x <= 0.

    Example:
        >>> round(digamma(1), 6)
        -0.577216

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if x <= 0:
        raise ValueError("x must be positive.")

    result = 0.0

    # Shift x to large range
    while x < 6.0:
        result -= 1.0 / x
        x += 1.0

    # Asymptotic expansion
    result += math.log(x) - 1.0 / (2.0 * x)
    x2 = x * x
    result -= 1.0 / (12.0 * x2)
    result += 1.0 / (120.0 * x2 * x2)
    result -= 1.0 / (252.0 * x2 * x2 * x2)

    return result


# ---------------------------------------------------------------------------
# Jacobi theta, Weierstrass, Dedekind eta (Spiegel Ch. Elliptic & Special)
# ---------------------------------------------------------------------------


def jacobi_theta_3(z: float, q: float, terms: int = 50) -> float:
    """Computes the Jacobi theta function θ₃(z, q).

    θ₃(z, q) = 1 + 2 Σ_{n=1}^{terms} q^(n²) cos(2nz).

    Args:
        z: Argument (real).
        q: Nome parameter (|q| < 1).
        terms: Number of series terms.

    Returns:
        θ₃(z, q).

    Raises:
        TypeError: If z or q are not numeric.
        ValueError: If |q| >= 1.

    Example:
        >>> round(jacobi_theta_3(0, 0.1), 6)
        1.200020

    Complexity: O(terms)
    """
    if not isinstance(z, (int, float)) or not isinstance(q, (int, float)):
        raise TypeError("z and q must be numeric.")

    if abs(q) >= 1:
        raise ValueError("|q| must be < 1.")

    result = 1.0

    for n in range(1, terms + 1):
        result += 2.0 * q ** (n * n) * math.cos(2.0 * n * z)

    return result


def jacobi_theta_1(z: float, q: float, terms: int = 50) -> float:
    """Computes the Jacobi theta function θ₁(z, q).

    θ₁(z, q) = 2 Σ_{n=0}^{terms} (-1)^n q^((n+1/2)²) sin((2n+1)z).

    Args:
        z: Argument (real).
        q: Nome parameter (|q| < 1).
        terms: Number of series terms.

    Returns:
        θ₁(z, q).

    Raises:
        TypeError: If z or q are not numeric.
        ValueError: If |q| >= 1.

    Example:
        >>> round(jacobi_theta_1(0.5, 0.1), 6)
        0.091557

    Complexity: O(terms)
    """
    if not isinstance(z, (int, float)) or not isinstance(q, (int, float)):
        raise TypeError("z and q must be numeric.")

    if abs(q) >= 1:
        raise ValueError("|q| must be < 1.")

    result = 0.0

    for n in range(terms + 1):
        exp = (n + 0.5) ** 2
        result += ((-1) ** n) * q ** exp * math.sin((2 * n + 1) * z)

    return 2.0 * result


def jacobi_theta_2(z: float, q: float, terms: int = 50) -> float:
    """Computes the Jacobi theta function θ₂(z, q).

    θ₂(z, q) = 2 Σ_{n=0}^{terms} q^((n+1/2)²) cos((2n+1)z).

    Args:
        z: Argument (real).
        q: Nome parameter (|q| < 1).
        terms: Number of series terms.

    Returns:
        θ₂(z, q).

    Example:
        >>> round(jacobi_theta_2(0, 0.1), 6)
        0.200010

    Complexity: O(terms)
    """
    if not isinstance(z, (int, float)) or not isinstance(q, (int, float)):
        raise TypeError("z and q must be numeric.")

    if abs(q) >= 1:
        raise ValueError("|q| must be < 1.")

    result = 0.0

    for n in range(terms + 1):
        exp = (n + 0.5) ** 2
        result += q ** exp * math.cos((2 * n + 1) * z)

    return 2.0 * result


def jacobi_theta_4(z: float, q: float, terms: int = 50) -> float:
    """Computes the Jacobi theta function θ₄(z, q).

    θ₄(z, q) = 1 + 2 Σ_{n=1}^{terms} (-1)^n q^(n²) cos(2nz).

    Args:
        z: Argument (real).
        q: Nome parameter (|q| < 1).
        terms: Number of series terms.

    Returns:
        θ₄(z, q).

    Example:
        >>> round(jacobi_theta_4(0, 0.1), 6)
        0.799980

    Complexity: O(terms)
    """
    if not isinstance(z, (int, float)) or not isinstance(q, (int, float)):
        raise TypeError("z and q must be numeric.")

    if abs(q) >= 1:
        raise ValueError("|q| must be < 1.")

    result = 1.0

    for n in range(1, terms + 1):
        result += 2.0 * ((-1) ** n) * q ** (n * n) * math.cos(2.0 * n * z)

    return result


def dedekind_eta(tau_im: float, terms: int = 100) -> float:
    """Computes the Dedekind eta function η(τ) for purely imaginary τ = i·τ_im.

    η(τ) = exp(πiτ/12) Π_{n=1}^{∞} (1 - exp(2πinτ)).

    For pure imaginary τ with positive imaginary part, the result is real.

    Args:
        tau_im: Imaginary part of τ (> 0).
        terms: Number of product terms.

    Returns:
        η(i·tau_im).

    Raises:
        ValueError: If tau_im <= 0.

    Example:
        >>> round(dedekind_eta(1), 6)
        0.768225

    Complexity: O(terms)
    """
    if not isinstance(tau_im, (int, float)):
        raise TypeError("tau_im must be numeric.")

    if tau_im <= 0:
        raise ValueError("tau_im must be positive.")

    # exp(pi*i*i*tau_im/12) = exp(-pi*tau_im/12) (since i*i = -1)
    result = math.exp(-math.pi * tau_im / 12.0)

    for n in range(1, terms + 1):
        # exp(2*pi*i*n*i*tau_im) = exp(-2*pi*n*tau_im)
        q_factor = math.exp(-2.0 * math.pi * n * tau_im)
        result *= (1.0 - q_factor)

    return result


def weierstrass_p(
    z: float, omega1: float = 1.0, omega3_im: float = 1.0, terms: int = 10
) -> float:
    """Computes the Weierstrass ℘-function for real z with rectangular lattice.

    Uses the lattice with periods 2ω₁ (real) and 2iω₃ (pure imaginary).
    ℘(z) = 1/z² + Σ'_{(m,n)} [1/(z - 2mω₁ - 2niω₃)² - 1/(2mω₁ + 2niω₃)²].

    Args:
        z: Real argument (not a lattice point).
        omega1: Real half-period (> 0).
        omega3_im: Imaginary half-period (> 0).
        terms: Number of lattice shells to sum.

    Returns:
        ℘(z) (approximately real for real z on rectangular lattice).

    Raises:
        ValueError: If z is too close to a lattice point.

    Example:
        >>> round(weierstrass_p(0.5, 1.0, 1.0, 10), 4)  # doctest: +SKIP
        4.0304

    Complexity: O(terms^2)
    """
    if not isinstance(z, (int, float)):
        raise TypeError("z must be numeric.")

    if not isinstance(omega1, (int, float)) or omega1 <= 0:
        raise ValueError("omega1 must be positive.")

    if not isinstance(omega3_im, (int, float)) or omega3_im <= 0:
        raise ValueError("omega3_im must be positive.")

    result = 1.0 / (z * z) if abs(z) > 1e-15 else 0.0

    if abs(z) < 1e-15:
        raise ValueError("z must not be a lattice point.")

    for m in range(-terms, terms + 1):

        for n in range(-terms, terms + 1):

            if m == 0 and n == 0:
                continue

            # Lattice point: 2m*omega1 + 2n*i*omega3
            # For real z, the contribution involves complex arithmetic
            w_re = 2.0 * m * omega1
            w_im = 2.0 * n * omega3_im

            # 1/(z - w)^2 where w = w_re + i*w_im
            d_re = z - w_re
            d_im = -w_im
            d2 = d_re * d_re + d_im * d_im

            if d2 < 1e-15:
                raise ValueError("z is too close to a lattice point.")

            inv_re = (d_re * d_re - d_im * d_im) / (d2 * d2)

            # 1/w^2
            w2 = w_re * w_re + w_im * w_im
            inv_w_re = (w_re * w_re - w_im * w_im) / (w2 * w2)

            result += inv_re - inv_w_re

    return result


def trigamma(x: float) -> float:
    """Computes the trigamma function ψ₁(x) = d²/dx² ln(Γ(x)).

    Uses the recurrence ψ₁(x) = ψ₁(x+1) + 1/x² and asymptotic expansion.

    Args:
        x: Real positive argument.

    Returns:
        ψ₁(x).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x <= 0.

    Example:
        >>> round(trigamma(1), 6)
        1.644934

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if x <= 0:
        raise ValueError("x must be positive.")

    result = 0.0

    while x < 6.0:
        result += 1.0 / (x * x)
        x += 1.0

    # Asymptotic expansion
    x2 = x * x
    result += 1.0 / x + 1.0 / (2.0 * x2) + 1.0 / (6.0 * x2 * x)
    result -= 1.0 / (30.0 * x2 * x2 * x)
    result += 1.0 / (42.0 * x2 * x2 * x2 * x)

    return result


def polygamma(m: int, x: float) -> float:
    """Computes the polygamma function ψ^(m)(x) numerically.

    For m=0 returns digamma, m=1 returns trigamma, etc.
    Uses finite differences of digamma for m >= 2.

    Args:
        m: Order (non-negative integer).
        x: Real positive argument.

    Returns:
        ψ^(m)(x).

    Raises:
        TypeError: If m is not int or x not numeric.
        ValueError: If m < 0 or x <= 0.

    Example:
        >>> round(polygamma(0, 1), 6)
        -0.577216

    Complexity: O(m) finite differences.
    """
    if not isinstance(m, int) or isinstance(m, bool):
        raise TypeError("m must be an integer.")

    if m < 0:
        raise ValueError("m must be non-negative.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if x <= 0:
        raise ValueError("x must be positive.")

    if m == 0:
        return digamma(x)

    if m == 1:
        return trigamma(x)

    # Numerical finite differences of digamma for higher orders
    h = 0.001
    result = 0.0
    sign = 1

    for k in range(m + 1):
        binom = math.comb(m, k)
        val = digamma(x + (m - k) * h)
        result += sign * binom * val
        sign *= -1

    return result / (h ** m)


# ---------------------------------------------------------------------------
# Additional orthogonal polynomials (Spiegel)
# ---------------------------------------------------------------------------


def gegenbauer_polynomial(n: int, alpha: float, x: float) -> float:
    """Gegenbauer (ultraspherical) polynomial C_n^α(x) via recurrence.

    C_0^α(x) = 1, C_1^α(x) = 2αx,
    k·C_k^α(x) = 2(k+α-1)x·C_{k-1}^α(x) - (k+2α-2)·C_{k-2}^α(x).

    Args:
        n: Degree (non-negative integer).
        alpha: Parameter α > -1/2, α ≠ 0.
        x: Evaluation point.

    Returns:
        Value of C_n^α(x).

    Example:
        >>> round(gegenbauer_polynomial(2, 1.0, 0.5), 6)
        -0.5

    Complexity: O(n)
    """

    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    if not isinstance(alpha, (int, float)):
        raise TypeError("alpha must be numeric.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n == 0:
        return 1.0

    if n == 1:
        return 2.0 * alpha * x

    c_prev2 = 1.0
    c_prev1 = 2.0 * alpha * x

    for k in range(2, n + 1):
        c_curr = (2.0 * (k + alpha - 1) * x * c_prev1 - (k + 2 * alpha - 2) * c_prev2) / k
        c_prev2 = c_prev1
        c_prev1 = c_curr

    return c_prev1


def jacobi_polynomial(n: int, alpha: float, beta: float, x: float) -> float:
    """Jacobi polynomial P_n^(α,β)(x) via recurrence.

    P_0 = 1, P_1 = (α-β)/2 + (α+β+2)x/2.

    Args:
        n: Degree (non-negative integer).
        alpha: Parameter α > -1.
        beta: Parameter β > -1.
        x: Evaluation point in [-1, 1].

    Returns:
        Value of P_n^(α,β)(x).

    Example:
        >>> round(jacobi_polynomial(2, 0, 0, 0.5), 6)
        -0.125

    Complexity: O(n)
    """

    if not isinstance(n, int) or n < 0:
        raise ValueError("n must be a non-negative integer.")

    if not isinstance(alpha, (int, float)) or not isinstance(beta, (int, float)):
        raise TypeError("alpha and beta must be numeric.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if n == 0:
        return 1.0

    if n == 1:
        return (alpha - beta) / 2.0 + (alpha + beta + 2.0) * x / 2.0

    p_prev2 = 1.0
    p_prev1 = (alpha - beta) / 2.0 + (alpha + beta + 2.0) * x / 2.0

    for k in range(2, n + 1):
        ab = alpha + beta
        a2b2 = alpha * alpha - beta * beta
        c1 = 2.0 * k * (k + ab) * (2.0 * k + ab - 2.0)
        c2 = (2.0 * k + ab - 1.0) * a2b2
        c3 = (2.0 * k + ab - 2.0) * (2.0 * k + ab - 1.0) * (2.0 * k + ab)
        c4 = 2.0 * (k + alpha - 1.0) * (k + beta - 1.0) * (2.0 * k + ab)

        if abs(c1) < 1e-15:
            break

        p_curr = ((c2 + c3 * x) * p_prev1 - c4 * p_prev2) / c1
        p_prev2 = p_prev1
        p_prev1 = p_curr

    return p_prev1


# ---------------------------------------------------------------------------
# Struve function (Spiegel)
# ---------------------------------------------------------------------------


def struve_h(nu: int, x: float, terms: int = 50) -> float:
    """Struve function H_ν(x) for integer ν ≥ 0.

    H_ν(x) = Σ_{k=0}^∞ (-1)^k (x/2)^(2k+ν+1) / (Γ(k+3/2)Γ(k+ν+3/2)).

    Args:
        nu: Order (non-negative integer).
        x: Argument.
        terms: Number of series terms (default 50).

    Returns:
        Value of H_ν(x).

    Example:
        >>> round(struve_h(0, 1.0), 6)
        0.568657

    Complexity: O(terms)
    """

    if not isinstance(nu, int) or nu < 0:
        raise ValueError("nu must be a non-negative integer.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    total = 0.0

    for k in range(terms):
        num = (-1) ** k * (x / 2.0) ** (2 * k + nu + 1)
        denom = math.gamma(k + 1.5) * math.gamma(k + nu + 1.5)
        term = num / denom

        total += term

        if abs(term) < 1e-16:
            break

    return total


# ---------------------------------------------------------------------------
# Kelvin functions (Spiegel)
# ---------------------------------------------------------------------------


def kelvin_ber(x: float, terms: int = 50) -> float:
    """Kelvin function ber(x) = Re[J_0(x√i)].

    ber(x) = Σ_{k=0}^∞ cos(kπ/2) · (x/2)^{2k} / (k!)^2.

    Args:
        x: Argument.
        terms: Series terms (default 50).

    Returns:
        Value of ber(x).

    Example:
        >>> round(kelvin_ber(1.0), 6)
        0.98438

    Complexity: O(terms)
    """

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    total = 0.0

    for k in range(terms):
        cos_val = math.cos(k * math.pi / 2.0)

        if abs(cos_val) < 1e-15:
            continue

        num = (x / 2.0) ** (2 * k)
        denom = math.factorial(k) ** 2
        term = cos_val * num / denom
        total += term

        if k > 0 and abs(term) < 1e-16:
            break

    return total


def kelvin_bei(x: float, terms: int = 50) -> float:
    """Kelvin function bei(x) = Im[J_0(x√i)].

    bei(x) = Σ_{k=0}^∞ sin(kπ/2) · (x/2)^{2k} / (k!)^2.

    Args:
        x: Argument.
        terms: Series terms (default 50).

    Returns:
        Value of bei(x).

    Example:
        >>> round(kelvin_bei(1.0), 6)
        0.249937

    Complexity: O(terms)
    """

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    total = 0.0

    for k in range(terms):
        sin_val = math.sin(k * math.pi / 2.0)

        if abs(sin_val) < 1e-15:
            continue

        num = (x / 2.0) ** (2 * k)
        denom = math.factorial(k) ** 2
        term = sin_val * num / denom
        total += term

        if k > 0 and abs(term) < 1e-16:
            break

    return total


# ---------------------------------------------------------------------------
# Anger function (Spiegel)
# ---------------------------------------------------------------------------


def anger_j(nu: float, x: float, n_points: int = 1000) -> float:
    """Anger function J_ν(x) = (1/π) ∫_0^π cos(νθ - x sinθ) dθ.

    Generalizes the Bessel function to non-integer orders via integral representation.

    Args:
        nu: Order (real).
        x: Argument.
        n_points: Quadrature points (default 1000).

    Returns:
        Value of the Anger function.

    Example:
        >>> round(anger_j(0, 0.0), 6)
        1.0

    Complexity: O(n_points)
    """

    if not isinstance(nu, (int, float)):
        raise TypeError("nu must be numeric.")

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    h = math.pi / n_points
    total = 0.0

    for i in range(n_points + 1):
        theta = i * h
        val = math.cos(nu * theta - x * math.sin(theta))

        if i == 0 or i == n_points:
            total += val
        else:
            total += 2.0 * val

    return total * h / (2.0 * math.pi)


# ---------------------------------------------------------------------------
# Mittag-Leffler function (Spiegel)
# ---------------------------------------------------------------------------


def mittag_leffler(alpha: float, beta: float, z: float, terms: int = 100) -> float:
    """Mittag-Leffler function E_{α,β}(z) = Σ_{k=0}^∞ z^k / Γ(αk+β).

    Generalizes the exponential function. E_{1,1}(z) = e^z.

    Args:
        alpha: Parameter α > 0.
        beta: Parameter β > 0.
        z: Argument.
        terms: Series terms (default 100).

    Returns:
        Value of E_{α,β}(z).

    Example:
        >>> round(mittag_leffler(1.0, 1.0, 1.0), 6)
        2.718282

    Complexity: O(terms)
    """

    if not isinstance(alpha, (int, float)) or alpha <= 0:
        raise ValueError("alpha must be positive.")

    if not isinstance(beta, (int, float)) or beta <= 0:
        raise ValueError("beta must be positive.")

    if not isinstance(z, (int, float)):
        raise TypeError("z must be numeric.")

    total = 0.0

    for k in range(terms):

        try:
            g = math.gamma(alpha * k + beta)
        except (ValueError, OverflowError):
            break

        if g == 0:
            break

        term = z ** k / g
        total += term

        if abs(term) < 1e-16:
            break

    return total


# ---------------------------------------------------------------------------
# Gamma function identities (Spiegel)
# ---------------------------------------------------------------------------


def reciprocal_gamma(x: float) -> float:
    """Reciprocal gamma function 1/Γ(x).

    Well-defined everywhere including non-positive integers where Γ has poles.

    Args:
        x: Argument.

    Returns:
        1/Γ(x), or 0 at non-positive integers.

    Example:
        >>> reciprocal_gamma(1.0)
        1.0
        >>> reciprocal_gamma(0.0)
        0.0

    Complexity: O(1)
    """

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    # At non-positive integers, Gamma has poles → reciprocal is 0
    if x <= 0 and x == int(x):
        return 0.0

    return 1.0 / math.gamma(x)


def euler_reflection_formula(z: float) -> float:
    """Verifies Euler's reflection formula: Γ(z)Γ(1-z) = π/sin(πz).

    Returns Γ(z) computed via the reflection formula (useful when z < 0.5).

    Args:
        z: Argument (z not an integer).

    Returns:
        Γ(z) computed via π / (sin(πz) · Γ(1-z)).

    Raises:
        ValueError: If z is a non-positive integer.

    Example:
        >>> round(euler_reflection_formula(0.5), 6)
        1.772454

    Complexity: O(1)
    """

    if not isinstance(z, (int, float)):
        raise TypeError("z must be numeric.")

    if z <= 0 and z == int(z):
        raise ValueError("z must not be a non-positive integer.")

    sin_pz = math.sin(math.pi * z)

    if abs(sin_pz) < 1e-15:
        raise ValueError("z must not be an integer for the reflection formula.")

    return math.pi / (sin_pz * math.gamma(1.0 - z))


def gamma_duplication_formula(z: float) -> float:
    """Legendre's duplication formula: Γ(z)Γ(z+1/2) = √π · Γ(2z) / 2^(2z-1).

    Returns Γ(z+1/2) computed from this identity.

    Args:
        z: Argument (z > 0).

    Returns:
        Γ(z+1/2) via the duplication formula.

    Raises:
        ValueError: If z <= 0.

    Example:
        >>> round(gamma_duplication_formula(1.0), 6)
        0.886227

    Complexity: O(1)
    """

    if not isinstance(z, (int, float)):
        raise TypeError("z must be numeric.")

    if z <= 0:
        raise ValueError("z must be positive.")

    gamma_z = math.gamma(z)
    gamma_2z = math.gamma(2.0 * z)

    return math.sqrt(math.pi) * gamma_2z / (2.0 ** (2.0 * z - 1.0) * gamma_z)


def bernstein_polynomial(n: int, k: int, t: float) -> float:
    """Evaluate the Bernstein basis polynomial B_{n,k}(t).

    Description:
        B_{n,k}(t) = C(n,k) · t^k · (1−t)^{n−k}.
        Bernstein polynomials form the basis of Bézier curves and
        surfaces in computer graphics and CAD.

    Args:
        n: Degree of the polynomial (>= 0).
        k: Index (0 <= k <= n).
        t: Evaluation point, typically in [0, 1].

    Returns:
        Value of B_{n,k}(t).

    Raises:
        TypeError: If n or k are not integers, or t is not numeric.
        ValueError: If n < 0 or k not in [0, n].

    Example:
        >>> bernstein_polynomial(3, 1, 0.5)
        0.375
        >>> bernstein_polynomial(4, 2, 0.5)
        0.375

    Complexity: O(n) for the binomial coefficient computation.
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers.")

    if not isinstance(t, (int, float)):
        raise TypeError("t must be numeric.")

    if n < 0:
        raise ValueError("n must be >= 0.")

    if k < 0 or k > n:
        raise ValueError("k must be in [0, n].")

    binom = math.comb(n, k)

    return float(binom * t ** k * (1.0 - t) ** (n - k))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 13: Additional Special Functions
# ---------------------------------------------------------------------------

def error_function(x: float) -> float:
    """Compute the error function erf(x) via Maclaurin series.

    erf(x) = (2/√π) Σ_{n=0}^{∞} (-1)^n x^{2n+1} / (n! (2n+1))

    Args:
        x: Input value.

    Returns:
        erf(x) in [-1, 1].

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> round(error_function(1.0), 4)
        0.8427

    Complexity: O(N) where N ≈ 50 terms
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    total = 0.0
    term = x  # first term: x
    for n in range(50):
        if n > 0:
            term *= -x * x / n
        total += term / (2 * n + 1)
    return total * 2.0 / math.sqrt(math.pi)


def complementary_error_function(x: float) -> float:
    """Compute the complementary error function erfc(x) = 1 - erf(x).

    Args:
        x: Input value.

    Returns:
        erfc(x).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> round(complementary_error_function(1.0), 4)
        0.1573

    Complexity: O(N) where N ≈ 50 terms
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    return 1.0 - error_function(x)


def inverse_error_function(p: float) -> float:
    """Compute the inverse error function erfinv(p) via Newton-Raphson.

    Finds x such that erf(x) = p.

    Args:
        p: Value in (-1, 1).

    Returns:
        x such that erf(x) ≈ p.

    Raises:
        TypeError: If p is not numeric.
        ValueError: If p is not in (-1, 1).

    Usage Example:
        >>> round(inverse_error_function(0.8427), 2)
        1.0

    Complexity: O(N) Newton iterations × O(M) series terms
    """
    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")
    p = float(p)
    if p <= -1.0 or p >= 1.0:
        raise ValueError("p must be in (-1, 1).")
    # Initial guess using rational approximation
    a = 0.147
    ln_term = math.log(1.0 - p * p)
    inner = 2.0 / (math.pi * a) + ln_term / 2.0
    x = math.copysign(1.0, p) * math.sqrt(math.sqrt(inner * inner - ln_term / a) - inner)
    # Newton-Raphson refinement
    two_over_sqrt_pi = 2.0 / math.sqrt(math.pi)
    for _ in range(10):
        err = error_function(x) - p
        deriv = two_over_sqrt_pi * math.exp(-x * x)
        if abs(deriv) < 1e-300:
            break
        x -= err / deriv
    return float(x)


def log_gamma(x: float) -> float:
    """Compute the natural logarithm of the Gamma function ln(Γ(x)).

    Uses Lanczos approximation with g=7.

    Args:
        x: Positive real number.

    Returns:
        ln(Γ(x)).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x ≤ 0.

    Usage Example:
        >>> round(log_gamma(5.0), 4)
        3.1781

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if x <= 0:
        raise ValueError("x must be positive.")
    coeffs = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7,
    ]
    g = 7.0
    if x < 0.5:
        return math.log(math.pi / math.sin(math.pi * x)) - log_gamma(1.0 - x)
    x -= 1.0
    a = coeffs[0]
    t = x + g + 0.5
    for i in range(1, len(coeffs)):
        a += coeffs[i] / (x + i)
    return 0.5 * math.log(2.0 * math.pi) + (x + 0.5) * math.log(t) - t + math.log(a)


def catalan_number(n: int) -> int:
    """Compute the n-th Catalan number C_n = (2n)! / ((n+1)! · n!).

    Args:
        n: Non-negative integer.

    Returns:
        The n-th Catalan number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> catalan_number(5)
        42

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return math.comb(2 * n, n) // (n + 1)


def bell_number(n: int) -> int:
    """Compute the n-th Bell number using the Bell triangle.

    B_n counts the number of partitions of a set of n elements.

    Args:
        n: Non-negative integer.

    Returns:
        The n-th Bell number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> bell_number(5)
        52

    Complexity: O(n²)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    if n == 0:
        return 1
    # Bell triangle
    row = [1] + [0] * n
    for i in range(1, n + 1):
        new_row = [row[i - 1]] + [0] * n
        for j in range(1, i + 1):
            new_row[j] = new_row[j - 1] + row[j - 1]
        row = new_row
    return row[0]


def partition_number(n: int) -> int:
    """Compute the partition number p(n) using dynamic programming.

    p(n) counts the number of ways to write n as a sum of positive integers.

    Args:
        n: Non-negative integer.

    Returns:
        The partition number p(n).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> partition_number(10)
        42

    Complexity: O(n²)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    dp = [0] * (n + 1)
    dp[0] = 1
    for k in range(1, n + 1):
        for i in range(k, n + 1):
            dp[i] += dp[i - k]
    return dp[n]


def harmonic_number(n: int) -> float:
    """Compute the n-th harmonic number H_n = Σ_{k=1}^{n} 1/k.

    Args:
        n: Positive integer.

    Returns:
        The n-th harmonic number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> round(harmonic_number(10), 4)
        2.9290

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be at least 1.")
    return float(sum(1.0 / k for k in range(1, n + 1)))


def generalized_harmonic_number(n: int, m: float = 1.0) -> float:
    """Compute the generalized harmonic number H(n, m) = Σ_{k=1}^{n} 1/k^m.

    Args:
        n: Positive integer (upper limit).
        m: Exponent (default 1.0 gives ordinary harmonic number).

    Returns:
        The generalized harmonic number.

    Raises:
        TypeError: If n is not an integer or m is not numeric.
        ValueError: If n < 1.

    Usage Example:
        >>> round(generalized_harmonic_number(10, 2), 4)
        1.5498

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if not isinstance(m, (int, float)):
        raise TypeError("m must be numeric.")
    if n < 1:
        raise ValueError("n must be at least 1.")
    return float(sum(1.0 / k ** m for k in range(1, n + 1)))


def gudermannian(x: float) -> float:
    """Compute the Gudermannian function gd(x) = 2·arctan(tanh(x/2)).

    Relates circular and hyperbolic functions without complex numbers.

    Args:
        x: Input value.

    Returns:
        gd(x) in (-π/2, π/2).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> round(gudermannian(1.0), 4)
        0.8658

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    return float(2.0 * math.atan(math.tanh(float(x) / 2.0)))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 14: More Special Functions
# ---------------------------------------------------------------------------

def inverse_gudermannian(x: float) -> float:
    """Compute the inverse Gudermannian gd⁻¹(x) = ln(tan(π/4 + x/2)).

    Also known as the Mercator function or isometric latitude.

    Args:
        x: Input value in (-π/2, π/2).

    Returns:
        gd⁻¹(x).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If |x| ≥ π/2.

    Usage Example:
        >>> round(inverse_gudermannian(0.8658), 4)
        1.0

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    half_pi = math.pi / 2.0
    if abs(x) >= half_pi:
        raise ValueError("x must be in (-π/2, π/2).")
    return float(math.log(math.tan(math.pi / 4.0 + x / 2.0)))


def sinc_function(x: float) -> float:
    """Compute the unnormalized sinc function sinc(x) = sin(x)/x.

    Returns 1.0 when x = 0 (the limit).

    Args:
        x: Input value.

    Returns:
        sinc(x).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> sinc_function(0)
        1.0

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if x == 0.0:
        return 1.0
    return float(math.sin(x) / x)


def clausen_function(x: float, terms: int = 100) -> float:
    """Compute the Clausen function Cl₂(x) = -∫₀ˣ ln|2 sin(t/2)| dt.

    Uses Fourier series: Cl₂(x) = Σ_{k=1}^{N} sin(kx)/k².

    Args:
        x: Input angle in radians.
        terms: Number of series terms (default 100).

    Returns:
        Cl₂(x).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> round(clausen_function(1.0), 4)
        1.0139

    Complexity: O(terms)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    total = 0.0
    for k in range(1, terms + 1):
        total += math.sin(k * x) / (k * k)
    return float(total)


def debye_function(n: int, x: float, terms: int = 200) -> float:
    """Compute the Debye function D_n(x) = (n/x^n) ∫₀ˣ t^n/(e^t - 1) dt.

    Uses numerical trapezoidal integration.

    Args:
        n: Order (positive integer).
        x: Upper limit (positive real).
        terms: Number of integration steps (default 200).

    Returns:
        D_n(x).

    Raises:
        TypeError: If n is not int or x is not numeric.
        ValueError: If n < 1 or x ≤ 0.

    Usage Example:
        >>> round(debye_function(3, 1.0), 4)
        0.6788

    Complexity: O(terms)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if n < 1:
        raise ValueError("n must be at least 1.")
    if x <= 0:
        raise ValueError("x must be positive.")
    h = x / terms
    total = 0.0
    for i in range(1, terms + 1):
        t = i * h
        if t > 500:
            break
        et = math.exp(t)
        total += (t ** n) / (et - 1.0)
    total *= h
    total *= n / (x ** n)
    return float(total)


def logistic_function(x: float, upper: float = 1.0, k: float = 1.0, x0: float = 0.0) -> float:
    """Compute the logistic (sigmoid) function f(x) = L / (1 + e^{-k(x - x₀)}).

    Args:
        x: Input value.
        upper: Maximum value (default 1.0).
        k: Steepness (default 1.0).
        x0: Midpoint (default 0.0).

    Returns:
        Logistic function value.

    Raises:
        TypeError: If any argument is not numeric.

    Usage Example:
        >>> logistic_function(0)
        0.5

    Complexity: O(1)
    """
    for name, val in [("x", x), ("upper", upper), ("k", k), ("x0", x0)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    exp_arg = -float(k) * (float(x) - float(x0))
    if exp_arg > 700:
        return 0.0
    if exp_arg < -700:
        return float(upper)
    return float(float(upper) / (1.0 + math.exp(exp_arg)))


def heaviside_step(x: float) -> float:
    """Compute the Heaviside step function H(x).

    H(x) = 0 for x < 0, 0.5 for x = 0, 1 for x > 0.

    Args:
        x: Input value.

    Returns:
        0.0, 0.5, or 1.0.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> heaviside_step(5)
        1.0

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if x < 0:
        return 0.0
    if x == 0:
        return 0.5
    return 1.0


def rectangular_function(x: float) -> float:
    """Compute the rectangular (boxcar) function rect(x).

    rect(x) = 1 for |x| < 0.5, 0.5 for |x| = 0.5, 0 otherwise.

    Args:
        x: Input value.

    Returns:
        0.0, 0.5, or 1.0.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> rectangular_function(0.3)
        1.0

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    ax = abs(float(x))
    if ax < 0.5:
        return 1.0
    if ax == 0.5:
        return 0.5
    return 0.0


def triangular_function(x: float) -> float:
    """Compute the triangular function tri(x) = max(0, 1 - |x|).

    Args:
        x: Input value.

    Returns:
        tri(x) in [0, 1].

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> triangular_function(0.3)
        0.7

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    return float(max(0.0, 1.0 - abs(float(x))))


def ramp_function(x: float) -> float:
    """Compute the ramp function R(x) = max(0, x).

    Args:
        x: Input value.

    Returns:
        R(x).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> ramp_function(3.5)
        3.5

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    return float(max(0.0, float(x)))


def softplus_function(x: float) -> float:
    """Compute the softplus function f(x) = ln(1 + e^x).

    Smooth approximation of the ReLU function.

    Args:
        x: Input value.

    Returns:
        softplus(x).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> round(softplus_function(0), 4)
        0.6931

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if x > 700:
        return x
    return float(math.log1p(math.exp(x)))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 15: Polynomials & Combinatorial Special Functions
# ---------------------------------------------------------------------------

def lambert_w(x: float, tol: float = 1e-12) -> float:
    """Compute the principal branch W₀ of the Lambert W function.

    W(x) satisfies W(x)·e^{W(x)} = x for x ≥ -1/e.

    Args:
        x: Input value ≥ -1/e.
        tol: Convergence tolerance (default 1e-12).

    Returns:
        W₀(x).

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x < -1/e.

    Usage Example:
        >>> round(lambert_w(1.0), 4)
        0.5671

    Complexity: O(N) Halley iterations
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    neg_inv_e = -1.0 / math.e
    if x < neg_inv_e - 1e-14:
        raise ValueError("x must be >= -1/e.")
    if abs(x - neg_inv_e) < 1e-14:
        return -1.0
    # Initial guess
    if x <= 1.0:
        w = x / (1.0 + x) if x > 0 else max(x, -0.9)
    else:
        ln_x = math.log(x)
        w = ln_x - math.log(ln_x)
    # Halley's method
    for _ in range(50):
        ew = math.exp(w)
        f = w * ew - x
        fp = ew * (w + 1.0)
        if abs(fp) < 1e-300:
            break
        fpp = ew * (w + 2.0)
        delta = f * fp / (fp * fp - 0.5 * f * fpp)
        w -= delta
        if abs(delta) < tol:
            break
    return float(w)


def double_factorial(n: int) -> int:
    """Compute the double factorial n!! = n × (n-2) × (n-4) × ··· × (1 or 2).

    Args:
        n: Non-negative integer.

    Returns:
        n!!

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> double_factorial(7)
        105

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    if n <= 1:
        return 1
    result = 1
    k = n
    while k > 1:
        result *= k
        k -= 2
    return result


def central_binomial_coefficient(n: int) -> int:
    """Compute the central binomial coefficient C(2n, n).

    Args:
        n: Non-negative integer.

    Returns:
        C(2n, n).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> central_binomial_coefficient(5)
        252

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return math.comb(2 * n, n)


def pentagonal_number(n: int) -> int:
    """Compute the n-th pentagonal number P_n = n(3n - 1)/2.

    Args:
        n: Non-negative integer.

    Returns:
        The n-th pentagonal number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> pentagonal_number(5)
        35

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return n * (3 * n - 1) // 2


def hexagonal_number(n: int) -> int:
    """Compute the n-th hexagonal number H_n = n(2n - 1).

    Args:
        n: Non-negative integer.

    Returns:
        The n-th hexagonal number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> hexagonal_number(5)
        45

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    return n * (2 * n - 1)


def fibonacci_polynomial(n: int, x: float) -> float:
    """Compute the n-th Fibonacci polynomial F_n(x).

    F_0(x) = 0, F_1(x) = 1, F_n(x) = x·F_{n-1}(x) + F_{n-2}(x).

    Args:
        n: Non-negative integer.
        x: Variable.

    Returns:
        F_n(x).

    Raises:
        TypeError: If n is not int or x is not numeric.
        ValueError: If n < 0.

    Usage Example:
        >>> fibonacci_polynomial(5, 1.0)
        5.0

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    x = float(x)
    if n == 0:
        return 0.0
    if n == 1:
        return 1.0
    a, b = 0.0, 1.0
    for _ in range(2, n + 1):
        a, b = b, x * b + a
    return float(b)


def lucas_polynomial(n: int, x: float) -> float:
    """Compute the n-th Lucas polynomial L_n(x).

    L_0(x) = 2, L_1(x) = x, L_n(x) = x·L_{n-1}(x) + L_{n-2}(x).

    Args:
        n: Non-negative integer.
        x: Variable.

    Returns:
        L_n(x).

    Raises:
        TypeError: If n is not int or x is not numeric.
        ValueError: If n < 0.

    Usage Example:
        >>> lucas_polynomial(5, 1.0)
        11.0

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    x = float(x)
    if n == 0:
        return 2.0
    if n == 1:
        return x
    a, b = 2.0, x
    for _ in range(2, n + 1):
        a, b = b, x * b + a
    return float(b)


def touchard_polynomial(n: int, x: float) -> float:
    """Compute the n-th Touchard (exponential) polynomial T_n(x).

    T_n(x) = Σ_{k=0}^{n} S(n,k) x^k where S(n,k) are Stirling numbers
    of the second kind.

    Args:
        n: Non-negative integer.
        x: Variable.

    Returns:
        T_n(x).

    Raises:
        TypeError: If n is not int or x is not numeric.
        ValueError: If n < 0.

    Usage Example:
        >>> touchard_polynomial(3, 1.0)
        5.0

    Complexity: O(n²)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    x = float(x)
    # Stirling numbers of the second kind using recurrence
    # S(n,0) = 0 for n>0, S(0,0) = 1, S(n,k) = k*S(n-1,k) + S(n-1,k-1)
    if n == 0:
        return 1.0
    stirling = [0.0] * (n + 1)
    stirling[0] = 1.0
    for i in range(1, n + 1):
        new = [0.0] * (n + 1)
        for k in range(1, i + 1):
            new[k] = k * stirling[k] + stirling[k - 1]
        stirling = new
    total = 0.0
    xk = 1.0
    for k in range(n + 1):
        total += stirling[k] * xk
        xk *= x
    return float(total)


def abel_polynomial(n: int, x: float, a: float = 1.0) -> float:
    """Compute the n-th Abel polynomial p_n(x; a) = x(x - na)^{n-1}.

    Args:
        n: Non-negative integer.
        x: Variable.
        a: Parameter (default 1.0).

    Returns:
        p_n(x; a).

    Raises:
        TypeError: If n is not int or x/a are not numeric.
        ValueError: If n < 0.

    Usage Example:
        >>> abel_polynomial(3, 2.0)
        2.0

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be numeric.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    x, a = float(x), float(a)
    if n == 0:
        return 1.0
    base = x - n * a
    return float(x * base ** (n - 1))


def normalized_sinc(x: float) -> float:
    """Compute the normalized sinc function sinc(x) = sin(πx)/(πx).

    Returns 1.0 when x = 0 (the limit).

    Args:
        x: Input value.

    Returns:
        sin(πx)/(πx).

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> normalized_sinc(0)
        1.0

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if x == 0.0:
        return 1.0
    px = math.pi * x
    return float(math.sin(px) / px)
