"""Tests for fxString.string_operations."""

import re

import pytest

from shortfx.fxString.string_evaluations import is_valid_issn, is_valid_swift_bic
from shortfx.fxString.string_operations import (
    camel_to_snake,
    chunk_string,
    collapse_whitespace,
    cologne_phonetic,
    constant_case,
    count_consonants,
    count_occurrences,
    count_syllables,
    count_vowels,
    double_metaphone,
    erase_lspaces,
    erase_rspaces,
    extract_hashtags,
    interleave_strings,
    kebab_case,
    longest_common_prefix,
    longest_common_suffix,
    longest_word,
    metaphone,
    nysiis,
    pad_center,
    pad_end,
    pad_start,
    regex_replace,
    remove_prefix,
    remove_suffix,
    repeat_each_char,
    replace_by_position,
    reverse_words,
    rot13,
    run_length_decode,
    run_length_encode,
    shortest_word,
    snake_to_camel,
    soundex,
    squeeze,
    string_xor,
    swap_case,
    title_case,
    truncate_with_ellipsis,
    zigzag_case,
)


class TestInterleaveStrings:

    def test_equal_length(self):
        assert interleave_strings("abc", "123") == "a1b2c3"

    def test_first_longer(self):
        assert interleave_strings("abcd", "12") == "a1b2cd"

    def test_second_longer(self):
        assert interleave_strings("ab", "1234") == "a1b234"

    def test_empty(self):
        assert interleave_strings("", "") == ""

    def test_type_error(self):

        with pytest.raises(TypeError):
            interleave_strings("a", 1)

class TestRunLengthEncoding:

    def test_encode(self):
        assert run_length_encode("aaabbc") == "3a2b1c"

    def test_decode(self):
        assert run_length_decode("3a2b1c") == "aaabbc"

    def test_roundtrip(self):
        original = "aabbccdddd"
        assert run_length_decode(run_length_encode(original)) == original

    def test_empty(self):
        assert run_length_encode("") == ""
        assert run_length_decode("") == ""

    def test_decode_invalid(self):

        with pytest.raises(ValueError):
            run_length_decode("abc")


# ── fxString ── string_convertions ──────────────────────────────────────

class TestCountVowels:

    def test_english(self):
        assert count_vowels("Hello World") == 3

    def test_spanish(self):
        assert count_vowels("café", lang="es") == 2

    def test_empty(self):
        assert count_vowels("") == 0

    def test_type_error(self):

        with pytest.raises(TypeError):
            count_vowels(42)


# ── fxString ── string_convertions ──────────────────────────────────────

class TestGeneratePassword:
    """Cryptographic password generation."""

    def test_generate_password_length(self):
        from shortfx.fxString.string_operations import generate_password

        pwd = generate_password(20)
        assert len(pwd) == 20

    def test_generate_password_has_all_categories(self):
        from shortfx.fxString.string_operations import generate_password

        pwd = generate_password(16)
        assert any(c.isupper() for c in pwd)
        assert any(c.islower() for c in pwd)
        assert any(c.isdigit() for c in pwd)
        assert any(not c.isalnum() for c in pwd)

    def test_generate_password_no_special(self):
        from shortfx.fxString.string_operations import generate_password

        pwd = generate_password(12, special=False)
        assert len(pwd) == 12
        assert all(c.isalnum() for c in pwd)

    def test_generate_password_digits_only(self):
        from shortfx.fxString.string_operations import generate_password

        pwd = generate_password(8, uppercase=False, lowercase=False, digits=True, special=False)
        assert len(pwd) == 8
        assert pwd.isdigit()

    def test_generate_password_too_short(self):
        from shortfx.fxString.string_operations import generate_password

        with pytest.raises(ValueError):
            generate_password(2)

    def test_generate_password_no_category(self):
        from shortfx.fxString.string_operations import generate_password

        with pytest.raises(ValueError):
            generate_password(8, uppercase=False, lowercase=False, digits=False, special=False)


# =====================================================================
# fxDate — date_evaluations (sidereal time)
# =====================================================================

class TestPadStart:
    def test_basic(self):
        assert pad_start("42", 5, "0") == "00042"

    def test_no_padding_needed(self):
        assert pad_start("hello", 3) == "hello"

    def test_default_space(self):
        assert pad_start("x", 3) == "  x"

    def test_type_error(self):
        with pytest.raises(TypeError):
            pad_start(42, 5)

    def test_fillchar_error(self):
        with pytest.raises(ValueError):
            pad_start("x", 5, "ab")

