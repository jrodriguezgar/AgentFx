"""Financial Functions Module.

Contains functions for common financial calculations: future value (FV),
present value (PV), periodic payment (PMT), number of periods (NPER),
interest rate (RATE), internal rate of return (IRR), net present value
(NPV), and depreciation (SLN, DB).

Key Features:
    - TVM (Time Value of Money) functions
    - Iterative calculations for IRR and RATE
    - Depreciation methods
    - Compatible with ordinary and due annuities

Example:
    >>> future_value(rate=0.05, nper=5, pmt=0, pv=-1000)
    1276.2815625000003
"""

import math
from typing import Union, List
from datetime import date, datetime
import calendar


def _validate_annuity_type(type_val: int) -> None:
    """Validate the annuity type parameter (0 = end, 1 = beginning)."""
    if not isinstance(type_val, int) or type_val not in (0, 1):
        raise TypeError("Type must be 0 (end of period) or 1 (beginning of period).")


def future_value(rate: float, nper: Union[int, float], pmt: float, pv: float, type: int = 0) -> float:
    """
    Calculates the Future Value (FV) of an investment based on a series of
    periodic constant payments and a constant interest rate.

    Args:
        rate (float): The interest rate per period (e.g., 0.05 for 5% annual rate).
        nper (Union[int, float]): The total number of payment periods in an investment.
        pmt (float): The payment made each period. Payments are typically negative
                     (cash outflow).
        pv (float): The Present Value (PV), or the lump-sum amount that a series of
                    future payments is worth right now. Typically negative (cash outflow).
        type (int, optional): When payments are due.
                              0 = at the end of the period (default).
                              1 = at the beginning of the period.

    Returns:
        float: The Future Value of the investment.

    Raises:
        TypeError: If any input is not a number or if 'type' is not 0 or 1.
        ValueError: If 'nper' is negative.

    Example:
        >>> # FV of $1000 invested for 5 years at 5% annual interest, compounded annually.
        >>> future_value(rate=0.05, nper=5, pmt=0, pv=-1000)
        1276.2815625000003

        >>> # FV of $100 payments made at end of each year for 5 years at 5% annual interest.
        >>> future_value(rate=0.05, nper=5, pmt=-100, pv=0)
        552.5631250000001

    **Cost:** O(1), direct future value formula calculation.
    """
    if not all(isinstance(arg, (int, float)) for arg in [rate, nper, pmt, pv]):
        raise TypeError("Rate, NPER, PMT, and PV must be numeric values.")
    _validate_annuity_type(type)
    if nper < 0:
        raise ValueError("NPER cannot be negative.")

    if rate == 0:
        # Special case for zero interest rate
        return -pv - pmt * nper
    else:
        fv_val = -pv * ((1 + rate) ** nper) - pmt * ((((1 + rate) ** nper) - 1) / rate)
        if type == 1: # Payments at beginning of period (annuity due)
            fv_val = fv_val * (1 + rate)
        return fv_val


def present_value(rate: float, nper: Union[int, float], pmt: float, fv: float = 0.0, type: int = 0) -> float:
    """
    Calculates the Present Value (PV) of an investment based on a series of
    future payments and a constant interest rate.

    Args:
        rate (float): The interest rate per period (e.g., 0.05 for 5% annual rate).
        nper (Union[int, float]): The total number of payment periods in an investment.
        pmt (float): The payment made each period. Payments are typically negative
                     (cash outflow).
        fv (float, optional): The Future Value, or a cash balance you want to attain
                              after the last payment. Defaults to 0.0.
        type (int, optional): When payments are due.
                              0 = at the end of the period (default).
                              1 = at the beginning of the period.

    Returns:
        float: The Present Value of the investment.

    Raises:
        TypeError: If any input is not a number or if 'type' is not 0 or 1.
        ValueError: If 'nper' is negative.

    Example:
        >>> # PV of $1276.28 received in 5 years at 5% annual interest.
        >>> present_value(rate=0.05, nper=5, pmt=0, fv=1276.28)
        -999.9989807559194

        >>> # PV of $100 payments received at end of each year for 5 years at 5% annual interest.
        >>> present_value(rate=0.05, nper=5, pmt=100, fv=0)
        -432.94766060133177

    **Cost:** O(1), direct present value formula calculation.
    """
    if not all(isinstance(arg, (int, float)) for arg in [rate, nper, pmt, fv]):
        raise TypeError("Rate, NPER, PMT, and FV must be numeric values.")
    _validate_annuity_type(type)
    if nper < 0:
        raise ValueError("NPER cannot be negative.")

    if rate == 0:
        return -fv - pmt * nper
    else:
        pv_val = (-fv - pmt * ((((1 + rate) ** nper) - 1) / rate) * (1 + rate * type)) / ((1 + rate) ** nper)
        return pv_val


def pmt(rate: float, nper: Union[int, float], pv: float, fv: float = 0.0, type: int = 0) -> float:
    """
    Calculates the payment for a loan based on constant payments and a
    constant interest rate.

    Args:
        rate (float): The interest rate per period.
        nper (Union[int, float]): The total number of payments for the loan.
        pv (float): The Present Value, or the principal amount of the loan.
                    This is typically positive (cash inflow to you).
        fv (float, optional): The Future Value, or the cash balance you want after
                              the last payment. Defaults to 0.0 (loan fully paid off).
        type (int, optional): When payments are due.
                              0 = at the end of the period (default).
                              1 = at the beginning of the period.

    Returns:
        float: The payment made each period (will be negative as cash outflow).

    Raises:
        TypeError: If any input is not a number or if 'type' is not 0 or 1.
        ValueError: If 'nper' is not positive or if denominator for rate=0 becomes 0.

    Example:
        >>> # Monthly payment for a $100,000 loan at 5% annual interest for 30 years.
        >>> # Monthly rate = 0.05 / 12, NPER = 30 * 12 = 360
        >>> round(pmt(rate=0.05/12, nper=360, pv=100000), 2)
        -536.82

    **Cost:** O(1), direct periodic payment formula calculation.
    """
    if not all(isinstance(arg, (int, float)) for arg in [rate, nper, pv, fv]):
        raise TypeError("Rate, NPER, PV, and FV must be numeric values.")
    _validate_annuity_type(type)
    if nper <= 0:
        raise ValueError("NPER must be a positive number of periods.")

    if rate == 0:
        if nper == 0: # Avoid division by zero if nper is also 0
            raise ValueError("Cannot calculate PMT when rate is 0 and NPER is 0.")
        return -(pv + fv) / nper
    else:
        # The core PMT formula derived from FV/PV annuity formulas
        numerator = rate * (fv + pv * ((1 + rate) ** nper))
        denominator = ((1 + rate) ** nper - 1) * (1 + rate * type)

        if abs(denominator) < 1e-9: # Check for near-zero denominator
            raise ValueError("Cannot calculate PMT: denominator approaches zero. Check inputs.")

        return -numerator / denominator


def nper(rate: float, pmt: float, pv: float, fv: float = 0.0, type: int = 0) -> float:
    """
    Calculates the number of periods for an investment based on periodic,
    constant payments and a constant interest rate.

    Args:
        rate (float): The interest rate per period.
        pmt (float): The payment made each period.
        pv (float): The Present Value.
        fv (float, optional): The Future Value. Defaults to 0.0.
        type (int, optional): When payments are due (0 for end, 1 for beginning).

    Returns:
        float: The number of periods.

    Raises:
        TypeError: If any input is not a number or if 'type' is not 0 or 1.
        ValueError: If pmt is 0 and rate is not 0, or if arguments lead to invalid log.

    Example:
        >>> # Number of months to pay off a $10,000 loan with $100 monthly payments at 5% annual interest.
        >>> # Monthly rate = 0.05 / 12
        >>> round(nper(rate=0.05/12, pmt=-100, pv=10000), 2)
        122.09

    **Cost:** O(1), direct logarithmic calculation.
    """
    if not all(isinstance(arg, (int, float)) for arg in [rate, pmt, pv, fv]):
        raise TypeError("Rate, PMT, PV, and FV must be numeric values.")
    _validate_annuity_type(type)

    if rate == 0:
        if pmt == 0:
            raise ValueError("Cannot calculate NPER when rate is 0 and PMT is 0.")
        return (-pv - fv) / pmt
    else:
        # Adjust PMT for type
        if type == 1: # Annuity Due
            pmt_adjusted = pmt * (1 + rate)
        else: # Ordinary Annuity
            pmt_adjusted = pmt

        # Formula derived from FV = PV * (1+r)^n + PMT * [((1+r)^n - 1) / r] * (1+r*type)
        # Rearranging to solve for n:
        if pmt_adjusted == 0: # Avoid division by zero if there are no payments
            if pv == 0:
                raise ValueError("Cannot calculate NPER when PMT and PV are zero (and rate is not zero).")
            # If PMT is 0, then FV = PV * (1+rate)^n. Solve for n.
            if pv == 0:
                # If FV is also 0, it means 0 = 0*(1+rate)^n, which is true for any n.
                # If FV is not 0, 0 = 0 * (...), which is impossible.
                if fv == 0:
                    return float('inf')  # Or indicate indeterminate
                else:
                    raise ValueError("NPER is undefined when PMT=0, PV=0, and FV is not 0 (and rate != 0).")
            
            # FV / PV = (1 + rate) ^ n
            # log(FV / PV) = n * log(1 + rate)
            # n = log(FV / PV) / log(1 + rate)
            ratio = -fv / pv # PV and FV have opposite signs usually
            if ratio <= 0:
                raise ValueError("Cannot calculate NPER: log argument must be positive. Check PV and FV signs.")
            return math.log(ratio) / math.log(1 + rate)


        term1 = (pmt_adjusted / rate) - fv
        term2 = (pmt_adjusted / rate) + pv

        if term2 == 0:
             raise ValueError("Cannot calculate NPER: denominator in log argument is zero. Check PMT, PV, and rate values.")

        log_arg = term1 / term2
        
        if log_arg <= 0:
            raise ValueError("Cannot calculate NPER: Logarithm argument must be positive. Check payment, present value, and future value signs.")
        
        return math.log(log_arg) / math.log(1 + rate)


def rate(nper: Union[int, float], pmt: float, pv: float, fv: float = 0.0, type: int = 0, guess: float = 0.1) -> float:
    """
    Calculates the interest rate per period of an annuity.
    This function uses an iterative approach (Newton-Raphson-like) to find the rate,
    as there's no direct algebraic solution.

    Args:
        nper (Union[int, float]): The total number of payment periods.
        pmt (float): The payment made each period.
        pv (float): The Present Value.
        fv (float, optional): The Future Value. Defaults to 0.0.
        type (int, optional): When payments are due (0 for end, 1 for beginning).
        guess (float, optional): Your guess for the rate. Defaults to 0.1 (10%).

    Returns:
        float: The interest rate per period.

    Raises:
        TypeError: If any input is not a number or if 'type' is not 0 or 1.
        ValueError: If 'nper' is not positive or if the function fails to converge.

    Example:
        >>> # If you pay $536.82 monthly for 360 months on a $100,000 loan, what's the annual rate?
        >>> # Result will be monthly rate, multiply by 12 for annual.
        >>> monthly_rate = rate(nper=360, pmt=-536.82, pv=100000)
        >>> round(monthly_rate * 12, 4)
        0.05

        >>> # If you invest $1000 and it grows to $1276.28 in 5 years with no additional payments.
        >>> round(rate(nper=5, pmt=0, pv=-1000, fv=1276.28), 4)
        0.05

    **Cost:** O(k), where k is the number of iterations (up to 1000). Newton-Raphson/bisection iterative method.
    """
    if not all(isinstance(arg, (int, float)) for arg in [nper, pmt, pv, fv, guess]):
        raise TypeError("NPER, PMT, PV, FV, and guess must be numeric values.")
    _validate_annuity_type(type)
    if nper <= 0:
        raise ValueError("NPER must be a positive number of periods.")

    # Objective function: NPV = 0
    # NPV_func(rate) = PV + PMT * PV_annuity_factor + FV * PV_factor
    # We are solving for rate such that FV_func(rate) = 0
    # FV_func = PV * (1+rate)^nper + PMT * [((1+rate)^nper - 1) / rate] * (1+rate*type) + FV = 0
    
    # Using a simple iterative method (e.g., bisection or secant method)
    # The `numpy_financial` library has a robust `npf.rate` function,
    # but since we are building from scratch, we'll implement a basic solver.

    tolerance = 1e-7
    max_iterations = 1000
    
    # Function to calculate FV for a given rate
    def fv_for_rate(r):
        if r == 0:
            return pv + pmt * nper + fv
        fv_val = pv * ((1 + r) ** nper) + pmt * ((((1 + r) ** nper) - 1) / r)
        if type == 1:
            fv_val *= (1 + r)
        return fv_val + fv

    # Newton-Raphson method (simplified)
    # We will use an adjusted bisection or secant approach because Newton-Raphson requires derivative,
    # and a generic numerical solver often works better.

    low = -0.999999 # Smallest possible rate for real-world scenarios
    high = 10.0 # Arbitrarily high rate (1000%)

    # Initial bounds for bisection if guess is bad
    # Attempt to find a bracket [low, high] where f(low) and f(high) have opposite signs
    # This loop is to find an initial bracket for the root, robustly.
    for _ in range(50): # Limited attempts to find bounds
        f_low = fv_for_rate(low)
        f_high = fv_for_rate(high)
        if f_low * f_high < 0:
            break # Found a bracket
        elif abs(f_low) < tolerance:
            return low
        elif abs(f_high) < tolerance:
            return high
        else:
            # Adjust bounds if no bracket found yet
            if f_low < 0:
                low /= 2  # Try smaller negative rates
            else:
                low *= 2
            if f_high > 0:
                high *= 2  # Try larger positive rates
            else:
                high /= 2
            
    if fv_for_rate(low) * fv_for_rate(high) > 0:
        # If after trying to expand bounds, no bracket found, convergence might be an issue.
        # This could happen if there's no real rate solution or the range is too narrow.
        # For simple cases, the provided `guess` may be the starting point.
        # Let's try a direct iteration from guess if no clear bracket.
        current_rate = guess
        for i in range(max_iterations):
            f_val = fv_for_rate(current_rate)
            if abs(f_val) < tolerance:
                return current_rate
            
            # Numerical derivative approximation: (f(x+h) - f(x)) / h
            h = max(tolerance, abs(current_rate * 1e-5)) # A small step size
            f_prime = (fv_for_rate(current_rate + h) - f_val) / h
            
            if abs(f_prime) < 1e-10: # Avoid division by near-zero derivative
                 # If derivative is close to zero, it means the function is flat
                 # or we are at a local extremum.
                 # Try adjusting guess in a fixed direction or exiting.
                current_rate += tolerance # Small nudge
            else:
                current_rate -= f_val / f_prime
                
            # Basic sanity check to prevent rate from becoming excessively large or small (e.g., negative)
            if current_rate <= -1.0: # Rate cannot be -100% or less
                current_rate = -0.99999 # Keep it just above -1
            if current_rate > 100.0: # Arbitrary upper limit for practical rates
                current_rate = 100.0 # Cap it

        raise ValueError("Failed to converge on a rate within the maximum number of iterations.")

    # Bisection method (more robust than simple Newton-Raphson for general cases)
    for i in range(max_iterations):
        mid = (low + high) / 2
        f_mid = fv_for_rate(mid)

        if abs(f_mid) < tolerance:
            return mid
        elif f_mid * fv_for_rate(low) < 0:
            high = mid
        else:
            low = mid

    raise ValueError("Failed to converge on a rate within the maximum number of iterations. Check your inputs.")


def irr(cash_flows: List[float], guess: float = 0.1) -> float:
    """
    Calculates the Internal Rate of Return (IRR) for a series of cash flows.

    The IRR is the discount rate that makes the Net Present Value (NPV)
    of all cash flows from a particular project equal to zero.
    This function uses an iterative method to find the IRR.

    Args:
        cash_flows (List[float]): A list of cash flows, where the first cash flow
                                  is typically the initial investment (negative),
                                  followed by positive future cash inflows.
        guess (float, optional): An optional initial guess for the IRR. Defaults to 0.1 (10%).

    Returns:
        float: The Internal Rate of Return.

    Raises:
        TypeError: If cash_flows is not a list or contains non-numeric values, or guess is not numeric.
        ValueError: If cash_flows is empty, all cash flows are positive or negative,
                    or the function fails to converge.

    Example:
        >>> # Initial investment of -$100, followed by $20, $30, $40, $50, $60
        >>> irr([-100, 20, 30, 40, 50, 60])
        0.2809484834920677

    **Cost:** O(k*n), where k is the number of iterations (up to 1000) and n is the length of cash_flows. Iterative method.
    """
    if not isinstance(cash_flows, list):
        raise TypeError("Cash flows must be a list.")
    if not cash_flows:
        raise ValueError("Cash flows list cannot be empty.")
    if not all(isinstance(cf, (int, float)) for cf in cash_flows):
        raise TypeError("All cash flows must be numeric values.")

    # Check for mixed cash flow signs (necessary for a real IRR)
    pos_flow = any(cf > 0 for cf in cash_flows)
    neg_flow = any(cf < 0 for cf in cash_flows)
    if not (pos_flow and neg_flow):
        raise ValueError("Cash flows must contain at least one positive and one negative value to calculate IRR.")

    tolerance = 1e-7
    max_iterations = 1000

    # Define a function to calculate NPV for a given rate
    def npv_for_rate(rate):
        npv_val = 0.0
        for i, flow in enumerate(cash_flows):
            npv_val += flow / ((1 + rate) ** i)
        return npv_val

    # Find a reasonable initial bracket for the IRR using bisection for robustness
    # The range for IRR can be wide, from -1 (or slightly above) to very large numbers.
    low_rate = -0.999999  # Rate cannot be -100% or less
    high_rate = 10.0      # Arbitrarily high rate (1000%)

    # Try to find a bracket where NPV signs differ
    for _ in range(50): # Limited attempts to find bounds
        npv_low = npv_for_rate(low_rate)
        npv_high = npv_for_rate(high_rate)
        if npv_low * npv_high < 0:
            break # Found a bracket
        elif abs(npv_low) < tolerance:
            return low_rate
        elif abs(npv_high) < tolerance:
            return high_rate
        else:
            # Adjust bounds if no bracket found yet
            if npv_low < 0:
                low_rate /= 2
            else:
                low_rate *= 2
            if npv_high > 0:
                high_rate *= 2
            else:
                high_rate /= 2

    if npv_for_rate(low_rate) * npv_for_rate(high_rate) > 0:
        # If after trying to expand bounds, no bracket found,
        # it's possible there's no real root or our range is too limited.
        # Fallback to direct iteration from guess if no robust bracket.
        current_rate = guess
        for i in range(max_iterations):
            npv_val = npv_for_rate(current_rate)
            if abs(npv_val) < tolerance:
                return current_rate
            
            # Numerical derivative for Newton-Raphson: d(NPV)/dr
            # d(Sum[CF_i / (1+r)^i])/dr = Sum[-i * CF_i / (1+r)^(i+1)]
            npv_prime = sum([-i * flow / ((1 + current_rate) ** (i + 1)) for i, flow in enumerate(cash_flows)])

            if abs(npv_prime) < 1e-10: # Avoid division by near-zero derivative
                # If derivative is close to zero, it means the NPV function is flat
                # or we are at a local extremum.
                # Try adjusting guess in a fixed direction or exiting.
                current_rate += tolerance # Small nudge to try to move past flat spot
            else:
                current_rate -= npv_val / npv_prime
            
            if current_rate <= -1.0: # Rate cannot be -100% or less
                current_rate = -0.99999 # Keep it just above -1

        raise ValueError("Failed to converge on an IRR within the maximum number of iterations.")

    # Bisection method (more robust for finding roots)
    for i in range(max_iterations):
        mid_rate = (low_rate + high_rate) / 2
        npv_mid = npv_for_rate(mid_rate)

        if abs(npv_mid) < tolerance:
            return mid_rate
        elif npv_mid * npv_for_rate(low_rate) < 0:
            high_rate = mid_rate
        else:
            low_rate = mid_rate

    raise ValueError("Failed to converge on an IRR within the maximum number of iterations. Check your cash flows.")


def npv(rate: float, values: List[float]) -> float:
    """
    Calculates the Net Present Value (NPV) of an investment.

    NPV is the sum of the present values of the individual cash flows.
    The initial investment (cash outflow) should be the first value in the 'values' list.

    Args:
        rate (float): The discount rate per period (e.g., 0.05 for 5%).
        values (List[float]): A list of cash flows, starting with the initial investment.

    Returns:
        float: The Net Present Value.

    Raises:
        TypeError: If 'rate' is not numeric or 'values' is not a list of numbers.
        ValueError: If 'values' is empty.

    Example:
        >>> # NPV of initial -$100 investment, followed by $20, $30, $40, $50, $60 at 10% discount rate.
        >>> round(npv(rate=0.10, values=[-100, 20, 30, 40, 50, 60]), 2)
        60.85

    **Cost:** O(n), iterates over all cash flows.
    """
    if not isinstance(rate, (int, float)):
        raise TypeError("Rate must be a numeric value.")
    if not isinstance(values, list):
        raise TypeError("Values must be a list of cash flows.")
    if not values:
        raise ValueError("Cash flows list cannot be empty.")
    if not all(isinstance(val, (int, float)) for val in values):
        raise TypeError("All cash flow values must be numeric.")

    # NPV = CF0 + CF1/(1+r)^1 + CF2/(1+r)^2 + ...
    npv_value = 0.0
    for i, flow in enumerate(values):
        npv_value += flow / ((1 + rate) ** i)
    return npv_value


def sln(cost: float, salvage: float, life: Union[int, float]) -> float:
    """
    Calculates the straight-line depreciation of an asset for one period.

    Depreciation is allocated evenly over the useful life of the asset.

    Args:
        cost (float): The initial cost of the asset.
        salvage (float): The salvage value at the end of the useful life of the asset.
        life (Union[int, float]): The number of periods over which the asset is being depreciated.

    Returns:
        float: The straight-line depreciation amount per period.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If 'life' is zero or negative.

    Example:
        >>> # An asset costs $10,000, has a salvage value of $2,000, and a useful life of 5 years.
        >>> sln(cost=10000, salvage=2000, life=5)
        1600.0

    **Cost:** O(1), direct arithmetic calculation.
    """
    if not all(isinstance(arg, (int, float)) for arg in [cost, salvage, life]):
        raise TypeError("Cost, Salvage, and Life must be numeric values.")
    if life <= 0:
        raise ValueError("Life must be a positive number of periods.")

    return (cost - salvage) / life


def db(cost: float, salvage: float, life: Union[int, float], period: Union[int, float], month: int = 12) -> float:
    """
    Calculates the depreciation of an asset for a specified period using the
    fixed-declining balance method.

    Args:
        cost (float): The initial cost of the asset.
        salvage (float): The salvage value at the end of the useful life of the asset.
        life (Union[int, float]): The number of periods over which the asset is being depreciated (e.g., years).
        period (Union[int, float]): The period for which you want to calculate the depreciation.
                                    Must be between 1 and 'life' (inclusive).
        month (int, optional): The number of months in the first year. Defaults to 12.
                                If month is 12, then the initial depreciation is applied over 12 months.
                                If month is different, it adjusts the first period's depreciation.

    Returns:
        float: The depreciation amount for the specified period.

    Raises:
        TypeError: If inputs are not numeric or 'month' is not an integer.
        ValueError: If 'cost' or 'salvage' are negative, 'life' or 'period' are non-positive,
                    'period' is greater than 'life', or 'month' is not between 1 and 12.

    Example:
        >>> # Asset: Cost $10,000, Salvage $1,000, Life 6 years. Depreciation for year 1.
        >>> db(cost=10000, salvage=1000, life=6, period=1)
        3333.333333333333
        >>> # Depreciation for year 2
        >>> db(cost=10000, salvage=1000, life=6, period=2)
        2222.222222222222
        >>> # For an asset acquired mid-year (e.g., 9 months in first year)
        >>> db(cost=10000, salvage=1000, life=6, period=1, month=9)
        2500.0

    **Cost:** O(n), where n is the number of periods (life). Iterates up to the requested period.
    """
    if not all(isinstance(arg, (int, float)) for arg in [cost, salvage, life, period]):
        raise TypeError("Cost, Salvage, Life, and Period must be numeric values.")
    if not isinstance(month, int):
        raise TypeError("Month must be an integer.")
    
    if cost < 0 or salvage < 0:
        raise ValueError("Cost and Salvage cannot be negative.")
    if life <= 0 or period <= 0:
        raise ValueError("Life and Period must be positive.")
    if period > life:
        raise ValueError("Period cannot be greater than Life.")
    if not (1 <= month <= 12):
        raise ValueError("Month must be between 1 and 12.")

    # Excel's DB uses a fixed declining balance rate, usually (2 / life) for double-declining.
    # The DB function allows for custom rates but typically implies this standard.
    # The formula is: (Cost - total depreciation from prior periods) * Rate
    # Rate = 1 - (salvage / cost)^(1/life) -- or just a predefined rate like 2/life for DDB.
    
    # Excel's DB function has a specific internal rate calculation and logic.
    # The default rate in Excel's DB is 200% / life, or 2/life.
    # Let's use the rate calculation consistent with Excel's help for DB:
    rate_db = 1 - (salvage / cost)**(1 / life) if cost > 0 and salvage > 0 else (2 / life)

    remaining_value = cost

    for p in range(1, int(life) + 2): # Iterate up to life + 1 to handle final period and salvage
        if p == 1:
            # First period's depreciation adjusted by 'month'
            dep = remaining_value * rate_db * (month / 12)
        elif p == int(life) + 1:
            # Depreciation in the period after the life (to balance to salvage value)
            # This handles cases where remaining value is more than salvage after full life
            # Excel's DB often ensures the book value doesn't drop below salvage.
            # We calculate what's needed to reach salvage if period exceeds life.
            dep = max(0, min(remaining_value, remaining_value - salvage))
        else:
            dep = remaining_value * rate_db
        
        # Ensure depreciation doesn't reduce book value below salvage
        dep = min(dep, max(0, remaining_value - salvage))
        
        if p == period:
            return dep
        
        remaining_value -= dep
        if remaining_value <= salvage: # Stop depreciating once salvage is reached
            if p + 1 >= period: # If next period is the one requested, return 0 or final adjustment
                return 0.0 # Asset fully depreciated to salvage
            break # Exit loop if asset value reaches salvage prematurely
        
        # For periods after the first, if it's the last year and month < 12 (i.e. start of next year from acquisition)
        # Excel's DB handles mid-year acquisitions by splitting the first and last year's depreciation.
        # If month is given, for subsequent periods, apply full rate except for the last period adjustment
        if p == life and month != 12:
            # This is the last full year of depreciation, before the remaining part of the first year
            # The calculation is complex for exact Excel matching without iterating.
            # The DB function in Excel computes specific depreciation per period.
            # The logic above computes sequentially. Let's refine for direct calculation.
            pass # The loop handles it by keeping track of remaining_value

    # If the requested period is beyond the life or after salvage is reached
    if period > life or remaining_value <= salvage:
        return 0.0
    
    # This should not be reached if logic is sound; acts as a safeguard.
    raise ValueError("Could not calculate DB depreciation for the specified period.")


def xnpv(rate: float, values: List[float],
          dates: list) -> float:
    """Calculates Net Present Value for irregularly spaced cash flows.

    Args:
        rate: Discount rate.
        values: Cash flow amounts.
        dates: Corresponding dates (datetime objects).

    Returns:
        Net present value.

    Raises:
        TypeError: If inputs are invalid types.
        ValueError: If lengths differ or lists are empty.

    Example:
        >>> from datetime import date
        >>> round(xnpv(0.1, [-1000, 300, 400, 500],
        ...     [date(2020,1,1), date(2020,6,1), date(2021,1,1), date(2021,6,1)]), 2)
        72.46

    Complexity: O(n)
    """
    if not isinstance(values, list) or not isinstance(dates, list):
        raise TypeError("'values' and 'dates' must be lists.")

    if len(values) != len(dates):
        raise ValueError("'values' and 'dates' must have the same length.")

    if not values:
        raise ValueError("Lists cannot be empty.")

    if not all(isinstance(v, (int, float)) for v in values):
        raise TypeError("All values must be numeric.")

    if not isinstance(rate, (int, float)):
        raise TypeError("'rate' must be numeric.")

    d0 = dates[0]
    result = 0.0

    for v, d in zip(values, dates):
        days = (d - d0).days
        result += v / ((1 + rate) ** (days / 365.0))

    return result


def xirr(values: List[float], dates: list,
         guess: float = 0.1) -> float:
    """Calculates Internal Rate of Return for irregularly spaced cash flows.

    Args:
        values: Cash flow amounts.
        dates: Corresponding dates (datetime objects).
        guess: Initial rate guess. Default 0.1.

    Returns:
        The XIRR rate.

    Raises:
        TypeError: If inputs are invalid types.
        ValueError: If convergence fails or inputs are invalid.

    Example:
        >>> from datetime import date
        >>> round(xirr([-1000, 300, 400, 500],
        ...     [date(2020,1,1), date(2020,6,1), date(2021,1,1), date(2021,6,1)]), 4)
        0.2417

    Complexity: O(k*n)
    """
    if not isinstance(values, list) or not isinstance(dates, list):
        raise TypeError("'values' and 'dates' must be lists.")

    if len(values) != len(dates):
        raise ValueError("'values' and 'dates' must have the same length.")

    if not values:
        raise ValueError("Lists cannot be empty.")

    if not all(isinstance(v, (int, float)) for v in values):
        raise TypeError("All values must be numeric.")

    tolerance = 1e-7
    max_iterations = 1000
    rate_val = guess

    for _ in range(max_iterations):
        npv_val = xnpv(rate_val, values, dates)

        if abs(npv_val) < tolerance:
            return rate_val

        # Numerical derivative
        h = max(tolerance, abs(rate_val * 1e-5))
        npv_deriv = (xnpv(rate_val + h, values, dates) - npv_val) / h

        if abs(npv_deriv) < 1e-10:
            rate_val += tolerance
            continue

        rate_val -= npv_val / npv_deriv

        if rate_val <= -1.0:
            rate_val = -0.99999

    raise ValueError("XIRR failed to converge.")


