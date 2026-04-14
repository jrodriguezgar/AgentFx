"""Numeric Statistics Module.

This module provides comprehensive statistical analysis functions for numeric data,
including measures of central tendency, dispersion, correlation, percentiles,
regression, and advanced statistical summaries.

Key Features:
    - Descriptive statistics (mean, median, mode, range, geometric/harmonic mean)
    - Measures of dispersion (variance, standard deviation, IQR, skewness, kurtosis)
    - Correlation and covariance calculations
    - Percentile and frequency calculations
    - Regression and forecasting (slope, intercept, forecast)
    - Fisher transformation, z-score, confidence intervals
    - Sum of squares computation

Example:
    >>> from formulite.fxNumeric.statistics_functions import calculate_mean, calculate_median
    >>> calculate_mean([1, 2, 3, 4, 5])
    3.0
    >>> calculate_median([1, 2, 3, 4])
    2.5
"""
import math
import statistics
import random as _random_mod
from typing import Any, Dict, List, Optional, Tuple, Union


def _validate_numeric_list(data: list, *, min_length: int = 1) -> None:
    """Validate that *data* is a non-empty list of numbers."""
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if len(data) < min_length:
        raise ValueError(
            "Input list cannot be empty."
            if min_length <= 1
            else f"Input list must contain at least {min_length} elements."
        )
    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")


# Basic Descriptive Statistics
# These functions help summarize and describe the main features of a dataset.

def calculate_frecuency(data: List[Union[int, float]]) -> dict:
    """Calculates the frequency of each value in a list of numbers.

    Args:
        data (List[Union[int, float]]): A list of numeric values.

    Returns:
        dict: A dictionary where keys are unique values and values are their frequencies.

    Raises:
        ValueError: If the list is empty.
        TypeError: If the input is not a list or contains non-numeric values.

    Example:
        >>> calculate_frecuency([1, 2, 2, 3, 3, 3])
        {1: 1, 2: 2, 3: 3}

    **Cost:** O(n), where n is the number of elements in the list.
    """
    _validate_numeric_list(data)

    frecuencia = {}
    for item in data:
        frecuencia[item] = frecuencia.get(item, 0) + 1
    return frecuencia


def calculate_mean(data: List[Union[int, float]]) -> float:
    """
    Calculates the arithmetic mean (average) of a list of numbers.

    The mean is the sum of all values divided by the number of values.
    It's a measure of central tendency.

    Args:
        data (List[Union[int, float]]): A list of numeric values.

    Returns:
        float: The arithmetic mean of the data.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric values.

    Example:
        >>> calculate_mean([1, 2, 3, 4, 5])
        3.0
        >>> calculate_mean([10, 20, 30])
        20.0

    **Cost:** O(n), where n is the number of elements.
    """
    _validate_numeric_list(data)

    return statistics.mean(data)

def calculate_median(data: List[Union[int, float]]) -> Union[int, float]:
    """
    Calculates the median (middle value) of a list of numbers.

    The median is the middle number in a sorted, ascending or descending,
    list of numbers and is a measure of central tendency. If the list
    has an even number of elements, the median is the average of the two
    middle values.

    Args:
        data (List[Union[int, float]]): A list of numeric values.

    Returns:
        Union[int, float]: The median of the data.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric values.

    Example:
        >>> calculate_median([1, 2, 3, 4, 5])
        3
        >>> calculate_median([1, 2, 3, 4])
        2.5

    **Cost:** O(n log n), includes list sorting.
    """
    _validate_numeric_list(data)

    return statistics.median(data)

def calculate_mode(data: List[Union[int, float]]) -> List[Union[int, float]]:
    """
    Calculates the mode(s) of a list of numbers.

    The mode is the value that appears most frequently in a dataset.
    A dataset can have one mode (unimodal), multiple modes (multimodal),
    or no mode if all values appear with the same frequency.

    Args:
        data (List[Union[int, float]]): A list of numeric values.

    Returns:
        List[Union[int, float]]: A list of mode(s). Returns an empty list if no mode.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric values.

    Example:
        >>> calculate_mode([1, 2, 2, 3, 4])
        [2]
        >>> calculate_mode([1, 2, 2, 3, 3, 4])
        [2, 3]
        >>> calculate_mode([1, 2, 3])
        [1, 2, 3] # or similar depending on statistics.mode behavior for unique elements

    **Cost:** O(n), where n is the number of elements.
    """
    _validate_numeric_list(data)

    # statistics.mode raises StatisticsError for multimodal data in older Python versions
    # and returns only one mode. statistics.multimode is preferred.
    return statistics.multimode(data)

def calculate_range(data: List[Union[int, float]]) -> float:
    """
    Calculates the range of a list of numbers.

    The range is the difference between the maximum and minimum values in a dataset.
    It's a simple measure of dispersion.

    Args:
        data (List[Union[int, float]]): A list of numeric values.

    Returns:
        float: The range of the data.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric values.

    Example:
        >>> calculate_range([1, 5, 2, 8, 3])
        7.0
        >>> calculate_range([10, 10, 10])
        0.0

    **Cost:** O(n), searching for maximum and minimum.
    """
    _validate_numeric_list(data)

    return float(max(data) - min(data))


# Measures of Dispersion (Spread)
# These functions quantify how spread out or dispersed the data points are.

def calculate_variance(data: List[Union[int, float]], sample: bool = True) -> float:
    """
    Calculates the variance of a list of numbers.

    Variance measures how far each number in the set is from the mean,
    and therefore from every other number in the set.
    For a **sample**, it's the sum of squared differences from the mean,
    divided by (n-1). For a **population**, it's divided by n.

    Args:
        data (List[Union[int, float]]): A list of numeric values.
        sample (bool, optional): If True, calculates sample variance (divides by n-1).
                                 If False, calculates population variance (divides by n).
                                 Defaults to True.

    Returns:
        float: The variance of the data.

    Raises:
        ValueError: If the input list has fewer than 2 elements for sample variance,
                    or is empty for population variance.
        TypeError: If the input is not a list or contains non-numeric values.

    Example:
        >>> calculate_variance([1, 2, 3, 4, 5]) # Sample variance
        2.5
        >>> calculate_variance([1, 2, 3, 4, 5], sample=False) # Population variance
        2.0

    **Cost:** O(n), variance calculation over the list.
    """
    _validate_numeric_list(data)
    if sample and len(data) < 2:
        raise ValueError("Sample variance requires at least two data points.")

    if sample:
        return statistics.variance(data)
    else:
        return statistics.pvariance(data)


def calculate_standard_deviation(data: List[Union[int, float]], sample: bool = True) -> float:
    """
    Calculates the standard deviation of a list of numbers.

    Standard deviation is the square root of the variance. It's a measure
    of the amount of variation or dispersion of a set of values. A low
    standard deviation indicates that the values tend to be close to the mean
    of the set, while a high standard deviation indicates that the values
    are spread out over a wider range.

    Args:
        data (List[Union[int, float]]): A list of numeric values.
        sample (bool, optional): If True, calculates sample standard deviation.
                                 If False, calculates population standard deviation.
                                 Defaults to True.

    Returns:
        float: The standard deviation of the data.

    Raises:
        ValueError: If the input list has fewer than 2 elements for sample standard deviation,
                    or is empty for population standard deviation.
        TypeError: If the input is not a list or contains non-numeric values.

    Example:
        >>> round(calculate_standard_deviation([1, 2, 3, 4, 5]), 2) # Sample std dev
        1.58
        >>> round(calculate_standard_deviation([1, 2, 3, 4, 5], sample=False), 2) # Population std dev
        1.41

    **Cost:** O(n), standard deviation calculation.
    """
    _validate_numeric_list(data)
    if sample and len(data) < 2:
        raise ValueError("Sample standard deviation requires at least two data points.")

    if sample:
        return statistics.stdev(data)
    else:
        return statistics.pstdev(data)


def calculate_interquartile_range(data: List[Union[int, float]]) -> float:
    """
    Calculates the Interquartile Range (IQR) of a list of numbers.

    The IQR is the range between the first quartile (Q1, 25th percentile)
    and the third quartile (Q3, 75th percentile) of a dataset. It is a
    measure of statistical dispersion, representing the middle 50% of the data.

    Args:
        data (List[Union[int, float]]): A list of numeric values.

    Returns:
        float: The Interquartile Range (IQR).

    Raises:
        ValueError: If the input list has fewer than 4 elements.
        TypeError: If the input is not a list or contains non-numeric values.

    Example:
        >>> calculate_interquartile_range([1, 2, 3, 4, 5, 6, 7, 8, 9])
        4.0
        >>> calculate_interquartile_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        5.0

    **Cost:** O(n log n), includes list sorting.
    """
    _validate_numeric_list(data, min_length=4)

    # Sort the data to find quartiles
    sorted_data = sorted(data)
    n = len(sorted_data)

    # Calculate Q1 (25th percentile) and Q3 (75th percentile)
    # Using the inclusive method (equivalent to numpy.percentile with interpolation='linear')
    q1_index = (n + 1) / 4 - 1
    q3_index = 3 * (n + 1) / 4 - 1

    # Linear interpolation for quartiles if index is not an integer
    def get_percentile_value(sorted_list, index):
        if index == int(index):
            return sorted_list[int(index)]
        else:
            lower_index = int(index)
            upper_index = lower_index + 1
            # Handle cases where upper_index might be out of bounds for very small datasets (though already handled by len(data) < 4 check)
            if upper_index >= len(sorted_list):
                 return sorted_list[lower_index] # Fallback for edge case, though ideally wouldn't hit this
            fraction = index - lower_index
            return sorted_list[lower_index] + fraction * (sorted_list[upper_index] - sorted_list[lower_index])

    q1 = get_percentile_value(sorted_data, q1_index)
    q3 = get_percentile_value(sorted_data, q3_index)

    return q3 - q1


# Correlation and Covariance
# These functions measure the relationship between two variables.

