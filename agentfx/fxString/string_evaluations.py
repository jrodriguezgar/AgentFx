import unicodedata
import re
import math
from typing import Optional
from datetime import datetime as dt

from . import string_format as fxStrFmt
from . import string_operations as fxStrOps

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

# Compile regex patterns once for efficiency, as they are static.
# \b ensures a "word boundary", so it matches whole numbers.
_POSTAL_CODE_5_DIGIT_PATTERN = re.compile(r'\b\d{5}\b')
_POSTAL_CODE_4_DIGIT_PATTERN = re.compile(r'\b\d{4}\b')

_DOMAIN_PATTERN = re.compile(
    r"^(?!-)[A-Za-z0-9-]+(?<!-)(\.[A-Za-z0-9-]+)*(?<!-)\.[A-Za-z]{2,}$"
)
_EMAIL_PATTERN = re.compile(
    r"^(?:[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+)"
    r"@"
    r"(?:(?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+"
    r"[a-zA-Z]{2,})$"
)
_URL_PATTERN = re.compile(
    r"^(?:[a-z]+:\/\/)"
    r"(?:(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+"
    r"[a-z]{2,}"
    r"|"
    r"(?:(?:[0-9]{1,3}\.){3}[0-9]{1,3})"
    r")"
    r"(?::\d+)?"
    r"(?:/?|[/?]\S+)$"
)


def is_alphabetic(alpha_string):
    """
    Checks if a given input is a single alphabetic character (letter),
    including common accented characters.
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
    if aZ_string is None:
        return None
    return bool(re.match('^[a-zA-Z]*$', aZ_string))


def is_aZ09(aZ0_string):
    if aZ0_string is None:
        return None
    return bool(re.match('^[a-zA-Z0-9]*$', aZ0_string))


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
    return bool(_DOMAIN_PATTERN.match(domain_string))


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
    return bool(_EMAIL_PATTERN.match(email_string))


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
    return bool(_URL_PATTERN.match(url_string))


def has_date_format(value: str) -> bool:
    """
    Verifies if a given string matches any of a predefined list of common date and datetime formats.

    Args:
        value (str): The string to be checked.

    Returns:
        bool: True if the string matches one of the formats, False otherwise.
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
    """Checks if the input string contains any numeric digits (0-9).

    Delegates to :func:`~agentfx.fxString.string_validations.contains_digit`.

    Args:
        input_string (str): The string to check for digits.

    Returns:
        bool: True if the string contains at least one digit, False otherwise.

    Raises:
        TypeError: If the input is not a string.

    Example:
        >>> has_numbers("abc123def")
        True
        >>> has_numbers("python")
        False
    """
    from agentfx.fxString.string_validations import contains_digit

    return contains_digit(input_string)


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
    """Checks if a string has a valid email format.

    Delegates to :func:`is_email_format`, which uses an RFC 5322-aligned
    regular expression for validation.

    Args:
        email_string: The string to be validated as an email address.

    Returns:
        True if the string is a valid email format, False otherwise.

    Raises:
        TypeError: If the input 'email_string' is not a string.

    Example of use:
        >>> is_valid_email_format("test@example.com")
        True
        >>> is_valid_email_format("invalid-email")
        False
    """
    return is_email_format(email_string)


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
    """Checks if a string conforms to a common internet domain name format.

    Delegates to :func:`is_internet_domain_format` after handling ``None``
    inputs (returns ``None`` for ``None``).

    Args:
        domain_string (str): The string to be validated as a domain name.

    Returns:
        bool: True if the string matches the expected domain format, False otherwise.

    Raises:
        TypeError: If the input 'domain_string' is not a string.

    Example of use:
        >>> is_valid_domain_format("example.com")
        True
        >>> is_valid_domain_format("invalid")
        False
    """
    if domain_string is None:
        return domain_string

    return is_internet_domain_format(domain_string)


def email_belongs_to_name(name,email):
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
                if word not in cleaned_name: 
                    result = None
                    break
        if not result:
            #case: mtorrescam@atresadvertising.es into "Manuel Torres Cambron")
            #case: mivillanego@atresmedia.com into "Mª Isabel Villanego Calderon"
            iter_name = iter(cleaned_name)
            result = all(char in iter_name for char in cleaned_email) # Mantiene el orden de las letras
    
    return result


def _is_valid_spanish_dni(nif_value: str) -> bool:
    """Validates a Spanish DNI (format and checksum)."""
    from agentfx.fxString.string_spanish import is_valid_dni

    return is_valid_dni(nif_value)


def _is_valid_spanish_nie(nif_value: str) -> bool:
    """Validates a Spanish NIE (format and checksum)."""
    from agentfx.fxString.string_spanish import is_valid_nie

    return is_valid_nie(nif_value)


def _is_valid_spanish_cif(nif_value: str) -> bool:
    """Validates a Spanish CIF (format and checksum)."""
    from agentfx.fxString.string_spanish import is_valid_cif

    return is_valid_cif(nif_value)


def _normalize_nif_input(raw_input: str) -> str:
    """
    Normalizes the input NIF string by removing spaces and converting to uppercase.
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

    Cost:
        O(1) - Constant time operation regardless of string length.
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


def word_frequency(text: str) -> dict[str, int]:
    """Calculates the frequency of each word in a text string.

    Words are split by whitespace and compared case-insensitively.

    Args:
        text: The input text.

    Returns:
        A dictionary mapping each lowercase word to its count.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> word_frequency("the cat and the dog")
        {'the': 2, 'cat': 1, 'and': 1, 'dog': 1}

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")

    from collections import Counter

    words = text.lower().split()
    return dict(Counter(words))


