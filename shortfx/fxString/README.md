# fxString Functions Documentation

Complete reference for all string manipulation, conversion, validation, and formatting functions in the shortfx fxString module.

## Overview

The fxString module provides comprehensive string manipulation functions for shortfx, including:
- **Conversions**: Parse strings to numbers, dates, JSON, booleans, Roman numerals, Morse, binary
- **Operations**: Substring, replace, split, extract, concatenate, deduplicate
- **Format**: Capitalize, pad, normalize, format names/emails/URLs, pluralize
- **Evaluations**: Validate formats, check content, parse emails, palindromes, anagrams, entropy
- **Similarity**: Calculate string similarity using various algorithms (Levenshtein, Jaro-Winkler, cosine, etc.)
- **Encoding**: Base64, URL percent-encoding, HTML entities
- **Case Conversion**: camelCase, PascalCase, snake_case, kebab-case, CONSTANT_CASE, slug, Title Case
- **Regex**: Match, extract, split, count with regex patterns
- **Hashing**: SHA-256, MD5, fingerprinting for deduplication
- **Compression**: zlib compression with Base64 transport
- **Spanish**: NIF/NIE/CIF validation, Spanish text processing
- **Validations**: Check patterns and content
- **Spellcheck**: Text normalization

### Additional Resources

- **Practical Use Cases** - Real-world examples and patterns for string similarity, spellcheck, autocompletion, and more
  - **[English Version (USE_CASES_EN.md)](USE_CASES_EN.md)** 
  - **[Spanish Version (USE_CASES.md)](USE_CASES.md)**
- **[Spanish Functions Guide](README_string_spanish.md)** - Specialized guide for Spanish language processing (DNI/NIE/CIF validation, phonetic reduction)

## Module Structure

- **string_convertions.py**: Functions for converting strings to other data types
- **string_operations.py**: Core string manipulation and extraction functions
- **string_format.py**: Text formatting and normalization functions
- **string_evaluations.py**: String validation and pattern matching functions
- **string_similarity.py**: String comparison and similarity algorithms
- **string_encoding.py**: Base64, URL, and HTML entity encoding/decoding
- **string_caseconv.py**: Naming convention conversions (camelCase, snake_case, etc.)
- **string_regex.py**: High-level regex wrappers (match, extract, split, count)
- **string_hashing.py**: Cryptographic hashing and deduplication fingerprinting
- **string_compression.py**: zlib text compression with Base64 transport
- **string_spanish.py**: Spanish-specific validation and processing functions
- **string_spellcheck.py**: Text normalization and spell-checking utilities
- **string_validations.py**: Character and pattern validation functions

---

## Table of Contents

