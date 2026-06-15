# Security Policy

Open Commerce is an open source standards and tooling project. It should not contain production secrets, customer PII, private marketplace credentials, or non-public commercial agreements.

## Reporting

Please report suspected security issues privately to the maintainers listed in [MAINTAINERS.md](MAINTAINERS.md). Do not open a public issue for vulnerabilities or sensitive data exposure.

## Scope

In scope:

- Vulnerabilities in validation tools, SDK code, or example workflows.
- Accidental exposure of secrets or private data in repository assets.
- Unsafe agent prompt behavior that could cause credential exposure or irreversible commerce operations.

Out of scope:

- Unverified claims about third-party marketplace policies.
- Bugs in external OMS, ERP, WMS, or marketplace connector systems.

## Data Handling

Examples and tests must use synthetic data only. Do not contribute live customer records, API keys, marketplace tokens, or private settlement reports.
