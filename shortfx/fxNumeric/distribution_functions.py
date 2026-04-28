"""Probability Distributions Module.

Provides probability density/mass functions, cumulative distribution functions,
and their inverses for common distributions. Requires ``scipy`` for most
functions; a graceful ``ImportError`` is raised when scipy is absent.

Key Features:
    - Normal (Gaussian) distribution
    - Student's t-distribution
    - Binomial distribution
    - Poisson distribution
    - Chi-squared distribution
    - F-distribution
    - Exponential distribution

Example:
    >>> from shortfx.fxNumeric.distribution_functions import norm_dist
    >>> round(norm_dist(0, 0, 1, cumulative=True), 4)
    0.5
"""

from __future__ import annotations

import math

_SCIPY_AVAILABLE = True

try:
    from scipy import stats as _st
except ImportError:  # pragma: no cover
    _SCIPY_AVAILABLE = False


def _require_scipy() -> None:
    if not _SCIPY_AVAILABLE:
        raise ImportError(
            "scipy is required for probability distributions. "
            "Install it with: pip install scipy"
        )


# ============================================================================
# NORMAL DISTRIBUTION
# ============================================================================


def norm_dist(x: float, mean: float = 0.0, std_dev: float = 1.0,
              cumulative: bool = True) -> float:
    """Normal (Gaussian) distribution PDF or CDF.

    Args:
        x: The value at which to evaluate.
        mean: Distribution mean. Default 0.
        std_dev: Standard deviation (must be > 0). Default 1.
        cumulative: If True return CDF, else PDF.

    Returns:
        Probability value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If std_dev <= 0.

    Example:
        >>> round(norm_dist(0, 0, 1, cumulative=True), 4)
        0.5
        >>> round(norm_dist(0, 0, 1, cumulative=False), 6)
        0.398942

    Complexity: O(1)
    """
    _require_scipy()

    if not all(isinstance(v, (int, float)) for v in [x, mean, std_dev]):
        raise TypeError("All numeric parameters must be int or float.")

    if std_dev <= 0:
        raise ValueError("Standard deviation must be positive.")

    if cumulative:
        return float(_st.norm.cdf(x, loc=mean, scale=std_dev))

    return float(_st.norm.pdf(x, loc=mean, scale=std_dev))


def norm_inv(probability: float, mean: float = 0.0,
             std_dev: float = 1.0) -> float:
    """Inverse of the normal cumulative distribution (quantile function).

    Args:
        probability: A probability in (0, 1).
        mean: Distribution mean. Default 0.
        std_dev: Standard deviation (must be > 0). Default 1.

    Returns:
        The value x such that P(X <= x) = probability.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If probability is not in (0, 1) or std_dev <= 0.

    Example:
        >>> round(norm_inv(0.975, 0, 1), 4)
        1.96

    Complexity: O(1)
    """
    _require_scipy()

    if not all(isinstance(v, (int, float)) for v in [probability, mean, std_dev]):
        raise TypeError("All numeric parameters must be int or float.")

    if not (0 < probability < 1):
        raise ValueError("Probability must be between 0 and 1 (exclusive).")

    if std_dev <= 0:
        raise ValueError("Standard deviation must be positive.")

    return float(_st.norm.ppf(probability, loc=mean, scale=std_dev))


def norm_s_dist(z: float, cumulative: bool = True) -> float:
    """Standard normal distribution (mean=0, std=1).

    Args:
        z: The z-value.
        cumulative: If True return CDF, else PDF.

    Returns:
        Probability value.

    Example:
        >>> round(norm_s_dist(1.96, cumulative=True), 4)
        0.975

    Complexity: O(1)
    """
    return norm_dist(z, 0.0, 1.0, cumulative)


def norm_s_inv(probability: float) -> float:
    """Inverse of the standard normal cumulative distribution.

    Args:
        probability: A probability in (0, 1).

    Returns:
        The z-value.

    Example:
        >>> round(norm_s_inv(0.975), 4)
        1.96

    Complexity: O(1)
    """
    return norm_inv(probability, 0.0, 1.0)


