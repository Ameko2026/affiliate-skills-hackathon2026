# 路演 PPT — 跨文化网盟管理 Skill 集合
# 腾讯云 2026 黑客松参赛作品
# 格式：Marp Markdown（可转为 PDF/PPTX）
# 作者：M COMPANY
# 总页数：16 页

---

<!-- Slide 1: 封面 -->
<div align="center">

# 🌍 跨文化网盟管理 Skill 集合

## 基于 AI Agent 的多区域 Affiliate 自动化运营系统

**腾讯云 2026 黑客松参赛作品**

**M COMPANY**

<br>

*连接全球广告主与多元流量源*

🇧🇷 🇨🇳 🇪🇺 🌏

</div>

---

<!-- Slide 2: 痛点 — 我们每天在做什么？ -->
# 每天的工作日常（Before）

| 时间 | 任务 | 工具 | 耗时 |
|------|------|------|------|
| 09:00-10:30 | 从 MMP 平台导出 5+ 份 PA/Install CSV，手动清洗去重 | Excel + 手工 | **1.5h** |
| 10:30-11:30 | 与巴西本地渠道 WhatsApp 来回确认 Offer/CAP 细节 | WhatsApp + 翻译 | **1h** |
| 13:00-14:30 | 手动对账 Settlement 单，标记差异 ≥5% 的异常项 | Excel + 计算器 | **1.5h** |
| 15:00-16:00 | 处理渠道 Wish List → 按广告主/地区拆分填表 | 手工复制粘贴 | **1h** |
| 16:00-17:00 | 整理 PA 反作弊报告 + 盈亏数据给广告主 | Excel + PPT | **1h** |

### 🔴 每天 6 小时花在重复劳动上
### 🔴 巴西渠道说 "Já vou"（马上）可能意味着三小时后 😅
### 🔴 CAP 分配靠"感觉"，20-30% 浪费在低质流量
### 🔴 同时服务巴西/欧洲/中国三类广告主，时区+语言+期望值完全不同

---

<!-- Slide 3: 我们的业务场景 — 真实的跨境网盟世界 -->
# 我们的战场：全球 Affiliate 网络

## 🌐 网盟生态 — 我们在中间连接两端

```
  ┌─────────────────────────────────────────────────────┐
  │                  广告主 (Advertisers)                 │
  │                                                     │
  │  🇧🇷 巴西本土出海公司   🇪🇺 欧洲出海互联网公司        │
  │  (金融/电商/工具)      (Fintech/SaaS/Mobile)         │
  │                                                     │
  │  🇨🇳 中国出海广告主                                   │
  │  (电商/游戏/工具/金融)                                │
  └────────────────────┬────────────────────────────────┘
                         │ CPA / CPI / CPS / SDK
              ┌──────────▼──────────┐
              │    网 盟 平 台       │  ← M COMPANY 所在位置
              │ (Affiliate Network)  │     匹配广告主 × 流量源
              └──────────┬──────────┘
                         │ Revenue Share / CAP
     ┌───────────────────┼───────────────────┬────────────┐
     ▼                   ▼                   ▼            ▼
 ┌────────┐       ┌──────────┐      ┌──────────┐   ┌─────────┐
 │🇧🇷 巴西  │       │🇨🇳 中国   │      │🌏 东南亚  │   │ 其他流量  │
 │本地渠道  │       │流量源    │      │互联网公司 │   │  合作方  │
 │KOL/Media│       │出海DSP   │      │Media Buy │   │         │
 │Buyer    │       │/ADX/SSP  │      │/Agency   │   │         │
 └────────┘       └──────────┘      └──────────┘   └─────────┘
```

### 三类广告主 × 三类流量源 = 复杂度 9 倍放大
> 每个广告主的 PA 规则不同、结算周期不同、对数据的要求格式不同
> 每个流量源的 Postback 方式不同、质量标准不同、沟通风格不同

---

<!-- Slide 4: 解决方案总览 — 13 个 Skill × 5 层架构 -->
# 解决方案：13 个 Skill × 5 层架构