class TestPadEnd:
    def test_basic(self):
        assert pad_end("hi", 5, ".") == "hi..."

    def test_no_padding_needed(self):
        assert pad_end("hello", 3, ".") == "hello"

    def test_type_error(self):
        with pytest.raises(TypeError):
            pad_end(123, 5)

class TestPadCenter:
    def test_basic(self):
        assert pad_center("hi", 6, "-") == "--hi--"

    def test_odd_padding(self):
        result = pad_center("hi", 5, "-")
        assert len(result) == 5

    def test_type_error(self):
        with pytest.raises(TypeError):
            pad_center(None, 5)

class TestRemovePrefix:
    def test_basic(self):
        assert remove_prefix("unhappy", "un") == "happy"

    def test_no_match(self):
        assert remove_prefix("happy", "un") == "happy"

    def test_empty_prefix(self):
        assert remove_prefix("hello", "") == "hello"

    def test_type_error(self):
        with pytest.raises(TypeError):
            remove_prefix(123, "un")

class TestRemoveSuffix:
    def test_basic(self):
        assert remove_suffix("filename.txt", ".txt") == "filename"

    def test_no_match(self):
        assert remove_suffix("filename.txt", ".csv") == "filename.txt"

    def test_empty_suffix(self):
        assert remove_suffix("hello", "") == "hello"

    def test_type_error(self):
        with pytest.raises(TypeError):
            remove_suffix(123, ".txt")

class TestCollapseWhitespace:
    def test_basic(self):
        assert collapse_whitespace("  hello   world  ") == "hello world"

    def test_tabs_newlines(self):
        assert collapse_whitespace("a\t\nb") == "a b"

    def test_empty(self):
        assert collapse_whitespace("") == ""

    def test_type_error(self):
        with pytest.raises(TypeError):
            collapse_whitespace(123)

class TestTruncateWithEllipsis:
    def test_basic(self):
        assert truncate_with_ellipsis("hello world", 8) == "hello..."

    def test_no_truncation(self):
        assert truncate_with_ellipsis("hi", 10) == "hi"

    def test_custom_ellipsis(self):
        assert truncate_with_ellipsis("abcdef", 5, "..") == "abc.."

    def test_type_error(self):
        with pytest.raises(TypeError):
            truncate_with_ellipsis(123, 5)

    def test_value_error(self):
        with pytest.raises(ValueError):
            truncate_with_ellipsis("hi", 1, "...")

class TestCamelToSnake:
    def test_basic(self):
        assert camel_to_snake("helloWorld") == "hello_world"

    def test_pascal(self):
        assert camel_to_snake("HelloWorld") == "hello_world"

    def test_single_word(self):
        assert camel_to_snake("hello") == "hello"

    def test_type_error(self):
        with pytest.raises(TypeError):
            camel_to_snake(123)

class TestCountOccurrences:
    def test_basic(self):
        assert count_occurrences("banana", "an") == 2

    def test_no_match(self):
        assert count_occurrences("hello", "xyz") == 0

    def test_type_error(self):
        with pytest.raises(TypeError):
            count_occurrences(123, "a")

class TestRepeatEachChar:
    def test_basic(self):
        assert repeat_each_char("abc", 2) == "aabbcc"

    def test_zero(self):
        assert repeat_each_char("abc", 0) == ""

    def test_type_error(self):
        with pytest.raises(TypeError):
            repeat_each_char(123, 2)

    def test_negative(self):
        with pytest.raises(ValueError):
            repeat_each_char("a", -1)

class TestZigzagCase:
    def test_basic(self):
        assert zigzag_case("hello") == "hElLo"

    def test_empty(self):
        assert zigzag_case("") == ""

    def test_type_error(self):
        with pytest.raises(TypeError):
            zigzag_case(123)

class TestSwapCase:
    def test_basic(self):
        assert swap_case("Hello World") == "hELLO wORLD"

    def test_all_lower(self):
        assert swap_case("abc") == "ABC"

    def test_type_error(self):
        with pytest.raises(TypeError):
            swap_case(123)

class TestRot13:
    def test_basic(self):
        assert rot13("hello") == "uryyb"

    def test_roundtrip(self):
        assert rot13(rot13("secret")) == "secret"

    def test_type_error(self):
        with pytest.raises(TypeError):
            rot13(42)

