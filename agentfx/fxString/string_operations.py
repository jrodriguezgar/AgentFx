"""String Operations and Manipulation Functions.

This module provides a comprehensive set of functions for string manipulation
and operations. It includes utilities for extracting, splitting, joining,
transforming, and analyzing strings in various ways.

Key Features:
- Character and word counting
- Substring extraction and manipulation
- Position finding and pattern matching
- String splitting and joining
- Number extraction from strings
- Content extraction between delimiters
- String cleaning and formatting
- Word manipulation and reordering

"""

from typing import Optional, Dict, List, Iterable
import re
import unicodedata
import difflib
import random
import string

from agentfx.fxString.string_convertions import (
    code_from_char as _core_code_from_char,
    char_from_code as _core_char_from_code,
)
from agentfx.fxString.string_caseconv import to_slug as _core_to_slug


# Pre-compiled regex patterns for optimization
_RE_WHITESPACE = re.compile(r'\s+')
_RE_WORD_BOUNDARY = re.compile(r'\b\w+\b')
_RE_NUMBER_PATTERN = re.compile(r'[-+]?\d*\.\d+|[-+]?\d+')
_RE_DIGITS = re.compile(r'\d')
_RE_NON_ALPHANUMERIC = re.compile(r'[^a-zA-Z0-9\s]')


DELIMITERS = {
    '/* */': (r'/\*', r'\*/'),  # C-style comments (e.g., /* comment */)
    '()': (r'\(', r'\)'),  # Parentheses (e.g., (content))
    '[]': (r'\[', r'\]'),  # Square brackets (e.g., [content])
    '{}': (r'\{', r'\}'),  # Curly braces (e.g., {content})
    '<>': (r'<', r'>'),  # Angle brackets (e.g., <tag>)
    '""': (r'"', r'"'),  # Double quotes (e.g., "text")
    "''": (r"'", r"'"),  # Single quotes (e.g., 'text')
    '$$': (r'\$\$', r'\$\$')  # Double dollar signs (e.g., $$math$$ in LaTeX)
}


# Default punctuation and separator pattern for word splitting, reusable in other functions
_DEFAULT_WORD_SEPARATORS = rf"[{re.escape(string.punctuation)}§¿¡«»‹›‘’“”„†‡°€¥£¢₽₹〒〶〴〵—–—~`\s]+"


def ascii_from_char(character: str) -> int:
    """
    Devuelve el valor entero (código Unicode/ASCII) del primer carácter de una cadena.

    Args:
        character (str): La cadena de la que se obtendrá el valor entero del primer carácter.
                         Solo se considera el primer carácter si la cadena tiene más de uno.

    Returns:
        int: El valor entero correspondiente al carácter.

    Raises:
        TypeError: Si la entrada no es una cadena.
        ValueError: Si la cadena de entrada está vacía.

    Ejemplos de uso:
        >>> ascii_from_char("A")
        65
        >>> ascii_from_char("a")
        97
        >>> ascii_from_char(" ")
        32
        >>> ascii_from_char("€") # Carácter Unicode
        8364
        >>> ascii_from_char("Python") # Solo toma el primer carácter 'P'
        80

    **Cost:** O(1), constant time operation
    """
    if not isinstance(character, str):
        raise TypeError("La entrada debe ser una cadena de texto (str).")
    if not character:  # Comprueba si la cadena está vacía
        raise ValueError("La cadena de entrada no puede estar vacía.")

    return _core_code_from_char(character)


def char_from_ascii(integer_code: int) -> str:
    """
    Devuelve el carácter correspondiente a un valor entero (código Unicode/ASCII).

    Args:
        integer_code (int): El valor entero (código Unicode/ASCII) del carácter deseado.
                            Debe ser un valor Unicode válido (0 a 1,114,111).

    Returns:
        str: El carácter correspondiente al valor entero.

    Raises:
        TypeError: Si la entrada no es un entero.
        ValueError: Si el entero está fuera del rango de los códigos Unicode válidos.

    Ejemplos de uso:
        >>> char_from_ascii(65)
        'A'
        >>> char_from_ascii(97)
        'a'
        >>> char_from_ascii(32)
        ' '
        >>> char_from_ascii(8364) # Carácter Euro
        '€'
        >>> char_from_ascii(100000) # Un carácter Unicode menos común
        '𖠀'
    """
    if not isinstance(integer_code, int):
        raise TypeError("La entrada debe ser un entero.")

    try:
        return _core_char_from_code(integer_code)
    except (TypeError, ValueError) as e:
        raise ValueError(f"El valor entero está fuera del rango de códigos Unicode válidos: {e}")
    

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

        >>> count_characters("", "a")
        0
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


def position_in_string(main_string: str, substring: str, start_position: int = 1) -> list[int]:
    """
    Devuelve una lista de todas las posiciones (basadas en 1) donde se encuentra una subcadena
    dentro de otra cadena, comenzando la búsqueda desde una posición especificada.

    Args:
        main_string (str): La cadena principal donde se realizará la búsqueda.
        substring (str): La subcadena que se desea encontrar.
        start_position (int, opcional): La posición (basada en 1) donde se inicia la búsqueda.
                                        Debe ser un entero positivo. Por defecto es 1.
                                        Si la posición de inicio es mayor que la longitud de la cadena,
                                        se devuelve una lista vacía.

    Returns:
        list[int]: Una lista de enteros que representa las posiciones (basadas en 1)
                   donde se encontró la subcadena. La lista estará vacía si no se encuentra
                   la subcadena o si 'start_position' es inválida.

    Raises:
        TypeError: Si 'main_string' o 'substring' no son cadenas, o si 'start_position' no es un entero.

    Ejemplos de uso:
        >>> position_in_string("banana", "a")
        [2, 4, 6]
        >>> position_in_string("ababa", "aba")
        [1, 3]
        >>> position_in_string("Mississippi", "ss")
        [3, 6]
        >>> position_in_string("Hello World World", "World")
        [7, 13]
        >>> position_in_string("Hello World World", "World", 8) # Busca desde la posición 8
        [13]
        >>> position_in_string("Programming is fun, programming is great", "is")
        [13, 36]
        >>> position_in_string("banana", "ana", 3) # Busca desde la posición 3
        [4]
        >>> position_in_string("programming", "z") # Subcadena no encontrada
        []
        >>> position_in_string("test", "test", 5) # start_position fuera de rango
        []
        >>> position_in_string("abc", "abcdef") # Subcadena más larga
        []
        >>> position_in_string("hola", "h", 0) # start_position inválida, se maneja como fuera de rango efectivo
        []
    """
    if not isinstance(main_string, str):
        raise TypeError("El argumento 'main_string' debe ser una cadena.")
    if not isinstance(substring, str):
        raise TypeError("El argumento 'substring' debe ser una cadena.")
    if not isinstance(start_position, int):
        raise TypeError("El argumento 'start_position' debe ser un entero.")

    # Si la subcadena es vacía, o si la subcadena es más larga que la cadena principal,
    # o si la posición de inicio es mayor que la longitud de la cadena principal,
    # no hay coincidencias válidas.
    if not substring or len(substring) > len(main_string) or start_position > len(main_string):
        return []
    
    # Ajustar la posición de inicio a base 0 para Python.
    # Si start_position es 0 o negativo, lo tratamos como 1 (índice 0).
    current_search_index = max(0, start_position - 1)
    
    found_positions = []
    
    while current_search_index < len(main_string):
        # Busca la subcadena desde el current_search_index
        found_at_index = main_string.find(substring, current_search_index)
        
        if found_at_index == -1:
            # Si no se encuentra más, salimos del bucle
            break
        else:
            # Se encontró, agregamos la posición basada en 1 a la lista
            found_positions.append(found_at_index + 1)
            
            # Movemos el índice de búsqueda para evitar encontrar la misma subcadena
            # en la misma posición (si la subcadena no tiene solapamiento consigo misma)
            # Para subcadenas solapadas (ej. "aba" en "ababa"), el comportamiento de find()
            # es encontrar la primera ocurrencia y luego continuar la búsqueda *después* de esa ocurrencia.
            # Para asegurar que encontramos todas las ocurrencias, incluso si se solapan,
            # debemos avanzar el índice de búsqueda en solo 1 posición si la subcadena tiene longitud 1.
            # Si la subcadena es más larga, avanzamos el índice por 1.
            # (Ej. "ababa", buscar "aba". found_at_index=0. Siguiente búsqueda desde índice 1).
            # Para el comportamiento tradicional de InStr (no solapamiento en la misma posición),
            # avanzaríamos found_at_index + len(substring).
            # Pero para encontrar TODAS las ocurrencias, incluso solapadas, avanzamos solo 1 posición.
            current_search_index = found_at_index + 1
            # Si la subcadena es vacía (ya manejado arriba), esto crearía un bucle infinito.

    return found_positions


def position_in_string_reverse(main_string: str, substring: str, start_position: int = -1) -> list[int]:
    """
    Devuelve una lista de todas las posiciones (basadas en 1) donde se encuentra una subcadena
    dentro de otra cadena, buscando de derecha a izquierda desde una posición especificada.
    Las posiciones en la lista se devuelven en orden descendente.

    Args:
        main_string (str): La cadena principal donde se realizará la búsqueda.
        substring (str): La subcadena que se desea encontrar.
        start_position (int, opcional): La posición (basada en 1) desde la que se inicia la búsqueda
                                        hacia atrás. Un valor de -1 (predeterminado) o un valor
                                        mayor que la longitud de la cadena, significa que la búsqueda
                                        comienza desde el final de la cadena.
                                        Debe ser un entero positivo o -1.

    Returns:
        list[int]: Una lista de enteros que representa las posiciones (basadas en 1)
                   donde se encontró la subcadena. La lista estará vacía si no se encuentra
                   la subcadena o si 'start_position' es inválida. Las posiciones se ordenan
                   de forma descendente (de derecha a izquierda).

    Raises:
        TypeError: Si 'main_string' o 'substring' no son cadenas, o si 'start_position' no es un entero.

    Ejemplos de uso:
        >>> position_in_string_reverse("banana", "a")
        [6, 4, 2]
        >>> position_in_string_reverse("ababa", "aba")
        [3, 1]
        >>> position_in_string_reverse("Mississippi", "ss")
        [6, 3]
        >>> position_in_string_reverse("Hello World World", "World")
        [13, 7]
        >>> position_in_string_reverse("Hello World World", "World", 10) # Busca hacia atrás desde la posición 10
        [7]
        >>> position_in_string_reverse("Programming is fun, programming is great", "is")
        [36, 13]
        >>> position_in_string_reverse("banana", "ana", 3) # Busca hacia atrás desde la posición 3
        [2]
        >>> position_in_string_reverse("programming", "z") # Subcadena no encontrada
        []
        >>> position_in_string_reverse("test", "test", 0) # start_position inválida
        []
        >>> position_in_string_reverse("abc", "abcdef") # Subcadena más larga
        []
    """
    if not isinstance(main_string, str):
        raise TypeError("El argumento 'main_string' debe ser una cadena.")
    if not isinstance(substring, str):
        raise TypeError("El argumento 'substring' debe ser una cadena.")
    if not isinstance(start_position, int):
        raise TypeError("El argumento 'start_position' debe ser un entero.")

    # Si la subcadena es vacía, o más larga que la cadena principal,
    # no hay coincidencias válidas.
    if not substring or len(substring) > len(main_string):
        return []
    
    found_positions = []

    # Ajustar el punto de inicio para la búsqueda inversa de Python.
    # rfind(sub, start, end) busca en slice[start:end]. 'end' es exclusivo.
    # Queremos buscar desde 'start_position' (basada en 1) hacia el principio de la cadena.
    # El 'end' para rfind debería ser start_position_base_0 + 1.
    if start_position == -1 or start_position > len(main_string):
        # Si -1 o más allá del final, busca en toda la cadena.
        # rfind(sub, 0, None) busca en toda la cadena desde el final.
        current_end_index_for_rfind = len(main_string) 
    elif start_position <= 0:
        # En VBA, un start_position <= 0 podría generar un error. Aquí devolvemos una lista vacía.
        return []
    else:
        # start_position es un índice basado en 1, lo convertimos a un índice basado en 0
        # y ese será el límite superior (exclusivo) para la búsqueda de rfind.
        current_end_index_for_rfind = start_position 
        
    # Python rfind(sub, start, end) busca en [start:end].
    # Para buscar desde el final hacia una posición específica, 'end' es el límite derecho (exclusivo).
    # 'start' es el límite izquierdo (inclusivo). Lo ponemos a 0 para buscar en toda la porción.
    search_start_limit = 0 
    
    # Bucle para encontrar todas las ocurrencias en orden inverso
    while True:
        # rfind busca la última ocurrencia en el segmento [search_start_limit : current_end_index_for_rfind]
        found_at_index = main_string.rfind(substring, search_start_limit, current_end_index_for_rfind)
        
        if found_at_index == -1:
            # Si no se encuentra más, salimos del bucle
            break
        else:
            # Se encontró, agregamos la posición basada en 1 a la lista
            found_positions.append(found_at_index + 1)
            
            # Para la siguiente iteración, ajustamos el límite de búsqueda.
            # La nueva búsqueda debe terminar justo antes del inicio de la ocurrencia que acabamos de encontrar.
            # Si la subcadena tiene longitud 1, necesitamos avanzar el límite en 1 para evitar un bucle infinito.
            # Esto es para manejar casos como "aaaa" buscando "a", donde siempre encontraría la misma 'a'
            # si el límite no se reduce.
            current_end_index_for_rfind = found_at_index 
            if substring: # Si substring no es vacía
                 current_end_index_for_rfind = found_at_index # Avanzamos el final para la próxima búsqueda

    return found_positions


def random_string(length: int = 10, secure: bool = True) -> str:
    """
    Generates a random string of a specified length.

    This function creates a random string using a combination of ASCII letters,
    digits, and punctuation characters. It can use either a cryptographically
    secure random number generator or a less secure, faster one, depending
    on the 'secure' flag.

    Args:
        length (int): The desired length of the generated string.
                      Defaults to 10 characters.
        secure (bool): If True, uses 'random.SystemRandom()' for cryptographic
                       security. If False, uses 'random.choices()' for
                       faster but less secure generation. Defaults to True.

    Returns:
        str: A randomly generated string.

    Raises:
        ValueError: If 'length' is less than 0.

    Example of use:
        >>> random_string(length=16, secure=True)
        'aBc1@EfG2#IjK3$LmN4' # Example output, actual output will vary
    """
    if length < 0:
        raise ValueError("String length cannot be negative.")

    # Combine all possible characters for string generation.
    # Using 'string' constants ensures we cover common character sets
    # and avoids manual string definition.
    all_characters = string.ascii_letters + string.digits + string.punctuation

    if secure:
        # Use SystemRandom for cryptographic security, suitable for
        # sensitive data like passwords or tokens.
        random_generator = random.SystemRandom()
    else:
        # Use the default random.choices for faster generation when
        # cryptographic security isn't required.
        random_generator = random

    # Efficiently join selected characters into a single string.
    # The 'choices' method is preferred for selecting multiple items
    # with replacement from a sequence.
    return ''.join(random_generator.choices(all_characters, k=length))

    
def reverse_string(input_string: str) -> str:
    """
    Invierte una cadena de texto.

    Esta función toma una cadena de entrada y devuelve una nueva cadena
    con los caracteres en orden inverso.

    Args:
        input_string (str): La cadena de texto que se desea invertir.

    Returns:
        str: La cadena invertida.

    Raises:
        TypeError: Si la entrada no es una cadena de texto.

    Ejemplos de uso:
        >>> reverse_string("hola")
        'aloh'
        >>> reverse_string("Python")
        'nohtyP'
        >>> reverse_string("12345")
        '54321'
        >>> reverse_string("")
        ''
        >>> reverse_string("programación")
        'nóicamargorp'
    """
    if not isinstance(input_string, str):
        raise TypeError("La entrada debe ser una cadena de texto (str).")

    # Utiliza el slicing de cadenas para invertirla.
    # [::-1] crea una copia invertida de la cadena.
    return input_string[::-1]


def replace_string(original_string: str, old_substring: str, new_substring: str) -> str:
    """
    Reemplaza todas las ocurrencias de una subcadena en una cadena con otra subcadena.

    Args:
        original_string (str): La cadena original en la que se realizará el reemplazo.
        old_substring (str): La subcadena que se buscará y reemplazará.
        new_substring (str): La subcadena con la que se reemplazarán las ocurrencias.

    Returns:
        str: La nueva cadena con las subcadenas reemplazadas.

    Raises:
        TypeError: Si 'original_string', 'old_substring' o 'new_substring' no son cadenas.

    Ejemplos de uso:
        >>> replace_string("Hola mundo", "mundo", "Python")
        'Hola Python'
        >>> replace_string("uno dos uno tres", "uno", "diez")
        'diez dos diez tres'
        >>> replace_string("abcabc", "b", "xyz")
        'axyzcAxyzc'
        >>> replace_string("Sin cambios", "no existe", "nada")
        'Sin cambios'
        >>> replace_string("AAA", "A", "B")
        'BBB'
    """
    if not isinstance(original_string, str):
        raise TypeError("El argumento 'original_string' debe ser una cadena.")
    if not isinstance(old_substring, str):
        raise TypeError("El argumento 'old_substring' debe ser una cadena.")
    if not isinstance(new_substring, str):
        raise TypeError("El argumento 'new_substring' debe ser una cadena.")

    return original_string.replace(old_substring, new_substring)


def replace_first_occurrence(
    text: Optional[str],
    old_substring: str,
    new_substring: str
) -> Optional[str]:
    """
    Replaces only the first occurrence of a specified substring within a string.

    Args:
        text (Optional[str]): The input string. Can be None.
        old_substring (str): The substring to search for and replace.
        new_substring (str): The substring to replace 'old_substring' with.

    Returns:
        Optional[str]: The string with the first occurrence replaced, or None if the input 'text' was None.
                       Returns the original string if 'old_substring' is not found.

    Example:
        replace_first_occurrence("apple banana apple", "apple", "orange") # Returns "orange banana apple"
        replace_first_occurrence("one two three", "two", "2")             # Returns "one 2 three"
        replace_first_occurrence("no_match", "xyz", "abc")                # Returns "no_match"
        replace_first_occurrence(None, "a", "b")                          # Returns None
    """
    if text is None:
        return None
    if not isinstance(text, str):
        # Convert to string if it's not, or raise TypeError for stricter validation.
        text = str(text)
    if not isinstance(old_substring, str) or not isinstance(new_substring, str):
        raise TypeError("old_substring and new_substring must be strings.")

    # Python's str.replace(old, new, count) method is perfect for this.
    # Setting count=1 ensures only the first match is replaced.
    return text.replace(old_substring, new_substring, 1)


def replace_last_occurrence(
    text: Optional[str],
    old_substring: str,
    new_substring: str
) -> Optional[str]:
    """
    Replaces only the last occurrence of a specified substring within a string.

    Args:
        text (Optional[str]): The input string. Can be None.
        old_substring (str): The substring to search for and replace.
        new_substring (str): The substring to replace 'old_substring' with.

    Returns:
        Optional[str]: The string with the last occurrence replaced, or None if the input 'text' was None.
                       Returns the original string if 'old_substring' is not found.

    Example:
        replace_last_occurrence("apple banana apple", "apple", "orange") # Returns "apple banana orange"
        replace_last_occurrence("one two three", "two", "2")             # Returns "one 2 three"
        replace_last_occurrence("no_match", "xyz", "abc")                # Returns "no_match"
        replace_last_occurrence(None, "a", "b")                          # Returns None
    """
    if text is None:
        return None
    if not isinstance(text, str):
        text = str(text)
    if not isinstance(old_substring, str) or not isinstance(new_substring, str):
        raise TypeError("old_substring and new_substring must be strings.")

    # Find the index of the last occurrence of old_substring
    last_index = text.rfind(old_substring)

    # If old_substring is not found, return the original string
    if last_index == -1:
        return text

    # Reconstruct the string by combining the part before the last occurrence,
    # the new substring, and the part after the last occurrence.
    return text[:last_index] + new_substring + text[last_index + len(old_substring):]


