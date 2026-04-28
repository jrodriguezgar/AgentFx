"""shortfx MCP Server — backward-compatible redirect.

The server has moved to ``shortfx.mcp.server``. This module re-exports
``main`` and ``mcp`` for backward compatibility.
"""

from shortfx.mcp.server import main, mcp  # noqa: F401

if __name__ == "__main__":
    main()
