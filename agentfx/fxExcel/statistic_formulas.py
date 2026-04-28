"""
AgentFx fxExcel - Statistical Functions Module

Excel-compatible statistical functions using official English Excel function names.
All functions follow Excel's standard naming conventions.
"""

import math
from typing import List, Union, Optional, Any

from agentfx.fxNumeric.distribution_functions import (
    binom_dist as _core_binom_dist,
    binom_dist_range as _core_binom_dist_range,
    binom_inv as _core_binom_inv,
    chisq_dist as _core_chisq_dist,
    chisq_dist_rt as _core_chisq_dist_rt,
    chisq_inv as _core_chisq_inv,
    chisq_inv_rt as _core_chisq_inv_rt,
    expon_dist as _core_expon_dist,
    f_dist as _core_f_dist,
    f_dist_rt as _core_f_dist_rt,
    f_inv as _core_f_inv,
    f_inv_rt as _core_f_inv_rt,
    gamma_dist as _core_gamma_dist,
    gamma_inv as _core_gamma_inv,
    gauss as _core_gauss,
    hypgeom_dist as _core_hypgeom_dist,
    lognorm_dist as _core_lognorm_dist,
    lognorm_inv as _core_lognorm_inv,
    negbinom_dist as _core_negbinom_dist,
    norm_dist as _core_norm_dist,
    norm_inv as _core_norm_inv,
    norm_s_dist as _core_norm_s_dist,
    norm_s_inv as _core_norm_s_inv,
    phi as _core_phi,
    poisson_dist as _core_poisson_dist,
    t_dist as _core_t_dist,
    t_dist_2t as _core_t_dist_2t,
    t_dist_rt as _core_t_dist_rt,
    t_inv as _core_t_inv,
    t_inv_2t as _core_t_inv_2t,
    weibull_dist as _core_weibull_dist,
)
from agentfx.fxNumeric.statistics_functions import (
    average_deviation as _core_average_deviation,
    calculate_covariance as _core_covariance,
    calculate_mean as _core_mean,
    calculate_median as _core_median,
    calculate_pearson_correlation as _core_pearson,
    calculate_standard_deviation as _core_std_dev,
    calculate_variance as _core_variance,
    confidence_norm as _core_confidence_norm,
    confidence_t as _core_confidence_t,
    fisher as _core_fisher,
    forecast_ets as _core_forecast_ets,
    forecast_linear as _core_forecast_linear,
    geometric_mean as _core_geometric_mean,
    harmonic_mean as _core_harmonic_mean,
    intercept as _core_intercept,
    kurtosis as _core_kurtosis,
    frequency_bins as _core_frequency,
    fisher_inv as _core_fisher_inv,
    large as _core_large,
    max_if as _core_max_if,
    min_if as _core_min_if,
    mode_mult as _core_mode_mult,
    percentile_exc as _core_percentile_exc,
    percentrank_exc as _core_percentrank_exc,
    probability_range as _core_probability_range,
    small as _core_small,
    standard_error_estimate as _core_standard_error_estimate,
    average_if as _core_average_if,
    slope as _core_slope,
    standardize as _core_standardize,
    sum_of_squared_deviations as _core_devsq,
    t_test as _core_t_test,
    trimmed_mean as _core_trimmed_mean,
    calculate_percentile as _core_percentile,
    rank as _core_rank,
    mode_single as _core_mode_single,
    trend as _core_trend,
)
from agentfx.fxNumeric.arithmetic_functions import (
    gamma as _core_gamma,
    log_gamma as _core_log_gamma,
    permutations as _core_permutations,
    permutations_with_repetition as _core_permutationa,
)
from agentfx.fxPython.py_operations import (
    count_numbers as _core_count_numbers,
    count_values as _core_count_values,
    count_blank as _core_count_blank,
    count_if as _core_count_if,
    count_ifs as _core_count_ifs,
)


def _get_scipy_stats():
    """Lazy-load scipy.stats, raising ImportError with guidance."""
    try:
        import scipy.stats as _stats
    except ImportError:  # pragma: no cover
        raise ImportError(
            "scipy is required for Excel statistical functions. "
            "Install it with: pip install scipy"
        )
    return _stats


def _polyfit1(x: list, y: list) -> tuple:
    """Simple degree-1 least-squares fit. Returns (slope, intercept)."""
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxy = sum(xi * yi for xi, yi in zip(x, y))
    sxx = sum(xi * xi for xi in x)
    denom = n * sxx - sx * sx
    slope = (n * sxy - sx * sy) / denom
    intercept = (sy - slope * sx) / n
    return (slope, intercept)


def _percentile(arr: list, pct: float, method: str = 'linear') -> float:
    """Compute percentile (0-100) with linear or Weibull interpolation."""
    n = len(arr)

    if method == 'weibull':
        rank = pct / 100 * (n + 1) - 1
    else:
        rank = pct / 100 * (n - 1)

    lower = int(math.floor(rank))
    upper = int(math.ceil(rank))
    lower = max(0, min(lower, n - 1))
    upper = max(0, min(upper, n - 1))

    if lower == upper:
        return arr[lower]

    frac = rank - lower
    return arr[lower] + frac * (arr[upper] - arr[lower])


def _meets_criteria(value, criteria):
    """Check if a value meets a given Excel-style criteria expression."""

    if isinstance(criteria, str):

        for op in ['>=', '<=', '<>', '>', '<', '=']:

            if criteria.startswith(op):
                criteria_val = criteria[len(op):]

                try:
                    criteria_num = float(criteria_val)
                    value_num = float(value) if isinstance(value, (int, float)) else 0

                    if op == '>=':
                        return value_num >= criteria_num
                    elif op == '<=':
                        return value_num <= criteria_num
                    elif op == '<>':
                        return value_num != criteria_num
                    elif op == '>':
                        return value_num > criteria_num
                    elif op == '<':
                        return value_num < criteria_num
                    elif op == '=':
                        return value_num == criteria_num
                except Exception:
                    return str(value) == criteria_val if op == '=' else str(value) != criteria_val

        return str(value) == criteria
    else:
        return value == criteria


def _extract_numerics(*values: Union[float, int, List]) -> List[Union[int, float]]:
    """Flatten variadic args and filter to numeric values, excluding booleans."""
    result = []

    for val in values:

        if isinstance(val, (list, tuple)):

            for v in val:

                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    result.append(v)

        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            result.append(val)

    return result


def _convert_values_a(*values: Union[float, int, str, bool, List]) -> List[Union[int, float]]:
    """Flatten variadic args converting text→0, True→1, False→0, skipping None/empty."""
    result = []

    for val in values:

        if isinstance(val, (list, tuple)):

            for v in val:

                if v is None or v == "":
                    continue
                elif isinstance(v, bool):
                    result.append(1 if v else 0)
                elif isinstance(v, str):
                    result.append(0)
                elif isinstance(v, (int, float)):
                    result.append(v)

        else:

            if val is None or val == "":
                continue
            elif isinstance(val, bool):
                result.append(1 if val else 0)
            elif isinstance(val, str):
                result.append(0)
            elif isinstance(val, (int, float)):
                result.append(val)

    return result


# ============================================================================
# CORRELATION AND COVARIANCE FUNCTIONS
# ============================================================================

def CORREL(array1: List[float], array2: List[float]) -> float:
    """
    Returns the correlation coefficient between two data sets.
    
    Excel function: CORREL
    
    Args:
        array1: First array of values
        array2: Second array of values
    
    Returns:
        float: Correlation coefficient between -1 and 1
    
    Raises:
        ValueError: If arrays have different lengths or less than 2 elements
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> CORREL([1, 2, 3], [2, 4, 6])
        1.0
    """
    if len(array1) != len(array2) or len(array1) < 2:
        raise ValueError("Arrays must have equal length and at least 2 elements")
    return _core_pearson(array1, array2)


def PEARSON(array1: List[float], array2: List[float]) -> float:
    """Returns the Pearson product-moment correlation coefficient.

    Identical to CORREL. Measures the linear relationship between two
    data sets, returning a value between -1 and 1.

    Excel function: PEARSON

    Args:
        array1: First array of values.
        array2: Second array of values.

    Returns:
        float: Pearson correlation coefficient between -1 and 1.

    Raises:
        ValueError: If arrays have different lengths or less than 2 elements.

    Usage Example:
        >>> round(PEARSON([1, 2, 3, 4, 5], [2, 4, 6, 8, 10]), 10)
        1.0
        >>> round(PEARSON([1, 2, 3], [3, 1, 2]), 6)
        -0.5

    Cost: O(n)
    """
    return CORREL(array1, array2)


# ============================================================================
# COUNTING FUNCTIONS
# ============================================================================

def COUNT(*values: Union[float, int]) -> int:
    """
    Counts the number of cells that contain numbers.
    
    Excel function: COUNT
    
    Args:
        *values: Values to count (only numeric values are counted)
    
    Returns:
        int: Count of numeric values
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> COUNT(1, 2, "text", None, 3.5)
        3
    """
    return _core_count_numbers(*values)


def COUNTA(*values: Any) -> int:
    """
    Counts the number of cells that are not empty.
    
    Excel function: COUNTA
    
    Args:
        *values: Values to count (all non-None values are counted)
    
    Returns:
        int: Count of non-None values
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> COUNTA(1, 2, "text", None, 3.5)
        4
    """
    return _core_count_values(*values)


def COUNTBLANK(range_values: List[Any]) -> int:
    """
    Counts empty cells in a range.
    
    Excel function: COUNTBLANK
    
    Args:
        range_values: Range of cells to check
    
    Returns:
        int: Count of blank (None or empty string) cells
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> COUNTBLANK([1, None, "", 3, None])
        3
    """
    return _core_count_blank(range_values)


def COUNTIF(range_values: List[Any], criteria: Any) -> int:
    """
    Counts the number of cells that meet a criterion.
    
    Excel function: COUNTIF
    
    Args:
        range_values: Range of values to evaluate
        criteria: Criterion in the form of a number, expression, or text
                 Supports operators: >, <, >=, <=, =, <>
    
    Returns:
        int: Count of cells meeting the criteria
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> COUNTIF([1, 2, 3, 4, 5], ">3")
        2
    """
    return _core_count_if(range_values, criteria)


def COUNTIFS(*args) -> int:
    """
    Counts cells that meet multiple criteria.
    
    Excel function: COUNTIFS
    
    Args:
        *args: Alternating range and criteria pairs (range1, criteria1, range2, criteria2, ...)
    
    Returns:
        int: Count of cells meeting all criteria
    
    Raises:
        ValueError: If arguments are not in pairs
    
    Cost:
        O(n * m) - where m is number of criteria
    
    Usage:
        >>> COUNTIFS([1,2,3,4], ">2", [10,20,30,40], "<35")
        2
    """
    if len(args) % 2 != 0:
        raise ValueError("Arguments must be in range/criteria pairs")

    if len(args) < 2:
        return 0

    first_range = args[0]
    return _core_count_ifs(first_range, *args)


# ============================================================================
# COVARIANCE FUNCTIONS
# ============================================================================

def COVARIANCE_P(array1: List[float], array2: List[float]) -> float:
    """
    Returns population covariance, the average of the products of deviations.
    
    Excel function: COVARIANCE.P
    
    Args:
        array1: First array of values
        array2: Second array of values
    
    Returns:
        float: Population covariance
    
    Raises:
        ValueError: If arrays have different lengths or are empty
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> COVARIANCE_P([3, 2, 4, 5, 6], [9, 7, 12, 15, 17])
        5.2
    """
    if len(array1) != len(array2) or len(array1) < 1:
        raise ValueError("Arrays must have equal length and at least 1 element")
    return _core_covariance(list(array1), list(array2), sample=False)


def COVARIANCE_S(array1: List[float], array2: List[float]) -> float:
    """
    Returns sample covariance.
    
    Excel function: COVARIANCE.S
    
    Args:
        array1: First array of values
        array2: Second array of values
    
    Returns:
        float: Sample covariance
    
    Raises:
        ValueError: If arrays have different lengths or less than 2 elements
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> COVARIANCE_S([2, 4, 8], [5, 11, 12])
        9.666...
    """
    if len(array1) != len(array2) or len(array1) < 2:
        raise ValueError("Arrays must have equal length and at least 2 elements")
    return _core_covariance(list(array1), list(array2), sample=True)


def COVAR(array1: List[float], array2: List[float]) -> float:
    """
    Returns covariance (legacy Excel 2007 function, equivalent to COVARIANCE.P).
    
    Excel function: COVAR
    
    Args:
        array1: First array of values
        array2: Second array of values
    
    Returns:
        float: Population covariance
    
    Cost:
        O(n) - Linear time complexity
    """
    return COVARIANCE_P(array1, array2)


# ============================================================================
# TREND AND REGRESSION FUNCTIONS
# ============================================================================

def GROWTH(known_y: List[float], known_x: Optional[List[float]] = None, 
           new_x: Optional[List[float]] = None, const: bool = True) -> List[float]:
    """
    Returns values along an exponential trend.
    
    Excel function: GROWTH
    
    Args:
        known_y: Set of known y-values
        known_x: Optional set of known x-values (defaults to 1, 2, 3, ...)
        new_x: Optional new x-values for prediction (defaults to known_x)
        const: If True, calculate b normally; if False, force b to equal 1
    
    Returns:
        List[float]: Predicted exponential values
    
    Raises:
        ValueError: If known arrays have different lengths
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> GROWTH([10, 20, 40, 80], [1, 2, 3, 4], [5, 6])
        [160.0, 320.0]
    """
    if known_x is None:
        known_x = list(range(1, len(known_y) + 1))
    if new_x is None:
        new_x = known_x
    if len(known_y) != len(known_x):
        raise ValueError("known_y and known_x must have equal length")
    
    log_y = [math.log(y) for y in known_y]
    slope, intercept = _polyfit1(known_x, log_y)

    if const:
        return [math.exp(intercept + slope * x) for x in new_x]
    else:
        # Force constant term to 1 (intercept = 0)
        s_xy = sum(x * ly for x, ly in zip(known_x, log_y))
        s_xx = sum(x * x for x in known_x)
        slope = s_xy / s_xx
        return [math.exp(slope * x) for x in new_x]


