"""Vector analysis and multivariable calculus.

Gradient, divergence, curl, Laplacian, Jacobian, Hessian, and related
operations from Spiegel's *Mathematical Handbook of Formulas and Tables*.
"""

import math
from typing import Callable, List, Tuple


# ---------------------------------------------------------------------------
# Vector triple products
# ---------------------------------------------------------------------------


def scalar_triple_product(
    u: List[float], v: List[float], w: List[float],
) -> float:
    """Scalar triple product u · (v × w) = det([u; v; w]).

    Args:
        u, v, w: 3-D vectors as lists of length 3.

    Returns:
        Scalar value.

    Example:
        >>> scalar_triple_product([1, 0, 0], [0, 1, 0], [0, 0, 1])
        1.0

    Complexity: O(1)
    """
    _check_3d_vector(u, "u")
    _check_3d_vector(v, "v")
    _check_3d_vector(w, "w")

    return float(
        u[0] * (v[1] * w[2] - v[2] * w[1])
        - u[1] * (v[0] * w[2] - v[2] * w[0])
        + u[2] * (v[0] * w[1] - v[1] * w[0])
    )


def vector_triple_product(
    u: List[float], v: List[float], w: List[float],
) -> List[float]:
    """Vector triple product u × (v × w) = v(u·w) - w(u·v).

    Args:
        u, v, w: 3-D vectors.

    Returns:
        Resulting 3-D vector.

    Example:
        >>> vector_triple_product([1, 0, 0], [0, 1, 0], [0, 0, 1])
        [0.0, 0.0, 0.0]

    Complexity: O(1)
    """
    _check_3d_vector(u, "u")
    _check_3d_vector(v, "v")
    _check_3d_vector(w, "w")

    u_dot_w = sum(a * b for a, b in zip(u, w))
    u_dot_v = sum(a * b for a, b in zip(u, v))

    return [
        float(v[i] * u_dot_w - w[i] * u_dot_v)
        for i in range(3)
    ]


def vector_projection(u: List[float], v: List[float]) -> List[float]:
    """Projection of vector u onto vector v: proj_v(u) = (u·v / v·v) v.

    Args:
        u: Vector to project.
        v: Vector to project onto (must be non-zero).

    Returns:
        Projection vector.

    Raises:
        ValueError: If v is a zero vector.

    Example:
        >>> vector_projection([3, 4], [1, 0])
        [3.0, 0.0]

    Complexity: O(n) for n-dimensional vectors.
    """
    if not isinstance(u, list) or not isinstance(v, list):
        raise TypeError("u and v must be lists.")

    if len(u) != len(v):
        raise ValueError("u and v must have the same dimension.")

    v_dot_v = sum(a * a for a in v)

    if v_dot_v == 0:
        raise ValueError("v must be a non-zero vector.")

    u_dot_v = sum(a * b for a, b in zip(u, v))
    scale = u_dot_v / v_dot_v
    return [float(scale * vi) for vi in v]


# ---------------------------------------------------------------------------
# Numerical multivariable calculus
# ---------------------------------------------------------------------------


def gradient_numerical(
    f: Callable[..., float],
    point: List[float],
    h: float = 1e-7,
) -> List[float]:
    """Computes the numerical gradient (nabla f) at a point.

    Uses central differences: df/dx_i ≈ (f(x+h e_i) - f(x-h e_i)) / (2h).

    Args:
        f: Scalar-valued function f(x1, x2, ..., xn).
        point: Evaluation point.
        h: Step size.

    Returns:
        Gradient vector.

    Example:
        >>> grad = gradient_numerical(lambda x, y: x**2 + y**2, [1.0, 2.0])
        >>> [round(g, 4) for g in grad]
        [2.0, 4.0]

    Complexity: O(2n) function evaluations.
    """
    if not isinstance(point, list):
        raise TypeError("point must be a list.")

    n = len(point)
    grad = []

    for i in range(n):
        point_plus = list(point)
        point_minus = list(point)
        point_plus[i] += h
        point_minus[i] -= h
        df = (f(*point_plus) - f(*point_minus)) / (2.0 * h)
        grad.append(df)

    return grad


