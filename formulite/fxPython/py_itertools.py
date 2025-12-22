# itertools recipes
# https://docs.python.org/3/library/itertools.html

from collections import Counter, deque
from contextlib import suppress
from functools import reduce
from itertools import (
    accumulate, batched, chain, combinations, count, cycle, filterfalse,
    groupby, islice, product, repeat, starmap, tee, zip_longest
)
from math import comb, isqrt, prod, sumprod
from operator import getitem, itemgetter, mul, neg

def take(n, iterable):
    """
    Description: Return first n items of the iterable as a list.

    Args:
        n (int): Number of items to take.
        iterable: The iterable to take from.

    Returns:
        list: List of first n items.

    Raises:
        (none)

    Usage Example:
        take(3, [1,2,3,4,5]) -> [1,2,3]
    """
    return list(islice(iterable, n))


def prepend(value, iterable):
    """
    Description: Prepend a single value in front of an iterable.

    Args:
        value: The value to prepend.
        iterable: The iterable to prepend to.

    Returns:
        iterator: Iterator with value prepended.

    Raises:
        (none)

    Usage Example:
        list(prepend(1, [2, 3, 4])) -> [1, 2, 3, 4]
    """
    return chain([value], iterable)

def tabulate(function, start=0):
    """
    Description: Return function(0), function(1), ...

    Args:
        function: The function to apply.
        start (int): Starting index.

    Returns:
        iterator: Iterator of function applied to consecutive integers.

    Raises:
        (none)

    Usage Example:
        list(tabulate(lambda x: x**2, 3)) -> [9, 16, 25, ...]
    """
    return map(function, count(start))


def repeatfunc(function, times=None, *args):
    """
    Description: Repeat calls to a function with specified arguments.

    Args:
        function: The function to call.
        times (int or None): Number of times to repeat, or None for infinite.
        *args: Arguments to pass to the function.

    Returns:
        iterator: Iterator of function results.

    Raises:
        (none)

    Usage Example:
        list(repeatfunc(lambda: random.random(), 3))
    """
    if times is None:
        return starmap(function, repeat(args))
    return starmap(function, repeat(args, times))


def flatten(list_of_lists):
    """
    Description: Flatten one level of nesting.

    Args:
        list_of_lists: Iterable of iterables to flatten.

    Returns:
        iterator: Flattened iterator.

    Raises:
        (none)

    Usage Example:
        list(flatten([[1,2], [3,4]])) -> [1,2,3,4]
    """
    return chain.from_iterable(list_of_lists)

def ncycles(iterable, n):
    """
    Description: Returns the sequence elements n times.

    Args:
        iterable: The iterable to cycle.
        n (int): Number of cycles.

    Returns:
        iterator: Iterator repeating the sequence n times.

    Raises:
        (none)

    Usage Example:
        list(ncycles([1,2], 3)) -> [1,2,1,2,1,2]
    """
    return chain.from_iterable(repeat(tuple(iterable), n))


def loops(n):
    """
    Description: Loop n times. Like range(n) but without creating integers.

    Args:
        n (int): Number of loops.

    Returns:
        iterator: Iterator of None values.

    Raises:
        (none)

    Usage Example:
        for _ in loops(5): print("loop")
    """
    return repeat(None, n)


def tail(n, iterable):
    """
    Description: Return an iterator over the last n items.

    Args:
        n (int): Number of last items.
        iterable: The iterable.

    Returns:
        iterator: Iterator of last n items.

    Raises:
        (none)

    Usage Example:
        list(tail(3, 'ABCDEFG')) -> ['E', 'F', 'G']
    """
    return iter(deque(iterable, maxlen=n))


def consume(iterator, n=None):
    """
    Description: Advance the iterator n-steps ahead. If n is None, consume entirely.

    Args:
        iterator: The iterator to consume.
        n (int or None): Number of steps or None.

    Returns:
        None

    Raises:
        (none)

    Usage Example:
        consume(iter([1,2,3]), 2)  # advances by 2
    """
    if n is None:
        deque(iterator, maxlen=0)
    else:
        next(islice(iterator, n, n), None)


def nth(iterable, n, default=None):
    """
    Description: Returns the nth item or a default value.

    Args:
        iterable: The iterable.
        n (int): Index of item.
        default: Default value if not found.

    Returns:
        The nth item or default.

    Raises:
        (none)

    Usage Example:
        nth([1,2,3], 1) -> 2
    """
    return next(islice(iterable, n, None), default)


