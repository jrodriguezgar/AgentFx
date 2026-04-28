# shortfx MCP Server

> Expose a big library of shortfx functions as tools for AI agents via the Model Context Protocol.

## Overview

The shortfx MCP server allows AI agents to **discover, search, and execute** any shortfx function through a standardized protocol. Instead of writing Python code, an agent can call `call_shortfx("fxExcel.math_formulas.ABS", '{"number": -5.5}')` and get the result directly.

### What is MCP?

[Model Context Protocol (MCP)](https://modelcontextprotocol.io/) is an open standard that enables AI models to interact with external tools and data sources. shortfx implements an MCP server that exposes 4 meta-tools which give agents access to the entire library.

### Why Dynamic Tool Definition?

shortfx contains **2700+ functions** — registering each one as an individual MCP tool would:

- **Overwhelm the context window**: Most LLMs have limited tool-description space; listing 2700 tools with full schemas would consume all available context.
- **Degrade selection accuracy**: The more tools presented at once, the harder it is for an AI to choose the right one.
- **Become stale quickly**: As new functions are added, a static tool list would need constant redeployment.

Instead, shortfx uses a **dynamic discovery pattern**: the MCP server registers only a handful of meta-tools (`search_shortfx_tools`, `list_shortfx_tools`, `get_shortfx_tool_details`, `call_shortfx`, `scientific_calculate`, etc.), and the AI agent uses them to discover, inspect, and invoke any of the 2700+ underlying functions at runtime.

This means:
- **No tool list explosion**: The AI sees ~7 tools, not 2700.
- **Always up-to-date**: New functions are automatically discoverable after a server restart.
- **Semantic search**: The agent can describe what it needs in natural language and get the best-matching functions back.
- **Deterministic execution**: Calculations are performed by tested Python code, not by LLM inference — guaranteeing correct, reproducible results.

## Module Structure

| File | Description |
|------|-------------|
| `server.py` | MCP server with 4 tools: list, search, details, and execute |
| `mcp.json` | Configuration template for MCP clients (VS Code, Claude, Cursor) |
| `__init__.py` | Package init, re-exports `main` and `mcp` |
| `__main__.py` | Entry point for `python -m shortfx.mcp` |
| [`examples/example_mcp_client.py`](../../examples/example_mcp_client.py) | Working example of a Python client connecting to the server |

## Installation

```bash
pip install shortfx[mcp]
```

With semantic search (AI-powered function discovery):

```bash
pip install shortfx[mcp-semantic]
```

Or install dependencies manually:

```bash
pip install "mcp[cli]>=1.0.0"           # MCP only
pip install "mcp[cli]>=1.0.0" fastembed  # MCP + semantic search
```

## Quick Start

### 1. Start the server

```bash
# Using the entry point
shortfx-mcp

# Or using Python module
python -m shortfx.mcp
```

### 2. Configure your AI client

Add this to your MCP client configuration:

**Claude Desktop** (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "shortfx": {
      "command": "python",
      "args": ["-m", "shortfx.mcp"]
    }
  }
}
```

**VS Code** (`.vscode/mcp.json`):

```json
{
  "servers": {
    "shortfx": {
      "command": "python",
      "args": ["-m", "shortfx.mcp"]
    }
  }
}
```

**Cursor** (`~/.cursor/mcp.json`):

```json
{
  "mcpServers": {
    "shortfx": {
      "command": "python",
      "args": ["-m", "shortfx.mcp"]
    }
  }
}
```

### 3. Use from an AI agent

Once configured, an agent can interact with shortfx using natural language. For example:

> **User**: "Calculate the future value of $1000 invested at 5% for 10 years"
>
> **Agent** (internally calls):
>
> ```
> call_shortfx("fxNumeric.finance_functions.future_value",
>                '{"rate": 0.05, "nper": 10, "pmt": 0, "pv": -1000}')
> ```
>
> **Agent**: "The future value is $1,628.89"

## Available MCP Tools

The server exposes 4 tools that together provide full access to shortfx:

### `list_shortfx_tools`

List all available functions, optionally filtered by module.

**Parameters:**

| Parameter  | Type   | Required | Description                                                                                        |
| ---------- | ------ | -------- | -------------------------------------------------------------------------------------------------- |
| `module` | string | No       | Module prefix filter:`fxDate`, `fxNumeric`, `fxString`, `fxPython`, `fxExcel`, `fxVBA` |

**Example:**

```python
# List all date functions
list_shortfx_tools("fxDate")

