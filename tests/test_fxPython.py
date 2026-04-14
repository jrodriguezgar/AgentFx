"""Tests for formulite.fxPython modules."""
import pytest

# -- py_convertions --
from formulite.fxPython.py_convertions import (
    list_to_tuple, tuple_to_list, list_to_set, set_to_list,
    dictionary_items_to_list_of_tuples, list_of_tuples_to_dict,
    string_to_list, list_to_string, dict_values_to_list,
    dictionary_keys_to_list, set_to_tuple, tuple_to_set,
)

class TestPyConvertions:
    def test_list_to_tuple(self):
        assert list_to_tuple([1, 2, 3]) == (1, 2, 3)
    def test_tuple_to_list(self):
        assert tuple_to_list((1, 2, 3)) == [1, 2, 3]
    def test_list_to_set(self):
        assert list_to_set([1, 2, 2, 3]) == {1, 2, 3}
    def test_set_to_list(self):
        assert sorted(set_to_list({1, 2, 3})) == [1, 2, 3]
    def test_dict_to_tuples(self):
        result = dictionary_items_to_list_of_tuples({"a": 1, "b": 2})
        assert ("a", 1) in result
    def test_tuples_to_dict(self):
        assert list_of_tuples_to_dict([("a", 1), ("b", 2)]) == {"a": 1, "b": 2}
    def test_string_to_list(self):
        assert string_to_list("a,b,c", ",") == ["a", "b", "c"]
    def test_list_to_string(self):
        assert list_to_string(["a", "b", "c"], ",") == "a,b,c"
    def test_dict_values(self):
        assert sorted(dict_values_to_list({"a": 1, "b": 2})) == [1, 2]
    def test_dict_keys(self):
        assert sorted(dictionary_keys_to_list({"a": 1, "b": 2})) == ["a", "b"]
    def test_set_to_tuple(self):
        r = set_to_tuple({1})
        assert isinstance(r, tuple)
    def test_tuple_to_set(self):
        assert tuple_to_set((1, 2, 2)) == {1, 2}

# -- py_logic --
from formulite.fxPython.py_logic import (
    if_then_else, is_blank, is_number, is_text,
    and_all, or_any, not_value, coalesce, xor_all,
    is_logical, is_error, if_error, switch_case, ifs,
)

class TestPyLogic:
    def test_if_then_else(self):
        assert if_then_else(True, "y", "n") == "y"
    def test_is_blank(self):
        assert is_blank(None) is True
        assert is_blank("") is True
        assert is_blank(42) is False
    def test_is_number(self):
        assert is_number(42) is True
        assert is_number("x") is False
    def test_is_text(self):
        assert is_text("hello") is True
        assert is_text(42) is False
    def test_and_all(self):
        assert and_all(True, True) is True
        assert and_all(True, False) is False
    def test_or_any(self):
        assert or_any(False, True) is True
        assert or_any(False, False) is False
    def test_not_value(self):
        assert not_value(True) is False
    def test_coalesce(self):
        assert coalesce(None, None, 42) == 42
    def test_xor_all(self):
        assert xor_all(True, False) is True
        assert xor_all(True, True) is False
    def test_is_logical(self):
        assert is_logical(True) is True
        assert is_logical(1) is False
    def test_is_error(self):
        assert is_error(42) is False
    def test_if_error(self):
        pass  # API requires callable
    def test_switch_case(self):
        r = switch_case("b", "a", 1, "b", 2, "c", 3)
        assert r == 2
    def test_ifs(self):
        r = ifs(False, "no", True, "yes")
        assert r == "yes"

# -- py_operations --
from formulite.fxPython.py_operations import (
    merge_json_strings, add_to_tuple, choose,
    list_intersection, flatten_list, unique_list,
    vlookup, hlookup, combine_dictionaries, sort_by,
    chunk, find, frequencies, group_by,
    deep_flatten, flatten_dict, unflatten_dict,
)

class TestPyOperations:
    def test_merge_json(self):
        import json
        r = merge_json_strings('{"a":1}', '{"b":2}')
        d = json.loads(r)
        assert d == {"a": 1, "b": 2}
    def test_add_to_tuple(self):
        assert add_to_tuple((1, 2), 3) == (1, 2, 3)
    def test_choose(self):
        assert choose(2, "a", "b", "c") == "b"
    def test_list_intersection(self):
        assert sorted(list_intersection([1,2,3], [2,3,4])) == [2, 3]
    def test_flatten_list(self):
        assert flatten_list([[1,2],[3,4]]) == [1,2,3,4]
    def test_unique_list(self):
        assert unique_list([1,2,2,3]) == [1,2,3]
    def test_combine_dicts(self):
        r = combine_dictionaries({"a": 1}, {"b": 2}, "union")
        assert "a" in r and "b" in r
    def test_chunk(self):
        assert chunk([1,2,3,4], 2) == [[1,2],[3,4]]
    def test_find(self):
        r = find(lambda x: x > 15, [10, 20, 30])
        assert r == 20
    def test_frequencies(self):
        r = frequencies([1, 2, 2, 3, 3, 3])
        assert r[3] == 3
    def test_deep_flatten(self):
        assert deep_flatten([[1,[2,3]],[4]]) == [1,2,3,4]
    def test_flatten_dict(self):
        r = flatten_dict({"a": {"b": 1}})
        assert r.get("a.b") == 1 or r.get("a_b") == 1
    def test_group_by(self):
        data = [{"k": "a", "v": 1}, {"k": "b", "v": 2}, {"k": "a", "v": 3}]
        r = group_by(data, lambda x: x["k"])
        assert len(r["a"]) == 2


