"""Conformal mappings from complex analysis.

Classical conformal transformations and complex mappings from Murray R.
Spiegel's *Mathematical Handbook of Formulas and Tables*: Möbius
(bilinear), Joukowski, power, exponential, and special mappings.
"""

import math
from typing import Tuple


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_numeric(value: float, name: str = "value") -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric.")


# ---------------------------------------------------------------------------
# Möbius (bilinear / linear fractional) transformation
# ---------------------------------------------------------------------------


def mobius_transform(
    z: Tuple[float, float],
    a: Tuple[float, float],
    b: Tuple[float, float],
    c: Tuple[float, float],
    d: Tuple[float, float],
) -> Tuple[float, float]:
    """Applies a Möbius (bilinear) transformation w = (az + b) / (cz + d).

    The transformation is conformal wherever cz + d ≠ 0.

    Args:
        z: Input complex number (re, im).
        a: Coefficient a (re, im).
        b: Coefficient b (re, im).
        c: Coefficient c (re, im).
        d: Coefficient d (re, im).

    Returns:
        Result w as (re, im).

    Raises:
        ValueError: If cz + d = 0.

    Example:
        >>> mobius_transform((1, 0), (1, 0), (0, 0), (0, 0), (1, 0))
        (1.0, 0.0)

    Complexity: O(1)
    """
    # Numerator: a*z + b
    num_re = a[0] * z[0] - a[1] * z[1] + b[0]
    num_im = a[0] * z[1] + a[1] * z[0] + b[1]

    # Denominator: c*z + d
    den_re = c[0] * z[0] - c[1] * z[1] + d[0]
    den_im = c[0] * z[1] + c[1] * z[0] + d[1]

    denom = den_re * den_re + den_im * den_im

    if denom < 1e-30:
        raise ValueError("Transformation undefined (cz + d = 0).")

    re = (num_re * den_re + num_im * den_im) / denom
    im = (num_im * den_re - num_re * den_im) / denom
    return (re, im)


def joukowski_transform(z: Tuple[float, float]) -> Tuple[float, float]:
    """Applies the Joukowski (Zhukovsky) conformal transformation w = z + 1/z.

    Maps circles to airfoil-like shapes. Fundamental in aerodynamics.

    Args:
        z: Input complex number (re, im). Must not be (0, 0).

    Returns:
        Result w as (re, im).

    Raises:
        ValueError: If z = 0.

    Example:
        >>> joukowski_transform((2, 0))
        (2.5, 0.0)

    Complexity: O(1)
    """
    r2 = z[0] * z[0] + z[1] * z[1]

    if r2 < 1e-30:
        raise ValueError("z must not be zero.")

    inv_re = z[0] / r2
    inv_im = -z[1] / r2
    return (z[0] + inv_re, z[1] + inv_im)


def inverse_joukowski(w: Tuple[float, float]) -> Tuple[Tuple[float, float], Tuple[float, float]]:
    """Computes both preimages of the Joukowski map: z = (w ± sqrt(w² - 4)) / 2.

    Args:
        w: Image complex number (re, im).

    Returns:
        Tuple of two complex numbers (z1, z2).

    Example:
        >>> z1, z2 = inverse_joukowski((2.5, 0))
        >>> round(z1[0], 4)
        2.0

    Complexity: O(1)
    """
    # w^2 - 4
    w2_re = w[0] * w[0] - w[1] * w[1] - 4.0
    w2_im = 2.0 * w[0] * w[1]

    # sqrt(w^2 - 4) via polar form
    r = math.sqrt(w2_re * w2_re + w2_im * w2_im)
    theta = math.atan2(w2_im, w2_re)
    sr = math.sqrt(r)
    s_re = sr * math.cos(theta / 2.0)
    s_im = sr * math.sin(theta / 2.0)

    z1 = ((w[0] + s_re) / 2.0, (w[1] + s_im) / 2.0)
    z2 = ((w[0] - s_re) / 2.0, (w[1] - s_im) / 2.0)
    return (z1, z2)


