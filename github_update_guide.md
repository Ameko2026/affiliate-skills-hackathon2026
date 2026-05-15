# GitHub 更新指南 - 跨文化网盟管理 Skill 集合

> 生成时间：2026-05-14
> 背景：本地文件已修复（中文乱码已解决），需覆盖 GitHub 上的旧版本

---

## 更新清单

| # | 文件路径 | GitHub 操作 | 说明 |
|---|---------|------------|------|
| 1 | `submission/intro_500words.md` | 覆盖编辑 | 作品简介，约499字 |
| 2 | `submission/ppt_deck.md` | 覆盖编辑 | 16页路演PPT完整内容 |
| 3 | `submission/technical_doc.md` | 覆盖编辑 | 完整技术文档，约3500字 |
| 4 | `submission/video_script.md` | 覆盖编辑 | 4分钟视频脚本，8个场景 |
| 5 | `submission/video_script_jianying.md` | 覆盖编辑 | 剪映图文成片专用脚本 |
| 6 | `skills/cross-cultural-negotiation-copilot/SKILL.md` | 覆盖编辑 | 跨文化沟通引擎完整文档 |
| 7 | `skills/cross-cultural-negotiation-copilot/scripts/negotiation_copilot.py` | 覆盖编辑 | Python脚本（294行） |

---

## 操作步骤

1. 打开 GitHub 仓库页面
2. 进入每个文件 → 点击 ✏️ Edit → 全选删除 → 粘贴下方对应内容 → Commit
3. 建议从文件 1 到 7 按顺序操作

---

---

## 文件 1：submission/intro_500words.md

```markdown
# 作品简介（约500字）- 直接展示

## 作品名称
跨文化网盟管理 Skill 集合 —— 基于 AI Agent 的多区域 Affiliate 自动化运营系统

## 作品简介
[Company] 作为跨境网盟公司，服务全球三类广告主——🇧🇷 巴西/拉丁美洲 出海公司、🇪🇺 欧洲 出海互联网公司、🇨🇳 中国 出海广告主；
流量来自 🇧🇷 巴西本地渠道、🇨🇳 中国出海 DSP/ADX/SSP、🌏 东南亚互联网公司；
日常运营面临三大痛点：
- **数据处理高度重复**（每周5+ 份报表手动清洗对账耗时 3-5 小时）
- **跨文化沟通效率低**（三类广告主 × 三类流量源，沟通风格差异巨大，邮件往返 5-8 次）
- **预算分配依赖经验**（人类判断导致 20-30% 预算浪费在低质量流量上）

本作品将网盟运营知识封装为**13 个可复用 AI Agent Skill**，采用四层架构：
**Layer 1 数据接入层**从 OCR 结算单自动提取渠道数据（crm-channel-extraction）、自动对账标记异常（crm-settlement-verification）
**Layer 2 数据分析层**含 Wish List 智能分析（wish-intelligence-collector / regional-wish-classifier）；多 MMP 归因去重基于 Source Bank 优先级（multi-mmp-attribution-engine）；预算最优生成建议（ai-budget-optimizer）；区域市场情报（geo-market-intel-engine）；转化漏斗分析（conversion-funnel-intelligence）；宏观监控（macro-monitoring-agent）
**Layer 3 反作弊与归因层**处理 PA 渠道数据导出（pa-channel-export）、PA 报告自动化工作流（pa-report-workflow）
**Layer 4 跨文化协作层（核心差异化）**含全球化跨文化沟通引擎（cross-cultural-negotiation-copilot v2.0），覆盖 🇧🇷 巴西 / 🇨🇳 中国 / 🇪🇺 欧洲 / 🌏 东南亚 / 🇸🇦 中东 五大文化圈，包含 Soft Wording / Validation Framing / Internal Coordination 三大策略，解决多文化场景中的合作伙伴沟通壁垒

**技术创新**：每个 Skill 内嵌完整可执行 Python 脚本，AI Agent 可自动调用；所有输出自动处理编码适配（utf-8-sig × Excel 无乱码）；业务规则来自真实运营经验，非通用 Prompt；支持同一事项一键生成 5 种文化版本

**应用效果**：月结对账时间从 1 天压减至 30 分钟，PA 报表制作 100% 自动化；Wish List 区分 95% 效率提升；跨文化沟通往返次数减少 80%；新人上手时间从 2 周压缩到 2 天

（共 499 字）
```

---

## 文件 2：submission/ppt_deck.md

```markdown
# 路演 PPT —— 跨文化网盟管理 Skill 集合
# 腾讯云 2026 黑客松参赛作品
# 格式：Markdown（可转为 PDF/PPTX）
# 演绎者：[Company]
# 总页数：16 页

---

## Slide 1：封面

**标题**：跨文化网盟管理 Skill 集合
**副标题**：基于 AI Agent 的多区域 Affiliate 自动化运营系统
**参赛赛道**：腾讯云 2026 黑客松 · AI Agent Skill 赛道
**团队**：[Company] Team

---

## Slide 2：业务背景

**标题**：我们是谁？我们面临什么挑战？

**内容**：
- 🏢 跨境网盟公司，同时服务三类广告主（巴西/欧洲/中国）
- 🌐 对接三类流量源（巴西本地、中国出海 DSP/ADX、东南亚互联网）
- 📊 管理 20+ 渠道，50+ APP
- ⏰ 团队每天有几个小时在重复劳动中

---

## Slide 3：三大核心痛点

**标题**：痛点一：数据处理高度重复

| 任务 | 频率 | 耗时 |
|------|------|------|
| AppsFlyer 报表清洗 | 每周 | 2-3h |
| Adjust 数据归因去重 | 每周 | 1-2h |
| CRM 结算单对账 | 每月 | 4-6h |
| PA 反作弊报表 | 每周 | 4h+ |

---

## Slide 4：三大核心痛点

**标题**：痛点二：跨文化沟通效率低

| 挑战 | 现状 |
|------|------|
| 三类广告主 × 三类流量源 | 沟通风格差异巨大 |
| 每封邮件来回 | 5-8 次 |
| 每次沟通耗时 | 1-4 小时 |
| 文化误判后果 | 渠道流失、合作降温 |

---

## Slide 5：三大核心痛点

**标题**：痛点三：预算分配依赖经验

| 问题 | 后果 |
|------|------|
| 20+ 渠道 CAP 怎么定？ | 全凭运营经验 |
| 缺乏数据支撑 | 20-30% 预算浪费在低质量流量 |
| 决策主观性强 | 效果不稳定，难以复盘 |

---

## Slide 6：解决方案

**标题**：14 个 AI Agent Skill，五层架构

```
┌─────────────────────────────────────────────┐
│  Layer 5（顶层）                             │
│  跨文化协作层 — 核心差异化                   │
│  cross-cultural-negotiation-copilot v2.0   │
├─────────────────────────────────────────────┤
│  Layer 4：智能决策层                          │
│  ai-budget-optimizer / conversion-funnel   │
├─────────────────────────────────────────────┤
│  Layer 3：反作弊与归因层                     │
│  pa-report-workflow / pa-channel-export    │
├─────────────────────────────────────────────┤
│  Layer 2：数据分析层                         │
│  multi-mmp / geo-market / macro-monitor    │
├─────────────────────────────────────────────┤
│  Layer 1（底层）：数据接入层                 │
│  crm-channel-extraction / settlement-verify │
└─────────────────────────────────────────────┘
```

---

## Slide 7：核心差异化

**标题**：为什么 Layer 5 是核心差异化？

**核心洞察**：
- ✅ 数据处理可以用通用工具（Excel/Airbyte）
- ✅ 自动化可以用通用 RPA（Power Automate）
- ❌ **跨文化沟通没有现成工具**——这就是真正的壁垒

**AI 优势**：
- 人类学会一种跨文化表达需要数月 → AI 1 秒完成
- 1 个资深 AM 最多覆盖 1-2 种文化 → AI 同时覆盖 5 种
- 人类状态不稳定 → AI 每次稳定输出

---

## Slide 8：三大沟通策略

**标题**：Soft Wording / Validation Framing / Internal Coordination

| 策略 | 核心 | 效果 |
|------|------|------|
| **Soft Wording** | 用"观察"替代"指控" | 降低防御心理 |
| **Validation Framing** | 把"要求"包装成"共同确认" | 增加接受度 |
| **Internal Coordinator** | 把压力转给"第三方" | 保全面子 |

---

## Slide 9：五大文化圈

**标题**：覆盖全球主要商业文化

| 区域 | 核心特征 | 关键词 |
|------|---------|--------|
| 🇧🇷 巴西 | 关系导向、Chill tone | Soft wording / Emoji OK |
| 🇨🇳 中国 | 效率驱动、数据说话 | 简洁 / 直球 / Action |
| 🇪🇺 欧洲 | 流程严谨、合规优先 | Formal / Structured |
| 🌏 东南亚 | 面子文化、关系先行 | Warm-up / Face-saving |
| 🇸🇦 中东 | 尊严信任、耐心为上 | Respect / Patience |

---

## Slide 10：Demo 演示 1

**标题**：数据处理自动化

**场景**：用户说"帮我跑一下上周的 AppsFlyer 归因数据"

**执行流程**：
1. AI Agent 识别意图 → 调用 multi-mmp-attribution-engine
2. 自动读取 CSV → Source Bank 去重 → 渠道归一化
3. 输出 UTF-8-SIG 编码 CSV → Excel 直接打开无乱码

**效果**：3 小时 → 几十秒，效率提升 99%+

---

## Slide 11：Demo 演示 2

**标题**：智能预算决策

**场景**：用户问"本月哪些渠道需要调整 CAP？"

**执行流程**：
1. AI Agent 调用 conversion-funnel-intelligence
2. 分析漏斗 5 阶段 → 计算有效率百分比
3. 输出带颜色标记的 Excel 报告

| 颜色 | 有效率 | 建议 |
|------|--------|------|
| 🟢 绿色 | >80% | 增加 CAP |
| 🟡 黄色 | 50-80% | 维持不变 |
| 🔴 红色 | <50% | 降低 CAP |

---

## Slide 12：Demo 演示 3

**标题**：跨文化邮件生成

**场景**：给巴西渠道 Hertzmobi 催数据

| 版本 | 内容 |
|------|------|
| ❌ 通用 AI | "Please send the report immediately. It is already overdue." |
| ✅ 跨文化 Skill | "Hey bro, just checking in on the validation data when you have a moment 🙏 No rush at all!" |

**关键差异**：
- "overdue" → "when you have a moment"
- "immediately" → 移除，直接要求变软性请求
- 巴西人感受到被尊重，而不是被命令

---

## Slide 13：效果数据

**标题**：量化业务价值

| 指标 | Before | After | 提升 |
|------|--------|-------|------|
| 月结对账 | 1 天 | 30 分钟 | ⬇️ 90%+ |
| PA 报表制作 | 4h+/次 | 全自动 | ⬇️ 100% |
| 跨文化沟通往返 | 5-8 次 | 1-2 次 | ⬇️ 75% |
| 新人上手时间 | 2 周 | 2 天 | ⬇️ 86% |
| 预算浪费 | 20-30% | 数据驱动 | ✅ 质变 |

---

## Slide 14：技术架构亮点

**标题**：Skill as Code — 每个 Skill 都是完整的解决方案

| 特性 | 说明 |
|------|------|
| 完整脚本 | 每个 Skill 含可执行 Python 脚本，非纯 Prompt |
| 编码自适应 | UTF-8-SIG × Excel 无乱码，跨平台兼容 |
| 业务规则内置 | 来自真实运营经验，非通用 AI 泛化回答 |
| 独立可执行 | 可单独运行，也可组合使用 |

---

## Slide 15：参赛定位

**标题**：为什么这个作品能赢？

| 维度 | 我们的优势 |
|------|-----------|
| **赛道契合** | 直接对应"AI Agent Skill"赛道核心诉求 |
| **真实需求** | 来自 [Company] 实际业务，非纸上谈兵 |
| **技术深度** | Skill as Code，完整可执行，非纯文档 |
| **差异化** | 跨文化沟通 Engine，无竞品直接对标 |
| **可落地性** | 已验证效果，有量化指标支撑 |

---

## Slide 16：结语 & CTA

**标题**：让 AI Agent 真正赋能跨境网盟业务

**一句话**：跨文化网盟管理 Skill 集合——把人类数月才能掌握的跨文化能力，变成 AI 的即时能力。

**团队**：M COMPANY Team

**参赛赛道**：腾讯云 2026 黑客松 · AI Agent Skill 赛道

**感谢观看！**
```