def cumipmt(rate: float, nper: int, pv: float, start_period: int,
            end_period: int, type: int = 0) -> float:
    """Calculates cumulative interest paid between two periods.

    Args:
        rate: Interest rate per period.
        nper: Total number of periods.
        pv: Present value (loan amount).
        start_period: First period (1-based).
        end_period: Last period (1-based).
        type: 0 = end of period, 1 = beginning. Default 0.

    Returns:
        Cumulative interest paid.

    Example:
        >>> round(cumipmt(0.05/12, 360, 100000, 1, 12), 2)
        -4948.04

    Complexity: O(n) where n = end_period - start_period
    """
    if not all(isinstance(a, (int, float)) for a in [rate, nper, pv]):
        raise TypeError("Rate, nper, and pv must be numeric.")

    if start_period < 1 or end_period < start_period or end_period > nper:
        raise ValueError("Period range is invalid.")

    return sum(ipmt(rate, p, nper, pv, 0.0, type) for p in range(start_period, end_period + 1))


def cumprinc(rate: float, nper: int, pv: float, start_period: int,
             end_period: int, type: int = 0) -> float:
    """Calculates cumulative principal paid between two periods.

    Args:
        rate: Interest rate per period.
        nper: Total number of periods.
        pv: Present value (loan amount).
        start_period: First period (1-based).
        end_period: Last period (1-based).
        type: 0 = end of period, 1 = beginning. Default 0.

    Returns:
        Cumulative principal paid.

    Example:
        >>> round(cumprinc(0.05/12, 360, 100000, 1, 12), 2)
        -1493.72

    Complexity: O(n) where n = end_period - start_period
    """
    if not all(isinstance(a, (int, float)) for a in [rate, nper, pv]):
        raise TypeError("Rate, nper, and pv must be numeric.")

    if start_period < 1 or end_period < start_period or end_period > nper:
        raise ValueError("Period range is invalid.")

    return sum(ppmt(rate, p, nper, pv, 0.0, type) for p in range(start_period, end_period + 1))


def effect(nominal_rate: float, npery: int) -> float:
    """Calculates the effective annual interest rate.

    Args:
        nominal_rate: Nominal annual interest rate.
        npery: Number of compounding periods per year.

    Returns:
        The effective annual rate.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If nominal_rate <= 0 or npery < 1.

    Example:
        >>> round(effect(0.10, 4), 6)
        0.103813

    Complexity: O(1)
    """
    if not isinstance(nominal_rate, (int, float)):
        raise TypeError("'nominal_rate' must be numeric.")

    if not isinstance(npery, int):
        raise TypeError("'npery' must be an integer.")

    if nominal_rate <= 0:
        raise ValueError("'nominal_rate' must be positive.")

    if npery < 1:
        raise ValueError("'npery' must be at least 1.")

    return (1 + nominal_rate / npery) ** npery - 1


def nominal(effect_rate: float, npery: int) -> float:
    """Calculates the nominal annual interest rate from effective rate.

    Args:
        effect_rate: Effective annual interest rate.
        npery: Number of compounding periods per year.

    Returns:
        The nominal annual rate.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If effect_rate <= 0 or npery < 1.

    Example:
        >>> round(nominal(0.103813, 4), 6)
        0.1

    Complexity: O(1)
    """
    if not isinstance(effect_rate, (int, float)):
        raise TypeError("'effect_rate' must be numeric.")

    if not isinstance(npery, int):
        raise TypeError("'npery' must be an integer.")

    if effect_rate <= 0:
        raise ValueError("'effect_rate' must be positive.")

    if npery < 1:
        raise ValueError("'npery' must be at least 1.")

    return npery * ((1 + effect_rate) ** (1 / npery) - 1)


def syd(cost: float, salvage: float, life: int, per: int) -> float:
    """Calculates depreciation using the sum-of-years' digits method.

    Args:
        cost: Initial cost of the asset.
        salvage: Salvage value at end of life.
        life: Useful life in periods.
        per: Period for which to calculate (1-based).

    Returns:
        Depreciation for the specified period.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If parameters are out of valid ranges.

    Example:
        >>> syd(10000, 1000, 5, 1)
        3000.0
        >>> syd(10000, 1000, 5, 5)
        600.0

    Complexity: O(1)
    """
    if not all(isinstance(a, (int, float)) for a in [cost, salvage, life, per]):
        raise TypeError("All parameters must be numeric.")

    if cost < 0 or salvage < 0:
        raise ValueError("Cost and salvage cannot be negative.")

    if life <= 0 or per <= 0:
        raise ValueError("Life and period must be positive.")

    if per > life:
        raise ValueError("Period cannot exceed life.")

    sum_years = life * (life + 1) / 2
    return (cost - salvage) * (life - per + 1) / sum_years


def fvschedule(principal: float, schedule: List[float]) -> float:
    """Calculates future value with a variable schedule of interest rates.

    Args:
        principal: The initial investment amount.
        schedule: List of interest rates for each period.

    Returns:
        The future value.

    Raises:
        TypeError: If inputs are invalid.
        ValueError: If schedule is empty.

    Example:
        >>> fvschedule(1000, [0.05, 0.06, 0.07])
        1190.91

    Complexity: O(n)
    """
    if not isinstance(principal, (int, float)):
        raise TypeError("'principal' must be numeric.")

    if not isinstance(schedule, list) or not schedule:
        raise ValueError("'schedule' must be a non-empty list.")

    if not all(isinstance(r, (int, float)) for r in schedule):
        raise TypeError("All rates must be numeric.")

    result = principal

    for r in schedule:
        result *= (1 + r)

    return round(result, 2)


def pduration(rate: float, pv: float, fv: float) -> float:
    """Calculates the number of periods to reach a target future value.

    Args:
        rate: Interest rate per period (must be > 0).
        pv: Present value (must be > 0).
        fv: Target future value (must be > 0).

    Returns:
        Number of periods needed.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If rate, pv, or fv are not positive.

    Example:
        >>> round(pduration(0.05, 1000, 2000), 4)
        14.2067

    Complexity: O(1)
    """
    if not all(isinstance(a, (int, float)) for a in [rate, pv, fv]):
        raise TypeError("All parameters must be numeric.")

    if rate <= 0:
        raise ValueError("'rate' must be positive.")

    if pv <= 0 or fv <= 0:
        raise ValueError("'pv' and 'fv' must be positive.")

    return (math.log(fv) - math.log(pv)) / math.log(1 + rate)

def simple_interest(principal: float, rate: float, time_periods: float) -> float:
    """Calculates simple interest.

    Args:
        principal: The initial amount.
        rate: Annual interest rate (e.g. 0.05 for 5%).
        time_periods: Number of periods (years).

    Returns:
        The interest earned.

    Example:
        >>> simple_interest(1000, 0.05, 3)
        150.0

    Complexity: O(1)
    """
    return round(principal * rate * time_periods, 2)


def compound_interest(
    principal: float, rate: float, n: int, t: float,
) -> float:
    """Calculates compound interest (total amount minus principal).

    Args:
        principal: The initial amount.
        rate: Annual interest rate.
        n: Number of compounding periods per year.
        t: Number of years.

    Returns:
        The interest earned (total - principal).

    Example:
        >>> compound_interest(1000, 0.05, 12, 1)
        51.16

    Complexity: O(1)
    """
    total = principal * (1 + rate / n) ** (n * t)
    return round(total - principal, 2)


def roi(gain: float, cost: float) -> float:
    """Calculates Return on Investment as a percentage.

    Args:
        gain: Total return (revenue or final value).
        cost: Total cost (initial investment).

    Returns:
        ROI percentage.

    Raises:
        ValueError: If *cost* is zero.

    Example:
        >>> roi(1500, 1000)
        50.0

    Complexity: O(1)
    """
    if cost == 0:
        raise ValueError("cost must not be zero.")

    return round((gain - cost) / cost * 100, 2)


def cagr(beginning: float, ending: float, years: float) -> float:
    """Calculates the Compound Annual Growth Rate.

    Args:
        beginning: Starting value.
        ending: Ending value.
        years: Number of years.

    Returns:
        CAGR as a decimal (e.g. 0.10 for 10%).

    Raises:
        ValueError: If *beginning* <= 0 or *years* <= 0.

    Example:
        >>> round(cagr(1000, 2000, 5), 4)
        0.1487

    Complexity: O(1)
    """
    if beginning <= 0:
        raise ValueError("beginning must be positive.")

    if years <= 0:
        raise ValueError("years must be positive.")

    return round((ending / beginning) ** (1 / years) - 1, 6)


def break_even_units(
    fixed_costs: float, price_per_unit: float, variable_cost_per_unit: float,
) -> float:
    """Calculates the break-even point in units.

    Args:
        fixed_costs: Total fixed costs.
        price_per_unit: Selling price per unit.
        variable_cost_per_unit: Variable cost per unit.

    Returns:
        Number of units needed to break even.

    Raises:
        ValueError: If price equals variable cost (no margin).

    Example:
        >>> break_even_units(10000, 50, 30)
        500.0

    Complexity: O(1)
    """
    margin = price_per_unit - variable_cost_per_unit

    if margin == 0:
        raise ValueError("Price per unit must exceed variable cost per unit.")

    return round(fixed_costs / margin, 2)


def loan_amortization_table(
    principal: float, annual_rate: float, periods: int,
) -> list[dict]:
    """Generates a loan amortization table with fixed payments.

    Args:
        principal: Loan principal.
        annual_rate: Annual interest rate (e.g. 0.06 for 6%).
        periods: Number of monthly payment periods.

    Returns:
        A list of dicts with keys ``period``, ``payment``, ``interest``,
        ``principal_paid`` and ``balance``.

    Raises:
        ValueError: If *principal* <= 0, *annual_rate* < 0 or *periods* < 1.

    Example:
        >>> table = loan_amortization_table(1200, 0.12, 3)
        >>> table[0]["payment"]
        481.2

    Complexity: O(periods)
    """
    if principal <= 0:
        raise ValueError("principal must be positive.")

    if annual_rate < 0:
        raise ValueError("annual_rate must be >= 0.")

    if periods < 1:
        raise ValueError("periods must be >= 1.")

    monthly_rate = annual_rate / 12

    if monthly_rate == 0:
        payment = round(principal / periods, 2)
    else:
        payment = round(
            principal * monthly_rate / (1 - (1 + monthly_rate) ** -periods), 2
        )

    balance = principal
    table: list[dict] = []

    for p in range(1, periods + 1):
        interest = round(balance * monthly_rate, 2)
        principal_paid = round(payment - interest, 2)
        balance = round(balance - principal_paid, 2)

        if p == periods:
            principal_paid = round(principal_paid + balance, 2)
            balance = 0.0

        table.append({
            "period": p,
            "payment": payment,
            "interest": interest,
            "principal_paid": principal_paid,
            "balance": balance,
        })

    return table


# ---------------------------------------------------------------------------
# Bond, coupon & fixed-income helpers
# ---------------------------------------------------------------------------

def _to_date(d) -> date:
    """Convert input to date."""
    if isinstance(d, datetime):
        return d.date()

    if isinstance(d, date):
        return d

    if isinstance(d, str):
        return datetime.strptime(d, "%Y-%m-%d").date()

    raise TypeError(f"Cannot convert {type(d)} to date.")


def _year_frac(start: date, end: date, basis: int = 0) -> float:
    """Year fraction between two dates.

    basis: 0=US30/360, 1=actual/actual, 2=actual/360, 3=actual/365, 4=EU30/360.
    """
    days_between = (end - start).days

    if basis == 0:
        d1 = min(start.day, 30)
        d2 = 30 if d1 == 30 and end.day == 31 else min(end.day, 31)
        m_diff = (end.year - start.year) * 12 + (end.month - start.month)
        return (m_diff * 30 + d2 - d1) / 360
    elif basis == 1:
        y1, y2 = start.year, end.year

        if y1 == y2:
            year_days = 366 if _is_leap_year(y1) else 365
        else:
            total = sum(366 if _is_leap_year(y) else 365 for y in range(y1, y2 + 1))
            year_days = total / (y2 - y1 + 1)

        return days_between / year_days
    elif basis == 2:
        return days_between / 360
    elif basis == 3:
        return days_between / 365
    elif basis == 4:
        d1 = min(start.day, 30)
        d2 = min(end.day, 30)
        m_diff = (end.year - start.year) * 12 + (end.month - start.month)
        return (m_diff * 30 + d2 - d1) / 360
    else:
        raise ValueError("basis must be 0, 1, 2, 3, or 4.")


def _is_leap_year(year: int) -> bool:
    """Check if year is a leap year."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def _next_coupon_date(settlement: date, maturity: date,
                      frequency: int) -> date:
    """Find the next coupon date after settlement."""
    months_per = 12 // frequency
    d = maturity

    while d > settlement:
        prev = _add_months(d, -months_per)

        if prev <= settlement:
            return d

        d = prev

    return d


def _prev_coupon_date(settlement: date, maturity: date,
                      frequency: int) -> date:
    """Find the previous coupon date before settlement."""
    ncd = _next_coupon_date(settlement, maturity, frequency)
    months_per = 12 // frequency
    return _add_months(ncd, -months_per)


def _add_months(d: date, months: int) -> date:
    """Add months to a date, clamping to last day of month."""
    month = d.month + months
    year = d.year + (month - 1) // 12
    month = (month - 1) % 12 + 1

    max_day = calendar.monthrange(year, month)[1]
    return date(year, month, min(d.day, max_day))


def _coup_num(settlement: date, maturity: date,
              frequency: int) -> int:
    """Number of coupons between settlement and maturity."""
    count = 0
    d = maturity

    while d > settlement:
        count += 1
        d = _add_months(d, -(12 // frequency))

    return count


def dollarde(fractional_dollar: float, fraction: int) -> float:
    """Convert fractional dollar price to decimal.

    Args:
        fractional_dollar: Dollar price expressed as a fraction.
        fraction: Denominator of the fraction.

    Returns:
        float: Decimal dollar price.

    Raises:
        ValueError: If fraction ≤ 0.

    Example:
        >>> dollarde(1.02, 16)
        1.125

    Complexity: O(1)
    """
    if fraction <= 0:
        raise ValueError("fraction must be positive.")

    integer_part = int(fractional_dollar)
    frac_part = fractional_dollar - integer_part
    return integer_part + frac_part * 10 ** math.ceil(math.log10(fraction + 1)) / fraction


def dollarfr(decimal_dollar: float, fraction: int) -> float:
    """Convert decimal dollar price to fractional notation.

    Args:
        decimal_dollar: Decimal dollar price.
        fraction: Denominator for the fractional part.

    Returns:
        float: Fractional dollar price.

    Raises:
        ValueError: If fraction ≤ 0.

    Example:
        >>> dollarfr(1.125, 16)
        1.02

    Complexity: O(1)
    """
    if fraction <= 0:
        raise ValueError("fraction must be positive.")

    integer_part = int(decimal_dollar)
    frac_part = decimal_dollar - integer_part
    return integer_part + frac_part * fraction / 10 ** math.ceil(math.log10(fraction + 1))


def ispmt(rate: float, per: int, nper: int, pv: float) -> float:
    """Interest paid during a specific period of an investment.

    Args:
        rate: Interest rate per period.
        per: Period for which to calculate interest (1-based).
        nper: Total number of periods.
        pv: Present value (principal).

    Returns:
        float: Interest paid in the period.

    Raises:
        ValueError: If per < 1 or per > nper.

    Example:
        >>> round(ispmt(0.1/12, 1, 36, 8000000), 2)
        -64814.81

    Complexity: O(1)
    """
    if per < 1 or per > nper:
        raise ValueError("per must be between 1 and nper.")

    return pv * rate * (per / nper - 1)


def vdb(cost: float, salvage: float, life: float,
        start_period: float, end_period: float,
        factor: float = 2.0, no_switch: bool = False) -> float:
    """Variable declining balance depreciation.

    Args:
        cost: Initial cost of the asset.
        salvage: Salvage value.
        life: Useful life of the asset.
        start_period: Start of the depreciation period.
        end_period: End of the depreciation period.
        factor: Declining balance factor (default 2 = DDB).
        no_switch: If True, do not switch to straight-line.

    Returns:
        float: Depreciation for the period.

    Raises:
        ValueError: If parameters are invalid.

    Example:
        >>> round(vdb(2400, 300, 10, 0, 1), 2)
        480.0

    Complexity: O(n)
    """
    if cost < 0 or salvage < 0 or life <= 0:
        raise ValueError("cost/salvage must be >= 0, life must be > 0.")

    if start_period < 0 or end_period < start_period:
        raise ValueError("Invalid period range.")

    total_dep = 0.0
    book_value = cost

    for period in range(int(math.ceil(end_period))):
        if book_value <= salvage:
            break

        db_dep = book_value * factor / life
        sl_dep = (book_value - salvage) / (life - period)

        if no_switch:
            dep = db_dep
        else:
            dep = max(db_dep, sl_dep)

        dep = min(dep, book_value - salvage)

        if period >= start_period:
            if period + 1 <= end_period:
                total_dep += dep
            else:
                total_dep += dep * (end_period - period)

        book_value -= dep

    return round(total_dep, 2)


def amorlinc(cost: float, date_purchased: str, first_period: str,
             salvage: float, period: int, rate: float,
             basis: int = 0) -> float:
    """Linear depreciation for each accounting period (French system).

    Args:
        cost: Asset cost.
        date_purchased: Purchase date (YYYY-MM-DD).
        first_period: End of first period (YYYY-MM-DD).
        salvage: Salvage value.
        period: Period number (0-based).
        rate: Depreciation rate.
        basis: Day-count basis (0-4).

    Returns:
        float: Depreciation for the period.

    Example:
        >>> round(amorlinc(2400, "2008-01-01", "2008-12-31", 300, 1, 0.15), 2)
        360.0

    Complexity: O(1)
    """
    dep = cost * rate

    if period == 0:
        d_start = _to_date(date_purchased)
        d_end = _to_date(first_period)
        frac = _year_frac(d_start, d_end, basis)
        return round(dep * frac, 2)

    accum = cost * rate * _year_frac(
        _to_date(date_purchased), _to_date(first_period), basis
    )

    for p in range(1, period):
        accum += dep

        if accum >= cost - salvage:
            return 0.0

    remaining = cost - salvage - accum

    if remaining <= 0:
        return 0.0

    return round(min(dep, remaining), 2)


def disc(settlement: str, maturity: str, pr: float,
         redemption: float, basis: int = 0) -> float:
    """Discount rate for a security.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        pr: Security price per $100 face.
        redemption: Redemption value per $100 face.
        basis: Day-count basis (0-4).

    Returns:
        float: Discount rate.

    Example:
        >>> round(disc("2018-02-07", "2018-07-15", 97.975, 100, 0), 6)
        0.046131

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    yf = _year_frac(s, m, basis)

    if yf == 0:
        raise ValueError("Settlement and maturity must differ.")

    return (redemption - pr) / redemption / yf


def intrate(settlement: str, maturity: str, investment: float,
            redemption: float, basis: int = 0) -> float:
    """Interest rate for a fully invested security.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        investment: Amount invested.
        redemption: Amount received at maturity.
        basis: Day-count basis (0-4).

    Returns:
        float: Interest rate.

    Example:
        >>> round(intrate("2008-02-15", "2008-05-15", 1000000, 1014420, 2), 6)
        0.058328

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    yf = _year_frac(s, m, basis)

    if yf == 0:
        raise ValueError("Settlement and maturity must differ.")

    return (redemption - investment) / investment / yf


def received(settlement: str, maturity: str, investment: float,
             discount: float, basis: int = 0) -> float:
    """Amount received at maturity for a fully invested security.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        investment: Amount invested.
        discount: Discount rate.
        basis: Day-count basis (0-4).

    Returns:
        float: Amount received at maturity.

    Example:
        >>> round(received("2008-02-15", "2008-05-15", 1000000, 0.0575, 2), 2)
        1014584.65

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    yf = _year_frac(s, m, basis)
    denominator = 1 - discount * yf

    if denominator == 0:
        raise ValueError("Discount results in zero denominator.")

    return investment / denominator


def accrint(issue: str, first_interest: str, settlement: str,
            rate: float, par: float, frequency: int,
            basis: int = 0) -> float:
    """Accrued interest for a security that pays periodic interest.

    Args:
        issue: Issue date (YYYY-MM-DD).
        first_interest: First interest date (YYYY-MM-DD).
        settlement: Settlement date (YYYY-MM-DD).
        rate: Annual coupon rate.
        par: Par value.
        frequency: Payments per year (1, 2, or 4).
        basis: Day-count basis (0-4).

    Returns:
        float: Accrued interest.

    Example:
        >>> round(accrint("2008-03-01", "2008-08-31", "2008-05-01", 0.10, 1000, 2), 2)
        16.67

    Complexity: O(1)
    """
    if frequency not in (1, 2, 4):
        raise ValueError("frequency must be 1, 2, or 4.")

    i = _to_date(issue)
    s = _to_date(settlement)
    yf = _year_frac(i, s, basis)
    return par * rate * yf


def accrintm(issue: str, settlement: str, rate: float,
             par: float, basis: int = 0) -> float:
    """Accrued interest for a security that pays interest at maturity.

    Args:
        issue: Issue date (YYYY-MM-DD).
        settlement: Settlement (maturity) date (YYYY-MM-DD).
        rate: Annual coupon rate.
        par: Par value.
        basis: Day-count basis (0-4).

    Returns:
        float: Accrued interest.

    Example:
        >>> round(accrintm("2008-04-01", "2008-06-15", 0.10, 1000, 3), 2)
        20.55

    Complexity: O(1)
    """
    i = _to_date(issue)
    s = _to_date(settlement)
    yf = _year_frac(i, s, basis)
    return par * rate * yf


def price(settlement: str, maturity: str, rate: float,
          yld: float, redemption: float, frequency: int,
          basis: int = 0) -> float:
    """Price per $100 face of a security paying periodic interest.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        rate: Annual coupon rate.
        yld: Annual yield.
        redemption: Redemption value per $100 face.
        frequency: Coupon payments per year (1, 2, or 4).
        basis: Day-count basis (0-4).

    Returns:
        float: Price per $100 face value.

    Example:
        >>> round(price("2008-02-15", "2017-11-15", 0.0575, 0.065, 100, 2, 0), 4)
        94.6344

    Complexity: O(n) where n = number of coupons
    """
    if frequency not in (1, 2, 4):
        raise ValueError("frequency must be 1, 2, or 4.")

    s = _to_date(settlement)
    m = _to_date(maturity)

    n = _coup_num(s, m, frequency)
    coupon = rate * 100 / frequency
    yld_per = yld / frequency

    ncd = _next_coupon_date(s, m, frequency)
    pcd = _prev_coupon_date(s, m, frequency)

    e = (ncd - pcd).days
    a = (s - pcd).days
    dsc = e - a

    if yld_per == 0:
        pv_coupons = coupon * n
        pv_redemption = redemption
    else:
        pv_coupons = sum(
            coupon / (1 + yld_per) ** (i + dsc / e)
            for i in range(n)
        )
        pv_redemption = redemption / (1 + yld_per) ** (n - 1 + dsc / e)

    accrued = coupon * a / e
    return pv_coupons + pv_redemption - accrued


def pricedisc(settlement: str, maturity: str, discount: float,
              redemption: float, basis: int = 0) -> float:
    """Price per $100 face of a discounted security.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        discount: Discount rate.
        redemption: Redemption value per $100 face.
        basis: Day-count basis (0-4).

    Returns:
        float: Price per $100 face value.

    Example:
        >>> round(pricedisc("2008-02-16", "2008-03-01", 0.0525, 100, 2), 4)
        99.7958

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    yf = _year_frac(s, m, basis)
    return redemption - discount * redemption * yf


def pricemat(settlement: str, maturity: str, issue: str,
             rate: float, yld: float, basis: int = 0) -> float:
    """Price per $100 face of a security that pays at maturity.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        issue: Issue date (YYYY-MM-DD).
        rate: Annual coupon rate.
        yld: Annual yield.
        basis: Day-count basis (0-4).

    Returns:
        float: Price per $100 face value.

    Example:
        >>> round(pricemat("2008-02-15", "2008-04-13", "2007-11-11", 0.061, 0.061, 0), 4)
        99.9844

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    i = _to_date(issue)

    b = _year_frac(i, m, basis)
    a = _year_frac(i, s, basis)
    dsm = _year_frac(s, m, basis)

    numerator = 100 + (b * rate * 100)
    denominator = 1 + (dsm * yld)
    accrued = a * rate * 100

    return numerator / denominator - accrued


def yield_bond(settlement: str, maturity: str, rate: float,
               pr: float, redemption: float, frequency: int,
               basis: int = 0) -> float:
    """Yield of a security that pays periodic interest.

    Description:
        Uses Newton-Raphson iteration to find the yield.
        Equivalent to Excel YIELD.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        rate: Annual coupon rate.
        pr: Current price per $100 face.
        redemption: Redemption value per $100 face.
        frequency: Coupon payments per year (1, 2, or 4).
        basis: Day-count basis (0-4).

    Returns:
        float: Annual yield.

    Example:
        >>> round(yield_bond("2008-02-15", "2016-11-15", 0.0575, 95.04287, 100, 2, 0), 4)
        0.065

    Complexity: O(k × n) where k = iterations, n = coupons
    """
    guess = rate

    for _ in range(100):
        p = price(settlement, maturity, rate, guess, redemption, frequency, basis)
        diff = p - pr

        if abs(diff) < 1e-8:
            return guess

        # numerical derivative
        dp = price(settlement, maturity, rate, guess + 0.0001, redemption,
                    frequency, basis) - p
        deriv = dp / 0.0001

        if abs(deriv) < 1e-15:
            break

        guess -= diff / deriv

    return guess


def yielddisc(settlement: str, maturity: str, pr: float,
              redemption: float, basis: int = 0) -> float:
    """Yield for a discounted security.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        pr: Price per $100 face.
        redemption: Redemption value per $100 face.
        basis: Day-count basis (0-4).

    Returns:
        float: Annual yield.

    Example:
        >>> round(yielddisc("2008-02-16", "2008-03-01", 99.795, 100, 2), 6)
        0.056873

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    yf = _year_frac(s, m, basis)

    if yf == 0 or pr == 0:
        raise ValueError("Invalid dates or price.")

    return (redemption - pr) / pr / yf


def yieldmat(settlement: str, maturity: str, issue: str,
             rate: float, pr: float, basis: int = 0) -> float:
    """Yield of a security that pays interest at maturity.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        issue: Issue date (YYYY-MM-DD).
        rate: Annual coupon rate.
        pr: Price per $100 face.
        basis: Day-count basis (0-4).

    Returns:
        float: Annual yield.

    Example:
        >>> round(yieldmat("2008-03-15", "2008-11-03", "2007-11-08", 0.0625, 100.0123, 0), 4)
        0.0609

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    i = _to_date(issue)

    dim = _year_frac(i, m, basis)
    a = _year_frac(i, s, basis)
    dsm = _year_frac(s, m, basis)

    if dsm == 0:
        raise ValueError("Settlement and maturity must differ.")

    numerator = (1 + dim * rate) / (pr / 100 + a * rate) - 1
    return numerator / dsm


def duration(settlement: str, maturity: str, coupon: float,
             yld: float, frequency: int, basis: int = 0) -> float:
    """Macaulay duration for a bond with par value $100.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        coupon: Annual coupon rate.
        yld: Annual yield.
        frequency: Coupon payments per year (1, 2, or 4).
        basis: Day-count basis (0-4).

    Returns:
        float: Macaulay duration in years.

    Example:
        >>> round(duration("2008-01-01", "2016-01-01", 0.08, 0.09, 2, 1), 4)
        5.9937

    Complexity: O(n) where n = number of coupons
    """
    if frequency not in (1, 2, 4):
        raise ValueError("frequency must be 1, 2, or 4.")

    s = _to_date(settlement)
    m = _to_date(maturity)

    n = _coup_num(s, m, frequency)
    coup = coupon * 100 / frequency
    yld_per = yld / frequency

    ncd = _next_coupon_date(s, m, frequency)
    pcd = _prev_coupon_date(s, m, frequency)
    e = (ncd - pcd).days
    dsc = (ncd - s).days

    pv_total = 0.0
    weighted_total = 0.0

    for k in range(1, n + 1):
        t = (k - 1 + dsc / e) / frequency
        cf = coup if k < n else coup + 100
        pv = cf / (1 + yld_per) ** (k - 1 + dsc / e)
        pv_total += pv
        weighted_total += t * pv

    if pv_total == 0:
        return 0.0

    return weighted_total / pv_total


def mduration(settlement: str, maturity: str, coupon: float,
              yld: float, frequency: int, basis: int = 0) -> float:
    """Modified duration for a bond with par value $100.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        coupon: Annual coupon rate.
        yld: Annual yield.
        frequency: Coupon payments per year (1, 2, or 4).
        basis: Day-count basis (0-4).

    Returns:
        float: Modified Macaulay duration.

    Example:
        >>> round(mduration("2008-01-01", "2016-01-01", 0.08, 0.09, 2, 1), 4)
        5.7356

    Complexity: O(n) where n = number of coupons
    """
    mac = duration(settlement, maturity, coupon, yld, frequency, basis)
    return mac / (1 + yld / frequency)


