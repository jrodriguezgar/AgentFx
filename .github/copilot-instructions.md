# GitHub Copilot Instructions - shortfx

## Project Description

shortfx is a Python library that encapsulates complex programming logic into 3000+ reusable functions, organized like Excel formulas. It also serves as a **deterministic toolset for AI agents** via `llms.txt` and a built-in MCP server, enabling LLMs to discover and invoke functions for reliable, reproducible calculations.

---

## Tech Stack

- **Language**: Python ≥ 3.10
- **Package Manager**: uv (preferred), pip
- **Build System**: Hatchling (`hatchling.build`)
- **Test Framework**: pytest
- **Optional deps**: `mcp[cli]` (MCP server), `fastembed` + `truststore` (semantic search)

---

## Code Conventions

> Language style defined in [`python-development.instructions.md`](.github/instructions/python-development.instructions.md) (auto-applied to `**/*.py`).
> Testing rules defined in [`unit-tests.instructions.md`](.github/instructions/testing/unit-tests.instructions.md) (auto-applied to `**/tests/**`).
> Documentation & versioning rules defined in [`docs-changelog-sync.instructions.md`](.github/instructions/docs-changelog-sync.instructions.md) (auto-applied to docs & config files).

### Project-Specific Overrides

- **Documentation language**: English
- **No external runtime deps**: core library uses only the Python standard library — never add `numpy`, `pandas`, etc. as required dependencies
- **File naming**: `snake_case.py` — function files follow `<category>_functions.py` or `<category>_<subcategory>.py`

---

## Design Patterns

### Architecture

Flat module hierarchy: 6 top-level `fx*` packages → submodule files → public functions. `auto_export()` dynamically re-exports all public callables from submodules. `registry.py` walks `fx*` packages at runtime for JSON Schema generation and MCP tool exposure.

### Key Patterns Used

