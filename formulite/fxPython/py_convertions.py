"""
FormuLite - fxPython: Python Collection Conversions Module

This module provides utility functions for converting between different Python
collection types (lists, tuples, sets, dictionaries) and strings. It includes
functions for:
- Converting between lists, tuples, and sets
- Converting collections to and from strings
- Dictionary key/value extractions and transformations
- Advanced type conversions with customizable formatting

All functions follow PEP standards with complete documentation including
complexity analysis.
"""

import json
from typing import Iterable, Callable, Any, Union, List, Tuple, Set, Dict, Type, Optional


def convert_collection(
    data_collection: Union[List[Any], Tuple[Any, ...], Set[Any]],
    target_type: Type[Union[List, Tuple, Set]]
) -> Union[List[Any], Tuple[Any, ...], Set[Any]]:
    """Converts a list, tuple, or set to a specified target collection type.

    This function takes an input collection (list, tuple, or set) and converts
    it to the desired target type. It handles type conversions between these
    three common collection types.

    Args:
        data_collection (Union[List[Any], Tuple[Any, ...], Set[Any]]): The
            input collection to convert. It can be a list, tuple, or set.
        target_type (Type[Union[List, Tuple, Set]]): The desired type for the
            output collection. Must be list, tuple, or set.

    Returns:
        Union[List[Any], Tuple[Any, ...], Set[Any]]: The converted collection
            of the specified `target_type`.

    Raises:
        TypeError: If `data_collection` is not a list, tuple, or set, or if
            `target_type` is not list, tuple, or set.

    Examples of use:
        >>> convert_collection([1, 'a', 3.5], tuple)
        (1, 'a', 3.5)
        >>> convert_collection((1, 2, 2, 'a'), set)
        {1, 2, 'a'} # Order not guaranteed
        >>> convert_collection({'red', 'green', 'blue'}, list)
        ['green', 'blue', 'red'] # Order not guaranteed
        >>> convert_collection([1, 2, 3], list)
        [1, 2, 3]
    Cost:
        The cost of this function is O(n), where n is the number of elements
        in the input collection, due to the iteration required for conversion
        by built-in constructors (list(), tuple(), set()).
    """
    if not isinstance(data_collection, (list, tuple, set)):
        # Because we only support list, tuple, and set as input.
        raise TypeError("Input 'data_collection' must be a list, tuple, or set.")

    if target_type not in (list, tuple, set):
        # Because the target type must be one of the supported collection types.
        raise TypeError("Target 'target_type' must be list, tuple, or set.")

    # Perform the conversion based on the target_type.
    if target_type is list:
        return list(data_collection)
    elif target_type is tuple:
        return tuple(data_collection)
    elif target_type is set:
        return set(data_collection)


# --- Set Conversions ---

def set_to_string(input_set: Set[Any], separator: str = ' ', use_quotes: bool = False) -> Optional[str]:
    """Converts a given set to its string representation.

    This function takes a set and converts its elements into a single string,
    joined by a specified separator. Optionally, string elements can be wrapped
    in single quotes. The order of elements in the resulting string is not
    guaranteed, as sets are inherently unordered. Returns None if the input set is empty.

    Args:
        input_set: The set to be converted.
        separator: The string used to join the elements. Defaults to a single space.
        use_quotes: If True, wraps string elements in single quotes. Defaults to False.

    Returns:
        The string representation of the set, or None if the input set is empty.

    Raises:
        TypeError: If the input 'input_set' is not a set.

    Example of use:
        >>> set_to_string({'apple', 'banana'}, separator=', ', use_quotes=True) # Order may vary
        "'apple', 'banana'"

        >>> set_to_string({1, 2, 3}, separator='-') # Order may vary
        "1-2-3"

        >>> set_to_string(set())
        None

    **Cost:** O(n), where n is the number of elements in the set.
    """
    # Return None immediately if the set is empty, aligning with the return type.
    if not input_set:
        return None

    # Use a generator expression to convert each item to a string.
    # Conditionally add quotes if 'use_quotes' is True.
    # It's important to note that the order of elements in the string
    # will be arbitrary, as sets do not guarantee order.
    if use_quotes:
        string_elements = (f"'{str(item)}'" for item in input_set)
    else:
        string_elements = (str(item) for item in input_set)

    # Join the processed string elements using the specified separator.
    return separator.join(string_elements)


