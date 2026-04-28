"""
Excel-compatible text and data functions.

This module provides Excel's TEXT & DATA functions including:
- Text extraction: LEFT, RIGHT, MID
- Text concatenation: CONCATENATE, CONCAT, TEXTJOIN
- Text transformation: UPPER, LOWER, PROPER, TRIM
- Text search: FIND, SEARCH, LEN
- Text replacement: SUBSTITUTE, REPLACE
- Character operations: CHAR, CODE
- Text validation: EXACT
- Text repetition: REPT
- Text formatting: TEXT
- Type conversion: VALUE

All functions follow Excel's naming conventions and behavior.
"""

from typing import Optional, Union, Any, List

from agentfx.fxString.string_format import (
    fixed as _core_fixed,
    to_upper as _core_upper,
    to_lower as _core_lower,
    normalize_spaces as _core_trim,
    format_with_pattern as _core_format_with_pattern,
    format_as_currency as _core_format_as_currency,
)
from agentfx.fxString.string_operations import (
    left_substring as _core_left,
    right_substring as _core_right,
    substring as _core_mid,
    replace_by_position as _core_replace,
    substitute as _core_substitute,
    clean_nonprintable as _core_clean,
    repeat_string as _core_repeat_string,
    text_before as _core_text_before,
    text_after as _core_text_after,
    text_split as _core_text_split,
    regex_replace as _core_regex_replace,
)
from agentfx.fxString.string_regex import (
    regex_match as _core_regex_match,
    regex_extract as _core_regex_extract,
)
from agentfx.fxString.string_convertions import (
    char_from_code as _core_char,
    code_from_char as _core_code,
    parse_text_to_number as _core_parse_text_to_number,
    to_full_width as _core_to_full_width,
)


def CONCATENATE(*args: str) -> str:
    """
    Joins several text strings into one text string.

    **Description:**
    Concatenates multiple strings into a single text string. Similar to the & operator.
    CONCATENATE does not provide delimiters or ignore empty arguments.

    **Args:**
        *args: Text strings to be joined. Can accept multiple arguments.

    **Returns:**
        str: The concatenated text string.

    **Raises:**
        None: Converts all arguments to strings.

    **Usage Example:**
        >>> CONCATENATE("Hello", " ", "World")
        'Hello World'
        >>> CONCATENATE("Value: ", 100)
        'Value: 100'
        >>> CONCATENATE("A", "B", "C", "D")
        'ABCD'

    **Cost:** O(n), where n is the total length of all strings.
    """
    return "".join(str(arg) for arg in args)


def CONCAT(*args: str) -> str:
    """Combines text from multiple ranges and/or strings.

    Description:
        Alias for CONCATENATE. In Excel, CONCAT supports array ranges,
        but in this Python library both names refer to the same function
        since there are no Excel ranges.

    Args:
        *args: Text strings to be joined.

    Returns:
        str: The concatenated text string.

    Usage Example:
        >>> CONCAT("Sun", "flower")
        'Sunflower'
        >>> CONCAT("Zip code: ", 90210)
        'Zip code: 90210'

    Cost: O(n), where n is the total length of all strings.
    """
    return CONCATENATE(*args)


def TEXTJOIN(delimiter: str, ignore_empty: bool, *args: Any) -> str:
    """
    Combines text from multiple ranges with a delimiter.

    **Description:**
    Joins text strings using a delimiter and can optionally ignore empty strings.
    More powerful than CONCATENATE as it allows a delimiter between values.

    **Args:**
        delimiter: Text string to use as separator between values.
        ignore_empty: If True, ignores empty cells/strings.
        *args: Text values to join.

    **Returns:**
        str: The joined text string with delimiters.

    **Raises:**
        None: Converts all arguments to strings.

    **Usage Example:**
        >>> TEXTJOIN(", ", True, "Red", "", "Blue", "Green")
        'Red, Blue, Green'
        >>> TEXTJOIN("-", False, 2024, 1, 15)
        '2024-1-15'
        >>> TEXTJOIN(" ", True, "Hello", None, "World")
        'Hello World'

    **Cost:** O(n), where n is the total length of all strings and delimiter.
    """
    if ignore_empty:
        values = [str(arg) for arg in args if arg not in (None, "", [])]
    else:
        values = [str(arg) if arg is not None else "" for arg in args]
    
    return delimiter.join(values)


def LEFT(text: str, num_chars: int = 1) -> str:
    """
    Returns the leftmost characters from a text string.

    **Description:**
    Extracts a specified number of characters from the start of a text string.
    Similar to Excel's LEFT function.

    **Args:**
        text: Text string containing the characters to extract.
        num_chars: Number of characters to extract (default: 1).

    **Returns:**
        str: The leftmost characters from the text string.

    **Raises:**
        TypeError: If num_chars is not an integer.
        ValueError: If num_chars is negative.

    **Usage Example:**
        >>> LEFT("Sale Price", 4)
        'Sale'
        >>> LEFT("Sweden")
        'S'
        >>> LEFT("Quarterly Report", 9)
        'Quarterly'

    **Cost:** O(k), where k is num_chars.
    """
    if not isinstance(num_chars, int):
        raise TypeError("num_chars must be an integer")
    if num_chars < 0:
        raise ValueError("num_chars must be non-negative")
    
    return _core_left(str(text), num_chars)


def RIGHT(text: str, num_chars: int = 1) -> str:
    """
    Returns the rightmost characters from a text string.

    **Description:**
    Extracts a specified number of characters from the end of a text string.
    Similar to Excel's RIGHT function.

    **Args:**
        text: Text string containing the characters to extract.
        num_chars: Number of characters to extract (default: 1).

    **Returns:**
        str: The rightmost characters from the text string.

    **Raises:**
        TypeError: If num_chars is not an integer.
        ValueError: If num_chars is negative.

    **Usage Example:**
        >>> RIGHT("Sale Price", 5)
        'Price'
        >>> RIGHT("Stock Number")
        'r'
        >>> RIGHT("2024-Q1", 2)
        'Q1'

    **Cost:** O(k), where k is num_chars.
    """
    if not isinstance(num_chars, int):
        raise TypeError("num_chars must be an integer")
    if num_chars < 0:
        raise ValueError("num_chars must be non-negative")
    
    return _core_right(str(text), num_chars)


