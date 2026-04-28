"""Coordinate system conversions.

Conversions between Cartesian and curvilinear coordinate systems from
Murray R. Spiegel's *Mathematical Handbook of Formulas and Tables*:
cylindrical, toroidal, parabolic cylindrical, paraboloidal, elliptic
cylindrical, oblate/prolate spheroidal, and bipolar coordinates.
"""

import math
from typing import Tuple


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_numeric(value: object, name: str = "value") -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric.")


def _check_positive(value: float, name: str = "value") -> None:
    if value < 0:
        raise ValueError(f"{name} must be non-negative.")


# ---------------------------------------------------------------------------
# Cylindrical coordinates
# ---------------------------------------------------------------------------


def cartesian_to_cylindrical(
    x: float, y: float, z: float
) -> Tuple[float, float, float]:
    """Converts Cartesian (x, y, z) to cylindrical (rho, phi, z).

    rho = sqrt(x² + y²), phi = atan2(y, x), z = z.

    Args:
        x: Cartesian x.
        y: Cartesian y.
        z: Cartesian z.

    Returns:
        Tuple (rho, phi, z) where phi is in (-π, π].

    Example:
        >>> rho, phi, z = cartesian_to_cylindrical(1, 1, 5)
        >>> (round(rho, 6), round(phi, 6), z)
        (1.414214, 0.785398, 5)

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_numeric(y, "y")
    _check_numeric(z, "z")
    rho = math.sqrt(x * x + y * y)
    phi = math.atan2(y, x)
    return (rho, phi, z)


def cylindrical_to_cartesian(
    rho: float, phi: float, z: float
) -> Tuple[float, float, float]:
    """Converts cylindrical (rho, phi, z) to Cartesian (x, y, z).

    x = rho cos(phi), y = rho sin(phi), z = z.

    Args:
        rho: Radial distance (>= 0).
        phi: Azimuthal angle in radians.
        z: Height.

    Returns:
        Tuple (x, y, z).

    Example:
        >>> x, y, z = cylindrical_to_cartesian(2, math.pi / 4, 3)
        >>> (round(x, 6), round(y, 6), z)
        (1.414214, 1.414214, 3)

    Complexity: O(1)
    """
    _check_numeric(rho, "rho")
    _check_numeric(phi, "phi")
    _check_numeric(z, "z")
    return (rho * math.cos(phi), rho * math.sin(phi), z)


# ---------------------------------------------------------------------------
# Parabolic cylindrical coordinates
# ---------------------------------------------------------------------------


def parabolic_cylindrical_to_cartesian(
    u: float, v: float, z: float
) -> Tuple[float, float, float]:
    """Converts parabolic cylindrical (u, v, z) to Cartesian (x, y, z).

    x = (u² - v²)/2, y = uv, z = z.

    Args:
        u: First parabolic coordinate.
        v: Second parabolic coordinate (>= 0).
        z: Height.

    Returns:
        Tuple (x, y, z).

    Example:
        >>> x, y, z = parabolic_cylindrical_to_cartesian(2, 1, 0)
        >>> (x, y, z)
        (1.5, 2, 0)

    Complexity: O(1)
    """
    _check_numeric(u, "u")
    _check_numeric(v, "v")
    _check_numeric(z, "z")
    return (0.5 * (u * u - v * v), u * v, z)


def cartesian_to_parabolic_cylindrical(
    x: float, y: float, z: float
) -> Tuple[float, float, float]:
    """Converts Cartesian (x, y, z) to parabolic cylindrical (u, v, z).

    u = sqrt(sqrt(x² + y²) + x), v = sqrt(sqrt(x² + y²) - x) * sign(y).

    Args:
        x: Cartesian x.
        y: Cartesian y.
        z: Cartesian z.

    Returns:
        Tuple (u, v, z).

    Example:
        >>> u, v, z = cartesian_to_parabolic_cylindrical(1.5, 2, 0)
        >>> (round(u, 4), round(v, 4), z)
        (2.0, 1.0, 0)

    Complexity: O(1)
    """
    _check_numeric(x, "x")
    _check_numeric(y, "y")
    _check_numeric(z, "z")
    r = math.sqrt(x * x + y * y)
    u = math.sqrt(r + x)
    v_abs = math.sqrt(r - x)
    v = v_abs if y >= 0 else -v_abs
    return (u, v, z)


# ---------------------------------------------------------------------------
# Paraboloidal coordinates
# ---------------------------------------------------------------------------


def paraboloidal_to_cartesian(
    u: float, v: float, phi: float
) -> Tuple[float, float, float]:
    """Converts paraboloidal (u, v, phi) to Cartesian (x, y, z).

    x = u·v·cos(phi), y = u·v·sin(phi), z = (u² - v²)/2.

    Args:
        u: First paraboloidal coordinate (>= 0).
        v: Second paraboloidal coordinate (>= 0).
        phi: Azimuthal angle in radians.

    Returns:
        Tuple (x, y, z).

    Example:
        >>> x, y, z = paraboloidal_to_cartesian(1, 1, 0)
        >>> (x, y, z)
        (1, 0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(u, "u")
    _check_numeric(v, "v")
    _check_numeric(phi, "phi")
    return (u * v * math.cos(phi), u * v * math.sin(phi), 0.5 * (u * u - v * v))


# ---------------------------------------------------------------------------
# Elliptic cylindrical coordinates
# ---------------------------------------------------------------------------


def elliptic_cylindrical_to_cartesian(
    u: float, v: float, z: float, a: float = 1.0
) -> Tuple[float, float, float]:
    """Converts elliptic cylindrical (u, v, z) to Cartesian (x, y, z).

    x = a·cosh(u)·cos(v), y = a·sinh(u)·sin(v), z = z.

    Args:
        u: Radial-like coordinate (u >= 0).
        v: Angular coordinate in [0, 2π).
        z: Height.
        a: Semi-focal distance (default 1.0).

    Returns:
        Tuple (x, y, z).

    Example:
        >>> x, y, z = elliptic_cylindrical_to_cartesian(1, 0, 0, 1)
        >>> round(x, 6)
        1.543081

    Complexity: O(1)
    """
    _check_numeric(u, "u")
    _check_numeric(v, "v")
    _check_numeric(z, "z")
    _check_numeric(a, "a")
    return (a * math.cosh(u) * math.cos(v), a * math.sinh(u) * math.sin(v), z)


# ---------------------------------------------------------------------------
# Prolate spheroidal coordinates
# ---------------------------------------------------------------------------


def prolate_spheroidal_to_cartesian(
    xi: float, eta: float, phi: float, a: float = 1.0
) -> Tuple[float, float, float]:
    """Converts prolate spheroidal (ξ, η, φ) to Cartesian (x, y, z).

    x = a·sinh(ξ)·sin(η)·cos(φ), y = a·sinh(ξ)·sin(η)·sin(φ),
    z = a·cosh(ξ)·cos(η).

    Args:
        xi: Radial coordinate (ξ >= 0).
        eta: Angle η in [0, π].
        phi: Azimuthal angle in [0, 2π).
        a: Semi-focal distance (default 1.0).

    Returns:
        Tuple (x, y, z).

    Example:
        >>> x, y, z = prolate_spheroidal_to_cartesian(1, math.pi / 2, 0, 1)
        >>> (round(x, 6), round(y, 6), round(z, 6))
        (1.175201, 0.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(xi, "xi")
    _check_numeric(eta, "eta")
    _check_numeric(phi, "phi")
    _check_numeric(a, "a")

    sh_xi = math.sinh(xi)
    ch_xi = math.cosh(xi)
    s_eta = math.sin(eta)
    c_eta = math.cos(eta)
    return (
        a * sh_xi * s_eta * math.cos(phi),
        a * sh_xi * s_eta * math.sin(phi),
        a * ch_xi * c_eta,
    )


# ---------------------------------------------------------------------------
# Oblate spheroidal coordinates
# ---------------------------------------------------------------------------


def oblate_spheroidal_to_cartesian(
    xi: float, eta: float, phi: float, a: float = 1.0
) -> Tuple[float, float, float]:
    """Converts oblate spheroidal (ξ, η, φ) to Cartesian (x, y, z).

    x = a·cosh(ξ)·cos(η)·cos(φ), y = a·cosh(ξ)·cos(η)·sin(φ),
    z = a·sinh(ξ)·sin(η).

    Args:
        xi: Radial coordinate (ξ >= 0).
        eta: Angle η in [-π/2, π/2].
        phi: Azimuthal angle in [0, 2π).
        a: Semi-focal distance (default 1.0).

    Returns:
        Tuple (x, y, z).

    Example:
        >>> x, y, z = oblate_spheroidal_to_cartesian(1, 0, 0, 1)
        >>> (round(x, 6), round(y, 6), round(z, 6))
        (1.543081, 0.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(xi, "xi")
    _check_numeric(eta, "eta")
    _check_numeric(phi, "phi")
    _check_numeric(a, "a")

    ch_xi = math.cosh(xi)
    sh_xi = math.sinh(xi)
    c_eta = math.cos(eta)
    s_eta = math.sin(eta)
    return (
        a * ch_xi * c_eta * math.cos(phi),
        a * ch_xi * c_eta * math.sin(phi),
        a * sh_xi * s_eta,
    )


# ---------------------------------------------------------------------------
# Bipolar coordinates
# ---------------------------------------------------------------------------


def bipolar_to_cartesian(
    u: float, v: float, a: float = 1.0
) -> Tuple[float, float]:
    """Converts bipolar (u, v) to Cartesian (x, y).

    x = a·sinh(v) / (cosh(v) - cos(u)),
    y = a·sin(u) / (cosh(v) - cos(u)).

    Args:
        u: First bipolar coordinate (u ≠ 2πk).
        v: Second bipolar coordinate.
        a: Scale parameter (default 1.0).

    Returns:
        Tuple (x, y).

    Raises:
        ValueError: If denominator is zero.

    Example:
        >>> x, y = bipolar_to_cartesian(math.pi / 2, 1, 1)
        >>> round(x, 4)
        1.3131

    Complexity: O(1)
    """
    _check_numeric(u, "u")
    _check_numeric(v, "v")
    _check_numeric(a, "a")

    denom = math.cosh(v) - math.cos(u)

    if abs(denom) < 1e-15:
        raise ValueError("Denominator is zero (cosh(v) = cos(u)).")

    x = a * math.sinh(v) / denom
    y = a * math.sin(u) / denom
    return (x, y)


# ---------------------------------------------------------------------------
# Toroidal coordinates
# ---------------------------------------------------------------------------


def toroidal_to_cartesian(
    u: float, v: float, phi: float, a: float = 1.0
) -> Tuple[float, float, float]:
    """Converts toroidal (u, v, φ) to Cartesian (x, y, z).

    x = a·sinh(v)·cos(φ) / (cosh(v) - cos(u)),
    y = a·sinh(v)·sin(φ) / (cosh(v) - cos(u)),
    z = a·sin(u) / (cosh(v) - cos(u)).

    Args:
        u: Poloidal angle.
        v: Radial-like coordinate (v > 0).
        phi: Toroidal angle.
        a: Scale parameter (default 1.0).

    Returns:
        Tuple (x, y, z).

    Example:
        >>> x, y, z = toroidal_to_cartesian(0, 1, 0, 1)
        >>> round(x, 4)
        2.1640

    Complexity: O(1)
    """
    _check_numeric(u, "u")
    _check_numeric(v, "v")
    _check_numeric(phi, "phi")
    _check_numeric(a, "a")

    denom = math.cosh(v) - math.cos(u)

    if abs(denom) < 1e-15:
        raise ValueError("Denominator is zero.")

    factor = a / denom
    sh_v = math.sinh(v)
    return (
        factor * sh_v * math.cos(phi),
        factor * sh_v * math.sin(phi),
        factor * math.sin(u),
    )