# ============================================================================
# STUDENT'S T-DISTRIBUTION
# ============================================================================


def t_dist(x: float, deg_freedom: int, cumulative: bool = True) -> float:
    """Student's t-distribution PDF or CDF.

    Args:
        x: The value at which to evaluate.
        deg_freedom: Degrees of freedom (must be >= 1).
        cumulative: If True return CDF, else PDF.

    Returns:
        Probability value.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If deg_freedom < 1.

    Example:
        >>> round(t_dist(0, 10, cumulative=True), 4)
        0.5

    Complexity: O(1)
    """
    _require_scipy()

    if not isinstance(x, (int, float)):
        raise TypeError("'x' must be numeric.")

    if not isinstance(deg_freedom, int):
        raise TypeError("'deg_freedom' must be an integer.")

    if deg_freedom < 1:
        raise ValueError("Degrees of freedom must be at least 1.")

    if cumulative:
        return float(_st.t.cdf(x, df=deg_freedom))

    return float(_st.t.pdf(x, df=deg_freedom))


def t_inv(probability: float, deg_freedom: int) -> float:
    """Inverse of the Student's t cumulative distribution.

    Args:
        probability: A probability in (0, 1).
        deg_freedom: Degrees of freedom (must be >= 1).

    Returns:
        The t-value.

    Example:
        >>> round(t_inv(0.975, 10), 4)
        2.2281

    Complexity: O(1)
    """
    _require_scipy()

    if not isinstance(probability, (int, float)):
        raise TypeError("'probability' must be numeric.")

    if not isinstance(deg_freedom, int):
        raise TypeError("'deg_freedom' must be an integer.")

    if not (0 < probability < 1):
        raise ValueError("Probability must be between 0 and 1 (exclusive).")

    if deg_freedom < 1:
        raise ValueError("Degrees of freedom must be at least 1.")

    return float(_st.t.ppf(probability, df=deg_freedom))


# ============================================================================
# BINOMIAL DISTRIBUTION
# ============================================================================


def binom_dist(number_s: int, trials: int, probability_s: float,
               cumulative: bool = True) -> float:
    """Binomial distribution PMF or CDF.

    Args:
        number_s: Number of successes.
        trials: Number of independent trials.
        probability_s: Probability of success on each trial.
        cumulative: If True return CDF, else PMF.

    Returns:
        Probability value.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If parameters are out of valid ranges.

    Example:
        >>> round(binom_dist(3, 10, 0.5, cumulative=False), 6)
        0.117188

    Complexity: O(1)
    """
    _require_scipy()

    if not isinstance(number_s, int) or not isinstance(trials, int):
        raise TypeError("'number_s' and 'trials' must be integers.")

    if not isinstance(probability_s, (int, float)):
        raise TypeError("'probability_s' must be numeric.")

    if trials < 0:
        raise ValueError("'trials' must be non-negative.")

    if number_s < 0 or number_s > trials:
        raise ValueError("'number_s' must be between 0 and 'trials'.")

    if not (0 <= probability_s <= 1):
        raise ValueError("'probability_s' must be between 0 and 1.")

    if cumulative:
        return float(_st.binom.cdf(number_s, n=trials, p=probability_s))

    return float(_st.binom.pmf(number_s, n=trials, p=probability_s))


# ============================================================================
# POISSON DISTRIBUTION
# ============================================================================


def poisson_dist(x: int, mean: float, cumulative: bool = True) -> float:
    """Poisson distribution PMF or CDF.

    Args:
        x: Number of events.
        mean: Expected number of events (lambda, must be > 0).
        cumulative: If True return CDF, else PMF.

    Returns:
        Probability value.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If parameters are out of valid ranges.

    Example:
        >>> round(poisson_dist(2, 5, cumulative=False), 6)
        0.084224

    Complexity: O(1)
    """
    _require_scipy()

    if not isinstance(x, int):
        raise TypeError("'x' must be an integer.")

    if not isinstance(mean, (int, float)):
        raise TypeError("'mean' must be numeric.")

    if x < 0:
        raise ValueError("'x' must be non-negative.")

    if mean <= 0:
        raise ValueError("'mean' (lambda) must be positive.")

    if cumulative:
        return float(_st.poisson.cdf(x, mu=mean))

    return float(_st.poisson.pmf(x, mu=mean))


