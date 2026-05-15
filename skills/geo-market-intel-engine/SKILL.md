---
name: geo-market-intel
display_name: "Geo Market Intelligence Engine | 区域市场情报引擎"
description: |
  This skill should be used when the user needs market intelligence for specific geographic regions and verticals in affiliate marketing operations.
  
  It aggregates competitive offer dynamics, regulatory changes, market trends, and BD opportunities across multiple regions (MENA, LATAM, APAC, Europe, US). Can generate structured market intelligence reports by region + vertical combination.
  
  The skill uses web search and API integrations to gather real-time market data, supporting new market expansion research and competitor monitoring.
  
  Applicable for affiliate BD teams planning regional expansion or evaluating new offer opportunities.
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

category: business-intelligence
tags: [market-intelligence, competitive-analysis, bd-support, geo-expansion]
layer: 2
trigger_keywords:
  - "市场情报"
  - "竞品动态"
  - "geo intel"
  - "BD 支持"

---

# geo-market-intel

Geo Market Intelligence Engine — 多区域市场情报聚合工具。

为 Affiliate 网盟业务的 BD 拓展提供实时市场洞察，支持：
- 新区域开拓前的市场调研
- 特定 Vertical 的 Top Offer 识别
- 竞争对手动态监控
- 监管风险预警

---

## 覆盖区域

| 区域 | 核心国家 | 重点 Vertical |
|------|---------|--------------|
| MENA | SA, AE, KW, OM, QA, EG | Fintech, Shopping, Betting |
| LATAM | BR, MX, AR, CO, CL, PE | Fintech, Gaming, E-commerce |
| APAC | IN, ID, TH, VN, PH, MY | Gaming, Shopping, Finance |
| Europe & US | US, GB, DE, FR, IT, ES | All verticals |

---

## 完整执行脚本

> 保存为 `geo_market_intel.py`。
> **注意**：脚本包含完整框架，真实排行数据需配置 API key。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
geo_market_intel.py
Geo Market Intelligence Engine — 完整执行脚本（框架版）

功能：
1. 接收用户指定的区域 + Vertical + 时间窗口
2. 构建搜索查询（通过 AI Agent 调用 web_search 执行）
3. 聚合竞品 Offer 动态、监管变化
4. 生成结构化市场情报 JSON + Markdown 简报

真实数据依赖（需配置）：
  - AppFollow API 或 AppMagic API（Top App 排行）
  - Adjust / AppsFlyer 行业报告（趋势）
  - web_search 工具（监管动态、实时新闻）

用法：
    python3 geo_market_intel.py \
        --region LATAM \
        --vertical Finance \
        --output latam_finance_intel.md
