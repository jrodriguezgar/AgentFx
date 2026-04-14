"""Numerical methods: integration, differentiation, root-finding, and ODE solvers.

Classical numerical algorithms from Murray R. Spiegel's *Mathematical Handbook
of Formulas and Tables*: quadrature rules, finite-difference differentiation,
root-finding iterations, and ordinary differential equation solvers.
"""

from typing import Callable, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_callable(f: object, name: str = "f") -> None:
    if not callable(f):
        raise TypeError(f"{name} must be callable.")


def _check_numeric(value: object, name: str = "value") -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric.")


def _check_positive(value: float, name: str = "value") -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive.")


def _check_positive_int(value: int, name: str = "n") -> None:
    if not isinstance(value, int) or value < 1:
        raise TypeError(f"{name} must be a positive integer.")


# ---------------------------------------------------------------------------
# Numerical integration (quadrature)
# ---------------------------------------------------------------------------


def trapezoidal_rule(
    f: Callable[[float], float], a: float, b: float, n: int = 1000
) -> float:
    """Approximates the definite integral of f from a to b using the trapezoidal rule.

    Args:
        f: Integrand function of one variable.
        a: Lower limit of integration.
        b: Upper limit of integration.
        n: Number of subintervals (default 1000).

    Returns:
        Approximate value of the integral.

    Raises:
        TypeError: If f is not callable or a, b are not numeric.
        ValueError: If n < 1.

    Example:
        >>> round(trapezoidal_rule(math.sin, 0, math.pi, 10000), 6)
        2.0

    Complexity: O(n)
    """
    _check_callable(f)
    _check_numeric(a, "a")
    _check_numeric(b, "b")
    _check_positive_int(n, "n")

    h = (b - a) / n
    total = 0.5 * (f(a) + f(b))

    for i in range(1, n):
        total += f(a + i * h)

    return total * h


def simpsons_rule(
    f: Callable[[float], float], a: float, b: float, n: int = 1000
) -> float:
    """Approximates the definite integral of f from a to b using Simpson's 1/3 rule.

    Args:
        f: Integrand function of one variable.
        a: Lower limit of integration.
        b: Upper limit of integration.
        n: Number of subintervals (must be even, default 1000).

    Returns:
        Approximate value of the integral.

    Raises:
        TypeError: If f is not callable or a, b are not numeric.
        ValueError: If n < 2 or n is odd.

    Example:
        >>> round(simpsons_rule(math.sin, 0, math.pi, 100), 10)
        2.0

    Complexity: O(n)
    """
    _check_callable(f)
    _check_numeric(a, "a")
    _check_numeric(b, "b")

    if not isinstance(n, int) or n < 2:
        raise ValueError("n must be an integer >= 2.")

    if n % 2 != 0:
        raise ValueError("n must be even for Simpson's 1/3 rule.")

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n, 2):
        total += 4.0 * f(a + i * h)

    for i in range(2, n, 2):
        total += 2.0 * f(a + i * h)

    return total * h / 3.0


def simpsons_38_rule(
    f: Callable[[float], float], a: float, b: float, n: int = 999
) -> float:
    """Approximates the definite integral of f from a to b using Simpson's 3/8 rule.

    Args:
        f: Integrand function of one variable.
        a: Lower limit of integration.
        b: Upper limit of integration.
        n: Number of subintervals (must be divisible by 3, default 999).

    Returns:
        Approximate value of the integral.

    Raises:
        TypeError: If f is not callable.
        ValueError: If n < 3 or n is not divisible by 3.

    Example:
        >>> round(simpsons_38_rule(math.sin, 0, math.pi, 999), 6)
        2.0

    Complexity: O(n)
    """
    _check_callable(f)
    _check_numeric(a, "a")
    _check_numeric(b, "b")

    if not isinstance(n, int) or n < 3:
        raise ValueError("n must be an integer >= 3.")

    if n % 3 != 0:
        raise ValueError("n must be divisible by 3 for Simpson's 3/8 rule.")

    h = (b - a) / n
    total = f(a) + f(b)

    for i in range(1, n):

        if i % 3 == 0:
            total += 2.0 * f(a + i * h)
        else:
            total += 3.0 * f(a + i * h)

    return total * 3.0 * h / 8.0


