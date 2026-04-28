"""Analytic geometry and solid geometry formulas.

Plane geometry (distances, areas, lines, conics), solid geometry (volumes,
surface areas), and spherical trigonometry from Spiegel's *Mathematical
Handbook of Formulas and Tables*.
"""

import math
from typing import List, Tuple


# ---------------------------------------------------------------------------
# 2-D point operations
# ---------------------------------------------------------------------------


def distance_2d(x1: float, y1: float, x2: float, y2: float) -> float:
    """Euclidean distance between two points in the plane.

    Args:
        x1, y1: First point.
        x2, y2: Second point.

    Returns:
        Distance d = sqrt((x2-x1)^2 + (y2-y1)^2).

    Example:
        >>> distance_2d(0, 0, 3, 4)
        5.0

    Complexity: O(1)
    """
    _check_numeric(x1, y1, x2, y2)
    return math.hypot(x2 - x1, y2 - y1)


def distance_3d(
    x1: float, y1: float, z1: float,
    x2: float, y2: float, z2: float,
) -> float:
    """Euclidean distance between two points in 3-D space.

    Args:
        x1, y1, z1: First point.
        x2, y2, z2: Second point.

    Returns:
        Distance.

    Example:
        >>> round(distance_3d(0, 0, 0, 1, 2, 2), 6)
        3.0

    Complexity: O(1)
    """
    _check_numeric(x1, y1, z1, x2, y2, z2)
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def midpoint_2d(
    x1: float, y1: float, x2: float, y2: float,
) -> Tuple[float, float]:
    """Midpoint of the segment connecting two 2-D points.

    Args:
        x1, y1: First point.
        x2, y2: Second point.

    Returns:
        Tuple (mx, my).

    Example:
        >>> midpoint_2d(0, 0, 4, 6)
        (2.0, 3.0)

    Complexity: O(1)
    """
    _check_numeric(x1, y1, x2, y2)
    return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)


def midpoint_3d(
    x1: float, y1: float, z1: float,
    x2: float, y2: float, z2: float,
) -> Tuple[float, float, float]:
    """Midpoint of the segment connecting two 3-D points.

    Args:
        x1, y1, z1: First point.
        x2, y2, z2: Second point.

    Returns:
        Tuple (mx, my, mz).

    Example:
        >>> midpoint_3d(0, 0, 0, 2, 4, 6)
        (1.0, 2.0, 3.0)

    Complexity: O(1)
    """
    _check_numeric(x1, y1, z1, x2, y2, z2)
    return ((x1 + x2) / 2.0, (y1 + y2) / 2.0, (z1 + z2) / 2.0)


def slope_two_points(x1: float, y1: float, x2: float, y2: float) -> float:
    """Slope of the line through two points (y2-y1)/(x2-x1).

    Args:
        x1, y1: First point.
        x2, y2: Second point.

    Returns:
        Slope m.

    Raises:
        ValueError: If x1 == x2 (vertical line).

    Example:
        >>> slope_two_points(0, 0, 2, 4)
        2.0

    Complexity: O(1)
    """
    _check_numeric(x1, y1, x2, y2)

    if x2 == x1:
        raise ValueError("Vertical line: slope is undefined (x1 == x2).")

    return (y2 - y1) / (x2 - x1)


