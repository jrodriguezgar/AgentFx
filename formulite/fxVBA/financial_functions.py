"""
Access Financial Functions Module.

Description
    Funciones financieras compatibles con VBA/Access para cálculo de
    depreciación, anualidades y préstamos.
"""

from typing import List

__all__ = [
    "DDB",
    "FV",
    "IPmt",
    "IRR",
    "MIRR",
    "NPer",
    "NPV",
    "Pmt",
    "PPmt",
    "PV",
    "Rate",
    "SLN",
    "SYD",
]


def DDB(
    cost: float,
    salvage: float,
    life: float,
    period: float,
    factor: float = 2.0
) -> float:
    """
    Description
        Depreciación de doble saldo decreciente de un activo.

    Args
        cost: Costo inicial del bien.
        salvage: Valor al término de vida útil.
        life: Duración de vida útil.
        period: Periodo para el cual se calcula depreciación.
        factor: Tasa de depreciación (por defecto 2.0).

    Returns
        float: Depreciación para el periodo especificado.

    Usage Example
        >>> ddb(1000, 100, 5, 1)
        400.0

    Cost
        O(1)
    """
    if period > life:
        return 0.0
    
    depreciation = 0.0
    total_depreciation = 0.0
    
    for p in range(1, int(period) + 1):
        remaining_value = cost - total_depreciation
        period_depreciation = min(
            remaining_value * (factor / life),
            remaining_value - salvage
        )
        depreciation = period_depreciation
        total_depreciation += period_depreciation
    
    return depreciation


def FV(rate: float, nper: float, pmt: float, pv: float = 0, type_: int = 0) -> float:
    """
    Description
        Valor futuro de anualidad basado en pagos periódicos constantes.

    Args
        rate: Tasa de interés por periodo.
        nper: Número total de periodos de pago.
        pmt: Pago por periodo.
        pv: Valor presente (por defecto 0).
        type_: Tipo de pago (0=final periodo, 1=inicio periodo).

    Returns
        float: Valor futuro.

    Usage Example
        >>> fv(0.05/12, 12, -100, -1000)
        2276.28

    Cost
        O(1)
    """
    if rate == 0:
        return -(pv + pmt * nper)
    
    factor = (1 + rate) ** nper
    if type_ == 0:
        return -(pv * factor + pmt * (factor - 1) / rate)
    else:
        return -(pv * factor + pmt * (factor - 1) / rate * (1 + rate))


def IPmt(rate: float, per: float, nper: float, pv: float, fv: float = 0, type_: int = 0) -> float:
    """
    Description
        Pago de intereses para periodo dado de una anualidad.

    Args
        rate: Tasa de interés por periodo.
        per: Periodo para el cual se calcula interés (1 a nper).
        nper: Número total de periodos.
        pv: Valor presente.
        fv: Valor futuro (por defecto 0).
        type_: Tipo de pago (0=final, 1=inicio).

    Returns
        float: Pago de intereses.

    Usage Example
        >>> ipmt(0.1/12, 1, 36, 8000)
        -66.67

    Cost
        O(1)
    """
    payment = pmt(rate, nper, pv, fv, type_)
    
    if per == 1 and type_ == 1:
        return 0.0
    
    if type_ == 1:
        return FV_Temp(rate, per - 2, payment, pv, 0) * rate
    else:
        return FV_Temp(rate, per - 1, payment, pv, 0) * rate


def FV_Temp(rate: float, nper: float, pmt_: float, pv: float, type_: int) -> float:
    """Helper interno para calcular valor futuro temporal."""
    if rate == 0:
        return -(pv + pmt_ * nper)
    factor = (1 + rate) ** nper
    return -(pv * factor + pmt_ * (factor - 1) / rate)


def Pmt(rate: float, nper: float, pv: float, fv: float = 0, type_: int = 0) -> float:
    """
    Description
        Pago para anualidad basado en pagos periódicos constantes.

    Args
        rate: Tasa de interés por periodo.
        nper: Número total de periodos.
        pv: Valor presente.
        fv: Valor futuro (por defecto 0).
        type_: Tipo de pago (0=final, 1=inicio).

    Returns
        float: Pago por periodo.

    Usage Example
        >>> pmt(0.1/12, 36, 8000)
        -258.14

    Cost
        O(1)
    """
    if rate == 0:
        return -(pv + fv) / nper
    
    factor = (1 + rate) ** nper
    
    if type_ == 0:
        return -(rate * (pv * factor + fv)) / (factor - 1)
    else:
        return -(rate * (pv * factor + fv)) / ((factor - 1) * (1 + rate))


