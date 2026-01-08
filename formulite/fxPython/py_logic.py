"""Logical operations and conditional functions for Python collections."""

from typing import Any, Iterable


def and_all(*args: bool) -> bool:
    """Returns True if all arguments are True; False otherwise.
    
    Description:
        Python implementation of logical AND operation that evaluates multiple
        boolean values. Returns True only when all provided arguments evaluate
        to True, similar to Excel's AND function.
    
    Args:
        *args (bool): One or more boolean values to evaluate.
    
    Returns:
        bool: True if all arguments are True, False otherwise.
    
    Raises:
        ValueError: If no arguments are provided.
        TypeError: If any argument is not a boolean.
    
    Usage Example:
        >>> and_all(True, True, True)
        True
        >>> and_all(True, False, True)
        False
        >>> and_all(5 > 3, 10 < 20, "a" == "a")
        True
    
    Cost: O(n) where n is the number of arguments
    """
    if not args:
        raise ValueError("and_all requires at least one argument.")
    
    for arg in args:
        if not isinstance(arg, bool):
            raise TypeError("All arguments must be boolean values.")
        if not arg:
            return False
    
    return True


def or_any(*args: bool) -> bool:
    """Returns True if any argument is True; False if all are False.
    
    Description:
        Python implementation of logical OR operation that evaluates multiple
        boolean values. Returns True when at least one argument evaluates
        to True, similar to Excel's OR function.
    
    Args:
        *args (bool): One or more boolean values to evaluate.
    
    Returns:
        bool: True if any argument is True, False otherwise.
    
    Raises:
        ValueError: If no arguments are provided.
        TypeError: If any argument is not a boolean.
    
    Usage Example:
        >>> or_any(True, False, False)
        True
        >>> or_any(False, False, False)
        False
        >>> or_any(5 < 3, 10 > 20, "a" == "a")
        True
    
    Cost: O(n) where n is the number of arguments
    """
    if not args:
        raise ValueError("or_any requires at least one argument.")
    
    for arg in args:
        if not isinstance(arg, bool):
            raise TypeError("All arguments must be boolean values.")
        if arg:
            return True
    
    return False


def not_value(logical_value: bool) -> bool:
    """Reverses the logical value of its argument.
    
    Description:
        Returns the opposite boolean value. If True, returns False;
        if False, returns True. Equivalent to Excel's NOT function.
    
    Args:
        logical_value (bool): The boolean value to negate.
    
    Returns:
        bool: The opposite boolean value.
    
    Raises:
        TypeError: If the argument is not a boolean.
    
    Usage Example:
        >>> not_value(True)
        False
        >>> not_value(False)
        True
        >>> not_value(5 > 10)
        True
    
    Cost: O(1)
    """
    if not isinstance(logical_value, bool):
        raise TypeError("The argument must be a boolean value.")
    
    return not logical_value


def xor_all(*args: bool) -> bool:
    """Returns True if an odd number of arguments are True.
    
    Description:
        Logical exclusive OR operation. Returns True when an odd number
        of arguments evaluate to True, False otherwise. Equivalent to
        Excel's XOR function.
    
    Args:
        *args (bool): One or more boolean values to evaluate.
    
    Returns:
        bool: True if an odd number of arguments are True, False otherwise.
    
    Raises:
        ValueError: If no arguments are provided.
        TypeError: If any argument is not a boolean.
    
    Usage Example:
        >>> xor_all(True, True)
        False
        >>> xor_all(True, False)
        True
        >>> xor_all(True, True, True)
        True
    
    Cost: O(n) where n is the number of arguments
    """
    if not args:
        raise ValueError("xor_all requires at least one argument.")
    
    true_count = 0
    for arg in args:
        if not isinstance(arg, bool):
            raise TypeError("All arguments must be boolean values.")
        if arg:
            true_count += 1
    
    return true_count % 2 == 1


def if_then_else(logical_test: bool, value_if_true: Any, value_if_false: Any) -> Any:
    """Returns one value if condition is True, another if False.
    
    Description:
        Conditional function that evaluates a logical test and returns
        different values based on the result. Equivalent to Excel's IF
        function or Python's ternary operator.
    
    Args:
        logical_test (bool): The condition to test.
        value_if_true (Any): The value to return if logical_test is True.
        value_if_false (Any): The value to return if logical_test is False.
    
    Returns:
        Any: Either value_if_true or value_if_false based on the test.
    
    Raises:
        TypeError: If logical_test is not a boolean.
    
    Usage Example:
        >>> if_then_else(True, "Yes", "No")
        'Yes'
        >>> if_then_else(5 > 3, "Greater", "Smaller")
        'Greater'
        >>> if_then_else(False, 10, 20)
        20
    
    Cost: O(1)
    """
    if not isinstance(logical_test, bool):
        raise TypeError("The 'logical_test' argument must be a boolean value.")
    
    return value_if_true if logical_test else value_if_false


