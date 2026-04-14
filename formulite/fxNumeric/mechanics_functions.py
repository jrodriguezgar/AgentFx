"""Moments of inertia, centroids, and section properties.

Classical formulas for mass properties and centroids of common geometric
shapes from Murray R. Spiegel's *Mathematical Handbook of Formulas and Tables*.
"""

import math
from typing import List, Tuple


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_positive(value: float, name: str = "value") -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric.")

    if value <= 0:
        raise ValueError(f"{name} must be positive.")


# ---------------------------------------------------------------------------
# Centroids (2D and 3D shapes)
# ---------------------------------------------------------------------------


def centroid_triangle(
    p1: Tuple[float, float],
    p2: Tuple[float, float],
    p3: Tuple[float, float]
) -> Tuple[float, float]:
    """Computes the centroid of a triangle given its vertices.

    Args:
        p1: First vertex (x, y).
        p2: Second vertex (x, y).
        p3: Third vertex (x, y).

    Returns:
        Centroid as (x, y).

    Example:
        >>> centroid_triangle((0, 0), (6, 0), (0, 6))
        (2.0, 2.0)

    Complexity: O(1)
    """
    return ((p1[0] + p2[0] + p3[0]) / 3.0, (p1[1] + p2[1] + p3[1]) / 3.0)


def centroid_polygon(vertices: List[Tuple[float, float]]) -> Tuple[float, float]:
    """Computes the centroid of a simple polygon using the Shoelace-derived formula.

    Args:
        vertices: Ordered list of (x, y) vertices (not repeated at end).

    Returns:
        Centroid as (x, y).

    Raises:
        ValueError: If polygon has fewer than 3 vertices or has zero area.

    Example:
        >>> centroid_polygon([(0, 0), (4, 0), (4, 4), (0, 4)])
        (2.0, 2.0)

    Complexity: O(n)
    """
    n = len(vertices)

    if n < 3:
        raise ValueError("Polygon must have at least 3 vertices.")

    area = 0.0
    cx = 0.0
    cy = 0.0

    for i in range(n):
        j = (i + 1) % n
        cross = vertices[i][0] * vertices[j][1] - vertices[j][0] * vertices[i][1]
        area += cross
        cx += (vertices[i][0] + vertices[j][0]) * cross
        cy += (vertices[i][1] + vertices[j][1]) * cross

    area *= 0.5

    if abs(area) < 1e-15:
        raise ValueError("Polygon has zero area.")

    factor = 1.0 / (6.0 * area)
    return (cx * factor, cy * factor)


def centroid_semicircle(r: float) -> Tuple[float, float]:
    """Returns the centroid of a semicircle of radius r lying above the x-axis.

    The centroid is at (0, 4r/(3π)) above the diameter.

    Args:
        r: Radius.

    Returns:
        Centroid as (0, y_c).

    Example:
        >>> _, y = centroid_semicircle(3)
        >>> round(y, 6)
        1.273240

    Complexity: O(1)
    """
    _check_positive(r, "r")
    return (0.0, 4.0 * r / (3.0 * math.pi))


def centroid_circular_sector(r: float, alpha: float) -> Tuple[float, float]:
    """Returns centroid distance from center of a circular sector.

    For a sector of half-angle α symmetric about x-axis, centroid is at
    (2r sin(α)/(3α), 0).

    Args:
        r: Radius.
        alpha: Half-angle of the sector in radians (0 < α <= π).

    Returns:
        Centroid as (x_c, 0).

    Example:
        >>> x, _ = centroid_circular_sector(3, math.pi / 2)
        >>> round(x, 6)
        1.273240

    Complexity: O(1)
    """
    _check_positive(r, "r")
    _check_positive(alpha, "alpha")
    return (2.0 * r * math.sin(alpha) / (3.0 * alpha), 0.0)


def centroid_cone(h: float) -> float:
    """Returns the height of the centroid of a solid cone above its base.

    The centroid is at h/4 from the base.

    Args:
        h: Height of the cone.

    Returns:
        Distance from base to centroid.

    Example:
        >>> centroid_cone(12)
        3.0

    Complexity: O(1)
    """
    _check_positive(h, "h")
    return h / 4.0


def centroid_hemisphere(r: float) -> float:
    """Returns the height of the centroid of a solid hemisphere above the flat face.

    The centroid is at 3r/8 from the base.

    Args:
        r: Radius.

    Returns:
        Distance from flat face to centroid.

    Example:
        >>> centroid_hemisphere(4)
        1.5

    Complexity: O(1)
    """
    _check_positive(r, "r")
    return 3.0 * r / 8.0


# ---------------------------------------------------------------------------
# Moments of inertia (area / second moment)
# ---------------------------------------------------------------------------


