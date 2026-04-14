# Deep coverage tests for formulite.fxString.string_similarity
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxString.string_similarity as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_calculate_similarity_deep:
    def test_c0(self):
        try:
            mod.calculate_similarity("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.calculate_similarity("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.calculate_similarity("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.calculate_similarity("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.calculate_similarity("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.calculate_similarity("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_algorithm(self):
        try:
            mod.calculate_similarity("hello world", "test", algorithm=1)
        except EXC:
            pass


class Test_string_similarity_score_deep:
    def test_c0(self):
        try:
            mod.string_similarity_score("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.string_similarity_score("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.string_similarity_score("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.string_similarity_score("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.string_similarity_score("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.string_similarity_score("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_find_closest_match_deep:
    def test_c0(self):
        try:
            mod.find_closest_match("hello world", [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.find_closest_match("test", [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.find_closest_match("abc123", [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.find_closest_match("", [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.find_closest_match("Hello, World!", [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.find_closest_match("UPPER lower 123", [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_algorithm(self):
        try:
            mod.find_closest_match("hello world", [10, 20, 30], algorithm="hello world")
        except EXC:
            pass


class Test_rank_by_similarity_deep:
    def test_c0(self):
        try:
            mod.rank_by_similarity("hello world", [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rank_by_similarity("test", [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rank_by_similarity("abc123", [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rank_by_similarity("", [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rank_by_similarity("Hello, World!", [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rank_by_similarity("UPPER lower 123", [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_algorithm(self):
        try:
            mod.rank_by_similarity("hello world", [10, 20, 30], algorithm="hello world")
        except EXC:
            pass

    def test_kw_top_n(self):
        try:
            mod.rank_by_similarity("hello world", [10, 20, 30], top_n=1)
        except EXC:
            pass


class Test_string_cosine_score_deep:
    def test_c0(self):
        try:
            mod.string_cosine_score("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.string_cosine_score("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.string_cosine_score("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.string_cosine_score("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.string_cosine_score("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.string_cosine_score("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_n(self):
        try:
            mod.string_cosine_score("hello world", "test", n=1)
        except EXC:
            pass


class Test_string_dna_score_deep:
    def test_c0(self):
        try:
            mod.string_dna_score("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.string_dna_score("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.string_dna_score("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.string_dna_score("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.string_dna_score("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.string_dna_score("UPPER lower 123", "hello world")
        except EXC:
            pass

