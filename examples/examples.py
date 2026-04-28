# Examples using AgentFx functions

from agentfx.fxExcel.math_formulas import SUMIF
from agentfx.fxExcel.statistic_formulas import AVERAGE
from agentfx.fxExcel.text_formulas import CONCAT, LEFT, RIGHT
from agentfx.fxExcel.lookup_formulas import VLOOKUP

# Ejemplos de funciones matemáticas
numbers = [1, 2, 3, 4, 5]
sum_greater_than_3 = SUMIF(numbers, ">3")  # Resultado: 9 (4 + 5)
promedio = AVERAGE(numbers)  # Resultado: 3.0

# Ejemplos de funciones de texto
texto = CONCAT("Hola", " ", "Mundo")  # Resultado: "Hola Mundo"
primeras_letras = LEFT("Python", 2)  # Resultado: "Py"
ultimas_letras = RIGHT("Python", 2)  # Resultado: "on"

# Ejemplos de funciones de búsqueda
tabla = [
    ["Nombre", "Edad", "Ciudad"],
    ["Ana", 25, "Madrid"],
    ["Juan", 30, "Barcelona"]
]
edad_ana = VLOOKUP("Ana", tabla, 2, range_lookup=False)  # Resultado: 25
ciudad_juan = VLOOKUP("Juan", tabla, 3, range_lookup=False)  # Resultado: "Barcelona"