"""
AgentFx - fxPython: Python Tools Module

This module provides high-level utility functions for Python programming patterns.
It includes functions for:
- Dictionary creation from key-value pairs
- Higher-order function execution (function_call, loop_for, loop_while)
- Switch-case pattern implementation
- Collection rotation and shifting operations
- Dynamic expression evaluation on iterables

All functions follow PEP standards with complete documentation including
complexity analysis.
"""

from collections import deque
from typing import Callable, Iterable, Any


def create_key_value_dictionary(p_key_columns, p_values):
    """Creates a dictionary by mapping key column names to their corresponding values.

    This function takes a string or list of key column names and a value or tuple of values,
    then combines them into a dictionary. It handles cases where p_key_columns is a
    comma-separated string or a list, ensuring that column names are properly cleaned.

    Args:
        p_key_columns (str or list): A comma-separated string of column names
                                     (e.g., "id,name") or a list of column names
                                     (e.g., ["id", "name"]).
        p_values (any or tuple): A single value or a tuple of values to be
                                 associated with the key columns.

    Returns:
        dict: A dictionary where keys are the column names and values are the
              corresponding input values. Returns None if inputs are empty or invalid.

    Raises:
        ValueError: If the number of key columns does not match the number of values.

    Example of use:
        >>> create_key_value_dictionary("id,name", (1, "Alice"))
        {'id': 1, 'name': 'Alice'}
        >>> create_key_value_dictionary(["product_id"], "P123")
        {'product_id': 'P123'}

    **Cost:** O(n), where n is the number of key columns.
    """
    # Validate inputs to ensure they are not empty.
    if not p_key_columns or not p_values:
        raise ValueError("The request cannot be empty.")

    # Normalize key_columns into a list of strings.
    if isinstance(p_key_columns, str):
        # Ensure key_columns is a list, even for a single column string.
        # This simplifies subsequent processing by consistently working with a list.
        key_column_names = [col.strip() for col in p_key_columns.split(',') if col.strip()]
    elif isinstance(p_key_columns, list):
        # Clean any whitespace from list elements directly.
        key_column_names = [col.strip() for col in p_key_columns if col.strip()]
    else:
        # Handle unexpected types for p_key_columns gracefully.
        raise TypeError("Invalid type for p_key_columns. Expected string or list.")

    # Normalize p_values into a tuple for consistent zipping.
    # We wrap single values in a tuple to allow iteration.
    values = p_values if isinstance(p_values, tuple) else (p_values,)

    # Ensure the number of keys matches the number of values to prevent errors during zipping.
    if len(key_column_names) != len(values):
        raise ValueError(
            f"The number of key columns ({len(key_column_names)}) "
            f"does not match the number of values ({len(values)})."
        )

    # Create the dictionary by zipping column names and values.
    # This is efficient and idiomatic Python for combining two lists into a dictionary.
    dict_keys = dict(zip(key_column_names, values))

    return dict_keys


def function_call(func: callable, *args, **kwargs) -> Any:
    """
    Higher-order function that executes a callable with optional arguments.

    This function provides a simple abstraction for executing any callable object,
    allowing you to pass both positional and keyword arguments. It's useful for
    building functional programming patterns and creating flexible execution flows.

    Args:
        func (callable): The function to execute.
        *args: Positional arguments to pass to the function.
        **kwargs: Keyword arguments to pass to the function.

    Returns:
        Any: The return value of the executed function.

    Raises:
        TypeError: If func is not callable.

    Example of use:
        >>> def greet(name, greeting="Hello"):
        ...     return f"{greeting}, {name}!"
        >>> function_call(greet, "Alice")
        'Hello, Alice!'
        >>> function_call(greet, "Bob", greeting="Hi")
        'Hi, Bob!'

    **Cost:** O(1) plus the cost of executing the provided function.
    """
    if not callable(func):
        raise TypeError("First argument must be a callable object.")

    return func(*args, **kwargs)


def switch_case(value, *cases, default=None):
    """Acts like a generic switch-case statement.

    Delegates to :func:`~agentfx.fxPython.py_logic.switch_case`.
    Accepts an explicit ``default`` keyword instead of the positional
    odd-argument convention used by the core implementation.

    Args:
        value: The value to be evaluated.
        *cases: A sequence of cases where each pair consists of a key and a value.
                Example: key1, value1, key2, value2, ...
        default: The value to return if no match is found. Defaults to None.

    Returns:
        The value associated with the matching key, or the default value if no match.

    Raises:
        ValueError: If the number of items in *cases is not an even number.

    Usage Example:
        >>> switch_case(2, 1, "January", 2, "February", 3, "March", default="Unknown Month")
        'February'

    Cost: O(n) where n is the number of case pairs
    """
    if len(cases) % 2 != 0:
        raise ValueError("Cases must be provided in key-value pairs.")

    from agentfx.fxPython.py_logic import switch_case as _core_switch

    return _core_switch(value, *cases, default)


