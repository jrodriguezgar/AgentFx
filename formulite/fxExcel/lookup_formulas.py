"""
Excel Lookup and Reference Functions Module.

This module provides Excel-compatible lookup and reference functions for FormuLite.
Functions include:
- CHOOSE, CHOOSECOLS, CHOOSEROWS: Selection functions
- DROP, TAKE: Array manipulation
- FILTER: Filter data by criteria
- HLOOKUP, VLOOKUP, XLOOKUP: Lookup functions
- HSTACK, VSTACK: Array stacking
- INDEX: Index-based lookup
- LOOKUP: Vector lookup
- MATCH, XMATCH: Position matching
- SORT, SORTBY: Sorting functions
- TOCOL, TOROW: Array reshaping
- TRIMRANGE: Trim blank edges from arrays
- UNIQUE: Extract unique values
- WRAPCOLS, WRAPROWS: Array wrapping

All functions follow Excel naming conventions and behavior.
"""

from typing import List, Union, Any, Optional, Callable
import numpy as np


# ============================================================================
# SELECTION FUNCTIONS
# ============================================================================

def CHOOSE(index_num: int, *values: Any) -> Any:
    """
    Choose a value from a list of values based on index.
    
    Args:
        index_num: Index number (1-based) of the value to choose.
        *values: List of values to choose from.
    
    Returns:
        Any: Value at the specified index.
    
    Raises:
        ValueError: If index is out of range.
    
    Example:
        >>> CHOOSE(2, "red", "blue", "green")
        'blue'
        >>> CHOOSE(1, 10, 20, 30)
        10
    
    Cost: O(1)
    """
    if index_num < 1 or index_num > len(values):
        raise ValueError(f"Index {index_num} out of range (1-{len(values)})")
    return values[index_num - 1]


def CHOOSECOLS(array: List[List[Any]], *col_nums: int) -> List[List[Any]]:
    """
    Return specified columns from an array.
    
    Args:
        array: The array from which to select columns.
        *col_nums: Column numbers to select (1-based, negative from end).
    
    Returns:
        List[List[Any]]: Array with only the specified columns.
    
    Example:
        >>> data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> CHOOSECOLS(data, 1, 3)
        [[1, 3], [4, 6], [7, 9]]
    
    Cost: O(r * c) where r=rows, c=selected columns
    """
    arr = np.array(array)
    selected_cols = []
    
    for col_num in col_nums:
        idx = col_num - 1 if col_num > 0 else col_num
        selected_cols.append(arr[:, idx])
    
    return np.column_stack(selected_cols).tolist()


def CHOOSEROWS(array: List[List[Any]], *row_nums: int) -> List[List[Any]]:
    """
    Return specified rows from an array.
    
    Args:
        array: The array from which to select rows.
        *row_nums: Row numbers to select (1-based, negative from end).
    
    Returns:
        List[List[Any]]: Array with only the specified rows.
    
    Example:
        >>> data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> CHOOSEROWS(data, 1, 3)
        [[1, 2, 3], [7, 8, 9]]
    
    Cost: O(r * c) where r=selected rows, c=columns
    """
    arr = np.array(array)
    selected_rows = []
    
    for row_num in row_nums:
        idx = row_num - 1 if row_num > 0 else row_num
        selected_rows.append(arr[idx])
    
    return np.array(selected_rows).tolist()


# ============================================================================
# ARRAY MANIPULATION FUNCTIONS
# ============================================================================

def DROP(array: List[List[Any]], rows: int = 0, columns: int = 0) -> List[List[Any]]:
    """
    Exclude a specified number of rows or columns from start or end of array.
    
    Args:
        array: The array to process.
        rows: Number of rows to drop (positive from start, negative from end).
        columns: Number of columns to drop (positive from start, negative from end).
    
    Returns:
        List[List[Any]]: Array with specified rows/columns removed.
    
    Example:
        >>> data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> DROP(data, 1, 1)
        [[5, 6], [8, 9]]
    
    Cost: O(r * c)
    """
    arr = np.array(array)
    
    if rows > 0:
        arr = arr[rows:]
    elif rows < 0:
        arr = arr[:rows]
    
    if columns > 0:
        arr = arr[:, columns:]
    elif columns < 0:
        arr = arr[:, :columns]
    
    return arr.tolist()


