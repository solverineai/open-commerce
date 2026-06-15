# Schema Standard

Open Commerce schemas use JSON Schema Draft 2020-12.

## Design Goals

- Plain JSON records.
- Stable identifiers.
- No required PII.
- Clear descriptions for AI agents.
- Compatibility with LangGraph state, MCP tool payloads, workflow engines, and repository automation.

## Conventions

- Every schema includes `$schema`, `$id`, `title`, `description`, `type`, and `properties`.
- Records include `schema_version`.
- Currency amounts are objects with `amount` and `currency`.
- Timestamps use RFC 3339 strings.
- Agent-facing context belongs in `agent_context`.
- External identifiers belong in `external_refs`.

## Compatibility

Additive optional fields are preferred. Required field changes should use a proposal issue and migration note.