def replace_by_position(
    original_string: str,
    start_position: int,
    num_chars: int,
    new_text: str
) -> str:
    """
    Replaces a segment of a string defined by position and length with new text.

    Equivalent to Excel's REPLACE function. Uses 1-based indexing.

    Args:
        original_string (str): The original string in which the replacement will be made.
        start_position (int): The 1-based position of the first character to replace.
        num_chars (int): The number of characters to replace from start_position.
        new_text (str): The text to insert in place of the removed segment.

    Returns:
        str: The resulting string after the positional replacement.

    Raises:
        TypeError: If original_string or new_text is not str, or if start_position/num_chars is not int.
        ValueError: If start_position < 1 or num_chars < 0.

    Usage Example:
        >>> replace_by_position("abcdefghijk", 6, 5, "*")
        'abcde*k'
        >>> replace_by_position("2024", 3, 2, "25")
        '2025'
        >>> replace_by_position("Hello World", 1, 5, "Goodbye")
        'Goodbye World'

    **Cost:** O(n), where n is the length of original_string.
    """
    if not isinstance(original_string, str):
        raise TypeError("El argumento 'original_string' debe ser una cadena.")

    if not isinstance(new_text, str):
        raise TypeError("El argumento 'new_text' debe ser una cadena.")

    if not isinstance(start_position, int) or not isinstance(num_chars, int):
        raise TypeError("'start_position' y 'num_chars' deben ser enteros.")

    if start_position < 1:
        raise ValueError("'start_position' debe ser >= 1.")

    if num_chars < 0:
        raise ValueError("'num_chars' debe ser >= 0.")

    # Convert 1-based to 0-based indexing
    start_idx = start_position - 1
    end_idx = start_idx + num_chars

    return original_string[:start_idx] + new_text + original_string[end_idx:]


def regex_replace(
    text: str,
    pattern: str,
    replacement: str,
    case_insensitive: bool = False
) -> str:
    """
    Replaces all occurrences matching a regular expression pattern with a replacement string.

    Equivalent to Excel's REGEXREPLACE function. Supports backreferences
    in the replacement string (e.g., ``\\1``, ``\\g<name>``).

    Args:
        text (str): The input string to modify.
        pattern (str): The regular expression pattern to match.
        replacement (str): The replacement string. Supports regex backreferences.
        case_insensitive (bool): If True, the pattern matching ignores case. Defaults to False.

    Returns:
        str: The text with all matching occurrences replaced.

    Raises:
        TypeError: If text, pattern, or replacement is not a string.
        re.error: If the pattern is not a valid regular expression.

    Usage Example:
        >>> regex_replace("Hello 123 World 456", r"\\d+", "X")
        'Hello X World X'
        >>> regex_replace("test@email.com", r"@.*", "@example.com")
        'test@example.com'
        >>> regex_replace("FooBar FooBaz", r"foo", "QUX", case_insensitive=True)
        'QUXBar QUXBaz'

    **Cost:** O(n*m), where n is text length and m is pattern complexity.
    """
    if not isinstance(text, str):
        raise TypeError("El argumento 'text' debe ser una cadena.")

    if not isinstance(pattern, str):
        raise TypeError("El argumento 'pattern' debe ser una cadena.")

    if not isinstance(replacement, str):
        raise TypeError("El argumento 'replacement' debe ser una cadena.")

    flags = re.IGNORECASE if case_insensitive else 0

    return re.sub(pattern, replacement, text, flags=flags)


def truncate_string(
    input_string: Optional[str],
    target_length: int = 255,
    align: str = 'right'
) -> Optional[str]:
    """Truncates a string to a specified target length from the left or right.

    If the `input_string`'s length exceeds `target_length`, it is shortened.
    The `align` parameter dictates which part of the string is preserved.

    Args:
        input_string: The string to be truncated. Can be None.
        target_length: The desired maximum length of the string. Must be a non-negative integer.
        align: The alignment for truncation.
               'left' to truncate from the left (keeping the right part of the string).
               'right' to truncate from the right (keeping the left part of the string).
               Defaults to 'right'.

    Returns:
        Optional[str]: The truncated string. Returns the original string if its length
                       is within the limit, or if `input_string` is None.

    Raises:
        ValueError: If `target_length` is negative.
        ValueError: If `align` is not 'left' or 'right'.

    Example of use:
        >>> truncate_string("abcdefg", 5)
        'abcde'
        >>> truncate_string("abcdefg", 5, align='left')
        'cdefg'
        >>> truncate_string("short", 10)
        'short'
        >>> truncate_string(None, 5)
        None
        >>> truncate_string("long string", 0)
        ''
        >>> truncate_string("another long string", 7, align='right')
        'another'
        >>> truncate_string("another long string", 7, align='left')
        'string'
    """
    # Why: Validate parameters early to prevent incorrect behavior or silent errors.
    if target_length < 0:
        raise ValueError("target_length must be a non-negative integer.")

    # Why: Ensure `align` is one of the supported values.
    if align not in ['left', 'right']:
        raise ValueError("align must be 'left' or 'right'.")

    # Why: Handle the edge case where input_string is None, returning None directly.
    if input_string is None:
        return None

    # Why: Convert input to string type to ensure consistent string operations.
    current_string = str(input_string)
    string_length = len(current_string)

    # Why: If the string's current length is already within the target, no truncation is needed.
    if string_length <= target_length:
        return current_string

    # Why: Perform truncation based on the specified alignment using slicing.
    # String slicing `s[start:end]` is efficient and Pythonic.
    if align == 'right':
        # Keep characters from the beginning up to `target_length`.
        return current_string[:target_length]
    else:  # align == 'left'
        # Keep characters from `string_length - target_length` to the end.
        return current_string[string_length - target_length:]


def substring(original_string: str, start_position: int, length: int) -> str:
    """
    Extrae una subcadena de una cadena a partir de una posición inicial y con una longitud específica.

    Args:
        original_string (str): La cadena de la que se extraerá la subcadena.
        start_position (int): La posición inicial desde la que se comenzará la extracción.
                              Las posiciones se basan en 1 (el primer carácter es 1).
                              Si 'start_position' es 0 o negativo, se ajusta a 1.
                              Si 'start_position' es mayor que la longitud de la cadena,
                              se devolverá una cadena vacía.
        length (int): La longitud de la subcadena a extraer.
                      Si 'length' es negativo, se tratará como 0.
                      Si la longitud excede el final de la cadena, se extraerá hasta el final.

    Returns:
        str: La subcadena extraída.

    Raises:
        TypeError: Si 'original_string' no es una cadena, o 'start_position' o 'length' no son enteros.

    Ejemplos de uso:
        >>> substring("Python Programacion", 1, 6) # "Python"
        'Python'
        >>> substring("Python Programacion", 8, 4) # "Prog"
        'Prog'
        >>> substring("Hola Mundo", 6, 5) # "Mundo"
        'Mundo'
        >>> substring("Ejemplo", 3, 10) # Desde el 3er caracter, hasta el final
        'emplo'
        >>> substring("Corto", 10, 5) # start_position fuera de rango
        ''
        >>> substring("Test", 1, 0) # length es 0
        ''
        >>> substring("ABC", 1, -2) # length es negativo
        ''
        >>> substring("XYZ", -5, 2) # start_position negativo (se ajusta a 1)
        'XY'
    """
    if not isinstance(original_string, str):
        raise TypeError("El argumento 'original_string' debe ser una cadena.")
    if not isinstance(start_position, int):
        raise TypeError("El argumento 'start_position' debe ser un entero.")
    if not isinstance(length, int):
        raise TypeError("El argumento 'length' debe ser un entero.")

    # Ajustar start_position a base 0 para Python y manejar valores <= 0
    # Si start_position es 1, el índice en Python es 0.
    # Si start_position es 0 o negativo, lo ajustamos a 1 (índice 0).
    actual_start_index = max(0, start_position - 1)

    # Manejar length negativo
    actual_length = max(0, length)

    # Si la posición de inicio efectiva ya está fuera de la cadena, devuelve una cadena vacía
    if actual_start_index >= len(original_string):
        return ""

    # Calcular el índice final (exclusivo)
    end_index = actual_start_index + actual_length

    # Realizar el slicing
    return original_string[actual_start_index:end_index]


def right_substring(original_string: str, num_chars: int) -> str:
    """
    Extrae un número especificado de caracteres del final de una cadena.

    Args:
        original_string (str): La cadena de la que se extraerán los caracteres.
        num_chars (int): El número de caracteres a extraer desde el final.
                         Si 'num_chars' es mayor que la longitud de la cadena,
                         se devolverá la cadena completa. Si es negativo, se tratará como 0.

    Returns:
        str: La subcadena extraída del final.

    Raises:
        TypeError: Si 'original_string' no es una cadena o 'num_chars' no es un entero.

    Ejemplos de uso:
        >>> right_substring("Python", 3)
        'hon'
        >>> right_substring("Programacion", 6)
        'macion'
        >>> right_substring("Hola", 10) # num_chars > longitud
        'Hola'
        >>> right_substring("Ejemplo", 0)
        ''
        >>> right_substring("Test", -5) # num_chars negativo
        ''
    """
    if not isinstance(original_string, str):
        raise TypeError("El argumento 'original_string' debe ser una cadena.")
    if not isinstance(num_chars, int):
        raise TypeError("El argumento 'num_chars' debe ser un entero.")

    if num_chars <= 0:
        return ""
    
    # El slicing [:-num_chars] significa "desde el principio hasta los últimos num_chars"
    # El slicing [-num_chars:] significa "los últimos num_chars hasta el final"
    return original_string[-num_chars:]


def left_substring(original_string: str, num_chars: int) -> str:
    """
    Extrae un número especificado de caracteres del principio de una cadena.

    Args:
        original_string (str): La cadena de la que se extraerán los caracteres.
        num_chars (int): El número de caracteres a extraer desde el principio.
                         Si 'num_chars' es mayor que la longitud de la cadena,
                         se devolverá la cadena completa. Si es negativo, se tratará como 0.

    Returns:
        str: La subcadena extraída del principio.

    Raises:
        TypeError: Si 'original_string' no es una cadena o 'num_chars' no es un entero.

    Ejemplos de uso:
        >>> left_substring("Python", 3)
        'Pyt'
        >>> left_substring("Programacion", 6)
        'Progra'
        >>> left_substring("Hola", 10) # num_chars > longitud
        'Hola'
        >>> left_substring("Ejemplo", 0)
        ''
        >>> left_substring("Test", -5) # num_chars negativo
        ''
    """
    if not isinstance(original_string, str):
        raise TypeError("El argumento 'original_string' debe ser una cadena.")
    if not isinstance(num_chars, int):
        raise TypeError("El argumento 'num_chars' debe ser un entero.")

    if num_chars <= 0:
        return ""

    # El slicing [:num_chars] significa "desde el principio hasta el índice num_chars (excluido)"
    return original_string[:num_chars]


def common_substring(string1: str, string2: str, min_longest_substring: int = 4) -> str:
    """Finds the longest common substring between two input strings, ignoring case,
    and ensures the substring is at least the length of the shortest word in either string.

    This function uses a dynamic programming approach to determine the longest
    contiguous sequence of characters that is common to both `string1` and `string2`.
    The comparison is case-insensitive. If no common substring is found, or if
    the found substring is shorter than the shortest word in either input string,
    an empty string is returned.

    Args:
        string1: The first input string.
        string2: The second input string.

    Returns:
        The longest common substring that meets the minimum length requirement.
        Returns an empty string if no common substring exists, if either input string
        is empty, or if the found substring is shorter than the shortest word.

    Raises:
        TypeError: If either `string1` or `string2` is not a string.

    Example of use:
        >>> common_substring("abcdef", "zbcdexy")
        "BCDE"

        >>> common_substring("Hello World", "world cup")
        "WORLD"

        >>> common_substring("apple", "banana")
        "" # 'a' is shorter than 'apple' or 'banana'

        >>> common_substring("test", "no match")
        ""

        >>> common_substring("", "abc")
        ""

        >>> common_substring("LongerExample", "a longer example phrase")
        "LONGEREXAMPLE" # "LONGER" is the common substring, but "LONGEREXAMPLE" is not the common string. It is not longer than "LongerExample" or "longer".

        >>> common_substring("test string", "another test phrase")
        "TEST"
    """
    # Validate input types to ensure both are strings.
    if not isinstance(string1, str) or not isinstance(string2, str):
        return ''

    # Return an empty string immediately if either input string is empty.
    # This avoids unnecessary computation for edge cases.
    if not string1 or not string2:
        return ''

    # Convert strings to uppercase for case-insensitive comparison.
    # This simplifies the comparison logic within the loop.
    upper_string1 = string1.upper()
    upper_string2 = string2.upper()

    len_string1 = len(upper_string1)
    len_string2 = len(upper_string2)

    # Initialize a 2D DP array. `dp[i][j]` will store the length of the longest
    # common suffix of `upper_string1[0...i-1]` and `upper_string2[0...j-1]`.
    # Each cell represents the length of the common substring ending at that point.
    dp = [[0] * (len_string2 + 1) for _ in range(len_string1 + 1)]

    # Variables to track the maximum length found and its ending position in string1.
    longest_substring_length = 0
    end_index_in_string1 = 0

    # Iterate through both strings using dynamic programming.
    # We start from 1 because `dp` array is 1-indexed relative to string characters.
    for i in range(1, len_string1 + 1):
        for j in range(1, len_string2 + 1):
            # If characters match, increment the length of the common suffix
            # from the diagonally previous cell.
            if upper_string1[i - 1] == upper_string2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

                # Update the longest common substring found so far.
                # We also store the ending index in `upper_string1` to easily
                # extract the substring later.
                if dp[i][j] > longest_substring_length:
                    longest_substring_length = dp[i][j]
                    end_index_in_string1 = i
            else:
                # If characters don't match, the common suffix is broken,
                # so the length resets to 0 at this point.
                dp[i][j] = 0

    # Calculate the minimum word length from both strings.
    # We use regex to split by non-alphanumeric characters to get distinct words.
    words1 = _RE_WORD_BOUNDARY.findall(string1)
    words2 = _RE_WORD_BOUNDARY.findall(string2)

    all_words = words1 + words2
    min_word_length = 0
    if all_words:  # Ensure there are words to avoid error on empty list
        # It calculates the length of each word and finds the minimum among them.
        min_word_length = min(len(word) for word in all_words)

    # If `longest_substring_length` is 0 or less than the minimum word length,
    # it means no common substring meeting the criteria was found.
    if longest_substring_length < min_longest_substring or longest_substring_length < min_word_length:
        return ''
    else:
        # Extract the longest common substring from the original `upper_string1`.
        # The slice goes from `end_index_in_string1 - longest_substring_length`
        # up to (but not including) `end_index_in_string1`.
        start_index = end_index_in_string1 - longest_substring_length
        return upper_string1[start_index:end_index_in_string1]
    

def substring_on_left(text: Optional[str], pattern: str) -> Optional[str]:
    """Extracts the substring that appears before the first occurrence of a specified pattern.

    Args:
        text (Optional[str]): The input string. Can be None.
        pattern (str): The pattern to search for.

    Returns:
        Optional[str]: The substring *before* the first 'pattern' occurrence.
                       Returns the original string if the pattern is not found.
                       Returns an empty string if the pattern is at the very beginning of the string.
                       Returns None if the input 'text' was None.

    Raises:
        TypeError: If 'pattern' is not a string.

    Example of use:
        >>> substring_on_left("hello world", " ")
        "hello"

        >>> substring_on_left("apple,banana,orange", ",")
        "apple"

        >>> substring_on_left("test", "xyz")
        "test" # Pattern not found, returns original string

        >>> substring_on_left("last char.", ".")
        "last char"

        >>> substring_on_left(" first", " ")
        "" # Pattern at the beginning
        
        >>> substring_on_left(None, "pattern")
        None
    """
    # Handle the None case for input text immediately.
    if text is None:
        return None
    
    # Ensure the input 'text' is a string. If not, convert it.
    # This makes the function more robust to varied input types.
    if not isinstance(text, str):
        text = str(text)

    # Validate that the pattern is a string, as it's critical for 'find' method.
    if not isinstance(pattern, str):
        raise TypeError("The 'pattern' must be a string.")

    # Find the index of the first occurrence of the pattern.
    # If the pattern is not found, find() returns -1.
    index = text.find(pattern)

    # If the pattern is not found, return the entire original string.
    if index == -1:
        return text
    else:
        # If the pattern is found, return the substring from the beginning
        # up to (but not including) the start of the pattern.
        return text[:index]


def substring_on_right(text: Optional[str], pattern: str) -> Optional[str]:
    """Extracts the substring that appears after the first occurrence of a specified pattern.

    Args:
        text (Optional[str]): The input string. Can be None.
        pattern (str): The pattern to search for.

    Returns:
        Optional[str]: The substring *after* the first 'pattern' occurrence.
                       Returns the original string if the pattern is not found.
                       Returns an empty string if the pattern is at the very end of the string.
                       Returns None if the input 'text' was None.

    Raises:
        TypeError: If 'pattern' is not a string.

    Example of use:
        >>> substring_on_right("hello world", " ")
        "world"

        >>> substring_on_right("apple,banana,orange", ",")
        "banana,orange"

        >>> substring_on_right("test", "xyz")
        "test" # Pattern not found, returns original string

        >>> substring_on_right("last char.", ".")
        "" # Pattern at the very end

        >>> substring_on_right("first char", "first char")
        "" # Pattern is the entire string

        >>> substring_on_right(None, "pattern")
        None
    """
    # Handle the None case for input text immediately.
    if text is None:
        return None
    
    # Ensure the input 'text' is a string. If not, convert it.
    if not isinstance(text, str):
        text = str(text)

    # Validate that the pattern is a string, as it's critical for 'find' method.
    if not isinstance(pattern, str):
        raise TypeError("The 'pattern' must be a string.")

    # Find the index of the first occurrence of the pattern.
    # If the pattern is not found, find() returns -1.
    index = text.find(pattern)

    # If the pattern is not found, return the entire original string.
    if index == -1:
        return text
    else:
        # If the pattern is found, return the substring starting *after* the pattern.
        # This is achieved by slicing from (index + length of pattern) to the end of the string.
        return text[index + len(pattern):]


