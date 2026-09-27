# AI Council — Autonomous Security & Compliance Auditor

[![Python](https://img.shields.io/badge/Python-3.12%2B-blue)](https://www.python.org/)
[![LLMs](https://img.shields.io/badge/LLMs-local%20via%20Ollama-0f766e)](https://ollama.com)
[![Framework](https://img.shields.io/badge/orchestration-LangChain-1c3c3c)](https://python.langchain.com)

An agentic framework that automates the vulnerability-management lifecycle with **local LLMs** — turning raw scan logs into an audit-ready report without sending a single byte to the cloud. It demonstrates **heterogeneous multi-agent orchestration**: three specialized models, each chosen for its job, chained from raw findings to executive summary.

> Built as the capstone for an **M.S. in Artificial Intelligence**. All inference runs offline via Ollama — a deliberate choice for sensitive security logs.

## The council

A sequential chain where each agent's output feeds the next:

| Agent | Model | Job |
| --- | --- | --- |
| **Technical Auditor** | `llama3.2` | Fast triage, then identifies the top vulnerabilities and maps each to a **MITRE ATT&CK** technique ID (e.g. `T1190`) |
| **Compliance Strategist** | `deepseek-r1:7b` | Reasoning-heavy analysis of legal/regulatory liability under **GDPR** and **PCI-DSS** |
| **Remediation Engineer** | `qwen2.5-coder:7b` | Generates the exact Linux/Unix commands to fix each finding |

## How it works

```
logs/*.txt
   │
   ▼  Phase 0 — Triage       (skip logs with no vulnerabilities)
   ▼  Phase 1 — Audit        (top findings + MITRE ATT&CK IDs)
   ▼  Phase 2 — Compliance   (GDPR / PCI-DSS liability)
   ▼  Phase 3 — Remediation  (exact fix commands)
   │
   ▼  output/Audit_<log>_<time>.md         (one report per log)
   ▼  output/EXECUTIVE_SUMMARY_<date>.md   (portfolio-wide overview)
```

## Key features

- **Local-first inference** — runs entirely offline through Ollama; sensitive scan data never leaves the machine.
- **MITRE ATT&CK mapping** — every finding is tagged with its technique ID, so results slot straight into a detection-engineering workflow.
- **Intelligent triage** — clean logs are detected and skipped before spending model time on them.
- **Output sanitization** — a regex pass strips DeepSeek's internal `<think>…</think>` reasoning tags and normalizes whitespace so reports read professionally.
- **Batch + executive reporting** — per-log Markdown audits plus a consolidated executive summary across every system scanned.

## Setup

**Prerequisites:** [Ollama](https://ollama.com) running locally, and Python 3.12+.

```bash
# 1. Pull the three models
ollama pull llama3.2
ollama pull deepseek-r1:7b
ollama pull qwen2.5-coder:7b

# 2. Install dependencies
pip install -r requirements.txt

# 3. Drop scan logs (.txt) into ./logs, then run
python main.py
```

Reports are written to `./output/`.

## Project structure

```text
AI_COUNCIL_GIT/
├── main.py            # coordinator: triage → audit → compliance → remediation → reports
├── tools.py           # SecurityTools.read_scan_log — reads a scan log
├── generate_tests.py  # helper to generate sample scan logs
├── requirements.txt   # langchain-ollama, langchain-core
├── logs/              # input scan logs (.txt)  — you provide
└── output/            # generated audit reports (.md) — created on first run
```

## Disclaimer

A learning and demonstration project. Point it only at scan data you are authorized to analyze; generated remediation commands should be reviewed by a human before they are run against any system.
