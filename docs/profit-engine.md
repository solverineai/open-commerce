# Profit Engine

The Profit Engine provides simple deterministic calculations for commerce economics.

## Core Inputs

- Selling price.
- Product cost.
- Marketplace fee.
- Payment fee.
- Shipping cost.
- Return cost.
- Advertising cost.
- Other costs.
- Quantity.

## Core Outputs

- Gross revenue.
- Total costs.
- Net profit.
- Margin rate.
- ROI.
- Break-even unit price.

## Current Scope

The first implementation treats fees as explicit monetary amounts. Dataset-backed fee lookup is a future layer so that the first API remains deterministic and easy to test.

## Future Direction

- Dataset-driven fee lookup.
- Scenario analysis.
- Forecast-aware inventory profitability.
- Agent tool wrappers for MCP and LangGraph.