def substring_between_pattern(input_string: str, pattern: str) -> str | None:
    """
    Extracts the substring located between the first two occurrences of a specified pattern
    within a given string.

    This function is particularly useful for parsing structured text where relevant
    information is consistently delimited by a repeating pattern. The pattern
    is treated as a literal string (special regex characters are escaped).

    Args:
        input_string (str): The string from which to extract the substring.
        pattern (str): The string pattern that acts as both the start and end delimiter.

    Returns:
        str | None: The extracted substring, stripped of leading/trailing whitespace.
                    Returns None if the input string is empty, the pattern is empty,
                    or if the pattern is not found twice in the string.

    Raises:
        TypeError: If 'input_string' or 'pattern' are not strings.

    Example:
        >>> substring_between_pattern("Data:VALUE:End", ":")
        'VALUE'

        >>> substring_between_pattern("START_data_END", "_")
        'data'

        >>> substring_between_pattern("No matching patterns", "ABC")
        None

        >>> substring_between_pattern("One pattern onlyABC", "ABC")
        None

        >>> substring_between_pattern("Multiple///segments///here", "///")
        'segments'

        >>> substring_between_pattern("Edge case: pattern at start: content: pattern at end", ":")
        ' pattern at start'

        >>> substring_between_pattern("  Pattern  \n  Content \n  Pattern  ", "Pattern")
        '  \n  Content \n  '
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(pattern, str):
        raise TypeError("Input 'pattern' must be a string.")

    # Return None early if either input is empty.
    # This prevents unnecessary regex processing for trivial cases.
    if not input_string or not pattern:
        return None

    # Escape the pattern to treat any special regex characters within it as literals.
    # This ensures that patterns like "a.b" match "a.b" literally, not "aXb".
    escaped_pattern = re.escape(pattern)

    # Construct the regular expression.
    # - `escaped_pattern`: Matches the literal start delimiter.
    # - `(.*?)`: This is the capturing group.
    #            `.` matches any character (including newline due to re.DOTALL).
    #            `*?` is a non-greedy quantifier, meaning it matches as few characters
    #            as possible to satisfy the overall match, ensuring it stops at the
    #            first subsequent `escaped_pattern`.
    # - `escaped_pattern`: Matches the literal end delimiter.
    # re.DOTALL: Makes the '.' in the regex match newline characters as well.
    regex_to_match = f"{escaped_pattern}(.*?){escaped_pattern}"

    # Search for the pattern in the input string.
    # re.search finds the first occurrence of the pattern.
    match = re.search(regex_to_match, input_string, re.DOTALL)

    # If a match is found, extract the content of the first capturing group.
    # The .strip() method is applied to remove any leading/trailing whitespace
    # from the extracted content, as per common requirements for such utilities.
    if match:
        return match.group(1).strip()
    else:
        # If no match is found (i.e., the pattern does not appear twice), return None.
        return None
    

def substring_from_delimiters(
    input_string: str,
    opening_delimiter: str = "(",
    closing_delimiter: str = ")",
) -> str:
    """
    Extracts the substring enclosed within the first pair of specified delimiters in a given string.

    This function finds the content between the first occurrence of the `opening_delimiter`
    and the last occurrence of the `closing_delimiter`. It is useful for parsing
    data where key information is consistently enclosed within a specific pair of characters.

    Args:
        input_string (str): The string from which to extract the substring.
        opening_delimiter (str): The character(s) marking the beginning of the substring. Defaults to "(".
        closing_delimiter (str): The character(s) marking the end of the substring. Defaults to ")".

    Returns:
        str: The substring found between the delimiters. Returns an empty string
             if no matching delimiters are found or if the content is empty.

    Raises:
        TypeError: If 'input_string', 'opening_delimiter', or 'closing_delimiter' is not a string.
        ValueError: If an empty string is provided as a delimiter, if a closing
                    delimiter is found before an opening one, or if the delimiters
                    are not properly balanced (e.g., missing one).

    Example of use:
        >>> substring_from_delimiters("This is a (test) string.", "(", ")")
        'test'
        >>> substring_from_delimiters("Another [example with multiple] brackets [like this].", "[", "]")
        'example with multiple] brackets [like this'
        >>> substring_from_delimiters("A {curly} brace example.", "{", "}")
        'curly'
        >>> substring_from_delimiters("No delimiters here.", "(", ")")
        ''
        >>> substring_from_delimiters("Empty <> content.", "<", ">")
        ''
        >>> substring_from_delimiters("{Starts with braces}", "{", "}")
        'Starts with braces'

    Cost: O(n), where n is the length of the input string. This is because `find` and `rfind`
    operations traverse the string linearly in the worst case.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(opening_delimiter, str) or not isinstance(closing_delimiter, str):
        raise TypeError("Delimiters must be strings.")
    if not opening_delimiter or not closing_delimiter:
        raise ValueError("Delimiters cannot be empty strings.")

    # Find the index of the first opening delimiter.
    # We use .find() because it returns -1 if not found.
    start_index = input_string.find(opening_delimiter)

    # Find the index of the last closing delimiter.
    # We use .rfind() to ensure we get the last occurrence.
    end_index = input_string.rfind(closing_delimiter)

    # Check if both delimiters were found and in the correct order.
    # We return an empty string if either delimiter is not found,
    # as there's no valid substring to extract.
    if start_index == -1 or end_index == -1:
        return ""
    # If the opening delimiter is at or after the closing one, they are misplaced,
    # which indicates an invalid enclosure.
    elif start_index >= end_index:
        raise ValueError("Mismatched or misplaced delimiters detected in the string.")
    else:
        # Extract the substring between the found indices.
        # We add the length of the opening_delimiter to start_index to exclude it.
        return input_string[start_index + len(opening_delimiter) : end_index]


def substring_between_delimiters(
    text: Optional[str],
    delimiter_key: str
) -> Optional[List[str]]:
    """
    Extracts all substrings found between a specified pair of delimiters.

    Args:
        text (Optional[str]): The input string from which to extract substrings. Can be None.
        delimiter_key (str): A key representing the type of delimiters to use.
                             Supported: '/* */', '()', '[]', '{}', '<>', '""', "''", '$$'

    Returns:
        Optional[List[str]]: A list of extracted substrings (excluding the delimiters themselves),
                              or None if the input was None. Returns an empty list if no matches are found.

    Raises:
        ValueError: If an unsupported delimiter key is provided.

    Example of use:
        >>> substring_between_delimiters("hello(world)foo[bar]baz", "()")
        ['world']
        >>> substring_between_delimiters("code /* multiline\\ncomment */ more code", "/* */")
        [' multiline\\ncomment ']
    """
    # Return None immediately if the input text is None.
    if text is None:
        return None

    # Validate the delimiter key to ensure it's supported.
    if delimiter_key not in DELIMITERS:
        supported_keys = ', '.join(DELIMITERS.keys())
        raise ValueError(f"Unsupported delimiter: '{delimiter_key}'. Please choose from: {supported_keys}")

    start_delimiter_pattern, end_delimiter_pattern = DELIMITERS[delimiter_key]

    # The pattern uses non-greedy matching (.*?) to ensure it only captures
    # content between the closest start and end delimiters.
    # The parentheses around '.*?' create a capturing group, so only the
    # content inside the delimiters is returned by re.findall.
    full_regex_pattern = start_delimiter_pattern + r'(.*?)' + end_delimiter_pattern

    # Find all occurrences of the pattern.
    # re.DOTALL ensures '.' matches newline characters.
    return re.findall(full_regex_pattern, text, flags=re.DOTALL)


def substring_before_first_digit(input_string: str) -> str:
    """
    Extracts the substring before the first occurrence of a digit in a given string.

    This function iterates through the input string character by character.
    If a digit is encountered, it returns the portion of the string
    that precedes this digit. If no digits are found, the entire
    original string is returned.

    Args:
        input_string: The string from which to extract the substring.

    Returns:
        The substring before the first digit, or the original string if no digits are present.

    Raises:
        TypeError: If the input is not a string.

    Example of use:
        >>> substring_before_first_digit("abc123def")
        'abc'
        >>> substring_before_first_digit("no_digits_here")
        'no_digits_here'
        >>> substring_before_first_digit("123start")
        ''
        >>> substring_before_first_digit("")
        ''
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Iterate through the string to find the index of the first digit.
    # This loop is optimized for early exit as soon as a digit is found.
    for index, char in enumerate(input_string):
        if char.isdigit():
            # Return the substring up to (but not including) the first digit.
            return input_string[:index]

    # If no digits are found after checking all characters, return the entire string.
    return input_string
  

def substring_after_last_digit(input_string: str) -> str:
    """
    Extracts the substring after the last occurrence of a digit in a given string.

    This function iterates through the input string in reverse order.
    When the last digit is found, it returns the portion of the string
    that follows this digit. If no digits are found, an empty string is returned.

    Args:
        input_string: The string from which to extract the substring.

    Returns:
        The substring after the last digit, or an empty string if no digits are present.

    Raises:
        TypeError: If the input is not a string.

    Example of use:
        >>> substring_after_last_digit("abc123def456ghi")
        'ghi'
        >>> substring_after_last_digit("no_digits_here")
        ''
        >>> substring_after_last_digit("123start")
        'start'
        >>> substring_after_last_digit("end123")
        ''
        >>> substring_after_last_digit("")
        ''
    """
    if not isinstance(input_string, str):
        raise TypeError("Input must be a string.")

    # Iterate through the string from right to left to find the last digit.
    # We use range(len(input_string) - 1, -1, -1) for reverse iteration.
    for index in range(len(input_string) - 1, -1, -1):
        if input_string[index].isdigit():
            # Return the substring from the character immediately after the last digit.
            # This handles cases where the last digit is at the end of the string,
            # resulting in an empty string being returned, which is correct.
            return input_string[index + 1:]

    # If no digits are found after checking all characters, return an empty string.
    # This is because there's no "after a digit" part.
    return ""


def split_by_substrings(p_iparse: str, p_separators: list[str]) -> list[str]:
    """
    Splits a string by a list of keyword separators, keeping the separator with its content.

    Description:
      This function takes a string (like a SQL script) and splits it into a list of
      substrings. Each substring in the output list begins with one of the specified
      separators. It is designed to handle complex inputs where separators mark the
      beginning of a new logical block. This implementation correctly handles Oracle
      SQL scripts containing both standard SQL statements and PL/SQL blocks.
    
    Args:
      p_iparse (str): The input string to be split.
      p_separators (list[str]): A list of strings to use as separators. These should
                                be the keywords that start each block.

    Returns:
      list[str]: A list of strings, where each element is a complete, executable
                 command block from the input script.

    Raises:
      None.

    Example of use:
      >>> sql_script = "CREATE TABLE T1 (c1 INT); COMMENT ON TABLE T1 IS 'test'; BEGIN NULL; END; /"
      >>> separators = ["CREATE TABLE", "COMMENT ON", "BEGIN"]
      >>> split_by_substrings(sql_script, separators)
      ["CREATE TABLE T1 (c1 INT);", "COMMENT ON TABLE T1 IS 'test';", "BEGIN NULL; END; /"]
    """
    if not isinstance(p_iparse, str) or not p_iparse.strip():
        # Why: We avoid processing empty or invalid input from the start.
        return []

    # 1. Escape separators for safe use in regex and create a pattern that finds any of them.
    #    This ensures that special regex characters in separators don't break the pattern.
    escaped_separators = [re.escape(s) for s in p_separators]

    # 2. Split the script using a positive lookahead.
    #    - `(?=...)` is a positive lookahead assertion. It checks if the text ahead matches
    #      the pattern without consuming it.
    #    - `(?:' + sep_pattern + `)`: This matches any of the defined separators.
    #    - The split happens at the position *just before* a separator is found.
    #    - This effectively splits the script into parts, where each part (except the first)
    #      starts with a separator keyword.
    # Why: This is a robust way to split a text by delimiters while keeping the delimiters
    #      at the beginning of the resulting strings.
    blocks = re.split(f'(?=(?:{"|".join(escaped_separators)}))', p_iparse, flags=re.IGNORECASE)

    # 3. Clean up the resulting list.
    #    - The first element of the split might be empty or just whitespace if the script
    #      starts with a separator. We filter this out.
    #    - Each block is stripped of leading/trailing whitespace.
    # Why: This ensures the final output is a clean list of executable statements.
    result = [block.strip() for block in blocks if block and block.strip()]

    return result


def split_between_delimiters(
    text: Optional[str],
    delimiter_key: str
) -> Optional[List[str]]:
    """
    Splits the input string into a list of substrings, using the content within
    the specified delimiters as separators.

    Args:
        text (Optional[str]): The input string to be split. Can be None.
        delimiter_key (str): A key representing the type of delimiters to use.
                             Supported: '/* */', '()', '[]', '{}', '<>', '""', "''", '$$'

    Returns:
        Optional[List[str]]: A list of substrings if the input was not None,
                              otherwise None. The delimiters and their contents
                              are not included in the resulting substrings.

    Raises:
        ValueError: If an unsupported delimiter key is provided.

    Example of use:
        >>> split_between_delimiters("hello(world)foo[bar]baz", "()")
        ['hello', 'foo[bar]baz']
        >>> split_between_delimiters("before /*comment*/ after", "/* */")
        ['before ', ' after']
    """
    # Return None immediately if the input text is None.
    if text is None:
        return None

    # Validate the delimiter key to ensure it's supported.
    if delimiter_key not in DELIMITERS:
        supported_keys = ', '.join(DELIMITERS.keys())
        raise ValueError(f"Unsupported delimiter: '{delimiter_key}'. Please choose from: {supported_keys}")

    start_delimiter_pattern, end_delimiter_pattern = DELIMITERS[delimiter_key]

    # Construct the regular expression pattern to find content within delimiters.
    # The pattern captures the content between delimiters but doesn't include the delimiters themselves in the split.
    full_regex_pattern = start_delimiter_pattern + r'.*?' + end_delimiter_pattern

    # Split the string using the constructed regex pattern.
    # re.split will use the matched patterns as delimiters for splitting.
    return re.split(full_regex_pattern, text, flags=re.DOTALL)


def extract_content_by_encloser_type(
    input_string: str,
    encloser_type: str,
) -> str:
    """
    Extracts the substring enclosed within a specific type of encloser
    (e.g., parentheses, square brackets, curly braces, angle brackets,
    double angle brackets, HTML-like comments, triple single quotes,
    triple double quotes, or Spanish question marks).

    This function serves as a wrapper to `substring_from_delimiters`, allowing
    the user to specify a common name for the encloser type. It maps the
    given encloser type to its corresponding opening and closing characters.

    Args:
        input_string (str): The string from which to extract the substring.
        encloser_type (str): The type of encloser to look for. Supported types
                             are "parentheses", "square_brackets", "curly_braces",
                             "question_marks" (for Spanish ¿?), "angle_brackets",
                             "double_angle_brackets", "html_comments",
                             "triple_single_quotes", and "triple_double_quotes".

    Returns:
        str: The extracted substring. Returns an empty string if the encloser
             type is not recognized or if no content is found.

    Raises:
        TypeError: If 'input_string' or 'encloser_type' is not a string.
        ValueError: If the encloser type is not supported, or if there are
                    mismatched or misplaced delimiters.

    Example of use:
        >>> extract_content_by_encloser_type("Hello (world)!", "parentheses")
        'world'
        >>> extract_content_by_encloser_type("Items [apple, banana, orange].", "square_brackets")
        'apple, banana, orange'
        >>> extract_content_by_encloser_type("Config {host: localhost, port: 8080}.", "curly_braces")
        'host: localhost, port: 8080'
        >>> extract_content_by_encloser_type("¿Qué tal estás?", "question_marks")
        'Qué tal estás'
        >>> extract_content_by_encloser_type("This is <important> content.", "angle_brackets")
        'important'
        >>> extract_content_by_encloser_type("Look <<very important>> data.", "double_angle_brackets")
        'very important'
        >>> extract_content_by_encloser_type("HTML: ", "html_comments")
        ' This is a comment '
        >>> extract_content_by_encloser_type("Docstring: '''This is a multiline\nexample with single quotes.'''", "triple_single_quotes")
        'This is a multiline\nexample with single quotes.'
        >>> extract_content_by_encloser_type("Python code: \"\"\"This is another\nmultiline string.\"\"\"", "triple_double_quotes")
        'This is another\nmultiline string.'
        >>> extract_content_by_encloser_type("No brackets here.", "square_brackets")
        ''
        >>> extract_content_by_encloser_type("Invalid {bracket placement)", "curly_braces")
        # Raises ValueError

    Cost: O(n), where n is the length of the input string. This is due to the underlying
    `substring_from_delimiters` function's complexity.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(encloser_type, str):
        raise TypeError("Input 'encloser_type' must be a string.")

    # A dictionary mapping common encloser names to their corresponding delimiters.
    # This helps in providing a more user-friendly interface.
    DELIMITER_MAP: Dict[str, tuple[str, str]] = {
        "parentheses": ("(", ")"),
        "square_brackets": ("[", "]"),
        "curly_braces": ("{", "}"),
        "question_marks": ("¿", "?"), # Corrected for Spanish convention (inverted opening mark)
        "angle_brackets": ("<", ">"),
        "double_angle_brackets": ("<<", ">>"),
        "html_comments": (""),
        "triple_single_quotes": ("'''", "'''"),
        "triple_double_quotes": ("\"\"\"", "\"\"\""),
    }

    # Retrieve the delimiters based on the provided encloser_type.
    # If the type is not found, raise a ValueError to inform the user.
    delimiters = DELIMITER_MAP.get(encloser_type.lower())
    if delimiters is None:
        raise ValueError(f"Unsupported encloser type: '{encloser_type}'. "
                         "Supported types are 'parentheses', 'square_brackets', 'curly_braces', "
                         "'question_marks', 'angle_brackets', 'double_angle_brackets', 'html_comments', "
                         "'triple_single_quotes', and 'triple_double_quotes'.")

    opening, closing = delimiters

    # Delegate the extraction to the more generic `substring_from_delimiters` function.
    return substring_from_delimiters(input_string, opening, closing)


def extract_first_number(input_string: str | None) -> int | float | None:
    """Extracts the first integer or float (positive or negative) from a string.

    This function searches for the first occurrence of a number within the
    given string. It handles both integer and decimal numbers, as well as
    positive and negative signs. If a decimal is found, the number is
    returned as a float; otherwise, it's returned as an integer.

    Args:
        input_string: The string from which to extract the number.

    Returns:
        The extracted number as an `int` or `float`, or `None` if no
        number is found or the input is invalid.

    Raises:
        ValueError: If a matched string cannot be converted to a number.
            (Though current implementation handles this with a return None)

    Example of use:
        >>> extract_first_number("The answer is 42.")
        42
        >>> extract_first_number("Price: -19.99 USD")
        -19.99
        >>> extract_first_number("No numbers here!")
        None
    """
    if not isinstance(input_string, str) or not input_string:
        return None

    # Regex to find numbers:
    # `[-+]?` matches an optional sign (+ or -).
    # `\d*\.\d+` matches a floating-point number (e.g., ".5", "1.5", "-.5").
    # `|` acts as an OR operator.
    # `[-+]?\d+` matches an integer number (e.g., "5", "-10", "+20").
    # The order `\d*\.\d+|\d+` is important to prioritize floats over integers
    # when an integer could also be a float (e.g., "10.0").
    match = re.search(r'[-+]?\d*\.\d+|[-+]?\d+', input_string)
    if match:
        number_string = match.group(0)
        try:
            # Check for the presence of a decimal point to determine the type.
            if '.' in number_string:
                return float(number_string)
            else:
                return int(number_string)
        except ValueError:
            # This handles cases where `re.search` might find something
            # that looks like a number but isn't a valid conversion (e.g., "++1").
            # While the regex is robust, this adds an extra layer of safety.
            return None

    return None


