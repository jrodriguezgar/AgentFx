"""Tests for fxNumeric.number_theory_functions."""


import pytest

from agentfx.fxNumeric import (
    additive_persistence,
    aliquot_sum,
    big_omega,
    carmichael_lambda,
    collatz_steps,
    continued_fraction_expansion,
    convergents,
    coprime,
    delannoy_number,
    digit_count,
    digital_sum,
    discrete_logarithm,
    egyptian_fraction,
    euler_totient,
    eulerian_number,
    is_abundant_number,
    is_achilles_number,
    is_amicable_pair,
    is_automorphic_number,
    is_cube_number,
    is_deficient_number,
    is_happy_number,
    is_harshad_number,
    is_kaprekar_number,
    is_lychrel_candidate,
    is_palindrome_number,
    is_palindromic_number,
    is_perfect_number,
    is_perfect_power,
    is_powerful_number,
    is_pronic_number,
    is_semiprime,
    is_smith_number,
    is_square_free,
    jacobi_symbol,
    jacobsthal_number,
    kronecker_symbol,
    legendre_symbol,
    liouville_lambda,
    lucas_number,
    lucas_sequence,
    mobius_function,
    modular_exponentiation,
    modular_inverse,
    motzkin_number,
    multiplicative_persistence,
    narayana_number,
    next_prime,
    number_of_distinct_prime_factors,
    number_of_divisors,
    omega_prime,
    partition_function,
    pell_number,
    prime_counting_approx,
    prime_nth_approx,
    primitive_root,
    radical,
    schroeder_number,
    squarefree_part,
    stern_brocot,
    stirling_number_second,
    sum_of_cubes_of_digits,
    sum_of_divisors,
    sum_of_squares_count,
    sum_of_squares_of_digits,
    sum_proper_divisors,
    tribonacci_number,
)
from agentfx.fxNumeric.statistics_functions import contraharmonic_mean
from agentfx.fxNumeric.trigonometry_functions import intermediate_point, normalize_angle


class TestNormalizeAngle:

    def test_over_360(self):
        assert normalize_angle(370, 360) == pytest.approx(10.0)

    def test_negative(self):
        assert normalize_angle(-30, 360) == pytest.approx(330.0)

    def test_full_turn_radians(self):
        import math
        assert normalize_angle(7.0) == pytest.approx(7.0 % (2 * math.pi))

    def test_already_in_range(self):
        assert normalize_angle(45, 360) == pytest.approx(45.0)

    def test_invalid_full_turn(self):
        with pytest.raises(ValueError):
            normalize_angle(10, -1)


# ── Number Theory ────────────────────────────────────────────────────────────


class TestEulerTotient:

    @pytest.mark.parametrize("n, expected", [
        (1, 1), (7, 6), (12, 4), (36, 12),
    ])
    def test_values(self, n, expected):
        assert euler_totient(n) == expected

    def test_prime(self):
        assert euler_totient(13) == 12

    def test_invalid(self):
        with pytest.raises(ValueError):
            euler_totient(0)

class TestIsPalindromeNumber:

    @pytest.mark.parametrize("n, expected", [
        (121, True), (123, False), (0, True), (1, True),
        (12321, True), (-121, False),
    ])
    def test_values(self, n, expected):
        assert is_palindrome_number(n) == expected

class TestModularExponentiation:

    def test_basic(self):
        assert modular_exponentiation(2, 10, 1000) == 24

    def test_zero_exponent(self):
        assert modular_exponentiation(5, 0, 7) == 1

    def test_negative_exponent(self):
        with pytest.raises(ValueError):
            modular_exponentiation(2, -1, 5)

class TestModularInverse:

    def test_basic(self):
        assert modular_inverse(3, 7) == 5
        assert (3 * 5) % 7 == 1

    def test_no_inverse(self):
        with pytest.raises(ValueError, match="does not exist"):
            modular_inverse(6, 9)

class TestLucasSequence:

    def test_first_8(self):
        assert lucas_sequence(8) == [2, 1, 3, 4, 7, 11, 18, 29]

    def test_single(self):
        assert lucas_sequence(1) == [2]

    def test_invalid(self):
        with pytest.raises(ValueError):
            lucas_sequence(0)

class TestNextPrime:

    @pytest.mark.parametrize("n, expected", [
        (1, 2), (2, 3), (10, 11), (13, 17), (100, 101),
    ])
    def test_values(self, n, expected):
        assert next_prime(n) == expected

class TestIsAbundantNumber:

    def test_abundant_12(self):
        from agentfx.fxNumeric.number_theory_functions import is_abundant_number
        assert is_abundant_number(12) is True

    def test_not_abundant_10(self):
        from agentfx.fxNumeric.number_theory_functions import is_abundant_number
        assert is_abundant_number(10) is False

    def test_not_abundant_1(self):
        from agentfx.fxNumeric.number_theory_functions import is_abundant_number
        assert is_abundant_number(1) is False

    def test_type_error(self):
        from agentfx.fxNumeric.number_theory_functions import is_abundant_number

        with pytest.raises(TypeError):
            is_abundant_number(12.5)

    def test_value_error(self):
        from agentfx.fxNumeric.number_theory_functions import is_abundant_number

        with pytest.raises(ValueError):
            is_abundant_number(0)

class TestIsDeficientNumber:

    def test_deficient_8(self):
        from agentfx.fxNumeric.number_theory_functions import is_deficient_number
        assert is_deficient_number(8) is True

    def test_not_deficient_12(self):
        from agentfx.fxNumeric.number_theory_functions import is_deficient_number
        assert is_deficient_number(12) is False

    def test_deficient_1(self):
        from agentfx.fxNumeric.number_theory_functions import is_deficient_number
        assert is_deficient_number(1) is True

