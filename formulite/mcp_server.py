"""FormuLite MCP Server — backward-compatible redirect.

The server has moved to ``formulite.mcp.server``. This module re-exports
``main`` and ``mcp`` for backward compatibility.
"""

from formulite.mcp.server import main, mcp  # noqa: F401

if __name__ == "__main__":
    main()
