"""Tests for fxNumeric.finance_functions."""

import math
from datetime import date, datetime

import pytest

from shortfx.fxDate.date_convertions import date_to_excel_serial, excel_serial_to_date
from shortfx.fxDate.date_evaluations import is_golden_hour, week_year
from shortfx.fxDate.date_operations import date_to_week_label
from shortfx.fxNumeric.finance_functions import (
    accounts_payable_turnover,
    acid_test_ratio,
    annuity_due_certain,
    annuity_due_fv,
    annuity_immediate_certain,
    asset_coverage_ratio,
    asset_turnover,
    binomial_option_price,
    bond_current_yield,
    bond_equivalent_yield,
    bond_yield_to_worst,
    capital_intensity_ratio,
    cash_conversion_cycle,
    cash_conversion_efficiency,
    cash_flow_coverage,
    cash_ratio,
    cash_return_on_assets,
    conditional_var,
    contribution_margin,
    credit_spread,
    days_payable_outstanding,
    debt_service_ratio,
    debt_to_capital,
    debt_to_income,
    decreasing_annuity_pv,
    defensive_interval,
    deferred_annuity_pv,
    degree_of_financial_leverage,
    dividend_payout_ratio,
    dividend_yield,
    dupont_roe,
    duration_gap,
    economic_order_quantity,
    economic_value_added,
    effective_annual_rate,
    effective_duration,
    endowment_insurance_pv,
    equity_multiplier,
    ev_to_ebitda,
    fixed_asset_turnover,
    force_of_interest,
    force_of_mortality,
    free_cash_flow_yield,
    garman_klass_volatility,
    gross_profit_margin,
    historical_var,
    holding_period_return,
    increasing_annuity_pv,
    inflation_adjusted_value,
    interest_burden_ratio,
    interest_coverage_ratio,
    inventory_to_sales,
    inventory_turnover,
    inventory_turnover_ratio,
    levered_beta,
    life_annuity_pv,
    loan_to_value,
    margin_of_safety_pct,
    marginal_cost,
    markdown_percentage,
    markup_percentage,
    modified_dietz_return,
    money_weighted_return,
    net_asset_value,
    net_profit_margin,
    nominal_to_real_rate,
    nopat_margin,
    omega_ratio,
    operating_expense_ratio,
    operating_leverage_degree,
    operating_profit_margin,
    option_charm_bs,
    option_color_bs,
    option_delta_bs,
    option_gamma_bs,
    option_speed_bs,
    option_vanna_bs,
    option_zomma_bs,
    parkinson_volatility,
    payback_period,
    plowback_ratio,
    price_earnings_growth,
    price_to_book,
    price_to_earnings,
    price_to_sales,
    put_call_parity_check,
    quick_ratio,
    receivables_turnover,
    retention_ratio,
    return_on_capital_employed,
    return_on_net_assets,
    sales_growth_rate,
    spot_to_forward,
    sustainable_growth_rate,
    term_life_insurance_pv,
    time_weighted_return,
    times_interest_earned,
    tobin_q_ratio,
    ulcer_index,
    unlevered_beta,
    wacc_two_sources,
    weighted_average_cost_of_debt,
    working_capital,
    working_capital_ratio,
    yang_zhang_volatility,
    zero_coupon_price,
)


class TestPaybackPeriod:

    def test_basic(self):
        assert payback_period(1000, [300, 400, 400, 200]) == pytest.approx(2.75)

    def test_exact_recovery(self):
        # 300 + 400 = 700 => recovered at end of period index 1 (2nd period)
        assert payback_period(700, [300, 400, 200]) == pytest.approx(2.0)

    def test_first_period(self):
        assert payback_period(100, [200, 100]) == pytest.approx(0.5)

    def test_never_recovered(self):
        with pytest.raises(ValueError, match="never fully recovered"):
            payback_period(1000, [100, 100])

    def test_invalid_type(self):
        with pytest.raises(TypeError):
            payback_period("1000", [300])

class TestBlackScholes:

    def test_call_price(self):
        from shortfx.fxNumeric.finance_functions import black_scholes_call

        assert round(black_scholes_call(100, 100, 1, 0.05, 0.2), 2) == 10.45

    def test_put_price(self):
        from shortfx.fxNumeric.finance_functions import black_scholes_put

        assert round(black_scholes_put(100, 100, 1, 0.05, 0.2), 2) == 5.57

    def test_put_call_parity(self):
        from shortfx.fxNumeric.finance_functions import (
            black_scholes_call, black_scholes_put,
        )

        c = black_scholes_call(100, 100, 1, 0.05, 0.2)
        p = black_scholes_put(100, 100, 1, 0.05, 0.2)
        # Put-call parity: C - P = S - K*e^(-rT)
        assert c - p == pytest.approx(100 - 100 * math.exp(-0.05), abs=0.01)

class TestImpliedVolatility:

    def test_round_trip(self):
        from shortfx.fxNumeric.finance_functions import (
            black_scholes_call, implied_volatility,
        )

        price = black_scholes_call(100, 100, 1, 0.05, 0.2)
        iv = implied_volatility(price, 100, 100, 1, 0.05, "call")
        assert round(iv, 2) == 0.2

class TestAltmanZScore:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import altman_z_score

        z = altman_z_score(50, 30, 40, 200, 100, 300, 250)
        assert isinstance(z, float)
        assert z > 0

class TestMacaulayDuration:

    def test_par_bond(self):
        from shortfx.fxNumeric.finance_functions import macaulay_duration_simple

        dur = macaulay_duration_simple(0.05, 0.05, 10)
        # Duration should be positive and less than periods
        assert 0 < dur < 10

class TestBondConvexity:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import bond_convexity

        conv = bond_convexity(0.05, 0.05, 10, 100)
        assert conv > 0

class TestVaR:

    def test_parametric(self):
        from shortfx.fxNumeric.finance_functions import var_parametric

        var = var_parametric(1_000_000, 0.001, 0.02, 0.95)
        assert var > 0

    def test_expected_shortfall_greater(self):
        from shortfx.fxNumeric.finance_functions import (
            var_parametric, expected_shortfall,
        )

        var = var_parametric(1_000_000, 0.001, 0.02, 0.95)
        es = expected_shortfall(1_000_000, 0.001, 0.02, 0.95)
        assert es > var

class TestMortgage:

    def test_total_cost(self):
        from shortfx.fxNumeric.finance_functions import mortgage_total_cost

        total = mortgage_total_cost(200_000, 0.035, 30)
        assert total > 200_000

    def test_remaining_balance_decreases(self):
        from shortfx.fxNumeric.finance_functions import mortgage_remaining_balance

        b60 = mortgage_remaining_balance(200_000, 0.035, 30, 60)
        b120 = mortgage_remaining_balance(200_000, 0.035, 30, 120)
        assert b60 > b120


# ── fxNumeric — Numerical Analysis ───────────────────────────────────────

class TestDdb:

    def test_period_1(self):
        from shortfx.fxNumeric.finance_functions import ddb
        assert round(ddb(10000, 1000, 5, 1), 2) == 4000.0

    def test_period_2(self):
        from shortfx.fxNumeric.finance_functions import ddb
        assert round(ddb(10000, 1000, 5, 2), 2) == 2400.0

    def test_period_exceeds_life(self):
        from shortfx.fxNumeric.finance_functions import ddb

        with pytest.raises(ValueError):
            ddb(10000, 1000, 5, 6)

    def test_negative_cost(self):
        from shortfx.fxNumeric.finance_functions import ddb

        with pytest.raises(ValueError):
            ddb(-100, 0, 5, 1)

class TestIpmt:

    def test_first_period(self):
        from shortfx.fxNumeric.finance_functions import ipmt
        assert round(ipmt(0.1 / 12, 1, 36, 8000), 2) == -66.67

    def test_zero_rate(self):
        from shortfx.fxNumeric.finance_functions import ipmt
        assert ipmt(0, 1, 12, 1200) == 0.0

    def test_invalid_period(self):
        from shortfx.fxNumeric.finance_functions import ipmt

        with pytest.raises(ValueError):
            ipmt(0.05, 0, 12, 1000)

class TestPpmt:

    def test_first_period(self):
        from shortfx.fxNumeric.finance_functions import ppmt
        result = round(ppmt(0.1 / 12, 1, 36, 8000), 2)
        assert result == -191.47