def char_frequency(text: str) -> dict[str, int]:
    """Calculates the frequency of each character in a string.

    Args:
        text: The input string.

    Returns:
        A dictionary mapping each character to its count.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> char_frequency("aab")
        {'a': 2, 'b': 1}

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")

    from collections import Counter

    return dict(Counter(text))


def sentence_count(text: str) -> int:
    """Counts the number of sentences in a text string.

    Sentences are detected by terminal punctuation (. ! ?).

    Args:
        text: The input text.

    Returns:
        The estimated number of sentences.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> sentence_count("Hello world. How are you? Fine!")
        3
        >>> sentence_count("No punctuation")
        1

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")

    if not text.strip():
        return 0

    # Count terminal punctuation sequences
    count = len(re.findall(r'[.!?]+', text))
    # If text has content but no terminal punctuation, count as 1 sentence
    return max(count, 1) if text.strip() else 0


def reading_time(text: str, words_per_minute: int = 200) -> float:
    """Estimates the reading time of a text in minutes.

    Args:
        text: The input text.
        words_per_minute: Average reading speed (default: 200 wpm).

    Returns:
        Estimated reading time in minutes (rounded to 1 decimal).

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> reading_time("word " * 400)
        2.0
        >>> reading_time("short text")
        0.1

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")

    if words_per_minute <= 0:
        words_per_minute = 200

    word_count = len(text.split())
    return round(max(word_count / words_per_minute, 0.1) if word_count > 0 else 0.0, 1)


# ---------------------------------------------------------------------------
# Extended validators and text analysis
# ---------------------------------------------------------------------------


def is_json(text: str) -> bool:
    """Check whether a string is valid JSON.

    Args:
        text: String to validate.

    Returns:
        True if the string can be parsed as JSON.

    Example:
        >>> is_json('{"key": "value"}')
        True
        >>> is_json('not json')
        False

    Complexity: O(n)
    """
    import json

    try:
        json.loads(text)
        return True
    except (json.JSONDecodeError, TypeError):
        return False


def is_uuid(text: str) -> bool:
    """Check whether a string matches the UUID format (any version).

    Args:
        text: String to validate.

    Returns:
        True if the string is a valid UUID.

    Example:
        >>> is_uuid('550e8400-e29b-41d4-a716-446655440000')
        True
        >>> is_uuid('not-a-uuid')
        False

    Complexity: O(1)
    """
    import uuid

    try:
        uuid.UUID(text)
        return True
    except (ValueError, AttributeError):
        return False


def is_ipv4(text: str) -> bool:
    """Check whether a string is a valid IPv4 address.

    Args:
        text: String to validate.

    Returns:
        True if the string is a valid IPv4 address.

    Example:
        >>> is_ipv4('192.168.1.1')
        True
        >>> is_ipv4('999.999.999.999')
        False

    Complexity: O(1)
    """
    import ipaddress

    try:
        ipaddress.IPv4Address(text.strip())
        return True
    except (ipaddress.AddressValueError, ValueError):
        return False


def is_ipv6(text: str) -> bool:
    """Check whether a string is a valid IPv6 address.

    Args:
        text: String to validate.

    Returns:
        True if the string is a valid IPv6 address.

    Example:
        >>> is_ipv6('::1')
        True
        >>> is_ipv6('192.168.1.1')
        False

    Complexity: O(1)
    """
    import ipaddress

    try:
        ipaddress.IPv6Address(text.strip())
        return True
    except (ipaddress.AddressValueError, ValueError):
        return False


def is_credit_card_format(text: str) -> bool:
    """Validate a credit card number using the Luhn algorithm.

    Strips spaces and dashes before validation.

    Args:
        text: Credit card number string.

    Returns:
        True if the number passes the Luhn check.

    Example:
        >>> is_credit_card_format('4532015112830366')
        True
        >>> is_credit_card_format('1234567890123456')
        False

    Complexity: O(n)
    """

    digits = text.replace(" ", "").replace("-", "")

    if not digits.isdigit() or len(digits) < 13 or len(digits) > 19:
        return False

    total = 0
    reverse_digits = digits[::-1]

    for i, ch in enumerate(reverse_digits):
        n = int(ch)

        if i % 2 == 1:
            n *= 2

            if n > 9:
                n -= 9

        total += n

    return total % 10 == 0


def count_sentences(text: str) -> int:
    """Count the number of sentences in a text.

    A sentence is defined as text ending with ``.``, ``!``, or ``?``.

    Args:
        text: Input text.

    Returns:
        Number of sentences.

    Example:
        >>> count_sentences("Hello world. How are you? Fine!")
        3

    Complexity: O(n)
    """

    if not text or not text.strip():
        return 0

    return len(re.findall(r'[.!?]+', text))


def text_stats(text: str) -> dict:
    """Compute summary statistics for a text string.

    Args:
        text: Input text.

    Returns:
        Dict with keys: ``words``, ``chars``, ``chars_no_spaces``,
        ``sentences``, ``lines``, ``avg_word_length``.

    Example:
        >>> stats = text_stats("Hello world. How are you?")
        >>> stats['words']
        5
        >>> stats['sentences']
        2

    Complexity: O(n)
    """

    words = text.split()
    word_count = len(words)
    char_count = len(text)
    chars_no_spaces = len(text.replace(" ", ""))
    sentence_count = count_sentences(text)
    line_count = text.count("\n") + 1 if text else 0
    avg_word = sum(len(w) for w in words) / word_count if word_count else 0.0

    return {
        "words": word_count,
        "chars": char_count,
        "chars_no_spaces": chars_no_spaces,
        "sentences": sentence_count,
        "lines": line_count,
        "avg_word_length": round(avg_word, 2),
    }


def is_palindrome(text: str) -> bool:
    """Checks whether a text is a palindrome (ignoring case, spaces and punctuation).

    Args:
        text: The input string to evaluate.

    Returns:
        True if the cleaned text reads the same forwards and backwards.

    Example:
        >>> is_palindrome("A man a plan a canal Panama")
        True
        >>> is_palindrome("hello")
        False

    Complexity: O(n)
    """
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', text).lower()
    return cleaned == cleaned[::-1]


def is_anagram(a: str, b: str) -> bool:
    """Checks whether two strings are anagrams of each other.

    Comparison is case-insensitive and ignores spaces and punctuation.

    Args:
        a: First string.
        b: Second string.

    Returns:
        True if both strings contain exactly the same letters.

    Example:
        >>> is_anagram("listen", "silent")
        True
        >>> is_anagram("hello", "world")
        False

    Complexity: O(n log n)
    """
    clean_a = sorted(re.sub(r'[^a-zA-Z0-9]', '', a).lower())
    clean_b = sorted(re.sub(r'[^a-zA-Z0-9]', '', b).lower())
    return clean_a == clean_b


def is_pangram(text: str, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> bool:
    """Checks whether a text contains every letter of the given alphabet.

    Args:
        text: The input string.
        alphabet: The set of required letters (default: English a-z).

    Returns:
        True if all alphabet letters appear at least once in *text*.

    Example:
        >>> is_pangram("The quick brown fox jumps over the lazy dog")
        True
        >>> is_pangram("Hello world")
        False

    Complexity: O(n + a) where a is the alphabet length.
    """
    lower = text.lower()
    return all(ch in lower for ch in alphabet.lower())


def compare_strings(string1: str, string2: str, case_sensitive: bool = True) -> int:
    """Compare two strings lexicographically.

    Returns ``-1``, ``0``, or ``1`` depending on whether *string1* is less
    than, equal to, or greater than *string2*.  Equivalent to VBA ``StrComp``.

    Args:
        string1: First string.
        string2: Second string.
        case_sensitive: If ``False``, comparison is case-insensitive.

    Returns:
        ``-1`` if string1 < string2, ``0`` if equal, ``1`` if string1 > string2.

    Example:
        >>> compare_strings("apple", "banana")
        -1
        >>> compare_strings("ABC", "abc", case_sensitive=False)
        0

    Complexity: O(min(len(string1), len(string2)))
    """
    a, b = (string1, string2) if case_sensitive else (string1.lower(), string2.lower())

    if a < b:
        return -1

    if a > b:
        return 1

    return 0


def text_entropy(text: str) -> float:
    """Calculates Shannon entropy of a string in bits per character.

    Measures the information density / randomness of the text.
    Higher values indicate more randomness; lower values more
    repetition or structure.

    Args:
        text: The input string to analyse.

    Returns:
        Shannon entropy in bits per character (0.0 for empty string).

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> round(text_entropy("aaaa"), 2)
        0.0
        >>> round(text_entropy("abcd"), 2)
        2.0

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        return 0.0

    length = len(text)
    freq: dict[str, int] = {}

    for ch in text:
        freq[ch] = freq.get(ch, 0) + 1

    entropy = 0.0

    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)

    return entropy


