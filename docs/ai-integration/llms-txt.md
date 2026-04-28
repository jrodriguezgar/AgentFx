# llms.txt

`llms.txt` is a machine-readable function catalogue placed at the project root, designed for LLMs with file access (GitHub Copilot, Cursor, etc.).

## Purpose

Instead of requiring a running MCP server, `llms.txt` provides a **static index** of all shortfx functions with their signatures and descriptions. An LLM can read this file and perform text search to find the right function.

## Format

```text
# shortfx - Function Catalogue for LLMs

> shortfx: 2,932 functions across 6 modules.

## fxDate.date_operations
- add_time_to_date(date, amount, unit) → Add a specified amount of time to a date
- calculate_days_between_dates(start_date, end_date) → Calculate days between two dates
...
```

Each entry follows:

```
- function_name(parameters) → Short description
```

## Usage by AI Agents

1. The LLM reads `llms.txt` from the project root
2. Searches for relevant function names by keyword
3. Imports and calls the function directly in Python code

## Keeping It Updated

`llms.txt` is updated whenever public functions are added, removed, or renamed. The file is generated from the `registry.py` introspection and should always match the current API surface.
