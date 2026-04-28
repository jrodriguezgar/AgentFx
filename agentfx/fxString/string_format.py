"""String Formatting and Normalization Functions.

This module provides functions for formatting, normalizing, and standardizing
strings according to various conventions and requirements. It includes utilities
for formatting names, addresses, identifiers, and other text data.

Key Features:
- Data masking and anonymization
- Date and number formatting
- Name and company name formatting
- Email, URL, and domain formatting
- String case transformations
- Symbol and space normalization
- Character set filtering
- Legal form parsing
- SQL quoting and escaping

"""

from datetime import datetime
from typing import Optional, Union, Any
import warnings


import os # For path management if not using importlib.resources (less recommended for packages)

import re
import unicodedata


# Pre-compiled regex patterns for optimization
_RE_PARENTHESES = re.compile(r'[\(\[\{][^\)\]\}]*[\)\]\}]')
_RE_PUNCTUATION = re.compile(r'[,.\-_:;/\\\'\"¿?¡!]')
_RE_WHITESPACE = re.compile(r'\s+')

# Pre-compiled patterns for normalize_symbols optimization
_RE_SYMBOLS_NO_SPACE = re.compile(r'\s*([ºª@()\[\]{}<>#/\\|_\-¿?!¡])\s*')
_RE_PUNCTUATION_AFTER_SPACE = re.compile(r'\s*([.,:;])\s*')
_RE_OPERATORS_AROUND_SPACE = re.compile(r'\s*([+=&])\s*')
_RE_CURRENCY_NO_SPACE_BEFORE = re.compile(r'\s*([$€])')

# Pre-compiled patterns for string filtering functions
_RE_ALPHANUMERIC = re.compile(r'[^a-zA-Z0-9]')
_RE_ALPHABETIC = re.compile(r'[^a-zA-Z]')
_RE_NUMBERS = re.compile(r'-?\d+\.?\d*')
_RE_NUMBERS_AND_DOTS = re.compile(r'[0-9.]')

# Pre-compiled patterns for format_email_address and format_url
_RE_EMAIL_VALID_CHARS = re.compile(r'[^a-zA-Z0-9.!#$%&\'*+/=?^_`{|}~@-]')


def mask_data(
    input_string: str,
    mask_char: str = "*",
    num_chars: Optional[int] = None,
    position: str = "all",
    start_index: int = 0,
    keep_visible: int = 0
) -> str:
    """Mask sensitive data based on various patterns.

    Description:
        Obfuscates parts of a string to protect sensitive information like 
        passwords, credit card numbers, or IDs. Supports multiple masking 
        strategies (start, end, full, or specific range).

    Args:
        input_string (str): The string to be masked.
        mask_char (str): Character used for masking. Defaults to '*'.
        num_chars (Optional[int]): Total characters to obfuscate. If None, 
                                    calculates based on 'position' and 'keep_visible'.
        position (str): 'all' (entire string), 'start' (mask prefix), 
                        'end' (mask suffix), or 'index' (mask range).
        start_index (int): Offset to start masking (only if position='index').
        keep_visible (int): Characters to preserve (unmasked) at the end 
                            (if position='start') or start (if position='end').

    Returns:
        str: The obfuscated string.

    Complexity: 
        O(N) where N is the length of input_string.

    Examples:
        >>> mask_data("123456789", position="start", num_chars=4)
        '****56789'
        >>> mask_data("123456789", position="end", keep_visible=3)
        '123******'
        >>> mask_data("John Doe", position="index", start_index=2, num_chars=3)
        'Jo***Doe'
        >>> mask_data("password", mask_char="#")
        '########'
    """
    if not input_string:
        return ""
    
    length = len(input_string)
    
    if position == "all":
        count = num_chars if num_chars is not None else length
        return mask_char * min(count, length)
    
    if position == "start":
        count = num_chars if num_chars is not None else (length - keep_visible)
        count = max(0, min(count, length))
        return (mask_char * count) + input_string[count:]
    
    if position == "end":
        count = num_chars if num_chars is not None else (length - keep_visible)
        count = max(0, min(count, length))
        return input_string[:length - count] + (mask_char * count)
    
    if position == "index":
        count = num_chars if num_chars is not None else (length - start_index)
        if start_index < 0 or start_index >= length:
            return input_string
        
        end_idx = min(start_index + count, length)
        return (
            input_string[:start_index] + 
            (mask_char * (end_idx - start_index)) + 
            input_string[end_idx:]
        )
    
    return input_string


def normalize_text(text: str) -> str:
    """
    Normalizes text by removing accents and converting to lowercase.

    This function strips diacritical marks (e.g., 'á' becomes 'a') to ensure
    consistent comparison keys for spellchecking algorithms.

    Args:
        text (str): The input string to normalize.

    Returns:
        str: The normalized, lowercase ASCII string.

    Example:
        >>> normalize_text("Julián")
        'julian'
    """
    if not text:
        return ""

    # Normalize unicode characters to NFD form
    normalized = unicodedata.normalize('NFD', text)

    # Filter out non-spacing mark characters and encode to ASCII
    return "".join(
        char for char in normalized if unicodedata.category(char) != 'Mn'
    ).lower()
_RE_URL_VALID_CHARS = re.compile(r'[^\w\-\.~:/?#\[\]@!$&\'()*+,;=%\s]')

# Pre-compiled patterns for format_internet_domain
_RE_DOMAIN_VALID_CHARS = re.compile(r'[^a-z0-9\-.]')
_RE_MULTIPLE_HYPHENS = re.compile(r'\-+')
_RE_MULTIPLE_DOTS = re.compile(r'\.+')

# Pre-compiled pattern for capitalize_string
_RE_WORD_DELIMITERS = re.compile(r'([\s/\-])')

# Pre-computed translation tables for format_name and format_fullname
# Creating these once at module level avoids repeated str.maketrans() calls
_TRANSLATION_TABLE_NAMES = str.maketrans({
    "´": "'", "`": "'",
    "{": " ", "}": " ", "[": " ", "]": " ", 
    "*": " ", '"': " ", "_": " ", "·": " ",
    ",": " ", ";": " ", "|": " ", "\\": " ", 
    "¬": " ", "‰": " ", "½": " ", "ƒ": " ",
    "Ž": " ", "œ": " ", "‹": " ", "Š": " ", 
    "˜": " ", "‡": " ", "†": " ", "¥": " ",
    "ð": " ", "§": " ", ".": " "
})

# Pre-defined set of titles to remove from person names (defined once at module level)
# Using frozenset for O(1) lookup performance and immutability:
    # 'DR', 'DRA', 'SR', 'SRA', 'SRTA', 'D', 'DA', 'DON', 'DOÑA',
    # 'MR', 'MRS', 'MS', 'MISS', 'ING', 'LIC', 'ARQ', 'C',
    # 'DE', 'DEL', 'LA', 'LAS', 'LOS', 'EL', 'Y'
_TITLES_TO_REMOVE = frozenset({
    'DR', 'DRA', 'SR', 'SRA', 'SRTA', 'D', 'DA', 'DON', 'DOÑA',
    'MR', 'MRS', 'MS', 'MISS', 'ING', 'LIC', 'ARQ', 'C'
})

try:
    from agentfx.fxString import string_operations as fxStrOp
except ImportError:
    from . import string_operations as fxStrOp


#Load legal forms data (executed once when the module is imported) ---
# LEGAL_FORMS_SET will contain all legal forms for efficient lookups.
# A 'set' is used for average O(1) lookups.
LEGAL_FORMS_SET = set()
# Optional: LEGAL_FORMS_BY_COUNTRY if you need to filter by country.
LEGAL_FORMS_BY_COUNTRY = {}

def _load_legal_forms_data():
    """
    Loads legal forms from the company_legalforms.txt file
    into LEGAL_FORMS_SET and LEGAL_FORMS_BY_COUNTRY.
    This function is called automatically once when the module is imported.
    """
    try:
        # Load data file from the local data directory
        # Get the directory where this module is located
        module_dir = os.path.dirname(os.path.abspath(__file__))
        data_file = os.path.join(module_dir, 'data', 'company_legalforms.txt')
        
        if not os.path.exists(data_file):
            warnings.warn(
                f"Legal forms data file not found at {data_file}",
                stacklevel=2,
            )
            return
        
        file_path = data_file
        
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # Why: Ignore empty lines or comments to ensure only valid data is processed.
                if not line or line.startswith('#'):
                    continue
                
                # Assume fields are separated by tabs.
                parts = line.split('\t') 
                if len(parts) == 2:
                    code_country, short_legal_form = parts[0].strip(), parts[1].strip()
                    
                    # Store the legal form in lowercase for case-insensitive searches
                    # and remove common trailing punctuation to normalize (e.g., "Inc." vs "Inc").
                    # Why: Normalizing the forms once during loading prevents repeated normalization
                    # during lookups and ensures consistent matching.
                    normalized_form = short_legal_form.lower().rstrip('.,')
                    LEGAL_FORMS_SET.add(normalized_form)
                    
                    # Load by country as well (if needed)
                    # Why: This structure allows for future enhancements where country-specific legal forms might be required.
                    if code_country not in LEGAL_FORMS_BY_COUNTRY:
                        LEGAL_FORMS_BY_COUNTRY[code_country] = set()
                    LEGAL_FORMS_BY_COUNTRY[code_country].add(normalized_form)
                    
    except FileNotFoundError:
        warnings.warn(
            f"Legal forms file '{file_path}' not found. "
            "Parsing functionality might be incomplete.",
            stacklevel=2,
        )
    except Exception as e:
        warnings.warn(
            f"Unexpected error loading legal forms: {e}",
            stacklevel=2,
        )

# Call the data loading function **once** when the module is imported.
# Why: This ensures the data is available immediately upon module import
# and avoids repeated loading, which would be inefficient.
_load_legal_forms_data()


# Constants should be in uppercase with underscores.
# Using a frozenset for faster 'in' lookups compared to a list.
EXCLUDED_COMPANY_TYPES = frozenset([
    'ORGANO DE LA ADMINISTRACION', 'ENTIDAD NO LUCRATIVA', 'CORPORACION LOCAL',
    'SUCURSAL EN ESPAÑA', 'PARTIDO POLITICO', 'ORGANISMO AUTONOMO',
    'ENTIDAD NO RESIDENTE', 'ASOCIACION', 'FUNDACION', 'CAJA', 'MUTUA', 'FONDO'
])

# Define company types that are abbreviated with a single dot.
SHORT_TYPES_WITH_DOTS = frozenset(['LTD', 'INC', 'CO'])