def line_equation(
    x1: float, y1: float, x2: float, y2: float,
) -> Tuple[float, float, float]:
    """Returns coefficients (a, b, c) of the line ax + by + c = 0 through two points.

    Args:
        x1, y1: First point.
        x2, y2: Second point.

    Returns:
        Tuple (a, b, c).

    Raises:
        ValueError: If the two points are identical.

    Example:
        >>> line_equation(0, 0, 1, 1)
        (-1.0, 1.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(x1, y1, x2, y2)

    if x1 == x2 and y1 == y2:
        raise ValueError("Two distinct points are required.")

    a = -(y2 - y1)
    b = x2 - x1
    c = -(a * x1 + b * y1)
    return (float(a), float(b), float(c))


def point_to_line_distance(
    px: float, py: float, a: float, b: float, c: float,
) -> float:
    """Distance from point (px, py) to the line ax + by + c = 0.

    Args:
        px, py: Point coordinates.
        a, b, c: Line coefficients.

    Returns:
        Perpendicular distance.

    Raises:
        ValueError: If a == 0 and b == 0.

    Example:
        >>> round(point_to_line_distance(0, 0, 1, 1, -2), 6)
        1.414214

    Complexity: O(1)
    """
    _check_numeric(px, py, a, b, c)

    if a == 0 and b == 0:
        raise ValueError("a and b cannot both be zero.")

    return abs(a * px + b * py + c) / math.sqrt(a * a + b * b)


# ---------------------------------------------------------------------------
# Triangle formulas
# ---------------------------------------------------------------------------


def triangle_area_vertices(
    x1: float, y1: float,
    x2: float, y2: float,
    x3: float, y3: float,
) -> float:
    """Area of a triangle from its vertices using the Shoelace formula.

    Args:
        x1, y1: First vertex.
        x2, y2: Second vertex.
        x3, y3: Third vertex.

    Returns:
        Area >= 0.

    Example:
        >>> triangle_area_vertices(0, 0, 4, 0, 0, 3)
        6.0

    Complexity: O(1)
    """
    _check_numeric(x1, y1, x2, y2, x3, y3)
    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0


def heron_formula(a: float, b: float, c: float) -> float:
    """Area of a triangle from side lengths using Heron's formula.

    Args:
        a, b, c: Side lengths (all > 0, satisfying triangle inequality).

    Returns:
        Area.

    Raises:
        ValueError: If sides don't form a valid triangle.

    Example:
        >>> heron_formula(3, 4, 5)
        6.0

    Complexity: O(1)
    """
    _check_numeric(a, b, c)

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be > 0.")

    if a + b <= c or a + c <= b or b + c <= a:
        raise ValueError("Sides do not satisfy the triangle inequality.")

    s = (a + b + c) / 2.0
    return math.sqrt(s * (s - a) * (s - b) * (s - c))


def law_of_cosines_side(a: float, b: float, angle_c: float) -> float:
    """Finds side c using the law of cosines: c^2 = a^2 + b^2 - 2ab cos(C).

    Args:
        a: Side a.
        b: Side b.
        angle_c: Angle C opposite to side c, in radians.

    Returns:
        Length of side c.

    Example:
        >>> round(law_of_cosines_side(3, 4, math.pi / 2), 6)
        5.0

    Complexity: O(1)
    """
    _check_numeric(a, b, angle_c)

    if a <= 0 or b <= 0:
        raise ValueError("Sides must be > 0.")

    c_sq = a * a + b * b - 2.0 * a * b * math.cos(angle_c)
    return math.sqrt(max(0.0, c_sq))


def law_of_cosines_angle(a: float, b: float, c: float) -> float:
    """Finds angle C opposite to side c using the law of cosines.

    cos(C) = (a^2 + b^2 - c^2) / (2ab).

    Args:
        a, b, c: Side lengths forming a valid triangle.

    Returns:
        Angle C in radians.

    Example:
        >>> round(law_of_cosines_angle(3, 4, 5), 6)
        1.570796

    Complexity: O(1)
    """
    _check_numeric(a, b, c)

    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Side lengths must be > 0.")

    cos_c = (a * a + b * b - c * c) / (2.0 * a * b)
    cos_c = max(-1.0, min(1.0, cos_c))
    return math.acos(cos_c)


def law_of_sines_side(a: float, angle_a: float, angle_b: float) -> float:
    """Finds side b using the law of sines: b = a * sin(B) / sin(A).

    Args:
        a: Known side.
        angle_a: Angle opposite to side a (radians).
        angle_b: Angle opposite to the unknown side b (radians).

    Returns:
        Length of side b.

    Raises:
        ValueError: If sin(angle_a) == 0.

    Example:
        >>> round(law_of_sines_side(5, math.pi / 6, math.pi / 3), 6)
        8.660254

    Complexity: O(1)
    """
    _check_numeric(a, angle_a, angle_b)

    if a <= 0:
        raise ValueError("Side a must be > 0.")

    sin_a = math.sin(angle_a)

    if abs(sin_a) < 1e-15:
        raise ValueError("sin(angle_a) must not be zero.")

    return a * math.sin(angle_b) / sin_a


# ---------------------------------------------------------------------------
# Circle formulas
# ---------------------------------------------------------------------------


def circle_area(radius: float) -> float:
    """Area of a circle: pi * r^2.

    Args:
        radius: Radius (> 0).

    Returns:
        Area.

    Example:
        >>> round(circle_area(1), 6)
        3.141593

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    return math.pi * radius * radius


def circle_circumference(radius: float) -> float:
    """Circumference of a circle: 2 * pi * r.

    Args:
        radius: Radius (> 0).

    Returns:
        Circumference.

    Example:
        >>> round(circle_circumference(1), 6)
        6.283185

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    return 2.0 * math.pi * radius


def sector_area(radius: float, angle: float) -> float:
    """Area of a circular sector: (1/2) r^2 theta.

    Args:
        radius: Radius (> 0).
        angle: Central angle in radians (> 0).

    Returns:
        Area of the sector.

    Example:
        >>> round(sector_area(2, math.pi / 2), 6)
        3.141593

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_positive(angle, "angle")
    return 0.5 * radius * radius * angle


def arc_length(radius: float, angle: float) -> float:
    """Length of a circular arc: r * theta.

    Args:
        radius: Radius (> 0).
        angle: Central angle in radians (> 0).

    Returns:
        Arc length.

    Example:
        >>> round(arc_length(2, math.pi), 6)
        6.283185

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_positive(angle, "angle")
    return radius * angle


def segment_area(radius: float, angle: float) -> float:
    """Area of a circular segment: (r^2/2)(theta - sin(theta)).

    Args:
        radius: Radius (> 0).
        angle: Central angle in radians (> 0).

    Returns:
        Area of the segment.

    Example:
        >>> round(segment_area(2, math.pi), 6)
        6.283185

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_positive(angle, "angle")
    return 0.5 * radius * radius * (angle - math.sin(angle))


# ---------------------------------------------------------------------------
# Ellipse formulas
# ---------------------------------------------------------------------------


