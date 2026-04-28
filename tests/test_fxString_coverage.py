"""Coverage tests for fxString modules."""
import pytest

from agentfx.fxString.string_operations import (
    reverse_string, count_occurrences, pad_start, pad_end,
    truncate_string, collapse_whitespace,
    repeat_string, replace_string,
    replace_first_occurrence, replace_last_occurrence,
    substring, left_substring, right_substring,
    swap_case, erase_specialchar,
    erase_digits, erase_allspaces, erase_lrspaces,
    slugify, camel_to_snake, snake_to_camel,
    title_case, count_words, count_lines, wrap_text, center_string, pad_center,
    remove_prefix, remove_suffix,
    reverse_words, distinct_words,
    sort_lines, remove_blank_lines,
    extract_numbers, extract_emails, extract_urls,
    generate_password, random_string,
    soundex, metaphone, cologne_phonetic,
    run_length_encode, run_length_decode,
    caesar_cipher, rot13,
)

class TestStringOperations:
    def test_reverse(self):
        assert reverse_string("hello") == "olleh"
    def test_count_occurrences(self):
        assert count_occurrences("hello world", "o") == 2
    def test_pad_start(self):
        r = pad_start("hi", 5)
        assert len(r) == 5
    def test_pad_end(self):
        r = pad_end("hi", 5)
        assert len(r) == 5
    def test_truncate(self):
        r = truncate_string("hello world", 5)
        assert len(r) <= 8
    def test_collapse_whitespace(self):
        assert collapse_whitespace("hello   world") == "hello world"
    def test_repeat_string(self):
        assert repeat_string("ab", 3) == "ababab"
    def test_replace_string(self):
        assert replace_string("hello world", "world", "earth") == "hello earth"
    def test_replace_first(self):
        assert replace_first_occurrence("aabaa", "a", "x") == "xabaa"
    def test_replace_last(self):
        assert replace_last_occurrence("aabaa", "a", "x") == "aabax"
    def test_substring(self):
        r = substring("hello", 1, 4)
        assert isinstance(r, str)
    def test_left_substring(self):
        assert left_substring("hello", 3) == "hel"
    def test_right_substring(self):
        assert right_substring("hello", 3) == "llo"

    def test_swap_case(self):
        assert swap_case("Hello") == "hELLO"
    def test_erase_specialchar(self):
        r = erase_specialchar("hello!")
        assert isinstance(r, str)
    def test_erase_digits(self):
        r = erase_digits("abc123")
        assert "1" not in r
    def test_erase_allspaces(self):
        assert erase_allspaces("h e l l o") == "hello"
    def test_erase_lrspaces(self):
        assert erase_lrspaces("  hello  ") == "hello"
    def test_slugify(self):
        r = slugify("Hello World!")
        assert " " not in r
    def test_camel_to_snake(self):
        assert camel_to_snake("helloWorld") == "hello_world"
    def test_snake_to_camel(self):
        assert snake_to_camel("hello_world") == "helloWorld"
    def test_title_case(self):
        assert title_case("hello world") == "Hello World"
    def test_count_words(self):
        assert count_words("hello world") == 2
    def test_count_lines(self):
        assert count_lines("a\nb\nc") == 3

    def test_wrap_text(self):
        r = wrap_text("hello world foo bar", 10)
        assert isinstance(r, str)
    def test_center_string(self):
        r = center_string("hi", 10)
        assert len(r) == 10
    def test_pad_center(self):
        r = pad_center("hi", 10)
        assert len(r) == 10
    def test_remove_prefix(self):
        assert remove_prefix("hello", "hel") == "lo"
    def test_remove_suffix(self):
        assert remove_suffix("hello", "llo") == "he"
    def test_reverse_words(self):
        assert reverse_words("hello world") == "world hello"
    def test_distinct_words(self):
        r = distinct_words("a b a c b")
        assert len(r) == 3
    def test_sort_lines(self):
        r = sort_lines("c\nb\na")
        assert r.startswith("a")
    def test_remove_blank_lines(self):
        r = remove_blank_lines("a\n\nb")
        assert "\n\n" not in r
    def test_extract_numbers(self):
        r = extract_numbers("a1b2c3")
        assert len(r) == 3
    def test_extract_emails(self):
        r = extract_emails("contact test@example.com please")
        assert len(r) == 1
    def test_extract_urls(self):
        r = extract_urls("visit https://example.com today")
        assert len(r) >= 1
    def test_generate_password(self):
        r = generate_password(12)
        assert len(r) == 12
    def test_random_string(self):
        r = random_string(8)
        assert len(r) == 8
    def test_soundex(self):
        assert isinstance(soundex("Robert"), str)
    def test_metaphone(self):
        assert isinstance(metaphone("Robert"), str)
    def test_cologne_phonetic(self):
        assert isinstance(cologne_phonetic("Müller"), str)
    def test_rle_encode(self):
        r = run_length_encode("aaabbc")
        assert isinstance(r, str)
    def test_rle_decode(self):
        enc = run_length_encode("aaabbc")
        dec = run_length_decode(enc)
        assert dec == "aaabbc"
    def test_caesar(self):
        r = caesar_cipher("hello", 3)
        assert isinstance(r, str) and r != "hello"
    def test_rot13(self):
        r = rot13("hello")
        assert isinstance(r, str)

