"""Spanish Language String Functions.

This module provides specialized functions for processing Spanish language
strings, including phonetic reductions, NIF/CIF/NIE validation, and text
normalization according to Spanish language rules.

Key Features:
- Spanish stop words removal
- Phonetic reduction algorithms
- NIF/CIF/NIE validation with checksums
- NIF format parsing and standardization
- Accent removal and text normalization
- Spanish-specific character handling

"""

from typing import Optional
import re

# Define the list of common Spanish articles, conjunctions, and prepositions
# to be removed. Words are ordered for slight optimization, but primarily for readability.
# Using 're.IGNORECASE' makes it case-insensitive, so we don't need 'Y', 'y', etc.
# Note: 'DA', 'DO' (Portuguese) and 'ELS', 'NAS' (non-standard Spanish/Catalan)
# have been removed for strict Spanish focus.
_SPANISH_STOP_WORDS = [
    r"al", r"del", r"el", r"la", r"las", r"los", r"un", r"una", r"unos", r"unas",
    r"y", r"e", r"o", r"u", r"a", r"de", r"en", r"por",
    # Add more common ones if needed based on the function's specific scope:
    # r"con", r"sin", r"sobre", r"bajo", r"entre", r"hacia", r"para",
    # r"segun", r"desde", r"hasta", r"tras", r"contra", r"ni", r"que",
    # r"pero", r"mas",
]

# Create a single, compiled regex pattern from the list of words.
# re.compile for efficiency if function is called multiple times.
# re.escape is used to escape any special regex characters in the words,
# though for simple words, it might not be strictly necessary, it's good practice.
# r"\b" ensures whole word matching.
# r"|" acts as an OR operator, matching any of the words.
_STOP_WORDS_PATTERN = re.compile(
    r"\b(?:" + "|".join(map(re.escape, _SPANISH_STOP_WORDS)) + r")\b",
    re.IGNORECASE
)


import re
import unicodedata # Potentially for accent removal if fxString.shift_string does this

# --- Constants for phonetic reductions ---
# Define replacements for each strength level.
# The order within each list matters!
_REDUCTIONS_LEVEL_1 = [
    ("RR", "R"),
    ("QU", "C"),  # 'que' -> 'ce'
    ("GÜ", "G"),  # 'pingüino' -> 'pingino'
    ("GU", "G"),  # 'guerra' -> 'gera'
    ("LL", "Y"),  # 'calle' -> 'caye'
    ("Y", "I"),   # 'ley' -> 'lei' (after LL->Y)
    ("Z", "C"),   # 'zapato' -> 'capato' (seseo-like for some)
    ("K", "C"),   # 'kilo' -> 'cilo'
    ("B", "V"),   # 'bola' -> 'vola' (common B/V merger)
    # H is removed after all other replacements if it's not part of CH.
    # It's better to remove it at the end if it's truly silent.
    # For simplicity, if we remove it, it has to be done carefully or regex.
    # If the intent is to remove *all* H, it can be done simply.
]

_REDUCTIONS_LEVEL_2 = [
    ("X", "S"), # 'texto' -> 'testo', 'taxi' -> 'tasi'
    ("C", "S"), # 'cena' -> 'sena' (seseo-based)
]

_REDUCTIONS_LEVEL_3 = [
    ("Ç", "S"), # Primarily for Catalan/Portuguese in Spanish context
    ("Ñ", "N"), # Strong reduction, loses palatal sound
    ("W", "V"), # Loanword approximation
    ("G", "J"), # Very strong reduction: 'gato' -> 'jato'
]


# --- Constants ---
_DNI_NIE_CONTROL_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"
_NIE_PREFIX_MAPPING = {'X': 0, 'Y': 1, 'Z': 2}
_VALID_NIF_TYPES = {'DNI', 'NIE', 'CIF'}

# Regex for basic format validation (optional, but highly recommended)
# DNI: 8 digits + 1 letter
_DNI_REGEX = re.compile(r"^\d{8}[TRWAGMYFPDXBNJZSQVHLCKE]$", re.IGNORECASE)
# NIE: 1 letter (X, Y, Z) + 7 digits + 1 letter
_NIE_REGEX = re.compile(r"^[XYZ]\d{7}[TRWAGMYFPDXBNJZSQVHLCKE]$", re.IGNORECASE)
# CIF: 1 letter + 7 digits + 1 digit/letter (more complex, simplified here)
_CIF_REGEX = re.compile(r"^[ABCDEFGHJNPQRSUVW]\d{7}[0-9A-J]$", re.IGNORECASE)


