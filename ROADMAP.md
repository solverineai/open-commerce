# Roadmap

## Phase 1: Marketplace Economics Dataset

- Define dataset structure for marketplace fees, shipping costs, settlement rules, return costs, and advertising costs.
- Add starter datasets for Korea and global marketplaces.
- Establish source-reference and version-history requirements.
- Invite community contributions for verified provider economics.

## Phase 2: Commerce Skill Library

- Stabilize first-party skill directories under `skills/`.
- Define interface specifications for profitability, forecasting, marketplace, inventory, fulfillment, and pricing skills.
- Add examples and tests for core skill payloads.
- Prepare skills for agent framework wrappers.

## Phase 3: Commerce Agent SDK

- Stabilize Python SDK surfaces.
- Add adapters for LangGraph, n8n, OpenAI Codex, Claude Code, and commerce automation systems.
- Provide package-level examples that compose datasets, schemas, prompts, and skills.

## Phase 4: Commerce MCP Server

- Convert stable skills into MCP tools.
- Add schema-compatible tool input and output payloads.
- Add safety guidance for advisory tools versus action tools.

## Phase 5: Autonomous Commerce Infrastructure

- Support autonomous commerce analysis loops.
- Add policy, confidence, and human-approval guardrails.
- Build a durable ecosystem around commerce skills, datasets, prompts, and standards.
