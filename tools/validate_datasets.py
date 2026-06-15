"""Validate Open Commerce economics datasets."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Iterable, Set

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_DATASETS = {
    "marketplaces/coupang",
    "marketplaces/smartstore",
    "marketplaces/11st",
    "marketplaces/gmarket",
    "marketplaces/auction",
    "marketplaces/cafe24",
    "marketplaces/amazon",
    "marketplaces/shopify",
    "marketplaces/ebay",
    "logistics/cj",
    "logistics/hanjin",
    "logistics/lotte",
    "payments/toss",
    "payments/kcp",
    "payments/kg",
    "advertising/coupang_ads",
    "advertising/naver_ads",
}

RULE_SECTIONS = ["fee_structures", "settlement_rules", "shipping_costs", "return_costs"]


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def rule_source_refs(dataset: Dict[str, Any]) -> Iterable[str]:
    for section in RULE_SECTIONS:
        for rule in dataset.get(section, []):
            yield from rule.get("source_ref_ids", [])


def validate_source_links(path: Path, dataset: Dict[str, Any]) -> None:
    source_ids: Set[str] = {source["id"] for source in dataset.get("source_references", [])}
    missing = sorted({source_ref for source_ref in rule_source_refs(dataset) if source_ref not in source_ids})
    if missing:
        raise SystemExit(f"{path}: source_ref_ids not found in source_references: {', '.join(missing)}")


def main() -> int:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        Draft202012Validator = None

    schema = load_json(ROOT / "datasets" / "economics-dataset.schema.json")
    validator = Draft202012Validator(schema) if Draft202012Validator is not None else None

    missing_paths = sorted(
        expected for expected in EXPECTED_DATASETS if not (ROOT / "datasets" / expected / "economics.json").exists()
    )
    if missing_paths:
        raise SystemExit(f"Missing expected datasets: {', '.join(missing_paths)}")

    dataset_paths = sorted((ROOT / "datasets").glob("*/*/economics.json"))
    if len(dataset_paths) != len(EXPECTED_DATASETS):
        raise SystemExit(f"Expected {len(EXPECTED_DATASETS)} datasets, found {len(dataset_paths)}")

    for path in dataset_paths:
        dataset = load_json(path)
        if validator is not None:
            errors = sorted(validator.iter_errors(dataset), key=lambda err: list(err.path))
            if errors:
                messages = [f"{path}: {list(error.path)}: {error.message}" for error in errors]
                raise SystemExit("\n".join(messages))
        validate_source_links(path, dataset)
        if dataset["metadata"]["status"] != dataset["coverage"]["status"]:
            raise SystemExit(f"{path}: metadata.status must match coverage.status")

    print(f"Validated {len(dataset_paths)} economics datasets")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