def MID(text: str, start_num: int, num_chars: int) -> str:
    """
    Returns characters from the middle of a text string.

    **Description:**
    Extracts a substring from a text string given a starting position and length.
    Uses 1-based indexing like Excel (first character is position 1).

    **Args:**
        text: Text string containing the characters to extract.
        start_num: Position of the first character (1-based indexing).
        num_chars: Number of characters to extract.

    **Returns:**
        str: The extracted substring.

    **Raises:**
        TypeError: If start_num or num_chars is not an integer.
        ValueError: If start_num is less than 1 or num_chars is negative.

    **Usage Example:**
        >>> MID("Fluid Flow", 1, 5)
        'Fluid'
        >>> MID("Fluid Flow", 7, 4)
        'Flow'
        >>> MID("Quarterly Report 2024", 11, 6)
        'Report'

    **Cost:** O(k), where k is num_chars.
    """
    if not isinstance(start_num, int) or not isinstance(num_chars, int):
        raise TypeError("start_num and num_chars must be integers")
    if start_num < 1:
        raise ValueError("start_num must be >= 1 (Excel uses 1-based indexing)")
    if num_chars < 0:
        raise ValueError("num_chars must be non-negative")
    
    return _core_mid(str(text), start_num, num_chars)


def LEN(text: str) -> int:
    """
    Returns the number of characters in a text string.

    **Description:**
    Counts the total number of characters including spaces.
    Similar to Excel's LEN function.

    **Args:**
        text: Text string whose length you want to find.

    **Returns:**
        int: The number of characters in the text.

    **Raises:**
        None: Converts input to string if needed.

    **Usage Example:**
        >>> LEN("Phoenix, AZ")
        11
        >>> LEN("")
        0
        >>> LEN("  spaces  ")
        10

    **Cost:** O(1) for most implementations, O(n) for Unicode grapheme counting.
    """
    return len(str(text))


def FIND(find_text: str, within_text: str, start_num: int = 1) -> int:
    """
    Finds one text string within another (case-sensitive).

    **Description:**
    Returns the starting position of find_text within within_text.
    FIND is case-sensitive and doesn't allow wildcard characters.
    Uses 1-based indexing like Excel.

    **Args:**
        find_text: The text you want to find.
        within_text: The text containing the text you want to find.
        start_num: The character position to start searching (default: 1).

    **Returns:**
        int: The position of the first character of find_text (1-based).

    **Raises:**
        ValueError: If find_text is not found or start_num is invalid.
        TypeError: If start_num is not an integer.

    **Usage Example:**
        >>> FIND("M", "Miriam McGovern")
        1
        >>> FIND("m", "Miriam McGovern")
        6
        >>> FIND("M", "Miriam McGovern", 3)
        8

    **Cost:** O(n*m), where n is length of within_text and m is length of find_text.
    """
    if not isinstance(start_num, int):
        raise TypeError("start_num must be an integer")
    if start_num < 1:
        raise ValueError("start_num must be >= 1")
    
    # Convert to 0-based indexing
    start_idx = start_num - 1
    
    # Find the position (0-based)
    position = str(within_text).find(str(find_text), start_idx)
    
    if position == -1:
        raise ValueError(f"'{find_text}' not found in '{within_text}'")
    
    # Convert to 1-based indexing
    return position + 1


def SEARCH(find_text: str, within_text: str, start_num: int = 1) -> int:
    """
    Finds one text string within another (case-insensitive).

    **Description:**
    Returns the starting position of find_text within within_text.
    SEARCH is case-insensitive and allows wildcard characters (? and *).
    Uses 1-based indexing like Excel.

    **Args:**
        find_text: The text you want to find (can use ? and * wildcards).
        within_text: The text containing the text you want to find.
        start_num: The character position to start searching (default: 1).

    **Returns:**
        int: The position of the first character of find_text (1-based).

    **Raises:**
        ValueError: If find_text is not found or start_num is invalid.
        TypeError: If start_num is not an integer.

    **Usage Example:**
        >>> SEARCH("e", "Statements", 6)
        7
        >>> SEARCH("margin", "Profit Margin")
        8
        >>> SEARCH("M", "miriam mcgovern")
        1

    **Cost:** O(n*m), where n is length of within_text and m is length of find_text.
    """
    if not isinstance(start_num, int):
        raise TypeError("start_num must be an integer")
    if start_num < 1:
        raise ValueError("start_num must be >= 1")
    
    # Convert to 0-based indexing
    start_idx = start_num - 1
    
    # Convert to lowercase for case-insensitive search
    find_lower = str(find_text).lower()
    within_lower = str(within_text).lower()
    
    # Find the position (0-based)
    position = within_lower.find(find_lower, start_idx)
    
    if position == -1:
        raise ValueError(f"'{find_text}' not found in '{within_text}'")
    
    # Convert to 1-based indexing
    return position + 1


def SUBSTITUTE(text: str, old_text: str, new_text: str, instance_num: Optional[int] = None) -> str:
    """
    Substitutes new text for old text in a text string.

    **Description:**
    Replaces existing text with new text in a string. If instance_num is specified,
    only that occurrence is replaced; otherwise all occurrences are replaced.

    **Args:**
        text: The text in which you want to substitute characters.
        old_text: The text you want to replace.
        new_text: The text you want to replace old_text with.
        instance_num: Which occurrence to replace (optional, default: all).

    **Returns:**
        str: The text with substitutions made.

    **Raises:**
        TypeError: If instance_num is not an integer.
        ValueError: If instance_num is less than 1.

    **Usage Example:**
        >>> SUBSTITUTE("Sales Data", "Sales", "Cost")
        'Cost Data'
        >>> SUBSTITUTE("Quarter 1, 2023", "1", "2", 1)
        'Quarter 2, 2023'
        >>> SUBSTITUTE("apple apple", "apple", "orange")
        'orange orange'

    **Cost:** O(n), where n is the length of the text.
    """
    return _core_substitute(text, old_text, new_text, instance_num if instance_num is not None else 0)