def midpoint_rule(
    f: Callable[[float], float], a: float, b: float, n: int = 1000
) -> float:
    """Approximates the definite integral of f from a to b using the midpoint rule.

    Args:
        f: Integrand function of one variable.
        a: Lower limit of integration.
        b: Upper limit of integration.
        n: Number of subintervals (default 1000).

    Returns:
        Approximate value of the integral.

    Raises:
        TypeError: If f is not callable.
        ValueError: If n < 1.

    Example:
        >>> round(midpoint_rule(math.sin, 0, math.pi, 10000), 6)
        2.0

    Complexity: O(n)
    """
    _check_callable(f)
    _check_numeric(a, "a")
    _check_numeric(b, "b")
    _check_positive_int(n, "n")

    h = (b - a) / n
    total = 0.0

    for i in range(n):
        total += f(a + (i + 0.5) * h)

    return total * h


def gaussian_quadrature(
    f: Callable[[float], float], a: float, b: float, n: int = 5
) -> float:
    """Approximates the definite integral of f from a to b using Gauss-Legendre quadrature.

    Args:
        f: Integrand function of one variable.
        a: Lower limit of integration.
        b: Upper limit of integration.
        n: Number of quadrature points (2, 3, 4, or 5; default 5).

    Returns:
        Approximate value of the integral.

    Raises:
        TypeError: If f is not callable.
        ValueError: If n not in {2, 3, 4, 5}.

    Example:
        >>> round(gaussian_quadrature(math.sin, 0, math.pi, 5), 10)
        2.0

    Complexity: O(n)
    """
    _check_callable(f)
    _check_numeric(a, "a")
    _check_numeric(b, "b")

    nodes_weights = {
        2: (
            [-0.5773502691896257, 0.5773502691896257],
            [1.0, 1.0],
        ),
        3: (
            [-0.7745966692414834, 0.0, 0.7745966692414834],
            [0.5555555555555556, 0.8888888888888888, 0.5555555555555556],
        ),
        4: (
            [-0.8611363115940526, -0.3399810435848563,
             0.3399810435848563, 0.8611363115940526],
            [0.3478548451374538, 0.6521451548625461,
             0.6521451548625461, 0.3478548451374538],
        ),
        5: (
            [-0.9061798459386640, -0.5384693101056831, 0.0,
             0.5384693101056831, 0.9061798459386640],
            [0.2369268850561891, 0.4786286704993665, 0.5688888888888889,
             0.4786286704993665, 0.2369268850561891],
        ),
    }

    if n not in nodes_weights:
        raise ValueError("n must be 2, 3, 4, or 5.")

    nodes, weights = nodes_weights[n]
    mid = 0.5 * (b + a)
    half = 0.5 * (b - a)
    total = 0.0

    for xi, wi in zip(nodes, weights):
        total += wi * f(mid + half * xi)

    return total * half