def is_balanced_brackets(text: str) -> bool:
    """Check whether all brackets in *text* are properly balanced and nested.

    Validates ``()``, ``[]``, and ``{}``.

    Args:
        text: Input string.

    Returns:
        ``True`` if every opening bracket has a matching closing bracket
        in the correct order.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> is_balanced_brackets("({[]})")
        True
        >>> is_balanced_brackets("([)]")
        False

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    stack: list[str] = []
    match = {")": "(", "]": "[", "}": "{"}

    for ch in text:

        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":

            if not stack or stack[-1] != match[ch]:
                return False

            stack.pop()

    return len(stack) == 0


def is_valid_hex_color(text: str) -> bool:
    """Check whether *text* is a valid hex colour code.

    Accepts ``#RGB``, ``#RGBA``, ``#RRGGBB``, or ``#RRGGBBAA``.

    Args:
        text: Input string.

    Returns:
        ``True`` if the string is a valid hex colour.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> is_valid_hex_color("#FF8800")
        True
        >>> is_valid_hex_color("red")
        False

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text.startswith("#"):
        return False

    hex_part = text[1:]

    if len(hex_part) not in (3, 4, 6, 8):
        return False

    return all(c in "0123456789abcdefABCDEF" for c in hex_part)


def is_valid_cron(expr: str) -> bool:
    """Validate a 5-field cron expression.

    Checks that each of the five space-separated fields (*minute*,
    *hour*, *day-of-month*, *month*, *day-of-week*) contains only
    valid characters and ranges.

    Args:
        expr: Cron expression string.

    Returns:
        ``True`` if the expression is syntactically valid.

    Raises:
        TypeError: If *expr* is not a string.

    Example:
        >>> is_valid_cron("0 12 * * 1-5")
        True
        >>> is_valid_cron("60 25 * * *")
        False

    Complexity: O(n)
    """
    if not isinstance(expr, str):
        raise TypeError("expr must be a string")

    fields = expr.strip().split()

    if len(fields) != 5:
        return False

    ranges = [(0, 59), (0, 23), (1, 31), (1, 12), (0, 7)]

    for field, (lo, hi) in zip(fields, ranges):

        for part in field.split(","):
            step_parts = part.split("/")

            if len(step_parts) > 2:
                return False

            val = step_parts[0]

            if val == "*":
                pass
            elif "-" in val:
                bounds = val.split("-")

                if len(bounds) != 2:
                    return False

                try:
                    a, b = int(bounds[0]), int(bounds[1])
                except ValueError:
                    return False

                if a < lo or b > hi or a > b:
                    return False
            else:

                try:
                    v = int(val)
                except ValueError:
                    return False

                if v < lo or v > hi:
                    return False

            if len(step_parts) == 2:

                try:
                    s = int(step_parts[1])
                except ValueError:
                    return False

                if s < 1:
                    return False

    return True


