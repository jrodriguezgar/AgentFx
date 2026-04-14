"""String Hashing and Fingerprinting Functions.

This module provides functions for generating cryptographic hashes and
normalized fingerprints from strings.

Key Features:
- MD5, SHA-256, SHA-512 hashing
- Normalized fingerprint for deduplication
"""

import hashlib
import re
import unicodedata


def hash_string(text: str, algorithm: str = "sha256") -> str:
    """Generates a hexadecimal hash digest of a string.

    Args:
        text: The input string to hash.
        algorithm: Hash algorithm name — "md5", "sha256", or "sha512".

    Returns:
        The hexadecimal hash digest.

    Raises:
        TypeError: If text is not a string.
        ValueError: If algorithm is not supported.

    Example:
        >>> hash_string("hello")
        '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        >>> hash_string("hello", "md5")
        '5d41402abc4b2a76b9719d911017c592'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    supported = {"md5", "sha256", "sha512"}

    if algorithm not in supported:
        raise ValueError(f"Unsupported algorithm '{algorithm}'. Use one of: {supported}")

    h = hashlib.new(algorithm)
    h.update(text.encode("utf-8"))
    return h.hexdigest()


def fingerprint(text: str) -> str:
    """Generates a normalized fingerprint for deduplication.

    The fingerprint is created by lowercasing, removing accents,
    stripping non-alphanumeric characters, sorting the remaining tokens,
    and joining them with a single space.

    Args:
        text: The input string.

    Returns:
        A normalized fingerprint string suitable for comparing duplicates.

    Example:
        >>> fingerprint("  Café  Résumé  ")
        'cafe resume'
        >>> fingerprint("The  LORD of The  RINGS")
        'lord of rings the'

    Complexity: O(n log n) due to word sorting.
    """
    if not text or not isinstance(text, str):
        return ""

    normalized = unicodedata.normalize("NFKD", text)
    ascii_text = normalized.encode("ascii", "ignore").decode("ascii")
    cleaned = re.sub(r"[^a-z0-9\s]", "", ascii_text.lower())
    words = sorted(cleaned.split())
    return " ".join(words)
