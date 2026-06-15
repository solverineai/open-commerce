# Open Commerce Claude Guide

## Project Context

Open Commerce is the open standard and economic intelligence layer for AI-native commerce. Use this repository as a standards, dataset, schema, skill, prompt, SDK, and MCP foundation for commerce agents.

## Required Behavior

- Preserve the distinction between Open Commerce and OMS, ERP, WMS, and marketplace connector systems.
- Use `datasets/economics-dataset.schema.json` as the source contract for marketplace, logistics, payment, and advertising datasets.
- Do not treat `starter` records as verified platform data.
- When using `draft` dataset economics, include the source ID, dataset version, and a confidence warning.
- Ask for seller-account, contract, campaign, or calculator data when a value is account-specific.

## Useful Commands

```bash
python -m unittest discover -s tests -p "test*.py"
python tools/validate_schemas.py
python tools/validate_skills.py
python tools/validate_agent_packages.py
python tools/validate_datasets.py
python tools/validate_markdown.py
python tools/validate_contribution.py
```

## Claude Extensions

- Project skills are in `.claude/skills/`.
- Shareable Claude plugin packages are in `plugins/claude/`.
- MCP server usage is documented in `docs/mcp-server.md`.
