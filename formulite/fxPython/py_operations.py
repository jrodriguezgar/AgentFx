"""
FormuLite - fxPython: Python Operations Module

This module provides advanced utility functions for Python data structure operations.
It includes functions for:
- JSON manipulation and merging
- List, tuple, and set operations (unique, flatten, intersection)
- Dictionary operations and filtering
- Subsequence and sublist checking
- Collection filtering and merging
- Command execution and expression evaluation
- Interactive user selection from collections

All functions follow PEP standards with complete documentation including
complexity analysis.
"""

import json
import sys
from collections.abc import Callable, Hashable, Iterable, Sequence
from typing import Any, List, Optional, Set, Tuple, Union
import subprocess
import re


def merge_json_strings(json_str_1: str, json_str_2: str) -> str:
    """Merges two JSON strings (representing JSON objects) into a new JSON string.

    If both JSONs contain the same keys, the values from the second JSON (json_str_2)
    will overwrite the values from the first (json_str_1).

    Args:
        json_str_1 (str): The first JSON string to merge (must represent a JSON object).
        json_str_2 (str): The second JSON string to merge (must represent a JSON object).

    Returns:
        str: A new JSON string representing the merged object.

    Raises:
        json.JSONDecodeError: If either input string is not a valid JSON.
        TypeError: If either input string does not represent a JSON object (dictionary).

    Example of use:
        >>> merge_json_strings('{"name": "Alice", "age": 30}', '{"age": 31, "city": "New York"}')
        '{"name": "Alice", "age": 31, "city": "New York"}'
        >>> merge_json_strings('{"a": 1}', '{"b": 2}')
        '{"a": 1, "b": 2}'

    **Cost:** O(n + m), where n and m are the number of keys in the two dictionaries.
    """
    try:
        # Convert the JSON strings to Python objects (dictionaries).
        obj_1 = json.loads(json_str_1)
        obj_2 = json.loads(json_str_2)
    except json.JSONDecodeError as e:
        # Re-raise with a more informative message if JSON decoding fails.
        raise json.JSONDecodeError(
            f"Error decoding input JSON: {e.msg}", e.doc, e.pos
        ) from e

    # Validate that both decoded objects are dictionaries.
    if not isinstance(obj_1, dict):
        raise TypeError(
            f"The first JSON does not represent an object (dictionary), but a {type(obj_1).__name__}."
        )
    if not isinstance(obj_2, dict):
        raise TypeError(
            f"The second JSON does not represent an object (dictionary), but a {type(obj_2).__name__}."
        )

    # Merge the two dictionaries.
    # The .copy() method is used to avoid modifying obj_1 directly.
    # The .update() method merges obj_2 into merged_obj, overwriting duplicate keys.
    merged_obj = obj_1.copy()
    merged_obj.update(obj_2)
    # Alternatively, in Python 3.9+, you could use the dictionary union operator:
    # merged_obj = obj_1 | obj_2

    # Convert the merged Python object back to a JSON string.
    # `ensure_ascii=False` is used to correctly handle non-ASCII characters in the output.
    return json.dumps(merged_obj, ensure_ascii=False)


def add_to_tuple(p_tuple: Tuple[Any, ...], p_value: Any) -> Tuple[Any, ...]:
    """Adds an element to the end of a tuple.

    Since tuples are immutable, this function creates and returns a *new* tuple
    that contains all elements from the original tuple plus the new value appended
    to the end.

    Args:
        p_tuple (Tuple[Any, ...]): The original tuple to which the element will be added.
        p_value (Any): The new value to append to the tuple.

    Returns:
        Tuple[Any, ...]: A new tuple with the value appended at the end.

    Example of use:
        >>> add_to_tuple((1, 2), 3)
        (1, 2, 3)
        >>> add_to_tuple((), "hello")
        ('hello',)

    **Cost:** O(n), where n is the number of elements in the tuple.
    """
    # The '*' operator (unpacking) expands the elements of p_tuple,
    # and p_value is added as the last element of the new tuple.
    # This is the most concise and Pythonic way to achieve this.
    return (*p_tuple, p_value)


def unique_list(p_list: List[Any]) -> List[Any]:
    """Returns a new list containing only the unique elements from the original list.

    The order of elements in the resulting list is not guaranteed, as a set
    is used internally for deduplication.

    Args:
        p_list (List[Any]): The input list which may contain duplicate elements.

    Returns:
        List[Any]: A new list containing all unique elements from the input list.

    Example of use:
        >>> unique_list([1, 2, 2, 3, 1])
        [1, 2, 3] # Order may vary
        >>> unique_list(["apple", "banana", "apple"])
        ['banana', 'apple'] # Order may vary

    **Cost:** O(n), where n is the number of elements in the list.
    """
    # Convert the list to a set to remove duplicates. Sets inherently do not allow duplicate elements.
    # Then, convert the set back to a list.
    return list(set(p_list))


def unique_tuple_list(p_list: list[tuple]) -> list[tuple]:
    """
    Removes duplicate tuples from a list based on the first element of each tuple.
    Returns a new list containing only the unique tuples.

    Args:
        p_list (list[tuple]): The input list of tuples. Each tuple must have at least one element.

    Returns:
        list[tuple]: A new list containing the unique tuples, maintaining the order
                     of their first appearance in the original list.

    Example usage:
        my_tuples = [(1, 'apple'), (2, 'banana'), (1, 'orange'), (3, 'grape'), (2, 'kiwi')]
        unique_list = unique_tuple_list(my_tuples)
        # unique_list will be [(1, 'apple'), (2, 'banana'), (3, 'grape')]
        # Cost: O(n) on average, where n is the number of tuples in p_list,
        # due to set lookups and list appends.
    """
    # Use a set to keep track of the first elements (keys) that have already been seen.
    # Sets provide O(1) average-case time complexity for 'in' operations and additions,
    # which is crucial for efficient duplicate checking.
    seen_keys = set()
    
    # This list will store the filtered unique tuples, preserving order.
    filtered_list = []

    for current_tuple in p_list:
        # The key for uniqueness is the first element of the tuple.
        key = current_tuple[0]
        
        # Check if this key has been encountered before.
        if key not in seen_keys:
            # If the key is new, add it to the set of seen keys.
            seen_keys.add(key)
            # And append the entire tuple to our filtered list.
            # We add the entire tuple because the requirement is to return the unique tuple.
            filtered_list.append(current_tuple)

    return filtered_list


def flatten_list(p_list: list[list]) -> list:
    """Flattens a list of lists into a single, one-dimensional list.

    Delegates to :func:`~formulite.fxPython.py_itertools.flatten`.

    Args:
        p_list (list[list]): The input list of lists.

    Returns:
        list: A new list containing all elements from the sublists.

    Example of use:
        >>> flatten_list([[1, 2, 3], [4, 5], [6]])
        [1, 2, 3, 4, 5, 6]

    Cost: O(n), where n is the total number of elements across all sublists.
    """
    from formulite.fxPython.py_itertools import flatten

    return list(flatten(p_list))


def list_intersection(p_list1: list, p_list2: list) -> set:
    """
    Finds the intersection of two lists, returning a set of common elements.
    It first filters out any falsy values (e.g., None, 0, '') from the input lists.

    Args:
        p_list1 (list): The first input list.
        p_list2 (list): The second input list.

    Returns:
        set: A set containing elements that are present in both filtered lists.

    Example usage:
        list_a = [1, 2, None, 3, 4, 0, 5]
        list_b = [3, 4, 5, 6, '', 7]
        common_elements = list_intersection(list_a, list_b)
        # common_elements will be {3, 4, 5}
        # Cost: O(n + m) on average, where n and m are the lengths of p_list1 and p_list2,
        # due to list comprehensions and set conversions/intersection.
    """
    # Filter out falsy values from both input lists.
    # A list comprehension is used for clarity and efficiency in creating new lists
    # that only contain truthy elements.
    filtered_list1 = [item for item in p_list1 if item]
    filtered_list2 = [item for item in p_list2 if item]

    # Convert the filtered lists to sets.
    # This is done because set operations (like intersection) are highly optimized
    # for O(1) average-case time complexity per element, making the intersection
    # much faster than iterating through lists.
    set1 = set(filtered_list1)
    set2 = set(filtered_list2)

    # Return the intersection of the two sets.
    # The intersection method returns a new set with elements common to both sets.
    return set1.intersection(set2)


def list_has_list(container_list: list, search_list: list) -> bool:
    """Checks if all elements from one list exist in another list, regardless of order.

    Problem/User Need: When comparing lists, it's often necessary to verify if all 
    elements from one list exist in another list, without considering their order 
    or position.

    Args:
        container_list (list): The larger list to search within.
        search_list (list): The list whose elements we want to find.

    Returns:
        bool: True if all elements in search_list exist in container_list,
              False otherwise.

    Raises:
        TypeError: If either argument is not a list.
        ValueError: If either list is empty.

    Example:
        >>> list_has_list(['a', 'b', 'c', 'd'], ['b', 'c'])
        True
        >>> list_has_list(['a', 'b', 'c'], ['b', 'd'])
        False
        >>> list_has_list([1, 2, 3, 4], [2, 1])
        True
        >>> list_has_list([], [1, 2])
        ValueError: Lists cannot be empty
    
    Cost:
        Time complexity: O(n * m) where n and m are the lengths of the lists
        Space complexity: O(1) as we only use set operations
    """
    # Input validation
    if not isinstance(container_list, list) or not isinstance(search_list, list):
        raise TypeError("Both arguments must be lists")
    
    if not container_list or not search_list:
        raise ValueError("Lists cannot be empty")

    # Convert container_list to set for O(1) lookup
    container_set = set(container_list)
    
    # Check if each element in search_list exists in container_set
    return all(item in container_set for item in search_list)


def is_subsequence(sub_sequence: Sequence[Hashable], main_sequence: Sequence[Hashable]) -> bool:
    """
    Checks if 'sub_sequence' is a subsequence of 'main_sequence', maintaining the order of elements.

    This function works correctly for ordered sequence types like lists and tuples.
    It does not logically apply to unordered collections like sets, as the concept of
    "order" is not defined for them. If you need to check element presence
    without regard to order in sets, consider checking if one set is a subset of another.

    Args:
        sub_sequence: The potential subsequence (e.g., a list or a tuple).
        main_sequence: The main sequence to check against (e.g., a list or a tuple).
                       Elements within the sequences should be hashable for efficient
                       searching if the underlying implementation uses hashing.

    Returns:
        True if 'sub_sequence' is a subsequence of 'main_sequence', False otherwise.

    # --- Examples with Lists ---
    list1_sub = ["apple", "banana"]
    list1_main = ["orange", "apple", "grape", "banana", "kiwi"]
    print(f"Is {list1_sub} a subsequence of {list1_main}? {is_subsequence(list1_sub, list1_main)}") # Expected: True

    list2_sub = ["banana", "apple"]
    list2_main = ["orange", "apple", "grape", "banana", "kiwi"]
    print(f"Is {list2_sub} a subsequence of {list2_main}? {is_subsequence(list2_sub, list2_main)}") # Expected: False (order matters)

    list3_sub = ["apple", "kiwi", "melon"]
    list3_main = ["orange", "apple", "grape", "banana", "kiwi"]
    print(f"Is {list3_sub} a subsequence of {list3_main}? {is_subsequence(list3_sub, list3_main)}") # Expected: False (melon not found)

    # --- Examples with Tuples ---
    tuple1_sub = (1, 3)
    tuple1_main = (0, 1, 2, 3, 4, 5)
    print(f"Is {tuple1_sub} a subsequence of {tuple1_main}? {is_subsequence(tuple1_sub, tuple1_main)}") # Expected: True

    tuple2_sub = ('b', 'a')
    tuple2_main = ('a', 'b', 'c')
    print(f"Is {tuple2_sub} a subsequence of {tuple2_main}? {is_subsequence(tuple2_sub, tuple2_main)}") # Expected: False (order matters)

    # --- Examples with Empty Sequences ---
    empty_sub = []
    any_main = ["a", "b", "c"]
    print(f"Is {empty_sub} a subsequence of {any_main}? {is_subsequence(empty_sub, any_main)}") # Expected: True

    non_empty_sub = ["a"]
    empty_main = []
    print(f"Is {non_empty_sub} a subsequence of {empty_main}? {is_subsequence(non_empty_sub, empty_main)}") # Expected: False
        
    """

    # If sub_sequence is empty, it's always a subsequence of any main_sequence
    if not sub_sequence:
        return True

    # If sub_sequence is longer than main_sequence, it cannot be a subsequence
    if len(sub_sequence) > len(main_sequence):
        return False

    main_index = -1  # Start looking from the beginning of main_sequence
    for element in sub_sequence:
        found = False
        # Search for 'element' in main_sequence starting from 'main_index + 1'
        for i in range(main_index + 1, len(main_sequence)):
            if main_sequence[i] == element:
                main_index = i  # Update the index to the current position of the found element
                found = True
                break  # Move to the next element in sub_sequence
        if not found:
            return False  # If an element is not found, it's not a subsequence

    return True  # All elements in sub_sequence were found in order


