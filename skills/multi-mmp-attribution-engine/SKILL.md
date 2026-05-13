---
name: multi-mmp-attribution-engine
display_name: "Multi-MMP Attribution Engine | 多平台归因清洗引擎"
description: "Deduplicates and normalizes attribution data across multiple Mobile Measurement Partners (MMPs) like AppsFlyer and Adjust. Handles channel name variants, invalid events, and cross-platform data consolidation to produce clean, unified attribution datasets for downstream analysis."
version: 1.0.0
agent_created: true
category: dataops-automation
tags: [attribution, mmp, appsflyer, adjust, deduplication, data-cleaning]
layer: 1
trigger_keywords:
  - "归因去重"
  - "渠道变体合并"
  - "attribution dedup"
  - "MMP 数据清洗"
  - "Source Bank"
---

# Multi-MMP Attribution Engine
## 多平台归因清洗引擎

### Overview

Solves the **channel identity crisis** in affiliate marketing: the same partner appears under different names across MMP platforms (e.g., `channel_a_mob`, `channel_a_int`, `Channel-A-Mobile` are all the same channel). This engine normalizes and deduplicates attribution data.

### Core Problem

```
Raw Data (Messy):
├── AppsFlyer:  channel_a_mob    → 1,234 installs
├── AppsFlyer:  channel_a_int    →   567 installs
├── Adjust:     Channel-A-Mobile →   890 installs
├── App Dnal:   Channel A        →   345 installs

Clean Output:
└── Channel: Channel A (normalized) → 3,036 total installs
```

### Source Bank (Channel Mapping)

The engine maintains a **Source Bank** — a canonical mapping of all known channel variants:

```yaml
# Example Source Bank entries
Channel A:
  canonical_name: "Channel A"
  variants:
    - "channel_a_mob"
    - "channel_a_int"
    - "Channel-A-Mobile"
    - "channel_a_mobile"
    - "channel_a-ios"
  category: "tier_1_network"
  region: "APAC"

Channel B:
  canonical_name: "Channel B"
  variants:
    - "channel_b_mob"
    - "channel_b_int"
    - "Channel-B-Mobile"
  category: "tier_2_network"
  region: "LATAM"

partner_c_channel_c:
  canonical_name: "Partner C (channel_c)"
  variants:
    - "channel_c_mob"
    - "channel_c_int"
    - "channel_c_alt"
  category: "tier_1_network"
  region: "LATAM"
```

### Processing Rules

| Rule | Description |
|------|-------------|
| **Variant normalization** | Map all variant names to canonical name via Source Bank |
| **Primary attribution only** | Keep only `Is Primary Attribution == true` records |
| **Invalid event filtering** | Remove test events, duplicate transaction IDs |
| **Cross-MMP merge** | Union data from AppsFlyer + Adjust on (user_id, event_time) |
| **Event type standardization** | Normalize `af_purchase`, `purchase`, `in_app_purchase` → unified schema |

### Execution Flow

```
1. Load raw CSV from MMP platform(s)
   ↓
2. Apply Source Bank mapping → normalize channel names
   ↓
3. Filter: Primary Attribution only
   ↓
4. Filter: Remove invalid/test events
   ↓
5. Deduplicate: (user_id, event_id, transaction_id) tuple
   ↓
6. Merge cross-MMP records (if multiple sources)
   ↓
7. Output clean dataset with canonical channel names
```

### Output Schema

| Column | Type | Description |
|--------|------|-------------|
| `canonical_channel` | string | Normalized channel name from Source Bank |
| `original_channel` | string | Original raw channel name (for traceability) |
| `mmp_source` | string | `appsflyer` or `adjust` |
| `user_id` | string | Anonymous user identifier |
| `event_time` | datetime | Event timestamp (UTC) |
| `event_name` | string | Standardized event name |
| `revenue` | float | Event revenue (USD) |
| `is_primary` | boolean | Primary attribution flag |

### Key Features

- **Source Bank as single source of truth**: Channel mappings maintained in one place
- **Audit trail**: Preserves original channel names for debugging
- **Multi-MMP support**: Handles AppsFlyer and Adjust simultaneously
- **Extensible**: New channels added to Source Bank without code changes

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`multi_mmp_attribution.py`](scripts/multi_mmp_attribution.py) | Executable script |

### Dependencies

```python
pandas >= 1.5.0
# No external API calls needed — pure local processing
```
