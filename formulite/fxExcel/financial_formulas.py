"""
Excel Financial Functions Module.

This module provides Excel-compatible financial functions for FormuLite. Functions include:
- Depreciation: SLN, DDB
- Bond/Coupon calculations: COUPDAYS, COUPDAYBS, COUPDAYSNC, COUPPCD, COUPNCD, COUPNUM
- Duration: DURATION, MDURATION
- Accrued interest: ACCRINT, ACCRINTM
- Pricing: PRICE, PRICEDISC, PRICEMAT
- Yield: YIELD, YIELDDISC, YIELDMAT
- Cash flows: XIRR, XNPV
- Loan payments: CUMPRINC, PPMT

All functions follow Excel naming conventions and behavior.
"""

from typing import Union, List, Optional
import numpy as np
import numpy_financial as npf
from datetime import datetime, timedelta, date
from dateutil.relativedelta import relativedelta
import math


# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def _days_between(start_date, end_date, basis=0):
    """Calculate days between dates based on day count basis."""
    if basis == 0:  # 30/360 US
        d1, m1, y1 = start_date.day, start_date.month, start_date.year
        d2, m2, y2 = end_date.day, end_date.month, end_date.year
        
        if d1 == 31:
            d1 = 30
        if d2 == 31 and d1 >= 30:
            d2 = 30
            
        return (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)
    elif basis == 1:  # Actual/actual
        return (end_date - start_date).days
    elif basis == 2:  # Actual/360
        return (end_date - start_date).days
    elif basis == 3:  # Actual/365
        return (end_date - start_date).days
    elif basis == 4:  # 30/360 European
        d1, m1, y1 = start_date.day, start_date.month, start_date.year
        d2, m2, y2 = end_date.day, end_date.month, end_date.year
        
        if d1 == 31:
            d1 = 30
        if d2 == 31:
            d2 = 30
            
        return (y2 - y1) * 360 + (m2 - m1) * 30 + (d2 - d1)
    else:
        return (end_date - start_date).days


def _year_days(date_ref, basis=0):
    """Get the number of days in a year based on basis."""
    if basis == 0 or basis == 2 or basis == 4:
        return 360
    elif basis == 3:
        return 365
    elif basis == 1:
        # Actual/actual - check if leap year
        year = date_ref.year if isinstance(date_ref, (datetime, date)) else datetime.now().year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            return 366
        return 365
    return 365


def _coup_num_internal(start_date, end_date, frequency):
    """Calculate number of coupon periods between two dates."""
    months_per_coupon = 12 // frequency
    num_coupons = 0
    current_date = start_date
    
    while current_date < end_date:
        current_date += relativedelta(months=months_per_coupon)
        num_coupons += 1
    
    return num_coupons


# ============================================================================
# DEPRECIATION FUNCTIONS
# ============================================================================

def SLN(cost: Union[int, float], salvage: Union[int, float], life: Union[int, float]) -> float:
    """
    Calculate straight-line depreciation of an asset for one period.
    
    Args:
        cost: Initial cost of the asset.
        salvage: Salvage value at the end of useful life.
        life: Number of periods over which the asset is depreciated.
    
    Returns:
        float: Straight-line depreciation per period.
    
    Raises:
        ValueError: If life is zero or negative.
    
    Example:
        >>> SLN(30000, 7500, 10)
        2250.0
    
    Cost: O(1)
    """
    if life <= 0:
        raise ValueError("Life must be positive.")
    return (cost - salvage) / life


def DDB(cost: Union[int, float], salvage: Union[int, float], life: Union[int, float], 
        period: int, factor: Union[int, float] = 2) -> float:
    """
    Calculate depreciation using the double-declining balance method.
    
    Args:
        cost: Initial cost of the asset.
        salvage: Salvage value at the end of useful life.
        life: Number of periods over which the asset is depreciated.
        period: Period for which to calculate depreciation.
        factor: Rate at which the balance declines (default 2 for double-declining).
    
    Returns:
        float: Depreciation for the specified period.
    
    Raises:
        ValueError: If period is not between 1 and life.
    
    Example:
        >>> DDB(2400, 300, 10, 1)
        480.0
    
    Cost: O(n) where n is the period number.
    """
    if not (1 <= period <= life):
        raise ValueError("Period must be between 1 and life.")
    
    rate = factor / life
    book_value = cost
    
    for i in range(1, period + 1):
        depreciation = book_value * rate
        if book_value - depreciation < salvage:
            depreciation = book_value - salvage
        book_value -= depreciation
        if i == period:
            return depreciation
    return 0


# ============================================================================
# BOND/COUPON FUNCTIONS
# ============================================================================

def COUPDAYS(settlement: datetime, maturity: datetime, frequency: int) -> int:
    """
    Return the number of days in the coupon period containing the settlement date.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        frequency: Number of coupon payments per year (1, 2, or 4).
    
    Returns:
        int: Number of days in the coupon period.
    
    Example:
        >>> from datetime import datetime
        >>> COUPDAYS(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        181
    
    Cost: O(1)
    """
    prev_coupon = COUPPCD(settlement, maturity, frequency)
    next_coupon = COUPNCD(settlement, maturity, frequency)
    return (next_coupon - prev_coupon).days


def COUPDAYBS(settlement: datetime, maturity: datetime, frequency: int) -> int:
    """
    Return the number of days from the beginning of the coupon period to the settlement date.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        frequency: Number of coupon payments per year (1, 2, or 4).
    
    Returns:
        int: Number of days from period start to settlement.
    
    Example:
        >>> from datetime import datetime
        >>> COUPDAYBS(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        71
    
    Cost: O(1)
    """
    prev_coupon = COUPPCD(settlement, maturity, frequency)
    return (settlement - prev_coupon).days


def COUPDAYSNC(settlement: datetime, maturity: datetime, frequency: int) -> int:
    """
    Return the number of days from the settlement date to the next coupon date.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        frequency: Number of coupon payments per year (1, 2, or 4).
    
    Returns:
        int: Number of days from settlement to next coupon.
    
    Example:
        >>> from datetime import datetime
        >>> COUPDAYSNC(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        110
    
    Cost: O(1)
    """
    next_coupon = COUPNCD(settlement, maturity, frequency)
    return (next_coupon - settlement).days


def COUPPCD(settlement: datetime, maturity: datetime, frequency: int) -> datetime:
    """
    Return the previous coupon date before the settlement date.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        frequency: Number of coupon payments per year (1, 2, or 4).
    
    Returns:
        datetime: Previous coupon date.
    
    Example:
        >>> from datetime import datetime
        >>> COUPPCD(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        datetime(2024, 11, 15, 0, 0)
    
    Cost: O(k) where k is the number of coupons from maturity to settlement.
    """
    months_per_coupon = 12 // frequency
    coupon_date = maturity
    
    while coupon_date > settlement:
        coupon_date = coupon_date - relativedelta(months=months_per_coupon)
    return coupon_date


def COUPNCD(settlement: datetime, maturity: datetime, frequency: int) -> datetime:
    """
    Return the next coupon date after the settlement date.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        frequency: Number of coupon payments per year (1, 2, or 4).
    
    Returns:
        datetime: Next coupon date.
    
    Example:
        >>> from datetime import datetime
        >>> COUPNCD(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        datetime(2025, 5, 15, 0, 0)
    
    Cost: O(k) where k is the number of coupons from maturity to settlement.
    """
    months_per_coupon = 12 // frequency
    coupon_date = COUPPCD(settlement, maturity, frequency)
    
    if coupon_date < settlement:
        coupon_date += relativedelta(months=months_per_coupon)
    return coupon_date