def is_valid_ipv4(text: str) -> bool:
    """Validate an IPv4 address string.

    Checks four dot-separated decimal octets, each in [0, 255].

    Args:
        text: String to validate.

    Returns:
        ``True`` if *text* is a valid IPv4 address.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> is_valid_ipv4("192.168.1.1")
        True

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    parts = text.strip().split(".")

    if len(parts) != 4:
        return False

    for p in parts:

        if not p.isdigit():
            return False

        val = int(p)

        if val < 0 or val > 255:
            return False

        # Reject leading zeros (e.g. "01")
        if len(p) > 1 and p[0] == "0":
            return False

    return True


def is_valid_ipv6(text: str) -> bool:
    """Validate an IPv6 address string.

    Supports full and compressed (``::``\\ ) notation.

    Args:
        text: String to validate.

    Returns:
        ``True`` if *text* is a valid IPv6 address.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> is_valid_ipv6("2001:0db8:85a3::8a2e:0370:7334")
        True

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    addr = text.strip()

    if "::" in addr:
        halves = addr.split("::")

        if len(halves) != 2:
            return False

        left = halves[0].split(":") if halves[0] else []
        right = halves[1].split(":") if halves[1] else []

        if len(left) + len(right) > 7:
            return False

        groups = left + ["0"] * (8 - len(left) - len(right)) + right
    else:
        groups = addr.split(":")

    if len(groups) != 8:
        return False

    hex_chars = set("0123456789abcdefABCDEF")

    for g in groups:

        if not g or len(g) > 4:
            return False

        if not all(c in hex_chars for c in g):
            return False

    return True


def is_valid_uuid(text: str) -> bool:
    """Validate a UUID string (versions 1-5).

    Expects the canonical 8-4-4-4-12 hex format.

    Args:
        text: String to validate.

    Returns:
        ``True`` if *text* matches UUID format.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> is_valid_uuid("550e8400-e29b-41d4-a716-446655440000")
        True

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text.strip().lower()

    if len(s) != 36:
        return False

    if s[8] != "-" or s[13] != "-" or s[18] != "-" or s[23] != "-":
        return False

    hex_chars = set("0123456789abcdef")

    for i, ch in enumerate(s):

        if i in (8, 13, 18, 23):
            continue

        if ch not in hex_chars:
            return False

    return True


def is_valid_semver(text: str) -> bool:
    """Validate a Semantic Versioning string (SemVer 2.0.0).

    Format: ``MAJOR.MINOR.PATCH[-prerelease][+build]``.

    Args:
        text: String to validate.

    Returns:
        ``True`` if *text* is valid SemVer.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> is_valid_semver("1.2.3-alpha.1+build.42")
        True

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text.strip()

    # Split off +build metadata
    if "+" in s:
        s, build = s.split("+", 1)

        if not build:
            return False

    # Split off -prerelease
    if "-" in s:
        idx = s.index("-")
        pre = s[idx + 1:]
        s = s[:idx]

        if not pre:
            return False

    parts = s.split(".")

    if len(parts) != 3:
        return False

    for p in parts:

        if not p.isdigit():
            return False

        # No leading zeros on numeric identifiers (except "0")
        if len(p) > 1 and p[0] == "0":
            return False

    return True


def is_valid_mac_address(text: str) -> bool:
    """Validate a MAC address string.

    Accepts colon, dash, and dot notations:
    ``AA:BB:CC:DD:EE:FF``, ``AA-BB-CC-DD-EE-FF``, ``AABB.CCDD.EEFF``.

    Args:
        text: String to validate.

    Returns:
        ``True`` if *text* is a valid MAC address.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> is_valid_mac_address("00:1A:2B:3C:4D:5E")
        True

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text.strip().upper()
    hex_chars = set("0123456789ABCDEF")

    # Colon or dash format
    for sep in (":", "-"):

        if sep in s:
            parts = s.split(sep)

            if len(parts) != 6:
                return False

            return all(len(p) == 2 and all(c in hex_chars for c in p) for p in parts)

    # Dot format (Cisco): AABB.CCDD.EEFF
    if "." in s:
        parts = s.split(".")

        if len(parts) != 3:
            return False

        return all(len(p) == 4 and all(c in hex_chars for c in p) for p in parts)

    # No separator: 12 hex chars
    if len(s) == 12 and all(c in hex_chars for c in s):
        return True

    return False


def is_valid_base64(text: str) -> bool:
    """Check whether a string is valid Base64 encoding.

    Validates the character set (A-Za-z0-9+/=) and correct padding.

    Args:
        text: String to validate.

    Returns:
        ``True`` if *text* is valid Base64.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> is_valid_base64("SGVsbG8gV29ybGQ=")
        True

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    s = text.strip()

    if not s:
        return False

    # Length must be a multiple of 4
    if len(s) % 4 != 0:
        return False

    b64_chars = set(
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    )

    # Check padding
    pad = s.count("=")

    if pad > 2:
        return False

    if pad > 0 and not s.endswith("=" * pad):
        return False

    body = s.rstrip("=")

    return all(c in b64_chars for c in body)


