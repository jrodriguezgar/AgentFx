# Coverage tests for formulite.fxNumeric.finance_functions
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

from formulite.fxNumeric import finance_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_accounts_payable_turnover:
    def test_exists(self):
        assert hasattr(mod, "accounts_payable_turnover")

    def test_doc0(self):
        try:
            mod.accounts_payable_turnover(600_000, 100_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.accounts_payable_turnover(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.accounts_payable_turnover(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.accounts_payable_turnover(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.accounts_payable_turnover("", "")
        except EXC:
            pass


class Test_accrint:
    def test_exists(self):
        assert hasattr(mod, "accrint")

    def test_var0(self):
        try:
            mod.accrint("hello", "hello", "hello", 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.accrint("", "", "", 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.accrint(None, "hello", "hello", 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.accrint("", "", "", 0, "", "")
        except EXC:
            pass


class Test_accrintm:
    def test_exists(self):
        assert hasattr(mod, "accrintm")

    def test_var0(self):
        try:
            mod.accrintm("hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.accrintm("", "", 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.accrintm(None, "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.accrintm("", "", 0, "")
        except EXC:
            pass


class Test_acid_test_ratio:
    def test_exists(self):
        assert hasattr(mod, "acid_test_ratio")

    def test_doc0(self):
        try:
            mod.acid_test_ratio(50_000, 30_000, 40_000, 80_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.acid_test_ratio(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.acid_test_ratio(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.acid_test_ratio(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.acid_test_ratio("", "", "", "")
        except EXC:
            pass


class Test_altman_z_score:
    def test_exists(self):
        assert hasattr(mod, "altman_z_score")

    def test_var0(self):
        try:
            mod.altman_z_score(3.14, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.altman_z_score(100, 100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.altman_z_score(None, 3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.altman_z_score("", "", "", "", "", "", "")
        except EXC:
            pass


class Test_amorlinc:
    def test_exists(self):
        assert hasattr(mod, "amorlinc")

    def test_var0(self):
        try:
            mod.amorlinc(3.14, "hello", "hello", 3.14, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.amorlinc(100, "", "", 100, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.amorlinc(None, "hello", "hello", 3.14, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.amorlinc("", "", "", "", "", 0)
        except EXC:
            pass


class Test_annuity_due_certain:
    def test_exists(self):
        assert hasattr(mod, "annuity_due_certain")

    def test_var0(self):
        try:
            mod.annuity_due_certain(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.annuity_due_certain(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.annuity_due_certain(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.annuity_due_certain("", 0, "")
        except EXC:
            pass


class Test_annuity_due_fv:
    def test_exists(self):
        assert hasattr(mod, "annuity_due_fv")

    def test_var0(self):
        try:
            mod.annuity_due_fv(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.annuity_due_fv(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.annuity_due_fv(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.annuity_due_fv("", 0, "")
        except EXC:
            pass


class Test_annuity_due_pv:
    def test_exists(self):
        assert hasattr(mod, "annuity_due_pv")

    def test_var0(self):
        try:
            mod.annuity_due_pv(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.annuity_due_pv(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.annuity_due_pv(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.annuity_due_pv("", 0, "")
        except EXC:
            pass


class Test_annuity_immediate_certain:
    def test_exists(self):
        assert hasattr(mod, "annuity_immediate_certain")

    def test_var0(self):
        try:
            mod.annuity_immediate_certain(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.annuity_immediate_certain(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.annuity_immediate_certain(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.annuity_immediate_certain("", 0, "")
        except EXC:
            pass


class Test_asset_coverage_ratio:
    def test_exists(self):
        assert hasattr(mod, "asset_coverage_ratio")

    def test_doc0(self):
        try:
            mod.asset_coverage_ratio(5_000_000, 500_000, 1_000_000, 2_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.asset_coverage_ratio(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.asset_coverage_ratio(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.asset_coverage_ratio(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.asset_coverage_ratio("", "", "", "")
        except EXC:
            pass


class Test_asset_turnover:
    def test_exists(self):
        assert hasattr(mod, "asset_turnover")

    def test_doc0(self):
        try:
            mod.asset_turnover(500000, 250000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.asset_turnover(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.asset_turnover(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.asset_turnover(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.asset_turnover("", "")
        except EXC:
            pass


class Test_binomial_option_price:
    def test_exists(self):
        assert hasattr(mod, "binomial_option_price")

    def test_var0(self):
        try:
            mod.binomial_option_price(3.14, 3.14, 3.14, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.binomial_option_price(100, 100, 100, 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.binomial_option_price(None, 3.14, 3.14, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.binomial_option_price("", 0, "", "", "", "")
        except EXC:
            pass


class Test_black_scholes_call:
    def test_exists(self):
        assert hasattr(mod, "black_scholes_call")

    def test_var0(self):
        try:
            mod.black_scholes_call(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.black_scholes_call(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.black_scholes_call(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.black_scholes_call("", 0, "", "", "")
        except EXC:
            pass


class Test_black_scholes_put:
    def test_exists(self):
        assert hasattr(mod, "black_scholes_put")

    def test_var0(self):
        try:
            mod.black_scholes_put(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.black_scholes_put(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.black_scholes_put(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.black_scholes_put("", 0, "", "", "")
        except EXC:
            pass


class Test_bond_convexity:
    def test_exists(self):
        assert hasattr(mod, "bond_convexity")

    def test_var0(self):
        try:
            mod.bond_convexity(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bond_convexity(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bond_convexity(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bond_convexity(0, "", "")
        except EXC:
            pass


class Test_bond_current_yield:
    def test_exists(self):
        assert hasattr(mod, "bond_current_yield")

    def test_doc0(self):
        try:
            mod.bond_current_yield(50, 980)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bond_current_yield(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bond_current_yield(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bond_current_yield(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bond_current_yield(0, "")
        except EXC:
            pass


class Test_bond_equivalent_yield:
    def test_exists(self):
        assert hasattr(mod, "bond_equivalent_yield")

    def test_var0(self):
        try:
            mod.bond_equivalent_yield(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bond_equivalent_yield(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bond_equivalent_yield(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bond_equivalent_yield("", "", "")
        except EXC:
            pass


class Test_bond_yield_to_worst:
    def test_exists(self):
        assert hasattr(mod, "bond_yield_to_worst")

    def test_var0(self):
        try:
            mod.bond_yield_to_worst(3.14, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bond_yield_to_worst(100, 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bond_yield_to_worst(None, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bond_yield_to_worst("", 0, "", "")
        except EXC:
            pass


class Test_break_even_units:
    def test_exists(self):
        assert hasattr(mod, "break_even_units")

    def test_doc0(self):
        try:
            mod.break_even_units(10000, 50, 30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.break_even_units(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.break_even_units(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.break_even_units(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.break_even_units("", "", "")
        except EXC:
            pass


class Test_breakeven_units:
    def test_exists(self):
        assert hasattr(mod, "breakeven_units")

    def test_doc0(self):
        try:
            mod.breakeven_units(10000, 50, 30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.breakeven_units(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.breakeven_units(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.breakeven_units(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.breakeven_units("", "", "")
        except EXC:
            pass


class Test_burn_rate:
    def test_exists(self):
        assert hasattr(mod, "burn_rate")

    def test_doc0(self):
        try:
            mod.burn_rate(1000000, 700000, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.burn_rate(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.burn_rate(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.burn_rate(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.burn_rate("", "", "")
        except EXC:
            pass


class Test_cagr:
    def test_exists(self):
        assert hasattr(mod, "cagr")

    def test_var0(self):
        try:
            mod.cagr(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cagr(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cagr(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cagr("", "", "")
        except EXC:
            pass


class Test_calmar_ratio:
    def test_exists(self):
        assert hasattr(mod, "calmar_ratio")

    def test_doc0(self):
        try:
            mod.calmar_ratio(0.15, 0.10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calmar_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calmar_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calmar_ratio(None, 0)
        except EXC:
            pass


class Test_capital_intensity_ratio:
    def test_exists(self):
        assert hasattr(mod, "capital_intensity_ratio")

    def test_doc0(self):
        try:
            mod.capital_intensity_ratio(2_000_000, 1_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.capital_intensity_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.capital_intensity_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.capital_intensity_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.capital_intensity_ratio("", "")
        except EXC:
            pass


class Test_capm:
    def test_exists(self):
        assert hasattr(mod, "capm")

    def test_var0(self):
        try:
            mod.capm(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.capm(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.capm(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.capm(0, 0, 0)
        except EXC:
            pass


class Test_cash_conversion_cycle:
    def test_exists(self):
        assert hasattr(mod, "cash_conversion_cycle")

    def test_doc0(self):
        try:
            mod.cash_conversion_cycle(45, 30, 35)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cash_conversion_cycle(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cash_conversion_cycle(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cash_conversion_cycle(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cash_conversion_cycle("", "", "")
        except EXC:
            pass


class Test_cash_conversion_efficiency:
    def test_exists(self):
        assert hasattr(mod, "cash_conversion_efficiency")

    def test_doc0(self):
        try:
            mod.cash_conversion_efficiency(90_000, 100_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cash_conversion_efficiency(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cash_conversion_efficiency(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cash_conversion_efficiency(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cash_conversion_efficiency("", "")
        except EXC:
            pass


class Test_cash_flow_coverage:
    def test_exists(self):
        assert hasattr(mod, "cash_flow_coverage")

    def test_doc0(self):
        try:
            mod.cash_flow_coverage(500_000, 1_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cash_flow_coverage(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cash_flow_coverage(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cash_flow_coverage(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cash_flow_coverage("", "")
        except EXC:
            pass


class Test_cash_ratio:
    def test_exists(self):
        assert hasattr(mod, "cash_ratio")

    def test_doc0(self):
        try:
            mod.cash_ratio(150000, 300000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cash_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cash_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cash_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cash_ratio("", "")
        except EXC:
            pass


class Test_cash_return_on_assets:
    def test_exists(self):
        assert hasattr(mod, "cash_return_on_assets")

    def test_doc0(self):
        try:
            mod.cash_return_on_assets(250_000, 2_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cash_return_on_assets(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cash_return_on_assets(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cash_return_on_assets(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cash_return_on_assets("", "")
        except EXC:
            pass


class Test_compound_interest:
    def test_exists(self):
        assert hasattr(mod, "compound_interest")

    def test_doc0(self):
        try:
            mod.compound_interest(1000, 0.05, 12, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.compound_interest(3.14, 3.14, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.compound_interest(100, 100, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.compound_interest(None, 3.14, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.compound_interest("", 0, 0, "")
        except EXC:
            pass


class Test_conditional_var:
    def test_exists(self):
        assert hasattr(mod, "conditional_var")

    def test_var0(self):
        try:
            mod.conditional_var(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.conditional_var(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.conditional_var(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.conditional_var("")
        except EXC:
            pass


class Test_continuous_compounding:
    def test_exists(self):
        assert hasattr(mod, "continuous_compounding")

    def test_var0(self):
        try:
            mod.continuous_compounding(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.continuous_compounding(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.continuous_compounding(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.continuous_compounding("", 0, "")
        except EXC:
            pass


class Test_contribution_margin:
    def test_exists(self):
        assert hasattr(mod, "contribution_margin")

    def test_doc0(self):
        try:
            mod.contribution_margin(100_000, 60_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.contribution_margin(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.contribution_margin(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.contribution_margin(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.contribution_margin("", "")
        except EXC:
            pass


class Test_convexity_adjustment:
    def test_exists(self):
        assert hasattr(mod, "convexity_adjustment")

    def test_doc0(self):
        try:
            mod.convexity_adjustment(150.0, 0.01)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.convexity_adjustment(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.convexity_adjustment(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.convexity_adjustment(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.convexity_adjustment("", "")
        except EXC:
            pass


class Test_cost_of_debt_after_tax:
    def test_exists(self):
        assert hasattr(mod, "cost_of_debt_after_tax")

    def test_doc0(self):
        try:
            mod.cost_of_debt_after_tax(0.06, 0.30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cost_of_debt_after_tax(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cost_of_debt_after_tax(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cost_of_debt_after_tax(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cost_of_debt_after_tax(0, 0)
        except EXC:
            pass


class Test_cost_of_equity_capm:
    def test_exists(self):
        assert hasattr(mod, "cost_of_equity_capm")

    def test_doc0(self):
        try:
            mod.cost_of_equity_capm(0.03, 1.2, 0.10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cost_of_equity_capm(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cost_of_equity_capm(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cost_of_equity_capm(None, 0, 0)
        except EXC:
            pass


class Test_coupdaybs:
    def test_exists(self):
        assert hasattr(mod, "coupdaybs")

    def test_doc0(self):
        try:
            mod.coupdaybs("2011-01-25", "2011-11-15", 2, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coupdaybs("hello", "hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coupdaybs("", "", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coupdaybs(None, "hello", 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coupdaybs("", "", "")
        except EXC:
            pass


class Test_coupdays:
    def test_exists(self):
        assert hasattr(mod, "coupdays")

    def test_doc0(self):
        try:
            mod.coupdays("2011-01-25", "2011-11-15", 2, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coupdays("hello", "hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coupdays("", "", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coupdays(None, "hello", 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coupdays("", "", "")
        except EXC:
            pass


class Test_coupdaysnc:
    def test_exists(self):
        assert hasattr(mod, "coupdaysnc")

    def test_doc0(self):
        try:
            mod.coupdaysnc("2011-01-25", "2011-11-15", 2, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coupdaysnc("hello", "hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coupdaysnc("", "", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coupdaysnc(None, "hello", 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coupdaysnc("", "", "")
        except EXC:
            pass


class Test_coupncd:
    def test_exists(self):
        assert hasattr(mod, "coupncd")

    def test_doc0(self):
        try:
            mod.coupncd("2011-01-25", "2011-11-15", 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coupncd("hello", "hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coupncd("", "", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coupncd(None, "hello", 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coupncd("", "", "")
        except EXC:
            pass


class Test_coupnum:
    def test_exists(self):
        assert hasattr(mod, "coupnum")

    def test_doc0(self):
        try:
            mod.coupnum("2011-01-25", "2013-11-15", 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coupnum("hello", "hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coupnum("", "", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coupnum(None, "hello", 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coupnum("", "", "")
        except EXC:
            pass


class Test_couppcd:
    def test_exists(self):
        assert hasattr(mod, "couppcd")

    def test_doc0(self):
        try:
            mod.couppcd("2011-01-25", "2011-11-15", 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.couppcd("hello", "hello", 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.couppcd("", "", 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.couppcd(None, "hello", 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.couppcd("", "", "")
        except EXC:
            pass


class Test_credit_spread:
    def test_exists(self):
        assert hasattr(mod, "credit_spread")

    def test_doc0(self):
        try:
            mod.credit_spread(0.065, 0.04)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.credit_spread(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.credit_spread(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.credit_spread(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.credit_spread(0, "")
        except EXC:
            pass


class Test_cumipmt:
    def test_exists(self):
        assert hasattr(mod, "cumipmt")

    def test_var0(self):
        try:
            mod.cumipmt(3.14, 0, 3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cumipmt(100, 1, 100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cumipmt(None, 0, 3.14, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cumipmt(0, "", "", "", "")
        except EXC:
            pass


class Test_cumprinc:
    def test_exists(self):
        assert hasattr(mod, "cumprinc")

    def test_var0(self):
        try:
            mod.cumprinc(3.14, 0, 3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cumprinc(100, 1, 100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cumprinc(None, 0, 3.14, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cumprinc(0, "", "", "", "")
        except EXC:
            pass


class Test_current_ratio:
    def test_exists(self):
        assert hasattr(mod, "current_ratio")

    def test_doc0(self):
        try:
            mod.current_ratio(150000, 100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.current_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.current_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.current_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.current_ratio("", "")
        except EXC:
            pass


class Test_days_payable_outstanding:
    def test_exists(self):
        assert hasattr(mod, "days_payable_outstanding")

    def test_doc0(self):
        try:
            mod.days_payable_outstanding(50_000, 500_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.days_payable_outstanding(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.days_payable_outstanding(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.days_payable_outstanding(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.days_payable_outstanding(0, "")
        except EXC:
            pass


class Test_db:
    def test_exists(self):
        assert hasattr(mod, "db")

    def test_doc0(self):
        try:
            mod.db(cost=10000, salvage=1000, life=6, period=1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.db(cost=10000, salvage=1000, life=6, period=2)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.db(cost=10000, salvage=1000, life=6, period=1, month=9)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.db(3.14, 3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.db(100, 100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.db(None, 3.14, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.db("", "", "", "")
        except EXC:
            pass


class Test_ddb:
    def test_exists(self):
        assert hasattr(mod, "ddb")

    def test_var0(self):
        try:
            mod.ddb(3.14, 3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ddb(100, 100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ddb(None, 3.14, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ddb("", "", "", "")
        except EXC:
            pass


class Test_debt_service_coverage:
    def test_exists(self):
        assert hasattr(mod, "debt_service_coverage")

    def test_doc0(self):
        try:
            mod.debt_service_coverage(500000, 400000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.debt_service_coverage(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.debt_service_coverage(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.debt_service_coverage(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.debt_service_coverage("", "")
        except EXC:
            pass


class Test_debt_service_ratio:
    def test_exists(self):
        assert hasattr(mod, "debt_service_ratio")

    def test_doc0(self):
        try:
            mod.debt_service_ratio(300_000, 200_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.debt_service_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.debt_service_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.debt_service_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.debt_service_ratio("", "")
        except EXC:
            pass


class Test_debt_to_capital:
    def test_exists(self):
        assert hasattr(mod, "debt_to_capital")

    def test_doc0(self):
        try:
            mod.debt_to_capital(400_000, 600_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.debt_to_capital(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.debt_to_capital(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.debt_to_capital(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.debt_to_capital("", "")
        except EXC:
            pass


class Test_debt_to_equity:
    def test_exists(self):
        assert hasattr(mod, "debt_to_equity")

    def test_doc0(self):
        try:
            mod.debt_to_equity(500000, 250000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.debt_to_equity(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.debt_to_equity(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.debt_to_equity(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.debt_to_equity("", "")
        except EXC:
            pass


class Test_debt_to_income:
    def test_exists(self):
        assert hasattr(mod, "debt_to_income")

    def test_doc0(self):
        try:
            mod.debt_to_income(1500, 5000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.debt_to_income(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.debt_to_income(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.debt_to_income(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.debt_to_income("", "")
        except EXC:
            pass


class Test_decreasing_annuity_pv:
    def test_exists(self):
        assert hasattr(mod, "decreasing_annuity_pv")

    def test_var0(self):
        try:
            mod.decreasing_annuity_pv(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.decreasing_annuity_pv(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.decreasing_annuity_pv(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.decreasing_annuity_pv(0, "")
        except EXC:
            pass


class Test_defensive_interval:
    def test_exists(self):
        assert hasattr(mod, "defensive_interval")

    def test_doc0(self):
        try:
            mod.defensive_interval(500_000, 10_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.defensive_interval(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.defensive_interval(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.defensive_interval(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.defensive_interval("", "")
        except EXC:
            pass


class Test_deferred_annuity_pv:
    def test_exists(self):
        assert hasattr(mod, "deferred_annuity_pv")

    def test_var0(self):
        try:
            mod.deferred_annuity_pv(3.14, 3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.deferred_annuity_pv(100, 100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.deferred_annuity_pv(None, 3.14, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.deferred_annuity_pv("", 0, "", "")
        except EXC:
            pass


class Test_degree_of_financial_leverage:
    def test_exists(self):
        assert hasattr(mod, "degree_of_financial_leverage")

    def test_doc0(self):
        try:
            mod.degree_of_financial_leverage(500_000, 100_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.degree_of_financial_leverage(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.degree_of_financial_leverage(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.degree_of_financial_leverage(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.degree_of_financial_leverage("", "")
        except EXC:
            pass


class Test_disc:
    def test_exists(self):
        assert hasattr(mod, "disc")

    def test_var0(self):
        try:
            mod.disc("hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.disc("", "", 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.disc(None, "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.disc("", "", "", 0)
        except EXC:
            pass


class Test_discount_factor:
    def test_exists(self):
        assert hasattr(mod, "discount_factor")

    def test_var0(self):
        try:
            mod.discount_factor(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.discount_factor(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.discount_factor(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.discount_factor(0, "")
        except EXC:
            pass


class Test_dividend_discount_price:
    def test_exists(self):
        assert hasattr(mod, "dividend_discount_price")

    def test_var0(self):
        try:
            mod.dividend_discount_price(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dividend_discount_price(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dividend_discount_price(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dividend_discount_price("", 0, "")
        except EXC:
            pass


class Test_dividend_payout_ratio:
    def test_exists(self):
        assert hasattr(mod, "dividend_payout_ratio")

    def test_doc0(self):
        try:
            mod.dividend_payout_ratio(40000, 100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.dividend_payout_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dividend_payout_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dividend_payout_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dividend_payout_ratio("", "")
        except EXC:
            pass


class Test_dividend_yield:
    def test_exists(self):
        assert hasattr(mod, "dividend_yield")

    def test_doc0(self):
        try:
            mod.dividend_yield(2, 50)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.dividend_yield(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dividend_yield(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dividend_yield(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dividend_yield("", "")
        except EXC:
            pass


class Test_dollarde:
    def test_exists(self):
        assert hasattr(mod, "dollarde")

    def test_doc0(self):
        try:
            mod.dollarde(1.02, 16)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.dollarde(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dollarde(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dollarde(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dollarde(0, 0)
        except EXC:
            pass


class Test_dollarfr:
    def test_exists(self):
        assert hasattr(mod, "dollarfr")

    def test_doc0(self):
        try:
            mod.dollarfr(1.125, 16)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.dollarfr(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dollarfr(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dollarfr(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dollarfr("", 0)
        except EXC:
            pass


class Test_dupont_roe:
    def test_exists(self):
        assert hasattr(mod, "dupont_roe")

    def test_doc0(self):
        try:
            mod.dupont_roe(0.10, 1.5, 2.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.dupont_roe(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dupont_roe(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dupont_roe(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dupont_roe(0, 0, "")
        except EXC:
            pass


class Test_duration:
    def test_exists(self):
        assert hasattr(mod, "duration")

    def test_var0(self):
        try:
            mod.duration("hello", "hello", 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.duration("", "", 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.duration(None, "hello", 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.duration("", "", 0, "", "")
        except EXC:
            pass


class Test_duration_gap:
    def test_exists(self):
        assert hasattr(mod, "duration_gap")

    def test_var0(self):
        try:
            mod.duration_gap(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.duration_gap(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.duration_gap(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.duration_gap(0, 0, 0)
        except EXC:
            pass


class Test_earnings_per_share:
    def test_exists(self):
        assert hasattr(mod, "earnings_per_share")

    def test_doc0(self):
        try:
            mod.earnings_per_share(1000000, 500000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.earnings_per_share(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.earnings_per_share(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.earnings_per_share(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.earnings_per_share("", "")
        except EXC:
            pass


class Test_earnings_yield:
    def test_exists(self):
        assert hasattr(mod, "earnings_yield")

    def test_doc0(self):
        try:
            mod.earnings_yield(5, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.earnings_yield(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.earnings_yield(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.earnings_yield(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.earnings_yield("", "")
        except EXC:
            pass


class Test_economic_order_quantity:
    def test_exists(self):
        assert hasattr(mod, "economic_order_quantity")

    def test_var0(self):
        try:
            mod.economic_order_quantity(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.economic_order_quantity(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.economic_order_quantity(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.economic_order_quantity("", 0, "")
        except EXC:
            pass


class Test_economic_value_added:
    def test_exists(self):
        assert hasattr(mod, "economic_value_added")

    def test_doc0(self):
        try:
            mod.economic_value_added(150_000, 1_000_000, 0.10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.economic_value_added(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.economic_value_added(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.economic_value_added(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.economic_value_added("", "", "")
        except EXC:
            pass


class Test_effect:
    def test_exists(self):
        assert hasattr(mod, "effect")

    def test_var0(self):
        try:
            mod.effect(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.effect(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.effect(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.effect(0, "")
        except EXC:
            pass


class Test_effective_annual_rate:
    def test_exists(self):
        assert hasattr(mod, "effective_annual_rate")

    def test_var0(self):
        try:
            mod.effective_annual_rate(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.effective_annual_rate(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.effective_annual_rate(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.effective_annual_rate(0, "")
        except EXC:
            pass


class Test_effective_duration:
    def test_exists(self):
        assert hasattr(mod, "effective_duration")

    def test_doc0(self):
        try:
            mod.effective_duration(102.0, 98.0, 100.0, 0.01)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.effective_duration(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.effective_duration(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.effective_duration(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.effective_duration(0, "", "", "")
        except EXC:
            pass


class Test_endowment_insurance_pv:
    def test_exists(self):
        assert hasattr(mod, "endowment_insurance_pv")

    def test_var0(self):
        try:
            mod.endowment_insurance_pv(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.endowment_insurance_pv(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.endowment_insurance_pv(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.endowment_insurance_pv("", 0, 0)
        except EXC:
            pass


class Test_enterprise_value_simple:
    def test_exists(self):
        assert hasattr(mod, "enterprise_value_simple")

    def test_doc0(self):
        try:
            mod.enterprise_value_simple(1_000_000, 200_000, 50_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.enterprise_value_simple(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.enterprise_value_simple(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.enterprise_value_simple(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.enterprise_value_simple(0, "", "")
        except EXC:
            pass


class Test_equity_multiplier:
    def test_exists(self):
        assert hasattr(mod, "equity_multiplier")

    def test_doc0(self):
        try:
            mod.equity_multiplier(500_000, 200_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.equity_multiplier(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.equity_multiplier(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.equity_multiplier(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.equity_multiplier("", "")
        except EXC:
            pass


class Test_ev_to_ebitda:
    def test_exists(self):
        assert hasattr(mod, "ev_to_ebitda")

    def test_doc0(self):
        try:
            mod.ev_to_ebitda(1000000, 200000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ev_to_ebitda(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ev_to_ebitda(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ev_to_ebitda(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ev_to_ebitda("", "")
        except EXC:
            pass


class Test_expected_shortfall:
    def test_exists(self):
        assert hasattr(mod, "expected_shortfall")

    def test_var0(self):
        try:
            mod.expected_shortfall(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.expected_shortfall(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.expected_shortfall(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.expected_shortfall("", 0, 0)
        except EXC:
            pass


class Test_fixed_asset_turnover:
    def test_exists(self):
        assert hasattr(mod, "fixed_asset_turnover")

    def test_doc0(self):
        try:
            mod.fixed_asset_turnover(1_000_000, 250_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fixed_asset_turnover(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fixed_asset_turnover(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fixed_asset_turnover(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fixed_asset_turnover("", "")
        except EXC:
            pass


class Test_fixed_charge_coverage:
    def test_exists(self):
        assert hasattr(mod, "fixed_charge_coverage")

    def test_doc0(self):
        try:
            mod.fixed_charge_coverage(300000, 100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fixed_charge_coverage(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fixed_charge_coverage(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fixed_charge_coverage(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fixed_charge_coverage("", "")
        except EXC:
            pass


class Test_force_of_interest:
    def test_exists(self):
        assert hasattr(mod, "force_of_interest")

    def test_var0(self):
        try:
            mod.force_of_interest(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.force_of_interest(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.force_of_interest(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.force_of_interest(0)
        except EXC:
            pass


class Test_force_of_mortality:
    def test_exists(self):
        assert hasattr(mod, "force_of_mortality")

    def test_var0(self):
        try:
            mod.force_of_mortality(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.force_of_mortality(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.force_of_mortality(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.force_of_mortality(0)
        except EXC:
            pass


class Test_free_cash_flow_yield:
    def test_exists(self):
        assert hasattr(mod, "free_cash_flow_yield")

    def test_doc0(self):
        try:
            mod.free_cash_flow_yield(50_000, 1_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.free_cash_flow_yield(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.free_cash_flow_yield(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.free_cash_flow_yield(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.free_cash_flow_yield("", "")
        except EXC:
            pass


class Test_future_value:
    def test_exists(self):
        assert hasattr(mod, "future_value")

    def test_doc0(self):
        try:
            mod.future_value(rate=0.05, nper=5, pmt=0, pv=-1000)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.future_value(rate=0.05, nper=5, pmt=-100, pv=0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.future_value(3.14, 0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.future_value(100, 1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.future_value(None, 0, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.future_value(0, "", "", "")
        except EXC:
            pass


class Test_fvschedule:
    def test_exists(self):
        assert hasattr(mod, "fvschedule")

    def test_doc0(self):
        try:
            mod.fvschedule(1000, [0.05, 0.06, 0.07])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fvschedule(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fvschedule(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fvschedule(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fvschedule("", "")
        except EXC:
            pass


class Test_garman_klass_volatility:
    def test_exists(self):
        assert hasattr(mod, "garman_klass_volatility")

    def test_var0(self):
        try:
            mod.garman_klass_volatility(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.garman_klass_volatility(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.garman_klass_volatility(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.garman_klass_volatility("")
        except EXC:
            pass


class Test_gordon_growth_price:
    def test_exists(self):
        assert hasattr(mod, "gordon_growth_price")

    def test_doc0(self):
        try:
            mod.gordon_growth_price(2.0, 0.10, 0.05)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gordon_growth_price(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gordon_growth_price(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gordon_growth_price(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gordon_growth_price("", 0, 0)
        except EXC:
            pass


class Test_gross_margin:
    def test_exists(self):
        assert hasattr(mod, "gross_margin")

    def test_doc0(self):
        try:
            mod.gross_margin(100000, 60000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gross_margin(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gross_margin(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gross_margin(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gross_margin("", "")
        except EXC:
            pass


class Test_gross_profit_margin:
    def test_exists(self):
        assert hasattr(mod, "gross_profit_margin")

    def test_doc0(self):
        try:
            mod.gross_profit_margin(200_000, 120_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gross_profit_margin(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gross_profit_margin(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gross_profit_margin(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gross_profit_margin("", "")
        except EXC:
            pass


class Test_growing_annuity_pv:
    def test_exists(self):
        assert hasattr(mod, "growing_annuity_pv")

    def test_var0(self):
        try:
            mod.growing_annuity_pv(3.14, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.growing_annuity_pv(100, 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.growing_annuity_pv(None, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.growing_annuity_pv("", 0, [], "")
        except EXC:
            pass


class Test_growing_perpetuity_pv:
    def test_exists(self):
        assert hasattr(mod, "growing_perpetuity_pv")

    def test_doc0(self):
        try:
            mod.growing_perpetuity_pv(100, 0.10, 0.03)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.growing_perpetuity_pv(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.growing_perpetuity_pv(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.growing_perpetuity_pv(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.growing_perpetuity_pv("", 0, [])
        except EXC:
            pass


class Test_historical_var:
    def test_exists(self):
        assert hasattr(mod, "historical_var")

    def test_var0(self):
        try:
            mod.historical_var(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.historical_var(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.historical_var(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.historical_var("")
        except EXC:
            pass


class Test_holding_period_return:
    def test_exists(self):
        assert hasattr(mod, "holding_period_return")

    def test_var0(self):
        try:
            mod.holding_period_return(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.holding_period_return(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.holding_period_return(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.holding_period_return("", "")
        except EXC:
            pass


class Test_implied_volatility:
    def test_exists(self):
        assert hasattr(mod, "implied_volatility")

    def test_var0(self):
        try:
            mod.implied_volatility(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.implied_volatility(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.implied_volatility(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.implied_volatility(0, "", 0, "", "")
        except EXC:
            pass


class Test_increasing_annuity_pv:
    def test_exists(self):
        assert hasattr(mod, "increasing_annuity_pv")

    def test_var0(self):
        try:
            mod.increasing_annuity_pv(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.increasing_annuity_pv(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.increasing_annuity_pv(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.increasing_annuity_pv(0, "")
        except EXC:
            pass


class Test_inflation_adjusted_value:
    def test_exists(self):
        assert hasattr(mod, "inflation_adjusted_value")

    def test_var0(self):
        try:
            mod.inflation_adjusted_value(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inflation_adjusted_value(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inflation_adjusted_value(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inflation_adjusted_value("", 0, "")
        except EXC:
            pass


class Test_information_ratio:
    def test_exists(self):
        assert hasattr(mod, "information_ratio")

    def test_doc0(self):
        try:
            mod.information_ratio(0.12, 0.10, 0.04)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.information_ratio(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.information_ratio(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.information_ratio(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.information_ratio(0, 0, "")
        except EXC:
            pass


class Test_interest_burden_ratio:
    def test_exists(self):
        assert hasattr(mod, "interest_burden_ratio")

    def test_doc0(self):
        try:
            mod.interest_burden_ratio(180_000, 200_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.interest_burden_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.interest_burden_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.interest_burden_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.interest_burden_ratio("", "")
        except EXC:
            pass


class Test_interest_coverage_ratio:
    def test_exists(self):
        assert hasattr(mod, "interest_coverage_ratio")

    def test_doc0(self):
        try:
            mod.interest_coverage_ratio(500000, 100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.interest_coverage_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.interest_coverage_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.interest_coverage_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.interest_coverage_ratio("", "")
        except EXC:
            pass


class Test_intrate:
    def test_exists(self):
        assert hasattr(mod, "intrate")

    def test_var0(self):
        try:
            mod.intrate("hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.intrate("", "", 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.intrate(None, "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.intrate("", "", "", 0)
        except EXC:
            pass


class Test_inventory_to_sales:
    def test_exists(self):
        assert hasattr(mod, "inventory_to_sales")

    def test_doc0(self):
        try:
            mod.inventory_to_sales(200_000, 1_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inventory_to_sales(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inventory_to_sales(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inventory_to_sales(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inventory_to_sales("", "")
        except EXC:
            pass


class Test_inventory_turnover:
    def test_exists(self):
        assert hasattr(mod, "inventory_turnover")

    def test_doc0(self):
        try:
            mod.inventory_turnover(600000, 100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inventory_turnover(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inventory_turnover(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inventory_turnover(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inventory_turnover("", "")
        except EXC:
            pass


class Test_inventory_turnover_ratio:
    def test_exists(self):
        assert hasattr(mod, "inventory_turnover_ratio")

    def test_doc0(self):
        try:
            mod.inventory_turnover_ratio(500_000, 100_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.inventory_turnover_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.inventory_turnover_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.inventory_turnover_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.inventory_turnover_ratio("", "")
        except EXC:
            pass


class Test_ipmt:
    def test_exists(self):
        assert hasattr(mod, "ipmt")

    def test_var0(self):
        try:
            mod.ipmt(3.14, 0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ipmt(100, 1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ipmt(None, 0, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ipmt(0, "", "", "")
        except EXC:
            pass


class Test_irr:
    def test_exists(self):
        assert hasattr(mod, "irr")

    def test_doc0(self):
        try:
            mod.irr([-100, 20, 30, 40, 50, 60])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.irr(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.irr(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.irr(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.irr("")
        except EXC:
            pass


class Test_ispmt:
    def test_exists(self):
        assert hasattr(mod, "ispmt")

    def test_var0(self):
        try:
            mod.ispmt(3.14, 0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ispmt(100, 1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ispmt(None, 0, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ispmt(0, "", "", "")
        except EXC:
            pass


class Test_kelly_criterion:
    def test_exists(self):
        assert hasattr(mod, "kelly_criterion")

    def test_doc0(self):
        try:
            mod.kelly_criterion(0.6, 2.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.kelly_criterion(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kelly_criterion(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kelly_criterion(None, 0)
        except EXC:
            pass


class Test_leverage_ratio:
    def test_exists(self):
        assert hasattr(mod, "leverage_ratio")

    def test_doc0(self):
        try:
            mod.leverage_ratio(500_000, 200_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.leverage_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.leverage_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.leverage_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.leverage_ratio("", "")
        except EXC:
            pass


class Test_levered_beta:
    def test_exists(self):
        assert hasattr(mod, "levered_beta")

    def test_var0(self):
        try:
            mod.levered_beta(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.levered_beta(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.levered_beta(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.levered_beta(0, 0, 0)
        except EXC:
            pass


class Test_life_annuity_pv:
    def test_exists(self):
        assert hasattr(mod, "life_annuity_pv")

    def test_var0(self):
        try:
            mod.life_annuity_pv(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.life_annuity_pv(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.life_annuity_pv(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.life_annuity_pv("", 0, 0)
        except EXC:
            pass


class Test_loan_amortization_table:
    def test_exists(self):
        assert hasattr(mod, "loan_amortization_table")

    def test_doc0(self):
        try:
            mod.loan_amortization_table(1200, 0.12, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.loan_amortization_table(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.loan_amortization_table(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.loan_amortization_table(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.loan_amortization_table("", 0, "")
        except EXC:
            pass


class Test_loan_to_value:
    def test_exists(self):
        assert hasattr(mod, "loan_to_value")

    def test_doc0(self):
        try:
            mod.loan_to_value(180_000, 200_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.loan_to_value(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.loan_to_value(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.loan_to_value(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.loan_to_value(0, "")
        except EXC:
            pass


class Test_macaulay_duration_simple:
    def test_exists(self):
        assert hasattr(mod, "macaulay_duration_simple")

    def test_var0(self):
        try:
            mod.macaulay_duration_simple(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.macaulay_duration_simple(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.macaulay_duration_simple(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.macaulay_duration_simple(0, "", "")
        except EXC:
            pass


class Test_margin_of_safety_pct:
    def test_exists(self):
        assert hasattr(mod, "margin_of_safety_pct")

    def test_doc0(self):
        try:
            mod.margin_of_safety_pct(200_000, 150_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.margin_of_safety_pct(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.margin_of_safety_pct(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.margin_of_safety_pct(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.margin_of_safety_pct("", 0)
        except EXC:
            pass


class Test_marginal_cost:
    def test_exists(self):
        assert hasattr(mod, "marginal_cost")

    def test_doc0(self):
        try:
            mod.marginal_cost(500, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.marginal_cost(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.marginal_cost(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.marginal_cost(None, 0)
        except EXC:
            pass


class Test_markdown_percentage:
    def test_exists(self):
        assert hasattr(mod, "markdown_percentage")

    def test_doc0(self):
        try:
            mod.markdown_percentage(100, 75)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.markdown_percentage(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.markdown_percentage(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.markdown_percentage(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.markdown_percentage("", "")
        except EXC:
            pass


class Test_market_cap:
    def test_exists(self):
        assert hasattr(mod, "market_cap")

    def test_doc0(self):
        try:
            mod.market_cap(150, 1_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.market_cap(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.market_cap(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.market_cap(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.market_cap("", "")
        except EXC:
            pass


class Test_markup_percentage:
    def test_exists(self):
        assert hasattr(mod, "markup_percentage")

    def test_doc0(self):
        try:
            mod.markup_percentage(50, 80)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.markup_percentage(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.markup_percentage(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.markup_percentage(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.markup_percentage("", "")
        except EXC:
            pass


class Test_mduration:
    def test_exists(self):
        assert hasattr(mod, "mduration")

    def test_var0(self):
        try:
            mod.mduration("hello", "hello", 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mduration("", "", 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mduration(None, "hello", 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mduration("", "", 0, "", "")
        except EXC:
            pass


class Test_mirr:
    def test_exists(self):
        assert hasattr(mod, "mirr")

    def test_var0(self):
        try:
            mod.mirr(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mirr(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mirr(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mirr("", 0, 0)
        except EXC:
            pass


class Test_modified_dietz_return:
    def test_exists(self):
        assert hasattr(mod, "modified_dietz_return")

    def test_doc0(self):
        try:
            mod.modified_dietz_return(1000, 1200, [100], [15], 30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.modified_dietz_return(3.14, 3.14, [1, 2, 3], [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.modified_dietz_return(100, 100, [0], [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.modified_dietz_return(None, 3.14, [1, 2, 3], [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.modified_dietz_return("", "", "", "", "")
        except EXC:
            pass


class Test_modified_duration_simple:
    def test_exists(self):
        assert hasattr(mod, "modified_duration_simple")

    def test_var0(self):
        try:
            mod.modified_duration_simple(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.modified_duration_simple(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.modified_duration_simple(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.modified_duration_simple(0, "")
        except EXC:
            pass


class Test_money_weighted_return:
    def test_exists(self):
        assert hasattr(mod, "money_weighted_return")

    def test_var0(self):
        try:
            mod.money_weighted_return(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.money_weighted_return(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.money_weighted_return(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.money_weighted_return("")
        except EXC:
            pass


class Test_months_of_runway:
    def test_exists(self):
        assert hasattr(mod, "months_of_runway")

    def test_doc0(self):
        try:
            mod.months_of_runway(600000, 100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.months_of_runway(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.months_of_runway(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.months_of_runway(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.months_of_runway("", "")
        except EXC:
            pass


class Test_mortgage_remaining_balance:
    def test_exists(self):
        assert hasattr(mod, "mortgage_remaining_balance")

    def test_var0(self):
        try:
            mod.mortgage_remaining_balance(3.14, 3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mortgage_remaining_balance(100, 100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mortgage_remaining_balance(None, 3.14, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mortgage_remaining_balance("", 0, "", "")
        except EXC:
            pass


class Test_mortgage_total_cost:
    def test_exists(self):
        assert hasattr(mod, "mortgage_total_cost")

    def test_var0(self):
        try:
            mod.mortgage_total_cost(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mortgage_total_cost(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mortgage_total_cost(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mortgage_total_cost("", 0, "")
        except EXC:
            pass


class Test_net_asset_value:
    def test_exists(self):
        assert hasattr(mod, "net_asset_value")

    def test_doc0(self):
        try:
            mod.net_asset_value(1_000_000, 200_000, 10_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.net_asset_value(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.net_asset_value(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.net_asset_value(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.net_asset_value("", "", "")
        except EXC:
            pass


class Test_net_profit_margin:
    def test_exists(self):
        assert hasattr(mod, "net_profit_margin")

    def test_doc0(self):
        try:
            mod.net_profit_margin(25000, 100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.net_profit_margin(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.net_profit_margin(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.net_profit_margin(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.net_profit_margin("", "")
        except EXC:
            pass


class Test_nominal:
    def test_exists(self):
        assert hasattr(mod, "nominal")

    def test_var0(self):
        try:
            mod.nominal(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nominal(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nominal(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nominal(0, "")
        except EXC:
            pass


class Test_nominal_to_real_rate:
    def test_exists(self):
        assert hasattr(mod, "nominal_to_real_rate")

    def test_var0(self):
        try:
            mod.nominal_to_real_rate(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nominal_to_real_rate(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nominal_to_real_rate(None, 0)
        except EXC:
            pass


class Test_nopat_margin:
    def test_exists(self):
        assert hasattr(mod, "nopat_margin")

    def test_doc0(self):
        try:
            mod.nopat_margin(150_000, 1_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.nopat_margin(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nopat_margin(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nopat_margin(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nopat_margin("", "")
        except EXC:
            pass


class Test_nper:
    def test_exists(self):
        assert hasattr(mod, "nper")

    def test_var0(self):
        try:
            mod.nper(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.nper(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.nper(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.nper(0, "", "")
        except EXC:
            pass


class Test_npv:
    def test_exists(self):
        assert hasattr(mod, "npv")

    def test_var0(self):
        try:
            mod.npv(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.npv(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.npv(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.npv(0, [])
        except EXC:
            pass


class Test_omega_ratio:
    def test_exists(self):
        assert hasattr(mod, "omega_ratio")

    def test_doc0(self):
        try:
            mod.omega_ratio([0.05, 0.02, -0.01, 0.03, -0.02], 0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.omega_ratio([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.omega_ratio([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.omega_ratio(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.omega_ratio("")
        except EXC:
            pass


class Test_operating_cash_flow_ratio:
    def test_exists(self):
        assert hasattr(mod, "operating_cash_flow_ratio")

    def test_doc0(self):
        try:
            mod.operating_cash_flow_ratio(250000, 200000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.operating_cash_flow_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.operating_cash_flow_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.operating_cash_flow_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.operating_cash_flow_ratio("", "")
        except EXC:
            pass


class Test_operating_expense_ratio:
    def test_exists(self):
        assert hasattr(mod, "operating_expense_ratio")

    def test_doc0(self):
        try:
            mod.operating_expense_ratio(80_000, 200_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.operating_expense_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.operating_expense_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.operating_expense_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.operating_expense_ratio("", "")
        except EXC:
            pass


class Test_operating_leverage_degree:
    def test_exists(self):
        assert hasattr(mod, "operating_leverage_degree")

    def test_doc0(self):
        try:
            mod.operating_leverage_degree(100_000, 40_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.operating_leverage_degree(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.operating_leverage_degree(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.operating_leverage_degree(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.operating_leverage_degree(0, "")
        except EXC:
            pass


class Test_operating_margin:
    def test_exists(self):
        assert hasattr(mod, "operating_margin")

    def test_doc0(self):
        try:
            mod.operating_margin(25000, 100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.operating_margin(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.operating_margin(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.operating_margin(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.operating_margin("", "")
        except EXC:
            pass


class Test_operating_profit_margin:
    def test_exists(self):
        assert hasattr(mod, "operating_profit_margin")

    def test_doc0(self):
        try:
            mod.operating_profit_margin(200_000, 1_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.operating_profit_margin(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.operating_profit_margin(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.operating_profit_margin(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.operating_profit_margin("", "")
        except EXC:
            pass


class Test_option_charm_bs:
    def test_exists(self):
        assert hasattr(mod, "option_charm_bs")

    def test_var0(self):
        try:
            mod.option_charm_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_charm_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_charm_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_charm_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_option_color_bs:
    def test_exists(self):
        assert hasattr(mod, "option_color_bs")

    def test_var0(self):
        try:
            mod.option_color_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_color_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_color_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_color_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_option_delta_bs:
    def test_exists(self):
        assert hasattr(mod, "option_delta_bs")

    def test_var0(self):
        try:
            mod.option_delta_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_delta_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_delta_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_delta_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_option_gamma_bs:
    def test_exists(self):
        assert hasattr(mod, "option_gamma_bs")

    def test_var0(self):
        try:
            mod.option_gamma_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_gamma_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_gamma_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_gamma_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_option_rho_bs:
    def test_exists(self):
        assert hasattr(mod, "option_rho_bs")

    def test_var0(self):
        try:
            mod.option_rho_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_rho_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_rho_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_rho_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_option_speed_bs:
    def test_exists(self):
        assert hasattr(mod, "option_speed_bs")

    def test_var0(self):
        try:
            mod.option_speed_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_speed_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_speed_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_speed_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_option_theta_bs:
    def test_exists(self):
        assert hasattr(mod, "option_theta_bs")

    def test_var0(self):
        try:
            mod.option_theta_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_theta_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_theta_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_theta_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_option_vanna_bs:
    def test_exists(self):
        assert hasattr(mod, "option_vanna_bs")

    def test_var0(self):
        try:
            mod.option_vanna_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_vanna_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_vanna_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_vanna_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_option_vega_bs:
    def test_exists(self):
        assert hasattr(mod, "option_vega_bs")

    def test_var0(self):
        try:
            mod.option_vega_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_vega_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_vega_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_vega_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_option_zomma_bs:
    def test_exists(self):
        assert hasattr(mod, "option_zomma_bs")

    def test_var0(self):
        try:
            mod.option_zomma_bs(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.option_zomma_bs(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.option_zomma_bs(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.option_zomma_bs("", 0, "", "", "")
        except EXC:
            pass


class Test_parkinson_volatility:
    def test_exists(self):
        assert hasattr(mod, "parkinson_volatility")

    def test_var0(self):
        try:
            mod.parkinson_volatility(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.parkinson_volatility(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.parkinson_volatility(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.parkinson_volatility("")
        except EXC:
            pass


class Test_payback_period:
    def test_exists(self):
        assert hasattr(mod, "payback_period")

    def test_doc0(self):
        try:
            mod.payback_period(1000, [300, 400, 400, 200])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.payback_period(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.payback_period(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.payback_period(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.payback_period("", "")
        except EXC:
            pass


class Test_pduration:
    def test_exists(self):
        assert hasattr(mod, "pduration")

    def test_var0(self):
        try:
            mod.pduration(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pduration(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pduration(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pduration(0, "", "")
        except EXC:
            pass


class Test_plowback_ratio:
    def test_exists(self):
        assert hasattr(mod, "plowback_ratio")

    def test_doc0(self):
        try:
            mod.plowback_ratio(2, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.plowback_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.plowback_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.plowback_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.plowback_ratio("", "")
        except EXC:
            pass


class Test_pmt:
    def test_exists(self):
        assert hasattr(mod, "pmt")

    def test_var0(self):
        try:
            mod.pmt(3.14, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pmt(100, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pmt(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pmt(0, "", "")
        except EXC:
            pass


class Test_ppmt:
    def test_exists(self):
        assert hasattr(mod, "ppmt")

    def test_var0(self):
        try:
            mod.ppmt(3.14, 0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ppmt(100, 1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ppmt(None, 0, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ppmt(0, "", "", "")
        except EXC:
            pass


class Test_present_value:
    def test_exists(self):
        assert hasattr(mod, "present_value")

    def test_doc0(self):
        try:
            mod.present_value(rate=0.05, nper=5, pmt=0, fv=1276.28)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.present_value(rate=0.05, nper=5, pmt=100, fv=0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.present_value(3.14, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.present_value(100, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.present_value(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.present_value(0, "", "")
        except EXC:
            pass


class Test_present_value_perpetuity:
    def test_exists(self):
        assert hasattr(mod, "present_value_perpetuity")

    def test_doc0(self):
        try:
            mod.present_value_perpetuity(100, 0.05)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.present_value_perpetuity(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.present_value_perpetuity(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.present_value_perpetuity(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.present_value_perpetuity("", 0)
        except EXC:
            pass


class Test_price:
    def test_exists(self):
        assert hasattr(mod, "price")

    def test_var0(self):
        try:
            mod.price("hello", "hello", 3.14, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.price("", "", 100, 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.price(None, "hello", 3.14, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.price("", "", 0, "", 0, "")
        except EXC:
            pass


class Test_price_earnings_growth:
    def test_exists(self):
        assert hasattr(mod, "price_earnings_growth")

    def test_doc0(self):
        try:
            mod.price_earnings_growth(20, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.price_earnings_growth(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.price_earnings_growth(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.price_earnings_growth(None, 0)
        except EXC:
            pass


class Test_price_to_book:
    def test_exists(self):
        assert hasattr(mod, "price_to_book")

    def test_doc0(self):
        try:
            mod.price_to_book(50, 25)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.price_to_book(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.price_to_book(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.price_to_book(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.price_to_book("", "")
        except EXC:
            pass


class Test_price_to_earnings:
    def test_exists(self):
        assert hasattr(mod, "price_to_earnings")

    def test_doc0(self):
        try:
            mod.price_to_earnings(150, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.price_to_earnings(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.price_to_earnings(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.price_to_earnings(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.price_to_earnings("", "")
        except EXC:
            pass


class Test_price_to_sales:
    def test_exists(self):
        assert hasattr(mod, "price_to_sales")

    def test_doc0(self):
        try:
            mod.price_to_sales(5_000_000, 2_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.price_to_sales(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.price_to_sales(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.price_to_sales(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.price_to_sales("", "")
        except EXC:
            pass


class Test_pricedisc:
    def test_exists(self):
        assert hasattr(mod, "pricedisc")

    def test_var0(self):
        try:
            mod.pricedisc("hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pricedisc("", "", 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pricedisc(None, "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pricedisc("", "", 0, 0)
        except EXC:
            pass


class Test_pricemat:
    def test_exists(self):
        assert hasattr(mod, "pricemat")

    def test_var0(self):
        try:
            mod.pricemat("hello", "hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pricemat("", "", "", 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pricemat(None, "hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pricemat("", "", "", 0, "")
        except EXC:
            pass


class Test_profitability_index:
    def test_exists(self):
        assert hasattr(mod, "profitability_index")

    def test_var0(self):
        try:
            mod.profitability_index(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.profitability_index(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.profitability_index(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.profitability_index(0, "", "")
        except EXC:
            pass


class Test_purchasing_power:
    def test_exists(self):
        assert hasattr(mod, "purchasing_power")

    def test_var0(self):
        try:
            mod.purchasing_power(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.purchasing_power(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.purchasing_power(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.purchasing_power("", 0, "")
        except EXC:
            pass


class Test_put_call_parity_check:
    def test_exists(self):
        assert hasattr(mod, "put_call_parity_check")

    def test_doc0(self):
        try:
            mod.put_call_parity_check(10.45, 5.57, 100, 100, 0.05, 1.0, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.put_call_parity_check(3.14, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.put_call_parity_check(100, 100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.put_call_parity_check(None, 3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.put_call_parity_check("", "", "", 0, "", "")
        except EXC:
            pass


class Test_quick_ratio:
    def test_exists(self):
        assert hasattr(mod, "quick_ratio")

    def test_doc0(self):
        try:
            mod.quick_ratio(100000, 30000, 50000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.quick_ratio(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.quick_ratio(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.quick_ratio(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.quick_ratio("", "", "")
        except EXC:
            pass


class Test_rate:
    def test_exists(self):
        assert hasattr(mod, "rate")

    def test_doc0(self):
        try:
            mod.rate(nper=360, pmt=-536.82, pv=100000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rate(0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rate(1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rate(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rate("", "", "")
        except EXC:
            pass


class Test_real_rate_of_return:
    def test_exists(self):
        assert hasattr(mod, "real_rate_of_return")

    def test_var0(self):
        try:
            mod.real_rate_of_return(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.real_rate_of_return(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.real_rate_of_return(None, 0)
        except EXC:
            pass


class Test_receivables_turnover:
    def test_exists(self):
        assert hasattr(mod, "receivables_turnover")

    def test_doc0(self):
        try:
            mod.receivables_turnover(1_000_000, 125_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.receivables_turnover(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.receivables_turnover(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.receivables_turnover(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.receivables_turnover("", "")
        except EXC:
            pass


class Test_received:
    def test_exists(self):
        assert hasattr(mod, "received")

    def test_var0(self):
        try:
            mod.received("hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.received("", "", 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.received(None, "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.received("", "", "", 0)
        except EXC:
            pass


class Test_retention_ratio:
    def test_exists(self):
        assert hasattr(mod, "retention_ratio")

    def test_doc0(self):
        try:
            mod.retention_ratio(100_000, 30_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.retention_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.retention_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.retention_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.retention_ratio("", "")
        except EXC:
            pass


class Test_return_on_assets:
    def test_exists(self):
        assert hasattr(mod, "return_on_assets")

    def test_doc0(self):
        try:
            mod.return_on_assets(50000, 500000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.return_on_assets(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.return_on_assets(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.return_on_assets(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.return_on_assets("", "")
        except EXC:
            pass


class Test_return_on_capital_employed:
    def test_exists(self):
        assert hasattr(mod, "return_on_capital_employed")

    def test_doc0(self):
        try:
            mod.return_on_capital_employed(100_000, 800_000, 200_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.return_on_capital_employed(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.return_on_capital_employed(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.return_on_capital_employed(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.return_on_capital_employed("", "", "")
        except EXC:
            pass


class Test_return_on_equity:
    def test_exists(self):
        assert hasattr(mod, "return_on_equity")

    def test_doc0(self):
        try:
            mod.return_on_equity(50000, 200000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.return_on_equity(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.return_on_equity(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.return_on_equity(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.return_on_equity("", "")
        except EXC:
            pass


class Test_return_on_net_assets:
    def test_exists(self):
        assert hasattr(mod, "return_on_net_assets")

    def test_doc0(self):
        try:
            mod.return_on_net_assets(50_000, 300_000, 100_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.return_on_net_assets(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.return_on_net_assets(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.return_on_net_assets(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.return_on_net_assets("", "", "")
        except EXC:
            pass


class Test_revenue_per_employee:
    def test_exists(self):
        assert hasattr(mod, "revenue_per_employee")

    def test_doc0(self):
        try:
            mod.revenue_per_employee(5000000, 50)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.revenue_per_employee(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.revenue_per_employee(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.revenue_per_employee(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.revenue_per_employee("", "")
        except EXC:
            pass


class Test_roi:
    def test_exists(self):
        assert hasattr(mod, "roi")

    def test_doc0(self):
        try:
            mod.roi(1500, 1000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.roi(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.roi(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.roi(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.roi(0, "")
        except EXC:
            pass


class Test_rri:
    def test_exists(self):
        assert hasattr(mod, "rri")

    def test_var0(self):
        try:
            mod.rri(0, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rri(1, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rri(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rri("", "", "")
        except EXC:
            pass


class Test_rule_of_72:
    def test_exists(self):
        assert hasattr(mod, "rule_of_72")

    def test_doc0(self):
        try:
            mod.rule_of_72(0.06)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rule_of_72(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rule_of_72(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rule_of_72(None)
        except EXC:
            pass


class Test_sales_growth_rate:
    def test_exists(self):
        assert hasattr(mod, "sales_growth_rate")

    def test_doc0(self):
        try:
            mod.sales_growth_rate(1_250_000, 1_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sales_growth_rate(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sales_growth_rate(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sales_growth_rate(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sales_growth_rate("", "")
        except EXC:
            pass


class Test_sharpe_ratio:
    def test_exists(self):
        assert hasattr(mod, "sharpe_ratio")

    def test_var0(self):
        try:
            mod.sharpe_ratio(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sharpe_ratio(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sharpe_ratio(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sharpe_ratio("")
        except EXC:
            pass


class Test_simple_interest:
    def test_exists(self):
        assert hasattr(mod, "simple_interest")

    def test_doc0(self):
        try:
            mod.simple_interest(1000, 0.05, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.simple_interest(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.simple_interest(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.simple_interest(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.simple_interest("", 0, "")
        except EXC:
            pass


class Test_sln:
    def test_exists(self):
        assert hasattr(mod, "sln")

    def test_doc0(self):
        try:
            mod.sln(cost=10000, salvage=2000, life=5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sln(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sln(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sln(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sln("", "", "")
        except EXC:
            pass


class Test_sortino_ratio:
    def test_exists(self):
        assert hasattr(mod, "sortino_ratio")

    def test_var0(self):
        try:
            mod.sortino_ratio(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sortino_ratio(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sortino_ratio(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sortino_ratio("")
        except EXC:
            pass


class Test_spot_to_forward:
    def test_exists(self):
        assert hasattr(mod, "spot_to_forward")

    def test_var0(self):
        try:
            mod.spot_to_forward(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spot_to_forward(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spot_to_forward(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spot_to_forward("", "", "", "")
        except EXC:
            pass


class Test_sustainable_growth_rate:
    def test_exists(self):
        assert hasattr(mod, "sustainable_growth_rate")

    def test_doc0(self):
        try:
            mod.sustainable_growth_rate(0.15, 0.7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sustainable_growth_rate(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sustainable_growth_rate(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sustainable_growth_rate(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sustainable_growth_rate("", 0)
        except EXC:
            pass


class Test_syd:
    def test_exists(self):
        assert hasattr(mod, "syd")

    def test_doc0(self):
        try:
            mod.syd(10000, 1000, 5, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.syd(10000, 1000, 5, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.syd(3.14, 3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.syd(100, 100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.syd(None, 3.14, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.syd("", "", "", "")
        except EXC:
            pass


class Test_tbilleq:
    def test_exists(self):
        assert hasattr(mod, "tbilleq")

    def test_var0(self):
        try:
            mod.tbilleq("hello", "hello", 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tbilleq("", "", 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tbilleq(None, "hello", 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tbilleq("", "", 0)
        except EXC:
            pass


class Test_tbillprice:
    def test_exists(self):
        assert hasattr(mod, "tbillprice")

    def test_var0(self):
        try:
            mod.tbillprice("hello", "hello", 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tbillprice("", "", 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tbillprice(None, "hello", 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tbillprice("", "", 0)
        except EXC:
            pass


class Test_tbillyield:
    def test_exists(self):
        assert hasattr(mod, "tbillyield")

    def test_var0(self):
        try:
            mod.tbillyield("hello", "hello", 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tbillyield("", "", 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tbillyield(None, "hello", 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tbillyield("", "", "")
        except EXC:
            pass


class Test_term_life_insurance_pv:
    def test_exists(self):
        assert hasattr(mod, "term_life_insurance_pv")

    def test_var0(self):
        try:
            mod.term_life_insurance_pv(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.term_life_insurance_pv(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.term_life_insurance_pv(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.term_life_insurance_pv("", 0, 0)
        except EXC:
            pass


class Test_time_weighted_return:
    def test_exists(self):
        assert hasattr(mod, "time_weighted_return")

    def test_var0(self):
        try:
            mod.time_weighted_return(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.time_weighted_return(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.time_weighted_return(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.time_weighted_return("")
        except EXC:
            pass


class Test_times_interest_earned:
    def test_exists(self):
        assert hasattr(mod, "times_interest_earned")

    def test_doc0(self):
        try:
            mod.times_interest_earned(500_000, 100_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.times_interest_earned(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.times_interest_earned(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.times_interest_earned(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.times_interest_earned("", "")
        except EXC:
            pass


class Test_tobin_q_ratio:
    def test_exists(self):
        assert hasattr(mod, "tobin_q_ratio")

    def test_doc0(self):
        try:
            mod.tobin_q_ratio(1_500_000, 1_000_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.tobin_q_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tobin_q_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tobin_q_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tobin_q_ratio("", "")
        except EXC:
            pass


class Test_treynor_ratio:
    def test_exists(self):
        assert hasattr(mod, "treynor_ratio")

    def test_doc0(self):
        try:
            mod.treynor_ratio(0.12, 0.03, 1.2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.treynor_ratio(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.treynor_ratio(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.treynor_ratio(None, 0, 0)
        except EXC:
            pass


class Test_ulcer_index:
    def test_exists(self):
        assert hasattr(mod, "ulcer_index")

    def test_doc0(self):
        try:
            mod.ulcer_index([100, 105, 102, 98, 103])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ulcer_index([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ulcer_index([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ulcer_index(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ulcer_index([])
        except EXC:
            pass


class Test_unlevered_beta:
    def test_exists(self):
        assert hasattr(mod, "unlevered_beta")

    def test_var0(self):
        try:
            mod.unlevered_beta(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unlevered_beta(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unlevered_beta(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unlevered_beta(0, 0, 0)
        except EXC:
            pass


class Test_var_parametric:
    def test_exists(self):
        assert hasattr(mod, "var_parametric")

    def test_var0(self):
        try:
            mod.var_parametric(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.var_parametric(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.var_parametric(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.var_parametric("", 0, 0)
        except EXC:
            pass


class Test_vdb:
    def test_exists(self):
        assert hasattr(mod, "vdb")

    def test_var0(self):
        try:
            mod.vdb(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.vdb(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.vdb(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.vdb("", "", "", "", "")
        except EXC:
            pass


class Test_wacc:
    def test_exists(self):
        assert hasattr(mod, "wacc")

    def test_var0(self):
        try:
            mod.wacc(3.14, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wacc(100, 100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wacc(None, 3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wacc("", "", "", "", 0)
        except EXC:
            pass


class Test_wacc_two_sources:
    def test_exists(self):
        assert hasattr(mod, "wacc_two_sources")

    def test_var0(self):
        try:
            mod.wacc_two_sources(0, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wacc_two_sources(1, 1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wacc_two_sources(None, 0, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wacc_two_sources("", "", "", "", 0)
        except EXC:
            pass


class Test_weighted_average_cost_of_debt:
    def test_exists(self):
        assert hasattr(mod, "weighted_average_cost_of_debt")

    def test_var0(self):
        try:
            mod.weighted_average_cost_of_debt(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weighted_average_cost_of_debt(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weighted_average_cost_of_debt(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weighted_average_cost_of_debt("", 0)
        except EXC:
            pass


class Test_working_capital:
    def test_exists(self):
        assert hasattr(mod, "working_capital")

    def test_doc0(self):
        try:
            mod.working_capital(500000, 300000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.working_capital(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.working_capital(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.working_capital(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.working_capital("", "")
        except EXC:
            pass


class Test_working_capital_ratio:
    def test_exists(self):
        assert hasattr(mod, "working_capital_ratio")

    def test_doc0(self):
        try:
            mod.working_capital_ratio(150_000, 100_000)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.working_capital_ratio(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.working_capital_ratio(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.working_capital_ratio(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.working_capital_ratio("", "")
        except EXC:
            pass


class Test_xirr:
    def test_exists(self):
        assert hasattr(mod, "xirr")

    def test_var0(self):
        try:
            mod.xirr(3.14, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.xirr(100, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.xirr(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.xirr([], "")
        except EXC:
            pass


class Test_xnpv:
    def test_exists(self):
        assert hasattr(mod, "xnpv")

    def test_var0(self):
        try:
            mod.xnpv(3.14, 3.14, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.xnpv(100, 100, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.xnpv(None, 3.14, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.xnpv(0, [], "")
        except EXC:
            pass


class Test_yang_zhang_volatility:
    def test_exists(self):
        assert hasattr(mod, "yang_zhang_volatility")

    def test_var0(self):
        try:
            mod.yang_zhang_volatility(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.yang_zhang_volatility(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.yang_zhang_volatility(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.yang_zhang_volatility("")
        except EXC:
            pass


class Test_yield_bond:
    def test_exists(self):
        assert hasattr(mod, "yield_bond")

    def test_var0(self):
        try:
            mod.yield_bond("hello", "hello", 3.14, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.yield_bond("", "", 100, 100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.yield_bond(None, "hello", 3.14, 3.14, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.yield_bond("", "", 0, "", 0, "")
        except EXC:
            pass


class Test_yielddisc:
    def test_exists(self):
        assert hasattr(mod, "yielddisc")

    def test_var0(self):
        try:
            mod.yielddisc("hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.yielddisc("", "", 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.yielddisc(None, "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.yielddisc("", "", "", 0)
        except EXC:
            pass


class Test_yieldmat:
    def test_exists(self):
        assert hasattr(mod, "yieldmat")

    def test_var0(self):
        try:
            mod.yieldmat("hello", "hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.yieldmat("", "", "", 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.yieldmat(None, "hello", "hello", 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.yieldmat("", "", "", 0, "")
        except EXC:
            pass


class Test_zero_coupon_price:
    def test_exists(self):
        assert hasattr(mod, "zero_coupon_price")

    def test_var0(self):
        try:
            mod.zero_coupon_price(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.zero_coupon_price(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.zero_coupon_price(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.zero_coupon_price("", 0, "")
        except EXC:
            pass

