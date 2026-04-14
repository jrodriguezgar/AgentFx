"""String Case Conversion Functions.

This module provides functions for converting strings between different
naming conventions commonly used in programming and URL generation.

Key Features:
- camelCase, PascalCase, snake_case, kebab-case conversions
- URL-friendly slug generation
- Intelligent title case
- CONSTANT_CASE conversion
"""

import re
import unicodedata


# Pre-compiled patterns for word boundary detection
_RE_CASE_BOUNDARY = re.compile(
    r"(?<=[a-z0-9])(?=[A-Z])"
    r"|(?<=[A-Z])(?=[A-Z][a-z])"
    r"|[_\-\s./\\]+"
)

# Articles/prepositions for smart title case (English + Spanish)
_TITLE_CASE_EXCEPTIONS = frozenset({
    "a", "an", "the", "and", "but", "or", "nor", "for", "yet", "so",
    "in", "on", "at", "to", "by", "of", "up", "as", "is", "if",
    "de", "del", "la", "las", "los", "el", "en", "y", "o", "con",
    "por", "para", "al", "un", "una", "unos", "unas",
})


def _split_into_words(text: str) -> list[str]:
    """Splits a string into words by detecting case boundaries and separators.

    Args:
        text: The input string.

    Returns:
        List of word tokens.

    Complexity: O(n)
    """
    parts = _RE_CASE_BOUNDARY.split(text)
    return [p.strip() for p in parts if p.strip()]


def to_camel_case(text: str) -> str:
    """Converts a string to camelCase.

    Args:
        text: The input string in any naming convention.

    Returns:
        The string in camelCase format.

    Example:
        >>> to_camel_case("hello world")
        'helloWorld'
        >>> to_camel_case("some_variable_name")
        'someVariableName'
        >>> to_camel_case("PascalCase")
        'pascalCase'

    Complexity: O(n)
    """
    words = _split_into_words(text)

    if not words:
        return ""

    return words[0].lower() + "".join(w.capitalize() for w in words[1:])


def to_pascal_case(text: str) -> str:
    """Converts a string to PascalCase.

    Args:
        text: The input string in any naming convention.

    Returns:
        The string in PascalCase format.

    Example:
        >>> to_pascal_case("hello world")
        'HelloWorld'
        >>> to_pascal_case("some_variable_name")
        'SomeVariableName'

    Complexity: O(n)
    """
    words = _split_into_words(text)
    return "".join(w.capitalize() for w in words)


def to_snake_case(text: str) -> str:
    """Converts a string to snake_case.

    Args:
        text: The input string in any naming convention.

    Returns:
        The string in snake_case format.

    Example:
        >>> to_snake_case("Hello World")
        'hello_world'
        >>> to_snake_case("camelCaseText")
        'camel_case_text'

    Complexity: O(n)
    """
    words = _split_into_words(text)
    return "_".join(w.lower() for w in words)


def to_kebab_case(text: str) -> str:
    """Converts a string to kebab-case.

    Args:
        text: The input string in any naming convention.

    Returns:
        The string in kebab-case format.

    Example:
        >>> to_kebab_case("Hello World")
        'hello-world'
        >>> to_kebab_case("camelCaseText")
        'camel-case-text'

    Complexity: O(n)
    """
    words = _split_into_words(text)
    return "-".join(w.lower() for w in words)


def to_constant_case(text: str) -> str:
    """Converts a string to CONSTANT_CASE (screaming snake case).

    Args:
        text: The input string in any naming convention.

    Returns:
        The string in CONSTANT_CASE format.

    Example:
        >>> to_constant_case("hello world")
        'HELLO_WORLD'
        >>> to_constant_case("maxRetries")
        'MAX_RETRIES'

    Complexity: O(n)
    """
    words = _split_into_words(text)
    return "_".join(w.upper() for w in words)


def to_slug(text: str, separator: str = "-") -> str:
    """Converts a string to a URL-friendly slug.

    Removes accents, special characters, and converts spaces to the separator.

    Args:
        text: The input string to slugify.
        separator: The character used between words.

    Returns:
        A URL-safe slug string.

    Example:
        >>> to_slug("Café Résumé!")
        'cafe-resume'
        >>> to_slug("Hello World 2024", separator="_")
        'hello_world_2024'

    Complexity: O(n)
    """
    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    slug = re.sub(r"[^a-z0-9]+", separator, ascii_text.lower())
    return slug.strip(separator)


def to_title_case(text: str) -> str:
    """Converts a string to smart Title Case.

    Capitalizes the first letter of each word except articles and
    prepositions (English and Spanish). The first and last words are
    always capitalized.

    Args:
        text: The input string.

    Returns:
        The string in Title Case.

    Example:
        >>> to_title_case("the lord of the rings")
        'The Lord of the Rings'
        >>> to_title_case("el señor de los anillos")
        'El Señor de los Anillos'

    Complexity: O(n)
    """
    words = text.split()

    if not words:
        return ""

    result = []

    for i, word in enumerate(words):
        is_first_or_last = i == 0 or i == len(words) - 1

        if is_first_or_last or word.lower() not in _TITLE_CASE_EXCEPTIONS:
            result.append(word.capitalize())
        else:
            result.append(word.lower())

    return " ".join(result)
