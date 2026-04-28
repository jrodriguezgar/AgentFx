"""Tests for fxExcel.lookup_formulas."""


import pytest

from shortfx.fxExcel.lookup_formulas import HLOOKUP, VLOOKUP

test_table = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 30, "London"],
    ["Charlie", 35, "Paris"]
]


def test_vlookup():
    # Exact match
    assert VLOOKUP("Bob", test_table, 2, range_lookup=False) == 30
    assert VLOOKUP("Alice", test_table, 3, range_lookup=False) == "New York"

    with pytest.raises(ValueError):
        VLOOKUP("David", test_table, 2, range_lookup=False)

    # Approximate match
    numbers = [[1, "A"], [3, "B"], [5, "C"]]
    assert VLOOKUP(4, numbers, 2) == "B"
    assert VLOOKUP(6, numbers, 2) == "C"

def test_hlookup():
    transposed_table = [
        [1, 2, 3, 4],
        ["A", "B", "C", "D"],
        ["W", "X", "Y", "Z"]
    ]

    assert HLOOKUP(3, transposed_table, 2, range_lookup=False) == "C"
    assert HLOOKUP(1, transposed_table, 3, range_lookup=False) == "W"

    with pytest.raises(ValueError):
        HLOOKUP(5, transposed_table, 2, range_lookup=False)
