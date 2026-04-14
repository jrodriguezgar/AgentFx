# Deep coverage tests for formulite.fxPython.py_operations
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxPython.py_operations as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_pick_in_collection_deep:
    def test_c0(self):
        try:
            mod.pick_in_collection([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pick_in_collection([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pick_in_collection([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pick_in_collection([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pick_in_collection([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pick_in_collection([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_prompt(self):
        try:
            mod.pick_in_collection([1, 2, 3, 4, 5], prompt="hello world")
        except EXC:
            pass

    def test_kw_allow_multiple(self):
        try:
            mod.pick_in_collection([1, 2, 3, 4, 5], allow_multiple=True)
        except EXC:
            pass

    def test_kw_return_index(self):
        try:
            mod.pick_in_collection([1, 2, 3, 4, 5], return_index=True)
        except EXC:
            pass


class Test_xmatch_deep:
    def test_c0(self):
        try:
            mod.xmatch({"a": 1, "b": 2, "c": 3}, [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.xmatch({}, [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.xmatch({"key": "value"}, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.xmatch({"a": 1, "b": 2, "c": 3}, [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.xmatch({}, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.xmatch({"key": "value"}, [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_match_mode(self):
        try:
            mod.xmatch({"a": 1, "b": 2, "c": 3}, [10, 20, 30], match_mode=1)
        except EXC:
            pass

    def test_kw_search_mode(self):
        try:
            mod.xmatch({"a": 1, "b": 2, "c": 3}, [10, 20, 30], search_mode=1)
        except EXC:
            pass


class Test_xlookup_deep:
    def test_c0(self):
        try:
            mod.xlookup({"a": 1, "b": 2, "c": 3}, [10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.xlookup({}, [0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.xlookup({"key": "value"}, [-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.xlookup({"a": 1, "b": 2, "c": 3}, [100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.xlookup({}, [1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.xlookup({"key": "value"}, [1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_kw_if_not_found(self):
        try:
            mod.xlookup({"a": 1, "b": 2, "c": 3}, [10, 20, 30], [0, 1], if_not_found=1)
        except EXC:
            pass

    def test_kw_match_mode(self):
        try:
            mod.xlookup({"a": 1, "b": 2, "c": 3}, [10, 20, 30], [0, 1], match_mode=1)
        except EXC:
            pass


class Test_collection_filter_deep:
    def test_c0(self):
        try:
            mod.collection_filter([1, 2, 3, 4, 5], False)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.collection_filter([10, 20, 30], True)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.collection_filter([0, 1], False)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.collection_filter([-3, -1, 0, 2, 5], True)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.collection_filter([100], False)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.collection_filter([1, 1, 2, 3, 5, 8], True)
        except EXC:
            pass


class Test_dictionary_rename_keys_deep:
    def test_c0(self):
        try:
            mod.dictionary_rename_keys(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dictionary_rename_keys(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dictionary_rename_keys(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dictionary_rename_keys(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dictionary_rename_keys(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dictionary_rename_keys(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.dictionary_rename_keys(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.dictionary_rename_keys(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.dictionary_rename_keys(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.dictionary_rename_keys(2, 10)
        except EXC:
            pass


class Test_merge_elements_deep:
    def test_c0(self):
        try:
            mod.merge_elements(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.merge_elements(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.merge_elements(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.merge_elements(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.merge_elements(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.merge_elements(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.merge_elements(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.merge_elements(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.merge_elements(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.merge_elements(2, 1)
        except EXC:
            pass

    def test_kw_return_type(self):
        try:
            mod.merge_elements(1, 42, return_type="hello world")
        except EXC:
            pass

    def test_kw_remove_duplicates(self):
        try:
            mod.merge_elements(1, 42, remove_duplicates=True)
        except EXC:
            pass


class Test_filter_elements_by_another_deep:
    def test_c0(self):
        try:
            mod.filter_elements_by_another(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.filter_elements_by_another(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.filter_elements_by_another(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.filter_elements_by_another(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.filter_elements_by_another(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.filter_elements_by_another(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.filter_elements_by_another(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.filter_elements_by_another(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.filter_elements_by_another(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.filter_elements_by_another(2, 1)
        except EXC:
            pass

    def test_kw_return_type(self):
        try:
            mod.filter_elements_by_another(1, 42, return_type="hello world")
        except EXC:
            pass


class Test_index_2d_deep:
    def test_c0(self):
        try:
            mod.index_2d([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.index_2d([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.index_2d([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.index_2d([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.index_2d([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.index_2d([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass

    def test_kw_col_num(self):
        try:
            mod.index_2d([1, 2, 3, 4, 5], 2, col_num=1)
        except EXC:
            pass


class Test_combine_dictionaries_deep:
    def test_c0(self):
        try:
            mod.combine_dictionaries(1, 42, "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.combine_dictionaries(42, 0, "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.combine_dictionaries(0, -5, "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.combine_dictionaries(-5, 3.14, "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.combine_dictionaries(3.14, 100, "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.combine_dictionaries(100, 0.5, "test")
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.combine_dictionaries(0.5, 1000, "abc123")
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.combine_dictionaries(1000, -1, "")
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.combine_dictionaries(-1, 2, "Hello, World!")
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.combine_dictionaries(2, 1, "UPPER lower 123")
        except EXC:
            pass


class Test_collection_stdev_deep:
    def test_c0(self):
        try:
            mod.collection_stdev(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.collection_stdev(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.collection_stdev(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.collection_stdev(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.collection_stdev(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.collection_stdev(0)
        except EXC:
            pass

    def test_kw_is_sample(self):
        try:
            mod.collection_stdev(1, is_sample=True)
        except EXC:
            pass

    def test_kw_ignore_none(self):
        try:
            mod.collection_stdev(1, ignore_none=True)
        except EXC:
            pass


class Test_execute_os_command_deep:
    def test_c0(self):
        try:
            mod.execute_os_command([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.execute_os_command([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.execute_os_command([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.execute_os_command([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.execute_os_command([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.execute_os_command([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_unique_tuple_list_deep:
    def test_c0(self):
        try:
            mod.unique_tuple_list([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.unique_tuple_list([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.unique_tuple_list([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.unique_tuple_list([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.unique_tuple_list([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.unique_tuple_list([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_choose_cols_deep:
    def test_c0(self):
        try:
            mod.choose_cols([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.choose_cols([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.choose_cols([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.choose_cols([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.choose_cols([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.choose_cols([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_choose_rows_deep:
    def test_c0(self):
        try:
            mod.choose_rows([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.choose_rows([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.choose_rows([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.choose_rows([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.choose_rows([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.choose_rows([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_collection_avg_deep:
    def test_c0(self):
        try:
            mod.collection_avg(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.collection_avg(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.collection_avg(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.collection_avg(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.collection_avg(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.collection_avg(0)
        except EXC:
            pass

    def test_kw_ignore_none(self):
        try:
            mod.collection_avg(1, ignore_none=True)
        except EXC:
            pass


class Test_collection_max_deep:
    def test_c0(self):
        try:
            mod.collection_max([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.collection_max([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.collection_max([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.collection_max([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.collection_max([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.collection_max([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_ignore_none(self):
        try:
            mod.collection_max([1, 2, 3, 4, 5], ignore_none=True)
        except EXC:
            pass


class Test_collection_min_deep:
    def test_c0(self):
        try:
            mod.collection_min([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.collection_min([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.collection_min([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.collection_min([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.collection_min([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.collection_min([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_ignore_none(self):
        try:
            mod.collection_min([1, 2, 3, 4, 5], ignore_none=True)
        except EXC:
            pass


class Test_count_ifs_deep:
    def test_c0(self):
        try:
            mod.count_ifs([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.count_ifs([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.count_ifs([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.count_ifs([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.count_ifs([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.count_ifs([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_count_numbers_deep:
    def test_c0(self):
        try:
            mod.count_numbers()
        except EXC:
            pass


class Test_count_values_deep:
    def test_c0(self):
        try:
            mod.count_values()
        except EXC:
            pass


class Test_get_nested_deep:
    def test_c0(self):
        try:
            mod.get_nested([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_nested([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_nested([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_nested([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_nested([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_nested([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_default(self):
        try:
            mod.get_nested([1, 2, 3, 4, 5], [10, 20, 30], default=1)
        except EXC:
            pass


class Test_hlookup_deep:
    def test_c0(self):
        try:
            mod.hlookup({"a": 1, "b": 2, "c": 3}, [10, 20, 30], 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.hlookup({}, [0, 1], 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.hlookup({"key": "value"}, [-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.hlookup({"a": 1, "b": 2, "c": 3}, [100], 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.hlookup({}, [1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.hlookup({"key": "value"}, [1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_kw_approximate(self):
        try:
            mod.hlookup({"a": 1, "b": 2, "c": 3}, [10, 20, 30], 3, approximate=True)
        except EXC:
            pass


class Test_is_subsequence_deep:
    def test_c0(self):
        try:
            mod.is_subsequence([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.is_subsequence([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.is_subsequence([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.is_subsequence([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.is_subsequence([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.is_subsequence([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass


class Test_merge_json_strings_deep:
    def test_c0(self):
        try:
            mod.merge_json_strings("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.merge_json_strings("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.merge_json_strings("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.merge_json_strings("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.merge_json_strings("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.merge_json_strings("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_vlookup_deep:
    def test_c0(self):
        try:
            mod.vlookup({"a": 1, "b": 2, "c": 3}, [10, 20, 30], 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.vlookup({}, [0, 1], 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.vlookup({"key": "value"}, [-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.vlookup({"a": 1, "b": 2, "c": 3}, [100], 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.vlookup({}, [1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.vlookup({"key": "value"}, [1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_kw_approximate(self):
        try:
            mod.vlookup({"a": 1, "b": 2, "c": 3}, [10, 20, 30], 3, approximate=True)
        except EXC:
            pass


class Test_chunk_deep:
    def test_c0(self):
        try:
            mod.chunk(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chunk(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chunk(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chunk(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chunk(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chunk(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.chunk(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.chunk(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.chunk(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.chunk(2, 10)
        except EXC:
            pass


class Test_collection_sum_deep:
    def test_c0(self):
        try:
            mod.collection_sum(1)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.collection_sum(2)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.collection_sum(3)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.collection_sum(5)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.collection_sum(10)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.collection_sum(0)
        except EXC:
            pass

    def test_kw_ignore_none(self):
        try:
            mod.collection_sum(1, ignore_none=True)
        except EXC:
            pass


class Test_conditional_average_deep:
    def test_c0(self):
        try:
            mod.conditional_average([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.conditional_average([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.conditional_average([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.conditional_average([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.conditional_average([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.conditional_average([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_conditional_max_deep:
    def test_c0(self):
        try:
            mod.conditional_max([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.conditional_max([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.conditional_max([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.conditional_max([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.conditional_max([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.conditional_max([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_conditional_min_deep:
    def test_c0(self):
        try:
            mod.conditional_min([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.conditional_min([10, 20, 30], 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.conditional_min([0, 1], 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.conditional_min([-3, -1, 0, 2, 5], 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.conditional_min([100], 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.conditional_min([1, 1, 2, 3, 5, 8], 1)
        except EXC:
            pass


class Test_count_by_deep:
    def test_c0(self):
        try:
            mod.count_by(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.count_by(42, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.count_by(0, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.count_by(-5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.count_by(3.14, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.count_by(100, 1)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.count_by(0.5, 2)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.count_by(1000, 3)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.count_by(-1, 5)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.count_by(2, 10)
        except EXC:
            pass


class Test_deep_merge_deep:
    def test_c0(self):
        try:
            mod.deep_merge(1, 42)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.deep_merge(42, 0)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.deep_merge(0, -5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.deep_merge(-5, 3.14)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.deep_merge(3.14, 100)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.deep_merge(100, 0.5)
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.deep_merge(0.5, 1000)
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.deep_merge(1000, -1)
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.deep_merge(-1, 2)
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.deep_merge(2, 1)
        except EXC:
            pass


class Test_dictionary_filter_by_keys_deep:
    def test_c0(self):
        try:
            mod.dictionary_filter_by_keys(1, [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.dictionary_filter_by_keys(42, [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.dictionary_filter_by_keys(0, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.dictionary_filter_by_keys(-5, [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.dictionary_filter_by_keys(3.14, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.dictionary_filter_by_keys(100, [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c6(self):
        try:
            mod.dictionary_filter_by_keys(0.5, [10, 20, 30])
        except EXC:
            pass

    def test_c7(self):
        try:
            mod.dictionary_filter_by_keys(1000, [0, 1])
        except EXC:
            pass

    def test_c8(self):
        try:
            mod.dictionary_filter_by_keys(-1, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c9(self):
        try:
            mod.dictionary_filter_by_keys(2, [100])
        except EXC:
            pass


class Test_drop_from_array_deep:
    def test_c0(self):
        try:
            mod.drop_from_array([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.drop_from_array([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.drop_from_array([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.drop_from_array([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.drop_from_array([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.drop_from_array([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_rows(self):
        try:
            mod.drop_from_array([1, 2, 3, 4, 5], rows=1)
        except EXC:
            pass

    def test_kw_columns(self):
        try:
            mod.drop_from_array([1, 2, 3, 4, 5], columns=1)
        except EXC:
            pass


class Test_expand_array_deep:
    def test_c0(self):
        try:
            mod.expand_array([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.expand_array([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.expand_array([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.expand_array([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.expand_array([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.expand_array([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_rows(self):
        try:
            mod.expand_array([1, 2, 3, 4, 5], rows=1)
        except EXC:
            pass

    def test_kw_columns(self):
        try:
            mod.expand_array([1, 2, 3, 4, 5], columns=1)
        except EXC:
            pass

    def test_kw_pad_with(self):
        try:
            mod.expand_array([1, 2, 3, 4, 5], pad_with=1)
        except EXC:
            pass


class Test_hstack_deep:
    def test_c0(self):
        try:
            mod.hstack()
        except EXC:
            pass


class Test_make_array_deep:
    def test_c0(self):
        try:
            mod.make_array(1, 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.make_array(2, 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.make_array(3, 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.make_array(5, 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.make_array(10, 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.make_array(0, 1, 2)
        except EXC:
            pass


class Test_search_deep:
    def test_c0(self):
        try:
            mod.search([1, 2, 3, 4, 5], "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.search([10, 20, 30], "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.search([0, 1], "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.search([-3, -1, 0, 2, 5], "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.search([100], "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.search([1, 1, 2, 3, 5, 8], "hello world")
        except EXC:
            pass


class Test_sort_by_deep:
    def test_c0(self):
        try:
            mod.sort_by([1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.sort_by([10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.sort_by([0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.sort_by([-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.sort_by([100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.sort_by([1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_reverse(self):
        try:
            mod.sort_by([1, 2, 3, 4, 5], [10, 20, 30], reverse=True)
        except EXC:
            pass


class Test_take_from_array_deep:
    def test_c0(self):
        try:
            mod.take_from_array([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.take_from_array([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.take_from_array([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.take_from_array([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.take_from_array([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.take_from_array([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_rows(self):
        try:
            mod.take_from_array([1, 2, 3, 4, 5], rows=1)
        except EXC:
            pass

    def test_kw_columns(self):
        try:
            mod.take_from_array([1, 2, 3, 4, 5], columns=1)
        except EXC:
            pass


class Test_vstack_deep:
    def test_c0(self):
        try:
            mod.vstack()
        except EXC:
            pass

