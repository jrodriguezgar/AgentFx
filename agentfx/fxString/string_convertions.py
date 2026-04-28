"""
AgentFx - fxString: String Conversions Module

This module provides comprehensive string conversion utilities for the AgentFx framework.
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
from typing import Any, Optional
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
    result = string_to_date(input_value)

    if result is None:
        return None

    if isinstance(result, dt):
        return result

    if isinstance(result, date):
        return dt(result.year, result.month, result.day)

    return None


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
        except json.JSONDecodeError:
            return None
    
    # If the regex pattern doesn't find a match in the input string,
    # it means no JSON block was present.
    return None

    # **Cost:** O(n), where n is the length of the text content, due to regex search


def string_to_boolean(text: str) -> Optional[bool]:
    """Converts a string representation to a boolean value.

    Recognizes common true/false words in English and Spanish.

    Args:
        text: The string to convert.

    Returns:
        True, False, or None if the string is not recognized.

    Example:
        >>> string_to_boolean("yes")
        True
        >>> string_to_boolean("no")
        False
        >>> string_to_boolean("maybe")

    Complexity: O(1)
    """
    if not isinstance(text, str):
        return None

    normalized = text.strip().lower()

    if normalized in {"true", "yes", "1", "on", "sí", "si", "verdadero"}:
        return True

    if normalized in {"false", "no", "0", "off", "falso"}:
        return False

    return None


def boolean_to_string(value: bool, language: str = "en") -> str:
    """Converts a boolean value to its string representation.

    Args:
        value: The boolean to convert.
        language: Output language — "en" for English, "es" for Spanish.

    Returns:
        String representation of the boolean.

    Example:
        >>> boolean_to_string(True)
        'true'
        >>> boolean_to_string(False, language="es")
        'falso'

    Complexity: O(1)
    """
    mapping = {
        "en": {True: "true", False: "false"},
        "es": {True: "verdadero", False: "falso"},
    }

    lang_map = mapping.get(language, mapping["en"])
    return lang_map.get(bool(value), str(value))


def string_to_list(text: str, delimiter: str = ",", strip: bool = True) -> list[str]:
    """Parses a delimited string into a list of strings.

    Args:
        text: The input delimited string.
        delimiter: The separator character or string.
        strip: Whether to strip whitespace from each element.

    Returns:
        A list of string elements.

    Example:
        >>> string_to_list("a, b, c")
        ['a', 'b', 'c']
        >>> string_to_list("1;2;3", delimiter=";")
        ['1', '2', '3']

    Complexity: O(n)
    """
    if not isinstance(text, str) or not text:
        return []

    parts = text.split(delimiter)

    if strip:
        return [p.strip() for p in parts]

    return parts


def integer_to_roman(number: int) -> str:
    """Converts a positive integer to its Roman numeral representation.

    Delegates to :func:`~agentfx.fxNumeric.conversion_functions.int_to_roman`.

    Args:
        number: An integer between 1 and 3999.

    Returns:
        The Roman numeral string.

    Raises:
        ValueError: If number is out of the valid range.

    Example:
        >>> integer_to_roman(14)
        'XIV'

    Complexity: O(1)
    """
    from agentfx.fxNumeric.conversion_functions import int_to_roman

    return int_to_roman(number)


def roman_to_integer(text: str) -> int:
    """Converts a Roman numeral string to an integer.

    Delegates to :func:`~agentfx.fxNumeric.conversion_functions.roman_to_int`.

    Args:
        text: A valid Roman numeral string (e.g. "XIV").

    Returns:
        The integer value.

    Raises:
        ValueError: If the string contains invalid Roman numeral characters.

    Example:
        >>> roman_to_integer("XIV")
        14

    Complexity: O(n)
    """
    from agentfx.fxNumeric.conversion_functions import roman_to_int

    return roman_to_int(text)


def text_to_binary(text: str, separator: str = " ") -> str:
    """Converts text to its binary (8-bit) representation.

    Args:
        text: The input string.
        separator: Separator between byte groups (default: space).

    Returns:
        A binary string representation.

    Example:
        >>> text_to_binary("AB")
        '01000001 01000010'
        >>> text_to_binary("Hi")
        '01001000 01101001'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    return separator.join(format(ord(ch), "08b") for ch in text)