def REPLACE(old_text: str, start_num: int, num_chars: int, new_text: str) -> str:
    """
    Replaces part of a text string with a different text string.

    **Description:**
    Replaces a specified number of characters at a specific position.
    Uses 1-based indexing like Excel.

    **Args:**
        old_text: Text in which you want to replace characters.
        start_num: Position of the first character to replace (1-based).
        num_chars: Number of characters to replace.
        new_text: Text that will replace characters in old_text.

    **Returns:**
        str: The text with replacements made.

    **Raises:**
        TypeError: If start_num or num_chars is not an integer.
        ValueError: If start_num is less than 1 or num_chars is negative.

    **Usage Example:**
        >>> REPLACE("abcdefghijk", 6, 5, "*")
        'abcde*k'
        >>> REPLACE("2024", 3, 2, "25")
        '2025'
        >>> REPLACE("XYZ123", 4, 3, "456")
        'XYZ456'

    **Cost:** O(n), where n is the length of old_text.
    """
    if not isinstance(start_num, int) or not isinstance(num_chars, int):
        raise TypeError("start_num and num_chars must be integers")
    if start_num < 1:
        raise ValueError("start_num must be >= 1")
    if num_chars < 0:
        raise ValueError("num_chars must be non-negative")
    
    return _core_replace(str(old_text), start_num, num_chars, str(new_text))


def UPPER(text: str) -> str:
    """
    Converts text to uppercase.

    **Description:**
    Converts all lowercase letters in a text string to uppercase.
    Numbers and punctuation are not affected.

    **Args:**
        text: The text you want to convert to uppercase.

    **Returns:**
        str: The text converted to uppercase.

    **Raises:**
        None: Converts input to string if needed.

    **Usage Example:**
        >>> UPPER("total")
        'TOTAL'
        >>> UPPER("E. E. Cummings")
        'E. E. CUMMINGS'
        >>> UPPER("Yield-12%")
        'YIELD-12%'

    **Cost:** O(n), where n is the length of the text.
    """
    return _core_upper(str(text))


def LOWER(text: str) -> str:
    """
    Converts text to lowercase.

    **Description:**
    Converts all uppercase letters in a text string to lowercase.
    Numbers and punctuation are not affected.

    **Args:**
        text: The text you want to convert to lowercase.

    **Returns:**
        str: The text converted to lowercase.

    **Raises:**
        None: Converts input to string if needed.

    **Usage Example:**
        >>> LOWER("E. E. Cummings")
        'e. e. cummings'
        >>> LOWER("PAID IN FULL")
        'paid in full'
        >>> LOWER("ABC-123")
        'abc-123'

    **Cost:** O(n), where n is the length of the text.
    """
    return _core_lower(str(text))


def PROPER(text: str) -> str:
    """
    Capitalizes the first letter in each word of a text string.

    **Description:**
    Converts a text string to proper case: the first letter in each word
    is uppercase, and all other letters are lowercase.

    **Args:**
        text: Text to convert to proper case.

    **Returns:**
        str: The text in proper case.

    **Raises:**
        None: Converts input to string if needed.

    **Usage Example:**
        >>> PROPER("this is a TITLE")
        'This Is A Title'
        >>> PROPER("2-way street")
        '2-Way Street'
        >>> PROPER("76BudGet")
        '76Budget'

    **Cost:** O(n), where n is the length of the text.
    """
    return str(text).title()


def TRIM(text: str) -> str:
    """
    Removes all spaces from text except single spaces between words.

    **Description:**
    Removes leading and trailing spaces, and reduces multiple spaces
    between words to a single space.

    **Args:**
        text: The text from which you want spaces removed.

    **Returns:**
        str: The text with extra spaces removed.

    **Raises:**
        None: Converts input to string if needed.

    **Usage Example:**
        >>> TRIM("  First Quarter   Earnings  ")
        'First Quarter Earnings'
        >>> TRIM("Hello     World")
        'Hello World'
        >>> TRIM("   text   ")
        'text'

    **Cost:** O(n), where n is the length of the text.
    """
    return _core_trim(str(text))


def CLEAN(text: str) -> str:
    """
    Removes all nonprintable characters from text.

    **Description:**
    Removes characters with ASCII values 0-31 (nonprintable characters).
    Useful for cleaning text imported from other applications.

    **Args:**
        text: Text from which you want to remove nonprintable characters.

    **Returns:**
        str: The cleaned text.

    **Raises:**
        None: Converts input to string if needed.

    **Usage Example:**
        >>> CLEAN("Monthly Report\\n\\r\\t2024")
        'Monthly Report2024'
        >>> CLEAN("Hello\\x00World")
        'HelloWorld'

    **Cost:** O(n), where n is the length of the text.
    """
    return _core_clean(text)


def CHAR(number: int) -> str:
    """
    Returns the character specified by the code number.

    **Description:**
    Converts a number into a character according to the Unicode character set.
    Similar to Excel's CHAR function.

    **Args:**
        number: A number between 1 and 1114111 (Unicode code point).

    **Returns:**
        str: The character corresponding to the code number.

    **Raises:**
        TypeError: If number is not an integer.
        ValueError: If number is outside the valid range.

    **Usage Example:**
        >>> CHAR(65)
        'A'
        >>> CHAR(97)
        'a'
        >>> CHAR(33)
        '!'

    **Cost:** O(1), constant time operation.
    """
    if not isinstance(number, int):
        raise TypeError("number must be an integer")
    if number < 1 or number > 1114111:
        raise ValueError("number must be between 1 and 1114111")
    
    return _core_char(number)


def CODE(text: str) -> int:
    """
    Returns a numeric code for the first character in a text string.

    **Description:**
    Returns the Unicode code point value of the first character.
    Similar to Excel's CODE function.

    **Args:**
        text: The text for which you want the code of the first character.

    **Returns:**
        int: The numeric code for the first character.

    **Raises:**
        ValueError: If the text string is empty.

    **Usage Example:**
        >>> CODE("A")
        65
        >>> CODE("Apple")
        65
        >>> CODE("!")
        33

    **Cost:** O(1), constant time operation.
    """
    text_str = str(text)
    if not text_str:
        raise ValueError("Text cannot be empty")
    
    return _core_code(text_str[0])


