# 🌍 Cross-Cultural Affiliate Network Management Skills

<p align="center">
  <strong>Tencent Cloud Hackathon 2026 · AI Agent Skill Track</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue" alt="Version">
  <img src="https://img.shields.io/badge/license-MIT-green" alt="License">
  <img src="https://img.shields.io/badge/skills-15-orange" alt="Skills Count">
  <img src="https://img.shields.io/badge/platform-AI%20Agent-purple" alt="Platform">
</p>

---

## 📖 项目简介 (Project Introduction)

As a cross-border affiliate network operator managing **20+ traffic channels** and **50+ apps** across **MENA, LATAM, APAC, and Europe&US**, we face three core operational challenges:

1. **Highly repetitive data processing** — Weekly report cleaning takes 3-5 hours manually
2. **Low cross-cultural communication efficiency** — Language barriers cause 5-8 email round-trips per issue
3. **Experience-driven budget allocation** — 20-30% budget wasted on low-quality traffic

This project encapsulates affiliate operations knowledge into **15 reusable AI Agent Skills** with a **five-layer architecture**:

```
Global Affiliate Ops Agent
├── Layer 1 — DataOps Automation (Data Extraction & Validation)
│   ├── CRM Channel Extraction          — Extract & filter channel data from MMP CSV
│   ├── CRM Settlement Verification      — Auto-reconcile settlement data
│   ├── Multi-MMP Attribution Engine    — Deduplicate & normalize channel variants
│   └── Cross-Regional Revenue Audit    — Full P&L analysis across regions
│
├── Layer 2 — Business Intelligence (Analysis & Insights)
│   ├── Wish Intelligence Collector     — Parse multi-format Wish Lists → tracking table
│   ├── Regional Wish Classifier        — Auto-classify offers by geo-region (5 zones)
│   ├── AI Budget Allocation Optimizer  — Data-driven budget distribution
│   ├── Conversion Funnel Intelligence — Funnel bottleneck detection & CAP planning
│   ├── Geo Market Intelligence Engine  — Multi-region market intel aggregation
│   └── Macroeconomic Monitoring Agent — Daily macro data tracking & alerting
│
├── Layer 3 — Anti-Fraud & Reporting (Specialized Workflows)
│   ├── PA Channel Export               — Generate anti-fraud reports for partners
│   └── PA Report Workflow              — Weekly PA HTML report update pipeline
│
├── Layer 4 — Cross-Cultural Collaboration (Core Differentiator)
│   └── Cross-Cultural Negotiation Copilot — BR↔CN communication style adapter
│
└── Layer 5 — AI Organization Behavior 🆕 (Core Innovation)
    ├── Partner Memory System           — 10-dimension partner memory for AI agents
    └── Relationship Health Score       — Real-time partner health scoring (0-100)
```

## ✨ 核心亮点 (Key Highlights)

| 维度 | 说明 |
|------|------|
| **🏭 生产验证** | 所有 Skill 基于真实运营场景开发，已在日常工作中投入使用 |
| **🧩 模块化架构** | 五层解耦，新增区域/Vertical 只需添加对应 Skill |
| **🌍 跨文化差异化** | Layer 4 解决巴西↔中国沟通痛点，Layer 5 AI 记忆+健康度为独家能力 |
| **⚡ 即插即用** | 每个 SKILL.md 内嵌完整可执行 Python 脚本，AI Agent 可直接调用 |
| **🔧 编码自适应** | 自动处理 utf-8-sig/GBK/BOM，消除跨平台乱码 |
| **📊 数据驱动** | 业务规则来自真实运营经验，非通用 Prompt |

## 🚀 快速开始 (Quick Start)

### Prerequisites

- Python 3.8+
- Git

### Installation

```bash
# Clone the repository
git clone https://github.com/Ameko2026/affiliate-skills-hackathon2026.git
cd affiliate-skills-hackathon2026

# Install dependencies
pip install -r requirements.txt
```

### Usage with AI Agent Platform

Each skill is a self-contained `SKILL.md` file that can be loaded by any AI Agent platform supporting the OpenClaw / WorkBuddy skill format:

```bash
# Copy individual skills to your agent's skills directory
cp -r skills/wish-intelligence-collector ~/.your-agent/skills/
cp -r skills/crm-channel-extraction ~/.your-agent/skills/
# ... or copy all at once
cp -r skills/* ~/.your-agent/skills/
```

### Run Scripts Standalone

Each skill includes executable Python scripts that can run independently:

```bash
# Example: Parse a Wish List file
python3 scripts/parse_wish_list.py --input data/sample_wish_list.csv --output output/tracking_table.xlsx

# Example: Generate a regional classification report
python3 scripts/classify_geo.py --input data/wish_data.xlsx --output output/regional_report.xlsx
```

## 📁 项目结构 (Project Structure)

