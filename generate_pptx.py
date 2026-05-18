"""Generate PPTX for Tencent Cloud Hackathon 2026 submission."""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import os

# Color palette: Ocean Gradient (deep blue + teal)
C_PRIMARY = RGBColor(0x06, 0x5A, 0x82)    # deep blue
C_SECONDARY = RGBColor(0x1C, 0x72, 0x93)  # teal
C_ACCENT = RGBColor(0x02, 0xC3, 0x9A)     # mint
C_DARK = RGBColor(0x21, 0x29, 0x5C)       # midnight
C_LIGHT = RGBColor(0xF5, 0xF7, 0xFA)      # off-white
C_WHITE = RGBColor(0xFF, 0xFF, 0xFF)
C_GRAY = RGBColor(0x94, 0xA3, 0xB8)       # muted gray
C_TEXT = RGBColor(0x1E, 0x29, 0x3B)        # dark text
C_RED = RGBColor(0xEF, 0x44, 0x44)
C_YELLOW = RGBColor(0xF5, 0x9E, 0x0B)
C_GREEN = RGBColor(0x10, 0xB9, 0x81)

prs = Presentation()
prs.slide_width = Inches(10)
prs.slide_height = Inches(5.625)

def add_bg(slide, color):
    bg = slide.background
    fill = bg.fill
    fill.solid()
    fill.fore_color.rgb = color

def add_textbox(slide, left, top, width, height, text, font_size=14, bold=False, color=C_TEXT, align=PP_ALIGN.LEFT, font_name="Calibri"):
    txBox = slide.shapes.add_textbox(Inches(left), Inches(top), Inches(width), Inches(height))
    tf = txBox.text_frame
    tf.word_wrap = True
    p = tf.paragraphs[0]
    p.text = text
    p.font.size = Pt(font_size)
    p.font.bold = bold
    p.font.color.rgb = color
    p.font.name = font_name
    p.alignment = align
    return txBox

def add_shape(slide, left, top, width, height, fill_color):
    from pptx.enum.shapes import MSO_SHAPE
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(left), Inches(top), Inches(width), Inches(height))
    shape.fill.solid()
    shape.fill.fore_color.rgb = fill_color
    shape.line.fill.background()
    return shape

# ============ Slide 1: Cover ============
slide = prs.slides.add_slide(prs.slide_layouts[6])  # blank
add_bg(slide, C_DARK)
add_shape(slide, 0, 0, 10, 0.08, C_ACCENT)
add_textbox(slide, 0.8, 1.2, 8.4, 1.0, "Cross-Cultural Affiliate Network", 38, True, C_WHITE, PP_ALIGN.CENTER)
add_textbox(slide, 0.8, 2.0, 8.4, 0.8, "Management Skill Collection", 38, True, C_ACCENT, PP_ALIGN.CENTER)
add_textbox(slide, 0.8, 3.2, 8.4, 0.5, "AI Agent-based Multi-Region Affiliate Automation System", 16, False, C_GRAY, PP_ALIGN.CENTER)
add_shape(slide, 3.5, 4.0, 3.0, 0.04, C_ACCENT)
add_textbox(slide, 0.8, 4.3, 8.4, 0.4, "Tencent Cloud Hackathon 2026  |  AI Agent Skill Track", 13, False, C_GRAY, PP_ALIGN.CENTER)

# ============ Slide 2: Agenda ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_LIGHT)
add_shape(slide, 0, 0, 10, 0.08, C_PRIMARY)
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Agenda", 32, True, C_PRIMARY)

items = [
    ("01", "Who We Are & The Problem", C_PRIMARY),
    ("02", "5-Layer Skill Architecture", C_SECONDARY),
    ("03", "Core Innovation: Layer 5 - AI Organization Behavior", C_ACCENT),
    ("04", "Demo & Impact Metrics", C_PRIMARY),
    ("05", "Why We're Unique", C_SECONDARY),
]
for i, (num, text, color) in enumerate(items):
    y = 1.3 + i * 0.75
    add_shape(slide, 0.8, y, 0.5, 0.5, color)
    add_textbox(slide, 0.85, y + 0.05, 0.4, 0.4, num, 18, True, C_WHITE, PP_ALIGN.CENTER)
    add_textbox(slide, 1.5, y + 0.05, 7.7, 0.4, text, 18, False, C_TEXT, PP_ALIGN.LEFT)

