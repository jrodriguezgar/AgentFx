"""Tests for fxExcel.text_formulas."""


from formulite.fxExcel.text_formulas import (
    CONCAT,
    LEFT,
    MID,
    RIGHT,
)


def test_concat():
    assert CONCAT("Hello", " ", "World") == "Hello World"
    assert CONCAT(1, 2, 3) == "123"
    assert CONCAT("A", "-", "B", "-", "C") == "A-B-C"

def test_left():
    assert LEFT("Hello World", 5) == "Hello"
    assert LEFT("Python", 2) == "Py"
    assert LEFT("A", 5) == "A"  # Should not error when num_chars > len(text)

def test_right():
    assert RIGHT("Hello World", 5) == "World"
    assert RIGHT("Python", 2) == "on"
    assert RIGHT("A", 5) == "A"  # Should not error when num_chars > len(text)

def test_mid():
    assert MID("Hello World", 7, 5) == "World"
    assert MID("Python", 2, 2) == "yt"
    assert MID("A", 1, 5) == "A"  # Should not error when num_chars > len(text)