def ellipse_area(a: float, b: float) -> float:
    """Area of an ellipse: pi * a * b.

    Args:
        a: Semi-major axis (> 0).
        b: Semi-minor axis (> 0).

    Returns:
        Area.

    Example:
        >>> round(ellipse_area(3, 2), 6)
        18.849556

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    return math.pi * a * b


def ellipse_perimeter_approx(a: float, b: float) -> float:
    """Approximate perimeter of an ellipse using Ramanujan's second formula.

    P ≈ pi(a+b)(1 + 3h/(10 + sqrt(4 - 3h))), h = ((a-b)/(a+b))^2.

    Args:
        a: Semi-major axis (> 0).
        b: Semi-minor axis (> 0).

    Returns:
        Approximate perimeter.

    Example:
        >>> round(ellipse_perimeter_approx(3, 2), 4)
        15.8654

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    h = ((a - b) / (a + b)) ** 2
    return math.pi * (a + b) * (1.0 + 3.0 * h / (10.0 + math.sqrt(4.0 - 3.0 * h)))


def ellipse_eccentricity(a: float, b: float) -> float:
    """Eccentricity of an ellipse: e = sqrt(1 - (b/a)^2) where a >= b.

    Args:
        a: Semi-major axis (> 0).
        b: Semi-minor axis (> 0, <= a).

    Returns:
        Eccentricity in [0, 1).

    Example:
        >>> round(ellipse_eccentricity(5, 3), 6)
        0.8

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")

    if b > a:
        a, b = b, a

    return math.sqrt(1.0 - (b / a) ** 2)


# ---------------------------------------------------------------------------
# Polygon formulas
# ---------------------------------------------------------------------------


def polygon_area(vertices: List[Tuple[float, float]]) -> float:
    """Area of a simple polygon using the Shoelace formula.

    Args:
        vertices: List of (x, y) tuples in order. Minimum 3 vertices.

    Returns:
        Area >= 0.

    Raises:
        ValueError: If fewer than 3 vertices.

    Example:
        >>> polygon_area([(0, 0), (4, 0), (4, 3), (0, 3)])
        12.0

    Complexity: O(n)
    """
    if not isinstance(vertices, list) or len(vertices) < 3:
        raise ValueError("At least 3 vertices are required.")

    n = len(vertices)
    area = 0.0

    for i in range(n):
        j = (i + 1) % n
        area += vertices[i][0] * vertices[j][1]
        area -= vertices[j][0] * vertices[i][1]

    return abs(area) / 2.0


def regular_polygon_area(n_sides: int, side: float) -> float:
    """Area of a regular n-sided polygon: (n s^2) / (4 tan(pi/n)).

    Args:
        n_sides: Number of sides (>= 3).
        side: Side length (> 0).

    Returns:
        Area.

    Example:
        >>> round(regular_polygon_area(6, 1), 6)
        2.598076

    Complexity: O(1)
    """
    if not isinstance(n_sides, int):
        raise TypeError("n_sides must be an integer.")

    if n_sides < 3:
        raise ValueError("n_sides must be >= 3.")

    _check_positive(side, "side")
    return (n_sides * side * side) / (4.0 * math.tan(math.pi / n_sides))


def trapezoid_area(a: float, b: float, h: float) -> float:
    """Area of a trapezoid: (a + b) * h / 2.

    Args:
        a: First parallel side (> 0).
        b: Second parallel side (> 0).
        h: Height (> 0).

    Returns:
        Area.

    Example:
        >>> trapezoid_area(3, 5, 4)
        16.0

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    _check_positive(h, "h")
    return (a + b) * h / 2.0


def parallelogram_area(base: float, height: float) -> float:
    """Area of a parallelogram: base * height.

    Args:
        base: Base length (> 0).
        height: Height (> 0).

    Returns:
        Area.

    Example:
        >>> parallelogram_area(5, 3)
        15.0

    Complexity: O(1)
    """
    _check_positive(base, "base")
    _check_positive(height, "height")
    return base * height


# ---------------------------------------------------------------------------
# 3-D solid geometry
# ---------------------------------------------------------------------------


def sphere_volume(radius: float) -> float:
    """Volume of a sphere: (4/3) pi r^3.

    Args:
        radius: Radius (> 0).

    Returns:
        Volume.

    Example:
        >>> round(sphere_volume(1), 6)
        4.18879

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    return (4.0 / 3.0) * math.pi * radius ** 3


def sphere_surface_area(radius: float) -> float:
    """Surface area of a sphere: 4 pi r^2.

    Args:
        radius: Radius (> 0).

    Returns:
        Surface area.

    Example:
        >>> round(sphere_surface_area(1), 6)
        12.566371

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    return 4.0 * math.pi * radius * radius


def cylinder_volume(radius: float, height: float) -> float:
    """Volume of a right circular cylinder: pi r^2 h.

    Args:
        radius: Radius (> 0).
        height: Height (> 0).

    Returns:
        Volume.

    Example:
        >>> round(cylinder_volume(2, 5), 6)
        62.831853

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_positive(height, "height")
    return math.pi * radius * radius * height


def cylinder_surface_area(radius: float, height: float) -> float:
    """Total surface area of a right circular cylinder: 2 pi r (r + h).

    Args:
        radius: Radius (> 0).
        height: Height (> 0).

    Returns:
        Total surface area.

    Example:
        >>> round(cylinder_surface_area(2, 5), 6)
        87.964594

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_positive(height, "height")
    return 2.0 * math.pi * radius * (radius + height)


