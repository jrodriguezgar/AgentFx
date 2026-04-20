# fxPython — Python Utilities

Common design patterns, iterable utilities, type conversions, and logic helpers for Pythonic code.

## Submodules

| Submodule | Purpose |
|-----------|---------|
| [`py_tools`](../reference/fxPython/py_tools.md) | Dictionary builders, data manipulation utilities |
| [`py_itertools`](../reference/fxPython/py_itertools.md) | Iterable utilities (take, chunk, flatten, etc.) |
| [`py_logic`](../reference/fxPython/py_logic.md) | Logic helpers (coalesce, switch, ternary) |
| [`py_operations`](../reference/fxPython/py_operations.md) | General-purpose operations |
| [`py_convertions`](../reference/fxPython/py_convertions.md) | Type conversion utilities |

## Quick Examples

```python
from formulite.fxPython import py_tools, py_itertools, py_logic

# Create dictionary from parallel lists
d = py_tools.create_key_value_dictionary("id,name", (1, "Alice"))
# {'id': 1, 'name': 'Alice'}

# Take the first N items
first = py_itertools.take(3, range(10))  # [0, 1, 2]

# Coalesce (first non-None value)
value = py_logic.coalesce(None, None, "default")  # "default"
```