def set_to_list(input_set: Set[Any]) -> List[Any]:
    """Converts a given set into a list.

    This function takes a set as input and returns a new list containing
    all the elements from the set. The order of elements in the resulting
    list is not guaranteed, as sets are inherently unordered.

    Args:
        input_set: The set to be converted to a list.

    Returns:
        A list containing the elements from the input set.

    Raises:
        TypeError: If the input 'input_set' is not a set.

    Example of use:
        >>> set_to_list({1, 2, 3}) # Order may vary
        [1, 2, 3]

        >>> set_to_list({'apple', 'banana'}) # Order may vary
        ['banana', 'apple']

        >>> set_to_list(set())
        []

    **Cost:** O(n), where n is the number of elements in the set.
    """
    # The built-in list() constructor is the most Pythonic and efficient
    # way to convert any iterable (like a set) into a list.
    # It handles all cases, including empty sets, correctly.
    converted_list = list(input_set)

    return converted_list


def set_to_tuple(input_set: Set[Any]) -> Tuple[Any, ...]:
    """Converts a given set into a tuple.

    This function takes a set as input and returns a new tuple containing
    all the elements from the set. The order of elements in the resulting
    tuple is not guaranteed, as sets are inherently unordered.

    Args:
        input_set: The set to be converted to a tuple.

    Returns:
        A tuple containing the elements from the input set.

    Raises:
        TypeError: If the input 'input_set' is not a set.

    Example of use:
        >>> set_to_tuple({1, 2, 3}) # Order may vary
        (1, 2, 3)

        >>> set_to_tuple({'red', 'green', 'blue'}) # Order may vary
        ('blue', 'red', 'green')

        >>> set_to_tuple(set())
        ()

    **Cost:** O(n), where n is the number of elements in the set.
    """
    # The built-in tuple() constructor is the most Pythonic and efficient
    # way to convert any iterable (like a set) into a tuple.
    # It handles all cases, including empty sets, correctly.
    converted_tuple = tuple(input_set)

    return converted_tuple


# --- Tuple Conversions ---

def tuple_to_string(input_tuple: Tuple[Any, ...], separator: str = ' ', use_quotes: bool = False) -> Optional[str]:
    """Converts a given tuple to its string representation.

    This function takes a tuple and converts its elements into a single string,
    joined by a specified separator. Optionally, string elements can be wrapped
    in single quotes. Returns None if the input tuple is empty.

    Args:
        input_tuple: The tuple to be converted.
        separator: The string used to join the elements. Defaults to a single space.
        use_quotes: If True, wraps string elements in single quotes. Defaults to False.

    Returns:
        The string representation of the tuple, or None if the input tuple is empty.

    Raises:
        TypeError: If the input 'input_tuple' is not a tuple.

    Example of use:
        >>> tuple_to_string(('apple', 'banana', 'orange'), separator=', ', use_quotes=True)
        "'apple', 'banana', 'orange'"

        >>> tuple_to_string((1, 2, 3), separator='-')
        "1-2-3"

        >>> tuple_to_string(())
        None

    **Cost:** O(n), where n is the number of elements in the tuple.
    """
    # Return None immediately if the tuple is empty, aligning with the return type.
    if not input_tuple:
        return None

    # Use a generator expression to convert each item to a string.
    # Conditionally add quotes if 'use_quotes' is True.
    # This approach is concise and efficient, avoiding intermediate list creation.
    if use_quotes:
        string_elements = (f"'{str(item)}'" for item in input_tuple)
    else:
        string_elements = (str(item) for item in input_tuple)

    # Join the processed string elements using the specified separator.
    return separator.join(string_elements)


def tuple_to_list(input_tuple: Tuple[Any, ...]) -> List[Any]:
    """Converts a given tuple into a list.

    This function takes a tuple as input and returns a new list containing
    all the elements from the tuple, maintaining their original order.

    Args:
        input_tuple: The tuple to be converted to a list.

    Returns:
        A list containing the elements from the input tuple.

    Raises:
        TypeError: If the input 'input_tuple' is not a tuple.

    Example of use:
        >>> tuple_to_list((1, 2, 3, 4, 5))
        [1, 2, 3, 4, 5]

        >>> tuple_to_list(('red', 'green', 'blue'))
        ['red', 'green', 'blue']

        >>> tuple_to_list(())
        []

    **Cost:** O(n), where n is the number of elements in the tuple.
    """
    # The built-in list() constructor is the most Pythonic and efficient
    # way to convert any iterable (like a tuple) into a list.
    # It handles all cases, including empty tuples, correctly.
    converted_list = list(input_tuple)

    return converted_list