def is_valid_regex(pattern: str) -> bool:
    """Checks whether a string is a syntactically valid regular expression.

    Args:
        pattern: The regex pattern string to validate.

    Returns:
        ``True`` if the pattern compiles without error.

    Raises:
        TypeError: If pattern is not a string.

    Example:
        >>> is_valid_regex(r"\\d{3}-\\d{4}")
        True
        >>> is_valid_regex("[unclosed")
        False

    Complexity: O(n)
    """
    if not isinstance(pattern, str):
        raise TypeError("pattern must be a string")

    try:
        re.compile(pattern)
        return True
    except re.error:
        return False


def is_valid_mime_type(text: str) -> bool:
    """Validates whether a string matches the MIME type format.

    Checks for the standard ``type/subtype`` structure (e.g.
    ``text/html``, ``application/json``).

    Args:
        text: The string to validate.

    Returns:
        ``True`` if the string is a valid MIME type format.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> is_valid_mime_type("application/json")
        True
        >>> is_valid_mime_type("not-a-mime")
        False

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return bool(re.match(
        r"^(application|audio|font|image|message|model|multipart|text|video)"
        r"/[a-zA-Z0-9][a-zA-Z0-9!#$&\-^_.+]*$",
        text.strip(),
    ))


def is_valid_iban(text: str) -> bool:
    """Validates an International Bank Account Number (IBAN).

    Description:
        Checks both the structural format (2 letter country code, 2 check
        digits, and up to 30 alphanumeric BBAN characters) and the MOD-97
        check-digit integrity defined by ISO 13616.

    Args:
        text: The IBAN string to validate.

    Returns:
        True if the IBAN is structurally valid and passes MOD-97 check.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_iban("GB29 NWBK 6016 1331 9268 19")
        True
        >>> is_valid_iban("GB29 NWBK 6016 1331 9268 18")
        False

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.replace(" ", "").replace("-", "").upper()

    if not re.match(r"^[A-Z]{2}\d{2}[A-Z0-9]{4,30}$", cleaned):
        return False

    rearranged = cleaned[4:] + cleaned[:4]
    numeric = "".join(str(int(c, 36)) for c in rearranged)

    return int(numeric) % 97 == 1


def is_valid_isbn(text: str) -> bool:
    """Validates an ISBN-10 or ISBN-13 string.

    Description:
        Strips hyphens/spaces and validates the check digit using the
        appropriate algorithm (modular arithmetic for ISBN-10 and weighted
        sum modulo 10 for ISBN-13).

    Args:
        text: The ISBN string to validate.

    Returns:
        True if the ISBN is valid.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_isbn("978-3-16-148410-0")
        True
        >>> is_valid_isbn("0-306-40615-2")
        True

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.replace("-", "").replace(" ", "")

    if len(cleaned) == 10:
        if not re.match(r"^\d{9}[\dXx]$", cleaned):
            return False

        total = sum(
            (10 if c in "Xx" else int(c)) * (10 - i)
            for i, c in enumerate(cleaned)
        )

        return total % 11 == 0

    if len(cleaned) == 13:
        if not cleaned.isdigit():
            return False

        total = sum(
            int(c) * (1 if i % 2 == 0 else 3)
            for i, c in enumerate(cleaned)
        )

        return total % 10 == 0

    return False


def is_valid_luhn(text: str) -> bool:
    """Validates a numeric string using the Luhn (mod-10) algorithm.

    Description:
        Implements the standard Luhn algorithm used for credit card
        numbers, IMEI codes, and other identifiers.

    Args:
        text: The numeric string to validate.

    Returns:
        True if the string passes the Luhn check.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_luhn("4539148803436467")
        True
        >>> is_valid_luhn("1234567890")
        False

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.replace(" ", "").replace("-", "")

    if not cleaned.isdigit() or len(cleaned) < 2:
        return False

    digits = [int(d) for d in cleaned]
    digits.reverse()

    total = 0

    for i, d in enumerate(digits):

        if i % 2 == 1:
            d *= 2

            if d > 9:
                d -= 9

        total += d

    return total % 10 == 0


def is_valid_ean(text: str) -> bool:
    """Validates an EAN-8 or EAN-13 barcode number.

    Description:
        Checks the length (8 or 13 digits) and the weighted-sum check
        digit used in European Article Numbers.

    Args:
        text: The EAN string to validate.

    Returns:
        True if the EAN is valid.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_ean("4006381333931")
        True
        >>> is_valid_ean("96385074")
        True

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.replace(" ", "").replace("-", "")

    if len(cleaned) not in (8, 13) or not cleaned.isdigit():
        return False

    # EAN-8 starts with weight 3; EAN-13 starts with weight 1
    weights = [1, 3] if len(cleaned) % 2 == 1 else [3, 1]

    total = sum(
        int(c) * weights[i % 2]
        for i, c in enumerate(cleaned)
    )

    return total % 10 == 0


def is_valid_swift_bic(text: str) -> bool:
    """Validates a SWIFT/BIC (Business Identifier Code) string.

    Description:
        Checks that the code conforms to the ISO 9362 format:
        4 letters (bank) + 2 letters (country) + 2 alphanumeric
        (location) + optional 3 alphanumeric (branch or ``XXX``).

    Args:
        text: The SWIFT/BIC code to validate.

    Returns:
        True if the code matches the SWIFT/BIC format.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_swift_bic("DEUTDEFF")
        True
        >>> is_valid_swift_bic("DEUTDEFF500")
        True

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.strip().upper()

    return bool(re.match(r"^[A-Z]{4}[A-Z]{2}[A-Z0-9]{2}([A-Z0-9]{3})?$", cleaned))