---

## 文件 3：submission/technical_doc.md

```markdown
# 产品说明文档
# 腾讯云 2026 黑客松参赛作品
# 跨文化网盟管理 Skill 集合
# 格式：Markdown（可转为 PDF/DOCX 提交）
# 演绎者：[Company] Team

---

## 目录

1. [产品概述](#1-产品概述)
2. [背景与痛点](#2-背景与痛点)
3. [解决方案架构](#3-解决方案架构)
4. [13 个 Skill 详细说明](#4-13-个-skill-详细说明)
5. [技术创新点](#5-技术创新点)
6. [应用场景与效果](#6-应用场景与效果)
7. [核心技术差异化：跨文化沟通 Skill](#7-核心技术差异化跨文化沟通-skill)

---

## 1. 产品概述

### 1.1 基本信息

| 项目 | 内容 |
|------|------|
| 产品名称 | 跨文化网盟管理 AI Agent Skill 集合 |
| 英文名 | Cross-Cultural Affiliate Network Management Skills |
| 参赛赛道 | 腾讯云 2026 黑客松 · AI Agent Skill Track |
| 适用平台 | CodeBuddy / WorkBuddy / OpenClaw |
| Skill 数量 | 13 个 |
| 版本 | v1.0 |
| 创建日期 | 2026-05-12 |

### 1.2 一句话描述

将跨境网盟运营知识封装为 13 个可复用的 AI Agent Skill，实现多区域、多文化、多 MMP 场景下的运营自动化。

---

## 2. 背景与痛点

### 2.1 业务背景

[Company] 作为跨境网盟公司，同时服务三类广告主（巴西/欧洲/中国），对接三类流量源（巴西本地、中国出海 DSP、东南亚互联网），管理二十多个渠道和五十多个 APP。

### 2.2 三大核心痛点

| 痛点 | 表现 | 影响 |
|------|------|------|
| **数据处理高度重复** | 每周 5+ 份报表手动清洗、去重、合并，每次耗时 3-5 小时 | 运营团队 30% 时间消耗在重复劳动 |
| **跨文化沟通效率低** | 三类广告主 × 三类流量源，沟通风格差异大，邮件往返 5-8 次 | 每次沟通耗时 1-4 小时，效率极低 |
| **预算分配依赖经验** | 每月二十多个渠道的 CAP 怎么定？全凭运营经验和直觉 | 20-30% 的预算浪费在低质量流量上 |

---

## 3. 解决方案架构

### 3.1 四层 Skill 架构

```
Global Affiliate Ops Agent
├── Layer 1 — 数据接入层 (Data Connectors)
│   ├── crm-channel-extraction     — OCR 结算单自动提取
│   ├── crm-settlement-verification — 自动对账 + 异常标记
│   └── pa-channel-export          — PA 标准化报告生成
│
├── Layer 2 — 数据分析层 (Business Intelligence)
│   ├── multi-mmp-attribution-engine — 多 MMP 归因去重
│   ├── cross-regional-revenue-audit — Campaign 盈利核算
│   ├── ai-budget-optimizer        — 预算最优分配
│   ├── conversion-funnel-intelligence — 转化漏斗 + CAP 建议
│   ├── geo-market-intel-engine    — 区域市场情报
│   ├── macro-monitoring-agent     — 宏观经济监控
│   ├── wish-intelligence-collector — Wish List 解析
│   └── regional-wish-classifier  — 区域分类
│
├── Layer 3 — 反作弊与归因层 (Fraud & Attribution)
│   ├── pa-report-workflow         — PA 报告自动化
│   └── [扩展中]
│
└── Layer 4 — 跨文化协作层 (Core Differentiator)
    └── cross-cultural-negotiation-copilot — 跨文化沟通引擎