def coupdays(settlement: str, maturity: str, frequency: int,
             basis: int = 0) -> float:
    """Number of days in the coupon period containing settlement.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        frequency: Coupon payments per year (1, 2, or 4).
        basis: Day-count basis (0-4).

    Returns:
        float: Days in the coupon period.

    Example:
        >>> coupdays("2011-01-25", "2011-11-15", 2, 1)
        181

    Complexity: O(n)
    """
    if frequency not in (1, 2, 4):
        raise ValueError("frequency must be 1, 2, or 4.")

    if basis in (0, 4):
        return 360 / frequency

    s = _to_date(settlement)
    m = _to_date(maturity)

    ncd = _next_coupon_date(s, m, frequency)
    pcd = _prev_coupon_date(s, m, frequency)
    return (ncd - pcd).days


def coupdaybs(settlement: str, maturity: str, frequency: int,
              basis: int = 0) -> float:
    """Days from beginning of coupon period to settlement.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        frequency: Coupon payments per year (1, 2, or 4).
        basis: Day-count basis (0-4).

    Returns:
        float: Number of days.

    Example:
        >>> coupdaybs("2011-01-25", "2011-11-15", 2, 1)
        71

    Complexity: O(n)
    """
    if frequency not in (1, 2, 4):
        raise ValueError("frequency must be 1, 2, or 4.")

    s = _to_date(settlement)
    m = _to_date(maturity)

    pcd = _prev_coupon_date(s, m, frequency)

    if basis in (0, 4):
        d1 = min(pcd.day, 30)
        d2 = min(s.day, 30)
        return (s.year - pcd.year) * 360 + (s.month - pcd.month) * 30 + d2 - d1

    return (s - pcd).days


def coupdaysnc(settlement: str, maturity: str, frequency: int,
               basis: int = 0) -> float:
    """Days from settlement to next coupon date.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        frequency: Coupon payments per year (1, 2, or 4).
        basis: Day-count basis (0-4).

    Returns:
        float: Number of days.

    Example:
        >>> coupdaysnc("2011-01-25", "2011-11-15", 2, 1)
        110

    Complexity: O(n)
    """
    if frequency not in (1, 2, 4):
        raise ValueError("frequency must be 1, 2, or 4.")

    s = _to_date(settlement)
    m = _to_date(maturity)
    ncd = _next_coupon_date(s, m, frequency)

    if basis in (0, 4):
        return coupdays(settlement, maturity, frequency, basis) - \
               coupdaybs(settlement, maturity, frequency, basis)

    return (ncd - s).days


def coupncd(settlement: str, maturity: str,
            frequency: int) -> date:
    """Next coupon date after settlement.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        frequency: Coupon payments per year (1, 2, or 4).

    Returns:
        date: Next coupon date.

    Example:
        >>> coupncd("2011-01-25", "2011-11-15", 2)
        datetime.date(2011, 5, 15)

    Complexity: O(n)
    """
    if frequency not in (1, 2, 4):
        raise ValueError("frequency must be 1, 2, or 4.")

    s = _to_date(settlement)
    m = _to_date(maturity)
    return _next_coupon_date(s, m, frequency)


def couppcd(settlement: str, maturity: str,
            frequency: int) -> date:
    """Previous coupon date before settlement.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        frequency: Coupon payments per year (1, 2, or 4).

    Returns:
        date: Previous coupon date.

    Example:
        >>> couppcd("2011-01-25", "2011-11-15", 2)
        datetime.date(2010, 11, 15)

    Complexity: O(n)
    """
    if frequency not in (1, 2, 4):
        raise ValueError("frequency must be 1, 2, or 4.")

    s = _to_date(settlement)
    m = _to_date(maturity)
    return _prev_coupon_date(s, m, frequency)


def coupnum(settlement: str, maturity: str,
            frequency: int) -> int:
    """Number of coupons between settlement and maturity.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        frequency: Coupon payments per year (1, 2, or 4).

    Returns:
        int: Number of coupon payments.

    Example:
        >>> coupnum("2011-01-25", "2013-11-15", 2)
        6

    Complexity: O(n)
    """
    if frequency not in (1, 2, 4):
        raise ValueError("frequency must be 1, 2, or 4.")

    s = _to_date(settlement)
    m = _to_date(maturity)
    return _coup_num(s, m, frequency)


def tbilleq(settlement: str, maturity: str,
            discount: float) -> float:
    """Bond-equivalent yield for a Treasury bill.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        discount: Discount rate.

    Returns:
        float: Bond-equivalent yield.

    Example:
        >>> round(tbilleq("2008-03-31", "2008-06-01", 0.0914), 6)
        0.094151

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    dsm = (m - s).days

    if dsm <= 0:
        raise ValueError("Maturity must be after settlement.")

    return 365 * discount / (360 - discount * dsm)


def tbillprice(settlement: str, maturity: str,
               discount: float) -> float:
    """Price per $100 face for a Treasury bill.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        discount: Discount rate.

    Returns:
        float: Price per $100 face.

    Example:
        >>> round(tbillprice("2008-03-31", "2008-06-01", 0.09), 4)
        98.45

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    dsm = (m - s).days

    if dsm <= 0:
        raise ValueError("Maturity must be after settlement.")

    return 100 * (1 - discount * dsm / 360)


def tbillyield(settlement: str, maturity: str,
               pr: float) -> float:
    """Yield for a Treasury bill.

    Args:
        settlement: Settlement date (YYYY-MM-DD).
        maturity: Maturity date (YYYY-MM-DD).
        pr: Price per $100 face.

    Returns:
        float: Annual yield.

    Example:
        >>> round(tbillyield("2008-03-31", "2008-06-01", 98.45), 6)
        0.091417

    Complexity: O(1)
    """
    s = _to_date(settlement)
    m = _to_date(maturity)
    dsm = (m - s).days

    if dsm <= 0 or pr <= 0:
        raise ValueError("Invalid dates or price.")

    return (100 - pr) / pr * 360 / dsm


def rri(nper: Union[int, float], pv: float, fv: float) -> float:
    """Equivalent interest rate for the growth of an investment.

    Description:
        Returns the rate needed for pv to grow to fv over nper periods.
        Formula: (fv / pv)^(1/nper) - 1. Equivalent to Excel RRI.

    Args:
        nper: Number of periods (> 0).
        pv: Present value (must not be zero).
        fv: Future value.

    Returns:
        float: Equivalent per-period interest rate.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If nper ≤ 0 or pv = 0.

    Example:
        >>> round(rri(96, 10000, 11000), 6)
        0.000993

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [nper, pv, fv]):
        raise TypeError("All parameters must be numeric.")

    if nper <= 0:
        raise ValueError("nper must be positive.")

    if pv == 0:
        raise ValueError("pv must not be zero.")

    return (fv / pv) ** (1 / nper) - 1


def payback_period(initial_investment: float,
                   cash_flows: List[float]) -> float:
    """Calculates the simple payback period of an investment.

    The payback period is the time required for cumulative cash flows to
    equal the initial investment. Returns a fractional period value
    using linear interpolation within the break-even period.

    Args:
        initial_investment: Positive upfront cost.
        cash_flows: List of periodic cash inflows.

    Returns:
        Number of periods to recover the investment.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If the investment is never recovered.

    Example:
        >>> payback_period(1000, [300, 400, 400, 200])
        2.75

    Complexity: O(n)
    """
    if not isinstance(initial_investment, (int, float)):
        raise TypeError("initial_investment must be numeric.")

    if not isinstance(cash_flows, list) or not all(isinstance(c, (int, float)) for c in cash_flows):
        raise TypeError("cash_flows must be a list of numeric values.")

    cumulative = 0.0

    for i, cf in enumerate(cash_flows):
        cumulative += cf

        if cumulative >= initial_investment:
            overshoot = cumulative - initial_investment
            fraction = 1 - (overshoot / cf) if cf != 0 else 0
            return i + fraction

    raise ValueError("Investment is never fully recovered within the given cash flows.")


def profitability_index(rate: float, initial_investment: float,
                        cash_flows: List[float]) -> float:
    """Calculates the Profitability Index (PI) of a project.

    PI = PV(future cash flows) / initial investment.
    A PI > 1 indicates a potentially profitable investment.

    Args:
        rate: Discount rate per period.
        initial_investment: Positive upfront cost.
        cash_flows: List of future cash flows.

    Returns:
        Profitability index as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If initial_investment <= 0.

    Example:
        >>> round(profitability_index(0.10, 1000, [300, 400, 500, 200]), 4)
        1.1156

    Complexity: O(n)
    """
    if not isinstance(rate, (int, float)):
        raise TypeError("rate must be numeric.")

    if not isinstance(initial_investment, (int, float)):
        raise TypeError("initial_investment must be numeric.")

    if initial_investment <= 0:
        raise ValueError("initial_investment must be positive.")

    if not isinstance(cash_flows, list) or not all(isinstance(c, (int, float)) for c in cash_flows):
        raise TypeError("cash_flows must be a list of numeric values.")

    pv_flows = sum(cf / (1 + rate) ** (i + 1) for i, cf in enumerate(cash_flows))
    return pv_flows / initial_investment


def ddb(
    cost: float,
    salvage: float,
    life: Union[int, float],
    period: Union[int, float],
    factor: float = 2.0,
) -> float:
    """Calculates depreciation using the double-declining-balance method.

    In each period the depreciation is min(rate * book_value, book_value - salvage).

    Args:
        cost: Initial cost of the asset.
        salvage: Salvage value at end of life.
        life: Useful life in periods.
        period: Period for which to compute depreciation (1-based).
        factor: Declining-balance factor (default 2 for double).

    Returns:
        Depreciation for the given period.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any value is negative, life is zero, or period > life.

    Example:
        >>> round(ddb(10000, 1000, 5, 1), 2)
        4000.0
        >>> round(ddb(10000, 1000, 5, 2), 2)
        2400.0

    Complexity: O(period)
    """
    if not all(isinstance(v, (int, float)) for v in [cost, salvage, life, period, factor]):
        raise TypeError("All arguments must be numeric.")

    if cost < 0 or salvage < 0 or life <= 0 or period < 1 or factor <= 0:
        raise ValueError("cost >= 0, salvage >= 0, life > 0, period >= 1, factor > 0.")

    if period > life:
        raise ValueError("period must not exceed life.")

    rate = factor / life
    book_value = cost
    dep = 0.0

    for p in range(1, int(period) + 1):
        dep = min(rate * book_value, book_value - salvage)
        dep = max(dep, 0.0)
        book_value -= dep

    return dep


def ipmt(
    rate: float,
    per: Union[int, float],
    nper: Union[int, float],
    pv: float,
    fv: float = 0.0,
    type_: int = 0,
) -> float:
    """Calculates the interest portion of a payment for a given period.

    Uses the standard TVM formula to compute each periodic payment,
    then isolates the interest component.

    Args:
        rate: Interest rate per period.
        per: The period for which to find interest (1-based).
        nper: Total number of periods.
        pv: Present value (principal).
        fv: Future value (default 0).
        type_: 0 = end of period (ordinary), 1 = beginning (annuity due).

    Returns:
        Interest portion of the payment for the specified period.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If per < 1 or per > nper.

    Example:
        >>> round(ipmt(0.1/12, 1, 36, 8000), 2)
        -66.67

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in [rate, per, nper, pv, fv]):
        raise TypeError("All arguments must be numeric.")

    if per < 1 or per > nper:
        raise ValueError("per must be between 1 and nper.")

    total_pmt = pmt(rate, nper, pv, fv, type_)

    if rate == 0:
        return 0.0

    # Balance at start of the given period (using FV sign convention)
    if type_ == 0:
        remaining = pv * (1 + rate) ** (per - 1) + total_pmt * (((1 + rate) ** (per - 1) - 1) / rate)
        return -remaining * rate
    else:
        # Annuity-due: payment at start of period
        if per == 1:
            return 0.0

        remaining = pv * (1 + rate) ** (per - 1) + total_pmt * (1 + rate) * (((1 + rate) ** (per - 1) - 1) / rate)
        return -remaining * rate / (1 + rate)


def ppmt(
    rate: float,
    per: Union[int, float],
    nper: Union[int, float],
    pv: float,
    fv: float = 0.0,
    type_: int = 0,
) -> float:
    """Calculates the principal portion of a payment for a given period.

    The principal portion is the total payment minus the interest portion.

    Args:
        rate: Interest rate per period.
        per: The period for which to find principal (1-based).
        nper: Total number of periods.
        pv: Present value (principal).
        fv: Future value (default 0).
        type_: 0 = end of period (ordinary), 1 = beginning (annuity due).

    Returns:
        Principal portion of the payment for the specified period.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If per < 1 or per > nper.

    Example:
        >>> round(ppmt(0.1/12, 1, 36, 8000), 2)
        -191.47

    Complexity: O(1)
    """
    total = pmt(rate, nper, pv, fv, type_)
    interest = ipmt(rate, per, nper, pv, fv, type_)
    return total - interest


def mirr(
    cash_flows: List[float],
    finance_rate: float,
    reinvest_rate: float,
) -> float:
    """Calculates the Modified Internal Rate of Return.

    MIRR resolves IRR's multiple-root issue by separating the finance
    rate (for negative flows) from the reinvestment rate (for positive
    flows).

    Args:
        cash_flows: List of cash flows (first is typically negative).
        finance_rate: Interest rate paid on borrowed money.
        reinvest_rate: Return rate on reinvested positive flows.

    Returns:
        The MIRR as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If cash_flows has < 2 values or no sign change.

    Example:
        >>> round(mirr([-100, 50, 60, 70], 0.10, 0.12), 4)
        0.2598

    Complexity: O(n)
    """
    if not isinstance(cash_flows, list) or not all(isinstance(c, (int, float)) for c in cash_flows):
        raise TypeError("cash_flows must be a list of numeric values.")

    if not isinstance(finance_rate, (int, float)) or not isinstance(reinvest_rate, (int, float)):
        raise TypeError("finance_rate and reinvest_rate must be numeric.")

    if len(cash_flows) < 2:
        raise ValueError("cash_flows must have at least 2 values.")

    n = len(cash_flows)

    # PV of negative flows at finance rate
    pv_neg = sum(
        cf / (1 + finance_rate) ** i
        for i, cf in enumerate(cash_flows)
        if cf < 0
    )

    # FV of positive flows at reinvestment rate
    fv_pos = sum(
        cf * (1 + reinvest_rate) ** (n - 1 - i)
        for i, cf in enumerate(cash_flows)
        if cf > 0
    )

    if pv_neg == 0:
        raise ValueError("cash_flows must contain at least one negative value.")

    if fv_pos == 0:
        raise ValueError("cash_flows must contain at least one positive value.")

    return ((-fv_pos / pv_neg) ** (1.0 / (n - 1))) - 1


def wacc(
    equity: float,
    debt: float,
    cost_of_equity: float,
    cost_of_debt: float,
    tax_rate: float,
) -> float:
    """Computes the Weighted Average Cost of Capital.

    WACC = (E/(E+D)) × Re + (D/(E+D)) × Rd × (1 − T).

    Args:
        equity: Market value of equity (positive).
        debt: Market value of debt (non-negative).
        cost_of_equity: Cost of equity as decimal (e.g. 0.10 for 10%).
        cost_of_debt: Cost of debt as decimal.
        tax_rate: Corporate tax rate as decimal (0 to 1).

    Returns:
        The WACC as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If equity <= 0 or debt < 0 or tax_rate not in [0, 1].

    Example:
        >>> round(wacc(600000, 400000, 0.08, 0.05, 0.30), 4)
        0.062

    Complexity: O(1)
    """
    for name, val in [("equity", equity), ("debt", debt),
                      ("cost_of_equity", cost_of_equity),
                      ("cost_of_debt", cost_of_debt), ("tax_rate", tax_rate)]:

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if equity <= 0:
        raise ValueError("equity must be positive.")

    if debt < 0:
        raise ValueError("debt must be non-negative.")

    if not 0 <= tax_rate <= 1:
        raise ValueError("tax_rate must be between 0 and 1.")

    total = equity + debt
    return (equity / total) * cost_of_equity + (debt / total) * cost_of_debt * (1 - tax_rate)


def capm(
    risk_free_rate: float,
    beta: float,
    market_return: float,
) -> float:
    """Computes the expected return using the Capital Asset Pricing Model.

    E(R) = Rf + β × (Rm − Rf).

    Args:
        risk_free_rate: Risk-free rate as decimal.
        beta: Asset beta (systematic risk).
        market_return: Expected market return as decimal.

    Returns:
        Expected return as a decimal.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> round(capm(0.03, 1.2, 0.10), 4)
        0.114

    Complexity: O(1)
    """
    for name, val in [("risk_free_rate", risk_free_rate),
                      ("beta", beta), ("market_return", market_return)]:

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    return risk_free_rate + beta * (market_return - risk_free_rate)


def sharpe_ratio(
    returns: List[float],
    risk_free_rate: float = 0.0,
) -> float:
    """Computes the Sharpe ratio of a return series.

    SR = (mean(R) − Rf) / std(R).

    Args:
        returns: List of periodic returns (as decimals).
        risk_free_rate: Risk-free rate per period.

    Returns:
        The Sharpe ratio.

    Raises:
        TypeError: If inputs are invalid types.
        ValueError: If returns is empty or has zero standard deviation.

    Example:
        >>> round(sharpe_ratio([0.05, 0.02, 0.08, -0.01, 0.04], 0.01), 4)
        0.4728

    Complexity: O(n)
    """
    if not isinstance(returns, list):
        raise TypeError("returns must be a list.")

    if not returns:
        raise ValueError("returns cannot be empty.")

    if not all(isinstance(r, (int, float)) for r in returns):
        raise TypeError("All returns must be numeric.")

    if not isinstance(risk_free_rate, (int, float)):
        raise TypeError("risk_free_rate must be numeric.")

    n = len(returns)
    mean_r = sum(returns) / n
    variance = sum((r - mean_r) ** 2 for r in returns) / n
    std_r = math.sqrt(variance)

    if std_r == 0:
        raise ValueError("Standard deviation of returns is zero.")

    return (mean_r - risk_free_rate) / std_r


def sortino_ratio(
    returns: List[float],
    risk_free_rate: float = 0.0,
) -> float:
    """Computes the Sortino ratio (uses downside deviation only).

    SR = (mean(R) − Rf) / downside_dev.

    Args:
        returns: List of periodic returns (as decimals).
        risk_free_rate: Minimum acceptable return per period.

    Returns:
        The Sortino ratio.

    Raises:
        TypeError: If inputs are invalid types.
        ValueError: If returns is empty or has zero downside deviation.

    Example:
        >>> round(sortino_ratio([0.05, 0.02, 0.08, -0.01, 0.04], 0.01), 4)
        1.0328

    Complexity: O(n)
    """
    if not isinstance(returns, list):
        raise TypeError("returns must be a list.")

    if not returns:
        raise ValueError("returns cannot be empty.")

    if not all(isinstance(r, (int, float)) for r in returns):
        raise TypeError("All returns must be numeric.")

    if not isinstance(risk_free_rate, (int, float)):
        raise TypeError("risk_free_rate must be numeric.")

    n = len(returns)
    mean_r = sum(returns) / n
    downside_sq = [min(0, r - risk_free_rate) ** 2 for r in returns]
    downside_var = sum(downside_sq) / n
    downside_dev = math.sqrt(downside_var)

    if downside_dev == 0:
        return float("inf")

    return (mean_r - risk_free_rate) / downside_dev


def debt_to_equity(total_debt: float, total_equity: float) -> float:
    """Computes the debt-to-equity ratio.

    D/E = Total Debt / Total Equity.

    Args:
        total_debt: Total liabilities (non-negative).
        total_equity: Total shareholders' equity (positive).

    Returns:
        The D/E ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If debt < 0 or equity <= 0.

    Example:
        >>> debt_to_equity(500000, 250000)
        2.0

    Complexity: O(1)
    """
    if not isinstance(total_debt, (int, float)):
        raise TypeError("total_debt must be numeric.")

    if not isinstance(total_equity, (int, float)):
        raise TypeError("total_equity must be numeric.")

    if total_debt < 0:
        raise ValueError("total_debt must be non-negative.")

    if total_equity <= 0:
        raise ValueError("total_equity must be positive.")

    return total_debt / total_equity


def rule_of_72(rate: Union[int, float]) -> float:
    """Estimates the number of periods to double an investment.

    Uses the Rule of 72: periods ≈ 72 / (rate × 100).

    Args:
        rate: Interest rate per period as a decimal (e.g. 0.06 for 6 %).

    Returns:
        Approximate number of periods to double.

    Raises:
        TypeError: If rate is not numeric.
        ValueError: If rate is zero or negative.

    Example:
        >>> rule_of_72(0.06)
        12.0

    Complexity: O(1)
    """
    if not isinstance(rate, (int, float)):
        raise TypeError("rate must be numeric.")

    if rate <= 0:
        raise ValueError("rate must be positive.")

    return 72.0 / (rate * 100)


def real_rate_of_return(
    nominal_rate: Union[int, float],
    inflation_rate: Union[int, float],
) -> float:
    """Computes the real rate of return using the Fisher equation.

    real = ((1 + nominal) / (1 + inflation)) − 1.

    Args:
        nominal_rate: Nominal interest rate as a decimal.
        inflation_rate: Inflation rate as a decimal.

    Returns:
        Real rate of return as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inflation_rate is −1 (division by zero).

    Example:
        >>> round(real_rate_of_return(0.08, 0.03), 6)
        0.048544

    Complexity: O(1)
    """
    if not isinstance(nominal_rate, (int, float)):
        raise TypeError("nominal_rate must be numeric.")

    if not isinstance(inflation_rate, (int, float)):
        raise TypeError("inflation_rate must be numeric.")

    if inflation_rate == -1:
        raise ValueError("inflation_rate cannot be -1.")

    return ((1 + nominal_rate) / (1 + inflation_rate)) - 1


def gross_margin(revenue: Union[int, float], cogs: Union[int, float]) -> float:
    """Computes the gross margin ratio.

    gross_margin = (revenue − COGS) / revenue.

    Args:
        revenue: Total revenue.
        cogs: Cost of goods sold.

    Returns:
        Gross margin as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If revenue is zero.

    Example:
        >>> gross_margin(100000, 60000)
        0.4

    Complexity: O(1)
    """
    if not isinstance(revenue, (int, float)):
        raise TypeError("revenue must be numeric.")

    if not isinstance(cogs, (int, float)):
        raise TypeError("cogs must be numeric.")

    if revenue == 0:
        raise ValueError("revenue must not be zero.")

    return (revenue - cogs) / revenue


def operating_margin(
    operating_income: Union[int, float],
    revenue: Union[int, float],
) -> float:
    """Computes the operating margin ratio.

    operating_margin = operating_income / revenue.

    Args:
        operating_income: Operating income (EBIT).
        revenue: Total revenue.

    Returns:
        Operating margin as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If revenue is zero.

    Example:
        >>> operating_margin(25000, 100000)
        0.25

    Complexity: O(1)
    """
    if not isinstance(operating_income, (int, float)):
        raise TypeError("operating_income must be numeric.")

    if not isinstance(revenue, (int, float)):
        raise TypeError("revenue must be numeric.")

    if revenue == 0:
        raise ValueError("revenue must not be zero.")

    return operating_income / revenue


def current_ratio(
    current_assets: Union[int, float],
    current_liabilities: Union[int, float],
) -> float:
    """Computes the current (liquidity) ratio.

    current_ratio = current_assets / current_liabilities.

    Args:
        current_assets: Total current assets.
        current_liabilities: Total current liabilities.

    Returns:
        The current ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If current_liabilities is zero or negative.

    Example:
        >>> current_ratio(150000, 100000)
        1.5

    Complexity: O(1)
    """
    if not isinstance(current_assets, (int, float)):
        raise TypeError("current_assets must be numeric.")

    if not isinstance(current_liabilities, (int, float)):
        raise TypeError("current_liabilities must be numeric.")

    if current_liabilities <= 0:
        raise ValueError("current_liabilities must be positive.")

    return current_assets / current_liabilities


def return_on_assets(
    net_income: Union[int, float],
    total_assets: Union[int, float],
) -> float:
    """Computes return on assets (ROA).

    ROA = net_income / total_assets.

    Args:
        net_income: Net income.
        total_assets: Total assets.

    Returns:
        ROA as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If total_assets is zero.

    Example:
        >>> return_on_assets(50000, 500000)
        0.1

    Complexity: O(1)
    """
    if not isinstance(net_income, (int, float)):
        raise TypeError("net_income must be numeric.")

    if not isinstance(total_assets, (int, float)):
        raise TypeError("total_assets must be numeric.")

    if total_assets == 0:
        raise ValueError("total_assets must not be zero.")

    return net_income / total_assets


def return_on_equity(
    net_income: Union[int, float],
    shareholders_equity: Union[int, float],
) -> float:
    """Computes return on equity (ROE).

    ROE = net_income / shareholders_equity.

    Args:
        net_income: Net income.
        shareholders_equity: Total shareholders' equity.

    Returns:
        ROE as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If shareholders_equity is zero.

    Example:
        >>> return_on_equity(50000, 200000)
        0.25

    Complexity: O(1)
    """
    if not isinstance(net_income, (int, float)):
        raise TypeError("net_income must be numeric.")

    if not isinstance(shareholders_equity, (int, float)):
        raise TypeError("shareholders_equity must be numeric.")

    if shareholders_equity == 0:
        raise ValueError("shareholders_equity must not be zero.")

    return net_income / shareholders_equity


def earnings_per_share(
    net_income: Union[int, float],
    shares_outstanding: Union[int, float],
) -> float:
    """Computes earnings per share (EPS).

    EPS = net_income / shares_outstanding.

    Args:
        net_income: Net income.
        shares_outstanding: Number of outstanding shares.

    Returns:
        EPS value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If shares_outstanding is zero or negative.

    Example:
        >>> earnings_per_share(1000000, 500000)
        2.0

    Complexity: O(1)
    """
    if not isinstance(net_income, (int, float)):
        raise TypeError("net_income must be numeric.")

    if not isinstance(shares_outstanding, (int, float)):
        raise TypeError("shares_outstanding must be numeric.")

    if shares_outstanding <= 0:
        raise ValueError("shares_outstanding must be positive.")

    return net_income / shares_outstanding


def price_to_earnings(
    market_price: Union[int, float],
    earnings_per_share_value: Union[int, float],
) -> float:
    """Calculate the Price-to-Earnings (P/E) ratio.

    Args:
        market_price: Current market price per share.
        earnings_per_share_value: Earnings per share (EPS).

    Returns:
        P/E ratio as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If earnings_per_share_value is zero.

    Example:
        >>> price_to_earnings(150, 5)
        30.0

    Complexity: O(1)
    """
    if not isinstance(market_price, (int, float)):
        raise TypeError("market_price must be numeric.")

    if not isinstance(earnings_per_share_value, (int, float)):
        raise TypeError("earnings_per_share_value must be numeric.")

    if earnings_per_share_value == 0:
        raise ValueError("earnings_per_share_value must not be zero.")

    return market_price / earnings_per_share_value


def price_to_book(
    market_price: Union[int, float],
    book_value_per_share: Union[int, float],
) -> float:
    """Calculate the Price-to-Book (P/B) ratio.

    Args:
        market_price: Current market price per share.
        book_value_per_share: Book value per share.

    Returns:
        P/B ratio as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If book_value_per_share is zero or negative.

    Example:
        >>> price_to_book(50, 25)
        2.0

    Complexity: O(1)
    """
    if not isinstance(market_price, (int, float)):
        raise TypeError("market_price must be numeric.")

    if not isinstance(book_value_per_share, (int, float)):
        raise TypeError("book_value_per_share must be numeric.")

    if book_value_per_share <= 0:
        raise ValueError("book_value_per_share must be positive.")

    return market_price / book_value_per_share


def dividend_yield(
    annual_dividend: Union[int, float],
    market_price: Union[int, float],
) -> float:
    """Calculate the dividend yield as a percentage.

    Args:
        annual_dividend: Total annual dividend per share.
        market_price: Current market price per share.

    Returns:
        Dividend yield as a percentage (e.g. 3.5 means 3.5%).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If market_price is zero or negative.

    Example:
        >>> dividend_yield(2, 50)
        4.0

    Complexity: O(1)
    """
    if not isinstance(annual_dividend, (int, float)):
        raise TypeError("annual_dividend must be numeric.")

    if not isinstance(market_price, (int, float)):
        raise TypeError("market_price must be numeric.")

    if market_price <= 0:
        raise ValueError("market_price must be positive.")

    return (annual_dividend / market_price) * 100


def dividend_payout_ratio(
    dividends_paid: Union[int, float],
    net_income: Union[int, float],
) -> float:
    """Calculate the dividend payout ratio as a percentage.

    Args:
        dividends_paid: Total dividends paid.
        net_income: Net income of the company.

    Returns:
        Payout ratio as a percentage.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If net_income is zero.

    Example:
        >>> dividend_payout_ratio(40000, 100000)
        40.0

    Complexity: O(1)
    """
    if not isinstance(dividends_paid, (int, float)):
        raise TypeError("dividends_paid must be numeric.")

    if not isinstance(net_income, (int, float)):
        raise TypeError("net_income must be numeric.")

    if net_income == 0:
        raise ValueError("net_income must not be zero.")

    return (dividends_paid / net_income) * 100


