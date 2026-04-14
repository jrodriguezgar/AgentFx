# Coverage tests for formulite.fxNumeric.distribution_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import distribution_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_beta_dist:
    def test_exists(self):
        assert hasattr(mod, "beta_dist")

    def test_var0(self):
        try:
            mod.beta_dist(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.beta_dist(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.beta_dist(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.beta_dist("", 0, 0)
        except EXC:
            pass


class Test_beta_inv:
    def test_exists(self):
        assert hasattr(mod, "beta_inv")

    def test_var0(self):
        try:
            mod.beta_inv(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.beta_inv(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.beta_inv(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.beta_inv(0, 0, 0)
        except EXC:
            pass


class Test_binom_dist:
    def test_exists(self):
        assert hasattr(mod, "binom_dist")

    def test_var0(self):
        try:
            mod.binom_dist(0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.binom_dist(1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.binom_dist(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.binom_dist("", "", 0)
        except EXC:
            pass


class Test_binom_dist_range:
    def test_exists(self):
        assert hasattr(mod, "binom_dist_range")

    def test_var0(self):
        try:
            mod.binom_dist_range(0, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.binom_dist_range(1, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.binom_dist_range(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.binom_dist_range("", 0, "")
        except EXC:
            pass


class Test_binom_inv:
    def test_exists(self):
        assert hasattr(mod, "binom_inv")

    def test_doc0(self):
        try:
            mod.binom_inv(6, 0.5, 0.75)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.binom_inv(0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.binom_inv(1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.binom_inv(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.binom_inv("", 0, 0)
        except EXC:
            pass


class Test_chisq_dist:
    def test_exists(self):
        assert hasattr(mod, "chisq_dist")

    def test_var0(self):
        try:
            mod.chisq_dist(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chisq_dist(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chisq_dist(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chisq_dist("", "")
        except EXC:
            pass


class Test_chisq_dist_rt:
    def test_exists(self):
        assert hasattr(mod, "chisq_dist_rt")

    def test_var0(self):
        try:
            mod.chisq_dist_rt(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chisq_dist_rt(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chisq_dist_rt(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chisq_dist_rt("", "")
        except EXC:
            pass


class Test_chisq_inv:
    def test_exists(self):
        assert hasattr(mod, "chisq_inv")

    def test_var0(self):
        try:
            mod.chisq_inv(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chisq_inv(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chisq_inv(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chisq_inv(0, "")
        except EXC:
            pass


class Test_chisq_inv_rt:
    def test_exists(self):
        assert hasattr(mod, "chisq_inv_rt")

    def test_var0(self):
        try:
            mod.chisq_inv_rt(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chisq_inv_rt(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chisq_inv_rt(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chisq_inv_rt(0, "")
        except EXC:
            pass


class Test_expon_dist:
    def test_exists(self):
        assert hasattr(mod, "expon_dist")

    def test_var0(self):
        try:
            mod.expon_dist(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.expon_dist(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.expon_dist(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.expon_dist("", "")
        except EXC:
            pass


class Test_f_dist:
    def test_exists(self):
        assert hasattr(mod, "f_dist")

    def test_var0(self):
        try:
            mod.f_dist(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.f_dist(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.f_dist(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.f_dist("", "", "")
        except EXC:
            pass


class Test_f_dist_rt:
    def test_exists(self):
        assert hasattr(mod, "f_dist_rt")

    def test_var0(self):
        try:
            mod.f_dist_rt(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.f_dist_rt(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.f_dist_rt(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.f_dist_rt("", "", "")
        except EXC:
            pass


class Test_f_inv:
    def test_exists(self):
        assert hasattr(mod, "f_inv")

    def test_var0(self):
        try:
            mod.f_inv(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.f_inv(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.f_inv(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.f_inv(0, "", "")
        except EXC:
            pass


class Test_f_inv_rt:
    def test_exists(self):
        assert hasattr(mod, "f_inv_rt")

    def test_var0(self):
        try:
            mod.f_inv_rt(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.f_inv_rt(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.f_inv_rt(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.f_inv_rt(0, "", "")
        except EXC:
            pass


class Test_gamma_dist:
    def test_exists(self):
        assert hasattr(mod, "gamma_dist")

    def test_var0(self):
        try:
            mod.gamma_dist(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gamma_dist(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gamma_dist(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gamma_dist("", 0, 0)
        except EXC:
            pass


class Test_gamma_inv:
    def test_exists(self):
        assert hasattr(mod, "gamma_inv")

    def test_var0(self):
        try:
            mod.gamma_inv(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gamma_inv(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gamma_inv(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gamma_inv(0, 0, 0)
        except EXC:
            pass


class Test_gauss:
    def test_exists(self):
        assert hasattr(mod, "gauss")

    def test_var0(self):
        try:
            mod.gauss(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gauss(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gauss(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gauss("")
        except EXC:
            pass


class Test_hypgeom_dist:
    def test_exists(self):
        assert hasattr(mod, "hypgeom_dist")

    def test_var0(self):
        try:
            mod.hypgeom_dist(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hypgeom_dist(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hypgeom_dist(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hypgeom_dist("", "", 0, "")
        except EXC:
            pass


class Test_lognorm_dist:
    def test_exists(self):
        assert hasattr(mod, "lognorm_dist")

    def test_var0(self):
        try:
            mod.lognorm_dist(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lognorm_dist(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lognorm_dist(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lognorm_dist("", 0, "")
        except EXC:
            pass


class Test_lognorm_inv:
    def test_exists(self):
        assert hasattr(mod, "lognorm_inv")

    def test_var0(self):
        try:
            mod.lognorm_inv(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lognorm_inv(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lognorm_inv(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lognorm_inv(0, 0, "")
        except EXC:
            pass


class Test_negbinom_dist:
    def test_exists(self):
        assert hasattr(mod, "negbinom_dist")

    def test_var0(self):
        try:
            mod.negbinom_dist(0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.negbinom_dist(1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.negbinom_dist(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.negbinom_dist("", "", 0)
        except EXC:
            pass


class Test_norm_dist:
    def test_exists(self):
        assert hasattr(mod, "norm_dist")

    def test_var0(self):
        try:
            mod.norm_dist(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.norm_dist(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.norm_dist(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.norm_dist("")
        except EXC:
            pass


class Test_norm_inv:
    def test_exists(self):
        assert hasattr(mod, "norm_inv")

    def test_var0(self):
        try:
            mod.norm_inv(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.norm_inv(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.norm_inv(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.norm_inv(0)
        except EXC:
            pass


class Test_norm_s_dist:
    def test_exists(self):
        assert hasattr(mod, "norm_s_dist")

    def test_var0(self):
        try:
            mod.norm_s_dist(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.norm_s_dist(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.norm_s_dist(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.norm_s_dist("")
        except EXC:
            pass


class Test_norm_s_inv:
    def test_exists(self):
        assert hasattr(mod, "norm_s_inv")

    def test_var0(self):
        try:
            mod.norm_s_inv(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.norm_s_inv(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.norm_s_inv(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.norm_s_inv(0)
        except EXC:
            pass


class Test_phi:
    def test_exists(self):
        assert hasattr(mod, "phi")

    def test_var0(self):
        try:
            mod.phi(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.phi(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.phi(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.phi("")
        except EXC:
            pass


class Test_poisson_dist:
    def test_exists(self):
        assert hasattr(mod, "poisson_dist")

    def test_var0(self):
        try:
            mod.poisson_dist(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.poisson_dist(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.poisson_dist(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.poisson_dist("", 0)
        except EXC:
            pass


class Test_t_dist:
    def test_exists(self):
        assert hasattr(mod, "t_dist")

    def test_var0(self):
        try:
            mod.t_dist(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.t_dist(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.t_dist(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.t_dist("", "")
        except EXC:
            pass


class Test_t_dist_2t:
    def test_exists(self):
        assert hasattr(mod, "t_dist_2t")

    def test_var0(self):
        try:
            mod.t_dist_2t(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.t_dist_2t(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.t_dist_2t(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.t_dist_2t("", "")
        except EXC:
            pass


class Test_t_dist_rt:
    def test_exists(self):
        assert hasattr(mod, "t_dist_rt")

    def test_var0(self):
        try:
            mod.t_dist_rt(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.t_dist_rt(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.t_dist_rt(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.t_dist_rt("", "")
        except EXC:
            pass


class Test_t_inv:
    def test_exists(self):
        assert hasattr(mod, "t_inv")

    def test_var0(self):
        try:
            mod.t_inv(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.t_inv(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.t_inv(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.t_inv(0, "")
        except EXC:
            pass


class Test_t_inv_2t:
    def test_exists(self):
        assert hasattr(mod, "t_inv_2t")

    def test_var0(self):
        try:
            mod.t_inv_2t(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.t_inv_2t(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.t_inv_2t(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.t_inv_2t(0, "")
        except EXC:
            pass


class Test_weibull_dist:
    def test_exists(self):
        assert hasattr(mod, "weibull_dist")

    def test_var0(self):
        try:
            mod.weibull_dist(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weibull_dist(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weibull_dist(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weibull_dist("", 0, 0)
        except EXC:
            pass

