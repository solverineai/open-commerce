# Agent Integrations

Open Commerce is designed to become a commerce capability layer for AI-native commerce agents.

## LangGraph

Skill `interface.json` files and schemas are JSON serializable and can be stored directly in graph state. Stable skills should be easy to wrap as graph nodes.

## MCP

Skills are designed for future MCP tool inputs and outputs. Future MCP servers can expose tools such as:

- `calculate_profit`.
- `marketplace_fee_lookup`.
- `stockout_prediction`.
- `compare_marketplace_economics`.

## n8n

Skill examples should remain easy to convert into workflow nodes by keeping inputs explicit and avoiding hidden process state.

## OpenAI Codex and Claude Code

Repository assets should remain easy for coding agents to inspect, validate, and extend. Prompt assets and skill specs should be explicit about assumptions and source requirements.