# ============ Slide 3: Pain Points ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_WHITE)
add_shape(slide, 0, 0, 10, 0.08, C_PRIMARY)
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Three Core Pain Points", 30, True, C_PRIMARY)

pain_data = [
    ("Data Processing", "5+ reports/week manual\ncleaning & merging", "3-5h each", C_RED),
    ("Cross-Cultural Comms", "3 advertiser types x 3 traffic\nsources, 5-8 email rounds", "1-4h each", C_YELLOW),
    ("Budget Allocation", "20+ channels, CAP based\non gut feeling", "20-30% waste", C_PRIMARY),
]
for i, (title, desc, impact, color) in enumerate(pain_data):
    x = 0.8 + i * 3.0
    add_shape(slide, x, 1.3, 2.7, 0.5, color)
    add_textbox(slide, x + 0.1, 1.35, 2.5, 0.4, title, 16, True, C_WHITE, PP_ALIGN.CENTER)
    add_textbox(slide, x + 0.1, 2.0, 2.5, 1.0, desc, 13, False, C_TEXT, PP_ALIGN.LEFT)
    add_textbox(slide, x + 0.1, 3.2, 2.5, 0.4, impact, 20, True, color, PP_ALIGN.CENTER)

add_textbox(slide, 0.8, 4.2, 8.4, 0.5, '"We\'re not building a tool \u2014 we\'re training an AI Business Manager"', 14, True, C_DARK, PP_ALIGN.CENTER)

# ============ Slide 4: Architecture Overview ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_LIGHT)
add_shape(slide, 0, 0, 10, 0.08, C_PRIMARY)
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "5-Layer Skill Architecture", 30, True, C_PRIMARY)

layers = [
    ("Layer 5", "AI Organization Behavior", "Partner Memory + Relationship Health", C_ACCENT, "CORE INNOVATION"),
    ("Layer 4", "Cross-Cultural Collaboration", "5 cultural zones: BR/CN/EU/SEA/ME", RGBColor(0x7C, 0x3A, 0xED), ""),
    ("Layer 3", "Anti-Fraud & Attribution", "PA Reports + Fraud Detection", C_SECONDARY, ""),
    ("Layer 2", "Data Analytics", "Budget + Funnel + Market Intel", RGBColor(0x03, 0x69, 0x8A), ""),
    ("Layer 1", "Data Connectors", "OCR + CRM + PA Export", RGBColor(0x47, 0x55, 0x69), ""),
]
for i, (layer, name, desc, color, badge) in enumerate(layers):
    y = 1.2 + i * 0.78
    add_shape(slide, 0.8, y, 7.5, 0.65, color)
    add_textbox(slide, 0.9, y + 0.05, 1.2, 0.5, layer, 13, True, C_WHITE)
    add_textbox(slide, 2.2, y + 0.05, 2.5, 0.5, name, 14, True, C_WHITE)
    add_textbox(slide, 4.8, y + 0.05, 3.2, 0.5, desc, 11, False, RGBColor(0xE0,0xE7,0xFF))
    if badge:
        add_shape(slide, 8.5, y + 0.1, 1.3, 0.4, C_DARK)
        add_textbox(slide, 8.55, y + 0.12, 1.2, 0.35, badge, 9, True, C_ACCENT, PP_ALIGN.CENTER)

add_textbox(slide, 0.8, 5.0, 8.4, 0.4, "15 Skills  |  5 Layers  |  Each Skill = SKILL.md + Executable Python Script", 12, False, C_GRAY, PP_ALIGN.CENTER)

# ============ Slide 5: Layer 1 - Data Connectors ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_WHITE)
add_shape(slide, 0, 0, 10, 0.08, RGBColor(0x47, 0x55, 0x69))
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Layer 1: Data Connectors", 28, True, RGBColor(0x47, 0x55, 0x69))

