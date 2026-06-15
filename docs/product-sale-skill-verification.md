# Product Sale Skill Verification

This document maps a product-sale workflow to Open Commerce skills and records whether the current dataset values are official, partial, or still unverified.

## Skill Flow

When an agent evaluates selling a product, it should use skills in this order:

1. `marketplace/marketplace_fee_lookup`: Find marketplace fee rules and dataset confidence.
2. `fulfillment/shipping_cost_estimator`: Estimate shipping or fulfillment cost.
3. `marketplace/settlement_calculator`: Estimate payout amount after fees and deductions.
4. `profitability/calculate_profit`: Calculate gross revenue, total costs, net profit, margin, ROI, and break-even price.
5. `inventory/inventory_health_check`: Check whether available stock can support the sale.
6. `forecasting/stockout_prediction`: Evaluate stockout risk after expected demand.
7. `forecasting/reorder_recommendation`: Recommend replenishment only when demand and lead time are explicit.
8. `pricing/competitor_gap_analysis`: Compare competitive position when competitor observations are timestamped.
9. `pricing/dynamic_pricing`: Recommend price changes within profitability guardrails.

## Current Verification Status

| Dataset | Status | What is verified |
| --- | --- | --- |
| Coupang | `draft` | Representative official category commission examples and Rocket Growth cost examples. |
| SmartStore | `starter` | Official help center location is recorded, but exact fee table is not materialized. |
| 11st | `starter` | Official service-fee FAQ location is recorded, but exact category table is not materialized. |
| Gmarket | `draft` | Official ESM Plus service-fee formula, 1% to 12% category range, prepaid-shipping surcharge, and server-fee rule. |
| Auction | `draft` | Same ESM Plus formula coverage as Gmarket; exact category lookup still needs full table ingestion. |
| Cafe24 | `draft` | Official Cafe24 PRO service fees and Cafe24 Payments fee examples. |
| Amazon | `draft` | Representative official US referral fee examples and minimum referral fee notes. |
| Shopify | `draft` | Official Shopify payment fee examples observed from localized pricing; rates vary by store location and plan. |
| eBay | `draft` | Official final value fee range, per-order fees, and representative category examples. |
| CJ Logistics | `draft` | Official parcel price lookup source and package-size rules; exact calculated prices are not stored. |
| Hanjin | `draft` | Official fee lookup source and surcharge notes; base calculated prices are not stored. |
| Lotte Global Logistics | `draft` | Official agency parcel public tariff examples. |
| Toss Payments | `draft` | Official public PG fee table. |
| KCP | `starter` | No direct official NHN KCP fee table was materialized; rates remain unavailable. |
| KG Inicis | `draft` | Official payment-method fee table. |
| Coupang Ads | `draft` | Official CPC model; exact CPC is campaign dependent. |
| Naver Ads | `draft` | Official CPC model; exact CPC is bid and auction dependent. |

## Agent Rules

- A skill may use a `draft` value only when it returns the source ID, dataset version, and confidence warning.
- A skill must not treat `starter` values as actual platform data.
- A skill must not infer a missing category rate from an example category.
- Account-specific, contract-specific, campaign-specific, or localized values must be requested from the seller account or official calculator before automated action.

## Next Data Work

- Ingest full category tables for Coupang, Gmarket, Auction, Amazon, and eBay.
- Extract exact SmartStore and 11st current fee tables from official seller-center pages.
- Add direct official NHN KCP fee source or keep KCP unavailable.
- Add dedicated settlement timing sources by provider.
- Add carrier return-cost sources separately from outbound shipping tables.
