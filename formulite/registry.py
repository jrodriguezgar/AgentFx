"""FormuLite function registry for AI agent integration.

Provides automatic discovery and JSON Schema generation for all FormuLite
functions. Enables AI agents to discover, describe, and invoke functions
via OpenAI function-calling format or MCP tool definitions.

Example:
    >>> from formulite.registry import get_tool_schemas, invoke_tool
    >>> schemas = get_tool_schemas()
    >>> result = invoke_tool("fxExcel.math_formulas.ABS", {"number": -5.5})
    >>> result
    5.5

Complexity: O(n) where n is total number of functions across all modules.
"""

import importlib
import inspect
import pkgutil
import re
from typing import Any, Callable, Optional

import formulite

# Python type → JSON Schema type mapping
_TYPE_MAP: dict[type, str] = {
    int: "integer",
    float: "number",
    str: "string",
    bool: "boolean",
    list: "array",
    dict: "object",
    type(None): "null",
}

# Modules to skip during discovery (not public API)
_SKIP_MODULES = {"data", "mcp", "__pycache__"}


def _python_type_to_json_schema(annotation: Any) -> dict[str, Any]:
    """Convert a Python type annotation to a JSON Schema fragment.

    Args:
        annotation: A Python type annotation from ``inspect.Parameter``.

    Returns:
        A JSON Schema dict (e.g. ``{"type": "number"}``).

    Complexity: O(1)
    """
    if annotation is inspect.Parameter.empty:
        return {}

    origin = getattr(annotation, "__origin__", None)

    # Handle Optional[X] → Union[X, None]
    if origin is type(None):
        return {"type": "null"}

    # Handle Union types (e.g. Union[int, float])
    args = getattr(annotation, "__args__", None)

    if origin is list or annotation is list:
        schema: dict[str, Any] = {"type": "array"}

        if args:
            schema["items"] = _python_type_to_json_schema(args[0])

        return schema

    if origin is dict or annotation is dict:
        return {"type": "object"}

    # Direct type match
    json_type = _TYPE_MAP.get(annotation)

    if json_type:
        return {"type": json_type}

    # Union[int, float] → number
    if args:
        real_args = [a for a in args if a is not type(None)]

        if real_args:
            return _python_type_to_json_schema(real_args[0])

    return {}


def _extract_param_descriptions(docstring: str) -> dict[str, str]:
    """Extract parameter descriptions from a Google-style docstring.

    Args:
        docstring: The full docstring text.

    Returns:
        Dict mapping parameter names to their description strings.

    Complexity: O(n) where n is the length of the docstring.
    """
    descriptions: dict[str, str] = {}

    if not docstring:
        return descriptions

    # Match lines like "        param_name (type): Description text"
    # or "        param_name: Description text"
    pattern = re.compile(
        r"^\s{4,}(\*?\w+)\s*(?:\([^)]*\))?\s*:\s*(.+)", re.MULTILINE
    )

    in_args = False

    for line in docstring.split("\n"):
        stripped = line.strip()

        if stripped.startswith("Args:"):
            in_args = True
            continue

        if in_args and stripped and not stripped[0].isspace() and ":" in stripped:
            # Check if it's a new section header (Returns:, Raises:, etc.)
            if stripped.endswith(":") and stripped[:-1].isalpha():
                in_args = False
                continue

        if in_args:
            match = pattern.match(line)

            if match:
                param_name = match.group(1).lstrip("*")
                param_desc = match.group(2).strip()
                descriptions[param_name] = param_desc

    return descriptions


def _build_function_schema(
    func: Callable, module_path: str
) -> dict[str, Any]:
    """Build an OpenAI-compatible function/tool schema for a single function.

    Args:
        func: The callable to introspect.
        module_path: Dotted path like ``fxExcel.math_formulas``.

    Returns:
        A dict with ``name``, ``description``, and ``parameters`` keys
        following the OpenAI function-calling schema format.

    Complexity: O(p) where p is the number of parameters.
    """
    sig = inspect.signature(func)
    docstring = inspect.getdoc(func) or ""
    first_line = docstring.split("\n")[0].strip() if docstring else ""
    param_docs = _extract_param_descriptions(docstring)

    properties: dict[str, Any] = {}
    required: list[str] = []

    for name, param in sig.parameters.items():

        if name in ("self", "cls"):
            continue

        prop = _python_type_to_json_schema(param.annotation)
        prop_desc = param_docs.get(name, "")

        if prop_desc:
            prop["description"] = prop_desc

        if param.default is not inspect.Parameter.empty:
            prop["default"] = param.default
        elif param.kind != inspect.Parameter.VAR_POSITIONAL:
            required.append(name)

        # VAR_POSITIONAL (*args) → array
        if param.kind == inspect.Parameter.VAR_POSITIONAL:
            prop = {"type": "array", "description": prop_desc or f"Variable arguments: {name}"}

        properties[name] = prop

    tool_name = f"{module_path}.{func.__name__}"

    return {
        "name": tool_name,
        "description": first_line,
        "parameters": {
            "type": "object",
            "properties": properties,
            "required": required,
        },
    }