def extract_last_number(input_string: str | None) -> int | float | None:
    """Extracts the last integer or float (positive or negative) from a string.

    This function searches for the last occurrence of a number within the
    given string. It handles both integer and decimal numbers, as well as
    positive and negative signs. If a decimal is found, the number is
    returned as a float; otherwise, it's returned as an integer.

    Args:
        input_string: The string from which to extract the number.

    Returns:
        The extracted number as an `int` or `float`, or `None` if no
        number is found or the input is invalid.

    Raises:
        ValueError: If a matched string cannot be converted to a number.
            (Though current implementation handles this with a return None)

    Example of use:
        >>> extract_last_number("Item A: 10, Item B: 20.5, Total: 30")
        30
        >>> extract_last_number("Values: -5.0, +100")
        100
        >>> extract_last_number("No numbers here!")
        None
    """
    # Defensive programming: Ensure the input is a non-empty string.
    # This check is crucial because the `re.findall` function expects a string.
    if not isinstance(input_string, str) or not input_string:
        return None

    # Regex to find numbers:
    # `[-+]?` matches an optional sign (+ or -).
    # `\d*\.\d+` matches a floating-point number (e.g., ".5", "1.5", "-.5").
    # `|` acts as an OR operator.
    # `[-+]?\d+` matches an integer number (e.g., "5", "-10", "+20").
    # We use `re.findall` to get all matches, then take the last one.
    # The order `\d*\.\d+|\d+` is important to prioritize floats over integers.
    all_matches = _RE_NUMBER_PATTERN.findall(input_string)

    # If matches were found, process the last one.
    if all_matches:
        # We take the last matched string, as the goal is to extract the last number.
        number_string = all_matches[-1]
        try:
            # Check for the presence of a decimal point to determine the type.
            if '.' in number_string:
                return float(number_string)
            else:
                return int(number_string)
        except ValueError:
            # This handles cases where `re.findall` might find something
            # that looks like a number but isn't a valid conversion.
            return None

    # Return None if no match is found by the regex.
    return None


def extract_numbers(input_string: str | None) -> list[int | float]:
    """Extracts all integers and floats (positive or negative) from a string.

    This function searches for all occurrences of numbers within the
    given string. It handles both integer and decimal numbers, as well as
    positive and negative signs. Returns a list of all numbers found,
    where each number is returned as an int or float depending on whether
    it contains a decimal point.

    Args:
        input_string: The string from which to extract the numbers.

    Returns:
        A list of extracted numbers as `int` or `float` values.
        Returns an empty list if no numbers are found or the input is invalid.

    Raises:
        None

    Example of use:
        >>> extract_numbers("The prices are 42 and 19.99")
        [42, 19.99]
        >>> extract_numbers("Values: -5, 10.5, +100")
        [-5, 10.5, 100]
        >>> extract_numbers("No numbers here!")
        []
        >>> extract_numbers("Mixed: 1.5, 2, -3.14, 42")
        [1.5, 2, -3.14, 42]
        >>> extract_numbers(None)
        []

    Cost:
        O(n) where n is the length of the input string. This is due to
        the regular expression search operation.
    """
    # Defensive programming: Ensure the input is a non-empty string.
    if not isinstance(input_string, str) or not input_string:
        return []

    # Regex to find numbers:
    # `[-+]?` matches an optional sign (+ or -).
    # `\d*\.\d+` matches a floating-point number (e.g., ".5", "1.5", "-.5").
    # `|` acts as an OR operator.
    # `[-+]?\d+` matches an integer number (e.g., "5", "-10", "+20").
    # We use `re.findall` to get all matches.
    # The order `\d*\.\d+|\d+` is important to prioritize floats over integers.
    all_matches = _RE_NUMBER_PATTERN.findall(input_string)

    # Convert matched strings to appropriate numeric types
    result = []
    for match in all_matches:
        try:
            # Check for the presence of a decimal point to determine the type.
            if '.' in match:
                result.append(float(match))
            else:
                result.append(int(match))
        except ValueError:
            # Skip any matches that cannot be converted (though regex should prevent this)
            continue

    return result


def split_all(text_to_tokenize: str, delimiter_pattern: str = None, return_joined: bool = False) -> list[str] | tuple[list[str], str]:
    r"""
    Splits the input string into a list of words (tokens) based on a
    comprehensive set of delimiters.

    This function is designed to break down a continuous string of text into
    individual meaningful units (tokens). By default, it uses a pattern
    that includes common punctuation, symbols, and various whitespace characters
    as delimiters. You can also provide a custom regex pattern to define
    specific splitting behavior. Empty strings resulting from the split
    operation are automatically removed.

    Args:
        text_to_tokenize (str): The input string to be tokenized.
        delimiter_pattern (str, optional): A custom regular expression pattern
                                           to use as a delimiter. If None,
                                           a default comprehensive pattern
                                           including punctuation, symbols, and
                                           whitespace will be used.
                                           Defaults to None.
        return_joined (bool, optional): If True, returns a tuple containing
                                         the split list and the joined string
                                         using join_to_string with default separator.
                                         Defaults to False.

    Returns:
        list[str] | tuple[list[str], str]: A list of strings, where each string is a token (word).
                   Returns an empty list if the input is None or an empty string
                   after processing. If return_joined is True, returns a tuple
                   (split_list, joined_string).

    Raises:
        TypeError: If 'text_to_tokenize' is not a string or None, or if
                   'delimiter_pattern' is provided but not a string.

    Example of use:
        >>> split_all("Hello, world! This is a test.")
        ['Hello', 'world', 'This', 'is', 'a', 'test']
        >>> split_all("  Another example  with   extra   spaces!  ")
        ['Another', 'example', 'with', 'extra', 'spaces']
        >>> split_all("item1/item2-item3", delimiter_pattern=r'[/\-]+')
        ['item1', 'item2', 'item3']
        >>> split_all("Python's cool!")
        ['Python', 's', 'cool']
        >>> split_all(None)
        []
        >>> split_all("Hello world", return_joined=True)
        (['Hello', 'world'], 'Hello world')

    Cost:
        O(N), where N is the length of the input string. This is due to
        the regular expression splitting, which is generally linear with
        respect to the input size.
    """
    if text_to_tokenize is None:
        if return_joined:
            return ([], "")
        return []

    # If no custom pattern is provided, use the default comprehensive one.
    if delimiter_pattern is None:
        pattern_to_use = _DEFAULT_WORD_SEPARATORS
    else:
        pattern_to_use = delimiter_pattern

    # Split the string using the determined regex pattern.
    # This will return a list that may contain empty strings if delimiters
    # are at the start/end or if there are multiple consecutive delimiters.
    split_parts = re.split(pattern_to_use, text_to_tokenize)

    # Filter out any empty strings and return the cleaned list of tokens.
    # filter(None, ...) is an efficient way to remove falsy values (like empty strings)
    # from an iterable.
    split_list = list(filter(None, split_parts))

    if return_joined:
        joined_string = join_to_string(split_list)
        return (split_list, joined_string)

    return split_list


def join_to_string(iterable: Iterable[str], separator: str = " ") -> str:
    """
    Joins an iterable of strings into a single string with a specified separator.

    Args:
        iterable (Iterable[str]): The iterable of strings to join.
        separator (str, optional): The separator to use between strings.
                                   Defaults to a single space.

    Returns:
        str: The joined string.

    Example of use:
        >>> join_to_string(['Hello', 'world!'])
        'Hello world!'
        >>> join_to_string(['apple', 'banana', 'cherry'], separator=', ')
        'apple, banana, cherry'
        >>> join_to_string(('a', 'b', 'c'))
        'a b c'
    """
    return separator.join(iterable)

def get_substrings(string1: str, string2: str) -> list[dict]:
    """
    Identifies and returns all common contiguous substrings (matching blocks)
    between two input strings.

    This function utilizes the `difflib.SequenceMatcher` to find sequences of
    identical characters that appear in the same order in both strings.
    For each common block found, it provides details such as their positions
    in the original strings and their length.

    Args:
        string1 (str): The first string for comparison.
        string2 (str): The second string for comparison.

    Returns:
        list[dict]: A list of dictionaries, where each dictionary represents
                    a common contiguous substring (matching block). Each dictionary
                    contains the following keys:
                    - 'string1_start': Starting index of the common substring in string1.
                    - 'string2_start': Starting index of the common substring in string2.
                    - 'length': The length of the common substring.
                    - 'substring': The actual common substring found.
                    Returns an empty list if no common substrings are found.

    Raises:
        TypeError: If 'string1' or 'string2' are not strings.

    Example:
        >>> get_substrings("apple tree", "pineapple")
        [{'string1_start': 0, 'string2_start': 1, 'length': 5, 'substring': 'apple'}]

        >>> get_substrings("banana peel", "bandana")
        [{'string1_start': 0, 'string2_start': 0, 'length': 3, 'substring': 'ban'},
         {'string1_start': 5, 'string2_start': 4, 'length': 2, 'substring': 'na'}]

        >>> get_substrings("hello world", "python")
        []

        >>> get_substrings("abc", "abc")
        [{'string1_start': 0, 'string2_start': 0, 'length': 3, 'substring': 'abc'}]
    """
    if not isinstance(string1, str):
        raise TypeError("Input 'string1' must be a string.")
    if not isinstance(string2, str):
        raise TypeError("Input 'string2' must be a string.")

    # Initialize SequenceMatcher with the two input strings.
    # It analyzes the sequences to find common subsequences and matching blocks.
    matcher = difflib.SequenceMatcher(a=string1, b=string2)

    # Initialize a list to store the details of each common substring found.
    # This list will hold dictionaries, each describing a match.
    common_substring_blocks = []

    # Iterate through the matching blocks provided by the SequenceMatcher.
    # Each 'match' object contains (a, b, size), where:
    # a: starting index in string1
    # b: starting index in string2
    # size: length of the common substring
    for match in matcher.get_matching_blocks():
        # A match.size of 0 indicates a sentinel block (end of matches),
        # so we only process blocks with actual length.
        if match.size > 0:
            # Construct a dictionary for the current matching block.
            # Using more descriptive keys enhances clarity for users of this data.
            block_details = {
                "string1_start": match.a,
                "string2_start": match.b,
                "length": match.size,
                "substring": string1[match.a : match.a + match.size],
            }
            common_substring_blocks.append(block_details)

    return common_substring_blocks


def get_in_text_by_pattern(text: str, pattern_type: str) -> list:
    """
    Finds and returns all occurrences of a specified pattern type within the given text.

    This function acts as a versatile wrapper for common regular expression searches.
    It takes a text string and a predefined pattern type, then applies the
    corresponding regex to extract all matching substrings. This centralizes
    pattern definitions, making your code cleaner and more maintainable.

    Args:
        text (str): The input string to search within.
        pattern_type (str): A string indicating the type of pattern to search for.
                            Supported types include:
                            - 'alphanumeric_strings': Strings containing both numbers and letters.
                            - 'letters_and_numbers': Strings with at least one letter and one number.
                            - 'only_letters': Strings containing only letters.
                            - 'uppercase_letters': Strings containing only uppercase letters.
                            - 'lowercase_letters': Strings containing only lowercase letters.
                            - 'words_without_numbers': Words that do not contain any digits.
                            - 'words_length_5': Words exactly 5 characters long.
                            - 'words_length_3_to_5': Words between 3 and 5 characters long.
                            - 'specific_words': Matches 'word1', 'word2', or 'word3'.
                            - 'text_in_parentheses': Text enclosed within parentheses.
                            - 'no_forbidden_word': Lines that do not contain the word "forbidden".
                            - 'all_words': All words in the text.
                            - 'words_starting_with_python': Words that begin with "python".
                            - 'alphanumeric_user_id': User IDs (4-10 alphanumeric characters).
                            - 'strict_email': Strict email address format.
                            - 'broad_email': Broader email address format.
                            - 'integer': Integer numbers.
                            - 'decimal_number': Decimal numbers.
                            - 'only_numbers': Strings containing only numbers.
                            - 'date_yyyy_mm_dd': Dates in YYYY-MM-DD format.
                            - 'time_hh_mm_ss': Time in HH:MM:SS format.
                            - 'time_12_hour': 12-hour time with AM/PM.
                            - 'phone_number_specific': Specific phone number format (e.g., +XX YYYYZZZZZZ).
                            - 'international_phone_number': International phone numbers.
                            - 'visa_credit_card': Visa credit card numbers.
                            - 'txt_filename': Filenames with a .txt extension.
                            - 'ipv4_address': IPv4 addresses.
                            - 'ipv6_address': IPv6 addresses.
                            - 'simple_html_tag': Simple HTML tags.
                            - 'basic_url': Basic URLs starting with http:// or https://.

    Returns:
        list: A list of all found matches. Returns an empty list if no matches are found
              or if the pattern_type is not recognized.

    Raises:
        ValueError: If an unknown pattern_type is provided.

    Example:
        >>> get_in_text_by_pattern("Hello 123 World! This is a test.", 'alphanumeric_strings')
        ['Hello 123', 'World']

    Cost:
        The cost of this function is O(N*M) in the worst case, where N is the length
        of the input text and M is the length of the regular expression pattern.
        This is because the `re.findall` operation needs to potentially
        scan the entire string for all occurrences of the pattern.
    """
    # Define a dictionary of common regex patterns for clarity and easy access.
    # This design allows for easy extension with new patterns without modifying
    # the core logic of the function.
    patterns = {
        'alphanumeric_strings': r'[a-zA-Z0-9]+',
        'letters_and_numbers': r'(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z0-9]+',
        'only_letters': r'[a-zA-Z]+',
        'uppercase_letters': r'[A-Z]+',
        'lowercase_letters': r'[a-z]+',
        'words_without_numbers': r'\b\D+\b',
        'words_length_5': r'\b\w{5}\b',
        'words_length_3_to_5': r'\b\w{3,5}\b',
        'specific_words': r'(word1|word2|word3)',
        'text_in_parentheses': r'\((.*?)\)',
        'no_forbidden_word': r'^(?!.*forbidden).*$',
        'all_words': r'\b\w+\b',
        'words_starting_with_python': r'\bpython\w*\b',
        'alphanumeric_user_id': r'\b[a-zA-Z0-9]{4,10}\b',
        'strict_email': r'[\w\.-]+@[\w\.-]+',
        'broad_email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
        'integer': r'\d+',
        'decimal_number': r'\d+\.\d+',
        'only_numbers': r'\d+',
        'date_yyyy_mm_dd': r'\d{4}-\d{2}-\d{2}',
        'time_hh_mm_ss': r'\d{2}:\d{2}:\d{2}',
        'time_12_hour': r'(1[0-2]|0?[1-9]):[0-5][0-9]\s*[APMapm]{2}',
        'phone_number_specific': r'(\+\d{1,2}\s?)?(\d{10,12})',
        'international_phone_number': r'\+\d{1,4}\s?\(?\d{1,}\)?[-.\s]?\d{1,}[-.\s]?\d{1,}',
        'visa_credit_card': r'4[0-9]{12}(?:[0-9]{3})?',
        'txt_filename': r'\b\w+\.txt\b',
        'ipv4_address': r'\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b',
        'ipv6_address': r'([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}',
        'simple_html_tag': r'<[^>]+>',
        'basic_url': r'https?://\S+'
    }

    # Retrieve the pattern based on the provided pattern_type.
    # If the pattern_type is not found, raise a ValueError to indicate an invalid input.
    pattern = patterns.get(pattern_type)
    if not pattern:
        raise ValueError(f"Unknown pattern type: '{pattern_type}'. Please choose from the supported types.")

    # For patterns that require matching across multiple lines (like 'no_forbidden_word'),
    # the re.M (re.MULTILINE) flag is used to ensure the '^' and '$' anchors work per line.
    # Otherwise, for most other patterns, the re.IGNORECASE flag is often useful for
    # case-insensitive matching, making the searches more flexible.
    flags = 0
    if pattern_type == 'no_forbidden_word':
        flags = re.M
    else:
        flags = re.IGNORECASE # Default to case-insensitive for broader matches.

    # Use re.findall to get all non-overlapping matches of the pattern in the string.
    # re.findall is chosen here because the requirement is to "find all" occurrences.
    # The result is a list of strings (or tuples if the pattern has groups).
    found_matches = re.findall(pattern, text, flags)

    # Some regex patterns (like 'text_in_parentheses' or 'phone_number_specific')
    # might return tuples if they contain capturing groups.
    # This loop flattens those results into a simple list of strings for consistent output.
    processed_matches = []
    for match in found_matches:
        if isinstance(match, tuple):
            # For patterns returning tuples, we typically want the first group
            # or concatenate all groups if they form a single logical match.
            # Here, we join them, assuming they collectively represent a single match.
            processed_matches.append(''.join(match))
        else:
            processed_matches.append(match)

    return processed_matches


def erase_specialchar(text: str, allow_spaces: bool = True, allow_underscores: bool = False, additional_allowed_chars: str = '') -> str:
    """
    Limpia una cadena de texto eliminando caracteres especiales.
    Optimizada con patrones pre-compilados y técnicas de procesamiento eficientes.

    La función convierte la cadena a mayúsculas, normaliza los acentos,
    y luego elimina todos los caracteres que no sean alfanuméricos,
    espacios (opcional), guiones bajos (opcional) o caracteres
    especificados adicionalmente.

    Args:
        text (str): La cadena de texto a limpiar.
        allow_spaces (bool): Si es True, permite espacios en blanco. Por defecto es True.
        allow_underscores (bool): Si es True, permite guiones bajos. Por defecto es False.
        additional_allowed_chars (str): Una cadena de caracteres adicionales
                                        que deben conservarse (ej. '.-_').

    Returns:
        str: La cadena de texto limpia.
    
    Cost:
        O(n) where n is the length of the text. Optimized with list comprehension
        for accent removal and pre-compiled regex for whitespace normalization.
    """
    if not isinstance(text, str):
        text = str(text)

    # 1. Normalizar a mayúsculas y quitar acentos (aplanar vocales) en un solo paso
    # Usar list comprehension es más eficiente que join con generador
    normalized_text = unicodedata.normalize('NFKD', text.upper())
    cleaned_text = ''.join(c for c in normalized_text if not unicodedata.combining(c))

    # 2. Construir el patrón de caracteres permitidos de forma optimizada
    allowed_chars = ['A-Z0-9']
    
    if allow_spaces:
        allowed_chars.append(r'\s')
    if allow_underscores:
        allowed_chars.append('_')
    if additional_allowed_chars:
        allowed_chars.append(re.escape(additional_allowed_chars))

    # Crear y compilar el patrón una sola vez
    pattern = re.compile(r'[^' + ''.join(allowed_chars) + r']')

    # 3. Eliminar caracteres no permitidos
    cleaned_text = pattern.sub('', cleaned_text)

    # 4. Normalizar espacios usando patrón pre-compilado
    return _RE_WHITESPACE.sub(' ', cleaned_text).strip()


def erase_symbol(p_iparse: str | None) -> str | None:
    """
    Removes a predefined set of common symbols from the input string,
    then applies a general special character cleaning and space normalization.

    Args:
        p_iparse (str | None): The input string.

    Returns:
        str | None: The cleaned string, or None if input was None.
    """
    if p_iparse is None:
        return None

    # Define a regex pattern that matches all the symbols to remove.
    # Characters within [] in regex form a character set.
    # '-' should be at the start or end, or escaped, to avoid range interpretation.
    # Many common symbols lose their special meaning inside a character set,
    # but escaping `\`, `^`, `]`, and `-` (if not at ends) is good practice.
    symbols_to_remove_pattern = r"[°ª@#$%€&=+\-_/\\|·.:,;\[\](){}<>'\"´–’‘‹˜`’¬‰½ƒŽœ‹Š˜‡†¥ð§\xa0¿?!¡>]"
    
    # Replace all occurrences of these symbols with an empty string
    oparse = re.sub(symbols_to_remove_pattern, "", p_iparse)
    
    # Apply further cleaning: flatten vowels, uppercase, remove other special chars, and normalize spaces.
    return erase_specialchar(oparse)


