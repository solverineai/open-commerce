# Python SDK

Install locally:

```bash
python -m pip install -e .
```

Use:

```python
from opencommerce import ProfitEngine

engine = ProfitEngine(default_currency="KRW")
result = engine.calculate_profit(
    selling_price=35000,
    product_cost=17000,
    marketplace_fee=3500,
    payment_fee=900,
    shipping_cost=3200,
    ad_cost=2500,
)
```

The SDK currently exposes deterministic profitability primitives. Dataset-backed fee lookup, forecast adapters, LangGraph wrappers, MCP tools, and n8n examples are planned future layers.
