"""Profit calculation entrypoint."""

from __future__ import annotations

from typing import Any, Dict

from opencommerce import ProfitEngine


def calculate_profit(**kwargs: Any) -> Dict[str, Any]:
    return ProfitEngine().calculate_profit(**kwargs)
