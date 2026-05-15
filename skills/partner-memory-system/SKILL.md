---
name: partner-memory-system
version: 1.0.0
display_name: "🧠 AI Partner Memory System"
description: AI 记住每个 Partner 的多维度特征，从"无状态工具"升级到"有记忆的 AI 商务经理"
category: ai-organization-behavior
tags:
  - partner-management
  - ai-memory
  - relationship
author: "[Company]"
created: 2026-05-15
platform: workbuddy
---

# 🧠 Partner Memory System

> **Layer 5: AI Organization Behavior** — AI 开始"记人"

## 核心价值

将 AI Agent 从"无状态工具"升级为"有记忆的 AI 商务经理"。

- ❌ **Before**: AI 不认识人，每次沟通都是陌生人
- ✅ **After**: AI 记住每个 Partner 的 10 维度特征，越用越懂你

---

## 记忆维度（10 维度）

| 维度 | 可选值 | 说明 |
|------|--------|------|
| `communication_style` | soft / warm / aggressive / formal | 沟通风格 |
| `reply_speed` | fast / medium / slow / dead | 回复速度 |
| `risk_history` | fraud / payment_delay / no_issues | 风险历史 |
| `negotiation_habit` | price_pressure / bonus_hunter / easy_cooperation | 谈判习惯 |
| `category_preference` | finance / gaming / utility | 偏好品类 |
| `timezone` | BRT / EST / CST / ... | 时区 |
| `emotion_style` | optimistic / pessimistic / dramatic | 情绪风格 |
| `contact_reliability` | always_online / intermittent / offline | 联系可靠性 |
| `call_preference` | voice_call / sms_only / async_only | 通话偏好 |
| `budget_cooperation` | high / medium / low | 预算配合度 |

---

## 数据结构

```json
{
  "partner_id": "partner_001",
  "name": "Hertzmobi",
  "region": "🇧🇷 巴西",
  "memory": {
    "communication_style": "warm",
    "reply_speed": "fast",
    "risk_history": "no_issues",
    "negotiation_habit": "price_pressure",
    "category_preference": "finance",
    "timezone": "BRT",
    "emotion_style": "optimistic",
    "contact_reliability": "always_online",
    "call_preference": "voice_call",
    "budget_cooperation": "high"
  },
  "last_interaction": "2026-05-15T10:00:00Z",
  "last_updated": "2026-05-15T10:30:00Z",
  "confidence_score": 0.85
}
```

---

## 使用场景

### 场景 1：查询 Partner 记忆

```python
from partner_memory import get_partner_memory

# 查询 Partner 记忆
memory = get_partner_memory("partner_001")
print(memory["memory"]["communication_style"])  # 输出: "warm"
```

### 场景 2：自动适配沟通策略

```python
from partner_memory import get_communication_suggestion

# 基于记忆生成沟通建议
suggestion = get_communication_suggestion(
    partner_id="partner_001",
    context="follow_up"  # follow_up | negotiation | complaint | regular
)
print(suggestion)
# 输出: {"channel": "voice_call", "wording": "建议电话沟通，避免纯文字"}
```

### 场景 3：更新 Partner 记忆

```python
from partner_memory import update_partner_memory

# 更新 Partner 记忆
updates = {
    "reply_speed": "medium",  # 最近回复变慢了
    "emotion_style": "pessimistic"  # 最近情绪偏悲观
}
updated = update_partner_memory("partner_001", updates)
```

---

## 与其他 Skill 集成

### 集成 cross-cultural-negotiation-copilot

```python
# 在生成跨文化沟通内容前，先读取 Partner 记忆
memory = get_partner_memory("partner_001")

# 根据记忆调整文化适配策略
if memory["memory"]["call_preference"] == "voice_call":
    context = "建议电话沟通而非文字"
```

### 集成 relationship-health-score

```python
# Partner Memory 是 Relationship Health Score 的数据来源
# Health Score 会自动读取 Partner Memory 进行评分
```

---

## 更新机制

| 触发条件 | 更新逻辑 |
|----------|---------|
| 新 Partner 首次交互 | 初始化记忆，confidence = 0.3 |
| 常规交互完成 | 更新相关维度，confidence += 0.1 |
| 重要事件（付款/违约） | 立即更新 + confidence = 1.0 |
| 超过 30 天无交互 | confidence -= 0.2 |

---

## 技术规格

| 项目 | 说明 |
|------|------|
| 存储格式 | 本地 JSON 文件 |
| 存储位置 | `data/partners/{partner_id}.json` |
| 数据库 | 无需外部数据库 |
| Python 版本 | 3.9+ |
| 依赖 | json, os, datetime |

---

## 示例输出

### 查询示例

```bash
$ python partner_memory.py --action query --partner_id partner_001

{
  "partner_id": "partner_001",
  "name": "Hertzmobi",
  "region": "🇧🇷 巴西",
  "memory": {...},
  "confidence_score": 0.85,
  "last_updated": "2026-05-15T10:30:00Z"
}
```

### 更新示例

```bash
$ python partner_memory.py --action update --partner_id partner_001 \
  --updates '{"reply_speed": "medium", "emotion_style": "pessimistic"}'

✅ Partner memory updated successfully
📊 Confidence score: 0.85 → 0.90
```

---

*Skill 版本: v1.0.0*
*新增于 Hackathon 2026*
