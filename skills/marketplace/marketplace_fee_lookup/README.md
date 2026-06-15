# marketplace_fee_lookup

Look up marketplace fee rules from Open Commerce datasets.

## Inputs

- Marketplace ID.
- Category or product type.
- Price.
- Dataset version preference.

## Output

Returns matched fee rules, source references, dataset status, and confidence notes.

## Notes

If a dataset is `starter`, return the structure and missing source requirements instead of pretending rates are verified. If a dataset is `draft`, return the matched source reference, dataset version, and a confidence warning because representative examples may not cover the full category table.