def loop_for(iterable, func):
    """
    Executes a function for each item in an iterable, simulating a for loop.

    This function abstracts the common pattern of iterating over a sequence
    and applying a specific operation to each element. It promotes code
    reusability by separating the iteration logic from the operation itself.

    Args:
        iterable: An iterable object (e.g., a list, tuple, string) to loop over.
        func: A callable function that takes a single argument (the current item
              from the iterable) and performs an action.

    Example of use:
        >>> my_list = [1, 2, 3]
        >>> def print_item(item):
        ...     print(f"Current item: {item}")
        >>> loop_for(my_list, print_item)
        Current item: 1
        Current item: 2
        Current item: 3

    **Cost:** O(n), where n is the number of items in the iterable.
    """
    for item in iterable:
        func(item)


def loop_while(condition, func, *args, **kwargs):
    """
    Executes a function repeatedly as long as a specified condition is true.

    This function abstracts a while loop, allowing you to define the loop's
    continuation condition and the action to perform in each iteration as
    separate, reusable components.

    Args:
        condition: A callable function that takes a variable number of positional
                   and keyword arguments and returns a boolean value. The loop
                   continues as long as this function returns True.
        func: A callable function that is executed in each iteration of the loop.
              It should also accept the same arguments.
        *args: Positional arguments to pass to both the condition and func functions.
        **kwargs: Keyword arguments to pass to both the condition and func functions.

    Example of use:
        >>> count = [0]
        >>> def is_less_than_five(c):
        ...     return c[0] < 5
        >>> def increment_count(c):
        ...     print(f"Current count: {c[0]}")
        ...     c[0] += 1
        >>> loop_while(is_less_than_five, increment_count, count)
        Current count: 0
        Current count: 1
        Current count: 2
        Current count: 3
        Current count: 4

    **Cost:** O(k), where k is the number of iterations until condition becomes False.
    """
    while condition(*args, **kwargs):
        func(*args, **kwargs)


def rotate(iterable, steps=1):
    """
    Rotates the elements of an iterable.

    This function rotates the elements of an iterable by a specified number of steps.
    A positive `steps` value rotates elements to the right, and a negative value
    rotates them to the left. The function returns a new list and does not modify
    the original iterable.

    Args:
        iterable: The collection (e.g., list, tuple) to be rotated.
        steps: The number of positions to rotate. A positive integer shifts
               elements to the right, and a negative integer shifts to the left.

    Returns:
        A new list with the elements rotated.

    Example of use:
        >>> my_list = [1, 2, 3, 4]

        >>> # Rotate right by one step (default)
        >>> rotate_right = rotate(my_list)
        >>> print(f"Rotate right: {rotate_right}")
        Rotate right: [4, 1, 2, 3]

        >>> # Rotate left by two steps
        >>> rotate_left = rotate(my_list, steps=-2)
        >>> print(f"Rotate left: {rotate_left}")
        Rotate left: [3, 4, 1, 2]

        >>> # Rotate right by three steps
        >>> rotate_right_three = rotate(my_list, steps=3)
        >>> print(f"Rotate right three: {rotate_right_three}")
        Rotate right three: [2, 3, 4, 1]

    **Cost:** O(n), where n is the number of elements in the iterable.
    """
    if not iterable:
        return []

    collection = deque(iterable)
    collection.rotate(steps)

    return list(collection)


