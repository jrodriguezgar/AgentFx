"""Tests for fxNumeric.complex_functions."""

import math

import pytest

from agentfx.fxNumeric import (
    complex_add,
    complex_argument,
    complex_argument_degrees,
    complex_conjugate,
    complex_cos,
    complex_cosh,
    complex_distance,
    complex_divide,
    complex_exp,
    complex_from_polar,
    complex_lerp,
    complex_ln,
    complex_log,
    complex_midpoint,
    complex_modulus,
    complex_multiply,
    complex_nth_root,
    complex_polar_form,
    complex_power,
    complex_reciprocal,
    complex_rotate,
    complex_sin,
    complex_sinh,
    complex_sqrt,
    complex_subtract,
    complex_tan,
    complex_to_polar,
    de_moivre,
    euler_formula,
    nth_roots_complex,
    polar_to_complex,
    roots_of_unity,
)


class TestComplexTan:
    def test_real(self):
        re, im = complex_tan((1.0, 0.0))
        assert round(re, 4) == 1.5574
        assert im == pytest.approx(0.0, abs=1e-10)

    def test_imaginary(self):
        re, im = complex_tan((0.0, 1.0))
        assert re == pytest.approx(0.0, abs=1e-10)
        assert im == pytest.approx(math.tanh(1.0), rel=1e-8)

class TestComplexSinh:
    def test_real(self):
        re, im = complex_sinh((1.0, 0.0))
        assert round(re, 4) == 1.1752
        assert im == pytest.approx(0.0, abs=1e-10)

    def test_zero(self):
        re, im = complex_sinh((0.0, 0.0))
        assert re == pytest.approx(0.0, abs=1e-10)

class TestComplexCosh:
    def test_real(self):
        re, im = complex_cosh((1.0, 0.0))
        assert round(re, 4) == 1.5431
        assert im == pytest.approx(0.0, abs=1e-10)

class TestComplexLog:
    def test_one(self):
        re, im = complex_log((1.0, 0.0))
        assert re == pytest.approx(0.0, abs=1e-10)
        assert im == pytest.approx(0.0, abs=1e-10)

    def test_negative(self):
        re, im = complex_log((-1.0, 0.0))
        assert re == pytest.approx(0.0, abs=1e-10)
        assert im == pytest.approx(math.pi, rel=1e-8)

    def test_zero(self):
        with pytest.raises(ValueError):
            complex_log((0.0, 0.0))

class TestComplexSqrt:
    def test_negative_one(self):
        re, im = complex_sqrt((-1.0, 0.0))
        assert re == pytest.approx(0.0, abs=1e-10)
        assert im == pytest.approx(1.0, rel=1e-8)

    def test_positive(self):
        re, im = complex_sqrt((4.0, 0.0))
        assert re == pytest.approx(2.0, rel=1e-8)
        assert im == pytest.approx(0.0, abs=1e-10)

class TestComplexReciprocal:
    def test_basic(self):
        re, im = complex_reciprocal((2.0, 0.0))
        assert re == pytest.approx(0.5)

    def test_zero(self):
        with pytest.raises(ValueError):
            complex_reciprocal((0.0, 0.0))

class TestComplexNthRoot:
    def test_cube_root_one(self):
        re, im = complex_nth_root((1.0, 0.0), 3)
        assert re == pytest.approx(1.0, rel=1e-8)
        assert im == pytest.approx(0.0, abs=1e-10)

    def test_second_root(self):
        re, im = complex_nth_root((1.0, 0.0), 3, 1)
        # Should be on unit circle
        assert re**2 + im**2 == pytest.approx(1.0, rel=1e-8)

    def test_invalid_n(self):
        with pytest.raises(ValueError):
            complex_nth_root((1.0, 0.0), 0)

class TestComplexDistance:
    def test_basic(self):
        assert complex_distance((0, 0), (3, 4)) == 5.0

    def test_same_point(self):
        assert complex_distance((1, 2), (1, 2)) == pytest.approx(0.0, abs=1e-10)

class TestComplexRotate:
    def test_quarter_turn(self):
        re, im = complex_rotate((1.0, 0.0), math.pi / 2)
        assert re == pytest.approx(0.0, abs=1e-10)
        assert im == pytest.approx(1.0, rel=1e-8)

    def test_full_turn(self):
        re, im = complex_rotate((1.0, 0.0), 2 * math.pi)
        assert re == pytest.approx(1.0, rel=1e-8)
        assert im == pytest.approx(0.0, abs=1e-10)

class TestComplexPolarForm:
    def test_basic(self):
        r, theta = complex_polar_form((1.0, 1.0))
        assert r == pytest.approx(math.sqrt(2.0), rel=1e-8)
        assert theta == pytest.approx(math.pi / 4, rel=1e-8)

    def test_real_positive(self):
        r, theta = complex_polar_form((5.0, 0.0))
        assert r == pytest.approx(5.0)
        assert theta == pytest.approx(0.0, abs=1e-10)

