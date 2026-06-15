"""Break-even calculation entrypoint."""

from __future__ import annotations

from typing import Any

from opencommerce import ProfitEngine


def calculate_break_even(**kwargs: Any) -> float:
    return ProfitEngine().calculate_break_even(**kwargs)
