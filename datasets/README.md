# Datasets

Open Commerce datasets describe commerce economics for marketplaces, logistics providers, payment processors, and advertising channels.

Every provider directory contains an `economics.json` file that follows [economics-dataset.schema.json](economics-dataset.schema.json).

## Dataset Groups

- `marketplaces/`: Coupang, Smartstore, 11st, Gmarket, Auction, Cafe24, Amazon, Shopify, eBay.
- `logistics/`: CJ, Hanjin, Lotte.
- `payments/`: Toss, KCP, KG.
- `advertising/`: Coupang Ads, Naver Ads.

Dataset entries use status values to control agent trust. `draft` entries may include official source references and representative values, but they are not necessarily complete category tables. `starter` entries are structural or source-discovery placeholders and must not be treated as verified economics.

See [../docs/product-sale-skill-verification.md](../docs/product-sale-skill-verification.md) for the current product-sale skill flow and platform-data verification matrix.
