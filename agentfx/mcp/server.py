"""AgentFx MCP (Model Context Protocol) Server.

Exposes all AgentFx functions as MCP tools, enabling AI agents (Claude,
Copilot, etc.) to discover and execute 580+ mathematical, statistical,
date, text, and financial functions directly.

Usage:
    Run via stdio (default for MCP clients):
        python -m agentfx.mcp

    Or use the entry point:
        agentfx-mcp

Complexity: O(n) startup for tool registration, O(1) per tool invocation.
"""

import json
from typing import Any

from mcp.server.fastmcp import FastMCP

from agentfx.registry import get_tool_schemas, invoke_tool, search_tools, warm_up_semantic_search

mcp = FastMCP(
    "AgentFx",
    instructions=(
        "AgentFx provides 1600+ reusable functions organized in 6 modules: "
        "fxDate (dates), fxNumeric (math/finance/stats/calculator), fxString (text), "
        "fxPython (utilities), fxExcel (Excel-compatible), fxVBA (VBA-compatible). "
        "\n\n"
        "IMPORTANT — Dynamic tool definition: AgentFx does NOT register each "
        "function as an individual MCP tool. Instead, use these meta-tools to "
        "discover and execute functions at runtime:\n"
        "1. 'search_agentfx_tools' — find functions by natural language query "
        "(semantic search when fastembed is installed).\n"
        "2. 'list_agentfx_tools' — browse available functions by module.\n"
        "3. 'get_agentfx_tool_details' — get full parameter schema before calling.\n"
        "4. 'call_agentfx' — execute any function by its qualified name "
        "(format: module.file.function, e.g. 'fxExcel.math_formulas.ABS').\n"
        "5. 'scientific_calculate' — evaluate math expressions directly (AST-safe).\n"
        "6. 'get_scientific_constant' — look up math/physical constants.\n"
        "\n"
        "Recommended workflow: SEARCH → INSPECT → EXECUTE. "
        "Always use these functions for calculations instead of computing results "
        "via inference — they guarantee deterministic, reproducible answers."
    ),
)


@mcp.tool()
def list_agentfx_tools(module: str = "") -> str:
    """List available AgentFx functions, optionally filtered by module.

    Args:
        module: Optional module prefix to filter results.
            Valid prefixes: fxDate, fxNumeric, fxString, fxPython, fxExcel, fxVBA.
            Leave empty to list all functions.

    Returns:
        JSON array of tool schemas with name, description, and parameters.

    Example:
        list_agentfx_tools("fxExcel.math")
    """
    schemas = get_tool_schemas(module_filter=module or None)

    # Return compact summaries to avoid overwhelming the context
    summaries = [
        {"name": s["name"], "description": s.get("description", "")}
        for s in schemas
    ]

    return json.dumps(summaries, indent=2, default=str)


@mcp.tool()
def search_agentfx_tools(query: str) -> str:
    """Search AgentFx functions using natural language or keywords.

    Supports semantic search (when fastembed is installed) to find
    functions by intent, not just exact keyword matching. For example,
    'calculate compound interest' will find financial functions even
    if "compound" does not appear in the function name.

    Falls back to substring matching if semantic search is unavailable.

    Args:
        query: Natural language query or keyword
            (e.g. 'round a number', 'date difference in business days').

    Returns:
        JSON array of matching tool schemas sorted by relevance.

    Example:
        search_agentfx_tools("convert temperature")
    """
    results = search_tools(query)

    summaries = [
        {
            "name": s["name"],
            "description": s.get("description", ""),
            "parameters": s.get("parameters", {}),
        }
        for s in results
    ]

    return json.dumps(summaries, indent=2, default=str)


@mcp.tool()
def get_agentfx_tool_details(tool_name: str) -> str:
    """Get full details of a specific AgentFx function including parameters.

    Args:
        tool_name: Full tool name (e.g. 'fxExcel.math_formulas.SUM').

    Returns:
        JSON object with name, description, and full parameter schema.

    Example:
        get_agentfx_tool_details("fxExcel.lookup_formulas.VLOOKUP")
    """
    from agentfx.registry import get_tool_schema

    schema = get_tool_schema(tool_name)

    if schema is None:
        return json.dumps({"error": f"Tool '{tool_name}' not found."})

    return json.dumps(schema, indent=2, default=str)


