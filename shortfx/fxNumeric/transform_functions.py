"""Integral transforms: Laplace, Fourier, and related operations.

Numerical Laplace and Fourier transforms, DFT/IDFT, convolution,
and cross-correlation from Spiegel's *Mathematical Handbook*.
"""

import math
from typing import Callable, List, Tuple


# ---------------------------------------------------------------------------
# Discrete Fourier Transform
# ---------------------------------------------------------------------------


def dft(signal: List[float]) -> List[Tuple[float, float]]:
    """Computes the Discrete Fourier Transform of a real signal.

    X[k] = sum_{n=0}^{N-1} x[n] e^{-i 2 pi k n / N}.

    Args:
        signal: List of real-valued samples.

    Returns:
        List of (real, imag) tuples for each frequency bin.

    Raises:
        TypeError: If signal is not a list.
        ValueError: If signal is empty.

    Example:
        >>> result = dft([1, 0, 1, 0])
        >>> (round(result[0][0], 4), round(result[0][1], 4))
        (2.0, 0.0)

    Complexity: O(N^2) — use FFT for large signals.
    """
    if not isinstance(signal, list):
        raise TypeError("signal must be a list.")

    if not signal:
        raise ValueError("signal must not be empty.")

    n = len(signal)
    result = []

    for k in range(n):
        real_part = 0.0
        imag_part = 0.0

        for t in range(n):
            angle = 2.0 * math.pi * k * t / n
            real_part += signal[t] * math.cos(angle)
            imag_part -= signal[t] * math.sin(angle)

        result.append((real_part, imag_part))

    return result


def idft(spectrum: List[Tuple[float, float]]) -> List[float]:
    """Computes the Inverse Discrete Fourier Transform.

    x[n] = (1/N) sum_{k=0}^{N-1} X[k] e^{i 2 pi k n / N}.

    Args:
        spectrum: List of (real, imag) tuples.

    Returns:
        List of real-valued time-domain samples.

    Raises:
        TypeError: If spectrum is not a list.
        ValueError: If spectrum is empty.

    Example:
        >>> signal = idft([(2, 0), (0, 0), (2, 0), (0, 0)])
        >>> [round(s, 4) for s in signal]
        [1.0, 0.0, 1.0, 0.0]

    Complexity: O(N^2)
    """
    if not isinstance(spectrum, list):
        raise TypeError("spectrum must be a list.")

    if not spectrum:
        raise ValueError("spectrum must not be empty.")

    n = len(spectrum)
    result = []

    for t in range(n):
        real_sum = 0.0

        for k in range(n):
            angle = 2.0 * math.pi * k * t / n
            re, im = spectrum[k]
            real_sum += re * math.cos(angle) - im * math.sin(angle)

        result.append(real_sum / n)

    return result


# ---------------------------------------------------------------------------
# Numerical Laplace transform
# ---------------------------------------------------------------------------


def laplace_transform_numerical(
    f: Callable[[float], float],
    s: float,
    t_max: float = 50.0,
    n_points: int = 1000,
) -> float:
    """Numerically approximates the Laplace transform F(s) = integral_0^inf f(t) e^{-st} dt.

    Uses the trapezoidal rule over [0, t_max].

    Args:
        f: Time-domain function f(t).
        s: Complex frequency (real, > 0 for convergence).
        t_max: Upper integration limit.
        n_points: Number of sample points.

    Returns:
        Approximate F(s).

    Raises:
        TypeError: If s is not numeric.
        ValueError: If s <= 0 or t_max <= 0 or n_points < 2.

    Example:
        >>> round(laplace_transform_numerical(lambda t: 1, 1.0), 2)
        1.0

    Complexity: O(n_points)
    """
    if not isinstance(s, (int, float)):
        raise TypeError("s must be numeric.")

    if s <= 0:
        raise ValueError("s must be > 0.")

    if t_max <= 0:
        raise ValueError("t_max must be > 0.")

    if n_points < 2:
        raise ValueError("n_points must be >= 2.")

    dt = t_max / n_points
    total = 0.0

    for i in range(n_points + 1):
        t = i * dt
        weight = 0.5 if (i == 0 or i == n_points) else 1.0
        total += weight * f(t) * math.exp(-s * t)

    return total * dt