# ============================================================================
# DESCRIPTIVE STATISTICS
# ============================================================================

def KURT(values: List[float]) -> float:
    """
    Returns the kurtosis of a data set (excess kurtosis).
    
    Excel function: KURT
    
    Args:
        values: Array of values (requires at least 4 data points)
    
    Returns:
        float: Kurtosis value (excess kurtosis using Fisher's definition)
    
    Raises:
        ValueError: If less than 4 data points
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> KURT([3, 4, 5, 2, 3, 4, 5, 6, 4, 7])
        -0.1518...
    """
    return _core_kurtosis(list(values), excess=True)


def AVEDEV(values: List[float]) -> float:
    """
    Returns the average of the absolute deviations of data points from their mean.
    
    Excel function: AVEDEV
    
    Args:
        values: Array of values
    
    Returns:
        float: Average absolute deviation
    
    Raises:
        ValueError: If values is empty
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> AVEDEV([4, 5, 6, 7, 5, 4, 3])
        1.020...
    """
    return _core_average_deviation(list(values))


def DEVSQ(values: List[float]) -> float:
    """
    Returns the sum of squares of deviations.
    
    Excel function: DEVSQ
    
    Args:
        values: Array of values
    
    Returns:
        float: Sum of squared deviations from mean
    
    Raises:
        ValueError: If values is empty
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> DEVSQ([4, 5, 6, 7, 5, 4, 3])
        16.857...
    """
    return _core_devsq(list(values))


def GEOMEAN(values: List[float]) -> float:
    """
    Returns the geometric mean of an array of positive numbers.
    
    Excel function: GEOMEAN
    
    Args:
        values: Array of positive values
    
    Returns:
        float: Geometric mean
    
    Raises:
        ValueError: If any value is zero or negative
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> GEOMEAN([4, 5, 8, 7, 11, 4, 3])
        5.476...
    """
    if any(x <= 0 for x in values):
        raise ValueError("Geometric mean requires positive values")
    return float(_core_geometric_mean(list(values)))


def HARMEAN(values: List[float]) -> float:
    """
    Returns the harmonic mean of a data set.
    
    Excel function: HARMEAN
    
    Args:
        values: Array of positive values
    
    Returns:
        float: Harmonic mean
    
    Raises:
        ValueError: If any value is zero or negative
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> HARMEAN([4, 5, 8, 7, 11, 4, 3])
        5.028...
    """
    if any(x <= 0 for x in values):
        raise ValueError("Harmonic mean requires positive values")
    return float(_core_harmonic_mean(list(values)))


def LARGE(array: List[float], k: int) -> float:
    """
    Returns the k-th largest value in a data set.
    
    Excel function: LARGE
    
    Args:
        array: Array of values
        k: Position (from the largest) in the array to return
    
    Returns:
        float: k-th largest value
    
    Raises:
        ValueError: If k is out of valid range
    
    Cost:
        O(n log n) - Due to sorting
    
    Usage:
        >>> LARGE([3, 5, 3, 5, 4], 3)
        4
    """
    return float(_core_large(list(array), k))


def MAX(*values: Union[float, int]) -> float:
    """
    Returns the largest value in a set of values.
    
    Excel function: MAX
    
    Args:
        *values: Values to evaluate (ignores text and logical values)
    
    Returns:
        float: Maximum value
    
    Raises:
        ValueError: If no numeric values provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> MAX(10, 7, 9, 27, 2)
        27
    """
    nums = [x for x in values if isinstance(x, (int, float)) and not isinstance(x, bool)]
    if not nums:
        raise ValueError("No numeric values provided")
    return float(max(nums))


def MAXA(*values: Any) -> float:
    """
    Returns the largest value in a set of values (includes text and logical values).
    
    Excel function: MAXA
    
    Args:
        *values: Values to evaluate (TRUE=1, FALSE=0, text=0)
    
    Returns:
        float: Maximum value
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> MAXA(10, 7, 9, True, 2)
        10
    """
    converted = []
    for x in values:
        if isinstance(x, bool):
            converted.append(1.0 if x else 0.0)
        elif isinstance(x, (int, float)):
            converted.append(float(x))
        elif isinstance(x, str):
            converted.append(0.0)
        elif x is not None:
            converted.append(0.0)
    
    if not converted:
        raise ValueError("No values provided")
    return max(converted)


def MAXIFS(max_range: List[float], *args) -> float:
    """
    Returns the maximum value among cells specified by a given set of conditions.
    
    Excel function: MAXIFS
    
    Args:
        max_range: Range of cells from which to return maximum
        *args: Alternating criteria_range and criteria pairs
    
    Returns:
        float: Maximum value meeting all criteria
    
    Raises:
        ValueError: If no values meet criteria or args not in pairs
    
    Cost:
        O(n * m) - where m is number of criteria
    
    Usage:
        >>> MAXIFS([10, 20, 30, 40], [1, 2, 3, 4], ">2")
        40
    """
    if len(args) % 2 != 0:
        raise ValueError("Criteria arguments must be in range/criteria pairs")

    if len(args) == 2:
        return float(_core_max_if(max_range, args[0], args[1]))

    # Multiple criteria pairs — intersect matches
    pairs = [(args[i], args[i + 1]) for i in range(0, len(args), 2)]
    valid = []

    for i in range(len(max_range)):

        if all(
            _meets_criteria(rng[i], crit)
            for rng, crit in pairs
            if i < len(rng)
        ):
            valid.append(max_range[i])

    if not valid:
        raise ValueError("No values meet the criteria")

    return float(max(valid))


# ============================================================================
# PROBABILITY DISTRIBUTIONS
# ============================================================================

def BETA_DIST(x: float, alpha: float, beta: float, cumulative: bool = True, 
              A: float = 0, B: float = 1) -> float:
    """
    Returns the beta probability distribution function.
    
    Excel function: BETA.DIST
    
    Args:
        x: Value between A and B at which to evaluate
        alpha: First parameter of the distribution (α > 0)
        beta: Second parameter of the distribution (β > 0)
        cumulative: If True, returns CDF; if False, returns PDF
        A: Lower bound of interval (default 0)
        B: Upper bound of interval (default 1)
    
    Returns:
        float: Beta distribution value
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> BETA_DIST(2, 8, 10, True, 1, 3)
        0.685...
    """
    if cumulative:
        return float(_get_scipy_stats().beta.cdf(x, alpha, beta, loc=A, scale=B-A))
    else:
        return float(_get_scipy_stats().beta.pdf(x, alpha, beta, loc=A, scale=B-A))


def BETA_INV(probability: float, alpha: float, beta: float, 
             A: float = 0, B: float = 1) -> float:
    """
    Returns the inverse of the beta cumulative distribution function.
    
    Excel function: BETA.INV
    
    Args:
        probability: Probability associated with the beta distribution
        alpha: First parameter of the distribution
        beta: Second parameter of the distribution
        A: Lower bound of interval (default 0)
        B: Upper bound of interval (default 1)
    
    Returns:
        float: Value for which the beta CDF equals probability
    
    Cost:
        O(1) - Constant time
    """
    return float(_get_scipy_stats().beta.ppf(probability, alpha, beta, loc=A, scale=B-A))


def BINOM_DIST(number_s: int, trials: int, probability_s: float, 
               cumulative: bool) -> float:
    """
    Returns the individual term binomial distribution probability.
    
    Excel function: BINOM.DIST
    
    Args:
        number_s: Number of successes in trials
        trials: Number of independent trials
        probability_s: Probability of success on each trial
        cumulative: If True, returns CDF; if False, returns PMF
    
    Returns:
        float: Binomial distribution probability
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> BINOM_DIST(6, 10, 0.5, False)
        0.205...
    """
    return _core_binom_dist(number_s, trials, probability_s, cumulative)


def BINOM_DIST_RANGE(trials: int, probability_s: float, 
                     number_s: int, number_s2: Optional[int] = None) -> float:
    """
    Returns the probability of a trial result using a binomial distribution.
    
    Excel function: BINOM.DIST.RANGE
    
    Args:
        trials: Number of independent trials
        probability_s: Probability of success on each trial
        number_s: Lower bound of successes
        number_s2: Upper bound of successes (if None, equals number_s)
    
    Returns:
        float: Probability of number_s to number_s2 successes
    
    Cost:
        O(k) - where k is the range size
    """
    return _core_binom_dist_range(trials, probability_s, number_s, number_s2)


def BINOM_INV(trials: int, probability_s: float, alpha: float) -> int:
    """
    Returns the smallest value for which the cumulative binomial distribution is >= criterion.
    
    Excel function: BINOM.INV
    
    Args:
        trials: Number of Bernoulli trials
        probability_s: Probability of success on each trial
        alpha: Criterion value
    
    Returns:
        int: Smallest number of successes
    
    Cost:
        O(1) - Constant time
    """
    return _core_binom_inv(trials, probability_s, alpha)


def CHISQ_DIST(x: float, deg_freedom: int, cumulative: bool = True) -> float:
    """
    Returns the chi-squared distribution.
    
    Excel function: CHISQ.DIST
    
    Args:
        x: Value at which to evaluate the distribution
        deg_freedom: Number of degrees of freedom
        cumulative: If True, returns CDF; if False, returns PDF
    
    Returns:
        float: Chi-squared distribution value
    
    Cost:
        O(1) - Constant time
    """
    return _core_chisq_dist(x, deg_freedom, cumulative)


def CHISQ_DIST_RT(x: float, deg_freedom: int) -> float:
    """
    Returns the right-tailed probability of the chi-squared distribution.
    
    Excel function: CHISQ.DIST.RT
    
    Args:
        x: Value at which to evaluate
        deg_freedom: Number of degrees of freedom
    
    Returns:
        float: Right-tailed probability
    
    Cost:
        O(1) - Constant time
    """
    return _core_chisq_dist_rt(x, deg_freedom)


def CHISQ_INV(probability: float, deg_freedom: int) -> float:
    """
    Returns the inverse of the left-tailed probability of the chi-squared distribution.
    
    Excel function: CHISQ.INV
    
    Args:
        probability: Probability associated with the chi-squared distribution
        deg_freedom: Number of degrees of freedom
    
    Returns:
        float: Inverse value
    
    Cost:
        O(1) - Constant time
    """
    return _core_chisq_inv(probability, deg_freedom)


def CHISQ_INV_RT(probability: float, deg_freedom: int) -> float:
    """
    Returns the inverse of the right-tailed probability of the chi-squared distribution.
    
    Excel function: CHISQ.INV.RT
    
    Args:
        probability: Probability associated with the chi-squared distribution
        deg_freedom: Number of degrees of freedom
    
    Returns:
        float: Inverse value
    
    Cost:
        O(1) - Constant time
    """
    return _core_chisq_inv_rt(probability, deg_freedom)


def EXPON_DIST(x: float, lambda_: float, cumulative: bool) -> float:
    """
    Returns the exponential distribution.
    
    Excel function: EXPON.DIST
    
    Args:
        x: Value at which to evaluate
        lambda_: Parameter value (rate parameter)
        cumulative: If True, returns CDF; if False, returns PDF
    
    Returns:
        float: Exponential distribution value
    
    Cost:
        O(1) - Constant time
    """
    return _core_expon_dist(x, lambda_, cumulative)


def F_DIST(x: float, deg_freedom1: int, deg_freedom2: int, cumulative: bool = True) -> float:
    """
    Returns the F probability distribution.
    
    Excel function: F.DIST
    
    Args:
        x: Value at which to evaluate
        deg_freedom1: Numerator degrees of freedom
        deg_freedom2: Denominator degrees of freedom
        cumulative: If True, returns CDF; if False, returns PDF
    
    Returns:
        float: F distribution value
    
    Cost:
        O(1) - Constant time
    """
    return _core_f_dist(x, deg_freedom1, deg_freedom2, cumulative)


def F_DIST_RT(x: float, deg_freedom1: int, deg_freedom2: int) -> float:
    """
    Returns the right-tailed F probability distribution.
    
    Excel function: F.DIST.RT
    
    Args:
        x: Value at which to evaluate
        deg_freedom1: Numerator degrees of freedom
        deg_freedom2: Denominator degrees of freedom
    
    Returns:
        float: Right-tailed probability
    
    Cost:
        O(1) - Constant time
    """
    return _core_f_dist_rt(x, deg_freedom1, deg_freedom2)


def F_INV(probability: float, deg_freedom1: int, deg_freedom2: int) -> float:
    """
    Returns the inverse of the F probability distribution.
    
    Excel function: F.INV
    
    Args:
        probability: Probability associated with the F distribution
        deg_freedom1: Numerator degrees of freedom
        deg_freedom2: Denominator degrees of freedom
    
    Returns:
        float: Inverse value
    
    Cost:
        O(1) - Constant time
    """
    return _core_f_inv(probability, deg_freedom1, deg_freedom2)


def F_INV_RT(probability: float, deg_freedom1: int, deg_freedom2: int) -> float:
    """
    Returns the inverse of the right-tailed F probability distribution.
    
    Excel function: F.INV.RT
    
    Args:
        probability: Probability associated with the F distribution
        deg_freedom1: Numerator degrees of freedom
        deg_freedom2: Denominator degrees of freedom
    
    Returns:
        float: Inverse value
    
    Cost:
        O(1) - Constant time
    """
    return _core_f_inv_rt(probability, deg_freedom1, deg_freedom2)