def filter_elements_by_another(
    main_collection: Iterable, 
    filter_criteria: Iterable, 
    return_type: str = "list"
) -> Union[list, tuple, set]:
    """Filters elements from a main collection that are also present in a filter criteria collection.

    This function is highly flexible, accepting lists, tuples, or sets as input for both
    `main_collection` and `filter_criteria`. It efficiently identifies common elements
    and returns them in the specified output type (list, tuple, or set).

    Args:
        main_collection (Iterable): The collection (list, tuple, or set) from which elements will be filtered.
        filter_criteria (Iterable): The collection (list, tuple, or set) containing elements to use as a filter.
        return_type (str, optional): The desired type of the returned collection.
                                     Accepted values are "list", "tuple", or "set".
                                     Defaults to "list".

    Returns:
        Union[list, tuple, set]: A new collection of the specified `return_type`
                                 containing only the elements from `main_collection` that are
                                 present in `filter_criteria`.

    Raises:
        TypeError: If `main_collection` or `filter_criteria` is not a recognized iterable type (list, tuple, set).
        ValueError: If `return_type` is not one of "list", "tuple", or "set".

    Example of use:
        >>> my_set = {1, 2, 3, 4, 5}
        >>> filter_list = [2, 4, 6]
        >>> filter_elements_by_another(my_set, filter_list, return_type="set")
        {2, 4}

        >>> data_tuple = ("a", "b", "c", "d")
        >>> criteria_set = {"b", "d", "e"}
        >>> filter_elements_by_another(data_tuple, criteria_set, return_type="list")
        ['b', 'd']

        >>> list_numbers = [10, 20, 30, 20, 40]
        >>> common_values = {20, 50}
        >>> filter_elements_by_another(list_numbers, common_values, return_type="tuple")
        (20, 20)
    """
    # Input type validation for main_collection and filter_criteria
    valid_input_types = (list, tuple, set)
    if not isinstance(main_collection, valid_input_types):
        raise TypeError(f"'main_collection' must be a list, tuple, or set, not {type(main_collection).__name__}.")
    if not isinstance(filter_criteria, valid_input_types):
        raise TypeError(f"'filter_criteria' must be a list, tuple, or set, not {type(filter_criteria).__name__}.")

    # Validate the requested return_type
    valid_return_types = {"list", "tuple", "set"}
    if return_type not in valid_return_types:
        raise ValueError(f"Invalid 'return_type'. Expected one of {', '.join(valid_return_types)}, got '{return_type}'.")

    # Convert the filter_criteria to a set for O(1) average time complexity lookups.
    # This is crucial for performance, especially with large collections.
    filter_set = set(filter_criteria)

    # Use a list comprehension to build an intermediate list of filtered elements.
    # This ensures consistent processing before converting to the final desired type.
    filtered_elements_list = [element for element in main_collection if element in filter_set]

    # Convert the intermediate list to the specified return_type
    if return_type == "list":
        return filtered_elements_list
    elif return_type == "tuple":
        return tuple(filtered_elements_list)
    elif return_type == "set":
        # Converting to a set will automatically handle uniqueness
        return set(filtered_elements_list)


def merge_elements(
    first_collection: Iterable,
    second_collection: Iterable,
    return_type: str = "list",
    remove_duplicates: bool = False
) -> Union[list, tuple, set]:
    """Merges two collections into a single collection of the specified type.

    This function is highly flexible, accepting lists, tuples, or sets as input for both
    collections. It combines all elements from both collections and returns them in the
    specified output type (list, tuple, or set).

    Args:
        first_collection (Iterable): The first collection (list, tuple, or set) to merge.
        second_collection (Iterable): The second collection (list, tuple, or set) to merge.
        return_type (str, optional): The desired type of the returned collection.
                                     Accepted values are "list", "tuple", or "set".
                                     Defaults to "list".
        remove_duplicates (bool, optional): If True, removes duplicate elements from the merged result.
                                           Only applicable when return_type is "list" or "tuple".
                                           Defaults to False.

    Returns:
        Union[list, tuple, set]: A new collection of the specified `return_type`
                                 containing all elements from both input collections.

    Raises:
        TypeError: If `first_collection` or `second_collection` is not a recognized iterable type (list, tuple, set).
        ValueError: If `return_type` is not one of "list", "tuple", or "set".

    Example of use:
        >>> list_a = [1, 2, 3]
        >>> list_b = [4, 5, 6]
        >>> merge_elements(list_a, list_b, return_type="list")
        [1, 2, 3, 4, 5, 6]

        >>> tuple_a = ("a", "b", "c")
        >>> set_b = {"c", "d", "e"}
        >>> merge_elements(tuple_a, set_b, return_type="tuple")
        ('a', 'b', 'c', 'c', 'd', 'e')

        >>> list_a = [1, 2, 2, 3]
        >>> list_b = [3, 4, 4, 5]
        >>> merge_elements(list_a, list_b, return_type="list", remove_duplicates=True)
        [1, 2, 3, 4, 5]

        >>> set_a = {1, 2, 3}
        >>> set_b = {3, 4, 5}
        >>> merge_elements(set_a, set_b, return_type="set")
        {1, 2, 3, 4, 5}

    Cost:
        O(n + m) where n and m are the lengths of the input collections.
        If remove_duplicates is True and return_type is not "set", the cost becomes
        O(n + m) for creating a set and then converting back.
    """
    # Input type validation for first_collection and second_collection
    valid_input_types = (list, tuple, set)
    if not isinstance(first_collection, valid_input_types):
        raise TypeError(f"'first_collection' must be a list, tuple, or set, not {type(first_collection).__name__}.")
    if not isinstance(second_collection, valid_input_types):
        raise TypeError(f"'second_collection' must be a list, tuple, or set, not {type(second_collection).__name__}.")

    # Validate the requested return_type
    valid_return_types = {"list", "tuple", "set"}
    if return_type not in valid_return_types:
        raise ValueError(f"Invalid 'return_type'. Expected one of {', '.join(valid_return_types)}, got '{return_type}'.")

    # Merge the collections by converting both to lists and concatenating them.
    # This approach preserves order and handles all iterable types uniformly.
    # Cost: O(n + m) where n and m are the lengths of the collections.
    merged_list = list(first_collection) + list(second_collection)

    # Handle duplicate removal if requested
    if remove_duplicates and return_type != "set":
        # Convert to set to remove duplicates, then back to list.
        # Note: This may not preserve the original order in Python < 3.7,
        # but in Python 3.7+ dictionaries maintain insertion order, and
        # dict.fromkeys() can be used to preserve order while removing duplicates.
        merged_list = list(dict.fromkeys(merged_list))

    # Convert the merged list to the specified return_type
    if return_type == "list":
        return merged_list
    elif return_type == "tuple":
        return tuple(merged_list)
    elif return_type == "set":
        # Converting to a set will automatically handle uniqueness
        return set(merged_list)
    

def pick_in_collection(
    collection: Iterable,
    prompt: str = "Por favor, selecciona una opción:",
    allow_multiple: bool = False,
    return_index: bool = False,
    exit_on_cancel: bool = False
) -> Union[Any, List[Any], int, List[int], None]:
    """
    Permite al usuario seleccionar una o varias opciones de cualquier colección iterable numerada.

    Args:
        collection (Iterable): Una colección de elementos (lista, tupla, conjunto, etc.)
                               de los que el usuario puede elegir.
                               Los elementos pueden ser de cualquier tipo (cadenas, números, objetos, etc.).
        prompt (str, opcional): El mensaje que se mostrará al usuario antes de la lista de opciones.
                                Por defecto: "Por favor, selecciona una opción:".
        allow_multiple (bool, opcional): Si es True, el usuario puede seleccionar múltiples opciones
                                          separadas por comas (ej. "1,3,5"). Por defecto es False.
        return_index (bool, opcional): Si es True, la función devuelve el/los índice/s (basado en 0)
                                        de la/s opción/es en la lista interna creada a partir de la colección.
                                        Si es False, devuelve el/los valor/es de la/s opción/es.
                                        Por defecto es False.
        exit_on_cancel (bool, opcional): Si es True, el programa terminará si el usuario introduce
                                          'q' o 'cancelar'. Por defecto es False.

    Returns:
        any | list[any] | int | list[int] | None:
            - El elemento seleccionado (si allow_multiple es False).
            - Una lista de elementos seleccionados (si allow_multiple es True).
            - El índice del elemento seleccionado (si return_index es True y allow_multiple es False).
            - Una lista de índices (si return_index es True y allow_multiple es True).
            - None si el usuario cancela (introduce 'q' o 'cancelar') y exit_on_cancel es False.

    Raises:
        TypeError: Si la 'collection' proporcionada no es iterable.
        ValueError: Si la 'collection' está vacía.

    Ejemplos de uso:
        >>> colores_tuple = ("Rojo", "Verde", "Azul", "Amarillo")
        >>> color_elegido = pick_in_collection(colores_tuple, "Elige tu color favorito:")
        >>> print(f"Has elegido: {color_elegido}")

        >>> numeros_set = {10, 20, 30, 40, 50}
        >>> numeros_elegidos = pick_in_collection(numeros_set, "Elige algunos números:", allow_multiple=True)
        >>> print(f"Has elegido: {numeros_elegidos}")

        >>> texto_generator = (f"Item {i}" for i in range(1, 6))
        >>> item_elegido = pick_in_collection(texto_generator, "Selecciona un ítem del generador:", return_index=True)
        >>> print(f"El índice del ítem elegido es: {item_elegido}")
    """

    if not isinstance(collection, Iterable):
        raise TypeError("El argumento 'collection' debe ser un iterable (e.g., lista, tupla, conjunto).")

    # Convertir el iterable a una lista para asegurar un orden y permitir el acceso por índice.
    # Esto también consume generadores.
    options_list = list(collection)

    if not options_list:
        raise ValueError("La colección de opciones no puede estar vacía después de la conversión a lista.")

    while True:
        print(f"\n{prompt}")
        for i, option in enumerate(options_list):
            print(f"  {i + 1}. {option}")

        if allow_multiple:
            input_msg = "Introduce los números de las opciones (separados por comas), o 'q' para cancelar: "
        else:
            input_msg = "Introduce el número de la opción, o 'q' para cancelar: "

        user_input = input(input_msg).strip().lower()

        if user_input in ('q', 'cancelar'):
            if exit_on_cancel:
                print("Operación cancelada. Saliendo del programa.")
                sys.exit(0)  # Termina el programa
            else:
                print("Operación cancelada.")
                return None

        try:
            if allow_multiple:
                selected_indices = []
                input_parts = [part.strip() for part in user_input.split(',')]
                
                if not input_parts or any(not part.isdigit() for part in input_parts):
                    raise ValueError("Entrada inválida. Por favor, introduce números enteros separados por comas.")

                for part in input_parts:
                    choice_num = int(part)
                    if not (1 <= choice_num <= len(options_list)):
                        raise ValueError(f"El número {choice_num} está fuera de rango. Por favor, introduce un número entre 1 y {len(options_list)}.")
                    selected_indices.append(choice_num - 1) # Convertir a índice basado en 0
                
                # Eliminar duplicados y ordenar para consistencia si es necesario
                selected_indices = sorted(list(set(selected_indices)))

                if return_index:
                    return selected_indices
                else:
                    return [options_list[idx] for idx in selected_indices]
            else:
                choice_num = int(user_input)
                if not (1 <= choice_num <= len(options_list)):
                    raise ValueError(f"El número {choice_num} está fuera de rango. Por favor, introduce un número entre 1 y {len(options_list)}.")

                selected_index = choice_num - 1 # Convertir a índice basado en 0

                if return_index:
                    return selected_index
                else:
                    return options_list[selected_index]
        except ValueError as e:
            print(f"Entrada inválida: {e}. Por favor, inténtalo de nuevo.")
        except Exception as e:
            print(f"Ha ocurrido un error inesperado: {e}. Por favor, inténtalo de nuevo.")


