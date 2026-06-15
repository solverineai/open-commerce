# Open Commerce

Open Commerce is an open-source collection of commerce skills, datasets, prompts, and standards for AI agents. Commerce software has OMS, ERP, and WMS, but AI-native commerce requires reusable skills, knowledge, economic intelligence, and agent tooling. Open Commerce aims to become the foundational commerce capability layer for AI Agents, LangGraph, MCP Servers, n8n, OpenAI Codex, Claude Code, and commerce automation systems.

The repository is designed to feel like LangChain for Commerce or an OpenAI Agents SDK for Commerce rather than a traditional OMS project. It prioritizes skills, datasets, documentation, community contributions, and agent interoperability before complex applications.

## Positioning

Open Commerce is not an OMS, ERP, WMS, or marketplace connector. It does not replace operational systems.

Open Commerce is:

- A commerce skill library.
- A marketplace economics dataset.
- A prompt library and schema standard.
- A capability layer for agentic commerce workflows.
- Infrastructure for AI agents, workflow engines, and future MCP servers.

Think of it as shared commerce capability infrastructure for agents.

## Project Modules

| Area | Purpose |
| --- | --- |
| `skills/` | Reusable commerce skills with README, examples, interface specs, and future MCP support notes. |
| `datasets/` | Starter marketplace, logistics, payment, and advertising economics datasets. |
| `schemas/` | JSON Schemas for profit, forecast, inventory, shipment, order, and related commerce records. |
| `prompts/` | Markdown prompt assets for commerce agents. |
| `examples/` | Runnable examples and agent payloads. |
| `docs/` | Architecture, dataset, schema, integration, and roadmap documentation. |
| `governance/` | Founder-led open source governance supported by Solverine. |
| `.github/` | Issue templates, PR templates, CODEOWNERS, labels, repository settings, and CI workflows. |

The repository also includes an early Python SDK and validation tools so contributors can test the first skill interfaces locally.

## Quick Start

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

Use the Python SDK:

```python
from opencommerce import ProfitEngine

engine = ProfitEngine()
result = engine.calculate_profit(
    selling_price=35000,
    product_cost=17000,
    marketplace_fee=3500,
    payment_fee=900,
    shipping_cost=3200,
    return_cost=0,
    ad_cost=2500,
)

print(result["net_profit"])
```

## Roadmap

- Phase 1: Marketplace Economics Dataset.
- Phase 2: Commerce Skill Library.
- Phase 3: Commerce Agent SDK.
- Phase 4: Commerce MCP Server.
- Phase 5: Autonomous Commerce Infrastructure.

See [ROADMAP.md](ROADMAP.md) for milestone details.

## Dataset Status

The initial datasets are intentionally marked as `starter`. They define the required shape for fee structures, settlement rules, shipping costs, return costs, metadata, source references, and version history. Contributors should replace TODO source references with verified official documentation before changing a dataset status to `reviewed` or `stable`.

## Governance

Open Commerce is a public Apache-2.0 open source project supported by Solverine and designed for community-driven contributions. Governance documents are available in:

- [GOVERNANCE.md](GOVERNANCE.md)
- [MAINTAINERS.md](MAINTAINERS.md)
- [ROADMAP.md](ROADMAP.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)

## Community

The project is designed for public GitHub Issues, Pull Requests, and Discussions with Wiki and Projects disabled. See [docs/community.md](docs/community.md) for recommended discussion categories and labels.

## License

Apache-2.0. See [LICENSE](LICENSE).
