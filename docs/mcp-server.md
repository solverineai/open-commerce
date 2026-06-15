# MCP Server

Open Commerce includes an early Python MCP server for source-aware commerce economics workflows.

## Install

```bash
python -m pip install -e ".[mcp]"
```

## Run

```bash
OPENCOMMERCE_DATASETS=./datasets python -m opencommerce_mcp.server
```

The server resolves datasets from `OPENCOMMERCE_DATASETS` when set. If that variable is not set, it searches for a local `datasets/` directory from the current working directory and package location.

## Tools

- `calculate_profit`: Run deterministic profitability calculations with explicit cost inputs.
- `list_datasets`: List available economics datasets and their trust status.
- `get_economics_dataset`: Return a provider economics dataset with source references and safety warnings.
- `explain_dataset_status`: Explain how agents may use `starter`, `draft`, `reviewed`, `stable`, and `deprecated` data.

## Safety Rules

- `starter` data is structural only and must not be treated as verified economics.
- `draft` data may be used for analysis only when source IDs, version, and confidence warnings are returned.
- Account-specific, contract-specific, campaign-specific, and calculator-dependent values must be collected from the seller account or official provider calculator before automated action.