# ============================================================================
# CHI-SQUARED DISTRIBUTION
# ============================================================================


def chisq_dist(x: float, deg_freedom: int,
               cumulative: bool = True) -> float:
    """Chi-squared distribution PDF or CDF.

    Args:
        x: The value at which to evaluate (must be >= 0).
        deg_freedom: Degrees of freedom (must be >= 1).
        cumulative: If True return CDF, else PDF.

    Returns:
        Probability value.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If parameters are out of valid ranges.

    Example:
        >>> round(chisq_dist(3.84, 1, cumulative=True), 4)
        0.9499

    Complexity: O(1)
    """
    _require_scipy()

    if not isinstance(x, (int, float)):
        raise TypeError("'x' must be numeric.")

    if not isinstance(deg_freedom, int):
        raise TypeError("'deg_freedom' must be an integer.")

    if x < 0:
        raise ValueError("'x' must be non-negative.")

    if deg_freedom < 1:
        raise ValueError("Degrees of freedom must be at least 1.")

    if cumulative:
        return float(_st.chi2.cdf(x, df=deg_freedom))

    return float(_st.chi2.pdf(x, df=deg_freedom))


def chisq_inv(probability: float, deg_freedom: int) -> float:
    """Inverse of the chi-squared cumulative distribution.

    Args:
        probability: A probability in (0, 1).
        deg_freedom: Degrees of freedom (must be >= 1).

    Returns:
        The chi-squared value.

    Example:
        >>> round(chisq_inv(0.95, 1), 4)
        3.8415

    Complexity: O(1)
    """
    _require_scipy()

    if not isinstance(probability, (int, float)):
        raise TypeError("'probability' must be numeric.")

    if not isinstance(deg_freedom, int):
        raise TypeError("'deg_freedom' must be an integer.")

    if not (0 < probability < 1):
        raise ValueError("Probability must be between 0 and 1 (exclusive).")

    if deg_freedom < 1:
        raise ValueError("Degrees of freedom must be at least 1.")

    return float(_st.chi2.ppf(probability, df=deg_freedom))


# ============================================================================
# F-DISTRIBUTION
# ============================================================================


def f_dist(x: float, deg_freedom1: int, deg_freedom2: int,
           cumulative: bool = True) -> float:
    """F-distribution PDF or CDF.

    Args:
        x: The value at which to evaluate (must be >= 0).
        deg_freedom1: Numerator degrees of freedom (>= 1).
        deg_freedom2: Denominator degrees of freedom (>= 1).
        cumulative: If True return CDF, else PDF.

    Returns:
        Probability value.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If parameters are out of valid ranges.

    Example:
        >>> round(f_dist(3.0, 5, 10, cumulative=True), 4)
        0.9269

    Complexity: O(1)
    """
    _require_scipy()

    if not isinstance(x, (int, float)):
        raise TypeError("'x' must be numeric.")

    if not isinstance(deg_freedom1, int) or not isinstance(deg_freedom2, int):
        raise TypeError("Degrees of freedom must be integers.")

    if x < 0:
        raise ValueError("'x' must be non-negative.")

    if deg_freedom1 < 1 or deg_freedom2 < 1:
        raise ValueError("Both degrees of freedom must be at least 1.")

    if cumulative:
        return float(_st.f.cdf(x, dfn=deg_freedom1, dfd=deg_freedom2))

    return float(_st.f.pdf(x, dfn=deg_freedom1, dfd=deg_freedom2))