```
┌─────────────────────────────────────────────────┐
│  Layer 5  跨文化协作层  (Cross-Cultural)          │  ← 核心差异化
│  └─ cross-cultural-negotiation-copilot           │
├─────────────────────────────────────────────────┤
│  Layer 4  智能决策层  (AI Decision & Risk)        │
│  ├─ conversion-funnel-intelligence (转化漏斗 + CAP 建议)            │
│  ├─ cross-regional-revenue-audit (Campaign 盈亏核算)             │
│  └─ macro-monitoring-agent (定时监控 + 异常预警)            │
├─────────────────────────────────────────────────┤
│  Layer 3  反作弊与归因层  (Fraud & Attribution)    │
│  ├─ multi-mmp-attribution-engine (多 MMP 归因引擎)        │
│  ├─ pa-channel-export (PA 渠道数据导出)      │
│  ├─ pa-channel-export (专项 PA 分析)      │
│  └─ pa-report-workflow (PA 报告自动化工作流)        │
├─────────────────────────────────────────────────┤
│  Layer 2  数据分析层  (Data Analytics)             │
│  ├─ ai-budget-optimizer (预算汇总优化)         │
│  ├─ geo-market-intel-engine (区域市场情报)                │
│  ├─ wish-intelligence-collector (Wish List → 个人追踪表)       │
│  └─ regional-wish-classifier (Wish List → 公司标准表)  │
├─────────────────────────────────────────────────┤
│  Layer 1  数据接入层  (Data Connectors)            │
│  ├─ crm-channel-extraction (OCR 结算单提取)        │
│  └─ crm-settlement-verification (自动对账)          │
└─────────────────────────────────────────────────┘
```

**每个 Skill = 一段真实业务 Know-how + 一个可执行 Python 脚本**

---

<!-- Slide 5: Layer 1 — 数据接入层 -->
# Layer 1：数据接入层 — 告别手工录入

## 两大能力

### 📄 crm-channel-extraction
从 OCR 识别的结算单 PDF/图片中自动提取渠道名和金额
> "拍照 → 提取 → 入库"，不再手动敲键盘
> 💡 巴西本地渠道发来的结算单经常是手写扫描件 + 葡萄牙语备注

### ✅ crm-settlement-verification
自动对账：渠道报数 vs AppsFlyer 数据，标记差异 ≥5% 的异常项
> 人工对账 2 小时 → 自动化 3 分钟
> 💡 Deduplication 规则不一致、Postback S2S 延迟是常见争议来源
> 💡 transaction_id 正则匹配 + 推广窗口验证双重校验

---

<!-- Slide 6: Layer 2 — 数据分析层 -->
# Layer 2：数据分析 + 渠道管理

### 📋 wish-intelligence-collector / regional-wish-classifier
渠道 Wish List 智能解析双模式：
- **个人模式**：8 列标准格式（Name / Vertical / Link / ID / Ad_type / Channel / Geo / Notes）
- **公司模式**：按地区自动分类（MENA / US / Betting / LATAM / APAC / ForexCrypto）
> 💡 收到 Hertzmobi、FlexMedia 等巴西/东南亚渠道的 Wish List → 一键拆分填表
> 💡 同时输出本地 xlsx + 腾讯文档在线表格

### 📈 ai-budget-optimizer（预算汇总优化）
- 多 APP × 多 GEO × 多 Offer 的预算交叉矩阵
- 服务三类广告主（巴西/欧洲/中国），每种有不同的预算审批流程
> 💡 一个中国广告主同时跑 5 个 GEO × 3 个 Offer → 预算复杂度爆炸

### 🌍 geo-market-intel-engine（区域市场情报）
- 竞品 App 下载量、排名、评分追踪
- 覆盖 LATAM / APAC / Europe 主要市场
> 💡 帮助欧洲广告主了解拉美市场、帮助中国广告主理解巴西竞争格局

---