l1_skills = [
    ("crm-channel-extraction", "OCR settlement auto-extraction", "1h \u2192 3min"),
    ("crm-settlement-verification", "Auto reconciliation + anomaly flag", "2h \u2192 3min"),
    ("pa-channel-export", "PA standardized report generation", "1h \u2192 1min"),
]
for i, (skill, desc, impact) in enumerate(l1_skills):
    y = 1.4 + i * 1.1
    add_shape(slide, 0.8, y, 8.4, 0.85, C_LIGHT)
    add_shape(slide, 0.8, y, 0.08, 0.85, RGBColor(0x47, 0x55, 0x69))
    add_textbox(slide, 1.1, y + 0.05, 4.0, 0.35, skill, 14, True, C_TEXT)
    add_textbox(slide, 1.1, y + 0.4, 5.0, 0.35, desc, 12, False, C_GRAY)
    add_textbox(slide, 7.0, y + 0.2, 2.0, 0.45, impact, 18, True, C_ACCENT, PP_ALIGN.CENTER)

add_textbox(slide, 0.8, 4.6, 8.4, 0.4, "Auto encoding detection (utf-8-sig + CRLF) | Excel opens without garbled characters", 11, False, C_GRAY, PP_ALIGN.CENTER)

# ============ Slide 6: Layer 2 - Data Analytics ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_WHITE)
add_shape(slide, 0, 0, 10, 0.08, RGBColor(0x03, 0x69, 0x8A))
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Layer 2: Data Analytics", 28, True, RGBColor(0x03, 0x69, 0x8A))

l2_skills = [
    ("multi-mmp-attribution-engine", "MMP dedup via Source Bank priority"),
    ("ai-budget-optimizer", "Channel effectiveness + CAP suggestions"),
    ("conversion-funnel-intelligence", "5-stage funnel + color-coded report"),
    ("geo-market-intel-engine", "Regional market intelligence"),
]
for i, (skill, desc) in enumerate(l2_skills):
    y = 1.3 + i * 0.9
    add_shape(slide, 0.8, y, 4.2, 0.7, C_LIGHT)
    add_shape(slide, 0.8, y, 0.08, 0.7, RGBColor(0x03, 0x69, 0x8A))
    add_textbox(slide, 1.1, y + 0.05, 3.8, 0.3, skill, 12, True, C_TEXT)
    add_textbox(slide, 1.1, y + 0.35, 3.8, 0.3, desc, 10, False, C_GRAY)

l2_skills2 = [
    ("wish-intelligence-collector", "Multi-format Wish List parsing"),
    ("regional-wish-classifier", "5-zone auto classification"),
    ("cross-regional-revenue-audit", "Campaign P&L full audit"),
    ("macro-monitoring-agent", "FX/inflation/CPI tracking"),
]
for i, (skill, desc) in enumerate(l2_skills2):
    y = 1.3 + i * 0.9
    add_shape(slide, 5.3, y, 4.2, 0.7, C_LIGHT)
    add_shape(slide, 5.3, y, 0.08, 0.7, RGBColor(0x03, 0x69, 0x8A))
    add_textbox(slide, 5.6, y + 0.05, 3.8, 0.3, skill, 12, True, C_TEXT)
    add_textbox(slide, 5.6, y + 0.35, 3.8, 0.3, desc, 10, False, C_GRAY)

# ============ Slide 7: Layer 3 - Anti-Fraud ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_WHITE)
add_shape(slide, 0, 0, 10, 0.08, C_SECONDARY)
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Layer 3: Anti-Fraud & Attribution", 28, True, C_SECONDARY)

l3_skills = [
    ("pa-channel-export", "Export PA anti-fraud data with highlighted fraud reasons", "4h \u2192 Auto"),
    ("pa-report-workflow", "Weekly pipeline: CSV \u2192 JS arrays \u2192 HTML report", "Manual \u2192 Auto"),
]
for i, (skill, desc, impact) in enumerate(l3_skills):
    y = 1.4 + i * 1.1
    add_shape(slide, 0.8, y, 8.4, 0.85, C_LIGHT)
    add_shape(slide, 0.8, y, 0.08, 0.85, C_SECONDARY)
    add_textbox(slide, 1.1, y + 0.05, 4.0, 0.35, skill, 14, True, C_TEXT)
    add_textbox(slide, 1.1, y + 0.4, 5.0, 0.35, desc, 12, False, C_GRAY)
    add_textbox(slide, 7.0, y + 0.2, 2.0, 0.45, impact, 16, True, C_SECONDARY, PP_ALIGN.CENTER)

