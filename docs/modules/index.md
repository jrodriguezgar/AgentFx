# Modules

FormuLite is organized into 6 thematic modules covering dates, mathematics, strings, Python utilities, and Excel/VBA compatibility.

| Module | Functions | Scope |
|--------|----------:|-------|
| [`fxDate`](fxdate.md) | 261 | Date operations, evaluations, conversions, system dates |
| [`fxNumeric`](fxnumeric.md) | 1,602 | Finance, statistics, geometry, transforms, series, number theory |
| [`fxString`](fxstring.md) | 331 | Text manipulation, regex, hashing, validation, encoding, similarity |
| [`fxPython`](fxpython.md) | 116 | Iterable utilities, type conversions, logic helpers |
| [`fxExcel`](fxexcel.md) | 489 | Excel-compatible formulas (VLOOKUP, PMT, CONCATENATE …) |
| [`fxVBA`](fxvba.md) | 133 | VBA/Access-compatible functions (Left, InStr, Format …) |

## Architecture

All modules follow the same pattern:

1. **Flat module hierarchy**: Each `fx*` package contains submodule files (`<category>_functions.py`)
2. **Dynamic re-export**: `auto_export()` in each `__init__.py` exposes all public functions at the package level
3. **Automatic discovery**: `registry.py` walks all `fx*` packages at runtime for JSON Schema generation and MCP tool exposure

```
formulite/
├── fxDate/
│   ├── __init__.py          # auto_export()
│   ├── date_operations.py
│   ├── date_evaluations.py
│   ├── date_convertions.py
│   └── date_sys.py
├── fxNumeric/
│   ├── __init__.py
│   ├── arithmetic_functions.py
│   ├── finance_functions.py
│   └── ... (29 submodules)
└── ...
```

## Importing Functions

You can import at different levels:

```python
# Package-level (recommended for quick use)
from formulite import fxDate
result = fxDate.add_time_to_date(...)

# Submodule-level (explicit, recommended for large projects)
from formulite.fxDate import date_operations
result = date_operations.add_time_to_date(...)

# Direct function import
from formulite.fxDate.date_operations import add_time_to_date
result = add_time_to_date(...)
```
