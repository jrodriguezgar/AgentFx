"""Tests for fxNumeric.statistics_functions."""

import math

import pytest

from agentfx.fxNumeric import (
    absolute_error,
    adjusted_r_squared,
    anderson_darling,
    autocorrelation,
    balanced_accuracy_scalar,
    bayes_posterior,
    bayes_theorem,
    bayesian_update,
    benford_distribution,
    beta_function,
    beta_function_value,
    binary_entropy,
    binomial_pmf,
    binomial_probability,
    bowley_skewness,
    cauchy_pdf,
    chi_squared_pdf,
    chi_squared_statistic,
    coefficient_of_quartile_deviation,
    coefficient_of_variation,
    cohens_d,
    cohens_kappa_scalar,
    cosine_similarity,
    cosine_similarity_scalar,
    cramers_v,
    cross_entropy,
    cross_entropy_binary,
    cumulative_moving_average,
    dixon_q_test,
    elu,
    entropy,
    entropy_binary,
    erlang_pdf,
    euclidean_distance,
    exponential_cdf,
    exponential_moving_average,
    exponential_pdf,
    false_discovery_rate,
    gamma_pdf,
    geometric_pdf,
    geometric_pmf,
    gini_impurity_binary,
    glass_delta,
    grubbs_test,
    gumbel_pdf,
    hedges_g,
    holt_linear_forecast,
    huber_loss,
    hypergeometric_pmf,
    jaccard_index_scalar,
    js_divergence,
    kendall_tau,
    kl_divergence,
    laplace_pdf,
    leaky_relu,
    ljung_box,
    log_cosh_loss,
    log_normal_pdf,
    logistic_cdf,
    logistic_function,
    logistic_pdf,
    logit,
    mahalanobis_distance_1d,
    manhattan_distance,
    markov_chain_steady_state,
    maxwell_boltzmann_pdf,
    mean_absolute_error,
    mean_absolute_percentage_error,
    mean_percentage_error,
    mean_squared_error,
    median_absolute_deviation,
    midhinge,
    midrange,
    moors_kurtosis,
    multinomial_coefficient,
    mutual_information,
    negative_binomial_pmf,
    negative_predictive_value,
    normal_cdf,
    normal_pdf,
    odds_ratio,
    outliers_iqr,
    pareto_pdf,
    partial_autocorrelation,
    pct_change,
    percentile_rank,
    percentile_to_z_score,
    point_biserial_correlation,
    poisson_pmf,
    poisson_probability,
    quartile_deviation,
    r_squared,
    r_squared_scalar,
    rayleigh_pdf,
    relative_error,
    relu,
    residual_standard_error,
    risk_ratio,
    rolling_std,
    root_mean_square,
    root_mean_squared_log_error,
    running_max,
    running_min,
    running_std,
    shannon_entropy,
    shapiro_wilk_w,
    sigmoid,
    simple_moving_average,
    softplus,
    spearman_correlation,
    standard_error,
    swish,
    symmetric_mape,
    triangular_pdf,
    trimmed_variance,
    tukey_trimean,
    uniform_cdf,
    uniform_pdf,
    weibull_pdf,
    weighted_median,
    weighted_moving_average,
    weighted_variance,
    winsorize,
    winsorized_mean,
    z_score,
    z_score_to_percentile,
    zipf_pmf,
)
from agentfx.fxNumeric.finance_functions import (
    annuity_due_pv,
    convexity_adjustment,
    cost_of_debt_after_tax,
    purchasing_power,
)
from agentfx.fxNumeric.number_theory_functions import is_coprime


class TestIsCoprime:

    def test_coprime(self):
        assert is_coprime(14, 15) is True

    def test_not_coprime(self):
        assert is_coprime(14, 21) is False

    def test_one(self):
        assert is_coprime(1, 100) is True


# ── Statistics ───────────────────────────────────────────────────────────────


class TestRootMeanSquare:

    def test_basic(self):
        assert root_mean_square([1, 2, 3, 4, 5]) == pytest.approx(3.316625, rel=1e-4)

    def test_single(self):
        assert root_mean_square([5]) == pytest.approx(5.0)

    def test_empty(self):
        with pytest.raises(ValueError):
            root_mean_square([])

class TestWeightedVariance:

    def test_population(self):
        result = weighted_variance([2, 4, 6], [1, 2, 1], sample=False)
        assert result == pytest.approx(2.0, rel=1e-4)

    def test_different_lengths(self):
        with pytest.raises(ValueError):
            weighted_variance([1, 2], [1], sample=False)

    def test_negative_weights(self):
        with pytest.raises(ValueError):
            weighted_variance([1, 2, 3], [-1, 1, 1], sample=False)

class TestKendallTau:

    def test_perfect_concordance(self):
        assert kendall_tau([1, 2, 3, 4], [1, 2, 3, 4]) == pytest.approx(1.0)

    def test_perfect_discordance(self):
        assert kendall_tau([1, 2, 3, 4], [4, 3, 2, 1]) == pytest.approx(-1.0)

    def test_different_lengths(self):
        with pytest.raises(ValueError):
            kendall_tau([1, 2], [1, 2, 3])

class TestBootstrapCI:

    def test_contains_mean(self):
        from agentfx.fxNumeric.statistics_functions import bootstrap_mean_ci

        lo, hi = bootstrap_mean_ci([1, 2, 3, 4, 5], 0.95, 5000, seed=42)
        assert lo < 3.0 < hi

class TestEmpiricalCDF:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import empirical_cdf

        assert empirical_cdf([1, 2, 3, 4, 5], 3) == 0.6

class TestJarqueBera:

    def test_normal_data(self):
        from agentfx.fxNumeric.statistics_functions import jarque_bera

        jb, is_normal = jarque_bera([1, 2, 3, 4, 5])
        assert is_normal is True

class TestDurbinWatson:

    def test_no_autocorrelation(self):
        from agentfx.fxNumeric.statistics_functions import durbin_watson

        # Alternating residuals → DW near 2 or above
        dw = durbin_watson([0.1, -0.1, 0.1, -0.1, 0.1])
        assert 1.5 < dw < 3.5

class TestMannWhitney:

    def test_separated_samples(self):
        from agentfx.fxNumeric.statistics_functions import mann_whitney_u

        u, z = mann_whitney_u([1, 2, 3], [4, 5, 6])
        assert u == 0.0

class TestRunsTest:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import runs_test_statistic

        runs, z = runs_test_statistic([1, 1, 0, 0, 1, 0, 1])
        assert runs == 5

class TestTheilSenSlope:

    def test_perfect_linear(self):
        from agentfx.fxNumeric.statistics_functions import theil_sen_slope

        assert theil_sen_slope([1, 2, 3, 4], [2, 4, 6, 8]) == 2.0

class TestExponentialSmoothingSingle:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import exponential_smoothing_single

        assert exponential_smoothing_single(10, 8, 0.3) == pytest.approx(8.6)

class TestBayesianUpdate:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import bayesian_update

        assert bayesian_update(0.01, [0.9], [0.05]) == pytest.approx(0.18)


# ── fxNumeric — Engineering ──────────────────────────────────────────────

class TestMeanAbsoluteError:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import mean_absolute_error
        assert mean_absolute_error([3, -0.5, 2, 7], [2.5, 0.0, 2, 8]) == 0.5

    def test_perfect(self):
        from agentfx.fxNumeric.statistics_functions import mean_absolute_error
        assert mean_absolute_error([1, 2, 3], [1, 2, 3]) == 0.0

    def test_length_mismatch(self):
        from agentfx.fxNumeric.statistics_functions import mean_absolute_error

        with pytest.raises(ValueError):
            mean_absolute_error([1, 2], [1])

class TestRootMeanSquaredError:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import root_mean_squared_error
        assert round(root_mean_squared_error([3, -0.5, 2, 7], [2.5, 0.0, 2, 8]), 4) == 0.6124

    def test_perfect(self):
        from agentfx.fxNumeric.statistics_functions import root_mean_squared_error
        assert root_mean_squared_error([1, 2, 3], [1, 2, 3]) == 0.0

class TestRelativeStandardDeviation:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import relative_standard_deviation
        assert round(relative_standard_deviation([10, 12, 11, 9, 13]), 2) == 14.37

    def test_zero_mean_raises(self):
        from agentfx.fxNumeric.statistics_functions import relative_standard_deviation

        with pytest.raises(ValueError):
            relative_standard_deviation([-1, 1])

class TestGiniCoefficient:

    def test_equal(self):
        from agentfx.fxNumeric.statistics_functions import gini_coefficient
        assert gini_coefficient([1, 1, 1, 1]) == 0.0

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import gini_coefficient
        assert round(gini_coefficient([1, 2, 3, 4, 5]), 4) == 0.2667

    def test_negative_raises(self):
        from agentfx.fxNumeric.statistics_functions import gini_coefficient

        with pytest.raises(ValueError):
            gini_coefficient([-1, 2])


# ── Interpolation ───────────────────────────────────────────────

class TestSpearmanRankCorrelation:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import spearman_rank_correlation
        assert round(spearman_rank_correlation([1, 2, 3, 4, 5], [5, 6, 7, 8, 7]), 2) == 0.82

    def test_perfect(self):
        from agentfx.fxNumeric.statistics_functions import spearman_rank_correlation
        assert round(spearman_rank_correlation([1, 2, 3], [10, 20, 30]), 2) == 1.0

    def test_length_mismatch(self):
        from agentfx.fxNumeric.statistics_functions import spearman_rank_correlation

        with pytest.raises(ValueError):
            spearman_rank_correlation([1, 2], [1])

class TestChiSquaredStatistic:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import chi_squared_statistic
        assert chi_squared_statistic([20, 30, 50], [25, 25, 50]) == 2.0

    def test_perfect_fit(self):
        from agentfx.fxNumeric.statistics_functions import chi_squared_statistic
        assert chi_squared_statistic([10, 20, 30], [10, 20, 30]) == 0.0

    def test_zero_expected(self):
        from agentfx.fxNumeric.statistics_functions import chi_squared_statistic

        with pytest.raises(ValueError):
            chi_squared_statistic([10, 20], [0, 20])

class TestMovingMedian:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import moving_median
        assert moving_median([1, 3, 5, 7, 9], 3) == [None, None, 3.0, 5.0, 7.0]

    def test_window_1(self):
        from agentfx.fxNumeric.statistics_functions import moving_median
        assert moving_median([5, 3, 8], 1) == [5.0, 3.0, 8.0]

    def test_even_window(self):
        from agentfx.fxNumeric.statistics_functions import moving_median
        assert moving_median([1, 2, 3, 4], 2) == [None, 1.5, 2.5, 3.5]


# ── Trigonometry ─────────────────────────────────────────────────