def sql_quote(sql_string: str, db_type: str) -> str:
    """Escapes single quotes in a SQL string based on the database type.

    This function prevents SQL injection by properly escaping single quotes
    within a given SQL string. Different database systems handle quote
    escaping differently (e.g., SQLite and Oracle use two single quotes,
    while others might use a backslash).

    Args:
        sql_string (str): The SQL string that needs to have its quotes escaped.
        db_type (str): The type of the database ('sqlite', 'oracle', or others).

    Returns:
        str: The SQL string with single quotes properly escaped for the specified database type.

    Raises:
        ValueError: If db_type is not a string.

    Example:
        >>> sql_quote("SELECT * FROM users WHERE name = 'O''Reilly'", "sqlite")
        "SELECT * FROM users WHERE name = ''O''''Reilly''"
        >>> sql_quote("INSERT INTO products (name) VALUES ('Laptop')", "postgresql")
        "INSERT INTO products (name) VALUES ('\'Laptop'\'')"
    """
    if not isinstance(db_type, str):
        # We raise a ValueError because the db_type is expected to be a string
        # for proper conditional logic.
        raise ValueError("The 'db_type' argument must be a string.")

    # Convert db_type to lowercase to ensure case-insensitive comparison.
    # This prevents issues where 'SQLite' or 'ORACLE' might not be matched.
    normalized_db_type = db_type.lower()

    if normalized_db_type in ('sqlite', 'oracle'):
        # SQLite and Oracle use two single quotes to escape a single quote.
        return sql_string.replace("'", "''")
    else:
        # Most other SQL databases (e.g., PostgreSQL, MySQL) use a backslash
        # to escape single quotes.
        return sql_string.replace("'", "\\'")

    # Cost: O(n) where n is the length of sql_string due to the string replacement operation.

def format_date(date_input: Union[str, datetime], output_format: str = None,
                locale: str = "en_US") -> str:
    """
    Formats a date input (string or datetime object) into a specified output format,
    considering the given locale for parsing string inputs and default output format.

    This function accepts either a string representing a date or a datetime object.
    If the input is a string, it attempts to parse it using various common date formats
    relevant to the specified locale. It then formats the resulting datetime object
    into the desired output format.

    Args:
        date_input (Union[str, datetime]): The input date, which can be a string
                                            or a datetime object, to be formatted.
        output_format (str, optional): The desired output format for the date.
                                       If None, it defaults to "%Y-%m-%d" for "en_US"
                                       and "%d/%m/%Y" for "es_ES".
        locale (str, optional): The locale to use for parsing string dates and
                                default output format. Supported locales are "en_US"
                                (Anglo-Saxon) and "es_ES" (European).
                                Defaults to "en_US".

    Returns:
        str: The formatted date string.

    Raises:
        ValueError: If the input date string cannot be parsed into a valid date
                    for the given locale, or if an unsupported locale is provided.
        TypeError: If the 'date_input' type is unsupported.
    """
    # Determine the default output format based on locale if not explicitly provided
    if output_format is None:
        if locale == "en_US":
            default_output_format = "%Y-%m-%d"
        elif locale == "es_ES":
            default_output_format = "%d/%m/%Y"
        else:
            raise ValueError(f"Unsupported locale: '{locale}'. "
                             "Supported locales are 'en_US' and 'es_ES'.")
    else:
        default_output_format = output_format # Use the provided format if specified

    if isinstance(date_input, datetime):
        parsed_date = date_input
    elif isinstance(date_input, str):
        # Define common input date formats based on the specified locale.
        if locale == "en_US":
            input_formats = [
                "%Y-%m-%d",            # ISO-MM-DD (Universal)
                "%m/%d/%Y",            # MM/DD/YYYY
                "%m-%d-%Y",            # MM-DD-YYYY
                "%b %d, %Y",           # Mon DD, YYYY (e.g., Oct 26, 2023)
                "%B %d, %Y",           # Month DD, YYYY (e.g., October 26, 2023)
                "%Y%m%d",              # YYYYMMDD
            ]
        elif locale == "es_ES":
            input_formats = [
                "%Y-%m-%d",            # ISO-MM-DD (Universal, still useful for parsing)
                "%d/%m/%Y",            # DD/MM/YYYY (Common European default)
                "%d-%m-%Y",            # DD-MM-YYYY
                "%d/%m/%y",            # DD/MM/YY (e.g., 26/10/23)
                "%b %d, %Y",           # Mon DD, YYYY (for international compatibility)
                "%B %d, %Y",           # Month DD, YYYY
                "%Y%m%d",              # YYYYMMDD
            ]
        else:
            raise ValueError(f"Unsupported locale: '{locale}'. "
                             "Supported locales are 'en_US' and 'es_ES'.")

        parsed_date = None
        for fmt in input_formats:
            try:
                parsed_date = datetime.strptime(date_input, fmt)
                break
            except ValueError:
                continue

        if parsed_date is None:
            raise ValueError(f"Unable to parse date string: '{date_input}' for locale '{locale}'. "
                             "Please ensure it's a valid date format for the specified locale.")
    else:
        raise TypeError("Unsupported type for 'date_input'. Must be a string or a datetime object.")

    return parsed_date.strftime(default_output_format)


def format_number(number_input: Union[int, float, str], decimal_places: int = 2,
                  locale: str = "en_US", currency_symbol: str = "") -> str:
    """
    Formats a numeric input (int, float, or string) according to specified locale conventions.

    This function provides flexible formatting for numbers, including control over
    decimal places, thousands separators, and optional currency symbols, based
    on the chosen locale (e.g., "en_US" for Anglo-Saxon, "es_ES" for European).

    Args:
        number_input (Union[int, float, str]): The input number, which can be an
                                                integer, float, or a string representation
                                                of a number.
        decimal_places (int, optional): The number of decimal places to include.
                                        Defaults to 2.
        locale (str, optional): The locale for formatting conventions.
                                Supports "en_US" (Anglo-Saxon: comma for thousands, dot for decimals)
                                and "es_ES" (European: dot for thousands, comma for decimals).
                                Defaults to "en_US".
        currency_symbol (str, optional): An optional string to prepend as a currency symbol.
                                         Defaults to "".

    Returns:
        str: The formatted number as a string.

    Raises:
        ValueError: If the input cannot be converted into a valid number or an unsupported locale is provided.
        TypeError: If the 'decimal_places' argument is not an integer.
    """
    if not isinstance(decimal_places, int):
        raise TypeError("'decimal_places' must be an integer.")

    numeric_value: Union[int, float]

    if isinstance(number_input, (int, float)):
        numeric_value = number_input
    elif isinstance(number_input, str):
        try:
            if locale == "es_ES":
                temp_string = number_input.replace(".", "").replace(",", ".")
                numeric_value = float(temp_string)
            else:
                numeric_value = float(number_input)
        except ValueError:
            raise ValueError(f"Unable to convert '{number_input}' to a valid number. "
                             "Please ensure it's a numeric string.")
    else:
        raise TypeError("Unsupported type for 'number_input'. Must be an int, float, or string.")

    formatted_number_str = f"{numeric_value:,.{decimal_places}f}"

    if locale == "es_ES":
        temp_formatted = formatted_number_str.replace(",", "TEMP_COMMA").replace(".", ",").replace("TEMP_COMMA", ".")
        formatted_number_str = temp_formatted

    if currency_symbol:
        return f"{currency_symbol}{formatted_number_str}"
    return formatted_number_str


def format_number_with_negative_style(
    number_input: Union[int, float, str],
    decimal_places: int = 2,
    locale: str = "en_US",
    currency_symbol: str = "",
    negative_style: str = "minus"
) -> str:
    """
    Formats a numeric input, handling negative numbers with either a minus sign or parentheses.

    This function leverages the `format_number` function for standard formatting
    (decimal places, locale, currency) and then applies a specific style
    for negative numbers.

    Args:
        number_input (Union[int, float, str]): The number to format.
        decimal_places (int, optional): The number of decimal places. Defaults to 2.
        locale (str, optional): The locale for formatting ("en_US" or "es_ES").
                                Defaults to "en_US".
        currency_symbol (str, optional): An optional currency symbol. Defaults to "".
        negative_style (str, optional): How to display negative numbers.
                                        Accepts "minus" (e.g., -123.45) or
                                        "parentheses" (e.g., (123.45)).
                                        Defaults to "minus".

    Returns:
        str: The formatted number as a string.

    Raises:
        ValueError: If the input cannot be converted to a number, an unsupported
                    locale is provided, or an invalid `negative_style` is used.
        TypeError: If 'decimal_places' is not an integer.

    Example of use:
        >>> format_number_with_negative_style(-12345.678, decimal_places=2, currency_symbol="$", negative_style="parentheses")
        '($12,345.68)'
        >>> format_number_with_negative_style(-987.65, decimal_places=1, locale="es_ES", negative_style="minus")
        '-987,7'
        >>> format_number_with_negative_style(5000, decimal_places=0)
        '5,000'
    """
    if negative_style not in ["minus", "parentheses"]:
        raise ValueError("Invalid 'negative_style'. Must be 'minus' or 'parentheses'.")

    # First, convert the input to a numeric value to check its sign.
    numeric_value: Union[int, float]
    if isinstance(number_input, (int, float)):
        numeric_value = number_input
    elif isinstance(number_input, str):
        try:
            # Handle locale-specific string to float conversion if the number is negative
            # so the sign is correctly interpreted before passing to format_number
            if locale == "es_ES":
                temp_string = number_input.replace(".", "").replace(",", ".")
                numeric_value = float(temp_string)
            else:
                numeric_value = float(number_input)
        except ValueError:
            raise ValueError(f"Unable to convert '{number_input}' to a valid number. "
                             "Please ensure it's a numeric string.")
    else:
        raise TypeError("Unsupported type for 'number_input'. Must be an int, float, or string.")

    # If the number is negative and parentheses style is requested
    if numeric_value < 0 and negative_style == "parentheses":
        # Format the absolute value of the number
        formatted_abs_value = format_number(
            abs(numeric_value),
            decimal_places=decimal_places,
            locale=locale,
            currency_symbol=currency_symbol
        )
        return f"({formatted_abs_value})"
    else:
        # Otherwise, just use the standard formatting, which handles the minus sign by default
        return format_number(
            numeric_value,
            decimal_places=decimal_places,
            locale=locale,
            currency_symbol=currency_symbol
        )


