# Dataset Standard

Open Commerce datasets describe marketplace economics in a shape that agents and analysis tools can use.

## Required Sections

Each provider dataset must include:

- `dataset_type`.
- `provider`.
- `coverage`.
- `fee_structures`.
- `settlement_rules`.
- `shipping_costs`.
- `return_costs`.
- `metadata`.
- `source_references`.
- `version_history`.

## Status Values

| Status | Meaning |
| --- | --- |
| `starter` | Structural placeholder ready for community completion. |
| `draft` | Values are being collected and may contain unverified entries. |
| `reviewed` | Maintainers reviewed source references and structure. |
| `stable` | Suitable for examples and downstream use with version pinning. |
| `deprecated` | Superseded by a newer dataset version. |

## Evidence Rules

Source references should identify:

- Publisher.
- Title.
- URL when public.
- Access date when public.
- Reliability level: `official`, `partner`, `community`, `inferred`, or `unknown`.

When source material is not public, contributors should describe the limitation without exposing confidential information.

## Versioning

Dataset versions use semantic versioning:

- Patch: source link updates, typo fixes, metadata improvements.
- Minor: new fee category, new shipping rule, new source-backed field.
- Major: breaking shape or semantic change.
