"""Deterministic profit calculations for Open Commerce."""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from typing import Any, Dict, Union

Number = Union[int, float, str, Decimal]


def _to_decimal(value: Number) -> Decimal:
    try:
        decimal_value = Decimal(str(value))
    except (InvalidOperation, ValueError) as exc:
        raise ValueError(f"Invalid numeric value: {value!r}") from exc
    if not decimal_value.is_finite():
        raise ValueError(f"Numeric value must be finite: {value!r}")
    return decimal_value


def _money(value: Decimal) -> float:
    return float(value.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def _ratio(numerator: Decimal, denominator: Decimal) -> float:
    if denominator == 0:
        return 0.0
    return float((numerator / denominator).quantize(Decimal("0.0001"), rounding=ROUND_HALF_UP))


@dataclass(frozen=True)
class ProfitEngine:
    """Small SDK surface for commerce profitability calculations.

    The first version accepts explicit monetary costs instead of resolving fees
    from datasets. Dataset-backed fee lookup can be layered on this API later.
    """

    default_currency: str = "KRW"

    def calculate_profit(
        self,
        *,
        selling_price: Number,
        product_cost: Number,
        marketplace_fee: Number = 0,
        payment_fee: Number = 0,
        shipping_cost: Number = 0,
        return_cost: Number = 0,
        ad_cost: Number = 0,
        other_costs: Number = 0,
        quantity: int = 1,
        currency: str | None = None,
    ) -> Dict[str, Any]:
        if quantity < 1:
            raise ValueError("quantity must be at least 1")

        unit_price = _to_decimal(selling_price)
        unit_product_cost = _to_decimal(product_cost)
        quantity_value = Decimal(quantity)

        gross_revenue = unit_price * quantity_value
        total_product_cost = unit_product_cost * quantity_value
        total_costs = (
            total_product_cost
            + _to_decimal(marketplace_fee)
            + _to_decimal(payment_fee)
            + _to_decimal(shipping_cost)
            + _to_decimal(return_cost)
            + _to_decimal(ad_cost)
            + _to_decimal(other_costs)
        )
        net_profit = gross_revenue - total_costs
        break_even_unit_price = total_costs / quantity_value

        return {
            "currency": currency or self.default_currency,
            "quantity": quantity,
            "gross_revenue": _money(gross_revenue),
            "total_costs": _money(total_costs),
            "net_profit": _money(net_profit),
            "margin_rate": _ratio(net_profit, gross_revenue),
            "roi": _ratio(net_profit, total_costs),
            "break_even_unit_price": _money(break_even_unit_price),
            "cost_breakdown": {
                "product_cost": _money(total_product_cost),
                "marketplace_fee": _money(_to_decimal(marketplace_fee)),
                "payment_fee": _money(_to_decimal(payment_fee)),
                "shipping_cost": _money(_to_decimal(shipping_cost)),
                "return_cost": _money(_to_decimal(return_cost)),
                "ad_cost": _money(_to_decimal(ad_cost)),
                "other_costs": _money(_to_decimal(other_costs)),
            },
        }

    def calculate_margin(
        self,
        *,
        revenue: Number,
        total_costs: Number | None = None,
        profit: Number | None = None,
    ) -> float:
        revenue_value = _to_decimal(revenue)
        if profit is None:
            if total_costs is None:
                raise ValueError("Provide either profit or total_costs")
            profit_value = revenue_value - _to_decimal(total_costs)
        else:
            profit_value = _to_decimal(profit)
        return _ratio(profit_value, revenue_value)

    def calculate_roi(self, *, profit: Number, investment: Number) -> float:
        return _ratio(_to_decimal(profit), _to_decimal(investment))

    def calculate_break_even(
        self,
        *,
        unit_product_cost: Number,
        marketplace_fee: Number = 0,
        payment_fee: Number = 0,
        shipping_cost: Number = 0,
        return_cost: Number = 0,
        ad_cost: Number = 0,
        other_costs: Number = 0,
        fixed_costs: Number = 0,
        target_profit: Number = 0,
        quantity: int = 1,
    ) -> float:
        if quantity < 1:
            raise ValueError("quantity must be at least 1")

        total_required_revenue = (
            _to_decimal(unit_product_cost) * Decimal(quantity)
            + _to_decimal(marketplace_fee)
            + _to_decimal(payment_fee)
            + _to_decimal(shipping_cost)
            + _to_decimal(return_cost)
            + _to_decimal(ad_cost)
            + _to_decimal(other_costs)
            + _to_decimal(fixed_costs)
            + _to_decimal(target_profit)
        )
        return _money(total_required_revenue / Decimal(quantity))
