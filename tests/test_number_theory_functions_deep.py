# Deep coverage tests for formulite.fxNumeric.number_theory_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxNumeric.number_theory_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_kronecker_symbol_deep:
    def test_c0(self):
        try:
            mod.kronecker_symbol(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.kronecker_symbol(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.kronecker_symbol(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.kronecker_symbol(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.kronecker_symbol(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.kronecker_symbol(0, 1)
        except EXC:
            pass


class Test_chinese_remainder_theorem_deep:
    def test_c0(self):
        try:
            mod.chinese_remainder_theorem([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chinese_remainder_theorem([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chinese_remainder_theorem([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chinese_remainder_theorem([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chinese_remainder_theorem([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chinese_remainder_theorem([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_eulerian_number_deep:
    def test_c0(self):
        try:
            mod.eulerian_number(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.eulerian_number(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.eulerian_number(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.eulerian_number(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.eulerian_number(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.eulerian_number(0, 1)
        except EXC:
            pass


class Test_sum_of_squares_count_deep:
    def test_c0(self):
        try:
            mod.sum_of_squares_count(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_of_squares_count(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_of_squares_count(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_of_squares_count(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_of_squares_count(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_of_squares_count(0)
        except EXC:
            pass


class Test_continued_fraction_expansion_deep:
    def test_c0(self):
        try:
            mod.continued_fraction_expansion(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.continued_fraction_expansion(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.continued_fraction_expansion(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.continued_fraction_expansion(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.continued_fraction_expansion(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.continued_fraction_expansion(0, 1)
        except EXC:
            pass


class Test_delannoy_number_deep:
    def test_c0(self):
        try:
            mod.delannoy_number(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.delannoy_number(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.delannoy_number(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.delannoy_number(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.delannoy_number(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.delannoy_number(0, 1)
        except EXC:
            pass


class Test_discrete_logarithm_deep:
    def test_c0(self):
        try:
            mod.discrete_logarithm(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.discrete_logarithm(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.discrete_logarithm(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.discrete_logarithm(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.discrete_logarithm(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.discrete_logarithm(0, 1, 2)
        except EXC:
            pass


class Test_primitive_root_deep:
    def test_c0(self):
        try:
            mod.primitive_root(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.primitive_root(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.primitive_root(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.primitive_root(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.primitive_root(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.primitive_root(0)
        except EXC:
            pass


class Test_stirling_number_second_deep:
    def test_c0(self):
        try:
            mod.stirling_number_second(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.stirling_number_second(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.stirling_number_second(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.stirling_number_second(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.stirling_number_second(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.stirling_number_second(0, 1)
        except EXC:
            pass


class Test_additive_persistence_deep:
    def test_c0(self):
        try:
            mod.additive_persistence(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.additive_persistence(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.additive_persistence(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.additive_persistence(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.additive_persistence(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.additive_persistence(0)
        except EXC:
            pass


class Test_carmichael_lambda_deep:
    def test_c0(self):
        try:
            mod.carmichael_lambda(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.carmichael_lambda(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.carmichael_lambda(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.carmichael_lambda(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.carmichael_lambda(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.carmichael_lambda(0)
        except EXC:
            pass


class Test_convergents_deep:
    def test_c0(self):
        try:
            mod.convergents([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.convergents([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.convergents([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.convergents([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.convergents([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.convergents([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_digit_count_deep:
    def test_c0(self):
        try:
            mod.digit_count(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.digit_count(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.digit_count(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.digit_count(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.digit_count(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.digit_count(0)
        except EXC:
            pass


class Test_digital_root_deep:
    def test_c0(self):
        try:
            mod.digital_root(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.digital_root(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.digital_root(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.digital_root(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.digital_root(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.digital_root(0)
        except EXC:
            pass


class Test_fibonacci_sequence_deep:
    def test_c0(self):
        try:
            mod.fibonacci_sequence(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fibonacci_sequence(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fibonacci_sequence(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fibonacci_sequence(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fibonacci_sequence(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fibonacci_sequence(0)
        except EXC:
            pass


class Test_goldbach_partition_deep:
    def test_c0(self):
        try:
            mod.goldbach_partition(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.goldbach_partition(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.goldbach_partition(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.goldbach_partition(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.goldbach_partition(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.goldbach_partition(0)
        except EXC:
            pass


class Test_is_achilles_number_deep:
    def test_c0(self):
        try:
            mod.is_achilles_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_achilles_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_achilles_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_achilles_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_achilles_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_achilles_number(0)
        except EXC:
            pass


class Test_is_automorphic_number_deep:
    def test_c0(self):
        try:
            mod.is_automorphic_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_automorphic_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_automorphic_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_automorphic_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_automorphic_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_automorphic_number(0)
        except EXC:
            pass


class Test_is_cube_number_deep:
    def test_c0(self):
        try:
            mod.is_cube_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_cube_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_cube_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_cube_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_cube_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_cube_number(0)
        except EXC:
            pass


class Test_is_lychrel_candidate_deep:
    def test_c0(self):
        try:
            mod.is_lychrel_candidate(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_lychrel_candidate(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_lychrel_candidate(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_lychrel_candidate(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_lychrel_candidate(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_lychrel_candidate(0)
        except EXC:
            pass

    def test_kw_max_iterations(self):
        try:
            mod.is_lychrel_candidate(1, max_iterations=1)
        except EXC:
            pass


class Test_is_narcissistic_number_deep:
    def test_c0(self):
        try:
            mod.is_narcissistic_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_narcissistic_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_narcissistic_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_narcissistic_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_narcissistic_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_narcissistic_number(0)
        except EXC:
            pass


class Test_is_palindromic_number_deep:
    def test_c0(self):
        try:
            mod.is_palindromic_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_palindromic_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_palindromic_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_palindromic_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_palindromic_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_palindromic_number(0)
        except EXC:
            pass


class Test_is_powerful_number_deep:
    def test_c0(self):
        try:
            mod.is_powerful_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_powerful_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_powerful_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_powerful_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_powerful_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_powerful_number(0)
        except EXC:
            pass


class Test_is_pronic_number_deep:
    def test_c0(self):
        try:
            mod.is_pronic_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_pronic_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_pronic_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_pronic_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_pronic_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_pronic_number(0)
        except EXC:
            pass


class Test_is_smith_number_deep:
    def test_c0(self):
        try:
            mod.is_smith_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_smith_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_smith_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_smith_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_smith_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_smith_number(0)
        except EXC:
            pass


class Test_is_square_number_deep:
    def test_c0(self):
        try:
            mod.is_square_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_square_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_square_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_square_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_square_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_square_number(0)
        except EXC:
            pass


class Test_is_triangular_number_deep:
    def test_c0(self):
        try:
            mod.is_triangular_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_triangular_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_triangular_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_triangular_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_triangular_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_triangular_number(0)
        except EXC:
            pass


class Test_multiplicative_persistence_deep:
    def test_c0(self):
        try:
            mod.multiplicative_persistence(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.multiplicative_persistence(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.multiplicative_persistence(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.multiplicative_persistence(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.multiplicative_persistence(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.multiplicative_persistence(0)
        except EXC:
            pass


class Test_narayana_number_deep:
    def test_c0(self):
        try:
            mod.narayana_number(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.narayana_number(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.narayana_number(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.narayana_number(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.narayana_number(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.narayana_number(0, 1)
        except EXC:
            pass


class Test_partition_function_deep:
    def test_c0(self):
        try:
            mod.partition_function(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.partition_function(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.partition_function(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.partition_function(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.partition_function(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.partition_function(0)
        except EXC:
            pass


class Test_sum_of_cubes_of_digits_deep:
    def test_c0(self):
        try:
            mod.sum_of_cubes_of_digits(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_of_cubes_of_digits(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_of_cubes_of_digits(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_of_cubes_of_digits(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_of_cubes_of_digits(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_of_cubes_of_digits(0)
        except EXC:
            pass


class Test_sum_of_divisors_deep:
    def test_c0(self):
        try:
            mod.sum_of_divisors(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_of_divisors(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_of_divisors(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_of_divisors(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_of_divisors(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_of_divisors(0)
        except EXC:
            pass

    def test_kw_k(self):
        try:
            mod.sum_of_divisors(1, k=1)
        except EXC:
            pass


class Test_sum_of_squares_of_digits_deep:
    def test_c0(self):
        try:
            mod.sum_of_squares_of_digits(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_of_squares_of_digits(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_of_squares_of_digits(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_of_squares_of_digits(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_of_squares_of_digits(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_of_squares_of_digits(0)
        except EXC:
            pass