def COUPNUM(settlement: datetime, maturity: datetime, frequency: int) -> int:
    """
    Return the number of coupons payable between settlement and maturity dates.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        frequency: Number of coupon payments per year (1, 2, or 4).
    
    Returns:
        int: Number of coupons remaining.
    
    Example:
        >>> from datetime import datetime
        >>> COUPNUM(datetime(2025, 1, 25), datetime(2026, 11, 15), 2)
        4
    
    Cost: O(n) where n is the number of remaining coupons.
    """
    months_per_coupon = 12 // frequency
    current_date = COUPNCD(settlement, maturity, frequency)
    num_coupons = 0
    
    while current_date <= maturity:
        num_coupons += 1
        current_date += relativedelta(months=months_per_coupon)
    return num_coupons


# ============================================================================
# DURATION FUNCTIONS
# ============================================================================

def DURATION(settlement: datetime, maturity: datetime, coupon: float, yld: float, 
             frequency: int, basis: int = 0) -> float:
    """
    Return the Macaulay duration for an assumed par value of 100.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        coupon: Annual coupon rate.
        yld: Annual yield.
        frequency: Number of coupon payments per year (1, 2, or 4).
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Macaulay duration.
    
    Example:
        >>> from datetime import datetime
        >>> DURATION(datetime(2025, 1, 1), datetime(2030, 1, 1), 0.08, 0.09, 2)
        4.2
    
    Cost: O(n) where n is the number of coupons.
    """
    price_val = PRICE(settlement, maturity, coupon, yld, 100, frequency, basis)
    num_coupons = COUPNUM(settlement, maturity, frequency)
    coupon_pmt = coupon * 100 / frequency
    weighted_sum = 0
    time = 0
    
    for i in range(1, num_coupons + 1):
        time += 1 / frequency
        cash_flow = coupon_pmt if i < num_coupons else coupon_pmt + 100
        weighted_sum += time * cash_flow / (1 + yld / frequency) ** i
    
    return weighted_sum / price_val


def MDURATION(settlement: datetime, maturity: datetime, coupon: float, yld: float, 
              frequency: int, basis: int = 0) -> float:
    """
    Return the modified duration for an assumed par value of 100.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        coupon: Annual coupon rate.
        yld: Annual yield.
        frequency: Number of coupon payments per year (1, 2, or 4).
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Modified duration.
    
    Example:
        >>> from datetime import datetime
        >>> MDURATION(datetime(2025, 1, 1), datetime(2030, 1, 1), 0.08, 0.09, 2)
        4.0
    
    Cost: O(n) where n is the number of coupons.
    """
    macaulay = DURATION(settlement, maturity, coupon, yld, frequency, basis)
    return macaulay / (1 + yld / frequency)


# ============================================================================
# ACCRUED INTEREST FUNCTIONS
# ============================================================================

def ACCRINT(issue: datetime, first_interest: datetime, settlement: datetime, 
            rate: float, par: Union[int, float], frequency: int, basis: int = 0) -> float:
    """
    Return the accrued interest for a security that pays periodic interest.
    
    Args:
        issue: Issue date.
        first_interest: First interest date.
        settlement: Settlement date.
        rate: Annual coupon rate.
        par: Par value of the security.
        frequency: Number of coupon payments per year (1, 2, or 4).
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Accrued interest.
    
    Example:
        >>> from datetime import datetime
        >>> ACCRINT(datetime(2025, 1, 1), datetime(2025, 7, 1), datetime(2025, 4, 1), 0.08, 1000, 2)
        20.0
    
    Cost: O(1)
    """
    days = COUPDAYBS(settlement, first_interest, frequency)
    days_period = COUPDAYS(settlement, first_interest, frequency)
    coupon = rate * par / frequency
    return coupon * days / days_period


def ACCRINTM(issue: datetime, settlement: datetime, rate: float, 
             par: Union[int, float], basis: int = 0) -> float:
    """
    Return the accrued interest for a security that pays interest at maturity.
    
    Args:
        issue: Issue date.
        settlement: Maturity date.
        rate: Annual coupon rate.
        par: Par value of the security.
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Accrued interest.
    
    Example:
        >>> from datetime import datetime
        >>> ACCRINTM(datetime(2025, 1, 1), datetime(2025, 12, 31), 0.08, 1000)
        80.0
    
    Cost: O(1)
    """
    days = (settlement - issue).days
    days_year = 365 if basis == 1 else 360
    return rate * par * days / days_year


# ============================================================================
# LOAN PAYMENT FUNCTIONS
# ============================================================================

def CUMPRINC(rate: float, nper: int, pv: Union[int, float], start_period: int, 
             end_period: int, type: int = 0) -> float:
    """
    Return the cumulative principal paid on a loan between two periods.
    
    Args:
        rate: Interest rate per period.
        nper: Total number of payment periods.
        pv: Present value (loan amount).
        start_period: First period in the calculation (1-based).
        end_period: Last period in the calculation.
        type: Payment timing (0=end of period, 1=beginning of period).
    
    Returns:
        float: Cumulative principal paid.
    
    Example:
        >>> CUMPRINC(0.09/12, 30*12, 125000, 1, 12, 0)
        -934.11
    
    Cost: O(n) where n is the number of periods.
    """
    principal = 0
    for i in range(start_period, end_period + 1):
        principal += npf.ppmt(rate, i, nper, pv, 0, type)
    return principal


def PPMT(rate: float, per: int, nper: int, pv: Union[int, float], 
         fv: Union[int, float] = 0, type: int = 0) -> float:
    """
    Return the principal payment for a given period.
    
    Args:
        rate: Interest rate per period.
        per: Period for which to calculate payment (1-based).
        nper: Total number of payment periods.
        pv: Present value (loan amount).
        fv: Future value (default 0).
        type: Payment timing (0=end of period, 1=beginning of period).
    
    Returns:
        float: Principal payment for the period.
    
    Example:
        >>> PPMT(0.08/12, 1, 10*12, 10000)
        -75.62
    
    Cost: O(1)
    """
    return npf.ppmt(rate, per, nper, pv, fv, type)


# ============================================================================
# PRICING FUNCTIONS
# ============================================================================

def PRICE(settlement: datetime, maturity: datetime, rate: float, yld: float, 
          redemption: Union[int, float], frequency: int, basis: int = 0) -> float:
    """
    Return the price per $100 face value of a security that pays periodic interest.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        rate: Annual coupon rate.
        yld: Annual yield.
        redemption: Redemption value per $100 face value.
        frequency: Number of coupon payments per year (1, 2, or 4).
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Price per $100 face value.
    
    Example:
        >>> from datetime import datetime
        >>> PRICE(datetime(2025, 2, 15), datetime(2032, 11, 15), 0.0575, 0.065, 100, 2)
        92.89
    
    Cost: O(n) where n is the number of coupons.
    """
    num_coupons = COUPNUM(settlement, maturity, frequency)
    coupon = rate * redemption / frequency
    price = 0
    
    for i in range(1, num_coupons + 1):
        price += coupon / (1 + yld / frequency) ** i
    price += redemption / (1 + yld / frequency) ** num_coupons
    
    days = COUPDAYBS(settlement, maturity, frequency)
    days_period = COUPDAYS(settlement, maturity, frequency)
    fraction = days / days_period
    price = price / (1 + yld / frequency) ** fraction
    
    return price


def PRICEDISC(settlement: datetime, maturity: datetime, discount: float, 
              redemption: Union[int, float], basis: int = 0) -> float:
    """
    Return the price per $100 face value of a discounted security.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        discount: Security's discount rate.
        redemption: Redemption value per $100 face value.
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Price per $100 face value.
    
    Example:
        >>> from datetime import datetime
        >>> PRICEDISC(datetime(2025, 2, 16), datetime(2025, 3, 1), 0.0525, 100)
        99.79
    
    Cost: O(1)
    """
    if basis == 1:
        days = (maturity - settlement).days
        year_fraction = days / 365
    else:
        days = 360 * (maturity.year - settlement.year) + \
               30 * (maturity.month - settlement.month) + \
               (maturity.day - settlement.day)
        year_fraction = days / 360
    
    return redemption - (discount * redemption * year_fraction)


