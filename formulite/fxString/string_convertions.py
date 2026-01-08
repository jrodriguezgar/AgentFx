"""
FormuLite - fxString: String Conversions Module

This module provides comprehensive string conversion utilities for the FormuLite framework.
It includes functions for:
- Value replacement and null handling (replace_void, none_to_string)
- String to numeric conversions (string_to_integer, string_to_float, string_to_number)
- String to date/datetime conversions (string_to_date, string_to_datetime)
- String splitting utilities (split_all, split_by_substrings, split_limited)
- JSON extraction and decoding (extract_and_decode_json)

All conversion functions handle edge cases, invalid inputs, and return None on failure,
ensuring safe and predictable behavior in data processing pipelines.
"""

from datetime import datetime as dt, date
from typing import Any, List, Optional
import re
import json


def replace_void(primary_value: Any, replacement_value: Any = 'NaN') -> Any:
    """Replaces empty or None values with a specified replacement value.

    Problem/User Need: When handling data, it's common to need to replace empty,
    None, or zero-length values with a default value to ensure data consistency.

    Args:
        primary_value (Any): The primary value to check.
        replacement_value (Any): The value to use if primary_value is empty/None.

    Returns:
        Any: replacement_value if primary_value is empty/None/zero-length,
             otherwise returns primary_value.

    Example:
        >>> replace_void("", "default")
        'default'
        >>> replace_void(None, 0)
        0
        >>> replace_void([], [1, 2, 3])
        [1, 2, 3]
        >>> replace_void("hello", "default")
        'hello'
        >>> replace_void(0, 42)
        0  # 0 is not considered void
        
    Cost:
        Time complexity: O(1) for most types
        Space complexity: O(1)
    """
    # Check for None first as it's the most common case
    if primary_value is None:
        return replacement_value
    
    # For strings, lists, tuples, sets, dicts - check if empty
    if isinstance(primary_value, (str, list, tuple, set, dict)):
        if len(primary_value) == 0:
            return replacement_value
            
    # Return original value if not void
    return primary_value


def none_to_string(value: str | None) -> str:
    """
    Converts a None value to an empty string; otherwise, returns the original value.

    This utility function is particularly useful when you need to ensure that a variable
    that might be None is always treated as a string, specifically an empty string,
    to avoid TypeError exceptions in string operations. It leverages Python's
    truthiness to provide a concise and efficient conversion.

    Args:
        value (str | None): The input value, which could be a string or None.

    Returns:
        str: An empty string if the input 'value' was None, otherwise the original
             'value' itself (assuming it was already a string).

    Example:
        >>> none_to_string("hello")
        'hello'

        >>> none_to_string(None)
        ''

        >>> none_to_string("")
        ''

        >>> none_to_string("  ")
        '  '
    """
    # This leverages the 'or' operator's behavior: it returns the first truthy value.
    # If 'value' is None (which is falsy), it returns "" (empty string, which is truthy).
    # If 'value' is a non-empty string (truthy), it returns 'value' itself.
    # If 'value' is an empty string (falsy), it also returns "" as it's the second operand.
    return value or ""

    # **Cost:** O(1) - constant time operation


def string_to_integer(input_string: str) -> int | None:
    """Converts a string to an integer, returning None if conversion fails.

    This function attempts to convert the given `input_string` into an integer.
    It first cleans the string by removing all non-numeric characters except
    digits, '-', and '+'. It returns `None` if the cleaned string cannot be
    safely converted to an integer.

    Args:
        input_string (str): The string to be converted to an integer.

    Returns:
        int | None: The integer representation of the cleaned string, or None if
                    the conversion is not possible.

    Example:
        >>> string_to_integer("123")
        123
        >>> string_to_integer("-45")
        -45
        >>> string_to_integer("123.45")
        123
        >>> string_to_integer("abc123def")
        123
        >>> string_to_integer("12 34")
        1234
        >>> string_to_integer("abc")
        None
        >>> string_to_integer(None)
        None
    """
    if not isinstance(input_string, str):
        # We return None because the function specifically handles string conversion.
        # Non-string types cannot be directly converted this way.
        return None
    
    # Clean the string by removing all characters except digits, '-', and '+'
    cleaned_string = re.sub(r'[^0-9\-+]', '', input_string)
    
    if not cleaned_string:
        return None
    
    try:
        # Attempt to convert the cleaned string to an integer.
        # Python's built-in int() function is efficient and handles leading/trailing
        # whitespace and positive/negative signs automatically.
        return int(cleaned_string)
    except ValueError:
        # Catch ValueError if the cleaned string cannot be parsed as an integer.
        # This handles cases like multiple signs or invalid formats.
        return None

    # **Cost:** O(n), where n is the length of the input string, due to regex processing


