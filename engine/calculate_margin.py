"""Margin calculation entrypoint."""

from __future__ import annotations

from typing import Any

from opencommerce import ProfitEngine


def calculate_margin(**kwargs: Any) -> float:
    return ProfitEngine().calculate_margin(**kwargs)