class TestGoldbachPartition:

    def test_partition_28(self):
        from agentfx.fxNumeric.number_theory_functions import goldbach_partition

        p, q = goldbach_partition(28)
        assert p + q == 28

    def test_partition_100(self):
        from agentfx.fxNumeric.number_theory_functions import goldbach_partition

        p, q = goldbach_partition(100)
        assert p + q == 100

    def test_odd_raises(self):
        from agentfx.fxNumeric.number_theory_functions import goldbach_partition

        with pytest.raises(ValueError):
            goldbach_partition(7)

    def test_small_raises(self):
        from agentfx.fxNumeric.number_theory_functions import goldbach_partition

        with pytest.raises(ValueError):
            goldbach_partition(2)

class TestNthFibonacci:

    def test_fib_0(self):
        from agentfx.fxNumeric.number_theory_functions import nth_fibonacci
        assert nth_fibonacci(0) == 0

    def test_fib_1(self):
        from agentfx.fxNumeric.number_theory_functions import nth_fibonacci
        assert nth_fibonacci(1) == 1

    def test_fib_10(self):
        from agentfx.fxNumeric.number_theory_functions import nth_fibonacci
        assert nth_fibonacci(10) == 55

    def test_fib_20(self):
        from agentfx.fxNumeric.number_theory_functions import nth_fibonacci
        assert nth_fibonacci(20) == 6765

    def test_negative_raises(self):
        from agentfx.fxNumeric.number_theory_functions import nth_fibonacci

        with pytest.raises(ValueError):
            nth_fibonacci(-1)

class TestMobiusFunction:

    def test_one(self):
        from agentfx.fxNumeric.number_theory_functions import mobius_function
        assert mobius_function(1) == 1

    def test_prime(self):
        from agentfx.fxNumeric.number_theory_functions import mobius_function
        assert mobius_function(7) == -1

    def test_two_distinct_primes(self):
        from agentfx.fxNumeric.number_theory_functions import mobius_function
        # 6 = 2*3, two distinct primes → μ = 1
        assert mobius_function(6) == 1

    def test_squared_factor(self):
        from agentfx.fxNumeric.number_theory_functions import mobius_function
        # 12 = 2²*3, has squared factor → μ = 0
        assert mobius_function(12) == 0

class TestIntegerPartitionsCount:

    def test_zero(self):
        from agentfx.fxNumeric.number_theory_functions import integer_partitions_count
        assert integer_partitions_count(0) == 1

    def test_five(self):
        from agentfx.fxNumeric.number_theory_functions import integer_partitions_count
        assert integer_partitions_count(5) == 7

    def test_ten(self):
        from agentfx.fxNumeric.number_theory_functions import integer_partitions_count
        assert integer_partitions_count(10) == 42

    def test_negative_raises(self):
        from agentfx.fxNumeric.number_theory_functions import integer_partitions_count

        with pytest.raises(ValueError):
            integer_partitions_count(-1)


# ── Statistics ───────────────────────────────────────────────────

class TestChineseRemainderTheorem:

    def test_basic(self):
        from agentfx.fxNumeric.number_theory_functions import chinese_remainder_theorem
        assert chinese_remainder_theorem([2, 3, 2], [3, 5, 7]) == 23

    def test_two_congruences(self):
        from agentfx.fxNumeric.number_theory_functions import chinese_remainder_theorem
        # x ≡ 1 (mod 3), x ≡ 4 (mod 5) → x = 4
        assert chinese_remainder_theorem([1, 4], [3, 5]) == 4

    def test_not_coprime(self):
        from agentfx.fxNumeric.number_theory_functions import chinese_remainder_theorem

        with pytest.raises(ValueError):
            chinese_remainder_theorem([1, 2], [4, 6])

class TestIsHarshadNumber:

    def test_harshad_18(self):
        from agentfx.fxNumeric.number_theory_functions import is_harshad_number
        assert is_harshad_number(18) is True

    def test_not_harshad_19(self):
        from agentfx.fxNumeric.number_theory_functions import is_harshad_number
        assert is_harshad_number(19) is False

    def test_harshad_1(self):
        from agentfx.fxNumeric.number_theory_functions import is_harshad_number
        assert is_harshad_number(1) is True

class TestJacobiSymbol:

    def test_basic(self):
        from agentfx.fxNumeric.number_theory_functions import jacobi_symbol
        assert jacobi_symbol(2, 15) == 1

    def test_negative_result(self):
        from agentfx.fxNumeric.number_theory_functions import jacobi_symbol
        assert jacobi_symbol(7, 15) == -1

    def test_even_n_raises(self):
        from agentfx.fxNumeric.number_theory_functions import jacobi_symbol

        with pytest.raises(ValueError):
            jacobi_symbol(2, 4)


# ── Arithmetic ───────────────────────────────────────────────────

class TestCollatzSteps:

    def test_6(self):
        from agentfx.fxNumeric.number_theory_functions import collatz_steps

        assert collatz_steps(6) == 8

    def test_1(self):
        from agentfx.fxNumeric.number_theory_functions import collatz_steps

        assert collatz_steps(1) == 0

    def test_negative(self):
        from agentfx.fxNumeric.number_theory_functions import collatz_steps

        with pytest.raises(ValueError):
            collatz_steps(-1)

class TestAdditivePersistence:

    def test_199(self):
        from agentfx.fxNumeric.number_theory_functions import additive_persistence

        assert additive_persistence(199) == 3

    def test_single_digit(self):
        from agentfx.fxNumeric.number_theory_functions import additive_persistence

        assert additive_persistence(5) == 0

    def test_type_error(self):
        from agentfx.fxNumeric.number_theory_functions import additive_persistence

        with pytest.raises(TypeError):
            additive_persistence(5.5)

