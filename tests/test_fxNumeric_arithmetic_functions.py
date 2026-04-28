"""Tests for fxNumeric.arithmetic_functions."""

import math

import pytest

from agentfx.fxNumeric import (
    adjugate_matrix,
    cantor_pairing,
    cantor_unpairing,
    cholesky_decomposition,
    collatz_sequence,
    digit_product,
    integer_partition_distinct,
    is_automorphic,
    is_narcissistic,
    look_and_say,
    lu_decomposition,
    matrix_eigenvalues_2x2,
    matrix_frobenius_norm,
    matrix_infinity_norm,
    matrix_one_norm,
    matrix_power,
    matrix_rank,
    qr_decomposition,
    solve_linear_system,
    square_pyramidal_number,
    sum_first_n_cubes,
    sum_first_n_powers,
    sum_first_n_squares,
    tetrahedral_number,
    triangular_number,
)
from agentfx.fxNumeric.arithmetic_functions import (
    absolute_value,
    chebyshev_nodes,
    combinations,
    exp,
    expm1,
    factorial,
    gamma,
    gcd_list,
    greatest_common_divisor,
    lcm,
    lcm_list,
    permutations,
    romberg_integrate,
    sign,
)


class TestNumericalDerivative:

    def test_sin_at_zero(self):
        from agentfx.fxNumeric.arithmetic_functions import numerical_derivative

        assert round(numerical_derivative(math.sin, 0), 6) == 1.0

    def test_quadratic(self):
        from agentfx.fxNumeric.arithmetic_functions import numerical_derivative

        f = lambda x: x ** 2
        assert numerical_derivative(f, 3) == pytest.approx(6.0, abs=1e-5)

class TestIntegration:

    def test_trapezoidal_sin(self):
        from agentfx.fxNumeric.arithmetic_functions import trapezoidal_integrate

        result = trapezoidal_integrate(math.sin, 0, math.pi, 10000)
        assert result == pytest.approx(2.0, abs=1e-5)

    def test_simpsons_sin(self):
        from agentfx.fxNumeric.arithmetic_functions import simpsons_integrate

        result = simpsons_integrate(math.sin, 0, math.pi, 100)
        assert result == pytest.approx(2.0, abs=1e-7)

    def test_simpsons_odd_n_raises(self):
        from agentfx.fxNumeric.arithmetic_functions import simpsons_integrate

        with pytest.raises(ValueError):
            simpsons_integrate(math.sin, 0, 1, 99)

class TestPolynomial:

    def test_evaluate_quadratic(self):
        from agentfx.fxNumeric.arithmetic_functions import polynomial_evaluate

        assert polynomial_evaluate([1, -3, 2], 2) == 0

    def test_roots_quadratic_real(self):
        from agentfx.fxNumeric.arithmetic_functions import polynomial_roots_quadratic

        r1, r2 = polynomial_roots_quadratic(1, -3, 2)
        assert {r1, r2} == {1.0, 2.0}

    def test_roots_quadratic_complex(self):
        from agentfx.fxNumeric.arithmetic_functions import polynomial_roots_quadratic

        r1, r2 = polynomial_roots_quadratic(1, 0, 1)
        assert r1 == pytest.approx(1j)
        assert r2 == pytest.approx(-1j)

    def test_roots_cubic(self):
        from agentfx.fxNumeric.arithmetic_functions import polynomial_roots_cubic

        roots = polynomial_roots_cubic(1, -6, 11, -6)
        real_roots = sorted([r.real if isinstance(r, complex) else r for r in roots])
        assert real_roots == pytest.approx([1, 2, 3], abs=1e-6)

class TestContinuedFraction:

    def test_pi_approx(self):
        from agentfx.fxNumeric.arithmetic_functions import continued_fraction

        assert continued_fraction(355, 113) == [3, 7, 16]

class TestRungeKutta4:

    def test_exponential_ode(self):
        from agentfx.fxNumeric.arithmetic_functions import runge_kutta_4_step

        t1, y1 = runge_kutta_4_step(lambda t, y: y, 0, 1.0, 0.1)
        assert y1 == pytest.approx(math.exp(0.1), abs=1e-6)


# ── fxNumeric — Statistics ───────────────────────────────────────────────

