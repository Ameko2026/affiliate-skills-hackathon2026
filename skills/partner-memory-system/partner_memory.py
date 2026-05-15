"""
Partner Memory System
AI 合作伙伴记忆系统 - Layer 5 核心 Skill

功能：
1. 存储和查询 Partner 的多维度记忆
2. 基于记忆生成沟通策略建议
3. 自动更新记忆置信度

使用方法：
    python partner_memory.py --action query --partner_id partner_001
    python partner_memory.py --action update --partner_id partner_001 --updates '{"reply_speed": "medium"}'
    python partner_memory.py --action suggest --partner_id partner_001 --context follow_up
"""

import json
import os
import argparse
from datetime import datetime
from pathlib import Path

# 配置
DATA_DIR = Path("data/partners")
DEFAULT_CONFIDENCE = 0.3
CONFIDENCE_INCREMENT = 0.1
CONFIDENCE_DECAY = 0.2
MEMORY_DIMENSIONS = [
    "communication_style",
    "reply_speed", 
    "risk_history",
    "negotiation_habit",
    "category_preference",
    "timezone",
    "emotion_style",
    "contact_reliability",
    "call_preference",
    "budget_cooperation"
]

VALID_VALUES = {
    "communication_style": ["soft", "warm", "aggressive", "formal"],
    "reply_speed": ["fast", "medium", "slow", "dead"],
    "risk_history": ["fraud", "payment_delay", "no_issues"],
    "negotiation_habit": ["price_pressure", "bonus_hunter", "easy_cooperation"],
    "category_preference": ["finance", "gaming", "utility"],
    "timezone": ["BRT", "EST", "CST", "GMT", "CET", "JST", "ICT"],
    "emotion_style": ["optimistic", "pessimistic", "dramatic"],
    "contact_reliability": ["always_online", "intermittent", "offline"],
    "call_preference": ["voice_call", "sms_only", "async_only"],
    "budget_cooperation": ["high", "medium", "low"]
}

# 沟通策略建议模板
STRATEGY_TEMPLATES = {
    "follow_up": {
        "voice_call": "建议电话跟进，语气亲切自然",
        "sms_only": "建议发送简洁文字，语气友好",
        "async_only": "建议异步沟通，发送邮件或消息"
    },
    "negotiation": {
        "price_pressure": "谈判时预留议价空间，准备好让步方案",
        "bonus_hunter": "准备额外激励方案，如提高分成比例",
        "easy_cooperation": "直接进入正题，效率优先"
    },
    "complaint": {
        "pessimistic": "先共情理解，再理性分析问题",
        "dramatic": "认真对待情绪，表达理解和重视",
        "optimistic": "积极回应，展示改进意愿"
    },
    "regular": {
        "warm": "保持温暖友好的沟通风格",
        "formal": "使用正式商务用语",
        "soft": "语气柔和，避免直接施压",
        "aggressive": "简洁明了，直接进入主题"
    }
}


def ensure_data_dir():
    """确保数据目录存在"""
    DATA_DIR.mkdir(parents=True, exist_ok=True)


def get_partner_file(partner_id: str) -> Path:
    """获取 Partner 数据文件路径"""
    return DATA_DIR / f"{partner_id}.json"


def get_partner_memory(partner_id: str) -> dict:
    """
    查询 Partner 记忆
    
    Args:
        partner_id: Partner ID
        
    Returns:
        Partner 记忆 JSON
    """
    partner_file = get_partner_file(partner_id)
    
    if not partner_file.exists():
        return {
            "error": f"Partner {partner_id} not found",
            "partner_id": partner_id,
            "exists": False
        }
    
    with open(partner_file, "r", encoding="utf-8") as f:
        memory = json.load(f)
    
    return memory


def create_partner_memory(partner_id: str, name: str, region: str = "未知", **kwargs) -> dict:
    """
    创建新的 Partner 记忆
    
    Args:
        partner_id: Partner ID
        name: Partner 名称
        region: 地区
        **kwargs: 记忆维度初始值
    """
    ensure_data_dir()
    
    memory = {
        "partner_id": partner_id,
        "name": name,
        "region": region,
        "memory": {},
        "last_interaction": datetime.now().isoformat(),
        "last_updated": datetime.now().isoformat(),
        "confidence_score": DEFAULT_CONFIDENCE
    }
    
    # 设置默认记忆
    for dim in MEMORY_DIMENSIONS:
        if dim in kwargs:
            memory["memory"][dim] = kwargs[dim]
        else:
            memory["memory"][dim] = None
    
    partner_file = get_partner_file(partner_id)
    with open(partner_file, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)
    
    return memory


def update_partner_memory(partner_id: str, updates: dict) -> dict:
    """
    更新 Partner 记忆
    
    Args:
        partner_id: Partner ID
        updates: 需要更新的维度及其新值
        
    Returns:
        更新后的记忆
    """
    partner_file = get_partner_file(partner_id)
    
    if not partner_file.exists():
        return {"error": f"Partner {partner_id} not found", "partner_id": partner_id}
    
    with open(partner_file, "r", encoding="utf-8") as f:
        memory = json.load(f)
    
    # 更新记忆维度
    for key, value in updates.items():
        if key in MEMORY_DIMENSIONS:
            # 验证值是否合法
            if key in VALID_VALUES and value not in VALID_VALUES[key]:
                print(f"⚠️  Warning: {key} value '{value}' not in valid values {VALID_VALUES[key]}")
            memory["memory"][key] = value
    
    # 更新置信度（每次交互后提高）
    memory["confidence_score"] = min(1.0, memory["confidence_score"] + CONFIDENCE_INCREMENT)
    memory["last_interaction"] = datetime.now().isoformat()
    memory["last_updated"] = datetime.now().isoformat()
    
    with open(partner_file, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=2)
    
    return memory


