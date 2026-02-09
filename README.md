# 🤖 AI Council: Autonomous Security & Compliance Auditor

An agentic AI framework designed to automate the vulnerability management lifecycle using local LLMs. Built as a capstone-level project for an MS in Artificial Intelligence.

## 🚀 The Architecture
This system utilizes a **Sequential Multi-Agent Chain** to move from raw data to executive-level reporting without human intervention.



### 🛠️ The Council Members
1. **The Technical Auditor (Llama 3.2):** High-speed parsing of Nmap/Security logs to identify CVEs and technical flaws.
2. **The Compliance Strategist (DeepSeek-R1 7B):** Reasoning-heavy agent that cross-references technical flaws with legal frameworks like **GDPR, HIPAA, and PCI-DSS**.

## 🛡️ Key Features
- **Local Inference:** Runs entirely offline via Ollama, ensuring 100% data privacy for sensitive security logs.
- **Sanitization Pipeline:** Implements custom Regex post-processing to handle stochastic LLM outputs and ensure report integrity.
- **Automated Reporting:** Generates timestamped, audit-ready Markdown reports.

## 📋 Setup
1. **Clone & Install:**
   ```bash
   pip install -r requirements.txt