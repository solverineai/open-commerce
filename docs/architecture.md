# Architecture

Open Commerce is organized as a skills-first repository with datasets, schemas, prompts, examples, and validation around those skills.

## Boundary

Open Commerce does not connect to marketplaces, operate a warehouse, manage customer service, or replace an OMS. It defines common economic records and provides calculations that other systems can use.

## Layers

| Layer | Directory | Responsibility |
| --- | --- | --- |
| Skill Layer | `skills/` | Reusable commerce capabilities for agents and future MCP tools. |
| Dataset Layer | `datasets/` | Source-backed economics for marketplaces, logistics, payments, and advertising. |
| Schema Layer | `schemas/` | JSON Schemas for interoperable commerce records. |
| Prompt Layer | `prompts/` | Reusable Markdown prompts for agent workflows. |
| Agent Layer | `examples/`, `sdk/`, `src/opencommerce/` | Early examples and SDK surfaces for agent interoperability. |
| Governance Layer | root docs and `governance/` | Contribution, review, and decision rules. |

## Agent Compatibility

Schemas and examples are designed to be plain JSON so they can move through:

- LangGraph state.
- MCP tool input and output payloads.
- n8n workflow nodes.
- OpenAI Codex repository tasks.
- Claude Code repository tasks.

## Trust Model

Dataset entries should be explicit about evidence. A value can be useful before it is final, but it must not be represented as verified unless the source reference supports it.