def PPmt(rate: float, per: float, nper: float, pv: float, fv: float = 0, type_: int = 0) -> float:
    """
    Description
        Pago principal para periodo dado de una anualidad.

    Args
        rate: Tasa de interés por periodo.
        per: Periodo (1 a nper).
        nper: Número total de periodos.
        pv: Valor presente.
        fv: Valor futuro (por defecto 0).
        type_: Tipo de pago (0=final, 1=inicio).

    Returns
        float: Pago principal.

    Usage Example
        >>> ppmt(0.1/12, 1, 36, 8000)
        -191.47

    Cost
        O(1)
    """
    payment = pmt(rate, nper, pv, fv, type_)
    interest = ipmt(rate, per, nper, pv, fv, type_)
    return payment - interest


def PV(rate: float, nper: float, pmt_: float, fv: float = 0, type_: int = 0) -> float:
    """
    Description
        Valor actual de una anualidad.

    Args
        rate: Tasa de interés por periodo.
        nper: Número total de periodos.
        pmt_: Pago por periodo.
        fv: Valor futuro (por defecto 0).
        type_: Tipo de pago (0=final, 1=inicio).

    Returns
        float: Valor presente.

    Usage Example
        >>> pv(0.08/12, 20*12, -500)
        59777.15

    Cost
        O(1)
    """
    if rate == 0:
        return -(fv + pmt_ * nper)
    
    factor = (1 + rate) ** nper
    
    if type_ == 0:
        return -(fv + pmt_ * (factor - 1) / rate) / factor
    else:
        return -(fv + pmt_ * (factor - 1) / rate * (1 + rate)) / factor


def Rate(
    nper: float,
    pmt_: float,
    pv: float,
    fv: float = 0,
    type_: int = 0,
    guess: float = 0.1
) -> float:
    """
    Description
        Tasa de interés por periodo de una anualidad.

    Args
        nper: Número total de periodos.
        pmt_: Pago por periodo.
        pv: Valor presente.
        fv: Valor futuro (por defecto 0).
        type_: Tipo de pago (0=final, 1=inicio).
        guess: Estimación inicial (por defecto 0.1).

    Returns
        float: Tasa de interés por periodo.

    Usage Example
        >>> rate(60, -1000, 50000)
        0.015

    Cost
        O(n) iteraciones de Newton-Raphson
    """
    rate_val = guess
    max_iter = 100
    precision = 1e-6
    
    for _ in range(max_iter):
        f = _rate_function(rate_val, nper, pmt_, pv, fv, type_)
        if abs(f) < precision:
            return rate_val
        
        df = _rate_derivative(rate_val, nper, pmt_, pv, fv, type_)
        if df == 0:
            break
        
        rate_val = rate_val - f / df
    
    return rate_val


def _rate_function(r: float, n: float, p: float, pv_: float, fv_: float, t: int) -> float:
    """Helper para calcular función de tasa."""
    if r == 0:
        return pv_ + p * n + fv_
    factor = (1 + r) ** n
    if t == 0:
        return pv_ * factor + p * (factor - 1) / r + fv_
    else:
        return pv_ * factor + p * (factor - 1) / r * (1 + r) + fv_


def _rate_derivative(r: float, n: float, p: float, pv_: float, fv_: float, t: int) -> float:
    """Helper para calcular derivada de función de tasa."""
    if r == 0:
        return 0
    factor = (1 + r) ** n
    if t == 0:
        return n * pv_ * factor / (1 + r) + p * (n * factor / (1 + r) / r - (factor - 1) / (r ** 2))
    else:
        return n * pv_ * factor / (1 + r) + p * ((n * factor / (1 + r) / r - (factor - 1) / (r ** 2)) * (1 + r) + (factor - 1) / r)


def SLN(cost: float, salvage: float, life: float) -> float:
    """
    Description
        Depreciación lineal de un bien durante único periodo.

    Args
        cost: Costo inicial del bien.
        salvage: Valor al término de vida útil.
        life: Duración de vida útil.

    Returns
        float: Depreciación lineal.

    Usage Example
        >>> sln(10000, 1000, 5)
        1800.0

    Cost
        O(1)
    """
    return (cost - salvage) / life


def SYD(cost: float, salvage: float, life: float, period: float) -> float:
    """
    Description
        Depreciación por suma de dígitos de años para un periodo.

    Args
        cost: Costo inicial del bien.
        salvage: Valor al término de vida útil.
        life: Duración de vida útil.
        period: Periodo para el cual se calcula.

    Returns
        float: Depreciación para el periodo.

    Usage Example
        >>> syd(10000, 1000, 5, 1)
        3000.0

    Cost
        O(1)
    """
    sum_of_years = life * (life + 1) / 2
    return (cost - salvage) * (life - period + 1) / sum_of_years