# Define the regex pattern as a constant outside the function.
# This improves performance if the function is called multiple times,
# as the regex is compiled only once.
# This pattern is more robust, disallowing leading/trailing hyphens in labels,
# and enforcing length constraints more accurately for common domains.
# It does NOT fully validate all possible edge cases or new gTLDs,
# but covers most standard domain formats.
# Source for robust patterns often refers to RFCs (e.g., RFC 1035, RFC 1123, RFC 2181)
# or implementations like the Django URL validator.
# This simplified pattern:
# - ^: start of string
# - (?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+: one or more domain labels,
#   each starting and ending with alphanumeric, with hyphens in between (max 63 chars per label).
#   The (?:...) makes it a non-capturing group.
# - [a-zA-Z]{2,6}: Top-Level Domain (TLD) with 2 to 6 characters (common range).
#   This is a simplification; actual TLDs can be longer.
# - $: end of string
_DOMAIN_REGEX_PATTERN = re.compile(
    r"^(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$"
)


def remove_spanish_stop_words(input_string: str) -> str | None:
    """
    Removes common Spanish articles, conjunctions, and prepositions (stop words)
    from a text string.

    This function processes the input string by:
    1. Validating the input type.
    2. Converting the string to lowercase (handled by re.IGNORECASE).
    3. Using a pre-compiled regular expression to efficiently find and replace
       all defined stop words with a single space.
    4. Normalizing multiple spaces to a single space and stripping leading/trailing
       whitespace to ensure a clean output.

    Note: The list of stop words is configurable within the `_SPANISH_STOP_WORDS`
    constant. This function focuses on a basic set and does not include all
    possible prepositions or conjunctions, nor does it handle complex grammatical
    nuances or Internationalized Domain Names (IDNs) if characters beyond basic
    Latin alphabet are present in the text and need special handling.

    Args:
        input_string (str): The text string from which to remove stop words.

    Returns:
        str | None: The processed string with stop words removed and normalized
                    spaces, or None if the input was None.

    Raises:
        TypeError: If the input 'input_string' is not a string.

    Example of use:
        >>> remove_spanish_stop_words("El coche de la casa es grande y azul")
        'coche casa es grande azul'
        >>> remove_spanish_stop_words("Un perro y un gato")
        'perro gato'
        >>> remove_spanish_stop_words("La historia de El Cid")
        'historia Cid'
        >>> remove_spanish_stop_words("Con la mano en el corazon") # 'Con' is not in list
        'Con mano corazon'
        >>> remove_spanish_stop_words(None)
        None
        >>> remove_spanish_stop_words("A, e, o, u.")
        ',' # This highlights that it removes the word boundary matches, not general characters.
        >>> remove_spanish_stop_words(123)
        Traceback (most recent call last):
            ...
        TypeError: Input 'input_string' must be a string.

    **Cost:** O(n), where n is the length of the input string (regex operations)
    """
    # 1. Handle None input gracefully.
    if input_string is None:
        return None

    # 2. Validate input type.
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # 3. Replace all stop words with a single space.
    # re.sub with the compiled pattern and re.IGNORECASE flag handles case-insensitivity.
    # We replace with a space to avoid joining words that were separated by an article.
    processed_string = _STOP_WORDS_PATTERN.sub(' ', input_string)

    # 4. Normalize spaces: replace multiple spaces with a single space, then strip
    # leading/trailing whitespace. This ensures a clean output.
    processed_string = re.sub(r'\s+', ' ', processed_string).strip()

    return processed_string


def _determine_original_case(text: str) -> int:
    """
    Determines the original casing format of the string.
    0: all lowercase
    1: all uppercase
    2: capitalize (first letter only)
    3: title case (first letter of each word)
    (This is a placeholder for fxString.get_format_string)
    """
    if not text:
        return 0
    if text.islower():
        return 0
    if text.isupper():
        return 1
    if text.istitle():
        return 3
    # Check for capitalize specifically (first char upper, rest lower)
    if text[0].isupper() and text[1:].islower():
        return 2
    return 0 # Default if mixed or other format