def quantify(iterable, predicate=bool):
    """
    Description: Given a predicate that returns True or False, count the True results.

    Args:
        iterable: The iterable to check.
        predicate: Function to apply.

    Returns:
        int: Count of True results.

    Raises:
        (none)

    Usage Example:
        quantify([1,2,3,4], lambda x: x > 2) -> 2
    """
    return sum(map(predicate, iterable))


def first_true(iterable, default=False, predicate=None):
    """
    Description: Returns the first true value or the default if there is no true value.

    Args:
        iterable: The iterable.
        default: Default value.
        predicate: Function to check truthiness.

    Returns:
        First true value or default.

    Raises:
        (none)

    Usage Example:
        first_true([0,1,2], predicate=bool) -> 1
    """
    return next(filter(predicate, iterable), default)


def all_equal(iterable, key=None):
    """
    Description: Returns True if all the elements are equal to each other.

    Args:
        iterable: The iterable.
        key: Key function for comparison.

    Returns:
        bool: True if all equal.

    Raises:
        (none)

    Usage Example:
        all_equal([1,1,1]) -> True
    """
    return len(take(2, groupby(iterable, key))) <= 1

def unique_justseen(iterable, key=None):
    """
    Description: Yield unique elements, preserving order. Remember only the element just seen.

    Args:
        iterable: The iterable.
        key: Key function.

    Returns:
        iterator: Unique elements.

    Raises:
        (none)

    Usage Example:
        list(unique_justseen('AAAABBBCCDAABBB')) -> ['A', 'B', 'C', 'D', 'A', 'B']
    """
    if key is None:
        return map(itemgetter(0), groupby(iterable))
    return map(next, map(itemgetter(1), groupby(iterable, key)))


def unique_everseen(iterable, key=None):
    """
    Description: Yield unique elements, preserving order. Remember all elements ever seen.

    Args:
        iterable: The iterable.
        key: Key function.

    Returns:
        iterator: Unique elements.

    Raises:
        (none)

    Usage Example:
        list(unique_everseen('AAAABBBCCDAABBB')) -> ['A', 'B', 'C', 'D']
    """
    seen = set()
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen.add(element)
            yield element
    else:
        for element in iterable:
            k = key(element)
            if k not in seen:
                seen.add(k)
                yield element


def unique(iterable, key=None, reverse=False):
    """
    Description: Yield unique elements in sorted order. Supports unhashable inputs.

    Args:
        iterable: The iterable.
        key: Key function.
        reverse (bool): Sort in reverse.

    Returns:
        iterator: Unique sorted elements.

    Raises:
        (none)

    Usage Example:
        list(unique([[1, 2], [3, 4], [1, 2]])) -> [[1, 2], [3, 4]]
    """
    sequenced = sorted(iterable, key=key, reverse=reverse)
    return unique_justseen(sequenced, key=key)

def sliding_window(iterable, n):
    """
    Description: Collect data into overlapping fixed-length chunks or blocks.

    Args:
        iterable: The iterable.
        n (int): Window size.

    Returns:
        iterator: Iterator of tuples.

    Raises:
        (none)

    Usage Example:
        list(sliding_window('ABCDEFG', 4)) -> [('A','B','C','D'), ('B','C','D','E'), ...]
    """
    iterator = iter(iterable)
    window = deque(islice(iterator, n - 1), maxlen=n)
    for x in iterator:
        window.append(x)
        yield tuple(window)


def grouper(iterable, n, *, incomplete='fill', fillvalue=None):
    """
    Description: Collect data into non-overlapping fixed-length chunks or blocks.

    Args:
        iterable: The iterable.
        n (int): Group size.
        incomplete: How to handle incomplete groups ('fill', 'strict', 'ignore').
        fillvalue: Value to fill with.

    Returns:
        iterator: Iterator of tuples.

    Raises:
        ValueError: If incomplete is not 'fill', 'strict', or 'ignore'.

    Usage Example:
        list(grouper('ABCDEFG', 3, fillvalue='x')) -> [('A','B','C'), ('D','E','F'), ('G','x','x')]
    """
    iterators = [iter(iterable)] * n
    match incomplete:
        case 'fill':
            return zip_longest(*iterators, fillvalue=fillvalue)
        case 'strict':
            return zip(*iterators, strict=True)
        case 'ignore':
            return zip(*iterators)
        case _:
            raise ValueError('Expected fill, strict, or ignore')


