"""String Evaluation Functions.

This module provides comprehensive functions for evaluating and validating
various properties and formats of strings. It includes functions for checking
data types, validating formats (emails, URLs, domains), extracting information
from structured strings, and performing complex string comparisons.

Key Features:
- Character type validation (alphabetic, numeric, alphanumeric)
- Format validation (email, URL, domain, date, NIF/VAT)
- Pattern extraction (postal codes, phone numbers)
- Email parsing and domain validation
- Spanish NIF/CIF/NIE validation with checksums
- Substring presence and position checking

"""

import unicodedata
import re
from typing import Optional
from datetime import datetime as dt, date

import formulite.fxString.string_format as fxStrFmt
import formulite.fxString.string_operations as fxStrOps

# --- Constants for NIF/VAT Validation ---
# Pre-compiled regex patterns for efficiency
_VALID_COUNTRY_CODES = {
    'ES', 'DE', 'FR', 'PT', 'IT', 'EL', 'AT', 'BE', 'BG', 'HR', 'CY', 'CZ', 'DK', 'EE',
    'FI', 'HU', 'IE', 'LV', 'LT', 'LU', 'MT', 'NL', 'PL', 'RO', 'SK', 'SI', 'SE', 'GB', 'UK'
}

# General patterns for format validation (NOT checksum validation)
# These would ideally be compiled using re.compile()
_COUNTRY_NIF_PATTERNS = {
    'ES': [
        (re.compile(r'^[0-9]{8}[A-Z]$'), 'DNI'),
        (re.compile(r'^[XYZ][0-9]{7}[A-Z]$'), 'NIE'),
        (re.compile(r'^[A-HJKLMNPQRSUVW][0-9]{7}[0-9A-J]$'), 'CIF') # Simplified, CIF is complex
    ],
    'PT': [re.compile(r'^[0-9]{9}$')], # Portuguese NIF (just digits)
    'DE': [re.compile(r'^[0-9]{9}$')], # German Steuernummer or USt-IdNr. (VAT ID)
    # ... other countries
}

# Spanish DNI/NIE control character lookup
_DNI_NIE_CONTROL_LETTERS = "TRWAGMYFPDXBNJZSQVHLCKE"
_NIE_PREFIX_MAPPING = {'X': 0, 'Y': 1, 'Z': 2}


# Compile regex patterns once for efficiency, as they are static.
# \b ensures a "word boundary", so it matches whole numbers.
_POSTAL_CODE_5_DIGIT_PATTERN = re.compile(r'\b\d{5}\b')
_POSTAL_CODE_4_DIGIT_PATTERN = re.compile(r'\b\d{4}\b')

_DOMAIN_REGEX_PATTERN = re.compile(
    r"^(?!-)[A-Za-z0-9-]{1,63}(?<!-)"  # Domain label (e.g., 'example', 'sub-domain')
    r"(?:\.(?!-)[A-Za-z0-9-]{1,63}(?<!-))+"  # Subsequent labels, each preceded by a dot
    r"\.[A-Za-z]{2,63}$"  # Top-Level Domain (TLD) - 2 to 63 letters
)


def contains_digit(input_string: str) -> bool:
    """
    Checks if the given string contains at least one digit.

    This function iterates through each character of the input string and
    returns True as soon as it finds any digit. If no digits are found
    after checking all characters, it returns False.

    Args:
        input_string: The string to be checked for the presence of digits.

    Returns:
        True if the string contains at least one digit, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Example of use:
        >>> contains_digit("abc123def")
        True
        >>> contains_digit("no_digits_here")
        False
        >>> contains_digit("")
        False
        >>> contains_digit("123")
        True

    **Cost:** O(n), where n is the length of the input string
    """
    if input_string is None:
        return input_string
        
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Use a generator expression with 'any()' for efficient checking.
    # 'any()' returns True as soon as the first digit is found,
    # avoiding unnecessary iterations.
    return any(char.isdigit() for char in input_string)


def same_letters(string_a: str, string_b: str) -> bool:
    """
    Checks if two strings contain the exact same characters, irrespective of their order.

    This function determines if one string is an anagram of another,
    meaning they are composed of the same characters with the same frequencies.
    The comparison is case-sensitive.

    Args:
        string_a (str): The first string for comparison.
        string_b (str): The second string for comparison.

    Returns:
        bool: True if both strings contain the same characters (same count, same case),
              False otherwise.

    Raises:
        TypeError: If 'string_a' or 'string_b' are not strings.

    Example:
        >>> same_letters("listen", "silent")
        True

        >>> same_letters("hello", "holle")
        True

        >>> same_letters("abc", "ab")
        False

        >>> same_letters("Aardvark", "aardvark")
        False

        >>> same_letters("", "")
        True

    **Cost:** O(n log n), where n is the maximum length of the two input strings (due to sorting)
    """
    if string_a is None or string_b is None:
        return None    
        
    if not isinstance(string_a, str):
        raise TypeError("Input 'string_a' must be a string.")
    if not isinstance(string_b, str):
        raise TypeError("Input 'string_b' must be a string.")

    # Convert both strings to sorted lists of their characters.
    # Sorting ensures that if the strings contain the same characters,
    # they will be in the same order after sorting, allowing for direct comparison.
    # This approach effectively checks for anagrams.
    return sorted(string_a) == sorted(string_b)


def is_alphabetic(alpha_string):
    """
    Checks if a given input is a single alphabetic character (letter),
    including common accented characters.

    **Cost:** O(1), constant time operation
    """
    if alpha_string is None:
        return alpha_string
        
    # 1. Handle non-string inputs or empty strings/strings longer than 1 character
    if not isinstance(alpha_string, str) or len(alpha_string) != 1:
        return False

    # 2. Use unicodedata.category to check if it's an alphabetic letter
    # 'L' category includes all Unicode letter characters (Lu, Ll, Lt, Lm, Lo)
    return unicodedata.category(alpha_string).startswith('L')


def is_numeric(input_string: str) -> bool:
    """
    Checks if a given string represents a numeric value (integer or float).

    This function attempts to cast the input string to a float. If the conversion
    is successful, it means the string can be interpreted as a number. This
    approach handles both integers and floating-point numbers, including
    negative values.

    Args:
        input_string (str): The string to check.

    Returns:
        bool: True if the string is numeric, False otherwise.

    Raises:
        None

    Example:
        is_numeric("123") returns True
        is_numeric("-45.67") returns True
        is_numeric("abc") returns False
        is_numeric("12a") returns False

    **Cost:** O(n), where n is the length of the input string (due to float conversion)
    """
    try:
        # Attempt to convert the string to a float.
        # This will raise a ValueError if the string is not a valid number.
        float(input_string)
        return True
    except ValueError:
        # If a ValueError is caught, the string is not numeric.
        return False
    