@mcp.tool()
def call_agentfx(tool_name: str, arguments: str = "{}") -> str:
    """Execute a AgentFx function by name with the given arguments.

    Args:
        tool_name: Full tool name (e.g. 'fxExcel.math_formulas.ABS').
        arguments: JSON string of arguments (e.g. '{"number": -5.5}').

    Returns:
        JSON object with the result or error message.

    Example:
        call_agentfx("fxExcel.math_formulas.ABS", '{"number": -5.5}')
    """
    try:
        parsed_args: dict[str, Any] = json.loads(arguments)
    except json.JSONDecodeError as exc:
        return json.dumps({"error": f"Invalid JSON arguments: {exc}"})

    try:
        result = invoke_tool(tool_name, parsed_args)
        return json.dumps({"result": result}, default=str)
    except KeyError as exc:
        return json.dumps({"error": str(exc)})
    except TypeError as exc:
        return json.dumps({"error": f"Argument error: {exc}"})
    except Exception as exc:
        return json.dumps({"error": f"{type(exc).__name__}: {exc}"})


def main() -> None:
    """Run the AgentFx MCP server over stdio."""
    warm_up_semantic_search()
    mcp.run(transport="stdio")


@mcp.tool()
def scientific_calculate(expression: str) -> str:
    """Evaluate a mathematical expression safely and return the result.

    Description:
        Parses and evaluates a math expression using AST-based parsing.
        Supports arithmetic (+, -, *, /, **, //, %), scientific functions
        (sin, cos, log, sqrt, factorial, etc.), and constants (pi, e, tau).
        Does NOT use eval() — only whitelisted operations are allowed.

    Args:
        expression: A mathematical expression string.
            Examples: "sin(pi/4) + sqrt(2)", "log(100, 10)", "factorial(5)"

    Returns:
        JSON object with the numeric result or error message.

    Example:
        scientific_calculate("sin(pi/2) + cos(0)")
    """
    from agentfx.fxNumeric.calculator_functions import evaluate_expression

    try:
        result = evaluate_expression(expression)
        return json.dumps({"expression": expression, "result": result}, default=str)
    except (TypeError, ValueError) as exc:
        return json.dumps({"error": str(exc)})
    except Exception as exc:
        return json.dumps({"error": f"{type(exc).__name__}: {exc}"})


@mcp.tool()
def get_scientific_constant(name: str) -> str:
    """Look up a mathematical or physical constant by name.

    Description:
        Returns the value of a scientific constant from the built-in
        catalog. Supports both mathematical constants (pi, e, phi, tau)
        and physical constants (speed_of_light, planck, avogadro, etc.).

    Args:
        name: The constant name (case-insensitive).
            Examples: "pi", "e", "avogadro", "speed_of_light", "planck"

    Returns:
        JSON object with the constant value, symbol, and description.

    Example:
        get_scientific_constant("avogadro")
    """
    from agentfx.fxNumeric.constants_functions import _CONSTANTS

    key = name.strip().lower()

    if key not in _CONSTANTS:
        available = ", ".join(sorted(_CONSTANTS.keys()))
        return json.dumps({"error": f"Unknown constant '{name}'. Available: {available}"})

    value, symbol, description = _CONSTANTS[key]

    return json.dumps({
        "name": name,
        "symbol": symbol,
        "value": value,
        "description": description,
    }, default=str)


@mcp.tool()
def list_scientific_constants(category: str = "") -> str:
    """List available scientific and mathematical constants.

    Args:
        category: Filter by "math" or "physical". Leave empty for all.

    Returns:
        JSON array of constants with name, symbol, value, and description.

    Example:
        list_scientific_constants("math")
    """
    from agentfx.fxNumeric.constants_functions import list_constants

    try:
        cat = category if category else None
        constants = list_constants(cat)
        return json.dumps(constants, indent=2, default=str)
    except ValueError as exc:
        return json.dumps({"error": str(exc)})


@mcp.tool()
def list_calculator_functions() -> str:
    """List all functions available in the scientific expression evaluator.

    Returns:
        JSON array of function names that can be used inside
        scientific_calculate expressions.

    Example:
        list_calculator_functions()
    """
    from agentfx.fxNumeric.calculator_functions import (
        list_available_constants,
        list_available_functions,
    )

    return json.dumps({
        "functions": list_available_functions(),
        "constants": list_available_constants(),
    }, indent=2)


if __name__ == "__main__":
    main()
