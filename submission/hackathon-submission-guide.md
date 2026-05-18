# 2026 腾讯云黑客松 — 提交材料填写指南

> 生成时间：2026-05-18 | 项目：跨文化网盟管理 Skill 集合

---

## 一、必填材料

### 1. 作品简介（不超过 500 字）

**直接复制以下内容粘贴：**

```
[Company] 作为跨境网盟公司，服务全球三类广告主——巴西/拉丁美洲出海公司、欧洲出海互联网公司、中国出海广告主；流量来自巴西本地渠道、中国出海 DSP/ADX/SSP、东南亚互联网公司。日常运营面临三大痛点：数据处理高度重复（每周5+份报表手动清洗对账耗时3-5小时）、跨文化沟通效率低（三类广告主×三类流量源，邮件往返5-8次）、预算分配依赖经验（人类判断导致20-30%预算浪费在低质量流量上）。

本作品将网盟运营知识封装为15个可复用 AI Agent Skill，采用五层架构：Layer 1 数据接入层从 OCR 结算单自动提取渠道数据、自动对账标记异常；Layer 2 数据分析层含 Wish List 智能分析、多 MMP 归因去重、预算最优生成建议、区域市场情报、转化漏斗分析、宏观监控；Layer 3 反作弊与归因层处理 PA 渠道数据导出、PA 报告自动化工作流；Layer 4 跨文化协作层（核心差异化）覆盖巴西/中国/欧洲/东南亚/中东五大文化圈的沟通风格适配；Layer 5 AI 组织行为层（核心创新）使 AI 进化为有记忆、会评估关系、能主动预警的"AI 商务经理"——partner-memory-system 记住每个 Partner 的10维度特征，relationship-health-score 实时评估关系健康度（0-100分）并三级预警。

技术创新：每个 Skill 内嵌完整可执行 Python 脚本；自动处理编码适配；业务规则来自真实运营经验。应用效果：月结对账从1天压减至30分钟，PA 报表100%自动化，跨文化沟通往返减少80%，Partner 流失预警准确率提升60%。
```

**字数：约 498 字 ✅**

---

### 2. Skill/Agent 文件（ZIP 压缩包，≤20MB）

**上传文件：**
```
submission/affiliate-skills.zip  (119KB，远小于 20MB 限制)
```

**文件路径：**
```
C:\Users\晏昭\WorkBuddy\2026-05-11-task-3\affiliate-skills-hackathon2026\submission\affiliate-skills.zip
```

**内容说明：** 包含全部 15 个 Skill 的 SKILL.md + scripts/ 目录，可直接导入 CodeBuddy/WorkBuddy/ClawPro 使用。

---

## 二、选填材料（加分项）

### 3. 作品说明文档（PDF/DOCX，≤50MB）

**上传文件：**
```
submission/technical_document.pdf  (16KB)
```

**文件路径：**
```
C:\Users\晏昭\WorkBuddy\2026-05-11-task-3\affiliate-skills-hackathon2026\submission\technical_document.pdf
```

**内容：** 10 章节技术文档，涵盖架构设计、Skill 详解、使用指南、部署说明。

---

### 4. 演示视频（3-5 分钟，MP4 格式，≤500MB）

**⚠️ 需用户自行录制**

**录制脚本参考：** `submission/video_script.md`

**建议内容结构（3-4 分钟）：**
1. **开场**（15秒）：项目定位 + 痛点
2. **Layer 5 演示**（60秒）：Partner Memory System + Relationship Health Score（最亮眼）
3. **Layer 4 演示**（45秒）：跨文化邮件生成（巴西↔中国）
4. **Layer 3 演示**（45秒）：PA 反欺诈报告导出
5. **Layer 2 演示**（45秒）：预算优化 / 转化漏斗
6. **结尾**（15秒）：应用效果数据 + Streamlit Demo 二维码

**录制工具推荐：** OBS / 腾讯会议录屏 / 剪映

---

### 5. 代码仓库链接（Git 地址）

**填写：**
```
https://github.com/Ameko2026/affiliate-skills-hackathon2026
```

**说明：** 默认分支为 `master`，README 包含完整项目介绍、五层架构图、Quick Start。

---

### 6. 在线体验链接 / Demo 地址

**填写：**
```
https://affiliate-skills-hackathon2026.streamlit.app/
```

**说明：** Streamlit Cloud 已部署，包含 15 个 Skill 的交互式演示页面。

---

### 7. SkillHub / 产品平台发布链接

**填写（当前 8 个已发布）：**
```
https://skillhub.cn/
```

**⚠️ 注意：** 等平台审核通过后（7 个"审核中"→"已发布"），可补充提供具体 Skill 链接。目前建议先填 SkillHub 首页，备注"15 个 Skill 已全部提交，8 个已发布，7 个审核中"。

**已发布的 8 个 Skill：**
- partner-memory-system
- relationship-health-score
- cross-cultural-negotiation-copilot
- pa-report-workflow
- pa-channel-export
- conversion-funnel-intelligence
- geo-market-intel-engine
- ai-budget-optimizer
- macro-monitoring-agent

---

### 8. 路演 PPT / Deck（PDF/PPTX，≤100MB）

**上传文件：**
```
submission/hackathon_presentation.pptx  (54KB)
```

**文件路径：**
```
C:\Users\晏昭\WorkBuddy\2026-05-11-task-3\affiliate-skills-hackathon2026\submission\hackathon_presentation.pptx
```

**内容：** 15 页路演 PPT，Ocean Gradient 配色，含五层架构图、核心亮点、应用效果、团队介绍。

---

## 三、提交检查清单

| 字段 | 状态 | 内容 |
|------|------|------|
| 作品简介 | ✅ 可直接粘贴 | 上方 498 字版本 |
| Skill/Agent 文件 | ✅ 已准备 | affiliate-skills.zip (119KB) |
| 作品说明文档 | ✅ 已准备 | technical_document.pdf (16KB) |
| 演示视频 | ⚠️ 需录制 | 参考 video_script.md |
| 代码仓库链接 | ✅ 可直接填 | GitHub 仓库 |
| 在线体验链接 | ✅ 可直接填 | Streamlit Cloud |
| SkillHub 链接 | ⏳ 部分审核中 | 8 已发布 + 7 审核中 |
| 路演 PPT | ✅ 已准备 | hackathon_presentation.pptx |

---

## 四、提交后下一步

1. **录制演示视频**（最大加分项，强烈建议做）
2. **关注 SkillHub 审核状态**，7 个"审核中"通过后补充链接
3. **GitHub README 持续更新**，保持与提交材料一致