def EXACT(text1: str, text2: str) -> bool:
    """
    Checks whether two text strings are exactly the same.

    **Description:**
    Compares two text strings and returns True if they are exactly the same
    (case-sensitive), False otherwise.

    **Args:**
        text1: The first text string.
        text2: The second text string.

    **Returns:**
        bool: True if the strings are identical, False otherwise.

    **Raises:**
        None: Converts inputs to strings if needed.

    **Usage Example:**
        >>> EXACT("Word", "word")
        False
        >>> EXACT("Word", "Word")
        True
        >>> EXACT("abc", "abc")
        True

    **Cost:** O(n), where n is the length of the strings.
    """
    return str(text1) == str(text2)


def REPT(text: str, number_times: int) -> str:
    """
    Repeats text a given number of times.

    **Description:**
    Returns text repeated a specified number of times.
    Use REPT to fill a cell with a number of instances of a text string.

    **Args:**
        text: The text you want to repeat.
        number_times: A positive number specifying the number of times to repeat.

    **Returns:**
        str: The repeated text.

    **Raises:**
        TypeError: If number_times is not an integer.
        ValueError: If number_times is negative.

    **Usage Example:**
        >>> REPT("*-", 3)
        '*-*-*-'
        >>> REPT("=", 5)
        '====='
        >>> REPT("AB", 2)
        'ABAB'

    **Cost:** O(n*m), where n is the length of text and m is number_times.
    """
    return _core_repeat_string(str(text), number_times)


def TEXT(value: Union[int, float, str], format_text: str) -> str:
    """
    Formats a number and converts it to text.

    **Description:**
    Converts a value to text in a specified number format.
    Simplified version supporting basic formats.

    **Args:**
        value: A numeric value to format.
        format_text: A number format as a text string (e.g., "0.00", "#,##0").

    **Returns:**
        str: The formatted text.

    **Raises:**
        None: Returns basic string conversion for unsupported formats.

    **Usage Example:**
        >>> TEXT(1234.567, "0.00")
        '1234.57'
        >>> TEXT(0.285, "0.0%")
        '28.5%'
        >>> TEXT(1234, "#,##0")
        '1,234'

    **Cost:** O(n), where n is the length of the formatted output.

    **Note:** This is a simplified implementation. Full Excel TEXT function
    supports complex formatting codes.
    """
    return _core_format_with_pattern(value, format_text)


def VALUE(text: str) -> Union[int, float]:
    """
    Converts text that represents a number to a number.

    **Description:**
    Converts a text string that represents a number to a numeric value.
    Handles integers, floats, percentages, and basic formatting.

    **Args:**
        text: The text to convert to a number.

    **Returns:**
        Union[int, float]: The numeric value.

    **Raises:**
        ValueError: If the text cannot be converted to a number.

    **Usage Example:**
        >>> VALUE("$1,000")
        1000.0
        >>> VALUE("16:48:00")
        0.7
        >>> VALUE("123.45")
        123.45

    **Cost:** O(n), where n is the length of the text.

    **Note:** This is a simplified implementation. Full Excel VALUE function
    handles dates, times, and regional formats.
    """
    return _core_parse_text_to_number(text)


def UNICHAR(number: int) -> str:
    """
    Returns the Unicode character referenced by the given numeric value.
    Excel/Spanish name: UNICAR

    **Description:**
    Returns the Unicode character that corresponds to the numeric value.
    Supports the full Unicode range.

    **Args:**
        number: A number between 1 and 1114111 representing a Unicode code point.

    **Returns:**
        str: The Unicode character.

    **Raises:**
        ValueError: If number is outside the valid range.

    **Usage Example:**
        >>> UNICHAR(65)
        'A'
        >>> UNICHAR(8364)
        '€'
        >>> UNICHAR(128512)
        '😀'

    **Cost:** O(1)
    """
    if not (1 <= number <= 1114111):
        raise ValueError(f"Number must be between 1 and 1114111, got {number}")
    
    return _core_char(number)


def UNICODE(text: str) -> int:
    """
    Returns the number (code point) corresponding to the first character of the text.
    Excel/Spanish name: UNICODE

    **Description:**
    Returns the numeric Unicode code point of the first character in a text string.

    **Args:**
        text: The text whose first character's code point you want.

    **Returns:**
        int: The Unicode code point of the first character.

    **Raises:**
        ValueError: If text is empty.

    **Usage Example:**
        >>> UNICODE("A")
        65
        >>> UNICODE("€")
        8364
        >>> UNICODE("😀")
        128512

    **Cost:** O(1)
    """
    if not text:
        raise ValueError("Text cannot be empty")
    
    return _core_code(text[0])


def DOLLAR(number: Union[int, float], decimals: int = 2) -> str:
    """
    Converts a number to text using currency format ($).
    Excel/Spanish name: MONEDA

    **Description:**
    Formats a number as currency text with the dollar sign and specified decimal places.

    **Args:**
        number: The number to format.
        decimals: Number of decimal places (default: 2). Can be negative to round.

    **Returns:**
        str: The formatted currency string.

    **Raises:**
        None

    **Usage Example:**
        >>> DOLLAR(1234.567)
        '$1,234.57'
        >>> DOLLAR(1234.567, 1)
        '$1,234.6'
        >>> DOLLAR(-1234.567, 0)
        '($1,235)'

    **Cost:** O(log n), where n is the magnitude of the number.
    """
    result = _core_format_as_currency(number, decimals)

    if number < 0:
        return f"(${result.lstrip('-$')})"

    return result


