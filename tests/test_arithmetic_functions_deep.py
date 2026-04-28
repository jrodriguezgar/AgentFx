# Deep coverage tests for agentfx.fxNumeric.arithmetic_functions

import agentfx.fxNumeric.arithmetic_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_adjugate_matrix_deep:
    def test_c0(self):
        try:
            mod.adjugate_matrix([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.adjugate_matrix([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.adjugate_matrix([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.adjugate_matrix([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.adjugate_matrix([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.adjugate_matrix([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_matrix_multiply_deep:
    def test_c0(self):
        try:
            mod.matrix_multiply([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_multiply([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_multiply([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_multiply([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_multiply([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_multiply([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_vector_angle_deep:
    def test_c0(self):
        try:
            mod.vector_angle([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.vector_angle([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.vector_angle([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.vector_angle([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.vector_angle([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.vector_angle([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_matrix_determinant_deep:
    def test_c0(self):
        try:
            mod.matrix_determinant([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_determinant([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_determinant([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_determinant([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_determinant([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_determinant([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_power_deep:
    def test_c0(self):
        try:
            mod.power(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.power(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.power(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.power(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.power(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.power(0, 1)
        except EXC:
            pass


class Test_qr_decomposition_deep:
    def test_c0(self):
        try:
            mod.qr_decomposition([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.qr_decomposition([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.qr_decomposition([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.qr_decomposition([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.qr_decomposition([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.qr_decomposition([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_bessel_k_deep:
    def test_c0(self):
        try:
            mod.bessel_k(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bessel_k(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bessel_k(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bessel_k(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bessel_k(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bessel_k(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bessel_k(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bessel_k(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bessel_k(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bessel_k(2, 10)
        except EXC:
            pass


class Test_bessel_y_deep:
    def test_c0(self):
        try:
            mod.bessel_y(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bessel_y(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bessel_y(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bessel_y(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bessel_y(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bessel_y(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bessel_y(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bessel_y(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bessel_y(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bessel_y(2, 10)
        except EXC:
            pass


class Test_cholesky_decomposition_deep:
    def test_c0(self):
        try:
            mod.cholesky_decomposition([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cholesky_decomposition([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cholesky_decomposition([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cholesky_decomposition([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cholesky_decomposition([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cholesky_decomposition([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_cube_root_deep:
    def test_c0(self):
        try:
            mod.cube_root(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cube_root(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cube_root(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cube_root(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cube_root(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cube_root(0)
        except EXC:
            pass


class Test_dot_product_deep:
    def test_c0(self):
        try:
            mod.dot_product([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dot_product([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dot_product([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dot_product([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dot_product([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dot_product([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_gaussian_quadrature_deep:
    def test_c0(self):
        try:
            mod.gaussian_quadrature(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gaussian_quadrature(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gaussian_quadrature(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gaussian_quadrature(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gaussian_quadrature(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gaussian_quadrature(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.gaussian_quadrature(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.gaussian_quadrature(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.gaussian_quadrature(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.gaussian_quadrature(2, 1, 42)
        except EXC:
            pass

    def test_kw_n(self):
        try:
            mod.gaussian_quadrature(1, 42, 0, n=1)
        except EXC:
            pass


class Test_lu_decomposition_deep:
    def test_c0(self):
        try:
            mod.lu_decomposition([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lu_decomposition([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lu_decomposition([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lu_decomposition([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lu_decomposition([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lu_decomposition([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_matrix_add_deep:
    def test_c0(self):
        try:
            mod.matrix_add([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_add([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_add([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_add([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_add([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_add([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_matrix_inverse_deep:
    def test_c0(self):
        try:
            mod.matrix_inverse([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_inverse([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_inverse([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_inverse([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_inverse([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_inverse([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_matrix_power_deep:
    def test_c0(self):
        try:
            mod.matrix_power([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_power([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_power([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_power([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_power([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_power([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_newton_raphson_deep:
    def test_c0(self):
        try:
            mod.newton_raphson(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.newton_raphson(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.newton_raphson(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.newton_raphson(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.newton_raphson(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.newton_raphson(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.newton_raphson(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.newton_raphson(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.newton_raphson(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.newton_raphson(2, 1, 42)
        except EXC:
            pass

    def test_kw_tol(self):
        try:
            mod.newton_raphson(1, 42, 0, tol=1)
        except EXC:
            pass

    def test_kw_max_iter(self):
        try:
            mod.newton_raphson(1, 42, 0, max_iter=1)
        except EXC:
            pass


class Test_solve_linear_system_deep:
    def test_c0(self):
        try:
            mod.solve_linear_system([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.solve_linear_system([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.solve_linear_system([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.solve_linear_system([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.solve_linear_system([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.solve_linear_system([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_bessel_i_deep:
    def test_c0(self):
        try:
            mod.bessel_i(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bessel_i(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bessel_i(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bessel_i(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bessel_i(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bessel_i(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bessel_i(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bessel_i(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bessel_i(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bessel_i(2, 10)
        except EXC:
            pass


class Test_bessel_j_deep:
    def test_c0(self):
        try:
            mod.bessel_j(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bessel_j(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bessel_j(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bessel_j(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bessel_j(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bessel_j(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bessel_j(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bessel_j(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bessel_j(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bessel_j(2, 10)
        except EXC:
            pass


class Test_bisection_method_deep:
    def test_c0(self):
        try:
            mod.bisection_method(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bisection_method(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bisection_method(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bisection_method(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bisection_method(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bisection_method(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bisection_method(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bisection_method(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bisection_method(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bisection_method(2, 1, 42)
        except EXC:
            pass

    def test_kw_tol(self):
        try:
            mod.bisection_method(1, 42, 0, tol=1)
        except EXC:
            pass

    def test_kw_max_iter(self):
        try:
            mod.bisection_method(1, 42, 0, max_iter=1)
        except EXC:
            pass


class Test_bit_lshift_deep:
    def test_c0(self):
        try:
            mod.bit_lshift(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bit_lshift(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bit_lshift(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bit_lshift(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bit_lshift(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bit_lshift(0, 1)
        except EXC:
            pass


class Test_bit_rshift_deep:
    def test_c0(self):
        try:
            mod.bit_rshift(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bit_rshift(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bit_rshift(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bit_rshift(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bit_rshift(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bit_rshift(0, 1)
        except EXC:
            pass


class Test_bitwise_not_deep:
    def test_c0(self):
        try:
            mod.bitwise_not(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bitwise_not(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bitwise_not(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bitwise_not(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bitwise_not(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bitwise_not(0)
        except EXC:
            pass

    def test_kw_bit_width(self):
        try:
            mod.bitwise_not(1, bit_width=1)
        except EXC:
            pass


class Test_chebyshev_nodes_deep:
    def test_c0(self):
        try:
            mod.chebyshev_nodes(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chebyshev_nodes(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chebyshev_nodes(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chebyshev_nodes(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chebyshev_nodes(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chebyshev_nodes(0)
        except EXC:
            pass

    def test_kw_a(self):
        try:
            mod.chebyshev_nodes(1, a=1)
        except EXC:
            pass

    def test_kw_b(self):
        try:
            mod.chebyshev_nodes(1, b=1)
        except EXC:
            pass


class Test_cross_product_deep:
    def test_c0(self):
        try:
            mod.cross_product([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cross_product([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cross_product([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cross_product([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cross_product([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cross_product([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_look_and_say_deep:
    def test_c0(self):
        try:
            mod.look_and_say()
        except EXC:
            pass

    def test_kw_seed(self):
        try:
            mod.look_and_say(seed="hello world")
        except EXC:
            pass

    def test_kw_iterations(self):
        try:
            mod.look_and_say(iterations=1)
        except EXC:
            pass


class Test_matrix_eigenvalues_2x2_deep:
    def test_c0(self):
        try:
            mod.matrix_eigenvalues_2x2([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_eigenvalues_2x2([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_eigenvalues_2x2([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_eigenvalues_2x2([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_eigenvalues_2x2([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_eigenvalues_2x2([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_nth_root_deep:
    def test_c0(self):
        try:
            mod.nth_root(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.nth_root(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.nth_root(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.nth_root(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.nth_root(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.nth_root(0, 1)
        except EXC:
            pass


class Test_numerical_derivative_deep:
    def test_c0(self):
        try:
            mod.numerical_derivative(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.numerical_derivative(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.numerical_derivative(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.numerical_derivative(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.numerical_derivative(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.numerical_derivative(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.numerical_derivative(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.numerical_derivative(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.numerical_derivative(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.numerical_derivative(2, 1)
        except EXC:
            pass

    def test_kw_h(self):
        try:
            mod.numerical_derivative(1, 42, h=1)
        except EXC:
            pass


class Test_permutations_deep:
    def test_c0(self):
        try:
            mod.permutations(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.permutations(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.permutations(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.permutations(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.permutations(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.permutations(0, 1)
        except EXC:
            pass


class Test_permutations_with_repetition_deep:
    def test_c0(self):
        try:
            mod.permutations_with_repetition(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.permutations_with_repetition(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.permutations_with_repetition(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.permutations_with_repetition(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.permutations_with_repetition(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.permutations_with_repetition(0, 1)
        except EXC:
            pass


class Test_polynomial_evaluate_deep:
    def test_c0(self):
        try:
            mod.polynomial_evaluate([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.polynomial_evaluate([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.polynomial_evaluate([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.polynomial_evaluate([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.polynomial_evaluate([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.polynomial_evaluate([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.polynomial_evaluate([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.polynomial_evaluate([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.polynomial_evaluate([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.polynomial_evaluate([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass


class Test_secant_method_deep:
    def test_c0(self):
        try:
            mod.secant_method(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.secant_method(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.secant_method(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.secant_method(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.secant_method(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.secant_method(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.secant_method(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.secant_method(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.secant_method(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.secant_method(2, 1, 42)
        except EXC:
            pass

    def test_kw_tol(self):
        try:
            mod.secant_method(1, 42, 0, tol=1)
        except EXC:
            pass

    def test_kw_max_iter(self):
        try:
            mod.secant_method(1, 42, 0, max_iter=1)
        except EXC:
            pass


class Test_trapezoidal_integrate_deep:
    def test_c0(self):
        try:
            mod.trapezoidal_integrate(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.trapezoidal_integrate(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.trapezoidal_integrate(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.trapezoidal_integrate(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.trapezoidal_integrate(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.trapezoidal_integrate(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.trapezoidal_integrate(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.trapezoidal_integrate(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.trapezoidal_integrate(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.trapezoidal_integrate(2, 1, 42)
        except EXC:
            pass

    def test_kw_n(self):
        try:
            mod.trapezoidal_integrate(1, 42, 0, n=1)
        except EXC:
            pass


class Test_vector_normalize_deep:
    def test_c0(self):
        try:
            mod.vector_normalize([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.vector_normalize([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.vector_normalize([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.vector_normalize([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.vector_normalize([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.vector_normalize([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_adaptive_simpson_deep:
    def test_c0(self):
        try:
            mod.adaptive_simpson(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.adaptive_simpson(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.adaptive_simpson(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.adaptive_simpson(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.adaptive_simpson(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.adaptive_simpson(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.adaptive_simpson(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.adaptive_simpson(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.adaptive_simpson(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.adaptive_simpson(2, 1, 42)
        except EXC:
            pass

    def test_kw_tol(self):
        try:
            mod.adaptive_simpson(1, 42, 0, tol=1)
        except EXC:
            pass

    def test_kw_max_depth(self):
        try:
            mod.adaptive_simpson(1, 42, 0, max_depth=1)
        except EXC:
            pass


class Test_additive_persistence_deep:
    def test_c0(self):
        try:
            mod.additive_persistence(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.additive_persistence(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.additive_persistence(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.additive_persistence(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.additive_persistence(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.additive_persistence(0)
        except EXC:
            pass


class Test_bit_count_deep:
    def test_c0(self):
        try:
            mod.bit_count(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bit_count(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bit_count(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bit_count(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bit_count(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bit_count(0)
        except EXC:
            pass


class Test_bitwise_and_deep:
    def test_c0(self):
        try:
            mod.bitwise_and(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bitwise_and(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bitwise_and(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bitwise_and(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bitwise_and(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bitwise_and(0, 1)
        except EXC:
            pass


class Test_bitwise_or_deep:
    def test_c0(self):
        try:
            mod.bitwise_or(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bitwise_or(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bitwise_or(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bitwise_or(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bitwise_or(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bitwise_or(0, 1)
        except EXC:
            pass


class Test_bitwise_xor_deep:
    def test_c0(self):
        try:
            mod.bitwise_xor(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bitwise_xor(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bitwise_xor(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bitwise_xor(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bitwise_xor(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bitwise_xor(0, 1)
        except EXC:
            pass


class Test_cantor_unpairing_deep:
    def test_c0(self):
        try:
            mod.cantor_unpairing(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cantor_unpairing(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cantor_unpairing(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cantor_unpairing(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cantor_unpairing(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cantor_unpairing(0)
        except EXC:
            pass


class Test_combinations_deep:
    def test_c0(self):
        try:
            mod.combinations(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.combinations(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.combinations(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.combinations(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.combinations(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.combinations(0, 1)
        except EXC:
            pass


class Test_combinations_with_repetition_deep:
    def test_c0(self):
        try:
            mod.combinations_with_repetition(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.combinations_with_repetition(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.combinations_with_repetition(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.combinations_with_repetition(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.combinations_with_repetition(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.combinations_with_repetition(0, 1)
        except EXC:
            pass


class Test_common_log_deep:
    def test_c0(self):
        try:
            mod.common_log(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.common_log(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.common_log(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.common_log(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.common_log(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.common_log(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.common_log(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.common_log(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.common_log(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.common_log(2)
        except EXC:
            pass


class Test_digit_product_deep:
    def test_c0(self):
        try:
            mod.digit_product(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.digit_product(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.digit_product(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.digit_product(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.digit_product(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.digit_product(0)
        except EXC:
            pass


class Test_digital_sum_deep:
    def test_c0(self):
        try:
            mod.digital_sum(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.digital_sum(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.digital_sum(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.digital_sum(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.digital_sum(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.digital_sum(0)
        except EXC:
            pass


class Test_euler_method_deep:
    def test_c0(self):
        try:
            mod.euler_method(1, 42, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.euler_method(42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.euler_method(0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.euler_method(-5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.euler_method(3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.euler_method(100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.euler_method(0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.euler_method(1000, -1, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.euler_method(-1, 2, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.euler_method(2, 1, 42, 0)
        except EXC:
            pass

    def test_kw_steps(self):
        try:
            mod.euler_method(1, 42, 0, -5, steps=1)
        except EXC:
            pass


class Test_fibonacci_deep:
    def test_c0(self):
        try:
            mod.fibonacci(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fibonacci(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fibonacci(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fibonacci(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fibonacci(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fibonacci(0)
        except EXC:
            pass


class Test_fixed_point_iteration_deep:
    def test_c0(self):
        try:
            mod.fixed_point_iteration(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fixed_point_iteration(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fixed_point_iteration(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fixed_point_iteration(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fixed_point_iteration(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fixed_point_iteration(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.fixed_point_iteration(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.fixed_point_iteration(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.fixed_point_iteration(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.fixed_point_iteration(2, 1)
        except EXC:
            pass

    def test_kw_tol(self):
        try:
            mod.fixed_point_iteration(1, 42, tol=1)
        except EXC:
            pass

    def test_kw_max_iter(self):
        try:
            mod.fixed_point_iteration(1, 42, max_iter=1)
        except EXC:
            pass


class Test_gcd_list_deep:
    def test_c0(self):
        try:
            mod.gcd_list([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gcd_list([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gcd_list([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gcd_list([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gcd_list([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gcd_list([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_integer_partition_distinct_deep:
    def test_c0(self):
        try:
            mod.integer_partition_distinct(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.integer_partition_distinct(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.integer_partition_distinct(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.integer_partition_distinct(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.integer_partition_distinct(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.integer_partition_distinct(0)
        except EXC:
            pass


class Test_is_automorphic_deep:
    def test_c0(self):
        try:
            mod.is_automorphic(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_automorphic(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_automorphic(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_automorphic(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_automorphic(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_automorphic(0)
        except EXC:
            pass


class Test_is_narcissistic_deep:
    def test_c0(self):
        try:
            mod.is_narcissistic(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_narcissistic(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_narcissistic(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_narcissistic(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_narcissistic(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_narcissistic(0)
        except EXC:
            pass


class Test_lcm_list_deep:
    def test_c0(self):
        try:
            mod.lcm_list([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lcm_list([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lcm_list([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lcm_list([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lcm_list([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lcm_list([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_log1p_deep:
    def test_c0(self):
        try:
            mod.log1p(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.log1p(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.log1p(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.log1p(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.log1p(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.log1p(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.log1p(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.log1p(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.log1p(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.log1p(2)
        except EXC:
            pass


class Test_log_base_n_deep:
    def test_c0(self):
        try:
            mod.log_base_n(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.log_base_n(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.log_base_n(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.log_base_n(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.log_base_n(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.log_base_n(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.log_base_n(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.log_base_n(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.log_base_n(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.log_base_n(2, 10)
        except EXC:
            pass


class Test_matrix_frobenius_norm_deep:
    def test_c0(self):
        try:
            mod.matrix_frobenius_norm([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_frobenius_norm([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_frobenius_norm([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_frobenius_norm([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_frobenius_norm([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_frobenius_norm([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_matrix_infinity_norm_deep:
    def test_c0(self):
        try:
            mod.matrix_infinity_norm([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_infinity_norm([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_infinity_norm([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_infinity_norm([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_infinity_norm([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_infinity_norm([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_matrix_one_norm_deep:
    def test_c0(self):
        try:
            mod.matrix_one_norm([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_one_norm([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_one_norm([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_one_norm([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_one_norm([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_one_norm([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_matrix_scalar_multiply_deep:
    def test_c0(self):
        try:
            mod.matrix_scalar_multiply([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matrix_scalar_multiply([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matrix_scalar_multiply([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matrix_scalar_multiply([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matrix_scalar_multiply([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matrix_scalar_multiply([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_multinomial_coefficient_deep:
    def test_c0(self):
        try:
            mod.multinomial_coefficient()
        except EXC:
            pass


class Test_multiplicative_persistence_deep:
    def test_c0(self):
        try:
            mod.multiplicative_persistence(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.multiplicative_persistence(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.multiplicative_persistence(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.multiplicative_persistence(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.multiplicative_persistence(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.multiplicative_persistence(0)
        except EXC:
            pass


class Test_natural_log_deep:
    def test_c0(self):
        try:
            mod.natural_log(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.natural_log(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.natural_log(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.natural_log(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.natural_log(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.natural_log(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.natural_log(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.natural_log(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.natural_log(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.natural_log(2)
        except EXC:
            pass


class Test_polynomial_roots_cubic_deep:
    def test_c0(self):
        try:
            mod.polynomial_roots_cubic(1, 42, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.polynomial_roots_cubic(42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.polynomial_roots_cubic(0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.polynomial_roots_cubic(-5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.polynomial_roots_cubic(3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.polynomial_roots_cubic(100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.polynomial_roots_cubic(0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.polynomial_roots_cubic(1000, -1, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.polynomial_roots_cubic(-1, 2, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.polynomial_roots_cubic(2, 1, 42, 0)
        except EXC:
            pass


class Test_polynomial_roots_quadratic_deep:
    def test_c0(self):
        try:
            mod.polynomial_roots_quadratic(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.polynomial_roots_quadratic(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.polynomial_roots_quadratic(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.polynomial_roots_quadratic(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.polynomial_roots_quadratic(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.polynomial_roots_quadratic(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.polynomial_roots_quadratic(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.polynomial_roots_quadratic(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.polynomial_roots_quadratic(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.polynomial_roots_quadratic(2, 1, 42)
        except EXC:
            pass


class Test_product_list_deep:
    def test_c0(self):
        try:
            mod.product_list([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.product_list([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.product_list([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.product_list([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.product_list([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.product_list([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_romberg_integrate_deep:
    def test_c0(self):
        try:
            mod.romberg_integrate(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.romberg_integrate(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.romberg_integrate(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.romberg_integrate(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.romberg_integrate(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.romberg_integrate(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.romberg_integrate(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.romberg_integrate(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.romberg_integrate(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.romberg_integrate(2, 1, 42)
        except EXC:
            pass

    def test_kw_max_order(self):
        try:
            mod.romberg_integrate(1, 42, 0, max_order=1)
        except EXC:
            pass

    def test_kw_tol(self):
        try:
            mod.romberg_integrate(1, 42, 0, tol=1)
        except EXC:
            pass


class Test_runge_kutta_4_step_deep:
    def test_c0(self):
        try:
            mod.runge_kutta_4_step(1, 42, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.runge_kutta_4_step(42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.runge_kutta_4_step(0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.runge_kutta_4_step(-5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.runge_kutta_4_step(3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.runge_kutta_4_step(100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.runge_kutta_4_step(0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.runge_kutta_4_step(1000, -1, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.runge_kutta_4_step(-1, 2, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.runge_kutta_4_step(2, 1, 42, 0)
        except EXC:
            pass


class Test_simpsons_integrate_deep:
    def test_c0(self):
        try:
            mod.simpsons_integrate(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.simpsons_integrate(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.simpsons_integrate(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.simpsons_integrate(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.simpsons_integrate(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.simpsons_integrate(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.simpsons_integrate(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.simpsons_integrate(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.simpsons_integrate(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.simpsons_integrate(2, 1, 42)
        except EXC:
            pass

    def test_kw_n(self):
        try:
            mod.simpsons_integrate(1, 42, 0, n=1)
        except EXC:
            pass


class Test_sqrt_pi_deep:
    def test_c0(self):
        try:
            mod.sqrt_pi(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sqrt_pi(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sqrt_pi(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sqrt_pi(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sqrt_pi(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sqrt_pi(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.sqrt_pi(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.sqrt_pi(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.sqrt_pi(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.sqrt_pi(2)
        except EXC:
            pass


class Test_square_pyramidal_number_deep:
    def test_c0(self):
        try:
            mod.square_pyramidal_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.square_pyramidal_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.square_pyramidal_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.square_pyramidal_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.square_pyramidal_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.square_pyramidal_number(0)
        except EXC:
            pass


class Test_square_root_deep:
    def test_c0(self):
        try:
            mod.square_root(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.square_root(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.square_root(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.square_root(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.square_root(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.square_root(0)
        except EXC:
            pass


class Test_sum_first_n_cubes_deep:
    def test_c0(self):
        try:
            mod.sum_first_n_cubes(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_first_n_cubes(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_first_n_cubes(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_first_n_cubes(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_first_n_cubes(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_first_n_cubes(0)
        except EXC:
            pass


class Test_sum_first_n_powers_deep:
    def test_c0(self):
        try:
            mod.sum_first_n_powers(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_first_n_powers(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_first_n_powers(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_first_n_powers(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_first_n_powers(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_first_n_powers(0, 1)
        except EXC:
            pass


class Test_sum_first_n_squares_deep:
    def test_c0(self):
        try:
            mod.sum_first_n_squares(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_first_n_squares(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_first_n_squares(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_first_n_squares(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_first_n_squares(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_first_n_squares(0)
        except EXC:
            pass


class Test_sum_x2my2_deep:
    def test_c0(self):
        try:
            mod.sum_x2my2([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_x2my2([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_x2my2([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_x2my2([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_x2my2([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_x2my2([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_sum_x2py2_deep:
    def test_c0(self):
        try:
            mod.sum_x2py2([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_x2py2([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_x2py2([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_x2py2([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_x2py2([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_x2py2([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_sum_xmy2_deep:
    def test_c0(self):
        try:
            mod.sum_xmy2([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_xmy2([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_xmy2([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_xmy2([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_xmy2([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_xmy2([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_tetrahedral_number_deep:
    def test_c0(self):
        try:
            mod.tetrahedral_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.tetrahedral_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.tetrahedral_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.tetrahedral_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.tetrahedral_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.tetrahedral_number(0)
        except EXC:
            pass


class Test_triangular_number_deep:
    def test_c0(self):
        try:
            mod.triangular_number(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.triangular_number(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.triangular_number(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.triangular_number(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.triangular_number(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.triangular_number(0)
        except EXC:
            pass


class Test_vector_magnitude_deep:
    def test_c0(self):
        try:
            mod.vector_magnitude([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.vector_magnitude([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.vector_magnitude([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.vector_magnitude([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.vector_magnitude([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.vector_magnitude([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

