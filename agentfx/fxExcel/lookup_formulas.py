"""
Excel Lookup and Reference Functions Module.

This module provides Excel-compatible lookup and reference functions for AgentFx.
Functions include:
- ADDRESS: Build a cell reference string
- CHOOSE, CHOOSECOLS, CHOOSEROWS: Selection functions
- COLUMN, COLUMNS: Column number / count
- DROP, TAKE: Array manipulation
- EXPAND: Expand an array to specified dimensions
- FILTER: Filter data by criteria
- HLOOKUP, VLOOKUP, XLOOKUP: Lookup functions
- HSTACK, VSTACK: Array stacking
- INDEX: Index-based lookup
- INDIRECT: Parse a cell-reference string
- LOOKUP: Vector lookup
- MATCH, XMATCH: Position matching
- OFFSET: Return a sub-range from a 2-D array
- ROW, ROWS: Row number / count
- SORT, SORTBY: Sorting functions
- TOCOL, TOROW: Array reshaping
- TRANSPOSE: Transpose a 2-D array
- TRIMRANGE: Trim blank edges from arrays
- UNIQUE: Extract unique values
- WRAPCOLS, WRAPROWS: Array wrapping

All functions follow Excel naming conventions and behavior.
"""

from typing import List, Union, Any, Optional, Tuple
import math
import re
from bisect import bisect_right, bisect_left

from agentfx.fxPython.py_operations import (
    choose_cols as _core_choose_cols,
    choose_rows as _core_choose_rows,
    drop_from_array as _core_drop,
    hlookup as _core_hlookup,
    hstack as _core_hstack,
    take_from_array as _core_take,
    tocol as _core_tocol,
    torow as _core_torow,
    vlookup as _core_vlookup,
    vstack as _core_vstack,
    wrap_rows as _core_wrap_rows,
    xmatch as _core_xmatch,
)


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
    return _core_choose_cols(array, *col_nums)


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
    return _core_choose_rows(array, *row_nums)


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
    return _core_drop(array, rows, columns)


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
    return _core_take(array, rows, columns)


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
    result = [list(array[i]) for i in range(len(array)) if include[i]]

    if not result:
        return if_empty

    return result


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
    return _core_hlookup(lookup_value, table_array, row_index_num,
                         approximate=range_lookup)


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
    return _core_vlookup(lookup_value, table_array, col_index_num,
                         approximate=range_lookup)


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
    lookup = list(lookup_array)
    returns = list(return_array)

    if search_mode in [2, -2]:
        idx = bisect_left(lookup, lookup_value)

        if idx < len(lookup) and lookup[idx] == lookup_value:
            return returns[idx]
    else:
        try:
            if search_mode == -1:
                idx = len(lookup) - 1 - list(reversed(lookup)).index(lookup_value)
            else:
                idx = lookup.index(lookup_value)

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
    if row_num == 0 and column_num == 0:
        return [list(row) for row in array]
    elif row_num == 0:
        return [row[column_num - 1] for row in array]
    elif column_num == 0:
        return list(array[row_num - 1])
    else:
        return array[row_num - 1][column_num - 1]


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
    items = list(lookup_array)

    if match_type == 0:
        try:
            return items.index(lookup_value) + 1
        except ValueError:
            raise ValueError(f"Value {lookup_value} not found")
    elif match_type == 1:
        idx = bisect_right(items, lookup_value) - 1

        if idx < 0:
            raise ValueError(f"No value <= {lookup_value}")

        return idx + 1
    else:
        rev = items[::-1]
        idx = bisect_left(rev, lookup_value)

        if idx >= len(items):
            raise ValueError(f"No value >= {lookup_value}")

        return len(items) - idx


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
    return _core_xmatch(lookup_value, lookup_array, match_mode, search_mode)


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
    lookup = list(lookup_vector)

    if result_vector is None:
        result_vector = lookup_vector

    result = list(result_vector)
    idx = bisect_right(lookup, lookup_value) - 1

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
    rows_data = [list(row) for row in array]
    num_cols = len(rows_data[0]) if rows_data else 0

    if by_col:
        key_row = rows_data[sort_index - 1]
        order = sorted(range(num_cols), key=lambda c: key_row[c],
                        reverse=(sort_order == -1))
        return [[row[c] for c in order] for row in rows_data]
    else:
        order = sorted(range(len(rows_data)),
                        key=lambda r: rows_data[r][sort_index - 1],
                        reverse=(sort_order == -1))
        return [rows_data[r] for r in order]


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
    rows_data = [list(row) for row in array]
    by = list(by_array1)

    order = sorted(range(len(rows_data)), key=lambda i: by[i],
                    reverse=(sort_order1 == -1))

    return [rows_data[i] for i in order]


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
    return _core_hstack(*arrays)


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
    return _core_vstack(*arrays)


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
    result = _core_tocol(array, scan_by_column=scan_by_column)

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
    return _core_torow(array, scan_by_column=scan_by_column)


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
    vec = list(vector) if not isinstance(vector[0], list) else [v for row in vector for v in row]
    rows = wrap_count
    cols = math.ceil(len(vec) / rows)

    padded = vec + [pad_with] * (rows * cols - len(vec))

    # Fill column-wise: result[r][c] = padded[c * rows + r]
    return [[padded[c * rows + r] for c in range(cols)] for r in range(rows)]


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
    vec = list(vector) if not isinstance(vector[0], list) else [v for row in vector for v in row]
    return _core_wrap_rows(vec, wrap_count, pad_with=pad_with)


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
    # Handle 1-D list
    if not array or not isinstance(array[0], list):
        items = list(array)

        if exactly_once:
            from collections import Counter
            counts = Counter(items)
            return [x for x in items if counts[x] == 1]

        seen: set = set()
        result: list = []

        for x in items:
            key = repr(x)

            if key not in seen:
                seen.add(key)
                result.append(x)

        return result
    else:
        if by_col:
            # Transpose, deduplicate rows, transpose back
            transposed = list(zip(*array))
            unique_cols = _unique_rows(transposed)
            return [list(row) for row in zip(*unique_cols)]
        else:
            return _unique_rows(array)


