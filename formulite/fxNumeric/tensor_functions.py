"""Tensor analysis and index notation utilities.

Fundamental tools for tensor analysis from Murray R. Spiegel's
*Mathematical Handbook of Formulas and Tables*: Kronecker delta,
Levi-Civita symbol, metric tensors, Christoffel symbols, covariant
derivatives, and related operations.
"""

import math
from typing import List


# ---------------------------------------------------------------------------
# Kronecker delta and Levi-Civita
# ---------------------------------------------------------------------------


def kronecker_delta(i: int, j: int) -> int:
    """Kronecker delta δ_ij: 1 if i == j, else 0.

    Args:
        i: First index.
        j: Second index.

    Returns:
        1 if i == j, 0 otherwise.

    Example:
        >>> kronecker_delta(1, 1)
        1
        >>> kronecker_delta(1, 2)
        0

    Complexity: O(1)
    """

    if not isinstance(i, int) or not isinstance(j, int):
        raise TypeError("Indices must be integers.")

    return 1 if i == j else 0


def levi_civita(i: int, j: int, k: int) -> int:
    """Levi-Civita (permutation) symbol ε_{ijk} for 3D.

    Args:
        i: First index (1, 2, or 3).
        j: Second index (1, 2, or 3).
        k: Third index (1, 2, or 3).

    Returns:
        +1 for even permutations, -1 for odd, 0 if any indices repeat.

    Example:
        >>> levi_civita(1, 2, 3)
        1
        >>> levi_civita(1, 3, 2)
        -1

    Complexity: O(1)
    """

    if not all(isinstance(x, int) for x in (i, j, k)):
        raise TypeError("All indices must be integers.")

    if not all(x in (1, 2, 3) for x in (i, j, k)):
        raise ValueError("Indices must be 1, 2, or 3.")

    return (i - j) * (j - k) * (k - i) // 2


def levi_civita_nd(indices: List[int]) -> int:
    """Generalized Levi-Civita symbol for n dimensions.

    Args:
        indices: List of n indices, each in range [1, n].

    Returns:
        +1 for even permutations, -1 for odd, 0 if any repeat.

    Example:
        >>> levi_civita_nd([1, 2, 3, 4])
        1

    Complexity: O(n^2)
    """

    if not isinstance(indices, (list, tuple)):
        raise TypeError("indices must be a list.")

    n = len(indices)

    # Check for repeats
    if len(set(indices)) != n:
        return 0

    # Count inversions
    inv = 0

    for a in range(n):

        for b in range(a + 1, n):

            if indices[a] > indices[b]:
                inv += 1

    return 1 if inv % 2 == 0 else -1


# ---------------------------------------------------------------------------
# Metric tensor
# ---------------------------------------------------------------------------


def metric_tensor_from_jacobian(jacobian: List[List[float]]) -> List[List[float]]:
    """Computes the metric tensor g_{ij} = J^T · J from a Jacobian matrix.

    For a coordinate transformation x = x(q), the metric tensor is
    g_{ij} = Σ_k (∂x_k/∂q_i)(∂x_k/∂q_j).

    Args:
        jacobian: The Jacobian matrix J[i][j] = ∂x_i/∂q_j.

    Returns:
        Metric tensor as a 2D list.

    Example:
        >>> metric_tensor_from_jacobian([[1, 0], [0, 2]])
        [[1, 0], [0, 4]]

    Complexity: O(n^2 · m) where J is m × n
    """

    if not isinstance(jacobian, (list, tuple)):
        raise TypeError("jacobian must be a 2D list.")

    m = len(jacobian)

    if m == 0:
        raise ValueError("jacobian must not be empty.")

    n = len(jacobian[0])

    # g_{ij} = J^T · J
    g = []

    for i in range(n):
        row = []

        for j in range(n):
            s = 0.0

            for k in range(m):
                s += jacobian[k][i] * jacobian[k][j]

            row.append(s)

        g.append(row)

    return g


def metric_tensor_spherical(r: float, theta: float) -> List[List[float]]:
    """Metric tensor for spherical coordinates (r, θ, φ).

    g = diag(1, r², r²sin²θ)

    Args:
        r: Radial distance (must be positive).
        theta: Polar angle in radians.

    Returns:
        3×3 diagonal metric tensor.

    Example:
        >>> metric_tensor_spherical(2.0, math.pi / 2)
        [[1, 0, 0], [0, 4.0, 0], [0, 0, 4.0]]

    Complexity: O(1)
    """

    if not isinstance(r, (int, float)) or not isinstance(theta, (int, float)):
        raise TypeError("r and theta must be numeric.")

    if r <= 0:
        raise ValueError("r must be positive.")

    r2 = r * r
    sin_theta = math.sin(theta)

    return [
        [1, 0, 0],
        [0, r2, 0],
        [0, 0, r2 * sin_theta * sin_theta],
    ]