def collection_filter(
    collection: Iterable[Any],
    filter_logic_func: Callable[[Any], bool]
) -> Union[List[Any], Tuple[Any, ...], Set[Any]]:
    """
    Filters an iterable (list, tuple, set, etc.) based on a provided filtering function.

    Args:
        collection: The iterable to filter (e.g., a list, tuple, or set).
        filter_logic_func: A callable (function) that takes a single item from the
            collection as input and returns True if the item should be included
            in the filtered result, False otherwise.

    Returns:
        A new collection of the same type as the input (list, tuple, or set)
        containing only the items for which filter_logic_func returned True.

    Raises:
        TypeError: If 'collection' is not an iterable or 'filter_logic_func' is not callable.

    Example of use:
        >>> numbers = [1, 2, 3, 4, 5, 6]
        >>> is_even = lambda x: x % 2 == 0
        >>> collection_filter(numbers, is_even)
        [2, 4, 6]

        >>> data_tuple = (10, 15, 20, 25)
        >>> is_greater_than_20 = lambda x: x > 20
        >>> collection_filter(data_tuple, is_greater_than_20)
        (25,)

        >>> unique_letters = {'a', 'b', 'c', 'd'}
        >>> is_vowel = lambda x: x in 'aeiou'
        >>> collection_filter(unique_letters, is_vowel)
        {'a'}
    """
    # Validate inputs to ensure they are of the expected types.
    # This helps catch errors early and provides clear feedback.
    if not isinstance(collection, Iterable):
        raise TypeError("Input 'collection' must be an iterable (e.g., list, tuple, set).")
    if not callable(filter_logic_func):
        raise TypeError("Input 'filter_logic_func' must be a callable function.")

    # Convert the filtered results to the original collection type.
    # This avoids redundant type checks and ensures type consistency.
    filtered_items = [item for item in collection if filter_logic_func(item)]

    # Return the filtered items, cast to the original collection's type.
    # This is more concise than multiple if/elif branches for type conversion.
    if isinstance(collection, list):
        return filtered_items
    elif isinstance(collection, tuple):
        return tuple(filtered_items)
    elif isinstance(collection, set):
        return set(filtered_items)
    else:
        # Default to a list if the collection type is not explicitly handled.
        # This makes the function more flexible for various iterable types.
        return filtered_items
    

def dictionary_filter_by_keys(input_dict: dict, keys_to_include: list) -> dict:
    """Filters a dictionary, returning a new dictionary with only the specified keys.

    This function iterates through a provided list of keys and creates a new dictionary
    containing only the key-value pairs where the key exists in the original dictionary.
    This is highly useful for preparing a subset of data for serialization or other
    processing.

    Args:
        input_dict (dict): The original dictionary to filter.
        keys_to_include (list): A list of keys (strings) that should be included
                                 in the new, filtered dictionary.

    Returns:
        dict: A new dictionary containing only the key-value pairs
              corresponding to the `keys_to_include`.

    Raises:
        TypeError: If input_dict is not a dictionary or keys_to_include is not a list.

    Example of use:
        original_data = {"name": "Charlie", "age": 45, "city": "London", "email": "charlie@example.com"}
        desired_keys = ["name", "city", "country"] # 'country' is not in original_data

        filtered_data = dictionary_filter_by_keys(original_data, desired_keys)
        print(f"Filtered data: {filtered_data}")
        # Expected output: {'name': 'Charlie', 'city': 'London'}

        # This output can now be passed to our JSON conversion functions:
        # from your_module import any_to_json_string # Assuming it's in a module
        # json_string = any_to_json_string(filtered_data, indent=2)
        # print(json_string)
    """
    if not isinstance(input_dict, dict):
        #raise TypeError("Input 'input_dict' must be a dictionary.")
        return None
    
    if not isinstance(keys_to_include, list):
        #raise TypeError("Input 'keys_to_include' must be a list of strings.")
        return None

    # A dictionary comprehension is the most Pythonic and efficient way to build
    # a new dictionary from an existing one based on certain conditions.
    # It ensures only the requested keys that are present in the input_dict are included.
    # Cost: O(M) where M is the number of keys in `keys_to_include`.
    # In the worst case, M could be equal to the number of keys in `input_dict`.
    filtered_dict = {key: input_dict[key] for key in keys_to_include if key in input_dict}

    return filtered_dict


def combine_dictionaries(dict_one: dict, dict_two: dict, operation: str) -> dict:
    """
    Performs union or intersection operations on two dictionaries.

    This function takes two dictionaries and an operation type ('union' or 'intersection')
    to return a new dictionary based on the specified operation.

    Args:
        dict_one (dict): The first dictionary.
        dict_two (dict): The second dictionary.
        operation (str): The type of operation to perform. Must be 'union' or 'intersection'.

    Returns:
        dict: A new dictionary resulting from the specified operation.

    Raises:
        ValueError: If an unsupported operation type is provided.

    Example of use:
        dict_a = {'a': 1, 'b': 2, 'c': 3}
        dict_b = {'b': 4, 'd': 5}

        union_result = combine_dictionaries(dict_a, dict_b, 'union')
        # Expected: {'a': 1, 'b': 4, 'c': 3, 'd': 5}

        intersection_result = combine_dictionaries(dict_a, dict_b, 'intersection')
        # Expected: {'b': 4}

    Cost:
        O(N + M) for union (where N and M are the number of items in dict_one and dict_two respectively)
        O(min(N, M)) for intersection (iterating over the smaller dictionary's keys)
    """
    # Ensure the operation type is valid before proceeding.
    if operation not in ['union', 'intersection']:
        raise ValueError("Unsupported operation. Choose 'union' or 'intersection'.")

    if operation == 'union':
        # The union operation leverages dictionary unpacking.
        # This creates a new dictionary by first unpacking dict_one,
        # and then unpacking dict_two. If there are common keys,
        # the values from dict_two will overwrite those from dict_one,
        # which aligns with the definition of dictionary union in this context.
        return {**dict_one, **dict_two}
    else:  # operation == 'intersection'
        result_dict = {}
        # Iterate over the keys of the first dictionary.
        # This is generally efficient for finding common keys.
        for key, value in dict_one.items():
            # If a key exists in both dictionaries, add it to the result.
            # We take the value from dict_two for consistency, similar to how
            # union handles overwrites.
            if key in dict_two:
                result_dict[key] = dict_two[key]
        return result_dict
    
    
def dictionary_rename_keys(original_dict: dict, key_mapping: dict) -> dict:
    """Renames keys in a dictionary based on a provided mapping.

    This function iterates through the original dictionary's items. If a key
    exists in the `key_mapping`, its corresponding value from the mapping is
    used as the new key in the new dictionary. Keys not found in the mapping
    are kept as is. This approach creates a new dictionary, leaving the
    original dictionary unchanged.

    Args:
        original_dict: The dictionary whose keys are to be renamed.
        key_mapping: A dictionary where keys are old key names and values are
                     the new key names.

    Returns:
        A new dictionary with the keys renamed according to the `key_mapping`.

    Raises:
        TypeError: If `original_dict` or `key_mapping` are not dictionaries.

    Example of use:
        >>> my_dict = {"name": "Alice", "age": 30}
        >>> mapping = {"name": "full_name", "age": "person_age"}
        >>> renamed_dict = dictionary_rename_keys(my_dict, mapping)
        >>> print(renamed_dict)
        {'full_name': 'Alice', 'person_age': 30}
    """
    if not isinstance(original_dict, dict):
        raise TypeError("The 'original_dict' argument must be a dictionary.")
    if not isinstance(key_mapping, dict):
        raise TypeError("The 'key_mapping' argument must be a dictionary.")

    # Create a new dictionary to store the renamed keys and their values.
    # We do this to avoid modifying the dictionary while iterating over it,
    # which can lead to unexpected behavior or errors.
    renamed_dict = {}

    # Iterate over each key-value pair in the original dictionary.
    # This loop has a time complexity of O(n), where n is the number of
    # items in the original dictionary.
    for original_key, value in original_dict.items():
        # Check if the original key exists in our mapping.
        # Dictionary lookups are, on average, O(1).
        if original_key in key_mapping:
            # If a mapping exists, use the new key from the mapping.
            new_key = key_mapping[original_key]
            renamed_dict[new_key] = value
        else:
            # If no mapping exists, keep the original key.
            renamed_dict[original_key] = value

    return renamed_dict


