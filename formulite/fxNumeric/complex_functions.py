"""Complex number operations and formulas.

Classical complex number formulas from Murray R. Spiegel's *Mathematical
Handbook of Formulas and Tables*: arithmetic, polar/rectangular conversion,
De Moivre's theorem, roots of unity, and Euler's formula.
"""

import math
from typing import List, Tuple


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def _check_numeric(value: object, name: str = "value") -> None:
    if not isinstance(value, (int, float)):
        raise TypeError(f"{name} must be numeric.")


# ---------------------------------------------------------------------------
# Basic complex arithmetic (on (re, im) tuples)
# ---------------------------------------------------------------------------


def complex_add(
    a: Tuple[float, float], b: Tuple[float, float]
) -> Tuple[float, float]:
    """Adds two complex numbers represented as (real, imag) tuples.

    Args:
        a: First complex number (re, im).
        b: Second complex number (re, im).

    Returns:
        Sum as (re, im).

    Example:
        >>> complex_add((1, 2), (3, 4))
        (4, 6)

    Complexity: O(1)
    """
    return (a[0] + b[0], a[1] + b[1])


def complex_subtract(
    a: Tuple[float, float], b: Tuple[float, float]
) -> Tuple[float, float]:
    """Subtracts complex number b from a.

    Args:
        a: First complex number (re, im).
        b: Second complex number (re, im).

    Returns:
        Difference as (re, im).

    Example:
        >>> complex_subtract((5, 3), (2, 1))
        (3, 2)

    Complexity: O(1)
    """
    return (a[0] - b[0], a[1] - b[1])


def complex_multiply(
    a: Tuple[float, float], b: Tuple[float, float]
) -> Tuple[float, float]:
    """Multiplies two complex numbers.

    (a+bi)(c+di) = (ac-bd) + (ad+bc)i

    Args:
        a: First complex number (re, im).
        b: Second complex number (re, im).

    Returns:
        Product as (re, im).

    Example:
        >>> complex_multiply((1, 2), (3, 4))
        (-5, 10)

    Complexity: O(1)
    """
    return (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])


def complex_divide(
    a: Tuple[float, float], b: Tuple[float, float]
) -> Tuple[float, float]:
    """Divides complex number a by b.

    Args:
        a: Numerator (re, im).
        b: Denominator (re, im).

    Returns:
        Quotient as (re, im).

    Raises:
        ZeroDivisionError: If b is zero.

    Example:
        >>> complex_divide((4, 2), (1, 1))
        (3.0, -1.0)

    Complexity: O(1)
    """
    denom = b[0] * b[0] + b[1] * b[1]

    if denom == 0:
        raise ZeroDivisionError("Cannot divide by zero complex number.")

    re = (a[0] * b[0] + a[1] * b[1]) / denom
    im = (a[1] * b[0] - a[0] * b[1]) / denom
    return (re, im)


def complex_modulus(z: Tuple[float, float]) -> float:
    """Computes the modulus (absolute value) of a complex number.

    |z| = sqrt(re² + im²)

    Args:
        z: Complex number (re, im).

    Returns:
        Modulus |z|.

    Example:
        >>> complex_modulus((3, 4))
        5.0

    Complexity: O(1)
    """
    return math.sqrt(z[0] * z[0] + z[1] * z[1])


def complex_argument(z: Tuple[float, float]) -> float:
    """Computes the argument (phase angle) of a complex number in radians.

    arg(z) = atan2(im, re), result in (-π, π].

    Args:
        z: Complex number (re, im).

    Returns:
        Argument in radians.

    Example:
        >>> round(complex_argument((1, 1)), 6)
        0.785398

    Complexity: O(1)
    """
    return math.atan2(z[1], z[0])


def complex_to_polar(z: Tuple[float, float]) -> Tuple[float, float]:
    """Converts a complex number from rectangular to polar form.

    Args:
        z: Complex number (re, im).

    Returns:
        Tuple (r, theta) where r is modulus and theta is argument in radians.

    Example:
        >>> r, theta = complex_to_polar((1, 1))
        >>> (round(r, 6), round(theta, 6))
        (1.414214, 0.785398)

    Complexity: O(1)
    """
    r = math.sqrt(z[0] * z[0] + z[1] * z[1])
    theta = math.atan2(z[1], z[0])
    return (r, theta)


