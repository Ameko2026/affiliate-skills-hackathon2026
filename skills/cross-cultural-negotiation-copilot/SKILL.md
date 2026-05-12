---
name: cross-cultural-negotiation-copilot
display_name: "Cross-Cultural Negotiation Copilot | 跨文化谈判智能助手"
description: "AI-powered cross-cultural communication adapter for affiliate partner negotiations. Generates culturally-appropriate email/message drafts that bridge communication style gaps between regions (e.g., Brazil direct style vs. Chinese indirect style). Includes Soft Wording, Validation Framing, and App Dnal Coordination Positioning strategies."
version: 1.0.0
category: cross-cultural-collaboration
tags: [cross-cultural, negotiation, communication, brazil-china, soft-skills]
layer: 4
trigger_keywords:
  - "跨文化沟通"
  - "邮件草稿"
  - "谈判话术"
  - "巴西沟通"
  - "cross-cultural"
---

# Cross-Cultural Negotiation Copilot
## 跨文化谈判智能助手

### Overview

The **core differentiator** of this skill collection. Solves a real operational pain point: **direct communication styles from Chinese teams can damage relationships with Brazilian/Latin American partners** who expect more relationship-oriented approaches.

### The Problem

```
Chinese Team Style (Direct):
"Please check your traffic quality. Your conversion rate dropped 30%.
We need to fix this by Friday or we will reduce your CAP."

→ Partner perceives: Threatening, disrespectful, transactional
→ Result: Relationship damage, reduced cooperation, partner defensiveness
```

### Three Core Strategies

#### Strategy 1: Soft Wording（委婉表达）

Replace hard demands with collaborative suggestions:

| Direct (Avoid) | Soft Wording (Use) |
|---------------|-------------------|
| "You must fix this" | "It would be helpful if we could look into this together" |
| "Your traffic quality is bad" | "We've noticed some room for improvement in conversion metrics" |
| "Reduce CAP or we stop" | "Let's discuss how to optimize the current setup for mutual benefit" |
| "This is unacceptable" | "This falls below our shared expectations" |

#### Strategy 2: Validation Framing（确认式框架）

Start by validating the partner's position before raising concerns:

```
Template:
  1. Acknowledge: "We really value our partnership with [Partner]..."
  2. Validate: "...and we appreciate the volume you've been driving."
  3. Context: "That said, looking at the latest data..."
  4. Collaborative ask: "...would you be open to exploring [suggestion] together?"
```

#### Strategy 3: App Dnal Coordination Positioning（内部协调定位）

Frame requests as **app_dnal coordination needs** rather than external demands:

| Framing | Example |
|---------|---------|
| External demand | "You need to improve quality" |
| App Dnal positioning | "I'm working to justify your increased budget app_dnally, and I need some data points to help make that case. Could we..." |

### Communication Style Matrix

| Dimension | Brazil/LATAM Style | China/East Asia Style | Adaptation Needed |
|-----------|-------------------|----------------------|-------------------|
| **Directness** | High (say what you mean) | Low (indirect, face-saving) | Chinese team → soften edges |
| **Relationship-first** | Yes (build trust first) | Mixed (task + relationship) | Add relationship context |
| **Time perception** | Flexible (relationships take time) | Efficient (time is money) | Allow more warm-up |
| **Conflict handling** | Open, expressive | Indirect, avoid confrontation | Use "we" language |
| **Decision making** | Personal trust-based | Data/hierarchy-based | Provide both data + personal touch |

### Execution Flow

```
1. User describes communication goal:
   - What message needs to be conveyed?
   - Who is the recipient (region/role/personality)?
   - What is the desired outcome?
   ↓
2. Analyze cultural context:
   - Identify source culture (team's default style)
   - Identify target culture (partner's expected style)
   - Assess relationship stage (new / established / strained)
   ↓
3. Select appropriate strategy combination:
   - Simple issue → Soft Wording only
   - Sensitive issue → Soft + Validation Framing
   - Budget/CAP negotiation → All three strategies
   ↓
4. Generate draft in target language (English/Portuguese/Spanish)
   ↓
5. Provide alternative versions:
   - Version A: Softer (for sensitive partners)
   - Version B: Balanced (standard)
   - Version C: More direct (for established, close partners)
   ↓
6. Include cultural notes explaining why certain phrasings were chosen
```

### Output Example

**Input**: "Tell Channel X their conversion rate dropped 30% and they need to fix it or we cut budget"

**Output (Balanced Version)**:

```email
Subject: Quick sync on [Campaign Name] performance opportunities

Hi [Partner Name],

Hope this email finds you well! I wanted to personally reach out because I
really value the partnership we've built over [timeframe].

The volume your team has been driving has been solid, and I appreciate
the effort you've put into [specific campaign].

I'm looking at the latest cohort data, and I wanted to flag something
that caught my attention — the post-install conversion rate has shifted
a bit compared to our baseline. I'm sharing this early because I want to
make sure we're aligned before my app_dnal review next week.

Would you be open to jumping on a brief call to compare notes? I have
some ideas on how we might optimize things together, and I'd love to
get your perspective as well.

Best regards,
[Your Name]

---
Cultural Notes:
- Opens with relationship building (not data dump)
- Uses "I'm sharing this early" = caring about partner, not blaming
- "App Dnal review" = App Dnal Coordination Positioning
- "Compare notes" = collaborative, not accusatory
- "Get your perspective" = validates partner's expertise
```

### Dependencies

No external dependencies. This skill operates at the **prompt/instruction level** — it guides the AI Agent's language generation.

### Integration

This skill should be invoked when:
- User asks to draft an email to a channel partner
- User mentions "negotiation", "communication", "draft message"
- User describes a situation involving partner conflict or difficult conversation
- Any outbound communication to LATAM/Brazil/MENA partners is being composed