def autoformat(data_input: Any, locale: str = "en_US") -> str:
    """
    Automatically formats an input value as a date or a number based on its type
    and content, adhering to the specified locale conventions for both parsing
    and default output formats. If unable to format, returns the original input
    as a string.

    This function attempts to interpret the input as a datetime object. If it's
    not a datetime object and appears to be a string, it tries to parse it
    as a date using locale-specific formats. If date parsing fails, it then attempts
    to interpret and format the input as a number (int, float, or numeric string),
    again respecting the locale's number formatting conventions.

    Args:
        data_input (Any): The input data to be auto-formatted. Can be a datetime object,
                          an int, a float, or a string that represents a date or a number.
        locale (str, optional): The locale to use for both date and number formatting.
                                Supported locales are "en_US" (Anglo-Saxon)
                                and "es_ES" (European). Defaults to "en_US".

    Returns:
        str: The automatically formatted string representation of the input,
             or the original input converted to string if formatting fails.

    Raises:
        TypeError: If the input type is fundamentally unsupported.

    Example of use:
        >>> from datetime import datetime

        >>> # Successful formatting
        >>> autoformat("10/26/2023", locale="en_US")
        '2023-10-26'
        >>> autoformat("26/10/2023", locale="es_ES")
        '26/10/2023'
        >>> autoformat(1234567.89, locale="en_US")
        '1,234,567.89'
        >>> autoformat("98.765,43", locale="es_ES")
        '98.765,43'

        >>> # Fallback to original data
        >>> autoformat("not a date or number", locale="en_US")
        'not a date or number'
        >>> autoformat([1, 2, 3], locale="es_ES") # Unsupported type, will return str([1, 2, 3])
        '[1, 2, 3]'
        >>> autoformat(None)
        'None'
    """
    # Determine the default output format for dates based on locale
    default_date_output_format = "%Y-%m-%d"
    if locale == "es_ES":
        default_date_output_format = "%d/%m/%Y"

    # Handle direct datetime, int, or float types first
    if isinstance(data_input, datetime):
        return format_date(data_input, output_format=default_date_output_format, locale=locale)
    elif isinstance(data_input, (int, float)):
        return format_number(data_input, locale=locale)

    # For string inputs, attempt date then number formatting, with a final fallback.
    elif isinstance(data_input, str):
        try:
            # Attempt to format as a DATE
            # We call format_date, if it succeeds, it means it's a date and we return its formatted value.
            return format_date(data_input, output_format=default_date_output_format, locale=locale)
        except ValueError:
            # If not a date, attempt to format as a NUMBER
            try:
                # Prepare the string for float conversion based on locale
                numeric_string_for_float = data_input
                if locale == "es_ES":
                    # Remove thousands separators (dots) and replace decimal comma with dot for float conversion
                    numeric_string_for_float = data_input.replace(".", "").replace(",", ".")
                
                # Try converting to float
                numeric_value = float(numeric_string_for_float)
                
                # If conversion to float succeeds, format it as a number
                return format_number(numeric_value, locale=locale)
            except ValueError:
                # If neither date nor number parsing works, return the original string.
                return str(data_input) # Ensure it's a string, just in case data_input was technically something else convertible to str.
    else:
        # If the type itself is not string, datetime, int, or float,
        # return its string representation as a fallback.
        # This handles types like lists, dicts, None, etc. gracefully without raising TypeError.
        return str(data_input)
    

def get_string_format(input_string: str) -> int:
    """Determines the casing format of a given string.

    This function analyzes the input string to identify if it's entirely
    lowercase, uppercase, title-cased, capitalized, or none of these (mixed/unknown).

    Args:
        input_string (str): The string to analyze.

    Returns:
        int:
            0: None, empty, or mixed/unknown format.
            1: Lowercase (e.g., "lowercase text").
            2: Capitalized (first letter uppercase, rest lowercase, e.g., "Capitalized text.").
            3: Title case (first letter of each word uppercase, e.g., "An Example Title", "Word").
            4: Uppercase (e.g., "UPPERCASE TEXT").

    Example:
        >>> get_string_format("hello world")
        1
        >>> get_string_format("Hello World")
        3
        >>> get_string_format("HELLO WORLD")
        4
        >>> get_string_format("Hello world")
        2
        >>> get_string_format("MiXeD cAsE")
        0
        >>> get_string_format(None)
        0
        >>> get_string_format("")
        0
    """
    if input_string is None or not input_string:
        # Handles None and empty strings as unknown/no format.
        return 0
    if input_string.isupper():
        # Checks if all characters are uppercase.
        return 4
    if input_string.islower():
        # Checks if all characters are lowercase.
        return 1
    if input_string.istitle():
        # Checks if the string is in title case (first letter of each word is capitalized).
        # This also correctly handles single words like "Word".
        return 3
    if input_string == input_string.capitalize():
        # Checks if only the first letter of the entire string is capitalized,
        # and the rest are lowercase. This condition is reached only if it's
        # not already captured by isupper, islower, or istitle.
        return 2

    # If none of the above formats match, it's considered mixed or unrecognized.
    return 0

    # Cost: O(N) where N is the length of the input_string, as string methods
    # like isupper(), islower(), istitle(), and capitalize() iterate over the string.


def apply_string_format(input_string: str, format_code: int) -> str:
    """Applies a specified casing format to a given string.

    This function transforms the input string based on a numeric format code,
    converting it to lowercase, capitalized, title case, or uppercase.

    Args:
        input_string (str): The string to which the format will be applied.
        format_code (int): The integer code representing the desired format:
                           1 for lowercase, 2 for capitalized, 3 for title case,
                           4 for uppercase. Any other value defaults to uppercase.

    Returns:
        str: The formatted string.

    Example:
        >>> apply_string_format("Hello World", 1)
        'hello world'
        >>> apply_string_format("hello world", 2)
        'Hello world'
        >>> apply_string_format("hello world", 3)
        'Hello World'
        >>> apply_string_format("hello world", 4)
        'HELLO WORLD'
        >>> apply_string_format("test", 99) # Defaults to uppercase
        'TEST'
    """
    if format_code == 1:
        # Converts the entire string to lowercase.
        return input_string.lower()
    elif format_code == 2:
        # Capitalizes the first letter of the string and converts the rest to lowercase.
        return input_string.capitalize()
    elif format_code == 3:
        # Converts the string to title case (first letter of each word capitalized).
        return input_string.title()
    elif format_code == 4:
        # Converts the entire string to uppercase.
        return input_string.upper()
    else:
        # If the format code is not recognized, default to uppercase.
        # This provides a consistent fallback behavior.
        return input_string.upper()

    # Cost: O(N) where N is the length of the input_string, as string transformation
    # methods iterate over the string.


def auto_format_string(input_string: str) -> str:
    """Automatically formats a string to either its original case (if all upper/lower)
    or capitalized.

    This function checks if the input string is entirely uppercase or lowercase.
    If so, it returns the string as is. Otherwise, it capitalizes the first letter
    of the string. This is useful for standardizing text where a consistent
    initial capitalization is desired unless the string is already uniformly cased.

    Args:
        input_string (str): The string to format automatically.

    Returns:
        str: The automatically formatted string.

    Example:
        >>> auto_format_string("HELLO")
        'HELLO'
        >>> auto_format_string("hello")
        'hello'
        >>> auto_format_string("hello world")
        'Hello world'
        >>> auto_format_string("Hello world")
        'Hello world'
    """
    if input_string.isupper() or input_string.islower():
        # If the string is entirely uppercase or lowercase, return it as is.
        return input_string
    else:
        # Otherwise, capitalize the first letter and make the rest lowercase.
        return input_string.capitalize()

    # Cost: O(N) where N is the length of the input_string due to string checks and transformations.


def capitalize_string(input_string: str, mode: str = 'all') -> str:
    """Capitalizes words in a string, with an optional mode to handle specific particles.

    This function capitalizes the first letter of each word in the input string.
    It can optionally handle 'particles' (prepositions, articles, conjunctions)
    in Spanish by keeping them lowercase when `mode` is 'location' and they
    are not the very first word of a segment. It intelligently splits the string
    by spaces, hyphens, and slashes to process each word or segment independently.

    Args:
        input_string (str): The string to be capitalized.
        mode (str, optional): The capitalization mode.
                              'all': Capitalize every word.
                              'location': Capitalize every word, but keep specified
                                          particles (e.g., 'de', 'el') lowercase
                                          unless they are the first word in a segment.
                                          Defaults to 'all'.

    Returns:
        str: The string with words capitalized according to the specified mode.

    Example:
        >>> capitalize_string("via del mar", mode='location')
        'Via del Mar'
        >>> capitalize_string("san-pablo", mode='location')
        'San-Pablo'
        >>> capitalize_string("juan perez")
        'Juan Perez'
        >>> capitalize_string("calle de la amargura", mode='location')
        'Calle de la Amargura'
        >>> capitalize_string("felipe ii/madrid", mode='location')
        'Felipe II/Madrid'
    """
    # Define a set of particles to be kept lowercase in 'location' mode.
    # Using a set provides O(1) average time complexity for lookups,
    # which is efficient for checking word membership.
    particles = {"de", "al", "del", "la", "las", "los", "el", "y", "o", "u", "en", "con", "por", "para", "a"}

    def _capitalize_word(word: str, is_first_word_in_segment: bool) -> str:
        """Helper function to capitalize a single word based on the mode and position."""
        # Only apply particle rule if mode is 'location' AND it's not the first word
        # in its logical segment AND the word (lowercase) is in our particles set.
        if mode == 'location' and word.lower() in particles and not is_first_word_in_segment:
            return word.lower()
        # Otherwise, capitalize the word.
        return word.capitalize()

    # Split the input string by delimiters (spaces, hyphens, slashes) using pre-compiled pattern
    # The delimiters themselves are included in the `parts` list for string reconstruction
    parts = _RE_WORD_DELIMITERS.split(input_string)
    capitalized_parts = []

    # This flag helps determine if a word is the first word within a segment
    # (e.g., "VIA-DEL-MAR" means "VIA" is first, then "DEL" is first in its segment).
    is_first_word_in_segment = True

    for part in parts:
        # Check if the current part is one of our defined delimiters.
        if re.match(r'[\s/\-]', part):
            capitalized_parts.append(part)
            # Reset the flag because a delimiter signifies the start of a new segment.
            is_first_word_in_segment = True
        else:
            # If it's a word, apply the capitalization rules using the helper function.
            capitalized_parts.append(_capitalize_word(part, is_first_word_in_segment))
            # After processing a word, the next word in the same segment won't be the first.
            is_first_word_in_segment = False

    # Join all the processed parts back into a single string.
    return "".join(capitalized_parts)

    # Cost: O(N) where N is the length of input_string due to splitting and joining
    # operations, and word processing. The `re.split` operation and string concatenations
    # dominate the cost.


