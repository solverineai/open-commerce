# dynamic_pricing

Recommend price adjustments using cost, margin, demand, inventory, and competitor context.

## Inputs

- Current price.
- Cost and fee assumptions.
- Margin floor.
- Inventory state.
- Demand forecast.
- Competitor observations.

## Output

Returns recommended price, guardrail checks, rationale, and confidence warnings.

## Notes

This skill should produce recommendations only. Price changes require explicit downstream authorization.
