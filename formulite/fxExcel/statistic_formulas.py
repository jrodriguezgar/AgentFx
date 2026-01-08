"""
FormuLite fxExcel - Statistical Functions Module

Excel-compatible statistical functions using official English Excel function names.
All functions follow Excel's standard naming conventions.
"""

import numpy as np
import scipy.stats as stats
import math
from typing import List, Union, Optional, Any


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
    return float(np.corrcoef(array1, array2)[0, 1])


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
    return sum(1 for val in values if isinstance(val, (int, float)) and not isinstance(val, bool))


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
    return sum(1 for val in values if val is not None and val != "")


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
    return sum(1 for val in range_values if val is None or val == "")


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
    if isinstance(criteria, str) and criteria and criteria[0] in "><!=":
        # Extract operator and value
        if criteria[:2] in {">=", "<=", "<>", "!="}:
            op = criteria[:2]
            val_str = criteria[2:]
        else:
            op = criteria[0]
            val_str = criteria[1:]
        
        try:
            value = float(val_str)
            count = 0
            for x in range_values:
                if isinstance(x, (int, float)):
                    if op == ">=" and x >= value:
                        count += 1
                    elif op == "<=" and x <= value:
                        count += 1
                    elif op == ">" and x > value:
                        count += 1
                    elif op == "<" and x < value:
                        count += 1
                    elif op == "=" and x == value:
                        count += 1
                    elif op in {"<>", "!="} and x != value:
                        count += 1
            return count
        except ValueError:
            pass
    
    return sum(1 for x in range_values if x == criteria)


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
    
    pairs = [(args[i], args[i+1]) for i in range(0, len(args), 2)]
    if not pairs:
        return 0
    
    # All ranges must have the same length
    length = len(pairs[0][0])
    if not all(len(rng) == length for rng, _ in pairs):
        raise ValueError("All ranges must have the same length")
    
    count = 0
    for i in range(length):
        meets_all = True
        for rng, criteria in pairs:
            value = rng[i]
            
            if isinstance(criteria, str) and criteria and criteria[0] in "><!=":
                # Extract operator and value
                if criteria[:2] in {">=", "<=", "<>", "!="}:
                    op = criteria[:2]
                    val_str = criteria[2:]
                else:
                    op = criteria[0]
                    val_str = criteria[1:]
                
                try:
                    crit_value = float(val_str)
                    if not isinstance(value, (int, float)):
                        meets_all = False
                        break
                    
                    if op == ">=" and not (value >= crit_value):
                        meets_all = False
                        break
                    elif op == "<=" and not (value <= crit_value):
                        meets_all = False
                        break
                    elif op == ">" and not (value > crit_value):
                        meets_all = False
                        break
                    elif op == "<" and not (value < crit_value):
                        meets_all = False
                        break
                    elif op == "=" and not (value == crit_value):
                        meets_all = False
                        break
                    elif op in {"<>", "!="} and not (value != crit_value):
                        meets_all = False
                        break
                except ValueError:
                    meets_all = False
                    break
            elif value != criteria:
                meets_all = False
                break
        
        if meets_all:
            count += 1
    
    return count


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
    return float(np.cov(array1, array2, bias=True)[0, 1])


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
    return float(np.cov(array1, array2, bias=False)[0, 1])


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
    
    log_y = np.log(np.array(known_y))
    coeffs = np.polyfit(known_x, log_y, 1)
    
    if const:
        return [float(np.exp(coeffs[1] + coeffs[0] * x)) for x in new_x]
    else:
        # Force constant term to 1 (coeffs[1] = 0)
        slope = np.sum(np.array(known_x) * log_y) / np.sum(np.array(known_x) ** 2)
        return [float(np.exp(slope * x)) for x in new_x]


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
    if len(values) < 4:
        raise ValueError("At least 4 data points required")
    return float(stats.kurtosis(values, fisher=True))


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
    if not values:
        raise ValueError("Values cannot be empty")
    mean = np.mean(values)
    return float(np.mean([abs(x - mean) for x in values]))


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
    if not values:
        raise ValueError("Values cannot be empty")
    mean = np.mean(values)
    return float(sum((x - mean) ** 2 for x in values))


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
    return float(np.exp(np.mean(np.log(values))))


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
    return float(len(values) / sum(1/x for x in values))


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
    if k < 1 or k > len(array):
        raise ValueError(f"k must be between 1 and {len(array)}")
    return float(sorted(array, reverse=True)[k-1])


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
    
    pairs = [(args[i], args[i+1]) for i in range(0, len(args), 2)]
    
    valid_values = []
    for i in range(len(max_range)):
        meets_all = True
        for rng, criteria in pairs:
            if i >= len(rng):
                meets_all = False
                break
            
            value = rng[i]
            
            if isinstance(criteria, str) and criteria and criteria[0] in "><!=":
                if criteria[:2] in {">=", "<=", "<>", "!="}:
                    op = criteria[:2]
                    val_str = criteria[2:]
                else:
                    op = criteria[0]
                    val_str = criteria[1:]
                
                try:
                    crit_value = float(val_str)
                    if not isinstance(value, (int, float)):
                        meets_all = False
                        break
                    
                    if op == ">=" and not (value >= crit_value):
                        meets_all = False
                        break
                    elif op == "<=" and not (value <= crit_value):
                        meets_all = False
                        break
                    elif op == ">" and not (value > crit_value):
                        meets_all = False
                        break
                    elif op == "<" and not (value < crit_value):
                        meets_all = False
                        break
                    elif op == "=" and not (value == crit_value):
                        meets_all = False
                        break
                    elif op in {"<>", "!="} and not (value != crit_value):
                        meets_all = False
                        break
                except ValueError:
                    meets_all = False
                    break
            elif value != criteria:
                meets_all = False
                break
        
        if meets_all:
            valid_values.append(max_range[i])
    
    if not valid_values:
        raise ValueError("No values meet the criteria")
    return float(max(valid_values))


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
        return float(stats.beta.cdf(x, alpha, beta, loc=A, scale=B-A))
    else:
        return float(stats.beta.pdf(x, alpha, beta, loc=A, scale=B-A))


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
    return float(stats.beta.ppf(probability, alpha, beta, loc=A, scale=B-A))


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
    if cumulative:
        return float(stats.binom.cdf(number_s, trials, probability_s))
    else:
        return float(stats.binom.pmf(number_s, trials, probability_s))


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
    if number_s2 is None:
        number_s2 = number_s
    
    prob = 0.0
    for k in range(number_s, number_s2 + 1):
        prob += stats.binom.pmf(k, trials, probability_s)
    return float(prob)


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
    return int(stats.binom.ppf(alpha, trials, probability_s))