def GAMMA_DIST(x: float, alpha: float, beta: float, cumulative: bool) -> float:
    """
    Returns the gamma distribution.
    
    Excel function: GAMMA.DIST
    
    Args:
        x: Value at which to evaluate
        alpha: Shape parameter
        beta: Scale parameter
        cumulative: If True, returns CDF; if False, returns PDF
    
    Returns:
        float: Gamma distribution value
    
    Cost:
        O(1) - Constant time
    """
    return _core_gamma_dist(x, alpha, beta, cumulative)


def GAMMA_INV(probability: float, alpha: float, beta: float) -> float:
    """
    Returns the inverse of the gamma cumulative distribution.
    
    Excel function: GAMMA.INV
    
    Args:
        probability: Probability associated with the gamma distribution
        alpha: Shape parameter
        beta: Scale parameter
    
    Returns:
        float: Inverse value
    
    Cost:
        O(1) - Constant time
    """
    return _core_gamma_inv(probability, alpha, beta)


def HYPGEOM_DIST(sample_s: int, number_sample: int, population_s: int, 
                 number_pop: int, cumulative: bool) -> float:
    """
    Returns the hypergeometric distribution.
    
    Excel function: HYPGEOM.DIST
    
    Args:
        sample_s: Number of successes in the sample
        number_sample: Size of the sample
        population_s: Number of successes in the population
        number_pop: Population size
        cumulative: If True, returns CDF; if False, returns PMF
    
    Returns:
        float: Hypergeometric distribution value
    
    Cost:
        O(1) - Constant time
    """
    return _core_hypgeom_dist(sample_s, number_sample, population_s, number_pop, cumulative)


def LOGNORM_DIST(x: float, mean: float, standard_dev: float, cumulative: bool) -> float:
    """
    Returns the lognormal distribution.
    
    Excel function: LOGNORM.DIST
    
    Args:
        x: Value at which to evaluate
        mean: Mean of the natural logarithm
        standard_dev: Standard deviation of the natural logarithm
        cumulative: If True, returns CDF; if False, returns PDF
    
    Returns:
        float: Lognormal distribution value
    
    Cost:
        O(1) - Constant time
    """
    return _core_lognorm_dist(x, mean, standard_dev, cumulative)


def LOGNORM_INV(probability: float, mean: float, standard_dev: float) -> float:
    """
    Returns the inverse of the lognormal cumulative distribution.
    
    Excel function: LOGNORM.INV
    
    Args:
        probability: Probability associated with the lognormal distribution
        mean: Mean of the natural logarithm
        standard_dev: Standard deviation of the natural logarithm
    
    Returns:
        float: Inverse value
    
    Cost:
        O(1) - Constant time
    """
    return _core_lognorm_inv(probability, mean, standard_dev)


# ============================================================================
# REGRESSION AND TREND ANALYSIS
# ============================================================================

def LINEST(known_y: List[float], known_x: Optional[List[float]] = None, 
           const: bool = True, stats_flag: bool = False) -> Union[tuple, List[float]]:
    """
    Returns statistics for a linear trend.
    
    Excel function: LINEST
    
    Args:
        known_y: Set of known y-values
        known_x: Set of known x-values (defaults to 1, 2, 3, ...)
        const: If True, force constant term; if False, force through origin
        stats_flag: If True, return additional regression statistics
    
    Returns:
        tuple or List[float]: Slope and intercept, or extended statistics
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> LINEST([1, 9, 5, 7], [0, 4, 2, 3])
        (2.0, 1.0)
    """
    if known_x is None:
        known_x = list(range(1, len(known_y) + 1))
    if len(known_y) != len(known_x):
        raise ValueError("known_y and known_x must have equal length")
    
    if const:
        slope, intercept = _polyfit1(known_x, known_y)
    else:
        # Force through origin
        s_xy = sum(x * y for x, y in zip(known_x, known_y))
        s_xx = sum(x * x for x in known_x)
        slope = s_xy / s_xx
        intercept = 0.0

    if stats_flag:
        y_pred = [slope * x + intercept for x in known_x]
        ss_res = sum((y - yp) ** 2 for y, yp in zip(known_y, y_pred))
        ss_tot = sum((y - _core_mean(list(known_y))) ** 2 for y in known_y)
        r_squared = 1 - (ss_res / ss_tot) if ss_tot != 0 else 0
        return (slope, intercept, r_squared)

    return (slope, intercept)


def LOGEST(known_y: List[float], known_x: Optional[List[float]] = None, 
           const: bool = True, stats_flag: bool = False) -> Union[tuple, List[float]]:
    """
    Returns parameters of an exponential trend.
    
    Excel function: LOGEST
    
    Args:
        known_y: Set of known y-values
        known_x: Set of known x-values (defaults to 1, 2, 3, ...)
        const: If True, calculate b normally; if False, force b = 1
        stats_flag: If True, return additional regression statistics
    
    Returns:
        tuple: Base and multiplier for exponential curve
    
    Cost:
        O(n) - Linear time complexity
    """
    if known_x is None:
        known_x = list(range(1, len(known_y) + 1))
    if len(known_y) != len(known_x):
        raise ValueError("known_y and known_x must have equal length")
    
    log_y = [math.log(y) for y in known_y]

    if const:
        slope, intercept = _polyfit1(known_x, log_y)
        base = math.exp(slope)
        multiplier = math.exp(intercept)
    else:
        s_xy = sum(x * ly for x, ly in zip(known_x, log_y))
        s_xx = sum(x * x for x in known_x)
        slope_val = s_xy / s_xx
        base = math.exp(slope_val)
        multiplier = 1.0

    return (base, multiplier)


def INTERCEPT(known_y: List[float], known_x: Optional[List[float]] = None) -> float:
    """
    Returns the intercept of the linear regression line.
    
    Excel function: INTERCEPT
    
    Args:
        known_y: Set of known y-values
        known_x: Set of known x-values (defaults to 1, 2, 3, ...)
    
    Returns:
        float: Y-intercept value
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> INTERCEPT([2, 3, 9, 1, 8], [6, 5, 11, 7, 5])
        0.048...
    """
    return _core_intercept(known_y, known_x)


def SLOPE(known_y: List[float], known_x: Optional[List[float]] = None) -> float:
    """
    Returns the slope of the linear regression line.
    
    Excel function: SLOPE
    
    Args:
        known_y: Set of known y-values
        known_x: Set of known x-values (defaults to 1, 2, 3, ...)
    
    Returns:
        float: Slope value
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> SLOPE([2, 3, 9, 1, 8], [6, 5, 11, 7, 5])
        0.305...
    """
    return _core_slope(known_y, known_x)


# ============================================================================
# FORECASTING FUNCTIONS
# ============================================================================

def FORECAST_LINEAR(x: float, known_y: List[float], known_x: Optional[List[float]] = None) -> float:
    """
    Returns a value along a linear trend using linear regression.
    
    Excel function: FORECAST.LINEAR (also FORECAST in older Excel)
    
    Args:
        x: Data point for which to predict a value
        known_y: Set of known y-values
        known_x: Set of known x-values (defaults to 1, 2, 3, ...)
    
    Returns:
        float: Forecasted value
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> FORECAST_LINEAR(30, [6, 7, 9, 15, 21], [20, 28, 31, 38, 40])
        10.607...
    """
    return _core_forecast_linear(x, known_y, known_x)


def FORECAST_ETS(target_date: float, values: List[float], timeline: List[float], 
                 seasonality: Optional[int] = None, data_completion: int = 1, 
                 aggregation: int = 1) -> float:
    """
    Returns a forecasted value based on exponential smoothing (simplified).
    
    Excel function: FORECAST.ETS
    
    Note: This is a simplified implementation. Full ETS requires complex state space models.
    
    Args:
        target_date: Data point for which to predict
        values: Historical values
        timeline: Historical timeline
        seasonality: Seasonal period length (auto-detected if None)
        data_completion: How to handle missing data (1=interpolate, 0=zero)
        aggregation: How to aggregate duplicate times (1=average)
    
    Returns:
        float: Forecasted value
    
    Cost:
        O(n) - Linear time complexity
    """
    # Simplified: use linear trend if no obvious seasonality
    return float(_core_forecast_ets(
        target_date, values, timeline,
        seasonality if seasonality is not None else 1,
        data_completion, aggregation,
    ))


def FORECAST_ETS_CONFINT(target_date: float, values: List[float], timeline: List[float], 
                         confidence_level: float = 0.95, seasonality: Optional[int] = None, 
                         data_completion: int = 1, aggregation: int = 1) -> tuple:
    """
    Returns confidence interval for forecast (simplified).
    
    Excel function: FORECAST.ETS.CONFINT
    
    Args:
        target_date: Data point for which to predict
        values: Historical values
        timeline: Historical timeline
        confidence_level: Confidence level (default 0.95 for 95%)
        seasonality: Seasonal period length
        data_completion: How to handle missing data
        aggregation: How to aggregate duplicate times
    
    Returns:
        tuple: (lower_bound, upper_bound)
    
    Cost:
        O(n) - Linear time complexity
    """
    forecast = FORECAST_ETS(target_date, values, timeline, seasonality, data_completion, aggregation)
    std_err = _core_std_dev(list(values), sample=False) / math.sqrt(len(values))
    z = _get_scipy_stats().norm.ppf(1 - (1 - confidence_level) / 2)
    margin = z * std_err
    return (float(forecast - margin), float(forecast + margin))


def FORECAST_ETS_SEASONALITY(values: List[float], timeline: List[float], 
                             data_completion: int = 1, aggregation: int = 1) -> int:
    """
    Returns the detected seasonality length (simplified).
    
    Excel function: FORECAST.ETS.SEASONALITY
    
    Args:
        values: Historical values
        timeline: Historical timeline
        data_completion: How to handle missing data
        aggregation: How to aggregate duplicate times
    
    Returns:
        int: Detected seasonality period (simplified: returns 12 for monthly)
    
    Cost:
        O(n) - Linear time complexity
    """
    # Simplified: assume monthly seasonality
    return 12


def FORECAST_ETS_STAT(values: List[float], timeline: List[float], statistic_type: int, 
                      seasonality: Optional[int] = None, data_completion: int = 1, 
                      aggregation: int = 1) -> float:
    """
    Returns statistical value for ETS forecast (simplified).
    
    Excel function: FORECAST.ETS.STAT
    
    Args:
        values: Historical values
        timeline: Historical timeline
        statistic_type: Type of statistic to return (1=Alpha, 2=Beta, 3=Gamma, etc.)
        seasonality: Seasonal period length
        data_completion: How to handle missing data
        aggregation: How to aggregate duplicate times
    
    Returns:
        float: Requested statistic
    
    Cost:
        O(n) - Linear time complexity
    """
    # Simplified: return basic statistics
    if statistic_type == 1:  # Alpha (level smoothing)
        return 0.2
    elif statistic_type == 2:  # Beta (trend smoothing)
        return 0.1
    elif statistic_type == 3:  # Gamma (seasonal smoothing)
        return 0.1
    else:
        return 0.0


# ============================================================================
# STATISTICAL TESTS AND TRANSFORMATIONS
# ============================================================================

def FISHER(x: float) -> float:
    """
    Returns the Fisher transformation.
    
    Excel function: FISHER
    
    Args:
        x: Value for which to calculate the transformation (-1 < x < 1)
    
    Returns:
        float: Fisher transformation value
    
    Raises:
        ValueError: If x is not in valid range
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> FISHER(0.75)
        0.972...
    """
    return _core_fisher(x)


def FISHERINV(y: float) -> float:
    """
    Returns the inverse of the Fisher transformation.
    
    Excel function: FISHERINV
    
    Args:
        y: Value for which to perform the inverse transformation
    
    Returns:
        float: Inverse Fisher transformation value
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> FISHERINV(0.972)
        0.75...
    """
    return float(_core_fisher_inv(y))


def GAMMA(number: float) -> float:
    """
    Returns the gamma function value.
    
    Excel function: GAMMA
    
    Args:
        number: Value for which to calculate gamma
    
    Returns:
        float: Gamma function value
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> GAMMA(2.5)
        1.329...
    """
    return float(_core_gamma(number))


def GAMMALN(x: float) -> float:
    """
    Returns the natural logarithm of the gamma function.
    
    Excel function: GAMMALN
    
    Args:
        x: Value for which to calculate ln(gamma)
    
    Returns:
        float: Natural logarithm of gamma(x)
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> GAMMALN(4)
        1.791...
    """
    return float(_core_log_gamma(x))


def GAMMALN_PRECISE(x: float) -> float:
    """
    Returns the natural logarithm of the gamma function (precise version).
    
    Excel function: GAMMALN.PRECISE
    
    Args:
        x: Value for which to calculate ln(gamma)
    
    Returns:
        float: Natural logarithm of gamma(x)
    
    Cost:
        O(1) - Constant time
    """
    return GAMMALN(x)


def GAUSS(z: float) -> float:
    """
    Returns 0.5 less than the standard normal cumulative distribution.
    
    Excel function: GAUSS
    
    Args:
        z: Value for which to calculate
    
    Returns:
        float: P(0 < Z < z) for standard normal distribution
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> GAUSS(2)
        0.477...
    """
    return _core_gauss(z)


def FREQUENCY(data_array: List[float], bins_array: List[float]) -> List[int]:
    """
    Returns a frequency distribution as a vertical array.
    
    Excel function: FREQUENCY
    
    Args:
        data_array: Array of values for which to count frequencies
        bins_array: Array of intervals into which to group values
    
    Returns:
        List[int]: Frequency counts for each bin
    
    Cost:
        O(n log n) - Due to binning operation
    
    Usage:
        >>> FREQUENCY([79, 85, 78, 85, 50, 81, 95, 88, 97], [70, 79, 89])
        [1, 2, 4, 2]
    """
    return _core_frequency(list(data_array), list(bins_array))


