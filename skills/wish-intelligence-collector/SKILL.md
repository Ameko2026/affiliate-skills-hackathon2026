---
name: wish-intelligence-collector
display_name: "Wish Intelligence Collector | 渠道 Wish 智能采集器"
description: "AI-powered Wish List parser for affiliate marketing. Automatically extracts offer information from multi-format channel Wish Lists (screenshots via OCR, text, Excel) and converts them into a standardized 8-column tracking table. Eliminates manual data entry errors and ensures consistent data structure across all channels."
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

category: business-intelligence
tags: [wish-list, parsing, ocr, data-normalization, affiliate-marketing]
layer: 2
trigger_keywords:
  - "解析 Wish List"
  - "Wish List 转表格"
  - "渠道 Offer 提取"
  - "wish to my table"
  - "采集渠道Offer"
---

# Wish Intelligence Collector
## 渠道 Wish 智能采集器

### Overview

Automatically parse channel Wish Lists from multiple formats (OCR screenshots, plain text, Excel) into a **standardized 8-column tracking table**.

### Input Formats

| Format | Source | Processing Method |
|--------|--------|-------------------|
| Screenshot/Image | Channel sends via chat | OCR extraction |
| Plain Text | Email / Chat message | Regex + NLP parsing |
| Excel/CSV | Attached file | pandas direct read |

### Standard Output Schema (8 Columns)

| # | Column Name | Description | Example |
|---|------------|-------------|---------|
| 1 | `offer_id` | Unique offer identifier | `OFF-2026-001` |
| 2 | `offer_name` | Offer / campaign name | `Summer Sale App Install` |
| 3 | `geo_target` | Target geographic region | `MENA`, `LATAM`, `BR` |
| 4 | `payout_model` | CPA / CPI / CPS / RevShare | `CPI $2.50` |
| 5 | `cap_limit` | Daily/total cap | `500/day` |
| 6 | `tracking_link` | Affiliate tracking URL | `https://track.example.com/...` |
| 7 | `status` | Active / Paused / Expired | `Active` |
| 8 | `notes` | Special conditions or remarks | `Incentive allowed` |

### Execution Flow

```
1. Receive Wish List (image/text/file)
   ↓
2. Detect format → Select parser (OCR/Regex/pandas)
   ↓
3. Extract structured fields using predefined patterns
   ↓
4. Validate against 8-column schema
   ↓
5. Flag missing/ambiguous fields for human review
   ↓
6. Output standardized tracking table (Excel/CSV)
```

### Key Features

- **Multi-format input**: Handles OCR text (often messy), copy-pasted text, and structured files
- **Schema validation**: Ensures every row conforms to the 8-column standard
- **Ambiguity detection**: Flags fields that need human confirmation (e.g., unclear geo targeting)
- **Encoding auto-detection**: Handles utf-8-sig, gbk, and mixed encoding inputs

### Output

- **Primary**: Excel file (.xlsx) with formatted 8-column table
- **Secondary**: CSV export for system integration
- **Validation report**: List of rows with missing or flagged fields

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`wish_collector.py`](scripts/wish_collector.py) | Executable script |

### Dependencies

```python
# requirements
pandas >= 1.5.0
openpyxl >= 3.1.0
# Optional: pytesseract for OCR support
```

### Integration

This skill is designed to be invoked by an AI Agent when the user mentions:
- "Parse this Wish List"
- "Convert channel offers to tracking table"
- "Extract offers from [file/image]"

The agent should pass the raw content (text or file path) to the skill's processing script.