def BINOM_CRIT(trials: int, probability_s: float, alpha: float) -> int:
    """
    Returns the smallest value for which the cumulative binomial distribution is >= criterion.
    
    Excel function: BINOM.CRIT (Compatibility function, same as BINOM.INV)
    
    Args:
        trials: Number of Bernoulli trials
        probability_s: Probability of success on each trial
        alpha: Criterion value
    
    Returns:
        int: Smallest number of successes
    
    Cost:
        O(1) - Constant time
    
    Usage:
        >>> BINOM_CRIT(10, 0.5, 0.75)
        6
    """
    return BINOM_INV(trials, probability_s, alpha)


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
    if cumulative:
        return float(stats.chi2.cdf(x, deg_freedom))
    else:
        return float(stats.chi2.pdf(x, deg_freedom))


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
    return float(1 - stats.chi2.cdf(x, deg_freedom))


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
    return float(stats.chi2.ppf(probability, deg_freedom))


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
    return float(stats.chi2.ppf(1 - probability, deg_freedom))


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
    if cumulative:
        return float(stats.expon.cdf(x, scale=1/lambda_))
    else:
        return float(stats.expon.pdf(x, scale=1/lambda_))


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
    if cumulative:
        return float(stats.f.cdf(x, deg_freedom1, deg_freedom2))
    else:
        return float(stats.f.pdf(x, deg_freedom1, deg_freedom2))


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
    return float(1 - stats.f.cdf(x, deg_freedom1, deg_freedom2))


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
    return float(stats.f.ppf(probability, deg_freedom1, deg_freedom2))


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
    return float(stats.f.ppf(1 - probability, deg_freedom1, deg_freedom2))


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
    if cumulative:
        return float(stats.gamma.cdf(x, a=alpha, scale=beta))
    else:
        return float(stats.gamma.pdf(x, a=alpha, scale=beta))


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
    return float(stats.gamma.ppf(probability, a=alpha, scale=beta))


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
    if cumulative:
        return float(stats.hypergeom.cdf(sample_s, number_pop, population_s, number_sample))
    else:
        return float(stats.hypergeom.pmf(sample_s, number_pop, population_s, number_sample))


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
    if cumulative:
        return float(stats.lognorm.cdf(x, s=standard_dev, scale=np.exp(mean)))
    else:
        return float(stats.lognorm.pdf(x, s=standard_dev, scale=np.exp(mean)))


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
    return float(stats.lognorm.ppf(probability, s=standard_dev, scale=np.exp(mean)))


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
        coeffs = np.polyfit(known_x, known_y, 1)
        slope, intercept = float(coeffs[0]), float(coeffs[1])
    else:
        # Force through origin
        slope = float(np.sum(np.array(known_x) * np.array(known_y)) / np.sum(np.array(known_x) ** 2))
        intercept = 0.0
    
    if stats_flag:
        # Return extended statistics: slope, intercept, r_squared, std_error, F_statistic
        y_pred = [slope * x + intercept for x in known_x]
        ss_res = sum((y - yp) ** 2 for y, yp in zip(known_y, y_pred))
        ss_tot = sum((y - np.mean(known_y)) ** 2 for y in known_y)
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
    
    log_y = np.log(np.array(known_y))
    
    if const:
        coeffs = np.polyfit(known_x, log_y, 1)
        base = float(np.exp(coeffs[0]))
        multiplier = float(np.exp(coeffs[1]))
    else:
        slope = float(np.sum(np.array(known_x) * log_y) / np.sum(np.array(known_x) ** 2))
        base = float(np.exp(slope))
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
    _, intercept = LINEST(known_y, known_x)
    return float(intercept)


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
    slope, _ = LINEST(known_y, known_x)
    return float(slope)


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
    slope, intercept = LINEST(known_y, known_x)
    return float(slope * x + intercept)