def power_map(z: Tuple[float, float], n: float) -> Tuple[float, float]:
    """Conformal power map w = z^n.

    Maps sectors to half-planes when n is chosen appropriately.

    Args:
        z: Input complex number (re, im).
        n: Exponent (real).

    Returns:
        Result w as (re, im).

    Example:
        >>> re, im = power_map((0, 1), 2)
        >>> (round(re, 6), round(im, 6))
        (-1.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(n, "n")
    r = math.sqrt(z[0] * z[0] + z[1] * z[1])

    if r < 1e-30:
        return (0.0, 0.0)

    theta = math.atan2(z[1], z[0])
    rn = r ** n
    return (rn * math.cos(n * theta), rn * math.sin(n * theta))


def exponential_map(z: Tuple[float, float]) -> Tuple[float, float]:
    """Conformal exponential map w = e^z.

    Maps horizontal strips to sectors/annuli.

    Args:
        z: Input complex number (re, im).

    Returns:
        Result w as (re, im).

    Example:
        >>> re, im = exponential_map((0, 3.14159265))
        >>> (round(re, 4), round(im, 4))
        (-1.0, 0.0)

    Complexity: O(1)
    """
    mag = math.exp(z[0])
    return (mag * math.cos(z[1]), mag * math.sin(z[1]))


def log_map(z: Tuple[float, float]) -> Tuple[float, float]:
    """Principal branch of the complex logarithm w = Log(z).

    Maps the punctured plane to a horizontal strip of width 2π.

    Args:
        z: Input complex number (re, im). Must not be (0, 0).

    Returns:
        Result w as (re, im) where im is in (-π, π].

    Raises:
        ValueError: If z = 0.

    Example:
        >>> re, im = log_map((1, 0))
        >>> (round(re, 6), round(im, 6))
        (0.0, 0.0)

    Complexity: O(1)
    """
    r2 = z[0] * z[0] + z[1] * z[1]

    if r2 < 1e-30:
        raise ValueError("z must not be zero.")

    return (math.log(math.sqrt(r2)), math.atan2(z[1], z[0]))


def inversion_map(z: Tuple[float, float]) -> Tuple[float, float]:
    """Complex inversion w = 1/z.

    Fundamental conformal mapping exchanging interior and exterior of unit circle.

    Args:
        z: Input complex number (re, im). Must not be (0, 0).

    Returns:
        Result w as (re, im).

    Raises:
        ValueError: If z = 0.

    Example:
        >>> inversion_map((0, 1))
        (0.0, -1.0)

    Complexity: O(1)
    """
    r2 = z[0] * z[0] + z[1] * z[1]

    if r2 < 1e-30:
        raise ValueError("z must not be zero.")

    return (z[0] / r2, -z[1] / r2)


def schwarz_christoffel_half_plane_to_rectangle(
    z: Tuple[float, float], k: float
) -> Tuple[float, float]:
    """Approximate Schwarz-Christoffel map from upper half-plane to a rectangle.

    Uses the incomplete elliptic integral F(arcsin(z), k) for the mapping.
    This is a simplified version for real z on [0, 1].

    Args:
        z: Point in the z-plane (re, im). For basic use, im should be small.
        k: Modulus of the elliptic function, 0 < k < 1.

    Returns:
        Approximate mapped point w as (re, im).

    Example:
        >>> re, im = schwarz_christoffel_half_plane_to_rectangle((0.5, 0), 0.5)
        >>> isinstance(re, float)
        True

    Complexity: O(n) numerical quadrature.
    """
    _check_numeric(k, "k")

    if k <= 0 or k >= 1:
        raise ValueError("k must be in (0, 1).")

    # Numerical integration of 1/sqrt((1-t^2)(1-k^2 t^2)) from 0 to z[0]
    x_val = z[0]

    if abs(x_val) < 1e-15:
        return (0.0, 0.0)

    n_pts = 50
    dt = x_val / n_pts
    total = 0.0

    for i in range(n_pts):
        t = (i + 0.5) * dt
        t2 = t * t

        denom = (1.0 - t2) * (1.0 - k * k * t2)

        if denom <= 0:
            break

        total += dt / math.sqrt(denom)

    return (total, z[1])


def cayley_transform(z: Tuple[float, float]) -> Tuple[float, float]:
    """Cayley transform w = (z - i) / (z + i).

    Maps the upper half-plane to the unit disk, sending i → 0.

    Args:
        z: Input complex number (re, im).

    Returns:
        Result w as (re, im).

    Raises:
        ValueError: If z + i = 0 (i.e. z = -i).

    Example:
        >>> cayley_transform((0, 1))
        (0.0, 0.0)

    Complexity: O(1)
    """
    # z - i
    num_re = z[0]
    num_im = z[1] - 1.0

    # z + i
    den_re = z[0]
    den_im = z[1] + 1.0

    denom = den_re * den_re + den_im * den_im

    if denom < 1e-30:
        raise ValueError("Transformation undefined at z = -i.")

    re = (num_re * den_re + num_im * den_im) / denom
    im = (num_im * den_re - num_re * den_im) / denom
    return (re, im)


def inverse_cayley_transform(w: Tuple[float, float]) -> Tuple[float, float]:
    """Inverse Cayley transform z = i(1 + w) / (1 - w).

    Maps the unit disk back to the upper half-plane.

    Args:
        w: Input complex number (re, im).

    Returns:
        Result z as (re, im).

    Raises:
        ValueError: If w = 1.

    Example:
        >>> z = inverse_cayley_transform((0, 0))
        >>> (round(z[0], 6), round(z[1], 6))
        (0.0, 1.0)

    Complexity: O(1)
    """
    # 1 + w
    p_re = 1.0 + w[0]
    p_im = w[1]

    # 1 - w
    q_re = 1.0 - w[0]
    q_im = -w[1]

    denom = q_re * q_re + q_im * q_im

    if denom < 1e-30:
        raise ValueError("Transformation undefined at w = 1.")

    # i * (p / q)
    div_re = (p_re * q_re + p_im * q_im) / denom
    div_im = (p_im * q_re - p_re * q_im) / denom

    # Multiply by i: (re, im) → (-im, re)
    return (-div_im, div_re)


def koebe_function(z: Tuple[float, float]) -> Tuple[float, float]:
    """Koebe function w = z / (1 - z)².

    The extremal function in the theory of univalent functions (Bieberbach conjecture).
    Maps the unit disk to C \\ (-∞, -1/4].

    Args:
        z: Input complex number (re, im) with |z| < 1.

    Returns:
        Result w as (re, im).

    Raises:
        ValueError: If 1 - z = 0.

    Example:
        >>> re, im = koebe_function((0.5, 0))
        >>> round(re, 4)
        2.0

    Complexity: O(1)
    """
    # 1 - z
    d_re = 1.0 - z[0]
    d_im = -z[1]

    # (1 - z)^2
    d2_re = d_re * d_re - d_im * d_im
    d2_im = 2.0 * d_re * d_im

    denom = d2_re * d2_re + d2_im * d2_im

    if denom < 1e-30:
        raise ValueError("Transformation undefined at z = 1.")

    # z / (1-z)^2
    re = (z[0] * d2_re + z[1] * d2_im) / denom
    im = (z[1] * d2_re - z[0] * d2_im) / denom
    return (re, im)