class TestMirr:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import mirr
        assert round(mirr([-100, 50, 60, 70], 0.10, 0.12), 4) == 0.2598

    def test_no_negative(self):
        from shortfx.fxNumeric.finance_functions import mirr

        with pytest.raises(ValueError):
            mirr([10, 20, 30], 0.10, 0.12)

    def test_no_positive(self):
        from shortfx.fxNumeric.finance_functions import mirr

        with pytest.raises(ValueError):
            mirr([-100, -50], 0.10, 0.12)


# ── Statistics ───────────────────────────────────────────────────

class TestTreynorRatio:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import treynor_ratio

        assert treynor_ratio(0.12, 0.03, 1.2) == pytest.approx(0.075)

    def test_zero_beta(self):
        from shortfx.fxNumeric.finance_functions import treynor_ratio

        with pytest.raises(ValueError):
            treynor_ratio(0.12, 0.03, 0)

    def test_type_error(self):
        from shortfx.fxNumeric.finance_functions import treynor_ratio

        with pytest.raises(TypeError):
            treynor_ratio("a", 0.03, 1.2)

class TestCalmarRatio:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import calmar_ratio

        assert calmar_ratio(0.15, 0.10) == pytest.approx(1.5)

    def test_zero_drawdown(self):
        from shortfx.fxNumeric.finance_functions import calmar_ratio

        with pytest.raises(ValueError):
            calmar_ratio(0.15, 0)

class TestKellyCriterion:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import kelly_criterion

        assert kelly_criterion(0.6, 2.0) == pytest.approx(0.4)

    def test_bad_probability(self):
        from shortfx.fxNumeric.finance_functions import kelly_criterion

        with pytest.raises(ValueError):
            kelly_criterion(1.5, 2.0)

class TestBreakevenUnits:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import breakeven_units

        assert breakeven_units(10000, 50, 30) == 500.0

    def test_no_margin(self):
        from shortfx.fxNumeric.finance_functions import breakeven_units

        with pytest.raises(ValueError):
            breakeven_units(10000, 30, 30)

class TestCostOfEquityCapm:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import cost_of_equity_capm

        assert cost_of_equity_capm(0.03, 1.2, 0.10) == pytest.approx(0.114)

    def test_type_error(self):
        from shortfx.fxNumeric.finance_functions import cost_of_equity_capm

        with pytest.raises(TypeError):
            cost_of_equity_capm("a", 1.2, 0.10)

class TestInformationRatio:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import information_ratio

        assert information_ratio(0.12, 0.10, 0.04) == pytest.approx(0.5)

    def test_zero_tracking(self):
        from shortfx.fxNumeric.finance_functions import information_ratio

        with pytest.raises(ValueError):
            information_ratio(0.12, 0.10, 0)


# ── Statistics / ML ──────────────────────────────────────────────────

class TestGordonGrowthPrice:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import gordon_growth_price

        assert gordon_growth_price(2.0, 0.10, 0.05) == 40.0

    def test_growth_ge_rate(self):
        from shortfx.fxNumeric.finance_functions import gordon_growth_price

        with pytest.raises(ValueError):
            gordon_growth_price(2.0, 0.10, 0.10)

    def test_type_error(self):
        from shortfx.fxNumeric.finance_functions import gordon_growth_price

        with pytest.raises(TypeError):
            gordon_growth_price("a", 0.10, 0.05)

class TestEarningsYield:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import earnings_yield

        assert earnings_yield(5, 100) == 0.05

    def test_zero_price(self):
        from shortfx.fxNumeric.finance_functions import earnings_yield

        with pytest.raises(ValueError):
            earnings_yield(5, 0)

class TestMarketCap:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import market_cap

        assert market_cap(150, 1_000_000) == 150_000_000.0

    def test_negative_shares(self):
        from shortfx.fxNumeric.finance_functions import market_cap

        with pytest.raises(ValueError):
            market_cap(150, -1)

class TestEnterpriseValueSimple:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import enterprise_value_simple

        assert enterprise_value_simple(1_000_000, 200_000, 50_000) == 1_150_000.0

    def test_type_error(self):
        from shortfx.fxNumeric.finance_functions import enterprise_value_simple

        with pytest.raises(TypeError):
            enterprise_value_simple("a", 200_000, 50_000)

class TestLeverageRatio:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import leverage_ratio

        assert leverage_ratio(500_000, 200_000) == 2.5

    def test_zero_equity(self):
        from shortfx.fxNumeric.finance_functions import leverage_ratio

        with pytest.raises(ValueError):
            leverage_ratio(500_000, 0)

class TestDividendDiscountPrice:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import dividend_discount_price

        assert round(dividend_discount_price(2.0, 0.10, 5), 4) == 7.5816

    def test_zero_periods(self):
        from shortfx.fxNumeric.finance_functions import dividend_discount_price

        with pytest.raises(ValueError):
            dividend_discount_price(2.0, 0.10, 0)

    def test_type_periods(self):
        from shortfx.fxNumeric.finance_functions import dividend_discount_price

        with pytest.raises(TypeError):
            dividend_discount_price(2.0, 0.10, 5.5)


# ── Statistics / ML ──────────────────────────────────────────────────

class TestContributionMargin:

    def test_basic(self):
        assert contribution_margin(100_000, 60_000) == pytest.approx(40_000)

    def test_zero_variable_costs(self):
        assert contribution_margin(50_000, 0) == pytest.approx(50_000)

    def test_type_error(self):
        with pytest.raises(TypeError):
            contribution_margin("100", 60_000)