def pad_string(text: str, length: int, char: str = ' ', direction: str = 'right') -> str:
    """
    Rellena una cadena de texto hasta una longitud específica con un carácter dado.

    Args:
        text (str): La cadena de texto a rellenar.
        length (int): La longitud total deseada de la cadena resultante.
        char (str): El carácter con el que se rellenará la cadena. Debe ser un solo carácter.
                    Por defecto es un espacio (' ').
        direction (str): La dirección del relleno. Puede ser 'left' (izquierda) o 'right' (derecha).
                         Por defecto es 'right'.

    Returns:
        str: La cadena rellenada hasta la longitud especificada.
             Si la cadena original ya es igual o más larga que la longitud deseada,
             se devolverá la cadena original truncada a la longitud si es más larga.

    Raises:
        ValueError: Si 'char' no es un solo carácter o 'direction' no es 'left' o 'right'.
    """
    if not isinstance(text, str):
        text = str(text) # Asegurarse de que la entrada sea una cadena

    if not isinstance(length, int) or length < 0:
        raise ValueError("La longitud debe ser un número entero no negativo.")

    if not isinstance(char, str) or len(char) != 1:
        raise ValueError("El carácter de relleno (char) debe ser un solo carácter.")

    if direction not in ['left', 'right']:
        raise ValueError("La dirección debe ser 'left' o 'right'.")

    # Si la cadena ya es igual o más larga, la truncamos.
    # En muchos casos de "padding", se espera que si la cadena ya es larga,
    # no se modifique o se trunque. Aquí optamos por truncar si excede.
    if len(text) >= length:
        return text[:length]

    # Calcular cuántos caracteres de relleno se necesitan
    padding_needed = length - len(text)
    if padding_needed < 0:
        padding_needed = 0

    if direction == 'right':
        return text + (char * padding_needed)
    else: # direction == 'left'
        return (char * padding_needed) + text


def to_upper(text: Optional[str]) -> Optional[str]:
    """
    Convierte una cadena de texto a mayúsculas.

    Args:
        text (Optional[str]): La cadena de texto de entrada. Puede ser None.

    Returns:
        Optional[str]: La cadena convertida a mayúsculas, o None si la entrada fue None.
                       Si la entrada es una cadena vacía, devuelve una cadena vacía.
    """
    if text is None:
        return None
    return text.upper()


def to_lower(text: Optional[str]) -> Optional[str]:
    """
    Convierte una cadena de texto a minúsculas.

    Args:
        text (Optional[str]): La cadena de texto de entrada. Puede ser None.

    Returns:
        Optional[str]: La cadena convertida a minúsculas, o None si la entrada fue None.
                       Si la entrada es una cadena vacía, devuelve una cadena vacía.
    """
    if text is None:
        return None
    return text.lower()


def normalize_spaces(text: Optional[str]) -> Optional[str]:
    """
    Normalizes whitespace in a string: replaces multiple spaces with a single space
    and removes leading/trailing spaces.
    Optimized with pre-compiled regex pattern for better performance.

    Args:
        text (Optional[str]): The input string. Can be None.

    Returns:
        Optional[str]: The string with normalized spaces, or None if the input was None.
                       Returns an empty string if the input was an empty string.
    
    Cost:
        O(n) where n is the length of the text. Uses pre-compiled regex pattern
        to avoid repeated compilation overhead.
    """
    if text is None:
        return None
    
    # Use pre-compiled regex pattern to replace multiple whitespace with single space
    # Then use .strip() to remove leading/trailing whitespace
    return _RE_WHITESPACE.sub(' ', text).strip()


def normalize_symbols(text: Optional[str]) -> Optional[str]:
    r"""
    Normalizes spacing around common symbols and punctuation marks in a string.
    Optimized with pre-compiled regex patterns for better performance.

    This function applies the following rules:
    1. Removes spaces around symbols that typically 'stick' to words/numbers (e.g., @, (), [], {}, <>, #, /, \, |, _, -, ?, !, ¡, º, ª).
    2. Ensures a space AFTER punctuation that typically requires it (e.g., ., ,, :, ;).
    3. Ensures a single space AROUND operators (e.g., +, =, &).
    4. Removes space BEFORE currency symbols (e.g., $, €).
    5. Finally, normalizes all remaining multiple spaces to single spaces.

    Args:
        text (Optional[str]): The input string. Can be None.

    Returns:
        Optional[str]: The string with normalized symbols and spaces, or None if the input was None.
                       Returns an empty string if the input was an empty string.
    
    Cost:
        O(n) where n is the length of the text. Optimized with pre-compiled regex patterns
        to eliminate repeated pattern compilation overhead.
    """
    if text is None:
        return None

    # Ensure the input is a string to avoid errors with string methods.
    processed_text = str(text)

    # 1. Normalize spaces around symbols that should have NO space before/after
    # Using pre-compiled pattern for better performance
    processed_text = _RE_SYMBOLS_NO_SPACE.sub(r'\1', processed_text)

    # 2. Normalize spaces around punctuation that should always have a space AFTER them
    # Using pre-compiled pattern
    processed_text = _RE_PUNCTUATION_AFTER_SPACE.sub(r'\1 ', processed_text)

    # 3. Ensure a single space *around* specific operators (+, =, &)
    # Using pre-compiled pattern
    processed_text = _RE_OPERATORS_AROUND_SPACE.sub(r' \1 ', processed_text)

    # 4. Remove space before currency symbols ($ , €)
    # Using pre-compiled pattern
    processed_text = _RE_CURRENCY_NO_SPACE_BEFORE.sub(r'\1', processed_text)
    
    # 5. Final normalization of multiple spaces and strip using pre-compiled pattern
    return _RE_WHITESPACE.sub(' ', processed_text).strip()


def flat_vowels(input_string: str) -> str:
    """
    Removes only acute accents from vowels while preserving 'ñ', 'ç', and 'ü'.

    This function iterates through the input string, applying specific rules
    for 'ñ', 'ç', and 'ü' to ensure they remain unchanged. For other characters,
    it normalizes them to decompose accented vowels into their base letter
    and a diacritic, then filters out only the diacritics. The final string
    is converted to uppercase.

    Args:
        input_string (str): The string to process.

    Returns:
        str: The string with only acute accents removed, with 'ñ', 'ç', and 'ü'
             preserved, and converted to uppercase.

    Raises:
        TypeError: If the input is not a string.

    Example:
        >>> flat_vowels("España, cómo estás, pingüino, Cançao, Corazón")
        'ESPAÑA, COMO ESTAS, PINGÜINO, CANÇAO, CORAZON'

    Cost:
        The cost of this function is **O(n)**, where 'n' is the length of the
        input string. This is because it processes each character individually.
    """
    if not isinstance(input_string, str):
        # Raising a TypeError clearly indicates that the function received an
        # unsupported input type, which is a common best practice for robust functions.
        raise TypeError("Input must be a string.")

    result_chars = []
    for char in input_string:
        # Check if the character is one of the special Spanish characters (Ñ, Ç, Ü)
        # or their lowercase equivalents. If so, preserve them as is.
        if char.lower() in ('ñ', 'ç', 'ü'):
            result_chars.append(char)
        else:
            # For all other characters, normalize them to their decomposed form (NFKD).
            # This separates base letters from their diacritics (like acute accents).
            normalized_char = unicodedata.normalize('NFKD', char)
            # Filter out only the combining characters (diacritics/accents)
            # and append the base character to the result.
            # This effectively removes acute accents from vowels (á -> a, é -> e, etc.).
            flattened_char = ''.join([c for c in normalized_char if not unicodedata.combining(c)])
            result_chars.append(flattened_char)

    # Finally, convert the entire resulting string to uppercase.
    return normalize_spaces("".join(result_chars).upper())


def ascii_string(input_string: str | None) -> str | None:
    """
    Converts a string to its ASCII representation, ignoring characters that cannot be encoded in ASCII.

    This function is useful for cleaning strings by removing non-ASCII characters,
    which can be beneficial when working with systems or formats that only support ASCII.
    If the input is None, it returns None directly.

    Args:
        input_string (str | None): The string to convert. Can be None.

    Returns:
        str | None: The ASCII-encoded string. Returns None if the input was None.

    Raises:
        TypeError: If 'input_string' is provided and is not a string or None.

    Example:
        >>> ascii_string("Héllø Wörld!")
        'Hll Wrld!'

        >>> ascii_string("This is an ASCII string.")
        'This is an ASCII string.'

        >>> ascii_string(None) is None
        True

        >>> ascii_string("Grüße")
        'Gre'
    """
    if input_string is None:
        return None

    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string or None.")

    # Encode the string to ASCII, ignoring characters that cannot be represented in ASCII.
    # Then, decode it back to a UTF-8 string to ensure it's a standard Python string.
    # This process effectively strips out all non-ASCII characters.
    ascii_string = input_string.encode('ascii', 'ignore').decode('utf-8')

    return ascii_string


def string_aZ09(input_string):
    """
    Feature Description:
    Filters a string to keep only alphanumeric characters (a-z, A-Z, 0-9).
    Optimized with pre-compiled regex pattern for better performance.

    Args:
        input_string (str): The string to filter.

    Returns:
        str: A new string containing only alphanumeric characters from the input.

    Raises:
        TypeError: If the input is not a string.

    Usage Example:
    string_aZ09("Hola Mundo 123!") returns "HolaMundo123"
    
    Cost:
        O(n) where n is the length of input_string. Uses pre-compiled regex pattern.
    """
    return string_aZ09_plus(input_string)


