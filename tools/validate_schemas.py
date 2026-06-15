"""Validate Open Commerce JSON Schema files and examples."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: Path) -> Dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def main() -> int:
    try:
        from jsonschema import Draft202012Validator
    except ImportError:
        Draft202012Validator = None

    schema_paths = sorted(ROOT.glob("schemas/*.schema.json"))
    schema_paths.append(ROOT / "datasets" / "economics-dataset.schema.json")

    if not schema_paths:
        raise SystemExit("No schema files found")

    for path in schema_paths:
        schema = load_json(path)
        required_keys = {"$schema", "$id", "title", "description", "type", "properties"}
        missing = sorted(required_keys - set(schema))
        if missing:
            raise SystemExit(f"{path}: missing schema keys: {', '.join(missing)}")
        if Draft202012Validator is not None:
            Draft202012Validator.check_schema(schema)

    if Draft202012Validator is not None:
        examples = [
            (ROOT / "schemas" / "profit.schema.json", ROOT / "examples" / "agent_payloads" / "profit_analysis.json"),
            (ROOT / "schemas" / "marketplace.schema.json", ROOT / "examples" / "datasets" / "marketplace_dataset_example.json"),
        ]
        for schema_path, example_path in examples:
            validator = Draft202012Validator(load_json(schema_path))
            errors = sorted(validator.iter_errors(load_json(example_path)), key=lambda err: list(err.path))
            if errors:
                messages = [f"{example_path}: {list(error.path)}: {error.message}" for error in errors]
                raise SystemExit("\n".join(messages))

    print(f"Validated {len(schema_paths)} schema files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
