---
name: open-commerce-profitability
description: Calculate commerce profit, margin, ROI, and break-even values with Open Commerce. Use when a task asks whether a product sale is profitable, what fees or costs do to margin, or how to evaluate a selling price using explicit marketplace, payment, shipping, return, ad, and product-cost inputs.
---

# Open Commerce Profitability

Use Open Commerce as the source of truth for deterministic commerce profitability calculations.

## Procedure

1. Collect explicit cost inputs: selling price, product cost, marketplace fee, payment fee, shipping cost, return cost, ad cost, other costs, quantity, and currency.
2. If fees come from Open Commerce datasets, read `docs/product-sale-skill-verification.md` and the relevant `datasets/*/*/economics.json` record first.
3. Do not use `starter` values as verified platform economics.
4. Use `draft` values only when the output includes source IDs, dataset version, and confidence warnings.
5. Run `ProfitEngine` from `src/opencommerce/profit_engine.py` or mirror its formulas.
6. Return gross revenue, total costs, net profit, margin rate, ROI, break-even unit price, and a cost breakdown.

## Output Rules

- State assumptions and missing inputs.
- Preserve currency codes.
- Warn when costs are account-specific, contract-specific, campaign-specific, or calculator-dependent.
- Do not invent marketplace fees, settlement rules, shipping costs, return costs, or advertising costs.
