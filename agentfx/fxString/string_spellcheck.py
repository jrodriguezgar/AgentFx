from collections import Counter
from typing import List, Optional, Dict

from .string_format import normalize_text


def _import_rapidfuzz():
    """Lazy-load rapidfuzz."""
    try:
        from rapidfuzz import process
    except ImportError:  # pragma: no cover
        raise ImportError(
            "rapidfuzz is required for spell-checking. "
            "Install it with: pip install rapidfuzz"
        )
    return process


def _import_spellchecker():
    """Lazy-load pyspellchecker."""
    try:
        from spellchecker import SpellChecker
    except ImportError:  # pragma: no cover
        raise ImportError(
            "pyspellchecker is required for spell-checking. "
            "Install it with: pip install pyspellchecker"
        )
    return SpellChecker


def _import_symspellpy():
    """Lazy-load symspellpy."""
    try:
        from symspellpy import SymSpell, Verbosity
    except ImportError:  # pragma: no cover
        raise ImportError(
            "symspellpy is required for spell-checking. "
            "Install it with: pip install symspellpy"
        )
    return SymSpell, Verbosity

# Constants
DEFAULT_EDIT_DISTANCE = 2
PREFIX_LENGTH = 7
FUZZY_SCORE_THRESHOLD = 85
DEFAULT_WORD_FREQUENCY = 100


class UniversalSpellChecker:
    """
    Multi-purpose spell checker engine that integrates SymSpell and RapidFuzz.
    """

    def __init__(self, language: str = "es", custom_vocabulary: Optional[List[str]] = None):
        """
        Initializes the UniversalSpellChecker.

        Args:
            language (str): The language code (e.g., 'es', 'en').
            custom_vocabulary (list, optional): Specific words to prioritize.
        """
        self.spell_checker = _import_spellchecker()(language=language)

        SymSpell, _ = _import_symspellpy()
        self.sym_spell = SymSpell(
            max_dictionary_edit_distance=DEFAULT_EDIT_DISTANCE,
            prefix_length=PREFIX_LENGTH
        )

        # Determine vocabulary source
        if custom_vocabulary:
            self.vocabulary = custom_vocabulary
        else:
            # Use keys from the generic dictionary
            self.vocabulary = list(self.spell_checker.word_frequency.words.keys())

        # Map normalized -> original for casing restoration
        self._normalized_map: Dict[str, str] = {}

        self._load_dictionary()

    def _load_dictionary(self) -> None:
        """Loads the vocabulary into SymSpell and creates the normalization map."""
        for word in self.vocabulary:
            clean_key = normalize_text(word)
            self._normalized_map[clean_key] = word

            # Load into SymSpell with high priority
            self.sym_spell.create_dictionary_entry(clean_key, DEFAULT_WORD_FREQUENCY)

    def correct(self, raw_word: str) -> str:
        """
        Corrects the input word using weighted voting (SymSpell + RapidFuzz).

        Aggregates results from SymSpell and RapidFuzz to determine the most
        likely correction. Prioritizes exact matches and low edit distances.

        Args:
            raw_word (str): The potentially misspelled word.

        Returns:
            str: The best correction found with original casing from vocabulary.
        """
        if not raw_word:
            return ""

        clean_input = normalize_text(raw_word)

        # Optimization: Check if the normalized input is already valid
        if clean_input in self._normalized_map:
            return self._normalized_map[clean_input]

        # 1. SymSpell Lookup
        sym_suggestion = self._get_symspell_suggestion(clean_input)

        # 2. RapidFuzz Lookup
        fuzz_suggestion = self._get_fuzzy_suggestion(clean_input)

        # 3. Decision Logic
        return self._decide_best_match(raw_word, sym_suggestion, fuzz_suggestion)

    def _get_symspell_suggestion(self, clean_input: str) -> Optional[str]:
        """Runs SymSpell lookup and maps back to original casing."""
        _, Verbosity = _import_symspellpy()
        suggestions = self.sym_spell.lookup(
            clean_input,
            Verbosity.CLOSEST,
            max_edit_distance=DEFAULT_EDIT_DISTANCE
        )

        if suggestions:
            # SymSpell returns normalized key. Map back to original.
            normalized_term = suggestions[0].term
            return self._normalized_map.get(normalized_term, normalized_term)

        return None

    def _get_fuzzy_suggestion(self, clean_input: str) -> Optional[str]:
        """Runs RapidFuzz lookup returning original casing."""
        _process = _import_rapidfuzz()
        # process.extractOne returns (match, score, index)
        match_result = _process.extractOne(
            clean_input,
            self.vocabulary,
            processor=normalize_text
        )

        if match_result and match_result[1] >= FUZZY_SCORE_THRESHOLD:
            return match_result[0]

        return None

    def _decide_best_match(self, raw_word: str, sym_match: Optional[str], fuzz_match: Optional[str]) -> str:
        """Determines the winner between algorithms."""
        if not sym_match and not fuzz_match:
            return raw_word

        candidates = []
        if sym_match:
            candidates.append(sym_match)
        if fuzz_match:
            candidates.append(fuzz_match)

        # If both exist and are different, this logic favors the most common one.
        # Since there are max 2 items, if they differ, Counter picks the first one encountered (SymSpell).
        # This implies SymSpell > RapidFuzz in priority (Edit Distance > Loose shape).
        most_common = Counter(candidates).most_common(1)[0][0]

        return most_common
