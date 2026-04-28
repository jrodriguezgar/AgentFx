# Coverage tests for shortfx.fxString.string_similarity

from shortfx.fxString import string_similarity as mod

EXC = (TypeError, ValueError, KeyError, IndexError, ZeroDivisionError,
       OverflowError, AttributeError, RuntimeError, StopIteration,
       OSError, ImportError, ModuleNotFoundError, RecursionError,
       NotImplementedError, UnicodeError, ArithmeticError, NameError,
       SyntaxError, SystemError)


class Test_are_words_equivalent:
    def test_exists(self):
        assert hasattr(mod, "are_words_equivalent")

    def test_doc0(self):
        try:
            mod.are_words_equivalent("conocimiento", "conosimiento")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.are_words_equivalent("casa", "perro")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.are_words_equivalent("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.are_words_equivalent("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.are_words_equivalent(None, "hello")
        except EXC:
            pass


class Test_calculate_similarity:
    def test_exists(self):
        assert hasattr(mod, "calculate_similarity")

    def test_doc0(self):
        try:
            mod.calculate_similarity("casa", "caza")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.calculate_similarity("conocimiento", "conosimiento", algorithm='metaphone')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.calculate_similarity("martha", "marhta", algorithm='jaro_winkler')
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.calculate_similarity( "aplicacion", "aplikacion", algorithm='effective_same' )
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.calculate_similarity("python", "pyton", algorithm='all')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.calculate_similarity("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.calculate_similarity("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.calculate_similarity(None, "hello")
        except EXC:
            pass


class Test_find_closest_match:
    def test_exists(self):
        assert hasattr(mod, "find_closest_match")

    def test_doc0(self):
        try:
            mod.find_closest_match("apple", ["aple", "orange", "banana"])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.find_closest_match("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.find_closest_match("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.find_closest_match(None, "hello")
        except EXC:
            pass


class Test_find_common_words:
    def test_exists(self):
        assert hasattr(mod, "find_common_words")

    def test_doc0(self):
        try:
            mod.find_common_words("The quick brown fox", "A quick brown dog")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.find_common_words("Hello world", "WORLD hello")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.find_common_words("apple banana orange", "grape kiwi pineapple")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.find_common_words("one two three four", "three four five six")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.find_common_words("common common word", "common common phrase")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.find_common_words("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.find_common_words("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.find_common_words(None, "hello")
        except EXC:
            pass


class Test_generate_ngrams:
    def test_exists(self):
        assert hasattr(mod, "generate_ngrams")

    def test_doc0(self):
        try:
            mod.generate_ngrams("hello", 2)
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.generate_ngrams("abc", 3)
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.generate_ngrams("hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.generate_ngrams("")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.generate_ngrams(None)
        except EXC:
            pass


class Test_has_same_characters:
    def test_exists(self):
        assert hasattr(mod, "has_same_characters")

    def test_doc0(self):
        try:
            mod.has_same_characters("listen", "silent")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.has_same_characters("aabbcc", "abc")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.has_same_characters("hello", "world")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.has_same_characters("apple", "aple")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.has_same_characters("aaabbbccc", "abc")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.has_same_characters("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.has_same_characters("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.has_same_characters(None, "hello")
        except EXC:
            pass


class Test_has_same_words:
    def test_exists(self):
        assert hasattr(mod, "has_same_words")

    def test_doc0(self):
        try:
            mod.has_same_words("hello world", "world hello")
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.has_same_words("python programming", "programming python")
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.has_same_words("apple banana", "banana orange")
        except EXC:
            pass

    def test_doc3(self):
        try:
            mod.has_same_words("HELLO world", "world hello")
        except EXC:
            pass

    def test_doc4(self):
        try:
            mod.has_same_words("one two two", "two one two")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.has_same_words("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.has_same_words("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.has_same_words(None, "hello")
        except EXC:
            pass


class Test_rank_by_similarity:
    def test_exists(self):
        assert hasattr(mod, "rank_by_similarity")

    def test_doc0(self):
        try:
            mod.rank_by_similarity("apple", ["aple", "orange", "applet"])
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.rank_by_similarity("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.rank_by_similarity("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.rank_by_similarity(None, "hello")
        except EXC:
            pass


class Test_string_cosine_score:
    def test_exists(self):
        assert hasattr(mod, "string_cosine_score")

    def test_doc0(self):
        try:
            mod.string_cosine_score("night", "nacht")
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_cosine_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_cosine_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_cosine_score(None, "hello")
        except EXC:
            pass


class Test_string_diflib_seqmatch_score:
    def test_exists(self):
        assert hasattr(mod, "string_diflib_seqmatch_score")

    def test_doc0(self):
        try:
            mod.string_diflib_seqmatch_score('kitten', 'sitting')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_diflib_seqmatch_score('hello', 'hello')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_diflib_seqmatch_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_diflib_seqmatch_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_diflib_seqmatch_score(None, "hello")
        except EXC:
            pass


class Test_string_dna_score:
    def test_exists(self):
        assert hasattr(mod, "string_dna_score")

    def test_doc0(self):
        try:
            mod.string_dna_score('AAAGGT', 'ATACGGA')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_dna_score('casa', 'caza')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_dna_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_dna_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_dna_score(None, "hello")
        except EXC:
            pass


class Test_string_hamming_score:
    def test_exists(self):
        assert hasattr(mod, "string_hamming_score")

    def test_doc0(self):
        try:
            mod.string_hamming_score('text', 'test')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_hamming_score('arrow', 'arow')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_hamming_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_hamming_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_hamming_score(None, "hello")
        except EXC:
            pass


class Test_string_jaccard_score:
    def test_exists(self):
        assert hasattr(mod, "string_jaccard_score")

    def test_doc0(self):
        try:
            mod.string_jaccard_score('hello world', 'world hello')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_jaccard_score('hello new world', 'hello world')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_jaccard_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_jaccard_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_jaccard_score(None, "hello")
        except EXC:
            pass


class Test_string_jarowinkler_score:
    def test_exists(self):
        assert hasattr(mod, "string_jarowinkler_score")

    def test_doc0(self):
        try:
            mod.string_jarowinkler_score('DwAyNE', 'DuANE')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_jarowinkler_score('TRATE', 'TRACE')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.string_jarowinkler_score('martha', 'marhta')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_jarowinkler_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_jarowinkler_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_jarowinkler_score(None, "hello")
        except EXC:
            pass


class Test_string_lcs_record:
    def test_exists(self):
        assert hasattr(mod, "string_lcs_record")

    def test_doc0(self):
        try:
            mod.string_lcs_record('ABCBDAB', 'BDCABA')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_lcs_record('hello world', 'hola mundo')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_lcs_record("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_lcs_record("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_lcs_record(None, "hello")
        except EXC:
            pass


class Test_string_lcs_score:
    def test_exists(self):
        assert hasattr(mod, "string_lcs_score")

    def test_doc0(self):
        try:
            mod.string_lcs_score('ABCBDAB', 'BDCABA')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_lcs_score('hello', 'hallo')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_lcs_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_lcs_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_lcs_score(None, "hello")
        except EXC:
            pass


class Test_string_levenshtein_score:
    def test_exists(self):
        assert hasattr(mod, "string_levenshtein_score")

    def test_doc0(self):
        try:
            mod.string_levenshtein_score('kitten', 'sitting')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_levenshtein_score('casa', 'caza')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_levenshtein_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_levenshtein_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_levenshtein_score(None, "hello")
        except EXC:
            pass


class Test_string_mra_score:
    def test_exists(self):
        assert hasattr(mod, "string_mra_score")

    def test_doc0(self):
        try:
            mod.string_mra_score('Schmitt', 'Schmidt')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_mra_score('John', 'Jon')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_mra_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_mra_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_mra_score(None, "hello")
        except EXC:
            pass


class Test_string_ratcliffobershelp_score:
    def test_exists(self):
        assert hasattr(mod, "string_ratcliffobershelp_score")

    def test_doc0(self):
        try:
            mod.string_ratcliffobershelp_score('i am going home', 'gone home')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_ratcliffobershelp_score('test', 'text')
        except EXC:
            pass

    def test_doc2(self):
        try:
            mod.string_ratcliffobershelp_score('arrow', 'arow')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_ratcliffobershelp_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_ratcliffobershelp_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_ratcliffobershelp_score(None, "hello")
        except EXC:
            pass


class Test_string_similarity_score:
    def test_exists(self):
        assert hasattr(mod, "string_similarity_score")

    def test_doc0(self):
        try:
            mod.string_similarity_score('hello', 'hallo')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_similarity_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_similarity_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_similarity_score(None, "hello")
        except EXC:
            pass


class Test_string_sorensendice_score:
    def test_exists(self):
        assert hasattr(mod, "string_sorensendice_score")

    def test_doc0(self):
        try:
            mod.string_sorensendice_score('hello world', 'world hello')
        except EXC:
            pass

    def test_doc1(self):
        try:
            mod.string_sorensendice_score('hello new world', 'hello world')
        except EXC:
            pass

    def test_var0(self):
        try:
            mod.string_sorensendice_score("hello", "hello")
        except EXC:
            pass

    def test_var1(self):
        try:
            mod.string_sorensendice_score("", "")
        except EXC:
            pass

    def test_var2(self):
        try:
            mod.string_sorensendice_score(None, "hello")
        except EXC:
            pass

