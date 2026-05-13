---
name: campaign-budget-analysis
display_name: "AI Budget Allocation Optimizer | AI 预算分配优化器"
description: |
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

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

# Campaign Budget Analysis Skill

## 概述

本skill用于营销campaign的预算分配和渠道有效性分析。通过合并AppsFlyer (AF)事件数据与CRM数据（如e-Grana转化数据），计算各渠道有效性并生成预算分配建议。

## 核心指标

| 指标 | 说明 |
|------|------|
| AF事件数 | AppsFlyer记录的有效事件（如conta_criada_sucesso_view） |
| CRM转化数 | CRM系统中实际转化用户数（如e-Grana） |
| 有效性 | `CRM转化数 / AF事件数 × 100%` |
| AF CAP | 建议的AF事件量上限 |
| 预计CRM | 基于有效性和CAP预计的CRM产出 |

## 有效性分类标准

| 分类 | 有效性范围 | Action建议 |
|------|------------|------------|
| ✅ 高有效性 | ≥30% | ↑增加 (Factor 1.2) |
| ⚡ 中有效性 | 20-30% | →维持 (Factor 1.0) |
| ⚠️ 低有效性 | <20% | ↓控制 (Factor 0.5) |

## 工作流程

### Step 1: 数据准备

读取以下数据源：
- AF事件数据：包含channel、事件数、appsflyer_id等
- CRM转化数据：包含source bank、转化用户数等

关键字段映射：
- Channel标识：`source bank`或channel字段
- 关联键：`v_appsflyer_id`（需去重）

### Step 2: 数据处理

```python
# 合并AF和CRM数据
df = pd.merge(af_data, crm_data, on='channel', how='left')

# 计算有效性
df['有效性'] = df['CRM转化数'] / df['AF事件数'] * 100

# 分类
df['分类'] = df['有效性'].apply(
    lambda x: '高' if x >= 30 else ('中' if x >= 20 else '低')
)

# 计算AF CAP
df['Factor'] = df['有效性'].apply(
    lambda x: 1.2 if x >= 30 else (1.0 if x >= 20 else 0.5)
)
df['AF_CAP'] = (df['AF事件数'] * df['Factor']).astype(int)

# 计算预计CRM
df['预计CRM'] = (df['AF_CAP'] * df['有效性'] / 100).astype(int)
```

### Step 3: 生成Excel报告

输出文件包含以下Sheet：
1. **Channel Validity Data**: 按有效性分类的完整数据
2. **Summary**: 分类汇总和整体有效性

Excel格式要求：
- 表头：深蓝色背景+白色粗体字
- 高有效性行：绿色背景
- 中有效性行：黄色背景
- 低有效性行：红色背景
- 小计行：灰色背景
- 总计行：深蓝色背景+白色字
- 有效性列格式：百分比（如25.8%）
- 数值列：整数，千分位分隔

### Step 4: 预算校验

```
总AF CAP = Σ(各Channel AF CAP)
预计总CRM = Σ(各Channel 预计CRM)
整体有效性 = 预计总CRM / 总AF CAP × 100%

目标达成率 = 预计总CRM / CRM目标 × 100%
```

## 脚本资源

### scripts/create_validity_excel.py

生成Channel有效性分析Excel的核心脚本：

```python
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# 使用说明：
# 1. 准备CSV文件：Channel,Validity,AF_apr,Factor,AF_CAP,Est_CRM,PID_count,Action
# 2. 运行脚本生成Excel
# 3. Excel打开后自动计算公式
```

### references/jxxxx_example.csv

JXXXX 5月预算分配示例数据，包含23个channel的有效性分析。

## 输出示例

### Channel有效性数据表

| Channel | Validity | AF Apr | AF CAP | Est. CRM | Action |
|---------|----------|--------|--------|----------|--------|
| bromo_mob | 25.8% | 4,807 | 2,207 | 569 | →维持 |
| nain_mob | 27.9% | 1,755 | 805 | 224 | →维持 |
| ... | ... | ... | ... | ... | ... |

### 汇总表

| 分类 | Channel数 | AF CAP | 预计CRM |
|------|-----------|--------|---------|
| 高有效性 | 9 | 144 | 46 |
| 中有效性 | 12 | 4,205 | 1,118 |
| 低有效性 | 2 | 80 | 14 |
| **总计** | **23** | **4,429** | **~1,178** |

## 注意事项

1. **数据去重**：按`v_appsflyer_id`去重，排除特定事件（如af_purchase_esim）
2. **渠道归因**：Source Bank确定渠道归属，不依赖PID
3. **渠道变体**：按共同前缀合并（如bromo_mob_apr → bromo_mob）
4. **分层输出**：高/中/低三档分区显示，便于决策

## 触发词

- "预算分配"、"预算规划"、"campaign分析"
- "channel有效性"、"渠道有效性"、"有效性分析"
- "AF CAP"、"预算建议"、"CRM转化"
- "预算报告"、"Excel报告"、"数据分析报告"

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`budget_optimizer.py`](scripts/budget_optimizer.py) | Executable script |

