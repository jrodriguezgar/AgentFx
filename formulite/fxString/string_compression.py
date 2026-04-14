"""String Compression and Decompression Functions.

This module provides functions for compressing and decompressing strings
using zlib, returning Base64-encoded representations for safe transport.

Key Features:
- zlib-based text compression with Base64 output
- Decompression from Base64-encoded compressed data
"""

import base64
import zlib


def compress_string(text: str, encoding: str = "utf-8") -> str:
    """Compresses a string using zlib and returns a Base64-encoded result.

    Args:
        text: The input string to compress.
        encoding: Character encoding to use before compression.

    Returns:
        A Base64-encoded string of the compressed data.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> compressed = compress_string("hello " * 100)
        >>> len(compressed) < len("hello " * 100)
        True

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    compressed = zlib.compress(text.encode(encoding))
    return base64.b64encode(compressed).decode("ascii")


def decompress_string(compressed_text: str, encoding: str = "utf-8") -> str:
    """Decompresses a Base64-encoded zlib-compressed string.

    Args:
        compressed_text: The Base64-encoded compressed string.
        encoding: Character encoding to use after decompression.

    Returns:
        The original decompressed text.

    Raises:
        TypeError: If compressed_text is not a string.
        ValueError: If the input is not valid compressed data.

    Example:
        >>> decompress_string(compress_string("hello world"))
        'hello world'

    Complexity: O(n)
    """
    if not isinstance(compressed_text, str):
        raise TypeError("compressed_text must be a string")

    try:
        raw = base64.b64decode(compressed_text)
        return zlib.decompress(raw).decode(encoding)
    except Exception as exc:
        raise ValueError(f"Invalid compressed data: {exc}") from exc