def shift(iterable: Iterable[Any], direction: str = None, new_elements: Iterable[Any] = None) -> list[Any]:
    """
    Shifts an iterable, adding or removing elements.

    This function provides a flexible way to modify an iterable by shifting its
    elements and optionally adding multiple new elements from another iterable.
    It does not modify the original iterable, but returns a new one.

    Args:
        iterable: The collection (e.g., list, tuple) to be shifted.
        direction: A string indicating the shift direction ('left' or 'right').
                   If None, it removes one element from the left.
        new_elements: An iterable of elements to add to the collection.
                      If None, the function removes one element from the
                      specified direction.

    Returns:
        A new list representing the shifted collection.

    Raises:
        ValueError: If an invalid direction is provided.

    Example of use:
        >>> my_list = [1, 2, 3, 4]

        >>> # Remove the first element (default behavior)
        >>> removed_first = shift(my_list)
        >>> print(f"Removed first: {removed_first}")
        Removed first: [2, 3, 4]

        >>> # Remove the last element
        >>> removed_last = shift(my_list, direction='right')
        >>> print(f"Removed last: {removed_last}")
        Removed last: [1, 2, 3]

        >>> # Shift left, adding multiple elements from a tuple
        >>> elements_to_add = (5, 6, 7)
        >>> shifted_left = shift(my_list, direction='left', new_elements=elements_to_add)
        >>> print(f"Shift left and add: {shifted_left}")
        Shift left and add: [2, 3, 4, 5, 6, 7]

        >>> # Shift right, adding multiple elements from a list
        >>> shifted_right = shift(my_list, direction='right', new_elements=[0, -1])
        >>> print(f"Shift right and add: {shifted_right}")
        Shift right and add: [0, -1, 1, 2, 3]

    **Cost:** O(n + m), where n is the size of the iterable and m is the number of new elements.
    """
    if not iterable:
        return []

    collection = deque(iterable)

    if new_elements is not None:
        num_elements_to_add = len(new_elements)
        if direction == 'left':
            for _ in range(num_elements_to_add):
                collection.popleft()
            collection.extend(new_elements)
        elif direction == 'right':
            for _ in range(num_elements_to_add):
                collection.pop()
            collection.extendleft(reversed(new_elements))
        else:
            raise ValueError("Direction must be specified when adding elements.")
    else:
        if direction == 'left' or direction is None:
            collection.popleft()
        elif direction == 'right':
            collection.pop()
        else:
            raise ValueError("Invalid direction. Use 'left', 'right', or None.")

    return list(collection)


def apply_expression(expression: str, iterable: Iterable[Any]) -> list[Any]:
    """
    Applies a string expression to every item in an iterable and returns a list.

    This function dynamically creates a lambda function from a string expression,
    providing a concise way to perform transformations on a collection of data
    without manually writing a lambda function.

    Args:
        expression: A string representing a Python expression (e.g., 'x * 2').
        iterable: A collection of items to which the expression will be applied.

    Returns:
        A new list containing the results of applying the expression to each item.

    Raises:
        SyntaxError: If the expression string is not a valid Python expression.

    Example of use:
        >>> my_numbers = [1, 2, 3, 4]
        >>> results = apply_expression('x * x', my_numbers)
        >>> print(results)
        [1, 4, 9, 16]

        >>> my_strings = ['hello', 'world']
        >>> capitalized_strings = apply_expression('x.capitalize()', my_strings)
        >>> print(capitalized_strings)
        ['Hello', 'World']

    **Cost:** O(n), where n is the number of items in the iterable.
    """
    import ast
    import operator as _op

    tree = ast.parse(expression, mode="eval")

    _SAFE_BUILTINS: dict[str, Any] = {
        "abs": abs, "all": all, "any": any, "bool": bool,
        "chr": chr, "divmod": divmod, "enumerate": enumerate,
        "float": float, "int": int, "isinstance": isinstance,
        "len": len, "list": list, "map": map, "max": max,
        "min": min, "ord": ord, "pow": pow, "range": range,
        "round": round, "set": set, "sorted": sorted, "str": str,
        "sum": sum, "tuple": tuple, "type": type, "zip": zip,
    }

    _BIN_OPS = {
        ast.Add: _op.add, ast.Sub: _op.sub, ast.Mult: _op.mul,
        ast.Div: _op.truediv, ast.FloorDiv: _op.floordiv,
        ast.Mod: _op.mod, ast.Pow: _op.pow,
    }
    _UNARY_OPS = {ast.UAdd: _op.pos, ast.USub: _op.neg, ast.Not: _op.not_}
    _CMP_OPS = {
        ast.Eq: _op.eq, ast.NotEq: _op.ne, ast.Lt: _op.lt,
        ast.LtE: _op.le, ast.Gt: _op.gt, ast.GtE: _op.ge,
        ast.In: lambda a, b: a in b,
        ast.NotIn: lambda a, b: a not in b,
        ast.Is: _op.is_, ast.IsNot: _op.is_not,
    }
    _BOOL_OPS = {ast.And: all, ast.Or: any}

    def _eval(node: ast.AST, x: Any) -> Any:  # noqa: C901
        if isinstance(node, ast.Expression):
            return _eval(node.body, x)
        if isinstance(node, ast.Constant):
            return node.value
        if isinstance(node, ast.Name):
            if node.id == "x":
                return x
            if node.id in _SAFE_BUILTINS:
                return _SAFE_BUILTINS[node.id]
            raise NameError(f"Name '{node.id}' is not allowed")
        if isinstance(node, ast.BinOp):
            op_fn = _BIN_OPS.get(type(node.op))
            if op_fn is None:
                raise SyntaxError(f"Unsupported operator: {type(node.op).__name__}")
            return op_fn(_eval(node.left, x), _eval(node.right, x))
        if isinstance(node, ast.UnaryOp):
            op_fn = _UNARY_OPS.get(type(node.op))
            if op_fn is None:
                raise SyntaxError(f"Unsupported unary operator: {type(node.op).__name__}")
            return op_fn(_eval(node.operand, x))
        if isinstance(node, ast.Compare):
            left = _eval(node.left, x)
            for op_node, comparator in zip(node.ops, node.comparators):
                cmp_fn = _CMP_OPS.get(type(op_node))
                if cmp_fn is None:
                    raise SyntaxError(f"Unsupported comparator: {type(op_node).__name__}")
                right = _eval(comparator, x)
                if not cmp_fn(left, right):
                    return False
                left = right
            return True
        if isinstance(node, ast.BoolOp):
            fn = _BOOL_OPS.get(type(node.op))
            if fn is None:
                raise SyntaxError(f"Unsupported bool op: {type(node.op).__name__}")
            return fn(_eval(v, x) for v in node.values)
        if isinstance(node, ast.IfExp):
            return _eval(node.body, x) if _eval(node.test, x) else _eval(node.orelse, x)
        if isinstance(node, ast.Attribute):
            obj = _eval(node.value, x)
            attr = node.attr
            if attr.startswith("_"):
                raise SyntaxError(f"Access to private attribute '{attr}' is not allowed")
            if not isinstance(obj, (str, int, float, bool, list, tuple, dict, set)):
                raise SyntaxError(
                    f"Attribute access on type '{type(obj).__name__}' is not allowed"
                )
            return getattr(obj, attr)
        if isinstance(node, ast.Call):
            func = _eval(node.func, x)
            if node.keywords:
                raise SyntaxError("Keyword arguments are not supported")
            args = [_eval(a, x) for a in node.args]
            return func(*args)
        if isinstance(node, ast.Subscript):
            return _eval(node.value, x)[_eval(node.slice, x)]
        if isinstance(node, (ast.List, ast.Tuple)):
            items = [_eval(el, x) for el in node.elts]
            return items if isinstance(node, ast.List) else tuple(items)
        raise SyntaxError(f"Unsupported expression element: {type(node).__name__}")

    return [_eval(tree, item) for item in iterable]


