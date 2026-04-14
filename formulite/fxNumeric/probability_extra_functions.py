"""Pure-Python probability distributions not requiring scipy.

Provides PDF/PMF, CDF and basic moments for distributions covered in
Murray R. Spiegel's *Mathematical Handbook of Formulas and Tables*
that are absent from the scipy-based ``distribution_functions`` module:
geometric, Cauchy, uniform (continuous & discrete), Pareto, Bernoulli,
and Maxwell-Boltzmann.
"""

import math


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_numeric(value: float, name: str = "value") -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric.")


def _check_positive(value: float, name: str = "value") -> None:
    _check_numeric(value, name)

    if value <= 0:
        raise ValueError(f"{name} must be positive.")


def _check_probability(p: float, name: str = "p") -> None:
    _check_numeric(p, name)

    if p < 0 or p > 1:
        raise ValueError(f"{name} must be in [0, 1].")


# ===================================================================
# Bernoulli distribution
# ===================================================================


def bernoulli_pmf(k: int, p: float) -> float:
    """Probability mass function of the Bernoulli distribution.

    P(X=k) = p^k (1-p)^(1-k) for k in {0, 1}.

    Args:
        k: Outcome (0 or 1).
        p: Success probability in [0, 1].

    Returns:
        P(X=k).

    Raises:
        ValueError: If k not in {0,1} or p not in [0,1].

    Example:
        >>> bernoulli_pmf(1, 0.3)
        0.3

    Complexity: O(1)
    """
    _check_probability(p, "p")

    if k not in (0, 1):
        raise ValueError("k must be 0 or 1.")

    return p if k == 1 else 1.0 - p


def bernoulli_mean(p: float) -> float:
    """Mean of the Bernoulli distribution: E[X] = p.

    Args:
        p: Success probability in [0, 1].

    Returns:
        Mean.

    Example:
        >>> bernoulli_mean(0.7)
        0.7

    Complexity: O(1)
    """
    _check_probability(p, "p")
    return p


def bernoulli_variance(p: float) -> float:
    """Variance of the Bernoulli distribution: Var(X) = p(1-p).

    Args:
        p: Success probability in [0, 1].

    Returns:
        Variance.

    Example:
        >>> bernoulli_variance(0.5)
        0.25

    Complexity: O(1)
    """
    _check_probability(p, "p")
    return p * (1.0 - p)


# ===================================================================
# Geometric distribution
# ===================================================================


def geometric_pmf(k: int, p: float) -> float:
    """Probability mass function of the geometric distribution.

    P(X=k) = (1-p)^(k-1) * p for k = 1, 2, 3, ...
    (number of trials until first success).

    Args:
        k: Trial number (k >= 1).
        p: Success probability in (0, 1].

    Returns:
        P(X=k).

    Example:
        >>> round(geometric_pmf(3, 0.5), 4)
        0.125

    Complexity: O(1)
    """
    if not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer.")

    _check_probability(p, "p")

    if p == 0:
        raise ValueError("p must be > 0 for geometric distribution.")

    return (1.0 - p) ** (k - 1) * p


def geometric_cdf(k: int, p: float) -> float:
    """Cumulative distribution function of the geometric distribution.

    P(X <= k) = 1 - (1-p)^k.

    Args:
        k: Number of trials (k >= 1).
        p: Success probability in (0, 1].

    Returns:
        P(X <= k).

    Example:
        >>> geometric_cdf(3, 0.5)
        0.875

    Complexity: O(1)
    """
    if not isinstance(k, int) or k < 1:
        raise ValueError("k must be a positive integer.")

    _check_probability(p, "p")

    if p == 0:
        raise ValueError("p must be > 0.")

    return 1.0 - (1.0 - p) ** k


def geometric_mean_dist(p: float) -> float:
    """Mean of the geometric distribution: E[X] = 1/p.

    Args:
        p: Success probability in (0, 1].

    Returns:
        Mean.

    Example:
        >>> geometric_mean_dist(0.25)
        4.0

    Complexity: O(1)
    """
    _check_probability(p, "p")

    if p == 0:
        raise ValueError("p must be > 0.")

    return 1.0 / p


def geometric_variance_dist(p: float) -> float:
    """Variance of the geometric distribution: Var(X) = (1-p)/p².

    Args:
        p: Success probability in (0, 1].

    Returns:
        Variance.

    Example:
        >>> geometric_variance_dist(0.5)
        2.0

    Complexity: O(1)
    """
    _check_probability(p, "p")

    if p == 0:
        raise ValueError("p must be > 0.")

    return (1.0 - p) / (p * p)


# ===================================================================
# Cauchy (Lorentz) distribution
# ===================================================================