# Alias for backward compatibility
FORECAST = FORECAST_LINEAR


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
    return FORECAST_LINEAR(target_date, values, timeline)


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
    std_err = np.std(values) / np.sqrt(len(values))
    z = stats.norm.ppf(1 - (1 - confidence_level) / 2)
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
    if abs(x) >= 1:
        raise ValueError("Value must be between -1 and 1")
    return float(0.5 * np.log((1 + x) / (1 - x)))


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
    e2y = np.exp(2 * y)
    return float((e2y - 1) / (e2y + 1))


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
    return float(math.gamma(number))


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
    return float(math.lgamma(x))


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
    return float(stats.norm.cdf(z) - 0.5)


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
    counts, _ = np.histogram(data_array, bins=bins_array + [float('inf')])
    return counts.tolist()


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
    z = stats.norm.ppf(1 - alpha / 2)
    return float(z * standard_dev / np.sqrt(size))


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
    t = stats.t.ppf(1 - alpha / 2, df=size - 1)
    return float(t * standard_dev / np.sqrt(size))


# Alias for backward compatibility
CONFIDENCE = CONFIDENCE_NORM


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
    numeric_values = []
    
    for val in values:
        if isinstance(val, (list, tuple)):
            for v in val:
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    numeric_values.append(v)
        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            numeric_values.append(val)
    
    if not numeric_values:
        raise ValueError("AVERAGE requires at least one numeric value")
    
    return sum(numeric_values) / len(numeric_values)


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
        raise ValueError("AVERAGEA requires at least one value")
    
    return sum(converted_values) / len(converted_values)


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
    
    if len(range_values) != len(average_range):
        raise ValueError("Range and average_range must have the same length")
    
    # Parse criteria
    def meets_criteria(value, criteria):
        if isinstance(criteria, str):
            # Handle comparison operators
            for op in ['>=', '<=', '<>', '>', '<', '=']:
                if criteria.startswith(op):
                    criteria_val = criteria[len(op):]
                    try:
                        criteria_num = float(criteria_val)
                        value_num = float(value) if isinstance(value, (int, float)) else 0
                        
                        if op == '>=': return value_num >= criteria_num
                        elif op == '<=': return value_num <= criteria_num
                        elif op == '<>': return value_num != criteria_num
                        elif op == '>': return value_num > criteria_num
                        elif op == '<': return value_num < criteria_num
                        elif op == '=': return value_num == criteria_num
                    except:
                        return str(value) == criteria_val if op == '=' else str(value) != criteria_val
            # Exact text match
            return str(value) == criteria
        else:
            # Direct value comparison
            return value == criteria
    
    values_to_average = [
        average_range[i] for i in range(len(range_values))
        if meets_criteria(range_values[i], criteria) and isinstance(average_range[i], (int, float))
    ]
    
    if not values_to_average:
        raise ValueError("No values meet the criterion")
    
    return sum(values_to_average) / len(values_to_average)


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
    
    # Parse criteria pairs
    criteria_list = []
    for i in range(0, len(criteria_pairs), 2):
        criteria_range = criteria_pairs[i]
        criterion = criteria_pairs[i + 1]
        if len(criteria_range) != len(average_range):
            raise ValueError("All ranges must have the same length")
        criteria_list.append((criteria_range, criterion))
    
    # Helper function from AVERAGEIF
    def meets_criteria(value, criteria):
        if isinstance(criteria, str):
            for op in ['>=', '<=', '<>', '>', '<', '=']:
                if criteria.startswith(op):
                    criteria_val = criteria[len(op):]
                    try:
                        criteria_num = float(criteria_val)
                        value_num = float(value) if isinstance(value, (int, float)) else 0
                        
                        if op == '>=': return value_num >= criteria_num
                        elif op == '<=': return value_num <= criteria_num
                        elif op == '<>': return value_num != criteria_num
                        elif op == '>': return value_num > criteria_num
                        elif op == '<': return value_num < criteria_num
                        elif op == '=': return value_num == criteria_num
                    except:
                        return str(value) == criteria_val if op == '=' else str(value) != criteria_val
            return str(value) == criteria
        else:
            return value == criteria
    
    # Find values that meet all criteria
    values_to_average = []
    for i in range(len(average_range)):
        if not isinstance(average_range[i], (int, float)):
            continue
        
        all_criteria_met = True
        for criteria_range, criterion in criteria_list:
            if not meets_criteria(criteria_range[i], criterion):
                all_criteria_met = False
                break
        
        if all_criteria_met:
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
    numeric_values = []
    
    for val in values:
        if isinstance(val, (list, tuple)):
            for v in val:
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    numeric_values.append(v)
        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            numeric_values.append(val)
    
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
    
    criteria_list = []
    for i in range(0, len(criteria_pairs), 2):
        criteria_range = criteria_pairs[i]
        criterion = criteria_pairs[i + 1]
        if len(criteria_range) != len(min_range):
            raise ValueError("All ranges must have the same length")
        criteria_list.append((criteria_range, criterion))
    
    def meets_criteria(value, criteria):
        if isinstance(criteria, str):
            for op in ['>=', '<=', '<>', '>', '<', '=']:
                if criteria.startswith(op):
                    criteria_val = criteria[len(op):]
                    try:
                        criteria_num = float(criteria_val)
                        value_num = float(value) if isinstance(value, (int, float)) else 0
                        
                        if op == '>=': return value_num >= criteria_num
                        elif op == '<=': return value_num <= criteria_num
                        elif op == '<>': return value_num != criteria_num
                        elif op == '>': return value_num > criteria_num
                        elif op == '<': return value_num < criteria_num
                        elif op == '=': return value_num == criteria_num
                    except:
                        return str(value) == criteria_val if op == '=' else str(value) != criteria_val
            return str(value) == criteria
        else:
            return value == criteria
    
    values_to_check = []
    for i in range(len(min_range)):
        if not isinstance(min_range[i], (int, float)):
            continue
        
        all_criteria_met = True
        for criteria_range, criterion in criteria_list:
            if not meets_criteria(criteria_range[i], criterion):
                all_criteria_met = False
                break
        
        if all_criteria_met:
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
    numeric_values = []
    
    for val in values:
        if isinstance(val, (list, tuple)):
            for v in val:
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    numeric_values.append(v)
        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            numeric_values.append(val)
    
    if not numeric_values:
        raise ValueError("MEDIAN requires at least one numeric value")
    
    return float(np.median(numeric_values))


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
    
    if not numeric_values:
        raise ValueError("MODE.MULT requires at least one numeric value")
    
    # Count frequencies
    from collections import Counter
    freq = Counter(numeric_values)
    
    # Find maximum frequency
    max_freq = max(freq.values())
    
    if max_freq == 1:
        raise ValueError("No repeated values found")
    
    # Return all values with maximum frequency
    modes = [float(val) for val, count in freq.items() if count == max_freq]
    return sorted(modes)


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
    
    from collections import Counter
    freq = Counter(numeric_values)
    
    max_freq = max(freq.values())
    
    if max_freq == 1:
        raise ValueError("No repeated values found")
    
    # Return first value with maximum frequency (in order of appearance)
    for val in numeric_values:
        if freq[val] == max_freq:
            return float(val)
    
    return float(numeric_values[0])


