"""Numeric Statistics Module.

This module provides comprehensive statistical analysis functions for numeric data,
including measures of central tendency, dispersion, correlation, and percentiles.

Key Features:
    - Descriptive statistics (mean, median, mode, range)
    - Measures of dispersion (variance, standard deviation, IQR)
    - Correlation and covariance calculations
    - Percentile and frequency calculations
    - Sum of squares computation

Example:
    >>> from formulite.fxNumeric.numeric_statistics import calculate_mean, calculate_median
    >>> calculate_mean([1, 2, 3, 4, 5])
    3.0
    >>> calculate_median([1, 2, 3, 4])
    2.5
"""
import math
import statistics
from typing import List, Union


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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if not data:
        raise ValueError("Input list cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if not data:
        raise ValueError("Input list cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if not data:
        raise ValueError("Input list cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if not data:
        raise ValueError("Input list cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if not data:
        raise ValueError("Input list cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if not data:
        raise ValueError("Input list cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")
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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if not data:
        raise ValueError("Input list cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")
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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if len(data) < 4: # IQR requires at least 4 points to reliably calculate Q1 and Q3
        raise ValueError("Input list must contain at least 4 elements to calculate IQR.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if not data:
        raise ValueError("Input list cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")
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
    if not isinstance(data, list):
        raise TypeError("Input 'data' must be a list.")
    if not data:
        raise ValueError("Input list cannot be empty.")
    if not all(isinstance(item, (int, float)) for item in data):
        raise TypeError("All elements in 'data' must be numeric (int or float).")

    mean_value = calculate_mean(data)
    return sum([(x - mean_value) ** 2 for x in data])


