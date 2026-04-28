"""Number Theory Functions Module.

Provides functions for primality testing, prime generation, divisor analysis,
Fibonacci sequences, digital roots, and other number-theoretic operations.

Example:
    >>> from agentfx.fxNumeric.number_theory_functions import is_prime, divisors
    >>> is_prime(7)
    True
    >>> divisors(12)
    [1, 2, 3, 4, 6, 12]
"""

import math
from typing import List


def is_prime(n: int) -> bool:
    """Checks if a number is prime.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if the number is prime, False otherwise.

    Example:
        >>> is_prime(7)
        True
        >>> is_prime(4)
        False
        >>> is_prime(2)
        True
        >>> is_prime(1)
        False

    **Cost:** O(sqrt(n)), where n is the number to check.
    """
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):

        if n % i == 0:
            return False

    return True


def get_primes_up_to(limit: int) -> list[int]:
    """Generates a list of prime numbers up to a given limit using the Sieve of Eratosthenes.

    Args:
        limit (int): The upper limit to search for prime numbers.

    Returns:
        list[int]: List of prime numbers found.

    Raises:
        ValueError: If the limit is less than 2.

    Example:
        >>> get_primes_up_to(10)
        [2, 3, 5, 7]
        >>> get_primes_up_to(20)
        [2, 3, 5, 7, 11, 13, 17, 19]

    **Cost:** O(n log log n), Sieve of Eratosthenes algorithm.
    """
    if limit < 2:
        raise ValueError("Limit must be at least 2")

    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(math.sqrt(limit)) + 1):

        if sieve[i]:

            for j in range(i * i, limit + 1, i):
                sieve[j] = False

    return [i for i in range(limit + 1) if sieve[i]]


def fibonacci_sequence(n: int) -> list[int]:
    """Returns the first *n* Fibonacci numbers.

    Args:
        n: How many numbers to generate (>= 0).

    Returns:
        A list with the first *n* Fibonacci numbers.

    Raises:
        ValueError: If *n* is negative.

    Example:
        >>> fibonacci_sequence(7)
        [0, 1, 1, 2, 3, 5, 8]

    Complexity: O(n)
    """
    if n < 0:
        raise ValueError("n must be >= 0.")

    if n == 0:
        return []

    seq = [0]
    a, b = 0, 1

    for _ in range(n - 1):
        a, b = b, a + b
        seq.append(a)

    return seq


