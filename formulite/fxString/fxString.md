# fxString Functions Documentation

Complete reference for all string manipulation, conversion, validation, and formatting functions in the FormuLite fxString module.

## Overview

The fxString module provides comprehensive string manipulation functions for FormuLite, including:
- **Conversions**: Parse strings to numbers, dates, JSON
- **Operations**: Substring, replace, split, extract, concatenate
- **Format**: Capitalize, pad, normalize, format names/emails/URLs
- **Evaluations**: Validate formats, check content, parse emails
- **Similarity**: Calculate string similarity using various algorithms
- **Spanish**: NIF/NIE/CIF validation, Spanish text processing
- **Validations**: Check patterns and content
- **Spellcheck**: Text normalization

## Module Structure

- **string_convertions.py**: Functions for converting strings to other data types
- **string_operations.py**: Core string manipulation and extraction functions
- **string_format.py**: Text formatting and normalization functions
- **string_evaluations.py**: String validation and pattern matching functions
- **string_similarity.py**: String comparison and similarity algorithms
- **string_spanish.py**: Spanish-specific validation and processing functions
- **string_spellcheck.py**: Text normalization and spell-checking utilities
- **string_validations.py**: Character and pattern validation functions

---

## Table of Contents

- [Function Categories](#function-categories)
  - [String Conversions](#string-conversions)
  - [String Operations](#string-operations)
  - [String Format](#string-format)
  - [String Evaluations](#string-evaluations)
  - [String Similarity](#string-similarity)
  - [String Spanish](#string-spanish)
  - [String Validations](#string-validations)
  - [String Spellcheck](#string-spellcheck)
- [Function Index](#function-index)
- [Credits](#credits)

---

## Function Categories

### String Conversions
- [replace_void](#replace_void) - Replaces empty or None values with specified replacement
- [none_to_string](#none_to_string) - Converts None to empty string, preserves original otherwise
- [string_to_integer](#string_to_integer) - Converts string to integer or None if fails
- [string_to_float](#string_to_float) - Converts string to float or None if fails
- [string_to_number](#string_to_number) - Converts string to integer or float based on type
- [string_to_date](#string_to_date) - Converts string to date or datetime object
- [string_to_datetime](#string_to_datetime) - Converts string to datetime.datetime object
- [split_all](#split_all) - Splits string by common delimiters, removes empty strings
- [split_by_substrings](#split_by_substrings) - Splits string by substring list, preserves separators
- [split_limited](#split_limited) - Splits string by whitespace with word limit
- [extract_and_decode_json](#extract_and_decode_json) - Extracts and decodes JSON from fenced block

### String Operations
- [ascii_from_char](#ascii_from_char) - Returns Unicode/ASCII code of first character
- [char_from_ascii](#char_from_ascii) - Returns character from Unicode/ASCII code value
- [count_words](#count_words) - Counts number of words in string
- [count_characters](#count_characters) - Counts occurrences of specific character in string
- [position_in_string](#position_in_string) - Finds all positions where substring appears (1-indexed)
- [random_string](#random_string) - Generates random string of specified length
- [reverse_string](#reverse_string) - Reverses characters in string
- [replace_string](#replace_string) - Replaces all occurrences of substring with another
- [replace_first_occurrence](#replace_first_occurrence) - Replaces only first occurrence of substring
- [replace_last_occurrence](#replace_last_occurrence) - Replaces only last occurrence of substring
- [truncate_string](#truncate_string) - Truncates string to maximum length with ellipsis
- [substring](#substring) - Extracts substring from given position and length
- [left_substring](#left_substring) - Returns leftmost n characters of string
- [right_substring](#right_substring) - Returns rightmost n characters of string
- [common_substring](#common_substring) - Finds longest common substring between two strings
- [substring_on_left](#substring_on_left) - Extracts substring left of first pattern occurrence
- [substring_on_right](#substring_on_right) - Extracts substring right of first pattern occurrence
- [substring_between_pattern](#substring_between_pattern) - Extracts substring between two pattern occurrences
- [substring_from_delimiters](#substring_from_delimiters) - Extracts content between specified delimiters
- [extract_first_number](#extract_first_number) - Extracts first number (integer/float) from string
- [extract_last_number](#extract_last_number) - Extracts last number (integer/float) from string
- [extract_numbers](#extract_numbers) - Extracts all numbers (integers/floats) from string
- [join_to_string](#join_to_string) - Joins iterable of strings with separator
- [erase_specialchar](#erase_specialchar) - Removes special characters, optionally allows spaces/underscores
- [erase_digits](#erase_digits) - Removes all digits from string
- [erase_lrspaces](#erase_lrspaces) - Removes leading and trailing spaces from string
- [erase_allspaces](#erase_allspaces) - Removes all spaces from string
- [distinct_words](#distinct_words) - Returns list of unique words from string
- [move_word](#move_word) - Moves word from one position to another
- [concatenate_strings](#concatenate_strings) - Concatenates two strings together
- [add_quotes](#add_quotes) - Adds quotes around string (single or double)

### String Format
- [sql_quote](#sql_quote) - Escapes single quotes for safe SQL queries
- [format_date](#format_date) - Formats date/datetime into specified string format
- [format_number](#format_number) - Formats number with decimal places and separators
- [capitalize_string](#capitalize_string) - Capitalizes string by mode (all/first/each word)
- [pad_string](#pad_string) - Pads string to length with character
- [to_upper](#to_upper) - Converts string to uppercase
- [to_lower](#to_lower) - Converts string to lowercase
- [normalize_spaces](#normalize_spaces) - Replaces multiple spaces with single, trims ends
- [normalize_symbols](#normalize_symbols) - Normalizes symbol spacing per typographical rules
- [flat_vowels](#flat_vowels) - Removes diacritical marks (accents) from vowels
- [ascii_string](#ascii_string) - Converts to ASCII, removing non-ASCII characters
- [format_email_address](#format_email_address) - Formats and normalizes email address (lowercase, trimmed)
- [format_url](#format_url) - Formats and normalizes URL
- [format_name](#format_name) - Formats person's name by specified rules
- [format_fullname](#format_fullname) - Formats full name, removes titles and normalizes
- [format_company_name](#format_company_name) - Formats company name, handles legal forms

### String Evaluations
- [contains_digit](#contains_digit) - Checks if string contains at least one digit
- [is_alphabetic](#is_alphabetic) - Checks if string contains only alphabetic characters
- [is_numeric](#is_numeric) - Checks if string represents valid number
- [is_internet_domain_format](#is_internet_domain_format) - Validates if string matches internet domain format
- [is_email_format](#is_email_format) - Validates if string matches email address format
- [is_url_format](#is_url_format) - Validates if string matches URL format
- [has_date_format](#has_date_format) - Checks if string can be interpreted as date
- [has_numbers](#has_numbers) - Checks if string contains any numeric digits
- [has_substring](#has_substring) - Checks if string contains specific substring
- [starts_with_substring](#starts_with_substring) - Checks if string starts with specific prefix
- [ends_with_substring](#ends_with_substring) - Checks if string ends with specific suffix
- [parse_email](#parse_email) - Parses email address into username and domain components
- [username_from_email](#username_from_email) - Extracts username portion from email address
- [domain_from_email](#domain_from_email) - Extracts domain portion from email address

### String Similarity
- [calculate_similarity](#calculate_similarity) - Calculates similarity using specified algorithm
- [has_same_words](#has_same_words) - Checks if strings contain same words (order-independent)
- [find_common_words](#find_common_words) - Finds words appearing in both strings
- [has_same_characters](#has_same_characters) - Checks if strings contain same characters (anagram)
- [string_hamming_score](#string_hamming_score) - Calculates Hamming distance between two strings
- [string_levenshtein_score](#string_levenshtein_score) - Calculates Levenshtein distance between two strings
- [string_jarowinkler_score](#string_jarowinkler_score) - Calculates Jaro-Winkler similarity between two strings
- [string_jaccard_score](#string_jaccard_score) - Calculates Jaccard similarity coefficient between strings
- [string_similarity_score](#string_similarity_score) - Calculates multiple similarity scores using all algorithms

### String Spanish
- [remove_spanish_stop_words](#remove_spanish_stop_words) - Removes common Spanish stop words from string
- [reduce_spanish_letters](#reduce_spanish_letters) - Reduces Spanish text to phonetic representation
- [nif_padding](#nif_padding) - Pads Spanish NIF/CIF to standard format
- [nif_parse](#nif_parse) - Parses and normalizes Spanish NIF/NIE/CIF
- [nif_letter](#nif_letter) - Calculates control letter for Spanish DNI
- [is_valid_dni](#is_valid_dni) - Validates Spanish DNI (Documento Nacional de Identidad)
- [is_valid_nie](#is_valid_nie) - Validates Spanish NIE (Número de Identidad de Extranjero)
- [is_valid_cif](#is_valid_cif) - Validates Spanish CIF (Certificado de Identificación Fiscal)
- [validate_spanish_nif](#validate_spanish_nif) - Validates Spanish NIF (DNI/NIE/CIF) by type
- [fix_spanish](#fix_spanish) - Fixes common Spanish character encoding issues

### String Validations
- [contains_digit](#contains_digit) - Checks if string contains at least one digit
- [same_letters](#same_letters) - Checks if strings contain exact same characters (anagram)

### String Spellcheck
- [normalize_text](#normalize_text) - Normalizes text by lowercasing and removing accents

---

## Function Index

**A**
- [add_quotes](#add_quotes) - Adds quotes around string (single or double)
- [ascii_from_char](#ascii_from_char) - Returns Unicode/ASCII code of first character
- [ascii_string](#ascii_string) - Converts to ASCII, removing non-ASCII characters

**C**
- [calculate_similarity](#calculate_similarity) - Calculates similarity using specified algorithm
- [capitalize_string](#capitalize_string) - Capitalizes string by mode (all/first/each word)
- [char_from_ascii](#char_from_ascii) - Returns character from Unicode/ASCII code value
- [common_substring](#common_substring) - Finds longest common substring between two strings
- [concatenate_strings](#concatenate_strings) - Concatenates two strings together
- [contains_digit](#contains_digit) - Checks if string contains at least one digit
- [count_characters](#count_characters) - Counts occurrences of specific character in string
- [count_words](#count_words) - Counts number of words in string

**D**
- [distinct_words](#distinct_words) - Returns list of unique words from string
- [domain_from_email](#domain_from_email) - Extracts domain portion from email address

**E**
- [ends_with_substring](#ends_with_substring) - Checks if string ends with specific suffix
- [erase_allspaces](#erase_allspaces) - Removes all spaces from string
- [erase_digits](#erase_digits) - Removes all digits from string
- [erase_lrspaces](#erase_lrspaces) - Removes leading and trailing spaces from string
- [erase_specialchar](#erase_specialchar) - Removes special characters, optionally allows spaces/underscores
- [extract_and_decode_json](#extract_and_decode_json) - Extracts and decodes JSON from fenced block
- [extract_first_number](#extract_first_number) - Extracts first number (integer/float) from string
- [extract_last_number](#extract_last_number) - Extracts last number (integer/float) from string
- [extract_numbers](#extract_numbers) - Extracts all numbers (integers/floats) from string

**F**
- [find_common_words](#find_common_words) - Finds words appearing in both strings
- [fix_spanish](#fix_spanish) - Fixes common Spanish character encoding issues
- [flat_vowels](#flat_vowels) - Removes diacritical marks (accents) from vowels
- [format_company_name](#format_company_name) - Formats company name, handles legal forms
- [format_date](#format_date) - Formats date/datetime into specified string format
- [format_email_address](#format_email_address) - Formats and normalizes email address (lowercase, trimmed)
- [format_fullname](#format_fullname) - Formats full name, removes titles and normalizes
- [format_name](#format_name) - Formats person's name by specified rules
- [format_number](#format_number) - Formats number with decimal places and separators
- [format_url](#format_url) - Formats and normalizes URL

**H**
- [has_date_format](#has_date_format) - Checks if string can be interpreted as date
- [has_numbers](#has_numbers) - Checks if string contains any numeric digits
- [has_same_characters](#has_same_characters) - Checks if strings contain same characters (anagram)
- [has_same_words](#has_same_words) - Checks if strings contain same words (order-independent)
- [has_substring](#has_substring) - Checks if string contains specific substring

**I**
- [is_alphabetic](#is_alphabetic) - Checks if string contains only alphabetic characters
- [is_email_format](#is_email_format) - Validates if string matches email address format
- [is_internet_domain_format](#is_internet_domain_format) - Validates if string matches internet domain format
- [is_numeric](#is_numeric) - Checks if string represents valid number
- [is_url_format](#is_url_format) - Validates if string matches URL format
- [is_valid_cif](#is_valid_cif) - Validates Spanish CIF (Certificado de Identificación Fiscal)
- [is_valid_dni](#is_valid_dni) - Validates Spanish DNI (Documento Nacional de Identidad)
- [is_valid_nie](#is_valid_nie) - Validates Spanish NIE (Número de Identidad de Extranjero)

**J**
- [join_to_string](#join_to_string) - Joins iterable of strings with separator

**L**
- [left_substring](#left_substring) - Returns leftmost n characters of string

**M**
- [move_word](#move_word) - Moves word from one position to another

**N**
- [nif_letter](#nif_letter) - Calculates control letter for Spanish DNI
- [nif_padding](#nif_padding) - Pads Spanish NIF/CIF to standard format
- [nif_parse](#nif_parse) - Parses and normalizes Spanish NIF/NIE/CIF
- [none_to_string](#none_to_string) - Converts None to empty string, preserves original otherwise
- [normalize_spaces](#normalize_spaces) - Replaces multiple spaces with single, trims ends
- [normalize_symbols](#normalize_symbols) - Normalizes symbol spacing per typographical rules
- [normalize_text](#normalize_text) - Normalizes text by lowercasing and removing accents

**P**
- [pad_string](#pad_string) - Pads string to length with character
- [parse_email](#parse_email) - Parses email address into username and domain components
- [position_in_string](#position_in_string) - Finds all positions where substring appears (1-indexed)

**R**
- [random_string](#random_string) - Generates random string of specified length
- [reduce_spanish_letters](#reduce_spanish_letters) - Reduces Spanish text to phonetic representation
- [remove_spanish_stop_words](#remove_spanish_stop_words) - Removes common Spanish stop words from string
- [replace_first_occurrence](#replace_first_occurrence) - Replaces only first occurrence of substring
- [replace_last_occurrence](#replace_last_occurrence) - Replaces only last occurrence of substring
- [replace_string](#replace_string) - Replaces all occurrences of substring with another
- [replace_void](#replace_void) - Replaces empty or None values with specified replacement
- [reverse_string](#reverse_string) - Reverses characters in string
- [right_substring](#right_substring) - Returns rightmost n characters of string

**S**
- [same_letters](#same_letters) - Checks if strings contain exact same characters (anagram)
- [split_all](#split_all) - Splits string by common delimiters, removes empty strings
- [split_by_substrings](#split_by_substrings) - Splits string by substring list, preserves separators
- [split_limited](#split_limited) - Splits string by whitespace with word limit
- [sql_quote](#sql_quote) - Escapes single quotes for safe SQL queries
- [starts_with_substring](#starts_with_substring) - Checks if string starts with specific prefix
- [string_hamming_score](#string_hamming_score) - Calculates Hamming distance between two strings
- [string_jaccard_score](#string_jaccard_score) - Calculates Jaccard similarity coefficient between strings
- [string_jarowinkler_score](#string_jarowinkler_score) - Calculates Jaro-Winkler similarity between two strings
- [string_levenshtein_score](#string_levenshtein_score) - Calculates Levenshtein distance between two strings
- [string_similarity_score](#string_similarity_score) - Calculates multiple similarity scores using all algorithms
- [string_to_date](#string_to_date) - Converts string to date or datetime object
- [string_to_datetime](#string_to_datetime) - Converts string to datetime.datetime object
- [string_to_float](#string_to_float) - Converts string to float or None if fails
- [string_to_integer](#string_to_integer) - Converts string to integer or None if fails
- [string_to_number](#string_to_number) - Converts string to integer or float based on type
- [substring](#substring) - Extracts substring from given position and length
- [substring_between_pattern](#substring_between_pattern) - Extracts substring between two pattern occurrences
- [substring_from_delimiters](#substring_from_delimiters) - Extracts content between specified delimiters
- [substring_on_left](#substring_on_left) - Extracts substring left of first pattern occurrence
- [substring_on_right](#substring_on_right) - Extracts substring right of first pattern occurrence

**T**
- [to_lower](#to_lower) - Converts string to lowercase
- [to_upper](#to_upper) - Converts string to uppercase
- [truncate_string](#truncate_string) - Truncates string to maximum length with ellipsis

**U**
- [username_from_email](#username_from_email) - Extracts username portion from email address

**V**
- [validate_spanish_nif](#validate_spanish_nif) - Validates Spanish NIF (DNI/NIE/CIF) by type

---

## String Conversions

Functions for converting strings to other data types and splitting/parsing operations.

### replace_void

Replaces empty or None values with a specified replacement value.

**Args:**
- `primary_value` (Any): The primary value to check
- `replacement_value` (Any): The value to use if primary_value is empty/None. Defaults to 'NaN'

**Returns:**
- Any: replacement_value if primary_value is empty/None/zero-length, otherwise returns primary_value

**Usage Example:**
```python
>>> replace_void("", "default")
'default'
>>> replace_void(None, 0)
0
>>> replace_void([], [1, 2, 3])
[1, 2, 3]
>>> replace_void("hello", "default")
'hello'
```

**Cost:** O(1) for most types

---

### none_to_string

Converts a None value to an empty string; otherwise, returns the original value.

**Args:**
- `value` (str | None): The input value, which could be a string or None

**Returns:**
- str: An empty string if the input 'value' was None, otherwise the original value

**Usage Example:**
```python
>>> none_to_string("hello")
'hello'
>>> none_to_string(None)
''
```

**Cost:** O(1) - constant time operation

---

### string_to_integer

Converts a string to an integer, returning None if conversion fails.

**Args:**
- `input_string` (str): The string to be converted to an integer

**Returns:**
- int | None: The integer representation of the cleaned string, or None if the conversion is not possible

**Usage Example:**
```python
>>> string_to_integer("123")
123
>>> string_to_integer("-45")
-45
>>> string_to_integer("abc123def")
123
>>> string_to_integer("abc")
None
```

**Cost:** O(n), where n is the length of the input string, due to regex processing

---

### string_to_float

Converts a string to a float, returning None if conversion fails.

**Args:**
- `input_string` (str): The string to be converted to a float

**Returns:**
- float | None: The float representation of the cleaned string, or None if the conversion is not possible

**Usage Example:**
```python
>>> string_to_float("123.45")
123.45
>>> string_to_float("123,45")
123.45
>>> string_to_float("abc123.45def")
123.45
```

**Cost:** O(n), where n is the length of the input string, due to regex processing

---

### string_to_number

Converts a string to an integer or float based on the specified target type.

**Args:**
- `input_string` (str): The string to convert
- `target_type` (str): The desired numeric type ('integer' or 'float'). Defaults to 'string'

**Returns:**
- int | float | None: The converted number, or None if conversion fails or target_type is invalid

**Usage Example:**
```python
>>> string_to_number("123", "integer")
123
>>> string_to_number("123.45", "float")
123.45
>>> string_to_number("abc123def", "integer")
123
```

**Cost:** O(n), where n is the length of input_string (delegates to string_to_integer or string_to_float)

---

### string_to_date

Converts a string to a date or datetime object based on common formats.

**Args:**
- `input_value` (str | date | dt): The string or existing date/datetime object to be converted or returned

**Returns:**
- date | dt | None: A datetime.date object if the string represents only a date, a datetime.datetime object if the string includes time information, or None if the string cannot be parsed

**Usage Example:**
```python
>>> string_to_date("2023-10-26")
datetime.date(2023, 10, 26)
>>> string_to_date("2023-10-26 14:30:00")
datetime.datetime(2023, 10, 26, 14, 30)
```

**Cost:** O(k * m), where k is the number of formats and m is the length of input_value

---

### string_to_datetime

Converts a string to a datetime.datetime object using common date and datetime formats.

**Args:**
- `input_value` (str | date | dt): The value to convert. Can be a string, date, or datetime

**Returns:**
- dt | None: A datetime.datetime object if conversion is successful, otherwise None

**Usage Example:**
```python
>>> string_to_datetime("2023-10-26 14:30:00")
datetime.datetime(2023, 10, 26, 14, 30)
>>> string_to_datetime("2023-10-26")
datetime.datetime(2023, 10, 26, 0, 0)
```

**Cost:** O(k * m), where k is the number of formats and m is the length of the input string

---

### split_all

Splits a string by an expanded set of common delimiters and removes any empty strings from the result.

**Args:**
- `input_string` (str): The string to be split
- `delimiter_pattern` (str): The regular expression pattern to use as a delimiter. Defaults to `'[.\-_\s,/():;\'"\\]+'`

**Returns:**
- list: A list of non-empty strings resulting from the split operation

**Raises:**
- TypeError: If 'input_string' is not a string

**Usage Example:**
```python
>>> split_all("hello-world_123/test")
['hello', 'world', '123', 'test']
```

**Cost:** O(n), where n is the length of the input string

---

### split_by_substrings

Splits a string by a list of substrings (separators), preserving the separators.

**Args:**
- `input_string` (str): The string to be split
- `separators` (list[str]): A list of strings to use as separators

**Returns:**
- list[str]: A list of strings, where each string represents a segment of the original string

**Raises:**
- TypeError: If 'input_string' is not a string or 'separators' is not a list
- ValueError: If 'separators' is an empty list or contains non-string elements

**Usage Example:**
```python
>>> split_by_substrings("Name: John Doe; Age: 30, City: New York", [":", ";", ","])
['Name:', ' John Doe;', ' Age:', ' 30,', ' City:', ' New York']
```

**Cost:** O(n + m * k), where n is the string length, m is the number of separators, and k is the number of segments

---

### split_limited

Splits a string by whitespace into a list of words, with an optional limit on the number of initial words.

**Args:**
- `input_string` (str): The string to be split
- `limit` (int): The maximum number of initial words to return individually. Must be non-negative

**Returns:**
- list[str]: A list of strings, where the last element might contain multiple words if the original string exceeded the limit

**Raises:**
- TypeError: If 'input_string' is not a string or 'limit' is not an integer
- ValueError: If 'limit' is a negative integer

**Usage Example:**
```python
>>> split_limited("This is a test of the split function", 3)
['This', 'is', 'a', 'test of the split function']
```

**Cost:** O(n), where n is the length of the input string

---

### extract_and_decode_json

Extracts and decodes a JSON string embedded within a block delimited by ```json\n and \n```.

**Args:**
- `text_content` (str): The input string potentially containing a fenced JSON block

**Returns:**
- Optional[dict]: A dictionary representing the decoded JSON if found and successfully parsed; otherwise, returns None

**Usage Example:**
```python
>>> example_string = "Some text.\\n```json\\n{\\"key\\": \\"value\\"}\\n```\\nMore text."
>>> extract_and_decode_json(example_string)
{'key': 'value'}
```

**Cost:** O(n), where n is the length of the text content, due to regex search

---

## String Operations

Functions for manipulating, extracting, and transforming strings.

### ascii_from_char

Devuelve el valor entero (código Unicode/ASCII) del primer carácter de una cadena.

**Args:**
- `character` (str): La cadena de la que se obtendrá el valor entero del primer carácter

**Returns:**
- int: El valor entero correspondiente al carácter

**Raises:**
- TypeError: Si la entrada no es una cadena
- ValueError: Si la cadena de entrada está vacía

**Usage Example:**
```python
>>> ascii_from_char("A")
65
>>> ascii_from_char("€")
8364
```

**Cost:** O(1)

---

### char_from_ascii

Devuelve el carácter correspondiente a un valor entero (código Unicode/ASCII).

**Args:**
- `integer_code` (int): El valor entero (código Unicode/ASCII) del carácter deseado. Debe ser un valor Unicode válido (0 a 1,114,111)

**Returns:**
- str: El carácter correspondiente al valor entero

**Raises:**
- TypeError: Si la entrada no es un entero
- ValueError: Si el entero está fuera del rango de los códigos Unicode válidos

**Usage Example:**
```python
>>> char_from_ascii(65)
'A'
>>> char_from_ascii(8364)
'€'
```

**Cost:** O(1)

---

### count_words

Counts the number of words in a string.

**Args:**
- `input_string` (str): The string to be analyzed

**Returns:**
- int: The number of words in the string

**Usage Example:**
```python
>>> count_words("Hello world from Python")
4
>>> count_words("   Multiple   spaces   ")
2
```

**Cost:** O(n), where n is the length of the input string

---

### count_characters

Counts the occurrences of a specific character in a string.

**Args:**
- `input_string` (str): The string to search
- `target_char` (str): The character to count

**Returns:**
- int: The number of times target_char appears in input_string

**Usage Example:**
```python
>>> count_characters("hello world", "l")
3
>>> count_characters("Python", "z")
0
```

**Cost:** O(n), where n is the length of the input string

---

### position_in_string

Finds all positions where a substring appears in a string (1-indexed).

**Args:**
- `main_string` (str): The string to search in
- `substring` (str): The substring to find
- `start_position` (int): The position to start searching from (1-indexed). Defaults to 1

**Returns:**
- list[int]: A list of all positions (1-indexed) where the substring is found

**Usage Example:**
```python
>>> position_in_string("hello world hello", "hello")
[1, 13]
>>> position_in_string("test", "xyz")
[]
```

**Cost:** O(n * m), where n is the length of main_string and m is the length of substring

---

### random_string

Generates a random string of a specified length.

**Args:**
- `length` (int): The desired length of the random string. Defaults to 10
- `secure` (bool): If True, uses cryptographically secure random generation. Defaults to True

**Returns:**
- str: A random string consisting of ASCII letters and digits

**Usage Example:**
```python
>>> len(random_string(15))
15
>>> random_string(5, secure=False)
'aB3x9'  # Example output
```

**Cost:** O(n), where n is the desired length

---

### reverse_string

Reverses the characters in a string.

**Args:**
- `input_string` (str): The string to be reversed

**Returns:**
- str: The reversed string

**Usage Example:**
```python
>>> reverse_string("hello")
'olleh'
>>> reverse_string("Python")
'nohtyP'
```

**Cost:** O(n), where n is the length of the input string

---

### replace_string

Replaces all occurrences of a substring with another substring.

**Args:**
- `original_string` (str): The original string
- `old_substring` (str): The substring to be replaced
- `new_substring` (str): The replacement substring

**Returns:**
- str: The modified string with all occurrences replaced

**Usage Example:**
```python
>>> replace_string("hello world", "world", "Python")
'hello Python'
```

**Cost:** O(n), where n is the length of the original string

---

### replace_first_occurrence

Replaces only the first occurrence of a substring.

**Args:**
- `original_string` (str): The original string
- `old_substring` (str): The substring to be replaced
- `new_substring` (str): The replacement substring

**Returns:**
- str: The modified string with the first occurrence replaced

**Usage Example:**
```python
>>> replace_first_occurrence("test test test", "test", "exam")
'exam test test'
```

**Cost:** O(n), where n is the length of the original string

---

### replace_last_occurrence

Replaces only the last occurrence of a substring.

**Args:**
- `original_string` (str): The original string
- `old_substring` (str): The substring to be replaced
- `new_substring` (str): The replacement substring

**Returns:**
- str: The modified string with the last occurrence replaced

**Usage Example:**
```python
>>> replace_last_occurrence("test test test", "test", "exam")
'test test exam'
```

**Cost:** O(n), where n is the length of the original string

---

### truncate_string

Truncates a string to a maximum length, optionally adding an ellipsis.

**Args:**
- `input_string` (str): The string to truncate
- `max_length` (int): The maximum allowed length
- `add_ellipsis` (bool): Whether to add '...' at the end. Defaults to True

**Returns:**
- str: The truncated string

**Usage Example:**
```python
>>> truncate_string("This is a long string", 10)
'This is...'
>>> truncate_string("Short", 10)
'Short'
```

**Cost:** O(n), where n is max_length

---

### substring

Extracts a substring from a string starting at a given position.

**Args:**
- `original_string` (str): The original string
- `start_position` (int): The starting position (1-indexed)
- `length` (int): The number of characters to extract

**Returns:**
- str: The extracted substring

**Usage Example:**
```python
>>> substring("hello world", 1, 5)
'hello'
>>> substring("Python", 3, 2)
'th'
```

**Cost:** O(length)

---

### left_substring

Returns the leftmost n characters of a string.

**Args:**
- `original_string` (str): The original string
- `num_chars` (int): The number of characters to return from the left

**Returns:**
- str: The leftmost num_chars characters

**Usage Example:**
```python
>>> left_substring("hello world", 5)
'hello'
```

**Cost:** O(num_chars)

---

### right_substring

Returns the rightmost n characters of a string.

**Args:**
- `original_string` (str): The original string
- `num_chars` (int): The number of characters to return from the right

**Returns:**
- str: The rightmost num_chars characters

**Usage Example:**
```python
>>> right_substring("hello world", 5)
'world'
```

**Cost:** O(num_chars)

---

### common_substring

Finds the longest common substring between two strings.

**Args:**
- `string1` (str): The first string
- `string2` (str): The second string
- `min_longest_substring` (int): The minimum length of the substring to find. Defaults to 4

**Returns:**
- str: The longest common substring, or empty string if none found

**Usage Example:**
```python
>>> common_substring("hello world", "world peace")
'world'
```

**Cost:** O(n * m), where n and m are the lengths of the two strings

---

### substring_on_left

Extracts the substring to the left of the first occurrence of a pattern.

**Args:**
- `text` (Optional[str]): The text to search
- `pattern` (str): The pattern to search for

**Returns:**
- Optional[str]: The substring before the pattern, or None if pattern not found

**Usage Example:**
```python
>>> substring_on_left("hello@world.com", "@")
'hello'
```

**Cost:** O(n), where n is the length of the text

---

### substring_on_right

Extracts the substring to the right of the first occurrence of a pattern.

**Args:**
- `text` (Optional[str]): The text to search
- `pattern` (str): The pattern to search for

**Returns:**
- Optional[str]: The substring after the pattern, or None if pattern not found

**Usage Example:**
```python
>>> substring_on_right("hello@world.com", "@")
'world.com'
```

**Cost:** O(n), where n is the length of the text

---

### substring_between_pattern

Extracts substring between two occurrences of the same pattern.

**Args:**
- `input_string` (str): The string to search
- `pattern` (str): The pattern to use as delimiter

**Returns:**
- str | None: The substring between two occurrences of the pattern

**Usage Example:**
```python
>>> substring_between_pattern("Name: John Doe: Age", ": ")
'John Doe'
```

**Cost:** O(n), where n is the length of the input string

---

### substring_from_delimiters

Extracts content from between specified delimiters.

**Args:**
- `input_string` (str): The string to search
- `left_delimiter` (str): The opening delimiter
- `right_delimiter` (str): The closing delimiter
- `include_delimiters` (bool): Whether to include delimiters in result. Defaults to False

**Returns:**
- str | None: The extracted content, or None if delimiters not found

**Usage Example:**
```python
>>> substring_from_delimiters("Hello (world)", "(", ")")
'world'
```

**Cost:** O(n), where n is the length of the input string

---

### extract_first_number

Extracts the first number (integer or float) from a string.

**Args:**
- `input_string` (str | None): The string to extract from

**Returns:**
- int | float | None: The first number found, or None if no number found

**Usage Example:**
```python
>>> extract_first_number("Price is 19.99 dollars")
19.99
>>> extract_first_number("Age: 25")
25
```

**Cost:** O(n), where n is the length of the input string

---

### extract_last_number

Extracts the last number (integer or float) from a string.

**Args:**
- `input_string` (str | None): The string to extract from

**Returns:**
- int | float | None: The last number found, or None if no number found

**Usage Example:**
```python
>>> extract_last_number("Prices: 10.50 and 25.75")
25.75
```

**Cost:** O(n), where n is the length of the input string

---

### extract_numbers

Extracts all numbers (integers and floats) from a string.

**Args:**
- `input_string` (str | None): The string to extract from

**Returns:**
- list[int | float]: A list of all numbers found in the string

**Usage Example:**
```python
>>> extract_numbers("Total: 100 items at 5.99 each")
[100, 5.99]
```

**Cost:** O(n), where n is the length of the input string

---

### join_to_string

Joins an iterable of strings into a single string with a separator.

**Args:**
- `iterable` (Iterable[str]): The iterable of strings to join
- `separator` (str): The separator to use between elements. Defaults to " "

**Returns:**
- str: The joined string

**Usage Example:**
```python
>>> join_to_string(["hello", "world"], " ")
'hello world'
>>> join_to_string(["a", "b", "c"], "-")
'a-b-c'
```

**Cost:** O(n), where n is the total length of all strings

---

### erase_specialchar

Removes special characters from a string, optionally allowing spaces and underscores.

**Args:**
- `text` (str): The text to process
- `allow_spaces` (bool): Whether to preserve spaces. Defaults to True
- `allow_underscores` (bool): Whether to preserve underscores. Defaults to False
- `additional_allowed_chars` (str): Additional characters to preserve. Defaults to ''

**Returns:**
- str: The text with special characters removed

**Usage Example:**
```python
>>> erase_specialchar("Hello@World!", allow_spaces=True)
'Hello World'
```

**Cost:** O(n), where n is the length of the text

---

### erase_digits

Removes all digits from a string.

**Args:**
- `text` (Optional[str]): The text to process

**Returns:**
- Optional[str]: The text with all digits removed, or None if input is None

**Usage Example:**
```python
>>> erase_digits("abc123def456")
'abcdef'
```

**Cost:** O(n), where n is the length of the text

---

### erase_lrspaces

Removes leading and trailing spaces from a string.

**Args:**
- `text` (Optional[str]): The text to process

**Returns:**
- Optional[str]: The text with leading and trailing spaces removed

**Usage Example:**
```python
>>> erase_lrspaces("  hello world  ")
'hello world'
```

**Cost:** O(n), where n is the length of the text

---

### erase_allspaces

Removes all spaces from a string.

**Args:**
- `text` (Optional[str]): The text to process

**Returns:**
- Optional[str]: The text with all spaces removed

**Usage Example:**
```python
>>> erase_allspaces("hello world from python")
'helloworldfrompython'
```

**Cost:** O(n), where n is the length of the text

---

### distinct_words

Returns a list of unique words from a string.

**Args:**
- `input_string` (str): The string to process
- `case_sensitive` (bool): Whether to distinguish between uppercase and lowercase. Defaults to False

**Returns:**
- list[str]: A list of unique words

**Usage Example:**
```python
>>> distinct_words("hello world hello python")
['hello', 'world', 'python']
```

**Cost:** O(n), where n is the length of the input string

---

### move_word

Moves a word from one position to another in a string.

**Args:**
- `input_string` (str): The string containing words
- `from_index` (int): The index of the word to move (0-based)
- `to_index` (int): The target index for the word (0-based)

**Returns:**
- str: The string with the word moved

**Usage Example:**
```python
>>> move_word("first second third", 0, 2)
'second third first'
```

**Cost:** O(n), where n is the length of the input string

---

### concatenate_strings

Concatenates two strings.

**Args:**
- `string1` (str): The first string
- `string2` (str): The second string

**Returns:**
- str: The concatenated string

**Usage Example:**
```python
>>> concatenate_strings("hello", "world")
'helloworld'
```

**Cost:** O(n + m), where n and m are the lengths of the strings

---

### add_quotes

Adds quotes around a string.

**Args:**
- `text` (Optional[str]): The text to quote
- `quote_type` (str): The type of quote to use ("'" or '"'). Defaults to "'"

**Returns:**
- Optional[str]: The quoted string, or None if input is None

**Usage Example:**
```python
>>> add_quotes("hello world")
"'hello world'"
>>> add_quotes("test", '"')
'"test"'
```

**Cost:** O(1)

---

## String Format

Functions for formatting, normalizing, and standardizing strings.

### sql_quote

Escapes single quotes in a SQL string for safe database queries.

**Args:**
- `sql_string` (str): The SQL string to escape
- `db_type` (str): The database type (e.g., 'mysql', 'postgres')

**Returns:**
- str: The escaped SQL string

**Usage Example:**
```python
>>> sql_quote("O'Brien", "mysql")
"O''Brien"
```

**Cost:** O(n), where n is the length of sql_string

---

### format_date

Formats a date or datetime object into a specified string format.

**Args:**
- `date_input` (Union[str, datetime]): The date to format
- `output_format` (str): The desired output format. Defaults to None
- `input_format` (str): The input format if date_input is a string. Defaults to None

**Returns:**
- str: The formatted date string

**Usage Example:**
```python
>>> from datetime import datetime
>>> format_date(datetime(2023, 10, 26), "%Y-%m-%d")
'2023-10-26'
```

**Cost:** O(1)

---

### format_number

Formats a number with specified decimal places and thousand separators.

**Args:**
- `number_input` (Union[int, float, str]): The number to format
- `decimal_places` (int): Number of decimal places. Defaults to 2
- `use_separator` (bool): Whether to use thousand separators. Defaults to True
- `locale` (str): The locale to use for formatting. Defaults to 'en_US'

**Returns:**
- str: The formatted number string

**Usage Example:**
```python
>>> format_number(1234567.89, decimal_places=2)
'1,234,567.89'
```

**Cost:** O(log n), where n is the value of the number

---

### capitalize_string

Capitalizes a string according to specified mode.

**Args:**
- `input_string` (str): The string to capitalize
- `mode` (str): The capitalization mode ('all', 'first', 'each'). Defaults to 'all'

**Returns:**
- str: The capitalized string

**Usage Example:**
```python
>>> capitalize_string("hello world", mode='all')
'HELLO WORLD'
>>> capitalize_string("hello world", mode='each')
'Hello World'
>>> capitalize_string("hello world", mode='first')
'Hello world'
```

**Cost:** O(n), where n is the length of input_string

---

### pad_string

Pads a string to a specified length with a character.

**Args:**
- `text` (str): The text to pad
- `length` (int): The desired total length
- `char` (str): The character to use for padding. Defaults to ' '
- `direction` (str): The padding direction ('left', 'right', 'both'). Defaults to 'right'

**Returns:**
- str: The padded string

**Usage Example:**
```python
>>> pad_string("hello", 10, direction='right')
'hello     '
>>> pad_string("42", 5, '0', direction='left')
'00042'
```

**Cost:** O(n), where n is the desired length

---

### to_upper

Converts a string to uppercase.

**Args:**
- `text` (Optional[str]): The text to convert

**Returns:**
- Optional[str]: The uppercase string, or None if input is None

**Usage Example:**
```python
>>> to_upper("hello world")
'HELLO WORLD'
```

**Cost:** O(n), where n is the length of the text

---

### to_lower

Converts a string to lowercase.

**Args:**
- `text` (Optional[str]): The text to convert

**Returns:**
- Optional[str]: The lowercase string, or None if input is None

**Usage Example:**
```python
>>> to_lower("HELLO WORLD")
'hello world'
```

**Cost:** O(n), where n is the length of the text

---

### normalize_spaces

Normalizes whitespace in a string by replacing multiple spaces with single spaces and trimming.

**Args:**
- `text` (Optional[str]): The text to normalize

**Returns:**
- Optional[str]: The normalized string, or None if input is None

**Usage Example:**
```python
>>> normalize_spaces("  hello    world  ")
'hello world'
```

**Cost:** O(n), where n is the length of the text

---

### normalize_symbols

Normalizes symbol spacing in a string according to typographical rules.

**Args:**
- `text` (Optional[str]): The text to normalize

**Returns:**
- Optional[str]: The normalized string with proper symbol spacing

**Usage Example:**
```python
>>> normalize_symbols("hello , world !")
'hello, world!'
```

**Cost:** O(n), where n is the length of the text

---

### flat_vowels

Removes diacritical marks (accents) from vowels in a string.

**Args:**
- `input_string` (str): The string to process

**Returns:**
- str: The string with accent marks removed from vowels

**Usage Example:**
```python
>>> flat_vowels("café")
'cafe'
>>> flat_vowels("niño")
'nino'
```

**Cost:** O(n), where n is the length of the input string

---

### ascii_string

Converts a string to ASCII, removing or replacing non-ASCII characters.

**Args:**
- `input_string` (str | None): The string to convert

**Returns:**
- str | None: The ASCII-compatible string, or None if input is None

**Usage Example:**
```python
>>> ascii_string("Héllo Wörld")
'Hello World'
```

**Cost:** O(n), where n is the length of the input string

---

### format_email_address

Formats and normalizes an email address.

**Args:**
- `email_string` (str): The email address to format

**Returns:**
- str: The formatted email address (lowercased, trimmed)

**Usage Example:**
```python
>>> format_email_address("  USER@EXAMPLE.COM  ")
'user@example.com'
```

**Cost:** O(n), where n is the length of the email string

---

### format_url

Formats and normalizes a URL.

**Args:**
- `url_string` (str): The URL to format

**Returns:**
- str: The formatted URL

**Usage Example:**
```python
>>> format_url("  HTTPS://EXAMPLE.COM/PATH  ")
'https://example.com/path'
```

**Cost:** O(n), where n is the length of the URL string

---

### format_name

Formats a person's name according to specified rules.

**Args:**
- `input_string` (str): The name to format
- `add_charset` (str): Additional allowed characters. Defaults to ""
- `name_type` (str): Type of name ('PERSONA' or 'EMPRESA'). Defaults to 'PERSONA'
- `shift` (bool): Whether to shift words. Defaults to False

**Returns:**
- str: The formatted name

**Usage Example:**
```python
>>> format_name("   john   doe  ")
'JOHN DOE'
```

**Cost:** O(n), where n is the length of the input string

---

### format_fullname

Formats a full name, removing titles and normalizing.

**Args:**
- `fullname` (str | None): The full name to format
- `uppercase` (bool): Whether to convert to uppercase. Defaults to True

**Returns:**
- str | None: The formatted full name, or None if input is None

**Usage Example:**
```python
>>> format_fullname("Dr. John Smith")
'JOHN SMITH'
```

**Cost:** O(n), where n is the length of the fullname

---

### format_company_name

Formats a company name, handling legal forms.

**Args:**
- `company_name` (str): The company name to format
- `remove_legal_form` (bool): Whether to remove legal forms. Defaults to False
- `legal_forms_set` (set): Set of legal forms to recognize. Defaults to None

**Returns:**
- str: The formatted company name

**Usage Example:**
```python
>>> format_company_name("Microsoft Corporation")
'MICROSOFT CORPORATION'
```

**Cost:** O(n * m), where n is the name length and m is the number of legal forms

---

## String Evaluations

Functions for evaluating, validating, and checking string properties.

### contains_digit

Checks if the given string contains at least one digit.

**Args:**
- `input_string` (str): The string to be checked for the presence of digits

**Returns:**
- bool: True if the string contains at least one digit, False otherwise

**Raises:**
- TypeError: If the input is not a string

**Usage Example:**
```python
>>> contains_digit("abc123def")
True
>>> contains_digit("no_digits_here")
False
```

**Cost:** O(n), where n is the length of the input string

---

### is_alphabetic

Checks if a string contains only alphabetic characters.

**Args:**
- `alpha_string`: The string to check

**Returns:**
- bool: True if the string contains only letters, False otherwise

**Usage Example:**
```python
>>> is_alphabetic("Hello")
True
>>> is_alphabetic("Hello123")
False
```

**Cost:** O(n), where n is the length of the string

---

### is_numeric

Checks if a string represents a valid number (integer or float).

**Args:**
- `input_string` (str): The string to check

**Returns:**
- bool: True if the string represents a valid number, False otherwise

**Usage Example:**
```python
>>> is_numeric("123")
True
>>> is_numeric("123.45")
True
>>> is_numeric("abc")
False
```

**Cost:** O(n), where n is the length of the input string

---

### is_internet_domain_format

Validates if a string matches the format of an internet domain.

**Args:**
- `domain_string` (str): The domain string to validate

**Returns:**
- bool: True if the string matches domain format, False otherwise

**Usage Example:**
```python
>>> is_internet_domain_format("example.com")
True
>>> is_internet_domain_format("sub.example.co.uk")
True
>>> is_internet_domain_format("invalid")
False
```

**Cost:** O(n), where n is the length of the domain string

---

### is_email_format

Validates if a string matches the format of an email address.

**Args:**
- `email_string` (str): The email string to validate

**Returns:**
- bool: True if the string matches email format, False otherwise

**Usage Example:**
```python
>>> is_email_format("user@example.com")
True
>>> is_email_format("invalid.email")
False
```

**Cost:** O(n), where n is the length of the email string

---

### is_url_format

Validates if a string matches the format of a URL.

**Args:**
- `url_string` (str): The URL string to validate

**Returns:**
- bool: True if the string matches URL format, False otherwise

**Usage Example:**
```python
>>> is_url_format("https://www.example.com")
True
>>> is_url_format("not a url")
False
```

**Cost:** O(n), where n is the length of the URL string

---

### has_date_format

Checks if a string can be interpreted as a date.

**Args:**
- `value` (str): The string to check

**Returns:**
- bool: True if the string represents a valid date format, False otherwise

**Usage Example:**
```python
>>> has_date_format("2023-10-26")
True
>>> has_date_format("not a date")
False
```

**Cost:** O(k * n), where k is the number of date formats and n is the string length

---

### has_numbers

Checks if a string contains any numeric digits.

**Args:**
- `input_string` (str): The string to check

**Returns:**
- bool: True if the string contains at least one digit, False otherwise

**Usage Example:**
```python
>>> has_numbers("Hello123")
True
>>> has_numbers("Hello")
False
```

**Cost:** O(n), where n is the length of the input string

---

### has_substring

Checks if a string contains a specific substring.

**Args:**
- `input_string` (str): The string to search in
- `char_to_find` (str): The substring to search for

**Returns:**
- bool: True if the substring is found, False otherwise

**Usage Example:**
```python
>>> has_substring("hello world", "world")
True
>>> has_substring("hello world", "python")
False
```

**Cost:** O(n * m), where n is the length of input_string and m is the length of char_to_find

---

### starts_with_substring

Checks if a string starts with a specific prefix.

**Args:**
- `input_string` (str): The string to check
- `prefix` (str): The prefix to look for
- `case_sensitive` (bool): Whether the comparison is case-sensitive. Defaults to True

**Returns:**
- bool: True if the string starts with the prefix, False otherwise

**Usage Example:**
```python
>>> starts_with_substring("hello world", "hello")
True
>>> starts_with_substring("Hello world", "hello", case_sensitive=False)
True
```

**Cost:** O(m), where m is the length of the prefix

---

### ends_with_substring

Checks if a string ends with a specific suffix.

**Args:**
- `input_string` (str): The string to check
- `suffix` (str): The suffix to look for
- `case_sensitive` (bool): Whether the comparison is case-sensitive. Defaults to True

**Returns:**
- bool: True if the string ends with the suffix, False otherwise

**Usage Example:**
```python
>>> ends_with_substring("hello world", "world")
True
>>> ends_with_substring("hello World", "world", case_sensitive=False)
True
```

**Cost:** O(m), where m is the length of the suffix

---

### parse_email

Parses an email address into its components.

**Args:**
- `email_address` (str): The email address to parse

**Returns:**
- dict | None: A dictionary with 'username' and 'domain' keys, or None if invalid

**Usage Example:**
```python
>>> parse_email("user@example.com")
{'username': 'user', 'domain': 'example.com'}
```

**Cost:** O(n), where n is the length of the email address

---

### username_from_email

Extracts the username portion from an email address.

**Args:**
- `email_address` (str): The email address

**Returns:**
- list[str] | None: The username part(s), or None if invalid

**Usage Example:**
```python
>>> username_from_email("john.doe@example.com")
['john', 'doe']
```

**Cost:** O(n), where n is the length of the email address

---

### domain_from_email

Extracts the domain portion from an email address.

**Args:**
- `email_address` (str): The email address

**Returns:**
- str | None: The domain part, or None if invalid

**Usage Example:**
```python
>>> domain_from_email("user@example.com")
'example.com'
```

**Cost:** O(n), where n is the length of the email address

---

## String Similarity

Functions for comparing strings and calculating similarity scores.

### calculate_similarity

Calculates similarity between two strings using specified algorithm.

**Args:**
- `string_one` (str): The first string to compare
- `string_two` (str): The second string to compare
- `algorithm` (str): The similarity algorithm to use
- `normalize` (bool): Whether to normalize the result. Defaults to True

**Returns:**
- Union[float, Dict[str, float]]: Similarity score or dictionary of scores

**Usage Example:**
```python
>>> calculate_similarity("hello", "hallo", algorithm="levenshtein")
0.8
```

**Cost:** Varies by algorithm, typically O(n * m) where n and m are string lengths

---

### has_same_words

Checks if two strings contain the same words (order-independent).

**Args:**
- `string_one` (str): The first string
- `string_two` (str): The second string

**Returns:**
- bool: True if both strings contain the same words, False otherwise

**Usage Example:**
```python
>>> has_same_words("hello world", "world hello")
True
>>> has_same_words("hello world", "hello python")
False
```

**Cost:** O(n + m), where n and m are the lengths of the strings

---

### find_common_words

Finds words that appear in both strings.

**Args:**
- `string_one` (str): The first string
- `string_two` (str): The second string

**Returns:**
- List[str]: A list of words common to both strings

**Usage Example:**
```python
>>> find_common_words("hello world", "world peace")
['world']
```

**Cost:** O(n + m), where n and m are the lengths of the strings

---

### has_same_characters

Checks if two strings contain the same characters (anagram check).

**Args:**
- `string_one` (str): The first string
- `string_two` (str): The second string

**Returns:**
- bool: True if both strings contain the same characters, False otherwise

**Usage Example:**
```python
>>> has_same_characters("listen", "silent")
True
>>> has_same_characters("hello", "world")
False
```

**Cost:** O(n log n), where n is the length of the longer string

---

### string_hamming_score

Calculates the Hamming distance between two strings.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- Dict[str, float]: Dictionary with 'distance' and 'similarity' scores

**Usage Example:**
```python
>>> string_hamming_score("karolin", "kathrin")
{'distance': 3, 'similarity': 0.571}
```

**Cost:** O(n), where n is the length of the strings

---

### string_levenshtein_score

Calculates the Levenshtein distance between two strings.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- Dict[str, float]: Dictionary with 'distance' and 'similarity' scores

**Usage Example:**
```python
>>> string_levenshtein_score("kitten", "sitting")
{'distance': 3, 'similarity': 0.571}
```

**Cost:** O(n * m), where n and m are the lengths of the strings

---

### string_jarowinkler_score

Calculates the Jaro-Winkler similarity between two strings.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- Dict[str, float]: Dictionary with similarity score

**Usage Example:**
```python
>>> string_jarowinkler_score("martha", "marhta")
{'similarity': 0.961}
```

**Cost:** O(n * m), where n and m are the lengths of the strings

---

### string_jaccard_score

Calculates the Jaccard similarity coefficient between two strings.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- Dict[str, float]: Dictionary with similarity score

**Usage Example:**
```python
>>> string_jaccard_score("hello", "hallo")
{'similarity': 0.6}
```

**Cost:** O(n + m), where n and m are the lengths of the strings

---

### string_similarity_score

Calculates multiple similarity scores between two strings using all available algorithms.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- List[Tuple[str, Union[Dict[str, float], float]]]: List of tuples with algorithm name and scores

**Usage Example:**
```python
>>> scores = string_similarity_score("hello", "hallo")
>>> # Returns scores from all algorithms
```

**Cost:** O(n * m) for most algorithms, combined

---

## String Spanish

Functions specific to Spanish language processing and validation.

### remove_spanish_stop_words

Removes common Spanish stop words from a string.

**Args:**
- `input_string` (str): The string to process

**Returns:**
- str | None: The string with stop words removed, or None if input is None

**Usage Example:**
```python
>>> remove_spanish_stop_words("el gato en la casa")
'gato casa'
```

**Cost:** O(n), where n is the length of the input string

---

### reduce_spanish_letters

Reduces Spanish text to a phonetic representation.

**Args:**
- `input_string` (str): The string to reduce
- `strength` (int): The strength of reduction (1-3)

**Returns:**
- str | None: The phonetically reduced string, or None if input is None

**Usage Example:**
```python
>>> reduce_spanish_letters("llamar", 2)
'yamar'
```

**Cost:** O(n), where n is the length of the input string

---

### nif_padding

Pads a Spanish NIF/CIF to standard format.

**Args:**
- `p_nif` (Optional[str]): The NIF to pad

**Returns:**
- Optional[str]: The padded NIF, or None if input is None

**Usage Example:**
```python
>>> nif_padding("12345678")
'00012345678'
```

**Cost:** O(1)

---

### nif_parse

Parses and normalizes a Spanish NIF/NIE/CIF.

**Args:**
- `nif` (Optional[str]): The NIF to parse

**Returns:**
- Optional[str]: The normalized NIF, or None if invalid

**Usage Example:**
```python
>>> nif_parse("12345678-Z")
'12345678Z'
```

**Cost:** O(n), where n is the length of the NIF

---

### nif_letter

Calculates the control letter for a Spanish DNI.

**Args:**
- `p_dni` (str): The DNI number (8 digits)

**Returns:**
- str: The control letter

**Usage Example:**
```python
>>> nif_letter("12345678")
'Z'
```

**Cost:** O(1)

---

### is_valid_dni

Validates a Spanish DNI (Documento Nacional de Identidad).

**Args:**
- `dni_value` (str): The DNI to validate

**Returns:**
- bool: True if the DNI is valid, False otherwise

**Usage Example:**
```python
>>> is_valid_dni("12345678Z")
True
>>> is_valid_dni("12345678X")
False
```

**Cost:** O(1)

---

### is_valid_nie

Validates a Spanish NIE (Número de Identidad de Extranjero).

**Args:**
- `nie_value` (str): The NIE to validate

**Returns:**
- bool: True if the NIE is valid, False otherwise

**Usage Example:**
```python
>>> is_valid_nie("X1234567L")
True
>>> is_valid_nie("X1234567M")
False
```

**Cost:** O(1)

---

### is_valid_cif

Validates a Spanish CIF (Certificado de Identificación Fiscal).

**Args:**
- `cif_value` (str): The CIF to validate

**Returns:**
- bool: True if the CIF is valid, False otherwise

**Usage Example:**
```python
>>> is_valid_cif("A12345674")
True
>>> is_valid_cif("A12345675")
False
```

**Cost:** O(1)

---

### validate_spanish_nif

Validates a Spanish NIF (DNI, NIE, or CIF).

**Args:**
- `nif_type` (str): The type of NIF ('DNI', 'NIE', or 'CIF')
- `nif_value` (str): The NIF value to validate

**Returns:**
- bool: True if the NIF is valid for the specified type, False otherwise

**Usage Example:**
```python
>>> validate_spanish_nif("DNI", "12345678Z")
True
>>> validate_spanish_nif("NIE", "X1234567L")
True
```

**Cost:** O(1)

---

### fix_spanish

Fixes common Spanish character encoding issues.

**Args:**
- `input_string` (str | None): The string to fix
- `additional_allowed_chars` (str): Additional allowed characters. Defaults to ''

**Returns:**
- str | None: The fixed string, or None if input is None

**Usage Example:**
```python
>>> fix_spanish("cafÃ©")
'café'
```

**Cost:** O(n), where n is the length of the input string

---

## String Validations

Functions for validating string properties and content.

### contains_digit

Checks if the given string contains at least one digit.

**Args:**
- `input_string` (str): The string to be checked for the presence of digits

**Returns:**
- bool: True if the string contains at least one digit, False otherwise

**Raises:**
- TypeError: If the input is not a string

**Usage Example:**
```python
>>> contains_digit("abc123def")
True
>>> contains_digit("no_digits_here")
False
```

**Cost:** O(n), where n is the length of the input string

---

### same_letters

Checks if two strings contain the exact same characters, irrespective of their order (anagram check).

**Args:**
- `string_a` (str): The first string for comparison
- `string_b` (str): The second string for comparison

**Returns:**
- bool: True if both strings contain the same characters (same count, same case), False otherwise

**Raises:**
- TypeError: If 'string_a' or 'string_b' are not strings

**Usage Example:**
```python
>>> same_letters("listen", "silent")
True
>>> same_letters("hello", "holle")
True
>>> same_letters("abc", "ab")
False
```

**Cost:** O(n log n), where n is the maximum length of the two input strings (due to sorting)

---

## String Spellcheck

Functions for spell checking and text normalization.

### normalize_text

Normalizes text for spell checking by converting to lowercase and removing accents.

**Args:**
- `text` (str): The text to normalize

**Returns:**
- str: The normalized text

**Usage Example:**
```python
>>> normalize_text("Héllo Wörld")
'hello world'
```

**Cost:** O(n), where n is the length of the text

---

## Summary

The fxString module provides a comprehensive suite of over 150 functions for:

- **String Conversions (11 functions)**: Type conversions, date parsing, JSON extraction
- **String Operations (60+ functions)**: Manipulation, extraction, substring operations
- **String Format (25+ functions)**: Formatting, normalization, capitalization
- **String Evaluations (25+ functions)**: Validation, pattern checking, email/URL parsing
- **String Similarity (20+ functions)**: Comparison algorithms, similarity scores
- **String Spanish (10+ functions)**: Spanish-specific validation and processing
- **String Validations (2 functions)**: Character presence and anagram checking
- **String Spellcheck (2+ functions)**: Text normalization for spell checking

All functions follow Python best practices (PEP standards), include comprehensive documentation with complexity analysis, and handle edge cases gracefully.