class TestCoefficientOfVariation:

    def test_basic(self):
        result = coefficient_of_variation([10, 12, 14, 16, 18])
        assert result == pytest.approx(0.225877, rel=1e-4)

    def test_zero_variation(self):
        assert coefficient_of_variation([5, 5, 5]) == pytest.approx(0.0)

    def test_population(self):
        # New API has no 'sample' kwarg — always uses sample std dev
        result = coefficient_of_variation([10, 20, 30])
        assert result == pytest.approx(0.5, rel=1e-2)

    def test_zero_mean_raises(self):
        with pytest.raises(ValueError, match="Mean must not be zero"):
            coefficient_of_variation([-1, 0, 1])

    def test_single_element_raises(self):
        with pytest.raises(ValueError):
            coefficient_of_variation([5])

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            coefficient_of_variation([])

    def test_non_numeric_raises(self):
        with pytest.raises(TypeError):
            coefficient_of_variation([1, "a", 3])


# ============================================================================
# standard_error
# ============================================================================

class TestStandardError:

    def test_basic(self):
        result = standard_error([2, 4, 4, 4, 5, 5, 7, 9])
        assert result == pytest.approx(0.755929, rel=1e-4)

    def test_single_element_raises(self):
        with pytest.raises(ValueError):
            standard_error([5])

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            standard_error([])


# ============================================================================
# median_absolute_deviation
# ============================================================================

class TestMedianAbsoluteDeviation:

    def test_basic(self):
        assert median_absolute_deviation([1, 1, 2, 2, 4, 6, 9]) == 1

    def test_symmetric(self):
        assert median_absolute_deviation([1, 2, 3, 4, 5]) == 1

    def test_single_element(self):
        assert median_absolute_deviation([42]) == 0

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            median_absolute_deviation([])


# ============================================================================
# winsorize
# ============================================================================

class TestWinsorize:

    def test_basic(self):
        result = winsorize([1, 2, 3, 4, 100], 0.2)
        assert result == [2.0, 2.0, 3.0, 4.0, 4.0]

    def test_zero_percent(self):
        result = winsorize([1, 2, 3], 0.0)
        assert result == [1.0, 2.0, 3.0]

    def test_invalid_percent_raises(self):
        with pytest.raises(ValueError):
            winsorize([1, 2, 3], 0.5)

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            winsorize([], 0.1)


# ============================================================================
# spearman_correlation
# ============================================================================

class TestSpearmanCorrelation:

    def test_perfect_positive(self):
        result = spearman_correlation([1, 2, 3, 4, 5], [10, 20, 30, 40, 50])
        assert result == pytest.approx(1.0)

    def test_perfect_negative(self):
        result = spearman_correlation([1, 2, 3], [30, 20, 10])
        assert result == pytest.approx(-1.0)

    def test_non_linear_monotonic(self):
        # Exponential relationship → perfect Spearman despite non-linear
        result = spearman_correlation([1, 2, 3, 4, 5], [1, 4, 9, 16, 25])
        assert result == pytest.approx(1.0)

    def test_too_few_elements_raises(self):
        with pytest.raises(ValueError):
            spearman_correlation([1, 2], [3, 4])

    def test_different_lengths_raises(self):
        with pytest.raises(ValueError):
            spearman_correlation([1, 2, 3], [1, 2])


# ============================================================================
# r_squared
# ============================================================================

class TestRSquared:

    def test_perfect_fit(self):
        assert r_squared([1, 2, 3], [1, 2, 3]) == pytest.approx(1.0)

    def test_partial_fit(self):
        result = r_squared([1, 2, 3, 4, 5], [1.1, 2.0, 2.9, 4.1, 5.0])
        assert result == pytest.approx(0.997, rel=1e-2)

    def test_zero_variance_y_raises(self):
        with pytest.raises(ValueError, match="Total sum of squares must not be zero"):
            r_squared([5, 5, 5], [1, 2, 3])

    def test_single_point_raises(self):
        with pytest.raises(ValueError):
            r_squared([1], [1])


# ============================================================================
# mean_squared_error
# ============================================================================

class TestMeanSquaredError:

    def test_basic(self):
        result = mean_squared_error([3, -0.5, 2, 7], [2.5, 0.0, 2, 8])
        assert result == pytest.approx(0.375)

    def test_perfect_prediction(self):
        assert mean_squared_error([1, 2, 3], [1, 2, 3]) == pytest.approx(0.0)

    def test_different_lengths_raises(self):
        with pytest.raises(ValueError):
            mean_squared_error([1, 2], [1])

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            mean_squared_error([], [])


# ============================================================================
# pct_change
# ============================================================================

class TestPctChange:

    def test_basic(self):
        result = pct_change([100, 110, 99])
        assert result[0] is None
        assert result[1] == pytest.approx(0.1)
        assert result[2] == pytest.approx(-0.1, abs=1e-6)

    def test_zero_denominator(self):
        result = pct_change([50, 0, 100])
        assert result[0] is None
        assert result[1] == pytest.approx(-1.0)
        assert result[2] is None

    def test_single_element(self):
        assert pct_change([42]) == [None]

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            pct_change([])


# ============================================================================
# rolling_std
# ============================================================================

class TestRollingStd:

    def test_basic(self):
        result = rolling_std([2, 4, 4, 4, 5, 5, 7, 9], 3)
        assert result[0] is None
        assert result[1] is None
        assert result[2] == pytest.approx(1.1547, rel=1e-3)
        assert result[3] == pytest.approx(0.0)

    def test_window_too_small_raises(self):
        with pytest.raises(ValueError):
            rolling_std([1, 2, 3], 1)

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            rolling_std([], 2)


# ============================================================================
# outliers_iqr
# ============================================================================

class TestOutliersIqr:

    def test_detects_outlier(self):
        result = outliers_iqr([1, 2, 3, 4, 5, 100])
        assert 100 in result

    def test_no_outliers(self):
        assert outliers_iqr([10, 12, 14, 16, 18]) == []

    def test_too_few_elements_raises(self):
        with pytest.raises(ValueError):
            outliers_iqr([1, 2, 3])

    def test_custom_factor(self):
        # Stricter factor should catch more values
        result = outliers_iqr([1, 2, 3, 4, 5, 6, 7, 8, 9, 20], factor=1.0)
        assert 20 in result


# ============================================================================
# entropy
# ============================================================================

class TestEntropy:

    def test_uniform_binary(self):
        result = entropy([1, 1, 2, 2])
        assert result == pytest.approx(1.0)

    def test_no_uncertainty(self):
        assert entropy(["a", "a", "a", "a"]) == pytest.approx(0.0)

    def test_uniform_four_classes(self):
        result = entropy([1, 2, 3, 4])
        assert result == pytest.approx(2.0)

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            entropy([])


# ============================================================================
# weighted_median
# ============================================================================

class TestWeightedMedian:

    def test_equal_weights(self):
        result = weighted_median([1, 2, 3], [1, 1, 1])
        assert result == pytest.approx(2.0)

    def test_heavy_first(self):
        result = weighted_median([1, 2, 3, 4, 5], [5, 1, 1, 1, 1])
        assert result == pytest.approx(1.0)

    def test_heavy_last(self):
        result = weighted_median([1, 2, 3, 4, 5], [1, 1, 1, 1, 5])
        assert result == pytest.approx(5.0)

    def test_different_lengths_raises(self):
        with pytest.raises(ValueError):
            weighted_median([1, 2], [1])

    def test_non_positive_weights_raises(self):
        with pytest.raises(ValueError):
            weighted_median([1, 2, 3], [1, -1, 1])

class TestFocalLoss:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import focal_loss

        assert round(focal_loss(1, 0.9), 6) == 0.000263

    def test_invalid_label(self):
        from agentfx.fxNumeric.statistics_functions import focal_loss

        with pytest.raises(ValueError):
            focal_loss(2, 0.9)

    def test_invalid_pred(self):
        from agentfx.fxNumeric.statistics_functions import focal_loss

        with pytest.raises(ValueError):
            focal_loss(1, 1.0)

class TestMeanBiasError:

    def test_overestimate(self):
        from agentfx.fxNumeric.statistics_functions import mean_bias_error

        assert mean_bias_error(105, 100) == 5.0

    def test_underestimate(self):
        from agentfx.fxNumeric.statistics_functions import mean_bias_error

        assert mean_bias_error(95, 100) == -5.0

class TestDiceCoefficientScalar:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import dice_coefficient_scalar

        assert dice_coefficient_scalar(30, 10, 5) == pytest.approx(0.8)

    def test_all_zero(self):
        from agentfx.fxNumeric.statistics_functions import dice_coefficient_scalar

        with pytest.raises(ValueError):
            dice_coefficient_scalar(0, 0, 0)

    def test_negative(self):
        from agentfx.fxNumeric.statistics_functions import dice_coefficient_scalar

        with pytest.raises(ValueError):
            dice_coefficient_scalar(-1, 0, 0)

class TestExponentialDecayRate:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import exponential_decay_rate

        assert round(exponential_decay_rate(100, 50, 5), 4) == 0.1386

    def test_final_exceeds_initial(self):
        from agentfx.fxNumeric.statistics_functions import exponential_decay_rate

        with pytest.raises(ValueError):
            exponential_decay_rate(50, 100, 5)

class TestZScoreSingle:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import z_score_single

        assert z_score_single(85, 70, 10) == 1.5

    def test_zero_std(self):
        from agentfx.fxNumeric.statistics_functions import z_score_single

        with pytest.raises(ValueError):
            z_score_single(85, 70, 0)


# ── Physics / Engineering ────────────────────────────────────────────

class TestRecallScoreScalar:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import recall_score_scalar

        assert recall_score_scalar(80, 20) == 0.8

    def test_both_zero(self):
        from agentfx.fxNumeric.statistics_functions import recall_score_scalar

        with pytest.raises(ValueError):
            recall_score_scalar(0, 0)

class TestPrecisionScoreScalar:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import precision_score_scalar

        assert precision_score_scalar(80, 20) == 0.8

    def test_negative(self):
        from agentfx.fxNumeric.statistics_functions import precision_score_scalar

        with pytest.raises(ValueError):
            precision_score_scalar(-1, 20)

class TestF1ScoreScalar:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import f1_score_scalar

        assert f1_score_scalar(80, 10, 20) == pytest.approx(0.8421, rel=1e-3)

    def test_all_zero(self):
        from agentfx.fxNumeric.statistics_functions import f1_score_scalar

        with pytest.raises(ValueError):
            f1_score_scalar(0, 0, 0)

class TestSpecificityScoreScalar:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import specificity_score_scalar

        assert specificity_score_scalar(900, 100) == 0.9

    def test_type_error(self):
        from agentfx.fxNumeric.statistics_functions import specificity_score_scalar

        with pytest.raises(TypeError):
            specificity_score_scalar("a", 100)

class TestMatthewsCorrcoefScalar:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import matthews_corrcoef_scalar

        assert round(matthews_corrcoef_scalar(80, 900, 100, 20), 3) == 0.544

    def test_degenerate(self):
        from agentfx.fxNumeric.statistics_functions import matthews_corrcoef_scalar

        with pytest.raises(ValueError):
            matthews_corrcoef_scalar(0, 0, 0, 0)


# ── Physics / Engineering ────────────────────────────────────────────