def binary_to_text(binary_str: str, separator: str = " ") -> str:
    """Converts a binary string back to text.

    Args:
        binary_str: Space-separated 8-bit binary bytes.
        separator: Separator used between byte groups (default: space).

    Returns:
        The decoded text string.

    Raises:
        ValueError: If any byte is not valid 8-bit binary.

    Example:
        >>> binary_to_text("01000001 01000010")
        'AB'

    Complexity: O(n)
    """
    if not isinstance(binary_str, str):
        raise TypeError("Input must be a string.")

    parts = binary_str.strip().split(separator)
    chars: list[str] = []

    for part in parts:
        part = part.strip()

        if not part:
            continue

        if len(part) != 8 or not all(c in "01" for c in part):
            raise ValueError(f"Invalid binary byte: '{part}'")

        chars.append(chr(int(part, 2)))

    return "".join(chars)


_MORSE_ENCODE: dict[str, str] = {
    "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
    "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
    "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
    "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
    "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
    "Z": "--..",
    "0": "-----", "1": ".----", "2": "..---", "3": "...--", "4": "....-",
    "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
    ".": ".-.-.-", ",": "--..--", "?": "..--..", "'": ".----.",
    "!": "-.-.--", "/": "-..-.", "(": "-.--.", ")": "-.--.-",
    "&": ".-...", ":": "---...", ";": "-.-.-.", "=": "-...-",
    "+": ".-.-.", "-": "-....-", "_": "..--.-", '"': ".-..-.",
    "@": ".--.-.",
}
_MORSE_DECODE: dict[str, str] = {v: k for k, v in _MORSE_ENCODE.items()}


def text_to_morse(text: str) -> str:
    """Converts text to International Morse Code.

    Letters are separated by spaces, words by `` / ``.
    Unknown characters are silently skipped.

    Args:
        text: The input string.

    Returns:
        The Morse code representation.

    Example:
        >>> text_to_morse("SOS")
        '... --- ...'
        >>> text_to_morse("HI THERE")
        '.... .. / - .... . .-. .'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    words = text.upper().split()
    coded_words: list[str] = []

    for word in words:
        coded = " ".join(_MORSE_ENCODE[ch] for ch in word if ch in _MORSE_ENCODE)

        if coded:
            coded_words.append(coded)

    return " / ".join(coded_words)


def morse_to_text(morse: str) -> str:
    """Decodes International Morse Code back to text.

    Letters are separated by spaces, words by `` / ``.

    Args:
        morse: The Morse code string.

    Returns:
        The decoded text (uppercase).

    Example:
        >>> morse_to_text("... --- ...")
        'SOS'
        >>> morse_to_text(".... .. / - .... . .-. .")
        'HI THERE'

    Complexity: O(n)
    """
    if not isinstance(morse, str):
        raise TypeError("Input must be a string.")

    words = morse.strip().split(" / ")
    decoded: list[str] = []

    for word in words:
        letters = word.strip().split()
        decoded.append("".join(_MORSE_DECODE.get(letter, "") for letter in letters))

    return " ".join(decoded)


def char_from_code(code_point: int) -> str:
    """Returns the Unicode character for a given code point.

    Description:
        Converts an integer code point to the corresponding Unicode
        character. Equivalent to Excel UNICHAR.

    Args:
        code_point: A valid Unicode code point (1 to 1114111).

    Returns:
        The single Unicode character.

    Raises:
        TypeError: If input is not an integer.
        ValueError: If code point is out of valid Unicode range.

    Example:
        >>> char_from_code(65)
        'A'
        >>> char_from_code(8364)
        '€'
        >>> char_from_code(128522)
        '😊'

    Complexity: O(1)
    """
    if not isinstance(code_point, int):
        raise TypeError("code_point must be an integer.")

    if code_point < 1 or code_point > 0x10FFFF:
        raise ValueError("code_point must be between 1 and 1114111.")

    return chr(code_point)


def code_from_char(character: str) -> int:
    """Returns the Unicode code point of the first character of a string.

    Description:
        Returns the numeric code point for the first character.
        Equivalent to Excel UNICODE.

    Args:
        character: A non-empty string (first character is used).

    Returns:
        The Unicode code point as an integer.

    Raises:
        TypeError: If input is not a string.
        ValueError: If the string is empty.

    Example:
        >>> code_from_char('A')
        65
        >>> code_from_char('€')
        8364

    Complexity: O(1)
    """
    if not isinstance(character, str):
        raise TypeError("Input must be a string.")

    if not character:
        raise ValueError("Input string cannot be empty.")

    return ord(character[0])


def parse_text_to_number(
    text: str,
    decimal_separator: str = ".",
    group_separator: str = ",",
) -> float:
    """Convert formatted text to a numeric value.

    Description:
        Strips currency symbols (``$``, ``€``), group separators, and
        handles percentages and locale-specific decimal separators.
        Equivalent to Excel ``VALUE`` / ``NUMBERVALUE``.

    Args:
        text: The text to convert.
        decimal_separator: Character used as decimal point (default ``"."``).
        group_separator: Character used for thousands (default ``","``).

    Returns:
        The parsed numeric value.

    Raises:
        ValueError: If the text cannot be converted.

    Example:
        >>> parse_text_to_number("$1,000.50")
        1000.5
        >>> parse_text_to_number("25%")
        0.25
        >>> parse_text_to_number("1.234,56", ",", ".")
        1234.56

    Complexity: O(n)
    """
    text_str = str(text).strip()

    is_percentage = text_str.endswith("%")

    if is_percentage:
        text_str = text_str[:-1].strip()

    if group_separator:
        text_str = text_str.replace(group_separator, "")

    if decimal_separator != ".":
        text_str = text_str.replace(decimal_separator, ".")

    text_str = (
        text_str.replace("$", "")
        .replace("€", "")
        .replace("£", "")
        .replace("¥", "")
        .replace("฿", "")
        .replace(" ", "")
    )

    try:
        result = float(text_str)
    except ValueError:
        raise ValueError(f"Cannot convert '{text}' to a number.")

    if is_percentage:
        result /= 100

    return result


def value_to_text(value: object, format_type: int = 0) -> str:
    """Converts any value to its text representation.

    Description:
        Returns a string representation of the given value. When
        format_type is 0, returns a concise representation. When 1,
        returns a quoted representation suitable for formulas.
        Equivalent to Excel VALUETOTEXT.

    Args:
        value: Any Python value.
        format_type: 0 for concise (default), 1 for quoted/repr.

    Returns:
        The text representation of the value.

    Example:
        >>> value_to_text(123)
        '123'
        >>> value_to_text("hello", 1)
        '"hello"'
        >>> value_to_text([1, 2, 3])
        '[1, 2, 3]'

    Complexity: O(n) where n is the string length of the representation.
    """
    if format_type == 1:
        return repr(value)

    return str(value)


def to_full_width(text: str) -> str:
    """Converts half-width (single-byte) characters to full-width (double-byte).

    Transforms ASCII printable characters (``!`` through ``~``) and the
    space character into their Unicode full-width equivalents.  Useful for
    CJK typography where monospaced alignment is needed.

    Args:
        text: The input string containing half-width characters.

    Returns:
        A new string with half-width characters replaced by full-width ones.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> to_full_width("HELLO")
        '\uff28\uff25\uff2c\uff2c\uff2f'
        >>> to_full_width("123")
        '\uff11\uff12\uff13'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Argument 'text' must be a string.")

    result: list[str] = []

    for char in text:
        code = ord(char)

        if 0x21 <= code <= 0x7E:
            result.append(chr(code + 0xFEE0))
        elif code == 0x20:
            result.append('\u3000')
        else:
            result.append(char)

    return ''.join(result)