def roundrobin(*iterables):
    """
    Description: Visit input iterables in a cycle until each is exhausted.

    Args:
        *iterables: The iterables.

    Returns:
        iterator: Round-robin iterator.

    Raises:
        (none)

    Usage Example:
        list(roundrobin('ABC', 'D', 'EF')) -> ['A', 'D', 'E', 'B', 'F', 'C']
    """
    iterators = map(iter, iterables)
    for num_active in range(len(iterables), 0, -1):
        iterators = cycle(islice(iterators, num_active))
        yield from map(next, iterators)

def subslices(seq):
    """
    Description: Return all contiguous non-empty subslices of a sequence.

    Args:
        seq: The sequence.

    Returns:
        iterator: Iterator of slices.

    Raises:
        (none)

    Usage Example:
        list(subslices('ABCD')) -> ['A', 'AB', 'ABC', 'ABCD', 'B', 'BC', 'BCD', 'C', 'CD', 'D']
    """
    slices = starmap(slice, combinations(range(len(seq) + 1), 2))
    return map(getitem, repeat(seq), slices)


def iter_index(iterable, value, start=0, stop=None):
    """
    Description: Return indices where a value occurs in a sequence or iterable.

    Args:
        iterable: The iterable.
        value: Value to find.
        start (int): Start index.
        stop (int or None): Stop index.

    Returns:
        iterator: Iterator of indices.

    Raises:
        (none)

    Usage Example:
        list(iter_index('AABCADEAF', 'A')) -> [0, 1, 4, 7]
    """
    seq_index = getattr(iterable, 'index', None)
    if seq_index is None:
        iterator = islice(iterable, start, stop)
        for i, element in enumerate(iterator, start):
            if element is value or element == value:
                yield i
    else:
        stop = len(iterable) if stop is None else stop
        i = start
        with suppress(ValueError):
            while True:
                yield (i := seq_index(value, i, stop))
                i += 1


def iter_except(function, exception, first=None):
    """
    Description: Convert a call-until-exception interface to an iterator interface.

    Args:
        function: Function to call.
        exception: Exception to catch.
        first: Initial value.

    Returns:
        iterator: Iterator from function calls.

    Raises:
        (none)

    Usage Example:
        list(iter_except(dict.popitem, KeyError))  # from a dict
    """
    with suppress(exception):
        if first is not None:
            yield first()
        while True:
            yield function()

def multinomial(*counts):
    """
    Description: Number of distinct arrangements of a multiset.

    Args:
        *counts: Counts of each item.

    Returns:
        int: Multinomial coefficient.

    Raises:
        (none)

    Usage Example:
        multinomial(5, 2, 2, 1, 1) -> 83160
    """
    return prod(map(comb, accumulate(counts), counts))


def powerset(iterable):
    """
    Description: Subsequences of the iterable from shortest to longest.

    Args:
        iterable: The iterable.

    Returns:
        iterator: Iterator of tuples.

    Raises:
        (none)

    Usage Example:
        list(powerset([1,2,3])) -> [(), (1,), (2,), (3,), (1,2), (1,3), (2,3), (1,2,3)]
    """
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))


def sum_of_squares(iterable):
    """
    Description: Add up the squares of the input values.

    Args:
        iterable: The iterable of numbers.

    Returns:
        float or int: Sum of squares.

    Raises:
        (none)

    Usage Example:
        sum_of_squares([10, 20, 30]) -> 1400
    """
    return sumprod(*tee(iterable))


def reshape(matrix, columns):
    """
    Description: Reshape a 2-D matrix to have a given number of columns.

    Args:
        matrix: 2D matrix.
        columns (int): Number of columns.

    Returns:
        iterator: Reshaped matrix.

    Raises:
        (none)

    Usage Example:
        list(reshape([(0, 1), (2, 3), (4, 5)], 3)) -> [(0, 1, 2), (3, 4, 5)]
    """
    return batched(chain.from_iterable(matrix), columns, strict=True)


