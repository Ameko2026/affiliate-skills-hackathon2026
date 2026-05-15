"""
Cross-Cultural Affiliate Network Management Skills - App Dactive Demo
Tencent Cloud Hackathon 2026 | AI Agent Skill Track
"""

import streamlit as st

st.set_page_config(
    page_title="Affiliate Skills Demo",
    page_icon="🌍",
    layout="wide",
)

# Header
st.title("🌍 Cross-Cultural Affiliate Network Management Skills")
st.markdown("**Tencent Cloud Hackathon 2026 · AI Agent Skill Track**")
st.markdown("---")

# Sidebar navigation
st.sidebar.header("Navigation")
view = st.sidebar.radio(
    "Select a section",
    ["🏠 Overview", "📦 Skills Explorer", "🏗️ Architecture", "📊 Impact Metrics", "🔧 Technical Details"],
)

# ==================== VIEW: Overview ====================
if view == "🏠 Overview":
    st.header("Project Overview")

    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        ### The Problem
        Cross-border affiliate network operators managing **20+ channels** and **50+ apps** 
        across **MENA, LATAM, APAC, and Europe&US** face three core challenges:
        
        1. **Highly repetitive data processing** — Weekly report cleaning takes 3-5 hours manually
        2. **Low cross-cultural communication efficiency** — Language barriers cause 5-8 email round-trips
        3. **Experience-driven budget allocation** — 20-30% budget wasted on low-quality traffic
        """)
        
        st.markdown("""
        ### Our Solution
        A **13-Skill AI Agent Collection** organized in a four-layer architecture that encapsulates
        real affiliate operations knowledge into reusable, automated modules.
        """)
    
    with col2:
        st.metric("Total Skills", "13")
        st.metric("Architecture Layers", "4")
        st.metric("Production Validated", "9+ Skills")
        st.markdown("""
        ---
        **Tech Stack**
        - Python 3.8+
        - pandas / openpyxl
        - AI Agent (SKILL.md format)
        - MIT License
        """)

# ==================== VIEW: Skills Explorer ====================
elif view == "📦 Skills Explorer":
    st.header("Skills Explorer")
    st.markdown("Browse all 13 skills by layer. Click to expand details.")
    
    skills_data = [
        # Layer 1 - DataOps
        {
            "name": "CRM Channel Extraction",
            "tech": "crm-channel-extraction",
            "layer": "Layer 1 · DataOps Automation",
            "emoji": "🔧",
            "status": "✅ Production",
            "desc": "Extract & filter channel data from AppsFlyer CSV/CRM databases with flexible conditions.",
            "triggers": ["提取渠道数据", "过滤渠道", "channel extraction"],
        },
        {
            "name": "CRM Settlement Verification",
            "tech": "crm-settlement-verification",
            "layer": "Layer 1 · DataOps Automation",
            "emoji": "✅",
            "status": "✅ Production",
            "desc": "Multi-step funnel validation of settlement data: primary attribution → transaction ID → channel → promotion window.",
            "triggers": ["结算核对", "对账", "settlement verify"],
        },
        {
            "name": "Multi-MMP Attribution Engine",
            "tech": "multi-mmp-attribution-engine",
            "layer": "Layer 1 · DataOps Automation",
            "emoji": "🔄",
            "status": "📋 Defined",
            "desc": "Deduplicate & normalize channel names across AppsFlyer/Adjust using Source Bank mapping.",
            "triggers": ["归因去重", "渠道变体合并", "MMP 数据清洗"],
        },
        {
            "name": "Cross-Regional Revenue Audit",
            "tech": "cross-regional-revenue-audit",
            "layer": "Layer 1 · DataOps Automation",
            "emoji": "💰",
            "status": "✅ Production",
            "desc": "Full P&L audit integrating MMP + settlement + revenue data → 7-sheet Excel report.",
            "triggers": ["盈亏分析", "P&L 报告", "ROI 审计"],
        },
        {
            "name": "AI Budget Allocation Optimizer",
            "tech": "ai-budget-optimizer",
            "layer": "Layer 1 · DataOps Automation",
            "emoji": "📈",
            "status": "✅ Production",
            "desc": "Data-driven budget distribution using ROI analysis, attenuation models, and risk scoring.",
            "triggers": ["预算分配", "预算优化", "budget allocation"],
        },
        {
            "name": "Macroeconomic Monitoring Agent",
            "tech": "macro-monitoring-agent",
            "layer": "Layer 1 · DataOps Automation",
            "emoji": "🌐",
            "status": "✅ Production",
            "desc": "Daily tracking of exchange rates, inflation, CPI across MENA/LATAM/APAC with smart alerts.",
            "triggers": ["宏观经济", "汇率监控", "macro monitor"],
        },
        # Layer 2 - BI
        {
            "name": "Wish Intelligence Collector",
            "tech": "wish-intelligence-collector",
            "layer": "Layer 2 · Business Intelligence",
            "emoji": "📥",
            "status": "✅ Production",
            "desc": "Parse multi-format Wish Lists (OCR/text/Excel) → standardized 8-column tracking table.",
            "triggers": ["解析 Wish List", "Wish List 转表格", "采集渠道Offer"],
        },
        {
            "name": "Regional Wish Classifier",
            "tech": "regional-wish-classifier",
            "layer": "Layer 2 · Business Intelligence",
            "emoji": "🗺️",
            "status": "✅ Production",
            "desc": "Auto-classify offers into 5 regional zones (MENA/LATAM/APAC/EU_US/Global).",
            "triggers": ["按区域分类", "Geo 分类", "regional classify"],
        },
        {
            "name": "Conversion Funnel Intelligence",
            "tech": "conversion-funnel-intelligence",
            "layer": "Layer 2 · Business Intelligence",
            "emoji": "🔄",
            "status": "📋 Defined",
            "desc": "Funnel bottleneck detection + CAP planning with color-coded effectiveness ratings.",
            "triggers": ["转化漏斗", "漏斗分析", "CAP 规划"],
        },
        {
            "name": "Geo Market Intelligence Engine",
            "tech": "geo-market-intel-engine",
            "layer": "Layer 2 · Business Intelligence",
            "emoji": "🎯",
            "status": "📋 Defined",
            "desc": "Multi-region market intel aggregation: top apps, trends, competitors, regulations.",
            "triggers": ["市场情报", "竞品动态", "geo intel"],
        },
        # Layer 3 - Anti-Fraud
        {
            "name": "PA Channel Export",
            "tech": "pa-channel-export",
            "layer": "Layer 3 · Anti-Fraud & Reporting",
            "emoji": "🛡️",
            "status": "✅ Production",
            "desc": "Export PA anti-fraud data → styled Excel with highlighted fraud reason columns.",
            "triggers": ["PA 导出", "反作弊报告", "pa export"],
        },
        {
            "name": "PA Report Workflow",
            "tech": "pa-report-workflow",
            "layer": "Layer 3 · Anti-Fraud & Reporting",
            "emoji": "📊",
            "status": "✅ Production",
            "desc": "Weekly pipeline: CSV collection → JS array generation → HTML report injection.",
            "triggers": ["PA 报告更新", "周报生成", "pa report workflow"],
        },
        # Layer 4 - Cross-Cultural
        {
            "name": "Cross-Cultural Negotiation Copilot",
            "tech": "cross-cultural-negotiation-copilot",
            "layer": "Layer 4 · Cross-Cultural Collaboration",
            "emoji": "🤝",
            "status": "📋 Defined",
            "desc": "**Core differentiator** — AI generates culturally-appropriate partner communication drafts.",
            "triggers": ["跨文化沟通", "邮件草稿", "谈判话术"],
        },
    ]
    
    for skill in skills_data:
        with st.expander(f"{skill['emoji']} **{skill['name']}** `{skill['status']}`"):
            cols = st.columns(3)
            cols[0].markdown(f"**Layer**: {skill['layer']}")
            cols[1].markdown(f"**Tech ID**: `{skill['tech']}`")
            cols[2].markdown(f"**Status**: {skill['status']}")
            st.markdown(f"**Description**: {skill['desc']}")
            st.markdown("**Trigger Keywords**: `" + "`, `".join(skill['triggers']) + "`")

# ==================== VIEW: Architecture ====================
elif view == "🏗️ Architecture":
    st.header("Four-Layer Architecture")
    
    st.markdown("""
    ```
    Global Affiliate Ops Agent
    │
    ├── Layer 1 — DataOps Automation (Data Extraction & Validation)
    │   ├── 🔧 CRM Channel Extraction
    │   ├── ✅ CRM Settlement Verification  
    │   ├── 🔄 Multi-MMP Attribution Engine
    │   ├── 💰 Cross-Regional Revenue Audit
    │   ├── 📈 AI Budget Allocation Optimizer
    │   └── 🌐 Macroeconomic Monitoring Agent
    │
    ├── Layer 2 — Business Intelligence (Analysis & Insights)
    │   ├── 📥 Wish Intelligence Collector
    │   ├── 🗺️ Regional Wish Classifier
    │   ├── 🔄 Conversion Funnel Intelligence
    │   └── 🎯 Geo Market Intelligence Engine
    │
    ├── Layer 3 — Anti-Fraud & Reporting (Specialized Workflows)
    │   ├── 🛡️ PA Channel Export
    │   └── 📊 PA Report Workflow
    │
    └── Layer 4 — Cross-Cultural Collaboration (Core Differentiator)
        └── 🤝 Cross-Cultural Negotiation Copilot
    ```
    """)
    
    st.markdown("### Layer Responsibilities")
    
    arch_data = [
        ("Layer 1", "DataOps Automation", "Raw data extraction, validation, cleaning, reconciliation",
         "CRM extraction, Settlement verify, Attribution, Revenue audit, Budget optimization, Macro monitoring"),
        ("Layer 2", "Business Intelligence", "Analysis, classification, insights, intelligence gathering",
         "Wish parsing, Geo classification, Funnel analysis, Market intel"),
        ("Layer 3", "Anti-Fraud & Reporting", "Specialized fraud detection workflows and reporting pipelines",
         "PA data export, PA weekly report generation"),
        ("Layer 4", "Cross-Cultural Collaboration", "Communication adaptation between cultural contexts",
         "Email drafting, Negotiation support, Style adaptation (BR↔CN)"),
    ]
    
    for layer, name, desc, components in arch_data:
        with st.expander(f"**{layer}** — {name}"):
            st.markdown(f"*{desc}*")
            st.markdown(f"**Components**: {components}")

# ==================== VIEW: Impact Metrics ====================
elif view == "📊 Impact Metrics":
    st.header("Impact & Results")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Reconciliation Time", "~30 min", "-95%", delta_color="inverse")
        st.caption("From ~1 day per month")
    
    with col2:
        st.metric("Budget Waste Eliminated", "20-30%", "Data-driven allocation")
    
    with col3:
        st.metric("Email Round-trips", "1-2 times", "-80% reduction")
    
    st.markdown("---")
    st.header("Before vs After Comparison")
    
    before_after = {
        "Metric": ["Monthly Reconciliation", "Budget Allocation Method", "Partner Communication", "Weekly Reports", "Data Quality"],
        "Before": ["~1 day manual", "Experience/gut feel", "5-8 email round trips", "3-5 hours manual", "Inconsistent formats"],
        "After": ["~30 min automated", "Data-driven + ML models", "1-2 round trips", "Near-zero manual effort", "Standardized schema"],
        "Improvement": ["95% faster", "20-30% waste cut", "80% reduction", "Fully automated", "100% consistent"],
    }
    
    st.dataframe(before_after, use_container_width=True)

# ==================== VIEW: Technical Details ====================
elif view == "🔧 Technical Details":
    st.header("Technical Details")
    
    tab1, tab2, tab3 = st.tabs(["File Structure", "Dependencies", "Integration"])
    
    with tab1:
        st.code("""