def execute_os_command(command: Union[str, list[str]]) -> Tuple[int, str, str]:
    """
    Executes a command in the underlying operating system and captures its output.

    This function provides a secure and flexible way to interact with the shell
    or directly execute programs. It uses `subprocess.Popen` for fine-grained control
    and is generally preferred over `os.system` for security and functionality.

    Args:
        command (Union[str, list[str]]): The command to execute.
            - If a string, it will be executed via the shell (e.g., 'ls -l', 'dir').
              Be cautious with user-provided input when `shell=True` due to security risks.
            - If a list of strings, it will be executed directly without a shell
              (e.g., ['ls', '-l'], ['cmd.exe', '/c', 'dir']). This is safer for
              commands constructed from untrusted input.

    Returns:
        Tuple[int, str, str]: A tuple containing:
            - int: The return code of the command (0 typically indicates success).
            - str: The standard output (stdout) of the command as a string.
            - str: The standard error (stderr) of the command as a string.

    Raises:
        TypeError: If the 'command' argument is not a string or a list of strings.
        subprocess.CalledProcessError: If the command returns a non-zero exit status
                                      and `check=True` (though not used directly here,
                                      it's good to be aware of this common subprocess error).
        FileNotFoundError: If the command or executable specified is not found.
        # Other subprocess-related exceptions can occur (e.g., PermissionError)

    Example of use:
        >>> # Example 1: Listing directory contents (shell=True for simplicity, but be careful!)
        >>> return_code, stdout, stderr = execute_os_command("ls -l" if os.name == 'posix' else "dir")
        >>> print(f"Return Code: {return_code}")
        >>> print("STDOUT:")
        >>> print(stdout)
        >>> if stderr:
        >>>     print("STDERR:")
        >>>     print(stderr)

        >>> # Example 2: Running a command without shell (safer for user input)
        >>> # On Linux/macOS:
        >>> # return_code, stdout, stderr = execute_os_command(["echo", "Hello from Python!"])
        >>> # On Windows:
        >>> # return_code, stdout, stderr = execute_os_command(["cmd.exe", "/c", "echo", "Hello from Python!"])
        >>> # print(f"Return Code: {return_code}")
        >>> # print("STDOUT:")
        >>> # print(stdout)

        >>> # Example 3: Command with an error
        >>> # return_code, stdout, stderr = execute_os_command("nonexistent_command")
        >>> # print(f"Return Code: {return_code}")
        >>> # print("STDOUT:")
        >>> # print(stdout)
        >>> # print("STDERR:")
        >>> # print(stderr)
    """
    if not isinstance(command, (str, list)):
        raise TypeError("The 'command' argument must be a string or a list of strings.")
    if isinstance(command, list) and not all(isinstance(item, str) for item in command):
        raise TypeError("If 'command' is a list, all its elements must be strings.")

    # Determine if shell should be used. Using shell=True for string commands is common
    # but also carries security implications if 'command' originates from untrusted user input.
    # For list commands, shell=False is the default and generally safer.
    use_shell = isinstance(command, str)

    try:
        # subprocess.run is the high-level interface recommended for most cases.
        # It runs the command, waits for it to complete, and then returns a CompletedProcess object.
        # capture_output=True ensures stdout and stderr are captured.
        # text=True decodes stdout/stderr as text using default encoding (or specified encoding).
        # check=False means it will not raise an exception for non-zero exit codes;
        #            instead, the return code is provided in the result.
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,  # Decode output as text (uses default encoding, e.g., UTF-8)
            shell=use_shell,
            check=False # Do not raise CalledProcessError for non-zero exit codes
        )

        return result.returncode, result.stdout.strip(), result.stderr.strip()

    except FileNotFoundError:
        # This occurs if the command itself (the executable) is not found in the system's PATH.
        return 127, "", "Error: Command not found." # Common exit code for command not found

    except Exception as e:
        # Catch other potential errors during process execution (e.g., permissions)
        return 1, "", f"An unexpected error occurred: {e}"
    

def calculate(expression_string):
    """Evaluates a compound arithmetic expression from a string.

    Handles implicit multiplication (e.g. ``3(4+2)`` → ``3*(4+2)``), then
    delegates to :func:`~formulite.fxNumeric.calculator_functions.evaluate_expression`
    for safe AST-based evaluation.

    Args:
        expression_string (str): The mathematical expression to be evaluated.

    Returns:
        int | float: The numerical result of the expression.

    Raises:
        ValueError: If the expression is syntactically incorrect or invalid.

    Example of use:
        >>> calculate("3 + 4 * 5")
        23
        >>> calculate("2 * 3(6 / 2) - 9 + 6")
        15.0

    Cost: O(n) where n is the expression length.
    """
    # Expand implicit multiplication before delegating.
    processed_string = re.sub(r'(?<=[0-9\)])\s*\(', '*(', expression_string)

    from formulite.fxNumeric.calculator_functions import evaluate_expression

    return evaluate_expression(processed_string)


def search(collection: Iterable[Any], target_element: Any) -> Optional[Any]:
    """
    Searches for a target element within an iterable collection.

    This function iterates through the provided collection to find the first
    occurrence of the `target_element`. It is designed to work with any
    iterable, such as lists, tuples, sets, and generators.

    Args:
        collection (Iterable[Any]): The collection to be searched.
        target_element (Any): The element to search for.

    Returns:
        Optional[Any]: The found element, or `None` if the element is not found.
        The return type is `Optional[Any]` to clearly indicate that the function
        might not return an element.

    Raises:
        TypeError: If the provided `collection` is not an iterable.

    Example of use:
        >>> my_list = [1, 2, 3, 4, 5]
        >>> search(my_list, 3)
        3
        >>> search(my_list, 6)
        None

    Cost:
        The time complexity is O(N) in the worst-case scenario, where N is the
        number of elements in the collection, as it may need to check every
        element. In the best case, it is O(1) if the element is the first in
        the collection. The space complexity is O(1) as no extra storage is
        needed.
    """
    if not isinstance(collection, Iterable):
        # We raise a TypeError because the function requires an iterable
        # to operate correctly. This helps in early error detection.
        raise TypeError("The 'collection' argument must be an iterable.")

    for element in collection:
        if element == target_element:
            return element
            # The loop terminates immediately upon finding the element,
            # which is an efficient way to handle the search.

    # If the loop completes without finding the element, we return None
    # to signal that the search was unsuccessful.
    return None


def collection_avg(collection: Iterable[Union[int, float]], ignore_none: bool = True) -> Optional[float]:
    """
    Calculates the average of the numeric values in an iterable collection.

    This function is equivalent to the SQL aggregate function AVG and allows
    calculating the average of numeric values in any iterable collection.

    Args:
        collection (Iterable[Union[int, float]]): Collection of numeric values.
        ignore_none (bool): If True, ignores None values in the calculation.
                           Defaults to True.

    Returns:
        Optional[float]: The average of the values, or None if the collection is empty
                        or contains no valid values.

    Raises:
        TypeError: If the collection is not iterable or contains non-numeric values.

    Example of use:
        >>> collection_avg([1, 2, 3, 4, 5])
        3.0
        >>> collection_avg([10, 20, None, 30], ignore_none=True)
        20.0
        >>> collection_avg((5.5, 10.5, 15.5))
        10.5

    **Cost:** O(n), where n is the number of elements in the collection.
    """
    if not isinstance(collection, Iterable):
        raise TypeError("The 'collection' argument must be an iterable.")

    values = []
    for item in collection:
        if item is None and ignore_none:
            continue
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be numeric. Found: {type(item).__name__}")
        values.append(item)

    if not values:
        return None

    return sum(values) / len(values)


def collection_count(collection: Iterable[Any], ignore_none: bool = True) -> int:
    """
    Counts the number of elements in an iterable collection.

    This function is equivalent to the SQL aggregate function COUNT and allows
    counting elements in any iterable collection, with an option to ignore None values.

    Args:
        collection (Iterable[Any]): The collection to count.
        ignore_none (bool): If True, does not count None values.
                           Defaults to True (similar to COUNT(field) in SQL).

    Returns:
        int: The number of elements in the collection.

    Raises:
        TypeError: If the argument is not an iterable.

    Example of use:
        >>> collection_count([1, 2, 3, 4, 5])
        5
        >>> collection_count([1, None, 3, None, 5], ignore_none=True)
        3
        >>> collection_count([1, None, 3, None, 5], ignore_none=False)
        5

    **Cost:** O(n), where n is the number of elements in the collection.
    """
    if not isinstance(collection, Iterable):
        raise TypeError("The 'collection' argument must be an iterable.")

    if ignore_none:
        return sum(1 for item in collection if item is not None)
    else:
        return sum(1 for _ in collection)


def collection_max(collection: Iterable[Any], ignore_none: bool = True) -> Optional[Any]:
    """
    Returns the highest value in an iterable collection.

    This function is equivalent to the SQL aggregate function MAX and allows
    finding the maximum value in any iterable collection.

    Args:
        collection (Iterable[Any]): The collection to search for the maximum.
        ignore_none (bool): If True, ignores None values in the calculation.
                           Defaults to True.

    Returns:
        Optional[Any]: The maximum value in the collection, or None if it is empty
                      or contains only None.

    Raises:
        TypeError: If the collection is not iterable.
        ValueError: If the collection is empty after filtering None.

    Example of use:
        >>> collection_max([1, 5, 3, 9, 2])
        9
        >>> collection_max(['apple', 'zebra', 'banana'])
        'zebra'
        >>> collection_max([1.5, None, 3.7, 2.1], ignore_none=True)
        3.7

    **Cost:** O(n), where n is the number of elements in the collection.
    """
    if not isinstance(collection, Iterable):
        raise TypeError("The 'collection' argument must be an iterable.")

    if ignore_none:
        filtered_values = [item for item in collection if item is not None]
    else:
        filtered_values = list(collection)

    if not filtered_values:
        return None

    return max(filtered_values)


def collection_min(collection: Iterable[Any], ignore_none: bool = True) -> Optional[Any]:
    """
    Returns the smallest value in an iterable collection.

    This function is equivalent to the SQL aggregate function MIN and allows
    finding the minimum value in any iterable collection.

    Args:
        collection (Iterable[Any]): The collection to search for the minimum.
        ignore_none (bool): If True, ignores None values in the calculation.
                           Defaults to True.

    Returns:
        Optional[Any]: The minimum value in the collection, or None if it is empty
                      or contains only None.

    Raises:
        TypeError: If the collection is not iterable.
        ValueError: If the collection is empty after filtering None.

    Example of use:
        >>> collection_min([5, 1, 9, 3, 2])
        1
        >>> collection_min(['zebra', 'apple', 'banana'])
        'apple'
        >>> collection_min([3.7, None, 1.5, 2.1], ignore_none=True)
        1.5

    **Cost:** O(n), where n is the number of elements in the collection.
    """
    if not isinstance(collection, Iterable):
        raise TypeError("The 'collection' argument must be an iterable.")

    if ignore_none:
        filtered_values = [item for item in collection if item is not None]
    else:
        filtered_values = list(collection)

    if not filtered_values:
        return None

    return min(filtered_values)


def collection_stdev(collection: Iterable[Union[int, float]], is_sample: bool = True, ignore_none: bool = True) -> Optional[float]:
    """
    Calculates the standard deviation of the values in an iterable collection.

    This function is equivalent to the SQL aggregate functions STDEV (sample) and
    STDEVP (population), allowing the calculation of standard deviation in any
    iterable collection.

    Args:
        collection (Iterable[Union[int, float]]): Collection of numeric values.
        is_sample (bool): If True, calculates for a sample (n-1).
                         If False, calculates for a population (n).
                         Defaults to True (equivalent to SQL's STDEV).
        ignore_none (bool): If True, ignores None values in the calculation.
                           Defaults to True.

    Returns:
        Optional[float]: The standard deviation, or None if there is not enough data.

    Raises:
        TypeError: If the collection is not iterable or contains non-numeric values.
        ValueError: If there are fewer than 2 values for a sample calculation.

    Example of use:
        >>> collection_stdev([2, 4, 4, 4, 5, 5, 7, 9])
        2.138089935299395
        >>> collection_stdev([2, 4, 4, 4, 5, 5, 7, 9], is_sample=False)
        2.0
        >>> collection_stdev([10, None, 20, 30], ignore_none=True)
        10.0

    **Cost:** O(n), where n is the number of elements in the collection.
    """
    if not isinstance(collection, Iterable):
        raise TypeError("The 'collection' argument must be an iterable.")

    values = []
    for item in collection:
        if item is None and ignore_none:
            continue
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be numeric. Found: {type(item).__name__}")
        values.append(item)

    if not values:
        return None

    if is_sample and len(values) < 2:
        raise ValueError("At least 2 values are required to calculate the standard deviation of a sample.")

    mean = sum(values) / len(values)
    variance = sum((x - mean) ** 2 for x in values)

    divisor = len(values) - 1 if is_sample else len(values)
    return (variance / divisor) ** 0.5


