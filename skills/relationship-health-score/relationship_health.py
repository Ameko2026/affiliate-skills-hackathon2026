"""
Relationship Health Score System
AI 关系健康度评分系统 - Layer 5 核心 Skill

功能：
1. 评估每个 Partner 的关系健康度（0-100分）
2. 三级预警机制（绿/黄/红）
3. AI 沟通策略建议

使用方法：
    python relationship_health.py --action query --partner_id partner_001
    python relationship_health.py --action check_alerts
    python relationship_health.py --action monitor_all
"""

import json
import os
import argparse
from datetime import datetime, timedelta
from pathlib import Path
from typing import Optional

# 导入 Partner Memory System
try:
    from partner_memory import get_partner_memory, list_all_partners
except ImportError:
    # 如果没有 Partner Memory，使用简化版本
    get_partner_memory = None
    list_all_partners = None

# 配置
HEALTH_DATA_DIR = Path("data/health_scores")
ALERT_HISTORY_DIR = Path("data/alert_history")

# 评分权重
WEIGHTS = {
    "reply_speed": 0.20,
    "emotion_stability": 0.25,
    "cooperation": 0.20,
    "payment_timeliness": 0.15,
    "traffic_stability": 0.20
}

# 预警阈值
THRESHOLD_HEALTHY = 70
THRESHOLD_WARNING = 50

# 评分等级
GRADE_COLORS = {
    "healthy": "🟢 健康",
    "warning": "🟡 注意",
    "critical": "🔴 预警"
}


def ensure_data_dirs():
    """确保数据目录存在"""
    HEALTH_DATA_DIR.mkdir(parents=True, exist_ok=True)
    ALERT_HISTORY_DIR.mkdir(parents=True, exist_ok=True)


def score_reply_speed(memory: dict, history: list = None) -> dict:
    """评估回复速度得分"""
    reply_speed = memory.get("memory", {}).get("reply_speed", "medium")
    
    scores = {
        "fast": 100,
        "medium": 70,
        "slow": 40,
        "dead": 10
    }
    
    score = scores.get(reply_speed, 50)
    
    # 如果有历史数据，分析趋势
    trend = "stable"
    if history and len(history) >= 2:
        prev_speed = history[-2].get("reply_speed", reply_speed)
        if scores.get(reply_speed, 50) < scores.get(prev_speed, 50):
            trend = "down"
        elif scores.get(reply_speed, 50) > scores.get(prev_speed, 50):
            trend = "up"
    
    return {
        "score": score,
        "trend": trend,
        "detail": f"回复速度: {reply_speed}"
    }


def score_emotion_stability(memory: dict, history: list = None) -> dict:
    """评估情绪稳定性得分"""
    emotion_style = memory.get("memory", {}).get("emotion_style", "optimistic")
    
    scores = {
        "optimistic": 100,
        "pessimistic": 50,
        "dramatic": 60
    }
    
    score = scores.get(emotion_style, 70)
    trend = "stable"
    
    # 情绪风格变化分析
    if history and len(history) >= 2:
        prev_emotion = history[-2].get("emotion_style", emotion_style)
        if emotion_style != prev_emotion:
            trend = "changing"
    
    return {
        "score": score,
        "trend": trend,
        "detail": f"情绪风格: {emotion_style}"
    }


def score_cooperation(memory: dict, interaction_history: list = None) -> dict:
    """评估配合度得分"""
    negotiation_habit = memory.get("memory", {}).get("negotiation_habit", "easy_cooperation")
    budget_coop = memory.get("memory", {}).get("budget_cooperation", "medium")
    
    # 基础分
    scores = {
        "easy_cooperation": 100,
        "bonus_hunter": 70,
        "price_pressure": 60
    }
    base_score = scores.get(negotiation_habit, 70)
    
    # 预算配合度调整
    budget_adjustments = {
        "high": 0,
        "medium": -10,
        "low": -20
    }
    adjustment = budget_adjustments.get(budget_coop, 0)
    
    score = max(0, min(100, base_score + adjustment))
    trend = "stable"
    
    # 分析配合度趋势
    if interaction_history and len(interaction_history) >= 3:
        recent_responses = [h.get("response_rate", 0.8) for h in interaction_history[-3:]]
        if sum(recent_responses) / len(recent_responses) < 0.7:
            trend = "down"
    
    return {
        "score": score,
        "trend": trend,
        "detail": f"谈判习惯: {negotiation_habit}, 预算配合度: {budget_coop}"
    }


