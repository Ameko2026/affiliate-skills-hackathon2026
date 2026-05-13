---
name: pa-channel-export
display_name: "PA Channel Export | PA 渠道数据导出器"
description: "Exports Protected Apps (PA) anti-fraud data from AppsFlyer CSV into styled Excel reports filtered by channel. Preserves all 60+ original CSV fields while highlighting key fraud reason columns (Blocked Reason, Rejected Reason etc.) with orange headers and yellow background for easy partner review."
version: 1.0.0
agent_created: true
category: anti-fraud
tags: [pa, anti-fraud, appsflyer, excel-export, channel-report]
layer: 3
trigger_keywords:
  - "PA 导出"
  - "反作弊报告"
  - "pa export"
  - "渠道 PA 数据"
---

# PA Channel Export
## PA 渠道数据导出器

### Overview

From AppsFlyer PA (Protected Apps) CSV exports, **filter by channel** and generate a **styled Excel report** with all original fields + highlighted fraud reason columns.

### Supported CSV File Types

| File Type | PA Category | Description |
|-----------|-------------|-------------|
| `blocked-installs` | Install PA | Blocked install attempts |
| `detection` | Install/Event PA | Detected fraud (check Event Name field) |
| `blocked-in-app-events` | Event PA | Blocked in-app events |
| `fraud-post-inapps` | Event PA | Post-install fraud detection |

### Highlighted Fraud Reason Columns (moved to end, styled)

| Field Name | Description |
|------------|-------------|
| Blocked Reason | Primary fraud category (bots, fake_location, etc.) |
| Blocked Reason Value | Specific value of the fraud reason |
| Blocked Reason Rule | Rule name that triggered the block |
| Blocked Sub Reason | Secondary fraud detail |
| Rejected Reason | Rejection cause (for in-app events) |
| Rejected Reason Value | Specific rejection value |

Styling: **Orange header (#FF8C00)** + **Light yellow background (#FFFFCC)** for data cells.

### Execution Flow

```
1. Identify target channel and App ID
2. Configure script: TARGET_CHANNEL, FILES_CONFIG
3. For each CSV file type:
   a. Read CSV with encoding auto-detection
   b. Filter rows by channel match
   c. Move 6 fraud reason columns to the end
   d. Apply orange+yellow styling to those columns
   e. Auto-adjust column widths
4. Generate multi-sheet Excel (1 sheet per file type)
5. Deliver Excel file
```

### Output

- **4-sheet Excel file**: blocked-installs, detection, blocked-in-app-events, fraud-post-inapps
- All 60+ original fields preserved
- Fraud reason columns: last 6 cols, orange header + yellow bg
- Auto-fitted column widths

### App ID Reference (Common)

```
Example App IDs (replace with your actual apps):
  App_A_iOS:         idXXXXXXXX
  App_A_Android:     com.example.appa
  App_B_iOS:         idXXXXXXXX
  App_B_Android:     com.example.appb
```

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`pa_export.py`](scripts/pa_export.py) | Executable script |

### Dependencies

```python
pandas >= 1.5.0
openpyxl >= 3.1.0
