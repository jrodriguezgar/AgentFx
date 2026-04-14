# --- Example of how to use UniversalSpellChecker ---

from formulite.fxString.string_spellcheck import UniversalSpellChecker

# 1. Use case: Correcting specific names from a predefined list.
print("--- Using UniversalSpellChecker with custom vocabulary ---")
nombres_propios = ["Javier", "Beatriz", "Alejandro", "Verónica"]
name_corrector = UniversalSpellChecker(custom_vocabulary=nombres_propios)

palabras_a_corregir_nombres = ["Javierr", "Beatris", "Alexandro"]
for palabra in palabras_a_corregir_nombres:
    corregida = name_corrector.correct(palabra)
    print(f"Original: '{palabra}', Corregido: '{corregida}'")

print("\n" + "="*40 + "\n")

# 2. Use case: General spell checking for common Spanish words.
print("--- Using UniversalSpellChecker for general text ---")
general_checker = UniversalSpellChecker(language='es')

palabras_a_corregir_general = ["cosina", "vienbenido", "diccionrio"]
for palabra in palabras_a_corregir_general:
    corregida = general_checker.correct(palabra)
    print(f"Original: '{palabra}', Corregido: '{corregida}'")

# --- Expected Output ---
# --- Using UniversalSpellChecker with custom vocabulary ---
# Original: 'Javierr', Corregido: 'Javier'
# Original: 'Beatris', Corregido: 'Beatriz'
# Original: 'Alexandro', Corregido: 'Alejandro'
#
# ========================================
#
# --- Using UniversalSpellChecker for general text ---
# Original: 'cosina', Corregido: 'cocina'
# Original: 'vienbenido', Corregido: 'bienvenido'
# Original: 'diccionrio', Corregido: 'diccionario'