```

### 3.2 技术架构原则

| 原则 | 说明 |
|------|------|
| **单一职责** | 每个 Skill 只解决一个明确的业务问题 |
| **独立可执行** | 每个 Skill 包含完整 Python 脚本，可单独运行 |
| **层间解耦** | 上层不依赖下层具体实现，只依赖输出格式 |
| **渐进增强** | 可从单 Skill 使用逐步扩展到全链路自动化 |

---

## 4. 13 个 Skill 详细说明

### 4.1 Layer 1 — 数据接入层

#### crm-channel-extraction

| 属性 | 内容 |
|------|------|
| **功能** | 从 OCR 识别的结算单 PDF/图片中自动提取渠道名和金额 |
| **输入** | OCR 输出的文本文件（含渠道名、金额信息） |
| **输出** | 结构化的渠道-金额映射表（CSV/JSON） |
| **解决痛点** | 结算单手工录入 1-1.5 小时/次 → 自动 3 分钟 |
| **版本** | v1.0.0 |

#### crm-settlement-verification

| 属性 | 内容 |
|------|------|
| **功能** | 自动对账，标记差异 >5% 的异常项 |
| **输入** | 两份数据源：内部 CRM 记录 vs 渠道提交的结算单 |
| **输出** | 对账报告（匹配项 + 差异项 + 异常标记） |
| **解决痛点** | 人工对账 2 小时 → 自动 3 分钟 |
| **版本** | v1.0.0 |

#### pa-channel-export

| 属性 | 内容 |
|------|------|
| **功能** | 生成 Partner Alliance 格式的标准化投放报告 |
| **输入** | 归因后的渠道数据 + 预算分配数据 |
| **输出** | 符合 PA 规范的标准化报告（Excel/CSV） |
| **解决痛点** | 手工制表 0.5-1 小时/次 → 一键导出 |
| **版本** | v1.0.0 |

### 4.2 Layer 2 — 数据分析层

#### multi-mmp-attribution-engine (v1.1.0)

| 属性 | 内容 |
|------|------|
| **功能** | 多 MMP 归因去重，基于 Source Bank 优先级，输出纯净归因数据 |
| **输入** | AppsFlyer/Adjust 原始导出 CSV（可能含多个 MMP 来源） |
| **输出** | 去重后的归因 CSV（utf-8-sig 编码） |
| **脚本** | `affiliate_attribution.py` |
| **版本** | v1.1.0 |

#### conversion-funnel-intelligence (v1.1.0)

| 属性 | 内容 |
|------|------|
| **功能** | JXXXX 信贷漏斗 5 阶段分析，输出渠道 CAP 建议 |
| **输入** | AppsFlyer 事件数据 + e-Grana CRM 数据 |
| **输出** | 带颜色标记的 Excel 报告（绿/黄/红三级）+ CAP 建议 |
| **脚本** | `jxxxx_funnel.py` |
| **版本** | v1.1.0 |

#### cross-cultural-negotiation-copilot (v2.0)

| 属性 | 内容 |
|------|------|
| **功能** | 巴西 ↔ 中国跨文化沟通风格适配与话术生成 |
| **输入** | 沟通场景（催数据、确认 Offer、谈判 CAP、投诉处理）+ 目标语种 |
| **输出** | 符合巴西/中国商务文化的英语邮件/WhatsApp 消息草稿 |
| **版本** | v2.0 |
| **定位** | ⭐ 核心技术差异化 Skill |

---

## 5. 技术创新点

### 5.1 Skill 即代码（Skill as Code）

传统 AI Agent 方案只有 Prompt（提示词），调用外部 API 或依赖人工操作。本作品的每个 Skill 都包含**完整可执行 Python 脚本**，AI Agent 可以独立调用执行。

### 5.2 跨平台编码自适应

网盟业务涉及多国数据，文件编码问题是日常高频痛点。本作品在所有 Skill 中内置了完整的编码处理策略：

| 场景 | 处理方式 |
|------|---------|
| 输入文件编码未知 | 自动检测（chardet 算法） |
| 输出给 Windows 用户 | utf-8-sig + CRLF |
| 输出给 Mac/Linux 用户 | utf-8 + LF |
| .bat/.cmd 脚本中文 | GBK 编码 |

### 5.3 业务规则内置

每个 Skill 中的业务规则都来自 [Company] 团队的真实运营经验，不是通用 AI 的泛化回答：

| 示例 | 通用 AI 回答 | 本作品 Skill |
|------|------------|-------------|
| "如何去重？" | "用 pandas drop_duplicates()" | 基于 Source Bank 优先级的归因逻辑，考虑渠道优先级顺序 |
| "怎么写英文邮件？" | 标准商务英语模板 | Soft Wording + Validation Framing + Internal Coordination 三大策略 |
| "哪些该降 CAP？" | "看 ROI 低的" | JXXXX 漏斗 5 阶段有效率分级 + Factor 计算 + 三色标记 |

---

## 6. 应用场景与效果

### 场景一：月结对账（每月一次）

**Before**：
- 周五下午开始 → 导出 5 份报表 → 手工清洗 3h → 对账 2h → 发现差异 → 追溯原因 → 重新核算 → 周末加班

**After**：
- 运行 multi-mmp-attribution-engine → 自动去重归因
- 运行 crm-settlement-verification → 自动对账标记异常
- 查看差异项（通常 <5 项）→ 确认
- 耗时：30 分钟

**提升：96%**

### 场景二：跨文化沟通（每天多次）

**Before**：
- 中国运营写英文邮件 → 巴西渠道觉得太直接 →
- 修改措辞 → 再发 → 还是不对 → 来回 5-8 次，平均每次沟通耗时 1-4 小时

**After**：
- 运营告诉 AI：帮我写封邮件给 Hertzmobi 要数据
- AI 调用 cross-cultural-negotiation-copilot
- 输出符合 Soft Wording 规范的邮件 →
- 运营检查后发送 → 通常 1 次搞定，平均每次沟通耗时 15-30 分钟

**提升：75-87%**

### 6.1 效果汇总

| 指标 | Before | After | 提升 |
|------|--------|-------|------|
| 月结对账耗时 | 1 天 | 30 分钟 | **96% ↓** |
| 报表清洗去重 | 3-5h/次 | 自动完成 | **100% ↓** |
| 跨文化沟通往返 | 5-8 次/次 | 1-2 次/次 | **75% ↓** |
| 预算分配依据 | 经验驱动 | 数据驱动 | **质变** |
| 新人上手时间 | 2 周 | 2 天 | **86% ↓** |

---

## 7. 核心技术差异化：跨文化沟通 Skill

### 7.1 为什么这是核心差异化？

市面上的 AI Agent 工具大多聚焦在"数据处理"和"自动化"层面，极少关注*跨文化商务沟通*这一最刚需场景。

对于跨境网盟公司来说：
- ✅ 数据处理可以用通用工具（Excel/Airbyte/Fivetran）
- ✅ 自动化可以用通用 RPA（iPath/Power Automate）
- ❌ **跨文化沟通没有现成工具**——这就是真正的壁垒

### 7.2 三大沟通策略详解

#### Strategy 1: Soft Wording（委婉措辞）

**问题**：中文/英文的直接表达在巴西文化中被视为傲慢。

| ❌ Direct（避免） | ✅ Soft Wording（推荐） |
|------------------|----------------------|
| Send the report now. | Would you mind sharing the report when you have a moment? |
| This is overdue. | I wanted to follow up on this to make sure nothing fell through the cracks. |
| We need this urgently. | It would be really helpful to have this by [date] if possible. |

#### Strategy 2: Validation Framing（确认式框架）

**问题**：直接提出要求容易被拒绝；先确认共识再提要求，对方更易接受。

**模板**：
```
Step 1: 确认双方理解一致（"Just to confirm we're aligned on..."）
Step 2: 表达感谢/认可（"Really appreciate your support on..."）
Step 3: 温和提出下一步（"Would it be possible to..."）
```

#### Strategy 3: Internal Coordination Positioning（内部协调定位）

**问题**：直接施压会破坏关系；将压力推给"内部其他部门"，保全面子。

**模板**：
```
"Our [finance/legal/compliance] team is asking for..."
"Our internal process requires..."
"To keep everything smooth on our end..."
```

---

## 8. 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| Skill 定义 | Markdown (YAML frontmatter) | 元数据 + 文档 + 脚本 |
| 自动化脚本 | Python 3.9+ | pandas, openpyxl, requests, chardet |
| AI Agent 运行环境 | OpenClaw / WorkBuddy | Skill 加载 + 调用 + 工具调用 |
| 编码处理 | 自研（write_file.py） | 跨平台编码推送 + BOM/CRLF 自动适配 |
| 数据格式 | CSV / JSON / Excel (xlsx) | 输入输出均支持 |
| 定时任务 | Cron / OpenClaw Scheduler | macro-monitoring-agent 定时触发 |

---

## 9. 未来规划

### Phase 1（近 1-2 月）
- [ ] 接入 AppFollow/AppMagic API，让 geo-market-intel-engine 输出真实排行数据
- [ ] 补充 Partner Risk Radar Skill（渠道风控预警）
- [ ] 补充 Campaign Health Doctor Skill（活动健康度诊断）

### Phase 2（中 3-6 月）
- [ ] 接入腾讯云 API（TDS 用户触达）、OCR（智能结算单识别）、多语言翻译
- [ ] 发布到 SkillHub 平台，供其他网盟公司使用
- [ ] 支持更多 MMP 平台（SingTen、AppsFlyer 新版等）

### Phase 3（长 6-12 月）
- [ ] 构建 Skill Marketplace（技能市场），支持组织协作
- [ ] 接入大模型多轮对话，让跨文化沟通更加自然
- [ ] 多租户 SaaS 化，服务中小型网盟公司

---

*文档版本：v1.0 | 创建日期：2026-05-12 | 演绎者：[Company] Team*
*总字数：约 3500 字（不含代码块）*
```

---

## 文件 4：submission/video_script.md