def BAHTTEXT(number: Union[int, float]) -> str:
    """
    Converts a number to text using Thai Baht currency format.
    Excel/Spanish name: TEXTOBAHT

    **Description:**
    Converts a number to Thai text in the Baht currency format.
    This is a simplified implementation that returns a formatted string.

    **Args:**
        number: The number to convert.

    **Returns:**
        str: The number formatted as Baht text.

    **Raises:**
        None

    **Usage Example:**
        >>> BAHTTEXT(1234)
        '฿1,234.00'
        >>> BAHTTEXT(5678.50)
        '฿5,678.50'

    **Cost:** O(log n), where n is the magnitude of the number.

    **Note:** Full Thai text conversion would require Thai language number names.
    This implementation provides the numeric format with Baht symbol.
    """
    formatted = f"{abs(number):,.2f}"
    if number < 0:
        return f"-฿{formatted}"
    return f"฿{formatted}"


def FIXED(number: Union[int, float], decimals: int = 2, no_commas: bool = False) -> str:
    """
    Formats a number as text with a fixed number of decimals.
    Excel/Spanish name: CORREGIDO

    **Description:**
    Rounds a number to the specified number of decimals and returns it as text.
    Optionally includes thousands separators.

    **Args:**
        number: The number to format.
        decimals: Number of decimal places (default: 2).
        no_commas: If True, omits thousands separators (default: False).

    **Returns:**
        str: The formatted number as text.

    **Raises:**
        None

    **Usage Example:**
        >>> FIXED(1234.567)
        '1,234.57'
        >>> FIXED(1234.567, 1)
        '1,234.6'
        >>> FIXED(1234.567, 1, True)
        '1234.6'

    **Cost:** O(log n), where n is the magnitude of the number.
    """
    return _core_fixed(number, decimals, no_commas)


def T(value: Any) -> str:
    """
    Converts its argument to text.
    Excel/Spanish name: T

    **Description:**
    Returns the text if the value is text; otherwise returns empty string.
    Used to test whether a value is text.

    **Args:**
        value: The value to check.

    **Returns:**
        str: The text value if value is text, otherwise empty string.

    **Raises:**
        None

    **Usage Example:**
        >>> T("Hello")
        'Hello'
        >>> T(123)
        ''
        >>> T(True)
        ''

    **Cost:** O(1)
    """
    if isinstance(value, str):
        return value
    return ""


def NUMBERVALUE(text: str, decimal_separator: str = ".", group_separator: str = ",") -> float:
    """
    Converts text to number in a locale-independent manner.
    Excel/Spanish name: VALOR.NUMERO

    **Description:**
    Converts text to a number using specified decimal and group separators.
    Useful for converting numbers with different regional formats.

    **Args:**
        text: The text to convert.
        decimal_separator: The character used as decimal separator (default: ".").
        group_separator: The character used for thousands separator (default: ",").

    **Returns:**
        float: The converted number.

    **Raises:**
        ValueError: If the text cannot be converted.

    **Usage Example:**
        >>> NUMBERVALUE("1,234.56")
        1234.56
        >>> NUMBERVALUE("1.234,56", ",", ".")
        1234.56
        >>> NUMBERVALUE("3.5%")
        0.035

    **Cost:** O(n), where n is the length of the text.
    """
    return _core_parse_text_to_number(text, decimal_separator, group_separator)


def TEXTAFTER(text: str, delimiter: str, instance_num: int = 1, 
              match_mode: int = 0, match_end: int = 0, if_not_found: Any = None) -> str:
    """
    Returns text that occurs after a given character or substring.
    Excel/Spanish name: TEXTODESPUES

    **Description:**
    Extracts text that appears after a specified delimiter.
    Supports multiple instances and case-sensitive/insensitive matching.

    **Args:**
        text: The text to search.
        delimiter: The delimiter text.
        instance_num: Which instance of delimiter to use (default: 1, negative counts from end).
        match_mode: 0 = case-sensitive (default), 1 = case-insensitive.
        match_end: 0 = if not found return error (default), 1 = return text from end.
        if_not_found: Value to return if delimiter not found.

    **Returns:**
        str: The text after the delimiter.

    **Raises:**
        ValueError: If delimiter not found and if_not_found is None.

    **Usage Example:**
        >>> TEXTAFTER("Red-Blue-Green", "-")
        'Blue-Green'
        >>> TEXTAFTER("Red-Blue-Green", "-", 2)
        'Green'
        >>> TEXTAFTER("Red-Blue-Green", "-", -1)
        'Green'

    **Cost:** O(n), where n is the length of the text.
    """
    if match_mode == 0 and match_end == 0 and if_not_found is None:
        return _core_text_after(text, delimiter, instance_num)

    if match_end == 1 and delimiter not in text:
        return text
    
    search_text = text if match_mode == 0 else text.lower()
    search_delim = delimiter if match_mode == 0 else delimiter.lower()
    
    if instance_num > 0:
        pos = -1

        for _ in range(instance_num):
            pos = search_text.find(search_delim, pos + 1)

            if pos == -1:

                if if_not_found is not None:
                    return str(if_not_found)

                raise ValueError(f"Delimiter '{delimiter}' not found")

        return text[pos + len(delimiter):]
    else:
        pos = len(text)

        for _ in range(abs(instance_num)):
            pos = search_text.rfind(search_delim, 0, pos)

            if pos == -1:

                if if_not_found is not None:
                    return str(if_not_found)

                raise ValueError(f"Delimiter '{delimiter}' not found")

        return text[pos + len(delimiter):]