<!-- Slide 7: Layer 3 — 反作弊与归因层 ⭐ -->
# Layer 3：反作弊与归因 — 网盟的核心生命力

### 🔗 multi-mmp-attribution-engine（多 MMP 归因引擎）
- Source Bank 优先级归因逻辑（Organic > Non-organic > Uninstall）
- `v_appsflyer_id` 去重 + 渠道变体前缀合并（如 `xxx_int` + `xxx_mobile`）
- 输出 utf-8-sig 编码 CSV → Excel 直接打开无乱码
> 💡 同一个 Install 可能被 AppsFlyer + Adjust 同时归因 → 必须跨 MMP 去重

### 🛡️ pa-channel-export（PA 渠道数据导出）
从 AppsFlyer PA CSV 中筛选指定渠道，生成带样式的 Excel：
- 4 种 PA 类型全覆盖：blocked-installs / detection / blocked-in-app-events / fraud-post-inapps
- 作弊原因字段橙色高亮（Blocked Reason / Rejected Reason 等）
- 保留 60+ 列原始字段
> 💡 发给巴西本地渠道的 PA Report 必须有理有据，否则引发 Dispute

### 🎯 pa-channel-export（专项渠道 PA 分析）
针对单一渠道的深度 PA 分析（iOS + Android 双端）
- Install PA + Event PA 双维度统计
- 按 PID 粒度下钻到子渠道
> 💡 大型巴西 Media Buy 渠道需要单独出专项报告，证明流量质量

### 📊 pa-report-workflow（PA 报告自动化工作流）
每周自动更新 PA Dashboard：
- CSV → JS 数组 → 注入 HTML 页面
- 跨周期自动拆分（Week 2 / Week 3 by date cutoff）
> 💡 每周给广告主提交 PA 报告的重复劳动 → 一键全自动更新

---

<!-- Slide 8: Layer 4 — 智能决策层 -->
# Layer 4：智能决策层 — 不再靠"感觉"做决策

### 🎯 conversion-funnel-intelligence（JXXXX Campaign 转化漏斗分析）
- JXXXX Campaign 漏斗 5 阶段：**Install → Register → KYC → Loan Draw → Repayment**
- 按有效性分类：高(≥30%) / 中(20-30%) / 低(<20%)
- **输出带颜色标注的 Excel 报告**：
  - 🟢 绿色 = 高有效性 → **增加 CAP**
  - 🟡 黄色 = 中有效性 → 维持不变
  - 🔴 红色 = 低有效性 → **降低 CAP 或暂停**
> 💡 金融类 Offer 的漏斗转化率直接决定盈亏生死线

### 💰 cross-regional-revenue-audit（NXXX Campaign 盈亏核算）
- 自动标记负 ROI 渠道（红黑榜）
- Payout > Revenue = 在亏钱 → 必须立刻行动
- 多维度拆解：按渠道 / 按 APP / 按日期
> 💡 表面高安装量的巴西本地渠道，实际可能在亏钱

### ⏰ macro-monitoring-agent（定时监控）
- 定时拉取 AppsFlyer / Adjust 数据
- 异常自动预警：安装量骤降、ROI 异常、Postback 掉线、PA 飙升
> 💡 凌晨 3 点巴西渠道停量了你还在睡觉？Agent 替你盯着 👁️

---

<!-- Slide 9: Layer 5 — 核心差异化 -->
# Layer 5：跨文化沟通 Skill — **独家创新**

## 问题：通用 AI 太"直白"，三方关系随时崩

我们的沟通复杂度是 **3×3 矩阵**：

| 广告主来源 | 流量源 | 典型冲突 |
|-----------|--------|---------|
| 🇧🇷 巴西广告主（直接/急躁） | 🇧🇷 巴西渠道（随意/关系导向） | 期望错位 |
| 🇪🇺 欧洲广告主（严谨/流程化） | 🇧🇷 巴西渠道（灵活/非正式） | 格式冲突 |
| 🇨🇳 中国广告主（高效/结果导向） | 🇧🇷 巴西渠道（慢热/关系优先） | 节奏冲突 |