# ============ Slide 8: Layer 4 - Cross-Cultural ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_WHITE)
add_shape(slide, 0, 0, 10, 0.08, RGBColor(0x7C, 0x3A, 0xED))
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Layer 4: Cross-Cultural Collaboration", 28, True, RGBColor(0x7C, 0x3A, 0xED))
add_textbox(slide, 0.8, 1.2, 4.0, 0.4, "Core Differentiator", 20, True, RGBColor(0x7C, 0x3A, 0xED))

zones = ["BR Brazil", "CN China", "EU Europe", "SEA Southeast Asia", "ME Middle East"]
for i, zone in enumerate(zones):
    x = 0.8 + i * 1.7
    add_shape(slide, x, 1.8, 1.5, 0.5, RGBColor(0x7C, 0x3A, 0xED))
    add_textbox(slide, x + 0.05, 1.85, 1.4, 0.4, zone, 10, True, C_WHITE, PP_ALIGN.CENTER)

strategies = [
    ("Soft Wording", "Avoid directness in BR culture"),
    ("Validation Framing", "Confirm consensus before requesting"),
    ("Internal Coordination", "Pressure via \"other departments\""),
]
add_textbox(slide, 0.8, 2.6, 4.0, 0.3, "3 Communication Strategies:", 14, True, C_TEXT)
for i, (name, desc) in enumerate(strategies):
    y = 3.0 + i * 0.7
    add_shape(slide, 0.8, y, 8.4, 0.55, C_LIGHT)
    add_shape(slide, 0.8, y, 0.08, 0.55, RGBColor(0x7C, 0x3A, 0xED))
    add_textbox(slide, 1.1, y + 0.05, 2.5, 0.4, name, 13, True, C_TEXT)
    add_textbox(slide, 3.8, y + 0.05, 5.2, 0.4, desc, 12, False, C_GRAY)

add_textbox(slide, 0.8, 5.0, 8.4, 0.4, '"One request \u2192 5 cultural versions generated instantly"', 13, True, C_DARK, PP_ALIGN.CENTER)

# ============ Slide 9: Layer 5 - AI Organization Behavior ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_DARK)
add_shape(slide, 0, 0, 10, 0.08, C_ACCENT)
add_textbox(slide, 0.8, 0.3, 8.4, 0.6, "Layer 5: AI Organization Behavior", 30, True, C_ACCENT)
add_textbox(slide, 0.8, 0.9, 8.4, 0.3, "CORE INNOVATION \u2014 AI is no longer a tool, but a \"partner\"", 14, False, C_GRAY, PP_ALIGN.LEFT)

# Left: Partner Memory
add_shape(slide, 0.8, 1.5, 4.0, 3.5, RGBColor(0x1E, 0x29, 0x3B))
add_textbox(slide, 1.0, 1.6, 3.6, 0.4, "Partner Memory System", 18, True, C_ACCENT)
add_textbox(slide, 1.0, 2.1, 3.6, 0.3, "AI starts \"remembering people\"", 12, False, C_GRAY)
dims = ["Communication style", "Reply speed", "Risk history", "Negotiation habit",
        "Category preference", "Timezone", "Emotion style", "Contact reliability",
        "Call preference", "Budget cooperation"]
for i, d in enumerate(dims[:5]):
    add_textbox(slide, 1.2, 2.5 + i * 0.35, 3.2, 0.3, f"\u2022 {d}", 11, False, C_WHITE)
for i, d in enumerate(dims[5:]):
    add_textbox(slide, 3.0, 2.5 + i * 0.35, 1.8, 0.3, f"\u2022 {d}", 11, False, C_WHITE)