def TAKE(array: List[List[Any]], rows: int = None, columns: int = None) -> List[List[Any]]:
    """
    Return a specified number of contiguous rows or columns from start or end of array.
    
    Args:
        array: The array to process.
        rows: Number of rows to take (positive from start, negative from end).
        columns: Number of columns to take (positive from start, negative from end).
    
    Returns:
        List[List[Any]]: Array with specified rows/columns.
    
    Example:
        >>> data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> TAKE(data, 2, 2)
        [[1, 2], [4, 5]]
    
    Cost: O(r * c)
    """
    arr = np.array(array)
    
    if rows is not None:
        if rows > 0:
            arr = arr[:rows]
        else:
            arr = arr[rows:]
    
    if columns is not None:
        if columns > 0:
            arr = arr[:, :columns]
        else:
            arr = arr[:, columns:]
    
    return arr.tolist()


# ============================================================================
# FILTER FUNCTION
# ============================================================================

def FILTER(array: List[List[Any]], include: List[bool], 
           if_empty: Any = None) -> Union[List[List[Any]], Any]:
    """
    Filter a range of data based on criteria.
    
    Args:
        array: The array to filter.
        include: Boolean array indicating which rows to include.
        if_empty: Value to return if no rows match.
    
    Returns:
        Union[List[List[Any]], Any]: Filtered array or if_empty value.
    
    Example:
        >>> data = [[1, "A"], [2, "B"], [3, "C"]]
        >>> FILTER(data, [True, False, True])
        [[1, 'A'], [3, 'C']]
    
    Cost: O(r * c)
    """
    arr = np.array(array)
    include_arr = np.array(include)
    
    result = arr[include_arr]
    
    if len(result) == 0:
        return if_empty
    
    return result.tolist()


# ============================================================================
# LOOKUP FUNCTIONS
# ============================================================================

def HLOOKUP(lookup_value: Any, table_array: List[List[Any]], 
            row_index_num: int, range_lookup: bool = True) -> Any:
    """
    Search in the top row of an array and return value from specified row.
    
    Args:
        lookup_value: Value to search for in first row.
        table_array: Array to search.
        row_index_num: Row number to return value from (1-based).
        range_lookup: True for approximate match, False for exact match.
    
    Returns:
        Any: Value from the specified row.
    
    Raises:
        ValueError: If value not found (exact match) or index out of range.
    
    Example:
        >>> table = [["A", "B", "C"], [1, 2, 3], [10, 20, 30]]
        >>> HLOOKUP("B", table, 2)
        2
    
    Cost: O(c) where c=columns
    """
    arr = np.array(table_array)
    first_row = arr[0]
    
    if row_index_num < 1 or row_index_num > len(arr):
        raise ValueError(f"Row index {row_index_num} out of range")
    
    if range_lookup:
        idx = np.searchsorted(first_row, lookup_value, side='right') - 1
        if idx < 0:
            raise ValueError(f"Value {lookup_value} not found")
    else:
        try:
            idx = list(first_row).index(lookup_value)
        except ValueError:
            raise ValueError(f"Value {lookup_value} not found")
    
    return arr[row_index_num - 1, idx]


