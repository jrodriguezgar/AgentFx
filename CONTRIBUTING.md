# Contributing to FormuLite

Thank you for your interest in contributing to FormuLite! This guide explains how to add new formulas to the project step by step.

---

## Table of Contents

- [Project Architecture](#project-architecture)
- [Adding a New Function to an Existing Module](#adding-a-new-function-to-an-existing-module)
- [Creating a New File in an Existing Module](#creating-a-new-file-in-an-existing-module)
- [Creating a New Module](#creating-a-new-module)
- [Function Design Rules](#function-design-rules)
- [Docstring Format](#docstring-format)
- [Input Validation](#input-validation)
- [Writing Tests](#writing-tests)
- [Updating Documentation](#updating-documentation)
- [MCP Tool Name Convention](#mcp-tool-name-convention)
- [Checklist Before Submitting](#checklist-before-submitting)

---

## Project Architecture

### How It Works

1. Each `fx*` module has an `__init__.py` that calls `auto_export()` from `_loader.py`.
2. `auto_export()` dynamically imports submodules and re-exports all their public callables.
3. `registry.py` walks all `fx*` packages at runtime to discover functions and build JSON schemas.
4. The MCP server uses `registry.py` to expose functions via meta-tools — no manual registration needed.

**Key takeaway**: you only need to write a function in the right file and register the file in `__init__.py`. Everything else (discovery, MCP exposure, schema generation) is automatic.

---

## Adding a New Function to an Existing Module

This is the simplest case. Example: adding a `cube_root` function to `fxNumeric/arithmetic_functions.py`.

### Step 1 — Write the function

Open the target file and add your function:

```python
# formulite/fxNumeric/arithmetic_functions.py

def cube_root(x: float) -> float:
    """Calculates the cube root of a number.

    Description:
        Computes x^(1/3), handling negative numbers correctly.

    Args:
        x: The number to compute the cube root for.

    Returns:
        The cube root of x.

    Raises:
        TypeError: If x is not numeric.

    Usage Example:
        >>> from formulite.fxNumeric.arithmetic_functions import cube_root
        >>> cube_root(27)
        3.0
        >>> cube_root(-8)
        -2.0

    Cost: O(1)
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric (int or float).")

    if x >= 0:
        return x ** (1 / 3)

    return -((-x) ** (1 / 3))
```

### Step 2 — No additional registration needed

Since `arithmetic_functions` is already listed in `fxNumeric/__init__.py`, `auto_export` picks up any new public function automatically.

### Step 3 — Write tests

Add tests to the corresponding test file (see [Writing Tests](#writing-tests)).

### Step 4 — Update `llms.txt`

Add an entry under the correct `### file.py` section (see [Updating Documentation](#updating-documentation)).

---

## Creating a New File in an Existing Module

Example: adding a `matrix_functions.py` file to `fxNumeric`.

### Step 1 — Create the file

```python
# formulite/fxNumeric/matrix_functions.py

"""Matrix operations module.

This module provides basic matrix operations such as transposition,
multiplication, determinant, and identity generation.
"""

from typing import List


def matrix_transpose(matrix: List[List[float]]) -> List[List[float]]:
    """Transposes a 2D matrix (swaps rows and columns).

    Description:
        Given an m×n matrix, returns an n×m matrix where element [i][j]
        becomes [j][i].

    Args:
        matrix: A 2D list representing the matrix.

    Returns:
        The transposed matrix.

    Raises:
        TypeError: If matrix is not a list of lists.
        ValueError: If rows have inconsistent lengths.

    Usage Example:
        >>> from formulite.fxNumeric.matrix_functions import matrix_transpose
        >>> matrix_transpose([[1, 2], [3, 4]])
        [[1, 3], [2, 4]]

    Cost: O(m·n)
    """
    if not isinstance(matrix, list) or not all(isinstance(r, list) for r in matrix):
        raise TypeError("matrix must be a list of lists.")

    if matrix and len(set(len(r) for r in matrix)) > 1:
        raise ValueError("All rows must have the same length.")

    return [list(row) for row in zip(*matrix)]
```

### Step 2 — Register the file in `__init__.py`

Open `formulite/fxNumeric/__init__.py` and add the new file to `_SUBMODULES`:

```python
_SUBMODULES = [
    "arithmetic_functions",
    "calculator_functions",
    "constants_functions",
    "conversion_functions",
    "distribution_functions",
    "finance_functions",
    "format_functions",
    "interpolation_functions",
    "matrix_functions",        # ← NEW
    "number_theory_functions",
    "random_functions",
    "rounding_functions",
    "statistics_functions",
    "trigonometry_functions",
]
```

### Step 3 — Write tests and update docs

Follow [Writing Tests](#writing-tests) and [Updating Documentation](#updating-documentation).

---

## Creating a New Module

If none of the existing modules (`fxDate`, `fxNumeric`, `fxString`, `fxPython`, `fxExcel`, `fxVBA`) fits your functions, you can create a new module.

### Step 1 — Create the module directory

```
formulite/
└── fxGeometry/           # New module
    ├── __init__.py
    └── shape_functions.py
```

### Step 2 — Write `__init__.py`

Follow the exact same pattern as existing modules:

```python
# formulite/fxGeometry/__init__.py

"""fxGeometry — Geometric calculations and shape operations.

Re-exports all public functions from submodules. Submodules with
uninstalled optional dependencies are silently skipped.
"""

from formulite._loader import auto_export

_SUBMODULES = [
    "shape_functions",
]

auto_export("formulite.fxGeometry", _SUBMODULES, globals())
```

### Step 3 — Write your function files

Follow the same structure as [Adding a New Function](#adding-a-new-function-to-an-existing-module).

### Step 4 — Update documentation

- Add a new `## fxGeometry` section in `llms.txt`.
- Update the function count in the header of `llms.txt`.
- Add the module to the `README.md` main modules list.
- Create a `README.md` inside `formulite/fxGeometry/` describing the module.

---

## Function Design Rules

Every function in FormuLite must follow these principles:

| Rule | Description |
|------|-------------|
| **Atomic** | One function = one operation. Split into independent steps if possible. |
| **Pure** | Same inputs → same output. No side effects. |
| **Composable** | Small building blocks that combine easily via chaining or nesting. |
| **No hidden dependencies** | All inputs via parameters, all outputs via return values. |
| **Type-annotated** | Always annotate parameters and return types. |
| **Explicit failures** | Raise specific exceptions (`TypeError`, `ValueError`), never return ambiguous sentinels. |
| **Naming reflects action** | Name describes what it returns or does: `calculate_total`, `is_valid_date`, `parse_row`. |
| **Pythonic** | Clear, concise, minimal lines. |

---

## Docstring Format

Use **Google-style docstrings** with all these sections:

```python
def function_name(param: type) -> return_type:
    """Brief one-line description.

    Description:
        More detailed description (if needed) on as few lines as possible.

    Args:
        param: Purpose of the parameter.

    Returns:
        Description of the return value.

    Raises:
        ExceptionType: When it occurs.

    Usage Example:
        >>> from formulite.fxModule.file import function_name
        >>> function_name(value)
        expected_result

    Cost: O(n)
    """
```

Required sections: **description line**, **Args**, **Returns**. Include **Raises** if the function raises exceptions. Always include a **Usage Example** and **Cost** (Big-O complexity).

---

## Input Validation

Use the shared helpers in `formulite/_validators.py` for consistent error messages:

```python
from formulite._validators import ensure_type, ensure_numeric, ensure_positive

def my_function(value: float, name: str) -> float:
    ensure_numeric(value, "value")
    ensure_positive(value, "value")
    ensure_type(name, str, "name")
    # ... logic
```

Available validators:

| Function | Purpose |
|----------|---------|
| `ensure_type(value, expected, name)` | Checks `isinstance` |
| `ensure_numeric(value, name)` | Checks `int` or `float` |
| `ensure_positive(value, name)` | Checks `> 0` |

For domain-specific validation (e.g., date ranges), validate inline with clear error messages.

---

## Writing Tests

Tests live in the `tests/` directory and use **pytest**.

### Naming convention

- File: `test_<descriptive_name>.py`
- Function: `test_<unit>_<scenario>`

### Example test file

```python
# tests/test_matrix_functions.py

"""Tests for fxNumeric matrix operations."""

import pytest
from formulite.fxNumeric.matrix_functions import matrix_transpose


def test_matrix_transpose_square():
    assert matrix_transpose([[1, 2], [3, 4]]) == [[1, 3], [2, 4]]


def test_matrix_transpose_rectangular():
    assert matrix_transpose([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]]


def test_matrix_transpose_empty():
    assert matrix_transpose([]) == []


def test_matrix_transpose_invalid_type():
    with pytest.raises(TypeError):
        matrix_transpose("not a matrix")


def test_matrix_transpose_inconsistent_rows():
    with pytest.raises(ValueError):
        matrix_transpose([[1, 2], [3]])


@pytest.mark.parametrize("matrix, expected", [
    ([[1]], [[1]]),
    ([[1, 2]], [[1], [2]]),
])
def test_matrix_transpose_parametrized(matrix, expected):
    assert matrix_transpose(matrix) == expected
```

### Running tests

```bash
uv run pytest                        # All tests
uv run pytest tests/test_matrix_functions.py  # Specific file
uv run pytest -k "transpose"         # Filter by keyword
```

---

## Updating Documentation

Every new function requires updates to **two files** in the same step:

### 1. `llms.txt`

Add the function entry under the correct `### file.py` section:

```markdown
### matrix_functions.py
- `matrix_transpose(matrix)` - Transposes a 2D matrix (swaps rows and columns)
```

If you created a new file, add a new `### file.py` heading under the correct module section. Update the total function count in the header:

```markdown
# FormuLite - LLM Function Reference

**2181+ functions across 6 modules** | ...
```

### 2. Module `README.md`

If the module has a `README.md` (e.g., `formulite/fxNumeric/README.md`), add the new function there.

---

## MCP Tool Name Convention

Functions are automatically exposed via the MCP server with this naming pattern:

```
<module>.<file>.<function>
```

Example:
```
fxNumeric.matrix_functions.matrix_transpose
─────────┬────────────────  ────────────────
    │          │                   └── Function name
    │          └── Source file (without .py)
    └── Module name
```

You do **not** need to manually register the function in the MCP server — `registry.py` discovers it automatically from the `fx*` packages.

---

## Checklist Before Submitting

Use this checklist to make sure your contribution is complete:

- [ ] **Function written** in the correct module/file
- [ ] **Type hints** on all parameters and return type
- [ ] **Google-style docstring** with Description, Args, Returns, Raises, Usage Example, Cost
- [ ] **Input validation** using `_validators.py` helpers or inline checks
- [ ] **Pure function** — no side effects, no hidden dependencies
- [ ] **File registered** in `__init__.py` `_SUBMODULES` (if new file)
- [ ] **Tests written** in `tests/` with `pytest`
- [ ] **`llms.txt` updated** with function entry and updated count
- [ ] **Module README updated** (if applicable)
- [ ] **All tests pass** — `uv run pytest`

---

## Quick Reference: Where to Put Your Function

| Function Type | Module | Example Files |
|---------------|--------|---------------|
| Date/time operations | `fxDate` | `date_operations.py`, `date_convertions.py` |
| Math, arithmetic, calculus | `fxNumeric` | `arithmetic_functions.py`, `rounding_functions.py` |
| Finance, interest, amortization | `fxNumeric` | `finance_functions.py` |
| Statistics, distributions | `fxNumeric` | `statistics_functions.py`, `distribution_functions.py` |
| Text manipulation, formatting | `fxString` | `string_operations.py`, `string_similarity.py` |
| Collections, itertools, logic | `fxPython` | `py_itertools.py`, `py_convertions.py` |
| Excel-compatible formulas | `fxExcel` | `math_formulas.py`, `lookup_formulas.py` |
| VBA/Access-compatible | `fxVBA` | `array_functions.py`, `financial_functions.py` |
