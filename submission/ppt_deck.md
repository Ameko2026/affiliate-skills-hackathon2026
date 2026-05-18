# 路演 PPT —— 跨文化网盟管理 Skill 集合
# 腾讯云 2026 黑客松参赛作品
# 格式：Markdown（可转为 PDF/PPTX）
# 演绎者：[Company]
# 总页数：20 页（新增 Layer 5 四页）

---

## Slide 1：封面

# 🌍 跨文化网盟管理 Skill 集合

**基于 AI Agent 的多区域 Affiliate 自动化运营系统**

---

### 团队：[Company]
### 赛道：AI Agent Skill Track
### 日期：2026-05-15

---

---

## Slide 2：目录

# 📋 今天要讲的内容

1. 🎯 我们是谁 & 解决什么问题
2. 🏗️ 五层 Skill 架构
3. 💡 核心创新：Layer 5 — AI 组织行为
4. 🧪 Demo 演示
5. 📊 效果数据
6. ❓ Q&A

---

---

## Slide 3：痛点深挖

# 😤 每天的三大噩梦

| 痛点 | 现状 | 耗时 |
|------|------|------|
| 📊 **数据处理** | 每周 5+ 报表手动清洗、去重、合并 | 3-5 小时/次 |
| 🌍 **跨文化沟通** | 三类广告主 × 三类流量源，邮件来回 | 5-8 次/次 |
| 💰 **预算分配** | 二十多个渠道 CAP 全凭经验拍脑袋 | 浪费 20-30% |

---

> "我们不是在做一个工具，而是在培养一个 AI 商务经理"

---

---

## Slide 4：解决方案总览

# 🎯 14 个 AI Agent Skill × 五层架构

```
         ┌─────────────────────────────────────┐
 Layer 5 │  🧠 AI 组织行为层（新增）             │  ← 核心创新
         │  Partner Memory + Relationship Health │
         ├─────────────────────────────────────┤
 Layer 4 │  🌍 跨文化协作层                      │
         │  巴西/中国/欧洲/东南亚/中东 五大文化圈 │
         ├─────────────────────────────────────┤
 Layer 3 │  🛡️ 反作弊与归因层                   │
         │  PA 报表 + 归因去重 + Fraud Detection│
         ├─────────────────────────────────────┤
 Layer 2 │  📊 数据分析层                        │
         │  预算优化 + 转化漏斗 + 市场情报       │
         ├─────────────────────────────────────┤
 Layer 1 │  🔌 数据接入层                        │
         │  OCR 结算单 + CRM 对账 + PA 导出     │
         └─────────────────────────────────────┘
```

---

---

## Slide 5：Layer 1 — 数据接入层

# 🔌 Layer 1：自动提取 + 自动对账

| Skill | 功能 | 效率提升 |
|-------|------|----------|
| `crm-channel-extraction` | OCR 结算单自动提取渠道数据 | 1h → 3min |
| `crm-settlement-verification` | 内部 CRM vs 渠道对账 | 2h → 3min |
| `pa-channel-export` | PA 标准化报告生成 | 1h → 1min |

---

### 核心能力
- ✅ 自动检测文件编码（中文/葡语/英语）
- ✅ 自动处理 utf-8-sig + CRLF
- ✅ Excel 打开无乱码

---

---

## Slide 6：Layer 2 — 数据分析层

# 📊 Layer 2：智能决策支持

| Skill | 功能 | 输出 |
|-------|------|------|
| `multi-mmp-attribution-engine` | 多 MMP 归因去重 | 纯净归因 CSV |
| `ai-budget-optimizer` | 渠道有效性分析 | CAP 建议 |
| `conversion-funnel-intelligence` | 转化漏斗 5 阶段分析 | 三色报告 |
| `geo-market-intel-engine` | 区域市场情报 | 市场报告 |

---

### 核心能力
- ✅ 基于 Source Bank 优先级的归因规则
- ✅ 三色分级：🟢 ≥30% / 🟡 20-30% / 🔴 <20%
- ✅ 数据驱动 CAP 调整

---

---

## Slide 7：Layer 3 — 反作弊与归因层

# 🛡️ Layer 3：反作弊 + Fraud Detection

| Skill | 功能 | 解决痛点 |
|-------|------|----------|
| `pa-report-workflow` | PA 报告自动化 | 4h → 自动 |
| `affiliate_attribution.py` | 归因去重 | 手动 → 自动 |

---

### 核心能力
- ✅ 排除 af_purchase_esim 等无效事件
- ✅ 渠道变体按前缀归一化（_gdn / _organic 等）
- ✅ Source Bank 优先级自动排序

