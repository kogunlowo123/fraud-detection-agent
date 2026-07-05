# Fraud Detection Agent

[![CI](https://github.com/kogunlowo123/fraud-detection-agent/actions/workflows/ci.yml/badge.svg)](https://github.com/kogunlowo123/fraud-detection-agent/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)

> **Category**: Finance | **Cloud**: MULTI-CLOUD | **LLM**: gpt-4o

Financial fraud detection agent that analyzes transactions for anomalies, calculates risk scores, flags suspicious patterns, manages investigation workflows, and generates SAR reports.

---

## Domain-Specific Tools

| Tool | Description |
|------|-------------|
| `analyze_transaction` | Analyze a financial transaction for fraud indicators |
| `calculate_risk_score` | Calculate fraud risk score using ML models and rules |
| `flag_anomaly` | Flag a suspicious transaction pattern for investigation |
| `manage_investigation` | Manage fraud investigation workflow and evidence collection |
| `generate_sar` | Generate Suspicious Activity Report for regulatory filing |

## API Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `POST` | `/api/v1/fraud-detection/process` | Process transaction |
| `POST` | `/api/v1/fraud-detection/analyze` | Analyze data |
| `POST` | `/api/v1/fraud-detection/validate` | Validate |
| `POST` | `/api/v1/fraud-detection/report` | Generate report |
| `GET` | `/api/v1/fraud-detection/audit` | Get audit trail |

## Features

- Fraud
- Detection
- Compliance
- Reporting

## Integrations

- Netsuite
- Quickbooks
- Xero
- Sap
- Oracle Financials

## Architecture

```
fraud-detection-agent/
├── src/
│   ├── agent/              # Domain-specific agent logic
│   │   ├── fraud_detection_agent_agent.py  # Main agent with domain tools
│   │   ├── tools.py        # 5 domain-specific tools
│   │   └── prompts.py      # Expert system prompts
│   ├── api/                # FastAPI routes
│   │   └── routes/
│   │       ├── domain.py   # 5 domain-specific endpoints
│   │       └── health.py   # Health check
│   ├── connectors/         # 5 integration connectors
│   ├── config/             # Settings and configuration
│   ├── models/             # Domain-specific Pydantic schemas
│   ├── rag/                # RAG pipeline
│   ├── mcp/                # MCP server
│   └── a2a/                # Agent-to-agent protocol
├── tests/
├── infrastructure/         # Terraform, K8s, Helm, Docker
├── dashboard/              # Next.js frontend
└── docs/                   # Architecture and deployment docs
```

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Run
make dev

# Test
make test

# Docker
docker compose up -d
```

## Primary Service

**ERP + Accounting Platform + LLM**

---

Built as part of the Enterprise AI Agent Platform.
