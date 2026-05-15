---
name: relationship-health-score
version: 1.0.0
display_name: "💗 AI Relationship Health Score"
description: AI 实时评估每个 Partner 的关系健康度（0-100分），三级预警 + AI 沟通策略建议
category: ai-organization-behavior
tags:
  - partner-management
  - health-score
  - relationship
  - alert
author: "[Company]"
created: 2026-05-15
platform: workbuddy
---

# 💗 Relationship Health Score

> **Layer 5: AI Organization Behavior** — AI 开始"评估关系"

## 核心价值

将 AI 从"监控数据异常"升级到"监控关系异常"。

- ❌ **Before**: 靠经验判断谁要流失，往往发现时已经晚了
- ✅ **After**: AI 实时评估健康度，主动预警潜在流失

---

## 评分维度

| 维度 | 权重 | 说明 |
|------|------|------|
| 回复速度 (reply_speed) | 20% | 最近 30 天平均回复时间趋势 |
| 情绪稳定性 (emotion_stability) | 25% | 最近沟通的语气波动分析 |
| 配合度 (cooperation) | 20% | 任务完成率、CAP 调整响应率 |
| 付款及时性 (payment_timeliness) | 15% | 付款延迟次数统计 |
| 流量稳定性 (traffic_stability) | 20% | 最近 30 天流量波动 |

---

## 评分标准

### 各维度评分规则

| 维度 | 100分 | 70分 | 50分 | 30分 |
|------|-------|------|------|------|
| 回复速度 | 持续 fast | 偶尔 medium | 经常 slow | 出现 dead |
| 情绪稳定性 | 持续正面 | 偶尔波动 | 负面增多 | 持续负面 |
| 配合度 | 100% 响应 | 80%+ 响应 | 50%+ 响应 | <50% 响应 |
| 付款及时性 | 从不延迟 | 偶尔延迟 | 经常延迟 | 多次严重延迟 |
| 流量稳定性 | 波动 <10% | 波动 10-20% | 波动 20-30% | 波动 >30% |

### 综合评分

```
Health Score = Σ (dimension_score × weight) / Σ weights
```

### 预警等级

| 等级 | 分数范围 | 颜色 | AI 动作 |
|------|----------|------|---------|
| 🟢 健康 | ≥70 分 | 绿色 | 正常监控 |
| 🟡 注意 | 50-70 分 | 黄色 | 24h 内主动问候 |
| 🔴 预警 | <50 分 | 红色 | 立即通知 + 建议行动 |

---

## 数据结构

### 健康度报告

```json
{
  "partner_id": "partner_001",
  "partner_name": "Hertzmobi",
  "health_score": 62,
  "grade": "🟡 注意",
  "breakdown": {
    "reply_speed": {"score": 70, "trend": "down", "weight": 0.20},
    "emotion_stability": {"score": 55, "trend": "stable", "weight": 0.25},
    "cooperation": {"score": 65, "trend": "stable", "weight": 0.20},
    "payment_timeliness": {"score": 80, "trend": "stable", "weight": 0.15},
    "traffic_stability": {"score": 50, "trend": "down", "weight": 0.20}
  },
  "alerts": [
    {
      "type": "reply_speed_decline",
      "message": "回复速度从 2h 降至 8h",
      "severity": "warning"
    }
  ],
  "ai_suggestion": {
    "action": "主动电话沟通",
    "reason": "该 Partner 回复速度和流量都出现下降趋势",
    "script": "建议电话询问是否对当前 CAP 或条款有调整需求",
    "priority": "high"
  },
  "last_updated": "2026-05-15T10:30:00Z"
}
```

---

## 使用场景

### 场景 1：查询健康度

```python
from relationship_health import get_relationship_health

# 查询 Partner 健康度
health = get_relationship_health("partner_001")
print(f"健康度: {health['health_score']} ({health['grade']})")
```

### 场景 2：批量监控

```python
from relationship_health import monitor_all_partners

# 监控所有 Partner 健康度
results = monitor_all_partners()

# 筛选需要预警的
alerts = [r for r in results if r["grade"] in ["🟡 注意", "🔴 预警"]]
for alert in alerts:
    send_notification(alert)
```

### 场景 3：预警通知

```python
from relationship_health import check_and_alert

# 检查并自动发送预警
alerts = check_and_alert(
    threshold_warning=70,
    threshold_critical=50
)

for alert in alerts:
    print(f"🚨 {alert['partner_name']}: {alert['health_score']} 分")
    print(f"   建议: {alert['ai_suggestion']['action']}")
```

---

## 与其他 Skill 集成

### 集成 partner-memory-system

```python
# Health Score 自动读取 Partner Memory 进行评分
from partner_memory import get_partner_memory

memory = get_partner_memory(partner_id)
# 使用 memory 中的数据计算各维度得分
```

### 集成 cross-cultural-negotiation-copilot

```python
# 根据健康度调整沟通策略
health = get_relationship_health(partner_id)

if health["grade"] == "🔴 预警":
    strategy = "empathetic_urgent"  # 共情优先 + 紧迫感
    message = "非常重视与您的合作关系..."
elif health["grade"] == "🟡 注意":
    strategy = "supportive_caring"  # 支持性 + 关心
    message = "希望了解您最近的反馈..."
else:
    strategy = "normal"  # 正常商务沟通
```

---

## 技术规格

| 项目 | 说明 |
|------|------|
| 存储格式 | 本地 JSON 文件 |
| 存储位置 | `data/health_scores/{partner_id}.json` |
| 数据来源 | partner-memory-system |
| Python 版本 | 3.9+ |
| 依赖 | json, os, datetime |

---

## 示例输出

### 健康度查询

```bash
$ python relationship_health.py --action query --partner_id partner_001

{
  "partner_id": "partner_001",
  "partner_name": "Hertzmobi",
  "health_score": 85,
  "grade": "🟢 健康",
  "breakdown": {...},
  "ai_suggestion": {
    "action": "保持当前沟通频率",
    "priority": "low"
  }
}
```

### 预警检查

```bash
$ python relationship_health.py --action check_alerts

🚨 发现 2 个需要关注的 Partner:

🔴 partner_003 (GamePartner)
   健康度: 35 分
   原因: 回复速度下降 + 流量波动 >30%
   建议: 立即电话沟通

🟡 partner_002 (AppTango)
   健康度: 62 分
   原因: 最近情绪风格偏悲观
   建议: 24h 内主动问候
```

---

*Skill 版本: v1.0.0*
*新增于 Hackathon 2026*
