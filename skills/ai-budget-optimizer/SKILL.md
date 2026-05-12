---
name: ai-budget-optimizer
display_name: "AI Budget Allocation Optimizer | AI 预算分配优化器"
description: "Data-driven budget allocation optimizer for multi-channel affiliate campaigns. Analyzes historical channel effectiveness (ROI, decay rates, quality scores), applies attenuation models, and generates optimized budget distribution recommendations with CAP adjustments for each channel."
version: 1.0.0
category: dataops-automation
tags: [budget-allocation, optimization, roi, campaign-management, affiliate]
layer: 1
trigger_keywords:
  - "预算分配"
  - "预算优化"
  - "budget allocation"
  - "渠道有效性"
  - "CAP 建议"
---

# AI Budget Allocation Optimizer
## AI 预算分配优化器

### Overview

Replaces experience-driven budget decisions with a **quantitative framework** that analyzes each channel's historical performance and recommends optimal budget distribution.

### Input Data Requirements

| Data Type | Source | Required Fields |
|-----------|--------|-----------------|
| Historical spend | Ad Network / App Dnal DB | channel, date, spend |
| Conversion data | MMP | channel, installs, events, revenue |
| Quality signals | App Dnal scoring | channel, retention_rate, fraud_rate |
| Current constraints | User input | total_budget, min_per_channel, max_per_channel |

### Optimization Model

```
Channel Score = f(ROI, Volume, Quality, Decay, Risk)

Where:
  ROI_Score     = normalized ROI percentile (0-100)
  Volume_Score  = normalized install volume percentile (0-100)
  Quality_Score = weighted avg of (retention_rate, fraud_inverse, LTV)
  Decay_Factor  = time-decay weight (recent performance > older)
  Risk_Penalty  = deduction for high-variance channels

Final Budget Share_i = (Score_i / Σ Score_j) × Total_Budget
```

### Attenuation Model

Accounts for the fact that **doubling spend does not double returns**:

```
Effective_Returns = Base_Returns × (1 - e^(-α × Spend_Increment))

Where α is the channel-specific saturation coefficient
(learned from historical spend-response curves)
```

### Execution Flow

```
1. Load historical performance data (last 4-8 weeks recommended)
   ↓
2. Calculate per-channel KPIs:
   - ROI, CPA, LTV, Retention Rate, Fraud Rate
   - Spend elasticity (how much return per additional $)
   ↓
3. Apply attenuation model to project diminishing returns
   ↓
4. Run optimization: maximize total expected ROI subject to constraints
   ↓
5. Generate recommendations:
   ├── Budget allocation table (% and $ amount)
   ├── CAP adjustment suggestions (increase/decrease/hold)
   ├── Risk warnings for volatile channels
   └── Expected portfolio ROI after reallocation
   ↓
6. Output formatted Excel with color-coded recommendations
```

### Output Format

#### Sheet 1: Budget Allocation Recommendation

| Channel | Current Budget | Recommended Budget | Δ % | Expected ROI | Confidence | Action |
|---------|:-------------:|:------------------:|:---:|:------------:|:----------:|--------|
| Ch_A | $5,000 | $7,000 | +40% | 52% | High | ⬆️ Increase |
| Ch_B | $8,000 | $4,000 | -50% | -12% | High | ⬇️ Decrease |
| Ch_C | $3,000 | $3,500 | +17% | 35% | Medium | ➡️ Hold+ |

#### Sheet 2: Channel Effectiveness Heatmap

Matrix showing channels × KPIs with color intensity representing performance.

#### Sheet 3: Scenario Comparison

| Scenario | Total Budget | Expected Portfolio ROI | Risk Level |
|----------|:-----------:|:---------------------:|:----------:|
| Current Allocation | $50,000 | 18.2% | Medium |
| Optimized Allocation | $50,000 | 27.8% | Low |
| Conservative (low risk) | $50,000 | 22.1% | Very Low |
| Aggressive (high risk) | $50,000 | 34.5% | High |

### Key Features

- **Quantitative over qualitative**: Every recommendation backed by numbers
- **Attenuation awareness**: Doesn't blindly scale top performers
- **Risk-adjusted**: Penalizes high-variance channels
- **Constraint-aware**: Respects min/max budgets per channel
- **Scenario modeling**: Shows conservative vs aggressive options

### Dependencies

```python
pandas >= 1.5.0
openpyxl >= 3.1.0
numpy >= 1.24.0  # For numerical optimization
scipy >= 1.10.0  # Optional: for advanced optimization algorithms
```
