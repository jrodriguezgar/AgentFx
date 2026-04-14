"""
Excel Logic Functions Module.

This module provides Excel-compatible logical and conditional functions for FormuLite.
Functions include:
- Basic Logic: AND, OR, NOT, XOR, TRUE, FALSE
- Conditionals: IF, IFS, IFERROR, IFNA
- Lambda Functions: LAMBDA, LET, BYCOL, BYROW, REDUCE, SCAN

All functions follow Excel naming conventions and behavior.
"""

from typing import Any, Callable, List, Optional, Union

from formulite.fxPython.py_logic import (
    and_all as _core_and,
    if_then_else as _core_if,
    if_error as _core_if_error,
    ifs as _core_ifs,
    not_value as _core_not,
    or_any as _core_or,
    switch_case as _core_switch,
    xor_all as _core_xor,
)


# ============================================================================
# BASIC LOGIC FUNCTIONS
# ============================================================================

def AND(*args: Any) -> bool:
    """
    Return TRUE if all arguments are TRUE.
    
    Args:
        *args: Logical values to evaluate.
    
    Returns:
        bool: True if all arguments are True, False otherwise.
    
    Example:
        >>> AND(True, True, True)
        True
        >>> AND(True, False, True)
        False
    
    Cost: O(n) where n is the number of arguments
    """
    return _core_and(*args)


def OR(*args: Any) -> bool:
    """
    Return TRUE if any argument is TRUE.
    
    Args:
        *args: Logical values to evaluate.
    
    Returns:
        bool: True if any argument is True, False otherwise.
    
    Example:
        >>> OR(False, True, False)
        True
        >>> OR(False, False, False)
        False
    
    Cost: O(n) where n is the number of arguments
    """
    return _core_or(*args)


def NOT(value: Any) -> bool:
    """
    Reverse the logical value of its argument.
    
    Args:
        value: Logical value to invert.
    
    Returns:
        bool: Inverted logical value.
    
    Example:
        >>> NOT(True)
        False
        >>> NOT(False)
        True
    
    Cost: O(1)
    """
    return _core_not(value)


def XOR(*args: Any) -> bool:
    """
    Return a logical exclusive OR of all arguments.
    
    Args:
        *args: Logical values to evaluate.
    
    Returns:
        bool: True if an odd number of arguments are True, False otherwise.
    
    Example:
        >>> XOR(True, False, False)
        True
        >>> XOR(True, True, False)
        False
    
    Cost: O(n) where n is the number of arguments
    """
    return _core_xor(*args)


def TRUE() -> bool:
    """
    Return the logical value TRUE.
    
    Returns:
        bool: True
    
    Example:
        >>> TRUE()
        True
    
    Cost: O(1)
    """
    return True


def FALSE() -> bool:
    """
    Return the logical value FALSE.
    
    Returns:
        bool: False
    
    Example:
        >>> FALSE()
        False
    
    Cost: O(1)
    """
    return False


# ============================================================================
# CONDITIONAL FUNCTIONS
# ============================================================================

def IF(logical_test: Any, value_if_true: Any, value_if_false: Any = None) -> Any:
    """
    Perform a logical test and return one value for TRUE and another for FALSE.
    
    Args:
        logical_test: Condition to evaluate.
        value_if_true: Value to return if condition is True.
        value_if_false: Value to return if condition is False (optional).
    
    Returns:
        Any: value_if_true if test is True, otherwise value_if_false.
    
    Example:
        >>> IF(10 > 5, "Yes", "No")
        'Yes'
        >>> IF(3 < 2, "Yes", "No")
        'No'
    
    Cost: O(1)
    """
    return _core_if(logical_test, value_if_true, value_if_false)


def IFS(*args: Any) -> Any:
    """
    Check multiple conditions and return the value corresponding to the first TRUE condition.
    
    Args:
        *args: Pairs of condition and value (cond1, val1, cond2, val2, ..., default).
    
    Returns:
        Any: Value corresponding to the first True condition, or default value.
    
    Raises:
        ValueError: If number of arguments is even (missing default value).
    
    Example:
        >>> IFS(False, "A", True, "B", False, "C", "Default")
        'B'
        >>> IFS(False, "A", False, "B", "Default")
        'Default'
    
    Cost: O(n) where n is the number of condition pairs
    """
    return _core_ifs(*args)


def IFERROR(value: Union[Callable, Any], value_if_error: Any) -> Any:
    """
    Return a value if an expression results in an error, otherwise return the expression result.
    
    Args:
        value: Expression to evaluate (callable) or direct value.
        value_if_error: Value to return if error occurs.
    
    Returns:
        Any: Result of expression or value_if_error if error occurs.
    
    Example:
        >>> IFERROR(lambda: 10 / 2, "Error")
        5.0
        >>> IFERROR(lambda: 10 / 0, "Error")
        'Error'
    
    Cost: O(1)
    """
    return _core_if_error(value, value_if_error)


