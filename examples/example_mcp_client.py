"""Example: Using the shortfx MCP server programmatically.

This script demonstrates how an AI agent or client application can connect
to the shortfx MCP server and use its tools to discover and execute
800+ mathematical, text, date, financial, and statistical functions.

Requirements:
    pip install shortfx[mcp]

Usage:
    python example_mcp_client.py
"""

import asyncio
import json

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client


async def main() -> None:
    """Connect to the shortfx MCP server and demonstrate all 4 tools."""

    # ── 1. Connect to the shortfx MCP server via stdio ─────────────
    server_params = StdioServerParameters(
        command="python",
        args=["-m", "shortfx.mcp"],
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            await session.initialize()

            # ── 2. List available tools ──────────────────────────────
            tools = await session.list_tools()
            print("=== Available MCP Tools ===")

            for tool in tools.tools:
                print(f"  - {tool.name}: {tool.description[:70]}...")

            print()

            # ── 3. Search for functions by keyword ───────────────────
            print("=== Search: 'round' ===")
            result = await session.call_tool(
                "search_shortfx_tools",
                arguments={"query": "round"},
            )
            matches = json.loads(result.content[0].text)
            print(f"Found {len(matches)} functions matching 'round':")

            for m in matches[:5]:
                print(f"  - {m['name']}: {m['description']}")

            print()

            # ── 4. List functions by module ───────────────────────────
            print("=== List: fxDate module ===")
            result = await session.call_tool(
                "list_shortfx_tools",
                arguments={"module": "fxDate"},
            )
            date_tools = json.loads(result.content[0].text)
            print(f"fxDate has {len(date_tools)} functions. First 5:")

            for t in date_tools[:5]:
                print(f"  - {t['name']}")

            print()

            # ── 5. Get details of a specific function ────────────────
            print("=== Details: fxExcel.math_formulas.ABS ===")
            result = await session.call_tool(
                "get_shortfx_tool_details",
                arguments={"tool_name": "fxExcel.math_formulas.ABS"},
            )
            details = json.loads(result.content[0].text)
            print(json.dumps(details, indent=2))
            print()

            # ── 6. Execute functions ─────────────────────────────────
            print("=== Execute Functions ===")

            # Math: absolute value
            result = await session.call_tool(
                "call_shortfx",
                arguments={
                    "tool_name": "fxExcel.math_formulas.ABS",
                    "arguments": json.dumps({"number": -42.5}),
                },
            )
            print(f"ABS(-42.5) = {json.loads(result.content[0].text)['result']}")

            # Numeric: square root
            result = await session.call_tool(
                "call_shortfx",
                arguments={
                    "tool_name": "fxNumeric.arithmetic_functions.square_root",
                    "arguments": json.dumps({"x": 144}),
                },
            )
            print(f"square_root(144) = {json.loads(result.content[0].text)['result']}")

            # String: reverse
            result = await session.call_tool(
                "call_shortfx",
                arguments={
                    "tool_name": "fxString.string_operations.reverse_string",
                    "arguments": json.dumps({"input_string": "shortfx"}),
                },
            )
            print(f"reverse_string('shortfx') = {json.loads(result.content[0].text)['result']}")

            # Finance: future value
            result = await session.call_tool(
                "call_shortfx",
                arguments={
                    "tool_name": "fxNumeric.finance_functions.future_value",
                    "arguments": json.dumps({
                        "rate": 0.05,
                        "nper": 10,
                        "pmt": -100,
                        "pv": -1000,
                    }),
                },
            )
            print(f"future_value(5%, 10y, pmt=-100, pv=-1000) = {json.loads(result.content[0].text)['result']}")

            # Date: validate date
            result = await session.call_tool(
                "call_shortfx",
                arguments={
                    "tool_name": "fxDate.date_operations.is_valid_date",
                    "arguments": json.dumps({"date_input": "2025-02-30"}),
                },
            )
            print(f"is_valid_date('2025-02-30') = {json.loads(result.content[0].text)['result']}")

            # VBA: Left function
            result = await session.call_tool(
                "call_shortfx",
                arguments={
                    "tool_name": "fxVBA.string_functions.Left",
                    "arguments": json.dumps({"string": "Hello World", "length": 5}),
                },
            )
            print(f"Left('Hello World', 5) = {json.loads(result.content[0].text)['result']}")

            print()
            print("=== All examples completed successfully ===")


if __name__ == "__main__":
    asyncio.run(main())