def is_aZ(aZ_string):
    """Checks if string contains only alphabetic characters.

    **Cost:** O(n), where n is the length of the input string
    """
    if aZ_string is None: return None
    else: return bool(re.match('^[a-zA-Z]*$',aZ_string))


def is_aZ09(aZ0_string):
    """Checks if string contains only alphanumeric characters.

    **Cost:** O(n), where n is the length of the input string
    """
    if aZ0_string is None: return None
    else: return bool(re.match('^[a-zA-Z0-9]*$',aZ0_string))


def is_internet_domain_format(domain_string: str) -> bool:
    """Checks if a given string adheres to the general format of an internet domain name.

    This function validates a string against common internet domain naming
    conventions. It ensures the string adheres to the standard format for
    domain names, including alphanumeric characters, hyphens (not at the
    beginning or end), and a valid-looking top-level domain (TLD).
    It does not validate against a specific list of registered TLDs.

    Args:
        domain_string (str): The string to be checked for domain format validity.

    Returns:
        bool: True if the string adheres to the general internet domain format, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Example of use:
        >>> is_internet_domain_format("example.com")
        True
        >>> is_internet_domain_format("sub.domain.org")
        True
        >>> is_internet_domain_format("invalid-domain")
        False
        >>> is_internet_domain_format("domain.c") # Fails because TLD is too short
        False

    **Cost:** O(n), where n is the length of the input string (regex matching)
    """
    if not isinstance(domain_string, str):
        # We raise a TypeError because the function expects a string input.
        # This helps in catching incorrect usage early.
        raise TypeError("Input must be a string.")

    # A regular expression is used to match the pattern of a valid domain name format.
    # It checks for:
    # ^: Start of the string.
    # (?!-): Ensures the domain does not start with a hyphen.
    # [A-Za-z0-9-]+: Matches one or more alphanumeric characters or hyphens.
    # (?<!-): Ensures the domain does not end with a hyphen.
    # (\.[A-Za-z0-9-]+)*: Matches subdomains, allowing multiple levels.
    # \.[A-Za-z]{2,}: Matches the Top-Level Domain (TLD), which must be at least two letters.
    # $: End of the string.
    # This regex balances strictness with common domain name variations for format.
    domain_pattern = re.compile(
        r"^(?!-)[A-Za-z0-9-]+(?<!-)(\.[A-Za-z0-9-]+)*(?<!-)\.[A-Za-z]{2,}$"
    )

    return bool(domain_pattern.match(domain_string))


def is_email_format(email_string: str) -> bool:
    """Checks if a given string has the general format of an email address.

    This function validates a string against a common regular expression pattern for email addresses.
    It verifies the presence of a local part, an '@' symbol, and a domain part
    (which follows standard domain naming conventions). It does not validate
    the email against a list of known domains or check for its existence.

    Args:
        email_string (str): The string to be checked for email format validity.

    Returns:
        bool: True if the string adheres to the general email format, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Example of use:
        >>> is_email_format("user@example.com")
        True
        >>> is_email_format("first.last@sub.domain.org")
        True
        >>> is_email_format("user+tag@domain.co.uk")
        True
        >>> is_email_format("invalid-email")
        False
        >>> is_email_format("user@domain") # Missing TLD
        False
        >>> is_email_format("user@.com") # Invalid domain start
        False

    **Cost:** O(n), where n is the length of the input string (regex matching)
    """
    if not isinstance(email_string, str):
        # We ensure the input is a string for robust function behavior,
        # raising a TypeError if not.
        raise TypeError("Input must be a string.")

    # This regular expression defines the pattern for a common email address format.
    # It attempts to balance strictness with common email address variations while
    # adhering to the structure defined by RFCs for practical purposes.
    #
    # Breakdown of the regex:
    # ^: Start of the string.
    # (?:[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+): Local part.
    #   (?:...) creates a non-capturing group for the local part.
    #   [a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+ matches one or more allowed characters
    #   in the local part of an email address. This is a broad set based on RFC 5322.
    # @: The mandatory 'at' symbol separating local and domain parts.
    # (?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+: Domain name part (labels before TLD).
    #   (?:...) is a non-capturing group for domain labels.
    #   [a-zA-Z0-9] ensures labels start with alphanumeric characters.
    #   (?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])? allows hyphens internally, not at start/end, max 61 chars.
    #   \.+ requires at least one dot between labels (e.g., sub.domain).
    # [a-zA-Z]{2,}: Top-Level Domain (TLD).
    #   [a-zA-Z]{2,} matches two or more alphabetic characters for the TLD.
    # $: End of the string.
    email_pattern = re.compile(
        r"^(?:[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+)"  # Local part
        r"@"  # Separator
        r"(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"  # Domain name part (labels)
        r"[a-zA-Z]{2,})$"  # Top-Level Domain (TLD)
    )

    return bool(email_pattern.match(email_string))