def _unique_rows(rows: List[List[Any]]) -> List[List[Any]]:
    """Return rows with unique content (preserving first occurrence order)."""
    seen: set = set()
    result: list = []

    for row in rows:
        key = tuple(row)

        if key not in seen:
            seen.add(key)
            result.append(list(row))

    return result


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
    num_rows = len(array)
    num_cols = len(array[0]) if num_rows else 0

    def is_blank(values):
        return all(
            v is None or v == '' or (isinstance(v, str) and v.strip() == '')
            or (isinstance(v, float) and math.isnan(v))
            for v in values
        )

    # Find first and last non-blank rows
    first_row = 0
    last_row = num_rows - 1

    while first_row <= last_row and is_blank(array[first_row]):
        first_row += 1

    while last_row >= first_row and is_blank(array[last_row]):
        last_row -= 1

    if first_row > last_row:
        return [[]]

    trimmed = [list(row) for row in array[first_row:last_row + 1]]

    # Find first and last non-blank columns
    first_col = 0
    last_col = num_cols - 1

    while first_col <= last_col and is_blank([row[first_col] for row in trimmed]):
        first_col += 1

    while last_col >= first_col and is_blank([row[last_col] for row in trimmed]):
        last_col -= 1

    if first_col > last_col:
        return [[]]

    return [row[first_col:last_col + 1] for row in trimmed]


# ============================================================================
# CELL REFERENCE AND ARRAY DIMENSION FUNCTIONS
# ============================================================================