def VLOOKUP(lookup_value: Any, table_array: List[List[Any]], 
            col_index_num: int, range_lookup: bool = True) -> Any:
    """
    Search in the first column of an array and return value from specified column.
    
    Args:
        lookup_value: Value to search for in first column.
        table_array: Array to search.
        col_index_num: Column number to return value from (1-based).
        range_lookup: True for approximate match, False for exact match.
    
    Returns:
        Any: Value from the specified column.
    
    Raises:
        ValueError: If value not found (exact match) or index out of range.
    
    Example:
        >>> table = [["A", 1, 10], ["B", 2, 20], ["C", 3, 30]]
        >>> VLOOKUP("B", table, 2)
        2
    
    Cost: O(r) where r=rows
    """
    arr = np.array(table_array)
    first_col = arr[:, 0]
    
    if col_index_num < 1 or col_index_num > arr.shape[1]:
        raise ValueError(f"Column index {col_index_num} out of range")
    
    if range_lookup:
        idx = np.searchsorted(first_col, lookup_value, side='right') - 1
        if idx < 0:
            raise ValueError(f"Value {lookup_value} not found")
    else:
        try:
            idx = list(first_col).index(lookup_value)
        except ValueError:
            raise ValueError(f"Value {lookup_value} not found")
    
    return arr[idx, col_index_num - 1]


def XLOOKUP(lookup_value: Any, lookup_array: List[Any], 
            return_array: List[Any], if_not_found: Any = "#N/A",
            match_mode: int = 0, search_mode: int = 1) -> Any:
    """
    Search a range or array and return corresponding item from second range/array.
    
    Args:
        lookup_value: Value to search for.
        lookup_array: Array to search.
        return_array: Array of values to return.
        if_not_found: Value to return if no match found.
        match_mode: 0=exact, -1=exact or next smaller, 1=exact or next larger, 2=wildcard.
        search_mode: 1=first to last, -1=last to first, 2=binary ascending, -2=binary descending.
    
    Returns:
        Any: Corresponding value from return_array.
    
    Example:
        >>> XLOOKUP("B", ["A", "B", "C"], [10, 20, 30])
        20
    
    Cost: O(n) for linear search, O(log n) for binary
    """
    lookup = np.array(lookup_array)
    returns = np.array(return_array)
    
    if search_mode in [2, -2]:
        idx = np.searchsorted(lookup, lookup_value)
        if idx < len(lookup) and lookup[idx] == lookup_value:
            return returns[idx]
    else:
        try:
            if search_mode == -1:
                idx = len(lookup) - 1 - list(reversed(lookup.tolist())).index(lookup_value)
            else:
                idx = lookup.tolist().index(lookup_value)
            return returns[idx]
        except ValueError:
            pass
    
    return if_not_found


# ============================================================================
# INDEX AND MATCH FUNCTIONS
# ============================================================================

def INDEX(array: List[List[Any]], row_num: int = 0, 
          column_num: int = 0) -> Union[Any, List[Any]]:
    """
    Use an index to choose a value from a reference or array.
    
    Args:
        array: The array to index.
        row_num: Row number (1-based, 0 for all rows).
        column_num: Column number (1-based, 0 for all columns).
    
    Returns:
        Union[Any, List[Any]]: Value at position or entire row/column.
    
    Example:
        >>> data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        >>> INDEX(data, 2, 3)
        6
    
    Cost: O(1) for single value, O(n) for row/column
    """
    arr = np.array(array)
    
    if row_num == 0 and column_num == 0:
        return arr.tolist()
    elif row_num == 0:
        return arr[:, column_num - 1].tolist()
    elif column_num == 0:
        return arr[row_num - 1].tolist()
    else:
        return arr[row_num - 1, column_num - 1]


def MATCH(lookup_value: Any, lookup_array: List[Any], 
          match_type: int = 1) -> int:
    """
    Return the relative position of an item in an array.
    
    Args:
        lookup_value: Value to search for.
        lookup_array: Array to search.
        match_type: 1=largest value <=, 0=exact match, -1=smallest value >=.
    
    Returns:
        int: Position (1-based) of the match.
    
    Raises:
        ValueError: If no match found.
    
    Example:
        >>> MATCH("B", ["A", "B", "C"])
        2
    
    Cost: O(n) for linear search, O(log n) for sorted
    """
    arr = np.array(lookup_array)
    
    if match_type == 0:
        try:
            return arr.tolist().index(lookup_value) + 1
        except ValueError:
            raise ValueError(f"Value {lookup_value} not found")
    elif match_type == 1:
        idx = np.searchsorted(arr, lookup_value, side='right') - 1
        if idx < 0:
            raise ValueError(f"No value <= {lookup_value}")
        return idx + 1
    else:
        idx = np.searchsorted(arr[::-1], lookup_value, side='left')
        if idx >= len(arr):
            raise ValueError(f"No value >= {lookup_value}")
        return len(arr) - idx