def inverse_laplace_gaver_stehfest(
    f_s: Callable[[float], float],
    t: float,
    n: int = 12,
) -> float:
    """Numerically inverts the Laplace transform using the Gaver-Stehfest algorithm.

    Args:
        f_s: Laplace-domain function F(s).
        t: Time at which to evaluate the inverse.
        n: Algorithm order (must be even, typically 8-14).

    Returns:
        Approximate f(t).

    Raises:
        TypeError: If t is not numeric or n is not an integer.
        ValueError: If t <= 0 or n < 2 or n is odd.

    Example:
        >>> round(inverse_laplace_gaver_stehfest(lambda s: 1/s, 1.0), 4)
        1.0

    Complexity: O(n^2) for coefficient computation + O(n) evaluations.
    """
    if not isinstance(t, (int, float)):
        raise TypeError("t must be numeric.")

    if not isinstance(n, int):
        raise TypeError("n must be an integer.")

    if t <= 0:
        raise ValueError("t must be > 0.")

    if n < 2 or n % 2 != 0:
        raise ValueError("n must be an even integer >= 2.")

    ln2_over_t = math.log(2) / t
    half_n = n // 2
    total = 0.0

    for k in range(1, n + 1):
        vk = 0.0
        lower = (k + 1) // 2
        upper = min(k, half_n)

        for j in range(lower, upper + 1):
            num = j ** half_n * math.factorial(2 * j)
            den = (
                math.factorial(half_n - j)
                * math.factorial(j)
                * math.factorial(j - 1)
                * math.factorial(k - j)
                * math.factorial(2 * j - k)
            )
            vk += num / den

        vk *= (-1) ** (k + half_n)
        total += vk * f_s(k * ln2_over_t)

    return total * ln2_over_t


# ---------------------------------------------------------------------------
# Numerical Fourier transform
# ---------------------------------------------------------------------------


def fourier_transform_numerical(
    f: Callable[[float], float],
    omega: float,
    t_range: Tuple[float, float] = (-50.0, 50.0),
    n_points: int = 2000,
) -> Tuple[float, float]:
    """Numerically approximates the Fourier transform F(omega).

    F(w) = integral_{-inf}^{inf} f(t) e^{-i w t} dt.

    Args:
        f: Time-domain function.
        omega: Angular frequency.
        t_range: Integration interval (t_min, t_max).
        n_points: Number of sample points.

    Returns:
        Tuple (real_part, imaginary_part) of F(omega).

    Example:
        >>> import math
        >>> re, im = fourier_transform_numerical(
        ...     lambda t: math.exp(-abs(t)), 0.0
        ... )
        >>> round(re, 2)
        2.0

    Complexity: O(n_points)
    """
    if not isinstance(omega, (int, float)):
        raise TypeError("omega must be numeric.")

    t_min, t_max = t_range

    if t_min >= t_max:
        raise ValueError("t_range must have t_min < t_max.")

    if n_points < 2:
        raise ValueError("n_points must be >= 2.")

    dt = (t_max - t_min) / n_points
    real_part = 0.0
    imag_part = 0.0

    for i in range(n_points + 1):
        t = t_min + i * dt
        weight = 0.5 if (i == 0 or i == n_points) else 1.0
        ft = f(t)
        real_part += weight * ft * math.cos(omega * t)
        imag_part -= weight * ft * math.sin(omega * t)

    return (real_part * dt, imag_part * dt)


# ---------------------------------------------------------------------------
# Convolution and correlation
# ---------------------------------------------------------------------------


def convolution(f: List[float], g: List[float]) -> List[float]:
    """Computes the discrete linear convolution of two sequences.

    (f * g)[n] = sum_k f[k] g[n-k].

    Args:
        f: First sequence.
        g: Second sequence.

    Returns:
        Convolution result of length len(f) + len(g) - 1.

    Raises:
        TypeError: If f or g are not lists.
        ValueError: If f or g is empty.

    Example:
        >>> convolution([1, 2, 3], [1, 1])
        [1.0, 3.0, 5.0, 3.0]

    Complexity: O(n * m)
    """
    if not isinstance(f, list) or not isinstance(g, list):
        raise TypeError("f and g must be lists.")

    if not f or not g:
        raise ValueError("f and g must not be empty.")

    n = len(f)
    m = len(g)
    result_len = n + m - 1
    result = [0.0] * result_len

    for i in range(n):

        for j in range(m):
            result[i + j] += f[i] * g[j]

    return result


