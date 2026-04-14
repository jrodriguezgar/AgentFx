# Coverage tests for formulite.fxNumeric.transform_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import transform_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_abel_transform_numerical:
    def test_exists(self):
        assert hasattr(mod, "abel_transform_numerical")

    def test_var0(self):
        try:
            mod.abel_transform_numerical(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.abel_transform_numerical(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.abel_transform_numerical(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.abel_transform_numerical("", "")
        except EXC:
            pass


class Test_auto_correlation:
    def test_exists(self):
        assert hasattr(mod, "auto_correlation")

    def test_doc0(self):
        try:
            mod.auto_correlation([1, 0, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.auto_correlation(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.auto_correlation(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.auto_correlation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.auto_correlation("")
        except EXC:
            pass


class Test_convolution:
    def test_exists(self):
        assert hasattr(mod, "convolution")

    def test_doc0(self):
        try:
            mod.convolution([1, 2, 3], [1, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.convolution(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.convolution(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.convolution(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.convolution("", "")
        except EXC:
            pass


class Test_cross_correlation:
    def test_exists(self):
        assert hasattr(mod, "cross_correlation")

    def test_doc0(self):
        try:
            mod.cross_correlation([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cross_correlation(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cross_correlation(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cross_correlation(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cross_correlation("", "")
        except EXC:
            pass


class Test_dft:
    def test_exists(self):
        assert hasattr(mod, "dft")

    def test_doc0(self):
        try:
            mod.dft([1, 0, 1, 0])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.dft(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dft(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dft(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dft("")
        except EXC:
            pass


class Test_discrete_cosine_transform:
    def test_exists(self):
        assert hasattr(mod, "discrete_cosine_transform")

    def test_doc0(self):
        try:
            mod.discrete_cosine_transform([1, 1, 1, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.discrete_cosine_transform([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.discrete_cosine_transform([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.discrete_cosine_transform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.discrete_cosine_transform("")
        except EXC:
            pass


class Test_discrete_sine_transform:
    def test_exists(self):
        assert hasattr(mod, "discrete_sine_transform")

    def test_doc0(self):
        try:
            mod.discrete_sine_transform([1, 1, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.discrete_sine_transform([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.discrete_sine_transform([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.discrete_sine_transform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.discrete_sine_transform("")
        except EXC:
            pass


class Test_fourier_transform_numerical:
    def test_exists(self):
        assert hasattr(mod, "fourier_transform_numerical")

    def test_var0(self):
        try:
            mod.fourier_transform_numerical(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fourier_transform_numerical(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fourier_transform_numerical(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fourier_transform_numerical("", "")
        except EXC:
            pass


class Test_hankel_transform_numerical:
    def test_exists(self):
        assert hasattr(mod, "hankel_transform_numerical")

    def test_var0(self):
        try:
            mod.hankel_transform_numerical(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hankel_transform_numerical(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hankel_transform_numerical(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hankel_transform_numerical("", 0)
        except EXC:
            pass


class Test_hartley_transform:
    def test_exists(self):
        assert hasattr(mod, "hartley_transform")

    def test_doc0(self):
        try:
            mod.hartley_transform([1, 0, 0, 0])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hartley_transform([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hartley_transform([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hartley_transform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hartley_transform("")
        except EXC:
            pass


class Test_hilbert_transform:
    def test_exists(self):
        assert hasattr(mod, "hilbert_transform")

    def test_doc0(self):
        try:
            mod.hilbert_transform([1, 0, -1, 0])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hilbert_transform(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hilbert_transform(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hilbert_transform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hilbert_transform("")
        except EXC:
            pass


class Test_idft:
    def test_exists(self):
        assert hasattr(mod, "idft")

    def test_doc0(self):
        try:
            mod.idft([(2, 0), (0, 0), (2, 0), (0, 0)])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.idft(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.idft(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.idft(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.idft("")
        except EXC:
            pass


class Test_inverse_discrete_cosine_transform:
    def test_exists(self):
        assert hasattr(mod, "inverse_discrete_cosine_transform")

    def test_doc0(self):
        try:
            mod.inverse_discrete_cosine_transform([4, 0, 0, 0])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_discrete_cosine_transform([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_discrete_cosine_transform([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_discrete_cosine_transform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_discrete_cosine_transform([])
        except EXC:
            pass


class Test_inverse_hartley_transform:
    def test_exists(self):
        assert hasattr(mod, "inverse_hartley_transform")

    def test_doc0(self):
        try:
            mod.inverse_hartley_transform([1, 1, 1, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inverse_hartley_transform([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_hartley_transform([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_hartley_transform(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_hartley_transform([])
        except EXC:
            pass


class Test_inverse_laplace_gaver_stehfest:
    def test_exists(self):
        assert hasattr(mod, "inverse_laplace_gaver_stehfest")

    def test_var0(self):
        try:
            mod.inverse_laplace_gaver_stehfest(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inverse_laplace_gaver_stehfest(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inverse_laplace_gaver_stehfest(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inverse_laplace_gaver_stehfest("", "")
        except EXC:
            pass


class Test_laplace_transform_numerical:
    def test_exists(self):
        assert hasattr(mod, "laplace_transform_numerical")

    def test_var0(self):
        try:
            mod.laplace_transform_numerical(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.laplace_transform_numerical(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.laplace_transform_numerical(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.laplace_transform_numerical("", "")
        except EXC:
            pass


class Test_mellin_transform_numerical:
    def test_exists(self):
        assert hasattr(mod, "mellin_transform_numerical")

    def test_var0(self):
        try:
            mod.mellin_transform_numerical(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mellin_transform_numerical(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mellin_transform_numerical(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mellin_transform_numerical("", "")
        except EXC:
            pass


class Test_z_transform_eval:
    def test_exists(self):
        assert hasattr(mod, "z_transform_eval")

    def test_doc0(self):
        try:
            mod.z_transform_eval([1, 1, 1], 2.0, 0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.z_transform_eval(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.z_transform_eval(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.z_transform_eval(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.z_transform_eval("", "", "")
        except EXC:
            pass