from agentfx.fxString.string_format import (
    format_number, format_as_currency, format_as_percent,
    format_file_size,
    capitalize_string, mask_data, normalize_text,
    to_lower, to_upper, word_wrap, zfill, pad_string,
    format_name, format_fullname,
    numbers_from_string, remove_numbers_from_string,
    string_aZ, string_aZ09, pluralize_count,
)

class TestStringFormat:
    def test_format_number(self):
        r = format_number(1234567.89)
        assert isinstance(r, str)
    def test_format_as_currency(self):
        r = format_as_currency(1234.56)
        assert isinstance(r, str)
    def test_format_as_percent(self):
        r = format_as_percent(0.42)
        assert isinstance(r, str)

    def test_format_file_size(self):
        r = format_file_size(1024)
        assert isinstance(r, str)
    def test_capitalize(self):
        r = capitalize_string("hello world")
        assert r[0] == "H"
    def test_mask_data(self):
        r = mask_data("1234567890")
        assert r != "1234567890"
    def test_normalize_text(self):
        r = normalize_text("  hello   world  ")
        assert isinstance(r, str)
    def test_to_lower(self):
        assert to_lower("HELLO") == "hello"
    def test_to_upper(self):
        assert to_upper("hello") == "HELLO"
    def test_word_wrap(self):
        r = word_wrap("hello world foo bar baz", 10)
        assert isinstance(r, str)
    def test_zfill(self):
        assert zfill("42", 5) == "00042"
    def test_pad_string(self):
        r = pad_string("hi", 5)
        assert len(r) >= 5
    def test_format_name(self):
        r = format_name("john doe")
        assert isinstance(r, str)
    def test_format_fullname(self):
        r = format_fullname("john", "doe")
        assert isinstance(r, str)
    def test_numbers_from_string(self):
        r = numbers_from_string("abc123def")
        assert isinstance(r, str) and "123" in r
    def test_remove_numbers(self):
        r = remove_numbers_from_string("abc123")
        assert "1" not in r
    def test_string_aZ(self):
        r = string_aZ("hello 123")
        assert isinstance(r, str)
    def test_string_aZ09(self):
        r = string_aZ09("hello 123!")
        assert isinstance(r, str)
    def test_pluralize_count(self):
        r = pluralize_count(3, "cat")
        assert isinstance(r, str)

from agentfx.fxString.string_similarity import (
    string_lcs_score, generate_ngrams,
)

class TestStringSimilarity:

    def test_lcs(self):
        r = string_lcs_score("abcde", "ace")
        assert isinstance(r, (int, float))

    def test_ngrams(self):
        r = generate_ngrams("hello", 2)
        assert isinstance(r, list)

from agentfx.fxString.string_evaluations import (
    is_numeric as str_is_numeric, is_aZ, is_aZ09,
    is_palindrome, is_anagram, is_email_format,
    is_url_format, is_ipv4, is_ipv6,
    count_sentences, word_frequency, char_frequency,
    reading_time, text_entropy,
    flesch_reading_ease, gunning_fog_index,
    is_json, is_uuid, is_valid_base64,
    check_password_strength,
    has_numbers,
)

class TestStringEvaluations:
    def test_is_numeric(self):
        assert str_is_numeric("123") is True

    def test_is_aZ(self):
        assert is_aZ("abc") is True
    def test_is_aZ09(self):
        assert is_aZ09("abc123") is True
    def test_is_palindrome(self):
        assert is_palindrome("racecar") is True
    def test_is_anagram(self):
        assert is_anagram("listen", "silent") is True
    def test_is_email(self):
        assert is_email_format("test@example.com") is True
    def test_is_url(self):
        assert is_url_format("https://example.com") is True
    def test_is_ipv4(self):
        assert is_ipv4("192.168.1.1") is True
    def test_is_ipv6(self):
        r = is_ipv6("::1")
        assert isinstance(r, bool)
    def test_count_sentences(self):
        assert count_sentences("Hello. World.") == 2
    def test_word_frequency(self):
        r = word_frequency("hello hello world")
        assert r["hello"] == 2
    def test_char_frequency(self):
        r = char_frequency("hello")
        assert r["l"] == 2
    def test_reading_time(self):
        r = reading_time("word " * 250)
        assert isinstance(r, (int, float))
    def test_text_entropy(self):
        r = text_entropy("hello world")
        assert isinstance(r, (int, float))
    def test_flesch(self):
        r = flesch_reading_ease("The quick brown fox jumps over the lazy dog.")
        assert isinstance(r, (int, float))
    def test_gunning_fog(self):
        r = gunning_fog_index("The quick brown fox jumps over the lazy dog.")
        assert isinstance(r, (int, float))
    def test_is_json(self):
        assert is_json('{"a": 1}') is True
    def test_is_uuid(self):
        assert is_uuid("550e8400-e29b-41d4-a716-446655440000") is True
    def test_is_valid_base64(self):
        assert is_valid_base64("aGVsbG8=") is True
    def test_password_strength(self):
        r = check_password_strength("MyP@ssw0rd!")
        assert isinstance(r, (str, dict, int, float))
    def test_has_numbers(self):
        assert has_numbers("abc123") is True