```markdown
# 视频脚本 —— 跨文化网盟管理 Skill 集合
# 腾讯云 2026 黑客松 · 演示视频
# 时长：4-5 分钟（建议 4 分钟）
# 格式：MP4（1080p）
# 总字数：约 900 字（匀速大约 220 字/分钟）

---

## 视频基本信息

| 项目 | 内容 |
|------|------|
| **总时长** | 4 分钟，40 秒 |
| **格式** | MP4，1080p |
| **风格** | 专业 + 务实，不浮夸 |
| **字幕** | 中文为主，关键词保留英文 |
| **BGM** | 前 30 秒轻快结尾曲，中间平滑，结尾上扬 |

---

## 分镜头脚本

---

### 🎬 Scene 1：开场（0:00 - 0:25）≈ 25 秒

**画面**：
- 黑屏渐显作品标题：「跨文化网盟管理 Skill 集合」
- 副标题：「基于 AI Agent 的多区域 Affiliate 自动化运营系统」
- 背景用流动的全球地图（巴西/欧洲/中国/东南亚五颜六色地闪烁）
- 底部显示 "腾讯云 2026 黑客松 · [Company]"

**字幕**：
> 我们是？M COMPANY，一家跨境网盟公司。每天要同时服务巴西、欧洲、中国三类广告主，对接巴西本地、中国出海、东南亚三类流量源，管理二十多个渠道和五十多个 APP。听起来很厉害吧？但现实是——我们团队每天有几个小时在重复劳动中。

**画面动作**：
- 标题停留 5 秒后，切入一个快节奏蒙太奇：
  - Excel 表格密密麻麻的数据
  - WhatsApp 里发来的英文消息
  - 结算单 PDF 飘来飘去
  - 一个人对着电脑眉头紧锁

---

### 🎬 Scene 2：痛点深挖（0:25 - 1:00）≈ 35 秒

**画面**：
- 分屏展示三大痛点（左中右三栏）
- 每个痛点配一个简短的动画

**字幕**：
> 第一个痛点——数据处理。每周我们要从 AppsFlyer、Adjust 导出十份以上的报表，手工清洗、去重、合并，每次轮三到五个小时。还有 PA 反作弊报表，四类数据 × 多个 APP，制作一次要四个多小时？
>
> 第二个痛点——跨文化沟通。我们同时服务巴西、欧洲、中国三类广告主，对接三类流量源，沟通风格差异巨大。一封确认 Offer 细节的邮件，平均来回五到八次才能定下来。
>
> 第三个痛点——预算分配。每个月二十多个渠道的 CAP 怎么定？全凭运营的经验和"感觉"。结果就是——百分之二三十的预算浪费在了低质量流量上。

**画面动作**：
- 左栏：Excel 数据 ← 手工标记 ← 时间轴飞快转动
- 中栏：WhatsApp 对话不断弹出 ← 翻译工具 ← 对话越来越长
- 右栏：图表 ← 预算分配不均 ← 红色区域标注"浪费"

---

### 🎬 Scene 3：解决方案总览（1:00 - 1:35）≈ 35 秒

**画面**：
- 五层架构图从下往上逐层显现（带动画）
- 每层出现时，对应的 Skill 标签依次点亮

**字幕**：
> 所以我们做了一个决定——把所有这些业务知识，封装成 14 个 AI Agent Skill，组成一个五层架构的系统。
>
> 最底层是数据接入层，负责从结算单、CRM 系统自动提取数据。
> 往上是数据分析层，含 Wish List 分析、预算优化、区域市场情报、转化漏斗分析、宏观经济监控。
> 再往上是反作弊与归因层，处理 PA 报表、归因去重、反欺诈分析。
> 再往上是智能决策层，输出渠道 CAP 建议、盈利核算、异常预警。
> 最顶层——也是我们最核心的创新——跨文化沟通引擎，专门解决同时服务多类广告主、对接多类流量源时的文化和语言障碍。
**画面动作**：
- 架构图从底层 Layer 1 开始，一层层往上生成
- 每层出现时，对应的 Skill 图标依次高亮
- Layer 5 出现时加一个 ⭐ 特效（标注"核心差异化"）

---

### 🎬 Scene 4：Demo 1 数据处理（1:35 - 2:10）≈ 35 秒

**画面**：
- 分屏演示：用户在对话框输入指令
- AI 自动调用脚本，终端屏幕显示执行过程
- 最终输出 CSV 文件在 Excel 中打开，数据显示正常

**字幕**：
> 来看第一个演示场景——数据处理自动化。
>
> 用户只需说一句话："帮我跑一下上周的 AppsFlyer 归因数据。"
>
> AI Agent 自动调用 multi-mmp-attribution-engine 这个 Skill，执行 Python 脚本完成 Source Bank 去重、渠道变体归一化，然后输出一份干净的 CSV 文件。
>
> 注意看——这份文件直接用 Excel 打开，中文完全正常，没有任何乱码。因为我们的脚本自动处理了编码问题。
>
> 这整个过程，以前需要三个小时，现在只需要几十秒？

**画面动作**：
- 用户输入框打勾 → 回车
- 终端窗口滚动执行日志
- CSV 文件生成 ← 双击打开 ← Excel 显示整齐的数据
- 字幕：演示"无乱码"那一刻，在 Excel 加一个特写

---

### 🎬 Scene 5：Demo 2 智能决策（2:10 - 2:50）≈ 40 秒

**画面**：
- 用户咨询：本月哪些渠道需要调整 CAP
- AI 输出带颜色标记的 Excel 报告
- 绿色/黄色/红色等级分明

**字幕**：
> 第二个演示——智能决策。
>
> 用户问："本月 JXXXX Campaign 哪些渠道需要调整 CAP？"
>
> AI 调用 conversion-funnel-intelligence 这个 Skill，分析转化漏斗的五个阶段，计算每个渠道的有效率百分比。
>
> 然后输出这样一份报告——绿色行代表高有效率渠道，建议增加 CAP；黄色行维持不变；红色行低有效率，建议降低 CAP。
>
> 不再靠经验拍脑袋了，每个建议背后都有数据支撑。
**画面动作**：
- 用户输入问题
- 执行过程（漏斗图动画 + 数据流转）
- Excel 报告打开 ← 鼠标滑过绿色行 ← 黄色行 ← 红色行
- 最后定格在三种颜色的对比图上

---

### 🎬 Scene 6：Demo 3 跨文化沟通（2:50 - 3:20）≈ 30 秒

**画面**：
- 左右分屏：左侧是"错误示范"，右侧是"正确示范"
- 错误示范：AI 直接生成的生硬邮件 ← 红色叉
- 正确示范：调用跨文化 Skill 后生成的适配邮件 ← 绿色勾

**字幕**：
> 第三个演示——也是我们最得意的部分——跨文化沟通引擎。
>
> 如果让通用 AI 写一封给巴西渠道催数据的邮件，它会写成这样——"请立即发送报告，已经过期了。" 已经扎心了对吗？但在巴西文化里，这会被认为非常傲慢。
>
> 但是如果调用我们的 cross-cultural-negotiation-copilot 这个 Skill，AI 会自动识别目标文化背景，使用 Soft Wording 表达策略，把同一件事变成适合当地商业文化的措辞。
>
> 同样的目的，完全不同的效果。而且——这套引擎覆盖巴西、中国、欧洲、东南亚、中东五大文化圈，同一件事可以一键生成五种不同文化的版本。
>
> 人类需要数月才能掌握一种跨文化表达，AI 可以再一秒内完成多文化切换。

**画面动作**：
- 左屏：❌ 邮件内容 + 巴西国旗 + 😰 表情（表示被冒犯）
- 右屏：✅ 邮件内容 + 握手标志 + 😄 表情（表示合作关系）
- 关键词高亮："Would you mind..." / "Our finance team is asking..."
- 最后显示 5 个文化图标并列（🇧🇷🇨🇳🇪🇺🌏🇸🇦）

---

### 🎬 Scene 7：效果总结（3:20 - 3:45）≈ 25 秒

**画面**：
- Before / After 对比表格（动态数字翻动效果）
- 每一行数字从 Before 的数值翻转到 After 的数值

**字幕**：
> 总结一下这套 Skill 集合带来的改变——
>
> 月结对账时间，从一天压减到了三十分钟，效率提升百分之九十多。
>
> PA 报表制作，从四个多小时变成了全自动，效率提升百分之百。
>
> 跨文化沟通往返，从五次八次降到了两次以内。
>
> 新人上手时间，从两周压缩到两天。
>
> 最重要的是——预算分配终于从"感觉驱动"变成了"数据驱动"。

**画面动作**：
- 大号数字依次翻动：
  - "1 天 → 30 分钟" ← 90%+ ⬆️
  - "4-6 小时/次 → 自动完成" ← 100% ⬆️
  - "5-8 次 → 1-2 次" ← 75% ⬆️
  - "2 周 → 2 天" ← 86% ⬆️
- 每个数字翻动时配一个 ✅ 的动画效果

---

### 🎬 Scene 8：收尾（3:45 - 4:00）≈ 15 秒

**画面**：
- 回到开场标题页的收尾风格
- 作品名称 + 团队名 + 腾讯云 Logo
- 底部滚动显示技术关键词

**字幕**：
> 跨文化网盟管理 Skill 集合——让 AI Agent 真正赋能跨境网盟业务。
>
> 我们是？M COMPANY 团队，感谢观看！

**画面动作**：
- 标题居中
- 全球地图淡出
- 底部技术关键词滚动：Python · AI Agent · Skill as Code · Cross-Cultural Communication Engine · Multi-MMP Attribution
- 最后定格在 "Q&A" 字幕上

---

## 制作注意事项

### 录制建议
1. **Demo 部分**必须用真实屏幕录制，不要用模拟截图
2. 如果真实数据敏感，可用脱敏后的示例数据
3. Excel 打开 CSV 无乱码的那个细节——**要特写**，这是评委容易记住的亮点
4. 跨文化沟通的左右分屏对比——**要有冲击力**，让评委看清差异

### 字幕建议
- 语速：中等偏快（200-240 字/分钟），保持专业但不拖沓
- 重点数据适当放慢强调
- Demo 操作部分可以稍微加快，展现"自动化"的高效感

### BGM 建议
- 0:00-0:25：轻快引入（如 Upbeat Corporate）
- 0:25-3:20：平滑过渡（如 Ambient Corporate）
- 3:20-4:00：收尾上扬（如 Inspiring Uplift）

### 字幕
- 全程配中文字幕（评委可能不懂英文）
- 关键词术语（Skill 名称、APP 名）保留英文原名

---

*视频脚本版本 v2.0 | 2026-05-12 | 总时长 4 分钟 | 适配 13 个 Skill + 五大文化圈*
```

---

## 文件 5：submission/video_script_jianying.md

