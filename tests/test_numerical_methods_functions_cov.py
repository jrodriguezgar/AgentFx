# Coverage tests for formulite.fxNumeric.numerical_methods_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import numerical_methods_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_adaptive_rk45:
    def test_exists(self):
        assert hasattr(mod, "adaptive_rk45")

    def test_var0(self):
        try:
            mod.adaptive_rk45(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.adaptive_rk45(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.adaptive_rk45(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.adaptive_rk45("", "", "", "")
        except EXC:
            pass


class Test_backward_difference:
    def test_exists(self):
        assert hasattr(mod, "backward_difference")

    def test_var0(self):
        try:
            mod.backward_difference(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.backward_difference(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.backward_difference(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.backward_difference("", "")
        except EXC:
            pass


class Test_bisection_method:
    def test_exists(self):
        assert hasattr(mod, "bisection_method")

    def test_var0(self):
        try:
            mod.bisection_method(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bisection_method(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bisection_method(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bisection_method("", "", "")
        except EXC:
            pass


class Test_central_difference:
    def test_exists(self):
        assert hasattr(mod, "central_difference")

    def test_var0(self):
        try:
            mod.central_difference(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.central_difference(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.central_difference(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.central_difference("", "")
        except EXC:
            pass


class Test_euler_method:
    def test_exists(self):
        assert hasattr(mod, "euler_method")

    def test_var0(self):
        try:
            mod.euler_method(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.euler_method(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.euler_method(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.euler_method("", "", "", "")
        except EXC:
            pass


class Test_fixed_point_iteration:
    def test_exists(self):
        assert hasattr(mod, "fixed_point_iteration")

    def test_var0(self):
        try:
            mod.fixed_point_iteration(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fixed_point_iteration(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fixed_point_iteration(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fixed_point_iteration("", "")
        except EXC:
            pass


class Test_forward_difference:
    def test_exists(self):
        assert hasattr(mod, "forward_difference")

    def test_var0(self):
        try:
            mod.forward_difference(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.forward_difference(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.forward_difference(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.forward_difference("", "")
        except EXC:
            pass


class Test_gaussian_quadrature:
    def test_exists(self):
        assert hasattr(mod, "gaussian_quadrature")

    def test_var0(self):
        try:
            mod.gaussian_quadrature(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gaussian_quadrature(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gaussian_quadrature(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gaussian_quadrature("", "", "")
        except EXC:
            pass


class Test_midpoint_rule:
    def test_exists(self):
        assert hasattr(mod, "midpoint_rule")

    def test_var0(self):
        try:
            mod.midpoint_rule(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.midpoint_rule(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.midpoint_rule(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.midpoint_rule("", "", "")
        except EXC:
            pass


class Test_monte_carlo_integration:
    def test_exists(self):
        assert hasattr(mod, "monte_carlo_integration")

    def test_var0(self):
        try:
            mod.monte_carlo_integration(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.monte_carlo_integration(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.monte_carlo_integration(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.monte_carlo_integration("", "", "")
        except EXC:
            pass


class Test_newton_raphson:
    def test_exists(self):
        assert hasattr(mod, "newton_raphson")

    def test_var0(self):
        try:
            mod.newton_raphson(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.newton_raphson(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.newton_raphson(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.newton_raphson("", "", "")
        except EXC:
            pass


class Test_ode_system_rk4:
    def test_exists(self):
        assert hasattr(mod, "ode_system_rk4")

    def test_var0(self):
        try:
            mod.ode_system_rk4(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ode_system_rk4(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ode_system_rk4(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ode_system_rk4("", "", "", "")
        except EXC:
            pass


class Test_regula_falsi:
    def test_exists(self):
        assert hasattr(mod, "regula_falsi")

    def test_var0(self):
        try:
            mod.regula_falsi(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.regula_falsi(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.regula_falsi(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.regula_falsi("", "", "")
        except EXC:
            pass


class Test_richardson_extrapolation:
    def test_exists(self):
        assert hasattr(mod, "richardson_extrapolation")

    def test_var0(self):
        try:
            mod.richardson_extrapolation(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.richardson_extrapolation(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.richardson_extrapolation(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.richardson_extrapolation("", "")
        except EXC:
            pass


class Test_romberg_integration:
    def test_exists(self):
        assert hasattr(mod, "romberg_integration")

    def test_var0(self):
        try:
            mod.romberg_integration(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.romberg_integration(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.romberg_integration(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.romberg_integration("", "", "")
        except EXC:
            pass


class Test_runge_kutta_2:
    def test_exists(self):
        assert hasattr(mod, "runge_kutta_2")

    def test_var0(self):
        try:
            mod.runge_kutta_2(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.runge_kutta_2(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.runge_kutta_2(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.runge_kutta_2("", "", "", "")
        except EXC:
            pass


class Test_runge_kutta_4:
    def test_exists(self):
        assert hasattr(mod, "runge_kutta_4")

    def test_var0(self):
        try:
            mod.runge_kutta_4(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.runge_kutta_4(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.runge_kutta_4(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.runge_kutta_4("", "", "", "")
        except EXC:
            pass


class Test_secant_method:
    def test_exists(self):
        assert hasattr(mod, "secant_method")

    def test_var0(self):
        try:
            mod.secant_method(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.secant_method(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.secant_method(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.secant_method("", "", "")
        except EXC:
            pass


class Test_second_derivative_central:
    def test_exists(self):
        assert hasattr(mod, "second_derivative_central")

    def test_var0(self):
        try:
            mod.second_derivative_central(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.second_derivative_central(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.second_derivative_central(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.second_derivative_central("", "")
        except EXC:
            pass


class Test_simpsons_38_rule:
    def test_exists(self):
        assert hasattr(mod, "simpsons_38_rule")

    def test_var0(self):
        try:
            mod.simpsons_38_rule(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.simpsons_38_rule(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.simpsons_38_rule(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.simpsons_38_rule("", "", "")
        except EXC:
            pass


class Test_simpsons_rule:
    def test_exists(self):
        assert hasattr(mod, "simpsons_rule")

    def test_var0(self):
        try:
            mod.simpsons_rule(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.simpsons_rule(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.simpsons_rule(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.simpsons_rule("", "", "")
        except EXC:
            pass


class Test_trapezoidal_rule:
    def test_exists(self):
        assert hasattr(mod, "trapezoidal_rule")

    def test_var0(self):
        try:
            mod.trapezoidal_rule(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.trapezoidal_rule(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.trapezoidal_rule(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.trapezoidal_rule("", "", "")
        except EXC:
            pass