---

---

## Slide 8：Layer 4 — 跨文化协作层

# 🌍 Layer 4：核心差异化 — 跨文化沟通引擎

### 覆盖五大文化圈
🇧🇷 巴西 | 🇨🇳 中国 | 🇪🇺 欧洲 | 🌏 东南亚 | 🇸🇦 中东

### 三大沟通策略
| 策略 | 适用场景 | 效果 |
|------|----------|------|
| **Soft Wording** | 催数据、问进度 | 避免傲慢感 |
| **Validation Framing** | 确认共识后提要求 | 提高接受率 |
| **Internal Coordination** | 施压但保全面子 | 维护关系 |

---

### 一键生成 5 种文化版本
> "请发送上周数据" → 5 种文化的不同表达方式

---

---

## Slide 9：Layer 5 架构图 — AI Organization Behavior

# 🧠 Layer 5：AI 不再是工具，而是"伙伴"

## 核心问题
❌ 传统 AI Agent：**无状态** —— 不认识人，每次都是陌生人
✅ 进化后 AI：**有记忆** —— 记住合作伙伴，关系可积累

---

```
┌──────────────────────────────────────────────────────────────┐
│                    AI Organization Behavior                  │
│                                                              │
│  ┌─────────────────┐         ┌─────────────────────────┐   │
│  │  🧠 Partner     │         │  💗 Relationship        │   │
│  │     Memory      │ ──────→ │     Health Score        │   │
│  │     System      │         │     (0-100 分)          │   │
│  └─────────────────┘         └─────────────────────────┘   │
│           ↓                            ↓                     │
│  ┌─────────────────┐         ┌─────────────────────────┐   │
│  │ 10 维度记忆      │         │ 三级预警机制            │   │
│  │ • 沟通风格       │         │ 🟢 绿 ≥70 分           │   │
│  │ • 回复速度       │         │ 🟡 黄 50-70 分         │   │
│  │ • 风险历史       │         │ 🔴 红 <50 分           │   │
│  │ • 谈判习惯       │         └─────────────────────────┘   │
│  │ • ...           │                   ↓                   │
│  └─────────────────┘         ┌─────────────────────────┐   │
│                               │ 🤖 AI 主动建议          │   │
│                               │ "建议 24h 内电话沟通"   │   │
│                               └─────────────────────────┘   │
└──────────────────────────────────────────────────────────────┘
```

---

---

## Slide 10：Partner Memory System Demo

# 🧠 Partner Memory System — AI 开始"记人"

## 记忆数据结构（JSON）
```json
{
  "partner_id": "partner_001",
  "name": "Hertzmobi",
  "region": "🇧🇷 巴西",
  "memory": {
    "communication_style": "warm",      // soft/warm/aggressive/formal
    "reply_speed": "fast",              // fast/medium/slow/dead
    "risk_history": "no_issues",        // fraud/payment_delay/no_issues
    "negotiation_habit": "price_pressure", // price_pressure/bonus_hunter/easy
    "category_preference": "finance",   // finance/gaming/utility
    "timezone": "BRT",                 // BRT/EST/CST
    "emotion_style": "optimistic",     // optimistic/pessimistic/dramatic
    "contact_reliability": "always_online", // always_online/intermittent/offline
    "call_preference": "voice_call",   // voice_call/sms_only/async_only
    "budget_cooperation": "high"       // high/medium/low
  },
  "last_updated": "2026-05-15"
}
```

---

## 对比：有无记忆的 AI 回复差异

| 场景 | ❌ 无记忆 AI | ✅ 有记忆 AI |
|------|-------------|-------------|
| 催数据 | "Send the report now." | "Hi [Partner], hope you're having a great week! Would you mind sharing the report when you have a moment? Our team is asking :)" |
| 压价谈判 | 直接报价 | "我记得你上次提到预算压力大，我们看看有没有更好的套餐方案..." |

---

---

## Slide 11：Relationship Health Score Demo

# 💗 Relationship Health Score — AI 评估关系健康度

## 评分维度（总分 0-100）

| 维度 | 权重 | 说明 |
|------|------|------|
| 回复速度 | 20% | 最近 30 天平均回复时间 |
| 情绪稳定性 | 25% | 沟通语气波动分析 |
| 配合度 | 20% | 任务完成率、CAP 调整响应率 |
| 付款及时性 | 15% | 付款延迟次数 |
| 流量稳定性 | 20% | 流量波动幅度 |

---

## 界面展示

