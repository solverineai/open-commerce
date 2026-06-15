"""Validate Codex, Claude, discovery, and MCP package entrypoints."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Iterable

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")

REQUIRED_FILES = [
    "AGENTS.md",
    "CLAUDE.md",
    "CITATION.cff",
    "llms.txt",
    "mkdocs.yml",
    ".agents/plugins/marketplace.json",
    ".claude-plugin/marketplace.json",
    "plugins/codex/open-commerce/.codex-plugin/plugin.json",
    "plugins/codex/open-commerce/.mcp.json",
    "plugins/claude/open-commerce/.claude-plugin/plugin.json",
    "plugins/claude/open-commerce/.mcp.json",
    "src/opencommerce_mcp/server.py",
    "docs/agent-packages.md",
    "docs/mcp-server.md",
]

SKILL_ROOTS = [
    ".agents/skills",
    ".claude/skills",
    "plugins/codex/open-commerce/skills",
    "plugins/claude/open-commerce/skills",
]

EXPECTED_SKILLS = {
    "open-commerce-profitability",
    "open-commerce-marketplace-economics",
}


def load_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def parse_frontmatter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter")
    end = text.find("\n---\n", 4)
    if end == -1:
        raise ValueError("unclosed YAML frontmatter")
    values: dict[str, str] = {}
    for line in text[4:end].splitlines():
        if not line.strip():
            continue
        if ":" not in line:
            raise ValueError(f"invalid frontmatter line: {line}")
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def skill_dirs(root: Path) -> Iterable[Path]:
    if not root.is_dir():
        return []
    return sorted(path for path in root.iterdir() if path.is_dir() and not path.name.startswith("."))


def validate_skill_root(root: Path, failures: list[str]) -> None:
    found = {path.name for path in skill_dirs(root)}
    missing = sorted(EXPECTED_SKILLS - found)
    if missing:
        failures.append(f"{root}: missing skills: {', '.join(missing)}")
    for skill_path in skill_dirs(root):
        skill_md = skill_path / "SKILL.md"
        if not skill_md.exists():
            failures.append(f"{skill_path}: missing SKILL.md")
            continue
        try:
            frontmatter = parse_frontmatter(skill_md)
        except ValueError as exc:
            failures.append(f"{skill_md}: {exc}")
            continue
        name = frontmatter.get("name")
        description = frontmatter.get("description")
        if name != skill_path.name:
            failures.append(f"{skill_md}: frontmatter name must match directory name")
        if not name or SKILL_NAME_RE.fullmatch(name) is None:
            failures.append(f"{skill_md}: invalid skill name")
        if not description:
            failures.append(f"{skill_md}: missing description")
        if "[TODO:" in skill_md.read_text(encoding="utf-8"):
            failures.append(f"{skill_md}: contains TODO placeholder")


def validate_codex_plugin(failures: list[str]) -> None:
    manifest_path = ROOT / "plugins" / "codex" / "open-commerce" / ".codex-plugin" / "plugin.json"
    manifest = load_json(manifest_path)
    if manifest.get("name") != "open-commerce":
        failures.append(f"{manifest_path}: name must be open-commerce")
    if manifest.get("skills") != "./skills/":
        failures.append(f"{manifest_path}: skills must be ./skills/")
    if manifest.get("mcpServers") != "./.mcp.json":
        failures.append(f"{manifest_path}: mcpServers must be ./.mcp.json")
    if "interface" not in manifest:
        failures.append(f"{manifest_path}: missing interface metadata")


def validate_claude_plugin(failures: list[str]) -> None:
    manifest_path = ROOT / "plugins" / "claude" / "open-commerce" / ".claude-plugin" / "plugin.json"
    manifest = load_json(manifest_path)
    if manifest.get("name") != "open-commerce":
        failures.append(f"{manifest_path}: name must be open-commerce")
    if manifest.get("skills") != "./skills/":
        failures.append(f"{manifest_path}: skills must be ./skills/")


def validate_marketplaces(failures: list[str]) -> None:
    for relative_path in [".agents/plugins/marketplace.json", ".claude-plugin/marketplace.json"]:
        path = ROOT / relative_path
        marketplace = load_json(path)
        plugins = marketplace.get("plugins", [])
        names = {plugin.get("name") for plugin in plugins if isinstance(plugin, dict)}
        if "open-commerce" not in names:
            failures.append(f"{path}: missing open-commerce plugin entry")


def main() -> int:
    failures: list[str] = []
    for relative_path in REQUIRED_FILES:
        if not (ROOT / relative_path).exists():
            failures.append(f"Missing required agent package file: {relative_path}")

    for relative_root in SKILL_ROOTS:
        validate_skill_root(ROOT / relative_root, failures)

    if not failures:
        validate_codex_plugin(failures)
        validate_claude_plugin(failures)
        validate_marketplaces(failures)

    if failures:
        raise SystemExit("\n".join(failures))

    print("Agent package checks passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