def to_half_width(text: str) -> str:
    """Converts full-width (double-byte) characters to half-width (single-byte).

    Inverse of :func:`to_full_width`.  Transforms Unicode full-width
    printable characters back into their standard ASCII equivalents.

    Args:
        text: The input string containing full-width characters.

    Returns:
        A new string with full-width characters replaced by half-width ones.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> to_half_width('\uff28\uff25\uff2c\uff2c\uff2f')
        'HELLO'
        >>> to_half_width('\uff11\uff12\uff13')
        '123'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Argument 'text' must be a string.")

    result: list[str] = []

    for char in text:
        code = ord(char)

        if 0xFF01 <= code <= 0xFF5E:
            result.append(chr(code - 0xFEE0))
        elif code == 0x3000:
            result.append(' ')
        else:
            result.append(char)

    return ''.join(result)


# NATO phonetic alphabet mapping
_NATO_ALPHABET: dict[str, str] = {
    "A": "Alpha", "B": "Bravo", "C": "Charlie", "D": "Delta",
    "E": "Echo", "F": "Foxtrot", "G": "Golf", "H": "Hotel",
    "I": "India", "J": "Juliet", "K": "Kilo", "L": "Lima",
    "M": "Mike", "N": "November", "O": "Oscar", "P": "Papa",
    "Q": "Quebec", "R": "Romeo", "S": "Sierra", "T": "Tango",
    "U": "Uniform", "V": "Victor", "W": "Whiskey", "X": "X-ray",
    "Y": "Yankee", "Z": "Zulu",
}
_NATO_REVERSE: dict[str, str] = {v.upper(): k for k, v in _NATO_ALPHABET.items()}


def text_to_nato_phonetic(text: str) -> str:
    """Convert text to NATO phonetic alphabet representation.

    Non-alphabetic characters are passed through unchanged.

    Args:
        text: Input text.

    Returns:
        Space-separated NATO phonetic words.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> text_to_nato_phonetic("AB")
        'Alpha Bravo'
        >>> text_to_nato_phonetic("SOS")
        'Sierra Oscar Sierra'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    parts: list[str] = []

    for ch in text:
        upper = ch.upper()
        parts.append(_NATO_ALPHABET.get(upper, ch))

    return " ".join(parts)


