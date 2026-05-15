---
name: product-a-analysis
display_name: "Cross-Regional Revenue Audit Agent | 跨区域收入审计智能体"
description: |
  This skill should be used when the user needs to perform full-chain profit & loss (P&L) analysis for a specific product (Product_A) across multiple MMP data sources.
  
  It merges AppsFlyer (Android + iOS) event data with settlement data, applies multi-step deduplication logic, calculates revenue and costs at PID/Channel dimensions, and generates a styled 7-sheet Excel report covering P&L, funnel analysis, and settlement rate sensitivity.
  
  Applicable for monthly campaign settlement reconciliation and profitability analysis in affiliate marketing operations.
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

category: dataops-automation
tags: [revenue-audit, p-and-l, roi-analysis, financial-reporting, affiliate]
layer: 1
trigger_keywords:
  - "盈亏分析"
  - "P&L 报告"
  - "ROI 审计"
  - "收入核算"
  - "Product_A 分析"

---

# product-a-analysis

Product_A 项目的全链路盈亏分析工具。从 AppsFlyer 原始数据和结算表出发，自动生成带样式的 7 Sheet Excel 报告。

## 适用场景

- 每月 Product_A 项目结算，需计算新旧方案收入对比与盈亏
- 需要 PID / Channel 维度的精细化盈利分析
- 需要按产品线拆解成本和利润
- 需要不同结算率下的利润敏感性分析

## 数据源

### 1. AppsFlyer CSV（AOS + iOS）

- **文件名格式**: `{package_name}_in-app-events_{start}_{end}_UTC.csv`
- **AOS 包名**: `com.example.product_a`
- **iOS ID**: `idXXXXXXXX`
- **关键字段**: `AppsFlyer ID`, `Media Source`, `Channel`, `Campaign`, `Event Name`, `Event Time`, `Is Primary Attribution`, `Customer User ID`
- **关键事件**:
  - `product_a_event_a` — 事件A（产品线A）
  - `product_a_event_b` — 事件B（产品线B）
- **筛选**: 仅取 `Is Primary Attribution == True` 的记录

### 2. 结算表（xlsx）

- **新格式列名**（header=0）: `date, source, partner, tier, value_unit, quantity, cost_gross`
- **字段映射**:
  | 原始列名 | 映射名 | 说明 |
  |---|---|---|
  | `date` | Date | 日期 |
  | `partner` | PID | 对应 Media Source |
  | `tier` | Tier | 等级 1-9（可能含10） |
  | `quantity` | Count | 转化数量 |
  | `cost_gross` | revenue | 毛收入 |
  | `value_unit` | unit_price_raw | 单价（备用验证） |

- **Tier 单价字典**（示例货币单位）：
  | Tier | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | 示例 | 0 | 0 | 0 | 5 | 10 | 20 | 40 | 150 | 200 | 300 |

- **注意**: 低等级无收入；收入以 `cost_gross` 列为准

## 核心计算逻辑

### Campaign 分类

```python
df['is_line_a'] = df['Campaign'].str.contains('_variant_a_', na=False)
# True → 产品线A
# False → 产品线B
```

### 去重规则

| 产品线 | 事件 | 去重方式 | 说明 |
|---|---|---|---|
| 产品线B | `event_b` | AF ID 去重（取最早 Event Time） | 非 variant_a campaign |
| 产品线A | `event_a` | 双重去重 | 含 variant_a campaign |

**产品线A 双重去重流程**:
1. 先按 `AppsFlyer ID` 去重（取最早）
2. 对有 `Customer User ID` 的记录，再按 `Customer User ID` 去重（取最早）
3. 无 Customer User ID 的保留不动
4. 合并两部分

### PID → Channel 映射

```python
# 每个 Media Source(PID) 归入其出现次数最多的 Channel
pid_ch_map = df.groupby(['Media Source', 'Channel']).size()
    .reset_index().sort_values('cnt', ascending=False)
    .groupby('Media Source').first()
```

