import sqlite3
import os
from typing import List, Tuple, Dict, Any

# Importar las clases de los módulos (asegúrate de que los archivos estén en el mismo directorio)
try:
    from agentfx.fxString.string_spellcheck import UniversalSpellChecker
    from agentfx.fxString.string_similarity import WordSimilarity
except ImportError as e:
    print(f"Error al importar módulos. Asegúrate de instalar las dependencias: pip install agentfx")
    print(f"Detalle del error: {e}")
    print("Por favor, verifica la instalación de las dependencias también.")
    exit()

DATABASE_NAME = 'names_database.db'

def setup_database():
    """Configura una base de datos SQLite con tablas para personas y empresas."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    # Crear tabla de personas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS persons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    # Crear tabla de empresas
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS companies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    # Insertar algunos datos de ejemplo (solo si no existen)
    sample_persons = [
        ("Juan Perez",), ("Maria Garcia",), ("Carlos Ruiz",),
        ("Laura Fernandez",), ("David Lopez",), ("Ana Martinez",)
    ]
    sample_companies = [
        ("Google Inc.",), ("Microsoft Corp.",), ("Apple S.A.",),
        ("Amazon Web Services",), ("IBM",), ("Oracle Corp",)
    ]

    for table, samples in [("persons", sample_persons), ("companies", sample_companies)]:
        for name_tuple in samples:
            try:
                cursor.execute(f"INSERT INTO {table} (name) VALUES (?)", name_tuple)
            except sqlite3.IntegrityError:
                # El nombre ya existe, lo ignoramos
                pass
    
    conn.commit()
    conn.close()
    print(f"Base de datos '{DATABASE_NAME}' configurada con datos de ejemplo.")

def get_names_from_db(table_name: str) -> List[str]:
    """Obtiene todos los nombres de una tabla específica de la base de datos."""
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM {table_name}")
    names = [row[0] for row in cursor.fetchall()]
    conn.close()
    return names

def correct_and_validate_name(
    input_name: str,
    reference_names: List[str],
    name_type: str,
    spell_corrector: UniversalSpellChecker,
    similarity_checker: WordSimilarity
) -> Tuple[str, bool, str]:
    """
    Corrige un nombre de entrada y lo valida contra una lista de nombres de referencia.

    Args:
        input_name (str): El nombre a corregir y validar.
        reference_names (List[str]): Lista de nombres válidos para comparar.
        name_type (str): Tipo de nombre ('Persona' o 'Empresa') para mensajes.
        spell_corrector (UniversalSpellChecker): Instancia del corrector ortográfico.
        similarity_checker (WordSimilarity): Instancia del verificador de similitud.

    Returns:
        Tuple[str, bool, str]: Tupla con (nombre_corregido, es_valido, mensaje_validacion).
    """
    print(f"\n--- Procesando {name_type}: '{input_name}' ---")

    # 1. Corrección del nombre
    try:
        corrected_name = spell_corrector.correct(input_name)
        print(f"  Nombre corregido: '{corrected_name}'")
    except ImportError as e:
        print(f"  No se pudo corregir el nombre debido a una librería de corrección faltante: {e}")
        return input_name, False, "Corrección fallida: Dependencias no instaladas."
    except Exception as e:
        print(f"  Error inesperado durante la corrección: {e}")
        corrected_name = input_name # Fallback a nombre original
        
    is_valid = False
    validation_message = f"'{corrected_name}' no se encontró directamente."

    # 2. Validación: Búsqueda exacta en los nombres de referencia
    if corrected_name in reference_names:
        is_valid = True
        validation_message = f"'{corrected_name}' es un {name_type} válido (coincidencia exacta)."
    else:
        # 3. Validación: Búsqueda aproximada usando similitud de palabras
        print(f"  Buscando coincidencia aproximada para '{corrected_name}' en el diccionario de {name_type}s...")
        best_match_name = None
        best_match_score = 0.0
        
        try:
            for ref_name in reference_names:
                # Usamos la función are_words_effectively_the_same para una validación robusta
                # Se pueden ajustar los umbrales si es necesario
                are_same, metrics = similarity_checker.are_words_effectively_the_same(
                    corrected_name, ref_name,
                    levenshtein_threshold=0.8,  # Ajusta según la permisividad deseada
                    jaro_winkler_threshold=85.0, # Ajusta según la permisividad deseada
                    metaphone_required=True # Para nombres, la fonética es importante
                )
                
                # Si se consideran "efectivamente el mismo", lo marcamos como válido
                if are_same:
                    is_valid = True
                    best_match_name = ref_name
                    # Podrías usar un score combinado para elegir el "mejor" si hay múltiples matches
                    best_match_score = metrics.get('jaro_winkler_score', 0) # Ejemplo de cómo obtener un score
                    validation_message = f"'{corrected_name}' es válido y coincide aproximadamente con '{best_match_name}' (score Jaro-Winkler: {best_match_score:.2f})."
                    break # Encontramos una buena coincidencia, salimos

            if not is_valid:
                validation_message = f"'{corrected_name}' no se validó contra ningún {name_type} existente."
        except ImportError as e:
            print(f"  No se pudo validar el nombre debido a una librería de similitud faltante: {e}")
            validation_message = "Validación fallida: Dependencias no instaladas."
            is_valid = False
        except Exception as e:
            print(f"  Error inesperado durante la validación: {e}")
            validation_message = f"Error en la validación: {e}"
            is_valid = False

    return corrected_name, is_valid, validation_message

def main():
    """Función principal para corregir y validar nombres."""
    print("Iniciando programa de corrección y validación de nombres.")

    # 1. Configurar la base de datos de ejemplo
    setup_database()

    # 2. Cargar los diccionarios de nombres desde la base de datos
    person_names_db = get_names_from_db('persons')
    company_names_db = get_names_from_db('companies')

    print(f"\nNombres de personas cargados ({len(person_names_db)}): {person_names_db}")
    print(f"Nombres de empresas cargados ({len(company_names_db)}): {company_names_db}")

    # 3. Inicializar el corrector ortográfico y el verificador de similitud
    #    Pasamos ambos vocabularios al UniversalSpellChecker para que pueda usarlos.
    #    UniversalSpellChecker internamente maneja el vocabulario para correcciones.
    #    WordSimilarity se usará para la fase de validación.
    all_known_names = list(set(person_names_db + company_names_db))
    
    # Intentar inicializar los correctores
    spell_corrector = None
    similarity_checker = None

    try:
        spell_corrector = UniversalSpellChecker(custom_vocabulary=all_known_names, language='es')
        similarity_checker = WordSimilarity() # No necesita vocabulario, usa algoritmos
    except ImportError as e:
        print(f"\n[ERROR CRÍTICO] Una de las librerías principales no está instalada o el modelo de spaCy falta. Por favor, revisa los pasos de instalación.")
        print(f"  Detalle: {e}")
        print("  Asegúrate de ejecutar: `pip install pyspellchecker symspellpy rapidfuzz spacy metaphone python-Levenshtein jellyfish textdistance`")
        print("  Y también: `python -m spacy download es_core_news_sm`")
        return
    except Exception as e:
        print(f"\n[ERROR CRÍTICO] Un error inesperado ocurrió durante la inicialización de los correctores: {e}")
        return


    # 4. Ejemplos de uso
    names_to_process = [
        # Nombres de personas
        {"name": "Juann Peres", "type": "Persona"},
        {"name": "Mara Gracia", "type": "Persona"},
        {"name": "Caros Ruiiz", "type": "Persona"},
        {"name": "Luara Fernadez", "type": "Persona"},
        {"name": "Albert Einsten", "type": "Persona"}, # Nombre no en la base de datos
        
        # Nombres de empresas
        {"name": "Gooogle Inc", "type": "Empresa"},
        {"name": "Microsot Corpp", "type": "Empresa"},
        {"name": "Aple SA", "type": "Empresa"},
        {"name": "Amason Web Servies", "type": "Empresa"},
        {"name": "Tezla Motors", "type": "Empresa"}, # Nombre no en la base de datos
    ]

    results = []
    for item in names_to_process:
        name = item["name"]
        name_type = item["type"]
        
        if name_type == "Persona":
            ref_list = person_names_db
        else: # "Empresa"
            ref_list = company_names_db
        
        corrected, valid, message = correct_and_validate_name(
            name, ref_list, name_type, spell_corrector, similarity_checker
        )
        results.append({
            "Original": name,
            "Tipo": name_type,
            "Corregido": corrected,
            "Válido": valid,
            "Mensaje": message
        })

    print("\n\n--- Resumen de Resultados ---")
    for res in results:
        print(f"\nOriginal: {res['Original']}")
        print(f"Tipo:     {res['Tipo']}")
        print(f"Corregido: {res['Corregido']}")
        print(f"Válido:   {res['Válido']}")
        print(f"Mensaje:  {res['Mensaje']}")

    # Limpiar la base de datos de ejemplo al finalizar (opcional)
    # if os.path.exists(DATABASE_NAME):
    #     os.remove(DATABASE_NAME)
    #     print(f"\nBase de datos '{DATABASE_NAME}' eliminada.")

if __name__ == "__main__":
    main()