class TestIsSquareFree:

    def test_true(self):
        from agentfx.fxNumeric.number_theory_functions import is_square_free

        assert is_square_free(30) is True

    def test_false(self):
        from agentfx.fxNumeric.number_theory_functions import is_square_free

        assert is_square_free(12) is False

    def test_one(self):
        from agentfx.fxNumeric.number_theory_functions import is_square_free

        assert is_square_free(1) is True


# ── Date Evaluations ─────────────────────────────────────────────────

class TestCountDivisors:

    def test_12(self):
        from agentfx.fxNumeric.number_theory_functions import count_divisors

        assert count_divisors(12) == 6

    def test_prime(self):
        from agentfx.fxNumeric.number_theory_functions import count_divisors

        assert count_divisors(7) == 2

    def test_one(self):
        from agentfx.fxNumeric.number_theory_functions import count_divisors

        assert count_divisors(1) == 1

class TestRadical:

    def test_12(self):
        from agentfx.fxNumeric.number_theory_functions import radical

        assert radical(12) == 6

    def test_1(self):
        from agentfx.fxNumeric.number_theory_functions import radical

        assert radical(1) == 1

    def test_prime(self):
        from agentfx.fxNumeric.number_theory_functions import radical

        assert radical(13) == 13

class TestIsSphenicNumber:

    def test_true(self):
        from agentfx.fxNumeric.number_theory_functions import is_sphenic_number

        assert is_sphenic_number(30) is True

    def test_false(self):
        from agentfx.fxNumeric.number_theory_functions import is_sphenic_number

        assert is_sphenic_number(12) is False

    def test_66(self):
        from agentfx.fxNumeric.number_theory_functions import is_sphenic_number

        assert is_sphenic_number(66) is True


# ── Date Evaluations ─────────────────────────────────────────────────

class TestNumberOfDistinctPrimeFactors:

    def test_basic(self):
        assert number_of_distinct_prime_factors(60) == 3

    def test_prime(self):
        assert number_of_distinct_prime_factors(13) == 1

    def test_type_error(self):
        with pytest.raises(TypeError):
            number_of_distinct_prime_factors(3.5)

class TestSumOfSquaresOfDigits:

    def test_basic(self):
        assert sum_of_squares_of_digits(123) == 14

    def test_single_digit(self):
        assert sum_of_squares_of_digits(5) == 25

    def test_type_error(self):
        with pytest.raises(TypeError):
            sum_of_squares_of_digits(3.5)

class TestSumProperDivisors:

    def test_basic(self):
        assert sum_proper_divisors(12) == 16

    def test_prime(self):
        assert sum_proper_divisors(7) == 1

    def test_perfect(self):
        # 6 is a perfect number: 1+2+3 = 6
        assert sum_proper_divisors(6) == 6

    def test_type_error(self):
        with pytest.raises(TypeError):
            sum_proper_divisors(3.5)


# ── Date ─────────────────────────────────────────────────────────────────────

class TestIsPowerfulNumber:

    def test_powerful(self):
        assert is_powerful_number(8) is True
        assert is_powerful_number(36) is True  # 2²·3²

    def test_not_powerful(self):
        assert is_powerful_number(12) is False

    def test_one(self):
        assert is_powerful_number(1) is True

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_powerful_number(3.5)

class TestLiouvilleLambda:

    def test_even_omega(self):
        assert liouville_lambda(6) == 1  # 2·3, Ω=2
        assert liouville_lambda(1) == 1  # Ω=0

    def test_odd_omega(self):
        assert liouville_lambda(2) == -1  # Ω=1
        assert liouville_lambda(30) == -1  # 2·3·5, Ω=3

    def test_type_error(self):
        with pytest.raises(TypeError):
            liouville_lambda(3.5)

class TestSumOfCubesOfDigits:

    def test_basic(self):
        assert sum_of_cubes_of_digits(123) == 36  # 1+8+27

    def test_single_digit(self):
        assert sum_of_cubes_of_digits(5) == 125

    def test_zero(self):
        assert sum_of_cubes_of_digits(0) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            sum_of_cubes_of_digits(3.5)


# ── Date ─────────────────────────────────────────────────────────────────────

