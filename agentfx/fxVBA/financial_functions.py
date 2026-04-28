"""
Access Financial Functions Module.

Description
    Funciones financieras compatibles con VBA/Access para cálculo de
    depreciación, anualidades y préstamos.
"""

from typing import List

from agentfx.fxNumeric.finance_functions import (
    ddb as _core_ddb,
    future_value as _core_fv,
    ipmt as _core_ipmt,
    irr as _core_irr,
    mirr as _core_mirr,
    nper as _core_nper,
    npv as _core_npv,
    pmt as _core_pmt,
    ppmt as _core_ppmt,
    present_value as _core_pv,
    rate as _core_rate,
    sln as _core_sln,
    syd as _core_syd,
)

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
    return _core_ddb(cost, salvage, life, period, factor)


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
    return _core_fv(rate, nper, pmt, pv, type_)


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
    return _core_ipmt(rate, int(per), int(nper), pv, fv, type_)


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
    return _core_pmt(rate, nper, pv, fv, type_)


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
    return _core_ppmt(rate, int(per), int(nper), pv, fv, type_)


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
    return _core_pv(rate, nper, pmt_, fv, type_)


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
    return _core_rate(nper, pmt_, pv, fv, type_, guess)


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
    return _core_sln(cost, salvage, life)


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
    return _core_syd(cost, salvage, int(life), int(period))


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
    return _core_npv(rate, values)


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
    return _core_irr(values, guess)


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
    return _core_mirr(values, finance_rate, reinvest_rate)


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
    return _core_nper(rate, pmt, pv, fv, type_)