- [Additional Resources](#additional-resources)
- [Function Categories](#function-categories)
  - [String Conversions](#string-conversions)
  - [String Operations](#string-operations)
  - [String Format](#string-format)
  - [String Evaluations](#string-evaluations)
  - [String Similarity](#string-similarity)
  - [String Encoding](#string-encoding)
  - [String Case Conversion](#string-case-conversion)
  - [String Regex](#string-regex)
  - [String Hashing](#string-hashing)
  - [String Compression](#string-compression)
  - [String Spanish](#string-spanish)
  - [String Validations](#string-validations)
  - [String Spellcheck](#string-spellcheck)
- [Function Index](#function-index)

---

## Function Categories

### String Conversions
- [replace_void](#replace_void) - Replaces empty or None values with specified replacement
- [none_to_string](#none_to_string) - Converts None to empty string, preserves original otherwise
- [string_to_integer](#string_to_integer) - Converts string to integer or None if fails
- [string_to_float](#string_to_float) - Converts string to float or None if fails
- [string_to_number](#string_to_number) - Converts string to integer or float based on type
- [string_to_date](#string_to_date) - Converts string to date or datetime object
- [string_to_datetime](#string_to_datetime) - Converts string to datetime.datetime object
- [split_all](#split_all) - Splits string by common delimiters, removes empty strings
- [split_by_substrings](#split_by_substrings) - Splits string by substring list, preserves separators
- [extract_and_decode_json](#extract_and_decode_json) - Extracts and decodes JSON from fenced block
- [string_to_boolean](#string_to_boolean) - Converts truthy/falsy string to boolean
- [boolean_to_string](#boolean_to_string) - Converts boolean to "true"/"false" string
- [string_to_list](#string_to_list) - Splits string into list by delimiter
- [integer_to_roman](#integer_to_roman) - Converts integer to Roman numeral string
- [roman_to_integer](#roman_to_integer) - Converts Roman numeral string to integer
- [text_to_binary](#text_to_binary) - Converts text to binary representation
- [binary_to_text](#binary_to_text) - Converts binary string back to text
- [text_to_morse](#text_to_morse) - Encodes text to Morse code
- [morse_to_text](#morse_to_text) - Decodes Morse code back to text
- [encode_base64](#encode_base64) - Encodes string to Base64 representation
- [decode_base64](#decode_base64) - Decodes Base64 string back to plain text
- [encode_url](#encode_url) - Applies percent-encoding for safe URL use
- [decode_url](#decode_url) - Decodes percent-encoded URL string
- [char_from_code](#char_from_code) - Character from Unicode code point (UNICHAR)
- [code_from_char](#code_from_char) - Unicode code point from character (UNICODE)
- [value_to_text](#value_to_text) - Value to text with optional formatting (VALUETOTEXT)
- [to_full_width](#to_full_width) - Convert half-width characters to full-width (DBCS)
- [to_half_width](#to_half_width) - Convert full-width characters to half-width (ASC)
- [text_to_hex](#text_to_hex) - Converts text to hexadecimal byte representation
- [hex_to_text](#hex_to_text) - Converts hexadecimal string back to text

### String Operations
- [ascii_from_char](#ascii_from_char) - Returns Unicode/ASCII code of first character
- [char_from_ascii](#char_from_ascii) - Returns character from Unicode/ASCII code value
- [count_words](#count_words) - Counts number of words in string
- [count_characters](#count_characters) - Counts occurrences of specific character in string
- [position_in_string](#position_in_string) - Finds all positions where substring appears (1-indexed)
- [random_string](#random_string) - Generates random string of specified length
- [reverse_string](#reverse_string) - Reverses characters in string
- [replace_string](#replace_string) - Replaces all occurrences of substring with another
- [replace_by_position](#replace_by_position) - Replaces a segment by position and length (Excel REPLACE)
- [replace_first_occurrence](#replace_first_occurrence) - Replaces only first occurrence of substring
- [replace_last_occurrence](#replace_last_occurrence) - Replaces only last occurrence of substring
- [regex_replace](#regex_replace) - Replaces all matches of a regex pattern (Excel REGEXREPLACE)
- [truncate_string](#truncate_string) - Truncates string to maximum length with ellipsis
- [substring](#substring) - Extracts substring from given position and length
- [left_substring](#left_substring) - Returns leftmost n characters of string
- [right_substring](#right_substring) - Returns rightmost n characters of string
- [common_substring](#common_substring) - Finds longest common substring between two strings
- [substring_on_left](#substring_on_left) - Extracts substring left of first pattern occurrence
- [substring_on_right](#substring_on_right) - Extracts substring right of first pattern occurrence
- [substring_between_pattern](#substring_between_pattern) - Extracts substring between two pattern occurrences
- [substring_from_delimiters](#substring_from_delimiters) - Extracts content between specified delimiters
- [extract_first_number](#extract_first_number) - Extracts first number (integer/float) from string
- [extract_last_number](#extract_last_number) - Extracts last number (integer/float) from string
- [extract_numbers](#extract_numbers) - Extracts all numbers (integers/floats) from string
- [join_to_string](#join_to_string) - Joins iterable of strings with separator
- [erase_specialchar](#erase_specialchar) - Removes special characters, optionally allows spaces/underscores
- [erase_digits](#erase_digits) - Removes all digits from string
- [erase_lspaces](#erase_lspaces) - Removes leading (left) spaces from string (VBA LTrim)
- [erase_lrspaces](#erase_lrspaces) - Removes leading and trailing spaces from string
- [erase_rspaces](#erase_rspaces) - Removes trailing (right) spaces from string (VBA RTrim)
- [erase_allspaces](#erase_allspaces) - Removes all spaces from string
- [distinct_words](#distinct_words) - Returns list of unique words from string
- [distinct_split](#distinct_split) - Splits delimited string, removes duplicates, re-joins
- [move_word](#move_word) - Moves word from one position to another
- [concatenate_strings](#concatenate_strings) - Concatenates two strings together
- [add_quotes](#add_quotes) - Adds quotes around string (single or double)
- [slugify](#slugify) - Converts text to URL-friendly slug
- [extract_urls](#extract_urls) - Extracts all URLs from text
- [extract_emails](#extract_emails) - Extracts all email addresses from text
- [repeat_string](#repeat_string) - Repeats string n times
- [center_string](#center_string) - Centers string within given width
- [strip_html_tags](#strip_html_tags) - Removes HTML tags from text
- [clean_non_printable](#clean_non_printable) - Removes non-printable characters
- [abbreviate](#abbreviate) - Truncates text with ellipsis at word boundary
- [generate_initials](#generate_initials) - Generates initials from name
- [wrap_text](#wrap_text) - Word-wrap to fixed column width
- [count_lines](#count_lines) - Counts lines in multiline text
- [get_line](#get_line) - Gets specific line by number (1-indexed)
- [remove_blank_lines](#remove_blank_lines) - Removes blank/whitespace-only lines
- [sort_lines](#sort_lines) - Sorts lines alphabetically
- [deduplicate_words](#deduplicate_words) - Removes duplicate words preserving order
- [surround](#surround) - Wraps text with string on both sides
- [word_at](#word_at) - Gets word at position (0-indexed) from text
- [substitute](#substitute) - Replaces occurrences of old text with new text (SUBSTITUTE)
- [text_before](#text_before) - Text before the Nth delimiter (TEXTBEFORE)
- [text_after](#text_after) - Text after the Nth delimiter (TEXTAFTER)
- [text_split](#text_split) - Split text by delimiters into list (TEXTSPLIT)
- [count_syllables](#count_syllables) - Estimates syllable count in text (English/Spanish)
- [soundex](#soundex) - Computes Soundex phonetic code for a word
- [metaphone](#metaphone) - Computes Metaphone phonetic code for a word
- [extract_domain_from_url](#extract_domain_from_url) - Extracts domain from a URL string
- [nysiis](#nysiis) - NYSIIS phonetic encoding (improved Soundex for names)
- [double_metaphone](#double_metaphone) - Double Metaphone phonetic encoding (primary + alternate)
- [cologne_phonetic](#cologne_phonetic) - Kölner Phonetik phonetic encoding (German-optimised)
- [longest_common_prefix](#longest_common_prefix) - Longest common prefix of two strings
- [longest_common_suffix](#longest_common_suffix) - Longest common suffix of two strings
- [normalize_unicode](#normalize_unicode) - Unicode normalization (NFC/NFD/NFKC/NFKD)

### String Format
- [sql_quote](#sql_quote) - Escapes single quotes for safe SQL queries
- [format_date](#format_date) - Formats date/datetime into specified string format
- [format_number](#format_number) - Formats number with decimal places and separators
- [capitalize_string](#capitalize_string) - Capitalizes string by mode (all/first/each word)
- [pad_string](#pad_string) - Pads string to length with character
- [to_upper](#to_upper) - Converts string to uppercase
- [to_lower](#to_lower) - Converts string to lowercase
- [normalize_spaces](#normalize_spaces) - Replaces multiple spaces with single, trims ends
- [normalize_symbols](#normalize_symbols) - Normalizes symbol spacing per typographical rules
- [flat_vowels](#flat_vowels) - Removes diacritical marks (accents) from vowels
- [ascii_string](#ascii_string) - Converts to ASCII, removing non-ASCII characters
- [format_email_address](#format_email_address) - Formats and normalizes email address (lowercase, trimmed)
- [format_url](#format_url) - Formats and normalizes URL
- [format_name](#format_name) - Formats person's name by specified rules
- [format_fullname](#format_fullname) - Formats full name, removes titles and normalizes
- [format_company_name](#format_company_name) - Formats company name, handles legal forms
- [camel_to_snake](#camel_to_snake) - Converts camelCase/PascalCase to snake_case
- [snake_to_camel](#snake_to_camel) - Converts snake_case to camelCase or PascalCase
- [word_wrap](#word_wrap) - Wraps text to specified line width at word boundaries
- [swap_case](#swap_case) - Inverts case of every character
- [indent_text](#indent_text) - Adds prefix to every line
- [dedent_text](#dedent_text) - Removes common leading whitespace
- [zfill](#zfill) - Pads with leading zeros
- [rot13](#rot13) - Applies ROT13 substitution cipher
- [format_list_as_sentence](#format_list_as_sentence) - Joins list as "a, b and c"
- [pluralize_count](#pluralize_count) - "1 item" / "3 items"
- [format_as_currency](#format_as_currency) - Formats number as currency string (DOLLAR)
- [fixed](#fixed) - Formats number with fixed decimals and thousands separators (FIXED)
- [dollar](#dollar) - Formats number as dollar currency text (DOLLAR)

### String Evaluations
- [contains_digit](#contains_digit) - Checks if string contains at least one digit
- [is_alphabetic](#is_alphabetic) - Checks if string contains only alphabetic characters
- [is_numeric](#is_numeric) - Checks if string represents valid number
- [is_internet_domain_format](#is_internet_domain_format) - Validates if string matches internet domain format
- [is_email_format](#is_email_format) - Validates if string matches email address format
- [is_url_format](#is_url_format) - Validates if string matches URL format
- [has_date_format](#has_date_format) - Checks if string can be interpreted as date
- [has_numbers](#has_numbers) - Checks if string contains any numeric digits
- [has_substring](#has_substring) - Checks if string contains specific substring
- [starts_with_substring](#starts_with_substring) - Checks if string starts with specific prefix
- [ends_with_substring](#ends_with_substring) - Checks if string ends with specific suffix
- [parse_email](#parse_email) - Parses email address into username and domain components
- [username_from_email](#username_from_email) - Extracts username portion from email address
- [domain_from_email](#domain_from_email) - Extracts domain portion from email address
- [word_frequency](#word_frequency) - Frequency of each word as dict
- [char_frequency](#char_frequency) - Frequency of each character as dict
- [sentence_count](#sentence_count) - Counts sentences by terminal punctuation
- [reading_time](#reading_time) - Estimated reading time in minutes
- [is_palindrome](#is_palindrome) - Checks if text is a palindrome
- [is_json](#is_json) - Checks if string is valid JSON
- [is_uuid](#is_uuid) - Checks if string is valid UUID format
- [is_ipv4](#is_ipv4) - Checks if string is valid IPv4 address
- [is_ipv6](#is_ipv6) - Checks if string is valid IPv6 address
- [is_credit_card_format](#is_credit_card_format) - Checks if string has valid credit card number format (Luhn)
- [count_sentences](#count_sentences) - Counts sentences in text
- [text_stats](#text_stats) - Dict with chars, words, sentences, lines, avg_word_length
- [is_anagram](#is_anagram) - Checks if two strings are anagrams
- [is_pangram](#is_pangram) - Checks if text uses all alphabet letters
- [is_valid_iban](#is_valid_iban) - Validates IBAN (format + MOD-97 check digit)
- [is_valid_isbn](#is_valid_isbn) - Validates ISBN-10 / ISBN-13
- [is_valid_luhn](#is_valid_luhn) - Generic Luhn (mod-10) algorithm validation
- [is_valid_ean](#is_valid_ean) - Validates EAN-8 / EAN-13 barcode
- [is_valid_swift_bic](#is_valid_swift_bic) - Validates SWIFT/BIC code (ISO 9362)
- [is_valid_isin](#is_valid_isin) - Validates ISIN (International Securities ID, Luhn on alphanumeric)
- [is_valid_cusip](#is_valid_cusip) - Validates CUSIP (9-character US securities ID)
- [is_valid_sedol](#is_valid_sedol) - Validates SEDOL (7-character UK securities ID)
- [is_valid_vin](#is_valid_vin) - Validates VIN (Vehicle Identification Number, 17 chars)
- [is_valid_issn](#is_valid_issn) - Validates ISSN (International Standard Serial Number, mod-11)

### String Similarity
- [calculate_similarity](#calculate_similarity) - Calculates similarity using specified algorithm
- [has_same_words](#has_same_words) - Checks if strings contain same words (order-independent)
- [find_common_words](#find_common_words) - Finds words appearing in both strings
- [has_same_characters](#has_same_characters) - Checks if strings contain same characters (anagram)
- [string_hamming_score](#string_hamming_score) - Calculates Hamming distance between two strings
- [string_levenshtein_score](#string_levenshtein_score) - Calculates Levenshtein distance between two strings
- [string_jarowinkler_score](#string_jarowinkler_score) - Calculates Jaro-Winkler similarity between two strings
- [string_jaccard_score](#string_jaccard_score) - Calculates Jaccard similarity coefficient between strings
- [string_similarity_score](#string_similarity_score) - Calculates multiple similarity scores using all algorithms
- [string_cosine_score](#string_cosine_score) - Cosine similarity between two strings
- [generate_ngrams](#generate_ngrams) - Generates character n-grams from text
- [find_closest_match](#find_closest_match) - Finds best match from candidate list
- [rank_by_similarity](#rank_by_similarity) - Ranks candidates by similarity score

### String Encoding
- [encode_base64](#encode_base64) - Encodes string to Base64
- [decode_base64](#decode_base64) - Decodes Base64 string
- [encode_url](#encode_url) - URL percent-encoding
- [decode_url](#decode_url) - Decodes percent-encoded URL
- [encode_html_entities](#encode_html_entities) - Encodes HTML special characters
- [decode_html_entities](#decode_html_entities) - Decodes HTML entities

### String Case Conversion
- [to_camel_case](#to_camel_case) - Converts to camelCase
- [to_pascal_case](#to_pascal_case) - Converts to PascalCase
- [to_snake_case](#to_snake_case) - Converts to snake_case
- [to_kebab_case](#to_kebab_case) - Converts to kebab-case
- [to_constant_case](#to_constant_case) - Converts to CONSTANT_CASE
- [to_slug](#to_slug) - Converts to url-slug (ASCII, lowered, hyphenated)
- [to_title_case](#to_title_case) - Smart Title Case respecting articles (en/es)

### String Regex
- [regex_match](#regex_match) - Tests if pattern matches anywhere
- [regex_extract](#regex_extract) - Extracts first regex match
- [regex_extract_all](#regex_extract_all) - Extracts all regex matches
- [regex_split](#regex_split) - Splits string by regex pattern
- [regex_count](#regex_count) - Counts regex pattern matches

### String Hashing
- [hash_string](#hash_string) - Generates hash digest (md5/sha256/sha512)
- [fingerprint](#fingerprint) - Normalized fingerprint for deduplication

### String Compression
- [compress_string](#compress_string) - Compresses text via zlib + Base64
- [decompress_string](#decompress_string) - Decompresses Base64/zlib string

### String Spanish
- [remove_spanish_stop_words](#remove_spanish_stop_words) - Removes common Spanish stop words from string
- [reduce_spanish_letters](#reduce_spanish_letters) - Reduces Spanish text to phonetic representation
- [nif_padding](#nif_padding) - Pads Spanish NIF/CIF to standard format
- [nif_parse](#nif_parse) - Parses and normalizes Spanish NIF/NIE/CIF
- [nif_letter](#nif_letter) - Calculates control letter for Spanish DNI
- [is_valid_dni](#is_valid_dni) - Validates Spanish DNI (Documento Nacional de Identidad)
- [is_valid_nie](#is_valid_nie) - Validates Spanish NIE (Número de Identidad de Extranjero)
- [is_valid_cif](#is_valid_cif) - Validates Spanish CIF (Certificado de Identificación Fiscal)
- [validate_spanish_nif](#validate_spanish_nif) - Validates Spanish NIF (DNI/NIE/CIF) by type
- [fix_spanish](#fix_spanish) - Fixes common Spanish character encoding issues

### String Validations
- [contains_digit](#contains_digit) - Checks if string contains at least one digit
- [same_letters](#same_letters) - Checks if strings contain exact same characters (anagram)

### String Spellcheck
- [normalize_text](#normalize_text) - Normalizes text by lowercasing and removing accents

---

## Function Index

**A**
- [add_quotes](#add_quotes) - Adds quotes around string (single or double)
- [ascii_from_char](#ascii_from_char) - Returns Unicode/ASCII code of first character
- [ascii_string](#ascii_string) - Converts to ASCII, removing non-ASCII characters
- [abbreviate](#abbreviate) - Truncates text with ellipsis at word boundary

**B**
- [binary_to_text](#binary_to_text) - Converts binary string back to text
- [boolean_to_string](#boolean_to_string) - Converts boolean to "true"/"false" string

**C**
- [camel_to_snake](#camel_to_snake) - Converts camelCase/PascalCase to snake_case
- [calculate_similarity](#calculate_similarity) - Calculates similarity using specified algorithm
- [capitalize_string](#capitalize_string) - Capitalizes string by mode (all/first/each word)
- [center_string](#center_string) - Centers string within given width
- [char_frequency](#char_frequency) - Frequency of each character as dict
- [char_from_ascii](#char_from_ascii) - Returns character from Unicode/ASCII code value
- [char_from_code](#char_from_code) - Character from Unicode code point (UNICHAR)
- [clean_non_printable](#clean_non_printable) - Removes non-printable characters
- [common_substring](#common_substring) - Finds longest common substring between two strings
- [compress_string](#compress_string) - Compresses text via zlib + Base64
- [code_from_char](#code_from_char) - Unicode code point from character (UNICODE)
- [concatenate_strings](#concatenate_strings) - Concatenates two strings together
- [contains_digit](#contains_digit) - Checks if string contains at least one digit
- [count_characters](#count_characters) - Counts occurrences of specific character in string
- [count_lines](#count_lines) - Counts lines in multiline text
- [count_words](#count_words) - Counts number of words in string

**D**
- [decode_base64](#decode_base64) - Decodes Base64 string back to plain text
- [decode_html_entities](#decode_html_entities) - Decodes HTML entities
- [decode_url](#decode_url) - Decodes percent-encoded URL string
- [decompress_string](#decompress_string) - Decompresses Base64/zlib string
- [dedent_text](#dedent_text) - Removes common leading whitespace
- [deduplicate_words](#deduplicate_words) - Removes duplicate words preserving order
- [distinct_words](#distinct_words) - Returns list of unique words from string
- [distinct_split](#distinct_split) - Splits delimited string, removes duplicates, re-joins
- [domain_from_email](#domain_from_email) - Extracts domain portion from email address

**E**
- [ends_with_substring](#ends_with_substring) - Checks if string ends with specific suffix
- [erase_allspaces](#erase_allspaces) - Removes all spaces from string
- [erase_digits](#erase_digits) - Removes all digits from string
- [erase_lrspaces](#erase_lrspaces) - Removes leading and trailing spaces from string
- [erase_lspaces](#erase_lspaces) - Removes leading (left) spaces from string (VBA LTrim)
- [erase_rspaces](#erase_rspaces) - Removes trailing (right) spaces from string (VBA RTrim)
- [erase_specialchar](#erase_specialchar) - Removes special characters, optionally allows spaces/underscores
- [extract_and_decode_json](#extract_and_decode_json) - Extracts and decodes JSON from fenced block
- [extract_emails](#extract_emails) - Extracts all email addresses from text
- [extract_first_number](#extract_first_number) - Extracts first number (integer/float) from string
- [extract_last_number](#extract_last_number) - Extracts last number (integer/float) from string
- [extract_numbers](#extract_numbers) - Extracts all numbers (integers/floats) from string
- [extract_urls](#extract_urls) - Extracts all URLs from text

**F**
- [find_closest_match](#find_closest_match) - Finds best match from candidate list
- [find_common_words](#find_common_words) - Finds words appearing in both strings
- [fingerprint](#fingerprint) - Normalized fingerprint for deduplication
- [fix_spanish](#fix_spanish) - Fixes common Spanish character encoding issues
- [flat_vowels](#flat_vowels) - Removes diacritical marks (accents) from vowels
- [format_company_name](#format_company_name) - Formats company name, handles legal forms
- [format_date](#format_date) - Formats date/datetime into specified string format
- [format_email_address](#format_email_address) - Formats and normalizes email address (lowercase, trimmed)
- [format_fullname](#format_fullname) - Formats full name, removes titles and normalizes
- [format_list_as_sentence](#format_list_as_sentence) - Joins list as "a, b and c"
- [format_name](#format_name) - Formats person's name by specified rules
- [format_number](#format_number) - Formats number with decimal places and separators
- [format_url](#format_url) - Formats and normalizes URL
- [format_as_currency](#format_as_currency) - Formats number as currency string (DOLLAR)
- [fixed](#fixed) - Formats number with fixed decimals and thousands separators (FIXED)
- [dollar](#dollar) - Formats number as dollar currency text (DOLLAR)

**G**
- [generate_initials](#generate_initials) - Generates initials from name
- [generate_ngrams](#generate_ngrams) - Generates character n-grams from text
- [get_line](#get_line) - Gets specific line by number (1-indexed)

**H**
- [has_date_format](#has_date_format) - Checks if string can be interpreted as date
- [has_numbers](#has_numbers) - Checks if string contains any numeric digits
- [has_same_characters](#has_same_characters) - Checks if strings contain same characters (anagram)
- [has_same_words](#has_same_words) - Checks if strings contain same words (order-independent)
- [has_substring](#has_substring) - Checks if string contains specific substring
- [hash_string](#hash_string) - Generates hash digest (md5/sha256/sha512)

**I**
- [indent_text](#indent_text) - Adds prefix to every line
- [integer_to_roman](#integer_to_roman) - Converts integer to Roman numeral string
- [is_alphabetic](#is_alphabetic) - Checks if string contains only alphabetic characters
- [is_anagram](#is_anagram) - Checks if two strings are anagrams
- [is_email_format](#is_email_format) - Validates if string matches email address format
- [is_internet_domain_format](#is_internet_domain_format) - Validates if string matches internet domain format
- [is_numeric](#is_numeric) - Checks if string represents valid number
- [is_palindrome](#is_palindrome) - Checks if text is a palindrome
- [is_pangram](#is_pangram) - Checks if text uses all alphabet letters
- [is_url_format](#is_url_format) - Validates if string matches URL format
- [is_valid_cif](#is_valid_cif) - Validates Spanish CIF (Certificado de Identificación Fiscal)
- [is_valid_dni](#is_valid_dni) - Validates Spanish DNI (Documento Nacional de Identidad)
- [is_valid_nie](#is_valid_nie) - Validates Spanish NIE (Número de Identidad de Extranjero)

**J**
- [join_to_string](#join_to_string) - Joins iterable of strings with separator

**L**
- [left_substring](#left_substring) - Returns leftmost n characters of string

**M**
- [move_word](#move_word) - Moves word from one position to another

**N**
- [nif_letter](#nif_letter) - Calculates control letter for Spanish DNI
- [nif_padding](#nif_padding) - Pads Spanish NIF/CIF to standard format
- [nif_parse](#nif_parse) - Parses and normalizes Spanish NIF/NIE/CIF
- [none_to_string](#none_to_string) - Converts None to empty string, preserves original otherwise
- [normalize_spaces](#normalize_spaces) - Replaces multiple spaces with single, trims ends
- [normalize_symbols](#normalize_symbols) - Normalizes symbol spacing per typographical rules
- [normalize_text](#normalize_text) - Normalizes text by lowercasing and removing accents
**P**
- [pad_string](#pad_string) - Pads string to length with character
- [parse_email](#parse_email) - Parses email address into username and domain components
- [pluralize_count](#pluralize_count) - "1 item" / "3 items"
- [position_in_string](#position_in_string) - Finds all positions where substring appears (1-indexed)

**R**
- [random_string](#random_string) - Generates random string of specified length
- [rank_by_similarity](#rank_by_similarity) - Ranks candidates by similarity score
- [reading_time](#reading_time) - Estimated reading time in minutes
- [reduce_spanish_letters](#reduce_spanish_letters) - Reduces Spanish text to phonetic representation
- [regex_count](#regex_count) - Counts regex pattern matches
- [regex_extract](#regex_extract) - Extracts first regex match
- [regex_extract_all](#regex_extract_all) - Extracts all regex matches
- [regex_match](#regex_match) - Tests if pattern matches anywhere
- [regex_replace](#regex_replace) - Replaces all matches of a regex pattern (Excel REGEXREPLACE)
- [regex_split](#regex_split) - Splits string by regex pattern
- [remove_blank_lines](#remove_blank_lines) - Removes blank/whitespace-only lines
- [remove_spanish_stop_words](#remove_spanish_stop_words) - Removes common Spanish stop words from string
- [repeat_string](#repeat_string) - Repeats string n times
- [replace_by_position](#replace_by_position) - Replaces a segment by position and length (Excel REPLACE)
- [replace_first_occurrence](#replace_first_occurrence) - Replaces only first occurrence of substring
- [replace_last_occurrence](#replace_last_occurrence) - Replaces only last occurrence of substring
- [replace_string](#replace_string) - Replaces all occurrences of substring with another
- [replace_void](#replace_void) - Replaces empty or None values with specified replacement
- [reverse_string](#reverse_string) - Reverses characters in string
- [right_substring](#right_substring) - Returns rightmost n characters of string
- [roman_to_integer](#roman_to_integer) - Converts Roman numeral string to integer
- [rot13](#rot13) - Applies ROT13 substitution cipher

**S**
- [same_letters](#same_letters) - Checks if strings contain exact same characters (anagram)
- [sentence_count](#sentence_count) - Counts sentences by terminal punctuation
- [slugify](#slugify) - Converts text to URL-friendly slug
- [sort_lines](#sort_lines) - Sorts lines alphabetically
- [split_all](#split_all) - Splits string by common delimiters, removes empty strings
- [split_by_substrings](#split_by_substrings) - Splits string by substring list, preserves separators
- [snake_to_camel](#snake_to_camel) - Converts snake_case to camelCase or PascalCase
- [sql_quote](#sql_quote) - Escapes single quotes for safe SQL queries
- [starts_with_substring](#starts_with_substring) - Checks if string starts with specific prefix
- [string_cosine_score](#string_cosine_score) - Cosine similarity between two strings
- [string_hamming_score](#string_hamming_score) - Calculates Hamming distance between two strings
- [string_jaccard_score](#string_jaccard_score) - Calculates Jaccard similarity coefficient between strings
- [string_jarowinkler_score](#string_jarowinkler_score) - Calculates Jaro-Winkler similarity between two strings
- [string_levenshtein_score](#string_levenshtein_score) - Calculates Levenshtein distance between two strings
- [string_similarity_score](#string_similarity_score) - Calculates multiple similarity scores using all algorithms
- [string_to_boolean](#string_to_boolean) - Converts truthy/falsy string to boolean
- [string_to_date](#string_to_date) - Converts string to date or datetime object
- [string_to_datetime](#string_to_datetime) - Converts string to datetime.datetime object
- [string_to_float](#string_to_float) - Converts string to float or None if fails
- [string_to_integer](#string_to_integer) - Converts string to integer or None if fails
- [string_to_list](#string_to_list) - Splits string into list by delimiter
- [string_to_number](#string_to_number) - Converts string to integer or float based on type
- [substring](#substring) - Extracts substring from given position and length
- [substring_between_pattern](#substring_between_pattern) - Extracts substring between two pattern occurrences
- [substring_from_delimiters](#substring_from_delimiters) - Extracts content between specified delimiters
- [substring_on_left](#substring_on_left) - Extracts substring left of first pattern occurrence
- [substring_on_right](#substring_on_right) - Extracts substring right of first pattern occurrence
- [substitute](#substitute) - Replaces occurrences of old text with new text (SUBSTITUTE)

- [strip_html_tags](#strip_html_tags) - Removes HTML tags from text
- [surround](#surround) - Wraps text with string on both sides
- [swap_case](#swap_case) - Inverts case of every character

**T**
- [text_after](#text_after) - Text after the Nth delimiter (TEXTAFTER)
- [text_before](#text_before) - Text before the Nth delimiter (TEXTBEFORE)
- [text_split](#text_split) - Split text by delimiters into list (TEXTSPLIT)
- [text_to_binary](#text_to_binary) - Converts text to binary representation
- [text_to_morse](#text_to_morse) - Encodes text to Morse code
- [to_camel_case](#to_camel_case) - Converts to camelCase
- [to_constant_case](#to_constant_case) - Converts to CONSTANT_CASE
- [to_full_width](#to_full_width) - Convert half-width characters to full-width (DBCS)
- [to_half_width](#to_half_width) - Convert full-width characters to half-width (ASC)
- [to_kebab_case](#to_kebab_case) - Converts to kebab-case
- [to_lower](#to_lower) - Converts string to lowercase
- [to_pascal_case](#to_pascal_case) - Converts to PascalCase
- [to_slug](#to_slug) - Converts to url-slug
- [to_snake_case](#to_snake_case) - Converts to snake_case
- [to_title_case](#to_title_case) - Smart Title Case respecting articles
- [to_upper](#to_upper) - Converts string to uppercase
- [truncate_string](#truncate_string) - Truncates string to maximum length with ellipsis

**U**
- [username_from_email](#username_from_email) - Extracts username portion from email address

**V**
- [validate_spanish_nif](#validate_spanish_nif) - Validates Spanish NIF (DNI/NIE/CIF) by type
- [value_to_text](#value_to_text) - Value to text with optional formatting (VALUETOTEXT)

**W**
- [word_frequency](#word_frequency) - Frequency of each word as dict
- [word_wrap](#word_wrap) - Wraps text to specified line width at word boundaries
- [wrap_text](#wrap_text) - Word-wrap to fixed column width

**Z**
- [zfill](#zfill) - Pads with leading zeros

---

## String Conversions

Functions for converting strings to other data types and splitting/parsing operations.

### replace_void

Replaces empty or None values with a specified replacement value.

**Args:**
- `primary_value` (Any): The primary value to check
- `replacement_value` (Any): The value to use if primary_value is empty/None. Defaults to 'NaN'

**Returns:**
- Any: replacement_value if primary_value is empty/None/zero-length, otherwise returns primary_value

**Usage Example:**
```python
>>> replace_void("", "default")
'default'
>>> replace_void(None, 0)
0
>>> replace_void([], [1, 2, 3])
[1, 2, 3]
>>> replace_void("hello", "default")
'hello'
```

**Cost:** O(1) for most types

---

### none_to_string

Converts a None value to an empty string; otherwise, returns the original value.

**Args:**
- `value` (str | None): The input value, which could be a string or None

**Returns:**
- str: An empty string if the input 'value' was None, otherwise the original value

**Usage Example:**
```python
>>> none_to_string("hello")
'hello'
>>> none_to_string(None)
''
```

**Cost:** O(1) - constant time operation

---

### string_to_integer

Converts a string to an integer, returning None if conversion fails.

**Args:**
- `input_string` (str): The string to be converted to an integer

**Returns:**
- int | None: The integer representation of the cleaned string, or None if the conversion is not possible

**Usage Example:**
```python
>>> string_to_integer("123")
123
>>> string_to_integer("-45")
-45
>>> string_to_integer("abc123def")
123
>>> string_to_integer("abc")
None
```

**Cost:** O(n), where n is the length of the input string, due to regex processing

---

### string_to_float

Converts a string to a float, returning None if conversion fails.

**Args:**
- `input_string` (str): The string to be converted to a float

**Returns:**
- float | None: The float representation of the cleaned string, or None if the conversion is not possible

**Usage Example:**
```python
>>> string_to_float("123.45")
123.45
>>> string_to_float("123,45")
123.45
>>> string_to_float("abc123.45def")
123.45
```

**Cost:** O(n), where n is the length of the input string, due to regex processing

---

### string_to_number

Converts a string to an integer or float based on the specified target type.

**Args:**
- `input_string` (str): The string to convert
- `target_type` (str): The desired numeric type ('integer' or 'float'). Defaults to 'string'

**Returns:**
- int | float | None: The converted number, or None if conversion fails or target_type is invalid

**Usage Example:**
```python
>>> string_to_number("123", "integer")
123
>>> string_to_number("123.45", "float")
123.45
>>> string_to_number("abc123def", "integer")
123
```

**Cost:** O(n), where n is the length of input_string (delegates to string_to_integer or string_to_float)

---

### string_to_date

Converts a string to a date or datetime object based on common formats.

**Args:**
- `input_value` (str | date | dt): The string or existing date/datetime object to be converted or returned

**Returns:**
- date | dt | None: A datetime.date object if the string represents only a date, a datetime.datetime object if the string includes time information, or None if the string cannot be parsed

**Usage Example:**
```python
>>> string_to_date("2023-10-26")
datetime.date(2023, 10, 26)
>>> string_to_date("2023-10-26 14:30:00")
datetime.datetime(2023, 10, 26, 14, 30)
```

**Cost:** O(k * m), where k is the number of formats and m is the length of input_value

---

### string_to_datetime

Converts a string to a datetime.datetime object using common date and datetime formats.

**Args:**
- `input_value` (str | date | dt): The value to convert. Can be a string, date, or datetime

**Returns:**
- dt | None: A datetime.datetime object if conversion is successful, otherwise None

**Usage Example:**
```python
>>> string_to_datetime("2023-10-26 14:30:00")
datetime.datetime(2023, 10, 26, 14, 30)
>>> string_to_datetime("2023-10-26")
datetime.datetime(2023, 10, 26, 0, 0)
```

**Cost:** O(k * m), where k is the number of formats and m is the length of the input string

---

### split_all

Splits a string by an expanded set of common delimiters and removes any empty strings from the result.

**Args:**
- `input_string` (str): The string to be split
- `delimiter_pattern` (str): The regular expression pattern to use as a delimiter. Defaults to `'[.\-_\s,/():;\'"\\]+'`

**Returns:**
- list: A list of non-empty strings resulting from the split operation

**Raises:**
- TypeError: If 'input_string' is not a string

**Usage Example:**
```python
>>> split_all("hello-world_123/test")
['hello', 'world', '123', 'test']
```

**Cost:** O(n), where n is the length of the input string

---

### split_by_substrings

Splits a string by a list of substrings (separators), preserving the separators.

**Args:**
- `input_string` (str): The string to be split
- `separators` (list[str]): A list of strings to use as separators

**Returns:**
- list[str]: A list of strings, where each string represents a segment of the original string

**Raises:**
- TypeError: If 'input_string' is not a string or 'separators' is not a list
- ValueError: If 'separators' is an empty list or contains non-string elements

**Usage Example:**
```python
>>> split_by_substrings("Name: John Doe; Age: 30, City: New York", [":", ";", ","])
['Name:', ' John Doe;', ' Age:', ' 30,', ' City:', ' New York']
```

**Cost:** O(n + m * k), where n is the string length, m is the number of separators, and k is the number of segments

---

### extract_and_decode_json

Extracts and decodes a JSON string embedded within a block delimited by ```json\n and \n```.

**Args:**
- `text_content` (str): The input string potentially containing a fenced JSON block

**Returns:**
- Optional[dict]: A dictionary representing the decoded JSON if found and successfully parsed; otherwise, returns None

**Usage Example:**
```python
>>> example_string = "Some text.\\n```json\\n{\\"key\\": \\"value\\"}\\n```\\nMore text."
>>> extract_and_decode_json(example_string)
{'key': 'value'}
```

**Cost:** O(n), where n is the length of the text content, due to regex search

---

## String Operations

Functions for manipulating, extracting, and transforming strings.

### ascii_from_char

Devuelve el valor entero (código Unicode/ASCII) del primer carácter de una cadena.

**Args:**
- `character` (str): La cadena de la que se obtendrá el valor entero del primer carácter

**Returns:**
- int: El valor entero correspondiente al carácter

**Raises:**
- TypeError: Si la entrada no es una cadena
- ValueError: Si la cadena de entrada está vacía

**Usage Example:**
```python
>>> ascii_from_char("A")
65
>>> ascii_from_char("€")
8364
```

**Cost:** O(1)

---

### char_from_ascii

Devuelve el carácter correspondiente a un valor entero (código Unicode/ASCII).

**Args:**
- `integer_code` (int): El valor entero (código Unicode/ASCII) del carácter deseado. Debe ser un valor Unicode válido (0 a 1,114,111)

**Returns:**
- str: El carácter correspondiente al valor entero

**Raises:**
- TypeError: Si la entrada no es un entero
- ValueError: Si el entero está fuera del rango de los códigos Unicode válidos

**Usage Example:**
```python
>>> char_from_ascii(65)
'A'
>>> char_from_ascii(8364)
'€'
```

**Cost:** O(1)

---

### count_words

Counts the number of words in a string.

**Args:**
- `input_string` (str): The string to be analyzed

**Returns:**
- int: The number of words in the string

**Usage Example:**
```python
>>> count_words("Hello world from Python")
4
>>> count_words("   Multiple   spaces   ")
2
```

**Cost:** O(n), where n is the length of the input string

---

### count_characters

Counts the occurrences of a specific character in a string.

**Args:**
- `input_string` (str): The string to search
- `target_char` (str): The character to count

**Returns:**
- int: The number of times target_char appears in input_string

**Usage Example:**
```python
>>> count_characters("hello world", "l")
3
>>> count_characters("Python", "z")
0
```

**Cost:** O(n), where n is the length of the input string

---

### position_in_string

Finds all positions where a substring appears in a string (1-indexed).

**Args:**
- `main_string` (str): The string to search in
- `substring` (str): The substring to find
- `start_position` (int): The position to start searching from (1-indexed). Defaults to 1

**Returns:**
- list[int]: A list of all positions (1-indexed) where the substring is found

**Usage Example:**
```python
>>> position_in_string("hello world hello", "hello")
[1, 13]
>>> position_in_string("test", "xyz")
[]
```

**Cost:** O(n * m), where n is the length of main_string and m is the length of substring

---

### random_string

Generates a random string of a specified length.

**Args:**
- `length` (int): The desired length of the random string. Defaults to 10
- `secure` (bool): If True, uses cryptographically secure random generation. Defaults to True

**Returns:**
- str: A random string consisting of ASCII letters and digits

**Usage Example:**
```python
>>> len(random_string(15))
15
>>> random_string(5, secure=False)
'aB3x9'  # Example output
```

**Cost:** O(n), where n is the desired length

---

### reverse_string

Reverses the characters in a string.

**Args:**
- `input_string` (str): The string to be reversed

**Returns:**
- str: The reversed string

**Usage Example:**
```python
>>> reverse_string("hello")
'olleh'
>>> reverse_string("Python")
'nohtyP'
```

**Cost:** O(n), where n is the length of the input string

---

### replace_string

Replaces all occurrences of a substring with another substring.

**Args:**
- `original_string` (str): The original string
- `old_substring` (str): The substring to be replaced
- `new_substring` (str): The replacement substring

**Returns:**
- str: The modified string with all occurrences replaced

**Usage Example:**
```python
>>> replace_string("hello world", "world", "Python")
'hello Python'
```

**Cost:** O(n), where n is the length of the original string

---

### replace_first_occurrence

Replaces only the first occurrence of a substring.

**Args:**
- `original_string` (str): The original string
- `old_substring` (str): The substring to be replaced
- `new_substring` (str): The replacement substring

**Returns:**
- str: The modified string with the first occurrence replaced

**Usage Example:**
```python
>>> replace_first_occurrence("test test test", "test", "exam")
'exam test test'
```

**Cost:** O(n), where n is the length of the original string

---

### replace_last_occurrence

Replaces only the last occurrence of a substring.

**Args:**
- `original_string` (str): The original string
- `old_substring` (str): The substring to be replaced
- `new_substring` (str): The replacement substring

**Returns:**
- str: The modified string with the last occurrence replaced

**Usage Example:**
```python
>>> replace_last_occurrence("test test test", "test", "exam")
'test test exam'
```

**Cost:** O(n), where n is the length of the original string

---

### replace_by_position

Replaces a segment of a string defined by position and length with new text. Equivalent to Excel's REPLACE function. Uses 1-based indexing.

**Args:**
- `original_string` (str): The original string in which the replacement will be made
- `start_position` (int): The 1-based position of the first character to replace
- `num_chars` (int): The number of characters to replace from start_position
- `new_text` (str): The text to insert in place of the removed segment

**Returns:**
- str: The resulting string after the positional replacement

**Raises:**
- `TypeError`: If original_string or new_text is not str, or if start_position/num_chars is not int
- `ValueError`: If start_position < 1 or num_chars < 0

**Usage Example:**
```python
>>> replace_by_position("abcdefghijk", 6, 5, "*")
'abcde*k'
>>> replace_by_position("2024", 3, 2, "25")
'2025'
>>> replace_by_position("Hello World", 1, 5, "Goodbye")
'Goodbye World'
```

**Cost:** O(n), where n is the length of original_string

---

### regex_replace

Replaces all occurrences matching a regular expression pattern with a replacement string. Equivalent to Excel's REGEXREPLACE function. Supports backreferences in the replacement string.

**Args:**
- `text` (str): The input string to modify
- `pattern` (str): The regular expression pattern to match
- `replacement` (str): The replacement string (supports regex backreferences)
- `case_insensitive` (bool): If True, the pattern matching ignores case. Defaults to False

**Returns:**
- str: The text with all matching occurrences replaced

**Raises:**
- `TypeError`: If text, pattern, or replacement is not a string
- `re.error`: If the pattern is not a valid regular expression

**Usage Example:**
```python
>>> regex_replace("Hello 123 World 456", r"\d+", "X")
'Hello X World X'
>>> regex_replace("test@email.com", r"@.*", "@example.com")
'test@example.com'
>>> regex_replace("FooBar FooBaz", r"foo", "QUX", case_insensitive=True)
'QUXBar QUXBaz'
```

**Cost:** O(n*m), where n is text length and m is pattern complexity

---

### truncate_string

Truncates a string to a maximum length, optionally adding an ellipsis.

**Args:**
- `input_string` (str): The string to truncate
- `max_length` (int): The maximum allowed length
- `add_ellipsis` (bool): Whether to add '...' at the end. Defaults to True

**Returns:**
- str: The truncated string

**Usage Example:**
```python
>>> truncate_string("This is a long string", 10)
'This is...'
>>> truncate_string("Short", 10)
'Short'
```

**Cost:** O(n), where n is max_length

---

### substring

Extracts a substring from a string starting at a given position.

**Args:**
- `original_string` (str): The original string
- `start_position` (int): The starting position (1-indexed)
- `length` (int): The number of characters to extract

**Returns:**
- str: The extracted substring

**Usage Example:**
```python
>>> substring("hello world", 1, 5)
'hello'
>>> substring("Python", 3, 2)
'th'
```

**Cost:** O(length)

---

### left_substring

Returns the leftmost n characters of a string.

**Args:**
- `original_string` (str): The original string
- `num_chars` (int): The number of characters to return from the left

**Returns:**
- str: The leftmost num_chars characters

**Usage Example:**
```python
>>> left_substring("hello world", 5)
'hello'
```

**Cost:** O(num_chars)

---

### right_substring

Returns the rightmost n characters of a string.

**Args:**
- `original_string` (str): The original string
- `num_chars` (int): The number of characters to return from the right

**Returns:**
- str: The rightmost num_chars characters

**Usage Example:**
```python
>>> right_substring("hello world", 5)
'world'
```

**Cost:** O(num_chars)

---

### common_substring

Finds the longest common substring between two strings.

**Args:**
- `string1` (str): The first string
- `string2` (str): The second string
- `min_longest_substring` (int): The minimum length of the substring to find. Defaults to 4

**Returns:**
- str: The longest common substring, or empty string if none found

**Usage Example:**
```python
>>> common_substring("hello world", "world peace")
'world'
```

**Cost:** O(n * m), where n and m are the lengths of the two strings

---

### substring_on_left

Extracts the substring to the left of the first occurrence of a pattern.

**Args:**
- `text` (Optional[str]): The text to search
- `pattern` (str): The pattern to search for

**Returns:**
- Optional[str]: The substring before the pattern, or None if pattern not found

**Usage Example:**
```python
>>> substring_on_left("hello@world.com", "@")
'hello'
```

**Cost:** O(n), where n is the length of the text

---

### substring_on_right

Extracts the substring to the right of the first occurrence of a pattern.

**Args:**
- `text` (Optional[str]): The text to search
- `pattern` (str): The pattern to search for

**Returns:**
- Optional[str]: The substring after the pattern, or None if pattern not found

**Usage Example:**
```python
>>> substring_on_right("hello@world.com", "@")
'world.com'
```

**Cost:** O(n), where n is the length of the text

---

### substring_between_pattern

Extracts substring between two occurrences of the same pattern.

**Args:**
- `input_string` (str): The string to search
- `pattern` (str): The pattern to use as delimiter

**Returns:**
- str | None: The substring between two occurrences of the pattern

**Usage Example:**
```python
>>> substring_between_pattern("Name: John Doe: Age", ": ")
'John Doe'
```

**Cost:** O(n), where n is the length of the input string

---

### substring_from_delimiters

Extracts content from between specified delimiters.

**Args:**
- `input_string` (str): The string to search
- `left_delimiter` (str): The opening delimiter
- `right_delimiter` (str): The closing delimiter
- `include_delimiters` (bool): Whether to include delimiters in result. Defaults to False

**Returns:**
- str | None: The extracted content, or None if delimiters not found

**Usage Example:**
```python
>>> substring_from_delimiters("Hello (world)", "(", ")")
'world'
```

**Cost:** O(n), where n is the length of the input string

---

### extract_first_number

Extracts the first number (integer or float) from a string.

**Args:**
- `input_string` (str | None): The string to extract from

**Returns:**
- int | float | None: The first number found, or None if no number found

**Usage Example:**
```python
>>> extract_first_number("Price is 19.99 dollars")
19.99
>>> extract_first_number("Age: 25")
25
```

**Cost:** O(n), where n is the length of the input string

---

### extract_last_number

Extracts the last number (integer or float) from a string.

**Args:**
- `input_string` (str | None): The string to extract from

**Returns:**
- int | float | None: The last number found, or None if no number found

**Usage Example:**
```python
>>> extract_last_number("Prices: 10.50 and 25.75")
25.75
```

**Cost:** O(n), where n is the length of the input string

---

### extract_numbers

Extracts all numbers (integers and floats) from a string.

**Args:**
- `input_string` (str | None): The string to extract from

**Returns:**
- list[int | float]: A list of all numbers found in the string

**Usage Example:**
```python
>>> extract_numbers("Total: 100 items at 5.99 each")
[100, 5.99]
```

**Cost:** O(n), where n is the length of the input string

---

### join_to_string

Joins an iterable of strings into a single string with a separator.

**Args:**
- `iterable` (Iterable[str]): The iterable of strings to join
- `separator` (str): The separator to use between elements. Defaults to " "

**Returns:**
- str: The joined string

**Usage Example:**
```python
>>> join_to_string(["hello", "world"], " ")
'hello world'
>>> join_to_string(["a", "b", "c"], "-")
'a-b-c'
```

**Cost:** O(n), where n is the total length of all strings

---

### erase_specialchar

Removes special characters from a string, optionally allowing spaces and underscores.

**Args:**
- `text` (str): The text to process
- `allow_spaces` (bool): Whether to preserve spaces. Defaults to True
- `allow_underscores` (bool): Whether to preserve underscores. Defaults to False
- `additional_allowed_chars` (str): Additional characters to preserve. Defaults to ''

**Returns:**
- str: The text with special characters removed

**Usage Example:**
```python
>>> erase_specialchar("Hello@World!", allow_spaces=True)
'Hello World'
```

**Cost:** O(n), where n is the length of the text

---

### erase_digits

Removes all digits from a string.

**Args:**
- `text` (Optional[str]): The text to process

**Returns:**
- Optional[str]: The text with all digits removed, or None if input is None

**Usage Example:**
```python
>>> erase_digits("abc123def456")
'abcdef'
```

**Cost:** O(n), where n is the length of the text

---

### erase_lrspaces

Removes leading and trailing spaces from a string.

**Args:**
- `text` (Optional[str]): The text to process

**Returns:**
- Optional[str]: The text with leading and trailing spaces removed

**Usage Example:**
```python
>>> erase_lrspaces("  hello world  ")
'hello world'
```

**Cost:** O(n), where n is the length of the text

---

### erase_lspaces

Removes leading (left) whitespace from a string. Equivalent to VBA's LTrim function.

**Args:**
- `text` (Optional[str]): The text to process

**Returns:**
- Optional[str]: The text with leading spaces removed

**Usage Example:**
```python
>>> erase_lspaces("   hello   ")
'hello   '
```

**Cost:** O(n), where n is the length of the text

---

### erase_rspaces

Removes trailing (right) whitespace from a string. Equivalent to VBA's RTrim function.

**Args:**
- `text` (Optional[str]): The text to process

**Returns:**
- Optional[str]: The text with trailing spaces removed

**Usage Example:**
```python
>>> erase_rspaces("   hello   ")
'   hello'
```

**Cost:** O(n), where n is the length of the text

---

### erase_allspaces

Removes all spaces from a string.

**Args:**
- `text` (Optional[str]): The text to process

**Returns:**
- Optional[str]: The text with all spaces removed

**Usage Example:**
```python
>>> erase_allspaces("hello world from python")
'helloworldfrompython'
```

**Cost:** O(n), where n is the length of the text

---

### distinct_words

Returns a list of unique words from a string.

**Args:**
- `input_string` (str): The string to process
- `case_sensitive` (bool): Whether to distinguish between uppercase and lowercase. Defaults to False

**Returns:**
- list[str]: A list of unique words

**Usage Example:**
```python
>>> distinct_words("hello world hello python")
['hello', 'world', 'python']
```

**Cost:** O(n), where n is the length of the input string

---

### distinct_split

Splits a delimited string, removes duplicate tokens preserving first-occurrence order, and re-joins with the same separator. Useful for cleaning fields that accumulate repeated values after concatenation.

**Args:**
- `text` (str): The delimited string to process
- `separator` (str): Delimiter used to split and re-join tokens. Defaults to `";"`
- `strip_tokens` (bool): Strip whitespace from each token before comparison. Defaults to True
- `case_sensitive` (bool): Whether to distinguish between uppercase and lowercase tokens. Defaults to True

**Returns:**
- str: A string with unique tokens joined by the separator

**Raises:**
- TypeError: If `text` is not a string

**Usage Example:**
```python
>>> distinct_split("Office365;PowerBI;Office365;Visio;PowerBI")
'Office365;PowerBI;Visio'

>>> distinct_split("a ; b ; a ; c", separator=";")
'a;b;c'

>>> distinct_split("Alpha;alpha;ALPHA", case_sensitive=False)
'Alpha'

>>> distinct_split("x|y|x|z", separator="|")
'x|y|z'
```

**Cost:** O(n), where n is the length of the text

---

### move_word

Moves a word from one position to another in a string.

**Args:**
- `input_string` (str): The string containing words
- `from_index` (int): The index of the word to move (0-based)
- `to_index` (int): The target index for the word (0-based)

**Returns:**
- str: The string with the word moved

**Usage Example:**
```python
>>> move_word("first second third", 0, 2)
'second third first'
```

**Cost:** O(n), where n is the length of the input string

---

### concatenate_strings

Concatenates two strings.

**Args:**
- `string1` (str): The first string
- `string2` (str): The second string

**Returns:**
- str: The concatenated string

**Usage Example:**
```python
>>> concatenate_strings("hello", "world")
'helloworld'
```

**Cost:** O(n + m), where n and m are the lengths of the strings

---

### add_quotes

Adds quotes around a string.

**Args:**
- `text` (Optional[str]): The text to quote
- `quote_type` (str): The type of quote to use ("'" or '"'). Defaults to "'"

**Returns:**
- Optional[str]: The quoted string, or None if input is None

**Usage Example:**
```python
>>> add_quotes("hello world")
"'hello world'"
>>> add_quotes("test", '"')
'"test"'
```

**Cost:** O(1)

---

## String Format

Functions for formatting, normalizing, and standardizing strings.

### sql_quote

Escapes single quotes in a SQL string for safe database queries.

**Args:**
- `sql_string` (str): The SQL string to escape
- `db_type` (str): The database type (e.g., 'mysql', 'postgres')

**Returns:**
- str: The escaped SQL string

**Usage Example:**
```python
>>> sql_quote("O'Brien", "mysql")
"O''Brien"
```

**Cost:** O(n), where n is the length of sql_string

---

### format_date

Formats a date or datetime object into a specified string format.

**Args:**
- `date_input` (Union[str, datetime]): The date to format
- `output_format` (str): The desired output format. Defaults to None
- `input_format` (str): The input format if date_input is a string. Defaults to None

**Returns:**
- str: The formatted date string

**Usage Example:**
```python
>>> from datetime import datetime
>>> format_date(datetime(2023, 10, 26), "%Y-%m-%d")
'2023-10-26'
```

**Cost:** O(1)

---

### format_number

Formats a number with specified decimal places and thousand separators.

**Args:**
- `number_input` (Union[int, float, str]): The number to format
- `decimal_places` (int): Number of decimal places. Defaults to 2
- `use_separator` (bool): Whether to use thousand separators. Defaults to True
- `locale` (str): The locale to use for formatting. Defaults to 'en_US'

**Returns:**
- str: The formatted number string

**Usage Example:**
```python
>>> format_number(1234567.89, decimal_places=2)
'1,234,567.89'
```

**Cost:** O(log n), where n is the value of the number

---

### capitalize_string

Capitalizes a string according to specified mode.

**Args:**
- `input_string` (str): The string to capitalize
- `mode` (str): The capitalization mode ('all', 'first', 'each'). Defaults to 'all'

**Returns:**
- str: The capitalized string

**Usage Example:**
```python
>>> capitalize_string("hello world", mode='all')
'HELLO WORLD'
>>> capitalize_string("hello world", mode='each')
'Hello World'
>>> capitalize_string("hello world", mode='first')
'Hello world'
```

**Cost:** O(n), where n is the length of input_string

---

### pad_string

Pads a string to a specified length with a character.

**Args:**
- `text` (str): The text to pad
- `length` (int): The desired total length
- `char` (str): The character to use for padding. Defaults to ' '
- `direction` (str): The padding direction ('left', 'right', 'both'). Defaults to 'right'

**Returns:**
- str: The padded string

**Usage Example:**
```python
>>> pad_string("hello", 10, direction='right')
'hello     '
>>> pad_string("42", 5, '0', direction='left')
'00042'
```

**Cost:** O(n), where n is the desired length

---

### to_upper

Converts a string to uppercase.

**Args:**
- `text` (Optional[str]): The text to convert

**Returns:**
- Optional[str]: The uppercase string, or None if input is None

**Usage Example:**
```python
>>> to_upper("hello world")
'HELLO WORLD'
```

**Cost:** O(n), where n is the length of the text

---

### to_lower

Converts a string to lowercase.

**Args:**
- `text` (Optional[str]): The text to convert

**Returns:**
- Optional[str]: The lowercase string, or None if input is None

**Usage Example:**
```python
>>> to_lower("HELLO WORLD")
'hello world'
```

**Cost:** O(n), where n is the length of the text

---

### normalize_spaces

Normalizes whitespace in a string by replacing multiple spaces with single spaces and trimming.

**Args:**
- `text` (Optional[str]): The text to normalize

**Returns:**
- Optional[str]: The normalized string, or None if input is None

**Usage Example:**
```python
>>> normalize_spaces("  hello    world  ")
'hello world'
```

**Cost:** O(n), where n is the length of the text

---

### normalize_symbols

Normalizes symbol spacing in a string according to typographical rules.

**Args:**
- `text` (Optional[str]): The text to normalize

**Returns:**
- Optional[str]: The normalized string with proper symbol spacing

**Usage Example:**
```python
>>> normalize_symbols("hello , world !")
'hello, world!'
```

**Cost:** O(n), where n is the length of the text

---

### normalize_text

Normalizes text for spell checking by converting to lowercase and removing accents.

**Args:**
- `text` (str): The text to normalize

**Returns:**
- str: The normalized, lowercase ASCII string.

**Usage Example:**
```python
>>> normalize_text("Julián")
'julian'
```

**Cost:** O(n), where n is the length of the text

---

### flat_vowels

Removes diacritical marks (accents) from vowels in a string.

**Args:**
- `input_string` (str): The string to process

**Returns:**
- str: The string with accent marks removed from vowels

**Usage Example:**
```python
>>> flat_vowels("café")
'cafe'
>>> flat_vowels("niño")
'nino'
```

**Cost:** O(n), where n is the length of the input string

---

### ascii_string

Converts a string to ASCII, removing or replacing non-ASCII characters.

**Args:**
- `input_string` (str | None): The string to convert

**Returns:**
- str | None: The ASCII-compatible string, or None if input is None

**Usage Example:**
```python
>>> ascii_string("Héllo Wörld")
'Hello World'
```

**Cost:** O(n), where n is the length of the input string

---

### format_email_address

Formats and normalizes an email address.

**Args:**
- `email_string` (str): The email address to format

**Returns:**
- str: The formatted email address (lowercased, trimmed)

**Usage Example:**
```python
>>> format_email_address("  USER@EXAMPLE.COM  ")
'user@example.com'
```

**Cost:** O(n), where n is the length of the email string

---

### format_url

Formats and normalizes a URL.

**Args:**
- `url_string` (str): The URL to format

**Returns:**
- str: The formatted URL

**Usage Example:**
```python
>>> format_url("  HTTPS://EXAMPLE.COM/PATH  ")
'https://example.com/path'
```

**Cost:** O(n), where n is the length of the URL string

---

### format_name

Formats a person's name according to specified rules.

**Args:**
- `input_string` (str): The name to format
- `add_charset` (str): Additional allowed characters. Defaults to ""
- `name_type` (str): Type of name ('PERSONA' or 'EMPRESA'). Defaults to 'PERSONA'
- `shift` (bool): Whether to shift words. Defaults to False

**Returns:**
- str: The formatted name

**Usage Example:**
```python
>>> format_name("   john   doe  ")
'JOHN DOE'
```

**Cost:** O(n), where n is the length of the input string

---

### format_fullname

Formats a full name, removing titles and normalizing.

**Args:**
- `fullname` (str | None): The full name to format
- `uppercase` (bool): Whether to convert to uppercase. Defaults to True

**Returns:**
- str | None: The formatted full name, or None if input is None

**Usage Example:**
```python
>>> format_fullname("Dr. John Smith")
'JOHN SMITH'
```

**Cost:** O(n), where n is the length of the fullname

---

### format_company_name

Formats a company name, handling legal forms.

**Args:**
- `company_name` (str): The company name to format
- `remove_legal_form` (bool): Whether to remove legal forms. Defaults to False
- `legal_forms_set` (set): Set of legal forms to recognize. Defaults to None

**Returns:**
- str: The formatted company name

**Usage Example:**
```python
>>> format_company_name("Microsoft Corporation")
'MICROSOFT CORPORATION'
```

**Cost:** O(n * m), where n is the name length and m is the number of legal forms

---

## String Evaluations

Functions for evaluating, validating, and checking string properties.

### contains_digit

Checks if the given string contains at least one digit.

**Args:**
- `input_string` (str): The string to be checked for the presence of digits

**Returns:**
- bool: True if the string contains at least one digit, False otherwise

**Raises:**
- TypeError: If the input is not a string

**Usage Example:**
```python
>>> contains_digit("abc123def")
True
>>> contains_digit("no_digits_here")
False
```

**Cost:** O(n), where n is the length of the input string

---

### is_alphabetic

Checks if a string contains only alphabetic characters.

**Args:**
- `alpha_string`: The string to check

**Returns:**
- bool: True if the string contains only letters, False otherwise

**Usage Example:**
```python
>>> is_alphabetic("Hello")
True
>>> is_alphabetic("Hello123")
False
```

**Cost:** O(n), where n is the length of the string

---

### is_numeric

Checks if a string represents a valid number (integer or float).

**Args:**
- `input_string` (str): The string to check

**Returns:**
- bool: True if the string represents a valid number, False otherwise

**Usage Example:**
```python
>>> is_numeric("123")
True
>>> is_numeric("123.45")
True
>>> is_numeric("abc")
False
```

**Cost:** O(n), where n is the length of the input string

---

### is_internet_domain_format

Validates if a string matches the format of an internet domain.

**Args:**
- `domain_string` (str): The domain string to validate

**Returns:**
- bool: True if the string matches domain format, False otherwise

**Usage Example:**
```python
>>> is_internet_domain_format("example.com")
True
>>> is_internet_domain_format("sub.example.co.uk")
True
>>> is_internet_domain_format("invalid")
False
```

**Cost:** O(n), where n is the length of the domain string

---

### is_email_format

Validates if a string matches the format of an email address.

**Args:**
- `email_string` (str): The email string to validate

**Returns:**
- bool: True if the string matches email format, False otherwise

**Usage Example:**
```python
>>> is_email_format("user@example.com")
True
>>> is_email_format("invalid.email")
False
```

**Cost:** O(n), where n is the length of the email string

---

### is_url_format

Validates if a string matches the format of a URL.

**Args:**
- `url_string` (str): The URL string to validate

**Returns:**
- bool: True if the string matches URL format, False otherwise

**Usage Example:**
```python
>>> is_url_format("https://www.example.com")
True
>>> is_url_format("not a url")
False
```

**Cost:** O(n), where n is the length of the URL string

---

### has_date_format

Checks if a string can be interpreted as a date.

**Args:**
- `value` (str): The string to check

**Returns:**
- bool: True if the string represents a valid date format, False otherwise

**Usage Example:**
```python
>>> has_date_format("2023-10-26")
True
>>> has_date_format("not a date")
False
```

**Cost:** O(k * n), where k is the number of date formats and n is the string length

---

### has_numbers

Checks if a string contains any numeric digits.

**Args:**
- `input_string` (str): The string to check

**Returns:**
- bool: True if the string contains at least one digit, False otherwise

**Usage Example:**
```python
>>> has_numbers("Hello123")
True
>>> has_numbers("Hello")
False
```

**Cost:** O(n), where n is the length of the input string

---

### has_substring

Checks if a string contains a specific substring.

**Args:**
- `input_string` (str): The string to search in
- `char_to_find` (str): The substring to search for

**Returns:**
- bool: True if the substring is found, False otherwise

**Usage Example:**
```python
>>> has_substring("hello world", "world")
True
>>> has_substring("hello world", "python")
False
```

**Cost:** O(n * m), where n is the length of input_string and m is the length of char_to_find

---

### starts_with_substring

Checks if a string starts with a specific prefix.

**Args:**
- `input_string` (str): The string to check
- `prefix` (str): The prefix to look for
- `case_sensitive` (bool): Whether the comparison is case-sensitive. Defaults to True

**Returns:**
- bool: True if the string starts with the prefix, False otherwise

**Usage Example:**
```python
>>> starts_with_substring("hello world", "hello")
True
>>> starts_with_substring("Hello world", "hello", case_sensitive=False)
True
```

**Cost:** O(m), where m is the length of the prefix

---

### ends_with_substring

Checks if a string ends with a specific suffix.

**Args:**
- `input_string` (str): The string to check
- `suffix` (str): The suffix to look for
- `case_sensitive` (bool): Whether the comparison is case-sensitive. Defaults to True

**Returns:**
- bool: True if the string ends with the suffix, False otherwise

**Usage Example:**
```python
>>> ends_with_substring("hello world", "world")
True
>>> ends_with_substring("hello World", "world", case_sensitive=False)
True
```

**Cost:** O(m), where m is the length of the suffix

---

### parse_email

Parses an email address into its components.

**Args:**
- `email_address` (str): The email address to parse

**Returns:**
- dict | None: A dictionary with 'username' and 'domain' keys, or None if invalid

**Usage Example:**
```python
>>> parse_email("user@example.com")
{'username': 'user', 'domain': 'example.com'}
```

**Cost:** O(n), where n is the length of the email address

---

### username_from_email

Extracts the username portion from an email address.

**Args:**
- `email_address` (str): The email address

**Returns:**
- list[str] | None: The username part(s), or None if invalid

**Usage Example:**
```python
>>> username_from_email("john.doe@example.com")
['john', 'doe']
```

**Cost:** O(n), where n is the length of the email address

---

### domain_from_email

Extracts the domain portion from an email address.

**Args:**
- `email_address` (str): The email address

**Returns:**
- str | None: The domain part, or None if invalid

**Usage Example:**
```python
>>> domain_from_email("user@example.com")
'example.com'
```

**Cost:** O(n), where n is the length of the email address

---

## String Similarity

Functions for comparing strings and calculating similarity scores.

> Some algorithms (Metaphone, Levenshtein, Jaro-Winkler) require optional third-party libraries. If missing, the library logs an install instruction and returns ``None``. shortfx never installs packages automatically.

### calculate_similarity

Calculates similarity between two strings using specified algorithm.

**Args:**
- `string_one` (str): The first string to compare
- `string_two` (str): The second string to compare
- `algorithm` (str): The similarity algorithm to use
- `normalize` (bool): Whether to normalize the result. Defaults to True

**Returns:**
- Union[float, Dict[str, float]]: Similarity score or dictionary of scores

**Usage Example:**
```python
>>> calculate_similarity("hello", "hallo", algorithm="levenshtein")
0.8
```

**Cost:** Varies by algorithm, typically O(n * m) where n and m are string lengths

---

### has_same_words

Checks if two strings contain the same words (order-independent).

**Args:**
- `string_one` (str): The first string
- `string_two` (str): The second string

**Returns:**
- bool: True if both strings contain the same words, False otherwise

**Usage Example:**
```python
>>> has_same_words("hello world", "world hello")
True
>>> has_same_words("hello world", "hello python")
False
```

**Cost:** O(n + m), where n and m are the lengths of the strings

---

### find_common_words

Finds words that appear in both strings.

**Args:**
- `string_one` (str): The first string
- `string_two` (str): The second string

**Returns:**
- List[str]: A list of words common to both strings

**Usage Example:**
```python
>>> find_common_words("hello world", "world peace")
['world']
```

**Cost:** O(n + m), where n and m are the lengths of the strings

---

### has_same_characters

Checks if two strings contain the same characters (anagram check).

**Args:**
- `string_one` (str): The first string
- `string_two` (str): The second string

**Returns:**
- bool: True if both strings contain the same characters, False otherwise

**Usage Example:**
```python
>>> has_same_characters("listen", "silent")
True
>>> has_same_characters("hello", "world")
False
```

**Cost:** O(n log n), where n is the length of the longer string

---

### string_hamming_score

Calculates the Hamming distance between two strings.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- Dict[str, float]: Dictionary with 'distance' and 'similarity' scores

**Usage Example:**
```python
>>> string_hamming_score("karolin", "kathrin")
{'distance': 3, 'similarity': 0.571}
```

**Cost:** O(n), where n is the length of the strings

---

### string_levenshtein_score

Calculates the Levenshtein distance between two strings.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- Dict[str, float]: Dictionary with 'distance' and 'similarity' scores

**Usage Example:**
```python
>>> string_levenshtein_score("kitten", "sitting")
{'distance': 3, 'similarity': 0.571}
```

**Cost:** O(n * m), where n and m are the lengths of the strings

---

### string_jarowinkler_score

Calculates the Jaro-Winkler similarity between two strings.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- Dict[str, float]: Dictionary with similarity score

**Usage Example:**
```python
>>> string_jarowinkler_score("martha", "marhta")
{'similarity': 0.961}
```

**Cost:** O(n * m), where n and m are the lengths of the strings

---

### string_jaccard_score

Calculates the Jaccard similarity coefficient between two strings.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- Dict[str, float]: Dictionary with similarity score

**Usage Example:**
```python
>>> string_jaccard_score("hello", "hallo")
{'similarity': 0.6}
```

**Cost:** O(n + m), where n and m are the lengths of the strings

---

### string_similarity_score

Calculates multiple similarity scores between two strings using all available algorithms.

**Args:**
- `a` (str): The first string
- `b` (str): The second string

**Returns:**
- List[Tuple[str, Union[Dict[str, float], float]]]: List of tuples with algorithm name and scores

**Usage Example:**
```python
>>> scores = string_similarity_score("hello", "hallo")
>>> # Returns scores from all algorithms
```

**Cost:** O(n * m) for most algorithms, combined

---

### Guía de Umbrales de Similitud

Los algoritmos de similitud retornan valores entre 0.0 (completamente diferentes) y 1.0 (idénticos). La elección del umbral correcto depende del caso de uso:

#### Umbrales Recomendados por Caso de Uso

**Validación Estricta (0.90 - 1.00)**
- Detección de duplicados exactos
- Verificación de identidad
- Control de calidad de datos críticos
- Ejemplo: Verificar si dos DNI son el mismo
```python
# Umbral: 0.95
if calculate_similarity(dni1, dni2, 'levenshtein') >= 0.95:
    print("Posible duplicado - revisión manual requerida")
```

**Nombres Propios (0.85 - 0.90)**
- Comparación de nombres de personas
- Búsqueda de clientes
- Matching de registros
- Ejemplo: Encontrar un cliente por nombre
```python
# Umbral: 0.85 con jaro_winkler (favorece coincidencias al inicio)
similarity = calculate_similarity(busqueda, nombre_cliente, 'jaro_winkler')
if similarity['score'] >= 0.85:
    resultados.append(nombre_cliente)
```

**Búsqueda Tolerante (0.70 - 0.80)**
- Autocompletado
- Sugerencias de búsqueda
- Corrección ortográfica
- Búsqueda en catálogos
- Ejemplo: Sistema de autocompletado
```python
# Umbral: 0.70
sugerencias = [
    item for item in catalogo
    if calculate_similarity(query, item, 'levenshtein') >= 0.70
]
```

**Similitud Semántica (0.50 - 0.70)**
- Comparación de textos
- Detección de contenido similar
- Agrupación de documentos
- Ejemplo: Detectar artículos similares
```python
# Umbral: 0.60 con sorensen_dice (bueno para textos)
if calculate_similarity(texto1, texto2, 'sorensen_dice')['score'] >= 0.60:
    print("Contenido similar detectado")
```

**Filtrado Inicial (0.40 - 0.50)**
- Pre-filtrado en datasets grandes
- Primera pasada en búsquedas complejas
- Ejemplo: Filtro rápido antes de análisis detallado
```python
# Umbral: 0.45 con metaphone (rápido, fonético)
candidatos = [
    item for item in dataset_grande
    if calculate_similarity(query, item, 'metaphone')  # True/False
]
# Luego aplicar algoritmo más preciso a candidatos
```

#### Umbrales por Algoritmo

**Levenshtein (Distancia de Edición)**
- Estricto: ≥ 0.90
- Moderado: ≥ 0.75
- Tolerante: ≥ 0.60
- Mejor para: Errores tipográficos, texto general

**Jaro-Winkler (Favorece Prefijos)**
- Estricto: ≥ 0.92
- Moderado: ≥ 0.85
- Tolerante: ≥ 0.75
- Mejor para: Nombres propios, palabras cortas

**Metaphone (Fonético)**
- Solo retorna True/False
- Mejor para: Filtrado rápido, palabras que suenan igual

**Sorensen-Dice / Jaccard (Tokens)**
- Estricto: ≥ 0.80
- Moderado: ≥ 0.60
- Tolerante: ≥ 0.40
- Mejor para: Frases, documentos, textos largos

#### Estrategia Multi-Umbral

Para casos críticos, combina múltiples algoritmos con diferentes umbrales:

```python
def validacion_robusta(palabra1, palabra2):
    """Validación usando múltiples algoritmos con umbrales específicos."""
    
    # Levenshtein: errores tipográficos (umbral: 0.85)
    lev_score = calculate_similarity(palabra1, palabra2, 'levenshtein')
    
    # Jaro-Winkler: similitud de nombres (umbral: 0.90)
    jw_result = calculate_similarity(palabra1, palabra2, 'jaro_winkler')
    
    # Metaphone: similitud fonética (True/False)
    metaphone_match = calculate_similarity(palabra1, palabra2, 'metaphone')
    
    # Decisión combinada
    es_similar = (
        lev_score >= 0.85 and
        jw_result['score'] >= 0.90 and
        metaphone_match
    )
    
    return es_similar
```

#### Ajuste de Umbrales

Factores a considerar al ajustar umbrales:

1. **Longitud de cadenas**: Cadenas más largas toleran umbrales más bajos
2. **Criticidad del dato**: Datos críticos requieren umbrales más altos
3. **Volumen de datos**: Datasets grandes pueden necesitar umbrales más altos para reducir falsos positivos
4. **Tipo de errores esperados**: Errores tipográficos vs. variaciones fonéticas
5. **Consecuencias de errores**: Balance entre falsos positivos y falsos negativos

**Ejemplo de ajuste dinámico:**
```python
def calcular_umbral_dinamico(longitud_texto):
    """Ajusta el umbral según la longitud del texto."""
    if longitud_texto < 5:
        return 0.90  # Palabras cortas: muy estricto
    elif longitud_texto < 15:
        return 0.85  # Palabras medias: estricto
    elif longitud_texto < 50:
        return 0.75  # Frases cortas: moderado
    else:
        return 0.65  # Textos largos: tolerante
```

---

## String Spanish

Functions specific to Spanish language processing and validation.

### remove_spanish_stop_words

Removes common Spanish stop words from a string.

**Args:**
- `input_string` (str): The string to process

**Returns:**
- str | None: The string with stop words removed, or None if input is None

**Usage Example:**
```python
>>> remove_spanish_stop_words("el gato en la casa")
'gato casa'
```

**Cost:** O(n), where n is the length of the input string

---

### reduce_spanish_letters

Reduces Spanish text to a phonetic representation.

**Args:**
- `input_string` (str): The string to reduce
- `strength` (int): The strength of reduction (1-3)

**Returns:**
- str | None: The phonetically reduced string, or None if input is None

**Usage Example:**
```python
>>> reduce_spanish_letters("llamar", 2)
'yamar'
```

**Cost:** O(n), where n is the length of the input string

---

### nif_padding

Pads a Spanish NIF/CIF to standard format.

**Args:**
- `p_nif` (Optional[str]): The NIF to pad

**Returns:**
- Optional[str]: The padded NIF, or None if input is None

**Usage Example:**
```python
>>> nif_padding("12345678")
'00012345678'
```

**Cost:** O(1)

---

### nif_parse

Parses and normalizes a Spanish NIF/NIE/CIF.

**Args:**
- `nif` (Optional[str]): The NIF to parse

**Returns:**
- Optional[str]: The normalized NIF, or None if invalid

**Usage Example:**
```python
>>> nif_parse("12345678-Z")
'12345678Z'
```

**Cost:** O(n), where n is the length of the NIF

---

### nif_letter

Calculates the control letter for a Spanish DNI.

**Args:**
- `p_dni` (str): The DNI number (8 digits)

**Returns:**
- str: The control letter

**Usage Example:**
```python
>>> nif_letter("12345678")
'Z'
```

**Cost:** O(1)

---

### is_valid_dni

Validates a Spanish DNI (Documento Nacional de Identidad).

**Args:**
- `dni_value` (str): The DNI to validate

**Returns:**
- bool: True if the DNI is valid, False otherwise

**Usage Example:**
```python
>>> is_valid_dni("12345678Z")
True
>>> is_valid_dni("12345678X")
False
```

**Cost:** O(1)

---

### is_valid_nie

Validates a Spanish NIE (Número de Identidad de Extranjero).

**Args:**
- `nie_value` (str): The NIE to validate

**Returns:**
- bool: True if the NIE is valid, False otherwise

**Usage Example:**
```python
>>> is_valid_nie("X1234567L")
True
>>> is_valid_nie("X1234567M")
False
```

**Cost:** O(1)

---

### is_valid_cif

Validates a Spanish CIF (Certificado de Identificación Fiscal).

**Args:**
- `cif_value` (str): The CIF to validate

**Returns:**
- bool: True if the CIF is valid, False otherwise

**Usage Example:**
```python
>>> is_valid_cif("A12345674")
True
>>> is_valid_cif("A12345675")
False
```

**Cost:** O(1)

---

### validate_spanish_nif

Validates a Spanish NIF (DNI, NIE, or CIF).

**Args:**
- `nif_type` (str): The type of NIF ('DNI', 'NIE', or 'CIF')
- `nif_value` (str): The NIF value to validate

**Returns:**
- bool: True if the NIF is valid for the specified type, False otherwise

**Usage Example:**
```python
>>> validate_spanish_nif("DNI", "12345678Z")
True
>>> validate_spanish_nif("NIE", "X1234567L")
True
```

**Cost:** O(1)

---

### fix_spanish

Fixes common Spanish character encoding issues.

**Args:**
- `input_string` (str | None): The string to fix
- `additional_allowed_chars` (str): Additional allowed characters. Defaults to ''

**Returns:**
- str | None: The fixed string, or None if input is None

**Usage Example:**
```python
>>> fix_spanish("cafÃ©")
'café'
```

**Cost:** O(n), where n is the length of the input string

---

## String Validations

Functions for validating string properties and content.

### contains_digit

Checks if the given string contains at least one digit.

**Args:**
- `input_string` (str): The string to be checked for the presence of digits

**Returns:**
- bool: True if the string contains at least one digit, False otherwise

**Raises:**
- TypeError: If the input is not a string

**Usage Example:**
```python
>>> contains_digit("abc123def")
True
>>> contains_digit("no_digits_here")
False
```

**Cost:** O(n), where n is the length of the input string

---

### same_letters

Checks if two strings contain the exact same characters, irrespective of their order (anagram check).

**Args:**
- `string_a` (str): The first string for comparison
- `string_b` (str): The second string for comparison

**Returns:**
- bool: True if both strings contain the same characters (same count, same case), False otherwise

**Raises:**
- TypeError: If 'string_a' or 'string_b' are not strings

**Usage Example:**
```python
>>> same_letters("listen", "silent")
True
>>> same_letters("hello", "holle")
True
>>> same_letters("abc", "ab")
False
```

**Cost:** O(n log n), where n is the maximum length of the two input strings (due to sorting)

---

## String Spellcheck

Functions for spell checking and text normalization.

### UniversalSpellChecker

Class for multi-algorithm spell checking.

---

## String Encoding

Functions for encoding and decoding text in various formats.

### encode_html_entities

Encodes HTML special characters (`<`, `>`, `&`, `"`, `'`) as HTML entities.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: HTML-escaped string.

**Example:**
```python
>>> encode_html_entities('<b>"Hello"</b>')
'&lt;b&gt;&quot;Hello&quot;&lt;/b&gt;'
```

**Cost:** O(n)

---

### decode_html_entities

Decodes HTML entities back to their original characters.

**Parameters:**
- `text` (str): HTML-encoded string.

**Returns:**
- `str`: Decoded text.

**Example:**
```python
>>> decode_html_entities('&lt;b&gt;Hi&lt;/b&gt;')
'<b>Hi</b>'
```

**Cost:** O(n)

---

## String Case Conversion

Functions for converting between naming conventions.

### to_camel_case

Converts text to camelCase.

**Parameters:**
- `text` (str): Input text in any convention.

**Returns:**
- `str`: camelCase string.

**Example:**
```python
>>> to_camel_case("hello_world")
'helloWorld'
```

**Cost:** O(n)

---

### to_pascal_case

Converts text to PascalCase.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: PascalCase string.

**Example:**
```python
>>> to_pascal_case("hello_world")
'HelloWorld'
```

**Cost:** O(n)

---

### to_snake_case

Converts text to snake_case.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: snake_case string.

**Example:**
```python
>>> to_snake_case("helloWorld")
'hello_world'
```

**Cost:** O(n)

---

### to_kebab_case

Converts text to kebab-case.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: kebab-case string.

**Example:**
```python
>>> to_kebab_case("helloWorld")
'hello-world'
```

**Cost:** O(n)

---

### to_constant_case

Converts text to CONSTANT_CASE.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: CONSTANT_CASE string.

**Example:**
```python
>>> to_constant_case("maxRetries")
'MAX_RETRIES'
```

**Cost:** O(n)

---

### to_slug

Converts text to URL-safe slug (ASCII, lowered, hyphenated).

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: Slug string.

**Example:**
```python
>>> to_slug("Café Résumé")
'cafe-resume'
```

**Cost:** O(n)

---

### to_title_case

Smart Title Case that respects articles and prepositions (en/es).

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: Title-cased string.

**Example:**
```python
>>> to_title_case("the lord of the rings")
'The Lord of the Rings'
```

**Cost:** O(n)

---

## String Regex

High-level regex wrappers.

### regex_match

Tests if a pattern matches anywhere in text.

**Parameters:**
- `text` (str): Input string.
- `pattern` (str): Regex pattern.
- `case_sensitive` (bool): Case sensitivity. Defaults to True.

**Returns:**
- `bool`: True if pattern matches.

**Example:**
```python
>>> regex_match("Hello World", r"\d+")
False
>>> regex_match("abc123", r"\d+")
True
```

**Cost:** O(n*m)

---

### regex_extract

Extracts first regex match.

**Parameters:**
- `text` (str): Input string.
- `pattern` (str): Regex pattern.
- `group` (int): Capture group. Defaults to 0.
- `case_sensitive` (bool): Case sensitivity. Defaults to True.

**Returns:**
- `Optional[str]`: First match or None.

**Example:**
```python
>>> regex_extract("ID: 12345", r"\d+")
'12345'
```

**Cost:** O(n*m)

---

### regex_extract_all

Extracts all regex matches.

**Parameters:**
- `text` (str): Input string.
- `pattern` (str): Regex pattern.
- `case_sensitive` (bool): Case sensitivity. Defaults to True.

**Returns:**
- `list[str]`: All matches.

**Example:**
```python
>>> regex_extract_all("a1 b2 c3", r"[a-z]\d")
['a1', 'b2', 'c3']
```

**Cost:** O(n*m)

---

### regex_split

Splits a string by regex pattern.

**Parameters:**
- `text` (str): Input string.
- `pattern` (str): Regex delimiter.
- `max_split` (int): Max splits (0 = unlimited). Defaults to 0.
- `case_sensitive` (bool): Case sensitivity. Defaults to True.

**Returns:**
- `list[str]`: Split substrings.

**Example:**
```python
>>> regex_split("one, two; three", r"[,;]\s*")
['one', 'two', 'three']
```

**Cost:** O(n*m)

---

### regex_count

Counts non-overlapping matches of a regex pattern.

**Parameters:**
- `text` (str): Input string.
- `pattern` (str): Regex pattern.
- `case_sensitive` (bool): Case sensitivity. Defaults to True.

**Returns:**
- `int`: Number of matches.

**Example:**
```python
>>> regex_count("one 1 two 2 three 3", r"\d+")
3
```

**Cost:** O(n*m)

---

## String Hashing

Cryptographic hashing and deduplication fingerprinting.

### hash_string

Generates a hex hash digest of a string.

**Parameters:**
- `text` (str): Input string.
- `algorithm` (str): Hash algorithm (`"md5"`, `"sha256"`, `"sha512"`). Defaults to `"sha256"`.

**Returns:**
- `str`: Hex digest.

**Example:**
```python
>>> hash_string("hello", "md5")
'5d41402abc4b2a76b9719d911017c592'
```

**Cost:** O(n)

---

### fingerprint

Creates a normalized fingerprint for deduplication (lowered, sorted unique words).

**Parameters:**
- `text` (str): Input string.

**Returns:**
- `str`: Fingerprint string.

**Example:**
```python
>>> fingerprint("The Quick Brown Fox")
'brown fox quick the'
```

**Cost:** O(n log n)

---

## String Compression

Text compression using zlib with Base64 transport.

### compress_string

Compresses a text string via zlib and encodes as URL-safe Base64.

**Parameters:**
- `text` (str): Input string.
- `level` (int): Compression level 1-9. Defaults to 9.

**Returns:**
- `str`: Compressed Base64 string.

**Example:**
```python
>>> compressed = compress_string("hello " * 100)
>>> len(compressed) < 600
True
```

**Cost:** O(n)

---

### decompress_string

Decompresses a Base64/zlib compressed string.

**Parameters:**
- `compressed` (str): Base64-encoded compressed string.

**Returns:**
- `str`: Original text.

**Example:**
```python
>>> decompress_string(compress_string("hello"))
'hello'
```

**Cost:** O(n)

---

## Additional String Operations (recent)

### repeat_string

Repeats a string n times.

**Parameters:**
- `text` (str): Input string.
- `n` (int): Number of repetitions.

**Returns:**
- `str`: Repeated string.

**Example:**
```python
>>> repeat_string("ab", 3)
'ababab'
```

**Cost:** O(n)

---

### center_string

Centers a string within a given width.

**Parameters:**
- `text` (str): Input string.
- `width` (int): Total width.
- `fill_char` (str): Padding character. Defaults to ' '.

**Returns:**
- `str`: Centered string.

**Example:**
```python
>>> center_string("hi", 8, '-')
'---hi---'
```

**Cost:** O(1)

---

### strip_html_tags

Removes all HTML tags from text, keeping only content.

**Parameters:**
- `text` (str): HTML text.

**Returns:**
- `str`: Plain text.

**Example:**
```python
>>> strip_html_tags("<p>Hello <b>World</b></p>")
'Hello World'
```

**Cost:** O(n)

---

### clean_non_printable

Removes non-printable control characters from text.

**Parameters:**
- `text` (str): Input string.

**Returns:**
- `str`: Cleaned string.

**Example:**
```python
>>> clean_non_printable("ABC\x00\x01\x02")
'ABC'
```

**Cost:** O(n)

---

### abbreviate

Truncates text at word boundary with ellipsis.

**Parameters:**
- `text` (str): Input string.
- `max_length` (int): Maximum length including ellipsis.

**Returns:**
- `str`: Abbreviated text.

**Example:**
```python
>>> abbreviate("Hello World Example", 12)
'Hello...'
```

**Cost:** O(n)

---

### generate_initials

Generates initials from a name.

**Parameters:**
- `name` (str): Full name.
- `separator` (str): Separator between initials. Defaults to '.'.

**Returns:**
- `str`: Initials string.

**Example:**
```python
>>> generate_initials("John Ronald Tolkien")
'J.R.T.'
```

**Cost:** O(n)

---

### count_lines

Counts lines in multiline text.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `int`: Number of lines.

**Example:**
```python
>>> count_lines("a\nb\nc")
3
```

**Cost:** O(n)

---

### get_line

Gets a specific line from text (1-indexed).

**Parameters:**
- `text` (str): Input text.
- `line_number` (int): Line number (1-based).

**Returns:**
- `Optional[str]`: The line, or None if out of range.

**Example:**
```python
>>> get_line("a\nb\nc", 2)
'b'
```

**Cost:** O(n)

---

### remove_blank_lines

Removes blank or whitespace-only lines.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: Text without blank lines.

**Example:**
```python
>>> remove_blank_lines("a\n\n  \nb")
'a\nb'
```

**Cost:** O(n)

---

### sort_lines

Sorts lines alphabetically.

**Parameters:**
- `text` (str): Input text.
- `reverse` (bool): Descending order. Defaults to False.

**Returns:**
- `str`: Sorted text.

**Example:**
```python
>>> sort_lines("c\na\nb")
'a\nb\nc'
```

**Cost:** O(n log n)

---

### deduplicate_words

Removes duplicate words, preserving first occurrence order.

**Parameters:**
- `text` (str): Input string.

**Returns:**
- `str`: Text with duplicate words removed.

**Example:**
```python
>>> deduplicate_words("the cat and the dog and the bird")
'the cat and dog bird'
```

**Cost:** O(n)

---

### surround

Wraps text with a given string on both sides.

**Parameters:**
- `text` (str): Input string.
- `wrapper` (str): String to prepend and append.

**Returns:**
- `str`: Surrounded text.

**Example:**
```python
>>> surround("hello", "**")
'**hello**'
```

**Cost:** O(1)

---

### extract_emails

Extracts all email addresses from a text.

**Parameters:**
- `text` (str): Input string.

**Returns:**
- `list[str]`: List of email addresses.

**Example:**
```python
>>> extract_emails("Contact info@test.com or admin@site.org")
['info@test.com', 'admin@site.org']
```

**Cost:** O(n)

---

## Additional String Format (recent)

### swap_case

Inverts case of every character.

**Parameters:**
- `text` (str): Input string.

**Returns:**
- `str`: Case-swapped string.

**Example:**
```python
>>> swap_case("Hello World")
'hELLO wORLD'
```

**Cost:** O(n)

---

### indent_text

Adds a prefix to every line.

**Parameters:**
- `text` (str): Input text.
- `prefix` (str): Line prefix. Defaults to `'    '`.

**Returns:**
- `str`: Indented text.

**Example:**
```python
>>> indent_text("a\nb", prefix=">> ")
'>> a\n>> b'
```

**Cost:** O(n)

---

### dedent_text

Removes common leading whitespace from all lines.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: Dedented text.

**Example:**
```python
>>> dedent_text("    a\n    b")
'a\nb'
```

**Cost:** O(n)

---

### zfill

Pads a string with leading zeros.

**Parameters:**
- `text` (str): Input string.
- `width` (int): Target total width.

**Returns:**
- `str`: Zero-padded string.

**Example:**
```python
>>> zfill("42", 5)
'00042'
```

**Cost:** O(1)

---

### rot13

Applies ROT13 letter substitution cipher.

**Parameters:**
- `text` (str): Input string.

**Returns:**
- `str`: ROT13-encoded string.

**Example:**
```python
>>> rot13("Hello")
'Uryyb'
```

**Cost:** O(n)

---

### format_list_as_sentence

Formats a list as a human-readable sentence.

**Parameters:**
- `items` (list[str]): List of items.
- `conjunction` (str): Conjunction before last item. Defaults to `"and"`.
- `separator` (str): Item separator. Defaults to `", "`.

**Returns:**
- `str`: Formatted sentence.

**Example:**
```python
>>> format_list_as_sentence(["a", "b", "c"])
'a, b and c'
```

**Cost:** O(n)

---

### pluralize_count

Returns count with noun in singular or plural form.

**Parameters:**
- `count` (int): Quantity.
- `singular` (str): Singular noun.
- `plural` (Optional[str]): Plural noun. Defaults to singular + "s".

**Returns:**
- `str`: Formatted string.

**Example:**
```python
>>> pluralize_count(1, "item")
'1 item'
>>> pluralize_count(5, "item")
'5 items'
```

**Cost:** O(1)

---

## Additional String Evaluations (recent)

### word_frequency

Returns frequency of each word as a dictionary.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `dict[str, int]`: Word → count mapping.

**Example:**
```python
>>> word_frequency("the cat and the dog")
{'the': 2, 'cat': 1, 'and': 1, 'dog': 1}
```

**Cost:** O(n)

---

### char_frequency

Returns frequency of each character as a dictionary.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `dict[str, int]`: Character → count mapping.

**Example:**
```python
>>> char_frequency("aabbc")
{'a': 2, 'b': 2, 'c': 1}
```

**Cost:** O(n)

---

### sentence_count

Counts sentences by terminal punctuation (`.`, `!`, `?`).

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `int`: Number of sentences.

**Example:**
```python
>>> sentence_count("Hello! How are you? Fine.")
3
```

**Cost:** O(n)

---

### reading_time

Estimates reading time in minutes.

**Parameters:**
- `text` (str): Input text.
- `words_per_minute` (int): Reading speed. Defaults to 200.

**Returns:**
- `float`: Minutes.

**Example:**
```python
>>> reading_time("word " * 400)
2.0
```

**Cost:** O(n)

---

### is_palindrome

Checks if text is a palindrome (ignoring case, spaces, punctuation).

**Parameters:**
- `text` (str): Input string.

**Returns:**
- `bool`: True if palindrome.

**Example:**
```python
>>> is_palindrome("A man a plan a canal Panama")
True
```

**Cost:** O(n)

---

### is_anagram

Checks if two strings are anagrams (same letters, ignoring case/spaces).

**Parameters:**
- `a` (str): First string.
- `b` (str): Second string.

**Returns:**
- `bool`: True if anagrams.

**Example:**
```python
>>> is_anagram("listen", "silent")
True
```

**Cost:** O(n log n)

---

### is_pangram

Checks if text contains every letter of the given alphabet.

**Parameters:**
- `text` (str): Input string.
- `alphabet` (str): Required letters. Defaults to `"abcdefghijklmnopqrstuvwxyz"`.

**Returns:**
- `bool`: True if pangram.

**Example:**
```python
>>> is_pangram("The quick brown fox jumps over the lazy dog")
True
```

**Cost:** O(n + a)

---

## Additional String Similarity (recent)

### string_cosine_score

Cosine similarity between two strings based on character frequency vectors.

**Parameters:**
- `a` (str): First string.
- `b` (str): Second string.

**Returns:**
- `dict`: `{'similarity': float, 'score': float}`.

**Example:**
```python
>>> string_cosine_score("hello world", "hello earth")
{'similarity': 0.5, 'score': 50.0}
```

**Cost:** O(n)

---

### generate_ngrams

Generates character n-grams from text.

**Parameters:**
- `text` (str): Input string.
- `n` (int): N-gram size. Defaults to 2.

**Returns:**
- `list[str]`: List of n-grams.

**Example:**
```python
>>> generate_ngrams("hello", 2)
['he', 'el', 'll', 'lo']
```

**Cost:** O(n)

---

### find_closest_match

Finds best match from a candidate list.

**Parameters:**
- `text` (str): Query string.
- `candidates` (list[str]): List of candidate strings.
- `algorithm` (str): Similarity algorithm. Defaults to `"levenshtein"`.

**Returns:**
- `tuple[str, float]`: Best match and score.

**Example:**
```python
>>> find_closest_match("cart", ["cat", "car", "card"])
('cat', 75.0)
```

**Cost:** O(n*m*k)

---

### rank_by_similarity

Ranks candidates by similarity score (descending).

**Parameters:**
- `text` (str): Query string.
- `candidates` (list[str]): Candidate strings.
- `algorithm` (str): Similarity algorithm. Defaults to `"levenshtein"`.

**Returns:**
- `list[tuple[str, float]]`: Sorted (candidate, score) pairs.

**Example:**
```python
>>> rank_by_similarity("cart", ["cat", "car", "card"])
[('cat', 75.0), ('car', 75.0), ('card', 75.0)]
```

**Cost:** O(n*m*k)

---

## Additional String Conversions (recent)

### string_to_boolean

Converts truthy/falsy strings to boolean.

**Parameters:**
- `text` (str): Input string (e.g. "yes", "true", "1", "no", "false", "0").

**Returns:**
- `bool`: Boolean value.

**Example:**
```python
>>> string_to_boolean("yes")
True
>>> string_to_boolean("no")
False
```

**Cost:** O(1)

---

### boolean_to_string

Converts boolean to "true" / "false" string.

**Parameters:**
- `value` (bool): Boolean value.

**Returns:**
- `str`: "true" or "false".

**Example:**
```python
>>> boolean_to_string(True)
'true'
```

**Cost:** O(1)

---

### string_to_list

Splits a string into a list by delimiter with optional stripping.

**Parameters:**
- `text` (str): Input string.
- `delimiter` (str): Separator. Defaults to `","`.
- `strip` (bool): Strip whitespace. Defaults to True.

**Returns:**
- `list[str]`: Split items.

**Example:**
```python
>>> string_to_list("a, b, c")
['a', 'b', 'c']
```

**Cost:** O(n)

---

### integer_to_roman

Converts an integer (1–3999) to Roman numeral string.

**Parameters:**
- `number` (int): Input integer.

**Returns:**
- `str`: Roman numeral.

**Example:**
```python
>>> integer_to_roman(2024)
'MMXXIV'
```

**Cost:** O(1)

---

### roman_to_integer

Converts a Roman numeral string to integer.

**Parameters:**
- `roman` (str): Roman numeral string.

**Returns:**
- `int`: Integer value.

**Example:**
```python
>>> roman_to_integer("MMXXIV")
2024
```

**Cost:** O(n)

---

### text_to_binary

Converts text to binary representation.

**Parameters:**
- `text` (str): Input text.
- `separator` (str): Between bytes. Defaults to `" "`.

**Returns:**
- `str`: Binary string.

**Example:**
```python
>>> text_to_binary("AB")
'01000001 01000010'
```

**Cost:** O(n)

---

### binary_to_text

Converts binary string back to text.

**Parameters:**
- `binary_str` (str): Binary string.
- `separator` (str): Byte separator. Defaults to `" "`.

**Returns:**
- `str`: Decoded text.

**Example:**
```python
>>> binary_to_text("01000001 01000010")
'AB'
```

**Cost:** O(n)

---

### text_to_morse

Encodes text to Morse code.

**Parameters:**
- `text` (str): Input text.

**Returns:**
- `str`: Morse code.

**Example:**
```python
>>> text_to_morse("SOS")
'... --- ...'
```

**Cost:** O(n)

---

### morse_to_text

Decodes Morse code back to text.

**Parameters:**
- `morse` (str): Morse code string.

**Returns:**
- `str`: Decoded text.

**Example:**
```python
>>> morse_to_text("... --- ...")
'SOS'
```

**Cost:** O(n)

---

### `camel_to_snake()`

Converts a camelCase or PascalCase string to snake_case.

**Parameters:**
- text: The camelCase or PascalCase string.

**Returns:**
- The snake_case equivalent.

**Ejemplo:**
```python
from shortfx.fxString.string_format import camel_to_snake

result = camel_to_snake(...)
```

---

### `char_from_code()`

Returns the Unicode character for a given code point.

**Parameters:**
- code_point: A valid Unicode code point (1 to 1114111).

**Returns:**
- The single Unicode character.

**Raises:**
- TypeError: If input is not an integer.
- ValueError: If code point is out of valid Unicode range.

**Ejemplo:**
```python
from shortfx.fxString.string_convertions import char_from_code

result = char_from_code(...)
```

---

### `code_from_char()`

Returns the Unicode code point of the first character of a string.

**Parameters:**
- character: A non-empty string (first character is used).

**Returns:**
- The Unicode code point as an integer.

**Raises:**
- TypeError: If input is not a string.
- ValueError: If the string is empty.

**Ejemplo:**
```python
from shortfx.fxString.string_convertions import code_from_char

result = code_from_char(...)
```

---

### `count_sentences()`

Count the number of sentences in a text.

**Parameters:**
- text: Input text.

**Returns:**
- Number of sentences.

**Ejemplo:**
```python
from shortfx.fxString.string_evaluations import count_sentences

result = count_sentences(...)
```

---

### `decode_base64()`

Decodes a Base64-encoded string back to plain text.

**Parameters:**
- encoded_text: The Base64-encoded string.
- encoding: Character encoding to use after Base64 decoding.

**Returns:**
- The decoded plain text string.

**Raises:**
- TypeError: If encoded_text is not a string.
- ValueError: If the input is not valid Base64.

**Ejemplo:**
```python
from shortfx.fxString.string_encoding import decode_base64

result = decode_base64(...)
```

---

### `decode_url()`

Decodes a URL percent-encoded string back to plain text.

**Parameters:**
- encoded_text: The percent-encoded string.

**Returns:**
- The decoded plain text string.

**Raises:**
- TypeError: If encoded_text is not a string.

**Ejemplo:**
```python
from shortfx.fxString.string_encoding import decode_url

result = decode_url(...)
```

---

### `dollar()`

Format number as currency text with dollar sign.

**Parameters:**
- number: Numeric value to format.
- decimals: Decimal places (default 2).

**Returns:**
- str: Dollar-formatted text.

**Raises:**
- TypeError: If number is not numeric or decimals not int.

**Ejemplo:**
```python
from shortfx.fxString.string_format import dollar

result = dollar(...)
```

---

### `encode_base64()`

Encodes a string to Base64 representation.

**Parameters:**
- text: The input string to encode.
- encoding: Character encoding to use before Base64 conversion.

**Returns:**
- The Base64-encoded string.

**Raises:**
- TypeError: If text is not a string.

**Ejemplo:**
```python
from shortfx.fxString.string_encoding import encode_base64

result = encode_base64(...)
```

---

### `encode_url()`

Encodes a string using URL percent-encoding (RFC 3986).

**Parameters:**
- text: The input string to encode.
- safe: Characters that should not be encoded.

**Returns:**
- The percent-encoded string.

**Raises:**
- TypeError: If text is not a string.

**Ejemplo:**
```python
from shortfx.fxString.string_encoding import encode_url

result = encode_url(...)
```

---

### `extract_urls()`

Extracts all URLs from a text string.

**Parameters:**
- text: The input string to scan.

**Returns:**
- A list of extracted URL strings.

**Ejemplo:**
```python
from shortfx.fxString.string_operations import extract_urls

result = extract_urls(...)
```

---

### `fixed()`

Format number with a fixed number of decimal places.

**Parameters:**
- number: Numeric value to format.
- decimals: Decimal places (default 2).
- no_commas: If True, suppress thousands separators.

**Returns:**
- str: Formatted text representation.

**Raises:**
- TypeError: If number is not numeric or decimals not int.

**Ejemplo:**
```python
from shortfx.fxString.string_format import fixed

result = fixed(...)
```

---

### `format_as_currency()`

Formats a number as currency text with thousands separator.

**Parameters:**
- number: The number to format.
- decimals: Number of decimal places (default 2).
- symbol: Currency symbol to prepend (default '$').

**Returns:**
- The formatted currency string.

**Raises:**
- TypeError: If number is not numeric or decimals is not an integer.

**Ejemplo:**
```python
from shortfx.fxString.string_format import format_as_currency

result = format_as_currency(...)
```

---

### `is_credit_card_format()`

Validate a credit card number using the Luhn algorithm.

**Parameters:**
- text: Credit card number string.

**Returns:**
- True if the number passes the Luhn check.

**Ejemplo:**
```python
from shortfx.fxString.string_evaluations import is_credit_card_format

result = is_credit_card_format(...)
```

---

### `is_ipv4()`

Check whether a string is a valid IPv4 address.

**Parameters:**
- text: String to validate.

**Returns:**
- True if the string is a valid IPv4 address.

**Ejemplo:**
```python
from shortfx.fxString.string_evaluations import is_ipv4

result = is_ipv4(...)
```

---

### `is_ipv6()`

Check whether a string is a valid IPv6 address.

**Parameters:**
- text: String to validate.

**Returns:**
- True if the string is a valid IPv6 address.

**Ejemplo:**
```python
from shortfx.fxString.string_evaluations import is_ipv6

result = is_ipv6(...)
```

---

### `is_json()`

Check whether a string is valid JSON.

**Parameters:**
- text: String to validate.

**Returns:**
- True if the string can be parsed as JSON.

**Ejemplo:**
```python
from shortfx.fxString.string_evaluations import is_json

result = is_json(...)
```

---

### `is_uuid()`

Check whether a string matches the UUID format (any version).

**Parameters:**
- text: String to validate.

**Returns:**
- True if the string is a valid UUID.

**Ejemplo:**
```python
from shortfx.fxString.string_evaluations import is_uuid

result = is_uuid(...)
```

---

### `slugify()`

Converts text to a URL-friendly slug.

**Parameters:**
- text: The input string.
- separator: Character used between words (default ``-``).

**Returns:**
- A URL-safe slug string.

**Ejemplo:**
```python
from shortfx.fxString.string_operations import slugify

result = slugify(...)
```

---

### `snake_to_camel()`

Converts a snake_case string to camelCase (or PascalCase).

**Parameters:**
- text: The snake_case string.
- pascal: If True, returns PascalCase (first letter uppercase).
- Defaults to False (camelCase).

**Returns:**
- The camelCase or PascalCase equivalent.

**Ejemplo:**
```python
from shortfx.fxString.string_format import snake_to_camel

result = snake_to_camel(...)
```

---

### `substitute()`

Substitutes new text for old text in a string.

**Parameters:**
- text: The original text.
- old_text: The text to find and replace.
- new_text: The replacement text.
- instance_num: Which occurrence to replace (0 = all, 1 = first, etc.).

**Returns:**
- The text with substitutions applied.

**Raises:**
- TypeError: If text, old_text, or new_text are not strings.
- ValueError: If instance_num is negative.

**Ejemplo:**
```python
from shortfx.fxString.string_operations import substitute

result = substitute(...)
```

---

### `text_after()`

Returns text that occurs after a given delimiter.

**Parameters:**
- text: The input text to search.
- delimiter: The delimiter to search for.
- instance_num: Which occurrence (1 = first, -1 = last, etc.).

**Returns:**
- The text after the specified occurrence of the delimiter.

**Raises:**
- TypeError: If text or delimiter are not strings.
- ValueError: If instance_num is 0 or delimiter is not found.

**Ejemplo:**
```python
from shortfx.fxString.string_operations import text_after

result = text_after(...)
```

---

### `text_before()`

Returns text that occurs before a given delimiter.

**Parameters:**
- text: The input text to search.
- delimiter: The delimiter to search for.
- instance_num: Which occurrence (1 = first, -1 = last, etc.).

**Returns:**
- The text before the specified occurrence of the delimiter.

**Raises:**
- TypeError: If text or delimiter are not strings.
- ValueError: If instance_num is 0 or delimiter is not found.

**Ejemplo:**
```python
from shortfx.fxString.string_operations import text_before

result = text_before(...)
```

---

### `text_split()`

Splits text into rows and/or columns using delimiters.

**Parameters:**
- text: The input text to split.
- col_delimiter: Delimiter for splitting into columns. If None, no
- column splitting.
- row_delimiter: Delimiter for splitting into rows. If None, no
- row splitting.

**Returns:**
- A 2-D list of strings if both delimiters are provided,
- a 1-D list if only one delimiter is provided.

**Raises:**
- TypeError: If text is not a string.
- ValueError: If both delimiters are None.

**Ejemplo:**
```python
from shortfx.fxString.string_operations import text_split

result = text_split(...)
```

---

### `text_stats()`

Compute summary statistics for a text string.

**Parameters:**
- text: Input text.

**Returns:**
- Dict with keys: ``words``, ``chars``, ``chars_no_spaces``,
- ``sentences``, ``lines``, ``avg_word_length``.

**Ejemplo:**
```python
from shortfx.fxString.string_evaluations import text_stats

result = text_stats(...)
```

---

### `to_full_width()`

Converts half-width (single-byte) characters to full-width (double-byte).

**Parameters:**
- text: The input string containing half-width characters.

**Returns:**
- A new string with half-width characters replaced by full-width ones.

**Ejemplo:**
```python
from shortfx.fxString.string_convertions import to_full_width

result = to_full_width("HELLO")  # 'ＨＥＬＬＯ'
```

---

### `to_half_width()`

Converts full-width (double-byte) characters to half-width (single-byte).

**Parameters:**
- text: The input string containing full-width characters.

**Returns:**
- A new string with full-width characters replaced by half-width ones.

**Ejemplo:**
```python
from shortfx.fxString.string_convertions import to_half_width

result = to_half_width("ＨＥＬＬＯ")  # 'HELLO'
```

---

### `value_to_text()`

Converts any value to its text representation.

**Parameters:**
- value: Any Python value.
- format_type: 0 for concise (default), 1 for quoted/repr.

**Returns:**
- The text representation of the value.

**Ejemplo:**
```python
from shortfx.fxString.string_convertions import value_to_text

result = value_to_text(...)
```

---

### `word_at()`

Return the word at the given 1-indexed position.

**Parameters:**
- text: Input text.
- index: 1-based word position.

**Returns:**
- The word at the specified position.

**Raises:**
- IndexError: If index is out of range.

**Ejemplo:**
```python
from shortfx.fxString.string_operations import word_at

result = word_at(...)
```

---

### `word_wrap()`

Wraps text to a specified line width, breaking at word boundaries.

**Parameters:**
- text: The input text to wrap.
- width: Maximum number of characters per line. Defaults to 80.

**Returns:**
- The wrapped text with newline separators.

**Raises:**
- ValueError: If *width* is less than 1.

**Ejemplo:**
```python
from shortfx.fxString.string_format import word_wrap

result = word_wrap(...)
```

---

### `wrap_text()`

Wraps text to a specified line width at word boundaries.

**Parameters:**
- text: The input string.
- width: Maximum characters per line (default 80).

**Returns:**
- Word-wrapped text with newlines inserted.

**Raises:**
- ValueError: If width is less than 1.

**Ejemplo:**
```python
from shortfx.fxString.string_operations import wrap_text

result = wrap_text(...)
```

---

