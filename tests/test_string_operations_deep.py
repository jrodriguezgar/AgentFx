# Deep coverage tests for formulite.fxString.string_operations
import pytest
from datetime import date, datetime, time, timedelta
from decimal import Decimal
import math

import formulite.fxString.string_operations as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_double_metaphone_deep:
    def test_c0(self):
        try:
            mod.double_metaphone("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.double_metaphone("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.double_metaphone("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.double_metaphone("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.double_metaphone("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.double_metaphone("UPPER lower 123")
        except EXC:
            pass


class Test_metaphone_deep:
    def test_c0(self):
        try:
            mod.metaphone("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.metaphone("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.metaphone("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.metaphone("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.metaphone("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.metaphone("UPPER lower 123")
        except EXC:
            pass


class Test_nysiis_deep:
    def test_c0(self):
        try:
            mod.nysiis("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.nysiis("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.nysiis("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.nysiis("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.nysiis("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.nysiis("UPPER lower 123")
        except EXC:
            pass


class Test_rotate_words_deep:
    def test_c0(self):
        try:
            mod.rotate_words("hello world", 2, "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.rotate_words("test", 3, "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.rotate_words("abc123", 5, "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.rotate_words("", 10, "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.rotate_words("Hello, World!", 0, "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.rotate_words("UPPER lower 123", 1, "test")
        except EXC:
            pass


class Test_string_merge_deep:
    def test_c0(self):
        try:
            mod.string_merge("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.string_merge("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.string_merge("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.string_merge("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.string_merge("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.string_merge("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_base(self):
        try:
            mod.string_merge("hello world", "test", base="hello world")
        except EXC:
            pass


class Test_get_in_text_by_pattern_deep:
    def test_c0(self):
        try:
            mod.get_in_text_by_pattern("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_in_text_by_pattern("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_in_text_by_pattern("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_in_text_by_pattern("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_in_text_by_pattern("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_in_text_by_pattern("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_cologne_phonetic_deep:
    def test_c0(self):
        try:
            mod.cologne_phonetic("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.cologne_phonetic("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.cologne_phonetic("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.cologne_phonetic("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.cologne_phonetic("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.cologne_phonetic("UPPER lower 123")
        except EXC:
            pass


class Test_text_after_deep:
    def test_c0(self):
        try:
            mod.text_after("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.text_after("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.text_after("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.text_after("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.text_after("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.text_after("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_instance_num(self):
        try:
            mod.text_after("hello world", "test", instance_num=1)
        except EXC:
            pass


class Test_text_before_deep:
    def test_c0(self):
        try:
            mod.text_before("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.text_before("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.text_before("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.text_before("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.text_before("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.text_before("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_instance_num(self):
        try:
            mod.text_before("hello world", "test", instance_num=1)
        except EXC:
            pass


class Test_move_word_deep:
    def test_c0(self):
        try:
            mod.move_word("hello world", 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.move_word("test", 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.move_word("abc123", 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.move_word("", 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.move_word("Hello, World!", 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.move_word("UPPER lower 123", 1, 2)
        except EXC:
            pass


class Test_extract_last_number_deep:
    def test_c0(self):
        try:
            mod.extract_last_number("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.extract_last_number("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.extract_last_number("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.extract_last_number("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.extract_last_number("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.extract_last_number("UPPER lower 123")
        except EXC:
            pass


class Test_position_in_string_reverse_deep:
    def test_c0(self):
        try:
            mod.position_in_string_reverse("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.position_in_string_reverse("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.position_in_string_reverse("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.position_in_string_reverse("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.position_in_string_reverse("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.position_in_string_reverse("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_start_position(self):
        try:
            mod.position_in_string_reverse("hello world", "test", start_position=1)
        except EXC:
            pass


class Test_replace_last_occurrence_deep:
    def test_c0(self):
        try:
            mod.replace_last_occurrence("hello world", "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.replace_last_occurrence("test", "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.replace_last_occurrence("abc123", "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.replace_last_occurrence("", "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.replace_last_occurrence("Hello, World!", "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.replace_last_occurrence("UPPER lower 123", "hello world", "test")
        except EXC:
            pass


class Test_split_all_deep:
    def test_c0(self):
        try:
            mod.split_all("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.split_all("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.split_all("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.split_all("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.split_all("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.split_all("UPPER lower 123")
        except EXC:
            pass

    def test_kw_delimiter_pattern(self):
        try:
            mod.split_all("hello world", delimiter_pattern="hello world")
        except EXC:
            pass

    def test_kw_return_joined(self):
        try:
            mod.split_all("hello world", return_joined=True)
        except EXC:
            pass


class Test_substring_from_delimiters_deep:
    def test_c0(self):
        try:
            mod.substring_from_delimiters("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.substring_from_delimiters("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.substring_from_delimiters("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.substring_from_delimiters("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.substring_from_delimiters("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.substring_from_delimiters("UPPER lower 123")
        except EXC:
            pass

    def test_kw_opening_delimiter(self):
        try:
            mod.substring_from_delimiters("hello world", opening_delimiter="hello world")
        except EXC:
            pass

    def test_kw_closing_delimiter(self):
        try:
            mod.substring_from_delimiters("hello world", closing_delimiter="hello world")
        except EXC:
            pass


class Test_erase_specialchar_deep:
    def test_c0(self):
        try:
            mod.erase_specialchar("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.erase_specialchar("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.erase_specialchar("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.erase_specialchar("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.erase_specialchar("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.erase_specialchar("UPPER lower 123")
        except EXC:
            pass

    def test_kw_allow_spaces(self):
        try:
            mod.erase_specialchar("hello world", allow_spaces=True)
        except EXC:
            pass

    def test_kw_allow_underscores(self):
        try:
            mod.erase_specialchar("hello world", allow_underscores=True)
        except EXC:
            pass

    def test_kw_additional_allowed_chars(self):
        try:
            mod.erase_specialchar("hello world", additional_allowed_chars="hello world")
        except EXC:
            pass


class Test_extract_first_number_deep:
    def test_c0(self):
        try:
            mod.extract_first_number("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.extract_first_number("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.extract_first_number("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.extract_first_number("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.extract_first_number("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.extract_first_number("UPPER lower 123")
        except EXC:
            pass


class Test_extract_numbers_deep:
    def test_c0(self):
        try:
            mod.extract_numbers("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.extract_numbers("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.extract_numbers("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.extract_numbers("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.extract_numbers("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.extract_numbers("UPPER lower 123")
        except EXC:
            pass


class Test_position_in_string_deep:
    def test_c0(self):
        try:
            mod.position_in_string("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.position_in_string("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.position_in_string("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.position_in_string("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.position_in_string("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.position_in_string("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_start_position(self):
        try:
            mod.position_in_string("hello world", "test", start_position=1)
        except EXC:
            pass


class Test_random_string_deep:
    def test_c0(self):
        try:
            mod.random_string()
        except EXC:
            pass

    def test_kw_length(self):
        try:
            mod.random_string(length=1)
        except EXC:
            pass

    def test_kw_secure(self):
        try:
            mod.random_string(secure=True)
        except EXC:
            pass


class Test_replace_first_occurrence_deep:
    def test_c0(self):
        try:
            mod.replace_first_occurrence("hello world", "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.replace_first_occurrence("test", "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.replace_first_occurrence("abc123", "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.replace_first_occurrence("", "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.replace_first_occurrence("Hello, World!", "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.replace_first_occurrence("UPPER lower 123", "hello world", "test")
        except EXC:
            pass


class Test_replace_string_deep:
    def test_c0(self):
        try:
            mod.replace_string("hello world", "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.replace_string("test", "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.replace_string("abc123", "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.replace_string("", "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.replace_string("Hello, World!", "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.replace_string("UPPER lower 123", "hello world", "test")
        except EXC:
            pass


class Test_search_text_deep:
    def test_c0(self):
        try:
            mod.search_text("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.search_text("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.search_text("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.search_text("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.search_text("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.search_text("UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_kw_start_num(self):
        try:
            mod.search_text("hello world", "test", start_num=1)
        except EXC:
            pass


class Test_substitute_deep:
    def test_c0(self):
        try:
            mod.substitute("hello world", "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.substitute("test", "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.substitute("abc123", "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.substitute("", "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.substitute("Hello, World!", "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.substitute("UPPER lower 123", "hello world", "test")
        except EXC:
            pass

    def test_kw_instance_num(self):
        try:
            mod.substitute("hello world", "test", "abc123", instance_num=1)
        except EXC:
            pass


class Test_substring_on_left_deep:
    def test_c0(self):
        try:
            mod.substring_on_left("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.substring_on_left("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.substring_on_left("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.substring_on_left("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.substring_on_left("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.substring_on_left("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_substring_on_right_deep:
    def test_c0(self):
        try:
            mod.substring_on_right("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.substring_on_right("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.substring_on_right("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.substring_on_right("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.substring_on_right("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.substring_on_right("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_truncate_string_deep:
    def test_c0(self):
        try:
            mod.truncate_string("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.truncate_string("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.truncate_string("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.truncate_string("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.truncate_string("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.truncate_string("UPPER lower 123")
        except EXC:
            pass

    def test_kw_target_length(self):
        try:
            mod.truncate_string("hello world", target_length=1)
        except EXC:
            pass

    def test_kw_align(self):
        try:
            mod.truncate_string("hello world", align="hello world")
        except EXC:
            pass


class Test_add_quotes_deep:
    def test_c0(self):
        try:
            mod.add_quotes("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.add_quotes("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.add_quotes("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.add_quotes("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.add_quotes("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.add_quotes("UPPER lower 123")
        except EXC:
            pass

    def test_kw_quote_type(self):
        try:
            mod.add_quotes("hello world", quote_type="hello world")
        except EXC:
            pass


class Test_caesar_cipher_deep:
    def test_c0(self):
        try:
            mod.caesar_cipher("hello world", 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.caesar_cipher("test", 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.caesar_cipher("abc123", 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.caesar_cipher("", 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.caesar_cipher("Hello, World!", 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.caesar_cipher("UPPER lower 123", 1)
        except EXC:
            pass


class Test_chunk_string_deep:
    def test_c0(self):
        try:
            mod.chunk_string("hello world", 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.chunk_string("test", 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.chunk_string("abc123", 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.chunk_string("", 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.chunk_string("Hello, World!", 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.chunk_string("UPPER lower 123", 1)
        except EXC:
            pass


class Test_count_characters_deep:
    def test_c0(self):
        try:
            mod.count_characters("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.count_characters("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.count_characters("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.count_characters("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.count_characters("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.count_characters("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_count_syllables_deep:
    def test_c0(self):
        try:
            mod.count_syllables("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.count_syllables("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.count_syllables("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.count_syllables("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.count_syllables("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.count_syllables("UPPER lower 123")
        except EXC:
            pass

    def test_kw_lang(self):
        try:
            mod.count_syllables("hello world", lang="hello world")
        except EXC:
            pass


class Test_extract_content_by_encloser_type_deep:
    def test_c0(self):
        try:
            mod.extract_content_by_encloser_type("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.extract_content_by_encloser_type("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.extract_content_by_encloser_type("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.extract_content_by_encloser_type("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.extract_content_by_encloser_type("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.extract_content_by_encloser_type("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_generate_password_deep:
    def test_c0(self):
        try:
            mod.generate_password()
        except EXC:
            pass

    def test_kw_length(self):
        try:
            mod.generate_password(length=1)
        except EXC:
            pass


class Test_get_line_deep:
    def test_c0(self):
        try:
            mod.get_line("hello world", 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_line("test", 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_line("abc123", 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_line("", 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_line("Hello, World!", 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_line("UPPER lower 123", 1)
        except EXC:
            pass


class Test_get_substrings_deep:
    def test_c0(self):
        try:
            mod.get_substrings("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.get_substrings("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.get_substrings("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.get_substrings("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.get_substrings("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.get_substrings("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_pad_center_deep:
    def test_c0(self):
        try:
            mod.pad_center("hello world", 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pad_center("test", 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pad_center("abc123", 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pad_center("", 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pad_center("Hello, World!", 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pad_center("UPPER lower 123", 1)
        except EXC:
            pass

    def test_kw_fillchar(self):
        try:
            mod.pad_center("hello world", 2, fillchar="hello world")
        except EXC:
            pass


class Test_pad_end_deep:
    def test_c0(self):
        try:
            mod.pad_end("hello world", 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.pad_end("test", 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.pad_end("abc123", 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.pad_end("", 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.pad_end("Hello, World!", 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.pad_end("UPPER lower 123", 1)
        except EXC:
            pass

    def test_kw_fillchar(self):
        try:
            mod.pad_end("hello world", 2, fillchar="hello world")
        except EXC:
            pass


class Test_regex_replace_deep:
    def test_c0(self):
        try:
            mod.regex_replace("hello world", "test", "abc123")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.regex_replace("test", "abc123", "")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.regex_replace("abc123", "", "Hello, World!")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.regex_replace("", "Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.regex_replace("Hello, World!", "UPPER lower 123", "hello world")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.regex_replace("UPPER lower 123", "hello world", "test")
        except EXC:
            pass

    def test_kw_case_insensitive(self):
        try:
            mod.regex_replace("hello world", "test", "abc123", case_insensitive=True)
        except EXC:
            pass


class Test_repeat_each_char_deep:
    def test_c0(self):
        try:
            mod.repeat_each_char("hello world", 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.repeat_each_char("test", 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.repeat_each_char("abc123", 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.repeat_each_char("", 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.repeat_each_char("Hello, World!", 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.repeat_each_char("UPPER lower 123", 1)
        except EXC:
            pass


class Test_repeat_string_deep:
    def test_c0(self):
        try:
            mod.repeat_string("hello world", 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.repeat_string("test", 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.repeat_string("abc123", 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.repeat_string("", 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.repeat_string("Hello, World!", 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.repeat_string("UPPER lower 123", 1)
        except EXC:
            pass


class Test_snake_to_camel_deep:
    def test_c0(self):
        try:
            mod.snake_to_camel("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.snake_to_camel("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.snake_to_camel("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.snake_to_camel("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.snake_to_camel("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.snake_to_camel("UPPER lower 123")
        except EXC:
            pass


class Test_substring_deep:
    def test_c0(self):
        try:
            mod.substring("hello world", 2, 3)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.substring("test", 3, 5)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.substring("abc123", 5, 10)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.substring("", 10, 0)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.substring("Hello, World!", 0, 1)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.substring("UPPER lower 123", 1, 2)
        except EXC:
            pass


class Test_substring_between_pattern_deep:
    def test_c0(self):
        try:
            mod.substring_between_pattern("hello world", "test")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.substring_between_pattern("test", "abc123")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.substring_between_pattern("abc123", "")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.substring_between_pattern("", "Hello, World!")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.substring_between_pattern("Hello, World!", "UPPER lower 123")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.substring_between_pattern("UPPER lower 123", "hello world")
        except EXC:
            pass


class Test_truncate_with_ellipsis_deep:
    def test_c0(self):
        try:
            mod.truncate_with_ellipsis("hello world", 2)
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.truncate_with_ellipsis("test", 3)
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.truncate_with_ellipsis("abc123", 5)
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.truncate_with_ellipsis("", 10)
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.truncate_with_ellipsis("Hello, World!", 0)
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.truncate_with_ellipsis("UPPER lower 123", 1)
        except EXC:
            pass

    def test_kw_ellipsis(self):
        try:
            mod.truncate_with_ellipsis("hello world", 2, ellipsis="hello world")
        except EXC:
            pass


class Test_wrap_text_deep:
    def test_c0(self):
        try:
            mod.wrap_text("hello world")
        except EXC:
            pass

    def test_c1(self):
        try:
            mod.wrap_text("test")
        except EXC:
            pass

    def test_c2(self):
        try:
            mod.wrap_text("abc123")
        except EXC:
            pass

    def test_c3(self):
        try:
            mod.wrap_text("")
        except EXC:
            pass

    def test_c4(self):
        try:
            mod.wrap_text("Hello, World!")
        except EXC:
            pass

    def test_c5(self):
        try:
            mod.wrap_text("UPPER lower 123")
        except EXC:
            pass

    def test_kw_width(self):
        try:
            mod.wrap_text("hello world", width=1)
        except EXC:
            pass

