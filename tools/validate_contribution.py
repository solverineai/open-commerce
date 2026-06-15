"""Validate community and contribution readiness files."""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "NOTICE",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "GOVERNANCE.md",
    "MAINTAINERS.md",
    "ROADMAP.md",
    "DECISION_PROCESS.md",
    ".github/CODEOWNERS",
    ".github/settings.yml",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/config.yml",
    ".github/ISSUE_TEMPLATE/dataset.yml",
    ".github/ISSUE_TEMPLATE/schema.yml",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/feature_request.yml",
    ".github/ISSUE_TEMPLATE/docs.yml",
    ".github/labels.yml",
]

REQUIRED_LABELS = {
    "good-first-issue",
    "help-wanted",
    "dataset",
    "schema",
    "forecast",
    "profit-engine",
    "marketplace",
    "documentation",
}


def main() -> int:
    missing = [path for path in REQUIRED_FILES if not (ROOT / path).exists()]
    if missing:
        raise SystemExit(f"Missing contribution files: {', '.join(missing)}")

    labels_text = (ROOT / ".github" / "labels.yml").read_text(encoding="utf-8")
    labels = set(re.findall(r"^- name: ([A-Za-z0-9_.-]+)$", labels_text, flags=re.MULTILINE))
    missing_labels = sorted(REQUIRED_LABELS - labels)
    if missing_labels:
        raise SystemExit(f"Missing required labels: {', '.join(missing_labels)}")

    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    required_phrase = "Open Commerce is an open-source collection of commerce skills, datasets, prompts, and standards for AI agents."
    if not readme.startswith("# Open Commerce\n\n" + required_phrase):
        raise SystemExit("README.md must open with the required positioning paragraph")

    print("Contribution readiness checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