```
┌─────────────────────────────────────────────────────────┐
│              Partner Health Dashboard                    │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  Hertzmobi       ████████████████░░░░  85 分  🟢 健康   │
│  ---------------------------------------------           │
│  AppTango        ██████████░░░░░░░░░░░  62 分  🟡 注意  │
│  ---------------------------------------------           │
│  GamePartner     ████░░░░░░░░░░░░░░░░░  35 分  🔴 预警  │
│                                                          │
│  ⚠️ GamePartner 健康度降至 35，建议 24h 内主动沟通     │
└─────────────────────────────────────────────────────────┘
```

---

---

## Slide 12：AI 主动预警 Demo

# 🚨 AI 主动预警 — 被动工具 → 主动伙伴

## 预警触发场景
- 🟡 某 Partner 健康度跌破 70 → 黄色预警
- 🔴 某 Partner 健康度跌破 50 → 红色预警 + 立即通知
- 📉 连续 3 天流量下降 >20% → 异常预警

---

## 预警通知示例

```
📱 来自 AI 商务经理的通知：

⚠️ Partner: GamePartner
📊 健康度: 85 → 62 (↓23)
🚨 预警等级: 🟡 黄色预警

📋 AI 分析：
• 回复速度：从 2h → 8h
• 最近沟通：语气变得简短
• 风险：可能对当前 CAP 不满意

💡 AI 建议：
"建议 24h 内主动电话沟通，
  询问是否对预算或条款有调整需求"
```

---

---

## Slide 13：AI 升级路径总结

# 🚀 AI 进化论：v1.0 → v2.0 → v3.0

```
时间轴 ─────────────────────────────────────────────────→

        v1.0                    v2.0                    v3.0
     "无状态工具"            "有状态 AI"            "主动 AI 伙伴"
        🤖                      🧠                      💗

┌───────────────┐      ┌───────────────┐      ┌───────────────┐
│ 只分析数据     │      │ 记住合作伙伴   │      │ 评估健康度     │
│ 不认识人       │      │ 自动适配话术   │      │ 主动预警       │
│ 被动响应       │  →   │ 积累关系资产   │  →   │ 预防流失       │
│ 每次都像陌生人 │      │ 越用越懂你     │      │ 越用越贴心     │
└───────────────┘      └───────────────┘      └───────────────┘

价值：效率提升      →  关系管理       →  风险预防
      90% ↓              60% ↓             ???
```

---

## 核心金句

> **"我们不是在做一个工具，而是在培养一个 AI 商务经理"**

---

---

## Slide 14：Demo 1 — 数据处理自动化

# 🧪 Demo 1：数据处理自动化

## 场景：运行多 MMP 归因去重

```bash
$ python affiliate_attribution.py \
  --af data/appsflyer_export.csv \
  --source-bank data/source_bank.csv \
  --output results/attribution_clean.csv
```

## 输出
- ✅ Source Bank 去重完成
- ✅ 渠道变体归一化（_gdn / _organic 合并）
- ✅ 排除 af_purchase_esim 无效事件
- ✅ 编码：utf-8-sig（Excel 打开无乱码）

---

> **以前：3 小时手动处理 → 现在：30 秒自动完成**

---

---

## Slide 15：Demo 2 — 跨文化沟通

# 🧪 Demo 2：一键生成 5 种文化版本

## 场景：给巴西渠道催数据

### 通用 AI 生成的邮件（❌ 冒犯）
> "Please send the report immediately. It's already overdue."

### 调用 cross-cultural-negotiation-copilot 后（✅ 适配）

| 文化圈 | 邮件内容 |
|--------|----------|
| 🇧🇷 巴西 | "Hi [Partner], hope you're having a great week! Would you mind sharing the report when you have a chance? No rush at all :)" |
| 🇨🇳 中国 | "Hi [Partner], following up on the report we discussed last week. Let me know if you need any clarification." |
| 🇪🇺 欧洲 | "Dear [Partner], I wanted to check in on the report status. Please let me know if there's anything I can help with." |
| 🌏 东南亚 | "Hi [Partner], hope all is well! Just a friendly reminder about the report. Thanks for your support!" |
| 🇸🇦 中东 | "Salam [Partner], I hope this message finds you well. Would you kindly share the report at your convenience?" |

---

> **人类需要数月掌握一种文化，AI 1 秒完成 5 种切换**

---

---

## Slide 16：Demo 3 — AI 关系管理

# 🧪 Demo 3：AI 关系健康度预警

## 场景：Dashboard 实时监控