def f_inv(probability: float, deg_freedom1: int,
          deg_freedom2: int) -> float:
    """Inverse of the F cumulative distribution.

    Args:
        probability: A probability in (0, 1).
        deg_freedom1: Numerator degrees of freedom (>= 1).
        deg_freedom2: Denominator degrees of freedom (>= 1).

    Returns:
        The F-value.

    Example:
        >>> round(f_inv(0.95, 5, 10), 4)
        3.3258

    Complexity: O(1)
    """
    _require_scipy()

    if not isinstance(probability, (int, float)):
        raise TypeError("'probability' must be numeric.")

    if not isinstance(deg_freedom1, int) or not isinstance(deg_freedom2, int):
        raise TypeError("Degrees of freedom must be integers.")

    if not (0 < probability < 1):
        raise ValueError("Probability must be between 0 and 1 (exclusive).")

    if deg_freedom1 < 1 or deg_freedom2 < 1:
        raise ValueError("Both degrees of freedom must be at least 1.")

    return float(_st.f.ppf(probability, dfn=deg_freedom1, dfd=deg_freedom2))


# ============================================================================
# EXPONENTIAL DISTRIBUTION
# ============================================================================


def expon_dist(x: float, lambda_: float,
               cumulative: bool = True) -> float:
    """Exponential distribution PDF or CDF.

    Args:
        x: The value at which to evaluate (must be >= 0).
        lambda_: Rate parameter (must be > 0).
        cumulative: If True return CDF, else PDF.

    Returns:
        Probability value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If parameters are out of valid ranges.

    Example:
        >>> round(expon_dist(1, 1, cumulative=True), 6)
        0.632121

    Complexity: O(1)
    """
    _require_scipy()

    if not isinstance(x, (int, float)):
        raise TypeError("'x' must be numeric.")

    if not isinstance(lambda_, (int, float)):
        raise TypeError("'lambda_' must be numeric.")

    if x < 0:
        raise ValueError("'x' must be non-negative.")

    if lambda_ <= 0:
        raise ValueError("'lambda_' must be positive.")

    scale = 1.0 / lambda_

    if cumulative:
        return float(_st.expon.cdf(x, scale=scale))

    return float(_st.expon.pdf(x, scale=scale))


def gauss(z: float) -> float:
    """Probability that a standard normal variable falls between 0 and z.

    Description:
        Returns P(0 < Z < z) for the standard normal distribution.
        Equivalent to Excel GAUSS. Computed as Φ(z) − 0.5.

    Args:
        z: The z-score value.

    Returns:
        float: The probability in the range (0, z).

    Raises:
        TypeError: If z is not a number.

    Example:
        >>> round(gauss(2), 6)
        0.47725
        >>> round(gauss(0), 6)
        0.0

    Complexity: O(1)
    """
    if not isinstance(z, (int, float)):
        raise TypeError("z must be a number.")

    _require_scipy()

    return float(_st.norm.cdf(z) - 0.5)


def phi(x: float) -> float:
    """Standard normal probability density function φ(x).

    Description:
        Returns the value of the standard normal PDF at x.
        Equivalent to Excel PHI. Formula: (1/√(2π)) · e^(−x²/2).

    Args:
        x: The point to evaluate.

    Returns:
        float: The PDF value at x.

    Raises:
        TypeError: If x is not a number.

    Example:
        >>> round(phi(0), 6)
        0.398942
        >>> round(phi(1), 6)
        0.241971

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be a number.")

    return float(math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi))


def beta_dist(x: float, alpha: float, beta: float,
              cumulative: bool = True) -> float:
    """Beta distribution PDF or CDF.

    Args:
        x: Value at which to evaluate (0 ≤ x ≤ 1).
        alpha: Alpha parameter (> 0).
        beta: Beta parameter (> 0).
        cumulative: True for CDF, False for PDF.

    Returns:
        float: Probability value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If x not in [0,1] or parameters ≤ 0.

    Example:
        >>> round(beta_dist(0.4, 2, 5), 6)
        0.580096

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [x, alpha, beta]):
        raise TypeError("All parameters must be numeric.")

    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive.")

    if x < 0 or x > 1:
        raise ValueError("x must be in [0, 1].")

    _require_scipy()

    dist = _st.beta(alpha, beta)
    return float(dist.cdf(x) if cumulative else dist.pdf(x))


