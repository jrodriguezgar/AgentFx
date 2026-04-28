"""
Excel Information Functions Module.

This module provides Excel-compatible validation and error handling functions for AgentFx.
Functions include:
- IS Functions: ISBLANK, ISERR, ISERROR, ISEVEN, ISLOGICAL, ISNA, 
  ISNONTEXT, ISNUMBER, ISODD, ISOMITTED, ISTEXT
- Error handling: ERROR_TYPE

All functions follow Excel naming conventions and behavior.

Note: Functions like CELL, INFO, ISREF, and ISFORMULA are excluded because they
depend on Excel's application context (cells, worksheets, references) which don't
exist in standalone Python execution.
"""

from typing import Any, Optional, Union
import inspect
import math

from agentfx.fxPython.py_logic import (
    is_logical as _core_is_logical,
    is_number as _core_is_number,
    is_text as _core_is_text,
)
from agentfx.fxNumeric.number_theory_functions import (
    is_even as _core_is_even,
    is_odd as _core_is_odd,
)


# ============================================================================
# IS FUNCTIONS (VALIDATION)
# ============================================================================

def ISBLANK(value: Any) -> bool:
    """
    Return TRUE if the value is blank.
    
    Args:
        value: Value to test.
    
    Returns:
        bool: True if value is blank, False otherwise.
    
    Example:
        >>> ISBLANK(None)
        True
        >>> ISBLANK("")
        True
        >>> ISBLANK("text")
        False
    
    Cost: O(1)
    """
    return value is None or (isinstance(value, str) and value.strip() == "")


def ISERR(value: Any) -> bool:
    """
    Return TRUE if the value is any error value except #N/A.
    
    Args:
        value: Value to test.
    
    Returns:
        bool: True if value is error (except #N/A), False otherwise.
    
    Example:
        >>> ISERR(ValueError())
        True
        >>> ISERR("#N/A")
        False
    
    Cost: O(1)
    """
    return isinstance(value, Exception) and not ISNA(value)


def ISERROR(value: Any) -> bool:
    """
    Return TRUE if the value is any error value.
    
    Args:
        value: Value to test.
    
    Returns:
        bool: True if value is any error, False otherwise.
    
    Example:
        >>> ISERROR(ValueError())
        True
        >>> ISERROR(42)
        False
    
    Cost: O(1)
    """
    return isinstance(value, Exception)


def ISEVEN(number: Union[int, float]) -> bool:
    """
    Return TRUE if the number is even.
    
    Args:
        number: Number to test.
    
    Returns:
        bool: True if number is even, False otherwise.
    
    Example:
        >>> ISEVEN(4)
        True
        >>> ISEVEN(3)
        False
    
    Cost: O(1)
    """
    try:
        return _core_is_even(int(number))
    except (ValueError, TypeError):
        return False


def ISLOGICAL(value: Any) -> bool:
    """
    Return TRUE if the value is a logical value.
    
    Args:
        value: Value to test.
    
    Returns:
        bool: True if value is boolean, False otherwise.
    
    Example:
        >>> ISLOGICAL(True)
        True
        >>> ISLOGICAL(1)
        False
    
    Cost: O(1)
    """
    return _core_is_logical(value)


def ISNA(value: Any) -> bool:
    """
    Return TRUE if the value is the #N/A error value.
    
    Args:
        value: Value to test.
    
    Returns:
        bool: True if value is #N/A, False otherwise.
    
    Example:
        >>> ISNA("#N/A")
        True
        >>> ISNA(ValueError())
        False
    
    Cost: O(1)
    """
    return value == "#N/A" or (isinstance(value, float) and math.isnan(value))


def ISNONTEXT(value: Any) -> bool:
    """
    Return TRUE if the value is not text.
    
    Args:
        value: Value to test.
    
    Returns:
        bool: True if value is not text, False otherwise.
    
    Example:
        >>> ISNONTEXT(42)
        True
        >>> ISNONTEXT("text")
        False
    
    Cost: O(1)
    """
    return not ISTEXT(value)


def ISNUMBER(value: Any) -> bool:
    """
    Return TRUE if the value is a number.
    
    Args:
        value: Value to test.
    
    Returns:
        bool: True if value is numeric, False otherwise.
    
    Example:
        >>> ISNUMBER(42)
        True
        >>> ISNUMBER(3.14)
        True
        >>> ISNUMBER("42")
        False
    
    Cost: O(1)
    """
    return _core_is_number(value)


