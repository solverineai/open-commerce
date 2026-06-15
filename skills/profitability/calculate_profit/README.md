# calculate_profit

Calculate gross revenue, total costs, net profit, margin rate, ROI, and break-even unit price from explicit commerce cost inputs.

## Inputs

- Selling price.
- Product cost.
- Marketplace fee.
- Payment fee.
- Shipping cost.
- Return cost.
- Advertising cost.
- Other costs.
- Quantity.

## Output

Returns a structured profitability result with a cost breakdown and assumptions.

## Notes

Use explicit monetary inputs first. Dataset-backed fee lookup should only be used when the dataset status is `reviewed` or `stable`, or when the response clearly flags lower confidence.
