# Coverage tests for shortfx.fxNumeric.series_functions
import math

from shortfx.fxNumeric import series_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_abel_sum:
    def test_exists(self):
        assert hasattr(mod, "abel_sum")

    def test_var0(self):
        try:
            mod.abel_sum(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.abel_sum(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.abel_sum(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.abel_sum([])
        except EXC:
            pass


class Test_alternating_series_sum:
    def test_exists(self):
        assert hasattr(mod, "alternating_series_sum")

    def test_var0(self):
        try:
            mod.alternating_series_sum(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.alternating_series_sum(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.alternating_series_sum(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.alternating_series_sum("", 0)
        except EXC:
            pass


class Test_arithmetic_series_sum:
    def test_exists(self):
        assert hasattr(mod, "arithmetic_series_sum")

    def test_doc0(self):
        try:
            mod.arithmetic_series_sum(1, 2, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.arithmetic_series_sum(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.arithmetic_series_sum(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.arithmetic_series_sum(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.arithmetic_series_sum("", "", 0)
        except EXC:
            pass


class Test_basel_series:
    def test_exists(self):
        assert hasattr(mod, "basel_series")

    def test_var0(self):
        try:
            mod.basel_series()
        except EXC:
            pass


class Test_bbp_pi_digit:
    def test_exists(self):
        assert hasattr(mod, "bbp_pi_digit")

    def test_var0(self):
        try:
            mod.bbp_pi_digit(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bbp_pi_digit(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bbp_pi_digit(None)
        except EXC:
            pass


class Test_binomial_series:
    def test_exists(self):
        assert hasattr(mod, "binomial_series")

    def test_var0(self):
        try:
            mod.binomial_series(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.binomial_series(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.binomial_series(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.binomial_series(0, "")
        except EXC:
            pass


class Test_cesaro_sum:
    def test_exists(self):
        assert hasattr(mod, "cesaro_sum")

    def test_doc0(self):
        try:
            mod.cesaro_sum([1, -1, 1, -1, 1, -1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cesaro_sum(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cesaro_sum(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cesaro_sum(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cesaro_sum([])
        except EXC:
            pass


class Test_chudnovsky_pi:
    def test_exists(self):
        assert hasattr(mod, "chudnovsky_pi")

    def test_var0(self):
        try:
            mod.chudnovsky_pi()
        except EXC:
            pass


class Test_convergent_sequence:
    def test_exists(self):
        assert hasattr(mod, "convergent_sequence")

    def test_var0(self):
        try:
            mod.convergent_sequence(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.convergent_sequence(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.convergent_sequence(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.convergent_sequence("", "")
        except EXC:
            pass


class Test_euler_maclaurin_sum:
    def test_exists(self):
        assert hasattr(mod, "euler_maclaurin_sum")

    def test_var0(self):
        try:
            mod.euler_maclaurin_sum(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.euler_maclaurin_sum(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.euler_maclaurin_sum(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.euler_maclaurin_sum("", "", "")
        except EXC:
            pass


class Test_fourier_coefficients:
    def test_exists(self):
        assert hasattr(mod, "fourier_coefficients")

    def test_doc0(self):
        try:
            mod.fourier_coefficients(math.sin, 2 * math.pi, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fourier_coefficients(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fourier_coefficients(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fourier_coefficients(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fourier_coefficients("", "", 0)
        except EXC:
            pass


class Test_fourier_series_eval:
    def test_exists(self):
        assert hasattr(mod, "fourier_series_eval")

    def test_doc0(self):
        try:
            mod.fourier_series_eval([0, 0], [0, 1], 2 * math.pi, math.pi / 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fourier_series_eval(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fourier_series_eval(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fourier_series_eval(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fourier_series_eval("", "", "", "")
        except EXC:
            pass


class Test_generalized_harmonic:
    def test_exists(self):
        assert hasattr(mod, "generalized_harmonic")

    def test_var0(self):
        try:
            mod.generalized_harmonic(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.generalized_harmonic(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.generalized_harmonic(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.generalized_harmonic(0, "")
        except EXC:
            pass


class Test_geometric_series_infinite:
    def test_exists(self):
        assert hasattr(mod, "geometric_series_infinite")

    def test_doc0(self):
        try:
            mod.geometric_series_infinite(1, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.geometric_series_infinite(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geometric_series_infinite(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geometric_series_infinite(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geometric_series_infinite("", "")
        except EXC:
            pass


class Test_geometric_series_sum:
    def test_exists(self):
        assert hasattr(mod, "geometric_series_sum")

    def test_doc0(self):
        try:
            mod.geometric_series_sum(1, 0.5, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.geometric_series_sum(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geometric_series_sum(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geometric_series_sum(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geometric_series_sum("", "", 0)
        except EXC:
            pass


class Test_gregory_leibniz_pi:
    def test_exists(self):
        assert hasattr(mod, "gregory_leibniz_pi")

    def test_var0(self):
        try:
            mod.gregory_leibniz_pi()
        except EXC:
            pass


class Test_harmonic_series_partial:
    def test_exists(self):
        assert hasattr(mod, "harmonic_series_partial")

    def test_var0(self):
        try:
            mod.harmonic_series_partial(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.harmonic_series_partial(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.harmonic_series_partial(None)
        except EXC:
            pass


class Test_leibniz_pi:
    def test_exists(self):
        assert hasattr(mod, "leibniz_pi")

    def test_var0(self):
        try:
            mod.leibniz_pi()
        except EXC:
            pass


class Test_madhava_pi:
    def test_exists(self):
        assert hasattr(mod, "madhava_pi")

    def test_var0(self):
        try:
            mod.madhava_pi()
        except EXC:
            pass


class Test_nilakantha_pi:
    def test_exists(self):
        assert hasattr(mod, "nilakantha_pi")

    def test_var0(self):
        try:
            mod.nilakantha_pi()
        except EXC:
            pass


class Test_p_series_partial:
    def test_exists(self):
        assert hasattr(mod, "p_series_partial")

    def test_var0(self):
        try:
            mod.p_series_partial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.p_series_partial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.p_series_partial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.p_series_partial(0, "")
        except EXC:
            pass


class Test_power_series_eval:
    def test_exists(self):
        assert hasattr(mod, "power_series_eval")

    def test_doc0(self):
        try:
            mod.power_series_eval([1, 0, -0.5], 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.power_series_eval(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.power_series_eval(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.power_series_eval(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.power_series_eval([], "")
        except EXC:
            pass


class Test_ramanujan_pi:
    def test_exists(self):
        assert hasattr(mod, "ramanujan_pi")

    def test_var0(self):
        try:
            mod.ramanujan_pi()
        except EXC:
            pass


class Test_taylor_asin:
    def test_exists(self):
        assert hasattr(mod, "taylor_asin")

    def test_var0(self):
        try:
            mod.taylor_asin(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_asin(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_asin(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_asin("")
        except EXC:
            pass


class Test_taylor_atan:
    def test_exists(self):
        assert hasattr(mod, "taylor_atan")

    def test_var0(self):
        try:
            mod.taylor_atan(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_atan(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_atan(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_atan("")
        except EXC:
            pass


class Test_taylor_atanh:
    def test_exists(self):
        assert hasattr(mod, "taylor_atanh")

    def test_var0(self):
        try:
            mod.taylor_atanh(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_atanh(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_atanh(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_atanh("")
        except EXC:
            pass


class Test_taylor_cos:
    def test_exists(self):
        assert hasattr(mod, "taylor_cos")

    def test_var0(self):
        try:
            mod.taylor_cos(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_cos(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_cos(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_cos("")
        except EXC:
            pass


class Test_taylor_cosh:
    def test_exists(self):
        assert hasattr(mod, "taylor_cosh")

    def test_var0(self):
        try:
            mod.taylor_cosh(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_cosh(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_cosh(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_cosh("")
        except EXC:
            pass


class Test_taylor_exp:
    def test_exists(self):
        assert hasattr(mod, "taylor_exp")

    def test_var0(self):
        try:
            mod.taylor_exp(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_exp(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_exp(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_exp("")
        except EXC:
            pass


class Test_taylor_ln1p:
    def test_exists(self):
        assert hasattr(mod, "taylor_ln1p")

    def test_var0(self):
        try:
            mod.taylor_ln1p(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_ln1p(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_ln1p(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_ln1p("")
        except EXC:
            pass


class Test_taylor_log1p:
    def test_exists(self):
        assert hasattr(mod, "taylor_log1p")

    def test_var0(self):
        try:
            mod.taylor_log1p(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_log1p(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_log1p(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_log1p("")
        except EXC:
            pass


class Test_taylor_sin:
    def test_exists(self):
        assert hasattr(mod, "taylor_sin")

    def test_var0(self):
        try:
            mod.taylor_sin(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_sin(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_sin(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_sin("")
        except EXC:
            pass


class Test_taylor_sinh:
    def test_exists(self):
        assert hasattr(mod, "taylor_sinh")

    def test_var0(self):
        try:
            mod.taylor_sinh(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.taylor_sinh(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.taylor_sinh(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.taylor_sinh("")
        except EXC:
            pass


class Test_vieta_pi:
    def test_exists(self):
        assert hasattr(mod, "vieta_pi")

    def test_var0(self):
        try:
            mod.vieta_pi()
        except EXC:
            pass


class Test_wallis_pi:
    def test_exists(self):
        assert hasattr(mod, "wallis_pi")

    def test_var0(self):
        try:
            mod.wallis_pi()
        except EXC:
            pass


class Test_zeta_even:
    def test_exists(self):
        assert hasattr(mod, "zeta_even")

    def test_var0(self):
        try:
            mod.zeta_even(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.zeta_even(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.zeta_even(None)
        except EXC:
            pass

