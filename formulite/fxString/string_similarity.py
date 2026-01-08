"""String Similarity and Comparison Functions.

This module provides advanced algorithms for measuring similarity between
strings using various metrics. It includes both exact and fuzzy matching
techniques, phonetic algorithms, and edit distance calculations.

Key Features:
- Multiple similarity algorithms (Levenshtein, Jaro-Winkler, Jaccard, etc.)
- Phonetic matching (Metaphone, MRA)
- Edit distance calculations
- Word and character comparison
- Longest common subsequence
- Configurable similarity thresholds
- Batch comparison utilities

"""

import sys
import importlib
import difflib
from collections import deque
from typing import Union, List, Dict, Any, Tuple, Optional, Literal


_lazy_loaded_modules = {}

# Type alias para los algoritmos disponibles
AlgorithmType = Literal[
    'metaphone', 'levenshtein', 'hamming', 'ratcliff_obershelp',
    'sorensen_dice', 'mra', 'needleman_wunsch', 'jaro_winkler',
    'jaccard', 'lcs'
]

def _lazy_import(module_name: str, package_name: str = None):
    """
    Intenta importar un módulo de forma perezosa. Si el módulo no está
    disponible, imprime un mensaje sugiriendo la instalación con pip.

    Args:
        module_name (str): El nombre del módulo a importar (ej. 'metaphone').
        package_name (str): El nombre del paquete para la instalación de pip
                            si es diferente al module_name (ej. 'python-Levenshtein').
                            Si es None, se usa module_name.

    Returns:
        module: El módulo importado.

    Raises:
        ImportError: Si el módulo no se puede importar después de la sugerencia.
    """
    if module_name in _lazy_loaded_modules:
        return _lazy_loaded_modules[module_name]

    try:
        module = importlib.import_module(module_name)
        _lazy_loaded_modules[module_name] = module
        return module
    except ImportError:
        install_name = package_name if package_name else module_name
        print(f"Error: La librería '{module_name}' no está instalada.")
        print(f"Por favor, instálala usando: pip install {install_name}")
        # En un entorno real, podrías intentar instalarla aquí,
        # pero en este entorno restringido, solo podemos sugerirlo.
        import subprocess
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", install_name])
            module = importlib.import_module(module_name)
            _lazy_loaded_modules[module_name] = module
            return module
        except Exception as e:
            print(f"No se pudo instalar '{install_name}' automáticamente: {e}")
            #raise
        raise # Re-lanza el error para que el programa sepa que la dependencia no está disponible


def calculate_similarity(
    word1: str,
    word2: str,
    algorithm: AlgorithmType = 'levenshtein',
    **kwargs
) -> Union[bool, float, Dict[str, Any], Tuple[bool, Dict[str, Any]]]:
    """
    Función wrapper unificada para calcular similitud entre dos palabras/frases
    usando el algoritmo especificado.

    Esta función simplifica el uso del módulo permitiendo seleccionar el algoritmo
    mediante un parámetro string, sin necesidad de instanciar WordSimilarity
    ni llamar métodos específicos.

    Args:
        word1 (str): La primera palabra o frase a comparar.
        word2 (str): La segunda palabra o frase a comparar.
        algorithm (AlgorithmType): El algoritmo a utilizar. Opciones disponibles:
            - 'metaphone': Similitud fonética (retorna bool)
            - 'levenshtein': Distancia de edición (retorna float 0.0-1.0)
            - 'hamming': Distancia para cadenas de igual longitud (retorna float)
            - 'ratcliff_obershelp': Subsecuencias comunes (retorna Dict)
            - 'sorensen_dice': Similitud de tokens (retorna Dict)
            - 'mra': Match Rating Approach fonético (retorna Dict)
            - 'needleman_wunsch': Alineación de secuencias (retorna Dict)
            - 'jaro_winkler': Similitud con peso en prefijo (retorna Dict)
            - 'jaccard': Índice de similitud de conjuntos (retorna Dict)
            - 'lcs': Longest Common Subsequence (retorna Dict)
            - 'effective_same': Determina si son efectivamente iguales (retorna Tuple[bool, Dict])
            - 'all': Ejecuta todos los algoritmos (retorna Dict completo)
        **kwargs: Argumentos adicionales según el algoritmo:
            - Para 'needleman_wunsch': nw_gap_cost (int, default=1)
            - Para 'effective_same': levenshtein_threshold (float, default=0.85),
                                    jaro_winkler_threshold (float, default=0.9),
                                    metaphone_required (bool, default=True)

    Returns:
        Union[bool, float, Dict, Tuple]: El resultado depende del algoritmo:
            - bool: Para 'metaphone'
            - float: Para 'levenshtein', 'hamming'
            - Dict: Para algoritmos que retornan métricas múltiples
            - Tuple[bool, Dict]: Para 'effective_same'

    Raises:
        ValueError: Si el algoritmo especificado no es válido.
        TypeError: Si los argumentos de entrada no son cadenas.

    Ejemplos:
        >>> # Uso básico con Levenshtein (por defecto)
        >>> resultado = calculate_similarity("casa", "caza")
        >>> print(f"Similitud: {resultado:.2%}")
        Similitud: 75.00%

        >>> # Similitud fonética
        >>> resultado = calculate_similarity("conocimiento", "conosimiento", algorithm='metaphone')
        >>> print(f"¿Suenan igual? {resultado}")
        ¿Suenan igual? True

        >>> # Jaro-Winkler con métricas detalladas
        >>> resultado = calculate_similarity("martha", "marhta", algorithm='jaro_winkler')
        >>> print(f"Score: {resultado['score']:.4f}")
        Score: 0.9611

        >>> # Determinar equivalencia efectiva
        >>> resultado, metricas = calculate_similarity(
        ...     "aplicacion", "aplikacion",
        ...     algorithm='effective_same'
        ... )
        >>> print(f"¿Son la misma? {resultado}")
        ¿Son la misma? True

        >>> # Ejecutar todos los algoritmos
        >>> resultados = calculate_similarity("python", "pyton", algorithm='all')
        >>> print(f"Levenshtein: {resultados['levenshtein_ratio']:.2%}")
        >>> print(f"Metaphone: {resultados['metaphone_match']}")
        Levenshtein: 83.33%
        Metaphone: True

        >>> # Needleman-Wunsch con gap cost personalizado
        >>> resultado = calculate_similarity(
        ...     "GATTACA", "GTAC",
        ...     algorithm='needleman_wunsch',
        ...     nw_gap_cost=2
        ... )
        >>> print(f"Score: {resultado['score']:.4f}")
        Score: 0.4286

        >>> # Effective same con umbrales personalizados
        >>> resultado, metricas = calculate_similarity(
        ...     "color", "colour",
        ...     algorithm='effective_same',
        ...     levenshtein_threshold=0.75,
        ...     jaro_winkler_threshold=0.85,
        ...     metaphone_required=False
        ... )
        >>> print(f"¿Son la misma? {resultado}")
        ¿Son la misma? True

    Guía de Implementación:
        1. **Selección Simple de Algoritmo:**
           Cambia el parámetro `algorithm` para probar diferentes métricas
           sin cambiar el código de llamada.

        2. **Comparación de Algoritmos:**
           Usa algorithm='all' para obtener todos los resultados y compararlos:
           ```python
           resultados = calculate_similarity(palabra1, palabra2, algorithm='all')
           for metrica, valor in resultados.items():
               print(f"{metrica}: {valor}")
           ```

        3. **Búsqueda Difusa Optimizada:**
           Para búsquedas rápidas en listas grandes, usa 'metaphone' como filtro
           inicial y luego 'levenshtein' para refinar:
           ```python
           # Filtro rápido
           if calculate_similarity(query, candidato, algorithm='metaphone'):
               # Refinamiento
               ratio = calculate_similarity(query, candidato, algorithm='levenshtein')
               if ratio > 0.8:
                   resultados_finales.append(candidato)
           ```

        4. **Manejo de Casos Específicos:**
           - Nombres de personas: usa 'jaro_winkler'
           - Frases o documentos: usa 'sorensen_dice' o 'jaccard'
           - Secuencias biológicas: usa 'needleman_wunsch'
           - Validación general: usa 'effective_same'

        5. **Performance:**
           Los algoritmos están ordenados por velocidad aproximada:
           metaphone > hamming > levenshtein > jaro_winkler > needleman_wunsch

    Cost:
        La complejidad depende del algoritmo seleccionado:
        - metaphone: $O(n)$
        - levenshtein: $O(m \times n)$
        - hamming: $O(n)$
        - jaro_winkler: $O(m \times n)$
        - needleman_wunsch: $O(m \times n)$
        - all: $O(k \times m \times n)$ donde k es el número de algoritmos
    """
    if not isinstance(word1, str) or not isinstance(word2, str):
        raise TypeError("Ambos argumentos deben ser cadenas de texto.")

    # Normalizar el nombre del algoritmo
    algorithm = algorithm.lower().strip()

    # Validar algoritmo
    valid_algorithms = [
        'metaphone', 'levenshtein', 'hamming', 'ratcliff_obershelp',
        'sorensen_dice', 'mra', 'needleman_wunsch', 'jaro_winkler',
        'jaccard', 'lcs', 'effective_same', 'all'
    ]

    if algorithm not in valid_algorithms:
        raise ValueError(
            f"Algoritmo '{algorithm}' no válido. "
            f"Opciones disponibles: {', '.join(valid_algorithms)}"
        )

    # Inicializar WordSimilarity con gap_cost si se especifica
    nw_gap_cost = kwargs.get('nw_gap_cost', 1)
    ws = WordSimilarity(nw_gap_cost=nw_gap_cost)

    # Ejecutar el algoritmo solicitado
    if algorithm == 'metaphone':
        return ws.metaphone_score(word1, word2)

    elif algorithm == 'levenshtein':
        return ws.string_levenshtein_score(word1, word2)

    elif algorithm == 'hamming':
        return ws.string_hamming_score(word1, word2)

    elif algorithm == 'ratcliff_obershelp':
        return ws.ratcliff_obershelp_score(word1, word2)

    elif algorithm == 'sorensen_dice':
        return ws.sorensen_dice_score(word1, word2)

    elif algorithm == 'mra':
        return ws.string_mra_score(word1, word2)

    elif algorithm == 'needleman_wunsch':
        return ws.needleman_wunsch_score(word1, word2)

    elif algorithm == 'jaro_winkler':
        return ws.jaro_winkler_score(word1, word2)

    elif algorithm == 'jaccard':
        return ws.string_jaccard_score(word1, word2)

    elif algorithm == 'lcs':
        return ws.string_lcs_score(word1, word2)

    elif algorithm == 'effective_same':
        levenshtein_threshold = kwargs.get('levenshtein_threshold', 0.85)
        jaro_winkler_threshold = kwargs.get('jaro_winkler_threshold', 0.9)
        metaphone_required = kwargs.get('metaphone_required', True)
        return are_words_equivalent(word1, word2, levenshtein_threshold, jaro_winkler_threshold, metaphone_required)

    elif algorithm == 'all':
        return ws.compare(word1, word2)