def beta_inv(probability: float, alpha: float, beta: float) -> float:
    """Inverse of the Beta cumulative distribution.

    Args:
        probability: Probability (0 < p < 1).
        alpha: Alpha parameter (> 0).
        beta: Beta parameter (> 0).

    Returns:
        float: Value x such that P(X ≤ x) = probability.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If probability not in (0,1) or parameters ≤ 0.

    Example:
        >>> round(beta_inv(0.5, 2, 5), 6)
        0.264653

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [probability, alpha, beta]):
        raise TypeError("All parameters must be numeric.")

    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive.")

    if probability <= 0 or probability >= 1:
        raise ValueError("probability must be in (0, 1).")

    _require_scipy()

    return float(_st.beta.ppf(probability, alpha, beta))


def gamma_dist(x: float, alpha: float, beta: float,
               cumulative: bool = True) -> float:
    """Gamma distribution PDF or CDF.

    Args:
        x: Value at which to evaluate (≥ 0).
        alpha: Shape parameter (> 0).
        beta: Scale parameter (> 0).
        cumulative: True for CDF, False for PDF.

    Returns:
        float: Probability value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If x < 0 or parameters ≤ 0.

    Example:
        >>> round(gamma_dist(2, 3, 1), 6)
        0.323324

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [x, alpha, beta]):
        raise TypeError("All parameters must be numeric.")

    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive.")

    if x < 0:
        raise ValueError("x must be >= 0.")

    _require_scipy()

    dist = _st.gamma(alpha, scale=beta)
    return float(dist.cdf(x) if cumulative else dist.pdf(x))


def gamma_inv(probability: float, alpha: float, beta: float) -> float:
    """Inverse of the Gamma cumulative distribution.

    Args:
        probability: Probability (0 < p < 1).
        alpha: Shape parameter (> 0).
        beta: Scale parameter (> 0).

    Returns:
        float: Value x such that P(X ≤ x) = probability.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If probability not in (0,1) or parameters ≤ 0.

    Example:
        >>> round(gamma_inv(0.5, 3, 1), 6)
        2.674051

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [probability, alpha, beta]):
        raise TypeError("All parameters must be numeric.")

    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive.")

    if probability <= 0 or probability >= 1:
        raise ValueError("probability must be in (0, 1).")

    _require_scipy()

    return float(_st.gamma.ppf(probability, alpha, scale=beta))


def lognorm_dist(x: float, mean: float, standard_dev: float,
                 cumulative: bool = True) -> float:
    """Log-normal distribution PDF or CDF.

    Args:
        x: Value at which to evaluate (> 0).
        mean: Mean of ln(x).
        standard_dev: Standard deviation of ln(x) (> 0).
        cumulative: True for CDF, False for PDF.

    Returns:
        float: Probability value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If x ≤ 0 or standard_dev ≤ 0.

    Example:
        >>> round(lognorm_dist(4, 3.5, 1.2), 6)
        0.01761

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [x, mean, standard_dev]):
        raise TypeError("All parameters must be numeric.")

    if standard_dev <= 0:
        raise ValueError("standard_dev must be positive.")

    if x <= 0:
        raise ValueError("x must be positive.")

    _require_scipy()

    dist = _st.lognorm(s=standard_dev, scale=math.exp(mean))
    return float(dist.cdf(x) if cumulative else dist.pdf(x))


