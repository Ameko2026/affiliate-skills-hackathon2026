---
name: regional-wish-classifier
display_name: "Regional Wish Classifier | 区域 Wish 智能分类器"
description: "Auto-classifies affiliate offers by geographic region based on country codes, geo-targeting fields, and contextual clues. Supports 5 regional zones (MENA, LATAM, APAC, Europe&US, Global) and generates separate regional spreadsheets synchronized with master tracking documents."
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

category: business-intelligence
tags: [geo-classification, regional-segmentation, affiliate-marketing, automation]
layer: 2
trigger_keywords:
  - "按区域分类"
  - "区域划分"
  - "Geo 分类"
  - "regional classify"
  - "MENA LATAM 分组"
---

# Regional Wish Classifier
## 区域 Wish 智能分类器

### Overview

Takes parsed Wish List data (output from Wish Intelligence Collector) and **auto-classifies each offer into one of 5 regional zones**, generating region-specific spreadsheets.

### Supported Regions

| Region Code | Full Name | Covered Countries (Examples) |
|-------------|-----------|------------------------------|
| `MENA` | Middle East & North Africa | SA, AE, EG, MA, DZ, TN, JO, BH, KW, QA, OM, IQ, LB, LY, SY, YE, PS |
| `LATAM` | Latin America | BR, MX, AR, CO, PE, CL, VE, EC, BO, PY, UY, PY, CR, PA, DO, GT, CU, HT, TT |
| `APAC` | Asia-Pacific | ID, MY, TH, VN, PH, SG, IN, KR, JP, TW, HK, AU, NZ, PK, BD, MM, KH, LA |
| `EU_US` | Europe & United States | US, GB, DE, FR, IT, ES, NL, PL, SE, NO, DK, FI, AT, BE, IE, PT, GR, CZ, RO, HU |
| `GLOBAL` | Global / Multi-Region | Offers targeting multiple regions or worldwide |

### Classification Rules

```
Priority Order:
1. Explicit geo field in offer data → Direct match
2. Country code in offer name/description → Map to region
3. Tracking link domain TLD hint → Infer region
4. Default → Flag for manual review
```

### Execution Flow

```
1. Input: Parsed Wish List (standardized 8-column format)
   ↓
2. For each offer row:
   a. Check geo_target field (if populated)
   b. Scan offer_name for country keywords
   c. Check tracking_link domain hints
   d. Apply classification rules with confidence score
   ↓
3. Group offers by classified region
   ↓
4. Generate per-region Excel files:
   ├── MENA_Offers.xlsx
   ├── LATAM_Offers.xlsx
   ├── APAC_Offers.xlsx
   ├── EU_US_Offers.xlsx
   └── GLOBAL_Offers.xlsx
   ↓
5. Generate summary report:
   - Total offers per region
   - Classification confidence distribution
   - Items flagged for manual review
```

### Output Structure

Each regional file contains the same 8-column schema plus:

| Additional Column | Description |
|--------------------|-------------|
| `region_code` | Auto-assigned region code |
| `confidence` | Classification confidence (High/Medium/Low) |
| `classification_source` | Which rule matched (geo_field/keyword/domain/manual) |

### Key Features

- **5-zone coverage**: Covers all major affiliate markets
- **Confidence scoring**: Low-confidence items flagged for human review
- **Bidirectional sync**: Regional files can be merged back to master
- **Template-based output**: Uses pre-formatted Excel templates per region

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`regional_classifier.py`](scripts/regional_classifier.py) | Executable script |

### Dependencies

```python
pandas >= 1.5.0
openpyxl >= 3.1.0
```

### Integration

Invoke after `wish-intelligence-collector` completes. The agent chains these two skills automatically when processing new Wish Lists.