"""

import argparse
import json
import sys
import time
from datetime import datetime, timezone, timedelta

# ── 区域 & 国家配置 ──────────────────────────────────
GEO_MAPPING = {
    "MENA":        ["SA", "AE", "KW", "OM", "QA", "BH", "EG", "JO", "LB", "IQ"],
    "LATAM":       ["BR", "MX", "AR", "CO", "CL", "PE", "UY", "PY", "BO", "EC", "VE"],
    "APAC":        ["IN", "ID", "TH", "VN", "PH", "MY", "SG", "JP", "KR", "TW", "HK"],
    "Europe_US":   ["US", "GB", "DE", "FR", "IT", "ES", "CA", "AU", "NZ", "IE"],
}

VERTICAL_KEYWORDS = {
    "Finance":      ["bank", "loan", "credit", "fintech", "payment", "wallet"],
    "Shopping":     ["shop", "store", "mall", "market", "ecommerce"],
    "Betting":      ["bet", "casino", "sport", "gambling", "poker"],
    "Gaming":       ["game", "play", "puzzle", "rpg", "casual", "royale"],
    "Forex_Crypto": ["forex", "crypto", "trading", "bitcoin"],
}

# iOS App Store 国家代码映射
IOS_CC_MAP = {
    "BR": "br", "MX": "mx", "AR": "ar", "CO": "co", "CL": "cl", "PE": "pe",
    "IN": "in", "ID": "id", "TH": "th", "VN": "vn", "PH": "ph", "MY": "my",
    "US": "us", "GB": "gb", "DE": "de", "FR": "fr", "IT": "it", "ES": "es",
    "SA": "sa", "AE": "ae", "KR": "kr", "JP": "jp", "SG": "sg", "AU": "au",
}


def build_search_queries(region: str, vertical: str, countries: list) -> list:
    """构建搜索查询列表（由 AI Agent 调用 web_search 执行）"""
    queries = []
    vert_lower = vertical.lower()

    # Top App 搜索（每个区域取前3个国家）
    for country in countries[:3]:
        queries.append(f"top {vert_lower} apps google play {country} 2026")
        queries.append(f"best {vert_lower} apps {country} 2026")

    # 趋势搜索
    queries.append(f"{region} {vert_lower} market size 2026")
    queries.append(f"{region} affiliate marketing {vert_lower} opportunities 2026")

    # 监管动态
    if vertical.lower() in ["finance", "fintech"]:
        for country in countries[:2]:
            queries.append(f"{country} central bank digital banking regulation 2026")
    if vertical.lower() in ["betting", "gaming"]:
        for country in countries[:2]:
            queries.append(f"{country} online betting regulation 2026")

    return queries


def generate_intel_schema(region: str, vertical: str, countries: list) -> dict:
    """生成市场情报数据结构"""
    now = datetime.now(timezone.utc).strftime('%Y-%m-%d')
    return {
        "report_meta": {
            "region": region,
            "countries": countries,
            "vertical": vertical,
            "generated_at": now,
            "data_sources": [
                "Adjust Mobile App Trends Report",
                "AppsFlyer Performance Index",
                "AppFollow Top Charts API (需要key)",
                "Trading Economics (macro)",
                "AI web_search (实时新闻/监管)"
            ]
        },
        "top_apps": [],        # 由 API 或 AI 搜索填充
        "trends": [],          # 由搜索/报告填充
        "regulatory_notes": [], # 由搜索填充
        "bd_opportunities": [], # AI 推荐的行动建议
        "risk_flags": [],      # 高风险信号
    }


def generate_markdown_brief(intel: dict) -> str:
    """将情报数据渲染为 Markdown 简报"""
    meta = intel["report_meta"]
    lines = []
    lines.append(f"# {meta['region']} 市场情报简报 — {meta['vertical']}")
    lines.append(f"**生成时间**：{meta['generated_at']}  ")
    lines.append(f"**覆盖国家**：{', '.join(meta['countries'])}  ")
    lines.append(f"**数据来源**：{', '.join(meta['data_sources'])}")
    lines.append("")

    # Top Apps
    lines.append("## 📱 Top Offer 机会")
    if intel["top_apps"]:
        lines.append("| App | 平台 | 预估月安装 | 推荐 Vertical | 备注 |")
        lines.append("|-----|------|---------|--------------|------|")
        for app in intel["top_apps"][:10]:
            name = app.get("name", "未知")
            platform = app.get("platform", "-")
            installs = app.get("estimated_installs_monthly", "-")
            vert = app.get("recommended_vertical", meta["vertical"])
            notes = app.get("notes", "")
            lines.append(f"| {name} | {platform} | {installs} | {vert} | {notes} |")
    else:
        lines.append("*（需要配置 AppFollow / AppMagic API 以获取真实排行数据）*")
    lines.append("")

    # Trends
    lines.append("## 📈 趋势信号")
    if intel["trends"]:
        for t in intel["trends"]:
            lines.append(f"- {t}")
    else:
        lines.append("*（建议由 AI Agent 调用 web_search 获取最新趋势）*")
    lines.append("")

    # Regulatory
    lines.append("## 🏛️ 监管动态")
    if intel["regulatory_notes"]:
        for r in intel["regulatory_notes"]:
            lines.append(f"- {r}")
    else:
        lines.append("*（建议搜索目标市场监管动态）*")
    lines.append("")

    # BD Opportunities
    lines.append("## 🎯 BD 行动建议")
    if intel["bd_opportunities"]:
        for i, opp in enumerate(intel["bd_opportunities"], 1):
            lines.append(f"{i}. {opp}")
    else:
        lines.append("1. 确认目标区域 Top App 排行，识别高潜力 Offer")
        lines.append("2. 搜索监管机构最新政策，评估合规风险")
        lines.append("3. 联系已有渠道，询问目标 App 的流量成本和 CAP")
    lines.append("")

    # Risk Flags
    if intel["risk_flags"]:
        lines.append("## ⚠️ 风险信号")
        for rf in intel["risk_flags"]:
            lines.append(f"- ⚠️ {rf}")
        lines.append("")

    lines.append("---")
    lines.append(f"*由 Geo Market Intelligence Engine 自动生成 | {meta['generated_at']}*")
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description='Geo Market Intelligence Engine — 多区域市场情报聚合工具'
    )
    parser.add_argument('--region', required=True,
                        choices=list(GEO_MAPPING.keys()),
                        help='目标区域')
    parser.add_argument('--vertical', required=True,
                        choices=list(VERTICAL_KEYWORDS.keys()),
                        help='目标垂直领域')
    parser.add_argument('--countries', nargs='+', default=None,
                        help='指定国家代码（默认使用该区域全部国家）')
    parser.add_argument('--output', default=None, help='输出文件路径 (.md 或 .json)')
    parser.add_argument('--format', choices=['markdown', 'json', 'both'],
                        default='markdown', help='输出格式')
    args = parser.parse_args()

    region = args.region
    vertical = args.vertical
    countries = args.countries or GEO_MAPPING[region]
    base_name = f"{region.lower()}_{vertical.lower()}_intel"
    output_path = args.output or f"{base_name}.md"

    print(f"═══ Geo Market Intelligence Engine ═══")
    print(f"  区域：{region}")
    print(f"  国家：{', '.join(countries)}")
    print(f"  Vertical：{vertical}")
    print()

    # Step 1：构建搜索查询
    print("[Step 1] 构建搜索查询...")
    queries = build_search_queries(region, vertical, countries)
    print(f"  生成 {len(queries)} 条搜索查询")
    print("  ⚠️ 以下查询需要由 AI Agent 调用 web_search 工具执行：")
    for q in queries[:5]:
        print(f"     - {q}")

    # Step 2：初始化情报数据结构
    print("[Step 2] 初始化情报数据结构...")
    intel = generate_intel_schema(region, vertical, countries)

    # Step 3：填充示例数据（LATAM/Finance 示例，正式使用请删除）
    if region == "LATAM" and vertical == "Finance":
        print("[Step 3] 加载 LATAM/Finance 示例数据（演示用）...")
        intel["top_apps"] = [
            {"name": "Competitor_A", "package_id": "com.competitor.a", "platform": "Android",
             "estimated_installs_monthly": "8M+", "affiliate_opportunity": True,
             "recommended_vertical": "Finance", "notes": "CPI约$0.8，核心事件活跃"},
            {"name": "Product_A", "package_id": "com.example.product_a", "platform": "Android",
             "estimated_installs_monthly": "2M+", "affiliate_opportunity": True,
             "recommended_vertical": "Finance", "notes": "直客 + 渠道A"},
            {"name": "Product_B", "package_id": "com.example.product_b", "platform": "Android",
             "estimated_installs_monthly": "500K+", "affiliate_opportunity": True,
             "recommended_vertical": "Finance", "notes": "有效性漏斗分析已配置"},
        ]
        intel["trends"] = [
            "某地区 BNPL 渗透率 2026Q1 同比+45%",
            "某地区数字银行用户突破 3000 万",
            "某地区通胀背景下加密货币需求激增",
        ]
        intel["regulatory_notes"] = [
            "某地区央行推进即时支付扩展，要求 Fintech 加强 KYC",
            "某地区加强对数字银行牌照审批",
        ]
        intel["bd_opportunities"] = [
            "联系渠道A / 渠道B，询问 Competitor_A 的独家流量包",
            "评估即时支付相关 Fintech Offer 的佣金结构",
            "关注加密钱包 Offer（通胀背景下的高增长垂类）",
        ]
    else:
        print("[Step 3] ⚠️ 无示例数据，请配置 API 或由 AI 调用 web_search 填充")

    # Step 4：生成输出
    print(f"[Step 4] 生成输出：{output_path}")
    md_content = generate_markdown_brief(intel)

    if args.format in ['markdown', 'both']:
        md_path = output_path if output_path.endswith('.md') else f"{base_name}.md"
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"  ✅ Markdown 简报已保存：{md_path}")

    if args.format in ['json', 'both']:
        json_path = f"{base_name}.json"
        with open(json_path, 'w', encoding='utf-8') as f:
            json.dump(intel, f, ensure_ascii=False, indent=2)
        print(f"  ✅ JSON 数据已保存：{json_path}")

    print("\n═══ 完成 ═══")
    print(f"  情报条目：Top Apps={len(intel['top_apps'])}, Trends={len(intel['trends'])}")
    print(f"  输出文件：{output_path}")
    print()
    print("⚠️  正式使用前请完成以下配置：")
    print("  1. 配置 AppFollow / AppMagic API key（获取真实 Top Apps 排行）")
    print("  2. 由 AI Agent 调用 web_search 工具执行搜索查询（获取趋势/监管）")
    print("  3. 删除示例数据填充代码（LATAM/Finance 分支）")
    print()
    # 打印简报预览
    print("═══ 简报预览 ═══")
    print(md_content[:1000])
    if len(md_content) > 1000:
        print("... (完整内容请查看输出文件)")


if __name__ == '__main__':
    main()
```

---

## 脚本使用方法

### 安装依赖

```bash
pip install requests beautifulsoup4 pandas openpyxl
```

### 运行（框架版，使用示例数据）

```bash
python3 geo_market_intel.py \
    --region LATAM \
    --vertical Finance \
    --output latam_finance_intel.md
```

### 输出文件

**Markdown 简报**（`latam_finance_intel.md`）：

```markdown
# LATAM 市场情报简报 — Finance

**生成时间**：2026-05-13
**覆盖国家**：BR, MX, AR, CO, CL, PE
**数据来源**：Adjust Mobile App Trends Report, AppsFlyer Performance Index, ...

## 📱 Top Offer 机会

| App | 平台 | 预估月安装 | 推荐 Vertical | 备注 |
|-----|------|---------|--------------|------|
| Competitor_A | Android | 8M+ | Finance | CPI约$0.8，核心事件活跃 |
| Product_A | Android | 2M+ | Finance | 直客 + 渠道A |
| Product_B | Android | 500K+ | Finance | 有效性漏斗分析已配置 |

## 📈 趋势信号

- 某地区 BNPL 渗透率 2026Q1 同比+45%
- 某地区数字银行用户突破 3000 万
- 某地区通胀背景下加密货币需求激增

## 🏛️ 监管动态

- 某地区央行推进即时支付扩展，要求 Fintech 加强 KYC
- 某地区加强对数字银行牌照审批

## 🎯 BD 行动建议

1. 联系渠道A / 渠道B，询问 Competitor_A 的独家流量包
2. 评估即时支付相关 Fintech Offer 的佣金结构
3. 关注加密钱包 Offer（通胀背景下的高增长垂类）
```

**JSON 数据**（`latam_finance_intel.json`）：供 AI Agent 进一步处理或存入知识库。

---

## 接入真实数据的两种方式

### 方式A：配置 AppFollow / AppMagic API（推荐）

```python
# 在脚本顶部添加 API 配置
APPFOLLOW_API_KEY = "your_api_key_here"
APPFOLLOW_BASE = "https://api.appfollow.io/v2"

def fetch_top_apps_real(region, vertical, limit=10):
    """通过 AppFollow API 获取真实排行"""
    import requests
    headers = {"X-AppFollow-Key": APPFOLLOW_API_KEY}
    params = {"region": region, "category": vertical, "limit": limit}
    resp = requests.get(f"{APPFOLLOW_BASE}/top_apps", headers=headers, params=params)
    return resp.json().get("apps", [])
```

### 方式B：由 AI Agent 调用 web_search（最灵活）

在 WorkBuddy / OpenClaw 中，AI 自动调用：

```
用户："帮我生成 LATAM Finance 市场情报简报"

AI 自动执行：
1. 调用 geo_market_intel.py --region LATAM --vertical Finance
2. 同时调用 web_search 执行搜索查询（趋势、监管）
3. 将搜索结果填入 intel 字典
4. 输出最终 Markdown 简报
```

---

## 与其他 Skill 的关系

```
geo-market-intel（本 Skill）
    ↓ 输出市场情报简报
├── Wish Intelligence Collector（优先入库高潜力 Offer）
├── Multi-MMP Attribution Engine（为新区域配置归因）
└── AI Budget Allocation Optimizer（根据区域机会调整预算）
```

---

## 触发词

- "市场调研"、"区域情报"、"MENA 市场"、"LATAM 机会"
- "Top App"、"热门 Offer"、"竞品分析"
- "BD 参考"、"新市场开拓"、"渠道拓展"
- "Geo Market Intelligence"、"市场简报"
- "监管动态"、"合规风险"

---

*版本：v1.2.0 | 更新：2026-05-13 | 脱敏优化版本*

### Scripts

The following bundled scripts support this skill:

| Script | Purpose |
|--------|---------|
| [`geo_market_intel.py`](scripts/geo_market_intel.py) | Executable script |