class TestOddsRatio:

    def test_basic(self):
        assert odds_ratio(50, 40, 10, 5) == pytest.approx(40.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            odds_ratio("50", 40, 10, 5)

class TestRiskRatio:

    def test_basic(self):
        assert risk_ratio(30, 200, 10, 200) == pytest.approx(3.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            risk_ratio("30", 200, 10, 200)

class TestBalancedAccuracyScalar:

    def test_basic(self):
        assert balanced_accuracy_scalar(50, 40, 10, 5) == pytest.approx(0.8545454545)

    def test_type_error(self):
        with pytest.raises(TypeError):
            balanced_accuracy_scalar("50", 40, 10, 5)

class TestNegativePredictiveValue:

    def test_basic(self):
        assert negative_predictive_value(40, 5) == pytest.approx(0.8888888889)

    def test_type_error(self):
        with pytest.raises(TypeError):
            negative_predictive_value("40", 5)

class TestFalseDiscoveryRate:

    def test_basic(self):
        assert false_discovery_rate(10, 50) == pytest.approx(0.1666666667)

    def test_type_error(self):
        with pytest.raises(TypeError):
            false_discovery_rate("10", 50)


# ── Physics / Engineering ────────────────────────────────────────────────────

class TestJaccardIndexScalar:

    def test_basic(self):
        assert jaccard_index_scalar(50, 10, 5) == pytest.approx(0.76923077)

    def test_zero_denom_raises(self):
        with pytest.raises(ValueError):
            jaccard_index_scalar(0, 0, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            jaccard_index_scalar("50", 10, 5)

class TestCosineSimilarityScalar:

    def test_orthogonal(self):
        assert cosine_similarity_scalar(1, 0, 0, 1) == pytest.approx(0.0)

    def test_parallel(self):
        assert cosine_similarity_scalar(3, 4, 3, 4) == pytest.approx(1.0)

    def test_general(self):
        assert cosine_similarity_scalar(3, 4, 1, 2) == pytest.approx(0.98387, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cosine_similarity_scalar("3", 4, 1, 2)

class TestRSquaredScalar:

    def test_basic(self):
        assert r_squared_scalar(20, 100) == pytest.approx(0.8)

    def test_zero_ss_tot_raises(self):
        with pytest.raises(ValueError):
            r_squared_scalar(20, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            r_squared_scalar("20", 100)

class TestMeanPercentageError:

    def test_basic(self):
        assert mean_percentage_error(100, 90) == pytest.approx(10.0)

    def test_overestimate(self):
        assert mean_percentage_error(100, 110) == pytest.approx(-10.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            mean_percentage_error("100", 90)

class TestSymmetricMape:

    def test_basic(self):
        assert symmetric_mape(100, 80) == pytest.approx(22.2222, rel=1e-3)

    def test_both_zero_raises(self):
        with pytest.raises(ValueError):
            symmetric_mape(0, 0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            symmetric_mape("100", 80)


# ── Physics / Engineering ────────────────────────────────────────────────────

class TestLogCoshLoss:

    def test_basic(self):
        assert log_cosh_loss(3, 5) == pytest.approx(1.3250, rel=1e-3)

    def test_zero_error(self):
        assert log_cosh_loss(5, 5) == pytest.approx(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            log_cosh_loss("3", 5)

class TestPoissonProbability:

    def test_basic(self):
        assert poisson_probability(3, 2.5) == pytest.approx(0.21376, rel=1e-3)

    def test_k_zero(self):
        assert poisson_probability(0, 1.0) == pytest.approx(math.exp(-1.0))

    def test_negative_k_raises(self):
        with pytest.raises(ValueError):
            poisson_probability(-1, 2.5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            poisson_probability(3.5, 2.5)

class TestEntropyBinary:

    def test_half(self):
        assert entropy_binary(0.5) == pytest.approx(1.0)

    def test_low_p(self):
        assert entropy_binary(0.1) == pytest.approx(0.46899, rel=1e-3)

    def test_boundary_raises(self):
        with pytest.raises(ValueError):
            entropy_binary(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            entropy_binary("0.5")

class TestGiniImpurityBinary:

    def test_half(self):
        assert gini_impurity_binary(0.5) == pytest.approx(0.5)

    def test_pure(self):
        assert gini_impurity_binary(0.0) == pytest.approx(0.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            gini_impurity_binary("0.5")

class TestCohensKappaScalar:

    def test_basic(self):
        assert cohens_kappa_scalar(50, 40, 10, 5) == pytest.approx(0.71233, rel=1e-3)

    def test_perfect_agreement(self):
        assert cohens_kappa_scalar(50, 50, 0, 0) == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cohens_kappa_scalar("50", 40, 10, 5)


# ── Physics / Engineering ────────────────────────────────────────────────────

class TestBinomialProbability:

    def test_basic(self):
        assert binomial_probability(10, 3, 0.5) == pytest.approx(0.117188, rel=1e-3)

    def test_certain(self):
        assert binomial_probability(5, 5, 1.0) == pytest.approx(1.0)

    def test_k_gt_n_raises(self):
        with pytest.raises(ValueError):
            binomial_probability(3, 5, 0.5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            binomial_probability(10.0, 3, 0.5)

class TestExponentialPdf:

    def test_basic(self):
        assert exponential_pdf(1, 2) == pytest.approx(0.27067, rel=1e-3)

    def test_at_zero(self):
        assert exponential_pdf(0, 2) == pytest.approx(2.0)

    def test_negative_x_raises(self):
        with pytest.raises(ValueError):
            exponential_pdf(-1, 2)

    def test_type_error(self):
        with pytest.raises(TypeError):
            exponential_pdf("1", 2)

class TestLogisticFunction:

    def test_midpoint(self):
        assert logistic_function(0) == pytest.approx(0.5)

    def test_large_positive(self):
        assert logistic_function(100) == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            logistic_function("0")

class TestCrossEntropyBinary:

    def test_basic(self):
        assert cross_entropy_binary(1, 0.9) == pytest.approx(0.10536, rel=1e-3)

    def test_bad_label_raises(self):
        with pytest.raises(ValueError):
            cross_entropy_binary(0.5, 0.9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cross_entropy_binary("1", 0.9)

class TestLaplacePdf:

    def test_at_mean(self):
        assert laplace_pdf(0) == pytest.approx(0.5)

    def test_away_from_mean(self):
        assert laplace_pdf(1, 0, 1) == pytest.approx(0.5 * math.exp(-1))

    def test_type_error(self):
        with pytest.raises(TypeError):
            laplace_pdf("0")


# ── Physics / Engineering ────────────────────────────────────────────────────

class TestCauchyPdf:
    def test_peak(self):
        assert cauchy_pdf(0) == pytest.approx(1 / math.pi, rel=1e-4)

    def test_shifted(self):
        assert cauchy_pdf(2, x0=2, gamma=1) == pytest.approx(1 / math.pi, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cauchy_pdf("a")

    def test_negative_gamma(self):
        with pytest.raises(ValueError):
            cauchy_pdf(0, gamma=-1)

class TestWeibullPdf:
    def test_basic(self):
        assert weibull_pdf(1, 1.5, 1) == pytest.approx(0.551819, rel=1e-4)

    def test_x_zero_k_gt_1(self):
        assert weibull_pdf(0, 2, 1) == 0.0

    def test_x_zero_k_eq_1(self):
        assert weibull_pdf(0, 1, 1) == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            weibull_pdf("a", 1, 1)

    def test_negative_x(self):
        with pytest.raises(ValueError):
            weibull_pdf(-1, 1, 1)

class TestRayleighPdf:
    def test_basic(self):
        assert rayleigh_pdf(1) == pytest.approx(0.606531, rel=1e-4)

    def test_zero(self):
        assert rayleigh_pdf(0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            rayleigh_pdf("a")

    def test_negative_sigma(self):
        with pytest.raises(ValueError):
            rayleigh_pdf(1, sigma=-1)

class TestGammaPdf:
    def test_basic(self):
        assert gamma_pdf(2, 2, 1) == pytest.approx(0.270671, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            gamma_pdf("a", 1, 1)

    def test_negative_x(self):
        with pytest.raises(ValueError):
            gamma_pdf(-1, 1, 1)

class TestBetaFunctionValue:
    def test_basic(self):
        assert beta_function_value(2, 3) == pytest.approx(0.083333, rel=1e-4)

    def test_symmetry(self):
        assert beta_function_value(3, 2) == pytest.approx(beta_function_value(2, 3))

    def test_type_error(self):
        with pytest.raises(TypeError):
            beta_function_value("a", 1)

    def test_negative_a(self):
        with pytest.raises(ValueError):
            beta_function_value(-1, 1)


# ---------------------------------------------------------------------------
# Physics / Engineering
# ---------------------------------------------------------------------------

class TestLogNormalPdf:
    def test_basic(self):
        assert log_normal_pdf(1) == pytest.approx(0.398942, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            log_normal_pdf("a")

    def test_negative_x(self):
        with pytest.raises(ValueError):
            log_normal_pdf(-1)

    def test_negative_sigma(self):
        with pytest.raises(ValueError):
            log_normal_pdf(1, sigma=-1)

class TestGeometricPdf:
    def test_basic(self):
        assert geometric_pdf(3, 0.5) == pytest.approx(0.125)

    def test_first_trial(self):
        assert geometric_pdf(1, 0.5) == pytest.approx(0.5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            geometric_pdf(1.5, 0.5)

    def test_invalid_p(self):
        with pytest.raises(ValueError):
            geometric_pdf(1, 0)

    def test_k_zero(self):
        with pytest.raises(ValueError):
            geometric_pdf(0, 0.5)

class TestParetoPdf:
    def test_basic(self):
        assert pareto_pdf(2, 1, 3) == pytest.approx(0.1875)

    def test_at_minimum(self):
        assert pareto_pdf(1, 1, 3) == pytest.approx(3.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            pareto_pdf("a", 1, 1)

    def test_x_below_xm(self):
        # New implementation returns 0.0 instead of raising
        assert pareto_pdf(0.5, 1, 1) == 0.0

class TestGumbelPdf:
    def test_basic(self):
        assert gumbel_pdf(0) == pytest.approx(0.367879, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            gumbel_pdf("a")

    def test_negative_beta(self):
        with pytest.raises(ValueError):
            gumbel_pdf(0, beta=-1)

class TestTriangularPdf:
    def test_at_mode(self):
        assert triangular_pdf(5, 0, 10, 5) == pytest.approx(0.2)

    def test_below_range(self):
        assert triangular_pdf(-1, 0, 10, 5) == 0.0

    def test_above_range(self):
        assert triangular_pdf(11, 0, 10, 5) == 0.0

    def test_left_of_mode(self):
        assert triangular_pdf(2, 0, 10, 5) == pytest.approx(2 * 2 / (10 * 5))

    def test_right_of_mode(self):
        assert triangular_pdf(8, 0, 10, 5) == pytest.approx(2 * 2 / (10 * 5))

    def test_type_error(self):
        with pytest.raises(TypeError):
            triangular_pdf("a", 0, 10, 5)

    def test_a_ge_b(self):
        with pytest.raises(ValueError):
            triangular_pdf(5, 10, 10, 10)


# ---------------------------------------------------------------------------
# Physics / Engineering
# ---------------------------------------------------------------------------

class TestHypergeometricPmf:
    def test_basic(self):
        assert hypergeometric_pmf(2, 52, 13, 5) == pytest.approx(0.27428, rel=1e-3)

    def test_zero_prob(self):
        assert hypergeometric_pmf(6, 52, 13, 5) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            hypergeometric_pmf(1.5, 52, 13, 5)

    def test_invalid_population(self):
        with pytest.raises(ValueError):
            hypergeometric_pmf(1, -1, 0, 0)

class TestNegativeBinomialPmf:
    def test_basic(self):
        assert negative_binomial_pmf(3, 2, 0.5) == pytest.approx(0.125)

    def test_zero_failures(self):
        assert negative_binomial_pmf(0, 1, 0.5) == pytest.approx(0.5)

    def test_type_error(self):
        with pytest.raises(TypeError):
            negative_binomial_pmf(1.5, 2, 0.5)

    def test_invalid_p(self):
        with pytest.raises(ValueError):
            negative_binomial_pmf(1, 1, 0)

class TestZipfPmf:
    def test_rank_1(self):
        assert zipf_pmf(1, 1, 10) == pytest.approx(0.341417, rel=1e-4)

    def test_rank_2(self):
        h10 = sum(1 / i for i in range(1, 11))
        assert zipf_pmf(2, 1, 10) == pytest.approx(0.5 / h10, rel=1e-4)

    def test_type_error(self):
        with pytest.raises(TypeError):
            zipf_pmf(1.5, 1, 10)

    def test_out_of_range(self):
        with pytest.raises(ValueError):
            zipf_pmf(11, 1, 10)

class TestErlangPdf:
    def test_basic(self):
        assert erlang_pdf(1, 2, 1) == pytest.approx(0.367879, rel=1e-4)

    def test_x_zero_k_1(self):
        assert erlang_pdf(0, 1, 2) == pytest.approx(2.0)

    def test_x_zero_k_gt_1(self):
        assert erlang_pdf(0, 2, 1) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            erlang_pdf("a", 1, 1)

    def test_negative_x(self):
        with pytest.raises(ValueError):
            erlang_pdf(-1, 1, 1)

class TestMaxwellBoltzmannPdf:
    def test_basic(self):
        assert maxwell_boltzmann_pdf(1, 1) == pytest.approx(0.483941, rel=1e-4)

    def test_zero_speed(self):
        assert maxwell_boltzmann_pdf(0, 1) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            maxwell_boltzmann_pdf("a", 1)

    def test_negative_a(self):
        with pytest.raises(ValueError):
            maxwell_boltzmann_pdf(1, -1)


# ---------------------------------------------------------------------------
# Physics / Engineering
# ---------------------------------------------------------------------------

class TestAnnuityDuePv:
    def test_basic(self):
        result = annuity_due_pv(1000, 0.05, 10)
        assert result == pytest.approx(8107.82, rel=1e-2)

    def test_zero_rate(self):
        assert annuity_due_pv(1000, 0.0, 5) == pytest.approx(5000.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            annuity_due_pv("a", 0.05, 10)


# ---------------------------------------------------------------------------
# fxNumeric — statistics_functions.py
# ---------------------------------------------------------------------------


class TestAndersonDarling:
    def test_uniform_ish(self):
        data = list(range(1, 9))
        result = anderson_darling(data)
        assert isinstance(result, float)

    def test_too_few(self):
        with pytest.raises(ValueError):
            anderson_darling([1])

    def test_type_error(self):
        with pytest.raises(TypeError):
            anderson_darling("abc")

class TestGrubbsTest:
    def test_basic(self):
        data = [1, 2, 3, 4, 5, 100]
        result = grubbs_test(data)
        assert result["outlier_value"] == 100
        assert result["position"] == "max"

    def test_too_few(self):
        with pytest.raises(ValueError):
            grubbs_test([1, 2])

    def test_type_error(self):
        with pytest.raises(TypeError):
            grubbs_test("abc")

class TestDixonQTest:
    def test_basic(self):
        data = [1, 2, 3, 4, 5, 100]
        result = dixon_q_test(data)
        assert "q_statistic" in result
        assert "suspect_value" in result

    def test_too_few(self):
        with pytest.raises(ValueError):
            dixon_q_test([1, 2])

    def test_type_error(self):
        with pytest.raises(TypeError):
            dixon_q_test("abc")

class TestShapiroWilkW:

    def test_normal_like(self):
        w = shapiro_wilk_w([1, 2, 3, 4, 5])
        assert 0.9 < w <= 1.0

    def test_too_few(self):

        with pytest.raises(ValueError):
            shapiro_wilk_w([1, 2])

class TestLjungBox:

    def test_alternating(self):
        data = [1, -1, 1, -1, 1, -1, 1, -1, 1, -1, 1, -1]
        q = ljung_box(data, 5)
        assert q > 0

    def test_too_short(self):

        with pytest.raises(ValueError):
            ljung_box([1, 2, 3], 5)

class TestMarkovChainSteadyState:

    def test_two_state(self):
        pi = markov_chain_steady_state([[0.9, 0.1], [0.5, 0.5]])
        assert round(pi[0], 4) == 0.8333
        assert round(pi[1], 4) == 0.1667

class TestBenfordDistribution:

    def test_basic(self):
        d = benford_distribution([1, 20, 300, 4000])
        assert d[1] == 0.25
        assert sum(d.values()) == pytest.approx(1.0)


# ── fxNumeric ── arithmetic_functions ───────────────────────────────────

class TestZScorePercentile:

    def test_z_to_p(self):
        assert round(z_score_to_percentile(0), 4) == 50.0

    def test_z_1_96(self):
        assert round(z_score_to_percentile(1.96), 1) == 97.5

    def test_p_to_z(self):
        assert round(percentile_to_z_score(0.975), 2) == 1.96

    def test_p_to_z_lower(self):
        assert round(percentile_to_z_score(0.025), 2) == -1.96

    def test_p_out_of_range(self):

        with pytest.raises(ValueError):
            percentile_to_z_score(0)

class TestBayesPosterior:

    def test_basic(self):
        assert bayes_posterior(0.01, 0.9, 0.05) == 0.18

    def test_zero_evidence(self):

        with pytest.raises(ValueError):
            bayes_posterior(0.5, 0.5, 0)


# ── fxNumeric ── conversion_functions ───────────────────────────────────

class TestMLActivations:
    """CELU, hard_sigmoid, hard_swish."""

    def test_celu_positive(self):
        from agentfx.fxNumeric.statistics_functions import celu

        assert celu(1.0) == 1.0

    def test_celu_negative(self):
        from agentfx.fxNumeric.statistics_functions import celu

        assert round(celu(-1.0, 1.0), 6) == -0.632121

    def test_celu_zero(self):
        from agentfx.fxNumeric.statistics_functions import celu

        assert celu(0.0) == 0.0

    def test_celu_invalid_alpha(self):
        from agentfx.fxNumeric.statistics_functions import celu

        with pytest.raises(ValueError):
            celu(1.0, alpha=0)

    def test_hard_sigmoid_center(self):
        from agentfx.fxNumeric.statistics_functions import hard_sigmoid

        assert hard_sigmoid(0.0) == 0.5

    def test_hard_sigmoid_saturated_high(self):
        from agentfx.fxNumeric.statistics_functions import hard_sigmoid

        assert hard_sigmoid(3.0) == 1.0

    def test_hard_sigmoid_saturated_low(self):
        from agentfx.fxNumeric.statistics_functions import hard_sigmoid

        assert hard_sigmoid(-3.0) == 0.0

    def test_hard_swish_zero(self):
        from agentfx.fxNumeric.statistics_functions import hard_swish

        assert hard_swish(0.0) == 0.0

    def test_hard_swish_positive(self):
        from agentfx.fxNumeric.statistics_functions import hard_swish

        assert hard_swish(3.0) == 3.0

    def test_hard_swish_negative(self):
        from agentfx.fxNumeric.statistics_functions import hard_swish

        assert round(hard_swish(-1.0), 6) == -0.333333


# =====================================================================
# fxNumeric — special_functions (Bernstein)
# =====================================================================

class TestLogisticFunctionV2:
    def test_midpoint(self):
        assert logistic_function(0) == 0.5

    def test_large_positive(self):
        assert logistic_function(100) == pytest.approx(1.0, abs=1e-10)

    def test_large_negative(self):
        assert logistic_function(-100) == pytest.approx(0.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            logistic_function("abc")

class TestGeometricPMF:
    def test_basic(self):
        assert round(geometric_pmf(3, 0.5), 4) == 0.125

    def test_first_trial(self):
        assert geometric_pmf(1, 0.5) == 0.5

    def test_invalid_k(self):
        with pytest.raises(ValueError):
            geometric_pmf(0, 0.5)

class TestHypergeometricPMF:
    def test_basic(self):
        assert round(hypergeometric_pmf(2, 52, 13, 5), 4) == 0.2743

    def test_impossible(self):
        # k > K → impossible
        assert hypergeometric_pmf(14, 52, 13, 15) == 0.0

class TestNegativeBinomialPMF:
    def test_basic(self):
        assert round(negative_binomial_pmf(3, 2, 0.5), 4) == 0.125

    def test_zero_failures(self):
        # k=0 → P = p^r
        assert negative_binomial_pmf(0, 2, 0.5) == pytest.approx(0.25)

class TestExponentialPDF:
    def test_basic(self):
        assert round(exponential_pdf(1.0, 1.0), 4) == 0.3679

    def test_zero(self):
        assert exponential_pdf(0.0, 1.0) == pytest.approx(1.0)

    def test_negative_x(self):
        with pytest.raises(ValueError):
            exponential_pdf(-1, 1.0)

class TestExponentialCDF:
    def test_basic(self):
        assert round(exponential_cdf(1.0, 1.0), 4) == 0.6321

    def test_zero(self):
        assert exponential_cdf(0.0, 1.0) == pytest.approx(0.0)

    def test_negative_lam(self):
        with pytest.raises(ValueError):
            exponential_cdf(1.0, -1)

class TestUniformPDF:
    def test_basic(self):
        assert uniform_pdf(0.5, 0.0, 1.0) == 1.0

    def test_outside(self):
        assert uniform_pdf(2.0, 0.0, 1.0) == 0.0

    def test_invalid_range(self):
        with pytest.raises(ValueError):
            uniform_pdf(0.5, 1.0, 0.0)

class TestUniformCDF:
    def test_midpoint(self):
        assert uniform_cdf(0.5, 0.0, 1.0) == 0.5

    def test_below(self):
        assert uniform_cdf(-1.0, 0.0, 1.0) == 0.0

    def test_above(self):
        assert uniform_cdf(2.0, 0.0, 1.0) == 1.0

class TestNormalCDF:
    def test_mean(self):
        assert round(normal_cdf(0.0), 4) == 0.5

    def test_one_sigma(self):
        assert round(normal_cdf(1.0), 4) == 0.8413

    def test_negative_sigma(self):
        with pytest.raises(ValueError):
            normal_cdf(0.0, 0.0, -1.0)

class TestLogNormalPDF:
    def test_basic(self):
        assert round(log_normal_pdf(1.0), 4) == 0.3989

    def test_negative_x(self):
        with pytest.raises(ValueError):
            log_normal_pdf(-1.0)

class TestChiSquaredPDF:
    def test_basic(self):
        assert round(chi_squared_pdf(2.0, 3), 4) == 0.2076

    def test_negative_x(self):
        with pytest.raises(ValueError):
            chi_squared_pdf(-1.0, 3)

class TestCauchyPDF:
    def test_center(self):
        assert round(cauchy_pdf(0.0), 4) == 0.3183

    def test_negative_gamma(self):
        with pytest.raises(ValueError):
            cauchy_pdf(0.0, 0.0, -1.0)

class TestBetaFunction:
    def test_basic(self):
        assert round(beta_function(2.0, 3.0), 4) == 0.0833

    def test_symmetric(self):
        assert beta_function(3.0, 2.0) == pytest.approx(beta_function(2.0, 3.0))

    def test_negative(self):
        with pytest.raises(ValueError):
            beta_function(-1, 3)

class TestWeibullPDF:
    def test_exponential(self):
        # k=1 → exponential
        assert round(weibull_pdf(1.0, 1.0, 1.0), 4) == 0.3679

    def test_negative_x(self):
        with pytest.raises(ValueError):
            weibull_pdf(-1.0, 1.0, 1.0)

class TestGammaPDF:
    def test_basic(self):
        assert round(gamma_pdf(1.0, 2.0, 1.0), 4) == 0.3679

    def test_negative_x(self):
        with pytest.raises(ValueError):
            gamma_pdf(-1.0, 2.0, 1.0)

class TestMultinomialCoefficient:
    def test_basic(self):
        assert multinomial_coefficient(2, 3, 4) == 1260

    def test_binomial(self):
        # C(5,2) = 10
        assert multinomial_coefficient(2, 3) == 10

    def test_single(self):
        assert multinomial_coefficient(5) == 1

    def test_negative(self):
        with pytest.raises(ValueError):
            multinomial_coefficient(-1, 2)

class TestLaplacePdfV2:
    def test_at_mean(self):
        assert round(laplace_pdf(0.0), 4) == 0.5

    def test_symmetric(self):
        assert laplace_pdf(-1.0) == pytest.approx(laplace_pdf(1.0))

    def test_custom_params(self):
        assert laplace_pdf(2.0, mu=2.0, b=0.5) == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            laplace_pdf("x")

    def test_value_error(self):
        with pytest.raises(ValueError):
            laplace_pdf(0.0, b=-1)

class TestLogisticPdf:
    def test_at_mean(self):
        assert round(logistic_pdf(0.0), 4) == 0.25

    def test_symmetric(self):
        assert logistic_pdf(-2.0) == pytest.approx(logistic_pdf(2.0))

    def test_type_error(self):
        with pytest.raises(TypeError):
            logistic_pdf("x")

    def test_value_error(self):
        with pytest.raises(ValueError):
            logistic_pdf(0.0, s=0)

class TestLogisticCdf:
    def test_at_mean(self):
        assert logistic_cdf(0.0) == 0.5

    def test_large_positive(self):
        assert logistic_cdf(100.0) == pytest.approx(1.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            logistic_cdf("x")

class TestTriangularPdfV2:
    def test_at_mode(self):
        assert round(triangular_pdf(0.5, 0.0, 1.0, 0.5), 4) == 2.0

    def test_outside_range(self):
        assert triangular_pdf(-1.0, 0.0, 1.0, 0.5) == 0.0

    def test_at_lower(self):
        assert triangular_pdf(0.0, 0.0, 1.0, 0.5) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            triangular_pdf("x", 0, 1, 0.5)

    def test_invalid_range(self):
        with pytest.raises(ValueError):
            triangular_pdf(0.5, 1.0, 0.0, 0.5)

class TestParetoPdfV2:
    def test_basic(self):
        assert round(pareto_pdf(2.0, 1.0, 3.0), 4) == 0.1875

    def test_at_min(self):
        assert pareto_pdf(1.0, 1.0, 2.0) == pytest.approx(2.0)

    def test_below_min(self):
        assert pareto_pdf(0.5, 1.0, 2.0) == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            pareto_pdf("x", 1, 2)

    def test_value_error(self):
        with pytest.raises(ValueError):
            pareto_pdf(1.0, -1.0, 2.0)


# ── String Operations ────────────────────────────────────────────────────

class TestWinsorizedMean:
    """Tests for winsorized_mean."""

    def test_basic(self):
        assert winsorized_mean([1, 2, 3, 4, 100], 0.2) == 3.0

    def test_no_winsorization(self):
        data = [1, 2, 3, 4, 5]
        assert winsorized_mean(data, 0.0) == pytest.approx(3.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            winsorized_mean("bad", 0.1)

    def test_value_error(self):
        with pytest.raises(ValueError):
            winsorized_mean([1], 0.1)

class TestTrimmedVariance:
    """Tests for trimmed_variance."""

    def test_basic(self):
        assert round(trimmed_variance([1, 2, 3, 4, 5, 6, 7, 8, 9, 100], 0.1), 4) == 6.0

    def test_no_trim(self):
        data = [1, 2, 3, 4, 5]
        result = trimmed_variance(data, 0.0)
        expected = sum((x - 3) ** 2 for x in data) / 4
        assert result == pytest.approx(expected, rel=1e-9)

class TestMedianAbsoluteDeviationV2:
    """Tests for median_absolute_deviation."""

    def test_basic(self):
        assert median_absolute_deviation([1, 2, 3, 4, 5]) == 1.0

    def test_single_value(self):
        assert median_absolute_deviation([5]) == 0.0

    def test_value_error_empty(self):
        with pytest.raises(ValueError):
            median_absolute_deviation([])

class TestCoefficientOfVariationV2:
    """Tests for coefficient_of_variation."""

    def test_basic(self):
        assert round(coefficient_of_variation([2, 4, 4, 4, 5, 5, 7, 9]), 4) == 0.4276

    def test_value_error_zero_mean(self):
        with pytest.raises(ValueError):
            coefficient_of_variation([-1, 1])

class TestQuartileDeviation:
    """Tests for quartile_deviation."""

    def test_basic(self):
        assert quartile_deviation([1, 2, 3, 4, 5, 6, 7, 8]) == 1.75

    def test_value_error(self):
        with pytest.raises(ValueError):
            quartile_deviation([1, 2, 3])

class TestBowleySkewness:
    """Tests for bowley_skewness."""

    def test_symmetric(self):
        assert round(bowley_skewness([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), 4) == 0.0

    def test_range(self):
        result = bowley_skewness([1, 1, 1, 2, 3, 5, 8, 13])
        assert -1 <= result <= 1

class TestMoorsKurtosis:
    """Tests for moors_kurtosis."""

    def test_uniform(self):
        assert round(moors_kurtosis(list(range(1, 101))), 2) == 1.0

    def test_value_error(self):
        with pytest.raises(ValueError):
            moors_kurtosis([1, 2, 3])

class TestCohensD:
    """Tests for cohens_d."""

    def test_basic(self):
        assert round(cohens_d([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), 4) == -1.2649

    def test_same_groups(self):
        assert cohens_d([1, 2, 3], [1, 2, 3]) == pytest.approx(0.0, abs=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            cohens_d("bad", [1, 2])

class TestHedgesG:
    """Tests for hedges_g."""

    def test_basic(self):
        assert round(hedges_g([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), 4) == -1.1425

    def test_smaller_than_d(self):
        """Hedges' g should be closer to zero than Cohen's d."""
        d = abs(cohens_d([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
        g = abs(hedges_g([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]))
        assert g <= d

class TestGlassDelta:
    """Tests for glass_delta."""

    def test_basic(self):
        assert round(glass_delta([3, 4, 5, 6, 7], [1, 2, 3, 4, 5]), 4) == 1.2649

    def test_type_error(self):
        with pytest.raises(TypeError):
            glass_delta("bad", [1, 2, 3])

class TestRSquaredV2:
    """Tests for r_squared."""

    def test_basic(self):
        assert round(r_squared([1, 2, 3, 4, 5], [1.1, 2.0, 2.9, 4.1, 5.0]), 3) == 0.997

    def test_perfect_fit(self):
        assert r_squared([1, 2, 3], [1, 2, 3]) == pytest.approx(1.0, rel=1e-9)

    def test_type_error(self):
        with pytest.raises(TypeError):
            r_squared("bad", [1, 2])

class TestAdjustedRSquared:
    """Tests for adjusted_r_squared."""

    def test_basic(self):
        assert round(adjusted_r_squared(0.997, 5, 1), 3) == 0.996

    def test_lower_than_r2(self):
        assert adjusted_r_squared(0.9, 20, 3) < 0.9

    def test_value_error(self):
        with pytest.raises(ValueError):
            adjusted_r_squared(0.9, 3, 3)

class TestResidualStandardError:
    """Tests for residual_standard_error."""

    def test_basic(self):
        assert round(residual_standard_error([1, 2, 3, 4, 5], [1.1, 2.0, 2.9, 4.1, 5.0], 1), 1) == 0.1

    def test_perfect_fit(self):
        assert residual_standard_error([1, 2, 3, 4, 5], [1, 2, 3, 4, 5], 1) == pytest.approx(0.0, abs=1e-9)

class TestMeanAbsoluteErrorV2:
    """Tests for mean_absolute_error."""

    def test_basic(self):
        assert mean_absolute_error([1, 2, 3], [1.5, 2.5, 3.5]) == 0.5

    def test_perfect(self):
        assert mean_absolute_error([1, 2, 3], [1, 2, 3]) == 0.0

    def test_value_error(self):
        with pytest.raises(ValueError):
            mean_absolute_error([1], [1, 2])

class TestMeanAbsolutePercentageError:
    """Tests for mean_absolute_percentage_error."""

    def test_basic(self):
        assert round(mean_absolute_percentage_error([100, 200, 300], [110, 190, 280]), 2) == 7.22

    def test_value_error_zero_observed(self):
        with pytest.raises(ValueError):
            mean_absolute_percentage_error([0, 1], [1, 1])

class TestRootMeanSquaredLogError:
    """Tests for root_mean_squared_log_error."""

    def test_basic(self):
        assert round(root_mean_squared_log_error([3, 5, 2.5], [2.5, 5, 4]), 4) == 0.2199

    def test_perfect(self):
        assert root_mean_squared_log_error([1, 2, 3], [1, 2, 3]) == pytest.approx(0.0, abs=1e-9)

class TestZScore:
    """Tests for z_score."""

    def test_basic(self):
        assert z_score(85, 70, 10) == 1.5

    def test_negative(self):
        assert z_score(60, 70, 10) == -1.0

    def test_value_error(self):
        with pytest.raises(ValueError):
            z_score(85, 70, 0)

class TestZScoreToPercentile:
    """Tests for z_score_to_percentile."""

    def test_basic(self):
        assert round(z_score_to_percentile(1.96), 1) == 97.5

    def test_zero(self):
        assert z_score_to_percentile(0) == pytest.approx(50.0, abs=0.1)

    def test_type_error(self):
        with pytest.raises(TypeError):
            z_score_to_percentile("bad")

class TestPercentileRank:
    """Tests for percentile_rank."""

    def test_basic(self):
        assert percentile_rank([1, 2, 3, 4, 5], 3) == 60.0

    def test_below_all(self):
        assert percentile_rank([1, 2, 3], 0) == 0.0

    def test_above_all(self):
        assert percentile_rank([1, 2, 3], 10) == 100.0

class TestPointBiserialCorrelation:
    """Tests for point_biserial_correlation."""

    def test_basic(self):
        assert round(point_biserial_correlation([0, 0, 1, 1], [10, 12, 20, 22]), 4) == 0.8492

    def test_range(self):
        result = point_biserial_correlation([0, 0, 1, 1], [10, 12, 20, 22])
        assert -1 <= result <= 1

    def test_type_error(self):
        with pytest.raises(TypeError):
            point_biserial_correlation([0, 0.5, 1, 1], [10, 12, 20, 22])

class TestShannonEntropy:
    """Tests for shannon_entropy."""

    def test_uniform_binary(self):
        assert shannon_entropy([0.5, 0.5]) == pytest.approx(1.0, rel=1e-9)

    def test_certain(self):
        assert shannon_entropy([1.0]) == pytest.approx(0.0, abs=1e-9)

    def test_value_error_empty(self):
        with pytest.raises(ValueError):
            shannon_entropy([])

class TestCrossEntropy:
    """Tests for cross_entropy."""

    def test_basic(self):
        assert round(cross_entropy([0.5, 0.5], [0.6, 0.4]), 4) == 1.0294

    def test_same_distributions(self):
        """Cross entropy equals Shannon entropy when P == Q."""
        h = shannon_entropy([0.5, 0.5])
        ce = cross_entropy([0.5, 0.5], [0.5, 0.5])
        assert ce == pytest.approx(h, rel=1e-9)

class TestKLDivergence:
    """Tests for kl_divergence."""

    def test_basic(self):
        assert round(kl_divergence([0.5, 0.5], [0.6, 0.4]), 4) == 0.0294

    def test_zero_when_same(self):
        assert kl_divergence([0.5, 0.5], [0.5, 0.5]) == pytest.approx(0.0, abs=1e-9)

    def test_non_negative(self):
        assert kl_divergence([0.3, 0.7], [0.6, 0.4]) >= 0

class TestJSDivergence:
    """Tests for js_divergence."""

    def test_basic(self):
        assert round(js_divergence([0.5, 0.5], [0.6, 0.4]), 4) == 0.0073

    def test_zero_when_same(self):
        assert js_divergence([0.5, 0.5], [0.5, 0.5]) == pytest.approx(0.0, abs=1e-9)

    def test_symmetric(self):
        jsd1 = js_divergence([0.3, 0.7], [0.6, 0.4])
        jsd2 = js_divergence([0.6, 0.4], [0.3, 0.7])
        assert jsd1 == pytest.approx(jsd2, rel=1e-9)

class TestMutualInformation:
    """Tests for mutual_information."""

    def test_independent(self):
        assert mutual_information([[0.25, 0.25], [0.25, 0.25]]) == pytest.approx(0.0, abs=1e-9)

    def test_dependent(self):
        result = mutual_information([[0.5, 0.0001], [0.0001, 0.4998]])
        assert result > 0

class TestMahalanobisDistance1D:
    """Tests for mahalanobis_distance_1d."""

    def test_basic(self):
        assert round(mahalanobis_distance_1d(10, [2, 4, 4, 4, 5, 5, 7, 9]), 4) == 2.3385

    def test_at_mean(self):
        data = [1, 2, 3, 4, 5]
        assert mahalanobis_distance_1d(3.0, data) == pytest.approx(0.0, abs=1e-9)

class TestCosineSimilarity:
    """Tests for cosine_similarity."""

    def test_basic(self):
        assert round(cosine_similarity([1, 2, 3], [4, 5, 6]), 4) == 0.9746

    def test_identical(self):
        assert cosine_similarity([1, 0], [1, 0]) == pytest.approx(1.0, rel=1e-9)

    def test_orthogonal(self):
        assert cosine_similarity([1, 0], [0, 1]) == pytest.approx(0.0, abs=1e-9)

class TestEuclideanDistance:
    """Tests for euclidean_distance."""

    def test_basic(self):
        assert round(euclidean_distance([1, 2, 3], [4, 5, 6]), 4) == 5.1962

    def test_same_point(self):
        assert euclidean_distance([1, 2], [1, 2]) == pytest.approx(0.0, abs=1e-9)

class TestManhattanDistance:
    """Tests for manhattan_distance."""

    def test_basic(self):
        assert manhattan_distance([1, 2, 3], [4, 5, 6]) == 9.0

    def test_same_point(self):
        assert manhattan_distance([1, 2], [1, 2]) == pytest.approx(0.0, abs=1e-9)

    def test_value_error(self):
        with pytest.raises(ValueError):
            manhattan_distance([1], [1, 2])

class TestSimpleMovingAverage:
    """Tests for simple_moving_average."""

    def test_basic(self):
        assert simple_moving_average([1, 2, 3, 4, 5], 3) == [2.0, 3.0, 4.0]

    def test_window_1(self):
        assert simple_moving_average([10, 20, 30], 1) == [10.0, 20.0, 30.0]

    def test_value_error(self):
        with pytest.raises(ValueError):
            simple_moving_average([1, 2], 3)

class TestExponentialMovingAverage:
    """Tests for exponential_moving_average."""

    def test_basic(self):
        result = [round(v, 2) for v in exponential_moving_average([1, 2, 3, 4, 5], 0.5)]
        assert result == [1.0, 1.5, 2.25, 3.12, 4.06]

    def test_alpha_1(self):
        """Alpha=1 returns data itself."""
        assert exponential_moving_average([1, 2, 3], 1.0) == [1.0, 2.0, 3.0]

class TestWeightedMovingAverage:
    """Tests for weighted_moving_average."""

    def test_basic(self):
        result = [round(v, 4) for v in weighted_moving_average([1, 2, 3, 4, 5], [1, 2, 3])]
        assert result == [2.3333, 3.3333, 4.3333]

class TestCumulativeMovingAverage:
    """Tests for cumulative_moving_average."""

    def test_basic(self):
        assert cumulative_moving_average([1, 2, 3, 4, 5]) == [1.0, 1.5, 2.0, 2.5, 3.0]

    def test_value_error(self):
        with pytest.raises(ValueError):
            cumulative_moving_average([])

class TestAutocorrelation:
    """Tests for autocorrelation."""

    def test_basic(self):
        assert round(autocorrelation([1, 2, 3, 4, 5, 4, 3, 2, 1], 1), 4) == 0.5397

    def test_lag_gt_data(self):
        with pytest.raises(ValueError):
            autocorrelation([1, 2, 3], 3)

class TestPartialAutocorrelation:
    """Tests for partial_autocorrelation."""

    def test_basic(self):
        result = [round(v, 2) for v in partial_autocorrelation([1, 2, 3, 4, 5, 4, 3, 2, 1], 2)]
        assert result == [0.54, -0.43]

class TestHoltLinearForecast:
    """Tests for holt_linear_forecast."""

    def test_basic(self):
        result = [round(v, 2) for v in holt_linear_forecast([1, 2, 3, 4, 5], 0.8, 0.2, 3)]
        assert result == [6.0, 7.0, 8.0]

    def test_single_step(self):
        result = holt_linear_forecast([10, 20, 30], 0.5, 0.5, 1)
        assert len(result) == 1

class TestRunningMax:
    """Tests for running_max."""

    def test_basic(self):
        assert running_max([1, 3, 2, 5, 4], 3) == [3.0, 5.0, 5.0]

class TestRunningMin:
    """Tests for running_min."""

    def test_basic(self):
        assert running_min([1, 3, 2, 5, 4], 3) == [1.0, 2.0, 2.0]

class TestRunningStd:
    """Tests for running_std."""

    def test_basic(self):
        result = [round(v, 4) for v in running_std([1, 2, 3, 4, 5], 3)]
        assert result == [1.0, 1.0, 1.0]

    def test_value_error(self):
        with pytest.raises(ValueError):
            running_std([1, 2, 3], 1)

class TestBayesTheorem:
    """Tests for bayes_theorem."""

    def test_basic(self):
        assert round(bayes_theorem(0.01, 0.9, 0.05), 4) == 0.18

    def test_type_error(self):
        with pytest.raises(TypeError):
            bayes_theorem("bad", 0.9, 0.05)

    def test_value_error(self):
        with pytest.raises(ValueError):
            bayes_theorem(0, 0.9, 0.05)

class TestBayesianUpdateV2:
    """Tests for bayesian_update."""

    def test_basic(self):
        assert round(bayesian_update(0.5, [0.8, 0.9], [0.5, 0.6]), 4) == 1.2

    def test_single_update(self):
        result = bayesian_update(0.5, [0.8], [0.5])
        assert result == pytest.approx(bayes_theorem(0.5, 0.8, 0.5), rel=1e-9)

class TestChiSquaredStatisticV2:
    """Tests for chi_squared_statistic."""

    def test_basic(self):
        assert round(chi_squared_statistic([10, 20, 30], [15, 15, 30]), 4) == 3.3333

    def test_perfect_fit(self):
        assert chi_squared_statistic([10, 20], [10, 20]) == pytest.approx(0.0, abs=1e-9)

    def test_value_error(self):
        with pytest.raises(ValueError):
            chi_squared_statistic([10], [0])

class TestCramersV:
    """Tests for cramers_v."""

    def test_basic(self):
        assert round(cramers_v(10.0, 100, 3), 4) == 0.2236

    def test_zero_chi2(self):
        assert cramers_v(0, 100, 3) == 0.0

    def test_value_error(self):
        with pytest.raises(ValueError):
            cramers_v(10, 100, 1)

class TestNormalPdf:
    """Tests for normal_pdf."""

    def test_standard(self):
        assert round(normal_pdf(0), 4) == 0.3989

    def test_symmetric(self):
        assert normal_pdf(1) == pytest.approx(normal_pdf(-1), rel=1e-9)

    def test_value_error(self):
        with pytest.raises(ValueError):
            normal_pdf(0, sigma=0)

class TestNormalCdf:
    """Tests for normal_cdf."""

    def test_196(self):
        assert round(normal_cdf(1.96), 3) == 0.975

    def test_zero(self):
        assert normal_cdf(0) == pytest.approx(0.5, rel=1e-6)

class TestExponentialPdfV2:
    """Tests for exponential_pdf."""

    def test_basic(self):
        assert round(exponential_pdf(1, 2), 4) == 0.2707

    def test_at_zero(self):
        assert exponential_pdf(0, 2) == pytest.approx(2.0, rel=1e-9)

class TestExponentialCdf:
    """Tests for exponential_cdf."""

    def test_basic(self):
        assert round(exponential_cdf(1, 2), 4) == 0.8647

    def test_at_zero(self):
        assert exponential_cdf(0, 2) == pytest.approx(0.0, abs=1e-9)

class TestPoissonPmf:
    """Tests for poisson_pmf."""

    def test_basic(self):
        assert round(poisson_pmf(3, 2.5), 4) == 0.2138

    def test_zero_events(self):
        assert poisson_pmf(0, 1) == pytest.approx(math.exp(-1), rel=1e-9)

    def test_value_error(self):
        with pytest.raises(ValueError):
            poisson_pmf(-1, 2)

class TestBinomialPmf:
    """Tests for binomial_pmf."""

    def test_basic(self):
        assert round(binomial_pmf(3, 10, 0.5), 4) == 0.1172

    def test_certain(self):
        assert binomial_pmf(10, 10, 1.0) == pytest.approx(1.0, rel=1e-9)

    def test_impossible(self):
        assert binomial_pmf(0, 10, 0.0) == pytest.approx(1.0, rel=1e-9)

class TestPurchasingPower:

    def test_basic(self):
        assert round(purchasing_power(1000, 0.03, 10), 2) == 737.42

    def test_zero_rate(self):
        assert purchasing_power(1000, 0, 5) == 1000.0


# ---------------------------------------------------------------------------
# fxNumeric — statistics_functions.py
# ---------------------------------------------------------------------------


class TestSigmoid:

    def test_zero(self):
        assert sigmoid(0) == 0.5

    def test_large_positive(self):
        assert sigmoid(100) == pytest.approx(1.0)

    def test_large_negative(self):
        assert sigmoid(-100) == pytest.approx(0.0, abs=1e-10)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sigmoid("x")

class TestLogit:

    def test_half(self):
        assert logit(0.5) == 0.0

    def test_boundary_low(self):
        with pytest.raises(ValueError):
            logit(0)

    def test_boundary_high(self):
        with pytest.raises(ValueError):
            logit(1)

    def test_inverse_of_sigmoid(self):
        assert logit(sigmoid(2.5)) == pytest.approx(2.5)

class TestCostOfDebtAfterTax:

    def test_basic(self):
        result = cost_of_debt_after_tax(0.06, 0.30)
        assert abs(result - 0.042) < 1e-9

    def test_zero_tax(self):
        assert cost_of_debt_after_tax(0.06, 0.0) == 0.06

    def test_type_error(self):
        with pytest.raises(TypeError):
            cost_of_debt_after_tax("0.06", 0.30)


# ── fxNumeric · statistics_functions ──────────────────────────────────────


class TestQuartileDeviationV2:

    def test_basic(self):
        result = quartile_deviation([1, 2, 3, 4, 5, 6, 7, 8])
        assert isinstance(result, float)
        assert result > 0

    def test_uniform(self):
        result = quartile_deviation([1, 1, 1, 1])
        assert result == 0.0

    def test_too_short(self):
        with pytest.raises(ValueError):
            quartile_deviation([1])

    def test_type_error(self):
        with pytest.raises(TypeError):
            quartile_deviation("abc")

class TestBowleySkewnessV2:

    def test_symmetric(self):
        result = bowley_skewness([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        assert abs(result) < 0.01

    def test_skewed(self):
        result = bowley_skewness([1, 1, 1, 2, 5, 10, 20, 50])
        assert isinstance(result, float)

    def test_too_short(self):
        with pytest.raises(ValueError):
            bowley_skewness([1, 2, 3])

    def test_equal_quartiles(self):
        with pytest.raises(ValueError):
            bowley_skewness([5, 5, 5, 5, 5, 5])

class TestCoefficientOfQuartileDeviation:

    def test_basic(self):
        result = coefficient_of_quartile_deviation([2, 4, 6, 8, 10])
        assert isinstance(result, float)
        assert 0 <= result <= 1

    def test_too_short(self):
        with pytest.raises(ValueError):
            coefficient_of_quartile_deviation([1])

    def test_type_error(self):
        with pytest.raises(TypeError):
            coefficient_of_quartile_deviation("abc")


# ── fxNumeric · number_theory_functions ───────────────────────────────────


class TestConvexityAdjustment:

    def test_basic(self):
        result = convexity_adjustment(150.0, 0.01)
        assert abs(result - 0.0075) < 1e-8

    def test_zero_yield(self):
        result = convexity_adjustment(150.0, 0.0)
        assert result == 0.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            convexity_adjustment("150", 0.01)


# ── fxNumeric · statistics_functions ─────────────────────────────────


class TestTukeyTrimean:

    def test_symmetric(self):
        assert tukey_trimean([1, 2, 3, 4, 5]) == 3.0

    def test_single_value_raises(self):
        with pytest.raises(ValueError):
            tukey_trimean([1, 2])

    def test_type_error(self):
        with pytest.raises(TypeError):
            tukey_trimean("not_a_list")

class TestMidrange:

    def test_basic(self):
        assert midrange([2, 4, 6, 8, 10]) == 6.0

    def test_single_element(self):
        assert midrange([5]) == 5.0

    def test_negative_values(self):
        assert midrange([-10, 10]) == 0.0

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            midrange([])

    def test_type_error(self):
        with pytest.raises(TypeError):
            midrange("abc")

class TestMidhinge:

    def test_basic(self):
        result = midhinge([1, 2, 3, 4, 5])
        assert result == 3.0

    def test_type_error(self):
        with pytest.raises(TypeError):
            midhinge("not_a_list")

class TestCosineimilarity:

    def test_identical_vectors(self):
        from agentfx.fxNumeric.statistics_functions import cosine_similarity
        assert cosine_similarity([1, 2, 3], [1, 2, 3]) == pytest.approx(1.0)

    def test_orthogonal_vectors(self):
        from agentfx.fxNumeric.statistics_functions import cosine_similarity
        assert cosine_similarity([1, 0], [0, 1]) == pytest.approx(0.0)

    def test_opposite_vectors(self):
        from agentfx.fxNumeric.statistics_functions import cosine_similarity
        assert cosine_similarity([1, 0], [-1, 0]) == pytest.approx(-1.0)

    def test_typical(self):
        from agentfx.fxNumeric.statistics_functions import cosine_similarity
        result = cosine_similarity([1, 2, 3], [4, 5, 6])
        assert result == pytest.approx(0.9746318461970762, rel=1e-6)

    def test_zero_vector_raises(self):
        from agentfx.fxNumeric.statistics_functions import cosine_similarity
        with pytest.raises(ValueError):
            cosine_similarity([0, 0, 0], [1, 2, 3])

    def test_different_lengths_raises(self):
        from agentfx.fxNumeric.statistics_functions import cosine_similarity
        with pytest.raises(ValueError):
            cosine_similarity([1, 2], [1, 2, 3])

class TestEuclideanDistanceV2:

    def test_same_point(self):
        from agentfx.fxNumeric.statistics_functions import euclidean_distance
        assert euclidean_distance([0, 0], [0, 0]) == 0.0

    def test_3d(self):
        from agentfx.fxNumeric.statistics_functions import euclidean_distance
        assert euclidean_distance([1, 2, 3], [4, 6, 3]) == pytest.approx(5.0)

    def test_2d_345(self):
        from agentfx.fxNumeric.statistics_functions import euclidean_distance
        assert euclidean_distance([0, 0], [3, 4]) == pytest.approx(5.0)

class TestManhattanDistanceV2:

    def test_typical(self):
        from agentfx.fxNumeric.statistics_functions import manhattan_distance
        assert manhattan_distance([1, 2, 3], [4, 6, 3]) == 7

    def test_same_point(self):
        from agentfx.fxNumeric.statistics_functions import manhattan_distance
        assert manhattan_distance([5, 5], [5, 5]) == 0

class TestMinkowskiDistance:

    def test_p1_is_manhattan(self):
        from agentfx.fxNumeric.statistics_functions import minkowski_distance
        result = minkowski_distance([1, 2, 3], [4, 6, 3], 1)
        assert result == pytest.approx(7.0)

    def test_p2_is_euclidean(self):
        from agentfx.fxNumeric.statistics_functions import minkowski_distance
        result = minkowski_distance([1, 2, 3], [4, 6, 3], 2)
        assert result == pytest.approx(5.0)

    def test_p3(self):
        from agentfx.fxNumeric.statistics_functions import minkowski_distance
        result = minkowski_distance([1, 2, 3], [4, 6, 3], 3)
        assert result == pytest.approx(4.4979, rel=1e-3)

    def test_p_less_than_1_raises(self):
        from agentfx.fxNumeric.statistics_functions import minkowski_distance
        with pytest.raises(ValueError):
            minkowski_distance([1], [2], 0.5)

class TestJaccardSimilarity:

    def test_overlap(self):
        from agentfx.fxNumeric.statistics_functions import jaccard_similarity
        assert jaccard_similarity([1, 2, 3], [2, 3, 4]) == pytest.approx(0.5)

    def test_identical(self):
        from agentfx.fxNumeric.statistics_functions import jaccard_similarity
        assert jaccard_similarity([1, 2, 3], [1, 2, 3]) == pytest.approx(1.0)

    def test_disjoint(self):
        from agentfx.fxNumeric.statistics_functions import jaccard_similarity
        assert jaccard_similarity([1, 2], [3, 4]) == pytest.approx(0.0)

    def test_both_empty(self):
        from agentfx.fxNumeric.statistics_functions import jaccard_similarity
        assert jaccard_similarity([], []) == pytest.approx(1.0)

class TestCramersVV2:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import cramers_v
        result = cramers_v(10.0, 100, 3)
        assert result == pytest.approx(0.2236, rel=1e-2)

    def test_perfect_association(self):
        from agentfx.fxNumeric.statistics_functions import cramers_v
        result = cramers_v(100.0, 100, 2)
        assert result == pytest.approx(1.0)

    def test_too_small_table_raises(self):
        from agentfx.fxNumeric.statistics_functions import cramers_v
        with pytest.raises(ValueError):
            cramers_v(10.0, 100, 1)

class TestPointBiserialCorrelationV2:

    def test_positive(self):
        from agentfx.fxNumeric.statistics_functions import point_biserial_correlation
        result = point_biserial_correlation([0, 0, 1, 1], [10, 12, 20, 22])
        assert result == pytest.approx(0.8492, rel=1e-2)

    def test_all_same_binary_raises(self):
        from agentfx.fxNumeric.statistics_functions import point_biserial_correlation
        with pytest.raises(ValueError):
            point_biserial_correlation([1, 1, 1], [1, 2, 3])


# ── Trigonometry ────────────────────────────────────────────────────────────

class TestKlDivergence:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import kl_divergence
        result = kl_divergence([0.4, 0.6], [0.5, 0.5])
        assert round(result, 3) == 0.029

    def test_identical(self):
        from agentfx.fxNumeric.statistics_functions import kl_divergence
        result = kl_divergence([0.5, 0.5], [0.5, 0.5])
        assert abs(result) < 1e-10

class TestCrossEntropyV2:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import cross_entropy
        result = cross_entropy([0.4, 0.6], [0.5, 0.5])
        assert round(result, 4) == 1.0

class TestRollingCorrelation:

    def test_perfect(self):
        from agentfx.fxNumeric.statistics_functions import rolling_correlation
        result = rolling_correlation([1, 2, 3, 4, 5], [2, 4, 6, 8, 10], 3)
        assert result[0] is None
        assert result[1] is None
        assert round(result[2], 4) == 1.0

class TestCumulativeReturn:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import cumulative_return
        result = cumulative_return([0.05, -0.02, 0.03])
        assert round(result, 5) == 0.05987

    def test_empty(self):
        from agentfx.fxNumeric.statistics_functions import cumulative_return

        with pytest.raises(ValueError):
            cumulative_return([])

class TestMaxDrawdown:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import max_drawdown
        result = max_drawdown([100, 120, 90, 110, 80])
        assert round(result, 4) == round(1 - 80 / 120, 4)

    def test_monotonic_up(self):
        from agentfx.fxNumeric.statistics_functions import max_drawdown
        result = max_drawdown([100, 110, 120, 130])
        assert result == 0.0


# ============================================================================
# ARITHMETIC CORE
# ============================================================================

class TestZToPercentile:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import z_to_percentile
        assert round(z_to_percentile(1.96), 2) == 97.5

    def test_zero(self):
        from agentfx.fxNumeric.statistics_functions import z_to_percentile
        assert z_to_percentile(0) == 50.0

    def test_negative(self):
        from agentfx.fxNumeric.statistics_functions import z_to_percentile
        assert round(z_to_percentile(-1.96), 2) == 2.5

class TestPercentileToZ:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import percentile_to_z
        assert round(percentile_to_z(97.5), 2) == 1.96

    def test_median(self):
        from agentfx.fxNumeric.statistics_functions import percentile_to_z
        assert round(percentile_to_z(50), 2) == 0.0

    def test_out_of_range(self):
        from agentfx.fxNumeric.statistics_functions import percentile_to_z
        with pytest.raises(ValueError):
            percentile_to_z(0)

    def test_out_of_range_100(self):
        from agentfx.fxNumeric.statistics_functions import percentile_to_z
        with pytest.raises(ValueError):
            percentile_to_z(100)

class TestCohensDV2:

    def test_medium_effect(self):
        from agentfx.fxNumeric.statistics_functions import cohens_d
        assert round(cohens_d([1, 2, 3, 4, 5], [3, 4, 5, 6, 7]), 4) == -1.2649

    def test_zero_diff(self):
        from agentfx.fxNumeric.statistics_functions import cohens_d
        assert cohens_d([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]) == 0.0

    def test_small_n(self):
        from agentfx.fxNumeric.statistics_functions import cohens_d
        with pytest.raises(ValueError):
            cohens_d([1], [1, 2, 3])


# =====================================================================
# Date Operations
# =====================================================================

class TestSigmoidV2:

    def test_zero(self):
        assert sigmoid(0) == 0.5

    def test_large_positive(self):
        assert sigmoid(100) == pytest.approx(1.0, abs=1e-10)

    def test_large_negative(self):
        assert sigmoid(-100) == pytest.approx(0.0, abs=1e-10)

    def test_symmetry(self):
        assert sigmoid(2) + sigmoid(-2) == pytest.approx(1.0)

    def test_type_error(self):
        with pytest.raises(TypeError):
            sigmoid("0")


# ──────────────────────────────────────────────
# Statistics/ML: relu
# ──────────────────────────────────────────────

class TestRelu:

    def test_negative(self):
        assert relu(-3) == 0

    def test_positive(self):
        assert relu(5) == 5

    def test_zero(self):
        assert relu(0) == 0

    def test_float(self):
        assert relu(-0.5) == 0
        assert relu(2.7) == 2.7


# ──────────────────────────────────────────────
# Statistics/ML: softplus
# ──────────────────────────────────────────────

class TestSoftplus:

    def test_zero(self):
        assert round(softplus(0), 4) == 0.6931

    def test_large_value(self):
        assert softplus(50) == pytest.approx(50.0, abs=1e-10)

    def test_negative(self):
        assert softplus(-10) == pytest.approx(math.log1p(math.exp(-10)), abs=1e-10)


# ──────────────────────────────────────────────
# Statistics/ML: logit
# ──────────────────────────────────────────────

class TestLogitV2:

    def test_half(self):
        assert logit(0.5) == 0.0

    def test_boundary_zero_raises(self):
        with pytest.raises(ValueError):
            logit(0)

    def test_boundary_one_raises(self):
        with pytest.raises(ValueError):
            logit(1)

    def test_inverse_of_sigmoid(self):
        assert logit(sigmoid(2.5)) == pytest.approx(2.5, abs=1e-10)


# ──────────────────────────────────────────────
# Statistics/ML: binary_entropy
# ──────────────────────────────────────────────

class TestBinaryEntropy:

    def test_max_entropy(self):
        assert binary_entropy(0.5) == 1.0

    def test_zero(self):
        assert binary_entropy(0) == 0.0

    def test_one(self):
        assert binary_entropy(1) == 0.0

    def test_out_of_range_raises(self):
        with pytest.raises(ValueError):
            binary_entropy(1.5)


# ──────────────────────────────────────────────
# Statistics/ML: bayes_theorem
# ──────────────────────────────────────────────

class TestBayesTheoremV2:

    def test_basic(self):
        assert bayes_theorem(0.01, 0.9, 0.05) == pytest.approx(0.18)

    def test_equal_priors(self):
        assert bayes_theorem(0.5, 0.8, 0.5) == pytest.approx(0.8)

    def test_zero_pb_raises(self):
        with pytest.raises(ValueError):
            bayes_theorem(0.5, 0.8, 0)

    def test_out_of_range_raises(self):
        with pytest.raises(ValueError):
            bayes_theorem(1.5, 0.8, 0.5)


# ──────────────────────────────────────────────
# Engineering: bmi
# ──────────────────────────────────────────────

class TestLeakyRelu:

    def test_positive(self):
        assert leaky_relu(5) == 5.0

    def test_negative_default(self):
        assert leaky_relu(-10) == pytest.approx(-0.1)

    def test_negative_custom_alpha(self):
        assert leaky_relu(-10, alpha=0.2) == pytest.approx(-2.0)

    def test_zero(self):
        assert leaky_relu(0) == 0.0


# ──────────────────────────────────────────────
# Statistics/ML: elu
# ──────────────────────────────────────────────

class TestElu:

    def test_positive(self):
        assert elu(1.0) == 1.0

    def test_negative(self):
        assert round(elu(-1.0), 4) == -0.6321

    def test_zero(self):
        assert elu(0) == 0.0

    def test_custom_alpha(self):
        assert round(elu(-1.0, alpha=2.0), 4) == -1.2642


# ──────────────────────────────────────────────
# Statistics/ML: swish
# ──────────────────────────────────────────────

class TestSwish:

    def test_zero(self):
        assert swish(0) == 0.0

    def test_positive(self):
        assert round(swish(1), 4) == 0.7311

    def test_negative(self):
        result = swish(-2)
        assert result < 0


# ──────────────────────────────────────────────
# Statistics/ML: huber_loss
# ──────────────────────────────────────────────

class TestHuberLoss:

    def test_small_error(self):
        assert huber_loss(1.0, 1.5) == pytest.approx(0.125)

    def test_large_error(self):
        assert huber_loss(1.0, 5.0) == pytest.approx(3.5)

    def test_zero_error(self):
        assert huber_loss(3.0, 3.0) == 0.0

    def test_negative_delta_raises(self):
        with pytest.raises(ValueError):
            huber_loss(1.0, 2.0, delta=-1)


# ──────────────────────────────────────────────
# Statistics/ML: relative_error
# ──────────────────────────────────────────────

class TestRelativeError:

    def test_basic(self):
        assert relative_error(10.5, 10.0) == pytest.approx(0.05)

    def test_zero_actual_raises(self):
        with pytest.raises(ValueError):
            relative_error(5, 0)


# ──────────────────────────────────────────────
# Statistics/ML: absolute_error
# ──────────────────────────────────────────────

class TestAbsoluteError:

    def test_basic(self):
        assert absolute_error(10.5, 10.0) == pytest.approx(0.5)

    def test_negative(self):
        assert absolute_error(9.5, 10.0) == pytest.approx(0.5)

    def test_exact(self):
        assert absolute_error(5, 5) == 0.0


# ──────────────────────────────────────────────
# Physics: ideal_gas_pressure
# ──────────────────────────────────────────────

class TestGelu:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import gelu

        assert round(gelu(1.0), 4) == 0.8412

    def test_zero(self):
        from agentfx.fxNumeric.statistics_functions import gelu

        assert gelu(0) == pytest.approx(0.0, abs=1e-6)

    def test_type_error(self):
        from agentfx.fxNumeric.statistics_functions import gelu

        with pytest.raises(TypeError):
            gelu("a")

class TestMish:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import mish

        assert round(mish(1.0), 4) == 0.8651

    def test_zero(self):
        from agentfx.fxNumeric.statistics_functions import mish

        assert mish(0) == pytest.approx(0.0, abs=1e-6)

class TestHingeLoss:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import hinge_loss

        assert hinge_loss(1, 0.5) == 0.5

    def test_correct_prediction(self):
        from agentfx.fxNumeric.statistics_functions import hinge_loss

        assert hinge_loss(1, 2.0) == 0.0

    def test_invalid_label(self):
        from agentfx.fxNumeric.statistics_functions import hinge_loss

        with pytest.raises(ValueError):
            hinge_loss(0, 0.5)

class TestLogLoss:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import log_loss

        assert round(log_loss(1, 0.9), 4) == 0.1054

    def test_invalid_label(self):
        from agentfx.fxNumeric.statistics_functions import log_loss

        with pytest.raises(ValueError):
            log_loss(2, 0.5)

class TestTanhActivation:

    def test_basic(self):
        from agentfx.fxNumeric.statistics_functions import tanh_activation

        assert round(tanh_activation(1.0), 4) == 0.7616

    def test_zero(self):
        from agentfx.fxNumeric.statistics_functions import tanh_activation

        assert tanh_activation(0) == pytest.approx(0.0)


# ── Physics / Engineering ────────────────────────────────────────────

class TestBetaFunctionV2:

    def test_basic(self):
        from agentfx.fxNumeric.special_functions import beta_function
        # B(2,3) = 1!*2!/4! = 1/12
        assert beta_function(2, 3) == pytest.approx(1.0 / 12.0)

    def test_symmetry(self):
        from agentfx.fxNumeric.special_functions import beta_function
        assert beta_function(3, 5) == pytest.approx(beta_function(5, 3))
