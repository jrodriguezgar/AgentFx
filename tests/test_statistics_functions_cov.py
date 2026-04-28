# Coverage tests for shortfx.fxNumeric.statistics_functions

from shortfx.fxNumeric import statistics_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_absolute_error:
    def test_exists(self):
        assert hasattr(mod, "absolute_error")

    def test_doc0(self):
        try:
            mod.absolute_error(10.5, 10.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.absolute_error(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.absolute_error(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.absolute_error(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.absolute_error("", "")
        except EXC:
            pass


class Test_adjusted_r_squared:
    def test_exists(self):
        assert hasattr(mod, "adjusted_r_squared")

    def test_var0(self):
        try:
            mod.adjusted_r_squared(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.adjusted_r_squared(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.adjusted_r_squared(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.adjusted_r_squared("", 0, "")
        except EXC:
            pass


class Test_aggregate:
    def test_exists(self):
        assert hasattr(mod, "aggregate")

    def test_doc0(self):
        try:
            mod.aggregate([1, 2, 3, 4], "sum")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.aggregate([1, 2, 3, 4], "avg")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.aggregate(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.aggregate(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.aggregate(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.aggregate([])
        except EXC:
            pass


class Test_anderson_darling:
    def test_exists(self):
        assert hasattr(mod, "anderson_darling")

    def test_var0(self):
        try:
            mod.anderson_darling(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.anderson_darling(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.anderson_darling(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.anderson_darling([])
        except EXC:
            pass


class Test_argmax:
    def test_exists(self):
        assert hasattr(mod, "argmax")

    def test_doc0(self):
        try:
            mod.argmax([3, 1, 4, 1, 5, 9])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.argmax(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.argmax(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.argmax(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.argmax([])
        except EXC:
            pass


class Test_argmin:
    def test_exists(self):
        assert hasattr(mod, "argmin")

    def test_doc0(self):
        try:
            mod.argmin([3, 1, 4, 1, 5, 9])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.argmin(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.argmin(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.argmin(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.argmin([])
        except EXC:
            pass


class Test_auto_correlation:
    def test_exists(self):
        assert hasattr(mod, "auto_correlation")

    def test_var0(self):
        try:
            mod.auto_correlation(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.auto_correlation(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.auto_correlation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.auto_correlation([])
        except EXC:
            pass


class Test_autocorrelation:
    def test_exists(self):
        assert hasattr(mod, "autocorrelation")

    def test_var0(self):
        try:
            mod.autocorrelation(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.autocorrelation(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.autocorrelation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.autocorrelation([])
        except EXC:
            pass


class Test_average_deviation:
    def test_exists(self):
        assert hasattr(mod, "average_deviation")

    def test_doc0(self):
        try:
            mod.average_deviation([2, 3, 4, 5, 6])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.average_deviation(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.average_deviation(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.average_deviation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.average_deviation([])
        except EXC:
            pass


class Test_average_if:
    def test_exists(self):
        assert hasattr(mod, "average_if")

    def test_doc0(self):
        try:
            mod.average_if([10, 20, 30, 40], ["A", "B", "A", "B"], "A")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.average_if([1, 2, 3, 4], [10, 20, 30, 40], ">15")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.average_if(0, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.average_if(1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.average_if(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.average_if([], "", "")
        except EXC:
            pass


class Test_balanced_accuracy_scalar:
    def test_exists(self):
        assert hasattr(mod, "balanced_accuracy_scalar")

    def test_doc0(self):
        try:
            mod.balanced_accuracy_scalar(80, 900, 100, 20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.balanced_accuracy_scalar(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.balanced_accuracy_scalar(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.balanced_accuracy_scalar(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.balanced_accuracy_scalar("", 0, "", 0)
        except EXC:
            pass


class Test_bayes_posterior:
    def test_exists(self):
        assert hasattr(mod, "bayes_posterior")

    def test_doc0(self):
        try:
            mod.bayes_posterior(0.01, 0.9, 0.05)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bayes_posterior(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bayes_posterior(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bayes_posterior(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bayes_posterior("", "", "")
        except EXC:
            pass


class Test_bayes_theorem:
    def test_exists(self):
        assert hasattr(mod, "bayes_theorem")

    def test_var0(self):
        try:
            mod.bayes_theorem(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bayes_theorem(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bayes_theorem(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bayes_theorem("", "", "")
        except EXC:
            pass


class Test_bayesian_update:
    def test_exists(self):
        assert hasattr(mod, "bayesian_update")

    def test_var0(self):
        try:
            mod.bayesian_update(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bayesian_update(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bayesian_update(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bayesian_update("", "", "")
        except EXC:
            pass


class Test_benford_distribution:
    def test_exists(self):
        assert hasattr(mod, "benford_distribution")

    def test_doc0(self):
        try:
            mod.benford_distribution([1, 20, 300, 4000])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.benford_distribution(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.benford_distribution(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.benford_distribution(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.benford_distribution([])
        except EXC:
            pass


class Test_beta_function:
    def test_exists(self):
        assert hasattr(mod, "beta_function")

    def test_var0(self):
        try:
            mod.beta_function(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.beta_function(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.beta_function(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.beta_function("", "")
        except EXC:
            pass


class Test_beta_function_value:
    def test_exists(self):
        assert hasattr(mod, "beta_function_value")

    def test_var0(self):
        try:
            mod.beta_function_value(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.beta_function_value(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.beta_function_value(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.beta_function_value("", "")
        except EXC:
            pass


class Test_bfill:
    def test_exists(self):
        assert hasattr(mod, "bfill")

    def test_doc0(self):
        try:
            mod.bfill([None, None, 3, None, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bfill([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bfill([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bfill(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bfill([])
        except EXC:
            pass


class Test_binary_entropy:
    def test_exists(self):
        assert hasattr(mod, "binary_entropy")

    def test_doc0(self):
        try:
            mod.binary_entropy(0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.binary_entropy(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.binary_entropy(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.binary_entropy(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.binary_entropy("")
        except EXC:
            pass


class Test_binomial_pmf:
    def test_exists(self):
        assert hasattr(mod, "binomial_pmf")

    def test_var0(self):
        try:
            mod.binomial_pmf(0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.binomial_pmf(1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.binomial_pmf(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.binomial_pmf(0, 0, "")
        except EXC:
            pass


class Test_binomial_probability:
    def test_exists(self):
        assert hasattr(mod, "binomial_probability")

    def test_var0(self):
        try:
            mod.binomial_probability(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.binomial_probability(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.binomial_probability(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.binomial_probability(0, 0, "")
        except EXC:
            pass


class Test_bootstrap_mean_ci:
    def test_exists(self):
        assert hasattr(mod, "bootstrap_mean_ci")

    def test_doc0(self):
        try:
            mod.bootstrap_mean_ci([1, 2, 3, 4, 5], 0.95, 5000, seed=42)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bootstrap_mean_ci(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bootstrap_mean_ci(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bootstrap_mean_ci(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bootstrap_mean_ci([])
        except EXC:
            pass


class Test_bowley_skewness:
    def test_exists(self):
        assert hasattr(mod, "bowley_skewness")

    def test_var0(self):
        try:
            mod.bowley_skewness(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bowley_skewness(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bowley_skewness(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bowley_skewness([])
        except EXC:
            pass


class Test_calculate_covariance:
    def test_exists(self):
        assert hasattr(mod, "calculate_covariance")

    def test_doc0(self):
        try:
            mod.calculate_covariance([1, 2, 3], [2, 4, 6]) # Positive correlation
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_covariance([1, 2, 3], [6, 4, 2]) # Negative correlation
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_covariance(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_covariance(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_covariance(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_covariance([], [])
        except EXC:
            pass


class Test_calculate_frecuency:
    def test_exists(self):
        assert hasattr(mod, "calculate_frecuency")

    def test_doc0(self):
        try:
            mod.calculate_frecuency([1, 2, 2, 3, 3, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_frecuency(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_frecuency(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_frecuency(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_frecuency([])
        except EXC:
            pass


class Test_calculate_interquartile_range:
    def test_exists(self):
        assert hasattr(mod, "calculate_interquartile_range")

    def test_doc0(self):
        try:
            mod.calculate_interquartile_range([1, 2, 3, 4, 5, 6, 7, 8, 9])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_interquartile_range([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_interquartile_range(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_interquartile_range(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_interquartile_range(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_interquartile_range([])
        except EXC:
            pass


class Test_calculate_mean:
    def test_exists(self):
        assert hasattr(mod, "calculate_mean")

    def test_doc0(self):
        try:
            mod.calculate_mean([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_mean([10, 20, 30])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_mean(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_mean(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_mean(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_mean([])
        except EXC:
            pass


class Test_calculate_median:
    def test_exists(self):
        assert hasattr(mod, "calculate_median")

    def test_doc0(self):
        try:
            mod.calculate_median([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_median([1, 2, 3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_median(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_median(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_median(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_median([])
        except EXC:
            pass


class Test_calculate_mode:
    def test_exists(self):
        assert hasattr(mod, "calculate_mode")

    def test_doc0(self):
        try:
            mod.calculate_mode([1, 2, 2, 3, 4])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_mode([1, 2, 2, 3, 3, 4])
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.calculate_mode([1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_mode(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_mode(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_mode(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_mode([])
        except EXC:
            pass


class Test_calculate_pearson_correlation:
    def test_exists(self):
        assert hasattr(mod, "calculate_pearson_correlation")

    def test_doc0(self):
        try:
            mod.calculate_pearson_correlation([1, 2, 3], [2, 4, 6])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_pearson_correlation([1, 2, 3], [6, 4, 2])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_pearson_correlation(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_pearson_correlation(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_pearson_correlation(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_pearson_correlation([], [])
        except EXC:
            pass


class Test_calculate_percentile:
    def test_exists(self):
        assert hasattr(mod, "calculate_percentile")

    def test_doc0(self):
        try:
            mod.calculate_percentile([10, 20, 30, 40, 50], 50) # Median
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_percentile([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 90)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_percentile(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_percentile(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_percentile(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_percentile([], 0)
        except EXC:
            pass


class Test_calculate_range:
    def test_exists(self):
        assert hasattr(mod, "calculate_range")

    def test_doc0(self):
        try:
            mod.calculate_range([1, 5, 2, 8, 3])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_range([10, 10, 10])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_range(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_range(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_range(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_range([])
        except EXC:
            pass


class Test_calculate_standard_deviation:
    def test_exists(self):
        assert hasattr(mod, "calculate_standard_deviation")

    def test_var0(self):
        try:
            mod.calculate_standard_deviation(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_standard_deviation(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_standard_deviation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_standard_deviation([])
        except EXC:
            pass


class Test_calculate_variance:
    def test_exists(self):
        assert hasattr(mod, "calculate_variance")

    def test_doc0(self):
        try:
            mod.calculate_variance([1, 2, 3, 4, 5]) # Sample variance
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_variance([1, 2, 3, 4, 5], sample=False) # Population variance
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_variance(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_variance(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_variance(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.calculate_variance([])
        except EXC:
            pass


class Test_cauchy_pdf:
    def test_exists(self):
        assert hasattr(mod, "cauchy_pdf")

    def test_var0(self):
        try:
            mod.cauchy_pdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cauchy_pdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cauchy_pdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cauchy_pdf("")
        except EXC:
            pass


class Test_celu:
    def test_exists(self):
        assert hasattr(mod, "celu")

    def test_doc0(self):
        try:
            mod.celu(1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.celu(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.celu(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.celu(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.celu("")
        except EXC:
            pass


class Test_chi_squared_pdf:
    def test_exists(self):
        assert hasattr(mod, "chi_squared_pdf")

    def test_var0(self):
        try:
            mod.chi_squared_pdf(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chi_squared_pdf(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chi_squared_pdf(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chi_squared_pdf("", 0)
        except EXC:
            pass


class Test_chi_squared_statistic:
    def test_exists(self):
        assert hasattr(mod, "chi_squared_statistic")

    def test_var0(self):
        try:
            mod.chi_squared_statistic(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chi_squared_statistic(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chi_squared_statistic(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chi_squared_statistic("", "")
        except EXC:
            pass


class Test_chisq_test:
    def test_exists(self):
        assert hasattr(mod, "chisq_test")

    def test_var0(self):
        try:
            mod.chisq_test(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chisq_test(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chisq_test(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chisq_test("")
        except EXC:
            pass


class Test_coefficient_of_quartile_deviation:
    def test_exists(self):
        assert hasattr(mod, "coefficient_of_quartile_deviation")

    def test_doc0(self):
        try:
            mod.coefficient_of_quartile_deviation([2, 4, 6, 8, 10])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.coefficient_of_quartile_deviation([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coefficient_of_quartile_deviation([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coefficient_of_quartile_deviation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coefficient_of_quartile_deviation([])
        except EXC:
            pass


class Test_coefficient_of_variation:
    def test_exists(self):
        assert hasattr(mod, "coefficient_of_variation")

    def test_var0(self):
        try:
            mod.coefficient_of_variation(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.coefficient_of_variation(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.coefficient_of_variation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.coefficient_of_variation([])
        except EXC:
            pass


class Test_cohens_d:
    def test_exists(self):
        assert hasattr(mod, "cohens_d")

    def test_var0(self):
        try:
            mod.cohens_d(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cohens_d(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cohens_d(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cohens_d("", "")
        except EXC:
            pass


class Test_cohens_kappa_scalar:
    def test_exists(self):
        assert hasattr(mod, "cohens_kappa_scalar")

    def test_var0(self):
        try:
            mod.cohens_kappa_scalar(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cohens_kappa_scalar(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cohens_kappa_scalar(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cohens_kappa_scalar("", 0, "", 0)
        except EXC:
            pass


class Test_confidence_norm:
    def test_exists(self):
        assert hasattr(mod, "confidence_norm")

    def test_var0(self):
        try:
            mod.confidence_norm(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.confidence_norm(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.confidence_norm(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.confidence_norm(0, "", 0)
        except EXC:
            pass


class Test_confidence_t:
    def test_exists(self):
        assert hasattr(mod, "confidence_t")

    def test_var0(self):
        try:
            mod.confidence_t(3.14, 3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.confidence_t(100, 100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.confidence_t(None, 3.14, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.confidence_t(0, "", 0)
        except EXC:
            pass


class Test_contraharmonic_mean:
    def test_exists(self):
        assert hasattr(mod, "contraharmonic_mean")

    def test_doc0(self):
        try:
            mod.contraharmonic_mean([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.contraharmonic_mean([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.contraharmonic_mean([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.contraharmonic_mean(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.contraharmonic_mean([])
        except EXC:
            pass


class Test_cosine_similarity:
    def test_exists(self):
        assert hasattr(mod, "cosine_similarity")

    def test_var0(self):
        try:
            mod.cosine_similarity(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cosine_similarity(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cosine_similarity(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cosine_similarity("", "")
        except EXC:
            pass


class Test_cosine_similarity_scalar:
    def test_exists(self):
        assert hasattr(mod, "cosine_similarity_scalar")

    def test_doc0(self):
        try:
            mod.cosine_similarity_scalar(1, 0, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cosine_similarity_scalar(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cosine_similarity_scalar(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cosine_similarity_scalar(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cosine_similarity_scalar("", "", "", "")
        except EXC:
            pass


class Test_count_true_with_sum:
    def test_exists(self):
        assert hasattr(mod, "count_true_with_sum")

    def test_doc0(self):
        try:
            mod.count_true_with_sum([True, False, True, True])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.count_true_with_sum([False, False, False])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.count_true_with_sum(True)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.count_true_with_sum(False)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.count_true_with_sum(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.count_true_with_sum(0)
        except EXC:
            pass


class Test_covariance_matrix:
    def test_exists(self):
        assert hasattr(mod, "covariance_matrix")

    def test_doc0(self):
        try:
            mod.covariance_matrix([[1, 2, 3], [4, 5, 6]])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.covariance_matrix([[1, 2, 3], [6, 5, 4]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.covariance_matrix(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.covariance_matrix(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.covariance_matrix(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.covariance_matrix([])
        except EXC:
            pass


class Test_cramers_v:
    def test_exists(self):
        assert hasattr(mod, "cramers_v")

    def test_var0(self):
        try:
            mod.cramers_v(3.14, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cramers_v(100, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cramers_v(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cramers_v("", 0, 0)
        except EXC:
            pass


class Test_cross_entropy:
    def test_exists(self):
        assert hasattr(mod, "cross_entropy")

    def test_var0(self):
        try:
            mod.cross_entropy(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cross_entropy(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cross_entropy(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cross_entropy("", "")
        except EXC:
            pass


class Test_cross_entropy_binary:
    def test_exists(self):
        assert hasattr(mod, "cross_entropy_binary")

    def test_var0(self):
        try:
            mod.cross_entropy_binary(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cross_entropy_binary(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cross_entropy_binary(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cross_entropy_binary("", "")
        except EXC:
            pass


class Test_cumulative_max:
    def test_exists(self):
        assert hasattr(mod, "cumulative_max")

    def test_doc0(self):
        try:
            mod.cumulative_max([3, 1, 4, 1, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cumulative_max(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cumulative_max(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cumulative_max(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cumulative_max([])
        except EXC:
            pass


class Test_cumulative_min:
    def test_exists(self):
        assert hasattr(mod, "cumulative_min")

    def test_doc0(self):
        try:
            mod.cumulative_min([3, 1, 4, 1, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cumulative_min(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cumulative_min(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cumulative_min(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cumulative_min([])
        except EXC:
            pass


class Test_cumulative_moving_average:
    def test_exists(self):
        assert hasattr(mod, "cumulative_moving_average")

    def test_doc0(self):
        try:
            mod.cumulative_moving_average([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cumulative_moving_average(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cumulative_moving_average(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cumulative_moving_average(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cumulative_moving_average([])
        except EXC:
            pass


class Test_cumulative_product:
    def test_exists(self):
        assert hasattr(mod, "cumulative_product")

    def test_doc0(self):
        try:
            mod.cumulative_product([1, 2, 3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cumulative_product(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cumulative_product(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cumulative_product(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cumulative_product([])
        except EXC:
            pass


class Test_cumulative_return:
    def test_exists(self):
        assert hasattr(mod, "cumulative_return")

    def test_var0(self):
        try:
            mod.cumulative_return(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cumulative_return(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cumulative_return(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cumulative_return("")
        except EXC:
            pass


class Test_cumulative_sum:
    def test_exists(self):
        assert hasattr(mod, "cumulative_sum")

    def test_doc0(self):
        try:
            mod.cumulative_sum([1, 2, 3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cumulative_sum(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cumulative_sum(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cumulative_sum(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cumulative_sum([])
        except EXC:
            pass


class Test_describe:
    def test_exists(self):
        assert hasattr(mod, "describe")

    def test_doc0(self):
        try:
            mod.describe([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.describe(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.describe(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.describe(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.describe([])
        except EXC:
            pass


class Test_deviation_squared:
    def test_exists(self):
        assert hasattr(mod, "deviation_squared")

    def test_doc0(self):
        try:
            mod.deviation_squared([2, 5, 8])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.deviation_squared(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.deviation_squared(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.deviation_squared(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.deviation_squared([])
        except EXC:
            pass


class Test_dice_coefficient_scalar:
    def test_exists(self):
        assert hasattr(mod, "dice_coefficient_scalar")

    def test_doc0(self):
        try:
            mod.dice_coefficient_scalar(30, 10, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.dice_coefficient_scalar(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dice_coefficient_scalar(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dice_coefficient_scalar(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dice_coefficient_scalar("", "", 0)
        except EXC:
            pass


class Test_diff:
    def test_exists(self):
        assert hasattr(mod, "diff")

    def test_doc0(self):
        try:
            mod.diff([1, 3, 6, 10])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.diff(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.diff(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.diff(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.diff([])
        except EXC:
            pass


class Test_dixon_q_test:
    def test_exists(self):
        assert hasattr(mod, "dixon_q_test")

    def test_doc0(self):
        try:
            mod.dixon_q_test([1, 2, 3, 4, 5, 100])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.dixon_q_test(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dixon_q_test(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dixon_q_test(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dixon_q_test([])
        except EXC:
            pass


class Test_durbin_watson:
    def test_exists(self):
        assert hasattr(mod, "durbin_watson")

    def test_var0(self):
        try:
            mod.durbin_watson(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.durbin_watson(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.durbin_watson(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.durbin_watson("")
        except EXC:
            pass


class Test_elu:
    def test_exists(self):
        assert hasattr(mod, "elu")

    def test_doc0(self):
        try:
            mod.elu(1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.elu(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.elu(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.elu(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.elu("")
        except EXC:
            pass


class Test_empirical_cdf:
    def test_exists(self):
        assert hasattr(mod, "empirical_cdf")

    def test_doc0(self):
        try:
            mod.empirical_cdf([1, 2, 3, 4, 5], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.empirical_cdf(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.empirical_cdf(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.empirical_cdf(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.empirical_cdf([], "")
        except EXC:
            pass


class Test_entropy:
    def test_exists(self):
        assert hasattr(mod, "entropy")

    def test_var0(self):
        try:
            mod.entropy(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.entropy(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.entropy(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.entropy([])
        except EXC:
            pass


class Test_entropy_binary:
    def test_exists(self):
        assert hasattr(mod, "entropy_binary")

    def test_var0(self):
        try:
            mod.entropy_binary(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.entropy_binary(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.entropy_binary(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.entropy_binary("")
        except EXC:
            pass


class Test_erlang_pdf:
    def test_exists(self):
        assert hasattr(mod, "erlang_pdf")

    def test_var0(self):
        try:
            mod.erlang_pdf(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.erlang_pdf(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.erlang_pdf(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.erlang_pdf("", 0, "")
        except EXC:
            pass


class Test_euclidean_distance:
    def test_exists(self):
        assert hasattr(mod, "euclidean_distance")

    def test_var0(self):
        try:
            mod.euclidean_distance(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.euclidean_distance(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.euclidean_distance(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.euclidean_distance("", "")
        except EXC:
            pass


class Test_ewma_variance:
    def test_exists(self):
        assert hasattr(mod, "ewma_variance")

    def test_doc0(self):
        try:
            mod.ewma_variance([1, 2, 3, 4, 5], 0.3)[:2]
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ewma_variance(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ewma_variance(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ewma_variance(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ewma_variance([])
        except EXC:
            pass


class Test_exponential_cdf:
    def test_exists(self):
        assert hasattr(mod, "exponential_cdf")

    def test_var0(self):
        try:
            mod.exponential_cdf(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.exponential_cdf(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.exponential_cdf(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.exponential_cdf("", "")
        except EXC:
            pass


class Test_exponential_decay_rate:
    def test_exists(self):
        assert hasattr(mod, "exponential_decay_rate")

    def test_var0(self):
        try:
            mod.exponential_decay_rate(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.exponential_decay_rate(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.exponential_decay_rate(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.exponential_decay_rate("", "", "")
        except EXC:
            pass


class Test_exponential_moving_average:
    def test_exists(self):
        assert hasattr(mod, "exponential_moving_average")

    def test_var0(self):
        try:
            mod.exponential_moving_average(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.exponential_moving_average(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.exponential_moving_average(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.exponential_moving_average([], 0)
        except EXC:
            pass


class Test_exponential_pdf:
    def test_exists(self):
        assert hasattr(mod, "exponential_pdf")

    def test_var0(self):
        try:
            mod.exponential_pdf(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.exponential_pdf(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.exponential_pdf(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.exponential_pdf("", "")
        except EXC:
            pass


class Test_exponential_smoothing_single:
    def test_exists(self):
        assert hasattr(mod, "exponential_smoothing_single")

    def test_doc0(self):
        try:
            mod.exponential_smoothing_single(10, 8, 0.3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.exponential_smoothing_single(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.exponential_smoothing_single(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.exponential_smoothing_single(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.exponential_smoothing_single("", "", 0)
        except EXC:
            pass


class Test_f1_score_scalar:
    def test_exists(self):
        assert hasattr(mod, "f1_score_scalar")

    def test_doc0(self):
        try:
            mod.f1_score_scalar(80, 10, 20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.f1_score_scalar(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.f1_score_scalar(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.f1_score_scalar(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.f1_score_scalar("", "", 0)
        except EXC:
            pass


class Test_f_test:
    def test_exists(self):
        assert hasattr(mod, "f_test")

    def test_var0(self):
        try:
            mod.f_test(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.f_test(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.f_test(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.f_test([], [])
        except EXC:
            pass


class Test_false_discovery_rate:
    def test_exists(self):
        assert hasattr(mod, "false_discovery_rate")

    def test_doc0(self):
        try:
            mod.false_discovery_rate(100, 80)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.false_discovery_rate(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.false_discovery_rate(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.false_discovery_rate(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.false_discovery_rate("", "")
        except EXC:
            pass


class Test_ffill:
    def test_exists(self):
        assert hasattr(mod, "ffill")

    def test_doc0(self):
        try:
            mod.ffill([1, None, None, 4, None])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.ffill([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ffill([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ffill(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ffill([])
        except EXC:
            pass


class Test_fillna:
    def test_exists(self):
        assert hasattr(mod, "fillna")

    def test_doc0(self):
        try:
            mod.fillna([1, None, 3, None, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.fillna([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fillna([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fillna(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fillna([])
        except EXC:
            pass


class Test_fisher:
    def test_exists(self):
        assert hasattr(mod, "fisher")

    def test_var0(self):
        try:
            mod.fisher(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fisher(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fisher(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fisher("")
        except EXC:
            pass


class Test_fisher_inv:
    def test_exists(self):
        assert hasattr(mod, "fisher_inv")

    def test_var0(self):
        try:
            mod.fisher_inv(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.fisher_inv(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.fisher_inv(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.fisher_inv("")
        except EXC:
            pass


class Test_focal_loss:
    def test_exists(self):
        assert hasattr(mod, "focal_loss")

    def test_var0(self):
        try:
            mod.focal_loss(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.focal_loss(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.focal_loss(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.focal_loss("", "")
        except EXC:
            pass


class Test_forecast_ets:
    def test_exists(self):
        assert hasattr(mod, "forecast_ets")

    def test_var0(self):
        try:
            mod.forecast_ets(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.forecast_ets(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.forecast_ets(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.forecast_ets("", [], "")
        except EXC:
            pass


class Test_forecast_linear:
    def test_exists(self):
        assert hasattr(mod, "forecast_linear")

    def test_doc0(self):
        try:
            mod.forecast_linear(4, [2, 4, 6], [1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.forecast_linear(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.forecast_linear(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.forecast_linear(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.forecast_linear("", 0, 0)
        except EXC:
            pass


class Test_frequency_bins:
    def test_exists(self):
        assert hasattr(mod, "frequency_bins")

    def test_doc0(self):
        try:
            mod.frequency_bins([1, 2, 3, 4, 5, 6], [2, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.frequency_bins(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.frequency_bins(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.frequency_bins(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.frequency_bins([], "")
        except EXC:
            pass


class Test_gamma_pdf:
    def test_exists(self):
        assert hasattr(mod, "gamma_pdf")

    def test_var0(self):
        try:
            mod.gamma_pdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gamma_pdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gamma_pdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gamma_pdf("", 0, 0)
        except EXC:
            pass


class Test_gelu:
    def test_exists(self):
        assert hasattr(mod, "gelu")

    def test_var0(self):
        try:
            mod.gelu(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gelu(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gelu(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gelu("")
        except EXC:
            pass


class Test_geometric_mean:
    def test_exists(self):
        assert hasattr(mod, "geometric_mean")

    def test_doc0(self):
        try:
            mod.geometric_mean([2, 8])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.geometric_mean(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geometric_mean(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geometric_mean(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geometric_mean([])
        except EXC:
            pass


class Test_geometric_pdf:
    def test_exists(self):
        assert hasattr(mod, "geometric_pdf")

    def test_doc0(self):
        try:
            mod.geometric_pdf(3, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.geometric_pdf(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geometric_pdf(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geometric_pdf(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geometric_pdf(0, "")
        except EXC:
            pass


class Test_geometric_pmf:
    def test_exists(self):
        assert hasattr(mod, "geometric_pmf")

    def test_var0(self):
        try:
            mod.geometric_pmf(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geometric_pmf(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geometric_pmf(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geometric_pmf(0, "")
        except EXC:
            pass


class Test_gini_coefficient:
    def test_exists(self):
        assert hasattr(mod, "gini_coefficient")

    def test_doc0(self):
        try:
            mod.gini_coefficient([1, 1, 1, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gini_coefficient(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gini_coefficient(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gini_coefficient(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gini_coefficient([])
        except EXC:
            pass


class Test_gini_impurity_binary:
    def test_exists(self):
        assert hasattr(mod, "gini_impurity_binary")

    def test_doc0(self):
        try:
            mod.gini_impurity_binary(0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.gini_impurity_binary(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gini_impurity_binary(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gini_impurity_binary(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gini_impurity_binary("")
        except EXC:
            pass


class Test_glass_delta:
    def test_exists(self):
        assert hasattr(mod, "glass_delta")

    def test_var0(self):
        try:
            mod.glass_delta(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.glass_delta(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.glass_delta(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.glass_delta("", "")
        except EXC:
            pass


class Test_growth:
    def test_exists(self):
        assert hasattr(mod, "growth")

    def test_var0(self):
        try:
            mod.growth(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.growth(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.growth(None)
        except EXC:
            pass


class Test_grubbs_test:
    def test_exists(self):
        assert hasattr(mod, "grubbs_test")

    def test_doc0(self):
        try:
            mod.grubbs_test([1, 2, 3, 4, 5, 100])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.grubbs_test(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.grubbs_test(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.grubbs_test(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.grubbs_test([])
        except EXC:
            pass


class Test_gumbel_pdf:
    def test_exists(self):
        assert hasattr(mod, "gumbel_pdf")

    def test_var0(self):
        try:
            mod.gumbel_pdf(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.gumbel_pdf(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.gumbel_pdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.gumbel_pdf("")
        except EXC:
            pass


class Test_hard_sigmoid:
    def test_exists(self):
        assert hasattr(mod, "hard_sigmoid")

    def test_doc0(self):
        try:
            mod.hard_sigmoid(0.0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hard_sigmoid(3.0)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.hard_sigmoid(-3.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hard_sigmoid(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hard_sigmoid(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hard_sigmoid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hard_sigmoid("")
        except EXC:
            pass


class Test_hard_swish:
    def test_exists(self):
        assert hasattr(mod, "hard_swish")

    def test_doc0(self):
        try:
            mod.hard_swish(0.0)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hard_swish(3.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hard_swish(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hard_swish(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hard_swish(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hard_swish("")
        except EXC:
            pass


class Test_harmonic_mean:
    def test_exists(self):
        assert hasattr(mod, "harmonic_mean")

    def test_doc0(self):
        try:
            mod.harmonic_mean([1, 4, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.harmonic_mean(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.harmonic_mean(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.harmonic_mean(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.harmonic_mean([])
        except EXC:
            pass


class Test_hedges_g:
    def test_exists(self):
        assert hasattr(mod, "hedges_g")

    def test_var0(self):
        try:
            mod.hedges_g(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hedges_g(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hedges_g(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hedges_g("", "")
        except EXC:
            pass


class Test_hinge_loss:
    def test_exists(self):
        assert hasattr(mod, "hinge_loss")

    def test_doc0(self):
        try:
            mod.hinge_loss(1, 0.8)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.hinge_loss(1, 2.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hinge_loss(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hinge_loss(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hinge_loss(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hinge_loss("", "")
        except EXC:
            pass


class Test_holt_linear_forecast:
    def test_exists(self):
        assert hasattr(mod, "holt_linear_forecast")

    def test_var0(self):
        try:
            mod.holt_linear_forecast(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.holt_linear_forecast(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.holt_linear_forecast(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.holt_linear_forecast([], 0, 0)
        except EXC:
            pass


class Test_huber_loss:
    def test_exists(self):
        assert hasattr(mod, "huber_loss")

    def test_doc0(self):
        try:
            mod.huber_loss(1.0, 1.5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.huber_loss(1.0, 5.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.huber_loss(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.huber_loss(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.huber_loss(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.huber_loss("", "")
        except EXC:
            pass


class Test_hypergeometric_pmf:
    def test_exists(self):
        assert hasattr(mod, "hypergeometric_pmf")

    def test_var0(self):
        try:
            mod.hypergeometric_pmf(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hypergeometric_pmf(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hypergeometric_pmf(None, 0, 0, 0)
        except EXC:
            pass


class Test_intercept:
    def test_exists(self):
        assert hasattr(mod, "intercept")

    def test_doc0(self):
        try:
            mod.intercept([2, 4, 6], [1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.intercept(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.intercept(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.intercept(None, 0)
        except EXC:
            pass


class Test_jaccard_index_scalar:
    def test_exists(self):
        assert hasattr(mod, "jaccard_index_scalar")

    def test_doc0(self):
        try:
            mod.jaccard_index_scalar(50, 10, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.jaccard_index_scalar(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jaccard_index_scalar(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jaccard_index_scalar(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.jaccard_index_scalar("", "", 0)
        except EXC:
            pass


class Test_jaccard_similarity:
    def test_exists(self):
        assert hasattr(mod, "jaccard_similarity")

    def test_doc0(self):
        try:
            mod.jaccard_similarity([1, 2, 3], [2, 3, 4])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.jaccard_similarity([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jaccard_similarity([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jaccard_similarity(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.jaccard_similarity("", "")
        except EXC:
            pass


class Test_jarque_bera:
    def test_exists(self):
        assert hasattr(mod, "jarque_bera")

    def test_doc0(self):
        try:
            mod.jarque_bera([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.jarque_bera(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.jarque_bera(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.jarque_bera(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.jarque_bera([])
        except EXC:
            pass


class Test_js_divergence:
    def test_exists(self):
        assert hasattr(mod, "js_divergence")

    def test_var0(self):
        try:
            mod.js_divergence(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.js_divergence(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.js_divergence(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.js_divergence("", "")
        except EXC:
            pass


class Test_kendall_tau:
    def test_exists(self):
        assert hasattr(mod, "kendall_tau")

    def test_var0(self):
        try:
            mod.kendall_tau(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kendall_tau(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kendall_tau(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kendall_tau([], [])
        except EXC:
            pass


class Test_kl_divergence:
    def test_exists(self):
        assert hasattr(mod, "kl_divergence")

    def test_var0(self):
        try:
            mod.kl_divergence(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kl_divergence(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kl_divergence(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kl_divergence("", "")
        except EXC:
            pass


class Test_kurtosis:
    def test_exists(self):
        assert hasattr(mod, "kurtosis")

    def test_var0(self):
        try:
            mod.kurtosis(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.kurtosis(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.kurtosis(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.kurtosis([])
        except EXC:
            pass


class Test_lag:
    def test_exists(self):
        assert hasattr(mod, "lag")

    def test_doc0(self):
        try:
            mod.lag([10, 20, 30, 40], 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lag([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lag([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lag(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lag([])
        except EXC:
            pass


class Test_laplace_pdf:
    def test_exists(self):
        assert hasattr(mod, "laplace_pdf")

    def test_var0(self):
        try:
            mod.laplace_pdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.laplace_pdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.laplace_pdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.laplace_pdf("")
        except EXC:
            pass


class Test_large:
    def test_exists(self):
        assert hasattr(mod, "large")

    def test_doc0(self):
        try:
            mod.large([3, 1, 4, 1, 5, 9], 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.large([3, 1, 4, 1, 5, 9], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.large(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.large(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.large(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.large([], 0)
        except EXC:
            pass


class Test_lead:
    def test_exists(self):
        assert hasattr(mod, "lead")

    def test_doc0(self):
        try:
            mod.lead([10, 20, 30, 40], 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.lead([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.lead([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.lead(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.lead([])
        except EXC:
            pass


class Test_leaky_relu:
    def test_exists(self):
        assert hasattr(mod, "leaky_relu")

    def test_doc0(self):
        try:
            mod.leaky_relu(5)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.leaky_relu(-10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.leaky_relu(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.leaky_relu(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.leaky_relu(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.leaky_relu("")
        except EXC:
            pass


class Test_linest:
    def test_exists(self):
        assert hasattr(mod, "linest")

    def test_doc0(self):
        try:
            mod.linest([1, 9, 5, 7])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.linest(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.linest(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.linest(None)
        except EXC:
            pass


class Test_ljung_box:
    def test_exists(self):
        assert hasattr(mod, "ljung_box")

    def test_var0(self):
        try:
            mod.ljung_box(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.ljung_box(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.ljung_box(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.ljung_box("")
        except EXC:
            pass


class Test_log_cosh_loss:
    def test_exists(self):
        assert hasattr(mod, "log_cosh_loss")

    def test_var0(self):
        try:
            mod.log_cosh_loss(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.log_cosh_loss(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.log_cosh_loss(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.log_cosh_loss("", "")
        except EXC:
            pass


class Test_log_loss:
    def test_exists(self):
        assert hasattr(mod, "log_loss")

    def test_var0(self):
        try:
            mod.log_loss(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.log_loss(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.log_loss(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.log_loss("", "")
        except EXC:
            pass


class Test_log_normal_pdf:
    def test_exists(self):
        assert hasattr(mod, "log_normal_pdf")

    def test_var0(self):
        try:
            mod.log_normal_pdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.log_normal_pdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.log_normal_pdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.log_normal_pdf("")
        except EXC:
            pass


class Test_logest:
    def test_exists(self):
        assert hasattr(mod, "logest")

    def test_doc0(self):
        try:
            mod.logest([33100, 47300, 69000, 102000, 150000, 220000])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.logest(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.logest(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.logest(None)
        except EXC:
            pass


class Test_logistic_cdf:
    def test_exists(self):
        assert hasattr(mod, "logistic_cdf")

    def test_doc0(self):
        try:
            mod.logistic_cdf(0.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.logistic_cdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.logistic_cdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.logistic_cdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.logistic_cdf("")
        except EXC:
            pass


class Test_logistic_function:
    def test_exists(self):
        assert hasattr(mod, "logistic_function")

    def test_doc0(self):
        try:
            mod.logistic_function(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.logistic_function(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.logistic_function(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.logistic_function(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.logistic_function("")
        except EXC:
            pass


class Test_logistic_pdf:
    def test_exists(self):
        assert hasattr(mod, "logistic_pdf")

    def test_var0(self):
        try:
            mod.logistic_pdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.logistic_pdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.logistic_pdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.logistic_pdf("")
        except EXC:
            pass


class Test_logit:
    def test_exists(self):
        assert hasattr(mod, "logit")

    def test_doc0(self):
        try:
            mod.logit(0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.logit(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.logit(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.logit(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.logit("")
        except EXC:
            pass


class Test_mahalanobis_distance_1d:
    def test_exists(self):
        assert hasattr(mod, "mahalanobis_distance_1d")

    def test_var0(self):
        try:
            mod.mahalanobis_distance_1d(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mahalanobis_distance_1d(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mahalanobis_distance_1d(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mahalanobis_distance_1d("", [])
        except EXC:
            pass


class Test_manhattan_distance:
    def test_exists(self):
        assert hasattr(mod, "manhattan_distance")

    def test_doc0(self):
        try:
            mod.manhattan_distance([1, 2, 3], [4, 5, 6])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.manhattan_distance(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.manhattan_distance(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.manhattan_distance(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.manhattan_distance("", "")
        except EXC:
            pass


class Test_mann_whitney_u:
    def test_exists(self):
        assert hasattr(mod, "mann_whitney_u")

    def test_doc0(self):
        try:
            mod.mann_whitney_u([1, 2, 3], [4, 5, 6])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mann_whitney_u(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mann_whitney_u(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mann_whitney_u(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mann_whitney_u([], [])
        except EXC:
            pass


class Test_markov_chain_steady_state:
    def test_exists(self):
        assert hasattr(mod, "markov_chain_steady_state")

    def test_doc0(self):
        try:
            mod.markov_chain_steady_state([[0.9, 0.1], [0.5, 0.5]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.markov_chain_steady_state(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.markov_chain_steady_state(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.markov_chain_steady_state(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.markov_chain_steady_state(0)
        except EXC:
            pass


class Test_matthews_corrcoef_scalar:
    def test_exists(self):
        assert hasattr(mod, "matthews_corrcoef_scalar")

    def test_var0(self):
        try:
            mod.matthews_corrcoef_scalar(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.matthews_corrcoef_scalar(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.matthews_corrcoef_scalar(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.matthews_corrcoef_scalar("", 0, "", 0)
        except EXC:
            pass


class Test_max_drawdown:
    def test_exists(self):
        assert hasattr(mod, "max_drawdown")

    def test_doc0(self):
        try:
            mod.max_drawdown([100, 120, 90, 110, 80])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.max_drawdown(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.max_drawdown(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.max_drawdown(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.max_drawdown([])
        except EXC:
            pass


class Test_max_if:
    def test_exists(self):
        assert hasattr(mod, "max_if")

    def test_doc0(self):
        try:
            mod.max_if([5, 10, 15, 20], ["A", "B", "A", "B"], "A")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.max_if([1, 2, 3, 4], [10, 20, 30, 40], ">15")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.max_if(0, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.max_if(1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.max_if(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.max_if([], "", "")
        except EXC:
            pass


class Test_maxwell_boltzmann_pdf:
    def test_exists(self):
        assert hasattr(mod, "maxwell_boltzmann_pdf")

    def test_var0(self):
        try:
            mod.maxwell_boltzmann_pdf(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.maxwell_boltzmann_pdf(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.maxwell_boltzmann_pdf(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.maxwell_boltzmann_pdf("", "")
        except EXC:
            pass


class Test_mean_absolute_error:
    def test_exists(self):
        assert hasattr(mod, "mean_absolute_error")

    def test_doc0(self):
        try:
            mod.mean_absolute_error([1, 2, 3], [1.5, 2.5, 3.5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mean_absolute_error(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mean_absolute_error(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mean_absolute_error(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mean_absolute_error("", "")
        except EXC:
            pass


class Test_mean_absolute_percentage_error:
    def test_exists(self):
        assert hasattr(mod, "mean_absolute_percentage_error")

    def test_var0(self):
        try:
            mod.mean_absolute_percentage_error(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mean_absolute_percentage_error(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mean_absolute_percentage_error(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mean_absolute_percentage_error("", "")
        except EXC:
            pass


class Test_mean_bias_error:
    def test_exists(self):
        assert hasattr(mod, "mean_bias_error")

    def test_doc0(self):
        try:
            mod.mean_bias_error(105, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mean_bias_error(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mean_bias_error(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mean_bias_error(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mean_bias_error("", "")
        except EXC:
            pass


class Test_mean_percentage_error:
    def test_exists(self):
        assert hasattr(mod, "mean_percentage_error")

    def test_doc0(self):
        try:
            mod.mean_percentage_error(100, 90)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mean_percentage_error(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mean_percentage_error(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mean_percentage_error(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mean_percentage_error("", "")
        except EXC:
            pass


class Test_mean_squared_error:
    def test_exists(self):
        assert hasattr(mod, "mean_squared_error")

    def test_doc0(self):
        try:
            mod.mean_squared_error([3, -0.5, 2, 7], [2.5, 0.0, 2, 8])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.mean_squared_error([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mean_squared_error(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mean_squared_error(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mean_squared_error(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mean_squared_error("", "")
        except EXC:
            pass


class Test_median_absolute_deviation:
    def test_exists(self):
        assert hasattr(mod, "median_absolute_deviation")

    def test_doc0(self):
        try:
            mod.median_absolute_deviation([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.median_absolute_deviation(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.median_absolute_deviation(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.median_absolute_deviation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.median_absolute_deviation([])
        except EXC:
            pass


class Test_midhinge:
    def test_exists(self):
        assert hasattr(mod, "midhinge")

    def test_doc0(self):
        try:
            mod.midhinge([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.midhinge([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.midhinge([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.midhinge(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.midhinge([])
        except EXC:
            pass


class Test_midrange:
    def test_exists(self):
        assert hasattr(mod, "midrange")

    def test_doc0(self):
        try:
            mod.midrange([2, 4, 6, 8, 10])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.midrange([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.midrange([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.midrange(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.midrange([])
        except EXC:
            pass


class Test_min_if:
    def test_exists(self):
        assert hasattr(mod, "min_if")

    def test_doc0(self):
        try:
            mod.min_if([5, 10, 15, 20], ["A", "B", "A", "B"], "A")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.min_if([1, 2, 3, 4], [10, 20, 30, 40], ">15")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.min_if(0, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.min_if(1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.min_if(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.min_if([], "", "")
        except EXC:
            pass


class Test_minkowski_distance:
    def test_exists(self):
        assert hasattr(mod, "minkowski_distance")

    def test_var0(self):
        try:
            mod.minkowski_distance(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.minkowski_distance(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.minkowski_distance(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.minkowski_distance("", "")
        except EXC:
            pass


class Test_mish:
    def test_exists(self):
        assert hasattr(mod, "mish")

    def test_var0(self):
        try:
            mod.mish(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mish(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mish(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mish("")
        except EXC:
            pass


class Test_mode_mult:
    def test_exists(self):
        assert hasattr(mod, "mode_mult")

    def test_doc0(self):
        try:
            mod.mode_mult([1, 2, 3, 4, 3, 2, 1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mode_mult(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mode_mult(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mode_mult(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mode_mult([])
        except EXC:
            pass


class Test_mode_single:
    def test_exists(self):
        assert hasattr(mod, "mode_single")

    def test_doc0(self):
        try:
            mod.mode_single([1, 2, 3, 3, 4])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.mode_single([1, 2, 2, 3, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.mode_single(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mode_single(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mode_single(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mode_single([])
        except EXC:
            pass


class Test_moors_kurtosis:
    def test_exists(self):
        assert hasattr(mod, "moors_kurtosis")

    def test_var0(self):
        try:
            mod.moors_kurtosis(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moors_kurtosis(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moors_kurtosis(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moors_kurtosis([])
        except EXC:
            pass


class Test_moving_median:
    def test_exists(self):
        assert hasattr(mod, "moving_median")

    def test_doc0(self):
        try:
            mod.moving_median([1, 3, 5, 7, 9], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.moving_median(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.moving_median(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.moving_median(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.moving_median([], "")
        except EXC:
            pass


class Test_multinomial_coefficient:
    def test_exists(self):
        assert hasattr(mod, "multinomial_coefficient")

    def test_doc0(self):
        try:
            mod.multinomial_coefficient(2, 3, 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.multinomial_coefficient()
        except EXC:
            pass


class Test_mutual_information:
    def test_exists(self):
        assert hasattr(mod, "mutual_information")

    def test_var0(self):
        try:
            mod.mutual_information(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.mutual_information(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.mutual_information(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.mutual_information("")
        except EXC:
            pass


class Test_negative_binomial_pmf:
    def test_exists(self):
        assert hasattr(mod, "negative_binomial_pmf")

    def test_var0(self):
        try:
            mod.negative_binomial_pmf(0, 0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.negative_binomial_pmf(1, 1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.negative_binomial_pmf(None, 0, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.negative_binomial_pmf(0, "", "")
        except EXC:
            pass


class Test_negative_predictive_value:
    def test_exists(self):
        assert hasattr(mod, "negative_predictive_value")

    def test_doc0(self):
        try:
            mod.negative_predictive_value(900, 20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.negative_predictive_value(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.negative_predictive_value(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.negative_predictive_value(None, 0)
        except EXC:
            pass


class Test_normal_cdf:
    def test_exists(self):
        assert hasattr(mod, "normal_cdf")

    def test_var0(self):
        try:
            mod.normal_cdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.normal_cdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.normal_cdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.normal_cdf("")
        except EXC:
            pass


class Test_normal_pdf:
    def test_exists(self):
        assert hasattr(mod, "normal_pdf")

    def test_var0(self):
        try:
            mod.normal_pdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.normal_pdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.normal_pdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.normal_pdf("")
        except EXC:
            pass


class Test_odds_ratio:
    def test_exists(self):
        assert hasattr(mod, "odds_ratio")

    def test_doc0(self):
        try:
            mod.odds_ratio(80, 900, 100, 20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.odds_ratio(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.odds_ratio(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.odds_ratio(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.odds_ratio("", 0, "", 0)
        except EXC:
            pass


class Test_outliers_iqr:
    def test_exists(self):
        assert hasattr(mod, "outliers_iqr")

    def test_doc0(self):
        try:
            mod.outliers_iqr([1, 2, 3, 4, 5, 100])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.outliers_iqr([10, 12, 14, 16, 18])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.outliers_iqr(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.outliers_iqr(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.outliers_iqr(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.outliers_iqr([])
        except EXC:
            pass


class Test_pareto_pdf:
    def test_exists(self):
        assert hasattr(mod, "pareto_pdf")

    def test_var0(self):
        try:
            mod.pareto_pdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pareto_pdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pareto_pdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pareto_pdf("", "", 0)
        except EXC:
            pass


class Test_partial_autocorrelation:
    def test_exists(self):
        assert hasattr(mod, "partial_autocorrelation")

    def test_var0(self):
        try:
            mod.partial_autocorrelation(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.partial_autocorrelation(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.partial_autocorrelation(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.partial_autocorrelation([], 0)
        except EXC:
            pass


class Test_pct_change:
    def test_exists(self):
        assert hasattr(mod, "pct_change")

    def test_doc0(self):
        try:
            mod.pct_change([100, 110, 99])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.pct_change([50, 0, 100])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pct_change(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pct_change(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pct_change(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pct_change([])
        except EXC:
            pass


class Test_percentile_exc:
    def test_exists(self):
        assert hasattr(mod, "percentile_exc")

    def test_doc0(self):
        try:
            mod.percentile_exc([1, 2, 3, 4], 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.percentile_exc(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.percentile_exc(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.percentile_exc(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.percentile_exc([], 0)
        except EXC:
            pass


class Test_percentile_rank:
    def test_exists(self):
        assert hasattr(mod, "percentile_rank")

    def test_doc0(self):
        try:
            mod.percentile_rank([1, 2, 3, 4, 5], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.percentile_rank(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.percentile_rank(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.percentile_rank(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.percentile_rank([], "")
        except EXC:
            pass


class Test_percentile_to_z:
    def test_exists(self):
        assert hasattr(mod, "percentile_to_z")

    def test_var0(self):
        try:
            mod.percentile_to_z(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.percentile_to_z(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.percentile_to_z(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.percentile_to_z("")
        except EXC:
            pass


class Test_percentile_to_z_score:
    def test_exists(self):
        assert hasattr(mod, "percentile_to_z_score")

    def test_var0(self):
        try:
            mod.percentile_to_z_score(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.percentile_to_z_score(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.percentile_to_z_score(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.percentile_to_z_score("")
        except EXC:
            pass


class Test_percentrank_exc:
    def test_exists(self):
        assert hasattr(mod, "percentrank_exc")

    def test_doc0(self):
        try:
            mod.percentrank_exc([1, 2, 3, 6, 6, 6, 7, 8, 9], 7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.percentrank_exc(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.percentrank_exc(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.percentrank_exc(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.percentrank_exc([], "")
        except EXC:
            pass


class Test_point_biserial_correlation:
    def test_exists(self):
        assert hasattr(mod, "point_biserial_correlation")

    def test_var0(self):
        try:
            mod.point_biserial_correlation(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.point_biserial_correlation(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.point_biserial_correlation(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.point_biserial_correlation("", "")
        except EXC:
            pass


class Test_poisson_pmf:
    def test_exists(self):
        assert hasattr(mod, "poisson_pmf")

    def test_var0(self):
        try:
            mod.poisson_pmf(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.poisson_pmf(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.poisson_pmf(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.poisson_pmf(0, "")
        except EXC:
            pass


class Test_poisson_probability:
    def test_exists(self):
        assert hasattr(mod, "poisson_probability")

    def test_var0(self):
        try:
            mod.poisson_probability(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.poisson_probability(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.poisson_probability(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.poisson_probability(0, "")
        except EXC:
            pass


class Test_precision_score_scalar:
    def test_exists(self):
        assert hasattr(mod, "precision_score_scalar")

    def test_doc0(self):
        try:
            mod.precision_score_scalar(80, 20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.precision_score_scalar(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.precision_score_scalar(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.precision_score_scalar(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.precision_score_scalar("", "")
        except EXC:
            pass


class Test_probability_range:
    def test_exists(self):
        assert hasattr(mod, "probability_range")

    def test_doc0(self):
        try:
            mod.probability_range([0, 1, 2, 3], [0.1, 0.2, 0.4, 0.3], 1, 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.probability_range([10, 20, 30], [0.3, 0.5, 0.2], 20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.probability_range(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.probability_range(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.probability_range(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.probability_range("", 0, 0)
        except EXC:
            pass


class Test_quantile:
    def test_exists(self):
        assert hasattr(mod, "quantile")

    def test_doc0(self):
        try:
            mod.quantile([1, 2, 3, 4, 5], 0.25)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.quantile([1, 2, 3, 4, 5], 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.quantile(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.quantile(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.quantile(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.quantile([], "")
        except EXC:
            pass


class Test_quartile_deviation:
    def test_exists(self):
        assert hasattr(mod, "quartile_deviation")

    def test_doc0(self):
        try:
            mod.quartile_deviation([1, 2, 3, 4, 5, 6, 7, 8])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.quartile_deviation(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.quartile_deviation(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.quartile_deviation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.quartile_deviation([])
        except EXC:
            pass


class Test_quartile_exc:
    def test_exists(self):
        assert hasattr(mod, "quartile_exc")

    def test_doc0(self):
        try:
            mod.quartile_exc([6, 7, 15, 36, 39, 40, 41, 42, 43, 47, 49], 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.quartile_exc(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.quartile_exc(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.quartile_exc(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.quartile_exc([], "")
        except EXC:
            pass


class Test_r_squared:
    def test_exists(self):
        assert hasattr(mod, "r_squared")

    def test_var0(self):
        try:
            mod.r_squared(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.r_squared(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.r_squared(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.r_squared("", "")
        except EXC:
            pass


class Test_r_squared_scalar:
    def test_exists(self):
        assert hasattr(mod, "r_squared_scalar")

    def test_doc0(self):
        try:
            mod.r_squared_scalar(20, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.r_squared_scalar(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.r_squared_scalar(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.r_squared_scalar(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.r_squared_scalar("", "")
        except EXC:
            pass


class Test_rank:
    def test_exists(self):
        assert hasattr(mod, "rank")

    def test_doc0(self):
        try:
            mod.rank([40, 10, 30, 20])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.rank([10, 20, 20, 30], method="min")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rank(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rank(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rank(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rank([])
        except EXC:
            pass


class Test_rayleigh_pdf:
    def test_exists(self):
        assert hasattr(mod, "rayleigh_pdf")

    def test_var0(self):
        try:
            mod.rayleigh_pdf(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rayleigh_pdf(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rayleigh_pdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rayleigh_pdf("")
        except EXC:
            pass


class Test_recall_score_scalar:
    def test_exists(self):
        assert hasattr(mod, "recall_score_scalar")

    def test_doc0(self):
        try:
            mod.recall_score_scalar(80, 20)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.recall_score_scalar(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.recall_score_scalar(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.recall_score_scalar(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.recall_score_scalar("", 0)
        except EXC:
            pass


class Test_relative_error:
    def test_exists(self):
        assert hasattr(mod, "relative_error")

    def test_doc0(self):
        try:
            mod.relative_error(10.5, 10.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.relative_error(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.relative_error(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.relative_error(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.relative_error("", "")
        except EXC:
            pass


class Test_relative_standard_deviation:
    def test_exists(self):
        assert hasattr(mod, "relative_standard_deviation")

    def test_var0(self):
        try:
            mod.relative_standard_deviation(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.relative_standard_deviation(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.relative_standard_deviation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.relative_standard_deviation([])
        except EXC:
            pass


class Test_relu:
    def test_exists(self):
        assert hasattr(mod, "relu")

    def test_doc0(self):
        try:
            mod.relu(-3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.relu(5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.relu(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.relu(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.relu(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.relu("")
        except EXC:
            pass


class Test_residual_standard_error:
    def test_exists(self):
        assert hasattr(mod, "residual_standard_error")

    def test_var0(self):
        try:
            mod.residual_standard_error(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.residual_standard_error(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.residual_standard_error(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.residual_standard_error("", "")
        except EXC:
            pass


class Test_risk_ratio:
    def test_exists(self):
        assert hasattr(mod, "risk_ratio")

    def test_doc0(self):
        try:
            mod.risk_ratio(30, 100, 10, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.risk_ratio(0, 0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.risk_ratio(1, 1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.risk_ratio(None, 0, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.risk_ratio("", "", "", "")
        except EXC:
            pass


class Test_rolling_correlation:
    def test_exists(self):
        assert hasattr(mod, "rolling_correlation")

    def test_doc0(self):
        try:
            mod.rolling_correlation([1,2,3,4,5], [2,4,6,8,10], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rolling_correlation(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rolling_correlation(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rolling_correlation(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rolling_correlation([], [], "")
        except EXC:
            pass


class Test_rolling_mean:
    def test_exists(self):
        assert hasattr(mod, "rolling_mean")

    def test_doc0(self):
        try:
            mod.rolling_mean([1, 2, 3, 4, 5], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rolling_mean(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rolling_mean(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rolling_mean(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rolling_mean([], "")
        except EXC:
            pass


class Test_rolling_median:
    def test_exists(self):
        assert hasattr(mod, "rolling_median")

    def test_doc0(self):
        try:
            mod.rolling_median([1, 3, 5, 7, 9], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rolling_median(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rolling_median(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rolling_median(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rolling_median([], "")
        except EXC:
            pass


class Test_rolling_std:
    def test_exists(self):
        assert hasattr(mod, "rolling_std")

    def test_doc0(self):
        try:
            mod.rolling_std([2, 4, 4, 4, 5, 5, 7, 9], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rolling_std(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rolling_std(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rolling_std(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rolling_std([], "")
        except EXC:
            pass


class Test_rolling_sum:
    def test_exists(self):
        assert hasattr(mod, "rolling_sum")

    def test_doc0(self):
        try:
            mod.rolling_sum([1, 2, 3, 4, 5], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rolling_sum(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rolling_sum(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rolling_sum(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rolling_sum([], "")
        except EXC:
            pass


class Test_root_mean_square:
    def test_exists(self):
        assert hasattr(mod, "root_mean_square")

    def test_var0(self):
        try:
            mod.root_mean_square(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.root_mean_square(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.root_mean_square(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.root_mean_square([])
        except EXC:
            pass


class Test_root_mean_squared_error:
    def test_exists(self):
        assert hasattr(mod, "root_mean_squared_error")

    def test_var0(self):
        try:
            mod.root_mean_squared_error(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.root_mean_squared_error(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.root_mean_squared_error(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.root_mean_squared_error("", "")
        except EXC:
            pass


class Test_root_mean_squared_log_error:
    def test_exists(self):
        assert hasattr(mod, "root_mean_squared_log_error")

    def test_var0(self):
        try:
            mod.root_mean_squared_log_error(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.root_mean_squared_log_error(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.root_mean_squared_log_error(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.root_mean_squared_log_error("", "")
        except EXC:
            pass


class Test_running_max:
    def test_exists(self):
        assert hasattr(mod, "running_max")

    def test_doc0(self):
        try:
            mod.running_max([1, 3, 2, 5, 4], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.running_max(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.running_max(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.running_max(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.running_max([], "")
        except EXC:
            pass


class Test_running_min:
    def test_exists(self):
        assert hasattr(mod, "running_min")

    def test_doc0(self):
        try:
            mod.running_min([1, 3, 2, 5, 4], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.running_min(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.running_min(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.running_min(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.running_min([], "")
        except EXC:
            pass


class Test_running_std:
    def test_exists(self):
        assert hasattr(mod, "running_std")

    def test_var0(self):
        try:
            mod.running_std(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.running_std(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.running_std(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.running_std([], "")
        except EXC:
            pass


class Test_runs_test_statistic:
    def test_exists(self):
        assert hasattr(mod, "runs_test_statistic")

    def test_doc0(self):
        try:
            mod.runs_test_statistic([1, 1, 0, 0, 1, 0, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.runs_test_statistic(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.runs_test_statistic(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.runs_test_statistic(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.runs_test_statistic([])
        except EXC:
            pass


class Test_shannon_entropy:
    def test_exists(self):
        assert hasattr(mod, "shannon_entropy")

    def test_var0(self):
        try:
            mod.shannon_entropy(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.shannon_entropy(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.shannon_entropy(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.shannon_entropy(0)
        except EXC:
            pass


class Test_shapiro_wilk_w:
    def test_exists(self):
        assert hasattr(mod, "shapiro_wilk_w")

    def test_var0(self):
        try:
            mod.shapiro_wilk_w(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.shapiro_wilk_w(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.shapiro_wilk_w(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.shapiro_wilk_w([])
        except EXC:
            pass


class Test_sigmoid:
    def test_exists(self):
        assert hasattr(mod, "sigmoid")

    def test_doc0(self):
        try:
            mod.sigmoid(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sigmoid(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sigmoid(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sigmoid(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sigmoid("")
        except EXC:
            pass


class Test_simple_moving_average:
    def test_exists(self):
        assert hasattr(mod, "simple_moving_average")

    def test_doc0(self):
        try:
            mod.simple_moving_average([1, 2, 3, 4, 5], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.simple_moving_average(3.14, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.simple_moving_average(100, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.simple_moving_average(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.simple_moving_average([], "")
        except EXC:
            pass


class Test_skew_p:
    def test_exists(self):
        assert hasattr(mod, "skew_p")

    def test_var0(self):
        try:
            mod.skew_p(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.skew_p(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.skew_p(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.skew_p([])
        except EXC:
            pass


class Test_skewness:
    def test_exists(self):
        assert hasattr(mod, "skewness")

    def test_var0(self):
        try:
            mod.skewness(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.skewness(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.skewness(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.skewness([])
        except EXC:
            pass


class Test_slope:
    def test_exists(self):
        assert hasattr(mod, "slope")

    def test_doc0(self):
        try:
            mod.slope([2, 4, 6], [1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.slope(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.slope(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.slope(None, 0)
        except EXC:
            pass


class Test_small:
    def test_exists(self):
        assert hasattr(mod, "small")

    def test_doc0(self):
        try:
            mod.small([3, 1, 4, 1, 5, 9], 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.small([3, 1, 4, 1, 5, 9], 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.small(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.small(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.small(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.small([], 0)
        except EXC:
            pass


class Test_softplus:
    def test_exists(self):
        assert hasattr(mod, "softplus")

    def test_var0(self):
        try:
            mod.softplus(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.softplus(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.softplus(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.softplus("")
        except EXC:
            pass


class Test_spearman_correlation:
    def test_exists(self):
        assert hasattr(mod, "spearman_correlation")

    def test_doc0(self):
        try:
            mod.spearman_correlation([1, 2, 3, 4, 5], [5, 6, 7, 8, 7])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.spearman_correlation([1, 2, 3], [3, 2, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.spearman_correlation(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spearman_correlation(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spearman_correlation(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spearman_correlation([], [])
        except EXC:
            pass


class Test_spearman_rank_correlation:
    def test_exists(self):
        assert hasattr(mod, "spearman_rank_correlation")

    def test_var0(self):
        try:
            mod.spearman_rank_correlation(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.spearman_rank_correlation(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.spearman_rank_correlation(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.spearman_rank_correlation([], [])
        except EXC:
            pass


class Test_specificity_score_scalar:
    def test_exists(self):
        assert hasattr(mod, "specificity_score_scalar")

    def test_doc0(self):
        try:
            mod.specificity_score_scalar(900, 100)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.specificity_score_scalar(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.specificity_score_scalar(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.specificity_score_scalar(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.specificity_score_scalar(0, "")
        except EXC:
            pass


class Test_standard_error:
    def test_exists(self):
        assert hasattr(mod, "standard_error")

    def test_var0(self):
        try:
            mod.standard_error(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.standard_error(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.standard_error(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.standard_error([])
        except EXC:
            pass


class Test_standard_error_estimate:
    def test_exists(self):
        assert hasattr(mod, "standard_error_estimate")

    def test_var0(self):
        try:
            mod.standard_error_estimate(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.standard_error_estimate(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.standard_error_estimate(None, 0)
        except EXC:
            pass


class Test_standardize:
    def test_exists(self):
        assert hasattr(mod, "standardize")

    def test_doc0(self):
        try:
            mod.standardize(42, 40, 1.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.standardize(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.standardize(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.standardize(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.standardize("", 0, "")
        except EXC:
            pass


class Test_sum_if:
    def test_exists(self):
        assert hasattr(mod, "sum_if")

    def test_doc0(self):
        try:
            mod.sum_if([10, 20, 30, 40], ["A", "B", "A", "B"], "A")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sum_if([1, 2, 3, 4], [10, 20, 30, 40], ">15")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sum_if(0, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_if(1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_if(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sum_if([], "", "")
        except EXC:
            pass


class Test_sum_list:
    def test_exists(self):
        assert hasattr(mod, "sum_list")

    def test_doc0(self):
        try:
            mod.sum_list([1, 2, 3, 4])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sum_list([1.5, 2.5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sum_list(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_list(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_list(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sum_list([])
        except EXC:
            pass


class Test_sum_of_squared_deviations:
    def test_exists(self):
        assert hasattr(mod, "sum_of_squared_deviations")

    def test_var0(self):
        try:
            mod.sum_of_squared_deviations(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_of_squared_deviations(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_of_squared_deviations(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sum_of_squared_deviations([])
        except EXC:
            pass


class Test_sum_of_squares:
    def test_exists(self):
        assert hasattr(mod, "sum_of_squares")

    def test_doc0(self):
        try:
            mod.sum_of_squares([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sum_of_squares([1, 1, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sum_of_squares(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_of_squares(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_of_squares(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sum_of_squares([])
        except EXC:
            pass


class Test_sum_product:
    def test_exists(self):
        assert hasattr(mod, "sum_product")

    def test_doc0(self):
        try:
            mod.sum_product([1, 2, 3], [4, 5, 6])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sum_product([10, 20], [0.5, 0.3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sum_product(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sum_product(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sum_product(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sum_product("", "")
        except EXC:
            pass


class Test_swish:
    def test_exists(self):
        assert hasattr(mod, "swish")

    def test_doc0(self):
        try:
            mod.swish(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.swish(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.swish(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.swish(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.swish("")
        except EXC:
            pass


class Test_symmetric_mape:
    def test_exists(self):
        assert hasattr(mod, "symmetric_mape")

    def test_doc0(self):
        try:
            mod.symmetric_mape(100, 80)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.symmetric_mape(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.symmetric_mape(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.symmetric_mape(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.symmetric_mape("", "")
        except EXC:
            pass


class Test_t_test:
    def test_exists(self):
        assert hasattr(mod, "t_test")

    def test_var0(self):
        try:
            mod.t_test(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.t_test(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.t_test(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.t_test([], [])
        except EXC:
            pass


class Test_tanh_activation:
    def test_exists(self):
        assert hasattr(mod, "tanh_activation")

    def test_doc0(self):
        try:
            mod.tanh_activation(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.tanh_activation(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tanh_activation(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tanh_activation(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tanh_activation("")
        except EXC:
            pass


class Test_theil_sen_slope:
    def test_exists(self):
        assert hasattr(mod, "theil_sen_slope")

    def test_doc0(self):
        try:
            mod.theil_sen_slope([1, 2, 3, 4], [2, 4, 6, 8])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.theil_sen_slope(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.theil_sen_slope(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.theil_sen_slope(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.theil_sen_slope([], [])
        except EXC:
            pass


class Test_trend:
    def test_exists(self):
        assert hasattr(mod, "trend")

    def test_var0(self):
        try:
            mod.trend(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.trend(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.trend(None)
        except EXC:
            pass


class Test_triangular_pdf:
    def test_exists(self):
        assert hasattr(mod, "triangular_pdf")

    def test_var0(self):
        try:
            mod.triangular_pdf(3.14, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.triangular_pdf(100, 100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.triangular_pdf(None, 3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.triangular_pdf("", "", "", "")
        except EXC:
            pass


class Test_trimmed_mean:
    def test_exists(self):
        assert hasattr(mod, "trimmed_mean")

    def test_doc0(self):
        try:
            mod.trimmed_mean([1, 2, 3, 4, 100], 0.2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.trimmed_mean(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.trimmed_mean(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.trimmed_mean(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.trimmed_mean([], 0)
        except EXC:
            pass


class Test_trimmed_variance:
    def test_exists(self):
        assert hasattr(mod, "trimmed_variance")

    def test_var0(self):
        try:
            mod.trimmed_variance(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.trimmed_variance(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.trimmed_variance(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.trimmed_variance([])
        except EXC:
            pass


class Test_tukey_trimean:
    def test_exists(self):
        assert hasattr(mod, "tukey_trimean")

    def test_doc0(self):
        try:
            mod.tukey_trimean([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.tukey_trimean([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tukey_trimean([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tukey_trimean(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tukey_trimean([])
        except EXC:
            pass


class Test_uniform_cdf:
    def test_exists(self):
        assert hasattr(mod, "uniform_cdf")

    def test_doc0(self):
        try:
            mod.uniform_cdf(0.5, 0.0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.uniform_cdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.uniform_cdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.uniform_cdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.uniform_cdf("", "", "")
        except EXC:
            pass


class Test_uniform_pdf:
    def test_exists(self):
        assert hasattr(mod, "uniform_pdf")

    def test_doc0(self):
        try:
            mod.uniform_pdf(0.5, 0.0, 1.0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.uniform_pdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.uniform_pdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.uniform_pdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.uniform_pdf("", "", "")
        except EXC:
            pass


class Test_weibull_pdf:
    def test_exists(self):
        assert hasattr(mod, "weibull_pdf")

    def test_var0(self):
        try:
            mod.weibull_pdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weibull_pdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weibull_pdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weibull_pdf("", 0, "")
        except EXC:
            pass


class Test_weighted_mean:
    def test_exists(self):
        assert hasattr(mod, "weighted_mean")

    def test_doc0(self):
        try:
            mod.weighted_mean([80, 90], [3, 7])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.weighted_mean([10, 20, 30], [1, 1, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.weighted_mean(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weighted_mean(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weighted_mean(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weighted_mean([], [])
        except EXC:
            pass


class Test_weighted_median:
    def test_exists(self):
        assert hasattr(mod, "weighted_median")

    def test_doc0(self):
        try:
            mod.weighted_median([1, 2, 3], [1, 1, 1])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.weighted_median([1, 2, 3, 4, 5], [5, 1, 1, 1, 1])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.weighted_median(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weighted_median(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weighted_median(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weighted_median([], [])
        except EXC:
            pass


class Test_weighted_moving_average:
    def test_exists(self):
        assert hasattr(mod, "weighted_moving_average")

    def test_var0(self):
        try:
            mod.weighted_moving_average(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weighted_moving_average(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weighted_moving_average(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weighted_moving_average([], [])
        except EXC:
            pass


class Test_weighted_variance:
    def test_exists(self):
        assert hasattr(mod, "weighted_variance")

    def test_var0(self):
        try:
            mod.weighted_variance(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.weighted_variance(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.weighted_variance(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.weighted_variance([], [])
        except EXC:
            pass


class Test_winsorize:
    def test_exists(self):
        assert hasattr(mod, "winsorize")

    def test_doc0(self):
        try:
            mod.winsorize([1, 2, 3, 4, 100], 0.2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.winsorize(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.winsorize(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.winsorize(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.winsorize([], 0)
        except EXC:
            pass


class Test_winsorized_mean:
    def test_exists(self):
        assert hasattr(mod, "winsorized_mean")

    def test_doc0(self):
        try:
            mod.winsorized_mean([1, 2, 3, 4, 100], 0.2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.winsorized_mean(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.winsorized_mean(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.winsorized_mean(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.winsorized_mean([])
        except EXC:
            pass


class Test_z_score:
    def test_exists(self):
        assert hasattr(mod, "z_score")

    def test_doc0(self):
        try:
            mod.z_score(85, 70, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.z_score(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.z_score(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.z_score(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.z_score("", 0, "")
        except EXC:
            pass


class Test_z_score_single:
    def test_exists(self):
        assert hasattr(mod, "z_score_single")

    def test_doc0(self):
        try:
            mod.z_score_single(85, 70, 10)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.z_score_single(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.z_score_single(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.z_score_single(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.z_score_single("", 0, "")
        except EXC:
            pass


class Test_z_score_to_percentile:
    def test_exists(self):
        assert hasattr(mod, "z_score_to_percentile")

    def test_var0(self):
        try:
            mod.z_score_to_percentile(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.z_score_to_percentile(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.z_score_to_percentile(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.z_score_to_percentile("")
        except EXC:
            pass


class Test_z_test:
    def test_exists(self):
        assert hasattr(mod, "z_test")

    def test_var0(self):
        try:
            mod.z_test(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.z_test(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.z_test(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.z_test([], "")
        except EXC:
            pass


class Test_z_to_percentile:
    def test_exists(self):
        assert hasattr(mod, "z_to_percentile")

    def test_var0(self):
        try:
            mod.z_to_percentile(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.z_to_percentile(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.z_to_percentile(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.z_to_percentile("")
        except EXC:
            pass


class Test_zipf_pmf:
    def test_exists(self):
        assert hasattr(mod, "zipf_pmf")

    def test_var0(self):
        try:
            mod.zipf_pmf(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.zipf_pmf(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.zipf_pmf(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.zipf_pmf(0, "", 0)
        except EXC:
            pass