class TestTitleCase:
    def test_basic(self):
        assert title_case("hello world") == "Hello World"

    def test_already_titled(self):
        assert title_case("Hello") == "Hello"

    def test_type_error(self):
        with pytest.raises(TypeError):
            title_case(123)

class TestSnakeToCamel:
    def test_basic(self):
        assert snake_to_camel("hello_world") == "helloWorld"

    def test_single_word(self):
        assert snake_to_camel("hello") == "hello"

    def test_multiple_parts(self):
        assert snake_to_camel("a_b_c") == "aBC"

    def test_type_error(self):
        with pytest.raises(TypeError):
            snake_to_camel(123)

class TestKebabCase:
    def test_basic(self):
        assert kebab_case("Hello World") == "hello-world"

    def test_extra_spaces(self):
        assert kebab_case("  Hello   World  ") == "hello-world"

    def test_type_error(self):
        with pytest.raises(TypeError):
            kebab_case(123)

class TestConstantCase:
    def test_basic(self):
        assert constant_case("Hello World") == "HELLO_WORLD"

    def test_single_word(self):
        assert constant_case("hello") == "HELLO"

    def test_type_error(self):
        with pytest.raises(TypeError):
            constant_case(123)

class TestChunkString:
    def test_basic(self):
        assert chunk_string("abcdefgh", 3) == ["abc", "def", "gh"]

    def test_exact_multiple(self):
        assert chunk_string("abcdef", 3) == ["abc", "def"]

    def test_empty(self):
        assert chunk_string("", 5) == []

    def test_type_error(self):
        with pytest.raises(TypeError):
            chunk_string(123, 3)

    def test_value_error(self):
        with pytest.raises(ValueError):
            chunk_string("abc", 0)

class TestSqueeze:
    def test_basic(self):
        assert squeeze("aaabbbccc", "b") == "aaabccc"

    def test_no_runs(self):
        assert squeeze("abc", "a") == "abc"

    def test_all_same(self):
        assert squeeze("aaaa", "a") == "a"

    def test_type_error(self):
        with pytest.raises(TypeError):
            squeeze(123, "a")

    def test_value_error(self):
        with pytest.raises(ValueError):
            squeeze("abc", "ab")

class TestStringXor:
    def test_basic(self):
        assert string_xor("abc", "ABC") == "202020"

    def test_same_strings(self):
        assert string_xor("aaa", "aaa") == "000000"

    def test_type_error(self):
        with pytest.raises(TypeError):
            string_xor(123, "abc")

    def test_length_error(self):
        with pytest.raises(ValueError):
            string_xor("ab", "abc")


# ── String Evaluations ──────────────────────────────────────────────────

class TestCountConsonants:

    def test_basic(self):
        assert count_consonants("Hello World") == 7

    def test_empty(self):
        assert count_consonants("") == 0

    def test_no_consonants(self):
        assert count_consonants("aeiou") == 0

    def test_spanish(self):
        assert count_consonants("Hóla", lang="es") == 2

    def test_type_error(self):
        with pytest.raises(TypeError):
            count_consonants(123)

class TestLongestWord:

    def test_basic(self):
        assert longest_word("the quick brown fox") == "quick"

    def test_empty(self):
        assert longest_word("") == ""

    def test_single(self):
        assert longest_word("word") == "word"

    def test_type_error(self):
        with pytest.raises(TypeError):
            longest_word(123)

class TestShortestWord:

    def test_basic(self):
        assert shortest_word("the quick brown fox") == "the"

    def test_empty(self):
        assert shortest_word("") == ""

    def test_single(self):
        assert shortest_word("hi") == "hi"

class TestReverseWords:

    def test_basic(self):
        assert reverse_words("hello world foo") == "foo world hello"

    def test_empty(self):
        assert reverse_words("") == ""

    def test_single(self):
        assert reverse_words("word") == "word"

class TestExtractHashtags:

    def test_basic(self):
        assert extract_hashtags("Hello #world #python3") == ["#world", "#python3"]

    def test_none(self):
        assert extract_hashtags("no tags here") == []

    def test_type_error(self):
        with pytest.raises(TypeError):
            extract_hashtags(123)