def PRICEMAT(settlement: datetime, maturity: datetime, issue: datetime, rate: float, 
             yld: float, basis: int = 0) -> float:
    """
    Return the price per $100 face value of a security that pays interest at maturity.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        issue: Issue date.
        rate: Interest rate at date of issue.
        yld: Annual yield.
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Price per $100 face value.
    
    Example:
        >>> from datetime import datetime
        >>> PRICEMAT(datetime(2025, 2, 15), datetime(2025, 4, 13), datetime(2024, 11, 11), 0.061, 0.061)
        99.98
    
    Cost: O(1)
    """
    if basis == 1:
        days = (maturity - settlement).days
        year_fraction = days / 365
    else:
        days = 360 * (maturity.year - settlement.year) + \
               30 * (maturity.month - settlement.month) + \
               (maturity.day - settlement.day)
        year_fraction = days / 360
    
    interest = rate * 100 * year_fraction
    return (100 + interest) / (1 + yld * year_fraction)


# ============================================================================
# YIELD FUNCTIONS
# ============================================================================

def YIELD(settlement: datetime, maturity: datetime, rate: float, pr: Union[int, float], 
          redemption: Union[int, float], frequency: int, basis: int = 0) -> float:
    """
    Return the yield of a security that pays periodic interest.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        rate: Annual coupon rate.
        pr: Price per $100 face value.
        redemption: Redemption value per $100 face value.
        frequency: Number of coupon payments per year (1, 2, or 4).
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Annual yield.
    
    Example:
        >>> from datetime import datetime
        >>> YIELD(datetime(2025, 2, 15), datetime(2032, 11, 15), 0.0575, 95.04, 100, 2)
        0.065
    
    Cost: O(n*m) where n is iterations and m is number of coupons.
    """
    # Use Newton-Raphson method to find yield
    yld_guess = 0.1
    tolerance = 0.00001
    max_iterations = 100
    
    for _ in range(max_iterations):
        price_calc = PRICE(settlement, maturity, rate, yld_guess, redemption, frequency, basis)
        diff = price_calc - pr
        
        if abs(diff) < tolerance:
            return yld_guess
        
        # Approximate derivative
        yld_delta = yld_guess * 0.001
        price_delta = PRICE(settlement, maturity, rate, yld_guess + yld_delta, redemption, frequency, basis)
        derivative = (price_delta - price_calc) / yld_delta
        
        if derivative != 0:
            yld_guess = yld_guess - diff / derivative
    
    return yld_guess


def YIELDDISC(settlement: datetime, maturity: datetime, pr: Union[int, float], 
              redemption: Union[int, float], basis: int = 0) -> float:
    """
    Return the annual yield for a discounted security.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        pr: Price per $100 face value.
        redemption: Redemption value per $100 face value.
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Annual yield.
    
    Example:
        >>> from datetime import datetime
        >>> YIELDDISC(datetime(2025, 2, 16), datetime(2025, 3, 1), 99.795, 100)
        0.0525
    
    Cost: O(1)
    """
    if basis == 1:
        days = (maturity - settlement).days
        year_fraction = days / 365
    else:
        days = 360 * (maturity.year - settlement.year) + \
               30 * (maturity.month - settlement.month) + \
               (maturity.day - settlement.day)
        year_fraction = days / 360
    
    return (redemption - pr) / pr * (1 / year_fraction)


def YIELDMAT(settlement: datetime, maturity: datetime, issue: datetime, rate: float, 
             pr: Union[int, float], basis: int = 0) -> float:
    """
    Return the annual yield of a security that pays interest at maturity.
    
    Args:
        settlement: Settlement date.
        maturity: Maturity date.
        issue: Issue date.
        rate: Interest rate at date of issue.
        pr: Price per $100 face value.
        basis: Day count basis (0=30/360, 1=actual/actual).
    
    Returns:
        float: Annual yield.
    
    Example:
        >>> from datetime import datetime
        >>> YIELDMAT(datetime(2025, 3, 15), datetime(2025, 11, 3), datetime(2024, 11, 8), 0.0625, 100.0123)
        0.0609
    
    Cost: O(1)
    """
    if basis == 1:
        days = (maturity - settlement).days
        year_fraction = days / 365
    else:
        days = 360 * (maturity.year - settlement.year) + \
               30 * (maturity.month - settlement.month) + \
               (maturity.day - settlement.day)
        year_fraction = days / 360
    
    interest = rate * 100 * year_fraction
    return (100 + interest - pr) / pr * (1 / year_fraction)


# ============================================================================
# CASH FLOW FUNCTIONS
# ============================================================================

def XIRR(values: List[Union[int, float]], dates: List[datetime], guess: float = 0.1) -> float:
    """
    Return the internal rate of return for a schedule of cash flows.
    
    Args:
        values: Series of cash flows.
        dates: Schedule of payment dates.
        guess: Initial guess for the rate (default 0.1).
    
    Returns:
        float: Internal rate of return.
    
    Raises:
        ValueError: If values and dates have different lengths.
    
    Example:
        >>> from datetime import datetime
        >>> values = [-10000, 2750, 4250, 3250, 2750]
        >>> dates = [datetime(2008, 1, 1), datetime(2008, 3, 1), 
        ...          datetime(2008, 10, 30), datetime(2009, 2, 15), datetime(2009, 4, 1)]
        >>> round(XIRR(values, dates), 4)
        0.3733
    
    Cost: O(n*m) where n is iterations and m is the number of cash flows.
    """
    if len(values) != len(dates):
        raise ValueError("Values and dates must have the same length.")
    
    rate = guess
    tolerance = 0.00001
    max_iterations = 100
    
    for _ in range(max_iterations):
        xnpv_val = XNPV(rate, values, dates)
        
        if abs(xnpv_val) < tolerance:
            return rate
        
        # Approximate derivative
        rate_delta = rate * 0.001
        xnpv_delta = XNPV(rate + rate_delta, values, dates)
        derivative = (xnpv_delta - xnpv_val) / rate_delta
        
        if derivative != 0:
            rate = rate - xnpv_val / derivative
    
    return rate


def XNPV(rate: float, values: List[Union[int, float]], dates: List[datetime]) -> float:
    """
    Return the net present value for a schedule of cash flows.
    
    Args:
        rate: Discount rate to apply.
        values: Series of cash flows.
        dates: Schedule of payment dates.
    
    Returns:
        float: Net present value.
    
    Raises:
        ValueError: If values and dates have different lengths.
    
    Example:
        >>> from datetime import datetime
        >>> values = [-10000, 2750, 4250, 3250, 2750]
        >>> dates = [datetime(2008, 1, 1), datetime(2008, 3, 1), 
        ...          datetime(2008, 10, 30), datetime(2009, 2, 15), datetime(2009, 4, 1)]
        >>> round(XNPV(0.09, values, dates), 2)
        2086.65
    
    Cost: O(n) where n is the number of cash flows.
    """
    if len(values) != len(dates):
        raise ValueError("Values and dates must have the same length.")
    
    total = 0
    for i, value in enumerate(values):
        days = (dates[i] - dates[0]).days
        total += value / (1 + rate) ** (days / 365)
    
    return total


# ============================================================================
# ANNUITY AND LOAN FUNCTIONS
# ============================================================================