def cone_volume(radius: float, height: float) -> float:
    """Volume of a right circular cone: (1/3) pi r^2 h.

    Args:
        radius: Base radius (> 0).
        height: Height (> 0).

    Returns:
        Volume.

    Example:
        >>> round(cone_volume(3, 4), 6)
        37.699112

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_positive(height, "height")
    return (1.0 / 3.0) * math.pi * radius * radius * height


def cone_lateral_area(radius: float, slant_height: float) -> float:
    """Lateral surface area of a cone: pi r l.

    Args:
        radius: Base radius (> 0).
        slant_height: Slant height (> 0).

    Returns:
        Lateral surface area.

    Example:
        >>> round(cone_lateral_area(3, 5), 6)
        47.12389

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_positive(slant_height, "slant_height")
    return math.pi * radius * slant_height


def pyramid_volume(base_area: float, height: float) -> float:
    """Volume of a pyramid: (1/3) A_base h.

    Args:
        base_area: Area of the base (> 0).
        height: Perpendicular height (> 0).

    Returns:
        Volume.

    Example:
        >>> pyramid_volume(9, 4)
        12.0

    Complexity: O(1)
    """
    _check_positive(base_area, "base_area")
    _check_positive(height, "height")
    return base_area * height / 3.0


def torus_volume(major_r: float, minor_r: float) -> float:
    """Volume of a torus: 2 pi^2 R r^2.

    Args:
        major_r: Distance from center of tube to center of torus (> 0).
        minor_r: Radius of the tube (> 0).

    Returns:
        Volume.

    Example:
        >>> round(torus_volume(3, 1), 4)
        59.2176

    Complexity: O(1)
    """
    _check_positive(major_r, "major_r")
    _check_positive(minor_r, "minor_r")
    return 2.0 * math.pi ** 2 * major_r * minor_r ** 2


def torus_surface_area(major_r: float, minor_r: float) -> float:
    """Surface area of a torus: 4 pi^2 R r.

    Args:
        major_r: Major radius (> 0).
        minor_r: Minor radius (> 0).

    Returns:
        Surface area.

    Example:
        >>> round(torus_surface_area(3, 1), 4)
        118.4352

    Complexity: O(1)
    """
    _check_positive(major_r, "major_r")
    _check_positive(minor_r, "minor_r")
    return 4.0 * math.pi ** 2 * major_r * minor_r


def frustum_volume(r1: float, r2: float, height: float) -> float:
    """Volume of a frustum (truncated cone): (pi h / 3)(r1^2 + r1*r2 + r2^2).

    Args:
        r1: Top radius (>= 0).
        r2: Bottom radius (>= 0).
        height: Height (> 0).

    Returns:
        Volume.

    Example:
        >>> round(frustum_volume(2, 4, 5), 4)
        146.608

    Complexity: O(1)
    """
    if not isinstance(r1, (int, float)) or not isinstance(r2, (int, float)):
        raise TypeError("Radii must be numeric.")

    if r1 < 0 or r2 < 0:
        raise ValueError("Radii must be >= 0.")

    _check_positive(height, "height")
    return (math.pi * height / 3.0) * (r1 ** 2 + r1 * r2 + r2 ** 2)