def divisors(n: int) -> list[int]:
    """Returns all positive divisors of *n* in ascending order.

    Args:
        n: A positive integer.

    Returns:
        Sorted list of divisors.

    Raises:
        ValueError: If *n* < 1.

    Example:
        >>> divisors(12)
        [1, 2, 3, 4, 6, 12]

    Complexity: O(sqrt(n))
    """
    if n < 1:
        raise ValueError("n must be >= 1.")

    small, large = [], []

    for i in range(1, int(n ** 0.5) + 1):

        if n % i == 0:
            small.append(i)

            if i != n // i:
                large.append(n // i)

    return small + large[::-1]


def prime_factors(n: int) -> list[int]:
    """Returns the prime factorization of *n* in ascending order.

    Args:
        n: An integer >= 2.

    Returns:
        List of prime factors (with repetition).

    Raises:
        ValueError: If *n* < 2.

    Example:
        >>> prime_factors(60)
        [2, 2, 3, 5]
        >>> prime_factors(17)
        [17]

    Complexity: O(sqrt(n))
    """
    if n < 2:
        raise ValueError("n must be >= 2.")

    factors: list[int] = []
    d = 2

    while d * d <= n:

        while n % d == 0:
            factors.append(d)
            n //= d

        d += 1

    if n > 1:
        factors.append(n)

    return factors


def collatz_length(n: int) -> int:
    """Counts the number of steps in the Collatz sequence until reaching 1.

    Args:
        n: A positive integer.

    Returns:
        Number of steps.

    Raises:
        ValueError: If *n* < 1.

    Example:
        >>> collatz_length(6)
        8
        >>> collatz_length(1)
        0

    Complexity: O(?) -- conjectured to terminate for all n.
    """
    if n < 1:
        raise ValueError("n must be >= 1.")

    steps = 0

    while n != 1:

        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        steps += 1

    return steps


def is_even(n: int) -> bool:
    """Checks whether an integer is even.

    Description:
        Returns True if n is divisible by 2. Equivalent to Excel ISEVEN.

    Args:
        n: The integer to test.

    Returns:
        bool: True if n is even, False otherwise.

    Raises:
        TypeError: If n is not an integer.

    Example:
        >>> is_even(4)
        True
        >>> is_even(7)
        False

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    return n % 2 == 0


def is_odd(n: int) -> bool:
    """Checks whether an integer is odd.

    Description:
        Returns True if n is not divisible by 2. Equivalent to Excel ISODD.

    Args:
        n: The integer to test.

    Returns:
        bool: True if n is odd, False otherwise.

    Raises:
        TypeError: If n is not an integer.

    Example:
        >>> is_odd(7)
        True
        >>> is_odd(4)
        False

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    return n % 2 != 0


def euler_totient(n: int) -> int:
    """Calculates Euler's totient function phi(n).

    Returns the count of integers from 1 to n that are coprime to n.
    Fundamental in number theory and used in RSA cryptography.

    Args:
        n: Positive integer.

    Returns:
        Number of integers coprime to n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Example:
        >>> euler_totient(12)
        4
        >>> euler_totient(7)
        6

    Complexity: O(sqrt(n))
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    result = n
    p = 2

    temp = n

    while p * p <= temp:

        if temp % p == 0:
            # Remove all factors of p
            while temp % p == 0:
                temp //= p

            result -= result // p

        p += 1

    if temp > 1:
        result -= result // temp

    return result


def is_palindrome_number(n: int) -> bool:
    """Checks whether an integer is a palindrome.

    A palindrome number reads the same forwards and backwards.
    Negative numbers are not considered palindromes.

    Args:
        n: Integer to check.

    Returns:
        True if n is a palindrome number, False otherwise.

    Raises:
        TypeError: If n is not an integer.

    Example:
        >>> is_palindrome_number(121)
        True
        >>> is_palindrome_number(123)
        False
        >>> is_palindrome_number(-121)
        False

    Complexity: O(d) where d is the number of digits.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        return False

    s = str(n)
    return s == s[::-1]


def modular_exponentiation(base: int, exponent: int, modulus: int) -> int:
    """Computes (base ** exponent) % modulus efficiently.

    Uses Python's built-in three-argument ``pow`` for fast modular
    exponentiation with the square-and-multiply algorithm.

    Args:
        base: The base integer.
        exponent: The exponent (must be >= 0).
        modulus: The modulus (must be > 0).

    Returns:
        Result of (base ** exponent) mod modulus.

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If exponent < 0 or modulus <= 0.

    Example:
        >>> modular_exponentiation(2, 10, 1000)
        24
        >>> modular_exponentiation(3, 13, 7)
        3

    Complexity: O(log(exponent))
    """
    if not all(isinstance(v, int) for v in [base, exponent, modulus]):
        raise TypeError("base, exponent, and modulus must be integers.")

    if exponent < 0:
        raise ValueError("exponent must be >= 0.")

    if modulus <= 0:
        raise ValueError("modulus must be > 0.")

    return pow(base, exponent, modulus)


def modular_inverse(a: int, m: int) -> int:
    """Computes the modular multiplicative inverse of a modulo m.

    Finds x such that (a * x) % m == 1 using the extended Euclidean
    algorithm. The inverse exists only when gcd(a, m) == 1.

    Args:
        a: The integer whose inverse is sought.
        m: The modulus (must be > 0).

    Returns:
        The modular inverse in the range [0, m).

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If m <= 0 or the inverse does not exist.

    Example:
        >>> modular_inverse(3, 7)
        5
        >>> modular_inverse(10, 17)
        12

    Complexity: O(log(min(a, m)))
    """
    if not isinstance(a, int) or not isinstance(m, int):
        raise TypeError("a and m must be integers.")

    if m <= 0:
        raise ValueError("m must be > 0.")

    # Extended Euclidean algorithm
    g, x, _ = _extended_gcd(a % m, m)

    if g != 1:
        raise ValueError(f"Modular inverse does not exist (gcd({a}, {m}) = {g}).")

    return x % m


def _extended_gcd(a: int, b: int) -> tuple:
    """Extended Euclidean algorithm returning (gcd, x, y)."""
    if a == 0:
        return (b, 0, 1)

    g, x1, y1 = _extended_gcd(b % a, a)
    return (g, y1 - (b // a) * x1, x1)


def lucas_sequence(n: int) -> List[int]:
    """Generates the first n Lucas numbers.

    The Lucas sequence starts with 2, 1 and follows the same recurrence
    as Fibonacci: L(n) = L(n-1) + L(n-2). It is closely related to
    Fibonacci numbers and appears in various mathematical identities.

    Args:
        n: Number of Lucas numbers to generate (must be >= 1).

    Returns:
        List of the first n Lucas numbers.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Example:
        >>> lucas_sequence(8)
        [2, 1, 3, 4, 7, 11, 18, 29]

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    if n == 1:
        return [2]

    seq = [2, 1]

    for _ in range(2, n):
        seq.append(seq[-1] + seq[-2])

    return seq


def catalan_number(n: int) -> int:
    """Calculates the nth Catalan number.

    Catalan numbers count the number of correct bracket sequences,
    binary trees with n+1 leaves, triangulations of polygons, and
    many other combinatorial structures.

    C(n) = (2n)! / ((n+1)! * n!)

    Args:
        n: Non-negative integer index.

    Returns:
        The nth Catalan number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> catalan_number(0)
        1
        >>> catalan_number(5)
        42
        >>> catalan_number(10)
        16796

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be >= 0.")

    # Iterative computation to avoid large intermediate factorials
    result = 1

    for i in range(n):
        result = result * (2 * n - i) // (i + 1)

    return result // (n + 1)


def next_prime(n: int) -> int:
    """Finds the smallest prime number greater than n.

    Args:
        n: Starting integer.

    Returns:
        The next prime after n.

    Raises:
        TypeError: If n is not an integer.

    Example:
        >>> next_prime(10)
        11
        >>> next_prime(13)
        17
        >>> next_prime(1)
        2

    Complexity: O(k * sqrt(k)) where k is the gap to the next prime.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    candidate = max(n + 1, 2)

    while not is_prime(candidate):
        candidate += 1

    return candidate


def is_coprime(a: int, b: int) -> bool:
    """Checks whether two integers are coprime.

    Two integers are coprime if their greatest common divisor is 1.

    Args:
        a: First integer.
        b: Second integer.

    Returns:
        True if gcd(a, b) == 1.

    Raises:
        TypeError: If inputs are not integers.

    Example:
        >>> is_coprime(14, 15)
        True
        >>> is_coprime(14, 21)
        False

    Complexity: O(log(min(a, b)))
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers.")

    import math as _math
    return _math.gcd(a, b) == 1


def goldbach_partition(n: int) -> tuple:
    """Finds a Goldbach partition for an even integer >= 4.

    Goldbach's conjecture states that every even integer ≥ 4 can be
    expressed as the sum of two primes.

    Args:
        n: An even integer >= 4.

    Returns:
        A tuple (p, q) where both are prime and p + q == n, with p <= q.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is odd or less than 4.

    Example:
        >>> goldbach_partition(28)
        (5, 23)
        >>> goldbach_partition(100)
        (3, 97)

    Complexity: O(n * sqrt(n))
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 4 or n % 2 != 0:
        raise ValueError("n must be an even integer >= 4.")

    for p in range(2, n // 2 + 1):

        if is_prime(p) and is_prime(n - p):
            return (p, n - p)

    raise ValueError(f"No Goldbach partition found for {n}.")


def nth_fibonacci(n: int) -> int:
    """Returns the n-th Fibonacci number using fast doubling.

    F(0) = 0, F(1) = 1, F(k) = F(k-1) + F(k-2).

    Args:
        n: Non-negative index into the Fibonacci sequence.

    Returns:
        The n-th Fibonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> nth_fibonacci(10)
        55
        >>> nth_fibonacci(0)
        0

    Complexity: O(log n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    def _fast_double(k: int) -> tuple:
        if k == 0:
            return (0, 1)

        a, b = _fast_double(k >> 1)
        c = a * (2 * b - a)
        d = a * a + b * b

        if k & 1:
            return (d, c + d)

        return (c, d)

    return _fast_double(n)[0]


def integer_partitions_count(n: int) -> int:
    """Counts the number of integer partitions of n.

    A partition of n is a way of writing n as a sum of positive integers,
    where order does not matter.

    Args:
        n: Non-negative integer.

    Returns:
        The number of partitions p(n).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> integer_partitions_count(5)
        7
        >>> integer_partitions_count(0)
        1

    Complexity: O(n^2)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be a non-negative integer.")

    dp = [0] * (n + 1)
    dp[0] = 1

    for k in range(1, n + 1):

        for j in range(k, n + 1):
            dp[j] += dp[j - k]

    return dp[n]


def chinese_remainder_theorem(
    remainders: List[int],
    moduli: List[int],
) -> int:
    """Solves a system of simultaneous congruences via CRT.

    Given x ≡ r_i (mod m_i) for pairwise coprime moduli, returns
    the unique solution x in [0, M) where M = product of all moduli.

    Args:
        remainders: List of remainders r_i.
        moduli: List of pairwise coprime moduli m_i (each > 0).

    Returns:
        The unique solution x.

    Raises:
        TypeError: If inputs are not lists of integers.
        ValueError: If lists are empty, different lengths, or moduli not coprime.

    Example:
        >>> chinese_remainder_theorem([2, 3, 2], [3, 5, 7])
        23

    Complexity: O(n log M) where M is the product of moduli.
    """
    if not isinstance(remainders, list) or not isinstance(moduli, list):
        raise TypeError("remainders and moduli must be lists.")

    if not remainders:
        raise ValueError("Lists cannot be empty.")

    if len(remainders) != len(moduli):
        raise ValueError("remainders and moduli must have the same length.")

    if not all(isinstance(r, int) for r in remainders):
        raise TypeError("All remainders must be integers.")

    if not all(isinstance(m, int) and m > 0 for m in moduli):
        raise TypeError("All moduli must be positive integers.")

    # Check pairwise coprime
    for i in range(len(moduli)):

        for j in range(i + 1, len(moduli)):

            if math.gcd(moduli[i], moduli[j]) != 1:
                raise ValueError("All moduli must be pairwise coprime.")

    M = 1

    for m in moduli:
        M *= m

    x = 0

    for r, m in zip(remainders, moduli):
        M_i = M // m
        # Extended Euclidean to find inverse of M_i mod m
        y = modular_inverse(M_i, m)
        x += r * M_i * y

    return x % M


def is_narcissistic_number(n: int) -> bool:
    """Checks if n is a narcissistic (Armstrong) number.

    An m-digit number where the sum of each digit raised to the m-th
    power equals the number itself.

    Args:
        n: A non-negative integer.

    Returns:
        True if n is narcissistic, False otherwise.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> is_narcissistic_number(153)
        True
        >>> is_narcissistic_number(10)
        False

    Complexity: O(m) where m = number of digits
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    digits = [int(d) for d in str(n)]
    m = len(digits)
    return sum(d ** m for d in digits) == n


def stern_brocot(n: int) -> List[int]:
    """Generates the first n elements of the Stern-Brocot sequence.

    The sequence is: s(0)=0, s(1)=1, s(2n)=s(n), s(2n+1)=s(n)+s(n+1).

    Args:
        n: Number of elements to generate (>= 1).

    Returns:
        A list of the first n elements.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Example:
        >>> stern_brocot(10)
        [0, 1, 1, 2, 1, 3, 2, 3, 1, 4]

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    if n == 1:
        return [0]

    seq = [0, 1]

    while len(seq) < n:
        idx = len(seq) // 2

        if len(seq) % 2 == 0:
            seq.append(seq[idx])
        else:
            seq.append(seq[idx] + seq[idx + 1])

    return seq[:n]


def is_square_number(n: int) -> bool:
    """Checks whether a non-negative integer is a perfect square.

    Args:
        n: Non-negative integer.

    Returns:
        True if n is a perfect square.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> is_square_number(49)
        True

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    import math

    root = math.isqrt(n)
    return root * root == n


def is_triangular_number(n: int) -> bool:
    """Checks whether a non-negative integer is a triangular number.

    T_k = k(k+1)/2. Solves 8n+1 being a perfect square.

    Args:
        n: Non-negative integer.

    Returns:
        True if n is a triangular number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> is_triangular_number(10)
        True

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    import math

    disc = 8 * n + 1
    root = math.isqrt(disc)
    return root * root == disc


def is_power_of_two(n: int) -> bool:
    """Checks whether a positive integer is a power of two.

    Args:
        n: Positive integer.

    Returns:
        True if n is a power of two.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Example:
        >>> is_power_of_two(64)
        True

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n <= 0:
        raise ValueError("n must be positive.")

    return (n & (n - 1)) == 0


def digital_sum(n: int) -> int:
    """Computes the sum of digits of an integer.

    For negative integers, the sign is ignored.

    Args:
        n: An integer.

    Returns:
        Sum of its decimal digits.

    Raises:
        TypeError: If n is not an integer.

    Example:
        >>> digital_sum(12345)
        15

    Complexity: O(d) where d is the number of digits
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    return sum(int(d) for d in str(abs(n)))


def count_digits(n: int) -> int:
    """Counts the number of decimal digits of an integer.

    For negative integers, the sign is ignored.

    Args:
        n: An integer.

    Returns:
        Number of digits.

    Raises:
        TypeError: If n is not an integer.

    Example:
        >>> count_digits(12345)
        5

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    return len(str(abs(n)))


def is_perfect_power(n: int) -> bool:
    """Check if n can be expressed as a^b where a, b are integers and b > 1.

    Args:
        n: Positive integer to check.

    Returns:
        True if n is a perfect power, False otherwise.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is less than 1.

    Example:
        >>> is_perfect_power(8)
        True
        >>> is_perfect_power(10)
        False

    Complexity: O(log(n)^2)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be at least 1.")

    if n == 1:
        return True


    for b in range(2, n.bit_length() + 1):
        a = round(n ** (1.0 / b))

        for candidate in (a - 1, a, a + 1):

            if candidate >= 2 and candidate ** b == n:
                return True

    return False


def is_cube_number(n: int) -> bool:
    """Check if n is a perfect cube.

    Args:
        n: Non-negative integer to check.

    Returns:
        True if n is a perfect cube, False otherwise.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> is_cube_number(27)
        True
        >>> is_cube_number(10)
        False

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return True

    cr = round(n ** (1.0 / 3.0))

    for candidate in (cr - 1, cr, cr + 1):

        if candidate >= 0 and candidate ** 3 == n:
            return True

    return False


def is_pronic_number(n: int) -> bool:
    """Check if n is a pronic (oblong) number: n = k * (k + 1) for some k >= 0.

    Pronic numbers: 0, 2, 6, 12, 20, 30, 42, ...

    Args:
        n: Non-negative integer to check.

    Returns:
        True if n is pronic, False otherwise.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> is_pronic_number(6)
        True
        >>> is_pronic_number(7)
        False

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    import math

    k = int(math.isqrt(n))

    return k * (k + 1) == n


def is_automorphic_number(n: int) -> bool:
    """Check if n is automorphic: n² ends with n in decimal representation.

    Examples: 1, 5, 6, 25, 76, 376, 625, ...

    Args:
        n: Non-negative integer to check.

    Returns:
        True if n is automorphic, False otherwise.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> is_automorphic_number(76)
        True
        >>> is_automorphic_number(77)
        False

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    n_str = str(n)
    sq_str = str(n * n)

    return sq_str.endswith(n_str)


def multiplicative_persistence(n: int) -> int:
    """Count the multiplicative persistence of n.

    The number of times you must multiply the digits of n to reach
    a single digit.

    Args:
        n: Non-negative integer.

    Returns:
        Number of multiplication steps.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> multiplicative_persistence(39)
        3
        >>> multiplicative_persistence(999)
        4

    Complexity: O(log(n) * steps)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    steps = 0

    while n >= 10:
        product = 1

        for ch in str(n):
            product *= int(ch)

        n = product
        steps += 1

    return steps


def is_happy_number(n: int) -> bool:
    """Check if n is a happy number.

    A happy number eventually reaches 1 when replaced by the sum
    of the squares of its digits repeatedly. A number that never
    reaches 1 enters a cycle.

    Args:
        n: Positive integer to check.

    Returns:
        True if n is a happy number, False otherwise.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Example:
        >>> is_happy_number(19)
        True
        >>> is_happy_number(2)
        False

    Complexity: O(log(n) * cycle_length)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n <= 0:
        raise ValueError("n must be positive.")

    seen = set()

    while n != 1 and n not in seen:
        seen.add(n)
        n = sum(int(d) ** 2 for d in str(n))

    return n == 1


def digital_root(n: int) -> int:
    """Calculate the digital root of n.

    The digital root is the single-digit value obtained by
    repeatedly summing the digits of n.

    Args:
        n: Non-negative integer.

    Returns:
        Single-digit digital root.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> digital_root(493)
        7
        >>> digital_root(0)
        0

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 0

    return 1 + (n - 1) % 9


def collatz_steps(n: int) -> int:
    """Count steps to reach 1 in the Collatz sequence.

    Rules: if n is even → n/2, if odd → 3n+1. Repeat until n == 1.

    Args:
        n: Positive integer.

    Returns:
        Number of steps to reach 1.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Example:
        >>> collatz_steps(6)
        8
        >>> collatz_steps(1)
        0

    Complexity: O(steps) — conjectured to always terminate
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n <= 0:
        raise ValueError("n must be positive.")

    steps = 0

    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        steps += 1

    return steps


def additive_persistence(n: int) -> int:
    """Count the additive persistence of n.

    The number of times you must sum the digits of n to reach
    a single digit (the digital root).

    Args:
        n: Non-negative integer.

    Returns:
        Number of addition steps.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> additive_persistence(199)
        3
        >>> additive_persistence(5)
        0

    Complexity: O(log(n) * steps)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    steps = 0

    while n >= 10:
        n = sum(int(d) for d in str(n))
        steps += 1

    return steps


def count_divisors(n: int) -> int:
    """Count the number of positive divisors of n.

    Args:
        n: Positive integer.

    Returns:
        Number of divisors.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Example:
        >>> count_divisors(12)
        6
        >>> count_divisors(7)
        2

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n <= 0:
        raise ValueError("n must be positive.")

    count = 0
    i = 1

    while i * i <= n:

        if n % i == 0:
            count += 1

            if i != n // i:
                count += 1

        i += 1

    return count


def is_sphenic_number(n: int) -> bool:
    """Check if n is a sphenic number (product of exactly 3 distinct primes).

    Examples: 30 = 2·3·5, 66 = 2·3·11.

    Args:
        n: Positive integer.

    Returns:
        True if n is sphenic, False otherwise.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Example:
        >>> is_sphenic_number(30)
        True
        >>> is_sphenic_number(12)
        False

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n <= 0:
        raise ValueError("n must be positive.")

    factors = []
    temp = n
    i = 2

    while i * i <= temp and len(factors) <= 3:

        if temp % i == 0:
            count = 0

            while temp % i == 0:
                temp //= i
                count += 1

            if count != 1:
                return False

            factors.append(i)

        i += 1

    if temp > 1:
        factors.append(temp)

    return len(factors) == 3


def number_of_distinct_prime_factors(n: int) -> int:
    """Count the number of distinct prime factors of n (ω(n)).

    Args:
        n: Positive integer (≥ 2).

    Returns:
        Number of distinct prime factors.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 2.

    Example:
        >>> number_of_distinct_prime_factors(12)
        2
        >>> number_of_distinct_prime_factors(30)
        3

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 2:
        raise ValueError("n must be at least 2.")

    count = 0
    temp = n
    i = 2

    while i * i <= temp:

        if temp % i == 0:
            count += 1

            while temp % i == 0:
                temp //= i

        i += 1

    if temp > 1:
        count += 1

    return count


def sum_of_squares_of_digits(n: int) -> int:
    """Calculate the sum of squares of the digits of n.

    Args:
        n: Non-negative integer.

    Returns:
        Sum of squared digits.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> sum_of_squares_of_digits(19)
        82
        >>> sum_of_squares_of_digits(0)
        0

    Complexity: O(d) where d is the number of digits
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    return sum(int(d) ** 2 for d in str(n))


def sum_proper_divisors(n: int) -> int:
    """Calculate the sum of proper divisors of n (all divisors except n itself).

    Also known as the aliquot sum s(n).

    Args:
        n: Positive integer.

    Returns:
        Sum of proper divisors.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is not positive.

    Example:
        >>> sum_proper_divisors(12)
        16
        >>> sum_proper_divisors(1)
        0

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n <= 0:
        raise ValueError("n must be positive.")

    if n == 1:
        return 0

    total = 1
    i = 2

    while i * i <= n:

        if n % i == 0:
            total += i

            if i != n // i:
                total += n // i

        i += 1

    return total


def sum_of_cubes_of_digits(n: int) -> int:
    """Calculate the sum of cubes of the digits of n.

    Args:
        n: Non-negative integer.

    Returns:
        Sum of cubes of each digit.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> sum_of_cubes_of_digits(123)
        36

    Complexity: O(d) where d is the number of digits
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    total = 0

    for ch in str(n):
        total += int(ch) ** 3

    return total


def lucas_number(n: int) -> int:
    """Calculate the n-th Lucas number.

    L(0)=2, L(1)=1, L(n)=L(n-1)+L(n-2).

    Args:
        n: Non-negative index.

    Returns:
        The n-th Lucas number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> lucas_number(5)
        11

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 2

    if n == 1:
        return 1

    a, b = 2, 1

    for _ in range(2, n + 1):
        a, b = b, a + b

    return b


def is_achilles_number(n: int) -> bool:
    """Check if n is an Achilles number.

    An Achilles number is powerful (p²|n for every prime p|n)
    but not a perfect power.

    Args:
        n: Positive integer to check.

    Returns:
        True if n is an Achilles number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Example:
        >>> is_achilles_number(72)
        True
        >>> is_achilles_number(36)
        False

    Complexity: O(√n · log n)
    """
    import math

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be a positive integer.")

    if n == 1:
        return False

    # Check powerful: every prime factor p must have p² | n
    temp = n
    exponents = []
    d = 2

    while d * d <= temp:

        if temp % d == 0:
            exp = 0

            while temp % d == 0:
                exp += 1
                temp //= d

            if exp < 2:
                return False

            exponents.append(exp)

        d += 1

    if temp > 1:
        # remaining prime factor with exponent 1 -> not powerful
        return False

    # Check not a perfect power: gcd of all exponents must be 1
    g = exponents[0]

    for e in exponents[1:]:
        g = math.gcd(g, e)

    return g == 1


def digit_count(n: int) -> int:
    """Count the number of digits in a non-negative integer.

    Args:
        n: Non-negative integer.

    Returns:
        Number of digits.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> digit_count(12345)
        5
        >>> digit_count(0)
        1

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 1

    import math

    return int(math.log10(n)) + 1


def tribonacci_number(n: int) -> int:
    """Calculate the n-th tribonacci number.

    T(0)=0, T(1)=0, T(2)=1, T(n)=T(n-1)+T(n-2)+T(n-3).

    Args:
        n: Non-negative index.

    Returns:
        The n-th tribonacci number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> tribonacci_number(7)
        13

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0 or n == 1:
        return 0

    if n == 2:
        return 1

    a, b, c = 0, 0, 1

    for _ in range(3, n + 1):
        a, b, c = b, c, a + b + c

    return c


def jacobsthal_number(n: int) -> int:
    """Calculate the n-th Jacobsthal number.

    J(0)=0, J(1)=1, J(n)=J(n-1)+2·J(n-2).

    Args:
        n: Non-negative index.

    Returns:
        The n-th Jacobsthal number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> jacobsthal_number(6)
        21

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 0

    if n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, b + 2 * a

    return b


def pell_number(n: int) -> int:
    """Calculate the n-th Pell number.

    P(0)=0, P(1)=1, P(n)=2·P(n-1)+P(n-2).

    Args:
        n: Non-negative index.

    Returns:
        The n-th Pell number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> pell_number(6)
        70

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 0

    if n == 1:
        return 1

    a, b = 0, 1

    for _ in range(2, n + 1):
        a, b = b, 2 * b + a

    return b


def motzkin_number(n: int) -> int:
    """Return the *n*-th Motzkin number.

    Motzkin numbers count the number of different ways of drawing
    non-intersecting chords among *n* points on a circle.

    Recurrence: (n + 2) · M(n) = (2n + 1) · M(n−1) + 3(n − 1) · M(n−2),
    with M(0) = M(1) = 1.

    Args:
        n: Non-negative index.

    Returns:
        The *n*-th Motzkin number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> motzkin_number(5)
        21

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n <= 1:
        return 1

    a, b = 1, 1

    for i in range(2, n + 1):
        a, b = b, ((2 * i + 1) * b + 3 * (i - 1) * a) // (i + 2)

    return b


def pentagonal_number(n: int) -> int:
    """Return the *n*-th pentagonal number.

    P(n) = n · (3n − 1) / 2.  The sequence starts 0, 1, 5, 12, 22, …

    Args:
        n: Non-negative index.

    Returns:
        The *n*-th pentagonal number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> pentagonal_number(5)
        35

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    return n * (3 * n - 1) // 2


def bell_number(n: int) -> int:
    """Return the *n*-th Bell number.

    The Bell number B(n) counts the number of partitions of a
    set with *n* elements.  Computed via the Bell triangle.

    Args:
        n: Non-negative index.

    Returns:
        The *n*-th Bell number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> bell_number(5)
        52

    Complexity: O(n²)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 1

    prev = [1]

    for i in range(1, n + 1):
        curr = [prev[-1]]

        for j in range(1, i + 1):
            curr.append(curr[j - 1] + prev[j - 1])

        prev = curr

    return prev[0]


def narayana_number(n: int, k: int) -> int:
    """Return the Narayana number N(n, k).

    N(n, k) = C(n, k) · C(n, k−1) / n,  where C is the binomial
    coefficient.  Narayana numbers refine the Catalan numbers and
    count the number of paths that have exactly *k* peaks.

    Args:
        n: Row index (must be ≥ 1).
        k: Column index (must be 1 ≤ k ≤ n).

    Returns:
        The Narayana number N(n, k).

    Raises:
        TypeError: If n or k is not an integer.
        ValueError: If n < 1 or k is outside [1, n].

    Example:
        >>> narayana_number(4, 2)
        6

    Complexity: O(n)
    """
    import math as _math

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if n < 1:
        raise ValueError("n must be at least 1.")

    if not 1 <= k <= n:
        raise ValueError("k must be between 1 and n inclusive.")

    return _math.comb(n, k) * _math.comb(n, k - 1) // n


def delannoy_number(m: int, n: int) -> int:
    """Return the central Delannoy number D(m, n).

    D(m, n) counts the paths from (0,0) to (m,n) using steps
    (1,0), (0,1), and (1,1).

    Recurrence: D(m, n) = D(m−1, n) + D(m, n−1) + D(m−1, n−1),
    with D(0, ·) = D(·, 0) = 1.

    Args:
        m: Row index (must be ≥ 0).
        n: Column index (must be ≥ 0).

    Returns:
        The Delannoy number D(m, n).

    Raises:
        TypeError: If m or n is not an integer.
        ValueError: If m or n is negative.

    Example:
        >>> delannoy_number(3, 3)
        63

    Complexity: O(m · n)
    """
    if not isinstance(m, int):
        raise TypeError("m must be an integer.")

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if m < 0:
        raise ValueError("m must be non-negative.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    prev = [1] * (n + 1)

    for i in range(1, m + 1):
        curr = [1] * (n + 1)

        for j in range(1, n + 1):
            curr[j] = curr[j - 1] + prev[j] + prev[j - 1]

        prev = curr

    return prev[n]


def schroeder_number(n: int) -> int:
    """Return the *n*-th large Schröder number.

    Schröder numbers count the number of lattice paths from
    (0,0) to (n,n) that do not go above the diagonal, using
    steps (1,0), (0,1), and (1,1).

    Recurrence: S(n) = ((6n − 3) · S(n−1) − (n − 2) · S(n−2)) / (n + 1),
    with S(0) = 1, S(1) = 2.

    Args:
        n: Non-negative index.

    Returns:
        The *n*-th large Schröder number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> schroeder_number(4)
        90

    Complexity: O(n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 1

    if n == 1:
        return 2

    a, b = 1, 2

    for i in range(2, n + 1):
        a, b = b, ((6 * i - 3) * b - (i - 2) * a) // (i + 1)

    return b


def eulerian_number(n: int, k: int) -> int:
    """Return the Eulerian number A(n, k).

    The Eulerian number counts the number of permutations of
    {1, …, n} with exactly *k* ascents.

    Recurrence: A(n, k) = (k+1)·A(n−1, k) + (n−k)·A(n−1, k−1),
    with A(0, 0) = 1.

    Args:
        n: Permutation size (must be ≥ 0).
        k: Number of ascents (must be 0 ≤ k < n, or k = 0 if n = 0).

    Returns:
        The Eulerian number A(n, k).

    Raises:
        TypeError: If n or k is not an integer.
        ValueError: If n < 0 or k is out of range.

    Example:
        >>> eulerian_number(4, 1)
        11

    Complexity: O(n · k)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        if k != 0:
            raise ValueError("k must be 0 when n is 0.")

        return 1

    if not 0 <= k < n:
        raise ValueError("k must be in [0, n-1).")

    prev = [1]

    for i in range(1, n + 1):
        curr = [0] * i

        for j in range(i):
            left = (j + 1) * prev[j] if j < len(prev) else 0
            right = (i - j) * prev[j - 1] if j > 0 and j - 1 < len(prev) else 0
            curr[j] = left + right

        prev = curr

    return prev[k]


def stirling_number_second(n: int, k: int) -> int:
    """Return the Stirling number of the second kind S(n, k).

    S(n, k) counts the number of ways to partition a set of
    *n* elements into *k* non-empty subsets.

    Recurrence: S(n, k) = k · S(n−1, k) + S(n−1, k−1),
    with S(n, 0) = 0 for n ≥ 1, S(0, 0) = 1.

    Args:
        n: Set size (must be ≥ 0).
        k: Number of subsets (must be 0 ≤ k ≤ n).

    Returns:
        Stirling number of the second kind.

    Raises:
        TypeError: If n or k is not an integer.
        ValueError: If n < 0 or k is out of range.

    Example:
        >>> stirling_number_second(4, 2)
        7

    Complexity: O(n · k)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if not isinstance(k, int):
        raise TypeError("k must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if not 0 <= k <= n:
        raise ValueError("k must be in [0, n].")

    if k == 0:
        return 1 if n == 0 else 0

    if k == n:
        return 1

    prev = [0] * (k + 1)
    prev[0] = 1

    for _ in range(1, n + 1):
        curr = [0] * (k + 1)

        for j in range(1, k + 1):
            curr[j] = j * prev[j] + prev[j - 1]

        prev = curr

    return prev[k]


def partition_number(n: int) -> int:
    """Return the number of integer partitions of *n*.

    p(n) counts the number of ways to write *n* as a sum of
    positive integers, disregarding order.

    Args:
        n: Non-negative integer.

    Returns:
        The partition number p(n).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n is negative.

    Example:
        >>> partition_number(5)
        7

    Complexity: O(n²)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for j in range(i, n + 1):
            dp[j] += dp[j - i]

    return dp[n]


def continued_fraction_expansion(
    numerator: int,
    denominator: int,
) -> list[int]:
    """Compute the continued fraction expansion of a rational number.

    Args:
        numerator: Integer numerator.
        denominator: Integer denominator (non-zero).

    Returns:
        List of continued fraction coefficients [a₀, a₁, a₂, …].

    Raises:
        TypeError: If inputs are not integers.
        ValueError: If *denominator* is zero.

    Example:
        >>> continued_fraction_expansion(355, 113)
        [3, 7, 16]

    Complexity: O(log(min(numerator, denominator)))
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("numerator and denominator must be integers")

    if denominator == 0:
        raise ValueError("denominator must be non-zero")

    a, b = numerator, denominator

    if b < 0:
        a, b = -a, -b

    coeffs: list[int] = []

    while b != 0:
        q = a // b

        if a < 0 and a % b != 0:
            q -= 1

        coeffs.append(q)
        a, b = b, a - q * b

    return coeffs


def convergents(cf: list[int]) -> list[tuple[int, int]]:
    """Compute the convergents of a continued fraction.

    Args:
        cf: Continued fraction coefficients [a₀, a₁, a₂, …].

    Returns:
        List of ``(numerator, denominator)`` tuples for each convergent,
        from the 0th to the last.

    Raises:
        TypeError: If *cf* is not a list of integers.
        ValueError: If *cf* is empty.

    Example:
        >>> convergents([3, 7, 16])
        [(3, 1), (22, 7), (355, 113)]

    Complexity: O(n), n = len(cf)
    """
    if not isinstance(cf, list):
        raise TypeError("cf must be a list")

    if not cf:
        raise ValueError("cf must not be empty")

    for v in cf:

        if not isinstance(v, int):
            raise TypeError("All elements of cf must be integers")

    result: list[tuple[int, int]] = []
    h_prev, h_curr = 0, 1
    k_prev, k_curr = 1, 0

    for a in cf:
        h_prev, h_curr = h_curr, a * h_curr + h_prev
        k_prev, k_curr = k_curr, a * k_curr + k_prev
        result.append((h_curr, k_curr))

    return result


def discrete_logarithm(g: int, h: int, p: int) -> int:
    """Compute the discrete logarithm: find *x* such that g^x ≡ h (mod p).

    Uses the baby-step giant-step algorithm.

    Args:
        g: Base.
        h: Target value.
        p: Modulus (should be prime for guaranteed result).

    Returns:
        The exponent *x*.

    Raises:
        TypeError: If arguments are not integers.
        ValueError: If no solution is found.

    Example:
        >>> discrete_logarithm(2, 8, 13)
        3

    Complexity: O(√p) time and space.
    """
    import math

    for name, val in (("g", g), ("h", h), ("p", p)):

        if not isinstance(val, int):
            raise TypeError(f"{name} must be an integer")

    m = math.isqrt(p) + 1

    # Baby step: g^j mod p for j = 0..m-1
    table: dict[int, int] = {}
    power = 1

    for j in range(m):
        table[power] = j
        power = (power * g) % p

    # Giant step: g^(-m) mod p
    factor = pow(g, -m, p)
    gamma = h

    for i in range(m):

        if gamma in table:
            return i * m + table[gamma]

        gamma = (gamma * factor) % p

    raise ValueError("No discrete logarithm found")


def egyptian_fraction(numerator: int, denominator: int) -> list[int]:
    """Decompose a fraction into a sum of distinct unit fractions.

    Uses the greedy (Sylvester-Fibonacci) algorithm:
    find the smallest *n* such that 1/n ≤ a/b, subtract, repeat.

    Args:
        numerator: Positive integer numerator.
        denominator: Positive integer denominator.

    Returns:
        List of denominators of the unit fractions.

    Raises:
        TypeError: If arguments are not integers.
        ValueError: If numerator or denominator ≤ 0.

    Example:
        >>> egyptian_fraction(3, 7)
        [3, 11, 231]

    Complexity: O(numerator) average.
    """
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("numerator and denominator must be integers")

    if numerator <= 0 or denominator <= 0:
        raise ValueError("numerator and denominator must be positive")

    import math

    result: list[int] = []
    a, b = numerator, denominator

    while a > 0:
        # Ceiling of b/a
        n = (b + a - 1) // a
        result.append(n)
        a = a * n - b
        b = b * n

        g = math.gcd(abs(a), b)

        if g > 1:
            a //= g
            b //= g

    return result


def is_fibonacci_number(n: int) -> bool:
    """Check whether a non-negative integer belongs to the Fibonacci sequence.

    Description:
        Uses the property that *n* is Fibonacci if and only if
        5n² + 4 or 5n² − 4 is a perfect square.

    Args:
        n: Non-negative integer to test.

    Returns:
        True if *n* is a Fibonacci number.

    Raises:
        TypeError: If *n* is not an integer.
        ValueError: If *n* is negative.

    Usage Example:
        >>> is_fibonacci_number(13)
        True
        >>> is_fibonacci_number(14)
        False

    Complexity: O(1)
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer")

    if n < 0:
        raise ValueError("n must be non-negative")

    def _is_perfect_square(x: int) -> bool:
        s = math.isqrt(x)
        return s * s == x

    return _is_perfect_square(5 * n * n + 4) or _is_perfect_square(5 * n * n - 4)


# ---------------------------------------------------------------------------
# Partition function, Liouville, Carmichael (Spiegel Ch. Number Theory)
# ---------------------------------------------------------------------------


def partition_function(n: int) -> int:
    """Computes the number of integer partitions p(n).

    p(n) is the number of ways to write n as a sum of positive integers
    (order doesn't matter).

    Args:
        n: Non-negative integer.

    Returns:
        p(n).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> partition_function(5)
        7
        >>> partition_function(10)
        42

    Complexity: O(n^2)
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for k in range(1, n + 1):

        for i in range(k, n + 1):
            dp[i] += dp[i - k]

    return dp[n]


def sum_of_squares_count(n: int) -> int:
    """Counts the number of representations of n as a sum of two squares.

    r2(n) counts ordered pairs (a, b) with a² + b² = n (including signs and order).

    Args:
        n: Non-negative integer.

    Returns:
        Number of representations r2(n).

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Example:
        >>> sum_of_squares_count(5)
        8
        >>> sum_of_squares_count(1)
        4

    Complexity: O(√n)
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if n == 0:
        return 1

    count = 0

    for a in range(int(math.isqrt(n)) + 1):
        b_sq = n - a * a

        if b_sq < 0:
            break

        b = math.isqrt(b_sq)

        if b * b == b_sq and b >= a:

            if a == 0 or b == 0:
                count += 4  # Signs only (not both zero)
            elif a == b:
                count += 4
            else:
                count += 8  # All permutations of signs and order

    return count


def squarefree_part(n: int) -> int:
    """Computes the squarefree part of n.

    The squarefree part is n divided by the largest perfect square that divides it.

    Args:
        n: Positive integer.

    Returns:
        Squarefree part.

    Example:
        >>> squarefree_part(12)
        3
        >>> squarefree_part(7)
        7

    Complexity: O(√n)
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be positive.")

    result = n
    d = 2

    while d * d <= result:

        while result % (d * d) == 0:
            result //= (d * d)

        d += 1

    return result


def primitive_root(p: int) -> int:
    """Finds the smallest primitive root modulo p (p must be prime).

    A primitive root g has order p-1 modulo p, meaning g generates
    the multiplicative group (Z/pZ)*.

    Args:
        p: Prime number > 1.

    Returns:
        Smallest primitive root.

    Raises:
        TypeError: If p is not an integer.
        ValueError: If p < 2 or p is not prime.

    Example:
        >>> primitive_root(7)
        3
        >>> primitive_root(11)
        2

    Complexity: O(p * √p) worst case.
    """
    if not isinstance(p, int) or isinstance(p, bool):
        raise TypeError("p must be an integer.")

    if p < 2:
        raise ValueError("p must be >= 2.")

    # Quick primality check
    if p == 2:
        return 1

    if p % 2 == 0:
        raise ValueError("p must be prime.")

    for i in range(3, int(math.isqrt(p)) + 1, 2):

        if p % i == 0:
            raise ValueError("p must be prime.")

    phi = p - 1
    # Find prime factors of phi
    factors = set()
    temp = phi
    d = 2

    while d * d <= temp:

        if temp % d == 0:
            factors.add(d)

            while temp % d == 0:
                temp //= d

        d += 1

    if temp > 1:
        factors.add(temp)

    # Test candidates
    for g in range(2, p):
        is_root = True

        for f in factors:

            if pow(g, phi // f, p) == 1:
                is_root = False
                break

        if is_root:
            return g

    raise ValueError("No primitive root found (should not happen for primes).")


def carmichael_lambda(n: int) -> int:
    """Compute the Carmichael function λ(n).

    Description:
        The smallest positive integer *m* such that a^m ≡ 1 (mod n) for
        every integer *a* coprime to *n*.  Also known as the reduced
        totient function or least universal exponent.

    Args:
        n: Positive integer ≥ 1.

    Returns:
        λ(n).

    Raises:
        TypeError: If *n* is not an integer.
        ValueError: If *n* < 1.

    Usage Example:
        >>> carmichael_lambda(8)
        2
        >>> carmichael_lambda(15)
        4

    Complexity: O(√n)
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    if n < 1:
        raise ValueError("n must be >= 1.")

    if n == 1:
        return 1

    def _lcm(a: int, b: int) -> int:
        return a * b // math.gcd(a, b)

    def _lambda_prime_power(p: int, e: int) -> int:
        """λ(p^e) for prime p and exponent e."""

        if p == 2:
            # λ(2) = 1, λ(4) = 2, λ(2^e) = 2^(e-2) for e >= 3
            if e == 1:
                return 1

            if e == 2:
                return 2

            return 2 ** (e - 2)

        return (p - 1) * p ** (e - 1)  # φ(p^e) = λ(p^e) for odd primes

    # Factor n and compute lcm of λ for each prime power
    result = 1
    temp = n
    d = 2

    while d * d <= temp:

        if temp % d == 0:
            e = 0

            while temp % d == 0:
                e += 1
                temp //= d

            result = _lcm(result, _lambda_prime_power(d, e))

        d += 1

    if temp > 1:
        result = _lcm(result, _lambda_prime_power(temp, 1))

    return result


def is_lychrel_candidate(n: int, max_iterations: int = 50) -> bool:
    """Check if a number is a Lychrel candidate.

    Description:
        A Lychrel number never forms a palindrome through the
        iterative process of reversing digits and adding.  Since
        this is unproven for any base-10 number, this function tests
        up to *max_iterations* steps.  If no palindrome is found,
        the number is considered a *candidate*.

    Args:
        n: Non-negative integer.
        max_iterations: Maximum reverse-and-add steps (default 50).

    Returns:
        True if *n* does not produce a palindrome within the limit.

    Raises:
        TypeError: If *n* is not an integer.
        ValueError: If *n* < 0 or *max_iterations* < 1.

    Usage Example:
        >>> is_lychrel_candidate(196)
        True
        >>> is_lychrel_candidate(56)
        False

    Complexity: O(max_iterations × d) where d is the digit count.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    if not isinstance(max_iterations, int) or max_iterations < 1:
        raise ValueError("max_iterations must be a positive integer.")

    current = n

    for _ in range(max_iterations):
        current = current + int(str(current)[::-1])
        s = str(current)

        if s == s[::-1]:
            return False

    return True


def digit_factorial_sum(n: int) -> int:
    """Compute the sum of factorials of the digits of n.

    Description:
        For each digit *d* of *n*, computes d! and sums them.
        Numbers equal to their digit factorial sum are called
        factorions (e.g. 145 = 1! + 4! + 5!).

    Args:
        n: Non-negative integer.

    Returns:
        Sum of digit factorials.

    Raises:
        TypeError: If *n* is not an integer.
        ValueError: If *n* is negative.

    Usage Example:
        >>> digit_factorial_sum(145)
        145
        >>> digit_factorial_sum(123)
        9

    Complexity: O(d) where d is the number of digits.
    """
    if not isinstance(n, int) or isinstance(n, bool):
        raise TypeError("n must be an integer.")

    if n < 0:
        raise ValueError("n must be non-negative.")

    factorials = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

    return sum(factorials[int(d)] for d in str(n))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 16: Number Theory Functions (1 of 3)
# ---------------------------------------------------------------------------

def jacobi_symbol(a: int, n: int) -> int:
    """Compute the Jacobi symbol (a/n).

    Generalization of the Legendre symbol to odd positive n.

    Args:
        a: Integer.
        n: Odd positive integer ≥ 3.

    Returns:
        -1, 0, or 1.

    Raises:
        TypeError: If a or n is not an integer.
        ValueError: If n < 3 or n is even.

    Usage Example:
        >>> jacobi_symbol(2, 7)
        1

    Complexity: O(log(n)²)
    """
    if not isinstance(a, int) or not isinstance(n, int):
        raise TypeError("a and n must be integers.")
    if n < 3 or n % 2 == 0:
        raise ValueError("n must be an odd positive integer >= 3.")
    a = a % n
    result = 1
    while a != 0:
        while a % 2 == 0:
            a //= 2
            if n % 8 in (3, 5):
                result = -result
        a, n = n, a
        if a % 4 == 3 and n % 4 == 3:
            result = -result
        a = a % n
    return result if n == 1 else 0


def kronecker_symbol(a: int, n: int) -> int:
    """Compute the Kronecker symbol (a|n).

    Extension of the Jacobi symbol to all integers n.

    Args:
        a: Integer.
        n: Integer.

    Returns:
        -1, 0, or 1.

    Raises:
        TypeError: If a or n is not an integer.

    Usage Example:
        >>> kronecker_symbol(2, 7)
        1

    Complexity: O(log(n)²)
    """
    if not isinstance(a, int) or not isinstance(n, int):
        raise TypeError("a and n must be integers.")
    if n == 0:
        return 1 if abs(a) == 1 else 0
    if n == 1:
        return 1
    if n == -1:
        return -1 if a < 0 else 1
    # Factor out sign
    result = 1
    if n < 0:
        n = -n
        if a < 0:
            result = -1
    # Factor out powers of 2
    v = 0
    while n % 2 == 0:
        v += 1
        n //= 2
    if v > 0:
        if a % 2 == 0:
            result = 0
        elif v % 2 == 1 and (a % 8 in (3, 5)):
            result = -result
    if n == 1:
        return result
    return result * jacobi_symbol(a, n)


def legendre_symbol(a: int, p: int) -> int:
    """Compute the Legendre symbol (a/p) for odd prime p.

    Args:
        a: Integer.
        p: Odd prime.

    Returns:
        -1, 0, or 1.

    Raises:
        TypeError: If a or p is not an integer.
        ValueError: If p < 3 or p is even.

    Usage Example:
        >>> legendre_symbol(2, 7)
        1

    Complexity: O(log(p))
    """
    if not isinstance(a, int) or not isinstance(p, int):
        raise TypeError("a and p must be integers.")
    if p < 3 or p % 2 == 0:
        raise ValueError("p must be an odd prime >= 3.")
    a = a % p
    if a == 0:
        return 0
    result = pow(a, (p - 1) // 2, p)
    return result if result <= 1 else -1


def mobius_function(n: int) -> int:
    """Compute the Möbius function μ(n).

    μ(n) = 1 if n is square-free with even number of prime factors,
    -1 if square-free with odd number, 0 if not square-free.

    Args:
        n: Positive integer.

    Returns:
        -1, 0, or 1.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> mobius_function(30)
        -1

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    if n == 1:
        return 1
    count = 0
    temp = n
    for p in range(2, int(temp ** 0.5) + 1):
        if temp % p == 0:
            count += 1
            temp //= p
            if temp % p == 0:
                return 0
    if temp > 1:
        count += 1
    return 1 if count % 2 == 0 else -1


def liouville_lambda(n: int) -> int:
    """Compute the Liouville function λ(n) = (-1)^Ω(n).

    Ω(n) is the number of prime factors of n counted with multiplicity.

    Args:
        n: Positive integer.

    Returns:
        1 or -1.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> liouville_lambda(12)
        -1

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    count = 0
    temp = n
    p = 2
    while p * p <= temp:
        while temp % p == 0:
            count += 1
            temp //= p
        p += 1
    if temp > 1:
        count += 1
    return 1 if count % 2 == 0 else -1


def sum_of_divisors(n: int, k: int = 1) -> int:
    """Compute σ_k(n), the sum of k-th powers of divisors of n.

    Args:
        n: Positive integer.
        k: Power exponent (default 1, giving σ₁ = sum of divisors).

    Returns:
        σ_k(n).

    Raises:
        TypeError: If n or k is not an integer.
        ValueError: If n < 1 or k < 0.

    Usage Example:
        >>> sum_of_divisors(12)
        28

    Complexity: O(√n)
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers.")
    if n < 1:
        raise ValueError("n must be positive.")
    if k < 0:
        raise ValueError("k must be non-negative.")
    total = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            total += i ** k
            other = n // i
            if other != i:
                total += other ** k
    return total


def number_of_divisors(n: int) -> int:
    """Compute d(n) = σ₀(n), the number of divisors of n.

    Args:
        n: Positive integer.

    Returns:
        Number of divisors.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> number_of_divisors(12)
        6

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    count = 0
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            count += 1
            if n // i != i:
                count += 1
    return count


def is_perfect_number(n: int) -> bool:
    """Check if n is a perfect number (σ₁(n) = 2n).

    Args:
        n: Positive integer.

    Returns:
        True if n is perfect.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> is_perfect_number(28)
        True

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    return sum_of_divisors(n) == 2 * n


def is_abundant_number(n: int) -> bool:
    """Check if n is an abundant number (σ₁(n) > 2n).

    Args:
        n: Positive integer.

    Returns:
        True if n is abundant.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> is_abundant_number(12)
        True

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    return sum_of_divisors(n) > 2 * n


# ---------------------------------------------------------------------------
# Phase 21 – Batch 17: Number Theory Functions (2 of 3)
# ---------------------------------------------------------------------------

def is_deficient_number(n: int) -> bool:
    """Check if n is a deficient number (σ₁(n) < 2n).

    Args:
        n: Positive integer.

    Returns:
        True if n is deficient.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> is_deficient_number(8)
        True

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    return sum_of_divisors(n) < 2 * n


def is_semiprime(n: int) -> bool:
    """Check if n is a semiprime (product of exactly two primes).

    Args:
        n: Positive integer ≥ 2.

    Returns:
        True if n is a semiprime.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 2.

    Usage Example:
        >>> is_semiprime(15)
        True

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 2:
        raise ValueError("n must be >= 2.")
    count = 0
    temp = n
    p = 2
    while p * p <= temp:
        while temp % p == 0:
            count += 1
            temp //= p
            if count > 2:
                return False
        p += 1
    if temp > 1:
        count += 1
    return count == 2


def is_square_free(n: int) -> bool:
    """Check if n is square-free (no prime factor appears more than once).

    Args:
        n: Positive integer.

    Returns:
        True if n is square-free.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> is_square_free(30)
        True

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    if n == 1:
        return True
    p = 2
    while p * p <= n:
        if n % (p * p) == 0:
            return False
        p += 1
    return True


def is_powerful_number(n: int) -> bool:
    """Check if n is a powerful number (every prime factor appears ≥ 2 times).

    Args:
        n: Positive integer.

    Returns:
        True if n is powerful.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> is_powerful_number(72)
        True

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    if n == 1:
        return True
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            count = 0
            while temp % p == 0:
                count += 1
                temp //= p
            if count < 2:
                return False
        p += 1
    return temp == 1


def is_smith_number(n: int) -> bool:
    """Check if n is a Smith number.

    A Smith number is a composite where the digit sum equals the sum
    of digit sums of its prime factors (with multiplicity).

    Args:
        n: Integer ≥ 2.

    Returns:
        True if n is a Smith number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 2.

    Usage Example:
        >>> is_smith_number(22)
        True

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 2:
        raise ValueError("n must be >= 2.")

    def _digit_sum(k: int) -> int:
        return sum(int(d) for d in str(k))

    # Must be composite
    if n < 4:
        return False
    temp = n
    p = 2
    is_prime_flag = True
    factor_digit_sum = 0
    while p * p <= temp:
        while temp % p == 0:
            is_prime_flag = False
            factor_digit_sum += _digit_sum(p)
            temp //= p
        p += 1
    if temp > 1:
        if is_prime_flag:
            return False
        factor_digit_sum += _digit_sum(temp)
    return _digit_sum(n) == factor_digit_sum


def is_harshad_number(n: int) -> bool:
    """Check if n is a Harshad (Niven) number (divisible by its digit sum).

    Args:
        n: Positive integer.

    Returns:
        True if n is a Harshad number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> is_harshad_number(18)
        True

    Complexity: O(log n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    digit_sum = sum(int(d) for d in str(n))
    return n % digit_sum == 0


def is_kaprekar_number(n: int) -> bool:
    """Check if n is a Kaprekar number.

    n is Kaprekar if n² can be split into two parts that sum to n
    (right part must not be zero and left part can be empty/0).

    Args:
        n: Positive integer.

    Returns:
        True if n is a Kaprekar number.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> is_kaprekar_number(45)
        True

    Complexity: O(log n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    if n == 1:
        return True
    sq = n * n
    s = str(sq)
    for i in range(1, len(s)):
        right = int(s[i:])
        left = int(s[:i]) if s[:i] else 0
        if right > 0 and left + right == n:
            return True
    return False


def prime_counting_approx(x: float) -> float:
    """Approximate π(x), the number of primes ≤ x, using x/ln(x).

    Args:
        x: Positive real number > 1.

    Returns:
        Approximate prime count.

    Raises:
        TypeError: If x is not numeric.
        ValueError: If x ≤ 1.

    Usage Example:
        >>> round(prime_counting_approx(1000), 1)
        144.8

    Complexity: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric.")
    x = float(x)
    if x <= 1:
        raise ValueError("x must be > 1.")
    return float(x / math.log(x))


def prime_nth_approx(n: int) -> float:
    """Approximate the n-th prime using n·ln(n) + n·ln(ln(n)).

    Args:
        n: Positive integer (the index, 1-based).

    Returns:
        Approximate value of the n-th prime.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> round(prime_nth_approx(100))
        613

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    if n == 1:
        return 2.0
    ln_n = math.log(n)
    return float(n * ln_n + n * math.log(ln_n))


def aliquot_sum(n: int) -> int:
    """Compute the aliquot sum s(n) = σ₁(n) - n (sum of proper divisors).

    Args:
        n: Positive integer.

    Returns:
        Sum of proper divisors.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> aliquot_sum(12)
        16

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    return sum_of_divisors(n) - n


# ---------------------------------------------------------------------------
# Phase 21 – Batch 18: Number Theory Functions (3 of 3)
# ---------------------------------------------------------------------------

def is_amicable_pair(a: int, b: int) -> bool:
    """Check if (a, b) is an amicable pair: s(a) = b and s(b) = a.

    Args:
        a: Positive integer.
        b: Positive integer.

    Returns:
        True if (a, b) is an amicable pair.

    Raises:
        TypeError: If a or b is not an integer.
        ValueError: If a or b < 1 or a == b.

    Usage Example:
        >>> is_amicable_pair(220, 284)
        True

    Complexity: O(√a + √b)
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers.")
    if a < 1 or b < 1:
        raise ValueError("a and b must be positive.")
    if a == b:
        raise ValueError("a and b must be different.")
    return aliquot_sum(a) == b and aliquot_sum(b) == a


def radical(n: int) -> int:
    """Compute the radical of n: product of distinct prime factors.

    rad(n) = Π p for each prime p dividing n.

    Args:
        n: Positive integer.

    Returns:
        Radical of n.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> radical(12)
        6

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    result = 1
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            result *= p
            while temp % p == 0:
                temp //= p
        p += 1
    if temp > 1:
        result *= temp
    return result


def omega_prime(n: int) -> int:
    """Count distinct prime factors ω(n).

    Args:
        n: Positive integer.

    Returns:
        Number of distinct prime factors.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> omega_prime(12)
        2

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    if n == 1:
        return 0
    count = 0
    temp = n
    p = 2
    while p * p <= temp:
        if temp % p == 0:
            count += 1
            while temp % p == 0:
                temp //= p
        p += 1
    if temp > 1:
        count += 1
    return count


def big_omega(n: int) -> int:
    """Count prime factors with multiplicity Ω(n).

    Args:
        n: Positive integer.

    Returns:
        Number of prime factors counted with multiplicity.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 1.

    Usage Example:
        >>> big_omega(12)
        3

    Complexity: O(√n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 1:
        raise ValueError("n must be positive.")
    if n == 1:
        return 0
    count = 0
    temp = n
    p = 2
    while p * p <= temp:
        while temp % p == 0:
            count += 1
            temp //= p
        p += 1
    if temp > 1:
        count += 1
    return count


def is_palindromic_number(n: int) -> bool:
    """Check if n is a palindromic number in base 10.

    Args:
        n: Non-negative integer.

    Returns:
        True if n reads the same forwards and backwards.

    Raises:
        TypeError: If n is not an integer.
        ValueError: If n < 0.

    Usage Example:
        >>> is_palindromic_number(12321)
        True

    Complexity: O(log n)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be non-negative.")
    s = str(n)
    return s == s[::-1]


def coprime(a: int, b: int) -> bool:
    """Check if a and b are coprime (gcd(a, b) = 1).

    Args:
        a: Integer.
        b: Integer.

    Returns:
        True if gcd(a, b) = 1.

    Raises:
        TypeError: If a or b is not an integer.

    Usage Example:
        >>> coprime(8, 15)
        True

    Complexity: O(log(min(a, b)))
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("a and b must be integers.")
    return math.gcd(a, b) == 1