```
┌─────────────────────────────────────────────────────────┐
│            🧠 AI Partner Relations Dashboard            │
├─────────────────────────────────────────────────────────┤
│                                                          │
│  📈 整体健康度趋势                                        │
│  ┌──────────────────────────────────────────────────┐  │
│  │ 90│    ●                                          │  │
│  │ 80│    │●                                         │  │
│  │ 70│    │ │●                                       │  │
│  │ 60│    │ │ │● ●                          ●       │  │
│  │ 50│    │ │ │ │● ●                      │ ●      │  │
│  │ 40│────│─│─│─│─●─●─●─●─●─●─●─●─●─●─●─●─●─●─●─●       │  │
│  └──────────────────────────────────────────────────┘  │
│       Week1  2   3   4   5   6   7   8   9  10         │
│                                                          │
│  🚨 预警列表                                              │
│  ┌──────────────────────────────────────────────────┐  │
│  │ 🔴 GamePartner  健康度 35  "立即电话沟通"         │  │
│  │ 🟡 AppTango     健康度 62  "24h内主动问候"        │  │
│  └──────────────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────┘
```

---

---

## Slide 17：效果数据汇总

# 📊 应用效果 — 效率提升看得见

| 指标 | Before | After | 提升 |
|------|--------|-------|------|
| 月结对账耗时 | 1 天 | 30 分钟 | **96% ↓** |
| 报表清洗去重 | 3-5h/次 | 自动完成 | **100% ↓** |
| 跨文化沟通往返 | 5-8 次/次 | 1-2 次/次 | **75% ↓** |
| 新人上手时间 | 2 周 | 2 天 | **86% ↓** |
| Partner 流失预警 | 靠经验 | AI 主动预警 | **60% ↓** |

---

## 评委关注点

| 视角 | 亮点 |
|------|------|
| 🔧 技术评委 | Layer 5 的创新性（AI 记忆、关系评估） |
| 💼 商务评委 | ROI 提升、Partner 流失率降低 |
| 📱 产品评委 | 可扩展性（能否应用到其他行业） |

---

---

## Slide 18：差异化亮点

# ✨ 为什么我们是独特的？

## 市面现状
- ✅ 数据分析工具：FineBI、Tableau、PowerBI...
- ✅ RPA 自动化：Power Automate、UiPath...
- ✅ 通用 AI 助手：ChatGPT、Claude...

## 我们的独特价值
- ❌ **跨文化商务沟通**：没有现成工具 —— 真正的壁垒
- ❌ **AI 有记忆**：不只是分析数据，还认识合作伙伴
- ❌ **关系可量化**：健康度评分让关系管理数据化

---

> **"大多数项目在做更好的数据分析工具，我们在做 AI Employee"**

---

---

## Slide 19：技术栈 & 部署

# 🔧 技术实现

| 组件 | 技术选型 |
|------|----------|
| Skill 定义 | Markdown + YAML frontmatter |
| 执行脚本 | Python 3.9+（pandas, openpyxl, requests） |
| 运行环境 | WorkBuddy / OpenClaw / CodeBuddy |
| 编码处理 | 自研 write_file.py（utf-8-sig × CRLF） |
| 数据格式 | CSV / JSON / Excel (xlsx) |

---

## 部署方式
```bash
# 方式 1：CLI
npx clawhub publish --skill skills/cross-cultural-negotiation-copilot

# 方式 2：Web UI
# 访问 SkillHub 平台，上传 SKILL.md + scripts/

# 方式 3：REST API
curl -X POST https://api.skillhub.example/v1/skills \
  -H "Authorization: Bearer TOKEN" \
  -F "file=@skill.zip"
```

---

---

## Slide 20：Q&A & 联系方式

# ❓ 谢谢观看！

## 团队：[Company]
## 项目：跨文化网盟管理 Skill 集合
## 参赛赛道：AI Agent Skill Track

---

### 核心 Skill 列表

| Layer | Skill 数量 | 代表 Skill |
|-------|------------|------------|
| Layer 1 | 3 | crm-channel-extraction |
| Layer 2 | 6 | multi-mmp-attribution-engine |
| Layer 3 | 2 | pa-report-workflow |
| Layer 4 | 1 | cross-cultural-negotiation-copilot |
| Layer 5 | 2 | partner-memory-system ⭐ |
| **总计** | **14** | — |

---

### 演示地址
- 🌐 Streamlit Demo：https://affiliate-skills-hackathon2026.streamlit.app/
- 📦 GitHub：https://github.com/Ameko2026/affiliate-skills-hackathon2026

---

> **"让 AI Agent 真正赋能跨境网盟业务"**

---

*PPT 版本 v7 | 新增 Layer 5 四页 | 2026-05-15*
