---
name: affiliate-attribution
display_name: "Multi-MMP Attribution Engine | 多平台归因清洗引擎"
description: |
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

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

# affiliate-attribution

Multi-MMP Attribution Engine — 渠道归因去重与清洗工具。

适用于多渠道并行投放的网盟（Affiliate）场景，解决以下核心问题：
- AppsFlyer 原始事件数据中同一设备被多个渠道归因
- 渠道名称含变体后缀（如 `bromo_mob_apr`），需合并为统一渠道名
- 存在无效事件（如电信行业 `af_purchase_esim`）需排除
- Source Bank（财务结算数据）的渠道归属优先级高于 AF 自动归因

---

## 适用场景

- 月度渠道结算前的归因数据清洗
- AppsFlyer 原始事件数据去重与渠道归一化
- 多渠道变体名合并（如 `channel_a_mob_apr` → `channel_a_mob`）
- 为 `nxxx-analysis` / `campaign-budget-analysis` 提供干净归因数据

---

## 核心归因规则（4条）

### 规则1：Source Bank 决定渠道归属（最高优先级）

```
Source Bank 中记录的渠道名 → 最终归因渠道
AppsFlyer Media Source 仅作辅助验证（Source Bank 无记录时使用）
```

**原因**：财务结算以 Source Bank 为准，AF 自动归因可能存在误差。

### 规则2：v_appsflyer_id 去重（每个设备只保留最早事件）

```python
df = (df
    .sort_values('event_time')
    .groupby('v_appsflyer_id')
    .first()
    .reset_index())
```

### 规则3：排除无效事件

```python
EXCLUDED_EVENTS = ['af_purchase_esim']
df = df[~df['event_name'].isin(EXCLUDED_EVENTS)]
```

### 规则4：渠道变体按前缀合并

```python
VARIANT_SUFFIXES = ['_apr', '_ios', '_and', '_v2', '_new', '_old']

def normalize_channel(channel: str) -> str:
    if not isinstance(channel, str):
        return channel
    for suffix in VARIANT_SUFFIXES:
        if channel.endswith(suffix):
            return channel[:-len(suffix)]
    return channel
```

---

## 完整执行脚本

> 保存为 `affiliate_attribution.py`，与 AF CSV 和 Source Bank xlsx 放在同一目录运行。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
affiliate_attribution.py
Multi-MMP Attribution Engine — 完整执行脚本

功能：
1. 加载 AppsFlyer 事件数据（CSV，自动检测编码）
2. 加载 Source Bank（xlsx），以 Source Bank 渠道归属为优先
3. 按 v_appsflyer_id 去重（取最早事件）
4. 排除无效事件（如 af_purchase_esim）
5. 渠道变体按共同前缀合并
6. 输出归因结果 CSV（utf-8-sig 编码，Excel 可直接打开）

用法：
    python3 affiliate_attribution.py \
        --af appsflyer_events.csv \
        --source-bank source_bank.xlsx \
        --output attributed_result.csv