def score_payment_timeliness(memory: dict, payment_history: list = None) -> dict:
    """评估付款及时性得分"""
    risk_history = memory.get("memory", {}).get("risk_history", "no_issues")
    
    scores = {
        "no_issues": 100,
        "payment_delay": 50,
        "fraud": 0
    }
    
    score = scores.get(risk_history, 70)
    
    # 分析付款延迟历史
    trend = "stable"
    if payment_history and len(payment_history) >= 3:
        delay_count = sum(1 for p in payment_history[-3:] if p.get("delayed", False))
        if delay_count >= 2:
            trend = "down"
        elif delay_count == 0:
            trend = "up"
    
    return {
        "score": score,
        "trend": trend,
        "detail": f"风险历史: {risk_history}"
    }


def score_traffic_stability(memory: dict, traffic_history: list = None) -> dict:
    """评估流量稳定性得分"""
    contact_reliability = memory.get("memory", {}).get("contact_reliability", "always_online")
    
    scores = {
        "always_online": 100,
        "intermittent": 70,
        "offline": 30
    }
    
    score = scores.get(contact_reliability, 70)
    trend = "stable"
    
    # 分析流量趋势
    if traffic_history and len(traffic_history) >= 3:
        volumes = [t.get("volume", 0) for t in traffic_history[-3:]]
        if all(volumes) and len(set(volumes)) > 1:
            avg = sum(volumes) / len(volumes)
            volatility = max(abs(v - avg) / avg for v in volumes if avg > 0) if avg > 0 else 0
            if volatility > 0.3:
                score = max(20, score - 30)
                trend = "volatile"
            elif volatility > 0.2:
                score = max(50, score - 15)
                trend = "fluctuating"
    
    return {
        "score": score,
        "trend": trend,
        "detail": f"联系可靠性: {contact_reliability}"
    }


def calculate_health_score(memory: dict, history: dict = None) -> dict:
    """
    计算综合健康度评分
    
    Args:
        memory: Partner 记忆数据
        history: 历史健康度数据
        
    Returns:
        健康度报告
    """
    partner_id = memory.get("partner_id")
    partner_name = memory.get("name", "未知")
    
    # 计算各维度得分
    breakdown = {
        "reply_speed": score_reply_speed(memory, history.get("reply_history") if history else None),
        "emotion_stability": score_emotion_stability(memory, history.get("emotion_history") if history else None),
        "cooperation": score_cooperation(memory, history.get("interaction_history") if history else None),
        "payment_timeliness": score_payment_timeliness(memory, history.get("payment_history") if history else None),
        "traffic_stability": score_traffic_stability(memory, history.get("traffic_history") if history else None)
    }
    
    # 计算加权总分
    total_score = 0
    total_weight = 0
    for dim, data in breakdown.items():
        weight = WEIGHTS.get(dim, 0)
        total_score += data["score"] * weight
        total_weight += weight
    
    health_score = int(total_score / total_weight) if total_weight > 0 else 50
    
    # 确定等级
    if health_score >= THRESHOLD_HEALTHY:
        grade = GRADE_COLORS["healthy"]
    elif health_score >= THRESHOLD_WARNING:
        grade = GRADE_COLORS["warning"]
    else:
        grade = GRADE_COLORS["critical"]
    
    # 生成预警
    alerts = []
    for dim, data in breakdown.items():
        if data["trend"] == "down" and data["score"] < 60:
            alerts.append({
                "type": f"{dim}_decline",
                "dimension": dim,
                "message": f"{dim} 评分下降: {data['score']}",
                "severity": "warning" if data["score"] >= 40 else "critical"
            })
        elif data["trend"] == "volatile":
            alerts.append({
                "type": f"{dim}_instability",
                "dimension": dim,
                "message": f"{dim} 波动较大",
                "severity": "warning"
            })
    
    # 生成 AI 建议
    ai_suggestion = generate_suggestion(health_score, grade, breakdown, alerts)
    
    return {
        "partner_id": partner_id,
        "partner_name": partner_name,
        "health_score": health_score,
        "grade": grade,
        "breakdown": breakdown,
        "alerts": alerts,
        "ai_suggestion": ai_suggestion,
        "last_updated": datetime.now().isoformat()
    }


