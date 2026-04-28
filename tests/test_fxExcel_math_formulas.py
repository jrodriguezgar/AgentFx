"""Tests for fxExcel.math_formulas."""


from shortfx.fxExcel.math_formulas import ROUND, SUMIF


def test_sum_if():
    values = [1, 2, 3, 4, 5]
    assert SUMIF(values, ">3") == 9  # 4 + 5
    assert SUMIF(values, "<3") == 3  # 1 + 2
    assert SUMIF(values, "=3") == 3  # 3

def test_round_number():
    assert ROUND(3.14159, 2) == 3.14
    assert ROUND(3.14159) == 3
    assert ROUND(3.5) == 4
