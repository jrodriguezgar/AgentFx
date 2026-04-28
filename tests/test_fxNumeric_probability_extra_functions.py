"""Tests for fxNumeric.probability_extra_functions."""

import math

import pytest

from agentfx.fxNumeric import (
    bernoulli_mean,
    bernoulli_pmf,
    bernoulli_variance,
    cauchy_cdf,
    cauchy_pdf,
    cauchy_quantile,
    geometric_cdf,
    geometric_mean_dist,
    geometric_pmf,
    geometric_variance_dist,
    log_logistic_cdf,
    log_logistic_pdf,
    maxwell_boltzmann_cdf,
    maxwell_boltzmann_mean,
    maxwell_boltzmann_pdf,
    pareto_cdf,
    pareto_mean,
    pareto_pdf,
    pareto_variance,
    rayleigh_cdf,
    rayleigh_mean,
    rayleigh_pdf,
    rayleigh_variance,
    uniform_continuous_cdf,
    uniform_continuous_mean,
    uniform_continuous_pdf,
    uniform_continuous_variance,
    uniform_discrete_cdf,
    uniform_discrete_pmf,
)


class TestBernoulli:

    def test_pmf_1(self):
        assert bernoulli_pmf(1, 0.3) == 0.3

    def test_pmf_0(self):
        assert bernoulli_pmf(0, 0.3) == pytest.approx(0.7)

    def test_mean(self):
        assert bernoulli_mean(0.7) == 0.7

    def test_variance(self):
        assert bernoulli_variance(0.5) == 0.25

    def test_invalid_k(self):
        with pytest.raises(ValueError):
            bernoulli_pmf(2, 0.5)

class TestGeometric:

    def test_pmf(self):
        assert geometric_pmf(3, 0.5) == 0.125

    def test_cdf(self):
        assert geometric_cdf(3, 0.5) == 0.875

    def test_mean(self):
        assert geometric_mean_dist(0.25) == 4.0

    def test_variance(self):
        assert geometric_variance_dist(0.5) == 2.0

    def test_pmf_sums(self):
        # PMF should sum to ~1
        total = sum(geometric_pmf(k, 0.3) for k in range(1, 100))
        assert abs(total - 1.0) < 1e-6

class TestCauchy:

    def test_pdf_peak(self):
        assert abs(cauchy_pdf(0) - 1.0 / math.pi) < 1e-10

    def test_cdf_half(self):
        assert cauchy_cdf(0) == 0.5

    def test_quantile_median(self):
        assert abs(cauchy_quantile(0.5) - 0) < 1e-10

    def test_quantile_inverse(self):
        x = cauchy_quantile(0.75)
        assert abs(cauchy_cdf(x) - 0.75) < 1e-10

class TestUniformContinuous:

    def test_pdf(self):
        assert uniform_continuous_pdf(0.5, 0, 1) == 1.0

    def test_pdf_outside(self):
        assert uniform_continuous_pdf(2, 0, 1) == 0.0

    def test_cdf(self):
        assert uniform_continuous_cdf(0.25, 0, 1) == 0.25

    def test_mean(self):
        assert uniform_continuous_mean(2, 8) == 5.0

    def test_variance(self):
        assert abs(uniform_continuous_variance(0, 1) - 1.0 / 12) < 1e-10

class TestUniformDiscrete:

    def test_pmf(self):
        assert abs(uniform_discrete_pmf(3, 1, 6) - 1.0 / 6) < 1e-10

    def test_pmf_outside(self):
        assert uniform_discrete_pmf(7, 1, 6) == 0.0

    def test_cdf(self):
        assert uniform_discrete_cdf(3, 1, 6) == 0.5

class TestPareto:

    def test_pdf(self):
        assert pareto_pdf(1, 1, 2) == 2.0

    def test_cdf(self):
        assert pareto_cdf(2, 1, 2) == 0.75

    def test_mean(self):
        assert pareto_mean(1, 3) == 1.5

    def test_variance(self):
        assert abs(pareto_variance(1, 3) - 0.75) < 1e-6

    def test_mean_undefined(self):
        with pytest.raises(ValueError):
            pareto_mean(1, 1)

class TestRayleigh:

    def test_pdf(self):
        assert abs(rayleigh_pdf(1, 1) - math.exp(-0.5)) < 1e-10

    def test_cdf(self):
        assert abs(rayleigh_cdf(1, 1) - (1 - math.exp(-0.5))) < 1e-10

    def test_mean(self):
        assert abs(rayleigh_mean(1) - math.sqrt(math.pi / 2)) < 1e-10

    def test_variance(self):
        assert abs(rayleigh_variance(1) - (4 - math.pi) / 2) < 1e-10

class TestMaxwellBoltzmann:

    def test_pdf_positive(self):
        assert maxwell_boltzmann_pdf(1, 1) > 0

    def test_cdf_monotone(self):
        assert maxwell_boltzmann_cdf(2, 1) > maxwell_boltzmann_cdf(1, 1)

    def test_mean(self):
        assert abs(maxwell_boltzmann_mean(1) - 2 * math.sqrt(2 / math.pi)) < 1e-10

class TestLogLogistic:

    def test_pdf_at_median(self):
        # At x = alpha, CDF = 0.5
        assert abs(log_logistic_cdf(1, 1, 2) - 0.5) < 1e-10

    def test_pdf_positive(self):
        assert log_logistic_pdf(1, 1, 2) > 0


# ===================================================================
# Conformal mappings
# ===================================================================
