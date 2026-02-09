# 🤖 AI Council: Autonomous Security & Compliance Auditor
#
An agentic AI framework designed to automate the vulnerability management lifecycle using local LLMs. This project demonstrates **Heterogeneous Agent Orchestration**, moving from raw scan data to executive-level reporting without human intervention.
#
#
#
## 🚀 System Architecture
This framework utilizes a **Sequential Multi-Agent Chain** to process data. Each agent is specialized for its specific task, optimizing both speed and reasoning depth.
#
### 🛠️ The Council Members
1. **Agent 1: The Technical Auditor (Llama 3.2)**
   * **Role**: High-speed technical parsing.
   * **Task**: Identifies CVEs, open ports, and technical misconfigurations.
2. **Agent 2: The Compliance Strategist (DeepSeek-R1 7B)**
   * **Role**: Reasoning-heavy legal and risk assessment.
   * **Task**: Analyzes liability under **GDPR, HIPAA, and PCI-DSS**.
3. **Agent 3: The Remediation Engineer (Llama 3.2)**
   * **Role**: Actionable solution engineering.
   * **Task**: Generates exact terminal commands and configuration patches to fix detected vulnerabilities.
#
## 🛡️ Key Features
* **Local-First Inference**: Runs entirely offline via **Ollama**, ensuring 100% data privacy—a critical requirement for sensitive security logs.
* **Post-Processing Sanitization**: Implements a custom Regex pipeline to handle stochastic LLM outputs, specifically filtering DeepSeek's internal `<think>` tags and normalizing whitespace for professional reporting.
* **Automated Reporting**: Generates timestamped, audit-ready Markdown reports consolidating technical findings and legal risks.
#
#--
#
## 📋 Setup & Installation
#
### 1. Prerequisites
* [Ollama](https://ollama.com/) installed and running.
* Python 3.12+
#
### 2. Install Dependencies
```powershell
pip install -r requirements.txt
3. Pull Required Models
PowerShell
ollama pull llama3.2
ollama pull deepseek-r1:7b
4. Run the Audit
Place your .txt scan logs into the /logs directory and execute:
#
PowerShell
python main.py
Consolidated reports will be generated in the /output folder.
#
🎓 About the Developer
This project was developed as a capstone-level implementation for a Master of Science in Artificial Intelligence (Graduating April 2026). It showcases the practical application of Agentic AI, local model deployment, and data engineering in a cybersecurity context.
#
#
### Next Step: `requirements.txt`
To ensure this works for anyone who clones it, create a file named `requirements.txt` in the same folder with this content:
#
```text
langchain-ollama
langchain-core