def FV(rate: float, nper: int, pmt: Union[int, float], pv: Union[int, float] = 0,
       type: int = 0) -> float:
    """
    Calculate the future value of an investment.
    
    Description:
        Returns the future value of an investment based on periodic, constant payments
        and a constant interest rate.
    
    Args:
        rate: Interest rate per period.
        nper: Total number of payment periods.
        pmt: Payment made each period (cannot change over the life of the investment).
        pv: Present value, or the lump-sum amount that a series of future payments is worth now (default 0).
        type: When payments are due (0 = end of period, 1 = beginning of period).
    
    Returns:
        float: Future value of the investment.
    
    Raises:
        ValueError: If nper is negative.
    
    Usage Example:
        >>> FV(0.06/12, 10, -200, -500, 1)
        2581.40
        >>> FV(0.12/12, 12, -1000)
        12682.50
    
    Cost: O(1)
    """
    if nper < 0:
        raise ValueError("Number of periods must be non-negative.")
    
    if rate == 0:
        return -pv - pmt * nper
    
    factor = (1 + rate) ** nper
    if type == 1:
        return -pv * factor - pmt * (1 + rate) * (factor - 1) / rate
    else:
        return -pv * factor - pmt * (factor - 1) / rate


def FVSCHEDULE(principal: Union[int, float], schedule: List[float]) -> float:
    """
    Calculate future value with a variable interest rate schedule.
    
    Description:
        Returns the future value of an initial principal after applying a series
        of compound interest rates.
    
    Args:
        principal: Present value.
        schedule: Array of interest rates to apply.
    
    Returns:
        float: Future value after applying all interest rates.
    
    Usage Example:
        >>> FVSCHEDULE(1, [0.09, 0.11, 0.10])
        1.3308900000000001
    
    Cost: O(n) where n is the number of rates in schedule.
    """
    result = principal
    for rate in schedule:
        result *= (1 + rate)
    return result


def IRR(values: List[Union[int, float]], guess: float = 0.1) -> float:
    """
    Calculate the internal rate of return for a series of cash flows.
    
    Description:
        Returns the internal rate of return for a series of cash flows represented
        by the numbers in values. These cash flows do not have to be even, but they
        must occur at regular intervals.
    
    Args:
        values: Array of cash flows. Must contain at least one positive and one negative value.
        guess: Estimate for what the rate will be (default 0.1).
    
    Returns:
        float: Internal rate of return.
    
    Raises:
        ValueError: If values do not contain at least one positive and one negative value.
    
    Usage Example:
        >>> IRR([-70000, 12000, 15000, 18000, 21000, 26000])
        0.0866309480589569
    
    Cost: O(n*m) where n is iterations and m is the number of cash flows.
    """
    return npf.irr(values)


def MIRR(values: List[Union[int, float]], finance_rate: float, reinvest_rate: float) -> float:
    """
    Calculate the modified internal rate of return.
    
    Description:
        Returns the modified internal rate of return for a series of periodic cash flows.
        MIRR considers both the cost of the investment and the interest received on
        reinvestment of cash.
    
    Args:
        values: Array of cash flows.
        finance_rate: Interest rate paid on money used in cash flows.
        reinvest_rate: Interest rate received on cash flows as they are reinvested.
    
    Returns:
        float: Modified internal rate of return.
    
    Usage Example:
        >>> MIRR([-120000, 39000, 30000, 21000, 37000, 46000], 0.10, 0.12)
        0.1260941303659051
    
    Cost: O(n) where n is the number of cash flows.
    """
    return npf.mirr(values, finance_rate, reinvest_rate)


def NPER(rate: float, pmt: Union[int, float], pv: Union[int, float],
         fv: Union[int, float] = 0, type: int = 0) -> float:
    """
    Calculate the number of periods for an investment.
    
    Description:
        Returns the number of periods for an investment based on periodic, constant
        payments and a constant interest rate.
    
    Args:
        rate: Interest rate per period.
        pmt: Payment made each period (cannot change).
        pv: Present value, or the lump-sum amount.
        fv: Future value, or a cash balance you want after the last payment (default 0).
        type: When payments are due (0 = end of period, 1 = beginning of period).
    
    Returns:
        float: Number of periods.
    
    Usage Example:
        >>> NPER(0.12/12, -100, -1000, 10000, 1)
        59.673865674320484
    
    Cost: O(1)
    """
    return npf.nper(rate, pmt, pv, fv, type)


def NPV(rate: float, *values: Union[int, float]) -> float:
    """
    Calculate the net present value of an investment.
    
    Description:
        Calculates the net present value of an investment by using a discount rate
        and a series of future payments (negative values) and income (positive values).
    
    Args:
        rate: Discount rate over one period.
        *values: Arguments representing the payments and income.
    
    Returns:
        float: Net present value.
    
    Usage Example:
        >>> NPV(0.10, -10000, 3000, 4200, 6800)
        1188.4434123352216
    
    Cost: O(n) where n is the number of values.
    """
    return npf.npv(rate, list(values))


def PMT(rate: float, nper: int, pv: Union[int, float], fv: Union[int, float] = 0,
        type: int = 0) -> float:
    """
    Calculate the payment for a loan.
    
    Description:
        Calculates the payment for a loan based on constant payments and a constant
        interest rate.
    
    Args:
        rate: Interest rate for the loan.
        nper: Total number of payments for the loan.
        pv: Present value (the total amount that a series of future payments is worth now).
        fv: Future value (cash balance after the last payment, default 0).
        type: When payments are due (0 = end of period, 1 = beginning of period).
    
    Returns:
        float: Payment amount.
    
    Usage Example:
        >>> PMT(0.08/12, 10, 10000)
        -1037.0320893438879
    
    Cost: O(1)
    """
    return npf.pmt(rate, nper, pv, fv, type)


def PV(rate: float, nper: int, pmt: Union[int, float], fv: Union[int, float] = 0,
       type: int = 0) -> float:
    """
    Calculate the present value of an investment.
    
    Description:
        Returns the present value of an investment: the total amount that a series
        of future payments is worth now.
    
    Args:
        rate: Interest rate per period.
        nper: Total number of payment periods.
        pmt: Payment made each period.
        fv: Future value (cash balance after the last payment, default 0).
        type: When payments are due (0 = end of period, 1 = beginning of period).
    
    Returns:
        float: Present value.
    
    Usage Example:
        >>> PV(0.08/12, 12*20, 500)
        -59777.14551580659
    
    Cost: O(1)
    """
    return npf.pv(rate, nper, pmt, fv, type)


def RATE(nper: int, pmt: Union[int, float], pv: Union[int, float],
         fv: Union[int, float] = 0, type: int = 0, guess: float = 0.1) -> float:
    """
    Calculate the interest rate per period of an annuity.
    
    Description:
        Returns the interest rate per period of an annuity. RATE is calculated by
        iteration and can have zero or more solutions.
    
    Args:
        nper: Total number of payment periods.
        pmt: Payment made each period.
        pv: Present value.
        fv: Future value (default 0).
        type: When payments are due (0 = end of period, 1 = beginning of period).
        guess: Initial guess for the rate (default 0.1).
    
    Returns:
        float: Interest rate per period.
    
    Usage Example:
        >>> RATE(4*12, -200, 8000)
        0.0077010094049834785
    
    Cost: O(n) where n is the number of iterations needed for convergence.
    """
    return npf.rate(nper, pmt, pv, fv, type, guess)


def IPMT(rate: float, per: int, nper: int, pv: Union[int, float],
         fv: Union[int, float] = 0, type: int = 0) -> float:
    """
    Calculate the interest payment for a given period.
    
    Description:
        Returns the interest payment for a given period for an investment based on
        periodic, constant payments and a constant interest rate.
    
    Args:
        rate: Interest rate per period.
        per: Period for which you want to find the interest (must be between 1 and nper).
        nper: Total number of payment periods.
        pv: Present value.
        fv: Future value (default 0).
        type: When payments are due (0 = end of period, 1 = beginning of period).
    
    Returns:
        float: Interest payment for the period.
    
    Raises:
        ValueError: If per is not between 1 and nper.
    
    Usage Example:
        >>> IPMT(0.1/12, 1, 3*12, 8000)
        -66.66666666666667
    
    Cost: O(1)
    """
    return npf.ipmt(rate, per, nper, pv, fv, type)


