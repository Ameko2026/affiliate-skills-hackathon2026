---
name: nxxx-analysis
display_name: "Cross-Regional Revenue Audit Agent | 跨区域收入审计智能体"
description: NXXX Campaign 全链路盈亏分析。合并 AppsFlyer（AOS+iOS）与 GH 结算表数据，自动生成 7 Sheet Excel 报告，覆盖 GH 数据补充、新旧收入对比、下游成本计算、PID/Channel 维度盈亏、account campaign 结算率分析。适用于每月 NXXX Campaign 项目结算与盈利分析。
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
  - "App A 分析"

---

# nxxx-analysis

NXXX（巴西数字银行）项目的全链路盈亏分析工具。从 AppsFlyer 原始数据和 GH 结算表出发，自动生成带样式的 7 Sheet Excel 报告。

## 适用场景

- 每月 NXXX 项目结算，需计算新旧方案收入对比与盈亏
- 需要 PID / Channel 维度的精细化盈利分析
- 需要按 accnt / crd 双产品线拆解成本和利润
- 需要不同 accnt 结算率（50%/60%）下的利润敏感性分析

## 数据源

### 1. AppsFlyer CSV（AOS + iOS）

- **文件名格式**: `{package_name}_in-app-events_{start}_{end}_UTC.csv`
- **AOS 包名**: `br.com.nxxx`
- **iOS ID**: `id1127996388`
- **关键字段**: `AppsFlyer ID`, `Media Source`, `Channel`, `Campaign`, `Event Name`, `Event Time`, `Is Primary Attribution`, `Customer User ID`
- **关键事件**:
  - `accnt_approved_stts` — 开户成功（accnt 产品线）
  - `crd_pre_approved_stts` — 信用卡预批（crd 产品线）
- **筛选**: 仅取 `Is Primary Attribution == True` 的记录

### 2. GH 结算表（xlsx）

- **新格式列名**（header=0）: `date, source, parceiro, gh, valor_unitario, qtde_sinais, cost_bruto`
- **字段映射**:
  | 原始列名 | 映射名 | 说明 |
  |---|---|---|
  | `date` | Date | 日期 |
  | `parceiro` | PID | 对应 Media Source |
  | `gh` | GH | 等级 1-9（可能含10） |
  | `qtde_sinais` | Count | 转化数量 |
  | `cost_bruto` | revenue_BRL | 毛收入（BRL） |
  | `valor_unitario` | unit_price_raw | 单价（备用验证） |

- **GH 单价字典**（BRL）:

  | GH | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 |
  |---|---|---|---|---|---|---|---|---|---|---|
  | R$ | 0 | 0 | 0 | 5 | 10 | 20 | 40 | 150 | 200 | 300 |

- **注意**: GH1-3 无收入；收入以 `cost_bruto` 列为准（已验证与单价字典一致）

## 核心计算逻辑

### Campaign 分类

```python
df['is_apr'] = df['Campaign'].str.contains('_apr_', na=False)
# True → accnt 产品线（开户）
# False → crd 产品线（信用卡）
```

### 去重规则

| 产品线 | 事件 | 去重方式 | 说明 |
|---|---|---|---|
| crd（方式1） | `crd_pre_approved_stts` | AF ID 去重（取最早 Event Time） | 非 `_apr_` campaign |
| accnt（方式2） | `accnt_approved_stts` | 双重去重 | 含 `_apr_` campaign |

**accnt 双重去重流程**:
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

**方式1（crd 阶梯成本）**:
- Channel 粒度计算，≤150 个 @$4.5，>150 个 @$5.5
- 各 PID 按该 Channel 内的转化占比分摊成本

```python
def tiered_cost(n, r1=4.5, r2=5.5, tier=150):
    if n <= tier:
        return n * r1
    return tier * r1 + (n - tier) * r2
```

**方式2（accnt 固定成本）**:
- $1 / 转化 × 结算率（50% 或 60%）
- Sheet 3 按 100% 计算（$1/conv）
- Sheet 7 分别展示 50% 和 60% 结算率

### 汇率

- 1 USD = 4.980259 BRL（固定值，按实际结算周期更新）