def XMATCH(lookup_value: Any, lookup_array: List[Any],
           match_mode: int = 0, search_mode: int = 1) -> int:
    """
    Return the relative position of an item in an array.
    
    Args:
        lookup_value: Value to search for.
        lookup_array: Array to search.
        match_mode: 0=exact, -1=exact or next smaller, 1=exact or next larger, 2=wildcard.
        search_mode: 1=first to last, -1=last to first, 2=binary ascending, -2=binary descending.
    
    Returns:
        int: Position (1-based) of the match.
    
    Raises:
        ValueError: If no match found.
    
    Example:
        >>> XMATCH("B", ["A", "B", "C"])
        2
    
    Cost: O(n) for linear, O(log n) for binary
    """
    arr = np.array(lookup_array)
    
    try:
        if search_mode == -1:
            idx = len(arr) - 1 - list(reversed(arr.tolist())).index(lookup_value)
        else:
            idx = arr.tolist().index(lookup_value)
        return idx + 1
    except ValueError:
        raise ValueError(f"Value {lookup_value} not found")


def LOOKUP(lookup_value: Any, lookup_vector: List[Any], 
           result_vector: Optional[List[Any]] = None) -> Any:
    """
    Look up values in a vector or array.
    
    Args:
        lookup_value: Value to search for.
        lookup_vector: Sorted array to search.
        result_vector: Optional array of values to return.
    
    Returns:
        Any: Corresponding value.
    
    Example:
        >>> LOOKUP(5, [1, 3, 5, 7], ["A", "B", "C", "D"])
        'C'
    
    Cost: O(log n)
    """
    lookup = np.array(lookup_vector)
    
    if result_vector is None:
        result_vector = lookup_vector
    
    result = np.array(result_vector)
    idx = np.searchsorted(lookup, lookup_value, side='right') - 1
    
    if idx < 0:
        idx = 0
    
    return result[idx]


# ============================================================================
# SORTING FUNCTIONS
# ============================================================================

def SORT(array: List[List[Any]], sort_index: int = 1, 
         sort_order: int = 1, by_col: bool = False) -> List[List[Any]]:
    """
    Sort the contents of a range or array.
    
    Args:
        array: The array to sort.
        sort_index: Row or column index to sort by (1-based).
        sort_order: 1 for ascending, -1 for descending.
        by_col: False to sort by row, True to sort by column.
    
    Returns:
        List[List[Any]]: Sorted array.
    
    Example:
        >>> data = [[3, "C"], [1, "A"], [2, "B"]]
        >>> SORT(data)
        [[1, 'A'], [2, 'B'], [3, 'C']]
    
    Cost: O(n log n)
    """
    arr = np.array(array)
    
    if by_col:
        idx = arr[sort_index - 1].argsort()
        if sort_order == -1:
            idx = idx[::-1]
        return arr[:, idx].tolist()
    else:
        idx = arr[:, sort_index - 1].argsort()
        if sort_order == -1:
            idx = idx[::-1]
        return arr[idx].tolist()


def SORTBY(array: List[List[Any]], by_array1: List[Any], 
           sort_order1: int = 1, *args) -> List[List[Any]]:
    """
    Sort the contents of a range based on corresponding values in other ranges.
    
    Args:
        array: The array to sort.
        by_array1: First array to sort by.
        sort_order1: 1 for ascending, -1 for descending.
        *args: Additional by_array, sort_order pairs.
    
    Returns:
        List[List[Any]]: Sorted array.
    
    Example:
        >>> data = [[1, "A"], [3, "C"], [2, "B"]]
        >>> by = [3, 1, 2]
        >>> SORTBY(data, by)
        [[3, 'C'], [2, 'B'], [1, 'A']]
    
    Cost: O(n log n)
    """
    arr = np.array(array)
    by = np.array(by_array1)
    
    idx = by.argsort()
    if sort_order1 == -1:
        idx = idx[::-1]
    
    return arr[idx].tolist()


