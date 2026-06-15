"""Run a basic Open Commerce profitability calculation."""

from opencommerce import ProfitEngine


def main() -> None:
    engine = ProfitEngine(default_currency="KRW")
    result = engine.calculate_profit(
        selling_price=35000,
        product_cost=17000,
        marketplace_fee=3500,
        payment_fee=900,
        shipping_cost=3200,
        return_cost=0,
        ad_cost=2500,
    )
    print(result)


if __name__ == "__main__":
    main()
