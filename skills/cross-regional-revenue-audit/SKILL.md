---
name: cross-regional-revenue-audit
display_name: "Cross-Regional Revenue Audit Agent | 跨区域收入审计智能体"
description: "Full-chain P&L (Profit & Loss) audit for digital product campaigns across regions. Automatically integrates MMP install/conversion data, ad network settlement data, and payment gateway revenue to generate a comprehensive 7-sheet Excel report highlighting ROI-positive and ROI-negative channels by region and cohort."
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

category: dataops-automation
tags: [revenue-audit, p-and-l, roi-analysis, financial-reporting, affiliate]
layer: 1
trigger_keywords:
  - "盈亏分析"
  - "P&L 报告"
  - "ROI 审计"
  - "收入核算"
  - "App A 分析"
---

# Cross-Regional Revenue Audit Agent
## 跨区域收入审计智能体

### Overview

End-to-end financial audit connecting three data sources:
**MMP (installs + events)** → **Ad Network Settlement (cost)** → **Payment Gateway (revenue)**

Output: A **7-sheet Excel report** with per-channel, per-region, per-cohort P&L analysis.

### Data Sources Integration

```
                    ┌─────────────────────┐
                    │   Payment Gateway   │
                    │   (Revenue Data)    │
                    └─────────┬───────────┘
                              │
┌─────────────┐         ┌────▼──────────┐       ┌──────────────────┐
│    MMP      │ ──────▶ │  Audit Engine  │ ◀──── │  Ad Network      │
│ (AppsFlyer) │         │                │       │  (Settlement)    │
│             │         │  Cost vs Rev   │       │                  │
└─────────────┘         └────┬──────────┘       └──────────────────┘
                              │
                     ┌────────▼────────┐
                     │  P&L Report     │
                     │  (7 Sheets)     │
                     └─────────────────┘
```

### Report Structure (7 Sheets)

| Sheet # | Name | Content |
|---------|------|---------|
| 1 | **Executive Summary** | Top-level KPIs: Total Revenue, Total Cost, Net Profit, Overall ROI % |
| 2 | **Channel P&L** | Per-channel breakdown: Installs, Cost, Revenue, Profit, ROI % |
| 3 | **Regional Summary** | Aggregated metrics by geo-region (MENA/LATAM/APAC/EU_US) |
| 4 | **Cohort Analysis** | Weekly/monthly cohort performance with decay curves |
| 5 | **Negative ROI Channels** | 🔴 Flagged channels where Cost > Revenue (action required) |
| 6 | **Positive ROI Channels** | 🟢 Top performers ranked by ROI % |
| 7 | **Raw Data** | Joined raw data from all sources for auditing |

### Key Metrics Calculated

```python
# Core formulas
ROI_pct = (Revenue - Cost) / Cost * 100
CPA = Cost / Conversions
LTV = Revenue / Installs
Payback_Days = CPA / (Revenue_per_Day_per_User)
Break_Even_Rate = Users_with_Revenue / Total_Users * 100
```

### Execution Flow

```
1. Load MMP data (CSV exports)
   - Install events by channel, country, date
   - In-app events (purchase, subscription)
   
2. Load settlement data (Excel/CSV)
   - Channel costs per period
   - Payment terms applied
   
3. Load revenue data (Payment Gateway export)
   - Transaction-level revenue
   - Refunds and chargebacks deducted
   
4. Join on: (channel, date_range, user_cohort)
   
5. Calculate P&L per channel/region/cohort
   
6. Generate 7-sheet Excel report with conditional formatting:
   - 🟢 Green: ROI > 0%
   - 🔴 Red: ROI < 0%
   - 🟡 Yellow: -10% < ROI < 0% (warning zone)
   
7. Auto-highlight actionable insights:
   - Top 3 negative ROI channels requiring immediate attention
   - Top 3 positive ROI channels for budget increase recommendation
```

### Output Sample (Sheet 2: Channel P&L)

| Channel | Region | Installs | Cost ($) | Revenue ($) | Profit ($) | ROI % | Status |
|---------|--------|----------|----------|-------------|------------|-------|--------|
| Channel_A | MENA | 12,345 | $15,000 | $22,500 | $7,500 | +50% | 🟢 |
| Channel_B | LATAM | 8,900 | $12,000 | $8,100 | -$3,900 | -32.5% | 🔴 |
| Channel_C | APAC | 15,600 | $18,000 | $27,300 | $9,300 | +51.7% | 🟢 |

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`revenue_audit.py`](scripts/revenue_audit.py) | Executable script |

### Dependencies

```python
pandas >= 1.5.0
openpyxl >= 3.1.0
xlsxwriter >= 3.0.0  # For advanced formatting
```