def is_url_format(url_string: str) -> bool:
    """Checks if a given string has the general format of a URL.

    This function validates a string against a common regular expression pattern for URLs.
    It considers various components such as scheme (http, https, ftp, etc.),
    domain/IP address, optional port, path, query parameters, and fragment identifier.
    It does not check if the URL actually exists or is accessible, only its structural validity.

    Args:
        url_string (str): The string to be checked for URL format validity.

    Returns:
        bool: True if the string adheres to the general URL format, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Example of use:
        >>> is_url_format("https://www.example.com")
        True
        >>> is_url_format("http://localhost:8080/path/to/resource?id=123#section")
        True
        >>> is_url_format("ftp://files.server.org/data.zip")
        True
        >>> is_url_format("invalid-url")
        False
        >>> is_url_format("www.example.com") # No scheme
        False
        >>> is_url_format("example.com/path") # No scheme
        False

    **Cost:** O(n), where n is the length of the input string (regex matching)
    """
    if not isinstance(url_string, str):
        # We raise a TypeError to ensure the function receives expected input,
        # promoting robust error handling.
        raise TypeError("Input must be a string.")

    # This regular expression is designed to capture common URL patterns.
    # It accounts for:
    # ^: Start of the string.
    # (?:[a-z]+:\/\/)?: Optional scheme (e.g., http://, https://, ftp://).
    #   (?:...) creates a non-capturing group.
    #   [a-z]+ matches one or more lowercase letters for the protocol name.
    #   :\/\/ matches the literal "://".
    # (?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+: Subdomains/domain labels.
    #   This part validates the domain name structure as defined by DNS (alphanumeric, hyphens, not at ends).
    # [a-z]{2,}: Top-Level Domain (TLD) of at least two letters.
    # (?:(?:[0-9]{1,3}\.){3}[0-9]{1,3}): Or an IPv4 address.
    # (?:(?::\d+)?(?:(?:\/[a-zA-Z0-9-._~:/?#\[\]@!$&'()*+,;=]*)?)?): Optional port, path, query, fragment.
    #   (?: :\d+)? : Optional port number preceded by a colon.
    #   (?: \/ ...)? : Optional path, allowing various URL-safe characters.
    # $: End of the string.
    # This regex aims for a balance between strictness and covering common URL variations,
    # ensuring a scheme is present.
    url_pattern = re.compile(
        r"^(?:[a-z]+:\/\/)"  # Scheme (e.g., http://, https://) - MANDATORY
        r"(?:(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"  # Domain name labels
        r"[a-z]{2,}"  # TLD (at least two letters)
        r"|"  # OR
        r"(?:(?:[0-9]{1,3}\.){3}[0-9]{1,3})" # IPv4 address
        r")"
        r"(?::\d+)?"  # Optional port number
        r"(?:/?|[/?]\S+)$" # Optional path, query, fragment (allowing most URL-safe characters)
    )

    return bool(url_pattern.match(url_string))


def has_date_format(value: str) -> bool:
    """
    Verifies if a given string matches any of a predefined list of common date and datetime formats.

    Args:
        value (str): The string to be checked.

    Returns:
        bool: True if the string matches one of the formats, False otherwise.

    **Cost:** O(k * m), where k is the number of date formats to try and m is the length of the input string
    """
    if not isinstance(value, str):
        return False

    # Require at least one of the typical date/time format separators to quickly filter non-date strings
    if not any(sep in value for sep in ['-', '/', 'T', ':']):
        return False

    # Define a list of common date and datetime formats to check against
    # We've added a few more robust ISO formats and microseconds support.
    format_list = [
        "%Y-%m-%d %H:%M:%S",      # e.g., "2023-10-27 15:30:00"
        "%Y-%m-%dT%H:%M:%S",      # e.g., "2023-10-27T15:30:00" (common ISO)
        "%Y-%m-%dT%H:%M:%SZ",     # e.g., "2023-10-27T15:30:00Z" (ISO with Z for UTC)
        "%Y-%m-%dT%H:%M:%S%z",    # e.g., "2023-10-27T15:30:00+01:00" (ISO with timezone offset)
        "%Y-%m-%d %H:%M:%S.%f",   # e.g., "2023-10-27 15:30:00.123456" (with microseconds)
        "%Y-%m-%dT%H:%M:%S.%f",   # e.g., "2023-10-27T15:30:00.123456" (ISO with microseconds)
        "%d/%m/%Y %H:%M:%S",      # e.g., "27/10/2023 15:30:00"
        "%d-%m-%Y %H:%M:%S",      # e.g., "27-10-2023 15:30:00"
        "%Y/%m/%d %H:%M:%S",      # e.g., "2023/10/27 15:30:00"
        "%Y-%m-%d",               # e.g., "2023-10-27"
        "%d/%m/%Y",               # e.g., "27/10/2023"
        "%d-%m-%Y",               # e.g., "27-10-2023"
        "%Y/%m/%d"                # e.g., "2023/10/27"
    ]

    # Iterate through the list of formats and try to parse the value
    for fmt in format_list:
        try:
            # Use dt.strptime to attempt parsing.
            # If successful, it means the string matches the format.
            dt.strptime(value, fmt)
            return True
        except ValueError:
            # If parsing fails, try the next format
            continue
            
    # If no format matches after trying all of them, return False
    return False


def has_numbers(input_string: str) -> bool:
    """
    Checks if the input string contains any numeric digits (0-9).

    This function iterates over each character in the provided string.
    If any character is found to be a digit, the function immediately
    returns True. If the loop completes without finding any digits,
    it means the string does not contain numbers, and the function
    returns False.

    Args:
        input_string (str): The string to check for digits.

    Returns:
        bool: True if the string contains at least one digit, False otherwise.

    Raises:
        None

    Example:
        has_numbers("abc123def") returns True
        has_numbers("python") returns False
        has_numbers("!@#$") returns False
        has_numbers("12345") returns True

    **Cost:** O(n), where n is the length of the input string
    """
    for char in input_string:
        # Check if the current character is a digit.
        # The 'isdigit()' method returns True for characters that are digits.
        if char.isdigit():
            return True
    # If the loop finishes, no digits were found in the string.
    return False


def has_substring(input_string: str, char_to_find: str) -> bool:
    """
    Checks if a specific character is present within a given string.

    This function utilizes the 'in' operator, which is the most Pythonic and
    readable way to determine if a substring (in this case, a single character)
    exists within another string. It returns True if the character is found,
    and False otherwise.

    Args:
        input_string (str): The string to search within.
        char_to_find (str): The character (or single-character string) to search for.

    Returns:
        bool: True if 'char_to_find' is found in 'input_string', False otherwise.

    Raises:
        ValueError: If 'char_to_find' is not a single character.

    Example:
        has_substring("hello world", "o") returns True
        has_substring("python", "z") returns False
        has_substring("programming", "g") returns True

    **Cost:** O(n), where n is the length of the input string
    """
    if not isinstance(char_to_find, str) or len(char_to_find) != 1:
        # Raises an error if the character to find is not a single character string.
        # This ensures the function is used as intended for character checks.
        raise ValueError("The 'char_to_find' argument must be a single character string.")

    # The 'in' operator is efficient and readable for checking membership.
    # It directly returns True if 'char_to_find' is found in 'input_string'.
    return char_to_find in input_string


