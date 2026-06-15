# Contributing to Open Commerce

Open Commerce prioritizes documentation, governance, community contributions, dataset quality, and long-term ecosystem growth before advanced implementation.

## Contribution Types

- Dataset updates for marketplace, logistics, payment, and advertising economics.
- JSON Schema improvements.
- Profit engine calculations and test cases.
- Forecast interface examples.
- Agent prompt assets.
- Documentation, governance, and contributor experience improvements.

## Dataset Contributions

Dataset changes must include:

- The affected provider and dataset type.
- The field being changed.
- Source references with publisher, title, URL when available, and access date.
- Version history explaining the change.
- A note on whether values are official, inferred, estimated, or community-reported.

Do not submit unsupported fee or settlement values as stable data. If a value is useful but not yet verified, mark it as `starter`, `draft`, or `needs-source`.

## Schema Contributions

Schema changes must remain:

- JSON serializable.
- AI-agent friendly.
- LangGraph compatible.
- MCP compatible.
- Backward compatible unless the proposal includes a migration note.

## Development Setup

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m unittest discover -s tests -p "test*.py"
python tools/validate_schemas.py
python tools/validate_skills.py
python tools/validate_datasets.py
python tools/validate_markdown.py
python tools/validate_contribution.py
```

## Pull Request Checklist

- Tests or validation commands were run locally.
- Dataset changes include source references and version history.
- Schema changes include examples or documentation updates.
- Documentation changes avoid marketing claims that the project cannot support.
- The PR explains user impact, compatibility impact, and review focus.

## Community Conduct

Participation is governed by [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