# ============================================================================
# ARRAY STACKING FUNCTIONS
# ============================================================================

def HSTACK(*arrays: List[List[Any]]) -> List[List[Any]]:
    """
    Append arrays horizontally and in sequence to return a larger array.
    
    Args:
        *arrays: Arrays to stack horizontally.
    
    Returns:
        List[List[Any]]: Horizontally stacked array.
    
    Example:
        >>> a1 = [[1], [2], [3]]
        >>> a2 = [[4], [5], [6]]
        >>> HSTACK(a1, a2)
        [[1, 4], [2, 5], [3, 6]]
    
    Cost: O(r * c)
    """
    np_arrays = [np.array(arr) for arr in arrays]
    return np.hstack(np_arrays).tolist()


def VSTACK(*arrays: List[List[Any]]) -> List[List[Any]]:
    """
    Append arrays vertically and in sequence to return a larger array.
    
    Args:
        *arrays: Arrays to stack vertically.
    
    Returns:
        List[List[Any]]: Vertically stacked array.
    
    Example:
        >>> a1 = [[1, 2, 3]]
        >>> a2 = [[4, 5, 6]]
        >>> VSTACK(a1, a2)
        [[1, 2, 3], [4, 5, 6]]
    
    Cost: O(r * c)
    """
    np_arrays = [np.array(arr) for arr in arrays]
    return np.vstack(np_arrays).tolist()


# ============================================================================
# ARRAY RESHAPING FUNCTIONS
# ============================================================================

def TOCOL(array: List[List[Any]], ignore: int = 0, 
          scan_by_column: bool = False) -> List[List[Any]]:
    """
    Return the array as a single column.
    
    Args:
        array: The array to transform.
        ignore: 0=keep all, 1=ignore blanks, 2=ignore errors, 3=ignore both.
        scan_by_column: False for row-wise, True for column-wise.
    
    Returns:
        List[List[Any]]: Single column array.
    
    Example:
        >>> data = [[1, 2], [3, 4]]
        >>> TOCOL(data)
        [[1], [2], [3], [4]]
    
    Cost: O(r * c)
    """
    arr = np.array(array)
    
    if scan_by_column:
        flat = arr.T.flatten()
    else:
        flat = arr.flatten()
    
    result = [[x] for x in flat]
    
    if ignore > 0:
        result = [x for x in result if x[0] is not None and x[0] != ""]
    
    return result


def TOROW(array: List[List[Any]], ignore: int = 0, 
          scan_by_column: bool = False) -> List[List[Any]]:
    """
    Return the array as a single row.
    
    Args:
        array: The array to transform.
        ignore: 0=keep all, 1=ignore blanks, 2=ignore errors, 3=ignore both.
        scan_by_column: False for row-wise, True for column-wise.
    
    Returns:
        List[List[Any]]: Single row array.
    
    Example:
        >>> data = [[1, 2], [3, 4]]
        >>> TOROW(data)
        [[1, 2, 3, 4]]
    
    Cost: O(r * c)
    """
    arr = np.array(array)
    
    if scan_by_column:
        flat = arr.T.flatten()
    else:
        flat = arr.flatten()
    
    result = [flat.tolist()]
    
    return result


# ============================================================================
# ARRAY WRAPPING FUNCTIONS
# ============================================================================

def WRAPCOLS(vector: List[Any], wrap_count: int, 
             pad_with: Any = None) -> List[List[Any]]:
    """
    Wrap the provided row or column of values by columns after specified number of elements.
    
    Args:
        vector: The vector to wrap.
        wrap_count: Number of values per column.
        pad_with: Value to pad incomplete columns.
    
    Returns:
        List[List[Any]]: Wrapped array.
    
    Example:
        >>> WRAPCOLS([1, 2, 3, 4, 5, 6], 2)
        [[1, 3, 5], [2, 4, 6]]
    
    Cost: O(n)
    """
    vec = np.array(vector).flatten()
    rows = wrap_count
    cols = int(np.ceil(len(vec) / rows))
    
    padded = np.full(rows * cols, pad_with)
    padded[:len(vec)] = vec
    
    return padded.reshape(rows, cols).tolist()