def CONFIDENCE_NORM(alpha: float, standard_dev: float, size: int) -> float:
    """
    Returns the confidence interval for a population mean (normal distribution).
    
    Excel function: CONFIDENCE.NORM
    
    Args:
        alpha: Significance level (e.g., 0.05 for 95% confidence)
        standard_dev: Population standard deviation
        size: Sample size
    
    Returns:
        float: Confidence interval margin
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> CONFIDENCE_NORM(0.05, 2.5, 50)
        0.692...
    """
    return _core_confidence_norm(alpha, standard_dev, size)


def CONFIDENCE_T(alpha: float, standard_dev: float, size: int) -> float:
    """
    Returns the confidence interval for a population mean (t-distribution).
    
    Excel function: CONFIDENCE.T
    
    Args:
        alpha: Significance level (e.g., 0.05 for 95% confidence)
        standard_dev: Sample standard deviation
        size: Sample size
    
    Returns:
        float: Confidence interval margin
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> CONFIDENCE_T(0.05, 1, 50)
        0.284...
    """
    return _core_confidence_t(alpha, standard_dev, size)


# ============================================================================
# AVERAGE FUNCTIONS
# ============================================================================

def AVERAGE(*values: Union[float, int, List]) -> float:
    """
    Returns the average (arithmetic mean) of the arguments.
    
    Excel function: AVERAGE (PROMEDIO in Spanish)
    
    Description:
        Calculates the average of numbers provided as arguments. Ignores text,
        logical values, and empty cells. If a list is provided, it flattens it.
    
    Args:
        *values: Numbers or lists of numbers to average
    
    Returns:
        float: The arithmetic mean of the values
    
    Raises:
        ValueError: If no numeric values are provided
    
    Cost:
        O(n) - Linear time complexity where n is total number of elements
    
    Usage:
        >>> AVERAGE(10, 20, 30)
        20.0
        >>> AVERAGE([10, 20, 30])
        20.0
        >>> AVERAGE(10, 20, "text", 30)
        20.0
    """
    numeric_values = _extract_numerics(*values)

    if not numeric_values:
        raise ValueError("AVERAGE requires at least one numeric value")

    return _core_mean(numeric_values)


def AVERAGEA(*values: Union[float, int, str, bool, List]) -> float:
    """
    Returns the average of arguments, including numbers, text, and logical values.
    
    Excel function: AVERAGEA
    
    Description:
        Calculates the average including text and logical values. Text is treated
        as 0, TRUE as 1, FALSE as 0. Empty cells are ignored.
    
    Args:
        *values: Values to average (numbers, text, logical values, lists)
    
    Returns:
        float: The arithmetic mean of the values
    
    Raises:
        ValueError: If no values are provided
    
    Cost:
        O(n) - Linear time complexity where n is total number of elements
    
    Usage:
        >>> AVERAGEA(10, 20, 30)
        20.0
        >>> AVERAGEA(10, 20, True, False)
        7.75
        >>> AVERAGEA(10, "text", 20)
        10.0
    """
    converted_values = _convert_values_a(*values)

    if not converted_values:
        raise ValueError("AVERAGEA requires at least one value")

    return _core_mean(converted_values)


def AVERAGEIF(range_values: List, criteria, average_range: Optional[List] = None) -> float:
    """
    Returns the average of cells that meet a criterion.
    
    Excel function: AVERAGEIF (PROMEDIO.SI in Spanish)
    
    Description:
        Calculates the average of cells in a range that meet a specified criterion.
        Supports numeric comparisons (>, <, >=, <=, =, <>) and text matching.
    
    Args:
        range_values: Range to evaluate against criteria
        criteria: Condition to test (can be number, string with comparison, or text)
        average_range: Optional range to average (if different from range_values)
    
    Returns:
        float: Average of cells meeting the criterion
    
    Raises:
        ValueError: If no values meet the criterion or ranges have different lengths
    
    Cost:
        O(n) - Linear time complexity where n is length of range
    
    Usage:
        >>> AVERAGEIF([10, 20, 30, 40], ">20")
        35.0
        >>> AVERAGEIF(["apple", "banana", "apple"], "apple", [10, 20, 30])
        20.0
    """
    if average_range is None:
        average_range = range_values

    return _core_average_if(average_range, range_values, criteria)


def AVERAGEIFS(average_range: List, *criteria_pairs) -> float:
    """
    Returns the average of cells that meet multiple criteria.
    
    Excel function: AVERAGEIFS (PROMEDIO.SI.CONJUNTO in Spanish)
    
    Description:
        Calculates the average of cells that meet multiple criteria. Criteria are
        specified as pairs of (range, criterion).
    
    Args:
        average_range: Range to average
        *criteria_pairs: Pairs of (criteria_range, criterion) to test
    
    Returns:
        float: Average of cells meeting all criteria
    
    Raises:
        ValueError: If no values meet criteria, invalid pairs, or mismatched lengths
    
    Cost:
        O(n * m) - where n is range length and m is number of criteria
    
    Usage:
        >>> AVERAGEIFS([10, 20, 30], [5, 15, 25], ">10", [1, 2, 3], "<3")
        15.0
    """
    if len(criteria_pairs) % 2 != 0:
        raise ValueError("Criteria must be provided as pairs of (range, criterion)")

    if len(criteria_pairs) == 2:
        return _core_average_if(average_range, criteria_pairs[0], criteria_pairs[1])

    # Multiple criteria pairs — intersect matches
    criteria_list = []

    for i in range(0, len(criteria_pairs), 2):
        criteria_range = criteria_pairs[i]
        criterion = criteria_pairs[i + 1]

        if len(criteria_range) != len(average_range):
            raise ValueError("All ranges must have the same length")

        criteria_list.append((criteria_range, criterion))

    from agentfx.fxNumeric.statistics_functions import _parse_criteria

    preds = [_parse_criteria(crit) for _, crit in criteria_list]
    values_to_average = []

    for i in range(len(average_range)):

        if not isinstance(average_range[i], (int, float)):
            continue

        if all(pred(criteria_list[j][0][i]) for j, pred in enumerate(preds)):
            values_to_average.append(average_range[i])

    if not values_to_average:
        raise ValueError("No values meet all criteria")

    return sum(values_to_average) / len(values_to_average)


# ============================================================================
# MIN/MAX FUNCTIONS
# ============================================================================

def MIN(*values: Union[float, int, List]) -> float:
    """
    Returns the minimum value from a set of values.
    
    Excel function: MIN
    
    Description:
        Returns the smallest number in a set of values. Ignores text and
        logical values.
    
    Args:
        *values: Numbers or lists of numbers
    
    Returns:
        float: The minimum value
    
    Raises:
        ValueError: If no numeric values are provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> MIN(10, 20, 5, 30)
        5
        >>> MIN([10, 20, 5, 30])
        5
    """
    numeric_values = _extract_numerics(*values)

    if not numeric_values:
        raise ValueError("MIN requires at least one numeric value")

    return min(numeric_values)


def MINA(*values: Union[float, int, str, bool, List]) -> float:
    """
    Returns the minimum value, including numbers, text, and logical values.
    
    Excel function: MINA
    
    Description:
        Returns the smallest value treating text as 0, TRUE as 1, FALSE as 0.
    
    Args:
        *values: Values to evaluate
    
    Returns:
        float: The minimum value
    
    Raises:
        ValueError: If no values are provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> MINA(10, 20, True, False)
        0
        >>> MINA(10, "text", 20)
        0
    """
    converted_values = []
    
    for val in values:
        if isinstance(val, (list, tuple)):
            for v in val:
                if v is None or v == "":
                    continue
                elif isinstance(v, bool):
                    converted_values.append(1 if v else 0)
                elif isinstance(v, str):
                    converted_values.append(0)
                elif isinstance(v, (int, float)):
                    converted_values.append(v)
        else:
            if val is None or val == "":
                continue
            elif isinstance(val, bool):
                converted_values.append(1 if val else 0)
            elif isinstance(val, str):
                converted_values.append(0)
            elif isinstance(val, (int, float)):
                converted_values.append(val)
    
    if not converted_values:
        raise ValueError("MINA requires at least one value")
    
    return min(converted_values)


def MINIFS(min_range: List, *criteria_pairs) -> float:
    """
    Returns the minimum value among cells specified by a set of conditions.
    
    Excel function: MINIFS (MIN.SI.CONJUNTO in Spanish)
    
    Description:
        Returns the minimum value from cells that meet multiple criteria.
    
    Args:
        min_range: Range to find minimum from
        *criteria_pairs: Pairs of (criteria_range, criterion)
    
    Returns:
        float: Minimum value meeting all criteria
    
    Raises:
        ValueError: If no values meet criteria or invalid arguments
    
    Cost:
        O(n * m) - where n is range length and m is number of criteria
    
    Usage:
        >>> MINIFS([10, 20, 30], [5, 15, 25], ">10")
        20
    """
    if len(criteria_pairs) % 2 != 0:
        raise ValueError("Criteria must be provided as pairs of (range, criterion)")

    if len(criteria_pairs) == 2:
        return float(_core_min_if(min_range, criteria_pairs[0], criteria_pairs[1]))

    # Multiple criteria pairs
    criteria_list = []

    for i in range(0, len(criteria_pairs), 2):
        criteria_range = criteria_pairs[i]
        criterion = criteria_pairs[i + 1]

        if len(criteria_range) != len(min_range):
            raise ValueError("All ranges must have the same length")

        criteria_list.append((criteria_range, criterion))

    values_to_check = []

    for i in range(len(min_range)):

        if not isinstance(min_range[i], (int, float)):
            continue

        if all(_meets_criteria(cr[i], crit) for cr, crit in criteria_list):
            values_to_check.append(min_range[i])

    if not values_to_check:
        raise ValueError("No values meet all criteria")

    return min(values_to_check)


def MEDIAN(*values: Union[float, int, List]) -> float:
    """
    Returns the median (middle value) of the given numbers.
    
    Excel function: MEDIAN (MEDIANA in Spanish)
    
    Description:
        Returns the median, the number in the middle of a set of numbers.
        If there is an even number of values, returns the average of the two middle values.
    
    Args:
        *values: Numbers or lists of numbers
    
    Returns:
        float: The median value
    
    Raises:
        ValueError: If no numeric values are provided
    
    Cost:
        O(n log n) - Due to sorting
    
    Usage:
        >>> MEDIAN(1, 2, 3, 4, 5)
        3.0
        >>> MEDIAN(1, 2, 3, 4)
        2.5
    """
    numeric_values = _extract_numerics(*values)

    if not numeric_values:
        raise ValueError("MEDIAN requires at least one numeric value")

    return float(_core_median(numeric_values))


# ============================================================================
# MODE FUNCTIONS
# ============================================================================

def MODE_MULT(values: List[Union[float, int]]) -> List[float]:
    """
    Returns a vertical array of the most frequently occurring values in a range.
    
    Excel function: MODE.MULT (MODA.VARIOS in Spanish)
    
    Description:
        Returns an array of the most frequently occurring, or repetitive values
        in an array or range of data.
    
    Args:
        values: List of numeric values
    
    Returns:
        List[float]: List of most frequent values
    
    Raises:
        ValueError: If no numeric values or no repeated values
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> MODE_MULT([1, 2, 3, 3, 4, 4, 5])
        [3.0, 4.0]
    """
    numeric_values = [v for v in values if isinstance(v, (int, float)) and not isinstance(v, bool)]
    result = _core_mode_mult(numeric_values)
    return [float(v) for v in result]


def MODE_SNGL(values: List[Union[float, int]]) -> float:
    """
    Returns the most common value in a data set.
    
    Excel function: MODE.SNGL (MODA.UNO in Spanish) / MODE
    
    Description:
        Returns the most frequently occurring value in a range or array of data.
        If multiple values have the same frequency, returns the first one found.
    
    Args:
        values: List of numeric values
    
    Returns:
        float: The most frequent value
    
    Raises:
        ValueError: If no numeric values or no repeated values
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> MODE_SNGL([1, 2, 3, 3, 4])
        3.0
    """
    numeric_values = [v for v in values if isinstance(v, (int, float)) and not isinstance(v, bool)]

    if not numeric_values:
        raise ValueError("MODE.SNGL requires at least one numeric value")

    return _core_mode_single(numeric_values)


# ============================================================================
# STATISTICAL TESTS
# ============================================================================

def CHISQ_TEST(actual_range: List[Union[float, int]], expected_range: List[Union[float, int]]) -> float:
    """
    Returns the test for independence (chi-squared test).
    
    Excel function: CHISQ.TEST (PRUEBA.CHICUAD in Spanish)
    
    Description:
        Returns the value from the chi-squared distribution for the statistic
        and the appropriate degrees of freedom. Used to determine whether a
        hypothesis is confirmed by an experiment.
    
    Args:
        actual_range: Range of observed data
        expected_range: Range of expected values
    
    Returns:
        float: P-value from chi-squared test
    
    Raises:
        ValueError: If ranges have different lengths or invalid values
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> CHISQ_TEST([58, 35], [45.35, 47.65])
        0.000308...
    """
    if len(actual_range) != len(expected_range):
        raise ValueError("Actual and expected ranges must have the same length")
    
    actual = [float(v) for v in actual_range if isinstance(v, (int, float))]
    expected = [float(v) for v in expected_range if isinstance(v, (int, float))]
    
    if len(actual) < 2 or len(expected) < 2:
        raise ValueError("At least 2 values required in each range")
    
    if any(e <= 0 for e in expected):
        raise ValueError("Expected values must be positive")
    
    # Calculate chi-squared statistic
    chi2_stat = sum((a - e) ** 2 / e for a, e in zip(actual, expected))
    
    # Degrees of freedom
    df = len(actual) - 1
    
    # Return p-value
    return float(1 - _get_scipy_stats().chi2.cdf(chi2_stat, df))