def erase_digits(text: Optional[str]) -> Optional[str]:
    """
    Removes all digit characters from the input string.

    Args:
        text (Optional[str]): The input string. Can be None.

    Returns:
        Optional[str]: The string with digits removed, or None if the input was None.
                       Returns an empty string if the input was an empty string.
    """
    if text is None:
        return None
    return ''.join(c for c in text if not c.isdigit())


def erase_lrspaces(text: Optional[str]) -> Optional[str]:
    """
    Removes leading and trailing whitespace from the input string.

    Args:
        text (Optional[str]): The input string. Can be None.

    Returns:
        Optional[str]: The string with leading/trailing spaces removed, or None if the input was None.
                       Returns an empty string if the input was an empty string.
    """
    if text is None:
        return None
    return text.strip()


def erase_lspaces(text: Optional[str]) -> Optional[str]:
    """Removes leading (left) whitespace from the input string.

    Equivalent to VBA's LTrim function.

    Args:
        text (Optional[str]): The input string. Can be None.

    Returns:
        Optional[str]: The string with leading spaces removed, or None if the input was None.

    Usage Example:
        >>> erase_lspaces("   hello   ")
        'hello   '

    **Cost:** O(n), where n is the length of the text.
    """
    if text is None:
        return None
    return text.lstrip()


def erase_rspaces(text: Optional[str]) -> Optional[str]:
    """Removes trailing (right) whitespace from the input string.

    Equivalent to VBA's RTrim function.

    Args:
        text (Optional[str]): The input string. Can be None.

    Returns:
        Optional[str]: The string with trailing spaces removed, or None if the input was None.

    Usage Example:
        >>> erase_rspaces("   hello   ")
        '   hello'

    **Cost:** O(n), where n is the length of the text.
    """
    if text is None:
        return None
    return text.rstrip()


def erase_allspaces(text: Optional[str]) -> Optional[str]:
    """
    Removes all whitespace characters from the input string.

    Args:
        text (Optional[str]): The input string. Can be None.

    Returns:
        Optional[str]: The string with all spaces removed, or None if the input was None.
                       Returns an empty string if the input was an empty string.
    """
    if text is None:
        return None
    # Ensure the input is treated as a string before replacement.
    # This handles cases like numbers being passed in, converting them to string first.
    return str(text).replace(" ", "")


def erase_between_delimiters(
    text: Optional[str],
    delimiter_key: str
) -> Optional[str]:
    """
    Removes text content that is enclosed between a specified pair of delimiters.

    Args:
        text (Optional[str]): The input string from which to remove content. Can be None.
        delimiter_key (str): A key representing the type of delimiters to use.
                              Supported: '/* */', '()', '[]', '{}', '<>', '""', "''", '$$'

    Returns:
        Optional[str]: The string with content between delimiters removed, or None if the input was None.

    Raises:
        ValueError: If an unsupported delimiter key is provided.

    Example of use:
        >>> erase_between_delimiters("hello(world)foo", "()")
        'hellofoo'
        >>> erase_between_delimiters("this /*a comment*/ is some code", "/* */")
        'this  is some code'
    """
    # Handle None input immediately
    if text is None:
        return None

    # Validate the delimiter key against the global DELIMITERS constant.
    if delimiter_key not in DELIMITERS:
        supported_keys = ', '.join(DELIMITERS.keys())
        raise ValueError(f"Unsupported delimiter: '{delimiter_key}'. Please choose from: {supported_keys}")

    start_delimiter_pattern, end_delimiter_pattern = DELIMITERS[delimiter_key]

    # The pattern 'start_delimiter_pattern + r'.*?' + end_delimiter_pattern'
    # matches the start delimiter, then any character (non-greedily,
    # including newlines due to re.DOTALL), and finally the end delimiter.
    # The '.*?' ensures it's non-greedy, matching the smallest possible string
    # between delimiters, which is usually what you want to avoid eating too much.
    full_regex_pattern = start_delimiter_pattern + r'.*?' + end_delimiter_pattern

    # re.sub replaces all occurrences of the pattern with an empty string.
    # re.DOTALL ensures '.' matches newline characters, useful for multi-line blocks
    # like C-style comments or multi-line strings.
    return re.sub(full_regex_pattern, '', text, flags=re.DOTALL)


def distinct_words(input_string: str, case_sensitive: bool = False) -> list[str]:
    """
    Extracts all unique words from a string, with an option for case sensitivity.

    This function first tokenizes the input string into words, considering only
    alphanumeric characters. It then returns a list of these words, ensuring
    each word appears only once. The comparison for distinctness can be
    configured to be case-sensitive or case-insensitive.

    Args:
        input_string (str): The string from which to extract distinct words.
        case_sensitive (bool): If True, words like "Apple" and "apple" are
                               considered distinct. If False (default), they
                               are considered the same word.

    Returns:
        list[str]: A list of unique words found in the input string.
                   The words will be in the case they appeared in the original
                   string if `case_sensitive` is True. If `case_sensitive` is False,
                   words will be returned in their lowercase form.

    Raises:
        TypeError: If 'input_string' is not a string.

    Example:
        >>> distinct_words("Hello world, hello Python!", case_sensitive=False)
        ['hello', 'world', 'python']

        >>> distinct_words("Apple, apple, Banana", case_sensitive=True)
        ['Apple', 'apple', 'Banana']

        >>> distinct_words("One two ONE three.", case_sensitive=False)
        ['one', 'two', 'three']

        >>> distinct_words("A B C a b c", case_sensitive=True)
        ['A', 'B', 'C', 'a', 'b', 'c']

        >>> distinct_words("  leading and trailing spaces  ")
        ['leading', 'and', 'trailing', 'spaces']

        >>> distinct_words("No-punctuation_here,just words!")
        ['no', 'punctuation', 'here', 'just', 'words']
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")

    # Use a regular expression to find all sequences of word characters (alphanumeric + underscore).
    # This effectively splits the string by non-word characters and handles punctuation.
    words = _RE_WORD_BOUNDARY.findall(input_string)

    # Use a set to store unique words for efficient lookup and to handle distinctness.
    distinct_words_set = set()
    result_list = [] # Maintain order of first appearance if needed, otherwise could just return list(distinct_words_set)

    for word in words:
        # Determine the word's form for comparison based on case_sensitive flag.
        # If case_sensitive is False, convert to lowercase for comparison.
        # Otherwise, use the word as is.
        processed_word = word if case_sensitive else word.lower()

        if processed_word not in distinct_words_set:
            distinct_words_set.add(processed_word)
            # Add the original word (or lowercase word if case_sensitive is False) to the result list.
            result_list.append(word if case_sensitive else processed_word)

    return result_list


def distinct_split(
    text: str,
    separator: str = ";",
    *,
    strip_tokens: bool = True,
    case_sensitive: bool = True,
) -> str:
    """Split a delimited string, remove duplicate tokens, and re-join.

    Combines ``str.split`` with first-occurrence deduplication in a single
    pass.  Useful for cleaning fields that accumulate repeated values
    after concatenation (e.g. licence lists separated by ``";"``).  Empty
    tokens (or tokens that become empty after stripping) are silently
    discarded.

    Args:
        text: The delimited string to process.
        separator: Delimiter used to split **and** re-join tokens.
        strip_tokens: If ``True`` (default), leading/trailing whitespace
            is stripped from each token before comparison and output.
        case_sensitive: If ``True`` (default), ``"Office365"`` and
            ``"office365"`` are treated as different tokens.  When
            ``False`` the first-seen casing is preserved in the output.

    Returns:
        A string with unique tokens joined by *separator*.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> distinct_split("Office365;PowerBI;Office365;Visio;PowerBI")
        'Office365;PowerBI;Visio'

        >>> distinct_split("a ; b ; a ; c", separator=";")
        'a;b;c'

        >>> distinct_split("Alpha;alpha;ALPHA", case_sensitive=False)
        'Alpha'

        >>> distinct_split("x|y|x|z", separator="|")
        'x|y|z'

        >>> distinct_split("one,,two,,one", separator=",")
        'one,two'

    Cost:
        O(n) where n is the length of *text*.  Uses a single
        iteration with a ``set`` for O(1) membership checks.
    """
    if not isinstance(text, str):
        raise TypeError("Input 'text' must be a string.")

    seen: set[str] = set()
    unique: list[str] = []

    for token in text.split(separator):
        cleaned = token.strip() if strip_tokens else token
        key = cleaned if case_sensitive else cleaned.lower()
        if key and key not in seen:
            seen.add(key)
            unique.append(cleaned)

    return separator.join(unique)


def move_word(input_string: str, from_index: int, to_index: int) -> str:
    """
    Moves a word from one position to another within a string.

    This function splits the input string into words, removes the word at the specified
    'from_index', and inserts it at the 'to_index'. The resulting words are then joined
    back into a single string with spaces. If 'from_index' equals 'to_index', the original
    string is returned unchanged.

    Args:
        input_string (str): The string containing the words to manipulate.
        from_index (int): The 0-based index of the word to move. Must be non-negative
                          and within the range of available words.
        to_index (int): The 0-based index where to insert the moved word. If 'to_index'
                        is greater than the number of words after removal, the word is
                        appended at the end.

    Returns:
        str: The modified string with the word moved to the new position.

    Raises:
        TypeError: If 'input_string' is not a string, or if 'from_index' or 'to_index'
                   are not integers.
        ValueError: If 'from_index' is negative, or if 'from_index' is out of range
                    for the available words.

    Example Usage:
        >>> move_word("hello world this is a test", 0, 4)
        'world this is a hello test'
        >>> move_word("apple banana cherry", 1, 0)
        'banana apple cherry'
        >>> move_word("one two three", 2, 2)
        'one two three'

    Cost:
        O(n), where n is the length of the input string. This is due to string splitting
        and joining operations, which are linear in the string length.
    """
    if not isinstance(input_string, str):
        raise TypeError("Input 'input_string' must be a string.")
    if not isinstance(from_index, int):
        raise TypeError("Input 'from_index' must be an integer.")
    if not isinstance(to_index, int):
        raise TypeError("Input 'to_index' must be an integer.")
    if from_index < 0:
        raise ValueError("Input 'from_index' must be non-negative.")
    if to_index < 0:
        raise ValueError("Input 'to_index' must be non-negative.")

    # Split the string into words
    words = input_string.split()

    # Check if from_index is within range
    if from_index >= len(words):
        raise ValueError(f"Input 'from_index' {from_index} is out of range for {len(words)} words.")

    # If from_index equals to_index, no change needed
    if from_index == to_index:
        return input_string

    # Remove the word at from_index
    word_to_move = words.pop(from_index)

    # Insert the word at to_index, handling if to_index is beyond the current length
    if to_index >= len(words):
        words.append(word_to_move)
    else:
        words.insert(to_index, word_to_move)

    # Join the words back into a string
    return ' '.join(words)


def rotate_words(
    text: Optional[str],
    num_rotations: int,
    rotate_direction: str
) -> Optional[str]:
    """
    Cyclically rotates words within a text string.

    Args:
        text (Optional[str]): The input string containing words to rotate. Can be None.
        num_rotations (int): The number of positions to rotate the words. Must be a non-negative integer.
        rotate_direction (str): The direction of the rotation.
                                Must be 'left' (first word moves to end) or
                                'right' (last word moves to beginning).

    Returns:
        Optional[str]: The string with words rotated, or None if the input 'text' was None.

    Raises:
        ValueError: If 'num_rotations' is negative, or 'rotate_direction' is not 'left' or 'right'.
    """
    # 1. Handle None input immediately
    if text is None:
        return None

    # 2. Input validation
    if not isinstance(num_rotations, int) or num_rotations < 0:
        raise ValueError("num_rotations must be a non-negative integer.")
    
    # Renamed 'first' to 'left' and 'last' to 'right' for clearer directional analogy
    if rotate_direction not in ['left', 'right']:
        raise ValueError("rotate_direction must be 'left' or 'right'.")

    # Split the input string into a list of words
    words = text.split()

    # If there are no words or only one word, no rotation is needed
    if len(words) <= 1:
        return text

    # 3. Optimize for large num_rotations
    # The effective number of rotations is the remainder after dividing by the number of words.
    effective_rotations = num_rotations % len(words)

    # If no effective rotations, return the original string
    if effective_rotations == 0:
        return text

    # 4. Perform rotations using move_word
    for _ in range(effective_rotations):
        if rotate_direction == 'left':
            # Move the first word to the end
            words = text.split()
            text = move_word(text, 0, len(words) - 1)
        elif rotate_direction == 'right':
            # Move the last word to the beginning
            words = text.split()
            text = move_word(text, len(words) - 1, 0)
    
    # 5. Return the rotated string
    return text


def concatenate_strings(string1: str, string2: str) -> str:
    """
    Concatenates two strings into a single string.

    This function combines two string inputs using the `+` operator. While
    `str.join()` is more efficient for a list of many strings, the `+`
    operator is perfectly clear and performant for just two strings.

    Args:
        string1 (str): The first string.
        string2 (str): The second string.

    Returns:
        str: The single concatenated string.

    Raises:
        TypeError: If either input is not a string.

    Example of use:
        >>> first_name = "John"
        >>> last_name = "Doe"
        >>> full_name = concatenate_two_strings(first_name, last_name)
        'JohnDoe'

    Cost:
        The time complexity is O(N + M), where N and M are the lengths of
        the two input strings. The space complexity is O(N + M) to store
        the new resulting string.
    """
    return string1 + string2



def add_quotes(text: Optional[str], quote_type: str = "'") -> Optional[str]:
    """
    Adds single or double quotes to the beginning and end of a string.

    This function wraps the input string with the specified quote character.
    It performs input validation and defaults to single quotes if an invalid
    quote type is provided.

    Args:
        text (Optional[str]): The string to be quoted. Can be None.
        quote_type (str): The type of quote to use. Must be either "'" (single)
                         or '"' (double). Defaults to single quote.

    Returns:
        Optional[str]: The quoted string, or None if the input was None.
                       Non-string inputs are converted to strings before quoting.

    Raises:
        None

    Example of use:
        >>> add_quotes("hello world")
        "'hello world'"
        >>> add_quotes("Python is great", '"')
        '"Python is great"'
        >>> add_quotes("text with 'quotes'", '"')
        '"text with \'quotes\'"'
        >>> add_quotes(None)
        None
        >>> add_quotes(123)
        "'123'"

    Cost:
        O(n) where n is the length of the input string.
    """
    # Define valid quote characters as a constant for clarity and maintainability
    VALID_QUOTES = ("'", '"')

    # Handle None input
    if text is None:
        return None

    # Ensure text is a string (convert if necessary)
    if not isinstance(text, str):
        text = str(text)

    # Validate quote_type and default to single quote if invalid
    if quote_type not in VALID_QUOTES:
        quote_type = "'"

    # Add quotes using f-string for clarity and efficiency
    return f"{quote_type}{text}{quote_type}"


def string_merge(string1: str, string2: str, base: Optional[str] = None) -> str:
    """
    Merges two strings based on a common base string (3-way merge).

    Description:
        Performs a 3-way merge of two strings (`string1` and `string2`) relative to a
        common ancestor (`base`). It automatically resolves non-conflicting changes
        (additions, deletions, modifications). When conflicting changes are detected
        (overlapping edits or different insertions at the same position), it marks
        the conflict region using the pattern `<<<<<<< ++ SOURCE ======= ++ TARGET >>>>>>>`.

    Args:
        string1 (str): The first modified string (source).
        string2 (str): The second modified string (target).
        base (Optional[str]): The common ancestor string. If None, defaults to an empty string.

    Returns:
        str: The merged string, potentially containing conflict markers.

    Raises:
        None

    Usage Example:
        >>> base = '123456'
        >>> s1 = '1234567' # Added 7
        >>> s2 = '0123456' # Added 0
        >>> string_merge(s1, s2, base)
        '01234567'

        >>> s1 = '12a456' # Modified 3 to a
        >>> s2 = '12b456' # Modified 3 to b
        >>> string_merge(s1, s2, base)
        '12<<<<<<< ++ a ======= ++ b >>>>>>>456'

    Cost:
        O(N*M) due to the complexity of calculating diffs (SequenceMatcher).
    """
    if base is None:
        base = ""

    # Helper to extract changes from SequenceMatcher
    def get_changes(original, modified):
        matcher = difflib.SequenceMatcher(None, original, modified)
        # Filter out 'equal' to only get changes
        return [op for op in matcher.get_opcodes() if op[0] != 'equal']

    ops1 = get_changes(base, string1)
    ops2 = get_changes(base, string2)

    # Convert ops to a standardized dictionary format
    # Op format: {'start': int, 'end': int, 'text': str}
    # start/end are indices in 'base'. 'text' is the replacement from string1/string2.
    def normalize_ops(ops, source_string):
        normalized = []
        for tag, i1, i2, j1, j2 in ops:
            normalized.append({
                'start': i1,
                'end': i2,
                'text': source_string[j1:j2]
            })
        return normalized

    changes1 = normalize_ops(ops1, string1)
    changes2 = normalize_ops(ops2, string2)

    output = []
    base_idx = 0
    idx1, idx2 = 0, 0

    while idx1 < len(changes1) or idx2 < len(changes2):
        # Get current changes or dummy if exhausted
        c1 = changes1[idx1] if idx1 < len(changes1) else {'start': float('inf'), 'end': float('inf'), 'text': ''}
        c2 = changes2[idx2] if idx2 < len(changes2) else {'start': float('inf'), 'end': float('inf'), 'text': ''}

        # Determine the next change to process based on start position
        if c1['start'] < c2['start']:
            next_change = c1
            other_change = c2
            is_c1_primary = True
        else:
            next_change = c2
            other_change = c1
            is_c1_primary = False

        # Append base text up to the start of the next change
        # We stop at the start of the *earliest* change to ensure we don't skip over the other one
        limit = min(next_change['start'], other_change['start'])
        if base_idx < limit:
            output.append(base[base_idx:limit])
            base_idx = limit

        # Check for overlap
        # Overlap exists if the 'other' change starts before the 'next' change ends
        # OR if they start at the same position (insertion conflict)
        has_overlap = (other_change['start'] < next_change['end']) or \
                      (other_change['start'] == next_change['start'])

        if not has_overlap:
            # No conflict, apply the change
            output.append(next_change['text'])
            base_idx = next_change['end']
            if is_c1_primary:
                idx1 += 1
            else:
                idx2 += 1
        else:
            # Conflict or identical change
            conflict_start = next_change['start'] # min(c1.start, c2.start)
            conflict_end = max(next_change['end'], other_change['end'])
            
            # Reconstruct the views for the conflict area
            # View = (Base prefix) + (Change text) + (Base suffix)
            
            # For c1:
            prefix1 = base[conflict_start : c1['start']]
            suffix1 = base[c1['end'] : conflict_end]
            view1 = prefix1 + c1['text'] + suffix1
            
            # For c2:
            prefix2 = base[conflict_start : c2['start']]
            suffix2 = base[c2['end'] : conflict_end]
            view2 = prefix2 + c2['text'] + suffix2
            
            if view1 == view2:
                # Identical changes, just apply one
                output.append(view1)
            else:
                # Real conflict
                output.append(f"<<<<<<< ++ {view1} ======= ++ {view2} >>>>>>>")
            
            base_idx = conflict_end
            idx1 += 1
            idx2 += 1

    # Append remaining base text
    if base_idx < len(base):
        output.append(base[base_idx:])

    return "".join(output)


def repeat_string(text: str, times: int) -> str:
    """Repeats a string a given number of times.

    Equivalent to Excel REPT function for fxString.

    Args:
        text: The string to repeat.
        times: Number of times to repeat (must be non-negative).

    Returns:
        The repeated string.

    Raises:
        TypeError: If times is not an integer.
        ValueError: If times is negative.

    Example:
        >>> repeat_string("ab", 3)
        'ababab'
        >>> repeat_string("*", 5)
        '*****'

    Complexity: O(n * times)
    """
    if not isinstance(times, int):
        raise TypeError("times must be an integer")

    if times < 0:
        raise ValueError("times must be non-negative")

    return str(text) * times


def center_string(text: str, width: int, fill_char: str = " ") -> str:
    """Centers a string within a given width using a fill character.

    Args:
        text: The string to center.
        width: The total width of the resulting string.
        fill_char: The padding character.

    Returns:
        The centered string, or the original if it is already wider.

    Example:
        >>> center_string("hello", 11, "-")
        '---hello---'
        >>> center_string("hi", 6)
        '  hi  '

    Complexity: O(width)
    """
    return str(text).center(width, fill_char[0])


def strip_html_tags(text: str) -> str:
    """Removes all HTML/XML tags from a string.

    Args:
        text: The input string containing HTML tags.

    Returns:
        The string with all tags removed.

    Example:
        >>> strip_html_tags("<p>Hello <b>World</b></p>")
        'Hello World'
        >>> strip_html_tags("No tags here")
        'No tags here'

    Complexity: O(n)
    """
    return re.sub(r"<[^>]+>", "", str(text))


def clean_non_printable(text: str) -> str:
    """Removes all non-printable characters (ASCII 0-31) from a string.

    Equivalent to Excel CLEAN function for fxString.

    Args:
        text: The input string.

    Returns:
        The string with non-printable characters removed.

    Example:
        >>> clean_non_printable("Hello\\x00World\\n")
        'HelloWorld'

    Complexity: O(n)
    """
    return "".join(ch for ch in str(text) if ord(ch) >= 32)


def abbreviate(text: str, separator: str = "") -> str:
    """Generates an abbreviation (initials/acronym) from a text string.

    Takes the first letter of each word and joins them.

    Args:
        text: The input text.
        separator: Character placed between initials.

    Returns:
        The abbreviation string in uppercase.

    Example:
        >>> abbreviate("World Health Organization")
        'WHO'
        >>> abbreviate("artificial intelligence", separator=".")
        'A.I.'

    Complexity: O(n)
    """
    words = str(text).split()

    if not words:
        return ""

    initials = separator.join(w[0] for w in words if w)

    if separator:
        initials += separator

    return initials.upper()


def generate_initials(name: str, separator: str = ".") -> str:
    """Generates initials from a person's name.

    Args:
        name: The full name (e.g. "John Ronald Tolkien").
        separator: Character placed after each initial.

    Returns:
        The initials string (e.g. "J.R.T.").

    Example:
        >>> generate_initials("John Ronald Tolkien")
        'J.R.T.'
        >>> generate_initials("Albert Einstein", separator="")
        'AE'

    Complexity: O(n)
    """
    words = str(name).split()

    if not words:
        return ""

    if separator:
        return separator.join(w[0].upper() for w in words if w) + separator

    return "".join(w[0].upper() for w in words if w)


def count_lines(text: str) -> int:
    """Counts the number of lines in a text string.

    Args:
        text: The input text.

    Returns:
        The number of lines (at least 1 for non-empty text, 0 for empty).

    Example:
        >>> count_lines("line1\\nline2\\nline3")
        3
        >>> count_lines("")
        0

    Complexity: O(n)
    """
    if not text:
        return 0

    return text.count("\n") + 1


def get_line(text: str, line_number: int) -> Optional[str]:
    """Returns a specific line from a multiline string (1-indexed).

    Args:
        text: The input multiline text.
        line_number: The line number to retrieve (1-based).

    Returns:
        The requested line, or None if line_number is out of range.

    Example:
        >>> get_line("alpha\\nbeta\\ngamma", 2)
        'beta'
        >>> get_line("single line", 1)
        'single line'

    Complexity: O(n)
    """
    if not text or not isinstance(line_number, int) or line_number < 1:
        return None

    lines = text.split("\n")

    if line_number > len(lines):
        return None

    return lines[line_number - 1]


def remove_blank_lines(text: str) -> str:
    """Removes all blank (empty or whitespace-only) lines from a text string.

    Args:
        text: The input multiline text.

    Returns:
        The text with blank lines removed.

    Example:
        >>> remove_blank_lines("a\\n\\nb\\n  \\nc")
        'a\\nb\\nc'

    Complexity: O(n)
    """
    lines = text.split("\n")
    non_blank = [line for line in lines if line.strip()]
    return "\n".join(non_blank)


def sort_lines(text: str, reverse: bool = False) -> str:
    """Sorts lines in a text string alphabetically.

    Args:
        text: The input multiline text.
        reverse: If True, sorts in descending order.

    Returns:
        The text with lines sorted.

    Example:
        >>> sort_lines("banana\\napple\\ncherry")
        'apple\\nbanana\\ncherry'
        >>> sort_lines("b\\na\\nc", reverse=True)
        'c\\nb\\na'

    Complexity: O(n log n)
    """
    lines = text.split("\n")
    return "\n".join(sorted(lines, reverse=reverse))


def slugify(text: str, separator: str = "-") -> str:
    """Converts text to a URL-friendly slug.

    Removes accents, lowercases, replaces non-alphanumeric characters with
    a separator, and collapses consecutive separators.

    Args:
        text: The input string.
        separator: Character used between words (default ``-``).

    Returns:
        A URL-safe slug string.

    Example:
        >>> slugify("Hola Mundo!")
        'hola-mundo'
        >>> slugify("  Café con Leche  ")
        'cafe-con-leche'
        >>> slugify("Python 3.12 is great", separator="_")
        'python_3_12_is_great'

    Complexity: O(n)
    """
    return _core_to_slug(text, separator=separator)


def wrap_text(text: str, width: int = 80) -> str:
    """Wraps text to a specified line width at word boundaries.

    Splits long lines without breaking words, inserting newlines at the
    nearest whitespace before the width limit.

    Args:
        text: The input string.
        width: Maximum characters per line (default 80).

    Returns:
        Word-wrapped text with newlines inserted.

    Raises:
        ValueError: If width is less than 1.

    Example:
        >>> wrap_text("The quick brown fox jumps over the lazy dog", width=20)
        'The quick brown fox\\njumps over the lazy\\ndog'

    Complexity: O(n)
    """
    if width < 1:
        raise ValueError("Width must be at least 1.")

    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    import textwrap
    return textwrap.fill(text, width=width)


def extract_urls(text: str) -> list[str]:
    """Extracts all URLs from a text string.

    Finds http, https, and ftp URLs using a standard pattern.

    Args:
        text: The input string to scan.

    Returns:
        A list of extracted URL strings.

    Example:
        >>> extract_urls("Visit https://example.com or http://test.org/path")
        ['https://example.com', 'http://test.org/path']
        >>> extract_urls("No links here")
        []

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    pattern = re.compile(r'https?://[^\s<>"\')\]]+|ftp://[^\s<>"\')\]]+')
    return pattern.findall(text)


