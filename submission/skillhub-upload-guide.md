# SkillHub 批量上传操作指南

> 目标：将 15 个 Skill 全部发布到 https://skillhub.cn/dashboard/publish

## 📦 已准备好的上传包

所有 Skill zip 文件位于：`submission/skillhub-zips/`

| # | 文件名 | Skill 名称 | 显示名称 | 分类 |
|---|--------|-----------|---------|------|
| 1 | ai-budget-optimizer.zip | campaign-budget-analysis | AI Budget Allocation Optimizer \| AI 预算分配优化器 | DataOps Automation |
| 2 | conversion-funnel-intelligence.zip | product-b-funnel | Conversion Funnel Intelligence \| 转化漏斗智能分析 | Business Intelligence |
| 3 | crm-channel-extraction.zip | crm-channel-extraction | CRM Channel Extraction \| 渠道 CRM 数据提取器 | DataOps Automation |
| 4 | crm-settlement-verification.zip | crm-settlement-verification | CRM Settlement Verification \| 结算数据核对智能体 | DataOps Automation |
| 5 | cross-cultural-negotiation-copilot.zip | cross-cultural-communication-engine | Cross-Cultural Negotiation Copilot \| 跨文化谈判智能助手 | Cross-Cultural Collaboration |
| 6 | cross-regional-revenue-audit.zip | product-a-analysis | Cross-Regional Revenue Audit Agent \| 跨区域收入审计智能体 | DataOps Automation |
| 7 | geo-market-intel-engine.zip | geo-market-intel | Geo Market Intelligence Engine \| 区域市场情报引擎 | Business Intelligence |
| 8 | macro-monitoring-agent.zip | macro-monitor | Macroeconomic Monitoring Agent \| 宏观经济监控智能体 | Business Intelligence |
| 9 | multi-mmp-attribution-engine.zip | affiliate-attribution | Multi-MMP Attribution Engine \| 多平台归因清洗引擎 | DataOps Automation |
| 10 | pa-channel-export.zip | pa-channel-export | PA Channel Export \| PA 渠道数据导出器 | Anti-Fraud |
| 11 | pa-report-workflow.zip | pa-report-workflow | PA Report Workflow \| PA 报告更新工作流 | Anti-Fraud |
| 12 | partner-memory-system.zip | partner-memory-system | 🧠 AI Partner Memory System | AI Organization Behavior |
| 13 | regional-wish-classifier.zip | wish-to-company-table | Regional Wish Classifier \| 区域 Wish 智能分类器 | Business Intelligence |
| 14 | relationship-health-score.zip | relationship-health-score | 💗 AI Relationship Health Score | AI Organization Behavior |
| 15 | wish-intelligence-collector.zip | wish-to-my-table | Wish Intelligence Collector \| 渠道 Wish 智能采集器 | Business Intelligence |

## 🔧 单个 Skill 发布步骤

1. 登录 https://skillhub.cn/dashboard/publish
2. 选择上传方式：
   - **方式 A**：上传 zip 文件（推荐，直接选 `submission/skillhub-zips/xxx.zip`）
   - **方式 B**：选择文件夹（选 `skills/xxx/` 目录）
3. 填写/确认元信息（SKILL.md 已包含，系统应自动识别）：
   - **Name/Slug**：使用上表"Skill 名称"列
   - **Display Name**：使用上表"显示名称"列
   - **Description**：从 SKILL.md 的 description 字段自动读取
   - **Category**：使用上表"分类"列
   - **Tags**：从 SKILL.md 的 tags 字段自动读取
4. 点击「发布」
5. 记录发布后的 URL（格式如 `https://skillhub.cn/skills/xxx`）

## 📋 建议上传顺序（按 Layer 层级）

### 第一批：核心创新（Layer 5）— 最先上传，突出亮点
- partner-memory-system.zip
- relationship-health-score.zip

### 第二批：跨文化差异化（Layer 4）
- cross-cultural-negotiation-copilot.zip

### 第三批：反欺诈专业能力（Layer 3）
- pa-channel-export.zip
- pa-report-workflow.zip

### 第四批：商业智能（Layer 2）
- conversion-funnel-intelligence.zip
- geo-market-intel-engine.zip
- macro-monitoring-agent.zip
- ai-budget-optimizer.zip
- wish-intelligence-collector.zip
- regional-wish-classifier.zip

### 第五批：数据运维基础（Layer 1）
- multi-mmp-attribution-engine.zip
- crm-channel-extraction.zip
- crm-settlement-verification.zip
- cross-regional-revenue-audit.zip

## ✅ 发布后记录模板

在下方记录每个 Skill 发布后的链接（用于比赛提交）：

| Skill | SkillHub URL | 状态 |
|-------|-------------|------|
| partner-memory-system | | ⬜ |
| relationship-health-score | | ⬜ |
| cross-cultural-negotiation-copilot | | ⬜ |
| pa-channel-export | | ⬜ |
| pa-report-workflow | | ⬜ |
| conversion-funnel-intelligence | | ⬜ |
| geo-market-intel-engine | | ⬜ |
| macro-monitoring-agent | | ⬜ |
| ai-budget-optimizer | | ⬜ |
| wish-intelligence-collector | | ⬜ |
| regional-wish-classifier | | ⬜ |
| multi-mmp-attribution-engine | | ⬜ |
| crm-channel-extraction | | ⬜ |
| crm-settlement-verification | | ⬜ |
| cross-regional-revenue-audit | | ⬜ |

---

生成时间：2026-05-18
