"""String Regular Expression Functions.

This module provides high-level regex wrappers for common pattern matching,
extraction, and search operations on strings.

Key Features:
- Regex pattern matching (boolean)
- Single and multi-match extraction
- Regex-based splitting
"""

import re
from typing import Optional


def regex_match(text: str, pattern: str, case_sensitive: bool = True) -> bool:
    """Checks whether a string matches a regular expression pattern.

    Args:
        text: The input string to test.
        pattern: The regex pattern to match against.
        case_sensitive: If False, performs case-insensitive matching.

    Returns:
        True if the pattern matches anywhere in the string.

    Raises:
        re.error: If the pattern is not a valid regex.

    Example:
        >>> regex_match("Hello World 123", r"\\d+")
        True
        >>> regex_match("abc", r"^[A-Z]+$")
        False

    Complexity: O(n*m)
    """
    flags = 0 if case_sensitive else re.IGNORECASE
    return bool(re.search(pattern, str(text), flags))


def regex_extract(text: str, pattern: str, group: int = 0,
                  case_sensitive: bool = True) -> Optional[str]:
    """Extracts the first match of a regex pattern from a string.

    Args:
        text: The input string to search.
        pattern: The regex pattern to find.
        group: The capture group index to return (0 = full match).
        case_sensitive: If False, performs case-insensitive matching.

    Returns:
        The matched text, or None if no match was found.

    Raises:
        re.error: If the pattern is not a valid regex.

    Example:
        >>> regex_extract("Order #12345 confirmed", r"#(\\d+)", group=1)
        '12345'
        >>> regex_extract("no match here", r"\\d+")

    Complexity: O(n*m)
    """
    flags = 0 if case_sensitive else re.IGNORECASE
    match = re.search(pattern, str(text), flags)

    if match is None:
        return None

    try:
        return match.group(group)
    except IndexError:
        return match.group(0)


def regex_extract_all(text: str, pattern: str,
                      case_sensitive: bool = True) -> list[str]:
    """Extracts all matches of a regex pattern from a string.

    Args:
        text: The input string to search.
        pattern: The regex pattern to find.
        case_sensitive: If False, performs case-insensitive matching.

    Returns:
        A list of all matching strings. Empty list if no matches found.

    Raises:
        re.error: If the pattern is not a valid regex.

    Example:
        >>> regex_extract_all("a1 b2 c3", r"[a-z]\\d")
        ['a1', 'b2', 'c3']
        >>> regex_extract_all("no digits here", r"\\d+")
        []

    Complexity: O(n*m)
    """
    flags = 0 if case_sensitive else re.IGNORECASE
    return re.findall(pattern, str(text), flags)


def regex_split(text: str, pattern: str, max_split: int = 0,
                case_sensitive: bool = True) -> list[str]:
    """Splits a string by a regex pattern.

    Args:
        text: The input string to split.
        pattern: The regex pattern to use as delimiter.
        max_split: Maximum number of splits (0 = unlimited).
        case_sensitive: If False, performs case-insensitive matching.

    Returns:
        A list of substrings.

    Raises:
        re.error: If the pattern is not a valid regex.

    Example:
        >>> regex_split("one, two; three  four", r"[,;\\s]+")
        ['one', 'two', 'three', 'four']

    Complexity: O(n*m)
    """
    flags = 0 if case_sensitive else re.IGNORECASE
    return re.split(pattern, str(text), maxsplit=max_split, flags=flags)


def regex_count(text: str, pattern: str,
                case_sensitive: bool = True) -> int:
    """Counts the number of non-overlapping matches of a regex pattern.

    Args:
        text: The input string to search.
        pattern: The regex pattern to count.
        case_sensitive: If False, performs case-insensitive matching.

    Returns:
        The number of matches found.

    Raises:
        re.error: If the pattern is not a valid regex.

    Example:
        >>> regex_count("aAbBaA", r"a", case_sensitive=False)
        4
        >>> regex_count("one 1 two 2 three 3", r"\\d+")
        3

    Complexity: O(n*m)
    """
    flags = 0 if case_sensitive else re.IGNORECASE
    return len(re.findall(pattern, str(text), flags))