- **Dynamic Re-export** (`_loader.auto_export`): Each `fx*/__init__.py` calls `auto_export()` to expose all public functions at the package level — no manual imports needed
- **⚠️ Shadowing risk**: `auto_export()` iterates `_SUBMODULES` in order — if two submodules define a function with the **same name**, the last submodule in the list wins and silently shadows the earlier one. This applies **across the entire `fx*` package**, not just within a single file. Always verify uniqueness before adding a function (see Best Practices #1)
- **Automatic Discovery** (`registry.py`): Walks `fx*` packages at runtime, introspects signatures, and builds OpenAI-compatible JSON Schemas for every public function
- **Dynamic MCP Meta-tools** (`mcp/server.py`): Instead of registering 3000+ individual tools, exposes 6 meta-tools (search → inspect → execute) to keep the AI context window manageable

### Base Classes / Interfaces

- `_loader.auto_export()` (`shortfx/_loader.py`): Central import machinery — all `fx*` packages depend on it
- `_validators` (`shortfx/_validators.py`): Shared input validation (`ensure_type`, `ensure_numeric`, `ensure_positive`, etc.)
- `registry` (`shortfx/registry.py`): Tool discovery, schema generation, and invocation dispatcher
- `SemanticToolSearch` (`shortfx/semantic_search.py`): Vector-based function discovery via fastembed embeddings

---

## Key Abstractions

### Core Modules

| Module | Purpose |
| ------ | ------- |
| `fxDate` | Date operations, evaluations, conversions, system dates |
| `fxNumeric` | Finance, statistics, geometry, transforms, series, number theory, 30+ submodules |
| `fxString` | Text manipulation, regex, hashing, validation, encoding, similarity, Spanish NLP |
| `fxPython` | Iterable utilities, type conversions, logic helpers |
| `fxExcel` | Excel-compatible formulas (VLOOKUP, PMT, CONCATENATE, etc.) |
| `fxVBA` | VBA/Access-compatible functions (Left, InStr, Format, etc.) |

### Important Functions

| Function | Location | Purpose |
| -------- | -------- | ------- |
| `auto_export()` | `shortfx/_loader.py` | Dynamic re-export of submodule callables |
| `get_tool_schemas()` | `shortfx/registry.py` | Build JSON Schemas for all functions |
| `invoke_tool()` | `shortfx/registry.py` | Execute any function by qualified name |
| `search_tools()` | `shortfx/registry.py` | Keyword/semantic search across the function catalogue |
| `call_shortfx()` | `shortfx/mcp/server.py` | MCP tool: execute any function with JSON args |
| `search_shortfx_tools()` | `shortfx/mcp/server.py` | MCP tool: natural-language function discovery |

---

## Configuration

### Configuration Files

- `pyproject.toml`: Project metadata, dependencies, build config, entry points
- `shortfx/mcp/mcp.json`: MCP client configuration template

### Priority Resolution

1. Direct function arguments
2. Module-level defaults
3. No config files or environment variables (pure library)

---

## Security Guidelines

- **No `eval()`/`exec()`**: The `scientific_calculate` tool uses AST-based expression parsing — never raw `eval`
- **No external network calls**: Core library is fully offline — only `fastembed` (optional) downloads a model at first use
- **NEVER**: Hardcode secrets, API keys, or credentials anywhere in source

---

## Error Handling

> Base rules in [`python-development.instructions.md`](.github/instructions/python-development.instructions.md).

### Project-Specific

- Use shared validators from `shortfx/_validators.py` (`ensure_type`, `ensure_numeric`, `ensure_positive`) — do not write ad-hoc `isinstance` checks
- All functions must raise `TypeError` / `ValueError` with descriptive messages for invalid inputs
- MCP server catches all exceptions and returns structured error JSON — never let exceptions crash the server

---

## Best Practices for Copilot

1. **When creating a new function**: Place it in the correct `fx*/<category>_functions.py` file. Use `_validators` for input checks. Follow the docstring format (Google style with `Args`, `Returns`, `Raises`, `Example`, `Complexity`). **Before committing the name**, search ALL other submodules in the same `fx*` package for an existing function with the same name — `auto_export()` will silently shadow it. Quick check: `grep -rn "^def func_name(" shortfx/fxPackage/`
2. **When creating a new file in an existing module**: Add the file name to the module's `__init__.py` `_SUBMODULES` list — `auto_export()` handles the rest
3. **When adding a new module**: Create `fx<Name>/` with `__init__.py` calling `auto_export()`, add submodule files, and update `README.md`
4. **When updating docs**: Always update `CHANGELOG.md`, module `README.md`, and `llms.txt` in the same step as code changes
5. **When writing tests**: One test file per source module under `tests/`, use `pytest.approx` for floats, `pytest.mark.parametrize` for data-driven tests

---

## Common Patterns

### Adding a Function

```python
# shortfx/fxNumeric/arithmetic_functions.py

from shortfx._validators import ensure_numeric


def cube_root(x: float) -> float:
    """Calculate the cube root of a number.

    Args:
        x: The number to compute the cube root for.

    Returns:
        The cube root of x.

    Raises:
        TypeError: If x is not numeric.

    Example:
        >>> cube_root(27)
        3.0

    Complexity: O(1)
    """
    ensure_numeric(x, "x")
    return x ** (1 / 3) if x >= 0 else -((-x) ** (1 / 3))
```

### Registering a New File

```python
# shortfx/fxNumeric/__init__.py
from shortfx._loader import auto_export

_SUBMODULES = [
    "arithmetic_functions",
    "new_file_functions",   # ← just add the name here
]

auto_export(__name__, _SUBMODULES, globals())
```

---

## Git Workflow

- **Branch naming**: `feature/*`, `bugfix/*`, `hotfix/*`
- **Commit format**: Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`)
- **Version**: Single source of truth in `pyproject.toml` → `[project] version`

---

## Checklist

When generating code, ensure:

- [ ] Function has full Google-style docstring with `Args`, `Returns`, `Raises`, `Example`, `Complexity`
- [ ] Input validation uses `shortfx/_validators.py` helpers
- [ ] No external runtime dependencies added to core
- [ ] No secrets or credentials hardcoded in source
- [ ] Tests added/updated under `tests/`
- [ ] `CHANGELOG.md` updated under `## [Unreleased]`
- [ ] Module `README.md` and `llms.txt` updated if public API changed
- [ ] No `eval()`, `exec()`, or `subprocess` in function code
- [ ] No name collision with existing functions in the same `fx*` package (shadowing check via `grep -rn "^def <name>(" shortfx/fx*/`)

## Response Quality

- **Token-efficient** → Tables > prose, bullets > paragraphs, symbols (→ ✓ ❌) > words
- **Minimal tokens** → Maximize information density; eliminate filler words, redundant phrases, and unnecessary qualifiers without losing meaning
