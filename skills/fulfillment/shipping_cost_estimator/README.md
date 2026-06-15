# shipping_cost_estimator

Estimate shipping cost from carrier, service level, parcel attributes, destination, and dataset rules.

## Inputs

- Carrier ID.
- Origin and destination market.
- Weight and dimensions.
- Service level.
- Dataset version preference.

## Output

Returns estimated shipping cost, matched rules, source references, and warnings.

## Notes

Starter logistics datasets should produce missing-source warnings rather than verified estimates. Draft logistics datasets may point to official calculators or public tariff examples, but the skill must still return the source and tell the caller when a final account-specific quote is required.