def IFNA(value: Union[Callable, Any], value_if_na: Any) -> Any:
    """
    Return a value if the expression results in #N/A or None, otherwise return the expression result.
    
    Args:
        value: Expression to evaluate (callable) or direct value.
        value_if_na: Value to return if result is None or #N/A.
    
    Returns:
        Any: Result of expression or value_if_na if result is None.
    
    Example:
        >>> IFNA(lambda: None, "N/A")
        'N/A'
        >>> IFNA(lambda: 42, "N/A")
        42
    
    Cost: O(1)
    """
    result = value() if callable(value) else value
    return value_if_na if result is None or result == "#N/A" else result


# ============================================================================
# LAMBDA FUNCTIONS
# ============================================================================

def LAMBDA(*args: Any, expression: Optional[Callable] = None) -> Callable:
    """
    Create a reusable lambda function with named parameters.
    
    Args:
        *args: Parameter names for the lambda.
        expression: Lambda expression as a callable function.
    
    Returns:
        Callable: Lambda function that can be called with specified arguments.
    
    Example:
        >>> add = LAMBDA(expression=lambda x, y: x + y)
        >>> add(5, 3)
        8
    
    Cost: O(1)
    """
    if expression is None:
        raise ValueError("LAMBDA requires an 'expression' argument")
    return lambda *values: expression(*values)


def LET(**kwargs: Any) -> Any:
    """
    Assign names to calculation results and evaluate a final expression.
    
    Args:
        **kwargs: Name-value pairs where the last pair must be 'expression' with the function to evaluate.
    
    Returns:
        Any: Result of the final expression using the assigned names.
    
    Raises:
        ValueError: If 'expression' argument is missing.
    
    Example:
        >>> LET(x=5, y=3, expression=lambda x, y: x + y)
        8
    
    Cost: O(1)
    """
    if 'expression' not in kwargs:
        raise ValueError("LET requires an 'expression' argument")
    
    expression = kwargs.pop('expression')
    return expression(**kwargs)


def BYCOL(array: List[List[Any]], lambda_func: Callable[[List[Any]], Any]) -> List[Any]:
    """
    Apply a LAMBDA to each column and return an array of results.
    
    Args:
        array: List of lists (matrix) where each sublist is a row.
        lambda_func: Lambda function that takes a list (column) as argument.
    
    Returns:
        List[Any]: Results of applying lambda_func to each column.
    
    Example:
        >>> BYCOL([[1, 2], [3, 4]], lambda col: sum(col))
        [4, 6]
    
    Cost: O(r * c) where r is rows and c is columns
    """
    if not array or not array[0]:
        return []
    
    num_rows = len(array)
    num_cols = len(array[0])
    
    # Transpose matrix to work with columns
    columns = [[array[row][col] for row in range(num_rows)] for col in range(num_cols)]
    
    return [lambda_func(col) for col in columns]


def BYROW(array: List[List[Any]], lambda_func: Callable[[List[Any]], Any]) -> List[Any]:
    """
    Apply a LAMBDA to each row and return an array of results.
    
    Excel: BYROW / Spanish: BYROW
    
    Args:
        array: List of lists (matrix) where each sublist is a row.
        lambda_func: Lambda function that takes a list (row) as argument.
    
    Returns:
        List[Any]: Results of applying lambda_func to each row.
    
    Example:
        >>> BYROW([[1, 2, 3], [4, 5, 6]], lambda row: sum(row))
        [6, 15]
    
    Cost: O(r) where r is the number of rows
    """
    if not array:
        return []
    
    return [lambda_func(row) for row in array]


# ============================================================================
# ADVANCED LOGIC FUNCTIONS
# ============================================================================

def SWITCH(expression: Any, *args: Any) -> Any:
    """
    Evaluate an expression and return a value from a list based on matching values.
    
    Excel: SWITCH / Spanish: CAMBIAR
    
    Args:
        expression: The value to compare against.
        *args: Alternating value/result pairs, with optional default at the end.
              Format: value1, result1, value2, result2, ..., [default]
    
    Returns:
        Any: The result corresponding to the first matching value, or default.
    
    Raises:
        ValueError: If no match found and no default provided.
    
    Example:
        >>> SWITCH(2, 1, "one", 2, "two", 3, "three")
        'two'
        >>> SWITCH(5, 1, "one", 2, "two", "other")
        'other'
    
    Cost: O(n) where n is the number of value/result pairs
    """
    return _core_switch(expression, *args)


