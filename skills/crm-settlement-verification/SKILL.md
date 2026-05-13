---
name: crm-settlement-verification
display_name: "CRM Settlement Verification | 结算数据核对智能体"
description: "Automated settlement data verification from AppsFlyer in-app events CSV. Filters settlement records by channel, validates transaction IDs against promotion records, checks promotion window compliance, and generates a funnel analysis report."
version: 1.1.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

category: dataops-automation
tags: [settlement, verification, reconciliation, appsflyer]
layer: 1
trigger_keywords:
  - "结算核对"
  - "对账"
  - "settlement verify"
  - "推广窗口验证"
---

# CRM Settlement Verification
## 结算数据核对智能体

### Overview

Validates settlement records through a **multi-step funnel**, producing a reconciliation report.

### Validation Funnel (Sequential)

| Step | Condition | Purpose |
|------|-----------|---------|
| Step 1 | Is Primary Attribution = true | Remove duplicates |
| Step 2 | Event Value contains transaction_id | Valid transactions |
| Step 3 | Channel matches target | Scope to partner |
| Step 4 | Event Time within promotion window | Active period check |

### Transaction ID Validation

```python
import re
pattern = r'"transaction_id"\s*:\s*"(\d+)"'
# Extract and validate numeric transaction IDs from Event Value
```

### Promotion Window Verification

Load promotion record Excel to determine valid date range, then validate each record's Event Time falls within the window.

### Sample Funnel Output

```
Settlement Verification Report
Channel: example_channel
==============================
Initial Data:         10,304 records
  Step 1 (Primary):    4,521 (-43.9%)
  Step 2 (TXN ID):     2,156 (-52.3%)
  Step 3 (Channel):    2,156 ( 0.0%)
  Step 4 (Window):       91 (-95.8%)

Valid Settlements: 91 records
Validation Rate: 0.88%
```

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`settlement_verify.py`](scripts/settlement_verify.py) | Executable script |

### Dependencies

```python
pandas >= 1.5.0
openpyxl >= 3.1.0
re  # Standard library
