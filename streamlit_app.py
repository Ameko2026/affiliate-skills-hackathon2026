"""
Cross-Cultural Affiliate Network Management Skills - Streamlit Cloud Demo
Tencent Cloud Hackathon 2026 | AI Agent Skill Track

This is the entry point for Streamlit Cloud deployment.
Source: https://github.com/Ameko2026/affiliate-skills-hackathon2026
"""

import streamlit as st
import json

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
    ["🏠 Overview", "📦 Skills Explorer", "🏗️ Architecture", "🧠 Layer 5 Innovation", "📊 Impact Metrics", "🔧 Technical Details"],
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
        4. **No partner churn warning** — Discover partner loss when it's already too late
        """)

        st.markdown("""
        ### Our Solution
        A **15-Skill AI Agent Collection** organized in a **five-layer architecture** that encapsulates
        real affiliate operations knowledge into reusable, automated modules. **Layer 5 (AI Organization Behavior)**
        is our core innovation — AI that remembers partners and evaluates relationship health.
        """)

    with col2:
        st.metric("Total Skills", "15")
        st.metric("Architecture Layers", "5")
        st.metric("Production Validated", "9+ Skills")
        st.metric("AI Memory Dimensions", "10")
        st.markdown("""
        ---
        **Tech Stack**
        - Python 3.9+
        - pandas / openpyxl
        - AI Agent (SKILL.md format)
        - Streamlit Demo
        - MIT License
        """)

# ==================== VIEW: Skills Explorer ====================
elif view == "📦 Skills Explorer":
    st.header("Skills Explorer")
    st.markdown("Browse all 15 skills by layer. Click to expand details.")

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
            "name": "PA Channel Export",
            "tech": "pa-channel-export",
            "layer": "Layer 1 · DataOps Automation",
            "emoji": "🛡️",
            "status": "✅ Production",
            "desc": "Export PA anti-fraud data → styled Excel with highlighted fraud reason columns.",
            "triggers": ["PA 导出", "反作弊报告", "pa export"],
        },
        # Layer 2 - BI
        {
            "name": "Multi-MMP Attribution Engine",
            "tech": "multi-mmp-attribution-engine",
            "layer": "Layer 2 · Business Intelligence",
            "emoji": "🔄",
            "status": "✅ Production",
            "desc": "Deduplicate & normalize channel names across AppsFlyer/Adjust using Source Bank mapping.",
            "triggers": ["归因去重", "渠道变体合并", "MMP 数据清洗"],
        },
        {
            "name": "AI Budget Allocation Optimizer",
            "tech": "ai-budget-optimizer",
            "layer": "Layer 2 · Business Intelligence",
            "emoji": "📈",
            "status": "✅ Production",
            "desc": "Data-driven budget distribution using ROI analysis, attenuation models, and risk scoring.",
            "triggers": ["预算分配", "预算优化", "budget allocation"],
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
            "name": "Cross-Regional Revenue Audit",
            "tech": "cross-regional-revenue-audit",
            "layer": "Layer 2 · Business Intelligence",
            "emoji": "💰",
            "status": "✅ Production",
            "desc": "Full P&L audit integrating MMP + settlement + revenue data → 7-sheet Excel report.",
            "triggers": ["盈亏分析", "P&L 报告", "ROI 审计"],
        },
        {
            "name": "Macroeconomic Monitoring Agent",
            "tech": "macro-monitoring-agent",
            "layer": "Layer 2 · Business Intelligence",
            "emoji": "🌐",
            "status": "✅ Production",
            "desc": "Daily tracking of exchange rates, inflation, CPI across MENA/LATAM/APAC with smart alerts.",
            "triggers": ["宏观经济", "汇率监控", "macro monitor"],
        },
        # Layer 3 - Anti-Fraud
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
            "status": "✅ Production v2.0",
            "desc": "**Core differentiator** — AI generates culturally-appropriate partner communication drafts across 5 cultural zones.",
            "triggers": ["跨文化沟通", "邮件草稿", "谈判话术"],
        },
        # Layer 5 - AI Organization Behavior
        {
            "name": "Partner Memory System",
            "tech": "partner-memory-system",
            "layer": "Layer 5 · AI Organization Behavior ⭐",
            "emoji": "🧠",
            "status": "🆕 v1.0",
            "desc": "**Core Innovation** — AI remembers each partner's 10-dimension profile (communication style, reply speed, risk history, etc.).",
            "triggers": ["Partner 记忆", "合作伙伴档案", "partner memory"],
        },
        {
            "name": "Relationship Health Score",
            "tech": "relationship-health-score",
            "layer": "Layer 5 · AI Organization Behavior ⭐",
            "emoji": "💗",
            "status": "🆕 v1.0",
            "desc": "**Core Innovation** — AI evaluates each partner's relationship health (0-100 score) with 3-tier alerts and AI action suggestions.",
            "triggers": ["关系健康度", "健康度评分", "health score"],
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
    st.header("Five-Layer Architecture")

    st.markdown("""
    ```
    Global Affiliate Ops Agent
    │
    ├── Layer 1 — DataOps Automation (Data Extraction & Validation)
    │   ├── 🔧 CRM Channel Extraction
    │   ├── ✅ CRM Settlement Verification
    │   └── 🛡️ PA Channel Export
    │
    ├── Layer 2 — Business Intelligence (Analysis & Insights)
    │   ├── 🔄 Multi-MMP Attribution Engine
    │   ├── 💰 Cross-Regional Revenue Audit
    │   ├── 📈 AI Budget Allocation Optimizer
    │   ├── 🔄 Conversion Funnel Intelligence
    │   ├── 🎯 Geo Market Intelligence Engine
    │   ├── 📥 Wish Intelligence Collector
    │   ├── 🗺️ Regional Wish Classifier
    │   └── 🌐 Macroeconomic Monitoring Agent
    │
    ├── Layer 3 — Anti-Fraud & Reporting (Specialized Workflows)
    │   └── 📊 PA Report Workflow
    │
    ├── Layer 4 — Cross-Cultural Collaboration (Core Differentiator)
    │   └── 🤝 Cross-Cultural Negotiation Copilot v2.0
    │
    └── Layer 5 — AI Organization Behavior ⭐ (CORE INNOVATION)
        ├── 🧠 Partner Memory System
        └── 💗 Relationship Health Score
    ```
    """)

    st.markdown("### Layer Responsibilities")

    arch_data = [
        ("Layer 1", "DataOps Automation", "Raw data extraction, validation, cleaning, reconciliation",
         "CRM extraction, Settlement verify, PA export"),
        ("Layer 2", "Business Intelligence", "Analysis, classification, insights, intelligence gathering",
         "Attribution, Budget, Funnel, Market intel, Wish parsing, Geo classification, Revenue audit, Macro monitoring"),
        ("Layer 3", "Anti-Fraud & Reporting", "Specialized fraud detection workflows and reporting pipelines",
         "PA data export, PA weekly report generation"),
        ("Layer 4", "Cross-Cultural Collaboration", "Communication adaptation between cultural contexts",
         "Email drafting, Negotiation support, Style adaptation (BR/CN/EU/SEA/ME)"),
        ("Layer 5", "AI Organization Behavior ⭐", "AI memory + relationship evaluation + proactive alerts",
         "Partner Memory (10 dimensions), Health Score (0-100), 3-tier alerts"),
    ]

    for layer, name, desc, components in arch_data:
        with st.expander(f"**{layer}** — {name}"):
            st.markdown(f"*{desc}*")
            st.markdown(f"**Components**: {components}")

# ==================== VIEW: Layer 5 Innovation ====================
elif view == "🧠 Layer 5 Innovation":
    st.header("🧠 Layer 5: AI Organization Behavior")
    st.markdown("**CORE INNOVATION** — AI is no longer a tool, but a partner with memory and relationship awareness.")

    tab1, tab2, tab3 = st.tabs(["🧠 Partner Memory", "💗 Health Score", "🚀 AI Evolution"])

    with tab1:
        st.subheader("Partner Memory System")
        st.markdown("AI remembers each partner's **10-dimension profile**:")

        memory_dims = {
            "Dimension": ["Communication Style", "Reply Speed", "Risk History", "Negotiation Habit",
                          "Category Preference", "Timezone", "Emotion Style", "Contact Reliability",
                          "Call Preference", "Budget Cooperation"],
            "Values": ["soft/warm/aggressive/formal", "fast/medium/slow/dead",
                       "fraud/payment_delay/no_issues", "price_pressure/bonus_hunter/easy",
                       "finance/gaming/utility", "BRT/EST/CST",
                       "optimistic/pessimistic/dramatic", "always_online/intermittent/offline",
                       "voice_call/sms_only/async_only", "high/medium/low"],
        }
        st.dataframe(memory_dims, use_container_width=True, hide_index=True)

        st.markdown("### Before vs After")
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("#### ❌ Without Memory")
            st.markdown('> "Send the report now."')
            st.markdown("- Same tone for everyone")
            st.markdown("- Can't predict churn")
        with col2:
            st.markdown("#### ✅ With Memory")
            st.markdown('> "Hi [Partner], would you mind sharing the report when you have a moment? :)"')
            st.markdown("- Auto-adapt based on partner profile")
            st.markdown("- Proactive churn risk alert")

    with tab2:
        st.subheader("Relationship Health Score (0-100)")
        st.markdown("AI evaluates each partner's relationship health in real-time.")

        score_dims = {
            "Dimension": ["Reply Speed", "Emotional Stability", "Cooperation Level",
                          "Payment Timeliness", "Traffic Stability"],
            "Weight": ["20%", "25%", "20%", "15%", "20%"],
            "Data Source": ["Partner Memory.reply_speed", "Last 10 communications tone",
                            "Task completion rate", "Payment delay history", "Last 30 days traffic"],
        }
        st.dataframe(score_dims, use_container_width=True, hide_index=True)

        st.markdown("### Alert Thresholds")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("🟢 Healthy", "≥ 70", "Normal monitoring")
        with col2:
            st.metric("🟡 Attention", "50-70", "24h proactive check-in")
        with col3:
            st.metric("🔴 Alert", "< 50", "Immediate action + AI suggestion")

        st.markdown("### Demo Dashboard")
        partner_health = {
            "Partner": ["Hertzmobi", "AppTango", "GamePartner"],
            "Score": [85, 62, 35],
            "Status": ["🟢 Healthy", "🟡 Attention", "🔴 Alert"],
        }
        st.dataframe(partner_health, use_container_width=True, hide_index=True)
        st.warning("⚠️ GamePartner health dropped to 35 — AI suggests: call within 24h to discuss CAP adjustment needs")

    with tab3:
        st.subheader("AI Evolution Path")
        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown("### v1.0\n**Stateless Tool**")
            st.markdown("- Only analyzes data")
            st.markdown("- Doesn't know people")
            st.markdown("- Passive response")
            st.metric("Value", "Efficiency +90%")

        with col2:
            st.markdown("### v2.0\n**Stateful AI**")
            st.markdown("- Remembers partners")
            st.markdown("- Auto-adapts style")
            st.markdown("- Accumulates relationships")
            st.metric("Value", "Relationship +60%")

        with col3:
            st.markdown("### v3.0\n**Proactive AI Partner**")
            st.markdown("- Evaluates health")
            st.markdown("- Proactive alerts")
            st.markdown("- Prevents churn")
            st.metric("Value", "Risk Prevention")

# ==================== VIEW: Impact Metrics ====================
elif view == "📊 Impact Metrics":
    st.header("Impact & Results")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Reconciliation Time", "~30 min", "-95%", delta_color="inverse")
    with col2:
        st.metric("Report Automation", "100%", "Fully automated")
    with col3:
        st.metric("Email Round-trips", "1-2 times", "-80% reduction")
    with col4:
        st.metric("Churn Prediction", "+60%", "AI proactive alert")

    st.markdown("---")
    st.header("Before vs After Comparison")

    before_after = {
        "Metric": ["Monthly Reconciliation", "Budget Allocation", "Partner Communication",
                    "Weekly Reports", "Data Quality", "Churn Prediction"],
        "Before": ["~1 day manual", "Experience/gut feel", "5-8 email round trips",
                    "3-5 hours manual", "Inconsistent formats", "By experience only"],
        "After": ["~30 min automated", "Data-driven + ML models", "1-2 round trips",
                   "Near-zero manual effort", "Standardized schema", "AI proactive alerts"],
        "Improvement": ["96% faster", "20-30% waste cut", "80% reduction",
                        "Fully automated", "100% consistent", "60% improvement"],
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
├── streamlit_app.py                 # Streamlit Cloud entry point
├── skills/                          # 15 SKILL.md files
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
│   ├── cross-cultural-negotiation-copilot/SKILL.md
│   ├── partner-memory-system/SKILL.md       🆕
│   └── relationship-health-score/SKILL.md   🆕
├── demo/
│   └── app.py
└── submission/
    ├── intro_500words.md
    ├── technical_doc.md
    ├── ppt_deck.md
    └── video_script.md
        """, language="text")

    with tab2:
        st.code("""
pandas>=1.5.0          # Data processing
openpyxl>=3.1.0        # Excel read/write with styling
numpy>=1.24.0          # Numerical computations
requests>=2.28.0       # API calls (macro monitoring, market intel)
streamlit>=1.28.0      # Web demo
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