## 方案：内置跨文化沟通策略引擎

| 策略 | 英文示例 | 适用场景 |
|------|---------|---------|
| **Soft Wording** | "Would you mind sharing..." | 对巴西渠道 — 直说=没礼貌 |
| **Validation Framing** | "Just to confirm we're aligned on..." | 对欧洲广告主 — 先确认再推进 |
| **Internal Coordination** | "Our finance team is asking for..." | 对所有方 — 保全面子 |

### 🇧🇷 巴西特色：自动识别 "Abraço!" / "Tudo bem?" / "Oi tudo bem?" 并适配回复语气
### 🇪🇺 欧洲广告主适配：正式邮件格式、详细数据附件、UTC 时间标注
### 🇨🇳 中国广告主适配：简洁高效汇报、关键指标突出、微信/飞书同步
### ✅ 沟通往返次数减少 80%，三方满意度显著提升

---

<!-- Slide 10: 技术创新点 -->
# 技术创新

### 1️⃣ Skill 即代码（Skill as Code）
每个 Skill 包含完整可执行 Python 脚本，AI Agent 可零干预自动调用
> 不是 Prompt 模板，是真·可运行代码（pandas + openpyxl + re）

### 2️⃣ 跨平台编码适配
所有输出文件自动处理编码：
- CSV → utf-8-sig（Excel 无乱码）
- 换行符 CRLF/LF 自适应
- 支持 Windows/Mac/Linux 跨平台
> 💡 巴西渠道用 Excel 打开中文 CSV → 乱码 = 数据作废。彻底解决。

### 3️⃣ 业务规则内置
归因逻辑、PA 分类规则、有效性阈值、沟通话术均来自 **真实业务踩坑经验**
> 不是 ChatGPT 生成的"正确废话"，是在真金白银的网盟业务中验证过的规则

### 4️⃣ 腾讯文档集成
Wish List 解析结果自动同步到腾讯文档在线表格
> 团队协作无缝衔接，不用再发文件来回传

### 5️⃣ 模块化可扩展
5 层架构清晰，新增广告主类型或流量源只需添加对应 Skill
> 今天服务巴西/欧洲/中国广告主，明天可以接入中东/北美

---

<!-- Slide 11: 应用效果对比 -->
# Before vs After

| 指标 | Before（传统方式） | After（Skill 集合） | 提升 |
|------|-------------------|---------------------|------|
| 月度 Settle 对账耗时 | **1 天** | **30 分钟** | **96% ↓** |
| PA 报表制作（4类×多App） | **4-6 小时/周** | **自动完成** | **100% ↓** |
| Wish List 拆分填表 | **1-2 小时/次** | **一键完成** | **95% ↓** |
| 跨文化沟通往返 | **5-8 次/次** | **1-2 次/次** | **75% ↓** |
| CAP / 预算分配依据 | 经验驱动（拍脑袋） | 数据驱动（有理有据） | **质变** |
| 新人上手时间 | **2 周** | **2 天** | **86% ↓** |
| 凌晨紧急响应 | **人工盯守 😵‍💫** | **Agent 自动预警 🤖** | **解放睡眠** |

---

<!-- Slide 12: Demo 演示路线图 -->
# Demo 演示（4 个场景）

### 场景 1：数据处理自动化（30 秒）
> 用户："帮我跑一下上周的归因数据"
> AI：调用 `multi-mmp-attribution-engine` → 输出去重后的干净 CSV
> 🎬 展示：原始脏数据 → 一键清洗 → 干净报表

### 场景 2：反作弊 PA 报告（45 秒）
> 用户："生成本地渠道本周的 PA Report"
> AI：调用 `pa-channel-export` → 输出带橙色高亮的 Excel
> 🎬 展示：4 类 PA 数据 → 作弊原因一目了然