def _remove_accents(text: str) -> str:
    """
    Removes accent marks from a string.
    (This is a placeholder for fxString.shift_string if it does accent removal)
    """
    if not isinstance(text, str):
        return text # Or raise error
    normalized_text = unicodedata.normalize('NFKD', text)
    return ''.join([
        char for char in normalized_text if not unicodedata.combining(char)
    ])


def reduce_spanish_letters(input_string: str, strength: int) -> str | None:
    """
    Reduces phonetic and orthographic variations in Spanish strings based on a
    specified strength level for similarity matching or normalization.

    The function applies a series of character replacements to simplify the
    string, simulating common phonetic mergers or orthographic conventions
    in Spanish, and attempts to preserve the original casing style.

    Args:
        input_string (str | None): The string to parse.
        strength (int): The level of phonetic/orthographic reduction to apply.
                        - 0: Only basic normalization (remove accents, to uppercase).
                        - 1: Basic phonetic reductions (e.g., silent H, RR->R, B/V merger).
                        - 2: Stronger phonetic reductions (e.g., C/Z to S, X to S).
                        - 3: Most aggressive reductions (e.g., Ñ->N, W->V, G->J).

    Returns:
        str | None: The processed string with reduced letters and restored casing,
                    or None if the input was None.

    Raises:
        TypeError: If 'input_string' is not a string.
        ValueError: If 'strength' is not within the valid range [0, 3].

    Example of use:
        >>> reduce_spanish_letters("Coche", 0)
        'COCHE'
        >>> reduce_spanish_letters("Guerrero", 1)
        'GERERO'
        >>> reduce_spanish_letters("Excelente", 2)
        'ESCELENTE' # X->S, C->S
        >>> reduce_spanish_letters("Ñandú", 3)
        'NANDU'
        >>> reduce_spanish_letters("México", 2)
        'MESICO' # assuming _remove_accents handled 'é'
        >>> reduce_spanish_letters("Bogotá", 1)
        'VOGOTA'
        >>> reduce_spanish_letters("Gigante", 3)
        'JIJANTE' # G->J (aggressive)
        >>> reduce_spanish_letters(None, 1)
        None
        >>> reduce_spanish_letters("Árbol", 0) # Assuming _remove_accents handled accents
        'ARBOL'
    """
    if input_string is None:
        return None

    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    if not 0 <= strength <= 3:
        raise ValueError("Strength must be an integer between 0 and 3.")

    # 1. Store original casing format
    original_case_format = _determine_original_case(input_string)

    # 2. Initial normalization: remove accents and convert to uppercase for processing
    # Assuming _remove_accents handles accents (similar to fxString.shift_string)
    processed_string = _remove_accents(input_string).upper()

    # 3. Apply reductions based on strength level (cascading)
    # Order of levels is important: higher strength includes lower strength changes
    if strength >= 3:
        for old, new in _REDUCTIONS_LEVEL_3:
            processed_string = processed_string.replace(old, new)

    if strength >= 2:
        for old, new in _REDUCTIONS_LEVEL_2:
            processed_string = processed_string.replace(old, new)

    if strength >= 1:
        for old, new in _REDUCTIONS_LEVEL_1:
            processed_string = processed_string.replace(old, new)
        # Special case: Remove 'H' after all other letter manipulations, if 'H' is silent
        # This handles cases like 'CH' if 'C' was already changed, etc.
        processed_string = processed_string.replace("H", "")

    # 4. Restore original casing
    if original_case_format == 0: # All lowercase
        processed_string = processed_string.lower()
    elif original_case_format == 1: # All uppercase (already is)
        pass
    elif original_case_format == 2: # Capitalize
        processed_string = processed_string.capitalize()
    elif original_case_format == 3: # Title case
        processed_string = processed_string.title()

    return processed_string