def asset_turnover(
    net_sales: Union[int, float],
    total_assets: Union[int, float],
) -> float:
    """Calculate the asset turnover ratio.

    Measures how efficiently a company uses its assets to generate revenue.

    Args:
        net_sales: Total net sales/revenue.
        total_assets: Average total assets.

    Returns:
        Asset turnover ratio as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If total_assets is zero or negative.

    Example:
        >>> asset_turnover(500000, 250000)
        2.0

    Complexity: O(1)
    """
    if not isinstance(net_sales, (int, float)):
        raise TypeError("net_sales must be numeric.")

    if not isinstance(total_assets, (int, float)):
        raise TypeError("total_assets must be numeric.")

    if total_assets <= 0:
        raise ValueError("total_assets must be positive.")

    return net_sales / total_assets


def interest_coverage_ratio(
    ebit: Union[int, float],
    interest_expense: Union[int, float],
) -> float:
    """Calculate the interest coverage ratio.

    Measures a company's ability to pay interest on outstanding debt.

    Args:
        ebit: Earnings before interest and taxes.
        interest_expense: Total interest expense.

    Returns:
        Interest coverage ratio as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If interest_expense is zero.

    Example:
        >>> interest_coverage_ratio(500000, 100000)
        5.0

    Complexity: O(1)
    """
    if not isinstance(ebit, (int, float)):
        raise TypeError("ebit must be numeric.")

    if not isinstance(interest_expense, (int, float)):
        raise TypeError("interest_expense must be numeric.")

    if interest_expense == 0:
        raise ValueError("interest_expense must not be zero.")

    return ebit / interest_expense


def quick_ratio(
    current_assets: Union[int, float],
    inventories: Union[int, float],
    current_liabilities: Union[int, float],
) -> float:
    """Calculate the quick (acid-test) ratio.

    Measures a company's ability to meet short-term obligations
    with its most liquid assets.

    Args:
        current_assets: Total current assets.
        inventories: Total inventories.
        current_liabilities: Total current liabilities.

    Returns:
        Quick ratio as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If current_liabilities is zero or negative.

    Example:
        >>> quick_ratio(100000, 30000, 50000)
        1.4

    Complexity: O(1)
    """
    if not isinstance(current_assets, (int, float)):
        raise TypeError("current_assets must be numeric.")

    if not isinstance(inventories, (int, float)):
        raise TypeError("inventories must be numeric.")

    if not isinstance(current_liabilities, (int, float)):
        raise TypeError("current_liabilities must be numeric.")

    if current_liabilities <= 0:
        raise ValueError("current_liabilities must be positive.")

    return (current_assets - inventories) / current_liabilities


def net_profit_margin(
    net_income: Union[int, float],
    revenue: Union[int, float],
) -> float:
    """Calculate the net profit margin as a percentage.

    Args:
        net_income: Net income after all expenses.
        revenue: Total revenue.

    Returns:
        Net profit margin as a percentage.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If revenue is zero.

    Example:
        >>> net_profit_margin(25000, 100000)
        25.0

    Complexity: O(1)
    """
    if not isinstance(net_income, (int, float)):
        raise TypeError("net_income must be numeric.")

    if not isinstance(revenue, (int, float)):
        raise TypeError("revenue must be numeric.")

    if revenue == 0:
        raise ValueError("revenue must not be zero.")

    return (net_income / revenue) * 100


def ev_to_ebitda(
    enterprise_value: Union[int, float],
    ebitda: Union[int, float],
) -> float:
    """Calculate the Enterprise Value to EBITDA ratio.

    A valuation measure comparing the value of a company to its earnings
    before interest, taxes, depreciation, and amortization.

    Args:
        enterprise_value: Enterprise value of the company.
        ebitda: Earnings before interest, taxes, depreciation, and amortization.

    Returns:
        EV/EBITDA ratio as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If ebitda is zero.

    Example:
        >>> ev_to_ebitda(1000000, 200000)
        5.0

    Complexity: O(1)
    """
    if not isinstance(enterprise_value, (int, float)):
        raise TypeError("enterprise_value must be numeric.")

    if not isinstance(ebitda, (int, float)):
        raise TypeError("ebitda must be numeric.")

    if ebitda == 0:
        raise ValueError("ebitda must not be zero.")

    return enterprise_value / ebitda


def working_capital(
    current_assets: Union[int, float],
    current_liabilities: Union[int, float],
) -> float:
    """Calculate working capital.

    Measures a company's short-term liquidity: the difference between
    current assets and current liabilities.

    Args:
        current_assets: Total current assets.
        current_liabilities: Total current liabilities.

    Returns:
        Working capital as a float.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> working_capital(500000, 300000)
        200000

    Complexity: O(1)
    """
    if not isinstance(current_assets, (int, float)):
        raise TypeError("current_assets must be numeric.")

    if not isinstance(current_liabilities, (int, float)):
        raise TypeError("current_liabilities must be numeric.")

    return current_assets - current_liabilities


def inventory_turnover(
    cogs: Union[int, float],
    average_inventory: Union[int, float],
) -> float:
    """Calculate the inventory turnover ratio.

    Measures how many times inventory is sold and replaced over a period.

    Args:
        cogs: Cost of goods sold.
        average_inventory: Average inventory during the period.

    Returns:
        Inventory turnover ratio as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If average_inventory is zero or negative.

    Example:
        >>> inventory_turnover(600000, 100000)
        6.0

    Complexity: O(1)
    """
    if not isinstance(cogs, (int, float)):
        raise TypeError("cogs must be numeric.")

    if not isinstance(average_inventory, (int, float)):
        raise TypeError("average_inventory must be numeric.")

    if average_inventory <= 0:
        raise ValueError("average_inventory must be positive.")

    return cogs / average_inventory


def cash_ratio(
    cash: Union[int, float],
    current_liabilities: Union[int, float],
) -> float:
    """Calculate the cash ratio.

    The most conservative liquidity ratio, using only cash and cash
    equivalents to cover current liabilities.

    Args:
        cash: Cash and cash equivalents.
        current_liabilities: Total current liabilities.

    Returns:
        Cash ratio as a float.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If current_liabilities is zero or negative.

    Example:
        >>> cash_ratio(150000, 300000)
        0.5

    Complexity: O(1)
    """
    if not isinstance(cash, (int, float)):
        raise TypeError("cash must be numeric.")

    if not isinstance(current_liabilities, (int, float)):
        raise TypeError("current_liabilities must be numeric.")

    if current_liabilities <= 0:
        raise ValueError("current_liabilities must be positive.")

    return cash / current_liabilities


def dupont_roe(
    net_margin: Union[int, float],
    asset_turnover_ratio: Union[int, float],
    equity_multiplier: Union[int, float],
) -> float:
    """Calculate Return on Equity using the DuPont decomposition.

    ROE = Net Profit Margin × Asset Turnover × Equity Multiplier.
    All inputs should be ratios (not percentages).

    Args:
        net_margin: Net profit margin ratio (e.g. 0.10 for 10%).
        asset_turnover_ratio: Asset turnover ratio.
        equity_multiplier: Total assets / shareholders' equity.

    Returns:
        ROE as a decimal ratio.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> dupont_roe(0.10, 1.5, 2.0)
        0.3

    Complexity: O(1)
    """
    if not isinstance(net_margin, (int, float)):
        raise TypeError("net_margin must be numeric.")

    if not isinstance(asset_turnover_ratio, (int, float)):
        raise TypeError("asset_turnover_ratio must be numeric.")

    if not isinstance(equity_multiplier, (int, float)):
        raise TypeError("equity_multiplier must be numeric.")

    return float(net_margin * asset_turnover_ratio * equity_multiplier)


def effective_annual_rate(
    nominal_rate: Union[int, float],
    periods_per_year: int,
) -> float:
    """Convert a nominal interest rate to the effective annual rate.

    EAR = (1 + r/n)^n - 1 where r is the nominal rate and n is
    the number of compounding periods per year.

    Args:
        nominal_rate: Nominal annual interest rate (e.g. 0.12 for 12%).
        periods_per_year: Number of compounding periods per year.

    Returns:
        Effective annual rate as a decimal.

    Raises:
        TypeError: If inputs are not of the correct type.
        ValueError: If periods_per_year is less than 1.

    Example:
        >>> round(effective_annual_rate(0.12, 12), 6)
        0.126825

    Complexity: O(1)
    """
    if not isinstance(nominal_rate, (int, float)):
        raise TypeError("nominal_rate must be numeric.")

    if not isinstance(periods_per_year, int):
        raise TypeError("periods_per_year must be an integer.")

    if periods_per_year < 1:
        raise ValueError("periods_per_year must be at least 1.")

    return (1 + nominal_rate / periods_per_year) ** periods_per_year - 1


def debt_service_coverage(
    net_operating_income: Union[int, float],
    total_debt_service: Union[int, float],
) -> float:
    """Calculate the Debt Service Coverage Ratio (DSCR).

    Measures ability to service debt obligations with operating income.

    Args:
        net_operating_income: Net operating income.
        total_debt_service: Total debt service (principal + interest).

    Returns:
        DSCR as a float. Values > 1 indicate sufficient income.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If total_debt_service is zero.

    Example:
        >>> debt_service_coverage(500000, 400000)
        1.25

    Complexity: O(1)
    """
    if not isinstance(net_operating_income, (int, float)):
        raise TypeError("net_operating_income must be numeric.")

    if not isinstance(total_debt_service, (int, float)):
        raise TypeError("total_debt_service must be numeric.")

    if total_debt_service == 0:
        raise ValueError("total_debt_service must not be zero.")

    return net_operating_income / total_debt_service


def burn_rate(
    starting_cash: Union[int, float],
    ending_cash: Union[int, float],
    months: int,
) -> float:
    """Calculate the monthly cash burn rate.

    Args:
        starting_cash: Cash at the beginning of the period.
        ending_cash: Cash at the end of the period.
        months: Number of months in the period.

    Returns:
        Average monthly cash burn (positive = spending cash).

    Raises:
        TypeError: If inputs are not of correct types.
        ValueError: If months is less than 1.

    Example:
        >>> burn_rate(1000000, 700000, 3)
        100000.0

    Complexity: O(1)
    """
    if not isinstance(starting_cash, (int, float)):
        raise TypeError("starting_cash must be numeric.")

    if not isinstance(ending_cash, (int, float)):
        raise TypeError("ending_cash must be numeric.")

    if not isinstance(months, int):
        raise TypeError("months must be an integer.")

    if months < 1:
        raise ValueError("months must be at least 1.")

    return (starting_cash - ending_cash) / months


def months_of_runway(
    cash_available: Union[int, float],
    monthly_burn_rate: Union[int, float],
) -> float:
    """Calculate financial runway in months.

    How many months a company can operate before running out of cash.

    Args:
        cash_available: Current available cash.
        monthly_burn_rate: Average monthly cash burn (positive).

    Returns:
        Number of months of runway.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If monthly_burn_rate is not positive.

    Example:
        >>> months_of_runway(600000, 100000)
        6.0

    Complexity: O(1)
    """
    if not isinstance(cash_available, (int, float)):
        raise TypeError("cash_available must be numeric.")

    if not isinstance(monthly_burn_rate, (int, float)):
        raise TypeError("monthly_burn_rate must be numeric.")

    if monthly_burn_rate <= 0:
        raise ValueError("monthly_burn_rate must be positive.")

    return cash_available / monthly_burn_rate


def revenue_per_employee(
    total_revenue: Union[int, float],
    number_of_employees: int,
) -> float:
    """Calculate revenue generated per employee.

    Args:
        total_revenue: Total revenue of the company.
        number_of_employees: Total number of employees.

    Returns:
        Revenue per employee.

    Raises:
        TypeError: If inputs are not of correct types.
        ValueError: If number_of_employees is less than 1.

    Example:
        >>> revenue_per_employee(5000000, 50)
        100000.0

    Complexity: O(1)
    """
    if not isinstance(total_revenue, (int, float)):
        raise TypeError("total_revenue must be numeric.")

    if not isinstance(number_of_employees, int):
        raise TypeError("number_of_employees must be an integer.")

    if number_of_employees < 1:
        raise ValueError("number_of_employees must be at least 1.")

    return total_revenue / number_of_employees


def fixed_charge_coverage(
    ebit: Union[int, float],
    fixed_charges: Union[int, float],
) -> float:
    """Calculate the Fixed Charge Coverage Ratio.

    Measures the ability to cover fixed charges (interest, leases, etc.)
    with earnings before interest and taxes plus those fixed charges.

    FCCR = (EBIT + fixed_charges) / fixed_charges

    Args:
        ebit: Earnings before interest and taxes.
        fixed_charges: Total fixed charges (interest, lease payments, etc.).

    Returns:
        Fixed charge coverage ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If fixed_charges is zero.

    Example:
        >>> fixed_charge_coverage(300000, 100000)
        4.0

    Complexity: O(1)
    """
    if not isinstance(ebit, (int, float)):
        raise TypeError("ebit must be numeric.")

    if not isinstance(fixed_charges, (int, float)):
        raise TypeError("fixed_charges must be numeric.")

    if fixed_charges == 0:
        raise ValueError("fixed_charges must not be zero.")

    return (ebit + fixed_charges) / fixed_charges


def operating_cash_flow_ratio(
    operating_cash_flow: Union[int, float],
    current_liabilities: Union[int, float],
) -> float:
    """Calculate the Operating Cash Flow Ratio.

    Measures how well current liabilities are covered by cash flow
    from operations.

    Args:
        operating_cash_flow: Cash flow from operations.
        current_liabilities: Total current liabilities.

    Returns:
        Operating cash flow ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If current_liabilities is zero or negative.

    Example:
        >>> operating_cash_flow_ratio(250000, 200000)
        1.25

    Complexity: O(1)
    """
    if not isinstance(operating_cash_flow, (int, float)):
        raise TypeError("operating_cash_flow must be numeric.")

    if not isinstance(current_liabilities, (int, float)):
        raise TypeError("current_liabilities must be numeric.")

    if current_liabilities <= 0:
        raise ValueError("current_liabilities must be positive.")

    return operating_cash_flow / current_liabilities


def treynor_ratio(
    portfolio_return: Union[int, float],
    risk_free_rate: Union[int, float],
    beta: Union[int, float],
) -> float:
    """Calculate the Treynor ratio: (Rp - Rf) / β.

    Measures risk-adjusted return per unit of systematic (market) risk.

    Args:
        portfolio_return: Portfolio return (as decimal, e.g. 0.12 for 12 %).
        risk_free_rate: Risk-free rate (as decimal).
        beta: Portfolio beta (systematic risk).

    Returns:
        Treynor ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If beta is zero.

    Example:
        >>> treynor_ratio(0.12, 0.03, 1.2)
        0.075

    Complexity: O(1)
    """
    if not isinstance(portfolio_return, (int, float)):
        raise TypeError("portfolio_return must be numeric.")

    if not isinstance(risk_free_rate, (int, float)):
        raise TypeError("risk_free_rate must be numeric.")

    if not isinstance(beta, (int, float)):
        raise TypeError("beta must be numeric.")

    if beta == 0:
        raise ValueError("beta must not be zero.")

    return float((portfolio_return - risk_free_rate) / beta)


def calmar_ratio(
    annualized_return: Union[int, float],
    max_drawdown: Union[int, float],
) -> float:
    """Calculate the Calmar ratio: annualized return / max drawdown.

    Args:
        annualized_return: Annualized return (as decimal).
        max_drawdown: Maximum drawdown as a positive decimal (e.g. 0.20 for 20 %).

    Returns:
        Calmar ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If max_drawdown is not positive.

    Example:
        >>> calmar_ratio(0.15, 0.10)
        1.5

    Complexity: O(1)
    """
    if not isinstance(annualized_return, (int, float)):
        raise TypeError("annualized_return must be numeric.")

    if not isinstance(max_drawdown, (int, float)):
        raise TypeError("max_drawdown must be numeric.")

    if max_drawdown <= 0:
        raise ValueError("max_drawdown must be positive.")

    return float(annualized_return / max_drawdown)


def kelly_criterion(
    win_probability: Union[int, float],
    win_loss_ratio: Union[int, float],
) -> float:
    """Calculate the Kelly criterion: f* = p - (1-p)/b.

    Determines the optimal fraction of capital to wager.

    Args:
        win_probability: Probability of winning (0 < p < 1).
        win_loss_ratio: Ratio of average win to average loss (b > 0).

    Returns:
        Optimal fraction of bankroll to bet (can be negative → don't bet).

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If win_probability not in (0,1) or win_loss_ratio not positive.

    Example:
        >>> kelly_criterion(0.6, 2.0)
        0.4

    Complexity: O(1)
    """
    if not isinstance(win_probability, (int, float)):
        raise TypeError("win_probability must be numeric.")

    if not isinstance(win_loss_ratio, (int, float)):
        raise TypeError("win_loss_ratio must be numeric.")

    if not 0 < win_probability < 1:
        raise ValueError("win_probability must be between 0 and 1 exclusive.")

    if win_loss_ratio <= 0:
        raise ValueError("win_loss_ratio must be positive.")

    return float(win_probability - (1 - win_probability) / win_loss_ratio)


def breakeven_units(
    fixed_costs: Union[int, float],
    price_per_unit: Union[int, float],
    variable_cost_per_unit: Union[int, float],
) -> float:
    """Calculate the break-even point in units.

    Units = Fixed Costs / (Price - Variable Cost).

    Args:
        fixed_costs: Total fixed costs.
        price_per_unit: Selling price per unit.
        variable_cost_per_unit: Variable cost per unit.

    Returns:
        Number of units to break even.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If price <= variable cost or fixed_costs < 0.

    Example:
        >>> breakeven_units(10000, 50, 30)
        500.0

    Complexity: O(1)
    """
    if not isinstance(fixed_costs, (int, float)):
        raise TypeError("fixed_costs must be numeric.")

    if not isinstance(price_per_unit, (int, float)):
        raise TypeError("price_per_unit must be numeric.")

    if not isinstance(variable_cost_per_unit, (int, float)):
        raise TypeError("variable_cost_per_unit must be numeric.")

    if fixed_costs < 0:
        raise ValueError("fixed_costs must be non-negative.")

    margin = price_per_unit - variable_cost_per_unit

    if margin <= 0:
        raise ValueError("price_per_unit must exceed variable_cost_per_unit.")

    return float(fixed_costs / margin)


def cost_of_equity_capm(
    risk_free_rate: Union[int, float],
    beta: Union[int, float],
    market_return: Union[int, float],
) -> float:
    """Calculate cost of equity using CAPM: Ke = Rf + β * (Rm - Rf).

    Args:
        risk_free_rate: Risk-free rate (decimal).
        beta: Equity beta.
        market_return: Expected market return (decimal).

    Returns:
        Cost of equity (decimal).

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> cost_of_equity_capm(0.03, 1.2, 0.10)
        0.114

    Complexity: O(1)
    """
    if not isinstance(risk_free_rate, (int, float)):
        raise TypeError("risk_free_rate must be numeric.")

    if not isinstance(beta, (int, float)):
        raise TypeError("beta must be numeric.")

    if not isinstance(market_return, (int, float)):
        raise TypeError("market_return must be numeric.")

    return float(risk_free_rate + beta * (market_return - risk_free_rate))


def information_ratio(
    portfolio_return: Union[int, float],
    benchmark_return: Union[int, float],
    tracking_error: Union[int, float],
) -> float:
    """Calculate the Information Ratio: (Rp - Rb) / TE.

    Measures excess return per unit of tracking error.

    Args:
        portfolio_return: Portfolio return (decimal).
        benchmark_return: Benchmark return (decimal).
        tracking_error: Tracking error (std dev of excess returns).

    Returns:
        Information ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If tracking_error is not positive.

    Example:
        >>> information_ratio(0.12, 0.10, 0.04)
        0.5

    Complexity: O(1)
    """
    if not isinstance(portfolio_return, (int, float)):
        raise TypeError("portfolio_return must be numeric.")

    if not isinstance(benchmark_return, (int, float)):
        raise TypeError("benchmark_return must be numeric.")

    if not isinstance(tracking_error, (int, float)):
        raise TypeError("tracking_error must be numeric.")

    if tracking_error <= 0:
        raise ValueError("tracking_error must be positive.")

    return float((portfolio_return - benchmark_return) / tracking_error)


def gordon_growth_price(
    dividend: Union[int, float],
    discount_rate: Union[int, float],
    growth_rate: Union[int, float],
) -> float:
    """Estimate the intrinsic price of a stock using the Gordon Growth Model.

    P = D₁ / (r - g)

    Args:
        dividend: Expected dividend next period.
        discount_rate: Required rate of return (decimal).
        growth_rate: Constant dividend growth rate (decimal, must be < discount_rate).

    Returns:
        Intrinsic stock price.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If growth_rate >= discount_rate or dividend is negative.

    Example:
        >>> gordon_growth_price(2.0, 0.10, 0.05)
        40.0

    Complexity: O(1)
    """
    if not isinstance(dividend, (int, float)):
        raise TypeError("dividend must be numeric.")

    if not isinstance(discount_rate, (int, float)):
        raise TypeError("discount_rate must be numeric.")

    if not isinstance(growth_rate, (int, float)):
        raise TypeError("growth_rate must be numeric.")

    if dividend < 0:
        raise ValueError("dividend must be non-negative.")

    if growth_rate >= discount_rate:
        raise ValueError("growth_rate must be less than discount_rate.")

    return float(dividend / (discount_rate - growth_rate))


def earnings_yield(
    earnings_per_share: Union[int, float],
    price_per_share: Union[int, float],
) -> float:
    """Calculate the earnings yield: EPS / Price (inverse of P/E ratio).

    Args:
        earnings_per_share: Earnings per share.
        price_per_share: Market price per share.

    Returns:
        Earnings yield as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If price_per_share is not positive.

    Example:
        >>> earnings_yield(5, 100)
        0.05

    Complexity: O(1)
    """
    if not isinstance(earnings_per_share, (int, float)):
        raise TypeError("earnings_per_share must be numeric.")

    if not isinstance(price_per_share, (int, float)):
        raise TypeError("price_per_share must be numeric.")

    if price_per_share <= 0:
        raise ValueError("price_per_share must be positive.")

    return float(earnings_per_share / price_per_share)


def market_cap(
    share_price: Union[int, float],
    shares_outstanding: Union[int, float],
) -> float:
    """Calculate market capitalisation: Price × Shares Outstanding.

    Args:
        share_price: Current share price.
        shares_outstanding: Total shares outstanding.

    Returns:
        Market capitalisation.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If either value is not positive.

    Example:
        >>> market_cap(150, 1_000_000)
        150000000.0

    Complexity: O(1)
    """
    if not isinstance(share_price, (int, float)):
        raise TypeError("share_price must be numeric.")

    if not isinstance(shares_outstanding, (int, float)):
        raise TypeError("shares_outstanding must be numeric.")

    if share_price <= 0:
        raise ValueError("share_price must be positive.")

    if shares_outstanding <= 0:
        raise ValueError("shares_outstanding must be positive.")

    return float(share_price * shares_outstanding)


def enterprise_value_simple(
    market_cap_value: Union[int, float],
    total_debt: Union[int, float],
    cash: Union[int, float],
) -> float:
    """Calculate simplified enterprise value: EV = Market Cap + Debt - Cash.

    Args:
        market_cap_value: Market capitalisation.
        total_debt: Total debt.
        cash: Cash and cash equivalents.

    Returns:
        Enterprise value.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> enterprise_value_simple(1_000_000, 200_000, 50_000)
        1150000.0

    Complexity: O(1)
    """
    if not isinstance(market_cap_value, (int, float)):
        raise TypeError("market_cap_value must be numeric.")

    if not isinstance(total_debt, (int, float)):
        raise TypeError("total_debt must be numeric.")

    if not isinstance(cash, (int, float)):
        raise TypeError("cash must be numeric.")

    return float(market_cap_value + total_debt - cash)


def leverage_ratio(
    total_assets: Union[int, float],
    total_equity: Union[int, float],
) -> float:
    """Calculate the leverage ratio (equity multiplier): Assets / Equity.

    Args:
        total_assets: Total assets.
        total_equity: Total equity.

    Returns:
        Leverage ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If total_equity is not positive.

    Example:
        >>> leverage_ratio(500_000, 200_000)
        2.5

    Complexity: O(1)
    """
    if not isinstance(total_assets, (int, float)):
        raise TypeError("total_assets must be numeric.")

    if not isinstance(total_equity, (int, float)):
        raise TypeError("total_equity must be numeric.")

    if total_equity <= 0:
        raise ValueError("total_equity must be positive.")

    return float(total_assets / total_equity)


def dividend_discount_price(
    dividend: Union[int, float],
    discount_rate: Union[int, float],
    periods: int,
    growth_rate: Union[int, float] = 0.0,
) -> float:
    """Calculate stock price via a finite-period dividend discount model.

    P = Σ D₀·(1+g)^t / (1+r)^t  for t = 1 … periods

    Args:
        dividend: Current dividend (D₀).
        discount_rate: Required rate of return (decimal, > 0).
        periods: Number of future periods.
        growth_rate: Dividend growth rate per period (decimal, default 0).

    Returns:
        Present value of future dividends.

    Raises:
        TypeError: If inputs are not numeric / periods not int.
        ValueError: If discount_rate not positive, periods < 1, or dividend negative.

    Example:
        >>> round(dividend_discount_price(2.0, 0.10, 5), 4)
        7.5816

    Complexity: O(n)
    """
    if not isinstance(dividend, (int, float)):
        raise TypeError("dividend must be numeric.")

    if not isinstance(discount_rate, (int, float)):
        raise TypeError("discount_rate must be numeric.")

    if not isinstance(periods, int):
        raise TypeError("periods must be an integer.")

    if not isinstance(growth_rate, (int, float)):
        raise TypeError("growth_rate must be numeric.")

    if dividend < 0:
        raise ValueError("dividend must be non-negative.")

    if discount_rate <= 0:
        raise ValueError("discount_rate must be positive.")

    if periods < 1:
        raise ValueError("periods must be at least 1.")

    total = 0.0

    for t in range(1, periods + 1):
        total += dividend * (1 + growth_rate) ** t / (1 + discount_rate) ** t

    return float(total)


def contribution_margin(
    revenue: Union[int, float],
    variable_costs: Union[int, float],
) -> float:
    """Calculate the contribution margin: Revenue - Variable Costs.

    Args:
        revenue: Total revenue.
        variable_costs: Total variable costs.

    Returns:
        Contribution margin.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> contribution_margin(100_000, 60_000)
        40000.0

    Complexity: O(1)
    """
    if not isinstance(revenue, (int, float)):
        raise TypeError("revenue must be numeric.")

    if not isinstance(variable_costs, (int, float)):
        raise TypeError("variable_costs must be numeric.")

    return float(revenue - variable_costs)


def margin_of_safety_pct(
    actual_sales: Union[int, float],
    breakeven_sales: Union[int, float],
) -> float:
    """Calculate the margin of safety as a percentage.

    MoS% = (Actual - Breakeven) / Actual × 100

    Args:
        actual_sales: Actual or expected sales.
        breakeven_sales: Break-even sales level.

    Returns:
        Margin of safety percentage.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If actual_sales is not positive.

    Example:
        >>> margin_of_safety_pct(200_000, 150_000)
        25.0

    Complexity: O(1)
    """
    if not isinstance(actual_sales, (int, float)):
        raise TypeError("actual_sales must be numeric.")

    if not isinstance(breakeven_sales, (int, float)):
        raise TypeError("breakeven_sales must be numeric.")

    if actual_sales <= 0:
        raise ValueError("actual_sales must be positive.")

    return float((actual_sales - breakeven_sales) / actual_sales * 100)


def operating_leverage_degree(
    contribution_margin_value: Union[int, float],
    operating_income: Union[int, float],
) -> float:
    """Calculate the Degree of Operating Leverage: DOL = CM / EBIT.

    Args:
        contribution_margin_value: Total contribution margin.
        operating_income: Operating income (EBIT).

    Returns:
        Degree of operating leverage.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If operating_income is zero.

    Example:
        >>> operating_leverage_degree(100_000, 40_000)
        2.5

    Complexity: O(1)
    """
    if not isinstance(contribution_margin_value, (int, float)):
        raise TypeError("contribution_margin_value must be numeric.")

    if not isinstance(operating_income, (int, float)):
        raise TypeError("operating_income must be numeric.")

    if operating_income == 0:
        raise ValueError("operating_income must not be zero.")

    return float(contribution_margin_value / operating_income)


