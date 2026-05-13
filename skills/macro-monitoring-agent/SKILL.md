---
name: macro-monitoring-agent
display_name: "Macroeconomic Monitoring Agent | 宏观经济监控智能体"
description: "Daily macroeconomic data monitoring and alerting system for cross-border affiliate operations. Tracks exchange rates, inflation indices, CPI, and key economic indicators across operating regions (MENA, LATAM, APAC) to inform budget decisions and flag currency/economic risks."
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

category: dataops-automation
tags: [macro-monitoring, economic-indicators, exchange-rate, alerting, cross-border]
layer: 1
trigger_keywords:
  - "宏观经济"
  - "汇率监控"
  - "macro monitor"
  - "每日数据"
  - "通胀数据"
---

# Macroeconomic Monitoring Agent
## 宏观经济监控智能体

### Overview

Automated daily monitoring of **macroeconomic indicators** that directly impact affiliate campaign profitability across regions.

### Tracked Indicators by Region

| Region | Key Indicators | Data Sources |
|--------|---------------|--------------|
| **MENA** | USD/AED, USD/SAR, UAE inflation rate, Saudi CPI | Central bank APIs |
| **LATAM** | USD/BRL, USD/MXN, Brazil IPCA, Mexico INPC | BCB, Banxico APIs |
| **APAC** | USD/IDR, USD/THB, Indonesia inflation, Thailand CPI | Bank Indonesia, BOT APIs |
| **Global** | DXY Index, Fed Rate, global risk sentiment | Financial data feeds |

### Alert Rules

```yaml
alert_rules:
  exchange_rate_volatility:
    thresholds:
      BRL: 2.0%
      MXN: 1.5%
      IDR: 1.5%
      AED: 0.5%
      SAR: 0.5%
    action: "Send alert with P&L impact analysis"
  inflation_spike:
    thresholds:
      BR: 1.0%/month
      MX: 0.8%/month
      ID: 0.6%/month
    action: "Flag for budget re-evaluation"
```

### Execution Flow (Daily)

```
1. [Scheduled Trigger] Daily at configured time
2. Fetch latest data from APIs / financial feeds
3. Compute day-over-day changes & trends
4. Evaluate against alert rules
5. If alerts triggered -> Generate alert + impact estimate
6. Generate daily digest
7. Store snapshot in JSON archive
```

### Output Format (Daily Digest)

```
Macro Monitor Daily Digest - YYYY-MM-DD
========================================
Exchange Rates (vs USD):
  BRL:   5.12  (+1.2%) [yellow]
  MXN:  17.34  (+0.8%) [ok]
  IDR: 15890  (+0.3%) [ok]

Alerts (1):
  [MEDIUM] BRL volatility +1.2% exceeds 7-day avg.
  Impact: LATAM CPA may increase ~1.2%
```

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`macro_monitor.py`](scripts/macro_monitor.py) | Executable script |

### Dependencies

```python
requests >= 2.28.0
pandas >= 1.5.0
apscheduler >= 3.10.0  # Optional
