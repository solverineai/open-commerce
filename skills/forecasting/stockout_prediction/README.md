# stockout_prediction

Estimate whether current and inbound inventory can satisfy forecasted demand.

## Inputs

- Current inventory.
- Reserved inventory.
- Inbound inventory.
- Lead time.
- Demand forecast.

## Output

Returns stockout risk, estimated stockout date, and missing data requirements.

## Notes

Do not recommend automated purchase actions unless lead time and demand assumptions are explicit.