add_textbox(slide, 1.0, 4.5, 3.6, 0.3, "10 dimensions of partner memory", 11, True, C_ACCENT)

# Right: Relationship Health
add_shape(slide, 5.2, 1.5, 4.0, 3.5, RGBColor(0x1E, 0x29, 0x3B))
add_textbox(slide, 5.4, 1.6, 3.6, 0.4, "Relationship Health Score", 18, True, RGBColor(0xF4, 0x72, 0xB6))
add_textbox(slide, 5.4, 2.1, 3.6, 0.3, "0-100 real-time health scoring", 12, False, C_GRAY)

alerts = [
    ("Green \u226570", "Normal monitoring", C_GREEN),
    ("Yellow 50-70", "24h proactive check-in", C_YELLOW),
    ("Red <50", "Immediate alert + AI action", C_RED),
]
for i, (level, action, color) in enumerate(alerts):
    y = 2.6 + i * 0.6
    add_shape(slide, 5.4, y, 0.3, 0.4, color)
    add_textbox(slide, 5.9, y, 1.5, 0.4, level, 12, True, C_WHITE)
    add_textbox(slide, 7.5, y, 1.5, 0.4, action, 10, False, C_GRAY)

add_textbox(slide, 5.4, 4.5, 3.6, 0.3, "3-tier alert + AI suggestions", 11, True, RGBColor(0xF4, 0x72, 0xB6))

# ============ Slide 10: Partner Memory Demo ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_WHITE)
add_shape(slide, 0, 0, 10, 0.08, C_ACCENT)
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Partner Memory: Before vs After", 28, True, C_ACCENT)

# Before
add_shape(slide, 0.8, 1.3, 4.0, 3.5, RGBColor(0xFE, 0xF2, 0xF2))
add_textbox(slide, 1.0, 1.4, 3.6, 0.4, "Without Memory", 18, True, C_RED)
scenarios_no = [
    '"Send the report now."',
    "Direct pricing offer",
    "Same tone for everyone",
    "Can't predict churn",
]
for i, s in enumerate(scenarios_no):
    add_textbox(slide, 1.2, 2.0 + i * 0.6, 3.4, 0.5, f"\u274c {s}", 12, False, C_TEXT)

# After
add_shape(slide, 5.2, 1.3, 4.0, 3.5, RGBColor(0xEC, 0xFD, 0xF5))
add_textbox(slide, 5.4, 1.4, 3.6, 0.4, "With Memory", 18, True, C_GREEN)
scenarios_yes = [
    '"Hi [Partner], would you mind sharing... :)"',
    '"I remember you mentioned budget pressure..."',
    "Auto-adapt based on partner profile",
    "Proactive churn risk alert",
]
for i, s in enumerate(scenarios_yes):
    add_textbox(slide, 5.6, 2.0 + i * 0.6, 3.4, 0.5, f"\u2705 {s}", 11, False, C_TEXT)

# ============ Slide 11: Health Score Dashboard ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_LIGHT)
add_shape(slide, 0, 0, 10, 0.08, RGBColor(0xF4, 0x72, 0xB6))
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Relationship Health Dashboard", 28, True, RGBColor(0xF4, 0x72, 0xB6))

partners = [
    ("Hertzmobi", 85, C_GREEN, "Healthy"),
    ("AppTango", 62, C_YELLOW, "Attention"),
    ("GamePartner", 35, C_RED, "Alert"),
]
for i, (name, score, color, status) in enumerate(partners):
    y = 1.3 + i * 1.1
    add_shape(slide, 0.8, y, 8.4, 0.85, C_WHITE)
    add_shape(slide, 0.8, y, 0.08, 0.85, color)
    add_textbox(slide, 1.1, y + 0.1, 2.5, 0.3, name, 16, True, C_TEXT)
    # Score bar background
    add_shape(slide, 1.1, y + 0.5, 5.0, 0.2, RGBColor(0xE2, 0xE8, 0xF0))
    # Score bar fill
    bar_w = 5.0 * score / 100
    add_shape(slide, 1.1, y + 0.5, bar_w, 0.2, color)
    add_textbox(slide, 6.3, y + 0.1, 1.0, 0.3, str(score), 22, True, color, PP_ALIGN.CENTER)
    add_textbox(slide, 7.5, y + 0.15, 1.5, 0.25, status, 14, True, color, PP_ALIGN.LEFT)