def if_error(value: Any, value_if_error: Any) -> Any:
    """Returns value if not an error; otherwise returns alternative value.
    
    Description:
        Attempts to return the provided value. If value is callable and
        raises an exception, or if value itself is an exception, returns
        the alternative error value. Similar to Excel's IFERROR function.
    
    Args:
        value (Any): The value or callable to check for errors.
        value_if_error (Any): The value to return if an error occurs.
    
    Returns:
        Any: The result of value if no error, otherwise value_if_error.
    
    Usage Example:
        >>> if_error(10 / 2, "Error!")
        5.0
        >>> if_error(lambda: 10 / 0, "Error!")
        'Error!'
        >>> if_error(lambda: int("abc"), "Invalid")
        'Invalid'
    
    Cost: O(1)
    """
    try:
        if callable(value):
            return value()
        return value
    except Exception:
        return value_if_error


def is_blank(value: Any) -> bool:
    """Returns True if value is blank (None, empty string, or empty collection).
    
    Description:
        Checks whether a value is considered blank. Returns True for None,
        empty strings, and empty collections. Equivalent to Excel's ISBLANK.
    
    Args:
        value (Any): The value to check.
    
    Returns:
        bool: True if the value is considered blank, False otherwise.
    
    Usage Example:
        >>> is_blank(None)
        True
        >>> is_blank("")
        True
        >>> is_blank([])
        True
        >>> is_blank("Hello")
        False
        >>> is_blank(0)
        False
    
    Cost: O(1) for most cases; O(n) for checking empty collections
    """
    if value is None:
        return True
    if isinstance(value, str) and value == "":
        return True
    if isinstance(value, Iterable) and not isinstance(value, str):
        try:
            return not bool(list(value))
        except TypeError:
            return False
    
    return False


def is_error(value: Any) -> bool:
    """Returns True if evaluating value produces an error.
    
    Description:
        Checks if a value (typically a callable) raises an exception when
        evaluated. Returns True for errors, False otherwise. Similar to
        Excel's ISERROR function.
    
    Args:
        value (Any): The value or callable to check for errors.
    
    Returns:
        bool: True if an error occurs, False otherwise.
    
    Usage Example:
        >>> is_error(lambda: 10 / 2)
        False
        >>> is_error(lambda: 10 / 0)
        True
        >>> is_error(lambda: int("abc"))
        True
    
    Cost: O(1) plus the cost of executing the callable
    """
    if callable(value):
        try:
            value()
            return False
        except Exception:
            return True
    
    return False


def is_text(value: Any) -> bool:
    """Returns True if value is a string.
    
    Description:
        Type checking function that determines if a value is text.
        Equivalent to Excel's ISTEXT function.
    
    Args:
        value (Any): The value to check.
    
    Returns:
        bool: True if the value is a string, False otherwise.
    
    Usage Example:
        >>> is_text("hello")
        True
        >>> is_text(123)
        False
        >>> is_text(True)
        False
    
    Cost: O(1)
    """
    return isinstance(value, str)


def is_number(value: Any) -> bool:
    """Returns True if value is a number (int or float, not bool).
    
    Description:
        Type checking function that determines if a value is numeric.
        Excludes booleans even though they are technically integers in
        Python. Equivalent to Excel's ISNUMBER function.
    
    Args:
        value (Any): The value to check.
    
    Returns:
        bool: True if the value is an int or float, False otherwise.
    
    Usage Example:
        >>> is_number(123)
        True
        >>> is_number(3.14)
        True
        >>> is_number("hello")
        False
        >>> is_number(True)
        False
    
    Cost: O(1)
    """
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def is_logical(value: Any) -> bool:
    """Returns True if value is a boolean.
    
    Description:
        Type checking function that determines if a value is a logical
        boolean. Equivalent to Excel's ISLOGICAL function.
    
    Args:
        value (Any): The value to check.
    
    Returns:
        bool: True if the value is a boolean, False otherwise.
    
    Usage Example:
        >>> is_logical(True)
        True
        >>> is_logical(False)
        True
        >>> is_logical(0)
        False
        >>> is_logical("True")
        False
    
    Cost: O(1)
    """
    return isinstance(value, bool)


def switch_case(expression: Any, *args: Any) -> Any:
    """Evaluates expression against values and returns matching result.
    
    Description:
        Switch-case implementation that compares an expression against
        multiple value-result pairs. Returns the result for the first
        matching value, or a default if no match found. Similar to
        Excel's SWITCH function.
    
    Args:
        expression (Any): The value to compare.
        *args (Any): Pairs of (value, result), optionally ending with default.
    
    Returns:
        Any: The result corresponding to the first match, or default value.
    
    Raises:
        ValueError: If insufficient arguments or no match without default.
    
    Usage Example:
        >>> switch_case(3, 1, "One", 2, "Two", 3, "Three", "Other")
        'Three'
        >>> switch_case("apple", "orange", "Fruit", "apple", "Favorite", "Unknown")
        'Favorite'
        >>> switch_case(5, 1, "One", 2, "Two", "Not Found")
        'Not Found'
    
    Cost: O(n) where n is the number of value-result pairs
    """
    if len(args) < 2:
        raise ValueError("switch_case requires at least one value-result pair.")
    
    has_default = len(args) % 2 != 0
    
    for i in range(0, len(args) - (1 if has_default else 0), 2):
        case_value = args[i]
        result_value = args[i + 1]
        if expression == case_value:
            return result_value
    
    if has_default:
        return args[-1]
    
    raise ValueError("No match found for the expression and no default value provided.")