def ADDRESS(row_num: int, column_num: int, abs_num: int = 1,
            a1: bool = True, sheet_text: str = "") -> str:
    """Build a cell-reference string from row/column numbers.

    Excel function: ADDRESS

    Args:
        row_num: Row number (1-based).
        column_num: Column number (1-based).
        abs_num: Reference type (1=absolute, 2=abs row/rel col,
                 3=rel row/abs col, 4=relative).
        a1: True for A1 style, False for R1C1 style.
        sheet_text: Optional sheet name prefix.

    Returns:
        str: Cell reference string.

    Raises:
        ValueError: If row_num or column_num < 1 or abs_num not in 1..4.

    Usage Example:
        >>> ADDRESS(1, 1)
        '$A$1'

    Cost: O(1)
    """

    if row_num < 1 or column_num < 1:
        raise ValueError("row_num and column_num must be >= 1")

    if abs_num not in (1, 2, 3, 4):
        raise ValueError("abs_num must be 1, 2, 3 or 4")

    prefix = f"'{sheet_text}'!" if sheet_text else ""

    if not a1:
        row_part = f"R{row_num}" if abs_num in (1, 2) else f"R[{row_num}]"
        col_part = f"C{column_num}" if abs_num in (1, 3) else f"C[{column_num}]"
        return f"{prefix}{row_part}{col_part}"

    # Convert column number to letter(s)
    col_str = ""
    n = column_num

    while n > 0:
        n, remainder = divmod(n - 1, 26)
        col_str = chr(65 + remainder) + col_str

    dollar_col = "$" if abs_num in (1, 3) else ""
    dollar_row = "$" if abs_num in (1, 2) else ""

    return f"{prefix}{dollar_col}{col_str}{dollar_row}{row_num}"


def INDIRECT(ref_text: str, a1: bool = True) -> Tuple[int, int]:
    """Parse a cell-reference string into (row, column) indices.

    Excel function: INDIRECT

    In a spreadsheet engine INDIRECT resolves a live reference; in AgentFx
    it parses the text and returns the 1-based (row, column) tuple.

    Args:
        ref_text: Cell reference string (e.g. "A1", "$B$3", "R2C3").
        a1: True for A1 style, False for R1C1 style.

    Returns:
        Tuple[int, int]: (row_number, column_number) both 1-based.

    Raises:
        ValueError: If ref_text cannot be parsed.

    Usage Example:
        >>> INDIRECT("B3")
        (3, 2)

    Cost: O(1)
    """
    clean = ref_text.strip().lstrip("'")

    # Remove optional sheet prefix
    if "!" in clean:
        clean = clean.split("!")[-1]

    clean = clean.replace("$", "")

    if a1:
        match = re.match(r"^([A-Za-z]+)(\d+)$", clean)

        if not match:
            raise ValueError(f"Cannot parse A1 reference: '{ref_text}'")

        col_str = match.group(1).upper()
        row = int(match.group(2))
        col = 0

        for ch in col_str:
            col = col * 26 + (ord(ch) - 64)

        return (row, col)

    # R1C1 style
    match = re.match(r"^R\[?(\d+)]?C\[?(\d+)]?$", clean, re.IGNORECASE)

    if not match:
        raise ValueError(f"Cannot parse R1C1 reference: '{ref_text}'")

    return (int(match.group(1)), int(match.group(2)))


def OFFSET(reference: List[List[Any]], rows: int, cols: int,
           height: Optional[int] = None,
           width: Optional[int] = None) -> List[List[Any]]:
    """Return a sub-range from a 2-D array offset from a starting cell.

    Excel function: OFFSET

    Args:
        reference: 2-D list used as the source range.
        rows: Row offset from top-left of reference.
        cols: Column offset from top-left of reference.
        height: Number of rows to return (default: same as reference).
        width: Number of columns to return (default: same as reference).

    Returns:
        List[List[Any]]: The extracted sub-range.

    Raises:
        IndexError: If the resulting range falls outside the array.

    Usage Example:
        >>> OFFSET([[1,2],[3,4],[5,6]], 1, 0, 2, 2)
        [[3, 4], [5, 6]]

    Cost: O(height * width)
    """
    num_rows = len(reference)
    num_cols = len(reference[0]) if num_rows else 0

    if height is None:
        height = num_rows

    if width is None:
        width = num_cols

    r_end = rows + height
    c_end = cols + width

    if (rows < 0 or cols < 0 or r_end > num_rows
            or c_end > num_cols):
        raise IndexError(
            f"OFFSET range ({rows}:{r_end}, {cols}:{c_end}) "
            f"exceeds array shape ({num_rows}, {num_cols})"
        )

    return [reference[r][cols:c_end] for r in range(rows, r_end)]


