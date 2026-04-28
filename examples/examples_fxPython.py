
# Examples of fxPython module usage
from agentfx.fxPython import py_operations, py_tools, py_itertools


# --- Example 1: Scientific expression evaluator ---
print("### Expression Evaluator ###")

expression1 = "3 + 4 * 5"
resultado1 = py_operations.calculate(expression1)
print(f"El resultado de '{expression1}' es: {resultado1}")

expression2 = "2 * (6 / 2) - 9 + 6"
resultado2 = py_operations.calculate(expression2)
print(f"El resultado de '{expression2}' es: {resultado2}")

try:
    expression3 = "5 * (3 + 2"  # Missing closing parenthesis
    py_operations.calculate(expression3)
except ValueError as e:
    print(f"Error al evaluar '{expression3}': {e}")


# --- Example 2: Dictionary creation ---
print("\n### Dictionary Tools ###")

dictionary = py_tools.create_key_value_dictionary("id,name", (1, "Alice"))
print(f"create_key_value_dictionary: {dictionary}")


# --- Example 3: Itertools utilities ---
print("\n### Itertools ###")

first_items = py_itertools.take(3, range(10))
print(f"take(3, range(10)): {first_items}")