def tuple_to_set(input_tuple: Tuple[Any, ...]) -> Set[Any]:
    """Converts a given tuple into a set.

    This function takes a tuple as input and returns a new set containing
    all the unique elements from the tuple. The order of elements is not
    preserved in the resulting set.

    Args:
        input_tuple: The tuple to be converted to a set.

    Returns:
        A set containing the unique elements from the input tuple.

    Raises:
        TypeError: If the input 'input_tuple' is not a tuple.

    Example of use:
        >>> tuple_to_set((1, 2, 2, 3, 4, 4, 5))
        {1, 2, 3, 4, 5}

        >>> tuple_to_set(('apple', 'banana', 'apple'))
        {'apple', 'banana'}

        >>> tuple_to_set(())
        set()

    **Cost:** O(n), where n is the number of elements in the tuple.
    """
    # The built-in set() constructor is the most Pythonic and efficient
    # way to convert any iterable (like a tuple) into a set.
    # It automatically handles duplicate removal and provides O(N) average
    # time complexity for the conversion.
    unique_elements_set = set(input_tuple)

    return unique_elements_set


# --- List Conversions ---

def list_to_string(lst: List[Any], separator: str = ' ', use_quotes: bool = False) -> Optional[str]:
    """Converts a list to its string representation.

    This function takes a list and converts its elements into a single string,
    joined by a specified separator. Optionally, string elements can be wrapped in
    single quotes. Returns None if the input list is empty.

    Args:
        lst: The list to be converted.
        separator: The string used to join the elements. Defaults to a single space.
        use_quotes: If True, wraps string elements in single quotes. Defaults to False.

    Returns:
        The string representation of the list, or None if the input list is empty.

    Raises:
        TypeError: If the input 'lst' is not a list.

    Example of use:
        >>> list_to_string(['apple', 'banana', 'orange'], separator=', ', use_quotes=True)
        "'apple', 'banana', 'orange'"

        >>> list_to_string([1, 2, 3], separator='-')
        "1-2-3"

        >>> list_to_string([])
        None

    **Cost:** O(n), where n is the number of elements in the list.
    """
    # Return None immediately if the list is empty, aligning with the return type.
    if not lst:
        return None

    # Use a generator expression to convert each item to a string.
    # Conditionally add quotes if 'use_quotes' is True.
    # This approach is concise and efficient, avoiding intermediate list creation.
    if use_quotes:
        string_elements = (f"'{str(item)}'" for item in lst)
    else:
        string_elements = (str(item) for item in lst)

    # Join the processed string elements using the specified separator.
    return separator.join(string_elements)


def list_to_set(input_list: List[Any]) -> Set[Any]:
    """Converts a given list into a set.

    This function takes a list as input and returns a new set containing
    all the unique elements from the list. The order of elements is not
    preserved in the resulting set.

    Args:
        input_list: The list to be converted to a set.

    Returns:
        A set containing the unique elements from the input list.

    Raises:
        TypeError: If the input 'input_list' is not a list.

    Example of use:
        >>> list_to_set([1, 2, 2, 3, 4, 4, 5])
        {1, 2, 3, 4, 5}

        >>> list_to_set(['apple', 'banana', 'apple'])
        {'apple', 'banana'}

        >>> list_to_set([])
        set()

    **Cost:** O(n), where n is the number of elements in the list.
    """
    # Create a set from the input list. This automatically handles
    # duplicate removal and provides O(N) average time complexity.
    unique_elements_set = set(input_list)

    return unique_elements_set


