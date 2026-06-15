---
name: open-commerce-marketplace-economics
description: Inspect Open Commerce marketplace, logistics, payment, and advertising economics datasets with source references and trust-status warnings. Use when a task asks whether platform fee rates, settlement rules, shipping costs, return costs, payment fees, or ad costs are official, draft, starter, reviewed, or safe for an agent to use.
---

# Open Commerce Marketplace Economics

Use this skill to evaluate whether platform economics data is safe for an agent workflow.

## Procedure

1. Identify provider, dataset type, market, category, fee basis, and requested value.
2. Load the relevant economics dataset from Open Commerce.
3. Check dataset status, rule status, source references, and version history.
4. Reject `starter` values as unverified platform economics.
5. Return `draft` values only with source IDs, version, and warnings.
6. Prefer the MCP `get_economics_dataset` and `list_datasets` tools when the Open Commerce MCP server is available.

## Output Rules

- Include provider ID, dataset version, dataset status, source IDs, and source reliability.
- Separate verified values, examples, notes, and unavailable values.
- Do not infer missing values from examples.