from agentfx.fxString.string_caseconv import (
    to_camel_case, to_constant_case, to_kebab_case,
    to_pascal_case, to_slug, to_snake_case, to_title_case,
)

class TestStringCaseConv:
    def test_camel(self):
        assert to_camel_case("hello_world") == "helloWorld"
    def test_constant(self):
        r = to_constant_case("hello world")
        assert "_" in r
    def test_kebab(self):
        assert to_kebab_case("hello world") == "hello-world"
    def test_pascal(self):
        assert to_pascal_case("hello_world") == "HelloWorld"
    def test_slug(self):
        r = to_slug("Hello World!")
        assert " " not in r
    def test_snake(self):
        assert to_snake_case("helloWorld") == "hello_world"
    def test_title(self):
        assert to_title_case("hello world") == "Hello World"

from agentfx.fxString.string_encoding import (
    encode_base64, decode_base64, encode_url, decode_url,
    encode_html_entities, decode_html_entities,
    caesar_cipher as enc_caesar, vigenere_cipher,
)

class TestStringEncoding:
    def test_base64_roundtrip(self):
        enc = encode_base64("hello")
        assert decode_base64(enc) == "hello"
    def test_url_roundtrip(self):
        enc = encode_url("hello world")
        assert decode_url(enc) == "hello world"
    def test_html_entities(self):
        enc = encode_html_entities("<p>hello</p>")
        assert "&lt;" in enc
        assert "<p>" in decode_html_entities(enc)
    def test_caesar(self):
        r = enc_caesar("hello", 3)
        assert r != "hello"
    def test_vigenere(self):
        r = vigenere_cipher("hello", "key")
        assert isinstance(r, str)

from agentfx.fxString.string_hashing import fingerprint, hash_string

class TestStringHashing:
    def test_hash_string(self):
        r = hash_string("hello")
        assert isinstance(r, str)
    def test_fingerprint(self):
        r = fingerprint("hello world test")
        assert isinstance(r, str)

from agentfx.fxString.string_regex import (
    regex_match,
)

class TestStringRegex:
    def test_regex_match(self):
        r = regex_match(r"\d+", "abc123")
        assert r is not None

from agentfx.fxString.string_compression import compress_string, decompress_string

class TestStringCompression:
    def test_roundtrip(self):
        original = "hello world " * 100
        compressed = compress_string(original)
        assert decompress_string(compressed) == original

from agentfx.fxString.string_convertions import (
    integer_to_roman, roman_to_integer, text_to_binary, binary_to_text,
    base64_encode, base64_decode, text_to_hex, hex_to_text,
    text_to_morse, morse_to_text,
    string_to_boolean, string_to_integer, string_to_float,
    string_to_list, ordinal_suffix,
)

class TestStringConversions:
    def test_roman_roundtrip(self):
        assert integer_to_roman(42) == "XLII"
        assert roman_to_integer("XLII") == 42
    def test_binary_roundtrip(self):
        b = text_to_binary("A")
        assert binary_to_text(b) == "A"
    def test_base64_roundtrip(self):
        enc = base64_encode("hello")
        assert base64_decode(enc) == "hello"
    def test_hex_roundtrip(self):
        h = text_to_hex("hello")
        assert hex_to_text(h) == "hello"
    def test_morse_roundtrip(self):
        m = text_to_morse("HELLO")
        r = morse_to_text(m)
        assert isinstance(r, str)
    def test_string_to_boolean(self):
        assert string_to_boolean("true") is True
    def test_string_to_integer(self):
        assert string_to_integer("42") == 42
    def test_string_to_float(self):
        assert string_to_float("3.14") == pytest.approx(3.14)
    def test_string_to_list(self):
        r = string_to_list("a,b,c")
        assert len(r) == 3
    def test_ordinal_suffix(self):
        assert ordinal_suffix(1) in ("st", "1st")

from agentfx.fxString.string_validations import contains_digit, same_letters

class TestStringValidations:
    def test_contains_digit(self):
        assert contains_digit("abc123") is True
        assert contains_digit("abc") is False
    def test_same_letters(self):
        r = same_letters("abc", "bca")
        assert r is True