```
affiliate-skills-hackathon2026/
├── README.md                          # This file
├── LICENSE                            # MIT License
├── .gitignore                         # Git ignore rules
├── requirements.txt                   # Python dependencies
│
├── skills/                            # 🔑 Core: 13 Skill definitions
│   ├── wish-intelligence-collector/     #   Layer 2 - BI
│   │   ├── SKILL.md
│   │   └── scripts/                    #   Bundled resources
│   ├── regional-wish-classifier/      #   Layer 2 - BI
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── multi-mmp-attribution-engine/  #   Layer 1 - DataOps
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── cross-regional-revenue-audit/  #   Layer 1 - DataOps
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── ai-budget-optimizer/           #   Layer 1 - DataOps
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── conversion-funnel-intelligence/ #   Layer 2 - BI
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── macro-monitoring-agent/        #   Layer 1 - DataOps
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── geo-market-intel-engine/     #   Layer 2 - BI
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── crm-channel-extraction/      #   Layer 1 - DataOps
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── crm-settlement-verification/ #   Layer 1 - DataOps
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── pa-channel-export/           #   Layer 3 - Anti-Fraud
│   │   ├── SKILL.md
│   │   └── scripts/
│   ├── pa-report-workflow/         #   Layer 3 - Anti-Fraud
│   │   ├── SKILL.md
│   │   └── scripts/
│   └── cross-cultural-negotiation-copilot/  # Layer 4 - Collaboration
│       ├── SKILL.md
│       └── scripts/
│
├── scripts/                           # Executable Python scripts
│   ├── parse_wish_list.py
│   ├── classify_geo.py
│   ├── attribution_dedup.py
│   ├── app_a_report.py
│   ├── budget_analysis.py
│   ├── funnel_analysis.py
│   ├── macro_monitor.py
│   ├── market_intel.py
│   ├── extract_channel.py
│   ├── verify_settlement.py
│   ├── export_pa_by_channel.py
│   ├── generate_week_data.py
│   └── inject_data.py
│
├── templates/                         # Excel templates
│   └── [company]_region_template.xlsx
│
├── demo/                              # App Dactive web demo
│   ├── app.py                         # Streamlit main app
│   └── requirements-demo.txt
│
├── docs/                              # Additional documentation
│   ├── ARCHITECTURE.md
│   ├── API_REFERENCE.md
│   └── SUBMISSION_GUIDE.md
│
└── tests/                             # Unit tests
    ├── test_classification.py
    ├── test_attribution.py
    └── test_budget.py
```

## 📋 Skill 清单 (Skills Inventory)

| # | Skill Name | Layer | Category | Status |
|---|-----------|-------|----------|--------|
| 1 | **Wish Intelligence Collector** | L2 | BI | ✅ Production |
| 2 | **Regional Wish Classifier** | L2 | BI | ✅ Production |
| 3 | **Multi-MMP Attribution Engine** | L1 | DataOps | ✅ Production |
| 4 | **Cross-Regional Revenue Audit** | L1 | DataOps | ✅ Production |
| 5 | **AI Budget Allocation Optimizer** | L1 | DataOps | ✅ Production |
| 6 | **Conversion Funnel Intelligence** | L2 | BI | ✅ Production |
| 7 | **Macroeconomic Monitoring Agent** | L1 | DataOps | ✅ Production |
| 8 | **Geo Market Intelligence Engine** | L2 | BI | ✅ Production |
| 9 | **CRM Channel Extraction** | L1 | DataOps | ✅ Production |
| 10 | **CRM Settlement Verification** | L1 | DataOps | ✅ Production |
| 11 | **PA Channel Export** | L3 | Anti-Fraud | ✅ Production |
| 12 | **PA Report Workflow** | L3 | Anti-Fraud | ✅ Production |
| 13 | **Cross-Cultural Negotiation Copilot** | L4 | Collaboration | ✅ Production |

## 🛠️ 技术栈 (Tech Stack)

| Component | Technology |
|-----------|-----------|
| Skill Format | SKILL.md (OpenClaw / WorkBuddy compatible) |
| Scripting Language | Python 3.8+ |
| Data Processing | pandas, openpyxl |
| Web Demo | [Streamlit Cloud](https://affiliate-skills-hackathon2026.streamlit.app/) |
| Version Control | Git + GitHub |
| License | MIT |

## 📊 应用效果 (Impact)

| Metric | Before | After | Improvement |
|---------|--------|-------|-------------|
| Monthly reconciliation time | ~1 day | ~30 min | **95% faster** |
| Budget allocation method | Experience-driven | Data-driven | **20-30% waste eliminated** |
| Cross-cultural email round-trips | 5-8 times | 1-2 times | **80% reduction** |
| Weekly report generation | 3-5 hours manual | Automated | **Near-zero manual effort** |

## 🤝 Contributing

This is a hackathon submission. For feedback or collaboration, please contact the team through the hackathon platform.

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <sub>Built for <strong>Tencent Cloud Hackathon 2026</strong> · AI Agent Skill Track</sub>
</p>
<p align="center">
  <sub>🌍 Empowering cross-border affiliate operations through AI automation</sub>
</p>