# Alias for backward compatibility
MODE = MODE_SNGL


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
    return float(1 - stats.chi2.cdf(chi2_stat, df))


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
    var1 = np.var(arr1, ddof=1)
    var2 = np.var(arr2, ddof=1)
    
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
    p_value = 2 * min(stats.f.cdf(f_stat, df1, df2), 1 - stats.f.cdf(f_stat, df1, df2))
    
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
    
    if test_type == 1:
        # Paired t-test
        if len(arr1) != len(arr2):
            raise ValueError("For paired t-test, arrays must have equal length")
        t_stat, p_value = stats.ttest_rel(arr1, arr2)
    elif test_type == 2:
        # Two-sample t-test with equal variances
        t_stat, p_value = stats.ttest_ind(arr1, arr2, equal_var=True)
    else:
        # Two-sample t-test with unequal variances (Welch's t-test)
        t_stat, p_value = stats.ttest_ind(arr1, arr2, equal_var=False)
    
    # Adjust for one-tailed test
    if tails == 1:
        p_value = p_value / 2
    
    return float(p_value)


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
    
    mean = np.mean(arr)
    
    if sigma is None:
        sigma = np.std(arr, ddof=1)
    
    # Calculate z-score
    z = (mean - x) / (sigma / np.sqrt(len(arr)))
    
    # One-tailed p-value
    p_value = 1 - stats.norm.cdf(z)
    
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
    if number_f < 0 or number_s < 1:
        raise ValueError("number_f must be >= 0 and number_s must be >= 1")
    
    if probability_s <= 0 or probability_s >= 1:
        raise ValueError("probability_s must be between 0 and 1 (exclusive)")
    
    if cumulative:
        return float(stats.nbinom.cdf(number_f, number_s, probability_s))
    else:
        return float(stats.nbinom.pmf(number_f, number_s, probability_s))


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
    
    if cumulative:
        return float(stats.norm.cdf(x, mean, standard_dev))
    else:
        return float(stats.norm.pdf(x, mean, standard_dev))


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
    
    return float(stats.norm.ppf(probability, mean, standard_dev))


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
    if cumulative:
        return float(stats.norm.cdf(z))
    else:
        return float(stats.norm.pdf(z))


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
    if probability <= 0 or probability >= 1:
        raise ValueError("Probability must be between 0 and 1 (exclusive)")
    
    return float(stats.norm.ppf(probability))


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
    
    return float(np.percentile(arr, k * 100, method='weibull'))


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
    
    return float(np.percentile(arr, k * 100, method='linear'))


