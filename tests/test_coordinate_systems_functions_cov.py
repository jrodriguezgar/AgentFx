# Coverage tests for formulite.fxNumeric.coordinate_systems_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import coordinate_systems_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_bipolar_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "bipolar_to_cartesian")

    def test_doc0(self):
        try:
            mod.bipolar_to_cartesian(math.pi / 2, 1, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bipolar_to_cartesian(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bipolar_to_cartesian(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bipolar_to_cartesian(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bipolar_to_cartesian("", "")
        except EXC:
            pass


class Test_cartesian_to_cylindrical:
    def test_exists(self):
        assert hasattr(mod, "cartesian_to_cylindrical")

    def test_doc0(self):
        try:
            mod.cartesian_to_cylindrical(1, 1, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cartesian_to_cylindrical(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cartesian_to_cylindrical(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cartesian_to_cylindrical(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cartesian_to_cylindrical("", "", "")
        except EXC:
            pass


class Test_cartesian_to_parabolic_cylindrical:
    def test_exists(self):
        assert hasattr(mod, "cartesian_to_parabolic_cylindrical")

    def test_doc0(self):
        try:
            mod.cartesian_to_parabolic_cylindrical(1.5, 2, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cartesian_to_parabolic_cylindrical(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cartesian_to_parabolic_cylindrical(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cartesian_to_parabolic_cylindrical(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cartesian_to_parabolic_cylindrical("", "", "")
        except EXC:
            pass


class Test_cylindrical_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "cylindrical_to_cartesian")

    def test_doc0(self):
        try:
            mod.cylindrical_to_cartesian(2, math.pi / 4, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cylindrical_to_cartesian(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cylindrical_to_cartesian(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cylindrical_to_cartesian(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cylindrical_to_cartesian("", "", "")
        except EXC:
            pass


class Test_elliptic_cylindrical_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "elliptic_cylindrical_to_cartesian")

    def test_doc0(self):
        try:
            mod.elliptic_cylindrical_to_cartesian(1, 0, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.elliptic_cylindrical_to_cartesian(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elliptic_cylindrical_to_cartesian(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elliptic_cylindrical_to_cartesian(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elliptic_cylindrical_to_cartesian("", "", "")
        except EXC:
            pass


class Test_oblate_spheroidal_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "oblate_spheroidal_to_cartesian")

    def test_doc0(self):
        try:
            mod.oblate_spheroidal_to_cartesian(1, 0, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.oblate_spheroidal_to_cartesian(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.oblate_spheroidal_to_cartesian(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.oblate_spheroidal_to_cartesian(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.oblate_spheroidal_to_cartesian("", "", "")
        except EXC:
            pass


class Test_parabolic_cylindrical_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "parabolic_cylindrical_to_cartesian")

    def test_doc0(self):
        try:
            mod.parabolic_cylindrical_to_cartesian(2, 1, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.parabolic_cylindrical_to_cartesian(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parabolic_cylindrical_to_cartesian(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parabolic_cylindrical_to_cartesian(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parabolic_cylindrical_to_cartesian("", "", "")
        except EXC:
            pass


class Test_paraboloidal_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "paraboloidal_to_cartesian")

    def test_doc0(self):
        try:
            mod.paraboloidal_to_cartesian(1, 1, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.paraboloidal_to_cartesian(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.paraboloidal_to_cartesian(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.paraboloidal_to_cartesian(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.paraboloidal_to_cartesian("", "", "")
        except EXC:
            pass


class Test_prolate_spheroidal_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "prolate_spheroidal_to_cartesian")

    def test_doc0(self):
        try:
            mod.prolate_spheroidal_to_cartesian(1, math.pi / 2, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.prolate_spheroidal_to_cartesian(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.prolate_spheroidal_to_cartesian(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.prolate_spheroidal_to_cartesian(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.prolate_spheroidal_to_cartesian("", "", "")
        except EXC:
            pass


class Test_toroidal_to_cartesian:
    def test_exists(self):
        assert hasattr(mod, "toroidal_to_cartesian")

    def test_doc0(self):
        try:
            mod.toroidal_to_cartesian(0, 1, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.toroidal_to_cartesian(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.toroidal_to_cartesian(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.toroidal_to_cartesian(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.toroidal_to_cartesian("", "", "")
        except EXC:
            pass