def F_TEST(array1: List[Union[float, int]], array2: List[Union[float, int]]) -> float:
    """
    Returns the result of an F-test.
    
    Excel function: F.TEST (PRUEBA.F.N in Spanish)
    
    Description:
        Returns the two-tailed probability that the variances in array1 and
        array2 are not significantly different. Used to determine whether two
        samples have different variances.
    
    Args:
        array1: First array of data
        array2: Second array of data
    
    Returns:
        float: Two-tailed P-value
    
    Raises:
        ValueError: If arrays don't have enough values
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> F_TEST([6, 7, 9, 15, 21], [20, 28, 31, 38, 40])
        0.648...
    """
    arr1 = [float(v) for v in array1 if isinstance(v, (int, float)) and not isinstance(v, bool)]
    arr2 = [float(v) for v in array2 if isinstance(v, (int, float)) and not isinstance(v, bool)]
    
    if len(arr1) < 2 or len(arr2) < 2:
        raise ValueError("Each array must contain at least 2 values")
    
    # Calculate variances
    var1 = _core_variance(arr1, sample=True)
    var2 = _core_variance(arr2, sample=True)
    
    # F statistic (larger variance / smaller variance)
    if var1 >= var2:
        f_stat = var1 / var2
        df1 = len(arr1) - 1
        df2 = len(arr2) - 1
    else:
        f_stat = var2 / var1
        df1 = len(arr2) - 1
        df2 = len(arr1) - 1
    
    # Two-tailed p-value
    _st = _get_scipy_stats()
    p_value = 2 * min(_st.f.cdf(f_stat, df1, df2), 1 - _st.f.cdf(f_stat, df1, df2))
    
    return float(p_value)


def T_TEST(array1: List[Union[float, int]], array2: List[Union[float, int]], 
           tails: int = 2, test_type: int = 1) -> float:
    """
    Returns the probability associated with a Student's t-Test.
    
    Excel function: T.TEST (PRUEBA.T.N in Spanish)
    
    Description:
        Returns the p-value for a t-test. Used to determine whether two samples
        are likely to have come from the same two underlying populations.
    
    Args:
        array1: First data set
        array2: Second data set
        tails: Number of distribution tails (1 or 2)
        test_type: Type of t-test (1=paired, 2=two-sample equal variance, 
                   3=two-sample unequal variance)
    
    Returns:
        float: P-value from t-test
    
    Raises:
        ValueError: If invalid parameters
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> T_TEST([3, 4, 5, 8, 9], [6, 19, 3, 2, 14], tails=2, test_type=1)
        0.196...
    """
    arr1 = [float(v) for v in array1 if isinstance(v, (int, float)) and not isinstance(v, bool)]
    arr2 = [float(v) for v in array2 if isinstance(v, (int, float)) and not isinstance(v, bool)]

    if tails not in [1, 2]:
        raise ValueError("Tails must be 1 or 2")

    if test_type not in [1, 2, 3]:
        raise ValueError("Test type must be 1, 2, or 3")

    if len(arr1) < 2 or len(arr2) < 2:
        raise ValueError("Each array must contain at least 2 values")

    return float(_core_t_test(arr1, arr2, tails, test_type))


def Z_TEST(array: List[Union[float, int]], x: float, sigma: Optional[float] = None) -> float:
    """
    Returns the one-tailed P-value of a z-test.
    
    Excel function: Z.TEST (PRUEBA.Z.N in Spanish)
    
    Description:
        Returns the one-tailed P-value of a z-test. For a given hypothesized
        population mean, returns the probability that the sample mean would be
        greater than the average of observations in the data set.
    
    Args:
        array: Array of data to test
        x: Value to test
        sigma: Optional population standard deviation (if None, uses sample std dev)
    
    Returns:
        float: One-tailed P-value
    
    Raises:
        ValueError: If array has less than 2 values
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> Z_TEST([3, 6, 7, 8, 6, 5, 4, 2, 1, 9], 4)
        0.863...
    """
    arr = [float(v) for v in array if isinstance(v, (int, float)) and not isinstance(v, bool)]
    
    if len(arr) < 2:
        raise ValueError("Array must contain at least 2 values")
    
    mean = _core_mean(arr)

    if sigma is None:
        sigma = _core_std_dev(arr, sample=True)

    # Calculate z-score
    z = (mean - x) / (sigma / math.sqrt(len(arr)))
    
    # One-tailed p-value
    p_value = 1 - _get_scipy_stats().norm.cdf(z)
    
    return float(p_value)


# ============================================================================
# DISTRIBUTION FUNCTIONS - NEGATIVE BINOMIAL
# ============================================================================

def NEGBINOM_DIST(number_f: int, number_s: int, probability_s: float, cumulative: bool = False) -> float:
    """
    Returns the negative binomial distribution.
    
    Excel function: NEGBINOM.DIST
    
    Description:
        Returns the negative binomial distribution, the probability that there
        will be number_f failures before the number_s-th success, when the
        constant probability of a success is probability_s.
    
    Args:
        number_f: Number of failures
        number_s: Threshold number of successes
        probability_s: Probability of a success
        cumulative: If True, returns cumulative distribution function
    
    Returns:
        float: Negative binomial probability
    
    Raises:
        ValueError: If parameters are out of valid range
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> NEGBINOM_DIST(10, 5, 0.25)
        0.055...
    """
    return _core_negbinom_dist(number_f, number_s, probability_s, cumulative)


# ============================================================================
# DISTRIBUTION FUNCTIONS - NORMAL
# ============================================================================

def NORM_DIST(x: float, mean: float, standard_dev: float, cumulative: bool = False) -> float:
    """
    Returns the normal cumulative distribution.
    
    Excel function: NORM.DIST (DISTR.NORM.N in Spanish)
    
    Description:
        Returns the normal distribution for the specified mean and standard
        deviation. Can return either cumulative distribution or probability density.
    
    Args:
        x: Value for which to calculate the distribution
        mean: Arithmetic mean of the distribution
        standard_dev: Standard deviation of the distribution
        cumulative: If True, returns CDF; if False, returns PDF
    
    Returns:
        float: Normal distribution value
    
    Raises:
        ValueError: If standard_dev <= 0
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> NORM_DIST(42, 40, 1.5, True)
        0.908...
    """
    if standard_dev <= 0:
        raise ValueError("Standard deviation must be positive")

    return float(_core_norm_dist(x, mean, standard_dev, cumulative))


def NORM_INV(probability: float, mean: float, standard_dev: float) -> float:
    """
    Returns the inverse of the normal cumulative distribution.
    
    Excel function: NORM.INV (DISTR.NORM.INV in Spanish)
    
    Description:
        Returns the inverse of the normal cumulative distribution for the
        specified mean and standard deviation.
    
    Args:
        probability: Probability corresponding to the normal distribution
        mean: Arithmetic mean of the distribution
        standard_dev: Standard deviation of the distribution
    
    Returns:
        float: Value for which the cumulative distribution equals probability
    
    Raises:
        ValueError: If probability not in (0,1) or standard_dev <= 0
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> NORM_INV(0.908789, 40, 1.5)
        42.000...
    """
    if probability <= 0 or probability >= 1:
        raise ValueError("Probability must be between 0 and 1 (exclusive)")

    if standard_dev <= 0:
        raise ValueError("Standard deviation must be positive")

    return float(_core_norm_inv(probability, mean, standard_dev))


def NORM_S_DIST(z: float, cumulative: bool = False) -> float:
    """
    Returns the standard normal cumulative distribution.
    
    Excel function: NORM.S.DIST (DISTR.NORM.ESTAND.N in Spanish)
    
    Description:
        Returns the standard normal distribution (mean=0, std dev=1).
    
    Args:
        z: Value for which to calculate the distribution
        cumulative: If True, returns CDF; if False, returns PDF
    
    Returns:
        float: Standard normal distribution value
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> NORM_S_DIST(1.333333)
        0.181...
    """
    return _core_norm_s_dist(z, cumulative)


def NORM_S_INV(probability: float) -> float:
    """
    Returns the inverse of the standard normal cumulative distribution.
    
    Excel function: NORM.S.INV (INV.NORM.ESTAND in Spanish)
    
    Description:
        Returns the inverse of the standard normal cumulative distribution.
        The distribution has a mean of zero and a standard deviation of one.
    
    Args:
        probability: Probability corresponding to the normal distribution
    
    Returns:
        float: Z-value for which the cumulative distribution equals probability
    
    Raises:
        ValueError: If probability not in (0,1)
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> NORM_S_INV(0.908789)
        1.333...
    """
    return _core_norm_s_inv(probability)


# ============================================================================
# PERCENTILE AND QUARTILE FUNCTIONS
# ============================================================================

def PERCENTILE_EXC(array: List[Union[float, int]], k: float) -> float:
    """
    Returns the k-th percentile of values (k in range 0..1, exclusive).
    
    Excel function: PERCENTILE.EXC (PERCENTIL.EXC in Spanish)
    
    Description:
        Returns the k-th percentile of values in a range, where k is in the
        range 0..1, exclusive.
    
    Args:
        array: Array or range of data
        k: Percentile value in the range 0..1 (exclusive)
    
    Returns:
        float: The k-th percentile
    
    Raises:
        ValueError: If k not in valid range or array too small
    
    Cost:
        O(n log n) - Due to sorting
    
    Usage:
        >>> PERCENTILE_EXC([1, 2, 3, 4], 0.25)
        1.25
    """
    arr = sorted([float(v) for v in array if isinstance(v, (int, float)) and not isinstance(v, bool)])
    
    if not arr:
        raise ValueError("Array must contain at least one numeric value")
    
    if k <= 0 or k >= 1:
        raise ValueError("k must be between 0 and 1 (exclusive)")
    
    n = len(arr)
    
    # Excel's PERCENTILE.EXC uses (n+1)*k formula
    if k < 1/(n+1) or k > n/(n+1):
        raise ValueError(f"k must be between {1/(n+1)} and {n/(n+1)}")

    return float(_core_percentile_exc(arr, k))


def PERCENTILE_INC(array: List[Union[float, int]], k: float) -> float:
    """
    Returns the k-th percentile of values in a range.
    
    Excel function: PERCENTILE.INC (PERCENTIL.INC in Spanish) / PERCENTILE
    
    Description:
        Returns the k-th percentile of values in a range, where k is in the
        range 0..1, inclusive.
    
    Args:
        array: Array or range of data
        k: Percentile value in the range 0..1 (inclusive)
    
    Returns:
        float: The k-th percentile
    
    Raises:
        ValueError: If k not in valid range or array empty
    
    Cost:
        O(n log n) - Due to sorting
    
    Usage:
        >>> PERCENTILE_INC([1, 2, 3, 4], 0.3)
        1.9
    """
    arr = sorted([float(v) for v in array if isinstance(v, (int, float)) and not isinstance(v, bool)])
    
    if not arr:
        raise ValueError("Array must contain at least one numeric value")
    
    if k < 0 or k > 1:
        raise ValueError("k must be between 0 and 1 (inclusive)")
    
    return float(_core_percentile(arr, k * 100))


def QUARTILE_EXC(
    array: List[Union[float, int]],
    quart: int,
) -> float:
    """Returns the quartile of a data set (exclusive of 0 and 4).

    Excel function: QUARTILE.EXC (CUARTIL.EXC in Spanish)

    Args:
        array: Array or range of numeric data.
        quart: Quartile to return (1, 2, or 3).

    Returns:
        float: The requested quartile value.

    Raises:
        ValueError: If *quart* is not 1, 2, or 3, or array is empty.

    Usage Example:
        >>> QUARTILE_EXC([1, 2, 3, 4, 5, 6, 7, 8], 1)
        2.25

    Cost: O(n log n)
    """
    if quart not in (1, 2, 3):
        raise ValueError("quart must be 1, 2, or 3 for QUARTILE.EXC.")

    k = quart / 4.0
    return PERCENTILE_EXC(array, k)


def QUARTILE_INC(
    array: List[Union[float, int]],
    quart: int,
) -> float:
    """Returns the quartile of a data set (inclusive of 0 and 4).

    Excel function: QUARTILE.INC (CUARTIL.INC in Spanish) / QUARTILE

    Args:
        array: Array or range of numeric data.
        quart: Quartile to return (0 = min, 1 = Q1, 2 = median, 3 = Q3, 4 = max).

    Returns:
        float: The requested quartile value.

    Raises:
        ValueError: If *quart* is not in 0..4, or array is empty.

    Usage Example:
        >>> QUARTILE_INC([1, 2, 3, 4], 2)
        2.5

    Cost: O(n log n)
    """
    if quart not in (0, 1, 2, 3, 4):
        raise ValueError("quart must be between 0 and 4 for QUARTILE.INC.")

    k = quart / 4.0
    return PERCENTILE_INC(array, k)


def PERCENTRANK_EXC(array: List[Union[float, int]], x: float, significance: int = 3) -> float:
    """
    Returns the rank of a value as a percentage (0..1, exclusive).
    
    Excel function: PERCENTRANK.EXC (RANGO.PERCENTIL.EXC in Spanish)
    
    Description:
        Returns the rank of a value in a data set as a percentage of the data
        set, exclusive of 0 and 1.
    
    Args:
        array: Array of data
        x: Value for which to find the rank
        significance: Number of significant digits (default 3)
    
    Returns:
        float: Percentile rank
    
    Raises:
        ValueError: If array is empty or x outside range
    
    Cost:
        O(n log n) - Due to sorting
    
    Usage:
        >>> PERCENTRANK_EXC([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)
        0.667
    """
    arr = sorted([float(v) for v in array if isinstance(v, (int, float)) and not isinstance(v, bool)])

    if not arr:
        raise ValueError("Array must contain at least one numeric value")

    if x < arr[0] or x > arr[-1]:
        raise ValueError("x must be within the range of array values")

    return _core_percentrank_exc(arr, x, significance)