class WordSimilarity:
    """
    Clase para calcular similitudes entre palabras o frases usando una variedad
    de algoritmos de distancia y similitud de cadenas.

    Ofrece métodos para:
      - Similitud fonética (Metaphone).
      - Similitud de edición (Levenshtein, Hamming, Needleman-Wunsch).
      - Similitud basada en subsecuencias y patrones (Ratcliff-Obershelp, LCS).
      - Similitud basada en tokens (Sørensen-Dice, Jaccard).
      - Similitud fonética avanzada (Match Rating Approach - MRA).
      - Similitud de prefijo (Jaro-Winkler).

    Atributos:
        nw_gap_cost (int): Costo de 'gap' para el algoritmo de Needleman-Wunsch.
                           Por defecto es 1.

    Ejemplo de Uso General:
        >>> ws = WordSimilarity()
        >>> word1 = "aplicacion"
        >>> word2 = "aplikacion"
        >>> results = ws.compare(word1, word2)
        >>> print(results)
        # Salida esperada (parcial):
        # {
        # 'metaphone_match': True,
        # 'levenshtein_ratio': 0.9,
        # 'hamming_ratio': None, # Será None si las longitudes son diferentes
        # 'ratcliff_obershelp': {'distance': ..., 'similarity': ..., 'normalized_similarity': ..., 'score': ...},
        # ...
        # }

    Guía de Implementación:
        1. Inicialización:
            Crea una instancia de WordSimilarity. Puedes especificar el costo
            de gap para Needleman-Wunsch si lo deseas.
            >>> ws = WordSimilarity()
            >>> ws_custom_nw = WordSimilarity(nw_gap_cost=2)

        2. Uso de Métodos Específicos:
            Cada método estático puede ser llamado directamente desde la clase
            o desde una instancia.
            >>> WordSimilarity.levenshtein_similarity("casa", "caza")
            >>> ws.metaphone_similarity("conocimiento", "conosimiento")

        3. Comparación Completa con `compare()`:
            El método `compare()` es la forma más sencilla de obtener un resumen
            de todas las métricas para dos cadenas.
            Devuelve un diccionario con los resultados de cada algoritmo.
            Es útil para una visión general o para seleccionar el mejor algoritmo
            para un caso de uso específico.

        4. Manejo de Errores:
            El método `hamming_similarity` lanzará un ValueError si las cadenas
            tienen longitudes diferentes. El método `compare` maneja esto
            internamente asignando `None` a `hamming_ratio` en ese caso.
            Otros métodos lanzarán TypeError si los inputs no son cadenas.

        5. Determinación de Equivalencia "Efectiva":
            Utiliza el método estático `are_words_equivalent`
            para aplicar un criterio combinado de similitud.
            >>> WordSimilarity.are_words_equivalent("aplicacion", "aplikacion")
            True
            >>> WordSimilarity.are_words_equivalent("cat", "dog")
            False
    """
    def __init__(self, nw_gap_cost: int = 1):
        """
        Inicializa la clase WordSimilarity.

        Args:
            nw_gap_cost (int): Costo por un 'gap' en el algoritmo de
                               Needleman-Wunsch. Por defecto es 1.
        """
        if not isinstance(nw_gap_cost, int) or nw_gap_cost < 0:
            raise ValueError("nw_gap_cost debe ser un entero no negativo.")
        td = _lazy_import('textdistance') # Importación perezosa
        td.needleman_wunsch.gap_cost = nw_gap_cost

    @staticmethod
    def metaphone_score(word1: str, word2: str) -> bool:
        """
        Compara la similitud fonética de dos palabras usando Double Metaphone.

        Este algoritmo genera una o dos claves fonéticas para cada palabra
        y devuelve True si alguna de las claves de la primera palabra
        coincide con alguna clave de la segunda palabra. Es útil para
        detectar palabras que suenan similar.

        Args:
            word1 (str): La primera palabra a comparar.
            word2 (str): La segunda palabra a comparar.

        Returns:
            bool: True si las palabras tienen similitud fonética según Metaphone,
                  False en caso contrario.

        Ejemplos:
            >>> WordSimilarity.metaphone_score("conocimiento", "conosimiento")
            True
            >>> WordSimilarity.metaphone_score("hello", "hola")
            False
            >>> WordSimilarity.metaphone_score("smith", "smyth")
            True
        """
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        
        # Validación tautológica
        if word1 == word2:
            return True
        
        metaphone = _lazy_import('metaphone') # Importación perezosa
        meta1 = metaphone.doublemetaphone(word1.lower()) # Convertir a minúsculas para consistencia
        meta2 = metaphone.doublemetaphone(word2.lower()) # Convertir a minúsculas para consistencia
        return any(m in meta2 for m in meta1 if m)

    @staticmethod
    def levenshtein_score(word1: str, word2: str) -> float:
        """
        Calcula el ratio de similitud de Levenshtein entre dos cadenas.

        La distancia de Levenshtein es el número mínimo de ediciones
        (inserciones, eliminaciones o sustituciones de un solo carácter)
        necesarias para transformar una cadena en la otra. El ratio
        es 1 - (distancia / max_longitud). Un valor de 1.0 indica
        cadenas idénticas, 0.0 indica que no hay similitud.

        Args:
            word1 (str): La primera cadena a comparar.
            word2 (str): La segunda cadena a comparar.

        Returns:
            float: Un valor flotante entre 0.0 y 1.0 que representa la
                   similitud de Levenshtein.

        Ejemplos:
            >>> WordSimilarity.levenshtein_score("kitten", "sitting")
            0.5714285714285714
            >>> WordSimilarity.levenshtein_score("casa", "caza")
            0.75
            >>> WordSimilarity.levenshtein_score("apple", "apple")
            1.0
            >>> WordSimilarity.levenshtein_score("", "abc")
            0.0
        """
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        
        # Validación tautológica
        if word1 == word2:
            return 1.0
        
        Levenshtein = _lazy_import('Levenshtein', 'python-Levenshtein') # Importación perezosa
        return Levenshtein.ratio(word1, word2)

    @staticmethod
    def hamming_score(word1: str, word2: str) -> float:
        """
        Calcula el ratio de similitud de Hamming entre dos cadenas.

        La distancia de Hamming solo es aplicable a cadenas de la misma longitud.
        Cuenta el número de posiciones en las que los símbolos correspondientes
        son diferentes. El ratio es 1 - (distancia / longitud).

        Args:
            word1 (str): La primera cadena a comparar.
            word2 (str): La segunda cadena a comparar.

        Returns:
            float: Un valor flotante entre 0.0 y 1.0 que representa la
                   similitud de Hamming.

        Raises:
            ValueError: Si las cadenas de entrada tienen longitudes diferentes.
            TypeError: Si los argumentos no son cadenas.

        Ejemplos:
            >>> WordSimilarity.hamming_score("karolin", "kathrin")
            0.5714285714285714
            >>> WordSimilarity.hamming_score("rojo", "rosa")
            0.5
            >>> WordSimilarity.hamming_score("abc", "abc")
            1.0
            >>> WordSimilarity.hamming_score("abc", "abd")
            0.6666666666666667
        """
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        
        # Validación tautológica
        if word1 == word2:
            return 1.0
        
        if len(word1) != len(word2):
            raise ValueError("Para Hamming, ambas palabras deben tener la misma longitud.")
        if not word1: # Si ambas son cadenas vacías, la distancia es 0, similitud 1.0
            return 1.0
        jellyfish = _lazy_import('jellyfish') # Importación perezosa
        dist = jellyfish.hamming_distance(word1, word2)
        return 1 - dist / len(word1)

    @staticmethod
    def ratcliff_obershelp_score(a: str, b: str) -> Dict[str, float]:
        """
        Calcula las métricas de similitud usando el algoritmo Ratcliff-Obershelp.

        Este algoritmo es efectivo para comparar cadenas que pueden contener
        subcadenas comunes, incluso si no están en el mismo orden exacto.
        Se basa en la Longest Common Subsequence (LCS).

        Args:
            a (str): La primera cadena a comparar.
            b (str): La segunda cadena a comparar.

        Returns:
            Dict[str, float]: Un diccionario con 'distance', 'similarity',
                              'normalized_similarity' y 'score' (similitud normalizada * 100).

        Ejemplos:
            >>> ws = WordSimilarity()
            >>> ws.ratcliff_obershelp_score("apple", "aple")
            {'distance': 0.1, 'similarity': 0.9, 'normalized_similarity': 0.9, 'score': 90.0}
            >>> ws.ratcliff_obershelp_score("information", "inform")
            {'distance': 0.36363636363636365, 'similarity': 0.6363636363636364, 'normalized_similarity': 0.6363636363636364, 'score': 63.63636363636363}
            >>> ws.ratcliff_obershelp_score("hello world", "world hello")
            {'distance': 0.0, 'similarity': 1.0, 'normalized_similarity': 1.0, 'score': 100.0}
        """
        if not isinstance(a, str) or not isinstance(b, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        td = _lazy_import('textdistance') # Importación perezosa
        d = td.ratcliff_obershelp
        return {
            'distance': d.distance(a, b),
            'similarity': d.similarity(a, b),
            'normalized_similarity': d.normalized_similarity(a, b),
            'score': d.normalized_similarity(a, b)  # Standardized to 0-1 range
        }

    @staticmethod
    def sorensen_dice_score(a: str, b: str) -> Dict[str, float]:
        """
        Calcula las métricas de similitud usando el coeficiente de Sørensen-Dice
        basado en tokens (palabras).

        Este coeficiente mide la similitud entre dos conjuntos. Aquí, las
        cadenas se dividen en palabras (tokens) por espacios en blanco,
        y la similitud se calcula en base a la superposición de estos tokens.
        Es útil para comparar la similitud de contenido de frases cortas
        o documentos pequeños.

        Args:
            a (str): La primera cadena a comparar (se dividirá en tokens).
            b (str): La segunda cadena a comparar (se dividirá en tokens).

        Returns:
            Dict[str, float]: Un diccionario con 'distance', 'similarity',
                              'normalized_similarity' y 'score' (similitud normalizada * 100).

        Ejemplos:
            >>> ws = WordSimilarity()
            >>> ws.sorensen_dice_score("this is a test", "this is test")
            {'distance': 0.2, 'similarity': 0.8, 'normalized_similarity': 0.8, 'score': 80.0}
            >>> ws.sorensen_dice_score("python programming", "java programming")
            {'distance': 0.33333333333333337, 'similarity': 0.6666666666666666, 'normalized_similarity': 0.6666666666666666, 'score': 66.66666666666666}
            >>> ws.sorensen_dice_score("apple orange", "banana kiwi")
            {'distance': 1.0, 'similarity': 0.0, 'normalized_similarity': 0.0, 'score': 0.0}
        """
        if not isinstance(a, str) or not isinstance(b, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        tokens_a, tokens_b = a.lower().split(), b.lower().split() # Convertir a minúsculas y tokenizar
        td = _lazy_import('textdistance') # Importación perezosa
        d = td.sorensen
        return {
            'distance': d.distance(tokens_a, tokens_b),
            'similarity': d.similarity(tokens_a, tokens_b),
            'normalized_similarity': d.normalized_similarity(tokens_a, tokens_b),
            'score': d.normalized_similarity(tokens_a, tokens_b)  # Standardized to 0-1 range
        }

    @staticmethod
    def mra_score(a: str, b: str) -> Dict[str, float]:
        """
        Calcula las métricas de similitud usando el Match Rating Approach (MRA).

        MRA es un algoritmo fonético diseñado para comparar nombres.
        Genera un "código de clasificación" para cada cadena y luego
        calcula una distancia basada en la comparación de estos códigos.
        Es similar a Metaphone pero con un enfoque diferente.

        Args:
            a (str): La primera cadena a comparar.
            b (str): La segunda cadena a comparar.

        Returns:
            Dict[str, float]: Un diccionario con 'distance', 'similarity',
                              'normalized_similarity' y 'score' (similitud normalizada * 100).

        Ejemplos:
            >>> ws = WordSimilarity()
            >>> ws.mra_score("Schmitt", "Schmidt")
            {'distance': 0.16666666666666666, 'similarity': 0.8333333333333334, 'normalized_similarity': 0.8333333333333334, 'score': 83.33333333333334}
            >>> ws.mra_score("John", "Jon")
            {'distance': 0.0, 'similarity': 1.0, 'normalized_similarity': 1.0, 'score': 100.0}
            >>> ws.mra_score("Michael", "Mike")
            {'distance': 0.0, 'similarity': 1.0, 'normalized_similarity': 1.0, 'score': 100.0}
        """
        if not isinstance(a, str) or not isinstance(b, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        td = _lazy_import('textdistance') # Importación perezosa
        d = td.mra
        return {
            'distance': d.distance(a, b),
            'similarity': d.similarity(a, b),
            'normalized_similarity': d.normalized_similarity(a, b),
            'score': d.normalized_similarity(a, b)  # Standardized to 0-1 range
        }

    @staticmethod
    def needleman_wunsch_score(a: str, b: str) -> Dict[str, float]:
        """
        Calcula las métricas de similitud usando el algoritmo de Needleman-Wunsch.

        Este algoritmo es comúnmente usado en bioinformática para alinear
        secuencias de ADN o proteínas. Encuentra la alineación global más óptima
        entre dos secuencias, considerando costos de 'match', 'mismatch' y 'gap'.
        El costo de 'gap' se puede configurar al inicializar la clase
        WordSimilarity.

        Args:
            a (str): La primera cadena a comparar.
            b (str): La segunda cadena a comparar.

        Returns:
            Dict[str, float]: Un diccionario con 'distance', 'similarity',
                              'normalized_similarity' y 'score' (similitud normalizada * 100).

        Ejemplos:
            >>> ws = WordSimilarity()
            >>> ws.needleman_wunsch_score("GATTACA", "GTAC")
            {'distance': 3.0, 'similarity': -3.0, 'normalized_similarity': -0.42857142857142855, 'score': -42.857142857142855}
            >>> ws.needleman_wunsch_score("casa", "caza")
            {'distance': 1.0, 'similarity': 3.0, 'normalized_similarity': 0.75, 'score': 75.0}
            >>> ws.needleman_wunsch_score("apple", "aple")
            {'distance': 1.0, 'similarity': 4.0, 'normalized_similarity': 0.8, 'score': 80.0}
        """
        if not isinstance(a, str) or not isinstance(b, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        td = _lazy_import('textdistance') # Importación perezosa
        d = td.needleman_wunsch
        return {
            'distance': d.distance(a, b),
            'similarity': d.similarity(a, b),
            'normalized_similarity': d.normalized_similarity(a, b),
            'score': d.normalized_similarity(a, b)  # Standardized to 0-1 range
        }

    @staticmethod
    def jaro_winkler_score(a: str, b: str) -> Dict[str, float]:
        """
        Calcula las métricas de similitud usando el algoritmo Jaro-Winkler.

        Este algoritmo es una variante de Jaro que da más peso a las
        concordancias en el prefijo de las cadenas. Es muy efectivo para
        comparar nombres cortos o palabras con errores tipográficos al
        principio.

        Args:
            a (str): La primera cadena a comparar.
            b (str): La segunda cadena a comparar.

        Returns:
            Dict[str, float]: Un diccionario con 'distance', 'similarity',
                              'normalized_similarity' y 'score' (similitud normalizada * 100).

        Ejemplos:
            >>> ws = WordSimilarity()
            >>> ws.jaro_winkler_score("martha", "marhta")
            {'distance': 0.04444444444444443, 'similarity': 0.9555555555555556, 'normalized_similarity': 0.9611111111111111, 'score': 96.11111111111111}
            >>> ws.jaro_winkler_score("dixon", "dicksonx")
            {'distance': 0.22499999999999998, 'similarity': 0.775, 'normalized_similarity': 0.8133333333333333, 'score': 81.33333333333333}
            >>> ws.jaro_winkler_score("cat", "cow")
            {'distance': 0.33333333333333337, 'similarity': 0.6666666666666666, 'normalized_similarity': 0.7777777777777778, 'score': 77.77777777777779}
        """
        if not isinstance(a, str) or not isinstance(b, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        td = _lazy_import('textdistance') # Importación perezosa
        d = td.jaro_winkler
        return {
            'distance': d.distance(a, b),
            'similarity': d.similarity(a, b),
            'normalized_similarity': d.normalized_similarity(a, b),
            'score': d.normalized_similarity(a, b)  # Standardized to 0-1 range
        }

    @staticmethod
    def jaccard_score(a: str, b: str) -> Dict[str, float]:
        """
        Calcula las métricas de similitud usando el índice de Jaccard
        basado en tokens (palabras).

        Similar a Sørensen-Dice, pero el índice de Jaccard es la
        cardinalidad de la intersección de los conjuntos dividida por la
        cardinalidad de su unión. Las cadenas se tokenizan por espacios
        en blanco. Es útil para medir la similitud de conjuntos de palabras.

        Args:
            a (str): La primera cadena a comparar (se dividirá en tokens).
            b (str): La segunda cadena a comparar (se dividirá en tokens).

        Returns:
            Dict[str, float]: Un diccionario con 'distance', 'similarity',
                              'normalized_similarity' y 'score' (similitud normalizada * 100).

        Ejemplos:
            >>> ws = WordSimilarity()
            >>> ws.jaccard_score("this is a test", "this is test")
            {'distance': 0.25, 'similarity': 0.75, 'normalized_similarity': 0.75, 'score': 75.0}
            >>> ws.jaccard_score("apple banana", "banana orange")
            {'distance': 0.6666666666666666, 'similarity': 0.33333333333333337, 'normalized_similarity': 0.33333333333333337, 'score': 33.333333333333336}
            >>> ws.jaccard_score("hello world", "hello world")
            {'distance': 0.0, 'similarity': 1.0, 'normalized_similarity': 1.0, 'score': 100.0}
        """
        if not isinstance(a, str) or not isinstance(b, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        tokens_a, tokens_b = a.lower().split(), b.lower().split() # Convertir a minúsculas y tokenizar
        td = _lazy_import('textdistance') # Importación perezosa
        d = td.jaccard
        return {
            'distance': d.distance(tokens_a, tokens_b),
            'similarity': d.similarity(tokens_a, tokens_b),
            'normalized_similarity': d.normalized_similarity(tokens_a, tokens_b),
            'score': d.normalized_similarity(tokens_a, tokens_b)  # Standardized to 0-1 range
        }

    @staticmethod
    def lcs_score(a: str, b: str) -> Dict[str, Union[str, float, int]]:
        """
        Calcula la Longest Common Subsequence (LCS) y su porcentaje de similitud.

        La LCS es la secuencia más larga que es una subsecuencia de ambas
        cadenas. No requiere que los caracteres sean contiguos.
        El 'score' es un porcentaje basado en la longitud de la LCS
        dividida por la media de las longitudes de las dos cadenas,
        multiplicado por 200.0 para escalarlo de 0 a 100%.

        Args:
            a (str): La primera cadena a comparar.
            b (str): La segunda cadena a comparar.

        Returns:
            Dict[str, Union[str, float, int]]: Un diccionario con:
                                                - 'sequence': La secuencia común más larga.
                                                - 'length': La longitud de la secuencia común.
                                                - 'score': Porcentaje de similitud basado en LCS.

        Ejemplos:
            >>> ws = WordSimilarity()
            >>> ws.lcs_score("ABCBDAB", "BDCABA")
            {'sequence': 'BCBA', 'length': 4, 'score': 66.66666666666666}
            >>> ws.lcs_score("AGGTAB", "GXTXAYB")
            {'sequence': 'GTAB', 'length': 4, 'score': 66.66666666666666}
            >>> ws.lcs_score("coche", "correr")
            {'sequence': 'coe', 'length': 3, 'score': 54.54545454545454}
            >>> ws.lcs_score("python", "java")
            {'sequence': '', 'length': 0, 'score': 0.0}
        """
        if not isinstance(a, str) or not isinstance(b, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")

        n1, n2 = len(a), len(b)
        
        # Casos base para cadenas vacías
        if n1 == 0 or n2 == 0:
            return {'sequence': '', 'length': 0, 'score': 0.0}

        # Matriz para DP: dp[i][j] es la longitud de LCS de a[:i] y b[:j]
        # Y también guardamos la secuencia
        dp = [[(0, '') for _ in range(n2 + 1)] for _ in range(n1 + 1)]

        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if a[i - 1] == b[j - 1]:
                    # Si los caracteres coinciden, extendemos la LCS de la subproblema anterior
                    dp[i][j] = (dp[i - 1][j - 1][0] + 1, dp[i - 1][j - 1][1] + a[i - 1])
                else:
                    # Si no coinciden, tomamos la LCS máxima de ignorar un carácter de 'a' o de 'b'
                    if dp[i - 1][j][0] >= dp[i][j - 1][0]:
                        dp[i][j] = dp[i - 1][j]
                    else:
                        dp[i][j] = dp[i][j - 1]

        length, seq = dp[n1][n2]
        similarity = length / max(n1, n2) if max(n1, n2) > 0 else 1.0
        return {'sequence': seq, 'length': length, 'similarity': similarity}

    def compare(self, word1: str, word2: str) -> Dict[str, Any]:
        """
        Devuelve un diccionario con los resultados de todos los algoritmos
        de similitud implementados en la clase para las dos palabras dadas.

        Args:
            word1 (str): La primera palabra o frase a comparar.
            word2 (str): La segunda palabra o frase a comparar.

        Returns:
            Dict[str, Any]: Un diccionario donde las claves son los nombres
                            de los algoritmos y los valores son sus respectivos
                            resultados. Incluye:
                            - metaphone_match (bool)
                            - levenshtein_ratio (float)
                            - hamming_ratio (float o None)
                            - ratcliff_obershelp (Dict)
                            - sorensen_dice (Dict)
                            - mra (Dict)
                            - needleman_wunsch (Dict)
                            - jaro_winkler (Dict)
                            - jaccard (Dict)
                            - lcs (Dict)

        Raises:
            TypeError: Si alguno de los argumentos de entrada no es una cadena.

        Ejemplos:
            >>> ws = WordSimilarity()
            >>> results = ws.compare("franco", "franko")
            >>> # print(results) mostrará todos los resultados
            >>> results['metaphone_match']
            True
            >>> results['levenshtein_ratio']
            0.8333333333333334
            >>> results['sorensen_dice']['score']
            0.0 # porque "franco" y "franko" son una sola palabra, no múltiples tokens
            >>> results['lcs']['sequence']
            'franco'
            >>>
            >>> results_phrases = ws.compare("the quick brown fox", "a quick red fox")
            >>> # print(results_phrases)
            >>> results_phrases['sorensen_dice']['score'] # Mayor para frases con palabras comunes
            66.66666666666666
            >>> results_phrases['jaccard']['score']
            50.0
            >>> results_phrases['lcs']['sequence']
            'quick rox' # Note que LCS no requiere contigüidad.

        """
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")

        results: Dict[str, Any] = {
            'metaphone_match': self.metaphone_score(word1, word2),
            'levenshtein_ratio': self.levenshtein_score(word1, word2),
            'hamming_ratio': None # Inicializar a None, se actualizará si es posible
        }
        try:
            results['hamming_ratio'] = self.hamming_score(word1, word2)
        except ValueError:
            # Captura el error de longitud diferente para Hamming y lo ignora,
            # dejando 'hamming_ratio' como None.
            pass
        except TypeError:
            # Aunque ya se comprueba al principio, es una doble seguridad.
            # En un entorno de producción, es preferible que la función
            # individual lance el error y `compare` lo maneje si quiere
            # ser más resiliente. Aquí, la validación inicial ya lo cubre.
            pass

        # Métricas que devuelven diccionarios de textdistance
        # Asegurarse de que se llaman con las cadenas originales
        results.update({
            'ratcliff_obershelp': self.ratcliff_obershelp_score(word1, word2),
            'sorensen_dice': self.sorensen_dice_score(word1, word2),
            'mra': self.mra_score(word1, word2),
            'needleman_wunsch': self.needleman_wunsch_score(word1, word2),
            'jaro_winkler': self.jaro_winkler_score(word1, word2),
            'jaccard': self.jaccard_score(word1, word2),
            'lcs': self.lcs_score(word1, word2)
        })
        
        return results

    @staticmethod
    def are_words_equivalent(
        word1: str,
        word2: str,
        levenshtein_threshold: float = 0.85,
        jaro_winkler_threshold: float = 0.9,
        metaphone_required: bool = True
    ) -> Tuple[bool, Dict[str, Any]]:
        """
        Propuesta de mejores prácticas para determinar si dos palabras son
        "efectivamente la misma" basándose en una combinación de algoritmos
        de similitud.

        Este método combina la similitud fonética (Metaphone) con métricas
        de distancia de edición (Levenshtein y Jaro-Winkler) para ofrecer
        un criterio más robusto que una sola métrica.
        Puede ser configurado mediante umbrales.

        Args:
            word1 (str): La primera palabra a comparar.
            word2 (str): La segunda palabra a comparar.
            levenshtein_threshold (float): Umbral para la similitud de Levenshtein.
                                           Las palabras se consideran similares si el ratio
                                           de Levenshtein es igual o superior a este valor.
                                           (Valor por defecto: 0.85)
            jaro_winkler_threshold (float): Umbral para la similitud de Jaro-Winkler.
                                            Las palabras se consideran similares si el score
                                            de Jaro-Winkler es igual o superior a este valor.
                                            (Valor por defecto: 0.9)
            metaphone_required (bool): Si es True, las palabras deben tener
                                       similitud fonética según Metaphone para
                                       ser consideradas "la misma".
                                       (Valor por defecto: True)

        Returns:
            Tuple[bool, Dict[str, Any]]: Una tupla que contiene:
                - bool: True si las palabras son consideradas "efectivamente la misma", False en caso contrario.
                - Dict[str, Any]: Un diccionario con los resultados de las métricas
                                  utilizadas para la decisión.

        Raises:
            TypeError: Si alguno de los argumentos de entrada no es una cadena.

        Ejemplos de Uso:
            >>> # Caso 1: Palabras muy similares tipográficamente y fonéticamente
            >>> result, metrics = WordSimilarity.are_words_equivalent("conocimiento", "conosimiento")
            >>> result
            True
            >>> metrics['metaphone_match']
            True
            >>> metrics['levenshtein_ratio'] > 0.85
            True

            >>> # Caso 2: Palabras diferentes, no deberían coincidir
            >>> result, metrics = WordSimilarity.are_words_equivalent("casa", "perro")
            >>> result
            False
            >>> metrics['levenshtein_ratio'] < 0.85
            True

            >>> # Caso 3: Palabras con un pequeño error, pero fonéticamente iguales (metaphone_required=True)
            >>> result, metrics = WordSimilarity.are_words_equivalent("aplicacion", "aplikacion")
            >>> result
            True

            >>> # Caso 4: Similar tipográficamente pero fonéticamente diferente (si metaphone_required=True)
            >>> result, metrics = WordSimilarity.are_words_equivalent("cat", "cut")
            >>> result
            False
            >>> # Si metaphone_required fuera False, podría dar True dependiendo de los umbrales
            >>> result, metrics = WordSimilarity.are_words_equivalent("cat", "cut", metaphone_required=False)
            >>> result # Puede ser True si los umbrales son bajos y la similitud tipográfica es alta
            True

            >>> # Caso 5: Nombres propios con ligeras variaciones
            >>> result, metrics = WordSimilarity.are_words_equivalent("Smith", "Smyth")
            >>> result
            True

        Guía de Implementación:
            Este enfoque es ideal para escenarios donde necesitas manejar
            variaciones comunes en la escritura (errores tipográficos,
            diferencias de dialecto, romanizaciones alternativas) o
            identificar nombres o términos que suenan igual.

            1.  **Ajusta los umbrales:** Los valores `levenshtein_threshold` y
                `jaro_winkler_threshold` son críticos y deben ajustarse
                según la sensibilidad deseada para tu caso de uso.
                Valores más altos = más estricto.
            2.  **`metaphone_required`:** Si estás comparando términos donde
                la fonética es crucial (ej. nombres de personas, lugares con
                variaciones ortográficas), mantenlo en `True`. Si el enfoque
                es puramente tipográfico, puedes establecerlo en `False`.
            3.  **Evaluación Combinada:** La función devuelve True si *todas*
                las condiciones configuradas se cumplen. Esto asegura que la
                "igualdad efectiva" se basa en múltiples criterios.
            4.  **Resultados Detallados:** El segundo elemento de la tupla de
                retorno (`metrics`) te proporciona los valores de las métricas
                individuales, lo cual es útil para depuración o para entender
                por qué se tomó una decisión.
        """
        if not isinstance(word1, str) or not isinstance(word2, str):
            raise TypeError("Ambos argumentos deben ser cadenas de texto.")
        if not isinstance(levenshtein_threshold, (int, float)) or not (0.0 <= levenshtein_threshold <= 1.0):
            raise ValueError("levenshtein_threshold debe ser un flotante entre 0.0 y 1.0.")
        if not isinstance(jaro_winkler_threshold, (int, float)) or not (0.0 <= jaro_winkler_threshold <= 1.0):
            raise ValueError("jaro_winkler_threshold debe ser un flotante entre 0.0 y 1.0.")
        if not isinstance(metaphone_required, bool):
            raise TypeError("metaphone_required debe ser un booleano.")
        
        # Validación tautológica
        if word1 == word2:
            return True, {
                'exact_match': True,
                'metaphone_match': True,
                'levenshtein_ratio': 1.0,
                'jaro_winkler_similarity': 1.0
            }

        # Asegurarse de que las palabras estén en minúsculas para comparaciones consistentes
        # Esto es importante para Levenshtein y Jaro-Winkler si se quiere insensibilidad a mayúsculas
        # Metaphone ya maneja esto internamente.
        w1_lower = word1.lower()
        w2_lower = word2.lower()

        # Caso trivial: palabras idénticas (después de normalizar a minúsculas)
        if w1_lower == w2_lower:
            return True, {
                'exact_match': True,
                'metaphone_match': True,
                'levenshtein_ratio': 1.0,
                'jaro_winkler_similarity': 1.0
            }

        # Calcular las métricas relevantes
        metaphone_match = WordSimilarity.metaphone_score(w1_lower, w2_lower)
        lev_ratio = WordSimilarity.levenshtein_score(w1_lower, w2_lower)
        jaro_similarity = WordSimilarity.jaro_winkler_score(w1_lower, w2_lower)['normalized_similarity']

        results_metrics = {
            'exact_match': False,
            'metaphone_match': metaphone_match,
            'levenshtein_ratio': lev_ratio,
            'jaro_winkler_similarity': jaro_similarity
        }

        # Aplicar los criterios
        is_lev_similar = lev_ratio >= levenshtein_threshold
        is_jaro_similar = jaro_similarity >= jaro_winkler_threshold
        algorithm_difference = abs(jaro_winkler_threshold - levenshtein_threshold)

        if metaphone_required:
            final_decision = metaphone_match and is_lev_similar and is_jaro_similar and algorithm_difference < 0.05
        else:
            final_decision = is_lev_similar and is_jaro_similar and algorithm_difference < 0.05

        return final_decision, results_metrics


def has_same_words(string_one: str, string_two: str) -> bool:
    """
    Checks if two strings contain the same words, ignoring word order and case.

    This function tokenizes both input strings into words, converts them to
    lowercase, sorts the resulting word lists, and then compares them.
    This approach ensures that the order of words and their capitalization
    do not affect the comparison result.

    Args:
        string_one (str): The first string to compare.
        string_two (str): The second string to compare.

    Returns:
        bool: True if both strings contain the same words, False otherwise.

    Raises:
        TypeError: If either input is not a string.

    Example of use:
        >>> has_same_words("hello world", "world hello")
        True
        >>> has_same_words("python programming", "programming python")
        True
        >>> has_same_words("apple banana", "banana orange")
        False
        >>> has_same_words("HELLO world", "world hello")
        True
        >>> has_same_words("one two two", "two one two")
        True
        >>> has_same_words("a b c", "A B C")
        True

    Guía de Implementación:
        Esta función es útil cuando solo importa la presencia de las mismas
        palabras, no su orden ni su capitalización, y también considera
        la multiplicidad de las palabras.
        Simplemente pasa las dos cadenas y obtén un booleano.
        Ten en cuenta que `split()` por defecto divide por cualquier espacio
        en blanco y descarta cadenas vacías resultantes.
    """
    if not isinstance(string_one, str) or not isinstance(string_two, str):
        raise TypeError("Both inputs must be strings.")
    
    # Validación tautológica
    if string_one == string_two:
        return True

    # Convert strings to lowercase and split them into words.
    # We convert to lowercase so that case differences don't affect the comparison.
    # For example, "Hello" and "hello" should be considered the same word.
    list_one = string_one.lower().split()
    list_two = string_two.lower().split()

    # Sort the lists of words.
    # Sorting allows us to compare the contents of the strings regardless of
    # the original word order. If the sorted lists are identical, it means
    # the strings contain the same words. This also accounts for word counts.
    list_one.sort()
    list_two.sort()

    return list_one == list_two


def find_common_words(string_one: str, string_two: str) -> List[str]:
    """
    Identifies and returns the common unique words between two input strings.

    This function first tokenizes both strings into words, converts them to
    lowercase, and then uses sets to efficiently find the words that are
    present in both strings. The result is a list of unique common words.
    The order of words in the returned list is not guaranteed.

    Args:
        string_one (str): The first string for comparison.
        string_two (str): The second string for comparison.

    Returns:
        list[str]: A list of unique words found in both strings.

    Raises:
        TypeError: If either input is not a string.

    Example of use:
        >>> find_common_words("The quick brown fox", "A quick brown dog")
        ['quick', 'brown'] # El orden puede variar
        >>> find_common_words("Hello world", "WORLD hello")
        ['world', 'hello'] # El orden puede variar
        >>> find_common_words("apple banana orange", "grape kiwi pineapple")
        []
        >>> find_common_words("one two three four", "three four five six")
        ['three', 'four'] # El orden puede variar
        >>> find_common_words("common common word", "common common phrase")
        ['common']

    Guía de Implementación:
        Usa esta función cuando necesites extraer una lista de palabras
        que aparecen en *ambas* cadenas, sin importar el orden ni la frecuencia
        dentro de cada cadena.
        La función es insensible a mayúsculas/minúsculas.
    """
    if not isinstance(string_one, str) or not isinstance(string_two, str):
        raise TypeError("Both inputs must be strings.")
    
    # Validación tautológica
    if string_one == string_two:
        return string_one.lower().split()

    # Convert strings to lowercase and split into words.
    # Lowercasing ensures that case differences (e.g., "The" vs. "the")
    # don't prevent words from being identified as common.
    words_one = string_one.lower().split()
    words_two = string_two.lower().split()

    # Convert lists of words to sets.
    # Sets provide efficient ways to find common elements (intersections).
    # This also automatically handles duplicate words within a single string,
    # ensuring that each word is considered only once for the commonality check.
    set_one = set(words_one)
    set_two = set(words_two)

    # Find the intersection of the two sets.
    # The intersection operation returns a new set containing only the elements
    # that are present in both set_one and set_two.
    common_words_set = set_one.intersection(set_two)

    # Convert the set of common words back to a list for the return value.
    # While sets are great for the logic, lists are often more convenient
    # for ordered or repeatable output (though the order is not guaranteed).
    return list(common_words_set)


def has_same_characters(string_one: str, string_two: str) -> bool:
    """
    Checks if two strings contain exactly the same unique characters,
    regardless of their order or frequency.

    This function converts both input strings into sets of characters.
    Since sets only store unique elements, this effectively ignores
    duplicate characters and character order. The function then
    compares these two sets. If the sets are identical, it means both
    strings are composed of the exact same unique characters.

    Args:
        string_one (str): The first string to compare.
        string_two (str): The second string to compare.

    Returns:
        bool: True if both strings contain the exact same set of unique
              characters, False otherwise.

    Raises:
        TypeError: If either input is not a string.

    Example of use:
        >>> has_same_characters("listen", "silent")
        True
        >>> has_same_characters("aabbcc", "abc")
        True
        >>> has_same_characters("hello", "world")
        False
        >>> has_same_characters("apple", "aple")
        True
        >>> has_same_characters("aaabbbccc", "abc")
        True
        >>> has_same_characters("abc", "cba")
        True
        >>> has_same_characters("", "")
        True
        >>> has_same_characters("a", "")
        False

    Guía de Implementación:
        Utiliza esta función para determinar si dos cadenas son anagramas
        (en su conjunto de caracteres únicos) o si están compuestas
        exactamente por los mismos elementos atómicos (caracteres),
        sin importar cuántas veces se repita cada uno o en qué orden aparezcan.
        Es útil para limpiar datos o para comprobaciones de "tipo de contenido"
        a nivel de carácter.
    """
    if not isinstance(string_one, str) or not isinstance(string_two, str):
        raise TypeError("Both inputs must be strings.")
    
    # Validación tautológica
    if string_one == string_two:
        return True

    # Convert each string into a set of its characters.
    # Sets are used because they only store unique elements. This automatically
    # handles the requirement to ignore character frequency and order.
    # For instance, set('aabbc') will result in {'a', 'b', 'c'}.
    set_one = set(string_one)
    set_two = set(string_two)

    # Compare the two sets.
    # If the sets are equal, it means they contain the exact same unique characters.
    return set_one == set_two


def are_words_equivalent(
    word1: str,
    word2: str,
    levenshtein_threshold: float = 0.85,
    jaro_winkler_threshold: float = 0.9,
    metaphone_required: bool = True
) -> Tuple[bool, Dict[str, Any]]:
    """
    Propuesta de mejores prácticas para determinar si dos palabras son
    "efectivamente la misma" basándose en una combinación de algoritmos
    de similitud.

    Esta función de nivel superior es un wrapper para el método estático
    WordSimilarity.are_words_equivalent.

    Este enfoque combina la similitud fonética (Metaphone) con métricas
    de distancia de edición (Levenshtein y Jaro-Winkler) para ofrecer
    un criterio más robusto que una sola métrica.
    Puede ser configurado mediante umbrales.

    Args:
        word1 (str): La primera palabra a comparar.
        word2 (str): La segunda palabra a comparar.
        levenshtein_threshold (float): Umbral para la similitud de Levenshtein.
                                       Las palabras se consideran similares si el ratio
                                       de Levenshtein es igual o superior a este valor.
                                       (Valor por defecto: 0.85)
        jaro_winkler_threshold (float): Umbral para la similitud de Jaro-Winkler.
                                        Las palabras se consideran similares si el score
                                        de Jaro-Winkler es igual o superior a este valor.
                                        (Valor por defecto: 0.9)
        metaphone_required (bool): Si es True, las palabras deben tener
                                   similitud fonética según Metaphone para
                                   ser consideradas "la misma".
                                   (Valor por defecto: True)

    Returns:
        Tuple[bool, Dict[str, Any]]: Una tupla que contiene:
            - bool: True si las palabras son consideradas "efectivamente la misma", False en caso contrario.
            - Dict[str, Any]: Un diccionario con los resultados de las métricas
                              utilizadas para la decisión.

    Raises:
        TypeError: Si alguno de los argumentos de entrada no es una cadena.

    Ejemplos de Uso:
        >>> # Caso 1: Palabras muy similares tipográficamente y fonéticamente
        >>> result, metrics = are_words_equivalent("conocimiento", "conosimiento")
        >>> result
        True
        >>> metrics['metaphone_match']
        True
        >>> metrics['levenshtein_ratio'] > 0.85
        True

        >>> # Caso 2: Palabras diferentes, no deberían coincidir
        >>> result, metrics = are_words_equivalent("casa", "perro")
        >>> result
        False
        >>> metrics['levenshtein_ratio'] < 0.85
        True

    Guía de Implementación:
        Esta función de utilidad es la forma recomendada de usar el criterio
        de "igualdad efectiva" sin necesidad de instanciar `WordSimilarity`
        explícitamente. Permite un control fino sobre los umbrales de decisión.
    """
    return WordSimilarity.are_words_equivalent(
        word1, word2,
        levenshtein_threshold,
        jaro_winkler_threshold,
        metaphone_required
    )


def string_hamming_score(a: str, b: str) -> Dict[str, float]:
    """
    Calculates the Hamming similarity scores between two strings.

    The Hamming distance measures the minimum number of substitutions required
    to change one string into another. Only applicable to strings of equal length.
    Counts the number of positions in which the corresponding symbols are different.

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        Dict[str, float]: Dictionary with:
            - 'distance': Number of differing positions.
            - 'similarity': Normalized similarity (0.0 to 1.0).
            - 'score': Similarity as percentage (0.0 to 100.0).

    Examples:
        >>> string_hamming_score('text', 'test')
        {'distance': 1, 'similarity': 0.75, 'score': 75.0}
        >>> string_hamming_score('arrow', 'arow')
        {'distance': 3, 'similarity': 0.4, 'score': 40.0}

    Cost:
        $O(n)$ where n is the length of the strings.
    """
    td = _lazy_import('textdistance')
    return {
        "distance": td.hamming.distance(a, b),
        "similarity": td.hamming.normalized_similarity(a, b),
        "score": 100.0 * td.hamming.normalized_similarity(a, b)
    }


def string_mra_score(a: str, b: str) -> Dict[str, float]:
    """
    Calculates the Match Rating Approach (MRA) similarity scores.

    The MRA algorithm is a phonetic matching algorithm designed for comparing names.
    It generates a classification code for each string and calculates distance
    based on comparing these codes. Particularly useful for name matching.

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        Dict[str, float]: Dictionary with:
            - 'distance': MRA distance value.
            - 'similarity': Normalized similarity (0.0 to 1.0).
            - 'score': Similarity as percentage (0.0 to 100.0).

    Examples:
        >>> string_mra_score('Schmitt', 'Schmidt')
        {'distance': ..., 'similarity': 0.833, 'score': 83.3}
        >>> string_mra_score('John', 'Jon')
        {'distance': ..., 'similarity': 1.0, 'score': 100.0}

    Cost:
        $O(n + m)$ where n and m are the lengths of the strings.
    """
    td = _lazy_import('textdistance')
    return {
        "distance": td.mra.distance(a, b),
        "similarity": td.mra.normalized_similarity(a, b),
        "score": 100.0 * td.mra.normalizsed_similarity(a, b)
    }


def string_sorensendice_score(a: str, b: str) -> Dict[str, float]:
    """
    Calculates the Sørensen-Dice similarity coefficient based on tokens (words).

    This coefficient measures the similarity between two sets by finding common tokens
    and dividing by the total number of tokens. The strings are divided into words
    (tokens) by whitespace, making it useful for comparing phrases or documents.

    Formula: 2 * |common_tokens| / (|tokens_a| + |tokens_b|)

    Args:
        a (str): The first string to compare (will be tokenized).
        b (str): The second string to compare (will be tokenized).

    Returns:
        Dict[str, float]: Dictionary with:
            - 'distance': Sørensen-Dice distance (1 - similarity).
            - 'similarity': Normalized similarity (0.0 to 1.0).
            - 'score': Similarity as percentage (0.0 to 100.0).

    Examples:
        >>> string_sorensendice_score('hello world', 'world hello')
        {'distance': 0.0, 'similarity': 1.0, 'score': 100.0}
        >>> string_sorensendice_score('hello new world', 'hello world')
        {'distance': 0.2, 'similarity': 0.8, 'score': 80.0}

    Cost:
        $O(n + m)$ where n and m are the number of tokens.
    """
    td = _lazy_import('textdistance')
    a_tokens = a.split()
    b_tokens = b.split()
    return {
        "distance": td.sorensen.distance(a_tokens, b_tokens),
        "similarity": td.sorensen.normalized_similarity(a_tokens, b_tokens),
        "score": 100.0 * td.sorensen.normalized_similarity(a_tokens, b_tokens)
    }


def string_levenshtein_score(a: str, b: str) -> Dict[str, float]:
    """
    Calculates the Levenshtein (edit) distance and similarity scores.

    The Levenshtein distance counts the minimum number of single-character edits
    (insertions, deletions, or substitutions) needed to transform one string into
    another. Also known as Damerau-Levenshtein distance when it includes transpositions.

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        Dict[str, float]: Dictionary with:
            - 'distance': Number of edits required.
            - 'similarity': Normalized similarity (0.0 to 1.0).
            - 'score': Similarity as percentage (0.0 to 100.0).

    Examples:
        >>> string_levenshtein_score('kitten', 'sitting')
        {'distance': 3, 'similarity': 0.571, 'score': 57.1}
        >>> string_levenshtein_score('casa', 'caza')
        {'distance': 1, 'similarity': 0.75, 'score': 75.0}

    Cost:
        $O(m \\times n)$ where m and n are the lengths of the strings.
    """
    td = _lazy_import('textdistance')
    return {
        "distance": td.levenshtein.distance(a, b),
        "similarity": td.levenshtein.normalized_similarity(a, b),
        "score": 100.0 * td.levenshtein.normalized_similarity(a, b)
    }


def string_dna_score(a: str, b: str) -> Dict[str, float]:
    """
    Calculates the Needleman-Wunsch similarity scores (DNA sequence alignment).

    This algorithm is commonly used in bioinformatics to align DNA or protein sequences.
    It finds the optimal global alignment between two sequences, considering costs
    for matches, mismatches, and gaps. The gap cost is configurable (default: 1).

    Args:
        a (str): The first string/sequence to compare.
        b (str): The second string/sequence to compare.

    Returns:
        Dict[str, float]: Dictionary with:
            - 'distance': Needleman-Wunsch distance.
            - 'similarity': Normalized similarity (can be negative).
            - 'score': Similarity as percentage (-100.0 to 100.0).

    Examples:
        >>> string_dna_score('AAAGGT', 'ATACGGA')
        {'distance': 3.0, 'similarity': -0.428, 'score': -42.8}
        >>> string_dna_score('casa', 'caza')
        {'distance': 1.0, 'similarity': 0.75, 'score': 75.0}

    Note:
        Gap cost can be adjusted via textdistance.needleman_wunsch.gap_cost.

    Cost:
        $O(m \\times n)$ where m and n are the lengths of the sequences.
    """
    td = _lazy_import('textdistance')
    td.needleman_wunsch.gap_cost = 1
    return {
        "distance": td.needleman_wunsch.distance(a, b),
        "similarity": td.needleman_wunsch.normalized_similarity(a, b),
        "score": 100.0 * td.needleman_wunsch.normalized_similarity(a, b)
    }


def string_jarowinkler_score(a: str, b: str) -> Dict[str, float]:
    """
    Calculates the Jaro-Winkler similarity scores.

    The Jaro-Winkler algorithm is a variant of Jaro that gives more weight to
    matching prefixes. It's particularly effective for comparing short strings
    or names with typographical errors at the beginning. Higher scores for strings
    with common prefixes.

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        Dict[str, float]: Dictionary with:
            - 'distance': Jaro-Winkler distance (1 - similarity).
            - 'similarity': Normalized similarity (0.0 to 1.0).
            - 'score': Similarity as percentage (0.0 to 100.0).

    Examples:
        >>> string_jarowinkler_score('DwAyNE', 'DuANE')
        {'distance': 0.178, 'similarity': 0.822, 'score': 82.2}
        >>> string_jarowinkler_score('TRATE', 'TRACE')
        {'distance': 0.093, 'similarity': 0.907, 'score': 90.7}
        >>> string_jarowinkler_score('martha', 'marhta')
        {'distance': 0.039, 'similarity': 0.961, 'score': 96.1}

    Cost:
        $O(m \\times n)$ where m and n are the lengths of the strings.
    """
    td = _lazy_import('textdistance')
    return {
        "distance": td.jaro_winkler.distance(a, b),
        "similarity": td.jaro_winkler.normalized_similarity(a, b),
        "score": 100.0 * td.jaro_winkler.normalized_similarity(a, b)
    }


def string_jaccard_score(a: str, b: str) -> Dict[str, float]:
    """
    Calculates the Jaccard similarity index based on tokens (words).

    The Jaccard index measures similarity between two sets as the cardinality
    of their intersection divided by the cardinality of their union. Strings
    are tokenized by whitespace. Useful for measuring word overlap in phrases
    or documents.

    Formula: |intersection| / |union| = |A ∩ B| / |A ∪ B|

    Args:
        a (str): The first string to compare (will be tokenized).
        b (str): The second string to compare (will be tokenized).

    Returns:
        Dict[str, float]: Dictionary with:
            - 'distance': Jaccard distance (1 - similarity).
            - 'similarity': Normalized similarity (0.0 to 1.0).
            - 'score': Similarity as percentage (0.0 to 100.0).

    Examples:
        >>> string_jaccard_score('hello world', 'world hello')
        {'distance': 0.0, 'similarity': 1.0, 'score': 100.0}
        >>> string_jaccard_score('hello new world', 'hello world')
        {'distance': 0.333, 'similarity': 0.667, 'score': 66.7}

    Cost:
        $O(n + m)$ where n and m are the number of tokens.
    """
    td = _lazy_import('textdistance')
    a_tokens = a.split()
    b_tokens = b.split()
    return {
        "distance": td.jaccard.distance(a_tokens, b_tokens),
        "similarity": td.jaccard.normalized_similarity(a_tokens, b_tokens),
        "score": 100.0 * td.jaccard.normalized_similarity(a_tokens, b_tokens)
    }


def string_ratcliffobershelp_score(a: str, b: str) -> Dict[str, float]:
    """
    Calculates the Ratcliff-Obershelp pattern recognition similarity scores.

    This algorithm finds the longest common substring from two strings, removes
    that part from both, and splits at the same location. It repeats this process
    recursively on the left and right parts until no significant common substrings
    remain. Effective for comparing strings with common subsequences even if not
    in the same order.

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        Dict[str, float]: Dictionary with:
            - 'distance': Ratcliff-Obershelp distance.
            - 'similarity': Normalized similarity (0.0 to 1.0).
            - 'score': Similarity as percentage (0.0 to 100.0).

    Examples:
        >>> string_ratcliffobershelp_score('i am going home', 'gone home')
        {'distance': 0.34, 'similarity': 0.66, 'score': 66.0}
        >>> string_ratcliffobershelp_score('test', 'text')
        {'distance': 0.25, 'similarity': 0.75, 'score': 75.0}
        >>> string_ratcliffobershelp_score('arrow', 'arow')
        {'distance': 0.11, 'similarity': 0.89, 'score': 88.9}

    Cost:
        $O(m \\times n)$ in the average case, can be slower for complex patterns.
    """
    td = _lazy_import('textdistance')
    return {
        "distance": td.ratcliff_obershelp.distance(a, b),
        "similarity": td.ratcliff_obershelp.normalized_similarity(a, b),
        "score": 100.0 * td.ratcliff_obershelp.normalized_similarity(a, b)
    }


def string_diflib_seqmatch_score(a: str, b: str) -> float:
    """
    Calculates the similarity score using difflib.SequenceMatcher.

    This function uses Python's built-in difflib library to compute the ratio
    of the longest common subsequence between two strings. It's equivalent to
    the LCS-based calculation and provides a quick similarity measure.

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        float: The similarity score as percentage (0.0 to 100.0).

    Examples:
        >>> string_diflib_seqmatch_score('kitten', 'sitting')
        57.14
        >>> string_diflib_seqmatch_score('hello', 'hello')
        100.0

    Cost:
        $O(m \\times n)$ where m and n are the lengths of the strings.
    """
    return 100.0 * difflib.SequenceMatcher(a=a, b=b).ratio()


def string_lcs_score(a: str, b: str) -> float:
    """
    Calculates the Longest Common Subsequence (LCS) similarity score.

    The LCS is the longest sequence that appears in both strings in the same
    order, but not necessarily contiguously. The score is calculated as
    200 * LCS_length / (len_a + len_b), providing a percentage-like metric.

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        float: The LCS similarity score as percentage (0.0 to 100.0).

    Examples:
        >>> string_lcs_score('ABCBDAB', 'BDCABA')
        66.67  # LCS is 'BCBA' with length 4
        >>> string_lcs_score('hello', 'hallo')
        80.0

    Cost:
        $O(m \\times n)$ where m and n are the lengths of the strings.
    """
    n1 = len(a)
    n2 = len(b)
    if n1 == 0 or n2 == 0:
        return 0.0
    previous = []
    for i in range(n2):
        previous.append(0)
    over = 0
    for ch1 in a:
        left = corner = 0
        for ch2 in b:
            over = previous.pop(0)
            if ch1 == ch2:
                this = corner + 1
            else:
                this = over if over >= left else left
            previous.append(this)
            left, corner = this, over
    return 200.0 * previous.pop() / (n1 + n2)


def string_lcs_record(a: str, b: str) -> Tuple[float, str]:
    """
    Calculates the Longest Common Subsequence (LCS) score and extracts the actual LCS string.

    This function not only computes the similarity score but also returns the actual
    longest common subsequence found between the two strings. Useful for understanding
    which parts of the strings match.

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        Tuple[float, str]: A tuple containing:
            - score: The LCS similarity score as percentage (0.0 to 100.0).
            - sequence: The actual longest common subsequence string.

    Examples:
        >>> string_lcs_record('ABCBDAB', 'BDCABA')
        (66.67, 'BCBA')
        >>> string_lcs_record('hello world', 'hola mundo')
        (36.36, 'lo od')

    Cost:
        $O(m \\times n)$ where m and n are the lengths of the strings.
    """
    n1 = len(a)
    n2 = len(b)
    if n1 == 0 or n2 == 0:
        return 0.0, ''
    previous = deque()
    for i in range(n2):
        previous.append((0, ''))
    over = (0, '')
    for i in range(n1):
        left = corner = (0, '')
        for j in range(n2):
            over = previous.popleft()
            if a[i] == b[j]:
                this = (corner[0] + 1, corner[1] + a[i])
            else:
                this = max(over, left)
            previous.append(this)
            left, corner = this, over
    score = 200.0 * this[0] / (n1 + n2)
    return score, this[1]


def string_similarity_score(a: str, b: str) -> List[Tuple[str, Union[Dict[str, float], float]]]:
    """
    Calculates similarity scores using multiple string comparison algorithms.

    This comprehensive function computes similarity metrics using eight different
    algorithms, providing a complete overview of how similar two strings are from
    various perspectives (phonetic, edit distance, token-based, pattern matching).

    Algorithms included:
    - Hamming: Character position differences
    - MRA: Phonetic matching for names
    - Sørensen-Dice: Token-based similarity
    - Levenshtein: Edit distance
    - DNA (Needleman-Wunsch): Sequence alignment
    - Jaro-Winkler: Prefix-weighted similarity
    - Jaccard: Set intersection/union
    - Ratcliff-Obershelp: Pattern recognition

    Args:
        a (str): The first string to compare.
        b (str): The second string to compare.

    Returns:
        List[Tuple[str, Union[Dict[str, float], float]]]: List of tuples where each
            tuple contains the algorithm name and its result (either a dict with
            'distance', 'similarity', 'score' or a float score).

    Examples:
        >>> scores = string_similarity_score('hello', 'hallo')
        >>> for name, result in scores:
        ...     print(f"{name}: {result}")
        hamming: {'distance': 1, 'similarity': 0.8, 'score': 80.0}
        mra: {'distance': 0.0, 'similarity': 1.0, 'score': 100.0}
        ...

    Cost:
        Varies by algorithm, up to $O(m \\times n)$ for most algorithms.
    """
    lscores = []
    lscores.append(('hamming', string_hamming_score(a, b)))
    lscores.append(('mra', string_mra_score(a, b)))
    lscores.append(('sorensendice', string_sorensendice_score(a, b)))
    lscores.append(('levenshtein', string_levenshtein_score(a, b)))
    lscores.append(('dna', string_dna_score(a, b)))
    lscores.append(('jarowinkler', string_jarowinkler_score(a, b)))
    lscores.append(('jaccard', string_jaccard_score(a, b)))
    lscores.append(('ratcliffobershelp', string_ratcliffobershelp_score(a, b)))
    return lscores


if __name__ == "__main__":
    print("--- Demostración de Comparación de Similitud de Palabras ---")
    ws = WordSimilarity()

    # Ejemplo de uso de compare()
    word1_compare = "computadora"
    word2_compare = "computador"
    print(f"\nComparando '{word1_compare}' y '{word2_compare}':")
    try:
        results = ws.compare(word1_compare, word2_compare)
        for metric, value in results.items():
            if isinstance(value, dict):
                print(f"  {metric}:")
                for sub_metric, sub_value in value.items():
                    print(f"    {sub_metric}: {sub_value}")
            else:
                print(f"  {metric}: {value}")
    except ImportError as e:
        print(f"No se pudieron calcular todas las métricas debido a una librería faltante: {e}")

    # Batería de Ejemplos para are_words_equivalent()
    print("\n--- Demostración de 'are_words_equivalent' (Mejores Prácticas) ---")

    test_cases = [
        ("conocimiento", "conosimiento", True),  # Similares fonéticamente y tipográficamente
        ("aplicacion", "aplikacion", True),      # Error ortográfico común
        ("Smith", "Smyth", True),                 # Nombres propios
        ("color", "colour", True),                # Variantes de idioma (requiere ajuste de umbrales o consideración cultural)
        ("alberto", "huberto", False),            # Diferentes fonéticamente
        ("casa", "caza", True),                   # Una letra diferente
        ("telefono", "telefno", True),            # Letra faltante
        ("programacion", "progrmacion", True),    # Omisión de vocal
        ("gato", "perro", False),                 # Completamente diferentes
        ("internet", "intranet", False),          # Palabras que suenan similar pero significan diferente
        ("hello", "hola", False),                 # Idiomas diferentes
        ("cancelar", "cancela", True),             # Forma verbal diferente
        ("organizar", "organise", True),          # Variante de ortografía (inglés americano vs británico)
        ("doctor", "doc", False),                 # Abreviatura, puede que no pase umbrales estrictos
        ("software", "sofftware", True),          # Error tipográfico
        ("identificador", "identificadr", True),
        ("implementacion", "implementacion", True) # Idénticas
    ]

    print("\nCasos de Prueba con umbrales por defecto (Levenshtein>=0.85, Jaro-Winkler>=0.9, Metaphone requerido=True):")
    for word1, word2, expected in test_cases:
        try:
            result, metrics = are_words_equivalent(word1, word2)
            status = "PASÓ" if result == expected else "FALLÓ"
            print(f"\nPalabras: '{word1}', '{word2}'")
            print(f"  Decisión Esperada: {expected}, Decisión Obtenida: {result} - {status}")
            print(f"  Métricas de Decisión: Metaphone Match={metrics['metaphone_match']:.0f}, Levenshtein Ratio={metrics['levenshtein_ratio']:.4f}, Jaro-Winkler Similarity={metrics['jaro_winkler_similarity']:.4f}")
        except ImportError as e:
            print(f"\nSaltando prueba para '{word1}', '{word2}' debido a una librería faltante: {e}")

    print("\n--- Ejemplos adicionales para otras funciones ---")

    # has_same_words
    print("\n--- has_same_words ---")
    print(f"'hello world', 'world hello': {has_same_words('hello world', 'world hello')}")
    print(f"'python programming', 'programming python': {has_same_words('python programming', 'programming python')}")
    print(f"'apple banana', 'banana orange': {has_same_words('apple banana', 'banana orange')}")
    print(f"'HELLO world', 'world hello': {has_same_words('HELLO world', 'world hello')}")
    print(f"'one two two', 'two one two': {has_same_words('one two two', 'two one two')}")

    # find_common_words
    print("\n--- find_common_words ---")
    print(f"'The quick brown fox', 'A quick brown dog': {find_common_words('The quick brown fox', 'A quick brown dog')}")
    print(f"'Hello world', 'WORLD hello': {find_common_words('Hello world', 'WORLD hello')}")
    print(f"'apple banana orange', 'grape kiwi pineapple': {find_common_words('apple banana orange', 'grape kiwi pineapple')}")
    print(f"'common common word', 'common common phrase': {find_common_words('common common word', 'common common phrase')}")

    # has_same_characters
    print("\n--- has_same_characters ---")
    print(f"'listen', 'silent': {has_same_characters('listen', 'silent')}")
    print(f"'aabbcc', 'abc': {has_same_characters('aabbcc', 'abc')}")
    print(f"'hello', 'world': {has_same_characters('hello', 'world')}")
    print(f"'apple', 'aple': {has_same_characters('apple', 'aple')}")
    print(f"'', '': {has_same_characters('', '')}")
    print(f"'a', '': {has_same_characters('a', '')}")

    # Demostración del wrapper calculate_similarity
    print("\n" + "="*80)
    print("--- Demostración del Wrapper calculate_similarity() ---")
    print("="*80)

    print("\n1. USO BÁSICO - Levenshtein (por defecto)")
    print("-" * 50)
    resultado = calculate_similarity("casa", "caza")
    print(f"calculate_similarity('casa', 'caza')")
    print(f"  Resultado: {resultado:.2%}")

    print("\n2. SIMILITUD FONÉTICA - Metaphone")
    print("-" * 50)
    resultado = calculate_similarity("conocimiento", "conosimiento", algorithm='metaphone')
    print(f"calculate_similarity('conocimiento', 'conosimiento', algorithm='metaphone')")
    print(f"  ¿Suenan igual?: {resultado}")

    print("\n3. JARO-WINKLER - Excelente para nombres")
    print("-" * 50)
    resultado = calculate_similarity("martha", "marhta", algorithm='jaro_winkler')
    print(f"calculate_similarity('martha', 'marhta', algorithm='jaro_winkler')")
    print(f"  Score: {resultado['score']:.4f}")
    print(f"  Normalized Similarity: {resultado['normalized_similarity']:.4f}")

    print("\n4. EQUIVALENCIA EFECTIVA - Criterio combinado")
    print("-" * 50)
    resultado, metricas = calculate_similarity("aplicacion", "aplikacion", algorithm='effective_same')
    print(f"calculate_similarity('aplicacion', 'aplikacion', algorithm='effective_same')")
    print(f"  ¿Son la misma?: {resultado}")
    print(f"  Métricas:")
    for key, value in metricas.items():
        print(f"    {key}: {value}")

    print("\n5. LCS - Longest Common Subsequence")
    print("-" * 50)
    resultado = calculate_similarity("ABCBDAB", "BDCABA", algorithm='lcs')
    print(f"calculate_similarity('ABCBDAB', 'BDCABA', algorithm='lcs')")
    print(f"  Secuencia común: '{resultado['sequence']}'")
    print(f"  Longitud: {resultado['length']}")
    print(f"  Similarity: {resultado['similarity']:.4f}")

    print("\n6. TODOS LOS ALGORITMOS - Comparación completa")
    print("-" * 50)
    resultados = calculate_similarity("python", "pyton", algorithm='all')
    print(f"calculate_similarity('python', 'pyton', algorithm='all')")
    print("  Resultados seleccionados:")
    print(f"    Metaphone Match: {resultados['metaphone_match']}")
    print(f"    Levenshtein Ratio: {resultados['levenshtein_ratio']:.4f}")
    print(f"    Jaro-Winkler Score: {resultados['jaro_winkler']['score']:.4f}")
    print(f"    LCS: '{resultados['lcs']['sequence']}' (longitud: {resultados['lcs']['length']})")

    print("\n7. COMPARACIÓN DE FRASES - Sørensen-Dice")
    print("-" * 50)
    resultado = calculate_similarity(
        "the quick brown fox",
        "a quick red fox",
        algorithm='sorensen_dice'
    )
    print(f"calculate_similarity('the quick brown fox', 'a quick red fox', algorithm='sorensen_dice')")
    print(f"  Score: {resultado['score']:.4f}")
    print(f"  Similarity: {resultado['normalized_similarity']:.4f}")

    print("\n8. NEEDLEMAN-WUNSCH - Con gap cost personalizado")
    print("-" * 50)
    resultado = calculate_similarity("GATTACA", "GTAC", algorithm='needleman_wunsch', nw_gap_cost=2)
    print(f"calculate_similarity('GATTACA', 'GTAC', algorithm='needleman_wunsch', nw_gap_cost=2)")
    print(f"  Score: {resultado['score']:.4f}")
    print(f"  Normalized Similarity: {resultado['normalized_similarity']:.4f}")

    print("\n9. EFFECTIVE SAME - Con umbrales personalizados")
    print("-" * 50)
    resultado, metricas = calculate_similarity(
        "color", "colour",
        algorithm='effective_same',
        levenshtein_threshold=0.75,
        jaro_winkler_threshold=0.85,
        metaphone_required=False
    )
    print(f"calculate_similarity('color', 'colour', algorithm='effective_same', ...)")
    print(f"  ¿Son la misma?: {resultado}")
    print(f"  Levenshtein Ratio: {metricas['levenshtein_ratio']:.4f}")

    print("\n10. USO EN BÚSQUEDA DIFUSA (Ejemplo práctico)")
    print("-" * 50)
    diccionario = ["aplicacion", "computadora", "programacion", "desarrollo", "software"]
    consulta = "aplikacion"
    print(f"Buscar '{consulta}' en diccionario: {diccionario}")
    print("\nCoincidencias (Levenshtein > 0.75):")
    coincidencias = []
    for palabra in diccionario:
        ratio = calculate_similarity(consulta, palabra, algorithm='levenshtein')
        if ratio > 0.75:
            coincidencias.append((palabra, ratio))
    coincidencias.sort(key=lambda x: x[1], reverse=True)
    for palabra, ratio in coincidencias:
        print(f"  {palabra}: {ratio:.2%}")

    print("\n" + "="*80)
    print("--- Fin de la demostración del wrapper ---")
    print("="*80)

    print("\n--- Fin de la demostración ---")