def metric_tensor_cylindrical(r: float) -> List[List[float]]:
    """Metric tensor for cylindrical coordinates (r, φ, z).

    g = diag(1, r², 1)

    Args:
        r: Radial distance (must be positive).

    Returns:
        3×3 diagonal metric tensor.

    Example:
        >>> metric_tensor_cylindrical(3.0)
        [[1, 0, 0], [0, 9.0, 0], [0, 0, 1]]

    Complexity: O(1)
    """

    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")

    if r <= 0:
        raise ValueError("r must be positive.")

    return [
        [1, 0, 0],
        [0, r * r, 0],
        [0, 0, 1],
    ]


# ---------------------------------------------------------------------------
# Christoffel symbols
# ---------------------------------------------------------------------------


def christoffel_symbols_diagonal(
    metric_diag: List[float],
    d_metric: List[List[float]],
) -> List[List[List[float]]]:
    """Christoffel symbols of the second kind for a diagonal metric.

    Γ^k_{ij} = (1 / 2g_{kk}) (∂g_{kj}/∂q_i + ∂g_{ki}/∂q_j - ∂g_{ij}/∂q_k)

    For a diagonal metric g_{ij} = 0 when i ≠ j, many symbols vanish.

    Args:
        metric_diag: Diagonal elements [g_11, g_22, g_33].
        d_metric: Partial derivatives of diagonal elements.
            ``d_metric[a][b]`` = ∂g_{aa} / ∂q_b.

    Returns:
        3D list Γ[k][i][j] for indices 0, 1, 2.

    Example:
        >>> christoffel_symbols_diagonal([1, 4, 4], [[0, 0, 0], [0, 0, 0], [0, 0, 0]])
        [[[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], [[0.0, 0.0, 0.0], [0.0, 0.0, 0.0], [0.0, 0.0, 0.0]]]

    Complexity: O(n^3) where n = dimension
    """

    if not isinstance(metric_diag, (list, tuple)):
        raise TypeError("metric_diag must be a list.")

    n = len(metric_diag)
    gamma = [[[0.0] * n for _ in range(n)] for _ in range(n)]

    for k in range(n):

        if metric_diag[k] == 0:
            continue

        inv_2g = 1.0 / (2.0 * metric_diag[k])

        for i in range(n):

            for j in range(n):
                # For diagonal metric: only non-zero when certain conditions hold
                val = 0.0

                if i == j == k:
                    val = inv_2g * d_metric[k][k]
                elif i == j and i != k:
                    val = -inv_2g * d_metric[i][k]
                elif (i == k and j != k):
                    val = inv_2g * d_metric[k][j]
                elif (j == k and i != k):
                    val = inv_2g * d_metric[k][i]

                gamma[k][i][j] = val

    return gamma


# ---------------------------------------------------------------------------
# Tensor operations
# ---------------------------------------------------------------------------


def tensor_contract(
    t: List[List[float]],
    idx1: int = 0,
    idx2: int = 1,
) -> float:
    """Contracts (traces) a rank-2 tensor over two indices.

    For a matrix T, the contraction T^i_i = Σ T_{ii} = trace(T).

    Args:
        t: Square matrix (2D list).
        idx1: First index (default 0).
        idx2: Second index (default 1).

    Returns:
        Scalar result of contraction.

    Example:
        >>> tensor_contract([[1, 2], [3, 4]])
        5

    Complexity: O(n)
    """

    if not isinstance(t, (list, tuple)):
        raise TypeError("t must be a 2D list.")

    n = len(t)
    result = 0.0

    for i in range(n):
        result += t[i][i]

    return result


def tensor_outer_product(u: list, v: list) -> List[List[float]]:
    """Outer (tensor) product of two vectors: T_{ij} = u_i · v_j.

    Args:
        u: First vector.
        v: Second vector.

    Returns:
        Rank-2 tensor (2D list).

    Example:
        >>> tensor_outer_product([1, 2], [3, 4])
        [[3, 4], [6, 8]]

    Complexity: O(n * m)
    """

    if not isinstance(u, (list, tuple)) or not isinstance(v, (list, tuple)):
        raise TypeError("u and v must be lists.")

    return [[ui * vj for vj in v] for ui in u]