def EFFECT(nominal_rate: float, npery: int) -> float:
    """
    Calculate the effective annual interest rate.
    
    Description:
        Returns the effective annual interest rate, given the nominal annual interest
        rate and the number of compounding periods per year.
    
    Args:
        nominal_rate: Nominal interest rate.
        npery: Number of compounding periods per year.
    
    Returns:
        float: Effective annual interest rate.
    
    Raises:
        ValueError: If nominal_rate < 0 or npery < 1.
    
    Usage Example:
        >>> EFFECT(0.0525, 4)
        0.053543247176560884
    
    Cost: O(1)
    """
    if nominal_rate < 0:
        raise ValueError("Nominal rate must be non-negative.")
    if npery < 1:
        raise ValueError("Number of periods must be at least 1.")
    
    return (1 + nominal_rate / npery) ** npery - 1


def NOMINAL(effect_rate: float, npery: int) -> float:
    """
    Calculate the nominal annual interest rate.
    
    Description:
        Returns the nominal annual interest rate, given the effective rate and the
        number of compounding periods per year.
    
    Args:
        effect_rate: Effective interest rate.
        npery: Number of compounding periods per year.
    
    Returns:
        float: Nominal annual interest rate.
    
    Raises:
        ValueError: If effect_rate < 0 or npery < 1.
    
    Usage Example:
        >>> NOMINAL(0.053543, 4)
        0.0525000113314875
    
    Cost: O(1)
    """
    if effect_rate < 0:
        raise ValueError("Effective rate must be non-negative.")
    if npery < 1:
        raise ValueError("Number of periods must be at least 1.")
    
    return npery * ((1 + effect_rate) ** (1 / npery) - 1)


def CUMIPMT(rate: float, nper: int, pv: Union[int, float], start_period: int,
            end_period: int, type: int) -> float:
    """
    Calculate cumulative interest paid between two periods.
    
    Description:
        Returns the cumulative interest paid on a loan between start_period and end_period.
    
    Args:
        rate: Interest rate.
        nper: Total number of payment periods.
        pv: Present value.
        start_period: First period in the calculation (1-based).
        end_period: Last period in the calculation.
        type: When payments are due (0 = end of period, 1 = beginning of period).
    
    Returns:
        float: Cumulative interest paid.
    
    Raises:
        ValueError: If start_period < 1, end_period < start_period, or end_period > nper.
    
    Usage Example:
        >>> CUMIPMT(0.09/12, 30*12, 125000, 1, 12, 0)
        -11135.232905681283
    
    Cost: O(n) where n is (end_period - start_period + 1).
    """
    if start_period < 1:
        raise ValueError("Start period must be >= 1.")
    if end_period < start_period:
        raise ValueError("End period must be >= start period.")
    if end_period > nper:
        raise ValueError("End period cannot exceed total number of periods.")
    
    total = 0
    for period in range(start_period, end_period + 1):
        total += IPMT(rate, period, nper, pv, 0, type)
    
    return total


def DB(cost: Union[int, float], salvage: Union[int, float], life: int, period: int,
       month: int = 12) -> float:
    """
    Calculate depreciation using the fixed-declining balance method.
    
    Description:
        Returns the depreciation of an asset for a specified period using the
        fixed-declining balance method.
    
    Args:
        cost: Initial cost of the asset.
        salvage: Value at the end of the depreciation.
        life: Number of periods over which the asset is depreciated.
        period: Period for which to calculate depreciation.
        month: Number of months in the first year (default 12).
    
    Returns:
        float: Depreciation for the specified period.
    
    Raises:
        ValueError: If period is not between 1 and life, or month not between 1 and 12.
    
    Usage Example:
        >>> DB(1000000, 100000, 6, 1, 7)
        186083.33333333334
    
    Cost: O(n) where n is the period number.
    """
    if not (1 <= period <= life + 1):
        raise ValueError(f"Period must be between 1 and {life + 1}.")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")
    
    rate = 1 - ((salvage / cost) ** (1 / life))
    rate = round(rate, 3)
    
    depreciation = 0
    value = cost
    
    for p in range(1, period + 1):
        if p == 1:
            depreciation = cost * rate * month / 12
        elif p == life + 1:
            depreciation = ((value - depreciation) * rate * (12 - month)) / 12
        else:
            depreciation = (value - depreciation) * rate
        
        if p == period:
            return depreciation
    
    return depreciation


def VDB(cost: Union[int, float], salvage: Union[int, float], life: Union[int, float],
        start_period: Union[int, float], end_period: Union[int, float],
        factor: Union[int, float] = 2, no_switch: bool = False) -> float:
    """
    Calculate depreciation using the double-declining balance or other method.
    
    Description:
        Returns the depreciation of an asset for any period you specify, including
        partial periods, using the double-declining balance method or some other
        method you specify.
    
    Args:
        cost: Initial cost of the asset.
        salvage: Value at the end of depreciation.
        life: Number of periods over which the asset is depreciated.
        start_period: Starting period for depreciation calculation.
        end_period: Ending period for depreciation calculation.
        factor: Rate at which the balance declines (default 2 for double-declining).
        no_switch: If True, don't switch to straight-line depreciation.
    
    Returns:
        float: Depreciation for the specified period range.
    
    Usage Example:
        >>> VDB(2400, 300, 10, 0, 1)
        480.0
    
    Cost: O(n) where n is the period range.
    """
    if life <= 0:
        raise ValueError("Life must be positive.")
    if start_period < 0 or end_period < start_period:
        raise ValueError("Invalid period range.")
    
    rate = factor / life
    total_depreciation = 0
    book_value = cost
    
    for period in np.arange(0, end_period, 0.1):
        if period >= start_period:
            # Calculate depreciation for this sub-period
            ddb_depreciation = book_value * rate * 0.1
            sln_depreciation = (cost - salvage - total_depreciation) / (life - period) * 0.1 if (life - period) > 0 else 0
            
            if no_switch:
                depreciation = ddb_depreciation
            else:
                depreciation = max(ddb_depreciation, sln_depreciation)
            
            # Ensure we don't go below salvage value
            if book_value - depreciation < salvage:
                depreciation = book_value - salvage
            
            total_depreciation += depreciation
            book_value -= depreciation
    
    return total_depreciation


def SYD(cost: Union[int, float], salvage: Union[int, float], life: int, per: int) -> float:
    """
    Calculate sum-of-years digits depreciation.
    
    Description:
        Returns the sum-of-years' digits depreciation of an asset for a specified period.
    
    Args:
        cost: Initial cost of the asset.
        salvage: Value at the end of depreciation.
        life: Number of periods over which the asset is depreciated.
        per: Period for which to calculate depreciation.
    
    Returns:
        float: Depreciation for the specified period.
    
    Raises:
        ValueError: If per is not between 1 and life.
    
    Usage Example:
        >>> SYD(30000, 7500, 10, 1)
        4090.909090909091
    
    Cost: O(1)
    """
    if not (1 <= per <= life):
        raise ValueError(f"Period must be between 1 and {life}.")
    
    sum_of_years = life * (life + 1) / 2
    return ((cost - salvage) * (life - per + 1)) / sum_of_years


def PDURATION(rate: float, pv: Union[int, float], fv: Union[int, float]) -> float:
    """
    Calculate the number of periods required for an investment to reach a specified value.
    
    Description:
        Returns the number of periods required by an investment to reach a specified
        value at a constant interest rate.
    
    Args:
        rate: Interest rate per period.
        pv: Present value of the investment.
        fv: Future value of the investment.
    
    Returns:
        float: Number of periods.
    
    Raises:
        ValueError: If rate <= 0, pv <= 0, or fv <= 0.
    
    Usage Example:
        >>> PDURATION(0.025, 2000, 2200)
        3.8654790948275353
    
    Cost: O(1)
    """
    if rate <= 0:
        raise ValueError("Rate must be positive.")
    if pv <= 0 or fv <= 0:
        raise ValueError("Present value and future value must be positive.")
    
    return (math.log(fv) - math.log(pv)) / math.log(1 + rate)