# ---------------------------------------------------------------------------
# Text layout and word-level operations
# ---------------------------------------------------------------------------


def indent_text(text: str, prefix: str = "  ") -> str:
    """Add a prefix string to the beginning of every line.

    Args:
        text: Input text (may contain multiple lines).
        prefix: String to prepend to each line. Defaults to two spaces.

    Returns:
        Indented text.

    Example:
        >>> indent_text("line1\\nline2", ">> ")
        '>> line1\\n>> line2'

    Complexity: O(n)
    """
    import textwrap

    return textwrap.indent(text, prefix)


def dedent_text(text: str) -> str:
    """Remove common leading whitespace from all lines.

    Args:
        text: Input text with indentation.

    Returns:
        De-indented text.

    Example:
        >>> dedent_text("    hello\\n    world")
        'hello\\nworld'

    Complexity: O(n)
    """
    import textwrap

    return textwrap.dedent(text)


def word_at(text: str, index: int) -> str:
    """Return the word at the given 1-indexed position.

    Args:
        text: Input text.
        index: 1-based word position.

    Returns:
        The word at the specified position.

    Raises:
        IndexError: If index is out of range.

    Example:
        >>> word_at("The quick brown fox", 3)
        'brown'

    Complexity: O(n)
    """

    words = text.split()

    if index < 1 or index > len(words):
        raise IndexError(f"index ({index}) out of range [1, {len(words)}].")

    return words[index - 1]


_RE_EMAIL_PATTERN = re.compile(
    r'[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'
)


def extract_emails(text: str) -> list[str]:
    """Extracts all email addresses from a text string.

    Args:
        text: The input string to scan.

    Returns:
        A list of extracted email address strings.

    Example:
        >>> extract_emails("Contact us at info@example.com or sales@test.org")
        ['info@example.com', 'sales@test.org']
        >>> extract_emails("No emails here")
        []

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    return _RE_EMAIL_PATTERN.findall(text)


def deduplicate_words(text: str) -> str:
    """Removes duplicate words from a text, preserving first occurrence order.

    Args:
        text: The input string.

    Returns:
        Text with duplicates removed.

    Example:
        >>> deduplicate_words("the cat and the dog and the bird")
        'the cat and dog bird'
        >>> deduplicate_words("hello hello hello")
        'hello'

    Complexity: O(n)
    """
    seen: set[str] = set()
    result: list[str] = []

    for word in text.split():

        if word not in seen:
            seen.add(word)
            result.append(word)

    return " ".join(result)


def surround(text: str, wrapper: str) -> str:
    """Wraps a text with a given string on both sides.

    Args:
        text: The input string.
        wrapper: The string to prepend and append.

    Returns:
        The surrounded text.

    Example:
        >>> surround("hello", "**")
        '**hello**'
        >>> surround("world", "'")
        "'world'"

    Complexity: O(1)
    """
    return f"{wrapper}{text}{wrapper}"


def substitute(
    text: str, old_text: str, new_text: str, instance_num: int = 0
) -> str:
    """Substitutes new text for old text in a string.

    Description:
        Replaces occurrences of old_text with new_text. If instance_num
        is 0, replaces all occurrences. Otherwise replaces only the
        Nth occurrence. Equivalent to Excel SUBSTITUTE.

    Args:
        text: The original text.
        old_text: The text to find and replace.
        new_text: The replacement text.
        instance_num: Which occurrence to replace (0 = all, 1 = first, etc.).

    Returns:
        The text with substitutions applied.

    Raises:
        TypeError: If text, old_text, or new_text are not strings.
        ValueError: If instance_num is negative.

    Example:
        >>> substitute("one fish two fish", "fish", "cat")
        'one cat two cat'
        >>> substitute("one fish two fish", "fish", "cat", 2)
        'one fish two cat'

    Complexity: O(n)
    """
    if not isinstance(text, str) or not isinstance(old_text, str) or not isinstance(new_text, str):
        raise TypeError("text, old_text, and new_text must be strings.")

    if instance_num < 0:
        raise ValueError("instance_num must be non-negative.")

    if instance_num == 0:
        return text.replace(old_text, new_text)

    # Replace only the Nth occurrence
    count = 0
    start = 0

    while True:
        pos = text.find(old_text, start)

        if pos == -1:
            break

        count += 1

        if count == instance_num:
            return text[:pos] + new_text + text[pos + len(old_text):]

        start = pos + 1

    return text


def text_before(
    text: str, delimiter: str, instance_num: int = 1
) -> str:
    """Returns text that occurs before a given delimiter.

    Description:
        Returns the portion of text before the Nth occurrence of the
        delimiter. Negative instance_num searches from the end.
        Equivalent to Excel TEXTBEFORE.

    Args:
        text: The input text to search.
        delimiter: The delimiter to search for.
        instance_num: Which occurrence (1 = first, -1 = last, etc.).

    Returns:
        The text before the specified occurrence of the delimiter.

    Raises:
        TypeError: If text or delimiter are not strings.
        ValueError: If instance_num is 0 or delimiter is not found.

    Example:
        >>> text_before("hello-world-test", "-")
        'hello'
        >>> text_before("hello-world-test", "-", 2)
        'hello-world'
        >>> text_before("hello-world-test", "-", -1)
        'hello-world'

    Complexity: O(n)
    """
    if not isinstance(text, str) or not isinstance(delimiter, str):
        raise TypeError("text and delimiter must be strings.")

    if instance_num == 0:
        raise ValueError("instance_num cannot be 0.")

    if instance_num > 0:
        count = 0
        start = 0

        while True:
            pos = text.find(delimiter, start)

            if pos == -1:
                break

            count += 1

            if count == instance_num:
                return text[:pos]

            start = pos + len(delimiter)

        raise ValueError(f"Delimiter '{delimiter}' not found {instance_num} time(s).")

    # Negative: search from end
    count = 0
    end = len(text)

    while True:
        pos = text.rfind(delimiter, 0, end)

        if pos == -1:
            break

        count += 1

        if count == abs(instance_num):
            return text[:pos]

        end = pos

    raise ValueError(f"Delimiter '{delimiter}' not found {abs(instance_num)} time(s) from end.")


def text_after(
    text: str, delimiter: str, instance_num: int = 1
) -> str:
    """Returns text that occurs after a given delimiter.

    Description:
        Returns the portion of text after the Nth occurrence of the
        delimiter. Negative instance_num searches from the end.
        Equivalent to Excel TEXTAFTER.

    Args:
        text: The input text to search.
        delimiter: The delimiter to search for.
        instance_num: Which occurrence (1 = first, -1 = last, etc.).

    Returns:
        The text after the specified occurrence of the delimiter.

    Raises:
        TypeError: If text or delimiter are not strings.
        ValueError: If instance_num is 0 or delimiter is not found.

    Example:
        >>> text_after("hello-world-test", "-")
        'world-test'
        >>> text_after("hello-world-test", "-", 2)
        'test'
        >>> text_after("hello-world-test", "-", -1)
        'test'

    Complexity: O(n)
    """
    if not isinstance(text, str) or not isinstance(delimiter, str):
        raise TypeError("text and delimiter must be strings.")

    if instance_num == 0:
        raise ValueError("instance_num cannot be 0.")

    if instance_num > 0:
        count = 0
        start = 0

        while True:
            pos = text.find(delimiter, start)

            if pos == -1:
                break

            count += 1

            if count == instance_num:
                return text[pos + len(delimiter):]

            start = pos + len(delimiter)

        raise ValueError(f"Delimiter '{delimiter}' not found {instance_num} time(s).")

    # Negative: search from end
    count = 0
    end = len(text)

    while True:
        pos = text.rfind(delimiter, 0, end)

        if pos == -1:
            break

        count += 1

        if count == abs(instance_num):
            return text[pos + len(delimiter):]

        end = pos

    raise ValueError(f"Delimiter '{delimiter}' not found {abs(instance_num)} time(s) from end.")


def text_split(
    text: str,
    col_delimiter: str = None,
    row_delimiter: str = None,
) -> list:
    """Splits text into rows and/or columns using delimiters.

    Description:
        Splits a string by column and/or row delimiters, returning a
        2-D list of strings. Equivalent to Excel TEXTSPLIT.

    Args:
        text: The input text to split.
        col_delimiter: Delimiter for splitting into columns. If None, no
            column splitting.
        row_delimiter: Delimiter for splitting into rows. If None, no
            row splitting.

    Returns:
        A 2-D list of strings if both delimiters are provided,
        a 1-D list if only one delimiter is provided.

    Raises:
        TypeError: If text is not a string.
        ValueError: If both delimiters are None.

    Example:
        >>> text_split("a,b,c", col_delimiter=",")
        ['a', 'b', 'c']
        >>> text_split("a,b;c,d", col_delimiter=",", row_delimiter=";")
        [['a', 'b'], ['c', 'd']]
        >>> text_split("row1;row2;row3", row_delimiter=";")
        ['row1', 'row2', 'row3']

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")

    if col_delimiter is None and row_delimiter is None:
        raise ValueError("At least one delimiter must be provided.")

    if row_delimiter is not None and col_delimiter is not None:
        rows = text.split(row_delimiter)
        return [row.split(col_delimiter) for row in rows]

    if col_delimiter is not None:
        return text.split(col_delimiter)

    return text.split(row_delimiter)


def search_text(
    find_text: str, within_text: str, start_num: int = 1,
) -> int:
    """Case-insensitive text search returning 1-based position.

    Description:
        Finds the position of find_text within within_text,
        ignoring case. Equivalent to Excel SEARCH.

    Args:
        find_text: Text to find.
        within_text: Text to search in.
        start_num: Starting position, 1-based (default 1).

    Returns:
        int: 1-based position of the first match.

    Raises:
        TypeError: If inputs are not valid.
        ValueError: If find_text is not found or start_num < 1.

    Example:
        >>> search_text('margin', 'Profit Margin')
        8
        >>> search_text('M', 'miriam mcgovern')
        1

    Complexity: O(n)
    """
    if not isinstance(find_text, str) or not isinstance(within_text, str):
        raise TypeError("find_text and within_text must be strings.")

    if not isinstance(start_num, int) or start_num < 1:
        raise ValueError("start_num must be an integer >= 1.")

    start_idx = start_num - 1
    position = within_text.lower().find(find_text.lower(), start_idx)

    if position == -1:
        raise ValueError(f"'{find_text}' not found in '{within_text}'.")

    return position + 1


def left_bytes(text: str, num_bytes: int) -> str:
    """Return leading characters from *text* measured in UTF-16 LE bytes.

    Equivalent to VBA ``LeftB``.  One ASCII character = 2 bytes in UTF-16 LE;
    multi-byte characters may occupy more.

    Args:
        text: Source string.
        num_bytes: Number of UTF-16 LE bytes to keep.

    Returns:
        Substring decoded from the first *num_bytes* bytes.

    Example:
        >>> left_bytes("Hello", 6)
        'Hel'

    Complexity: O(n)
    """
    encoded = text.encode("utf-16-le")
    return encoded[:num_bytes].decode("utf-16-le", errors="ignore")


def mid_bytes(text: str, start: int, length: int | None = None) -> str:
    """Return a substring of *text* measured in UTF-16 LE bytes.

    Equivalent to VBA ``MidB``.  *start* is **1-based** (first byte is 1).

    Args:
        text: Source string.
        start: 1-based starting byte position.
        length: Number of bytes to extract.  ``None`` means the rest.

    Returns:
        Substring decoded from the byte slice.

    Example:
        >>> mid_bytes("Hello", 3, 4)
        'el'

    Complexity: O(n)
    """
    encoded = text.encode("utf-16-le")
    start_idx = start - 1

    if length is None:
        chunk = encoded[start_idx:]
    else:
        chunk = encoded[start_idx:start_idx + length]

    return chunk.decode("utf-16-le", errors="ignore")


def right_bytes(text: str, num_bytes: int) -> str:
    """Return trailing characters from *text* measured in UTF-16 LE bytes.

    Equivalent to VBA ``RightB``.

    Args:
        text: Source string.
        num_bytes: Number of UTF-16 LE bytes to keep from the end.

    Returns:
        Substring decoded from the last *num_bytes* bytes.

    Example:
        >>> right_bytes("Hello", 6)
        'llo'

    Complexity: O(n)
    """
    encoded = text.encode("utf-16-le")
    return encoded[-num_bytes:].decode("utf-16-le", errors="ignore")


def clean_nonprintable(text: str) -> str:
    """Remove all nonprintable characters (ASCII 0–31) from text.

    Equivalent to the Excel ``CLEAN`` function.

    Args:
        text: Text to clean.

    Returns:
        String with all control characters removed.

    Example:
        >>> clean_nonprintable("Hello\x00World")
        'HelloWorld'

    Complexity: O(n)
    """
    return "".join(ch for ch in str(text) if ord(ch) >= 32)


