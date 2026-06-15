"""ROI calculation entrypoint."""

from __future__ import annotations

from typing import Any

from opencommerce import ProfitEngine


def calculate_roi(**kwargs: Any) -> float:
    return ProfitEngine().calculate_roi(**kwargs)