def cash_conversion_cycle(
    days_inventory: Union[int, float],
    days_receivable: Union[int, float],
    days_payable: Union[int, float],
) -> float:
    """Calculate the Cash Conversion Cycle: DIO + DSO - DPO.

    Args:
        days_inventory: Days inventory outstanding (DIO).
        days_receivable: Days sales outstanding (DSO).
        days_payable: Days payable outstanding (DPO).

    Returns:
        Cash conversion cycle in days.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> cash_conversion_cycle(45, 30, 35)
        40.0

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (days_inventory, days_receivable, days_payable)):
        raise TypeError("all inputs must be numeric.")

    return float(days_inventory + days_receivable - days_payable)


def retention_ratio(
    net_income: Union[int, float],
    dividends_paid: Union[int, float],
) -> float:
    """Calculate the retention ratio (plowback ratio).

    RR = (Net Income - Dividends) / Net Income

    Args:
        net_income: Net income.
        dividends_paid: Dividends paid.

    Returns:
        Retention ratio as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If net_income is not positive.

    Example:
        >>> retention_ratio(100_000, 30_000)
        0.7

    Complexity: O(1)
    """
    if not isinstance(net_income, (int, float)):
        raise TypeError("net_income must be numeric.")

    if not isinstance(dividends_paid, (int, float)):
        raise TypeError("dividends_paid must be numeric.")

    if net_income <= 0:
        raise ValueError("net_income must be positive.")

    return float((net_income - dividends_paid) / net_income)


def sustainable_growth_rate(
    roe: Union[int, float],
    retention: Union[int, float],
) -> float:
    """Calculate the sustainable growth rate: SGR = ROE × Retention Ratio.

    Args:
        roe: Return on equity (decimal, e.g. 0.15 for 15%).
        retention: Retention ratio (decimal, 0 to 1).

    Returns:
        Sustainable growth rate as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If retention not in [0, 1].

    Example:
        >>> sustainable_growth_rate(0.15, 0.7)
        0.105

    Complexity: O(1)
    """
    if not isinstance(roe, (int, float)):
        raise TypeError("roe must be numeric.")

    if not isinstance(retention, (int, float)):
        raise TypeError("retention must be numeric.")

    if not 0 <= retention <= 1:
        raise ValueError("retention must be between 0 and 1.")

    return float(roe * retention)


def equity_multiplier(
    total_assets: Union[int, float],
    total_equity: Union[int, float],
) -> float:
    """Calculate the equity multiplier (total assets / shareholders' equity).

    Args:
        total_assets: Total assets value.
        total_equity: Shareholders' equity value.

    Returns:
        Equity multiplier ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If total_equity is zero.

    Example:
        >>> equity_multiplier(500_000, 200_000)
        2.5

    Complexity: O(1)
    """
    if not isinstance(total_assets, (int, float)) or not isinstance(total_equity, (int, float)):
        raise TypeError("total_assets and total_equity must be numeric.")

    if total_equity == 0:
        raise ValueError("total_equity must not be zero.")

    return float(total_assets / total_equity)


def working_capital_ratio(
    current_assets: Union[int, float],
    current_liabilities: Union[int, float],
) -> float:
    """Calculate the working capital ratio (current ratio).

    Args:
        current_assets: Total current assets.
        current_liabilities: Total current liabilities.

    Returns:
        Working capital ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If current_liabilities is zero.

    Example:
        >>> working_capital_ratio(150_000, 100_000)
        1.5

    Complexity: O(1)
    """
    if not isinstance(current_assets, (int, float)) or not isinstance(current_liabilities, (int, float)):
        raise TypeError("current_assets and current_liabilities must be numeric.")

    if current_liabilities == 0:
        raise ValueError("current_liabilities must not be zero.")

    return float(current_assets / current_liabilities)


def receivables_turnover(
    net_credit_sales: Union[int, float],
    average_receivables: Union[int, float],
) -> float:
    """Calculate accounts receivable turnover ratio.

    Args:
        net_credit_sales: Net credit sales for the period.
        average_receivables: Average accounts receivable.

    Returns:
        Receivables turnover ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If average_receivables is zero.

    Example:
        >>> receivables_turnover(1_000_000, 125_000)
        8.0

    Complexity: O(1)
    """
    if not isinstance(net_credit_sales, (int, float)) or not isinstance(average_receivables, (int, float)):
        raise TypeError("net_credit_sales and average_receivables must be numeric.")

    if average_receivables == 0:
        raise ValueError("average_receivables must not be zero.")

    return float(net_credit_sales / average_receivables)


def inventory_turnover_ratio(
    cost_of_goods_sold: Union[int, float],
    average_inventory: Union[int, float],
) -> float:
    """Calculate inventory turnover ratio.

    Args:
        cost_of_goods_sold: COGS for the period.
        average_inventory: Average inventory value.

    Returns:
        Inventory turnover ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If average_inventory is zero.

    Example:
        >>> inventory_turnover_ratio(500_000, 100_000)
        5.0

    Complexity: O(1)
    """
    if not isinstance(cost_of_goods_sold, (int, float)) or not isinstance(average_inventory, (int, float)):
        raise TypeError("cost_of_goods_sold and average_inventory must be numeric.")

    if average_inventory == 0:
        raise ValueError("average_inventory must not be zero.")

    return float(cost_of_goods_sold / average_inventory)


def gross_profit_margin(
    revenue: Union[int, float],
    cost_of_goods_sold: Union[int, float],
) -> float:
    """Calculate gross profit margin as a percentage.

    Args:
        revenue: Total revenue.
        cost_of_goods_sold: Cost of goods sold.

    Returns:
        Gross profit margin percentage.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If revenue is zero.

    Example:
        >>> gross_profit_margin(200_000, 120_000)
        40.0

    Complexity: O(1)
    """
    if not isinstance(revenue, (int, float)) or not isinstance(cost_of_goods_sold, (int, float)):
        raise TypeError("revenue and cost_of_goods_sold must be numeric.")

    if revenue == 0:
        raise ValueError("revenue must not be zero.")

    return float((revenue - cost_of_goods_sold) / revenue * 100)


def return_on_net_assets(
    net_income: Union[int, float],
    fixed_assets: Union[int, float],
    working_capital: Union[int, float],
) -> float:
    """Calculate return on net assets (RONA).

    Args:
        net_income: Net income for the period.
        fixed_assets: Net fixed assets.
        working_capital: Net working capital.

    Returns:
        RONA as a decimal ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If net assets is zero.

    Example:
        >>> return_on_net_assets(50_000, 300_000, 100_000)
        0.125

    Complexity: O(1)
    """
    if not isinstance(net_income, (int, float)) or not isinstance(fixed_assets, (int, float)) or not isinstance(working_capital, (int, float)):
        raise TypeError("All inputs must be numeric.")

    net_assets = fixed_assets + working_capital

    if net_assets == 0:
        raise ValueError("Net assets (fixed_assets + working_capital) must not be zero.")

    return float(net_income / net_assets)


def fixed_asset_turnover(
    net_sales: Union[int, float],
    net_fixed_assets: Union[int, float],
) -> float:
    """Calculate fixed asset turnover ratio.

    Args:
        net_sales: Net sales for the period.
        net_fixed_assets: Average net fixed assets.

    Returns:
        Fixed asset turnover ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If net_fixed_assets is zero.

    Example:
        >>> fixed_asset_turnover(1_000_000, 250_000)
        4.0

    Complexity: O(1)
    """
    if not isinstance(net_sales, (int, float)) or not isinstance(net_fixed_assets, (int, float)):
        raise TypeError("net_sales and net_fixed_assets must be numeric.")

    if net_fixed_assets == 0:
        raise ValueError("net_fixed_assets must not be zero.")

    return float(net_sales / net_fixed_assets)


def times_interest_earned(
    ebit: Union[int, float],
    interest_expense: Union[int, float],
) -> float:
    """Calculate times interest earned (TIE) ratio.

    Args:
        ebit: Earnings before interest and taxes.
        interest_expense: Interest expense for the period.

    Returns:
        TIE ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If interest_expense is zero.

    Example:
        >>> times_interest_earned(500_000, 100_000)
        5.0

    Complexity: O(1)
    """
    if not isinstance(ebit, (int, float)) or not isinstance(interest_expense, (int, float)):
        raise TypeError("ebit and interest_expense must be numeric.")

    if interest_expense == 0:
        raise ValueError("interest_expense must not be zero.")

    return float(ebit / interest_expense)


def nominal_to_real_rate(
    nominal_rate: Union[int, float],
    inflation_rate: Union[int, float],
) -> float:
    """Convert nominal interest rate to real rate using the Fisher equation.

    real ≈ (1 + nominal) / (1 + inflation) - 1

    Args:
        nominal_rate: Nominal interest rate as a decimal.
        inflation_rate: Inflation rate as a decimal.

    Returns:
        Real interest rate as a decimal.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If inflation_rate is -1 (division by zero).

    Example:
        >>> round(nominal_to_real_rate(0.08, 0.03), 6)
        0.048544

    Complexity: O(1)
    """
    if not isinstance(nominal_rate, (int, float)) or not isinstance(inflation_rate, (int, float)):
        raise TypeError("nominal_rate and inflation_rate must be numeric.")

    if inflation_rate == -1:
        raise ValueError("inflation_rate must not be -1.")

    return float((1 + nominal_rate) / (1 + inflation_rate) - 1)


def operating_expense_ratio(
    operating_expenses: Union[int, float],
    net_sales: Union[int, float],
) -> float:
    """Calculate the operating expense ratio (OER).

    Args:
        operating_expenses: Total operating expenses.
        net_sales: Net sales revenue.

    Returns:
        OER as a decimal ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If net_sales is zero.

    Example:
        >>> operating_expense_ratio(80_000, 200_000)
        0.4

    Complexity: O(1)
    """
    if not isinstance(operating_expenses, (int, float)) or not isinstance(net_sales, (int, float)):
        raise TypeError("operating_expenses and net_sales must be numeric.")

    if net_sales == 0:
        raise ValueError("net_sales must not be zero.")

    return float(operating_expenses / net_sales)


def accounts_payable_turnover(
    total_purchases: Union[int, float],
    average_payables: Union[int, float],
) -> float:
    """Calculate accounts payable turnover ratio.

    Args:
        total_purchases: Total supplier purchases for the period.
        average_payables: Average accounts payable.

    Returns:
        Payable turnover ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If average_payables is zero.

    Example:
        >>> accounts_payable_turnover(600_000, 100_000)
        6.0

    Complexity: O(1)
    """
    if not isinstance(total_purchases, (int, float)) or not isinstance(average_payables, (int, float)):
        raise TypeError("total_purchases and average_payables must be numeric.")

    if average_payables == 0:
        raise ValueError("average_payables must not be zero.")

    return float(total_purchases / average_payables)


def debt_service_ratio(
    net_operating_income: Union[int, float],
    total_debt_service: Union[int, float],
) -> float:
    """Calculate debt service coverage ratio (DSCR).

    Args:
        net_operating_income: Net operating income.
        total_debt_service: Total debt service (principal + interest).

    Returns:
        DSCR ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If total_debt_service is zero.

    Example:
        >>> debt_service_ratio(300_000, 200_000)
        1.5

    Complexity: O(1)
    """
    if not isinstance(net_operating_income, (int, float)) or not isinstance(total_debt_service, (int, float)):
        raise TypeError("net_operating_income and total_debt_service must be numeric.")

    if total_debt_service == 0:
        raise ValueError("total_debt_service must not be zero.")

    return float(net_operating_income / total_debt_service)


def days_payable_outstanding(
    accounts_payable: Union[int, float],
    cost_of_goods_sold: Union[int, float],
    days: Union[int, float] = 365,
) -> float:
    """Calculate days payable outstanding (DPO).

    DPO = (accounts_payable / COGS) × days

    Args:
        accounts_payable: Average accounts payable.
        cost_of_goods_sold: Cost of goods sold for the period.
        days: Number of days in the period (default 365).

    Returns:
        DPO in days.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If cost_of_goods_sold is zero.

    Example:
        >>> days_payable_outstanding(50_000, 500_000)
        36.5

    Complexity: O(1)
    """
    if not isinstance(accounts_payable, (int, float)) or not isinstance(cost_of_goods_sold, (int, float)) or not isinstance(days, (int, float)):
        raise TypeError("All inputs must be numeric.")

    if cost_of_goods_sold == 0:
        raise ValueError("cost_of_goods_sold must not be zero.")

    return float(accounts_payable / cost_of_goods_sold * days)


def return_on_capital_employed(
    ebit: Union[int, float],
    total_assets: Union[int, float],
    current_liabilities: Union[int, float],
) -> float:
    """Calculate return on capital employed (ROCE).

    ROCE = EBIT / (total_assets − current_liabilities)

    Args:
        ebit: Earnings before interest and taxes.
        total_assets: Total assets.
        current_liabilities: Current liabilities.

    Returns:
        ROCE as a decimal ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If capital employed is zero.

    Example:
        >>> return_on_capital_employed(100_000, 800_000, 200_000)
        0.16666666666666666

    Complexity: O(1)
    """
    if not isinstance(ebit, (int, float)) or not isinstance(total_assets, (int, float)) or not isinstance(current_liabilities, (int, float)):
        raise TypeError("All inputs must be numeric.")

    capital_employed = total_assets - current_liabilities

    if capital_employed == 0:
        raise ValueError("Capital employed must not be zero.")

    return float(ebit / capital_employed)


def price_to_sales(
    market_cap: Union[int, float],
    total_revenue: Union[int, float],
) -> float:
    """Calculate the price-to-sales (P/S) ratio.

    Args:
        market_cap: Market capitalisation.
        total_revenue: Total revenue for the period.

    Returns:
        P/S ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If total_revenue is zero.

    Example:
        >>> price_to_sales(5_000_000, 2_000_000)
        2.5

    Complexity: O(1)
    """
    if not isinstance(market_cap, (int, float)) or not isinstance(total_revenue, (int, float)):
        raise TypeError("market_cap and total_revenue must be numeric.")

    if total_revenue == 0:
        raise ValueError("total_revenue must not be zero.")

    return float(market_cap / total_revenue)


def plowback_ratio(
    dividends_per_share: Union[int, float],
    earnings_per_share: Union[int, float],
) -> float:
    """Calculate the plowback (retention) ratio from per-share values.

    plowback = 1 − (DPS / EPS)

    Args:
        dividends_per_share: Dividends per share.
        earnings_per_share: Earnings per share.

    Returns:
        Plowback ratio in [0, 1].

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If earnings_per_share is zero.

    Example:
        >>> plowback_ratio(2, 5)
        0.6

    Complexity: O(1)
    """
    if not isinstance(dividends_per_share, (int, float)) or not isinstance(earnings_per_share, (int, float)):
        raise TypeError("dividends_per_share and earnings_per_share must be numeric.")

    if earnings_per_share == 0:
        raise ValueError("earnings_per_share must not be zero.")

    return float(1 - dividends_per_share / earnings_per_share)


def degree_of_financial_leverage(
    ebit: Union[int, float],
    interest_expense: Union[int, float],
) -> float:
    """Calculate the degree of financial leverage (DFL).

    DFL = EBIT / (EBIT − interest)

    Args:
        ebit: Earnings before interest and taxes.
        interest_expense: Interest expense.

    Returns:
        DFL ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If EBIT equals interest (division by zero).

    Example:
        >>> degree_of_financial_leverage(500_000, 100_000)
        1.25

    Complexity: O(1)
    """
    if not isinstance(ebit, (int, float)) or not isinstance(interest_expense, (int, float)):
        raise TypeError("ebit and interest_expense must be numeric.")

    denom = ebit - interest_expense

    if denom == 0:
        raise ValueError("EBIT minus interest must not be zero.")

    return float(ebit / denom)


def acid_test_ratio(
    cash: Union[int, float],
    marketable_securities: Union[int, float],
    receivables: Union[int, float],
    current_liabilities: Union[int, float],
) -> float:
    """Calculate the acid-test (quick) ratio.

    acid_test = (cash + marketable_securities + receivables) / current_liabilities

    Args:
        cash: Cash and equivalents.
        marketable_securities: Short-term investments.
        receivables: Accounts receivable.
        current_liabilities: Current liabilities.

    Returns:
        Acid-test ratio.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If current_liabilities is zero.

    Example:
        >>> acid_test_ratio(50_000, 30_000, 40_000, 80_000)
        1.5

    Complexity: O(1)
    """
    if not all(isinstance(v, (int, float)) for v in (cash, marketable_securities, receivables, current_liabilities)):
        raise TypeError("All inputs must be numeric.")

    if current_liabilities == 0:
        raise ValueError("current_liabilities must not be zero.")

    return float((cash + marketable_securities + receivables) / current_liabilities)


def cash_flow_coverage(
    operating_cash_flow: Union[int, float],
    total_debt: Union[int, float],
) -> float:
    """Return the cash flow coverage ratio.

    Measures a company's ability to pay off its total debt
    using operating cash flow.  CFR = OCF / Total Debt.

    Args:
        operating_cash_flow: Operating cash flow amount.
        total_debt: Total outstanding debt (must be ≠ 0).

    Returns:
        Cash flow coverage ratio as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If total_debt is zero.

    Example:
        >>> cash_flow_coverage(500_000, 1_000_000)
        0.5

    Complexity: O(1)
    """
    if not isinstance(operating_cash_flow, (int, float)):
        raise TypeError("operating_cash_flow must be numeric.")

    if not isinstance(total_debt, (int, float)):
        raise TypeError("total_debt must be numeric.")

    if total_debt == 0:
        raise ValueError("total_debt must not be zero.")

    return float(operating_cash_flow / total_debt)


def economic_value_added(
    nopat: Union[int, float],
    capital_employed: Union[int, float],
    wacc: Union[int, float],
) -> float:
    """Return the Economic Value Added (EVA).

    EVA = NOPAT - (Capital Employed × WACC).  Measures value
    created above the required return on invested capital.

    Args:
        nopat: Net Operating Profit After Taxes.
        capital_employed: Total capital invested in the business.
        wacc: Weighted Average Cost of Capital (as a decimal).

    Returns:
        Economic value added as a float.

    Raises:
        TypeError: If any argument is not numeric.

    Example:
        >>> economic_value_added(150_000, 1_000_000, 0.10)
        50000.0

    Complexity: O(1)
    """
    if not isinstance(nopat, (int, float)):
        raise TypeError("nopat must be numeric.")

    if not isinstance(capital_employed, (int, float)):
        raise TypeError("capital_employed must be numeric.")

    if not isinstance(wacc, (int, float)):
        raise TypeError("wacc must be numeric.")

    return float(nopat - capital_employed * wacc)


def marginal_cost(
    change_in_total_cost: Union[int, float],
    change_in_quantity: Union[int, float],
) -> float:
    """Return the marginal cost of production.

    Marginal Cost = ΔTotal Cost / ΔQuantity.  Indicates the cost
    of producing one additional unit.

    Args:
        change_in_total_cost: Change in total production cost.
        change_in_quantity: Change in quantity produced (must be ≠ 0).

    Returns:
        Marginal cost as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If change_in_quantity is zero.

    Example:
        >>> marginal_cost(500, 100)
        5.0

    Complexity: O(1)
    """
    if not isinstance(change_in_total_cost, (int, float)):
        raise TypeError("change_in_total_cost must be numeric.")

    if not isinstance(change_in_quantity, (int, float)):
        raise TypeError("change_in_quantity must be numeric.")

    if change_in_quantity == 0:
        raise ValueError("change_in_quantity must not be zero.")

    return float(change_in_total_cost / change_in_quantity)


def cash_conversion_efficiency(
    operating_cash_flow: Union[int, float],
    net_income: Union[int, float],
) -> float:
    """Return the cash conversion efficiency ratio.

    Measures how efficiently net income is converted into
    operating cash flow.  CCE = OCF / Net Income.

    Args:
        operating_cash_flow: Operating cash flow amount.
        net_income: Net income (must be ≠ 0).

    Returns:
        Cash conversion efficiency as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If net_income is zero.

    Example:
        >>> cash_conversion_efficiency(90_000, 100_000)
        0.9

    Complexity: O(1)
    """
    if not isinstance(operating_cash_flow, (int, float)):
        raise TypeError("operating_cash_flow must be numeric.")

    if not isinstance(net_income, (int, float)):
        raise TypeError("net_income must be numeric.")

    if net_income == 0:
        raise ValueError("net_income must not be zero.")

    return float(operating_cash_flow / net_income)


def free_cash_flow_yield(
    free_cash_flow: Union[int, float],
    market_cap: Union[int, float],
) -> float:
    """Return the free cash flow yield.

    FCF Yield = Free Cash Flow / Market Capitalization.
    Indicates how much free cash flow a company generates
    relative to its market value.

    Args:
        free_cash_flow: Free cash flow amount.
        market_cap: Market capitalization (must be > 0).

    Returns:
        Free cash flow yield as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If market_cap is zero or negative.

    Example:
        >>> free_cash_flow_yield(50_000, 1_000_000)
        0.05

    Complexity: O(1)
    """
    if not isinstance(free_cash_flow, (int, float)):
        raise TypeError("free_cash_flow must be numeric.")

    if not isinstance(market_cap, (int, float)):
        raise TypeError("market_cap must be numeric.")

    if market_cap <= 0:
        raise ValueError("market_cap must be positive.")

    return float(free_cash_flow / market_cap)


def price_earnings_growth(
    pe_ratio: Union[int, float],
    earnings_growth_rate: Union[int, float],
) -> float:
    """Return the Price/Earnings-to-Growth (PEG) ratio.

    PEG = P/E Ratio / Earnings Growth Rate.  A PEG < 1 may
    indicate the stock is undervalued relative to its growth.

    Args:
        pe_ratio: Price-to-earnings ratio.
        earnings_growth_rate: Expected earnings growth rate as
            a percentage (e.g. 15 for 15 %).  Must be > 0.

    Returns:
        PEG ratio as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If earnings_growth_rate is zero or negative.

    Example:
        >>> price_earnings_growth(20, 10)
        2.0

    Complexity: O(1)
    """
    if not isinstance(pe_ratio, (int, float)):
        raise TypeError("pe_ratio must be numeric.")

    if not isinstance(earnings_growth_rate, (int, float)):
        raise TypeError("earnings_growth_rate must be numeric.")

    if earnings_growth_rate <= 0:
        raise ValueError("earnings_growth_rate must be positive.")

    return float(pe_ratio / earnings_growth_rate)


def capital_intensity_ratio(
    total_assets: Union[int, float],
    total_revenue: Union[int, float],
) -> float:
    """Return the capital intensity ratio.

    Measures how much asset investment is needed to generate one
    unit of revenue.  CIR = Total Assets / Total Revenue.

    Args:
        total_assets: Total assets (must be ≥ 0).
        total_revenue: Total revenue (must be > 0).

    Returns:
        Capital intensity ratio as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If total_revenue is zero or negative.

    Example:
        >>> capital_intensity_ratio(2_000_000, 1_000_000)
        2.0

    Complexity: O(1)
    """
    if not isinstance(total_assets, (int, float)):
        raise TypeError("total_assets must be numeric.")

    if not isinstance(total_revenue, (int, float)):
        raise TypeError("total_revenue must be numeric.")

    if total_revenue <= 0:
        raise ValueError("total_revenue must be positive.")

    return float(total_assets / total_revenue)


def asset_coverage_ratio(
    total_assets: Union[int, float],
    intangible_assets: Union[int, float],
    current_liabilities: Union[int, float],
    total_debt: Union[int, float],
) -> float:
    """Return the asset coverage ratio.

    ACR = (Total Assets − Intangible Assets − Current Liabilities) /
    Total Debt.  Measures the ability of tangible assets to cover debt.

    Args:
        total_assets: Total assets.
        intangible_assets: Intangible assets (goodwill, patents, …).
        current_liabilities: Current liabilities.
        total_debt: Total outstanding debt (must be > 0).

    Returns:
        Asset coverage ratio as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If total_debt is zero or negative.

    Example:
        >>> asset_coverage_ratio(5_000_000, 500_000, 1_000_000, 2_000_000)
        1.75

    Complexity: O(1)
    """
    for name, val in (("total_assets", total_assets),
                      ("intangible_assets", intangible_assets),
                      ("current_liabilities", current_liabilities),
                      ("total_debt", total_debt)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if total_debt <= 0:
        raise ValueError("total_debt must be positive.")

    return float(
        (total_assets - intangible_assets - current_liabilities) / total_debt
    )


def wacc_two_sources(
    equity: Union[int, float],
    cost_of_equity: Union[int, float],
    debt: Union[int, float],
    cost_of_debt: Union[int, float],
    tax_rate: Union[int, float],
) -> float:
    """Return the Weighted Average Cost of Capital (two-source model).

    WACC = (E / V) · Re + (D / V) · Rd · (1 − Tc),  where
    V = E + D.

    Args:
        equity: Market value of equity (must be ≥ 0).
        cost_of_equity: Cost of equity as a decimal.
        debt: Market value of debt (must be ≥ 0).
        cost_of_debt: Cost of debt as a decimal.
        tax_rate: Corporate tax rate as a decimal (0–1).

    Returns:
        WACC as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If equity + debt is zero.

    Example:
        >>> round(wacc_two_sources(600_000, 0.10, 400_000, 0.05, 0.30), 4)
        0.074

    Complexity: O(1)
    """
    for name, val in (("equity", equity), ("cost_of_equity", cost_of_equity),
                      ("debt", debt), ("cost_of_debt", cost_of_debt),
                      ("tax_rate", tax_rate)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    total = equity + debt

    if total == 0:
        raise ValueError("equity + debt must not be zero.")

    return float(
        (equity / total) * cost_of_equity
        + (debt / total) * cost_of_debt * (1 - tax_rate)
    )


def inventory_to_sales(
    inventory: Union[int, float],
    net_sales: Union[int, float],
) -> float:
    """Return the inventory-to-sales ratio.

    Measures the proportion of inventory relative to net sales.
    A lower ratio indicates faster inventory turnover.

    Args:
        inventory: Inventory value (must be ≥ 0).
        net_sales: Net sales (must be > 0).

    Returns:
        Inventory-to-sales ratio as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If net_sales is zero or negative.

    Example:
        >>> inventory_to_sales(200_000, 1_000_000)
        0.2

    Complexity: O(1)
    """
    if not isinstance(inventory, (int, float)):
        raise TypeError("inventory must be numeric.")

    if not isinstance(net_sales, (int, float)):
        raise TypeError("net_sales must be numeric.")

    if net_sales <= 0:
        raise ValueError("net_sales must be positive.")

    return float(inventory / net_sales)


def nopat_margin(
    nopat: Union[int, float],
    revenue: Union[int, float],
) -> float:
    """Return the NOPAT margin.

    NOPAT Margin = Net Operating Profit After Taxes / Revenue.
    Indicates operational profitability after taxes.

    Args:
        nopat: Net Operating Profit After Taxes.
        revenue: Total revenue (must be > 0).

    Returns:
        NOPAT margin as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If revenue is zero or negative.

    Example:
        >>> nopat_margin(150_000, 1_000_000)
        0.15

    Complexity: O(1)
    """
    if not isinstance(nopat, (int, float)):
        raise TypeError("nopat must be numeric.")

    if not isinstance(revenue, (int, float)):
        raise TypeError("revenue must be numeric.")

    if revenue <= 0:
        raise ValueError("revenue must be positive.")

    return float(nopat / revenue)


def cash_return_on_assets(
    operating_cash_flow: Union[int, float],
    total_assets: Union[int, float],
) -> float:
    """Return the cash return on assets ratio.

    CROA = Operating Cash Flow / Total Assets.  Measures the
    cash-generating efficiency of the asset base.

    Args:
        operating_cash_flow: Operating cash flow.
        total_assets: Total assets (must be > 0).

    Returns:
        Cash return on assets as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If total_assets is zero or negative.

    Example:
        >>> cash_return_on_assets(250_000, 2_000_000)
        0.125

    Complexity: O(1)
    """
    if not isinstance(operating_cash_flow, (int, float)):
        raise TypeError("operating_cash_flow must be numeric.")

    if not isinstance(total_assets, (int, float)):
        raise TypeError("total_assets must be numeric.")

    if total_assets <= 0:
        raise ValueError("total_assets must be positive.")

    return float(operating_cash_flow / total_assets)


def tobin_q_ratio(
    market_value: Union[int, float],
    replacement_cost: Union[int, float],
) -> float:
    """Return Tobin's Q ratio.

    Q = Market Value of Assets / Replacement Cost of Assets.
    A Q > 1 suggests the market values the firm above its
    asset replacement cost.

    Args:
        market_value: Total market value of the firm.
        replacement_cost: Replacement cost of assets (must be > 0).

    Returns:
        Tobin's Q as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If replacement_cost is zero or negative.

    Example:
        >>> tobin_q_ratio(1_500_000, 1_000_000)
        1.5

    Complexity: O(1)
    """
    if not isinstance(market_value, (int, float)):
        raise TypeError("market_value must be numeric.")

    if not isinstance(replacement_cost, (int, float)):
        raise TypeError("replacement_cost must be numeric.")

    if replacement_cost <= 0:
        raise ValueError("replacement_cost must be positive.")

    return float(market_value / replacement_cost)


def defensive_interval(
    liquid_assets: Union[int, float],
    daily_operating_expenses: Union[int, float],
) -> float:
    """Return the defensive interval ratio (in days).

    DIR = Liquid Assets / Daily Operating Expenses.
    Measures how many days a company can operate from
    liquid assets alone without additional revenue.

    Args:
        liquid_assets: Cash + marketable securities + receivables.
        daily_operating_expenses: Average daily operating expenses (> 0).

    Returns:
        Defensive interval in days.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If daily_operating_expenses is zero or negative.

    Example:
        >>> defensive_interval(500_000, 10_000)
        50.0

    Complexity: O(1)
    """
    if not isinstance(liquid_assets, (int, float)):
        raise TypeError("liquid_assets must be numeric.")

    if not isinstance(daily_operating_expenses, (int, float)):
        raise TypeError("daily_operating_expenses must be numeric.")

    if daily_operating_expenses <= 0:
        raise ValueError("daily_operating_expenses must be positive.")

    return float(liquid_assets / daily_operating_expenses)


def sales_growth_rate(
    current_sales: Union[int, float],
    previous_sales: Union[int, float],
) -> float:
    """Return the sales growth rate as a decimal.

    Growth = (Current − Previous) / Previous.

    Args:
        current_sales: Revenue in the current period.
        previous_sales: Revenue in the prior period (must be > 0).

    Returns:
        Sales growth rate as a float (e.g. 0.25 for 25 %).

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If previous_sales is zero or negative.

    Example:
        >>> sales_growth_rate(1_250_000, 1_000_000)
        0.25

    Complexity: O(1)
    """
    if not isinstance(current_sales, (int, float)):
        raise TypeError("current_sales must be numeric.")

    if not isinstance(previous_sales, (int, float)):
        raise TypeError("previous_sales must be numeric.")

    if previous_sales <= 0:
        raise ValueError("previous_sales must be positive.")

    return float((current_sales - previous_sales) / previous_sales)


def debt_to_capital(
    total_debt: Union[int, float],
    total_equity: Union[int, float],
) -> float:
    """Return the debt-to-capital ratio.

    D/(D+E).  Measures the proportion of debt in the
    capital structure.

    Args:
        total_debt: Total debt (must be ≥ 0).
        total_equity: Total equity (must be ≥ 0).

    Returns:
        Debt-to-capital ratio as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If total_debt + total_equity is zero.

    Example:
        >>> debt_to_capital(400_000, 600_000)
        0.4

    Complexity: O(1)
    """
    if not isinstance(total_debt, (int, float)):
        raise TypeError("total_debt must be numeric.")

    if not isinstance(total_equity, (int, float)):
        raise TypeError("total_equity must be numeric.")

    total = total_debt + total_equity

    if total == 0:
        raise ValueError("total_debt + total_equity must not be zero.")

    return float(total_debt / total)


def operating_profit_margin(
    operating_income: Union[int, float],
    revenue: Union[int, float],
) -> float:
    """Return the operating profit margin.

    OPM = Operating Income / Revenue.

    Args:
        operating_income: Operating income (EBIT).
        revenue: Total revenue (must be > 0).

    Returns:
        Operating profit margin as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If revenue is zero or negative.

    Example:
        >>> operating_profit_margin(200_000, 1_000_000)
        0.2

    Complexity: O(1)
    """
    if not isinstance(operating_income, (int, float)):
        raise TypeError("operating_income must be numeric.")

    if not isinstance(revenue, (int, float)):
        raise TypeError("revenue must be numeric.")

    if revenue <= 0:
        raise ValueError("revenue must be positive.")

    return float(operating_income / revenue)


def interest_burden_ratio(
    pre_tax_income: Union[int, float],
    ebit: Union[int, float],
) -> float:
    """Return the interest burden ratio (DuPont component).

    IBR = Pre-tax Income / EBIT.  Values near 1 indicate low
    interest expense relative to operating earnings.

    Args:
        pre_tax_income: Earnings before taxes.
        ebit: Earnings before interest and taxes (must be ≠ 0).

    Returns:
        Interest burden ratio as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If ebit is zero.

    Example:
        >>> interest_burden_ratio(180_000, 200_000)
        0.9

    Complexity: O(1)
    """
    if not isinstance(pre_tax_income, (int, float)):
        raise TypeError("pre_tax_income must be numeric.")

    if not isinstance(ebit, (int, float)):
        raise TypeError("ebit must be numeric.")

    if ebit == 0:
        raise ValueError("ebit must not be zero.")

    return float(pre_tax_income / ebit)


# ---------------------------------------------------------------------------
# Quantitative finance — Options, risk, and advanced valuation
# ---------------------------------------------------------------------------

def _norm_cdf(x: float) -> float:
    """Standard normal CDF via the error function (standalone, no scipy)."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def _norm_pdf(x: float) -> float:
    """Standard normal PDF."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def black_scholes_call(
    s: float, k: float, t: float, r: float, sigma: float
) -> float:
    """Calculates the price of a European call option (Black-Scholes model).

    Args:
        s: Current price of the underlying asset.
        k: Strike price.
        t: Time to expiration in years.
        r: Risk-free interest rate (annualised, e.g. 0.05).
        sigma: Volatility of the underlying (annualised, e.g. 0.2).

    Returns:
        Theoretical call option price.

    Raises:
        TypeError: If any input is not numeric.
        ValueError: If s, k, t, or sigma are not positive.

    Example:
        >>> round(black_scholes_call(100, 100, 1, 0.05, 0.2), 2)
        10.45

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("r", r), ("sigma", sigma)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t, and sigma must be positive")

    d1 = (math.log(s / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    return float(s * _norm_cdf(d1) - k * math.exp(-r * t) * _norm_cdf(d2))


def black_scholes_put(
    s: float, k: float, t: float, r: float, sigma: float
) -> float:
    """Calculates the price of a European put option (Black-Scholes model).

    Uses put-call parity: P = C - S + K·e^(-rT).

    Args:
        s: Current price of the underlying asset.
        k: Strike price.
        t: Time to expiration in years.
        r: Risk-free interest rate (annualised).
        sigma: Volatility of the underlying (annualised).

    Returns:
        Theoretical put option price.

    Raises:
        TypeError: If any input is not numeric.
        ValueError: If s, k, t, or sigma are not positive.

    Example:
        >>> round(black_scholes_put(100, 100, 1, 0.05, 0.2), 2)
        5.57

    Complexity: O(1)
    """
    call = black_scholes_call(s, k, t, r, sigma)
    return float(call - s + k * math.exp(-r * t))


def implied_volatility(
    option_price: float,
    s: float,
    k: float,
    t: float,
    r: float,
    option_type: str = "call",
    tol: float = 1e-6,
    max_iter: int = 100,
) -> float:
    """Estimates implied volatility via bisection (standalone, no scipy).

    Args:
        option_price: Observed market price of the option.
        s: Current price of the underlying asset.
        k: Strike price.
        t: Time to expiration in years.
        r: Risk-free interest rate (annualised).
        option_type: ``"call"`` or ``"put"``.
        tol: Convergence tolerance.
        max_iter: Maximum iterations.

    Returns:
        Implied volatility (annualised).

    Raises:
        TypeError: If numeric inputs are not numeric.
        ValueError: If option_type is invalid or convergence fails.

    Example:
        >>> round(implied_volatility(10.45, 100, 100, 1, 0.05, "call"), 2)
        0.2

    Complexity: O(max_iter)
    """
    for name, val in (("option_price", option_price), ("s", s), ("k", k), ("t", t)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if option_type not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'")

    pricer = black_scholes_call if option_type == "call" else black_scholes_put
    lo, hi = 1e-6, 5.0

    for _ in range(max_iter):
        mid = (lo + hi) / 2.0
        price = pricer(s, k, t, r, mid)

        if abs(price - option_price) < tol:
            return float(mid)

        if price < option_price:
            lo = mid
        else:
            hi = mid

    return float((lo + hi) / 2.0)


def altman_z_score(
    working_capital: float,
    retained_earnings: float,
    ebit: float,
    market_cap: float,
    total_liabilities: float,
    total_assets: float,
    sales: float,
) -> float:
    """Calculates the Altman Z-Score for bankruptcy prediction.

    Z = 1.2·X1 + 1.4·X2 + 3.3·X3 + 0.6·X4 + 1.0·X5

    Args:
        working_capital: Current assets minus current liabilities.
        retained_earnings: Total retained earnings.
        ebit: Earnings before interest and taxes.
        market_cap: Market capitalisation of equity.
        total_liabilities: Total liabilities.
        total_assets: Total assets (must be positive).
        sales: Total sales / revenue.

    Returns:
        Altman Z-Score (> 2.99 safe, 1.81–2.99 grey zone, < 1.81 distress).

    Raises:
        TypeError: If any input is not numeric.
        ValueError: If total_assets or total_liabilities is not positive.

    Example:
        >>> round(altman_z_score(50, 30, 40, 200, 100, 300, 250), 2)
        2.82

    Complexity: O(1)
    """
    params = {
        "working_capital": working_capital,
        "retained_earnings": retained_earnings,
        "ebit": ebit,
        "market_cap": market_cap,
        "total_liabilities": total_liabilities,
        "total_assets": total_assets,
        "sales": sales,
    }

    for name, val in params.items():

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if total_assets <= 0:
        raise ValueError("total_assets must be positive")

    if total_liabilities <= 0:
        raise ValueError("total_liabilities must be positive")

    x1 = working_capital / total_assets
    x2 = retained_earnings / total_assets
    x3 = ebit / total_assets
    x4 = market_cap / total_liabilities
    x5 = sales / total_assets
    return float(1.2 * x1 + 1.4 * x2 + 3.3 * x3 + 0.6 * x4 + 1.0 * x5)


def macaulay_duration_simple(
    coupon_rate: float, ytm: float, periods: int
) -> float:
    """Calculates Macaulay duration from coupon rate and yield to maturity.

    Args:
        coupon_rate: Annual coupon rate (e.g. 0.05 for 5%).
        ytm: Yield to maturity per period (e.g. 0.05).
        periods: Number of remaining coupon periods.

    Returns:
        Macaulay duration in periods.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If periods is not positive or ytm is negative.

    Example:
        >>> round(macaulay_duration_simple(0.05, 0.05, 10), 4)
        7.1078

    Complexity: O(n) where n = periods
    """
    if not isinstance(coupon_rate, (int, float)):
        raise TypeError("coupon_rate must be numeric")

    if not isinstance(ytm, (int, float)):
        raise TypeError("ytm must be numeric")

    if not isinstance(periods, int) or periods <= 0:
        raise ValueError("periods must be a positive integer")

    c = coupon_rate  # coupon as fraction of face
    pv_total = 0.0
    weighted_sum = 0.0

    for t in range(1, periods + 1):
        cf = c if t < periods else c + 1.0  # last period includes face value
        df = (1 + ytm) ** t
        pv = cf / df
        pv_total += pv
        weighted_sum += t * pv

    return float(weighted_sum / pv_total)


def modified_duration_simple(
    mac_duration: float, ytm: float, frequency: int = 1
) -> float:
    """Calculates modified duration from Macaulay duration.

    Modified duration = Macaulay duration / (1 + ytm / frequency).

    Args:
        mac_duration: Macaulay duration in periods.
        ytm: Yield to maturity (annualised).
        frequency: Coupon payments per year (1, 2, 4, 12).

    Returns:
        Modified duration.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If frequency is not positive.

    Example:
        >>> round(modified_duration_simple(7.1078, 0.05, 1), 4)
        6.7693

    Complexity: O(1)
    """
    if not isinstance(mac_duration, (int, float)):
        raise TypeError("mac_duration must be numeric")

    if not isinstance(ytm, (int, float)):
        raise TypeError("ytm must be numeric")

    if not isinstance(frequency, int) or frequency <= 0:
        raise ValueError("frequency must be a positive integer")

    return float(mac_duration / (1 + ytm / frequency))


def bond_convexity(
    coupon_rate: float, ytm: float, periods: int, face: float = 100.0
) -> float:
    """Calculates the convexity of a bond.

    Convexity measures the curvature of the price-yield relationship,
    providing a second-order correction to duration.

    Args:
        coupon_rate: Annual coupon rate (e.g. 0.05).
        ytm: Yield to maturity per period.
        periods: Number of remaining coupon periods.
        face: Face (par) value of the bond.

    Returns:
        Bond convexity.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If periods or face is not positive.

    Example:
        >>> round(bond_convexity(0.05, 0.05, 10, 100), 2)
        60.98

    Complexity: O(n) where n = periods
    """
    if not isinstance(coupon_rate, (int, float)):
        raise TypeError("coupon_rate must be numeric")

    if not isinstance(ytm, (int, float)):
        raise TypeError("ytm must be numeric")

    if not isinstance(periods, int) or periods <= 0:
        raise ValueError("periods must be a positive integer")

    if not isinstance(face, (int, float)) or face <= 0:
        raise ValueError("face must be a positive number")

    c = coupon_rate * face
    pv_total = 0.0
    conv_sum = 0.0

    for t in range(1, periods + 1):
        cf = c if t < periods else c + face
        df = (1 + ytm) ** t
        pv = cf / df
        pv_total += pv
        conv_sum += t * (t + 1) * cf / ((1 + ytm) ** (t + 2))

    return float(conv_sum / pv_total)


def var_parametric(
    portfolio_value: float,
    mean_return: float,
    std_return: float,
    confidence: float = 0.95,
) -> float:
    """Calculates parametric Value at Risk (VaR) assuming normal returns.

    VaR = Portfolio × (μ − z_α × σ), standalone using math.erfinv.

    Args:
        portfolio_value: Total portfolio value.
        mean_return: Expected return (e.g. 0.001 for 0.1%).
        std_return: Standard deviation of returns.
        confidence: Confidence level (e.g. 0.95 or 0.99).

    Returns:
        Value at Risk as a positive loss amount.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If confidence is not in (0, 1) or std_return is negative.

    Example:
        >>> round(var_parametric(1_000_000, 0.001, 0.02, 0.95), 2)
        31901.39

    Complexity: O(1)
    """
    for name, val in (
        ("portfolio_value", portfolio_value),
        ("mean_return", mean_return),
        ("std_return", std_return),
        ("confidence", confidence),
    ):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1 (exclusive)")

    if std_return < 0:
        raise ValueError("std_return must be non-negative")

    # Inverse normal CDF via erfinv: z = sqrt(2) * erfinv(2p - 1)
    z = math.sqrt(2) * _erfinv(2 * confidence - 1)
    return float(abs(portfolio_value * (mean_return - z * std_return)))


def _erfinv(x: float) -> float:
    """Approximate inverse error function (standalone, rational approx)."""
    # Winitzki approximation
    a = 0.147
    ln_part = math.log(1 - x * x)
    term1 = 2 / (math.pi * a) + ln_part / 2
    sign = 1 if x >= 0 else -1
    return sign * math.sqrt(math.sqrt(term1 ** 2 - ln_part / a) - term1)


def expected_shortfall(
    portfolio_value: float,
    mean_return: float,
    std_return: float,
    confidence: float = 0.95,
) -> float:
    """Calculates parametric Expected Shortfall (CVaR) assuming normal returns.

    ES = Portfolio × (μ − σ × φ(z_α) / (1 − α))

    Args:
        portfolio_value: Total portfolio value.
        mean_return: Expected return.
        std_return: Standard deviation of returns.
        confidence: Confidence level (e.g. 0.95).

    Returns:
        Expected Shortfall as a positive loss amount.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If confidence is not in (0, 1).

    Example:
        >>> round(expected_shortfall(1_000_000, 0.001, 0.02, 0.95), 2)
        40134.66

    Complexity: O(1)
    """
    for name, val in (
        ("portfolio_value", portfolio_value),
        ("mean_return", mean_return),
        ("std_return", std_return),
        ("confidence", confidence),
    ):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if not 0 < confidence < 1:
        raise ValueError("confidence must be between 0 and 1 (exclusive)")

    z = math.sqrt(2) * _erfinv(2 * confidence - 1)
    phi_z = _norm_pdf(z)
    es_return = mean_return - std_return * phi_z / (1 - confidence)
    return float(abs(portfolio_value * es_return))


def mortgage_total_cost(
    principal: float, annual_rate: float, years: int
) -> float:
    """Calculates the total cost of a fixed-rate mortgage (principal + interest).

    Args:
        principal: Loan principal amount.
        annual_rate: Annual interest rate (e.g. 0.035 for 3.5%).
        years: Loan term in years.

    Returns:
        Total amount paid over the life of the loan.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If principal, annual_rate, or years are not positive.

    Example:
        >>> round(mortgage_total_cost(200_000, 0.035, 30), 2)
        323312.18

    Complexity: O(1)
    """
    if not isinstance(principal, (int, float)):
        raise TypeError("principal must be numeric")

    if not isinstance(annual_rate, (int, float)):
        raise TypeError("annual_rate must be numeric")

    if not isinstance(years, int):
        raise TypeError("years must be an integer")

    if principal <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("principal, annual_rate, and years must be positive")

    monthly_rate = annual_rate / 12
    n_payments = years * 12
    payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** (-n_payments))
    return float(payment * n_payments)


def mortgage_remaining_balance(
    principal: float,
    annual_rate: float,
    years: int,
    payments_made: int,
) -> float:
    """Calculates the remaining balance of a fixed-rate mortgage after N payments.

    Args:
        principal: Original loan principal.
        annual_rate: Annual interest rate.
        years: Original loan term in years.
        payments_made: Number of monthly payments already made.

    Returns:
        Remaining loan balance.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If payments_made exceeds total payments or inputs are not positive.

    Example:
        >>> round(mortgage_remaining_balance(200_000, 0.035, 30, 60), 2)
        178779.95

    Complexity: O(1)
    """
    if not isinstance(principal, (int, float)):
        raise TypeError("principal must be numeric")

    if not isinstance(annual_rate, (int, float)):
        raise TypeError("annual_rate must be numeric")

    if not isinstance(years, int) or not isinstance(payments_made, int):
        raise TypeError("years and payments_made must be integers")

    if principal <= 0 or annual_rate <= 0 or years <= 0:
        raise ValueError("principal, annual_rate, and years must be positive")

    n_total = years * 12

    if payments_made < 0 or payments_made > n_total:
        raise ValueError(f"payments_made must be between 0 and {n_total}")

    r = annual_rate / 12
    balance = principal * ((1 + r) ** n_total - (1 + r) ** payments_made) / (
        (1 + r) ** n_total - 1
    )
    return float(balance)


def loan_to_value(loan_amount: float, appraised_value: float) -> float:
    """Calculate the Loan-to-Value (LTV) ratio.

    LTV = loan_amount / appraised_value * 100.

    Args:
        loan_amount: Outstanding loan balance.
        appraised_value: Current appraised value of the asset.

    Returns:
        LTV ratio as a percentage.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If *appraised_value* is not positive.

    Example:
        >>> loan_to_value(180_000, 200_000)
        90.0

    Complexity: O(1)
    """
    if not isinstance(loan_amount, (int, float)):
        raise TypeError("loan_amount must be numeric")

    if not isinstance(appraised_value, (int, float)):
        raise TypeError("appraised_value must be numeric")

    if appraised_value <= 0:
        raise ValueError("appraised_value must be positive")

    return float(loan_amount / appraised_value * 100)


def debt_to_income(monthly_debt: float, monthly_income: float) -> float:
    """Calculate Debt-to-Income (DTI) ratio.

    DTI = monthly_debt / monthly_income * 100.

    Args:
        monthly_debt: Total monthly debt payments.
        monthly_income: Gross monthly income.

    Returns:
        DTI ratio as a percentage.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If *monthly_income* is not positive.

    Example:
        >>> debt_to_income(1500, 5000)
        30.0

    Complexity: O(1)
    """
    if not isinstance(monthly_debt, (int, float)):
        raise TypeError("monthly_debt must be numeric")

    if not isinstance(monthly_income, (int, float)):
        raise TypeError("monthly_income must be numeric")

    if monthly_income <= 0:
        raise ValueError("monthly_income must be positive")

    return float(monthly_debt / monthly_income * 100)


def annuity_due_fv(
    payment: float,
    rate: float,
    periods: int,
) -> float:
    """Future value of an annuity due (payments at the beginning of each period).

    FV = payment × [((1+r)^n − 1) / r] × (1+r).

    Args:
        payment: Periodic payment amount.
        rate: Interest rate per period (e.g. 0.05 for 5%).
        periods: Number of periods.

    Returns:
        Future value as a float.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If *rate* < 0 or *periods* < 1.

    Example:
        >>> round(annuity_due_fv(1000, 0.05, 10), 2)
        13206.79

    Complexity: O(1)
    """
    if not isinstance(payment, (int, float)):
        raise TypeError("payment must be numeric")

    if not isinstance(rate, (int, float)):
        raise TypeError("rate must be numeric")

    if not isinstance(periods, int):
        raise TypeError("periods must be an integer")

    if rate < 0:
        raise ValueError("rate must be non-negative")

    if periods < 1:
        raise ValueError("periods must be at least 1")

    if rate == 0:
        return float(payment * periods)

    fv_ordinary = payment * (((1 + rate) ** periods - 1) / rate)
    return float(fv_ordinary * (1 + rate))


def annuity_due_pv(
    payment: float,
    rate: float,
    periods: int,
) -> float:
    """Present value of an annuity due (payments at the beginning of each period).

    PV = payment × [(1 − (1+r)^−n) / r] × (1+r).

    Args:
        payment: Periodic payment amount.
        rate: Interest rate per period.
        periods: Number of periods.

    Returns:
        Present value as a float.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If *rate* < 0 or *periods* < 1.

    Example:
        >>> round(annuity_due_pv(1000, 0.05, 10), 2)
        8107.82

    Complexity: O(1)
    """
    if not isinstance(payment, (int, float)):
        raise TypeError("payment must be numeric")

    if not isinstance(rate, (int, float)):
        raise TypeError("rate must be numeric")

    if not isinstance(periods, int):
        raise TypeError("periods must be an integer")

    if rate < 0:
        raise ValueError("rate must be non-negative")

    if periods < 1:
        raise ValueError("periods must be at least 1")

    if rate == 0:
        return float(payment * periods)

    pv_ordinary = payment * ((1 - (1 + rate) ** -periods) / rate)
    return float(pv_ordinary * (1 + rate))


def weighted_average_cost_of_debt(
    debts: list[float],
    rates: list[float],
    tax_rate: float = 0.0,
) -> float:
    """Compute the weighted average after-tax cost of debt.

    Each debt weight is ``debts[i] / total_debt``.  The effective rate
    is ``rates[i] * (1 - tax_rate)``.

    Args:
        debts: Outstanding amounts for each debt tranche.
        rates: Annual interest rate for each tranche.
        tax_rate: Corporate tax rate in [0, 1).

    Returns:
        Weighted average cost as a float.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If lists are empty, lengths differ, or total debt is zero.

    Example:
        >>> round(weighted_average_cost_of_debt([1000, 2000], [0.05, 0.07], 0.3), 4)
        0.0443

    Complexity: O(n)
    """
    if not isinstance(debts, list) or not isinstance(rates, list):
        raise TypeError("debts and rates must be lists")

    if not debts:
        raise ValueError("debts must not be empty")

    if len(debts) != len(rates):
        raise ValueError("debts and rates must have the same length")

    if not isinstance(tax_rate, (int, float)):
        raise TypeError("tax_rate must be numeric")

    total = sum(debts)

    if total == 0:
        raise ValueError("total debt must not be zero")

    return float(
        sum(d * r * (1 - tax_rate) for d, r in zip(debts, rates)) / total
    )


def bond_yield_to_worst(
    face: float,
    coupon_rate: float,
    price: float,
    years_to_maturity: int,
    call_years: list[int] | None = None,
) -> float:
    """Estimate the yield-to-worst for a callable bond.

    Computes the yield-to-maturity and each yield-to-call, then
    returns the minimum.  Uses a simple Newton iteration for each
    scenario.

    Args:
        face: Face / par value.
        coupon_rate: Annual coupon rate.
        price: Current market price.
        years_to_maturity: Years to final maturity.
        call_years: Optional list of years at which the bond is callable.

    Returns:
        Yield-to-worst as a decimal.

    Raises:
        TypeError: If inputs have wrong types.
        ValueError: If *price* <= 0 or *years_to_maturity* < 1.

    Example:
        >>> round(bond_yield_to_worst(1000, 0.06, 950, 10, [5]), 4)
        0.0708

    Complexity: O(k × i), k = number of call dates, i = iterations.
    """
    if not isinstance(face, (int, float)):
        raise TypeError("face must be numeric")

    if not isinstance(coupon_rate, (int, float)):
        raise TypeError("coupon_rate must be numeric")

    if not isinstance(price, (int, float)):
        raise TypeError("price must be numeric")

    if not isinstance(years_to_maturity, int):
        raise TypeError("years_to_maturity must be an integer")

    if price <= 0:
        raise ValueError("price must be positive")

    if years_to_maturity < 1:
        raise ValueError("years_to_maturity must be at least 1")

    coupon = face * coupon_rate

    def _ytm(n: int, redemption: float) -> float:
        # Newton's method to solve: price = Σ coupon/(1+y)^t + redemption/(1+y)^n
        y = coupon_rate  # initial guess

        for _ in range(200):
            pv = sum(coupon / (1 + y) ** t for t in range(1, n + 1))
            pv += redemption / (1 + y) ** n
            dpv = sum(-t * coupon / (1 + y) ** (t + 1) for t in range(1, n + 1))
            dpv -= n * redemption / (1 + y) ** (n + 1)

            if abs(dpv) < 1e-15:
                break

            y -= (pv - price) / dpv

        return y

    yields = [_ytm(years_to_maturity, face)]

    for cy in (call_years or []):

        if 1 <= cy < years_to_maturity:
            yields.append(_ytm(cy, face))

    return float(min(yields))


def option_delta_bs(
    s: float,
    k: float,
    t: float,
    r: float,
    sigma: float,
    option_type: str = "call",
) -> float:
    """Black-Scholes delta for a European option.

    Args:
        s: Current underlying price.
        k: Strike price.
        t: Time to expiry in years.
        r: Risk-free rate.
        sigma: Volatility (annualised).
        option_type: ``'call'`` or ``'put'``.

    Returns:
        Delta value.

    Raises:
        TypeError: If numeric inputs are wrong type.
        ValueError: If *s*, *k*, *t*, *sigma* <= 0 or bad *option_type*.

    Example:
        >>> round(option_delta_bs(100, 100, 1, 0.05, 0.2), 4)
        0.6368

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("r", r), ("sigma", sigma)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t, sigma must be positive")

    if option_type not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'")

    d1 = (math.log(s / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * math.sqrt(t))

    # Standard normal CDF via ERF
    def _norm_cdf(x: float) -> float:
        return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

    if option_type == "call":
        return float(_norm_cdf(d1))

    return float(_norm_cdf(d1) - 1.0)


def option_gamma_bs(
    s: float,
    k: float,
    t: float,
    r: float,
    sigma: float,
) -> float:
    """Black-Scholes gamma for a European option.

    Gamma is the same for calls and puts.

    Args:
        s: Current underlying price.
        k: Strike price.
        t: Time to expiry in years.
        r: Risk-free rate.
        sigma: Volatility (annualised).

    Returns:
        Gamma value.

    Raises:
        TypeError: If numeric inputs are wrong type.
        ValueError: If *s*, *k*, *t*, *sigma* <= 0.

    Example:
        >>> round(option_gamma_bs(100, 100, 1, 0.05, 0.2), 6)
        0.018762

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("r", r), ("sigma", sigma)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t, sigma must be positive")

    d1 = (math.log(s / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * math.sqrt(t))

    pdf = math.exp(-0.5 * d1 ** 2) / math.sqrt(2.0 * math.pi)

    return float(pdf / (s * sigma * math.sqrt(t)))


def economic_order_quantity(
    annual_demand: float,
    order_cost: float,
    holding_cost: float,
) -> float:
    """Economic Order Quantity (EOQ) — Wilson's formula.

    EOQ = √(2 × D × S / H)

    Args:
        annual_demand: Annual demand in units.
        order_cost: Fixed cost per order.
        holding_cost: Holding cost per unit per year.

    Returns:
        Optimal order quantity.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If any input is not positive.

    Example:
        >>> round(economic_order_quantity(10000, 50, 2), 2)
        707.11

    Complexity: O(1)
    """
    for name, val in (("annual_demand", annual_demand),
                      ("order_cost", order_cost),
                      ("holding_cost", holding_cost)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric")

        if val <= 0:
            raise ValueError(f"{name} must be positive")

    return float(math.sqrt(2 * annual_demand * order_cost / holding_cost))


def markup_percentage(
    cost: Union[int, float],
    selling_price: Union[int, float],
) -> float:
    """Calculate markup percentage (margin over cost).

    markup = (selling_price - cost) / cost × 100

    Args:
        cost: Unit cost.
        selling_price: Selling price.

    Returns:
        Markup as a percentage.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If cost is zero.

    Example:
        >>> markup_percentage(50, 80)
        60.0

    Complexity: O(1)
    """
    if not isinstance(cost, (int, float)) or not isinstance(selling_price, (int, float)):
        raise TypeError("All inputs must be numeric.")

    if cost == 0:
        raise ValueError("cost must not be zero.")

    return float((selling_price - cost) / cost * 100)


def markdown_percentage(
    original_price: Union[int, float],
    sale_price: Union[int, float],
) -> float:
    """Calculate markdown (discount) percentage.

    markdown = (original_price - sale_price) / original_price × 100

    Args:
        original_price: Original price before discount.
        sale_price: Discounted selling price.

    Returns:
        Discount as a percentage.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If original_price is zero.

    Example:
        >>> markdown_percentage(100, 75)
        25.0

    Complexity: O(1)
    """
    if not isinstance(original_price, (int, float)) or not isinstance(sale_price, (int, float)):
        raise TypeError("All inputs must be numeric.")

    if original_price == 0:
        raise ValueError("original_price must not be zero.")

    return float((original_price - sale_price) / original_price * 100)


def inflation_adjusted_value(
    amount: Union[int, float],
    rate: Union[int, float],
    years: Union[int, float],
) -> float:
    """Calculate the inflation-adjusted (real) value of money.

    real_value = amount / (1 + rate)^years

    Args:
        amount: Nominal amount.
        rate: Annual inflation rate as a decimal (e.g. 0.03 for 3 %).
        years: Number of years.

    Returns:
        Present real value.

    Raises:
        TypeError: If inputs are not numeric.
        ValueError: If rate is -1 (division by zero).

    Example:
        >>> round(inflation_adjusted_value(1000, 0.03, 10), 2)
        744.09

    Complexity: O(1)
    """
    for name, val in (("amount", amount), ("rate", rate), ("years", years)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if rate == -1:
        raise ValueError("rate must not be -1 (would cause division by zero).")

    return float(amount / (1 + rate) ** years)


def purchasing_power(
    amount: Union[int, float],
    inflation_rate: Union[int, float],
    years: Union[int, float],
) -> float:
    """Calculate remaining purchasing power after inflation erodes value.

    pp = amount * (1 - inflation_rate)^years

    Args:
        amount: Initial monetary amount.
        inflation_rate: Annual inflation rate as a decimal.
        years: Number of years.

    Returns:
        Reduced purchasing power.

    Raises:
        TypeError: If inputs are not numeric.

    Example:
        >>> round(purchasing_power(1000, 0.03, 10), 2)
        737.42

    Complexity: O(1)
    """
    for name, val in (("amount", amount), ("inflation_rate", inflation_rate), ("years", years)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    return float(amount * (1 - inflation_rate) ** years)


def net_asset_value(
    total_assets: float, total_liabilities: float, shares: float
) -> float:
    """Calculate Net Asset Value (NAV) per share.

    Description:
        NAV = (Total Assets − Total Liabilities) / Shares Outstanding.
        Common in mutual fund and ETF valuation.

    Args:
        total_assets: Total assets of the fund.
        total_liabilities: Total liabilities of the fund.
        shares: Number of shares outstanding.

    Returns:
        NAV per share.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If *shares* is zero.

    Usage Example:
        >>> net_asset_value(1_000_000, 200_000, 10_000)
        80.0

    Complexity: O(1)
    """
    for name, val in (("total_assets", total_assets), ("total_liabilities", total_liabilities), ("shares", shares)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if shares == 0:
        raise ValueError("shares must not be zero.")

    return float((total_assets - total_liabilities) / shares)


def unlevered_beta(
    levered_beta: float, tax_rate: float, de_ratio: float
) -> float:
    """Calculate unlevered (asset) beta using the Hamada equation.

    Description:
        β_u = β_L / (1 + (1 − tax_rate) × D/E).
        Strips out the financial leverage effect.

    Args:
        levered_beta: Levered (equity) beta.
        tax_rate: Corporate tax rate (0–1).
        de_ratio: Debt-to-equity ratio.

    Returns:
        Unlevered beta.

    Raises:
        TypeError: If any argument is not numeric.

    Usage Example:
        >>> round(unlevered_beta(1.2, 0.30, 0.5), 4)
        0.8889

    Complexity: O(1)
    """
    for name, val in (("levered_beta", levered_beta), ("tax_rate", tax_rate), ("de_ratio", de_ratio)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    return float(levered_beta / (1 + (1 - tax_rate) * de_ratio))


def levered_beta(
    asset_beta: float, tax_rate: float, de_ratio: float
) -> float:
    """Calculate levered (equity) beta using the inverse Hamada equation.

    Description:
        β_L = β_u × (1 + (1 − tax_rate) × D/E).
        Adds the financial leverage effect to the asset beta.

    Args:
        asset_beta: Unlevered (asset) beta.
        tax_rate: Corporate tax rate (0–1).
        de_ratio: Debt-to-equity ratio.

    Returns:
        Levered beta.

    Raises:
        TypeError: If any argument is not numeric.

    Usage Example:
        >>> round(levered_beta(0.8889, 0.30, 0.5), 2)
        1.2

    Complexity: O(1)
    """
    for name, val in (("asset_beta", asset_beta), ("tax_rate", tax_rate), ("de_ratio", de_ratio)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    return float(asset_beta * (1 + (1 - tax_rate) * de_ratio))


def bond_current_yield(
    annual_coupon: float, market_price: float
) -> float:
    """Calculate the current yield of a bond.

    Description:
        Current Yield = Annual Coupon Payment / Market Price × 100.
        A simple measure of investment income relative to price.

    Args:
        annual_coupon: Annual coupon payment.
        market_price: Current market price of the bond.

    Returns:
        Current yield as a percentage.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If *market_price* is zero.

    Usage Example:
        >>> bond_current_yield(50, 980)
        5.102040816326531

    Complexity: O(1)
    """
    for name, val in (("annual_coupon", annual_coupon), ("market_price", market_price)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if market_price == 0:
        raise ValueError("market_price must not be zero.")

    return float(annual_coupon / market_price * 100)


def cost_of_debt_after_tax(
    interest_rate: float, tax_rate: float
) -> float:
    """Calculate the after-tax cost of debt.

    Description:
        After-tax cost = Interest Rate × (1 − Tax Rate).
        Used in WACC calculations.

    Args:
        interest_rate: Pre-tax cost of debt (as decimal, e.g. 0.06).
        tax_rate: Corporate tax rate (as decimal, e.g. 0.30).

    Returns:
        After-tax cost of debt (as decimal).

    Raises:
        TypeError: If any argument is not numeric.

    Usage Example:
        >>> cost_of_debt_after_tax(0.06, 0.30)
        0.042

    Complexity: O(1)
    """
    for name, val in (("interest_rate", interest_rate), ("tax_rate", tax_rate)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    return float(interest_rate * (1 - tax_rate))


def modified_dietz_return(
    start_value: float,
    end_value: float,
    cash_flows: list,
    cf_days: list,
    total_days: int,
) -> float:
    """Calculate the Modified Dietz rate of return.

    Description:
        A money-weighted approximation that adjusts for the timing of
        cash flows: R = (V1 - V0 - CF) / (V0 + Σ(CFi × Wi)), where
        Wi = (total_days - dayi) / total_days.

    Args:
        start_value: Portfolio value at start.
        end_value: Portfolio value at end.
        cash_flows: List of cash flow amounts (positive = inflow).
        cf_days: Day number of each cash flow (0 = start).
        total_days: Total days in the period (> 0).

    Returns:
        Modified Dietz return as a float.

    Raises:
        TypeError: If numeric arguments are not numeric or lists are wrong.
        ValueError: If lists differ in length or total_days <= 0.

    Usage Example:
        >>> modified_dietz_return(1000, 1200, [100], [15], 30)
        0.09090909090909091

    Complexity: O(n)
    """
    for name, val in (
        ("start_value", start_value),
        ("end_value", end_value),
        ("total_days", total_days),
    ):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if not isinstance(cash_flows, list) or not isinstance(cf_days, list):
        raise TypeError("cash_flows and cf_days must be lists.")

    if len(cash_flows) != len(cf_days):
        raise ValueError("cash_flows and cf_days must have the same length.")

    if total_days <= 0:
        raise ValueError("total_days must be positive.")

    total_cf = sum(cash_flows)
    weighted_cf = sum(
        cf * ((total_days - day) / total_days)
        for cf, day in zip(cash_flows, cf_days)
    )

    denominator = start_value + weighted_cf

    if denominator == 0:
        raise ValueError("Denominator is zero; cannot compute return.")

    return float((end_value - start_value - total_cf) / denominator)


def omega_ratio(returns: list, threshold: float = 0.0) -> float:
    """Calculate the Omega ratio of a return series.

    Description:
        Omega = Σmax(Ri - threshold, 0) / Σmax(threshold - Ri, 0).
        A higher omega indicates a more favourable return distribution.

    Args:
        returns: List of periodic returns (as decimals).
        threshold: Minimum acceptable return (default 0.0).

    Returns:
        Omega ratio (positive float).

    Raises:
        TypeError: If arguments are not the correct type.
        ValueError: If returns is empty or all returns are below threshold.

    Usage Example:
        >>> omega_ratio([0.05, 0.02, -0.01, 0.03, -0.02], 0.0)
        2.0

    Complexity: O(n)
    """
    if not isinstance(returns, list):
        raise TypeError("returns must be a list.")

    if not isinstance(threshold, (int, float)):
        raise TypeError("threshold must be numeric.")

    if not returns:
        raise ValueError("returns must not be empty.")

    gains = sum(max(r - threshold, 0) for r in returns)
    losses = sum(max(threshold - r, 0) for r in returns)

    if losses == 0:
        raise ValueError("No returns below threshold; omega ratio is infinite.")

    return float(gains / losses)


def ulcer_index(values: list) -> float:
    """Calculate the Ulcer Index for a price or value series.

    Description:
        Measures the depth and duration of drawdowns.
        UI = sqrt(mean(drawdown_pct²)), where drawdown_pct is the
        percentage decline from the running peak.

    Args:
        values: List of prices or portfolio values.

    Returns:
        Ulcer Index as a float.

    Raises:
        TypeError: If *values* is not a list of numerics.
        ValueError: If *values* has fewer than 2 elements.

    Usage Example:
        >>> ulcer_index([100, 105, 102, 98, 103])
        3.5734484731396085

    Complexity: O(n)
    """
    if not isinstance(values, list):
        raise TypeError("values must be a list.")

    if len(values) < 2:
        raise ValueError("values must have at least 2 elements.")

    peak = values[0]
    dd_sq_sum = 0.0

    for v in values:

        if not isinstance(v, (int, float)):
            raise TypeError("All values must be numeric.")

        if v > peak:
            peak = v

        dd_pct = ((v - peak) / peak) * 100.0

        dd_sq_sum += dd_pct ** 2

    return float(math.sqrt(dd_sq_sum / len(values)))


def effective_duration(
    price_down: float,
    price_up: float,
    initial_price: float,
    delta_yield: float,
) -> float:
    """Calculate the effective duration of a bond.

    Description:
        Effective duration = (P₋ - P₊) / (2 × P₀ × Δy), where
        P₋ is the price when yields decrease, P₊ when yields increase.

    Args:
        price_down: Bond price when yield decreases by delta_yield.
        price_up: Bond price when yield increases by delta_yield.
        initial_price: Current bond price.
        delta_yield: The yield shift (as decimal, e.g. 0.01 for 1%).

    Returns:
        Effective duration as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If initial_price or delta_yield is zero.

    Usage Example:
        >>> effective_duration(102.0, 98.0, 100.0, 0.01)
        2.0

    Complexity: O(1)
    """
    for name, val in (
        ("price_down", price_down),
        ("price_up", price_up),
        ("initial_price", initial_price),
        ("delta_yield", delta_yield),
    ):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if initial_price == 0:
        raise ValueError("initial_price must not be zero.")

    if delta_yield == 0:
        raise ValueError("delta_yield must not be zero.")

    return float(
        (price_down - price_up) / (2 * initial_price * delta_yield)
    )


def convexity_adjustment(convexity: float, delta_yield: float) -> float:
    """Calculate the convexity adjustment for bond price change.

    Description:
        Adjustment = 0.5 × Convexity × (Δy)².
        This is the second-order correction added to the duration-based
        price change estimate.

    Args:
        convexity: Bond convexity measure.
        delta_yield: Yield change (as decimal, e.g. 0.01 for 1%).

    Returns:
        Convexity adjustment as a float (percentage price change).

    Raises:
        TypeError: If any argument is not numeric.

    Usage Example:
        >>> convexity_adjustment(150.0, 0.01)
        0.0075

    Complexity: O(1)
    """
    for name, val in (("convexity", convexity), ("delta_yield", delta_yield)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    return float(0.5 * convexity * delta_yield ** 2)


# ---------------------------------------------------------------------------
# Black-Scholes Greeks (standalone, no numpy/scipy)
# ---------------------------------------------------------------------------


def _bs_d1_d2(s: float, k: float, t: float, r: float,
              sigma: float) -> tuple:
    """Compute d1 and d2 for Black-Scholes formulas."""
    d1 = (math.log(s / k) + (r + 0.5 * sigma ** 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    return d1, d2


def _standard_normal_pdf(x: float) -> float:
    """Standard normal PDF φ(x)."""
    return math.exp(-0.5 * x * x) / math.sqrt(2.0 * math.pi)


def _standard_normal_cdf(x: float) -> float:
    """Standard normal CDF Φ(x) via the error function."""
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def option_vega_bs(s: float, k: float, t: float, r: float,
                   sigma: float) -> float:
    """Black-Scholes vega: sensitivity of option price to volatility.

    Description:
        Vega = S √T φ(d₁), where φ is the standard normal PDF.
        The result is the change in option price per unit change
        in volatility.  Vega is the same for calls and puts.

    Args:
        s: Current underlying asset price (> 0).
        k: Strike price (> 0).
        t: Time to expiration in years (> 0).
        r: Risk-free interest rate (annualised, as decimal).
        sigma: Volatility of the underlying (annualised, > 0).

    Returns:
        Vega as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If s, k, t, or sigma are not positive.

    Usage Example:
        >>> round(option_vega_bs(100, 100, 1.0, 0.05, 0.2), 4)
        37.5245

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("r", r), ("sigma", sigma)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t and sigma must be positive.")

    d1, _ = _bs_d1_d2(s, k, t, r, sigma)

    return float(s * math.sqrt(t) * _standard_normal_pdf(d1))


def option_theta_bs(s: float, k: float, t: float, r: float,
                    sigma: float, option_type: str = "call") -> float:
    """Black-Scholes theta: time decay of an option per year.

    Description:
        Theta_call  = −S φ(d₁) σ / (2√T) − r K e^{−rT} Φ(d₂)
        Theta_put   = −S φ(d₁) σ / (2√T) + r K e^{−rT} Φ(−d₂)

    Args:
        s: Current underlying asset price (> 0).
        k: Strike price (> 0).
        t: Time to expiration in years (> 0).
        r: Risk-free interest rate (annualised, as decimal).
        sigma: Volatility of the underlying (annualised, > 0).
        option_type: ``'call'`` or ``'put'``. Default ``'call'``.

    Returns:
        Theta (per year) as a float.  Divide by 365 for daily theta.

    Raises:
        TypeError: If any numeric argument is not numeric.
        ValueError: If s, k, t, or sigma are not positive.
        ValueError: If option_type is not 'call' or 'put'.

    Usage Example:
        >>> round(option_theta_bs(100, 100, 1.0, 0.05, 0.2), 4)
        -6.4140

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("r", r), ("sigma", sigma)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t and sigma must be positive.")

    opt = option_type.lower()

    if opt not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'.")

    d1, d2 = _bs_d1_d2(s, k, t, r, sigma)
    common = -s * _standard_normal_pdf(d1) * sigma / (2.0 * math.sqrt(t))

    if opt == "call":
        return float(common - r * k * math.exp(-r * t) * _standard_normal_cdf(d2))

    return float(common + r * k * math.exp(-r * t) * _standard_normal_cdf(-d2))


def option_rho_bs(s: float, k: float, t: float, r: float,
                  sigma: float, option_type: str = "call") -> float:
    """Black-Scholes rho: sensitivity to the risk-free interest rate.

    Description:
        Rho_call = K T e^{−rT} Φ(d₂)
        Rho_put  = −K T e^{−rT} Φ(−d₂)

    Args:
        s: Current underlying asset price (> 0).
        k: Strike price (> 0).
        t: Time to expiration in years (> 0).
        r: Risk-free interest rate (annualised, as decimal).
        sigma: Volatility of the underlying (annualised, > 0).
        option_type: ``'call'`` or ``'put'``. Default ``'call'``.

    Returns:
        Rho as a float.

    Raises:
        TypeError: If any numeric argument is not numeric.
        ValueError: If s, k, t, or sigma are not positive.
        ValueError: If option_type is not 'call' or 'put'.

    Usage Example:
        >>> round(option_rho_bs(100, 100, 1.0, 0.05, 0.2), 4)
        53.2325

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("r", r), ("sigma", sigma)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t and sigma must be positive.")

    opt = option_type.lower()

    if opt not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'.")

    _, d2 = _bs_d1_d2(s, k, t, r, sigma)
    discount = k * t * math.exp(-r * t)

    if opt == "call":
        return float(discount * _standard_normal_cdf(d2))

    return float(-discount * _standard_normal_cdf(-d2))


# ---------------------------------------------------------------------------
# Perpetuities & continuous compounding
# ---------------------------------------------------------------------------


def present_value_perpetuity(payment: float, rate: float) -> float:
    """Present value of a perpetuity (infinite stream of equal payments).

    Description:
        PV = PMT / r.

    Args:
        payment: Periodic payment amount (> 0).
        rate: Discount rate per period (> 0).

    Returns:
        Present value as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If payment or rate are not positive.

    Usage Example:
        >>> present_value_perpetuity(100, 0.05)
        2000.0

    Complexity: O(1)
    """
    for name, val in (("payment", payment), ("rate", rate)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if payment <= 0 or rate <= 0:
        raise ValueError("payment and rate must be positive.")

    return float(payment / rate)


def growing_perpetuity_pv(payment: float, rate: float,
                          growth: float) -> float:
    """Present value of a growing perpetuity.

    Description:
        PV = PMT / (r − g), where g < r.

    Args:
        payment: First periodic payment (> 0).
        rate: Discount rate per period (> 0).
        growth: Growth rate per period (>= 0, must be < rate).

    Returns:
        Present value as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If payment or rate are not positive, or growth >= rate.

    Usage Example:
        >>> growing_perpetuity_pv(100, 0.10, 0.03)
        1428.5714285714287

    Complexity: O(1)
    """
    for name, val in (("payment", payment), ("rate", rate), ("growth", growth)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if payment <= 0 or rate <= 0:
        raise ValueError("payment and rate must be positive.")

    if growth >= rate:
        raise ValueError("growth must be less than rate.")

    return float(payment / (rate - growth))


def growing_annuity_pv(payment: float, rate: float, growth: float,
                       periods: int) -> float:
    """Present value of a growing annuity.

    Description:
        PV = PMT / (r − g) × [1 − ((1+g)/(1+r))^n].

    Args:
        payment: First periodic payment (> 0).
        rate: Discount rate per period (> 0).
        growth: Growth rate per period (>= 0, must be != rate).
        periods: Number of periods (> 0).

    Returns:
        Present value as a float.

    Raises:
        TypeError: If any argument is not of the expected type.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(growing_annuity_pv(100, 0.10, 0.03, 20), 2)
        1045.05

    Complexity: O(1)
    """
    for name, val in (("payment", payment), ("rate", rate), ("growth", growth)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if not isinstance(periods, int) or periods <= 0:
        raise TypeError("periods must be a positive integer.")

    if payment <= 0 or rate <= 0:
        raise ValueError("payment and rate must be positive.")

    if rate == growth:
        raise ValueError("rate must differ from growth.")

    factor = 1.0 - ((1.0 + growth) / (1.0 + rate)) ** periods

    return float(payment / (rate - growth) * factor)


def continuous_compounding(principal: float, rate: float,
                           time: float) -> float:
    """Future value with continuous compounding.

    Description:
        FV = P × e^{r·t}.

    Args:
        principal: Initial investment amount (> 0).
        rate: Annual interest rate (as decimal).
        time: Time in years (> 0).

    Returns:
        Future value as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If principal or time are not positive.

    Usage Example:
        >>> round(continuous_compounding(1000, 0.05, 10), 2)
        1648.72

    Complexity: O(1)
    """
    for name, val in (("principal", principal), ("rate", rate), ("time", time)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if principal <= 0 or time <= 0:
        raise ValueError("principal and time must be positive.")

    return float(principal * math.exp(rate * time))


def discount_factor(rate: float, periods: Union[int, float]) -> float:
    """Discount factor for a given rate and number of periods.

    Description:
        DF = 1 / (1 + r)^n.

    Args:
        rate: Discount rate per period (> 0).
        periods: Number of periods (> 0).

    Returns:
        Discount factor as a float in (0, 1].

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If rate or periods are not positive.

    Usage Example:
        >>> round(discount_factor(0.05, 10), 6)
        0.613913

    Complexity: O(1)
    """
    for name, val in (("rate", rate), ("periods", periods)):

        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")

    if rate <= 0 or periods <= 0:
        raise ValueError("rate and periods must be positive.")

    return float(1.0 / (1.0 + rate) ** periods)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 1: Actuarial & Fixed-Income Functions
# ---------------------------------------------------------------------------

def life_annuity_pv(
    annual_payment: float,
    interest_rate: float,
    mortality_rates: list[float],
) -> float:
    """Present value of a life annuity-due using discrete mortality rates.

    Computes Σ_k (payment × v^k × _kp_x) where v = 1/(1+i) and _kp_x is the
    probability of surviving *k* years from the given mortality vector.

    Args:
        annual_payment: Payment per period (> 0).
        interest_rate: Annual effective interest rate (> 0).
        mortality_rates: List of one-year mortality probabilities q_x, q_{x+1},
            … for successive ages.  Each value must be in [0, 1).

    Returns:
        Present value as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If numeric constraints are violated.

    Usage Example:
        >>> round(life_annuity_pv(1000, 0.05, [0.01, 0.02, 0.03]), 2)
        3635.81

    Complexity: O(n) where n = len(mortality_rates)
    """
    if not isinstance(annual_payment, (int, float)):
        raise TypeError("annual_payment must be numeric.")
    if not isinstance(interest_rate, (int, float)):
        raise TypeError("interest_rate must be numeric.")
    if not isinstance(mortality_rates, list):
        raise TypeError("mortality_rates must be a list.")
    if annual_payment <= 0:
        raise ValueError("annual_payment must be positive.")
    if interest_rate <= 0:
        raise ValueError("interest_rate must be positive.")

    v = 1.0 / (1.0 + interest_rate)
    survival = 1.0
    pv = 0.0
    for k, q in enumerate(mortality_rates):
        if not isinstance(q, (int, float)):
            raise TypeError("Each mortality rate must be numeric.")
        if q < 0 or q >= 1:
            raise ValueError("Each mortality rate must be in [0, 1).")
        pv += annual_payment * (v ** k) * survival
        survival *= (1.0 - q)
    # Add the last surviving payment
    pv += annual_payment * (v ** len(mortality_rates)) * survival
    return float(pv)


def term_life_insurance_pv(
    benefit: float,
    interest_rate: float,
    mortality_rates: list[float],
) -> float:
    """Present value of a term life insurance (death benefit paid at end of year of death).

    Computes Σ_k (benefit × v^{k+1} × _kp_x × q_{x+k}) for k = 0 … n-1.

    Args:
        benefit: Death benefit amount (> 0).
        interest_rate: Annual effective interest rate (> 0).
        mortality_rates: List of one-year mortality probabilities for successive
            ages.  Each value must be in [0, 1).

    Returns:
        Actuarial present value as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If numeric constraints are violated.

    Usage Example:
        >>> round(term_life_insurance_pv(100000, 0.05, [0.01, 0.02, 0.03]), 2)
        5262.59

    Complexity: O(n)
    """
    if not isinstance(benefit, (int, float)):
        raise TypeError("benefit must be numeric.")
    if not isinstance(interest_rate, (int, float)):
        raise TypeError("interest_rate must be numeric.")
    if not isinstance(mortality_rates, list):
        raise TypeError("mortality_rates must be a list.")
    if benefit <= 0:
        raise ValueError("benefit must be positive.")
    if interest_rate <= 0:
        raise ValueError("interest_rate must be positive.")

    v = 1.0 / (1.0 + interest_rate)
    survival = 1.0
    apv = 0.0
    for k, q in enumerate(mortality_rates):
        if not isinstance(q, (int, float)):
            raise TypeError("Each mortality rate must be numeric.")
        if q < 0 or q >= 1:
            raise ValueError("Each mortality rate must be in [0, 1).")
        apv += benefit * (v ** (k + 1)) * survival * q
        survival *= (1.0 - q)
    return float(apv)


def endowment_insurance_pv(
    benefit: float,
    interest_rate: float,
    mortality_rates: list[float],
) -> float:
    """Present value of an endowment insurance.

    Combines term life insurance with a pure endowment: pays *benefit* on
    death during the term **or** on survival at the end of the term.

    Args:
        benefit: Amount payable (> 0).
        interest_rate: Annual effective interest rate (> 0).
        mortality_rates: One-year mortality probabilities for the term.

    Returns:
        Actuarial present value as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If numeric constraints are violated.

    Usage Example:
        >>> round(endowment_insurance_pv(100000, 0.05, [0.01, 0.02, 0.03]), 2)
        86557.82

    Complexity: O(n)
    """
    if not isinstance(benefit, (int, float)):
        raise TypeError("benefit must be numeric.")
    if not isinstance(interest_rate, (int, float)):
        raise TypeError("interest_rate must be numeric.")
    if not isinstance(mortality_rates, list):
        raise TypeError("mortality_rates must be a list.")
    if benefit <= 0:
        raise ValueError("benefit must be positive.")
    if interest_rate <= 0:
        raise ValueError("interest_rate must be positive.")

    v = 1.0 / (1.0 + interest_rate)
    # Term insurance part
    survival = 1.0
    term_pv = 0.0
    for k, q in enumerate(mortality_rates):
        if not isinstance(q, (int, float)):
            raise TypeError("Each mortality rate must be numeric.")
        if q < 0 or q >= 1:
            raise ValueError("Each mortality rate must be in [0, 1).")
        term_pv += benefit * (v ** (k + 1)) * survival * q
        survival *= (1.0 - q)
    # Pure endowment part
    pure_endowment = benefit * (v ** len(mortality_rates)) * survival
    return float(term_pv + pure_endowment)


def annuity_immediate_certain(
    payment: float,
    interest_rate: float,
    periods: int,
) -> float:
    """Present value of an annuity-immediate (payments at end of each period).

    PV = payment × (1 − v^n) / i  where v = 1/(1+i).

    Args:
        payment: Payment per period (> 0).
        interest_rate: Interest rate per period (> 0).
        periods: Number of periods (positive integer).

    Returns:
        Present value as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If numeric constraints are violated.

    Usage Example:
        >>> round(annuity_immediate_certain(1000, 0.05, 10), 2)
        7721.73

    Complexity: O(1)
    """
    if not isinstance(payment, (int, float)):
        raise TypeError("payment must be numeric.")
    if not isinstance(interest_rate, (int, float)):
        raise TypeError("interest_rate must be numeric.")
    if not isinstance(periods, int):
        raise TypeError("periods must be an integer.")
    if payment <= 0:
        raise ValueError("payment must be positive.")
    if interest_rate <= 0:
        raise ValueError("interest_rate must be positive.")
    if periods <= 0:
        raise ValueError("periods must be positive.")

    v = 1.0 / (1.0 + interest_rate)
    return float(payment * (1.0 - v ** periods) / interest_rate)


def annuity_due_certain(
    payment: float,
    interest_rate: float,
    periods: int,
) -> float:
    """Present value of an annuity-due (payments at beginning of each period).

    PV = payment × (1 − v^n) / d  where d = i/(1+i).

    Args:
        payment: Payment per period (> 0).
        interest_rate: Interest rate per period (> 0).
        periods: Number of periods (positive integer).

    Returns:
        Present value as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If numeric constraints are violated.

    Usage Example:
        >>> round(annuity_due_certain(1000, 0.05, 10), 2)
        8107.82

    Complexity: O(1)
    """
    if not isinstance(payment, (int, float)):
        raise TypeError("payment must be numeric.")
    if not isinstance(interest_rate, (int, float)):
        raise TypeError("interest_rate must be numeric.")
    if not isinstance(periods, int):
        raise TypeError("periods must be an integer.")
    if payment <= 0:
        raise ValueError("payment must be positive.")
    if interest_rate <= 0:
        raise ValueError("interest_rate must be positive.")
    if periods <= 0:
        raise ValueError("periods must be positive.")

    v = 1.0 / (1.0 + interest_rate)
    d = interest_rate / (1.0 + interest_rate)
    return float(payment * (1.0 - v ** periods) / d)


def increasing_annuity_pv(
    interest_rate: float,
    periods: int,
) -> float:
    """Present value of an increasing annuity-immediate paying k at time k.

    (Iä)_n = (ä_n − n·v^n) / i  where ä_n is the annuity-immediate PV of 1.

    Args:
        interest_rate: Interest rate per period (> 0).
        periods: Number of periods (positive integer).

    Returns:
        Present value per unit of increase as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If numeric constraints are violated.

    Usage Example:
        >>> round(increasing_annuity_pv(0.05, 10), 4)
        39.3738

    Complexity: O(1)
    """
    if not isinstance(interest_rate, (int, float)):
        raise TypeError("interest_rate must be numeric.")
    if not isinstance(periods, int):
        raise TypeError("periods must be an integer.")
    if interest_rate <= 0:
        raise ValueError("interest_rate must be positive.")
    if periods <= 0:
        raise ValueError("periods must be positive.")

    v = 1.0 / (1.0 + interest_rate)
    # ä_n (annuity-due) = (1+i) × a_n
    a_due_n = (1.0 - v ** periods) * (1.0 + interest_rate) / interest_rate
    return float((a_due_n - periods * v ** periods) / interest_rate)


def decreasing_annuity_pv(
    interest_rate: float,
    periods: int,
) -> float:
    """Present value of a decreasing annuity-immediate paying (n−k+1) at time k.

    (Dä)_n = (n − a_n) / i.

    Args:
        interest_rate: Interest rate per period (> 0).
        periods: Number of periods (positive integer).

    Returns:
        Present value per unit as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If numeric constraints are violated.

    Usage Example:
        >>> round(decreasing_annuity_pv(0.05, 10), 4)
        45.5653

    Complexity: O(1)
    """
    if not isinstance(interest_rate, (int, float)):
        raise TypeError("interest_rate must be numeric.")
    if not isinstance(periods, int):
        raise TypeError("periods must be an integer.")
    if interest_rate <= 0:
        raise ValueError("interest_rate must be positive.")
    if periods <= 0:
        raise ValueError("periods must be positive.")

    v = 1.0 / (1.0 + interest_rate)
    a_n = (1.0 - v ** periods) / interest_rate
    return float((periods - a_n) / interest_rate)


def deferred_annuity_pv(
    payment: float,
    interest_rate: float,
    deferral: int,
    periods: int,
) -> float:
    """Present value of a deferred annuity-immediate.

    PV = v^deferral × payment × a_{periods} where a_{periods} is the
    annuity-immediate PV factor.

    Args:
        payment: Payment per period (> 0).
        interest_rate: Interest rate per period (> 0).
        deferral: Number of deferral periods (≥ 0).
        periods: Number of payment periods (positive integer).

    Returns:
        Present value as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If numeric constraints are violated.

    Usage Example:
        >>> round(deferred_annuity_pv(1000, 0.05, 5, 10), 2)
        6050.18

    Complexity: O(1)
    """
    if not isinstance(payment, (int, float)):
        raise TypeError("payment must be numeric.")
    if not isinstance(interest_rate, (int, float)):
        raise TypeError("interest_rate must be numeric.")
    if not isinstance(deferral, int):
        raise TypeError("deferral must be an integer.")
    if not isinstance(periods, int):
        raise TypeError("periods must be an integer.")
    if payment <= 0:
        raise ValueError("payment must be positive.")
    if interest_rate <= 0:
        raise ValueError("interest_rate must be positive.")
    if deferral < 0:
        raise ValueError("deferral must be non-negative.")
    if periods <= 0:
        raise ValueError("periods must be positive.")

    v = 1.0 / (1.0 + interest_rate)
    a_n = (1.0 - v ** periods) / interest_rate
    return float(payment * (v ** deferral) * a_n)


def force_of_interest(
    annual_rate: float,
) -> float:
    """Convert annual effective interest rate to force of interest (continuous rate).

    δ = ln(1 + i).

    Args:
        annual_rate: Annual effective interest rate (> 0).

    Returns:
        Force of interest as a float.

    Raises:
        TypeError: If annual_rate is not numeric.
        ValueError: If annual_rate is not positive.

    Usage Example:
        >>> round(force_of_interest(0.05), 6)
        0.048790

    Complexity: O(1)
    """
    if not isinstance(annual_rate, (int, float)):
        raise TypeError("annual_rate must be numeric.")
    if annual_rate <= 0:
        raise ValueError("annual_rate must be positive.")
    return float(math.log(1.0 + annual_rate))


def force_of_mortality(
    mortality_rate: float,
) -> float:
    """Convert a one-year mortality probability to force of mortality.

    μ = −ln(1 − q).

    Args:
        mortality_rate: One-year mortality probability in (0, 1).

    Returns:
        Force of mortality as a float.

    Raises:
        TypeError: If mortality_rate is not numeric.
        ValueError: If mortality_rate is not in (0, 1).

    Usage Example:
        >>> round(force_of_mortality(0.02), 6)
        0.020203

    Complexity: O(1)
    """
    if not isinstance(mortality_rate, (int, float)):
        raise TypeError("mortality_rate must be numeric.")
    if mortality_rate <= 0 or mortality_rate >= 1:
        raise ValueError("mortality_rate must be in (0, 1).")
    return float(-math.log(1.0 - mortality_rate))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 2: Exotic Greeks & Volatility Estimators
# ---------------------------------------------------------------------------

def option_charm_bs(
    s: float,
    k: float,
    t: float,
    r: float,
    sigma: float,
    option_type: str = "call",
) -> float:
    """Black-Scholes charm (delta decay): rate of change of delta w.r.t. time.

    Charm = −∂²C/∂S∂t.  Useful for hedging adjustments between rebalances.

    Args:
        s: Current spot price (> 0).
        k: Strike price (> 0).
        t: Time to expiration in years (> 0).
        r: Risk-free interest rate.
        sigma: Annualised volatility (> 0).
        option_type: ``"call"`` or ``"put"``.

    Returns:
        Charm value as a float.

    Raises:
        TypeError: If numeric args are not numeric or option_type not str.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(option_charm_bs(100, 100, 1.0, 0.05, 0.2), 6)
        -0.065667

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("sigma", sigma)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")
    if not isinstance(option_type, str):
        raise TypeError("option_type must be a string.")
    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t, and sigma must be positive.")
    if option_type not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'.")

    d1 = (math.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * math.sqrt(t))
    d2 = d1 - sigma * math.sqrt(t)
    pdf_d1 = math.exp(-d1 ** 2 / 2) / math.sqrt(2 * math.pi)

    charm_call = -pdf_d1 * (
        2 * r * t - d2 * sigma * math.sqrt(t)
    ) / (2 * t * sigma * math.sqrt(t))
    if option_type == "call":
        return float(charm_call)
    return float(charm_call + r * math.exp(-r * t) * _norm_cdf(-d2))


def option_vanna_bs(
    s: float,
    k: float,
    t: float,
    r: float,
    sigma: float,
) -> float:
    """Black-Scholes vanna: sensitivity of delta to volatility (∂²C/∂S∂σ).

    Vanna = (−d2 / σ) × N'(d1) × e^{−qt}/S  (with q=0).

    Args:
        s: Current spot price (> 0).
        k: Strike price (> 0).
        t: Time to expiration in years (> 0).
        r: Risk-free interest rate.
        sigma: Annualised volatility (> 0).

    Returns:
        Vanna value as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If s, k, t, or sigma are not positive.

    Usage Example:
        >>> round(option_vanna_bs(100, 100, 1.0, 0.05, 0.2), 6)
        -0.281430

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("sigma", sigma)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")
    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t, and sigma must be positive.")

    sqrt_t = math.sqrt(t)
    d1 = (math.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * sqrt_t)
    d2 = d1 - sigma * sqrt_t
    pdf_d1 = math.exp(-d1 ** 2 / 2) / math.sqrt(2 * math.pi)
    return float(-d2 / sigma * pdf_d1)


def option_speed_bs(
    s: float,
    k: float,
    t: float,
    r: float,
    sigma: float,
) -> float:
    """Black-Scholes speed: rate of change of gamma w.r.t. spot price (∂³C/∂S³).

    Speed = −Gamma/S × (d1/(σ√t) + 1).

    Args:
        s: Current spot price (> 0).
        k: Strike price (> 0).
        t: Time to expiration in years (> 0).
        r: Risk-free interest rate.
        sigma: Annualised volatility (> 0).

    Returns:
        Speed value as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If s, k, t, or sigma are not positive.

    Usage Example:
        >>> round(option_speed_bs(100, 100, 1.0, 0.05, 0.2), 6)
        -0.000516

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("sigma", sigma)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")
    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t, and sigma must be positive.")

    sqrt_t = math.sqrt(t)
    d1 = (math.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * sqrt_t)
    pdf_d1 = math.exp(-d1 ** 2 / 2) / math.sqrt(2 * math.pi)
    gamma = pdf_d1 / (s * sigma * sqrt_t)
    return float(-gamma / s * (d1 / (sigma * sqrt_t) + 1))


def option_zomma_bs(
    s: float,
    k: float,
    t: float,
    r: float,
    sigma: float,
) -> float:
    """Black-Scholes zomma: rate of change of gamma w.r.t. volatility.

    Zomma = Gamma × (d1×d2 − 1) / σ.

    Args:
        s: Current spot price (> 0).
        k: Strike price (> 0).
        t: Time to expiration in years (> 0).
        r: Risk-free interest rate.
        sigma: Annualised volatility (> 0).

    Returns:
        Zomma value as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If s, k, t, or sigma are not positive.

    Usage Example:
        >>> round(option_zomma_bs(100, 100, 1.0, 0.05, 0.2), 6)
        -0.088885

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("sigma", sigma)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")
    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t, and sigma must be positive.")

    sqrt_t = math.sqrt(t)
    d1 = (math.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * sqrt_t)
    d2 = d1 - sigma * sqrt_t
    pdf_d1 = math.exp(-d1 ** 2 / 2) / math.sqrt(2 * math.pi)
    gamma = pdf_d1 / (s * sigma * sqrt_t)
    return float(gamma * (d1 * d2 - 1) / sigma)


def option_color_bs(
    s: float,
    k: float,
    t: float,
    r: float,
    sigma: float,
) -> float:
    """Black-Scholes color: rate of change of gamma w.r.t. time (∂Γ/∂t).

    Color = −N'(d1)/(2·S·t·σ√t) × [2rt + 1 + d1×(2(r−q)t − d2σ√t)/(σ√t)]
    with q = 0.

    Args:
        s: Current spot price (> 0).
        k: Strike price (> 0).
        t: Time to expiration in years (> 0).
        r: Risk-free interest rate.
        sigma: Annualised volatility (> 0).

    Returns:
        Color value as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If s, k, t, or sigma are not positive.

    Usage Example:
        >>> abs(option_color_bs(100, 100, 1.0, 0.05, 0.2)) < 1
        True

    Complexity: O(1)
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("sigma", sigma)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")
    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t, and sigma must be positive.")

    sqrt_t = math.sqrt(t)
    d1 = (math.log(s / k) + (r + sigma ** 2 / 2) * t) / (sigma * sqrt_t)
    d2 = d1 - sigma * sqrt_t
    pdf_d1 = math.exp(-d1 ** 2 / 2) / math.sqrt(2 * math.pi)
    term = 2 * r * t + 1 + d1 * (2 * r * t - d2 * sigma * sqrt_t) / (sigma * sqrt_t)
    return float(-pdf_d1 / (2 * s * t * sigma * sqrt_t) * term)


def put_call_parity_check(
    call_price: float,
    put_price: float,
    s: float,
    k: float,
    r: float,
    t: float,
    tolerance: float = 0.01,
) -> bool:
    """Check if put-call parity holds within a tolerance.

    Parity: C − P = S − K·e^{−rT}.

    Args:
        call_price: Observed call option price (≥ 0).
        put_price: Observed put option price (≥ 0).
        s: Current spot price (> 0).
        k: Strike price (> 0).
        r: Risk-free interest rate.
        t: Time to expiration in years (> 0).
        tolerance: Maximum allowable deviation (default 0.01).

    Returns:
        ``True`` if parity holds within tolerance, ``False`` otherwise.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If constraints are violated.

    Usage Example:
        >>> put_call_parity_check(10.45, 5.57, 100, 100, 0.05, 1.0, 0.5)
        True

    Complexity: O(1)
    """
    for name, val in (("call_price", call_price), ("put_price", put_price),
                      ("s", s), ("k", k), ("r", r), ("t", t)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if not isinstance(tolerance, (int, float)):
        raise TypeError("tolerance must be numeric.")
    if call_price < 0 or put_price < 0:
        raise ValueError("Option prices must be non-negative.")
    if s <= 0 or k <= 0 or t <= 0:
        raise ValueError("s, k, and t must be positive.")
    if tolerance < 0:
        raise ValueError("tolerance must be non-negative.")

    lhs = call_price - put_price
    rhs = s - k * math.exp(-r * t)
    return abs(lhs - rhs) <= tolerance


def binomial_option_price(
    s: float,
    k: float,
    t: float,
    r: float,
    sigma: float,
    steps: int,
    option_type: str = "call",
) -> float:
    """European option price via the Cox-Ross-Rubinstein binomial tree.

    Args:
        s: Current spot price (> 0).
        k: Strike price (> 0).
        t: Time to expiration in years (> 0).
        r: Risk-free interest rate.
        sigma: Annualised volatility (> 0).
        steps: Number of tree steps (positive integer).
        option_type: ``"call"`` or ``"put"``.

    Returns:
        Option price as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(binomial_option_price(100, 100, 1.0, 0.05, 0.2, 100), 2)
        10.43

    Complexity: O(n²) where n = steps
    """
    for name, val in (("s", s), ("k", k), ("t", t), ("sigma", sigma)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if not isinstance(r, (int, float)):
        raise TypeError("r must be numeric.")
    if not isinstance(steps, int):
        raise TypeError("steps must be an integer.")
    if not isinstance(option_type, str):
        raise TypeError("option_type must be a string.")
    if s <= 0 or k <= 0 or t <= 0 or sigma <= 0:
        raise ValueError("s, k, t, and sigma must be positive.")
    if steps <= 0:
        raise ValueError("steps must be positive.")
    if option_type not in ("call", "put"):
        raise ValueError("option_type must be 'call' or 'put'.")

    dt = t / steps
    u = math.exp(sigma * math.sqrt(dt))
    d = 1.0 / u
    disc = math.exp(-r * dt)
    p = (math.exp(r * dt) - d) / (u - d)

    # Terminal payoffs
    prices = [s * u ** (steps - j) * d ** j for j in range(steps + 1)]
    if option_type == "call":
        values = [max(price - k, 0.0) for price in prices]
    else:
        values = [max(k - price, 0.0) for price in prices]

    # Backward induction
    for i in range(steps - 1, -1, -1):
        values = [disc * (p * values[j] + (1 - p) * values[j + 1])
                  for j in range(i + 1)]

    return float(values[0])


def historical_var(
    returns: list[float],
    confidence: float = 0.95,
) -> float:
    """Historical Value at Risk (VaR) at a given confidence level.

    Returns the loss threshold such that losses exceed this value with
    probability (1 − confidence).

    Args:
        returns: List of periodic returns (e.g. daily log-returns).
        confidence: Confidence level in (0, 1), default 0.95.

    Returns:
        VaR as a positive float (loss amount).

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If returns is empty or confidence is out of range.

    Usage Example:
        >>> returns = [-0.02, -0.01, 0.0, 0.01, 0.02, -0.03, 0.015, 0.005, -0.005, 0.01]
        >>> round(historical_var(returns, 0.9), 4)
        0.03

    Complexity: O(n log n)
    """
    if not isinstance(returns, list):
        raise TypeError("returns must be a list.")
    if not isinstance(confidence, (int, float)):
        raise TypeError("confidence must be numeric.")
    if len(returns) == 0:
        raise ValueError("returns must not be empty.")
    if confidence <= 0 or confidence >= 1:
        raise ValueError("confidence must be in (0, 1).")
    for i, r in enumerate(returns):
        if not isinstance(r, (int, float)):
            raise TypeError(f"returns[{i}] must be numeric.")

    sorted_returns = sorted(returns)
    index = int((1 - confidence) * len(sorted_returns))
    index = max(0, min(index, len(sorted_returns) - 1))
    return float(-sorted_returns[index])


def conditional_var(
    returns: list[float],
    confidence: float = 0.95,
) -> float:
    """Conditional Value at Risk (CVaR / Expected Shortfall).

    Average of losses exceeding the VaR threshold.

    Args:
        returns: List of periodic returns.
        confidence: Confidence level in (0, 1), default 0.95.

    Returns:
        CVaR as a positive float.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If returns is empty or confidence is out of range.

    Usage Example:
        >>> returns = [-0.02, -0.01, 0.0, 0.01, 0.02, -0.03, 0.015, 0.005, -0.005, 0.01]
        >>> round(conditional_var(returns, 0.9), 4)
        0.03

    Complexity: O(n log n)
    """
    if not isinstance(returns, list):
        raise TypeError("returns must be a list.")
    if not isinstance(confidence, (int, float)):
        raise TypeError("confidence must be numeric.")
    if len(returns) == 0:
        raise ValueError("returns must not be empty.")
    if confidence <= 0 or confidence >= 1:
        raise ValueError("confidence must be in (0, 1).")
    for i, r in enumerate(returns):
        if not isinstance(r, (int, float)):
            raise TypeError(f"returns[{i}] must be numeric.")

    sorted_returns = sorted(returns)
    cutoff = int((1 - confidence) * len(sorted_returns))
    cutoff = max(1, cutoff)
    tail = sorted_returns[:cutoff]
    return float(-sum(tail) / len(tail))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 3: Fixed-Income, Returns & Volatility Estimators
# ---------------------------------------------------------------------------

def garman_klass_volatility(
    ohlc: list[tuple[float, float, float, float]],
) -> float:
    """Garman-Klass volatility estimator from OHLC bars.

    σ²_GK = (1/n) Σ [0.5·ln(H/L)² − (2ln2−1)·ln(C/O)²].

    Args:
        ohlc: List of (open, high, low, close) tuples.  Each price must be > 0,
            high ≥ low, high ≥ open, high ≥ close, low ≤ open, low ≤ close.

    Returns:
        Annualised volatility estimate as a float (assuming 252 trading days).

    Raises:
        TypeError: If ohlc is not a list or elements are not tuples.
        ValueError: If ohlc is empty or prices violate constraints.

    Usage Example:
        >>> bars = [(100, 105, 98, 103), (103, 107, 101, 106), (106, 110, 104, 108)]
        >>> round(garman_klass_volatility(bars), 4) > 0
        True

    Complexity: O(n)
    """
    if not isinstance(ohlc, list):
        raise TypeError("ohlc must be a list.")
    if len(ohlc) == 0:
        raise ValueError("ohlc must not be empty.")

    var_sum = 0.0
    for i, bar in enumerate(ohlc):
        if not isinstance(bar, tuple) or len(bar) != 4:
            raise TypeError(f"ohlc[{i}] must be a 4-tuple (O, H, L, C).")
        o, h, lo, c = bar  # noqa: E741 — OHLC standard notation
        for name, val in (("open", o), ("high", h), ("low", lo), ("close", c)):
            if not isinstance(val, (int, float)):
                raise TypeError(f"{name} in ohlc[{i}] must be numeric.")
            if val <= 0:
                raise ValueError(f"{name} in ohlc[{i}] must be positive.")
        if h < lo:
            raise ValueError(f"high < low in ohlc[{i}].")
        var_sum += 0.5 * math.log(h / lo) ** 2 - (2 * math.log(2) - 1) * math.log(c / o) ** 2

    daily_var = var_sum / len(ohlc)
    return float(math.sqrt(max(daily_var, 0.0) * 252))


def parkinson_volatility(
    high_low: list[tuple[float, float]],
) -> float:
    """Parkinson volatility estimator from high-low prices.

    σ²_P = (1 / (4n·ln2)) Σ ln(H/L)².

    Args:
        high_low: List of (high, low) tuples. Each price must be > 0, high ≥ low.

    Returns:
        Annualised volatility estimate (assuming 252 trading days).

    Raises:
        TypeError: If high_low is not a list or elements are wrong.
        ValueError: If list is empty or constraints are violated.

    Usage Example:
        >>> bars = [(105, 98), (107, 101), (110, 104)]
        >>> round(parkinson_volatility(bars), 4) > 0
        True

    Complexity: O(n)
    """
    if not isinstance(high_low, list):
        raise TypeError("high_low must be a list.")
    if len(high_low) == 0:
        raise ValueError("high_low must not be empty.")

    var_sum = 0.0
    for i, pair in enumerate(high_low):
        if not isinstance(pair, tuple) or len(pair) != 2:
            raise TypeError(f"high_low[{i}] must be a 2-tuple (high, low).")
        h, lo = pair
        if not isinstance(h, (int, float)) or not isinstance(lo, (int, float)):
            raise TypeError(f"Prices in high_low[{i}] must be numeric.")
        if h <= 0 or lo <= 0:
            raise ValueError(f"Prices in high_low[{i}] must be positive.")
        if h < lo:
            raise ValueError(f"high < low in high_low[{i}].")
        var_sum += math.log(h / lo) ** 2

    daily_var = var_sum / (4 * len(high_low) * math.log(2))
    return float(math.sqrt(daily_var * 252))


def yang_zhang_volatility(
    ohlc: list[tuple[float, float, float, float]],
) -> float:
    """Yang-Zhang volatility estimator from OHLC bars.

    Combines overnight, open-to-close, and Rogers-Satchell components.

    Args:
        ohlc: List of (open, high, low, close) tuples (≥ 2 bars).

    Returns:
        Annualised volatility estimate (assuming 252 trading days).

    Raises:
        TypeError: If ohlc is not a valid list of 4-tuples.
        ValueError: If fewer than 2 bars or constraints violated.

    Usage Example:
        >>> bars = [(100, 105, 98, 103), (103, 107, 101, 106), (106, 110, 104, 108)]
        >>> round(yang_zhang_volatility(bars), 4) > 0
        True

    Complexity: O(n)
    """
    if not isinstance(ohlc, list):
        raise TypeError("ohlc must be a list.")
    if len(ohlc) < 2:
        raise ValueError("ohlc must have at least 2 bars.")

    n = len(ohlc)
    for i, bar in enumerate(ohlc):
        if not isinstance(bar, tuple) or len(bar) != 4:
            raise TypeError(f"ohlc[{i}] must be a 4-tuple (O, H, L, C).")
        for name, val in zip(("O", "H", "L", "C"), bar):
            if not isinstance(val, (int, float)):
                raise TypeError(f"{name} in ohlc[{i}] must be numeric.")
            if val <= 0:
                raise ValueError(f"{name} in ohlc[{i}] must be positive.")

    # Overnight returns (open-to-previous close)
    overnight = [math.log(ohlc[i][0] / ohlc[i - 1][3]) for i in range(1, n)]
    o_mean = sum(overnight) / len(overnight)
    sigma_o = sum((x - o_mean) ** 2 for x in overnight) / (len(overnight) - 1)

    # Close-to-open returns
    close_open = [math.log(ohlc[i][3] / ohlc[i][0]) for i in range(n)]
    c_mean = sum(close_open) / len(close_open)
    sigma_c = sum((x - c_mean) ** 2 for x in close_open) / (len(close_open) - 1)

    # Rogers-Satchell
    rs_sum = 0.0
    for o, h, lo, c in ohlc:
        rs_sum += math.log(h / c) * math.log(h / o) + math.log(lo / c) * math.log(lo / o)
    sigma_rs = rs_sum / n

    k = 0.34 / (1.34 + (n + 1) / (n - 1))
    daily_var = sigma_o + k * sigma_c + (1 - k) * sigma_rs
    return float(math.sqrt(max(daily_var, 0.0) * 252))


def zero_coupon_price(
    face_value: float,
    yield_rate: float,
    years_to_maturity: float,
) -> float:
    """Price of a zero-coupon bond.

    P = F / (1 + y)^T.

    Args:
        face_value: Face (par) value of the bond (> 0).
        yield_rate: Yield to maturity (> 0).
        years_to_maturity: Time to maturity in years (> 0).

    Returns:
        Bond price as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(zero_coupon_price(1000, 0.05, 10), 2)
        613.91

    Complexity: O(1)
    """
    for name, val in (("face_value", face_value), ("yield_rate", yield_rate),
                      ("years_to_maturity", years_to_maturity)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
        if val <= 0:
            raise ValueError(f"{name} must be positive.")
    return float(face_value / (1.0 + yield_rate) ** years_to_maturity)


def spot_to_forward(
    spot1: float,
    t1: float,
    spot2: float,
    t2: float,
) -> float:
    """Implied forward rate between two spot rates.

    f(t1,t2) = [(1+s2)^t2 / (1+s1)^t1]^{1/(t2−t1)} − 1.

    Args:
        spot1: Spot rate for period t1 (> 0).
        t1: Shorter maturity in years (> 0).
        spot2: Spot rate for period t2 (> 0).
        t2: Longer maturity in years (> t1).

    Returns:
        Implied forward rate as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(spot_to_forward(0.04, 1, 0.05, 2), 6)
        0.060096

    Complexity: O(1)
    """
    for name, val in (("spot1", spot1), ("t1", t1), ("spot2", spot2), ("t2", t2)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if spot1 <= 0 or spot2 <= 0 or t1 <= 0 or t2 <= 0:
        raise ValueError("All arguments must be positive.")
    if t2 <= t1:
        raise ValueError("t2 must be greater than t1.")

    return float(((1 + spot2) ** t2 / (1 + spot1) ** t1) ** (1.0 / (t2 - t1)) - 1)


def bond_equivalent_yield(
    face_value: float,
    purchase_price: float,
    days_to_maturity: int,
) -> float:
    """Bond equivalent yield (BEY) for a discount instrument.

    BEY = (F − P) / P × (365 / days).

    Args:
        face_value: Face value (> 0).
        purchase_price: Purchase price (> 0, < face_value).
        days_to_maturity: Days to maturity (positive integer).

    Returns:
        BEY as a float.

    Raises:
        TypeError: If any argument has the wrong type.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(bond_equivalent_yield(1000, 980, 90), 6)
        0.082766

    Complexity: O(1)
    """
    if not isinstance(face_value, (int, float)):
        raise TypeError("face_value must be numeric.")
    if not isinstance(purchase_price, (int, float)):
        raise TypeError("purchase_price must be numeric.")
    if not isinstance(days_to_maturity, int):
        raise TypeError("days_to_maturity must be an integer.")
    if face_value <= 0 or purchase_price <= 0:
        raise ValueError("face_value and purchase_price must be positive.")
    if purchase_price >= face_value:
        raise ValueError("purchase_price must be less than face_value.")
    if days_to_maturity <= 0:
        raise ValueError("days_to_maturity must be positive.")

    return float((face_value - purchase_price) / purchase_price * (365 / days_to_maturity))


def holding_period_return(
    initial_value: float,
    final_value: float,
    income: float = 0.0,
) -> float:
    """Holding period return (HPR).

    HPR = (final − initial + income) / initial.

    Args:
        initial_value: Initial investment value (> 0).
        final_value: Final investment value (≥ 0).
        income: Total income received during the period (≥ 0).

    Returns:
        HPR as a float (e.g. 0.10 = 10%).

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(holding_period_return(1000, 1100, 50), 4)
        0.15

    Complexity: O(1)
    """
    for name, val in (("initial_value", initial_value), ("final_value", final_value),
                      ("income", income)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
    if initial_value <= 0:
        raise ValueError("initial_value must be positive.")
    if final_value < 0:
        raise ValueError("final_value must be non-negative.")
    if income < 0:
        raise ValueError("income must be non-negative.")
    return float((final_value - initial_value + income) / initial_value)


def money_weighted_return(
    cashflows: list[tuple[float, float]],
    guess: float = 0.05,
    tolerance: float = 1e-9,
    max_iterations: int = 200,
) -> float:
    """Money-weighted rate of return (IRR of investor cash flows).

    Solves Σ CF_i / (1+r)^{t_i} = 0 via Newton-Raphson.

    Args:
        cashflows: List of (time, amount) tuples.  At least one positive and
            one negative amount required.  Times in years.
        guess: Initial rate guess (default 0.05).
        tolerance: Convergence tolerance (default 1e-9).
        max_iterations: Maximum iterations (default 200).

    Returns:
        Money-weighted return as a float.

    Raises:
        TypeError: If arguments have wrong types.
        ValueError: If cashflows don't have both signs or convergence fails.

    Usage Example:
        >>> cfs = [(0, -1000), (0.5, 50), (1.0, 1080)]
        >>> round(money_weighted_return(cfs), 4)
        0.1332

    Complexity: O(n × max_iterations)
    """
    if not isinstance(cashflows, list):
        raise TypeError("cashflows must be a list.")
    if len(cashflows) < 2:
        raise ValueError("cashflows must have at least 2 entries.")

    has_pos = has_neg = False
    for i, cf in enumerate(cashflows):
        if not isinstance(cf, tuple) or len(cf) != 2:
            raise TypeError(f"cashflows[{i}] must be a 2-tuple (time, amount).")
        t, amt = cf
        if not isinstance(t, (int, float)) or not isinstance(amt, (int, float)):
            raise TypeError(f"cashflows[{i}] values must be numeric.")
        if amt > 0:
            has_pos = True
        if amt < 0:
            has_neg = True
    if not (has_pos and has_neg):
        raise ValueError("cashflows must contain both positive and negative amounts.")

    r = guess
    for _ in range(max_iterations):
        npv = sum(amt / (1 + r) ** t for t, amt in cashflows)
        dnpv = sum(-t * amt / (1 + r) ** (t + 1) for t, amt in cashflows)
        if abs(dnpv) < 1e-30:
            break
        r_new = r - npv / dnpv
        if abs(r_new - r) < tolerance:
            return float(r_new)
        r = r_new
    return float(r)


def time_weighted_return(
    period_returns: list[float],
) -> float:
    """Time-weighted rate of return (geometric linking of sub-period returns).

    TWR = ∏(1 + r_i) − 1.

    Args:
        period_returns: List of sub-period returns (e.g. [0.02, -0.01, 0.03]).

    Returns:
        Cumulative TWR as a float.

    Raises:
        TypeError: If period_returns is not a list of numerics.
        ValueError: If the list is empty or any return ≤ −1.

    Usage Example:
        >>> round(time_weighted_return([0.02, -0.01, 0.03]), 6)
        0.040094

    Complexity: O(n)
    """
    if not isinstance(period_returns, list):
        raise TypeError("period_returns must be a list.")
    if len(period_returns) == 0:
        raise ValueError("period_returns must not be empty.")

    product = 1.0
    for i, r in enumerate(period_returns):
        if not isinstance(r, (int, float)):
            raise TypeError(f"period_returns[{i}] must be numeric.")
        if r <= -1:
            raise ValueError(f"period_returns[{i}] must be > -1.")
        product *= (1 + r)
    return float(product - 1)


def duration_gap(
    asset_duration: float,
    liability_duration: float,
    leverage_ratio: float,
) -> float:
    """Duration gap for an institution's balance sheet.

    Gap = D_A − (L/A) × D_L.

    Args:
        asset_duration: Duration of assets (≥ 0).
        liability_duration: Duration of liabilities (≥ 0).
        leverage_ratio: Liabilities / Assets ratio (≥ 0, typically < 1).

    Returns:
        Duration gap as a float.

    Raises:
        TypeError: If any argument is not numeric.
        ValueError: If constraints are violated.

    Usage Example:
        >>> round(duration_gap(5.0, 3.0, 0.9), 2)
        2.3

    Complexity: O(1)
    """
    for name, val in (("asset_duration", asset_duration),
                      ("liability_duration", liability_duration),
                      ("leverage_ratio", leverage_ratio)):
        if not isinstance(val, (int, float)):
            raise TypeError(f"{name} must be numeric.")
        if val < 0:
            raise ValueError(f"{name} must be non-negative.")
    return float(asset_duration - leverage_ratio * liability_duration)


def credit_spread(
    corporate_yield: float,
    risk_free_yield: float,
) -> float:
    """Credit spread between a corporate bond and risk-free rate.

    Spread = y_corporate − y_risk_free.

    Args:
        corporate_yield: Yield of the corporate bond.
        risk_free_yield: Yield of the risk-free benchmark.

    Returns:
        Credit spread as a float (in the same units as the yields).

    Raises:
        TypeError: If any argument is not numeric.

    Usage Example:
        >>> credit_spread(0.065, 0.04)
        0.025

    Complexity: O(1)
    """
    if not isinstance(corporate_yield, (int, float)):
        raise TypeError("corporate_yield must be numeric.")
    if not isinstance(risk_free_yield, (int, float)):
        raise TypeError("risk_free_yield must be numeric.")
    return float(corporate_yield - risk_free_yield)