def string_to_float(input_string: str) -> float | None:
    """Converts a string to a float, returning None if conversion fails.

    This function attempts to convert the given `input_string` into a floating-point number.
    It first normalizes the decimal separator by replacing commas with dots if a comma
    is present and no dot is found (assuming comma is used as decimal separator).
    Then, it cleans the string by removing all non-numeric characters except
    digits, '-', '+', and '.'. It returns `None` if the cleaned string cannot be
    safely converted to a float.

    Args:
        input_string (str): The string to be converted to a float.

    Returns:
        float | None: The float representation of the cleaned string, or None if
                      the conversion is not possible.

    Example:
        >>> string_to_float("123.45")
        123.45
        >>> string_to_float("-0.75")
        -0.75
        >>> string_to_float("100")
        100.0
        >>> string_to_float("123,45")
        123.45
        >>> string_to_float("abc123.45def")
        123.45
        >>> string_to_float("12 34.56")
        1234.56
        >>> string_to_float("abc")
        None
        >>> string_to_float(None)
        None
    """
    if not isinstance(input_string, str):
        # We return None for non-string inputs, as this function is for string conversion.
        return None
    
    # Normalize decimal separator: if comma is present and no dot, assume comma is decimal
    if ',' in input_string and '.' not in input_string:
        input_string = input_string.replace(',', '.')
    
    # Clean the string by removing all characters except digits, '-', '+', and '.'
    cleaned_string = re.sub(r'[^0-9\-+\.]', '', input_string)
    
    if not cleaned_string:
        return None
    
    try:
        # Attempt to convert the cleaned string to a float.
        # Python's built-in float() function handles various valid float formats,
        # including scientific notation and leading/trailing whitespace.
        return float(cleaned_string)
    except ValueError:
        # Catch ValueError if the cleaned string cannot be parsed as a float.
        # This covers cases like multiple dots or invalid formats.
        return None

    # **Cost:** O(n), where n is the length of the input string, due to regex processing


def string_to_number(input_string: str, target_type: str = 'string') -> int | float | None:
    """Converts a string to an integer or float based on the specified target type.

    This function acts as a dispatcher, calling `string_to_integer` or
    `string_to_float` based on the `target_type` argument. The underlying functions
    clean the input string by removing non-numeric characters and handle decimal
    separators (replacing commas with dots when appropriate). If the `target_type`
    is not 'integer' or 'float', it returns `None`. It also returns `None`
    if the conversion to the specified type fails.

    Args:
        input_string (str): The string to convert.
        target_type (str, optional): The desired numeric type ('integer' or 'float').
                                     Defaults to 'string', which results in None.

    Returns:
        int | float | None: The converted number (integer or float), or None if
                            the conversion fails or the target_type is invalid.

    Example:
        >>> string_to_number("123", "integer")
        123
        >>> string_to_number("123.45", "float")
        123.45
        >>> string_to_number("123,45", "float")
        123.45
        >>> string_to_number("abc123def", "integer")
        123
        >>> string_to_number("12 34.56", "float")
        1234.56
        >>> string_to_number("abc", "integer")
        None
        >>> string_to_number("not_a_number", "unknown_type")
        None
        >>> string_to_number(None, "integer")
        None
    """
    # Normalize the target_type to lowercase for case-insensitive comparison.
    normalized_type = target_type.lower()

    if normalized_type == 'integer':
        # Delegate to the specific integer conversion function.
        return string_to_integer(input_string)
    elif normalized_type == 'float':
        # Delegate to the specific float conversion function.
        return string_to_float(input_string)
    else:
        # If the target_type is neither 'integer' nor 'float', return None.
        # This handles the default 'string' case or any other unrecognized type.
        return None

    # **Cost:** O(n), where n is the length of input_string (delegates to string_to_integer or string_to_float)