class TestLucasNumber:

    def test_basic(self):
        assert lucas_number(0) == 2
        assert lucas_number(1) == 1
        assert lucas_number(5) == 11

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            lucas_number(-1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            lucas_number(5.0)

class TestIsAchillesNumber:

    def test_achilles(self):
        assert is_achilles_number(72) is True    # 2³·3², gcd(3,2)=1
        assert is_achilles_number(108) is True   # 2²·3³, gcd(2,3)=1

    def test_not_achilles(self):
        assert is_achilles_number(36) is False   # 2²·3², gcd(2,2)=2
        assert is_achilles_number(12) is False   # not powerful

    def test_one(self):
        assert is_achilles_number(1) is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_achilles_number(72.0)

class TestDigitCount:

    def test_basic(self):
        assert digit_count(12345) == 5

    def test_zero(self):
        assert digit_count(0) == 1

    def test_single(self):
        assert digit_count(9) == 1

    def test_power_of_ten(self):
        assert digit_count(1000) == 4

    def test_type_error(self):
        with pytest.raises(TypeError):
            digit_count(12.5)


# ── Date ─────────────────────────────────────────────────────────────────────

class TestTribonacciNumber:

    def test_sequence(self):
        assert tribonacci_number(0) == 0
        assert tribonacci_number(1) == 0
        assert tribonacci_number(2) == 1
        assert tribonacci_number(7) == 13

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            tribonacci_number(-1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            tribonacci_number(7.0)

class TestJacobsthalNumber:

    def test_sequence(self):
        assert jacobsthal_number(0) == 0
        assert jacobsthal_number(1) == 1
        assert jacobsthal_number(6) == 21

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            jacobsthal_number(-1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            jacobsthal_number(6.0)

class TestPellNumber:

    def test_sequence(self):
        assert pell_number(0) == 0
        assert pell_number(1) == 1
        assert pell_number(6) == 70

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            pell_number(-1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            pell_number(6.0)


# ── Date ─────────────────────────────────────────────────────────────────────

class TestMotzkinNumber:
    def test_base_cases(self):
        assert motzkin_number(0) == 1
        assert motzkin_number(1) == 1

    def test_known_values(self):
        assert motzkin_number(2) == 2
        assert motzkin_number(3) == 4
        assert motzkin_number(4) == 9
        assert motzkin_number(5) == 21

    def test_type_error(self):
        with pytest.raises(TypeError):
            motzkin_number(1.5)

    def test_negative(self):
        with pytest.raises(ValueError):
            motzkin_number(-1)

class TestNarayanaNumber:
    def test_basic(self):
        assert narayana_number(4, 2) == 6

    def test_n1_k1(self):
        assert narayana_number(1, 1) == 1

    def test_known_values(self):
        assert narayana_number(3, 1) == 1
        assert narayana_number(3, 2) == 3
        assert narayana_number(3, 3) == 1

    def test_type_error(self):
        with pytest.raises(TypeError):
            narayana_number(1.5, 1)

    def test_k_out_of_range(self):
        with pytest.raises(ValueError):
            narayana_number(3, 4)

class TestDelannoyNumber:
    def test_basic(self):
        assert delannoy_number(3, 3) == 63

    def test_base_cases(self):
        assert delannoy_number(0, 0) == 1
        assert delannoy_number(0, 5) == 1
        assert delannoy_number(5, 0) == 1

    def test_known_values(self):
        assert delannoy_number(1, 1) == 3
        assert delannoy_number(2, 2) == 13

    def test_type_error(self):
        with pytest.raises(TypeError):
            delannoy_number(1.5, 1)

    def test_negative(self):
        with pytest.raises(ValueError):
            delannoy_number(-1, 0)

class TestSchroederNumber:
    def test_known_values(self):
        assert schroeder_number(0) == 1
        assert schroeder_number(1) == 2
        assert schroeder_number(2) == 6
        assert schroeder_number(3) == 22
        assert schroeder_number(4) == 90

    def test_type_error(self):
        with pytest.raises(TypeError):
            schroeder_number(1.5)

    def test_negative(self):
        with pytest.raises(ValueError):
            schroeder_number(-1)


# ---------------------------------------------------------------------------
# Date
# ---------------------------------------------------------------------------

class TestEulerianNumber:
    def test_basic(self):
        assert eulerian_number(4, 1) == 11

    def test_n0_k0(self):
        assert eulerian_number(0, 0) == 1

    def test_known(self):
        assert eulerian_number(3, 0) == 1
        assert eulerian_number(3, 1) == 4
        assert eulerian_number(3, 2) == 1

    def test_type_error(self):
        with pytest.raises(TypeError):
            eulerian_number(1.5, 0)

    def test_k_out_of_range(self):
        with pytest.raises(ValueError):
            eulerian_number(3, 3)

class TestStirlingNumberSecond:
    def test_basic(self):
        assert stirling_number_second(4, 2) == 7

    def test_identity(self):
        assert stirling_number_second(5, 5) == 1
        assert stirling_number_second(5, 1) == 1

    def test_known(self):
        assert stirling_number_second(4, 3) == 6
        assert stirling_number_second(5, 2) == 15

    def test_type_error(self):
        with pytest.raises(TypeError):
            stirling_number_second(1.5, 1)

    def test_k_out_of_range(self):
        with pytest.raises(ValueError):
            stirling_number_second(3, 4)

class TestIntermediatePoint:
    def test_midpoint(self):
        lat, lon = intermediate_point(0.0, 0.0, 0.0, 10.0, 0.5)
        assert lon == pytest.approx(5.0, abs=0.1)

    def test_start(self):
        lat, lon = intermediate_point(40.0, -3.0, 50.0, 2.0, 0.0)
        assert lat == pytest.approx(40.0, abs=1e-6)
        assert lon == pytest.approx(-3.0, abs=1e-6)

    def test_type_error(self):
        with pytest.raises(TypeError):
            intermediate_point("a", 0, 0, 10, 0.5)

    def test_invalid_fraction(self):
        with pytest.raises(ValueError):
            intermediate_point(0, 0, 0, 10, 1.5)


# ---------------------------------------------------------------------------
# fxNumeric — number_theory_functions.py
# ---------------------------------------------------------------------------


class TestLegendreSymbol:
    def test_quadratic_residue(self):
        assert legendre_symbol(1, 5) == 1

    def test_non_residue(self):
        assert legendre_symbol(2, 5) == -1

    def test_zero(self):
        assert legendre_symbol(5, 5) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            legendre_symbol(1.5, 5)

    def test_invalid_p(self):
        with pytest.raises(ValueError):
            legendre_symbol(1, 2)

class TestContinuedFractionExpansion:
    def test_pi_approx(self):
        result = continued_fraction_expansion(355, 113)
        assert result == [3, 7, 16]

    def test_integer(self):
        assert continued_fraction_expansion(5, 1) == [5]

    def test_type_error(self):
        with pytest.raises(TypeError):
            continued_fraction_expansion(3.5, 1)

    def test_zero_denominator(self):
        with pytest.raises(ValueError):
            continued_fraction_expansion(1, 0)

class TestConvergents:
    def test_pi_approx(self):
        result = convergents([3, 7, 16])
        assert result == [(3, 1), (22, 7), (355, 113)]

    def test_single(self):
        assert convergents([5]) == [(5, 1)]

    def test_type_error(self):
        with pytest.raises(TypeError):
            convergents("abc")

    def test_empty(self):
        with pytest.raises(ValueError):
            convergents([])

class TestPrimitiveRoot:

    def test_prime_7(self):
        assert primitive_root(7) == 3

    def test_prime_2(self):
        assert primitive_root(2) == 1

    def test_not_prime(self):

        with pytest.raises(ValueError):
            primitive_root(4)

class TestDiscreteLogarithm:

    def test_basic(self):
        x = discrete_logarithm(2, 8, 13)
        assert pow(2, x, 13) == 8

    def test_another(self):
        x = discrete_logarithm(3, 13, 17)
        assert pow(3, x, 17) == 13

class TestEgyptianFraction:

    def test_3_7(self):
        result = egyptian_fraction(3, 7)
        total = sum(1.0 / d for d in result)
        assert abs(total - 3 / 7) < 1e-10

    def test_invalid(self):

        with pytest.raises(ValueError):
            egyptian_fraction(0, 5)

class TestJacobiSymbolV2:
    def test_basic(self):
        assert jacobi_symbol(2, 7) == 1

    def test_zero(self):
        assert jacobi_symbol(7, 7) == 0

    def test_negative(self):
        assert jacobi_symbol(3, 5) == -1

    def test_type_error(self):
        with pytest.raises(TypeError):
            jacobi_symbol(1.5, 7)

    def test_even_n(self):
        with pytest.raises(ValueError):
            jacobi_symbol(2, 4)

class TestKroneckerSymbol:
    def test_basic(self):
        assert kronecker_symbol(2, 7) == 1

    def test_zero(self):
        assert kronecker_symbol(2, 0) == 0

    def test_one(self):
        assert kronecker_symbol(5, 1) == 1

class TestLegendreSymbolV2:
    def test_basic(self):
        assert legendre_symbol(2, 7) == 1

    def test_qr(self):
        assert legendre_symbol(3, 5) == -1

    def test_zero(self):
        assert legendre_symbol(5, 5) == 0

class TestMobiusFunctionV2:
    def test_thirty(self):
        assert mobius_function(30) == -1

    def test_one(self):
        assert mobius_function(1) == 1

    def test_square(self):
        assert mobius_function(4) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            mobius_function(1.5)

class TestLiouvilleLambdaV2:
    def test_twelve(self):
        assert liouville_lambda(12) == -1

    def test_one(self):
        assert liouville_lambda(1) == 1

    def test_four(self):
        # 4 = 2^2, Ω=2, (-1)^2 = 1
        assert liouville_lambda(4) == 1

class TestSumOfDivisors:
    def test_twelve(self):
        assert sum_of_divisors(12) == 28

    def test_one(self):
        assert sum_of_divisors(1) == 1

    def test_sigma_zero(self):
        assert sum_of_divisors(12, 0) == 6

    def test_type_error(self):
        with pytest.raises(TypeError):
            sum_of_divisors(1.5)

class TestNumberOfDivisors:
    def test_twelve(self):
        assert number_of_divisors(12) == 6

    def test_prime(self):
        assert number_of_divisors(7) == 2

    def test_one(self):
        assert number_of_divisors(1) == 1

class TestIsPerfectNumber:
    def test_six(self):
        assert is_perfect_number(6) is True

    def test_twenty_eight(self):
        assert is_perfect_number(28) is True

    def test_twelve(self):
        assert is_perfect_number(12) is False

class TestIsAbundantNumberV2:
    def test_twelve(self):
        assert is_abundant_number(12) is True

    def test_six(self):
        assert is_abundant_number(6) is False

    def test_twenty(self):
        assert is_abundant_number(20) is True

class TestIsDeficientNumberV2:
    def test_eight(self):
        assert is_deficient_number(8) is True

    def test_twelve(self):
        assert is_deficient_number(12) is False

    def test_one(self):
        assert is_deficient_number(1) is True

class TestIsSemiprime:
    def test_fifteen(self):
        assert is_semiprime(15) is True

    def test_four(self):
        assert is_semiprime(4) is True

    def test_eight(self):
        assert is_semiprime(8) is False

    def test_prime(self):
        assert is_semiprime(7) is False

class TestIsSquareFreeV2:
    def test_thirty(self):
        assert is_square_free(30) is True

    def test_twelve(self):
        assert is_square_free(12) is False

    def test_one(self):
        assert is_square_free(1) is True

class TestIsPowerfulNumberV2:
    def test_seventy_two(self):
        assert is_powerful_number(72) is True

    def test_twelve(self):
        assert is_powerful_number(12) is False

    def test_one(self):
        assert is_powerful_number(1) is True

class TestIsSmithNumber:
    def test_twenty_two(self):
        assert is_smith_number(22) is True

    def test_prime(self):
        assert is_smith_number(7) is False

    def test_twenty_seven(self):
        # 27 = 3^3, digit sum 9, factor digit sum 3+3+3=9
        assert is_smith_number(27) is True

class TestIsHarshadNumberV2:
    def test_eighteen(self):
        assert is_harshad_number(18) is True

    def test_eleven(self):
        assert is_harshad_number(11) is False

    def test_one(self):
        assert is_harshad_number(1) is True

class TestIsKaprekarNumber:
    def test_forty_five(self):
        assert is_kaprekar_number(45) is True

    def test_nine(self):
        assert is_kaprekar_number(9) is True

    def test_one(self):
        assert is_kaprekar_number(1) is True

    def test_two(self):
        assert is_kaprekar_number(2) is False

class TestPrimeCountingApprox:
    def test_thousand(self):
        assert round(prime_counting_approx(1000), 1) == 144.8

    def test_type_error(self):
        with pytest.raises(TypeError):
            prime_counting_approx("abc")

    def test_value_error(self):
        with pytest.raises(ValueError):
            prime_counting_approx(1)

class TestPrimeNthApprox:
    def test_hundred(self):
        assert round(prime_nth_approx(100)) == 613

    def test_one(self):
        assert prime_nth_approx(1) == 2.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            prime_nth_approx(1.5)

class TestAliquotSum:
    def test_twelve(self):
        assert aliquot_sum(12) == 16

    def test_one(self):
        assert aliquot_sum(1) == 0

    def test_prime(self):
        assert aliquot_sum(7) == 1

class TestIsAmicablePair:
    def test_classic(self):
        assert is_amicable_pair(220, 284) is True

    def test_reversed(self):
        assert is_amicable_pair(284, 220) is True

    def test_not_amicable(self):
        assert is_amicable_pair(10, 20) is False

    def test_same(self):
        with pytest.raises(ValueError):
            is_amicable_pair(6, 6)

class TestRadicalV2:
    def test_twelve(self):
        assert radical(12) == 6

    def test_one(self):
        assert radical(1) == 1

    def test_prime(self):
        assert radical(7) == 7

class TestOmegaPrime:
    def test_twelve(self):
        assert omega_prime(12) == 2

    def test_one(self):
        assert omega_prime(1) == 0

    def test_prime(self):
        assert omega_prime(7) == 1

class TestBigOmega:
    def test_twelve(self):
        assert big_omega(12) == 3

    def test_one(self):
        assert big_omega(1) == 0

    def test_prime(self):
        assert big_omega(7) == 1

    def test_eight(self):
        assert big_omega(8) == 3

class TestIsPalindromicNumber:
    def test_palindrome(self):
        assert is_palindromic_number(12321) is True

    def test_not_palindrome(self):
        assert is_palindromic_number(12345) is False

    def test_single_digit(self):
        assert is_palindromic_number(7) is True

    def test_zero(self):
        assert is_palindromic_number(0) is True

class TestCoprime:
    def test_coprime(self):
        assert coprime(8, 15) is True

    def test_not_coprime(self):
        assert coprime(8, 12) is False

    def test_one(self):
        assert coprime(1, 100) is True

class TestDigitalSum:
    def test_basic(self):
        assert digital_sum(12345) == 15

    def test_zero(self):
        assert digital_sum(0) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            digital_sum(1.5)

class TestMultiplicativePersistence:
    def test_thirty_nine(self):
        assert multiplicative_persistence(39) == 3

    def test_single_digit(self):
        assert multiplicative_persistence(5) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            multiplicative_persistence(1.5)

class TestAdditivePersistenceV2:
    def test_basic(self):
        assert additive_persistence(199) == 3

    def test_single_digit(self):
        assert additive_persistence(5) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            additive_persistence(1.5)

class TestCollatzStepsV2:
    def test_twenty_seven(self):
        assert collatz_steps(27) == 111

    def test_one(self):
        assert collatz_steps(1) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            collatz_steps(1.5)

class TestIsHappyNumber:
    def test_true(self):
        assert is_happy_number(19) is True

    def test_false(self):
        assert is_happy_number(2) is False

    def test_one(self):
        assert is_happy_number(1) is True

class TestSternBrocot:
    def test_ten(self):
        assert stern_brocot(10) == [0, 1, 1, 2, 1, 3, 2, 3, 1, 4]

    def test_one(self):
        assert stern_brocot(1) == [0]

    def test_type_error(self):
        with pytest.raises(TypeError):
            stern_brocot(1.5)

class TestContraharmonicMean:

    def test_basic(self):
        # sum_sq = 1+4+9+16+25 = 55, sum = 15 → 55/15 = 3.666...
        result = contraharmonic_mean([1, 2, 3, 4, 5])
        assert abs(result - 55 / 15) < 1e-10

    def test_zero_sum_raises(self):
        with pytest.raises(ValueError):
            contraharmonic_mean([-1, 1])

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            contraharmonic_mean([])

    def test_type_error(self):
        with pytest.raises(TypeError):
            contraharmonic_mean("not_a_list")


# ── fxNumeric · number_theory_functions ──────────────────────────────


class TestCarmichaelLambda:

    def test_lambda_1(self):
        assert carmichael_lambda(1) == 1

    def test_lambda_8(self):
        assert carmichael_lambda(8) == 2

    def test_lambda_15(self):
        assert carmichael_lambda(15) == 4

    def test_lambda_prime(self):
        # λ(p) = p-1 for prime p
        assert carmichael_lambda(7) == 6

    def test_lambda_12(self):
        # 12 = 2^2 × 3 → λ = lcm(λ(4), λ(3)) = lcm(2, 2) = 2
        assert carmichael_lambda(12) == 2

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            carmichael_lambda(0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            carmichael_lambda(8.5)

class TestIsLychrelCandidate:

    def test_196_is_candidate(self):
        assert is_lychrel_candidate(196) is True

    def test_56_is_not(self):
        assert is_lychrel_candidate(56) is False

    def test_0_not_candidate(self):
        # 0 + 0 = 0 which is palindrome
        assert is_lychrel_candidate(0) is False

    def test_negative_raises(self):
        with pytest.raises(ValueError):
            is_lychrel_candidate(-1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_lychrel_candidate(196.5)

class TestIsSmithNumberV2:

    def test_22_is_smith(self):
        from agentfx.fxNumeric.number_theory_functions import is_smith_number
        assert is_smith_number(22) is True

    def test_27_is_smith(self):
        from agentfx.fxNumeric.number_theory_functions import is_smith_number
        assert is_smith_number(27) is True

    def test_prime_not_smith(self):
        from agentfx.fxNumeric.number_theory_functions import is_smith_number
        assert is_smith_number(23) is False

    def test_4_is_smith(self):
        from agentfx.fxNumeric.number_theory_functions import is_smith_number
        assert is_smith_number(4) is True

class TestIsNarcissisticNumber:

    def test_153(self):
        from agentfx.fxNumeric.number_theory_functions import is_narcissistic_number
        assert is_narcissistic_number(153) is True

    def test_370(self):
        from agentfx.fxNumeric.number_theory_functions import is_narcissistic_number
        assert is_narcissistic_number(370) is True

    def test_single_digits(self):
        from agentfx.fxNumeric.number_theory_functions import is_narcissistic_number
        for d in range(10):
            assert is_narcissistic_number(d) is True

    def test_10_is_not(self):
        from agentfx.fxNumeric.number_theory_functions import is_narcissistic_number
        assert is_narcissistic_number(10) is False

class TestSternBrocotV2:

    def test_first_10(self):
        from agentfx.fxNumeric.number_theory_functions import stern_brocot
        assert stern_brocot(10) == [0, 1, 1, 2, 1, 3, 2, 3, 1, 4]

    def test_single(self):
        from agentfx.fxNumeric.number_theory_functions import stern_brocot
        assert stern_brocot(1) == [0]

    def test_two(self):
        from agentfx.fxNumeric.number_theory_functions import stern_brocot
        assert stern_brocot(2) == [0, 1]


# ── Arithmetic ──────────────────────────────────────────────────────────────

class TestIsSquareNumber:

    def test_true(self):
        from agentfx.fxNumeric.number_theory_functions import is_square_number
        assert is_square_number(49) is True

    def test_false(self):
        from agentfx.fxNumeric.number_theory_functions import is_square_number
        assert is_square_number(50) is False

    def test_zero(self):
        from agentfx.fxNumeric.number_theory_functions import is_square_number
        assert is_square_number(0) is True

class TestIsTriangularNumber:

    def test_true(self):
        from agentfx.fxNumeric.number_theory_functions import is_triangular_number
        assert is_triangular_number(10) is True

    def test_false(self):
        from agentfx.fxNumeric.number_theory_functions import is_triangular_number
        assert is_triangular_number(11) is False

    def test_one(self):
        from agentfx.fxNumeric.number_theory_functions import is_triangular_number
        assert is_triangular_number(1) is True

class TestIsPowerOfTwo:

    def test_true(self):
        from agentfx.fxNumeric.number_theory_functions import is_power_of_two
        assert is_power_of_two(64) is True

    def test_false(self):
        from agentfx.fxNumeric.number_theory_functions import is_power_of_two
        assert is_power_of_two(65) is False

    def test_one(self):
        from agentfx.fxNumeric.number_theory_functions import is_power_of_two
        assert is_power_of_two(1) is True

class TestDigitalSumV2:

    def test_basic(self):
        from agentfx.fxNumeric.number_theory_functions import digital_sum
        assert digital_sum(12345) == 15

    def test_negative(self):
        from agentfx.fxNumeric.number_theory_functions import digital_sum
        assert digital_sum(-999) == 27

    def test_zero(self):
        from agentfx.fxNumeric.number_theory_functions import digital_sum
        assert digital_sum(0) == 0

class TestCountDigits:

    def test_basic(self):
        from agentfx.fxNumeric.number_theory_functions import count_digits
        assert count_digits(12345) == 5

    def test_negative(self):
        from agentfx.fxNumeric.number_theory_functions import count_digits
        assert count_digits(-99) == 2

    def test_zero(self):
        from agentfx.fxNumeric.number_theory_functions import count_digits
        assert count_digits(0) == 1


# =====================================================================
# Statistics
# =====================================================================

class TestIsPerfectPower:

    def test_true_cases(self):
        assert is_perfect_power(1) is True
        assert is_perfect_power(4) is True
        assert is_perfect_power(8) is True
        assert is_perfect_power(27) is True
        assert is_perfect_power(16) is True
        assert is_perfect_power(256) is True

    def test_false_cases(self):
        assert is_perfect_power(2) is False
        assert is_perfect_power(3) is False
        assert is_perfect_power(10) is False
        assert is_perfect_power(15) is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_perfect_power(8.0)


# ──────────────────────────────────────────────
# Number Theory: is_semiprime
# ──────────────────────────────────────────────

class TestIsSemiprimeV2:

    def test_true_cases(self):
        assert is_semiprime(4) is True   # 2*2
        assert is_semiprime(6) is True   # 2*3
        assert is_semiprime(9) is True   # 3*3
        assert is_semiprime(15) is True  # 3*5

    def test_false_cases(self):
        assert is_semiprime(2) is False   # prime
        assert is_semiprime(8) is False   # 2*2*2
        assert is_semiprime(12) is False  # 2*2*3

    def test_value_error(self):
        with pytest.raises(ValueError):
            is_semiprime(1)


# ──────────────────────────────────────────────
# Number Theory: aliquot_sum
# ──────────────────────────────────────────────

class TestAliquotSumV2:

    def test_basic(self):
        assert aliquot_sum(12) == 16  # 1+2+3+4+6

    def test_one(self):
        assert aliquot_sum(1) == 0

    def test_prime(self):
        assert aliquot_sum(7) == 1

    def test_perfect_number(self):
        assert aliquot_sum(6) == 6  # 1+2+3 = 6

    def test_type_error(self):
        with pytest.raises(TypeError):
            aliquot_sum(12.0)


# ──────────────────────────────────────────────
# Date: is_first_of_month
# ──────────────────────────────────────────────

class TestIsCubeNumber:

    def test_true_cases(self):
        assert is_cube_number(0) is True
        assert is_cube_number(1) is True
        assert is_cube_number(8) is True
        assert is_cube_number(27) is True
        assert is_cube_number(64) is True
        assert is_cube_number(125) is True

    def test_false_cases(self):
        assert is_cube_number(2) is False
        assert is_cube_number(9) is False
        assert is_cube_number(26) is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_cube_number(27.0)


# ──────────────────────────────────────────────
# Number Theory: is_pronic_number
# ──────────────────────────────────────────────

class TestIsPronicNumber:

    def test_true_cases(self):
        assert is_pronic_number(0) is True   # 0*1
        assert is_pronic_number(2) is True   # 1*2
        assert is_pronic_number(6) is True   # 2*3
        assert is_pronic_number(12) is True  # 3*4
        assert is_pronic_number(20) is True  # 4*5
        assert is_pronic_number(42) is True  # 6*7

    def test_false_cases(self):
        assert is_pronic_number(1) is False
        assert is_pronic_number(3) is False
        assert is_pronic_number(7) is False


# ──────────────────────────────────────────────
# Number Theory: is_automorphic_number
# ──────────────────────────────────────────────

class TestIsAutomorphicNumber:

    def test_true_cases(self):
        assert is_automorphic_number(0) is True
        assert is_automorphic_number(1) is True
        assert is_automorphic_number(5) is True
        assert is_automorphic_number(6) is True
        assert is_automorphic_number(25) is True
        assert is_automorphic_number(76) is True
        assert is_automorphic_number(376) is True
        assert is_automorphic_number(625) is True

    def test_false_cases(self):
        assert is_automorphic_number(2) is False
        assert is_automorphic_number(77) is False


# ──────────────────────────────────────────────
# Number Theory: multiplicative_persistence
# ──────────────────────────────────────────────

class TestMultiplicativePersistenceV2:

    def test_single_digit(self):
        assert multiplicative_persistence(5) == 0

    def test_39(self):
        assert multiplicative_persistence(39) == 3

    def test_999(self):
        assert multiplicative_persistence(999) == 4

    def test_zero(self):
        assert multiplicative_persistence(0) == 0

    def test_10(self):
        assert multiplicative_persistence(10) == 1


# ──────────────────────────────────────────────
# Date: is_palindrome_date
# ──────────────────────────────────────────────

class TestIsKaprekarNumberV2:

    def test_true(self):
        from agentfx.fxNumeric.number_theory_functions import is_kaprekar_number

        assert is_kaprekar_number(9) is True
        assert is_kaprekar_number(45) is True

    def test_false(self):
        from agentfx.fxNumeric.number_theory_functions import is_kaprekar_number

        assert is_kaprekar_number(10) is False

    def test_one(self):
        from agentfx.fxNumeric.number_theory_functions import is_kaprekar_number

        assert is_kaprekar_number(1) is True

class TestIsHappyNumberV2:

    def test_happy(self):
        from agentfx.fxNumeric.number_theory_functions import is_happy_number

        assert is_happy_number(19) is True

    def test_unhappy(self):
        from agentfx.fxNumeric.number_theory_functions import is_happy_number

        assert is_happy_number(2) is False

    def test_negative(self):
        from agentfx.fxNumeric.number_theory_functions import is_happy_number

        with pytest.raises(ValueError):
            is_happy_number(-1)

class TestDigitalRoot:

    def test_basic(self):
        from agentfx.fxNumeric.number_theory_functions import digital_root

        assert digital_root(493) == 7

    def test_zero(self):
        from agentfx.fxNumeric.number_theory_functions import digital_root

        assert digital_root(0) == 0

    def test_single_digit(self):
        from agentfx.fxNumeric.number_theory_functions import digital_root

        assert digital_root(5) == 5


# ── Date Evaluations ─────────────────────────────────────────────────

class TestNumberTheoryExtensions:

    def test_partition_function_5(self):
        assert partition_function(5) == 7

    def test_partition_function_10(self):
        assert partition_function(10) == 42

    def test_partition_function_0(self):
        assert partition_function(0) == 1

    def test_liouville_6(self):
        # 6 = 2 * 3 → Ω = 2 → λ = 1
        assert liouville_lambda(6) == 1

    def test_liouville_12(self):
        # 12 = 2^2 * 3 → Ω = 3 → λ = -1
        assert liouville_lambda(12) == -1

    def test_carmichael_8(self):
        assert carmichael_lambda(8) == 2

    def test_carmichael_12(self):
        assert carmichael_lambda(12) == 2

    def test_sum_of_squares_count_5(self):
        # 5 = 1² + 2², and all sign/order permutations → 8
        assert sum_of_squares_count(5) == 8

    def test_sum_of_squares_count_1(self):
        assert sum_of_squares_count(1) == 4

    def test_squarefree_12(self):
        assert squarefree_part(12) == 3

    def test_squarefree_7(self):
        assert squarefree_part(7) == 7

    def test_primitive_root_7(self):
        assert primitive_root(7) == 3

    def test_primitive_root_11(self):
        assert primitive_root(11) == 2


# ===================================================================
# Special functions extensions
# ===================================================================