def TEXTBEFORE(text: str, delimiter: str, instance_num: int = 1,
               match_mode: int = 0, match_end: int = 0, if_not_found: Any = None) -> str:
    """
    Returns text that occurs before a given character or substring.
    Excel/Spanish name: TEXTOANTES

    **Description:**
    Extracts text that appears before a specified delimiter.
    Supports multiple instances and case-sensitive/insensitive matching.

    **Args:**
        text: The text to search.
        delimiter: The delimiter text.
        instance_num: Which instance of delimiter to use (default: 1, negative counts from end).
        match_mode: 0 = case-sensitive (default), 1 = case-insensitive.
        match_end: 0 = if not found return error (default), 1 = return text from start.
        if_not_found: Value to return if delimiter not found.

    **Returns:**
        str: The text before the delimiter.

    **Raises:**
        ValueError: If delimiter not found and if_not_found is None.

    **Usage Example:**
        >>> TEXTBEFORE("Red-Blue-Green", "-")
        'Red'
        >>> TEXTBEFORE("Red-Blue-Green", "-", 2)
        'Red-Blue'
        >>> TEXTBEFORE("Red-Blue-Green", "-", -1)
        'Red-Blue'

    **Cost:** O(n), where n is the length of the text.
    """
    if match_mode == 0 and match_end == 0 and if_not_found is None:
        return _core_text_before(text, delimiter, instance_num)

    if match_end == 1 and delimiter not in text:
        return text
    
    search_text = text if match_mode == 0 else text.lower()
    search_delim = delimiter if match_mode == 0 else delimiter.lower()
    
    if instance_num > 0:
        pos = -1

        for _ in range(instance_num):
            pos = search_text.find(search_delim, pos + 1)

            if pos == -1:

                if if_not_found is not None:
                    return str(if_not_found)

                raise ValueError(f"Delimiter '{delimiter}' not found")

        return text[:pos]
    else:
        pos = len(text)

        for _ in range(abs(instance_num)):
            pos = search_text.rfind(search_delim, 0, pos)

            if pos == -1:

                if if_not_found is not None:
                    return str(if_not_found)

                raise ValueError(f"Delimiter '{delimiter}' not found")

        return text[:pos]


def TEXTSPLIT(text: str, col_delimiter: str = " ", row_delimiter: str = None,
              ignore_empty: bool = False, match_mode: int = 0, pad_with: Any = None) -> List[List[str]]:
    """
    Splits text into rows and columns using delimiters.
    Excel/Spanish name: DIVIDIRTEXTO

    **Description:**
    Splits text strings using column and row delimiters.
    Returns a 2D array (list of lists).

    **Args:**
        text: The text to split.
        col_delimiter: The delimiter for columns (default: space).
        row_delimiter: The delimiter for rows (optional).
        ignore_empty: If True, ignores empty cells (default: False).
        match_mode: 0 = case-sensitive (default), 1 = case-insensitive.
        pad_with: Value to use for padding (default: None).

    **Returns:**
        List[List[str]]: 2D array of split text.

    **Raises:**
        None

    **Usage Example:**
        >>> TEXTSPLIT("Red Blue Green")
        [['Red', 'Blue', 'Green']]
        >>> TEXTSPLIT("A,B,C;D,E,F", ",", ";")
        [['A', 'B', 'C'], ['D', 'E', 'F']]
        >>> TEXTSPLIT("A,,C", ",", ignore_empty=True)
        [['A', 'C']]

    **Cost:** O(n), where n is the length of the text.
    """
    if not ignore_empty and match_mode == 0 and pad_with is None:
        result = _core_text_split(text, col_delimiter=col_delimiter, row_delimiter=row_delimiter)

        if isinstance(result[0], list):
            return result

        return [result]

    # Full Excel behavior with ignore_empty, match_mode, pad_with
    if row_delimiter:
        rows = text.split(row_delimiter)
    else:
        rows = [text]
    
    result = []

    for row in rows:

        if col_delimiter:
            cols = row.split(col_delimiter)
        else:
            cols = [row]

        if ignore_empty:
            cols = [c for c in cols if c]

        result.append(cols)

    if pad_with is not None:
        max_cols = max(len(row) for row in result) if result else 0

        for row in result:

            while len(row) < max_cols:
                row.append(pad_with)

    return result


def VALUETOTEXT(value: Any, format_type: int = 0) -> str:
    """
    Returns text from any specified value.
    Excel/Spanish name: VALORATEXTO

    **Description:**
    Converts any value to text with optional concise formatting.

    **Args:**
        value: The value to convert to text.
        format_type: 0 = normal (default), 1 = concise format.

    **Returns:**
        str: The text representation of the value.

    **Raises:**
        None

    **Usage Example:**
        >>> VALUETOTEXT("Hello")
        'Hello'
        >>> VALUETOTEXT(123)
        '123'
        >>> VALUETOTEXT([1, 2, 3])
        '[1, 2, 3]'

    **Cost:** O(n), where n is the size of the value.
    """
    if format_type == 1:
        # Concise format (no extra spaces)
        if isinstance(value, (list, tuple)):
            return str(value).replace(" ", "")
        return str(value).strip()
    else:
        # Normal format
        return str(value)


def ARRAYTOTEXT(
    array: Any,
    format_type: int = 0,
) -> str:
    """Returns a text representation of an array of values.

    Excel function: ARRAYTOTEXT

    Args:
        array: A list, list of lists, or tuple to convert.
        format_type: 0 = concise with comma/semicolon, 1 = strict with braces
                     and quoted strings.

    Returns:
        str: Text representation of the array.

    Usage Example:
        >>> ARRAYTOTEXT([1, "hello", True])
        '1, hello, True'
        >>> ARRAYTOTEXT([1, "hello", True], 1)
        '{1,"hello",TRUE}'
        >>> ARRAYTOTEXT([[1, 2], [3, 4]], 1)
        '{1,2;3,4}'

    Cost: O(n)
    """
    if not isinstance(array, (list, tuple)):
        return str(array)

    is_2d = any(isinstance(row, (list, tuple)) for row in array)

    if format_type == 1:

        def _fmt(v: Any) -> str:
            if isinstance(v, bool):
                return "TRUE" if v else "FALSE"

            if isinstance(v, str):
                return f'"{v}"'

            return str(v)

        if is_2d:
            rows = [",".join(_fmt(c) for c in row) if isinstance(row, (list, tuple))
                    else _fmt(row) for row in array]
            return "{" + ";".join(rows) + "}"

        return "{" + ",".join(_fmt(v) for v in array) + "}"

    # format_type 0 — concise
    if is_2d:
        rows = [", ".join(str(c) for c in row) if isinstance(row, (list, tuple))
                else str(row) for row in array]
        return "; ".join(rows)

    return ", ".join(str(v) for v in array)