```markdown
# 字幕·图文成片·专用脚本
# 复制下方分隔符之间的中文，粘贴到剪映 → 图文成片 → 输入台词 → 选择风格
# 建议风格：科技感或商务风
# 完成后删除此说明文字

---

我们是？M COMPANY，一家跨境网盟公司。每天要同时服务巴西、欧洲、中国三类广告主，对接二十多个渠道和五十多个 APP。听起来很厉害？但现实是——我们团队每天有几个小时在重复劳动中。

第一个痛点是数据处理。每周要从 AppsFlyer、Adjust 导出十份以上的报表，手工清洗、去重、合并，每次轮三到五个小时。还有 PA 反作弊报表，制作一次要四个多小时？

第二个痛点是跨文化沟通。同时服务三类广告主，对接三类流量源，沟通风格差异巨大。一封确认 Offer 细节的邮件，平均来回五到八次才能定下来。

第三个痛点是预算分配。每个月二十多个渠道的 CAP 怎么定？全凭运营的经验和感觉。结果就是百分之二三十的预算浪费在了低质量流量上。

所以我们做了一个决定——把所有这些业务知识，封装成 14 个 AI Agent Skill，组成一个五层架构的系统。

最底层是数据接入层，负责自动提取数据。往上是数据分析层，含 Wish List 分析、预算优化、区域市场情报。再往上是反作弊与归因层。再往上是智能决策层。最顶层——也是我们最核心的创新——跨文化沟通引擎，专门解决多文化场景下的语言障碍。

来看第一个演示——数据处理自动化。用户只需说一句话，AI Agent 自动调用脚本完成 Source Bank 去重、渠道归一化，然后输出一份干净的 CSV 文件。注意看——这份文件直接用 Excel 打开，中文完全正常，没有任何乱码。整个过程，以前需要三个小时，现在只需要几十秒。

第二个演示——智能决策。用户问本月哪些渠道需要调整 CAP，AI 分析转化漏斗五个阶段，计算每个渠道的有效率百分比，然后输出带颜色标记的报告。绿色行代表高有效率渠道，建议增加 CAP；黄色行维持不变；红色行建议降低 CAP。每个建议背后都有数据支撑。

第三个演示——也是我们最得意的——跨文化沟通引擎。如果让通用 AI 写一封给巴西渠道催数据的邮件，它会写成——请立即发送报告，已经过期了。已经扎心了。但在巴西文化里，这会被认为非常傲慢。但如果调用我们的跨文化 Skill，AI 会自动使用 Soft Wording 策略，把同一件事变成适合当地商业文化的措辞。人类需要数月才能掌握一种跨文化表达，AI 可以再一秒内完成多文化切换。

总结一下——月结对账时间，从一天压减到了三十分钟，效率提升百分之九十多。PA 报表制作，从四个多小时变成了全自动。跨文化沟通往返，从五次八次降到了两次以内。新人上手时间，从两周压缩到两天。最重要的是——预算分配终于从感觉驱动变成了数据驱动。

跨文化网盟管理 Skill 集合——让 AI Agent 真正赋能跨境网盟业务。我们是？M COMPANY 团队，感谢观看！

---

## 使用说明（生成后可删除）

1. 打开剪映专业版 → 首页点「图文成片」
2. 把上方分隔符之间的全部中文复制粘贴到台词输入框
3. 选择一个风格（推荐「科技」或「商务」）
4. 点生成 → 等 3-5 分钟
5. 生成后建议检查：
   - 场景 4/5/6（Demo 部分）：如果 AI 匹配的画面不够真实，建议替换为真实截图
   - 结尾：加上作品名字幕 + 团队 Logo
6. 导出前检查字幕是否有错别字
```

---

## 文件 6：skills/cross-cultural-negotiation-copilot/SKILL.md

```markdown
---
name: cross-cultural-communication-engine
display_name: "Cross-Cultural Negotiation Copilot | 跨文化谈判智能助手"
description: |
  This skill should be used when the user needs to draft professional communications (emails, messages) for cross-cultural affiliate network operations.
  
  It automatically adapts tone, wording, and communication style based on the target culture (Brazil, China, Europe, Southeast Asia, Middle East), applies "soft wording" techniques to reduce defensiveness, and generates culturally appropriate email drafts with subject lines and sign-offs.
  
  Key features:
  - Five-cultivation framework (Brazil/China/Europe/SE Asia/Middle East)
  - Validation Framing: frames requests as "joint确认" rather than demands
  - Internal Coordinator: transfers pressure to "third party" to save face
  - Multi-push escalation templates (3 levels of gentle persistence)
  - Good news/bad news communication strategies
  
  Applicable for affiliate AM teams managing partners across multiple cultural backgrounds, reducing email round-trips by 80%.
version: 1.0.0
agent_created: true
compatibility:
  platforms: [CodeBuddy, WorkBuddy, OpenClaw]
  requirements: [Python 3.9+]

category: cross-cultural-collaboration
tags: [cross-cultural, negotiation, communication, brazil-china, soft-skills]
layer: 4
trigger_keywords:
  - "跨文化沟通"
  - "邮件草稿"
  - "谈判话术"
  - "巴西沟通"
  - "cross-cultural"

---

---

# cross-cultural-communication-engine

## 全球化网盟跨文化沟通引擎 v2.0

> **核心价值：不是把英语写得"正确"，而是在多种商业文化之间实时"翻译气氛"。**
>
> **人类痛点**：学会一种跨文化表达需要数月沉浸 → 切换文化理解状态再写作 → 极耗精力
> **AI 优势**：1 秒识别目标文化 → 自动切换语气/措辞/节奏 → 每次都"像当地人"

---

## 一、为什么人类做不好这件事？

### 认知负荷分析

```
人类写一封跨文化邮件的认知流程：

Step 1: 理解业务需求（我要催数据/要结算/谈 CAP）
    ↓ ~10 秒
Step 2: 识别对方文化背景（巴西渠道？欧洲广告主？中东 Partner？）
    ↓ ~5 秒（但经常搞混！）
Step 3: 切换到对应文化的思维模式
    ↓ ~30+ 秒（这是最难的！需要"进入角色"）
Step 4: 用英语写出符合该文化的表达
    ↓ ~5-15 分钟（反复斟酌用词）
Step 5: 自查：会不会太直接？够不够正式？emoji 用多了？
    ↓ ~2-5 分钟（焦虑时间）
Total: ~10-25 分钟/封，且质量不稳定

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

AI Agent 的认知流程：

Step 1: 用户说 "帮我写封邮件给巴西渠道催 settlement"
    ↓
Step 2: AI 识别 → 目标=🇧🇷巴西渠道 + 场景=催数据
    ↓
Step 3: 自动加载 🇧🇷 文化配置（soft wording / chill tone / emoji OK）
    ↓
Step 4: 输出完整邮件（含 subject / body / sign-off）
    ↓
Total: < 3 秒，质量稳定，每次都"像在当地工作过3年的AM"
```

### 关键洞察

| 维度 | 人类 | AI Agent |
|------|------|---------|
| 文化切换速度 | 需要心理准备时间（30秒~数分钟） | 即时（<1秒） |
| 表达一致性 | 取决于当天状态、疲劳程度 | 始终稳定 |
| 多文化同时处理 | 极难（同时服务巴西+欧洲+中国广告主） | 天然优势 |
| "进入角色"能力 | 需要真实沉浸经验 | 通过 Skill 规则精确模拟 |
| 规模化 | 1 个资深 AM 只能覆盖 1-2 个文化圈 | 无限并行 |

**结论**：这不是"辅助工具"，而是**人类能力盲区的补全**。

---

## 二、五大文化圈沟通画像

### 🇧🇷 巴西（Brazil）— 关系导向型

| 维度 | 特征 |
|------|------|
| **核心价值观** | 关系 > 规则、情绪舒适度 > 效率、face-saving > 准确性 |
| **沟通节奏** | 慢热、"Já vou"（马上）可能 = 3小时后 |
| **典型忌讳** | 太正式（像法务）、太直接（像在命令）、连续 push |
| **最佳状态** | "Chill but responsive" — 像一起赚钱的 partner |
| **Emoji 策略** | ✅ 大量使用（🙌👀🤔😊），但不过度 |
| **称呼习惯** | bro / dude / 名字 first name |
| **开场白** | "Hey bro!" / "Tudo bem?" / "Como vai?" |
| **压力容忍度** | ⚠️ 低 — 压迫感重会流失合作意愿 |

**关键词**：soft wording / casual ping / emotional buffering / internal coordinator

---

### 🇨🇳 中国（China）— 结果导向型

| 维度 | 特征 |
|------|------|
| **核心价值观** | 效率 > 形式、结果 > 过程、数据 > 感受 |
| **沟通节奏** | 快、期望即时回复、不喜欢等 |
| **典型忌讳** | 太啰嗦、绕弯子、没有明确 action item |
| **最佳状态** | 简洁高效、关键指标突出、有明确下一步 |
| **Emoji 策略** | 🔶 适度使用（👍✅📊），商务场景克制 |
| **称呼习惯** | 名字 / 英文名 / 职位 |
| **开场白** | "Hi [Name]" / 直接进入主题 |
| **压力容忍度** | ✅ 高 — 接受直球，但要有理有据 |

**关键词**：简洁 / 数据驱动 / action-oriented / 同步效率

---

### 🇪🇺 欧洲（Europe）— 流程严谨型

| 维度 | 特征 |
|------|------|
| **核心价值观** | 流程 > 速度、合规 > 灵活、书面确认 > 口头约定 |
| **沟通节奏** | 稳定、按计划走、不喜意外 |
| **典型忌讳** | 太随意（不专业）、数据无来源、承诺无法兑现 |
| **最佳状态** | 正式但友好、结构清晰、附件齐全 |
| **Emoji 策略** | ⚠️ 极少使用（仅 😊🤝），商务邮件几乎不用 |
| **称呼习惯** | Dear [First Name] / Hi [Name] |
| **开场白** | "I hope this email finds you well." |
| **压力容忍度** | 中 — 只要流程合理、提前通知即可 |

**关键词**：formal / structured / compliance / documentation / UTC time

---

### 🌏 东南亚（Southeast Asia）— 社交关系型

| 维度 | 特征 |
|------|------|
| **核心价值观** | 面子 > 一切、关系建立 > 商务推进、间接 > 直接 |
| **沟通节奏** | 中等偏慢、需要 warm-up 阶段 |
| **典型忌讳** | 当众拒绝/纠错、说"No"、让对方面子上过不去 |
| **最佳状态** | 礼貌热情、先聊生活再谈生意、给足面子 |
| **Emoji 策略** | ✅ 大量使用（😊🙏💪🎉），比巴西还丰富 |
| **称呼习惯** | Brother / Boss / 名字 + 称谓 |
| **开场白** | "Hi [Name]! Hope you're doing great!" |
| **压力容忍度** | ⚠️ 低 — 但会用微笑掩饰不满 |

**关键词**：face-saving / indirect / warm-up / relationship-first

---

### 🇸🇦 中东（Middle East）— 尊严信任型

| 维度 | 特征 |
|------|------|
| **核心价值观** | 信任 > 合同、尊严 > 效率、个人关系 > 公司关系 |
| **沟通节奏** | 慢、决策周期长、需要多次非正式接触 |
| **典型忌讳** | 质疑诚信、公开冲突、催促太紧 |
| **最佳状态** | 尊重、耐心、通过中间人建立信任 |
| **Emoji 策略** | 🔶 适中（🤝👍🌟），不过分随意 |
| **称呼习惯** | Mr. [Name] / My friend / 尊称 |
| **开场白** | "Assalamu alaykum / Peace be upon you" 或 "Dear Mr. [Name]" |
| **压力容忍度** | ⚠️⚠️ 很低 — 催促 = 不信任 = 关系受损 |

**关键词**：patience / trust-building / respect / intermediary

---

## 三、文化对比速查表

| 场景 | 🇧🇷 巴西 | 🇨🇳 中国 | 🇪🇺 欧洲 | 🌏 东南亚 | 🇸🇦 中东 |
|------|---------|---------|---------|---------|---------|
| **催数据** | "Could you check when you have a moment? No rush 🙌" | "麻烦核对一下数据，今天能给反馈吗？" | "Could you please validate the data by [date]?" | "Brother, if convenient, can help check? 🙏" | "My friend, when possible for you 🤝" |
| **指出错误** | "Maybe I missed something on my end 🤔" | "数据这里有点问题，请确认" | "We noticed a discrepancy in line X" | "Small observation here, maybe we can discuss 😊" | "There may be a small difference to review together" |
| **Push 第1次** | "Just checking 👀" | "跟进一下进度" | "Gentle reminder regarding X" | "Quick check-in brother! 💪" | "Whenever convenient my friend" |
| **Push 第2次** | "Any update when you have a chance? 🙏" | "这个事情比较急，麻烦尽快" | "Following up on our previous correspondence" | "Any news on this? Hope all good! 😊" | "No pressure at all, just checking in 🤝" |
| **Push 第3次** | "Need to close internal validation, help me out? 🙏" | "今天必须给到，不然影响结算" | "Urgent: deadline approaching for X" | "Brother really need your help here! 🙏💪" | "My friend, I am in difficult position, need your support" |
| **结尾** | "Cheers! / Abraço!" | "谢谢 / Best regards" | "Best regards / Kind regards" | "Thanks brother! Take care! 🙏" | "Best wishes / Respectfully" |
| **Email Subject** | 简短口语化 | 简洁明了 | 完整正式 | 友好+主题 | 正式+尊重 |
| **回复时效期望** | 24-48h 正常 | 当天/次日 | 工作日 24h | 24-72h 正常 | 3-7 天正常 |

---

## 四、三大通用沟通策略（所有文化适用）

### 策略 A：Soft Wording（委婉措辞）

**核心**：永远用"观察"替代"指控"

| ❌ Aggressive（攻击性） | ✅ Soft（委婉） |
|----------------------|---------------|
| issue / problem | feedback / update / observation |
| wrong data | data difference / mismatch |
| error | small discrepancy |
| settlement problem | validation update |
| you made a mistake | let me double check internally too |
| this is incorrect | there may be a difference on our side |
| fix it immediately | could you take a look when you have a moment |

### 策略 B：Validation Framing（确认式框架）

**核心**：把"要求对方做事"包装成"双方共同确认"

```
❌ "请重新提交正确的数据。"
✅ "我想确认一下我们两边的数据是否一致，
   能否帮忙看一下你那边的情况？"
   
   区别：
   - 前者 = 你错了，你来改
   - 后者 = 我们一起确认，共同找答案