def starts_with_substring(input_string: str, prefix: str, case_sensitive: bool = True) -> bool:
    """
    Checks if a string starts with a specific substring.

    Args:
        input_string (str): The string to check.
        prefix (str): The substring to look for at the beginning.
        case_sensitive (bool): If True, the comparison is case-sensitive.

    Returns:
        bool: True if the string starts with the prefix, False otherwise.

    Examples:
        starts_with_substring("hello world", "hello") returns True
        starts_with_substring("Hello World", "hello", case_sensitive=False) returns True
        starts_with_substring("filename.txt", "file") returns True
        starts_with_substring("data_123", "data_") returns True
        starts_with_substring("MyDocument", "document", case_sensitive=False) returns True
        starts_with_substring("MyDocument", "Doc") returns False

    **Cost:** O(m), where m is the length of the prefix
    """
    if not input_string:
        # An empty string cannot start with any prefix (unless prefix is also empty,
        # which Python's startswith handles as True, but for clarity in data transform,
        # we often treat empty inputs as non-matches for non-empty prefixes).
        return False
    
    if not prefix:
        # An empty prefix technically "starts" any string (including empty),
        # but in data transformation context, it often implies looking for content.
        # Python's startswith returns True for empty prefix. We'll follow that.
        return True # An empty prefix is considered to start any string.

    if case_sensitive:
        return input_string.startswith(prefix)
    else:
        return input_string.lower().startswith(prefix.lower())
    

def ends_with_substring(input_string: str, suffix: str, case_sensitive: bool = True) -> bool:
    """
    Checks if a string ends with a specific substring.

    Args:
        input_string (str): The string to check.
        suffix (str): The substring to look for at the end.
        case_sensitive (bool): If True, the comparison is case-sensitive.

    Returns:
        bool: True if the string ends with the suffix, False otherwise.

    **Cost:** O(m), where m is the length of the suffix
    """
    if not input_string:
        return False

    if case_sensitive:
        return input_string.endswith(suffix)
    else:
        return input_string.lower().endswith(suffix.lower())
   

def check_substring_at_position(main_string: str, substring: str, position: int | str) -> bool:
    """
    Checks if a substring exists at a specified position within a main string.

    This function supports checking at a numerical index, or at the 'start' or 'end'
    of the main string.

    Args:
        main_string (str): The string to search within.
        substring (str): The substring to search for.
        position (int | str): The starting index for the search, or 'start'/'end'.

    Returns:
        bool: True if the substring is found at the specified position, False otherwise.

    Raises:
        ValueError: If 'position' is an integer and is out of the valid range
                    for 'main_string'.
        TypeError: If 'position' is not an int or a string ('start' or 'end').

    Example of use:
        >>> check_substring_at_position("hello world", "hello", "start")
        True
        >>> check_substring_at_position("hello world", "world", "end")
        True
        >>> check_substring_at_position("hello world", "lo", 3)
        True
        >>> check_substring_at_position("hello world", "lo", 2)
        False
        >>> check_substring_at_position("hello world", "xyz", "start")
        False

    **Cost:** O(m), where m is the length of the substring
    """
    substring_length = len(substring)
    main_string_length = len(main_string)

    if isinstance(position, int):
        # We need to ensure the provided index is within the bounds of the main string.
        # This prevents IndexError when slicing.
        if not (-main_string_length <= position < main_string_length):
            raise ValueError(f"Position {position} is out of valid range for a string of length {main_string_length}.")
    elif isinstance(position, str):
        if position == 'start':
            position = 0
        elif position == 'end':
            # The 'end' position should align the start of the substring with the end of the main string.
            # For example, if main_string is "hello" and substring is "lo", the position should be 3.
            position = main_string_length - substring_length
        else:
            raise TypeError("Position must be an integer, 'start', or 'end'.")
    else:
        raise TypeError("Position must be an integer, 'start', or 'end'.")

    # If the calculated position is negative, it indicates that the substring
    # is longer than the remaining part of the main string from that position,
    # or that the substring itself is longer than the main string when checking 'end'.
    if position < 0 or position + substring_length > main_string_length:
        return False

    # Check if the slice of the main string matches the substring.
    return main_string[position:position + substring_length] == substring


def validate_substring_type(
    original_string: str,
    extract_method: str,
    expected_type: str,
    start_position: int = None,
    length: int = None,
    num_chars: int = None,
    date_format: str = None # Nuevo parámetro para fechas
) -> tuple[bool, str, str]:
    """
    Extrae una subcadena y verifica si su contenido corresponde a un tipo de dato esperado.

    Args:
        original_string (str): La cadena de la que se extraerá la subcadena.
        extract_method (str): El método de extracción ('substring', 'left', 'right').
        expected_type (str): El tipo de dato esperado ('numeric', 'integer', 'alphabetic', 'alphanumeric', 'date', 'boolean').
        start_position (int, optional): Posición inicial para 'substring'.
        length (int, optional): Longitud para 'substring' o 'left'.
        num_chars (int, optional): Número de caracteres para 'left' o 'right'.
        date_format (str, optional): Formato esperado si expected_type es 'date' (ej. '%Y-%m-%d').

    Returns:
        tuple[bool, str, str]: Una tupla que contiene:
            - bool: True si la subcadena es del tipo esperado, False en caso contrario.
            - str: La subcadena extraída.
            - str: Un mensaje de estado o error.

    Raises:
        ValueError: Si extract_method es inválido o faltan parámetros para la extracción.
        TypeError: Si los tipos de entrada no son correctos.

    **Cost:** O(n), where n is the length of the extracted substring
    """
    
    # If the input is None, do not execute the function
    if original_string is None:
        return False, "", "El argumento 'original_string' es None."

    # 1. Validar parámetros de entrada generales
    if not isinstance(original_string, str):
        raise TypeError("El argumento 'original_string' debe ser una cadena.")
    if not isinstance(extract_method, str):
        raise TypeError("El argumento 'extract_method' debe ser una cadena.")
    if not isinstance(expected_type, str):
        raise TypeError("El argumento 'expected_type' debe ser una cadena.")

    # 2. Extraer la subcadena según el método especificado
    sub = ""
    try:
        if extract_method == 'substring':
            if start_position is None or length is None:
                raise ValueError("Para 'substring', 'start_position' y 'length' son obligatorios.")
            sub = fxStrOps.substring(original_string, start_position, length)
        elif extract_method == 'left':
            if num_chars is None:
                raise ValueError("Para 'left', 'num_chars' es obligatorio.")
            sub = fxStrOps.left_substring(original_string, num_chars)
        elif extract_method == 'right':
            if num_chars is None:
                raise ValueError("Para 'right', 'num_chars' es obligatorio.")
            sub = fxStrOps.right_substring(original_string, num_chars)
        else:
            raise ValueError(f"Método de extracción '{extract_method}' no reconocido. Use 'substring', 'left' o 'right'.")
    except TypeError as e:
        return False, "", f"Error en los parámetros de extracción: {e}"
    except ValueError as e:
        return False, "", f"Error en los parámetros de extracción: {e}"

    if not sub: # Si la subcadena está vacía, no puede ser de ningún tipo
        return False, sub, "La subcadena extraída está vacía."

    # 3. Validar el tipo de la subcadena
    is_valid = False
    message = f"Subcadena '{sub}' no es de tipo '{expected_type}'."

    expected_type = expected_type.lower()

    if expected_type == 'numeric':
        # Permite números enteros o flotantes, con o sin signo
        if re.fullmatch(r"[-+]?\d*\.?\d+", sub):
            is_valid = True
            message = f"Subcadena '{sub}' es de tipo numérico."
    elif expected_type == 'integer':
        if sub.isdigit() or (sub.startswith('-') and sub[1:].isdigit()):
            is_valid = True
            message = f"Subcadena '{sub}' es de tipo entero."
    elif expected_type == 'alphabetic':
        if sub.isalpha():
            is_valid = True
            message = f"Subcadena '{sub}' es de tipo alfabético."
    elif expected_type == 'alphanumeric':
        if sub.isalnum():
            is_valid = True
            message = f"Subcadena '{sub}' es de tipo alfanumérico."
    elif expected_type == 'date':
        if date_format:
            try:
                dt.strptime(sub, date_format)
                is_valid = True
                message = f"Subcadena '{sub}' es una fecha válida con formato '{date_format}'."
            except ValueError:
                message = f"Subcadena '{sub}' no es una fecha válida con formato '{date_format}'."
        else:
            message = "Se requiere 'date_format' para validar el tipo 'date'."
    elif expected_type == 'boolean':
        normalized_sub = sub.lower()
        if normalized_sub in ['true', 'false', '1', '0']:
            is_valid = True
            message = f"Subcadena '{sub}' es de tipo booleano."
    else:
        message = f"Tipo esperado '{expected_type}' no soportado."

    return is_valid, sub, message


