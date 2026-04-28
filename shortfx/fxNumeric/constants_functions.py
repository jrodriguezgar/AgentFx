"""Scientific and mathematical constants module.

Provides a curated set of fundamental mathematical and physical constants
with full precision. Constants can be queried by name for AI agent
integration or used directly as module-level values.

Key Features:
    - Mathematical constants (π, e, φ, √2, etc.)
    - Physical constants (speed of light, Planck, Boltzmann, etc.)
    - Named lookup via ``get_constant()`` for MCP/AI usage
    - Full catalog via ``list_constants()``

Example:
    >>> from shortfx.fxNumeric.constants_functions import get_constant, PI
    >>> get_constant("pi")
    3.141592653589793
    >>> PI
    3.141592653589793
"""

import math
from typing import Optional


# ── Mathematical Constants ──────────────────────────────────────────────────

PI = math.pi
"""The ratio of a circle's circumference to its diameter (π ≈ 3.14159)."""

E = math.e
"""Euler's number, the base of the natural logarithm (e ≈ 2.71828)."""

TAU = math.tau
"""The ratio of a circle's circumference to its radius (τ = 2π ≈ 6.28318)."""

PHI = (1 + math.sqrt(5)) / 2
"""The golden ratio (φ ≈ 1.61803)."""

SQRT2 = math.sqrt(2)
"""The square root of 2 (√2 ≈ 1.41421)."""

SQRT3 = math.sqrt(3)
"""The square root of 3 (√3 ≈ 1.73205)."""

LN2 = math.log(2)
"""The natural logarithm of 2 (ln(2) ≈ 0.69315)."""

LN10 = math.log(10)
"""The natural logarithm of 10 (ln(10) ≈ 2.30259)."""

LOG2E = math.log2(math.e)
"""The base-2 logarithm of e (log₂(e) ≈ 1.44270)."""

LOG10E = math.log10(math.e)
"""The base-10 logarithm of e (log₁₀(e) ≈ 0.43429)."""

INF = math.inf
"""Positive infinity."""

NAN = math.nan
"""Not a Number (NaN)."""

EULER_MASCHERONI = 0.5772156649015329
"""The Euler-Mascheroni constant (γ ≈ 0.57722)."""


# ── Physical Constants (SI units, CODATA 2018) ──────────────────────────────

SPEED_OF_LIGHT = 299_792_458.0
"""Speed of light in vacuum (m/s)."""

PLANCK = 6.62607015e-34
"""Planck constant (J·s)."""

REDUCED_PLANCK = 1.054571817e-34
"""Reduced Planck constant ℏ = h/(2π) (J·s)."""

BOLTZMANN = 1.380649e-23
"""Boltzmann constant (J/K)."""

AVOGADRO = 6.02214076e23
"""Avogadro's number (mol⁻¹)."""

GAS_CONSTANT = 8.314462618
"""Ideal gas constant R (J/(mol·K))."""

GRAVITATIONAL = 6.67430e-11
"""Newtonian gravitational constant G (m³/(kg·s²))."""

GRAVITY = 9.80665
"""Standard acceleration of gravity g (m/s²)."""

ELEMENTARY_CHARGE = 1.602176634e-19
"""Elementary charge e (C)."""

ELECTRON_MASS = 9.1093837015e-31
"""Electron mass (kg)."""

PROTON_MASS = 1.67262192369e-27
"""Proton mass (kg)."""

STEFAN_BOLTZMANN = 5.670374419e-8
"""Stefan-Boltzmann constant σ (W/(m²·K⁴))."""

VACUUM_PERMITTIVITY = 8.8541878128e-12
"""Vacuum permittivity ε₀ (F/m)."""

VACUUM_PERMEABILITY = 1.25663706212e-6
"""Vacuum permeability μ₀ (H/m)."""

ABSOLUTE_ZERO_CELSIUS = -273.15
"""Absolute zero in Celsius (°C)."""


# ── Constant Registry ───────────────────────────────────────────────────────