# Byte-specific variants (for double-byte character sets like Japanese)
def LEFTB(text: str, num_bytes: int = 1) -> str:
    """
    Returns the leftmost characters based on number of bytes.
    Excel/Spanish name: IZQUIERDAB

    **Description:**
    Similar to LEFT but counts bytes instead of characters.
    Useful for double-byte character sets (DBCS).

    **Args:**
        text: The text string.
        num_bytes: Number of bytes to extract (default: 1).

    **Returns:**
        str: The leftmost characters up to num_bytes.

    **Raises:**
        None

    **Usage Example:**
        >>> LEFTB("Hello", 3)
        'Hel'
        >>> LEFTB("日本語", 6)
        '日本'

    **Cost:** O(n), where n is num_bytes.
    """
    encoded = text.encode('utf-8')
    return encoded[:num_bytes].decode('utf-8', errors='ignore')


def RIGHTB(text: str, num_bytes: int = 1) -> str:
    """
    Returns the rightmost characters based on number of bytes.
    Excel/Spanish name: DERECHAB

    **Description:**
    Similar to RIGHT but counts bytes instead of characters.
    Useful for double-byte character sets (DBCS).

    **Args:**
        text: The text string.
        num_bytes: Number of bytes to extract (default: 1).

    **Returns:**
        str: The rightmost characters up to num_bytes.

    **Raises:**
        None

    **Usage Example:**
        >>> RIGHTB("Hello", 2)
        'lo'
        >>> RIGHTB("日本語", 6)
        '本語'

    **Cost:** O(n), where n is num_bytes.
    """
    encoded = text.encode('utf-8')
    return encoded[-num_bytes:].decode('utf-8', errors='ignore')


def MIDB(text: str, start_byte: int, num_bytes: int) -> str:
    """
    Returns characters from the middle based on bytes.
    Excel/Spanish name: EXTRAEB

    **Description:**
    Similar to MID but uses byte positions and counts.
    Useful for double-byte character sets (DBCS).

    **Args:**
        text: The text string.
        start_byte: Starting byte position (1-based).
        num_bytes: Number of bytes to extract.

    **Returns:**
        str: The extracted substring.

    **Raises:**
        None

    **Usage Example:**
        >>> MIDB("Hello World", 7, 5)
        'World'

    **Cost:** O(n), where n is num_bytes.
    """
    encoded = text.encode('utf-8')
    start_idx = start_byte - 1  # Convert to 0-based
    return encoded[start_idx:start_idx + num_bytes].decode('utf-8', errors='ignore')


def LENB(text: str) -> int:
    """
    Returns the number of bytes in text.
    Excel/Spanish name: LARGOB

    **Description:**
    Returns the number of bytes used to represent the text in UTF-8 encoding.

    **Args:**
        text: The text string.

    **Returns:**
        int: The number of bytes.

    **Raises:**
        None

    **Usage Example:**
        >>> LENB("Hello")
        5
        >>> LENB("日本語")
        9

    **Cost:** O(n), where n is the length of the text.
    """
    return len(text.encode('utf-8'))


def FINDB(find_bytes: str, within_text: str, start_byte: int = 1) -> int:
    """
    Finds one text value within another based on bytes (case-sensitive).
    Excel/Spanish name: ENCONTRARB

    **Description:**
    Similar to FIND but works with byte positions.

    **Args:**
        find_bytes: The bytes to find.
        within_text: The text to search within.
        start_byte: Starting byte position (1-based, default: 1).

    **Returns:**
        int: The byte position of the found text (1-based).

    **Raises:**
        ValueError: If find_bytes is not found.

    **Usage Example:**
        >>> FINDB("World", "Hello World")
        7

    **Cost:** O(n), where n is the length of within_text.
    """
    encoded = within_text.encode('utf-8')
    find_enc = find_bytes.encode('utf-8')
    start_idx = start_byte - 1
    
    pos = encoded.find(find_enc, start_idx)
    if pos == -1:
        raise ValueError(f"'{find_bytes}' not found")
    
    return pos + 1


def SEARCHB(find_bytes: str, within_text: str, start_byte: int = 1) -> int:
    """
    Finds one text value within another based on bytes (case-insensitive).
    Excel/Spanish name: SEARB

    **Description:**
    Similar to SEARCH but works with byte positions.

    **Args:**
        find_bytes: The bytes to find.
        within_text: The text to search within.
        start_byte: Starting byte position (1-based, default: 1).

    **Returns:**
        int: The byte position of the found text (1-based).

    **Raises:**
        ValueError: If find_bytes is not found.

    **Usage Example:**
        >>> SEARCHB("world", "Hello World")
        7

    **Cost:** O(n), where n is the length of within_text.
    """
    encoded = within_text.lower().encode('utf-8')
    find_enc = find_bytes.lower().encode('utf-8')
    start_idx = start_byte - 1
    
    pos = encoded.find(find_enc, start_idx)
    if pos == -1:
        raise ValueError(f"'{find_bytes}' not found")
    
    return pos + 1


def REPLACEB(old_text: str, start_byte: int, num_bytes: int, new_text: str) -> str:
    """
    Replaces part of a text string based on bytes.
    Excel/Spanish name: REEMPLAZARB

    **Description:**
    Similar to REPLACE but uses byte positions and counts.

    **Args:**
        old_text: The text to modify.
        start_byte: Starting byte position (1-based).
        num_bytes: Number of bytes to replace.
        new_text: The replacement text.

    **Returns:**
        str: The modified text.

    **Raises:**
        None

    **Usage Example:**
        >>> REPLACEB("Hello World", 7, 5, "Python")
        'Hello Python'

    **Cost:** O(n), where n is the length of the text.
    """
    encoded = old_text.encode('utf-8')
    start_idx = start_byte - 1
    
    before = encoded[:start_idx].decode('utf-8', errors='ignore')
    after = encoded[start_idx + num_bytes:].decode('utf-8', errors='ignore')
    
    return before + new_text + after