add_shape(slide, 0.8, 4.5, 8.4, 0.6, RGBColor(0xFE, 0xF2, 0xF2))
add_textbox(slide, 1.0, 4.55, 8.0, 0.4, "GamePartner health dropped to 35 \u2014 AI suggests: call within 24h", 13, True, C_RED, PP_ALIGN.LEFT)

# ============ Slide 12: AI Evolution Path ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_WHITE)
add_shape(slide, 0, 0, 10, 0.08, C_PRIMARY)
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "AI Evolution: v1.0 \u2192 v2.0 \u2192 v3.0", 28, True, C_PRIMARY)

evo = [
    ("v1.0", "Stateless Tool", "Only analyzes data\nDoesn't know people", "Efficiency +90%", C_GRAY),
    ("v2.0", "Stateful AI", "Remembers partners\nAuto-adapts style", "Relationship +60%", C_SECONDARY),
    ("v3.0", "Proactive AI", "Evaluates health\nPrevents churn", "Risk prevention", C_ACCENT),
]
for i, (ver, title, desc, value, color) in enumerate(evo):
    x = 0.8 + i * 3.1
    add_shape(slide, x, 1.3, 2.8, 3.2, C_LIGHT)
    add_shape(slide, x, 1.3, 2.8, 0.5, color)
    add_textbox(slide, x + 0.1, 1.35, 2.6, 0.4, f"{ver}: {title}", 14, True, C_WHITE, PP_ALIGN.CENTER)
    add_textbox(slide, x + 0.2, 2.0, 2.4, 1.2, desc, 12, False, C_TEXT, PP_ALIGN.LEFT)
    add_textbox(slide, x + 0.2, 3.5, 2.4, 0.4, value, 14, True, color, PP_ALIGN.CENTER)

add_textbox(slide, 0.8, 4.8, 8.4, 0.4, '"We\'re not building a tool \u2014 we\'re training an AI Business Manager"', 14, True, C_DARK, PP_ALIGN.CENTER)

# ============ Slide 13: Impact Metrics ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_LIGHT)
add_shape(slide, 0, 0, 10, 0.08, C_PRIMARY)
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Impact & Results", 30, True, C_PRIMARY)

metrics = [
    ("96%", "Reconciliation\ntime reduced", C_PRIMARY),
    ("100%", "Report cleaning\nautomated", C_SECONDARY),
    ("75%", "Email rounds\nreduced", RGBColor(0x7C, 0x3A, 0xED)),
    ("60%", "Churn prediction\nimprovement", C_ACCENT),
]
for i, (val, label, color) in enumerate(metrics):
    x = 0.6 + i * 2.35
    add_shape(slide, x, 1.2, 2.1, 2.5, C_WHITE)
    add_textbox(slide, x + 0.1, 1.4, 1.9, 0.8, val, 36, True, color, PP_ALIGN.CENTER)
    add_textbox(slide, x + 0.1, 2.3, 1.9, 0.8, label, 12, False, C_TEXT, PP_ALIGN.CENTER)

compare_data = [
    ("Monthly reconciliation", "1 day", "30 min"),
    ("Budget allocation", "Experience", "Data-driven"),
    ("Cross-cultural comms", "5-8 rounds", "1-2 rounds"),
    ("New hire onboarding", "2 weeks", "2 days"),
]
add_textbox(slide, 0.8, 3.8, 2.0, 0.3, "Metric", 11, True, C_TEXT)
add_textbox(slide, 3.5, 3.8, 2.0, 0.3, "Before", 11, True, C_RED)
add_textbox(slide, 6.0, 3.8, 2.0, 0.3, "After", 11, True, C_GREEN)
for i, (metric, before, after) in enumerate(compare_data):
    y = 4.15 + i * 0.3
    add_textbox(slide, 0.8, y, 2.5, 0.25, metric, 10, False, C_TEXT)
    add_textbox(slide, 3.5, y, 2.0, 0.25, before, 10, False, C_RED)
    add_textbox(slide, 6.0, y, 2.0, 0.25, after, 10, True, C_GREEN)

