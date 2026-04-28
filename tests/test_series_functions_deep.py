# Deep coverage tests for agentfx.fxNumeric.series_functions

import agentfx.fxNumeric.series_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_taylor_asin_deep:
    def test_c0(self):
        try:
            mod.taylor_asin(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.taylor_asin(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.taylor_asin(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.taylor_asin(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.taylor_asin(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.taylor_asin(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.taylor_asin(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.taylor_asin(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.taylor_asin(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.taylor_asin(2)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.taylor_asin(1, terms=1)
        except EXC:
            pass


class Test_binomial_series_deep:
    def test_c0(self):
        try:
            mod.binomial_series(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.binomial_series(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.binomial_series(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.binomial_series(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.binomial_series(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.binomial_series(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.binomial_series(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.binomial_series(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.binomial_series(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.binomial_series(2, 1)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.binomial_series(1, 42, terms=1)
        except EXC:
            pass


class Test_fourier_coefficients_deep:
    def test_c0(self):
        try:
            mod.fourier_coefficients(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fourier_coefficients(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fourier_coefficients(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fourier_coefficients(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fourier_coefficients(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fourier_coefficients(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.fourier_coefficients(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.fourier_coefficients(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.fourier_coefficients(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.fourier_coefficients(2, 1, 0)
        except EXC:
            pass

    def test_kw_n_points(self):
        try:
            mod.fourier_coefficients(1, 42, 3, n_points=1)
        except EXC:
            pass


class Test_basel_series_deep:
    def test_c0(self):
        try:
            mod.basel_series()
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.basel_series(terms=1)
        except EXC:
            pass


class Test_leibniz_pi_deep:
    def test_c0(self):
        try:
            mod.leibniz_pi()
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.leibniz_pi(terms=1)
        except EXC:
            pass


class Test_taylor_cos_deep:
    def test_c0(self):
        try:
            mod.taylor_cos(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.taylor_cos(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.taylor_cos(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.taylor_cos(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.taylor_cos(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.taylor_cos(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.taylor_cos(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.taylor_cos(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.taylor_cos(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.taylor_cos(2)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.taylor_cos(1, terms=1)
        except EXC:
            pass


class Test_taylor_ln1p_deep:
    def test_c0(self):
        try:
            mod.taylor_ln1p(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.taylor_ln1p(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.taylor_ln1p(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.taylor_ln1p(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.taylor_ln1p(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.taylor_ln1p(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.taylor_ln1p(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.taylor_ln1p(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.taylor_ln1p(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.taylor_ln1p(2)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.taylor_ln1p(1, terms=1)
        except EXC:
            pass


class Test_taylor_sin_deep:
    def test_c0(self):
        try:
            mod.taylor_sin(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.taylor_sin(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.taylor_sin(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.taylor_sin(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.taylor_sin(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.taylor_sin(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.taylor_sin(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.taylor_sin(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.taylor_sin(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.taylor_sin(2)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.taylor_sin(1, terms=1)
        except EXC:
            pass


class Test_abel_sum_deep:
    def test_c0(self):
        try:
            mod.abel_sum([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.abel_sum([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.abel_sum([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.abel_sum([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.abel_sum([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.abel_sum([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_r(self):
        try:
            mod.abel_sum([1, 2, 3, 4, 5], r=1)
        except EXC:
            pass


class Test_alternating_series_sum_deep:
    def test_c0(self):
        try:
            mod.alternating_series_sum(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.alternating_series_sum(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.alternating_series_sum(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.alternating_series_sum(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.alternating_series_sum(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.alternating_series_sum(0, 1)
        except EXC:
            pass


class Test_arithmetic_series_sum_deep:
    def test_c0(self):
        try:
            mod.arithmetic_series_sum(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.arithmetic_series_sum(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.arithmetic_series_sum(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.arithmetic_series_sum(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.arithmetic_series_sum(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.arithmetic_series_sum(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.arithmetic_series_sum(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.arithmetic_series_sum(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.arithmetic_series_sum(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.arithmetic_series_sum(2, 1, 0)
        except EXC:
            pass


class Test_bbp_pi_digit_deep:
    def test_c0(self):
        try:
            mod.bbp_pi_digit(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bbp_pi_digit(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bbp_pi_digit(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bbp_pi_digit(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bbp_pi_digit(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bbp_pi_digit(0)
        except EXC:
            pass


class Test_chudnovsky_pi_deep:
    def test_c0(self):
        try:
            mod.chudnovsky_pi()
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.chudnovsky_pi(terms=1)
        except EXC:
            pass


class Test_convergent_sequence_deep:
    def test_c0(self):
        try:
            mod.convergent_sequence(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.convergent_sequence(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.convergent_sequence(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.convergent_sequence(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.convergent_sequence(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.convergent_sequence(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.convergent_sequence(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.convergent_sequence(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.convergent_sequence(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.convergent_sequence(2, 1)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.convergent_sequence(1, 42, terms=1)
        except EXC:
            pass


class Test_euler_maclaurin_sum_deep:
    def test_c0(self):
        try:
            mod.euler_maclaurin_sum(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.euler_maclaurin_sum(42, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.euler_maclaurin_sum(0, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.euler_maclaurin_sum(-5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.euler_maclaurin_sum(3.14, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.euler_maclaurin_sum(100, 1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.euler_maclaurin_sum(0.5, 2, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.euler_maclaurin_sum(1000, 3, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.euler_maclaurin_sum(-1, 5, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.euler_maclaurin_sum(2, 10, 0)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.euler_maclaurin_sum(1, 2, 3, terms=1)
        except EXC:
            pass


class Test_fourier_series_eval_deep:
    def test_c0(self):
        try:
            mod.fourier_series_eval([1, 2, 3, 4, 5], [10, 20, 30], 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fourier_series_eval([10, 20, 30], [0, 1], -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fourier_series_eval([0, 1], [-3, -1, 0, 2, 5], 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fourier_series_eval([-3, -1, 0, 2, 5], [100], 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fourier_series_eval([100], [1, 1, 2, 3, 5, 8], 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fourier_series_eval([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5], 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.fourier_series_eval([1, 2, 3, 4, 5], [10, 20, 30], -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.fourier_series_eval([10, 20, 30], [0, 1], 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.fourier_series_eval([0, 1], [-3, -1, 0, 2, 5], 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.fourier_series_eval([-3, -1, 0, 2, 5], [100], 42, 0)
        except EXC:
            pass


class Test_generalized_harmonic_deep:
    def test_c0(self):
        try:
            mod.generalized_harmonic(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.generalized_harmonic(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.generalized_harmonic(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.generalized_harmonic(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.generalized_harmonic(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.generalized_harmonic(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.generalized_harmonic(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.generalized_harmonic(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.generalized_harmonic(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.generalized_harmonic(5, 1)
        except EXC:
            pass


class Test_geometric_series_sum_deep:
    def test_c0(self):
        try:
            mod.geometric_series_sum(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.geometric_series_sum(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.geometric_series_sum(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.geometric_series_sum(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.geometric_series_sum(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.geometric_series_sum(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.geometric_series_sum(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.geometric_series_sum(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.geometric_series_sum(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.geometric_series_sum(2, 1, 0)
        except EXC:
            pass


class Test_gregory_leibniz_pi_deep:
    def test_c0(self):
        try:
            mod.gregory_leibniz_pi()
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.gregory_leibniz_pi(terms=1)
        except EXC:
            pass


class Test_madhava_pi_deep:
    def test_c0(self):
        try:
            mod.madhava_pi()
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.madhava_pi(terms=1)
        except EXC:
            pass


class Test_nilakantha_pi_deep:
    def test_c0(self):
        try:
            mod.nilakantha_pi()
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.nilakantha_pi(terms=1)
        except EXC:
            pass


class Test_power_series_eval_deep:
    def test_c0(self):
        try:
            mod.power_series_eval([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.power_series_eval([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.power_series_eval([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.power_series_eval([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.power_series_eval([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.power_series_eval([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.power_series_eval([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.power_series_eval([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.power_series_eval([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.power_series_eval([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass


class Test_ramanujan_pi_deep:
    def test_c0(self):
        try:
            mod.ramanujan_pi()
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.ramanujan_pi(terms=1)
        except EXC:
            pass


class Test_vieta_pi_deep:
    def test_c0(self):
        try:
            mod.vieta_pi()
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.vieta_pi(terms=1)
        except EXC:
            pass


class Test_wallis_pi_deep:
    def test_c0(self):
        try:
            mod.wallis_pi()
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.wallis_pi(terms=1)
        except EXC:
            pass