def ROW(reference: Optional[List[List[Any]]] = None,
        row_index: int = 1) -> int:
    """Return the row number of a reference.

    Excel function: ROW

    In AgentFx, *row_index* simulates the starting row of the range.

    Args:
        reference: Ignored in AgentFx (kept for API compat).
        row_index: The 1-based row number to return.

    Returns:
        int: Row number.

    Usage Example:
        >>> ROW(row_index=5)
        5

    Cost: O(1)
    """
    return row_index


def COLUMN(reference: Optional[List[List[Any]]] = None,
           col_index: int = 1) -> int:
    """Return the column number of a reference.

    Excel function: COLUMN

    Args:
        reference: Ignored in AgentFx (kept for API compat).
        col_index: The 1-based column number to return.

    Returns:
        int: Column number.

    Usage Example:
        >>> COLUMN(col_index=3)
        3

    Cost: O(1)
    """
    return col_index


def ROWS(array: List[List[Any]]) -> int:
    """Return the number of rows in an array or reference.

    Excel function: ROWS

    Args:
        array: 2-D list.

    Returns:
        int: Number of rows.

    Raises:
        TypeError: If array is not a list.

    Usage Example:
        >>> ROWS([[1,2],[3,4],[5,6]])
        3

    Cost: O(1)
    """

    if not isinstance(array, list):
        raise TypeError("array must be a list")

    return len(array)


def COLUMNS(array: List[List[Any]]) -> int:
    """Return the number of columns in an array or reference.

    Excel function: COLUMNS

    Args:
        array: 2-D list.

    Returns:
        int: Number of columns.

    Raises:
        TypeError: If array is not a list.

    Usage Example:
        >>> COLUMNS([[1,2,3],[4,5,6]])
        3

    Cost: O(1)
    """

    if not isinstance(array, list):
        raise TypeError("array must be a list")

    if len(array) == 0:
        return 0

    first = array[0]

    if isinstance(first, list):
        return len(first)

    return 1


def TRANSPOSE(array: List[List[Any]]) -> List[List[Any]]:
    """Transpose a 2-D array (swap rows and columns).

    Excel function: TRANSPOSE

    Args:
        array: 2-D list to transpose.

    Returns:
        List[List[Any]]: Transposed array.

    Usage Example:
        >>> TRANSPOSE([[1,2],[3,4]])
        [[1, 3], [2, 4]]

    Cost: O(rows * cols)
    """
    return [list(row) for row in zip(*array)]


def EXPAND(array: List[List[Any]], rows: Optional[int] = None,
           columns: Optional[int] = None,
           pad_with: Any = "") -> List[List[Any]]:
    """Expand an array to the specified dimensions, padding with a value.

    Excel function: EXPAND

    Args:
        array: 2-D list to expand.
        rows: Target number of rows (default: keep current).
        columns: Target number of columns (default: keep current).
        pad_with: Value to fill in new cells.

    Returns:
        List[List[Any]]: Expanded array.

    Raises:
        ValueError: If target dimensions are smaller than the input.

    Usage Example:
        >>> EXPAND([[1,2],[3,4]], 3, 4, 0)
        [[1, 2, 0, 0], [3, 4, 0, 0], [0, 0, 0, 0]]

    Cost: O(rows * columns)
    """
    cur_rows = len(array)
    cur_cols = len(array[0]) if cur_rows else 0

    if rows is None:
        rows = cur_rows

    if columns is None:
        columns = cur_cols

    if rows < cur_rows or columns < cur_cols:
        raise ValueError(
            f"Target ({rows}, {columns}) must be >= source "
            f"({cur_rows}, {cur_cols})"
        )

    result = []

    for r in range(rows):

        if r < cur_rows:
            row = list(array[r]) + [pad_with] * (columns - cur_cols)
        else:
            row = [pad_with] * columns

        result.append(row)

    return result