# List only Excel math functions
list_shortfx_tools("fxExcel.math_formulas")

# List everything
list_shortfx_tools()
```

**Returns:** JSON array of `{"name": "...", "description": "..."}` objects.

---

### `search_shortfx_tools`

Search functions using natural language. Uses **semantic vector search** to match
by intent — not just exact keywords. Requires `fastembed` (`pip install shortfx[mcp-semantic]`).

**Parameters:**

| Parameter | Type   | Required | Description                                              |
| --------- | ------ | -------- | -------------------------------------------------------- |
| `query` | string | Yes      | Natural language query or keyword (e.g. `"round a number"`) |

**Example:**

```python
# Semantic search (finds functions by intent)
search_shortfx_tools("round a number to 2 decimals")     # → ROUND, round_to_n_decimals
search_shortfx_tools("find a value in a table")          # → VLOOKUP, HLOOKUP, XLOOKUP
search_shortfx_tools("how many days between two dates")  # → calculate_days_between_dates, DAYS
search_shortfx_tools("calculate compound interest")      # → future_value, present_value, nper

# Also works with simple keywords
search_shortfx_tools("round")
search_shortfx_tools("vlookup")
```

**Returns:** JSON array with name, description, and full parameter schema for each match, sorted by relevance.

---

### `get_shortfx_tool_details`

Get the complete schema of a specific function, including all parameters with types and descriptions.

**Parameters:**

| Parameter     | Type   | Required | Description                                         |
| ------------- | ------ | -------- | --------------------------------------------------- |
| `tool_name` | string | Yes      | Full tool name (e.g.,`fxExcel.math_formulas.ABS`) |

**Example:**

```python
get_shortfx_tool_details("fxExcel.lookup_formulas.VLOOKUP")
```

**Returns:**

```json
{
  "name": "fxExcel.lookup_formulas.VLOOKUP",
  "description": "Vertical lookup in a table.",
  "parameters": {
    "type": "object",
    "properties": {
      "lookup_value": {"description": "The value to search for."},
      "table_array": {"type": "array", "description": "The table to search."},
      "col_index_num": {"type": "integer", "description": "Column index to return."},
      "range_lookup": {"type": "boolean", "default": true}
    },
    "required": ["lookup_value", "table_array", "col_index_num"]
  }
}
```

---

### `call_shortfx`

Execute any shortfx function by name.

**Parameters:**

| Parameter     | Type   | Required | Description                                 |
| ------------- | ------ | -------- | ------------------------------------------- |
| `tool_name` | string | Yes      | Full tool name                              |
| `arguments` | string | No       | JSON string of arguments (default:`"{}"`) |

**Example:**

```python
# Math
call_shortfx("fxExcel.math_formulas.ABS", '{"number": -5.5}')
# → {"result": 5.5}

# String manipulation
call_shortfx("fxString.string_operations.reverse_string", '{"input_string": "hello"}')
# → {"result": "olleh"}

# Financial calculation
call_shortfx("fxNumeric.finance_functions.future_value",
               '{"rate": 0.05, "nper": 10, "pmt": -100, "pv": -1000}')
# → {"result": 1628.89}

# Date validation
call_shortfx("fxDate.date_operations.is_valid_date", '{"date_input": "2025-02-30"}')
# → {"result": false}

# VBA compatibility
call_shortfx("fxVBA.string_functions.Left", '{"string": "Hello World", "length": 5}')
# → {"result": "Hello"}
```

**Returns:** `{"result": <value>}` on success, `{"error": "<message>"}` on failure.

## Tool Name Convention

Tool names follow the pattern: `<module>.<file>.<function>`

```
fxExcel.math_formulas.ABS
───────┬──────────── ───
   │        │        └── Function name
   │        └── Source file (without .py)
   └── Module name
