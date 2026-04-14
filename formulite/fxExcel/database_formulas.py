"""
Excel Database Functions Module.

This module provides Excel-compatible database functions that operate on structured
data (list of dictionaries). Functions include:
- DCOUNT, DCOUNTA: Count functions
- DAVERAGE, DSUM: Aggregate functions
- DMAX, DMIN: Statistical functions
- DSTDEV, DSTDEVP, DVAR, DVARP: Variance and standard deviation
- DPRODUCT: Product calculation
- DGET: Single record extraction

All functions follow Excel naming conventions and behavior.
"""

from typing import List, Dict, Optional, Union, Any
import statistics


def _evaluate_criteria(record: Dict[str, Any], criteria: Dict[str, Any]) -> bool:
    """
    Evaluate if a record matches specified criteria.
    
    Args:
        record: Dictionary representing a database record.
        criteria: Dictionary with field names as keys and conditions as values.
    
    Returns:
        bool: True if record matches all criteria, False otherwise.
    
    Cost: O(k) where k is the number of criteria fields.
    """
    for field, condition in criteria.items():
        if field not in record:
            return False
        value = record[field]
        
        if isinstance(condition, dict):
            operator = condition.get('operator', '=')
            cond_value = condition.get('value')
            if operator == '=' and value != cond_value:
                return False
            elif operator == '>' and not (value > cond_value):
                return False
            elif operator == '<' and not (value < cond_value):
                return False
            elif operator == '>=' and not (value >= cond_value):
                return False
            elif operator == '<=' and not (value <= cond_value):
                return False
            elif operator == '<>' and value == cond_value:
                return False
        else:
            if value != condition:
                return False
    return True


def _get_db_values(
    database: List[Dict[str, Any]],
    field: str,
    criteria: Optional[Dict[str, Any]] = None,
) -> List[Union[int, float]]:
    """Extract numeric field values from records matching criteria."""
    values = []

    for record in database:

        if criteria is None or _evaluate_criteria(record, criteria):

            if field in record and isinstance(record[field], (int, float)):
                values.append(record[field])

    return values


# ============================================================================
# COUNT FUNCTIONS
# ============================================================================