def ISODD(number: Union[int, float]) -> bool:
    """
    Return TRUE if the number is odd.
    
    Args:
        number: Number to test.
    
    Returns:
        bool: True if number is odd, False otherwise.
    
    Example:
        >>> ISODD(3)
        True
        >>> ISODD(4)
        False
    
    Cost: O(1)
    """
    try:
        return _core_is_odd(int(number))
    except (ValueError, TypeError):
        return False


def ISOMITTED(value: Any) -> bool:
    """
    Check if a value is missing in a LAMBDA expression.
    
    Args:
        value: Value to test.
    
    Returns:
        bool: True if value was omitted, False otherwise.
    
    Example:
        >>> ISOMITTED(inspect.Parameter.empty)
        True
        >>> ISOMITTED(42)
        False
    
    Cost: O(1)
    """
    return value is inspect.Parameter.empty


def ISTEXT(value: Any) -> bool:
    """
    Return TRUE if the value is text.
    
    Args:
        value: Value to test.
    
    Returns:
        bool: True if value is text, False otherwise.
    
    Example:
        >>> ISTEXT("hello")
        True
        >>> ISTEXT(42)
        False
    
    Cost: O(1)
    """
    return _core_is_text(value)


# ============================================================================
# ERROR HANDLING FUNCTIONS
# ============================================================================

def N(value: Any) -> Union[int, float]:
    """
    Return a value converted to a number.
    
    Args:
        value: Value to convert.
    
    Returns:
        Union[int, float]: Numeric value.
            - Numbers return themselves
            - True returns 1, False returns 0
            - Dates return serial number
            - Everything else returns 0
    
    Example:
        >>> N(42)
        42
        >>> N(True)
        1
        >>> N("text")
        0
    
    Cost: O(1)
    """
    if ISNUMBER(value):
        return value
    if isinstance(value, bool):
        return 1 if value else 0
    return 0


def NA() -> str:
    """
    Return the error value #N/A.
    
    Returns:
        str: "#N/A" error value.
    
    Example:
        >>> NA()
        '#N/A'
    
    Cost: O(1)
    """
    return "#N/A"


def ERROR_TYPE(error_val: Any) -> Optional[int]:
    """
    Return a number corresponding to an error type.
    
    Args:
        error_val: Error value to analyze.
    
    Returns:
        Optional[int]: Error number, or None if not an error.
            - 1: #NULL!
            - 2: #DIV/0!
            - 3: #VALUE!
            - 4: #REF!
            - 5: #NAME?
            - 6: #NUM!
            - 7: #N/A
    
    Example:
        >>> ERROR_TYPE(ZeroDivisionError())
        2
        >>> ERROR_TYPE(42)
        None
    
    Cost: O(1)
    """
    if not ISERROR(error_val):
        return None
    
    error_types = {
        ZeroDivisionError: 2,
        ValueError: 3,
        NameError: 5,
        TypeError: 6,
        "#N/A": 7
    }
    
    return error_types.get(type(error_val), 3)


def TYPE(value: Any) -> int:
    """Returns the type of a value as a numeric code.

    Follows Excel's TYPE function convention:
        1 = Number (int or float)
        2 = Text (str)
        4 = Logical (bool)
        16 = Error (Exception)
        64 = Array (list, tuple, or numpy array)

    Excel function: TYPE

    Args:
        value: The value whose type to determine.

    Returns:
        int: Type code (1, 2, 4, 16, or 64).

    Usage Example:
        >>> TYPE(42)
        1
        >>> TYPE(3.14)
        1
        >>> TYPE("hello")
        2
        >>> TYPE(True)
        4
        >>> TYPE([1, 2, 3])
        64
        >>> TYPE(ValueError())
        16

    Cost: O(1)
    """
    if isinstance(value, bool):
        return 4

    if isinstance(value, (int, float)):
        return 1

    if isinstance(value, str):
        if value in ("#N/A", "#DIV/0!", "#VALUE!", "#REF!", "#NAME?", "#NUM!", "#NULL!"):
            return 16

        return 2

    if isinstance(value, Exception):
        return 16

    if isinstance(value, (list, tuple)):
        return 64

    return 1