```

### Available Modules

| Module        | Functions | Description                                           |
| ------------- | --------- | ----------------------------------------------------- |
| `fxDate`    | ~110      | Date/time operations, conversions, evaluations        |
| `fxNumeric` | ~120      | Arithmetic, finance, statistics, trigonometry         |
| `fxString`  | ~150      | Text manipulation, formatting, validation, similarity |
| `fxPython`  | ~70       | Collection utilities, itertools, logic operations     |
| `fxExcel`   | ~230      | Excel-compatible formulas (VLOOKUP, SUM, IF, etc.)    |
| `fxVBA`     | ~150      | VBA/Access-compatible functions                       |

## Programmatic Client Example

See [example_mcp_client.py](../../examples/example_mcp_client.py) for a complete working example.

```python
import asyncio
import json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main():
    server = StdioServerParameters(command="python", args=["-m", "shortfx.mcp"])

    async with stdio_client(server) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # Search for rounding functions
            result = await session.call_tool(
                "search_shortfx_tools",
                arguments={"query": "round"},
            )
            print(json.loads(result.content[0].text))

            # Execute ABS(-5.5)
            result = await session.call_tool(
                "call_shortfx",
                arguments={
                    "tool_name": "fxExcel.math_formulas.ABS",
                    "arguments": '{"number": -5.5}',
                },
            )
            print(json.loads(result.content[0].text))  # {"result": 5.5}


asyncio.run(main())
```

## Typical Agent Workflow

An AI agent typically follows this pattern when using shortfx MCP:

```
1. User asks: "What is the standard deviation of [4, 8, 15, 16, 23, 42]?"

2. Agent calls: search_shortfx_tools("standard deviation")
   → Finds: fxNumeric.statistics_functions.calculate_standard_deviation

3. Agent calls: get_shortfx_tool_details("fxNumeric.statistics_functions.calculate_standard_deviation")
   → Gets parameter schema: data (array), sample (boolean, default true)

4. Agent calls: call_shortfx("fxNumeric.statistics_functions.calculate_standard_deviation",
                               '{"data": [4, 8, 15, 16, 23, 42]}')
   → Returns: {"result": 13.284...}

5. Agent responds: "The standard deviation is approximately 13.28"
```

## Semantic Search

When installed with `pip install shortfx[mcp-semantic]`, the `search_shortfx_tools`
tool uses **AI-powered vector search**.

### How It Works

1. **Server startup**: The embedding model is loaded and all tool schemas are embedded
   into vectors via `warm_up_semantic_search()`. This happens once at startup so the
   first search query is instant.
2. **Query time**: The search query is embedded and compared via cosine similarity
   against all pre-computed tool embeddings.
3. **Results**: Tools are returned sorted by semantic relevance, with a configurable
   similarity threshold (default: 0.3).

### Benefits Over Keyword Search

| Scenario | Keyword Search | Semantic Search |
|----------|---------------|------------------|
| `"round a number"` | Matches only if "round" appears literally | Finds `ROUND`, `MROUND`, `round_to_n_decimals` |
| `"find a value in a table"` | No match (no keyword overlap) | Finds `VLOOKUP`, `HLOOKUP`, `XLOOKUP` |
| `"how many days between dates"` | Partial match at best | Finds `calculate_days_between_dates`, `DAYS` |
| `"calculate compound interest"` | Only if "compound" or "interest" in description | Finds `future_value`, `present_value`, `compound_interest` |

### First Run

The embedding model (`BAAI/bge-small-en-v1.5`, ~66 MB ONNX) is downloaded from
HuggingFace on first server start and cached locally in `$TEMP/fastembed_cache`.
Subsequent startups reuse the cached model. The index is built during
`warm_up_semantic_search()` at server startup — all queries after that are instant.
On corporate networks with SSL interception, `truststore` is used automatically to
resolve certificate issues.

## Troubleshooting

| Issue                                          | Solution                                                                                                  |
| ---------------------------------------------- | --------------------------------------------------------------------------------------------------------- |
| `ModuleNotFoundError: No module named 'mcp'` | Run `pip install shortfx[mcp]`                                                                        |
| Semantic search not activating                 | Run `pip install shortfx[mcp-semantic]` to install `fastembed`                                        |
| SSL error downloading embedding model          | Install `truststore` (`pip install truststore`) or set `SSL_CERT_FILE` env var                          |
| Some functions missing from listing            | Optional dependencies not installed (`mpmath`, `scipy`, `rapidfuzz`). The server loads what it can. |
| `Tool 'xxx' not found`                       | Use `search_shortfx_tools` or `list_shortfx_tools` to find the correct tool name                  |
| Connection refused / timeout                   | Verify the server starts correctly with `python -m shortfx.mcp`                                       |