def cauchy_pdf(x: float, x0: float = 0.0, gamma: float = 1.0) -> float:
    """Probability density function of the Cauchy distribution.

    f(x) = 1 / (π γ [1 + ((x-x0)/γ)²]).

    Args:
        x: Point to evaluate.
        x0: Location parameter (median).
        gamma: Scale parameter (> 0).

    Returns:
        PDF value at x.

    Example:
        >>> round(cauchy_pdf(0), 6)
        0.318310

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_numeric(x0, "x0")
    _check_positive(gamma, "gamma")
    z = (x - x0) / gamma
    return 1.0 / (math.pi * gamma * (1.0 + z * z))


def cauchy_cdf(x: float, x0: float = 0.0, gamma: float = 1.0) -> float:
    """Cumulative distribution function of the Cauchy distribution.

    F(x) = (1/π) arctan((x-x0)/γ) + 1/2.

    Args:
        x: Point to evaluate.
        x0: Location parameter.
        gamma: Scale parameter (> 0).

    Returns:
        CDF value at x.

    Example:
        >>> cauchy_cdf(0)
        0.5

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_numeric(x0, "x0")
    _check_positive(gamma, "gamma")
    return math.atan((x - x0) / gamma) / math.pi + 0.5


def cauchy_quantile(p: float, x0: float = 0.0, gamma: float = 1.0) -> float:
    """Quantile (inverse CDF) of the Cauchy distribution.

    Q(p) = x0 + γ tan(π(p - 1/2)).

    Args:
        p: Probability in (0, 1).
        x0: Location parameter.
        gamma: Scale parameter (> 0).

    Returns:
        Quantile value.

    Example:
        >>> cauchy_quantile(0.5)
        0.0

    Complexity: O(1)
    """
    _check_numeric(x0, "x0")
    _check_positive(gamma, "gamma")

    if not isinstance(p, (int, float)) or p <= 0 or p >= 1:
        raise ValueError("p must be in (0, 1).")

    return x0 + gamma * math.tan(math.pi * (p - 0.5))


# ===================================================================
# Continuous uniform distribution
# ===================================================================


def uniform_continuous_pdf(x: float, a: float, b: float) -> float:
    """PDF of the continuous uniform distribution U(a, b).

    f(x) = 1/(b-a) for a <= x <= b, else 0.

    Args:
        x: Point to evaluate.
        a: Lower bound.
        b: Upper bound (b > a).

    Returns:
        PDF value.

    Example:
        >>> uniform_continuous_pdf(0.5, 0, 1)
        1.0

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_numeric(a, "a")
    _check_numeric(b, "b")

    if b <= a:
        raise ValueError("b must be greater than a.")

    if x < a or x > b:
        return 0.0

    return 1.0 / (b - a)


def uniform_continuous_cdf(x: float, a: float, b: float) -> float:
    """CDF of the continuous uniform distribution U(a, b).

    Args:
        x: Point to evaluate.
        a: Lower bound.
        b: Upper bound (b > a).

    Returns:
        CDF value.

    Example:
        >>> uniform_continuous_cdf(0.25, 0, 1)
        0.25

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_numeric(a, "a")
    _check_numeric(b, "b")

    if b <= a:
        raise ValueError("b must be greater than a.")

    if x <= a:
        return 0.0

    if x >= b:
        return 1.0

    return (x - a) / (b - a)


def uniform_continuous_mean(a: float, b: float) -> float:
    """Mean of U(a, b): (a+b)/2.

    Args:
        a: Lower bound.
        b: Upper bound.

    Returns:
        Mean.

    Example:
        >>> uniform_continuous_mean(2, 8)
        5.0

    Complexity: O(1)
    """
    _check_numeric(a, "a")
    _check_numeric(b, "b")
    return (a + b) / 2.0


def uniform_continuous_variance(a: float, b: float) -> float:
    """Variance of U(a, b): (b-a)²/12.

    Args:
        a: Lower bound.
        b: Upper bound (b > a).

    Returns:
        Variance.

    Example:
        >>> round(uniform_continuous_variance(0, 1), 6)
        0.083333

    Complexity: O(1)
    """
    _check_numeric(a, "a")
    _check_numeric(b, "b")

    if b <= a:
        raise ValueError("b must be greater than a.")

    return (b - a) ** 2 / 12.0


# ===================================================================
# Discrete uniform distribution
# ===================================================================