def get_phones(phone, p_separator=""):
    """
    Extracts potential phone numbers from a string.

    A phone number is identified as a sequence of digits that:
    1. Is at least 5 digits long after removing common phone number delimiters
       (spaces, hyphens, parentheses, dots) and any custom separators provided.
    2. May optionally start with a '+' sign.
    3. May contain common phone number delimiters internally.

    Args:
        phone (str): The input string to parse for phone numbers.
        p_separator (str, optional): A string containing additional characters
                                     that should be treated as allowed delimiters
                                     within a phone number but removed in the final output.
                                     Defaults to an empty string.

    Returns:
        list[str] or None: A list of cleaned phone numbers (digits only) if found,
                           otherwise None.

    **Cost:** O(n), where n is the length of the input string (regex operations)
    """
    if phone is None:
        return phone

    # Define characters that are allowed within a phone number string but should be stripped
    # for the final digit-only output. This includes common phone number separators
    # like spaces, hyphens, parentheses, dots, and any custom separators provided.
    # re.escape() is used to ensure p_separator characters are treated literally in the regex.
    allowed_internal_chars = re.escape(" \t\n\r\f\v-()." + p_separator)

    # Regex pattern to find potential phone number candidates:
    # - \+? : Optionally starts with a '+' sign (for international numbers).
    # - \d : Must contain at least one digit to start the sequence.
    # - [\d' + allowed_internal_chars + ']* : Followed by zero or more characters that are
    #                                         digits OR any of the allowed internal delimiters.
    # - \d : Must end with a digit (to avoid capturing strings like "word-").
    # This pattern captures a broader string that *looks* like a phone number,
    # including its formatting characters.
    phone_candidate_pattern = r'\+?\d[' + allowed_internal_chars + r'\d]*\d'

    # Find all occurrences of the phone candidate pattern in the input string.
    potential_phone_strings = re.findall(phone_candidate_pattern, phone)

    found_phones = []
    for candidate_str in potential_phone_strings:
        # Clean the extracted string: remove all non-digit characters.
        # This gives us the pure digit sequence of the potential phone number.
        cleaned_digits = re.sub(r'\D', '', candidate_str) # \D matches any non-digit character

        # Filter by minimum length. The original function used a minimum of 5 digits.
        if len(cleaned_digits) >= 5:
            found_phones.append(cleaned_digits)

    # Return the list of found phone numbers, or None if no valid numbers were found.
    if not found_phones:
        return None
    else:
        return found_phones


def get_postalcode(address: str) -> list[str] | None:
    """
    Extracts 5-digit or 4-digit postal codes from an address string.

    It first attempts to find all 5-digit number sequences that are whole "words".
    If no 5-digit codes are found, it then attempts to find all 4-digit number
    sequences that are whole "words".

    Args:
        address (str): The input address string.

    Returns:
        list[str] or None: A list of found postal codes (as strings).
                           Returns an empty list if no codes are found.
                           Returns None if the input `address` is None.

    **Cost:** O(n), where n is the length of the address string (regex search)
    """
    if address is None:
        return address
    
    # Ensure address is treated as a string, in case it's a number or other type.
    address_str = str(address)

    # First, try to find 5-digit postal codes
    found_codes = _POSTAL_CODE_5_DIGIT_PATTERN.findall(address_str)

    if not found_codes:
        # If no 5-digit codes are found, try to find 4-digit postal codes
        found_codes = _POSTAL_CODE_4_DIGIT_PATTERN.findall(address_str)
    
    # Return the list of found codes. If no codes are found, findall returns an empty list.
    return found_codes