# Consider if you want to use a third-party library like 'dateutil.parser'
# for even more flexible parsing, but for predefined formats, your current
# approach is perfectly fine and avoids external dependencies.


def string_to_date(input_value: str | date | dt) -> date | dt | None:
    """Converts a string to a date or datetime object based on common formats.

    This function intelligently parses the input value, attempting to convert
    strings into `datetime` or `date` objects using a prioritized list of
    common formats. If the input is already a `date` or `datetime` object,
    it's returned as is. It prioritizes formats with time components, returning
    a `datetime` object when time information is present, otherwise a `date` object.
    Returns `None` if the input string cannot be parsed into a valid date/datetime
    by any of the specified formats.

    Args:
        input_value (str | date | dt): The string or existing date/datetime object
                                        to be converted or returned.

    Returns:
        date | dt | None: A `datetime.date` object if the string represents only
                          a date, a `datetime.datetime` object if the string includes
                          time information, or `None` if the string cannot be parsed.

    Example:
        >>> from datetime import date, datetime
        >>> string_to_date("2023-10-26")
        datetime.date(2023, 10, 26)
        >>> string_to_date("2023-10-26 14:30:00")
        datetime.datetime(2023, 10, 26, 14, 30)
        >>> string_to_date("invalid date") is None
        True
        >>> string_to_date(date(2024, 1, 1))
        datetime.date(2024, 1, 1)
        >>> string_to_date(datetime(2024, 1, 1, 10, 0, 0))
        datetime.datetime(2024, 1, 1, 10, 0)
        >>> string_to_date("   ") is None
        True
        >>> string_to_date(None) is None
        True
    """
    if input_value is None:
        # Handles None input directly.
        return None

    if isinstance(input_value, (date, dt)):
        # If the input is already a date or datetime object, return it as is.
        # This avoids unnecessary processing.
        return input_value

    if not isinstance(input_value, str) or not input_value.strip():
        # If input_value is not a string, or is an empty/whitespace-only string, return None.
        # .strip() handles strings like " ", "  ", etc.
        return None

    # Defines the list of common date and datetime formats to attempt parsing.
    # More specific formats (with time components) are listed first to ensure
    # that if a string contains time, it's parsed as a datetime object.
    POSSIBLE_DATE_FORMATS = [
        "%Y-%m-%dT%H:%M:%S",  # ISO 8601 with 'T' separator (e.g., "2023-01-01T12:30:00")
        "%Y-%m-%d %H:%M:%S",  # Common YYYY-MM-DD HH:MM:SS (e.g., "2023-01-01 12:30:00")
        "%d/%m/%Y %H:%M:%S",  # DD/MM/YYYY HH:MM:SS (e.g., "01/01/2023 12:30:00")
        "%d-%m-%Y %H:%M:%S",  # DD-MM-YYYY HH:MM:SS (e.g., "01-01-2023 12:30:00")
        "%Y/%m/%d %H:%M:%S",  # YYYY/MM/DD HH:MM:SS (e.g., "2023/01/01 12:30:00")
        "%Y%m%d%H%M%S",       # Compact YYYYMMDDHHMMSS (e.g., "20230101123000")
        "%Y-%m-%d",           # YYYY-MM-DD (e.g., "2023-01-01")
        "%d/%m/%Y",           # DD/MM/YYYY (e.g., "01/01/2023")
        "%d-%m-%Y",           # DD-MM-YYYY (e.g., "01-01-2023")
        "%Y/%m/%d"            # YYYY/MM/DD (e.g., "2023/01/01")
    ]

    for date_format in POSSIBLE_DATE_FORMATS:
        try:
            # Attempt to parse the input string with the current format.
            date_object = dt.strptime(input_value, date_format)

            # Determine if the original format string included time components.
            # This is crucial for deciding whether to return a `datetime` or `date` object.
            if any(char_code in date_format for char_code in ['%H', '%M', '%S', '%f', '%Z', '%z']):
                return date_object  # Format includes time, return datetime object.
            else:
                return date_object.date()  # Format is date-only, return date object.

        except ValueError:
            # If the current format doesn't match the input string, continue to the next one.
            continue

    # If the loop completes without finding a matching format, the string cannot be parsed.
    return None

    # **Cost:** O(k * m), where k is the number of formats in POSSIBLE_DATE_FORMATS and m is the length of input_value    

