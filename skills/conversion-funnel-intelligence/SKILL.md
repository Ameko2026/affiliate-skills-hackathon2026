---
name: jxxxx-funnel
display_name: "Conversion Funnel Intelligence | 转化漏斗智能分析"
description: |
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

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

# jxxxx-funnel

Conversion Funnel Intelligence — JXXXX 营销转化漏斗分析与预算规划工具。

适用于每月 JXXXX 渠道预算分配决策，核心输出：**各渠道 AF CAP 建议值** + **渠道保留策略**（低有效性渠道只降 CAP，不暂停）。

---

## 适用场景

- 每月 JXXXX 渠道预算分配，需计算各渠道有效性并推荐 AF CAP
- 需要合并 AppsFlyer 事件数据与 CRM 实际转化数据做漏斗分析
- 评估哪些渠道值得增加投放，哪些需要控制
- **重要原则**：保留全量渠道数据，不因低有效性暂停渠道（仅调整 CAP）

---

## 核心指标

| 指标 | 计算公式 | 说明 |
|------|---------|------|
| AF 事件数 | COUNT(af_events) | AppsFlyer 记录的 `conta_criada_sucesso_view` 事件数 |
| CRM 转化数 | COUNT(egrana_users) | e-Grana 中实际完成注册的用户数 |
| 有效性 | CRM转化数 / AF事件数 × 100% | 渠道质量核心指标 |
| AF CAP | AF事件数 × Factor | 建议的下月 CAP 上限 |
| 预计 CRM | AF_CAP × 有效性% | 按新 CAP 预期的 CRM 产出 |

---

## 核心事件

```
AppsFlyer 关键事件：conta_criada_sucesso_view
含义：账户创建成功（JXXXX 核心转化事件）
```

---

## 有效性分类与调整策略

| 分类 | 有效性范围 | Factor | Action |
|------|-----------|--------|--------|
| 高有效性 | ≥30% | 1.2 | 增加投放（提高CAP） |
| 中有效性 | 20%-30% | 1.0 | 维持不变 |
| 低有效性 | <20% | 0.5 | 降低CAP（但不暂停） |

**重要原则**：低有效性渠道降低 CAP 但不暂停，保留优化空间（巴西 Fintech 流量质量波动大）。

---

## 完整执行脚本

> 保存为 `jxxxx_funnel.py`，与 AF CSV 和 CRM xlsx 放在同一目录运行。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
jxxxx_funnel.py
Conversion Funnel Intelligence — JXXXX 漏斗分析完整脚本

功能：
1. 加载 AppsFlyer 事件数据（过滤 conta_criada_sucesso_view）
2. 按 AppsFlyer ID 去重（每设备取最早事件）
3. 加载 e-Grana CRM 转化数据（source_bank + user_count）
4. 按渠道合并，计算有效性（CRM转化数 / AF事件数）
5. 根据有效性分类，计算 Factor 和 AF CAP 建议
6. 输出带颜色标注的 Excel 报告（绿/黄/红）

用法：
    python3 jxxxx_funnel.py \
        --af jxxxx_in-app-events_*.csv \
        --crm egrana_crm.xlsx \
        --output jxxxx_funnel_result.xlsx
