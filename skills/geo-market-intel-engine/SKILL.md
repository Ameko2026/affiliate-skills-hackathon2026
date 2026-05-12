---
name: geo-market-intel-engine
display_name: "Geo Market Intelligence Engine | 区域市场情报引擎"
description: "Multi-region market intelligence aggregator for affiliate business development. Collects and synthesizes top apps, market trends, competitor dynamics, and regulatory updates across MENA, LATAM, APAC, and Europe&US to support BD decision-making."
version: 1.0.0
category: business-intelligence
tags: [market-intelligence, competitive-analysis, bd-support, geo-expansion]
layer: 2
trigger_keywords:
  - "市场情报"
  - "竞品动态"
  - "geo intel"
  - "BD 支持"
---

# Geo Market Intelligence Engine
## 区域市场情报引擎

### Overview

Aggregates **multi-source market intelligence** into actionable regional briefs for business development.

### Intelligence Categories

| Category | Content | Frequency |
|----------|---------|-----------|
| **Top Apps** | Rankings by category (Fintech, E-comm, Gaming) | Weekly |
| **Market Size** | TAM/SAM by vertical & region | Quarterly |
| **Competitor Activity** | New entrants, pricing, launches | Weekly |
| **Regulatory** | Privacy laws, payment regulations | As-needed |

### Regional Coverage

- **MENA**: Saudi Arabia, UAE, Egypt — Fintech boom under Vision 2030
- **LATAM**: Brazil (Pix ecosystem), Mexico (BNPL growth)
- **APAC**: Indonesia, Thailand, Vietnam — Super-app dominance
- **Europe&US**: ATT impact, privacy-first targeting

### Report Template

```
{Region} Market Brief - Week of {Date}
=====================================
Top Apps (Fintech):
  1. App A - Installs est. +12% [Rising]
  2. App B - Installs est. Stable [Flat]

Competitor Intelligence:
  - Competitor X: Launched new offer in {vertical}
  - Partner Y: Expanded to {region}

BD Recommendations:
  1. Short-term: {action}
  2. Medium-term: {strategy}
```

### Execution Flow

1. Define target region(s) and categories
2. Fetch data from sources (app store APIs, news, reports)
3. Synthesize into structured brief format
4. Cross-reference with app_dnal data
5. Generate regional brief document
6. Distribute to stakeholders

### Dependencies

```python
requests >= 2.28.0
beautifulsoup4 >= 4.12.0  # Optional
pandas >= 1.5.0
```
