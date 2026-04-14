"""Tests for fxExcel.statistic_formulas."""


from formulite.fxExcel.statistic_formulas import AVERAGE


def test_average():
    assert AVERAGE([1, 2, 3, 4, 5]) == 3.0