def string_to_datetime(input_value: str | date | dt) -> dt | None:
    """
    Description:
        Converts a string to a datetime.datetime object using common date and datetime formats.
        If the input is already a datetime object, it is returned as is.
        If the input is a date object, it is converted to a datetime at midnight.
        Returns None if the string cannot be parsed.

    Args:
        input_value (str | date | dt): The value to convert. Can be a string, date, or datetime.

    Returns:
        dt | None: A datetime.datetime object if conversion is successful, otherwise None.

    Raises:
        None. Returns None on failure.

    Example Usage:
        >>> string_to_datetime("2023-10-26 14:30:00")
        datetime.datetime(2023, 10, 26, 14, 30)
        >>> string_to_datetime("2023-10-26")
        datetime.datetime(2023, 10, 26, 0, 0)
        >>> string_to_datetime(date(2024, 1, 1))
        datetime.datetime(2024, 1, 1, 0, 0)
        >>> string_to_datetime(datetime(2024, 1, 1, 10, 0, 0))
        datetime.datetime(2024, 1, 1, 10, 0)
        >>> string_to_datetime("invalid date") is None
        True

    Cost:
        O(N * M), where N is the number of formats and M is the length of the input string.
    """
    if input_value is None:
        return None

    if isinstance(input_value, dt):
        return input_value

    if isinstance(input_value, date):
        # Convert date to datetime at midnight
        return dt(input_value.year, input_value.month, input_value.day)

    if not isinstance(input_value, str) or not input_value.strip():
        return None

    POSSIBLE_DATETIME_FORMATS = [
        "%Y-%m-%dT%H:%M:%S",      # ISO 8601 with 'T'
        "%Y-%m-%d %H:%M:%S",      # Common format
        "%d/%m/%Y %H:%M:%S",      # European format
        "%d-%m-%Y %H:%M:%S",
        "%Y/%m/%d %H:%M:%S",
        "%Y%m%d%H%M%S",
        "%Y-%m-%d",               # Date only
        "%d/%m/%Y",
        "%d-%m-%Y",
        "%Y/%m/%d"
    ]

    for fmt in POSSIBLE_DATETIME_FORMATS:
        try:
            parsed = dt.strptime(input_value, fmt)
            return parsed
        except ValueError:
            continue

    return None


# --- Splits ---    