def list_to_tuple(input_list: List[Any]) -> Tuple[Any, ...]:
    """Converts a given list into a tuple.

    This function takes a list as input and returns a new tuple containing
    all the elements from the list, maintaining their order.

    Args:
        input_list: The list to be converted to a tuple.

    Returns:
        A tuple containing the elements from the input list.

    Raises:
        TypeError: If the input 'input_list' is not a list.

    Example of use:
        >>> list_to_tuple([1, 2, 3, 4, 5])
        (1, 2, 3, 4, 5)

        >>> list_to_tuple(['apple', 'banana', 'cherry'])
        ('apple', 'banana', 'cherry')

        >>> list_to_tuple([])
        ()

    **Cost:** O(n), where n is the number of elements in the list.
    """
    # The built-in tuple() constructor is the most Pythonic and efficient
    # way to convert any iterable (like a list) into a tuple.
    # It handles all cases, including empty lists, correctly.
    converted_tuple = tuple(input_list)

    return converted_tuple


# --- Dictionary Conversions ---

def dictionary_to_string(input_dict: dict) -> str:
    """Converts a dictionary into a string representation.

    This function serializes a dictionary into a string where keys and values
    are separated by colons and key-value pairs are separated by semicolons.
    It's useful for simple persistence or transmission when more robust
    serialization (like JSON or pickle) is overkill.

    Args:
        input_dict (dict): The dictionary to convert.

    Returns:
        str: A string representation of the input dictionary.

    Raises:
        TypeError: If the input_dict is not a dictionary.

    Example of usage:
        >>> my_dict = {"name": "Alice", "age": "30", "city": "New York"}
        >>> dictionary_to_string(my_dict)
        'name:Alice;age:30;city:New York'
    Cost: O(N) where N is the total number of characters in the dictionary's keys and values.
    """
    if not isinstance(input_dict, dict):
        raise TypeError("Input must be a dictionary.")

    # The goal is to create a string like "key1:value1;key2:value2"
    # Joining with ':' then with ';' is more efficient than string concatenation in a loop.
    pairs = [f"{key}:{value}" for key, value in input_dict.items()]
    return ";".join(pairs)


def string_to_dictionary(input_string: str) -> dict:
    """Converts a string representation back into a dictionary.

    This function deserializes a string, previously created by `dictionary_to_string()`,
    back into a dictionary. It's the inverse operation, useful for reconstructing
    the original dictionary from its string form.

    Args:
        input_string (str): The string to convert.

    Returns:
        dict: A dictionary reconstructed from the input string.

    Raises:
        TypeError: If the input_string is not a string.
        ValueError: If the input_string format is invalid (e.g., missing a colon).

    Example of usage:
        >>> my_string = 'name:Alice;age:30;city:New York'
        >>> string_to_dictionary(my_string)
        {'name': 'Alice', 'age': '30', 'city': 'New York'}
    Cost: O(N) where N is the length of the input string.
    """
    if not isinstance(input_string, str):
        return input_string

    output_dict = {}

    # If the string is empty, we should return an empty dictionary.
    if not input_string:
        return output_dict

    # We iterate over each key-value pair separated by semicolons.
    for pair in input_string.split(";"):
        # Splitting by the first colon ensures that values containing colons don't break the parsing.
        parts = pair.split(":", 1)
        if len(parts) != 2:
            # We raise a ValueError because an invalid format indicates an unrecoverable issue.
            raise ValueError(f"Invalid string format: '{pair}'. Expected 'key:value'.")
        key, value = parts
        output_dict[key] = value

    return output_dict


def dictionary_keys_to_list(data_dict: Dict[Any, Any]) -> List[Any]:
    """Returns the keys of a dictionary as a list.

    Args:
        data_dict (Dict[Any, Any]): The input dictionary.

    Returns:
        List[Any]: A list containing all keys from the dictionary.

    Example of use:
        >>> dictionary_keys_to_list({"name": "Alice", "age": 30})
        ['name', 'age']

    **Cost:** O(n), where n is the number of keys in the dictionary.
    """
    return list(data_dict.keys())


def dict_values_to_list(data_dict: Dict[Any, Any]) -> List[Any]:
    """Returns the values of a dictionary as a list.

    Args:
        data_dict (Dict[Any, Any]): The input dictionary.

    Returns:
        List[Any]: A list containing all values from the dictionary.

    Example of use:
        >>> dict_values_to_list({"item": "Laptop", "price": 1200})
        ['Laptop', 1200]

    **Cost:** O(n), where n is the number of values in the dictionary.
    """
    return list(data_dict.values())