def divergence_numerical(
    f_components: List[Callable[..., float]],
    point: List[float],
    h: float = 1e-7,
) -> float:
    """Computes the numerical divergence of a vector field F.

    div(F) = sum_i dF_i/dx_i.

    Args:
        f_components: List of scalar functions [F_1, F_2, ..., F_n], each
            accepting the same number of arguments as len(point).
        point: Evaluation point.
        h: Step size.

    Returns:
        Divergence scalar.

    Example:
        >>> div = divergence_numerical(
        ...     [lambda x, y: x, lambda x, y: y],
        ...     [1.0, 1.0],
        ... )
        >>> round(div, 4)
        2.0

    Complexity: O(2n) function evaluations.
    """
    if not isinstance(f_components, list) or not isinstance(point, list):
        raise TypeError("f_components and point must be lists.")

    if len(f_components) != len(point):
        raise ValueError("f_components and point must have the same length.")

    div = 0.0

    for i in range(len(point)):
        point_plus = list(point)
        point_minus = list(point)
        point_plus[i] += h
        point_minus[i] -= h
        div += (f_components[i](*point_plus) - f_components[i](*point_minus)) / (2.0 * h)

    return div


def curl_numerical(
    f_components: List[Callable[..., float]],
    point: List[float],
    h: float = 1e-7,
) -> List[float]:
    """Computes the numerical curl of a 3-D vector field F.

    curl(F) = (dF3/dy - dF2/dz, dF1/dz - dF3/dx, dF2/dx - dF1/dy).

    Args:
        f_components: List of 3 functions [F_x, F_y, F_z].
        point: 3-D evaluation point [x, y, z].
        h: Step size.

    Returns:
        Curl vector [curl_x, curl_y, curl_z].

    Raises:
        ValueError: If not 3-D.

    Example:
        >>> curl = curl_numerical(
        ...     [lambda x, y, z: -y, lambda x, y, z: x, lambda x, y, z: 0],
        ...     [0.0, 0.0, 0.0],
        ... )
        >>> [round(c, 4) for c in curl]
        [0.0, 0.0, 2.0]

    Complexity: O(12) function evaluations.
    """
    if len(f_components) != 3 or len(point) != 3:
        raise ValueError("curl is defined for 3-D vector fields.")

    def _partial(fi: Callable, pt: List[float], var: int) -> float:
        p_plus = list(pt)
        p_minus = list(pt)
        p_plus[var] += h
        p_minus[var] -= h
        return (fi(*p_plus) - fi(*p_minus)) / (2.0 * h)

    f1, f2, f3 = f_components

    curl_x = _partial(f3, point, 1) - _partial(f2, point, 2)
    curl_y = _partial(f1, point, 2) - _partial(f3, point, 0)
    curl_z = _partial(f2, point, 0) - _partial(f1, point, 1)

    return [curl_x, curl_y, curl_z]


def laplacian_numerical(
    f: Callable[..., float],
    point: List[float],
    h: float = 1e-5,
) -> float:
    """Computes the numerical Laplacian of a scalar field f.

    nabla^2 f = sum_i d^2f/dx_i^2.

    Args:
        f: Scalar-valued function.
        point: Evaluation point.
        h: Step size.

    Returns:
        Laplacian scalar.

    Example:
        >>> round(laplacian_numerical(lambda x, y: x**2 + y**2, [1.0, 1.0]), 2)
        4.0

    Complexity: O(2n) function evaluations.
    """
    if not isinstance(point, list):
        raise TypeError("point must be a list.")

    lap = 0.0
    f0 = f(*point)

    for i in range(len(point)):
        p_plus = list(point)
        p_minus = list(point)
        p_plus[i] += h
        p_minus[i] -= h
        lap += (f(*p_plus) - 2.0 * f0 + f(*p_minus)) / (h * h)

    return lap


def directional_derivative(
    f: Callable[..., float],
    point: List[float],
    direction: List[float],
    h: float = 1e-7,
) -> float:
    """Computes the directional derivative of f in the given direction.

    D_u f = grad(f) · u_hat.

    Args:
        f: Scalar-valued function.
        point: Evaluation point.
        direction: Direction vector (not necessarily unit).
        h: Step size for gradient.

    Returns:
        Directional derivative.

    Example:
        >>> round(directional_derivative(
        ...     lambda x, y: x**2 + y**2, [1.0, 1.0], [1.0, 0.0]
        ... ), 4)
        2.0

    Complexity: O(2n)
    """
    if not isinstance(direction, list):
        raise TypeError("direction must be a list.")

    mag = math.sqrt(sum(d * d for d in direction))

    if mag == 0:
        raise ValueError("direction must be a non-zero vector.")

    u_hat = [d / mag for d in direction]
    grad = gradient_numerical(f, point, h)
    return sum(g * u for g, u in zip(grad, u_hat))