affiliate-skills-hackathon2026/
├── README.md
├── LICENSE (MIT)
├── .gitignore
├── requirements.txt
├── skills/                          # 13 SKILL.md files
│   ├── wish-intelligence-collector/SKILL.md
│   ├── regional-wish-classifier/SKILL.md
│   ├── multi-mmp-attribution-engine/SKILL.md
│   ├── cross-regional-revenue-audit/SKILL.md
│   ├── ai-budget-optimizer/SKILL.md
│   ├── conversion-funnel-intelligence/SKILL.md
│   ├── macro-monitoring-agent/SKILL.md
│   ├── geo-market-intel-engine/SKILL.md
│   ├── crm-channel-extraction/SKILL.md
│   ├── crm-settlement-verification/SKILL.md
│   ├── pa-channel-export/SKILL.md
│   ├── pa-report-workflow/SKILL.md
│   └── cross-cultural-negotiation-copilot/SKILL.md
├── scripts/                         # Executable Python scripts
├── templates/                       # Excel templates
├── demo/                            # This Streamlit app
│   └── app.py
├── docs/                            # Additional documentation
└── tests/                           # Unit tests
        """, language="text")
    
    with tab2:
        st.code("""
pandas>=1.5.0          # Data processing
openpyxl>=3.1.0        # Excel read/write with styling
numpy>=1.24.0          # Numerical computations
requests>=2.28.0       # API calls (macro monitoring, market intel)
# Optional:
scipy>=1.10.0          # Advanced optimization algorithms
apscheduler>=3.10.0    # Scheduling for macro monitor
beautifulsoup4>=4.12.0 # Web scraping for market intel
        """, language="python")
    
    with tab3:
        st.markdown("""
        ### How to Integrate These Skills
        
        Each `SKILL.md` follows the **OpenClaw / WorkBuddy skill format** and can be loaded by any compatible AI Agent platform.
        
        #### Step 1: Copy to your agent's skills directory
        ```bash
        cp -r skills/* ~/.your-agent/skills/
        ```
        
        #### Step 2: The agent auto-discovers skills via trigger keywords
        
        When a user says "解析这个 Wish List", the agent matches against `trigger_keywords` and loads the appropriate SKILL.md.
        
        #### Step 3: Follow the execution flow defined in each SKILL.md
        
        Each skill contains a complete execution flow that the agent follows step-by-step, including input/output schemas and validation rules.
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: gray;">
    <p>Built for <strong>Tencent Cloud Hackathon 2026</strong> · AI Agent Skill Track</p>
    <p>🌍 Empowering cross-border affiliate operations through AI automation</p>
    <p><a href="https://github.com/Ameko2026/affiliate-skills-hackathon2026">GitHub Repository</a> · MIT License</p>
</div>
""", unsafe_allow_html=True)