def split_all(input_string: str, delimiter_pattern: str = r'[.\-_\s,/():;\'"\\]+') -> list:
    """
    Splits a string by an expanded set of common delimiters and removes any empty strings from the result.

    The default pattern now includes: periods, hyphens, underscores, whitespace,
    commas, slashes, parentheses, colons, semicolons, single quotes, double quotes,
    and backslashes. It also handles multiple consecutive delimiters.

    Args:
        input_string (str): The string to be split.
        delimiter_pattern (str): The regular expression pattern to use as a delimiter.
                                 Defaults to '[.\-_\s,/():;\'"\\]+'.

    Returns:
        list: A list of non-empty strings resulting from the split operation.

    Raises:
        TypeError: If 'input_string' is not a string.

    Example:
        >>> split_all("hello-world_123/test")
        ['hello', 'world', '123', 'test']
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # Split the string using the regular expression pattern and filter out empty strings
    # The 're.split' function can produce empty strings when delimiters are at the start/end
    # of the string or when multiple delimiters appear consecutively.
    # The list comprehension efficiently filters these out.
    return [part for part in re.split(delimiter_pattern, input_string) if part]

    # **Cost:** O(n), where n is the length of the input string


def split_by_substrings(input_string: str, separators: list[str]) -> list[str]:
    """
    Splits a string by a list of substrings (separators), preserving the separators
    and handling the initial segment before the first separator.

    This function is designed to split a string such that each resulting part
    (except possibly the very first one) starts with one of the specified separators,
    followed by the text until the next separator or the end of the string.
    The segment before the first separator, if any, is included as the initial element.

    Args:
        input_string (str): The string to be split.
        separators (list[str]): A list of strings to use as separators.

    Returns:
        list[str]: A list of strings, where each string represents a segment
                   of the original string. The first segment may not start
                   with a separator, but subsequent segments will.

    Raises:
        TypeError: If 'input_string' is not a string or 'separators' is not a list.
        ValueError: If 'separators' is an empty list or contains non-string elements.

    Example:
        >>> split_by_substrings("Name: John Doe; Age: 30, City: New York", [":", ";", ","])
        ['Name:', ' John Doe;', ' Age:', ' 30,', ' City:', ' New York']

        >>> split_by_substrings("First.Second-Third", [".", "-"])
        ['First', '.Second', '-Third']

        >>> split_by_substrings("No Separators Here", ["X"])
        ['No Separators Here']

        >>> split_by_substrings(":Starts with separator; End", [":", ";"])
        [':', 'Starts with separator;', ' End']
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(separators, list):
        raise TypeError("Input 'separators' must be a list of strings.")
    if not separators:
        raise ValueError("The 'separators' list cannot be empty.")
    if not all(isinstance(sep, str) for sep in separators):
        raise ValueError("All elements in 'separators' must be strings.")

    # Escape special regular expression characters in separators.
    # This ensures that characters like '.', '?', '*', '+' are treated as literal characters.
    escaped_separators = [re.escape(s) for s in separators]

    # Create a regular expression pattern that matches any of the escaped separators.
    # We use a non-capturing group (?:...) for the union of separators.
    separator_pattern = '|'.join(escaped_separators)

    # Use re.split with a capturing group around the separator pattern.
    # This ensures that the separators themselves are included in the split result.
    # Example: re.split('(,|;)', "a,b;c") -> ['a', ',', 'b', ';', 'c']
    parts_with_separators = re.split(f"({separator_pattern})", input_string)

    # Initialize the list of final segments.
    result_segments = []
    current_segment = []

    # Iterate through the parts and reconstruct the segments.
    # The split result will alternate between content and separator (if a separator was matched).
    for i, part in enumerate(parts_with_separators):
        if part:  # Only process non-empty parts
            # Check if the current part is one of our separators.
            # We re-escape and join the original separators for accurate checking.
            if re.fullmatch(f"(?:{separator_pattern})", part):
                # If it's a separator and we have accumulated a segment, add it to results.
                if current_segment:
                    result_segments.append("".join(current_segment))
                    current_segment = []
                # Add the separator itself to the current segment.
                current_segment.append(part)
            else:
                # If it's not a separator, add it to the current segment.
                current_segment.append(part)

    # Add any remaining accumulated segment.
    if current_segment:
        result_segments.append("".join(current_segment))

    return result_segments

    # **Cost:** O(n + m * k), where n is the string length, m is the number of separators, and k is the number of segments


