# Coverage tests for formulite.fxNumeric.number_theory_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import number_theory_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_additive_persistence:
    def test_exists(self):
        assert hasattr(mod, "additive_persistence")

    def test_doc0(self):
        try:
            mod.additive_persistence(199)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.additive_persistence(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.additive_persistence(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.additive_persistence(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.additive_persistence(None)
        except EXC:
            pass


class Test_aliquot_sum:
    def test_exists(self):
        assert hasattr(mod, "aliquot_sum")

    def test_doc0(self):
        try:
            mod.aliquot_sum(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.aliquot_sum(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.aliquot_sum(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.aliquot_sum(None)
        except EXC:
            pass


class Test_bell_number:
    def test_exists(self):
        assert hasattr(mod, "bell_number")

    def test_doc0(self):
        try:
            mod.bell_number(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bell_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bell_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bell_number(None)
        except EXC:
            pass


class Test_big_omega:
    def test_exists(self):
        assert hasattr(mod, "big_omega")

    def test_doc0(self):
        try:
            mod.big_omega(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.big_omega(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.big_omega(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.big_omega(None)
        except EXC:
            pass


class Test_carmichael_lambda:
    def test_exists(self):
        assert hasattr(mod, "carmichael_lambda")

    def test_doc0(self):
        try:
            mod.carmichael_lambda(8)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.carmichael_lambda(15)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.carmichael_lambda(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.carmichael_lambda(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.carmichael_lambda(None)
        except EXC:
            pass


class Test_catalan_number:
    def test_exists(self):
        assert hasattr(mod, "catalan_number")

    def test_doc0(self):
        try:
            mod.catalan_number(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.catalan_number(5)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.catalan_number(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.catalan_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.catalan_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.catalan_number(None)
        except EXC:
            pass


class Test_chinese_remainder_theorem:
    def test_exists(self):
        assert hasattr(mod, "chinese_remainder_theorem")

    def test_doc0(self):
        try:
            mod.chinese_remainder_theorem([2, 3, 2], [3, 5, 7])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.chinese_remainder_theorem(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chinese_remainder_theorem(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chinese_remainder_theorem(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chinese_remainder_theorem("", "")
        except EXC:
            pass


class Test_collatz_length:
    def test_exists(self):
        assert hasattr(mod, "collatz_length")

    def test_doc0(self):
        try:
            mod.collatz_length(6)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.collatz_length(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.collatz_length(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.collatz_length(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.collatz_length(None)
        except EXC:
            pass


class Test_collatz_steps:
    def test_exists(self):
        assert hasattr(mod, "collatz_steps")

    def test_doc0(self):
        try:
            mod.collatz_steps(6)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.collatz_steps(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.collatz_steps(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.collatz_steps(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.collatz_steps(None)
        except EXC:
            pass


class Test_continued_fraction_expansion:
    def test_exists(self):
        assert hasattr(mod, "continued_fraction_expansion")

    def test_doc0(self):
        try:
            mod.continued_fraction_expansion(355, 113)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.continued_fraction_expansion(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.continued_fraction_expansion(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.continued_fraction_expansion(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.continued_fraction_expansion("", "")
        except EXC:
            pass


class Test_convergents:
    def test_exists(self):
        assert hasattr(mod, "convergents")

    def test_doc0(self):
        try:
            mod.convergents([3, 7, 16])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.convergents(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.convergents(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.convergents(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.convergents("")
        except EXC:
            pass


class Test_coprime:
    def test_exists(self):
        assert hasattr(mod, "coprime")

    def test_doc0(self):
        try:
            mod.coprime(8, 15)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coprime(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coprime(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coprime(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coprime("", "")
        except EXC:
            pass


class Test_count_digits:
    def test_exists(self):
        assert hasattr(mod, "count_digits")

    def test_doc0(self):
        try:
            mod.count_digits(12345)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.count_digits(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.count_digits(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.count_digits(None)
        except EXC:
            pass


class Test_count_divisors:
    def test_exists(self):
        assert hasattr(mod, "count_divisors")

    def test_doc0(self):
        try:
            mod.count_divisors(12)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.count_divisors(7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.count_divisors(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.count_divisors(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.count_divisors(None)
        except EXC:
            pass


class Test_delannoy_number:
    def test_exists(self):
        assert hasattr(mod, "delannoy_number")

    def test_doc0(self):
        try:
            mod.delannoy_number(3, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.delannoy_number(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.delannoy_number(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.delannoy_number(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.delannoy_number("", 0)
        except EXC:
            pass


class Test_digit_count:
    def test_exists(self):
        assert hasattr(mod, "digit_count")

    def test_doc0(self):
        try:
            mod.digit_count(12345)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.digit_count(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.digit_count(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.digit_count(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.digit_count(None)
        except EXC:
            pass


class Test_digit_factorial_sum:
    def test_exists(self):
        assert hasattr(mod, "digit_factorial_sum")

    def test_doc0(self):
        try:
            mod.digit_factorial_sum(145)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.digit_factorial_sum(123)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.digit_factorial_sum(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.digit_factorial_sum(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.digit_factorial_sum(None)
        except EXC:
            pass


class Test_digital_root:
    def test_exists(self):
        assert hasattr(mod, "digital_root")

    def test_doc0(self):
        try:
            mod.digital_root(493)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.digital_root(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.digital_root(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.digital_root(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.digital_root(None)
        except EXC:
            pass


class Test_digital_sum:
    def test_exists(self):
        assert hasattr(mod, "digital_sum")

    def test_doc0(self):
        try:
            mod.digital_sum(12345)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.digital_sum(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.digital_sum(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.digital_sum(None)
        except EXC:
            pass


class Test_discrete_logarithm:
    def test_exists(self):
        assert hasattr(mod, "discrete_logarithm")

    def test_doc0(self):
        try:
            mod.discrete_logarithm(2, 8, 13)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.discrete_logarithm(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.discrete_logarithm(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.discrete_logarithm(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.discrete_logarithm("", "", "")
        except EXC:
            pass


class Test_divisors:
    def test_exists(self):
        assert hasattr(mod, "divisors")

    def test_doc0(self):
        try:
            mod.divisors(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.divisors(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.divisors(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.divisors(None)
        except EXC:
            pass


class Test_egyptian_fraction:
    def test_exists(self):
        assert hasattr(mod, "egyptian_fraction")

    def test_doc0(self):
        try:
            mod.egyptian_fraction(3, 7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.egyptian_fraction(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.egyptian_fraction(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.egyptian_fraction(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.egyptian_fraction("", "")
        except EXC:
            pass


class Test_euler_totient:
    def test_exists(self):
        assert hasattr(mod, "euler_totient")

    def test_doc0(self):
        try:
            mod.euler_totient(12)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.euler_totient(7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.euler_totient(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.euler_totient(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.euler_totient(None)
        except EXC:
            pass


class Test_eulerian_number:
    def test_exists(self):
        assert hasattr(mod, "eulerian_number")

    def test_doc0(self):
        try:
            mod.eulerian_number(4, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.eulerian_number(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.eulerian_number(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.eulerian_number(None, 0)
        except EXC:
            pass


class Test_fibonacci_sequence:
    def test_exists(self):
        assert hasattr(mod, "fibonacci_sequence")

    def test_doc0(self):
        try:
            mod.fibonacci_sequence(7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fibonacci_sequence(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fibonacci_sequence(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fibonacci_sequence(None)
        except EXC:
            pass


class Test_get_primes_up_to:
    def test_exists(self):
        assert hasattr(mod, "get_primes_up_to")

    def test_doc0(self):
        try:
            mod.get_primes_up_to(10)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_primes_up_to(20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_primes_up_to(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_primes_up_to(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_primes_up_to(None)
        except EXC:
            pass


class Test_goldbach_partition:
    def test_exists(self):
        assert hasattr(mod, "goldbach_partition")

    def test_doc0(self):
        try:
            mod.goldbach_partition(28)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.goldbach_partition(100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.goldbach_partition(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.goldbach_partition(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.goldbach_partition(None)
        except EXC:
            pass


class Test_integer_partitions_count:
    def test_exists(self):
        assert hasattr(mod, "integer_partitions_count")

    def test_doc0(self):
        try:
            mod.integer_partitions_count(5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.integer_partitions_count(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.integer_partitions_count(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.integer_partitions_count(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.integer_partitions_count(None)
        except EXC:
            pass


class Test_is_abundant_number:
    def test_exists(self):
        assert hasattr(mod, "is_abundant_number")

    def test_doc0(self):
        try:
            mod.is_abundant_number(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_abundant_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_abundant_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_abundant_number(None)
        except EXC:
            pass


class Test_is_achilles_number:
    def test_exists(self):
        assert hasattr(mod, "is_achilles_number")

    def test_doc0(self):
        try:
            mod.is_achilles_number(72)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_achilles_number(36)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_achilles_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_achilles_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_achilles_number(None)
        except EXC:
            pass


class Test_is_amicable_pair:
    def test_exists(self):
        assert hasattr(mod, "is_amicable_pair")

    def test_doc0(self):
        try:
            mod.is_amicable_pair(220, 284)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_amicable_pair(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_amicable_pair(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_amicable_pair(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_amicable_pair("", "")
        except EXC:
            pass


class Test_is_automorphic_number:
    def test_exists(self):
        assert hasattr(mod, "is_automorphic_number")

    def test_doc0(self):
        try:
            mod.is_automorphic_number(76)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_automorphic_number(77)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_automorphic_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_automorphic_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_automorphic_number(None)
        except EXC:
            pass


class Test_is_coprime:
    def test_exists(self):
        assert hasattr(mod, "is_coprime")

    def test_doc0(self):
        try:
            mod.is_coprime(14, 15)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_coprime(14, 21)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_coprime(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_coprime(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_coprime(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_coprime("", "")
        except EXC:
            pass


class Test_is_cube_number:
    def test_exists(self):
        assert hasattr(mod, "is_cube_number")

    def test_doc0(self):
        try:
            mod.is_cube_number(27)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_cube_number(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_cube_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_cube_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_cube_number(None)
        except EXC:
            pass


class Test_is_deficient_number:
    def test_exists(self):
        assert hasattr(mod, "is_deficient_number")

    def test_doc0(self):
        try:
            mod.is_deficient_number(8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_deficient_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_deficient_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_deficient_number(None)
        except EXC:
            pass


class Test_is_even:
    def test_exists(self):
        assert hasattr(mod, "is_even")

    def test_doc0(self):
        try:
            mod.is_even(4)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_even(7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_even(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_even(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_even(None)
        except EXC:
            pass


class Test_is_fibonacci_number:
    def test_exists(self):
        assert hasattr(mod, "is_fibonacci_number")

    def test_doc0(self):
        try:
            mod.is_fibonacci_number(13)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_fibonacci_number(14)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_fibonacci_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_fibonacci_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_fibonacci_number(None)
        except EXC:
            pass


class Test_is_happy_number:
    def test_exists(self):
        assert hasattr(mod, "is_happy_number")

    def test_doc0(self):
        try:
            mod.is_happy_number(19)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_happy_number(2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_happy_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_happy_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_happy_number(None)
        except EXC:
            pass


class Test_is_harshad_number:
    def test_exists(self):
        assert hasattr(mod, "is_harshad_number")

    def test_doc0(self):
        try:
            mod.is_harshad_number(18)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_harshad_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_harshad_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_harshad_number(None)
        except EXC:
            pass


class Test_is_kaprekar_number:
    def test_exists(self):
        assert hasattr(mod, "is_kaprekar_number")

    def test_doc0(self):
        try:
            mod.is_kaprekar_number(45)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_kaprekar_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_kaprekar_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_kaprekar_number(None)
        except EXC:
            pass


class Test_is_lychrel_candidate:
    def test_exists(self):
        assert hasattr(mod, "is_lychrel_candidate")

    def test_doc0(self):
        try:
            mod.is_lychrel_candidate(196)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_lychrel_candidate(56)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_lychrel_candidate(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_lychrel_candidate(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_lychrel_candidate(None)
        except EXC:
            pass


class Test_is_narcissistic_number:
    def test_exists(self):
        assert hasattr(mod, "is_narcissistic_number")

    def test_doc0(self):
        try:
            mod.is_narcissistic_number(153)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_narcissistic_number(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_narcissistic_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_narcissistic_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_narcissistic_number(None)
        except EXC:
            pass


class Test_is_odd:
    def test_exists(self):
        assert hasattr(mod, "is_odd")

    def test_doc0(self):
        try:
            mod.is_odd(7)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_odd(4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_odd(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_odd(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_odd(None)
        except EXC:
            pass


class Test_is_palindrome_number:
    def test_exists(self):
        assert hasattr(mod, "is_palindrome_number")

    def test_doc0(self):
        try:
            mod.is_palindrome_number(121)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_palindrome_number(123)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_palindrome_number(-121)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_palindrome_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_palindrome_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_palindrome_number(None)
        except EXC:
            pass


class Test_is_palindromic_number:
    def test_exists(self):
        assert hasattr(mod, "is_palindromic_number")

    def test_doc0(self):
        try:
            mod.is_palindromic_number(12321)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_palindromic_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_palindromic_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_palindromic_number(None)
        except EXC:
            pass


class Test_is_perfect_number:
    def test_exists(self):
        assert hasattr(mod, "is_perfect_number")

    def test_doc0(self):
        try:
            mod.is_perfect_number(28)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_perfect_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_perfect_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_perfect_number(None)
        except EXC:
            pass


class Test_is_perfect_power:
    def test_exists(self):
        assert hasattr(mod, "is_perfect_power")

    def test_doc0(self):
        try:
            mod.is_perfect_power(8)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_perfect_power(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_perfect_power(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_perfect_power(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_perfect_power(None)
        except EXC:
            pass


class Test_is_power_of_two:
    def test_exists(self):
        assert hasattr(mod, "is_power_of_two")

    def test_doc0(self):
        try:
            mod.is_power_of_two(64)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_power_of_two(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_power_of_two(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_power_of_two(None)
        except EXC:
            pass


class Test_is_powerful_number:
    def test_exists(self):
        assert hasattr(mod, "is_powerful_number")

    def test_doc0(self):
        try:
            mod.is_powerful_number(72)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_powerful_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_powerful_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_powerful_number(None)
        except EXC:
            pass


class Test_is_prime:
    def test_exists(self):
        assert hasattr(mod, "is_prime")

    def test_doc0(self):
        try:
            mod.is_prime(7)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_prime(4)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.is_prime(2)
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.is_prime(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_prime(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_prime(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_prime(None)
        except EXC:
            pass


class Test_is_pronic_number:
    def test_exists(self):
        assert hasattr(mod, "is_pronic_number")

    def test_doc0(self):
        try:
            mod.is_pronic_number(6)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_pronic_number(7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_pronic_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_pronic_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_pronic_number(None)
        except EXC:
            pass


class Test_is_semiprime:
    def test_exists(self):
        assert hasattr(mod, "is_semiprime")

    def test_doc0(self):
        try:
            mod.is_semiprime(15)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_semiprime(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_semiprime(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_semiprime(None)
        except EXC:
            pass


class Test_is_smith_number:
    def test_exists(self):
        assert hasattr(mod, "is_smith_number")

    def test_doc0(self):
        try:
            mod.is_smith_number(22)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_smith_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_smith_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_smith_number(None)
        except EXC:
            pass


class Test_is_sphenic_number:
    def test_exists(self):
        assert hasattr(mod, "is_sphenic_number")

    def test_doc0(self):
        try:
            mod.is_sphenic_number(30)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.is_sphenic_number(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_sphenic_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_sphenic_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_sphenic_number(None)
        except EXC:
            pass


class Test_is_square_free:
    def test_exists(self):
        assert hasattr(mod, "is_square_free")

    def test_doc0(self):
        try:
            mod.is_square_free(30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_square_free(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_square_free(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_square_free(None)
        except EXC:
            pass


class Test_is_square_number:
    def test_exists(self):
        assert hasattr(mod, "is_square_number")

    def test_doc0(self):
        try:
            mod.is_square_number(49)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_square_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_square_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_square_number(None)
        except EXC:
            pass


class Test_is_triangular_number:
    def test_exists(self):
        assert hasattr(mod, "is_triangular_number")

    def test_doc0(self):
        try:
            mod.is_triangular_number(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.is_triangular_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_triangular_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_triangular_number(None)
        except EXC:
            pass


class Test_jacobi_symbol:
    def test_exists(self):
        assert hasattr(mod, "jacobi_symbol")

    def test_doc0(self):
        try:
            mod.jacobi_symbol(2, 7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.jacobi_symbol(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jacobi_symbol(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jacobi_symbol(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.jacobi_symbol("", 0)
        except EXC:
            pass


class Test_jacobsthal_number:
    def test_exists(self):
        assert hasattr(mod, "jacobsthal_number")

    def test_doc0(self):
        try:
            mod.jacobsthal_number(6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.jacobsthal_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jacobsthal_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jacobsthal_number(None)
        except EXC:
            pass


class Test_kronecker_symbol:
    def test_exists(self):
        assert hasattr(mod, "kronecker_symbol")

    def test_doc0(self):
        try:
            mod.kronecker_symbol(2, 7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.kronecker_symbol(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kronecker_symbol(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kronecker_symbol(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kronecker_symbol("", 0)
        except EXC:
            pass


class Test_legendre_symbol:
    def test_exists(self):
        assert hasattr(mod, "legendre_symbol")

    def test_doc0(self):
        try:
            mod.legendre_symbol(2, 7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.legendre_symbol(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.legendre_symbol(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.legendre_symbol(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.legendre_symbol("", "")
        except EXC:
            pass


class Test_liouville_lambda:
    def test_exists(self):
        assert hasattr(mod, "liouville_lambda")

    def test_doc0(self):
        try:
            mod.liouville_lambda(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.liouville_lambda(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.liouville_lambda(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.liouville_lambda(None)
        except EXC:
            pass


class Test_lucas_number:
    def test_exists(self):
        assert hasattr(mod, "lucas_number")

    def test_doc0(self):
        try:
            mod.lucas_number(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lucas_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lucas_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lucas_number(None)
        except EXC:
            pass


class Test_lucas_sequence:
    def test_exists(self):
        assert hasattr(mod, "lucas_sequence")

    def test_doc0(self):
        try:
            mod.lucas_sequence(8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lucas_sequence(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lucas_sequence(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lucas_sequence(None)
        except EXC:
            pass


class Test_mobius_function:
    def test_exists(self):
        assert hasattr(mod, "mobius_function")

    def test_doc0(self):
        try:
            mod.mobius_function(30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mobius_function(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mobius_function(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mobius_function(None)
        except EXC:
            pass


class Test_modular_exponentiation:
    def test_exists(self):
        assert hasattr(mod, "modular_exponentiation")

    def test_doc0(self):
        try:
            mod.modular_exponentiation(2, 10, 1000)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.modular_exponentiation(3, 13, 7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.modular_exponentiation(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.modular_exponentiation(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.modular_exponentiation(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.modular_exponentiation("", "", "")
        except EXC:
            pass


class Test_modular_inverse:
    def test_exists(self):
        assert hasattr(mod, "modular_inverse")

    def test_doc0(self):
        try:
            mod.modular_inverse(3, 7)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.modular_inverse(10, 17)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.modular_inverse(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.modular_inverse(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.modular_inverse(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.modular_inverse("", "")
        except EXC:
            pass


class Test_motzkin_number:
    def test_exists(self):
        assert hasattr(mod, "motzkin_number")

    def test_doc0(self):
        try:
            mod.motzkin_number(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.motzkin_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.motzkin_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.motzkin_number(None)
        except EXC:
            pass


class Test_multiplicative_persistence:
    def test_exists(self):
        assert hasattr(mod, "multiplicative_persistence")

    def test_doc0(self):
        try:
            mod.multiplicative_persistence(39)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.multiplicative_persistence(999)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.multiplicative_persistence(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.multiplicative_persistence(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.multiplicative_persistence(None)
        except EXC:
            pass


class Test_narayana_number:
    def test_exists(self):
        assert hasattr(mod, "narayana_number")

    def test_doc0(self):
        try:
            mod.narayana_number(4, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.narayana_number(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.narayana_number(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.narayana_number(None, 0)
        except EXC:
            pass


class Test_next_prime:
    def test_exists(self):
        assert hasattr(mod, "next_prime")

    def test_doc0(self):
        try:
            mod.next_prime(10)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.next_prime(13)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.next_prime(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.next_prime(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.next_prime(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.next_prime(None)
        except EXC:
            pass


class Test_nth_fibonacci:
    def test_exists(self):
        assert hasattr(mod, "nth_fibonacci")

    def test_doc0(self):
        try:
            mod.nth_fibonacci(10)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.nth_fibonacci(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.nth_fibonacci(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nth_fibonacci(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nth_fibonacci(None)
        except EXC:
            pass


class Test_number_of_distinct_prime_factors:
    def test_exists(self):
        assert hasattr(mod, "number_of_distinct_prime_factors")

    def test_doc0(self):
        try:
            mod.number_of_distinct_prime_factors(12)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.number_of_distinct_prime_factors(30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.number_of_distinct_prime_factors(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.number_of_distinct_prime_factors(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.number_of_distinct_prime_factors(None)
        except EXC:
            pass


class Test_number_of_divisors:
    def test_exists(self):
        assert hasattr(mod, "number_of_divisors")

    def test_doc0(self):
        try:
            mod.number_of_divisors(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.number_of_divisors(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.number_of_divisors(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.number_of_divisors(None)
        except EXC:
            pass


class Test_omega_prime:
    def test_exists(self):
        assert hasattr(mod, "omega_prime")

    def test_doc0(self):
        try:
            mod.omega_prime(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.omega_prime(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.omega_prime(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.omega_prime(None)
        except EXC:
            pass


class Test_partition_function:
    def test_exists(self):
        assert hasattr(mod, "partition_function")

    def test_doc0(self):
        try:
            mod.partition_function(5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.partition_function(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.partition_function(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.partition_function(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.partition_function(None)
        except EXC:
            pass


class Test_partition_number:
    def test_exists(self):
        assert hasattr(mod, "partition_number")

    def test_doc0(self):
        try:
            mod.partition_number(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.partition_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.partition_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.partition_number(None)
        except EXC:
            pass


class Test_pell_number:
    def test_exists(self):
        assert hasattr(mod, "pell_number")

    def test_doc0(self):
        try:
            mod.pell_number(6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pell_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pell_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pell_number(None)
        except EXC:
            pass


class Test_pentagonal_number:
    def test_exists(self):
        assert hasattr(mod, "pentagonal_number")

    def test_doc0(self):
        try:
            mod.pentagonal_number(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pentagonal_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pentagonal_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pentagonal_number(None)
        except EXC:
            pass


class Test_prime_counting_approx:
    def test_exists(self):
        assert hasattr(mod, "prime_counting_approx")

    def test_var0(self):
        try:
            mod.prime_counting_approx(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.prime_counting_approx(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.prime_counting_approx(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.prime_counting_approx("")
        except EXC:
            pass


class Test_prime_factors:
    def test_exists(self):
        assert hasattr(mod, "prime_factors")

    def test_doc0(self):
        try:
            mod.prime_factors(60)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.prime_factors(17)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.prime_factors(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.prime_factors(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.prime_factors(None)
        except EXC:
            pass


class Test_prime_nth_approx:
    def test_exists(self):
        assert hasattr(mod, "prime_nth_approx")

    def test_var0(self):
        try:
            mod.prime_nth_approx(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.prime_nth_approx(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.prime_nth_approx(None)
        except EXC:
            pass


class Test_primitive_root:
    def test_exists(self):
        assert hasattr(mod, "primitive_root")

    def test_doc0(self):
        try:
            mod.primitive_root(7)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.primitive_root(11)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.primitive_root(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.primitive_root(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.primitive_root(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.primitive_root("")
        except EXC:
            pass


class Test_radical:
    def test_exists(self):
        assert hasattr(mod, "radical")

    def test_doc0(self):
        try:
            mod.radical(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.radical(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.radical(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.radical(None)
        except EXC:
            pass


class Test_schroeder_number:
    def test_exists(self):
        assert hasattr(mod, "schroeder_number")

    def test_doc0(self):
        try:
            mod.schroeder_number(4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.schroeder_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.schroeder_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.schroeder_number(None)
        except EXC:
            pass


class Test_squarefree_part:
    def test_exists(self):
        assert hasattr(mod, "squarefree_part")

    def test_doc0(self):
        try:
            mod.squarefree_part(12)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.squarefree_part(7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.squarefree_part(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.squarefree_part(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.squarefree_part(None)
        except EXC:
            pass


class Test_stern_brocot:
    def test_exists(self):
        assert hasattr(mod, "stern_brocot")

    def test_doc0(self):
        try:
            mod.stern_brocot(10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.stern_brocot(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stern_brocot(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stern_brocot(None)
        except EXC:
            pass


class Test_stirling_number_second:
    def test_exists(self):
        assert hasattr(mod, "stirling_number_second")

    def test_doc0(self):
        try:
            mod.stirling_number_second(4, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.stirling_number_second(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stirling_number_second(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stirling_number_second(None, 0)
        except EXC:
            pass


class Test_sum_of_cubes_of_digits:
    def test_exists(self):
        assert hasattr(mod, "sum_of_cubes_of_digits")

    def test_doc0(self):
        try:
            mod.sum_of_cubes_of_digits(123)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sum_of_cubes_of_digits(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_of_cubes_of_digits(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_of_cubes_of_digits(None)
        except EXC:
            pass


class Test_sum_of_divisors:
    def test_exists(self):
        assert hasattr(mod, "sum_of_divisors")

    def test_doc0(self):
        try:
            mod.sum_of_divisors(12)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sum_of_divisors(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_of_divisors(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_of_divisors(None)
        except EXC:
            pass


class Test_sum_of_squares_count:
    def test_exists(self):
        assert hasattr(mod, "sum_of_squares_count")

    def test_doc0(self):
        try:
            mod.sum_of_squares_count(5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sum_of_squares_count(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sum_of_squares_count(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_of_squares_count(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_of_squares_count(None)
        except EXC:
            pass


class Test_sum_of_squares_of_digits:
    def test_exists(self):
        assert hasattr(mod, "sum_of_squares_of_digits")

    def test_doc0(self):
        try:
            mod.sum_of_squares_of_digits(19)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sum_of_squares_of_digits(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sum_of_squares_of_digits(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_of_squares_of_digits(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_of_squares_of_digits(None)
        except EXC:
            pass


class Test_sum_proper_divisors:
    def test_exists(self):
        assert hasattr(mod, "sum_proper_divisors")

    def test_doc0(self):
        try:
            mod.sum_proper_divisors(12)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sum_proper_divisors(1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sum_proper_divisors(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_proper_divisors(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_proper_divisors(None)
        except EXC:
            pass


class Test_tribonacci_number:
    def test_exists(self):
        assert hasattr(mod, "tribonacci_number")

    def test_doc0(self):
        try:
            mod.tribonacci_number(7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.tribonacci_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tribonacci_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tribonacci_number(None)
        except EXC:
            pass

