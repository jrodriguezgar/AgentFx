import collections
from typing import Optional, Dict, List, Iterable
import re
import unicodedata
import difflib
import random
import string


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
    """
    if not isinstance(character, str):
        raise TypeError("La entrada debe ser una cadena de texto (str).")
    if not character:  # Comprueba si la cadena está vacía
        raise ValueError("La cadena de entrada no puede estar vacía.")

    # ord() devuelve el código Unicode de un carácter
    return ord(character[0])


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
        # char_from_ascii() convierte un entero a un carácter Unicode
        return char_from_ascii(integer_code)
    except ValueError as e:
        # Captura errores si el código no es un punto de código Unicode válido
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
    sep_pattern = '|'.join(escaped_separators)

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
    """
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


def split_by_substrings(p_iparse: str, p_separators: list[str]) -> list[str]:
    """
    Splits a string by a list of substrings (separators),
    with each resulting section starting with the separator that preceded it.

    Args:
        p_iparse: The input string to be split.
        p_separators: A list of strings to use as separators.

    Returns:
        A list of strings, where each string starts with a separator
        followed by the text until the next separator or the end of the input string.
    """
    # 1. Escape special regular expression characters in separators.
    #    This is crucial for robustness if separators contain characters like '.', '?', '*', '+', etc.
    escaped_separators = [re.escape(s) for s in p_separators]

    # 2. Create a union regular expression pattern for all separators.
    #    Example: if escaped_separators is ['\,', '\?', '\!'], sep_pattern becomes '\,|\?|\!'
    sep_pattern = '|'.join(escaped_separators)

    # 3. Construct the full regular expression for finding desired segments.
    #    - (sep_pattern): This is the first capturing group. It matches and captures
    #      any of the defined separators.
    #    - (.*?): This is the second capturing group. It non-greedily matches any
    #      character (except newline) zero or more times. The non-greedy aspect (.*?)
    #      is important to ensure it stops at the earliest possible point.
    #    - (?={sep_pattern}|$): This is a positive lookahead assertion. It means that
    #      the match for the second capturing group (.*?) must be immediately followed
    #      by either another separator (sep_pattern) or the end of the string ($).
    #      This ensures that the text captured in the second group is exactly
    #      the content between the current separator and the next one (or end of string).
    full_pattern = f"({sep_pattern})(.*?)(?={sep_pattern}|$)"

    # 4. Use re.findall to find all non-overlapping matches of the full_pattern.
    #    re.findall returns a list of tuples, where each tuple contains the strings
    #    captured by the groups in the pattern. In our case, each tuple will be
    #    (matched_separator, text_after_separator).
    found_matches = re.findall(full_pattern, p_iparse)

    # 5. Combine the captured separator with the text that follows it.
    #    Each combined section is then stripped of leading/trailing whitespace
    #    to match the original function's behavior.
    result = [(sep + text).strip() for sep, text in found_matches]

    return result


def split_limited(p_iparse, p_limit):
    #limit_split("esto es una prueba de split de un programa python", 3)
    #Salida: ['esto', 'es', 'una', 'prueba de split de un programa python']  
    oparse = p_iparse.split()
    if len(oparse) <= p_limit:
        return oparse
    else:
        return oparse[:p_limit] + [" ".join(oparse[p_limit:])]


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

    Example of use:
        sample_text = "Hello 123 World! This is a test. My email is test@example.com."
        alphanumeric_matches = get_in_text_by_pattern(sample_text, 'alphanumeric_strings')
        print(f"Alphanumeric matches: {alphanumeric_matches}") # Expected: ['Hello 123', 'World']

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

'''# Ejemplo 1: Básico, solo letras y números, sin acentos
texto1 = "¡Hola, mundo! Esto es una prueba con números 123 y símbolos: @#$€."
print(f"Original: '{texto1}'")
print(f"Limpio (por defecto): '{erase_specialchar(texto1)}'")
# Salida: HOLA MUNDO ESTO ES UNA PRUEBA CON NUMEROS 123 Y SIMBOLOS

print("-" * 30)

# Ejemplo 2: Permitir guiones bajos
texto2 = "Nombre_Usuario.123@email.com"
print(f"Original: '{texto2}'")
print(f"Limpio (permitiendo guion bajo): '{erase_specialchar(texto2, allow_underscores=True)}'")
# Salida: NOMBRE_USUARIO123EMAILCOM

print("-" * 30)

# Ejemplo 3: Permitir caracteres adicionales (por ejemplo, puntos y guiones)
texto3 = "Este es un código-1.2.3 o (referencia/ABC)"
print(f"Original: '{texto3}'")
print(f"Limpio (permitiendo puntos y guiones): '{erase_specialchar(texto3, additional_allowed_chars='.-')}'")
# Salida: ESTE ES UN CODIGO-1.2.3 O REFERENCIAABC

print("-" * 30)

# Ejemplo 4: Sin espacios
texto4 = "¿Qué tal estás hoy?"
print(f"Original: '{texto4}'")
print(f"Limpio (sin espacios): '{erase_specialchar(texto4, allow_spaces=False)}'")
# Salida: QUETAL ESTAS HOY

print("-" * 30)

# Ejemplo 5: Texto con acentos y Ñ/Ç
texto5 = "Camión y autobús. Mañana iré al pueblo. Corrupción y Barça."
print(f"Original: '{texto5}'")
print(f"Limpio: '{erase_specialchar(texto5)}'")
# Salida: CAMION Y AUTOBUS. MANANA IRE AL PUEBLO. CORRUPCION Y BARCA. (Si flat_vowels maneja la ñ)

print("-" * 30)

# Ejemplo 6: Entrada None o no string
texto6 = None
print(f"Original: '{texto6}'")
print(f"Limpio: '{erase_specialchar(texto6)}'") # Ojo: esto devolverá 'NONE' si se convierte a str
'''

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