def MAP(*args) -> List[List[Any]]:
    """
    Return an array formed by mapping each value in arrays to a new value by applying a LAMBDA.
    
    Excel: MAP / Spanish: MAPEAR
    
    Args:
        *args: One or more arrays (matrices) followed by the lambda function.
               The last argument must be the lambda function.
    
    Returns:
        List[List[Any]]: New array with lambda_func applied to each set of values.
    
    Example:
        >>> MAP([[1, 2], [3, 4]], lambda x: x * 2)
        [[2, 4], [6, 8]]
        >>> MAP([[1, 2], [3, 4]], [[5, 6], [7, 8]], lambda x, y: x + y)
        [[6, 8], [10, 12]]
    
    Cost: O(r * c) where r is rows and c is columns
    """
    if not args or len(args) < 2:
        raise ValueError("MAP requires at least one array and a lambda function")
    
    # Last argument is the lambda function
    lambda_func = args[-1]
    arrays = args[:-1]
    
    if not callable(lambda_func):
        raise ValueError("Last argument must be a lambda function")
    
    if not arrays or not arrays[0]:
        return []
    
    # Get dimensions from first array
    num_rows = len(arrays[0])
    num_cols = len(arrays[0][0]) if num_rows > 0 else 0
    
    result = []
    for row_idx in range(num_rows):
        result_row = []
        for col_idx in range(num_cols):
            # Collect values from all arrays at this position
            values = [arr[row_idx][col_idx] for arr in arrays]
            
            # Apply lambda function
            if len(values) == 1:
                result_row.append(lambda_func(values[0]))
            else:
                result_row.append(lambda_func(*values))
        
        result.append(result_row)
    
    return result


def MAKEARRAY(rows: int, cols: int, lambda_func: Callable[[int, int], Any]) -> List[List[Any]]:
    """
    Return a calculated array of a specified row and column size by applying a LAMBDA.
    
    Excel: MAKEARRAY / Spanish: ARCHIVOMAKEARRAY
    
    Args:
        rows: Number of rows in the array.
        cols: Number of columns in the array.
        lambda_func: Lambda function that takes (row_index, col_index) and returns a value.
                    Indices are 1-based (Excel convention).
    
    Returns:
        List[List[Any]]: Generated array with values from lambda_func.
    
    Example:
        >>> MAKEARRAY(2, 3, lambda r, c: r * c)
        [[1, 2, 3], [2, 4, 6]]
        >>> MAKEARRAY(3, 2, lambda r, c: r + c)
        [[2, 3], [3, 4], [4, 5]]
    
    Cost: O(r * c) where r is rows and c is columns
    """
    if rows <= 0 or cols <= 0:
        return []
    
    result = []
    for row_idx in range(1, rows + 1):
        result_row = []
        for col_idx in range(1, cols + 1):
            result_row.append(lambda_func(row_idx, col_idx))
        result.append(result_row)
    
    return result


def REDUCE(initial_value: Any, array: List[Any], lambda_func: Callable[[Any, Any], Any]) -> Any:
    """
    Reduce an array to an accumulated value by applying a LAMBDA to each value.

    Args:
        initial_value: The starting value for the accumulator.
        array: Array of values to reduce.
        lambda_func: Function taking (accumulator, current_value) and returning new accumulator.

    Returns:
        Any: The final accumulated value.

    Raises:
        ValueError: If lambda_func is not callable.

    Example:
        >>> REDUCE(0, [1, 2, 3, 4, 5], lambda acc, x: acc + x)
        15
        >>> REDUCE(1, [1, 2, 3, 4], lambda acc, x: acc * x)
        24

    Cost: O(n) where n is the number of elements
    """
    if not callable(lambda_func):
        raise ValueError("lambda_func must be a callable")

    accumulator = initial_value

    flat = []

    for item in array:

        if isinstance(item, list):

            for sub in item:
                flat.append(sub)
        else:
            flat.append(item)

    for value in flat:
        accumulator = lambda_func(accumulator, value)

    return accumulator


def SCAN(initial_value: Any, array: List[Any], lambda_func: Callable[[Any, Any], Any]) -> List[Any]:
    """
    Scan an array by applying a LAMBDA to each value, returning intermediate results.

    Args:
        initial_value: The starting value for the accumulator.
        array: Array of values to scan.
        lambda_func: Function taking (accumulator, current_value) and returning new accumulator.

    Returns:
        List[Any]: Array of each intermediate accumulated value.

    Raises:
        ValueError: If lambda_func is not callable.

    Example:
        >>> SCAN(0, [1, 2, 3, 4, 5], lambda acc, x: acc + x)
        [1, 3, 6, 10, 15]
        >>> SCAN(1, [2, 3, 4], lambda acc, x: acc * x)
        [2, 6, 24]

    Cost: O(n) where n is the number of elements
    """
    if not callable(lambda_func):
        raise ValueError("lambda_func must be a callable")

    accumulator = initial_value
    result = []

    flat = []

    for item in array:

        if isinstance(item, list):

            for sub in item:
                flat.append(sub)
        else:
            flat.append(item)

    for value in flat:
        accumulator = lambda_func(accumulator, value)
        result.append(accumulator)

    return result