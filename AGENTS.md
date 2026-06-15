# Open Commerce Agent Guide

## Repository Purpose

Open Commerce is the open standard and economic intelligence layer for AI-native commerce. Treat this repository as infrastructure for commerce datasets, schemas, profitability calculations, agent skills, prompts, and MCP interfaces.

## Core Rules

- Do not position Open Commerce as an OMS, ERP, WMS, or marketplace connector.
- Treat `datasets/*/*/economics.json` as source-backed economics records, not as complete production fee tables.
- Never use `starter` dataset values as actual platform economics.
- Use `draft` values only when the response includes source IDs, dataset version, and confidence warnings.
- Do not infer missing category rates, settlement timing, shipping costs, return costs, or ad costs from examples.
- Keep public schemas, datasets, skills, prompts, and docs compatible with agent workflows.

## Development Commands

Run these checks before committing changes:

```bash
python -m unittest discover -s tests -p "test*.py"
python tools/validate_schemas.py
python tools/validate_skills.py
python tools/validate_agent_packages.py
python tools/validate_datasets.py
python tools/validate_markdown.py
python tools/validate_contribution.py
```

## Agent Package Rules

- Codex repo-scoped skills live under `.agents/skills/*/SKILL.md`.
- Claude repo-scoped skills live under `.claude/skills/*/SKILL.md`.
- Codex plugin packages live under `plugins/codex/*`.
- Claude plugin packages live under `plugins/claude/*`.
- Shared domain specifications remain under `skills/`; do not replace them with runtime-specific package files.

## MCP Rules

- The Python MCP server lives in `src/opencommerce_mcp/server.py`.
- MCP tools must return dataset status and source-reference context whenever platform economics are used.
- Keep MCP tool names explicit and stable because external agents may depend on them.