def PERCENTRANK_INC(array: List[Union[float, int]], x: float, significance: int = 3) -> float:
    """
    Returns the percentage rank of a value in a data set.
    
    Excel function: PERCENTRANK.INC (RANGO.PERCENTIL.INC in Spanish) / PERCENTRANK
    
    Description:
        Returns the rank of a value in a data set as a percentage of the data
        set, inclusive of 0 and 1.
    
    Args:
        array: Array of data
        x: Value for which to find the rank
        significance: Number of significant digits (default 3)
    
    Returns:
        float: Percentile rank
    
    Raises:
        ValueError: If array is empty or x outside range
    
    Cost:
        O(n log n) - Due to sorting
    
    Usage:
        >>> PERCENTRANK_INC([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 7)
        0.667
    """
    arr = sorted([float(v) for v in array if isinstance(v, (int, float)) and not isinstance(v, bool)])
    
    if not arr:
        raise ValueError("Array must contain at least one numeric value")
    
    if x < arr[0] or x > arr[-1]:
        raise ValueError("x must be within the range of array values")
    
    n = len(arr)
    
    # Find position
    if x == arr[0]:
        rank = 0.0
    elif x == arr[-1]:
        rank = 1.0
    else:
        # Linear interpolation
        for i in range(len(arr) - 1):
            if arr[i] <= x <= arr[i + 1]:
                if arr[i] == arr[i + 1]:
                    rank = i / (n - 1)
                else:
                    rank = (i + (x - arr[i]) / (arr[i + 1] - arr[i])) / (n - 1)
                break
    
    return round(rank, significance)


# ============================================================================
# PERMUTATION AND COMBINATION FUNCTIONS
# ============================================================================

def PERMUT(number: int, number_chosen: int) -> int:
    """
    Returns the number of permutations for a given number of objects.
    
    Excel function: PERMUT (PERMUTACIONES in Spanish)
    
    Description:
        Returns the number of permutations for a given number of items that can
        be selected from the total objects. A permutation is any set or subset
        of objects where internal order is significant.
    
    Args:
        number: Total number of items
        number_chosen: Number of items in each permutation
    
    Returns:
        int: Number of permutations
    
    Raises:
        ValueError: If parameters are invalid
    
    Cost:
        O(k) - where k is number_chosen
    
    Usage:
        >>> PERMUT(100, 3)
        970200
    """
    return _core_permutations(number, number_chosen)


def PERMUTATIONA(number: int, number_chosen: int) -> int:
    """
    Returns the number of permutations with repetition.
    
    Excel function: PERMUTATIONA (PERMUTACIONES.A in Spanish)
    
    Description:
        Returns the number of permutations for a given number of objects (with
        repetitions) that can be selected from the total objects.
    
    Args:
        number: Total number of items
        number_chosen: Number of items in each permutation
    
    Returns:
        int: Number of permutations with repetition
    
    Raises:
        ValueError: If parameters are invalid
    
    Cost:
        O(k) - where k is number_chosen
    
    Usage:
        >>> PERMUTATIONA(3, 2)
        9
    """
    if number < 0 or number_chosen < 0:
        raise ValueError("Arguments must be non-negative")

    return _core_permutationa(number, number_chosen)


# ============================================================================
# DISTRIBUTION FUNCTIONS - PHI AND POISSON
# ============================================================================

def PHI(x: float) -> float:
    """
    Returns the value of the density function for a standard normal distribution.
    
    Excel function: PHI (FI in Spanish)
    
    Description:
        Returns the value of the probability density function for a standard
        normal distribution for a specified value.
    
    Args:
        x: The value for which you want the density of the standard normal distribution
    
    Returns:
        float: Density value
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> PHI(0.75)
        0.301...
    """
    return _core_phi(x)


def POISSON_DIST(x: int, mean: float, cumulative: bool = False) -> float:
    """
    Returns the Poisson distribution.
    
    Excel function: POISSON.DIST (POISSON.DIST in Spanish)
    
    Description:
        Returns the Poisson distribution. A common application is predicting the
        number of events over a specific time, such as the number of cars arriving
        at a toll plaza in 1 minute.
    
    Args:
        x: Number of events
        mean: Expected numeric value (lambda)
        cumulative: If True, returns cumulative distribution function
    
    Returns:
        float: Poisson probability
    
    Raises:
        ValueError: If x < 0 or mean <= 0
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> POISSON_DIST(2, 5, False)
        0.084...
    """
    return _core_poisson_dist(x, mean, cumulative)


# ============================================================================
# SKEWNESS AND KURTOSIS
# ============================================================================

def SKEW(*values: Union[float, int, List]) -> float:
    """
    Returns the skewness of a distribution.
    
    Excel function: SKEW (COEFICIENTE.ASIMETRIA in Spanish)
    
    Description:
        Returns the skewness of a distribution. Skewness characterizes the degree
        of asymmetry of a distribution around its mean. Positive skewness indicates
        a distribution with an asymmetric tail extending toward more positive values.
    
    Args:
        *values: Numbers or lists for which you want to calculate skewness
    
    Returns:
        float: Skewness value
    
    Raises:
        ValueError: If less than 3 values provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> SKEW(3, 4, 5, 2, 3, 4, 5, 6, 4, 7)
        0.359...
    """
    numeric_values = _extract_numerics(*values)

    if len(numeric_values) < 3:
        raise ValueError("SKEW requires at least 3 values")

    return float(_get_scipy_stats().skew(numeric_values, bias=False))


def SKEW_P(*values: Union[float, int, List]) -> float:
    """
    Returns the skewness of a distribution based on a population.

    Excel function: SKEW.P (COEFICIENTE.ASIMETRIA.P in Spanish)

    Description:
        Returns the skewness of a distribution based on a population:
        a characterization of the degree of asymmetry of a distribution
        around its mean.

    Args:
        *values: Numbers or lists for which you want to calculate population skewness

    Returns:
        float: Population skewness value

    Raises:
        ValueError: If less than 3 values provided

    Cost:
        O(n) - Linear time complexity

    Usage:
        >>> SKEW_P(3, 4, 5, 2, 3, 4, 5, 6, 4, 7)
        0.303...
    """
    numeric_values = _extract_numerics(*values)

    if len(numeric_values) < 3:
        raise ValueError("SKEW.P requires at least 3 values")

    return float(_get_scipy_stats().skew(numeric_values, bias=True))


# ============================================================================
# RANK AND PERCENTILE FUNCTIONS
# ============================================================================

def SMALL(array: List[Union[float, int]], k: int) -> float:
    """
    Returns the k-th smallest value in a data set.
    
    Excel function: SMALL (K.ESIMO.MENOR in Spanish)
    
    Description:
        Returns the k-th smallest value in a data set. Use this function to
        return values with a particular relative standing in a data set.
    
    Args:
        array: Array or range of numerical data
        k: Position (from the smallest value) in the array or range
    
    Returns:
        float: The k-th smallest value
    
    Raises:
        ValueError: If k is invalid or array is empty
    
    Cost:
        O(n log n) - Due to sorting
    
    Usage:
        >>> SMALL([3, 4, 5, 2, 3, 4, 6, 4, 7], 4)
        4
    """
    numeric_values = [v for v in array if isinstance(v, (int, float)) and not isinstance(v, bool)]
    return float(_core_small(numeric_values, k))


def STANDARDIZE(x: float, mean: float, standard_dev: float) -> float:
    """
    Returns a normalized value from a distribution.
    
    Excel function: STANDARDIZE (NORMALIZACION in Spanish)
    
    Description:
        Returns a normalized value from a distribution characterized by a mean
        and standard deviation.
    
    Args:
        x: Value to normalize
        mean: Arithmetic mean of the distribution
        standard_dev: Standard deviation of the distribution
    
    Returns:
        float: Normalized value (z-score)
    
    Raises:
        ValueError: If standard_dev <= 0
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> STANDARDIZE(42, 40, 1.5)
        1.333...
    """
    return _core_standardize(x, mean, standard_dev)


# ============================================================================
# STANDARD DEVIATION AND VARIANCE FUNCTIONS
# ============================================================================

def STDEV_P(*values: Union[float, int, List]) -> float:
    """
    Calculates standard deviation based on the entire population.
    
    Excel function: STDEV.P (DESVEST.P in Spanish)
    
    Description:
        Calculates standard deviation based on the entire population given as
        arguments. Ignores logical values and text.
    
    Args:
        *values: Numbers or lists representing the population
    
    Returns:
        float: Population standard deviation
    
    Raises:
        ValueError: If less than 1 value provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> STDEV_P(1345, 1301, 1368, 1322, 1310, 1370, 1318, 1350, 1303, 1299)
        27.46...
    """
    numeric_values = _extract_numerics(*values)

    if len(numeric_values) < 1:
        raise ValueError("STDEV.P requires at least one value")

    return _core_std_dev(numeric_values, sample=False)


def STDEV_S(*values: Union[float, int, List]) -> float:
    """
    Estimates standard deviation based on a sample.
    
    Excel function: STDEV.S (DESVEST.M in Spanish) / STDEV
    
    Description:
        Estimates standard deviation based on a sample. The standard deviation is
        a measure of how widely values are dispersed from the average value (the mean).
    
    Args:
        *values: Numbers or lists representing a sample of a population
    
    Returns:
        float: Sample standard deviation
    
    Raises:
        ValueError: If less than 2 values provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> STDEV_S(1345, 1301, 1368, 1322, 1310, 1370, 1318, 1350, 1303, 1299)
        29.05...
    """
    numeric_values = _extract_numerics(*values)

    if len(numeric_values) < 2:
        raise ValueError("STDEV.S requires at least 2 values")

    return _core_std_dev(numeric_values, sample=True)


def STDEVA(*values: Union[float, int, str, bool, List]) -> float:
    """
    Estimates standard deviation based on a sample, including text and logical values.
    
    Excel function: STDEVA (DESVESTA in Spanish)
    
    Description:
        Estimates standard deviation based on a sample. Text and FALSE evaluate to 0;
        TRUE evaluates to 1.
    
    Args:
        *values: Values to include in the sample
    
    Returns:
        float: Sample standard deviation
    
    Raises:
        ValueError: If less than 2 values provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> STDEVA(1345, 1301, 1368, True, False, "test")
        623.79...
    """
    converted_values = _convert_values_a(*values)

    if len(converted_values) < 2:
        raise ValueError("STDEVA requires at least 2 values")

    return _core_std_dev(converted_values, sample=True)


def STDEVPA(*values: Union[float, int, str, bool, List]) -> float:
    """
    Calculates standard deviation based on population, including text and logical values.
    
    Excel function: STDEVPA (DESVESTPA in Spanish)
    
    Description:
        Calculates standard deviation based on the entire population. Text and
        FALSE evaluate to 0; TRUE evaluates to 1.
    
    Args:
        *values: Values representing the population
    
    Returns:
        float: Population standard deviation
    
    Raises:
        ValueError: If no values provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> STDEVPA(1345, 1301, 1368, True, False, "test")
        590.69...
    """
    converted_values = _convert_values_a(*values)

    if len(converted_values) < 1:
        raise ValueError("STDEVPA requires at least 1 value")

    return _core_std_dev(converted_values, sample=False)


def STEYX(known_y: List[float], known_x: List[float]) -> float:
    """
    Returns the standard error of the predicted y-value for each x in the regression.
    
    Excel function: STEYX (ERROR.TIPICO.XY in Spanish)
    
    Description:
        Returns the standard error of the predicted y-value for each x in the
        regression. The standard error is a measure of the amount of error in
        the prediction of y for an individual x.
    
    Args:
        known_y: Array or range of dependent data points
        known_x: Array or range of independent data points
    
    Returns:
        float: Standard error of regression
    
    Raises:
        ValueError: If arrays have different lengths or less than 3 points
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> STEYX([2, 3, 9, 1, 8], [6, 5, 11, 7, 5])
        3.305...
    """
    if len(known_y) != len(known_x):
        raise ValueError("Arrays must have equal length")

    if len(known_y) < 3:
        raise ValueError("At least 3 data points required")

    y_vals = [float(v) for v in known_y]
    x_vals = [float(v) for v in known_x]

    return float(_core_standard_error_estimate(y_vals, x_vals))


# ============================================================================
# T-DISTRIBUTION FUNCTIONS
# ============================================================================

def T_DIST(x: float, deg_freedom: int, cumulative: bool = False) -> float:
    """
    Returns the Student's t-distribution.
    
    Excel function: T.DIST (DISTR.T.N in Spanish)
    
    Description:
        Returns the left-tailed Student's t-distribution.
    
    Args:
        x: Numeric value at which to evaluate the distribution
        deg_freedom: Degrees of freedom
        cumulative: If True, returns CDF; if False, returns PDF
    
    Returns:
        float: t-distribution value
    
    Raises:
        ValueError: If deg_freedom < 1
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> T_DIST(1.959999998, 60, True)
        0.973...
    """
    return _core_t_dist(x, deg_freedom, cumulative)


def T_DIST_2T(x: float, deg_freedom: int) -> float:
    """
    Returns the two-tailed Student's t-distribution.
    
    Excel function: T.DIST.2T (DISTR.T.2C in Spanish)
    
    Description:
        Returns the two-tailed Student's t-distribution.
    
    Args:
        x: Numeric value at which to evaluate the distribution (must be >= 0)
        deg_freedom: Degrees of freedom
    
    Returns:
        float: Two-tailed probability
    
    Raises:
        ValueError: If x < 0 or deg_freedom < 1
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> T_DIST_2T(1.959999998, 60)
        0.054...
    """
    return _core_t_dist_2t(x, deg_freedom)


def T_DIST_RT(x: float, deg_freedom: int) -> float:
    """
    Returns the right-tailed Student's t-distribution.
    
    Excel function: T.DIST.RT (DISTR.T.CD in Spanish)
    
    Description:
        Returns the right-tailed Student's t-distribution.
    
    Args:
        x: Numeric value at which to evaluate the distribution
        deg_freedom: Degrees of freedom
    
    Returns:
        float: Right-tailed probability
    
    Raises:
        ValueError: If deg_freedom < 1
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> T_DIST_RT(1.959999998, 60)
        0.027...
    """
    return _core_t_dist_rt(x, deg_freedom)


