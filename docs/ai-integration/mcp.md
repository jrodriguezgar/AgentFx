# MCP Server

The Model Context Protocol (MCP) server allows AI agents to discover and execute any FormuLite function as a tool.

## Installation

```bash
# MCP support only
pip install formulite[mcp]

# MCP + semantic search (recommended)
pip install formulite[mcp-semantic]
```

## Client Configuration

### VS Code (GitHub Copilot)

Add to your VS Code `settings.json` or `.vscode/mcp.json`:

```json
{
  "servers": {
    "formulite": {
      "command": "formulite-mcp",
      "args": []
    }
  }
}
```

### Claude Desktop

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "formulite": {
      "command": "formulite-mcp",
      "args": []
    }
  }
}
```

### Cursor

Add to `.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "formulite": {
      "command": "formulite-mcp",
      "args": []
    }
  }
}
```

## Available Meta-Tools

| Tool | Description |
|------|-------------|
| `search_formulite_tools` | Natural-language search across all functions |
| `list_formulite_tools` | List functions by module (with optional filter) |
| `get_formulite_tool_details` | Get JSON Schema for a specific function |
| `call_formulite` | Execute a function by qualified name with JSON arguments |
| `scientific_calculate` | Evaluate a math expression (AST-based, safe) |

## Security

| Measure | Detail |
|---------|--------|
| No `eval()` / `exec()` | Expression evaluators use AST-based parsing with whitelisted operations |
| No OS command execution | `subprocess` and OS shell access are not used |
| Sandboxed `apply_expression` | Attribute access restricted to built-in types; private attributes blocked |
| DoS protection | Factorial capped at n ≤ 170; exponents ≤ 10,000; expressions ≤ 1,000 chars |