def uniform_discrete_pmf(k: int, a: int, b: int) -> float:
    """PMF of the discrete uniform distribution on {a, a+1, ..., b}.

    P(X=k) = 1/(b-a+1) for a <= k <= b.

    Args:
        k: Integer value.
        a: Lower bound (integer).
        b: Upper bound (integer, b >= a).

    Returns:
        P(X=k).

    Example:
        >>> round(uniform_discrete_pmf(3, 1, 6), 6)
        0.166667

    Complexity: O(1)
    """
    if not isinstance(k, int) or not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("k, a, b must be integers.")

    if b < a:
        raise ValueError("b must be >= a.")

    if k < a or k > b:
        return 0.0

    return 1.0 / (b - a + 1)


def uniform_discrete_cdf(k: int, a: int, b: int) -> float:
    """CDF of the discrete uniform distribution.

    P(X <= k) = (floor(k) - a + 1) / (b - a + 1) for a <= k <= b.

    Args:
        k: Integer value.
        a: Lower bound.
        b: Upper bound.

    Returns:
        P(X <= k).

    Example:
        >>> uniform_discrete_cdf(3, 1, 6)
        0.5

    Complexity: O(1)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a, b must be integers.")

    if b < a:
        raise ValueError("b must be >= a.")

    if k < a:
        return 0.0

    if k >= b:
        return 1.0

    return (k - a + 1) / (b - a + 1)


# ===================================================================
# Pareto distribution
# ===================================================================


def pareto_pdf(x: float, x_m: float, alpha: float) -> float:
    """PDF of the Pareto distribution.

    f(x) = α x_m^α / x^(α+1) for x >= x_m.

    Args:
        x: Point to evaluate.
        x_m: Scale parameter (minimum value, > 0).
        alpha: Shape parameter (> 0).

    Returns:
        PDF value.

    Example:
        >>> pareto_pdf(1, 1, 2)
        2.0

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(x_m, "x_m")
    _check_positive(alpha, "alpha")

    if x < x_m:
        return 0.0

    return alpha * x_m ** alpha / x ** (alpha + 1)


def pareto_cdf(x: float, x_m: float, alpha: float) -> float:
    """CDF of the Pareto distribution.

    F(x) = 1 - (x_m/x)^α for x >= x_m.

    Args:
        x: Point to evaluate.
        x_m: Scale parameter (> 0).
        alpha: Shape parameter (> 0).

    Returns:
        CDF value.

    Example:
        >>> pareto_cdf(2, 1, 2)
        0.75

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(x_m, "x_m")
    _check_positive(alpha, "alpha")

    if x < x_m:
        return 0.0

    return 1.0 - (x_m / x) ** alpha


def pareto_mean(x_m: float, alpha: float) -> float:
    """Mean of the Pareto distribution: α x_m / (α-1) for α > 1.

    Args:
        x_m: Scale parameter (> 0).
        alpha: Shape parameter (> 1).

    Returns:
        Mean.

    Raises:
        ValueError: If alpha <= 1.

    Example:
        >>> pareto_mean(1, 3)
        1.5

    Complexity: O(1)
    """
    _check_positive(x_m, "x_m")
    _check_positive(alpha, "alpha")

    if alpha <= 1:
        raise ValueError("Mean undefined for alpha <= 1.")

    return alpha * x_m / (alpha - 1.0)


def pareto_variance(x_m: float, alpha: float) -> float:
    """Variance of the Pareto distribution: x_m² α / ((α-1)²(α-2)) for α > 2.

    Args:
        x_m: Scale parameter (> 0).
        alpha: Shape parameter (> 2).

    Returns:
        Variance.

    Raises:
        ValueError: If alpha <= 2.

    Example:
        >>> round(pareto_variance(1, 3), 4)
        0.75

    Complexity: O(1)
    """
    _check_positive(x_m, "x_m")
    _check_positive(alpha, "alpha")

    if alpha <= 2:
        raise ValueError("Variance undefined for alpha <= 2.")

    return x_m * x_m * alpha / ((alpha - 1.0) ** 2 * (alpha - 2.0))


# ===================================================================
# Rayleigh distribution
# ===================================================================


def rayleigh_pdf(x: float, sigma: float = 1.0) -> float:
    """PDF of the Rayleigh distribution.

    f(x) = (x/σ²) exp(-x²/(2σ²)) for x >= 0.

    Args:
        x: Point to evaluate (>= 0).
        sigma: Scale parameter (> 0).

    Returns:
        PDF value.

    Example:
        >>> round(rayleigh_pdf(1, 1), 6)
        0.606531

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(sigma, "sigma")

    if x < 0:
        return 0.0

    s2 = sigma * sigma
    return (x / s2) * math.exp(-x * x / (2.0 * s2))


