---
name: wish-to-company-table
display_name: "Regional Wish Classifier | 区域 Wish 智能分类器"
description: |
  This skill should be used when the user needs to parse channel Wish List data and automatically classify offers by geographic region into company-standard Excel templates (e.g., MENA/US, LATAM, APAC, Betting, ForexCrypto).
  
  It reads parsed Wish List CSV data, applies multi-rule geo classification logic, fills in company template Excel files, and syncs results to Tencent Docs.
  
  Applicable for affiliate BD teams managing offers across multiple verticals and regions, requiring standardized regional reporting.
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

# wish-to-company-table

将任意渠道的 Wish List 原始数据，解析后按地区自动分类，输出为公司标准格式的 xlsx 文件，并同步到腾讯文档。

## 适用场景

- 收到了渠道的 Wish List，需要填入公司标准格式表格
- 需要按地区拆分数据到不同文件
- 需要同时生成本地 xlsx 和腾讯文档在线表格

## 工作流程

### Step 1：解析原始数据

如果输入是原始文本（非结构化），先解析为结构化 CSV，字段包括：
`Name, Vertical, Link, ID, Ad_type, Channel, Geo, Notes`

可复用脚本中的解析逻辑，或直接要求用户提供已解析的 CSV。

### Step 2：按地区分类

使用脚本中的 `classify_record()` 函数，按以下规则分类：

| 目标文件 | 匹配规则 |
|---|---|
| Region_A_Europe | Geo 含：US, GB, UK, IE, IT, DE, FR, ES, CA, AU, NZ, SA, AE, KW, OM, QA 等 |
| Region_B_Betting | Vertical 或 Name 含：betting, gambling, casino, sport, bet, wager, poker, slot |
| Region_C_LATAM | Geo 含：MX, BR, AR, CO, CL, PE, LATAM, UY, PY, BO, EC, VE 等 |
| Region_D_APAC | Geo 含：IN, ID, TH, VN, PH, MY, SG, JP, KR, CN, HK, TW 等 |
| Region_E_Forex | Vertical 或 Name 含：crypto, forex, finance, trading, block, coin |

- 一条数据可同时命中多个分类
- 未匹配任何规则的数据，默认归入 Region_A_Europe

### Step 3：写入本地 xlsx

```bash
python3 scripts/regional_classifier.py \
  --input ./data/parsed.csv \
  --output-dir ./output \
  --no-tencent-docs
```

输出文件：
- `[Company]_Region_A_Europe_filled.xlsx`
- `[Company]_Region_B_Betting_filled.xlsx`
- `[Company]_Region_C_LATAM_filled.xlsx`
- `[Company]_Region_D_APAC_filled.xlsx`
- `[Company]_Region_E_Forex_filled.xlsx`

### Step 4：同步到腾讯文档

对每个地区，通过腾讯文档 MCP 工具执行：

1. **创建在线表格**：使用 `manage.create_file` 创建腾讯文档（类型：智能表格/Excel）
2. **写入数据**：使用 `sheet.set_range_value` 从第6行开始写入数据
   - 列A：序号（1, 2, 3...）
   - 列B：Client/Offer Name
   - 列C：App id（URL）
   - 列D：bundle ID
   - 列E：Vertical
   - 列F：GEO
   - 列G：BD Working（留空）

## 脚本路径

| 文件 | 路径 | 说明 |
|---|---|---|
| 主脚本 | `./scripts/regional_classifier.py` | 分类 + 写入 xlsx |
| 模板目录 | `./templates/` | 5个空白模板 |
| 输出目录 | `./output/` | 填充后的 xlsx |

## 注意事项

- 模板文件前5行为格式/说明，数据从第6行开始
- LATAM 模板有2个 sheet，只写入第一个 sheet
- Forex 模板只有6列（无 BD Working 列）
- 分类结果会保存为 `_classification_debug.json` 方便调试

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`regional_classifier.py`](scripts/regional_classifier.py) | Executable script |