def polar_to_complex(r: float, theta: float) -> Tuple[float, float]:
    """Converts a complex number from polar to rectangular form.

    z = r(cos θ + i sin θ)

    Args:
        r: Modulus (r >= 0).
        theta: Argument in radians.

    Returns:
        Complex number as (re, im).

    Example:
        >>> re, im = polar_to_complex(2, math.pi / 4)
        >>> (round(re, 6), round(im, 6))
        (1.414214, 1.414214)

    Complexity: O(1)
    """
    _check_numeric(r, "r")
    _check_numeric(theta, "theta")
    return (r * math.cos(theta), r * math.sin(theta))


# ---------------------------------------------------------------------------
# De Moivre, Euler, roots of unity
# ---------------------------------------------------------------------------


def de_moivre(r: float, theta: float, n: int) -> Tuple[float, float]:
    """Applies De Moivre's theorem: (r e^(iθ))^n = r^n e^(i·n·θ).

    Args:
        r: Modulus of the complex number.
        theta: Argument in radians.
        n: Integer exponent.

    Returns:
        Result as (re, im).

    Example:
        >>> re, im = de_moivre(1, math.pi / 4, 2)
        >>> (round(re, 6), round(im, 6))
        (0.0, 1.0)

    Complexity: O(1)
    """
    _check_numeric(r, "r")
    _check_numeric(theta, "theta")

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    rn = r ** n
    return (rn * math.cos(n * theta), rn * math.sin(n * theta))