def T_INV(probability: float, deg_freedom: int) -> float:
    """
    Returns the left-tailed inverse of the Student's t-distribution.
    
    Excel function: T.INV (INV.T in Spanish)
    
    Description:
        Returns the t-value of the Student's t-distribution as a function of
        the probability and the degrees of freedom.
    
    Args:
        probability: Probability associated with the t-distribution
        deg_freedom: Degrees of freedom
    
    Returns:
        float: t-value
    
    Raises:
        ValueError: If probability not in (0,1) or deg_freedom < 1
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> T_INV(0.75, 2)
        0.816...
    """
    return _core_t_inv(probability, deg_freedom)


def T_INV_2T(probability: float, deg_freedom: int) -> float:
    """
    Returns the two-tailed inverse of the Student's t-distribution.
    
    Excel function: T.INV.2T (INV.T.2C in Spanish)
    
    Description:
        Returns the t-value of the Student's t-distribution as a function of
        the probability and the degrees of freedom (two-tailed).
    
    Args:
        probability: Probability associated with the two-tailed t-distribution
        deg_freedom: Degrees of freedom
    
    Returns:
        float: t-value
    
    Raises:
        ValueError: If probability not in (0,1) or deg_freedom < 1
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> T_INV_2T(0.05, 60)
        2.000...
    """
    return _core_t_inv_2t(probability, deg_freedom)


def TRIMMEAN(array: List[Union[float, int]], fraction: float) -> float:
    """
    Returns the mean of the interior of a data set.
    
    Excel function: TRIMMEAN (MEDIA.ACOTADA in Spanish)
    
    Description:
        Returns the mean of the interior portion of a data set. TRIMMEAN calculates
        the mean taken by excluding a percentage of data points from the top and
        bottom tails of a data set.
    
    Args:
        array: Array or range of values to trim and average
        fraction: Fractional number of data points to exclude (0 to 1)
    
    Returns:
        float: Trimmed mean
    
    Raises:
        ValueError: If fraction not in [0,1) or array too small
    
    Cost:
        O(n log n) - Due to sorting
    
    Usage:
        >>> TRIMMEAN([4, 5, 6, 7, 2, 3, 4, 5, 1, 2, 3], 0.2)
        3.777...
    """
    if fraction < 0 or fraction >= 1:
        raise ValueError("Fraction must be in range [0, 1)")
    
    numeric_values = [v for v in array if isinstance(v, (int, float)) and not isinstance(v, bool)]
    
    if not numeric_values:
        raise ValueError("Array must contain at least one numeric value")
    
    return float(_core_trimmed_mean(numeric_values, fraction / 2))


# ============================================================================
# VARIANCE FUNCTIONS
# ============================================================================

def VAR_P(*values: Union[float, int, List]) -> float:
    """
    Calculates variance based on the entire population.
    
    Excel function: VAR.P (VAR.P in Spanish)
    
    Description:
        Calculates variance based on the entire population. Ignores logical
        values and text in the population.
    
    Args:
        *values: Numbers or lists representing the population
    
    Returns:
        float: Population variance
    
    Raises:
        ValueError: If less than 1 value provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> VAR_P(1345, 1301, 1368, 1322, 1310, 1370, 1318, 1350, 1303, 1299)
        754.27...
    """
    numeric_values = _extract_numerics(*values)

    if len(numeric_values) < 1:
        raise ValueError("VAR.P requires at least one value")

    return _core_variance(numeric_values, sample=False)


def VAR_S(*values: Union[float, int, List]) -> float:
    """
    Estimates variance based on a sample.
    
    Excel function: VAR.S (VAR.S in Spanish) / VAR
    
    Description:
        Estimates variance based on a sample (ignores logical values and text).
    
    Args:
        *values: Numbers or lists representing a sample of a population
    
    Returns:
        float: Sample variance
    
    Raises:
        ValueError: If less than 2 values provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> VAR_S(1345, 1301, 1368, 1322, 1310, 1370, 1318, 1350, 1303, 1299)
        843.63...
    """
    numeric_values = _extract_numerics(*values)

    if len(numeric_values) < 2:
        raise ValueError("VAR.S requires at least 2 values")

    return _core_variance(numeric_values, sample=True)


def VARA(*values: Union[float, int, str, bool, List]) -> float:
    """
    Estimates variance based on a sample, including text and logical values.
    
    Excel function: VARA
    
    Description:
        Estimates variance based on a sample. Text and FALSE evaluate to 0;
        TRUE evaluates to 1.
    
    Args:
        *values: Values to include in the sample
    
    Returns:
        float: Sample variance
    
    Raises:
        ValueError: If less than 2 values provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> VARA(1345, 1301, 1368, True, False, "test")
        389054.8
    """
    converted_values = _convert_values_a(*values)

    if len(converted_values) < 2:
        raise ValueError("VARA requires at least 2 values")

    return _core_variance(converted_values, sample=True)


def VARPA(*values: Union[float, int, str, bool, List]) -> float:
    """
    Calculates variance based on population, including text and logical values.
    
    Excel function: VARPA
    
    Description:
        Calculates variance based on the entire population. Text and FALSE
        evaluate to 0; TRUE evaluates to 1.
    
    Args:
        *values: Values representing the population
    
    Returns:
        float: Population variance
    
    Raises:
        ValueError: If no values provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> VARPA(1345, 1301, 1368, True, False, "test")
        348924.72...
    """
    converted_values = _convert_values_a(*values)

    if len(converted_values) < 1:
        raise ValueError("VARPA requires at least 1 value")

    return _core_variance(converted_values, sample=False)


# ============================================================================
# WEIBULL DISTRIBUTION
# ============================================================================

def WEIBULL_DIST(x: float, alpha: float, beta: float, cumulative: bool = False) -> float:
    """
    Returns the Weibull distribution.
    
    Excel function: WEIBULL.DIST (DISTR.WEIBULL in Spanish)
    
    Description:
        Returns the Weibull distribution. Use this distribution in reliability
        analysis, such as calculating a device's mean time to failure.
    
    Args:
        x: Value at which to evaluate the function (must be >= 0)
        alpha: Shape parameter (must be > 0)
        beta: Scale parameter (must be > 0)
        cumulative: If True, returns CDF; if False, returns PDF
    
    Returns:
        float: Weibull distribution value
    
    Raises:
        ValueError: If parameters are out of valid range
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> WEIBULL_DIST(105, 20, 100, True)
        0.929...
    """
    return _core_weibull_dist(x, alpha, beta, cumulative)


# ============================================================================
# RANKING FUNCTIONS
# ============================================================================

def RANK_EQ(number: Union[float, int], ref: List[Union[float, int]],
            order: int = 0) -> int:
    """Returns the rank of a number in a list. Duplicate values receive the same rank.

    Excel function: RANK.EQ (JERARQUIA.EQV in Spanish)

    Description:
        Returns the rank of a number within a list. If more than one value
        has the same rank, the top rank of that set is returned (like a
        competition ranking).

    Args:
        number: Value whose rank you want to find.
        ref: List of numeric values (the reference).
        order: 0 = descending (largest is rank 1), nonzero = ascending
            (smallest is rank 1).

    Returns:
        int: Rank of the number within the list.

    Raises:
        ValueError: If number is not found in ref or ref is empty.

    Usage Example:
        >>> RANK_EQ(3, [7, 3, 3, 1])
        2
        >>> RANK_EQ(1, [7, 3, 3, 1], order=1)
        1

    Cost: O(n log n) — due to sorting.
    """
    numeric = [v for v in ref if isinstance(v, (int, float)) and not isinstance(v, bool)]

    if not numeric:
        raise ValueError("ref must contain at least one numeric value.")

    if number not in numeric:
        raise ValueError("number is not found in the reference list.")

    ranks = _core_rank(numeric, method='min', ascending=(order != 0))
    idx = numeric.index(number)

    return int(ranks[idx])


def RANK_AVG(number: Union[float, int], ref: List[Union[float, int]],
             order: int = 0) -> float:
    """Returns the rank of a number in a list, averaging for ties.

    Excel function: RANK.AVG (JERARQUIA.MEDIA in Spanish)

    Description:
        Returns the rank of a number within a list. Duplicate values
        receive the average of their positions (fractional ranking).

    Args:
        number: Value whose rank you want to find.
        ref: List of numeric values (the reference).
        order: 0 = descending (largest is rank 1), nonzero = ascending
            (smallest is rank 1).

    Returns:
        float: Average rank of the number within the list.

    Raises:
        ValueError: If number is not found in ref or ref is empty.

    Usage Example:
        >>> RANK_AVG(3, [7, 3, 3, 1])
        2.5
        >>> RANK_AVG(1, [7, 3, 3, 1], order=1)
        1.0

    Cost: O(n log n) — due to sorting.
    """
    numeric = [v for v in ref if isinstance(v, (int, float)) and not isinstance(v, bool)]

    if not numeric:
        raise ValueError("ref must contain at least one numeric value.")

    if number not in numeric:
        raise ValueError("number is not found in the reference list.")

    ranks = _core_rank(numeric, method='average', ascending=(order != 0))
    idx = numeric.index(number)

    return float(ranks[idx])


# ============================================================================
# REGRESSION METRICS
# ============================================================================

def RSQ(known_y: List[float], known_x: List[float]) -> float:
    """Returns the R-squared value of the linear regression line.

    Excel function: RSQ (COEFICIENTE.R2 in Spanish)

    Description:
        Calculates the square of the Pearson correlation coefficient,
        representing the proportion of variance in known_y explained by
        known_x through linear regression.

    Args:
        known_y: Array of dependent data points.
        known_x: Array of independent data points.

    Returns:
        float: R-squared value between 0 and 1.

    Raises:
        ValueError: If arrays have different lengths or fewer than 2 points.

    Usage Example:
        >>> RSQ([2, 3, 9, 1, 8], [6, 5, 11, 7, 5])
        0.05795...

    Cost: O(n) — single pass correlation.
    """
    if len(known_y) != len(known_x):
        raise ValueError("Arrays must have equal length.")

    if len(known_y) < 2:
        raise ValueError("At least 2 data points required.")

    y = [float(v) for v in known_y]
    x = [float(v) for v in known_x]

    correlation = _core_pearson(x, y)

    return float(correlation ** 2)


def TREND(known_y: List[float], known_x: Optional[List[float]] = None,
          new_x: Optional[List[float]] = None,
          const: bool = True) -> List[float]:
    """Returns values along a linear trend using least-squares regression.

    Excel function: TREND (TENDENCIA in Spanish)

    Description:
        Calculates predicted y-values along a linear trend line fitted
        with the least-squares method.

    Args:
        known_y: Set of known y-values.
        known_x: Set of known x-values (defaults to 1, 2, 3, ...).
        new_x: New x-values for which to predict y (defaults to known_x).
        const: If True, calculate intercept normally; if False, force
            through origin.

    Returns:
        List[float]: Predicted y-values for each new_x point.

    Raises:
        ValueError: If known_y and known_x have different lengths.

    Usage Example:
        >>> TREND([1, 2, 3, 4], [10, 20, 30, 40], [50, 60])
        [5.0, 6.0]

    Cost: O(n) — linear regression.
    """
    if known_x is None:
        known_x = list(range(1, len(known_y) + 1))

    if len(known_y) != len(known_x):
        raise ValueError("known_y and known_x must have equal length.")

    if new_x is None:
        new_x = known_x

    x_vals = [float(v) for v in known_x]
    y_vals = [float(v) for v in known_y]
    new_x_vals = [float(v) for v in new_x]

    return _core_trend(y_vals, x_vals, new_x_vals, const=const)


def PROB(x_range: List[Union[float, int]],
         prob_range: List[float],
         lower_limit: Union[float, int],
         upper_limit: Optional[Union[float, int]] = None) -> float:
    """Returns the probability that values fall within a range.

    Excel function: PROB (PROBABILIDAD in Spanish)

    Description:
        Returns the probability that values in x_range fall between
        lower_limit and upper_limit, given associated probabilities.

    Args:
        x_range: Array of numeric values.
        prob_range: Array of probabilities associated with x_range values.
        lower_limit: Lower bound of the interval.
        upper_limit: Upper bound (defaults to lower_limit for exact match).

    Returns:
        float: Sum of probabilities for values within the limits.

    Raises:
        ValueError: If arrays differ in length, probabilities are invalid,
            or no matching values found.

    Usage Example:
        >>> PROB([0, 1, 2, 3], [0.1, 0.2, 0.3, 0.4], 2)
        0.3
        >>> PROB([0, 1, 2, 3], [0.1, 0.2, 0.3, 0.4], 1, 3)
        0.9

    Cost: O(n) — single pass.
    """
    if len(x_range) != len(prob_range):
        raise ValueError("x_range and prob_range must have equal length.")

    if any(p < 0 for p in prob_range):
        raise ValueError("Probabilities must be non-negative.")

    total_prob = sum(prob_range)

    if abs(total_prob - 1.0) > 1e-6:
        raise ValueError("Probabilities must sum to 1.")

    return float(_core_probability_range(x_range, prob_range, lower_limit, upper_limit))


# ============================================================================
# BACKWARD-COMPATIBILITY ALIASES
# ============================================================================


def RANK(number: Union[float, int], ref: List[Union[float, int]],
         order: int = 0) -> int:
    """Returns the rank of a number in a list (backward compatibility alias for RANK.EQ).

    Excel function: RANK

    Args:
        number: Value whose rank you want to find.
        ref: List of numeric values.
        order: 0 = descending, nonzero = ascending.

    Returns:
        int: Rank of the number within the list.

    Raises:
        ValueError: If number is not found in ref.

    Usage Example:
        >>> RANK(3, [7, 3, 5, 1])
        3

    Cost: O(n log n)
    """
    return RANK_EQ(number, ref, order)