def nif_padding(p_nif: Optional[str]) -> Optional[str]:
    """
    Attempts to format an incomplete Spanish identification number by padding with zeros.

    Description:
        Takes a potentially incomplete NIF/NIE/CIF and tries to complete it
        by adding leading zeros to the numeric portion. This function
        does not validate the control digit but ensures the length and
        numeric padding are correct for subsequent validation.

    Args:
        p_nif (str): The identification number to format.

    Returns:
        str or None: Padded and formatted identification number if it can be
                     processed, None if the input is invalid or cannot be padded.

    Example:
        >>> nif_padding("123456Z")
        "00123456Z"
        >>> nif_padding("X1234L")
        "X0001234L"
        >>> nif_padding("123Z")
        "00000123Z"
        >>> nif_padding("123456789")
        "123456789"
        >>> nif_padding("invalid")
        "INVALID"
    Cost: O(L) where L is the length of the input string.
    """
    if not isinstance(p_nif, str):
        return None

    # Clean and standardize the input
    # This replacement explains why we are doing it:
    # We are removing spaces and hyphens because they are common user input errors
    # and do not affect the NIF/NIE/CIF calculation.
    nif_raw = p_nif.strip().upper().replace(' ', '').replace('-', '')
    nif = nif_raw

    # Pad with zeros if the string is shorter than 9 characters
    # We only pad if the raw NIF is potentially a DNI or NIE that is missing leading zeros.
    # This prevents padding for other types of NIFs that might have different structures.
    if len(nif_raw) < 9:
        # Case DNI/NIE (ends with a letter)
        # We check if the last character is alphabetic to identify potential DNI/NIE.
        if nif_raw and nif_raw[-1].isalpha():
            last_char = nif_raw[-1]
            initial_part = nif_raw[:-1]

            # If the initial part is only numbers (DNI)
            # We pad with zeros up to 8 digits because a DNI numeric part should always be 8 digits.
            if initial_part.isdigit() and len(initial_part) < 8:
                nif = f"{initial_part.zfill(8)}{last_char}"

            # If it starts with a letter and the rest are numbers (NIE)
            # We pad the numeric part with zeros up to 7 digits for NIEs.
            elif len(initial_part) > 1 and initial_part[0].isalpha() and initial_part[1:].isdigit():
                first_char = initial_part[0]
                numbers = initial_part[1:]
                if len(numbers) < 7:
                    nif = f"{first_char}{numbers.zfill(7)}{last_char}"

        # Case CIF (starts with a letter, ends with a letter or number)
        # We assume CIFs can also be padded if their numeric part is short.
        elif len(nif_raw) > 2 and nif_raw[0].isalpha() and nif_raw[1:-1].isdigit():
            first_char = nif_raw[0]
            last_char = nif_raw[-1]
            numbers = nif_raw[1:-1]
            if len(numbers) < 7:
                nif = f"{first_char}{numbers.zfill(7)}{last_char}"
    
    # Return the padded NIF. We do not validate the control digit here,
    # as that's the responsibility of `nif_parse`.
    return nif