def calculate_covariance(data1: List[Union[int, float]], data2: List[Union[int, float]], sample: bool = True) -> float:
    """
    Calculates the covariance between two lists of numbers.

    Covariance measures how two variables change together. A positive covariance
    indicates that the variables tend to move in the same direction, while a
    negative covariance indicates they tend to move in opposite directions.

    Args:
        data1 (List[Union[int, float]]): The first list of numeric values.
        data2 (List[Union[int, float]]): The second list of numeric values.
        sample (bool, optional): If True, calculates sample covariance (divides by n-1).
                                 If False, calculates population covariance (divides by n).
                                 Defaults to True.

    Returns:
        float: The covariance between the two datasets.

    Raises:
        ValueError: If lists are of different lengths or have fewer than 2 elements for sample covariance.
        TypeError: If inputs are not lists or contain non-numeric values.

    Example:
        >>> calculate_covariance([1, 2, 3], [2, 4, 6]) # Positive correlation
        2.0
        >>> calculate_covariance([1, 2, 3], [6, 4, 2]) # Negative correlation
        -2.0

    **Cost:** O(n), where n is the length of the lists.
    """
    if not isinstance(data1, list) or not isinstance(data2, list):
        raise TypeError("Inputs 'data1' and 'data2' must be lists.")
    if len(data1) != len(data2):
        raise ValueError("Input lists must have the same length.")
    if not data1: # Implies data2 is also empty
        raise ValueError("Input lists cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data1) or \
       not all(isinstance(item, (int, float)) for item in data2):
        raise TypeError("All elements in both 'data' lists must be numeric (int or float).")
    if sample and len(data1) < 2:
        raise ValueError("Sample covariance requires at least two data points.")

    n = len(data1)
    mean1 = calculate_mean(data1)
    mean2 = calculate_mean(data2)

    sum_of_products = sum([(data1[i] - mean1) * (data2[i] - mean2) for i in range(n)])

    if sample:
        if n - 1 == 0:
            raise ValueError("Cannot calculate sample covariance for a single data point (division by zero).")
        return sum_of_products / (n - 1)
    else:
        return sum_of_products / n


def calculate_pearson_correlation(data1: List[Union[int, float]], data2: List[Union[int, float]]) -> float:
    """
    Calculates the Pearson product-moment correlation coefficient between two lists of numbers.

    Pearson correlation measures the linear relationship between two datasets.
    Its value ranges from -1 to 1.
    - +1 indicates a perfect positive linear relationship.
    - -1 indicates a perfect negative linear relationship.
    - 0 indicates no linear relationship.

    Args:
        data1 (List[Union[int, float]]): The first list of numeric values.
        data2 (List[Union[int, float]]): The second list of numeric values.

    Returns:
        float: The Pearson correlation coefficient.

    Raises:
        ValueError: If lists are of different lengths or have insufficient data points (less than 2).
                    Also if standard deviation is zero (no variance in one of the datasets).
        TypeError: If inputs are not lists or contain non-numeric values.

    Example:
        >>> calculate_pearson_correlation([1, 2, 3], [2, 4, 6])
        1.0
        >>> calculate_pearson_correlation([1, 2, 3], [6, 4, 2])
        -1.0
        >>> round(calculate_pearson_correlation([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), 10)
        -1.0

    **Cost:** O(n), correlation calculation.
    """
    if not isinstance(data1, list) or not isinstance(data2, list):
        raise TypeError("Inputs 'data1' and 'data2' must be lists.")
    if len(data1) != len(data2):
        raise ValueError("Input lists must have the same length.")
    if len(data1) < 2:
        raise ValueError("Pearson correlation requires at least two data points.")
    if not all(isinstance(item, (int, float)) for item in data1) or \
       not all(isinstance(item, (int, float)) for item in data2):
        raise TypeError("All elements in both 'data' lists must be numeric (int or float).")

    try:
        std_dev1 = calculate_standard_deviation(data1, sample=True)
        std_dev2 = calculate_standard_deviation(data2, sample=True)
    except ValueError as e:
        raise ValueError(f"Cannot calculate correlation: {e}. "
                         "This often happens if one dataset has zero variance (all values are the same).")

    if std_dev1 == 0 or std_dev2 == 0:
        # If one of the standard deviations is zero, it means all values in that list are the same.
        # In such cases, the correlation is undefined or often considered 0.
        # For perfectly identical and constant data, it can be 1 or -1 if the other is also constant.
        # However, for non-varying data, the Pearson formula involves division by zero.
        # It's better to explicitly raise an error or return 0, depending on the desired behavior.
        # Here, we'll raise an error as it implies no linear relationship can be measured.
        raise ValueError("Cannot calculate Pearson correlation if standard deviation of either dataset is zero (all values are the same).")

    cov = calculate_covariance(data1, data2, sample=True)
    return cov / (std_dev1 * std_dev2)


# Percentiles and Quantiles
# Functions to find specific points in a dataset that divide it into segments.

def calculate_percentile(data: List[Union[int, float]], percentile: float) -> float:
    """
    Calculates the specified percentile of a list of numbers.

    A percentile indicates the value below which a given percentage of
    observations in a group of observations falls. For example, the 90th
    percentile is the value below which 90% of the observations may be found.

    Args:
        data (List[Union[int, float]]): A list of numeric values.
        percentile (float): The desired percentile, a value between 0 and 100.

    Returns:
        float: The value at the specified percentile.

    Raises:
        ValueError: If the input list is empty, or if percentile is out of range [0, 100].
        TypeError: If the input is not a list or contains non-numeric values, or if percentile is not numeric.

    Example:
        >>> calculate_percentile([10, 20, 30, 40, 50], 50) # Median
        30.0
        >>> calculate_percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 90)
        9.0

    **Cost:** O(n log n), includes sorting to calculate percentile.
    """
    _validate_numeric_list(data)
    if not isinstance(percentile, (int, float)):
        raise TypeError("'percentile' must be a numeric value.")
    if not (0 <= percentile <= 100):
        raise ValueError("Percentile must be between 0 and 100.")

    sorted_data = sorted(data)
    n = len(sorted_data)
    # Calculate the rank (index) for the percentile
    # Using the standard method where Pth percentile is the element at (N * P / 100)
    # The formula (percentile / 100) * (n - 1) gives the 0-indexed position.
    # We add 1 to make it 1-indexed for the 'rank' concept.
    rank = (percentile / 100.0) * (n - 1)

    lower_index = int(math.floor(rank))
    upper_index = int(math.ceil(rank))

    # If the percentile falls exactly on an integer index
    if lower_index == upper_index:
        return float(sorted_data[lower_index])
    else:
        # Interpolate if the percentile falls between two data points
        lower_value = sorted_data[lower_index]
        upper_value = sorted_data[upper_index]
        interpolation_fraction = rank - lower_index
        return lower_value + (upper_value - lower_value) * interpolation_fraction
    

# Helper Functions (Internal Use or General Utility)
# While not strictly "statistical functions" in themselves, these are often used in statistical calculations.

def sum_of_squares(data: List[Union[int, float]]) -> float:
    """
    Calculates the sum of squares of a list of numbers.

    The sum of squares is a fundamental component in many statistical formulas,
    such as variance and standard deviation. It represents the sum of the
    squared differences of each data point from the mean.

    Args:
        data (List[Union[int, float]]): A list of numeric values.

    Returns:
        float: The sum of squares.

    Raises:
        ValueError: If the input list is empty.
        TypeError: If the input is not a list or contains non-numeric values.

    Example:
        >>> sum_of_squares([1, 2, 3, 4, 5])
        10.0
        >>> sum_of_squares([1, 1, 1])
        0.0

    **Cost:** O(n), sum of squares over the list.
    """
    _validate_numeric_list(data)

    mean_value = calculate_mean(data)
    return sum([(x - mean_value) ** 2 for x in data])


# ============================================================================
# CUMULATIVE FUNCTIONS
# ============================================================================


def cumulative_sum(data: List[Union[int, float]]) -> List[float]:
    """Returns the running cumulative sum of a list.

    Args:
        data: A list of numeric values.

    Returns:
        A list of the same length with cumulative sums.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> cumulative_sum([1, 2, 3, 4])
        [1, 3, 6, 10]

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    result: List[float] = []
    acc = 0.0

    for v in data:
        acc += v
        result.append(acc)

    return result


def cumulative_product(data: List[Union[int, float]]) -> List[float]:
    """Returns the running cumulative product of a list.

    Args:
        data: A list of numeric values.

    Returns:
        A list of the same length with cumulative products.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> cumulative_product([1, 2, 3, 4])
        [1, 2, 6, 24]

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    result: List[float] = []
    acc = 1.0

    for v in data:
        acc *= v
        result.append(acc)

    return result


def cumulative_max(data: List[Union[int, float]]) -> List[float]:
    """Returns the running cumulative maximum of a list.

    Args:
        data: A list of numeric values.

    Returns:
        A list of the same length with cumulative maxima.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> cumulative_max([3, 1, 4, 1, 5])
        [3, 3, 4, 4, 5]

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    result: List[float] = []
    current_max = float("-inf")

    for v in data:

        if v > current_max:
            current_max = v

        result.append(float(current_max))

    return result


def cumulative_min(data: List[Union[int, float]]) -> List[float]:
    """Returns the running cumulative minimum of a list.

    Args:
        data: A list of numeric values.

    Returns:
        A list of the same length with cumulative minima.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> cumulative_min([3, 1, 4, 1, 5])
        [3, 1, 1, 1, 1]

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    result: List[float] = []
    current_min = float("inf")

    for v in data:

        if v < current_min:
            current_min = v

        result.append(float(current_min))

    return result


# ============================================================================
# ROLLING / WINDOW FUNCTIONS
# ============================================================================


def rolling_mean(data: List[Union[int, float]], window: int) -> List[Optional[float]]:
    """Calculates the rolling (moving) average over a fixed window size.

    The first ``window - 1`` positions are ``None`` (insufficient data).

    Args:
        data: A list of numeric values.
        window: Number of consecutive elements per window (must be >= 1).

    Returns:
        A list of the same length; each entry is the mean of the preceding
        *window* elements or ``None`` when not enough data exists.

    Raises:
        TypeError: If input is not a list of numbers or window is not int.
        ValueError: If the list is empty or window < 1.

    Example:
        >>> rolling_mean([1, 2, 3, 4, 5], 3)
        [None, None, 2.0, 3.0, 4.0]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not isinstance(window, int):
        raise TypeError("'window' must be an integer.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if window < 1:
        raise ValueError("'window' must be >= 1.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements must be numeric.")

    result: List[Optional[float]] = [None] * (window - 1)
    window_sum = sum(data[:window])
    result.append(window_sum / window)

    for i in range(window, len(data)):
        window_sum += data[i] - data[i - window]
        result.append(window_sum / window)

    return result


def rolling_sum(data: List[Union[int, float]], window: int) -> List[Optional[float]]:
    """Calculates the rolling (moving) sum over a fixed window size.

    The first ``window - 1`` positions are ``None`` (insufficient data).

    Args:
        data: A list of numeric values.
        window: Number of consecutive elements per window (must be >= 1).

    Returns:
        A list of the same length; each entry is the sum of the preceding
        *window* elements or ``None`` when not enough data exists.

    Raises:
        TypeError: If input is not a list of numbers or window is not int.
        ValueError: If the list is empty or window < 1.

    Example:
        >>> rolling_sum([1, 2, 3, 4, 5], 3)
        [None, None, 6.0, 9.0, 12.0]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not isinstance(window, int):
        raise TypeError("'window' must be an integer.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if window < 1:
        raise ValueError("'window' must be >= 1.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements must be numeric.")

    result: List[Optional[float]] = [None] * (window - 1)
    window_sum = sum(data[:window])
    result.append(float(window_sum))

    for i in range(window, len(data)):
        window_sum += data[i] - data[i - window]
        result.append(float(window_sum))

    return result


# ============================================================================
# SERIES / WINDOW ANALYSIS
# ============================================================================


def diff(data: List[Union[int, float]], periods: int = 1) -> List[Optional[float]]:
    """Calculates consecutive differences in a list (like pandas Series.diff).

    Args:
        data: A list of numeric values.
        periods: Number of positions to shift for the difference (default 1).

    Returns:
        A list of the same length. The first *periods* entries are ``None``.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty or periods < 1.

    Example:
        >>> diff([1, 3, 6, 10])
        [None, 2.0, 3.0, 4.0]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if not isinstance(periods, int) or periods < 1:
        raise ValueError("'periods' must be an integer >= 1.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements must be numeric.")

    result: List[Optional[float]] = [None] * periods

    for i in range(periods, len(data)):
        result.append(float(data[i] - data[i - periods]))

    return result


def lag(data: List[Any], periods: int = 1, default: Any = None) -> List[Any]:
    """Shifts values forward (access previous values), like SQL LAG.

    Args:
        data: A list of values.
        periods: Number of positions to lag (default 1).
        default: Value to fill for positions without a predecessor.

    Returns:
        A list of the same length, shifted forward.

    Raises:
        TypeError: If input is not a list.
        ValueError: If periods < 1.

    Example:
        >>> lag([10, 20, 30, 40], 1)
        [None, 10, 20, 30]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not isinstance(periods, int) or periods < 1:
        raise ValueError("'periods' must be an integer >= 1.")

    if periods >= len(data):
        return [default] * len(data)

    return [default] * periods + data[:-periods]


def lead(data: List[Any], periods: int = 1, default: Any = None) -> List[Any]:
    """Shifts values backward (access subsequent values), like SQL LEAD.

    Args:
        data: A list of values.
        periods: Number of positions to lead (default 1).
        default: Value to fill for positions without a successor.

    Returns:
        A list of the same length, shifted backward.

    Raises:
        TypeError: If input is not a list.
        ValueError: If periods < 1.

    Example:
        >>> lead([10, 20, 30, 40], 1)
        [20, 30, 40, None]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not isinstance(periods, int) or periods < 1:
        raise ValueError("'periods' must be an integer >= 1.")

    if periods >= len(data):
        return [default] * len(data)

    return data[periods:] + [default] * periods


def argmax(data: List[Union[int, float]]) -> int:
    """Returns the index of the maximum value in a list.

    Args:
        data: A list of numeric values.

    Returns:
        Zero-based index of the first maximum value.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> argmax([3, 1, 4, 1, 5, 9])
        5

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    max_val = data[0]
    max_idx = 0

    for i, v in enumerate(data):

        if v > max_val:
            max_val = v
            max_idx = i

    return max_idx


def argmin(data: List[Union[int, float]]) -> int:
    """Returns the index of the minimum value in a list.

    Args:
        data: A list of numeric values.

    Returns:
        Zero-based index of the first minimum value.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> argmin([3, 1, 4, 1, 5, 9])
        1

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    min_val = data[0]
    min_idx = 0

    for i, v in enumerate(data):

        if v < min_val:
            min_val = v
            min_idx = i

    return min_idx


# ============================================================================
# DATA CLEANING
# ============================================================================


def fillna(data: List[Any], value: Any = 0) -> List[Any]:
    """Replaces None values in a list with a specified fill value.

    Args:
        data: A list that may contain None values.
        value: The replacement value (default 0).

    Returns:
        A new list with None values replaced.

    Raises:
        TypeError: If input is not a list.

    Example:
        >>> fillna([1, None, 3, None, 5])
        [1, 0, 3, 0, 5]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    return [value if v is None else v for v in data]


def ffill(data: List[Any]) -> List[Any]:
    """Forward-fills None values with the last non-None value.

    Args:
        data: A list that may contain None values.

    Returns:
        A new list with None values replaced by the previous non-None value.

    Raises:
        TypeError: If input is not a list.

    Example:
        >>> ffill([1, None, None, 4, None])
        [1, 1, 1, 4, 4]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    result: List[Any] = []
    last_valid = None

    for v in data:

        if v is not None:
            last_valid = v

        result.append(last_valid)

    return result


def bfill(data: List[Any]) -> List[Any]:
    """Backward-fills None values with the next non-None value.

    Args:
        data: A list that may contain None values.

    Returns:
        A new list with None values replaced by the next non-None value.

    Raises:
        TypeError: If input is not a list.

    Example:
        >>> bfill([None, None, 3, None, 5])
        [3, 3, 3, 5, 5]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    result: List[Any] = list(data)
    next_valid = None

    for i in range(len(result) - 1, -1, -1):

        if result[i] is not None:
            next_valid = result[i]
        else:
            result[i] = next_valid

    return result


# ============================================================================
# RANKING
# ============================================================================


def rank(data: List[Union[int, float]], method: str = "average",
         ascending: bool = True) -> List[float]:
    """Assigns a rank to each value in a list.

    Args:
        data: A list of numeric values.
        method: How to handle ties — ``"average"``, ``"min"``, ``"max"``,
            ``"dense"``, or ``"ordinal"``.
        ascending: If ``True`` (default) smallest value gets rank 1.

    Returns:
        A list of floats with the rank for each position.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty or method is invalid.

    Example:
        >>> rank([40, 10, 30, 20])
        [4.0, 1.0, 3.0, 2.0]

        >>> rank([10, 20, 20, 30], method="min")
        [1.0, 2.0, 2.0, 4.0]

    Complexity: O(n log n)
    """
    valid_methods = ("average", "min", "max", "dense", "ordinal")

    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if method not in valid_methods:
        raise ValueError(f"method must be one of {valid_methods}")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements must be numeric.")

    indexed = list(enumerate(data))
    indexed.sort(key=lambda x: x[1], reverse=not ascending)

    ranks = [0.0] * len(data)

    if method == "ordinal":

        for rank_pos, (orig_idx, _) in enumerate(indexed, 1):
            ranks[orig_idx] = float(rank_pos)

        return ranks

    if method == "dense":
        sorted_unique = sorted(set(data), reverse=not ascending)
        value_to_rank = {v: float(r + 1) for r, v in enumerate(sorted_unique)}
        return [value_to_rank[v] for v in data]

    i = 0

    while i < len(indexed):
        j = i

        while j < len(indexed) and indexed[j][1] == indexed[i][1]:
            j += 1

        if method == "average":
            avg_rank = (i + 1 + j) / 2.0

            for k in range(i, j):
                ranks[indexed[k][0]] = avg_rank

        elif method == "min":

            for k in range(i, j):
                ranks[indexed[k][0]] = float(i + 1)

        elif method == "max":

            for k in range(i, j):
                ranks[indexed[k][0]] = float(j)

        i = j

    return ranks


# ============================================================================
# DESCRIPTIVE SUMMARY
# ============================================================================


def describe(data: List[Union[int, float]]) -> dict:
    """Returns a summary of descriptive statistics for a list (like pandas describe).

    Args:
        data: A list of numeric values.

    Returns:
        A dict with keys: ``count``, ``mean``, ``std``, ``min``, ``25%``,
        ``50%`` (median), ``75%``, ``max``.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> result = describe([1, 2, 3, 4, 5])
        >>> result["count"]
        5
        >>> result["mean"]
        3.0

    Complexity: O(n log n)
    """
    _validate_numeric_list(data)

    sorted_data = sorted(data)
    n = len(sorted_data)

    def _percentile(pct: float) -> float:
        idx = (pct / 100.0) * (n - 1)
        lo = int(math.floor(idx))
        hi = int(math.ceil(idx))

        if lo == hi:
            return float(sorted_data[lo])

        return sorted_data[lo] + (sorted_data[hi] - sorted_data[lo]) * (idx - lo)

    mean_val = statistics.mean(data)
    std_val = statistics.stdev(data) if n > 1 else 0.0

    return {
        "count": n,
        "mean": mean_val,
        "std": std_val,
        "min": sorted_data[0],
        "25%": _percentile(25),
        "50%": _percentile(50),
        "75%": _percentile(75),
        "max": sorted_data[-1],
    }


# ============================================================================
# ADVANCED STATISTICAL FUNCTIONS
# ============================================================================


def geometric_mean(data: List[Union[int, float]]) -> float:
    """Calculates the geometric mean of a list of positive numbers.

    Args:
        data: A list of positive numeric values.

    Returns:
        The geometric mean.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty or contains non-positive values.

    Example:
        >>> geometric_mean([2, 8])
        4.0
        >>> round(geometric_mean([1, 3, 9, 27]), 6)
        5.196152

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

    if any(x <= 0 for x in data):
        raise ValueError("All values must be positive for geometric mean.")

    return statistics.geometric_mean(data)


def harmonic_mean(data: List[Union[int, float]]) -> float:
    """Calculates the harmonic mean of a list of positive numbers.

    Args:
        data: A list of positive numeric values.

    Returns:
        The harmonic mean.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty or contains non-positive values.

    Example:
        >>> harmonic_mean([1, 4, 4])
        2.0
        >>> round(harmonic_mean([2, 3, 6]), 6)
        3.0

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

    if any(x <= 0 for x in data):
        raise ValueError("All values must be positive for harmonic mean.")

    return statistics.harmonic_mean(data)


def trimmed_mean(data: List[Union[int, float]], percent: float) -> float:
    """Calculates the mean excluding a percentage of outliers from each end.

    Args:
        data: A list of numeric values.
        percent: Fraction of data to exclude from each end (0 to 0.5).

    Returns:
        The trimmed mean.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty or percent is out of range.

    Example:
        >>> trimmed_mean([1, 2, 3, 4, 100], 0.2)
        3.0

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

    if not (0 <= percent < 0.5):
        raise ValueError("Percent must be between 0 and 0.5 (exclusive).")

    sorted_data = sorted(data)
    n = len(sorted_data)
    trim_count = int(n * percent)

    if trim_count == 0:
        trimmed = sorted_data
    else:
        trimmed = sorted_data[trim_count:-trim_count]

    if not trimmed:
        raise ValueError("Too many values trimmed; no data remaining.")

    return statistics.mean(trimmed)


def weighted_mean(data: List[Union[int, float]], weights: List[Union[int, float]]) -> float:
    """Calculates the weighted arithmetic mean of a list of numbers.

    Args:
        data: A list of numeric values.
        weights: A list of corresponding weights (must be positive).

    Returns:
        The weighted mean.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists differ in length, are empty, or weights are non-positive.

    Example:
        >>> weighted_mean([80, 90], [3, 7])
        87.0
        >>> weighted_mean([10, 20, 30], [1, 1, 1])
        20.0

    Complexity: O(n)
    """
    if not isinstance(data, list) or not isinstance(weights, list):
        raise TypeError("Both 'data' and 'weights' must be lists.")

    if not data:
        raise ValueError("Input lists cannot be empty.")

    if len(data) != len(weights):
        raise ValueError("'data' and 'weights' must have the same length.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric.")

    if not all(isinstance(w, (int, float)) for w in weights):
        raise TypeError("All elements in 'weights' must be numeric.")

    if any(w <= 0 for w in weights):
        raise ValueError("All weights must be positive.")

    total_weight = sum(weights)
    return sum(d * w for d, w in zip(data, weights)) / total_weight


def average_deviation(data: List[Union[int, float]]) -> float:
    """Calculates the average of absolute deviations from the mean.

    Args:
        data: A list of numeric values.

    Returns:
        The average absolute deviation.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> average_deviation([2, 3, 4, 5, 6])
        1.2

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    mean_val = statistics.mean(data)
    return sum(abs(x - mean_val) for x in data) / len(data)


def deviation_squared(data: List[Union[int, float]]) -> float:
    """Calculates the sum of squared deviations from the mean.

    Args:
        data: A list of numeric values.

    Returns:
        Sum of squared deviations.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> deviation_squared([2, 5, 8])
        18.0

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    mean_val = statistics.mean(data)
    return sum((x - mean_val) ** 2 for x in data)


def kurtosis(data: List[Union[int, float]], excess: bool = True) -> float:
    """Calculates the kurtosis of a dataset.

    Kurtosis measures the "tailedness" of a probability distribution.
    Excess kurtosis subtracts 3 so that a normal distribution has kurtosis 0.

    Args:
        data: A list of numeric values (at least 4 elements).
        excess: If True, returns excess kurtosis (Fisher). Default True.

    Returns:
        The kurtosis value.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list has fewer than 4 elements or zero variance.

    Example:
        >>> round(kurtosis([1, 2, 3, 4, 5]), 4)
        -1.3

    Complexity: O(n)
    """
    _validate_numeric_list(data, min_length=4)

    n = len(data)
    mean_val = statistics.mean(data)
    std_val = statistics.pstdev(data)

    if std_val == 0:
        raise ValueError("Cannot compute kurtosis when standard deviation is zero.")

    m4 = sum((x - mean_val) ** 4 for x in data) / n
    kurt = m4 / (std_val ** 4)

    if excess:
        kurt -= 3.0

    return kurt


def skewness(data: List[Union[int, float]]) -> float:
    """Calculates the skewness of a dataset.

    Skewness measures the asymmetry of the probability distribution.
    A positive value indicates a right-skewed tail, negative indicates left-skewed.

    Args:
        data: A list of numeric values (at least 3 elements).

    Returns:
        The skewness value.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list has fewer than 3 elements or zero variance.

    Example:
        >>> round(skewness([1, 2, 3, 4, 100]), 4)
        2.0076

    Complexity: O(n)
    """
    _validate_numeric_list(data, min_length=3)

    n = len(data)
    mean_val = statistics.mean(data)
    std_val = statistics.pstdev(data)

    if std_val == 0:
        raise ValueError("Cannot compute skewness when standard deviation is zero.")

    m3 = sum((x - mean_val) ** 3 for x in data) / n
    return m3 / (std_val ** 3)


def large(data: List[Union[int, float]], k: int) -> Union[int, float]:
    """Returns the k-th largest value in a dataset.

    Args:
        data: A list of numeric values.
        k: The rank (1 = largest, 2 = second largest, etc.).

    Returns:
        The k-th largest value.

    Raises:
        TypeError: If input is not a list of numbers or k is not int.
        ValueError: If the list is empty or k is out of range.

    Example:
        >>> large([3, 1, 4, 1, 5, 9], 1)
        9
        >>> large([3, 1, 4, 1, 5, 9], 3)
        4

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not isinstance(k, int):
        raise TypeError("'k' must be an integer.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

    if k < 1 or k > len(data):
        raise ValueError(f"'k' must be between 1 and {len(data)}.")

    return sorted(data, reverse=True)[k - 1]


def small(data: List[Union[int, float]], k: int) -> Union[int, float]:
    """Returns the k-th smallest value in a dataset.

    Args:
        data: A list of numeric values.
        k: The rank (1 = smallest, 2 = second smallest, etc.).

    Returns:
        The k-th smallest value.

    Raises:
        TypeError: If input is not a list of numbers or k is not int.
        ValueError: If the list is empty or k is out of range.

    Example:
        >>> small([3, 1, 4, 1, 5, 9], 1)
        1
        >>> small([3, 1, 4, 1, 5, 9], 3)
        3

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not isinstance(k, int):
        raise TypeError("'k' must be an integer.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

    if k < 1 or k > len(data):
        raise ValueError(f"'k' must be between 1 and {len(data)}.")

    return sorted(data)[k - 1]


# ============================================================================
# REGRESSION & FORECASTING
# ============================================================================


def slope(known_y: List[Union[int, float]], known_x: List[Union[int, float]]) -> float:
    """Calculates the slope of the linear regression line.

    Args:
        known_y: Dependent data values.
        known_x: Independent data values.

    Returns:
        The slope (m) of the best-fit line y = mx + b.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists differ in length, have < 2 elements, or x has zero variance.

    Example:
        >>> slope([2, 4, 6], [1, 2, 3])
        2.0

    Complexity: O(n)
    """
    if not isinstance(known_y, list) or not isinstance(known_x, list):
        raise TypeError("Inputs must be lists.")

    if len(known_y) != len(known_x):
        raise ValueError("Input lists must have the same length.")

    if len(known_y) < 2:
        raise ValueError("At least 2 data points are required.")

    if not all(isinstance(x, (int, float)) for x in known_y + known_x):
        raise TypeError("All elements must be numeric.")

    n = len(known_x)
    mean_x = sum(known_x) / n
    mean_y = sum(known_y) / n

    numerator = sum((known_x[i] - mean_x) * (known_y[i] - mean_y) for i in range(n))
    denominator = sum((known_x[i] - mean_x) ** 2 for i in range(n))

    if denominator == 0:
        raise ValueError("Cannot compute slope: x values have zero variance.")

    return numerator / denominator


def intercept(known_y: List[Union[int, float]], known_x: List[Union[int, float]]) -> float:
    """Calculates the y-intercept of the linear regression line.

    Args:
        known_y: Dependent data values.
        known_x: Independent data values.

    Returns:
        The y-intercept (b) of the best-fit line y = mx + b.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists differ in length or have < 2 elements.

    Example:
        >>> intercept([2, 4, 6], [1, 2, 3])
        0.0

    Complexity: O(n)
    """
    m = slope(known_y, known_x)
    n = len(known_x)
    mean_x = sum(known_x) / n
    mean_y = sum(known_y) / n
    return mean_y - m * mean_x


def forecast_linear(x: Union[int, float], known_y: List[Union[int, float]],
                    known_x: List[Union[int, float]]) -> float:
    """Predicts a value using linear regression.

    Args:
        x: The independent value for which to predict y.
        known_y: Known dependent data values.
        known_x: Known independent data values.

    Returns:
        The predicted y value.

    Raises:
        TypeError: If inputs are invalid.
        ValueError: If data is insufficient.

    Example:
        >>> forecast_linear(4, [2, 4, 6], [1, 2, 3])
        8.0

    Complexity: O(n)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("'x' must be numeric.")

    m = slope(known_y, known_x)
    b = intercept(known_y, known_x)
    return m * x + b


# ============================================================================
# TRANSFORMATIONS & STANDARDIZATION
# ============================================================================


def fisher(x: float) -> float:
    """Calculates the Fisher transformation.

    Transforms a Pearson correlation coefficient into a normally distributed variable.

    Args:
        x: A value in the range (-1, 1).

    Returns:
        The Fisher transformation value.

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x is not in (-1, 1).

    Example:
        >>> round(fisher(0.75), 6)
        0.972955

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("Input must be numeric.")

    if x <= -1 or x >= 1:
        raise ValueError("Input must be in the open interval (-1, 1).")

    from formulite.fxNumeric.trigonometry_functions import inverse_hyperbolic_tangent

    return inverse_hyperbolic_tangent(x)


def fisher_inv(y: float) -> float:
    """Calculates the inverse Fisher transformation.

    Converts a Fisher-transformed value back to a correlation coefficient.

    Args:
        y: A Fisher-transformed value.

    Returns:
        The corresponding correlation coefficient in (-1, 1).

    Raises:
        TypeError: If y is not numeric.

    Example:
        >>> round(fisher_inv(0.972955), 6)
        0.75

    Complexity: O(1)
    """
    if not isinstance(y, (int, float)):
        raise TypeError("Input must be numeric.")

    e2y = math.exp(2 * y)
    return (e2y - 1) / (e2y + 1)


def confidence_norm(alpha: float, standard_dev: float, size: int) -> float:
    """Calculates the confidence interval half-width using the normal distribution.

    Args:
        alpha: Significance level (e.g. 0.05 for 95% confidence).
        standard_dev: Population standard deviation.
        size: Sample size.

    Returns:
        The margin of error (half-width of the confidence interval).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If alpha is not in (0, 1), standard_dev <= 0, or size < 1.

    Example:
        >>> round(confidence_norm(0.05, 2.5, 50), 6)
        0.692952

    Complexity: O(1)
    """
    if not isinstance(alpha, (int, float)):
        raise TypeError("'alpha' must be numeric.")

    if not isinstance(standard_dev, (int, float)):
        raise TypeError("'standard_dev' must be numeric.")

    if not isinstance(size, int):
        raise TypeError("'size' must be an integer.")

    if not (0 < alpha < 1):
        raise ValueError("'alpha' must be between 0 and 1 (exclusive).")

    if standard_dev <= 0:
        raise ValueError("'standard_dev' must be positive.")

    if size < 1:
        raise ValueError("'size' must be at least 1.")

    from statistics import NormalDist
    z = NormalDist().inv_cdf(1 - alpha / 2)
    return z * (standard_dev / math.sqrt(size))


def confidence_t(alpha: float, standard_dev: float, size: int) -> float:
    """Calculates the confidence interval half-width using the Student's t-distribution.

    Requires scipy for the t-distribution inverse CDF. Falls back to normal
    approximation if scipy is unavailable.

    Args:
        alpha: Significance level (e.g. 0.05 for 95% confidence).
        standard_dev: Sample standard deviation.
        size: Sample size.

    Returns:
        The margin of error (half-width of the confidence interval).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If alpha is not in (0, 1), standard_dev <= 0, or size < 2.

    Example:
        >>> round(confidence_t(0.05, 2.5, 50), 4)
        0.7091

    Complexity: O(1)
    """
    if not isinstance(alpha, (int, float)):
        raise TypeError("'alpha' must be numeric.")

    if not isinstance(standard_dev, (int, float)):
        raise TypeError("'standard_dev' must be numeric.")

    if not isinstance(size, int):
        raise TypeError("'size' must be an integer.")

    if not (0 < alpha < 1):
        raise ValueError("'alpha' must be between 0 and 1 (exclusive).")

    if standard_dev <= 0:
        raise ValueError("'standard_dev' must be positive.")

    if size < 2:
        raise ValueError("'size' must be at least 2 for t-distribution.")

    try:
        from scipy.stats import t as t_dist
        t_val = t_dist.ppf(1 - alpha / 2, df=size - 1)
    except ImportError:
        from statistics import NormalDist
        t_val = NormalDist().inv_cdf(1 - alpha / 2)

    return t_val * (standard_dev / math.sqrt(size))


def frequency_bins(data: List[Union[int, float]],
                   bins: List[Union[int, float]]) -> List[int]:
    """Calculates frequency distribution of data across bin boundaries.

    Returns how many values fall in each bin. The result has len(bins) + 1
    elements: values <= bins[0], between bins[0] and bins[1], ..., > bins[-1].

    Args:
        data: A list of numeric values.
        bins: A sorted list of bin upper boundaries.

    Returns:
        A list of counts per bin.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If data is empty.

    Example:
        >>> frequency_bins([1, 2, 3, 4, 5, 6], [2, 4])
        [2, 2, 2]

    Complexity: O(n * m) where n = len(data), m = len(bins)
    """
    if not isinstance(data, list) or not isinstance(bins, list):
        raise TypeError("Both 'data' and 'bins' must be lists.")

    if not data:
        raise ValueError("Input data cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric.")

    if not all(isinstance(x, (int, float)) for x in bins):
        raise TypeError("All elements in 'bins' must be numeric.")

    sorted_bins = sorted(bins)
    counts = [0] * (len(sorted_bins) + 1)

    for value in data:
        placed = False

        for i, boundary in enumerate(sorted_bins):

            if value <= boundary:
                counts[i] += 1
                placed = True
                break

        if not placed:
            counts[-1] += 1

    return counts


def sum_list(data: List[Union[int, float]]) -> Union[int, float]:
    """Calculates the sum of all values in a list.

    Args:
        data: A list of numeric values.

    Returns:
        The sum of all values.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> sum_list([1, 2, 3, 4])
        10
        >>> sum_list([1.5, 2.5])
        4.0

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    return sum(data)


def covariance_matrix(data: List[List[Union[int, float]]]) -> List[List[float]]:
    """Computes the sample covariance matrix for a set of variables.

    Each inner list represents one variable's observations. All variables
    must have the same number of observations.

    Args:
        data: A list of lists where ``data[i]`` is the observation series
              for variable *i*. Must contain at least 2 variables and
              at least 2 observations each.

    Returns:
        A square matrix (list of lists) where element ``[i][j]`` is the
        sample covariance between variable *i* and variable *j*.

    Raises:
        TypeError: If *data* is not a list of numeric lists.
        ValueError: If fewer than 2 variables or observations are given,
                    or if observation lengths differ.

    Example:
        >>> covariance_matrix([[1, 2, 3], [4, 5, 6]])
        [[1.0, 1.0], [1.0, 1.0]]
        >>> covariance_matrix([[1, 2, 3], [6, 5, 4]])
        [[1.0, -1.0], [-1.0, 1.0]]

    Complexity: O(k^2 * n) where k = number of variables, n = observations.
    """
    if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        raise TypeError("data must be a list of numeric lists.")

    k = len(data)

    if k < 2:
        raise ValueError("At least 2 variables are required.")

    n = len(data[0])

    if n < 2:
        raise ValueError("At least 2 observations per variable are required.")

    for i, row in enumerate(data):

        if len(row) != n:
            raise ValueError(f"All variables must have the same number of observations (variable {i} has {len(row)}, expected {n}).")

        if not all(isinstance(x, (int, float)) for x in row):
            raise TypeError("All elements must be numeric (int or float).")

    means = [sum(var) / n for var in data]
    matrix: List[List[float]] = []

    for i in range(k):

        row: List[float] = []

        for j in range(k):
            cov = sum((data[i][m] - means[i]) * (data[j][m] - means[j]) for m in range(n)) / (n - 1)
            row.append(cov)

        matrix.append(row)

    return matrix


def standard_error(data: List[Union[int, float]]) -> float:
    """Calculates the standard error of the mean (SEM).

    SEM = sample standard deviation / sqrt(n). It estimates how much the
    sample mean is expected to vary from the true population mean.

    Args:
        data: A list of numeric values (at least 2 elements).

    Returns:
        The standard error of the mean.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list has fewer than 2 elements.

    Example:
        >>> round(standard_error([2, 4, 4, 4, 5, 5, 7, 9]), 6)
        0.755929

    Complexity: O(n)
    """
    _validate_numeric_list(data, min_length=2)

    return statistics.stdev(data) / math.sqrt(len(data))


def winsorize(data: List[Union[int, float]], percent: float) -> List[float]:
    """Replaces extreme values with the corresponding percentile boundaries.

    Unlike ``trimmed_mean``, winsorization preserves the original list length
    by capping values at the lower and upper percentile thresholds.

    Args:
        data: A list of numeric values.
        percent: Fraction of data to replace on each end (0 to 0.5 exclusive).

    Returns:
        A new list with extreme values capped.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty or percent is out of range.

    Example:
        >>> winsorize([1, 2, 3, 4, 100], 0.2)
        [2.0, 2.0, 3.0, 4.0, 4.0]

    Complexity: O(n log n)
    """
    _validate_numeric_list(data)

    if not isinstance(percent, (int, float)) or not (0 <= percent < 0.5):
        raise ValueError("Percent must be between 0 and 0.5 (exclusive).")

    sorted_data = sorted(data)
    n = len(sorted_data)
    trim_count = int(n * percent)

    if trim_count == 0:
        return [float(x) for x in data]

    lower_bound = sorted_data[trim_count]
    upper_bound = sorted_data[n - 1 - trim_count]

    return [float(max(lower_bound, min(upper_bound, x))) for x in data]


# ============================================================================
# CORRELATION (NON-PARAMETRIC)
# ============================================================================


def spearman_correlation(data1: List[Union[int, float]],
                         data2: List[Union[int, float]]) -> float:
    """Calculates the Spearman rank correlation coefficient.

    Spearman correlation is a non-parametric measure of rank correlation.
    It assesses how well the relationship between two variables can be
    described using a monotonic function (not necessarily linear).

    Args:
        data1: The first list of numeric values.
        data2: The second list of numeric values.

    Returns:
        The Spearman correlation coefficient between -1 and 1.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists differ in length or have fewer than 3 elements.

    Example:
        >>> spearman_correlation([1, 2, 3, 4, 5], [5, 6, 7, 8, 7])
        0.8207826816681233
        >>> spearman_correlation([1, 2, 3], [3, 2, 1])
        -1.0

    Complexity: O(n log n)
    """
    if not isinstance(data1, list) or not isinstance(data2, list):
        raise TypeError("Inputs 'data1' and 'data2' must be lists.")

    if len(data1) != len(data2):
        raise ValueError("Input lists must have the same length.")

    if len(data1) < 3:
        raise ValueError("Spearman correlation requires at least 3 data points.")

    if not all(isinstance(x, (int, float)) for x in data1) or \
       not all(isinstance(x, (int, float)) for x in data2):
        raise TypeError("All elements must be numeric (int or float).")

    ranks1 = rank(data1, method="average")
    ranks2 = rank(data2, method="average")
    return calculate_pearson_correlation(ranks1, ranks2)


# ============================================================================
# REGRESSION METRICS
# ============================================================================


def mean_squared_error(observed: List[Union[int, float]],
                       predicted: List[Union[int, float]]) -> float:
    """Calculates the mean squared error (MSE) between observed and predicted values.

    MSE is a standard metric for evaluating prediction accuracy. Lower
    values indicate better fit.

    Args:
        observed: A list of actual values.
        predicted: A list of predicted values.

    Returns:
        The mean squared error.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists differ in length or are empty.

    Example:
        >>> mean_squared_error([3, -0.5, 2, 7], [2.5, 0.0, 2, 8])
        0.375
        >>> mean_squared_error([1, 2, 3], [1, 2, 3])
        0.0

    Complexity: O(n)
    """
    if not isinstance(observed, list) or not isinstance(predicted, list):
        raise TypeError("Inputs must be lists.")

    if len(observed) != len(predicted):
        raise ValueError("Input lists must have the same length.")

    if not observed:
        raise ValueError("Input lists cannot be empty.")

    if not all(isinstance(x, (int, float)) for x in observed) or \
       not all(isinstance(x, (int, float)) for x in predicted):
        raise TypeError("All elements must be numeric.")

    return sum((o - p) ** 2 for o, p in zip(observed, predicted)) / len(observed)


# ============================================================================
# TIME-SERIES UTILITIES
# ============================================================================


def pct_change(data: List[Union[int, float]]) -> List[Optional[float]]:
    """Calculates the percentage change between consecutive elements.

    The first element is always ``None`` (no predecessor). Zero values
    in the denominator produce ``None`` for that position.

    Args:
        data: A list of numeric values.

    Returns:
        A list of the same length with fractional changes (0.1 = 10 %).

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list is empty.

    Example:
        >>> pct_change([100, 110, 99])
        [None, 0.1, -0.1]
        >>> pct_change([50, 0, 100])
        [None, -1.0, None]

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    result: List[Optional[float]] = [None]

    for i in range(1, len(data)):

        if data[i - 1] == 0:
            result.append(None)
        else:
            result.append((data[i] - data[i - 1]) / data[i - 1])

    return result


def rolling_std(data: List[Union[int, float]], window: int,
                sample: bool = True) -> List[Optional[float]]:
    """Calculates the rolling (moving) standard deviation over a fixed window.

    The first ``window - 1`` positions are ``None`` (insufficient data).

    Args:
        data: A list of numeric values.
        window: Number of consecutive elements per window (>= 2).
        sample: If True, uses sample std dev (n-1); otherwise population.

    Returns:
        A list of the same length; each entry is the standard deviation of
        the preceding *window* elements or ``None``.

    Raises:
        TypeError: If input is not a list of numbers or window is not int.
        ValueError: If the list is empty or window < 2.

    Example:
        >>> result = rolling_std([2, 4, 4, 4, 5, 5, 7, 9], 3)
        >>> [round(v, 4) if v is not None else None for v in result]
        [None, None, 1.1547, 0.0, 0.5774, 0.5774, 1.1547, 2.0]

    Complexity: O(n * window)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not isinstance(window, int):
        raise TypeError("'window' must be an integer.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    if window < 2:
        raise ValueError("'window' must be >= 2.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements must be numeric.")

    std_func = statistics.stdev if sample else statistics.pstdev
    result: List[Optional[float]] = [None] * (window - 1)

    for i in range(window - 1, len(data)):
        segment = data[i - window + 1: i + 1]
        result.append(std_func(segment))

    return result


# ============================================================================
# DATA CLEANING & OUTLIERS
# ============================================================================


def outliers_iqr(data: List[Union[int, float]],
                 factor: float = 1.5) -> List[Union[int, float]]:
    """Detects outliers using the Interquartile Range (IQR) method.

    A value is considered an outlier if it lies below Q1 - factor*IQR or
    above Q3 + factor*IQR.

    Args:
        data: A list of numeric values (at least 4 elements).
        factor: Multiplier for the IQR to set the fences (default 1.5).

    Returns:
        A list containing only the outlier values (preserving order).

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If the list has fewer than 4 elements or factor <= 0.

    Example:
        >>> outliers_iqr([1, 2, 3, 4, 5, 100])
        [100]
        >>> outliers_iqr([10, 12, 14, 16, 18])
        []

    Complexity: O(n log n)
    """
    _validate_numeric_list(data, min_length=4)

    if not isinstance(factor, (int, float)) or factor <= 0:
        raise ValueError("'factor' must be a positive number.")

    sorted_data = sorted(data)
    q1 = calculate_percentile(sorted_data, 25)
    q3 = calculate_percentile(sorted_data, 75)
    iqr = q3 - q1

    lower_fence = q1 - factor * iqr
    upper_fence = q3 + factor * iqr

    return [x for x in data if x < lower_fence or x > upper_fence]


# ============================================================================
# INFORMATION THEORY
# ============================================================================


def entropy(data: List[Union[int, float, str]]) -> float:
    """Calculates the Shannon entropy of a discrete dataset.

    Entropy quantifies the average level of uncertainty or information
    inherent in a variable's possible outcomes. Higher entropy means
    higher unpredictability.

    Args:
        data: A list of categorical or numeric values.

    Returns:
        The Shannon entropy in bits (log base 2).

    Raises:
        TypeError: If input is not a list.
        ValueError: If the list is empty.

    Example:
        >>> round(entropy([1, 1, 2, 2]), 4)
        1.0
        >>> round(entropy(["a", "a", "a", "a"]), 4)
        0.0
        >>> round(entropy([1, 2, 3, 4]), 4)
        2.0

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")

    if not data:
        raise ValueError("Input list cannot be empty.")

    n = len(data)
    freq: Dict[Any, int] = {}

    for item in data:
        freq[item] = freq.get(item, 0) + 1

    h = 0.0

    for count in freq.values():
        p = count / n

        if p > 0:
            h -= p * math.log2(p)

    return h


# ============================================================================
# WEIGHTED STATISTICS
# ============================================================================


def weighted_median(data: List[Union[int, float]],
                    weights: List[Union[int, float]]) -> float:
    """Calculates the weighted median of a dataset.

    The weighted median is the value separating the higher half from the
    lower half of a dataset when each observation is weighted.

    Args:
        data: A list of numeric values.
        weights: A list of corresponding positive weights.

    Returns:
        The weighted median value.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists differ in length, are empty, or weights
                    are non-positive.

    Example:
        >>> weighted_median([1, 2, 3], [1, 1, 1])
        2.0
        >>> weighted_median([1, 2, 3, 4, 5], [5, 1, 1, 1, 1])
        1.0

    Complexity: O(n log n)
    """
    if not isinstance(data, list) or not isinstance(weights, list):
        raise TypeError("Both 'data' and 'weights' must be lists.")

    if not data:
        raise ValueError("Input lists cannot be empty.")

    if len(data) != len(weights):
        raise ValueError("'data' and 'weights' must have the same length.")

    if not all(isinstance(x, (int, float)) for x in data):
        raise TypeError("All elements in 'data' must be numeric.")

    if not all(isinstance(w, (int, float)) for w in weights):
        raise TypeError("All elements in 'weights' must be numeric.")

    if any(w <= 0 for w in weights):
        raise ValueError("All weights must be positive.")

    # Sort by data values, carrying weights along
    pairs = sorted(zip(data, weights), key=lambda p: p[0])
    total_weight = sum(w for _, w in pairs)
    cumulative = 0.0

    for value, weight in pairs:
        cumulative += weight

        if cumulative >= total_weight / 2:
            return float(value)

    return float(pairs[-1][0])


def rolling_median(
    data: List[Union[int, float]],
    window: int,
) -> List[Optional[float]]:
    """Calculates a rolling (moving) median over a dataset.

    For each position, returns the median of the preceding ``window``
    elements. Positions with fewer than ``window`` elements return None.

    Args:
        data: A list of numeric values.
        window: The size of the rolling window (must be >= 1).

    Returns:
        A list of the same length as ``data`` with rolling median values
        (or None where the window is incomplete).

    Raises:
        TypeError: If data is not a list or contains non-numeric values.
        ValueError: If window is less than 1 or data is empty.

    Example:
        >>> rolling_median([1, 3, 5, 7, 9], 3)
        [None, None, 3.0, 5.0, 7.0]

    Complexity: O(n * w) where n is the data length and w is the window size.
    """
    _validate_numeric_list(data)

    if window < 1:
        raise ValueError("Window must be at least 1.")

    import statistics

    result: List[Optional[float]] = []

    for i in range(len(data)):

        if i < window - 1:
            result.append(None)
        else:
            window_data = data[i - window + 1: i + 1]
            result.append(float(statistics.median(window_data)))

    return result


def sum_product(list1: List[Union[int, float]],
                list2: List[Union[int, float]]) -> float:
    """Return the sum of element-wise products of two lists.

    Equivalent to Excel's SUMPRODUCT for two arrays.

    Args:
        list1: First numeric list.
        list2: Second numeric list (same length).

    Returns:
        Sum of list1[i] * list2[i] for all i.

    Raises:
        ValueError: If lists have different lengths.

    Example:
        >>> sum_product([1, 2, 3], [4, 5, 6])
        32.0
        >>> sum_product([10, 20], [0.5, 0.3])
        11.0

    Complexity: O(n)
    """

    if len(list1) != len(list2):
        raise ValueError("Both lists must have the same length.")

    return float(sum(a * b for a, b in zip(list1, list2)))


def count_true_with_sum(boolean_list: List[bool]) -> int:
    """Counts the number of True values in a boolean list.

    Args:
        boolean_list (List[bool]): A list containing True or False values.

    Returns:
        int: The total number of True values in the list.

    Raises:
        TypeError: If 'boolean_list' is not a list or contains non-boolean elements.

    Example:
        >>> count_true_with_sum([True, False, True, True])
        3
        >>> count_true_with_sum([False, False, False])
        0

    **Cost:** O(n), where n is the number of elements in the list.
    """
    if not isinstance(boolean_list, list):
        raise TypeError("'boolean_list' must be a list.")

    for item in boolean_list:

        if not isinstance(item, bool):
            raise TypeError("All elements in 'boolean_list' must be booleans.")

    return sum(boolean_list)


def standard_error_estimate(
    known_y: List[Union[int, float]], known_x: List[Union[int, float]]
) -> float:
    """Returns the standard error of the predicted y-value for each x.

    Description:
        Computes the standard error of the estimate for a linear regression
        of known_y on known_x. Measures how far observed y-values fall from
        the regression line. Equivalent to Excel STEYX.

    Args:
        known_y: The dependent data (observed y-values).
        known_x: The independent data (observed x-values).

    Returns:
        The standard error of the estimate.

    Raises:
        ValueError: If arrays differ in length, have fewer than 3 points,
            or are empty.

    Example:
        >>> round(standard_error_estimate([2, 3, 9, 1, 8, 7, 5], [6, 5, 11, 7, 5, 4, 4]), 6)
        3.305719

    Complexity: O(n)
    """
    if len(known_y) != len(known_x):
        raise ValueError("Arrays must have the same length.")

    n = len(known_y)

    if n < 3:
        raise ValueError("At least 3 data points are required.")

    mean_x = sum(known_x) / n
    mean_y = sum(known_y) / n

    ss_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(known_x, known_y))
    ss_xx = sum((x - mean_x) ** 2 for x in known_x)

    if ss_xx == 0:
        raise ValueError("All x-values are identical; regression is undefined.")

    slope = ss_xy / ss_xx
    intercept = mean_y - slope * mean_x

    sse = sum((y - (slope * x + intercept)) ** 2 for x, y in zip(known_x, known_y))
    return (sse / (n - 2)) ** 0.5


def probability_range(
    x_range: list[float],
    prob_range: list[float],
    lower_limit: float,
    upper_limit: float | None = None,
) -> float:
    """Sum of probabilities for values within a range.

    Description:
        Given parallel arrays of discrete values and their probabilities,
        returns the sum of probabilities for values between lower_limit
        and upper_limit (inclusive). Equivalent to Excel PROB.

    Args:
        x_range: Array of discrete values.
        prob_range: Corresponding probabilities (must sum to ≈ 1).
        lower_limit: Lower bound of the range.
        upper_limit: Upper bound (defaults to lower_limit for exact match).

    Returns:
        float: Sum of matching probabilities.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If arrays differ in length, probabilities are negative,
                     or they don't sum to approximately 1.

    Example:
        >>> probability_range([0, 1, 2, 3], [0.1, 0.2, 0.4, 0.3], 1, 2)
        0.6
        >>> probability_range([10, 20, 30], [0.3, 0.5, 0.2], 20)
        0.5

    Complexity: O(n)
    """
    if upper_limit is None:
        upper_limit = lower_limit

    if len(x_range) != len(prob_range):
        raise ValueError("x_range and prob_range must have the same length.")

    if any(p < 0 for p in prob_range):
        raise ValueError("Probabilities must be non-negative.")

    total_prob = sum(prob_range)

    if abs(total_prob - 1.0) > 0.01:
        raise ValueError("Probabilities must sum to approximately 1.")

    if lower_limit > upper_limit:
        raise ValueError("lower_limit must be <= upper_limit.")

    return sum(
        p for x, p in zip(x_range, prob_range)
        if lower_limit <= x <= upper_limit
    )


def _require_scipy_stats() -> None:
    """Raise ImportError if scipy is not available."""
    try:
        import scipy.stats  # noqa: F401
    except ImportError:
        raise ImportError("scipy is required for this function.")


def chisq_test(observed: List[List[Union[int, float]]],
               expected: Optional[List[List[Union[int, float]]]] = None
               ) -> float:
    """Chi-squared test for independence.

    Description:
        Returns the p-value for a chi-squared test of independence
        on a contingency table. Equivalent to Excel CHISQ.TEST.

    Args:
        observed: 2-D contingency table of observed frequencies.
        expected: Optional 2-D table of expected frequencies.
                  If None, expected values are computed automatically.

    Returns:
        float: p-value of the chi-squared test.

    Raises:
        TypeError: If inputs are not 2-D lists of numbers.
        ValueError: If dimensions mismatch or values invalid.

    Example:
        >>> round(chisq_test([[58, 35], [11, 25], [10, 23]]), 4)
        0.0004

    Complexity: O(r × c)
    """
    if not isinstance(observed, list) or not all(isinstance(r, list) for r in observed):
        raise TypeError("observed must be a 2-D list.")

    _require_scipy_stats()
    import scipy.stats as st

    if expected is not None:
        if len(observed) != len(expected):
            raise ValueError("observed and expected must have same dimensions.")

        chi2 = sum(
            (o - e) ** 2 / e
            for obs_row, exp_row in zip(observed, expected)
            for o, e in zip(obs_row, exp_row)
        )
        df = sum(len(r) for r in observed) - 1
        return float(st.chi2.sf(chi2, df))

    chi2, p, _, _ = st.chi2_contingency(observed)
    return float(p)


def f_test(data1: List[Union[int, float]],
           data2: List[Union[int, float]]) -> float:
    """F-test for comparing two variances.

    Description:
        Returns the two-tailed p-value of an F-test comparing
        the variances of two datasets. Equivalent to Excel F.TEST.

    Args:
        data1: First dataset.
        data2: Second dataset.

    Returns:
        float: Two-tailed p-value.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If datasets have fewer than 2 elements.

    Example:
        >>> round(f_test([6, 7, 9, 15, 21], [20, 28, 31, 38, 40]), 4)
        0.6482

    Complexity: O(n)
    """
    if not isinstance(data1, list) or not isinstance(data2, list):
        raise TypeError("data1 and data2 must be lists.")

    if len(data1) < 2 or len(data2) < 2:
        raise ValueError("Each dataset must have at least 2 elements.")

    _require_scipy_stats()
    import scipy.stats as st

    var1 = sum((x - sum(data1) / len(data1)) ** 2 for x in data1) / (len(data1) - 1)
    var2 = sum((x - sum(data2) / len(data2)) ** 2 for x in data2) / (len(data2) - 1)

    if var2 == 0:
        raise ValueError("data2 has zero variance.")

    f_stat = var1 / var2
    df1 = len(data1) - 1
    df2 = len(data2) - 1

    p = st.f.sf(f_stat, df1, df2)
    return float(min(2 * p, 1.0))


def t_test(data1: List[Union[int, float]],
           data2: List[Union[int, float]],
           tails: int = 2, type_: int = 2) -> float:
    """Student's t-test.

    Description:
        Returns the p-value associated with a t-test.
        Equivalent to Excel T.TEST.

    Args:
        data1: First dataset.
        data2: Second dataset.
        tails: 1 for one-tailed, 2 for two-tailed.
        type_: 1 = paired, 2 = equal variance, 3 = unequal variance.

    Returns:
        float: p-value.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If parameters out of range or datasets too small.

    Example:
        >>> round(t_test([3, 4, 5, 8, 9, 1, 2, 4, 5], [6, 19, 3, 2, 14, 4, 5, 17, 1]), 4)
        0.1961

    Complexity: O(n)
    """
    if not isinstance(data1, list) or not isinstance(data2, list):
        raise TypeError("data1 and data2 must be lists.")

    if tails not in (1, 2):
        raise ValueError("tails must be 1 or 2.")

    if type_ not in (1, 2, 3):
        raise ValueError("type_ must be 1, 2, or 3.")

    _require_scipy_stats()
    import scipy.stats as st

    if type_ == 1:
        if len(data1) != len(data2):
            raise ValueError("Paired test requires equal-length datasets.")

        _, p = st.ttest_rel(data1, data2)
    elif type_ == 2:
        _, p = st.ttest_ind(data1, data2, equal_var=True)
    else:
        _, p = st.ttest_ind(data1, data2, equal_var=False)

    if tails == 1:
        return float(p / 2)

    return float(p)


def z_test(data: List[Union[int, float]], x: float,
           sigma: Optional[float] = None) -> float:
    """One-tailed p-value of a z-test.

    Description:
        Returns the one-tailed p-value of a z-test.
        Equivalent to Excel Z.TEST.

    Args:
        data: Sample data.
        x: Hypothesized population mean.
        sigma: Known population standard deviation.
               If None, uses sample standard deviation.

    Returns:
        float: One-tailed p-value.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If data has fewer than 2 elements.

    Example:
        >>> round(z_test([3, 6, 7, 8, 6, 5, 4, 2, 1, 9], 4), 4)
        0.0907

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")

    if len(data) < 2:
        raise ValueError("data must have at least 2 elements.")

    _require_scipy_stats()
    import scipy.stats as st

    n = len(data)
    mean = sum(data) / n

    if sigma is None:
        sigma = (sum((x_ - mean) ** 2 for x_ in data) / (n - 1)) ** 0.5

    if sigma == 0:
        return 0.0

    z = (mean - x) / (sigma / n ** 0.5)
    return float(1 - st.norm.cdf(z))


def percentile_exc(data: List[Union[int, float]], k: float) -> float:
    """k-th percentile using exclusive interpolation.

    Description:
        Returns the k-th percentile using the exclusive method
        (k in range (0, 1) exclusive). Equivalent to Excel PERCENTILE.EXC.

    Args:
        data: Numeric dataset.
        k: Percentile (0 < k < 1, exclusive).

    Returns:
        float: Percentile value.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If k ≤ 0 or k ≥ 1.

    Example:
        >>> percentile_exc([1, 2, 3, 4], 0.5)
        2.5

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")

    if not isinstance(k, (int, float)):
        raise TypeError("k must be numeric.")

    if k <= 0 or k >= 1:
        raise ValueError("k must be in (0, 1) exclusive.")

    sorted_data = sorted(data)
    n = len(sorted_data)
    rank = k * (n + 1) - 1

    if rank <= 0:
        return float(sorted_data[0])

    if rank >= n - 1:
        return float(sorted_data[-1])

    lower = int(rank)
    frac = rank - lower
    return float(sorted_data[lower] + frac * (sorted_data[lower + 1] - sorted_data[lower]))


def quartile_exc(data: List[Union[int, float]], quart: int) -> float:
    """Quartile using exclusive interpolation.

    Description:
        Returns a quartile value using the exclusive method.
        Equivalent to Excel QUARTILE.EXC. quart must be 1, 2, or 3.

    Args:
        data: Numeric dataset.
        quart: 1 (25th), 2 (50th), or 3 (75th).

    Returns:
        float: Quartile value.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If quart not in {1, 2, 3}.

    Example:
        >>> quartile_exc([6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49], 1)
        15.0

    Complexity: O(n log n)
    """
    if quart not in (1, 2, 3):
        raise ValueError("quart must be 1, 2, or 3.")

    return percentile_exc(data, quart / 4.0)


def percentrank_exc(data: List[Union[int, float]],
                    x: Union[int, float],
                    significance: int = 3) -> float:
    """Rank of a value as a percentage (exclusive).

    Description:
        Returns the rank of a value among a dataset as a percentage,
        using the exclusive method. Equivalent to Excel PERCENTRANK.EXC.

    Args:
        data: Numeric dataset.
        x: Value to rank.
        significance: Number of significant digits (default 3).

    Returns:
        float: Percentage rank (0 to 1, exclusive).

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If x is outside the range of data.

    Example:
        >>> percentrank_exc([1, 2, 3, 6, 6, 6, 7, 8, 9], 7)
        0.778

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")

    sorted_data = sorted(data)
    n = len(sorted_data)

    if x < sorted_data[0] or x > sorted_data[-1]:
        raise ValueError("x is outside the range of data.")

    if x in sorted_data:
        rank = sorted_data.index(x) + 1
        result = rank / (n + 1)
    else:
        for i in range(n - 1):

            if sorted_data[i] < x < sorted_data[i + 1]:
                frac = (x - sorted_data[i]) / (sorted_data[i + 1] - sorted_data[i])
                rank = (i + 1) + frac
                result = rank / (n + 1)
                break

    return round(result, significance)


def mode_mult(data: List[Union[int, float]]) -> List[Union[int, float]]:
    """Returns all modes (most frequent values) in a dataset.

    Description:
        Returns a list of all values that appear with the highest
        frequency. Equivalent to Excel MODE.MULT.

    Args:
        data: Numeric dataset.

    Returns:
        List: All modal values sorted ascending.

    Raises:
        TypeError: If data is not a list.
        ValueError: If no mode exists (all values unique).

    Example:
        >>> mode_mult([1, 2, 3, 4, 3, 2, 1, 2, 3])
        [2, 3]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")

    if len(data) == 0:
        raise ValueError("data must not be empty.")

    from collections import Counter
    counts = Counter(data)
    max_count = max(counts.values())

    if max_count == 1:
        raise ValueError("No mode exists; all values are unique.")

    return sorted(v for v, c in counts.items() if c == max_count)


def mode_single(data: List[Union[int, float]]) -> float:
    """Returns the single most frequent value in a dataset.

    Description:
        Returns the first value with the highest frequency in
        order of appearance. Equivalent to Excel MODE.SNGL.

    Args:
        data: Numeric dataset.

    Returns:
        float: The first modal value by order of appearance.

    Raises:
        TypeError: If data is not a list.
        ValueError: If data is empty or all values are unique.

    Example:
        >>> mode_single([1, 2, 3, 3, 4])
        3.0
        >>> mode_single([1, 2, 2, 3, 3])
        2.0

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")

    if len(data) == 0:
        raise ValueError("data must not be empty.")

    from collections import Counter
    counts = Counter(data)
    max_count = max(counts.values())

    if max_count == 1:
        raise ValueError("No mode exists; all values are unique.")

    # Return first value with max frequency in order of appearance
    for val in data:
        if counts[val] == max_count:
            return float(val)

    return float(data[0])


def trend(known_y: List[Union[int, float]],
          known_x: Optional[List[Union[int, float]]] = None,
          new_x: Optional[List[Union[int, float]]] = None,
          const: bool = True) -> List[float]:
    """Predicted values along a linear trend.

    Description:
        Uses least-squares linear regression to predict y values
        for new_x values. Equivalent to Excel TREND.

    Args:
        known_y: Known y-values.
        known_x: Known x-values (defaults to 1, 2, ..., n).
        new_x: X-values for which to predict (defaults to known_x).
        const: If True, calculate intercept normally. If False,
            force the regression line through the origin.

    Returns:
        List[float]: Predicted y-values.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If arrays are empty or mismatched.

    Example:
        >>> [round(v, 2) for v in trend([1, 9, 5, 7])]
        [2.0, 4.0, 6.0, 8.0]

    Complexity: O(n)
    """
    if not isinstance(known_y, list) or len(known_y) == 0:
        raise TypeError("known_y must be a non-empty list.")

    n = len(known_y)

    if known_x is None:
        known_x = list(range(1, n + 1))

    if len(known_x) != n:
        raise ValueError("known_x and known_y must have the same length.")

    if new_x is None:
        new_x = known_x

    if const:
        mean_x = sum(known_x) / n
        mean_y = sum(known_y) / n

        ss_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(known_x, known_y))
        ss_xx = sum((x - mean_x) ** 2 for x in known_x)

        if ss_xx == 0:
            return [mean_y] * len(new_x)

        m = ss_xy / ss_xx
        b = mean_y - m * mean_x
    else:
        s_xy = sum(x * y for x, y in zip(known_x, known_y))
        s_xx = sum(x * x for x in known_x)

        if s_xx == 0:
            return [0.0] * len(new_x)

        m = s_xy / s_xx
        b = 0.0

    return [m * x + b for x in new_x]


def growth(known_y: List[Union[int, float]],
           known_x: Optional[List[Union[int, float]]] = None,
           new_x: Optional[List[Union[int, float]]] = None) -> List[float]:
    """Predicted values along an exponential trend.

    Description:
        Uses least-squares exponential regression to predict y values.
        Equivalent to Excel GROWTH. Fits y = b * m^x.

    Args:
        known_y: Known y-values (must be positive).
        known_x: Known x-values (defaults to 1, 2, ..., n).
        new_x: X-values for which to predict (defaults to known_x).

    Returns:
        List[float]: Predicted y-values.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If known_y contains non-positive values.

    Example:
        >>> [round(v, 2) for v in growth([33100, 47300, 69000, 102000, 150000, 220000])]
        [32618.2, 47729.42, 69841.3, 102197.07, 149542.49, 218821.87]

    Complexity: O(n)
    """
    if not isinstance(known_y, list) or len(known_y) == 0:
        raise TypeError("known_y must be a non-empty list.")

    if any(y <= 0 for y in known_y):
        raise ValueError("known_y values must be positive for exponential fit.")

    n = len(known_y)

    if known_x is None:
        known_x = list(range(1, n + 1))

    if len(known_x) != n:
        raise ValueError("known_x and known_y must have the same length.")

    if new_x is None:
        new_x = known_x

    ln_y = [math.log(y) for y in known_y]
    result = trend(ln_y, known_x, new_x)
    return [math.exp(v) for v in result]


def linest(known_y: List[Union[int, float]],
           known_x: Optional[List[Union[int, float]]] = None
           ) -> Dict[str, float]:
    """Linear regression statistics.

    Description:
        Returns slope, intercept, r_squared, standard_error,
        and other statistics for a linear regression.
        Equivalent to Excel LINEST.

    Args:
        known_y: Known y-values.
        known_x: Known x-values (defaults to 1, 2, ..., n).

    Returns:
        Dict with keys: slope, intercept, r_squared, std_err_slope,
        std_err_intercept, f_statistic, df, ss_reg, ss_resid.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If arrays are empty or mismatched.

    Example:
        >>> result = linest([1, 9, 5, 7])
        >>> round(result['slope'], 4)
        2.0

    Complexity: O(n)
    """
    if not isinstance(known_y, list) or len(known_y) == 0:
        raise TypeError("known_y must be a non-empty list.")

    n = len(known_y)

    if known_x is None:
        known_x = list(range(1, n + 1))

    if len(known_x) != n:
        raise ValueError("known_x and known_y must have the same length.")

    if n < 3:
        raise ValueError("At least 3 data points are required.")

    mean_x = sum(known_x) / n
    mean_y = sum(known_y) / n

    ss_xy = sum((x - mean_x) * (y - mean_y) for x, y in zip(known_x, known_y))
    ss_xx = sum((x - mean_x) ** 2 for x in known_x)
    ss_yy = sum((y - mean_y) ** 2 for y in known_y)

    if ss_xx == 0:
        raise ValueError("All x-values are identical; regression undefined.")

    m = ss_xy / ss_xx
    b = mean_y - m * mean_x

    predicted = [m * x + b for x in known_x]
    ss_resid = sum((y - yp) ** 2 for y, yp in zip(known_y, predicted))
    ss_reg = ss_yy - ss_resid

    r_sq = ss_reg / ss_yy if ss_yy != 0 else 0.0

    df = n - 2
    mse = ss_resid / df if df > 0 else 0.0
    se_slope = (mse / ss_xx) ** 0.5 if ss_xx > 0 else 0.0
    se_intercept = (mse * (1 / n + mean_x ** 2 / ss_xx)) ** 0.5

    f_stat = (ss_reg / 1) / mse if mse > 0 else float('inf')

    return {
        "slope": m,
        "intercept": b,
        "r_squared": r_sq,
        "std_err_slope": se_slope,
        "std_err_intercept": se_intercept,
        "f_statistic": f_stat,
        "df": df,
        "ss_reg": ss_reg,
        "ss_resid": ss_resid,
    }


def logest(known_y: List[Union[int, float]],
           known_x: Optional[List[Union[int, float]]] = None
           ) -> Dict[str, float]:
    """Exponential regression statistics.

    Description:
        Returns base (m), coefficient (b), and r_squared for
        an exponential curve y = b * m^x. Equivalent to Excel LOGEST.

    Args:
        known_y: Known y-values (must be positive).
        known_x: Known x-values (defaults to 1, 2, ..., n).

    Returns:
        Dict with keys: base, coefficient, r_squared.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If known_y has non-positive values.

    Example:
        >>> result = logest([33100, 47300, 69000, 102000, 150000, 220000])
        >>> round(result['base'], 4)
        1.4633

    Complexity: O(n)
    """
    if not isinstance(known_y, list) or len(known_y) == 0:
        raise TypeError("known_y must be a non-empty list.")

    if any(y <= 0 for y in known_y):
        raise ValueError("known_y values must be positive for exponential fit.")

    ln_y = [math.log(y) for y in known_y]
    stats = linest(ln_y, known_x)

    return {
        "base": math.exp(stats["slope"]),
        "coefficient": math.exp(stats["intercept"]),
        "r_squared": stats["r_squared"],
    }


def skew_p(data: List[Union[int, float]]) -> float:
    """Population skewness of a distribution.

    Description:
        Returns the skewness based on the entire population
        (not sample). Equivalent to Excel SKEW.P.

    Args:
        data: Numeric dataset (at least 3 values).

    Returns:
        float: Population skewness.

    Raises:
        TypeError: If data is not a list.
        ValueError: If fewer than 3 elements or zero std deviation.

    Example:
        >>> round(skew_p([3, 4, 5, 2, 3, 4, 5, 6, 4, 7]), 6)
        0.303193

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")

    n = len(data)

    if n < 3:
        raise ValueError("At least 3 data points are required.")

    mean = sum(data) / n
    m2 = sum((x - mean) ** 2 for x in data) / n
    m3 = sum((x - mean) ** 3 for x in data) / n

    if m2 == 0:
        raise ValueError("Standard deviation is zero.")

    return m3 / (m2 ** 1.5)


def standardize(x: float, mean: float, standard_dev: float) -> float:
    """Normalized value from a distribution.

    Description:
        Returns (x - mean) / standard_dev. Equivalent to Excel STANDARDIZE.

    Args:
        x: Value to normalize.
        mean: Mean of the distribution.
        standard_dev: Standard deviation (> 0).

    Returns:
        float: Standardized z-value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If standard_dev ≤ 0.

    Example:
        >>> standardize(42, 40, 1.5)
        1.3333333333333333

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [x, mean, standard_dev]):
        raise TypeError("All parameters must be numeric.")

    if standard_dev <= 0:
        raise ValueError("standard_dev must be positive.")

    return (x - mean) / standard_dev


def forecast_ets(
    target: Union[int, float],
    values: List[Union[int, float]],
    timeline: List[Union[int, float]],
    seasonality: int = 1,
    data_completion: int = 1,
    aggregation: int = 1,
) -> float:
    """Forecast value using exponential smoothing (ETS).

    Description:
        Simplified ETS forecast using double exponential smoothing
        (Holt's method). Equivalent to Excel FORECAST.ETS.

    Args:
        target: Target timeline point to forecast.
        values: Known values.
        timeline: Known timeline points.
        seasonality: Seasonal period (1 = no seasonality).
        data_completion: 1 = fill missing with interpolation.
        aggregation: 1 = average for duplicates.

    Returns:
        float: Forecasted value.

    Raises:
        TypeError: If inputs are not valid types.
        ValueError: If arrays differ in length or are too short.

    Example:
        >>> round(forecast_ets(6, [10, 20, 30, 40, 50], [1, 2, 3, 4, 5]), 1)
        60.0

    Complexity: O(n)
    """
    if not isinstance(values, list) or not isinstance(timeline, list):
        raise TypeError("values and timeline must be lists.")

    if len(values) != len(timeline):
        raise ValueError("values and timeline must have the same length.")

    n = len(values)

    if n < 3:
        raise ValueError("At least 3 data points are required.")

    # Sort by timeline
    paired = sorted(zip(timeline, values))
    t_sorted = [p[0] for p in paired]
    v_sorted = [p[1] for p in paired]

    # Holt's double exponential smoothing
    alpha = 0.3
    beta = 0.1

    level = v_sorted[0]
    trend_val = v_sorted[1] - v_sorted[0]

    for i in range(1, n):
        prev_level = level
        level = alpha * v_sorted[i] + (1 - alpha) * (prev_level + trend_val)
        trend_val = beta * (level - prev_level) + (1 - beta) * trend_val

    # Forecast: extrapolate from end of timeline
    steps = target - t_sorted[-1]

    if len(t_sorted) >= 2:
        avg_step = (t_sorted[-1] - t_sorted[0]) / (n - 1)

        if avg_step != 0:
            steps_count = steps / avg_step
        else:
            steps_count = steps
    else:
        steps_count = steps

    return level + trend_val * steps_count


def aggregate(
    data: list[int | float],
    operation: str = "sum",
    ignore_errors: bool = False,
) -> float:
    """Perform a named aggregation on a numeric list.

    Supported operations: ``"sum"``, ``"avg"``, ``"max"``, ``"min"``,
    ``"count"``, ``"product"``.

    Args:
        data: List of numeric values.
        operation: Aggregation name (case-insensitive).
        ignore_errors: If ``True``, silently skip non-numeric items.

    Returns:
        Aggregated numeric result.

    Raises:
        ValueError: If *data* is empty or *operation* is unknown.

    Example:
        >>> aggregate([1, 2, 3, 4], "sum")
        10
        >>> aggregate([1, 2, 3, 4], "avg")
        2.5

    Complexity: O(n)
    """
    if ignore_errors:
        data = [v for v in data if isinstance(v, (int, float)) and not isinstance(v, bool)]

    if not data:
        raise ValueError("Data list is empty.")

    op = operation.strip().lower()

    if op == "sum":
        return sum(data)

    if op == "avg":
        return sum(data) / len(data)

    if op == "max":
        return max(data)

    if op == "min":
        return min(data)

    if op == "count":
        return len(data)

    if op == "product":
        result = 1

        for v in data:
            result *= v

        return result

    raise ValueError(f"Unknown operation: '{operation}'.")


def _parse_criteria(criteria) -> callable:
    """Return a predicate function for an Excel-style criteria expression."""

    if isinstance(criteria, str):

        for op in (">=" , "<=", "<>", ">", "<", "="):

            if criteria.startswith(op):
                raw = criteria[len(op):]

                try:
                    num = float(raw)
                except (ValueError, TypeError):
                    num = None

                if num is not None:
                    if op == ">=":
                        return lambda v, n=num: isinstance(v, (int, float)) and v >= n
                    if op == "<=":
                        return lambda v, n=num: isinstance(v, (int, float)) and v <= n
                    if op == "<>":
                        return lambda v, n=num: not (isinstance(v, (int, float)) and v == n)
                    if op == ">":
                        return lambda v, n=num: isinstance(v, (int, float)) and v > n
                    if op == "<":
                        return lambda v, n=num: isinstance(v, (int, float)) and v < n
                    if op == "=":
                        return lambda v, n=num: isinstance(v, (int, float)) and v == n

                if op == "=":
                    return lambda v, r=raw: str(v) == r

                if op == "<>":
                    return lambda v, r=raw: str(v) != r

                return lambda v: False

        return lambda v, c=criteria: str(v) == c

    return lambda v, c=criteria: v == c


def max_if(
    values: list[int | float],
    criteria_range: list,
    criteria,
) -> float:
    """Return the maximum of *values* where the parallel *criteria_range* meets *criteria*.

    Equivalent to the Excel ``MAXIFS`` function (single criteria pair).

    Args:
        values: Numeric values to evaluate.
        criteria_range: Range to test against *criteria* (same length as *values*).
        criteria: Excel-style criteria (e.g. ``">0"``, ``"<>5"``, ``10``).

    Returns:
        Maximum among matching values.

    Raises:
        ValueError: If no values match or lengths differ.

    Example:
        >>> max_if([5, 10, 15, 20], ["A", "B", "A", "B"], "A")
        15
        >>> max_if([1, 2, 3, 4], [10, 20, 30, 40], ">15")
        4

    Complexity: O(n)
    """
    if len(values) != len(criteria_range):
        raise ValueError("values and criteria_range must have the same length.")

    pred = _parse_criteria(criteria)
    matched = [v for v, c in zip(values, criteria_range) if pred(c)]

    if not matched:
        raise ValueError("No values match the criteria.")

    return max(matched)


def min_if(
    values: list[int | float],
    criteria_range: list,
    criteria,
) -> float:
    """Return the minimum of *values* where the parallel *criteria_range* meets *criteria*.

    Equivalent to the Excel ``MINIFS`` function (single criteria pair).

    Args:
        values: Numeric values to evaluate.
        criteria_range: Range to test against *criteria* (same length as *values*).
        criteria: Excel-style criteria (e.g. ``">0"``, ``"<>5"``, ``10``).

    Returns:
        Minimum among matching values.

    Raises:
        ValueError: If no values match or lengths differ.

    Example:
        >>> min_if([5, 10, 15, 20], ["A", "B", "A", "B"], "A")
        5
        >>> min_if([1, 2, 3, 4], [10, 20, 30, 40], ">15")
        2

    Complexity: O(n)
    """
    if len(values) != len(criteria_range):
        raise ValueError("values and criteria_range must have the same length.")

    pred = _parse_criteria(criteria)
    matched = [v for v, c in zip(values, criteria_range) if pred(c)]

    if not matched:
        raise ValueError("No values match the criteria.")

    return min(matched)


def sum_of_squared_deviations(data: list[int | float]) -> float:
    """Return the sum of squared deviations from the mean.

    Equivalent to the Excel ``DEVSQ`` function.

    Args:
        data: List of numeric values.

    Returns:
        Sum of (x − mean)² for every x in *data*.

    Raises:
        ValueError: If *data* is empty.

    Example:
        >>> round(sum_of_squared_deviations([4, 5, 6, 7, 5, 4, 3]), 4)
        10.8571

    Complexity: O(n)
    """
    if not data:
        raise ValueError("Data list is empty.")

    mean = sum(data) / len(data)
    return sum((x - mean) ** 2 for x in data)


def sum_if(
    values: list[int | float],
    criteria_range: list,
    criteria,
) -> float:
    """Return the sum of *values* where the parallel *criteria_range* meets *criteria*.

    Equivalent to the Excel ``SUMIF`` / ``SUMIFS`` function (single criteria pair).

    Args:
        values: Numeric values to sum.
        criteria_range: Range to test against *criteria* (same length as *values*).
        criteria: Excel-style criteria (e.g. ``">0"``, ``"<>5"``, ``10``).

    Returns:
        Sum of matching values.

    Raises:
        ValueError: If no values match or lengths differ.

    Example:
        >>> sum_if([10, 20, 30, 40], ["A", "B", "A", "B"], "A")
        40
        >>> sum_if([1, 2, 3, 4], [10, 20, 30, 40], ">15")
        9

    Complexity: O(n)
    """
    if len(values) != len(criteria_range):
        raise ValueError("values and criteria_range must have the same length.")

    pred = _parse_criteria(criteria)
    matched = [v for v, c in zip(values, criteria_range) if pred(c) and isinstance(v, (int, float))]

    if not matched:
        raise ValueError("No values match the criteria.")

    return sum(matched)


def average_if(
    values: list[int | float],
    criteria_range: list,
    criteria,
) -> float:
    """Return the average of *values* where the parallel *criteria_range* meets *criteria*.

    Equivalent to the Excel ``AVERAGEIF`` / ``AVERAGEIFS`` function (single criteria pair).

    Args:
        values: Numeric values to average.
        criteria_range: Range to test against *criteria* (same length as *values*).
        criteria: Excel-style criteria (e.g. ``">0"``, ``"<>5"``, ``10``).

    Returns:
        Average of matching values.

    Raises:
        ValueError: If no values match or lengths differ.

    Example:
        >>> average_if([10, 20, 30, 40], ["A", "B", "A", "B"], "A")
        20.0
        >>> average_if([1, 2, 3, 4], [10, 20, 30, 40], ">15")
        3.0

    Complexity: O(n)
    """
    if len(values) != len(criteria_range):
        raise ValueError("values and criteria_range must have the same length.")

    pred = _parse_criteria(criteria)
    matched = [v for v, c in zip(values, criteria_range) if pred(c) and isinstance(v, (int, float))]

    if not matched:
        raise ValueError("No values match the criteria.")

    return sum(matched) / len(matched)


def root_mean_square(data: List[Union[int, float]]) -> float:
    """Calculates the root mean square (RMS) of a list of numbers.

    RMS = sqrt(mean(x^2)). Used extensively in signal processing,
    electrical engineering, and physics to measure the effective
    magnitude of a varying quantity.

    Args:
        data: A non-empty list of numeric values.

    Returns:
        The RMS value.

    Raises:
        TypeError: If data is not a list of numbers.
        ValueError: If data is empty.

    Example:
        >>> round(root_mean_square([1, 2, 3, 4, 5]), 6)
        3.316625

    Complexity: O(n)
    """
    _validate_numeric_list(data)
    return math.sqrt(sum(x ** 2 for x in data) / len(data))


def weighted_variance(data: List[Union[int, float]],
                      weights: List[Union[int, float]],
                      sample: bool = True) -> float:
    """Calculates the weighted variance of a dataset.

    Uses reliability weights. For populations pass ``sample=False``,
    for samples pass ``sample=True`` which applies Bessel's correction
    adapted for weights.

    Args:
        data: List of numeric values.
        weights: Corresponding list of non-negative weights.
        sample: If True, apply Bessel's correction for sample variance.

    Returns:
        Weighted variance.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists are empty or of different length.

    Example:
        >>> round(weighted_variance([2, 4, 6], [1, 2, 1], sample=False), 6)
        2.0

    Complexity: O(n)
    """
    _validate_numeric_list(data, min_length=2 if sample else 1)

    if not isinstance(weights, list) or not all(isinstance(w, (int, float)) for w in weights):
        raise TypeError("weights must be a list of numeric values.")

    if len(data) != len(weights):
        raise ValueError("data and weights must have the same length.")

    if any(w < 0 for w in weights):
        raise ValueError("All weights must be non-negative.")

    w_sum = sum(weights)

    if w_sum == 0:
        raise ValueError("Sum of weights must be positive.")

    w_mean = sum(d * w for d, w in zip(data, weights)) / w_sum
    ss = sum(w * (d - w_mean) ** 2 for d, w in zip(data, weights))

    if sample:
        w_sum_sq = sum(w ** 2 for w in weights)
        denom = w_sum - w_sum_sq / w_sum

        if denom <= 0:
            raise ValueError("Effective degrees of freedom too small for sample variance.")

        return ss / denom

    return ss / w_sum


def auto_correlation(data: List[Union[int, float]], lag: int = 1) -> float:
    """Calculates the autocorrelation of a time series at a given lag.

    Measures how a signal correlates with a delayed copy of itself.
    Returns a value in [-1, 1].

    Args:
        data: A list of numeric values (time series).
        lag: Number of periods to shift (must be >= 0 and < len(data)).

    Returns:
        Autocorrelation coefficient at the given lag.

    Raises:
        TypeError: If data is not a list of numbers.
        ValueError: If lag is out of range or data too short.

    Example:
        >>> round(auto_correlation([1, 2, 3, 4, 5, 6, 7], 1), 6)
        0.761905

    Complexity: O(n)
    """
    _validate_numeric_list(data, min_length=2)

    if not isinstance(lag, int):
        raise TypeError("lag must be an integer.")

    if lag < 0 or lag >= len(data):
        raise ValueError("lag must be >= 0 and < len(data).")

    if lag == 0:
        return 1.0

    n = len(data)
    mean_val = sum(data) / n
    variance = sum((x - mean_val) ** 2 for x in data) / n

    if variance == 0:
        return 0.0

    covar = sum((data[i] - mean_val) * (data[i + lag] - mean_val) for i in range(n - lag)) / n
    return covar / variance


def kendall_tau(data1: List[Union[int, float]],
                data2: List[Union[int, float]]) -> float:
    """Calculates the Kendall rank correlation coefficient (tau-b).

    A non-parametric measure of the ordinal association between two
    ranked datasets. Handles tied pairs.

    Args:
        data1: First list of numeric values.
        data2: Second list of numeric values (same length as data1).

    Returns:
        Kendall tau-b in the range [-1, 1].

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists have different lengths or fewer than 2 elements.

    Example:
        >>> round(kendall_tau([1, 2, 3, 4, 5], [5, 6, 7, 8, 7]), 6)
        0.738549

    Complexity: O(n^2)
    """
    _validate_numeric_list(data1, min_length=2)
    _validate_numeric_list(data2, min_length=2)

    if len(data1) != len(data2):
        raise ValueError("data1 and data2 must have the same length.")

    n = len(data1)
    concordant = 0
    discordant = 0
    tied_x = 0
    tied_y = 0

    for i in range(n):

        for j in range(i + 1, n):
            dx = data1[i] - data1[j]
            dy = data2[i] - data2[j]
            product = dx * dy

            if product > 0:
                concordant += 1
            elif product < 0:
                discordant += 1
            else:
                if dx == 0:
                    tied_x += 1
                if dy == 0:
                    tied_y += 1

    total_pairs = n * (n - 1) / 2
    denom = math.sqrt((total_pairs - tied_x) * (total_pairs - tied_y))

    if denom == 0:
        return 0.0

    return (concordant - discordant) / denom


def quantile(data: List[Union[int, float]], q: float) -> float:
    """Calculates the q-th quantile of a dataset using linear interpolation.

    Equivalent to the exclusive percentile with interpolation.
    Generalization of median (q=0.5), quartiles, and percentiles.

    Args:
        data: A non-empty list of numeric values.
        q: Quantile to compute, in [0, 1].

    Returns:
        The q-th quantile value.

    Raises:
        TypeError: If data is not a list of numbers or q is not numeric.
        ValueError: If q is outside [0, 1] or data is empty.

    Example:
        >>> quantile([1, 2, 3, 4, 5], 0.25)
        2.0
        >>> quantile([1, 2, 3, 4, 5], 0.5)
        3.0

    Complexity: O(n log n)
    """
    _validate_numeric_list(data)

    if not isinstance(q, (int, float)):
        raise TypeError("q must be a numeric value.")

    if q < 0 or q > 1:
        raise ValueError("q must be in the range [0, 1].")

    sorted_data = sorted(data)
    n = len(sorted_data)

    if q == 0:
        return float(sorted_data[0])

    if q == 1:
        return float(sorted_data[-1])

    pos = q * (n - 1)
    low = int(pos)
    high = low + 1
    frac = pos - low

    if high >= n:
        return float(sorted_data[-1])

    return sorted_data[low] + frac * (sorted_data[high] - sorted_data[low])


def root_mean_squared_error(
    actual: List[Union[int, float]],
    predicted: List[Union[int, float]],
) -> float:
    """Computes the Root Mean Squared Error between actual and predicted values.

    RMSE = sqrt((1/n) * Σ(actual_i − predicted_i)²).

    Args:
        actual: List of observed values.
        predicted: List of predicted values (same length as actual).

    Returns:
        The root mean squared error.

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists are empty or different lengths.

    Example:
        >>> round(root_mean_squared_error([3, -0.5, 2, 7], [2.5, 0.0, 2, 8]), 4)
        0.6124

    Complexity: O(n)
    """
    _validate_numeric_list(actual)
    _validate_numeric_list(predicted)

    if len(actual) != len(predicted):
        raise ValueError("actual and predicted must have the same length.")

    mse = sum((a - p) ** 2 for a, p in zip(actual, predicted)) / len(actual)
    return math.sqrt(mse)


def relative_standard_deviation(data: List[Union[int, float]]) -> float:
    """Computes the Relative Standard Deviation (coefficient of variation) as a percentage.

    RSD = (sample_std / mean) * 100.

    Args:
        data: A non-empty list of numeric values with a non-zero mean.

    Returns:
        The relative standard deviation as a percentage.

    Raises:
        TypeError: If data is not a list of numbers.
        ValueError: If data is empty or the mean is zero.

    Example:
        >>> round(relative_standard_deviation([10, 12, 11, 9, 13]), 2)
        14.37

    Complexity: O(n)
    """
    _validate_numeric_list(data, min_length=2)

    avg = sum(data) / len(data)

    if avg == 0:
        raise ValueError("Cannot compute RSD when the mean is zero.")

    n = len(data)
    var = sum((x - avg) ** 2 for x in data) / (n - 1)
    return (math.sqrt(var) / abs(avg)) * 100


def gini_coefficient(data: List[Union[int, float]]) -> float:
    """Computes the Gini coefficient measuring statistical dispersion.

    A Gini of 0 represents perfect equality; 1 represents maximal inequality.
    Uses the relative mean absolute difference formula.

    Args:
        data: A non-empty list of non-negative numeric values.

    Returns:
        The Gini coefficient in [0, 1].

    Raises:
        TypeError: If data is not a list of numbers.
        ValueError: If data is empty or contains negative values.

    Example:
        >>> gini_coefficient([1, 1, 1, 1])
        0.0
        >>> round(gini_coefficient([1, 2, 3, 4, 5]), 4)
        0.2667
        >>> round(gini_coefficient([0, 0, 0, 0, 100]), 2)
        0.8

    Complexity: O(n²)
    """
    _validate_numeric_list(data)

    if any(x < 0 for x in data):
        raise ValueError("All values must be non-negative.")

    n = len(data)
    total = sum(data)

    if total == 0:
        return 0.0

    abs_diffs = sum(abs(x - y) for i, x in enumerate(data) for y in data[i + 1:])
    return abs_diffs / (n * total) if n > 1 else 0.0


def spearman_rank_correlation(
    data1: List[Union[int, float]],
    data2: List[Union[int, float]],
) -> float:
    """Computes Spearman's rank correlation coefficient.

    A non-parametric measure of rank correlation that assesses how well
    the relationship between two variables can be described using a
    monotonic function.

    Args:
        data1: First list of numeric values.
        data2: Second list of numeric values (same length).

    Returns:
        Spearman's rho in [-1, 1].

    Raises:
        TypeError: If inputs are not lists of numbers.
        ValueError: If lists are empty or different lengths.

    Example:
        >>> round(spearman_rank_correlation([1, 2, 3, 4, 5], [5, 6, 7, 8, 7]), 2)
        0.82

    Complexity: O(n log n)
    """
    _validate_numeric_list(data1, min_length=2)
    _validate_numeric_list(data2, min_length=2)

    if len(data1) != len(data2):
        raise ValueError("data1 and data2 must have the same length.")

    def _rank(values: list) -> list:
        sorted_indices = sorted(range(len(values)), key=lambda i: values[i])
        ranks = [0.0] * len(values)
        i = 0

        while i < len(sorted_indices):
            j = i

            while j < len(sorted_indices) - 1 and values[sorted_indices[j + 1]] == values[sorted_indices[i]]:
                j += 1

            avg_rank = (i + j) / 2.0 + 1

            for k in range(i, j + 1):
                ranks[sorted_indices[k]] = avg_rank

            i = j + 1

        return ranks

    ranks1 = _rank(data1)
    ranks2 = _rank(data2)

    n = len(data1)
    mean1 = sum(ranks1) / n
    mean2 = sum(ranks2) / n

    num = sum((r1 - mean1) * (r2 - mean2) for r1, r2 in zip(ranks1, ranks2))
    den1 = math.sqrt(sum((r1 - mean1) ** 2 for r1 in ranks1))
    den2 = math.sqrt(sum((r2 - mean2) ** 2 for r2 in ranks2))

    if den1 == 0 or den2 == 0:
        return 0.0

    return num / (den1 * den2)


def moving_median(
    data: List[Union[int, float]],
    window: int,
) -> List[Optional[float]]:
    """Computes a rolling median over a sliding window.

    Args:
        data: A list of numeric values.
        window: Size of the sliding window (must be >= 1).

    Returns:
        A list of the same length as data. Elements before the window
        is full are None; subsequent elements are the median of the
        preceding *window* values.

    Raises:
        TypeError: If data is not a list of numbers or window is not int.
        ValueError: If data is empty or window < 1.

    Example:
        >>> moving_median([1, 3, 5, 7, 9], 3)
        [None, None, 3.0, 5.0, 7.0]

    Complexity: O(n * w log w)
    """
    _validate_numeric_list(data)

    if not isinstance(window, int):
        raise TypeError("window must be an integer.")

    if window < 1:
        raise ValueError("window must be >= 1.")

    result: List[Optional[float]] = [None] * (window - 1)

    for i in range(window - 1, len(data)):
        segment = sorted(data[i - window + 1: i + 1])
        mid = len(segment) // 2

        if len(segment) % 2 == 0:
            result.append((segment[mid - 1] + segment[mid]) / 2.0)
        else:
            result.append(float(segment[mid]))

    return result


def minkowski_distance(
    vec_a: List[Union[int, float]],
    vec_b: List[Union[int, float]],
    p: Union[int, float] = 2,
) -> float:
    """Computes the Minkowski distance of order p between two vectors.

    d = (Σ|aᵢ − bᵢ|^p)^(1/p).
    p=1 gives Manhattan, p=2 gives Euclidean.

    Args:
        vec_a: First numeric vector.
        vec_b: Second numeric vector (same length).
        p: Order of the distance (must be >= 1).

    Returns:
        The Lp distance (non-negative float).

    Raises:
        TypeError: If inputs are not lists of numbers or p is not numeric.
        ValueError: If vectors are empty, different lengths, or p < 1.

    Example:
        >>> round(minkowski_distance([1, 2, 3], [4, 6, 3], 3), 4)
        4.4979

    Complexity: O(n)
    """
    _validate_numeric_list(vec_a)
    _validate_numeric_list(vec_b)

    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")

    if p < 1:
        raise ValueError("p must be >= 1.")

    if len(vec_a) != len(vec_b):
        raise ValueError("Vectors must have the same length.")

    total = sum(abs(a - b) ** p for a, b in zip(vec_a, vec_b))
    return total ** (1.0 / p)


def jaccard_similarity(
    set_a: List,
    set_b: List,
) -> float:
    """Computes the Jaccard similarity index between two collections.

    J(A, B) = |A ∩ B| / |A ∪ B|.

    Args:
        set_a: First collection of elements.
        set_b: Second collection of elements.

    Returns:
        A float in [0, 1]. Returns 1.0 if both are empty.

    Raises:
        TypeError: If inputs are not lists.

    Example:
        >>> jaccard_similarity([1, 2, 3], [2, 3, 4])
        0.5

    Complexity: O(n + m)
    """
    if not isinstance(set_a, list) or not isinstance(set_b, list):
        raise TypeError("Both inputs must be lists.")

    a = set(set_a)
    b = set(set_b)

    if not a and not b:
        return 1.0

    intersection = len(a & b)
    union = len(a | b)
    return intersection / union


def rolling_correlation(
    data1: List[Union[int, float]],
    data2: List[Union[int, float]],
    window: int,
) -> List[Optional[float]]:
    """Computes rolling Pearson correlation over a sliding window.

    Args:
        data1: First numeric series.
        data2: Second numeric series (same length).
        window: Size of the sliding window (>= 2).

    Returns:
        A list of the same length. Elements before the window is full
        are None; subsequent elements are the Pearson r.

    Raises:
        TypeError: If inputs are invalid types.
        ValueError: If data is empty, different lengths, or window < 2.

    Example:
        >>> result = rolling_correlation([1,2,3,4,5], [2,4,6,8,10], 3)
        >>> result[:2]
        [None, None]
        >>> round(result[2], 4)
        1.0

    Complexity: O(n * w)
    """
    _validate_numeric_list(data1)
    _validate_numeric_list(data2)

    if len(data1) != len(data2):
        raise ValueError("data1 and data2 must have the same length.")

    if not isinstance(window, int):
        raise TypeError("window must be an integer.")

    if window < 2:
        raise ValueError("window must be >= 2.")

    import math

    n = len(data1)
    result: List[Optional[float]] = [None] * (window - 1)

    for i in range(window - 1, n):
        x_seg = data1[i - window + 1: i + 1]
        y_seg = data2[i - window + 1: i + 1]
        w = len(x_seg)
        mx = sum(x_seg) / w
        my = sum(y_seg) / w
        cov = sum((x_seg[j] - mx) * (y_seg[j] - my) for j in range(w)) / w
        sx = math.sqrt(sum((x_seg[j] - mx) ** 2 for j in range(w)) / w)
        sy = math.sqrt(sum((y_seg[j] - my) ** 2 for j in range(w)) / w)

        if sx == 0 or sy == 0:
            result.append(None)
        else:
            result.append(cov / (sx * sy))

    return result


def cumulative_return(returns: List[Union[int, float]]) -> float:
    """Computes the total cumulative return from a list of periodic returns.

    cumulative = Π(1 + rᵢ) − 1.

    Args:
        returns: List of periodic returns as decimals (e.g. 0.05 = 5%).

    Returns:
        The cumulative return as a decimal.

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If returns is empty or any return <= -1.

    Example:
        >>> round(cumulative_return([0.10, 0.05, -0.02]), 4)
        0.1319

    Complexity: O(n)
    """
    _validate_numeric_list(returns)

    if any(r <= -1 for r in returns):
        raise ValueError("Returns must be greater than -1.")

    product = 1.0

    for r in returns:
        product *= (1 + r)

    return product - 1


def max_drawdown(values: List[Union[int, float]]) -> float:
    """Computes the maximum drawdown of a value series.

    Maximum peak-to-trough decline as a positive fraction.

    Args:
        values: List of portfolio values or price series (positive).

    Returns:
        The maximum drawdown as a positive fraction in [0, 1].

    Raises:
        TypeError: If input is not a list of numbers.
        ValueError: If values is empty or contains non-positive values.

    Example:
        >>> max_drawdown([100, 120, 90, 110, 80])
        0.3333333333333333

    Complexity: O(n)
    """
    _validate_numeric_list(values)

    if any(v <= 0 for v in values):
        raise ValueError("All values must be positive.")

    peak = values[0]
    mdd = 0.0

    for v in values:

        if v > peak:
            peak = v

        dd = (peak - v) / peak

        if dd > mdd:
            mdd = dd

    return mdd


def z_to_percentile(z: Union[int, float]) -> float:
    """Converts a z-score to a percentile (0–100) using the error function.

    percentile = 100 × 0.5 × (1 + erf(z / √2)).

    Args:
        z: Standard z-score.

    Returns:
        Percentile in [0, 100].

    Raises:
        TypeError: If z is not numeric.

    Example:
        >>> round(z_to_percentile(1.96), 2)
        97.5

    Complexity: O(1)
    """
    if not isinstance(z, (int, float)):
        raise TypeError("z must be numeric.")

    import math

    return 100.0 * 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def percentile_to_z(p: Union[int, float]) -> float:
    """Converts a percentile (0–100) to a z-score using inverse erf approximation.

    Uses a rational approximation of the inverse normal CDF.

    Args:
        p: Percentile in (0, 100) exclusive.

    Returns:
        The z-score.

    Raises:
        TypeError: If p is not numeric.
        ValueError: If p is not in (0, 100).

    Example:
        >>> round(percentile_to_z(97.5), 2)
        1.96

    Complexity: O(1)
    """
    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")

    if p <= 0 or p >= 100:
        raise ValueError("p must be in the open interval (0, 100).")

    import math

    prob = p / 100.0

    # Rational approximation (Abramowitz & Stegun 26.2.23)
    if prob < 0.5:
        t = math.sqrt(-2.0 * math.log(prob))
    else:
        t = math.sqrt(-2.0 * math.log(1.0 - prob))

    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308

    z_abs = t - (c0 + c1 * t + c2 * t * t) / (1.0 + d1 * t + d2 * t * t + d3 * t * t * t)

    return z_abs if prob >= 0.5 else -z_abs


def relu(x: Union[int, float]) -> Union[int, float]:
    """Compute the Rectified Linear Unit: max(0, x).

    Args:
        x: Input value.

    Returns:
        max(0, x).

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> relu(-3)
        0
        >>> relu(5)
        5

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    return max(0, x)


def binary_entropy(p: Union[int, float]) -> float:
    """Compute binary (Bernoulli) entropy: -p*log2(p) - (1-p)*log2(1-p).

    Measures uncertainty of a single binary event.

    Args:
        p: Probability in [0, 1].

    Returns:
        Binary entropy in bits, in [0, 1].

    Raises:
        TypeError: If p is not numeric.
        ValueError: If p is not in [0, 1].

    Example:
        >>> binary_entropy(0.5)
        1.0

    Complexity: O(1)
    """
    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")

    if p < 0 or p > 1:
        raise ValueError("p must be in [0, 1].")

    if p == 0 or p == 1:
        return 0.0

    import math

    return -p * math.log2(p) - (1 - p) * math.log2(1 - p)


def leaky_relu(x: Union[int, float], alpha: float = 0.01) -> float:
    """Compute Leaky Rectified Linear Unit: x if x > 0 else alpha * x.

    Args:
        x: Input value.
        alpha: Slope for negative values (default 0.01).

    Returns:
        Leaky ReLU of x.

    Raises:
        TypeError: If x or alpha is not numeric.

    Example:
        >>> leaky_relu(5)
        5
        >>> leaky_relu(-10)
        -0.1

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(alpha, (int, float)):
        raise TypeError("alpha must be numeric.")

    return float(x) if x > 0 else float(alpha * x)


def elu(x: Union[int, float], alpha: float = 1.0) -> float:
    """Compute Exponential Linear Unit: x if x > 0, else alpha * (exp(x) - 1).

    Args:
        x: Input value.
        alpha: Scale for negative values (default 1.0).

    Returns:
        ELU of x.

    Raises:
        TypeError: If x or alpha is not numeric.

    Example:
        >>> elu(1.0)
        1.0
        >>> round(elu(-1.0), 4)
        -0.6321

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(alpha, (int, float)):
        raise TypeError("alpha must be numeric.")

    if x > 0:
        return float(x)

    import math

    return float(alpha * (math.exp(x) - 1))


def swish(x: Union[int, float]) -> float:
    """Compute Swish activation: x * sigmoid(x).

    Self-gated activation function proposed by Google Brain.

    Args:
        x: Input value.

    Returns:
        Swish of x.

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> swish(0)
        0.0
        >>> round(swish(1), 4)
        0.7311

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    import math

    if x >= 0:
        s = 1.0 / (1.0 + math.exp(-x))
    else:
        exp_x = math.exp(x)
        s = exp_x / (1.0 + exp_x)

    return float(x * s)


def huber_loss(
    y_true: Union[int, float],
    y_pred: Union[int, float],
    delta: Union[int, float] = 1.0,
) -> float:
    """Compute the Huber loss for a single prediction.

    Less sensitive to outliers than squared error. Equals squared error
    for small residuals and absolute error for large residuals.

    Args:
        y_true: True value.
        y_pred: Predicted value.
        delta: Threshold at which to switch from squared to linear (positive).

    Returns:
        Huber loss value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If delta is not positive.

    Example:
        >>> huber_loss(1.0, 1.5)
        0.125
        >>> huber_loss(1.0, 5.0)
        3.5

    Complexity: O(1)
    """
    if not isinstance(y_true, (int, float)):
        raise TypeError("y_true must be numeric.")

    if not isinstance(y_pred, (int, float)):
        raise TypeError("y_pred must be numeric.")

    if not isinstance(delta, (int, float)):
        raise TypeError("delta must be numeric.")

    if delta <= 0:
        raise ValueError("delta must be positive.")

    a = abs(y_true - y_pred)

    if a <= delta:
        return 0.5 * a * a

    return delta * (a - 0.5 * delta)


def relative_error(
    measured: Union[int, float],
    actual: Union[int, float],
) -> float:
    """Compute the relative error: |measured - actual| / |actual|.

    Args:
        measured: Measured/observed value.
        actual: True/expected value.

    Returns:
        Relative error as a non-negative float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If actual is zero.

    Example:
        >>> relative_error(10.5, 10.0)
        0.05

    Complexity: O(1)
    """
    if not isinstance(measured, (int, float)):
        raise TypeError("measured must be numeric.")

    if not isinstance(actual, (int, float)):
        raise TypeError("actual must be numeric.")

    if actual == 0:
        raise ValueError("actual must not be zero.")

    return abs(measured - actual) / abs(actual)


def absolute_error(
    measured: Union[int, float],
    actual: Union[int, float],
) -> float:
    """Compute the absolute error: |measured - actual|.

    Args:
        measured: Measured/observed value.
        actual: True/expected value.

    Returns:
        Absolute error as a non-negative float.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> absolute_error(10.5, 10.0)
        0.5

    Complexity: O(1)
    """
    if not isinstance(measured, (int, float)):
        raise TypeError("measured must be numeric.")

    if not isinstance(actual, (int, float)):
        raise TypeError("actual must be numeric.")

    return float(abs(measured - actual))


def gelu(x: Union[int, float]) -> float:
    """Compute the Gaussian Error Linear Unit activation.

    GELU(x) = x * Φ(x) where Φ is the standard normal CDF.
    Uses the tanh approximation: 0.5*x*(1+tanh(sqrt(2/π)*(x+0.044715*x³)))

    Args:
        x: Input value.

    Returns:
        GELU of x.

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> round(gelu(1.0), 4)
        0.8412

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    import math

    c = math.sqrt(2.0 / math.pi)
    return 0.5 * x * (1.0 + math.tanh(c * (x + 0.044715 * x * x * x)))


def mish(x: Union[int, float]) -> float:
    """Compute Mish activation: x * tanh(softplus(x)).

    A self-regularized non-monotonic activation proposed by Misra (2019).

    Args:
        x: Input value.

    Returns:
        Mish of x.

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> round(mish(1.0), 4)
        0.8651

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    import math

    # softplus(x) = ln(1 + exp(x)), numerically stable
    if x > 20:
        sp = float(x)
    else:
        sp = math.log1p(math.exp(x))

    return float(x * math.tanh(sp))


def hinge_loss(
    y_true: Union[int, float],
    y_pred: Union[int, float],
) -> float:
    """Compute hinge loss for a single sample.

    Used in SVM classifiers. L = max(0, 1 - y_true * y_pred).
    y_true should be -1 or +1.

    Args:
        y_true: True label (-1 or +1).
        y_pred: Predicted score (real-valued).

    Returns:
        Hinge loss value (non-negative).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If y_true is not -1 or +1.

    Example:
        >>> hinge_loss(1, 0.8)
        0.19999999999999996
        >>> hinge_loss(1, 2.0)
        0

    Complexity: O(1)
    """
    if not isinstance(y_true, (int, float)):
        raise TypeError("y_true must be numeric.")

    if not isinstance(y_pred, (int, float)):
        raise TypeError("y_pred must be numeric.")

    if y_true not in (-1, 1):
        raise ValueError("y_true must be -1 or +1.")

    return max(0, 1 - y_true * y_pred)


def log_loss(
    y_true: int,
    y_pred: Union[int, float],
    eps: float = 1e-15,
) -> float:
    """Compute binary cross-entropy (log loss) for a single sample.

    L = -(y*ln(p) + (1-y)*ln(1-p))

    Args:
        y_true: True label (0 or 1).
        y_pred: Predicted probability in (0, 1).
        eps: Clipping epsilon to avoid log(0).

    Returns:
        Log loss value (non-negative).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If y_true is not 0 or 1, or y_pred not in [0, 1].

    Example:
        >>> round(log_loss(1, 0.9), 4)
        0.1054

    Complexity: O(1)
    """
    if not isinstance(y_true, int):
        raise TypeError("y_true must be an integer.")

    if not isinstance(y_pred, (int, float)):
        raise TypeError("y_pred must be numeric.")

    if y_true not in (0, 1):
        raise ValueError("y_true must be 0 or 1.")

    if y_pred < 0 or y_pred > 1:
        raise ValueError("y_pred must be in [0, 1].")

    import math

    # Clip to avoid log(0)
    p = max(eps, min(1 - eps, y_pred))

    return -(y_true * math.log(p) + (1 - y_true) * math.log(1 - p))


def tanh_activation(x: Union[int, float]) -> float:
    """Compute the hyperbolic tangent activation function.

    Convenience wrapper mapping any numeric input to (-1, 1).

    Args:
        x: Input value.

    Returns:
        tanh(x) in the range (-1, 1).

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> tanh_activation(0)
        0.0
        >>> round(tanh_activation(1), 4)
        0.7616

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    import math

    return math.tanh(x)


def focal_loss(
    y_true: Union[int, float],
    y_pred: Union[int, float],
    gamma: Union[int, float] = 2.0,
    alpha: Union[int, float] = 0.25,
) -> float:
    """Calculate focal loss for a single sample.

    FL(p_t) = -α_t * (1 - p_t)^γ * log(p_t)

    Args:
        y_true: True label (0 or 1).
        y_pred: Predicted probability in (0, 1).
        gamma: Focusing parameter (default 2.0).
        alpha: Balancing factor (default 0.25).

    Returns:
        Focal loss value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If y_true not in {0, 1} or y_pred not in (0, 1).

    Example:
        >>> round(focal_loss(1, 0.9), 6)
        0.000264

    Complexity: O(1)
    """
    if not isinstance(y_true, (int, float)):
        raise TypeError("y_true must be numeric.")

    if not isinstance(y_pred, (int, float)):
        raise TypeError("y_pred must be numeric.")

    if not isinstance(gamma, (int, float)):
        raise TypeError("gamma must be numeric.")

    if not isinstance(alpha, (int, float)):
        raise TypeError("alpha must be numeric.")

    if y_true not in (0, 1):
        raise ValueError("y_true must be 0 or 1.")

    if not 0 < y_pred < 1:
        raise ValueError("y_pred must be between 0 and 1 exclusive.")

    import math

    if y_true == 1:
        pt = y_pred
        at = alpha
    else:
        pt = 1.0 - y_pred
        at = 1.0 - alpha

    return float(-at * (1.0 - pt) ** gamma * math.log(pt))


def mean_bias_error(
    measured: Union[int, float],
    actual: Union[int, float],
) -> float:
    """Calculate mean bias error for a single observation: measured - actual.

    A positive value indicates overestimation, negative indicates underestimation.

    Args:
        measured: Measured/predicted value.
        actual: Actual/true value.

    Returns:
        Signed error (bias).

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> mean_bias_error(105, 100)
        5.0

    Complexity: O(1)
    """
    if not isinstance(measured, (int, float)):
        raise TypeError("measured must be numeric.")

    if not isinstance(actual, (int, float)):
        raise TypeError("actual must be numeric.")

    return float(measured - actual)


def dice_coefficient_scalar(
    tp: Union[int, float],
    fp: Union[int, float],
    fn: Union[int, float],
) -> float:
    """Calculate the Sørensen–Dice coefficient from counts: 2·TP / (2·TP + FP + FN).

    Args:
        tp: True positives count.
        fp: False positives count.
        fn: False negatives count.

    Returns:
        Dice coefficient in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any count is negative or all are zero.

    Example:
        >>> dice_coefficient_scalar(30, 10, 5)
        0.8

    Complexity: O(1)
    """
    if not isinstance(tp, (int, float)):
        raise TypeError("tp must be numeric.")

    if not isinstance(fp, (int, float)):
        raise TypeError("fp must be numeric.")

    if not isinstance(fn, (int, float)):
        raise TypeError("fn must be numeric.")

    if tp < 0 or fp < 0 or fn < 0:
        raise ValueError("counts must be non-negative.")

    denom = 2 * tp + fp + fn

    if denom == 0:
        raise ValueError("all counts are zero; coefficient is undefined.")

    return float(2 * tp / denom)


def exponential_decay_rate(
    initial: Union[int, float],
    final: Union[int, float],
    time: Union[int, float],
) -> float:
    """Calculate the decay constant λ given initial/final values and time.

    N(t) = N₀ * e^(-λt)  →  λ = -ln(N_final / N_initial) / t

    Args:
        initial: Initial value (> 0).
        final: Final value (> 0, ≤ initial).
        time: Elapsed time (> 0).

    Returns:
        Decay constant λ.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If constraints violated.

    Example:
        >>> round(exponential_decay_rate(100, 50, 5), 4)
        0.1386

    Complexity: O(1)
    """
    if not isinstance(initial, (int, float)):
        raise TypeError("initial must be numeric.")

    if not isinstance(final, (int, float)):
        raise TypeError("final must be numeric.")

    if not isinstance(time, (int, float)):
        raise TypeError("time must be numeric.")

    if initial <= 0 or final <= 0:
        raise ValueError("initial and final must be positive.")

    if final > initial:
        raise ValueError("final must not exceed initial.")

    if time <= 0:
        raise ValueError("time must be positive.")

    import math

    return float(-math.log(final / initial) / time)


def z_score_single(
    value: Union[int, float],
    mean: Union[int, float],
    std_dev: Union[int, float],
) -> float:
    """Calculate the z-score of a single observation: (x - μ) / σ.

    Args:
        value: Observation.
        mean: Population mean.
        std_dev: Population standard deviation.

    Returns:
        Z-score.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If std_dev is not positive.

    Example:
        >>> z_score_single(85, 70, 10)
        1.5

    Complexity: O(1)
    """
    if not isinstance(value, (int, float)):
        raise TypeError("value must be numeric.")

    if not isinstance(mean, (int, float)):
        raise TypeError("mean must be numeric.")

    if not isinstance(std_dev, (int, float)):
        raise TypeError("std_dev must be numeric.")

    if std_dev <= 0:
        raise ValueError("std_dev must be positive.")

    return float((value - mean) / std_dev)


def recall_score_scalar(
    tp: Union[int, float],
    fn: Union[int, float],
) -> float:
    """Calculate recall (sensitivity) from counts: TP / (TP + FN).

    Args:
        tp: True positives.
        fn: False negatives.

    Returns:
        Recall in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If counts are negative or both zero.

    Example:
        >>> recall_score_scalar(80, 20)
        0.8

    Complexity: O(1)
    """
    if not isinstance(tp, (int, float)):
        raise TypeError("tp must be numeric.")

    if not isinstance(fn, (int, float)):
        raise TypeError("fn must be numeric.")

    if tp < 0 or fn < 0:
        raise ValueError("counts must be non-negative.")

    denom = tp + fn

    if denom == 0:
        raise ValueError("tp + fn must be positive.")

    return float(tp / denom)


def precision_score_scalar(
    tp: Union[int, float],
    fp: Union[int, float],
) -> float:
    """Calculate precision from counts: TP / (TP + FP).

    Args:
        tp: True positives.
        fp: False positives.

    Returns:
        Precision in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If counts are negative or both zero.

    Example:
        >>> precision_score_scalar(80, 20)
        0.8

    Complexity: O(1)
    """
    if not isinstance(tp, (int, float)):
        raise TypeError("tp must be numeric.")

    if not isinstance(fp, (int, float)):
        raise TypeError("fp must be numeric.")

    if tp < 0 or fp < 0:
        raise ValueError("counts must be non-negative.")

    denom = tp + fp

    if denom == 0:
        raise ValueError("tp + fp must be positive.")

    return float(tp / denom)


def f1_score_scalar(
    tp: Union[int, float],
    fp: Union[int, float],
    fn: Union[int, float],
) -> float:
    """Calculate F1-score from counts: 2·TP / (2·TP + FP + FN).

    The harmonic mean of precision and recall.

    Args:
        tp: True positives.
        fp: False positives.
        fn: False negatives.

    Returns:
        F1-score in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If counts are negative or denominator is zero.

    Example:
        >>> f1_score_scalar(80, 10, 20)
        0.8421052631578947

    Complexity: O(1)
    """
    if not isinstance(tp, (int, float)):
        raise TypeError("tp must be numeric.")

    if not isinstance(fp, (int, float)):
        raise TypeError("fp must be numeric.")

    if not isinstance(fn, (int, float)):
        raise TypeError("fn must be numeric.")

    if tp < 0 or fp < 0 or fn < 0:
        raise ValueError("counts must be non-negative.")

    denom = 2 * tp + fp + fn

    if denom == 0:
        raise ValueError("denominator (2*tp + fp + fn) must be positive.")

    return float(2 * tp / denom)


def specificity_score_scalar(
    tn: Union[int, float],
    fp: Union[int, float],
) -> float:
    """Calculate specificity (true negative rate): TN / (TN + FP).

    Args:
        tn: True negatives.
        fp: False positives.

    Returns:
        Specificity in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If counts are negative or both zero.

    Example:
        >>> specificity_score_scalar(900, 100)
        0.9

    Complexity: O(1)
    """
    if not isinstance(tn, (int, float)):
        raise TypeError("tn must be numeric.")

    if not isinstance(fp, (int, float)):
        raise TypeError("fp must be numeric.")

    if tn < 0 or fp < 0:
        raise ValueError("counts must be non-negative.")

    denom = tn + fp

    if denom == 0:
        raise ValueError("tn + fp must be positive.")

    return float(tn / denom)


def matthews_corrcoef_scalar(
    tp: Union[int, float],
    tn: Union[int, float],
    fp: Union[int, float],
    fn: Union[int, float],
) -> float:
    """Calculate Matthews Correlation Coefficient from confusion matrix counts.

    MCC = (TP·TN - FP·FN) / √((TP+FP)(TP+FN)(TN+FP)(TN+FN))

    Args:
        tp: True positives.
        tn: True negatives.
        fp: False positives.
        fn: False negatives.

    Returns:
        MCC in [-1, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If counts are negative or denominator is zero.

    Example:
        >>> round(matthews_corrcoef_scalar(80, 900, 100, 20), 4)
        0.5765

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (tp, tn, fp, fn)):
        raise TypeError("all inputs must be numeric.")

    if any(v < 0 for v in (tp, tn, fp, fn)):
        raise ValueError("counts must be non-negative.")

    import math

    numer = tp * tn - fp * fn
    denom_sq = (tp + fp) * (tp + fn) * (tn + fp) * (tn + fn)

    if denom_sq == 0:
        raise ValueError("MCC is undefined when a row or column of the confusion matrix is zero.")

    return float(numer / math.sqrt(denom_sq))


def odds_ratio(
    tp: Union[int, float],
    tn: Union[int, float],
    fp: Union[int, float],
    fn: Union[int, float],
) -> float:
    """Calculate the odds ratio from a 2×2 confusion matrix.

    OR = (TP × TN) / (FP × FN)

    Args:
        tp: True positives.
        tn: True negatives.
        fp: False positives.
        fn: False negatives.

    Returns:
        Odds ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If counts are negative or denominator is zero.

    Example:
        >>> odds_ratio(80, 900, 100, 20)
        360.0

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (tp, tn, fp, fn)):
        raise TypeError("all inputs must be numeric.")

    if any(v < 0 for v in (tp, tn, fp, fn)):
        raise ValueError("counts must be non-negative.")

    denom = fp * fn

    if denom == 0:
        raise ValueError("FP * FN must be positive (denominator cannot be zero).")

    return float((tp * tn) / denom)


def risk_ratio(
    exposed_events: Union[int, float],
    exposed_total: Union[int, float],
    control_events: Union[int, float],
    control_total: Union[int, float],
) -> float:
    """Calculate the relative risk (risk ratio): RR = (a/n₁) / (c/n₂).

    Args:
        exposed_events: Events in exposed group.
        exposed_total: Total in exposed group.
        control_events: Events in control group.
        control_total: Total in control group.

    Returns:
        Risk ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If totals not positive or control risk is zero.

    Example:
        >>> risk_ratio(30, 100, 10, 100)
        3.0

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (exposed_events, exposed_total, control_events, control_total)):
        raise TypeError("all inputs must be numeric.")

    if exposed_total <= 0 or control_total <= 0:
        raise ValueError("totals must be positive.")

    control_risk = control_events / control_total

    if control_risk == 0:
        raise ValueError("control risk must be positive.")

    return float((exposed_events / exposed_total) / control_risk)


def balanced_accuracy_scalar(
    tp: Union[int, float],
    tn: Union[int, float],
    fp: Union[int, float],
    fn: Union[int, float],
) -> float:
    """Calculate balanced accuracy: (Sensitivity + Specificity) / 2.

    Args:
        tp: True positives.
        tn: True negatives.
        fp: False positives.
        fn: False negatives.

    Returns:
        Balanced accuracy in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If counts are negative or denominators are zero.

    Example:
        >>> balanced_accuracy_scalar(80, 900, 100, 20)
        0.85

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (tp, tn, fp, fn)):
        raise TypeError("all inputs must be numeric.")

    if any(v < 0 for v in (tp, tn, fp, fn)):
        raise ValueError("counts must be non-negative.")

    sens_denom = tp + fn
    spec_denom = tn + fp

    if sens_denom == 0 or spec_denom == 0:
        raise ValueError("tp+fn and tn+fp must both be positive.")

    sensitivity = tp / sens_denom
    specificity = tn / spec_denom

    return float((sensitivity + specificity) / 2.0)


def negative_predictive_value(
    tn: Union[int, float],
    fn: Union[int, float],
) -> float:
    """Calculate Negative Predictive Value: NPV = TN / (TN + FN).

    Args:
        tn: True negatives.
        fn: False negatives.

    Returns:
        NPV in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If counts negative or both zero.

    Example:
        >>> negative_predictive_value(900, 20)
        0.9782608695652174

    Complexity: O(1)
    """
    if not isinstance(tn, (int, float)):
        raise TypeError("tn must be numeric.")

    if not isinstance(fn, (int, float)):
        raise TypeError("fn must be numeric.")

    if tn < 0 or fn < 0:
        raise ValueError("counts must be non-negative.")

    denom = tn + fn

    if denom == 0:
        raise ValueError("tn + fn must be positive.")

    return float(tn / denom)


def false_discovery_rate(
    fp: Union[int, float],
    tp: Union[int, float],
) -> float:
    """Calculate False Discovery Rate: FDR = FP / (FP + TP).

    Args:
        fp: False positives.
        tp: True positives.

    Returns:
        FDR in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If counts negative or both zero.

    Example:
        >>> false_discovery_rate(100, 80)
        0.5555555555555556

    Complexity: O(1)
    """
    if not isinstance(fp, (int, float)):
        raise TypeError("fp must be numeric.")

    if not isinstance(tp, (int, float)):
        raise TypeError("tp must be numeric.")

    if fp < 0 or tp < 0:
        raise ValueError("counts must be non-negative.")

    denom = fp + tp

    if denom == 0:
        raise ValueError("fp + tp must be positive.")

    return float(fp / denom)


def jaccard_index_scalar(
    tp: Union[int, float],
    fp: Union[int, float],
    fn: Union[int, float],
) -> float:
    """Calculate the Jaccard index from scalar confusion-matrix counts.

    J = TP / (TP + FP + FN)

    Args:
        tp: True positives.
        fp: False positives.
        fn: False negatives.

    Returns:
        Jaccard index in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If tp + fp + fn is zero.

    Example:
        >>> jaccard_index_scalar(50, 10, 5)
        0.7692307692307693

    Complexity: O(1)
    """
    if not isinstance(tp, (int, float)) or not isinstance(fp, (int, float)) or not isinstance(fn, (int, float)):
        raise TypeError("tp, fp, fn must be numeric.")

    denom = tp + fp + fn

    if denom == 0:
        raise ValueError("tp + fp + fn must be positive.")

    return float(tp / denom)


def cosine_similarity_scalar(
    a1: Union[int, float],
    a2: Union[int, float],
    b1: Union[int, float],
    b2: Union[int, float],
) -> float:
    """Calculate cosine similarity between two 2D vectors (a1,a2) and (b1,b2).

    Args:
        a1: First component of vector A.
        a2: Second component of vector A.
        b1: First component of vector B.
        b2: Second component of vector B.

    Returns:
        Cosine similarity in [-1, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If either vector has zero magnitude.

    Example:
        >>> cosine_similarity_scalar(1, 0, 0, 1)
        0.0

    Complexity: O(1)
    """
    import math

    if not all(isinstance(v, (int, float)) for v in (a1, a2, b1, b2)):
        raise TypeError("All inputs must be numeric.")

    dot = a1 * b1 + a2 * b2
    mag_a = math.sqrt(a1 ** 2 + a2 ** 2)
    mag_b = math.sqrt(b1 ** 2 + b2 ** 2)

    if mag_a == 0 or mag_b == 0:
        raise ValueError("Vectors must have non-zero magnitude.")

    return float(dot / (mag_a * mag_b))


def r_squared_scalar(
    ss_res: Union[int, float],
    ss_tot: Union[int, float],
) -> float:
    """Calculate the coefficient of determination (R²).

    R² = 1 - SS_res / SS_tot

    Args:
        ss_res: Residual sum of squares.
        ss_tot: Total sum of squares.

    Returns:
        R-squared value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If ss_tot is zero.

    Example:
        >>> r_squared_scalar(20, 100)
        0.8

    Complexity: O(1)
    """
    if not isinstance(ss_res, (int, float)) or not isinstance(ss_tot, (int, float)):
        raise TypeError("ss_res and ss_tot must be numeric.")

    if ss_tot == 0:
        raise ValueError("ss_tot must not be zero.")

    return float(1.0 - ss_res / ss_tot)


def mean_percentage_error(
    actual: Union[int, float],
    predicted: Union[int, float],
) -> float:
    """Calculate mean percentage error for a single observation.

    MPE = (actual - predicted) / actual * 100

    Args:
        actual: Actual (true) value.
        predicted: Predicted value.

    Returns:
        Percentage error (positive = underestimate).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If actual is zero.

    Example:
        >>> mean_percentage_error(100, 90)
        10.0

    Complexity: O(1)
    """
    if not isinstance(actual, (int, float)) or not isinstance(predicted, (int, float)):
        raise TypeError("actual and predicted must be numeric.")

    if actual == 0:
        raise ValueError("actual must not be zero.")

    return float((actual - predicted) / actual * 100)


def symmetric_mape(
    actual: Union[int, float],
    predicted: Union[int, float],
) -> float:
    """Calculate symmetric mean absolute percentage error for a single observation.

    sMAPE = |actual - predicted| / ((|actual| + |predicted|) / 2) * 100

    Args:
        actual: Actual (true) value.
        predicted: Predicted value.

    Returns:
        sMAPE value in [0, 200].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If both actual and predicted are zero.

    Example:
        >>> symmetric_mape(100, 80)
        22.22222222222222

    Complexity: O(1)
    """
    if not isinstance(actual, (int, float)) or not isinstance(predicted, (int, float)):
        raise TypeError("actual and predicted must be numeric.")

    denom = (abs(actual) + abs(predicted)) / 2.0

    if denom == 0:
        raise ValueError("Cannot compute sMAPE when both values are zero.")

    return float(abs(actual - predicted) / denom * 100)


def log_cosh_loss(
    actual: Union[int, float],
    predicted: Union[int, float],
) -> float:
    """Calculate the log-cosh loss for a single observation.

    L = log(cosh(predicted - actual))

    Args:
        actual: True value.
        predicted: Predicted value.

    Returns:
        Log-cosh loss (always non-negative).

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> round(log_cosh_loss(3, 5), 6)
        1.32461

    Complexity: O(1)
    """
    import math

    if not isinstance(actual, (int, float)) or not isinstance(predicted, (int, float)):
        raise TypeError("actual and predicted must be numeric.")

    diff = predicted - actual

    return float(math.log(math.cosh(diff)))


def poisson_probability(
    k: int,
    lam: Union[int, float],
) -> float:
    """Calculate Poisson probability P(X=k) = e^(-λ) · λ^k / k!.

    Args:
        k: Number of observed events (non-negative integer).
        lam: Expected rate (λ > 0).

    Returns:
        Probability of exactly k events.

    Raises:
        TypeError: If k is not int or lam not numeric.
        ValueError: If k < 0 or lam <= 0.

    Example:
        >>> round(poisson_probability(3, 2.5), 6)
        0.213763

    Complexity: O(k)
    """
    import math

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if not isinstance(lam, (int, float)):
        raise TypeError("lam must be numeric.")

    if k < 0:
        raise ValueError("k must be non-negative.")

    if lam <= 0:
        raise ValueError("lam must be positive.")

    return float(math.exp(-lam) * lam ** k / math.factorial(k))


def entropy_binary(
    p: Union[int, float],
) -> float:
    """Calculate binary entropy H(p) = -p·log₂(p) - (1-p)·log₂(1-p).

    Args:
        p: Probability of positive class, in (0, 1).

    Returns:
        Binary entropy in bits.

    Raises:
        TypeError: If p is not numeric.
        ValueError: If p not in (0, 1).

    Example:
        >>> round(entropy_binary(0.5), 6)
        1.0

    Complexity: O(1)
    """
    import math

    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")

    if p <= 0 or p >= 1:
        raise ValueError("p must be in (0, 1).")

    return float(-p * math.log2(p) - (1 - p) * math.log2(1 - p))


def gini_impurity_binary(
    p: Union[int, float],
) -> float:
    """Calculate binary Gini impurity G = 2·p·(1-p).

    Args:
        p: Probability of positive class, in [0, 1].

    Returns:
        Gini impurity in [0, 0.5].

    Raises:
        TypeError: If p is not numeric.
        ValueError: If p not in [0, 1].

    Example:
        >>> gini_impurity_binary(0.5)
        0.5

    Complexity: O(1)
    """
    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")

    if p < 0 or p > 1:
        raise ValueError("p must be in [0, 1].")

    return float(2 * p * (1 - p))


def cohens_kappa_scalar(
    tp: Union[int, float],
    tn: Union[int, float],
    fp: Union[int, float],
    fn: Union[int, float],
) -> float:
    """Calculate Cohen's kappa from a 2×2 confusion matrix.

    κ = (p_o - p_e) / (1 - p_e)

    Args:
        tp: True positives.
        tn: True negatives.
        fp: False positives.
        fn: False negatives.

    Returns:
        Cohen's kappa coefficient.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If total is zero or p_e is 1.

    Example:
        >>> round(cohens_kappa_scalar(50, 40, 10, 5), 6)
        0.714286

    Complexity: O(1)
    """
    if not isinstance(tp, (int, float)) or not isinstance(tn, (int, float)) or not isinstance(fp, (int, float)) or not isinstance(fn, (int, float)):
        raise TypeError("tp, tn, fp, fn must be numeric.")

    total = tp + tn + fp + fn

    if total == 0:
        raise ValueError("Total count must be positive.")

    p_o = (tp + tn) / total
    p_yes = ((tp + fn) / total) * ((tp + fp) / total)
    p_no = ((fp + tn) / total) * ((fn + tn) / total)
    p_e = p_yes + p_no

    if p_e == 1:
        raise ValueError("Expected agreement is 1; kappa is undefined.")

    return float((p_o - p_e) / (1 - p_e))


def binomial_probability(
    n: int,
    k: int,
    p: Union[int, float],
) -> float:
    """Calculate binomial probability P(X=k) = C(n,k)·p^k·(1-p)^(n-k).

    Args:
        n: Number of trials.
        k: Number of successes.
        p: Probability of success per trial, in [0, 1].

    Returns:
        Probability of exactly k successes.

    Raises:
        TypeError: If n or k not int, or p not numeric.
        ValueError: If n < 0, k < 0, k > n, or p not in [0, 1].

    Example:
        >>> round(binomial_probability(10, 3, 0.5), 6)
        0.117188

    Complexity: O(k)
    """
    import math

    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers.")

    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")

    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative.")

    if k > n:
        raise ValueError("k must not exceed n.")

    if p < 0 or p > 1:
        raise ValueError("p must be in [0, 1].")

    return float(math.comb(n, k) * p ** k * (1 - p) ** (n - k))


def logistic_function(
    x: Union[int, float],
    L: Union[int, float] = 1.0,
    k: Union[int, float] = 1.0,
    x0: Union[int, float] = 0.0,
) -> float:
    """Calculate the generalised logistic (sigmoid) function.

    f(x) = L / (1 + e^(-k·(x - x₀)))

    Args:
        x: Input value.
        L: Supremum of output (default 1).
        k: Steepness (default 1).
        x0: Midpoint (default 0).

    Returns:
        Logistic value.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> logistic_function(0)
        0.5

    Complexity: O(1)
    """
    import math

    if not all(isinstance(v, (int, float)) for v in (x, L, k, x0)):
        raise TypeError("All inputs must be numeric.")

    return float(L / (1 + math.exp(-k * (x - x0))))


def cross_entropy_binary(
    y_true: Union[int, float],
    y_pred: Union[int, float],
) -> float:
    """Calculate binary cross-entropy loss for a single observation.

    H = -(y·log(p) + (1-y)·log(1-p))

    Args:
        y_true: Actual label (0 or 1).
        y_pred: Predicted probability, in (0, 1).

    Returns:
        Cross-entropy loss.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If y_true not in {0, 1} or y_pred not in (0, 1).

    Example:
        >>> round(cross_entropy_binary(1, 0.9), 6)
        0.105361

    Complexity: O(1)
    """
    import math

    if not isinstance(y_true, (int, float)) or not isinstance(y_pred, (int, float)):
        raise TypeError("y_true and y_pred must be numeric.")

    if y_true not in (0, 1):
        raise ValueError("y_true must be 0 or 1.")

    if y_pred <= 0 or y_pred >= 1:
        raise ValueError("y_pred must be in (0, 1).")

    return float(-(y_true * math.log(y_pred) + (1 - y_true) * math.log(1 - y_pred)))


def rayleigh_pdf(
    x: Union[int, float],
    sigma: Union[int, float] = 1.0,
) -> float:
    """Return the Rayleigh probability density at *x*.

    PDF = (x / σ²) · exp(-x² / (2σ²))  for x ≥ 0.

    Args:
        x: Point at which to evaluate (must be ≥ 0).
        sigma: Scale parameter (must be > 0).

    Returns:
        Probability density as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If x < 0 or sigma ≤ 0.

    Example:
        >>> round(rayleigh_pdf(1), 6)
        0.606531

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(sigma, (int, float)):
        raise TypeError("sigma must be numeric.")

    if x < 0:
        raise ValueError("x must be non-negative.")

    if sigma <= 0:
        raise ValueError("sigma must be positive.")

    sigma2 = sigma ** 2

    return float((x / sigma2) * math.exp(-x ** 2 / (2 * sigma2)))


def beta_function_value(
    a: Union[int, float],
    b: Union[int, float],
) -> float:
    """Return the value of the Beta function B(a, b).

    B(a, b) = Γ(a) · Γ(b) / Γ(a + b).

    Args:
        a: First parameter (must be > 0).
        b: Second parameter (must be > 0).

    Returns:
        Beta function value as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If a ≤ 0 or b ≤ 0.

    Example:
        >>> round(beta_function_value(2, 3), 6)
        0.083333

    Complexity: O(1)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be numeric.")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be numeric.")

    if a <= 0:
        raise ValueError("a must be positive.")

    if b <= 0:
        raise ValueError("b must be positive.")

    return float(math.gamma(a) * math.gamma(b) / math.gamma(a + b))


def geometric_pdf(
    k: int,
    p: Union[int, float],
) -> float:
    """Return the geometric probability mass at trial *k*.

    P(X = k) = (1 − p)^(k−1) · p,  where k ≥ 1.
    This counts the number of trials until the first success.

    Args:
        k: Trial number (must be ≥ 1).
        p: Success probability per trial (0 < p ≤ 1).

    Returns:
        Probability mass as a float.

    Raises:
        TypeError: If k is not an integer or p not numeric.
        ValueError: If k < 1 or p is out of (0, 1].

    Example:
        >>> geometric_pdf(3, 0.5)
        0.125

    Complexity: O(1)
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")

    if k < 1:
        raise ValueError("k must be at least 1.")

    if not 0 < p <= 1:
        raise ValueError("p must be in (0, 1].")

    return float((1 - p) ** (k - 1) * p)


def gumbel_pdf(
    x: Union[int, float],
    mu: Union[int, float] = 0.0,
    beta: Union[int, float] = 1.0,
) -> float:
    """Return the Gumbel (Type I extreme value) density at *x*.

    PDF = (1/β) · exp(−z − exp(−z)),  where z = (x − μ) / β.

    Args:
        x: Point at which to evaluate.
        mu: Location parameter.
        beta: Scale parameter (must be > 0).

    Returns:
        Probability density as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If beta ≤ 0.

    Example:
        >>> round(gumbel_pdf(0), 6)
        0.367879

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(mu, (int, float)):
        raise TypeError("mu must be numeric.")

    if not isinstance(beta, (int, float)):
        raise TypeError("beta must be numeric.")

    if beta <= 0:
        raise ValueError("beta must be positive.")

    z = (x - mu) / beta

    return float((1 / beta) * math.exp(-z - math.exp(-z)))


def zipf_pmf(
    k: int,
    s: Union[int, float],
    n: int,
) -> float:
    """Return the Zipf probability mass for rank *k*.

    P(X = k) = (1 / k^s) / H(n, s),  where H is the
    generalised harmonic number.

    Args:
        k: Rank (1 ≤ k ≤ n).
        s: Exponent parameter (must be > 0).
        n: Number of elements (must be ≥ 1).

    Returns:
        Probability mass as a float.

    Raises:
        TypeError: If k or n is not int, or s not numeric.
        ValueError: If k < 1, k > n, s ≤ 0, or n < 1.

    Example:
        >>> round(zipf_pmf(1, 1, 10), 6)
        0.341417

    Complexity: O(n)
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if not isinstance(s, (int, float)):
        raise TypeError("s must be numeric.")

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be at least 1.")

    if s <= 0:
        raise ValueError("s must be positive.")

    if not 1 <= k <= n:
        raise ValueError("k must be between 1 and n inclusive.")

    harmonic = sum(1 / i ** s for i in range(1, n + 1))

    return float((1 / k ** s) / harmonic)


def erlang_pdf(
    x: Union[int, float],
    k: int,
    lam: Union[int, float],
) -> float:
    """Return the Erlang probability density at *x*.

    PDF = λ^k · x^(k−1) · exp(−λx) / (k−1)!  for x ≥ 0.

    Args:
        x: Point at which to evaluate (must be ≥ 0).
        k: Shape parameter (positive integer).
        lam: Rate parameter (must be > 0).

    Returns:
        Probability density as a float.

    Raises:
        TypeError: If x or lam not numeric, or k not int.
        ValueError: If x < 0, k < 1, or lam ≤ 0.

    Example:
        >>> round(erlang_pdf(1, 2, 1), 6)
        0.367879

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if not isinstance(lam, (int, float)):
        raise TypeError("lam must be numeric.")

    if x < 0:
        raise ValueError("x must be non-negative.")

    if k < 1:
        raise ValueError("k must be at least 1.")

    if lam <= 0:
        raise ValueError("lam must be positive.")

    if x == 0:
        return float(lam) if k == 1 else 0.0

    return float(
        lam ** k * x ** (k - 1) * math.exp(-lam * x)
        / math.factorial(k - 1)
    )


def maxwell_boltzmann_pdf(
    v: Union[int, float],
    a: Union[int, float],
) -> float:
    """Return the Maxwell-Boltzmann speed distribution density.

    PDF = √(2/π) · v² · exp(−v² / (2a²)) / a³,  where
    a = √(kT / m).

    Args:
        v: Speed (must be ≥ 0).
        a: Scale parameter a = √(kT/m) (must be > 0).

    Returns:
        Probability density as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If v < 0 or a ≤ 0.

    Example:
        >>> round(maxwell_boltzmann_pdf(1, 1), 6)
        0.483941

    Complexity: O(1)
    """
    if not isinstance(v, (int, float)):
        raise TypeError("v must be numeric.")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be numeric.")

    if v < 0:
        raise ValueError("v must be non-negative.")

    if a <= 0:
        raise ValueError("a must be positive.")

    if v == 0:
        return 0.0

    return float(
        math.sqrt(2 / math.pi) * v ** 2 * math.exp(-v ** 2 / (2 * a ** 2))
        / a ** 3
    )


# ---------------------------------------------------------------------------
# Advanced statistics — Bootstrap, empirical CDF, hypothesis tests, etc.
# ---------------------------------------------------------------------------


def bootstrap_mean_ci(
    data: List[float],
    confidence: float = 0.95,
    n_resamples: int = 1000,
    seed: Optional[int] = None,
) -> Tuple[float, float]:
    """Estimates a confidence interval for the mean via bootstrap resampling.

    Draws *n_resamples* samples with replacement, computes their means,
    and returns the percentile-based interval.

    Args:
        data: Numeric data list.
        confidence: Confidence level (0 < confidence < 1).
        n_resamples: Number of bootstrap resamples.
        seed: Optional random seed for reproducibility.

    Returns:
        Tuple (lower_bound, upper_bound) of the confidence interval.

    Raises:
        TypeError: If data is not a list.
        ValueError: If data is empty or confidence is not in (0, 1).

    Example:
        >>> lo, hi = bootstrap_mean_ci([1, 2, 3, 4, 5], 0.95, 5000, seed=42)
        >>> lo < 3.0 < hi
        True

    Complexity: O(n × n_resamples)
    """
    _validate_numeric_list(data)

    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1 (exclusive)")

    rng = _random_mod.Random(seed)
    n = len(data)
    means: list[float] = []

    for _ in range(n_resamples):
        sample = [rng.choice(data) for _ in range(n)]
        means.append(sum(sample) / n)

    means.sort()
    alpha = 1 - confidence
    lo_idx = int((alpha / 2) * n_resamples)
    hi_idx = int((1 - alpha / 2) * n_resamples) - 1
    return (means[lo_idx], means[hi_idx])


def empirical_cdf(data: List[float], x: float) -> float:
    """Computes the empirical cumulative distribution function at x.

    ECDF(x) = (number of observations ≤ x) / n.

    Args:
        data: Numeric data list.
        x: The point at which to evaluate the ECDF.

    Returns:
        Proportion of data values ≤ x (between 0.0 and 1.0).

    Raises:
        TypeError: If data is not a list or x is not numeric.

    Example:
        >>> empirical_cdf([1, 2, 3, 4, 5], 3)
        0.6

    Complexity: O(n)
    """
    _validate_numeric_list(data)

    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")

    count = sum(1 for v in data if v <= x)
    return count / len(data)


def jarque_bera(data: List[float]) -> Tuple[float, bool]:
    """Performs the Jarque-Bera test for normality.

    JB = (n/6) × (S² + K²/4) where S = skewness, K = excess kurtosis.
    Under normality, JB is asymptotically χ²(2). The null hypothesis
    of normality is rejected when JB > 5.99 (α=0.05).

    Args:
        data: Numeric data list (n ≥ 3).

    Returns:
        Tuple of (JB statistic, is_normal) where is_normal is True
        if the null hypothesis of normality is NOT rejected at α=0.05.

    Raises:
        TypeError: If data is not a list.
        ValueError: If data has fewer than 3 elements.

    Example:
        >>> jb, normal = jarque_bera([1, 2, 3, 4, 5])
        >>> normal
        True

    Complexity: O(n)
    """
    _validate_numeric_list(data, min_length=3)

    n = len(data)
    mean = sum(data) / n
    m2 = sum((x - mean) ** 2 for x in data) / n
    m3 = sum((x - mean) ** 3 for x in data) / n
    m4 = sum((x - mean) ** 4 for x in data) / n

    if m2 == 0:
        return (0.0, True)

    s = m3 / (m2 ** 1.5)  # skewness
    k = m4 / (m2 ** 2) - 3  # excess kurtosis
    jb = (n / 6) * (s ** 2 + k ** 2 / 4)
    return (float(jb), jb <= 5.991)


def durbin_watson(residuals: List[float]) -> float:
    """Computes the Durbin-Watson statistic for autocorrelation in residuals.

    DW ≈ 2 means no autocorrelation, DW < 2 positive, DW > 2 negative.

    Args:
        residuals: List of regression residuals.

    Returns:
        Durbin-Watson statistic (0 to 4).

    Raises:
        TypeError: If residuals is not a list.
        ValueError: If residuals has fewer than 2 elements.

    Example:
        >>> round(durbin_watson([0.1, -0.2, 0.15, -0.1, 0.05]), 4)
        2.5824

    Complexity: O(n)
    """
    _validate_numeric_list(residuals, min_length=2)

    n = len(residuals)
    num = sum((residuals[i] - residuals[i - 1]) ** 2 for i in range(1, n))
    den = sum(r ** 2 for r in residuals)

    if den == 0:
        return 0.0

    return float(num / den)


def mann_whitney_u(data1: List[float], data2: List[float]) -> Tuple[float, float]:
    """Performs the Mann-Whitney U test (standalone, no scipy).

    Non-parametric test for whether two independent samples come from
    the same distribution. Returns U statistic and approximate z-score.

    Args:
        data1: First sample.
        data2: Second sample.

    Returns:
        Tuple of (U statistic, z_score).

    Raises:
        TypeError: If inputs are not lists.
        ValueError: If either sample is empty.

    Example:
        >>> u, z = mann_whitney_u([1, 2, 3], [4, 5, 6])
        >>> u
        0.0

    Complexity: O(n₁ × n₂)
    """
    _validate_numeric_list(data1)
    _validate_numeric_list(data2)

    n1, n2 = len(data1), len(data2)
    u1 = 0.0

    for x in data1:

        for y in data2:

            if x < y:
                u1 += 1
            elif x == y:
                u1 += 0.5

    u2 = n1 * n2 - u1
    u_stat = min(u1, u2)

    # Normal approximation
    mu_u = n1 * n2 / 2
    sigma_u = math.sqrt(n1 * n2 * (n1 + n2 + 1) / 12)

    if sigma_u == 0:
        return (float(u_stat), 0.0)

    z = (u_stat - mu_u) / sigma_u
    return (float(u_stat), float(z))


def runs_test_statistic(binary_sequence: List[int]) -> Tuple[int, float]:
    """Performs the Wald-Wolfowitz runs test for randomness.

    Counts the number of runs (consecutive identical values) in a
    binary sequence and computes the z-score.

    Args:
        binary_sequence: List of 0s and 1s.

    Returns:
        Tuple of (number_of_runs, z_score).

    Raises:
        TypeError: If input is not a list.
        ValueError: If sequence is empty or contains non-binary values.

    Example:
        >>> runs, z = runs_test_statistic([1, 1, 0, 0, 1, 0, 1])
        >>> runs
        5

    Complexity: O(n)
    """
    if not isinstance(binary_sequence, list):
        raise TypeError("binary_sequence must be a list")

    if not binary_sequence:
        raise ValueError("binary_sequence must not be empty")

    if not all(v in (0, 1) for v in binary_sequence):
        raise ValueError("binary_sequence must contain only 0s and 1s")

    n = len(binary_sequence)
    n1 = sum(binary_sequence)
    n0 = n - n1

    if n0 == 0 or n1 == 0:
        return (1, 0.0)

    runs = 1

    for i in range(1, n):

        if binary_sequence[i] != binary_sequence[i - 1]:
            runs += 1

    mu = 1 + 2 * n0 * n1 / n
    sigma_sq = (2 * n0 * n1 * (2 * n0 * n1 - n)) / (n ** 2 * (n - 1))

    if sigma_sq <= 0:
        return (runs, 0.0)

    z = (runs - mu) / math.sqrt(sigma_sq)
    return (runs, float(z))


def theil_sen_slope(x_data: List[float], y_data: List[float]) -> float:
    """Computes the Theil-Sen slope estimator (median of all pairwise slopes).

    Robust to outliers — unlike ordinary least squares, up to ~29% of
    data can be outliers without affecting the result.

    Args:
        x_data: Independent variable values.
        y_data: Dependent variable values (same length as x_data).

    Returns:
        Median slope.

    Raises:
        TypeError: If inputs are not lists.
        ValueError: If lists have different lengths or fewer than 2 points.

    Example:
        >>> theil_sen_slope([1, 2, 3, 4], [2, 4, 6, 8])
        2.0

    Complexity: O(n²)
    """
    _validate_numeric_list(x_data, min_length=2)
    _validate_numeric_list(y_data, min_length=2)

    if len(x_data) != len(y_data):
        raise ValueError("x_data and y_data must have the same length")

    n = len(x_data)
    slopes: list[float] = []

    for i in range(n):

        for j in range(i + 1, n):

            if x_data[j] != x_data[i]:
                slopes.append((y_data[j] - y_data[i]) / (x_data[j] - x_data[i]))

    if not slopes:
        return 0.0

    slopes.sort()
    mid = len(slopes) // 2

    if len(slopes) % 2 == 0:
        return float((slopes[mid - 1] + slopes[mid]) / 2)

    return float(slopes[mid])


def exponential_smoothing_single(
    value: float, previous_smoothed: float, alpha: float
) -> float:
    """Computes one step of single exponential smoothing.

    S_t = α × X_t + (1 − α) × S_{t−1}

    Args:
        value: Current observation X_t.
        previous_smoothed: Previous smoothed value S_{t−1}.
        alpha: Smoothing factor (0 < alpha ≤ 1).

    Returns:
        New smoothed value S_t.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If alpha is not in (0, 1].

    Example:
        >>> exponential_smoothing_single(10, 8, 0.3)
        8.6

    Complexity: O(1)
    """
    for name, val in (("value", value), ("previous_smoothed", previous_smoothed), ("alpha", alpha)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if not 0 < alpha <= 1:
        raise ValueError("alpha must be in (0, 1]")

    return float(alpha * value + (1 - alpha) * previous_smoothed)


def anderson_darling(data: list[float | int]) -> float:
    """Compute the Anderson-Darling normality test statistic (standalone).

    Tests whether a sample comes from a normal distribution.
    Higher values indicate stronger evidence against normality.

    Args:
        data: List of numeric observations (n ≥ 8 recommended).

    Returns:
        Anderson-Darling A² statistic.

    Raises:
        TypeError: If *data* is not a list of numbers.
        ValueError: If *data* has fewer than 2 elements or zero variance.

    Example:
        >>> round(anderson_darling([1, 2, 3, 4, 5, 6, 7, 8]), 4)
        0.2253

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    n = len(data)

    if n < 2:
        raise ValueError("data must have at least 2 elements")

    for v in data:

        if not isinstance(v, (int, float)):
            raise TypeError("All elements must be numeric")

    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data) / (n - 1)

    if var == 0:
        raise ValueError("data has zero variance")

    sd = math.sqrt(var)
    sorted_data = sorted(data)

    # Standard normal CDF via error function
    def _phi(x: float) -> float:
        return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

    s = 0.0

    for i in range(n):
        z = (sorted_data[i] - mean) / sd
        cdf_z = _phi(z)
        cdf_z = max(1e-15, min(1 - 1e-15, cdf_z))
        z_rev = (sorted_data[n - 1 - i] - mean) / sd
        cdf_rev = _phi(z_rev)
        cdf_rev = max(1e-15, min(1 - 1e-15, cdf_rev))
        s += (2 * (i + 1) - 1) * (math.log(cdf_z) + math.log(1 - cdf_rev))

    a2 = -n - s / n
    # Stephens' correction for finite sample
    a2_star = a2 * (1 + 0.75 / n + 2.25 / (n * n))
    return float(round(a2_star, 4))


def grubbs_test(data: list[float | int]) -> dict:
    """Perform Grubbs' test for a single outlier.

    Tests whether the maximum or minimum value is an outlier.

    Args:
        data: List of numeric observations (n ≥ 3).

    Returns:
        Dict with keys: ``"outlier_value"``, ``"g_statistic"``,
        ``"position"`` (``"max"`` or ``"min"``).

    Raises:
        TypeError: If *data* is not a list of numbers.
        ValueError: If *data* has fewer than 3 elements or zero variance.

    Example:
        >>> result = grubbs_test([1, 2, 3, 4, 5, 100])
        >>> result["position"]
        'max'

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    n = len(data)

    if n < 3:
        raise ValueError("data must have at least 3 elements")

    for v in data:

        if not isinstance(v, (int, float)):
            raise TypeError("All elements must be numeric")

    mean = sum(data) / n
    sd = math.sqrt(sum((x - mean) ** 2 for x in data) / (n - 1))

    if sd == 0:
        raise ValueError("data has zero variance")

    min_val = min(data)
    max_val = max(data)
    g_min = (mean - min_val) / sd
    g_max = (max_val - mean) / sd

    if g_max >= g_min:
        return {"outlier_value": max_val, "g_statistic": round(g_max, 4), "position": "max"}

    return {"outlier_value": min_val, "g_statistic": round(g_min, 4), "position": "min"}


def dixon_q_test(data: list[float | int]) -> dict:
    """Perform Dixon's Q test for outlier detection.

    Tests the smallest or largest value. Applicable for small samples
    (3 ≤ n ≤ 25).

    Args:
        data: List of numeric observations.

    Returns:
        Dict with: ``"q_statistic"``, ``"suspect_value"``,
        ``"position"`` (``"min"`` or ``"max"``).

    Raises:
        TypeError: If *data* is not a list of numbers.
        ValueError: If *data* has fewer than 3 elements.

    Example:
        >>> result = dixon_q_test([1, 2, 3, 4, 5, 100])
        >>> result["position"]
        'max'

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if len(data) < 3:
        raise ValueError("data must have at least 3 elements")

    for v in data:

        if not isinstance(v, (int, float)):
            raise TypeError("All elements must be numeric")

    sorted_data = sorted(data)
    range_val = sorted_data[-1] - sorted_data[0]

    if range_val == 0:
        return {"q_statistic": 0.0, "suspect_value": sorted_data[0], "position": "min"}

    q_min = (sorted_data[1] - sorted_data[0]) / range_val
    q_max = (sorted_data[-1] - sorted_data[-2]) / range_val

    if q_max >= q_min:
        return {"q_statistic": round(q_max, 4), "suspect_value": sorted_data[-1], "position": "max"}

    return {"q_statistic": round(q_min, 4), "suspect_value": sorted_data[0], "position": "min"}


def ewma_variance(data: list[float | int], alpha: float = 0.3) -> list[float]:
    """Compute exponentially weighted moving variance.

    Args:
        data: List of numeric observations.
        alpha: Smoothing factor in (0, 1).

    Returns:
        List of EWMA variance values (same length as *data*).

    Raises:
        TypeError: If *data* is not a list of numbers.
        ValueError: If *alpha* is not in (0, 1) or *data* is empty.

    Example:
        >>> ewma_variance([1, 2, 3, 4, 5], 0.3)[:2]
        [0.0, 0.21]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not data:
        raise ValueError("data must not be empty")

    if not isinstance(alpha, (int, float)) or alpha <= 0 or alpha >= 1:
        raise ValueError("alpha must be in (0, 1)")

    for v in data:

        if not isinstance(v, (int, float)):
            raise TypeError("All elements must be numeric")

    ewma_mean = float(data[0])
    ewma_var = 0.0
    result = [0.0]

    for i in range(1, len(data)):
        diff = data[i] - ewma_mean
        ewma_mean = alpha * data[i] + (1 - alpha) * ewma_mean
        ewma_var = (1 - alpha) * (ewma_var + alpha * diff * diff)
        result.append(round(ewma_var, 4))

    return result


def shapiro_wilk_w(data: list[float | int]) -> float:
    """Compute the Shapiro-Wilk W statistic for normality testing.

    Uses the simplified approximation with order-statistic expectations
    for small to moderate samples (n ≤ 5000).

    Args:
        data: Numeric observations (at least 3 values).

    Returns:
        The W statistic in (0, 1].

    Raises:
        TypeError: If *data* is not a list of numbers.
        ValueError: If *data* has fewer than 3 elements.

    Example:
        >>> round(shapiro_wilk_w([1, 2, 3, 4, 5]), 4)
        0.9867

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if len(data) < 3:
        raise ValueError("data must have at least 3 elements")

    for v in data:

        if not isinstance(v, (int, float)):
            raise TypeError("All elements must be numeric")

    import math

    n = len(data)
    x = sorted(data)
    mean = sum(x) / n

    # Expected normal order statistics approximation (Blom's formula)
    a: list[float] = []

    for i in range(n):
        p = (i + 1 - 0.375) / (n + 0.25)
        # Rational approximation of the inverse normal CDF
        t = math.sqrt(-2.0 * math.log(min(p, 1 - p)))
        sign = 1.0 if p >= 0.5 else -1.0
        c0, c1, c2 = 2.515517, 0.802853, 0.010328
        d1, d2, d3 = 1.432788, 0.189269, 0.001308
        val = t - (c0 + c1 * t + c2 * t ** 2) / (1 + d1 * t + d2 * t ** 2 + d3 * t ** 3)
        a.append(sign * val)

    a_sq_sum = sum(ai ** 2 for ai in a)

    if a_sq_sum == 0:
        return 1.0

    a = [ai / math.sqrt(a_sq_sum) for ai in a]

    numerator = sum(a[i] * x[i] for i in range(n)) ** 2
    denominator = sum((xi - mean) ** 2 for xi in x)

    if denominator == 0:
        return 1.0

    return float(round(numerator / denominator, 4))


def ljung_box(residuals: list[float | int], lags: int = 10) -> float:
    """Compute the Ljung-Box Q statistic for autocorrelation testing.

    Q = n(n+2) Σ_{k=1}^{h} r_k² / (n-k)

    Args:
        residuals: Time-series residuals.
        lags: Number of lags to test.

    Returns:
        The Q statistic.

    Raises:
        TypeError: If *residuals* is not a list of numbers.
        ValueError: If *residuals* has fewer elements than *lags* + 1.

    Example:
        >>> round(ljung_box([1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1], 5), 2)
        72.0

    Complexity: O(n × h)
    """
    if not isinstance(residuals, list):
        raise TypeError("residuals must be a list")

    if not isinstance(lags, int) or lags < 1:
        raise ValueError("lags must be a positive integer")

    n = len(residuals)

    if n <= lags:
        raise ValueError("residuals length must be greater than lags")

    for v in residuals:

        if not isinstance(v, (int, float)):
            raise TypeError("All elements must be numeric")

    mean = sum(residuals) / n
    var = sum((r - mean) ** 2 for r in residuals)

    if var == 0:
        return 0.0

    q = 0.0

    for k in range(1, lags + 1):
        rk = sum((residuals[t] - mean) * (residuals[t - k] - mean) for t in range(k, n))
        rho_k = rk / var
        q += rho_k ** 2 / (n - k)

    return float(round(n * (n + 2) * q, 4))


def markov_chain_steady_state(
    transition: list[list[float]],
    tol: float = 1e-10,
    max_iter: int = 1000,
) -> list[float]:
    """Compute the steady-state distribution of an ergodic Markov chain.

    Uses the power method: repeatedly multiplies a uniform distribution
    vector by the transition matrix until convergence.

    Args:
        transition: Square row-stochastic transition matrix.
        tol: Convergence tolerance.
        max_iter: Maximum iterations.

    Returns:
        Stationary distribution as a list.

    Raises:
        TypeError: If *transition* is not a list of lists.
        ValueError: If matrix is empty or not square.

    Example:
        >>> pi = markov_chain_steady_state([[0.9, 0.1], [0.5, 0.5]])
        >>> [round(p, 4) for p in pi]
        [0.8333, 0.1667]

    Complexity: O(n² × iterations)
    """
    if not isinstance(transition, list):
        raise TypeError("transition must be a list of lists")

    n = len(transition)

    if n == 0:
        raise ValueError("transition matrix must not be empty")

    for row in transition:

        if not isinstance(row, list) or len(row) != n:
            raise ValueError("transition must be a square matrix")

    # Start with uniform distribution
    pi = [1.0 / n] * n

    for _ in range(max_iter):
        new_pi = [0.0] * n

        for j in range(n):

            for i in range(n):
                new_pi[j] += pi[i] * transition[i][j]

        # Check convergence
        diff = sum(abs(new_pi[i] - pi[i]) for i in range(n))

        if diff < tol:
            return [round(p, 10) for p in new_pi]

        pi = new_pi

    return [round(p, 10) for p in pi]


def benford_distribution(data: list[float | int]) -> dict[int, float]:
    """Compute the leading-digit frequency distribution for Benford's law analysis.

    Returns observed frequencies for digits 1-9.

    Args:
        data: Positive numeric values.

    Returns:
        Dict mapping digit (1-9) to observed frequency.

    Raises:
        TypeError: If *data* is not a list of numbers.
        ValueError: If *data* is empty.

    Example:
        >>> d = benford_distribution([1, 20, 300, 4000])
        >>> d[1]
        0.25

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list")

    if not data:
        raise ValueError("data must not be empty")

    counts: dict[int, int] = {d: 0 for d in range(1, 10)}
    total = 0

    for v in data:

        if not isinstance(v, (int, float)):
            raise TypeError("All elements must be numeric")

        s = str(abs(v)).lstrip("0").lstrip(".")

        if s and s[0].isdigit() and s[0] != "0":
            counts[int(s[0])] += 1
            total += 1

    if total == 0:
        return {d: 0.0 for d in range(1, 10)}

    return {d: round(c / total, 4) for d, c in counts.items()}


def percentile_to_z_score(p: float) -> float:
    """Convert a percentile (cumulative probability) to a z-score.

    Uses the rational approximation by Abramowitz & Stegun (probit).

    Args:
        p: Percentile in (0, 1).

    Returns:
        Corresponding z-score.

    Raises:
        TypeError: If *p* is not numeric.
        ValueError: If *p* is outside (0, 1).

    Example:
        >>> round(percentile_to_z_score(0.975), 2)
        1.96

    Complexity: O(1)
    """
    import math

    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric")

    if p <= 0 or p >= 1:
        raise ValueError("p must be in (0, 1)")

    # Beasley-Springer-Moro approximation
    if p < 0.5:
        t = math.sqrt(-2.0 * math.log(p))
    else:
        t = math.sqrt(-2.0 * math.log(1.0 - p))

    c0, c1, c2 = 2.515517, 0.802853, 0.010328
    d1, d2, d3 = 1.432788, 0.189269, 0.001308

    z = t - (c0 + c1 * t + c2 * t ** 2) / (1.0 + d1 * t + d2 * t ** 2 + d3 * t ** 3)

    if p < 0.5:
        return float(-z)

    return float(z)


def bayes_posterior(
    prior: float,
    likelihood: float,
    evidence: float,
) -> float:
    """Compute the Bayesian posterior probability.

    P(H|E) = P(E|H) × P(H) / P(E)

    Args:
        prior: Prior probability P(H).
        likelihood: Likelihood P(E|H).
        evidence: Marginal probability P(E).

    Returns:
        Posterior probability.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If *evidence* is zero or probabilities out of [0, 1].

    Example:
        >>> bayes_posterior(0.01, 0.9, 0.05)
        0.18

    Complexity: O(1)
    """
    for name, val in (("prior", prior), ("likelihood", likelihood), ("evidence", evidence)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if evidence == 0:
        raise ValueError("evidence must not be zero")

    for name, val in (("prior", prior), ("likelihood", likelihood)):

        if val < 0 or val > 1:
            raise ValueError(f"{name} must be in [0, 1]")

    return float(round(likelihood * prior / evidence, 10))


def sigmoid(x: Union[int, float]) -> float:
    """Compute the logistic sigmoid function σ(x) = 1 / (1 + e⁻ˣ).

    Args:
        x: Input value.

    Returns:
        Sigmoid value in (0, 1).

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> sigmoid(0)
        0.5

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    # Numerically stable formulation
    if x >= 0:
        z = math.exp(-x)
        return float(1.0 / (1.0 + z))

    z = math.exp(x)

    return float(z / (1.0 + z))


def logit(p: Union[int, float]) -> float:
    """Compute the logit (log-odds) function, inverse of sigmoid.

    logit(p) = log(p / (1 - p))

    Args:
        p: Probability in (0, 1) exclusive.

    Returns:
        Log-odds value.

    Raises:
        TypeError: If p is not numeric.
        ValueError: If p is not in (0, 1).

    Example:
        >>> logit(0.5)
        0.0

    Complexity: O(1)
    """
    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")

    if p <= 0 or p >= 1:
        raise ValueError("p must be in (0, 1) exclusive.")

    return float(math.log(p / (1.0 - p)))


def softplus(x: Union[int, float]) -> float:
    """Compute the softplus activation: softplus(x) = log(1 + eˣ).

    Numerically stable for large positive x.

    Args:
        x: Input value.

    Returns:
        Softplus value (always positive).

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> round(softplus(0), 4)
        0.6931

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    # Avoid overflow for large x: softplus(x) ≈ x
    if x > 20:
        return float(x)

    return float(math.log1p(math.exp(x)))


def coefficient_of_quartile_deviation(data: list) -> float:
    """Calculate the Coefficient of Quartile Deviation (CQD).

    Description:
        CQD = (Q3 − Q1) / (Q3 + Q1).
        A dimensionless relative dispersion measure based on quartiles.

    Args:
        data: A list of numeric values (at least 2 elements).

    Returns:
        CQD value.

    Raises:
        TypeError: If *data* is not a list or contains non-numeric values.
        ValueError: If *data* has fewer than 2 elements or Q3 + Q1 == 0.

    Usage Example:
        >>> coefficient_of_quartile_deviation([2, 4, 6, 8, 10])
        0.5

    Complexity: O(n log n)
    """
    _validate_numeric_list(data, min_length=2)
    sorted_d = sorted(data)

    def _percentile(arr: list, p: float) -> float:
        k = (len(arr) - 1) * p
        f = math.floor(k)
        c = math.ceil(k)

        if f == c:
            return float(arr[f])

        return float(arr[f] * (c - k) + arr[c] * (k - f))

    q1 = _percentile(sorted_d, 0.25)
    q3 = _percentile(sorted_d, 0.75)

    denom = q3 + q1

    if denom == 0:
        raise ValueError("Q3 + Q1 equals zero; CQD is undefined.")

    return float((q3 - q1) / denom)


def tukey_trimean(data: list) -> float:
    """Calculate Tukey's trimean.

    Description:
        Trimean = (Q1 + 2·Q2 + Q3) / 4.
        A robust measure of central tendency that weights the median
        double, dampening the influence of outliers.

    Args:
        data: A list of numeric values (at least 3 elements).

    Returns:
        The trimean as a float.

    Raises:
        TypeError: If *data* is not a list or contains non-numeric values.
        ValueError: If *data* has fewer than 3 elements.

    Usage Example:
        >>> tukey_trimean([1, 2, 3, 4, 5])
        3.0

    Complexity: O(n log n)
    """
    _validate_numeric_list(data, min_length=3)
    sorted_d = sorted(data)

    def _percentile(arr: list, p: float) -> float:
        k = (len(arr) - 1) * p
        f = math.floor(k)
        c = math.ceil(k)

        if f == c:
            return float(arr[f])

        return float(arr[f] * (c - k) + arr[c] * (k - f))

    q1 = _percentile(sorted_d, 0.25)
    q2 = _percentile(sorted_d, 0.50)
    q3 = _percentile(sorted_d, 0.75)

    return float((q1 + 2 * q2 + q3) / 4)


def midrange(data: list) -> float:
    """Calculate the midrange of a dataset.

    Description:
        Midrange = (max + min) / 2.
        The arithmetic mean of the extreme values.

    Args:
        data: A list of numeric values (at least 1 element).

    Returns:
        The midrange as a float.

    Raises:
        TypeError: If *data* is not a list or contains non-numeric values.
        ValueError: If *data* is empty.

    Usage Example:
        >>> midrange([2, 4, 6, 8, 10])
        6.0

    Complexity: O(n)
    """
    _validate_numeric_list(data, min_length=1)

    return float((min(data) + max(data)) / 2)


def midhinge(data: list) -> float:
    """Calculate the midhinge of a dataset.

    Description:
        Midhinge = (Q1 + Q3) / 2.
        The average of the first and third quartiles.

    Args:
        data: A list of numeric values (at least 2 elements).

    Returns:
        The midhinge as a float.

    Raises:
        TypeError: If *data* is not a list or contains non-numeric values.
        ValueError: If *data* has fewer than 2 elements.

    Usage Example:
        >>> midhinge([1, 2, 3, 4, 5])
        3.0

    Complexity: O(n log n)
    """
    _validate_numeric_list(data, min_length=2)
    sorted_d = sorted(data)

    def _percentile(arr: list, p: float) -> float:
        k = (len(arr) - 1) * p
        f = math.floor(k)
        c = math.ceil(k)

        if f == c:
            return float(arr[f])

        return float(arr[f] * (c - k) + arr[c] * (k - f))

    q1 = _percentile(sorted_d, 0.25)
    q3 = _percentile(sorted_d, 0.75)

    return float((q1 + q3) / 2)


def contraharmonic_mean(data: list) -> float:
    """Calculate the contraharmonic mean.

    Description:
        Contraharmonic Mean = Σx² / Σx.
        Always greater than or equal to the arithmetic mean for
        positive values.  Useful in image processing and statistics.

    Args:
        data: A list of numeric values (at least 1 element, sum ≠ 0).

    Returns:
        The contraharmonic mean as a float.

    Raises:
        TypeError: If *data* is not a list or contains non-numeric values.
        ValueError: If *data* is empty or sum of values is zero.

    Usage Example:
        >>> contraharmonic_mean([1, 2, 3, 4, 5])
        3.6666666666666665

    Complexity: O(n)
    """
    _validate_numeric_list(data, min_length=1)

    s = sum(data)

    if s == 0:
        raise ValueError("Sum of data must not be zero.")

    return float(sum(x ** 2 for x in data) / s)


# ============================================================================
# MACHINE LEARNING ACTIVATION FUNCTIONS
# ============================================================================


def celu(x: float, alpha: float = 1.0) -> float:
    """Continuously Differentiable Exponential Linear Unit (CELU).

    Description:
        CELU(x) = max(0, x) + min(0, α(e^{x/α} − 1)).
        Provides a smooth, continuously differentiable alternative
        to ELU that avoids the non-differentiable point at x = 0.

    Args:
        x: Input value.
        alpha: Scale for the negative region (> 0). Default 1.0.

    Returns:
        CELU activation value.

    Raises:
        TypeError: If *x* or *alpha* is not numeric.
        ValueError: If *alpha* is not positive.

    Usage Example:
        >>> celu(1.0)
        1.0
        >>> round(celu(-1.0, 1.0), 6)
        -0.632121

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(alpha, (int, float)):
        raise TypeError("x and alpha must be numeric.")

    if alpha <= 0:
        raise ValueError("alpha must be positive.")

    return float(max(0.0, x) + min(0.0, alpha * (math.exp(x / alpha) - 1.0)))


def hard_sigmoid(x: float) -> float:
    """Hard sigmoid: piecewise-linear approximation of the sigmoid function.

    Description:
        hard_sigmoid(x) = max(0, min(1, (x + 3) / 6)).
        Computationally cheap alternative used in mobile and edge models.

    Args:
        x: Input value.

    Returns:
        Approximated sigmoid value in [0, 1].

    Raises:
        TypeError: If *x* is not numeric.

    Usage Example:
        >>> hard_sigmoid(0.0)
        0.5
        >>> hard_sigmoid(3.0)
        1.0
        >>> hard_sigmoid(-3.0)
        0.0

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    return float(max(0.0, min(1.0, (x + 3.0) / 6.0)))


def hard_swish(x: float) -> float:
    """Hard swish: efficient approximation of the swish activation.

    Description:
        hard_swish(x) = x × hard_sigmoid(x).
        Used in MobileNetV3 and similar efficient architectures.

    Args:
        x: Input value.

    Returns:
        Hard-swish activation value.

    Raises:
        TypeError: If *x* is not numeric.

    Usage Example:
        >>> hard_swish(0.0)
        0.0
        >>> hard_swish(3.0)
        3.0
        >>> round(hard_swish(-1.0), 6)
        -0.333333

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")

    return float(x * max(0.0, min(1.0, (x + 3.0) / 6.0)))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 4: Robust statistics, order statistics & effect sizes
# ---------------------------------------------------------------------------

def winsorized_mean(
    data: list[float],
    proportion: float = 0.05,
) -> float:
    """Winsorized mean: replace extreme values before averaging.

    Replaces the lowest and highest *proportion* of values with the nearest
    non-replaced values, then computes the arithmetic mean.

    Args:
        data: List of numeric values (length ≥ 2).
        proportion: Fraction of values to replace on each tail, in [0, 0.5).

    Returns:
        Winsorized mean as a float.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is too short or proportion is out of range.

    Usage Example:
        >>> winsorized_mean([1, 2, 3, 4, 100], 0.2)
        3.0

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(proportion, (int, float)):
        raise TypeError("proportion must be numeric.")
    if len(data) < 2:
        raise ValueError("data must have at least 2 elements.")
    if proportion < 0 or proportion >= 0.5:
        raise ValueError("proportion must be in [0, 0.5).")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    sorted_data = sorted(data)
    n = len(sorted_data)
    k = int(proportion * n)
    winsorized = sorted_data[:]
    for i in range(k):
        winsorized[i] = sorted_data[k]
    for i in range(n - k, n):
        winsorized[i] = sorted_data[n - k - 1]
    return float(sum(winsorized) / n)


def trimmed_variance(
    data: list[float],
    proportion: float = 0.05,
) -> float:
    """Variance of the trimmed dataset (after removing tails).

    Args:
        data: List of numeric values (length ≥ 3).
        proportion: Fraction of values to trim on each tail, in [0, 0.5).

    Returns:
        Trimmed variance as a float.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is too short, proportion out of range, or trimmed
            set has fewer than 2 elements.

    Usage Example:
        >>> round(trimmed_variance([1, 2, 3, 4, 5, 6, 7, 8, 9, 100], 0.1), 4)
        6.0

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(proportion, (int, float)):
        raise TypeError("proportion must be numeric.")
    if len(data) < 3:
        raise ValueError("data must have at least 3 elements.")
    if proportion < 0 or proportion >= 0.5:
        raise ValueError("proportion must be in [0, 0.5).")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    sorted_data = sorted(data)
    n = len(sorted_data)
    k = int(proportion * n)
    trimmed = sorted_data[k:n - k] if k > 0 else sorted_data[:]
    if len(trimmed) < 2:
        raise ValueError("Trimmed set must have at least 2 elements.")
    mean = sum(trimmed) / len(trimmed)
    return float(sum((x - mean) ** 2 for x in trimmed) / (len(trimmed) - 1))


def median_absolute_deviation(
    data: list[float],
) -> float:
    """Median absolute deviation (MAD) — robust measure of dispersion.

    MAD = median(|x_i − median(x)|).

    Args:
        data: List of numeric values (non-empty).

    Returns:
        MAD as a float.

    Raises:
        TypeError: If data is not a list of numerics.
        ValueError: If data is empty.

    Usage Example:
        >>> median_absolute_deviation([1, 2, 3, 4, 5])
        1.0

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if len(data) == 0:
        raise ValueError("data must not be empty.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    def _median(xs: list[float]) -> float:
        s = sorted(xs)
        n = len(s)
        if n % 2 == 1:
            return float(s[n // 2])
        return float((s[n // 2 - 1] + s[n // 2]) / 2)

    med = _median(data)
    deviations = [abs(x - med) for x in data]
    return float(_median(deviations))


def coefficient_of_variation(
    data: list[float],
) -> float:
    """Coefficient of variation (CV) — ratio of std dev to mean.

    CV = σ / |μ|.

    Args:
        data: List of numeric values (length ≥ 2, mean ≠ 0).

    Returns:
        CV as a float.

    Raises:
        TypeError: If data is not a list of numerics.
        ValueError: If data has fewer than 2 elements or mean is zero.

    Usage Example:
        >>> round(coefficient_of_variation([2, 4, 4, 4, 5, 5, 7, 9]), 4)
        0.4276

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if len(data) < 2:
        raise ValueError("data must have at least 2 elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    n = len(data)
    mean = sum(data) / n
    if mean == 0:
        raise ValueError("Mean must not be zero.")
    variance = sum((x - mean) ** 2 for x in data) / (n - 1)
    return float(variance ** 0.5 / abs(mean))


def quartile_deviation(
    data: list[float],
) -> float:
    """Quartile deviation (semi-interquartile range): (Q3 − Q1) / 2.

    Args:
        data: List of numeric values (length ≥ 4).

    Returns:
        Quartile deviation as a float.

    Raises:
        TypeError: If data is not a list of numerics.
        ValueError: If data has fewer than 4 elements.

    Usage Example:
        >>> quartile_deviation([1, 2, 3, 4, 5, 6, 7, 8])
        1.75

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if len(data) < 4:
        raise ValueError("data must have at least 4 elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    def _percentile(sorted_data: list[float], p: float) -> float:
        n = len(sorted_data)
        k = (n - 1) * p
        f = int(k)
        c = f + 1 if f + 1 < n else f
        return float(sorted_data[f] + (k - f) * (sorted_data[c] - sorted_data[f]))

    s = sorted(data)
    q1 = _percentile(s, 0.25)
    q3 = _percentile(s, 0.75)
    return float((q3 - q1) / 2)


def bowley_skewness(
    data: list[float],
) -> float:
    """Bowley (quartile) skewness: (Q3 + Q1 − 2·Q2) / (Q3 − Q1).

    A robust alternative to the moment-based skewness.

    Args:
        data: List of numeric values (length ≥ 4, IQR > 0).

    Returns:
        Bowley skewness in [−1, 1].

    Raises:
        TypeError: If data is not a list of numerics.
        ValueError: If data has fewer than 4 elements or IQR is zero.

    Usage Example:
        >>> round(bowley_skewness([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4)
        0.0

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if len(data) < 4:
        raise ValueError("data must have at least 4 elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    def _percentile(sorted_data: list[float], p: float) -> float:
        n = len(sorted_data)
        k = (n - 1) * p
        f = int(k)
        c = f + 1 if f + 1 < n else f
        return float(sorted_data[f] + (k - f) * (sorted_data[c] - sorted_data[f]))

    s = sorted(data)
    q1 = _percentile(s, 0.25)
    q2 = _percentile(s, 0.50)
    q3 = _percentile(s, 0.75)
    iqr = q3 - q1
    if iqr == 0:
        raise ValueError("IQR must not be zero.")
    return float((q3 + q1 - 2 * q2) / iqr)


def moors_kurtosis(
    data: list[float],
) -> float:
    """Moors' octile-based kurtosis measure (robust alternative).

    K_M = [(E7 − E5) + (E3 − E1)] / (E6 − E2) where E_i are octiles.

    Args:
        data: List of numeric values (length ≥ 8).

    Returns:
        Moors' kurtosis as a float (normal ≈ 1.23).

    Raises:
        TypeError: If data is not a list of numerics.
        ValueError: If data has fewer than 8 elements.

    Usage Example:
        >>> round(moors_kurtosis(list(range(1, 101))), 2)
        1.0

    Complexity: O(n log n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if len(data) < 8:
        raise ValueError("data must have at least 8 elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    def _percentile(sorted_data: list[float], p: float) -> float:
        n = len(sorted_data)
        k = (n - 1) * p
        f = int(k)
        c = f + 1 if f + 1 < n else f
        return float(sorted_data[f] + (k - f) * (sorted_data[c] - sorted_data[f]))

    s = sorted(data)
    e1 = _percentile(s, 0.125)
    e2 = _percentile(s, 0.25)
    e3 = _percentile(s, 0.375)
    e5 = _percentile(s, 0.625)
    e6 = _percentile(s, 0.75)
    e7 = _percentile(s, 0.875)
    denom = e6 - e2
    if denom == 0:
        raise ValueError("E6 − E2 must not be zero.")
    return float(((e7 - e5) + (e3 - e1)) / denom)


def cohens_d(
    group1: list[float],
    group2: list[float],
) -> float:
    """Cohen's d effect size between two independent groups.

    d = (M1 − M2) / s_pooled where s_pooled uses Bessel-corrected variances.

    Args:
        group1: First sample (length ≥ 2).
        group2: Second sample (length ≥ 2).

    Returns:
        Cohen's d as a float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If either group has fewer than 2 elements or pooled SD is 0.

    Usage Example:
        >>> round(cohens_d([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), 4)
        -1.2649

    Complexity: O(n + m)
    """
    for name, grp in (("group1", group1), ("group2", group2)):
        if not isinstance(grp, list):
            raise TypeError(f"{name} must be a list.")
        if len(grp) < 2:
            raise ValueError(f"{name} must have at least 2 elements.")
        for i, v in enumerate(grp):
            if not isinstance(v, (int, float)):
                raise TypeError(f"{name}[{i}] must be numeric.")

    n1, n2 = len(group1), len(group2)
    m1 = sum(group1) / n1
    m2 = sum(group2) / n2
    var1 = sum((x - m1) ** 2 for x in group1) / (n1 - 1)
    var2 = sum((x - m2) ** 2 for x in group2) / (n2 - 1)
    pooled_var = ((n1 - 1) * var1 + (n2 - 1) * var2) / (n1 + n2 - 2)
    if pooled_var == 0:
        raise ValueError("Pooled standard deviation must not be zero.")
    return float((m1 - m2) / pooled_var ** 0.5)


def hedges_g(
    group1: list[float],
    group2: list[float],
) -> float:
    """Hedges' g — bias-corrected effect size (for small samples).

    g = Cohen's d × (1 − 3 / (4(n1+n2) − 9)).

    Args:
        group1: First sample (length ≥ 2).
        group2: Second sample (length ≥ 2).

    Returns:
        Hedges' g as a float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If either group has fewer than 2 elements.

    Usage Example:
        >>> round(hedges_g([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), 4)
        -1.1425

    Complexity: O(n + m)
    """
    d = cohens_d(group1, group2)
    n = len(group1) + len(group2)
    correction = 1 - 3 / (4 * n - 9)
    return float(d * correction)


def glass_delta(
    treatment: list[float],
    control: list[float],
) -> float:
    """Glass's Δ — effect size using the control group's SD.

    Δ = (M_treatment − M_control) / SD_control.

    Args:
        treatment: Treatment group sample (length ≥ 1).
        control: Control group sample (length ≥ 2).

    Returns:
        Glass's Δ as a float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If treatment is empty, control has < 2, or control SD is 0.

    Usage Example:
        >>> round(glass_delta([3, 4, 5, 6, 7], [1, 2, 3, 4, 5]), 4)
        1.2649

    Complexity: O(n + m)
    """
    if not isinstance(treatment, list):
        raise TypeError("treatment must be a list.")
    if not isinstance(control, list):
        raise TypeError("control must be a list.")
    if len(treatment) < 1:
        raise ValueError("treatment must have at least 1 element.")
    if len(control) < 2:
        raise ValueError("control must have at least 2 elements.")
    for i, v in enumerate(treatment):
        if not isinstance(v, (int, float)):
            raise TypeError(f"treatment[{i}] must be numeric.")
    for i, v in enumerate(control):
        if not isinstance(v, (int, float)):
            raise TypeError(f"control[{i}] must be numeric.")

    m_t = sum(treatment) / len(treatment)
    m_c = sum(control) / len(control)
    var_c = sum((x - m_c) ** 2 for x in control) / (len(control) - 1)
    if var_c == 0:
        raise ValueError("Control group SD must not be zero.")
    return float((m_t - m_c) / var_c ** 0.5)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 5: Regression, Hypothesis Helpers & Distribution Functions
# ---------------------------------------------------------------------------

def r_squared(
    observed: list[float],
    predicted: list[float],
) -> float:
    """Coefficient of determination (R²).

    R² = 1 − SS_res / SS_tot.

    Args:
        observed: Observed values (length ≥ 2).
        predicted: Predicted values (same length as observed).

    Returns:
        R² as a float (can be negative for poor models).

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ, < 2 elements, or total SS is zero.

    Usage Example:
        >>> round(r_squared([1, 2, 3, 4, 5], [1.1, 2.0, 2.9, 4.1, 5.0]), 4)
        0.997

    Complexity: O(n)
    """
    if not isinstance(observed, list) or not isinstance(predicted, list):
        raise TypeError("observed and predicted must be lists.")
    if len(observed) != len(predicted):
        raise ValueError("observed and predicted must have equal length.")
    if len(observed) < 2:
        raise ValueError("At least 2 data points required.")
    for i, (o, p) in enumerate(zip(observed, predicted)):
        if not isinstance(o, (int, float)):
            raise TypeError(f"observed[{i}] must be numeric.")
        if not isinstance(p, (int, float)):
            raise TypeError(f"predicted[{i}] must be numeric.")

    mean_obs = sum(observed) / len(observed)
    ss_tot = sum((o - mean_obs) ** 2 for o in observed)
    if ss_tot == 0:
        raise ValueError("Total sum of squares must not be zero.")
    ss_res = sum((o - p) ** 2 for o, p in zip(observed, predicted))
    return float(1 - ss_res / ss_tot)


def adjusted_r_squared(
    r2: float,
    n: int,
    p: int,
) -> float:
    """Adjusted R² penalised for number of predictors.

    R²_adj = 1 − (1 − R²)(n − 1) / (n − p − 1).

    Args:
        r2: Coefficient of determination.
        n: Number of observations (> p + 1).
        p: Number of predictors (≥ 1).

    Returns:
        Adjusted R² as a float.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If n ≤ p + 1 or p < 1.

    Usage Example:
        >>> round(adjusted_r_squared(0.997, 5, 1), 4)
        0.996

    Complexity: O(1)
    """
    if not isinstance(r2, (int, float)):
        raise TypeError("r2 must be numeric.")
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if not isinstance(p, int):
        raise TypeError("p must be an integer.")
    if p < 1:
        raise ValueError("p must be at least 1.")
    if n <= p + 1:
        raise ValueError("n must be greater than p + 1.")
    return float(1 - (1 - r2) * (n - 1) / (n - p - 1))


def residual_standard_error(
    observed: list[float],
    predicted: list[float],
    p: int = 1,
) -> float:
    """Residual standard error (RSE) of a regression model.

    RSE = √(SS_res / (n − p − 1)).

    Args:
        observed: Observed values.
        predicted: Predicted values (same length).
        p: Number of predictors (default 1).

    Returns:
        RSE as a float.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If lengths differ or degrees of freedom ≤ 0.

    Usage Example:
        >>> round(residual_standard_error([1, 2, 3, 4, 5], [1.1, 2.0, 2.9, 4.1, 5.0], 1), 4)
        0.1

    Complexity: O(n)
    """
    if not isinstance(observed, list) or not isinstance(predicted, list):
        raise TypeError("observed and predicted must be lists.")
    if not isinstance(p, int):
        raise TypeError("p must be an integer.")
    if len(observed) != len(predicted):
        raise ValueError("observed and predicted must have equal length.")
    n = len(observed)
    df = n - p - 1
    if df <= 0:
        raise ValueError("Degrees of freedom must be positive (n > p + 1).")
    for i, (o, pr) in enumerate(zip(observed, predicted)):
        if not isinstance(o, (int, float)):
            raise TypeError(f"observed[{i}] must be numeric.")
        if not isinstance(pr, (int, float)):
            raise TypeError(f"predicted[{i}] must be numeric.")

    ss_res = sum((o - pr) ** 2 for o, pr in zip(observed, predicted))
    return float((ss_res / df) ** 0.5)


def mean_absolute_error(
    observed: list[float],
    predicted: list[float],
) -> float:
    """Mean absolute error (MAE).

    MAE = (1/n) Σ |observed_i − predicted_i|.

    Args:
        observed: Observed values.
        predicted: Predicted values (same length).

    Returns:
        MAE as a float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ or are empty.

    Usage Example:
        >>> mean_absolute_error([1, 2, 3], [1.5, 2.5, 3.5])
        0.5

    Complexity: O(n)
    """
    if not isinstance(observed, list) or not isinstance(predicted, list):
        raise TypeError("observed and predicted must be lists.")
    if len(observed) != len(predicted):
        raise ValueError("observed and predicted must have equal length.")
    if len(observed) == 0:
        raise ValueError("Lists must not be empty.")
    for i, (o, p) in enumerate(zip(observed, predicted)):
        if not isinstance(o, (int, float)):
            raise TypeError(f"observed[{i}] must be numeric.")
        if not isinstance(p, (int, float)):
            raise TypeError(f"predicted[{i}] must be numeric.")

    return float(sum(abs(o - p) for o, p in zip(observed, predicted)) / len(observed))


def mean_absolute_percentage_error(
    observed: list[float],
    predicted: list[float],
) -> float:
    """Mean absolute percentage error (MAPE).

    MAPE = (100/n) Σ |observed_i − predicted_i| / |observed_i|.

    Args:
        observed: Observed values (all non-zero).
        predicted: Predicted values (same length).

    Returns:
        MAPE as a percentage float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ, empty, or any observed value is zero.

    Usage Example:
        >>> round(mean_absolute_percentage_error([100, 200, 300], [110, 190, 280]), 2)
        7.22

    Complexity: O(n)
    """
    if not isinstance(observed, list) or not isinstance(predicted, list):
        raise TypeError("observed and predicted must be lists.")
    if len(observed) != len(predicted):
        raise ValueError("observed and predicted must have equal length.")
    if len(observed) == 0:
        raise ValueError("Lists must not be empty.")
    for i, (o, p) in enumerate(zip(observed, predicted)):
        if not isinstance(o, (int, float)):
            raise TypeError(f"observed[{i}] must be numeric.")
        if not isinstance(p, (int, float)):
            raise TypeError(f"predicted[{i}] must be numeric.")
        if o == 0:
            raise ValueError(f"observed[{i}] must not be zero.")

    return float(100 * sum(abs(o - p) / abs(o) for o, p in zip(observed, predicted)) / len(observed))


def root_mean_squared_log_error(
    observed: list[float],
    predicted: list[float],
) -> float:
    """Root mean squared logarithmic error (RMSLE).

    RMSLE = √((1/n) Σ (ln(1+observed) − ln(1+predicted))²).

    Args:
        observed: Observed values (all ≥ 0).
        predicted: Predicted values (all ≥ 0, same length).

    Returns:
        RMSLE as a float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ, empty, or negative values present.

    Usage Example:
        >>> round(root_mean_squared_log_error([3, 5, 2.5], [2.5, 5, 4]), 4)
        0.2199

    Complexity: O(n)
    """
    import math
    if not isinstance(observed, list) or not isinstance(predicted, list):
        raise TypeError("observed and predicted must be lists.")
    if len(observed) != len(predicted):
        raise ValueError("observed and predicted must have equal length.")
    if len(observed) == 0:
        raise ValueError("Lists must not be empty.")
    for i, (o, p) in enumerate(zip(observed, predicted)):
        if not isinstance(o, (int, float)):
            raise TypeError(f"observed[{i}] must be numeric.")
        if not isinstance(p, (int, float)):
            raise TypeError(f"predicted[{i}] must be numeric.")
        if o < 0 or p < 0:
            raise ValueError("All values must be non-negative.")

    msle = sum((math.log(1 + o) - math.log(1 + p)) ** 2
               for o, p in zip(observed, predicted)) / len(observed)
    return float(msle ** 0.5)


def z_score(
    value: float,
    mean: float,
    std_dev: float,
) -> float:
    """Standard score (z-score).

    z = (x − μ) / σ.

    Args:
        value: The observed value.
        mean: Population or sample mean.
        std_dev: Standard deviation (> 0).

    Returns:
        z-score as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If std_dev is not positive.

    Usage Example:
        >>> z_score(85, 70, 10)
        1.5

    Complexity: O(1)
    """
    for name, val in (("value", value), ("mean", mean), ("std_dev", std_dev)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if std_dev <= 0:
        raise ValueError("std_dev must be positive.")
    return float((value - mean) / std_dev)


def z_score_to_percentile(
    z: float,
) -> float:
    """Approximate percentile from z-score using the cumulative normal.

    Uses the Abramowitz & Stegun rational approximation.

    Args:
        z: Standard z-score.

    Returns:
        Percentile in [0, 100].

    Raises:
        TypeError: If z is not numeric.

    Usage Example:
        >>> round(z_score_to_percentile(1.96), 2)
        97.5

    Complexity: O(1)
    """
    import math
    if not isinstance(z, (int, float)):
        raise TypeError("z must be numeric.")
    cdf = 0.5 * (1.0 + math.erf(z / math.sqrt(2)))
    return float(cdf * 100)


def percentile_rank(
    data: list[float],
    value: float,
) -> float:
    """Percentile rank of a value within a dataset.

    Returns the percentage of values that fall at or below the given value.

    Args:
        data: List of numeric values (non-empty).
        value: The value to rank.

    Returns:
        Percentile rank in [0, 100].

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is empty.

    Usage Example:
        >>> percentile_rank([1, 2, 3, 4, 5], 3)
        60.0

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(value, (int, float)):
        raise TypeError("value must be numeric.")
    if len(data) == 0:
        raise ValueError("data must not be empty.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    count = sum(1 for x in data if x <= value)
    return float(count / len(data) * 100)


def point_biserial_correlation(
    binary: list[int],
    continuous: list[float],
) -> float:
    """Point-biserial correlation between a binary and continuous variable.

    r_pb = (M1 − M0) / s × √(n0·n1 / n²).

    Args:
        binary: List of 0s and 1s.
        continuous: List of corresponding continuous values (same length).

    Returns:
        Point-biserial r in [−1, 1].

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If lengths differ, < 2 elements, or binary not {0,1}.

    Usage Example:
        >>> round(point_biserial_correlation([0, 0, 1, 1], [10, 12, 20, 22]), 4)
        0.8492

    Complexity: O(n)
    """
    if not isinstance(binary, list) or not isinstance(continuous, list):
        raise TypeError("binary and continuous must be lists.")
    if len(binary) != len(continuous):
        raise ValueError("binary and continuous must have equal length.")
    if len(binary) < 2:
        raise ValueError("At least 2 data points required.")

    group0 = []
    group1 = []
    for i, (b, c) in enumerate(zip(binary, continuous)):
        if not isinstance(b, int) or b not in (0, 1):
            raise TypeError(f"binary[{i}] must be 0 or 1.")
        if not isinstance(c, (int, float)):
            raise TypeError(f"continuous[{i}] must be numeric.")
        if b == 0:
            group0.append(c)
        else:
            group1.append(c)

    if len(group0) == 0 or len(group1) == 0:
        raise ValueError("Both groups must have at least one element.")

    n = len(continuous)
    m0 = sum(group0) / len(group0)
    m1 = sum(group1) / len(group1)
    mean_all = sum(continuous) / n
    sd = (sum((x - mean_all) ** 2 for x in continuous) / (n - 1)) ** 0.5
    if sd == 0:
        raise ValueError("Standard deviation must not be zero.")
    return float((m1 - m0) / sd * (len(group0) * len(group1) / n ** 2) ** 0.5)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 6: Information Theory, Distances & Resampling
# ---------------------------------------------------------------------------

def shannon_entropy(
    probabilities: list[float],
) -> float:
    """Shannon entropy H(X) = −Σ p·log₂(p).

    Args:
        probabilities: List of probabilities that sum to 1. Each in (0, 1].

    Returns:
        Entropy in bits as a float.

    Raises:
        TypeError: If probabilities is not a list of numerics.
        ValueError: If empty, any value ≤ 0, or sum ≠ 1 (within tolerance).

    Usage Example:
        >>> round(shannon_entropy([0.5, 0.5]), 4)
        1.0

    Complexity: O(n)
    """
    import math
    if not isinstance(probabilities, list):
        raise TypeError("probabilities must be a list.")
    if len(probabilities) == 0:
        raise ValueError("probabilities must not be empty.")
    for i, p in enumerate(probabilities):
        if not isinstance(p, (int, float)):
            raise TypeError(f"probabilities[{i}] must be numeric.")
        if p <= 0:
            raise ValueError(f"probabilities[{i}] must be positive.")
    if abs(sum(probabilities) - 1.0) > 1e-6:
        raise ValueError("probabilities must sum to 1.")

    return float(-sum(p * math.log2(p) for p in probabilities))


def cross_entropy(
    p: list[float],
    q: list[float],
) -> float:
    """Cross-entropy H(P, Q) = −Σ p·log₂(q).

    Args:
        p: True distribution (probabilities summing to 1, each > 0).
        q: Predicted distribution (same length, each > 0).

    Returns:
        Cross-entropy in bits as a float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ, empty, or constraints violated.

    Usage Example:
        >>> round(cross_entropy([0.5, 0.5], [0.6, 0.4]), 4)
        1.0294

    Complexity: O(n)
    """
    import math
    if not isinstance(p, list) or not isinstance(q, list):
        raise TypeError("p and q must be lists.")
    if len(p) != len(q):
        raise ValueError("p and q must have equal length.")
    if len(p) == 0:
        raise ValueError("Lists must not be empty.")
    for i, (pi, qi) in enumerate(zip(p, q)):
        if not isinstance(pi, (int, float)) or not isinstance(qi, (int, float)):
            raise TypeError(f"Element [{i}] must be numeric.")
        if pi <= 0 or qi <= 0:
            raise ValueError(f"Element [{i}] must be positive.")

    return float(-sum(pi * math.log2(qi) for pi, qi in zip(p, q)))


def kl_divergence(
    p: list[float],
    q: list[float],
) -> float:
    """Kullback-Leibler divergence D_KL(P || Q) = Σ p·log₂(p/q).

    Args:
        p: True distribution (probabilities summing to 1, each > 0).
        q: Approximating distribution (same length, each > 0).

    Returns:
        KL divergence in bits as a float (≥ 0).

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ, empty, or constraints violated.

    Usage Example:
        >>> round(kl_divergence([0.5, 0.5], [0.6, 0.4]), 4)
        0.0294

    Complexity: O(n)
    """
    import math
    if not isinstance(p, list) or not isinstance(q, list):
        raise TypeError("p and q must be lists.")
    if len(p) != len(q):
        raise ValueError("p and q must have equal length.")
    if len(p) == 0:
        raise ValueError("Lists must not be empty.")
    for i, (pi, qi) in enumerate(zip(p, q)):
        if not isinstance(pi, (int, float)) or not isinstance(qi, (int, float)):
            raise TypeError(f"Element [{i}] must be numeric.")
        if pi <= 0 or qi <= 0:
            raise ValueError(f"Element [{i}] must be positive.")

    return float(sum(pi * math.log2(pi / qi) for pi, qi in zip(p, q)))


def js_divergence(
    p: list[float],
    q: list[float],
) -> float:
    """Jensen-Shannon divergence: symmetric, bounded version of KL.

    JSD(P || Q) = ½ D_KL(P || M) + ½ D_KL(Q || M) where M = ½(P+Q).

    Args:
        p: Distribution P (probabilities summing to 1, each > 0).
        q: Distribution Q (same length, each > 0).

    Returns:
        JS divergence in bits, in [0, 1].

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ, empty, or constraints violated.

    Usage Example:
        >>> round(js_divergence([0.5, 0.5], [0.6, 0.4]), 4)
        0.0073

    Complexity: O(n)
    """
    import math
    if not isinstance(p, list) or not isinstance(q, list):
        raise TypeError("p and q must be lists.")
    if len(p) != len(q):
        raise ValueError("p and q must have equal length.")
    if len(p) == 0:
        raise ValueError("Lists must not be empty.")
    for i, (pi, qi) in enumerate(zip(p, q)):
        if not isinstance(pi, (int, float)) or not isinstance(qi, (int, float)):
            raise TypeError(f"Element [{i}] must be numeric.")
        if pi <= 0 or qi <= 0:
            raise ValueError(f"Element [{i}] must be positive.")

    m = [(pi + qi) / 2 for pi, qi in zip(p, q)]
    kl_pm = sum(pi * math.log2(pi / mi) for pi, mi in zip(p, m))
    kl_qm = sum(qi * math.log2(qi / mi) for qi, mi in zip(q, m))
    return float((kl_pm + kl_qm) / 2)


def mutual_information(
    joint: list[list[float]],
) -> float:
    """Mutual information I(X;Y) from a joint probability table.

    I(X;Y) = Σ_x Σ_y p(x,y) log₂(p(x,y) / (p(x)·p(y))).

    Args:
        joint: 2D list (matrix) of joint probabilities. All > 0, sum to 1.

    Returns:
        Mutual information in bits as a float.

    Raises:
        TypeError: If joint is not a list of lists of numerics.
        ValueError: If empty, non-rectangular, or values invalid.

    Usage Example:
        >>> round(mutual_information([[0.25, 0.25], [0.25, 0.25]]), 4)
        0.0

    Complexity: O(rows × cols)
    """
    import math
    if not isinstance(joint, list):
        raise TypeError("joint must be a list.")
    if len(joint) == 0:
        raise ValueError("joint must not be empty.")
    cols = None
    for i, row in enumerate(joint):
        if not isinstance(row, list):
            raise TypeError(f"joint[{i}] must be a list.")
        if cols is None:
            cols = len(row)
        elif len(row) != cols:
            raise ValueError("All rows must have equal length.")
        for j, v in enumerate(row):
            if not isinstance(v, (int, float)):
                raise TypeError(f"joint[{i}][{j}] must be numeric.")
            if v <= 0:
                raise ValueError(f"joint[{i}][{j}] must be positive.")

    rows = len(joint)
    # Marginals
    p_x = [sum(joint[i][j] for j in range(cols)) for i in range(rows)]
    p_y = [sum(joint[i][j] for i in range(rows)) for j in range(cols)]

    mi = 0.0
    for i in range(rows):
        for j in range(cols):
            mi += joint[i][j] * math.log2(joint[i][j] / (p_x[i] * p_y[j]))
    return float(mi)


def mahalanobis_distance_1d(
    x: float,
    data: list[float],
) -> float:
    """Mahalanobis distance of a point from a 1D dataset.

    D = |x − μ| / σ.

    Args:
        x: The point to measure.
        data: The reference dataset (length ≥ 2).

    Returns:
        Mahalanobis distance as a float.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data has < 2 elements or SD is zero.

    Usage Example:
        >>> round(mahalanobis_distance_1d(10, [2, 4, 4, 4, 5, 5, 7, 9]), 4)
        2.3385

    Complexity: O(n)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if len(data) < 2:
        raise ValueError("data must have at least 2 elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    n = len(data)
    mean = sum(data) / n
    var = sum((v - mean) ** 2 for v in data) / (n - 1)
    if var == 0:
        raise ValueError("Standard deviation must not be zero.")
    return float(abs(x - mean) / var ** 0.5)


def cosine_similarity(
    a: list[float],
    b: list[float],
) -> float:
    """Cosine similarity between two vectors.

    cos(θ) = (a·b) / (||a|| × ||b||).

    Args:
        a: First vector (non-empty).
        b: Second vector (same length, non-empty).

    Returns:
        Cosine similarity in [−1, 1].

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ, empty, or a zero-norm vector.

    Usage Example:
        >>> round(cosine_similarity([1, 2, 3], [4, 5, 6]), 4)
        0.9746

    Complexity: O(n)
    """
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("a and b must be lists.")
    if len(a) != len(b):
        raise ValueError("a and b must have equal length.")
    if len(a) == 0:
        raise ValueError("Vectors must not be empty.")
    for i, (ai, bi) in enumerate(zip(a, b)):
        if not isinstance(ai, (int, float)):
            raise TypeError(f"a[{i}] must be numeric.")
        if not isinstance(bi, (int, float)):
            raise TypeError(f"b[{i}] must be numeric.")

    dot = sum(ai * bi for ai, bi in zip(a, b))
    norm_a = sum(ai ** 2 for ai in a) ** 0.5
    norm_b = sum(bi ** 2 for bi in b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        raise ValueError("Vectors must have non-zero norm.")
    return float(dot / (norm_a * norm_b))


def euclidean_distance(
    a: list[float],
    b: list[float],
) -> float:
    """Euclidean distance between two vectors.

    d = √(Σ (a_i − b_i)²).

    Args:
        a: First vector.
        b: Second vector (same length).

    Returns:
        Euclidean distance as a float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ or empty.

    Usage Example:
        >>> round(euclidean_distance([1, 2, 3], [4, 5, 6]), 4)
        5.1962

    Complexity: O(n)
    """
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("a and b must be lists.")
    if len(a) != len(b):
        raise ValueError("a and b must have equal length.")
    if len(a) == 0:
        raise ValueError("Vectors must not be empty.")
    for i, (ai, bi) in enumerate(zip(a, b)):
        if not isinstance(ai, (int, float)):
            raise TypeError(f"a[{i}] must be numeric.")
        if not isinstance(bi, (int, float)):
            raise TypeError(f"b[{i}] must be numeric.")

    return float(sum((ai - bi) ** 2 for ai, bi in zip(a, b)) ** 0.5)


def manhattan_distance(
    a: list[float],
    b: list[float],
) -> float:
    """Manhattan (L1) distance between two vectors.

    d = Σ |a_i − b_i|.

    Args:
        a: First vector.
        b: Second vector (same length).

    Returns:
        Manhattan distance as a float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ or empty.

    Usage Example:
        >>> manhattan_distance([1, 2, 3], [4, 5, 6])
        9.0

    Complexity: O(n)
    """
    if not isinstance(a, list) or not isinstance(b, list):
        raise TypeError("a and b must be lists.")
    if len(a) != len(b):
        raise ValueError("a and b must have equal length.")
    if len(a) == 0:
        raise ValueError("Vectors must not be empty.")
    for i, (ai, bi) in enumerate(zip(a, b)):
        if not isinstance(ai, (int, float)):
            raise TypeError(f"a[{i}] must be numeric.")
        if not isinstance(bi, (int, float)):
            raise TypeError(f"b[{i}] must be numeric.")

    return float(sum(abs(ai - bi) for ai, bi in zip(a, b)))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 7: Time-Series, Smoothing & Sampling Utilities
# ---------------------------------------------------------------------------

def simple_moving_average(
    data: list[float],
    window: int,
) -> list[float]:
    """Simple moving average (SMA) over a sliding window.

    Args:
        data: List of numeric values (length ≥ window).
        window: Window size (positive integer).

    Returns:
        List of SMA values (length = len(data) − window + 1).

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is shorter than window.

    Usage Example:
        >>> simple_moving_average([1, 2, 3, 4, 5], 3)
        [2.0, 3.0, 4.0]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(window, int):
        raise TypeError("window must be an integer.")
    if window <= 0:
        raise ValueError("window must be positive.")
    if len(data) < window:
        raise ValueError("data must have at least window elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    result = []
    current_sum = sum(data[:window])
    result.append(current_sum / window)
    for i in range(window, len(data)):
        current_sum += data[i] - data[i - window]
        result.append(current_sum / window)
    return [float(x) for x in result]


def exponential_moving_average(
    data: list[float],
    alpha: float,
) -> list[float]:
    """Exponential moving average (EMA) with smoothing factor alpha.

    EMA_t = α × data_t + (1 − α) × EMA_{t−1}, with EMA_0 = data_0.

    Args:
        data: List of numeric values (non-empty).
        alpha: Smoothing factor in (0, 1].

    Returns:
        List of EMA values (same length as data).

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is empty or alpha out of range.

    Usage Example:
        >>> [round(v, 2) for v in exponential_moving_average([1, 2, 3, 4, 5], 0.5)]
        [1.0, 1.5, 2.25, 3.12, 4.06]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(alpha, (int, float)):
        raise TypeError("alpha must be numeric.")
    if len(data) == 0:
        raise ValueError("data must not be empty.")
    if alpha <= 0 or alpha > 1:
        raise ValueError("alpha must be in (0, 1].")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    result = [float(data[0])]
    for i in range(1, len(data)):
        ema = alpha * data[i] + (1 - alpha) * result[-1]
        result.append(float(ema))
    return result


def weighted_moving_average(
    data: list[float],
    weights: list[float],
) -> list[float]:
    """Weighted moving average (WMA) with custom weights.

    Args:
        data: List of numeric values (length ≥ len(weights)).
        weights: List of weights (non-empty, all positive).

    Returns:
        List of WMA values (length = len(data) − len(weights) + 1).

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is shorter than weights or weights invalid.

    Usage Example:
        >>> [round(v, 4) for v in weighted_moving_average([1, 2, 3, 4, 5], [1, 2, 3])]
        [2.3333, 3.3333, 4.3333]

    Complexity: O(n × w)
    """
    if not isinstance(data, list) or not isinstance(weights, list):
        raise TypeError("data and weights must be lists.")
    if len(weights) == 0:
        raise ValueError("weights must not be empty.")
    if len(data) < len(weights):
        raise ValueError("data must be at least as long as weights.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")
    w_sum = 0.0
    for i, w in enumerate(weights):
        if not isinstance(w, (int, float)):
            raise TypeError(f"weights[{i}] must be numeric.")
        if w <= 0:
            raise ValueError(f"weights[{i}] must be positive.")
        w_sum += w

    w = len(weights)
    result = []
    for i in range(len(data) - w + 1):
        val = sum(data[i + j] * weights[j] for j in range(w)) / w_sum
        result.append(float(val))
    return result


def cumulative_moving_average(
    data: list[float],
) -> list[float]:
    """Cumulative moving average (expanding mean).

    CMA_t = (1/(t+1)) Σ_{i=0}^{t} data_i.

    Args:
        data: List of numeric values (non-empty).

    Returns:
        List of CMA values (same length as data).

    Raises:
        TypeError: If data is not a list of numerics.
        ValueError: If data is empty.

    Usage Example:
        >>> cumulative_moving_average([1, 2, 3, 4, 5])
        [1.0, 1.5, 2.0, 2.5, 3.0]

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if len(data) == 0:
        raise ValueError("data must not be empty.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    result = []
    running = 0.0
    for i, v in enumerate(data):
        running += v
        result.append(float(running / (i + 1)))
    return result


def autocorrelation(
    data: list[float],
    lag: int = 1,
) -> float:
    """Sample autocorrelation at a given lag.

    r(k) = Σ (x_t − x̄)(x_{t+k} − x̄) / Σ (x_t − x̄)².

    Args:
        data: List of numeric values (length > lag).
        lag: Lag offset (positive integer).

    Returns:
        Autocorrelation coefficient in [−1, 1].

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data too short or lag invalid.

    Usage Example:
        >>> round(autocorrelation([1, 2, 3, 4, 5, 4, 3, 2, 1], 1), 4)
        0.5397

    Complexity: O(n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(lag, int):
        raise TypeError("lag must be an integer.")
    if lag <= 0:
        raise ValueError("lag must be positive.")
    if len(data) <= lag:
        raise ValueError("data must have more elements than lag.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    n = len(data)
    mean = sum(data) / n
    denom = sum((x - mean) ** 2 for x in data)
    if denom == 0:
        return 0.0
    numer = sum((data[t] - mean) * (data[t + lag] - mean) for t in range(n - lag))
    return float(numer / denom)


def partial_autocorrelation(
    data: list[float],
    max_lag: int,
) -> list[float]:
    """Partial autocorrelation function (PACF) via Durbin-Levinson recursion.

    Args:
        data: List of numeric values (length > max_lag + 1).
        max_lag: Maximum lag to compute (positive integer).

    Returns:
        List of PACF values [pacf(1), pacf(2), … pacf(max_lag)].

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is too short or max_lag invalid.

    Usage Example:
        >>> [round(v, 4) for v in partial_autocorrelation([1, 2, 3, 4, 5, 4, 3, 2, 1], 2)]
        [0.5397, -0.43]

    Complexity: O(max_lag² + n)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(max_lag, int):
        raise TypeError("max_lag must be an integer.")
    if max_lag <= 0:
        raise ValueError("max_lag must be positive.")
    if len(data) <= max_lag + 1:
        raise ValueError("data must have more than max_lag + 1 elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    # Compute autocorrelations
    n = len(data)
    mean = sum(data) / n
    var = sum((x - mean) ** 2 for x in data)
    if var == 0:
        return [0.0] * max_lag

    acf = []
    for k in range(1, max_lag + 1):
        r = sum((data[t] - mean) * (data[t + k] - mean) for t in range(n - k)) / var
        acf.append(r)

    # Durbin-Levinson
    pacf_vals = []
    phi = [[0.0] * (max_lag + 1) for _ in range(max_lag + 1)]
    phi[1][1] = acf[0]
    pacf_vals.append(phi[1][1])

    for k in range(2, max_lag + 1):
        num = acf[k - 1] - sum(phi[k - 1][j] * acf[k - 1 - j] for j in range(1, k))
        den = 1 - sum(phi[k - 1][j] * acf[j - 1] for j in range(1, k))
        if abs(den) < 1e-30:
            phi[k][k] = 0.0
        else:
            phi[k][k] = num / den
        for j in range(1, k):
            phi[k][j] = phi[k - 1][j] - phi[k][k] * phi[k - 1][k - j]
        pacf_vals.append(phi[k][k])

    return [float(v) for v in pacf_vals]


def holt_linear_forecast(
    data: list[float],
    alpha: float,
    beta: float,
    steps: int = 1,
) -> list[float]:
    """Holt's linear exponential smoothing forecast.

    Double exponential smoothing with level and trend components.

    Args:
        data: Historical time series (length ≥ 2).
        alpha: Level smoothing factor in (0, 1].
        beta: Trend smoothing factor in (0, 1].
        steps: Number of future steps to forecast (≥ 1).

    Returns:
        List of forecasted values (length = steps).

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data has < 2 elements or parameters out of range.

    Usage Example:
        >>> [round(v, 2) for v in holt_linear_forecast([1, 2, 3, 4, 5], 0.8, 0.2, 3)]
        [6.0, 7.0, 8.0]

    Complexity: O(n + steps)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(alpha, (int, float)) or not isinstance(beta, (int, float)):
        raise TypeError("alpha and beta must be numeric.")
    if not isinstance(steps, int):
        raise TypeError("steps must be an integer.")
    if len(data) < 2:
        raise ValueError("data must have at least 2 elements.")
    if alpha <= 0 or alpha > 1:
        raise ValueError("alpha must be in (0, 1].")
    if beta <= 0 or beta > 1:
        raise ValueError("beta must be in (0, 1].")
    if steps < 1:
        raise ValueError("steps must be at least 1.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    level = float(data[0])
    trend = float(data[1] - data[0])
    for i in range(1, len(data)):
        new_level = alpha * data[i] + (1 - alpha) * (level + trend)
        new_trend = beta * (new_level - level) + (1 - beta) * trend
        level = new_level
        trend = new_trend

    return [float(level + (i + 1) * trend) for i in range(steps)]


def running_max(
    data: list[float],
    window: int,
) -> list[float]:
    """Running (rolling) maximum over a sliding window.

    Args:
        data: List of numeric values (length ≥ window).
        window: Window size (positive integer).

    Returns:
        List of rolling max values (length = len(data) − window + 1).

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is shorter than window.

    Usage Example:
        >>> running_max([1, 3, 2, 5, 4], 3)
        [3.0, 5.0, 5.0]

    Complexity: O(n × window)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(window, int):
        raise TypeError("window must be an integer.")
    if window <= 0:
        raise ValueError("window must be positive.")
    if len(data) < window:
        raise ValueError("data must have at least window elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    return [float(max(data[i:i + window])) for i in range(len(data) - window + 1)]


def running_min(
    data: list[float],
    window: int,
) -> list[float]:
    """Running (rolling) minimum over a sliding window.

    Args:
        data: List of numeric values (length ≥ window).
        window: Window size (positive integer).

    Returns:
        List of rolling min values (length = len(data) − window + 1).

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is shorter than window.

    Usage Example:
        >>> running_min([1, 3, 2, 5, 4], 3)
        [1.0, 2.0, 2.0]

    Complexity: O(n × window)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(window, int):
        raise TypeError("window must be an integer.")
    if window <= 0:
        raise ValueError("window must be positive.")
    if len(data) < window:
        raise ValueError("data must have at least window elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    return [float(min(data[i:i + window])) for i in range(len(data) - window + 1)]


def running_std(
    data: list[float],
    window: int,
) -> list[float]:
    """Running (rolling) standard deviation over a sliding window (sample).

    Args:
        data: List of numeric values (length ≥ window, window ≥ 2).
        window: Window size (integer ≥ 2).

    Returns:
        List of rolling SD values.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If data is shorter than window or window < 2.

    Usage Example:
        >>> [round(v, 4) for v in running_std([1, 2, 3, 4, 5], 3)]
        [1.0, 1.0, 1.0]

    Complexity: O(n × window)
    """
    if not isinstance(data, list):
        raise TypeError("data must be a list.")
    if not isinstance(window, int):
        raise TypeError("window must be an integer.")
    if window < 2:
        raise ValueError("window must be at least 2.")
    if len(data) < window:
        raise ValueError("data must have at least window elements.")
    for i, v in enumerate(data):
        if not isinstance(v, (int, float)):
            raise TypeError(f"data[{i}] must be numeric.")

    result = []
    for i in range(len(data) - window + 1):
        chunk = data[i:i + window]
        mean = sum(chunk) / window
        var = sum((x - mean) ** 2 for x in chunk) / (window - 1)
        result.append(float(var ** 0.5))
    return result


# ---------------------------------------------------------------------------
# Phase 21 – Batch 8: Bayesian, Hypothesis & Distribution Utilities
# ---------------------------------------------------------------------------

def bayes_theorem(
    prior: float,
    likelihood: float,
    evidence: float,
) -> float:
    """Posterior probability via Bayes' theorem.

    P(H|E) = P(E|H) × P(H) / P(E).

    Args:
        prior: Prior probability P(H) in (0, 1].
        likelihood: Likelihood P(E|H) in [0, 1].
        evidence: Evidence probability P(E) in (0, 1].

    Returns:
        Posterior probability as a float in [0, 1].

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(bayes_theorem(0.01, 0.9, 0.05), 4)
        0.18

    Complexity: O(1)
    """
    for name, val in (("prior", prior), ("likelihood", likelihood), ("evidence", evidence)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if prior <= 0 or prior > 1:
        raise ValueError("prior must be in (0, 1].")
    if likelihood < 0 or likelihood > 1:
        raise ValueError("likelihood must be in [0, 1].")
    if evidence <= 0 or evidence > 1:
        raise ValueError("evidence must be in (0, 1].")
    return float(likelihood * prior / evidence)


def bayesian_update(
    prior: float,
    likelihoods: list[float],
    marginals: list[float],
) -> float:
    """Sequential Bayesian update with multiple evidence events.

    Applies Bayes' theorem iteratively.

    Args:
        prior: Initial prior probability in (0, 1].
        likelihoods: P(E_i|H) for each evidence (all in [0, 1]).
        marginals: P(E_i) for each evidence (all in (0, 1]).

    Returns:
        Updated posterior as a float.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If lengths differ or constraints violated.

    Usage Example:
        >>> round(bayesian_update(0.5, [0.8, 0.9], [0.5, 0.6]), 4)
        1.2

    Complexity: O(n)
    """
    if not isinstance(prior, (int, float)):
        raise TypeError("prior must be numeric.")
    if not isinstance(likelihoods, list) or not isinstance(marginals, list):
        raise TypeError("likelihoods and marginals must be lists.")
    if len(likelihoods) != len(marginals):
        raise ValueError("likelihoods and marginals must have equal length.")
    if prior <= 0 or prior > 1:
        raise ValueError("prior must be in (0, 1].")

    posterior = prior
    for i, (lik, marg) in enumerate(zip(likelihoods, marginals)):
        if not isinstance(lik, (int, float)) or not isinstance(marg, (int, float)):
            raise TypeError(f"Element [{i}] must be numeric.")
        if lik < 0 or lik > 1:
            raise ValueError(f"likelihoods[{i}] must be in [0, 1].")
        if marg <= 0 or marg > 1:
            raise ValueError(f"marginals[{i}] must be in (0, 1].")
        posterior = lik * posterior / marg
    return float(posterior)


def chi_squared_statistic(
    observed: list[float],
    expected: list[float],
) -> float:
    """Chi-squared test statistic: Σ (O − E)² / E.

    Args:
        observed: Observed frequencies (all ≥ 0).
        expected: Expected frequencies (all > 0, same length).

    Returns:
        Chi-squared statistic as a float.

    Raises:
        TypeError: If arguments are not lists of numerics.
        ValueError: If lengths differ, empty, or expected ≤ 0.

    Usage Example:
        >>> round(chi_squared_statistic([10, 20, 30], [15, 15, 30]), 4)
        3.3333

    Complexity: O(n)
    """
    if not isinstance(observed, list) or not isinstance(expected, list):
        raise TypeError("observed and expected must be lists.")
    if len(observed) != len(expected):
        raise ValueError("observed and expected must have equal length.")
    if len(observed) == 0:
        raise ValueError("Lists must not be empty.")
    for i, (o, e) in enumerate(zip(observed, expected)):
        if not isinstance(o, (int, float)) or not isinstance(e, (int, float)):
            raise TypeError(f"Element [{i}] must be numeric.")
        if o < 0:
            raise ValueError(f"observed[{i}] must be non-negative.")
        if e <= 0:
            raise ValueError(f"expected[{i}] must be positive.")

    return float(sum((o - e) ** 2 / e for o, e in zip(observed, expected)))


def cramers_v(
    chi2: float,
    n: int,
    k: int,
) -> float:
    """Cramér's V — effect size for chi-squared tests.

    V = √(χ² / (n × (k − 1))).

    Args:
        chi2: Chi-squared statistic (≥ 0).
        n: Total sample size (> 0).
        k: Minimum of (rows, columns) in the contingency table (≥ 2).

    Returns:
        Cramér's V in [0, 1].

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(cramers_v(10.0, 100, 3), 4)
        0.2236

    Complexity: O(1)
    """
    if not isinstance(chi2, (int, float)):
        raise TypeError("chi2 must be numeric.")
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    if chi2 < 0:
        raise ValueError("chi2 must be non-negative.")
    if n <= 0:
        raise ValueError("n must be positive.")
    if k < 2:
        raise ValueError("k must be at least 2.")
    return float((chi2 / (n * (k - 1))) ** 0.5)


def normal_pdf(
    x: float,
    mu: float = 0.0,
    sigma: float = 1.0,
) -> float:
    """Probability density function of the normal distribution.

    f(x) = (1 / (σ√(2π))) exp(−(x−μ)² / (2σ²)).

    Args:
        x: Point at which to evaluate.
        mu: Mean (default 0).
        sigma: Standard deviation (> 0, default 1).

    Returns:
        PDF value as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If sigma is not positive.

    Usage Example:
        >>> round(normal_pdf(0), 4)
        0.3989

    Complexity: O(1)
    """
    import math
    for name, val in (("x", x), ("mu", mu), ("sigma", sigma)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if sigma <= 0:
        raise ValueError("sigma must be positive.")
    return float(math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi)))


def poisson_pmf(
    k: int,
    lam: float,
) -> float:
    """Probability mass function of the Poisson distribution.

    P(X=k) = (λ^k · e^{−λ}) / k!.

    Args:
        k: Number of events (non-negative integer).
        lam: Average rate of events λ (> 0).

    Returns:
        Probability as a float.

    Raises:
        TypeError: If k is not int or lam is not numeric.
        ValueError: If k < 0 or lam ≤ 0.

    Usage Example:
        >>> round(poisson_pmf(3, 2.5), 4)
        0.2138

    Complexity: O(k)
    """
    import math
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    if not isinstance(lam, (int, float)):
        raise TypeError("lam must be numeric.")
    if k < 0:
        raise ValueError("k must be non-negative.")
    if lam <= 0:
        raise ValueError("lam must be positive.")
    return float(lam ** k * math.exp(-lam) / math.factorial(k))


def binomial_pmf(
    k: int,
    n: int,
    p: float,
) -> float:
    """Probability mass function of the binomial distribution.

    P(X=k) = C(n,k) · p^k · (1−p)^{n−k}.

    Args:
        k: Number of successes (0 ≤ k ≤ n).
        n: Number of trials (positive integer).
        p: Probability of success in [0, 1].

    Returns:
        Probability as a float.

    Raises:
        TypeError: If k or n are not int, or p is not numeric.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(binomial_pmf(3, 10, 0.5), 4)
        0.1172

    Complexity: O(k)
    """
    import math
    if not isinstance(k, int) or not isinstance(n, int):
        raise TypeError("k and n must be integers.")
    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")
    if n <= 0:
        raise ValueError("n must be positive.")
    if k < 0 or k > n:
        raise ValueError("k must be in [0, n].")
    if p < 0 or p > 1:
        raise ValueError("p must be in [0, 1].")
    coeff = math.comb(n, k)
    return float(coeff * p ** k * (1 - p) ** (n - k))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 30: Probability / Statistics Functions (1 of 3)
# ---------------------------------------------------------------------------

def geometric_pmf(k: int, p: float) -> float:
    """Compute the geometric distribution PMF.

    P(X = k) = (1-p)^(k-1) · p,  k = 1, 2, 3, ...

    Args:
        k: Number of trials until first success (≥ 1).
        p: Success probability (0 < p ≤ 1).

    Returns:
        Probability of first success on trial k.

    Raises:
        TypeError: If k is not int or p is not numeric.
        ValueError: If k < 1 or p not in (0, 1].

    Usage Example:
        >>> round(geometric_pmf(3, 0.5), 4)
        0.125

    Complexity: O(1)
    """
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")
    if k < 1:
        raise ValueError("k must be >= 1.")
    p = float(p)
    if p <= 0 or p > 1:
        raise ValueError("p must be in (0, 1].")
    return (1.0 - p) ** (k - 1) * p


def hypergeometric_pmf(k: int, N: int, K: int, n: int) -> float:
    """Compute the hypergeometric distribution PMF.

    P(X = k) = C(K,k)·C(N-K,n-k) / C(N,n)

    Args:
        k: Number of successes drawn.
        N: Population size.
        K: Number of success states in population.
        n: Number of draws.

    Returns:
        Probability.

    Raises:
        TypeError: If arguments are not integers.
        ValueError: If parameters are out of range.

    Usage Example:
        >>> round(hypergeometric_pmf(2, 52, 13, 5), 4)
        0.2743

    Complexity: O(1) using math.comb
    """
    for name, val in [("k", k), ("N", N), ("K", K), ("n", n)]:
        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer.")
    if N < 0 or K < 0 or K > N or n < 0 or n > N:
        raise ValueError("Invalid population/draw parameters.")
    if k < max(0, n - (N - K)) or k > min(n, K):
        return 0.0
    return float(math.comb(K, k) * math.comb(N - K, n - k)) / math.comb(N, n)


def negative_binomial_pmf(k: int, r: int, p: float) -> float:
    """Compute the negative binomial distribution PMF.

    P(X = k) = C(k+r-1, k) · p^r · (1-p)^k,  k = 0, 1, 2, ...

    Args:
        k: Number of failures before the r-th success (≥ 0).
        r: Number of successes (≥ 1).
        p: Success probability (0 < p ≤ 1).

    Returns:
        Probability.

    Raises:
        TypeError: If k or r not int, p not numeric.
        ValueError: If k < 0, r < 1, or p not in (0, 1].

    Usage Example:
        >>> round(negative_binomial_pmf(3, 2, 0.5), 4)
        0.125

    Complexity: O(1)
    """
    if not isinstance(k, int) or not isinstance(r, int):
        raise TypeError("k and r must be integers.")
    if not isinstance(p, (int, float)):
        raise TypeError("p must be numeric.")
    if k < 0:
        raise ValueError("k must be >= 0.")
    if r < 1:
        raise ValueError("r must be >= 1.")
    p = float(p)
    if p <= 0 or p > 1:
        raise ValueError("p must be in (0, 1].")
    return float(math.comb(k + r - 1, k)) * p ** r * (1.0 - p) ** k


def exponential_pdf(x: float, lam: float) -> float:
    """Compute the exponential distribution PDF.

    f(x) = λ·e^(-λx),  x ≥ 0

    Args:
        x: Value (≥ 0).
        lam: Rate parameter λ (> 0).

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If x < 0 or lam ≤ 0.

    Usage Example:
        >>> round(exponential_pdf(1.0, 1.0), 4)
        0.3679

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(lam, (int, float)):
        raise TypeError("x and lam must be numeric.")
    x, lam = float(x), float(lam)
    if x < 0:
        raise ValueError("x must be >= 0.")
    if lam <= 0:
        raise ValueError("lam must be positive.")
    return lam * math.exp(-lam * x)


def exponential_cdf(x: float, lam: float) -> float:
    """Compute the exponential distribution CDF.

    F(x) = 1 - e^(-λx),  x ≥ 0

    Args:
        x: Value (≥ 0).
        lam: Rate parameter λ (> 0).

    Returns:
        Cumulative probability.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If x < 0 or lam ≤ 0.

    Usage Example:
        >>> round(exponential_cdf(1.0, 1.0), 4)
        0.6321

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(lam, (int, float)):
        raise TypeError("x and lam must be numeric.")
    x, lam = float(x), float(lam)
    if x < 0:
        raise ValueError("x must be >= 0.")
    if lam <= 0:
        raise ValueError("lam must be positive.")
    return 1.0 - math.exp(-lam * x)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 31: Probability / Statistics Functions (2 of 3)
# ---------------------------------------------------------------------------

def uniform_pdf(x: float, a: float, b: float) -> float:
    """Compute the continuous uniform distribution PDF.

    f(x) = 1/(b-a) for a ≤ x ≤ b, else 0.

    Args:
        x: Value.
        a: Lower bound.
        b: Upper bound.

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a ≥ b.

    Usage Example:
        >>> uniform_pdf(0.5, 0.0, 1.0)
        1.0

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("All arguments must be numeric.")
    x, a, b = float(x), float(a), float(b)
    if a >= b:
        raise ValueError("a must be less than b.")
    if x < a or x > b:
        return 0.0
    return 1.0 / (b - a)


def uniform_cdf(x: float, a: float, b: float) -> float:
    """Compute the continuous uniform distribution CDF.

    F(x) = (x-a)/(b-a) for a ≤ x ≤ b.

    Args:
        x: Value.
        a: Lower bound.
        b: Upper bound.

    Returns:
        Cumulative probability.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a ≥ b.

    Usage Example:
        >>> uniform_cdf(0.5, 0.0, 1.0)
        0.5

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("All arguments must be numeric.")
    x, a, b = float(x), float(a), float(b)
    if a >= b:
        raise ValueError("a must be less than b.")
    if x <= a:
        return 0.0
    if x >= b:
        return 1.0
    return (x - a) / (b - a)


def normal_cdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    """Compute the normal distribution CDF using the error function.

    F(x) = 0.5(1 + erf((x - μ) / (σ√2)))

    Args:
        x: Value.
        mu: Mean (default 0).
        sigma: Standard deviation (default 1, must be > 0).

    Returns:
        Cumulative probability.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If sigma ≤ 0.

    Usage Example:
        >>> round(normal_cdf(0.0), 4)
        0.5

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(mu, (int, float)) or not isinstance(sigma, (int, float)):
        raise TypeError("All arguments must be numeric.")
    sigma = float(sigma)
    if sigma <= 0:
        raise ValueError("sigma must be positive.")
    return 0.5 * (1.0 + math.erf((float(x) - float(mu)) / (sigma * math.sqrt(2.0))))


def log_normal_pdf(x: float, mu: float = 0.0, sigma: float = 1.0) -> float:
    """Compute the log-normal distribution PDF.

    f(x) = (1/(xσ√(2π))) · exp(-(ln(x)-μ)²/(2σ²))

    Args:
        x: Value (> 0).
        mu: Mean of the log (default 0).
        sigma: Std dev of the log (default 1, > 0).

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If x ≤ 0 or sigma ≤ 0.

    Usage Example:
        >>> round(log_normal_pdf(1.0), 4)
        0.3989

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(mu, (int, float)) or not isinstance(sigma, (int, float)):
        raise TypeError("All arguments must be numeric.")
    x, mu, sigma = float(x), float(mu), float(sigma)
    if x <= 0:
        raise ValueError("x must be positive.")
    if sigma <= 0:
        raise ValueError("sigma must be positive.")
    log_x = math.log(x)
    return (1.0 / (x * sigma * math.sqrt(2.0 * math.pi))) * math.exp(-0.5 * ((log_x - mu) / sigma) ** 2)


def chi_squared_pdf(x: float, k: int) -> float:
    """Compute the chi-squared distribution PDF.

    f(x) = x^(k/2-1)·e^(-x/2) / (2^(k/2)·Γ(k/2))

    Args:
        x: Value (≥ 0).
        k: Degrees of freedom (≥ 1).

    Returns:
        Probability density.

    Raises:
        TypeError: If x is not numeric or k is not int.
        ValueError: If x < 0 or k < 1.

    Usage Example:
        >>> round(chi_squared_pdf(2.0, 3), 4)
        0.2076

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    if not isinstance(k, int):
        raise TypeError("k must be an integer.")
    x = float(x)
    if x < 0:
        raise ValueError("x must be >= 0.")
    if k < 1:
        raise ValueError("k must be >= 1.")
    if x == 0:
        return float("inf") if k < 2 else (0.5 if k == 2 else 0.0)
    half_k = k / 2.0
    return (x ** (half_k - 1.0) * math.exp(-x / 2.0)) / (2.0 ** half_k * math.gamma(half_k))


def cauchy_pdf(x: float, x0: float = 0.0, gamma: float = 1.0) -> float:
    """Compute the Cauchy distribution PDF.

    f(x) = 1 / (πγ(1 + ((x-x0)/γ)²))

    Args:
        x: Value.
        x0: Location parameter (default 0).
        gamma: Scale parameter (default 1, > 0).

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If gamma ≤ 0.

    Usage Example:
        >>> round(cauchy_pdf(0.0), 4)
        0.3183

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(x0, (int, float)) or not isinstance(gamma, (int, float)):
        raise TypeError("All arguments must be numeric.")
    gamma = float(gamma)
    if gamma <= 0:
        raise ValueError("gamma must be positive.")
    z = (float(x) - float(x0)) / gamma
    return 1.0 / (math.pi * gamma * (1.0 + z * z))


def beta_function(a: float, b: float) -> float:
    """Compute the beta function B(a, b) = Γ(a)Γ(b)/Γ(a+b).

    Args:
        a: First parameter (> 0).
        b: Second parameter (> 0).

    Returns:
        Beta function value.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a or b ≤ 0.

    Usage Example:
        >>> round(beta_function(2.0, 3.0), 4)
        0.0833

    Complexity: O(1)
    """
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a and b must be numeric.")
    a, b = float(a), float(b)
    if a <= 0 or b <= 0:
        raise ValueError("a and b must be positive.")
    return math.exp(math.lgamma(a) + math.lgamma(b) - math.lgamma(a + b))


def weibull_pdf(x: float, k: float, lam: float) -> float:
    """Compute the Weibull distribution PDF.

    f(x) = (k/λ)(x/λ)^(k-1)·e^(-(x/λ)^k)

    Args:
        x: Value (≥ 0).
        k: Shape parameter (> 0).
        lam: Scale parameter (> 0).

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If x < 0, k ≤ 0, or lam ≤ 0.

    Usage Example:
        >>> round(weibull_pdf(1.0, 1.0, 1.0), 4)
        0.3679

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(k, (int, float)) or not isinstance(lam, (int, float)):
        raise TypeError("All arguments must be numeric.")
    x, k, lam = float(x), float(k), float(lam)
    if x < 0:
        raise ValueError("x must be >= 0.")
    if k <= 0 or lam <= 0:
        raise ValueError("k and lam must be positive.")
    if x == 0:
        return float("inf") if k < 1 else (1.0 / lam if k == 1 else 0.0)
    return (k / lam) * (x / lam) ** (k - 1) * math.exp(-(x / lam) ** k)


def gamma_pdf(x: float, alpha: float, beta: float) -> float:
    """Compute the gamma distribution PDF.

    f(x) = β^α · x^(α-1) · e^(-βx) / Γ(α)

    Args:
        x: Value (≥ 0).
        alpha: Shape parameter (> 0).
        beta: Rate parameter (> 0).

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If x < 0, alpha ≤ 0, or beta ≤ 0.

    Usage Example:
        >>> round(gamma_pdf(1.0, 2.0, 1.0), 4)
        0.3679

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(alpha, (int, float)) or not isinstance(beta, (int, float)):
        raise TypeError("All arguments must be numeric.")
    x, alpha, beta = float(x), float(alpha), float(beta)
    if x < 0:
        raise ValueError("x must be >= 0.")
    if alpha <= 0 or beta <= 0:
        raise ValueError("alpha and beta must be positive.")
    if x == 0:
        return float("inf") if alpha < 1 else (beta if alpha == 1 else 0.0)
    return (beta ** alpha * x ** (alpha - 1) * math.exp(-beta * x)) / math.gamma(alpha)


def multinomial_coefficient(*counts: int) -> int:
    """Compute the multinomial coefficient n! / (k1!·k2!·...·km!).

    Args:
        *counts: Non-negative integer counts.

    Returns:
        Multinomial coefficient.

    Raises:
        TypeError: If any count is not int.
        ValueError: If any count < 0.

    Usage Example:
        >>> multinomial_coefficient(2, 3, 4)
        1260

    Complexity: O(m) where m = number of counts
    """
    total = 0
    for c in counts:
        if not isinstance(c, int):
            raise TypeError("All counts must be integers.")
        if c < 0:
            raise ValueError("All counts must be non-negative.")
        total += c
    result = math.factorial(total)
    for c in counts:
        result //= math.factorial(c)
    return result


# ---------------------------------------------------------------------------
# Phase 21 – Batch 32: Probability / Statistics Functions (3 of 3)
# ---------------------------------------------------------------------------

def laplace_pdf(x: float, mu: float = 0.0, b: float = 1.0) -> float:
    """Compute the Laplace distribution PDF.

    f(x) = (1/(2b)) · e^(-|x-μ|/b)

    Args:
        x: Value.
        mu: Location parameter (default 0).
        b: Scale parameter (default 1, > 0).

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If b ≤ 0.

    Usage Example:
        >>> round(laplace_pdf(0.0), 4)
        0.5

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(mu, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("All arguments must be numeric.")
    b = float(b)
    if b <= 0:
        raise ValueError("b must be positive.")
    return (1.0 / (2.0 * b)) * math.exp(-abs(float(x) - float(mu)) / b)


def logistic_pdf(x: float, mu: float = 0.0, s: float = 1.0) -> float:
    """Compute the logistic distribution PDF.

    f(x) = e^(-(x-μ)/s) / (s(1 + e^(-(x-μ)/s))²)

    Args:
        x: Value.
        mu: Location parameter (default 0).
        s: Scale parameter (default 1, > 0).

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If s ≤ 0.

    Usage Example:
        >>> round(logistic_pdf(0.0), 4)
        0.25

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(mu, (int, float)) or not isinstance(s, (int, float)):
        raise TypeError("All arguments must be numeric.")
    s = float(s)
    if s <= 0:
        raise ValueError("s must be positive.")
    z = (float(x) - float(mu)) / s
    if z > 500:
        return 0.0
    exp_neg_z = math.exp(-z)
    return exp_neg_z / (s * (1.0 + exp_neg_z) ** 2)


def logistic_cdf(x: float, mu: float = 0.0, s: float = 1.0) -> float:
    """Compute the logistic distribution CDF.

    F(x) = 1 / (1 + e^(-(x-μ)/s))

    Args:
        x: Value.
        mu: Location parameter (default 0).
        s: Scale parameter (default 1, > 0).

    Returns:
        Cumulative probability.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If s ≤ 0.

    Usage Example:
        >>> logistic_cdf(0.0)
        0.5

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(mu, (int, float)) or not isinstance(s, (int, float)):
        raise TypeError("All arguments must be numeric.")
    s = float(s)
    if s <= 0:
        raise ValueError("s must be positive.")
    z = (float(x) - float(mu)) / s
    return 1.0 / (1.0 + math.exp(-z))


def triangular_pdf(x: float, a: float, b: float, c: float) -> float:
    """Compute the triangular distribution PDF.

    Args:
        x: Value.
        a: Lower limit.
        b: Upper limit.
        c: Mode (a ≤ c ≤ b).

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a ≥ b or c not in [a, b].

    Usage Example:
        >>> round(triangular_pdf(0.5, 0.0, 1.0, 0.5), 4)
        2.0

    Complexity: O(1)
    """
    for name, val in [("x", x), ("a", a), ("b", b), ("c", c)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    x, a, b, c = float(x), float(a), float(b), float(c)
    if a >= b:
        raise ValueError("a must be less than b.")
    if c < a or c > b:
        raise ValueError("c must be in [a, b].")
    if x < a or x > b:
        return 0.0
    if x <= c:
        return 2.0 * (x - a) / ((b - a) * (c - a)) if c > a else 0.0
    return 2.0 * (b - x) / ((b - a) * (b - c)) if b > c else 0.0


def pareto_pdf(x: float, x_m: float, alpha: float) -> float:
    """Compute the Pareto distribution PDF.

    f(x) = α·x_m^α / x^(α+1) for x ≥ x_m.

    Args:
        x: Value (≥ x_m).
        x_m: Scale (minimum value, > 0).
        alpha: Shape parameter (> 0).

    Returns:
        Probability density.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If x_m ≤ 0 or alpha ≤ 0.

    Usage Example:
        >>> round(pareto_pdf(2.0, 1.0, 3.0), 4)
        0.1875

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)) or not isinstance(x_m, (int, float)) or not isinstance(alpha, (int, float)):
        raise TypeError("All arguments must be numeric.")
    x, x_m, alpha = float(x), float(x_m), float(alpha)
    if x_m <= 0 or alpha <= 0:
        raise ValueError("x_m and alpha must be positive.")
    if x < x_m:
        return 0.0
    return alpha * x_m ** alpha / x ** (alpha + 1)
