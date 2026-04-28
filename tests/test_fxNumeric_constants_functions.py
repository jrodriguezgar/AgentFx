"""Tests for fxNumeric.constants_functions."""

import math

import pytest

from shortfx.fxNumeric.constants_functions import (
    E,
    PI,
    get_constant,
    list_constants,
)


class TestConstants:

    def test_get_constant_pi(self):
        assert get_constant("pi") == pytest.approx(math.pi)

    def test_get_constant_e(self):
        assert get_constant("e") == pytest.approx(math.e)

    def test_get_constant_avogadro(self):
        assert get_constant("avogadro") == pytest.approx(6.02214076e23)

    def test_get_constant_speed_of_light(self):
        assert get_constant("speed_of_light") == 299_792_458.0

    def test_get_constant_case_insensitive(self):
        assert get_constant("PI") == get_constant("pi")

    def test_get_constant_unknown_raises(self):

        with pytest.raises(KeyError):
            get_constant("nonexistent")

    def test_module_level_constants(self):
        assert PI == pytest.approx(math.pi)
        assert E == pytest.approx(math.e)

    def test_list_constants_all(self):
        result = list_constants()
        assert len(result) > 0
        assert all("name" in c for c in result)

    def test_list_constants_math(self):
        result = list_constants("math")
        names = {c["name"] for c in result}
        assert "pi" in names

    def test_list_constants_physical(self):
        result = list_constants("physical")
        names = {c["name"] for c in result}
        assert "avogadro" in names

    def test_list_constants_invalid_category_raises(self):

        with pytest.raises(ValueError):
            list_constants("invalid")


# ── Expression Evaluator ─────────────────────────────────────────────────────