def nato_phonetic_to_text(phonetic: str) -> str:
    """Convert NATO phonetic alphabet words back to plain text.

    Args:
        phonetic: Space-separated NATO phonetic words.

    Returns:
        Decoded plain text (uppercase).

    Raises:
        TypeError: If *phonetic* is not a string.

    Example:
        >>> nato_phonetic_to_text("Alpha Bravo")
        'AB'
        >>> nato_phonetic_to_text("Sierra Oscar Sierra")
        'SOS'

    Complexity: O(n)
    """
    if not isinstance(phonetic, str):
        raise TypeError("phonetic must be a string")

    parts: list[str] = []

    for word in phonetic.split():
        parts.append(_NATO_REVERSE.get(word.upper(), word))

    return "".join(parts)


# Braille mapping (ASCII printable → Braille Patterns U+2800 block)
_BRAILLE_MAP: dict[str, str] = {
    "a": "⠁", "b": "⠃", "c": "⠉", "d": "⠙", "e": "⠑",
    "f": "⠋", "g": "⠛", "h": "⠓", "i": "⠊", "j": "⠚",
    "k": "⠅", "l": "⠇", "m": "⠍", "n": "⠝", "o": "⠕",
    "p": "⠏", "q": "⠟", "r": "⠗", "s": "⠎", "t": "⠞",
    "u": "⠥", "v": "⠧", "w": "⠺", "x": "⠭", "y": "⠽",
    "z": "⠵",
    "1": "⠂", "2": "⠆", "3": "⠒", "4": "⠲", "5": "⠢",
    "6": "⠖", "7": "⠶", "8": "⠦", "9": "⠔", "0": "⠴",
    " ": "⠀", ".": "⠨", ",": "⠠", "!": "⠮", "?": "⠹",
}


def text_to_braille(text: str) -> str:
    """Convert ASCII text to Unicode Braille representation.

    Supports lowercase/uppercase letters, digits, and basic punctuation.
    Unsupported characters are passed through unchanged.

    Args:
        text: Input text.

    Returns:
        Braille-encoded string using Unicode Braille Patterns.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> text_to_braille("ab")
        '⠁⠃'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    parts: list[str] = []

    for ch in text:
        parts.append(_BRAILLE_MAP.get(ch.lower(), ch))

    return "".join(parts)


# Simplified English → IPA mapping (broad transcription)
_IPA_MAP: dict[str, str] = {
    "a": "æ", "b": "b", "c": "k", "d": "d", "e": "ɛ",
    "f": "f", "g": "ɡ", "h": "h", "i": "ɪ", "j": "dʒ",
    "k": "k", "l": "l", "m": "m", "n": "n", "o": "ɒ",
    "p": "p", "q": "k", "r": "ɹ", "s": "s", "t": "t",
    "u": "ʌ", "v": "v", "w": "w", "x": "ks", "y": "j",
    "z": "z",
}


def text_to_phonetic_ipa(text: str) -> str:
    """Convert ASCII text to a simplified IPA transcription.

    Uses a basic letter-by-letter mapping for English. This is a
    rough broad transcription, not a full phonological analysis.

    Args:
        text: Input ASCII text.

    Returns:
        IPA string.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> text_to_phonetic_ipa("hello")
        'hɛllɒ'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    parts: list[str] = []

    for ch in text:
        parts.append(_IPA_MAP.get(ch.lower(), ch))

    return "".join(parts)


