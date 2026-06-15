---
name: open-commerce-marketplace-economics
description: Inspect Open Commerce marketplace, logistics, payment, and advertising economics datasets with source references and trust-status warnings. Use when a task asks whether platform fee rates, settlement rules, shipping costs, return costs, payment fees, or ad costs are official, draft, starter, reviewed, or safe for an agent to use.
---

# Open Commerce Marketplace Economics

Use this skill to decide whether platform economics data can be used in an agent workflow.

## Procedure

1. Identify the provider, dataset type, market, category, fee basis, and requested value.
2. Read the matching `datasets/*/*/economics.json` record.
3. Check `coverage.status`, `metadata.status`, rule-level `status`, `source_references`, and `version_history`.
4. If the record is `starter`, return that the value is not verified platform data.
5. If the record is `draft`, return only representative or partial values with source IDs, dataset version, and a warning.
6. If the value is missing, account-specific, contract-specific, campaign-specific, or calculator-dependent, ask for seller-account data or official calculator output.

## Required References

- `datasets/economics-dataset.schema.json` defines the economics dataset contract.
- `docs/dataset-standard.md` explains dataset quality expectations.
- `docs/product-sale-skill-verification.md` lists current provider verification status.

## Output Rules

- Include provider ID, dataset version, dataset status, source IDs, and reliability.
- Separate verified values from examples, notes, and unavailable fields.
- Do not infer missing category rates from neighboring categories or examples.
