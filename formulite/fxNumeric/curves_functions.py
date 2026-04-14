"""Parametric curves, curvature, and arc-length formulas.

Classical plane curves and curvature analysis from Murray R. Spiegel's
*Mathematical Handbook of Formulas and Tables*: cycloid, epicycloid,
hypocycloid, cardioid, lemniscate, spirals, and curvature computations.
"""

import math
from typing import Callable, Tuple


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_numeric(value: object, name: str = "value") -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric.")


def _check_positive(value: float, name: str = "value") -> None:
    if value <= 0:
        raise ValueError(f"{name} must be positive.")


def _check_callable(f: object, name: str = "f") -> None:
    if not callable(f):
        raise TypeError(f"{name} must be callable.")


# ---------------------------------------------------------------------------
# Parametric curve coordinates
# ---------------------------------------------------------------------------


def cycloid(t: float, r: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of a cycloid at parameter t.

    A cycloid is the curve traced by a point on the rim of a circle
    of radius r rolling along a straight line.

    Args:
        t: Parameter (angle of rotation in radians).
        r: Radius of the generating circle (default 1.0).

    Returns:
        Tuple (x, y).

    Example:
        >>> cycloid(math.pi, 1.0)
        (3.141592653589793, 2.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_numeric(r, "r")
    _check_positive(r, "r")
    return (r * (t - math.sin(t)), r * (1.0 - math.cos(t)))


def epicycloid(t: float, R: float, r: float) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of an epicycloid at parameter t.

    Traced by a point on a circle of radius r rolling outside a circle of radius R.

    Args:
        t: Parameter angle in radians.
        R: Radius of the fixed circle.
        r: Radius of the rolling circle.

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = epicycloid(0, 3, 1)
        >>> (round(x, 6), round(y, 6))
        (4.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(R, "R")
    _check_positive(r, "r")
    ratio = (R + r) / r
    x = (R + r) * math.cos(t) - r * math.cos(ratio * t)
    y = (R + r) * math.sin(t) - r * math.sin(ratio * t)
    return (x, y)


def hypocycloid(t: float, R: float, r: float) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of a hypocycloid at parameter t.

    Traced by a point on a circle of radius r rolling inside a circle of radius R.

    Args:
        t: Parameter angle in radians.
        R: Radius of the fixed circle.
        r: Radius of the rolling circle (r < R).

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = hypocycloid(0, 4, 1)
        >>> (round(x, 6), round(y, 6))
        (4.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(R, "R")
    _check_positive(r, "r")
    ratio = (R - r) / r
    x = (R - r) * math.cos(t) + r * math.cos(ratio * t)
    y = (R - r) * math.sin(t) - r * math.sin(ratio * t)
    return (x, y)


def cardioid(t: float, a: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of a cardioid at parameter t.

    Polar equation r = a(1 + cos θ), converted to Cartesian.

    Args:
        t: Parameter angle in radians.
        a: Scale factor (default 1.0).

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = cardioid(0, 1.0)
        >>> (round(x, 6), round(y, 6))
        (2.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    rho = a * (1.0 + math.cos(t))
    return (rho * math.cos(t), rho * math.sin(t))


def lemniscate(t: float, a: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of the lemniscate of Bernoulli at parameter t.

    Polar equation r^2 = a^2 cos(2θ). Only defined where cos(2t) >= 0.

    Args:
        t: Parameter angle in radians.
        a: Scale factor (default 1.0).

    Returns:
        Tuple (x, y).

    Raises:
        ValueError: If cos(2t) < 0 (curve undefined at this angle).

    Example:
        >>> x, y = lemniscate(0, 1.0)
        >>> (round(x, 6), round(y, 6))
        (1.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    c2t = math.cos(2.0 * t)

    if c2t < 0:
        raise ValueError("Lemniscate undefined for cos(2t) < 0.")

    rho = a * math.sqrt(c2t)
    return (rho * math.cos(t), rho * math.sin(t))


def archimedean_spiral(t: float, a: float = 0.0, b: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of an Archimedean spiral at parameter t.

    Polar equation r = a + b*θ.

    Args:
        t: Parameter angle in radians (>= 0).
        a: Initial radius offset (default 0.0).
        b: Growth rate per radian (default 1.0).

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = archimedean_spiral(math.pi, 0, 1)
        >>> round(x, 4)
        -3.1416

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_numeric(a, "a")
    _check_numeric(b, "b")
    rho = a + b * t
    return (rho * math.cos(t), rho * math.sin(t))


def logarithmic_spiral(t: float, a: float = 1.0, b: float = 0.2) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of a logarithmic spiral at parameter t.

    Polar equation r = a * e^(b*θ).

    Args:
        t: Parameter angle in radians.
        a: Scale factor (default 1.0).
        b: Growth factor (default 0.2).

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = logarithmic_spiral(0, 1, 0.2)
        >>> (round(x, 6), round(y, 6))
        (1.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    _check_numeric(b, "b")
    rho = a * math.exp(b * t)
    return (rho * math.cos(t), rho * math.sin(t))


def involute_of_circle(t: float, r: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of the involute of a circle at parameter t.

    Args:
        t: Parameter angle in radians (>= 0).
        r: Radius of the base circle (default 1.0).

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = involute_of_circle(0, 1)
        >>> (round(x, 6), round(y, 6))
        (1.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(r, "r")
    x = r * (math.cos(t) + t * math.sin(t))
    y = r * (math.sin(t) - t * math.cos(t))
    return (x, y)


def rose_curve(t: float, a: float = 1.0, k: int = 3) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of a rose (rhodonea) curve at parameter t.

    Polar equation r = a * cos(k*θ).

    Args:
        t: Parameter angle in radians.
        a: Petal length (default 1.0).
        k: Number of petals parameter (default 3). k petals if odd, 2k if even.

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = rose_curve(0, 1, 3)
        >>> (round(x, 6), round(y, 6))
        (1.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    rho = a * math.cos(k * t)
    return (rho * math.cos(t), rho * math.sin(t))


def astroid(t: float, a: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of an astroid at parameter t.

    Special case of a hypocycloid with R = 4r. Parametric: x = a cos^3(t), y = a sin^3(t).

    Args:
        t: Parameter angle in radians.
        a: Scale factor (default 1.0).

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = astroid(0, 1)
        >>> (round(x, 6), round(y, 6))
        (1.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    return (a * math.cos(t) ** 3, a * math.sin(t) ** 3)


# ---------------------------------------------------------------------------
# Curvature and arc length
# ---------------------------------------------------------------------------


def curvature_explicit(
    f: Callable[[float], float], x: float, h: float = 1e-5
) -> float:
    """Computes the curvature κ of y = f(x) at point x using numerical derivatives.

    κ = |f''(x)| / (1 + f'(x)^2)^(3/2)

    Args:
        f: Function y = f(x).
        x: Point of evaluation.
        h: Step size for numerical derivatives (default 1e-5).

    Returns:
        Curvature κ at x.

    Example:
        >>> round(curvature_explicit(lambda x: x**2, 0), 6)
        2.0

    Complexity: O(1)
    """
    _check_callable(f, "f")
    _check_numeric(x, "x")
    fp = (f(x + h) - f(x - h)) / (2.0 * h)
    fpp = (f(x + h) - 2.0 * f(x) + f(x - h)) / (h * h)
    return abs(fpp) / (1.0 + fp * fp) ** 1.5


def curvature_parametric(
    x_func: Callable[[float], float], y_func: Callable[[float], float],
    t: float, h: float = 1e-5
) -> float:
    """Computes the curvature κ of a parametric curve (x(t), y(t)) at parameter t.

    κ = |x'y'' - y'x''| / (x'^2 + y'^2)^(3/2)

    Args:
        x_func: x(t) component function.
        y_func: y(t) component function.
        t: Parameter value.
        h: Step size for numerical derivatives (default 1e-5).

    Returns:
        Curvature κ at t.

    Example:
        >>> # Circle of radius 1: x=cos(t), y=sin(t), curvature = 1
        >>> round(curvature_parametric(math.cos, math.sin, 0), 4)
        1.0

    Complexity: O(1)
    """
    _check_callable(x_func, "x_func")
    _check_callable(y_func, "y_func")
    _check_numeric(t, "t")

    dx = (x_func(t + h) - x_func(t - h)) / (2.0 * h)
    dy = (y_func(t + h) - y_func(t - h)) / (2.0 * h)
    ddx = (x_func(t + h) - 2.0 * x_func(t) + x_func(t - h)) / (h * h)
    ddy = (y_func(t + h) - 2.0 * y_func(t) + y_func(t - h)) / (h * h)

    numer = abs(dx * ddy - dy * ddx)
    denom = (dx * dx + dy * dy) ** 1.5

    if denom < 1e-15:
        return float("inf")

    return numer / denom


def curvature_polar(
    r_func: Callable[[float], float], theta: float, h: float = 1e-5
) -> float:
    """Computes the curvature κ of a polar curve r = f(θ) at angle θ.

    κ = |r^2 + 2r'^2 - r*r''| / (r^2 + r'^2)^(3/2)

    Args:
        r_func: Polar function r(θ).
        theta: Angle of evaluation.
        h: Step size for numerical derivatives (default 1e-5).

    Returns:
        Curvature κ at θ.

    Example:
        >>> # Circle r = 1, curvature = 1
        >>> round(curvature_polar(lambda t: 1.0, 0), 4)
        1.0

    Complexity: O(1)
    """
    _check_callable(r_func, "r_func")
    _check_numeric(theta, "theta")

    r = r_func(theta)
    dr = (r_func(theta + h) - r_func(theta - h)) / (2.0 * h)
    ddr = (r_func(theta + h) - 2.0 * r_func(theta) + r_func(theta - h)) / (h * h)

    numer = abs(r * r + 2.0 * dr * dr - r * ddr)
    denom = (r * r + dr * dr) ** 1.5

    if denom < 1e-15:
        return float("inf")

    return numer / denom


def radius_of_curvature(
    f: Callable[[float], float], x: float, h: float = 1e-5
) -> float:
    """Computes the radius of curvature R = 1/κ of y = f(x) at point x.

    Args:
        f: Function y = f(x).
        x: Point of evaluation.
        h: Step size for numerical derivatives (default 1e-5).

    Returns:
        Radius of curvature. Returns inf if curvature is zero.

    Example:
        >>> round(radius_of_curvature(lambda x: x**2, 0), 6)
        0.5

    Complexity: O(1)
    """
    k = curvature_explicit(f, x, h)

    if k < 1e-15:
        return float("inf")

    return 1.0 / k


def arc_length_parametric(
    x_func: Callable[[float], float], y_func: Callable[[float], float],
    t_start: float, t_end: float, n: int = 10000
) -> float:
    """Computes the arc length of a parametric curve (x(t), y(t)) over [t_start, t_end].

    Uses the trapezoidal rule to integrate sqrt(x'^2 + y'^2).

    Args:
        x_func: x(t) component function.
        y_func: y(t) component function.
        t_start: Start parameter.
        t_end: End parameter.
        n: Number of integration steps (default 10000).

    Returns:
        Approximate arc length.

    Example:
        >>> # Semicircle: x=cos(t), y=sin(t) from 0 to pi → length = pi
        >>> round(arc_length_parametric(math.cos, math.sin, 0, math.pi, 100000), 4)
        3.1416

    Complexity: O(n)
    """
    _check_callable(x_func, "x_func")
    _check_callable(y_func, "y_func")

    h = (t_end - t_start) / n

    def speed(t: float) -> float:
        dx = (x_func(t + 1e-7) - x_func(t - 1e-7)) / 2e-7
        dy = (y_func(t + 1e-7) - y_func(t - 1e-7)) / 2e-7
        return math.sqrt(dx * dx + dy * dy)

    total = 0.5 * (speed(t_start) + speed(t_end))

    for i in range(1, n):
        total += speed(t_start + i * h)

    return total * h


def arc_length_polar(
    r_func: Callable[[float], float], theta_start: float, theta_end: float,
    n: int = 10000
) -> float:
    """Computes the arc length of a polar curve r = f(θ) over [θ_start, θ_end].

    Integrates sqrt(r^2 + (dr/dθ)^2) dθ.

    Args:
        r_func: Polar function r(θ).
        theta_start: Start angle.
        theta_end: End angle.
        n: Number of integration steps (default 10000).

    Returns:
        Approximate arc length.

    Example:
        >>> # Circle r = 1, full circle length = 2*pi
        >>> round(arc_length_polar(lambda t: 1.0, 0, 2 * math.pi, 100000), 4)
        6.2832

    Complexity: O(n)
    """
    _check_callable(r_func, "r_func")

    h = (theta_end - theta_start) / n
    eps = 1e-7

    def ds(theta: float) -> float:
        r = r_func(theta)
        dr = (r_func(theta + eps) - r_func(theta - eps)) / (2.0 * eps)
        return math.sqrt(r * r + dr * dr)

    total = 0.5 * (ds(theta_start) + ds(theta_end))

    for i in range(1, n):
        total += ds(theta_start + i * h)

    return total * h


def arc_length_function(
    f: Callable[[float], float], a: float, b: float, n: int = 10000
) -> float:
    """Computes the arc length of y = f(x) over [a, b].

    Integrates sqrt(1 + f'(x)^2) dx.

    Args:
        f: Function y = f(x).
        a: Start of interval.
        b: End of interval.
        n: Number of integration steps (default 10000).

    Returns:
        Approximate arc length.

    Example:
        >>> # y = x from 0 to 1, length = sqrt(2)
        >>> round(arc_length_function(lambda x: x, 0, 1), 6)
        1.414214

    Complexity: O(n)
    """
    _check_callable(f, "f")

    h_int = (b - a) / n
    eps = 1e-7

    def ds(x: float) -> float:
        fp = (f(x + eps) - f(x - eps)) / (2.0 * eps)
        return math.sqrt(1.0 + fp * fp)

    total = 0.5 * (ds(a) + ds(b))

    for i in range(1, n):
        total += ds(a + i * h_int)

    return total * h_int


def cycloid_arc_length(r: float) -> float:
    """Computes the arc length of one arch of a cycloid with radius r.

    One full arch (0 to 2π) has length 8r.

    Args:
        r: Radius of the generating circle.

    Returns:
        Arc length of one complete arch.

    Example:
        >>> cycloid_arc_length(1.0)
        8.0

    Complexity: O(1)
    """
    _check_numeric(r, "r")
    _check_positive(r, "r")
    return 8.0 * r


def catenary(x: float, a: float = 1.0) -> float:
    """Evaluates the catenary curve y = a * cosh(x / a) at point x.

    The catenary describes the shape of a flexible chain hanging under gravity.

    Args:
        x: Horizontal coordinate.
        a: Catenary parameter (sag constant, default 1.0).

    Returns:
        y coordinate.

    Example:
        >>> catenary(0, 1.0)
        1.0

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(a, "a")
    return a * math.cosh(x / a)


def tractrix(t: float, a: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of a tractrix at parameter t.

    Args:
        t: Parameter in (0, pi) (angle from vertical).
        a: Scale factor (default 1.0).

    Returns:
        Tuple (x, y).

    Raises:
        ValueError: If t is not in (0, pi).

    Example:
        >>> x, y = tractrix(math.pi / 2, 1.0)
        >>> round(y, 6)
        0.0

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")

    if t <= 0 or t >= math.pi:
        raise ValueError("t must be in (0, pi).")

    x = a * (math.log(math.tan(t / 2.0)) + math.cos(t))
    y = a * math.sin(t)
    return (x, y)


def cissoid(t: float, a: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of the cissoid of Diocles at parameter t.

    Parametric: x = 2a*sin^2(t), y = 2a*sin^2(t)*tan(t).

    Args:
        t: Parameter angle in radians, t ≠ ±π/2.
        a: Scale factor (default 1.0).

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = cissoid(0, 1.0)
        >>> (round(x, 6), round(y, 6))
        (0.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    s = math.sin(t)
    x = 2.0 * a * s * s
    y = x * math.tan(t)
    return (x, y)


def strophoid(t: float, a: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of a right strophoid at parameter t.

    Polar equation r = -a * cos(2θ) / cos(θ), converted to Cartesian.

    Args:
        t: Parameter angle in radians, t ≠ ±π/2.
        a: Scale factor (default 1.0).

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = strophoid(0, 1.0)
        >>> (round(x, 6), round(y, 6))
        (-1.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    ct = math.cos(t)

    if abs(ct) < 1e-15:
        raise ValueError("Strophoid undefined at t = ±π/2.")

    rho = -a * math.cos(2.0 * t) / ct
    return (rho * math.cos(t), rho * math.sin(t))


def witch_of_agnesi(x: float, a: float = 1.0) -> float:
    """Evaluates the Witch of Agnesi curve y = 8a^3 / (x^2 + 4a^2) at point x.

    Args:
        x: Horizontal coordinate.
        a: Scale factor (default 1.0).

    Returns:
        y coordinate.

    Example:
        >>> witch_of_agnesi(0, 1.0)
        2.0

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_positive(a, "a")
    return 8.0 * a ** 3 / (x * x + 4.0 * a * a)


def folium_of_descartes(t: float, a: float = 1.0) -> Tuple[float, float]:
    """Returns the (x, y) coordinates of the folium of Descartes at parameter t.

    Parametric: x = 3at/(1 + t^3), y = 3at^2/(1 + t^3).

    Args:
        t: Parameter (t ≠ -1).
        a: Scale factor (default 1.0).

    Returns:
        Tuple (x, y).

    Example:
        >>> x, y = folium_of_descartes(1, 1.0)
        >>> (round(x, 6), round(y, 6))
        (1.5, 1.5)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    denom = 1.0 + t ** 3

    if abs(denom) < 1e-15:
        raise ValueError("Folium undefined at t = -1.")

    return (3.0 * a * t / denom, 3.0 * a * t * t / denom)


# ---------------------------------------------------------------------------
# Differential geometry – surface curvatures (Spiegel Ch. Diff. Geometry)
# ---------------------------------------------------------------------------


def gaussian_curvature_sphere(r: float) -> float:
    """Returns the Gaussian curvature of a sphere of radius r.

    K = 1/r².

    Args:
        r: Radius (positive).

    Returns:
        Gaussian curvature.

    Example:
        >>> gaussian_curvature_sphere(2)
        0.25

    Complexity: O(1)
    """
    _check_positive(r, "r")
    return 1.0 / (r * r)


def mean_curvature_sphere(r: float) -> float:
    """Returns the mean curvature of a sphere of radius r.

    H = 1/r.

    Args:
        r: Radius (positive).

    Returns:
        Mean curvature.

    Example:
        >>> mean_curvature_sphere(4)
        0.25

    Complexity: O(1)
    """
    _check_positive(r, "r")
    return 1.0 / r


def gaussian_curvature_cylinder(r: float) -> float:
    """Returns the Gaussian curvature of a circular cylinder of radius r.

    K = 0 (cylinders are developable surfaces).

    Args:
        r: Radius (positive).

    Returns:
        0.0.

    Example:
        >>> gaussian_curvature_cylinder(5)
        0.0

    Complexity: O(1)
    """
    _check_positive(r, "r")
    return 0.0


def gaussian_curvature_torus(
    R: float, r: float, theta: float
) -> float:
    """Returns the Gaussian curvature of a torus at angle theta.

    K = cos(θ) / (r(R + r cos(θ))).

    Args:
        R: Major radius (distance from center of tube to center of torus).
        r: Minor radius (radius of tube).
        theta: Poloidal angle in radians.

    Returns:
        Gaussian curvature at theta.

    Example:
        >>> round(gaussian_curvature_torus(3, 1, 0), 6)
        0.25

    Complexity: O(1)
    """
    _check_positive(R, "R")
    _check_positive(r, "r")
    _check_numeric(theta, "theta")
    denom = r * (R + r * math.cos(theta))

    if abs(denom) < 1e-15:
        raise ValueError("Curvature undefined at this angle.")

    return math.cos(theta) / denom


def principal_curvatures_ellipsoid(
    a: float, b: float, c: float, u: float, v: float
) -> Tuple[float, float]:
    """Computes the principal curvatures of an ellipsoid at surface point (u, v).

    Uses the parametrization x = a sin(u) cos(v), y = b sin(u) sin(v), z = c cos(u).
    Evaluated at the specific poles for simplicity (general case is complex).

    For the north pole (u=0): kappa1 = c/a², kappa2 = c/b².

    Args:
        a: Semi-axis along x.
        b: Semi-axis along y.
        c: Semi-axis along z.
        u: Polar angle in [0, π].
        v: Azimuthal angle in [0, 2π].

    Returns:
        Tuple (kappa1, kappa2) principal curvatures.

    Example:
        >>> k1, k2 = principal_curvatures_ellipsoid(2, 3, 1, 0, 0)
        >>> (round(k1, 4), round(k2, 4))
        (0.25, 0.1111)

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    _check_positive(c, "c")
    _check_numeric(u, "u")
    _check_numeric(v, "v")

    # At generic point, use first/second fundamental form numerically
    h = 1e-6

    # Position
    def pos(uu: float, vv: float) -> Tuple[float, float, float]:
        return (a * math.sin(uu) * math.cos(vv),
                b * math.sin(uu) * math.sin(vv),
                c * math.cos(uu))

    # Partial derivatives via finite differences
    p = pos(u, v)
    pu = tuple((pos(u + h, v)[i] - pos(u - h, v)[i]) / (2 * h) for i in range(3))
    pv = tuple((pos(u, v + h)[i] - pos(u, v - h)[i]) / (2 * h) for i in range(3))
    puu = tuple((pos(u + h, v)[i] - 2 * p[i] + pos(u - h, v)[i]) / (h * h) for i in range(3))
    pvv = tuple((pos(u, v + h)[i] - 2 * p[i] + pos(u, v - h)[i]) / (h * h) for i in range(3))
    puv = tuple((pos(u + h, v + h)[i] - pos(u + h, v - h)[i] - pos(u - h, v + h)[i] + pos(u - h, v - h)[i]) / (4 * h * h) for i in range(3))

    # Normal vector
    nx = pu[1] * pv[2] - pu[2] * pv[1]
    ny = pu[2] * pv[0] - pu[0] * pv[2]
    nz = pu[0] * pv[1] - pu[1] * pv[0]
    n_len = math.sqrt(nx * nx + ny * ny + nz * nz)

    if n_len < 1e-15:
        raise ValueError("Surface normal is degenerate at this point.")

    nn = (nx / n_len, ny / n_len, nz / n_len)

    # First fundamental form
    E = sum(pu[i] * pu[i] for i in range(3))
    F = sum(pu[i] * pv[i] for i in range(3))
    G = sum(pv[i] * pv[i] for i in range(3))

    # Second fundamental form
    L = sum(puu[i] * nn[i] for i in range(3))
    M = sum(puv[i] * nn[i] for i in range(3))
    N = sum(pvv[i] * nn[i] for i in range(3))

    # Principal curvatures are roots of (EG-F²)k² - (EN + GL - 2FM)k + (LN-M²) = 0
    det1 = E * G - F * F

    if abs(det1) < 1e-15:
        raise ValueError("Degenerate first fundamental form.")

    trace_s = (E * N + G * L - 2.0 * F * M) / det1
    det_s = (L * N - M * M) / det1

    disc = trace_s * trace_s - 4.0 * det_s

    if disc < 0:
        disc = 0.0

    sqrt_disc = math.sqrt(disc)
    return ((trace_s + sqrt_disc) / 2.0, (trace_s - sqrt_disc) / 2.0)


def surface_area_revolution(
    f: Callable[[float], float],
    a: float,
    b: float,
    n: int = 1000,
) -> float:
    """Computes the surface area of revolution of y = f(x) around the x-axis.

    Uses the trapezoidal rule: S = 2π ∫_a^b f(x) sqrt(1 + f'(x)²) dx.

    Args:
        f: Function y = f(x) (must be non-negative on [a, b]).
        a: Lower integration limit.
        b: Upper integration limit.
        n: Number of subdivisions.

    Returns:
        Surface area.

    Example:
        >>> import math
        >>> round(surface_area_revolution(lambda x: 1.0, 0, 1, 1000), 4)
        6.2832

    Complexity: O(n)
    """
    if not callable(f):
        raise TypeError("f must be callable.")

    _check_numeric(a, "a")
    _check_numeric(b, "b")

    if a >= b:
        raise ValueError("a must be less than b.")

    h_step = (b - a) / n
    h_diff = 1e-7
    total = 0.0

    for i in range(n + 1):
        xi = a + i * h_step
        yi = f(xi)
        dydx = (f(xi + h_diff) - f(xi - h_diff)) / (2.0 * h_diff)
        integrand = yi * math.sqrt(1.0 + dydx * dydx)

        if i == 0 or i == n:
            total += integrand
        else:
            total += 2.0 * integrand

    return 2.0 * math.pi * h_step * total / 2.0


# ---------------------------------------------------------------------------
# Additional classical curves (Spiegel)
# ---------------------------------------------------------------------------


def nephroid(t: float, a: float = 1.0) -> Tuple[float, float]:
    """Nephroid curve: x = a(3cos(t) - cos(3t)), y = a(3sin(t) - sin(3t)).

    A 2-cusped epicycloid.

    Args:
        t: Parameter (radians).
        a: Scale factor.

    Returns:
        (x, y) coordinates.

    Example:
        >>> nephroid(0, 1.0)
        (2.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    x = a * (3.0 * math.cos(t) - math.cos(3.0 * t))
    y = a * (3.0 * math.sin(t) - math.sin(3.0 * t))
    return (x, y)


def deltoid(t: float, a: float = 1.0) -> Tuple[float, float]:
    """Deltoid (3-cusped hypocycloid): x = a(2cos(t) + cos(2t)), y = a(2sin(t) - sin(2t)).

    Args:
        t: Parameter (radians).
        a: Scale factor.

    Returns:
        (x, y) coordinates.

    Example:
        >>> deltoid(0, 1.0)
        (3.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    x = a * (2.0 * math.cos(t) + math.cos(2.0 * t))
    y = a * (2.0 * math.sin(t) - math.sin(2.0 * t))
    return (x, y)


def limacon(t: float, a: float = 1.0, b: float = 0.5) -> Tuple[float, float]:
    """Limaçon of Pascal: r = a + b·cos(t), returned as (x, y).

    When b < a → dimpled; b = a → cardioid; b > a → inner loop.

    Args:
        t: Angle in radians.
        a: Offset parameter.
        b: Cosine coefficient.

    Returns:
        (x, y) coordinates.

    Example:
        >>> x, y = limacon(0, 1, 0.5)
        >>> round(x, 6)
        1.5

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_numeric(a, "a")
    _check_numeric(b, "b")
    r = a + b * math.cos(t)
    return (r * math.cos(t), r * math.sin(t))


def cassini_oval(t: float, a: float = 1.0, c: float = 1.2) -> Tuple[float, float]:
    """Cassini oval in polar form: r² = a² cos(2t) ± √(a⁴cos²(2t) - a⁴ + c⁴).

    Returns the outer branch.

    Args:
        t: Angle in radians.
        a: Focus half-distance.
        c: Product constant (c > 0).

    Returns:
        (x, y) coordinates (outer branch), or (0, 0) if r² < 0.

    Example:
        >>> x, y = cassini_oval(0, 1.0, 1.5)
        >>> round(x, 4) > 0
        True

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    _check_positive(c, "c")
    cos2t = math.cos(2.0 * t)
    disc = a ** 4 * cos2t ** 2 - a ** 4 + c ** 4

    if disc < 0:
        return (0.0, 0.0)

    r2 = a ** 2 * cos2t + math.sqrt(disc)

    if r2 < 0:
        return (0.0, 0.0)

    r = math.sqrt(r2)
    return (r * math.cos(t), r * math.sin(t))


def conchoid_of_nicomedes(t: float, a: float = 1.0, b: float = 2.0) -> Tuple[float, float]:
    """Conchoid of Nicomedes: r = a/cos(t) + b, returned as (x, y).

    Args:
        t: Angle in radians (avoid t = ±π/2).
        a: Distance to directrix.
        b: Offset distance.

    Returns:
        (x, y) coordinates.

    Raises:
        ValueError: If cos(t) ≈ 0.

    Example:
        >>> x, y = conchoid_of_nicomedes(0, 1, 2)
        >>> round(x, 6)
        3.0

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    _check_numeric(b, "b")
    ct = math.cos(t)

    if abs(ct) < 1e-12:
        raise ValueError("t must not make cos(t) ≈ 0.")

    r = a / ct + b
    return (r * math.cos(t), r * math.sin(t))


def lissajous(t: float, a: float = 1.0, b: float = 1.0, omega_x: float = 3.0, omega_y: float = 2.0, delta: float = 0.0) -> Tuple[float, float]:
    """Lissajous figure: x = a·sin(ωₓt + δ), y = b·sin(ωᵧt).

    Args:
        t: Parameter.
        a: X-amplitude.
        b: Y-amplitude.
        omega_x: X-frequency.
        omega_y: Y-frequency.
        delta: Phase difference.

    Returns:
        (x, y) coordinates.

    Example:
        >>> lissajous(0, 1, 1, 3, 2, 0)
        (0.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    x = a * math.sin(omega_x * t + delta)
    y = b * math.sin(omega_y * t)
    return (x, y)


def piriform(t: float, a: float = 1.0, b: float = 1.0) -> Tuple[float, float]:
    """Piriform (pear-shaped) curve: x = a(1 + sin(t)), y = b·cos(t)(1 + sin(t)).

    Args:
        t: Parameter (radians).
        a: X-scale.
        b: Y-scale.

    Returns:
        (x, y) coordinates.

    Example:
        >>> piriform(0, 1, 1)
        (1.0, 1.0)

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    _check_positive(a, "a")
    _check_positive(b, "b")
    s = 1.0 + math.sin(t)
    return (a * s, b * math.cos(t) * s)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 27: Curves Functions (1 of 2)
# ---------------------------------------------------------------------------

def fermat_spiral(a: float, theta: float) -> float:
    """Compute r for Fermat's spiral: r = a·√θ.

    Args:
        a: Scale parameter.
        theta: Angle in radians (≥ 0).

    Returns:
        Radial distance r.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a ≤ 0 or theta < 0.

    Usage Example:
        >>> round(fermat_spiral(1.0, 4.0), 4)
        2.0

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_numeric(theta, "theta")
    theta = float(theta)
    if theta < 0:
        raise ValueError("theta must be non-negative.")
    return float(a) * math.sqrt(theta)


def cochleoid(a: float, theta: float) -> float:
    """Compute r for the cochleoid curve: r = a·sin(θ)/θ.

    Args:
        a: Scale parameter.
        theta: Angle in radians (≠ 0).

    Returns:
        Radial distance r.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a ≤ 0 or theta = 0.

    Usage Example:
        >>> round(cochleoid(1.0, 1.0), 4)
        0.8415

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_numeric(theta, "theta")
    theta = float(theta)
    if abs(theta) < 1e-15:
        raise ValueError("theta must not be zero.")
    return float(a) * math.sin(theta) / theta


def evolute_ellipse(a: float, b: float, t: float) -> tuple[float, float]:
    """Compute a point on the evolute of an ellipse.

    x = (a² - b²)/a · cos³(t)
    y = (b² - a²)/b · sin³(t)

    Args:
        a: Semi-major axis.
        b: Semi-minor axis.
        t: Parameter angle in radians.

    Returns:
        (x, y) coordinates on the evolute.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a or b ≤ 0.

    Usage Example:
        >>> tuple(round(v, 4) for v in evolute_ellipse(5.0, 3.0, 0.0))
        (3.2, 0.0)

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    _check_numeric(t, "t")
    a, b, t = float(a), float(b), float(t)
    cos_t = math.cos(t)
    sin_t = math.sin(t)
    x = (a * a - b * b) / a * cos_t ** 3
    y = (b * b - a * a) / b * sin_t ** 3
    return (x, y)


def tautochrone_period(radius: float, g: float = 9.80665) -> float:
    """Compute the period of a tautochrone (cycloid) pendulum.

    T = 2π√(r/g) — same as a simple pendulum of length r.

    Args:
        radius: Radius of the generating circle.
        g: Gravitational acceleration (default 9.80665 m/s²).

    Returns:
        Period in seconds.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius ≤ 0 or g ≤ 0.

    Usage Example:
        >>> round(tautochrone_period(1.0), 4)
        2.0064

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_numeric(g, "g")
    g = float(g)
    if g <= 0:
        raise ValueError("g must be positive.")
    return 2.0 * math.pi * math.sqrt(float(radius) / g)


def brachistochrone_time(x_end: float, y_end: float, g: float = 9.80665) -> float:
    """Approximate the brachistochrone (fastest descent) time.

    Uses the cycloid solution: T ≈ θ·√(R/g) where R and θ satisfy
    the cycloid parametric equations.

    Args:
        x_end: Horizontal distance to endpoint (> 0).
        y_end: Vertical drop to endpoint (> 0, downward positive).
        g: Gravitational acceleration (default 9.80665 m/s²).

    Returns:
        Approximate descent time in seconds.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If x_end ≤ 0, y_end ≤ 0, or g ≤ 0.

    Usage Example:
        >>> round(brachistochrone_time(1.0, 1.0), 4)
        0.493

    Complexity: O(1) (uses analytical approximation)
    """
    _check_positive(x_end, "x_end")
    _check_positive(y_end, "y_end")
    _check_numeric(g, "g")
    x_end, y_end, g = float(x_end), float(y_end), float(g)
    if g <= 0:
        raise ValueError("g must be positive.")
    # Newton iteration to find theta from x/y = (theta - sin(theta))/(1 - cos(theta))
    ratio = x_end / y_end
    theta = math.pi  # initial guess
    for _ in range(50):
        sin_t = math.sin(theta)
        cos_t = math.cos(theta)
        denom = 1.0 - cos_t
        if abs(denom) < 1e-15:
            break
        f = (theta - sin_t) / denom - ratio
        fp = (denom - (theta - sin_t) * sin_t) / (denom * denom)
        if abs(fp) < 1e-15:
            break
        theta -= f / fp
    denom = 1.0 - math.cos(theta)
    if abs(denom) < 1e-15:
        R = y_end / 2.0
    else:
        R = y_end / denom / 2.0
    return theta * math.sqrt(R / g)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 28: Curves Functions (2 of 2)
# ---------------------------------------------------------------------------

def cornu_spiral(t: float, n: int = 50) -> tuple[float, float]:
    """Evaluate the Cornu (Euler) spiral at parameter t.

    C(t) = (∫₀ᵗ cos(πu²/2) du, ∫₀ᵗ sin(πu²/2) du)

    Uses trapezoidal rule with n steps.

    Args:
        t: Curve parameter.
        n: Number of integration steps (default 50).

    Returns:
        (x, y) point on the Cornu spiral.

    Raises:
        TypeError: If t is not numeric.

    Usage Example:
        >>> x, y = cornu_spiral(1.0)
        >>> round(x, 4)
        0.7798

    Complexity: O(n)
    """
    _check_numeric(t, "t")
    t = float(t)
    dt = t / n
    x = 0.0
    y = 0.0
    for i in range(n):
        u0 = i * dt
        u1 = (i + 1) * dt
        x += (math.cos(math.pi * u0 * u0 / 2.0) + math.cos(math.pi * u1 * u1 / 2.0)) / 2.0
        y += (math.sin(math.pi * u0 * u0 / 2.0) + math.sin(math.pi * u1 * u1 / 2.0)) / 2.0
    return (x * dt, y * dt)


def superellipse(a: float, b: float, n_exp: float, t: float) -> tuple[float, float]:
    """Evaluate a point on a superellipse.

    |x/a|^n + |y/b|^n = 1, parametrized as:
    x = a·|cos(t)|^(2/n)·sign(cos(t)),  y = b·|sin(t)|^(2/n)·sign(sin(t))

    Args:
        a: Semi-axis x.
        b: Semi-axis y.
        n_exp: Exponent (> 0).
        t: Parameter angle in radians.

    Returns:
        (x, y) point on the superellipse.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a, b ≤ 0 or n_exp ≤ 0.

    Usage Example:
        >>> x, y = superellipse(1.0, 1.0, 2.0, 0.0)
        >>> (round(x, 4), round(y, 4))
        (1.0, 0.0)

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    _check_positive(n_exp, "n_exp")
    _check_numeric(t, "t")
    a, b, t = float(a), float(b), float(t)
    exp = 2.0 / float(n_exp)
    cos_t = math.cos(t)
    sin_t = math.sin(t)
    sign_c = 1.0 if cos_t >= 0 else -1.0
    sign_s = 1.0 if sin_t >= 0 else -1.0
    x = a * (abs(cos_t) ** exp) * sign_c
    y = b * (abs(sin_t) ** exp) * sign_s
    return (x, y)


def hypotrochoid(R: float, r: float, d: float, t: float) -> tuple[float, float]:
    """Evaluate a hypotrochoid curve point.

    x = (R-r)cos(t) + d·cos((R-r)t/r)
    y = (R-r)sin(t) - d·sin((R-r)t/r)

    Args:
        R: Outer circle radius.
        r: Inner circle radius.
        d: Distance from center of inner circle.
        t: Parameter angle in radians.

    Returns:
        (x, y) point.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If R or r ≤ 0.

    Usage Example:
        >>> x, y = hypotrochoid(5.0, 3.0, 5.0, 0.0)
        >>> (round(x, 4), round(y, 4))
        (7.0, 0.0)

    Complexity: O(1)
    """
    _check_positive(R, "R")
    _check_positive(r, "r")
    _check_numeric(d, "d")
    _check_numeric(t, "t")
    R, r, d, t = float(R), float(r), float(d), float(t)
    diff = R - r
    ratio = diff / r
    x = diff * math.cos(t) + d * math.cos(ratio * t)
    y = diff * math.sin(t) - d * math.sin(ratio * t)
    return (x, y)


def epitrochoid(R: float, r: float, d: float, t: float) -> tuple[float, float]:
    """Evaluate an epitrochoid curve point.

    x = (R+r)cos(t) - d·cos((R+r)t/r)
    y = (R+r)sin(t) - d·sin((R+r)t/r)

    Args:
        R: Fixed circle radius.
        r: Rolling circle radius.
        d: Distance from center of rolling circle.
        t: Parameter angle in radians.

    Returns:
        (x, y) point.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If R or r ≤ 0.

    Usage Example:
        >>> x, y = epitrochoid(3.0, 1.0, 0.5, 0.0)
        >>> (round(x, 4), round(y, 4))
        (3.5, 0.0)

    Complexity: O(1)
    """
    _check_positive(R, "R")
    _check_positive(r, "r")
    _check_numeric(d, "d")
    _check_numeric(t, "t")
    R, r, d, t = float(R), float(r), float(d), float(t)
    s = R + r
    ratio = s / r
    x = s * math.cos(t) - d * math.cos(ratio * t)
    y = s * math.sin(t) - d * math.sin(ratio * t)
    return (x, y)


def bezier_quadratic(p0: tuple, p1: tuple, p2: tuple, t: float) -> tuple[float, float]:
    """Evaluate a quadratic Bézier curve at parameter t.

    B(t) = (1-t)²·P0 + 2(1-t)t·P1 + t²·P2

    Args:
        p0: Start point (x, y).
        p1: Control point (x, y).
        p2: End point (x, y).
        t: Parameter in [0, 1].

    Returns:
        (x, y) point on the curve.

    Raises:
        TypeError: If t is not numeric.
        ValueError: If t not in [0, 1].

    Usage Example:
        >>> bezier_quadratic((0, 0), (1, 2), (2, 0), 0.5)
        (1.0, 1.0)

    Complexity: O(1)
    """
    if not isinstance(t, (int, float)):
        raise TypeError("t must be numeric.")
    t = float(t)
    if t < 0 or t > 1:
        raise ValueError("t must be in [0, 1].")
    u = 1.0 - t
    x = u * u * float(p0[0]) + 2.0 * u * t * float(p1[0]) + t * t * float(p2[0])
    y = u * u * float(p0[1]) + 2.0 * u * t * float(p1[1]) + t * t * float(p2[1])
    return (x, y)


def bezier_cubic(
    p0: tuple, p1: tuple, p2: tuple, p3: tuple, t: float,
) -> tuple[float, float]:
    """Evaluate a cubic Bézier curve at parameter t.

    B(t) = (1-t)³P0 + 3(1-t)²tP1 + 3(1-t)t²P2 + t³P3

    Args:
        p0: Start point (x, y).
        p1: First control point (x, y).
        p2: Second control point (x, y).
        p3: End point (x, y).
        t: Parameter in [0, 1].

    Returns:
        (x, y) point on the curve.

    Raises:
        TypeError: If t is not numeric.
        ValueError: If t not in [0, 1].

    Usage Example:
        >>> bezier_cubic((0, 0), (1, 3), (2, 3), (3, 0), 0.5)
        (1.5, 2.25)

    Complexity: O(1)
    """
    if not isinstance(t, (int, float)):
        raise TypeError("t must be numeric.")
    t = float(t)
    if t < 0 or t > 1:
        raise ValueError("t must be in [0, 1].")
    u = 1.0 - t
    u2 = u * u
    t2 = t * t
    x = u2 * u * float(p0[0]) + 3.0 * u2 * t * float(p1[0]) + 3.0 * u * t2 * float(p2[0]) + t2 * t * float(p3[0])
    y = u2 * u * float(p0[1]) + 3.0 * u2 * t * float(p1[1]) + 3.0 * u * t2 * float(p2[1]) + t2 * t * float(p3[1])
    return (x, y)


def hermite_interpolation(
    p0: float, p1: float, m0: float, m1: float, t: float,
) -> float:
    """Cubic Hermite interpolation between two points.

    H(t) = (2t³-3t²+1)p0 + (t³-2t²+t)m0 + (-2t³+3t²)p1 + (t³-t²)m1

    Args:
        p0: Value at start.
        p1: Value at end.
        m0: Tangent at start.
        m1: Tangent at end.
        t: Parameter in [0, 1].

    Returns:
        Interpolated value.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If t not in [0, 1].

    Usage Example:
        >>> hermite_interpolation(0.0, 1.0, 0.0, 0.0, 0.5)
        0.5

    Complexity: O(1)
    """
    for name, val in [("p0", p0), ("p1", p1), ("m0", m0), ("m1", m1), ("t", t)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    t = float(t)
    if t < 0 or t > 1:
        raise ValueError("t must be in [0, 1].")
    t2 = t * t
    t3 = t2 * t
    h00 = 2.0 * t3 - 3.0 * t2 + 1.0
    h10 = t3 - 2.0 * t2 + t
    h01 = -2.0 * t3 + 3.0 * t2
    h11 = t3 - t2
    return h00 * float(p0) + h10 * float(m0) + h01 * float(p1) + h11 * float(m1)


def catmull_rom(
    p0: float, p1: float, p2: float, p3: float, t: float,
) -> float:
    """Catmull-Rom spline interpolation between p1 and p2.

    Uses p0/p3 as neighboring points for tangent computation.

    Args:
        p0: Previous point value.
        p1: Start point value.
        p2: End point value.
        p3: Next point value.
        t: Parameter in [0, 1].

    Returns:
        Interpolated value between p1 and p2.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If t not in [0, 1].

    Usage Example:
        >>> catmull_rom(0.0, 1.0, 2.0, 3.0, 0.5)
        1.5

    Complexity: O(1)
    """
    for name, val in [("p0", p0), ("p1", p1), ("p2", p2), ("p3", p3), ("t", t)]:
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    t = float(t)
    if t < 0 or t > 1:
        raise ValueError("t must be in [0, 1].")
    p0, p1, p2, p3 = float(p0), float(p1), float(p2), float(p3)
    t2 = t * t
    t3 = t2 * t
    return 0.5 * (
        (2.0 * p1)
        + (-p0 + p2) * t
        + (2.0 * p0 - 5.0 * p1 + 4.0 * p2 - p3) * t2
        + (-p0 + 3.0 * p1 - 3.0 * p2 + p3) * t3
    )


def lituus(a: float, theta: float) -> float:
    """Compute r for the lituus curve: r = a / √θ.

    Args:
        a: Scale parameter.
        theta: Angle in radians (> 0).

    Returns:
        Radial distance.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If a ≤ 0 or theta ≤ 0.

    Usage Example:
        >>> round(lituus(1.0, 1.0), 4)
        1.0

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(theta, "theta")
    return float(a) / math.sqrt(float(theta))


def butterfly_curve(t: float) -> tuple[float, float]:
    """Evaluate a point on the butterfly curve.

    x = sin(t)(e^cos(t) - 2cos(4t) - sin⁵(t/12))
    y = cos(t)(e^cos(t) - 2cos(4t) - sin⁵(t/12))

    Args:
        t: Parameter angle in radians.

    Returns:
        (x, y) point on the butterfly curve.

    Raises:
        TypeError: If t is not numeric.

    Usage Example:
        >>> x, y = butterfly_curve(0.0)
        >>> round(y, 4)
        0.7183

    Complexity: O(1)
    """
    _check_numeric(t, "t")
    t = float(t)
    common = math.exp(math.cos(t)) - 2.0 * math.cos(4.0 * t) - math.sin(t / 12.0) ** 5
    return (math.sin(t) * common, math.cos(t) * common)