def pipe(value: Any, *functions: Callable) -> Any:
    """Threads a value through a sequence of functions.

    Applies each function to the result of the previous one, left to right.

    Args:
        value: The initial value.
        *functions: One or more callables to apply in order.

    Returns:
        The final result after all functions have been applied.

    Example:
        >>> pipe(5, lambda x: x * 2, lambda x: x + 3, str)
        '13'
        >>> pipe("  hello  ", str.strip, str.upper)
        'HELLO'

    **Cost:** O(k) where k is the number of functions.
    """
    result = value

    for func in functions:

        if not callable(func):
            raise TypeError(f"All arguments after value must be callable, got {type(func).__name__}.")

        result = func(result)

    return result


def retry(
    func: Callable,
    max_attempts: int = 3,
    delay: float = 1.0,
) -> Any:
    """Retries a function on failure up to a maximum number of attempts.

    Waits ``delay`` seconds between attempts using ``time.sleep``.

    Args:
        func: A zero-argument callable to execute.
        max_attempts: Maximum number of tries (default 3).
        delay: Seconds to wait between retries (default 1.0).

    Returns:
        The return value of ``func`` on success.

    Raises:
        RuntimeError: If all attempts fail, wrapping the last exception.

    Example:
        >>> counter = {"n": 0}
        >>> def flaky():
        ...     counter["n"] += 1
        ...     if counter["n"] < 3:
        ...         raise ValueError("not yet")
        ...     return "ok"
        >>> retry(flaky, max_attempts=5, delay=0)
        'ok'

    **Cost:** O(k) where k is max_attempts.
    """
    import time

    if max_attempts < 1:
        raise ValueError("max_attempts must be at least 1.")

    last_exc: Exception | None = None

    for attempt in range(1, max_attempts + 1):

        try:
            return func()
        except Exception as exc:
            last_exc = exc

            if attempt < max_attempts:
                time.sleep(delay)

    raise RuntimeError(
        f"All {max_attempts} attempts failed. Last error: {last_exc}"
    ) from last_exc
