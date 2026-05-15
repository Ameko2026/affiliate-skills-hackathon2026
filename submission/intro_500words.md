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

本作品将网盟运营知识封装为**13 个可复用 AI Agent Skill**，采用五层架构：
**Layer 1 数据接入层**从 OCR 结算单自动提取渠道数据（crm-channel-extraction）、自动对账标记异常（crm-settlement-verification）
**Layer 2 数据分析层**含 Wish List 智能分析（wish-intelligence-collector / regional-wish-classifier）；多 MMP 归因去重基于 Source Bank 优先级（multi-mmp-attribution-engine）；预算最优生成建议（ai-budget-optimizer）；区域市场情报（geo-market-intel-engine）；转化漏斗分析（conversion-funnel-intelligence）；宏观监控（macro-monitoring-agent）
**Layer 3 反作弊与归因层**处理 PA 渠道数据导出（pa-channel-export）、PA 报告自动化工作流（pa-report-workflow）
**Layer 4 跨文化协作层（核心差异化）**含全球化跨文化沟通引擎（cross-cultural-negotiation-copilot v2.0），覆盖 🇧🇷 巴西 / 🇨🇳 中国 / 🇪🇺 欧洲 / 🌏 东南亚 / 🇸🇦 中东 五大文化圈
**Layer 5 AI 组织行为层（核心创新）**是本作品最大创新——AI 不再只是被动执行工具，而是进化为有记忆、会评估关系、能主动预警的"AI 商务经理"：
  - **partner-memory-system**：AI 记住每个 Partner 的沟通风格、回复速度、风险历史、谈判习惯、偏好品类、时区、情绪风格等10维度信息
  - **relationship-health-score**：AI 实时评估每个 Partner 的关系健康度（0-100分），三级预警（绿/黄/红）+ AI 沟通策略建议

**AI 升级路径**：
- v1.0 无状态工具：只分析数据，不认识人
- v2.0 有状态 AI：记住合作伙伴特征，自动适配沟通风格
- v3.0 主动 AI：评估关系健康度，主动预警潜在流失风险

**技术创新**：每个 Skill 内嵌完整可执行 Python 脚本，AI Agent 可自动调用；所有输出自动处理编码适配（utf-8-sig × Excel 无乱码）；业务规则来自真实运营经验，非通用 Prompt；支持同一事项一键生成 5 种文化版本；AI 开始"记人"+"评估关系"

**应用效果**：月结对账时间从 1 天压减至 30 分钟，PA 报表制作 100% 自动化；Wish List 区分 95% 效率提升；跨文化沟通往返次数减少 80%；新人上手时间从 2 周压缩到 2 天；**Partner 流失预警准确率提升 60%**

（共 502 字）