def is_valid_isin(text: str) -> bool:
    """Validate an ISIN (International Securities Identification Number).

    Description:
        An ISIN consists of a 2-letter country code, a 9-character
        alphanumeric national identifier, and a single check digit.
        Validation converts letters to numbers (A=10..Z=35), concatenates
        the digit string, and applies the Luhn algorithm.

    Args:
        text: The ISIN string to validate.

    Returns:
        True if the ISIN is valid.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_isin("US0378331005")
        True
        >>> is_valid_isin("US0378331006")
        False

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.strip().upper()

    if len(cleaned) != 12:
        return False

    if not re.match(r"^[A-Z]{2}[A-Z0-9]{9}[0-9]$", cleaned):
        return False

    # Convert letters to numbers: A=10, B=11, ..., Z=35
    digit_str = ""

    for c in cleaned:

        if c.isdigit():
            digit_str += c
        else:
            digit_str += str(ord(c) - ord("A") + 10)

    # Apply Luhn algorithm on the resulting digit string
    total = 0
    reverse_digits = digit_str[::-1]

    for i, d in enumerate(reverse_digits):
        n = int(d)

        if i % 2 == 1:
            n *= 2

            if n > 9:
                n -= 9

        total += n

    return total % 10 == 0


def is_valid_cusip(text: str) -> bool:
    """Validate a CUSIP (Committee on Uniform Securities Identification Procedures) code.

    Description:
        A CUSIP is 9 characters: 6 alphanumeric (issuer) + 2 alphanumeric
        (issue) + 1 check digit.  The check digit is computed via a
        weighted Luhn-like algorithm where odd-position digits are
        multiplied by 1 and even-position digits by 2 (after letter-to-
        number conversion).

    Args:
        text: The CUSIP code to validate.

    Returns:
        True if the CUSIP is valid.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_cusip("037833100")
        True
        >>> is_valid_cusip("037833101")
        False

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.strip().upper()

    if len(cleaned) != 9:
        return False

    if not re.match(r"^[A-Z0-9*@#]{9}$", cleaned):
        return False

    total = 0

    for i in range(8):
        c = cleaned[i]

        if c.isdigit():
            v = int(c)
        elif c == "*":
            v = 36
        elif c == "@":
            v = 37
        elif c == "#":
            v = 38
        else:
            v = ord(c) - ord("A") + 10

        if i % 2 == 1:
            v *= 2

        total += v // 10 + v % 10

    check = (10 - (total % 10)) % 10

    return check == int(cleaned[8])


def is_valid_sedol(text: str) -> bool:
    """Validate a SEDOL (Stock Exchange Daily Official List) code.

    Description:
        A SEDOL is 7 characters: 6 alphanumeric characters (no vowels)
        followed by a weighted check digit.  Weights are [1, 3, 1, 7, 3, 9].

    Args:
        text: The SEDOL code to validate.

    Returns:
        True if the SEDOL is valid.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_sedol("0263494")
        True

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.strip().upper()

    if len(cleaned) != 7:
        return False

    # SEDOL characters: digits and consonants only
    if not re.match(r"^[0-9BCDFGHJKLMNPQRSTVWXYZ]{7}$", cleaned):
        return False

    weights = [1, 3, 1, 7, 3, 9]
    total = 0

    for i in range(6):
        c = cleaned[i]

        if c.isdigit():
            v = int(c)
        else:
            v = ord(c) - ord("A") + 10

        total += v * weights[i]

    check = (10 - (total % 10)) % 10

    return check == int(cleaned[6])


def is_valid_vin(text: str) -> bool:
    """Validate a VIN (Vehicle Identification Number).

    Description:
        A VIN is 17 characters (letters and digits, excluding I, O, Q).
        Position 9 is a check digit computed by transliterating each
        character to a value, multiplying by positional weights, summing,
        and taking mod 11 (10 → 'X').

    Args:
        text: The VIN to validate.

    Returns:
        True if the VIN is valid.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_vin("1M8GDM9AXKP042788")
        True

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.strip().upper()

    if len(cleaned) != 17:
        return False

    # I, O, Q are not allowed in VINs
    if re.search(r"[IOQ]", cleaned):
        return False

    transliteration = {
        "A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
        "J": 1, "K": 2, "L": 3, "M": 4, "N": 5, "P": 7, "R": 9,
        "S": 2, "T": 3, "U": 4, "V": 5, "W": 6, "X": 7, "Y": 8, "Z": 9,
    }
    weights = [8, 7, 6, 5, 4, 3, 2, 10, 0, 9, 8, 7, 6, 5, 4, 3, 2]

    total = 0

    for i, c in enumerate(cleaned):

        if c.isdigit():
            v = int(c)
        else:
            v = transliteration.get(c, 0)

        total += v * weights[i]

    remainder = total % 11
    expected = "X" if remainder == 10 else str(remainder)

    return cleaned[8] == expected


