"""MCP tools for Open Commerce datasets and profitability calculations."""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Dict, List

from opencommerce import ProfitEngine

try:  # Optional dependency, installed with the `mcp` extra.
    from mcp.server.fastmcp import FastMCP
except ImportError:  # pragma: no cover - exercised only when running the server without extras.
    FastMCP = None  # type: ignore[assignment]

Dataset = Dict[str, Any]


def find_datasets_root() -> Path:
    configured = os.environ.get("OPENCOMMERCE_DATASETS")
    if configured:
        return Path(configured).expanduser().resolve()

    candidates = [Path.cwd(), *Path(__file__).resolve().parents]
    for candidate in candidates:
        datasets = candidate / "datasets"
        if datasets.is_dir():
            return datasets

    return Path.cwd() / "datasets"


def dataset_status_warning(status: str) -> str:
    warnings = {
        "starter": "Structural placeholder only. Do not treat as verified platform economics.",
        "draft": "Partial source-backed data. Return source IDs, version, and confidence warnings before use.",
        "reviewed": "Reviewed data. Still check effective date, market, category, account, and provider conditions.",
        "stable": "Stable data. Still check effective date, market, category, account, and provider conditions.",
        "deprecated": "Deprecated data. Do not use for new analysis unless explicitly comparing historical behavior.",
    }
    return warnings.get(status, "Unknown status. Do not use without maintainer review.")


def economics_dataset_paths(datasets_root: Path | None = None) -> List[Path]:
    root = datasets_root or find_datasets_root()
    return sorted(root.glob("*/*/economics.json"))


def load_dataset(path: Path) -> Dataset:
    return json.loads(path.read_text(encoding="utf-8"))


def list_dataset_index() -> Dict[str, Any]:
    datasets = []
    for path in economics_dataset_paths():
        dataset = load_dataset(path)
        status = dataset["metadata"]["status"]
        provider = dataset["provider"]
        datasets.append(
            {
                "provider_id": provider["id"],
                "name": provider["name"],
                "dataset_type": dataset["dataset_type"],
                "markets": dataset["coverage"]["markets"],
                "currency": dataset["coverage"]["currency"],
                "version": dataset["metadata"]["version"],
                "status": status,
                "warning": dataset_status_warning(status),
                "path": str(path),
            }
        )
    return {"datasets": datasets, "count": len(datasets)}


def get_dataset_by_provider(provider_id: str) -> Dict[str, Any]:
    normalized = provider_id.strip().lower()
    for path in economics_dataset_paths():
        dataset = load_dataset(path)
        if dataset["provider"]["id"].lower() == normalized:
            status = dataset["metadata"]["status"]
            return {
                "dataset": dataset,
                "status": status,
                "warning": dataset_status_warning(status),
                "path": str(path),
            }
    raise ValueError(f"Unknown Open Commerce provider_id: {provider_id}")


def calculate_profit_payload(
    *,
    selling_price: float,
    product_cost: float,
    marketplace_fee: float = 0,
    payment_fee: float = 0,
    shipping_cost: float = 0,
    return_cost: float = 0,
    ad_cost: float = 0,
    other_costs: float = 0,
    quantity: int = 1,
    currency: str = "KRW",
) -> Dict[str, Any]:
    engine = ProfitEngine(default_currency=currency)
    result = engine.calculate_profit(
        selling_price=selling_price,
        product_cost=product_cost,
        marketplace_fee=marketplace_fee,
        payment_fee=payment_fee,
        shipping_cost=shipping_cost,
        return_cost=return_cost,
        ad_cost=ad_cost,
        other_costs=other_costs,
        quantity=quantity,
        currency=currency,
    )
    result["assumptions"] = [
        "All cost inputs were supplied explicitly.",
        "No marketplace, shipping, return, payment, or ad fee was inferred by the MCP tool.",
    ]
    return result


if FastMCP is not None:
    mcp = FastMCP(
        "open-commerce",
        instructions=(
            "Use Open Commerce tools for AI-native commerce profitability and economics data. "
            "Never treat starter datasets as verified platform economics. Return dataset source "
            "IDs, version, and status warnings when using draft economics."
        ),
    )

    @mcp.tool()
    def calculate_profit(
        selling_price: float,
        product_cost: float,
        marketplace_fee: float = 0,
        payment_fee: float = 0,
        shipping_cost: float = 0,
        return_cost: float = 0,
        ad_cost: float = 0,
        other_costs: float = 0,
        quantity: int = 1,
        currency: str = "KRW",
    ) -> Dict[str, Any]:
        """Calculate profit, margin, ROI, and break-even price from explicit costs."""

        return calculate_profit_payload(
            selling_price=selling_price,
            product_cost=product_cost,
            marketplace_fee=marketplace_fee,
            payment_fee=payment_fee,
            shipping_cost=shipping_cost,
            return_cost=return_cost,
            ad_cost=ad_cost,
            other_costs=other_costs,
            quantity=quantity,
            currency=currency,
        )

    @mcp.tool()
    def list_datasets() -> Dict[str, Any]:
        """List Open Commerce economics datasets and trust statuses."""

        return list_dataset_index()

    @mcp.tool()
    def get_economics_dataset(provider_id: str) -> Dict[str, Any]:
        """Return one provider economics dataset with source references and warnings."""

        return get_dataset_by_provider(provider_id)

    @mcp.tool()
    def explain_dataset_status(status: str) -> Dict[str, str]:
        """Explain how agents may use an Open Commerce dataset status."""

        normalized = status.strip().lower()
        return {"status": normalized, "warning": dataset_status_warning(normalized)}
else:
    mcp = None


def main() -> int:
    if mcp is None:
        raise SystemExit("Install MCP dependencies with: python -m pip install -e '.[mcp]'")
    mcp.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