class TestMatrixTranspose:

    def test_2x3(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_transpose
        assert matrix_transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]

    def test_1x1(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_transpose
        assert matrix_transpose([[42]]) == [[42]]

    def test_empty_raises(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_transpose

        with pytest.raises(ValueError):
            matrix_transpose([])

    def test_jagged_raises(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_transpose

        with pytest.raises(ValueError):
            matrix_transpose([[1, 2], [3]])


# ── Date Operations ──────────────────────────────────────────────

class TestRombergIntegrate:
    def test_sine_integral(self):
        result = romberg_integrate(math.sin, 0, math.pi)
        assert result == pytest.approx(2.0, abs=1e-8)

    def test_type_error(self):
        with pytest.raises(TypeError):
            romberg_integrate("not_a_func", 0, 1)

class TestChebyshevNodes:

    def test_three_nodes(self):
        nodes = chebyshev_nodes(3)
        assert len(nodes) == 3
        assert abs(nodes[0] - 0.866) < 0.001

    def test_invalid_n(self):

        with pytest.raises(ValueError):
            chebyshev_nodes(0)

class TestDigitProduct:
    def test_basic(self):
        assert digit_product(234) == 24

    def test_with_zero(self):
        assert digit_product(102) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            digit_product(1.5)

class TestCollatzSequence:
    def test_six(self):
        assert collatz_sequence(6) == [6, 3, 10, 5, 16, 8, 4, 2, 1]

    def test_one(self):
        assert collatz_sequence(1) == [1]

    def test_type_error(self):
        with pytest.raises(TypeError):
            collatz_sequence(1.5)

class TestIntegerPartitionDistinct:
    def test_ten(self):
        assert integer_partition_distinct(10) == 10

    def test_zero(self):
        assert integer_partition_distinct(0) == 1

    def test_five(self):
        assert integer_partition_distinct(5) == 3

    def test_type_error(self):
        with pytest.raises(TypeError):
            integer_partition_distinct(1.5)

class TestSumFirstNSquares:
    def test_ten(self):
        assert sum_first_n_squares(10) == 385

    def test_zero(self):
        assert sum_first_n_squares(0) == 0

    def test_one(self):
        assert sum_first_n_squares(1) == 1

class TestSumFirstNCubes:
    def test_ten(self):
        assert sum_first_n_cubes(10) == 3025

    def test_zero(self):
        assert sum_first_n_cubes(0) == 0

    def test_five(self):
        assert sum_first_n_cubes(5) == 225

class TestSumFirstNPowers:
    def test_cubes(self):
        assert sum_first_n_powers(5, 3) == 225

    def test_squares(self):
        assert sum_first_n_powers(10, 2) == 385

    def test_type_error(self):
        with pytest.raises(TypeError):
            sum_first_n_powers(5, 1.5)

class TestTriangularNumber:
    def test_ten(self):
        assert triangular_number(10) == 55

    def test_zero(self):
        assert triangular_number(0) == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            triangular_number(1.5)

class TestTetrahedralNumber:
    def test_five(self):
        assert tetrahedral_number(5) == 35

    def test_zero(self):
        assert tetrahedral_number(0) == 0

class TestSquarePyramidalNumber:
    def test_five(self):
        assert square_pyramidal_number(5) == 55

    def test_zero(self):
        assert square_pyramidal_number(0) == 0

class TestIsNarcissistic:
    def test_true(self):
        assert is_narcissistic(153) is True

    def test_false(self):
        assert is_narcissistic(10) is False

    def test_single_digit(self):
        assert is_narcissistic(5) is True

class TestIsAutomorphic:
    def test_true(self):
        assert is_automorphic(76) is True

    def test_false(self):
        assert is_automorphic(10) is False

    def test_five(self):
        assert is_automorphic(5) is True

class TestCantorPairing:
    def test_basic(self):
        assert cantor_pairing(3, 4) == 32

    def test_zero(self):
        assert cantor_pairing(0, 0) == 0

    def test_negative(self):
        with pytest.raises(ValueError):
            cantor_pairing(-1, 0)

class TestCantorUnpairing:
    def test_basic(self):
        assert cantor_unpairing(32) == (3, 4)

    def test_zero(self):
        assert cantor_unpairing(0) == (0, 0)

    def test_roundtrip(self):
        for a in range(5):
            for b in range(5):
                assert cantor_unpairing(cantor_pairing(a, b)) == (a, b)

class TestLookAndSay:
    def test_four(self):
        assert look_and_say("1", 4) == "111221"

    def test_zero(self):
        assert look_and_say("1", 0) == "1"

    def test_type_error(self):
        with pytest.raises(TypeError):
            look_and_say(1, 4)

class TestDotProduct:

    def test_basic(self):
        from agentfx.fxNumeric.arithmetic_functions import dot_product
        assert dot_product([1, 2, 3], [4, 5, 6]) == 32

    def test_orthogonal(self):
        from agentfx.fxNumeric.arithmetic_functions import dot_product
        assert dot_product([1, 0], [0, 1]) == 0

    def test_different_lengths_raises(self):
        from agentfx.fxNumeric.arithmetic_functions import dot_product
        with pytest.raises(ValueError):
            dot_product([1, 2], [3])

class TestCrossProduct:

    def test_unit_vectors(self):
        from agentfx.fxNumeric.arithmetic_functions import cross_product
        assert cross_product([1, 0, 0], [0, 1, 0]) == [0, 0, 1]

    def test_anti_commutative(self):
        from agentfx.fxNumeric.arithmetic_functions import cross_product
        a = [1, 2, 3]
        b = [4, 5, 6]
        ab = cross_product(a, b)
        ba = cross_product(b, a)
        assert ab == [-x for x in ba]

    def test_wrong_dimension_raises(self):
        from agentfx.fxNumeric.arithmetic_functions import cross_product
        with pytest.raises(ValueError):
            cross_product([1, 2], [3, 4])

class TestVectorMagnitude:

    def test_345(self):
        from agentfx.fxNumeric.arithmetic_functions import vector_magnitude
        assert vector_magnitude([3, 4]) == pytest.approx(5.0)

    def test_unit(self):
        from agentfx.fxNumeric.arithmetic_functions import vector_magnitude
        assert vector_magnitude([1, 0, 0]) == pytest.approx(1.0)

    def test_empty_raises(self):
        from agentfx.fxNumeric.arithmetic_functions import vector_magnitude
        with pytest.raises(ValueError):
            vector_magnitude([])

class TestMatrixTrace:

    def test_2x2(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_trace
        assert matrix_trace([[1, 2], [3, 4]]) == 5

    def test_3x3(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_trace
        assert matrix_trace([[1, 0, 0], [0, 2, 0], [0, 0, 3]]) == 6

    def test_non_square_raises(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_trace
        with pytest.raises(ValueError):
            matrix_trace([[1, 2, 3], [4, 5, 6]])


# ── Interpolation ──────────────────────────────────────────────────────────

class TestVectorNormalize:

    def test_basic(self):
        from agentfx.fxNumeric.arithmetic_functions import vector_normalize
        result = vector_normalize([3, 4])
        assert round(result[0], 4) == 0.6
        assert round(result[1], 4) == 0.8

    def test_zero_vector(self):
        from agentfx.fxNumeric.arithmetic_functions import vector_normalize

        with pytest.raises(ValueError):
            vector_normalize([0, 0, 0])

class TestVectorAngle:

    def test_orthogonal(self):
        from agentfx.fxNumeric.arithmetic_functions import vector_angle
        result = vector_angle([1, 0], [0, 1])
        assert round(result, 4) == round(math.pi / 2, 4)

    def test_parallel(self):
        from agentfx.fxNumeric.arithmetic_functions import vector_angle
        result = vector_angle([1, 0], [2, 0])
        assert round(result, 4) == 0.0

class TestMatrixAdd:

    def test_basic(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_add
        result = matrix_add([[1, 2], [3, 4]], [[5, 6], [7, 8]])
        assert result == [[6, 8], [10, 12]]

    def test_different_dims(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_add

        with pytest.raises(ValueError):
            matrix_add([[1, 2]], [[1, 2], [3, 4]])

class TestMatrixScalarMultiply:

    def test_basic(self):
        from agentfx.fxNumeric.arithmetic_functions import matrix_scalar_multiply
        result = matrix_scalar_multiply([[1, 2], [3, 4]], 3)
        assert result == [[3, 6], [9, 12]]


# ============================================================================
# CONVERSION CORE
# ============================================================================

class TestFactorial:

    @pytest.mark.parametrize("n, expected", [
        (0, 1),
        (1, 1),
        (5, 120),
        (10, 3628800),
    ])
    def test_factorial_valid(self, n: int, expected: int):
        assert factorial(n) == expected

    def test_factorial_negative_raises(self):

        with pytest.raises(ValueError):
            factorial(-1)

    def test_factorial_non_integer_raises(self):

        with pytest.raises(TypeError):
            factorial(3.5)

class TestGamma:

    def test_gamma_positive_integer(self):
        # Γ(5) = 4! = 24
        assert gamma(5) == pytest.approx(24.0)

    def test_gamma_half(self):
        # Γ(0.5) = √π
        assert gamma(0.5) == pytest.approx(math.sqrt(math.pi))

    def test_gamma_zero_raises(self):

        with pytest.raises(ValueError):
            gamma(0)

    def test_gamma_negative_integer_raises(self):

        with pytest.raises(ValueError):
            gamma(-3)

class TestGcd:

    @pytest.mark.parametrize("a, b, expected", [
        (12, 8, 4),
        (54, 24, 6),
        (0, 5, 5),
        (7, 7, 7),
    ])
    def test_gcd_valid(self, a: int, b: int, expected: int):
        assert greatest_common_divisor(a, b) == expected

    def test_gcd_non_integer_raises(self):

        with pytest.raises(TypeError):
            greatest_common_divisor(3.5, 2)

class TestLcm:

    @pytest.mark.parametrize("a, b, expected", [
        (4, 6, 12),
        (3, 7, 21),
        (0, 5, 0),
    ])
    def test_lcm_valid(self, a: int, b: int, expected: int):
        assert lcm(a, b) == expected

class TestGcdList:

    def test_gcd_list(self):
        assert gcd_list([12, 18, 24]) == 6

    def test_gcd_list_empty_raises(self):

        with pytest.raises(ValueError):
            gcd_list([])

class TestLcmList:

    def test_lcm_list(self):
        assert lcm_list([4, 6, 10]) == 60

    def test_lcm_list_empty_raises(self):

        with pytest.raises(ValueError):
            lcm_list([])


# ── Combinations / Permutations ──────────────────────────────────────────────

class TestCombinations:

    @pytest.mark.parametrize("n, k, expected", [
        (10, 3, 120),
        (5, 0, 1),
        (5, 5, 1),
        (6, 2, 15),
    ])
    def test_combinations_valid(self, n: int, k: int, expected: int):
        assert combinations(n, k) == expected

    def test_combinations_k_greater_than_n_raises(self):

        with pytest.raises(ValueError):
            combinations(3, 5)

class TestPermutations:

    @pytest.mark.parametrize("n, k, expected", [
        (5, 3, 60),
        (4, 4, 24),
        (5, 0, 1),
    ])
    def test_permutations_valid(self, n: int, k: int, expected: int):
        assert permutations(n, k) == expected


# ── Sign / Abs / Exp ─────────────────────────────────────────────────────────

class TestSignAbsExp:

    def test_sign_positive(self):
        assert sign(42) == 1

    def test_sign_negative(self):
        assert sign(-3.14) == -1

    def test_sign_zero(self):
        assert sign(0) == 0

    def test_absolute_value(self):
        assert absolute_value(-5.5) == 5.5
        assert absolute_value(3) == 3

    def test_exp(self):
        assert exp(0) == 1.0
        assert exp(1) == pytest.approx(math.e)

    def test_expm1(self):
        assert expm1(0) == 0.0


# ── Error functions ──────────────────────────────────────────────────────────

class TestMatrixExtensions:

    def test_lu_decomposition(self):
        L, U = lu_decomposition([[2, 1], [4, 3]])
        assert L == [[1.0, 0.0], [2.0, 1.0]]
        assert U == [[2.0, 1.0], [0.0, 1.0]]

    def test_lu_decomposition_3x3(self):
        A = [[1, 2, 3], [4, 5, 6], [7, 8, 10]]
        L, U = lu_decomposition(A)
        # Verify L * U = A
        n = 3

        for i in range(n):

            for j in range(n):
                s = sum(L[i][k] * U[k][j] for k in range(n))
                assert abs(s - A[i][j]) < 1e-10

    def test_eigenvalues_2x2_real(self):
        e1, e2 = matrix_eigenvalues_2x2([[2, 1], [1, 2]])
        assert abs(e1 - 3) < 1e-10
        assert abs(e2 - 1) < 1e-10

    def test_eigenvalues_2x2_complex(self):
        e1, e2 = matrix_eigenvalues_2x2([[0, -1], [1, 0]])
        assert isinstance(e1, complex)
        assert abs(e1.imag - 1) < 1e-10

    def test_frobenius_norm(self):
        val = matrix_frobenius_norm([[1, 2], [3, 4]])
        assert abs(val - math.sqrt(30)) < 1e-10

    def test_infinity_norm(self):
        assert matrix_infinity_norm([[1, -2], [3, 4]]) == 7

    def test_one_norm(self):
        assert matrix_one_norm([[1, -2], [3, 4]]) == 6

    def test_rank_full(self):
        assert matrix_rank([[1, 0], [0, 1]]) == 2

    def test_rank_deficient(self):
        assert matrix_rank([[1, 2], [2, 4]]) == 1

    def test_rank_3x3(self):
        assert matrix_rank([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == 2


# ===================================================================
# Curves / differential geometry extensions
# ===================================================================

class TestCholesky:

    def test_2x2(self):
        L = cholesky_decomposition([[4, 2], [2, 5]])
        assert L == [[2.0, 0.0], [1.0, 2.0]]

    def test_3x3(self):
        A = [[4, 12, -16], [12, 37, -43], [-16, -43, 98]]
        L = cholesky_decomposition(A)
        # Verify L * L^T = A
        n = 3

        for i in range(n):

            for j in range(n):
                s = sum(L[i][k] * L[j][k] for k in range(n))
                assert abs(s - A[i][j]) < 1e-10

    def test_not_positive_definite(self):
        with pytest.raises(ValueError):
            cholesky_decomposition([[-1, 0], [0, 1]])

class TestQR:

    def test_basic(self):
        Q, R = qr_decomposition([[1, 1], [0, 1], [1, 0]])
        assert len(Q) == 3
        assert len(R) == 2

    def test_orthogonality(self):
        Q, R = qr_decomposition([[1, 0], [0, 1], [1, 1]])
        # Q^T Q should be identity (2×2)
        n = len(R)

        for i in range(n):

            for j in range(n):
                dot = sum(Q[k][i] * Q[k][j] for k in range(len(Q)))

                if i == j:
                    assert abs(dot - 1.0) < 1e-10
                else:
                    assert abs(dot) < 1e-10

class TestMatrixPower:

    def test_identity(self):
        assert matrix_power([[1, 1], [0, 1]], 0) == [[1, 0], [0, 1]]

    def test_cube(self):
        result = matrix_power([[1, 1], [0, 1]], 3)
        assert result[0][1] == 3

    def test_power_2(self):
        A = [[0, 1], [-1, 0]]
        A2 = matrix_power(A, 2)
        # Should be -I
        assert abs(A2[0][0] - (-1)) < 1e-10
        assert abs(A2[1][1] - (-1)) < 1e-10

class TestAdjugate:

    def test_2x2(self):
        adj = adjugate_matrix([[1, 2], [3, 4]])
        assert adj == [[4.0, -2.0], [-3.0, 1.0]]

    def test_identity_property(self):
        # A * adj(A) = det(A) * I for 2x2
        A = [[2, 1], [5, 3]]
        adj = adjugate_matrix(A)
        det = 2 * 3 - 1 * 5  # = 1
        prod = [
            [A[0][0] * adj[0][0] + A[0][1] * adj[1][0],
             A[0][0] * adj[0][1] + A[0][1] * adj[1][1]],
            [A[1][0] * adj[0][0] + A[1][1] * adj[1][0],
             A[1][0] * adj[0][1] + A[1][1] * adj[1][1]],
        ]
        assert abs(prod[0][0] - det) < 1e-10
        assert abs(prod[1][1] - det) < 1e-10
        assert abs(prod[0][1]) < 1e-10

class TestSolveLinearSystem:

    def test_2x2(self):
        x = solve_linear_system([[2, 1], [1, 3]], [5, 10])
        assert abs(x[0] - 1.0) < 1e-10
        assert abs(x[1] - 3.0) < 1e-10

    def test_3x3(self):
        A = [[1, 1, 1], [0, 2, 5], [2, 5, -1]]
        b = [6, -4, 27]
        x = solve_linear_system(A, b)
        # Verify A*x = b
        for i in range(3):
            val = sum(A[i][j] * x[j] for j in range(3))
            assert abs(val - b[i]) < 1e-8

    def test_singular(self):
        with pytest.raises(ValueError):
            solve_linear_system([[1, 2], [2, 4]], [3, 6])


# ===================================================================
# Number theory extensions
# ===================================================================
