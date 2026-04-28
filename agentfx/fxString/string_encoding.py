"""String Encoding and Decoding Functions.

This module provides functions for encoding and decoding strings using
common formats such as Base64, URL percent-encoding, HTML entities,
and classical ciphers (Caesar, Vigenère).

Key Features:
- Base64 encoding and decoding
- URL percent-encoding and decoding
- HTML entity escaping and unescaping
- Caesar cipher (shift cipher)
- Vigenère cipher (polyalphabetic substitution)
"""

import base64
import html
from urllib.parse import quote, unquote


def encode_base64(text: str, encoding: str = "utf-8") -> str:
    """Encodes a string to Base64 representation.

    Args:
        text: The input string to encode.
        encoding: Character encoding to use before Base64 conversion.

    Returns:
        The Base64-encoded string.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> encode_base64("Hello World")
        'SGVsbG8gV29ybGQ='

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return base64.b64encode(text.encode(encoding)).decode("ascii")


def decode_base64(encoded_text: str, encoding: str = "utf-8") -> str:
    """Decodes a Base64-encoded string back to plain text.

    Args:
        encoded_text: The Base64-encoded string.
        encoding: Character encoding to use after Base64 decoding.

    Returns:
        The decoded plain text string.

    Raises:
        TypeError: If encoded_text is not a string.
        ValueError: If the input is not valid Base64.

    Example:
        >>> decode_base64("SGVsbG8gV29ybGQ=")
        'Hello World'

    Complexity: O(n)
    """
    if not isinstance(encoded_text, str):
        raise TypeError("encoded_text must be a string")

    try:
        return base64.b64decode(encoded_text).decode(encoding)
    except Exception as exc:
        raise ValueError(f"Invalid Base64 input: {exc}") from exc


def encode_url(text: str, safe: str = "") -> str:
    """Encodes a string using URL percent-encoding (RFC 3986).

    Args:
        text: The input string to encode.
        safe: Characters that should not be encoded.

    Returns:
        The percent-encoded string.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> encode_url("hello world&foo=bar")
        'hello%20world%26foo%3Dbar'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return quote(text, safe=safe)


def decode_url(encoded_text: str) -> str:
    """Decodes a URL percent-encoded string back to plain text.

    Args:
        encoded_text: The percent-encoded string.

    Returns:
        The decoded plain text string.

    Raises:
        TypeError: If encoded_text is not a string.

    Example:
        >>> decode_url("hello%20world%26foo%3Dbar")
        'hello world&foo=bar'

    Complexity: O(n)
    """
    if not isinstance(encoded_text, str):
        raise TypeError("encoded_text must be a string")

    return unquote(encoded_text)


def encode_html_entities(text: str) -> str:
    """Escapes HTML special characters into their entity equivalents.

    Converts characters like ``<``, ``>``, ``&``, ``"`` and ``'`` into
    safe HTML entities (e.g. ``&lt;``, ``&gt;``, ``&amp;``).

    Args:
        text: The input string containing HTML characters.

    Returns:
        The string with HTML characters escaped.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> encode_html_entities('<script>alert("xss")</script>')
        '&lt;script&gt;alert(&quot;xss&quot;)&lt;/script&gt;'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return html.escape(text, quote=True)


def decode_html_entities(encoded_text: str) -> str:
    """Unescapes HTML entities back to their original characters.

    Args:
        encoded_text: The string with HTML entities.

    Returns:
        The string with entities replaced by actual characters.

    Raises:
        TypeError: If encoded_text is not a string.

    Example:
        >>> decode_html_entities('&lt;b&gt;bold&lt;/b&gt;')
        '<b>bold</b>'

    Complexity: O(n)
    """
    if not isinstance(encoded_text, str):
        raise TypeError("encoded_text must be a string")

    return html.unescape(encoded_text)


def caesar_cipher(text: str, shift: int, decrypt: bool = False) -> str:
    """Applies the Caesar (shift) cipher to a string.

    Shifts each alphabetical character by *shift* positions in the
    alphabet. Non-alphabetic characters are left unchanged.

    Args:
        text: The input string to encrypt or decrypt.
        shift: Number of positions to shift (1-25).
        decrypt: If True, reverse the shift to decrypt.

    Returns:
        The encrypted or decrypted string.

    Raises:
        TypeError: If text is not a string or shift is not an integer.

    Example:
        >>> caesar_cipher("Hello World", 3)
        'Khoor Zruog'
        >>> caesar_cipher("Khoor Zruog", 3, decrypt=True)
        'Hello World'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not isinstance(shift, int):
        raise TypeError("shift must be an integer")

    if decrypt:
        shift = -shift

    shift = shift % 26
    result: list[str] = []

    for ch in text:

        if "A" <= ch <= "Z":
            result.append(chr((ord(ch) - 65 + shift) % 26 + 65))
        elif "a" <= ch <= "z":
            result.append(chr((ord(ch) - 97 + shift) % 26 + 97))
        else:
            result.append(ch)

    return "".join(result)


def vigenere_cipher(
    text: str, key: str, decrypt: bool = False
) -> str:
    """Applies the Vigenère polyalphabetic cipher to a string.

    Each alphabetical character is shifted by the corresponding
    character in *key*. Non-alphabetic characters pass through
    unchanged and do not consume a key character.

    Args:
        text: The input string to encrypt or decrypt.
        key: Alphabetic key string (e.g. ``"SECRET"``).
        decrypt: If True, reverse the operation to decrypt.

    Returns:
        The encrypted or decrypted string.

    Raises:
        TypeError: If text or key is not a string.
        ValueError: If key is empty or contains non-alphabetic characters.

    Example:
        >>> vigenere_cipher("Hello World", "KEY")
        'Rijvs Uyvjn'
        >>> vigenere_cipher("Rijvs Uyvjn", "KEY", decrypt=True)
        'Hello World'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not isinstance(key, str):
        raise TypeError("key must be a string")

    if not key or not key.isalpha():
        raise ValueError("key must be a non-empty alphabetic string")

    key_upper = key.upper()
    key_len = len(key_upper)
    result: list[str] = []
    ki = 0

    for ch in text:

        if ch.isalpha():
            shift = ord(key_upper[ki % key_len]) - 65

            if decrypt:
                shift = -shift

            base = 65 if ch.isupper() else 97
            result.append(chr((ord(ch) - base + shift) % 26 + base))
            ki += 1
        else:
            result.append(ch)

    return "".join(result)
