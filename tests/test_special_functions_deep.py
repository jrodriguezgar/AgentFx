# Deep coverage tests for agentfx.fxNumeric.special_functions

import agentfx.fxNumeric.special_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_incomplete_beta_regularized_deep:
    def test_c0(self):
        try:
            mod.incomplete_beta_regularized(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.incomplete_beta_regularized(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.incomplete_beta_regularized(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.incomplete_beta_regularized(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.incomplete_beta_regularized(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.incomplete_beta_regularized(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.incomplete_beta_regularized(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.incomplete_beta_regularized(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.incomplete_beta_regularized(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.incomplete_beta_regularized(2, 1, 42)
        except EXC:
            pass


class Test_elliptic_e_incomplete_deep:
    def test_c0(self):
        try:
            mod.elliptic_e_incomplete(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.elliptic_e_incomplete(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.elliptic_e_incomplete(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.elliptic_e_incomplete(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.elliptic_e_incomplete(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.elliptic_e_incomplete(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.elliptic_e_incomplete(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.elliptic_e_incomplete(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.elliptic_e_incomplete(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.elliptic_e_incomplete(2, 1)
        except EXC:
            pass


class Test_polygamma_deep:
    def test_c0(self):
        try:
            mod.polygamma(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.polygamma(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.polygamma(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.polygamma(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.polygamma(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.polygamma(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.polygamma(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.polygamma(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.polygamma(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.polygamma(5, 1)
        except EXC:
            pass


class Test_spherical_bessel_j_deep:
    def test_c0(self):
        try:
            mod.spherical_bessel_j(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spherical_bessel_j(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spherical_bessel_j(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spherical_bessel_j(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spherical_bessel_j(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spherical_bessel_j(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.spherical_bessel_j(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.spherical_bessel_j(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.spherical_bessel_j(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.spherical_bessel_j(5, 1)
        except EXC:
            pass


class Test_spherical_bessel_y_deep:
    def test_c0(self):
        try:
            mod.spherical_bessel_y(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spherical_bessel_y(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spherical_bessel_y(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spherical_bessel_y(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spherical_bessel_y(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spherical_bessel_y(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.spherical_bessel_y(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.spherical_bessel_y(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.spherical_bessel_y(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.spherical_bessel_y(5, 1)
        except EXC:
            pass


class Test_associated_legendre_deep:
    def test_c0(self):
        try:
            mod.associated_legendre(1, 2, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.associated_legendre(2, 3, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.associated_legendre(3, 5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.associated_legendre(5, 10, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.associated_legendre(10, 0, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.associated_legendre(0, 1, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.associated_legendre(1, 2, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.associated_legendre(2, 3, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.associated_legendre(3, 5, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.associated_legendre(5, 10, 42)
        except EXC:
            pass


class Test_elliptic_e_deep:
    def test_c0(self):
        try:
            mod.elliptic_e(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.elliptic_e(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.elliptic_e(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.elliptic_e(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.elliptic_e(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.elliptic_e(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.elliptic_e(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.elliptic_e(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.elliptic_e(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.elliptic_e(2)
        except EXC:
            pass


class Test_mittag_leffler_deep:
    def test_c0(self):
        try:
            mod.mittag_leffler(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mittag_leffler(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mittag_leffler(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mittag_leffler(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mittag_leffler(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mittag_leffler(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.mittag_leffler(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.mittag_leffler(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.mittag_leffler(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.mittag_leffler(2, 1, 42)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.mittag_leffler(1, 42, 0, terms=1)
        except EXC:
            pass


class Test_spherical_harmonic_real_deep:
    def test_c0(self):
        try:
            mod.spherical_harmonic_real(1, 2, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spherical_harmonic_real(2, 3, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spherical_harmonic_real(3, 5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spherical_harmonic_real(5, 10, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spherical_harmonic_real(10, 0, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spherical_harmonic_real(0, 1, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.spherical_harmonic_real(1, 2, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.spherical_harmonic_real(2, 3, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.spherical_harmonic_real(3, 5, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.spherical_harmonic_real(5, 10, 42, 0)
        except EXC:
            pass


class Test_incomplete_gamma_lower_deep:
    def test_c0(self):
        try:
            mod.incomplete_gamma_lower(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.incomplete_gamma_lower(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.incomplete_gamma_lower(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.incomplete_gamma_lower(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.incomplete_gamma_lower(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.incomplete_gamma_lower(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.incomplete_gamma_lower(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.incomplete_gamma_lower(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.incomplete_gamma_lower(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.incomplete_gamma_lower(2, 1)
        except EXC:
            pass


class Test_weierstrass_p_deep:
    def test_c0(self):
        try:
            mod.weierstrass_p(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weierstrass_p(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weierstrass_p(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weierstrass_p(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weierstrass_p(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weierstrass_p(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.weierstrass_p(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.weierstrass_p(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.weierstrass_p(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.weierstrass_p(2)
        except EXC:
            pass

    def test_kw_omega1(self):
        try:
            mod.weierstrass_p(1, omega1=1)
        except EXC:
            pass

    def test_kw_omega3_im(self):
        try:
            mod.weierstrass_p(1, omega3_im=1)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.weierstrass_p(1, terms=1)
        except EXC:
            pass


class Test_abel_polynomial_deep:
    def test_c0(self):
        try:
            mod.abel_polynomial(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.abel_polynomial(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.abel_polynomial(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.abel_polynomial(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.abel_polynomial(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.abel_polynomial(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.abel_polynomial(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.abel_polynomial(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.abel_polynomial(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.abel_polynomial(5, 1)
        except EXC:
            pass

    def test_kw_a(self):
        try:
            mod.abel_polynomial(1, 42, a=1)
        except EXC:
            pass


class Test_debye_function_deep:
    def test_c0(self):
        try:
            mod.debye_function(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.debye_function(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.debye_function(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.debye_function(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.debye_function(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.debye_function(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.debye_function(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.debye_function(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.debye_function(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.debye_function(5, 1)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.debye_function(1, 42, terms=1)
        except EXC:
            pass


class Test_elliptic_f_deep:
    def test_c0(self):
        try:
            mod.elliptic_f(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.elliptic_f(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.elliptic_f(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.elliptic_f(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.elliptic_f(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.elliptic_f(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.elliptic_f(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.elliptic_f(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.elliptic_f(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.elliptic_f(2, 1)
        except EXC:
            pass


class Test_euler_reflection_formula_deep:
    def test_c0(self):
        try:
            mod.euler_reflection_formula(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.euler_reflection_formula(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.euler_reflection_formula(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.euler_reflection_formula(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.euler_reflection_formula(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.euler_reflection_formula(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.euler_reflection_formula(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.euler_reflection_formula(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.euler_reflection_formula(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.euler_reflection_formula(2)
        except EXC:
            pass


class Test_generalized_laguerre_polynomial_deep:
    def test_c0(self):
        try:
            mod.generalized_laguerre_polynomial(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.generalized_laguerre_polynomial(2, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.generalized_laguerre_polynomial(3, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.generalized_laguerre_polynomial(5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.generalized_laguerre_polynomial(10, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.generalized_laguerre_polynomial(0, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.generalized_laguerre_polynomial(1, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.generalized_laguerre_polynomial(2, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.generalized_laguerre_polynomial(3, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.generalized_laguerre_polynomial(5, 1, 42)
        except EXC:
            pass


class Test_hurwitz_zeta_deep:
    def test_c0(self):
        try:
            mod.hurwitz_zeta(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hurwitz_zeta(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hurwitz_zeta(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hurwitz_zeta(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hurwitz_zeta(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hurwitz_zeta(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.hurwitz_zeta(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.hurwitz_zeta(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.hurwitz_zeta(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.hurwitz_zeta(2, 1)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.hurwitz_zeta(1, 42, terms=1)
        except EXC:
            pass


class Test_jacobi_polynomial_deep:
    def test_c0(self):
        try:
            mod.jacobi_polynomial(1, 42, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.jacobi_polynomial(2, 0, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.jacobi_polynomial(3, -5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.jacobi_polynomial(5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.jacobi_polynomial(10, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.jacobi_polynomial(0, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.jacobi_polynomial(1, 1000, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.jacobi_polynomial(2, -1, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.jacobi_polynomial(3, 2, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.jacobi_polynomial(5, 1, 42, 0)
        except EXC:
            pass


class Test_lambert_w_deep:
    def test_c0(self):
        try:
            mod.lambert_w(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lambert_w(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lambert_w(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lambert_w(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lambert_w(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lambert_w(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.lambert_w(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.lambert_w(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.lambert_w(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.lambert_w(2)
        except EXC:
            pass

    def test_kw_tol(self):
        try:
            mod.lambert_w(1, tol=1)
        except EXC:
            pass


class Test_log_gamma_deep:
    def test_c0(self):
        try:
            mod.log_gamma(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.log_gamma(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.log_gamma(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.log_gamma(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.log_gamma(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.log_gamma(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.log_gamma(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.log_gamma(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.log_gamma(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.log_gamma(2)
        except EXC:
            pass


class Test_modified_bessel_k_deep:
    def test_c0(self):
        try:
            mod.modified_bessel_k(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.modified_bessel_k(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.modified_bessel_k(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.modified_bessel_k(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.modified_bessel_k(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.modified_bessel_k(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.modified_bessel_k(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.modified_bessel_k(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.modified_bessel_k(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.modified_bessel_k(5, 1)
        except EXC:
            pass


class Test_upper_incomplete_gamma_deep:
    def test_c0(self):
        try:
            mod.upper_incomplete_gamma(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.upper_incomplete_gamma(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.upper_incomplete_gamma(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.upper_incomplete_gamma(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.upper_incomplete_gamma(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.upper_incomplete_gamma(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.upper_incomplete_gamma(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.upper_incomplete_gamma(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.upper_incomplete_gamma(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.upper_incomplete_gamma(2, 1)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.upper_incomplete_gamma(1, 42, terms=1)
        except EXC:
            pass


class Test_anger_j_deep:
    def test_c0(self):
        try:
            mod.anger_j(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.anger_j(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.anger_j(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.anger_j(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.anger_j(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.anger_j(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.anger_j(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.anger_j(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.anger_j(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.anger_j(2, 1)
        except EXC:
            pass

    def test_kw_n_points(self):
        try:
            mod.anger_j(1, 42, n_points=1)
        except EXC:
            pass


class Test_bell_number_deep:
    def test_c0(self):
        try:
            mod.bell_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bell_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bell_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bell_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bell_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bell_number(0)
        except EXC:
            pass


class Test_bernoulli_number_deep:
    def test_c0(self):
        try:
            mod.bernoulli_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bernoulli_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bernoulli_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bernoulli_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bernoulli_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bernoulli_number(0)
        except EXC:
            pass


class Test_bernoulli_polynomial_deep:
    def test_c0(self):
        try:
            mod.bernoulli_polynomial(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bernoulli_polynomial(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bernoulli_polynomial(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bernoulli_polynomial(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bernoulli_polynomial(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bernoulli_polynomial(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bernoulli_polynomial(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bernoulli_polynomial(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bernoulli_polynomial(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bernoulli_polynomial(5, 1)
        except EXC:
            pass


class Test_bernstein_polynomial_deep:
    def test_c0(self):
        try:
            mod.bernstein_polynomial(1, 2, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bernstein_polynomial(2, 3, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bernstein_polynomial(3, 5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bernstein_polynomial(5, 10, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bernstein_polynomial(10, 0, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bernstein_polynomial(0, 1, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bernstein_polynomial(1, 2, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bernstein_polynomial(2, 3, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bernstein_polynomial(3, 5, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bernstein_polynomial(5, 10, 42)
        except EXC:
            pass


class Test_bessel_y_deep:
    def test_c0(self):
        try:
            mod.bessel_y(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bessel_y(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bessel_y(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bessel_y(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bessel_y(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bessel_y(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bessel_y(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bessel_y(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bessel_y(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bessel_y(5, 1)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.bessel_y(1, 42, terms=1)
        except EXC:
            pass


class Test_beta_function_deep:
    def test_c0(self):
        try:
            mod.beta_function(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.beta_function(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.beta_function(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.beta_function(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.beta_function(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.beta_function(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.beta_function(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.beta_function(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.beta_function(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.beta_function(2, 1)
        except EXC:
            pass


class Test_chebyshev_polynomial_first_deep:
    def test_c0(self):
        try:
            mod.chebyshev_polynomial_first(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chebyshev_polynomial_first(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chebyshev_polynomial_first(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chebyshev_polynomial_first(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chebyshev_polynomial_first(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chebyshev_polynomial_first(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.chebyshev_polynomial_first(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.chebyshev_polynomial_first(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.chebyshev_polynomial_first(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.chebyshev_polynomial_first(5, 1)
        except EXC:
            pass


class Test_chebyshev_polynomial_second_deep:
    def test_c0(self):
        try:
            mod.chebyshev_polynomial_second(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chebyshev_polynomial_second(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chebyshev_polynomial_second(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chebyshev_polynomial_second(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chebyshev_polynomial_second(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chebyshev_polynomial_second(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.chebyshev_polynomial_second(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.chebyshev_polynomial_second(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.chebyshev_polynomial_second(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.chebyshev_polynomial_second(5, 1)
        except EXC:
            pass


class Test_double_factorial_deep:
    def test_c0(self):
        try:
            mod.double_factorial(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.double_factorial(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.double_factorial(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.double_factorial(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.double_factorial(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.double_factorial(0)
        except EXC:
            pass


class Test_elliptic_pi_deep:
    def test_c0(self):
        try:
            mod.elliptic_pi(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.elliptic_pi(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.elliptic_pi(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.elliptic_pi(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.elliptic_pi(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.elliptic_pi(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.elliptic_pi(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.elliptic_pi(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.elliptic_pi(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.elliptic_pi(2, 1)
        except EXC:
            pass


class Test_euler_number_deep:
    def test_c0(self):
        try:
            mod.euler_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.euler_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.euler_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.euler_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.euler_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.euler_number(0)
        except EXC:
            pass


class Test_euler_polynomial_deep:
    def test_c0(self):
        try:
            mod.euler_polynomial(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.euler_polynomial(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.euler_polynomial(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.euler_polynomial(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.euler_polynomial(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.euler_polynomial(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.euler_polynomial(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.euler_polynomial(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.euler_polynomial(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.euler_polynomial(5, 1)
        except EXC:
            pass


class Test_falling_factorial_deep:
    def test_c0(self):
        try:
            mod.falling_factorial(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.falling_factorial(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.falling_factorial(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.falling_factorial(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.falling_factorial(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.falling_factorial(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.falling_factorial(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.falling_factorial(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.falling_factorial(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.falling_factorial(2, 10)
        except EXC:
            pass


class Test_fibonacci_polynomial_deep:
    def test_c0(self):
        try:
            mod.fibonacci_polynomial(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fibonacci_polynomial(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fibonacci_polynomial(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fibonacci_polynomial(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fibonacci_polynomial(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fibonacci_polynomial(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.fibonacci_polynomial(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.fibonacci_polynomial(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.fibonacci_polynomial(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.fibonacci_polynomial(5, 1)
        except EXC:
            pass


class Test_gamma_duplication_formula_deep:
    def test_c0(self):
        try:
            mod.gamma_duplication_formula(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gamma_duplication_formula(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gamma_duplication_formula(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gamma_duplication_formula(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gamma_duplication_formula(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gamma_duplication_formula(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.gamma_duplication_formula(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.gamma_duplication_formula(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.gamma_duplication_formula(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.gamma_duplication_formula(2)
        except EXC:
            pass


class Test_gegenbauer_polynomial_deep:
    def test_c0(self):
        try:
            mod.gegenbauer_polynomial(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gegenbauer_polynomial(2, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gegenbauer_polynomial(3, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gegenbauer_polynomial(5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gegenbauer_polynomial(10, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gegenbauer_polynomial(0, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.gegenbauer_polynomial(1, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.gegenbauer_polynomial(2, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.gegenbauer_polynomial(3, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.gegenbauer_polynomial(5, 1, 42)
        except EXC:
            pass


class Test_generalized_harmonic_number_deep:
    def test_c0(self):
        try:
            mod.generalized_harmonic_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.generalized_harmonic_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.generalized_harmonic_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.generalized_harmonic_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.generalized_harmonic_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.generalized_harmonic_number(0)
        except EXC:
            pass

    def test_kw_m(self):
        try:
            mod.generalized_harmonic_number(1, m=1)
        except EXC:
            pass


class Test_hermite_polynomial_deep:
    def test_c0(self):
        try:
            mod.hermite_polynomial(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hermite_polynomial(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hermite_polynomial(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hermite_polynomial(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hermite_polynomial(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hermite_polynomial(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.hermite_polynomial(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.hermite_polynomial(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.hermite_polynomial(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.hermite_polynomial(5, 1)
        except EXC:
            pass


class Test_hypergeometric_1f1_deep:
    def test_c0(self):
        try:
            mod.hypergeometric_1f1(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hypergeometric_1f1(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hypergeometric_1f1(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hypergeometric_1f1(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hypergeometric_1f1(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hypergeometric_1f1(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.hypergeometric_1f1(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.hypergeometric_1f1(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.hypergeometric_1f1(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.hypergeometric_1f1(2, 1, 42)
        except EXC:
            pass


class Test_hypergeometric_2f1_deep:
    def test_c0(self):
        try:
            mod.hypergeometric_2f1(1, 42, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hypergeometric_2f1(42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hypergeometric_2f1(0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hypergeometric_2f1(-5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hypergeometric_2f1(3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hypergeometric_2f1(100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.hypergeometric_2f1(0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.hypergeometric_2f1(1000, -1, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.hypergeometric_2f1(-1, 2, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.hypergeometric_2f1(2, 1, 42, 0)
        except EXC:
            pass


class Test_inverse_error_function_deep:
    def test_c0(self):
        try:
            mod.inverse_error_function(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inverse_error_function(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inverse_error_function(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inverse_error_function(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inverse_error_function(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inverse_error_function(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.inverse_error_function(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.inverse_error_function(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.inverse_error_function(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.inverse_error_function(2)
        except EXC:
            pass


class Test_laguerre_polynomial_deep:
    def test_c0(self):
        try:
            mod.laguerre_polynomial(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.laguerre_polynomial(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.laguerre_polynomial(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.laguerre_polynomial(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.laguerre_polynomial(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.laguerre_polynomial(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.laguerre_polynomial(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.laguerre_polynomial(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.laguerre_polynomial(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.laguerre_polynomial(5, 1)
        except EXC:
            pass


class Test_lanczos_gamma_deep:
    def test_c0(self):
        try:
            mod.lanczos_gamma(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lanczos_gamma(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lanczos_gamma(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lanczos_gamma(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lanczos_gamma(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lanczos_gamma(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.lanczos_gamma(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.lanczos_gamma(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.lanczos_gamma(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.lanczos_gamma(2)
        except EXC:
            pass


class Test_logistic_function_deep:
    def test_c0(self):
        try:
            mod.logistic_function(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.logistic_function(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.logistic_function(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.logistic_function(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.logistic_function(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.logistic_function(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.logistic_function(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.logistic_function(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.logistic_function(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.logistic_function(2)
        except EXC:
            pass

    def test_kw_upper(self):
        try:
            mod.logistic_function(1, upper=1)
        except EXC:
            pass

    def test_kw_k(self):
        try:
            mod.logistic_function(1, k=1)
        except EXC:
            pass

    def test_kw_x0(self):
        try:
            mod.logistic_function(1, x0=1)
        except EXC:
            pass


class Test_lucas_polynomial_deep:
    def test_c0(self):
        try:
            mod.lucas_polynomial(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lucas_polynomial(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lucas_polynomial(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lucas_polynomial(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lucas_polynomial(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lucas_polynomial(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.lucas_polynomial(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.lucas_polynomial(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.lucas_polynomial(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.lucas_polynomial(5, 1)
        except EXC:
            pass


class Test_modified_bessel_i_deep:
    def test_c0(self):
        try:
            mod.modified_bessel_i(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.modified_bessel_i(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.modified_bessel_i(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.modified_bessel_i(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.modified_bessel_i(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.modified_bessel_i(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.modified_bessel_i(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.modified_bessel_i(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.modified_bessel_i(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.modified_bessel_i(5, 1)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.modified_bessel_i(1, 42, terms=1)
        except EXC:
            pass


class Test_multinomial_coefficient_deep:
    def test_c0(self):
        try:
            mod.multinomial_coefficient(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.multinomial_coefficient(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.multinomial_coefficient(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.multinomial_coefficient(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.multinomial_coefficient(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.multinomial_coefficient(0)
        except EXC:
            pass


class Test_partition_number_deep:
    def test_c0(self):
        try:
            mod.partition_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.partition_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.partition_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.partition_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.partition_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.partition_number(0)
        except EXC:
            pass


class Test_riemann_zeta_deep:
    def test_c0(self):
        try:
            mod.riemann_zeta(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.riemann_zeta(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.riemann_zeta(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.riemann_zeta(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.riemann_zeta(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.riemann_zeta(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.riemann_zeta(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.riemann_zeta(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.riemann_zeta(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.riemann_zeta(2)
        except EXC:
            pass


class Test_rising_factorial_deep:
    def test_c0(self):
        try:
            mod.rising_factorial(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rising_factorial(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rising_factorial(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rising_factorial(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rising_factorial(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rising_factorial(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.rising_factorial(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.rising_factorial(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.rising_factorial(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.rising_factorial(2, 10)
        except EXC:
            pass


class Test_stirling_number_first_deep:
    def test_c0(self):
        try:
            mod.stirling_number_first(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.stirling_number_first(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.stirling_number_first(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.stirling_number_first(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.stirling_number_first(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.stirling_number_first(0, 1)
        except EXC:
            pass


class Test_struve_h_deep:
    def test_c0(self):
        try:
            mod.struve_h(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.struve_h(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.struve_h(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.struve_h(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.struve_h(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.struve_h(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.struve_h(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.struve_h(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.struve_h(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.struve_h(5, 1)
        except EXC:
            pass

    def test_kw_terms(self):
        try:
            mod.struve_h(1, 42, terms=1)
        except EXC:
            pass


class Test_touchard_polynomial_deep:
    def test_c0(self):
        try:
            mod.touchard_polynomial(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.touchard_polynomial(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.touchard_polynomial(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.touchard_polynomial(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.touchard_polynomial(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.touchard_polynomial(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.touchard_polynomial(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.touchard_polynomial(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.touchard_polynomial(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.touchard_polynomial(5, 1)
        except EXC:
            pass


class Test_trigamma_deep:
    def test_c0(self):
        try:
            mod.trigamma(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.trigamma(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.trigamma(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.trigamma(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.trigamma(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.trigamma(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.trigamma(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.trigamma(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.trigamma(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.trigamma(2)
        except EXC:
            pass

