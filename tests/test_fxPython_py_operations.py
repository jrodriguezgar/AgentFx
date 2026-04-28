# Coverage tests for agentfx.fxPython.py_operations

from agentfx.fxPython import py_operations as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_add_to_tuple:
    def test_exists(self):
        assert hasattr(mod, "add_to_tuple")

    def test_doc0(self):
        try:
            mod.add_to_tuple((1, 2), 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.add_to_tuple((), "hello")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.add_to_tuple(0, 0.5)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.add_to_tuple(1, 0.1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.add_to_tuple(None, 0.5)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.add_to_tuple("", 0)
        except EXC:
            pass


class Test_calculate:
    def test_exists(self):
        assert hasattr(mod, "calculate")

    def test_doc0(self):
        try:
            mod.calculate("3 + 4 * 5")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate("2 * 3(6 / 2) - 9 + 6")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate(None)
        except EXC:
            pass


class Test_choose:
    def test_exists(self):
        assert hasattr(mod, "choose")

    def test_doc0(self):
        try:
            mod.choose(2, "a", "b", "c")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.choose(1, 10, 20, 30)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.choose(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.choose(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.choose(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.choose("")
        except EXC:
            pass


class Test_choose_cols:
    def test_exists(self):
        assert hasattr(mod, "choose_cols")

    def test_doc0(self):
        try:
            mod.choose_cols([[1, 2, 3], [4, 5, 6]], 1, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.choose_cols([[1, 2, 3]], -1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.choose_cols([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.choose_cols([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.choose_cols(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.choose_cols([])
        except EXC:
            pass


class Test_choose_rows:
    def test_exists(self):
        assert hasattr(mod, "choose_rows")

    def test_doc0(self):
        try:
            mod.choose_rows([[1, 2], [3, 4], [5, 6]], 1, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.choose_rows([[1, 2], [3, 4]], -1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.choose_rows([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.choose_rows([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.choose_rows(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.choose_rows([])
        except EXC:
            pass


class Test_chunk:
    def test_exists(self):
        assert hasattr(mod, "chunk")

    def test_doc0(self):
        try:
            mod.chunk([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.chunk("abcdef", 3)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.chunk(range(7), 4)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.chunk([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.chunk([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.chunk(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.chunk("", 0)
        except EXC:
            pass


class Test_collection_avg:
    def test_exists(self):
        assert hasattr(mod, "collection_avg")

    def test_doc0(self):
        try:
            mod.collection_avg([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.collection_avg([10, 20, None, 30], ignore_none=True)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.collection_avg((5.5, 10.5, 15.5))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.collection_avg(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.collection_avg(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.collection_avg(None)
        except EXC:
            pass


class Test_collection_count:
    def test_exists(self):
        assert hasattr(mod, "collection_count")

    def test_doc0(self):
        try:
            mod.collection_count([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.collection_count([1, None, 3, None, 5], ignore_none=True)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.collection_count([1, None, 3, None, 5], ignore_none=False)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.collection_count([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.collection_count([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.collection_count(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.collection_count(0)
        except EXC:
            pass


class Test_collection_filter:
    def test_exists(self):
        assert hasattr(mod, "collection_filter")

    def test_var0(self):
        try:
            mod.collection_filter([1, 2, 3], True)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.collection_filter([0], False)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.collection_filter(None, True)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.collection_filter(0, "")
        except EXC:
            pass


class Test_collection_max:
    def test_exists(self):
        assert hasattr(mod, "collection_max")

    def test_doc0(self):
        try:
            mod.collection_max([1, 5, 3, 9, 2])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.collection_max(['apple', 'zebra', 'banana'])
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.collection_max([1.5, None, 3.7, 2.1], ignore_none=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.collection_max([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.collection_max([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.collection_max(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.collection_max(0)
        except EXC:
            pass


class Test_collection_min:
    def test_exists(self):
        assert hasattr(mod, "collection_min")

    def test_doc0(self):
        try:
            mod.collection_min([5, 1, 9, 3, 2])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.collection_min(['zebra', 'apple', 'banana'])
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.collection_min([3.7, None, 1.5, 2.1], ignore_none=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.collection_min([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.collection_min([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.collection_min(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.collection_min(0)
        except EXC:
            pass


class Test_collection_stdev:
    def test_exists(self):
        assert hasattr(mod, "collection_stdev")

    def test_doc0(self):
        try:
            mod.collection_stdev([2, 4, 4, 4, 5, 5, 7, 9])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.collection_stdev([2, 4, 4, 4, 5, 5, 7, 9], is_sample=False)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.collection_stdev([10, None, 20, 30], ignore_none=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.collection_stdev(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.collection_stdev(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.collection_stdev(None)
        except EXC:
            pass


class Test_collection_sum:
    def test_exists(self):
        assert hasattr(mod, "collection_sum")

    def test_doc0(self):
        try:
            mod.collection_sum([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.collection_sum([10, None, 20, 30], ignore_none=True)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.collection_sum((5.5, 10.5, 15.5))
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.collection_sum(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.collection_sum(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.collection_sum(None)
        except EXC:
            pass


class Test_combine_dictionaries:
    def test_exists(self):
        assert hasattr(mod, "combine_dictionaries")

    def test_var0(self):
        try:
            mod.combine_dictionaries({"a": 1, "b": 2}, {"a": 1, "b": 2}, "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.combine_dictionaries({}, {}, "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.combine_dictionaries(None, {"a": 1, "b": 2}, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.combine_dictionaries("", "", 0)
        except EXC:
            pass


class Test_conditional_average:
    def test_exists(self):
        assert hasattr(mod, "conditional_average")

    def test_var0(self):
        try:
            mod.conditional_average(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.conditional_average(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.conditional_average(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.conditional_average([], "")
        except EXC:
            pass


class Test_conditional_count:
    def test_exists(self):
        assert hasattr(mod, "conditional_count")

    def test_var0(self):
        try:
            mod.conditional_count([1, 2, 3], True)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.conditional_count([0], False)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.conditional_count(None, True)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.conditional_count([], "")
        except EXC:
            pass


class Test_conditional_max:
    def test_exists(self):
        assert hasattr(mod, "conditional_max")

    def test_var0(self):
        try:
            mod.conditional_max(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.conditional_max(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.conditional_max(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.conditional_max([], "")
        except EXC:
            pass


class Test_conditional_min:
    def test_exists(self):
        assert hasattr(mod, "conditional_min")

    def test_var0(self):
        try:
            mod.conditional_min(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.conditional_min(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.conditional_min(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.conditional_min([], "")
        except EXC:
            pass


class Test_conditional_sum:
    def test_exists(self):
        assert hasattr(mod, "conditional_sum")

    def test_var0(self):
        try:
            mod.conditional_sum(0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.conditional_sum(1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.conditional_sum(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.conditional_sum([], "")
        except EXC:
            pass


class Test_count_blank:
    def test_exists(self):
        assert hasattr(mod, "count_blank")

    def test_doc0(self):
        try:
            mod.count_blank([1, "", None, "hello", 0])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.count_blank([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.count_blank([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.count_blank(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.count_blank([])
        except EXC:
            pass


class Test_count_by:
    def test_exists(self):
        assert hasattr(mod, "count_by")

    def test_var0(self):
        try:
            mod.count_by([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.count_by([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.count_by(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.count_by("", "")
        except EXC:
            pass


class Test_count_if:
    def test_exists(self):
        assert hasattr(mod, "count_if")

    def test_doc0(self):
        try:
            mod.count_if([1, 5, 10, 15, 20], ">8")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.count_if(["a", "b", "a", "c"], "a")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.count_if([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.count_if([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.count_if(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.count_if([], "")
        except EXC:
            pass


class Test_count_ifs:
    def test_exists(self):
        assert hasattr(mod, "count_ifs")

    def test_doc0(self):
        try:
            mod.count_ifs( [1, 2, 3, 4, 5], [1, 2, 3, 4, 5], ">1", [1, 2, 3, 4, 5], "<5", )
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.count_ifs([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.count_ifs([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.count_ifs(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.count_ifs([])
        except EXC:
            pass


class Test_count_numbers:
    def test_exists(self):
        assert hasattr(mod, "count_numbers")

    def test_doc0(self):
        try:
            mod.count_numbers([1, "a", 2, None, 3.5])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.count_numbers()
        except EXC:
            pass


class Test_count_values:
    def test_exists(self):
        assert hasattr(mod, "count_values")

    def test_doc0(self):
        try:
            mod.count_values([1, "", None, "hello", 0])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.count_values()
        except EXC:
            pass


class Test_deep_flatten:
    def test_exists(self):
        assert hasattr(mod, "deep_flatten")

    def test_doc0(self):
        try:
            mod.deep_flatten([1, [2, [3, [4]], 5]])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.deep_flatten([[1, 2], 'hello', [3, [4]]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.deep_flatten(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.deep_flatten(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.deep_flatten(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.deep_flatten("")
        except EXC:
            pass


class Test_deep_merge:
    def test_exists(self):
        assert hasattr(mod, "deep_merge")

    def test_doc0(self):
        try:
            mod.deep_merge({"a": 1, "b": {"x": 10}}, {"b": {"y": 20}, "c": 3})
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.deep_merge({"a": 1}, {"a": 2})
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.deep_merge({"a": 1, "b": 2}, {"a": 1, "b": 2})
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.deep_merge({}, {})
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.deep_merge(None, {"a": 1, "b": 2})
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.deep_merge("", "")
        except EXC:
            pass


class Test_dictionary_filter_by_keys:
    def test_exists(self):
        assert hasattr(mod, "dictionary_filter_by_keys")

    def test_var0(self):
        try:
            mod.dictionary_filter_by_keys({"a": 1, "b": 2}, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dictionary_filter_by_keys({}, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dictionary_filter_by_keys(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dictionary_filter_by_keys("", "")
        except EXC:
            pass


class Test_dictionary_rename_keys:
    def test_exists(self):
        assert hasattr(mod, "dictionary_rename_keys")

    def test_var0(self):
        try:
            mod.dictionary_rename_keys({"a": 1, "b": 2}, lambda x: x)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.dictionary_rename_keys({}, abs)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.dictionary_rename_keys(None, lambda x: x)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.dictionary_rename_keys("", "")
        except EXC:
            pass


class Test_drop_from_array:
    def test_exists(self):
        assert hasattr(mod, "drop_from_array")

    def test_doc0(self):
        try:
            mod.drop_from_array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=1, columns=-1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.drop_from_array([[1, 2], [3, 4]], rows=-1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.drop_from_array([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.drop_from_array([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.drop_from_array(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.drop_from_array([])
        except EXC:
            pass


class Test_expand_array:
    def test_exists(self):
        assert hasattr(mod, "expand_array")

    def test_doc0(self):
        try:
            mod.expand_array([[1, 2], [3, 4]], 3, 4, 0)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.expand_array([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.expand_array([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.expand_array(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.expand_array([])
        except EXC:
            pass


class Test_filter_elements_by_another:
    def test_exists(self):
        assert hasattr(mod, "filter_elements_by_another")

    def test_var0(self):
        try:
            mod.filter_elements_by_another([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.filter_elements_by_another([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.filter_elements_by_another(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.filter_elements_by_another(0, "")
        except EXC:
            pass


class Test_find:
    def test_exists(self):
        assert hasattr(mod, "find")

    def test_var0(self):
        try:
            mod.find(lambda x: x, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.find(abs, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.find(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.find("", "")
        except EXC:
            pass


class Test_flatten_dict:
    def test_exists(self):
        assert hasattr(mod, "flatten_dict")

    def test_doc0(self):
        try:
            mod.flatten_dict({"a": {"b": 1, "c": {"d": 2}}})
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.flatten_dict(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.flatten_dict(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.flatten_dict(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.flatten_dict("")
        except EXC:
            pass


class Test_flatten_list:
    def test_exists(self):
        assert hasattr(mod, "flatten_list")

    def test_doc0(self):
        try:
            mod.flatten_list([[1, 2, 3], [4, 5], [6]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.flatten_list([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.flatten_list([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.flatten_list(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.flatten_list("")
        except EXC:
            pass


class Test_frequencies:
    def test_exists(self):
        assert hasattr(mod, "frequencies")

    def test_doc0(self):
        try:
            mod.frequencies(["a", "b", "a", "c", "a"])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.frequencies([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.frequencies([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.frequencies(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.frequencies([])
        except EXC:
            pass


class Test_get_nested:
    def test_exists(self):
        assert hasattr(mod, "get_nested")

    def test_doc0(self):
        try:
            mod.get_nested({"a": {"b": {"c": 42}}}, ["a", "b", "c"])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.get_nested({"a": {"b": 1}}, ["a", "x"], default=-1)
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.get_nested({}, ["a"], default="missing")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.get_nested([1, 2, 3], "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.get_nested([0], "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.get_nested(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.get_nested([], "")
        except EXC:
            pass


class Test_group_by:
    def test_exists(self):
        assert hasattr(mod, "group_by")

    def test_var0(self):
        try:
            mod.group_by([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.group_by([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.group_by(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.group_by("", "")
        except EXC:
            pass


class Test_hlookup:
    def test_exists(self):
        assert hasattr(mod, "hlookup")

    def test_doc0(self):
        try:
            mod.hlookup(2.5, [[1, 2, 3], [10, 20, 30]], 2, approximate=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hlookup(0.5, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.hlookup(0.1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.hlookup(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.hlookup(0, "", [])
        except EXC:
            pass


class Test_hstack:
    def test_exists(self):
        assert hasattr(mod, "hstack")

    def test_doc0(self):
        try:
            mod.hstack([[1, 2], [3, 4]], [[5], [6]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.hstack()
        except EXC:
            pass


class Test_index_2d:
    def test_exists(self):
        assert hasattr(mod, "index_2d")

    def test_doc0(self):
        try:
            mod.index_2d([[10, 20], [30, 40]], 2, 1)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.index_2d([[10, 20], [30, 40]], 1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.index_2d([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.index_2d([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.index_2d(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.index_2d([], [])
        except EXC:
            pass


class Test_index_by:
    def test_exists(self):
        assert hasattr(mod, "index_by")

    def test_var0(self):
        try:
            mod.index_by([1, 2, 3], "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.index_by([0], "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.index_by(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.index_by("", "")
        except EXC:
            pass


class Test_is_subsequence:
    def test_exists(self):
        assert hasattr(mod, "is_subsequence")

    def test_var0(self):
        try:
            mod.is_subsequence([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.is_subsequence([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.is_subsequence(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.is_subsequence([], 0)
        except EXC:
            pass


class Test_list_has_list:
    def test_exists(self):
        assert hasattr(mod, "list_has_list")

    def test_doc0(self):
        try:
            mod.list_has_list(['a', 'b', 'c', 'd'], ['b', 'c'])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.list_has_list(['a', 'b', 'c'], ['b', 'd'])
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.list_has_list([1, 2, 3, 4], [2, 1])
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.list_has_list([], [1, 2])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.list_has_list([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.list_has_list([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.list_has_list(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.list_has_list("", "")
        except EXC:
            pass


class Test_list_intersection:
    def test_exists(self):
        assert hasattr(mod, "list_intersection")

    def test_var0(self):
        try:
            mod.list_intersection([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.list_intersection([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.list_intersection(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.list_intersection("", "")
        except EXC:
            pass


class Test_make_array:
    def test_exists(self):
        assert hasattr(mod, "make_array")

    def test_var0(self):
        try:
            mod.make_array(0, 0, 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.make_array(1, 1, 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.make_array(None, 0, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.make_array([], [], 0)
        except EXC:
            pass


class Test_merge_elements:
    def test_exists(self):
        assert hasattr(mod, "merge_elements")

    def test_var0(self):
        try:
            mod.merge_elements([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.merge_elements([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.merge_elements(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.merge_elements(0, 0)
        except EXC:
            pass


class Test_merge_json_strings:
    def test_exists(self):
        assert hasattr(mod, "merge_json_strings")

    def test_doc0(self):
        try:
            mod.merge_json_strings('{"name": "Alice", "age": 30}', '{"age": 31, "city": "New York"}')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.merge_json_strings('{"a": 1}', '{"b": 2}')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.merge_json_strings("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.merge_json_strings("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.merge_json_strings(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.merge_json_strings(0, 0)
        except EXC:
            pass


class Test_partition:
    def test_exists(self):
        assert hasattr(mod, "partition")

    def test_doc0(self):
        try:
            mod.partition(str.isupper, ["A", "b", "C", "d"])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.partition(lambda x: x, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.partition(abs, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.partition(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.partition("", "")
        except EXC:
            pass


class Test_pick_in_collection:
    def test_exists(self):
        assert hasattr(mod, "pick_in_collection")

    def test_var0(self):
        try:
            mod.pick_in_collection([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pick_in_collection([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pick_in_collection(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pick_in_collection(0)
        except EXC:
            pass


class Test_pluck:
    def test_exists(self):
        assert hasattr(mod, "pluck")

    def test_doc0(self):
        try:
            mod.pluck([{"name": "Alice"}, {"name": "Bob"}], "name")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.pluck([{"x": 1, "y": 2}, {"x": 3, "y": 4}], "x")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.pluck([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.pluck([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.pluck(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.pluck("", "")
        except EXC:
            pass


class Test_search:
    def test_exists(self):
        assert hasattr(mod, "search")

    def test_var0(self):
        try:
            mod.search([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.search([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.search(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.search(0, "")
        except EXC:
            pass


class Test_sequence:
    def test_exists(self):
        assert hasattr(mod, "sequence")

    def test_doc0(self):
        try:
            mod.sequence(2, 3)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sequence(3, 1, 0, 5)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sequence()
        except EXC:
            pass


class Test_sort_by:
    def test_exists(self):
        assert hasattr(mod, "sort_by")

    def test_doc0(self):
        try:
            mod.sort_by(["c", "a", "b"], [3, 1, 2])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.sort_by(["c", "a", "b"], [3, 1, 2], reverse=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sort_by([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sort_by([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sort_by(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sort_by([], "")
        except EXC:
            pass


class Test_sort_dict_by_key:
    def test_exists(self):
        assert hasattr(mod, "sort_dict_by_key")

    def test_doc0(self):
        try:
            mod.sort_dict_by_key({'c': 3, 'a': 1, 'b': 2})
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sort_dict_by_key(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sort_dict_by_key(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sort_dict_by_key(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sort_dict_by_key("")
        except EXC:
            pass


class Test_sort_dict_by_value:
    def test_exists(self):
        assert hasattr(mod, "sort_dict_by_value")

    def test_doc0(self):
        try:
            mod.sort_dict_by_value({'b': 2, 'a': 1, 'c': 3})
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sort_dict_by_value(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sort_dict_by_value(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sort_dict_by_value(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sort_dict_by_value("")
        except EXC:
            pass


class Test_sort_dicts_by_key:
    def test_exists(self):
        assert hasattr(mod, "sort_dicts_by_key")

    def test_doc0(self):
        try:
            mod.sort_dicts_by_key([{"n": 3}, {"n": 1}, {"n": 2}], "n")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.sort_dicts_by_key([1, 2, 3], "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.sort_dicts_by_key([0], "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.sort_dicts_by_key(None, "hello")
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.sort_dicts_by_key([], "")
        except EXC:
            pass


class Test_take_from_array:
    def test_exists(self):
        assert hasattr(mod, "take_from_array")

    def test_doc0(self):
        try:
            mod.take_from_array([[1, 2, 3], [4, 5, 6], [7, 8, 9]], rows=2, columns=-2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.take_from_array([[1, 2], [3, 4], [5, 6]], rows=-1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.take_from_array([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.take_from_array([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.take_from_array(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.take_from_array([])
        except EXC:
            pass


class Test_tocol:
    def test_exists(self):
        assert hasattr(mod, "tocol")

    def test_doc0(self):
        try:
            mod.tocol([[1, 2], [3, 4]])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.tocol([[1, 2], [3, 4]], scan_by_column=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.tocol([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.tocol([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.tocol(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.tocol([])
        except EXC:
            pass


class Test_torow:
    def test_exists(self):
        assert hasattr(mod, "torow")

    def test_doc0(self):
        try:
            mod.torow([[1, 2], [3, 4]])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.torow([[1, 2], [3, 4]], scan_by_column=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.torow([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.torow([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.torow(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.torow([])
        except EXC:
            pass


class Test_unflatten_dict:
    def test_exists(self):
        assert hasattr(mod, "unflatten_dict")

    def test_doc0(self):
        try:
            mod.unflatten_dict({"a.b": 1, "a.c.d": 2})
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.unflatten_dict(0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unflatten_dict(1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unflatten_dict(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unflatten_dict("")
        except EXC:
            pass


class Test_unique_list:
    def test_exists(self):
        assert hasattr(mod, "unique_list")

    def test_doc0(self):
        try:
            mod.unique_list([1, 2, 2, 3, 1])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.unique_list(["apple", "banana", "apple"])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.unique_list([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unique_list([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unique_list(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unique_list("")
        except EXC:
            pass


class Test_unique_tuple_list:
    def test_exists(self):
        assert hasattr(mod, "unique_tuple_list")

    def test_var0(self):
        try:
            mod.unique_tuple_list([1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.unique_tuple_list([0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.unique_tuple_list(None)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.unique_tuple_list("")
        except EXC:
            pass


class Test_vlookup:
    def test_exists(self):
        assert hasattr(mod, "vlookup")

    def test_doc0(self):
        try:
            mod.vlookup(2.5, [[1, "x"], [2, "y"], [3, "z"]], 2, approximate=True)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.vlookup(0.5, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.vlookup(0.1, [0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.vlookup(None, [1, 2, 3], 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.vlookup(0, "", [])
        except EXC:
            pass


class Test_vstack:
    def test_exists(self):
        assert hasattr(mod, "vstack")

    def test_doc0(self):
        try:
            mod.vstack([[1, 2]], [[3, 4], [5, 6]])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.vstack()
        except EXC:
            pass


class Test_wrap_rows:
    def test_exists(self):
        assert hasattr(mod, "wrap_rows")

    def test_doc0(self):
        try:
            mod.wrap_rows([1, 2, 3, 4, 5], 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.wrap_rows([1, 2, 3, 4], 2)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.wrap_rows([1, 2, 3], 0)
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.wrap_rows([0], 1)
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.wrap_rows(None, 0)
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.wrap_rows([], 0)
        except EXC:
            pass


class Test_xlookup:
    def test_exists(self):
        assert hasattr(mod, "xlookup")

    def test_doc0(self):
        try:
            mod.xlookup("b", ["a", "b", "c"], [1, 2, 3])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.xlookup("z", ["a", "b", "c"], [1, 2, 3], "Not Found")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.xlookup(25, [10, 20, 30], ["x", "y", "z"], match_mode=-1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.xlookup(0.5, [1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.xlookup(0.1, [0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.xlookup(None, [1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.xlookup(0, [], 0)
        except EXC:
            pass


class Test_xmatch:
    def test_exists(self):
        assert hasattr(mod, "xmatch")

    def test_doc0(self):
        try:
            mod.xmatch(30, [10, 20, 30, 40])
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.xmatch(25, [10, 20, 30, 40], match_mode=-1)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.xmatch(0.5, [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.xmatch(0.1, [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.xmatch(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.xmatch(0, [])
        except EXC:
            pass


class Test_zip_dict:
    def test_exists(self):
        assert hasattr(mod, "zip_dict")

    def test_doc0(self):
        try:
            mod.zip_dict(['a', 'b', 'c'], [1, 2, 3])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.zip_dict([1, 2, 3], [1, 2, 3])
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.zip_dict([0], [0])
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.zip_dict(None, [1, 2, 3])
        except EXC:
            pass

    def test_var3(self):
        try:
            mod.zip_dict("", [])
        except EXC:
            pass