def roots_of_unity(n: int) -> List[Tuple[float, float]]:
    """Computes the n-th roots of unity: e^(2πik/n) for k = 0, 1, ..., n-1.

    Args:
        n: Number of roots (n >= 1).

    Returns:
        List of (re, im) tuples.

    Example:
        >>> roots = roots_of_unity(4)
        >>> [(round(r, 6), round(i, 6)) for r, i in roots]
        [(1.0, 0.0), (0.0, 1.0), (-1.0, 0.0), (-0.0, -1.0)]

    Complexity: O(n)
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer.")

    result = []

    for k in range(n):
        angle = 2.0 * math.pi * k / n
        result.append((math.cos(angle), math.sin(angle)))

    return result


def nth_roots_complex(
    z: Tuple[float, float], n: int
) -> List[Tuple[float, float]]:
    """Computes all n-th roots of a complex number z.

    Args:
        z: Complex number (re, im).
        n: Root degree (n >= 1).

    Returns:
        List of n roots as (re, im) tuples.

    Example:
        >>> roots = nth_roots_complex((0, 1), 2)
        >>> len(roots)
        2

    Complexity: O(n)
    """
    if not isinstance(n, int) or n < 1:
        raise ValueError("n must be a positive integer.")

    r = math.sqrt(z[0] * z[0] + z[1] * z[1])
    theta = math.atan2(z[1], z[0])
    r_root = r ** (1.0 / n)
    result = []

    for k in range(n):
        angle = (theta + 2.0 * math.pi * k) / n
        result.append((r_root * math.cos(angle), r_root * math.sin(angle)))

    return result


def euler_formula(theta: float) -> Tuple[float, float]:
    """Evaluates Euler's formula e^(iθ) = cos θ + i sin θ.

    Args:
        theta: Angle in radians.

    Returns:
        Complex number as (re, im).

    Example:
        >>> re, im = euler_formula(math.pi)
        >>> (round(re, 6), round(im, 6))
        (-1.0, 0.0)

    Complexity: O(1)
    """
    _check_numeric(theta, "theta")
    return (math.cos(theta), math.sin(theta))


def complex_power(
    z: Tuple[float, float], w: Tuple[float, float]
) -> Tuple[float, float]:
    """Computes z^w for complex z and w via z^w = e^(w·ln(z)).

    Args:
        z: Base complex number (re, im). Must not be (0, 0).
        w: Exponent complex number (re, im).

    Returns:
        Result as (re, im).

    Raises:
        ValueError: If z is zero.

    Example:
        >>> re, im = complex_power((0, 1), (0, 1))  # i^i = e^(-π/2)
        >>> round(re, 6)
        0.207880

    Complexity: O(1)
    """
    r = math.sqrt(z[0] * z[0] + z[1] * z[1])

    if r == 0:
        raise ValueError("Base z must not be zero.")

    theta = math.atan2(z[1], z[0])
    ln_r = math.log(r)

    # w * ln(z) = (a+bi)(ln_r + i*theta) = (a*ln_r - b*theta) + i(b*ln_r + a*theta)
    a, b = w
    real_part = a * ln_r - b * theta
    imag_part = b * ln_r + a * theta

    magnitude = math.exp(real_part)
    return (magnitude * math.cos(imag_part), magnitude * math.sin(imag_part))


def complex_exp(z: Tuple[float, float]) -> Tuple[float, float]:
    """Computes the complex exponential e^z.

    e^(a+bi) = e^a (cos b + i sin b)

    Args:
        z: Complex number (re, im).

    Returns:
        Result as (re, im).

    Example:
        >>> re, im = complex_exp((0, math.pi))
        >>> (round(re, 6), round(im, 6))
        (-1.0, 0.0)

    Complexity: O(1)
    """
    ea = math.exp(z[0])
    return (ea * math.cos(z[1]), ea * math.sin(z[1]))


def complex_ln(z: Tuple[float, float]) -> Tuple[float, float]:
    """Computes the principal complex logarithm ln(z).

    ln(z) = ln|z| + i·arg(z)

    Args:
        z: Complex number (re, im). Must not be (0, 0).

    Returns:
        Result as (re, im).

    Raises:
        ValueError: If z is zero.

    Example:
        >>> re, im = complex_ln((-1, 0))
        >>> (round(re, 6), round(im, 6))
        (0.0, 3.141593)

    Complexity: O(1)
    """
    r = math.sqrt(z[0] * z[0] + z[1] * z[1])

    if r == 0:
        raise ValueError("Cannot take logarithm of zero.")

    return (math.log(r), math.atan2(z[1], z[0]))


def complex_sin(z: Tuple[float, float]) -> Tuple[float, float]:
    """Computes sin(z) for complex z.

    sin(a+bi) = sin(a)cosh(b) + i·cos(a)sinh(b)

    Args:
        z: Complex number (re, im).

    Returns:
        Result as (re, im).

    Example:
        >>> re, im = complex_sin((0, 1))
        >>> round(im, 6)  # sin(i) = i·sinh(1)
        1.175201

    Complexity: O(1)
    """
    a, b = z
    return (math.sin(a) * math.cosh(b), math.cos(a) * math.sinh(b))


def complex_cos(z: Tuple[float, float]) -> Tuple[float, float]:
    """Computes cos(z) for complex z.

    cos(a+bi) = cos(a)cosh(b) - i·sin(a)sinh(b)

    Args:
        z: Complex number (re, im).

    Returns:
        Result as (re, im).

    Example:
        >>> re, im = complex_cos((0, 1))
        >>> round(re, 6)  # cos(i) = cosh(1)
        1.543081

    Complexity: O(1)
    """
    a, b = z
    return (math.cos(a) * math.cosh(b), -math.sin(a) * math.sinh(b))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 29: Complex Functions
# ---------------------------------------------------------------------------

def complex_tan(z: tuple[float, float]) -> tuple[float, float]:
    """Compute the tangent of a complex number.

    tan(z) = sin(z) / cos(z)

    Args:
        z: Complex number as (re, im).

    Returns:
        Result as (re, im).

    Raises:
        TypeError: If z is not a tuple of two numerics.

    Usage Example:
        >>> re, im = complex_tan((1.0, 0.0))
        >>> round(re, 4)
        1.5574

    Complexity: O(1)
    """
    a, b = float(z[0]), float(z[1])
    sin_r, sin_i = math.sin(a) * math.cosh(b), math.cos(a) * math.sinh(b)
    cos_r, cos_i = math.cos(a) * math.cosh(b), -math.sin(a) * math.sinh(b)
    denom = cos_r * cos_r + cos_i * cos_i
    if abs(denom) < 1e-15:
        raise ValueError("Complex cosine is zero; tangent undefined.")
    return ((sin_r * cos_r + sin_i * cos_i) / denom, (sin_i * cos_r - sin_r * cos_i) / denom)


def complex_sinh(z: tuple[float, float]) -> tuple[float, float]:
    """Compute the hyperbolic sine of a complex number.

    sinh(a+bi) = sinh(a)cos(b) + i·cosh(a)sin(b)

    Args:
        z: Complex number as (re, im).

    Returns:
        Result as (re, im).

    Usage Example:
        >>> re, im = complex_sinh((1.0, 0.0))
        >>> round(re, 4)
        1.1752

    Complexity: O(1)
    """
    a, b = float(z[0]), float(z[1])
    return (math.sinh(a) * math.cos(b), math.cosh(a) * math.sin(b))


def complex_cosh(z: tuple[float, float]) -> tuple[float, float]:
    """Compute the hyperbolic cosine of a complex number.

    cosh(a+bi) = cosh(a)cos(b) + i·sinh(a)sin(b)

    Args:
        z: Complex number as (re, im).

    Returns:
        Result as (re, im).

    Usage Example:
        >>> re, im = complex_cosh((1.0, 0.0))
        >>> round(re, 4)
        1.5431

    Complexity: O(1)
    """
    a, b = float(z[0]), float(z[1])
    return (math.cosh(a) * math.cos(b), math.sinh(a) * math.sin(b))


def complex_log(z: tuple[float, float]) -> tuple[float, float]:
    """Compute the principal natural logarithm of a complex number.

    ln(z) = ln|z| + i·arg(z)

    Args:
        z: Complex number as (re, im).

    Returns:
        Result as (re, im).

    Raises:
        ValueError: If z is zero.

    Usage Example:
        >>> re, im = complex_log((1.0, 0.0))
        >>> (round(re, 4), round(im, 4))
        (0.0, 0.0)

    Complexity: O(1)
    """
    a, b = float(z[0]), float(z[1])
    modulus = math.hypot(a, b)
    if modulus < 1e-15:
        raise ValueError("Logarithm of zero is undefined.")
    return (math.log(modulus), math.atan2(b, a))


def complex_sqrt(z: tuple[float, float]) -> tuple[float, float]:
    """Compute the principal square root of a complex number.

    Args:
        z: Complex number as (re, im).

    Returns:
        Principal square root as (re, im).

    Usage Example:
        >>> re, im = complex_sqrt((-1.0, 0.0))
        >>> (round(re, 4), round(im, 4))
        (0.0, 1.0)

    Complexity: O(1)
    """
    a, b = float(z[0]), float(z[1])
    r = math.hypot(a, b)
    if r < 1e-15:
        return (0.0, 0.0)
    return (math.sqrt((r + a) / 2.0), math.copysign(math.sqrt((r - a) / 2.0), b))


def complex_reciprocal(z: tuple[float, float]) -> tuple[float, float]:
    """Compute the reciprocal (multiplicative inverse) of a complex number.

    1/(a+bi) = (a-bi)/(a²+b²)

    Args:
        z: Complex number as (re, im).

    Returns:
        Reciprocal as (re, im).

    Raises:
        ValueError: If z is zero.

    Usage Example:
        >>> complex_reciprocal((2.0, 0.0))
        (0.5, -0.0)

    Complexity: O(1)
    """
    a, b = float(z[0]), float(z[1])
    denom = a * a + b * b
    if denom < 1e-15:
        raise ValueError("Cannot compute reciprocal of zero.")
    return (a / denom, -b / denom)


def complex_nth_root(z: tuple[float, float], n: int, k: int = 0) -> tuple[float, float]:
    """Compute the k-th n-th root of a complex number.

    z^(1/n) = |z|^(1/n) · e^(i(arg(z) + 2πk)/n)

    Args:
        z: Complex number as (re, im).
        n: Root degree (≥ 1).
        k: Which root (0 to n-1, default 0 for principal root).

    Returns:
        k-th n-th root as (re, im).

    Raises:
        TypeError: If n or k is not int.
        ValueError: If n < 1 or z is zero.

    Usage Example:
        >>> re, im = complex_nth_root((1.0, 0.0), 3)
        >>> (round(re, 4), round(im, 4))
        (1.0, 0.0)

    Complexity: O(1)
    """
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers.")
    if n < 1:
        raise ValueError("n must be >= 1.")
    a, b = float(z[0]), float(z[1])
    r = math.hypot(a, b)
    if r < 1e-15:
        raise ValueError("n-th root of zero is zero.")
    theta = math.atan2(b, a)
    root_r = r ** (1.0 / n)
    root_theta = (theta + 2.0 * math.pi * k) / n
    return (root_r * math.cos(root_theta), root_r * math.sin(root_theta))


def complex_distance(z1: tuple[float, float], z2: tuple[float, float]) -> float:
    """Compute the distance between two complex numbers.

    |z1 - z2| = √((a1-a2)² + (b1-b2)²)

    Args:
        z1: First complex number (re, im).
        z2: Second complex number (re, im).

    Returns:
        Distance.

    Usage Example:
        >>> complex_distance((0.0, 0.0), (3.0, 4.0))
        5.0

    Complexity: O(1)
    """
    return math.hypot(float(z1[0]) - float(z2[0]), float(z1[1]) - float(z2[1]))


def complex_rotate(z: tuple[float, float], angle: float) -> tuple[float, float]:
    """Rotate a complex number by an angle.

    z' = z · e^(iθ)

    Args:
        z: Complex number as (re, im).
        angle: Rotation angle in radians.

    Returns:
        Rotated complex number as (re, im).

    Raises:
        TypeError: If angle is not numeric.

    Usage Example:
        >>> re, im = complex_rotate((1.0, 0.0), math.pi / 2)
        >>> (round(re, 4), round(im, 4))
        (0.0, 1.0)

    Complexity: O(1)
    """
    if not isinstance(angle, (int, float)):
        raise TypeError("angle must be numeric.")
    a, b = float(z[0]), float(z[1])
    cos_t = math.cos(float(angle))
    sin_t = math.sin(float(angle))
    return (a * cos_t - b * sin_t, a * sin_t + b * cos_t)


def complex_polar_form(z: tuple[float, float]) -> tuple[float, float]:
    """Convert a complex number to polar form (modulus, argument).

    Args:
        z: Complex number as (re, im).

    Returns:
        (modulus, argument) where argument is in radians [-π, π].

    Usage Example:
        >>> complex_polar_form((1.0, 1.0))
        (1.4142135623730951, 0.7853981633974483)

    Complexity: O(1)
    """
    a, b = float(z[0]), float(z[1])
    return (math.hypot(a, b), math.atan2(b, a))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 30: Complex Functions (cont.)
# ---------------------------------------------------------------------------

def complex_from_polar(r: float, theta: float) -> tuple[float, float]:
    """Create a complex number from polar form.

    z = r·(cos θ + i·sin θ)

    Args:
        r: Modulus.
        theta: Argument in radians.

    Returns:
        Complex number as (re, im).

    Raises:
        TypeError: If arguments are not numeric.

    Usage Example:
        >>> re, im = complex_from_polar(1.0, 0.0)
        >>> (round(re, 4), round(im, 4))
        (1.0, 0.0)

    Complexity: O(1)
    """
    if not isinstance(r, (int, float)) or not isinstance(theta, (int, float)):
        raise TypeError("r and theta must be numeric.")
    r, theta = float(r), float(theta)
    return (r * math.cos(theta), r * math.sin(theta))


def complex_conjugate(z: tuple[float, float]) -> tuple[float, float]:
    """Compute the complex conjugate.

    conj(a + bi) = a - bi

    Args:
        z: Complex number as (re, im).

    Returns:
        Conjugate as (re, im).

    Usage Example:
        >>> complex_conjugate((3.0, 4.0))
        (3.0, -4.0)

    Complexity: O(1)
    """
    return (float(z[0]), -float(z[1]))


def complex_argument_degrees(z: tuple[float, float]) -> float:
    """Compute the argument (phase) of a complex number in degrees.

    Args:
        z: Complex number as (re, im).

    Returns:
        Argument in degrees [-180, 180].

    Usage Example:
        >>> complex_argument_degrees((1.0, 1.0))
        45.0

    Complexity: O(1)
    """
    return math.degrees(math.atan2(float(z[1]), float(z[0])))


def complex_midpoint(z1: tuple[float, float], z2: tuple[float, float]) -> tuple[float, float]:
    """Compute the midpoint between two complex numbers.

    Args:
        z1: First complex number (re, im).
        z2: Second complex number (re, im).

    Returns:
        Midpoint as (re, im).

    Usage Example:
        >>> complex_midpoint((0.0, 0.0), (4.0, 6.0))
        (2.0, 3.0)

    Complexity: O(1)
    """
    return ((float(z1[0]) + float(z2[0])) / 2.0, (float(z1[1]) + float(z2[1])) / 2.0)


def complex_lerp(z1: tuple[float, float], z2: tuple[float, float], t: float) -> tuple[float, float]:
    """Linear interpolation between two complex numbers.

    z = z1 + t·(z2 - z1)

    Args:
        z1: Start complex number (re, im).
        z2: End complex number (re, im).
        t: Interpolation parameter (0 to 1).

    Returns:
        Interpolated complex number as (re, im).

    Raises:
        TypeError: If t is not numeric.

    Usage Example:
        >>> complex_lerp((0.0, 0.0), (4.0, 6.0), 0.5)
        (2.0, 3.0)

    Complexity: O(1)
    """
    if not isinstance(t, (int, float)):
        raise TypeError("t must be numeric.")
    t = float(t)
    a1, b1 = float(z1[0]), float(z1[1])
    a2, b2 = float(z2[0]), float(z2[1])
    return (a1 + t * (a2 - a1), b1 + t * (b2 - b1))