# Alias for backward compatibility
PERCENTILE = PERCENTILE_INC


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
    
    n = len(arr)
    
    # Find position
    if x <= arr[0]:
        rank = 0
    elif x >= arr[-1]:
        rank = 1
    else:
        # Linear interpolation
        for i in range(len(arr) - 1):
            if arr[i] <= x <= arr[i + 1]:
                rank = (i + 1 + (x - arr[i]) / (arr[i + 1] - arr[i])) / (n + 1)
                break
    
    return round(rank, significance)


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


# Alias for backward compatibility
PERCENTRANK = PERCENTRANK_INC


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
    if number < 0 or number_chosen < 0:
        raise ValueError("Arguments must be non-negative")
    
    if number_chosen > number:
        raise ValueError("number_chosen cannot be greater than number")
    
    # P(n,k) = n! / (n-k)!
    result = 1
    for i in range(number, number - number_chosen, -1):
        result *= i
    
    return result


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
    
    # Permutations with repetition = n^k
    return int(number ** number_chosen)


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
    return float(stats.norm.pdf(x))


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
    if x < 0:
        raise ValueError("x must be non-negative")
    
    if mean <= 0:
        raise ValueError("mean must be positive")
    
    if cumulative:
        return float(stats.poisson.cdf(x, mean))
    else:
        return float(stats.poisson.pmf(x, mean))


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
    numeric_values = []
    
    for val in values:
        if isinstance(val, (list, tuple)):
            for v in val:
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    numeric_values.append(v)
        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            numeric_values.append(val)
    
    if len(numeric_values) < 3:
        raise ValueError("SKEW requires at least 3 values")
    
    return float(stats.skew(numeric_values, bias=False))