def interleave_strings(s1: str, s2: str) -> str:
    """Interleave characters from two strings.

    Characters are taken alternately from *s1* and *s2*. When one
    string is exhausted the remainder of the other is appended.

    Args:
        s1: First string.
        s2: Second string.

    Returns:
        Interleaved result.

    Raises:
        TypeError: If either argument is not a string.

    Example:
        >>> interleave_strings("abc", "12")
        'a1b2c'

    Complexity: O(n + m)
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both arguments must be strings")

    result: list[str] = []
    i = 0

    while i < len(s1) or i < len(s2):

        if i < len(s1):
            result.append(s1[i])

        if i < len(s2):
            result.append(s2[i])

        i += 1

    return "".join(result)


def run_length_encode(text: str) -> str:
    """Run-length encode a string.

    Consecutive identical characters are replaced by their count
    followed by the character.

    Args:
        text: Input string.

    Returns:
        RLE-encoded string.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> run_length_encode("aaabbc")
        '3a2b1c'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    if not text:
        return ""

    parts: list[str] = []
    count = 1

    for i in range(1, len(text)):

        if text[i] == text[i - 1]:
            count += 1
        else:
            parts.append(f"{count}{text[i - 1]}")
            count = 1

    parts.append(f"{count}{text[-1]}")
    return "".join(parts)


def run_length_decode(encoded: str) -> str:
    """Decode a run-length encoded string.

    Expects the format produced by :func:`run_length_encode`
    (count-character pairs like ``"3a2b1c"``).

    Args:
        encoded: RLE-encoded string.

    Returns:
        Decoded string.

    Raises:
        TypeError: If *encoded* is not a string.
        ValueError: If the format is invalid.

    Example:
        >>> run_length_decode("3a2b1c")
        'aaabbc'

    Complexity: O(n)
    """
    if not isinstance(encoded, str):
        raise TypeError("encoded must be a string")

    if not encoded:
        return ""

    parts: list[str] = []
    i = 0

    while i < len(encoded):
        num_start = i

        while i < len(encoded) and encoded[i].isdigit():
            i += 1

        if i == num_start or i >= len(encoded):
            raise ValueError(f"Invalid RLE format at position {i}")

        count = int(encoded[num_start:i])
        parts.append(encoded[i] * count)
        i += 1

    return "".join(parts)


def count_vowels(text: str, lang: str = "en") -> int:
    """Count vowels in a string.

    Args:
        text: Input text.
        lang: Language code (``'en'`` for English, ``'es'`` for Spanish).
              Spanish adds accented vowels.

    Returns:
        Number of vowels found.

    Raises:
        TypeError: If *text* is not a string.

    Example:
        >>> count_vowels("Hello World")
        3

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    vowels = set("aeiouAEIOU")

    if lang.lower() == "es":
        vowels |= set("áéíóúÁÉÍÓÚüÜ")

    return sum(1 for ch in text if ch in vowels)


def count_consonants(text: str, lang: str = "en") -> int:
    """Counts the number of consonants in a text string.

    Non-alphabetic characters are ignored.

    Args:
        text: The input string.
        lang: Language code (``'en'`` or ``'es'``).

    Returns:
        Number of consonant characters.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> count_consonants("Hello World")
        7

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    vowels = set("aeiouAEIOU")

    if lang.lower() == "es":
        vowels |= set("áéíóúÁÉÍÓÚüÜ")

    return sum(1 for ch in text if ch.isalpha() and ch not in vowels)


def longest_word(text: str) -> str:
    """Returns the longest word in a text string.

    Words are split on whitespace.  If the text is empty an empty
    string is returned.  Ties are broken by first occurrence.

    Args:
        text: The input text.

    Returns:
        The longest word found, or ``''``.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> longest_word("the quick brown fox")
        'quick'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = text.split()

    if not words:
        return ""

    return max(words, key=len)


def shortest_word(text: str) -> str:
    """Returns the shortest word in a text string.

    Words are split on whitespace.  If the text is empty an empty
    string is returned.  Ties are broken by first occurrence.

    Args:
        text: The input text.

    Returns:
        The shortest word found, or ``''``.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> shortest_word("the quick brown fox")
        'the'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    words = text.split()

    if not words:
        return ""

    return min(words, key=len)


def reverse_words(text: str) -> str:
    """Reverses the order of words in a string.

    Individual words keep their original spelling; only their
    sequence is inverted.

    Args:
        text: The input text.

    Returns:
        Text with word order reversed.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> reverse_words("hello world foo")
        'foo world hello'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return " ".join(text.split()[::-1])


def extract_hashtags(text: str) -> list[str]:
    """Extracts ``#hashtag`` tokens from a text string.

    A hashtag starts with ``#`` followed by one or more word characters
    (letters, digits, underscore).

    Args:
        text: The input text.

    Returns:
        List of hashtags **including** the leading ``#``.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> extract_hashtags("Hello #world #python3")
        ['#world', '#python3']

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return re.findall(r"#\w+", text)


def extract_mentions(text: str) -> list[str]:
    """Extracts ``@mention`` tokens from a text string.

    A mention starts with ``@`` followed by one or more word characters.

    Args:
        text: The input text.

    Returns:
        List of mentions **including** the leading ``@``.

    Raises:
        TypeError: If text is not a string.

    Example:
        >>> extract_mentions("Hi @alice and @bob!")
        ['@alice', '@bob']

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    return re.findall(r"@\w+", text)


def count_syllables(text: str, lang: str = "en") -> int:
    """Estimates the total number of syllables in a text.

    Description:
        Uses a heuristic vowel-cluster approach for English and a
        vowel-group count for Spanish.  Intended for readability
        metrics, not linguistic accuracy.

    Args:
        text: The input text.
        lang: Language code (``'en'`` or ``'es'``).

    Returns:
        Estimated syllable count (minimum 1 per word).

    Raises:
        TypeError: If *text* is not a string.
        ValueError: If *lang* is not ``'en'`` or ``'es'``.

    Usage Example:
        >>> count_syllables("beautiful day")
        4

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    lang = lang.lower()

    if lang not in ("en", "es"):
        raise ValueError("lang must be 'en' or 'es'")

    words = re.findall(r"[a-zA-ZáéíóúüñÁÉÍÓÚÜÑ]+", text.lower())
    total = 0

    for word in words:

        if lang == "en":
            # Remove trailing silent-e
            w = word

            if w.endswith("e") and len(w) > 2:
                w = w[:-1]

            count = len(re.findall(r"[aeiouy]+", w))

            if count == 0:
                count = 1

            total += count

        else:
            count = len(re.findall(r"[aeiouáéíóúü]+", word))

            if count == 0:
                count = 1

            total += count

    return max(total, 1) if words else 0


def soundex(text: str) -> str:
    """Computes the Soundex phonetic code for a word.

    Description:
        Implements the American Soundex algorithm (Robert C. Russell,
        1918).  Useful for matching names that sound alike but are
        spelled differently.

    Args:
        text: A single word to encode.

    Returns:
        A 4-character Soundex code (letter + 3 digits).

    Raises:
        TypeError: If *text* is not a string.
        ValueError: If *text* contains no alphabetic characters.

    Usage Example:
        >>> soundex("Robert")
        'R163'
        >>> soundex("Rupert")
        'R163'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    word = re.sub(r"[^a-zA-Z]", "", text).upper()

    if not word:
        raise ValueError("text must contain at least one alphabetic character")

    mapping = {
        "B": "1", "F": "1", "P": "1", "V": "1",
        "C": "2", "G": "2", "J": "2", "K": "2",
        "Q": "2", "S": "2", "X": "2", "Z": "2",
        "D": "3", "T": "3",
        "L": "4",
        "M": "5", "N": "5",
        "R": "6",
    }

    code = word[0]
    prev = mapping.get(word[0], "0")

    for ch in word[1:]:
        digit = mapping.get(ch, "0")

        # H and W do not separate identical adjacent codes
        if ch in ("H", "W"):
            continue

        if digit != "0" and digit != prev:
            code += digit

        # Only update prev for coded consonants and vowels (not H/W)
        prev = digit

        if len(code) == 4:
            break

    return code.ljust(4, "0")


def metaphone(text: str) -> str:
    """Computes the Metaphone phonetic code for a word.

    Description:
        Implements Lawrence Philips' original Metaphone algorithm (1990).
        More accurate than Soundex for English words.

    Args:
        text: A single word to encode.

    Returns:
        The Metaphone code string.

    Raises:
        TypeError: If *text* is not a string.
        ValueError: If *text* contains no alphabetic characters.

    Usage Example:
        >>> metaphone("Thompson")
        'TMPSN'
        >>> metaphone("Smith")
        'SM0'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    word = re.sub(r"[^a-zA-Z]", "", text).upper()

    if not word:
        raise ValueError("text must contain at least one alphabetic character")

    # Drop initial silent letter pairs
    if word[:2] in ("AE", "GN", "KN", "PN", "WR"):
        word = word[1:]

    vowels = set("AEIOU")
    result: list[str] = []
    i = 0

    while i < len(word):
        c = word[i]
        nxt = word[i + 1] if i + 1 < len(word) else ""

        if c in vowels:

            if i == 0:
                result.append(c)

            i += 1
            continue

        if c == "B":

            if i == 0 or word[i - 1] != "M":
                result.append("B")

        elif c == "C":

            if nxt in ("E", "I", "Y"):
                result.append("S")
            else:
                result.append("K")

        elif c == "D":

            if nxt in ("G",) and i + 2 < len(word) and word[i + 2] in ("E", "I", "Y"):
                result.append("J")
            else:
                result.append("T")

        elif c == "F":
            result.append("F")

        elif c == "G":

            if nxt in ("H",) and i + 2 < len(word) and word[i + 2] not in vowels:
                pass
            elif nxt in ("N",) and (i + 2 >= len(word)):
                pass
            elif i > 0 and word[i - 1] == "G":
                pass
            else:

                if nxt in ("E", "I", "Y"):
                    result.append("J")
                else:
                    result.append("K")

        elif c == "H":

            if nxt in vowels and (i == 0 or word[i - 1] not in vowels):
                result.append("H")

        elif c == "J":
            result.append("J")

        elif c == "K":

            if i == 0 or word[i - 1] != "C":
                result.append("K")

        elif c == "L":
            result.append("L")

        elif c == "M":
            result.append("M")

        elif c == "N":
            result.append("N")

        elif c == "P":

            if nxt == "H":
                result.append("F")
                i += 1
            else:
                result.append("P")

        elif c == "Q":
            result.append("K")

        elif c == "R":
            result.append("R")

        elif c == "S":

            if nxt == "H" or (nxt == "I" and i + 2 < len(word) and word[i + 2] in ("O", "A")):
                result.append("X")
                i += 1
            else:
                result.append("S")

        elif c == "T":

            if nxt == "H":
                result.append("0")
                i += 1
            else:
                result.append("T")

        elif c == "V":
            result.append("F")

        elif c == "W" or c == "Y":

            if nxt in vowels:
                result.append(c)

        elif c == "X":
            result.append("KS")

        elif c == "Z":
            result.append("S")

        i += 1

    return "".join(result)


def extract_domain_from_url(url: str) -> str:
    """Extracts the domain (hostname) from a URL string.

    Description:
        Handles URLs with or without a scheme.  Returns the netloc
        component stripped of any ``www.`` prefix, port, auth,
        and path segments.

    Args:
        url: The URL to extract from.

    Returns:
        The domain name (e.g. ``'example.com'``).

    Raises:
        TypeError: If *url* is not a string.
        ValueError: If no domain can be extracted.

    Usage Example:
        >>> extract_domain_from_url("https://www.example.com/path?q=1")
        'example.com'

    Complexity: O(n)
    """
    if not isinstance(url, str):
        raise TypeError("url must be a string")

    from urllib.parse import urlparse

    cleaned = url.strip()

    if "://" not in cleaned:
        cleaned = "http://" + cleaned

    parsed = urlparse(cleaned)
    host = parsed.hostname or ""

    if not host:
        raise ValueError(f"Cannot extract domain from '{url}'")

    if host.startswith("www."):
        host = host[4:]

    return host


def nysiis(text: str) -> str:
    """Compute the NYSIIS (New York State Identification and Intelligence System) phonetic code.

    Description:
        Produces a phonetic encoding that is generally more accurate
        than Soundex for English names.  Applies prefix/suffix
        transformations, then walks through the string applying
        context-sensitive rules.

    Args:
        text: The text to encode.

    Returns:
        The NYSIIS code (uppercase, up to 6 characters).

    Raises:
        TypeError: If *text* is not a string.
        ValueError: If *text* is empty after cleaning.

    Usage Example:
        >>> nysiis("Watkins")
        'WATCAN'
        >>> nysiis("Johnson")
        'JANSAN'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    name = re.sub(r"[^A-Za-z]", "", text).upper()

    if not name:
        raise ValueError("text must contain at least one alphabetic character")

    # Step 1: prefix substitutions
    prefix_map = [
        ("MAC", "MCC"), ("KN", "NN"), ("K", "C"),
        ("PH", "FF"), ("PF", "FF"), ("SCH", "SSS"),
    ]

    for old, new in prefix_map:

        if name.startswith(old):
            name = new + name[len(old):]
            break

    # Step 2: suffix substitutions
    suffix_map = [
        ("EE", "Y"), ("IE", "Y"), ("DT", "D"),
        ("RT", "D"), ("RD", "D"), ("NT", "D"), ("ND", "D"),
    ]

    for old, new in suffix_map:

        if name.endswith(old):
            name = name[: -len(old)] + new
            break

    # Step 3: first character is kept
    first = name[0]
    result = [first]
    i = 1

    while i < len(name):
        c = name[i]

        if c == "E" and i + 1 < len(name) and name[i + 1] == "V":
            result.append("AF")
            i += 2
            continue

        if c in "AEIOU":
            result.append("A")
            i += 1
            continue

        if c == "Q":
            result.append("G")
        elif c == "Z":
            result.append("S")
        elif c == "M":
            result.append("N")
        elif c == "K":
            result.append("C" if i + 1 < len(name) and name[i + 1] == "N" else "C")
        elif c == "S" and i + 2 < len(name) and name[i + 1 : i + 3] == "CH":
            result.append("SS")
            i += 3
            continue
        elif c == "P" and i + 1 < len(name) and name[i + 1] == "H":
            result.append("FF")
            i += 2
            continue
        elif c == "H":
            prev_vowel = name[i - 1] in "AEIOU" if i > 0 else False
            next_vowel = name[i + 1] in "AEIOU" if i + 1 < len(name) else False

            if not prev_vowel or not next_vowel:
                result.append(result[-1] if result else c)
            else:
                result.append("H")
        elif c == "W":
            prev_vowel = name[i - 1] in "AEIOU" if i > 0 else False

            if prev_vowel:
                result.append(result[-1] if result else c)
            else:
                result.append("W")
        else:
            result.append(c)

        i += 1

    # Remove trailing 'S'
    code = "".join(result)

    if code.endswith("S") and len(code) > 1:
        code = code[:-1]

    # Replace trailing 'AY' with 'Y'
    if code.endswith("AY"):
        code = code[:-2] + "Y"

    # Remove trailing 'A'
    if code.endswith("A") and len(code) > 1:
        code = code[:-1]

    # Collapse repeated characters
    collapsed = [code[0]]

    for ch in code[1:]:

        if ch != collapsed[-1]:
            collapsed.append(ch)

    return "".join(collapsed)[:6]


def double_metaphone(text: str) -> tuple:
    """Compute the Double Metaphone phonetic encoding.

    Description:
        Produces a primary and alternate phonetic key.  Handles
        Germanic, Celtic, Romance, and Slavic name origins better
        than the original Metaphone.

    Args:
        text: The text to encode.

    Returns:
        A tuple ``(primary, alternate)`` of phonetic codes (uppercase).

    Raises:
        TypeError: If *text* is not a string.
        ValueError: If *text* is empty after cleaning.

    Usage Example:
        >>> double_metaphone("Smith")
        ('SM0', 'XMT')
        >>> double_metaphone("Schmidt")
        ('XMT', 'SMT')

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    original = text.strip().upper()

    if not original:
        raise ValueError("text must not be empty")

    # Pad for safe look-ahead
    word = original + "     "
    length = len(original)
    primary = []
    secondary = []
    current = 0

    def _at(pos: int, size: int) -> str:
        return word[pos : pos + size]

    def _vowel(c: str) -> bool:
        return c in "AEIOUY"

    # Skip silent start
    if _at(0, 2) in ("GN", "KN", "PN", "AE", "WR"):
        current += 1

    # Handle initial 'X'
    if word[0] == "X":
        primary.append("S")
        secondary.append("S")
        current += 1

    while current < length:

        if len(primary) >= 4 and len(secondary) >= 4:
            break

        c = word[current]

        if c in "AEIOUY":

            if current == 0:
                primary.append("A")
                secondary.append("A")

            current += 1
            continue

        if c == "B":
            primary.append("P")
            secondary.append("P")
            current += 2 if word[current + 1] == "B" else 1
            continue

        if c == "C":

            if _at(current, 2) == "CH":
                primary.append("X")
                secondary.append("X")
                current += 2
            elif _at(current, 2) in ("CI", "CE", "CY"):
                primary.append("S")
                secondary.append("S")
                current += 2
            else:
                primary.append("K")
                secondary.append("K")
                current += 2 if _at(current, 2) in ("CK", "CC", "CQ") else 1

            continue

        if c == "D":

            if _at(current, 2) in ("DG",):
                nxt2 = word[current + 2]

                if nxt2 in "IEY":
                    primary.append("J")
                    secondary.append("J")
                    current += 3
                else:
                    primary.append("TK")
                    secondary.append("TK")
                    current += 2
            else:
                primary.append("T")
                secondary.append("T")
                current += 2 if _at(current, 2) in ("DT", "DD") else 1

            continue

        if c == "F":
            primary.append("F")
            secondary.append("F")
            current += 2 if word[current + 1] == "F" else 1
            continue

        if c == "G":
            nxt = word[current + 1]

            if nxt == "H":

                if current > 0 and not _vowel(word[current - 1]):
                    primary.append("K")
                    secondary.append("K")
                    current += 2
                elif current == 0:

                    if word[current + 2] == "I":
                        primary.append("J")
                        secondary.append("J")
                    else:
                        primary.append("K")
                        secondary.append("K")

                    current += 2
                else:
                    current += 2
            elif nxt in "EIY":
                primary.append("J")
                secondary.append("K")
                current += 2
            else:
                primary.append("K")
                secondary.append("K")
                current += 2 if nxt == "G" else 1

            continue

        if c == "H":

            if _vowel(word[current + 1]) and (current == 0 or _vowel(word[current - 1])):
                primary.append("H")
                secondary.append("H")
                current += 2
            else:
                current += 1

            continue

        if c == "J":
            primary.append("J")
            secondary.append("H")
            current += 2 if word[current + 1] == "J" else 1
            continue

        if c == "K":
            primary.append("K")
            secondary.append("K")
            current += 2 if word[current + 1] == "K" else 1
            continue

        if c == "L":
            primary.append("L")
            secondary.append("L")
            current += 2 if word[current + 1] == "L" else 1
            continue

        if c == "M":
            primary.append("M")
            secondary.append("M")
            current += 2 if word[current + 1] == "M" else 1
            continue

        if c == "N":
            primary.append("N")
            secondary.append("N")
            current += 2 if word[current + 1] == "N" else 1
            continue

        if c == "P":

            if word[current + 1] == "H":
                primary.append("F")
                secondary.append("F")
                current += 2
            else:
                primary.append("P")
                secondary.append("P")
                current += 2 if word[current + 1] == "P" else 1

            continue

        if c == "Q":
            primary.append("K")
            secondary.append("K")
            current += 2 if word[current + 1] == "Q" else 1
            continue

        if c == "R":
            primary.append("R")
            secondary.append("R")
            current += 2 if word[current + 1] == "R" else 1
            continue

        if c == "S":

            if _at(current, 2) == "SH":
                primary.append("X")
                secondary.append("X")
                current += 2
            elif _at(current, 3) == "SCH":
                primary.append("SK")
                secondary.append("SK")
                current += 3
            elif _at(current, 2) in ("SI", "SY"):
                primary.append("S")
                secondary.append("S")
                current += 2
            else:
                primary.append("S")
                secondary.append("S")
                current += 2 if word[current + 1] == "S" else 1

            continue

        if c == "T":

            if _at(current, 2) == "TH":
                primary.append("0")  # theta
                secondary.append("T")
                current += 2
            else:
                primary.append("T")
                secondary.append("T")
                current += 2 if word[current + 1] in "T" else 1

            continue

        if c == "V":
            primary.append("F")
            secondary.append("F")
            current += 2 if word[current + 1] == "V" else 1
            continue

        if c == "W":

            if _vowel(word[current + 1]):
                primary.append("A")
                secondary.append("F")
                current += 1
            else:
                current += 1

            continue

        if c == "X":
            primary.append("KS")
            secondary.append("KS")
            current += 2 if word[current + 1] == "X" else 1
            continue

        if c == "Z":
            primary.append("S")
            secondary.append("TS")
            current += 2 if word[current + 1] == "Z" else 1
            continue

        current += 1

    return ("".join(primary)[:4], "".join(secondary)[:4])


