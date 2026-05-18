"""Generate PDF technical document for hackathon submission using fpdf2."""
from fpdf import FPDF
import os
import re

class HackathonPDF(FPDF):
    def header(self):
        if self.page_no() > 1:
            self.set_font("helvetica", "I", 8)
            self.set_text_color(150, 150, 150)
            self.cell(0, 8, "Cross-Cultural Affiliate Network Management Skills | Technical Document v2.0", align="C")
            self.ln(5)
            self.set_draw_color(6, 90, 130)
            self.line(10, self.get_y(), 200, self.get_y())
            self.ln(3)

    def footer(self):
        self.set_y(-15)
        self.set_font("helvetica", "I", 8)
        self.set_text_color(150, 150, 150)
        self.cell(0, 10, f"Page {self.page_no()}/{{nb}}", align="C")

    def chapter_title(self, title):
        self.set_font("helvetica", "B", 16)
        self.set_text_color(6, 90, 130)
        self.cell(0, 10, title, new_x="LMARGIN", new_y="NEXT")
        self.set_draw_color(2, 195, 154)
        self.set_line_width(0.8)
        self.line(10, self.get_y(), 80, self.get_y())
        self.set_line_width(0.2)
        self.ln(5)

    def section_title(self, title):
        self.set_font("helvetica", "B", 13)
        self.set_text_color(28, 114, 147)
        self.cell(0, 8, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(3)

    def subsection_title(self, title):
        self.set_font("helvetica", "B", 11)
        self.set_text_color(33, 41, 92)
        self.cell(0, 7, title, new_x="LMARGIN", new_y="NEXT")
        self.ln(2)

    def body_text(self, text):
        self.set_font("helvetica", "", 10)
        self.set_text_color(30, 41, 59)
        self.multi_cell(0, 5.5, text)
        self.ln(2)

    def bold_text(self, text):
        self.set_font("helvetica", "B", 10)
        self.set_text_color(6, 90, 130)
        self.multi_cell(0, 5.5, text)
        self.ln(1)

    def add_table(self, headers, rows, col_widths=None):
        if col_widths is None:
            col_widths = [190 / len(headers)] * len(headers)
        # Header
        self.set_font("helvetica", "B", 9)
        self.set_fill_color(6, 90, 130)
        self.set_text_color(255, 255, 255)
        for i, h in enumerate(headers):
            self.cell(col_widths[i], 7, h, border=1, fill=True, align="C")
        self.ln()
        # Rows
        self.set_font("helvetica", "", 9)
        self.set_text_color(30, 41, 59)
        fill = False
        for row in rows:
            if fill:
                self.set_fill_color(245, 247, 250)
            else:
                self.set_fill_color(255, 255, 255)
            max_h = 7
            for i, cell in enumerate(row):
                # Calculate needed height
                lines = self.multi_cell(col_widths[i], 7, str(cell), split_only=True)
                needed = len(lines) * 5.5
                if needed > max_h:
                    max_h = needed
            for i, cell in enumerate(row):
                self.cell(col_widths[i], 7, str(cell)[:60], border=1, fill=True)
            self.ln()
            fill = not fill
        self.ln(3)

    def code_block(self, code):
        self.set_font("courier", "", 8)
        self.set_fill_color(30, 41, 59)
        self.set_text_color(226, 232, 240)
        lines = code.strip().split("\n")
        for line in lines:
            self.cell(0, 4.5, f"  {line[:100]}", fill=True, new_x="LMARGIN", new_y="NEXT")
        self.set_text_color(30, 41, 59)
        self.ln(3)

    def quote_block(self, text):
        self.set_fill_color(240, 253, 244)
        self.set_draw_color(2, 195, 154)
        x = self.get_x()
        y = self.get_y()
        self.set_font("helvetica", "I", 10)
        self.set_text_color(30, 41, 59)
        self.set_x(15)
        self.multi_cell(180, 5.5, text, fill=True)
        # Draw left border
        self.line(13, y, 13, self.get_y())
        self.ln(3)


pdf = HackathonPDF()
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=20)