def jacobian_numerical(
    f_components: List[Callable[..., float]],
    point: List[float],
    h: float = 1e-7,
) -> List[List[float]]:
    """Computes the numerical Jacobian matrix of a vector-valued function F.

    J[i][j] = dF_i / dx_j.

    Args:
        f_components: List of m scalar functions.
        point: n-dimensional evaluation point.
        h: Step size.

    Returns:
        m × n Jacobian matrix.

    Example:
        >>> J = jacobian_numerical(
        ...     [lambda x, y: x*y, lambda x, y: x+y],
        ...     [2.0, 3.0],
        ... )
        >>> [[round(v, 2) for v in row] for row in J]
        [[3.0, 2.0], [1.0, 1.0]]

    Complexity: O(2 * m * n)
    """
    if not isinstance(f_components, list) or not isinstance(point, list):
        raise TypeError("f_components and point must be lists.")

    m = len(f_components)
    n = len(point)
    jac = []

    for i in range(m):
        row = []

        for j in range(n):
            p_plus = list(point)
            p_minus = list(point)
            p_plus[j] += h
            p_minus[j] -= h
            row.append((f_components[i](*p_plus) - f_components[i](*p_minus)) / (2.0 * h))

        jac.append(row)

    return jac


def hessian_numerical(
    f: Callable[..., float],
    point: List[float],
    h: float = 1e-5,
) -> List[List[float]]:
    """Computes the numerical Hessian matrix of a scalar function f.

    H[i][j] = d^2f / (dx_i dx_j).

    Args:
        f: Scalar-valued function.
        point: Evaluation point.
        h: Step size.

    Returns:
        n × n Hessian matrix.

    Example:
        >>> H = hessian_numerical(lambda x, y: x**2 + y**2, [1.0, 1.0])
        >>> [[round(v, 2) for v in row] for row in H]
        [[2.0, 0.0], [0.0, 2.0]]

    Complexity: O(n^2) function evaluations.
    """
    if not isinstance(point, list):
        raise TypeError("point must be a list.")

    n = len(point)
    hess = [[0.0] * n for _ in range(n)]

    for i in range(n):

        for j in range(i, n):

            if i == j:
                # Second partial: (f(x+h) - 2f(x) + f(x-h)) / h^2
                p_plus = list(point)
                p_minus = list(point)
                p_plus[i] += h
                p_minus[i] -= h
                val = (f(*p_plus) - 2.0 * f(*point) + f(*p_minus)) / (h * h)
            else:
                # Mixed partial: (f(x+h_i+h_j) - f(x+h_i-h_j) - f(x-h_i+h_j) + f(x-h_i-h_j)) / (4h^2)
                pp = list(point)
                pm = list(point)
                mp = list(point)
                mm = list(point)
                pp[i] += h
                pp[j] += h
                pm[i] += h
                pm[j] -= h
                mp[i] -= h
                mp[j] += h
                mm[i] -= h
                mm[j] -= h
                val = (f(*pp) - f(*pm) - f(*mp) + f(*mm)) / (4.0 * h * h)

            hess[i][j] = val
            hess[j][i] = val

    return hess


def line_integral_numerical(
    f_components: List[Callable[..., float]],
    path_points: List[List[float]],
) -> float:
    """Numerically approximates a line integral of F along a piecewise-linear path.

    integral F · dr ≈ sum F(midpoint) · delta_r.

    Args:
        f_components: Vector field [F_1, ..., F_n].
        path_points: Ordered list of points defining the path.

    Returns:
        Approximate line integral.

    Example:
        >>> line_integral_numerical(
        ...     [lambda x, y: 1, lambda x, y: 0],
        ...     [[0, 0], [1, 0], [1, 1]],
        ... )
        1.0

    Complexity: O(m * n) where m = number of segments.
    """
    if not isinstance(f_components, list) or not isinstance(path_points, list):
        raise TypeError("f_components and path_points must be lists.")

    if len(path_points) < 2:
        raise ValueError("At least 2 path points are required.")

    total = 0.0

    for i in range(len(path_points) - 1):
        p0 = path_points[i]
        p1 = path_points[i + 1]
        mid = [(a + b) / 2.0 for a, b in zip(p0, p1)]
        dr = [b - a for a, b in zip(p0, p1)]

        for j in range(len(f_components)):
            total += f_components[j](*mid) * dr[j]

    return total


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_3d_vector(v: List[float], name: str) -> None:
    """Validates a 3-D vector."""

    if not isinstance(v, list) or len(v) != 3:
        raise TypeError(f"{name} must be a list of 3 numeric values.")

    for vi in v:

        if not isinstance(vi, (int, float)):
            raise TypeError(f"All elements of {name} must be numeric.")