def WRAPROWS(vector: List[Any], wrap_count: int, 
             pad_with: Any = None) -> List[List[Any]]:
    """
    Wrap the provided row or column of values by rows after specified number of elements.
    
    Args:
        vector: The vector to wrap.
        wrap_count: Number of values per row.
        pad_with: Value to pad incomplete rows.
    
    Returns:
        List[List[Any]]: Wrapped array.
    
    Example:
        >>> WRAPROWS([1, 2, 3, 4, 5, 6], 3)
        [[1, 2, 3], [4, 5, 6]]
    
    Cost: O(n)
    """
    vec = np.array(vector).flatten()
    cols = wrap_count
    rows = int(np.ceil(len(vec) / cols))
    
    padded = np.full(rows * cols, pad_with)
    padded[:len(vec)] = vec
    
    return padded.reshape(rows, cols).tolist()


# ============================================================================
# UNIQUE FUNCTION
# ============================================================================

def UNIQUE(array: List[Any], by_col: bool = False, 
           exactly_once: bool = False) -> List[Any]:
    """
    Return a list of unique values from a list or range.
    
    Args:
        array: The array to process.
        by_col: False for unique rows, True for unique columns.
        exactly_once: False for all unique, True for values appearing once.
    
    Returns:
        List[Any]: Array of unique values.
    
    Example:
        >>> UNIQUE([1, 2, 2, 3, 1, 4])
        [1, 2, 3, 4]
    
    Cost: O(n log n)
    """
    arr = np.array(array)
    
    if arr.ndim == 1:
        unique_vals, counts = np.unique(arr, return_counts=True)
        if exactly_once:
            return unique_vals[counts == 1].tolist()
        return unique_vals.tolist()
    else:
        if by_col:
            arr = arr.T
        unique_rows = np.unique(arr, axis=0)
        return unique_rows.tolist()


# ============================================================================
# TRIM RANGE FUNCTION
# ============================================================================

def TRIMRANGE(array: List[List[Any]]) -> List[List[Any]]:
    """
    Trim blank rows and columns from the edges of a range or array.
    
    Examines from the edges of a range or array until it finds a cell (or value)
    that is not blank, then excludes those blank rows or columns.
    
    Args:
        array: The array to trim.
    
    Returns:
        List[List[Any]]: Array with blank rows/columns removed from edges.
    
    Example:
        >>> data = [[None, None, None], [None, 1, 2], [None, 3, 4], [None, None, None]]
        >>> TRIMRANGE(data)
        [[1, 2], [3, 4]]
    
    Cost: O(r * c) where r=rows, c=columns
    """
    arr = np.array(array)
    
    # Function to check if a row/column is all blank
    def is_blank(values):
        return all(v is None or v == '' or (isinstance(v, str) and v.strip() == '') 
                   or (isinstance(v, float) and np.isnan(v)) for v in values)
    
    # Find first and last non-blank rows
    first_row = 0
    last_row = arr.shape[0] - 1
    
    while first_row <= last_row and is_blank(arr[first_row]):
        first_row += 1
    
    while last_row >= first_row and is_blank(arr[last_row]):
        last_row -= 1
    
    if first_row > last_row:
        return [[]]
    
    # Trim rows
    arr = arr[first_row:last_row + 1]
    
    # Find first and last non-blank columns
    first_col = 0
    last_col = arr.shape[1] - 1
    
    while first_col <= last_col and is_blank(arr[:, first_col]):
        first_col += 1
    
    while last_col >= first_col and is_blank(arr[:, last_col]):
        last_col -= 1
    
    if first_col > last_col:
        return [[]]
    
    # Trim columns
    arr = arr[:, first_col:last_col + 1]
    
    return arr.tolist()