# ============ Slide 14: Unique Value ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_WHITE)
add_shape(slide, 0, 0, 10, 0.08, C_PRIMARY)
add_textbox(slide, 0.8, 0.4, 8.4, 0.6, "Why We're Unique", 30, True, C_PRIMARY)

add_textbox(slide, 0.8, 1.1, 8.4, 0.3, "Existing solutions cover data & automation. We cover what they can't.", 14, False, C_GRAY)

unique = [
    ("Cross-Cultural Business Comms", "No existing tool \u2014 real moat", RGBColor(0x7C, 0x3A, 0xED)),
    ("AI with Memory", "Not just data analysis, knows partners", C_ACCENT),
    ("Quantifiable Relationships", "Health scoring makes relationships measurable", RGBColor(0xF4, 0x72, 0xB6)),
]
for i, (title, desc, color) in enumerate(unique):
    y = 1.7 + i * 1.0
    add_shape(slide, 0.8, y, 8.4, 0.8, C_LIGHT)
    add_shape(slide, 0.8, y, 0.08, 0.8, color)
    add_textbox(slide, 1.1, y + 0.05, 7.8, 0.35, title, 16, True, color)
    add_textbox(slide, 1.1, y + 0.4, 7.8, 0.3, desc, 12, False, C_TEXT)

add_textbox(slide, 0.8, 4.8, 8.4, 0.4, '"Most projects build better data tools. We build an AI Employee."', 14, True, C_DARK, PP_ALIGN.CENTER)

# ============ Slide 15: Q&A ============
slide = prs.slides.add_slide(prs.slide_layouts[6])
add_bg(slide, C_DARK)
add_shape(slide, 0, 0, 10, 0.08, C_ACCENT)
add_textbox(slide, 0.8, 1.0, 8.4, 0.8, "Thank You!", 40, True, C_WHITE, PP_ALIGN.CENTER)
add_shape(slide, 3.5, 2.0, 3.0, 0.04, C_ACCENT)
add_textbox(slide, 0.8, 2.3, 8.4, 0.5, "Cross-Cultural Affiliate Network Management Skills", 18, False, C_GRAY, PP_ALIGN.CENTER)
add_textbox(slide, 0.8, 2.9, 8.4, 0.4, "Tencent Cloud Hackathon 2026  |  AI Agent Skill Track", 14, False, C_GRAY, PP_ALIGN.CENTER)

layer_summary = [
    ("Layer 1", "3 Skills", "Data Connectors"),
    ("Layer 2", "8 Skills", "Data Analytics"),
    ("Layer 3", "2 Skills", "Anti-Fraud"),
    ("Layer 4", "1 Skill", "Cross-Cultural"),
    ("Layer 5", "2 Skills", "AI Organization"),
]
for i, (layer, count, desc) in enumerate(layer_summary):
    x = 0.8 + i * 1.7
    add_shape(slide, x, 3.5, 1.5, 0.8, RGBColor(0x1E, 0x29, 0x3B))
    add_textbox(slide, x + 0.05, 3.55, 1.4, 0.25, layer, 10, True, C_ACCENT, PP_ALIGN.CENTER)
    add_textbox(slide, x + 0.05, 3.8, 1.4, 0.25, count, 12, True, C_WHITE, PP_ALIGN.CENTER)
    add_textbox(slide, x + 0.05, 4.05, 1.4, 0.2, desc, 8, False, C_GRAY, PP_ALIGN.CENTER)

add_textbox(slide, 0.8, 4.8, 8.4, 0.4, "github.com/Ameko2026/affiliate-skills-hackathon2026", 12, False, C_ACCENT, PP_ALIGN.CENTER)

# Save
output_path = os.path.join(os.path.dirname(__file__), "submission", "hackathon_presentation.pptx")
prs.save(output_path)
print(f"PPTX saved to: {output_path}")
