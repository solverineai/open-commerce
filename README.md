# Open Commerce

Open Commerce is the open standard and economic intelligence layer for AI-native commerce. Commerce has OMS, ERP, and WMS. AI-native commerce needs a Profit Layer, Forecast Layer, and Economic Intelligence Layer. Open Commerce aims to become that foundation.

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
| `.agents/skills/` | Codex-compatible repo-scoped Agent Skills. |
| `.claude/skills/` | Claude Code-compatible project skills. |
| `plugins/` | Codex and Claude plugin packages with skills and MCP configuration. |
| `src/opencommerce_mcp/` | Early MCP server entrypoint for agent tools. |
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
python tools/validate_agent_packages.py
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

Datasets use explicit trust status. `draft` datasets include official source references and representative platform values where public sources were confirmed, but they are not complete production-ready category tables. `starter` datasets are structural or source-discovery placeholders and must not be treated as verified economics.

See [docs/product-sale-skill-verification.md](docs/product-sale-skill-verification.md) for the current product-sale skill flow and platform-data verification matrix.

## Agent Packages

Open Commerce includes runtime entrypoints for coding agents and external AI systems:

- Codex skills: `.agents/skills/`
- Claude skills: `.claude/skills/`
- Codex plugin: `plugins/codex/open-commerce`
- Claude plugin: `plugins/claude/open-commerce`
- MCP server: `python -m opencommerce_mcp.server`

See [docs/agent-packages.md](docs/agent-packages.md) and [docs/mcp-server.md](docs/mcp-server.md).

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