def moment_of_inertia_rectangle(b: float, h: float) -> Tuple[float, float]:
    """Computes the area moments of inertia of a rectangle about centroidal axes.

    I_x = bh³/12 (about horizontal axis), I_y = hb³/12 (about vertical axis).

    Args:
        b: Width (base).
        h: Height.

    Returns:
        Tuple (I_x, I_y).

    Example:
        >>> ix, iy = moment_of_inertia_rectangle(4, 6)
        >>> (ix, iy)
        (72.0, 32.0)

    Complexity: O(1)
    """
    _check_positive(b, "b")
    _check_positive(h, "h")
    return (b * h ** 3 / 12.0, h * b ** 3 / 12.0)


def moment_of_inertia_circle(r: float) -> float:
    """Computes the area moment of inertia of a circle about a diameter.

    I = πr⁴/4.

    Args:
        r: Radius.

    Returns:
        Moment of inertia I.

    Example:
        >>> round(moment_of_inertia_circle(2), 6)
        12.566371

    Complexity: O(1)
    """
    _check_positive(r, "r")
    return math.pi * r ** 4 / 4.0


def moment_of_inertia_annulus(r_outer: float, r_inner: float) -> float:
    """Computes the area moment of inertia of an annulus (hollow circle) about a diameter.

    I = π(R⁴ - r⁴)/4.

    Args:
        r_outer: Outer radius.
        r_inner: Inner radius (< r_outer).

    Returns:
        Moment of inertia I.

    Raises:
        ValueError: If r_inner >= r_outer.

    Example:
        >>> round(moment_of_inertia_annulus(3, 2), 6)
        50.267544

    Complexity: O(1)
    """
    _check_positive(r_outer, "r_outer")
    _check_positive(r_inner, "r_inner")

    if r_inner >= r_outer:
        raise ValueError("r_inner must be less than r_outer.")

    return math.pi * (r_outer ** 4 - r_inner ** 4) / 4.0


def moment_of_inertia_triangle(b: float, h: float) -> float:
    """Computes the area moment of inertia of a triangle about its base.

    I = bh³/12.

    Args:
        b: Base length.
        h: Height.

    Returns:
        Moment of inertia I about the base.

    Example:
        >>> moment_of_inertia_triangle(6, 4)
        32.0

    Complexity: O(1)
    """
    _check_positive(b, "b")
    _check_positive(h, "h")
    return b * h ** 3 / 12.0


def moment_of_inertia_triangle_centroidal(b: float, h: float) -> float:
    """Computes the area moment of inertia of a triangle about its centroidal axis.

    I = bh³/36.

    Args:
        b: Base length.
        h: Height.

    Returns:
        Moment of inertia I about centroidal axis parallel to base.

    Example:
        >>> round(moment_of_inertia_triangle_centroidal(6, 4), 6)
        10.666667

    Complexity: O(1)
    """
    _check_positive(b, "b")
    _check_positive(h, "h")
    return b * h ** 3 / 36.0


def moment_of_inertia_semicircle(r: float) -> float:
    """Computes the area moment of inertia of a semicircle about its diameter.

    I = πr⁴/8.

    Args:
        r: Radius.

    Returns:
        Moment of inertia I about the diameter.

    Example:
        >>> round(moment_of_inertia_semicircle(2), 6)
        6.283185

    Complexity: O(1)
    """
    _check_positive(r, "r")
    return math.pi * r ** 4 / 8.0


