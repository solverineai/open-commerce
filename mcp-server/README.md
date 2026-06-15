# Open Commerce MCP Server

The MCP server implementation lives in `src/opencommerce_mcp/server.py` so it can be installed with the Python package.

## Install

```bash
python -m pip install -e ".[mcp]"
```

## Run

```bash
OPENCOMMERCE_DATASETS=./datasets python -m opencommerce_mcp.server
```

See `docs/mcp-server.md` for tools, safety rules, and plugin integration notes.
