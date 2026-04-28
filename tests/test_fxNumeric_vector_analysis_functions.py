"""Tests for fxNumeric.vector_analysis_functions."""

import math

import pytest

from shortfx.fxNumeric import flux_integral_numerical, surface_integral_numerical


class TestTripleProducts:

    def test_scalar_triple(self):
        from shortfx.fxNumeric.vector_analysis_functions import scalar_triple_product
        assert scalar_triple_product([1, 0, 0], [0, 1, 0], [0, 0, 1]) == pytest.approx(1.0)

    def test_vector_triple(self):
        from shortfx.fxNumeric.vector_analysis_functions import vector_triple_product
        result = vector_triple_product([1, 0, 0], [0, 1, 0], [0, 0, 1])
        assert all(abs(v) < 1e-10 for v in result)

class TestVectorProjection:

    def test_basic(self):
        from shortfx.fxNumeric.vector_analysis_functions import vector_projection
        proj = vector_projection([3, 4], [1, 0])
        assert proj == pytest.approx([3.0, 0.0])

class TestGradient:

    def test_gradient_quadratic(self):
        from shortfx.fxNumeric.vector_analysis_functions import gradient_numerical
        grad = gradient_numerical(lambda x, y: x ** 2 + y ** 2, [1.0, 2.0])
        assert grad[0] == pytest.approx(2.0, rel=1e-4)
        assert grad[1] == pytest.approx(4.0, rel=1e-4)

class TestDivergence:

    def test_identity_field(self):
        from shortfx.fxNumeric.vector_analysis_functions import divergence_numerical
        div = divergence_numerical(
            [lambda x, y: x, lambda x, y: y],
            [1.0, 1.0],
        )
        assert div == pytest.approx(2.0, rel=1e-4)

class TestCurl:

    def test_rotation_field(self):
        from shortfx.fxNumeric.vector_analysis_functions import curl_numerical
        curl = curl_numerical(
            [lambda x, y, z: -y, lambda x, y, z: x, lambda x, y, z: 0],
            [0.0, 0.0, 0.0],
        )
        assert curl[2] == pytest.approx(2.0, rel=1e-3)

class TestLaplacian:

    def test_quadratic(self):
        from shortfx.fxNumeric.vector_analysis_functions import laplacian_numerical
        lap = laplacian_numerical(lambda x, y: x ** 2 + y ** 2, [1.0, 1.0])
        assert lap == pytest.approx(4.0, rel=1e-3)

class TestJacobian:

    def test_basic(self):
        from shortfx.fxNumeric.vector_analysis_functions import jacobian_numerical
        J = jacobian_numerical(
            [lambda x, y: x * y, lambda x, y: x + y],
            [2.0, 3.0],
        )
        assert J[0][0] == pytest.approx(3.0, rel=1e-3)
        assert J[0][1] == pytest.approx(2.0, rel=1e-3)
        assert J[1][0] == pytest.approx(1.0, rel=1e-3)
        assert J[1][1] == pytest.approx(1.0, rel=1e-3)

class TestHessian:

    def test_quadratic(self):
        from shortfx.fxNumeric.vector_analysis_functions import hessian_numerical
        H = hessian_numerical(lambda x, y: x ** 2 + y ** 2, [1.0, 1.0])
        assert H[0][0] == pytest.approx(2.0, rel=1e-3)
        assert H[1][1] == pytest.approx(2.0, rel=1e-3)
        assert abs(H[0][1]) < 0.01


# ---------------------------------------------------------------------------
# Transform functions
# ---------------------------------------------------------------------------

class TestSurfaceIntegral:

    def test_sphere_area(self):
        # Surface area of unit sphere = 4π

        def sphere(u, v):
            return (math.sin(u) * math.cos(v), math.sin(u) * math.sin(v), math.cos(u))

        area = surface_integral_numerical(
            lambda x, y, z: 1.0,
            sphere,
            (0, math.pi),
            (0, 2 * math.pi),
            80, 80,
        )
        assert abs(area - 4 * math.pi) < 0.5

class TestFluxIntegral:

    def test_radial_field_sphere(self):
        # Flux of F=(x,y,z) through unit sphere = ∭ div(F)dV = ∭ 3 dV = 4π

        def sphere(u, v):
            return (math.sin(u) * math.cos(v), math.sin(u) * math.sin(v), math.cos(u))

        flux = flux_integral_numerical(
            (lambda x, y, z: x, lambda x, y, z: y, lambda x, y, z: z),
            sphere,
            (0, math.pi),
            (0, 2 * math.pi),
            80, 80,
        )
        assert abs(flux - 4 * math.pi) < 0.5