def string_aZ09_plus(input_string, additional_charset=""):
    """
    Filters a string to keep only alphanumeric characters (a-z, A-Z, 0-9)
    and any characters provided in an additional charset.

    This function leverages regular expressions for efficient character filtering,
    allowing for a highly customizable set of allowed characters.

    Args:
        input_string (str): The string to filter.
        additional_charset (str, optional): An optional string containing
            additional characters to allow in the filtered output. Defaults
            to an empty string, meaning only alphanumeric characters are kept.

    Returns:
        str: A new string containing only alphanumeric characters and characters
            from the additional_charset.

    Raises:
        TypeError: If the input_string is not a string.

    Usage Example:
        # Example 1: Basic alphanumeric filtering
        string_aZ09_plus("Hello World 123!")  # Returns "HelloWorld123"

        # Example 2: Filtering with an additional charset for spaces and hyphens
        string_aZ09_plus("This-is a test!", " -") # Returns "This-is a test"

    Cost:
        The time complexity of this function is O(n), where n is the length of the input_string,
        due to the regular expression substitution operation. The compilation of the regex
        is O(m), where m is the length of the regex pattern, which is constant for repeated calls.
    """
    if not isinstance(input_string, str):
        return None

    # Why combine the base alphanumeric set with the additional_charset:
    # This approach creates a comprehensive regular expression that includes
    # all standard alphanumeric characters along with any user-defined characters.
    # By using a character set within the regex [^...], we efficiently match
    # anything NOT in the specified set, allowing for a single substitution operation.
    # The re.escape is used to treat special regex characters in additional_charset
    # as literal characters.
    regex_pattern = r"[^a-zA-Z0-9" + re.escape(additional_charset) + r"]"
    disallowed_characters = re.compile(regex_pattern)

    # Substitute all non-allowed characters with an empty string
    cleaned_string = disallowed_characters.sub("", input_string)

    return cleaned_string


def string_aZ(input_string):
    """
    Feature Description:
    Filters a string to keep only alphabetic characters (a-z, A-Z).
    Optimized with pre-compiled regex pattern for better performance.

    Args:
        input_string (str): The string to filter.

    Returns:
        str: A new string containing only alphabetic characters from the input.

    Raises:
        TypeError: If the input is not a string.

    Usage Example:
    string_aZ("Hola Mundo 123!") returns "HolaMundo"
    
    Cost:
        O(n) where n is the length of input_string. Uses pre-compiled regex pattern.
    """
    return string_aZ_plus(input_string)


def string_aZ_plus(input_string, additional_charset=""):
    """
    Filters a string to keep only alphabetic characters (a-z, A-Z)
    and any characters provided in an additional charset.

    This function utilizes regular expressions for efficient character filtering,
    allowing for a highly customizable set of allowed characters.

    Args:
        input_string (str): The string to filter.
        additional_charset (str, optional): An optional string containing
            additional characters to allow in the filtered output. Defaults
            to an empty string, meaning only alphabetic characters are kept.

    Returns:
        str: A new string containing only alphabetic characters and characters
            from the additional_charset.

    Raises:
        TypeError: If the input_string is not a string.

    Usage Example:
        # Example 1: Basic alphabetic filtering
        string_aZ_plus("Hello World 123!")  # Returns "HelloWorld"

        # Example 2: Filtering with an additional charset for spaces and hyphens
        string_aZ_plus("This-is a test!", " -") # Returns "This-isatest"

    Cost:
        The time complexity of this function is O(n), where n is the length of the input_string,
        due to the regular expression substitution operation. The compilation of the regex
        is O(m), where m is the length of the regex pattern, which is constant for repeated calls.
    """
    if not isinstance(input_string, str):
        return None

    # Why combine the base alphabetic set with the additional_charset:
    # This approach creates a comprehensive regular expression that includes
    # all standard alphabetic characters along with any user-defined characters.
    # By using a character set within the regex [^...], we efficiently match
    # anything NOT in the specified set, allowing for a single substitution operation.
    # The re.escape is used to treat special regex characters in additional_charset
    # as literal characters.
    if not additional_charset:
        additional_charset = ""
    regex_pattern = r"[^a-zA-Z" + re.escape(additional_charset) + r"]"
    disallowed_characters = re.compile(regex_pattern)

    # Substitute all non-allowed characters with an empty string
    cleaned_string = disallowed_characters.sub("", input_string)

    return cleaned_string


def numbers_from_string(
    input_string: str,
    separator: str = ''
) -> Optional[str]:
    """Extracts all numerical sequences from a given string and returns them as a single string.

    This function uses regular expressions to find all occurrences of integers or
    floating-point numbers within the input string. It then joins these numbers
    together using an optional separator to form a single output string.
    If no numbers are found, or the input string is empty, it returns None.

    Args:
        input_string: The string from which to extract numbers.
        separator: The string to use to join the extracted numbers. Defaults to an
                   empty string, meaning numbers will be concatenated directly.

    Returns:
        A single string containing all the numbers found in the input string,
        joined by the specified separator. Returns None if no numbers are found
        or the input string is empty.

    Raises:
        TypeError: If the input 'input_string' is not a string.

    Example of use:
        >>> numbers_from_string("The price is $12.99 with 5% tax.")
        "12.995"

        >>> numbers_from_string("Item ID: 12345, Quantity: 7", separator="-")
        "12345-7"

        >>> numbers_from_string("No numbers here.")
        None

        >>> numbers_from_string("")
        None

        >>> numbers_from_string("Measurement: -10.5 meters and 20 degrees.", separator=", ")
        "-10.5, 20"
    """
    if not input_string:
        return None
    
    # Validate input type to ensure it's a string.
    if not isinstance(input_string, str):
        raise TypeError("The input 'input_string' must be a string.")

    # Use pre-compiled regex pattern for better performance
    # Pattern matches integers and floating-point numbers with optional negative signs
    found_numbers = _RE_NUMBERS.findall(input_string)

    # If no numbers were found, return None as per the specification.
    if not found_numbers:
        return None

    # Join the found number strings using the specified separator.
    return separator.join(found_numbers)


def remove_numbers_from_string(input_string: str) -> str:
    """Removes all numerical digits and decimal points from a given string.

    This function uses regular expressions to find and remove all occurrences
    of digits (0-9) and periods (which are often part of numbers, e.g., '3.14').
    It returns the modified string with numbers removed.

    Args:
        input_string: The string from which to remove numbers.

    Returns:
        A new string with all numerical digits and decimal points removed.

    Raises:
        TypeError: If the input 'input_string' is not a string.

    Example of use:
        >>> remove_numbers_from_string("The price is $12.99 with 5% tax.")
        "The price is $ with % tax."

        >>> remove_numbers_from_string("Item ID: 12345, Quantity: 7")
        "Item ID: , Quantity: "

        >>> remove_numbers_from_string("No numbers here.")
        "No numbers here."

        >>> remove_numbers_from_string("")
        ""
    """
    if not input_string:
        return None
    
    # Validate input type to ensure it's a string.
    if not isinstance(input_string, str):
        raise TypeError("The input 'input_string' must be a string.")

    # Use pre-compiled regex pattern to remove digits and decimal points
    return _RE_NUMBERS_AND_DOTS.sub('', input_string)


def reorder_comma_fullname(name_with_surname: str) -> str:
    """
    Reformats a name string from 'Surname, Name' to 'Name Surname'.

    This function takes a string where the surname is followed by a comma
    and then the first name. It splits the string at the comma and
    rearranges the parts to return the first name followed by the surname.

    Args:
        name_with_surname (str): The input string in 'Surname, Name' format.

    Returns:
        str: The reformatted name string in 'Name Surname' format.

    Raises:
        ValueError: If the input string does not contain a comma.

    Example of use:
        >>> reorder_comma_fullname("Doe, John")
        'John Doe'
    """
    # Ensure that the input string contains a comma before proceeding.
    if "," not in name_with_surname:
        raise ValueError("Input string must contain a comma to separate name and surname.")

    # Split the string into parts based on the comma.
    # We expect two parts: surname and name.
    parts = [part.strip() for part in name_with_surname.split(',')]

    # Check if we have exactly two parts after splitting.
    # This prevents issues with multiple commas or empty strings.
    if len(parts) != 2:
        raise ValueError("Input string must be in 'Surname, Name' format with exactly one comma.")

    # The first part is the surname, the second part is the name.
    surname, name = parts[0], parts[1]

    # Combine the name and surname in the desired order.
    # Cost: O(1) as it involves basic string operations.
    return f"{name} {surname}"


def format_email_address(email_string: str) -> str:
    """Cleans an email address string by removing common typos and invalid characters.

    This function sanitizes an email address string by:
    1. Stripping leading and trailing whitespace.
    2. Replacing multiple internal spaces with a single space.
    3. Removing characters that are generally invalid in email addresses,
       preserving standard email characters like alphanumeric, '.', '_', '+', '-', and '@'.
       It does not attempt to validate the email structure, only to clean it for validation.

    Args:
        email_string (str): The email address string to be cleaned.

    Returns:
        str: The cleaned email address string.

    Raises:
        TypeError: If the input is not a string.

    Example of use:
        >>> format_email_address("  user.name+tag@example.com  ")
        'user.name+tag@example.com'
        >>> format_email_address("user @ domain.c@om")
        'user@domain.com'
        >>> format_email_address("invalid#char!@test.com")
        'invalidchar@test.com'
    """
    if not isinstance(email_string, str):
        # Always check input type for robustness.
        raise TypeError("Input must be a string.")

    # 1. Strip leading and trailing whitespace.
    # Often, copy-pasted emails have accidental spaces.
    cleaned_email = email_string.strip()

    # 2. Replace multiple internal spaces with a single space using pre-compiled pattern
    cleaned_email = _RE_WHITESPACE.sub(' ', cleaned_email)

    # 3. Remove characters generally not valid in email addresses using pre-compiled pattern
    # This regex keeps alphanumeric characters, and common email special characters:
    # '.', '_', '+', '-', '@'. Other characters are removed.
    cleaned_email = _RE_EMAIL_VALID_CHARS.sub('', cleaned_email)

    # Although not strictly a "typo," a common error is having multiple '@' symbols.
    # We ensure only the last '@' is kept, assuming standard email format.
    # This simplifies strings like "user@domain@email.com" to "userdomain@email.com".
    parts = cleaned_email.split('@')
    if len(parts) > 2:
        # Join all but the last part, then add the last part with an '@'.
        # This effectively removes extra '@' symbols from the local part.
        cleaned_email = "".join(parts[:-1]).replace(' ', '') + '@' + parts[-1]
    elif len(parts) == 1 and '@' not in cleaned_email:
        # If there was no '@' originally, or it was stripped by invalid chars,
        # we might have a string that's not an email, but we still return it cleaned.
        pass # No change needed if no '@' or only one part

    return cleaned_email


