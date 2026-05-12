---
name: conversion-funnel-intelligence
display_name: "Conversion Funnel Intelligence | 转化漏斗智能分析"
description: "Analyzes conversion funnel performance for fintech/app verticals. Identifies funnel bottlenecks, projects conversion rates at each stage, and generates CAP (capacity) planning recommendations with color-coded effectiveness ratings for each traffic source."
version: 1.0.0
category: business-intelligence
tags: [funnel-analysis, conversion-rate, cap-planning, fintech, affiliate]
layer: 2
trigger_keywords:
  - "转化漏斗"
  - "漏斗分析"
  - "CAP 规划"
  - "funnel analysis"
  - "Vertical A 漏斗"
---

# Conversion Funnel Intelligence
## 转化漏斗智能分析

### Overview

Deep-dive funnel analysis for app install-to-conversion pipelines. Identifies where users drop off and which channels deliver the highest-quality users through the full funnel.

### Funnel Stages (Configurable per Vertical)

Default funnel for fintech/lending app vertical:

```
Stage 1: Impression        → Ad shown to user
Stage 2: Click             → User clicks ad
Stage 3: Install           → App installed
Stage 4: Registration      → Account created
Stage 5: KYC Completed     → Identity verified
Stage 6: First Loan/Transaction → First conversion event
Stage 7: Repeat Usage      → Return user (retention signal)
```

### Analysis Dimensions

| Dimension | Description |
|-----------|-------------|
| **By Channel** | Funnel conversion rates per traffic source |
| **By Region** | Geographic differences in funnel behavior |
| **By Cohort** | Weekly/monthly cohorts for trend analysis |
| **By Creative** | Ad creative performance impact on funnel stages |

### Key Metrics

```python
# Stage-to-stage conversion rate
CR_stage = (Users_at_next_stage / Users_at_current_stage) * 100

# Overall funnel conversion
Overall_CR = (Users_at_final_stage / Users_at_first_stage) * 100

# Drop-off rate (identifies bottlenecks)
Dropoff_Rate = 100 - CR_stage

# Channel Quality Score (composite)
Quality_Score = (
    w1 * Install_to_Reg_CR +
    w2 * Reg_to_KYC_CR +
    w3 * KYC_to_Conversion_CR +
    w4 * Retention_Rate_7day
)
```

### Bottleneck Detection Algorithm

```
For each stage transition:
  1. Calculate CR for each channel
  2. Compute mean CR and std dev across channels
  3. Flag bottleneck if:
     - CR < (mean - 2*std)  [significantly below average]
     - OR Dropoff_Rate > 50%  [more than half drop off]
  4. Rank bottlenecks by severity (impact × frequency)
  
Output: Ranked list of bottleneck stages with affected channels
```

### CAP Planning Recommendations

Based on funnel analysis, generate CAP suggestions:

| Funnel Signal | CAP Recommendation | Rationale |
|---------------|-------------------|-----------|
| High install CR, low conversion CR | ⬇️ Reduce CAP | Low-quality installs |
| Low install CR, high conversion CR | ⬆️ Increase CAP | High-quality but volume-limited |
| Balanced funnel (all CR > threshold) | ➡️ Hold or slight ⬆️ | Healthy channel |
| All CR below threshold | ❌ Pause channel | Systemic quality issue |

### Output Format

#### Sheet 1: Funnel Visualization Data

| Channel | Stage1→2 CR | Stage2→3 CR | Stage3→4 CR | Stage4→5 CR | Stage5→6 CR | Stage6→7 CR | Overall CR |
|---------|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:-----------:|:----------:|
| Ch_A | 45.2% | 78.3% | 62.1% | 85.0% | 34.2% | 67.8% | **4.9%** |
| Ch_B | 32.1% | 65.4% | 48.9% | 72.1% | 21.3% | 55.6% | **1.6%** |

#### Sheet 2: Bottleneck Report

| Rank | Channel | Bottleneck Stage | CR | vs Avg | Severity | Action |
|------|---------|------------------|----:|--------:|----------|--------|
| 1 | Ch_B | Registration→KYC | 48.9% | -22% | 🔴 Critical | Investigate UX friction |
| 2 | Ch_A | KYC→Conversion | 34.2% | -15% | 🟠 Warning | Review offer targeting |

#### Sheet 3: CAP Recommendations

| Channel | Current CAP | Recommended CAP | Reason | Priority |
|---------|:----------:|:--------------:|--------|----------|
| Ch_A | 500/day | 650/day | Strong post-KYC conversion | P2 |
| Ch_B | 800/day | 300/day | Severe KYC dropoff | P1 |
| Ch_C | 200/day | 400/day | Consistent high quality | P2 |

### Color Coding Legend

| Color | Meaning |
|-------|---------|
| 🟢 Green | High effectiveness (above 75th percentile) |
| 🟡 Yellow | Moderate effectiveness (25th-75th percentile) |
| 🔴 Red | Low effectiveness (below 25th percentile) |
| ⚪ Gray | Insufficient data |

### Dependencies

```python
pandas >= 1.5.0
openpyxl >= 3.1.0
numpy >= 1.24.0
```
