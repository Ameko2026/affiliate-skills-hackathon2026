---
name: crm-channel-extraction
display_name: "CRM Channel Extraction | 渠道 CRM 数据提取器"
description: "Extracts and filters channel-specific data from AppsFlyer CSV exports or CRM databases. Supports multiple filter conditions (channel name match, media source, date range, event type, attribution status) and outputs clean datasets."
version: 1.1.0
agent_created: true
category: dataops-automation
tags: [crm, channel-extraction, appsflyer, data-filtering]
layer: 1
trigger_keywords:
  - "提取渠道数据"
  - "过滤渠道"
  - "channel extraction"
---

# CRM Channel Extraction
## 渠道 CRM 数据提取器

### Overview

From AppsFlyer CSV files or CRM data, **extract all records matching a specific channel** with flexible filtering.

### Filter Conditions

| Condition | Description | Example |
|-----------|-------------|---------|
| Channel match | Exact or fuzzy | `Channel == 'channel_a_mob'` |
| Media Source | By Media Source ID | `Media Source == 'xxx_int'` |
| Date range | Event Time in range | `2026-02-01` to `2026-02-28` |
| Event type | By event name | `Event Name == 'af_purchase'` |
| Primary only | First attribution only | `Is Primary Attribution == true` |

### Execution Flow

```
1. Read file (auto-detect encoding: utf-8-sig/gbk/latin-1)
2. Apply channel matching (exact -> fuzzy fallback)
3. Apply additional filters (AND logic)
4. Export Excel + summary report
5. Statistics: total records, unique users, event distribution
```

### Output

- **File**: Excel/CSV with filtered channel data
- **Report**: Total count, unique users, event type distribution, date range

### Script Usage

```bash
python3 scripts/extract_channel.py \
  --input data/appsflyer_export.csv \
  --channel channel_a_mob \
  --start-date 2026-02-01 \
  --end-date 2026-02-28 \
  --output output/channel_data.xlsx
```

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`extract_channel.py`](scripts/extract_channel.py) | Executable script |

### Dependencies

```python
pandas >= 1.5.0
openpyxl >= 3.1.0