def transpose(matrix):
    """
    Description: Swap the rows and columns of a 2-D matrix.

    Args:
        matrix: 2D matrix.

    Returns:
        iterator: Transposed matrix.

    Raises:
        (none)

    Usage Example:
        list(transpose([(1, 2, 3), (11, 22, 33)])) -> [(1, 11), (2, 22), (3, 33)]
    """
    return zip(*matrix, strict=True)


def matmul(m1, m2):
    """
    Description: Multiply two matrices.

    Args:
        m1: First matrix.
        m2: Second matrix.

    Returns:
        iterator: Result matrix.

    Raises:
        (none)

    Usage Example:
        list(matmul([(7, 5), (3, 5)], [(2, 5), (7, 9)])) -> [(49, 80), (41, 60)]
    """
    n = len(m2[0])
    return batched(starmap(sumprod, product(m1, transpose(m2))), n)

def convolve(signal, kernel):
    """
    Description: Discrete linear convolution of two iterables. Equivalent to polynomial multiplication.

    Args:
        signal: The signal iterable.
        kernel: The kernel iterable.

    Returns:
        iterator: Convolution result.

    Raises:
        (none)

    Usage Example:
        list(convolve([1, -1, -20], [1, -3])) -> [1, -4, -17, 60]
    """
    kernel = tuple(kernel)[::-1]
    n = len(kernel)
    padded_signal = chain(repeat(0, n-1), signal, repeat(0, n-1))
    windowed_signal = sliding_window(padded_signal, n)
    return map(sumprod, repeat(kernel), windowed_signal)


def polynomial_from_roots(roots):
    """
    Description: Compute a polynomial's coefficients from its roots.

    Args:
        roots: List of roots.

    Returns:
        list: Coefficients.

    Raises:
        (none)

    Usage Example:
        polynomial_from_roots([5, -4, 3]) -> [1, -4, -17, 60]
    """
    factors = zip(repeat(1), map(neg, roots))
    return list(reduce(convolve, factors, [1]))


def polynomial_eval(coefficients, x):
    """
    Description: Evaluate a polynomial at a specific value.

    Args:
        coefficients: List of coefficients.
        x: Value to evaluate at.

    Returns:
        float or int: Result.

    Raises:
        (none)

    Usage Example:
        polynomial_eval([1, -4, -17, 60], x=5) -> 0
    """
    n = len(coefficients)
    if not n:
        return type(x)(0)
    powers = map(pow, repeat(x), reversed(range(n)))
    return sumprod(coefficients, powers)


def polynomial_derivative(coefficients):
    """
    Description: Compute the first derivative of a polynomial.

    Args:
        coefficients: List of coefficients.

    Returns:
        list: Derivative coefficients.

    Raises:
        (none)

    Usage Example:
        polynomial_derivative([1, -4, -17, 60]) -> [3, -8, -17]
    """
    n = len(coefficients)
    powers = reversed(range(1, n))
    return list(map(mul, coefficients, powers))

def sieve(n):
    """
    Description: Primes less than n.

    Args:
        n (int): Upper limit.

    Returns:
        iterator: Iterator of primes.

    Raises:
        (none)

    Usage Example:
        list(sieve(30)) -> [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    """
    if n > 2:
        yield 2
    data = bytearray((0, 1)) * (n // 2)
    for p in iter_index(data, 1, start=3, stop=isqrt(n) + 1):
        data[p*p : n : p+p] = bytes(len(range(p*p, n, p+p)))
    yield from iter_index(data, 1, start=3)


def factor(n):
    """
    Description: Prime factors of n.

    Args:
        n (int): Number to factor.

    Returns:
        iterator: Iterator of prime factors.

    Raises:
        (none)

    Usage Example:
        list(factor(99)) -> [3, 3, 11]
    """
    for prime in sieve(isqrt(n) + 1):
        while not n % prime:
            yield prime
            n //= prime
            if n == 1:
                return
    if n > 1:
        yield n


def is_prime(n):
    """
    Description: Return True if n is prime.

    Args:
        n (int): Number to check.

    Returns:
        bool: True if prime.

    Raises:
        (none)

    Usage Example:
        is_prime(7) -> True
    """
    return n > 1 and next(factor(n)) == n


def totient(n):
    """
    Description: Count of natural numbers up to n that are coprime to n.

    Args:
        n (int): Number.

    Returns:
        int: Totient value.

    Raises:
        (none)

    Usage Example:
        totient(12) -> 4
    """
    for prime in set(factor(n)):
        n -= n // prime
    return n
