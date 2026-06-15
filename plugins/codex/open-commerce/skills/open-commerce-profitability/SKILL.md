---
name: open-commerce-profitability
description: Calculate commerce profit, margin, ROI, and break-even values with Open Commerce. Use when a task asks whether a product sale is profitable, what fees or costs do to margin, or how to evaluate a selling price using explicit marketplace, payment, shipping, return, ad, and product-cost inputs.
---

# Open Commerce Profitability

Use Open Commerce for deterministic product-sale profitability analysis.

## Procedure

1. Collect explicit selling price, product cost, marketplace fee, payment fee, shipping cost, return cost, ad cost, other costs, quantity, and currency.
2. If using Open Commerce datasets, inspect dataset status and source references before applying any value.
3. Do not use `starter` economics as verified platform data.
4. Use `draft` values only with source IDs, dataset version, and confidence warnings.
5. Calculate gross revenue, total costs, net profit, margin rate, ROI, break-even unit price, and cost breakdown.
6. Prefer the MCP `calculate_profit` tool when the Open Commerce MCP server is available.

## Output Rules

- State all assumptions and missing inputs.
- Preserve currency codes.
- Warn for account-specific, contract-specific, campaign-specific, and calculator-dependent values.
- Do not invent fees or costs.