_CONSTANTS: dict[str, tuple[float, str, str]] = {
    # Mathematical
    "pi": (PI, "π", "Ratio of circumference to diameter"),
    "e": (E, "e", "Euler's number, base of natural logarithm"),
    "tau": (TAU, "τ", "Ratio of circumference to radius (2π)"),
    "phi": (PHI, "φ", "Golden ratio"),
    "sqrt2": (SQRT2, "√2", "Square root of 2"),
    "sqrt3": (SQRT3, "√3", "Square root of 3"),
    "ln2": (LN2, "ln(2)", "Natural logarithm of 2"),
    "ln10": (LN10, "ln(10)", "Natural logarithm of 10"),
    "log2e": (LOG2E, "log₂(e)", "Base-2 logarithm of e"),
    "log10e": (LOG10E, "log₁₀(e)", "Base-10 logarithm of e"),
    "inf": (INF, "∞", "Positive infinity"),
    "euler_mascheroni": (EULER_MASCHERONI, "γ", "Euler-Mascheroni constant"),
    # Physical
    "speed_of_light": (SPEED_OF_LIGHT, "c", "Speed of light in vacuum (m/s)"),
    "c": (SPEED_OF_LIGHT, "c", "Speed of light in vacuum (m/s)"),
    "planck": (PLANCK, "h", "Planck constant (J·s)"),
    "h": (PLANCK, "h", "Planck constant (J·s)"),
    "hbar": (REDUCED_PLANCK, "ℏ", "Reduced Planck constant (J·s)"),
    "boltzmann": (BOLTZMANN, "k_B", "Boltzmann constant (J/K)"),
    "avogadro": (AVOGADRO, "N_A", "Avogadro's number (mol⁻¹)"),
    "gas_constant": (GAS_CONSTANT, "R", "Ideal gas constant (J/(mol·K))"),
    "gravitational": (GRAVITATIONAL, "G", "Newtonian gravitational constant (m³/(kg·s²))"),
    "gravity": (GRAVITY, "g", "Standard gravity (m/s²)"),
    "g": (GRAVITY, "g", "Standard gravity (m/s²)"),
    "elementary_charge": (ELEMENTARY_CHARGE, "e", "Elementary charge (C)"),
    "electron_mass": (ELECTRON_MASS, "m_e", "Electron mass (kg)"),
    "proton_mass": (PROTON_MASS, "m_p", "Proton mass (kg)"),
    "stefan_boltzmann": (STEFAN_BOLTZMANN, "σ", "Stefan-Boltzmann constant (W/(m²·K⁴))"),
    "vacuum_permittivity": (VACUUM_PERMITTIVITY, "ε₀", "Vacuum permittivity (F/m)"),
    "vacuum_permeability": (VACUUM_PERMEABILITY, "μ₀", "Vacuum permeability (H/m)"),
    "absolute_zero": (ABSOLUTE_ZERO_CELSIUS, "0 K", "Absolute zero in Celsius (°C)"),
}


def get_constant(name: str) -> float:
    """Returns the value of a scientific or mathematical constant by name.

    Description:
        Looks up a constant from the built-in catalog of mathematical and
        physical constants. Names are case-insensitive.

    Args:
        name (str): The name of the constant (e.g. "pi", "avogadro", "c").

    Returns:
        float: The numeric value of the constant.

    Raises:
        TypeError: If name is not a string.
        KeyError: If the constant name is not found.

    Usage Example:
        >>> from shortfx.fxNumeric.constants_functions import get_constant
        >>> get_constant("pi")
        3.141592653589793
        >>> get_constant("avogadro")
        6.02214076e+23
        >>> get_constant("speed_of_light")
        299792458.0

    Cost: O(1)
    """
    if not isinstance(name, str):
        raise TypeError("Constant name must be a string.")

    key = name.strip().lower()

    if key not in _CONSTANTS:
        available = ", ".join(sorted(_CONSTANTS.keys()))
        raise KeyError(
            f"Unknown constant '{name}'. Available: {available}"
        )

    return _CONSTANTS[key][0]


def list_constants(category: Optional[str] = None) -> list[dict[str, str]]:
    """Lists all available scientific and mathematical constants.

    Description:
        Returns a catalog of all constants with their name, symbol,
        value, and description. Optionally filter by category.

    Args:
        category (Optional[str]): Filter by "math" or "physical".
            None returns all constants.

    Returns:
        list[dict[str, str]]: List of constant info dicts with keys
            name, symbol, value, description.

    Raises:
        ValueError: If category is not "math", "physical", or None.

    Usage Example:
        >>> from shortfx.fxNumeric.constants_functions import list_constants
        >>> math_consts = list_constants("math")
        >>> len(math_consts) > 0
        True

    Cost: O(n) where n is the number of constants.
    """
    _MATH_KEYS = {
        "pi", "e", "tau", "phi", "sqrt2", "sqrt3", "ln2", "ln10",
        "log2e", "log10e", "inf", "euler_mascheroni",
    }
    _PHYSICAL_KEYS = {
        "speed_of_light", "c", "planck", "h", "hbar", "boltzmann",
        "avogadro", "gas_constant", "gravitational", "gravity", "g",
        "elementary_charge", "electron_mass", "proton_mass",
        "stefan_boltzmann", "vacuum_permittivity", "vacuum_permeability",
        "absolute_zero",
    }

    if category is not None:
        cat = category.strip().lower()

        if cat not in ("math", "physical"):
            raise ValueError("Category must be 'math', 'physical', or None.")

        allowed = _MATH_KEYS if cat == "math" else _PHYSICAL_KEYS
    else:
        allowed = None

    result = []

    for key, (value, symbol, description) in sorted(_CONSTANTS.items()):

        if allowed is not None and key not in allowed:
            continue

        result.append({
            "name": key,
            "symbol": symbol,
            "value": str(value),
            "description": description,
        })

    return result