# ---------------------------------------------------------------------------
# Surface integrals and flux (Spiegel Ch. Vector Analysis)
# ---------------------------------------------------------------------------


def surface_integral_numerical(
    f: Callable[[float, float, float], float],
    r: Callable[[float, float], Tuple[float, float, float]],
    u_range: Tuple[float, float],
    v_range: Tuple[float, float],
    n_u: int = 50,
    n_v: int = 50,
) -> float:
    """Computes a scalar surface integral ∬_S f(x,y,z) dS numerically.

    dS = |∂r/∂u × ∂r/∂v| du dv for a parametric surface r(u,v).

    Args:
        f: Scalar function f(x, y, z).
        r: Parametric surface function r(u, v) → (x, y, z).
        u_range: Tuple (u_min, u_max).
        v_range: Tuple (v_min, v_max).
        n_u: Subdivisions in u.
        n_v: Subdivisions in v.

    Returns:
        Approximate surface integral.

    Example:
        >>> import math
        >>> # Sphere r=1: surface area = 4π
        >>> def sphere(u, v): return (math.sin(u)*math.cos(v), math.sin(u)*math.sin(v), math.cos(u))
        >>> round(surface_integral_numerical(lambda x,y,z: 1, sphere, (0, math.pi), (0, 2*math.pi), 100, 100), 1)
        12.6

    Complexity: O(n_u * n_v)
    """
    if not callable(f) or not callable(r):
        raise TypeError("f and r must be callable.")

    h_u = (u_range[1] - u_range[0]) / n_u
    h_v = (v_range[1] - v_range[0]) / n_v
    eps = 1e-7
    total = 0.0

    for i in range(n_u):
        u = u_range[0] + (i + 0.5) * h_u

        for j in range(n_v):
            v = v_range[0] + (j + 0.5) * h_v
            p = r(u, v)

            # Partial derivatives via central differences
            ru = tuple((r(u + eps, v)[k] - r(u - eps, v)[k]) / (2 * eps) for k in range(3))
            rv = tuple((r(u, v + eps)[k] - r(u, v - eps)[k]) / (2 * eps) for k in range(3))

            # Cross product ru × rv
            nx = ru[1] * rv[2] - ru[2] * rv[1]
            ny = ru[2] * rv[0] - ru[0] * rv[2]
            nz = ru[0] * rv[1] - ru[1] * rv[0]

            ds = math.sqrt(nx * nx + ny * ny + nz * nz)
            total += f(p[0], p[1], p[2]) * ds * h_u * h_v

    return total


