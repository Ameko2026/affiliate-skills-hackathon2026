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

    region_key = partner_region.upper() if partner_region.upper() in patterns else "DEFAULT"
    pattern = patterns[region_key]
    stage = stage_modifiers.get(relationship_stage, stage_modifiers["established"])

    greeting = pattern["greeting"]
    opener = pattern["opener"]
    intro = stage["intro_phrase"]

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