def moment_of_inertia_ellipse(a: float, b: float) -> Tuple[float, float]:
    """Computes the area moments of inertia of an ellipse about its centroidal axes.

    I_x = πab³/4 (about major axis), I_y = πa³b/4 (about minor axis).

    Args:
        a: Semi-axis along x.
        b: Semi-axis along y.

    Returns:
        Tuple (I_x, I_y).

    Example:
        >>> ix, iy = moment_of_inertia_ellipse(3, 2)
        >>> (round(ix, 6), round(iy, 6))
        (18.849556, 42.411501)

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    return (math.pi * a * b ** 3 / 4.0, math.pi * a ** 3 * b / 4.0)


# ---------------------------------------------------------------------------
# Mass moments of inertia (solid bodies)
# ---------------------------------------------------------------------------


def mass_moment_sphere(m: float, r: float) -> float:
    """Mass moment of inertia of a solid sphere about any diameter.

    I = (2/5)mr².

    Args:
        m: Mass.
        r: Radius.

    Returns:
        Moment of inertia I.

    Example:
        >>> mass_moment_sphere(10, 2)
        16.0

    Complexity: O(1)
    """
    _check_positive(m, "m")
    _check_positive(r, "r")
    return 2.0 * m * r * r / 5.0


def mass_moment_hollow_sphere(m: float, r: float) -> float:
    """Mass moment of inertia of a thin hollow sphere about any diameter.

    I = (2/3)mr².

    Args:
        m: Mass.
        r: Radius.

    Returns:
        Moment of inertia I.

    Example:
        >>> round(mass_moment_hollow_sphere(10, 2), 6)
        26.666667

    Complexity: O(1)
    """
    _check_positive(m, "m")
    _check_positive(r, "r")
    return 2.0 * m * r * r / 3.0


def mass_moment_cylinder(m: float, r: float) -> float:
    """Mass moment of inertia of a solid cylinder about its axis.

    I = mr²/2.

    Args:
        m: Mass.
        r: Radius.

    Returns:
        Moment of inertia I.

    Example:
        >>> mass_moment_cylinder(10, 2)
        20.0

    Complexity: O(1)
    """
    _check_positive(m, "m")
    _check_positive(r, "r")
    return m * r * r / 2.0


def mass_moment_cylinder_transverse(m: float, r: float, h: float) -> float:
    """Mass moment of inertia of a solid cylinder about a transverse centroidal axis.

    I = m(3r² + h²)/12.

    Args:
        m: Mass.
        r: Radius.
        h: Height.

    Returns:
        Moment of inertia I.

    Example:
        >>> round(mass_moment_cylinder_transverse(10, 2, 6), 6)
        40.0

    Complexity: O(1)
    """
    _check_positive(m, "m")
    _check_positive(r, "r")
    _check_positive(h, "h")
    return m * (3.0 * r * r + h * h) / 12.0


def mass_moment_rod(m: float, length: float) -> float:
    """Mass moment of inertia of a thin rod about its center (perpendicular axis).

    I = mL²/12.

    Args:
        m: Mass.
        length: Length of the rod.

    Returns:
        Moment of inertia I.

    Example:
        >>> round(mass_moment_rod(6, 4), 6)
        8.0

    Complexity: O(1)
    """
    _check_positive(m, "m")
    _check_positive(length, "length")
    return m * length * length / 12.0


def mass_moment_disk(m: float, r: float) -> float:
    """Mass moment of inertia of a thin uniform disk about its axis.

    I = mr²/2 (same as solid cylinder about axis).

    Args:
        m: Mass.
        r: Radius.

    Returns:
        Moment of inertia I.

    Example:
        >>> mass_moment_disk(10, 3)
        45.0

    Complexity: O(1)
    """
    _check_positive(m, "m")
    _check_positive(r, "r")
    return m * r * r / 2.0


def mass_moment_cone(m: float, r: float) -> float:
    """Mass moment of inertia of a solid cone about its axis.

    I = (3/10)mr².

    Args:
        m: Mass.
        r: Base radius.

    Returns:
        Moment of inertia I.

    Example:
        >>> mass_moment_cone(10, 2)
        12.0

    Complexity: O(1)
    """
    _check_positive(m, "m")
    _check_positive(r, "r")
    return 3.0 * m * r * r / 10.0


# ---------------------------------------------------------------------------
# Theorems
# ---------------------------------------------------------------------------


def parallel_axis_theorem(
    i_cm: float, m: float, d: float
) -> float:
    """Applies the parallel axis theorem: I = I_cm + md².

    Args:
        i_cm: Moment of inertia about the centroidal axis.
        m: Mass (or area for second moment of area).
        d: Distance between the two parallel axes.

    Returns:
        Moment of inertia about the new parallel axis.

    Example:
        >>> parallel_axis_theorem(8.0, 6, 3)
        62.0

    Complexity: O(1)
    """
    if not isinstance(i_cm, (int, float)):
        raise TypeError("i_cm must be numeric.")

    if not isinstance(m, (int, float)):
        raise TypeError("m must be numeric.")

    if not isinstance(d, (int, float)):
        raise TypeError("d must be numeric.")

    return i_cm + m * d * d


def radius_of_gyration(i: float, m: float) -> float:
    """Computes the radius of gyration k = sqrt(I/m).

    Args:
        i: Moment of inertia.
        m: Mass (or area).

    Returns:
        Radius of gyration.

    Example:
        >>> round(radius_of_gyration(48, 12), 6)
        2.0

    Complexity: O(1)
    """
    if not isinstance(i, (int, float)) or not isinstance(m, (int, float)):
        raise TypeError("i and m must be numeric.")

    if m <= 0:
        raise ValueError("m must be positive.")

    if i < 0:
        raise ValueError("i must be non-negative.")

    return math.sqrt(i / m)


def section_modulus(i: float, c: float) -> float:
    """Computes the section modulus S = I/c.

    Args:
        i: Moment of inertia about the neutral axis.
        c: Distance from neutral axis to extreme fiber.

    Returns:
        Section modulus S.

    Example:
        >>> section_modulus(72, 3)
        24.0

    Complexity: O(1)
    """
    if not isinstance(i, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("i and c must be numeric.")

    if c <= 0:
        raise ValueError("c must be positive.")

    return i / c


def polar_moment_of_inertia(ix: float, iy: float) -> float:
    """Computes the polar moment of inertia J = I_x + I_y.

    Args:
        ix: Moment of inertia about x-axis.
        iy: Moment of inertia about y-axis.

    Returns:
        Polar moment of inertia J.

    Example:
        >>> polar_moment_of_inertia(72, 32)
        104

    Complexity: O(1)
    """
    if not isinstance(ix, (int, float)) or not isinstance(iy, (int, float)):
        raise TypeError("ix and iy must be numeric.")

    return ix + iy
