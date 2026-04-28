# Getting Started

## Installation

=== "pip"

    ```bash
    pip install agentfx
    ```

=== "uv"

    ```bash
    uv add agentfx
    ```

### Optional Dependencies

| Extra | Command | Purpose |
|-------|---------|---------|
| `mcp` | `pip install agentfx[mcp]` | MCP server for AI agents |
| `semantic` | `pip install agentfx[semantic]` | Semantic search via fastembed |
| `mcp-semantic` | `pip install agentfx[mcp-semantic]` | MCP + semantic search |
| `scipy` | `pip install agentfx[scipy]` | SciPy-backed statistical functions |
| `similarity` | `pip install agentfx[similarity]` | Advanced string similarity |
| `all` | `pip install agentfx[all]` | Everything |

## Basic Usage

### Date Manipulation

```python
from datetime import datetime
from agentfx.fxDate import date_operations

# Add days to a date
start_date = datetime(2025, 1, 15)
new_date = date_operations.add_time_to_date(start_date, 30, "days")

# Validate a date (February 30th does not exist)
is_valid = date_operations.is_valid_date("2025-02-30")  # False
```

### Numeric & Financial Operations

```python
from agentfx.fxNumeric import finance_functions

# Calculate Future Value (FV)
fv = finance_functions.future_value(rate=0.05, nper=10, pmt=-100, pv=-1000)
```

### String Manipulation

```python
from agentfx.fxString import string_operations

# Find substring positions
text = "Programming is fun, programming is great"
positions = string_operations.position_in_string(text, "is")
# [13, 36] (returns all occurrences)
```

### Python Utilities

```python
from agentfx.fxPython import py_tools, py_itertools

# Create dictionary from parallel lists
dictionary = py_tools.create_key_value_dictionary("id,name", (1, "Alice"))

# Take the first N items from any iterable
first_items = py_itertools.take(3, range(10))  # [0, 1, 2]
```

### Excel-Style Functions

```python
from agentfx import fxExcel

table = [
    ["Name", "Age", "City"],
    ["Ana", 25, "Madrid"],
    ["Juan", 30, "Barcelona"],
]

age = fxExcel.VLOOKUP("Ana", table, 2)      # 25
greeting = fxExcel.CONCATENATE("Hello", " ", "World")  # "Hello World"
```

### VBA Compatibility

```python
from agentfx import fxVBA

text = "Hello World"
start = fxVBA.Left(text, 5)           # "Hello"
position = fxVBA.InStr(1, text, "World")  # 7 (1-based, like VBA)
```

## Next Steps

- **[Browse all modules](modules/index.md)** — Explore the 6 module families
- **[AI integration](ai-integration/index.md)** — Set up MCP server or use `llms.txt`
- **[API Reference](reference/index.md)** — Full auto-generated documentation from docstrings