def format_url(url_string: str) -> str:
    """Cleans a URL string by removing common typos and unsafe/invalid characters.

    This function sanitizes a URL string by:
    1. Stripping leading and trailing whitespace.
    2. Replacing multiple internal spaces with a single space.
    3. Removing characters that are generally invalid or unsafe in URLs
       (e.g., non-ASCII characters, specific symbols that are never allowed).
       It preserves standard URL characters like alphanumeric, '.', '/', ':',
       '?', '=', '&', '-', '_', and '~'.
       This function focuses on cleaning the string for URL parsing, not on
       percent-encoding data within query parameters (which is a separate step).

    Args:
        url_string (str): The URL string to be cleaned.

    Returns:
        str: The cleaned URL string.

    Raises:
        TypeError: If the input is not a string.

    Example of use:
        >>> format_url("  https://www.example.com/ path with spaces?id=123  ")
        'https://www.example.com/path%20with%20spaces?id=123'
        >>> format_url("http://site.com/page?query=val!ue")
        'http://site.com/page?query=val!ue'
        >>> format_url("ftp://bad^char.com/file")
        'ftp://badchar.com/file'
    """
    if not isinstance(url_string, str):
        # Input validation is crucial for function reliability.
        raise TypeError("Input must be a string.")

    # 1. Strip leading and trailing whitespace.
    # Common for URLs copied from text or documents.
    cleaned_url = url_string.strip()

    # 2. Replace multiple internal spaces with a single space using pre-compiled pattern
    cleaned_url = _RE_WHITESPACE.sub(' ', cleaned_url)

    # 3. Remove characters that are generally not allowed or unsafe using pre-compiled pattern
    # This regex removes characters that are typically *never* valid in a raw URL
    # We also include "%" as it's part of percent-encoding.
    cleaned_url = _RE_URL_VALID_CHARS.sub('', cleaned_url)

    # 4. Handle spaces within the URL: percent-encode them.
    # Spaces are not allowed unencoded in URLs. The `quote_plus` function from
    # `urllib.parse` is excellent for this. However, applying it to the *entire*
    # URL can over-encode. Instead, we manually replace spaces here.
    # For more robust encoding, consider using `urllib.parse.urlparse` and then
    # `quote` individual components (path, query, fragment).
    cleaned_url = cleaned_url.replace(' ', '%20')

    return cleaned_url


def format_internet_domain(domain_string: str) -> str:
    """
    Cleans and normalizes an internet domain string.

    This function:
    1. Strips leading/trailing whitespace.
    2. Converts to lowercase (domains are case-insensitive).
    3. Removes invalid characters (keeps a-z, 0-9, '-', and '.').
    4. Collapses multiple consecutive dots or hyphens.
    5. Removes leading/trailing dots and hyphens.
    6. Does not validate TLD or domain existence.

    Args:
        domain_string (str): The domain string to clean.

    Returns:
        str: The cleaned and normalized domain string.

    Example:
        >>> format_internet_domain("  WWW.Example--Site...COM  ")
        'www.example-site.com'
        >>> format_internet_domain("Mi_Sitio!@#$.es")
        'misitio.es'
    """
    if not isinstance(domain_string, str):
        raise TypeError("Input must be a string.")

    # 1. Strip whitespace and convert to lowercase
    domain = domain_string.strip().lower()

    # 2. Remove invalid characters using pre-compiled pattern (keep a-z, 0-9, '-', '.')
    domain = _RE_DOMAIN_VALID_CHARS.sub('', domain)

    # 3. Collapse multiple consecutive dots or hyphens using pre-compiled patterns
    domain = _RE_MULTIPLE_HYPHENS.sub('-', domain)
    domain = _RE_MULTIPLE_DOTS.sub('.', domain)

    # 4. Remove leading/trailing dots and hyphens
    domain = domain.strip('.-')

    return domain



def format_name(input_string: str, add_charset: str = "", name_type: str = "PERSONA", shift: bool = False) -> str:
    """
    Description:
        Formats a name string by removing unwanted characters, normalizing symbols, and applying type-specific character filtering.
        Optimized with pre-compiled regex patterns for better performance.

    Args:
        input_string (str): The string to format.
        add_charset (str): Additional characters to allow in the output.
        name_type (str): The type of name, e.g., "PERSONA" for people, determines filtering rules.
        shift (bool): Unused parameter, kept for compatibility.

    Returns:
        str: The formatted name string.

    Raises:
        TypeError: If input_string is not a string.

    Example Usage:
        >>> format_name("José Pérez", "", "PERSONA")
        'JOSE PEREZ'
        >>> format_name("Cía. de Café S.L.", "", "EMPRESA")
        'CIA DE CAFE SL'

    Cost:
        O(n) where n is the length of input_string. Optimized with pre-compiled regex patterns
        and streamlined character replacement using str.translate() for single-pass processing.
    """
    if input_string is None:
        return None

    if not isinstance(input_string, str):
        raise TypeError("input_string must be a string.")

    if name_type == "PERSONA":
        return format_fullname(input_string)
    
    # Use pre-computed translation table for efficient single-pass character replacement
    # This is significantly faster than multiple .replace() calls or creating the table each time
    formatted = input_string.translate(_TRANSLATION_TABLE_NAMES)
    
    # Remove unwanted special characters, respecting add_charset
    formatted = fxStrOp.erase_specialchar(formatted, add_charset)
    
    # Apply symbol normalization pattern
    formatted = normalize_symbols(formatted)
    
    if not formatted:
        return formatted
    
    # Ensure 'º' and 'ª' are spaced correctly using single replace chain
    formatted = formatted.replace("º", "º ").replace("ª", "ª ").replace(" º", "º").replace(" ª", "ª")
    
    # Normalize according to name_type
    # Note: name_type == "PERSONA" already handled above, so this is for other types
    formatted = string_aZ09_plus(formatted, "ºª " + add_charset)
    
    # Remove redundant spaces using pre-compiled regex
    formatted = _RE_WHITESPACE.sub(' ', formatted).strip()
    
    return formatted


def format_fullname(fullname: str | None, uppercase: bool = True) -> str | None:
    """
    Formats a person's full name by removing unwanted characters and normalizing spaces.
    Optimized with pre-compiled regex patterns and str.translate() for better performance.
    
    This function standardizes person names by:
    1. Removing or replacing special characters with spaces (optimized with translate)
    2. Flattening accented vowels while preserving 'ñ', 'ç', and 'ü'
    3. Removing titles (Dr, Sr, Don, Dña, Mr, Mrs, etc.) using pre-defined set
    4. Normalizing spaces with pre-compiled regex
    5. Converting to uppercase (optional)
    6. Capitalizing each word appropriately
    
    Args:
        fullname (str | None): The full name to format. Can be None.
        uppercase (bool): If True, converts to uppercase before capitalizing. Defaults to True.
    
    Returns:
        str | None: The formatted full name in proper case, or None if input was None.
    
    Raises:
        TypeError: If the input is not a string or None.
    
    Example:
        >>> format_fullname("josé  garcía-lópez")
        'Jose Garcia-Lopez'
        >>> format_fullname("MARÍA DEL CARMEN")
        'Maria Carmen'
        >>> format_fullname("Dr. Juan Pérez")
        'Juan Perez'
        >>> format_fullname("SR. D. ANTONIO GARCIA")
        'Antonio Garcia'
        >>> format_fullname("o'connor", uppercase=False)
        "O'connor"
        >>> format_fullname(None)
        None
    
    Cost:
        O(n + w) where n is the length of the fullname string and w is the number of words.
        Optimized with str.translate() for single-pass character replacement, pre-compiled 
        regex for whitespace normalization, and frozenset for O(1) title lookup.
    """
    if fullname is None:
        return None
    
    if not isinstance(fullname, str):
        raise TypeError("Input 'fullname' must be a string or None.")
    
    # Use pre-computed translation table for efficient single-pass character replacement
    # This avoids creating the translation table on every function call
    formatted = fullname.translate(_TRANSLATION_TABLE_NAMES)
    
    # Remove parentheses and their content using pre-compiled regex
    formatted = _RE_PARENTHESES.sub(' ', formatted)
    
    # Flatten accented vowels while preserving ñ, ç, ü
    formatted = flat_vowels(formatted)
    
    # Normalize multiple spaces to single space using pre-compiled regex
    formatted = _RE_WHITESPACE.sub(' ', formatted).strip()
    
    if not formatted:
        return formatted
    
    # Remove titles from the name (Dr, Sr, Don, etc.)
    # Split into words, filter out titles, and rejoin
    words = formatted.split()
    filtered_words = [word for word in words if word.upper() not in _TITLES_TO_REMOVE]
    formatted = ' '.join(filtered_words)
    
    if not formatted:
        return formatted
    
    # Convert to uppercase first if requested (for normalization)
    if uppercase:
        formatted = formatted.upper()
    else:
        # Capitalize appropriately (handles particles in Spanish names)
        formatted = capitalize_string(formatted, mode='location')
    
    return formatted


def format_company_name(
    company_name: str | None,
    company_type: str | None,
    format_style: str
) -> str | None:
    """
    Formats a company name by appending its type according to a specified style.

    This function takes a company name and its legal type, then combines them.
    It provides different formatting styles for the company type, such as enclosing
    it in brackets or abbreviating it with dots. Certain administrative or
    non-standard company types are handled differently, typically by appending
    them after a comma. The original function included a call to an undefined
    `get_companyname` function for these cases, which has been removed to ensure
    this function's sole responsibility is formatting.

    The function is case-sensitive.

    Args:
        company_name (str | None): The base name of the company.
        company_type (str | None): The legal type of the company (e.g., 'S.L.', 'LTD').
        format_style (str): The formatting rule to apply.
                              Expected values: 'brackets', 'dots', 'comma&dots'.

    Returns:
        str | None: The formatted company name, or None if the input name is None.

    Raises:
        ValueError: If an unknown format_style is provided.

    Example of use:
        format_company_name('My Business', 'S.L.', 'dots') -> 'My Business S.L.'
        format_company_name('Innovate Inc', 'INC', 'comma&dots') -> 'Innovate Inc, INC.'
        format_company_name('Tech Solutions', 'LTD', 'brackets') -> 'Tech Solutions (LTD)'
        format_company_name('City Council', 'CORPORACION LOCAL', 'dots') -> 'City Council, CORPORACION LOCAL'

    Cost:
        The time complexity is generally O(1). However, for short company types
        that require dots between letters (e.g., 'SL' -> 'S.L.'), the complexity
        is O(K), where K is the number of characters in the company_type string,
        due to the string join operation.
    """
    # Guard clause: Return early if there's no company name to format.
    if not company_name:
        return None

    # Guard clause: If the company type is missing or not applicable,
    # return the original name without formatting.
    if not company_type or company_type == 'N/A':
        return company_name

    #
    # Handle excluded types, which are not standard legal forms.
    #
    if company_type in EXCLUDED_COMPANY_TYPES:
        # These types are typically appended as-is, following a comma.
        return f"{company_name}, {company_type}"

    #
    # Handle standard legal forms based on the specified format style.
    #
    suffix = ""

    if format_style == 'brackets':
        suffix = f" ({company_type})"

    elif format_style in ['dots', 'comma&dots']:
        # Determine how to apply dots.
        # Why: Long forms or specific short forms get a single dot at the end.
        # Other short forms get dots between letters (e.g., 'S.A.' from 'SA').
        if len(company_type) >= 4 or company_type in SHORT_TYPES_WITH_DOTS:
            base_type = f"{company_type}."
        else:
            # Use join for efficiency instead of looping and concatenating strings.
            base_type = '.'.join(company_type) + '.'

        # A blank line to separate logical blocks: formatting vs. prefixing.
        if format_style == 'comma&dots':
            suffix = f", {base_type}"
        else: # 'dots'
            suffix = f" {base_type}"

    else:
        # Why: It's good practice to handle unexpected inputs to prevent silent failures.
        raise ValueError(f"Unknown format_style: '{format_style}'")

    return company_name + suffix