def cologne_phonetic(text: str) -> str:
    """Compute the Kölner Phonetik (Cologne Phonetic) code.

    Description:
        A phonetic algorithm optimised for the German language.
        Maps characters to digit codes based on context (preceding
        and following characters).

    Args:
        text: The text to encode.

    Returns:
        The Cologne phonetic code as a digit string.

    Raises:
        TypeError: If *text* is not a string.
        ValueError: If *text* is empty after cleaning.

    Usage Example:
        >>> cologne_phonetic("Müller")
        '657'
        >>> cologne_phonetic("Schmidt")
        '862'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Normalize: remove non-alpha, upper
    import unicodedata

    normalized = unicodedata.normalize("NFKD", text)
    # Map special German chars
    name = normalized.upper()
    name = name.replace("Ä", "A").replace("Ö", "O").replace("Ü", "U").replace("ß", "SS")
    name = re.sub(r"[^A-Z]", "", name)

    if not name:
        raise ValueError("text must contain at least one alphabetic character")

    codes = []

    for i, c in enumerate(name):
        prev_c = name[i - 1] if i > 0 else ""
        next_c = name[i + 1] if i + 1 < len(name) else ""

        if c in "AEIJOUY":
            code = "0"
        elif c == "H":
            code = ""
        elif c == "B":
            code = "1"
        elif c == "P":
            code = "1" if next_c != "H" else "3"
        elif c in "DT":
            code = "8" if next_c in "CSZ" else "2"
        elif c in "FVW":
            code = "3"
        elif c in "GKQ":
            code = "4"
        elif c == "C":

            if i == 0:
                code = "4" if next_c in "AHKLOQRUX" else "8"
            else:
                code = "4" if prev_c in "SZ" or next_c in "AHKOQUX" else "8"

        elif c == "X":
            code = "48" if prev_c not in "CKQ" else "8"
        elif c == "L":
            code = "5"
        elif c in "MN":
            code = "6"
        elif c == "R":
            code = "7"
        elif c in "SZ":
            code = "8"
        else:
            code = ""

        codes.append(code)

    # Collapse consecutive identical codes
    result = codes[0] if codes else ""

    for cd in codes[1:]:

        if cd and cd != result[-1:]:
            result += cd

    # Remove all '0' except if first
    if result:
        result = result[0] + result[1:].replace("0", "")

    return result


def longest_common_prefix(s1: str, s2: str) -> str:
    """Return the longest common prefix of two strings.

    Description:
        Compares character-by-character from the start until a
        mismatch is found.

    Args:
        s1: First string.
        s2: Second string.

    Returns:
        The longest common prefix (may be empty string).

    Raises:
        TypeError: If either argument is not a string.

    Usage Example:
        >>> longest_common_prefix("interstellar", "internet")
        'inter'
        >>> longest_common_prefix("abc", "xyz")
        ''

    Complexity: O(min(n, m))
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("s1 and s2 must be strings")

    i = 0

    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i += 1

    return s1[:i]


def longest_common_suffix(s1: str, s2: str) -> str:
    """Return the longest common suffix of two strings.

    Description:
        Compares character-by-character from the end until a
        mismatch is found.

    Args:
        s1: First string.
        s2: Second string.

    Returns:
        The longest common suffix (may be empty string).

    Raises:
        TypeError: If either argument is not a string.

    Usage Example:
        >>> longest_common_suffix("testing", "running")
        'ning'
        >>> longest_common_suffix("abc", "xyz")
        ''

    Complexity: O(min(n, m))
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("s1 and s2 must be strings")

    i = 0

    while i < len(s1) and i < len(s2) and s1[-(i + 1)] == s2[-(i + 1)]:
        i += 1

    return s1[len(s1) - i :] if i > 0 else ""


def normalize_unicode(text: str, form: str = "NFC") -> str:
    """Normalize a Unicode string to a canonical form.

    Description:
        Uses Python's ``unicodedata.normalize`` with the specified
        normalization form: NFC, NFD, NFKC, or NFKD.

    Args:
        text: The text to normalize.
        form: Normalization form (``'NFC'``, ``'NFD'``, ``'NFKC'``,
            or ``'NFKD'``).

    Returns:
        The normalized string.

    Raises:
        TypeError: If *text* is not a string.
        ValueError: If *form* is not a valid normalization form.

    Usage Example:
        >>> normalize_unicode("café", "NFC") == normalize_unicode("café", "NFC")
        True

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    form = form.upper()
    valid_forms = ("NFC", "NFD", "NFKC", "NFKD")

    if form not in valid_forms:
        raise ValueError(f"form must be one of {valid_forms}")

    import unicodedata

    return unicodedata.normalize(form, text)


def generate_password(length: int = 16, *, uppercase: bool = True,
                      lowercase: bool = True, digits: bool = True,
                      special: bool = True) -> str:
    """Generate a cryptographically secure random password.

    Description:
        Uses ``secrets.choice`` for randomness.  At least one character
        from each enabled category is guaranteed, then the remaining
        positions are filled from the combined pool and shuffled.

    Args:
        length: Total password length (>= number of enabled categories).
        uppercase: Include A-Z. Default True.
        lowercase: Include a-z. Default True.
        digits: Include 0-9. Default True.
        special: Include ``!@#$%^&*()-_=+``. Default True.

    Returns:
        A random password string of the requested length.

    Raises:
        TypeError: If *length* is not an integer.
        ValueError: If *length* is too short or no category is enabled.

    Usage Example:
        >>> pwd = generate_password(20)
        >>> len(pwd)
        20

    Complexity: O(n) where n = length.
    """
    import secrets

    if not isinstance(length, int):
        raise TypeError("length must be an integer.")

    pools: list = []
    required: list = []

    if uppercase:
        pool_upper = string.ascii_uppercase
        pools.append(pool_upper)
        required.append(secrets.choice(pool_upper))

    if lowercase:
        pool_lower = string.ascii_lowercase
        pools.append(pool_lower)
        required.append(secrets.choice(pool_lower))

    if digits:
        pool_digits = string.digits
        pools.append(pool_digits)
        required.append(secrets.choice(pool_digits))

    if special:
        pool_special = "!@#$%^&*()-_=+"
        pools.append(pool_special)
        required.append(secrets.choice(pool_special))

    if not pools:
        raise ValueError("At least one character category must be enabled.")

    if length < len(required):
        raise ValueError(f"length must be >= {len(required)} for the enabled categories.")

    combined = "".join(pools)
    remaining = [secrets.choice(combined) for _ in range(length - len(required))]
    result = required + remaining

    # Shuffle using Fisher-Yates with secrets
    for i in range(len(result) - 1, 0, -1):
        j = secrets.randbelow(i + 1)
        result[i], result[j] = result[j], result[i]

    return "".join(result)


# ---------------------------------------------------------------------------
# Phase 21 – Batch 32: String Operations (1 of 4)
# ---------------------------------------------------------------------------

def pad_start(text: str, width: int, fillchar: str = " ") -> str:
    """Pad *text* on the left to reach *width* characters.

    Args:
        text: Source string.
        width: Desired minimum width.
        fillchar: Single character to pad with (default space).

    Returns:
        Left-padded string.

    Raises:
        TypeError: If text is not a string or width is not int.
        ValueError: If fillchar is not a single character.

    Usage Example:
        >>> pad_start('42', 5, '0')
        '00042'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    if not isinstance(width, int):
        raise TypeError("width must be an integer.")
    if not isinstance(fillchar, str) or len(fillchar) != 1:
        raise ValueError("fillchar must be a single character.")
    return text.rjust(width, fillchar)


def pad_end(text: str, width: int, fillchar: str = " ") -> str:
    """Pad *text* on the right to reach *width* characters.

    Args:
        text: Source string.
        width: Desired minimum width.
        fillchar: Single character to pad with (default space).

    Returns:
        Right-padded string.

    Raises:
        TypeError: If text is not a string or width is not int.
        ValueError: If fillchar is not a single character.

    Usage Example:
        >>> pad_end('hi', 5, '.')
        'hi...'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    if not isinstance(width, int):
        raise TypeError("width must be an integer.")
    if not isinstance(fillchar, str) or len(fillchar) != 1:
        raise ValueError("fillchar must be a single character.")
    return text.ljust(width, fillchar)


def pad_center(text: str, width: int, fillchar: str = " ") -> str:
    """Centre *text* within *width* characters, padding both sides.

    Args:
        text: Source string.
        width: Desired minimum width.
        fillchar: Single character to pad with (default space).

    Returns:
        Centre-padded string.

    Raises:
        TypeError: If text is not a string or width is not int.
        ValueError: If fillchar is not a single character.

    Usage Example:
        >>> pad_center('hi', 6, '-')
        '--hi--'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    if not isinstance(width, int):
        raise TypeError("width must be an integer.")
    if not isinstance(fillchar, str) or len(fillchar) != 1:
        raise ValueError("fillchar must be a single character.")
    return text.center(width, fillchar)


def remove_prefix(text: str, prefix: str) -> str:
    """Remove *prefix* from the start of *text* if present.

    Args:
        text: Source string.
        prefix: Prefix to remove.

    Returns:
        String without the leading prefix.

    Raises:
        TypeError: If arguments are not strings.

    Usage Example:
        >>> remove_prefix('unhappy', 'un')
        'happy'

    Complexity: O(n)
    """
    if not isinstance(text, str) or not isinstance(prefix, str):
        raise TypeError("Both arguments must be strings.")
    if text.startswith(prefix):
        return text[len(prefix):]
    return text


def remove_suffix(text: str, suffix: str) -> str:
    """Remove *suffix* from the end of *text* if present.

    Args:
        text: Source string.
        suffix: Suffix to remove.

    Returns:
        String without the trailing suffix.

    Raises:
        TypeError: If arguments are not strings.

    Usage Example:
        >>> remove_suffix('filename.txt', '.txt')
        'filename'

    Complexity: O(n)
    """
    if not isinstance(text, str) or not isinstance(suffix, str):
        raise TypeError("Both arguments must be strings.")
    if suffix and text.endswith(suffix):
        return text[:-len(suffix)]
    return text


# ---------------------------------------------------------------------------
# Phase 21 – Batch 33: String Operations (2 of 4)
# ---------------------------------------------------------------------------

def collapse_whitespace(text: str) -> str:
    """Replace consecutive whitespace with a single space and strip edges.

    Args:
        text: Source string.

    Returns:
        String with normalised whitespace.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> collapse_whitespace('  hello   world  ')
        'hello world'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    import re as _re
    return _re.sub(r'\s+', ' ', text).strip()


def truncate_with_ellipsis(text: str, max_len: int, ellipsis: str = "...") -> str:
    """Truncate *text* to *max_len* characters, appending *ellipsis* if cut.

    Args:
        text: Source string.
        max_len: Maximum length INCLUDING ellipsis.
        ellipsis: Suffix to append (default ``"..."``).

    Returns:
        Truncated string.

    Raises:
        TypeError: If types are invalid.
        ValueError: If max_len < len(ellipsis).

    Usage Example:
        >>> truncate_with_ellipsis('hello world', 8)
        'hello...'

    Complexity: O(n)
    """
    if not isinstance(text, str) or not isinstance(ellipsis, str):
        raise TypeError("text and ellipsis must be strings.")
    if not isinstance(max_len, int):
        raise TypeError("max_len must be an integer.")
    if max_len < len(ellipsis):
        raise ValueError("max_len must be >= len(ellipsis).")
    if len(text) <= max_len:
        return text
    return text[:max_len - len(ellipsis)] + ellipsis


def camel_to_snake(text: str) -> str:
    """Convert camelCase or PascalCase to snake_case.

    Args:
        text: camelCase or PascalCase string.

    Returns:
        snake_case string.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> camel_to_snake('helloWorld')
        'hello_world'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    import re as _re
    result = _re.sub(r'([A-Z])', r'_\1', text).lower()
    return result.lstrip("_")


def count_occurrences(text: str, sub: str) -> int:
    """Count non-overlapping occurrences of *sub* in *text*.

    Args:
        text: Source string.
        sub: Substring to count.

    Returns:
        Number of occurrences.

    Raises:
        TypeError: If arguments are not strings.

    Usage Example:
        >>> count_occurrences('banana', 'an')
        2

    Complexity: O(n·m)
    """
    if not isinstance(text, str) or not isinstance(sub, str):
        raise TypeError("Both arguments must be strings.")
    return text.count(sub)


def repeat_each_char(text: str, n: int) -> str:
    """Repeat each character in *text* n times.

    Args:
        text: Source string.
        n: Repetition count (≥ 0).

    Returns:
        String with each character repeated.

    Raises:
        TypeError: If types are incorrect.
        ValueError: If n < 0.

    Usage Example:
        >>> repeat_each_char('abc', 2)
        'aabbcc'

    Complexity: O(n·m)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
    if n < 0:
        raise ValueError("n must be >= 0.")
    return "".join(ch * n for ch in text)


def zigzag_case(text: str) -> str:
    """Alternate character case: even indices lower, odd indices upper.

    Args:
        text: Source string.

    Returns:
        Zigzag-cased string.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> zigzag_case('hello')
        'hElLo'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    return "".join(
        ch.upper() if i % 2 else ch.lower() for i, ch in enumerate(text)
    )


def swap_case(text: str) -> str:
    """Swap the case of every character in *text*.

    Args:
        text: Source string.

    Returns:
        Case-swapped string.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> swap_case('Hello World')
        'hELLO wORLD'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    return text.swapcase()


def caesar_cipher(text: str, shift: int) -> str:
    """Apply Caesar cipher with the given shift (positive = right).

    Only shifts ASCII letters; other characters are unchanged.

    Args:
        text: Source string.
        shift: Number of positions to shift.

    Returns:
        Ciphered string.

    Raises:
        TypeError: If types are incorrect.

    Usage Example:
        >>> caesar_cipher('abc', 3)
        'def'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    if not isinstance(shift, int):
        raise TypeError("shift must be an integer.")
    result = []
    for ch in text:
        if 'a' <= ch <= 'z':
            result.append(chr((ord(ch) - ord('a') + shift) % 26 + ord('a')))
        elif 'A' <= ch <= 'Z':
            result.append(chr((ord(ch) - ord('A') + shift) % 26 + ord('A')))
        else:
            result.append(ch)
    return "".join(result)


def rot13(text: str) -> str:
    """Apply ROT13 rotation to *text*.

    Args:
        text: Source string.

    Returns:
        ROT13-rotated string.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> rot13('hello')
        'uryyb'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    return caesar_cipher(text, 13)


def title_case(text: str) -> str:
    """Convert *text* to title case, capitalising the first letter of each word.

    Args:
        text: Source string.

    Returns:
        Title-cased string.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> title_case('hello world')
        'Hello World'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    return text.title()


def snake_to_camel(text: str) -> str:
    """Convert snake_case to camelCase.

    Args:
        text: Snake-cased string.

    Returns:
        camelCase string.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> snake_to_camel('hello_world')
        'helloWorld'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    parts = text.split("_")
    if not parts:
        return text
    return parts[0] + "".join(p.capitalize() for p in parts[1:])


# ---------------------------------------------------------------------------
# Phase 21 – Batch 34: String Operations (3 of 4)
# ---------------------------------------------------------------------------

def kebab_case(text: str) -> str:
    """Convert whitespace-separated *text* to kebab-case (lowercase, hyphens).

    Args:
        text: Source string.

    Returns:
        kebab-cased string.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> kebab_case('Hello World')
        'hello-world'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    import re as _re
    return _re.sub(r'\s+', '-', text.strip()).lower()


def constant_case(text: str) -> str:
    """Convert whitespace-separated *text* to CONSTANT_CASE.

    Args:
        text: Source string.

    Returns:
        CONSTANT_CASE string.

    Raises:
        TypeError: If text is not a string.

    Usage Example:
        >>> constant_case('Hello World')
        'HELLO_WORLD'

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    import re as _re
    return _re.sub(r'\s+', '_', text.strip()).upper()


def chunk_string(text: str, size: int) -> list:
    """Split *text* into chunks of *size* characters.

    Args:
        text: Source string.
        size: Chunk width (> 0).

    Returns:
        List of string chunks.

    Raises:
        TypeError: If types are incorrect.
        ValueError: If size ≤ 0.

    Usage Example:
        >>> chunk_string('abcdefgh', 3)
        ['abc', 'def', 'gh']

    Complexity: O(n)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string.")
    if not isinstance(size, int):
        raise TypeError("size must be an integer.")
    if size <= 0:
        raise ValueError("size must be positive.")
    return [text[i:i + size] for i in range(0, len(text), size)]


def squeeze(text: str, char: str) -> str:
    """Reduce consecutive runs of *char* to a single occurrence.

    Args:
        text: Source string.
        char: Single character to squeeze.

    Returns:
        Squeezed string.

    Raises:
        TypeError: If types are incorrect.
        ValueError: If char is not a single character.

    Usage Example:
        >>> squeeze('aaabbbccc', 'b')
        'aaabccc'

    Complexity: O(n)
    """
    if not isinstance(text, str) or not isinstance(char, str):
        raise TypeError("Both arguments must be strings.")
    if len(char) != 1:
        raise ValueError("char must be a single character.")
    result = []
    prev = None
    for ch in text:
        if ch == char and prev == char:
            continue
        result.append(ch)
        prev = ch
    return "".join(result)


def string_xor(a: str, b: str) -> str:
    """XOR two equal-length strings character by character.

    Returns a string of XOR'd character ordinals as two-digit hex codes.

    Args:
        a: First string.
        b: Second string (same length as *a*).

    Returns:
        Hex-encoded XOR result.

    Raises:
        TypeError: If arguments are not strings.
        ValueError: If lengths differ.

    Usage Example:
        >>> string_xor('abc', 'ABC')
        '202020'

    Complexity: O(n)
    """
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both arguments must be strings.")
    if len(a) != len(b):
        raise ValueError("Strings must be the same length.")
    return "".join(f"{ord(x) ^ ord(y):02x}" for x, y in zip(a, b))
