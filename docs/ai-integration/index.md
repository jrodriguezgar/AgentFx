# AI Integration

FormuLite is designed as a **deterministic tool layer for AI agents**. LLMs are great at reasoning but can produce inconsistent results for calculations, date arithmetic, or string transformations. FormuLite provides tested, reliable functions that always return the same output for the same input.

## Two Discovery Methods

| Method | Best For | How It Works |
|--------|----------|--------------|
| **[MCP Server](mcp.md)** | AI agents with tool-calling (Claude, GPT, etc.) | A live server exposing search + execute meta-tools over the Model Context Protocol |
| **[`llms.txt`](llms-txt.md)** | LLMs with file access (Copilot, Cursor, etc.) | A static index of all functions with signatures and descriptions |

## Why Dynamic Tool Definition?

FormuLite exposes **3,000+ functions** — far too many to register each as an individual MCP tool. Instead, the MCP server uses a **dynamic discovery pattern** with a small set of meta-tools:

| Meta-Tool | Purpose |
|-----------|---------|
| `search_formulite_tools` | Find functions by natural-language query |
| `list_formulite_tools` | Browse all functions, optionally filtered by module |
| `get_formulite_tool_details` | Get full parameter schema for a specific function |
| `call_formulite` | Execute any function by its qualified name |
| `scientific_calculate` | Evaluate math expressions (AST-based, no eval) |

## Recommended AI Workflow

```
1. SEARCH   → search_formulite_tools("calculate days between two dates")
2. INSPECT  → get_formulite_tool_details("fxDate.date_operations.calculate_days_between_dates")
3. EXECUTE  → call_formulite("fxDate.date_operations.calculate_days_between_dates",
                             '{"start_date": "2025-01-01", "end_date": "2025-12-31"}')
```