# ===== COVER PAGE =====
pdf.add_page()
pdf.ln(30)
pdf.set_font("helvetica", "B", 28)
pdf.set_text_color(6, 90, 130)
pdf.cell(0, 15, "Cross-Cultural Affiliate Network", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.set_font("helvetica", "B", 28)
pdf.set_text_color(2, 195, 154)
pdf.cell(0, 15, "Management Skill Collection", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(10)
pdf.set_font("helvetica", "", 14)
pdf.set_text_color(100, 100, 100)
pdf.cell(0, 8, "AI Agent-based Multi-Region Affiliate Automation System", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
pdf.set_draw_color(2, 195, 154)
pdf.set_line_width(0.8)
pdf.line(70, pdf.get_y(), 140, pdf.get_y())
pdf.set_line_width(0.2)
pdf.ln(10)
pdf.set_font("helvetica", "", 12)
pdf.cell(0, 7, "Tencent Cloud Hackathon 2026", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 7, "AI Agent Skill Track", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.ln(5)
pdf.cell(0, 7, "Technical Document v2.0", align="C", new_x="LMARGIN", new_y="NEXT")
pdf.cell(0, 7, "2026-05-15", align="C", new_x="LMARGIN", new_y="NEXT")

# ===== 1. Product Overview =====
pdf.add_page()
pdf.chapter_title("1. Product Overview")
pdf.section_title("1.1 Basic Information")
pdf.add_table(
    ["Item", "Content"],
    [
        ["Product Name", "Cross-Cultural Affiliate Network Management AI Agent Skills"],
        ["Track", "Tencent Cloud Hackathon 2026 - AI Agent Skill Track"],
        ["Platform", "CodeBuddy / WorkBuddy / OpenClaw"],
        ["Skills", "15 (incl. 2 Layer 5 new additions)"],
        ["Version", "v2.0"],
    ],
    [50, 140]
)
pdf.section_title("1.2 One-line Description")
pdf.body_text("Encapsulate cross-border affiliate operations knowledge into 15 reusable AI Agent Skills, achieving multi-region, multi-cultural, multi-MMP operational automation, with a new AI Organization Behavior layer that enables AI to \"remember people\" and \"evaluate relationships\".")

# ===== 2. Background & Pain Points =====
pdf.chapter_title("2. Background & Pain Points")
pdf.section_title("2.1 Business Background")
pdf.body_text("As a cross-border affiliate network company, we simultaneously serve three types of advertisers (Brazil/Europe/China), connect with three types of traffic sources (Brazil local, Chinese outbound DSP, Southeast Asian internet), and manage 20+ channels and 50+ apps.")
pdf.section_title("2.2 Three Core Pain Points")
pdf.add_table(
    ["Pain Point", "Manifestation", "Impact"],
    [
        ["Highly repetitive data processing", "5+ reports/week manual cleaning, dedup, merge, 3-5h each", "30% team time on repetitive tasks"],
        ["Low cross-cultural comms efficiency", "3 advertiser types x 3 traffic sources, 5-8 email rounds", "1-4h per communication"],
        ["Experience-driven budget allocation", "20+ channels, CAP based on gut feeling", "20-30% budget wasted"],
    ],
    [50, 70, 70]
)
pdf.section_title("2.3 Relationship Management Pain Points")
pdf.add_table(
    ["Pain Point", "Manifestation", "Impact"],
    [
        ["No partner churn warning", "Rely on experience, discover too late", "Lose quality channel relationships"],
        ["AI doesn't know people", "Every interaction is with a stranger", "AI efficiency greatly reduced"],
    ],
    [50, 70, 70]
)

# ===== 3. Solution Architecture =====
pdf.chapter_title("3. Solution Architecture")
pdf.section_title("3.1 Five-Layer Skill Architecture")
pdf.code_block("""Global Affiliate Ops Agent
|-- Layer 1 -- Data Connectors (Data Extraction & Validation)
|   |-- crm-channel-extraction
|   |-- crm-settlement-verification
|   +-- pa-channel-export
|
|-- Layer 2 -- Data Analytics (Business Intelligence)
|   |-- multi-mmp-attribution-engine
|   |-- ai-budget-optimizer
|   |-- conversion-funnel-intelligence
|   |-- geo-market-intel-engine
|   |-- wish-intelligence-collector
|   +-- regional-wish-classifier
|
|-- Layer 3 -- Anti-Fraud & Attribution
|   |-- pa-report-workflow
|   +-- cross-regional-revenue-audit
|
|-- Layer 4 -- Cross-Cultural Collaboration (Core Differentiator)
|   +-- cross-cultural-negotiation-copilot
|
+-- Layer 5 -- AI Organization Behavior (CORE INNOVATION)
    |-- partner-memory-system
    +-- relationship-health-score""")

pdf.section_title("3.2 Technical Architecture Principles")
pdf.add_table(
    ["Principle", "Description"],
    [
        ["Single Responsibility", "Each Skill solves one clear business problem"],
        ["Independently Executable", "Each Skill contains complete Python scripts"],
        ["Layer Decoupling", "Upper layers don't depend on lower layer implementations"],
        ["Progressive Enhancement", "Start with single Skill, expand to full automation"],
        ["Stateful AI", "Layer 5 Skills support memory accumulation and persistence"],
    ],
    [50, 140]
)

# ===== 4. Skill Details =====
pdf.add_page()
pdf.chapter_title("4. 15 Skills Detailed Description")

pdf.section_title("4.1 Layer 1 - Data Connectors")
pdf.subsection_title("crm-channel-extraction")
pdf.body_text("Function: Auto-extract channel names and amounts from OCR-identified settlement PDFs/images. Impact: 1-1.5h manual -> 3min auto.")

pdf.subsection_title("crm-settlement-verification")
pdf.body_text("Function: Auto-reconciliation, flag anomalies with >5% discrepancy. Impact: 2h manual -> 3min auto.")

pdf.subsection_title("pa-channel-export")
pdf.body_text("Function: Generate standardized PA format reports. Impact: 0.5-1h manual -> one-click export.")

pdf.section_title("4.2 Layer 2 - Data Analytics")
skills_l2 = [
    ("multi-mmp-attribution-engine", "Multi-MMP attribution dedup via Source Bank priority"),
    ("ai-budget-optimizer", "Channel effectiveness analysis with CAP suggestions (Green/Yellow/Red)"),
    ("conversion-funnel-intelligence", "5-stage funnel analysis with color-coded effectiveness ratings"),
    ("geo-market-intel-engine", "Multi-region market intelligence aggregation"),
    ("wish-intelligence-collector", "Multi-format Wish List parsing to standardized 8-column table"),
    ("regional-wish-classifier", "Auto-classify offers into 5 regional zones"),
    ("cross-regional-revenue-audit", "Full P&L audit: MMP + settlement + revenue -> 7-sheet Excel"),
    ("macro-monitoring-agent", "Daily FX/inflation/CPI tracking across regions with smart alerts"),
]
for name, desc in skills_l2:
    pdf.subsection_title(name)
    pdf.body_text(desc)

pdf.section_title("4.3 Layer 3 - Anti-Fraud & Attribution")
pdf.subsection_title("pa-report-workflow")
pdf.body_text("PA report automation workflow, supports week2/week3 data updates. Weekly pipeline: CSV collection -> JS array generation -> HTML report injection.")

pdf.section_title("4.4 Layer 4 - Cross-Cultural Collaboration")
pdf.subsection_title("cross-cultural-negotiation-copilot (v2.0)")
pdf.body_text("CORE DIFFERENTIATOR. AI generates culturally-appropriate partner communication drafts covering 5 cultural zones (Brazil, China, Europe, Southeast Asia, Middle East). Three strategies: Soft Wording, Validation Framing, Internal Coordination Positioning.")

# ===== 5. Layer 5 =====
pdf.add_page()
pdf.chapter_title("5. Layer 5: AI Organization Behavior")
pdf.quote_block("CORE INNOVATION - AI is no longer a passive tool, but evolves into an 'AI Business Manager' with memory and relationship evaluation capabilities.")

pdf.section_title("5.1 Design Philosophy")
pdf.add_table(
    ["Version", "Positioning", "Capability"],
    [
        ["v1.0", "Stateless Tool", "Only analyzes data, doesn't know people, passive response"],
        ["v2.0", "Stateful AI", "Remembers partner features, auto-adapts communication style"],
        ["v3.0", "Proactive AI Partner", "Evaluates relationship health, proactively warns of churn risk"],
    ],
    [30, 50, 110]
)

pdf.section_title("5.2 Partner Memory System")
pdf.body_text("AI partner memory system - from 'stateless tool' to 'AI Business Manager with memory'. 10 dimensions of partner information:")
pdf.add_table(
    ["Dimension", "Values", "Description"],
    [
        ["communication_style", "soft/warm/aggressive/formal", "Communication style"],
        ["reply_speed", "fast/medium/slow/dead", "Reply speed"],
        ["risk_history", "fraud/payment_delay/no_issues", "Risk history"],
        ["negotiation_habit", "price_pressure/bonus_hunter/easy", "Negotiation habit"],
        ["category_preference", "finance/gaming/utility", "Category preference"],
        ["timezone", "BRT/EST/CST", "Timezone"],
        ["emotion_style", "optimistic/pessimistic/dramatic", "Emotion style"],
        ["contact_reliability", "always_online/intermittent/offline", "Contact reliability"],
        ["call_preference", "voice_call/sms_only/async_only", "Call preference"],
        ["budget_cooperation", "high/medium/low", "Budget cooperation level"],
    ],
    [50, 65, 75]
)

pdf.section_title("5.3 Relationship Health Score")
pdf.body_text("AI relationship health scoring system - from 'monitoring data anomalies' to 'monitoring relationship anomalies'. Score range: 0-100.")
pdf.add_table(
    ["Dimension", "Weight", "Data Source", "Calculation"],
    [
        ["Reply speed", "20%", "Partner Memory.reply_speed", "Trend analysis"],
        ["Emotional stability", "25%", "Last 10 communications tone", "Variance calculation"],
        ["Cooperation level", "20%", "Task completion rate", "Ratio statistics"],
        ["Payment timeliness", "15%", "Payment delay history", "Weighted statistics"],
        ["Traffic stability", "20%", "Last 30 days traffic", "Standard deviation"],
    ],
    [40, 20, 65, 65]
)

pdf.subsection_title("Alert Thresholds")
pdf.add_table(
    ["Level", "Score Range", "Alert", "AI Action"],
    [
        ["Green Healthy", ">=70", "None", "Normal monitoring"],
        ["Yellow Attention", "50-70", "Yellow alert", "Proactive check-in within 24h"],
        ["Red Alert", "<50", "Red alert", "Immediate notification + suggested action"],
    ],
    [35, 30, 40, 85]
)

# ===== 6. Technical Innovation =====
pdf.add_page()
pdf.chapter_title("6. Technical Innovation Points")

pdf.section_title("6.1 Skill as Code")
pdf.body_text("Each Skill contains complete executable Python scripts, not just prompts. AI Agents can independently invoke and execute them.")

pdf.section_title("6.2 Cross-Platform Encoding Adaptation")
pdf.add_table(
    ["Scenario", "Processing"],
    [
        ["Unknown input file encoding", "Auto-detect (chardet algorithm)"],
        ["Output for Windows users", "utf-8-sig + CRLF"],
        ["Output for Mac/Linux users", "utf-8 + LF"],
        [".bat/.cmd Chinese scripts", "GBK encoding"],
    ],
    [70, 120]
)

pdf.section_title("6.3 Stateful AI (Layer 5 Innovation)")
pdf.add_table(
    ["Innovation", "Description"],
    [
        ["Memory accumulation", "AI remembers 10 dimensions per partner"],
        ["Relationship quantification", "Health score makes relationships measurable"],
        ["Proactive alerts", "AI auto-monitors and pushes warning notifications"],
        ["Strategy adaptation", "Auto-adjusts communication based on memory"],
    ],
    [50, 140]
)

pdf.section_title("6.4 Built-in Business Rules")
pdf.body_text("Business rules come from real operations experience, not generic AI responses. Example: dedup uses Source Bank priority logic (not pandas drop_duplicates), cross-cultural comms use Soft Wording + Validation Framing strategies (not standard templates).")

# ===== 7. Impact =====
pdf.chapter_title("7. Application Scenarios & Impact")
pdf.add_table(
    ["Metric", "Before", "After", "Improvement"],
    [
        ["Monthly reconciliation", "~1 day", "~30 min", "96% reduction"],
        ["Report cleaning", "3-5h each", "Automated", "100% reduction"],
        ["Cross-cultural comms", "5-8 rounds", "1-2 rounds", "75% reduction"],
        ["Budget allocation", "Experience-driven", "Data-driven", "Qualitative change"],
        ["New hire onboarding", "2 weeks", "2 days", "86% reduction"],
        ["Partner churn warning", "By experience", "AI proactive alert", "60% improvement"],
    ],
    [45, 40, 45, 60]
)

# ===== 8. Differentiation =====
pdf.chapter_title("8. Core Differentiation: Cross-Cultural Communication")
pdf.body_text("Most AI Agent tools focus on 'data processing' and 'automation'. Few address the most critical need: cross-cultural business communication.")
pdf.quote_block("Data processing -> use generic tools. Automation -> use generic RPA. Cross-cultural communication -> NO existing tool. That's the real moat.")

pdf.subsection_title("Strategy 1: Soft Wording")
pdf.body_text("Avoid directness that is perceived as arrogant in Brazilian culture. Example: 'Would you mind sharing the report?' instead of 'Send the report now.'")

pdf.subsection_title("Strategy 2: Validation Framing")
pdf.body_text("Confirm consensus before making requests to increase acceptance rate. Template: Confirm understanding -> Express appreciation -> Gently propose next step.")

pdf.subsection_title("Strategy 3: Internal Coordination Positioning")
pdf.body_text("Attribute pressure to 'other departments' to preserve relationship. Template: 'Our finance/legal team is asking for...'")

# ===== 9. Tech Stack =====
pdf.chapter_title("9. Tech Stack")
pdf.add_table(
    ["Component", "Technology", "Notes"],
    [
        ["Skill definition", "Markdown (YAML frontmatter)", "Metadata + docs + scripts"],
        ["Automation scripts", "Python 3.9+", "pandas, openpyxl, requests, chardet"],
        ["AI Agent runtime", "OpenClaw / WorkBuddy", "Skill loading + invocation"],
        ["Encoding handling", "Custom (write_file.py)", "Cross-platform encoding + BOM/CRLF"],
        ["Data formats", "CSV / JSON / Excel (xlsx)", "Both input and output"],
        ["Partner memory", "Local JSON files", "data/partners/*.json"],
    ],
    [45, 60, 85]
)

# ===== 10. Future =====
pdf.chapter_title("10. Future Roadmap")
pdf.subsection_title("Phase 1 (1-2 months)")
pdf.body_text("- Complete Layer 5 Skills (partner-memory-system + relationship-health-score)\n- Integrate AppFollow/AppMagic API for real ranking data\n- Add Partner Risk Radar Skill")

pdf.subsection_title("Phase 2 (3-6 months)")
pdf.body_text("- Integrate Tencent Cloud API (TDS user outreach, OCR, translation)\n- Publish to SkillHub platform\n- Support more MMP platforms\n- Layer 5 expansion: multi-language sentiment analysis")

pdf.subsection_title("Phase 3 (6-12 months)")
pdf.body_text("- Build Skill Marketplace for organizational collaboration\n- Integrate LLM multi-turn conversations\n- Multi-tenant SaaS for SMB affiliate companies\n- Layer 5 expansion: AI negotiation strategy recommendation")

# Save
output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "submission", "technical_document.pdf")
pdf.output(output_path)
print(f"PDF saved to: {output_path}")