def get_communication_suggestion(partner_id: str, context: str = "regular") -> dict:
    """
    基于 Partner 记忆生成沟通策略建议
    
    Args:
        partner_id: Partner ID
        context: 沟通场景 (follow_up | negotiation | complaint | regular)
        
    Returns:
        沟通策略建议
    """
    memory = get_partner_memory(partner_id)
    
    if "error" in memory:
        return memory
    
    partner_memory = memory.get("memory", {})
    
    # 默认策略
    suggestion = {
        "partner_id": partner_id,
        "partner_name": memory.get("name"),
        "context": context,
        "suggestions": []
    }
    
    # 根据不同场景生成建议
    if context == "follow_up":
        call_pref = partner_memory.get("call_preference", "sms_only")
        suggestion["suggestions"].append(STRATEGY_TEMPLATES["follow_up"].get(call_pref, "建议文字沟通"))
        suggestion["suggestions"].append(f"时区: {partner_memory.get('timezone', '未知')}，注意工作时段")
    
    elif context == "negotiation":
        neg_habit = partner_memory.get("negotiation_habit", "easy_cooperation")
        suggestion["suggestions"].append(STRATEGY_TEMPLATES["negotiation"].get(neg_habit, "直接进入正题"))
        
        budget_coop = partner_memory.get("budget_cooperation", "medium")
        if budget_coop == "low":
            suggestion["suggestions"].append("⚠️ 预算配合度低，谈判时需准备让步方案")
    
    elif context == "complaint":
        emotion = partner_memory.get("emotion_style", "optimistic")
        suggestion["suggestions"].append(STRATEGY_TEMPLATES["complaint"].get(emotion, "理性回应"))
        suggestion["suggestions"].append("先共情理解，再理性分析问题")
    
    else:  # regular
        comm_style = partner_memory.get("communication_style", "formal")
        suggestion["suggestions"].append(STRATEGY_TEMPLATES["regular"].get(comm_style, "保持专业"))
    
    # 通用建议
    reply_speed = partner_memory.get("reply_speed", "medium")
    if reply_speed == "slow":
        suggestion["suggestions"].append("⚠️ 回复速度较慢，沟通时保持耐心")
    elif reply_speed == "dead":
        suggestion["suggestions"].append("🚨 Partner 几乎无回复，建议考虑替代方案")
    
    return suggestion


def delete_partner_memory(partner_id: str) -> dict:
    """删除 Partner 记忆"""
    partner_file = get_partner_file(partner_id)
    
    if not partner_file.exists():
        return {"error": f"Partner {partner_id} not found", "partner_id": partner_id}
    
    partner_file.unlink()
    return {"success": True, "partner_id": partner_id, "message": "Partner memory deleted"}


def list_all_partners() -> list:
    """列出所有 Partner"""
    ensure_data_dir()
    partners = []
    
    for file in DATA_DIR.glob("*.json"):
        with open(file, "r", encoding="utf-8") as f:
            data = json.load(f)
            partners.append({
                "partner_id": data.get("partner_id"),
                "name": data.get("name"),
                "region": data.get("region"),
                "confidence_score": data.get("confidence_score", 0),
                "last_interaction": data.get("last_interaction")
            })
    
    return partners


def main():
    parser = argparse.ArgumentParser(description="Partner Memory System - AI 合作伙伴记忆系统")
    parser.add_argument("--action", choices=["query", "create", "update", "delete", "suggest", "list"],
                        default="query", help="操作类型")
    parser.add_argument("--partner_id", help="Partner ID")
    parser.add_argument("--name", help="Partner 名称 (用于创建)")
    parser.add_argument("--region", default="未知", help="Partner 地区 (用于创建)")
    parser.add_argument("--updates", help="更新数据 (JSON 格式)")
    parser.add_argument("--context", default="regular", 
                        choices=["follow_up", "negotiation", "complaint", "regular"],
                        help="沟通场景 (用于建议)")
    
    args = parser.parse_args()
    
    if args.action == "query":
        if not args.partner_id:
            print("❌ Error: --partner_id is required for query")
            return
        result = get_partner_memory(args.partner_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.action == "create":
        if not args.partner_id or not args.name:
            print("❌ Error: --partner_id and --name are required for create")
            return
        result = create_partner_memory(args.partner_id, args.name, args.region)
        print(f"✅ Partner {args.partner_id} created successfully")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.action == "update":
        if not args.partner_id or not args.updates:
            print("❌ Error: --partner_id and --updates are required for update")
            return
        updates = json.loads(args.updates)
        result = update_partner_memory(args.partner_id, updates)
        print(f"✅ Partner {args.partner_id} memory updated successfully")
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.action == "delete":
        if not args.partner_id:
            print("❌ Error: --partner_id is required for delete")
            return
        result = delete_partner_memory(args.partner_id)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.action == "suggest":
        if not args.partner_id:
            print("❌ Error: --partner_id is required for suggest")
            return
        result = get_communication_suggestion(args.partner_id, args.context)
        print(json.dumps(result, ensure_ascii=False, indent=2))
    
    elif args.action == "list":
        partners = list_all_partners()
        print(f"📋 Total Partners: {len(partners)}")
        for p in partners:
            print(f"  - {p['partner_id']}: {p['name']} ({p['region']}) | Confidence: {p['confidence_score']:.2f}")


if __name__ == "__main__":
    main()