"""

import argparse
import pandas as pd
import sys
from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment
from openpyxl.utils.dataframe import dataframe_to_rows
from openpyxl.utils import get_column_letter

# ── 配置区 ─────────────────────────────────────────────
TARGET_EVENT = 'conta_criada_sucesso_view'  # JXXXX 核心转化事件
VALIDITY_HIGH = 30   # % 以上 → 高有效性
VALIDITY_MID = 20    # % 以上 → 中有效性，以下 → 低有效性


def classify_validity(pct: float) -> str:
    if pct >= VALIDITY_HIGH:
        return '高有效性'
    elif pct >= VALIDITY_MID:
        return '中有效性'
    else:
        return '低有效性'


def get_factor(pct: float) -> float:
    if pct >= VALIDITY_HIGH:
        return 1.2
    elif pct >= VALIDITY_MID:
        return 1.0
    else:
        return 0.5


def get_action(pct: float) -> str:
    if pct >= VALIDITY_HIGH:
        return '增加投放（提高CAP）'
    elif pct >= VALIDITY_MID:
        return '维持不变'
    else:
        return '降低CAP（但不暂停）'


def find_column(df: pd.DataFrame, candidates: list) -> str | None:
    """在 DataFrame 列名中查找第一个匹配的列（忽略大小写）"""
    df_cols_lower = {c.lower(): c for c in df.columns}
    for c in candidates:
        if c in df.columns:
            return c
        if c.lower() in df_cols_lower:
            return df_cols_lower[c.lower()]
    return None


def main():
    parser = argparse.ArgumentParser(
        description='Conversion Funnel Intelligence — JXXXX 漏斗分析工具'
    )
    parser.add_argument('--af', required=True, help='AppsFlyer 事件 CSV 文件路径')
    parser.add_argument('--crm', required=True, help='e-Grana CRM xlsx 文件路径')
    parser.add_argument('--output', default='jxxxx_funnel_result.xlsx', help='输出 Excel 路径')
    parser.add_argument('--target-event', default=TARGET_EVENT,
                        help=f'目标事件名（默认 {TARGET_EVENT}）')
    args = parser.parse_args()

    target_event = args.target_event

    # ── Step 1：加载 AppsFlyer 数据 ──────────────────
    print(f'[Step 1] 加载 AppsFlyer 数据：{args.af}')
    try:
        af = pd.read_csv(args.af, low_memory=False)
    except Exception as e:
        print(f'ERROR: 无法读取 AF CSV 文件：{e}')
        sys.exit(1)

    print(f'  AF 数据总行数：{len(af)}')

    id_col = find_column(af, ['AppsFlyer ID', 'v_appsflyer_id'])
    event_col = find_column(af, ['Event Name', 'event_name'])
    time_col = find_column(af, ['Event Time', 'event_time'])
    channel_col = find_column(af, ['Channel', 'channel'])
    media_source_col = find_column(af, ['Media Source', 'media_source'])
    primary_col = find_column(af, ['Is Primary Attribution', 'is_primary_attribution'])

    if not id_col or not event_col:
        print(f'ERROR: AF 数据缺少必要字段（需要 AppsFlyer ID + Event Name）')
        print(f'  可用字段：{list(af.columns)}')
        sys.exit(1)

    print(f'  字段映射：ID={id_col}, Event={event_col}, Time={time_col}')
    print(f'  Channel={channel_col}, Primary={primary_col}')

    # ── Step 2：过滤目标事件 + 主归因 ─────────────────
    print(f'[Step 2] 过滤目标事件：{target_event}')
    before = len(af)
    af = af[af[event_col] == target_event]
    after_event = len(af)
    print(f'  按事件名过滤：{before} → {after_event} 行')

    if primary_col:
        before_p = len(af)
        af[primary_col] = af[primary_col].astype(str).str.lower().isin(['true', '1', 'yes'])
        af = af[af[primary_col] == True]
        after_p = len(af)
        print(f'  保留主归因（{primary_col}=True）：{before_p} → {after_p} 行')
    else:
        print('  ⚠ 未找到 Is Primary Attribution 字段，跳过主归因过滤')

    # ── Step 3：按 AppsFlyer ID 去重（取最早事件）───
    print(f'[Step 3] 按 {id_col} 去重（保留最早事件）...')
    af[time_col] = pd.to_datetime(af[time_col], errors='coerce')
    af_dedup = (af
        .sort_values(time_col)
        .groupby(id_col)
        .first()
        .reset_index())
    print(f'  去重后行数：{len(af_dedup)}（移除 {len(af) - len(af_dedup)} 条重复）')

    # ── Step 4：按渠道汇总 AF 事件数 ──────────────────
    print('[Step 4] 按渠道汇总 AF 事件数...')
    group_col = channel_col if channel_col else media_source_col
    if not group_col:
        print('ERROR: 找不到 Channel 或 Media Source 字段，无法按渠道汇总')
        sys.exit(1)

    af_by_channel = (af_dedup
        .groupby(group_col)
        .size()
        .reset_index(name='af_events'))
    print(f'  渠道数：{len(af_by_channel)}')
    print(f'  AF 事件数 Top5：')
    for row in af_by_channel.nlargest(5, 'af_events').itertuples(index=False):
        ch = getattr(row, group_col)
        cnt = row.af_events
        print(f'    {ch}: {cnt:,}')

    # ── Step 5：加载 e-Grana CRM 数据 ───────────────
    print(f'[Step 5] 加载 e-Grana CRM 数据：{args.crm}')
    try:
        crm = pd.read_excel(args.crm)
    except Exception as e:
        print(f'ERROR: 无法读取 CRM xlsx 文件：{e}')
        sys.exit(1)

    print(f'  CRM 数据行数：{len(crm)}')

    crm_channel_col = find_column(crm, ['source_bank', 'source', 'channel', 'Channel'])
    crm_count_col = find_column(crm, ['user_count', 'conversions', 'users', 'count'])

    if not crm_channel_col or not crm_count_col:
        print(f'ERROR: CRM 数据缺少必要字段（需要渠道名列 + 用户数列）')
        print(f'  可用字段：{list(crm.columns)}')
        sys.exit(1)

    print(f'  CRM 字段映射：Channel={crm_channel_col}, Count={crm_count_col}')

    crm_by_channel = (crm
        .groupby(crm_channel_col)[crm_count_col]
        .sum()
        .reset_index(name='crm_conversions'))
    print(f'  CRM 渠道数：{len(crm_by_channel)}')

    # ── Step 6：合并 AF + CRM，计算有效性 ───────────
    print('[Step 6] 合并 AF + CRM，计算有效性...')
    result = af_by_channel.merge(crm_by_channel, left_on=group_col, right_on=crm_channel_col, how='left')
    result['crm_conversions'] = result['crm_conversions'].fillna(0).astype(int)

    # 计算有效性（避免除零）
    result['validity_pct'] = result.apply(
        lambda row: round(row['crm_conversions'] / row['af_events'] * 100, 2)
        if row['af_events'] > 0 else 0,
        axis=1
    )

    # 分类 + Factor + Action
    result['classification'] = result['validity_pct'].apply(classify_validity)
    result['factor'] = result['validity_pct'].apply(get_factor)
    result['af_cap'] = (result['af_events'] * result['factor']).astype(int)
    result['est_crm'] = (result['af_cap'] * result['validity_pct'] / 100).astype(int)
    result['action'] = result['validity_pct'].apply(get_action)

    # 整理输出列顺序
    out_cols = [group_col, 'af_events', 'crm_conversions', 'validity_pct',
                'classification', 'factor', 'af_cap', 'est_crm', 'action']
    out_cols = [c for c in out_cols if c in result.columns]
    result_out = result[out_cols].sort_values('af_events', ascending=False)

    print(f'  合并后渠道数：{len(result_out)}')
    print(f'  平均有效性：{result_out["validity_pct"].mean():.2f}%')
    print(f'  高有效性（≥{VALIDITY_HIGH}%）渠道数：{(result_out["classification"] == "高有效性").sum()}')
    print(f'  中有效性（{VALIDITY_MID}-{VALIDITY_HIGH}%）渠道数：{(result_out["classification"] == "中有效性").sum()}')
    print(f'  低有效性（<{VALIDITY_MID}%）渠道数：{(result_out["classification"] == "低有效性").sum()}')

    # ── Step 7：输出 Excel 报告（带颜色标注）────────
    print(f'[Step 7] 输出 Excel 报告：{args.output}')
    wb = Workbook()
    ws = wb.active
    ws.title = 'JXXXX Funnel Analysis'

    # 标题行样式
    header_fill = PatternFill(fill_type='solid', fgColor='1F4E79')  # 深蓝
    header_font = Font(color='FFFFFF', bold=True, size=11)
    high_fill = PatternFill(fill_type='solid', fgColor='C6EFCE')   # 绿
    mid_fill = PatternFill(fill_type='solid', fgColor='FFEB9C')    # 黄
    low_fill = PatternFill(fill_type='solid', fgColor='FFC7CE')    # 红

    # 写入表头
    for col_idx, col_name in enumerate(out_cols, 1):
        cell = ws.cell(row=1, column=col_idx, value=col_name)
        cell.fill = header_fill
        cell.font = header_font
        cell.alignment = Alignment(horizontal='center')

    # 写入数据行
    for row_idx, row in enumerate(result_out.itertuples(index=False), 2):
        for col_idx, col_name in enumerate(out_cols, 1):
            val = getattr(row, col_name)
            cell = ws.cell(row=row_idx, column=col_idx, value=val)
            cell.alignment = Alignment(horizontal='center')

        # 按有效性分类上色
        pct = row.validity_pct
        if pct >= VALIDITY_HIGH:
            fill = high_fill
        elif pct >= VALIDITY_MID:
            fill = mid_fill
        else:
            fill = low_fill
        for col_idx in range(1, len(out_cols) + 1):
            ws.cell(row=row_idx, column=col_idx).fill = fill

    # 自动调整列宽
    for col_idx, col_name in enumerate(out_cols, 1):
        max_len = max(
            len(str(col_name)),
            result_out[col_name].astype(str).map(len).max() if len(result_out) > 0 else 0
        )
        ws.column_dimensions[get_column_letter(col_idx)].width = min(max_len + 2, 30)

    wb.save(args.output)
    print(f'  ✅ Excel 报告已保存：{args.output}')
    print(f'  颜色标注：绿色=高有效性 ≥{VALIDITY_HIGH}%，黄色=中有效性 {VALIDITY_MID}-{VALIDITY_HIGH}%，红色=低有效性 <{VALIDITY_MID}%')

    # ── Step 8：打印汇总 ──────────────────────────────
    print('\n═══ 汇总结果 ═══')
    print(result_out.to_string(index=False))
    print('\n═══ 预算建议（按 AF CAP 排序）═══')
    budget_view = result_out[['af_cap', 'est_crm', 'action']].sort_values('af_cap', ascending=False)
    print(budget_view.to_string(index=False))
    print(f'\n总建议 AF CAP：{result_out["af_cap"].sum():,}')
    print(f'预计总 CRM 产出：{result_out["est_crm"].sum():,}')


if __name__ == '__main__':
    main()
```

---

## 脚本使用方法

### 安装依赖

```bash
pip install pandas openpyxl
```

### 准备输入文件

**文件1：AppsFlyer 事件 CSV**
- 从 AF 后台导出 `in-app-events` CSV
- 包含 `conta_criada_sucesso_view` 事件
- 必要字段：`AppsFlyer ID`（或 `v_appsflyer_id`）、`Event Name`、`Event Time`

**文件2：e-Grana CRM xlsx**
- 财务/结算系统导出的转化数据
- 必要字段：`source_bank`（渠道名）、`user_count`（转化用户数）

### 运行

```bash
python3 jxxxx_funnel.py \
    --af jxxxx_in-app-events_20260501_20260531.csv \
    --crm egrana_crm.xlsx \
    --output jxxxx_funnel_result.xlsx
```

### 输出文件

`jxxxx_funnel_result.xlsx`（带颜色标注）

| Channel | AF Events | CRM Conversions | Validity% | Classification | Factor | AF_CAP | Est.CRM | Action |
|---------|-----------|-----------------|-----------|----------------|--------|--------|---------|--------|
| hertzmobi_mob | 15000 | 5200 | 34.67 | 高有效性 | 1.2 | 18000 | 6238 | 增加投放 |
| flexmedia | 8000 | 2000 | 25.00 | 中有效性 | 1.0 | 8000 | 2000 | 维持不变 |
| abmedia | 5000 | 400 | 8.00 | 低有效性 | 0.5 | 2500 | 200 | 降低CAP |

**颜色标注**：
- 🟢 绿色行：高有效性（≥30%）→ 增加 CAP
- 🟡 黄色行：中有效性（20-30%）→ 维持不变
- 🔴 红色行：低有效性（<20%）→ 降低 CAP（不暂停）

---

## 漏斗可视化

```
总 AF 事件（conta_criada_sucesso_view）
    ↓ 去重（每设备1次）
有效 AF 事件
    ↓ × 有效性%
实际 CRM 转化（e-Grana）
    ↓ × Factor
建议 AF CAP（下月目标）
    ↓ × 有效性%
预计 CRM 产出
```

---

## 业务背景

- JXXXX 是巴西主流小额信贷应用，核心转化为账户创建（`conta_criada_sucesso_view`）
- 约 20-30 个渠道并行投放，有效性差异显著（5%-60%+）
- 低有效性渠道（<20%）通常是流量质量差或存在刷量，但保留观察不立即暂停
- 每月结算前需根据实际转化率调整下月预算分配

---

## 与其他 Skill 的关系

```
AppsFlyer 事件 CSV
    ↓  jxxxx-funnel（本 Skill）
渠道 AF CAP 建议 + 有效性分类
    ↓
├── campaign-budget-analysis（整合多 App 预算分配）
└── pa-export-channel-report-v2（导出 PA 数据时参考 CAP）
```

---

## 触发词

- "JXXXX 预算"、"JXXXX 分析"、"JXXXX 渠道"
- "e-Grana 数据"、"conta_criada_sucesso_view"
- "转化漏斗"、"渠道有效性分析"、"UA 预算分配"
- "Conversion Funnel Intelligence"
- "JXXXX CAP 建议"

---

*版本：v1.1.0 | 更新：2026-05-12 | 新增完整可执行脚本*

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`funnel_intelligence.py`](scripts/funnel_intelligence.py) | Executable script |