def cross_correlation(f: List[float], g: List[float]) -> List[float]:
    """Computes the discrete cross-correlation of two sequences.

    (f ⋆ g)[n] = sum_k f[k] g[k+n] (conjugate omitted for real signals).

    Args:
        f: First sequence.
        g: Second sequence.

    Returns:
        Cross-correlation result.

    Raises:
        TypeError: If f or g are not lists.
        ValueError: If f or g is empty.

    Example:
        >>> cross_correlation([1, 2, 3], [1, 2, 3])
        [3.0, 8.0, 14.0, 8.0, 3.0]

    Complexity: O(n * m)
    """
    if not isinstance(f, list) or not isinstance(g, list):
        raise TypeError("f and g must be lists.")

    if not f or not g:
        raise ValueError("f and g must not be empty.")

    # Cross-correlation: correlate f with g → convolve f_reversed with g
    f_reversed = list(reversed(f))
    return convolution(f_reversed, g)


def auto_correlation(signal: List[float]) -> List[float]:
    """Computes the discrete auto-correlation of a signal.

    Args:
        signal: Input sequence.

    Returns:
        Auto-correlation result.

    Example:
        >>> auto_correlation([1, 0, 1])
        [1.0, 0.0, 2.0, 0.0, 1.0]

    Complexity: O(n^2)
    """
    return cross_correlation(signal, signal)


# ---------------------------------------------------------------------------
# Z-transform (numerical evaluation)
# ---------------------------------------------------------------------------


def z_transform_eval(
    x: List[float], z_real: float, z_imag: float,
) -> Tuple[float, float]:
    """Evaluates the Z-transform X(z) = sum_{n=0}^{N-1} x[n] z^{-n} at a given z.

    Args:
        x: Discrete-time signal [x[0], x[1], ...].
        z_real: Real part of z.
        z_imag: Imaginary part of z.

    Returns:
        Tuple (real_part, imag_part) of X(z).

    Raises:
        ValueError: If z == 0 (except for x of length 1).

    Example:
        >>> z_transform_eval([1, 1, 1], 2.0, 0.0)
        (1.75, 0.0)

    Complexity: O(n)
    """
    if not isinstance(x, list):
        raise TypeError("x must be a list.")

    if not x:
        raise ValueError("x must not be empty.")

    if z_real == 0 and z_imag == 0 and len(x) > 1:
        raise ValueError("z must not be zero (division by zero for z^{-n}).")

    re_total = 0.0
    im_total = 0.0

    # z^{-n} = (z_real - i z_imag)^n / |z|^{2n} but we compute iteratively
    z_inv_re = z_real / (z_real ** 2 + z_imag ** 2) if (z_real != 0 or z_imag != 0) else 0.0
    z_inv_im = -z_imag / (z_real ** 2 + z_imag ** 2) if (z_real != 0 or z_imag != 0) else 0.0

    # z^{-0} = 1
    power_re, power_im = 1.0, 0.0

    for n in range(len(x)):
        re_total += x[n] * power_re
        im_total += x[n] * power_im

        # multiply power by z^{-1}
        new_re = power_re * z_inv_re - power_im * z_inv_im
        new_im = power_re * z_inv_im + power_im * z_inv_re
        power_re, power_im = new_re, new_im

    return (re_total, im_total)


# ---------------------------------------------------------------------------
# Hilbert-like transform (discrete)
# ---------------------------------------------------------------------------