def parse_company(company_name: str, legal_forms_set_override: set = None) -> list:
    """
    Description:
        Separates the company name from its legal form, handling malformed formats and edge cases.
        Prioritizes longer legal forms, normalizes input, and ensures robust matching using regular expressions.

    Args:
        company_name (str): The full company name (e.g., "Acme Corp Ltd").
        legal_forms_set_override (set, optional): A set of legal forms to search. If None, uses the global LEGAL_FORMS_SET.

    Returns:
        list: [company_name_only, canonical_legal_form]. If no legal form is found, returns [original_company_name, None].

    Raises:
        None

    Example Usage:
        >>> parse_company("PESCANOVA S.A.", {"SA"})
        ['PESCANOVA', 'SA']
        >>> parse_company("Acme Corp Ltd.", {"LTD"})
        ['Acme Corp', 'LTD']
        >>> parse_company("No Legal Form Company")
        ['No Legal Form Company', None]

    Cost:
        O(M log M + M * N * K), where M is the number of legal forms, N is the string length, and K is regex complexity.
    """
    # Use override set if provided, else global set
    forms_to_search = legal_forms_set_override if legal_forms_set_override is not None else LEGAL_FORMS_SET

    # Normalize and preprocess the company name
    original_company_name = company_name.strip()
    company_name_upper = original_company_name.upper()

    # Remove common suffixes and normalize
    suffixes = [
        '(EXTINGUIDA)', '- EXTINGUIDA', '-EXTINGUIDA',
        '(EN LIQUIDACION)', ' EN LIQUIDACION'
    ]
    for suffix in suffixes:
        company_name_upper = company_name_upper.replace(suffix, '')

    # Replace common Spanish legal form phrases with abbreviations
    replacements = {
        'SOCIEDAD LIMITADA': 'SL',
        'SOCIEDAD ANONIMA': 'SA',
        'COM PROP': 'COMUNIDAD DE PROPIETARIOS',
        'CDAD PROP': 'COMUNIDAD DE PROPIETARIOS',
        ' ASOC ': ' ASOCIACION ',
        ' ASOC.': ' ASOCIACION ',
        'SOCIEDAD DE RESPONSABILIDAD LIMITADA': 'SRL',
        'SOCIEDAD COOPERATIVA': 'SCOOP',
        'SOCIEDAD COOP': 'SCOOP',
        'S COOP': 'SCOOP',
        'SOCIEDAD ANONIMA LABORAL': 'SAL',
        'SOCIEDAD DE RESPONSABILIDAD LIMITADA LABORAL': 'SRLL',
        'SL LABORAL': 'SLL',
        'SOCIEDAD LIMITADA LABORAL': 'SLL',
        'SA DEPORTIVA': 'SAD',
        'SL PROFESIONAL': 'SLP',
        ' SCOOPL': ' SCOOP',
        ' SCL': ' SC'
    }
    for old, new in replacements.items():
        company_name_upper = company_name_upper.replace(old, new)

    # Normalize symbols and spaces
    company_name_normalized = format_name(company_name_upper, "ºª@#$%&=+-_/\\|.:[]()¿?¡!'", "COMPANY", True)

    # Sort legal forms by descending length for longest match first
    sorted_forms = sorted(forms_to_search, key=len, reverse=True)

    found_legal_form = None
    remaining_company_name = company_name_normalized

    for form_upper in sorted_forms:
        # Build regex for flexible matching (spaces, dots, commas, parentheses)
        regex_core = ''.join(
            f"{re.escape(char)}[\\s\\.,()]*" if char.isalnum() else re.escape(char)
            for char in form_upper
        )
        if regex_core.endswith('[\\s\\.,()]*'):
            regex_core = regex_core[:-len('[\\s\\.,()]*')]

        pattern = re.compile(
            r"^(.*?)"                  # Group 1: Company name part
            r"[\s.,;()\-\[\]]*"        # Leading separators
            r"(" + regex_core + r")"   # Group 2: Legal form
            r"[\s.,;()\-\[\]]*$",      # Trailing separators
            re.IGNORECASE | re.DOTALL
        )

        match = pattern.match(original_company_name)
        if match:
            company_part = match.group(1).strip()
            form_part = match.group(2).strip()
            normalized_form = re.sub(r'[^A-Z0-9]', '', form_part.upper())
            canonical_form = re.sub(r'[^A-Z0-9]', '', form_upper)
            if normalized_form == canonical_form:
                found_legal_form = form_upper.strip()
                remaining_company_name = company_part.rstrip('.,; ').strip()
                break

    # Fallback for special cases if no legal form found
    if not found_legal_form:
        special_forms = [
            'COMUNIDAD DE PROPIETARIOS', 'COMUNIDAD DE BIENES',
            'ORGANO DE LA ADMINISTRACION', 'ENTIDAD NO LUCRATIVA',
            'CORPORACION LOCAL', 'SUCURSAL EN ESPAÑA', 'PARTIDO POLITICO',
            'ORGANISMO AUTONOMO', 'ENTIDAD NO RESIDENTE', 'ASOCIACION',
            'ASSOCIACIO', 'FUNDACION'
        ]
        for special_form in special_forms:
            if special_form in remaining_company_name:
                found_legal_form = special_form
                break

    return [remaining_company_name, found_legal_form]


def swap_case(text: Optional[str]) -> Optional[str]:
    """Inverts the case of every character in a string.

    Uppercase becomes lowercase and vice versa.

    Args:
        text: The input string.

    Returns:
        The string with swapped case, or None if input is None.

    Example:
        >>> swap_case("Hello World")
        'hELLO wORLD'
        >>> swap_case("PyThOn")
        'pYtHoN'

    Complexity: O(n)
    """
    if text is None:
        return None

    return str(text).swapcase()


def zfill(text: str, width: int) -> str:
    """Pads a string with leading zeros to fill a given width.

    Args:
        text: The input string.
        width: The minimum total width of the result.

    Returns:
        The zero-padded string.

    Example:
        >>> zfill("42", 5)
        '00042'
        >>> zfill("hello", 3)
        'hello'

    Complexity: O(width)
    """
    return str(text).zfill(width)


def rot13(text: str) -> str:
    """Applies the ROT13 substitution cipher to a string.

    Each letter is shifted by 13 positions in the alphabet.
    Applying ROT13 twice returns the original text.

    Args:
        text: The input string.

    Returns:
        The ROT13-encoded string.

    Example:
        >>> rot13("Hello")
        'Uryyb'
        >>> rot13("Uryyb")
        'Hello'

    Complexity: O(n)
    """
    import codecs

    return codecs.encode(str(text), "rot_13")


def camel_to_snake(text: str) -> str:
    """Converts a camelCase or PascalCase string to snake_case.

    Handles sequences of uppercase letters (acronyms) correctly:
    ``"getHTTPResponse"`` becomes ``"get_http_response"``.

    Args:
        text: The camelCase or PascalCase string.

    Returns:
        The snake_case equivalent.

    Example:
        >>> camel_to_snake("camelCase")
        'camel_case'
        >>> camel_to_snake("PascalCase")
        'pascal_case'
        >>> camel_to_snake("getHTTPResponse")
        'get_http_response'
        >>> camel_to_snake("already_snake")
        'already_snake'

    Complexity: O(n)
    """
    # Insert underscore between a lowercase/digit and an uppercase letter
    s = re.sub(r'([a-z0-9])([A-Z])', r'\1_\2', str(text))

    # Insert underscore between an uppercase letter and an uppercase+lowercase sequence
    s = re.sub(r'([A-Z]+)([A-Z][a-z])', r'\1_\2', s)

    return s.lower()


def snake_to_camel(text: str, pascal: bool = False) -> str:
    """Converts a snake_case string to camelCase (or PascalCase).

    Args:
        text: The snake_case string.
        pascal: If True, returns PascalCase (first letter uppercase).
                Defaults to False (camelCase).

    Returns:
        The camelCase or PascalCase equivalent.

    Example:
        >>> snake_to_camel("snake_case")
        'snakeCase'
        >>> snake_to_camel("hello_world", pascal=True)
        'HelloWorld'
        >>> snake_to_camel("already")
        'already'
        >>> snake_to_camel("get_http_response")
        'getHttpResponse'

    Complexity: O(n)
    """
    parts = str(text).split('_')

    if not parts:
        return ''

    if pascal:
        return ''.join(word.capitalize() for word in parts)

    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


def word_wrap(text: str, width: int = 80) -> str:
    """Wraps text to a specified line width, breaking at word boundaries.

    Long words that exceed *width* are kept intact on their own line
    (no mid-word breaks).

    Args:
        text: The input text to wrap.
        width: Maximum number of characters per line. Defaults to 80.

    Returns:
        The wrapped text with newline separators.

    Raises:
        ValueError: If *width* is less than 1.

    Example:
        >>> word_wrap("The quick brown fox jumps over the lazy dog", 20)
        'The quick brown fox\\njumps over the lazy\\ndog'
        >>> word_wrap("short", 80)
        'short'

    Complexity: O(n)
    """
    if width < 1:
        raise ValueError("width must be at least 1.")

    import textwrap

    return textwrap.fill(str(text), width=width)


def format_list_as_sentence(
    items: list[str],
    conjunction: str = "and",
    separator: str = ", ",
) -> str:
    """Formats a list of strings as a human-readable sentence.

    Args:
        items: The list of string items.
        conjunction: Word placed before the last item (e.g. "and", "or", "y").
        separator: Separator between items (default ", ").

    Returns:
        Formatted string joining all items.

    Example:
        >>> format_list_as_sentence(["a", "b", "c"])
        'a, b and c'
        >>> format_list_as_sentence(["x", "y"], conjunction="or")
        'x or y'
        >>> format_list_as_sentence(["only"])
        'only'

    Complexity: O(n)
    """
    if not items:
        return ""

    if len(items) == 1:
        return items[0]

    if len(items) == 2:
        return f"{items[0]} {conjunction} {items[1]}"

    return f"{separator.join(items[:-1])} {conjunction} {items[-1]}"