def NPV(rate: float, values: List[float]) -> float:
    """
    Description
        Calcula Valor Presente Neto (NPV) de flujos de caja.

    Args
        rate: Tasa de descuento por periodo.
        values: Lista de flujos de caja (valores).

    Returns
        float: Valor presente neto.

    Usage Example
        >>> npv(0.1, [-10000, 3000, 4200, 6800])
        1188.44

    Cost
        O(n) donde n es número de flujos
    """
    npv_value = 0.0
    for i, value in enumerate(values):
        npv_value += value / ((1 + rate) ** (i + 1))
    return npv_value


def IRR(values: List[float], guess: float = 0.1) -> float:
    """
    Description
        Calcula Tasa Interna de Retorno (IRR) de flujos de caja.

    Args
        values: Lista de flujos de caja (debe incluir al menos un valor negativo y uno positivo).
        guess: Estimación inicial (por defecto 0.1).

    Returns
        float: Tasa interna de retorno.

    Raises
        ValueError: Si no converge o valores inválidos.

    Usage Example
        >>> irr([-10000, 3000, 4200, 6800])
        0.1896

    Cost
        O(n*iterations) - método iterativo Newton-Raphson
    """
    # Verificar que hay valores positivos y negativos
    if not any(v < 0 for v in values) or not any(v > 0 for v in values):
        raise ValueError("IRR requiere al menos un flujo negativo y uno positivo")
    
    # Método Newton-Raphson
    rate = guess
    max_iterations = 100
    tolerance = 1e-6
    
    for _ in range(max_iterations):
        # Calcular NPV y su derivada
        npv_val = 0.0
        npv_derivative = 0.0
        
        for i, value in enumerate(values):
            period = i + 1
            npv_val += value / ((1 + rate) ** period)
            npv_derivative -= period * value / ((1 + rate) ** (period + 1))
        
        # Si NPV es suficientemente cercano a 0, hemos encontrado IRR
        if abs(npv_val) < tolerance:
            return rate
        
        # Evitar división por cero
        if abs(npv_derivative) < tolerance:
            raise ValueError("IRR no converge - derivada cercana a cero")
        
        # Actualizar rate usando Newton-Raphson
        rate = rate - npv_val / npv_derivative
    
    raise ValueError("IRR no converge en número máximo de iteraciones")


def MIRR(values: List[float], finance_rate: float, reinvest_rate: float) -> float:
    """
    Description
        Calcula Tasa Interna de Retorno Modificada (MIRR).

    Args
        values: Lista de flujos de caja.
        finance_rate: Tasa de interés para flujos negativos (financiamiento).
        reinvest_rate: Tasa de interés para flujos positivos (reinversión).

    Returns
        float: Tasa interna de retorno modificada.

    Usage Example
        >>> mirr([-10000, 3000, 4200, 6800], 0.1, 0.12)
        0.1326

    Cost
        O(n) donde n es número de flujos
    """
    n = len(values)
    
    # Calcular valor presente de flujos negativos
    pv_negative = 0.0
    for i, value in enumerate(values):
        if value < 0:
            pv_negative += value / ((1 + finance_rate) ** i)
    
    # Calcular valor futuro de flujos positivos
    fv_positive = 0.0
    for i, value in enumerate(values):
        if value > 0:
            fv_positive += value * ((1 + reinvest_rate) ** (n - i - 1))
    
    # Calcular MIRR
    if pv_negative == 0:
        raise ValueError("MIRR requiere al menos un flujo negativo")
    
    mirr_val = ((-fv_positive / pv_negative) ** (1 / (n - 1))) - 1
    return mirr_val


def NPer(rate: float, pmt: float, pv: float, fv: float = 0.0, type_: int = 0) -> float:
    """
    Description
        Calcula número de períodos para inversión o préstamo.

    Args
        rate: Tasa de interés por periodo.
        pmt: Pago por periodo.
        pv: Valor presente.
        fv: Valor futuro (por defecto 0).
        type_: 0 = pago al final, 1 = pago al inicio.

    Returns
        float: Número de períodos.

    Usage Example
        >>> nper(0.01, -100, 1000, 0)
        10.4

    Cost
        O(1) con cálculo logarítmico
    """
    import math
    
    if rate == 0:
        # Caso especial: sin interés
        return -(pv + fv) / pmt
    
    # Ajustar pago según tipo
    if type_ == 1:
        pmt = pmt * (1 + rate)
    
    # Fórmula NPER
    numerator = math.log((pmt - fv * rate) / (pmt + pv * rate))
    denominator = math.log(1 + rate)
    
    return numerator / denominator