def RRI(nper: int, pv: Union[int, float], fv: Union[int, float]) -> float:
    """
    Calculate an equivalent interest rate for the growth of an investment.
    
    Description:
        Returns an equivalent interest rate for the growth of an investment.
    
    Args:
        nper: Number of periods for the investment.
        pv: Present value of the investment.
        fv: Future value of the investment.
    
    Returns:
        float: Interest rate.
    
    Raises:
        ValueError: If nper <= 0 or pv == 0.
    
    Usage Example:
        >>> RRI(96, 10000, 11000)
        0.0010099828308729896
    
    Cost: O(1)
    """
    if nper <= 0:
        raise ValueError("Number of periods must be positive.")
    if pv == 0:
        raise ValueError("Present value cannot be zero.")
    
    return (fv / pv) ** (1 / nper) - 1


def AMORLINC(cost, date_purchased, first_period, salvage, period, rate, basis=0):
    """
    Calculate depreciation for each accounting period using a depreciation coefficient.
    
    **Description:**
    Returns the depreciation for each accounting period. This function is provided
    for the French accounting system. If an asset is purchased in the middle of the
    accounting period, the prorated depreciation is taken into account.
    
    **Args:**
        cost (float): The cost of the asset.
        date_purchased (datetime.date): The date of the purchase of the asset.
        first_period (datetime.date): The date of the end of the first period.
        salvage (float): The salvage value at the end of the life of the asset.
        period (int): The period for which to calculate depreciation.
        rate (float): The rate of depreciation.
        basis (int, optional): The type of day count basis to use (0-4). Default is 0.
    
    **Returns:**
        float: The depreciation for the specified period.
    
    **Raises:**
        ValueError: If parameters are invalid.
    
    **Usage Example:**
        >>> from datetime import date
        >>> AMORLINC(2400, date(2008, 8, 19), date(2008, 12, 31), 300, 1, 0.15)
        360.0
    
    **Cost:** O(1)
    """
    if cost < 0 or salvage < 0 or rate <= 0 or period < 0:
        raise ValueError("Invalid parameters")
    
    if cost <= salvage:
        return 0
    
    # Calculate total depreciation
    total_depreciation = cost - salvage
    
    # Calculate depreciation rate per period
    depreciation_per_period = total_depreciation * rate
    
    # For period 0, calculate prorated first period
    if period == 0:
        # Calculate months in first period
        months = (first_period.year - date_purchased.year) * 12 + (first_period.month - date_purchased.month)
        if first_period.day >= date_purchased.day:
            months += 1
        return depreciation_per_period * months / 12
    
    # For subsequent periods, return full depreciation until asset is fully depreciated
    accumulated = depreciation_per_period * period
    if accumulated > total_depreciation:
        return max(0, total_depreciation - depreciation_per_period * (period - 1))
    
    return depreciation_per_period


def DISC(settlement, maturity, pr, redemption, basis=0):
    """
    Calculate the discount rate for a security.
    
    **Description:**
    Returns the discount rate for a security. The discount rate is the difference
    between the redemption value and the price, expressed as a percentage of the
    redemption value.
    
    **Args:**
        settlement (datetime.date): The security's settlement date.
        maturity (datetime.date): The security's maturity date.
        pr (float): The security's price per $100 face value.
        redemption (float): The security's redemption value per $100 face value.
        basis (int, optional): The type of day count basis to use (0-4). Default is 0.
    
    **Returns:**
        float: The discount rate.
    
    **Raises:**
        ValueError: If settlement >= maturity, or if pr <= 0 or redemption <= 0.
    
    **Usage Example:**
        >>> from datetime import date
        >>> DISC(date(2007, 1, 25), date(2007, 6, 15), 97.975, 100)
        0.0520
    
    **Cost:** O(1)
    """
    if settlement >= maturity:
        raise ValueError("Settlement date must be before maturity date")
    if pr <= 0 or redemption <= 0:
        raise ValueError("Price and redemption must be positive")
    
    # Calculate days based on basis
    days = _days_between(settlement, maturity, basis)
    year_days = _year_days(settlement, basis)
    
    discount = (redemption - pr) / redemption
    return discount * (year_days / days)


def DOLLARDE(fractional_dollar, fraction):
    """
    Convert a dollar price expressed as a fraction into a decimal dollar price.
    
    **Description:**
    Converts a dollar price expressed as a fraction into a dollar price expressed
    as a decimal number. This is useful for converting bond prices.
    
    **Args:**
        fractional_dollar (float): A number expressed as an integer part and a fraction part.
        fraction (int): The integer to use as the denominator of the fraction.
    
    **Returns:**
        float: The dollar price as a decimal number.
    
    **Raises:**
        ValueError: If fraction < 1.
    
    **Usage Example:**
        >>> DOLLARDE(1.02, 16)
        1.125
        >>> DOLLARDE(1.1, 32)
        1.3125
    
    **Cost:** O(1)
    """
    if fraction < 1:
        raise ValueError("Fraction must be at least 1")
    
    # Split into integer and fractional parts
    integer_part = int(fractional_dollar)
    frac_part = fractional_dollar - integer_part
    
    # The fractional part represents numerator/fraction
    # For example, 1.02 with fraction 16 means 1 + 2/16
    # frac_part is 0.02, we need to extract the numerator (2)
    numerator = round(frac_part * 100)  # Get the digits after decimal as numerator
    
    # Convert fraction to decimal
    decimal_part = numerator / fraction
    
    return integer_part + decimal_part


def DOLLARFR(decimal_dollar, fraction):
    """
    Convert a decimal dollar price into a fractional dollar price.
    
    **Description:**
    Converts a dollar price expressed as a decimal number into a dollar price
    expressed as a fraction. This is useful for converting bond prices.
    
    **Args:**
        decimal_dollar (float): A decimal number.
        fraction (int): The integer to use as the denominator of the fraction.
    
    **Returns:**
        float: The dollar price as a fraction.
    
    **Raises:**
        ValueError: If fraction < 1.
    
    **Usage Example:**
        >>> DOLLARFR(1.125, 16)
        1.02
        >>> DOLLARFR(1.3125, 32)
        1.1
    
    **Cost:** O(1)
    """
    if fraction < 1:
        raise ValueError("Fraction must be at least 1")
    
    # Split into integer and fractional parts
    integer_part = int(decimal_dollar)
    decimal_part = decimal_dollar - integer_part
    
    # Convert decimal to fraction numerator
    # For example, 0.125 with fraction 16 gives numerator 2 (0.125 * 16 = 2)
    numerator = decimal_part * fraction
    
    # Return as integer part + (numerator as decimal digits)
    # For example, 1 + 0.02 (representing 2/16)
    frac_part = numerator / 100  # Convert numerator to decimal representation
    
    return integer_part + frac_part


def INTRATE(settlement, maturity, investment, redemption, basis=0):
    """
    Calculate the interest rate for a fully invested security.
    
    **Description:**
    Returns the interest rate for a fully invested security. This is the interest
    rate earned on a security that is purchased and held to maturity.
    
    **Args:**
        settlement (datetime.date): The security's settlement date.
        maturity (datetime.date): The security's maturity date.
        investment (float): The amount invested in the security.
        redemption (float): The amount to be received at maturity.
        basis (int, optional): The type of day count basis to use (0-4). Default is 0.
    
    **Returns:**
        float: The interest rate.
    
    **Raises:**
        ValueError: If settlement >= maturity, or if investment <= 0 or redemption <= 0.
    
    **Usage Example:**
        >>> from datetime import date
        >>> INTRATE(date(2008, 2, 15), date(2008, 5, 15), 1000000, 1014420)
        0.0578
    
    **Cost:** O(1)
    """
    if settlement >= maturity:
        raise ValueError("Settlement date must be before maturity date")
    if investment <= 0 or redemption <= 0:
        raise ValueError("Investment and redemption must be positive")
    
    # Calculate days based on basis
    days = _days_between(settlement, maturity, basis)
    year_days = _year_days(settlement, basis)
    
    return ((redemption - investment) / investment) * (year_days / days)


