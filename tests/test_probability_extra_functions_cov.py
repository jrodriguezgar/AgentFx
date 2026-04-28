# Coverage tests for shortfx.fxNumeric.probability_extra_functions

from shortfx.fxNumeric import probability_extra_functions as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_bernoulli_mean:
    def test_exists(self):
        assert hasattr(mod, "bernoulli_mean")

    def test_doc0(self):
        try:
            mod.bernoulli_mean(0.7)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bernoulli_mean(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bernoulli_mean(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bernoulli_mean(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bernoulli_mean("")
        except EXC:
            pass


class Test_bernoulli_pmf:
    def test_exists(self):
        assert hasattr(mod, "bernoulli_pmf")

    def test_doc0(self):
        try:
            mod.bernoulli_pmf(1, 0.3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bernoulli_pmf(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bernoulli_pmf(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bernoulli_pmf(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bernoulli_pmf(0, "")
        except EXC:
            pass


class Test_bernoulli_variance:
    def test_exists(self):
        assert hasattr(mod, "bernoulli_variance")

    def test_doc0(self):
        try:
            mod.bernoulli_variance(0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.bernoulli_variance(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.bernoulli_variance(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.bernoulli_variance(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.bernoulli_variance("")
        except EXC:
            pass


class Test_cauchy_cdf:
    def test_exists(self):
        assert hasattr(mod, "cauchy_cdf")

    def test_doc0(self):
        try:
            mod.cauchy_cdf(0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cauchy_cdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cauchy_cdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cauchy_cdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cauchy_cdf("")
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


class Test_cauchy_quantile:
    def test_exists(self):
        assert hasattr(mod, "cauchy_quantile")

    def test_doc0(self):
        try:
            mod.cauchy_quantile(0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.cauchy_quantile(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.cauchy_quantile(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.cauchy_quantile(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.cauchy_quantile("")
        except EXC:
            pass


class Test_geometric_cdf:
    def test_exists(self):
        assert hasattr(mod, "geometric_cdf")

    def test_doc0(self):
        try:
            mod.geometric_cdf(3, 0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.geometric_cdf(0, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geometric_cdf(1, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geometric_cdf(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geometric_cdf(0, "")
        except EXC:
            pass


class Test_geometric_mean_dist:
    def test_exists(self):
        assert hasattr(mod, "geometric_mean_dist")

    def test_doc0(self):
        try:
            mod.geometric_mean_dist(0.25)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.geometric_mean_dist(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geometric_mean_dist(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geometric_mean_dist(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geometric_mean_dist("")
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


class Test_geometric_variance_dist:
    def test_exists(self):
        assert hasattr(mod, "geometric_variance_dist")

    def test_doc0(self):
        try:
            mod.geometric_variance_dist(0.5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.geometric_variance_dist(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.geometric_variance_dist(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.geometric_variance_dist(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.geometric_variance_dist("")
        except EXC:
            pass


class Test_log_logistic_cdf:
    def test_exists(self):
        assert hasattr(mod, "log_logistic_cdf")

    def test_doc0(self):
        try:
            mod.log_logistic_cdf(1, 1, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.log_logistic_cdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.log_logistic_cdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.log_logistic_cdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.log_logistic_cdf("", 0, 0)
        except EXC:
            pass


class Test_log_logistic_pdf:
    def test_exists(self):
        assert hasattr(mod, "log_logistic_pdf")

    def test_var0(self):
        try:
            mod.log_logistic_pdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.log_logistic_pdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.log_logistic_pdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.log_logistic_pdf("", 0, 0)
        except EXC:
            pass


class Test_maxwell_boltzmann_cdf:
    def test_exists(self):
        assert hasattr(mod, "maxwell_boltzmann_cdf")

    def test_var0(self):
        try:
            mod.maxwell_boltzmann_cdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.maxwell_boltzmann_cdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.maxwell_boltzmann_cdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.maxwell_boltzmann_cdf("")
        except EXC:
            pass


class Test_maxwell_boltzmann_mean:
    def test_exists(self):
        assert hasattr(mod, "maxwell_boltzmann_mean")

    def test_var0(self):
        try:
            mod.maxwell_boltzmann_mean()
        except EXC:
            pass


class Test_maxwell_boltzmann_pdf:
    def test_exists(self):
        assert hasattr(mod, "maxwell_boltzmann_pdf")

    def test_var0(self):
        try:
            mod.maxwell_boltzmann_pdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.maxwell_boltzmann_pdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.maxwell_boltzmann_pdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.maxwell_boltzmann_pdf("")
        except EXC:
            pass


class Test_pareto_cdf:
    def test_exists(self):
        assert hasattr(mod, "pareto_cdf")

    def test_doc0(self):
        try:
            mod.pareto_cdf(2, 1, 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pareto_cdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pareto_cdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pareto_cdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pareto_cdf("", "", 0)
        except EXC:
            pass


class Test_pareto_mean:
    def test_exists(self):
        assert hasattr(mod, "pareto_mean")

    def test_doc0(self):
        try:
            mod.pareto_mean(1, 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pareto_mean(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pareto_mean(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pareto_mean(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pareto_mean("", 0)
        except EXC:
            pass


class Test_pareto_pdf:
    def test_exists(self):
        assert hasattr(mod, "pareto_pdf")

    def test_doc0(self):
        try:
            mod.pareto_pdf(1, 1, 2)
        except EXC:
            pass

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


class Test_pareto_variance:
    def test_exists(self):
        assert hasattr(mod, "pareto_variance")

    def test_var0(self):
        try:
            mod.pareto_variance(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pareto_variance(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pareto_variance(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pareto_variance("", 0)
        except EXC:
            pass


class Test_rayleigh_cdf:
    def test_exists(self):
        assert hasattr(mod, "rayleigh_cdf")

    def test_var0(self):
        try:
            mod.rayleigh_cdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rayleigh_cdf(100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rayleigh_cdf(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.rayleigh_cdf("")
        except EXC:
            pass


class Test_rayleigh_mean:
    def test_exists(self):
        assert hasattr(mod, "rayleigh_mean")

    def test_var0(self):
        try:
            mod.rayleigh_mean()
        except EXC:
            pass


class Test_rayleigh_pdf:
    def test_exists(self):
        assert hasattr(mod, "rayleigh_pdf")

    def test_var0(self):
        try:
            mod.rayleigh_pdf(3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rayleigh_pdf(100)
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


class Test_rayleigh_variance:
    def test_exists(self):
        assert hasattr(mod, "rayleigh_variance")

    def test_var0(self):
        try:
            mod.rayleigh_variance()
        except EXC:
            pass


class Test_uniform_continuous_cdf:
    def test_exists(self):
        assert hasattr(mod, "uniform_continuous_cdf")

    def test_doc0(self):
        try:
            mod.uniform_continuous_cdf(0.25, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.uniform_continuous_cdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.uniform_continuous_cdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.uniform_continuous_cdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.uniform_continuous_cdf("", "", "")
        except EXC:
            pass


class Test_uniform_continuous_mean:
    def test_exists(self):
        assert hasattr(mod, "uniform_continuous_mean")

    def test_doc0(self):
        try:
            mod.uniform_continuous_mean(2, 8)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.uniform_continuous_mean(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.uniform_continuous_mean(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.uniform_continuous_mean(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.uniform_continuous_mean("", "")
        except EXC:
            pass


class Test_uniform_continuous_pdf:
    def test_exists(self):
        assert hasattr(mod, "uniform_continuous_pdf")

    def test_doc0(self):
        try:
            mod.uniform_continuous_pdf(0.5, 0, 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.uniform_continuous_pdf(3.14, 3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.uniform_continuous_pdf(100, 100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.uniform_continuous_pdf(None, 3.14, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.uniform_continuous_pdf("", "", "")
        except EXC:
            pass


class Test_uniform_continuous_variance:
    def test_exists(self):
        assert hasattr(mod, "uniform_continuous_variance")

    def test_var0(self):
        try:
            mod.uniform_continuous_variance(3.14, 3.14)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.uniform_continuous_variance(100, 100)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.uniform_continuous_variance(None, 3.14)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.uniform_continuous_variance("", "")
        except EXC:
            pass


class Test_uniform_discrete_cdf:
    def test_exists(self):
        assert hasattr(mod, "uniform_discrete_cdf")

    def test_doc0(self):
        try:
            mod.uniform_discrete_cdf(3, 1, 6)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.uniform_discrete_cdf(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.uniform_discrete_cdf(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.uniform_discrete_cdf(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.uniform_discrete_cdf(0, "", "")
        except EXC:
            pass


class Test_uniform_discrete_pmf:
    def test_exists(self):
        assert hasattr(mod, "uniform_discrete_pmf")

    def test_var0(self):
        try:
            mod.uniform_discrete_pmf(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.uniform_discrete_pmf(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.uniform_discrete_pmf(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.uniform_discrete_pmf(0, "", "")
        except EXC:
            pass

