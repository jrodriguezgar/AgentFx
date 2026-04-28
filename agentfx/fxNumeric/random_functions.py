"""Random number generation module.

Provides pure-function wrappers for random number generation, suitable for
MCP/LLM tool exposure. All functions use the module-level ``random`` generator
which can be seeded via :func:`set_random_seed` for reproducibility.
"""

import random as _rng
import uuid as _uuid
from typing import Any, List, Sequence


_generator = _rng.Random()


def set_random_seed(seed: int) -> None:
    """Set the random seed for reproducible generation.

    Args:
        seed: Integer seed value.

    Returns:
        None.

    Example:
        >>> set_random_seed(42)

    Complexity: O(1)
    """

    _generator.seed(seed)


def random_int(low: int, high: int) -> int:
    """Return a random integer in the inclusive range [low, high].

    Args:
        low: Lower bound (inclusive).
        high: Upper bound (inclusive).

    Returns:
        Random integer between low and high.

    Raises:
        ValueError: If low > high.

    Example:
        >>> set_random_seed(42)
        >>> random_int(1, 10)
        2

    Complexity: O(1)
    """

    if low > high:
        raise ValueError(f"low ({low}) must be <= high ({high}).")

    return _generator.randint(low, high)


def random_float(low: float = 0.0, high: float = 1.0) -> float:
    """Return a random float in the range [low, high).

    Args:
        low: Lower bound (inclusive). Defaults to 0.0.
        high: Upper bound (exclusive). Defaults to 1.0.

    Returns:
        Random float between low (inclusive) and high (exclusive).

    Raises:
        ValueError: If low >= high.

    Example:
        >>> set_random_seed(42)
        >>> round(random_float(0, 100), 2)
        63.94

    Complexity: O(1)
    """

    if low >= high:
        raise ValueError(f"low ({low}) must be < high ({high}).")

    return _generator.uniform(low, high)


def random_choice(items: Sequence[Any]) -> Any:
    """Return a random element from a non-empty sequence.

    Args:
        items: Non-empty sequence to choose from.

    Returns:
        A randomly selected element.

    Raises:
        ValueError: If items is empty.

    Example:
        >>> set_random_seed(42)
        >>> random_choice(['a', 'b', 'c', 'd'])
        'a'

    Complexity: O(1)
    """

    if not items:
        raise ValueError("Cannot choose from an empty sequence.")

    return _generator.choice(items)


def random_sample(items: Sequence[Any], k: int) -> List[Any]:
    """Return k unique elements chosen from the sequence without replacement.

    Args:
        items: Sequence to sample from.
        k: Number of elements to sample.

    Returns:
        List of k unique randomly selected elements.

    Raises:
        ValueError: If k > len(items) or k < 0.

    Example:
        >>> set_random_seed(42)
        >>> random_sample([1, 2, 3, 4, 5], 3)
        [4, 1, 5]

    Complexity: O(k)
    """

    if k < 0 or k > len(items):
        raise ValueError(f"k ({k}) must be between 0 and len(items) ({len(items)}).")

    return _generator.sample(list(items), k)


def random_shuffle(items: Sequence[Any]) -> List[Any]:
    """Return a new list with the elements randomly shuffled.

    The original sequence is not modified.

    Args:
        items: Sequence to shuffle.

    Returns:
        New list with elements in random order.

    Example:
        >>> set_random_seed(42)
        >>> random_shuffle([1, 2, 3, 4, 5])
        [4, 2, 5, 1, 3]

    Complexity: O(n)
    """

    result = list(items)
    _generator.shuffle(result)
    return result


def random_gaussian(mean: float = 0.0, std: float = 1.0) -> float:
    """Return a random float from a Gaussian (normal) distribution.

    Args:
        mean: Mean of the distribution. Defaults to 0.0.
        std: Standard deviation. Defaults to 1.0.

    Returns:
        Random float drawn from N(mean, std^2).

    Raises:
        ValueError: If std < 0.

    Example:
        >>> set_random_seed(42)
        >>> round(random_gaussian(0, 1), 4)
        -0.4008

    Complexity: O(1)
    """

    if std < 0:
        raise ValueError(f"std ({std}) must be >= 0.")

    return _generator.gauss(mean, std)


def random_weighted_choice(items: Sequence[Any],
                           weights: Sequence[float]) -> Any:
    """Return a random element using weighted probabilities.

    Args:
        items: Non-empty sequence of items.
        weights: Corresponding positive weights (same length as items).

    Returns:
        A single randomly selected element.

    Raises:
        ValueError: If items is empty or lengths mismatch.

    Example:
        >>> set_random_seed(42)
        >>> random_weighted_choice(['a', 'b', 'c'], [1, 1, 98])
        'c'

    Complexity: O(n)
    """

    if not items:
        raise ValueError("Cannot choose from an empty sequence.")

    if len(items) != len(weights):
        raise ValueError("items and weights must have the same length.")

    return _generator.choices(list(items), weights=list(weights), k=1)[0]


def random_uuid() -> str:
    """Generate a random UUID version 4 as a string.

    Returns:
        UUID v4 string (e.g. ``'550e8400-e29b-41d4-a716-446655440000'``).

    Example:
        >>> isinstance(random_uuid(), str)
        True

    Complexity: O(1)
    """

    return str(_uuid.uuid4())


def random_bool(probability: float = 0.5) -> bool:
    """Return a random boolean with the given probability of True.

    Args:
        probability: Probability of returning True, in [0, 1]. Defaults to 0.5.

    Returns:
        True with the given probability, False otherwise.

    Raises:
        ValueError: If probability is not in [0, 1].

    Example:
        >>> set_random_seed(42)
        >>> random_bool(0.9)
        True

    Complexity: O(1)
    """

    if not 0.0 <= probability <= 1.0:
        raise ValueError(f"probability ({probability}) must be in [0, 1].")

    return _generator.random() < probability


def random_array(
    rows: int = 1,
    columns: int = 1,
    min_value: float = 0.0,
    max_value: float = 1.0,
    whole_number: bool = False,
) -> List[List[float]]:
    """Returns an array of random numbers.

    Description:
        Generates a 2-D array (list of lists) filled with random numbers.
        Can return either floats in [min, max) or integers in [min, max].
        Equivalent to Excel RANDARRAY.

    Args:
        rows: Number of rows (default 1).
        columns: Number of columns (default 1).
        min_value: Minimum value (default 0.0).
        max_value: Maximum value (default 1.0).
        whole_number: If True, return integers; if False, return floats.

    Returns:
        A list of lists of random numbers.

    Raises:
        ValueError: If rows or columns < 1, or min_value > max_value.

    Example:
        >>> set_random_seed(42)
        >>> random_array(2, 3, 1, 10, True)
        [[2, 1, 10], [4, 10, 4]]

    Complexity: O(rows * columns)
    """
    if rows < 1 or columns < 1:
        raise ValueError("rows and columns must be at least 1.")

    if min_value > max_value:
        raise ValueError("min_value must be <= max_value.")

    if whole_number:
        lo = int(min_value)
        hi = int(max_value)
        return [
            [_generator.randint(lo, hi) for _ in range(columns)]
            for _ in range(rows)
        ]

    return [
        [_generator.uniform(min_value, max_value) for _ in range(columns)]
        for _ in range(rows)
    ]