def generate_suggestion(score: int, grade: str, breakdown: dict, alerts: list) -> dict:
    """生成 AI 沟通策略建议"""
    # 确定优先级
    priority = "low"
    if score < THRESHOLD_WARNING:
        priority = "high"
    elif score < THRESHOLD_HEALTHY:
        priority = "medium"
    
    # 确定行动建议
    if grade == GRADE_COLORS["critical"]:
        action = "立即电话沟通"
        reason = f"健康度 {score} 分处于预警状态，需要立即关注"
        script = "建议电话询问是否对当前合作有任何顾虑或调整需求，表达重视合作关系的意愿"
    elif grade == GRADE_COLORS["warning"]:
        action = "24小时内主动问候"
        reason = f"健康度 {score} 分需要注意，保持沟通频率"
        script = "建议发送友好问候消息，了解近期合作情况，表达持续合作的意愿"
    else:
        action = "保持当前沟通频率"
        reason = f"健康度 {score} 分处于健康状态"
        script = "继续保持良好的沟通频率和质量"
    
    # 添加具体维度建议
    suggestions = []
    for alert in alerts:
        dim = alert.get("dimension", "")
        if dim == "reply_speed":
            suggestions.append("注意回复速度变化，可能表示 Partner 较忙或有顾虑")
        elif dim == "emotion_stability":
            suggestions.append("关注 Partner 情绪变化，必要时提供更多支持")
        elif dim == "cooperation":
            suggestions.append("评估配合度变化，考虑是否需要调整合作条款")
        elif dim == "payment_timeliness":
            suggestions.append("⚠️ 付款记录需要关注，及时跟进")
        elif dim == "traffic_stability":
            suggestions.append("流量波动可能影响合作效果，建议分析原因")
    
    return {
        "action": action,
        "priority": priority,
        "reason": reason,
        "script": script,
        "additional_suggestions": suggestions
    }


def get_relationship_health(partner_id: str) -> dict:
    """
    获取 Partner 健康度
    
    Args:
        partner_id: Partner ID
        
    Returns:
        健康度报告
    """
    ensure_data_dirs()
    
    # 读取 Partner Memory
    if get_partner_memory:
        memory = get_partner_memory(partner_id)
        if "error" in memory:
            return memory
    else:
        return {"error": "Partner Memory System not available", "partner_id": partner_id}
    
    # 读取历史健康度数据
    history_file = HEALTH_DATA_DIR / f"{partner_id}.json"
    history = None
    if history_file.exists():
        with open(history_file, "r", encoding="utf-8") as f:
            history = json.load(f)
    
    # 计算当前健康度
    health = calculate_health_score(memory, history)
    
    # 保存当前健康度
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(health, f, ensure_ascii=False, indent=2)
    
    return health


def monitor_all_partners() -> list:
    """
    监控所有 Partner 的健康度
    
    Returns:
        所有 Partner 的健康度报告列表
    """
    ensure_data_dirs()
    
    results = []
    
    if list_all_partners:
        partners = list_all_partners()
        for partner in partners:
            partner_id = partner.get("partner_id")
            if partner_id:
                health = get_relationship_health(partner_id)
                results.append(health)
    else:
        # 如果没有 Partner Memory，扫描健康度数据
        for file in HEALTH_DATA_DIR.glob("*.json"):
            with open(file, "r", encoding="utf-8") as f:
                results.append(json.load(f))
    
    return results


