# FormuLite

**FormuLite** is a Python library designed to encapsulate complex programming logic into reusable "mini-programs," similar to spreadsheet formulas like Excel. Our goal is to help you write less code, do more, and keep your projects organized and readable.

> _"Write less, do more."_

## 🌟 What is FormuLite?

It is a library that provides high-level functions (Excel-style) to perform common operations easily and simply. It simplifies tasks that in standard Python would require:

1. Several lines of repetitive code.
2. Complex coding using loops.
3. Importing multiple libraries and using advanced patterns.

FormuLite follows the philosophy of simplicity and efficiency: **do one thing and do it well**.

## 🚀 Why FormuLite?

Have you ever wished for the simplicity and power of an Excel formula to execute snippets of Python logic? FormuLite allows you to define and reuse "formulas" with a clean syntax.

### Key Benefits

- **Minimizes Repetitive Code**: Encapsulates frequent code blocks into ready-to-use functions.
- **Improves Readability**: Uses descriptive and meaningful names (`fxDate`, `fxString`, `fxExcel`, etc.), making your code intuitive.
- **Efficient Abstraction**: Hides the internal complexity of processes, presenting only what is essential.
- **Facilitates Reusability**: Modular functions ready to be used anywhere in your application.

## 📦 Main Modules

FormuLite is organized into thematic modules to cover all your needs:

- **fxExcel**: Exact replicas of Excel formulas (VLOOKUP, PMT, CONCATENATE, etc.).
- **fxDate**: Date operations and evaluations.
- **fxNumeric**: Financial, statistical, and mathematical calculations.
- **fxString**: Advanced text manipulation and validations.
- **fxVBA**: VBA/Access compatible functions.
- **fxPython**: Utilities for iterables and Pythonic logic.

## 🛠️ Installation

You can install FormuLite using pip:

```bash
pip install formulite
```

## 📖 Usage

### 🖥️ Excel-style Functions (`fxExcel`)
[View full documentation](docs/api/fxExcel.md)

The `fxExcel` module exposes functions with names and behaviors identical to those in Excel.

```python
from formulite import fxExcel

# VLOOKUP Example
table = [
    ["Name", "Age", "City"],
    ["Ana", 25, "Madrid"],
    ["Juan", 30, "Barcelona"]
]

# Find the age (column 2) of "Ana"
age = fxExcel.VLOOKUP("Ana", table, 2)  # Result: 25

# Concatenate text
greeting = fxExcel.CONCATENATE("Hello", " ", "World")  # Result: "Hello World"
```

### 📅 Date Manipulation (`fxDate`)
[View full documentation](docs/api/fxDate.md)

Perform date calculations, validations, and arithmetic intuitively.

```python
from datetime import datetime
from formulite.fxDate import date_operations

# Add days to a date
start_date = datetime(2025, 1, 15)
new_date = date_operations.add_time_to_date(start_date, 30, 'days')

# Validate a date (February 30th does not exist)
is_valid = date_operations.is_valid_date("2025-02-30")  # Result: False
```

### 🔡 String Manipulation (`fxString`)
[View full documentation](docs/api/fxString.md)

Advanced tools for string search, cleaning, and analysis.

```python
from formulite.fxString import string_operations

# Find substring positions
text = "Programming is fun, programming is great"
positions = string_operations.position_in_string(text, "is")
# Result: [13, 36] (returns all occurrences)
```

### 🧮 Numeric and Financial Operations (`fxNumeric`)
[View full documentation](docs/api/fxNumeric.md)

Precise financial, statistical, and mathematical calculations.

```python
from formulite.fxNumeric import numeric_finance

# Calculate Future Value (FV)
# Rate: 5%, Periods: 10, Payment: -100, Present Value: -1000
fv = numeric_finance.future_value(rate=0.05, nper=10, pmt=-100, pv=-1000)
# Result: 1276.28...
```

### 🐍 Python Utilities (`fxPython`)
[View full documentation](docs/api/fxPython.md)

Common design patterns and tools for iterables.

```python
from formulite.fxPython import py_tools, py_itertools

# Create dictionary from parallel lists
dictionary = py_tools.create_key_value_dictionary("id,name", (1, "Alice"))
# Result: {'id': 1, 'name': 'Alice'}

# Take the first N items from any iterable
first_items = py_itertools.take(3, range(10))
# Result: [0, 1, 2]
```

### 🏗️ VBA Compatibility (`fxVBA`)
[View full documentation](docs/api/fxVBA.md)

If you come from the world of Excel or Access macros, you will feel immediately familiar.

```python
from formulite import fxVBA

text = "Hello World"

# Get left characters (Left)
start = fxVBA.Left(text, 5)  # Result: "Hello"

# Find text position (InStr is 1-based, like in VBA)
position = fxVBA.InStr(1, text, "World")  # Result: 7
```

## 📄 License

This project is licensed under the [MIT](LICENSE) license.
