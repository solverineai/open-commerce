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

If a dataset is `starter`, return the structure and missing source requirements instead of pretending rates are verified.
