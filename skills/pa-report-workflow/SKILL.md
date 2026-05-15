---
name: pa-report-workflow
display_name: "PA Report Workflow | PA 报告更新工作流"
description: "Weekly PA (Protected Apps) report data update pipeline. Collects AppsFlyer PA CSV files from Downloads folder, processes them into JS array format, and injects data into an HTML report page. Handles cross-period date splitting and multi-app aggregation."
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

category: anti-fraud
tags: [pa-report, workflow, weekly-update, html-report, automation]
layer: 3
trigger_keywords:
  - "PA 报告更新"
  - "周报生成"
  - "pa report workflow"
  - "week 数据"
---

# PA Report Workflow
## PA 报告更新工作流

### Overview

Weekly pipeline that updates the combined PA HTML report page with fresh data from AppsFlyer CSV exports.

### Supported CSV File Types

| File Type | PA Category |
|-----------|-------------|
| `blocked-installs` | Install PA |
| `detection` | Install/Event PA (check Event Name) |
| `blocked-in-app-events` | Event PA |
| `fraud-post-inapps` | Event PA |

### Key Configuration

**App Name Mapping**:
```python
APP_NAMES = {
    'idXXXXXXXX': 'App A iOS',
    'com.example.appa': 'App A Android',
    'idXXXXXXXX': 'App B iOS',
    'com.example.appb': 'App B Android',
}
```

**Cross-Period Split**:
```python
# Some apps span Week 2 and Week 3
SPLIT_DATE = "YYYY-MM-DD"  # Configurable split point
# Install Time < SPLIT_DATE -> Week 2
# Install Time >= SPLIT_DATE -> Week 3
```

### Execution Flow

```
1. Confirm CSV files downloaded to Downloads folder
2. Update WEEK_FILES config to match actual filenames
3. Run generate_week_data.py:
   - Read each CSV file
   - Parse per (channel, app_id, os)
   - Aggregate: install_pa, event_pa, reasons
   - Output: week2_final.js + week3_final.js (JSON arrays)
4. Run inject_data.py:
   - Read generated JS files
   - Inject into pa_report_combined.html
   - Replace var week2Data / week3Data declarations
5. Validate output JSON is well-formed
```

### Output Data Schema (per record)

```json
{
  "channel": "example_channel",
  "app_id": "com.example.app",
  "os": "Android",
  "install_pa": 55,
  "event_pa": 22468,
  "install_reasons": ["bots/bayesian_network"],
  "event_reasons": ["bots/behavioral_anomalies"],
  "pid": "",
  "pid_details": [
    {"pid": "example_pid", "install_pa": 0, "event_pa": 8941}
  ]
}
```

### Known Pitfalls

1. **reasons must use list, not Counter**: Counter has no `.append()` method
2. **inject_data.py handles single-line empty arrays**: `var week3Data = [];` needs special parsing
3. **CSV filename dates may vary**: Always verify filenames before running

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`pa_report_workflow.py`](scripts/pa_report_workflow.py) | Executable script |

### Dependencies

```python
pandas >= 1.5.0
# No external dependencies for injection step (string manipulation only)