### 场景 3：智能决策建议（45 秒）
> 用户："本月 JXXXX Campaign 哪些渠道要调 CAP？"
> AI：调用 `conversion-funnel-intelligence` → 输出绿黄红三色 Excel + CAP 建议
> 🎬 展示：红黑榜自动生成 → 绿增黄稳红降

### 场景 4：跨文化沟通（30 秒）
> 用户："帮我写一封催巴西渠道要 Settlement 的邮件，同时抄送欧洲广告主"
> AI：调用 `cross-cultural-negotiation-copilot` → 输出双版本邮件
> 🎬 展示：对巴西渠道 Soft Wording 版 vs 对欧洲广告主正式版

**总计 Demo 时长：约 150 秒（< 3 分钟）**

---

<!-- Slide 13: 架构与扩展性 -->
# 架构与未来规划

### 当前状态
- ✅ **13 个完整 Skill**（含 Python 脚本），覆盖网盟运营全流程
- ✅ 服务三类广告主（🇧🇷 巴西本土 / 🇪🇺 欧洲 / 🇨🇳 中国）
- ✅ 对接三类流量源（🇧🇷 巴西本地 / 🇨🇳 中国 / 🌏 东南亚）
- ✅ 已在实际业务中验证核心流程

### 未来规划
- 🔮 接入 AppFollow/AppMagic API 实现实时市场情报
- 🔮 新增 Partner Risk Radar（渠道风险雷达 — 逾期/质量下滑/投诉预警）
- 🔮 接入腾讯云 API（TTS 多语言语音通知 / OCR 结算单识别 / 实时翻译）
- 🔮 发布到 SkillHub 平台供全球网盟公司使用
- 🔮 扩展更多文化场景：🇸🇦 中东商务礼仪 / 🇮🇩 印尼社交型谈判

---

<!-- Slide 14: 为什么是我们？ -->
# 为什么这个方案有竞争力？

### 🎯 精准痛点 — 不做泛泛的"AI 提效"
每一个 Skill 解决的都是网盟从业者**每天头疼的具体问题**
> 归因去重 / 编码乱码 / PA 报告 / Wish List 拆分 / 跨文化催款
> 全部来自真实业务场景，不是假设出来的需求

### 🌍 真实全球化 — 不是 Demo，是日常
同时服务巴西/欧洲/中国三类广告主，对接巴西/中国/东南亚三类流量源
> 这不是 POC 概念验证，这是我们**每天的真实工作**

### 🧠 业务 Know-how 代码化
把资深网盟运营 2-3 年的经验沉淀成可复用的 Skill
> 新人用了 2 天达到老员工的水平 → 降低培训成本 → 快速扩展新区域

### 🤝 开放生态 — 基于 SkillHub
不是闭门造车的内部工具，而是可以发布到 SkillHub 的**行业标准级方案**
> 任何网盟公司都可以使用、扩展、共建

---

<!-- Slide 15: 评委维度自查 -->
# 对照评审标准 — 我们覆盖了什么？

| 评审维度 | 权重 | 我们的覆盖 | 状态 |
|---------|------|-----------|------|
| **场景价值** | 30% | 跨国网盟管理真实痛点（3 类广告主 × 3 类流量源 / 50+ 渠道 / 4 大区域） | ✅ 强 |
| **功能完整性** | 25% | 13 个 Skill + Demo + 完整文档 + 可执行脚本 | ✅ 覆盖 |
| **创新与深度** | 25% | 五层架构 + 跨文化谈判 Copilot（核心差异化） | ✅ 强 |
| **效能提升** | 20% | 对比数据：96% / 100% / 95% / 75% / 86%（有真实业务数据支撑） | ✅ 有数据 |

---

<!-- Slide 16: 结尾 -->
<div align="center">

# 🙏 Obrigado! Thank You! 谢谢!

## 跨文化网盟管理 Skill 集合

**让 AI Agent 真正懂跨境网盟业务**

<br>

### M COMPANY
### 腾讯云 2026 黑客松

<br>

🇧🇷 🇨🇳 🇪🇺 **De China para o mundo — 从中国，向世界**

<br>

*Q&A*

</div>