class TestIsValidSwiftBic:

    def test_8_char(self):
        assert is_valid_swift_bic("DEUTDEFF") is True

    def test_11_char(self):
        assert is_valid_swift_bic("DEUTDEFF500") is True

    def test_invalid_short(self):
        assert is_valid_swift_bic("DEUT") is False

    def test_invalid_numbers_in_bank(self):
        assert is_valid_swift_bic("1234DEFF") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_swift_bic(123)


# ── fxString · string_operations ──────────────────────────────────────────


class TestCountSyllables:

    def test_english_basic(self):
        assert count_syllables("beautiful day") == 4

    def test_english_single(self):
        assert count_syllables("the") >= 1

    def test_spanish(self):
        assert count_syllables("hermoso día", lang="es") >= 2

    def test_empty(self):
        assert count_syllables("") == 0

    def test_invalid_lang(self):
        with pytest.raises(ValueError):
            count_syllables("hello", lang="xx")

    def test_type_error(self):
        with pytest.raises(TypeError):
            count_syllables(123)

class TestSoundex:

    def test_robert(self):
        assert soundex("Robert") == "R163"

    def test_rupert(self):
        assert soundex("Rupert") == "R163"

    def test_ashcraft(self):
        assert soundex("Ashcraft") == "A261"

    def test_type_error(self):
        with pytest.raises(TypeError):
            soundex(123)

    def test_empty(self):
        with pytest.raises(ValueError):
            soundex("")

class TestMetaphone:

    def test_smith(self):
        result = metaphone("Smith")
        assert isinstance(result, str)
        assert len(result) > 0

    def test_thompson(self):
        result = metaphone("Thompson")
        assert isinstance(result, str)

    def test_type_error(self):
        with pytest.raises(TypeError):
            metaphone(123)

    def test_empty(self):
        with pytest.raises(ValueError):
            metaphone("")

class TestIsValidIssn:

    def test_valid_with_hyphen(self):
        assert is_valid_issn("0378-5955") is True

    def test_valid_no_hyphen(self):
        assert is_valid_issn("03785955") is True

    def test_valid_with_x(self):
        assert is_valid_issn("0000-0019") is True

    def test_invalid(self):
        assert is_valid_issn("1234-5678") is False

    def test_wrong_length(self):
        assert is_valid_issn("0378-595") is False

    def test_type_error(self):
        with pytest.raises(TypeError):
            is_valid_issn(12345678)


# ── fxString · string_operations ─────────────────────────────────────


class TestNysiis:

    def test_watkins(self):
        assert nysiis("Watkins") == "WATCAN"

    def test_johnson(self):
        assert nysiis("Johnson") == "JANSAN"

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            nysiis("")

    def test_type_error(self):
        with pytest.raises(TypeError):
            nysiis(123)

class TestDoubleMetaphone:

    def test_smith(self):
        primary, alt = double_metaphone("Smith")
        assert isinstance(primary, str) and isinstance(alt, str)
        assert len(primary) <= 4 and len(alt) <= 4

    def test_schmidt(self):
        primary, alt = double_metaphone("Schmidt")
        assert isinstance(primary, str)
        assert len(primary) <= 4

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            double_metaphone("   ")

    def test_type_error(self):
        with pytest.raises(TypeError):
            double_metaphone(42)

class TestColognePhonetic:

    def test_mueller(self):
        assert cologne_phonetic("Müller") == "657"

    def test_schmidt(self):
        result = cologne_phonetic("Schmidt")
        assert isinstance(result, str)
        assert result.isdigit()

    def test_empty_raises(self):
        with pytest.raises(ValueError):
            cologne_phonetic("123")

    def test_type_error(self):
        with pytest.raises(TypeError):
            cologne_phonetic(42)

class TestLongestCommonPrefix:

    def test_basic(self):
        assert longest_common_prefix("interstellar", "internet") == "inter"

    def test_no_match(self):
        assert longest_common_prefix("abc", "xyz") == ""

    def test_identical(self):
        assert longest_common_prefix("hello", "hello") == "hello"

    def test_empty_string(self):
        assert longest_common_prefix("", "abc") == ""

    def test_type_error(self):
        with pytest.raises(TypeError):
            longest_common_prefix(123, "abc")

class TestLongestCommonSuffix:

    def test_basic(self):
        assert longest_common_suffix("testing", "running") == "ing"

    def test_no_match(self):
        assert longest_common_suffix("abc", "xyz") == ""

    def test_identical(self):
        assert longest_common_suffix("hello", "hello") == "hello"

    def test_empty_string(self):
        assert longest_common_suffix("", "abc") == ""

    def test_type_error(self):
        with pytest.raises(TypeError):
            longest_common_suffix(123, "abc")