def check_and_alert(threshold_warning: int = 70, threshold_critical: int = 50) -> list:
    """
    检查所有 Partner 健康度并生成预警
    
    Args:
        threshold_warning: 黄色预警阈值
        threshold_critical: 红色预警阈值
        
    Returns:
        需要预警的 Partner 列表
    """
    all_health = monitor_all_partners()
    alerts = []
    
    for health in all_health:
        if "error" in health:
            continue
        
        score = health.get("health_score", 100)
        if score < threshold_critical:
            alerts.append(health)
        elif score < threshold_warning:
            alerts.append(health)
    
    # 按健康度排序（最紧急的在前）
    alerts.sort(key=lambda x: x.get("health_score", 100))
    
    return alerts


def get_health_trend(partner_id: str, days: int = 30) -> dict:
    """
    获取 Partner 健康度趋势
    
    Args:
        partner_id: Partner ID
        days: 统计天数
        
    Returns:
        健康度趋势数据
    """
    ensure_data_dirs()
    
    history_file = HEALTH_DATA_DIR / f"{partner_id}_history.json"
    
    if not history_file.exists():
        return {
            "partner_id": partner_id,
            "trend": "insufficient_data",
            "message": "历史数据不足"
        }
    
    with open(history_file, "r", encoding="utf-8") as f:
        history = json.load(f)
    
    # 过滤最近 N 天的数据
    cutoff = datetime.now() - timedelta(days=days)
    recent = [h for h in history if datetime.fromisoformat(h["timestamp"]) > cutoff]
    
    if len(recent) < 2:
        return {
            "partner_id": partner_id,
            "trend": "insufficient_data",
            "message": "历史数据不足"
        }
    
    # 计算趋势
    scores = [h.get("health_score", 50) for h in recent]
    first_half_avg = sum(scores[:len(scores)//2]) / (len(scores)//2)
    second_half_avg = sum(scores[len(scores)//2:]) / (len(scores) - len(scores)//2)
    
    if second_half_avg > first_half_avg + 5:
        trend = "improving"
        message = "健康度呈上升趋势 📈"
    elif second_half_avg < first_half_avg - 5:
        trend = "declining"
        message = "健康度呈下降趋势 📉"
    else:
        trend = "stable"
        message = "健康度保持稳定 ➡️"
    
    return {
        "partner_id": partner_id,
        "trend": trend,
        "message": message,
        "current_score": scores[-1],
        "period_avg": sum(scores) / len(scores),
        "data_points": len(recent)
    }


def main():
    parser = argparse.ArgumentParser(description="Relationship Health Score - AI 关系健康度评分系统")
    parser.add_argument("--action", 
                        choices=["query", "monitor", "check_alerts", "trend"],
                        default="query",
                        help="操作类型")
    parser.add_argument("--partner_id", help="Partner ID")
    parser.add_argument("--days", type=int, default=30, help="趋势统计天数")
    
    args = parser.parse_args()
    
    if args.action == "query":
        if not args.partner_id:
            print("❌ Error: --partner_id is required for query")
            return
        result = get_relationship_health(args.partner_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.action == "monitor":
        results = monitor_all_partners()
        print(f"📊 共监控 {len(results)} 个 Partner:\n")
        for r in sorted(results, key=lambda x: x.get("health_score", 100)):
            if "error" not in r:
                print(f"{r['grade']} {r['partner_name']}: {r['health_score']} 分")
                print(f"   建议: {r['ai_suggestion']['action']}")
                print()
    
    elif args.action == "check_alerts":
        alerts = check_and_alert()
        if alerts:
            print(f"🚨 发现 {len(alerts)} 个需要关注的 Partner:\n")
            for alert in alerts:
                print(f"{alert['grade']} {alert['partner_name']} ({alert['partner_id']})")
                print(f"   健康度: {alert['health_score']} 分")
                if alert.get("alerts"):
                    for a in alert["alerts"]:
                        print(f"   ⚠️ {a['message']}")
                print(f"   💡 建议: {alert['ai_suggestion']['action']}")
                print()
        else:
            print("✅ 所有 Partner 健康度正常")
    
    elif args.action == "trend":
        if not args.partner_id:
            print("❌ Error: --partner_id is required for trend")
            return
        trend = get_health_trend(args.partner_id, args.days)
        print(json.dumps(trend, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