def split_limited(input_string: str, limit: int) -> list[str]:
    """
    Splits a string by whitespace into a list of words, with an optional limit
    on the number of initial words.

    If the total number of words in the string exceeds the specified limit,
    the function returns a list containing the first 'limit' words, and all
    remaining words are joined back into a single string as the last element
    of the list. If the string has fewer words than the limit, all words are
    returned individually.

    Args:
        input_string (str): The string to be split.
        limit (int): The maximum number of initial words to return individually.
                     Must be a non-negative integer.

    Returns:
        list[str]: A list of strings, where the last element might contain
                   multiple words if the original string exceeded the limit.

    Raises:
        TypeError: If 'input_string' is not a string or 'limit' is not an integer.
        ValueError: If 'limit' is a negative integer.

    Example:
        >>> split_limited("This is a test of the split function", 3)
        ['This', 'is', 'a', 'test of the split function']

        >>> split_limited("Hello world", 5)
        ['Hello', 'world']

        >>> split_limited("SingleWord", 1)
        ['SingleWord']

        >>> split_limited("", 2)
        ['']
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(limit, int):
        raise TypeError("Input 'limit' must be an integer.")
    if limit < 0:
        raise ValueError("Input 'limit' cannot be negative.")

    # Split the input string by whitespace.
    # This creates a list of words from the string.
    words = input_string.split()

    # If the number of words is less than or equal to the limit,
    # return all words as individual elements.
    if len(words) <= limit:
        return words
    else:
        # If the number of words exceeds the limit,
        # take the first 'limit' words and join the rest back into a single string.
        # This creates the desired output where excess words are grouped.
        return words[:limit] + [" ".join(words[limit:])]

    # **Cost:** O(n), where n is the length of the input string


def extract_and_decode_json(text_content: str) -> Optional[dict]:
    """
    Extracts and decodes a JSON string embedded within a block delimited
    by ```json\\n and \\n``` in a given string.

    This function is designed to parse text that might contain a fenced
    code block specifically for JSON. It uses regular expressions to
    locate the JSON content and then attempts to parse it into a Python
    dictionary. Error handling is included for invalid input types and
    JSON decoding issues.

    Args:
        text_content (str): The input string potentially containing a
                            fenced JSON block.

    Returns:
        Optional[dict]: A dictionary representing the decoded JSON if found
                        and successfully parsed; otherwise, returns None.

    Raises:
        No specific exceptions are raised by this function, as decoding
        errors are caught and result in a 'None' return.

    Example of use:
        >>> example_string = "Some text before.\\n```json\\n{\\"key\\": \\"value\\"}\\n```\\nMore text after."
        >>> extract_and_decode_json(example_string)
        {'key': 'value'}

        >>> invalid_string = "No JSON here."
        >>> extract_and_decode_json(invalid_string)
        None
    """
    if not isinstance(text_content, str) or not text_content:
        # Return None for non-string or empty inputs, as there's no
        # content to parse for JSON.
        return None

    # The regex pattern specifically targets the '```json\n...\n```' block.
    # re.DOTALL is crucial as it allows '.' to match newline characters,
    # enabling the pattern to span multiple lines.
    json_block_match = re.search(r'```json\n(.*?)\n```', text_content, re.DOTALL)

    if json_block_match:
        # Extract the matched JSON string content from the capturing group.
        # .strip() removes any leading/trailing whitespace, ensuring clean parsing.
        json_string = json_block_match.group(1).strip()

        if not json_string:
            # If the extracted content is empty after stripping, it means
            # there was no actual JSON content within the delimiters.
            return None

        try:
            # Attempt to parse the cleaned JSON string into a Python dictionary.
            decoded_json = json.loads(json_string)
            return decoded_json
        except json.JSONDecodeError as e:
            # Catch JSON-specific decoding errors and print a user-friendly
            # message, then return None to indicate failure.
            print(f"JSON decoding error: {e}")
            return None
    
    # If the regex pattern doesn't find a match in the input string,
    # it means no JSON block was present.
    return None

    # **Cost:** O(n), where n is the length of the text content, due to regex search

