# Decision Process

Open Commerce uses a lightweight decision process for changes that affect standards, datasets, compatibility, governance, or long-term ecosystem direction.

## Change Classes

| Class | Examples | Process |
| --- | --- | --- |
| Patch | Typo fixes, examples, small docs updates | Pull request review. |
| Dataset | Fee rules, settlement timing, source references | Pull request review with source evidence. |
| Schema | New fields, renamed fields, required field changes | Proposal issue plus pull request. |
| Engine | Calculation semantics or return shape | Proposal issue plus tests. |
| Governance | Maintainer model, project scope, decision policy | Proposal issue plus maintainer approval. |

## Proposal Requirements

Compatibility-affecting proposals should include:

- Problem statement.
- Proposed change.
- Alternatives considered.
- Compatibility impact.
- Validation plan.
- Migration notes when applicable.

## Acceptance Criteria

A decision should optimize for:

- Public usefulness.
- Source quality.
- Agent interoperability.
- Minimal ambiguity.
- Long-term maintainability.