def is_valid_email_format(email_string: str) -> bool:
    """
    Checks if a string has a valid email format.

    This function uses a regular expression to validate the basic structure
    of an email address, covering most common cases. It does not guarantee
    that the email address actually exists or is deliverable, only that its
    format is syntactically correct according to typical standards.

    Args:
        email_string: The string to be validated as an email address.

    Returns:
        True if the string is a valid email format, False otherwise.

    Raises:
        TypeError: If the input 'email_string' is not a string.

    Example of use:
        >>> is_valid_email("test@example.com")
        True
        >>> is_valid_email("invalid-email")
        False

    **Cost:** O(n), where n is the length of the email string (regex matching)
    """
    if not isinstance(email_string, str):
        raise TypeError("Input 'email_string' must be a string.")

    # The regular expression pattern for email validation.
    # This pattern generally follows the RFC 5322 standard for email addresses.
    # It checks for:
    # 1. A valid username part (before the '@'):
    #    - Can contain letters, numbers, dots, underscores, percents, plus, and hyphens.
    #    - Starts and ends with an alphanumeric character.
    # 2. An '@' symbol.
    # 3. A valid domain part (after the '@'):
    #    - Can contain letters, numbers, dots, and hyphens.
    #    - Each segment separated by a dot must be at least one character.
    #    - The top-level domain (TLD) must be at least two letters long.
    # We use re.IGNORECASE to make the match case-insensitive for email addresses.
    email_pattern = re.compile(r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", re.IGNORECASE)

    # Check if the email_string matches the pattern.
    # The 're.match' function checks for a match only at the beginning of the string.
    # Because our pattern covers the entire string (start with ^ and end with $),
    # it effectively validates the whole string.
    return bool(email_pattern.match(email_string))


def parse_email(email_address: str) -> dict | None:
    """
    Parses an email address string and returns its username and domain.

    This function expects a valid email address format containing a single '@' symbol.
    It splits the email into its two main components: the username and the domain.

    Args:
        email_address (str): The email address string to be parsed.

    Returns:
        dict | None: A dictionary with 'username' and 'domain' keys if the email is valid,
                     otherwise None if the '@' symbol is not found.

    Example of use:
        >>> parse_email("user@example.com")
        {'username': 'user', 'domain': 'example.com'}
        >>> parse_email("another.user+tag@sub.domain.co.uk")
        {'username': 'another.user+tag', 'domain': 'sub.domain.co.uk'}
        >>> parse_email("invalid-email")
        None

    **Cost:** O(n), where n is the length of the email string
    """
    if email_address is None:
        return email_address
        
    # Check if the '@' symbol is present in the email address.
    # This is a fundamental requirement for a valid email format.
    if "@" in email_address:
        # Split the email address at the first occurrence of '@'.
        # Using split("@", 1) ensures that only the first '@' is used as a delimiter,
        # which is important for email addresses that might have '@' in the username part
        # (though less common and often escaped).
        username, domain = email_address.split("@", 1)
        return {"username": username, "domain": domain}
    else:
        # Return None if the email address does not contain an '@' symbol,
        # indicating it's not in a recognizable email format.
        return None
    

def username_from_email(email_address: str) -> list[str] | None:
    """
    Extracts and returns a list of individual parts from an email's username.

    This function first parses the email to get the username. It then splits
    the username by common delimiters such as periods (.), hyphens (-), and
    underscores (_), returning a list of these parts. This is useful for
    extracting components of a name or identifier from an email address.

    Args:
        email_address (str): The full email address string.

    Returns:
        list[str] | None: A list of strings representing the parts of the username,
                          or None if the email address is invalid or cannot be parsed.

    Example of use:
        >>> username_from_email("john.doe_123@example.com")
        ['john', 'doe', '123']
        >>> username_from_email("jane-smith@domain.net")
        ['jane', 'smith']
        >>> username_from_email("simpleuser@mail.org")
        ['simpleuser']
        >>> username_from_email("invalid-email-format")
        None
        >>> username_from_email("another.user+tag@example.com") # Note: '+' is not split by default
        ['another', 'user+tag']

    **Cost:** O(n), where n is the length of the username (regex split operation)
    """
    if email_address is None:
        return email_address
        
    # Attempt to parse the email address using the helper function.
    # We directly use the output of parse_email, as it handles the primary
    # validity checks for the '@' symbol.
    parsed_email = parse_email(email_address)

    # If parse_email returned None, the email was invalid, so we propagate None.
    if parsed_email is None:
        return None

    # Extract the username part from the parsed email dictionary.
    username = parsed_email["username"]

    # Use regular expression to split the username by periods, hyphens, or underscores.
    # re.split is more flexible than str.split() as it allows multiple delimiters.
    # This directly replaces the functionality of fxString.split_all if it
    # served this specific purpose.
    # It removes empty strings that might result from consecutive delimiters.
    username_parts = [part for part in re.split(r'[\.\-_]', username) if part]

    return username_parts


def domain_from_email(email_address: str) -> str | None:
    """
    Extracts the domain part from a given email address string.

    This function utilizes a helper function (parse_email) to safely parse
    the email address. If the email is valid and contains a domain,
    that domain is returned. Otherwise, None is returned, indicating
    an invalid or unparsable email address.

    Args:
        email_address (str): The full email address string from which to extract the domain.

    Returns:
        str | None: The domain string (e.g., 'example.com') if the email is valid,
                    otherwise None.

    Raises:
        TypeError: If the input email_address is not a string.

    Example of use:
        >>> domain_from_email("user@example.com")
        'example.com'
        >>> domain_from_email("another.user@sub.domain.co.uk")
        'sub.domain.co.uk'
        >>> domain_from_email("invalid-email-format")
        None
        >>> domain_from_email("noat.com")
        None
        >>> domain_from_email(123)
        Traceback (most recent call last):
            ...
        TypeError: Input must be a string.

    **Cost:** O(n), where n is the length of the email string
    """
    if email_address is None:
        return email_address
        
    # First, validate that the input is indeed a string.
    # This prevents unexpected errors down the line if a non-string is passed.
    if not isinstance(email_address, str):
        raise TypeError("Input must be a string.")

    # Attempt to parse the email address using the helper function.
    # The parse_email function already handles the absence of '@' by returning None.
    parsed_email = parse_email(email_address)

    # If parsing failed (i.e., parse_email returned None), propagate None.
    # This happens if the email_address does not contain an '@' symbol.
    if parsed_email is None:
        return None

    # If parsing was successful, return the 'domain' part from the dictionary.
    return parsed_email["domain"]


def is_valid_domain_format(domain_string: str) -> bool:
    """
    Checks if a string conforms to a common internet domain name format.

    This function uses a regular expression to validate the structural format
    of a domain name (e.g., example.com, sub.domain.org). It ensures that
    the domain contains valid characters, follows the label-dot-label structure,
    and has a basic Top-Level Domain (TLD) structure.

    Important Considerations:
    - This validation is based on regex and only checks the *format*.
      It does NOT guarantee that the domain actually exists, is registered,
      or is reachable on the internet (e.g., via DNS lookup).
    - The regex pattern is designed for common domain names and might not
      cover all edge cases, new gTLDs, or Internationalized Domain Names (IDNs)
      without prior punycode conversion.
    - It disallows hyphens at the start or end of domain labels.

    Args:
        domain_string (str): The string to be validated as a domain name.

    Returns:
        bool: True if the string matches the expected domain format, False otherwise.

    Raises:
        TypeError: If the input 'domain_string' is not a string.

    Example of use:
        >>> is_valid_domain_format("example.com")
        True
        >>> is_valid_domain_format("sub.domain.co.uk")
        True
        >>> is_valid_domain_format("my-website.org")
        True
        >>> is_valid_domain_format("invalid") # Missing TLD
        False
        >>> is_valid_domain_format("no.hyphen-.com") # Hyphen at end of label
        False
        >>> is_valid_domain_format("-start.com") # Hyphen at start of label
        False
        >>> is_valid_domain_format("a.b") # TLD too short for this regex
        False
        >>> is_valid_domain_format("")
        False
        >>> is_valid_domain_format(123)
        Traceback (most recent call last):
            ...
        TypeError: Input 'domain_string' must be a string.

    **Cost:** O(n), where n is the length of the domain string (regex matching)
    """
    if domain_string is None:
        return domain_string
        
    # 1. Input Type Validation
    if not isinstance(domain_string, str):
        raise TypeError("Input 'domain_string' must be a string.")

    # 2. Handle empty string early (as regex won't match it)
    # The regex already implicitly handles empty strings by not matching them,
    # but an explicit check can be clearer depending on desired behavior.
    if not domain_string:
        return False

    # 3. Perform regex match
    # Use the pre-compiled pattern for efficiency.
    # re.match checks from the beginning of the string.
    return _DOMAIN_REGEX_PATTERN.match(domain_string) is not None


def email_belongs_to_name(name,email):
    """
    Checks if an email address belongs to a given name.

    **Cost:** O(n + m), where n is the length of the name and m is the length of the email
    """
    result = None

    if name and email:
        #case: fernando.bernabe@i3television.es into "Fernando Marcos Bernabé"
        formatted_name = fxStrFmt.format_name(name,"-",'PERSONA',True).lower()
        splitted_email = email.split('@')[0].lower()

        split_name = formatted_name.split()
        split_email = splitted_email.split('.')

        cleaned_email = re.sub(r'[^a-zA-Z0-9]', '', splitted_email)
        cleaned_name = re.sub(r'\s+', '', formatted_name) # Eliminar espacios y normalizar el nombre completo
        
        result = all(word in split_name for word in split_email)
        if not result:
            #case: javier.bravob@i3television.es into "Javier Bravo Benitez"            
            result = cleaned_email in cleaned_name # Comprobar si la cuenta de correo limpia está contenida en el nombre completo limpio
        if not result:
            #case: joseantonio.yraola@atresmedia.com into "Jose Antonio Alvarez de Yraola"
            result = True
            for word in split_email:
                if not word in cleaned_name: 
                    result = None
                    break
        if not result:
            #case: mtorrescam@atresadvertising.es into "Manuel Torres Cambron")
            #case: mivillanego@atresmedia.com into "Mª Isabel Villanego Calderon"
            iter_name = iter(cleaned_name)
            result = all(char in iter_name for char in cleaned_email) # Mantiene el orden de las letras
    
    return result


def _calculate_dni_nie_control_letter(numerical_part: int) -> str:
    """Calculates the control letter for DNI/NIE based on the numerical part.

    **Cost:** O(1), constant time operation
    """
    return _DNI_NIE_CONTROL_LETTERS[numerical_part % 23]


def _is_valid_spanish_dni(nif_value: str) -> bool:
    """Validates a Spanish DNI (format and checksum)."""
    # ... (Implementation from previous review)
    pass # Placeholder


def _is_valid_spanish_nie(nif_value: str) -> bool:
    """Validates a Spanish NIE (format and checksum)."""
    # ... (Implementation from previous review)
    pass # Placeholder


def _is_valid_spanish_cif(nif_value: str) -> bool:
    """Validates a Spanish CIF (format and checksum - highly complex)."""
    # ... (Placeholder from previous review, requires detailed research)
    pass # Placeholder


def _normalize_nif_input(raw_input: str) -> str:
    """
    Normalizes the input NIF string by removing spaces and converting to uppercase.

    **Cost:** O(n), where n is the length of the input string
    """
    if not isinstance(raw_input, str):
        raise TypeError("NIF input must be a string.")
    return raw_input.replace(' ', '').upper()


def validate_nif_format_and_type(raw_nif_string: str, assume_spanish_if_no_prefix: bool = True) -> tuple[bool, str | None, str | None, str | None, str | None]:
    """
    Validates the format of a NIF (Spanish DNI/NIE/CIF or other European NIFs/VAT IDs).

    This function performs initial normalization, extracts country prefixes,
    and checks the format against known patterns. For Spanish NIFs (DNI/NIE),
    it also performs a checksum validation. For other countries, it primarily
    validates the format using regular expressions.

    Args:
        raw_nif_string (str): The NIF string to validate.
        assume_spanish_if_no_prefix (bool): If True, treats a string without a recognized
                                            country prefix as a potential Spanish NIF.

    Returns:
        tuple: (is_valid, nif_type, country_name, country_code, cleaned_nif_value)
               - is_valid (bool): True if valid, False otherwise.
               - nif_type (str | None): 'DNI', 'NIE', 'CIF', 'NIF' (general), or None.
               - country_name (str | None): 'SPAIN', 'GERMANY', etc., or None.
               - country_code (str | None): 'ES', 'DE', etc., or None.
               - cleaned_nif_value (str | None): The NIF string without spaces, uppercase.

    Raises:
        TypeError: If 'raw_nif_string' is not a string.

    Example of use:
        # Example using placeholder functions for DNI/NIE/CIF
        # >>> validate_nif_format_and_type("12345678Z")
        # (True, 'DNI', 'SPAIN', 'ES', 'ES12345678Z')
        # >>> validate_nif_format_and_type("PT123456789")
        # (True, 'NIF', 'PORTUGAL', 'PT', 'PT123456789')
        # >>> validate_nif_format_and_type("invalid-nif")
        # (False, None, None, None, None)

    **Cost:** O(n), where n is the length of the NIF string (regex matching and string operations)
    """
    try:
        oparse = _normalize_nif_input(raw_nif_string)
    except TypeError as e:
        raise e # Re-raise TypeError from helper

    if not oparse:
        return False, None, None, None, None

    country_code_prefix = oparse[:2]
    nif_value_without_prefix = oparse

    # Determine actual country code and NIF value
    if country_code_prefix in _VALID_COUNTRY_CODES:
        country_code = country_code_prefix
        nif_value_without_prefix = oparse[2:]
    elif assume_spanish_if_no_prefix:
        country_code = 'ES'
        # If assuming ES, the whole oparse is the potential NIF
    else:
        # Unknown or no prefix, and not assuming Spanish
        return False, None, None, None, None

    # Handle special case for Portugal (if a 9-digit number without PT prefix)
    # This logic assumes the input might be just digits.
    if country_code == 'PT' and len(oparse) == 9 and oparse.isdigit():
        nif_value_without_prefix = oparse # The whole number is the NIF
        oparse = 'PT' + oparse # Add prefix for pattern matching

    # --- NIF Validation Logic ---
    if country_code == 'ES':
        # Apply specific Spanish validation (DNI, NIE, CIF)
        # This part needs to call your _is_valid_spanish_dni, _is_valid_spanish_nie, _is_valid_spanish_cif
        # and return the specific type and validity.
        # This is where 'p_find_letter' (now derived_control_letter_if_missing) would be used.
        # For this review, I'll provide simplified dispatch.
        if _is_valid_spanish_dni(nif_value_without_prefix): # Pass only the number part
            return True, 'DNI', 'SPAIN', 'ES', 'ES' + nif_value_without_prefix
        elif _is_valid_spanish_nie(nif_value_without_prefix): # Pass only the number part
            return True, 'NIE', 'SPAIN', 'ES', 'ES' + nif_value_without_prefix
        elif _is_valid_spanish_cif(nif_value_without_prefix): # Pass only the number part
            return True, 'CIF', 'SPAIN', 'ES', 'ES' + nif_value_without_prefix
        else:
            return False, None, None, None, None

    elif country_code in _COUNTRY_NIF_PATTERNS:
        # For other countries, iterate through defined patterns (format check only)
        # This is where you would lookup _COUNTRY_NIF_PATTERNS[country_code]
        # and match against oparse.
        # This placeholder assumes a simple format check.
        for pattern_re, nif_type in _COUNTRY_NIF_PATTERNS[country_code]:
            if pattern_re.match(nif_value_without_prefix): # Match the NIF without the prefix
                # Example for Portugal, where the NIF value often doesn't include the prefix
                cleaned_nif_value = nif_value_without_prefix if country_code not in ['PT', 'IT', 'EL'] else oparse
                return True, nif_type, country_code, country_code, cleaned_nif_value
        return False, None, None, None, None
    
    return False, None, None, None, None # Fallback for unmatched cases



def detect_quotes(text: Optional[str]) -> bool:
    """
    Detects if a string is enclosed in either single or double quotes.

    This function checks whether the input string starts and ends with the same
    quote character (either single quote ' or double quote "). It performs
    input validation to handle edge cases gracefully.

    Args:
        text (Optional[str]): The string to analyze. Can be None.

    Returns:
        bool: True if the string is quoted with matching single or double quotes,
              False otherwise (including None input, non-string input, or strings
              that are too short to be quoted).

    Raises:
        None

    Example of use:
        >>> detect_quotes("'hello world'")
        True
        >>> detect_quotes('"Python is great"')
        True
        >>> detect_quotes("unquoted text")
        False
        >>> detect_quotes("'mismatched\"")
        False
        >>> detect_quotes("")
        False
        >>> detect_quotes(None)
        False
        >>> detect_quotes("'")
        False

    **Cost:** O(1), constant time operation regardless of string length
    """
    # Define valid quote characters as a constant for clarity and maintainability
    VALID_QUOTES = ("'", '"')

    # Input validation: handle None, non-string types, and strings too short to be quoted
    if text is None or not isinstance(text, str) or len(text) < 2:
        return False

    # Check if first and last characters are the same and are valid quotes
    first_char = text[0]
    last_char = text[-1]

    return first_char == last_char and first_char in VALID_QUOTES


def count_words(input_string: str) -> int:
    """
    Counts the number of words in a given string.

    This function splits the string by whitespace characters and returns
    the total number of resulting words. It handles multiple spaces
    between words and leading/trailing spaces correctly, as `str.split()`
    by default splits by any whitespace and discards empty strings.

    Args:
        input_string (str): The string whose words are to be counted.

    Returns:
        int: The total number of words in the string.

    Raises:
        TypeError: If 'input_string' is not a string.

    Example:
        >>> count_words("Hello world")
        2

        >>> count_words("  Leading and trailing spaces ")
        4

        >>> count_words("SingleWord")
        1

        >>> count_words("")
        0

        >>> count_words("  ") # Only spaces
        0

    **Cost:** O(n), where n is the length of the input string
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # Split the string by any whitespace.
    # By default, str.split() without arguments handles multiple spaces
    # and leading/trailing spaces by discarding empty strings,
    # ensuring accurate word counting.
    words = input_string.split()

    # The number of words is simply the length of the resulting list.
    return len(words)


def count_characters(input_string: str, target_char: str) -> int:
    """
    Counts the occurrences of a specific character within a string.

    This function leverages the built-in `str.count()` method to efficiently
    determine how many times a given character appears in the input string.
    The comparison is case-sensitive.

    Args:
        input_string (str): The string to search within.
        target_char (str): The single character to count.

    Returns:
        int: The number of times 'target_char' appears in 'input_string'.

    Raises:
        TypeError: If 'input_string' is not a string or 'target_char' is not a string.
        ValueError: If 'target_char' is an empty string or contains more than one character.

    Example:
        >>> count_characters("hello world", "o")
        2

        >>> count_characters("programming", "g")
        2

        >>> count_characters("Banana", "a")
        3

        >>> count_characters("Banana", "A") # Case-sensitive
        0

        >>> count_characters("test", "x")
        0

    **Cost:** O(n), where n is the length of the input string
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(target_char, str):
        raise TypeError("Input 'target_char' must be a string.")
    if not target_char:
        raise ValueError("Input 'target_char' cannot be an empty string.")
    if len(target_char) != 1:
        raise ValueError("Input 'target_char' must be a single character.")

    # Use the built-in str.count() method for efficient character counting.
    # This method is optimized in C and is generally the fastest way to count occurrences.
    return input_string.count(target_char)