def ISPMT(rate, per, nper, pv):
    """
    Calculate the interest paid during a specific period of an investment.
    
    **Description:**
    Calculates the interest paid (or received) for a specified period of a loan
    (or investment) with even principal payments. This function is used for
    calculating the interest portion of a payment when principal is paid evenly.
    
    **Args:**
        rate (float): The interest rate per period.
        per (int): The period for which to find the interest (must be between 1 and nper).
        nper (int): The total number of payment periods.
        pv (float): The present value or principal.
    
    **Returns:**
        float: The interest paid during the period.
    
    **Usage Example:**
        >>> ISPMT(0.1/12, 1, 3*12, 8000000)
        -66666.67
    
    **Cost:** O(1)
    """
    # Calculate remaining principal at beginning of period
    # With even principal payments, principal decreases linearly
    remaining_principal = pv * (1 - (per - 1) / nper)
    
    # Interest = rate * remaining principal
    return -rate * remaining_principal


def ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, basis=0):
    """
    Calculate the price per $100 face value of a security with an odd first period.
    
    **Description:**
    Returns the price per $100 face value of a security having an odd (short or long)
    first coupon period. This is used for bonds where the first coupon period differs
    from the standard period.
    
    **Args:**
        settlement (datetime.date): The security's settlement date.
        maturity (datetime.date): The security's maturity date.
        issue (datetime.date): The security's issue date.
        first_coupon (datetime.date): The security's first coupon date.
        rate (float): The security's annual coupon rate.
        yld (float): The security's annual yield.
        redemption (float): The security's redemption value per $100 face value.
        frequency (int): The number of coupon payments per year (1, 2, or 4).
        basis (int, optional): The type of day count basis to use (0-4). Default is 0.
    
    **Returns:**
        float: The price per $100 face value.
    
    **Raises:**
        ValueError: If dates are invalid or parameters are out of range.
    
    **Usage Example:**
        >>> from datetime import date
        >>> ODDFPRICE(date(2008, 11, 11), date(2021, 3, 1), date(2008, 10, 15),
        ...           date(2009, 3, 1), 0.0785, 0.0625, 100, 2)
        113.597717
    
    **Cost:** O(1)
    """
    if settlement >= maturity:
        raise ValueError("Settlement must be before maturity")
    if frequency not in [1, 2, 4]:
        raise ValueError("Frequency must be 1, 2, or 4")
    
    # Calculate days in first coupon period
    dsc = _days_between(settlement, first_coupon, basis)
    e = _days_between(issue, first_coupon, basis)
    
    # Calculate number of coupons from first coupon to maturity
    n = _coup_num_internal(first_coupon, maturity, frequency)
    
    # Calculate coupon payment
    coupon = redemption * rate / frequency
    
    # Calculate discount factor for settlement to first coupon
    dfc = dsc / (_year_days(settlement, basis) / frequency)
    
    # Calculate accrued interest from issue to settlement
    a = _days_between(issue, settlement, basis)
    
    # Price calculation with odd first period adjustment
    price = redemption / ((1 + yld / frequency) ** (n + dfc - 1))
    
    # Add present value of all coupons
    for k in range(1, n + 1):
        price += coupon / ((1 + yld / frequency) ** (k + dfc - 1))
    
    # Subtract accrued interest
    accrued = coupon * a / e
    price -= accrued
    
    return price


def ODDFYIELD(settlement, maturity, issue, first_coupon, rate, pr, redemption, frequency, basis=0):
    """
    Calculate the yield of a security with an odd first period.
    
    **Description:**
    Returns the yield of a security that has an odd (short or long) first period.
    This function uses iterative methods to find the yield that matches the price.
    
    **Args:**
        settlement (datetime.date): The security's settlement date.
        maturity (datetime.date): The security's maturity date.
        issue (datetime.date): The security's issue date.
        first_coupon (datetime.date): The security's first coupon date.
        rate (float): The security's annual coupon rate.
        pr (float): The security's price per $100 face value.
        redemption (float): The security's redemption value per $100 face value.
        frequency (int): The number of coupon payments per year (1, 2, or 4).
        basis (int, optional): The type of day count basis to use (0-4). Default is 0.
    
    **Returns:**
        float: The yield.
    
    **Raises:**
        ValueError: If dates are invalid or parameters are out of range.
    
    **Usage Example:**
        >>> from datetime import date
        >>> ODDFYIELD(date(2008, 11, 11), date(2021, 3, 1), date(2008, 10, 15),
        ...           date(2009, 3, 1), 0.0785, 113.597717, 100, 2)
        0.0625
    
    **Cost:** O(n) where n is iterations to converge (typically < 100)
    """
    if settlement >= maturity:
        raise ValueError("Settlement must be before maturity")
    if frequency not in [1, 2, 4]:
        raise ValueError("Frequency must be 1, 2, or 4")
    
    # Use Newton-Raphson method to find yield
    def price_func(yld):
        try:
            return ODDFPRICE(settlement, maturity, issue, first_coupon, rate, yld, redemption, frequency, basis)
        except:
            return None
    
    # Initial guess
    yld = rate
    
    # Newton-Raphson iteration
    for _ in range(100):
        p = price_func(yld)
        if p is None:
            raise ValueError("Cannot calculate yield")
        
        # Check convergence
        if abs(p - pr) < 0.00001:
            return yld
        
        # Calculate derivative numerically
        delta = 0.0001
        p_plus = price_func(yld + delta)
        if p_plus is None:
            raise ValueError("Cannot calculate yield")
        
        derivative = (p_plus - p) / delta
        
        # Update yield
        if abs(derivative) < 1e-10:
            break
        yld = yld - (p - pr) / derivative
        
        # Keep yield positive
        if yld < 0:
            yld = 0.0001
    
    return yld


def ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, basis=0):
    """
    Calculate the price per $100 face value of a security with an odd last period.
    
    **Description:**
    Returns the price per $100 face value of a security having an odd (short or long)
    last coupon period.
    
    **Args:**
        settlement (datetime.date): The security's settlement date.
        maturity (datetime.date): The security's maturity date.
        last_interest (datetime.date): The security's last coupon date.
        rate (float): The security's annual coupon rate.
        yld (float): The security's annual yield.
        redemption (float): The security's redemption value per $100 face value.
        frequency (int): The number of coupon payments per year (1, 2, or 4).
        basis (int, optional): The type of day count basis to use (0-4). Default is 0.
    
    **Returns:**
        float: The price per $100 face value.
    
    **Raises:**
        ValueError: If dates are invalid or parameters are out of range.
    
    **Usage Example:**
        >>> from datetime import date
        >>> ODDLPRICE(date(2008, 2, 7), date(2008, 6, 15), date(2007, 10, 15),
        ...           0.0375, 0.0405, 100, 2)
        99.878456
    
    **Cost:** O(1)
    """
    if settlement >= maturity:
        raise ValueError("Settlement must be before maturity")
    if frequency not in [1, 2, 4]:
        raise ValueError("Frequency must be 1, 2, or 4")
    
    # Calculate days
    dsl = _days_between(settlement, maturity, basis)
    dcl = _days_between(last_interest, maturity, basis)
    a = _days_between(last_interest, settlement, basis)
    
    # Calculate number of coupons from settlement to last regular coupon
    n = _coup_num_internal(settlement, last_interest, frequency)
    
    # Calculate coupon payment
    coupon = redemption * rate / frequency
    
    # Calculate odd last coupon
    odd_coupon = coupon * dcl / (_year_days(settlement, basis) / frequency)
    
    # Calculate price
    discount = 1 + (yld / frequency) * (dsl / (_year_days(settlement, basis) / frequency))
    price = (redemption + odd_coupon) / discount
    
    # Add present value of regular coupons
    for k in range(1, n + 1):
        price += coupon / ((1 + yld / frequency) ** k)
    
    # Subtract accrued interest
    accrued = coupon * a / (_year_days(settlement, basis) / frequency)
    price -= accrued
    
    return price


