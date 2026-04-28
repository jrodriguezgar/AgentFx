"""Tests for fxExcel.statistic_formulas."""


from agentfx.fxExcel.statistic_formulas import AVERAGE


def test_average():
    assert AVERAGE([1, 2, 3, 4, 5]) == 3.0