def pluralize_count(
    count: int,
    singular: str,
    plural: Optional[str] = None,
) -> str:
    """Returns a count with its noun in singular or plural form.

    Args:
        count: The numeric quantity.
        singular: The singular noun (e.g. "item").
        plural: The plural noun. If omitted, appends "s" to *singular*.

    Returns:
        Formatted string like ``"1 item"`` or ``"3 items"``.

    Example:
        >>> pluralize_count(1, "item")
        '1 item'
        >>> pluralize_count(5, "item")
        '5 items'
        >>> pluralize_count(2, "child", "children")
        '2 children'

    Complexity: O(1)
    """
    if plural is None:
        plural = singular + "s"

    return f"{count} {singular}" if count == 1 else f"{count} {plural}"


def format_as_currency(
    number: float, decimals: int = 2, symbol: str = "$"
) -> str:
    """Formats a number as currency text with thousands separator.

    Description:
        Converts a number to a formatted currency string with the given
        symbol, decimal places, and comma-separated thousands.
        Equivalent to Excel DOLLAR.

    Args:
        number: The number to format.
        decimals: Number of decimal places (default 2).
        symbol: Currency symbol to prepend (default '$').

    Returns:
        The formatted currency string.

    Raises:
        TypeError: If number is not numeric or decimals is not an integer.

    Example:
        >>> format_as_currency(1234.567)
        '$1,234.57'
        >>> format_as_currency(1234.567, 0)
        '$1,235'
        >>> format_as_currency(-1234.5, 2, '€')
        '-€1,234.50'

    Complexity: O(n) where n is the number of digits.
    """
    if not isinstance(number, (int, float)):
        raise TypeError("number must be numeric.")

    if not isinstance(decimals, int):
        raise TypeError("decimals must be an integer.")

    negative = number < 0
    abs_number = abs(number)

    if decimals < 0:
        rounded = round(abs_number, decimals)
        formatted = f"{int(rounded):,}"
    elif decimals == 0:
        formatted = f"{round(abs_number):,}"
    else:
        formatted = f"{abs_number:,.{decimals}f}"

    if negative:
        return f"-{symbol}{formatted}"

    return f"{symbol}{formatted}"


def fixed(
    number: Union[int, float],
    decimals: int = 2,
    no_commas: bool = False,
) -> str:
    """Format number with a fixed number of decimal places.

    Description:
        Rounds a number to the given decimal places and returns
        a text string, optionally without thousands separators.
        Equivalent to Excel FIXED.

    Args:
        number: Numeric value to format.
        decimals: Decimal places (default 2).
        no_commas: If True, suppress thousands separators.

    Returns:
        str: Formatted text representation.

    Raises:
        TypeError: If number is not numeric or decimals not int.

    Example:
        >>> fixed(1234567.89, 1)
        '1,234,567.9'
        >>> fixed(1234567.89, 1, True)
        '1234567.9'

    Complexity: O(1)
    """
    if not isinstance(number, (int, float)):
        raise TypeError("number must be numeric.")

    if not isinstance(decimals, int):
        raise TypeError("decimals must be an integer.")

    if decimals < 0:
        rounded = round(number, decimals)
        text = f"{int(rounded)}"
    else:
        text = f"{number:.{decimals}f}"

    if not no_commas:
        # Add thousands separators to integer part
        parts = text.split(".")
        sign = ""

        if parts[0].startswith("-"):
            sign = "-"
            parts[0] = parts[0][1:]

        int_part = parts[0]
        int_part_fmt = f"{int(int_part):,}"

        if len(parts) == 2:
            text = f"{sign}{int_part_fmt}.{parts[1]}"
        else:
            text = f"{sign}{int_part_fmt}"

    return text


def dollar(
    number: Union[int, float],
    decimals: int = 2,
) -> str:
    """Format number as currency text with dollar sign.

    Description:
        Converts a number to text using currency format with
        a dollar sign, commas, and specified decimals.
        Equivalent to Excel DOLLAR.

    Args:
        number: Numeric value to format.
        decimals: Decimal places (default 2).

    Returns:
        str: Dollar-formatted text.

    Raises:
        TypeError: If number is not numeric or decimals not int.

    Example:
        >>> dollar(1234.567)
        '$1,234.57'
        >>> dollar(-1234.567, 1)
        '-$1,234.6'

    Complexity: O(1)
    """
    return format_as_currency(number, decimals)


def format_as_number(
    number: Union[int, float],
    decimals: int = 2,
    use_parens_for_negative: bool = True,
) -> str:
    """Format a number with thousands separators and optional parentheses for negatives.

    Description:
        Rounds the number, adds comma thousands separators, and optionally
        wraps negative values in parentheses instead of using a minus sign.
        Equivalent to VBA ``FormatNumber``.

    Args:
        number: Numeric value to format.
        decimals: Number of decimal places (default 2).
        use_parens_for_negative: Wrap negatives in parentheses (default True).

    Returns:
        Formatted number string.

    Raises:
        TypeError: If number is not numeric or decimals is not an integer.

    Example:
        >>> format_as_number(1234.5678, 2)
        '1,234.57'
        >>> format_as_number(-42.5)
        '(42.50)'
        >>> format_as_number(-42.5, 2, False)
        '-42.50'

    Complexity: O(1)
    """
    if not isinstance(number, (int, float)):
        raise TypeError("number must be numeric.")

    if not isinstance(decimals, int):
        raise TypeError("decimals must be an integer.")

    value = float(number)
    formatted = f"{abs(value):,.{decimals}f}"

    if value < 0 and use_parens_for_negative:
        return f"({formatted})"

    if value < 0:
        return f"-{formatted}"

    return formatted


def format_as_percent(
    number: Union[int, float],
    decimals: int = 2,
    use_parens_for_negative: bool = True,
) -> str:
    """Format a number as a percentage string (multiplied by 100).

    Description:
        Multiplies by 100, rounds to the given decimals, adds a ``%``
        suffix, and optionally uses parentheses for negatives.
        Equivalent to VBA ``FormatPercent``.

    Args:
        number: Numeric value (0.25 → 25%).
        decimals: Number of decimal places (default 2).
        use_parens_for_negative: Wrap negatives in parentheses (default True).

    Returns:
        Formatted percentage string.

    Raises:
        TypeError: If number is not numeric or decimals is not an integer.

    Example:
        >>> format_as_percent(0.25)
        '25.00%'
        >>> format_as_percent(-0.1234, 1)
        '(12.3%)'
        >>> format_as_percent(-0.1234, 1, False)
        '-12.3%'

    Complexity: O(1)
    """
    if not isinstance(number, (int, float)):
        raise TypeError("number must be numeric.")

    if not isinstance(decimals, int):
        raise TypeError("decimals must be an integer.")

    value = float(number) * 100
    formatted = f"{abs(value):,.{decimals}f}%"

    if value < 0 and use_parens_for_negative:
        return f"({formatted})"

    if value < 0:
        return f"-{formatted}"

    return formatted


def format_with_pattern(value, pattern: str) -> str:
    """Format a numeric or date value using an Excel/VBA-style pattern.

    Supports common patterns including percentage (``"%"``), thousands
    separator (``"#,##0"``), fixed decimals (``"0.00"``), and date/time
    patterns (``"yyyy-mm-dd"``, ``"hh:nn:ss"``, etc.).

    Args:
        value: Numeric value (int/float) or ``datetime`` object.
        pattern: Excel/VBA format string.

    Returns:
        Formatted string representation of *value*.

    Example:
        >>> format_with_pattern(1234.5, "#,##0.00")
        '1,234.50'
        >>> format_with_pattern(0.75, "0%")
        '75%'
        >>> from datetime import datetime
        >>> format_with_pattern(datetime(2025, 3, 15), "yyyy-mm-dd")
        '2025-03-15'

    Complexity: O(n) where n is the length of *pattern*.
    """
    from datetime import datetime as _dt

    if isinstance(value, _dt):
        fmt_map = {
            "yyyy": "%Y", "yy": "%y",
            "mm": "%m", "dd": "%d",
            "hh": "%H", "nn": "%M", "ss": "%S",
        }
        result = pattern.lower()

        for token, py_fmt in fmt_map.items():
            result = result.replace(token, py_fmt)

        return value.strftime(result)

    try:
        num = float(value)
    except (ValueError, TypeError):
        return str(value)

    if "%" in pattern:
        dec = max(pattern.count("0") - 1, 0)
        return f"{num * 100:.{dec}f}%"

    if "#,##0" in pattern or "0,0" in pattern:
        dec = 0

        if "." in pattern:
            dec = pattern.split(".")[-1].count("0")

        return f"{num:,.{dec}f}"

    if "0." in pattern:
        dec = pattern.split(".")[-1].count("0")
        return f"{num:.{dec}f}"

    return str(num)


def format_file_size(size_bytes: int | float, binary: bool = True) -> str:
    """Convert a byte count to a human-readable file-size string.

    Args:
        size_bytes: Number of bytes (non-negative).
        binary: If True use IEC binary units (KiB, MiB, …) with 1024 base;
                if False use SI decimal units (KB, MB, …) with 1000 base.

    Returns:
        Human-readable string, e.g. ``"1.50 GiB"`` or ``"1.50 GB"``.

    Raises:
        TypeError: If *size_bytes* is not numeric.
        ValueError: If *size_bytes* is negative.

    Example:
        >>> format_file_size(1536)
        '1.50 KiB'
        >>> format_file_size(1500, binary=False)
        '1.50 KB'

    Complexity: O(1)
    """
    if not isinstance(size_bytes, (int, float)):
        raise TypeError("size_bytes must be numeric")

    if size_bytes < 0:
        raise ValueError("size_bytes must be non-negative")

    if binary:
        base = 1024
        suffixes = ["B", "KiB", "MiB", "GiB", "TiB", "PiB", "EiB"]
    else:
        base = 1000
        suffixes = ["B", "KB", "MB", "GB", "TB", "PB", "EB"]

    value = float(size_bytes)

    for suffix in suffixes[:-1]:

        if abs(value) < base:
            return f"{value:.2f} {suffix}" if suffix != "B" else f"{int(value)} B"

        value /= base

    return f"{value:.2f} {suffixes[-1]}"
