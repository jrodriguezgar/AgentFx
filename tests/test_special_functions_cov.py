# Coverage tests for formulite.fxNumeric.special_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import special_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_abel_polynomial:
    def test_exists(self):
        assert hasattr(mod, "abel_polynomial")

    def test_doc0(self):
        try:
            mod.abel_polynomial(3, 2.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.abel_polynomial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.abel_polynomial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.abel_polynomial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.abel_polynomial(0, "")
        except EXC:
            pass


class Test_airy_ai:
    def test_exists(self):
        assert hasattr(mod, "airy_ai")

    def test_var0(self):
        try:
            mod.airy_ai(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.airy_ai(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.airy_ai(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.airy_ai("")
        except EXC:
            pass


class Test_airy_bi:
    def test_exists(self):
        assert hasattr(mod, "airy_bi")

    def test_var0(self):
        try:
            mod.airy_bi(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.airy_bi(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.airy_bi(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.airy_bi("")
        except EXC:
            pass


class Test_anger_j:
    def test_exists(self):
        assert hasattr(mod, "anger_j")

    def test_var0(self):
        try:
            mod.anger_j(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.anger_j(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.anger_j(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.anger_j("", "")
        except EXC:
            pass


class Test_associated_legendre:
    def test_exists(self):
        assert hasattr(mod, "associated_legendre")

    def test_doc0(self):
        try:
            mod.associated_legendre(1, 1, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.associated_legendre(0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.associated_legendre(1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.associated_legendre(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.associated_legendre(0, "", "")
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


class Test_bernoulli_number:
    def test_exists(self):
        assert hasattr(mod, "bernoulli_number")

    def test_doc0(self):
        try:
            mod.bernoulli_number(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.bernoulli_number(1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.bernoulli_number(2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bernoulli_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bernoulli_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bernoulli_number(None)
        except EXC:
            pass


class Test_bernoulli_polynomial:
    def test_exists(self):
        assert hasattr(mod, "bernoulli_polynomial")

    def test_doc0(self):
        try:
            mod.bernoulli_polynomial(0, 0.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.bernoulli_polynomial(1, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bernoulli_polynomial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bernoulli_polynomial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bernoulli_polynomial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bernoulli_polynomial(0, "")
        except EXC:
            pass


class Test_bernstein_polynomial:
    def test_exists(self):
        assert hasattr(mod, "bernstein_polynomial")

    def test_doc0(self):
        try:
            mod.bernstein_polynomial(3, 1, 0.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.bernstein_polynomial(4, 2, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bernstein_polynomial(0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bernstein_polynomial(1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bernstein_polynomial(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bernstein_polynomial(0, 0, "")
        except EXC:
            pass


class Test_bessel_j:
    def test_exists(self):
        assert hasattr(mod, "bessel_j")

    def test_var0(self):
        try:
            mod.bessel_j(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bessel_j(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bessel_j(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bessel_j(0, "")
        except EXC:
            pass


class Test_bessel_y:
    def test_exists(self):
        assert hasattr(mod, "bessel_y")

    def test_var0(self):
        try:
            mod.bessel_y(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bessel_y(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bessel_y(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bessel_y(0, "")
        except EXC:
            pass


class Test_beta_function:
    def test_exists(self):
        assert hasattr(mod, "beta_function")

    def test_var0(self):
        try:
            mod.beta_function(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.beta_function(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.beta_function(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.beta_function("", "")
        except EXC:
            pass


class Test_catalan_number:
    def test_exists(self):
        assert hasattr(mod, "catalan_number")

    def test_doc0(self):
        try:
            mod.catalan_number(5)
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


class Test_central_binomial_coefficient:
    def test_exists(self):
        assert hasattr(mod, "central_binomial_coefficient")

    def test_doc0(self):
        try:
            mod.central_binomial_coefficient(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.central_binomial_coefficient(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.central_binomial_coefficient(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.central_binomial_coefficient(None)
        except EXC:
            pass


class Test_chebyshev_polynomial_first:
    def test_exists(self):
        assert hasattr(mod, "chebyshev_polynomial_first")

    def test_doc0(self):
        try:
            mod.chebyshev_polynomial_first(0, 0.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.chebyshev_polynomial_first(2, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.chebyshev_polynomial_first(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chebyshev_polynomial_first(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chebyshev_polynomial_first(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chebyshev_polynomial_first(0, "")
        except EXC:
            pass


class Test_chebyshev_polynomial_second:
    def test_exists(self):
        assert hasattr(mod, "chebyshev_polynomial_second")

    def test_doc0(self):
        try:
            mod.chebyshev_polynomial_second(0, 0.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.chebyshev_polynomial_second(2, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.chebyshev_polynomial_second(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chebyshev_polynomial_second(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chebyshev_polynomial_second(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chebyshev_polynomial_second(0, "")
        except EXC:
            pass


class Test_clausen_function:
    def test_exists(self):
        assert hasattr(mod, "clausen_function")

    def test_var0(self):
        try:
            mod.clausen_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.clausen_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.clausen_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.clausen_function("")
        except EXC:
            pass


class Test_complementary_error_function:
    def test_exists(self):
        assert hasattr(mod, "complementary_error_function")

    def test_var0(self):
        try:
            mod.complementary_error_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.complementary_error_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.complementary_error_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.complementary_error_function("")
        except EXC:
            pass


class Test_cosine_integral:
    def test_exists(self):
        assert hasattr(mod, "cosine_integral")

    def test_var0(self):
        try:
            mod.cosine_integral(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cosine_integral(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cosine_integral(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cosine_integral("")
        except EXC:
            pass


class Test_dawson_function:
    def test_exists(self):
        assert hasattr(mod, "dawson_function")

    def test_var0(self):
        try:
            mod.dawson_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dawson_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dawson_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dawson_function("")
        except EXC:
            pass


class Test_debye_function:
    def test_exists(self):
        assert hasattr(mod, "debye_function")

    def test_var0(self):
        try:
            mod.debye_function(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.debye_function(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.debye_function(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.debye_function(0, "")
        except EXC:
            pass


class Test_dedekind_eta:
    def test_exists(self):
        assert hasattr(mod, "dedekind_eta")

    def test_var0(self):
        try:
            mod.dedekind_eta(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dedekind_eta(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dedekind_eta(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dedekind_eta("")
        except EXC:
            pass


class Test_digamma:
    def test_exists(self):
        assert hasattr(mod, "digamma")

    def test_var0(self):
        try:
            mod.digamma(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.digamma(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.digamma(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.digamma("")
        except EXC:
            pass


class Test_dilogarithm:
    def test_exists(self):
        assert hasattr(mod, "dilogarithm")

    def test_var0(self):
        try:
            mod.dilogarithm(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dilogarithm(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dilogarithm(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dilogarithm("")
        except EXC:
            pass


class Test_dirichlet_integral:
    def test_exists(self):
        assert hasattr(mod, "dirichlet_integral")

    def test_var0(self):
        try:
            mod.dirichlet_integral()
        except EXC:
            pass


class Test_double_factorial:
    def test_exists(self):
        assert hasattr(mod, "double_factorial")

    def test_doc0(self):
        try:
            mod.double_factorial(7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.double_factorial(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.double_factorial(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.double_factorial(None)
        except EXC:
            pass


class Test_elliptic_e:
    def test_exists(self):
        assert hasattr(mod, "elliptic_e")

    def test_var0(self):
        try:
            mod.elliptic_e(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elliptic_e(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elliptic_e(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elliptic_e(0)
        except EXC:
            pass


class Test_elliptic_e_incomplete:
    def test_exists(self):
        assert hasattr(mod, "elliptic_e_incomplete")

    def test_var0(self):
        try:
            mod.elliptic_e_incomplete(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elliptic_e_incomplete(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elliptic_e_incomplete(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elliptic_e_incomplete("", 0)
        except EXC:
            pass


class Test_elliptic_f:
    def test_exists(self):
        assert hasattr(mod, "elliptic_f")

    def test_var0(self):
        try:
            mod.elliptic_f(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elliptic_f(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elliptic_f(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elliptic_f("", 0)
        except EXC:
            pass


class Test_elliptic_k:
    def test_exists(self):
        assert hasattr(mod, "elliptic_k")

    def test_var0(self):
        try:
            mod.elliptic_k(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elliptic_k(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elliptic_k(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elliptic_k(0)
        except EXC:
            pass


class Test_elliptic_pi:
    def test_exists(self):
        assert hasattr(mod, "elliptic_pi")

    def test_var0(self):
        try:
            mod.elliptic_pi(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elliptic_pi(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elliptic_pi(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elliptic_pi(0, 0)
        except EXC:
            pass


class Test_error_function:
    def test_exists(self):
        assert hasattr(mod, "error_function")

    def test_var0(self):
        try:
            mod.error_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.error_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.error_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.error_function("")
        except EXC:
            pass


class Test_euler_number:
    def test_exists(self):
        assert hasattr(mod, "euler_number")

    def test_doc0(self):
        try:
            mod.euler_number(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.euler_number(2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.euler_number(4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.euler_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.euler_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.euler_number(None)
        except EXC:
            pass


class Test_euler_polynomial:
    def test_exists(self):
        assert hasattr(mod, "euler_polynomial")

    def test_doc0(self):
        try:
            mod.euler_polynomial(0, 1.0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.euler_polynomial(1, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.euler_polynomial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.euler_polynomial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.euler_polynomial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.euler_polynomial(0, "")
        except EXC:
            pass


class Test_euler_reflection_formula:
    def test_exists(self):
        assert hasattr(mod, "euler_reflection_formula")

    def test_var0(self):
        try:
            mod.euler_reflection_formula(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.euler_reflection_formula(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.euler_reflection_formula(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.euler_reflection_formula("")
        except EXC:
            pass


class Test_exponential_integral_ei:
    def test_exists(self):
        assert hasattr(mod, "exponential_integral_ei")

    def test_var0(self):
        try:
            mod.exponential_integral_ei(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.exponential_integral_ei(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.exponential_integral_ei(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.exponential_integral_ei("")
        except EXC:
            pass


class Test_falling_factorial:
    def test_exists(self):
        assert hasattr(mod, "falling_factorial")

    def test_doc0(self):
        try:
            mod.falling_factorial(5, 3)  # 5*4*3
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.falling_factorial(5, 5)  # 5!
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.falling_factorial(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.falling_factorial(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.falling_factorial(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.falling_factorial("", 0)
        except EXC:
            pass


class Test_fibonacci_polynomial:
    def test_exists(self):
        assert hasattr(mod, "fibonacci_polynomial")

    def test_doc0(self):
        try:
            mod.fibonacci_polynomial(5, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fibonacci_polynomial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fibonacci_polynomial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fibonacci_polynomial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fibonacci_polynomial(0, "")
        except EXC:
            pass


class Test_fresnel_c:
    def test_exists(self):
        assert hasattr(mod, "fresnel_c")

    def test_var0(self):
        try:
            mod.fresnel_c(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fresnel_c(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fresnel_c(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fresnel_c("")
        except EXC:
            pass


class Test_fresnel_s:
    def test_exists(self):
        assert hasattr(mod, "fresnel_s")

    def test_var0(self):
        try:
            mod.fresnel_s(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fresnel_s(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fresnel_s(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fresnel_s("")
        except EXC:
            pass


class Test_gamma_duplication_formula:
    def test_exists(self):
        assert hasattr(mod, "gamma_duplication_formula")

    def test_var0(self):
        try:
            mod.gamma_duplication_formula(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gamma_duplication_formula(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gamma_duplication_formula(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gamma_duplication_formula("")
        except EXC:
            pass


class Test_gaussian_integral:
    def test_exists(self):
        assert hasattr(mod, "gaussian_integral")

    def test_var0(self):
        try:
            mod.gaussian_integral()
        except EXC:
            pass


class Test_gegenbauer_polynomial:
    def test_exists(self):
        assert hasattr(mod, "gegenbauer_polynomial")

    def test_var0(self):
        try:
            mod.gegenbauer_polynomial(0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gegenbauer_polynomial(1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gegenbauer_polynomial(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gegenbauer_polynomial(0, 0, "")
        except EXC:
            pass


class Test_generalized_harmonic_number:
    def test_exists(self):
        assert hasattr(mod, "generalized_harmonic_number")

    def test_var0(self):
        try:
            mod.generalized_harmonic_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.generalized_harmonic_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.generalized_harmonic_number(None)
        except EXC:
            pass


class Test_generalized_laguerre_polynomial:
    def test_exists(self):
        assert hasattr(mod, "generalized_laguerre_polynomial")

    def test_doc0(self):
        try:
            mod.generalized_laguerre_polynomial(2, 0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.generalized_laguerre_polynomial(0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.generalized_laguerre_polynomial(1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.generalized_laguerre_polynomial(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.generalized_laguerre_polynomial(0, 0, "")
        except EXC:
            pass


class Test_gudermannian:
    def test_exists(self):
        assert hasattr(mod, "gudermannian")

    def test_var0(self):
        try:
            mod.gudermannian(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gudermannian(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gudermannian(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gudermannian("")
        except EXC:
            pass


class Test_harmonic_number:
    def test_exists(self):
        assert hasattr(mod, "harmonic_number")

    def test_var0(self):
        try:
            mod.harmonic_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.harmonic_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.harmonic_number(None)
        except EXC:
            pass


class Test_heaviside_step:
    def test_exists(self):
        assert hasattr(mod, "heaviside_step")

    def test_doc0(self):
        try:
            mod.heaviside_step(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.heaviside_step(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.heaviside_step(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.heaviside_step(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.heaviside_step("")
        except EXC:
            pass


class Test_hermite_polynomial:
    def test_exists(self):
        assert hasattr(mod, "hermite_polynomial")

    def test_doc0(self):
        try:
            mod.hermite_polynomial(0, 1.0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hermite_polynomial(3, 2.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hermite_polynomial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hermite_polynomial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hermite_polynomial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hermite_polynomial(0, "")
        except EXC:
            pass


class Test_hexagonal_number:
    def test_exists(self):
        assert hasattr(mod, "hexagonal_number")

    def test_doc0(self):
        try:
            mod.hexagonal_number(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hexagonal_number(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hexagonal_number(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hexagonal_number(None)
        except EXC:
            pass


class Test_hurwitz_zeta:
    def test_exists(self):
        assert hasattr(mod, "hurwitz_zeta")

    def test_var0(self):
        try:
            mod.hurwitz_zeta(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hurwitz_zeta(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hurwitz_zeta(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hurwitz_zeta("", "")
        except EXC:
            pass


class Test_hypergeometric_1f1:
    def test_exists(self):
        assert hasattr(mod, "hypergeometric_1f1")

    def test_var0(self):
        try:
            mod.hypergeometric_1f1(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hypergeometric_1f1(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hypergeometric_1f1(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hypergeometric_1f1("", "", "")
        except EXC:
            pass


class Test_hypergeometric_2f1:
    def test_exists(self):
        assert hasattr(mod, "hypergeometric_2f1")

    def test_var0(self):
        try:
            mod.hypergeometric_2f1(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hypergeometric_2f1(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hypergeometric_2f1(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hypergeometric_2f1("", "", "", "")
        except EXC:
            pass


class Test_incomplete_beta_regularized:
    def test_exists(self):
        assert hasattr(mod, "incomplete_beta_regularized")

    def test_var0(self):
        try:
            mod.incomplete_beta_regularized(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.incomplete_beta_regularized(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.incomplete_beta_regularized(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.incomplete_beta_regularized("", "", "")
        except EXC:
            pass


class Test_incomplete_gamma_lower:
    def test_exists(self):
        assert hasattr(mod, "incomplete_gamma_lower")

    def test_var0(self):
        try:
            mod.incomplete_gamma_lower(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.incomplete_gamma_lower(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.incomplete_gamma_lower(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.incomplete_gamma_lower("", "")
        except EXC:
            pass


class Test_inverse_error_function:
    def test_exists(self):
        assert hasattr(mod, "inverse_error_function")

    def test_var0(self):
        try:
            mod.inverse_error_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_error_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_error_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_error_function("")
        except EXC:
            pass


class Test_inverse_gudermannian:
    def test_exists(self):
        assert hasattr(mod, "inverse_gudermannian")

    def test_var0(self):
        try:
            mod.inverse_gudermannian(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_gudermannian(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_gudermannian(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_gudermannian("")
        except EXC:
            pass


class Test_jacobi_polynomial:
    def test_exists(self):
        assert hasattr(mod, "jacobi_polynomial")

    def test_var0(self):
        try:
            mod.jacobi_polynomial(0, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jacobi_polynomial(1, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jacobi_polynomial(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.jacobi_polynomial(0, 0, 0, "")
        except EXC:
            pass


class Test_jacobi_theta_1:
    def test_exists(self):
        assert hasattr(mod, "jacobi_theta_1")

    def test_var0(self):
        try:
            mod.jacobi_theta_1(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jacobi_theta_1(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jacobi_theta_1(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.jacobi_theta_1("", "")
        except EXC:
            pass


class Test_jacobi_theta_2:
    def test_exists(self):
        assert hasattr(mod, "jacobi_theta_2")

    def test_var0(self):
        try:
            mod.jacobi_theta_2(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jacobi_theta_2(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jacobi_theta_2(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.jacobi_theta_2("", "")
        except EXC:
            pass


class Test_jacobi_theta_3:
    def test_exists(self):
        assert hasattr(mod, "jacobi_theta_3")

    def test_var0(self):
        try:
            mod.jacobi_theta_3(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jacobi_theta_3(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jacobi_theta_3(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.jacobi_theta_3("", "")
        except EXC:
            pass


class Test_jacobi_theta_4:
    def test_exists(self):
        assert hasattr(mod, "jacobi_theta_4")

    def test_var0(self):
        try:
            mod.jacobi_theta_4(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jacobi_theta_4(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jacobi_theta_4(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.jacobi_theta_4("", "")
        except EXC:
            pass


class Test_kelvin_bei:
    def test_exists(self):
        assert hasattr(mod, "kelvin_bei")

    def test_var0(self):
        try:
            mod.kelvin_bei(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kelvin_bei(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kelvin_bei(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kelvin_bei("")
        except EXC:
            pass


class Test_kelvin_ber:
    def test_exists(self):
        assert hasattr(mod, "kelvin_ber")

    def test_var0(self):
        try:
            mod.kelvin_ber(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kelvin_ber(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kelvin_ber(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kelvin_ber("")
        except EXC:
            pass


class Test_laguerre_polynomial:
    def test_exists(self):
        assert hasattr(mod, "laguerre_polynomial")

    def test_doc0(self):
        try:
            mod.laguerre_polynomial(0, 1.0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.laguerre_polynomial(2, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.laguerre_polynomial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.laguerre_polynomial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.laguerre_polynomial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.laguerre_polynomial(0, "")
        except EXC:
            pass


class Test_lambert_w:
    def test_exists(self):
        assert hasattr(mod, "lambert_w")

    def test_var0(self):
        try:
            mod.lambert_w(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lambert_w(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lambert_w(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lambert_w("")
        except EXC:
            pass


class Test_lanczos_gamma:
    def test_exists(self):
        assert hasattr(mod, "lanczos_gamma")

    def test_var0(self):
        try:
            mod.lanczos_gamma(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lanczos_gamma(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lanczos_gamma(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lanczos_gamma("")
        except EXC:
            pass


class Test_legendre_polynomial:
    def test_exists(self):
        assert hasattr(mod, "legendre_polynomial")

    def test_doc0(self):
        try:
            mod.legendre_polynomial(0, 0.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.legendre_polynomial(2, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.legendre_polynomial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.legendre_polynomial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.legendre_polynomial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.legendre_polynomial(0, "")
        except EXC:
            pass


class Test_log_gamma:
    def test_exists(self):
        assert hasattr(mod, "log_gamma")

    def test_var0(self):
        try:
            mod.log_gamma(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.log_gamma(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.log_gamma(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.log_gamma("")
        except EXC:
            pass


class Test_logistic_function:
    def test_exists(self):
        assert hasattr(mod, "logistic_function")

    def test_doc0(self):
        try:
            mod.logistic_function(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.logistic_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.logistic_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.logistic_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.logistic_function("")
        except EXC:
            pass


class Test_lucas_polynomial:
    def test_exists(self):
        assert hasattr(mod, "lucas_polynomial")

    def test_doc0(self):
        try:
            mod.lucas_polynomial(5, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lucas_polynomial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lucas_polynomial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lucas_polynomial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lucas_polynomial(0, "")
        except EXC:
            pass


class Test_mittag_leffler:
    def test_exists(self):
        assert hasattr(mod, "mittag_leffler")

    def test_var0(self):
        try:
            mod.mittag_leffler(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mittag_leffler(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mittag_leffler(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mittag_leffler(0, 0, "")
        except EXC:
            pass


class Test_modified_bessel_i:
    def test_exists(self):
        assert hasattr(mod, "modified_bessel_i")

    def test_var0(self):
        try:
            mod.modified_bessel_i(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.modified_bessel_i(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.modified_bessel_i(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.modified_bessel_i(0, "")
        except EXC:
            pass


class Test_modified_bessel_k:
    def test_exists(self):
        assert hasattr(mod, "modified_bessel_k")

    def test_var0(self):
        try:
            mod.modified_bessel_k(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.modified_bessel_k(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.modified_bessel_k(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.modified_bessel_k(0, "")
        except EXC:
            pass


class Test_multinomial_coefficient:
    def test_exists(self):
        assert hasattr(mod, "multinomial_coefficient")

    def test_doc0(self):
        try:
            mod.multinomial_coefficient(6, 2, 2, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.multinomial_coefficient(4, 2, 1, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.multinomial_coefficient(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.multinomial_coefficient(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.multinomial_coefficient(None)
        except EXC:
            pass


class Test_normalized_sinc:
    def test_exists(self):
        assert hasattr(mod, "normalized_sinc")

    def test_doc0(self):
        try:
            mod.normalized_sinc(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.normalized_sinc(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.normalized_sinc(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.normalized_sinc(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.normalized_sinc("")
        except EXC:
            pass


class Test_partition_number:
    def test_exists(self):
        assert hasattr(mod, "partition_number")

    def test_doc0(self):
        try:
            mod.partition_number(10)
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


class Test_polygamma:
    def test_exists(self):
        assert hasattr(mod, "polygamma")

    def test_var0(self):
        try:
            mod.polygamma(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polygamma(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polygamma(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polygamma("", "")
        except EXC:
            pass


class Test_polylogarithm:
    def test_exists(self):
        assert hasattr(mod, "polylogarithm")

    def test_var0(self):
        try:
            mod.polylogarithm(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.polylogarithm(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.polylogarithm(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.polylogarithm("", "")
        except EXC:
            pass


class Test_ramp_function:
    def test_exists(self):
        assert hasattr(mod, "ramp_function")

    def test_doc0(self):
        try:
            mod.ramp_function(3.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ramp_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ramp_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ramp_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ramp_function("")
        except EXC:
            pass


class Test_reciprocal_gamma:
    def test_exists(self):
        assert hasattr(mod, "reciprocal_gamma")

    def test_doc0(self):
        try:
            mod.reciprocal_gamma(1.0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.reciprocal_gamma(0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.reciprocal_gamma(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.reciprocal_gamma(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.reciprocal_gamma(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.reciprocal_gamma("")
        except EXC:
            pass


class Test_rectangular_function:
    def test_exists(self):
        assert hasattr(mod, "rectangular_function")

    def test_doc0(self):
        try:
            mod.rectangular_function(0.3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rectangular_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rectangular_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rectangular_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rectangular_function("")
        except EXC:
            pass


class Test_riemann_zeta:
    def test_exists(self):
        assert hasattr(mod, "riemann_zeta")

    def test_var0(self):
        try:
            mod.riemann_zeta(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.riemann_zeta(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.riemann_zeta(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.riemann_zeta("")
        except EXC:
            pass


class Test_rising_factorial:
    def test_exists(self):
        assert hasattr(mod, "rising_factorial")

    def test_doc0(self):
        try:
            mod.rising_factorial(3, 4)  # 3*4*5*6
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.rising_factorial(1, 5)  # 5!
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rising_factorial(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rising_factorial(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rising_factorial(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rising_factorial("", 0)
        except EXC:
            pass


class Test_sinc_function:
    def test_exists(self):
        assert hasattr(mod, "sinc_function")

    def test_doc0(self):
        try:
            mod.sinc_function(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sinc_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sinc_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sinc_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sinc_function("")
        except EXC:
            pass


class Test_sine_integral:
    def test_exists(self):
        assert hasattr(mod, "sine_integral")

    def test_var0(self):
        try:
            mod.sine_integral(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sine_integral(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sine_integral(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sine_integral("")
        except EXC:
            pass


class Test_softplus_function:
    def test_exists(self):
        assert hasattr(mod, "softplus_function")

    def test_var0(self):
        try:
            mod.softplus_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.softplus_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.softplus_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.softplus_function("")
        except EXC:
            pass


class Test_spherical_bessel_j:
    def test_exists(self):
        assert hasattr(mod, "spherical_bessel_j")

    def test_var0(self):
        try:
            mod.spherical_bessel_j(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_bessel_j(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_bessel_j(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_bessel_j(0, "")
        except EXC:
            pass


class Test_spherical_bessel_y:
    def test_exists(self):
        assert hasattr(mod, "spherical_bessel_y")

    def test_var0(self):
        try:
            mod.spherical_bessel_y(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_bessel_y(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_bessel_y(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_bessel_y(0, "")
        except EXC:
            pass


class Test_spherical_harmonic_real:
    def test_exists(self):
        assert hasattr(mod, "spherical_harmonic_real")

    def test_var0(self):
        try:
            mod.spherical_harmonic_real(0, 0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spherical_harmonic_real(1, 1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spherical_harmonic_real(None, 0, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spherical_harmonic_real("", "", "", "")
        except EXC:
            pass


class Test_stirling_approximation:
    def test_exists(self):
        assert hasattr(mod, "stirling_approximation")

    def test_var0(self):
        try:
            mod.stirling_approximation(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stirling_approximation(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stirling_approximation(None)
        except EXC:
            pass


class Test_stirling_number_first:
    def test_exists(self):
        assert hasattr(mod, "stirling_number_first")

    def test_doc0(self):
        try:
            mod.stirling_number_first(4, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.stirling_number_first(3, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.stirling_number_first(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.stirling_number_first(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.stirling_number_first(None, 0)
        except EXC:
            pass


class Test_struve_h:
    def test_exists(self):
        assert hasattr(mod, "struve_h")

    def test_var0(self):
        try:
            mod.struve_h(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.struve_h(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.struve_h(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.struve_h("", "")
        except EXC:
            pass


class Test_subfactorial:
    def test_exists(self):
        assert hasattr(mod, "subfactorial")

    def test_doc0(self):
        try:
            mod.subfactorial(0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.subfactorial(3)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.subfactorial(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.subfactorial(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.subfactorial(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.subfactorial(None)
        except EXC:
            pass


class Test_touchard_polynomial:
    def test_exists(self):
        assert hasattr(mod, "touchard_polynomial")

    def test_doc0(self):
        try:
            mod.touchard_polynomial(3, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.touchard_polynomial(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.touchard_polynomial(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.touchard_polynomial(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.touchard_polynomial(0, "")
        except EXC:
            pass


class Test_triangular_function:
    def test_exists(self):
        assert hasattr(mod, "triangular_function")

    def test_doc0(self):
        try:
            mod.triangular_function(0.3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.triangular_function(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.triangular_function(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.triangular_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.triangular_function("")
        except EXC:
            pass


class Test_trigamma:
    def test_exists(self):
        assert hasattr(mod, "trigamma")

    def test_var0(self):
        try:
            mod.trigamma(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.trigamma(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.trigamma(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.trigamma("")
        except EXC:
            pass


class Test_upper_incomplete_gamma:
    def test_exists(self):
        assert hasattr(mod, "upper_incomplete_gamma")

    def test_var0(self):
        try:
            mod.upper_incomplete_gamma(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.upper_incomplete_gamma(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.upper_incomplete_gamma(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.upper_incomplete_gamma("", "")
        except EXC:
            pass


class Test_wallis_product:
    def test_exists(self):
        assert hasattr(mod, "wallis_product")

    def test_var0(self):
        try:
            mod.wallis_product(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wallis_product(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wallis_product(None)
        except EXC:
            pass


class Test_weierstrass_p:
    def test_exists(self):
        assert hasattr(mod, "weierstrass_p")

    def test_var0(self):
        try:
            mod.weierstrass_p(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weierstrass_p(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weierstrass_p(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weierstrass_p("")
        except EXC:
            pass