def ASC(text: str) -> str:
    """
    Converts full-width (double-byte) characters to half-width (single-byte).
    Excel/Spanish name: ASC

    **Description:**
    Converts full-width English letters and katakana to half-width characters.
    Primarily used for Japanese text.

    **Args:**
        text: The text containing full-width characters.

    **Returns:**
        str: Text with full-width characters converted to half-width.

    **Raises:**
        None

    **Usage Example:**
        >>> ASC("ＨＥＬＬＯ")
        'HELLO'
        >>> ASC("１２３")
        '123'

    **Cost:** O(n), where n is the length of the text.

    **Note:** This is a simplified implementation focusing on common full-width characters.
    """
    result = []
    for char in text:
        code = ord(char)
        # Convert full-width ASCII (0xFF01-0xFF5E) to half-width (0x21-0x7E)
        if 0xFF01 <= code <= 0xFF5E:
            result.append(chr(code - 0xFEE0))
        # Convert full-width space (0x3000) to half-width (0x20)
        elif code == 0x3000:
            result.append(' ')
        else:
            result.append(char)
    
    return ''.join(result)


# Regex functions (Microsoft 365+)


def REGEXTEST(text: str, pattern: str, match_mode: int = 0) -> bool:
    """
    Tests whether any part of the text matches the regex pattern.
    Excel/Spanish name: REGEXPRUEBA

    **Description:**
    Determines if any part of the text matches the specified regular expression pattern.

    **Args:**
        text: The text to test.
        pattern: The regular expression pattern.
        match_mode: 0 = case-sensitive (default), 1 = case-insensitive.

    **Returns:**
        bool: True if pattern is found, False otherwise.

    **Raises:**
        re.error: If pattern is invalid.

    **Usage Example:**
        >>> REGEXTEST("Hello123", r"\\d+")
        True
        >>> REGEXTEST("NoNumbers", r"\\d+")
        False
        >>> REGEXTEST("hello", r"^HELLO$", 1)
        True

    **Cost:** O(n*m), where n is text length and m is pattern complexity.
    """
    return _core_regex_match(text, pattern, case_sensitive=(match_mode == 0))


def REGEXEXTRACT(text: str, pattern: str, match_mode: int = 0, capture_group: int = 0) -> Union[str, List[str]]:
    """
    Extracts strings within text that match the regex pattern.
    Excel/Spanish name: REGEXEXTRACCION

    **Description:**
    Extracts substrings from text that match the specified regular expression pattern.

    **Args:**
        text: The text to search.
        pattern: The regular expression pattern.
        match_mode: 0 = case-sensitive (default), 1 = case-insensitive.
        capture_group: Which capture group to return (0 = entire match).

    **Returns:**
        Union[str, List[str]]: The matched text or list of matches.

    **Raises:**
        ValueError: If pattern is not found.
        re.error: If pattern is invalid.

    **Usage Example:**
        >>> REGEXEXTRACT("Price: $123.45", r"\\$([0-9.]+)")
        '$123.45'
        >>> REGEXEXTRACT("Price: $123.45", r"\\$([0-9.]+)", capture_group=1)
        '123.45'

    **Cost:** O(n*m), where n is text length and m is pattern complexity.
    """
    result = _core_regex_extract(
        text, pattern, group=capture_group,
        case_sensitive=(match_mode == 0),
    )

    if result is None:
        raise ValueError(f"Pattern '{pattern}' not found in text")

    return result


def REGEXREPLACE(text: str, pattern: str, replacement: str, match_mode: int = 0) -> str:
    """
    Replaces strings within text that match the regex pattern with replacement.
    Excel/Spanish name: REGEXREEMPLAZAR

    **Description:**
    Replaces all occurrences of text matching the regular expression pattern
    with the specified replacement string.

    **Args:**
        text: The text to modify.
        pattern: The regular expression pattern to match.
        replacement: The replacement string.
        match_mode: 0 = case-sensitive (default), 1 = case-insensitive.

    **Returns:**
        str: The text with replacements made.

    **Raises:**
        re.error: If pattern is invalid.

    **Usage Example:**
        >>> REGEXREPLACE("Hello 123 World 456", r"\\d+", "X")
        'Hello X World X'
        >>> REGEXREPLACE("test@email.com", r"@.*", "@example.com")
        'test@example.com'

    **Cost:** O(n*m), where n is text length and m is pattern complexity.
    """
    return _core_regex_replace(
        text, pattern, replacement,
        case_insensitive=(match_mode == 1),
    )


def DBCS(text: str) -> str:
    """
    Converts half-width (single-byte) characters to full-width (double-byte).
    Excel/Spanish name: DBCS

    **Description:**
    Converts half-width English letters, katakana, and numbers to full-width characters.
    Primarily used for Japanese text. This is the opposite of ASC function.

    **Args:**
        text: The text containing half-width characters.

    **Returns:**
        str: Text with half-width characters converted to full-width.

    **Raises:**
        None

    **Usage Example:**
        >>> DBCS("HELLO")
        'ＨＥＬＬＯ'
        >>> DBCS("123")
        '１２３'

    **Cost:** O(n), where n is the length of the text.

    **Note:** This is a simplified implementation focusing on common half-width characters.
    """
    return _core_to_full_width(text)


# Export all functions
__all__ = [
    # Basic text operations
    'CONCATENATE', 'CONCAT', 'TEXTJOIN',
    'LEFT', 'RIGHT', 'MID',
    'LEN', 'FIND', 'SEARCH',
    'SUBSTITUTE', 'REPLACE',
    'UPPER', 'LOWER', 'PROPER', 'TRIM', 'CLEAN',
    'CHAR', 'CODE',
    'EXACT', 'REPT',
    'TEXT', 'VALUE',
    
    # Unicode and international
    'UNICHAR', 'UNICODE',
    
    # Formatting
    'DOLLAR', 'BAHTTEXT', 'FIXED', 'T',
    
    # Conversion
    'NUMBERVALUE', 'VALUETOTEXT', 'ARRAYTOTEXT',
    
    # Text extraction
    'TEXTAFTER', 'TEXTBEFORE', 'TEXTSPLIT',
    
    # Byte-based operations (DBCS)
    'LEFTB', 'RIGHTB', 'MIDB', 'LENB',
    'FINDB', 'SEARCHB', 'REPLACEB', 'ASC', 'DBCS',
    
    # Regex operations
    'REGEXTEST', 'REGEXEXTRACT', 'REGEXREPLACE'
]