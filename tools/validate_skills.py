"""Validate Open Commerce skill directories."""

from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

EXPECTED_SKILLS = {
    "profitability": {
        "calculate_profit",
        "calculate_margin",
        "break_even_analysis",
        "roi_analysis",
    },
    "forecasting": {
        "demand_forecast",
        "stockout_prediction",
        "reorder_recommendation",
    },
    "marketplace": {
        "marketplace_fee_lookup",
        "settlement_calculator",
    },
    "inventory": {
        "inventory_health_check",
        "inventory_turnover",
    },
    "fulfillment": {
        "shipping_cost_estimator",
        "fulfillment_recommendation",
    },
    "pricing": {
        "competitor_gap_analysis",
        "dynamic_pricing",
    },
}


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    failures = []
    for domain, skill_names in EXPECTED_SKILLS.items():
        domain_path = ROOT / "skills" / domain
        if not domain_path.is_dir():
            failures.append(f"Missing domain directory: {domain_path}")
            continue
        for skill_name in sorted(skill_names):
            skill_path = domain_path / skill_name
            required_paths = [
                skill_path / "README.md",
                skill_path / "interface.json",
                skill_path / "mcp.md",
                skill_path / "examples",
            ]
            for required_path in required_paths:
                if not required_path.exists():
                    failures.append(f"Missing skill artifact: {required_path}")
            if not (skill_path / "examples").is_dir():
                continue
            examples = sorted((skill_path / "examples").glob("*.json"))
            if not examples:
                failures.append(f"Missing JSON examples: {skill_path / 'examples'}")
            for example in examples:
                load_json(example)
            interface_path = skill_path / "interface.json"
            if interface_path.exists():
                interface = load_json(interface_path)
                if interface.get("name") != skill_name:
                    failures.append(f"{interface_path}: name must be {skill_name}")
                if interface.get("domain") != domain:
                    failures.append(f"{interface_path}: domain must be {domain}")
                for key in ["version", "description", "input_schema", "output_schema", "agent_compatibility"]:
                    if key not in interface:
                        failures.append(f"{interface_path}: missing {key}")

    found = {
        domain_path.name: {path.name for path in domain_path.iterdir() if path.is_dir()}
        for domain_path in (ROOT / "skills").iterdir()
        if domain_path.is_dir()
    }
    for domain, skill_names in found.items():
        unexpected = skill_names - EXPECTED_SKILLS.get(domain, set())
        if unexpected:
            failures.append(f"Unexpected skills in {domain}: {', '.join(sorted(unexpected))}")

    if failures:
        raise SystemExit("\n".join(failures))

    print("Validated 15 commerce skills")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