def rayleigh_cdf(x: float, sigma: float = 1.0) -> float:
    """CDF of the Rayleigh distribution.

    F(x) = 1 - exp(-x²/(2σ²)) for x >= 0.

    Args:
        x: Point to evaluate.
        sigma: Scale parameter (> 0).

    Returns:
        CDF value.

    Example:
        >>> round(rayleigh_cdf(1, 1), 6)
        0.393469

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(sigma, "sigma")

    if x < 0:
        return 0.0

    return 1.0 - math.exp(-x * x / (2.0 * sigma * sigma))


def rayleigh_mean(sigma: float = 1.0) -> float:
    """Mean of the Rayleigh distribution: σ√(π/2).

    Args:
        sigma: Scale parameter (> 0).

    Returns:
        Mean.

    Example:
        >>> round(rayleigh_mean(1), 6)
        1.253314

    Complexity: O(1)
    """
    _check_positive(sigma, "sigma")
    return sigma * math.sqrt(math.pi / 2.0)


def rayleigh_variance(sigma: float = 1.0) -> float:
    """Variance of the Rayleigh distribution: (4-π)/2 σ².

    Args:
        sigma: Scale parameter (> 0).

    Returns:
        Variance.

    Example:
        >>> round(rayleigh_variance(1), 6)
        0.429204

    Complexity: O(1)
    """
    _check_positive(sigma, "sigma")
    return (4.0 - math.pi) / 2.0 * sigma * sigma


# ===================================================================
# Maxwell-Boltzmann distribution
# ===================================================================


def maxwell_boltzmann_pdf(x: float, a: float = 1.0) -> float:
    """PDF of the Maxwell-Boltzmann distribution.

    f(x) = √(2/π) x² exp(-x²/(2a²)) / a³  for x >= 0.

    Args:
        x: Speed value (>= 0).
        a: Scale parameter (> 0), related to √(kT/m).

    Returns:
        PDF value.

    Example:
        >>> round(maxwell_boltzmann_pdf(1, 1), 6)
        0.483941

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(a, "a")

    if x < 0:
        return 0.0

    a3 = a * a * a
    return math.sqrt(2.0 / math.pi) * x * x * math.exp(-x * x / (2.0 * a * a)) / a3


def maxwell_boltzmann_cdf(x: float, a: float = 1.0) -> float:
    """CDF of the Maxwell-Boltzmann distribution.

    F(x) = erf(x/(a√2)) - √(2/π)(x/a) exp(-x²/(2a²)).

    Args:
        x: Speed value (>= 0).
        a: Scale parameter (> 0).

    Returns:
        CDF value.

    Example:
        >>> round(maxwell_boltzmann_cdf(1, 1), 6)
        0.198748

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(a, "a")

    if x < 0:
        return 0.0

    z = x / (a * math.sqrt(2.0))
    return math.erf(z) - math.sqrt(2.0 / math.pi) * (x / a) * math.exp(-x * x / (2.0 * a * a))


def maxwell_boltzmann_mean(a: float = 1.0) -> float:
    """Mean of the Maxwell-Boltzmann distribution: 2a√(2/π).

    Args:
        a: Scale parameter (> 0).

    Returns:
        Mean.

    Example:
        >>> round(maxwell_boltzmann_mean(1), 6)
        1.595769

    Complexity: O(1)
    """
    _check_positive(a, "a")
    return 2.0 * a * math.sqrt(2.0 / math.pi)


# ===================================================================
# Log-logistic (Fisk) distribution
# ===================================================================


def log_logistic_pdf(x: float, alpha: float, beta: float) -> float:
    """PDF of the log-logistic distribution.

    f(x) = (β/α)(x/α)^(β-1) / (1 + (x/α)^β)² for x > 0.

    Args:
        x: Point to evaluate (> 0).
        alpha: Scale parameter (> 0).
        beta: Shape parameter (> 0).

    Returns:
        PDF value.

    Example:
        >>> round(log_logistic_pdf(1, 1, 2), 4)
        0.5

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(alpha, "alpha")
    _check_positive(beta, "beta")

    if x <= 0:
        return 0.0

    z = (x / alpha) ** beta
    return (beta / alpha) * (x / alpha) ** (beta - 1) / (1.0 + z) ** 2


def log_logistic_cdf(x: float, alpha: float, beta: float) -> float:
    """CDF of the log-logistic distribution.

    F(x) = 1 / (1 + (x/α)^(-β)) for x > 0.

    Args:
        x: Point to evaluate.
        alpha: Scale parameter (> 0).
        beta: Shape parameter (> 0).

    Returns:
        CDF value.

    Example:
        >>> log_logistic_cdf(1, 1, 2)
        0.5

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(alpha, "alpha")
    _check_positive(beta, "beta")

    if x <= 0:
        return 0.0

    z = (x / alpha) ** beta
    return z / (1.0 + z)