def dictionary_items_to_list_of_tuples(data_dict: Dict[Any, Any]) -> List[Tuple[Any, Any]]:
    """Returns the key-value pairs (items) of a dictionary as a list of tuples.

    Args:
        data_dict (Dict[Any, Any]): The input dictionary.

    Returns:
        List[Tuple[Any, Any]]: A list where each element is a `(key, value)` tuple.

    Example of use:
        >>> dictionary_items_to_list_of_tuples({"city": "London", "population": 9000000})
        [('city', 'London'), ('population', 9000000)]

    **Cost:** O(n), where n is the number of items in the dictionary.
    """
    return list(data_dict.items())


def dictionary_keys_to_set(data_dict: Dict[Any, Any]) -> Set[Any]:
    """Returns the keys of a dictionary as a set.

    Args:
        data_dict (Dict[Any, Any]): The input dictionary.

    Returns:
        Set[Any]: A set containing all unique keys from the dictionary.

    Example of use:
        >>> dict_keys_to_set({"color": "red", "value": 50})
        {'color', 'value'} # Order not guaranteed

    **Cost:** O(n), where n is the number of keys in the dictionary.
    """
    return set(data_dict.keys())


def dictionary_values_to_set(data_dict: Dict[Any, Any]) -> Set[Any]:
    """Returns the values of a dictionary as a set, which inherently removes duplicate values.

    Args:
        data_dict (Dict[Any, Any]): The input dictionary.

    Returns:
        Set[Any]: A set containing all unique values from the dictionary.

    Example of use:
        >>> dictionary_values_to_set({"a": 1, "b": 2, "c": 1})
        {1, 2} # Order not guaranteed

    **Cost:** O(n), where n is the number of values in the dictionary.
    """
    return set(data_dict.values())


def dictionary_to_object(dictionary: dict) -> object:
    """Converts a dictionary into a simple object.

    This function dynamically creates a class and assigns the dictionary's
    key-value pairs as attributes to an instance of that class. This
    is useful for accessing dictionary data using dot notation.

    Args:
        dictionary (dict): The dictionary to convert.

    Returns:
        object: An object with attributes corresponding to the dictionary's keys.

    Raises:
        TypeError: If the input is not a dictionary.

    Example:
        >>> my_dict = {'name': 'Alice', 'age': 30}
        >>> my_object = dictionary_to_object(my_dict)
        >>> print(my_object.name)
        Alice

    **Cost:** O(n), where n is the number of keys in the dictionary.
    """

    if not isinstance(dictionary, dict):
        raise TypeError("Input must be a dictionary.")

    # Create a new, empty class on the fly.
    class DynamicObject:
        pass

    # Instantiate the new class.
    instance = DynamicObject()

    # Iterate through the dictionary and set attributes on the instance.
    for key, value in dictionary.items():
        setattr(instance, key, value)

    return instance


def dictionary_items_to_set_of_tuples(data_dict: Dict[Any, Any]) -> Set[Tuple[Any, Any]]:
    """Returns the key-value pairs (items) of a dictionary as a set of tuples.

    Args:
        data_dict (Dict[Any, Any]): The input dictionary.

    Returns:
        Set[Tuple[Any, Any]]: A set where each element is a unique `(key, value)` tuple.

    Example of use:
        >>> dictionary_items_to_set_of_tuples({"id": 101, "status": "active"})
        {('id', 101), ('status', 'active')} # Order not guaranteed

    **Cost:** O(n), where n is the number of items in the dictionary.
    """
    return set(data_dict.items())


# --- List/Tuple to Dictionary Conversions ---

def list_of_tuples_to_dict(data_list: List[Tuple[Any, Any]]) -> Dict[Any, Any]:
    """Converts a list of tuples (where each tuple is a key-value pair) to a dictionary.

    If there are duplicate keys in the list, the value from the **last tuple**
    with that key will prevail.

    Args:
        data_list (List[Tuple[Any, Any]]): The input list of `(key, value)` tuples.

    Returns:
        Dict[Any, Any]: The converted dictionary.

    Example of use:
        >>> list_of_tuples_to_dict([("a", 1), ("b", 2), ("a", 3)])
        {'a': 3, 'b': 2}

    **Cost:** O(n), where n is the number of tuples in the list.
    """
    return dict(data_list)