class TestReplaceByPosition:

    @pytest.mark.parametrize("original, start, num, new_text, expected", [
        ("abcdefghijk", 6, 5, "*", "abcde*k"),
        ("2024", 3, 2, "25", "2025"),
        ("Hello World", 1, 5, "Goodbye", "Goodbye World"),
        ("XYZ123", 4, 3, "456", "XYZ456"),
        ("ABCDE", 3, 0, "XY", "ABXYCDE"),
        ("ABC", 4, 0, "D", "ABCD"),
        ("ABC", 1, 3, "", ""),
        ("ABC", 2, 5, "X", "AX"),
    ])
    def test_replace_by_position_valid_cases(
        self, original: str, start: int, num: int, new_text: str, expected: str
    ):
        assert replace_by_position(original, start, num, new_text) == expected

    def test_replace_by_position_raises_on_non_string_original(self):

        with pytest.raises(TypeError):
            replace_by_position(123, 1, 2, "x")

    def test_replace_by_position_raises_on_non_string_new_text(self):

        with pytest.raises(TypeError):
            replace_by_position("abc", 1, 2, 123)

    def test_replace_by_position_raises_on_non_int_start(self):

        with pytest.raises(TypeError):
            replace_by_position("abc", "1", 2, "x")

    def test_replace_by_position_raises_on_start_less_than_1(self):

        with pytest.raises(ValueError):
            replace_by_position("abc", 0, 2, "x")

    def test_replace_by_position_raises_on_negative_num_chars(self):

        with pytest.raises(ValueError):
            replace_by_position("abc", 1, -1, "x")


# ── regex_replace ────────────────────────────────────────────────────────────

class TestRegexReplace:

    @pytest.mark.parametrize("text, pattern, replacement, expected", [
        ("Hello 123 World 456", r"\d+", "X", "Hello X World X"),
        ("test@email.com", r"@.*", "@example.com", "test@example.com"),
        ("aaa bbb ccc", r"\s+", "-", "aaa-bbb-ccc"),
        ("no match here", r"\d+", "X", "no match here"),
        ("abc", r"(.)", r"\1\1", "aabbcc"),
    ])
    def test_regex_replace_valid_cases(
        self, text: str, pattern: str, replacement: str, expected: str
    ):
        assert regex_replace(text, pattern, replacement) == expected

    def test_regex_replace_case_insensitive(self):
        assert regex_replace("FooBar FooBaz", r"foo", "QUX", case_insensitive=True) == "QUXBar QUXBaz"

    def test_regex_replace_case_sensitive_by_default(self):
        assert regex_replace("FooBar FooBaz", r"foo", "QUX") == "FooBar FooBaz"

    def test_regex_replace_raises_on_non_string_text(self):

        with pytest.raises(TypeError):
            regex_replace(123, r"\d+", "X")

    def test_regex_replace_raises_on_non_string_pattern(self):

        with pytest.raises(TypeError):
            regex_replace("abc", 123, "X")

    def test_regex_replace_raises_on_invalid_pattern(self):

        with pytest.raises(re.error):
            regex_replace("abc", r"[invalid", "X")


# ── erase_lspaces ────────────────────────────────────────────────────────────

class TestEraseLspaces:

    @pytest.mark.parametrize("text, expected", [
        ("   hello   ", "hello   "),
        ("hello", "hello"),
        ("   ", ""),
        ("\t\n hello", "hello"),
        ("", ""),
    ])
    def test_erase_lspaces_valid_cases(self, text: str, expected: str):
        assert erase_lspaces(text) == expected

    def test_erase_lspaces_returns_none_for_none(self):
        assert erase_lspaces(None) is None


# ── erase_rspaces ────────────────────────────────────────────────────────────

class TestEraseRspaces:

    @pytest.mark.parametrize("text, expected", [
        ("   hello   ", "   hello"),
        ("hello", "hello"),
        ("   ", ""),
        ("hello \t\n", "hello"),
        ("", ""),
    ])
    def test_erase_rspaces_valid_cases(self, text: str, expected: str):
        assert erase_rspaces(text) == expected

    def test_erase_rspaces_returns_none_for_none(self):
        assert erase_rspaces(None) is None