def lognorm_inv(probability: float, mean: float,
                standard_dev: float) -> float:
    """Inverse of the Log-normal cumulative distribution.

    Args:
        probability: Probability (0 < p < 1).
        mean: Mean of ln(x).
        standard_dev: Standard deviation of ln(x) (> 0).

    Returns:
        float: Value x such that P(X ≤ x) = probability.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If probability not in (0,1) or standard_dev ≤ 0.

    Example:
        >>> round(lognorm_inv(0.5, 3.5, 1.2), 6)
        33.11545

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [probability, mean, standard_dev]):
        raise TypeError("All parameters must be numeric.")

    if standard_dev <= 0:
        raise ValueError("standard_dev must be positive.")

    if probability <= 0 or probability >= 1:
        raise ValueError("probability must be in (0, 1).")

    _require_scipy()

    return float(_st.lognorm.ppf(probability, s=standard_dev, scale=math.exp(mean)))


def negbinom_dist(number_f: int, number_s: int, probability_s: float,
                  cumulative: bool = True) -> float:
    """Negative binomial distribution PMF or CDF.

    Args:
        number_f: Number of failures before the number_s-th success.
        number_s: Number of successes (> 0).
        probability_s: Probability of success per trial (0 < p ≤ 1).
        cumulative: True for CDF, False for PMF.

    Returns:
        float: Probability value.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If parameters out of range.

    Example:
        >>> round(negbinom_dist(3, 5, 0.4), 6)
        0.174286

    Complexity: O(1)
    """
    if not isinstance(number_f, int) or not isinstance(number_s, int):
        raise TypeError("number_f and number_s must be integers.")

    if not isinstance(probability_s, (int, float)):
        raise TypeError("probability_s must be numeric.")

    if number_f < 0:
        raise ValueError("number_f must be >= 0.")

    if number_s < 1:
        raise ValueError("number_s must be >= 1.")

    if probability_s <= 0 or probability_s > 1:
        raise ValueError("probability_s must be in (0, 1].")

    _require_scipy()

    dist = _st.nbinom(number_s, probability_s)
    return float(dist.cdf(number_f) if cumulative else dist.pmf(number_f))


def weibull_dist(x: float, alpha: float, beta: float,
                 cumulative: bool = True) -> float:
    """Weibull distribution PDF or CDF.

    Args:
        x: Value at which to evaluate (≥ 0).
        alpha: Shape parameter (> 0).
        beta: Scale parameter (> 0).
        cumulative: True for CDF, False for PDF.

    Returns:
        float: Probability value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If x < 0 or parameters ≤ 0.

    Example:
        >>> round(weibull_dist(2, 3, 1), 6)
        0.999877

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [x, alpha, beta]):
        raise TypeError("All parameters must be numeric.")

    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive.")

    if x < 0:
        raise ValueError("x must be >= 0.")

    _require_scipy()

    dist = _st.weibull_min(alpha, scale=beta)
    return float(dist.cdf(x) if cumulative else dist.pdf(x))


def hypgeom_dist(sample_s: int, number_sample: int, population_s: int,
                 number_pop: int, cumulative: bool = True) -> float:
    """Hypergeometric distribution PMF or CDF.

    Args:
        sample_s: Number of successes in the sample.
        number_sample: Size of the sample.
        population_s: Number of successes in the population.
        number_pop: Population size.
        cumulative: True for CDF, False for PMF.

    Returns:
        float: Probability value.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If parameters out of range.

    Example:
        >>> round(hypgeom_dist(1, 4, 8, 20), 6)
        0.213995

    Complexity: O(1)
    """
    if not all(isinstance(v, int) for v in [sample_s, number_sample,
                                             population_s, number_pop]):
        raise TypeError("All parameters must be integers.")

    if number_pop < 1:
        raise ValueError("number_pop must be >= 1.")

    if population_s < 0 or population_s > number_pop:
        raise ValueError("population_s must be in [0, number_pop].")

    if number_sample < 1 or number_sample > number_pop:
        raise ValueError("number_sample must be in [1, number_pop].")

    if sample_s < 0:
        raise ValueError("sample_s must be >= 0.")

    _require_scipy()

    dist = _st.hypergeom(number_pop, population_s, number_sample)
    return float(dist.cdf(sample_s) if cumulative else dist.pmf(sample_s))