def flux_integral_numerical(
    field: Tuple[
        Callable[[float, float, float], float],
        Callable[[float, float, float], float],
        Callable[[float, float, float], float],
    ],
    r: Callable[[float, float], Tuple[float, float, float]],
    u_range: Tuple[float, float],
    v_range: Tuple[float, float],
    n_u: int = 50,
    n_v: int = 50,
) -> float:
    """Computes a vector flux integral ∬_S F · dS numerically.

    F · dS = F · (∂r/∂u × ∂r/∂v) du dv.

    Args:
        field: Tuple of 3 functions (Fx, Fy, Fz) giving the vector field.
        r: Parametric surface function r(u, v) → (x, y, z).
        u_range: Tuple (u_min, u_max).
        v_range: Tuple (v_min, v_max).
        n_u: Subdivisions in u.
        n_v: Subdivisions in v.

    Returns:
        Approximate flux integral.

    Example:
        >>> import math
        >>> # Flux of radial field F=(x,y,z) through unit sphere = 4π
        >>> def sphere(u, v): return (math.sin(u)*math.cos(v), math.sin(u)*math.sin(v), math.cos(u))
        >>> round(flux_integral_numerical((lambda x,y,z: x, lambda x,y,z: y, lambda x,y,z: z), sphere, (0, math.pi), (0, 2*math.pi), 100, 100), 1)
        12.6

    Complexity: O(n_u * n_v)
    """
    if not callable(r):
        raise TypeError("r must be callable.")

    h_u = (u_range[1] - u_range[0]) / n_u
    h_v = (v_range[1] - v_range[0]) / n_v
    eps = 1e-7
    total = 0.0

    for i in range(n_u):
        u = u_range[0] + (i + 0.5) * h_u

        for j in range(n_v):
            v = v_range[0] + (j + 0.5) * h_v
            p = r(u, v)

            ru = tuple((r(u + eps, v)[k] - r(u - eps, v)[k]) / (2 * eps) for k in range(3))
            rv = tuple((r(u, v + eps)[k] - r(u, v - eps)[k]) / (2 * eps) for k in range(3))

            nx = ru[1] * rv[2] - ru[2] * rv[1]
            ny = ru[2] * rv[0] - ru[0] * rv[2]
            nz = ru[0] * rv[1] - ru[1] * rv[0]

            fx = field[0](p[0], p[1], p[2])
            fy = field[1](p[0], p[1], p[2])
            fz = field[2](p[0], p[1], p[2])

            total += (fx * nx + fy * ny + fz * nz) * h_u * h_v

    return total


def divergence_theorem_verify(
    field: Tuple[
        Callable[[float, float, float], float],
        Callable[[float, float, float], float],
        Callable[[float, float, float], float],
    ],
    r_surface: Callable[[float, float], Tuple[float, float, float]],
    u_range: Tuple[float, float],
    v_range: Tuple[float, float],
    x_range: Tuple[float, float],
    y_range: Tuple[float, float],
    z_range: Tuple[float, float],
    n_s: int = 50,
    n_v_pts: int = 20,
) -> Tuple[float, float]:
    """Verifies the divergence theorem: ∬_S F·dS = ∭_V ∇·F dV.

    Computes both the surface flux integral and the volume integral of
    the divergence, returning both for comparison.

    Args:
        field: Tuple of 3 functions (Fx, Fy, Fz).
        r_surface: Parametric surface r(u,v) → (x,y,z).
        u_range: Parameter range for surface.
        v_range: Parameter range for surface.
        x_range: Volume bounds in x.
        y_range: Volume bounds in y.
        z_range: Volume bounds in z.
        n_s: Surface quadrature subdivisions.
        n_v_pts: Volume quadrature points per dimension.

    Returns:
        Tuple (surface_flux, volume_divergence).

    Example:
        >>> isinstance(divergence_theorem_verify(
        ...     (lambda x,y,z: x, lambda x,y,z: y, lambda x,y,z: z),
        ...     lambda u,v: (__import__('math').sin(u)*__import__('math').cos(v), __import__('math').sin(u)*__import__('math').sin(v), __import__('math').cos(u)),
        ...     (0, 3.14159), (0, 6.28318), (-1,1), (-1,1), (-1,1), 30, 10
        ... ), tuple)
        True

    Complexity: O(n_s^2 + n_v_pts^3)
    """
    # Surface flux
    surface_val = flux_integral_numerical(field, r_surface, u_range, v_range, n_s, n_s)

    # Volume integral of divergence
    hx = (x_range[1] - x_range[0]) / n_v_pts
    hy = (y_range[1] - y_range[0]) / n_v_pts
    hz = (z_range[1] - z_range[0]) / n_v_pts
    eps = 1e-6
    vol_total = 0.0

    for i in range(n_v_pts):
        x = x_range[0] + (i + 0.5) * hx

        for j in range(n_v_pts):
            y = y_range[0] + (j + 0.5) * hy

            for k in range(n_v_pts):
                z = z_range[0] + (k + 0.5) * hz

                # ∇·F = ∂Fx/∂x + ∂Fy/∂y + ∂Fz/∂z
                dFx = (field[0](x + eps, y, z) - field[0](x - eps, y, z)) / (2 * eps)
                dFy = (field[1](x, y + eps, z) - field[1](x, y - eps, z)) / (2 * eps)
                dFz = (field[2](x, y, z + eps) - field[2](x, y, z - eps)) / (2 * eps)

                vol_total += (dFx + dFy + dFz) * hx * hy * hz

    return (surface_val, vol_total)
