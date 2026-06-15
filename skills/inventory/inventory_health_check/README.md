# inventory_health_check

Assess whether inventory is healthy relative to demand, reservations, inbound stock, and safety stock.

## Inputs

- SKU.
- Available quantity.
- Reserved quantity.
- Inbound quantity.
- Safety stock.
- Demand forecast.

## Output

Returns health status, risk level, and recommended investigation steps.

## Notes

Inventory health should consider profitability when recommending replenishment.