def SKEW_P(values: List[Union[float, int]]) -> float:
    """
    Returns the skewness of a distribution based on a population.
    
    Excel function: SKEW.P (COEFICIENTE.ASIMETRIA.P in Spanish)
    
    Description:
        Returns the skewness of a distribution based on a population: a
        characterization of the degree of asymmetry of a distribution around its mean.
    
    Args:
        values: Array or range for which you want the skewness
    
    Returns:
        float: Population skewness value
    
    Raises:
        ValueError: If less than 3 values provided
    
    Cost:
        O(n) - Linear time complexity
    
    Usage:
        >>> SKEW_P([3, 4, 5, 2, 3, 4, 5, 6, 4, 7])
        0.303...
    """
    numeric_values = [v for v in values if isinstance(v, (int, float)) and not isinstance(v, bool)]
    
    if len(numeric_values) < 3:
        raise ValueError("SKEW.P requires at least 3 values")
    
    return float(stats.skew(numeric_values, bias=True))


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
    numeric_values = sorted([v for v in array if isinstance(v, (int, float)) and not isinstance(v, bool)])
    
    if not numeric_values:
        raise ValueError("Array must contain at least one numeric value")
    
    if k < 1 or k > len(numeric_values):
        raise ValueError(f"k must be between 1 and {len(numeric_values)}")
    
    return float(numeric_values[k - 1])


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
    if standard_dev <= 0:
        raise ValueError("Standard deviation must be positive")
    
    return (x - mean) / standard_dev


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
    numeric_values = []
    
    for val in values:
        if isinstance(val, (list, tuple)):
            for v in val:
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    numeric_values.append(v)
        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            numeric_values.append(val)
    
    if len(numeric_values) < 1:
        raise ValueError("STDEV.P requires at least one value")
    
    return float(np.std(numeric_values, ddof=0))


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
    numeric_values = []
    
    for val in values:
        if isinstance(val, (list, tuple)):
            for v in val:
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    numeric_values.append(v)
        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            numeric_values.append(val)
    
    if len(numeric_values) < 2:
        raise ValueError("STDEV.S requires at least 2 values")
    
    return float(np.std(numeric_values, ddof=1))