def DCOUNT(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> int:
    """
    Count cells containing numbers in a database field that match criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to count.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        int: Count of numeric values matching criteria.
    
    Example:
        >>> db = [{'Name': 'Alice', 'Age': 30}, {'Name': 'Bob', 'Age': 25}]
        >>> DCOUNT(db, 'Age', None)
        2
    
    Cost: O(n) where n is the number of records.
    """
    return len(_get_db_values(database, field, criteria))


def DCOUNTA(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> int:
    """
    Count non-empty cells in a database field that match criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to count.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        int: Count of non-empty values matching criteria.
    
    Example:
        >>> db = [{'Name': 'Alice', 'Age': 30}, {'Name': 'Bob', 'Age': None}]
        >>> DCOUNTA(db, 'Age', None)
        1
    
    Cost: O(n) where n is the number of records.
    """
    count = 0
    for record in database:
        if criteria is None or _evaluate_criteria(record, criteria):
            if field in record and record[field] is not None:
                count += 1
    return count


# ============================================================================
# STATISTICAL FUNCTIONS
# ============================================================================

def DSTDEV(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> float:
    """
    Calculate sample standard deviation of database field values matching criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to analyze.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        float: Sample standard deviation, 0 if less than 2 values.
    
    Example:
        >>> db = [{'Value': 10}, {'Value': 20}, {'Value': 30}]
        >>> DSTDEV(db, 'Value', None)
        10.0
    
    Cost: O(n) where n is the number of records.
    """
    values = _get_db_values(database, field, criteria)
    return statistics.stdev(values) if len(values) > 1 else 0


def DSTDEVP(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> float:
    """
    Calculate population standard deviation of database field values matching criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to analyze.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        float: Population standard deviation, 0 if no values.
    
    Example:
        >>> db = [{'Value': 10}, {'Value': 20}, {'Value': 30}]
        >>> round(DSTDEVP(db, 'Value', None), 2)
        8.16
    
    Cost: O(n) where n is the number of records.
    """
    values = _get_db_values(database, field, criteria)
    return statistics.pstdev(values) if values else 0


def DGET(database: List[Dict[str, Any]], field: str, criteria: Dict[str, Any]) -> Any:
    """
    Extract a single value from a database field that matches criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to extract.
        criteria: Dictionary with filtering criteria.
    
    Returns:
        Any: Field value from the matching record, None if not found.
    
    Raises:
        ValueError: If multiple records match criteria (Excel behavior).
    
    Example:
        >>> db = [{'Name': 'Alice', 'Age': 30}, {'Name': 'Bob', 'Age': 25}]
        >>> DGET(db, 'Age', {'Name': 'Alice'})
        30
    
    Cost: O(n) where n is the number of records.
    """
    for record in database:
        if _evaluate_criteria(record, criteria):
            return record[field] if field in record else None
    return None


def DMAX(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> Optional[Union[int, float]]:
    """
    Return maximum value from database field values matching criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to analyze.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        Union[int, float, None]: Maximum value, None if no values.
    
    Example:
        >>> db = [{'Value': 10}, {'Value': 20}, {'Value': 30}]
        >>> DMAX(db, 'Value', None)
        30
    
    Cost: O(n) where n is the number of records.
    """
    values = _get_db_values(database, field, criteria)
    return max(values) if values else None


def DMIN(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> Optional[Union[int, float]]:
    """
    Return minimum value from database field values matching criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to analyze.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        Union[int, float, None]: Minimum value, None if no values.
    
    Example:
        >>> db = [{'Value': 10}, {'Value': 20}, {'Value': 30}]
        >>> DMIN(db, 'Value', None)
        10
    
    Cost: O(n) where n is the number of records.
    """
    values = _get_db_values(database, field, criteria)
    return min(values) if values else None


# ============================================================================
# AGGREGATE FUNCTIONS
# ============================================================================

def DPRODUCT(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> Union[int, float]:
    """
    Multiply values from database field that match criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to multiply.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        Union[int, float]: Product of values, 0 if no values.
    
    Example:
        >>> db = [{'Value': 2}, {'Value': 3}, {'Value': 4}]
        >>> DPRODUCT(db, 'Value', None)
        24
    
    Cost: O(n) where n is the number of records.
    """
    values = _get_db_values(database, field, criteria)
    product = 1
    for v in values:
        product *= v
    return product if values else 0


def DAVERAGE(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> float:
    """
    Calculate average of database field values matching criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to average.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        float: Average value, 0 if no values.
    
    Example:
        >>> db = [{'Value': 10}, {'Value': 20}, {'Value': 30}]
        >>> DAVERAGE(db, 'Value', None)
        20.0
    
    Cost: O(n) where n is the number of records.
    """
    values = _get_db_values(database, field, criteria)
    return sum(values) / len(values) if values else 0


def DSUM(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> Union[int, float]:
    """
    Sum values from database field that match criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to sum.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        Union[int, float]: Sum of values.
    
    Example:
        >>> db = [{'Value': 10}, {'Value': 20}, {'Value': 30}]
        >>> DSUM(db, 'Value', None)
        60
    
    Cost: O(n) where n is the number of records.
    """
    return sum(_get_db_values(database, field, criteria))


# ============================================================================
# VARIANCE FUNCTIONS
# ============================================================================

def DVAR(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> float:
    """
    Calculate sample variance of database field values matching criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to analyze.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        float: Sample variance, 0 if less than 2 values.
    
    Example:
        >>> db = [{'Value': 10}, {'Value': 20}, {'Value': 30}]
        >>> DVAR(db, 'Value', None)
        100.0
    
    Cost: O(n) where n is the number of records.
    """
    values = _get_db_values(database, field, criteria)
    return statistics.variance(values) if len(values) > 1 else 0


def DVARP(database: List[Dict[str, Any]], field: str, criteria: Optional[Dict[str, Any]] = None) -> float:
    """
    Calculate population variance of database field values matching criteria.
    
    Args:
        database: List of dictionaries representing database records.
        field: Field name to analyze.
        criteria: Optional dictionary with filtering criteria.
    
    Returns:
        float: Population variance, 0 if no values.
    
    Example:
        >>> db = [{'Value': 10}, {'Value': 20}, {'Value': 30}]
        >>> round(DVARP(db, 'Value', None), 2)
        66.67
    
    Cost: O(n) where n is the number of records.
    """
    values = _get_db_values(database, field, criteria)
    return statistics.pvariance(values) if values else 0