def collection_sum(collection: Iterable[Union[int, float]], ignore_none: bool = True) -> Union[int, float]:
    """
    Calculates the sum of the numeric values in an iterable collection.

    This function is equivalent to the SQL aggregate function SUM and allows
    summing numeric values in any iterable collection.

    Args:
        collection (Iterable[Union[int, float]]): Collection of numeric values.
        ignore_none (bool): If True, ignores None values in the calculation.
                           Defaults to True.

    Returns:
        Union[int, float]: The sum of the values. Returns 0 if the collection is empty.

    Raises:
        TypeError: If the collection is not iterable or contains non-numeric values.

    Example of use:
        >>> collection_sum([1, 2, 3, 4, 5])
        15
        >>> collection_sum([10, None, 20, 30], ignore_none=True)
        60
        >>> collection_sum((5.5, 10.5, 15.5))
        31.5

    **Cost:** O(n), where n is the number of elements in the collection.
    """
    if not isinstance(collection, Iterable):
        raise TypeError("The 'collection' argument must be an iterable.")

    total = 0
    for item in collection:
        if item is None and ignore_none:
            continue
        if not isinstance(item, (int, float)):
            raise TypeError(f"All elements must be numeric. Found: {type(item).__name__}")
        total += item

    return total


def deep_merge(dict1: dict, dict2: dict) -> dict:
    """Recursively merges two dictionaries.

    Nested dicts are merged instead of overwritten. For non-dict values,
    *dict2* takes precedence.

    Args:
        dict1: The base dictionary.
        dict2: The dictionary whose values override *dict1*.

    Returns:
        A new merged dictionary. Original inputs are not mutated.

    Raises:
        TypeError: If either argument is not a dict.

    Example:
        >>> deep_merge({"a": 1, "b": {"x": 10}}, {"b": {"y": 20}, "c": 3})
        {'a': 1, 'b': {'x': 10, 'y': 20}, 'c': 3}
        >>> deep_merge({"a": 1}, {"a": 2})
        {'a': 2}

    **Cost:** O(n) where n is the total number of keys across both dicts.
    """
    if not isinstance(dict1, dict):
        raise TypeError("dict1 must be a dict.")

    if not isinstance(dict2, dict):
        raise TypeError("dict2 must be a dict.")

    result = dict1.copy()

    for key, value in dict2.items():

        if key in result and isinstance(result[key], dict) and isinstance(value, dict):
            result[key] = deep_merge(result[key], value)
        else:
            result[key] = value

    return result


def get_nested(data: dict, keys: List[str], default: Any = None) -> Any:
    """Retrieves a value from a nested dictionary using a sequence of keys.

    Safely traverses nested dicts without raising ``KeyError``. Returns
    *default* if any intermediate key is missing or not a dict.

    Args:
        data: The nested dictionary.
        keys: Ordered list of keys forming the path.
        default: Value to return if the path does not exist.

    Returns:
        The value at the nested path, or *default*.

    Raises:
        TypeError: If *data* is not a dict or *keys* is not a list.

    Example:
        >>> get_nested({"a": {"b": {"c": 42}}}, ["a", "b", "c"])
        42
        >>> get_nested({"a": {"b": 1}}, ["a", "x"], default=-1)
        -1
        >>> get_nested({}, ["a"], default="missing")
        'missing'

    **Cost:** O(k) where k is the length of *keys*.
    """
    if not isinstance(data, dict):
        raise TypeError("data must be a dict.")

    if not isinstance(keys, list):
        raise TypeError("keys must be a list.")

    current: Any = data

    for key in keys:

        if not isinstance(current, dict):
            return default

        current = current.get(key, default)

        if current is default:
            return default

    return current