# Alias for backward compatibility
STDEV = STDEV_S


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
    
    if len(converted_values) < 2:
        raise ValueError("STDEVA requires at least 2 values")
    
    return float(np.std(converted_values, ddof=1))


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
    
    if len(converted_values) < 1:
        raise ValueError("STDEVPA requires at least 1 value")
    
    return float(np.std(converted_values, ddof=0))


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
    
    y_arr = np.array([float(v) for v in known_y])
    x_arr = np.array([float(v) for v in known_x])
    
    # Calculate regression
    slope, intercept = np.polyfit(x_arr, y_arr, 1)
    y_pred = slope * x_arr + intercept
    
    # Calculate standard error
    n = len(y_arr)
    sse = np.sum((y_arr - y_pred) ** 2)
    steyx = np.sqrt(sse / (n - 2))
    
    return float(steyx)


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
    if deg_freedom < 1:
        raise ValueError("Degrees of freedom must be at least 1")
    
    if cumulative:
        return float(stats.t.cdf(x, deg_freedom))
    else:
        return float(stats.t.pdf(x, deg_freedom))


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
    if x < 0:
        raise ValueError("x must be non-negative")
    
    if deg_freedom < 1:
        raise ValueError("Degrees of freedom must be at least 1")
    
    return float(2 * (1 - stats.t.cdf(x, deg_freedom)))


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
    if deg_freedom < 1:
        raise ValueError("Degrees of freedom must be at least 1")
    
    return float(1 - stats.t.cdf(x, deg_freedom))


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
    if probability <= 0 or probability >= 1:
        raise ValueError("Probability must be between 0 and 1 (exclusive)")
    
    if deg_freedom < 1:
        raise ValueError("Degrees of freedom must be at least 1")
    
    return float(stats.t.ppf(probability, deg_freedom))


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
    if probability <= 0 or probability >= 1:
        raise ValueError("Probability must be between 0 and 1 (exclusive)")
    
    if deg_freedom < 1:
        raise ValueError("Degrees of freedom must be at least 1")
    
    # Two-tailed: use 1 - probability/2
    return float(stats.t.ppf(1 - probability / 2, deg_freedom))


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
    
    numeric_values = sorted([v for v in array if isinstance(v, (int, float)) and not isinstance(v, bool)])
    
    if not numeric_values:
        raise ValueError("Array must contain at least one numeric value")
    
    n = len(numeric_values)
    
    # Calculate number of points to exclude from each end
    exclude = int(n * fraction / 2)
    
    if exclude * 2 >= n:
        raise ValueError("Fraction too large for the number of data points")
    
    # Trim and calculate mean
    if exclude > 0:
        trimmed = numeric_values[exclude:-exclude]
    else:
        trimmed = numeric_values
    
    return float(np.mean(trimmed))


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
    numeric_values = []
    
    for val in values:
        if isinstance(val, (list, tuple)):
            for v in val:
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    numeric_values.append(v)
        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            numeric_values.append(val)
    
    if len(numeric_values) < 1:
        raise ValueError("VAR.P requires at least one value")
    
    return float(np.var(numeric_values, ddof=0))


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
    numeric_values = []
    
    for val in values:
        if isinstance(val, (list, tuple)):
            for v in val:
                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    numeric_values.append(v)
        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            numeric_values.append(val)
    
    if len(numeric_values) < 2:
        raise ValueError("VAR.S requires at least 2 values")
    
    return float(np.var(numeric_values, ddof=1))


# Alias for backward compatibility
VAR = VAR_S


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
    
    if len(converted_values) < 2:
        raise ValueError("VARA requires at least 2 values")
    
    return float(np.var(converted_values, ddof=1))


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
    
    if len(converted_values) < 1:
        raise ValueError("VARPA requires at least 1 value")
    
    return float(np.var(converted_values, ddof=0))


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
    if x < 0:
        raise ValueError("x must be non-negative")
    
    if alpha <= 0:
        raise ValueError("alpha must be positive")
    
    if beta <= 0:
        raise ValueError("beta must be positive")
    
    # scipy uses (c, scale) where c=alpha (shape) and scale=beta
    if cumulative:
        return float(stats.weibull_min.cdf(x, alpha, scale=beta))
    else:
        return float(stats.weibull_min.pdf(x, alpha, scale=beta))
