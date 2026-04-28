# AgentFx

[![CI](https://github.com/jrodriguezgar/AgentFx/actions/workflows/ci.yml/badge.svg)](https://github.com/jrodriguezgar/AgentFx/actions/workflows/ci.yml)
[![PyPI version](https://img.shields.io/pypi/v/agentfx)](https://pypi.org/project/agentfx/)
[![PyPI downloads](https://img.shields.io/pypi/dm/agentfx)](https://pypi.org/project/agentfx/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue.svg)](https://www.python.org/)
[![Version](https://img.shields.io/badge/version-0.2.1-green.svg)](CHANGELOG.md)

> _"Write less, do more."_
> _"The deterministic toolset your AI agents can trust."_

**AgentFx** is a Python library designed to encapsulate complex programming logic into reusable "mini-programs," similar to spreadsheet formulas like Excel. Our goal is to help you write less code, do more, and keep your projects organized and readable.

---

### ✨ Highlights

| | |
|---|---|
| **3,000+ ready-to-use functions** | The largest open-source Python formula library — dates, math, finance, statistics, strings, Excel & VBA compatibility, and more |
| **AI-native via MCP** | Built-in [Model Context Protocol](agentfx/mcp/README.md) server lets AI agents (Claude, GPT, Copilot …) **discover, inspect, and execute** any function as a tool — no hallucinated calculations |
| **`llms.txt` included** | A machine-readable [function catalogue](llms.txt) so LLMs can look up signatures and descriptions without calling a server |
| **Zero dependencies** | Core library uses only the Python standard library — no NumPy, no Pandas |

---

## 🌟 What is AgentFx?

**The largest open-source Python formula library available.** With **2,932 ready-to-use functions** across 6 modules, AgentFx is the most comprehensive collection of reusable formulas for everyday operations:

| Module | Functions | Scope |
|--------|----------:|-------|
| `fxNumeric` | 1,602 | Finance, statistics, geometry, transforms, series, number theory |
| `fxExcel` | 489 | Excel-compatible formulas (VLOOKUP, PMT, CONCATENATE …) |
| `fxString` | 331 | Text manipulation, regex, hashing, validation, encoding, similarity |
| `fxDate` | 261 | Date operations, evaluations, conversions, system dates |
| `fxVBA` | 133 | VBA/Access-compatible functions (Left, InStr, Format …) |
| `fxPython` | 116 | Iterable utilities, type conversions, logic helpers |

It simplifies tasks that in standard Python would require:

1. Several lines of repetitive code.
2. Complex coding using loops.
3. Importing multiple libraries and using advanced patterns.

AgentFx follows the philosophy of simplicity and efficiency: **do one thing and do it well**.

## 🚀 Why AgentFx?

Have you ever wished for the simplicity and power of an Excel formula to execute snippets of Python logic? AgentFx allows you to define and reuse "formulas" with a clean syntax.

### Key Benefits

- **2,932 functions, zero dependencies**: The largest open-source formula library for Python — all powered by the standard library alone.
- **AI-Ready (LLMs & MCP)**: Every function is callable by AI agents via the built-in MCP server or `llms.txt`, guaranteeing **deterministic answers** — no hallucinated calculations.
- **Minimizes Repetitive Code**: Encapsulates frequent code blocks into ready-to-use functions.
- **Improves Readability**: Uses descriptive and meaningful names (`fxDate`, `fxString`, `fxExcel`, etc.), making your code intuitive.
- **Efficient Abstraction**: Hides the internal complexity of processes, presenting only what is essential.
- **Facilitates Reusability**: Modular functions ready to be used anywhere in your application.

## 📦 Main Modules

AgentFx is organized into thematic modules to cover all your needs:

- **fxDate**: Date operations and evaluations.
- **fxNumeric**: Financial, statistical, mathematical, geometry, special functions, series, transforms, and vector analysis.
- **fxString**: Advanced text manipulation and validations.
- **fxPython**: Utilities for iterables and Pythonic logic.
- **fxExcel**: Exact replicas of Excel formulas (VLOOKUP, PMT, CONCATENATE, etc.).
- **fxVBA**: VBA/Access compatible functions.

> 🔍 **Quality Data functions** (phonetic encoding, checksum validation, readability metrics) live in [ShadeTripTxt](https://github.com/jrodriguezgar/ShadeTripTxt). See the **[Quality Functions Guide](agentfx/fxString/quality_functions.md)** for details and examples.

## 🛠️ Installation

You can install AgentFx using pip:

```bash
pip install agentfx
```

## 📖 Usage

###  Date Manipulation (`fxDate`)
[View full documentation](agentfx/fxDate/README.md)

Perform date calculations, validations, and arithmetic intuitively.

```python
from datetime import datetime
from agentfx.fxDate import date_operations

# Add days to a date
start_date = datetime(2025, 1, 15)
new_date = date_operations.add_time_to_date(start_date, 30, 'days')

# Validate a date (February 30th does not exist)
is_valid = date_operations.is_valid_date("2025-02-30")  # Result: False
```

### 🧮 Numeric and Financial Operations (`fxNumeric`)
[View full documentation](agentfx/fxNumeric/README.md)

Precise financial, statistical, and mathematical calculations.

```python
from agentfx.fxNumeric import finance_functions

# Calculate Future Value (FV)
# Rate: 5%, Periods: 10, Payment: -100, Present Value: -1000
fv = finance_functions.future_value(rate=0.05, nper=10, pmt=-100, pv=-1000)
# Result: 1276.28...
```

### 🔡 String Manipulation (`fxString`)
[View full documentation](agentfx/fxString/README.md)

Advanced tools for string search, cleaning, and analysis.

```python
from agentfx.fxString import string_operations

# Find substring positions
text = "Programming is fun, programming is great"
positions = string_operations.position_in_string(text, "is")
# Result: [13, 36] (returns all occurrences)
```

### 🐍 Python Utilities (`fxPython`)
[View full documentation](agentfx/fxPython/README.md)

Common design patterns and tools for iterables.

```python
from agentfx.fxPython import py_tools, py_itertools

# Create dictionary from parallel lists
dictionary = py_tools.create_key_value_dictionary("id,name", (1, "Alice"))
# Result: {'id': 1, 'name': 'Alice'}

# Take the first N items from any iterable
first_items = py_itertools.take(3, range(10))
# Result: [0, 1, 2]
```

### 🖥️ Excel-style Functions (`fxExcel`)
[View full documentation](agentfx/fxExcel/README.md)

The `fxExcel` module exposes functions with names and behaviors identical to those in Excel.

```python
from agentfx import fxExcel

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

### 🏗️ VBA Compatibility (`fxVBA`)
[View full documentation](agentfx/fxVBA/README.md)

If you come from the world of Excel or Access macros, you will feel immediately familiar.

```python
from agentfx import fxVBA

text = "Hello World"

# Get left characters (Left)
start = fxVBA.Left(text, 5)  # Result: "Hello"

# Find text position (InStr is 1-based, like in VBA)
position = fxVBA.InStr(1, text, "World")  # Result: 7
```

## 🤖 AI Integration (LLMs & MCP)

AgentFx is designed to work as a **deterministic tool layer for AI agents**. Large language models are excellent at reasoning, but they can produce inconsistent or incorrect results when performing calculations, date arithmetic, or string transformations. AgentFx solves this by providing tested, reliable functions that always return the same output for the same input.

### Why Dynamic Tool Definition?

AgentFx exposes **2,932 functions**, far too many to register each one as an individual MCP tool (which would overwhelm any AI agent's context window). Instead, the MCP server uses a **dynamic discovery pattern** with a small set of meta-tools:

| Meta-Tool | Purpose |
|-----------|---------|
| `search_agentfx_tools` | Find functions by natural language query (semantic search) |
| `list_agentfx_tools` | Browse all functions, optionally filtered by module |
| `get_agentfx_tool_details` | Get full parameter schema for a specific function |
| `call_agentfx` | Execute any function by its qualified name |
| `scientific_calculate` | Evaluate math expressions directly (AST-based, no eval) |

### Recommended AI Workflow

```
1. SEARCH   → search_agentfx_tools("calculate days between two dates")
2. INSPECT  → get_agentfx_tool_details("fxDate.date_operations.calculate_days_between_dates")
3. EXECUTE  → call_agentfx("fxDate.date_operations.calculate_days_between_dates",
                             '{"start_date": "2025-01-01", "end_date": "2025-12-31"}')
```

### Two Ways AI Can Discover Functions

| Method | Best For | How It Works |
|--------|----------|--------------|
| **`llms.txt`** | LLMs with file access (Copilot, Cursor, etc.) | A static index of all 2,932 functions with signatures and descriptions. The AI reads it once and uses Ctrl+F-style lookup. |
| **MCP Server** | AI agents with tool-calling (Claude, GPT, etc.) | A live server that exposes search + execute meta-tools over the Model Context Protocol. |

### Setup

```bash
# Install with MCP support
pip install agentfx[mcp]

# With semantic search (recommended for AI agents)
pip install agentfx[mcp-semantic]
```

Configure your AI client (VS Code, Claude Desktop, Cursor) as described in the [MCP Server documentation](agentfx/mcp/README.md).

## 🔒 Security

| Measure | Detail |
|---------|--------|
| **No `eval()` / `exec()`** | Expression evaluators (`evaluate_expression`, `scientific_calculate`) use AST-based parsing with whitelisted operations only |
| **No OS command execution** | `subprocess` and OS shell access are not used anywhere in the library |
| **`apply_expression` sandboxed** | Attribute access restricted to built-in types; private attributes (`_`-prefixed) blocked |
| **DoS protection** | `factorial()` capped at n ≤ 170; exponents capped at ≤ 10,000; expression length capped at 1,000 chars |
| **No auto-install** | Missing optional dependencies are reported via logging — the library never installs packages |

## 🤝 Contributing

Want to add new formulas? Check the **[Contributing Guide](CONTRIBUTING.md)** for step-by-step instructions on how to:

- Add functions to existing modules
- Create new files or modules
- Follow the docstring, testing, and documentation conventions

## 📄 License

This project is licensed under the [MIT](LICENSE) license.

## 👤 Author

- **Javier Rodríguez** — [DatamanEdge](https://github.com/DatamanEdge)
- **Email**: [jrodriguezga@outlook.com](mailto:jrodriguezga@outlook.com)
- **LinkedIn**: [Javier Rodríguez](https://es.linkedin.com/in/javier-rodriguez-ga)