def _discover_modules() -> list[tuple[str, Any]]:
    """Discover all FormuLite submodules containing public functions.

    Returns:
        List of ``(dotted_path, module_object)`` tuples.

    Complexity: O(m) where m is the number of submodules.
    """
    modules: list[tuple[str, Any]] = []

    for pkg_info in pkgutil.iter_modules(formulite.__path__):

        if not pkg_info.ispkg or pkg_info.name in _SKIP_MODULES:
            continue

        subpkg_name = f"formulite.{pkg_info.name}"

        try:
            subpkg = importlib.import_module(subpkg_name)
        except ImportError:
            continue

        for mod_info in pkgutil.iter_modules(subpkg.__path__):

            if mod_info.name.startswith("_"):
                continue

            full_name = f"{subpkg_name}.{mod_info.name}"

            try:
                mod = importlib.import_module(full_name)
                # Store as short path: fxExcel.math_formulas
                short_path = f"{pkg_info.name}.{mod_info.name}"
                modules.append((short_path, mod))
            except ImportError:
                pass

    return modules


def _get_public_functions(module: Any) -> list[tuple[str, Callable]]:
    """Get all public callable functions from a module.

    Args:
        module: The imported module object.

    Returns:
        List of (function_name, function_object) tuples.

    Complexity: O(n) where n is the number of module attributes.
    """
    functions: list[tuple[str, Callable]] = []

    for name in dir(module):

        if name.startswith("_"):
            continue

        obj = getattr(module, name)

        if callable(obj) and inspect.isfunction(obj) and obj.__module__ == module.__name__:
            functions.append((name, obj))

    return functions


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

_CACHE: dict[str, dict[str, Any]] | None = None


def _build_registry() -> dict[str, dict[str, Any]]:
    """Build the full registry mapping tool names → (schema, callable).

    Returns:
        Dict mapping tool names to ``{"schema": ..., "callable": ...}``.

    Complexity: O(m * f) where m=modules, f=avg functions per module.
    """
    global _CACHE

    if _CACHE is not None:
        return _CACHE

    registry: dict[str, dict[str, Any]] = {}

    for module_path, module in _discover_modules():

        for func_name, func in _get_public_functions(module):
            schema = _build_function_schema(func, module_path)
            registry[schema["name"]] = {
                "schema": schema,
                "callable": func,
            }

    _CACHE = registry
    return registry


def get_tool_schemas(
    module_filter: Optional[str] = None,
) -> list[dict[str, Any]]:
    """Get OpenAI function-calling compatible tool schemas.

    Args:
        module_filter: Optional prefix to filter (e.g. ``"fxExcel"``).
            Only tools whose name starts with this prefix are returned.

    Returns:
        List of tool schema dicts with ``name``, ``description``,
        and ``parameters`` keys.

    Example:
        >>> schemas = get_tool_schemas("fxExcel.math")
        >>> schemas[0]["name"]
        'fxExcel.math_formulas.ABS'

    Complexity: O(n) where n is the total number of registered tools.
    """
    registry = _build_registry()

    if module_filter:
        return [
            entry["schema"]
            for name, entry in registry.items()
            if name.startswith(module_filter)
        ]

    return [entry["schema"] for entry in registry.values()]


def get_tool_names(module_filter: Optional[str] = None) -> list[str]:
    """Get a list of all available tool names.

    Args:
        module_filter: Optional prefix to filter (e.g. ``"fxDate"``).

    Returns:
        Sorted list of tool name strings.

    Example:
        >>> names = get_tool_names("fxDate")
        >>> "fxDate.date_operations.add_time_to_date" in names
        True

    Complexity: O(n log n) due to sorting.
    """
    registry = _build_registry()

    if module_filter:
        return sorted(n for n in registry if n.startswith(module_filter))

    return sorted(registry.keys())