## 输出报告结构（7 Sheet）

### Sheet 1: GH 数据补充

按 Date + PID 交叉展示:
- GH1-GH9 各等级转化数
- GH 总数
- AF Primary 的 accnt / crd 事件计数

### Sheet 2: 收入对比

- **旧方案**: crd AF ID 去重 × R$100
- **新方案**: GH 表 `cost_bruto` 合计
- GH 分层收入明细（按 GH 等级）
- 按 PID 收入明细

### Sheet 3: 下游渠道成本

- 成本总览（方式1 + 方式2）
- 方式1 明细（Channel → PID → OS → 阶梯成本）
- 方式2 明细（Channel → PID → OS → $1/conv）
- 按 Channel 汇总

### Sheet 4: 盈亏总览

| 项目 | 旧方案 | 新方案 |
|---|---|---|
| NXXX 收入 (BRL/USD) | crd × R$100 | GH cost_bruto |
| 下游成本 (USD) | 方式1+方式2 | 方式1+方式2 |
| 毛利 (USD) | 收入 - 成本 | 收入 - 成本 |
| 毛利率 (%) | 毛利/收入 | 毛利/收入 |

### Sheet 5: PID 维度盈亏

每个 PID 的完整盈亏拆解（Channel、旧/新方案收入、成本、毛利、毛利率），按新方案毛利排序。

### Sheet 6: Channel 维度盈亏

Channel 粒度汇总（PID 数、收入、成本、毛利），含新旧毛利差额。底部附盈亏分类统计。

### Sheet 7: accnt Campaign 分析

accnt 产品线按 Channel 汇总，分别展示 50% 和 60% 结算率下的成本、毛利和毛利率。

## 脚本

| 文件 | 路径 | 说明 |
|---|---|---|
| 统一报告脚本 | `/Users/analyst/work/nxxx_report_0429.py` | 生成全部 7 Sheet |
| 输出示例 | `/Users/analyst/work/NXXX_Analysis_Report_0429.xlsx` | 4/1-4/29 报告 |

## 使用方式

当用户说"跑 NXXX 分析"、"生成 NXXX 报告"、"NXXX 盈亏"等，或提到 NXXX 项目的月度结算分析时，加载此 Skill。

### 操作步骤

1. **确认数据范围**: 询问用户要分析的日期范围
2. **定位数据文件**: 在 `~/Downloads/` 下查找匹配的 AF CSV 和 GH xlsx
   - AF CSV: `br.com.nxxx_in-app-events_*_UTC.csv` 和 `id1127996388_in-app-events_*_UTC.csv`
   - GH xlsx: 文件名含 "M COMPANY" + "NXXX" + "GHs"
3. **检查 GH 表格式**: 读取 xlsx 的列名，判断是旧格式（header=1）还是新格式（header=0）
   - 新格式: `date, parceiro, gh, cost_bruto` 等
   - 旧格式: `GH, Date, PID, Count` 等
4. **更新脚本参数**: 修改 `nxxx_report_0429.py` 中的文件路径和日期范围
5. **运行脚本**: `python3 nxxx_report_0429.py`
6. **检查输出**: 验证 Excel 文件中的数据是否合理（总行数、金额等）
7. **交付报告**: 将 xlsx 文件交付给用户

### 数据调整注意事项

- 如果 GH 表格式变化（列名不同），需要调整 `rename()` 映射
- 如果汇率更新，修改 `USD_TO_BRL` 常量
- 如果阶梯成本参数变化，修改 `tiered_cost()` 默认参数
- 如果结算率变化（非 50%/60%），修改 Sheet 7 中的计算
- PID→Channel merge 时可能出现 suffix 冲突（如 `Channel` 和 `Channel_map`），需用 `fillna` 合并

## 已知限制

- GH 表通常不含 GH10 数据（如遇到需确认）
- GH 表可能缺少最后 1-2 天数据（结算延迟）
- 旧方案仅计算 crd 收入，不含 accnt
- 收入数据以 BRL 计价，需换算 USD 对比成本

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`revenue_audit.py`](scripts/revenue_audit.py) | Executable script |