def binom_dist_range(trials: int, probability_s: float,
                     number_s: int, number_s2: int | None = None) -> float:
    """Probability of a binomial trial result between two values.

    Args:
        trials: Number of trials.
        probability_s: Probability of success per trial.
        number_s: Lower bound of successes.
        number_s2: Upper bound of successes (defaults to number_s).

    Returns:
        float: Probability of successes in [number_s, number_s2].

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If parameters out of range.

    Example:
        >>> round(binom_dist_range(10, 0.5, 3, 7), 6)
        0.890625

    Complexity: O(k) where k = number_s2 - number_s
    """
    if number_s2 is None:
        number_s2 = number_s

    if not isinstance(trials, int):
        raise TypeError("trials must be an integer.")

    if not isinstance(probability_s, (int, float)):
        raise TypeError("probability_s must be numeric.")

    if not isinstance(number_s, int) or not isinstance(number_s2, int):
        raise TypeError("number_s and number_s2 must be integers.")

    if trials < 0:
        raise ValueError("trials must be >= 0.")

    if probability_s < 0 or probability_s > 1:
        raise ValueError("probability_s must be in [0, 1].")

    if number_s > number_s2:
        raise ValueError("number_s must be <= number_s2.")

    _require_scipy()

    return float(sum(
        _st.binom.pmf(k, trials, probability_s)
        for k in range(number_s, number_s2 + 1)
    ))


def binom_inv(trials: int, probability_s: float,
              alpha: float) -> int:
    """Inverse binomial distribution (CRITBINOM).

    Description:
        Returns the smallest value k such that
        P(X ≤ k) ≥ alpha for a binomial distribution.

    Args:
        trials: Number of trials.
        probability_s: Probability of success per trial.
        alpha: Criterion probability (0 < alpha < 1).

    Returns:
        int: Smallest k satisfying the criterion.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If parameters out of range.

    Example:
        >>> binom_inv(6, 0.5, 0.75)
        4

    Complexity: O(1)
    """
    if not isinstance(trials, int):
        raise TypeError("trials must be an integer.")

    if not isinstance(probability_s, (int, float)):
        raise TypeError("probability_s must be numeric.")

    if not isinstance(alpha, (int, float)):
        raise TypeError("alpha must be numeric.")

    if trials < 0:
        raise ValueError("trials must be >= 0.")

    if probability_s < 0 or probability_s > 1:
        raise ValueError("probability_s must be in [0, 1].")

    if alpha <= 0 or alpha >= 1:
        raise ValueError("alpha must be in (0, 1).")

    _require_scipy()

    return int(_st.binom.ppf(alpha, trials, probability_s))


def t_dist_rt(x: float, deg_freedom: int) -> float:
    """Right-tailed Student's t-distribution.

    Args:
        x: Value at which to evaluate.
        deg_freedom: Degrees of freedom (> 0).

    Returns:
        float: P(T > x).

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If deg_freedom ≤ 0.

    Example:
        >>> round(t_dist_rt(1.96, 10), 6)
        0.039317

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(deg_freedom, int) or deg_freedom <= 0:
        raise ValueError("deg_freedom must be a positive integer.")

    _require_scipy()

    return float(_st.t.sf(x, deg_freedom))


def t_dist_2t(x: float, deg_freedom: int) -> float:
    """Two-tailed Student's t-distribution.

    Args:
        x: Value at which to evaluate (must be ≥ 0).
        deg_freedom: Degrees of freedom (> 0).

    Returns:
        float: P(|T| > x) = 2 * P(T > |x|).

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If x < 0 or deg_freedom ≤ 0.

    Example:
        >>> round(t_dist_2t(1.96, 10), 6)
        0.078634

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if x < 0:
        raise ValueError("x must be >= 0 for two-tailed distribution.")

    if not isinstance(deg_freedom, int) or deg_freedom <= 0:
        raise ValueError("deg_freedom must be a positive integer.")

    _require_scipy()

    return float(2 * _st.t.sf(abs(x), deg_freedom))


def t_inv_2t(probability: float, deg_freedom: int) -> float:
    """Inverse of two-tailed Student's t-distribution.

    Args:
        probability: Two-tailed probability (0 < p < 1).
        deg_freedom: Degrees of freedom (> 0).

    Returns:
        float: Value t such that P(|T| > t) = probability.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If probability not in (0,1) or deg_freedom ≤ 0.

    Example:
        >>> round(t_inv_2t(0.05, 10), 6)
        2.228139

    Complexity: O(1)
    """
    if not isinstance(probability, (int, float)):
        raise TypeError("probability must be numeric.")

    if probability <= 0 or probability >= 1:
        raise ValueError("probability must be in (0, 1).")

    if not isinstance(deg_freedom, int) or deg_freedom <= 0:
        raise ValueError("deg_freedom must be a positive integer.")

    _require_scipy()

    return float(_st.t.ppf(1 - probability / 2, deg_freedom))


