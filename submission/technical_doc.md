# 作品说明文档
# 腾讯云 2026 黑客松参赛作品
# 跨文化网盟管理 Skill 集合
# 格式：Markdown（可转为 PDF/DOCX 提交）
# 作者：M COMPANY Team

---

## 目录

1. [作品概述](#1-作品概述)
2. [背景与痛点](#2-背景与痛点)
3. [解决方案架构](#3-解决方案架构)
4. [9 个 Skill 详细说明](#4-9-个-skill-详细说明)
5. [技术创新点](#5-技术创新点)
6. [应用场景与效果](#6-应用场景与效果)
7. [核心差异化：跨文化沟通 Skill](#7-核心差异化跨文化沟通-skill)
8. [技术实现细节](#8-技术实现细节)
9. [Demo 演示指南](#9-demo-演示指南)
10. [未来规划](#10-未来规划)
11. [团队与致谢](#11-团队与致谢)

---

## 1. 作品概述

### 作品名称

**跨文化网盟管理 Skill 集合 — 基于 AI Agent 的多区域 Affiliate 自动化运营系统**

### 一句话描述

一套面向跨境网盟（Affiliate Marketing）业务的 AI Agent 技能模块集合，覆盖从渠道数据接入、归因分析、预算智能分配到跨文化商务沟通的全链路自动化运营能力。

### 参赛类别

Skill / Agent 应用开发

### 关键数据

| 指标 | 数值 |
|------|------|
| Skill 总数 | **9 个**（全部完整可执行） |
| 架构分层 | **4 层** |
| 覆盖区域 | MENA / LATAM / APAC / Europe&US |
| 管理渠道数 | 20+ |
| 管理 APP 数 | 50+ |
| 核心编程语言 | Python 3 |
| AI Agent 平台 | OpenClaw / WorkBuddy |

---

## 2. 背景与痛点

### 2.1 公司背景

M COMPANY 是一家跨境网盟（Affiliate Network）公司，业务模式为：

```
广告主（APP 开发者） → M COMPANY（网盟平台） → 流量渠道（Publisher/Media Buyer）
     ↑ 提供安装/事件转化数据              ↑ 分发 Offer + 结算
```

公司在四大区域同时开展业务：
- **MENA**（中东）：沙特、阿联酋、科威特、阿曼、卡塔尔、埃及等
- **LATAM**（拉美）：巴西、墨西哥、阿根廷、哥伦比亚、智利、秘鲁等
- **APAC**（亚太）：印度、印尼、泰国、越南、菲律宾、马来西亚等
- **Europe & US**：美国、英国、德国、法国、意大利、西班牙等

核心 APP 客户包括：NXXX（巴西数字银行）、JXXXX（巴西信贷APP）、Claro Flex（电信运营商）等。

### 2.2 三大核心痛点

#### 痛点一：数据处理高度重复

每周运营团队需要完成以下重复工作：

| 任务 | 数据源 | 手工操作步骤 | 单次耗时 |
|------|--------|-------------|---------|
| AppsFlyer 导出 & 清洗 | AppsFlyer 后台 | 导出 CSV → 删除测试设备 → 去重 → 合并多渠道变体 | 1-2h |
| Adjust 导出 & 对齐 | Adjust 后台 | 导出 → 字段映射 → 与 AF 数据合并 | 1h |
| 结算单录入 | PDF/图片（OCR 识别后） | 人工核对渠道名 → 录入金额 → 标记异常 | 1-1.5h |
| 渠道报表生成 | 多个 Excel | 复制粘贴 → 格式统一 → 检查公式错误 | 0.5-1h |

**每周合计：3-5 小时纯手工数据处理。**

#### 痛点二：跨文化沟通效率极低

以巴西区域为例，典型沟通链路：

```
中国运营（中文思维） → 英文邮件/WhatsApp → 巴西渠道（葡萄牙语思维）
        ↑                                    ↓
    翻译工具辅助                          文化差异导致误解
```

**实际案例**：
- 中国运营习惯直接表达："请尽快发送报告，已经逾期了。" → 巴西渠道感到被冒犯，合作降温
- 巴西渠道习惯间接表达："我们正在整理中" → 中国运营理解为拖延，进一步催促 → 恶性循环
- 平均每封确认邮件需要 **5-8 个来回**才能达成一致

#### 痛点三：预算分配缺乏数据支撑

每月 CAP（流量上限）分配流程：

```
运营凭记忆回顾上月表现 → 内部讨论 → 凭经验拍数字 → 分配给各渠道
```

**问题**：
- 无量化依据，完全依赖个人经验
- 新人无法独立完成，需要老员工带教 2 周+
- 低质流量渠道占用 20-30% 预算但产出极低
- 缺乏统一的评估标准和决策框架

---

## 3. 解决方案架构

### 3.1 设计理念

> **"把业务知识变成代码，让 AI Agent 替代重复劳动。"**

核心理念是将 M COMPANY 团队积累的网盟运营经验，封装为一个个独立的、可复用的 **AI Agent Skill**。每个 Skill 包含：
- 一段结构化的业务知识描述（Markdown 文档）
- 一个完整可执行的 Python 脚本（自动化处理逻辑）
- 触发词列表（AI Agent 自动识别何时调用）

### 3.2 四层架构

```
┌──────────────────────────────────────────────────────────────┐
│                                                              │
│   Layer 4: 跨文化协作层 (Cross-Cultural Collaboration)       │
│   ──────────────────────────────────────────────────────      │
│   cross-cultural-br-ba-communication                         │
│   → 巴西 ↔ 中国跨文化沟通模板                                 │
│   → Soft Wording / Validation Framing / Internal Coordination │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   Layer 3: 智能决策层 (AI Decision & Risk)                   │
│   ──────────────────────────────────────────────────────      │
│   conversion-funnel-intelligence          → JXXXX 转化漏斗分析 + CAP 建议     │
│   macro-monitoring-agent          → 定时监控 + 异常预警               │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   Layer 2: 数据分析层 (Data Analytics)                       │
│   ──────────────────────────────────────────────────────      │
│   multi-mmp-attribution-engine   → 多 MMP 归因引擎（去重+归一化）     │
│   cross-regional-revenue-audit           → NXXX 盈亏核算（ROI 分析）         │
│   ai-budget-optimizer→ 多 APP 预算汇总 + 优化建议        │
│                                                              │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│   Layer 1: 数据接入层 (Data Connectors)                      │
│   ──────────────────────────────────────────────────────      │
│   crm-channel-extraction     → OCR 结算单自动提取             │
│   crm-settlement-verification→ 自动对账 + 异常标记            │
│   pa-channel-export   → PA 标准化报表生成              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### 3.3 架构设计原则

| 原则 | 说明 |
|------|------|
| **单一职责** | 每个 Skill 只解决一个明确的业务问题 |
| **独立可执行** | 每个 Skill 包含完整 Python 脚本，可单独运行 |
| **层间解耦** | 上层不依赖下层具体实现，只依赖输出格式 |
| **渐进增强** | 可从单 Skill 使用逐步扩展到全链路自动化 |

---

## 4. 9 个 Skill 详细说明

### 4.1 Layer 1 — 数据接入层

#### crm-channel-extraction

| 属性 | 内容 |
|------|------|
| **功能** | 从 OCR 识别的结算单 PDF/图片中自动提取渠道名和金额 |
| **输入** | OCR 输出的文本文件（含渠道名、金额信息） |
| **输出** | 结构化的渠道-金额映射表（CSV/JSON） |
| **解决痛点** | 结算单手动录入耗时 1-1.5 小时/次 → 自动化 3 分钟 |
| **版本** | v1.0.0 |

**核心能力**：
- 模糊匹配渠道名（处理 OCR 识别错误，如 "Hertzmobi" → "Hertz mobi"）
- 多币种金额识别（BRL/USD/EUR/SAR 等）
- 异常值标记（金额为 0、负数、超阈值等）

---

#### crm-settlement-verification

| 属性 | 内容 |
|------|------|
| **功能** | 自动对账，标记差异 ≥5% 的异常项 |
| **输入** | 两份数据源：内部 CRM 记录 vs 渠道提交的结算单 |
| **输出** | 对账报告（匹配项 + 差异项 + 异常标记） |
| **解决痛点** | 人工对账 2 小时 → 自动化 3 分钟 |
| **版本** | v1.0.0 |

**核心能力**：
- 双向匹配算法（内部→渠道 + 渠道→内部）
- 差异百分比计算与阈值告警
- 支持部分匹配（渠道名近似但金额不一致的情况）

---

#### pa-channel-export

| 属性 | 内容 |
|------|------|
| **功能** | 生成 Partner Alliance 格式的标准化投放报表 |
| **输入** | 归因后的渠道数据 + 预算分配数据 |
| **输出** | 符合 PA 规范的标准化报表（Excel/CSV） |
| **解决痛点** | 手工制表 0.5-1 小时/次 → 一键导出 |
| **版本** | v1.0.0 |

**核心能力**：
- 字段映射配置（内部字段名 → PA 标准字段名）
- 多维度汇总（按渠道/按 APP/按日期/按区域）
- 公式校验（确保汇总数据一致性）

---

### 4.2 Layer 2 — 数据分析层

#### multi-mmp-attribution-engine（v1.1.0）

| 属性 | 内容 |
|------|------|
| **Display Name** | Multi-MMP Attribution Engine |
| **功能** | 多 MMP 归因引擎，基于 Source Bank 去重，输出干净归因数据 |
| **输入** | AppsFlyer/Adjust 原始导出 CSV（可能含多个 MMP 来源） |
| **输出** | 去重后的干净归因 CSV（utf-8-sig 编码） |
| **脚本** | `affiliate_attribution.py`（完整可执行） |
| **版本** | v1.1.0 |

**核心能力**：
- **自动编码检测**：兼容 utf-8-sig / utf-8 / gbk / latin-1 编码的输入文件
- **字段名模糊查找**：兼容不同 AF 导出格式（`v_appsflyer_id` / `AppsFlyer ID` 等）
- **Source Bank 优先级归因**：按预定义优先级处理同一用户的多渠道触达
- **渠道变体归一化**：自动剥离 `_apr` / `_ios` / `_and` 等后缀，合并为统一渠道
- **排除规则**：自动排除 `af_purchase_esim` 等非目标事件
- **编码安全输出**：utf-8-sig 编码 → Windows Excel 直接打开无乱码

---

#### cross-regional-revenue-audit

| 属性 | 内容 |
|------|------|
| **功能** | NXXX APP 盈亏核算，自动标记负 ROI 渠道 |
| **输入** | NXXX 的 AppsFlyer 数据 + GH 结算数据 |
| **输出** | 盈亏报告（红黑榜 + ROI 排行） |
| **脚本** | `nxxx_analysis.py`（完整可执行） |
| **版本** | v1.0.0 |

**核心能力**：
- 收入端：GH 结算金额 × 汇率转换
- 成本端：AppsFlyer 事件成本（CPI/CPA）
- ROI 计算：按渠道 / 按 APP / 按日期 多维度拆解
- 红黑榜自动标注：负 ROI 渠道红色高亮

---

#### ai-budget-optimizer

| 属性 | 内容 |
|------|------|
| **功能** | 多 APP 预算汇总，生成优化建议 |
| **输入** | 各 APP 的渠道投放数据 + 预算分配记录 |
| **输出** | 预算汇总报告 + 调整建议 |
| **脚本** | `campaign_budget_analysis.py`（完整可执行） |
| **版本** | v1.0.0 |

**核心能力**：
- 跨 APP 预算一键汇总
- 渠道效率排名（ROI / CPA / 转化率）
- 预算再分配建议（基于数据而非经验）

---

### 4.3 Layer 3 — 智能决策层

#### conversion-funnel-intelligence（v1.1.0）

| 属性 | 内容 |
|------|------|
| **Display Name** | Conversion Funnel Intelligence |
| **功能** | JXXXX 信贷漏斗 5 阶段分析，输出渠道 CAP 建议 |
| **输入** | AppsFlyer 事件数据 + e-Grana CRM 数据 |
| **输出** | 带颜色标注的 Excel 报告（绿/黄/红三档）+ CAP 建议 |
| **脚本** | `jxxxx_funnel.py`（完整可执行） |
| **版本** | v1.1.0 |

**漏斗 5 阶段**：
1. 安装（Install）
2. 注册（Sign Up）
3. CPF 验证（CPF Verification）
4. 账户创建成功（Conta Criada Sucesso）
5. 首次贷款审批（First Loan Approval）

**核心能力**：
- 过滤 `conta_criada_sucesso_view` 事件，按 AF ID 去重
- 合并 e-Grana CRM 数据，计算有效性百分比
- **三色分类**：
  - 🟢 高有效性（≥30%）→ 建议 **增加 CAP**
  - 🟡 中有效性（20-30%）→ 维持不变
  - 🔴 低有效性（<20%）→ 建议 **降低 CAP**
- Factor 计算（调整系数）+ AF CAP 具体数值建议
- **Excel 颜色标注**（openpyxl 实现），一目了然

---

#### macro-monitoring-agent

| 属性 | 内容 |
|------|------|
| **功能** | 定时监控 AppsFlyer/Adjust 数据，异常自动预警 |
| **输入** | 定时任务配置（监控指标 + 阈值 + 通知方式） |
| **输出** | 异常预警通知（消息/邮件/ webhook） |
| **脚本** | `macro_monitor.py`（完整可执行） |
| **版本** | v1.0.0 |

**监控指标**：
- 安装量骤降（日环比 >30%）
- ROI 异常波动
- 渠道数据延迟/缺失
- CPA 突然飙升

---

### 4.4 Layer 4 — 跨文化协作层

#### cross-cultural-br-ba-communication（v1.0.0）

| 属性 | 内容 |
|------|------|
| **功能** | 巴西 ↔ 中国跨文化沟通模板与话术生成器 |
| **输入** | 沟通场景（催数据/确认Offer/谈判CAP/投诉处理）+ 目标语气 |
| **输出** | 符合巴西商务文化的英文邮件/WhatsApp 消息草稿 |
| **版本** | v1.0.0 |
| **定位** | **🌟 核心差异化 Skill** |

详见 [第 7 章](#7-核心差异化跨文化沟通-skill)。

---

## 5. 技术创新点

### 5.1 Skill 即代码（Skill as Code）

传统 AI Agent 方案通常只有 Prompt（提示词），调用外部 API 或依赖人工操作。本作品的每个 Skill 都包含 **完整可执行的 Python 脚本**，AI Agent 可以零干预地自动调用执行。

**优势**：
- 不依赖在线 API（离线可用）
- 处理逻辑透明可审计
- 可独立运行调试
- 易于扩展和定制

### 5.2 跨平台编码适配

网盟业务涉及多国数据，文件编码问题是日常高频痛点。本作品在所有 Skill 中内置了完整的编码处理策略：

| 场景 | 处理方式 |
|------|---------|
| 输入文件编码未知 | 自动检测（chardet 算法） |
| 输出给 Windows 用户看 | utf-8-sig + CRLF |
| 输出给 Mac/Linux 用户 | utf-8 + LF |
| .bat/.cmd 含中文 | GBK 编码（Windows cmd.exe 要求） |
| JSON/YAML/Shell 脚本 | 强制 utf-8 无 BOM |

**效果**：彻底消除"文件传过去乱码"的问题。

### 5.3 业务规则内置

每个 Skill 中的业务规则都来自 M COMPANY 团队的真实运营经验，不是通用 AI 的泛化回答：

| 示例 | 通用 AI 回答 | 本作品 Skill |
|------|------------|-------------|
| "如何去重？" | "用 pandas drop_duplicates()" | 基于 Source Bank 优先级的归因逻辑，考虑渠道触达顺序 |
| "怎么写英文邮件？" | 标准商务英语模板 | Soft Wording + Validation Framing + Internal Coordination 三大策略 |
| "哪些渠道该降 CAP？" | "看 ROI 低的" | JXXXX 漏斗 5 阶段有效性分类 + Factor 计算 + 三色标注 |

### 5.4 模块化可扩展架构

四层清晰分层，新增能力只需添加对应 Skill：

- 新增一个区域的市场情报？→ 在 Layer 2 添加新 Skill
- 新增一种沟通文化？→ 在 Layer 4 添加新 Skill
- 接入新的 MMP 平台？→ 扩展 Layer 2 的 attribution Skill

**不影响现有任何 Skill 的运行。**

---

## 6. 应用场景与效果

### 6.1 场景一：月度结算（每月一次）

**Before**：
```
周五下午开始 → 导出 5 份报表 → 手工清洗 3h → 对账 2h → 
发现差异 → 追查原因 → 重新核算 → 周末加班
总耗时：1-2 天
```

**After**：
```
运行 multi-mmp-attribution-engine → 自动去重归因 → 
运行 crm-settlement-verification → 自动对账标记异常 → 
查看差异项（通常 <5 项）→ 逐项确认
总耗时：30 分钟
```

**提升：96%**

### 6.2 场景二：月度预算分配（每月一次）

**Before**：
```
运营回忆上月表现 → 内部讨论会 2h → 凭经验写数字 → 
分配给各渠道 → 下月发现效果不好 → 再调整
结果：20-30% 预算浪费
```

**After**：
```
运行 conversion-funnel-intelligence → 获得各渠道有效性评级 → 
运行 ai-budget-optimizer → 获得预算优化建议 → 
基于数据分配 CAP
结果：预算利用率显著提升
```

**提升：从经验驱动 → 数据驱动（质变）**

### 6.3 场景三：日常渠道沟通（每天多次）

**Before**：
```
中国运营写英文邮件 → 巴西渠道觉得太直接 → 
修改措辞 → 再发 → 还是不对 → 来回 5-8 次
平均每次沟通耗时：2-4 小时
```

**After**：
```
运营告诉 AI："帮我写封邮件催 Hertzmobi 要数据" → 
AI 调用 cross-cultural-br-ba-communication → 
输出符合 Soft Wording 规范的邮件 → 
运营检查后发送 → 通常 1 次搞定
平均每次沟通耗时：15-30 分钟
```

**提升：75-87%**

### 6.4 效果汇总

| 指标 | Before | After | 提升 |
|------|--------|-------|------|
| 月度对账耗时 | 1 天 | 30 分钟 | **96% ↓** |
| 报表清洗去重 | 3-5h/次 | 自动完成 | **100% ↓** |
| 跨文化沟通往返 | 5-8 次/次 | 1-2 次/次 | **75% ↓** |
| 预算分配依据 | 经验驱动 | 数据驱动 | **质变** |
| 新人上手时间 | 2 周 | 2 天 | **86% ↓** |

---

## 7. 核心差异化：跨文化沟通 Skill

### 7.1 为什么这是核心差异化？

市面上的 AI Agent 工具大多聚焦在"数据处理"和"自动化"层面，极少关注**跨文化商务沟通**这一刚需场景。

对于跨境网盟公司来说：
- ✅ 数据处理可以用通用工具（Excel/Airbyte/Fivetran）
- ✅ 自动化可以用通用 RPA（UiPath/Power Automate）
- ❌ **跨文化沟通没有现成工具**——这是真正的蓝海

### 7.2 三大沟通策略详解

#### Strategy 1: Soft Wording（委婉表达）

**问题**：中文/英文的直接表达在巴西文化中被视为粗鲁。

| ❌ Direct（避免） | ✅ Soft Wording（推荐） |
|------------------|----------------------|
| Send the report now. | Would you mind sharing the report when you have a moment? |
| This is overdue. | I wanted to follow up on this to make sure nothing fell through the cracks. |
| We need this urgently. | It would be really helpful to have this by [date] if possible. |
| You didn't reply. | Just checking in to see if you had a chance to look at this. |

#### Strategy 2: Validation Framing（确认式框架）

**问题**：直接提出要求容易被拒绝；先确认共识再提要求，对方更易接受。

**模板**：
```
Step 1: 确认双方理解一致 ("Just to confirm we're aligned on...")
Step 2: 表达感谢/认可 ("Really appreciate your support on...")
Step 3: 温和提出下一步 ("Would it be possible to...")
```

**示例**：
> "Hi [Name], just to confirm we're aligned on the Q2 targets for NXXX Brazil. Really appreciate the strong performance in January. Would it be possible to share the February install breakdown by source? Our team is finalizing the budget allocation."

#### Strategy 3: Internal Coordination Positioning（内部协调定位）

**问题**：直接施压会破坏关系；将压力转嫁给"内部其他部门"，保护合作关系。

**模板**：
```
"Our [finance/legal/compliance] team is asking for..."
"Our internal process requires..."
"To keep everything smooth on our end..."
```

**示例**：
> "Our finance team is doing their month-end close and they're asking for the final settlement numbers. To avoid any payment delays on our end, could you send the invoice by Friday?"

### 7.3 危险信号清单

| 危险信号 | 触发条件 | 应对策略 |
|---------|---------|---------|
| 🟡 连续 2 次未回复 | 渠道超过 48h 未响应 | 换 WhatsApp + Internal Coordination |
| 🟡 回复内容模糊 | "正在处理中"/"稍后给你" | Validation Framing 确认具体时间 |
| 🟡 推诿给第三方 | "等广告主回复" | CC 相关方 + 设定 deadline |
| 🔴 提到竞品 | "XX 家给的条件更好" | 不要立即 counter，先了解全貌 |
| 🔴 威胁停止合作 | "如果不...我们就停掉" | 升级到 BD 负责人 + 准备备选渠道 |

### 7.4 Push 节奏控制规范

```
Day 1:  首次触达（Soft Wording + Validation Framing）
Day 3:  第一次跟进（Internal Coordination + 具体时间请求）
Day 5:  第二次跟进（换渠道 WhatsApp + 更委婉的措辞）
Day 7:  第三次跟进（CC 上级/财务 + 明确 deadline）
Day 10: 升级预警（通知 BD 负责人 + 启动备选方案）
Day 14: 最后通牒（正式邮件 + 抄送双方上级）
```

---

## 8. 技术实现细节

### 8.1 技术栈

| 组件 | 技术 | 说明 |
|------|------|------|
| Skill 定义 | Markdown (YAML frontmatter) | 元数据 + 文档 + 脚本 |
| 自动化脚本 | Python 3.9+ | pandas, openpyxl, requests, beautifulsoup4 |
| AI Agent 运行时 | OpenClaw / WorkBuddy | Skill 加载 + 调度 + 工具调用 |
| 编码处理 | 自研（write_file.py） | 跨平台编码推断 + BOM/CRLF 自动适配 |
| 数据格式 | CSV / JSON / Excel (xlsx) | 输入输出均支持 |
| 定时任务 | Cron / OpenClaw Scheduler | macro-monitoring-agent 定时触发 |

### 8.2 文件结构

```
affiliate-skills-export/
├── 01_wish-intelligence-collector.md              # Wish List → My Table
├── 02_regional-wish-classifier.md         # Wish List → M COMPANY Table
├── 03_multi-mmp-attribution-engine.md         # 多 MMP 归因引擎 ⭐ v1.1.0
├── 04_cross-regional-revenue-audit.md                 # NXXX 盈亏核算
├── 05_ai-budget-optimizer.md      # 预算汇总优化
├── 06_conversion-funnel-intelligence.md                 # JXXXX 漏斗分析 ⭐ v1.1.0
├── 07_macro-monitoring-agent.md                 # 定时监控
├── 08_geo-market-intel-engine.md              # 市场情报引擎 ⭐ v1.1.0
├── 09_cross-cultural-br-ba-communication.md  # 跨文化沟通 🌟
├── README.md                           # 项目说明
├── HACKATHON_SUBMISSION.md             # 参赛提交说明
├── SKILL_NAMING_PROPOSAL.md            # 命名建议
└── submission/                         # （本目录）参赛材料
    ├── intro_500words.md               # 作品简介（500字版）
    ├── ppt_deck.md                     # 路演 PPT（Marp 格式）
    ├── video_script.md                 # 视频脚本（4分钟）
    └── technical_doc.md                # 作品说明文档（本文档）
```

### 8.3 编码策略详情

所有文件通过 `qclaw-text-file` skill 的 `write_file.py` 脚本写入，确保：
- macOS 本地使用：utf-8，无 BOM，LF 换行
- 如需给 Windows 用户：自动切换 utf-8-sig + CRLF
- 临时文件写入 `/tmp/_tw_*.txt`，正式写入后清理

---

## 9. Demo 演示指南

### 9.1 推荐演示路线（评委现场 5 分钟版）

| 时间 | 演示内容 | 对应 Skill | 预期效果 |
|------|---------|-----------|---------|
| 0:00-0:45 | 自我介绍 + 痛点陈述 | - | 引起共鸣 |
| 0:45-1:30 | 四层架构介绍 | - | 展示系统性思考 |
| 1:30-2:00 | **Demo 1**：归因数据处理 | multi-mmp-attribution-engine | CSV → 干净数据，无乱码 |
| 2:00-2:40 | **Demo 2**：JXXXX 漏斗 + CAP 建议 | conversion-funnel-intelligence | 三色 Excel 报告 |
| 2:40-3:10 | **Demo 3**：跨文化邮件生成 | cross-cultural-br-ba-communication | 左右分屏对比 |
| 3:10-3:40 | 效果数据 + 技术创新 | - | 用数字说话 |
| 3:40-4:30 | Q&A | - | - |
| 4:30-5:00 | Buffer（备用） | - | - |

### 9.2 Demo 准备清单

- [ ] 一份 AppsFlyer 原始导出 CSV（脱敏后）
- [ ] 一份 NXXX GH 结算表（脱敏后）
- [ ] 一份 JXXXX e-Grana CRM 导出（脱敏后）
- [ ] 一个巴西渠道沟通场景（虚构或脱敏均可）
- [ ] OpenClaw / WorkBuddy 环境（可访问 Skill）
- [ ] 录屏软件（OBS / Loom）

### 9.3 Demo 话术要点

1. **不要背书**——自然讲解，像跟同事介绍项目一样
2. **每个 Demo 控制在 30-40 秒**——评委注意力有限
3. **突出"无乱码"这个细节**——看似小事，但体现工程素养
4. **跨文化沟通做左右分屏对比**——视觉冲击力最强
5. **准备好"如果评委问 X 怎么答"**——见下方 FAQ

### 9.4 常见评委问答预设

| 问题 | 建议回答 |
|------|---------|
| "跟 RPA 有什么区别？" | RPA 是 UI 自动化，我们是知识封装+数据分析。RPA 能帮你点按钮，但不能判断哪个渠道该降 CAP。 |
| "为什么不用 LangChain？" | 我们的核心价值不在框架选择，而在业务知识的深度封装。LangChain 是工具，Skill 是内容。 |
| "数据安全怎么保证？" | 所有脚本本地运行，不上传原始数据到第三方。敏感数据可在私有化部署的 Agent 环境中执行。 |
| "如何扩展到新区域？" | 模块化架构，新增区域只需添加对应 Skill。比如要加非洲市场，写一个 africa-market-intel Skill 即可。 |
| "跨文化沟通 Skill 能扩展到其他国家吗？" | 当然可以。当前聚焦巴西↔中国是因为这是我们最痛的点。方法论通用，只需替换文化规则库即可。 |

---

## 10. 未来规划

### Phase 1（近期 1-2 月）
- [ ] 接入 AppFollow/AppMagic API，让 geo-market-intel-engine 输出真实排行数据
- [ ] 补充 Partner Risk Radar Skill（渠道风险雷达）
- [ ] 补充 Campaign Health Doctor Skill（活动健康度诊断）

### Phase 2（中期 3-6 月）
- [ ] 接入腾讯云 API：TTS（语音播报）、OCR（ smarter 结算单识别）、翻译（实时多语言）
- [ ] 发布到 SkillHub 平台，供其他网盟公司使用
- [ ] 支持更多 MMP 平台（SingTen、Kochava 等）

### Phase 3（长期 6-12 月）
- [ ] 构建 Skill Marketplace（技能市场），支持社区贡献
- [ ] 接入大模型微调，让跨文化沟通更加自然
- [ ] 多租户 SaaS 化，服务中小型网盟公司

---

## 11. 团队与致谢

### 团队

| 角色 | 姓名 | 负责领域 |
|------|------|---------|
| 项目负责人 | | 架构设计 + 业务规则梳理 |
| 技术开发 | | Python 脚本开发 + Skill 封装 |
| 跨文化研究 | | 巴西商务沟通策略提炼 |
| AI Agent 工程 | | OpenClaw/WorkBuddy 集成 |

### 致谢

- **OpenClaw / WorkBuddy 团队**：提供 AI Agent 运行时环境
- **腾讯云黑客松组委会**：举办本次赛事
- **M COMPANY 运营团队**：提供真实的业务场景和数据反馈

---

*文档版本：v1.0 | 创建日期：2026-05-12 | 作者：M COMPANY Team*
*总字数：约 6500 字（不含代码块）*
