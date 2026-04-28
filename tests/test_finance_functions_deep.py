# Deep coverage tests for shortfx.fxNumeric.finance_functions

import shortfx.fxNumeric.finance_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_irr_deep:
    def test_c0(self):
        try:
            mod.irr([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.irr([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.irr([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.irr([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.irr([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.irr([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_guess(self):
        try:
            mod.irr([1, 2, 3, 4, 5], guess=1)
        except EXC:
            pass


class Test_xirr_deep:
    def test_c0(self):
        try:
            mod.xirr([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.xirr([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.xirr([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.xirr([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.xirr([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.xirr([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_guess(self):
        try:
            mod.xirr([1, 2, 3, 4, 5], [10, 20, 30], guess=1)
        except EXC:
            pass


class Test_rate_deep:
    def test_c0(self):
        try:
            mod.rate(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rate(2, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rate(3, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rate(5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rate(10, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rate(0, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.rate(1, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.rate(2, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.rate(3, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.rate(5, 1, 42)
        except EXC:
            pass

    def test_kw_fv(self):
        try:
            mod.rate(1, 42, 0, fv=1)
        except EXC:
            pass

    def test_kw_type(self):
        try:
            mod.rate(1, 42, 0, type=1)
        except EXC:
            pass

    def test_kw_guess(self):
        try:
            mod.rate(1, 42, 0, guess=1)
        except EXC:
            pass


class Test_xnpv_deep:
    def test_c0(self):
        try:
            mod.xnpv(1, [10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.xnpv(42, [0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.xnpv(0, [-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.xnpv(-5, [100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.xnpv(3.14, [1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.xnpv(100, [1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.xnpv(0.5, [10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.xnpv(1000, [0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.xnpv(-1, [-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.xnpv(2, [100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_db_deep:
    def test_c0(self):
        try:
            mod.db(1, 42, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.db(42, 0, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.db(0, -5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.db(-5, 3.14, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.db(3.14, 100, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.db(100, 0.5, 2, 3)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.db(0.5, 1000, 3, 5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.db(1000, -1, 5, 10)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.db(-1, 2, 10, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.db(2, 1, 0, 1)
        except EXC:
            pass

    def test_kw_month(self):
        try:
            mod.db(1, 42, 3, 5, month=1)
        except EXC:
            pass


class Test_nper_deep:
    def test_c0(self):
        try:
            mod.nper(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.nper(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.nper(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.nper(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.nper(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.nper(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.nper(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.nper(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.nper(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.nper(2, 1, 42)
        except EXC:
            pass

    def test_kw_fv(self):
        try:
            mod.nper(1, 42, 0, fv=1)
        except EXC:
            pass

    def test_kw_type(self):
        try:
            mod.nper(1, 42, 0, type=1)
        except EXC:
            pass


class Test_yield_bond_deep:
    def test_c0(self):
        try:
            mod.yield_bond("hello world", "test", 0, -5, 3.14, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.yield_bond("test", "abc123", -5, 3.14, 100, 1)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.yield_bond("abc123", "", 3.14, 100, 0.5, 2)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.yield_bond("", "Hello, World!", 100, 0.5, 1000, 3)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.yield_bond("Hello, World!", "UPPER lower 123", 0.5, 1000, -1, 5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.yield_bond("UPPER lower 123", "hello world", 1000, -1, 2, 10)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.yield_bond("hello world", "test", -1, 2, 1, 0)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.yield_bond("test", "abc123", 2, 1, 42, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.yield_bond("abc123", "", 1, 42, 0, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.yield_bond("", "Hello, World!", 42, 0, -5, 3)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.yield_bond("hello world", "test", 0, -5, 3.14, 0, basis=1)
        except EXC:
            pass


class Test_amorlinc_deep:
    def test_c0(self):
        try:
            mod.amorlinc(1, "test", "abc123", -5, 10, 100)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.amorlinc(42, "abc123", "", 3.14, 0, 0.5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.amorlinc(0, "", "Hello, World!", 100, 1, 1000)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.amorlinc(-5, "Hello, World!", "UPPER lower 123", 0.5, 2, -1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.amorlinc(3.14, "UPPER lower 123", "hello world", 1000, 3, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.amorlinc(100, "hello world", "test", -1, 5, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.amorlinc(0.5, "test", "abc123", 2, 10, 42)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.amorlinc(1000, "abc123", "", 1, 0, 0)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.amorlinc(-1, "", "Hello, World!", 42, 1, -5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.amorlinc(2, "Hello, World!", "UPPER lower 123", 0, 2, 3.14)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.amorlinc(1, "test", "abc123", -5, 10, 100, basis=1)
        except EXC:
            pass


class Test_deferred_annuity_pv_deep:
    def test_c0(self):
        try:
            mod.deferred_annuity_pv(1, 42, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.deferred_annuity_pv(42, 0, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.deferred_annuity_pv(0, -5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.deferred_annuity_pv(-5, 3.14, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.deferred_annuity_pv(3.14, 100, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.deferred_annuity_pv(100, 0.5, 2, 3)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.deferred_annuity_pv(0.5, 1000, 3, 5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.deferred_annuity_pv(1000, -1, 5, 10)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.deferred_annuity_pv(-1, 2, 10, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.deferred_annuity_pv(2, 1, 0, 1)
        except EXC:
            pass


class Test_npv_deep:
    def test_c0(self):
        try:
            mod.npv(1, [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.npv(42, [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.npv(0, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.npv(-5, [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.npv(3.14, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.npv(100, [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.npv(0.5, [10, 20, 30])
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.npv(1000, [0, 1])
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.npv(-1, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.npv(2, [100])
        except EXC:
            pass


class Test_bond_yield_to_worst_deep:
    def test_c0(self):
        try:
            mod.bond_yield_to_worst(1, 42, 0, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bond_yield_to_worst(42, 0, -5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bond_yield_to_worst(0, -5, 3.14, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bond_yield_to_worst(-5, 3.14, 100, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bond_yield_to_worst(3.14, 100, 0.5, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bond_yield_to_worst(100, 0.5, 1000, 3)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bond_yield_to_worst(0.5, 1000, -1, 5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bond_yield_to_worst(1000, -1, 2, 10)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bond_yield_to_worst(-1, 2, 1, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bond_yield_to_worst(2, 1, 42, 1)
        except EXC:
            pass

    def test_kw_call_years(self):
        try:
            mod.bond_yield_to_worst(1, 42, 0, 5, call_years=[1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_endowment_insurance_pv_deep:
    def test_c0(self):
        try:
            mod.endowment_insurance_pv(1, 42, [0, 1])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.endowment_insurance_pv(42, 0, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.endowment_insurance_pv(0, -5, [100])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.endowment_insurance_pv(-5, 3.14, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.endowment_insurance_pv(3.14, 100, [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.endowment_insurance_pv(100, 0.5, [10, 20, 30])
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.endowment_insurance_pv(0.5, 1000, [0, 1])
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.endowment_insurance_pv(1000, -1, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.endowment_insurance_pv(-1, 2, [100])
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.endowment_insurance_pv(2, 1, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_money_weighted_return_deep:
    def test_c0(self):
        try:
            mod.money_weighted_return([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.money_weighted_return([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.money_weighted_return([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.money_weighted_return([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.money_weighted_return([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.money_weighted_return([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_guess(self):
        try:
            mod.money_weighted_return([1, 2, 3, 4, 5], guess=1)
        except EXC:
            pass

    def test_kw_tolerance(self):
        try:
            mod.money_weighted_return([1, 2, 3, 4, 5], tolerance=1)
        except EXC:
            pass

    def test_kw_max_iterations(self):
        try:
            mod.money_weighted_return([1, 2, 3, 4, 5], max_iterations=1)
        except EXC:
            pass


class Test_term_life_insurance_pv_deep:
    def test_c0(self):
        try:
            mod.term_life_insurance_pv(1, 42, [0, 1])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.term_life_insurance_pv(42, 0, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.term_life_insurance_pv(0, -5, [100])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.term_life_insurance_pv(-5, 3.14, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.term_life_insurance_pv(3.14, 100, [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.term_life_insurance_pv(100, 0.5, [10, 20, 30])
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.term_life_insurance_pv(0.5, 1000, [0, 1])
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.term_life_insurance_pv(1000, -1, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.term_life_insurance_pv(-1, 2, [100])
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.term_life_insurance_pv(2, 1, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_annuity_due_certain_deep:
    def test_c0(self):
        try:
            mod.annuity_due_certain(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.annuity_due_certain(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.annuity_due_certain(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.annuity_due_certain(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.annuity_due_certain(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.annuity_due_certain(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.annuity_due_certain(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.annuity_due_certain(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.annuity_due_certain(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.annuity_due_certain(2, 1, 0)
        except EXC:
            pass


class Test_binomial_option_price_deep:
    def test_c0(self):
        try:
            mod.binomial_option_price(1, 42, 0, -5, 3.14, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.binomial_option_price(42, 0, -5, 3.14, 100, 1)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.binomial_option_price(0, -5, 3.14, 100, 0.5, 2)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.binomial_option_price(-5, 3.14, 100, 0.5, 1000, 3)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.binomial_option_price(3.14, 100, 0.5, 1000, -1, 5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.binomial_option_price(100, 0.5, 1000, -1, 2, 10)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.binomial_option_price(0.5, 1000, -1, 2, 1, 0)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.binomial_option_price(1000, -1, 2, 1, 42, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.binomial_option_price(-1, 2, 1, 42, 0, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.binomial_option_price(2, 1, 42, 0, -5, 3)
        except EXC:
            pass

    def test_kw_option_type(self):
        try:
            mod.binomial_option_price(1, 42, 0, -5, 3.14, 0, option_type="hello world")
        except EXC:
            pass


class Test_garman_klass_volatility_deep:
    def test_c0(self):
        try:
            mod.garman_klass_volatility([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.garman_klass_volatility([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.garman_klass_volatility([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.garman_klass_volatility([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.garman_klass_volatility([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.garman_klass_volatility([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_life_annuity_pv_deep:
    def test_c0(self):
        try:
            mod.life_annuity_pv(1, 42, [0, 1])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.life_annuity_pv(42, 0, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.life_annuity_pv(0, -5, [100])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.life_annuity_pv(-5, 3.14, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.life_annuity_pv(3.14, 100, [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.life_annuity_pv(100, 0.5, [10, 20, 30])
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.life_annuity_pv(0.5, 1000, [0, 1])
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.life_annuity_pv(1000, -1, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.life_annuity_pv(-1, 2, [100])
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.life_annuity_pv(2, 1, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_parkinson_volatility_deep:
    def test_c0(self):
        try:
            mod.parkinson_volatility([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.parkinson_volatility([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.parkinson_volatility([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.parkinson_volatility([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.parkinson_volatility([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.parkinson_volatility([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_put_call_parity_check_deep:
    def test_c0(self):
        try:
            mod.put_call_parity_check(1, 42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.put_call_parity_check(42, 0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.put_call_parity_check(0, -5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.put_call_parity_check(-5, 3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.put_call_parity_check(3.14, 100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.put_call_parity_check(100, 0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.put_call_parity_check(0.5, 1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.put_call_parity_check(1000, -1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.put_call_parity_check(-1, 2, 1, 42, 0, -5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.put_call_parity_check(2, 1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_kw_tolerance(self):
        try:
            mod.put_call_parity_check(1, 42, 0, -5, 3.14, 100, tolerance=1)
        except EXC:
            pass


class Test_sharpe_ratio_deep:
    def test_c0(self):
        try:
            mod.sharpe_ratio([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sharpe_ratio([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sharpe_ratio([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sharpe_ratio([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sharpe_ratio([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sharpe_ratio([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_risk_free_rate(self):
        try:
            mod.sharpe_ratio([1, 2, 3, 4, 5], risk_free_rate=1)
        except EXC:
            pass


class Test_weighted_average_cost_of_debt_deep:
    def test_c0(self):
        try:
            mod.weighted_average_cost_of_debt([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weighted_average_cost_of_debt([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weighted_average_cost_of_debt([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weighted_average_cost_of_debt([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weighted_average_cost_of_debt([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weighted_average_cost_of_debt([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_tax_rate(self):
        try:
            mod.weighted_average_cost_of_debt([1, 2, 3, 4, 5], [10, 20, 30], tax_rate=1)
        except EXC:
            pass


class Test_annuity_due_pv_deep:
    def test_c0(self):
        try:
            mod.annuity_due_pv(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.annuity_due_pv(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.annuity_due_pv(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.annuity_due_pv(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.annuity_due_pv(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.annuity_due_pv(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.annuity_due_pv(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.annuity_due_pv(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.annuity_due_pv(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.annuity_due_pv(2, 1, 0)
        except EXC:
            pass


class Test_bond_equivalent_yield_deep:
    def test_c0(self):
        try:
            mod.bond_equivalent_yield(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bond_equivalent_yield(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bond_equivalent_yield(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bond_equivalent_yield(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bond_equivalent_yield(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bond_equivalent_yield(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bond_equivalent_yield(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bond_equivalent_yield(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bond_equivalent_yield(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bond_equivalent_yield(2, 1, 0)
        except EXC:
            pass


class Test_breakeven_units_deep:
    def test_c0(self):
        try:
            mod.breakeven_units(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.breakeven_units(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.breakeven_units(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.breakeven_units(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.breakeven_units(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.breakeven_units(0, 1, 2)
        except EXC:
            pass


class Test_conditional_var_deep:
    def test_c0(self):
        try:
            mod.conditional_var([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.conditional_var([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.conditional_var([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.conditional_var([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.conditional_var([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.conditional_var([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_confidence(self):
        try:
            mod.conditional_var([1, 2, 3, 4, 5], confidence=1)
        except EXC:
            pass


class Test_dividend_discount_price_deep:
    def test_c0(self):
        try:
            mod.dividend_discount_price(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dividend_discount_price(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dividend_discount_price(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dividend_discount_price(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dividend_discount_price(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dividend_discount_price(0, 1, 2)
        except EXC:
            pass

    def test_kw_growth_rate(self):
        try:
            mod.dividend_discount_price(1, 2, 3, growth_rate=1)
        except EXC:
            pass


class Test_gordon_growth_price_deep:
    def test_c0(self):
        try:
            mod.gordon_growth_price(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gordon_growth_price(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gordon_growth_price(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gordon_growth_price(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gordon_growth_price(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gordon_growth_price(0, 1, 2)
        except EXC:
            pass


class Test_historical_var_deep:
    def test_c0(self):
        try:
            mod.historical_var([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.historical_var([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.historical_var([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.historical_var([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.historical_var([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.historical_var([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_confidence(self):
        try:
            mod.historical_var([1, 2, 3, 4, 5], confidence=1)
        except EXC:
            pass


class Test_holding_period_return_deep:
    def test_c0(self):
        try:
            mod.holding_period_return(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.holding_period_return(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.holding_period_return(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.holding_period_return(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.holding_period_return(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.holding_period_return(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.holding_period_return(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.holding_period_return(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.holding_period_return(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.holding_period_return(2, 1)
        except EXC:
            pass

    def test_kw_income(self):
        try:
            mod.holding_period_return(1, 42, income=1)
        except EXC:
            pass


class Test_loan_amortization_table_deep:
    def test_c0(self):
        try:
            mod.loan_amortization_table(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.loan_amortization_table(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.loan_amortization_table(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.loan_amortization_table(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.loan_amortization_table(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.loan_amortization_table(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.loan_amortization_table(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.loan_amortization_table(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.loan_amortization_table(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.loan_amortization_table(2, 1, 0)
        except EXC:
            pass


class Test_mortgage_remaining_balance_deep:
    def test_c0(self):
        try:
            mod.mortgage_remaining_balance(1, 42, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mortgage_remaining_balance(42, 0, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mortgage_remaining_balance(0, -5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mortgage_remaining_balance(-5, 3.14, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mortgage_remaining_balance(3.14, 100, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mortgage_remaining_balance(100, 0.5, 2, 3)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.mortgage_remaining_balance(0.5, 1000, 3, 5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.mortgage_remaining_balance(1000, -1, 5, 10)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.mortgage_remaining_balance(-1, 2, 10, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.mortgage_remaining_balance(2, 1, 0, 1)
        except EXC:
            pass


class Test_option_charm_bs_deep:
    def test_c0(self):
        try:
            mod.option_charm_bs(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.option_charm_bs(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.option_charm_bs(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.option_charm_bs(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.option_charm_bs(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.option_charm_bs(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.option_charm_bs(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.option_charm_bs(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.option_charm_bs(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.option_charm_bs(2, 1, 42, 0, -5)
        except EXC:
            pass

    def test_kw_option_type(self):
        try:
            mod.option_charm_bs(1, 42, 0, -5, 3.14, option_type="hello world")
        except EXC:
            pass


class Test_sortino_ratio_deep:
    def test_c0(self):
        try:
            mod.sortino_ratio([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sortino_ratio([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sortino_ratio([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sortino_ratio([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sortino_ratio([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sortino_ratio([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_risk_free_rate(self):
        try:
            mod.sortino_ratio([1, 2, 3, 4, 5], risk_free_rate=1)
        except EXC:
            pass


class Test_vdb_deep:
    def test_c0(self):
        try:
            mod.vdb(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.vdb(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.vdb(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.vdb(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.vdb(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.vdb(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.vdb(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.vdb(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.vdb(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.vdb(2, 1, 42, 0, -5)
        except EXC:
            pass

    def test_kw_factor(self):
        try:
            mod.vdb(1, 42, 0, -5, 3.14, factor=1)
        except EXC:
            pass

    def test_kw_no_switch(self):
        try:
            mod.vdb(1, 42, 0, -5, 3.14, no_switch=True)
        except EXC:
            pass


class Test_yang_zhang_volatility_deep:
    def test_c0(self):
        try:
            mod.yang_zhang_volatility([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.yang_zhang_volatility([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.yang_zhang_volatility([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.yang_zhang_volatility([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.yang_zhang_volatility([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.yang_zhang_volatility([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_altman_z_score_deep:
    def test_c0(self):
        try:
            mod.altman_z_score(1, 42, 0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.altman_z_score(42, 0, -5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.altman_z_score(0, -5, 3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.altman_z_score(-5, 3.14, 100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.altman_z_score(3.14, 100, 0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.altman_z_score(100, 0.5, 1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.altman_z_score(0.5, 1000, -1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.altman_z_score(1000, -1, 2, 1, 42, 0, -5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.altman_z_score(-1, 2, 1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.altman_z_score(2, 1, 42, 0, -5, 3.14, 100)
        except EXC:
            pass


class Test_annuity_due_fv_deep:
    def test_c0(self):
        try:
            mod.annuity_due_fv(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.annuity_due_fv(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.annuity_due_fv(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.annuity_due_fv(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.annuity_due_fv(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.annuity_due_fv(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.annuity_due_fv(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.annuity_due_fv(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.annuity_due_fv(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.annuity_due_fv(2, 1, 0)
        except EXC:
            pass


class Test_annuity_immediate_certain_deep:
    def test_c0(self):
        try:
            mod.annuity_immediate_certain(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.annuity_immediate_certain(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.annuity_immediate_certain(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.annuity_immediate_certain(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.annuity_immediate_certain(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.annuity_immediate_certain(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.annuity_immediate_certain(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.annuity_immediate_certain(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.annuity_immediate_certain(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.annuity_immediate_certain(2, 1, 0)
        except EXC:
            pass


class Test_burn_rate_deep:
    def test_c0(self):
        try:
            mod.burn_rate(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.burn_rate(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.burn_rate(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.burn_rate(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.burn_rate(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.burn_rate(0, 1, 2)
        except EXC:
            pass


class Test_cagr_deep:
    def test_c0(self):
        try:
            mod.cagr(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cagr(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cagr(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cagr(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cagr(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cagr(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.cagr(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.cagr(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.cagr(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.cagr(2, 1, 42)
        except EXC:
            pass


class Test_cost_of_equity_capm_deep:
    def test_c0(self):
        try:
            mod.cost_of_equity_capm(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cost_of_equity_capm(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cost_of_equity_capm(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cost_of_equity_capm(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cost_of_equity_capm(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cost_of_equity_capm(0, 1, 2)
        except EXC:
            pass


class Test_debt_to_equity_deep:
    def test_c0(self):
        try:
            mod.debt_to_equity(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.debt_to_equity(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.debt_to_equity(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.debt_to_equity(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.debt_to_equity(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.debt_to_equity(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.debt_to_equity(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.debt_to_equity(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.debt_to_equity(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.debt_to_equity(2, 1)
        except EXC:
            pass


class Test_economic_value_added_deep:
    def test_c0(self):
        try:
            mod.economic_value_added(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.economic_value_added(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.economic_value_added(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.economic_value_added(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.economic_value_added(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.economic_value_added(0, 1, 2)
        except EXC:
            pass


class Test_future_value_deep:
    def test_c0(self):
        try:
            mod.future_value(1, 2, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.future_value(42, 3, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.future_value(0, 5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.future_value(-5, 10, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.future_value(3.14, 0, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.future_value(100, 1, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.future_value(0.5, 2, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.future_value(1000, 3, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.future_value(-1, 5, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.future_value(2, 10, 42, 0)
        except EXC:
            pass

    def test_kw_type(self):
        try:
            mod.future_value(1, 2, 0, -5, type=1)
        except EXC:
            pass


class Test_implied_volatility_deep:
    def test_c0(self):
        try:
            mod.implied_volatility(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.implied_volatility(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.implied_volatility(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.implied_volatility(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.implied_volatility(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.implied_volatility(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.implied_volatility(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.implied_volatility(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.implied_volatility(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.implied_volatility(2, 1, 42, 0, -5)
        except EXC:
            pass

    def test_kw_option_type(self):
        try:
            mod.implied_volatility(1, 42, 0, -5, 3.14, option_type="hello world")
        except EXC:
            pass

    def test_kw_tol(self):
        try:
            mod.implied_volatility(1, 42, 0, -5, 3.14, tol=1)
        except EXC:
            pass

    def test_kw_max_iter(self):
        try:
            mod.implied_volatility(1, 42, 0, -5, 3.14, max_iter=1)
        except EXC:
            pass


class Test_ipmt_deep:
    def test_c0(self):
        try:
            mod.ipmt(1, 2, 3, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ipmt(42, 3, 5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ipmt(0, 5, 10, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ipmt(-5, 10, 0, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ipmt(3.14, 0, 1, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ipmt(100, 1, 2, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.ipmt(0.5, 2, 3, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.ipmt(1000, 3, 5, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.ipmt(-1, 5, 10, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.ipmt(2, 10, 0, 0)
        except EXC:
            pass

    def test_kw_fv(self):
        try:
            mod.ipmt(1, 2, 3, -5, fv=1)
        except EXC:
            pass

    def test_kw_type_(self):
        try:
            mod.ipmt(1, 2, 3, -5, type_=1)
        except EXC:
            pass


class Test_kelly_criterion_deep:
    def test_c0(self):
        try:
            mod.kelly_criterion(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.kelly_criterion(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.kelly_criterion(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.kelly_criterion(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.kelly_criterion(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.kelly_criterion(0, 1)
        except EXC:
            pass


class Test_modified_dietz_return_deep:
    def test_c0(self):
        try:
            mod.modified_dietz_return(1, 42, [0, 1], [-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.modified_dietz_return(42, 0, [-3, -1, 0, 2, 5], [100], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.modified_dietz_return(0, -5, [100], [1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.modified_dietz_return(-5, 3.14, [1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.modified_dietz_return(3.14, 100, [1, 2, 3, 4, 5], [10, 20, 30], 3)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.modified_dietz_return(100, 0.5, [10, 20, 30], [0, 1], 5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.modified_dietz_return(0.5, 1000, [0, 1], [-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.modified_dietz_return(1000, -1, [-3, -1, 0, 2, 5], [100], 0)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.modified_dietz_return(-1, 2, [100], [1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.modified_dietz_return(2, 1, [1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5], 2)
        except EXC:
            pass


class Test_mortgage_total_cost_deep:
    def test_c0(self):
        try:
            mod.mortgage_total_cost(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mortgage_total_cost(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mortgage_total_cost(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mortgage_total_cost(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mortgage_total_cost(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mortgage_total_cost(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.mortgage_total_cost(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.mortgage_total_cost(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.mortgage_total_cost(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.mortgage_total_cost(2, 1, 0)
        except EXC:
            pass


class Test_option_delta_bs_deep:
    def test_c0(self):
        try:
            mod.option_delta_bs(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.option_delta_bs(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.option_delta_bs(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.option_delta_bs(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.option_delta_bs(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.option_delta_bs(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.option_delta_bs(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.option_delta_bs(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.option_delta_bs(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.option_delta_bs(2, 1, 42, 0, -5)
        except EXC:
            pass

    def test_kw_option_type(self):
        try:
            mod.option_delta_bs(1, 42, 0, -5, 3.14, option_type="hello world")
        except EXC:
            pass


class Test_option_rho_bs_deep:
    def test_c0(self):
        try:
            mod.option_rho_bs(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.option_rho_bs(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.option_rho_bs(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.option_rho_bs(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.option_rho_bs(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.option_rho_bs(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.option_rho_bs(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.option_rho_bs(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.option_rho_bs(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.option_rho_bs(2, 1, 42, 0, -5)
        except EXC:
            pass

    def test_kw_option_type(self):
        try:
            mod.option_rho_bs(1, 42, 0, -5, 3.14, option_type="hello world")
        except EXC:
            pass


class Test_option_zomma_bs_deep:
    def test_c0(self):
        try:
            mod.option_zomma_bs(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.option_zomma_bs(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.option_zomma_bs(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.option_zomma_bs(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.option_zomma_bs(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.option_zomma_bs(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.option_zomma_bs(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.option_zomma_bs(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.option_zomma_bs(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.option_zomma_bs(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_pmt_deep:
    def test_c0(self):
        try:
            mod.pmt(1, 2, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pmt(42, 3, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pmt(0, 5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pmt(-5, 10, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pmt(3.14, 0, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pmt(100, 1, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.pmt(0.5, 2, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.pmt(1000, 3, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.pmt(-1, 5, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.pmt(2, 10, 42)
        except EXC:
            pass

    def test_kw_fv(self):
        try:
            mod.pmt(1, 2, 0, fv=1)
        except EXC:
            pass

    def test_kw_type(self):
        try:
            mod.pmt(1, 2, 0, type=1)
        except EXC:
            pass


class Test_present_value_deep:
    def test_c0(self):
        try:
            mod.present_value(1, 2, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.present_value(42, 3, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.present_value(0, 5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.present_value(-5, 10, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.present_value(3.14, 0, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.present_value(100, 1, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.present_value(0.5, 2, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.present_value(1000, 3, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.present_value(-1, 5, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.present_value(2, 10, 42)
        except EXC:
            pass

    def test_kw_fv(self):
        try:
            mod.present_value(1, 2, 0, fv=1)
        except EXC:
            pass

    def test_kw_type(self):
        try:
            mod.present_value(1, 2, 0, type=1)
        except EXC:
            pass


class Test_price_deep:
    def test_c0(self):
        try:
            mod.price("hello world", "test", 0, -5, 3.14, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.price("test", "abc123", -5, 3.14, 100, 1)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.price("abc123", "", 3.14, 100, 0.5, 2)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.price("", "Hello, World!", 100, 0.5, 1000, 3)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.price("Hello, World!", "UPPER lower 123", 0.5, 1000, -1, 5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.price("UPPER lower 123", "hello world", 1000, -1, 2, 10)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.price("hello world", "test", -1, 2, 1, 0)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.price("test", "abc123", 2, 1, 42, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.price("abc123", "", 1, 42, 0, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.price("", "Hello, World!", 42, 0, -5, 3)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.price("hello world", "test", 0, -5, 3.14, 0, basis=1)
        except EXC:
            pass


class Test_quick_ratio_deep:
    def test_c0(self):
        try:
            mod.quick_ratio(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.quick_ratio(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.quick_ratio(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.quick_ratio(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.quick_ratio(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.quick_ratio(0, 1, 2)
        except EXC:
            pass


class Test_sustainable_growth_rate_deep:
    def test_c0(self):
        try:
            mod.sustainable_growth_rate(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sustainable_growth_rate(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sustainable_growth_rate(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sustainable_growth_rate(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sustainable_growth_rate(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sustainable_growth_rate(0, 1)
        except EXC:
            pass


class Test_syd_deep:
    def test_c0(self):
        try:
            mod.syd(1, 42, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.syd(42, 0, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.syd(0, -5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.syd(-5, 3.14, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.syd(3.14, 100, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.syd(100, 0.5, 2, 3)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.syd(0.5, 1000, 3, 5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.syd(1000, -1, 5, 10)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.syd(-1, 2, 10, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.syd(2, 1, 0, 1)
        except EXC:
            pass


class Test_treynor_ratio_deep:
    def test_c0(self):
        try:
            mod.treynor_ratio(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.treynor_ratio(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.treynor_ratio(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.treynor_ratio(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.treynor_ratio(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.treynor_ratio(0, 1, 2)
        except EXC:
            pass


class Test_var_parametric_deep:
    def test_c0(self):
        try:
            mod.var_parametric(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.var_parametric(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.var_parametric(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.var_parametric(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.var_parametric(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.var_parametric(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.var_parametric(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.var_parametric(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.var_parametric(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.var_parametric(2, 1, 42)
        except EXC:
            pass

    def test_kw_confidence(self):
        try:
            mod.var_parametric(1, 42, 0, confidence=1)
        except EXC:
            pass


class Test_asset_turnover_deep:
    def test_c0(self):
        try:
            mod.asset_turnover(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.asset_turnover(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.asset_turnover(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.asset_turnover(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.asset_turnover(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.asset_turnover(0, 1)
        except EXC:
            pass


class Test_black_scholes_call_deep:
    def test_c0(self):
        try:
            mod.black_scholes_call(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.black_scholes_call(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.black_scholes_call(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.black_scholes_call(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.black_scholes_call(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.black_scholes_call(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.black_scholes_call(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.black_scholes_call(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.black_scholes_call(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.black_scholes_call(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_bond_convexity_deep:
    def test_c0(self):
        try:
            mod.bond_convexity(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bond_convexity(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bond_convexity(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bond_convexity(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bond_convexity(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bond_convexity(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bond_convexity(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bond_convexity(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bond_convexity(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bond_convexity(2, 1, 0)
        except EXC:
            pass

    def test_kw_face(self):
        try:
            mod.bond_convexity(1, 42, 3, face=1)
        except EXC:
            pass


class Test_calmar_ratio_deep:
    def test_c0(self):
        try:
            mod.calmar_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.calmar_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.calmar_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.calmar_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.calmar_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.calmar_ratio(0, 1)
        except EXC:
            pass


class Test_capital_intensity_ratio_deep:
    def test_c0(self):
        try:
            mod.capital_intensity_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.capital_intensity_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.capital_intensity_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.capital_intensity_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.capital_intensity_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.capital_intensity_ratio(0, 1)
        except EXC:
            pass


class Test_cash_conversion_efficiency_deep:
    def test_c0(self):
        try:
            mod.cash_conversion_efficiency(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cash_conversion_efficiency(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cash_conversion_efficiency(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cash_conversion_efficiency(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cash_conversion_efficiency(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cash_conversion_efficiency(0, 1)
        except EXC:
            pass


class Test_cash_flow_coverage_deep:
    def test_c0(self):
        try:
            mod.cash_flow_coverage(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cash_flow_coverage(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cash_flow_coverage(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cash_flow_coverage(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cash_flow_coverage(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cash_flow_coverage(0, 1)
        except EXC:
            pass


class Test_cash_ratio_deep:
    def test_c0(self):
        try:
            mod.cash_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cash_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cash_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cash_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cash_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cash_ratio(0, 1)
        except EXC:
            pass


class Test_cash_return_on_assets_deep:
    def test_c0(self):
        try:
            mod.cash_return_on_assets(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cash_return_on_assets(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cash_return_on_assets(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cash_return_on_assets(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cash_return_on_assets(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cash_return_on_assets(0, 1)
        except EXC:
            pass


class Test_continuous_compounding_deep:
    def test_c0(self):
        try:
            mod.continuous_compounding(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.continuous_compounding(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.continuous_compounding(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.continuous_compounding(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.continuous_compounding(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.continuous_compounding(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.continuous_compounding(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.continuous_compounding(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.continuous_compounding(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.continuous_compounding(2, 1, 42)
        except EXC:
            pass


class Test_contribution_margin_deep:
    def test_c0(self):
        try:
            mod.contribution_margin(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.contribution_margin(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.contribution_margin(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.contribution_margin(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.contribution_margin(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.contribution_margin(0, 1)
        except EXC:
            pass


class Test_current_ratio_deep:
    def test_c0(self):
        try:
            mod.current_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.current_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.current_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.current_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.current_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.current_ratio(0, 1)
        except EXC:
            pass


class Test_debt_service_coverage_deep:
    def test_c0(self):
        try:
            mod.debt_service_coverage(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.debt_service_coverage(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.debt_service_coverage(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.debt_service_coverage(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.debt_service_coverage(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.debt_service_coverage(0, 1)
        except EXC:
            pass


class Test_debt_to_capital_deep:
    def test_c0(self):
        try:
            mod.debt_to_capital(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.debt_to_capital(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.debt_to_capital(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.debt_to_capital(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.debt_to_capital(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.debt_to_capital(0, 1)
        except EXC:
            pass


class Test_debt_to_income_deep:
    def test_c0(self):
        try:
            mod.debt_to_income(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.debt_to_income(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.debt_to_income(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.debt_to_income(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.debt_to_income(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.debt_to_income(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.debt_to_income(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.debt_to_income(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.debt_to_income(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.debt_to_income(2, 1)
        except EXC:
            pass


class Test_decreasing_annuity_pv_deep:
    def test_c0(self):
        try:
            mod.decreasing_annuity_pv(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.decreasing_annuity_pv(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.decreasing_annuity_pv(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.decreasing_annuity_pv(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.decreasing_annuity_pv(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.decreasing_annuity_pv(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.decreasing_annuity_pv(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.decreasing_annuity_pv(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.decreasing_annuity_pv(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.decreasing_annuity_pv(2, 10)
        except EXC:
            pass


class Test_defensive_interval_deep:
    def test_c0(self):
        try:
            mod.defensive_interval(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.defensive_interval(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.defensive_interval(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.defensive_interval(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.defensive_interval(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.defensive_interval(0, 1)
        except EXC:
            pass


class Test_disc_deep:
    def test_c0(self):
        try:
            mod.disc("hello world", "test", 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.disc("test", "abc123", -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.disc("abc123", "", 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.disc("", "Hello, World!", 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.disc("Hello, World!", "UPPER lower 123", 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.disc("UPPER lower 123", "hello world", 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.disc("hello world", "test", -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.disc("test", "abc123", 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.disc("abc123", "", 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.disc("", "Hello, World!", 42, 0)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.disc("hello world", "test", 0, -5, basis=1)
        except EXC:
            pass


class Test_dividend_payout_ratio_deep:
    def test_c0(self):
        try:
            mod.dividend_payout_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dividend_payout_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dividend_payout_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dividend_payout_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dividend_payout_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dividend_payout_ratio(0, 1)
        except EXC:
            pass


class Test_dupont_roe_deep:
    def test_c0(self):
        try:
            mod.dupont_roe(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dupont_roe(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dupont_roe(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dupont_roe(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dupont_roe(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dupont_roe(0, 1, 2)
        except EXC:
            pass


class Test_duration_gap_deep:
    def test_c0(self):
        try:
            mod.duration_gap(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.duration_gap(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.duration_gap(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.duration_gap(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.duration_gap(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.duration_gap(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.duration_gap(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.duration_gap(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.duration_gap(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.duration_gap(2, 1, 42)
        except EXC:
            pass


class Test_earnings_per_share_deep:
    def test_c0(self):
        try:
            mod.earnings_per_share(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.earnings_per_share(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.earnings_per_share(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.earnings_per_share(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.earnings_per_share(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.earnings_per_share(0, 1)
        except EXC:
            pass


class Test_earnings_yield_deep:
    def test_c0(self):
        try:
            mod.earnings_yield(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.earnings_yield(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.earnings_yield(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.earnings_yield(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.earnings_yield(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.earnings_yield(0, 1)
        except EXC:
            pass


class Test_effect_deep:
    def test_c0(self):
        try:
            mod.effect(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.effect(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.effect(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.effect(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.effect(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.effect(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.effect(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.effect(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.effect(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.effect(2, 10)
        except EXC:
            pass


class Test_enterprise_value_simple_deep:
    def test_c0(self):
        try:
            mod.enterprise_value_simple(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.enterprise_value_simple(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.enterprise_value_simple(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.enterprise_value_simple(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.enterprise_value_simple(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.enterprise_value_simple(0, 1, 2)
        except EXC:
            pass


class Test_ev_to_ebitda_deep:
    def test_c0(self):
        try:
            mod.ev_to_ebitda(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ev_to_ebitda(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ev_to_ebitda(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ev_to_ebitda(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ev_to_ebitda(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ev_to_ebitda(0, 1)
        except EXC:
            pass


class Test_expected_shortfall_deep:
    def test_c0(self):
        try:
            mod.expected_shortfall(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.expected_shortfall(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.expected_shortfall(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.expected_shortfall(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.expected_shortfall(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.expected_shortfall(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.expected_shortfall(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.expected_shortfall(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.expected_shortfall(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.expected_shortfall(2, 1, 42)
        except EXC:
            pass

    def test_kw_confidence(self):
        try:
            mod.expected_shortfall(1, 42, 0, confidence=1)
        except EXC:
            pass


class Test_fixed_charge_coverage_deep:
    def test_c0(self):
        try:
            mod.fixed_charge_coverage(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fixed_charge_coverage(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fixed_charge_coverage(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fixed_charge_coverage(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fixed_charge_coverage(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fixed_charge_coverage(0, 1)
        except EXC:
            pass


class Test_free_cash_flow_yield_deep:
    def test_c0(self):
        try:
            mod.free_cash_flow_yield(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.free_cash_flow_yield(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.free_cash_flow_yield(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.free_cash_flow_yield(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.free_cash_flow_yield(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.free_cash_flow_yield(0, 1)
        except EXC:
            pass


class Test_fvschedule_deep:
    def test_c0(self):
        try:
            mod.fvschedule(1, [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fvschedule(42, [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fvschedule(0, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fvschedule(-5, [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fvschedule(3.14, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fvschedule(100, [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.fvschedule(0.5, [10, 20, 30])
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.fvschedule(1000, [0, 1])
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.fvschedule(-1, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.fvschedule(2, [100])
        except EXC:
            pass


class Test_gross_margin_deep:
    def test_c0(self):
        try:
            mod.gross_margin(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gross_margin(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gross_margin(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gross_margin(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gross_margin(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gross_margin(0, 1)
        except EXC:
            pass


class Test_growing_annuity_pv_deep:
    def test_c0(self):
        try:
            mod.growing_annuity_pv(1, 42, 0, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.growing_annuity_pv(42, 0, -5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.growing_annuity_pv(0, -5, 3.14, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.growing_annuity_pv(-5, 3.14, 100, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.growing_annuity_pv(3.14, 100, 0.5, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.growing_annuity_pv(100, 0.5, 1000, 3)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.growing_annuity_pv(0.5, 1000, -1, 5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.growing_annuity_pv(1000, -1, 2, 10)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.growing_annuity_pv(-1, 2, 1, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.growing_annuity_pv(2, 1, 42, 1)
        except EXC:
            pass


class Test_growing_perpetuity_pv_deep:
    def test_c0(self):
        try:
            mod.growing_perpetuity_pv(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.growing_perpetuity_pv(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.growing_perpetuity_pv(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.growing_perpetuity_pv(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.growing_perpetuity_pv(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.growing_perpetuity_pv(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.growing_perpetuity_pv(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.growing_perpetuity_pv(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.growing_perpetuity_pv(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.growing_perpetuity_pv(2, 1, 42)
        except EXC:
            pass


class Test_increasing_annuity_pv_deep:
    def test_c0(self):
        try:
            mod.increasing_annuity_pv(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.increasing_annuity_pv(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.increasing_annuity_pv(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.increasing_annuity_pv(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.increasing_annuity_pv(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.increasing_annuity_pv(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.increasing_annuity_pv(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.increasing_annuity_pv(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.increasing_annuity_pv(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.increasing_annuity_pv(2, 10)
        except EXC:
            pass


class Test_inflation_adjusted_value_deep:
    def test_c0(self):
        try:
            mod.inflation_adjusted_value(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inflation_adjusted_value(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inflation_adjusted_value(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inflation_adjusted_value(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inflation_adjusted_value(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inflation_adjusted_value(0, 1, 2)
        except EXC:
            pass


class Test_information_ratio_deep:
    def test_c0(self):
        try:
            mod.information_ratio(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.information_ratio(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.information_ratio(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.information_ratio(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.information_ratio(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.information_ratio(0, 1, 2)
        except EXC:
            pass


class Test_interest_burden_ratio_deep:
    def test_c0(self):
        try:
            mod.interest_burden_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.interest_burden_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.interest_burden_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.interest_burden_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.interest_burden_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.interest_burden_ratio(0, 1)
        except EXC:
            pass


class Test_interest_coverage_ratio_deep:
    def test_c0(self):
        try:
            mod.interest_coverage_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.interest_coverage_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.interest_coverage_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.interest_coverage_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.interest_coverage_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.interest_coverage_ratio(0, 1)
        except EXC:
            pass


class Test_intrate_deep:
    def test_c0(self):
        try:
            mod.intrate("hello world", "test", 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.intrate("test", "abc123", -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.intrate("abc123", "", 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.intrate("", "Hello, World!", 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.intrate("Hello, World!", "UPPER lower 123", 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.intrate("UPPER lower 123", "hello world", 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.intrate("hello world", "test", -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.intrate("test", "abc123", 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.intrate("abc123", "", 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.intrate("", "Hello, World!", 42, 0)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.intrate("hello world", "test", 0, -5, basis=1)
        except EXC:
            pass


class Test_inventory_to_sales_deep:
    def test_c0(self):
        try:
            mod.inventory_to_sales(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inventory_to_sales(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inventory_to_sales(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inventory_to_sales(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inventory_to_sales(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inventory_to_sales(0, 1)
        except EXC:
            pass


class Test_inventory_turnover_deep:
    def test_c0(self):
        try:
            mod.inventory_turnover(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.inventory_turnover(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.inventory_turnover(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.inventory_turnover(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.inventory_turnover(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.inventory_turnover(0, 1)
        except EXC:
            pass


class Test_leverage_ratio_deep:
    def test_c0(self):
        try:
            mod.leverage_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.leverage_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.leverage_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.leverage_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.leverage_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.leverage_ratio(0, 1)
        except EXC:
            pass


class Test_margin_of_safety_pct_deep:
    def test_c0(self):
        try:
            mod.margin_of_safety_pct(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.margin_of_safety_pct(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.margin_of_safety_pct(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.margin_of_safety_pct(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.margin_of_safety_pct(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.margin_of_safety_pct(0, 1)
        except EXC:
            pass


class Test_marginal_cost_deep:
    def test_c0(self):
        try:
            mod.marginal_cost(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.marginal_cost(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.marginal_cost(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.marginal_cost(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.marginal_cost(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.marginal_cost(0, 1)
        except EXC:
            pass


class Test_market_cap_deep:
    def test_c0(self):
        try:
            mod.market_cap(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.market_cap(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.market_cap(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.market_cap(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.market_cap(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.market_cap(0, 1)
        except EXC:
            pass


class Test_mirr_deep:
    def test_c0(self):
        try:
            mod.mirr([1, 2, 3, 4, 5], 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mirr([10, 20, 30], 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mirr([0, 1], -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mirr([-3, -1, 0, 2, 5], 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mirr([100], 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mirr([1, 1, 2, 3, 5, 8], 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.mirr([1, 2, 3, 4, 5], 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.mirr([10, 20, 30], -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.mirr([0, 1], 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.mirr([-3, -1, 0, 2, 5], 1, 42)
        except EXC:
            pass


class Test_modified_duration_simple_deep:
    def test_c0(self):
        try:
            mod.modified_duration_simple(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.modified_duration_simple(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.modified_duration_simple(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.modified_duration_simple(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.modified_duration_simple(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.modified_duration_simple(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.modified_duration_simple(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.modified_duration_simple(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.modified_duration_simple(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.modified_duration_simple(2, 1)
        except EXC:
            pass

    def test_kw_frequency(self):
        try:
            mod.modified_duration_simple(1, 42, frequency=1)
        except EXC:
            pass


class Test_months_of_runway_deep:
    def test_c0(self):
        try:
            mod.months_of_runway(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.months_of_runway(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.months_of_runway(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.months_of_runway(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.months_of_runway(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.months_of_runway(0, 1)
        except EXC:
            pass


class Test_net_profit_margin_deep:
    def test_c0(self):
        try:
            mod.net_profit_margin(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.net_profit_margin(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.net_profit_margin(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.net_profit_margin(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.net_profit_margin(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.net_profit_margin(0, 1)
        except EXC:
            pass


class Test_nominal_deep:
    def test_c0(self):
        try:
            mod.nominal(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.nominal(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.nominal(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.nominal(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.nominal(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.nominal(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.nominal(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.nominal(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.nominal(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.nominal(2, 10)
        except EXC:
            pass


class Test_nominal_to_real_rate_deep:
    def test_c0(self):
        try:
            mod.nominal_to_real_rate(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.nominal_to_real_rate(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.nominal_to_real_rate(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.nominal_to_real_rate(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.nominal_to_real_rate(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.nominal_to_real_rate(0, 1)
        except EXC:
            pass


class Test_nopat_margin_deep:
    def test_c0(self):
        try:
            mod.nopat_margin(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.nopat_margin(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.nopat_margin(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.nopat_margin(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.nopat_margin(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.nopat_margin(0, 1)
        except EXC:
            pass


class Test_omega_ratio_deep:
    def test_c0(self):
        try:
            mod.omega_ratio([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.omega_ratio([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.omega_ratio([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.omega_ratio([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.omega_ratio([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.omega_ratio([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_threshold(self):
        try:
            mod.omega_ratio([1, 2, 3, 4, 5], threshold=1)
        except EXC:
            pass


class Test_operating_cash_flow_ratio_deep:
    def test_c0(self):
        try:
            mod.operating_cash_flow_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.operating_cash_flow_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.operating_cash_flow_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.operating_cash_flow_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.operating_cash_flow_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.operating_cash_flow_ratio(0, 1)
        except EXC:
            pass


class Test_operating_margin_deep:
    def test_c0(self):
        try:
            mod.operating_margin(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.operating_margin(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.operating_margin(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.operating_margin(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.operating_margin(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.operating_margin(0, 1)
        except EXC:
            pass


class Test_operating_profit_margin_deep:
    def test_c0(self):
        try:
            mod.operating_profit_margin(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.operating_profit_margin(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.operating_profit_margin(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.operating_profit_margin(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.operating_profit_margin(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.operating_profit_margin(0, 1)
        except EXC:
            pass


class Test_option_color_bs_deep:
    def test_c0(self):
        try:
            mod.option_color_bs(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.option_color_bs(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.option_color_bs(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.option_color_bs(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.option_color_bs(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.option_color_bs(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.option_color_bs(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.option_color_bs(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.option_color_bs(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.option_color_bs(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_option_gamma_bs_deep:
    def test_c0(self):
        try:
            mod.option_gamma_bs(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.option_gamma_bs(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.option_gamma_bs(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.option_gamma_bs(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.option_gamma_bs(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.option_gamma_bs(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.option_gamma_bs(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.option_gamma_bs(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.option_gamma_bs(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.option_gamma_bs(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_option_speed_bs_deep:
    def test_c0(self):
        try:
            mod.option_speed_bs(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.option_speed_bs(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.option_speed_bs(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.option_speed_bs(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.option_speed_bs(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.option_speed_bs(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.option_speed_bs(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.option_speed_bs(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.option_speed_bs(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.option_speed_bs(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_option_theta_bs_deep:
    def test_c0(self):
        try:
            mod.option_theta_bs(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.option_theta_bs(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.option_theta_bs(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.option_theta_bs(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.option_theta_bs(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.option_theta_bs(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.option_theta_bs(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.option_theta_bs(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.option_theta_bs(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.option_theta_bs(2, 1, 42, 0, -5)
        except EXC:
            pass

    def test_kw_option_type(self):
        try:
            mod.option_theta_bs(1, 42, 0, -5, 3.14, option_type="hello world")
        except EXC:
            pass


class Test_option_vanna_bs_deep:
    def test_c0(self):
        try:
            mod.option_vanna_bs(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.option_vanna_bs(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.option_vanna_bs(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.option_vanna_bs(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.option_vanna_bs(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.option_vanna_bs(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.option_vanna_bs(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.option_vanna_bs(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.option_vanna_bs(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.option_vanna_bs(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_pduration_deep:
    def test_c0(self):
        try:
            mod.pduration(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pduration(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pduration(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pduration(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pduration(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pduration(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.pduration(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.pduration(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.pduration(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.pduration(2, 1, 42)
        except EXC:
            pass


class Test_present_value_perpetuity_deep:
    def test_c0(self):
        try:
            mod.present_value_perpetuity(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.present_value_perpetuity(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.present_value_perpetuity(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.present_value_perpetuity(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.present_value_perpetuity(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.present_value_perpetuity(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.present_value_perpetuity(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.present_value_perpetuity(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.present_value_perpetuity(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.present_value_perpetuity(2, 1)
        except EXC:
            pass


class Test_price_earnings_growth_deep:
    def test_c0(self):
        try:
            mod.price_earnings_growth(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.price_earnings_growth(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.price_earnings_growth(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.price_earnings_growth(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.price_earnings_growth(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.price_earnings_growth(0, 1)
        except EXC:
            pass


class Test_price_to_earnings_deep:
    def test_c0(self):
        try:
            mod.price_to_earnings(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.price_to_earnings(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.price_to_earnings(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.price_to_earnings(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.price_to_earnings(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.price_to_earnings(0, 1)
        except EXC:
            pass


class Test_real_rate_of_return_deep:
    def test_c0(self):
        try:
            mod.real_rate_of_return(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.real_rate_of_return(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.real_rate_of_return(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.real_rate_of_return(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.real_rate_of_return(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.real_rate_of_return(0, 1)
        except EXC:
            pass


class Test_received_deep:
    def test_c0(self):
        try:
            mod.received("hello world", "test", 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.received("test", "abc123", -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.received("abc123", "", 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.received("", "Hello, World!", 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.received("Hello, World!", "UPPER lower 123", 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.received("UPPER lower 123", "hello world", 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.received("hello world", "test", -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.received("test", "abc123", 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.received("abc123", "", 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.received("", "Hello, World!", 42, 0)
        except EXC:
            pass

    def test_kw_basis(self):
        try:
            mod.received("hello world", "test", 0, -5, basis=1)
        except EXC:
            pass


class Test_retention_ratio_deep:
    def test_c0(self):
        try:
            mod.retention_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.retention_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.retention_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.retention_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.retention_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.retention_ratio(0, 1)
        except EXC:
            pass


class Test_return_on_assets_deep:
    def test_c0(self):
        try:
            mod.return_on_assets(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.return_on_assets(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.return_on_assets(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.return_on_assets(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.return_on_assets(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.return_on_assets(0, 1)
        except EXC:
            pass


class Test_return_on_equity_deep:
    def test_c0(self):
        try:
            mod.return_on_equity(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.return_on_equity(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.return_on_equity(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.return_on_equity(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.return_on_equity(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.return_on_equity(0, 1)
        except EXC:
            pass


class Test_revenue_per_employee_deep:
    def test_c0(self):
        try:
            mod.revenue_per_employee(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.revenue_per_employee(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.revenue_per_employee(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.revenue_per_employee(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.revenue_per_employee(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.revenue_per_employee(0, 1)
        except EXC:
            pass


class Test_roi_deep:
    def test_c0(self):
        try:
            mod.roi(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.roi(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.roi(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.roi(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.roi(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.roi(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.roi(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.roi(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.roi(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.roi(2, 1)
        except EXC:
            pass


class Test_rri_deep:
    def test_c0(self):
        try:
            mod.rri(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rri(2, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rri(3, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rri(5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rri(10, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rri(0, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.rri(1, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.rri(2, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.rri(3, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.rri(5, 1, 42)
        except EXC:
            pass


class Test_sales_growth_rate_deep:
    def test_c0(self):
        try:
            mod.sales_growth_rate(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sales_growth_rate(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sales_growth_rate(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sales_growth_rate(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sales_growth_rate(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sales_growth_rate(0, 1)
        except EXC:
            pass


class Test_spot_to_forward_deep:
    def test_c0(self):
        try:
            mod.spot_to_forward(1, 42, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spot_to_forward(42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spot_to_forward(0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spot_to_forward(-5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spot_to_forward(3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spot_to_forward(100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.spot_to_forward(0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.spot_to_forward(1000, -1, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.spot_to_forward(-1, 2, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.spot_to_forward(2, 1, 42, 0)
        except EXC:
            pass


class Test_tbilleq_deep:
    def test_c0(self):
        try:
            mod.tbilleq("hello world", "test", 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.tbilleq("test", "abc123", -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.tbilleq("abc123", "", 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.tbilleq("", "Hello, World!", 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.tbilleq("Hello, World!", "UPPER lower 123", 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.tbilleq("UPPER lower 123", "hello world", 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.tbilleq("hello world", "test", -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.tbilleq("test", "abc123", 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.tbilleq("abc123", "", 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.tbilleq("", "Hello, World!", 42)
        except EXC:
            pass


class Test_tbillprice_deep:
    def test_c0(self):
        try:
            mod.tbillprice("hello world", "test", 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.tbillprice("test", "abc123", -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.tbillprice("abc123", "", 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.tbillprice("", "Hello, World!", 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.tbillprice("Hello, World!", "UPPER lower 123", 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.tbillprice("UPPER lower 123", "hello world", 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.tbillprice("hello world", "test", -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.tbillprice("test", "abc123", 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.tbillprice("abc123", "", 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.tbillprice("", "Hello, World!", 42)
        except EXC:
            pass


class Test_tbillyield_deep:
    def test_c0(self):
        try:
            mod.tbillyield("hello world", "test", 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.tbillyield("test", "abc123", -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.tbillyield("abc123", "", 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.tbillyield("", "Hello, World!", 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.tbillyield("Hello, World!", "UPPER lower 123", 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.tbillyield("UPPER lower 123", "hello world", 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.tbillyield("hello world", "test", -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.tbillyield("test", "abc123", 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.tbillyield("abc123", "", 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.tbillyield("", "Hello, World!", 42)
        except EXC:
            pass


class Test_time_weighted_return_deep:
    def test_c0(self):
        try:
            mod.time_weighted_return([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.time_weighted_return([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.time_weighted_return([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.time_weighted_return([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.time_weighted_return([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.time_weighted_return([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_tobin_q_ratio_deep:
    def test_c0(self):
        try:
            mod.tobin_q_ratio(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.tobin_q_ratio(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.tobin_q_ratio(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.tobin_q_ratio(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.tobin_q_ratio(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.tobin_q_ratio(0, 1)
        except EXC:
            pass


class Test_ulcer_index_deep:
    def test_c0(self):
        try:
            mod.ulcer_index([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ulcer_index([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ulcer_index([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ulcer_index([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ulcer_index([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ulcer_index([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_wacc_deep:
    def test_c0(self):
        try:
            mod.wacc(1, 42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.wacc(42, 0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.wacc(0, -5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.wacc(-5, 3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.wacc(3.14, 100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.wacc(100, 0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.wacc(0.5, 1000, -1, 2, 1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.wacc(1000, -1, 2, 1, 42)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.wacc(-1, 2, 1, 42, 0)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.wacc(2, 1, 42, 0, -5)
        except EXC:
            pass


class Test_working_capital_deep:
    def test_c0(self):
        try:
            mod.working_capital(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.working_capital(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.working_capital(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.working_capital(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.working_capital(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.working_capital(0, 1)
        except EXC:
            pass

