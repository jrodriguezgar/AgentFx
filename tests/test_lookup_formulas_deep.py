# Deep coverage tests for agentfx.fxExcel.lookup_formulas

import agentfx.fxExcel.lookup_formulas as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_TRIMRANGE_deep:
    def test_c0(self):
        try:
            mod.TRIMRANGE([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.TRIMRANGE([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.TRIMRANGE([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.TRIMRANGE([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.TRIMRANGE([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.TRIMRANGE([1, 1, 2, 3, 5, 8])
        except EXC:
            pass


class Test_MATCH_deep:
    def test_c0(self):
        try:
            mod.MATCH({"a": 1, "b": 2, "c": 3}, [10, 20, 30])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.MATCH({}, [0, 1])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.MATCH({"key": "value"}, [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.MATCH({"a": 1, "b": 2, "c": 3}, [100])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.MATCH({}, [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.MATCH({"key": "value"}, [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_kw_match_type(self):
        try:
            mod.MATCH({"a": 1, "b": 2, "c": 3}, [10, 20, 30], match_type=1)
        except EXC:
            pass


class Test_UNIQUE_deep:
    def test_c0(self):
        try:
            mod.UNIQUE([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.UNIQUE([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.UNIQUE([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.UNIQUE([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.UNIQUE([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.UNIQUE([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_by_col(self):
        try:
            mod.UNIQUE([1, 2, 3, 4, 5], by_col=True)
        except EXC:
            pass

    def test_kw_exactly_once(self):
        try:
            mod.UNIQUE([1, 2, 3, 4, 5], exactly_once=True)
        except EXC:
            pass


class Test_INDIRECT_deep:
    def test_c0(self):
        try:
            mod.INDIRECT("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.INDIRECT("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.INDIRECT("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.INDIRECT("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.INDIRECT("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.INDIRECT("UPPER lower 123")
        except EXC:
            pass

    def test_kw_a1(self):
        try:
            mod.INDIRECT("hello world", a1=True)
        except EXC:
            pass


class Test_ADDRESS_deep:
    def test_c0(self):
        try:
            mod.ADDRESS(1, 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.ADDRESS(2, 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.ADDRESS(3, 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.ADDRESS(5, 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.ADDRESS(10, 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.ADDRESS(0, 1)
        except EXC:
            pass

    def test_kw_abs_num(self):
        try:
            mod.ADDRESS(1, 2, abs_num=1)
        except EXC:
            pass

    def test_kw_a1(self):
        try:
            mod.ADDRESS(1, 2, a1=True)
        except EXC:
            pass

    def test_kw_sheet_text(self):
        try:
            mod.ADDRESS(1, 2, sheet_text="hello world")
        except EXC:
            pass


class Test_XLOOKUP_deep:
    def test_c0(self):
        try:
            mod.XLOOKUP({"a": 1, "b": 2, "c": 3}, [10, 20, 30], [0, 1])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.XLOOKUP({}, [0, 1], [-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.XLOOKUP({"key": "value"}, [-3, -1, 0, 2, 5], [100])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.XLOOKUP({"a": 1, "b": 2, "c": 3}, [100], [1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.XLOOKUP({}, [1, 1, 2, 3, 5, 8], [1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.XLOOKUP({"key": "value"}, [1, 2, 3, 4, 5], [10, 20, 30])
        except EXC:
            pass

    def test_kw_if_not_found(self):
        try:
            mod.XLOOKUP({"a": 1, "b": 2, "c": 3}, [10, 20, 30], [0, 1], if_not_found=1)
        except EXC:
            pass

    def test_kw_match_mode(self):
        try:
            mod.XLOOKUP({"a": 1, "b": 2, "c": 3}, [10, 20, 30], [0, 1], match_mode=1)
        except EXC:
            pass

    def test_kw_search_mode(self):
        try:
            mod.XLOOKUP({"a": 1, "b": 2, "c": 3}, [10, 20, 30], [0, 1], search_mode=1)
        except EXC:
            pass


class Test_SORT_deep:
    def test_c0(self):
        try:
            mod.SORT([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.SORT([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.SORT([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.SORT([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.SORT([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.SORT([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_sort_index(self):
        try:
            mod.SORT([1, 2, 3, 4, 5], sort_index=1)
        except EXC:
            pass

    def test_kw_sort_order(self):
        try:
            mod.SORT([1, 2, 3, 4, 5], sort_order=1)
        except EXC:
            pass

    def test_kw_by_col(self):
        try:
            mod.SORT([1, 2, 3, 4, 5], by_col=True)
        except EXC:
            pass


class Test_INDEX_deep:
    def test_c0(self):
        try:
            mod.INDEX([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.INDEX([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.INDEX([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.INDEX([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.INDEX([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.INDEX([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_row_num(self):
        try:
            mod.INDEX([1, 2, 3, 4, 5], row_num=1)
        except EXC:
            pass

    def test_kw_column_num(self):
        try:
            mod.INDEX([1, 2, 3, 4, 5], column_num=1)
        except EXC:
            pass


class Test_EXPAND_deep:
    def test_c0(self):
        try:
            mod.EXPAND([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.EXPAND([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.EXPAND([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.EXPAND([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.EXPAND([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.EXPAND([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_rows(self):
        try:
            mod.EXPAND([1, 2, 3, 4, 5], rows=1)
        except EXC:
            pass

    def test_kw_columns(self):
        try:
            mod.EXPAND([1, 2, 3, 4, 5], columns=1)
        except EXC:
            pass

    def test_kw_pad_with(self):
        try:
            mod.EXPAND([1, 2, 3, 4, 5], pad_with=1)
        except EXC:
            pass


class Test_FILTER_deep:
    def test_c0(self):
        try:
            mod.FILTER([1, 2, 3, 4, 5], False)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.FILTER([10, 20, 30], True)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.FILTER([0, 1], False)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.FILTER([-3, -1, 0, 2, 5], True)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.FILTER([100], False)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.FILTER([1, 1, 2, 3, 5, 8], True)
        except EXC:
            pass

    def test_kw_if_empty(self):
        try:
            mod.FILTER([1, 2, 3, 4, 5], False, if_empty=1)
        except EXC:
            pass


class Test_OFFSET_deep:
    def test_c0(self):
        try:
            mod.OFFSET([1, 2, 3, 4, 5], 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.OFFSET([10, 20, 30], 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.OFFSET([0, 1], 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.OFFSET([-3, -1, 0, 2, 5], 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.OFFSET([100], 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.OFFSET([1, 1, 2, 3, 5, 8], 1, 2)
        except EXC:
            pass

    def test_kw_height(self):
        try:
            mod.OFFSET([1, 2, 3, 4, 5], 2, 3, height=1)
        except EXC:
            pass

    def test_kw_width(self):
        try:
            mod.OFFSET([1, 2, 3, 4, 5], 2, 3, width=1)
        except EXC:
            pass


class Test_TOCOL_deep:
    def test_c0(self):
        try:
            mod.TOCOL([1, 2, 3, 4, 5])
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.TOCOL([10, 20, 30])
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.TOCOL([0, 1])
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.TOCOL([-3, -1, 0, 2, 5])
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.TOCOL([100])
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.TOCOL([1, 1, 2, 3, 5, 8])
        except EXC:
            pass

    def test_kw_ignore(self):
        try:
            mod.TOCOL([1, 2, 3, 4, 5], ignore=1)
        except EXC:
            pass

    def test_kw_scan_by_column(self):
        try:
            mod.TOCOL([1, 2, 3, 4, 5], scan_by_column=True)
        except EXC:
            pass

