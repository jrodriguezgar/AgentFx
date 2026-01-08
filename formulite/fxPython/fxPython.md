# FormuLite - fxPython Module

Complete API documentation for the fxPython module - Python utilities for collection conversions, operations, tools, and itertools recipes.

## Overview

The fxPython module provides comprehensive Python collection and utility functions for FormuLite, including:
- **Collection Conversions**: Transform between lists, sets, tuples, dictionaries, and strings
- **Collection Operations**: Merge, filter, flatten, intersection, unique operations
- **Python Tools**: Dynamic execution, switch-case, loops, key-value creation
- **Itertools Recipes**: Advanced iteration patterns from Python's itertools documentation

## Module Structure

- **py_convertions.py**: Functions for converting between Python collection types
- **py_operations.py**: Core collection operations and filtering functions
- **py_tools.py**: Utility functions for functional programming and control flow
- **py_logic.py**: Logical operations and conditional functions
- **py_itertools.py**: Advanced itertools recipes and iterator utilities

---

## Table of Contents

- [Function Categories](#function-categories)
  - [Collection Conversions](#collection-conversions)
  - [Collection Operations](#collection-operations)
  - [Python Tools](#python-tools)
  - [Itertools Recipes](#itertools-recipes)
- [Function Index](#function-index)
- [Credits](#credits)

---

## Function Categories

### Collection Conversions
- [convert_collection](#convert_collection) - Converts a collection to a specified target type
- [set_to_string](#set_to_string) - Converts a set to string representation with separator
- [set_to_list](#set_to_list) - Converts a set into a list
- [set_to_tuple](#set_to_tuple) - Converts a set into a tuple
- [tuple_to_string](#tuple_to_string) - Converts tuple to string representation with separator
- [tuple_to_list](#tuple_to_list) - Converts a tuple into a list
- [tuple_to_set](#tuple_to_set) - Converts a tuple into a set
- [list_to_string](#list_to_string) - Converts list to string representation with separator
- [list_to_set](#list_to_set) - Converts a list into a set
- [list_to_tuple](#list_to_tuple) - Converts a list into a tuple
- [dictionary_to_string](#dictionary_to_string) - Serializes dictionary into string with colons and semicolons
- [string_to_dictionary](#string_to_dictionary) - Deserializes string back into a dictionary
- [dictionary_keys_to_list](#dictionary_keys_to_list) - Returns dictionary keys as a list
- [dict_values_to_list](#dict_values_to_list) - Returns dictionary values as a list
- [dictionary_items_to_list_of_tuples](#dictionary_items_to_list_of_tuples) - Returns dictionary items as list of tuples
- [dictionary_keys_to_set](#dictionary_keys_to_set) - Returns dictionary keys as a set
- [dictionary_values_to_set](#dictionary_values_to_set) - Returns dictionary values as a set
- [dictionary_to_object](#dictionary_to_object) - Converts dictionary into an object with attributes
- [dictionary_items_to_set_of_tuples](#dictionary_items_to_set_of_tuples) - Returns dictionary items as set of tuples
- [list_of_tuples_to_dict](#list_of_tuples_to_dict) - Converts list of tuples to dictionary
- [list_of_lists_to_dict](#list_of_lists_to_dict) - Converts list of lists to dictionary
- [list_of_dicts_to_merged_dict](#list_of_dicts_to_merged_dict) - Merges list of dictionaries into single dictionary
- [string_to_list](#string_to_list) - Converts string to list of characters or substrings

### Collection Operations
- [merge_json_strings](#merge_json_strings) - Merges two JSON strings into one
- [add_to_tuple](#add_to_tuple) - Adds element to end of tuple
- [unique_list](#unique_list) - Returns list containing only unique elements
- [unique_tuple_list](#unique_tuple_list) - Removes duplicate tuples based on first element
- [flatten_list](#flatten_list) - Flattens list of lists into one-dimensional list
- [list_intersection](#list_intersection) - Finds intersection of two lists as set
- [list_has_list](#list_has_list) - Checks if all elements exist in another list
- [is_subsequence](#is_subsequence) - Checks if sub_sequence exists maintaining element order
- [filter_elements_by_another](#filter_elements_by_another) - Filters elements present in both collections
- [pick_in_collection](#pick_in_collection) - Interactive selection of options from iterable collection
- [merge_elements](#merge_elements) - Merges two collections into specified type
- [collection_filter](#collection_filter) - Filters iterable based on filtering function
- [dictionary_filter_by_keys](#dictionary_filter_by_keys) - Returns dictionary with only specified keys
- [combine_dictionaries](#combine_dictionaries) - Performs union or intersection on two dictionaries
- [dictionary_rename_keys](#dictionary_rename_keys) - Renames dictionary keys based on mapping
- [execute_os_command](#execute_os_command) - Executes OS command and captures output
- [calculate](#calculate) - Evaluates arithmetic expression from string
- [search](#search) - Searches for target element in iterable collection
- [collection_avg](#collection_avg) - Calculates the average of numeric values in a collection
- [collection_count](#collection_count) - Counts the number of elements in a collection
- [collection_max](#collection_max) - Returns the highest value in a collection
- [collection_min](#collection_min) - Returns the smallest value in a collection
- [collection_stdev](#collection_stdev) - Calculates the standard deviation of values in a collection
- [collection_sum](#collection_sum) - Calculates the sum of numeric values in a collection

### Logical Functions
- [and_all](#and_all) - Returns True if all arguments are True
- [or_any](#or_any) - Returns True if any argument is True
- [not_value](#not_value) - Reverses the logical value of its argument
- [xor_all](#xor_all) - Returns True if an odd number of arguments are True
- [if_then_else](#if_then_else) - Returns one value if condition is True, another if False
- [if_error](#if_error) - Returns value if not an error; otherwise returns alternative value
- [is_blank](#is_blank) - Returns True if value is blank (None, empty string, or empty collection)
- [is_error](#is_error) - Returns True if evaluating value produces an error
- [is_text](#is_text) - Returns True if value is a string
- [is_number](#is_number) - Returns True if value is a number (int or float, not bool)
- [is_logical](#is_logical) - Returns True if value is a boolean
- [switch_case](#switch_case) - Evaluates expression against values and returns matching result

### Python Tools
- [create_key_value_dictionary](#create_key_value_dictionary) - Creates dictionary mapping key names to values
- [function_call](#function_call) - Executes callable with optional arguments
- [switch_case](#switch_case) - Generic switch-case statement for value matching
- [loop_for](#loop_for) - Executes function for each item in iterable
- [loop_while](#loop_while) - Executes function while condition remains true
- [rotate](#rotate) - Rotates elements of iterable by steps
- [shift](#shift) - Shifts iterable adding or removing elements
- [apply_expression](#apply_expression) - Applies string expression to every iterable item

### Itertools Recipes
- [take](#take) - Returns first n items as list
- [prepend](#prepend) - Prepends single value in front of iterable
- [tabulate](#tabulate) - Returns function(0), function(1), etc.
- [repeatfunc](#repeatfunc) - Repeats calls to function with arguments
- [flatten](#flatten) - Flattens one level of nesting
- [ncycles](#ncycles) - Returns sequence elements n times
- [loops](#loops) - Loops n times without creating integers
- [tail](#tail) - Returns iterator over last n items
- [consume](#consume) - Advances iterator n-steps ahead
- [nth](#nth) - Returns nth item or default value
- [quantify](#quantify) - Counts True results from predicate
- [first_true](#first_true) - Returns first true value or default
- [all_equal](#all_equal) - Returns True if all elements equal
- [unique_justseen](#unique_justseen) - Yields unique elements preserving order
- [unique_everseen](#unique_everseen) - Yields unique elements remembering all seen
- [unique](#unique) - Yields unique elements in sorted order
- [sliding_window](#sliding_window) - Collects data into overlapping fixed-length chunks
- [grouper](#grouper) - Collects data into non-overlapping fixed-length chunks
- [roundrobin](#roundrobin) - Visits input iterables in cycle
- [subslices](#subslices) - Returns all contiguous non-empty subslices
- [iter_index](#iter_index) - Returns indices where value occurs
- [iter_except](#iter_except) - Converts call-until-exception interface to iterator
- [multinomial](#multinomial) - Calculates distinct arrangements of multiset
- [powerset](#powerset) - Returns subsequences from shortest to longest
- [sum_of_squares](#sum_of_squares) - Adds up squares of input values
- [reshape](#reshape) - Reshapes 2-D matrix to given columns
- [transpose](#transpose) - Swaps rows and columns of matrix
- [matmul](#matmul) - Multiplies two matrices
- [convolve](#convolve) - Discrete linear convolution of two iterables
- [polynomial_from_roots](#polynomial_from_roots) - Computes polynomial coefficients from roots
- [polynomial_eval](#polynomial_eval) - Evaluates polynomial at specific value
- [polynomial_derivative](#polynomial_derivative) - Computes first derivative of polynomial
- [sieve](#sieve) - Returns primes less than n
- [factor](#factor) - Returns prime factors of n
- [is_prime](#is_prime) - Returns True if n is prime
- [totient](#totient) - Counts natural numbers coprime to n

---

## Function Index

**A**
- [add_to_tuple](#add_to_tuple) - Adds element to end of tuple
- [all_equal](#all_equal) - Returns True if all elements equal
- [and_all](#and_all) - Returns True if all arguments are True
- [apply_expression](#apply_expression) - Applies string expression to every iterable item

**C**
- [calculate](#calculate) - Evaluates arithmetic expression from string
- [collection_avg](#collection_avg) - Calculates the average of numeric values in a collection
- [collection_count](#collection_count) - Counts the number of elements in a collection
- [collection_filter](#collection_filter) - Filters iterable based on filtering function
- [collection_max](#collection_max) - Returns the highest value in a collection
- [collection_min](#collection_min) - Returns the smallest value in a collection
- [collection_stdev](#collection_stdev) - Calculates the standard deviation of values in a collection
- [collection_sum](#collection_sum) - Calculates the sum of numeric values in a collection
- [combine_dictionaries](#combine_dictionaries) - Performs union or intersection on two dictionaries
- [consume](#consume) - Advances iterator n-steps ahead
- [convolve](#convolve) - Discrete linear convolution of two iterables
- [convert_collection](#convert_collection) - Converts a collection to a specified target type
- [create_key_value_dictionary](#create_key_value_dictionary) - Creates dictionary mapping key names to values

**D**
- [dict_values_to_list](#dict_values_to_list) - Returns dictionary values as a list
- [dictionary_filter_by_keys](#dictionary_filter_by_keys) - Returns dictionary with only specified keys
- [dictionary_items_to_list_of_tuples](#dictionary_items_to_list_of_tuples) - Returns dictionary items as list of tuples
- [dictionary_items_to_set_of_tuples](#dictionary_items_to_set_of_tuples) - Returns dictionary items as set of tuples
- [dictionary_keys_to_list](#dictionary_keys_to_list) - Returns dictionary keys as a list
- [dictionary_keys_to_set](#dictionary_keys_to_set) - Returns dictionary keys as a set
- [dictionary_rename_keys](#dictionary_rename_keys) - Renames dictionary keys based on mapping
- [dictionary_to_object](#dictionary_to_object) - Converts dictionary into an object with attributes
- [dictionary_to_string](#dictionary_to_string) - Serializes dictionary into string with colons and semicolons
- [dictionary_values_to_set](#dictionary_values_to_set) - Returns dictionary values as a set

**E**
- [execute_os_command](#execute_os_command) - Executes OS command and captures output

**F**
- [factor](#factor) - Returns prime factors of n
- [filter_elements_by_another](#filter_elements_by_another) - Filters elements present in both collections
- [first_true](#first_true) - Returns first true value or default
- [flatten](#flatten) - Flattens one level of nesting
- [flatten_list](#flatten_list) - Flattens list of lists into one-dimensional list
- [function_call](#function_call) - Executes callable with optional arguments

**G**
- [grouper](#grouper) - Collects data into non-overlapping fixed-length chunks

**I**
- [if_error](#if_error) - Returns value if not an error; otherwise returns alternative value
- [if_then_else](#if_then_else) - Returns one value if condition is True, another if False
- [is_blank](#is_blank) - Returns True if value is blank
- [is_error](#is_error) - Returns True if evaluating value produces an error
- [is_logical](#is_logical) - Returns True if value is a boolean
- [is_number](#is_number) - Returns True if value is a number
- [is_prime](#is_prime) - Returns True if n is prime
- [is_subsequence](#is_subsequence) - Checks if sub_sequence exists maintaining element order
- [is_text](#is_text) - Returns True if value is a string
- [iter_except](#iter_except) - Converts call-until-exception interface to iterator
- [iter_index](#iter_index) - Returns indices where value occurs

**L**
- [list_has_list](#list_has_list) - Checks if all elements exist in another list
- [list_intersection](#list_intersection) - Finds intersection of two lists as set
- [list_of_dicts_to_merged_dict](#list_of_dicts_to_merged_dict) - Merges list of dictionaries into single dictionary
- [list_of_lists_to_dict](#list_of_lists_to_dict) - Converts list of lists to dictionary
- [list_of_tuples_to_dict](#list_of_tuples_to_dict) - Converts list of tuples to dictionary
- [list_to_set](#list_to_set) - Converts a list into a set
- [list_to_string](#list_to_string) - Converts list to string representation with separator
- [list_to_tuple](#list_to_tuple) - Converts a list into a tuple
- [loop_for](#loop_for) - Executes function for each item in iterable
- [loop_while](#loop_while) - Executes function while condition remains true
- [loops](#loops) - Loops n times without creating integers

**M**
- [matmul](#matmul) - Multiplies two matrices
- [merge_elements](#merge_elements) - Merges two collections into specified type
- [merge_json_strings](#merge_json_strings) - Merges two JSON strings into one
- [multinomial](#multinomial) - Calculates distinct arrangements of multiset

**N**
- [ncycles](#ncycles) - Returns sequence elements n times
- [not_value](#not_value) - Reverses the logical value of its argument
- [nth](#nth) - Returns nth item or default value

**O**
- [or_any](#or_any) - Returns True if any argument is True

**P**
- [pick_in_collection](#pick_in_collection) - Interactive selection of options from iterable collection
- [polynomial_derivative](#polynomial_derivative) - Computes first derivative of polynomial
- [polynomial_eval](#polynomial_eval) - Evaluates polynomial at specific value
- [polynomial_from_roots](#polynomial_from_roots) - Computes polynomial coefficients from roots
- [powerset](#powerset) - Returns subsequences from shortest to longest
- [prepend](#prepend) - Prepends single value in front of iterable

**Q**
- [quantify](#quantify) - Counts True results from predicate

**R**
- [repeatfunc](#repeatfunc) - Repeats calls to function with arguments
- [reshape](#reshape) - Reshapes 2-D matrix to given columns
- [rotate](#rotate) - Rotates elements of iterable by steps
- [roundrobin](#roundrobin) - Visits input iterables in cycle

**S**
- [search](#search) - Searches for target element in iterable collection
- [set_to_list](#set_to_list) - Converts a set into a list
- [set_to_string](#set_to_string) - Converts a set to string representation with separator
- [set_to_tuple](#set_to_tuple) - Converts a set into a tuple
- [shift](#shift) - Shifts iterable adding or removing elements
- [sieve](#sieve) - Returns primes less than n
- [sliding_window](#sliding_window) - Collects data into overlapping fixed-length chunks
- [string_to_dictionary](#string_to_dictionary) - Deserializes string back into a dictionary
- [string_to_list](#string_to_list) - Converts string to list of characters or substrings
- [subslices](#subslices) - Returns all contiguous non-empty subslices
- [sum_of_squares](#sum_of_squares) - Adds up squares of input values
- [switch_case](#switch_case) - Evaluates expression against values and returns matching result

**T**
- [tabulate](#tabulate) - Returns function(0), function(1), etc.
- [tail](#tail) - Returns iterator over last n items
- [take](#take) - Returns first n items as list
- [totient](#totient) - Counts natural numbers coprime to n
- [transpose](#transpose) - Swaps rows and columns of matrix
- [tuple_to_list](#tuple_to_list) - Converts a tuple into a list
- [tuple_to_set](#tuple_to_set) - Converts a tuple into a set
- [tuple_to_string](#tuple_to_string) - Converts tuple to string representation with separator

**U**
- [unique](#unique) - Yields unique elements in sorted order
- [unique_everseen](#unique_everseen) - Yields unique elements remembering all seen
- [unique_justseen](#unique_justseen) - Yields unique elements preserving order
- [unique_list](#unique_list) - Returns list containing only unique elements
- [unique_tuple_list](#unique_tuple_list) - Removes duplicate tuples based on first element

**X**
- [xor_all](#xor_all) - Returns True if an odd number of arguments are True

---

## Collection Conversions

Functions for converting between different Python collection types and strings.

### convert_collection

Converts a list, tuple, or set to a specified target collection type.

**Description:**
This function takes an input collection (list, tuple, or set) and converts it to the desired target type. It handles type conversions between these three common collection types.

**Args:**
- `data_collection` (Union[List[Any], Tuple[Any, ...], Set[Any]]): The input collection to convert
- `target_type` (Type[Union[List, Tuple, Set]]): The desired type for the output collection

**Returns:**
- Union[List[Any], Tuple[Any, ...], Set[Any]]: The converted collection of the specified type

**Raises:**
- TypeError: If data_collection or target_type is not a list, tuple, or set

**Usage Example:**
```python
>>> convert_collection([1, 'a', 3.5], tuple)
(1, 'a', 3.5)
>>> convert_collection((1, 2, 2, 'a'), set)
{1, 2, 'a'}
```

**Cost:** O(n), where n is the number of elements in the input collection

---

### set_to_string

Converts a given set to its string representation.

**Description:**
Takes a set and converts its elements into a single string, joined by a specified separator. Optionally wraps string elements in single quotes. Returns None if the input set is empty.

**Args:**
- `input_set` (Set[Any]): The set to be converted
- `separator` (str): The string used to join the elements. Defaults to a single space
- `use_quotes` (bool): If True, wraps string elements in single quotes. Defaults to False

**Returns:**
- Optional[str]: The string representation of the set, or None if empty

**Raises:**
- TypeError: If the input is not a set

**Usage Example:**
```python
>>> set_to_string({'apple', 'banana'}, separator=', ', use_quotes=True)
"'apple', 'banana'"
>>> set_to_string({1, 2, 3}, separator='-')
"1-2-3"
```

**Cost:** O(n), where n is the number of elements in the set

---

### set_to_list

Converts a given set into a list.

**Description:**
Takes a set as input and returns a new list containing all the elements from the set. The order of elements in the resulting list is not guaranteed.

**Args:**
- `input_set` (Set[Any]): The set to be converted to a list

**Returns:**
- List[Any]: A list containing the elements from the input set

**Raises:**
- TypeError: If the input is not a set

**Usage Example:**
```python
>>> set_to_list({1, 2, 3})
[1, 2, 3]
>>> set_to_list(set())
[]
```

**Cost:** O(n), where n is the number of elements in the set

---

### set_to_tuple

Converts a given set into a tuple.

**Description:**
Takes a set as input and returns a new tuple containing all the elements from the set. The order of elements is not guaranteed.

**Args:**
- `input_set` (Set[Any]): The set to be converted to a tuple

**Returns:**
- Tuple[Any, ...]: A tuple containing the elements from the input set

**Raises:**
- TypeError: If the input is not a set

**Usage Example:**
```python
>>> set_to_tuple({1, 2, 3})
(1, 2, 3)
>>> set_to_tuple(set())
()
```

**Cost:** O(n), where n is the number of elements in the set

---

### tuple_to_string

Converts a given tuple to its string representation.

**Description:**
Takes a tuple and converts its elements into a single string, joined by a specified separator. Optionally wraps string elements in single quotes.

**Args:**
- `input_tuple` (Tuple[Any, ...]): The tuple to be converted
- `separator` (str): The string used to join the elements. Defaults to a single space
- `use_quotes` (bool): If True, wraps string elements in single quotes. Defaults to False

**Returns:**
- Optional[str]: The string representation of the tuple, or None if empty

**Raises:**
- TypeError: If the input is not a tuple

**Usage Example:**
```python
>>> tuple_to_string(('apple', 'banana', 'orange'), separator=', ', use_quotes=True)
"'apple', 'banana', 'orange'"
>>> tuple_to_string((1, 2, 3), separator='-')
"1-2-3"
```

**Cost:** O(n), where n is the number of elements in the tuple

---

### tuple_to_list

Converts a given tuple into a list.

**Description:**
Takes a tuple as input and returns a new list containing all the elements from the tuple, maintaining their original order.

**Args:**
- `input_tuple` (Tuple[Any, ...]): The tuple to be converted to a list

**Returns:**
- List[Any]: A list containing the elements from the input tuple

**Raises:**
- TypeError: If the input is not a tuple

**Usage Example:**
```python
>>> tuple_to_list((1, 2, 3, 4, 5))
[1, 2, 3, 4, 5]
>>> tuple_to_list(())
[]
```

**Cost:** O(n), where n is the number of elements in the tuple

---

### tuple_to_set

Converts a given tuple into a set.

**Description:**
Takes a tuple as input and returns a new set containing all the unique elements from the tuple. The order is not preserved.

**Args:**
- `input_tuple` (Tuple[Any, ...]): The tuple to be converted to a set

**Returns:**
- Set[Any]: A set containing the unique elements from the input tuple

**Raises:**
- TypeError: If the input is not a tuple

**Usage Example:**
```python
>>> tuple_to_set((1, 2, 2, 3, 4, 4, 5))
{1, 2, 3, 4, 5}
>>> tuple_to_set(())
set()
```

**Cost:** O(n), where n is the number of elements in the tuple

---

### list_to_string

Converts a list to its string representation.

**Description:**
Takes a list and converts its elements into a single string, joined by a specified separator. Optionally wraps string elements in single quotes.

**Args:**
- `lst` (List[Any]): The list to be converted
- `separator` (str): The string used to join the elements. Defaults to a single space
- `use_quotes` (bool): If True, wraps string elements in single quotes. Defaults to False

**Returns:**
- Optional[str]: The string representation of the list, or None if empty

**Raises:**
- TypeError: If the input is not a list

**Usage Example:**
```python
>>> list_to_string(['apple', 'banana', 'orange'], separator=', ', use_quotes=True)
"'apple', 'banana', 'orange'"
>>> list_to_string([1, 2, 3], separator='-')
"1-2-3"
```

**Cost:** O(n), where n is the number of elements in the list

---

### list_to_set

Converts a given list into a set.

**Description:**
Takes a list as input and returns a new set containing all the unique elements from the list. The order is not preserved.

**Args:**
- `input_list` (List[Any]): The list to be converted to a set

**Returns:**
- Set[Any]: A set containing the unique elements from the input list

**Raises:**
- TypeError: If the input is not a list

**Usage Example:**
```python
>>> list_to_set([1, 2, 2, 3, 4, 4, 5])
{1, 2, 3, 4, 5}
>>> list_to_set([])
set()
```

**Cost:** O(n), where n is the number of elements in the list

---

### list_to_tuple

Converts a given list into a tuple.

**Description:**
Takes a list as input and returns a new tuple containing all the elements from the list, maintaining their order.

**Args:**
- `input_list` (List[Any]): The list to be converted to a tuple

**Returns:**
- Tuple[Any, ...]: A tuple containing the elements from the input list

**Raises:**
- TypeError: If the input is not a list

**Usage Example:**
```python
>>> list_to_tuple([1, 2, 3, 4, 5])
(1, 2, 3, 4, 5)
>>> list_to_tuple([])
()
```

**Cost:** O(n), where n is the number of elements in the list

---

### dictionary_to_string

Converts a dictionary into a string representation.

**Description:**
Serializes a dictionary into a string where keys and values are separated by colons and key-value pairs are separated by semicolons.

**Args:**
- `input_dict` (dict): The dictionary to convert

**Returns:**
- str: A string representation of the input dictionary

**Raises:**
- TypeError: If the input_dict is not a dictionary

**Usage Example:**
```python
>>> dictionary_to_string({"name": "Alice", "age": "30", "city": "New York"})
'name:Alice;age:30;city:New York'
```

**Cost:** O(n), where n is the total number of characters in the dictionary's keys and values

---

### string_to_dictionary

Converts a string representation back into a dictionary.

**Description:**
Deserializes a string, previously created by dictionary_to_string(), back into a dictionary.

**Args:**
- `input_string` (str): The string to convert

**Returns:**
- dict: A dictionary reconstructed from the input string

**Raises:**
- TypeError: If the input_string is not a string
- ValueError: If the input_string format is invalid

**Usage Example:**
```python
>>> string_to_dictionary('name:Alice;age:30;city:New York')
{'name': 'Alice', 'age': '30', 'city': 'New York'}
```

**Cost:** O(n), where n is the length of the input string

---

### dictionary_keys_to_list

Returns the keys of a dictionary as a list.

**Args:**
- `data_dict` (Dict[Any, Any]): The input dictionary

**Returns:**
- List[Any]: A list containing all keys from the dictionary

**Usage Example:**
```python
>>> dictionary_keys_to_list({"name": "Alice", "age": 30})
['name', 'age']
```

**Cost:** O(n), where n is the number of keys in the dictionary

---

### dict_values_to_list

Returns the values of a dictionary as a list.

**Args:**
- `data_dict` (Dict[Any, Any]): The input dictionary

**Returns:**
- List[Any]: A list containing all values from the dictionary

**Usage Example:**
```python
>>> dict_values_to_list({"item": "Laptop", "price": 1200})
['Laptop', 1200]
```

**Cost:** O(n), where n is the number of values in the dictionary

---

### dictionary_items_to_list_of_tuples

Returns the key-value pairs (items) of a dictionary as a list of tuples.

**Args:**
- `data_dict` (Dict[Any, Any]): The input dictionary

**Returns:**
- List[Tuple[Any, Any]]: A list where each element is a (key, value) tuple

**Usage Example:**
```python
>>> dictionary_items_to_list_of_tuples({"city": "London", "population": 9000000})
[('city', 'London'), ('population', 9000000)]
```

**Cost:** O(n), where n is the number of items in the dictionary

---

### dictionary_keys_to_set

Returns the keys of a dictionary as a set.

**Args:**
- `data_dict` (Dict[Any, Any]): The input dictionary

**Returns:**
- Set[Any]: A set containing all unique keys from the dictionary

**Usage Example:**
```python
>>> dict_keys_to_set({"color": "red", "value": 50})
{'color', 'value'}
```

**Cost:** O(n), where n is the number of keys in the dictionary

---

### dictionary_values_to_set

Returns the values of a dictionary as a set, removing duplicates.

**Args:**
- `data_dict` (Dict[Any, Any]): The input dictionary

**Returns:**
- Set[Any]: A set containing all unique values from the dictionary

**Usage Example:**
```python
>>> dictionary_values_to_set({"a": 1, "b": 2, "c": 1})
{1, 2}
```

**Cost:** O(n), where n is the number of values in the dictionary

---

### dictionary_to_object

Converts a dictionary into a simple object.

**Description:**
Dynamically creates a class and assigns the dictionary's key-value pairs as attributes to an instance of that class.

**Args:**
- `dictionary` (dict): The dictionary to convert

**Returns:**
- object: An object with attributes corresponding to the dictionary's keys

**Raises:**
- TypeError: If the input is not a dictionary

**Usage Example:**
```python
>>> my_dict = {'name': 'Alice', 'age': 30}
>>> my_object = dictionary_to_object(my_dict)
>>> print(my_object.name)
Alice
```

**Cost:** O(n), where n is the number of keys in the dictionary

---

### dictionary_items_to_set_of_tuples

Returns the key-value pairs (items) of a dictionary as a set of tuples.

**Args:**
- `data_dict` (Dict[Any, Any]): The input dictionary

**Returns:**
- Set[Tuple[Any, Any]]: A set where each element is a unique (key, value) tuple

**Usage Example:**
```python
>>> dictionary_items_to_set_of_tuples({"id": 101, "status": "active"})
{('id', 101), ('status', 'active')}
```

**Cost:** O(n), where n is the number of items in the dictionary

---

### list_of_tuples_to_dict

Converts a list of tuples (key-value pairs) to a dictionary.

**Description:**
If there are duplicate keys, the value from the last tuple with that key will prevail.

**Args:**
- `data_list` (List[Tuple[Any, Any]]): The input list of (key, value) tuples

**Returns:**
- Dict[Any, Any]: The converted dictionary

**Usage Example:**
```python
>>> list_of_tuples_to_dict([("a", 1), ("b", 2), ("a", 3)])
{'a': 3, 'b': 2}
```

**Cost:** O(n), where n is the number of tuples in the list

---

### list_of_lists_to_dict

Converts a list of lists (key-value pairs) to a dictionary.

**Description:**
If there are duplicate keys, the value from the last inner list with that key will prevail.

**Args:**
- `data_list` (List[List[Any]]): The input list of [key, value] lists

**Returns:**
- Dict[Any, Any]: The converted dictionary

**Usage Example:**
```python
>>> list_of_lists_to_dict([["name", "Bob"], ["age", 25], ["name", "Robert"]])
{'name': 'Robert', 'age': 25}
```

**Cost:** O(n), where n is the number of lists

---

### list_of_dicts_to_merged_dict

Merges a list of dictionaries into a single dictionary.

**Description:**
If there are duplicate keys across the dictionaries, the value from the last dictionary in the list will take precedence.

**Args:**
- `list_of_dicts` (List[Dict[Any, Any]]): A list of dictionaries to be merged

**Returns:**
- Dict[Any, Any]: The single merged dictionary

**Usage Example:**
```python
>>> list_of_dicts_to_merged_dict([{"a": 1, "b": 2}, {"b": 3, "c": 4}, {"d": 5}])
{'a': 1, 'b': 3, 'c': 4, 'd': 5}
```

**Cost:** O(n*m), where n is the number of dictionaries and m is the average number of keys per dictionary

---

### string_to_list

Converts a string into a list of substrings or individual characters.

**Description:**
If split_by_character is provided, splits by that delimiter. Otherwise, converts to a list of individual characters.

**Args:**
- `input_string` (Optional[str]): The string to be converted
- `split_by_character` (Optional[str]): Delimiter for splitting. If None, split into characters

**Returns:**
- Optional[List[str]]: A list of strings, empty list for empty string, None for None input

**Raises:**
- TypeError: If input types are invalid

**Usage Example:**
```python
>>> string_to_list("hello world")
['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
>>> string_to_list("apple,banana,orange", split_by_character=",")
['apple', 'banana', 'orange']
```

**Cost:** O(n), where n is the length of the input string

---

## Collection Operations

Functions for advanced operations on Python collections.

### merge_json_strings

Merges two JSON strings (representing JSON objects) into a new JSON string.

**Description:**
If both JSONs contain the same keys, the values from the second JSON will overwrite the values from the first.

**Args:**
- `json_str_1` (str): The first JSON string to merge
- `json_str_2` (str): The second JSON string to merge

**Returns:**
- str: A new JSON string representing the merged object

**Raises:**
- json.JSONDecodeError: If either input string is not valid JSON
- TypeError: If either input does not represent a JSON object

**Usage Example:**
```python
>>> merge_json_strings('{"name": "Alice", "age": 30}', '{"age": 31, "city": "New York"}')
'{"name": "Alice", "age": 31, "city": "New York"}'
```

**Cost:** O(n + m), where n and m are the number of keys in the two dictionaries

---

### add_to_tuple

Adds an element to the end of a tuple.

**Description:**
Since tuples are immutable, this creates and returns a new tuple with the value appended.

**Args:**
- `p_tuple` (Tuple[Any, ...]): The original tuple
- `p_value` (Any): The new value to append

**Returns:**
- Tuple[Any, ...]: A new tuple with the value appended

**Usage Example:**
```python
>>> add_to_tuple((1, 2), 3)
(1, 2, 3)
>>> add_to_tuple((), "hello")
('hello',)
```

**Cost:** O(n), where n is the number of elements in the tuple

---

### unique_list

Returns a new list containing only the unique elements from the original list.

**Description:**
The order of elements in the resulting list is not guaranteed, as a set is used internally for deduplication.

**Args:**
- `p_list` (List[Any]): The input list which may contain duplicate elements

**Returns:**
- List[Any]: A new list containing all unique elements

**Usage Example:**
```python
>>> unique_list([1, 2, 2, 3, 1])
[1, 2, 3]
```

**Cost:** O(n), where n is the number of elements in the list

---

### unique_tuple_list

Removes duplicate tuples from a list based on the first element of each tuple.

**Description:**
Returns a new list containing only the unique tuples, maintaining the order of their first appearance.

**Args:**
- `p_list` (list[tuple]): The input list of tuples

**Returns:**
- list[tuple]: A new list containing the unique tuples

**Usage Example:**
```python
>>> unique_tuple_list([(1, 'apple'), (2, 'banana'), (1, 'orange'), (3, 'grape')])
[(1, 'apple'), (2, 'banana'), (3, 'grape')]
```

**Cost:** O(n), where n is the number of tuples in the list

---

### flatten_list

Flattens a list of lists into a single, one-dimensional list.

**Args:**
- `p_list` (list[list]): The input list of lists

**Returns:**
- list: A new list containing all elements from the sublists

**Usage Example:**
```python
>>> flatten_list([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
[1, 2, 3, 4, 5, 6, 7, 8, 9]
```

**Cost:** O(n), where n is the total number of elements across all sublists

---

### list_intersection

Finds the intersection of two lists, returning a set of common elements.

**Description:**
Filters out any falsy values (None, 0, '') from the input lists before finding the intersection.

**Args:**
- `p_list1` (list): The first input list
- `p_list2` (list): The second input list

**Returns:**
- set: A set containing elements present in both filtered lists

**Usage Example:**
```python
>>> list_intersection([1, 2, None, 3, 4, 0, 5], [3, 4, 5, 6, '', 7])
{3, 4, 5}
```

**Cost:** O(n + m), where n and m are the lengths of the two lists

---

### list_has_list

Checks if all elements from one list exist in another list, regardless of order.

**Args:**
- `container_list` (list): The larger list to search within
- `search_list` (list): The list whose elements we want to find

**Returns:**
- bool: True if all elements in search_list exist in container_list

**Raises:**
- TypeError: If either argument is not a list
- ValueError: If either list is empty

**Usage Example:**
```python
>>> list_has_list(['a', 'b', 'c', 'd'], ['b', 'c'])
True
>>> list_has_list(['a', 'b', 'c'], ['b', 'd'])
False
```

**Cost:** O(n * m), where n and m are the lengths of the lists

---

### is_subsequence

Checks if sub_sequence is a subsequence of main_sequence, maintaining element order.

**Description:**
Works correctly for ordered sequence types like lists and tuples. Does not apply to unordered collections like sets.

**Args:**
- `sub_sequence` (Sequence[Hashable]): The potential subsequence
- `main_sequence` (Sequence[Hashable]): The main sequence to check against

**Returns:**
- bool: True if sub_sequence is a subsequence of main_sequence

**Usage Example:**
```python
>>> is_subsequence(["apple", "banana"], ["orange", "apple", "grape", "banana", "kiwi"])
True
>>> is_subsequence(["banana", "apple"], ["orange", "apple", "grape", "banana", "kiwi"])
False
```

**Cost:** O(n * m), where n is the length of sub_sequence and m is the length of main_sequence

---

### filter_elements_by_another

Filters elements from a main collection that are also present in a filter criteria collection.

**Description:**
Accepts lists, tuples, or sets as input and returns results in the specified output type.

**Args:**
- `main_collection` (Iterable): The collection from which elements will be filtered
- `filter_criteria` (Iterable): The collection containing elements to use as a filter
- `return_type` (str): The desired type of the returned collection ('list', 'tuple', or 'set')

**Returns:**
- Union[list, tuple, set]: A new collection containing only elements present in both collections

**Raises:**
- TypeError: If inputs are not recognized iterable types
- ValueError: If return_type is invalid

**Usage Example:**
```python
>>> filter_elements_by_another({1, 2, 3, 4, 5}, [2, 4, 6], return_type="set")
{2, 4}
>>> filter_elements_by_another(("a", "b", "c", "d"), {"b", "d", "e"}, return_type="list")
['b', 'd']
```

**Cost:** O(n + m), where n and m are the sizes of the collections

---

### pick_in_collection

Permite al usuario seleccionar una o varias opciones de cualquier colección iterable numerada.

**Description:**
Interactive function that displays a numbered list of items from any iterable collection and allows the user to select one or multiple options. Supports returning either the selected values or their indices.

**Args:**
- `collection` (Iterable): A collection of elements (list, tuple, set, etc.) from which the user can choose
- `prompt` (str): Message to display to the user before the list of options. Defaults to "Por favor, selecciona una opción:"
- `allow_multiple` (bool): If True, user can select multiple options separated by commas. Defaults to False
- `return_index` (bool): If True, returns the index/indices instead of the value/values. Defaults to False
- `exit_on_cancel` (bool): If True, the program terminates if user enters 'q' or 'cancelar'. Defaults to False

**Returns:**
- Union[Any, List[Any], int, List[int], None]: 
  - The selected element (if allow_multiple is False)
  - A list of selected elements (if allow_multiple is True)
  - The index of selected element (if return_index is True and allow_multiple is False)
  - A list of indices (if return_index is True and allow_multiple is True)
  - None if the user cancels

**Raises:**
- TypeError: If the collection is not iterable
- ValueError: If the collection is empty

**Usage Example:**
```python
>>> colores_tuple = ("Rojo", "Verde", "Azul", "Amarillo")
>>> color_elegido = pick_in_collection(colores_tuple, "Elige tu color favorito:")
# Displays:
# Por favor, selecciona una opción:
#   1. Rojo
#   2. Verde
#   3. Azul
#   4. Amarillo

>>> numeros_set = {10, 20, 30, 40, 50}
>>> numeros_elegidos = pick_in_collection(numeros_set, "Elige algunos números:", allow_multiple=True)
# User can enter: 1,3,5
```

**Cost:** O(n) for displaying options, O(1) for selection

---

### merge_elements

Merges two collections into a single collection of the specified type.

**Description:**
Accepts lists, tuples, or sets as input. Can optionally remove duplicates from the result.

**Args:**
- `first_collection` (Iterable): The first collection to merge
- `second_collection` (Iterable): The second collection to merge
- `return_type` (str): The desired type ('list', 'tuple', or 'set'). Defaults to 'list'
- `remove_duplicates` (bool): If True, removes duplicates. Defaults to False

**Returns:**
- Union[list, tuple, set]: A new collection containing all elements from both collections

**Raises:**
- TypeError: If inputs are not recognized iterable types
- ValueError: If return_type is invalid

**Usage Example:**
```python
>>> merge_elements([1, 2, 3], [4, 5, 6], return_type="list")
[1, 2, 3, 4, 5, 6]
>>> merge_elements([1, 2, 2, 3], [3, 4, 4, 5], return_type="list", remove_duplicates=True)
[1, 2, 3, 4, 5]
```

**Cost:** O(n + m), where n and m are the lengths of the input collections

---

### collection_filter

Filters an iterable based on a provided filtering function.

**Args:**
- `collection` (Iterable[Any]): The iterable to filter
- `filter_logic_func` (Callable[[Any], bool]): A function that returns True for items to include

**Returns:**
- Union[List[Any], Tuple[Any, ...], Set[Any]]: A new collection of the same type containing only filtered items

**Raises:**
- TypeError: If collection is not iterable or filter_logic_func is not callable

**Usage Example:**
```python
>>> numbers = [1, 2, 3, 4, 5, 6]
>>> is_even = lambda x: x % 2 == 0
>>> collection_filter(numbers, is_even)
[2, 4, 6]
```

**Cost:** O(n), where n is the number of elements in the collection

---

### dictionary_filter_by_keys

Filters a dictionary, returning a new dictionary with only the specified keys.

**Args:**
- `input_dict` (dict): The original dictionary to filter
- `keys_to_include` (list): A list of keys that should be included in the new dictionary

**Returns:**
- dict: A new dictionary containing only the specified key-value pairs

**Raises:**
- TypeError: If inputs are not of correct types

**Usage Example:**
```python
>>> original_data = {"name": "Charlie", "age": 45, "city": "London", "email": "charlie@example.com"}
>>> dictionary_filter_by_keys(original_data, ["name", "city"])
{'name': 'Charlie', 'city': 'London'}
```

**Cost:** O(m), where m is the number of keys in keys_to_include

---

### combine_dictionaries

Performs union or intersection operations on two dictionaries.

**Args:**
- `dict_one` (dict): The first dictionary
- `dict_two` (dict): The second dictionary
- `operation` (str): The type of operation ('union' or 'intersection')

**Returns:**
- dict: A new dictionary resulting from the specified operation

**Raises:**
- ValueError: If an unsupported operation type is provided

**Usage Example:**
```python
>>> dict_a = {'a': 1, 'b': 2, 'c': 3}
>>> dict_b = {'b': 4, 'd': 5}
>>> combine_dictionaries(dict_a, dict_b, 'union')
{'a': 1, 'b': 4, 'c': 3, 'd': 5}
>>> combine_dictionaries(dict_a, dict_b, 'intersection')
{'b': 4}
```

**Cost:** O(n + m) for union, O(min(n, m)) for intersection

---

### dictionary_rename_keys

Renames keys in a dictionary based on a provided mapping.

**Description:**
Creates a new dictionary with keys renamed according to the mapping. Keys not in the mapping are kept as is.

**Args:**
- `original_dict` (dict): The dictionary whose keys are to be renamed
- `key_mapping` (dict): A dictionary where keys are old names and values are new names

**Returns:**
- dict: A new dictionary with the keys renamed

**Raises:**
- TypeError: If inputs are not dictionaries

**Usage Example:**
```python
>>> my_dict = {"name": "Alice", "age": 30}
>>> mapping = {"name": "full_name", "age": "person_age"}
>>> dictionary_rename_keys(my_dict, mapping)
{'full_name': 'Alice', 'person_age': 30}
```

**Cost:** O(n), where n is the number of items in the original dictionary

---

### execute_os_command

Executes a command in the underlying operating system and captures its output.

**Description:**
Provides a secure and flexible way to interact with the shell or directly execute programs.

**Args:**
- `command` (Union[str, list[str]]): The command to execute (string for shell, list for direct)

**Returns:**
- Tuple[int, str, str]: Return code, stdout, and stderr

**Raises:**
- TypeError: If the command argument is not a string or list of strings
- FileNotFoundError: If the command or executable is not found

**Usage Example:**
```python
>>> return_code, stdout, stderr = execute_os_command("echo Hello")
>>> print(f"Return Code: {return_code}")
>>> print(f"Output: {stdout}")
```

**Cost:** Depends on the executed command

---

### calculate

Evaluates a compound arithmetic expression from a string.

**Description:**
Safely evaluates a mathematical expression, respecting order of operations (PEMDAS). Handles implicit multiplication.

**Args:**
- `expression_string` (str): The mathematical expression to be evaluated

**Returns:**
- Union[int, float]: The numerical result of the expression

**Raises:**
- ValueError: If the expression is invalid or contains errors

**Usage Example:**
```python
>>> calculate("3 + 4 * 5")
23
>>> calculate("2 * 3(6 / 2) - 9 + 6")
15.0
```

**Cost:** O(n), where n is the length of the expression

---

### search

Searches for a target element within an iterable collection.

**Description:**
Iterates through the collection to find the first occurrence of the target element.

**Args:**
- `collection` (Iterable[Any]): The collection to be searched
- `target_element` (Any): The element to search for

**Returns:**
- Optional[Any]: The found element, or None if not found

**Raises:**
- TypeError: If the collection is not an iterable

**Usage Example:**
```python
>>> my_list = [1, 2, 3, 4, 5]
>>> search(my_list, 3)
3
>>> search(my_list, 6)
None
```

**Cost:** O(n), where n is the number of elements in the collection

---

### collection_avg

Calculates the average of the numeric values in an iterable collection.

**Description:**
This function is equivalent to the SQL aggregate function AVG and allows calculating the average of numeric values in any iterable collection.

**Args:**
- `collection` (Iterable[Union[int, float]]): Collection of numeric values
- `ignore_none` (bool): If True, ignores None values in the calculation. Defaults to True

**Returns:**
- Optional[float]: The average of the values, or None if the collection is empty or contains no valid values

**Raises:**
- TypeError: If the collection is not iterable or contains non-numeric values

**Usage Example:**
```python
>>> collection_avg([1, 2, 3, 4, 5])
3.0
>>> collection_avg([10, 20, None, 30], ignore_none=True)
20.0
>>> collection_avg((5.5, 10.5, 15.5))
10.5
```

**Cost:** O(n), where n is the number of elements in the collection

---

### collection_count

Counts the number of elements in an iterable collection.

**Description:**
This function is equivalent to the SQL aggregate function COUNT and allows counting elements in any iterable collection, with an option to ignore None values.

**Args:**
- `collection` (Iterable[Any]): The collection to count
- `ignore_none` (bool): If True, does not count None values. Defaults to True (similar to COUNT(field) in SQL)

**Returns:**
- int: The number of elements in the collection

**Raises:**
- TypeError: If the argument is not an iterable

**Usage Example:**
```python
>>> collection_count([1, 2, 3, 4, 5])
5
>>> collection_count([1, None, 3, None, 5], ignore_none=True)
3
>>> collection_count([1, None, 3, None, 5], ignore_none=False)
5
```

**Cost:** O(n), where n is the number of elements in the collection

---

### collection_max

Returns the highest value in an iterable collection.

**Description:**
This function is equivalent to the SQL aggregate function MAX and allows finding the maximum value in any iterable collection.

**Args:**
- `collection` (Iterable[Any]): The collection to search for the maximum
- `ignore_none` (bool): If True, ignores None values in the calculation. Defaults to True

**Returns:**
- Optional[Any]: The maximum value in the collection, or None if it is empty or contains only None

**Raises:**
- TypeError: If the collection is not iterable
- ValueError: If the collection is empty after filtering None

**Usage Example:**
```python
>>> collection_max([1, 5, 3, 9, 2])
9
>>> collection_max(['apple', 'zebra', 'banana'])
'zebra'
>>> collection_max([1.5, None, 3.7, 2.1], ignore_none=True)
3.7
```

**Cost:** O(n), where n is the number of elements in the collection

---

### collection_min

Returns the smallest value in an iterable collection.

**Description:**
This function is equivalent to the SQL aggregate function MIN and allows finding the minimum value in any iterable collection.

**Args:**
- `collection` (Iterable[Any]): The collection to search for the minimum
- `ignore_none` (bool): If True, ignores None values in the calculation. Defaults to True

**Returns:**
- Optional[Any]: The minimum value in the collection, or None if it is empty or contains only None

**Raises:**
- TypeError: If the collection is not iterable
- ValueError: If the collection is empty after filtering None

**Usage Example:**
```python
>>> collection_min([5, 1, 9, 3, 2])
1
>>> collection_min(['zebra', 'apple', 'banana'])
'apple'
>>> collection_min([3.7, None, 1.5, 2.1], ignore_none=True)
1.5
```

**Cost:** O(n), where n is the number of elements in the collection

---

### collection_stdev

Calculates the standard deviation of the values in an iterable collection.

**Description:**
This function is equivalent to the SQL aggregate functions STDEV (sample) and STDEVP (population), allowing the calculation of standard deviation in any iterable collection.

**Args:**
- `collection` (Iterable[Union[int, float]]): Collection of numeric values
- `is_sample` (bool): If True, calculates for a sample (n-1). If False, calculates for a population (n). Defaults to True (equivalent to SQL's STDEV)
- `ignore_none` (bool): If True, ignores None values in the calculation. Defaults to True

**Returns:**
- Optional[float]: The standard deviation, or None if there is not enough data

**Raises:**
- TypeError: If the collection is not iterable or contains non-numeric values
- ValueError: If there are fewer than 2 values for a sample calculation

**Usage Example:**
```python
>>> collection_stdev([2, 4, 4, 4, 5, 5, 7, 9])
2.138089935299395
>>> collection_stdev([2, 4, 4, 4, 5, 5, 7, 9], is_sample=False)
2.0
>>> collection_stdev([10, None, 20, 30], ignore_none=True)
10.0
```

**Cost:** O(n), where n is the number of elements in the collection

---

### collection_sum

Calculates the sum of the numeric values in an iterable collection.

**Description:**
This function is equivalent to the SQL aggregate function SUM and allows summing numeric values in any iterable collection.

**Args:**
- `collection` (Iterable[Union[int, float]]): Collection of numeric values
- `ignore_none` (bool): If True, ignores None values in the calculation. Defaults to True

**Returns:**
- Union[int, float]: The sum of the values. Returns 0 if the collection is empty

**Raises:**
- TypeError: If the collection is not iterable or contains non-numeric values

**Usage Example:**
```python
>>> collection_sum([1, 2, 3, 4, 5])
15
>>> collection_sum([10, None, 20, 30], ignore_none=True)
60
>>> collection_sum((5.5, 10.5, 15.5))
31.5
```

**Cost:** O(n), where n is the number of elements in the collection

---

## Python Tools

High-level utility functions for Python programming patterns.

### create_key_value_dictionary

Creates a dictionary by mapping key column names to their corresponding values.

**Description:**
Takes a string or list of key column names and values, then combines them into a dictionary.

**Args:**
- `p_key_columns` (str or list): Comma-separated string or list of column names
- `p_values` (any or tuple): A single value or tuple of values

**Returns:**
- dict: A dictionary where keys are column names and values are the corresponding input values

**Raises:**
- ValueError: If the number of key columns doesn't match the number of values

**Usage Example:**
```python
>>> create_key_value_dictionary("id,name", (1, "Alice"))
{'id': 1, 'name': 'Alice'}
>>> create_key_value_dictionary(["product_id"], "P123")
{'product_id': 'P123'}
```

**Cost:** O(n), where n is the number of key columns

---

### function_call

Higher-order function that executes a callable with optional arguments.

**Description:**
This function provides a simple abstraction for executing any callable object, allowing you to pass both positional and keyword arguments. It's useful for building functional programming patterns and creating flexible execution flows.

**Args:**
- `func` (callable): The function to execute
- `*args`: Positional arguments to pass to the function
- `**kwargs`: Keyword arguments to pass to the function

**Returns:**
- `Any`: The return value of the executed function

**Raises:**
- TypeError: If func is not callable

**Usage Example:**
```python
from formulite.fxPython.py_tools import function_call

def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

function_call(greet, "Alice")  # 'Hello, Alice!'
function_call(greet, "Bob", greeting="Hi")  # 'Hi, Bob!'
```

**Cost:** O(1) plus the cost of executing the provided function

---

### switch_case

Acts like a generic switch-case statement.

**Description:**
Iterates through a sequence of cases and returns the corresponding value if a match is found.

**Args:**
- `value`: The value to be evaluated
- `*cases`: A sequence of key-value pairs
- `default`: The value to return if no match is found

**Returns:**
- The value associated with the matching key, or the default value

**Raises:**
- ValueError: If the number of items in cases is not even

**Usage Example:**
```python
>>> month_name = switch_case(2, 1, "January", 2, "February", 3, "March", default="Unknown")
>>> print(month_name)
February
```

**Cost:** O(n), where n is the number of case pairs

---

### loop_for

Executes a function for each item in an iterable, simulating a for loop.

**Args:**
- `iterable`: An iterable object to loop over
- `func`: A callable function that takes a single argument

**Usage Example:**
```python
>>> my_list = [1, 2, 3]
>>> loop_for(my_list, lambda x: print(f"Item: {x}"))
Item: 1
Item: 2
Item: 3
```

**Cost:** O(n), where n is the number of items in the iterable

---

### loop_while

Executes a function repeatedly as long as a specified condition is true.

**Args:**
- `condition`: A callable that returns a boolean
- `func`: A callable function executed in each iteration
- `*args`: Positional arguments to pass to both functions
- `**kwargs`: Keyword arguments to pass to both functions

**Usage Example:**
```python
>>> count = [0]
>>> loop_while(lambda c: c[0] < 5, lambda c: c[0] += 1 or print(c[0]), count)
```

**Cost:** O(k), where k is the number of iterations until condition becomes False

---

### rotate

Rotates the elements of an iterable.

**Description:**
Rotates elements by a specified number of steps. Positive steps rotate right, negative rotate left.

**Args:**
- `iterable`: The collection to be rotated
- `steps` (int): The number of positions to rotate. Defaults to 1

**Returns:**
- list: A new list with the elements rotated

**Usage Example:**
```python
>>> rotate([1, 2, 3, 4])
[4, 1, 2, 3]
>>> rotate([1, 2, 3, 4], steps=-2)
[3, 4, 1, 2]
```

**Cost:** O(n), where n is the number of elements in the iterable

---

### shift

Shifts an iterable, adding or removing elements.

**Description:**
Modifies an iterable by shifting elements and optionally adding new elements from another iterable.

**Args:**
- `iterable` (Iterable[Any]): The collection to be shifted
- `direction` (str): The shift direction ('left' or 'right')
- `new_elements` (Iterable[Any]): An iterable of elements to add

**Returns:**
- list[Any]: A new list representing the shifted collection

**Raises:**
- ValueError: If an invalid direction is provided

**Usage Example:**
```python
>>> shift([1, 2, 3, 4])
[2, 3, 4]
>>> shift([1, 2, 3, 4], direction='left', new_elements=(5, 6, 7))
[2, 3, 4, 5, 6, 7]
```

**Cost:** O(n + m), where n is the size of the iterable and m is the number of new elements

---

### apply_expression

Applies a string expression to every item in an iterable and returns a list.

**Description:**
Dynamically creates a lambda function from a string expression for data transformations.

**Args:**
- `expression` (str): A string representing a Python expression (e.g., 'x * 2')
- `iterable` (Iterable[Any]): A collection of items to which the expression will be applied

**Returns:**
- list[Any]: A new list containing the results

**Raises:**
- SyntaxError: If the expression string is not valid

**Usage Example:**
```python
>>> apply_expression('x * x', [1, 2, 3, 4])
[1, 4, 9, 16]
>>> apply_expression('x.capitalize()', ['hello', 'world'])
['Hello', 'World']
```

**Cost:** O(n), where n is the number of items in the iterable

---

## Itertools Recipes

Advanced iterator utility functions based on Python's itertools documentation recipes.

### take

Return first n items of the iterable as a list.

**Args:**
- `n` (int): Number of items to take
- `iterable`: The iterable to take from

**Returns:**
- list: List of first n items

**Usage Example:**
```python
>>> take(3, [1,2,3,4,5])
[1,2,3]
```

**Cost:** O(n), where n is the number of items to take

---

### prepend

Prepend a single value in front of an iterable.

**Args:**
- `value`: The value to prepend
- `iterable`: The iterable to prepend to

**Returns:**
- iterator: Iterator with value prepended

**Usage Example:**
```python
>>> list(prepend(1, [2, 3, 4]))
[1, 2, 3, 4]
```

**Cost:** O(1) for creation, O(n) when consumed

---

### tabulate

Return function(0), function(1), ...

**Args:**
- `function`: The function to apply
- `start` (int): Starting index

**Returns:**
- iterator: Iterator of function applied to consecutive integers

**Usage Example:**
```python
>>> list(islice(tabulate(lambda x: x**2, 3), 5))
[9, 16, 25, 36, 49]
```

**Cost:** O(1) per element generated

---

### repeatfunc

Repeat calls to a function with specified arguments.

**Args:**
- `function`: The function to call
- `times` (int or None): Number of times to repeat, or None for infinite
- `*args`: Arguments to pass to the function

**Returns:**
- iterator: Iterator of function results

**Usage Example:**
```python
>>> list(repeatfunc(lambda: random.random(), 3))
[0.234, 0.567, 0.891]  # Random values
```

**Cost:** O(1) per function call

---

### flatten

Flatten one level of nesting.

**Args:**
- `list_of_lists`: Iterable of iterables to flatten

**Returns:**
- iterator: Flattened iterator

**Usage Example:**
```python
>>> list(flatten([[1,2], [3,4]]))
[1,2,3,4]
```

**Cost:** O(n), where n is the total number of elements

---

### ncycles

Returns the sequence elements n times.

**Args:**
- `iterable`: The iterable to cycle
- `n` (int): Number of cycles

**Returns:**
- iterator: Iterator repeating the sequence n times

**Usage Example:**
```python
>>> list(ncycles([1,2], 3))
[1,2,1,2,1,2]
```

**Cost:** O(n * m), where n is cycles and m is iterable length

---

### loops

Loop n times. Like range(n) but without creating integers.

**Args:**
- `n` (int): Number of loops

**Returns:**
- iterator: Iterator of None values

**Usage Example:**
```python
>>> for _ in loops(5): print("loop")
loop
loop
loop
loop
loop
```

**Cost:** O(1) for creation, O(n) when consumed

---

### tail

Return an iterator over the last n items.

**Args:**
- `n` (int): Number of last items
- `iterable`: The iterable

**Returns:**
- iterator: Iterator of last n items

**Usage Example:**
```python
>>> list(tail(3, 'ABCDEFG'))
['E', 'F', 'G']
```

**Cost:** O(m), where m is the total length of the iterable

---

### consume

Advance the iterator n-steps ahead. If n is None, consume entirely.

**Args:**
- `iterator`: The iterator to consume
- `n` (int or None): Number of steps or None

**Returns:**
- None

**Usage Example:**
```python
>>> it = iter([1,2,3,4,5])
>>> consume(it, 2)
>>> list(it)
[3, 4, 5]
```

**Cost:** O(n), where n is the number of steps

---

### nth

Returns the nth item or a default value.

**Args:**
- `iterable`: The iterable
- `n` (int): Index of item
- `default`: Default value if not found

**Returns:**
- The nth item or default

**Usage Example:**
```python
>>> nth([1,2,3], 1)
2
```

**Cost:** O(n)

---

### quantify

Given a predicate that returns True or False, count the True results.

**Args:**
- `iterable`: The iterable to check
- `predicate`: Function to apply

**Returns:**
- int: Count of True results

**Usage Example:**
```python
>>> quantify([1,2,3,4], lambda x: x > 2)
2
```

**Cost:** O(n), where n is the length of the iterable

---

### first_true

Returns the first true value or the default if there is no true value.

**Args:**
- `iterable`: The iterable
- `default`: Default value
- `predicate`: Function to check truthiness

**Returns:**
- First true value or default

**Usage Example:**
```python
>>> first_true([0,1,2], predicate=bool)
1
```

**Cost:** O(n) in worst case

---

### all_equal

Returns True if all the elements are equal to each other.

**Args:**
- `iterable`: The iterable
- `key`: Key function for comparison

**Returns:**
- bool: True if all equal

**Usage Example:**
```python
>>> all_equal([1,1,1])
True
>>> all_equal([1,2,1])
False
```

**Cost:** O(n) in worst case

---

### unique_justseen

Yield unique elements, preserving order. Remember only the element just seen.

**Args:**
- `iterable`: The iterable
- `key`: Key function

**Returns:**
- iterator: Unique elements

**Usage Example:**
```python
>>> list(unique_justseen('AAAABBBCCDAABBB'))
['A', 'B', 'C', 'D', 'A', 'B']
```

**Cost:** O(n), where n is the length of the iterable

---

### unique_everseen

Yield unique elements, preserving order. Remember all elements ever seen.

**Args:**
- `iterable`: The iterable
- `key`: Key function

**Returns:**
- iterator: Unique elements

**Usage Example:**
```python
>>> list(unique_everseen('AAAABBBCCDAABBB'))
['A', 'B', 'C', 'D']
```

**Cost:** O(n), where n is the length of the iterable

---

### unique

Yield unique elements in sorted order. Supports unhashable inputs.

**Args:**
- `iterable`: The iterable
- `key`: Key function
- `reverse` (bool): Sort in reverse

**Returns:**
- iterator: Unique sorted elements

**Usage Example:**
```python
>>> list(unique([[1, 2], [3, 4], [1, 2]]))
[[1, 2], [3, 4]]
```

**Cost:** O(n log n) due to sorting

---

### sliding_window

Collect data into overlapping fixed-length chunks or blocks.

**Args:**
- `iterable`: The iterable
- `n` (int): Window size

**Returns:**
- iterator: Iterator of tuples

**Usage Example:**
```python
>>> list(sliding_window('ABCDEFG', 4))
[('A','B','C','D'), ('B','C','D','E'), ('C','D','E','F'), ('D','E','F','G')]
```

**Cost:** O(n), where n is the length of the iterable

---

### grouper

Collect data into non-overlapping fixed-length chunks or blocks.

**Args:**
- `iterable`: The iterable
- `n` (int): Group size
- `incomplete`: How to handle incomplete groups ('fill', 'strict', 'ignore')
- `fillvalue`: Value to fill with

**Returns:**
- iterator: Iterator of tuples

**Raises:**
- ValueError: If incomplete is not 'fill', 'strict', or 'ignore'

**Usage Example:**
```python
>>> list(grouper('ABCDEFG', 3, fillvalue='x'))
[('A','B','C'), ('D','E','F'), ('G','x','x')]
```

**Cost:** O(n), where n is the length of the iterable

---

### roundrobin

Visit input iterables in a cycle until each is exhausted.

**Args:**
- `*iterables`: The iterables

**Returns:**
- iterator: Round-robin iterator

**Usage Example:**
```python
>>> list(roundrobin('ABC', 'D', 'EF'))
['A', 'D', 'E', 'B', 'F', 'C']
```

**Cost:** O(n), where n is the total number of elements

---

### subslices

Return all contiguous non-empty subslices of a sequence.

**Args:**
- `seq`: The sequence

**Returns:**
- iterator: Iterator of slices

**Usage Example:**
```python
>>> list(subslices('ABCD'))
['A', 'AB', 'ABC', 'ABCD', 'B', 'BC', 'BCD', 'C', 'CD', 'D']
```

**Cost:** O(n²), where n is the length of the sequence

---

### iter_index

Return indices where a value occurs in a sequence or iterable.

**Args:**
- `iterable`: The iterable
- `value`: Value to find
- `start` (int): Start index
- `stop` (int or None): Stop index

**Returns:**
- iterator: Iterator of indices

**Usage Example:**
```python
>>> list(iter_index('AABCADEAF', 'A'))
[0, 1, 4, 7]
```

**Cost:** O(n), where n is the length of the iterable

---

### iter_except

Convert a call-until-exception interface to an iterator interface.

**Args:**
- `function`: Function to call
- `exception`: Exception to catch
- `first`: Initial value

**Returns:**
- iterator: Iterator from function calls

**Usage Example:**
```python
>>> d = {'a': 1, 'b': 2}
>>> list(iter_except(d.popitem, KeyError))
[('b', 2), ('a', 1)]
```

**Cost:** O(n), where n is the number of successful calls

---

### multinomial

Number of distinct arrangements of a multiset.

**Args:**
- `*counts`: Counts of each item

**Returns:**
- int: Multinomial coefficient

**Usage Example:**
```python
>>> multinomial(5, 2, 2, 1, 1)
83160
```

**Cost:** O(n), where n is the number of counts

---

### powerset

Subsequences of the iterable from shortest to longest.

**Args:**
- `iterable`: The iterable

**Returns:**
- iterator: Iterator of tuples

**Usage Example:**
```python
>>> list(powerset([1,2,3]))
[(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]
```

**Cost:** O(2ⁿ), where n is the length of the iterable

---

### sum_of_squares

Add up the squares of the input values.

**Args:**
- `iterable`: The iterable of numbers

**Returns:**
- float or int: Sum of squares

**Usage Example:**
```python
>>> sum_of_squares([10, 20, 30])
1400
```

**Cost:** O(n), where n is the number of elements

---

### reshape

Reshape a 2-D matrix to have a given number of columns.

**Args:**
- `matrix`: 2D matrix
- `columns` (int): Number of columns

**Returns:**
- iterator: Reshaped matrix

**Usage Example:**
```python
>>> list(reshape([(0, 1), (2, 3), (4, 5)], 3))
[(0, 1, 2), (3, 4, 5)]
```

**Cost:** O(n), where n is the total number of elements

---

### transpose

Swap the rows and columns of a 2-D matrix.

**Args:**
- `matrix`: 2D matrix

**Returns:**
- iterator: Transposed matrix

**Usage Example:**
```python
>>> list(transpose([(1, 2, 3), (11, 22, 33)]))
[(1, 11), (2, 22), (3, 33)]
```

**Cost:** O(n * m), where n is rows and m is columns

---

### matmul

Multiply two matrices.

**Args:**
- `m1`: First matrix
- `m2`: Second matrix

**Returns:**
- iterator: Result matrix

**Usage Example:**
```python
>>> list(matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)]))
[(49, 80), (41, 60)]
```

**Cost:** O(n * m * p), where n×m and m×p are matrix dimensions

---

### convolve

Discrete linear convolution of two iterables. Equivalent to polynomial multiplication.

**Args:**
- `signal`: The signal iterable
- `kernel`: The kernel iterable

**Returns:**
- iterator: Convolution result

**Usage Example:**
```python
>>> list(convolve([1, -1, -20], [1, -3]))
[1, -4, -17, 60]
```

**Cost:** O(n * m), where n and m are the lengths of signal and kernel

---

### polynomial_from_roots

Compute a polynomial's coefficients from its roots.

**Args:**
- `roots`: List of roots

**Returns:**
- list: Coefficients

**Usage Example:**
```python
>>> polynomial_from_roots([5, -4, 3])
[1, -4, -17, 60]
```

**Cost:** O(n²), where n is the number of roots

---

### polynomial_eval

Evaluate a polynomial at a specific value.

**Args:**
- `coefficients`: List of coefficients
- `x`: Value to evaluate at

**Returns:**
- float or int: Result

**Usage Example:**
```python
>>> polynomial_eval([1, -4, -17, 60], x=5)
0
```

**Cost:** O(n), where n is the number of coefficients

---

### polynomial_derivative

Compute the first derivative of a polynomial.

**Args:**
- `coefficients`: List of coefficients

**Returns:**
- list: Derivative coefficients

**Usage Example:**
```python
>>> polynomial_derivative([1, -4, -17, 60])
[3, -8, -17]
```

**Cost:** O(n), where n is the number of coefficients

---

### sieve

Primes less than n.

**Args:**
- `n` (int): Upper limit

**Returns:**
- iterator: Iterator of primes

**Usage Example:**
```python
>>> list(sieve(30))
[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
```

**Cost:** O(n log log n) - Sieve of Eratosthenes complexity

---

### factor

Prime factors of n.

**Args:**
- `n` (int): Number to factor

**Returns:**
- iterator: Iterator of prime factors

**Usage Example:**
```python
>>> list(factor(99))
[3, 3, 11]
```

**Cost:** O(√n), where n is the number to factor

---

### is_prime

Return True if n is prime.

**Args:**
- `n` (int): Number to check

**Returns:**
- bool: True if prime

**Usage Example:**
```python
>>> is_prime(7)
True
>>> is_prime(10)
False
```

**Cost:** O(√n)

---

### totient

Count of natural numbers up to n that are coprime to n (Euler's totient function).

**Args:**
- `n` (int): Number

**Returns:**
- int: Totient value

**Usage Example:**
```python
>>> totient(12)
4
```

**Cost:** O(√n) due to factorization

---

## Logical Functions

### and_all

Returns True if all arguments are True; False otherwise.

**Args:**
- `*args` (bool): One or more boolean values to evaluate

**Returns:**
- bool: True if all arguments are True, False otherwise

**Raises:**
- ValueError: If no arguments are provided
- TypeError: If any argument is not a boolean

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import and_all
>>> and_all(True, True, True)
True
>>> and_all(True, False, True)
False
>>> and_all(5 > 3, 10 < 20, "a" == "a")
True
```

**Cost:** O(n) where n is the number of arguments

---

### or_any

Returns True if any argument is True; False if all are False.

**Args:**
- `*args` (bool): One or more boolean values to evaluate

**Returns:**
- bool: True if any argument is True, False otherwise

**Raises:**
- ValueError: If no arguments are provided
- TypeError: If any argument is not a boolean

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import or_any
>>> or_any(True, False, False)
True
>>> or_any(False, False, False)
False
>>> or_any(5 < 3, 10 > 20, "a" == "a")
True
```

**Cost:** O(n) where n is the number of arguments

---

### not_value

Reverses the logical value of its argument.

**Args:**
- `logical_value` (bool): The boolean value to negate

**Returns:**
- bool: The opposite boolean value

**Raises:**
- TypeError: If the argument is not a boolean

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import not_value
>>> not_value(True)
False
>>> not_value(False)
True
>>> not_value(5 > 10)
True
```

**Cost:** O(1)

---

### xor_all

Returns True if an odd number of arguments are True.

**Args:**
- `*args` (bool): One or more boolean values to evaluate

**Returns:**
- bool: True if an odd number of arguments are True, False otherwise

**Raises:**
- ValueError: If no arguments are provided
- TypeError: If any argument is not a boolean

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import xor_all
>>> xor_all(True, True)
False
>>> xor_all(True, False)
True
>>> xor_all(True, True, True)
True
```

**Cost:** O(n) where n is the number of arguments

---

### if_then_else

Returns one value if condition is True, another if False.

**Args:**
- `logical_test` (bool): The condition to test
- `value_if_true` (Any): The value to return if logical_test is True
- `value_if_false` (Any): The value to return if logical_test is False

**Returns:**
- Any: Either value_if_true or value_if_false based on the test

**Raises:**
- TypeError: If logical_test is not a boolean

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import if_then_else
>>> if_then_else(True, "Yes", "No")
'Yes'
>>> if_then_else(5 > 3, "Greater", "Smaller")
'Greater'
>>> if_then_else(False, 10, 20)
20
```

**Cost:** O(1)

---

### if_error

Returns value if not an error; otherwise returns alternative value.

**Args:**
- `value` (Any): The value or callable to check for errors
- `value_if_error` (Any): The value to return if an error occurs

**Returns:**
- Any: The result of value if no error, otherwise value_if_error

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import if_error
>>> if_error(10 / 2, "Error!")
5.0
>>> if_error(lambda: 10 / 0, "Error!")
'Error!'
>>> if_error(lambda: int("abc"), "Invalid")
'Invalid'
```

**Cost:** O(1)

---

### is_blank

Returns True if value is blank (None, empty string, or empty collection).

**Args:**
- `value` (Any): The value to check

**Returns:**
- bool: True if the value is considered blank, False otherwise

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import is_blank
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
```

**Cost:** O(1) for most cases; O(n) for checking empty collections

---

### is_error

Returns True if evaluating value produces an error.

**Args:**
- `value` (Any): The value or callable to check for errors

**Returns:**
- bool: True if an error occurs, False otherwise

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import is_error
>>> is_error(lambda: 10 / 2)
False
>>> is_error(lambda: 10 / 0)
True
>>> is_error(lambda: int("abc"))
True
```

**Cost:** O(1) plus the cost of executing the callable

---

### is_text

Returns True if value is a string.

**Args:**
- `value` (Any): The value to check

**Returns:**
- bool: True if the value is a string, False otherwise

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import is_text
>>> is_text("hello")
True
>>> is_text(123)
False
>>> is_text(True)
False
```

**Cost:** O(1)

---

### is_number

Returns True if value is a number (int or float, not bool).

**Args:**
- `value` (Any): The value to check

**Returns:**
- bool: True if the value is an int or float, False otherwise

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import is_number
>>> is_number(123)
True
>>> is_number(3.14)
True
>>> is_number("hello")
False
>>> is_number(True)
False
```

**Cost:** O(1)

---

### is_logical

Returns True if value is a boolean.

**Args:**
- `value` (Any): The value to check

**Returns:**
- bool: True if the value is a boolean, False otherwise

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import is_logical
>>> is_logical(True)
True
>>> is_logical(False)
True
>>> is_logical(0)
False
>>> is_logical("True")
False
```

**Cost:** O(1)

---

### switch_case

Evaluates expression against values and returns matching result.

**Args:**
- `expression` (Any): The value to compare
- `*args` (Any): Pairs of (value, result), optionally ending with default

**Returns:**
- Any: The result corresponding to the first match, or default value

**Raises:**
- ValueError: If insufficient arguments or no match without default

**Usage Example:**
```python
>>> from formulite.fxPython.py_logic import switch_case
>>> switch_case(3, 1, "One", 2, "Two", 3, "Three", "Other")
'Three'
>>> switch_case("apple", "orange", "Fruit", "apple", "Favorite", "Unknown")
'Favorite'
>>> switch_case(5, 1, "One", 2, "Two", "Not Found")
'Not Found'
```

**Cost:** O(n) where n is the number of value-result pairs

---

## Summary

The fxPython module provides a comprehensive set of utilities for Python programming:

- **27 conversion functions** for seamless type transformations
- **24 operation functions** for advanced collection manipulation (including 6 SQL-style aggregate functions)
- **12 logical functions** for conditional logic and type checking
- **8 tool functions** for high-level programming patterns
- **60+ itertools recipes** for efficient iterator processing

All functions are optimized with documented complexity analysis and follow Python best practices (PEP standards).