### 下游成本计算

**方式1（阶梯成本）**:
- Channel 粒度计算，≤150 个 @$4.5，>150 个 @$5.5
- 各 PID 按该 Channel 内的转化占比分摊成本

```python
def tiered_cost(n, r1=4.5, r2=5.5, tier=150):
    if n <= tier:
        return n * r1
    return tier * r1 + (n - tier) * r2
```

**方式2（固定成本）**:
- $1 / 转化 × 结算率（50% 或 60%）
- Sheet 3 按 100% 计算（$1/conv）
- Sheet 7 分别展示 50% 和 60% 结算率

### 汇率

- 使用固定汇率，按实际结算周期更新

## 输出报告结构（7 Sheet）

### Sheet 1: 数据补充

按 Date + PID 交叉展示各等级转化数和数据统计。

### Sheet 2: 收入对比

- **旧方案**: 某指标 × 单价
- **新方案**: 结算表 cost_gross 合计
- Tier 分层收入明细（按等级）
- 按 PID 收入明细

### Sheet 3: 下游渠道成本

- 成本总览（方式1 + 方式2）
- 方式1 明细（Channel → PID → OS → 阶梯成本）
- 方式2 明细（Channel → PID → OS → $1/conv）
- 按 Channel 汇总

### Sheet 4: 盈亏总览

| 项目 | 旧方案 | 新方案 |
|---|---|---|
| Product_A 收入 | 某指标 × 单价 | cost_gross |
| 下游成本 (USD) | 方式1+方式2 | 方式1+方式2 |
| 毛利 (USD) | 收入 - 成本 | 收入 - 成本 |
| 毛利率 (%) | 毛利/收入 | 毛利/收入 |

### Sheet 5: PID 维度盈亏

每个 PID 的完整盈亏拆解（Channel、旧/新方案收入、成本、毛利、毛利率），按新方案毛利排序。

### Sheet 6: Channel 维度盈亏

Channel 粒度汇总（PID 数、收入、成本、毛利），含新旧毛利差额。底部附盈亏分类统计。

### Sheet 7: 产品线A Campaign 分析

产品线A 按 Channel 汇总，分别展示 50% 和 60% 结算率下的成本、毛利和毛利率。

## 脚本

| 文件 | 说明 |
|---|---|
| 统一报告脚本 | `./scripts/revenue_audit.py` | 生成全部 7 Sheet |
| 输出示例 | `./output/Product_A_Analysis_Report_YYYYMMDD.xlsx` | 示例报告 |

## 使用方式

当用户说"跑 Product_A 分析"、"生成 Product_A 报告"、"Product_A 盈亏"等，或提到 Product_A 项目的月度结算分析时，加载此 Skill。

### 操作步骤

1. **确认数据范围**: 询问用户要分析的日期范围
2. **定位数据文件**: 在下载目录查找匹配的 AF CSV 和结算 xlsx
   - AF CSV: 包名/ID 相关的 in-app-events CSV
   - 结算 xlsx: 包含结算数据的文件
3. **检查表格式**: 读取 xlsx 的列名，判断格式
4. **更新脚本参数**: 修改脚本中的文件路径和日期范围
5. **运行脚本**: `python3 scripts/revenue_audit.py`
6. **检查输出**: 验证 Excel 文件中的数据是否合理
7. **交付报告**: 将 xlsx 文件交付给用户

### 数据调整注意事项

- 如果表格式变化（列名不同），需要调整映射
- 如果汇率更新，修改常量
- 如果阶梯成本参数变化，修改参数
- 如果结算率变化（非 50%/60%），修改计算
- PID→Channel merge 时可能出现 suffix 冲突，需用 fillna 合并

## 已知限制

- 结算表通常不含高等级数据（如遇到需确认）
- 结算表可能缺少最后 1-2 天数据（延迟）
- 旧方案仅计算部分收入
- 收入数据需换算对比成本

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`revenue_audit.py`](scripts/revenue_audit.py) | Executable script |