def chisq_dist_rt(x: float, deg_freedom: int) -> float:
    """Right-tailed Chi-squared distribution.

    Args:
        x: Value at which to evaluate (≥ 0).
        deg_freedom: Degrees of freedom (> 0).

    Returns:
        float: P(X² > x).

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If x < 0 or deg_freedom ≤ 0.

    Example:
        >>> round(chisq_dist_rt(18.307, 10), 6)
        0.05

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if x < 0:
        raise ValueError("x must be >= 0.")

    if not isinstance(deg_freedom, int) or deg_freedom <= 0:
        raise ValueError("deg_freedom must be a positive integer.")

    _require_scipy()

    return float(_st.chi2.sf(x, deg_freedom))


def chisq_inv_rt(probability: float, deg_freedom: int) -> float:
    """Inverse of the right-tailed Chi-squared distribution.

    Args:
        probability: Right-tail probability (0 < p < 1).
        deg_freedom: Degrees of freedom (> 0).

    Returns:
        float: Value x such that P(X² > x) = probability.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If probability not in (0,1) or deg_freedom ≤ 0.

    Example:
        >>> round(chisq_inv_rt(0.05, 10), 4)
        18.307

    Complexity: O(1)
    """
    if not isinstance(probability, (int, float)):
        raise TypeError("probability must be numeric.")

    if probability <= 0 or probability >= 1:
        raise ValueError("probability must be in (0, 1).")

    if not isinstance(deg_freedom, int) or deg_freedom <= 0:
        raise ValueError("deg_freedom must be a positive integer.")

    _require_scipy()

    return float(_st.chi2.isf(probability, deg_freedom))


def f_dist_rt(x: float, deg_freedom1: int, deg_freedom2: int) -> float:
    """Right-tailed F-distribution.

    Args:
        x: Value at which to evaluate (≥ 0).
        deg_freedom1: Numerator degrees of freedom (> 0).
        deg_freedom2: Denominator degrees of freedom (> 0).

    Returns:
        float: P(F > x).

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If x < 0 or degrees of freedom ≤ 0.

    Example:
        >>> round(f_dist_rt(3.5, 5, 10), 6)
        0.044525

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if x < 0:
        raise ValueError("x must be >= 0.")

    if not isinstance(deg_freedom1, int) or deg_freedom1 <= 0:
        raise ValueError("deg_freedom1 must be a positive integer.")

    if not isinstance(deg_freedom2, int) or deg_freedom2 <= 0:
        raise ValueError("deg_freedom2 must be a positive integer.")

    _require_scipy()

    return float(_st.f.sf(x, deg_freedom1, deg_freedom2))


def f_inv_rt(probability: float, deg_freedom1: int,
             deg_freedom2: int) -> float:
    """Inverse of the right-tailed F-distribution.

    Args:
        probability: Right-tail probability (0 < p < 1).
        deg_freedom1: Numerator degrees of freedom (> 0).
        deg_freedom2: Denominator degrees of freedom (> 0).

    Returns:
        float: Value x such that P(F > x) = probability.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If probability not in (0,1) or degrees of freedom ≤ 0.

    Example:
        >>> round(f_inv_rt(0.05, 5, 10), 6)
        3.325835

    Complexity: O(1)
    """
    if not isinstance(probability, (int, float)):
        raise TypeError("probability must be numeric.")

    if probability <= 0 or probability >= 1:
        raise ValueError("probability must be in (0, 1).")

    if not isinstance(deg_freedom1, int) or deg_freedom1 <= 0:
        raise ValueError("deg_freedom1 must be a positive integer.")

    if not isinstance(deg_freedom2, int) or deg_freedom2 <= 0:
        raise ValueError("deg_freedom2 must be a positive integer.")

    _require_scipy()

    return float(_st.f.isf(probability, deg_freedom1, deg_freedom2))
