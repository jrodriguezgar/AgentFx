"""String Validation Functions.

This module provides functions for validating and checking various properties
of strings. It includes functions to verify the presence of specific character
types (like digits) and to compare strings for character-level equality.

Key Features:
- Character presence validation (digits, letters)
- Anagram detection and character comparison
- Type-safe validation with proper error handling
"""


def contains_digit(input_string: str) -> bool:
    """
    Checks if the given string contains at least one digit.

    This function iterates through each character of the input string and
    returns True as soon as it finds any digit. If no digits are found
    after checking all characters, it returns False.

    Args:
        input_string: The string to be checked for the presence of digits.

    Returns:
        True if the string contains at least one digit, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Example of use:
        >>> contains_digit("abc123def")
        True
        >>> contains_digit("no_digits_here")
        False
        >>> contains_digit("")
        False
        >>> contains_digit("123")
        True

    **Cost:** O(n), where n is the length of the input string
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Use a generator expression with 'any()' for efficient checking.
    # 'any()' returns True as soon as the first digit is found,
    # avoiding unnecessary iterations.
    return any(char.isdigit() for char in input_string)


def same_letters(string_a: str, string_b: str) -> bool:
    """
    Checks if two strings contain the exact same characters, irrespective of their order.

    This function determines if one string is an anagram of another,
    meaning they are composed of the same characters with the same frequencies.
    The comparison is case-sensitive.

    Args:
        string_a (str): The first string for comparison.
        string_b (str): The second string for comparison.

    Returns:
        bool: True if both strings contain the same characters (same count, same case),
              False otherwise.

    Raises:
        TypeError: If 'string_a' or 'string_b' are not strings.

    Example:
        >>> same_letters("listen", "silent")
        True

        >>> same_letters("hello", "holle")
        True

        >>> same_letters("abc", "ab")
        False

        >>> same_letters("Aardvark", "aardvark")
        False

        >>> same_letters("", "")
        True

    **Cost:** O(n log n), where n is the maximum length of the two input strings (due to sorting)
    """
    if not isinstance(string_a, str):
        raise TypeError("Input 'string_a' must be a string.")
    if not isinstance(string_b, str):
        raise TypeError("Input 'string_b' must be a string.")

    # Convert both strings to sorted lists of their characters.
    # Sorting ensures that if the strings contain the same characters,
    # they will be in the same order after sorting, allowing for direct comparison.
    # This approach effectively checks for anagrams.
    return sorted(string_a) == sorted(string_b)