class TestMarginOfSafetyPct:

    def test_basic(self):
        assert margin_of_safety_pct(500_000, 300_000) == pytest.approx(40.0)

    def test_zero_breakeven(self):
        assert margin_of_safety_pct(100_000, 0) == pytest.approx(100.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            margin_of_safety_pct("500000", 300_000)

class TestOperatingLeverageDegree:

    def test_basic(self):
        assert operating_leverage_degree(200_000, 80_000) == pytest.approx(2.5)

    def test_zero_income_raises(self):
        with pytest.raises(ValueError):
            operating_leverage_degree(200_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            operating_leverage_degree("200000", 80_000)

class TestCashConversionCycle:

    def test_basic(self):
        assert cash_conversion_cycle(45, 30, 35) == pytest.approx(40)

    def test_negative_result(self):
        assert cash_conversion_cycle(10, 5, 30) == pytest.approx(-15)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cash_conversion_cycle("45", 30, 35)

class TestRetentionRatio:

    def test_basic(self):
        assert retention_ratio(500_000, 200_000) == pytest.approx(0.6)

    def test_no_dividends(self):
        assert retention_ratio(100_000, 0) == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            retention_ratio("500", 200)

class TestSustainableGrowthRate:

    def test_basic(self):
        assert sustainable_growth_rate(0.15, 0.6) == pytest.approx(0.09)

    def test_zero_retention(self):
        assert sustainable_growth_rate(0.15, 0.0) == pytest.approx(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sustainable_growth_rate("0.15", 0.6)


# ── Statistics / ML metrics ──────────────────────────────────────────────────

class TestEquityMultiplier:

    def test_basic(self):
        assert equity_multiplier(500_000, 200_000) == pytest.approx(2.5)

    def test_zero_equity_raises(self):
        with pytest.raises(ValueError):
            equity_multiplier(500_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            equity_multiplier("500000", 200_000)

class TestWorkingCapitalRatio:

    def test_basic(self):
        assert working_capital_ratio(150_000, 100_000) == pytest.approx(1.5)

    def test_zero_liabilities_raises(self):
        with pytest.raises(ValueError):
            working_capital_ratio(150_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            working_capital_ratio("150000", 100_000)

class TestReceivablesTurnover:

    def test_basic(self):
        assert receivables_turnover(1_000_000, 125_000) == pytest.approx(8.0)

    def test_zero_receivables_raises(self):
        with pytest.raises(ValueError):
            receivables_turnover(1_000_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            receivables_turnover("1000000", 125_000)

class TestInventoryTurnoverRatio:

    def test_basic(self):
        assert inventory_turnover_ratio(500_000, 100_000) == pytest.approx(5.0)

    def test_zero_inventory_raises(self):
        with pytest.raises(ValueError):
            inventory_turnover_ratio(500_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            inventory_turnover_ratio("500000", 100_000)

class TestGrossProfitMargin:

    def test_basic(self):
        assert gross_profit_margin(200_000, 120_000) == pytest.approx(40.0)

    def test_zero_revenue_raises(self):
        with pytest.raises(ValueError):
            gross_profit_margin(0, 120_000)

    def test_type_error(self):
        with pytest.raises(TypeError):
            gross_profit_margin("200000", 120_000)

class TestReturnOnNetAssets:

    def test_basic(self):
        assert return_on_net_assets(50_000, 300_000, 100_000) == pytest.approx(0.125)

    def test_zero_net_assets_raises(self):
        with pytest.raises(ValueError):
            return_on_net_assets(50_000, 0, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            return_on_net_assets("50000", 300_000, 100_000)


# ── Statistics / ML metrics ──────────────────────────────────────────────────

class TestFixedAssetTurnover:

    def test_basic(self):
        assert fixed_asset_turnover(1_000_000, 250_000) == pytest.approx(4.0)

    def test_zero_assets_raises(self):
        with pytest.raises(ValueError):
            fixed_asset_turnover(1_000_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            fixed_asset_turnover("1000000", 250_000)

class TestTimesInterestEarned:

    def test_basic(self):
        assert times_interest_earned(500_000, 100_000) == pytest.approx(5.0)

    def test_zero_interest_raises(self):
        with pytest.raises(ValueError):
            times_interest_earned(500_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            times_interest_earned("500000", 100_000)

class TestNominalToRealRate:

    def test_basic(self):
        assert nominal_to_real_rate(0.08, 0.03) == pytest.approx(0.048544, rel=1e-4)

    def test_zero_inflation(self):
        assert nominal_to_real_rate(0.05, 0.0) == pytest.approx(0.05)

    def test_type_error(self):
        with pytest.raises(TypeError):
            nominal_to_real_rate("0.08", 0.03)

class TestOperatingExpenseRatio:

    def test_basic(self):
        assert operating_expense_ratio(80_000, 200_000) == pytest.approx(0.4)

    def test_zero_sales_raises(self):
        with pytest.raises(ValueError):
            operating_expense_ratio(80_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            operating_expense_ratio("80000", 200_000)

class TestAccountsPayableTurnover:

    def test_basic(self):
        assert accounts_payable_turnover(600_000, 100_000) == pytest.approx(6.0)

    def test_zero_payables_raises(self):
        with pytest.raises(ValueError):
            accounts_payable_turnover(600_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            accounts_payable_turnover("600000", 100_000)

class TestDebtServiceRatio:

    def test_basic(self):
        assert debt_service_ratio(300_000, 200_000) == pytest.approx(1.5)

    def test_zero_debt_service_raises(self):
        with pytest.raises(ValueError):
            debt_service_ratio(300_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            debt_service_ratio("300000", 200_000)


# ── Statistics / ML ──────────────────────────────────────────────────────────

class TestDaysPayableOutstanding:

    def test_basic(self):
        assert days_payable_outstanding(50_000, 500_000) == pytest.approx(36.5)

    def test_zero_cogs_raises(self):
        with pytest.raises(ValueError):
            days_payable_outstanding(50_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            days_payable_outstanding("50000", 500_000)

class TestReturnOnCapitalEmployed:

    def test_basic(self):
        assert return_on_capital_employed(100_000, 800_000, 200_000) == pytest.approx(0.16667, rel=1e-3)

    def test_zero_capital_raises(self):
        with pytest.raises(ValueError):
            return_on_capital_employed(100_000, 200_000, 200_000)

    def test_type_error(self):
        with pytest.raises(TypeError):
            return_on_capital_employed("100000", 800_000, 200_000)

class TestPriceToSales:

    def test_basic(self):
        assert price_to_sales(5_000_000, 2_000_000) == pytest.approx(2.5)

    def test_zero_revenue_raises(self):
        with pytest.raises(ValueError):
            price_to_sales(5_000_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            price_to_sales("5000000", 2_000_000)

class TestPlowbackRatio:

    def test_basic(self):
        assert plowback_ratio(2, 5) == pytest.approx(0.6)

    def test_zero_eps_raises(self):
        with pytest.raises(ValueError):
            plowback_ratio(2, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            plowback_ratio("2", 5)

class TestDegreeOfFinancialLeverage:

    def test_basic(self):
        assert degree_of_financial_leverage(500_000, 100_000) == pytest.approx(1.25)

    def test_equal_raises(self):
        with pytest.raises(ValueError):
            degree_of_financial_leverage(100_000, 100_000)

    def test_type_error(self):
        with pytest.raises(TypeError):
            degree_of_financial_leverage("500000", 100_000)

class TestAcidTestRatio:

    def test_basic(self):
        assert acid_test_ratio(50_000, 30_000, 40_000, 80_000) == pytest.approx(1.5)

    def test_zero_liabilities_raises(self):
        with pytest.raises(ValueError):
            acid_test_ratio(50_000, 30_000, 40_000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            acid_test_ratio("50000", 30_000, 40_000, 80_000)


# ── Statistics / ML ──────────────────────────────────────────────────────────

class TestCashFlowCoverage:
    def test_basic(self):
        assert cash_flow_coverage(500_000, 1_000_000) == pytest.approx(0.5)

    def test_negative_ocf(self):
        assert cash_flow_coverage(-100_000, 500_000) == pytest.approx(-0.2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cash_flow_coverage("a", 1)

    def test_zero_debt(self):
        with pytest.raises(ValueError):
            cash_flow_coverage(100, 0)

class TestEconomicValueAdded:
    def test_basic(self):
        assert economic_value_added(150_000, 1_000_000, 0.10) == pytest.approx(50_000.0)

    def test_negative_eva(self):
        assert economic_value_added(50_000, 1_000_000, 0.10) == pytest.approx(-50_000.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            economic_value_added("a", 1, 0.1)

class TestMarginalCost:
    def test_basic(self):
        assert marginal_cost(500, 100) == pytest.approx(5.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            marginal_cost("a", 1)

    def test_zero_quantity(self):
        with pytest.raises(ValueError):
            marginal_cost(100, 0)

class TestCashConversionEfficiency:
    def test_basic(self):
        assert cash_conversion_efficiency(90_000, 100_000) == pytest.approx(0.9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cash_conversion_efficiency("a", 1)

    def test_zero_income(self):
        with pytest.raises(ValueError):
            cash_conversion_efficiency(100, 0)

class TestFreeCashFlowYield:
    def test_basic(self):
        assert free_cash_flow_yield(50_000, 1_000_000) == pytest.approx(0.05)

    def test_type_error(self):
        with pytest.raises(TypeError):
            free_cash_flow_yield("a", 1)

    def test_negative_market_cap(self):
        with pytest.raises(ValueError):
            free_cash_flow_yield(100, -1)

class TestPriceEarningsGrowth:
    def test_basic(self):
        assert price_earnings_growth(20, 10) == pytest.approx(2.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            price_earnings_growth("a", 1)

    def test_zero_growth(self):
        with pytest.raises(ValueError):
            price_earnings_growth(20, 0)


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

class TestCapitalIntensityRatio:
    def test_basic(self):
        assert capital_intensity_ratio(2_000_000, 1_000_000) == pytest.approx(2.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            capital_intensity_ratio("a", 1)

    def test_zero_revenue(self):
        with pytest.raises(ValueError):
            capital_intensity_ratio(100, 0)

class TestAssetCoverageRatio:
    def test_basic(self):
        assert asset_coverage_ratio(5_000_000, 500_000, 1_000_000, 2_000_000) == pytest.approx(1.75)

    def test_type_error(self):
        with pytest.raises(TypeError):
            asset_coverage_ratio("a", 0, 0, 1)

    def test_zero_debt(self):
        with pytest.raises(ValueError):
            asset_coverage_ratio(1, 0, 0, 0)

class TestWaccTwoSources:
    def test_basic(self):
        assert wacc_two_sources(600_000, 0.10, 400_000, 0.05, 0.30) == pytest.approx(0.074, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            wacc_two_sources("a", 0.1, 400_000, 0.05, 0.3)

    def test_zero_total(self):
        with pytest.raises(ValueError):
            wacc_two_sources(0, 0.1, 0, 0.05, 0.3)

class TestInventoryToSales:
    def test_basic(self):
        assert inventory_to_sales(200_000, 1_000_000) == pytest.approx(0.2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            inventory_to_sales("a", 1)

    def test_zero_sales(self):
        with pytest.raises(ValueError):
            inventory_to_sales(100, 0)

class TestNopatMargin:
    def test_basic(self):
        assert nopat_margin(150_000, 1_000_000) == pytest.approx(0.15)

    def test_type_error(self):
        with pytest.raises(TypeError):
            nopat_margin("a", 1)

    def test_zero_revenue(self):
        with pytest.raises(ValueError):
            nopat_margin(100, 0)

class TestCashReturnOnAssets:
    def test_basic(self):
        assert cash_return_on_assets(250_000, 2_000_000) == pytest.approx(0.125)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cash_return_on_assets("a", 1)

    def test_zero_assets(self):
        with pytest.raises(ValueError):
            cash_return_on_assets(100, 0)


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

class TestTobinQRatio:
    def test_basic(self):
        assert tobin_q_ratio(1_500_000, 1_000_000) == pytest.approx(1.5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            tobin_q_ratio("a", 1)

    def test_zero_replacement(self):
        with pytest.raises(ValueError):
            tobin_q_ratio(100, 0)

class TestDefensiveInterval:
    def test_basic(self):
        assert defensive_interval(500_000, 10_000) == pytest.approx(50.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            defensive_interval("a", 1)

    def test_zero_expenses(self):
        with pytest.raises(ValueError):
            defensive_interval(100, 0)

class TestSalesGrowthRate:
    def test_basic(self):
        assert sales_growth_rate(1_250_000, 1_000_000) == pytest.approx(0.25)

    def test_decline(self):
        assert sales_growth_rate(800_000, 1_000_000) == pytest.approx(-0.2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sales_growth_rate("a", 1)

    def test_zero_previous(self):
        with pytest.raises(ValueError):
            sales_growth_rate(100, 0)

class TestDebtToCapital:
    def test_basic(self):
        assert debt_to_capital(400_000, 600_000) == pytest.approx(0.4)

    def test_all_debt(self):
        assert debt_to_capital(100, 0) == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            debt_to_capital("a", 1)

    def test_zero_total(self):
        with pytest.raises(ValueError):
            debt_to_capital(0, 0)

class TestOperatingProfitMargin:
    def test_basic(self):
        assert operating_profit_margin(200_000, 1_000_000) == pytest.approx(0.2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            operating_profit_margin("a", 1)

    def test_zero_revenue(self):
        with pytest.raises(ValueError):
            operating_profit_margin(100, 0)

class TestInterestBurdenRatio:
    def test_basic(self):
        assert interest_burden_ratio(180_000, 200_000) == pytest.approx(0.9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            interest_burden_ratio("a", 1)

    def test_zero_ebit(self):
        with pytest.raises(ValueError):
            interest_burden_ratio(100, 0)


# ---------------------------------------------------------------------------
# Statistics
# ---------------------------------------------------------------------------

class TestIsGoldenHour:
    def test_returns_bool(self):
        result = is_golden_hour(datetime(2024, 6, 21, 6, 30), 40.0, -3.0)
        assert isinstance(result, bool)

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_golden_hour("2024-06-21", 40.0, -3.0)

    def test_invalid_latitude(self):
        with pytest.raises(ValueError):
            is_golden_hour(datetime(2024, 6, 21, 6, 30), 100.0, 0.0)


# ---------------------------------------------------------------------------
# fxNumeric — finance_functions.py
# ---------------------------------------------------------------------------


class TestLoanToValue:
    def test_basic(self):
        assert loan_to_value(180_000, 200_000) == pytest.approx(90.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            loan_to_value("a", 200_000)

    def test_zero_appraised(self):
        with pytest.raises(ValueError):
            loan_to_value(100, 0)

class TestDebtToIncome:
    def test_basic(self):
        assert debt_to_income(1500, 5000) == pytest.approx(30.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            debt_to_income("a", 5000)

    def test_zero_income(self):
        with pytest.raises(ValueError):
            debt_to_income(100, 0)

class TestAnnuityDueFv:
    def test_basic(self):
        result = annuity_due_fv(1000, 0.05, 10)
        assert result == pytest.approx(13206.79, rel=1e-2)

    def test_zero_rate(self):
        assert annuity_due_fv(1000, 0.0, 5) == pytest.approx(5000.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            annuity_due_fv("a", 0.05, 10)

    def test_negative_rate(self):
        with pytest.raises(ValueError):
            annuity_due_fv(1000, -0.05, 10)

class TestWeightedAverageCostOfDebt:

    def test_basic(self):
        result = weighted_average_cost_of_debt([1000, 2000], [0.05, 0.07], 0.3)
        assert round(result, 4) == 0.0443

    def test_zero_tax(self):
        result = weighted_average_cost_of_debt([500, 500], [0.04, 0.06])
        assert round(result, 4) == 0.05

class TestBondYieldToWorst:

    def test_basic(self):
        result = bond_yield_to_worst(1000, 0.06, 950, 10, [5])
        assert abs(result - 0.0708) < 0.005

    def test_no_call(self):
        result = bond_yield_to_worst(1000, 0.06, 950, 10)
        assert result > 0

class TestOptionDeltaBs:

    def test_call_atm(self):
        delta = option_delta_bs(100, 100, 1, 0.05, 0.2)
        assert 0.5 < delta < 0.75

    def test_put(self):
        delta = option_delta_bs(100, 100, 1, 0.05, 0.2, "put")
        assert delta < 0

class TestOptionGammaBs:

    def test_atm(self):
        gamma = option_gamma_bs(100, 100, 1, 0.05, 0.2)
        assert gamma > 0
        assert round(gamma, 6) == 0.018762


# ── fxNumeric ── statistics_functions ───────────────────────────────────

class TestEconomicOrderQuantity:

    def test_basic(self):
        result = economic_order_quantity(10000, 50, 2)
        assert round(result, 2) == 707.11

    def test_negative(self):

        with pytest.raises(ValueError):
            economic_order_quantity(-1, 50, 2)


# ── fxNumeric ── statistics_functions ───────────────────────────────────

class TestBlackScholesGreeks:
    """Black-Scholes vega, theta, rho."""

    def test_option_vega_bs_atm(self):
        from shortfx.fxNumeric.finance_functions import option_vega_bs

        result = option_vega_bs(100, 100, 1.0, 0.05, 0.2)
        assert round(result, 2) == 37.52

    def test_option_vega_bs_type_error(self):
        from shortfx.fxNumeric.finance_functions import option_vega_bs

        with pytest.raises(TypeError):
            option_vega_bs("100", 100, 1.0, 0.05, 0.2)

    def test_option_vega_bs_value_error(self):
        from shortfx.fxNumeric.finance_functions import option_vega_bs

        with pytest.raises(ValueError):
            option_vega_bs(-1, 100, 1.0, 0.05, 0.2)

    def test_option_theta_bs_call(self):
        from shortfx.fxNumeric.finance_functions import option_theta_bs

        result = option_theta_bs(100, 100, 1.0, 0.05, 0.2, "call")
        assert round(result, 2) == -6.41

    def test_option_theta_bs_put(self):
        from shortfx.fxNumeric.finance_functions import option_theta_bs

        result = option_theta_bs(100, 100, 1.0, 0.05, 0.2, "put")
        assert result < 0

    def test_option_theta_bs_invalid_type(self):
        from shortfx.fxNumeric.finance_functions import option_theta_bs

        with pytest.raises(ValueError):
            option_theta_bs(100, 100, 1.0, 0.05, 0.2, "other")

    def test_option_rho_bs_call(self):
        from shortfx.fxNumeric.finance_functions import option_rho_bs

        result = option_rho_bs(100, 100, 1.0, 0.05, 0.2, "call")
        assert round(result, 2) == 53.23

    def test_option_rho_bs_put(self):
        from shortfx.fxNumeric.finance_functions import option_rho_bs

        result = option_rho_bs(100, 100, 1.0, 0.05, 0.2, "put")
        assert result < 0

class TestPerpetuities:
    """Perpetuity and continuous compounding functions."""

    def test_present_value_perpetuity(self):
        from shortfx.fxNumeric.finance_functions import present_value_perpetuity

        assert present_value_perpetuity(100, 0.05) == 2000.0

    def test_present_value_perpetuity_type_error(self):
        from shortfx.fxNumeric.finance_functions import present_value_perpetuity

        with pytest.raises(TypeError):
            present_value_perpetuity("100", 0.05)

    def test_growing_perpetuity_pv(self):
        from shortfx.fxNumeric.finance_functions import growing_perpetuity_pv

        result = growing_perpetuity_pv(100, 0.10, 0.03)
        assert round(result, 2) == 1428.57

    def test_growing_perpetuity_pv_growth_ge_rate(self):
        from shortfx.fxNumeric.finance_functions import growing_perpetuity_pv

        with pytest.raises(ValueError):
            growing_perpetuity_pv(100, 0.05, 0.05)

    def test_growing_annuity_pv(self):
        from shortfx.fxNumeric.finance_functions import growing_annuity_pv

        result = growing_annuity_pv(100, 0.10, 0.03, 20)
        assert round(result, 2) == 1045.05

    def test_continuous_compounding(self):
        from shortfx.fxNumeric.finance_functions import continuous_compounding

        result = continuous_compounding(1000, 0.05, 10)
        assert round(result, 2) == 1648.72

    def test_discount_factor(self):
        from shortfx.fxNumeric.finance_functions import discount_factor

        result = discount_factor(0.05, 10)
        assert round(result, 6) == 0.613913

    def test_discount_factor_type_error(self):
        from shortfx.fxNumeric.finance_functions import discount_factor

        with pytest.raises(TypeError):
            discount_factor("0.05", 10)


# =====================================================================
# fxNumeric — conversion_functions (colour spaces)
# =====================================================================

class TestLifeAnnuityPV:
    """Tests for life_annuity_pv."""

    def test_basic(self):
        result = life_annuity_pv(1000, 0.05, [0.01, 0.02, 0.03])
        assert round(result, 2) == 3635.81

    def test_zero_mortality(self):
        result = life_annuity_pv(1000, 0.05, [0.0, 0.0, 0.0])
        expected = annuity_due_certain(1000, 0.05, 4)
        assert result == pytest.approx(expected, rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            life_annuity_pv("bad", 0.05, [0.01])

    def test_value_error_negative_payment(self):
        with pytest.raises(ValueError):
            life_annuity_pv(-100, 0.05, [0.01])

class TestTermLifeInsurancePV:
    """Tests for term_life_insurance_pv."""

    def test_basic(self):
        result = term_life_insurance_pv(100000, 0.05, [0.01, 0.02, 0.03])
        assert round(result, 2) == 5262.59

    def test_high_mortality(self):
        result = term_life_insurance_pv(100000, 0.05, [0.99])
        assert result == pytest.approx(100000 * 0.99 / 1.05, rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            term_life_insurance_pv("bad", 0.05, [0.01])

class TestEndowmentInsurancePV:
    """Tests for endowment_insurance_pv."""

    def test_basic(self):
        result = endowment_insurance_pv(100000, 0.05, [0.01, 0.02, 0.03])
        assert round(result, 2) == 86557.82

    def test_zero_mortality_equals_discount(self):
        """With q=0 the endowment is a pure discount."""
        result = endowment_insurance_pv(100000, 0.05, [0.0, 0.0])
        expected = 100000 / (1.05 ** 2)
        assert result == pytest.approx(expected, rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            endowment_insurance_pv(100000, 0.05, "bad")

class TestAnnuityImmediateCertain:
    """Tests for annuity_immediate_certain."""

    def test_basic(self):
        assert round(annuity_immediate_certain(1000, 0.05, 10), 2) == 7721.73

    def test_one_period(self):
        result = annuity_immediate_certain(1000, 0.10, 1)
        assert result == pytest.approx(1000 / 1.10, rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            annuity_immediate_certain(1000, 0.05, 2.5)

    def test_value_error(self):
        with pytest.raises(ValueError):
            annuity_immediate_certain(1000, -0.05, 10)

class TestAnnuityDueCertain:
    """Tests for annuity_due_certain."""

    def test_basic(self):
        assert round(annuity_due_certain(1000, 0.05, 10), 2) == 8107.82

    def test_relation_to_immediate(self):
        """Annuity-due = (1+i) × annuity-immediate."""
        immediate = annuity_immediate_certain(1000, 0.05, 10)
        due = annuity_due_certain(1000, 0.05, 10)
        assert due == pytest.approx(immediate * 1.05, rel=1e-9)

class TestIncreasingAnnuityPV:
    """Tests for increasing_annuity_pv."""

    def test_basic(self):
        assert round(increasing_annuity_pv(0.05, 10), 4) == 39.3738

    def test_one_period(self):
        result = increasing_annuity_pv(0.05, 1)
        expected = 1.0 / 1.05  # Pay 1 at time 1
        assert result == pytest.approx(expected, rel=1e-9)

class TestDecreasingAnnuityPV:
    """Tests for decreasing_annuity_pv."""

    def test_basic(self):
        assert round(decreasing_annuity_pv(0.05, 10), 4) == 45.5653

    def test_sum_property(self):
        """(Ia)_n + (Da)_n = (n+1) × a_n."""
        ia = increasing_annuity_pv(0.05, 10)
        da = decreasing_annuity_pv(0.05, 10)
        v = 1.0 / 1.05
        a_n = (1.0 - v ** 10) / 0.05
        assert ia + da == pytest.approx((10 + 1) * a_n, rel=1e-6)

class TestDeferredAnnuityPV:
    """Tests for deferred_annuity_pv."""

    def test_basic(self):
        assert round(deferred_annuity_pv(1000, 0.05, 5, 10), 2) == 6050.18

    def test_zero_deferral(self):
        """Zero deferral equals immediate annuity."""
        deferred = deferred_annuity_pv(1000, 0.05, 0, 10)
        immediate = annuity_immediate_certain(1000, 0.05, 10)
        assert deferred == pytest.approx(immediate, rel=1e-9)

class TestForceOfInterest:
    """Tests for force_of_interest."""

    def test_basic(self):
        assert round(force_of_interest(0.05), 6) == 0.048790

    def test_high_rate(self):
        assert force_of_interest(1.0) == pytest.approx(math.log(2), rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            force_of_interest("bad")

    def test_value_error(self):
        with pytest.raises(ValueError):
            force_of_interest(0)

class TestForceOfMortality:
    """Tests for force_of_mortality."""

    def test_basic(self):
        assert round(force_of_mortality(0.02), 6) == 0.020203

    def test_small_q(self):
        """For small q, μ ≈ q."""
        q = 0.001
        mu = force_of_mortality(q)
        assert mu == pytest.approx(q, abs=1e-5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            force_of_mortality("bad")

    def test_value_error_zero(self):
        with pytest.raises(ValueError):
            force_of_mortality(0)

    def test_value_error_one(self):
        with pytest.raises(ValueError):
            force_of_mortality(1.0)

class TestOptionCharmBS:
    """Tests for option_charm_bs."""

    def test_basic_call(self):
        result = option_charm_bs(100, 100, 1.0, 0.05, 0.2)
        assert round(result, 6) == -0.065667

    def test_put(self):
        result = option_charm_bs(100, 100, 1.0, 0.05, 0.2, "put")
        assert isinstance(result, float)

    def test_type_error(self):
        with pytest.raises(TypeError):
            option_charm_bs("bad", 100, 1.0, 0.05, 0.2)

    def test_value_error(self):
        with pytest.raises(ValueError):
            option_charm_bs(100, 100, 1.0, 0.05, 0.2, "bad")

class TestOptionVannaBS:
    """Tests for option_vanna_bs."""

    def test_basic(self):
        result = option_vanna_bs(100, 100, 1.0, 0.05, 0.2)
        assert round(result, 5) == round(-0.28143, 5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            option_vanna_bs(100, 100, 1.0, "bad", 0.2)

class TestOptionSpeedBS:
    """Tests for option_speed_bs."""

    def test_basic(self):
        result = option_speed_bs(100, 100, 1.0, 0.05, 0.2)
        assert round(result, 6) == -0.000516

    def test_value_error(self):
        with pytest.raises(ValueError):
            option_speed_bs(100, 100, -1.0, 0.05, 0.2)

class TestOptionZommaBS:
    """Tests for option_zomma_bs."""

    def test_basic(self):
        result = option_zomma_bs(100, 100, 1.0, 0.05, 0.2)
        assert round(result, 6) == -0.088885

    def test_type_error(self):
        with pytest.raises(TypeError):
            option_zomma_bs(100, "bad", 1.0, 0.05, 0.2)

class TestOptionColorBS:
    """Tests for option_color_bs."""

    def test_returns_float(self):
        result = option_color_bs(100, 100, 1.0, 0.05, 0.2)
        assert isinstance(result, float)
        assert abs(result) < 1

    def test_value_error(self):
        with pytest.raises(ValueError):
            option_color_bs(-100, 100, 1.0, 0.05, 0.2)

class TestPutCallParityCheck:
    """Tests for put_call_parity_check."""

    def test_passes(self):
        assert put_call_parity_check(10.45, 5.57, 100, 100, 0.05, 1.0, 0.5) is True

    def test_fails(self):
        assert put_call_parity_check(20.0, 5.0, 100, 100, 0.05, 1.0, 0.01) is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            put_call_parity_check("bad", 5, 100, 100, 0.05, 1.0)

class TestBinomialOptionPrice:
    """Tests for binomial_option_price."""

    def test_call(self):
        result = binomial_option_price(100, 100, 1.0, 0.05, 0.2, 100, "call")
        assert round(result, 2) == 10.43

    def test_put(self):
        result = binomial_option_price(100, 100, 1.0, 0.05, 0.2, 100, "put")
        assert result > 0

    def test_put_call_parity(self):
        """Binomial call - put ≈ S - K·e^{-rT}."""
        call = binomial_option_price(100, 100, 1.0, 0.05, 0.2, 200, "call")
        put = binomial_option_price(100, 100, 1.0, 0.05, 0.2, 200, "put")
        expected = 100 - 100 * math.exp(-0.05)
        assert call - put == pytest.approx(expected, abs=0.5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            binomial_option_price(100, 100, 1.0, 0.05, 0.2, 2.5)

class TestHistoricalVar:
    """Tests for historical_var."""

    def test_basic(self):
        rets = [-0.02, -0.01, 0.0, 0.01, 0.02, -0.03, 0.015, 0.005, -0.005, 0.01]
        assert round(historical_var(rets, 0.9), 4) == 0.03

    def test_positive_result(self):
        rets = [-0.05, -0.03, -0.01, 0.01, 0.03]
        assert historical_var(rets, 0.8) > 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            historical_var("bad", 0.95)

    def test_value_error_empty(self):
        with pytest.raises(ValueError):
            historical_var([], 0.95)

class TestConditionalVar:
    """Tests for conditional_var."""

    def test_basic(self):
        rets = [-0.02, -0.01, 0.0, 0.01, 0.02, -0.03, 0.015, 0.005, -0.005, 0.01]
        assert round(conditional_var(rets, 0.9), 4) == 0.03

    def test_cvar_ge_var(self):
        """CVaR should be >= VaR."""
        rets = [-0.05, -0.03, -0.01, 0.01, 0.03, -0.04, 0.02, -0.02, 0.0, 0.01]
        var = historical_var(rets, 0.9)
        cvar = conditional_var(rets, 0.9)
        assert cvar >= var - 1e-10

    def test_value_error(self):
        with pytest.raises(ValueError):
            conditional_var([], 0.95)

class TestGarmanKlassVolatility:
    """Tests for garman_klass_volatility."""

    def test_positive(self):
        bars = [(100, 105, 98, 103), (103, 107, 101, 106), (106, 110, 104, 108)]
        assert garman_klass_volatility(bars) > 0

    def test_type_error_not_list(self):
        with pytest.raises(TypeError):
            garman_klass_volatility("bad")

    def test_value_error_empty(self):
        with pytest.raises(ValueError):
            garman_klass_volatility([])

class TestParkinsonVolatility:
    """Tests for parkinson_volatility."""

    def test_positive(self):
        bars = [(105, 98), (107, 101), (110, 104)]
        assert parkinson_volatility(bars) > 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            parkinson_volatility("bad")

    def test_value_error_high_lt_low(self):
        with pytest.raises(ValueError):
            parkinson_volatility([(90, 100)])

class TestYangZhangVolatility:
    """Tests for yang_zhang_volatility."""

    def test_positive(self):
        bars = [(100, 105, 98, 103), (103, 107, 101, 106), (106, 110, 104, 108)]
        assert yang_zhang_volatility(bars) > 0

    def test_value_error_too_few(self):
        with pytest.raises(ValueError):
            yang_zhang_volatility([(100, 105, 98, 103)])

class TestZeroCouponPrice:
    """Tests for zero_coupon_price."""

    def test_basic(self):
        assert round(zero_coupon_price(1000, 0.05, 10), 2) == 613.91

    def test_one_year(self):
        assert zero_coupon_price(1000, 0.10, 1) == pytest.approx(1000 / 1.10, rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            zero_coupon_price("bad", 0.05, 10)

    def test_value_error(self):
        with pytest.raises(ValueError):
            zero_coupon_price(1000, -0.05, 10)

class TestSpotToForward:
    """Tests for spot_to_forward."""

    def test_basic(self):
        assert round(spot_to_forward(0.04, 1, 0.05, 2), 6) == 0.060096

    def test_equal_spots(self):
        result = spot_to_forward(0.05, 1, 0.05, 2)
        assert result == pytest.approx(0.05, rel=1e-6)

    def test_value_error_t2_le_t1(self):
        with pytest.raises(ValueError):
            spot_to_forward(0.04, 2, 0.05, 1)

class TestBondEquivalentYield:
    """Tests for bond_equivalent_yield."""

    def test_basic(self):
        assert round(bond_equivalent_yield(1000, 980, 90), 6) == 0.082766

    def test_type_error(self):
        with pytest.raises(TypeError):
            bond_equivalent_yield(1000, 980, 90.5)

    def test_value_error_price_ge_face(self):
        with pytest.raises(ValueError):
            bond_equivalent_yield(1000, 1000, 90)

class TestHoldingPeriodReturn:
    """Tests for holding_period_return."""

    def test_basic(self):
        assert round(holding_period_return(1000, 1100, 50), 4) == 0.15

    def test_no_income(self):
        assert holding_period_return(1000, 1100) == pytest.approx(0.10, rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            holding_period_return("bad", 1100)

class TestMoneyWeightedReturn:
    """Tests for money_weighted_return."""

    def test_basic(self):
        cfs = [(0, -1000), (0.5, 50), (1.0, 1080)]
        assert round(money_weighted_return(cfs), 4) == 0.1332

    def test_value_error_all_positive(self):
        with pytest.raises(ValueError):
            money_weighted_return([(0, 100), (1, 200)])

class TestTimeWeightedReturn:
    """Tests for time_weighted_return."""

    def test_basic(self):
        assert round(time_weighted_return([0.02, -0.01, 0.03]), 6) == 0.040094

    def test_single_period(self):
        assert time_weighted_return([0.05]) == pytest.approx(0.05, rel=1e-9)

    def test_value_error_empty(self):
        with pytest.raises(ValueError):
            time_weighted_return([])

    def test_value_error_total_loss(self):
        with pytest.raises(ValueError):
            time_weighted_return([-1.0])

class TestDurationGap:
    """Tests for duration_gap."""

    def test_basic(self):
        assert round(duration_gap(5.0, 3.0, 0.9), 2) == 2.3

    def test_zero_leverage(self):
        assert duration_gap(5.0, 3.0, 0.0) == pytest.approx(5.0, rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            duration_gap("bad", 3.0, 0.9)

class TestCreditSpread:
    """Tests for credit_spread."""

    def test_basic(self):
        assert credit_spread(0.065, 0.04) == pytest.approx(0.025, rel=1e-9)

    def test_negative_spread(self):
        assert credit_spread(0.03, 0.04) == pytest.approx(-0.01, rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            credit_spread("bad", 0.04)

class TestDateToWeekLabel:

    def test_basic(self):
        assert date_to_week_label(date(2024, 1, 8)) == "W02-2024"

    def test_first_week(self):
        label = date_to_week_label(date(2024, 1, 1))
        assert label.startswith("W01")


# ---------------------------------------------------------------------------
# fxNumeric — finance_functions.py
# ---------------------------------------------------------------------------


class TestMarkupPercentage:

    def test_basic(self):
        assert markup_percentage(50, 80) == 60.0

    def test_zero_cost(self):
        with pytest.raises(ValueError):
            markup_percentage(0, 80)

class TestMarkdownPercentage:

    def test_basic(self):
        assert markdown_percentage(100, 75) == 25.0

    def test_zero_original(self):
        with pytest.raises(ValueError):
            markdown_percentage(0, 75)

class TestInflationAdjustedValue:

    def test_basic(self):
        assert round(inflation_adjusted_value(1000, 0.03, 10), 2) == 744.09

    def test_zero_rate(self):
        assert inflation_adjusted_value(1000, 0, 5) == 1000.0

class TestDateToExcelSerial:

    def test_known_date(self):
        assert date_to_excel_serial(date(2023, 1, 1)) == 44927

    def test_roundtrip(self):
        d = date(2024, 6, 15)
        serial = date_to_excel_serial(d)
        assert excel_serial_to_date(serial) == d

    def test_before_1900_raises(self):
        with pytest.raises(ValueError):
            date_to_excel_serial(date(1899, 12, 31))

    def test_type_error(self):
        with pytest.raises(TypeError):
            date_to_excel_serial("2024-01-01")


# ── fxNumeric · finance_functions ─────────────────────────────────────────


class TestNetAssetValue:

    def test_basic(self):
        assert net_asset_value(1_000_000, 200_000, 10_000) == 80.0

    def test_zero_shares(self):
        with pytest.raises(ValueError):
            net_asset_value(100, 50, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            net_asset_value("100", 50, 10)

class TestUnleveredBeta:

    def test_basic(self):
        result = unlevered_beta(1.2, 0.30, 0.5)
        assert round(result, 4) == 0.8889

    def test_zero_de_ratio(self):
        assert unlevered_beta(1.2, 0.30, 0.0) == 1.2

    def test_type_error(self):
        with pytest.raises(TypeError):
            unlevered_beta("1.2", 0.30, 0.5)

class TestLeveredBeta:

    def test_basic(self):
        result = levered_beta(0.8889, 0.30, 0.5)
        assert round(result, 2) == 1.2

    def test_zero_de_ratio(self):
        assert levered_beta(0.8, 0.30, 0.0) == 0.8

    def test_type_error(self):
        with pytest.raises(TypeError):
            levered_beta("0.8", 0.30, 0.5)

class TestBondCurrentYield:

    def test_basic(self):
        result = bond_current_yield(50, 980)
        assert abs(result - 5.102040816326531) < 1e-6

    def test_zero_price(self):
        with pytest.raises(ValueError):
            bond_current_yield(50, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            bond_current_yield("50", 980)

class TestWeekYear:

    def test_boundary_2025(self):
        # 2025-12-29 (Monday) is ISO week 1 of 2026
        assert week_year(date(2025, 12, 29)) == 2026

    def test_mid_year(self):
        assert week_year(date(2025, 6, 15)) == 2025

    def test_jan1_2023(self):
        # 2023-01-01 is a Sunday → ISO year 2022
        assert week_year(date(2023, 1, 1)) == 2022

    def test_type_error(self):
        with pytest.raises(TypeError):
            week_year("2025-06-15")


# ── fxNumeric · finance_functions ────────────────────────────────────


class TestModifiedDietzReturn:

    def test_basic(self):
        result = modified_dietz_return(1000, 1200, [100], [15], 30)
        # V1-V0-CF = 1200-1000-100 = 100; denom = 1000 + 100*(15/30) = 1050
        assert abs(result - 100 / 1050) < 1e-6

    def test_no_cash_flows(self):
        result = modified_dietz_return(1000, 1100, [], [], 30)
        assert abs(result - 0.1) < 1e-6

    def test_list_length_mismatch(self):
        with pytest.raises(ValueError):
            modified_dietz_return(1000, 1200, [100, 200], [15], 30)

    def test_zero_days(self):
        with pytest.raises(ValueError):
            modified_dietz_return(1000, 1200, [], [], 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            modified_dietz_return("1000", 1200, [], [], 30)

class TestOmegaRatio:

    def test_positive_ratio(self):
        # gains: 0.05+0.02+0.03 = 0.10, losses: 0.01+0.02 = 0.03
        result = omega_ratio([0.05, 0.02, -0.01, 0.03, -0.02], 0.0)
        expected = 0.10 / 0.03
        assert abs(result - expected) < 1e-6

    def test_all_above_threshold_raises(self):
        with pytest.raises(ValueError):
            omega_ratio([0.05, 0.02, 0.03], 0.0)

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            omega_ratio([], 0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            omega_ratio("not_a_list", 0.0)

class TestUlcerIndex:

    def test_flat_series(self):
        # No drawdowns
        result = ulcer_index([100, 100, 100, 100])
        assert result == 0.0

    def test_drawdown_series(self):
        result = ulcer_index([100, 105, 102, 98, 103])
        assert result > 0

    def test_monotone_increasing(self):
        result = ulcer_index([100, 110, 120, 130])
        assert result == 0.0

    def test_too_short_raises(self):
        with pytest.raises(ValueError):
            ulcer_index([100])

    def test_type_error(self):
        with pytest.raises(TypeError):
            ulcer_index("not_a_list")

class TestEffectiveDuration:

    def test_basic(self):
        result = effective_duration(102.0, 98.0, 100.0, 0.01)
        assert abs(result - 2.0) < 1e-6

    def test_zero_price_raises(self):
        with pytest.raises(ValueError):
            effective_duration(102, 98, 0, 0.01)

    def test_zero_yield_raises(self):
        with pytest.raises(ValueError):
            effective_duration(102, 98, 100, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            effective_duration("102", 98, 100, 0.01)

class TestWacc:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import wacc
        result = wacc(600_000, 400_000, 0.08, 0.05, 0.30)
        assert round(result, 4) == 0.062

    def test_all_equity(self):
        from shortfx.fxNumeric.finance_functions import wacc
        result = wacc(1_000_000, 0, 0.10, 0.05, 0.30)
        assert round(result, 4) == 0.1

    def test_type_error(self):
        from shortfx.fxNumeric.finance_functions import wacc

        with pytest.raises(TypeError):
            wacc("x", 400_000, 0.08, 0.05, 0.30)

    def test_value_error_negative(self):
        from shortfx.fxNumeric.finance_functions import wacc

        with pytest.raises(ValueError):
            wacc(-1, 400_000, 0.08, 0.05, 0.30)

class TestCapm:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import capm
        result = capm(0.03, 1.2, 0.10)
        assert round(result, 4) == 0.114

    def test_zero_beta(self):
        from shortfx.fxNumeric.finance_functions import capm
        result = capm(0.03, 0.0, 0.10)
        assert round(result, 4) == 0.03

class TestSharpeRatio:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import sharpe_ratio
        result = sharpe_ratio([0.05, 0.02, 0.07, -0.01, 0.04])
        assert round(result, 4) == 1.2465

    def test_with_rfr(self):
        from shortfx.fxNumeric.finance_functions import sharpe_ratio
        result = sharpe_ratio([0.05, 0.02, 0.07, -0.01, 0.04], 0.01)
        assert result > 0

class TestSortinoRatio:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import sortino_ratio
        result = sortino_ratio([0.05, 0.02, 0.07, -0.01, 0.04])
        assert result > 0

    def test_no_downside(self):
        from shortfx.fxNumeric.finance_functions import sortino_ratio
        result = sortino_ratio([0.05, 0.02, 0.07, 0.01, 0.04])
        assert result == float("inf")

class TestDebtToEquity:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import debt_to_equity
        assert debt_to_equity(500_000, 250_000) == 2.0

    def test_zero_equity(self):
        from shortfx.fxNumeric.finance_functions import debt_to_equity

        with pytest.raises(ValueError):
            debt_to_equity(500_000, 0)


# ============================================================================
# STATISTICS CORE
# ============================================================================

class TestRuleOf72:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import rule_of_72
        assert rule_of_72(0.06) == 12.0

    def test_high_rate(self):
        from shortfx.fxNumeric.finance_functions import rule_of_72
        assert rule_of_72(0.12) == 6.0

    def test_zero_rate(self):
        from shortfx.fxNumeric.finance_functions import rule_of_72
        with pytest.raises(ValueError):
            rule_of_72(0)

class TestRealRateOfReturn:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import real_rate_of_return
        assert round(real_rate_of_return(0.08, 0.03), 6) == 0.048544

    def test_zero_inflation(self):
        from shortfx.fxNumeric.finance_functions import real_rate_of_return
        assert round(real_rate_of_return(0.05, 0.0), 10) == 0.05

    def test_invalid_inflation(self):
        from shortfx.fxNumeric.finance_functions import real_rate_of_return
        with pytest.raises(ValueError):
            real_rate_of_return(0.05, -1)

class TestGrossMargin:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import gross_margin
        assert gross_margin(100000, 60000) == 0.4

    def test_zero_revenue(self):
        from shortfx.fxNumeric.finance_functions import gross_margin
        with pytest.raises(ValueError):
            gross_margin(0, 100)

class TestOperatingMargin:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import operating_margin
        assert operating_margin(25000, 100000) == 0.25

    def test_zero_revenue(self):
        from shortfx.fxNumeric.finance_functions import operating_margin
        with pytest.raises(ValueError):
            operating_margin(1000, 0)

class TestCurrentRatio:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import current_ratio
        assert current_ratio(150000, 100000) == 1.5

    def test_zero_liabilities(self):
        from shortfx.fxNumeric.finance_functions import current_ratio
        with pytest.raises(ValueError):
            current_ratio(100, 0)

class TestReturnOnAssets:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import return_on_assets
        assert return_on_assets(50000, 500000) == 0.1

    def test_zero_assets(self):
        from shortfx.fxNumeric.finance_functions import return_on_assets
        with pytest.raises(ValueError):
            return_on_assets(100, 0)

class TestReturnOnEquity:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import return_on_equity
        assert return_on_equity(50000, 200000) == 0.25

    def test_zero_equity(self):
        from shortfx.fxNumeric.finance_functions import return_on_equity
        with pytest.raises(ValueError):
            return_on_equity(100, 0)

class TestEarningsPerShare:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import earnings_per_share
        assert earnings_per_share(1000000, 500000) == 2.0

    def test_zero_shares(self):
        from shortfx.fxNumeric.finance_functions import earnings_per_share
        with pytest.raises(ValueError):
            earnings_per_share(100, 0)


# =====================================================================
# Engineering / Physics
# =====================================================================

class TestPriceToEarnings:

    def test_basic(self):
        assert price_to_earnings(150, 5) == 30.0

    def test_negative_eps(self):
        assert price_to_earnings(50, -2) == -25.0

    def test_zero_eps_raises(self):
        with pytest.raises(ValueError):
            price_to_earnings(50, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            price_to_earnings("50", 5)


# ──────────────────────────────────────────────
# Finance: price_to_book
# ──────────────────────────────────────────────

class TestPriceToBook:

    def test_basic(self):
        assert price_to_book(50, 25) == 2.0

    def test_zero_book_raises(self):
        with pytest.raises(ValueError):
            price_to_book(50, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            price_to_book(50, "25")


# ──────────────────────────────────────────────
# Finance: dividend_yield
# ──────────────────────────────────────────────

class TestDividendYield:

    def test_basic(self):
        assert dividend_yield(2, 50) == 4.0

    def test_zero_price_raises(self):
        with pytest.raises(ValueError):
            dividend_yield(2, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            dividend_yield(2, None)


# ──────────────────────────────────────────────
# Finance: dividend_payout_ratio
# ──────────────────────────────────────────────

class TestDividendPayoutRatio:

    def test_basic(self):
        assert dividend_payout_ratio(40000, 100000) == 40.0

    def test_zero_income_raises(self):
        with pytest.raises(ValueError):
            dividend_payout_ratio(40000, 0)


# ──────────────────────────────────────────────
# Finance: asset_turnover
# ──────────────────────────────────────────────

class TestAssetTurnover:

    def test_basic(self):
        assert asset_turnover(500000, 250000) == 2.0

    def test_zero_assets_raises(self):
        with pytest.raises(ValueError):
            asset_turnover(500000, 0)


# ──────────────────────────────────────────────
# Finance: interest_coverage_ratio
# ──────────────────────────────────────────────

class TestInterestCoverageRatio:

    def test_basic(self):
        assert interest_coverage_ratio(500000, 100000) == 5.0

    def test_zero_interest_raises(self):
        with pytest.raises(ValueError):
            interest_coverage_ratio(500000, 0)


# ──────────────────────────────────────────────
# Finance: quick_ratio
# ──────────────────────────────────────────────

class TestQuickRatio:

    def test_basic(self):
        assert quick_ratio(100000, 30000, 50000) == 1.4

    def test_zero_liabilities_raises(self):
        with pytest.raises(ValueError):
            quick_ratio(100000, 30000, 0)


# ──────────────────────────────────────────────
# Finance: net_profit_margin
# ──────────────────────────────────────────────

class TestNetProfitMargin:

    def test_basic(self):
        assert net_profit_margin(25000, 100000) == 25.0

    def test_zero_revenue_raises(self):
        with pytest.raises(ValueError):
            net_profit_margin(25000, 0)


# ──────────────────────────────────────────────
# Statistics/ML: sigmoid
# ──────────────────────────────────────────────

class TestEvToEbitda:

    def test_basic(self):
        assert ev_to_ebitda(1000000, 200000) == 5.0

    def test_zero_ebitda_raises(self):
        with pytest.raises(ValueError):
            ev_to_ebitda(1000000, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            ev_to_ebitda("1000000", 200000)


# ──────────────────────────────────────────────
# Finance: working_capital
# ──────────────────────────────────────────────

class TestWorkingCapital:

    def test_positive(self):
        assert working_capital(500000, 300000) == 200000

    def test_negative(self):
        assert working_capital(200000, 300000) == -100000

    def test_type_error(self):
        with pytest.raises(TypeError):
            working_capital("500000", 300000)


# ──────────────────────────────────────────────
# Finance: inventory_turnover
# ──────────────────────────────────────────────

class TestInventoryTurnover:

    def test_basic(self):
        assert inventory_turnover(600000, 100000) == 6.0

    def test_zero_inventory_raises(self):
        with pytest.raises(ValueError):
            inventory_turnover(600000, 0)


# ──────────────────────────────────────────────
# Finance: cash_ratio
# ──────────────────────────────────────────────

class TestCashRatio:

    def test_basic(self):
        assert cash_ratio(150000, 300000) == 0.5

    def test_zero_liabilities_raises(self):
        with pytest.raises(ValueError):
            cash_ratio(150000, 0)


# ──────────────────────────────────────────────
# Finance: dupont_roe
# ──────────────────────────────────────────────

class TestDupontRoe:

    def test_basic(self):
        assert dupont_roe(0.10, 1.5, 2.0) == pytest.approx(0.3)

    def test_zero_margin(self):
        assert dupont_roe(0, 1.5, 2.0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            dupont_roe("0.1", 1.5, 2.0)


# ──────────────────────────────────────────────
# Finance: effective_annual_rate
# ──────────────────────────────────────────────

class TestEffectiveAnnualRate:

    def test_monthly(self):
        assert round(effective_annual_rate(0.12, 12), 6) == 0.126825

    def test_annual_single_period(self):
        assert effective_annual_rate(0.10, 1) == pytest.approx(0.10)

    def test_zero_periods_raises(self):
        with pytest.raises(ValueError):
            effective_annual_rate(0.12, 0)


# ──────────────────────────────────────────────
# Statistics/ML: leaky_relu
# ──────────────────────────────────────────────

class TestDebtServiceCoverage:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import debt_service_coverage

        assert debt_service_coverage(120000, 100000) == 1.2

    def test_type_error(self):
        from shortfx.fxNumeric.finance_functions import debt_service_coverage

        with pytest.raises(TypeError):
            debt_service_coverage("a", 100000)

    def test_zero_debt(self):
        from shortfx.fxNumeric.finance_functions import debt_service_coverage

        with pytest.raises(ValueError):
            debt_service_coverage(100000, 0)

class TestBurnRate:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import burn_rate

        assert burn_rate(500000, 350000, 6) == 25000.0

    def test_type_error(self):
        from shortfx.fxNumeric.finance_functions import burn_rate

        with pytest.raises(TypeError):
            burn_rate("a", 350000, 6)

    def test_zero_months(self):
        from shortfx.fxNumeric.finance_functions import burn_rate

        with pytest.raises(ValueError):
            burn_rate(500000, 350000, 0)

class TestMonthsOfRunway:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import months_of_runway

        assert months_of_runway(300000, 25000) == 12.0

    def test_zero_burn(self):
        from shortfx.fxNumeric.finance_functions import months_of_runway

        with pytest.raises(ValueError):
            months_of_runway(300000, 0)

class TestRevenuePerEmployee:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import revenue_per_employee

        assert revenue_per_employee(1000000, 50) == 20000.0

    def test_zero_employees(self):
        from shortfx.fxNumeric.finance_functions import revenue_per_employee

        with pytest.raises(ValueError):
            revenue_per_employee(1000000, 0)

class TestFixedChargeCoverage:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import fixed_charge_coverage

        assert fixed_charge_coverage(200000, 80000) == pytest.approx(3.5)

    def test_type_error(self):
        from shortfx.fxNumeric.finance_functions import fixed_charge_coverage

        with pytest.raises(TypeError):
            fixed_charge_coverage("a", 80000)

class TestOperatingCashFlowRatio:

    def test_basic(self):
        from shortfx.fxNumeric.finance_functions import operating_cash_flow_ratio

        assert operating_cash_flow_ratio(150000, 100000) == 1.5

    def test_zero_liabilities(self):
        from shortfx.fxNumeric.finance_functions import operating_cash_flow_ratio

        with pytest.raises(ValueError):
            operating_cash_flow_ratio(150000, 0)


# ── Statistics / ML ──────────────────────────────────────────────────