def get_tool_schema(tool_name: str) -> dict[str, Any] | None:
    """Get the schema for a specific tool by name.

    Args:
        tool_name: Full tool name (e.g. ``"fxExcel.math_formulas.ABS"``).

    Returns:
        The tool schema dict, or None if not found.

    Complexity: O(1) average case (dict lookup).
    """
    registry = _build_registry()
    entry = registry.get(tool_name)

    if entry:
        return entry["schema"]

    return None


def invoke_tool(tool_name: str, arguments: dict[str, Any]) -> Any:
    """Invoke a FormuLite tool by name with the given arguments.

    Args:
        tool_name: Full tool name (e.g. ``"fxExcel.math_formulas.SUM"``).
        arguments: Dict of argument names to values.

    Returns:
        The result of calling the function.

    Raises:
        KeyError: If the tool name is not found in the registry.
        TypeError: If arguments don't match the function signature.

    Example:
        >>> invoke_tool("fxExcel.math_formulas.ABS", {"number": -5.5})
        5.5

    Complexity: O(1) for lookup + cost of the invoked function.
    """
    registry = _build_registry()
    entry = registry.get(tool_name)

    if entry is None:
        raise KeyError(
            f"Tool '{tool_name}' not found. "
            f"Use get_tool_names() to list available tools."
        )

    func = entry["callable"]
    return func(**arguments)


# Lazy-initialized semantic search engine (None = not yet attempted).
_SEMANTIC_ENGINE: Optional[Any] = None
_SEMANTIC_AVAILABLE: Optional[bool] = None


def _get_semantic_engine() -> Any:
    """Get or initialize the semantic search engine.

    Returns the ``SemanticToolSearch`` instance. Raises if fastembed
    is not installed or initialization fails.

    Returns:
        A ``SemanticToolSearch`` instance.

    Raises:
        ImportError: If fastembed is not installed.
        RuntimeError: If initialization fails.

    Complexity: O(n) on first call (builds index), O(1) thereafter.
    """
    global _SEMANTIC_ENGINE, _SEMANTIC_AVAILABLE

    if _SEMANTIC_AVAILABLE is False:
        raise ImportError(
            "fastembed is required for semantic search. "
            "Install it with: pip install fastembed"
        )

    if _SEMANTIC_ENGINE is not None:
        return _SEMANTIC_ENGINE

    try:
        from formulite.semantic_search import SemanticToolSearch

        schemas = get_tool_schemas()
        _SEMANTIC_ENGINE = SemanticToolSearch(schemas)
        _SEMANTIC_AVAILABLE = True
        return _SEMANTIC_ENGINE
    except ImportError:
        _SEMANTIC_AVAILABLE = False
        raise ImportError(
            "fastembed is required for semantic search. "
            "Install it with: pip install fastembed"
        )
    except Exception as exc:
        _SEMANTIC_AVAILABLE = False
        raise RuntimeError(
            f"Semantic search initialization failed: {exc}"
        ) from exc


def warm_up_semantic_search() -> bool:
    """Pre-build the semantic search index at startup.

    Loads the embedding model and computes vectors for all registered
    tools so the first ``search_tools`` call is instant.

    Returns:
        ``True`` if semantic search is ready, ``False`` if unavailable.

    Complexity: O(n) where n is the total number of tools.
    """
    engine = _get_semantic_engine()
    return engine is not None


def search_tools(
    query: str,
    top_k: int = 10,
    threshold: float = 0.3,
) -> list[dict[str, Any]]:
    """Search for tools by natural-language query.

    Uses semantic vector search powered by fastembed.

    Args:
        query: Natural language search string.
        top_k: Maximum number of results to return.
        threshold: Minimum cosine similarity (0.0–1.0) for results.

    Returns:
        List of matching tool schemas sorted by relevance.

    Raises:
        ImportError: If fastembed is not installed.
        RuntimeError: If the semantic engine fails to initialize.

    Example:
        >>> results = search_tools("calculate compound interest")
        >>> len(results) >= 1
        True

    Complexity: O(n) where n is the total number of tools.
    """
    engine = _get_semantic_engine()
    return engine.search(query, top_k=top_k, threshold=threshold)