```

### 策略 C：Internal Coordination（内部协调定位）

**核心**：把压力转给"第三方"，保全面子

```
❌ "我要求你在周五前提供数据。"
✅ "财务团队这边需要在周五前关闭账期，
   能否帮忙协调一下？"
   
   魔力效果：
   - 巴西方感受：他在帮我解决内部问题，不是在命令我
   - 欧洲方感受：这是合理的流程需求
   - 东南亚方感受：他给我面子了，我帮他
   - 中东方感受：他是我的朋友，在为我考虑
```

---

## 五、高频场景 — 分文化完整话术模板

### 场景 1：Validation / 数据核对

#### 🇧🇷 给巴西渠道：
```
Hey bro, I was reviewing the validation data and noticed a 
small difference on my side 🤔

Could you double check when you have a moment? 
No rush at all, just want to make sure we're aligned 
before I close the internal report 🙌
```

#### 🇪🇺 给欧洲广告主：
```
Hi [Name],

I hope this email finds you well.

During our routine data validation, we noticed a minor 
discrepancy in the attached report (line items highlighted).

Could you kindly review these entries at your earliest 
convenience? We would like to reconcile the figures 
before the next billing cycle.

Please let me know if you need any additional information 
from our side.

Best regards,
[Your Name]
```

#### 🇨🇳 给中国广告主：
```
Hi [Name],

附件是本月的数据核对报告，有几处差异标红了：

1. 渠道 A：我方 1,200 vs 你方 980（差 220）
2. 渠道 B：日期范围不一致（3/1-3/31 vs 3/5-3/28）

麻烦确认一下，今天能反馈吗？谢谢。

Best,
[Your Name]
```

#### 🌏 给东南亚 Partner：
```
Hi [Name]! Hope you're doing great! 😊

Quick sharing — I was looking at the validation data and 
found some small differences. Maybe we can check together?

No rush brother, just want to make sure same page! 🙏

Take care!
[Your Name]
```

#### 🇸🇦 给中东 Partner：
```
Dear Mr. [Name],

I hope this message finds you and your family in good health.

I was reviewing our shared data and noticed a few items that 
may benefit from our joint review. Perhaps we can look into 
these together at your convenience?

I value our partnership greatly and want to ensure complete 
alignment between us.

With respect and best wishes,
[Your Name]
```

---

### 场景 2：Push 追进（三次递进）

#### 🇧🇷 巴西版（渐进式 Chill Push）：
```
Day1:
Hey bro just checking 👀 — any update on the validation? 
No rush, just curious if you've had a chance to look at it.

Day2:
Hey, any update when you have a chance? 🙏
Would love to close this out on my side if possible.

Day3:
Need this to close internal validation, could you help me out? 🙏
I really appreciate it bro!
```

#### 🇪🇺 欧洲版（Professional Follow-up）：
```
Day1:
Dear [Name],
Gentle reminder regarding the pending validation data.
Please let us know if you need any clarification.

Day2:
Dear [Name],
Following up on our previous email regarding the validation.
We would appreciate an update by [day] if possible.

Day3:
Dear [Name],
Urgent: The billing cycle deadline is approaching.
We need the validated data by [date/time] to avoid delays.
Your prompt attention would be greatly appreciated.
```

#### 🇨🇳 中国版（高效直球）：
```
Day1:
[Name]，数据核对那边有进展吗？辛苦尽快反馈。

Day2:
[Name]，这个比较急，今天下班前能给到吗？影响结算。

Day3:
[Name]，必须在今天下午X点前给到，否则这批结算要顺延。
谢谢配合。
```

#### 🌏 东南亚版（Warm but Persistent）：
```
Day1:
Hi [Name]! Quick check-in! Any update brother? 💪

Day2:
[Name]! Following up when free 😊 
Hope everything good your side!

Day3:
Brother [Name] really need your help here! 🙏💪
Appreciate so much!
```

#### 🇸🇦 中东版（Patient Trust-based）：
```
Day1:
My dear friend [Name], a gentle check-in whenever suitable for you 🤝

Day2:
[Name], hoping all is well. Whenever you have a moment, 
I would value your input on this matter.

Day3:
My respected friend [Name], I find myself in a position 
where I urgently need your support. Your help would mean 
a great deal to me and our continued partnership 🤝
```

---

### 场景 3：对方出错，需要纠正

#### 🇧🇷 巴西：
```
I think there may be a difference on our side — 
let me double check internally too.
Maybe I missed something on my end 🤔
Could you send me a screenshot of what you're seeing?
```

#### 🇪🇺 欧洲：
```
We have identified a potential inconsistency in the data provided.
Our team is also conducting an internal review simultaneously.
Could you please verify the figures on your end?
```

#### 🇨🇳 中国：
```
这边数据有些出入，我们也在自查。
麻烦你那边也核对一下具体数字。
```

#### 🌏 东南亚：
```
Brother maybe small mix-up here 😊 
Let me check my side too! Can share screenshot? 
We solve together! 🤝
```

#### 🇸🇦 中东：
```
My friend, there appears to be a matter that would benefit 
from our mutual review. I am certain we can resolve this 
together as we always do.
```

---

### 场景 4：结算 / 付款沟通

**⚠️ 用词选择直接影响合作关系！**

| 用词 | 🇧🇷 巴西感受 | 🇪🇺 欧洲感受 | 🇨🇳 中国感受 | 🌏 东南亚感受 | 🇸🇦 中东感受 |
|------|------------|------------|------------|-------------|------------|
| **settlement** | ❌ 财务压力 | ✅ 正常 | ✅ 正常 | ⚠️ 有点冷 | ⚠️ 太正式 |
| **validation** | ✅ 轻松协作 | ✅ 专业 | ✅ 可用 | ✅ 友好 | ✅ 得体 |
| **reconciliation** | ✅ 中性 | ✅ 最佳 | ⚠️ 太长 | ⚠️ 太正式 | ✅ 好 |
| **review** | ✅ 最轻松 | ✅ 可用 | ✅ 常用 | ✅ 最自然 | ✅ 舒适 |

**AI 自动选择规则**：
- 对巴西渠道 → 优先用 **validation / review**
- 对欧洲广告主 → 优先用 **reconciliation / settlement**
- 对中国广告主 → 优先用 **核对 / 结算**
- 对东南亚 Partner → 优先用 **review / check**
- 对中东 Partner → 优先用 **reconciliation / review**

---

### 场景 5：好消息（提高 CAP / 新 Offer / 预算增加）

#### 🇧🇷 巴西（兴奋但不夸张）：
```
!!! BRO GOOD NEWS !!! 🎉