def hex_color_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Convert a hex colour string to an RGB tuple.

    Accepts ``#RGB`` and ``#RRGGBB`` formats.

    Args:
        hex_color: Hex colour string starting with ``#``.

    Returns:
        Tuple of ``(red, green, blue)`` in the range 0-255.

    Raises:
        TypeError: If *hex_color* is not a string.
        ValueError: If the format is invalid.

    Example:
        >>> hex_color_to_rgb("#FF8800")
        (255, 136, 0)

    Complexity: O(1)
    """
    if not isinstance(hex_color, str):
        raise TypeError("hex_color must be a string")

    h = hex_color.lstrip("#")

    if len(h) == 3:
        h = h[0] * 2 + h[1] * 2 + h[2] * 2

    if len(h) != 6 or not all(c in "0123456789abcdefABCDEF" for c in h):
        raise ValueError(f"Invalid hex colour: {hex_color!r}")

    return (int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16))


def rgb_to_hex_color(r: int, g: int, b: int) -> str:
    """Convert RGB values to a hex colour string.

    Args:
        r: Red component (0-255).
        g: Green component (0-255).
        b: Blue component (0-255).

    Returns:
        Hex colour string in ``#RRGGBB`` format.

    Raises:
        TypeError: If any argument is not an integer.
        ValueError: If any value is outside [0, 255].

    Example:
        >>> rgb_to_hex_color(255, 136, 0)
        '#FF8800'

    Complexity: O(1)
    """
    for name, val in (("r", r), ("g", g), ("b", b)):

        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer")

        if val < 0 or val > 255:
            raise ValueError(f"{name} must be 0-255, got {val}")

    return f"#{r:02X}{g:02X}{b:02X}"


def base64_encode(text: str, encoding: str = "utf-8") -> str:
    """Encode a string to Base64.

    Args:
        text: Plain text to encode.
        encoding: Character encoding for the input bytes.

    Returns:
        Base64-encoded string.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> base64_encode("Hello World")
        'SGVsbG8gV29ybGQ='

    Complexity: O(n)
    """
    import base64

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return base64.b64encode(text.encode(encoding)).decode("ascii")


def base64_decode(encoded: str, encoding: str = "utf-8") -> str:
    """Decode a Base64 string to plain text.

    Args:
        encoded: Base64-encoded string.
        encoding: Character encoding for the output bytes.

    Returns:
        Decoded plain text.

    Raises:
        TypeError: If *encoded* is not a string.
        ValueError: If *encoded* is not valid Base64.

    Example:
        >>> base64_decode("SGVsbG8gV29ybGQ=")
        'Hello World'

    Complexity: O(n)
    """
    import base64 as _b64

    if not isinstance(encoded, str):
        raise TypeError("encoded must be a string")

    try:
        return _b64.b64decode(encoded).decode(encoding)
    except Exception as exc:
        raise ValueError(f"Invalid Base64: {exc}") from exc


def ordinal_suffix(n: int) -> str:
    """Converts an integer to its English ordinal string.

    Args:
        n: The integer to convert.

    Returns:
        String with the number and its ordinal suffix
        (e.g. ``'1st'``, ``'2nd'``, ``'3rd'``, ``'11th'``).

    Raises:
        TypeError: If n is not an integer.

    Example:
        >>> ordinal_suffix(1)
        '1st'
        >>> ordinal_suffix(22)
        '22nd'
        >>> ordinal_suffix(113)
        '113th'

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    abs_n = abs(n)

    if 11 <= (abs_n % 100) <= 13:
        return f"{n}th"

    suffix = {1: "st", 2: "nd", 3: "rd"}.get(abs_n % 10, "th")

    return f"{n}{suffix}"


def text_to_hex(text: str, encoding: str = "utf-8") -> str:
    """Converts text to its hexadecimal byte representation.

    Description:
        Encodes the string with the specified encoding and returns
        the hex string (lowercase, no prefix).

    Args:
        text: The input text.
        encoding: Character encoding to use.

    Returns:
        Hexadecimal string representation.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> text_to_hex("Hello")
        '48656c6c6f'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return text.encode(encoding).hex()


def hex_to_text(hex_str: str, encoding: str = "utf-8") -> str:
    """Converts a hexadecimal string back to text.

    Description:
        Interprets the hex string as bytes and decodes with the
        specified encoding.

    Args:
        hex_str: The hexadecimal string (no prefix).
        encoding: Character encoding to use.

    Returns:
        Decoded text string.

    Raises:
        TypeError: If *hex_str* is not a string.
        ValueError: If the hex string is invalid.

    Usage Example:
        >>> hex_to_text("48656c6c6f")
        'Hello'

    Complexity: O(n)
    """
    if not isinstance(hex_str, str):
        raise TypeError("hex_str must be a string")

    cleaned = hex_str.strip().replace(" ", "")

    try:
        return bytes.fromhex(cleaned).decode(encoding)
    except Exception as exc:
        raise ValueError(f"Invalid hex string: {exc}") from exc