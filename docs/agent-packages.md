# Agent Packages

Open Commerce ships agent-facing package entrypoints in addition to the source skill library under `skills/`.

## Codex

- Repo-scoped skills: `.agents/skills/*/SKILL.md`
- Repo marketplace: `.agents/plugins/marketplace.json`
- Shareable plugin package: `plugins/codex/open-commerce`

Codex skills provide concise runtime instructions that point agents back to the source datasets, schemas, SDK, and verification rules.

## Claude Code

- Project skills: `.claude/skills/*/SKILL.md`
- Marketplace catalog: `.claude-plugin/marketplace.json`
- Shareable plugin package: `plugins/claude/open-commerce`

Claude skills mirror the Codex package intent so the same commerce workflows can be invoked from Claude Code.

## Packaged Skills

- `open-commerce-profitability`: Calculate profit, margin, ROI, and break-even values from explicit commerce costs.
- `open-commerce-marketplace-economics`: Inspect marketplace, logistics, payment, and advertising economics datasets with source-status warnings.

## Distribution Rules

- Keep `SKILL.md` concise and move detailed source material to repository docs, schemas, datasets, and examples.
- Keep skill names lowercase, hyphenated, and stable.
- Do not put runtime-specific package files inside the canonical `skills/` source library unless the source contract changes.
- Validate agent packages with `python tools/validate_agent_packages.py`.