Hey! I talked to the team and we managed to get your CAP 
increased for [Offer]!! 

New CAP: [数量] — starting [日期]!!

Let's kill it this month! 🚀🔥
```

#### 🇪🇺 欧洲（专业且克制）：
```
Dear [Name],

I am pleased to inform you that following our recent 
performance review, we have approved a CAP increase for 
your account:

- Offer: [名称]
- New CAP: [数量]
- Effective date: [日期]

We look forward to continued success together.

Best regards,
```

#### 🇨🇳 中国（简洁有力）：
```
[Name]，好消息！

[Offer] 的 CAP 从 [旧] 提升到 [新]，[日期] 生效。
继续加油！

Best,
[Your Name]
```

#### 🌏 东南亚（热情洋溢）：
```
[Name]!!!! GOOD NEWS BROTHER!!!! 🎉🎉🎉

CAP INCREASED!!!! 🚀🚀🚀

[Offer] new CAP [数量]!! Starting [日期]!!
Let's make it happen brother! 💪🙏😊
```

#### 🇸🇦 中东（尊重+喜悦）：
```
My dear friend [Name],

It brings me great pleasure to share wonderful news with you.

After careful consideration, we are honored to increase 
your CAP for [Offer] to [数量], effective [日期].

This reflects our deep trust in your partnership.

With gratitude and respect,
[Your Name]
```

---

## 六、AI 引擎工作流

### 自动化流程

```
用户输入
  ↓
"帮我写封邮件给 [对象] 关于 [事项]"
  ↓
┌─────────────────────────────┐
│  Step 1: 文化识别            │
│  - 从上下文提取目标文化       │
│  - 或主动询问："发给谁？"     │
├─────────────────────────────┤
│  Step 2: 场景分类            │
│  - 催数据 / 好消息 / 坏消息   │
│  - Push / 协商 / 确认        │
├─────────────────────────────┤
│  Step 3: 加载文化配置        │
│  - 语气 / 措辞 / Emoji策略   │
│  - 压力等级 / 节奏控制       │
│  - 用词偏好表                │
├─────────────────────────────┤
│  Step 4: 生成草稿            │
│  - Subject + Body + Sign-off │
│  - 自动适配目标文化           │
├─────────────────────────────┤
│  Step 5: 提供"为什么这样写"   │
│  - 解释文化背景              │
│  - 替代方案（更正式/更轻松）  │
└─────────────────────────────┘
  ↓
输出：完整邮件 + 文化注释
```

### 示例交互

> **用户**：帮我写封邮件催巴西渠道 Hertzmobi 要上个月的 validation 数据
>
> **AI**：
> ```
> 📧 已识别：🇧🇷 巴西渠道 + 场景=催数据（第1次push）
> 
> Subject: March validation — quick sync 👀
> 
> Hey [Name],
> 
> Hope you're having a good week! 🙌
> 
> Just checking in on the March validation data — any update 
> when you have a chance? No rush at all, just want to close 
> this out on my side.
> 
> Appreciate it as always bro! Let me know if you need anything 
> from me 👀
> 
> Cheers,
> [Your Name]
> 
> ─── 文化注释 ───
> • 用 "quick sync" 而非 "validation request" — 降低正式感
> • "No rush at all" — 巴西渠道对催促敏感，必须降低防御
> • emoji 🙌👀 — 巴西商务 IM 中大量使用，显得自然亲切
> • "on my side" — 把需求定位为"我这边要关闭"，而非"你还没给"
> • 如果48h无回复，可升级为第2次push（gentle reminder模式）
> ```

---

## 七、高级功能

### 功能 1：同一件事 → 多文化版本一键生成

> **用户**：本月 NXXX Campaign 数据不好，需要通知三个广告主（巴西/欧洲/中国），分别写
>
> **AI**：一次性输出三封完全不同风格的邮件

这对**同时服务多类广告主的 AM** 是杀手级功能——人类需要在不同文化思维间来回切换，AI 天然并行。

### 功能 2：风险预警

当检测到用户意图的表达可能冒犯目标文化时，自动警告：

```
⚠️ 检测到：您使用了 "settlement" 一词
   目标文化：🇧🇷 巴西渠道
   建议：改为 "validation" 或 "review"
   原因：巴西 affiliate 行业中 settlement 有较强财务压迫感
   
⚠️ 检测到：您的语气过于直接
   目标文化：🌏 东南亚 Partner  
   建议：增加 warm-up 开场和 face-saving 表达
   原因：东南亚文化高度重视面子，直接指出问题可能导致合作降温
```

### 功能 3：历史学习

记录每次沟通的反馈（对方回复速度、语气变化、最终结果），持续优化话术：

```
[学习日志示例]
2026-03-15 → 发给 Hertzmobi（🇧🇷）→ 使用 soft wording v1
             → 对方 4h 内回复，态度积极 ✅
2026-03-20 → 发给 Hertzmobi（🇧🇷）→ 使用同样策略
             → 对方 2h 内回复 ✅
2026-04-01 → 发给 Adplex（🇪🇺）→ 误用了巴西 casual 风格
             → 对方 3天才回复，语气冷淡 ⚠️
             → [修正]：欧洲广告主需使用 formal 风格
```

---

## 八、长期价值 — 为什么这是核心竞争力？

### 网盟行业的本质

```
Affiliate Network 的利润公式：

利润 = ∑(每个渠道的流量质量 × 合作深度 × 合作时长)

其中：
- 流量质量 = 数据/技术层面（PA归因、反作弊）→ 其他 Skill 覆盖
- 合作深度 = 这个渠道愿意给你多少好流量 → 取决于"跟你合作舒不舒服"
- 合作时长 = 渠道留多久不跑 → 取决于沟通体验

→ 沟通技能直接影响 2/3 的利润因子！
```

### 竞争壁垒

| 壁垒类型 | 说明 |
|---------|------|
| **经验壁垒** | 这些话术来自真实业务踩坑，不是教科书 |
| **规模壁垒** | 1 个人最多熟练掌握 1-2 种文化；AI 可以同时覆盖 5 种 |
| **一致性壁垒** | 人类会累/情绪差/状态不好；AI 每次都稳定输出 |
| **迭代壁垒** | 每次沟通反馈都可以回流优化话术库 |

### 这不是"翻译工具"

> Google Translate 解决的是"语言不通"的问题。
> 
> 本 Skill 解决的是"**文化不通**"的问题 —— 即使大家都说英语，
> 🇧🇷 巴西人说英语的方式和 🇪🇺 欧洲人完全不同，
> 和 🇨🇳 中国人用英语写商务邮件又不一样。
> 
> **语言相同 ≠ 沟通相同。**

---

## 九、危险信号 — 必须避免的跨文化错误

### 🚨 致命错误 Top 5

| # | 错误 | 目标文化 | 后果 |
|---|------|---------|------|
| 1 | 用 URGENT/!!! 作为 email subject | 🇧🇷 巴西 | 渠道觉得被冒犯，下月减量 |
| 2 | 在群邮件中直接指出对方错误 | 🌏 东南亚 | 对方面子受损，长期冷淡 |
| 3 | 连续3天用同样强硬语气 push | 🇧🇷 巴西 | 直接被 ignore / 拉黑 |
| 4 | 用过于随意的语气对待欧洲广告主 | 🇪🇺 欧洲 | 被认为不专业，暂停合作 |
| 5 | 催促中东 Partner 时表现不耐烦 | 🇸🇦 中东 | 被视为不尊重，信任崩塌 |

### 🚨 常见文化混淆错误

| 混淆 | 错误做法 | 正确做法 |
|------|---------|--------|
| 把巴西 casual 风格用于欧洲 | "Hey bro! 👀" | "Dear [Name]," |
| 把欧洲正式风格用于巴西 | "Please find attached..." | "Quick update bro 🙌" |
| 把中国直球风格用于东南亚 | "数据有问题，请改" | "Maybe small issue, we check together? 😊" |
| 把东南亚过度热情用于欧洲 | "GOOD NEWS!!!! 🎉🎉" | "I am pleased to inform you..." |

---

## 十、触发词

- "跨文化沟通"、"cross-cultural communication"、"多文化邮件"
- "帮我写封邮件给 [国家/地区] [对象]"
- "[国家] 沟通技巧"、"怎么跟 [国家] 说"
- "催数据"、"push 渠道"、"validation 话术"
- "settlement 沟通"、"CAP 谈判"、"Offer 协商"
- "同时写给 [A国] 和 [B国]"、"多版本邮件"
- "巴西 / 欧洲 / 中国 / 东南亚 / 中东 沟通"
- "affiliate AM 话术"、"网盟 BD 沟通"

---

*基于 M COMPANY 公司全球网盟业务真实场景沉淀*
*覆盖 🇧🇷巴西 / 🇨🇳中国 / 🇪🇺欧洲 / 🌏东南亚 / 🇸🇦中东 五大文化圈*
*v2.0 — 从"中巴双边"升级为"全球化跨文化沟通引擎"*
```