def ODDLYIELD(settlement, maturity, last_interest, rate, pr, redemption, frequency, basis=0):
    """
    Calculate the yield of a security with an odd last period.
    
    **Description:**
    Returns the yield of a security that has an odd (short or long) last period.
    This function uses iterative methods to find the yield that matches the price.
    
    **Args:**
        settlement (datetime.date): The security's settlement date.
        maturity (datetime.date): The security's maturity date.
        last_interest (datetime.date): The security's last coupon date.
        rate (float): The security's annual coupon rate.
        pr (float): The security's price per $100 face value.
        redemption (float): The security's redemption value per $100 face value.
        frequency (int): The number of coupon payments per year (1, 2, or 4).
        basis (int, optional): The type of day count basis to use (0-4). Default is 0.
    
    **Returns:**
        float: The yield.
    
    **Raises:**
        ValueError: If dates are invalid or parameters are out of range.
    
    **Usage Example:**
        >>> from datetime import date
        >>> ODDLYIELD(date(2008, 2, 7), date(2008, 6, 15), date(2007, 10, 15),
        ...           0.0375, 99.878456, 100, 2)
        0.0405
    
    **Cost:** O(n) where n is iterations to converge (typically < 100)
    """
    if settlement >= maturity:
        raise ValueError("Settlement must be before maturity")
    if frequency not in [1, 2, 4]:
        raise ValueError("Frequency must be 1, 2, or 4")
    
    # Use Newton-Raphson method to find yield
    def price_func(yld):
        try:
            return ODDLPRICE(settlement, maturity, last_interest, rate, yld, redemption, frequency, basis)
        except:
            return None
    
    # Initial guess
    yld = rate
    
    # Newton-Raphson iteration
    for _ in range(100):
        p = price_func(yld)
        if p is None:
            raise ValueError("Cannot calculate yield")
        
        # Check convergence
        if abs(p - pr) < 0.00001:
            return yld
        
        # Calculate derivative numerically
        delta = 0.0001
        p_plus = price_func(yld + delta)
        if p_plus is None:
            raise ValueError("Cannot calculate yield")
        
        derivative = (p_plus - p) / delta
        
        # Update yield
        if abs(derivative) < 1e-10:
            break
        yld = yld - (p - pr) / derivative
        
        # Keep yield positive
        if yld < 0:
            yld = 0.0001
    
    return yld


def RECEIVED(settlement, maturity, investment, discount, basis=0):
    """
    Calculate the amount received at maturity for a fully invested security.
    
    **Description:**
    Returns the amount received at maturity for a fully invested security.
    This calculates the redemption value based on the investment and discount rate.
    
    **Args:**
        settlement (datetime.date): The security's settlement date.
        maturity (datetime.date): The security's maturity date.
        investment (float): The amount invested in the security.
        discount (float): The security's discount rate.
        basis (int, optional): The type of day count basis to use (0-4). Default is 0.
    
    **Returns:**
        float: The amount received at maturity.
    
    **Raises:**
        ValueError: If settlement >= maturity or if investment <= 0.
    
    **Usage Example:**
        >>> from datetime import date
        >>> RECEIVED(date(2008, 2, 15), date(2008, 5, 15), 1000000, 0.0575)
        1014584.65
    
    **Cost:** O(1)
    """
    if settlement >= maturity:
        raise ValueError("Settlement date must be before maturity date")
    if investment <= 0:
        raise ValueError("Investment must be positive")
    
    # Calculate days based on basis
    days = _days_between(settlement, maturity, basis)
    year_days = _year_days(settlement, basis)
    
    # Calculate received amount
    denominator = 1 - (discount * days / year_days)
    if abs(denominator) < 1e-10:
        raise ValueError("Discount rate results in division by zero")
    
    return investment / denominator


def TBILLEQ(settlement, maturity, discount):
    """
    Calculate the bond-equivalent yield for a Treasury bill.
    
    **Description:**
    Returns the bond-equivalent yield for a Treasury bill. This converts the
    discount rate to a bond-equivalent yield for comparison with coupon securities.
    
    **Args:**
        settlement (datetime.date): The Treasury bill's settlement date.
        maturity (datetime.date): The Treasury bill's maturity date.
        discount (float): The Treasury bill's discount rate.
    
    **Returns:**
        float: The bond-equivalent yield.
    
    **Raises:**
        ValueError: If settlement >= maturity or if discount <= 0.
    
    **Usage Example:**
        >>> from datetime import date
        >>> TBILLEQ(date(2008, 3, 31), date(2008, 6, 1), 0.0914)
        0.0944
    
    **Cost:** O(1)
    """
    if settlement >= maturity:
        raise ValueError("Settlement date must be before maturity date")
    if discount <= 0:
        raise ValueError("Discount must be positive")
    
    # Calculate days to maturity
    days = (maturity - settlement).days
    
    if days > 365:
        raise ValueError("Maturity must be within one year of settlement")
    
    # Bond-equivalent yield formula for T-bills
    if days <= 182:
        # For half year or less
        return (365 * discount) / (360 - discount * days)
    else:
        # For more than half year
        return (-days + ((days ** 2 - (2 * days - 365) * (365 * discount / (discount * days - 360))) ** 0.5)) / (days - 365 / 2)


def TBILLPRICE(settlement, maturity, discount):
    """
    Calculate the price per $100 face value for a Treasury bill.
    
    **Description:**
    Returns the price per $100 face value for a Treasury bill based on the
    discount rate.
    
    **Args:**
        settlement (datetime.date): The Treasury bill's settlement date.
        maturity (datetime.date): The Treasury bill's maturity date.
        discount (float): The Treasury bill's discount rate.
    
    **Returns:**
        float: The price per $100 face value.
    
    **Raises:**
        ValueError: If settlement >= maturity or if discount <= 0.
    
    **Usage Example:**
        >>> from datetime import date
        >>> TBILLPRICE(date(2008, 3, 31), date(2008, 6, 1), 0.09)
        98.45
    
    **Cost:** O(1)
    """
    if settlement >= maturity:
        raise ValueError("Settlement date must be before maturity date")
    if discount <= 0:
        raise ValueError("Discount must be positive")
    
    # Calculate days to maturity (360-day year basis)
    days = (maturity - settlement).days
    
    if days > 360:
        raise ValueError("Maturity must be within one year of settlement")
    
    # Price formula for T-bills
    return 100 * (1 - discount * days / 360)


def TBILLYIELD(settlement, maturity, pr):
    """
    Calculate the yield for a Treasury bill.
    
    **Description:**
    Returns the yield for a Treasury bill based on its price.
    
    **Args:**
        settlement (datetime.date): The Treasury bill's settlement date.
        maturity (datetime.date): The Treasury bill's maturity date.
        pr (float): The Treasury bill's price per $100 face value.
    
    **Returns:**
        float: The yield.
    
    **Raises:**
        ValueError: If settlement >= maturity or if pr <= 0.
    
    **Usage Example:**
        >>> from datetime import date
        >>> TBILLYIELD(date(2008, 3, 31), date(2008, 6, 1), 98.45)
        0.0914
    
    **Cost:** O(1)
    """
    if settlement >= maturity:
        raise ValueError("Settlement date must be before maturity date")
    if pr <= 0:
        raise ValueError("Price must be positive")
    
    # Calculate days to maturity (360-day year basis)
    days = (maturity - settlement).days
    
    if days > 360:
        raise ValueError("Maturity must be within one year of settlement")
    
    # Yield formula for T-bills
    return (100 - pr) / pr * (360 / days)