def hilbert_transform(signal: List[float]) -> List[float]:
    """Approximates the discrete Hilbert transform of a real signal.

    The Hilbert transform produces the analytic signal's imaginary component,
    i.e., a 90° phase shift.

    Args:
        signal: Real-valued input signal.

    Returns:
        Hilbert-transformed signal (imaginary part of analytic signal).

    Example:
        >>> h = hilbert_transform([1, 0, -1, 0])
        >>> [round(v, 4) for v in h]
        [0.0, -1.0, 0.0, 1.0]

    Complexity: O(N^2) via DFT approach.
    """
    if not isinstance(signal, list):
        raise TypeError("signal must be a list.")

    if not signal:
        raise ValueError("signal must not be empty.")

    n = len(signal)
    # Compute DFT
    spectrum = dft(signal)

    # Modify spectrum: multiply by -i*sgn(k)
    modified = []

    for k in range(n):

        if k == 0 or (n % 2 == 0 and k == n // 2):
            modified.append((0.0, 0.0))
        elif k < n / 2:
            # Multiply by -i: (re, im) * (0, -1) = (im, -re)
            re, im = spectrum[k]
            modified.append((im, -re))
        else:
            # Multiply by i: (re, im) * (0, 1) = (-im, re)
            re, im = spectrum[k]
            modified.append((-im, re))

    return idft(modified)


# ---------------------------------------------------------------------------
# Mellin and Hankel transforms (Spiegel Ch. Integral Transforms)
# ---------------------------------------------------------------------------


def mellin_transform_numerical(
    f: callable,
    s: float,
    a: float = 1e-6,
    b: float = 100.0,
    n: int = 2000,
) -> float:
    """Computes the Mellin transform M{f}(s) = ∫_0^∞ x^(s-1) f(x) dx numerically.

    Uses the trapezoidal rule on a log-spaced grid.

    Args:
        f: Integrand function f(x).
        s: Complex frequency parameter (real).
        a: Lower integration limit (> 0, approximation of 0).
        b: Upper integration limit (approximation of ∞).
        n: Number of quadrature points.

    Returns:
        Approximate M{f}(s).

    Raises:
        TypeError: If f is not callable or s not numeric.

    Example:
        >>> import math
        >>> round(mellin_transform_numerical(lambda x: math.exp(-x), 2), 4)
        1.0

    Complexity: O(n)
    """
    if not callable(f):
        raise TypeError("f must be callable.")

    if not isinstance(s, (int, float)):
        raise TypeError("s must be numeric.")

    # Log-spaced points for better accuracy on (0, ∞)
    log_a = math.log(a)
    log_b = math.log(b)
    h = (log_b - log_a) / n
    total = 0.0

    for i in range(n):
        log_x = log_a + (i + 0.5) * h
        x = math.exp(log_x)
        total += x ** s * f(x) * h  # substitution: dx = x * d(log x)

    return total


def hankel_transform_numerical(
    f: callable,
    k: float,
    nu: float = 0.0,
    a: float = 1e-6,
    b: float = 50.0,
    n: int = 2000,
) -> float:
    """Computes the Hankel transform H_ν{f}(k) = ∫_0^∞ f(r) J_ν(kr) r dr numerically.

    Uses the trapezoidal rule. Requires bessel_j from special_functions.

    Args:
        f: Radial function f(r).
        k: Transform variable.
        nu: Order of the Bessel function (default 0).
        a: Lower limit (> 0).
        b: Upper limit.
        n: Number of quadrature points.

    Returns:
        Approximate H_ν{f}(k).

    Raises:
        TypeError: If f is not callable or parameters not numeric.

    Example:
        >>> import math
        >>> round(hankel_transform_numerical(lambda r: math.exp(-r), 0, 0, 1e-6, 50, 2000), 2)
        1.0

    Complexity: O(n * Bessel_cost)
    """
    if not callable(f):
        raise TypeError("f must be callable.")

    if not isinstance(k, (int, float)):
        raise TypeError("k must be numeric.")

    # Import Bessel function
    from shortfx.fxNumeric.special_functions import bessel_j

    h = (b - a) / n
    total = 0.0

    for i in range(n):
        r = a + (i + 0.5) * h
        total += f(r) * bessel_j(int(nu), k * r) * r * h

    return total


def discrete_cosine_transform(signal: list) -> list:
    """Computes the Type-II Discrete Cosine Transform (DCT-II).

    X_k = Σ_{n=0}^{N-1} x_n cos(π(2n+1)k / (2N)).

    Args:
        signal: Real-valued input signal.

    Returns:
        DCT coefficients.

    Example:
        >>> dct = discrete_cosine_transform([1, 1, 1, 1])
        >>> round(dct[0], 4)
        4.0

    Complexity: O(N^2)
    """
    if not isinstance(signal, list):
        raise TypeError("signal must be a list.")

    if not signal:
        raise ValueError("signal must not be empty.")

    n = len(signal)
    result = []

    for k in range(n):
        s = 0.0

        for i in range(n):
            s += signal[i] * math.cos(math.pi * (2 * i + 1) * k / (2.0 * n))

        result.append(s)

    return result


def inverse_discrete_cosine_transform(coefficients: list) -> list:
    """Computes the inverse Type-II DCT (DCT-III).

    x_n = (2/N)(X_0/2 + Σ_{k=1}^{N-1} X_k cos(π(2n+1)k / (2N))).

    Args:
        coefficients: DCT coefficients.

    Returns:
        Reconstructed signal.

    Example:
        >>> idct = inverse_discrete_cosine_transform([4, 0, 0, 0])
        >>> [round(v, 4) for v in idct]
        [1.0, 1.0, 1.0, 1.0]

    Complexity: O(N^2)
    """
    if not isinstance(coefficients, list):
        raise TypeError("coefficients must be a list.")

    if not coefficients:
        raise ValueError("coefficients must not be empty.")

    n = len(coefficients)
    result = []

    for i in range(n):
        s = coefficients[0] / 2.0

        for k in range(1, n):
            s += coefficients[k] * math.cos(math.pi * (2 * i + 1) * k / (2.0 * n))

        result.append(2.0 * s / n)

    return result


def discrete_sine_transform(signal: list) -> list:
    """Computes the Type-I Discrete Sine Transform (DST-I).

    X_k = Σ_{n=0}^{N-1} x_n sin(π(n+1)(k+1) / (N+1)).

    Args:
        signal: Real-valued input signal.

    Returns:
        DST coefficients.

    Example:
        >>> dst = discrete_sine_transform([1, 1, 1])
        >>> round(dst[0], 4)
        2.4142

    Complexity: O(N^2)
    """
    if not isinstance(signal, list):
        raise TypeError("signal must be a list.")

    if not signal:
        raise ValueError("signal must not be empty.")

    n = len(signal)
    result = []

    for k in range(n):
        s = 0.0

        for i in range(n):
            s += signal[i] * math.sin(math.pi * (i + 1) * (k + 1) / (n + 1))

        result.append(s)

    return result


# ---------------------------------------------------------------------------
# Hartley transform (Spiegel)
# ---------------------------------------------------------------------------


def hartley_transform(signal: list) -> list:
    """Computes the discrete Hartley transform (DHT).

    H_k = Σ_{n=0}^{N-1} x_n · cas(2πnk/N), where cas(θ) = cos(θ) + sin(θ).

    The Hartley transform is its own inverse (up to 1/N normalisation).

    Args:
        signal: Real-valued input signal.

    Returns:
        DHT coefficients.

    Example:
        >>> dht = hartley_transform([1, 0, 0, 0])
        >>> [round(v, 4) for v in dht]
        [1.0, 1.0, 1.0, 1.0]

    Complexity: O(N^2)
    """

    if not isinstance(signal, list):
        raise TypeError("signal must be a list.")

    if not signal:
        raise ValueError("signal must not be empty.")

    n = len(signal)
    result = []

    for k in range(n):
        s = 0.0

        for i in range(n):
            angle = 2.0 * math.pi * i * k / n
            s += signal[i] * (math.cos(angle) + math.sin(angle))

        result.append(s)

    return result


def inverse_hartley_transform(coefficients: list) -> list:
    """Computes the inverse discrete Hartley transform.

    x_n = (1/N) Σ_{k=0}^{N-1} H_k · cas(2πnk/N).

    Args:
        coefficients: DHT coefficients.

    Returns:
        Reconstructed signal.

    Example:
        >>> inv = inverse_hartley_transform([1, 1, 1, 1])
        >>> [round(v, 4) for v in inv]
        [1.0, 0.0, 0.0, 0.0]

    Complexity: O(N^2)
    """

    if not isinstance(coefficients, list):
        raise TypeError("coefficients must be a list.")

    if not coefficients:
        raise ValueError("coefficients must not be empty.")

    n = len(coefficients)
    fwd = hartley_transform(coefficients)
    return [v / n for v in fwd]


# ---------------------------------------------------------------------------
# Abel transform (Spiegel)
# ---------------------------------------------------------------------------


def abel_transform_numerical(
    f: callable,
    y: float,
    r_max: float = 10.0,
    n_points: int = 1000,
) -> float:
    """Numerical Abel transform: F(y) = 2 ∫_y^∞ f(r) r / √(r²-y²) dr.

    Args:
        f: Radially-symmetric function f(r).
        y: Impact parameter (y ≥ 0).
        r_max: Upper integration limit (approximating ∞).
        n_points: Quadrature points.

    Returns:
        Abel transform value at y.

    Example:
        >>> import math
        >>> round(abel_transform_numerical(lambda r: math.exp(-r*r), 0.0), 4)
        1.7725

    Complexity: O(n_points)
    """

    if not callable(f):
        raise TypeError("f must be callable.")

    if not isinstance(y, (int, float)):
        raise TypeError("y must be numeric.")

    if y < 0:
        raise ValueError("y must be non-negative.")

    # Avoid singularity at r = y by starting slightly above
    eps = 1e-8
    a = y + eps

    if a >= r_max:
        return 0.0

    h = (r_max - a) / n_points
    total = 0.0

    for i in range(n_points + 1):
        r = a + i * h
        diff = r * r - y * y

        if diff <= 0:
            continue

        val = f(r) * r / math.sqrt(diff)

        if i == 0 or i == n_points:
            total += val
        else:
            total += 2.0 * val

    return 2.0 * h * total / 2.0