def FORECAST(x: float, known_y: List[float],
             known_x: Optional[List[float]] = None) -> float:
    """Returns a single predicted value along a linear trend (backward compat).

    Excel function: FORECAST

    Args:
        x: The x-value for which to predict y.
        known_y: Set of known y-values.
        known_x: Set of known x-values (defaults to 1, 2, 3, ...).

    Returns:
        float: The predicted y-value.

    Usage Example:
        >>> FORECAST(6, [1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
        0.6

    Cost: O(n)
    """
    return FORECAST_LINEAR(x, known_y, known_x)


def STDEV(*values: Union[float, int, List]) -> float:
    """Calculates standard deviation based on a sample (backward compat alias).

    Excel function: STDEV

    Args:
        *values: Numeric values or lists.

    Returns:
        float: Sample standard deviation.

    Usage Example:
        >>> STDEV(1, 2, 3, 4, 5)
        1.5811...

    Cost: O(n)
    """
    return STDEV_S(*values)


def VAR(*values: Union[float, int, List]) -> float:
    """Calculates variance based on a sample (backward compat alias).

    Excel function: VAR

    Args:
        *values: Numeric values or lists.

    Returns:
        float: Sample variance.

    Usage Example:
        >>> VAR(1, 2, 3, 4, 5)
        2.5

    Cost: O(n)
    """
    return VAR_S(*values)


def MODE(values: List[Union[float, int]]) -> float:
    """Returns the most common value in a data set (backward compat alias).

    Excel function: MODE

    Args:
        values: List of numeric values.

    Returns:
        float: The mode.

    Usage Example:
        >>> MODE([1, 2, 2, 3])
        2.0

    Cost: O(n)
    """
    return MODE_SNGL(values)


def PERCENTILE(array: List[Union[float, int]], k: float) -> float:
    """Returns the k-th percentile (backward compat alias).

    Excel function: PERCENTILE

    Args:
        array: List of numeric values.
        k: Percentile (0..1).

    Returns:
        float: The percentile value.

    Usage Example:
        >>> PERCENTILE([1, 2, 3, 4], 0.5)
        2.5

    Cost: O(n log n)
    """
    return PERCENTILE_INC(array, k)


def PERCENTRANK(array: List[Union[float, int]], x: float,
                significance: int = 3) -> float:
    """Returns the percentage rank (backward compat alias).

    Excel function: PERCENTRANK

    Args:
        array: List of numeric values.
        x: The value to rank.
        significance: Number of significant digits.

    Returns:
        float: Percentage rank.

    Usage Example:
        >>> PERCENTRANK([1, 2, 3, 4], 3)
        0.667

    Cost: O(n log n)
    """
    return PERCENTRANK_INC(array, x, significance)


def CONFIDENCE(alpha: float, standard_dev: float, size: int) -> float:
    """Returns the confidence interval (backward compat alias).

    Excel function: CONFIDENCE

    Args:
        alpha: Significance level.
        standard_dev: Population standard deviation.
        size: Sample size.

    Returns:
        float: Confidence interval half-width.

    Usage Example:
        >>> CONFIDENCE(0.05, 2.5, 50)
        0.6929...

    Cost: O(1)
    """
    return CONFIDENCE_NORM(alpha, standard_dev, size)


def QUARTILE(array: List[Union[float, int]], quart: int) -> float:
    """Returns the quartile of a data set (backward compat alias).

    Excel function: QUARTILE

    Args:
        array: List of numeric values.
        quart: Quartile value (0 = min, 1 = 25th, 2 = median, 3 = 75th, 4 = max).

    Returns:
        float: The quartile value.

    Usage Example:
        >>> QUARTILE([1, 2, 3, 4], 2)
        2.5

    Cost: O(n log n)
    """
    return QUARTILE_INC(array, quart)


# ============================================================================
# BACKWARD COMPATIBILITY ALIASES (pre-2010 Excel function names)
# ============================================================================

def BETADIST(x: float, alpha: float, beta: float,
             A: float = 0, B: float = 1) -> float:
    """Returns the beta cumulative distribution (backward compat alias).

    Usage Example:
        >>> round(BETADIST(2, 8, 10, 1, 3), 6)
        0.685470

    Cost: O(1)
    """
    return BETA_DIST(x, alpha, beta, True, A, B)


def BETAINV(probability: float, alpha: float, beta: float,
            A: float = 0, B: float = 1) -> float:
    """Returns the inverse of the beta cumulative distribution (backward compat alias).

    Usage Example:
        >>> round(BETAINV(0.685470, 8, 10, 1, 3), 1)
        2.0

    Cost: O(1)
    """
    return BETA_INV(probability, alpha, beta, A, B)


def BINOMDIST(number_s: int, trials: int, probability_s: float,
              cumulative: bool = True) -> float:
    """Returns the binomial distribution probability (backward compat alias).

    Usage Example:
        >>> round(BINOMDIST(6, 10, 0.5, False), 6)
        0.205078

    Cost: O(1)
    """
    return BINOM_DIST(number_s, trials, probability_s, cumulative)


def CHIDIST(x: float, deg_freedom: int) -> float:
    """Returns the right-tailed chi-squared distribution (backward compat alias).

    Usage Example:
        >>> round(CHIDIST(18.307, 10), 4)
        0.0500

    Cost: O(1)
    """
    return CHISQ_DIST_RT(x, deg_freedom)


def CHIINV(probability: float, deg_freedom: int) -> float:
    """Returns the inverse of the right-tailed chi-squared distribution (backward compat alias).

    Usage Example:
        >>> round(CHIINV(0.05, 10), 3)
        18.307

    Cost: O(1)
    """
    return CHISQ_INV_RT(probability, deg_freedom)


def CHITEST(actual_range: List[List[float]],
            expected_range: List[List[float]]) -> float:
    """Returns the chi-squared test for independence (backward compat alias).

    Usage Example:
        >>> CHITEST([[58, 35], [11, 25]], [[43.35, 49.65], [25.65, 10.35]])  # doctest: +SKIP
        0.000...

    Cost: O(r * c)
    """
    return CHISQ_TEST(actual_range, expected_range)


def CRITBINOM(trials: int, probability_s: float, alpha: float) -> int:
    """Returns the smallest value for cumulative binomial distribution (backward compat alias).

    Usage Example:
        >>> CRITBINOM(6, 0.5, 0.75)
        4

    Cost: O(1)
    """
    return BINOM_INV(trials, probability_s, alpha)


def EXPONDIST(x: float, lambda_: float,
              cumulative: bool = True) -> float:
    """Returns the exponential distribution (backward compat alias).

    Usage Example:
        >>> round(EXPONDIST(0.2, 10, True), 6)
        0.864665

    Cost: O(1)
    """
    return EXPON_DIST(x, lambda_, cumulative)


def FDIST(x: float, deg_freedom1: int, deg_freedom2: int) -> float:
    """Returns the right-tailed F probability distribution (backward compat alias).

    Usage Example:
        >>> round(FDIST(15.2069, 6, 4), 4)
        0.0100

    Cost: O(1)
    """
    return F_DIST_RT(x, deg_freedom1, deg_freedom2)


def FINV(probability: float, deg_freedom1: int, deg_freedom2: int) -> float:
    """Returns the inverse of the right-tailed F distribution (backward compat alias).

    Usage Example:
        >>> round(FINV(0.01, 6, 4), 4)
        15.2069

    Cost: O(1)
    """
    return F_INV_RT(probability, deg_freedom1, deg_freedom2)


def FTEST(array1: List[float], array2: List[float]) -> float:
    """Returns the F-test result (backward compat alias).

    Usage Example:
        >>> FTEST([6, 7, 9, 15, 21], [20, 28, 31, 38, 40])  # doctest: +SKIP
        0.648...

    Cost: O(n)
    """
    return F_TEST(array1, array2)


def GAMMADIST(x: float, alpha: float, beta: float,
              cumulative: bool = True) -> float:
    """Returns the gamma distribution (backward compat alias).

    Usage Example:
        >>> round(GAMMADIST(10.00001131, 9, 2, False), 6)
        0.032639

    Cost: O(1)
    """
    return GAMMA_DIST(x, alpha, beta, cumulative)


def GAMMAINV(probability: float, alpha: float, beta: float) -> float:
    """Returns the inverse of the gamma cumulative distribution (backward compat alias).

    Usage Example:
        >>> round(GAMMAINV(0.068094, 9, 2), 4)
        10.0000

    Cost: O(1)
    """
    return GAMMA_INV(probability, alpha, beta)


def HYPGEOMDIST(sample_s: int, number_sample: int,
                population_s: int, number_pop: int) -> float:
    """Returns the hypergeometric distribution (backward compat alias).

    Usage Example:
        >>> round(HYPGEOMDIST(1, 4, 8, 20), 6)
        0.363261

    Cost: O(1)
    """
    return HYPGEOM_DIST(sample_s, number_sample, population_s, number_pop, False)


def LOGINV(probability: float, mean: float, standard_dev: float) -> float:
    """Returns the inverse of the lognormal cumulative distribution (backward compat alias).

    Usage Example:
        >>> round(LOGINV(0.039084, 3.5, 1.2), 4)
        4.7002

    Cost: O(1)
    """
    return LOGNORM_INV(probability, mean, standard_dev)


def LOGNORMDIST(x: float, mean: float, standard_dev: float) -> float:
    """Returns the cumulative lognormal distribution (backward compat alias).

    Usage Example:
        >>> round(LOGNORMDIST(4, 3.5, 1.2), 6)
        0.039084

    Cost: O(1)
    """
    return LOGNORM_DIST(x, mean, standard_dev, True)


def NEGBINOMDIST(number_f: int, number_s: int,
                 probability_s: float) -> float:
    """Returns the negative binomial distribution (backward compat alias).

    Usage Example:
        >>> round(NEGBINOMDIST(10, 5, 0.25), 6)
        0.055049

    Cost: O(1)
    """
    return NEGBINOM_DIST(number_f, number_s, probability_s, False)


def NORMDIST(x: float, mean: float, standard_dev: float,
             cumulative: bool = True) -> float:
    """Returns the normal cumulative distribution (backward compat alias).

    Usage Example:
        >>> round(NORMDIST(42, 40, 1.5, True), 6)
        0.908789

    Cost: O(1)
    """
    return NORM_DIST(x, mean, standard_dev, cumulative)


def NORMINV(probability: float, mean: float, standard_dev: float) -> float:
    """Returns the inverse of the normal cumulative distribution (backward compat alias).

    Usage Example:
        >>> round(NORMINV(0.908789, 40, 1.5), 0)
        42.0

    Cost: O(1)
    """
    return NORM_INV(probability, mean, standard_dev)


def NORMSDIST(z: float) -> float:
    """Returns the standard normal cumulative distribution (backward compat alias).

    Usage Example:
        >>> round(NORMSDIST(1.333333), 6)
        0.908789

    Cost: O(1)
    """
    return NORM_S_DIST(z, True)


def NORMSINV(probability: float) -> float:
    """Returns the inverse of the standard normal cumulative distribution (backward compat alias).

    Usage Example:
        >>> round(NORMSINV(0.908789), 6)
        1.333333

    Cost: O(1)
    """
    return NORM_S_INV(probability)


def POISSON(x: int, mean: float, cumulative: bool = True) -> float:
    """Returns the Poisson distribution (backward compat alias).

    Usage Example:
        >>> round(POISSON(2, 5, True), 6)
        0.124652

    Cost: O(1)
    """
    return POISSON_DIST(x, mean, cumulative)


def STDEVP(*values: Union[float, int, List]) -> float:
    """Returns population standard deviation (backward compat alias).

    Usage Example:
        >>> round(STDEVP(1, 2, 3, 4, 5), 6)
        1.414214

    Cost: O(n)
    """
    return STDEV_P(*values)


def TDIST(x: float, deg_freedom: int, tails: int = 2) -> float:
    """Returns the Student's t-distribution (backward compat alias).

    Usage Example:
        >>> round(TDIST(1.96, 60, 2), 4)
        0.0546

    Cost: O(1)
    """
    if tails == 1:
        return T_DIST_RT(x, deg_freedom)

    return T_DIST_2T(x, deg_freedom)


def TINV(probability: float, deg_freedom: int) -> float:
    """Returns the inverse of the two-tailed Student's t-distribution (backward compat alias).

    Usage Example:
        >>> round(TINV(0.054645, 60), 2)
        1.96

    Cost: O(1)
    """
    return T_INV_2T(probability, deg_freedom)


def TTEST(array1: List[float], array2: List[float],
          tails: int = 2, test_type: int = 2) -> float:
    """Returns the probability from a t-test (backward compat alias).

    Usage Example:
        >>> TTEST([3, 4, 5, 8, 9, 1, 2, 4, 5], [6, 19, 3, 2, 14, 4, 5, 17, 1], 2, 2)  # doctest: +SKIP
        0.196...

    Cost: O(n)
    """
    return T_TEST(array1, array2, tails, test_type)


def VARP(*values: Union[float, int, List]) -> float:
    """Returns population variance (backward compat alias).

    Usage Example:
        >>> round(VARP(1, 2, 3, 4, 5), 1)
        2.0

    Cost: O(n)
    """
    return VAR_P(*values)


def WEIBULL(x: float, alpha: float, beta: float,
            cumulative: bool = True) -> float:
    """Returns the Weibull distribution (backward compat alias).

    Usage Example:
        >>> round(WEIBULL(105, 20, 100, True), 6)
        0.929581

    Cost: O(1)
    """
    return WEIBULL_DIST(x, alpha, beta, cumulative)


def ZTEST(array: List[float], x: float,
          sigma: Optional[float] = None) -> float:
    """Returns the one-tailed probability-value of a z-test (backward compat alias).

    Usage Example:
        >>> ZTEST([3, 6, 7, 8, 6, 5, 4, 2, 1, 9], 4)  # doctest: +SKIP
        0.090...

    Cost: O(n)
    """
    return Z_TEST(array, x, sigma)