def raise_index(
    v_covariant: list,
    metric_inverse_diag: list,
) -> list:
    """Raises the index of a covariant vector using a diagonal inverse metric.

    v^i = g^{ij} v_j. For diagonal metric, v^i = v_i / g_{ii}.

    Args:
        v_covariant: Covariant vector components.
        metric_inverse_diag: Diagonal elements of the inverse metric g^{ii}.

    Returns:
        Contravariant vector components.

    Example:
        >>> raise_index([3, 8], [1, 0.25])
        [3.0, 2.0]

    Complexity: O(n)
    """

    if not isinstance(v_covariant, (list, tuple)):
        raise TypeError("v_covariant must be a list.")

    if not isinstance(metric_inverse_diag, (list, tuple)):
        raise TypeError("metric_inverse_diag must be a list.")

    if len(v_covariant) != len(metric_inverse_diag):
        raise ValueError("Lengths must match.")

    return [v * g for v, g in zip(v_covariant, metric_inverse_diag)]


def lower_index(
    v_contravariant: list,
    metric_diag: list,
) -> list:
    """Lowers the index of a contravariant vector using a diagonal metric.

    v_i = g_{ij} v^j. For diagonal metric, v_i = g_{ii} · v^i.

    Args:
        v_contravariant: Contravariant vector components.
        metric_diag: Diagonal elements of the metric g_{ii}.

    Returns:
        Covariant vector components.

    Example:
        >>> lower_index([3, 2], [1, 4])
        [3, 8]

    Complexity: O(n)
    """

    if not isinstance(v_contravariant, (list, tuple)):
        raise TypeError("v_contravariant must be a list.")

    if not isinstance(metric_diag, (list, tuple)):
        raise TypeError("metric_diag must be a list.")

    if len(v_contravariant) != len(metric_diag):
        raise ValueError("Lengths must match.")

    return [v * g for v, g in zip(v_contravariant, metric_diag)]


def riemann_christoffel_check_2d(
    gamma: List[List[List[float]]],
) -> float:
    """Computes the single independent component of the Riemann curvature tensor in 2D.

    In 2 dimensions, R^1_{212} captures all curvature information.
    This is computed from Christoffel symbols: R^i_{jkl} = ∂Γ^i_{jl}/∂x_k - ∂Γ^i_{jk}/∂x_l + ...

    For a quick diagnostic, this returns Γ^0_{10}·Γ^1_{01} - Γ^0_{11}·Γ^1_{00}
    (the principal quadratic term of the 2D curvature).

    Args:
        gamma: Christoffel symbols Γ[k][i][j] for 2D (indices 0, 1).

    Returns:
        Approximate curvature indicator.

    Example:
        >>> riemann_christoffel_check_2d([[[0,0],[0,0]],[[0,0],[0,0]]])
        0.0

    Complexity: O(1)
    """

    if not isinstance(gamma, (list, tuple)):
        raise TypeError("gamma must be a 3D list.")

    return (
        gamma[0][1][0] * gamma[1][0][1]
        - gamma[0][1][1] * gamma[1][0][0]
    )


def geodesic_equation_rhs(
    gamma: List[List[List[float]]],
    velocity: list,
) -> list:
    """Right-hand side of the geodesic equation: d²x^k/dτ² = -Γ^k_{ij} dx^i/dτ dx^j/dτ.

    Args:
        gamma: Christoffel symbols Γ[k][i][j].
        velocity: Current velocity vector dx^i/dτ.

    Returns:
        Acceleration vector (d²x^k/dτ²).

    Example:
        >>> geodesic_equation_rhs([[[0,0],[0,0]],[[0,0],[0,0]]], [1, 0])
        [0.0, 0.0]

    Complexity: O(n^3)
    """

    if not isinstance(gamma, (list, tuple)):
        raise TypeError("gamma must be a 3D list.")

    if not isinstance(velocity, (list, tuple)):
        raise TypeError("velocity must be a list.")

    n = len(velocity)
    accel = [0.0] * n

    for k in range(n):

        for i in range(n):

            for j in range(n):
                accel[k] -= gamma[k][i][j] * velocity[i] * velocity[j]

    return accel
