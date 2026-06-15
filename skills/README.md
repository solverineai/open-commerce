# Commerce Skills

Open Commerce skills are reusable commerce capabilities for AI agents, LangGraph nodes, MCP tools, n8n workflows, OpenAI Codex tasks, Claude Code tasks, and commerce automation systems.

Each skill includes:

- `README.md`: Purpose, inputs, outputs, and usage notes.
- `interface.json`: Machine-readable interface specification.
- `examples/`: Example request and response payloads.
- `mcp.md`: Future MCP support notes.

## Skill Domains

- `profitability/`: Profit, margin, break-even, and ROI analysis.
- `forecasting/`: Demand forecast, stockout prediction, and reorder recommendation.
- `marketplace/`: Marketplace fee lookup and settlement calculation.
- `inventory/`: Inventory health and turnover analysis.
- `fulfillment/`: Shipping cost estimation and fulfillment recommendation.
- `pricing/`: Competitor gap analysis and dynamic pricing.

## Design Principles

- Keep inputs explicit.
- Return structured JSON.
- State assumptions and missing data.
- Do not invent economics when dataset status is `starter`.
- Preserve compatibility with agent frameworks and workflow engines.
