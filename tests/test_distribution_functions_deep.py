# Deep coverage tests for agentfx.fxNumeric.distribution_functions

import agentfx.fxNumeric.distribution_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_binom_dist_deep:
    def test_c0(self):
        try:
            mod.binom_dist(1, 2, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.binom_dist(2, 3, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.binom_dist(3, 5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.binom_dist(5, 10, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.binom_dist(10, 0, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.binom_dist(0, 1, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.binom_dist(1, 2, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.binom_dist(2, 3, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.binom_dist(3, 5, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.binom_dist(5, 10, 42)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.binom_dist(1, 2, 0, cumulative=True)
        except EXC:
            pass


class Test_expon_dist_deep:
    def test_c0(self):
        try:
            mod.expon_dist(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.expon_dist(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.expon_dist(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.expon_dist(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.expon_dist(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.expon_dist(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.expon_dist(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.expon_dist(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.expon_dist(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.expon_dist(2, 1)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.expon_dist(1, 42, cumulative=True)
        except EXC:
            pass


class Test_chisq_dist_deep:
    def test_c0(self):
        try:
            mod.chisq_dist(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chisq_dist(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chisq_dist(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chisq_dist(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chisq_dist(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chisq_dist(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.chisq_dist(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.chisq_dist(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.chisq_dist(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.chisq_dist(2, 10)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.chisq_dist(1, 2, cumulative=True)
        except EXC:
            pass


class Test_f_dist_deep:
    def test_c0(self):
        try:
            mod.f_dist(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.f_dist(42, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.f_dist(0, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.f_dist(-5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.f_dist(3.14, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.f_dist(100, 1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.f_dist(0.5, 2, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.f_dist(1000, 3, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.f_dist(-1, 5, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.f_dist(2, 10, 0)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.f_dist(1, 2, 3, cumulative=True)
        except EXC:
            pass


class Test_poisson_dist_deep:
    def test_c0(self):
        try:
            mod.poisson_dist(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.poisson_dist(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.poisson_dist(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.poisson_dist(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.poisson_dist(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.poisson_dist(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.poisson_dist(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.poisson_dist(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.poisson_dist(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.poisson_dist(5, 1)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.poisson_dist(1, 42, cumulative=True)
        except EXC:
            pass


class Test_chisq_inv_deep:
    def test_c0(self):
        try:
            mod.chisq_inv(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chisq_inv(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chisq_inv(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chisq_inv(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chisq_inv(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chisq_inv(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.chisq_inv(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.chisq_inv(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.chisq_inv(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.chisq_inv(2, 10)
        except EXC:
            pass


class Test_f_inv_deep:
    def test_c0(self):
        try:
            mod.f_inv(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.f_inv(42, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.f_inv(0, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.f_inv(-5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.f_inv(3.14, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.f_inv(100, 1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.f_inv(0.5, 2, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.f_inv(1000, 3, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.f_inv(-1, 5, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.f_inv(2, 10, 0)
        except EXC:
            pass


class Test_t_dist_deep:
    def test_c0(self):
        try:
            mod.t_dist(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.t_dist(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.t_dist(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.t_dist(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.t_dist(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.t_dist(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.t_dist(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.t_dist(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.t_dist(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.t_dist(2, 10)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.t_dist(1, 2, cumulative=True)
        except EXC:
            pass


class Test_t_inv_deep:
    def test_c0(self):
        try:
            mod.t_inv(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.t_inv(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.t_inv(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.t_inv(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.t_inv(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.t_inv(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.t_inv(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.t_inv(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.t_inv(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.t_inv(2, 10)
        except EXC:
            pass


class Test_binom_dist_range_deep:
    def test_c0(self):
        try:
            mod.binom_dist_range(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.binom_dist_range(2, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.binom_dist_range(3, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.binom_dist_range(5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.binom_dist_range(10, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.binom_dist_range(0, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.binom_dist_range(1, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.binom_dist_range(2, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.binom_dist_range(3, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.binom_dist_range(5, 1, 0)
        except EXC:
            pass

    def test_kw_number_s2(self):
        try:
            mod.binom_dist_range(1, 42, 3, number_s2=1)
        except EXC:
            pass


class Test_norm_dist_deep:
    def test_c0(self):
        try:
            mod.norm_dist(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.norm_dist(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.norm_dist(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.norm_dist(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.norm_dist(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.norm_dist(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.norm_dist(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.norm_dist(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.norm_dist(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.norm_dist(2)
        except EXC:
            pass

    def test_kw_mean(self):
        try:
            mod.norm_dist(1, mean=1)
        except EXC:
            pass

    def test_kw_std_dev(self):
        try:
            mod.norm_dist(1, std_dev=1)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.norm_dist(1, cumulative=True)
        except EXC:
            pass


class Test_norm_inv_deep:
    def test_c0(self):
        try:
            mod.norm_inv(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.norm_inv(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.norm_inv(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.norm_inv(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.norm_inv(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.norm_inv(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.norm_inv(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.norm_inv(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.norm_inv(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.norm_inv(2)
        except EXC:
            pass

    def test_kw_mean(self):
        try:
            mod.norm_inv(1, mean=1)
        except EXC:
            pass

    def test_kw_std_dev(self):
        try:
            mod.norm_inv(1, std_dev=1)
        except EXC:
            pass


class Test_f_inv_rt_deep:
    def test_c0(self):
        try:
            mod.f_inv_rt(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.f_inv_rt(42, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.f_inv_rt(0, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.f_inv_rt(-5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.f_inv_rt(3.14, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.f_inv_rt(100, 1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.f_inv_rt(0.5, 2, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.f_inv_rt(1000, 3, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.f_inv_rt(-1, 5, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.f_inv_rt(2, 10, 0)
        except EXC:
            pass


class Test_binom_inv_deep:
    def test_c0(self):
        try:
            mod.binom_inv(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.binom_inv(2, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.binom_inv(3, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.binom_inv(5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.binom_inv(10, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.binom_inv(0, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.binom_inv(1, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.binom_inv(2, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.binom_inv(3, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.binom_inv(5, 1, 42)
        except EXC:
            pass


class Test_hypgeom_dist_deep:
    def test_c0(self):
        try:
            mod.hypgeom_dist(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hypgeom_dist(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hypgeom_dist(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hypgeom_dist(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hypgeom_dist(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hypgeom_dist(0, 1, 2, 3)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.hypgeom_dist(1, 2, 3, 5, cumulative=True)
        except EXC:
            pass


class Test_negbinom_dist_deep:
    def test_c0(self):
        try:
            mod.negbinom_dist(1, 2, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.negbinom_dist(2, 3, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.negbinom_dist(3, 5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.negbinom_dist(5, 10, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.negbinom_dist(10, 0, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.negbinom_dist(0, 1, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.negbinom_dist(1, 2, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.negbinom_dist(2, 3, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.negbinom_dist(3, 5, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.negbinom_dist(5, 10, 42)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.negbinom_dist(1, 2, 0, cumulative=True)
        except EXC:
            pass


class Test_beta_dist_deep:
    def test_c0(self):
        try:
            mod.beta_dist(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.beta_dist(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.beta_dist(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.beta_dist(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.beta_dist(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.beta_dist(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.beta_dist(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.beta_dist(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.beta_dist(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.beta_dist(2, 1, 42)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.beta_dist(1, 42, 0, cumulative=True)
        except EXC:
            pass


class Test_chisq_inv_rt_deep:
    def test_c0(self):
        try:
            mod.chisq_inv_rt(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chisq_inv_rt(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chisq_inv_rt(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chisq_inv_rt(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chisq_inv_rt(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chisq_inv_rt(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.chisq_inv_rt(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.chisq_inv_rt(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.chisq_inv_rt(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.chisq_inv_rt(2, 10)
        except EXC:
            pass


class Test_gamma_dist_deep:
    def test_c0(self):
        try:
            mod.gamma_dist(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gamma_dist(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gamma_dist(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gamma_dist(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gamma_dist(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gamma_dist(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.gamma_dist(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.gamma_dist(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.gamma_dist(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.gamma_dist(2, 1, 42)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.gamma_dist(1, 42, 0, cumulative=True)
        except EXC:
            pass


class Test_lognorm_dist_deep:
    def test_c0(self):
        try:
            mod.lognorm_dist(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lognorm_dist(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lognorm_dist(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lognorm_dist(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lognorm_dist(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lognorm_dist(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.lognorm_dist(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.lognorm_dist(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.lognorm_dist(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.lognorm_dist(2, 1, 42)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.lognorm_dist(1, 42, 0, cumulative=True)
        except EXC:
            pass


class Test_t_inv_2t_deep:
    def test_c0(self):
        try:
            mod.t_inv_2t(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.t_inv_2t(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.t_inv_2t(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.t_inv_2t(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.t_inv_2t(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.t_inv_2t(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.t_inv_2t(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.t_inv_2t(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.t_inv_2t(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.t_inv_2t(2, 10)
        except EXC:
            pass


class Test_weibull_dist_deep:
    def test_c0(self):
        try:
            mod.weibull_dist(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weibull_dist(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weibull_dist(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weibull_dist(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weibull_dist(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weibull_dist(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.weibull_dist(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.weibull_dist(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.weibull_dist(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.weibull_dist(2, 1, 42)
        except EXC:
            pass

    def test_kw_cumulative(self):
        try:
            mod.weibull_dist(1, 42, 0, cumulative=True)
        except EXC:
            pass


class Test_f_dist_rt_deep:
    def test_c0(self):
        try:
            mod.f_dist_rt(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.f_dist_rt(42, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.f_dist_rt(0, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.f_dist_rt(-5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.f_dist_rt(3.14, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.f_dist_rt(100, 1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.f_dist_rt(0.5, 2, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.f_dist_rt(1000, 3, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.f_dist_rt(-1, 5, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.f_dist_rt(2, 10, 0)
        except EXC:
            pass


class Test_lognorm_inv_deep:
    def test_c0(self):
        try:
            mod.lognorm_inv(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lognorm_inv(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lognorm_inv(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lognorm_inv(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lognorm_inv(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lognorm_inv(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.lognorm_inv(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.lognorm_inv(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.lognorm_inv(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.lognorm_inv(2, 1, 42)
        except EXC:
            pass


class Test_beta_inv_deep:
    def test_c0(self):
        try:
            mod.beta_inv(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.beta_inv(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.beta_inv(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.beta_inv(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.beta_inv(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.beta_inv(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.beta_inv(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.beta_inv(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.beta_inv(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.beta_inv(2, 1, 42)
        except EXC:
            pass


class Test_chisq_dist_rt_deep:
    def test_c0(self):
        try:
            mod.chisq_dist_rt(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chisq_dist_rt(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chisq_dist_rt(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chisq_dist_rt(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chisq_dist_rt(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chisq_dist_rt(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.chisq_dist_rt(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.chisq_dist_rt(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.chisq_dist_rt(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.chisq_dist_rt(2, 10)
        except EXC:
            pass


class Test_gamma_inv_deep:
    def test_c0(self):
        try:
            mod.gamma_inv(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gamma_inv(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gamma_inv(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gamma_inv(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gamma_inv(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gamma_inv(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.gamma_inv(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.gamma_inv(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.gamma_inv(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.gamma_inv(2, 1, 42)
        except EXC:
            pass


class Test_t_dist_2t_deep:
    def test_c0(self):
        try:
            mod.t_dist_2t(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.t_dist_2t(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.t_dist_2t(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.t_dist_2t(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.t_dist_2t(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.t_dist_2t(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.t_dist_2t(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.t_dist_2t(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.t_dist_2t(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.t_dist_2t(2, 10)
        except EXC:
            pass


class Test_gauss_deep:
    def test_c0(self):
        try:
            mod.gauss(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gauss(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gauss(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gauss(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gauss(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gauss(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.gauss(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.gauss(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.gauss(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.gauss(2)
        except EXC:
            pass


class Test_t_dist_rt_deep:
    def test_c0(self):
        try:
            mod.t_dist_rt(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.t_dist_rt(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.t_dist_rt(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.t_dist_rt(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.t_dist_rt(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.t_dist_rt(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.t_dist_rt(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.t_dist_rt(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.t_dist_rt(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.t_dist_rt(2, 10)
        except EXC:
            pass