---

## 文件 7：skills/cross-cultural-negotiation-copilot/scripts/negotiation_copilot.py

```python
#!/usr/bin/env python3
"""
Cross-Cultural Negotiation Copilot - Cultural Communication Draft Generator
Part of affiliate-skills-hackathon2026

This script generates culturally-appropriate communication drafts for affiliate
network partners, adapting tone, formality, and communication style based on
cultural context (e.g., Brazil↔China communication patterns).
"""

import json
from typing import Optional


def generate_email_draft(
    partner_region: str,
    relationship_stage: str,
    topic: str,
    is_inquiry: bool = False,
    is_followup: bool = False,
    is_complaint: bool = False,
    tone: str = "professional"
) -> dict:
    """
    Generate a culturally-adapted email draft for affiliate partner communication.

    Args:
        partner_region: Target region code (BR, CN, MENA, LATAM, etc.)
        relationship_stage: new, developing, established, strategic
        topic: Main topic of communication
        is_inquiry: Whether this is an initial inquiry
        is_followup: Whether this is a follow-up message
        is_complaint: Whether this addresses a concern/complaint
        tone: preferred tone (formal, professional, friendly)

    Returns:
        dict with draft content and cultural adaptation notes
    """
    # Cultural communication patterns by region
    patterns = {
        "BR": {
            "greeting": "Olá {name}, Tudo bem?",
            "opener": "Espero que esta mensagem o encontre bem.",
            "closer": "Qualquer dúvida, estou à disposição!",
            "signoff": "Abraços cordiais,",
            "formality": "moderate",
            "emoji_allowed": True,
            "preferred_channel": "email_with_whatsapp",
            "response_expectation": "24-48h",
        },
        "CN": {
            "greeting": "尊敬的 {name}，您好：",
            "opener": "感谢您一直以来对我们业务的支持与信任。",
            "closer": "如有任何问题，请随时与我联系。",
            "signoff": "此致敬礼，",
            "formality": "high",
            "emoji_allowed": False,
            "preferred_channel": "email",
            "response_expectation": "48-72h",
        },
        "MENA": {
            "greeting": "Dear {name},",
            "opener": "I hope this message finds you well.",
            "closer": "Please do not hesitate to reach out if you have any questions.",
            "signoff": "Best regards,",
            "formality": "moderate_high",
            "emoji_allowed": False,
            "preferred_channel": "email",
            "response_expectation": "24-72h",
        },
        "DEFAULT": {
            "greeting": "Hello {name},",
            "opener": "I hope you are doing well.",
            "closer": "Please let me know if you have any questions.",
            "signoff": "Best,",
            "formality": "moderate",
            "emoji_allowed": True,
            "preferred_channel": "email",
            "response_expectation": "24-48h",
        }
    }

    # Relationship stage modifiers
    stage_modifiers = {
        "new": {
            "intro_phrase": "Thank you for your interest in our affiliate program.",
            "trust_building": "We look forward to building a mutually beneficial partnership.",
        },
        "developing": {
            "intro_phrase": "Thank you for your continued collaboration.",
            "trust_building": "We value the growing partnership between our teams.",
        },
        "established": {
            "intro_phrase": "As our valued partner,",
            "trust_building": "We appreciate your dedication to our joint success.",
        },
        "strategic": {
            "intro_phrase": "As we continue to strengthen our strategic alliance,",
            "trust_building": "We are committed to supporting your growth as a key partner.",
        }
    }

    # Get cultural pattern
    region_key = partner_region.upper() if partner_region.upper() in patterns else "DEFAULT"
    pattern = patterns[region_key]
    stage = stage_modifiers.get(relationship_stage, stage_modifiers["established"])

    # Build email sections
    greeting = pattern["greeting"]
    opener = pattern["opener"]
    intro = stage["intro_phrase"]

    # Topic-specific body generation
    if is_inquiry:
        body = f"""
Regarding {topic}, we would like to discuss the following points:

1. Current performance metrics and optimization opportunities
2. Budget allocation for the upcoming quarter
3. New campaign proposals and creative assets

{stage["trust_building"]}
"""
    elif is_followup:
        body = f"""
Following up on our previous discussion regarding {topic}:

• Action items from our last conversation
• Progress updates and next steps
• Timeline confirmation

{stage["trust_building"]}
"""
    elif is_complaint:
        body = f"""
We would like to address some concerns regarding {topic}:

• Specific issues that have been identified
• Impact on our partnership metrics
• Proposed solutions and mutual expectations

We believe addressing these points will strengthen our collaboration.
"""
    else:
        body = f"""
Regarding {topic}, I wanted to reach out to share some important updates:

• Key developments affecting our partnership
• New opportunities for growth
• Resources available to support your efforts

{stage["trust_building"]}
"""

    closer = pattern["closer"]
    signoff = pattern["signoff"]

    # Assemble full draft
    draft = f"""{greeting}

{opener}
{intro}
{body}
{closer}

{signoff}
[Your Name]
[Your Title]
[Company Name]"""

    return {
        "draft": draft,
        "cultural_notes": {
            "region": partner_region,
            "formality_level": pattern["formality"],
            "emoji_usage": pattern["emoji_allowed"],
            "preferred_channel": pattern["preferred_channel"],
            "response_expectation": pattern["response_expectation"],
            "tone_adjustments": [
                f"Use {pattern['formality']} formality level",
                f"{'Emojis are culturally appropriate' if pattern['emoji_allowed'] else 'Avoid emojis for this region'}",
                f"Expect response within {pattern['response_expectation']}",
            ]
        },
        "relationship_stage": relationship_stage,
        "topic": topic,
    }


def adapt_tone(draft: str, target_tone: str) -> str:
    """Adapt the tone of an existing draft."""
    tone_adjustments = {
        "formal": "Please adjust all language to use formal business terminology, avoid contractions, and maintain professional distance.",
        "professional": "Use standard professional language while maintaining approachability.",
        "friendly": "Incorporate warmer language, consider brief personal acknowledgments, and maintain enthusiasm.",
    }
    return draft + f"\n\n[Tone Adaptation Note: {tone_adjustments.get(target_tone, tone_adjustments['professional'])}]"


def generate_negotiation_talking_points(
    partner_region: str,
    topic: str,
    leverage_points: list[str]
) -> dict:
    """Generate culturally-aware negotiation talking points."""
    negotiation_styles = {
        "BR": {
            "approach": "relationship_first",
            "patience_level": "high",
            "directness": "moderate",
            "negotiation_tip": "Build rapport before discussing terms. Personal relationships are valued.",
        },
        "CN": {
            "approach": "mutual_benefit",
            "patience_level": "medium",
            "directness": "indirect",
            "negotiation_tip": "Emphasize long-term mutual benefits. Avoid aggressive tactics.",
        },
        "MENA": {
            "approach": "respect_honor",
            "patience_level": "medium",
            "directness": "moderate_indirect",
            "negotiation_tip": "Show respect for their business wisdom. Avoid public confrontation.",
        },
        "DEFAULT": {
            "approach": "direct_professional",
            "patience_level": "medium",
            "directness": "direct",
            "negotiation_tip": "Clear, professional communication with data-backed arguments.",
        }
    }

    style = negotiation_styles.get(partner_region.upper(), negotiation_styles["DEFAULT"])

    talking_points = []
    for i, point in enumerate(leverage_points, 1):
        talking_points.append({
            "point_number": i,
            "content": point,
            "delivery_note": f"Present {point.lower()} with {'data and examples' if partner_region.upper() in ['CN', 'MENA'] else 'clear metrics'}"
        })

    return {
        "topic": topic,
        "negotiation_approach": style["approach"],
        "cultural_tip": style["negotiation_tip"],
        "patience_recommendation": f"Maintain {style['patience_level']} patience level",
        "directness": style["directness"],
        "talking_points": talking_points,
    }


# CLI interface
if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Cross-Cultural Negotiation Copilot - Generate culturally-appropriate communication drafts"
    )
    parser.add_argument("--region", "-r", default="BR", help="Partner region (BR, CN, MENA, etc.)")
    parser.add_argument("--stage", "-s", default="established",
                        choices=["new", "developing", "established", "strategic"],
                        help="Relationship stage")
    parser.add_argument("--topic", "-t", required=True, help="Main topic of communication")
    parser.add_argument("--type", choices=["inquiry", "followup", "complaint", "update"],
                        default="update", help="Type of communication")
    parser.add_argument("--output", "-o", help="Output file path (JSON)")

    args = parser.parse_args()

    result = generate_email_draft(
        partner_region=args.region,
        relationship_stage=args.stage,
        topic=args.topic,
        is_inquiry=args.type == "inquiry",
        is_followup=args.type == "followup",
        is_complaint=args.type == "complaint",
    )

    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump(result, f, ensure_ascii=False, indent=2)
        print(f"Draft saved to {args.output}")
    else:
        print("=" * 60)
        print("CROSS-CULTURAL NEGOTIATION COPILOT")
        print("=" * 60)
        print(f"\n[Region: {args.region}] [Stage: {args.stage}] [Type: {args.type}]\n")
        print(result["draft"])
        print("\n" + "-" * 60)
        print("CULTURAL ADAPTATION NOTES:")
        for note in result["cultural_notes"]["tone_adjustments"]:
            print(f"  • {note}")
```