def romberg_integration(
    f: Callable[[float], float], a: float, b: float, max_order: int = 10,
    tol: float = 1e-12
) -> float:
    """Approximates the definite integral of f from a to b using Romberg's method.

    Iteratively refines trapezoidal estimates via Richardson extrapolation.

    Args:
        f: Integrand function of one variable.
        a: Lower limit of integration.
        b: Upper limit of integration.
        max_order: Maximum number of refinement levels (default 10).
        tol: Convergence tolerance (default 1e-12).

    Returns:
        Approximate value of the integral.

    Raises:
        TypeError: If f is not callable.

    Example:
        >>> round(romberg_integration(math.sin, 0, math.pi), 10)
        2.0

    Complexity: O(2^max_order)
    """
    _check_callable(f)
    _check_numeric(a, "a")
    _check_numeric(b, "b")

    R = [[0.0] * (max_order + 1) for _ in range(max_order + 1)]
    R[0][0] = 0.5 * (b - a) * (f(a) + f(b))

    for i in range(1, max_order + 1):
        n = 2 ** i
        h = (b - a) / n
        s = sum(f(a + (2 * k - 1) * h) for k in range(1, n // 2 + 1))
        R[i][0] = 0.5 * R[i - 1][0] + h * s

        for j in range(1, i + 1):
            factor = 4 ** j
            R[i][j] = (factor * R[i][j - 1] - R[i - 1][j - 1]) / (factor - 1)

        if i > 1 and abs(R[i][i] - R[i - 1][i - 1]) < tol:
            return R[i][i]

    return R[max_order][max_order]


def monte_carlo_integration(
    f: Callable[[float], float], a: float, b: float, n: int = 100000,
    seed: Optional[int] = None
) -> float:
    """Approximates the definite integral of f from a to b via Monte Carlo sampling.

    Args:
        f: Integrand function of one variable.
        a: Lower limit of integration.
        b: Upper limit of integration.
        n: Number of random samples (default 100000).
        seed: Optional random seed for reproducibility.

    Returns:
        Approximate value of the integral.

    Raises:
        TypeError: If f is not callable.

    Example:
        >>> import random; random.seed(42)
        >>> abs(monte_carlo_integration(math.sin, 0, math.pi, 100000, seed=42) - 2.0) < 0.05
        True

    Complexity: O(n)
    """
    _check_callable(f)
    _check_numeric(a, "a")
    _check_numeric(b, "b")
    _check_positive_int(n, "n")

    import random as _random

    rng = _random.Random(seed)
    total = sum(f(rng.uniform(a, b)) for _ in range(n))
    return (b - a) * total / n


# ---------------------------------------------------------------------------
# Numerical differentiation
# ---------------------------------------------------------------------------


def forward_difference(
    f: Callable[[float], float], x: float, h: float = 1e-7
) -> float:
    """Approximates f'(x) using the forward difference formula.

    Args:
        f: Function to differentiate.
        x: Point of evaluation.
        h: Step size (default 1e-7).

    Returns:
        Approximate value of f'(x).

    Example:
        >>> round(forward_difference(math.sin, 0), 6)
        1.0

    Complexity: O(1)
    """
    _check_callable(f)
    _check_numeric(x, "x")
    return (f(x + h) - f(x)) / h


def backward_difference(
    f: Callable[[float], float], x: float, h: float = 1e-7
) -> float:
    """Approximates f'(x) using the backward difference formula.

    Args:
        f: Function to differentiate.
        x: Point of evaluation.
        h: Step size (default 1e-7).

    Returns:
        Approximate value of f'(x).

    Example:
        >>> round(backward_difference(math.sin, 0), 6)
        1.0

    Complexity: O(1)
    """
    _check_callable(f)
    _check_numeric(x, "x")
    return (f(x) - f(x - h)) / h


def central_difference(
    f: Callable[[float], float], x: float, h: float = 1e-7
) -> float:
    """Approximates f'(x) using the central difference formula.

    More accurate than forward/backward difference (error O(h^2) vs O(h)).

    Args:
        f: Function to differentiate.
        x: Point of evaluation.
        h: Step size (default 1e-7).

    Returns:
        Approximate value of f'(x).

    Example:
        >>> round(central_difference(math.sin, 0), 10)
        1.0

    Complexity: O(1)
    """
    _check_callable(f)
    _check_numeric(x, "x")
    return (f(x + h) - f(x - h)) / (2.0 * h)


def second_derivative_central(
    f: Callable[[float], float], x: float, h: float = 1e-5
) -> float:
    """Approximates f''(x) using the central difference formula for second derivatives.

    Args:
        f: Function to differentiate.
        x: Point of evaluation.
        h: Step size (default 1e-5).

    Returns:
        Approximate value of f''(x).

    Example:
        >>> round(second_derivative_central(math.sin, 0), 4)
        0.0

    Complexity: O(1)
    """
    _check_callable(f)
    _check_numeric(x, "x")
    return (f(x + h) - 2.0 * f(x) + f(x - h)) / (h * h)


def richardson_extrapolation(
    f: Callable[[float], float], x: float, h: float = 0.1, order: int = 4
) -> float:
    """Approximates f'(x) using Richardson extrapolation on central differences.

    Iteratively improves the derivative estimate by eliminating error terms.

    Args:
        f: Function to differentiate.
        x: Point of evaluation.
        h: Initial step size (default 0.1).
        order: Number of extrapolation levels (default 4).

    Returns:
        Approximate value of f'(x).

    Example:
        >>> round(richardson_extrapolation(math.sin, 0, 0.1, 4), 12)
        1.0

    Complexity: O(order^2)
    """
    _check_callable(f)
    _check_numeric(x, "x")
    _check_positive_int(order, "order")

    D = [[0.0] * order for _ in range(order)]
    D[0][0] = (f(x + h) - f(x - h)) / (2.0 * h)

    for i in range(1, order):
        h_i = h / (2 ** i)
        D[i][0] = (f(x + h_i) - f(x - h_i)) / (2.0 * h_i)

        for j in range(1, i + 1):
            factor = 4 ** j
            D[i][j] = (factor * D[i][j - 1] - D[i - 1][j - 1]) / (factor - 1)

    return D[order - 1][order - 1]


# ---------------------------------------------------------------------------
# Root-finding methods
# ---------------------------------------------------------------------------


def bisection_method(
    f: Callable[[float], float], a: float, b: float,
    tol: float = 1e-12, max_iter: int = 1000
) -> float:
    """Finds a root of f in [a, b] using the bisection method.

    Requires f(a) and f(b) to have opposite signs.

    Args:
        f: Continuous function of one variable.
        a: Left endpoint of the interval.
        b: Right endpoint of the interval.
        tol: Convergence tolerance (default 1e-12).
        max_iter: Maximum number of iterations (default 1000).

    Returns:
        Approximate root x such that f(x) ≈ 0.

    Raises:
        ValueError: If f(a) and f(b) have the same sign.

    Example:
        >>> round(bisection_method(lambda x: x**2 - 2, 1, 2), 8)
        1.41421356

    Complexity: O(log((b - a) / tol))
    """
    _check_callable(f)
    fa, fb = f(a), f(b)

    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    for _ in range(max_iter):
        c = 0.5 * (a + b)
        fc = f(c)

        if abs(fc) < tol or (b - a) * 0.5 < tol:
            return c

        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc

    return 0.5 * (a + b)


def newton_raphson(
    f: Callable[[float], float], df: Callable[[float], float], x0: float,
    tol: float = 1e-12, max_iter: int = 1000
) -> float:
    """Finds a root of f using Newton-Raphson iteration.

    Args:
        f: Function whose root is sought.
        df: Derivative of f.
        x0: Initial guess.
        tol: Convergence tolerance (default 1e-12).
        max_iter: Maximum number of iterations (default 1000).

    Returns:
        Approximate root x such that f(x) ≈ 0.

    Raises:
        ValueError: If derivative is zero during iteration.
        RuntimeError: If convergence is not achieved.

    Example:
        >>> round(newton_raphson(lambda x: x**2 - 2, lambda x: 2*x, 1.0), 10)
        1.4142135624

    Complexity: O(max_iter) per call, quadratic convergence.
    """
    _check_callable(f, "f")
    _check_callable(df, "df")
    _check_numeric(x0, "x0")

    x = float(x0)

    for _ in range(max_iter):
        fx = f(x)
        dfx = df(x)

        if abs(dfx) < 1e-15:
            raise ValueError("Derivative is zero; Newton-Raphson cannot continue.")

        x_new = x - fx / dfx

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    raise RuntimeError(f"Newton-Raphson did not converge in {max_iter} iterations.")


def secant_method(
    f: Callable[[float], float], x0: float, x1: float,
    tol: float = 1e-12, max_iter: int = 1000
) -> float:
    """Finds a root of f using the secant method.

    Args:
        f: Function whose root is sought.
        x0: First initial approximation.
        x1: Second initial approximation.
        tol: Convergence tolerance (default 1e-12).
        max_iter: Maximum number of iterations (default 1000).

    Returns:
        Approximate root x such that f(x) ≈ 0.

    Raises:
        RuntimeError: If convergence is not achieved.

    Example:
        >>> round(secant_method(lambda x: x**2 - 2, 1.0, 2.0), 10)
        1.4142135624

    Complexity: O(max_iter), superlinear convergence.
    """
    _check_callable(f)
    _check_numeric(x0, "x0")
    _check_numeric(x1, "x1")

    f0 = f(x0)
    f1 = f(x1)

    for _ in range(max_iter):
        denom = f1 - f0

        if abs(denom) < 1e-15:
            return x1

        x2 = x1 - f1 * (x1 - x0) / denom

        if abs(x2 - x1) < tol:
            return x2

        x0, f0 = x1, f1
        x1, f1 = x2, f(x2)

    raise RuntimeError(f"Secant method did not converge in {max_iter} iterations.")


def regula_falsi(
    f: Callable[[float], float], a: float, b: float,
    tol: float = 1e-12, max_iter: int = 1000
) -> float:
    """Finds a root of f in [a, b] using the false position (regula falsi) method.

    Args:
        f: Continuous function of one variable.
        a: Left endpoint where f(a) and f(b) have opposite signs.
        b: Right endpoint.
        tol: Convergence tolerance (default 1e-12).
        max_iter: Maximum number of iterations (default 1000).

    Returns:
        Approximate root x such that f(x) ≈ 0.

    Raises:
        ValueError: If f(a) and f(b) have the same sign.

    Example:
        >>> round(regula_falsi(lambda x: x**2 - 2, 1, 2), 8)
        1.41421356

    Complexity: O(max_iter), linear convergence.
    """
    _check_callable(f)
    fa, fb = f(a), f(b)

    if fa * fb > 0:
        raise ValueError("f(a) and f(b) must have opposite signs.")

    for _ in range(max_iter):
        c = (a * fb - b * fa) / (fb - fa)
        fc = f(c)

        if abs(fc) < tol:
            return c

        if fa * fc < 0:
            b, fb = c, fc
        else:
            a, fa = c, fc

    return (a * fb - b * fa) / (fb - fa)


def fixed_point_iteration(
    g: Callable[[float], float], x0: float,
    tol: float = 1e-12, max_iter: int = 1000
) -> float:
    """Finds a fixed point x = g(x) via simple iteration.

    Args:
        g: Iteration function; the fixed point satisfies x = g(x).
        x0: Initial guess.
        tol: Convergence tolerance (default 1e-12).
        max_iter: Maximum number of iterations (default 1000).

    Returns:
        Approximate fixed point x.

    Raises:
        RuntimeError: If convergence is not achieved.

    Example:
        >>> round(fixed_point_iteration(lambda x: math.cos(x), 1.0), 6)
        0.739085

    Complexity: O(max_iter), linear convergence when |g'(x*)| < 1.
    """
    _check_callable(g, "g")
    _check_numeric(x0, "x0")

    x = float(x0)

    for _ in range(max_iter):
        x_new = g(x)

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    raise RuntimeError(
        f"Fixed point iteration did not converge in {max_iter} iterations."
    )


# ---------------------------------------------------------------------------
# ODE solvers
# ---------------------------------------------------------------------------


def euler_method(
    f: Callable[[float, float], float], y0: float,
    t_start: float, t_end: float, n: int = 1000
) -> List[Tuple[float, float]]:
    """Solves the ODE y' = f(t, y) using Euler's forward method.

    Args:
        f: Right-hand side function f(t, y).
        y0: Initial condition y(t_start) = y0.
        t_start: Start of the interval.
        t_end: End of the interval.
        n: Number of steps (default 1000).

    Returns:
        List of (t, y) pairs at each step.

    Example:
        >>> result = euler_method(lambda t, y: y, 1.0, 0, 1, 1000)
        >>> abs(result[-1][1] - math.e) < 0.01
        True

    Complexity: O(n)
    """
    _check_callable(f, "f")
    _check_positive_int(n, "n")

    h = (t_end - t_start) / n
    t = float(t_start)
    y = float(y0)
    result = [(t, y)]

    for _ in range(n):
        y = y + h * f(t, y)
        t = t + h
        result.append((t, y))

    return result


def runge_kutta_2(
    f: Callable[[float, float], float], y0: float,
    t_start: float, t_end: float, n: int = 1000
) -> List[Tuple[float, float]]:
    """Solves the ODE y' = f(t, y) using the 2nd-order Runge-Kutta (midpoint) method.

    Args:
        f: Right-hand side function f(t, y).
        y0: Initial condition y(t_start) = y0.
        t_start: Start of the interval.
        t_end: End of the interval.
        n: Number of steps (default 1000).

    Returns:
        List of (t, y) pairs at each step.

    Example:
        >>> result = runge_kutta_2(lambda t, y: y, 1.0, 0, 1, 1000)
        >>> abs(result[-1][1] - math.e) < 0.001
        True

    Complexity: O(n)
    """
    _check_callable(f, "f")
    _check_positive_int(n, "n")

    h = (t_end - t_start) / n
    t = float(t_start)
    y = float(y0)
    result = [(t, y)]

    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        y = y + k2
        t = t + h
        result.append((t, y))

    return result


def runge_kutta_4(
    f: Callable[[float, float], float], y0: float,
    t_start: float, t_end: float, n: int = 1000
) -> List[Tuple[float, float]]:
    """Solves the ODE y' = f(t, y) using the classic 4th-order Runge-Kutta method.

    Args:
        f: Right-hand side function f(t, y).
        y0: Initial condition y(t_start) = y0.
        t_start: Start of the interval.
        t_end: End of the interval.
        n: Number of steps (default 1000).

    Returns:
        List of (t, y) pairs at each step.

    Example:
        >>> result = runge_kutta_4(lambda t, y: y, 1.0, 0, 1, 100)
        >>> abs(result[-1][1] - math.e) < 1e-8
        True

    Complexity: O(n)
    """
    _check_callable(f, "f")
    _check_positive_int(n, "n")

    h = (t_end - t_start) / n
    t = float(t_start)
    y = float(y0)
    result = [(t, y)]

    for _ in range(n):
        k1 = h * f(t, y)
        k2 = h * f(t + 0.5 * h, y + 0.5 * k1)
        k3 = h * f(t + 0.5 * h, y + 0.5 * k2)
        k4 = h * f(t + h, y + k3)
        y = y + (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0
        t = t + h
        result.append((t, y))

    return result


def adaptive_rk45(
    f: Callable[[float, float], float], y0: float,
    t_start: float, t_end: float,
    tol: float = 1e-8, h_init: float = 0.01,
    h_min: float = 1e-12, h_max: float = 1.0
) -> List[Tuple[float, float]]:
    """Solves the ODE y' = f(t, y) using the adaptive Runge-Kutta-Fehlberg (RK45) method.

    Automatically adjusts step size to maintain the prescribed error tolerance.

    Args:
        f: Right-hand side function f(t, y).
        y0: Initial condition y(t_start) = y0.
        t_start: Start of the interval.
        t_end: End of the interval.
        tol: Error tolerance per step (default 1e-8).
        h_init: Initial step size (default 0.01).
        h_min: Minimum step size (default 1e-12).
        h_max: Maximum step size (default 1.0).

    Returns:
        List of (t, y) pairs at adaptively chosen steps.

    Example:
        >>> result = adaptive_rk45(lambda t, y: y, 1.0, 0, 1)
        >>> abs(result[-1][1] - math.e) < 1e-6
        True

    Complexity: O(variable) depending on tolerance and function smoothness.
    """
    _check_callable(f, "f")

    # RK45 Fehlberg coefficients
    a2, a3, a4, a5, a6 = 1/4, 3/8, 12/13, 1.0, 1/2
    b21 = 1/4
    b31, b32 = 3/32, 9/32
    b41, b42, b43 = 1932/2197, -7200/2197, 7296/2197
    b51, b52, b53, b54 = 439/216, -8.0, 3680/513, -845/4104
    b61, b62, b63, b64, b65 = -8/27, 2.0, -3544/2565, 1859/4104, -11/40

    c1, c3, c4, c5 = 25/216, 1408/2565, 2197/4104, -1/5
    d1, d3, d4, d5, d6 = 16/135, 6656/12825, 28561/56430, -9/50, 2/55

    t = float(t_start)
    y = float(y0)
    h = min(h_init, t_end - t_start)
    result = [(t, y)]

    while t < t_end - 1e-15:
        h = min(h, t_end - t)

        k1 = h * f(t, y)
        k2 = h * f(t + a2 * h, y + b21 * k1)
        k3 = h * f(t + a3 * h, y + b31 * k1 + b32 * k2)
        k4 = h * f(t + a4 * h, y + b41 * k1 + b42 * k2 + b43 * k3)
        k5 = h * f(t + a5 * h, y + b51 * k1 + b52 * k2 + b53 * k3 + b54 * k4)
        k6 = h * f(t + a6 * h, y + b61 * k1 + b62 * k2 + b63 * k3 + b64 * k4 + b65 * k5)

        y4 = y + c1 * k1 + c3 * k3 + c4 * k4 + c5 * k5
        y5 = y + d1 * k1 + d3 * k3 + d4 * k4 + d5 * k5 + d6 * k6

        error = abs(y5 - y4)

        if error <= tol or h <= h_min:
            t = t + h
            y = y5
            result.append((t, y))

        if error > 0:
            s = 0.84 * (tol / error) ** 0.25
            h = max(h_min, min(h_max, s * h))
        else:
            h = min(h_max, 2.0 * h)

    return result


def ode_system_rk4(
    f: Callable[[float, List[float]], List[float]],
    y0: List[float], t_start: float, t_end: float, n: int = 1000
) -> List[Tuple[float, List[float]]]:
    """Solves a system of ODEs y' = f(t, y) using the 4th-order Runge-Kutta method.

    Args:
        f: Right-hand side function f(t, y) returning a list of derivatives.
        y0: Initial condition vector y(t_start).
        t_start: Start of the interval.
        t_end: End of the interval.
        n: Number of steps (default 1000).

    Returns:
        List of (t, y_vector) pairs at each step.

    Example:
        >>> # Solve y'' + y = 0 as system [y, y'] with y(0)=0, y'(0)=1
        >>> result = ode_system_rk4(lambda t, y: [y[1], -y[0]], [0.0, 1.0], 0, math.pi, 1000)
        >>> abs(result[-1][1][0]) < 0.001  # sin(pi) ≈ 0
        True

    Complexity: O(n * dim)
    """
    _check_callable(f, "f")
    _check_positive_int(n, "n")

    dim = len(y0)
    h = (t_end - t_start) / n
    t = float(t_start)
    y = [float(v) for v in y0]
    result = [(t, list(y))]

    for _ in range(n):
        k1 = f(t, y)
        k2 = f(t + 0.5 * h, [y[i] + 0.5 * h * k1[i] for i in range(dim)])
        k3 = f(t + 0.5 * h, [y[i] + 0.5 * h * k2[i] for i in range(dim)])
        k4 = f(t + h, [y[i] + h * k3[i] for i in range(dim)])

        for i in range(dim):
            y[i] += h * (k1[i] + 2.0 * k2[i] + 2.0 * k3[i] + k4[i]) / 6.0

        t += h
        result.append((t, list(y)))

    return result