def is_valid_issn(text: str) -> bool:
    """Validate an ISSN (International Standard Serial Number).

    Description:
        An ISSN is 8 digits (with optional hyphen after digit 4).
        The check digit (last char, may be 'X' for 10) is validated
        using a weighted mod-11 algorithm with weights 8..2.

    Args:
        text: The ISSN to validate.

    Returns:
        True if the ISSN is valid.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_issn("0378-5955")
        True
        >>> is_valid_issn("0000-0019")
        True

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    cleaned = text.strip().upper().replace("-", "")

    if len(cleaned) != 8:
        return False

    if not re.match(r"^[0-9]{7}[0-9X]$", cleaned):
        return False

    total = 0

    for i in range(7):
        total += int(cleaned[i]) * (8 - i)

    check_val = 10 if cleaned[7] == "X" else int(cleaned[7])
    total += check_val

    return total % 11 == 0


def is_valid_e164_phone(text: str) -> bool:
    """Validate an E.164 international phone number.

    Description:
        E.164 format: ``+`` followed by 1 to 15 digits, no spaces or
        dashes.  This is the ITU-T standard used in SIP, SMS, and
        international dialling.

    Args:
        text: The phone number string to validate.

    Returns:
        True if the string matches E.164 format.

    Raises:
        TypeError: If *text* is not a string.

    Usage Example:
        >>> is_valid_e164_phone("+34612345678")
        True
        >>> is_valid_e164_phone("612345678")
        False
        >>> is_valid_e164_phone("+1234567890123456")
        False

    Complexity: O(1)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return bool(re.match(r"^\+[1-9]\d{1,14}$", text.strip()))


def check_password_strength(password: str) -> int:
    """Evaluate password strength on a 0–100 score scale.

    Description:
        The score is computed from: length contribution (up to 40 pts),
        character diversity — uppercase, lowercase, digits, special
        characters (up to 40 pts) — and a bonus for entropy above
        3.0 bits/char (up to 20 pts).  The result is clamped to [0, 100].

    Args:
        password: The password string to evaluate.

    Returns:
        Strength score as an integer in [0, 100].

    Raises:
        TypeError: If *password* is not a string.

    Usage Example:
        >>> check_password_strength("abc")
        18
        >>> check_password_strength("C0mpl3x!Pass#2026")
        100

    Complexity: O(n) where n is the password length.
    """
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    if not password:
        return 0

    length = len(password)
    score = 0

    # Length contribution (up to 40 pts)
    score += min(40, length * 4)

    # Character diversity (up to 10 pts each category)
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(not c.isalnum() for c in password)

    score += 10 * sum([has_upper, has_lower, has_digit, has_special])

    # Entropy bonus (up to 20 pts)
    freq: dict = {}

    for ch in password:
        freq[ch] = freq.get(ch, 0) + 1

    entropy = 0.0

    for count in freq.values():
        p = count / length
        entropy -= p * math.log2(p)

    if entropy > 3.0:
        score += 20
    elif entropy > 2.0:
        score += 10

    return min(100, max(0, score))


# ---------------------------------------------------------------------------
# Phase 21 – Batch 34: String Evaluations (1 of 2)
# ---------------------------------------------------------------------------

def is_isogram(text: str) -> bool:
    """Check if *text* is an isogram (no repeating letters, case-insensitive).

    Non-alphabetic characters are ignored.

    Args:
        text: Source string.

    Returns:
        True if isogram.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> is_isogram('subdermatoglyphic')
        True

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    seen: set = set()
    for ch in text.lower():
        if ch.isalpha():
            if ch in seen:
                return False
            seen.add(ch)
    return True


def is_heterogram(text: str) -> bool:
    """Check if *text* has no repeated characters at all (including spaces).

    Args:
        text: Source string.

    Returns:
        True if heterogram.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> is_heterogram('abcde')
        True

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    return len(set(text)) == len(text)


def is_tautogram(text: str) -> bool:
    """Check if every word in *text* starts with the same letter (case-insensitive).

    Args:
        text: Source string (whitespace-delimited words).

    Returns:
        True if tautogram.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> is_tautogram('Peter Piper picked peppers')
        True

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    words = text.split()
    if not words:
        return True
    first = words[0][0].lower()
    return all(w[0].lower() == first for w in words if w)


def is_lipogram(text: str, letter: str) -> bool:
    """Check if *text* avoids *letter* entirely (case-insensitive).

    Args:
        text: Source string.
        letter: Single letter to check absence of.

    Returns:
        True if letter is absent.

    Raises:
        TypeError: If arguments are not strings.
        ValueError: If letter is not a single alphabetic character.

    Usage Example:
        >>> is_lipogram('The quick brown fox jumps over the lazy dog', 'z')
        False

    Complexity: O(n)
    """
    if not isinstance(text, str) or not isinstance(letter, str):
        raise TypeError("Both arguments must be strings.")
    if len(letter) != 1 or not letter.isalpha():
        raise ValueError("letter must be a single alphabetic character.")
    return letter.lower() not in text.lower()


def flesch_reading_ease(text: str) -> float:
    """Estimate the Flesch Reading Ease score for English text.

    Score ranges typically 0-100 (higher = easier to read).
    Uses a simple heuristic syllable counter.

    Args:
        text: English prose text.

    Returns:
        Flesch Reading Ease score.

    Raises:
        TypeError: If text is not a string.
        ValueError: If text has no words.

    Usage Example:
        >>> round(flesch_reading_ease('The cat sat on the mat.'), 1)
        116.1

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    import re as _re

    sentences = _re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        raise ValueError("text must contain at least one sentence.")

    words = text.split()
    if not words:
        raise ValueError("text must contain at least one word.")

    num_sentences = len(sentences)
    num_words = len(words)

    def _count_syllables(word: str) -> int:
        word = word.lower().strip(".,!?;:'\"")
        if not word:
            return 1
        vowels = "aeiouy"
        count = 0
        prev_vowel = False
        for ch in word:
            if ch in vowels:
                if not prev_vowel:
                    count += 1
                prev_vowel = True
            else:
                prev_vowel = False
        if word.endswith("e") and count > 1:
            count -= 1
        return max(1, count)

    total_syllables = sum(_count_syllables(w) for w in words)

    return 206.835 - 1.015 * (num_words / num_sentences) - 84.6 * (total_syllables / num_words)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 35: String Evaluations (2 of 2)
