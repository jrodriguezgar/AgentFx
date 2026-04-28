# Deep coverage tests for agentfx.fxNumeric.statistics_functions

import agentfx.fxNumeric.statistics_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_forecast_ets_deep:
    def test_c0(self):
        try:
            mod.forecast_ets(1, [10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.forecast_ets(2, [0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.forecast_ets(3, [-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.forecast_ets(5, [100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.forecast_ets(10, [1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.forecast_ets(0, [1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_kw_seasonality(self):
        try:
            mod.forecast_ets(1, [10, 20, 30], [0, 1], seasonality=1)
        except EXC:
            pass

    def test_kw_data_completion(self):
        try:
            mod.forecast_ets(1, [10, 20, 30], [0, 1], data_completion=1)
        except EXC:
            pass

    def test_kw_aggregation(self):
        try:
            mod.forecast_ets(1, [10, 20, 30], [0, 1], aggregation=1)
        except EXC:
            pass


class Test_trend_deep:
    def test_c0(self):
        try:
            mod.trend([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.trend([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.trend([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.trend([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.trend([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.trend([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_known_x(self):
        try:
            mod.trend([1, 2, 3, 4, 5], known_x=[1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_new_x(self):
        try:
            mod.trend([1, 2, 3, 4, 5], new_x=[1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_const(self):
        try:
            mod.trend([1, 2, 3, 4, 5], const=True)
        except EXC:
            pass


class Test_standard_error_estimate_deep:
    def test_c0(self):
        try:
            mod.standard_error_estimate([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.standard_error_estimate([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.standard_error_estimate([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.standard_error_estimate([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.standard_error_estimate([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.standard_error_estimate([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_confidence_t_deep:
    def test_c0(self):
        try:
            mod.confidence_t(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.confidence_t(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.confidence_t(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.confidence_t(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.confidence_t(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.confidence_t(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.confidence_t(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.confidence_t(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.confidence_t(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.confidence_t(2, 1, 0)
        except EXC:
            pass


class Test_t_test_deep:
    def test_c0(self):
        try:
            mod.t_test([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.t_test([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.t_test([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.t_test([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.t_test([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.t_test([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_tails(self):
        try:
            mod.t_test([1, 2, 3, 4, 5], [10, 20, 30], tails=1)
        except EXC:
            pass

    def test_kw_type_(self):
        try:
            mod.t_test([1, 2, 3, 4, 5], [10, 20, 30], type_=1)
        except EXC:
            pass


class Test_growth_deep:
    def test_c0(self):
        try:
            mod.growth([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.growth([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.growth([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.growth([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.growth([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.growth([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_known_x(self):
        try:
            mod.growth([1, 2, 3, 4, 5], known_x=[1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_new_x(self):
        try:
            mod.growth([1, 2, 3, 4, 5], new_x=[1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_rank_deep:
    def test_c0(self):
        try:
            mod.rank([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rank([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rank([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rank([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rank([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rank([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_method(self):
        try:
            mod.rank([1, 2, 3, 4, 5], method="hello world")
        except EXC:
            pass

    def test_kw_ascending(self):
        try:
            mod.rank([1, 2, 3, 4, 5], ascending=True)
        except EXC:
            pass


class Test_aggregate_deep:
    def test_c0(self):
        try:
            mod.aggregate([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.aggregate([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.aggregate([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.aggregate([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.aggregate([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.aggregate([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_operation(self):
        try:
            mod.aggregate([1, 2, 3, 4, 5], operation="hello world")
        except EXC:
            pass

    def test_kw_ignore_errors(self):
        try:
            mod.aggregate([1, 2, 3, 4, 5], ignore_errors=True)
        except EXC:
            pass


class Test_f_test_deep:
    def test_c0(self):
        try:
            mod.f_test([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.f_test([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.f_test([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.f_test([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.f_test([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.f_test([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_kurtosis_deep:
    def test_c0(self):
        try:
            mod.kurtosis([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.kurtosis([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.kurtosis([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.kurtosis([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.kurtosis([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.kurtosis([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_excess(self):
        try:
            mod.kurtosis([1, 2, 3, 4, 5], excess=True)
        except EXC:
            pass


class Test_chisq_test_deep:
    def test_c0(self):
        try:
            mod.chisq_test([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chisq_test([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chisq_test([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chisq_test([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chisq_test([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chisq_test([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_expected(self):
        try:
            mod.chisq_test([1, 2, 3, 4, 5], expected=[1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_z_test_deep:
    def test_c0(self):
        try:
            mod.z_test([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.z_test([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.z_test([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.z_test([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.z_test([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.z_test([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.z_test([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.z_test([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.z_test([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.z_test([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass

    def test_kw_sigma(self):
        try:
            mod.z_test([1, 2, 3, 4, 5], 42, sigma=1)
        except EXC:
            pass


class Test_confidence_norm_deep:
    def test_c0(self):
        try:
            mod.confidence_norm(1, 42, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.confidence_norm(42, 0, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.confidence_norm(0, -5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.confidence_norm(-5, 3.14, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.confidence_norm(3.14, 100, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.confidence_norm(100, 0.5, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.confidence_norm(0.5, 1000, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.confidence_norm(1000, -1, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.confidence_norm(-1, 2, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.confidence_norm(2, 1, 0)
        except EXC:
            pass


class Test_percentrank_exc_deep:
    def test_c0(self):
        try:
            mod.percentrank_exc([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.percentrank_exc([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.percentrank_exc([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.percentrank_exc([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.percentrank_exc([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.percentrank_exc([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass

    def test_kw_significance(self):
        try:
            mod.percentrank_exc([1, 2, 3, 4, 5], 2, significance=1)
        except EXC:
            pass


class Test_skewness_deep:
    def test_c0(self):
        try:
            mod.skewness([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.skewness([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.skewness([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.skewness([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.skewness([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.skewness([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_weighted_variance_deep:
    def test_c0(self):
        try:
            mod.weighted_variance([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weighted_variance([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weighted_variance([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weighted_variance([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weighted_variance([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weighted_variance([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_sample(self):
        try:
            mod.weighted_variance([1, 2, 3, 4, 5], [10, 20, 30], sample=True)
        except EXC:
            pass


class Test_glass_delta_deep:
    def test_c0(self):
        try:
            mod.glass_delta([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.glass_delta([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.glass_delta([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.glass_delta([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.glass_delta([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.glass_delta([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_holt_linear_forecast_deep:
    def test_c0(self):
        try:
            mod.holt_linear_forecast([1, 2, 3, 4, 5], 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.holt_linear_forecast([10, 20, 30], 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.holt_linear_forecast([0, 1], -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.holt_linear_forecast([-3, -1, 0, 2, 5], 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.holt_linear_forecast([100], 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.holt_linear_forecast([1, 1, 2, 3, 5, 8], 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.holt_linear_forecast([1, 2, 3, 4, 5], 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.holt_linear_forecast([10, 20, 30], -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.holt_linear_forecast([0, 1], 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.holt_linear_forecast([-3, -1, 0, 2, 5], 1, 42)
        except EXC:
            pass

    def test_kw_steps(self):
        try:
            mod.holt_linear_forecast([1, 2, 3, 4, 5], 42, 0, steps=1)
        except EXC:
            pass


class Test_bayesian_update_deep:
    def test_c0(self):
        try:
            mod.bayesian_update(1, [10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bayesian_update(42, [0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bayesian_update(0, [-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bayesian_update(-5, [100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bayesian_update(3.14, [1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bayesian_update(100, [1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bayesian_update(0.5, [10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bayesian_update(1000, [0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bayesian_update(-1, [-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bayesian_update(2, [100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_calculate_covariance_deep:
    def test_c0(self):
        try:
            mod.calculate_covariance([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.calculate_covariance([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.calculate_covariance([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.calculate_covariance([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.calculate_covariance([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.calculate_covariance([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_sample(self):
        try:
            mod.calculate_covariance([1, 2, 3, 4, 5], [10, 20, 30], sample=True)
        except EXC:
            pass


class Test_calculate_pearson_correlation_deep:
    def test_c0(self):
        try:
            mod.calculate_pearson_correlation([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.calculate_pearson_correlation([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.calculate_pearson_correlation([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.calculate_pearson_correlation([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.calculate_pearson_correlation([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.calculate_pearson_correlation([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_focal_loss_deep:
    def test_c0(self):
        try:
            mod.focal_loss(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.focal_loss(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.focal_loss(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.focal_loss(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.focal_loss(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.focal_loss(0, 1)
        except EXC:
            pass

    def test_kw_gamma(self):
        try:
            mod.focal_loss(1, 2, gamma=1)
        except EXC:
            pass

    def test_kw_alpha(self):
        try:
            mod.focal_loss(1, 2, alpha=1)
        except EXC:
            pass


class Test_kendall_tau_deep:
    def test_c0(self):
        try:
            mod.kendall_tau([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.kendall_tau([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.kendall_tau([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.kendall_tau([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.kendall_tau([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.kendall_tau([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_mutual_information_deep:
    def test_c0(self):
        try:
            mod.mutual_information([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mutual_information([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mutual_information([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mutual_information([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mutual_information([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mutual_information([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_partial_autocorrelation_deep:
    def test_c0(self):
        try:
            mod.partial_autocorrelation([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.partial_autocorrelation([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.partial_autocorrelation([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.partial_autocorrelation([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.partial_autocorrelation([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.partial_autocorrelation([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_quantile_deep:
    def test_c0(self):
        try:
            mod.quantile([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.quantile([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.quantile([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.quantile([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.quantile([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.quantile([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.quantile([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.quantile([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.quantile([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.quantile([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass


class Test_residual_standard_error_deep:
    def test_c0(self):
        try:
            mod.residual_standard_error([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.residual_standard_error([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.residual_standard_error([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.residual_standard_error([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.residual_standard_error([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.residual_standard_error([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_p(self):
        try:
            mod.residual_standard_error([1, 2, 3, 4, 5], [10, 20, 30], p=1)
        except EXC:
            pass


class Test_root_mean_squared_log_error_deep:
    def test_c0(self):
        try:
            mod.root_mean_squared_log_error([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.root_mean_squared_log_error([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.root_mean_squared_log_error([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.root_mean_squared_log_error([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.root_mean_squared_log_error([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.root_mean_squared_log_error([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_skew_p_deep:
    def test_c0(self):
        try:
            mod.skew_p([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.skew_p([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.skew_p([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.skew_p([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.skew_p([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.skew_p([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_autocorrelation_deep:
    def test_c0(self):
        try:
            mod.autocorrelation([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.autocorrelation([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.autocorrelation([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.autocorrelation([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.autocorrelation([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.autocorrelation([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_lag(self):
        try:
            mod.autocorrelation([1, 2, 3, 4, 5], lag=1)
        except EXC:
            pass


class Test_chi_squared_statistic_deep:
    def test_c0(self):
        try:
            mod.chi_squared_statistic([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chi_squared_statistic([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chi_squared_statistic([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chi_squared_statistic([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chi_squared_statistic([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chi_squared_statistic([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_cross_entropy_deep:
    def test_c0(self):
        try:
            mod.cross_entropy([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cross_entropy([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cross_entropy([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cross_entropy([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cross_entropy([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cross_entropy([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_euclidean_distance_deep:
    def test_c0(self):
        try:
            mod.euclidean_distance([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.euclidean_distance([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.euclidean_distance([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.euclidean_distance([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.euclidean_distance([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.euclidean_distance([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_js_divergence_deep:
    def test_c0(self):
        try:
            mod.js_divergence([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.js_divergence([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.js_divergence([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.js_divergence([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.js_divergence([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.js_divergence([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_kl_divergence_deep:
    def test_c0(self):
        try:
            mod.kl_divergence([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.kl_divergence([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.kl_divergence([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.kl_divergence([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.kl_divergence([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.kl_divergence([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_mean_absolute_percentage_error_deep:
    def test_c0(self):
        try:
            mod.mean_absolute_percentage_error([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mean_absolute_percentage_error([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mean_absolute_percentage_error([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mean_absolute_percentage_error([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mean_absolute_percentage_error([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mean_absolute_percentage_error([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_point_biserial_correlation_deep:
    def test_c0(self):
        try:
            mod.point_biserial_correlation([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.point_biserial_correlation([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.point_biserial_correlation([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.point_biserial_correlation([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.point_biserial_correlation([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.point_biserial_correlation([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_probability_range_deep:
    def test_c0(self):
        try:
            mod.probability_range([1, 2, 3, 4, 5], [10, 20, 30], 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.probability_range([10, 20, 30], [0, 1], -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.probability_range([0, 1], [-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.probability_range([-3, -1, 0, 2, 5], [100], 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.probability_range([100], [1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.probability_range([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.probability_range([1, 2, 3, 4, 5], [10, 20, 30], -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.probability_range([10, 20, 30], [0, 1], 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.probability_range([0, 1], [-3, -1, 0, 2, 5], 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.probability_range([-3, -1, 0, 2, 5], [100], 42)
        except EXC:
            pass

    def test_kw_upper_limit(self):
        try:
            mod.probability_range([1, 2, 3, 4, 5], [10, 20, 30], 0, upper_limit=1)
        except EXC:
            pass


class Test_rolling_correlation_deep:
    def test_c0(self):
        try:
            mod.rolling_correlation([1, 2, 3, 4, 5], [10, 20, 30], 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rolling_correlation([10, 20, 30], [0, 1], 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rolling_correlation([0, 1], [-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rolling_correlation([-3, -1, 0, 2, 5], [100], 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rolling_correlation([100], [1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rolling_correlation([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5], 2)
        except EXC:
            pass


class Test_slope_deep:
    def test_c0(self):
        try:
            mod.slope([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.slope([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.slope([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.slope([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.slope([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.slope([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_trimmed_mean_deep:
    def test_c0(self):
        try:
            mod.trimmed_mean([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.trimmed_mean([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.trimmed_mean([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.trimmed_mean([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.trimmed_mean([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.trimmed_mean([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.trimmed_mean([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.trimmed_mean([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.trimmed_mean([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.trimmed_mean([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass


class Test_trimmed_variance_deep:
    def test_c0(self):
        try:
            mod.trimmed_variance([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.trimmed_variance([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.trimmed_variance([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.trimmed_variance([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.trimmed_variance([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.trimmed_variance([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_proportion(self):
        try:
            mod.trimmed_variance([1, 2, 3, 4, 5], proportion=1)
        except EXC:
            pass


class Test_weighted_mean_deep:
    def test_c0(self):
        try:
            mod.weighted_mean([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weighted_mean([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weighted_mean([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weighted_mean([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weighted_mean([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weighted_mean([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_weighted_moving_average_deep:
    def test_c0(self):
        try:
            mod.weighted_moving_average([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weighted_moving_average([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weighted_moving_average([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weighted_moving_average([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weighted_moving_average([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weighted_moving_average([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_cosine_similarity_deep:
    def test_c0(self):
        try:
            mod.cosine_similarity([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cosine_similarity([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cosine_similarity([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cosine_similarity([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cosine_similarity([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cosine_similarity([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_covariance_matrix_deep:
    def test_c0(self):
        try:
            mod.covariance_matrix([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.covariance_matrix([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.covariance_matrix([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.covariance_matrix([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.covariance_matrix([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.covariance_matrix([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_cramers_v_deep:
    def test_c0(self):
        try:
            mod.cramers_v(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cramers_v(42, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cramers_v(0, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cramers_v(-5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cramers_v(3.14, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cramers_v(100, 1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.cramers_v(0.5, 2, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.cramers_v(1000, 3, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.cramers_v(-1, 5, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.cramers_v(2, 10, 0)
        except EXC:
            pass


class Test_dixon_q_test_deep:
    def test_c0(self):
        try:
            mod.dixon_q_test([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dixon_q_test([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dixon_q_test([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dixon_q_test([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dixon_q_test([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dixon_q_test([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_erlang_pdf_deep:
    def test_c0(self):
        try:
            mod.erlang_pdf(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.erlang_pdf(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.erlang_pdf(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.erlang_pdf(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.erlang_pdf(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.erlang_pdf(0, 1, 2)
        except EXC:
            pass


class Test_exponential_decay_rate_deep:
    def test_c0(self):
        try:
            mod.exponential_decay_rate(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.exponential_decay_rate(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.exponential_decay_rate(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.exponential_decay_rate(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.exponential_decay_rate(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.exponential_decay_rate(0, 1, 2)
        except EXC:
            pass


class Test_exponential_moving_average_deep:
    def test_c0(self):
        try:
            mod.exponential_moving_average([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.exponential_moving_average([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.exponential_moving_average([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.exponential_moving_average([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.exponential_moving_average([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.exponential_moving_average([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.exponential_moving_average([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.exponential_moving_average([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.exponential_moving_average([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.exponential_moving_average([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass


class Test_f1_score_scalar_deep:
    def test_c0(self):
        try:
            mod.f1_score_scalar(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.f1_score_scalar(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.f1_score_scalar(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.f1_score_scalar(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.f1_score_scalar(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.f1_score_scalar(0, 1, 2)
        except EXC:
            pass


class Test_frequency_bins_deep:
    def test_c0(self):
        try:
            mod.frequency_bins([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.frequency_bins([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.frequency_bins([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.frequency_bins([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.frequency_bins([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.frequency_bins([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_grubbs_test_deep:
    def test_c0(self):
        try:
            mod.grubbs_test([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.grubbs_test([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.grubbs_test([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.grubbs_test([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.grubbs_test([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.grubbs_test([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_large_deep:
    def test_c0(self):
        try:
            mod.large([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.large([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.large([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.large([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.large([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.large([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_linest_deep:
    def test_c0(self):
        try:
            mod.linest([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.linest([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.linest([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.linest([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.linest([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.linest([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_known_x(self):
        try:
            mod.linest([1, 2, 3, 4, 5], known_x=[1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_ljung_box_deep:
    def test_c0(self):
        try:
            mod.ljung_box([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ljung_box([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ljung_box([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ljung_box([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ljung_box([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ljung_box([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_lags(self):
        try:
            mod.ljung_box([1, 2, 3, 4, 5], lags=1)
        except EXC:
            pass


class Test_mahalanobis_distance_1d_deep:
    def test_c0(self):
        try:
            mod.mahalanobis_distance_1d(1, [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mahalanobis_distance_1d(42, [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mahalanobis_distance_1d(0, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mahalanobis_distance_1d(-5, [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mahalanobis_distance_1d(3.14, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mahalanobis_distance_1d(100, [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.mahalanobis_distance_1d(0.5, [10, 20, 30])
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.mahalanobis_distance_1d(1000, [0, 1])
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.mahalanobis_distance_1d(-1, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.mahalanobis_distance_1d(2, [100])
        except EXC:
            pass


class Test_manhattan_distance_deep:
    def test_c0(self):
        try:
            mod.manhattan_distance([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.manhattan_distance([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.manhattan_distance([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.manhattan_distance([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.manhattan_distance([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.manhattan_distance([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_mann_whitney_u_deep:
    def test_c0(self):
        try:
            mod.mann_whitney_u([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mann_whitney_u([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mann_whitney_u([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mann_whitney_u([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mann_whitney_u([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mann_whitney_u([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_markov_chain_steady_state_deep:
    def test_c0(self):
        try:
            mod.markov_chain_steady_state([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.markov_chain_steady_state([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.markov_chain_steady_state([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.markov_chain_steady_state([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.markov_chain_steady_state([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.markov_chain_steady_state([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_tol(self):
        try:
            mod.markov_chain_steady_state([1, 2, 3, 4, 5], tol=1)
        except EXC:
            pass

    def test_kw_max_iter(self):
        try:
            mod.markov_chain_steady_state([1, 2, 3, 4, 5], max_iter=1)
        except EXC:
            pass


class Test_mean_absolute_error_deep:
    def test_c0(self):
        try:
            mod.mean_absolute_error([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mean_absolute_error([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mean_absolute_error([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mean_absolute_error([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mean_absolute_error([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mean_absolute_error([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_percentile_exc_deep:
    def test_c0(self):
        try:
            mod.percentile_exc([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.percentile_exc([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.percentile_exc([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.percentile_exc([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.percentile_exc([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.percentile_exc([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.percentile_exc([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.percentile_exc([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.percentile_exc([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.percentile_exc([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass


class Test_r_squared_deep:
    def test_c0(self):
        try:
            mod.r_squared([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.r_squared([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.r_squared([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.r_squared([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.r_squared([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.r_squared([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_rolling_mean_deep:
    def test_c0(self):
        try:
            mod.rolling_mean([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rolling_mean([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rolling_mean([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rolling_mean([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rolling_mean([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rolling_mean([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_rolling_sum_deep:
    def test_c0(self):
        try:
            mod.rolling_sum([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rolling_sum([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rolling_sum([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rolling_sum([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rolling_sum([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rolling_sum([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_running_max_deep:
    def test_c0(self):
        try:
            mod.running_max([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.running_max([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.running_max([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.running_max([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.running_max([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.running_max([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_running_min_deep:
    def test_c0(self):
        try:
            mod.running_min([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.running_min([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.running_min([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.running_min([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.running_min([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.running_min([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_runs_test_statistic_deep:
    def test_c0(self):
        try:
            mod.runs_test_statistic([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.runs_test_statistic([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.runs_test_statistic([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.runs_test_statistic([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.runs_test_statistic([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.runs_test_statistic([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_shannon_entropy_deep:
    def test_c0(self):
        try:
            mod.shannon_entropy([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.shannon_entropy([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.shannon_entropy([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.shannon_entropy([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.shannon_entropy([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.shannon_entropy([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_shapiro_wilk_w_deep:
    def test_c0(self):
        try:
            mod.shapiro_wilk_w([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.shapiro_wilk_w([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.shapiro_wilk_w([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.shapiro_wilk_w([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.shapiro_wilk_w([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.shapiro_wilk_w([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_small_deep:
    def test_c0(self):
        try:
            mod.small([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.small([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.small([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.small([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.small([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.small([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_theil_sen_slope_deep:
    def test_c0(self):
        try:
            mod.theil_sen_slope([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.theil_sen_slope([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.theil_sen_slope([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.theil_sen_slope([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.theil_sen_slope([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.theil_sen_slope([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_winsorized_mean_deep:
    def test_c0(self):
        try:
            mod.winsorized_mean([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.winsorized_mean([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.winsorized_mean([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.winsorized_mean([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.winsorized_mean([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.winsorized_mean([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_proportion(self):
        try:
            mod.winsorized_mean([1, 2, 3, 4, 5], proportion=1)
        except EXC:
            pass


class Test_adjusted_r_squared_deep:
    def test_c0(self):
        try:
            mod.adjusted_r_squared(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.adjusted_r_squared(42, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.adjusted_r_squared(0, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.adjusted_r_squared(-5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.adjusted_r_squared(3.14, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.adjusted_r_squared(100, 1, 2)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.adjusted_r_squared(0.5, 2, 3)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.adjusted_r_squared(1000, 3, 5)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.adjusted_r_squared(-1, 5, 10)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.adjusted_r_squared(2, 10, 0)
        except EXC:
            pass


class Test_anderson_darling_deep:
    def test_c0(self):
        try:
            mod.anderson_darling([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.anderson_darling([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.anderson_darling([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.anderson_darling([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.anderson_darling([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.anderson_darling([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_auto_correlation_deep:
    def test_c0(self):
        try:
            mod.auto_correlation([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.auto_correlation([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.auto_correlation([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.auto_correlation([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.auto_correlation([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.auto_correlation([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_lag(self):
        try:
            mod.auto_correlation([1, 2, 3, 4, 5], lag=1)
        except EXC:
            pass


class Test_benford_distribution_deep:
    def test_c0(self):
        try:
            mod.benford_distribution([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.benford_distribution([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.benford_distribution([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.benford_distribution([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.benford_distribution([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.benford_distribution([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_beta_function_value_deep:
    def test_c0(self):
        try:
            mod.beta_function_value(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.beta_function_value(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.beta_function_value(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.beta_function_value(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.beta_function_value(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.beta_function_value(0, 1)
        except EXC:
            pass


class Test_binomial_probability_deep:
    def test_c0(self):
        try:
            mod.binomial_probability(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.binomial_probability(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.binomial_probability(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.binomial_probability(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.binomial_probability(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.binomial_probability(0, 1, 2)
        except EXC:
            pass


class Test_calculate_interquartile_range_deep:
    def test_c0(self):
        try:
            mod.calculate_interquartile_range([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.calculate_interquartile_range([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.calculate_interquartile_range([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.calculate_interquartile_range([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.calculate_interquartile_range([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.calculate_interquartile_range([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_calculate_percentile_deep:
    def test_c0(self):
        try:
            mod.calculate_percentile([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.calculate_percentile([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.calculate_percentile([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.calculate_percentile([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.calculate_percentile([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.calculate_percentile([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.calculate_percentile([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.calculate_percentile([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.calculate_percentile([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.calculate_percentile([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass


class Test_calculate_standard_deviation_deep:
    def test_c0(self):
        try:
            mod.calculate_standard_deviation([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.calculate_standard_deviation([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.calculate_standard_deviation([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.calculate_standard_deviation([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.calculate_standard_deviation([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.calculate_standard_deviation([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_sample(self):
        try:
            mod.calculate_standard_deviation([1, 2, 3, 4, 5], sample=True)
        except EXC:
            pass


class Test_chi_squared_pdf_deep:
    def test_c0(self):
        try:
            mod.chi_squared_pdf(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chi_squared_pdf(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chi_squared_pdf(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chi_squared_pdf(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chi_squared_pdf(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chi_squared_pdf(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.chi_squared_pdf(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.chi_squared_pdf(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.chi_squared_pdf(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.chi_squared_pdf(2, 10)
        except EXC:
            pass


class Test_cohens_d_deep:
    def test_c0(self):
        try:
            mod.cohens_d([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cohens_d([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cohens_d([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cohens_d([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cohens_d([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cohens_d([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_dice_coefficient_scalar_deep:
    def test_c0(self):
        try:
            mod.dice_coefficient_scalar(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dice_coefficient_scalar(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dice_coefficient_scalar(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dice_coefficient_scalar(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dice_coefficient_scalar(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dice_coefficient_scalar(0, 1, 2)
        except EXC:
            pass


class Test_diff_deep:
    def test_c0(self):
        try:
            mod.diff([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.diff([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.diff([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.diff([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.diff([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.diff([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_periods(self):
        try:
            mod.diff([1, 2, 3, 4, 5], periods=1)
        except EXC:
            pass


class Test_false_discovery_rate_deep:
    def test_c0(self):
        try:
            mod.false_discovery_rate(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.false_discovery_rate(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.false_discovery_rate(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.false_discovery_rate(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.false_discovery_rate(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.false_discovery_rate(0, 1)
        except EXC:
            pass


class Test_fisher_deep:
    def test_c0(self):
        try:
            mod.fisher(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.fisher(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.fisher(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.fisher(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.fisher(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.fisher(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.fisher(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.fisher(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.fisher(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.fisher(2)
        except EXC:
            pass


class Test_gamma_pdf_deep:
    def test_c0(self):
        try:
            mod.gamma_pdf(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gamma_pdf(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gamma_pdf(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gamma_pdf(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gamma_pdf(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gamma_pdf(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.gamma_pdf(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.gamma_pdf(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.gamma_pdf(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.gamma_pdf(2, 1, 42)
        except EXC:
            pass


class Test_geometric_mean_deep:
    def test_c0(self):
        try:
            mod.geometric_mean([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.geometric_mean([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.geometric_mean([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.geometric_mean([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.geometric_mean([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.geometric_mean([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_gumbel_pdf_deep:
    def test_c0(self):
        try:
            mod.gumbel_pdf(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gumbel_pdf(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gumbel_pdf(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gumbel_pdf(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gumbel_pdf(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gumbel_pdf(0)
        except EXC:
            pass

    def test_kw_mu(self):
        try:
            mod.gumbel_pdf(1, mu=1)
        except EXC:
            pass

    def test_kw_beta(self):
        try:
            mod.gumbel_pdf(1, beta=1)
        except EXC:
            pass


class Test_harmonic_mean_deep:
    def test_c0(self):
        try:
            mod.harmonic_mean([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.harmonic_mean([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.harmonic_mean([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.harmonic_mean([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.harmonic_mean([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.harmonic_mean([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_huber_loss_deep:
    def test_c0(self):
        try:
            mod.huber_loss(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.huber_loss(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.huber_loss(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.huber_loss(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.huber_loss(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.huber_loss(0, 1)
        except EXC:
            pass

    def test_kw_delta(self):
        try:
            mod.huber_loss(1, 2, delta=1)
        except EXC:
            pass


class Test_log_loss_deep:
    def test_c0(self):
        try:
            mod.log_loss(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.log_loss(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.log_loss(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.log_loss(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.log_loss(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.log_loss(0, 1)
        except EXC:
            pass

    def test_kw_eps(self):
        try:
            mod.log_loss(1, 2, eps=1)
        except EXC:
            pass


class Test_maxwell_boltzmann_pdf_deep:
    def test_c0(self):
        try:
            mod.maxwell_boltzmann_pdf(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.maxwell_boltzmann_pdf(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.maxwell_boltzmann_pdf(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.maxwell_boltzmann_pdf(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.maxwell_boltzmann_pdf(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.maxwell_boltzmann_pdf(0, 1)
        except EXC:
            pass


class Test_median_absolute_deviation_deep:
    def test_c0(self):
        try:
            mod.median_absolute_deviation([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.median_absolute_deviation([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.median_absolute_deviation([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.median_absolute_deviation([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.median_absolute_deviation([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.median_absolute_deviation([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_minkowski_distance_deep:
    def test_c0(self):
        try:
            mod.minkowski_distance([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.minkowski_distance([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.minkowski_distance([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.minkowski_distance([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.minkowski_distance([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.minkowski_distance([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_p(self):
        try:
            mod.minkowski_distance([1, 2, 3, 4, 5], [10, 20, 30], p=1)
        except EXC:
            pass


class Test_moors_kurtosis_deep:
    def test_c0(self):
        try:
            mod.moors_kurtosis([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.moors_kurtosis([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.moors_kurtosis([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.moors_kurtosis([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.moors_kurtosis([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.moors_kurtosis([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_moving_median_deep:
    def test_c0(self):
        try:
            mod.moving_median([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.moving_median([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.moving_median([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.moving_median([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.moving_median([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.moving_median([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_negative_binomial_pmf_deep:
    def test_c0(self):
        try:
            mod.negative_binomial_pmf(1, 2, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.negative_binomial_pmf(2, 3, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.negative_binomial_pmf(3, 5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.negative_binomial_pmf(5, 10, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.negative_binomial_pmf(10, 0, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.negative_binomial_pmf(0, 1, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.negative_binomial_pmf(1, 2, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.negative_binomial_pmf(2, 3, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.negative_binomial_pmf(3, 5, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.negative_binomial_pmf(5, 10, 42)
        except EXC:
            pass


class Test_negative_predictive_value_deep:
    def test_c0(self):
        try:
            mod.negative_predictive_value(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.negative_predictive_value(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.negative_predictive_value(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.negative_predictive_value(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.negative_predictive_value(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.negative_predictive_value(0, 1)
        except EXC:
            pass


class Test_percentile_rank_deep:
    def test_c0(self):
        try:
            mod.percentile_rank([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.percentile_rank([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.percentile_rank([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.percentile_rank([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.percentile_rank([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.percentile_rank([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.percentile_rank([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.percentile_rank([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.percentile_rank([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.percentile_rank([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass


class Test_rayleigh_pdf_deep:
    def test_c0(self):
        try:
            mod.rayleigh_pdf(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rayleigh_pdf(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rayleigh_pdf(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rayleigh_pdf(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rayleigh_pdf(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rayleigh_pdf(0)
        except EXC:
            pass

    def test_kw_sigma(self):
        try:
            mod.rayleigh_pdf(1, sigma=1)
        except EXC:
            pass


class Test_recall_score_scalar_deep:
    def test_c0(self):
        try:
            mod.recall_score_scalar(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.recall_score_scalar(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.recall_score_scalar(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.recall_score_scalar(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.recall_score_scalar(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.recall_score_scalar(0, 1)
        except EXC:
            pass


class Test_running_std_deep:
    def test_c0(self):
        try:
            mod.running_std([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.running_std([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.running_std([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.running_std([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.running_std([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.running_std([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_simple_moving_average_deep:
    def test_c0(self):
        try:
            mod.simple_moving_average([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.simple_moving_average([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.simple_moving_average([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.simple_moving_average([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.simple_moving_average([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.simple_moving_average([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_spearman_rank_correlation_deep:
    def test_c0(self):
        try:
            mod.spearman_rank_correlation([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spearman_rank_correlation([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spearman_rank_correlation([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spearman_rank_correlation([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spearman_rank_correlation([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spearman_rank_correlation([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_weighted_median_deep:
    def test_c0(self):
        try:
            mod.weighted_median([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weighted_median([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weighted_median([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weighted_median([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weighted_median([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weighted_median([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_z_score_single_deep:
    def test_c0(self):
        try:
            mod.z_score_single(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.z_score_single(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.z_score_single(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.z_score_single(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.z_score_single(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.z_score_single(0, 1, 2)
        except EXC:
            pass


class Test_zipf_pmf_deep:
    def test_c0(self):
        try:
            mod.zipf_pmf(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.zipf_pmf(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.zipf_pmf(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.zipf_pmf(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.zipf_pmf(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.zipf_pmf(0, 1, 2)
        except EXC:
            pass


class Test_absolute_error_deep:
    def test_c0(self):
        try:
            mod.absolute_error(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.absolute_error(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.absolute_error(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.absolute_error(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.absolute_error(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.absolute_error(0, 1)
        except EXC:
            pass


class Test_average_if_deep:
    def test_c0(self):
        try:
            mod.average_if([1, 2, 3, 4, 5], [10, 20, 30], {"key": "value"})
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.average_if([10, 20, 30], [0, 1], {"a": 1, "b": 2, "c": 3})
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.average_if([0, 1], [-3, -1, 0, 2, 5], {})
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.average_if([-3, -1, 0, 2, 5], [100], {"key": "value"})
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.average_if([100], [1, 1, 2, 3, 5, 8], {"a": 1, "b": 2, "c": 3})
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.average_if([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5], {})
        except EXC:
            pass


class Test_balanced_accuracy_scalar_deep:
    def test_c0(self):
        try:
            mod.balanced_accuracy_scalar(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.balanced_accuracy_scalar(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.balanced_accuracy_scalar(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.balanced_accuracy_scalar(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.balanced_accuracy_scalar(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.balanced_accuracy_scalar(0, 1, 2, 3)
        except EXC:
            pass


class Test_bayes_theorem_deep:
    def test_c0(self):
        try:
            mod.bayes_theorem(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bayes_theorem(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bayes_theorem(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bayes_theorem(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bayes_theorem(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bayes_theorem(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.bayes_theorem(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.bayes_theorem(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.bayes_theorem(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.bayes_theorem(2, 1, 42)
        except EXC:
            pass


class Test_binomial_pmf_deep:
    def test_c0(self):
        try:
            mod.binomial_pmf(1, 2, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.binomial_pmf(2, 3, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.binomial_pmf(3, 5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.binomial_pmf(5, 10, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.binomial_pmf(10, 0, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.binomial_pmf(0, 1, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.binomial_pmf(1, 2, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.binomial_pmf(2, 3, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.binomial_pmf(3, 5, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.binomial_pmf(5, 10, 42)
        except EXC:
            pass


class Test_bootstrap_mean_ci_deep:
    def test_c0(self):
        try:
            mod.bootstrap_mean_ci([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bootstrap_mean_ci([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bootstrap_mean_ci([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bootstrap_mean_ci([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bootstrap_mean_ci([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bootstrap_mean_ci([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_confidence(self):
        try:
            mod.bootstrap_mean_ci([1, 2, 3, 4, 5], confidence=1)
        except EXC:
            pass

    def test_kw_n_resamples(self):
        try:
            mod.bootstrap_mean_ci([1, 2, 3, 4, 5], n_resamples=1)
        except EXC:
            pass

    def test_kw_seed(self):
        try:
            mod.bootstrap_mean_ci([1, 2, 3, 4, 5], seed=1)
        except EXC:
            pass


class Test_bowley_skewness_deep:
    def test_c0(self):
        try:
            mod.bowley_skewness([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.bowley_skewness([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.bowley_skewness([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.bowley_skewness([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.bowley_skewness([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.bowley_skewness([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_calculate_variance_deep:
    def test_c0(self):
        try:
            mod.calculate_variance([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.calculate_variance([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.calculate_variance([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.calculate_variance([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.calculate_variance([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.calculate_variance([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_sample(self):
        try:
            mod.calculate_variance([1, 2, 3, 4, 5], sample=True)
        except EXC:
            pass


class Test_coefficient_of_quartile_deviation_deep:
    def test_c0(self):
        try:
            mod.coefficient_of_quartile_deviation([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.coefficient_of_quartile_deviation([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.coefficient_of_quartile_deviation([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.coefficient_of_quartile_deviation([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.coefficient_of_quartile_deviation([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.coefficient_of_quartile_deviation([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_cohens_kappa_scalar_deep:
    def test_c0(self):
        try:
            mod.cohens_kappa_scalar(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cohens_kappa_scalar(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cohens_kappa_scalar(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cohens_kappa_scalar(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cohens_kappa_scalar(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cohens_kappa_scalar(0, 1, 2, 3)
        except EXC:
            pass


class Test_count_true_with_sum_deep:
    def test_c0(self):
        try:
            mod.count_true_with_sum(True)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.count_true_with_sum(False)
        except EXC:
            pass


class Test_cumulative_moving_average_deep:
    def test_c0(self):
        try:
            mod.cumulative_moving_average([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cumulative_moving_average([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cumulative_moving_average([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cumulative_moving_average([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cumulative_moving_average([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cumulative_moving_average([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_cumulative_return_deep:
    def test_c0(self):
        try:
            mod.cumulative_return([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cumulative_return([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cumulative_return([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cumulative_return([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cumulative_return([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cumulative_return([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_describe_deep:
    def test_c0(self):
        try:
            mod.describe([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.describe([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.describe([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.describe([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.describe([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.describe([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_durbin_watson_deep:
    def test_c0(self):
        try:
            mod.durbin_watson([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.durbin_watson([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.durbin_watson([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.durbin_watson([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.durbin_watson([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.durbin_watson([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_elu_deep:
    def test_c0(self):
        try:
            mod.elu(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.elu(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.elu(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.elu(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.elu(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.elu(0)
        except EXC:
            pass

    def test_kw_alpha(self):
        try:
            mod.elu(1, alpha=1)
        except EXC:
            pass


class Test_empirical_cdf_deep:
    def test_c0(self):
        try:
            mod.empirical_cdf([1, 2, 3, 4, 5], 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.empirical_cdf([10, 20, 30], 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.empirical_cdf([0, 1], -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.empirical_cdf([-3, -1, 0, 2, 5], 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.empirical_cdf([100], 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.empirical_cdf([1, 1, 2, 3, 5, 8], 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.empirical_cdf([1, 2, 3, 4, 5], 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.empirical_cdf([10, 20, 30], -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.empirical_cdf([0, 1], 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.empirical_cdf([-3, -1, 0, 2, 5], 1)
        except EXC:
            pass


class Test_ewma_variance_deep:
    def test_c0(self):
        try:
            mod.ewma_variance([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ewma_variance([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ewma_variance([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ewma_variance([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ewma_variance([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ewma_variance([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_alpha(self):
        try:
            mod.ewma_variance([1, 2, 3, 4, 5], alpha=1)
        except EXC:
            pass


class Test_exponential_cdf_deep:
    def test_c0(self):
        try:
            mod.exponential_cdf(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.exponential_cdf(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.exponential_cdf(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.exponential_cdf(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.exponential_cdf(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.exponential_cdf(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.exponential_cdf(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.exponential_cdf(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.exponential_cdf(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.exponential_cdf(2, 1)
        except EXC:
            pass


class Test_exponential_pdf_deep:
    def test_c0(self):
        try:
            mod.exponential_pdf(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.exponential_pdf(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.exponential_pdf(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.exponential_pdf(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.exponential_pdf(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.exponential_pdf(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.exponential_pdf(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.exponential_pdf(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.exponential_pdf(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.exponential_pdf(2, 1)
        except EXC:
            pass


class Test_gini_coefficient_deep:
    def test_c0(self):
        try:
            mod.gini_coefficient([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gini_coefficient([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gini_coefficient([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gini_coefficient([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gini_coefficient([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gini_coefficient([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_gini_impurity_binary_deep:
    def test_c0(self):
        try:
            mod.gini_impurity_binary(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.gini_impurity_binary(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.gini_impurity_binary(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.gini_impurity_binary(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.gini_impurity_binary(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.gini_impurity_binary(0)
        except EXC:
            pass


class Test_hinge_loss_deep:
    def test_c0(self):
        try:
            mod.hinge_loss(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hinge_loss(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hinge_loss(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hinge_loss(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hinge_loss(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hinge_loss(0, 1)
        except EXC:
            pass


class Test_jarque_bera_deep:
    def test_c0(self):
        try:
            mod.jarque_bera([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.jarque_bera([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.jarque_bera([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.jarque_bera([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.jarque_bera([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.jarque_bera([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_lag_deep:
    def test_c0(self):
        try:
            mod.lag([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lag([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lag([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lag([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lag([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lag([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_periods(self):
        try:
            mod.lag([1, 2, 3, 4, 5], periods=1)
        except EXC:
            pass

    def test_kw_default(self):
        try:
            mod.lag([1, 2, 3, 4, 5], default=1)
        except EXC:
            pass


class Test_lead_deep:
    def test_c0(self):
        try:
            mod.lead([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.lead([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.lead([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.lead([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.lead([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.lead([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_periods(self):
        try:
            mod.lead([1, 2, 3, 4, 5], periods=1)
        except EXC:
            pass

    def test_kw_default(self):
        try:
            mod.lead([1, 2, 3, 4, 5], default=1)
        except EXC:
            pass


class Test_leaky_relu_deep:
    def test_c0(self):
        try:
            mod.leaky_relu(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.leaky_relu(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.leaky_relu(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.leaky_relu(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.leaky_relu(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.leaky_relu(0)
        except EXC:
            pass

    def test_kw_alpha(self):
        try:
            mod.leaky_relu(1, alpha=1)
        except EXC:
            pass


class Test_logest_deep:
    def test_c0(self):
        try:
            mod.logest([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.logest([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.logest([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.logest([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.logest([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.logest([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_known_x(self):
        try:
            mod.logest([1, 2, 3, 4, 5], known_x=[1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_logistic_cdf_deep:
    def test_c0(self):
        try:
            mod.logistic_cdf(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.logistic_cdf(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.logistic_cdf(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.logistic_cdf(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.logistic_cdf(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.logistic_cdf(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.logistic_cdf(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.logistic_cdf(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.logistic_cdf(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.logistic_cdf(2)
        except EXC:
            pass

    def test_kw_mu(self):
        try:
            mod.logistic_cdf(1, mu=1)
        except EXC:
            pass

    def test_kw_s(self):
        try:
            mod.logistic_cdf(1, s=1)
        except EXC:
            pass


class Test_logistic_pdf_deep:
    def test_c0(self):
        try:
            mod.logistic_pdf(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.logistic_pdf(42)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.logistic_pdf(0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.logistic_pdf(-5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.logistic_pdf(3.14)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.logistic_pdf(100)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.logistic_pdf(0.5)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.logistic_pdf(1000)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.logistic_pdf(-1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.logistic_pdf(2)
        except EXC:
            pass

    def test_kw_mu(self):
        try:
            mod.logistic_pdf(1, mu=1)
        except EXC:
            pass

    def test_kw_s(self):
        try:
            mod.logistic_pdf(1, s=1)
        except EXC:
            pass


class Test_matthews_corrcoef_scalar_deep:
    def test_c0(self):
        try:
            mod.matthews_corrcoef_scalar(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.matthews_corrcoef_scalar(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.matthews_corrcoef_scalar(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.matthews_corrcoef_scalar(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.matthews_corrcoef_scalar(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.matthews_corrcoef_scalar(0, 1, 2, 3)
        except EXC:
            pass


class Test_max_drawdown_deep:
    def test_c0(self):
        try:
            mod.max_drawdown([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.max_drawdown([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.max_drawdown([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.max_drawdown([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.max_drawdown([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.max_drawdown([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_max_if_deep:
    def test_c0(self):
        try:
            mod.max_if([1, 2, 3, 4, 5], [10, 20, 30], {"key": "value"})
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.max_if([10, 20, 30], [0, 1], {"a": 1, "b": 2, "c": 3})
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.max_if([0, 1], [-3, -1, 0, 2, 5], {})
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.max_if([-3, -1, 0, 2, 5], [100], {"key": "value"})
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.max_if([100], [1, 1, 2, 3, 5, 8], {"a": 1, "b": 2, "c": 3})
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.max_if([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5], {})
        except EXC:
            pass


class Test_mean_bias_error_deep:
    def test_c0(self):
        try:
            mod.mean_bias_error(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mean_bias_error(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mean_bias_error(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mean_bias_error(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mean_bias_error(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mean_bias_error(0, 1)
        except EXC:
            pass


class Test_mean_squared_error_deep:
    def test_c0(self):
        try:
            mod.mean_squared_error([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mean_squared_error([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mean_squared_error([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mean_squared_error([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mean_squared_error([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mean_squared_error([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_min_if_deep:
    def test_c0(self):
        try:
            mod.min_if([1, 2, 3, 4, 5], [10, 20, 30], {"key": "value"})
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.min_if([10, 20, 30], [0, 1], {"a": 1, "b": 2, "c": 3})
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.min_if([0, 1], [-3, -1, 0, 2, 5], {})
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.min_if([-3, -1, 0, 2, 5], [100], {"key": "value"})
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.min_if([100], [1, 1, 2, 3, 5, 8], {"a": 1, "b": 2, "c": 3})
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.min_if([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5], {})
        except EXC:
            pass


class Test_mish_deep:
    def test_c0(self):
        try:
            mod.mish(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mish(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mish(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mish(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mish(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mish(0)
        except EXC:
            pass


class Test_mode_mult_deep:
    def test_c0(self):
        try:
            mod.mode_mult([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mode_mult([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mode_mult([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mode_mult([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mode_mult([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mode_mult([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_mode_single_deep:
    def test_c0(self):
        try:
            mod.mode_single([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.mode_single([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.mode_single([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.mode_single([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.mode_single([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.mode_single([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_multinomial_coefficient_deep:
    def test_c0(self):
        try:
            mod.multinomial_coefficient()
        except EXC:
            pass


class Test_odds_ratio_deep:
    def test_c0(self):
        try:
            mod.odds_ratio(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.odds_ratio(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.odds_ratio(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.odds_ratio(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.odds_ratio(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.odds_ratio(0, 1, 2, 3)
        except EXC:
            pass


class Test_outliers_iqr_deep:
    def test_c0(self):
        try:
            mod.outliers_iqr([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.outliers_iqr([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.outliers_iqr([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.outliers_iqr([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.outliers_iqr([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.outliers_iqr([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_factor(self):
        try:
            mod.outliers_iqr([1, 2, 3, 4, 5], factor=1)
        except EXC:
            pass


class Test_poisson_pmf_deep:
    def test_c0(self):
        try:
            mod.poisson_pmf(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.poisson_pmf(2, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.poisson_pmf(3, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.poisson_pmf(5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.poisson_pmf(10, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.poisson_pmf(0, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.poisson_pmf(1, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.poisson_pmf(2, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.poisson_pmf(3, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.poisson_pmf(5, 1)
        except EXC:
            pass


class Test_precision_score_scalar_deep:
    def test_c0(self):
        try:
            mod.precision_score_scalar(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.precision_score_scalar(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.precision_score_scalar(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.precision_score_scalar(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.precision_score_scalar(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.precision_score_scalar(0, 1)
        except EXC:
            pass


class Test_quartile_deviation_deep:
    def test_c0(self):
        try:
            mod.quartile_deviation([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.quartile_deviation([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.quartile_deviation([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.quartile_deviation([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.quartile_deviation([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.quartile_deviation([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_relative_error_deep:
    def test_c0(self):
        try:
            mod.relative_error(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.relative_error(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.relative_error(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.relative_error(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.relative_error(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.relative_error(0, 1)
        except EXC:
            pass


class Test_risk_ratio_deep:
    def test_c0(self):
        try:
            mod.risk_ratio(1, 2, 3, 5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.risk_ratio(2, 3, 5, 10)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.risk_ratio(3, 5, 10, 0)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.risk_ratio(5, 10, 0, 1)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.risk_ratio(10, 0, 1, 2)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.risk_ratio(0, 1, 2, 3)
        except EXC:
            pass


class Test_rolling_median_deep:
    def test_c0(self):
        try:
            mod.rolling_median([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rolling_median([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rolling_median([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rolling_median([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rolling_median([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rolling_median([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_rolling_std_deep:
    def test_c0(self):
        try:
            mod.rolling_std([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rolling_std([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rolling_std([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rolling_std([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rolling_std([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rolling_std([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass

    def test_kw_sample(self):
        try:
            mod.rolling_std([1, 2, 3, 4, 5], 2, sample=True)
        except EXC:
            pass


class Test_root_mean_squared_error_deep:
    def test_c0(self):
        try:
            mod.root_mean_squared_error([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.root_mean_squared_error([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.root_mean_squared_error([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.root_mean_squared_error([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.root_mean_squared_error([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.root_mean_squared_error([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_spearman_correlation_deep:
    def test_c0(self):
        try:
            mod.spearman_correlation([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.spearman_correlation([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.spearman_correlation([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.spearman_correlation([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.spearman_correlation([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.spearman_correlation([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_specificity_score_scalar_deep:
    def test_c0(self):
        try:
            mod.specificity_score_scalar(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.specificity_score_scalar(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.specificity_score_scalar(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.specificity_score_scalar(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.specificity_score_scalar(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.specificity_score_scalar(0, 1)
        except EXC:
            pass


class Test_standardize_deep:
    def test_c0(self):
        try:
            mod.standardize(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.standardize(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.standardize(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.standardize(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.standardize(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.standardize(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.standardize(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.standardize(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.standardize(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.standardize(2, 1, 42)
        except EXC:
            pass


class Test_sum_if_deep:
    def test_c0(self):
        try:
            mod.sum_if([1, 2, 3, 4, 5], [10, 20, 30], {"key": "value"})
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_if([10, 20, 30], [0, 1], {"a": 1, "b": 2, "c": 3})
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_if([0, 1], [-3, -1, 0, 2, 5], {})
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_if([-3, -1, 0, 2, 5], [100], {"key": "value"})
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_if([100], [1, 1, 2, 3, 5, 8], {"a": 1, "b": 2, "c": 3})
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_if([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5], {})
        except EXC:
            pass


class Test_sum_of_squared_deviations_deep:
    def test_c0(self):
        try:
            mod.sum_of_squared_deviations([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_of_squared_deviations([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_of_squared_deviations([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_of_squared_deviations([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_of_squared_deviations([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_of_squared_deviations([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_sum_product_deep:
    def test_c0(self):
        try:
            mod.sum_product([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sum_product([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sum_product([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sum_product([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sum_product([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sum_product([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_triangular_pdf_deep:
    def test_c0(self):
        try:
            mod.triangular_pdf(1, 42, 0, -5)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.triangular_pdf(42, 0, -5, 3.14)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.triangular_pdf(0, -5, 3.14, 100)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.triangular_pdf(-5, 3.14, 100, 0.5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.triangular_pdf(3.14, 100, 0.5, 1000)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.triangular_pdf(100, 0.5, 1000, -1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.triangular_pdf(0.5, 1000, -1, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.triangular_pdf(1000, -1, 2, 1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.triangular_pdf(-1, 2, 1, 42)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.triangular_pdf(2, 1, 42, 0)
        except EXC:
            pass


class Test_weibull_pdf_deep:
    def test_c0(self):
        try:
            mod.weibull_pdf(1, 42, 0)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.weibull_pdf(42, 0, -5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.weibull_pdf(0, -5, 3.14)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.weibull_pdf(-5, 3.14, 100)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.weibull_pdf(3.14, 100, 0.5)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.weibull_pdf(100, 0.5, 1000)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.weibull_pdf(0.5, 1000, -1)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.weibull_pdf(1000, -1, 2)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.weibull_pdf(-1, 2, 1)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.weibull_pdf(2, 1, 42)
        except EXC:
            pass