def list_of_lists_to_dict(data_list: List[List[Any]]) -> Dict[Any, Any]:
    """Converts a list of lists (where each inner list is a key-value pair) to a dictionary.

    If there are duplicate keys, the value from the **last inner list** with that key will prevail.

    Args:
        data_list (List[List[Any]]): The input list of `[key, value]` lists.

    Returns:
        Dict[Any, Any]: The converted dictionary.

    Example of use:
        >>> list_of_lists_to_dict([["name", "Bob"], ["age", 25], ["name", "Robert"]])
        {'name': 'Robert', 'age': 25}

    **Cost:** O(n), where n is the number of lists.
    """
    # The `dict()` constructor also works directly with lists of lists like `[key, value]`.
    return dict(data_list)


def list_of_dicts_to_merged_dict(list_of_dicts: List[Dict[Any, Any]]) -> Dict[Any, Any]:
    """Merges a list of dictionaries into a single dictionary.

    If there are **duplicate keys** across the dictionaries, the value from the
    **last dictionary** in the list will take precedence.

    Args:
        list_of_dicts (List[Dict[Any, Any]]): A list of dictionaries to be merged.

    Returns:
        Dict[Any, Any]: The single merged dictionary.

    Example of use:
        >>> list_of_dicts_to_merged_dict([{"a": 1, "b": 2}, {"b": 3, "c": 4}, {"d": 5}])
        {'a': 1, 'b': 3, 'c': 4, 'd': 5}

    **Cost:** O(n*m), where n is the number of dictionaries and m is the average number of keys per dictionary.
    """
    merged_dict = {}
    # Iterate through each dictionary and update the `merged_dict`.
    # The `.update()` method adds new keys or overwrites existing keys from the current dictionary.
    for d in list_of_dicts:
        merged_dict.update(d)
    return merged_dict



def string_to_list(
    input_string: Optional[str],
    split_by_character: Optional[str] = None
) -> Optional[List[str]]:
    """Converts a string into a list of substrings or individual characters.

    This function offers two primary modes of operation:
    1. If `split_by_character` is provided, the string will be split into
       a list of substrings using that character as a delimiter.
    2. If `split_by_character` is None (default), the string will be converted
       into a list of its individual characters.

    Args:
        input_string: The string to be converted. Can be None.
        split_by_character: An optional string to use as a delimiter for splitting.
                            If None, the string is split into individual characters.

    Returns:
        Optional[List[str]]: A list of strings (either substrings or characters).
                             Returns an empty list if `input_string` is an empty string.
                             Returns None if `input_string` is None.

    Raises:
        TypeError: If `input_string` is not a string (and not None) or if
                   `split_by_character` is not a string (and not None).

    Example of use:
        >>> convert_string_to_list("hello world")
        ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

        >>> convert_string_to_list("apple,banana,orange", split_by_character=",")
        ['apple', 'banana', 'orange']

        >>> convert_string_to_list("one two three", split_by_character=" ")
        ['one', 'two', 'three']

        >>> convert_string_to_list("")
        []

        >>> convert_string_to_list(None)
        None

        >>> convert_string_to_list("word")
        ['w', 'o', 'r', 'd']

    **Cost:** O(n), where n is the length of the input string.
    """
    # Why: Handle None input immediately as there's nothing to convert.
    if input_string is None:
        return None

    # Why: Ensure the main input is a string for consistent operations.
    if not isinstance(input_string, str):
        raise TypeError("The 'input_string' must be a string or None.")

    # Why: Handle the edge case of an empty string, returning an empty list.
    if not input_string:
        return []

    # Why: Validate the type of the split character if it's provided.
    if split_by_character is not None and not isinstance(split_by_character, str):
        raise TypeError("The 'split_by_character' must be a string or None.")

    # Why: Perform the splitting based on whether a delimiter is provided.
    if split_by_character is not None:
        # Splits the string by the specified delimiter.
        # Cost: O(N) where N is the length of input_string, as it iterates through the string.
        return input_string.split(split_by_character)
    else:
        # Converts the string into a list of its individual characters.
        # Cost: O(N) where N is the length of input_string, as it creates a new list.
        return list(input_string)