# ---------------------------------------------------------------------------

def gunning_fog_index(text: str) -> float:
    """Estimate the Gunning Fog readability index for English text.

    Higher values indicate harder text. A score of ~7–8 is considered
    easy reading; 12+ is considered hard.

    Args:
        text: English prose text.

    Returns:
        Gunning Fog index.

    Raises:
        TypeError: If text is not a string.
        ValueError: If text has no sentences.

    Usage Example:
        >>> round(gunning_fog_index('The cat sat on the mat.'), 1)
        2.4

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    import re as _re

    sentences = _re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        raise ValueError("text must contain at least one sentence.")

    words = text.split()
    if not words:
        raise ValueError("text must contain at least one word.")

    def _syllable_count(word: str) -> int:
        word = word.lower().strip(".,!?;:'\"")
        if not word:
            return 1
        vowels = "aeiouy"
        count = 0
        prev_vowel = False
        for ch in word:
            if ch in vowels:
                if not prev_vowel:
                    count += 1
                prev_vowel = True
            else:
                prev_vowel = False
        if word.endswith("e") and count > 1:
            count -= 1
        return max(1, count)

    complex_words = sum(1 for w in words if _syllable_count(w) >= 3)
    num_words = len(words)
    num_sentences = len(sentences)

    return 0.4 * ((num_words / num_sentences) + 100.0 * (complex_words / num_words))


def automated_readability_index(text: str) -> float:
    """Compute the Automated Readability Index (ARI) for English text.

    Returns an approximate US grade level needed to understand the text.

    Args:
        text: English prose text.

    Returns:
        ARI score (approximate US grade level).

    Raises:
        TypeError: If text is not a string.
        ValueError: If text has no sentences.

    Usage Example:
        >>> round(automated_readability_index('The cat sat on the mat.'), 1)
        -5.1

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    import re as _re

    sentences = _re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        raise ValueError("text must contain at least one sentence.")

    words = text.split()
    if not words:
        raise ValueError("text must contain at least one word.")

    num_chars = sum(1 for ch in text if ch.isalnum())
    num_words = len(words)
    num_sentences = len(sentences)

    return 4.71 * (num_chars / num_words) + 0.5 * (num_words / num_sentences) - 21.43


def coleman_liau_index(text: str) -> float:
    """Compute the Coleman–Liau readability index for English text.

    Returns an approximate US grade level.

    Args:
        text: English prose text.

    Returns:
        Coleman–Liau index.

    Raises:
        TypeError: If text is not a string.
        ValueError: If text has no words.

    Usage Example:
        >>> round(coleman_liau_index('The cat sat on the mat.'), 1)
        -4.1

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    import re as _re

    sentences = _re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        raise ValueError("text must contain at least one sentence.")

    words = text.split()
    if not words:
        raise ValueError("text must contain at least one word.")

    num_letters = sum(1 for ch in text if ch.isalpha())
    num_words = len(words)
    num_sentences = len(sentences)

    letters_per_100 = (num_letters / num_words) * 100.0  # letters per 100 words
    s = (num_sentences / num_words) * 100.0  # sentences per 100 words
    return 0.0588 * letters_per_100 - 0.296 * s - 15.8


def smog_index(text: str) -> float:
    """Compute the SMOG readability index for English text.

    Designed for texts with ≥ 30 sentences but works as an estimate
    on shorter texts.

    Args:
        text: English prose text.

    Returns:
        SMOG index.

    Raises:
        TypeError: If text is not a string.
        ValueError: If text has no sentences.

    Usage Example:
        >>> round(smog_index('The cat sat on the mat.'), 1)
        3.0

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    import re as _re
    import math as _math

    sentences = _re.split(r'[.!?]+', text)
    sentences = [s.strip() for s in sentences if s.strip()]
    if not sentences:
        raise ValueError("text must contain at least one sentence.")

    words = text.split()

    def _syllable_count(word: str) -> int:
        word = word.lower().strip(".,!?;:'\"")
        if not word:
            return 1
        vowels = "aeiouy"
        count = 0
        prev_vowel = False
        for ch in word:
            if ch in vowels:
                if not prev_vowel:
                    count += 1
                prev_vowel = True
            else:
                prev_vowel = False
        if word.endswith("e") and count > 1:
            count -= 1
        return max(1, count)

    polysyllables = sum(1 for w in words if _syllable_count(w) >= 3)
    num_sentences = len(sentences)

    return 3.0 + _math.sqrt(polysyllables * (30.0 / num_sentences))


def avg_word_length(text: str) -> float:
    """Compute the average word length in *text*.

    Args:
        text: Source string.

    Returns:
        Average word length.

    Raises:
        TypeError: If text is not a string.
        ValueError: If text has no words.

    Usage Example:
        >>> avg_word_length('The cat sat')
        3.0

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    words = text.split()
    if not words:
        raise ValueError("text must contain at least one word.")
    return sum(len(w) for w in words) / len(words)