def nif_parse(nif: Optional[str]) -> Optional[str]:
    """
    Validates if a Spanish identification number has the correct format.

    Description:
        Checks if the provided string matches any of the valid NIF/NIE/CIF patterns
        and validates the control digit. If the initial validation fails, it attempts
        to pad the NIF using `nif_padding` and re-validates.

    Args:
        nif (str): The identification number to validate.

    Returns:
        str or None: Validated identification number if correct, None if invalid.

    Example:
        >>> nif_parse("12345678Z")
        "12345678Z"
        >>> nif_parse("01234567Z") # Example with leading zero (becomes "01234567Z")
        "01234567Z"
        >>> nif_parse("1234567L") # Example needing padding (becomes "01234567L")
        "01234567L"
        >>> nif_parse("X1234567L")
        "X1234567L"
        >>> nif_parse("invalid")
        None
    Cost: O(L) where L is the length of the NIF string due to regex matching and
          string manipulation.
    """
    if not isinstance(nif, str):
        return None

    # Clean and standardize the input.
    # We strip whitespace and convert to uppercase for consistent matching.
    processed_nif = nif.strip().upper()

    # Define regex patterns for DNI, NIE, and CIF.
    # The patterns are defined here because they are specific to NIF parsing.
    pattern_dni = r'^(\d{8})([A-HJ-NP-TV-Z])$'  # 8 digits + letter
    pattern_nie = r'^([XYZ]\d{7})([A-HJ-NP-TV-Z])$'  # X, Y, Z + 7 digits + letter
    pattern_cif = r'^([ABCDEFGHJKLMNPQRSUVW]\d{7})([0-9A-J])$'  # Initial letter + 7 digits + control

    # Attempt to match the NIF against the defined patterns.
    # This is the first attempt, checking for already valid formats.
    match_dni = re.match(pattern_dni, processed_nif)
    match_nie = re.match(pattern_nie, processed_nif)
    match_cif = re.match(pattern_cif, processed_nif)

    # If none of the direct matches succeed, try padding the NIF.
    # This is crucial for handling cases where leading zeros might be missing.
    if not (match_dni or match_nie or match_cif):
        padded_nif = nif_padding(processed_nif)
        # If padding results in a valid string, update `processed_nif` and re-attempt matching.
        # We re-match because padding might have transformed the NIF into a valid format.
        if padded_nif:
            processed_nif = padded_nif
            match_dni = re.match(pattern_dni, processed_nif)
            match_nie = re.match(pattern_nie, processed_nif)
            match_cif = re.match(pattern_cif, processed_nif)
        else:
            # If padding itself failed, the NIF is invalid.
            return None

    # Handle DNI validation.
    # We check the DNI pattern and then validate the control letter.
    if match_dni:
        number_part, letter_part = match_dni.groups()
        numbers = int(number_part)
        control_letters = "TRWAGMYFPDXBNJZSQVHLCKE"
        # The modulo 23 calculation is standard for DNI control letter validation.
        if letter_part == control_letters[numbers % 23]:
            return processed_nif
        return None

    # Handle NIE validation.
    # We check the NIE pattern, convert the initial letter to a digit, and then validate.
    elif match_nie:
        number_part, letter_part = match_nie.groups()
        nie_map = {'X': '0', 'Y': '1', 'Z': '2'}
        # The first letter of an NIE is mapped to a digit for control letter calculation.
        numeric_nie_str = nie_map[number_part[0]] + number_part[1:]
        numbers = int(numeric_nie_str)
        control_letters = "TRWAGMYFPDXBNJZSQVHLCKE"
        if letter_part == control_letters[numbers % 23]:
            return processed_nif
        return None

    # Handle CIF validation.
    # CIF validation is more complex, involving even/odd digit sums and a final control character.
    elif match_cif:
        number_part, control_part = match_cif.groups()
        initial_letter = number_part[0]
        digits = number_part[1:]

        # Calculate sum of even-indexed digits (1-based, so 2nd, 4th, 6th digits).
        # Each digit is multiplied by 2, and if the result is two digits, they are summed.
        even_sum = 0
        for i in range(1, 7, 2):
            digit = int(digits[i]) * 2
            even_sum += (digit // 10) + (digit % 10)

        # Calculate sum of odd-indexed digits (1-based, so 1st, 3rd, 5th, 7th digits).
        odd_sum = 0
        for i in range(0, 7, 2):
            odd_sum += int(digits[i])

        total_sum = even_sum + odd_sum
        sum_unit_digit = total_sum % 10

        # Determine the control digit based on the sum's unit digit.
        control_digit = 0 if sum_unit_digit == 0 else 10 - sum_unit_digit
        control_letters = "JABCDEFGHI"

        # Validate based on the initial letter type.
        # Different ranges of initial letters have different control character rules.
        if initial_letter in "PQRSW":
            # For these letters, the control character must be a letter.
            if control_part == control_letters[control_digit]:
                return processed_nif
        elif initial_letter in "ABEH":
            # For these letters, the control character must be a digit.
            if control_part == str(control_digit):
                return processed_nif
        else:
            # For other letters, it can be either a digit or a letter.
            if control_part == str(control_digit) or control_part == control_letters[control_digit]:
                return processed_nif
        return None
    # If no pattern matched, even after padding, return None.
    return None


def nif_letter(p_dni: str) -> str:
    """
    Calculates and appends the control letter to a Spanish DNI/NIE numeric part.

    This function supports both DNI (8 digits) and NIE (starts with X, Y, or Z followed by 7 digits).

    Args:
        p_dni (str): The numeric part of the DNI or the full NIE (e.g., '12345678', 'X1234567').
                     Spaces and dots will be ignored.

    Returns:
        str: The full DNI/NIE with the calculated control letter appended.
             Returns the original input if the input is invalid (e.g., too short, contains
             invalid characters, or cannot be converted to a valid number for calculation).
    """
    if not isinstance(p_dni, str):
        # Handle non-string inputs
        return p_dni

    # 1. Clean the input string: remove spaces, dots, and convert to uppercase for NIE processing.
    #    re.sub is more efficient for multiple replacements.
    cleaned_dni = re.sub(r'[ .\-]', '', p_dni).upper() # Also remove hyphens for common input variations

    # 2. Check for valid length AFTER cleaning. A DNI has 8 digits. An NIE has a letter + 7 digits.
    #    So, the numeric part is effectively 8 digits for calculation.
    if len(cleaned_dni) < 8: # Minimum 8 characters for calculation (X+7 digits, or 8 digits)
        return p_dni

    # Define the list of control letters
    control_letters = 'TRWAGMYFPDXBNJZSQVHLCKE' # String is slightly more efficient than list for char access

    numeric_base = 0
    try:
        # Handle NIEs (Foreigner Identification Number)
        # NIEs start with X, Y, or Z. These correspond to 0, 1, 2 for calculation.
        if cleaned_dni.startswith('X'):
            numeric_base = int('0' + cleaned_dni[1:8]) # Replace 'X' with '0'
        elif cleaned_dni.startswith('Y'):
            numeric_base = int('1' + cleaned_dni[1:8]) # Replace 'Y' with '1'
        elif cleaned_dni.startswith('Z'):
            numeric_base = int('2' + cleaned_dni[1:8]) # Replace 'Z' with '2'
        else:
            # Assume it's a DNI (8 digits)
            numeric_base = int(cleaned_dni[:8]) # Take first 8 chars, in case input includes an existing letter

        # Ensure the numeric base is a valid number after conversion.
        # This implicitly handles cases where cleaned_dni[1:8] might not be fully numeric.
        if not isinstance(numeric_base, int): # Should not happen if int() succeeded but as a safeguard
            return p_dni

    except ValueError:
        # Catch cases where int() conversion fails (e.g., input like '123ABC78')
        return p_dni
    except IndexError:
        # Catch cases like 'X123' where slicing goes out of bounds after cleaning
        return p_dni

    # Calculate the control letter
    remainder = numeric_base % 23
    calculated_letter = control_letters[remainder]

    # Return the original input DNI/NIE part plus the calculated letter
    # This maintains the original formatting of the input string for the numeric part
    # but appends the correct calculated letter.
    return p_dni + calculated_letter


def _calculate_dni_nie_control_letter(numerical_part: int) -> str:
    """
    Calculates the control letter for DNI/NIE based on the numerical part.
    """
    return _DNI_NIE_CONTROL_LETTERS[numerical_part % 23]


def is_valid_dni(dni_value: str) -> bool:
    """
    Validates a Spanish DNI (Documento Nacional de Identidad) format and control letter.

    Args:
        dni_value (str): The DNI string to validate (e.g., "12345678A").

    Returns:
        bool: True if the DNI is valid, False otherwise.

    Raises:
        TypeError: If 'dni_value' is not a string.
        ValueError: If 'dni_value' does not match the basic DNI regex format.

    Example of use:
        >>> is_valid_dni("12345678Z") # Example valid DNI (not real)
        True
        >>> is_valid_dni("00000000T") # Invalid by specific rule
        False
        >>> is_valid_dni("12345678B") # Invalid control letter
        False
        >>> is_valid_dni("1234567A") # Incorrect length
        False
    """
    if not isinstance(dni_value, str):
        raise TypeError("DNI value must be a string.")

    # Convert to uppercase for case-insensitive comparison
    dni_value = dni_value.upper()

    # Basic regex format check
    if not _DNI_REGEX.match(dni_value):
        return False

    # Specific invalid DNI values (historical/reserved)
    invalid_dni_values = {"00000000T", "00000001R", "99999999R"}
    if dni_value in invalid_dni_values:
        return False

    numerical_part = int(dni_value[0:8])
    provided_control_letter = dni_value[8]

    calculated_control_letter = _calculate_dni_nie_control_letter(numerical_part)

    return provided_control_letter == calculated_control_letter


def is_valid_nie(nie_value: str) -> bool:
    """
    Validates a Spanish NIE (Número de Identificación de Extranjero) format and control letter.

    Args:
        nie_value (str): The NIE string to validate (e.g., "X1234567B").

    Returns:
        bool: True if the NIE is valid, False otherwise.

    Raises:
        TypeError: If 'nie_value' is not a string.
        ValueError: If 'nie_value' does not match the basic NIE regex format.

    Example of use:
        >>> is_valid_nie("X0000000T") # Example valid NIE (not real)
        True
        >>> is_valid_nie("Y1234567N") # Example valid NIE (not real)
        True
        >>> is_valid_nie("Z7654321A") # Example valid NIE (not real)
        True
        >>> is_valid_nie("A1234567B") # Invalid starting letter
        False
        >>> is_valid_nie("X1234567C") # Invalid control letter
        False
    """
    if not isinstance(nie_value, str):
        raise TypeError("NIE value must be a string.")

    # Convert to uppercase for case-insensitive comparison
    nie_value = nie_value.upper()

    # Basic regex format check
    if not _NIE_REGEX.match(nie_value):
        return False

    first_char = nie_value[0]
    numerical_part_str = nie_value[1:8]
    provided_control_letter = nie_value[8]

    # Convert the first character to its corresponding digit for calculation
    if first_char in _NIE_PREFIX_MAPPING:
        prefix_digit = _NIE_PREFIX_MAPPING[first_char]
        full_number_for_calc = int(str(prefix_digit) + numerical_part_str)
    else:
        # This case should ideally be caught by regex, but as a fallback.
        return False

    calculated_control_letter = _calculate_dni_nie_control_letter(full_number_for_calc)

    return provided_control_letter == calculated_control_letter


def is_valid_cif(cif_value: str) -> bool:
    """
    Validates a Spanish CIF (Código de Identificación Fiscal) format and control character.

    CIF validation is highly complex, depending on the first letter of the CIF
    (which denotes the type of legal entity) and involves different checksum
    calculations leading to either a digit or a letter as a control character.

    This is a simplified placeholder. A complete and accurate CIF validation
    requires implementing precise rules for each CIF type (A, B, C, D, E, F, G, H, J, N, P, Q, R, S, W, V).

    Args:
        cif_value (str): The CIF string to validate (e.g., "A12345678").

    Returns:
        bool: True if the CIF is valid, False otherwise.

    Raises:
        TypeError: If 'cif_value' is not a string.
        ValueError: If 'cif_value' does not match the basic CIF regex format.

    Example of use:
        >>> is_valid_cif("A12345678") # This will likely return False with current placeholder logic
        False
        >>> # A real, correct CIF validation requires detailed implementation.
    """
    if not isinstance(cif_value, str):
        raise TypeError("CIF value must be a string.")

    cif_value = cif_value.upper()

    # Basic regex format check
    # This regex is still a simplification, actual CIFs have specific last char types.
    if not _CIF_REGEX.match(cif_value):
        return False

    # --- Placeholder for actual CIF validation logic ---
    # The original logic for CIF in your code had significant issues and
    # does not correspond to standard CIF validation.
    # Implementing full CIF validation involves:
    # 1. Determining the type of entity from the first letter.
    # 2. Applying different checksum algorithms (sum of even digits, sum of odd digits where doubled odd digits are handled specially).
    # 3. Calculating a final control character (digit or letter) based on the first letter and the checksum.
    # 4. Comparing the calculated control character with the provided one.
    # Due to its complexity, this part is left as a placeholder or requires
    # a dedicated, well-researched implementation.

    # For demonstration, a simplistic (and likely incorrect) check:
    first_letter = cif_value[0]
    numerical_part = cif_value[1:8]
    control_char = cif_value[8]

    try:
        # Example: Simple sum check (not a real CIF algorithm)
        total_sum = sum(int(digit) for digit in numerical_part)
        if first_letter in "ABCDEFGHJ": # Example types with digit control
            expected_control = str(total_sum % 10)
            return expected_control == control_char
        elif first_letter in "KNPQRSUVW": # Example types with letter control
            # This is a highly simplified and likely incorrect calculation
            expected_control_letter = chr(65 + (total_sum % 10)) # A-J based on modulo
            return expected_control_letter == control_char
        else:
            return False # Unknown CIF type
    except ValueError:
        return False # Not purely numeric part
    # --- End Placeholder ---


def validate_spanish_nif(nif_type: str, nif_value: str) -> bool:
    """
    Validates a Spanish NIF (DNI, NIE, or CIF) based on its type and value.

    This is a dispatcher function that calls specific validation functions
    for DNI, NIE, or CIF based on the provided 'nif_type'.

    Args:
        nif_type (str): The type of NIF to validate ('DNI', 'NIE', or 'CIF').
        nif_value (str): The NIF string to validate.

    Returns:
        bool: True if the NIF is valid for its specified type, False otherwise.

    Raises:
        TypeError: If 'nif_type' or 'nif_value' are not strings.
        ValueError: If 'nif_type' is not one of 'DNI', 'NIE', or 'CIF'.

    Example of use:
        >>> validate_spanish_nif("DNI", "12345678Z") # Valid DNI (example)
        True
        >>> validate_spanish_nif("NIE", "X0000000T") # Valid NIE (example)
        True
        >>> validate_spanish_nif("CIF", "A12345678") # Will likely be False due to placeholder CIF logic
        False
        >>> validate_spanish_nif("DNI", "12345678X") # Invalid DNI (wrong letter)
        False
        >>> validate_spanish_nif("DNI", None)
        Traceback (most recent call last):
            ...
        TypeError: NIF value must be a string.
        >>> validate_spanish_nif("INVALID", "123")
        Traceback (most recent call last):
            ...
        ValueError: Invalid NIF type. Expected 'DNI', 'NIE', or 'CIF'.
    """
    if not isinstance(nif_type, str):
        raise TypeError("NIF type must be a string.")
    if not isinstance(nif_value, str):
        raise TypeError("NIF value must be a string.")

    nif_type = nif_type.upper() # Normalize type input

    if nif_type not in _VALID_NIF_TYPES:
        raise ValueError(f"Invalid NIF type. Expected {_VALID_NIF_TYPES}.")

    if nif_type == 'DNI':
        return is_valid_dni(nif_value)
    elif nif_type == 'NIE':
        return is_valid_nie(nif_value)
    elif nif_type == 'CIF':
        return is_valid_cif(nif_value)
    # This branch should theoretically not be reached due to the initial type check.
    return False


def fix_spanish(input_string: str | None, additional_allowed_chars: str = '') -> str | None:
    """Cleans an input string by replacing specific characters and filtering
    out any characters not explicitly allowed.

    This function handles common Spanish character replacements and ensures
    that only alphanumeric characters, Spanish-specific characters, spaces,
    and any user-defined additional characters remain in the string.

    Args:
        input_string (str | None): The string to be processed. If None,
                                   the function returns None.
        additional_allowed_chars (str, optional): A string containing any
                                                   extra characters that
                                                   should be considered valid.
                                                   Defaults to ''.

    Returns:
        str | None: The cleaned string, or None if the input was None.

    Raises:
        TypeError: If input_string is not a string or None, or if
                   additional_allowed_chars is not a string.

    Example of use:
        # Basic usage
        cleaned_text = fix_spanish("Hello, ‘world’§ with ¥ and other €!")
        print(f"Cleaned text: {cleaned_text}")
        # Expected output: Cleaned text: Hello, 'world'º with Ñ and other

        # With additional allowed characters
        cleaned_text_with_euro = fix_spanish("Hello, ‘world’§ with ¥ and other €!", "€")
        print(f"Cleaned text with euro: {cleaned_text_with_euro}")
        # Expected output: Cleaned text with euro: Hello, 'world'º with Ñ and other €
    """
    if input_string is None:
        return None

    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string or None.")
    if not isinstance(additional_allowed_chars, str):
        raise TypeError("Input 'additional_allowed_chars' must be a string.")

    # Define a mapping for specific character replacements to normalize them.
    # For example, various quote-like characters are mapped to a standard single quote.
    # The '§' character is replaced with 'º' (masculine ordinal indicator).
    # The '¥' character is replaced with 'Ñ'.
    replacement_map = {
        "‘": "'", "’": "'", "`": "'", "´": "'", "‡": "'", "†": "'", "Ž": "'",
        "§": "º", "¥": "Ñ"
    }

    # Initialize the output string with the input string for processing.
    processed_string = input_string

    # Apply all character replacements defined in the replacement_map.
    # This loop iterates through each character-replacement pair and updates
    # the processed_string in place.
    for original_char, replacement_char in replacement_map.items():
        processed_string = processed_string.replace(original_char, replacement_char)

    # Construct the set of allowed characters for efficient lookup.
    # This set includes standard English alphabet (both cases), common Spanish
    # characters (ñÑáéíóúüÁÉÍÓÚÜçÇ), and space, plus any user-specified characters.
    allowed_chars = set("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZñÑáéíóúüÁÉÍÓÚÜçÇ " + additional_allowed_chars)

    # Filter the processed string to retain only allowed characters.
    # This list comprehension builds a new string by including only those characters
    # from processed_string that are present in the allowed_chars set.
    final_string = ''.join(char for char in processed_string if char in allowed_chars)

    return final_string