"""

import argparse
import pandas as pd
import sys
import os

# ── 配置区（可通过命令行参数覆盖）─────────────────────
EXCLUDED_EVENTS = ['af_purchase_esim']
VARIANT_SUFFIXES = ['_apr', '_ios', '_and', '_v2', '_new', '_old', '_backup']


def normalize_channel(channel: str) -> str:
    """将渠道变体名归一化为主渠道名"""
    if not isinstance(channel, str):
        return channel
    for suffix in VARIANT_SUFFIXES:
        if channel.endswith(suffix):
            return channel[:-len(suffix)]
    return channel


def detect_encoding(file_path: str) -> str:
    """自动检测 CSV 文件编码"""
    for enc in ['utf-8-sig', 'utf-8', 'gbk', 'latin-1']:
        try:
            with open(file_path, 'r', encoding=enc) as f:
                f.read(1024)
            return enc
        except Exception:
            continue
    return 'utf-8-sig'  # 默认


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
        description='Multi-MMP Attribution Engine — 渠道归因去重工具'
    )
    parser.add_argument('--af', required=True, help='AppsFlyer 事件 CSV 文件路径')
    parser.add_argument('--source-bank', required=True, help='Source Bank xlsx 文件路径')
    parser.add_argument('--output', default='attributed_result.csv', help='输出 CSV 路径')
    parser.add_argument('--keep-non-primary', action='store_true',
                        help='保留非主归因记录（默认只保留 Is Primary Attribution=True）')
    args = parser.parse_args()

    # ── Step 1：加载 AppsFlyer 数据 ──────────────────────
    print(f'[Step 1] 加载 AppsFlyer 数据：{args.af}')
    encoding = detect_encoding(args.af)
    print(f'  检测到文件编码：{encoding}')
    try:
        af = pd.read_csv(args.af, encoding=encoding, low_memory=False)
    except Exception as e:
        print(f'ERROR: 无法读取 AF CSV 文件：{e}')
        sys.exit(1)

    print(f'  AF 数据行数：{len(af)}')
    print(f'  AF 字段列表（前10个）：{list(af.columns)[:10]}')

    # 字段名兼容（不同 AF 导出版本字段名可能不同）
    id_col = find_column(af, ['v_appsflyer_id', 'AppsFlyer ID'])
    event_col = find_column(af, ['event_name', 'Event Name'])
    time_col = find_column(af, ['event_time', 'Event Time'])
    channel_col = find_column(af, ['channel', 'Channel'])
    media_source_col = find_column(af, ['media_source', 'Media Source'])
    primary_col = find_column(af, ['is_primary_attribution', 'Is Primary Attribution'])

    if not id_col:
        print('ERROR: 找不到 v_appsflyer_id / AppsFlyer ID 字段')
        sys.exit(1)

    print(f'  字段映射：')
    print(f'    ID = {id_col}')
    print(f'    Event = {event_col}')
    print(f'    Time = {time_col}')
    print(f'    Channel = {channel_col}')
    print(f'    Media Source = {media_source_col}')
    print(f'    Primary Attribution = {primary_col}')

    # ── Step 2：排除无效事件 ────────────────────────────
    if event_col:
        before = len(af)
        af = af[~af[event_col].isin(EXCLUDED_EVENTS)]
        after = len(af)
        print(f'[Step 2] 排除无效事件 {EXCLUDED_EVENTS}：{before} → {after} 行（移除 {before - after} 行）')
    else:
        print('[Step 2] ⚠ 未找到 event_name 字段，跳过无效事件排除')

    # ── Step 3：过滤非主归因（可选）────────────────────
    if primary_col and not args.keep_non_primary:
        before = len(af)
        # 兼容多种写法：True/False、'true'/'false'、1/0
        af[primary_col] = af[primary_col].astype(str).str.lower().isin(['true', '1', 'yes'])
        af = af[af[primary_col] == True]
        after = len(af)
        print(f'[Step 3] 保留主归因（{primary_col}=True）：{before} → {after} 行')
    elif args.keep_non_primary:
        print('[Step 3] 保留所有归因记录（--keep-non-primary）')

    # ── Step 4：按 v_appsflyer_id 去重（取最早事件）───
    print(f'[Step 4] 按 {id_col} 去重（保留最早事件）...')
    af[time_col] = pd.to_datetime(af[time_col], errors='coerce')
    af_dedup = (af
        .sort_values(time_col)
        .groupby(id_col)
        .first()
        .reset_index())
    print(f'  去重后行数：{len(af_dedup)}（移除 {len(af) - len(af_dedup)} 条重复）')

    # ── Step 5：加载 Source Bank ────────────────────────
    print(f'[Step 5] 加载 Source Bank：{args.source_bank}')
    try:
        sb = pd.read_excel(args.source_bank)
    except Exception as e:
        print(f'ERROR: 无法读取 Source Bank xlsx 文件：{e}')
        sys.exit(1)

    sb_id_col = find_column(sb, ['v_appsflyer_id', 'AppsFlyer ID'])
    sb_source_col = find_column(sb, ['source', 'Source', 'channel', 'Channel'])

    if not sb_id_col or not sb_source_col:
        print(f'ERROR: Source Bank 缺少必要字段（需要 v_appsflyer_id + source）')
        print(f'  可用字段：{list(sb.columns)}')
        sys.exit(1)

    print(f'  Source Bank 行数：{len(sb)}')
    print(f'  SB 字段映射：ID={sb_id_col}, Source={sb_source_col}')

    # ── Step 6：合并归因 ───────────────────────────────
    print('[Step 6] 合并 Source Bank 归因（Source Bank 优先级最高）...')
    sb_merge = sb[[sb_id_col, sb_source_col]].copy()
    sb_merge.columns = ['merge_id', 'source_bank_channel']

    result = af_dedup.copy()
    result = result.rename(columns={id_col: 'merge_id'})
    result = result.merge(sb_merge, on='merge_id', how='left')
    result = result.rename(columns={'merge_id': id_col})

    # 最终渠道：Source Bank 优先，否则用 AF Media Source，再否则用 AF Channel
    if media_source_col:
        result['final_channel'] = result['source_bank_channel'].fillna(result[media_source_col])
    elif channel_col:
        result['final_channel'] = result['source_bank_channel'].fillna(result[channel_col])
    else:
        result['final_channel'] = result['source_bank_channel']
        result['final_channel'] = result['final_channel'].fillna('unknown')

    # ── Step 7：渠道变体归一化 ─────────────────────────
    print('[Step 7] 渠道变体归一化...')
    result['channel_normalized'] = result['final_channel'].apply(normalize_channel)

    # ── Step 8：输出结果 ────────────────────────────────
    print(f'[Step 8] 输出结果：{args.output}')
    output_cols = [id_col]
    for c in [event_col, time_col, 'final_channel', 'channel_normalized', 'source_bank_channel']:
        if c and c in result.columns and c not in output_cols:
            output_cols.append(c)

    out = result[output_cols].copy()
    out.to_csv(args.output, index=False, encoding='utf-8-sig')
    print(f'  输出行数：{len(out)}')
    print(f'  归一化后渠道数：{out["channel_normalized"].nunique()}')
    print(f'  各渠道行数：')
    for ch, cnt in out['channel_normalized'].value_counts().head(15).items():
        print(f'    {ch}: {cnt}')

    print('\n✅ 归因去重完成！')
    print(f'   Source Bank 覆盖行数：{(result["source_bank_channel"].notna()).sum()}/{len(result)}')
    print(f'   输出文件：{args.output}')
    print(f'   提示：文件已用 utf-8-sig 编码，可直接用 Excel 打开（中文无乱码）')


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
- 从 AppsFlyer 后台导出 `in-app-events` CSV
- 必要字段：`v_appsflyer_id`（或 `AppsFlyer ID`）、`event_name`、`event_time`
- 可选字段：`channel`、`media_source`、`is_primary_attribution`

**文件2：Source Bank xlsx**
- 财务/结算系统导出的渠道归属表
- 必要字段：`v_appsflyer_id`（或 `AppsFlyer ID`）、`source`（最终归因渠道名）

### 运行

```bash
python3 affiliate_attribution.py \
    --af appsflyer_events.csv \
    --source-bank source_bank.xlsx \
    --output attributed_result.csv
```

### 输出文件

`attributed_result.csv`（utf-8-sig 编码，Excel 直接打开无乱码）

| 字段 | 说明 |
|------|------|
| v_appsflyer_id | 设备ID（去重后，每设备1行） |
| event_name | 该设备的首个归因事件名 |
| event_time | 该事件的事件时间 |
| final_channel | 最终归因渠道（Source Bank 优先） |
| channel_normalized | 归一化渠道名（变体已合并） |
| source_bank_channel | Source Bank 中的渠道名（如未匹配则为空） |

---

## 数据格式详细说明

### AppsFlyer CSV 标准字段

| 字段名（常见变体） | 类型 | 说明 |
|-------------------|------|------|
| v_appsflyer_id / AppsFlyer ID | string | 去重键，每个设备唯一 |
| event_name / Event Name | string | 事件名称 |
| event_time / Event Time | datetime | 事件时间（UTC） |
| media_source / Media Source | string | AF 归因媒体来源 |
| channel / Channel | string | AF 归因渠道（可能含变体后缀） |
| is_primary_attribution / Is Primary Attribution | bool/string | 是否主归因 |
| event_value / Event Value | string | JSON 字符串，含 transaction_id 等 |

### Source Bank xlsx 标准字段

| 字段名（常见变体） | 类型 | 说明 |
|-------------------|------|------|
| v_appsflyer_id / AppsFlyer ID | string | 与 AF 数据对应 |
| source / Source / channel | string | Source Bank 确定的最终渠道名 |

---

## 业务背景

此归因规则来自 Claro Flex（巴西电信运营商）eSIM 推广的真实运营经验：

- Claro Flex 在 LATAM 多国投放，渠道包括：ABAMedia、Fumobi、FlexMedia、SparkAds、HKVivid、Influx、MobiReach 等
- AppsFlyer 自动归因存在误差，财务结算以 Source Bank（结算系统）为准
- AF 事件中含无效事件 `af_purchase_esim`（eSIM 安装事件，不计入业务转化）
- 渠道变体命名不规范（如 `bromo_mob_apr`、`channel_a_mob_ios`），需归一化后结算

---

## 与其他 Skill 的关系

```
AppsFlyer 原始 CSV
    ↓  affiliate-attribution（本 Skill）
归属因去重 + 变体合并后的 CSV
    ↓
├── nxxx-analysis（NXXX 盈亏核算）
├── campaign-budget-analysis（预算分配）
└── pa-export-channel-report-v2（PA 数据导出）
```

**建议**：每次结算前先运行本 Skill，再将干净数据交给下游分析 Skill。

---

## 触发词

- "渠道归因"、"attribution"、"去重"、"Source Bank"
- "Claro Flex 归因"、"渠道变体合并"
- "v_appsflyer_id 去重"、"af_purchase_esim 排除"
- "Multi-MMP Attribution Engine"
- "归因清洗"、"渠道归一化"

---

*版本：v1.1.0 | 更新：2026-05-12 | 新增完整可执行脚本*

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`multi_mmp_attribution.py`](scripts/multi_mmp_attribution.py) | Executable script |