class TestComplexFromPolar:
    def test_unit(self):
        re, im = complex_from_polar(1.0, 0.0)
        assert re == pytest.approx(1.0)
        assert im == pytest.approx(0.0, abs=1e-10)

    def test_imaginary(self):
        re, im = complex_from_polar(1.0, math.pi / 2)
        assert re == pytest.approx(0.0, abs=1e-10)
        assert im == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            complex_from_polar("a", 0)

class TestComplexConjugate:
    def test_basic(self):
        assert complex_conjugate((3.0, 4.0)) == (3.0, -4.0)

    def test_real(self):
        assert complex_conjugate((5.0, 0.0)) == (5.0, 0.0)

class TestComplexArgumentDegrees:
    def test_45(self):
        assert complex_argument_degrees((1.0, 1.0)) == 45.0

    def test_negative(self):
        assert complex_argument_degrees((1.0, -1.0)) == -45.0

class TestComplexMidpoint:
    def test_basic(self):
        assert complex_midpoint((0, 0), (4, 6)) == (2.0, 3.0)

    def test_same_point(self):
        assert complex_midpoint((2, 3), (2, 3)) == (2.0, 3.0)

class TestComplexLerp:
    def test_half(self):
        assert complex_lerp((0, 0), (4, 6), 0.5) == (2.0, 3.0)

    def test_zero(self):
        assert complex_lerp((0, 0), (4, 6), 0.0) == (0.0, 0.0)

    def test_one(self):
        assert complex_lerp((0, 0), (4, 6), 1.0) == (4.0, 6.0)

class TestComplexArithmetic:

    def test_add(self):
        assert complex_add((1, 2), (3, 4)) == (4, 6)

    def test_subtract(self):
        assert complex_subtract((5, 3), (2, 1)) == (3, 2)

    def test_multiply(self):
        # (1+2i)(3+4i) = 3+4i+6i+8i² = 3+10i-8 = (-5, 10)
        assert complex_multiply((1, 2), (3, 4)) == (-5, 10)

    def test_divide(self):
        # (1+0i)/(0+1i) = -i → (0, -1)
        re, im = complex_divide((1, 0), (0, 1))
        assert abs(re - 0) < 1e-10
        assert abs(im - (-1)) < 1e-10

    def test_divide_by_zero(self):
        with pytest.raises(ZeroDivisionError):
            complex_divide((1, 0), (0, 0))

    def test_modulus(self):
        assert complex_modulus((3, 4)) == 5.0

    def test_argument(self):
        assert abs(complex_argument((1, 1)) - math.pi / 4) < 1e-10

    def test_conjugate(self):
        assert complex_conjugate((3, -7)) == (3, 7)

    def test_to_polar_and_back(self):
        r, theta = complex_to_polar((1, 1))
        re, im = polar_to_complex(r, theta)
        assert abs(re - 1) < 1e-10
        assert abs(im - 1) < 1e-10

    def test_de_moivre(self):
        # (1 * e^(i pi/4))^4 = cos(pi) + i sin(pi) = (-1, 0)
        re, im = de_moivre(1, math.pi / 4, 4)
        assert abs(re - (-1)) < 1e-10
        assert abs(im) < 1e-10

    def test_roots_of_unity(self):
        roots = roots_of_unity(4)
        assert len(roots) == 4
        # First root: (1, 0)
        assert abs(roots[0][0] - 1) < 1e-10
        assert abs(roots[0][1]) < 1e-10

    def test_nth_roots_complex(self):
        # Cube roots of 8 (8+0i)
        roots = nth_roots_complex((8, 0), 3)
        assert len(roots) == 3
        # One root should be (2, 0)
        found = any(abs(r - 2) < 1e-6 and abs(i) < 1e-6 for r, i in roots)
        assert found

    def test_euler_formula(self):
        re, im = euler_formula(math.pi)
        assert abs(re - (-1)) < 1e-10
        assert abs(im) < 1e-10

    def test_complex_power(self):
        # (0+i)^(2+0i) = -1+0i
        re, im = complex_power((0, 1), (2, 0))
        assert abs(re - (-1)) < 1e-6
        assert abs(im) < 1e-6

    def test_complex_exp(self):
        # e^(i*pi) = -1
        re, im = complex_exp((0, math.pi))
        assert abs(re - (-1)) < 1e-10
        assert abs(im) < 1e-10

    def test_complex_ln(self):
        # ln(e) = 1+0i
        re, im = complex_ln((math.e, 0))
        assert abs(re - 1) < 1e-10
        assert abs(im) < 1e-10

    def test_complex_sin(self):
        # sin(0+0i) = 0+0i
        re, im = complex_sin((0, 0))
        assert abs(re) < 1e-10
        assert abs(im) < 1e-10

    def test_complex_cos(self):
        # cos(0+0i) = 1+0i
        re, im = complex_cos((0, 0))
        assert abs(re - 1) < 1e-10
        assert abs(im) < 1e-10


# ===================================================================
# Inequalities
# ===================================================================
