---
name: wish-to-my-table
display_name: "Wish Intelligence Collector | 渠道 Wish 智能采集器"
description: 将渠道 Wish List 数据解析后，写入用户个人的8列表格（Name, Vertical, Link, ID, Ad_type, Channel, Geo, Notes），输出到腾讯文档。适用于汇总追踪各渠道 Wish 数据的场景。
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

# wish-to-my-table

将任意渠道的 Wish List 原始数据，解析为标准8列格式，并同步到腾讯文档在线表格。

## 适用场景

- 收到渠道（Hertzmobi、FlexMedia 等）的 Wish List，需要汇总到个人追踪表格
- 需要生成标准8列 CSV / xlsx 本地存档
- 需要同步到腾讯文档在线表格

## 表格格式（8列）

| 列 | 字段名 | 说明 |
|---|---|---|
| A | Name | 应用名称 |
| B | Vertical | 垂直分类（Shopping/Finance/Casino等） |
| C | Link | App Store / Play Store URL |
| D | ID | Android package 或 iOS id |
| E | Adtype | CPI / CPE / CTV 等 |
| F | Channel | 渠道名称（Hertzmobi / FlexMedia 等） |
| G | Geo | 国家/地区 |
| H | Notes | 备注（tracker 信息等） |

腾讯文档地址：<ADDRESS_REMOVED>DpF（`Wish Information 05.2026 - Hertzmobi`）

## 工作流程

### Step 1：解析原始数据

如果输入是原始文本（非结构化），先解析为结构化数据。

解析规则（以 Hertzmobi 格式为例）：
- 应用名称：行首到第一个空格/冒号
- iOS ID：`id` + 数字
- Android package：`com.` / `org.` 开头的包名
- Geo：大写国家代码（BR, MX, IN 等）
- Tracker：AF / adjust / AppsFlyer / AppMetrica / singular / Branch

### Step 2：补全字段

- `Vertical`：根据应用名称推断（Shopping / Finance / Casino 等），或留空
- `Link`：根据 ID 构造 App Store / Play Store URL，或从数据中获取
- `Ad_type`：默认 CPI，如数据中有 CPE/CTv 则使用
- `Channel`：渠道名称

### Step 3：写入腾讯文档

1. 获取腾讯文档信息：使用 `manage.query_file_info` 或已知 file_id
2. 获取 sheet 信息：使用 `sheet.get_sheet_info`
3. 分批写入数据：使用 `sheet.set_range_value`（每批 ≤20行，避免超负载）
4. 数据格式：每行8列 [Name, Vertical, Link, ID, Ad_type, Channel, Geo, Notes]

### Step 4：保存到本地 xlsx

使用 `openpyxl` 将数据写入本地 xlsx 文件：
`/Users/yanzhao/WorkBuddy/Wish_Information/Wish_Information_05.2026.xlsx`

## 脚本参考

主解析脚本（Hertzmobi 示例）：`/Users/yanzhao/WorkBuddy/20260408165935/parse_hertzmobi.py`

## 注意事项

- 腾讯文档 API 有负载限制，每批不超过20行
- Geo 列如含多个地区，用逗号分隔（如 "BR, MX, AR"）
- Notes 列用于存放 tracker 信息（AF / adjust 等）
- 写入前先检查是否已存在相同 ID，避免重复

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`wish_collector.py`](scripts/wish_collector.py) | Executable script |