def ellipsoid_volume(a: float, b: float, c: float) -> float:
    """Volume of an ellipsoid: (4/3) pi a b c.

    Args:
        a, b, c: Semi-axes (all > 0).

    Returns:
        Volume.

    Example:
        >>> round(ellipsoid_volume(2, 3, 4), 4)
        100.531

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    _check_positive(c, "c")
    return (4.0 / 3.0) * math.pi * a * b * c


def spherical_cap_volume(radius: float, h: float) -> float:
    """Volume of a spherical cap: (pi h^2 / 3)(3R - h).

    Args:
        radius: Sphere radius (> 0).
        h: Height of cap (0 < h <= 2R).

    Returns:
        Volume.

    Raises:
        ValueError: If h <= 0 or h > 2*radius.

    Example:
        >>> round(spherical_cap_volume(5, 2), 4)
        54.4543

    Complexity: O(1)
    """
    _check_positive(radius, "radius")

    if not isinstance(h, (int, float)):
        raise TypeError("h must be numeric.")

    if h <= 0 or h > 2 * radius:
        raise ValueError("h must be in (0, 2*radius].")

    return (math.pi * h * h / 3.0) * (3.0 * radius - h)


# ---------------------------------------------------------------------------
# Spherical trigonometry
# ---------------------------------------------------------------------------


def haversine_distance(
    lat1: float, lon1: float, lat2: float, lon2: float,
    radius: float = 6371.0,
) -> float:
    """Great-circle distance between two points on a sphere (Haversine formula).

    Args:
        lat1, lon1: Latitude and longitude of point 1 (degrees).
        lat2, lon2: Latitude and longitude of point 2 (degrees).
        radius: Sphere radius (default: Earth's mean radius in km).

    Returns:
        Distance in the same units as radius.

    Example:
        >>> round(haversine_distance(40.7128, -74.0060, 51.5074, -0.1278), 0)
        5570.0

    Complexity: O(1)
    """
    _check_numeric(lat1, lon1, lat2, lon2, radius)
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlam = math.radians(lon2 - lon1)
    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlam / 2) ** 2
    return 2 * radius * math.asin(math.sqrt(a))


def spherical_law_of_cosines(a: float, b: float, angle_c: float) -> float:
    """Spherical law of cosines: cos(c) = cos(a)cos(b) + sin(a)sin(b)cos(C).

    All arcs and angles in radians.

    Args:
        a: Arc a (radians).
        b: Arc b (radians).
        angle_c: Angle C (radians).

    Returns:
        Arc c (radians).

    Example:
        >>> round(spherical_law_of_cosines(0.5, 0.6, 1.0), 6)
        0.730989

    Complexity: O(1)
    """
    _check_numeric(a, b, angle_c)
    cos_c = math.cos(a) * math.cos(b) + math.sin(a) * math.sin(b) * math.cos(angle_c)
    cos_c = max(-1.0, min(1.0, cos_c))
    return math.acos(cos_c)


def spherical_excess(a: float, b: float, c: float) -> float:
    """Spherical excess of a spherical triangle (L'Huilier's theorem).

    The area of a spherical triangle on a unit sphere equals the spherical excess.

    Args:
        a, b, c: Arcs (sides) of the spherical triangle in radians.

    Returns:
        Spherical excess E in radians.

    Example:
        >>> round(spherical_excess(math.pi/2, math.pi/2, math.pi/2), 6)
        1.570796

    Complexity: O(1)
    """
    _check_numeric(a, b, c)
    s = (a + b + c) / 2.0
    tan_e4 = math.sqrt(
        abs(
            math.tan(s / 2)
            * math.tan((s - a) / 2)
            * math.tan((s - b) / 2)
            * math.tan((s - c) / 2)
        )
    )
    return 4.0 * math.atan(tan_e4)


# ---------------------------------------------------------------------------
# Conic sections
# ---------------------------------------------------------------------------


def parabola_focus(a: float) -> Tuple[float, float]:
    """Focus of the parabola y = ax^2: located at (0, 1/(4a)).

    Args:
        a: Coefficient of x^2 (a != 0).

    Returns:
        Tuple (0, 1/(4a)).

    Example:
        >>> parabola_focus(1)
        (0, 0.25)

    Complexity: O(1)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be numeric.")

    if a == 0:
        raise ValueError("a must not be zero.")

    return (0, 1.0 / (4.0 * a))


def parabola_directrix(a: float) -> float:
    """Directrix of the parabola y = ax^2: y = -1/(4a).

    Args:
        a: Coefficient of x^2 (a != 0).

    Returns:
        y-coordinate of the directrix.

    Example:
        >>> parabola_directrix(1)
        -0.25

    Complexity: O(1)
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be numeric.")

    if a == 0:
        raise ValueError("a must not be zero.")

    return -1.0 / (4.0 * a)


def hyperbola_eccentricity(a: float, b: float) -> float:
    """Eccentricity of a hyperbola: e = sqrt(1 + (b/a)^2).

    Args:
        a: Semi-transverse axis (> 0).
        b: Semi-conjugate axis (> 0).

    Returns:
        Eccentricity (> 1).

    Example:
        >>> round(hyperbola_eccentricity(3, 4), 6)
        1.666667

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    return math.sqrt(1.0 + (b / a) ** 2)


def hyperbola_asymptotes(a: float, b: float) -> Tuple[float, float]:
    """Slopes of the asymptotes of x^2/a^2 - y^2/b^2 = 1.

    Returns:
        Tuple (b/a, -b/a).

    Example:
        >>> hyperbola_asymptotes(3, 4)
        (1.3333333333333333, -1.3333333333333333)

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    m = b / a
    return (m, -m)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_numeric(*values: float) -> None:
    """Raises TypeError if any value is not numeric."""

    for v in values:

        if not isinstance(v, (int, float)):
            raise TypeError(f"All arguments must be numeric, got {type(v).__name__}.")


def _check_positive(value: float, name: str) -> None:
    """Raises ValueError if value is not positive."""
    _check_numeric(value)

    if value <= 0:
        raise ValueError(f"{name} must be > 0.")


# ---------------------------------------------------------------------------
# Phase 21 – Batch 25: Geometry Functions (1 of 3)
# ---------------------------------------------------------------------------

def annulus_area(outer_radius: float, inner_radius: float) -> float:
    """Compute the area of an annulus (ring).

    A = π(R² - r²)

    Args:
        outer_radius: Outer radius R.
        inner_radius: Inner radius r.

    Returns:
        Area of the annulus.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radii are negative or inner ≥ outer.

    Usage Example:
        >>> round(annulus_area(5.0, 3.0), 4)
        50.2655

    Complexity: O(1)
    """
    _check_numeric(outer_radius, inner_radius)
    outer_radius, inner_radius = float(outer_radius), float(inner_radius)
    if outer_radius < 0 or inner_radius < 0:
        raise ValueError("Radii must be non-negative.")
    if inner_radius >= outer_radius:
        raise ValueError("inner_radius must be less than outer_radius.")
    import math
    return math.pi * (outer_radius ** 2 - inner_radius ** 2)


def circular_ring_perimeter(outer_radius: float, inner_radius: float) -> float:
    """Compute the perimeter of an annulus (both circles).

    P = 2π(R + r)

    Args:
        outer_radius: Outer radius R.
        inner_radius: Inner radius r.

    Returns:
        Total perimeter.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radii are negative or inner ≥ outer.

    Usage Example:
        >>> round(circular_ring_perimeter(5.0, 3.0), 4)
        50.2655

    Complexity: O(1)
    """
    _check_numeric(outer_radius, inner_radius)
    outer_radius, inner_radius = float(outer_radius), float(inner_radius)
    if outer_radius < 0 or inner_radius < 0:
        raise ValueError("Radii must be non-negative.")
    if inner_radius >= outer_radius:
        raise ValueError("inner_radius must be less than outer_radius.")
    import math
    return 2.0 * math.pi * (outer_radius + inner_radius)


def rhombus_area(d1: float, d2: float) -> float:
    """Compute the area of a rhombus from its diagonals.

    A = (d1 × d2) / 2

    Args:
        d1: Length of first diagonal.
        d2: Length of second diagonal.

    Returns:
        Area of the rhombus.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If either diagonal ≤ 0.

    Usage Example:
        >>> rhombus_area(6.0, 8.0)
        24.0

    Complexity: O(1)
    """
    _check_positive(d1, "d1")
    _check_positive(d2, "d2")
    return float(d1) * float(d2) / 2.0


def rhombus_perimeter(side: float) -> float:
    """Compute the perimeter of a rhombus.

    P = 4 × side

    Args:
        side: Side length.

    Returns:
        Perimeter.

    Raises:
        TypeError: If side is not numeric.
        ValueError: If side ≤ 0.

    Usage Example:
        >>> rhombus_perimeter(5.0)
        20.0

    Complexity: O(1)
    """
    _check_positive(side, "side")
    return 4.0 * float(side)


def regular_polygon_perimeter(n: int, side: float) -> float:
    """Compute the perimeter of a regular polygon.

    P = n × side

    Args:
        n: Number of sides (≥ 3).
        side: Side length.

    Returns:
        Perimeter.

    Raises:
        TypeError: If n is not int or side is not numeric.
        ValueError: If n < 3 or side ≤ 0.

    Usage Example:
        >>> regular_polygon_perimeter(6, 5.0)
        30.0

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 3:
        raise ValueError("n must be >= 3.")
    _check_positive(side, "side")
    return float(n) * float(side)


def regular_polygon_interior_angle(n: int) -> float:
    """Compute the interior angle of a regular n-gon in degrees.

    angle = (n - 2) × 180 / n

    Args:
        n: Number of sides (≥ 3).

    Returns:
        Interior angle in degrees.

    Raises:
        TypeError: If n is not int.
        ValueError: If n < 3.

    Usage Example:
        >>> regular_polygon_interior_angle(6)
        120.0

    Complexity: O(1)
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 3:
        raise ValueError("n must be >= 3.")
    return (n - 2) * 180.0 / n


def tetrahedron_surface_area(edge: float) -> float:
    """Compute the surface area of a regular tetrahedron.

    SA = √3 × edge²

    Args:
        edge: Edge length.

    Returns:
        Surface area.

    Raises:
        TypeError: If edge is not numeric.
        ValueError: If edge ≤ 0.

    Usage Example:
        >>> round(tetrahedron_surface_area(1.0), 4)
        1.7321

    Complexity: O(1)
    """
    _check_positive(edge, "edge")
    import math
    e = float(edge)
    return math.sqrt(3.0) * e * e


def prism_volume(base_area: float, height: float) -> float:
    """Compute the volume of a prism.

    V = base_area × height

    Args:
        base_area: Area of the base.
        height: Height of the prism.

    Returns:
        Volume.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If arguments ≤ 0.

    Usage Example:
        >>> prism_volume(25.0, 10.0)
        250.0

    Complexity: O(1)
    """
    _check_positive(base_area, "base_area")
    _check_positive(height, "height")
    return float(base_area) * float(height)


def prism_surface_area(base_area: float, base_perimeter: float, height: float) -> float:
    """Compute the surface area of a prism.

    SA = 2·base_area + base_perimeter·height

    Args:
        base_area: Area of the base.
        base_perimeter: Perimeter of the base.
        height: Height of the prism.

    Returns:
        Surface area.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If arguments ≤ 0.

    Usage Example:
        >>> prism_surface_area(25.0, 20.0, 10.0)
        250.0

    Complexity: O(1)
    """
    _check_positive(base_area, "base_area")
    _check_positive(base_perimeter, "base_perimeter")
    _check_positive(height, "height")
    return 2.0 * float(base_area) + float(base_perimeter) * float(height)


def tetrahedron_volume(edge: float) -> float:
    """Compute the volume of a regular tetrahedron.

    V = edge³ / (6√2)

    Args:
        edge: Edge length.

    Returns:
        Volume.

    Raises:
        TypeError: If edge is not numeric.
        ValueError: If edge ≤ 0.

    Usage Example:
        >>> round(tetrahedron_volume(1.0), 4)
        0.1179

    Complexity: O(1)
    """
    _check_positive(edge, "edge")
    import math
    e = float(edge)
    return e ** 3 / (6.0 * math.sqrt(2.0))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 26: Geometry Functions (2 of 3)
# ---------------------------------------------------------------------------

def octahedron_volume(edge: float) -> float:
    """Compute the volume of a regular octahedron.

    V = (√2 / 3) × edge³

    Args:
        edge: Edge length.

    Returns:
        Volume.

    Raises:
        TypeError: If edge is not numeric.
        ValueError: If edge ≤ 0.

    Usage Example:
        >>> round(octahedron_volume(1.0), 4)
        0.4714

    Complexity: O(1)
    """
    _check_positive(edge, "edge")
    import math
    e = float(edge)
    return math.sqrt(2.0) / 3.0 * e ** 3


def octahedron_surface_area(edge: float) -> float:
    """Compute the surface area of a regular octahedron.

    SA = 2√3 × edge²

    Args:
        edge: Edge length.

    Returns:
        Surface area.

    Raises:
        TypeError: If edge is not numeric.
        ValueError: If edge ≤ 0.

    Usage Example:
        >>> round(octahedron_surface_area(1.0), 4)
        3.4641

    Complexity: O(1)
    """
    _check_positive(edge, "edge")
    import math
    e = float(edge)
    return 2.0 * math.sqrt(3.0) * e * e


def dodecahedron_volume(edge: float) -> float:
    """Compute the volume of a regular dodecahedron.

    V = (15 + 7√5) / 4 × edge³

    Args:
        edge: Edge length.

    Returns:
        Volume.

    Raises:
        TypeError: If edge is not numeric.
        ValueError: If edge ≤ 0.

    Usage Example:
        >>> round(dodecahedron_volume(1.0), 4)
        7.6631

    Complexity: O(1)
    """
    _check_positive(edge, "edge")
    import math
    e = float(edge)
    return (15.0 + 7.0 * math.sqrt(5.0)) / 4.0 * e ** 3


def dodecahedron_surface_area(edge: float) -> float:
    """Compute the surface area of a regular dodecahedron.

    SA = 3√(25 + 10√5) × edge²

    Args:
        edge: Edge length.

    Returns:
        Surface area.

    Raises:
        TypeError: If edge is not numeric.
        ValueError: If edge ≤ 0.

    Usage Example:
        >>> round(dodecahedron_surface_area(1.0), 4)
        20.6457

    Complexity: O(1)
    """
    _check_positive(edge, "edge")
    import math
    e = float(edge)
    return 3.0 * math.sqrt(25.0 + 10.0 * math.sqrt(5.0)) * e * e


def icosahedron_volume(edge: float) -> float:
    """Compute the volume of a regular icosahedron.

    V = (5(3 + √5) / 12) × edge³

    Args:
        edge: Edge length.

    Returns:
        Volume.

    Raises:
        TypeError: If edge is not numeric.
        ValueError: If edge ≤ 0.

    Usage Example:
        >>> round(icosahedron_volume(1.0), 4)
        2.1817

    Complexity: O(1)
    """
    _check_positive(edge, "edge")
    import math
    e = float(edge)
    return 5.0 * (3.0 + math.sqrt(5.0)) / 12.0 * e ** 3


def icosahedron_surface_area(edge: float) -> float:
    """Compute the surface area of a regular icosahedron.

    SA = 5√3 × edge²

    Args:
        edge: Edge length.

    Returns:
        Surface area.

    Raises:
        TypeError: If edge is not numeric.
        ValueError: If edge ≤ 0.

    Usage Example:
        >>> round(icosahedron_surface_area(1.0), 4)
        8.6603

    Complexity: O(1)
    """
    _check_positive(edge, "edge")
    import math
    e = float(edge)
    return 5.0 * math.sqrt(3.0) * e * e


def stadium_area(radius: float, straight_length: float) -> float:
    """Compute the area of a stadium (discorectangle).

    A = π·r² + 2·r·a

    Args:
        radius: Radius of the semicircular ends.
        straight_length: Length of the straight sides.

    Returns:
        Area.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius ≤ 0 or straight_length < 0.

    Usage Example:
        >>> round(stadium_area(2.0, 5.0), 4)
        32.5664

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_numeric(straight_length)
    straight_length = float(straight_length)
    if straight_length < 0:
        raise ValueError("straight_length must be non-negative.")
    import math
    r = float(radius)
    return math.pi * r * r + 2.0 * r * straight_length


def capsule_volume(radius: float, cylinder_length: float) -> float:
    """Compute the volume of a capsule (cylinder with hemispherical caps).

    V = π·r²·l + (4/3)π·r³

    Args:
        radius: Radius of the capsule.
        cylinder_length: Length of the cylindrical section.

    Returns:
        Volume.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius ≤ 0 or cylinder_length < 0.

    Usage Example:
        >>> round(capsule_volume(2.0, 5.0), 4)
        96.3422

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_numeric(cylinder_length)
    cylinder_length = float(cylinder_length)
    if cylinder_length < 0:
        raise ValueError("cylinder_length must be non-negative.")
    import math
    r = float(radius)
    return math.pi * r * r * cylinder_length + 4.0 / 3.0 * math.pi * r ** 3


def capsule_surface_area(radius: float, cylinder_length: float) -> float:
    """Compute the surface area of a capsule.

    SA = 2π·r·l + 4π·r²

    Args:
        radius: Radius of the capsule.
        cylinder_length: Length of the cylindrical section.

    Returns:
        Surface area.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius ≤ 0 or cylinder_length < 0.

    Usage Example:
        >>> round(capsule_surface_area(2.0, 5.0), 4)
        113.0973

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_numeric(cylinder_length)
    cylinder_length = float(cylinder_length)
    if cylinder_length < 0:
        raise ValueError("cylinder_length must be non-negative.")
    import math
    r = float(radius)
    return 2.0 * math.pi * r * cylinder_length + 4.0 * math.pi * r * r


def shoelace_area(vertices: list[tuple[float, float]]) -> float:
    """Compute the area of a simple polygon using the shoelace formula.

    Args:
        vertices: List of (x, y) tuples forming the polygon (≥ 3 vertices).

    Returns:
        Absolute area.

    Raises:
        TypeError: If vertices is not a list of tuples.
        ValueError: If fewer than 3 vertices.

    Usage Example:
        >>> shoelace_area([(0, 0), (4, 0), (4, 3), (0, 3)])
        12.0

    Complexity: O(n)
    """
    if not isinstance(vertices, list):
        raise TypeError("vertices must be a list of (x, y) tuples.")
    if len(vertices) < 3:
        raise ValueError("At least 3 vertices required.")
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = float(vertices[i][0]), float(vertices[i][1])
        x2, y2 = float(vertices[(i + 1) % n][0]), float(vertices[(i + 1) % n][1])
        area += x1 * y2 - x2 * y1
    return abs(area) / 2.0


# ---------------------------------------------------------------------------
# Phase 21 – Batch 27: Geometry Functions (3 of 3)
# ---------------------------------------------------------------------------

def polygon_centroid(vertices: list[tuple[float, float]]) -> tuple[float, float]:
    """Compute the centroid of a simple polygon.

    Args:
        vertices: List of (x, y) tuples forming the polygon (≥ 3 vertices).

    Returns:
        Tuple (cx, cy) centroid coordinates.

    Raises:
        TypeError: If vertices is not a list.
        ValueError: If fewer than 3 vertices or polygon has zero area.

    Usage Example:
        >>> polygon_centroid([(0, 0), (4, 0), (4, 3), (0, 3)])
        (2.0, 1.5)

    Complexity: O(n)
    """
    if not isinstance(vertices, list):
        raise TypeError("vertices must be a list of (x, y) tuples.")
    if len(vertices) < 3:
        raise ValueError("At least 3 vertices required.")
    n = len(vertices)
    signed_area = 0.0
    cx = 0.0
    cy = 0.0
    for i in range(n):
        x0, y0 = float(vertices[i][0]), float(vertices[i][1])
        x1, y1 = float(vertices[(i + 1) % n][0]), float(vertices[(i + 1) % n][1])
        cross = x0 * y1 - x1 * y0
        signed_area += cross
        cx += (x0 + x1) * cross
        cy += (y0 + y1) * cross
    signed_area /= 2.0
    if abs(signed_area) < 1e-15:
        raise ValueError("Polygon has zero area.")
    cx /= (6.0 * signed_area)
    cy /= (6.0 * signed_area)
    return (cx, cy)


def spherical_cap_surface_area(radius: float, height: float) -> float:
    """Compute the curved surface area of a spherical cap.

    SA = 2π·R·h

    Args:
        radius: Radius of the sphere.
        height: Height of the cap.

    Returns:
        Curved surface area.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius ≤ 0 or height not in (0, 2R].

    Usage Example:
        >>> round(spherical_cap_surface_area(5.0, 2.0), 4)
        62.8319

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_numeric(height)
    radius, height = float(radius), float(height)
    if height <= 0 or height > 2.0 * radius:
        raise ValueError("height must be in (0, 2·radius].")
    import math
    return 2.0 * math.pi * radius * height


def cone_slant_height(radius: float, height: float) -> float:
    """Compute the slant height of a cone.

    l = √(r² + h²)

    Args:
        radius: Base radius.
        height: Height of the cone.

    Returns:
        Slant height.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If radius ≤ 0 or height ≤ 0.

    Usage Example:
        >>> cone_slant_height(3.0, 4.0)
        5.0

    Complexity: O(1)
    """
    _check_positive(radius, "radius")
    _check_positive(height, "height")
    import math
    return math.sqrt(float(radius) ** 2 + float(height) ** 2)


def pyramid_surface_area(base_area: float, base_perimeter: float, slant_height: float) -> float:
    """Compute the surface area of a regular pyramid.

    SA = base_area + (base_perimeter × slant_height) / 2

    Args:
        base_area: Area of the base.
        base_perimeter: Perimeter of the base.
        slant_height: Slant height of the pyramid.

    Returns:
        Total surface area.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If any argument ≤ 0.

    Usage Example:
        >>> pyramid_surface_area(16.0, 16.0, 5.0)
        56.0

    Complexity: O(1)
    """
    _check_positive(base_area, "base_area")
    _check_positive(base_perimeter, "base_perimeter")
    _check_positive(slant_height, "slant_height")
    return float(base_area) + float(base_perimeter) * float(slant_height) / 2.0


def cuboid_space_diagonal(a: float, b: float, c: float) -> float:
    """Compute the space diagonal of a cuboid.

    d = √(a² + b² + c²)

    Args:
        a: Length.
        b: Width.
        c: Height.

    Returns:
        Space diagonal.

    Raises:
        TypeError: If arguments are not numeric.
        ValueError: If any dimension ≤ 0.

    Usage Example:
        >>> round(cuboid_space_diagonal(3.0, 4.0, 5.0), 4)
        7.0711

    Complexity: O(1)
    """
    _check_positive(a, "a")
    _check_positive(b, "b")
    _check_positive(c, "c")
    import math
    return math.sqrt(float(a) ** 2 + float(b) ** 2 + float(c) ** 2)