def chunk(iterable: Iterable, n: int) -> List[list]:
    """Splits an iterable into fixed-size chunks.

    The last chunk may contain fewer than *n* elements.

    Args:
        iterable: The input iterable to split.
        n: Size of each chunk. Must be >= 1.

    Returns:
        A list of lists, each containing up to *n* elements.

    Raises:
        TypeError: If *iterable* is not iterable or *n* is not int.
        ValueError: If *n* < 1.

    Example:
        >>> chunk([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5]]
        >>> chunk("abcdef", 3)
        [['a', 'b', 'c'], ['d', 'e', 'f']]
        >>> chunk(range(7), 4)
        [[0, 1, 2, 3], [4, 5, 6]]

    **Cost:** O(n) where n is the number of elements.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be at least 1.")

    items = list(iterable)
    return [items[i:i + n] for i in range(0, len(items), n)]


def group_by(iterable: Iterable, key_func: Callable) -> dict:
    """Groups elements of an iterable by a key function.

    Args:
        iterable: The collection to group.
        key_func: A callable that returns the grouping key for each element.

    Returns:
        A dictionary mapping each key to a list of matching elements.

    Example:
        >>> group_by(["apple", "avocado", "banana", "blueberry"], lambda x: x[0])
        {'a': ['apple', 'avocado'], 'b': ['banana', 'blueberry']}
        >>> group_by([1, 2, 3, 4, 5, 6], lambda x: x % 2)
        {1: [1, 3, 5], 0: [2, 4, 6]}

    **Cost:** O(n) where n is the number of elements.
    """
    if not callable(key_func):
        raise TypeError("key_func must be callable.")

    result: dict = {}

    for item in iterable:
        key = key_func(item)
        result.setdefault(key, []).append(item)

    return result


def partition(
    predicate: Callable,
    iterable: Iterable,
) -> Tuple[list, list]:
    """Splits an iterable into two lists based on a predicate.

    Args:
        predicate: A callable returning True/False for each element.
        iterable: The collection to partition.

    Returns:
        A tuple ``(true_items, false_items)``.

    Example:
        >>> partition(lambda x: x > 3, [1, 2, 3, 4, 5, 6])
        ([4, 5, 6], [1, 2, 3])
        >>> partition(str.isupper, ["A", "b", "C", "d"])
        (['A', 'C'], ['b', 'd'])

    **Cost:** O(n) where n is the number of elements.
    """
    if not callable(predicate):
        raise TypeError("predicate must be callable.")

    true_items: list = []
    false_items: list = []

    for item in iterable:

        if predicate(item):
            true_items.append(item)
        else:
            false_items.append(item)

    return true_items, false_items


def pluck(iterable: Iterable, key: Any) -> list:
    """Extracts a single field from each element in a collection.

    Works with dictionaries (by key) and objects (by attribute name).

    Args:
        iterable: A collection of dicts or objects.
        key: The dictionary key or attribute name to extract.

    Returns:
        A list of extracted values.

    Example:
        >>> pluck([{"name": "Alice"}, {"name": "Bob"}], "name")
        ['Alice', 'Bob']
        >>> pluck([{"x": 1, "y": 2}, {"x": 3, "y": 4}], "x")
        [1, 3]

    **Cost:** O(n) where n is the number of elements.
    """
    result: list = []

    for item in iterable:

        if isinstance(item, dict):
            result.append(item[key])
        else:
            result.append(getattr(item, key))

    return result


def find(
    predicate: Callable,
    iterable: Iterable,
    default: Any = None,
) -> Any:
    """Returns the first element matching a predicate.

    Args:
        predicate: A callable returning True for the desired element.
        iterable: The collection to search.
        default: Value returned when no match is found (default None).

    Returns:
        The first matching element, or ``default``.

    Example:
        >>> find(lambda x: x > 3, [1, 2, 3, 4, 5])
        4
        >>> find(lambda x: x > 10, [1, 2, 3], default=-1)
        -1

    **Cost:** O(n) worst case.
    """
    if not callable(predicate):
        raise TypeError("predicate must be callable.")

    for item in iterable:

        if predicate(item):
            return item

    return default


def sort_dict_by_value(d: dict, reverse: bool = False) -> dict:
    """Return a new dict sorted by values.

    Args:
        d: Input dictionary.
        reverse: If True, sort descending. Defaults to False.

    Returns:
        Ordered dict sorted by values.

    Example:
        >>> sort_dict_by_value({'b': 2, 'a': 1, 'c': 3})
        {'a': 1, 'b': 2, 'c': 3}

    Complexity: O(n log n)
    """

    return dict(sorted(d.items(), key=lambda item: item[1], reverse=reverse))


def sort_dict_by_key(d: dict, reverse: bool = False) -> dict:
    """Return a new dict sorted by keys.

    Args:
        d: Input dictionary.
        reverse: If True, sort descending. Defaults to False.

    Returns:
        Ordered dict sorted by keys.

    Example:
        >>> sort_dict_by_key({'c': 3, 'a': 1, 'b': 2})
        {'a': 1, 'b': 2, 'c': 3}

    Complexity: O(n log n)
    """

    return dict(sorted(d.items(), key=lambda item: item[0], reverse=reverse))


def deep_flatten(nested: Any) -> list:
    """Recursively flatten a nested structure of arbitrary depth.

    Unlike :func:`flatten_list` which flattens one level, this function
    handles any nesting depth. Strings are not expanded.

    Args:
        nested: Nested lists/tuples/iterables.

    Returns:
        Flat list of all leaf elements.

    Example:
        >>> deep_flatten([1, [2, [3, [4]], 5]])
        [1, 2, 3, 4, 5]
        >>> deep_flatten([[1, 2], 'hello', [3, [4]]])
        [1, 2, 'hello', 3, 4]

    Complexity: O(n) total elements
    """

    result: list = []

    for item in nested:

        if isinstance(item, (list, tuple)):
            result.extend(deep_flatten(item))
        else:
            result.append(item)

    return result


def zip_dict(keys: List[Any], values: List[Any]) -> dict:
    """Create a dictionary from two parallel lists of keys and values.

    If lists differ in length, extra elements are dropped.

    Args:
        keys: List of keys.
        values: List of values.

    Returns:
        Dictionary mapping keys[i] to values[i].

    Example:
        >>> zip_dict(['a', 'b', 'c'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3}

    Complexity: O(n)
    """

    return dict(zip(keys, values))


def count_by(iterable: Iterable[Any],
             key_func: Callable[[Any], Any]) -> dict:
    """Count the number of elements in each group defined by a key function.

    Args:
        iterable: Input iterable.
        key_func: Function returning the grouping key.

    Returns:
        Dict mapping each key to its count.

    Example:
        >>> count_by(['apple', 'ant', 'banana', 'avocado'], lambda s: s[0])
        {'a': 3, 'b': 1}

    Complexity: O(n)
    """

    result: dict = {}

    for item in iterable:
        key = key_func(item)
        result[key] = result.get(key, 0) + 1

    return result


def index_by(dicts: List[dict], key: str) -> dict:
    """Index a list of dicts by a given field, creating a lookup table.

    If multiple dicts share the same key value, the last one wins.

    Args:
        dicts: List of dictionaries.
        key: Field name to use as the index key.

    Returns:
        Dict mapping key values to their source dicts.

    Example:
        >>> data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
        >>> index_by(data, 'id')
        {1: {'id': 1, 'name': 'Alice'}, 2: {'id': 2, 'name': 'Bob'}}

    Complexity: O(n)
    """

    return {d[key]: d for d in dicts if key in d}


def flatten_dict(
    d: dict,
    separator: str = ".",
    parent_key: str = "",
) -> dict:
    """Flattens a nested dictionary into a single-level dictionary.

    Nested keys are joined with *separator*.

    Args:
        d: The nested dictionary to flatten.
        separator: Separator between key levels (default ".").
        parent_key: Internal prefix (used by recursion).

    Returns:
        A flat dictionary with composite keys.

    Example:
        >>> flatten_dict({"a": {"b": 1, "c": {"d": 2}}})
        {'a.b': 1, 'a.c.d': 2}

    **Cost:** O(n) where n is total number of leaf values.
    """
    items: list[tuple[str, Any]] = []

    for key, value in d.items():
        new_key = f"{parent_key}{separator}{key}" if parent_key else str(key)

        if isinstance(value, dict):
            items.extend(flatten_dict(value, separator, new_key).items())
        else:
            items.append((new_key, value))

    return dict(items)


def unflatten_dict(d: dict, separator: str = ".") -> dict:
    """Reconstructs a nested dictionary from a flat one.

    Composite keys are split by *separator* to create nested levels.

    Args:
        d: The flat dictionary with composite keys.
        separator: The separator used in the keys (default ".").

    Returns:
        A nested dictionary.

    Example:
        >>> unflatten_dict({"a.b": 1, "a.c.d": 2})
        {'a': {'b': 1, 'c': {'d': 2}}}

    **Cost:** O(n*k) where k is average key depth.
    """
    result: dict = {}

    for composite_key, value in d.items():
        keys = composite_key.split(separator)
        current = result

        for part in keys[:-1]:

            if part not in current:
                current[part] = {}

            current = current[part]

        current[keys[-1]] = value

    return result


def frequencies(items: Iterable) -> dict:
    """Counts occurrences of each element in an iterable.

    Args:
        items: The collection of hashable elements.

    Returns:
        A dictionary mapping each element to its count.

    Example:
        >>> frequencies(["a", "b", "a", "c", "a"])
        {'a': 3, 'b': 1, 'c': 1}

    **Cost:** O(n)
    """
    counts: dict = {}

    for item in items:
        counts[item] = counts.get(item, 0) + 1

    return counts


def sort_dicts_by_key(
    items: list[dict],
    key: str,
    reverse: bool = False,
) -> list[dict]:
    """Sorts a list of dictionaries by a specific key.

    Args:
        items: The list of dictionaries to sort.
        key: The dictionary key to sort by.
        reverse: If True, sorts in descending order.

    Returns:
        A new sorted list of dictionaries.

    Example:
        >>> sort_dicts_by_key([{"n": 3}, {"n": 1}, {"n": 2}], "n")
        [{'n': 1}, {'n': 2}, {'n': 3}]

    **Cost:** O(n log n)
    """
    return sorted(items, key=lambda d: d.get(key), reverse=reverse)


def conditional_sum(
    values: List[Union[int, float]],
    criteria: Callable[[Union[int, float]], bool],
) -> float:
    """Sums values that match a criteria function.

    Description:
        Iterates over the values and sums only those for which the
        criteria function returns True. Equivalent to Excel SUMIF logic.

    Args:
        values: A list of numeric values.
        criteria: A callable that takes a value and returns True/False.

    Returns:
        The sum of matching values.

    Example:
        >>> conditional_sum([1, 2, 3, 4, 5], lambda x: x > 3)
        9
        >>> conditional_sum([10, 20, 30], lambda x: x < 15)
        10

    **Cost:** O(n)
    """
    return sum(v for v in values if criteria(v))


def conditional_count(
    values: List[Any],
    criteria: Callable[[Any], bool],
) -> int:
    """Counts values that match a criteria function.

    Description:
        Iterates over the values and counts those for which the
        criteria function returns True. Equivalent to Excel COUNTIF logic.

    Args:
        values: A list of values.
        criteria: A callable that takes a value and returns True/False.

    Returns:
        The count of matching values.

    Example:
        >>> conditional_count([1, 2, 3, 4, 5], lambda x: x > 3)
        2
        >>> conditional_count(["a", "b", "a"], lambda x: x == "a")
        2

    **Cost:** O(n)
    """
    return sum(1 for v in values if criteria(v))


def conditional_average(
    values: List[Union[int, float]],
    criteria: Callable[[Union[int, float]], bool],
) -> float:
    """Averages values that match a criteria function.

    Description:
        Computes the arithmetic mean of values for which the criteria
        function returns True. Equivalent to Excel AVERAGEIF logic.

    Args:
        values: A list of numeric values.
        criteria: A callable that takes a value and returns True/False.

    Returns:
        The average of matching values.

    Raises:
        ValueError: If no values match the criteria.

    Example:
        >>> conditional_average([1, 2, 3, 4, 5], lambda x: x > 2)
        4.0
        >>> conditional_average([10, 20, 30], lambda x: x >= 20)
        25.0

    **Cost:** O(n)
    """
    matched = [v for v in values if criteria(v)]

    if not matched:
        raise ValueError("No values match the criteria.")

    return sum(matched) / len(matched)


def conditional_min(
    values: List[Union[int, float]],
    criteria: Callable[[Union[int, float]], bool],
) -> Union[int, float]:
    """Returns the minimum of values that match a criteria function.

    Description:
        Finds the smallest value for which the criteria function
        returns True. Equivalent to Excel MINIFS logic.

    Args:
        values: A list of numeric values.
        criteria: A callable that takes a value and returns True/False.

    Returns:
        The minimum matching value.

    Raises:
        ValueError: If no values match the criteria.

    Example:
        >>> conditional_min([1, 2, 3, 4, 5], lambda x: x > 2)
        3
        >>> conditional_min([10, 20, 30], lambda x: x >= 20)
        20

    **Cost:** O(n)
    """
    matched = [v for v in values if criteria(v)]

    if not matched:
        raise ValueError("No values match the criteria.")

    return min(matched)


def conditional_max(
    values: List[Union[int, float]],
    criteria: Callable[[Union[int, float]], bool],
) -> Union[int, float]:
    """Returns the maximum of values that match a criteria function.

    Description:
        Finds the largest value for which the criteria function
        returns True. Equivalent to Excel MAXIFS logic.

    Args:
        values: A list of numeric values.
        criteria: A callable that takes a value and returns True/False.

    Returns:
        The maximum matching value.

    Raises:
        ValueError: If no values match the criteria.

    Example:
        >>> conditional_max([1, 2, 3, 4, 5], lambda x: x <= 3)
        3
        >>> conditional_max([10, 20, 30], lambda x: x < 25)
        20

    **Cost:** O(n)
    """
    matched = [v for v in values if criteria(v)]

    if not matched:
        raise ValueError("No values match the criteria.")

    return max(matched)


def vlookup(
    lookup_value: Any,
    table: List[List[Any]],
    col_index: int,
    approximate: bool = False,
) -> Any:
    """Searches for a value in the first column and returns a value from another column.

    Description:
        Looks up a value in the first column of a table (list of rows) and
        returns the corresponding value from the specified column index.
        Equivalent to Excel VLOOKUP.

    Args:
        lookup_value: The value to search for in the first column.
        table: A list of rows (lists), each with the same number of columns.
        col_index: The 1-based column index to return (1 = first column).
        approximate: If True, finds the closest match less than or equal
            to the lookup value (table must be sorted ascending by first column).
            If False, requires an exact match.

    Returns:
        The value from the matching row at the specified column.

    Raises:
        ValueError: If no match is found, col_index is out of range, or table is empty.
        TypeError: If table is not a list of lists.

    Example:
        >>> table = [[1, "a"], [2, "b"], [3, "c"]]
        >>> vlookup(2, table, 2)
        'b'
        >>> vlookup(2.5, [[1, "x"], [2, "y"], [3, "z"]], 2, approximate=True)
        'y'

    **Cost:** O(n) for exact match, O(n) for approximate match.
    """
    if not isinstance(table, list) or not all(isinstance(row, list) for row in table):
        raise TypeError("Table must be a list of lists.")

    if not table:
        raise ValueError("Table cannot be empty.")

    if col_index < 1 or col_index > len(table[0]):
        raise ValueError(
            f"col_index {col_index} is out of range. Table has {len(table[0])} columns."
        )

    if approximate:
        best_row = None

        for row in table:

            if row[0] <= lookup_value:

                if best_row is None or row[0] > best_row[0]:
                    best_row = row

        if best_row is None:
            raise ValueError(f"No match found for {lookup_value!r}.")

        return best_row[col_index - 1]

    for row in table:

        if row[0] == lookup_value:
            return row[col_index - 1]

    raise ValueError(f"No exact match found for {lookup_value!r}.")


def hlookup(
    lookup_value: Any,
    table: List[List[Any]],
    row_index: int,
    approximate: bool = False,
) -> Any:
    """Searches for a value in the first row and returns a value from another row.

    Description:
        Looks up a value in the first row of a table (list of rows) and
        returns the corresponding value from the specified row index.
        Equivalent to Excel HLOOKUP.

    Args:
        lookup_value: The value to search for in the first row.
        table: A list of rows (lists), each with the same number of columns.
        row_index: The 1-based row index to return (1 = first row).
        approximate: If True, finds the closest match less than or equal
            to the lookup value (first row must be sorted ascending).
            If False, requires an exact match.

    Returns:
        The value from the matching column at the specified row.

    Raises:
        ValueError: If no match is found, row_index is out of range, or table is empty.
        TypeError: If table is not a list of lists.

    Example:
        >>> table = [["a", "b", "c"], [1, 2, 3], [4, 5, 6]]
        >>> hlookup("b", table, 2)
        2
        >>> hlookup(2.5, [[1, 2, 3], [10, 20, 30]], 2, approximate=True)
        20

    **Cost:** O(m) where m is the number of columns.
    """
    if not isinstance(table, list) or not all(isinstance(row, list) for row in table):
        raise TypeError("Table must be a list of lists.")

    if not table or not table[0]:
        raise ValueError("Table cannot be empty.")

    if row_index < 1 or row_index > len(table):
        raise ValueError(
            f"row_index {row_index} is out of range. Table has {len(table)} rows."
        )

    first_row = table[0]

    if approximate:
        best_col = None

        for col_idx, val in enumerate(first_row):

            if val <= lookup_value:

                if best_col is None or val > first_row[best_col]:
                    best_col = col_idx

        if best_col is None:
            raise ValueError(f"No match found for {lookup_value!r}.")

        return table[row_index - 1][best_col]

    for col_idx, val in enumerate(first_row):

        if val == lookup_value:
            return table[row_index - 1][col_idx]

    raise ValueError(f"No exact match found for {lookup_value!r}.")


def choose(index: int, *values: Any) -> Any:
    """Chooses a value from a list of values based on a 1-based index.

    Description:
        Returns the value at the given position (1-based). Equivalent
        to Excel CHOOSE.

    Args:
        index: The 1-based position to select.
        *values: The values to choose from.

    Returns:
        The value at the specified index.

    Raises:
        ValueError: If index is out of range or no values are provided.
        TypeError: If index is not an integer.

    Example:
        >>> choose(2, "a", "b", "c")
        'b'
        >>> choose(1, 10, 20, 30)
        10

    **Cost:** O(1)
    """
    if not isinstance(index, int):
        raise TypeError("index must be an integer.")

    if not values:
        raise ValueError("At least one value must be provided.")

    if index < 1 or index > len(values):
        raise ValueError(
            f"index {index} is out of range. Must be between 1 and {len(values)}."
        )

    return values[index - 1]


def sort_by(
    data: List[Any],
    sort_keys: List[Any],
    reverse: bool = False,
) -> List[Any]:
    """Sorts data based on corresponding sort keys.

    Description:
        Sorts the data list using the values in sort_keys to determine
        order. Both lists must be the same length. Equivalent to Excel
        SORTBY.

    Args:
        data: The list of items to sort.
        sort_keys: The list of values to sort by (same length as data).
        reverse: If True, sorts in descending order.

    Returns:
        A new sorted list of data items.

    Raises:
        ValueError: If data and sort_keys have different lengths or are empty.

    Example:
        >>> sort_by(["c", "a", "b"], [3, 1, 2])
        ['a', 'b', 'c']
        >>> sort_by(["c", "a", "b"], [3, 1, 2], reverse=True)
        ['c', 'b', 'a']

    **Cost:** O(n log n)
    """
    if len(data) != len(sort_keys):
        raise ValueError("data and sort_keys must have the same length.")

    if not data:
        raise ValueError("data cannot be empty.")

    paired = sorted(zip(sort_keys, data), key=lambda pair: pair[0], reverse=reverse)
    return [item for _, item in paired]


def xlookup(
    lookup_value: Any,
    lookup_array: List[Any],
    return_array: List[Any],
    if_not_found: Any = None,
    match_mode: int = 0,
) -> Any:
    """Searches a lookup array and returns the corresponding value from a return array.

    Description:
        A more flexible lookup than vlookup/hlookup. Searches lookup_array
        for lookup_value and returns the corresponding element from
        return_array. Equivalent to Excel XLOOKUP.

    Args:
        lookup_value: The value to search for.
        lookup_array: The array to search in.
        return_array: The array to return a value from (same length).
        if_not_found: Value to return if no match is found (default None).
        match_mode: 0 = exact match, -1 = exact or next smaller,
            1 = exact or next larger.

    Returns:
        The matching value from return_array, or if_not_found.

    Raises:
        ValueError: If lookup_array and return_array have different lengths.

    Example:
        >>> xlookup("b", ["a", "b", "c"], [1, 2, 3])
        2
        >>> xlookup("z", ["a", "b", "c"], [1, 2, 3], "Not Found")
        'Not Found'
        >>> xlookup(25, [10, 20, 30], ["x", "y", "z"], match_mode=-1)
        'y'

    **Cost:** O(n)
    """
    if len(lookup_array) != len(return_array):
        raise ValueError("lookup_array and return_array must have the same length.")

    # Exact match
    if match_mode == 0:

        for i, val in enumerate(lookup_array):

            if val == lookup_value:
                return return_array[i]

        return if_not_found

    # Approximate: next smaller
    if match_mode == -1:
        best_idx = None

        for i, val in enumerate(lookup_array):

            if val <= lookup_value:

                if best_idx is None or val > lookup_array[best_idx]:
                    best_idx = i

        if best_idx is not None:
            return return_array[best_idx]

        return if_not_found

    # Approximate: next larger
    if match_mode == 1:
        best_idx = None

        for i, val in enumerate(lookup_array):

            if val >= lookup_value:

                if best_idx is None or val < lookup_array[best_idx]:
                    best_idx = i

        if best_idx is not None:
            return return_array[best_idx]

        return if_not_found

    return if_not_found


def sequence(
    rows: int = 1,
    columns: int = 1,
    start: float = 1,
    step: float = 1,
) -> list[list[float]]:
    """Generates a 2-D array of sequential numbers.

    Description:
        Returns a rows×columns matrix filled with values starting at
        *start* and incrementing by *step*. Equivalent to Excel SEQUENCE.

    Args:
        rows: Number of rows (>= 1).
        columns: Number of columns (>= 1).
        start: First value in the sequence.
        step: Increment between consecutive values.

    Returns:
        list[list[float]]: A 2-D list of sequential values.

    Raises:
        ValueError: If rows or columns < 1.

    Example:
        >>> sequence(2, 3)
        [[1, 2, 3], [4, 5, 6]]
        >>> sequence(3, 1, 0, 5)
        [[0], [5], [10]]

    Complexity: O(rows × columns)
    """
    if rows < 1 or columns < 1:
        raise ValueError("rows and columns must be >= 1.")

    result = []
    current = start

    for _ in range(rows):
        row = []

        for _ in range(columns):
            row.append(current)
            current += step

        result.append(row)

    return result


def index_2d(
    array: list[list[Any]],
    row_num: int,
    col_num: int | None = None,
) -> Any:
    """Returns an element or row/column from a 2-D array.

    Description:
        Uses 1-based indexing. If col_num is omitted, returns the entire
        row. If row_num is 0, returns the entire column.
        Equivalent to Excel INDEX.

    Args:
        array: A 2-D list (list of lists).
        row_num: 1-based row index (0 to get entire column).
        col_num: 1-based column index (None to get entire row).

    Returns:
        Any: The element, row, or column.

    Raises:
        IndexError: If row_num or col_num is out of bounds.
        TypeError: If array is not a list of lists.

    Example:
        >>> index_2d([[10, 20], [30, 40]], 2, 1)
        30
        >>> index_2d([[10, 20], [30, 40]], 1)
        [10, 20]

    Complexity: O(1) for element access, O(rows) for column
    """
    if not array or not isinstance(array[0], list):
        raise TypeError("array must be a list of lists.")

    num_rows = len(array)
    num_cols = len(array[0]) if num_rows > 0 else 0

    if col_num is None:
        # Return entire row
        if row_num < 1 or row_num > num_rows:
            raise IndexError(f"row_num {row_num} out of range [1, {num_rows}].")

        return array[row_num - 1]

    if row_num == 0:
        # Return entire column
        if col_num < 1 or col_num > num_cols:
            raise IndexError(f"col_num {col_num} out of range [1, {num_cols}].")

        return [row[col_num - 1] for row in array]

    if row_num < 1 or row_num > num_rows:
        raise IndexError(f"row_num {row_num} out of range [1, {num_rows}].")

    if col_num < 1 or col_num > num_cols:
        raise IndexError(f"col_num {col_num} out of range [1, {num_cols}].")

    return array[row_num - 1][col_num - 1]


def xmatch(
    lookup_value: Any,
    lookup_array: list[Any],
    match_mode: int = 0,
    search_mode: int = 1,
) -> int:
    """Returns the 1-based position of a value in an array.

    Description:
        Searches lookup_array for lookup_value and returns its relative
        position (1-based). Supports exact, next smaller, next larger,
        and wildcard matching. Equivalent to Excel XMATCH.

    Args:
        lookup_value: The value to search for.
        lookup_array: The array to search.
        match_mode: 0=exact, -1=exact or next smaller, 1=exact or next
                     larger, 2=wildcard (* and ?).
        search_mode: 1=first-to-last, -1=last-to-first.

    Returns:
        int: 1-based position of the match.

    Raises:
        ValueError: If no match is found.

    Example:
        >>> xmatch(30, [10, 20, 30, 40])
        3
        >>> xmatch(25, [10, 20, 30, 40], match_mode=-1)
        2

    Complexity: O(n)
    """
    import fnmatch as _fnmatch

    indices = range(len(lookup_array))

    if search_mode == -1:
        indices = reversed(indices)

    if match_mode == 0:
        # Exact match
        for i in indices:

            if lookup_array[i] == lookup_value:
                return i + 1

        raise ValueError(f"Value {lookup_value!r} not found (exact match).")

    if match_mode == 2:
        # Wildcard match
        pattern = str(lookup_value)

        for i in indices:

            if _fnmatch.fnmatch(str(lookup_array[i]), pattern):
                return i + 1

        raise ValueError(f"No wildcard match for {lookup_value!r}.")

    if match_mode == -1:
        # Exact or next smaller
        best_idx = None

        for i in range(len(lookup_array)):
            val = lookup_array[i]

            if val == lookup_value:
                return i + 1

            if val < lookup_value:

                if best_idx is None or val > lookup_array[best_idx]:
                    best_idx = i

        if best_idx is not None:
            return best_idx + 1

        raise ValueError(f"No match <= {lookup_value!r} found.")

    if match_mode == 1:
        # Exact or next larger
        best_idx = None

        for i in range(len(lookup_array)):
            val = lookup_array[i]

            if val == lookup_value:
                return i + 1

            if val > lookup_value:

                if best_idx is None or val < lookup_array[best_idx]:
                    best_idx = i

        if best_idx is not None:
            return best_idx + 1

        raise ValueError(f"No match >= {lookup_value!r} found.")

    raise ValueError(f"Invalid match_mode: {match_mode}.")


def hstack(*arrays: list[list[Any]]) -> list[list[Any]]:
    """Horizontally concatenates 2-D arrays side by side.

    Description:
        Joins multiple 2-D arrays by appending columns. All arrays must
        have the same number of rows. Equivalent to Excel HSTACK.

    Args:
        *arrays: Two or more 2-D arrays.

    Returns:
        list[list[Any]]: Combined array.

    Raises:
        ValueError: If arrays have different row counts.

    Example:
        >>> hstack([[1, 2], [3, 4]], [[5], [6]])
        [[1, 2, 5], [3, 4, 6]]

    Complexity: O(rows × total_cols)
    """
    if not arrays:
        return []

    num_rows = len(arrays[0])

    for arr in arrays[1:]:

        if len(arr) != num_rows:
            raise ValueError("All arrays must have the same number of rows.")

    return [
        [val for arr in arrays for val in arr[r]]
        for r in range(num_rows)
    ]


def vstack(*arrays: list[list[Any]]) -> list[list[Any]]:
    """Vertically stacks 2-D arrays on top of each other.

    Description:
        Joins multiple 2-D arrays by appending rows. All arrays must
        have the same number of columns. Equivalent to Excel VSTACK.

    Args:
        *arrays: Two or more 2-D arrays.

    Returns:
        list[list[Any]]: Combined array.

    Raises:
        ValueError: If arrays have different column counts.

    Example:
        >>> vstack([[1, 2]], [[3, 4], [5, 6]])
        [[1, 2], [3, 4], [5, 6]]

    Complexity: O(total_rows × cols)
    """
    if not arrays:
        return []

    num_cols = len(arrays[0][0]) if arrays[0] else 0

    result: list[list[Any]] = []

    for arr in arrays:

        for row in arr:

            if len(row) != num_cols:
                raise ValueError("All arrays must have the same number of columns.")

            result.append(row)

    return result


def choose_cols(
    array: list[list[Any]],
    *col_nums: int,
) -> list[list[Any]]:
    """Selects specific columns from a 2-D array.

    Description:
        Returns a new array containing only the columns at the given
        1-based positions. Negative indices count from the right.
        Equivalent to Excel CHOOSECOLS.

    Args:
        array: A 2-D list.
        *col_nums: 1-based column indices (negative = from right).

    Returns:
        list[list[Any]]: Array with selected columns only.

    Raises:
        IndexError: If any column index is out of bounds.

    Example:
        >>> choose_cols([[1, 2, 3], [4, 5, 6]], 1, 3)
        [[1, 3], [4, 6]]
        >>> choose_cols([[1, 2, 3]], -1)
        [[3]]

    Complexity: O(rows × selected_cols)
    """
    if not array:
        return []

    num_cols = len(array[0])
    resolved = []

    for c in col_nums:

        if c > 0:
            idx = c - 1
        elif c < 0:
            idx = num_cols + c
        else:
            raise IndexError("Column index must be non-zero.")

        if idx < 0 or idx >= num_cols:
            raise IndexError(f"Column {c} out of range for {num_cols} columns.")

        resolved.append(idx)

    return [[row[i] for i in resolved] for row in array]


def choose_rows(
    array: list[list[Any]],
    *row_nums: int,
) -> list[list[Any]]:
    """Selects specific rows from a 2-D array.

    Description:
        Returns a new array containing only the rows at the given
        1-based positions. Negative indices count from the bottom.
        Equivalent to Excel CHOOSEROWS.

    Args:
        array: A 2-D list.
        *row_nums: 1-based row indices (negative = from bottom).

    Returns:
        list[list[Any]]: Array with selected rows only.

    Raises:
        IndexError: If any row index is out of bounds.

    Example:
        >>> choose_rows([[1, 2], [3, 4], [5, 6]], 1, 3)
        [[1, 2], [5, 6]]
        >>> choose_rows([[1, 2], [3, 4]], -1)
        [[3, 4]]

    Complexity: O(selected_rows × cols)
    """
    if not array:
        return []

    num_rows = len(array)
    result = []

    for r in row_nums:

        if r > 0:
            idx = r - 1
        elif r < 0:
            idx = num_rows + r
        else:
            raise IndexError("Row index must be non-zero.")

        if idx < 0 or idx >= num_rows:
            raise IndexError(f"Row {r} out of range for {num_rows} rows.")

        result.append(array[idx])

    return result


def wrap_rows(
    vector: list[Any],
    wrap_count: int,
    pad_with: Any = None,
) -> list[list[Any]]:
    """Wraps a 1-D vector into a 2-D array by rows.

    Description:
        Splits a flat list into rows of *wrap_count* elements.
        The last row is padded with *pad_with* if needed.
        Equivalent to Excel WRAPROWS.

    Args:
        vector: Flat list of values.
        wrap_count: Number of elements per row (>= 1).
        pad_with: Value used to pad the last incomplete row.

    Returns:
        list[list[Any]]: A 2-D array.

    Raises:
        ValueError: If wrap_count < 1.

    Example:
        >>> wrap_rows([1, 2, 3, 4, 5], 2)
        [[1, 2], [3, 4], [5, None]]
        >>> wrap_rows([1, 2, 3, 4], 2)
        [[1, 2], [3, 4]]

    Complexity: O(n)
    """
    if wrap_count < 1:
        raise ValueError("wrap_count must be >= 1.")

    result = []

    for i in range(0, len(vector), wrap_count):
        chunk = vector[i:i + wrap_count]

        while len(chunk) < wrap_count:
            chunk.append(pad_with)

        result.append(chunk)

    return result


def drop_from_array(
    array: list[list[Any]],
    rows: int = 0,
    columns: int = 0,
) -> list[list[Any]]:
    """Drops rows and/or columns from a 2-D array.

    Description:
        If rows > 0, drops from the top; if rows < 0, drops from the
        bottom. Same logic for columns (left/right).
        Equivalent to Excel DROP.

    Args:
        array: A 2-D list.
        rows: Number of rows to drop (positive=top, negative=bottom).
        columns: Number of columns to drop (positive=left, negative=right).

    Returns:
        list[list[Any]]: The trimmed array.

    Example:
        >>> drop_from_array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=1, columns=-1)
        [[4, 5], [7, 8]]
        >>> drop_from_array([[1, 2], [3, 4]], rows=-1)
        [[1, 2]]

    Complexity: O(rows × cols)
    """
    if not array:
        return []

    result = list(array)

    if rows > 0:
        result = result[rows:]
    elif rows < 0:
        result = result[:rows]

    if columns > 0:
        result = [row[columns:] for row in result]
    elif columns < 0:
        result = [row[:columns] for row in result]

    return result


def take_from_array(
    array: list[list[Any]],
    rows: int | None = None,
    columns: int | None = None,
) -> list[list[Any]]:
    """Takes the first or last rows/columns from a 2-D array.

    Description:
        If rows > 0, takes from the top; if rows < 0, takes from the
        bottom. Same logic for columns (left/right).
        Equivalent to Excel TAKE.

    Args:
        array: A 2-D list.
        rows: Number of rows to take (positive=top, negative=bottom).
        columns: Number of columns to take (positive=left, negative=right).

    Returns:
        list[list[Any]]: The extracted sub-array.

    Example:
        >>> take_from_array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=2, columns=-2)
        [[2, 3], [5, 6]]
        >>> take_from_array([[1, 2], [3, 4], [5, 6]], rows=-1)
        [[5, 6]]

    Complexity: O(rows × cols)
    """
    if not array:
        return []

    result = list(array)

    if rows is not None:

        if rows > 0:
            result = result[:rows]
        elif rows < 0:
            result = result[rows:]

    if columns is not None:

        if columns > 0:
            result = [row[:columns] for row in result]
        elif columns < 0:
            result = [row[columns:] for row in result]

    return result


def make_array(
    rows: int,
    columns: int,
    fn: Callable[[int, int], Any],
) -> list[list[Any]]:
    """Generates a 2-D array using a function.

    Description:
        Creates a rows×columns matrix where each cell value is computed
        by calling fn(row_index, col_index) with 0-based indices.
        Equivalent to Excel MAKEARRAY.

    Args:
        rows: Number of rows (>= 1).
        columns: Number of columns (>= 1).
        fn: A callable that takes (row, col) and returns a value.

    Returns:
        list[list[Any]]: The generated array.

    Raises:
        ValueError: If rows or columns < 1.
        TypeError: If fn is not callable.

    Example:
        >>> make_array(2, 3, lambda r, c: (r + 1) * (c + 1))
        [[1, 2, 3], [2, 4, 6]]

    Complexity: O(rows × columns)
    """
    if rows < 1 or columns < 1:
        raise ValueError("rows and columns must be >= 1.")

    if not callable(fn):
        raise TypeError("fn must be callable.")

    return [[fn(r, c) for c in range(columns)] for r in range(rows)]


def tocol(
    array: list, scan_by_column: bool = False,
) -> list:
    """Flatten a 2-D array into a single-column list of lists.

    Description:
        Converts a 2-D array to column format [[v1],[v2],...].
        Equivalent to Excel TOCOL.

    Args:
        array: 2-D list.
        scan_by_column: If True, scan column-first; otherwise row-first.

    Returns:
        list: List of single-element lists.

    Raises:
        TypeError: If array is not a list.

    Example:
        >>> tocol([[1, 2], [3, 4]])
        [[1], [2], [3], [4]]
        >>> tocol([[1, 2], [3, 4]], scan_by_column=True)
        [[1], [3], [2], [4]]

    Complexity: O(r × c)
    """
    if not isinstance(array, list):
        raise TypeError("array must be a list.")

    if scan_by_column:
        cols = len(array[0]) if array else 0
        return [
            [array[r][c]]
            for c in range(cols)
            for r in range(len(array))
        ]

    return [[cell] for row in array for cell in row]


def torow(
    array: list, scan_by_column: bool = False,
) -> list:
    """Flatten a 2-D array into a single-row list.

    Description:
        Converts a 2-D array to row format [[v1, v2, ...]].
        Equivalent to Excel TOROW.

    Args:
        array: 2-D list.
        scan_by_column: If True, scan column-first; otherwise row-first.

    Returns:
        list: A list containing one list with all values.

    Raises:
        TypeError: If array is not a list.

    Example:
        >>> torow([[1, 2], [3, 4]])
        [[1, 2, 3, 4]]
        >>> torow([[1, 2], [3, 4]], scan_by_column=True)
        [[1, 3, 2, 4]]

    Complexity: O(r × c)
    """
    if not isinstance(array, list):
        raise TypeError("array must be a list.")

    if scan_by_column:
        cols = len(array[0]) if array else 0
        return [[
            array[r][c]
            for c in range(cols)
            for r in range(len(array))
        ]]

    return [[cell for row in array for cell in row]]


def expand_array(
    array: list,
    rows: int = None,
    columns: int = None,
    pad_with: Any = None,
) -> list:
    """Expand a 2-D array to target dimensions, padding new cells.

    Description:
        Pads an array with a fill value to reach the specified
        number of rows and columns. Equivalent to Excel EXPAND.

    Args:
        array: 2-D list to expand.
        rows: Target row count (default: keep current).
        columns: Target column count (default: keep current).
        pad_with: Value for new cells (default None).

    Returns:
        list: Expanded 2-D list.

    Raises:
        TypeError: If array is not a list.
        ValueError: If target is smaller than source.

    Example:
        >>> expand_array([[1, 2], [3, 4]], 3, 4, 0)
        [[1, 2, 0, 0], [3, 4, 0, 0], [0, 0, 0, 0]]

    Complexity: O(rows × columns)
    """
    if not isinstance(array, list):
        raise TypeError("array must be a list.")

    cur_rows = len(array)
    cur_cols = len(array[0]) if array else 0

    if rows is None:
        rows = cur_rows

    if columns is None:
        columns = cur_cols

    if rows < cur_rows or columns < cur_cols:
        raise ValueError(
            f"Target ({rows}, {columns}) must be >= source "
            f"({cur_rows}, {cur_cols})."
        )

    result = []

    for r in range(rows):

        if r < cur_rows:
            row = list(array[r][:columns])
            row.extend([pad_with] * (columns - len(row)))
        else:
            row = [pad_with] * columns

        result.append(row)

    return result


# ---------------------------------------------------------------------------
# Criteria-based counting helpers
# ---------------------------------------------------------------------------

def _parse_criteria(criteria) -> callable:
    """Return a predicate for an Excel-style criteria expression."""

    if isinstance(criteria, str):

        for op in (">=", "<=", "<>", ">", "<", "="):

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


def count_numbers(*values) -> int:
    """Count how many items are numeric (int or float, excluding bool).

    Equivalent to the Excel ``COUNT`` function.

    Args:
        *values: Individual values or lists/tuples of values.

    Returns:
        Number of numeric items.

    Example:
        >>> count_numbers([1, "a", 2, None, 3.5])
        3

    Complexity: O(n)
    """
    total = 0

    for val in values:

        if isinstance(val, (list, tuple)):

            for v in val:

                if isinstance(v, (int, float)) and not isinstance(v, bool):
                    total += 1

        elif isinstance(val, (int, float)) and not isinstance(val, bool):
            total += 1

    return total


def count_values(*values) -> int:
    """Count non-empty, non-None items.

    Equivalent to the Excel ``COUNTA`` function.

    Args:
        *values: Individual values or lists/tuples of values.

    Returns:
        Number of non-blank items.

    Example:
        >>> count_values([1, "", None, "hello", 0])
        3

    Complexity: O(n)
    """
    total = 0

    for val in values:

        if isinstance(val, (list, tuple)):

            for v in val:

                if v is not None and v != "":
                    total += 1

        elif val is not None and val != "":
            total += 1

    return total


def count_blank(values: list) -> int:
    """Count blank items (``None`` or ``\"\"``).

    Equivalent to the Excel ``COUNTBLANK`` function.

    Args:
        values: List of values to inspect.

    Returns:
        Number of blank items.

    Example:
        >>> count_blank([1, "", None, "hello", 0])
        2

    Complexity: O(n)
    """
    return sum(1 for v in values if v is None or v == "")


def count_if(values: list, criteria) -> int:
    """Count items that meet an Excel-style criteria.

    Equivalent to the Excel ``COUNTIF`` function.

    Args:
        values: List of values to evaluate.
        criteria: Excel-style criteria (e.g. ``\">10\"``, ``\"<>0\"``, ``\"apple\"``).

    Returns:
        Number of matching items.

    Example:
        >>> count_if([1, 5, 10, 15, 20], ">8")
        3
        >>> count_if(["a", "b", "a", "c"], "a")
        2

    Complexity: O(n)
    """
    pred = _parse_criteria(criteria)
    return sum(1 for v in values if pred(v))


def count_ifs(values: list, *criteria_pairs) -> int:
    """Count items where every criteria pair is satisfied.

    Equivalent to the Excel ``COUNTIFS`` function.  Criteria pairs are
    given as alternating ``(range, criteria)`` arguments.

    Args:
        values: Primary range whose length determines the row count.
        *criteria_pairs: Alternating ``criteria_range, criteria`` arguments.
            Must contain an even number of elements.

    Returns:
        Number of indices where **all** criteria are met.

    Raises:
        ValueError: If *criteria_pairs* length is odd or ranges differ in length.

    Example:
        >>> count_ifs(
        ...     [1, 2, 3, 4, 5],
        ...     [1, 2, 3, 4, 5], ">1",
        ...     [1, 2, 3, 4, 5], "<5",
        ... )
        3

    Complexity: O(n * k) where k is the number of criteria pairs.
    """
    if len(criteria_pairs) % 2 != 0:
        raise ValueError("criteria_pairs must contain an even number of elements.")

    pairs = []

    for i in range(0, len(criteria_pairs), 2):
        rng = criteria_pairs[i]
        crit = criteria_pairs[i + 1]

        if len(rng) != len(values):
            raise ValueError("All criteria ranges must match the length of values.")

        pairs.append((rng, _parse_criteria(crit)))

    total = 0

    for idx in range(len(values)):

        if all(pred(rng[idx]) for rng, pred in pairs):
            total += 1

    return total

