#!/usr/bin/env python3
"""Conversion Funnel Intelligence — 转化漏斗智能分析"""

import argparse, csv, json, sys
from pathlib import Path
from collections import defaultdict


# Standard funnel stages (configurable)
FUNNEL_STAGES = [
    ("Impressions", "展示"),
    ("Clicks", "点击"),
    ("Installs", "安装"),
    ("Registrations", "注册"),
    ("First_Deposit", "首存"),
    ("Conversions", "转化"),
]

# Color-coded effectiveness ratings
EFFECTIVENESS_SCALE = [
    (90, "🟢 Excellent", "#22c55e"),   # >= 90%
    (70, "🟡 Good", "#eab308"),         # >= 70%
    (50, "🟠 Fair", "#f97316"),          # >= 50%
    (0, "🔴 Poor", "#ef4444"),           # < 50%
]


def compute_funnel_metrics(data, stage_columns=None):
    """
    Compute conversion rates between consecutive funnel stages.
    
    Args:
        data: list of dicts with numeric stage columns
        stage_columns: ordered list of (column_name, display_name) tuples
    
    Returns:
        Dict with per-stage metrics and bottleneck analysis.
    """
    stages = stage_columns or FUNNEL_STAGES
    stage_names = [s[0] for s in stages]
    stage_labels = [s[1] for s in stages]

    # Aggregate totals per stage
    totals = defaultdict(int)
    channel_funnels = defaultdict(lambda: defaultdict(int))

    for row in data:
        ch_name = row.get("Channel", row.get("channel", "Total"))
        for sn in stage_names:
            try:
                val = int(float(row.get(sn, "0")))
            except (ValueError, TypeError):
                val = 0
            totals[sn] += val
            channel_funnels[ch_name][sn] += val

    # Compute conversion rates between stages
    metrics = []
    prev_val = None
    prev_name = None

    for i, (sn, label) in enumerate(stages):
        val = totals[sn]
        cr = None
        dropoff = None
        
        if prev_val is not None and prev_val > 0:
            cr = round(val / prev_val * 100, 2)
            dropoff = round((prev_val - val) / prev_val * 100, 2)
        
        # Determine effectiveness rating
        rating = EFFECTIVENESS_SCALE[-1]
        for threshold, label_, color in EFFECTIVENESS_SCALE:
            if cr is not None and cr >= threshold:
                rating = (threshold, label_, color)
                break

        metrics.append({
            "stage": sn,
            "stage_label": label,
            "stage_order": i + 1,
            "total_count": val,
            "prev_count": prev_val or 0,
            "conversion_rate": cr,
            "dropoff_rate": dropoff,
            "rating_label": rating[1],
            "rating_color": rating[2],
        })
        prev_val = val
        prev_name = sn

    # Find bottleneck (largest drop-off)
    bottleneck = max(
        [m for m in metrics if m["dropoff_rate"] is not None],
        key=lambda x: x["dropoff_rate"],
        default=None,
    )

    return {
        "stages": metrics,
        "bottleneck": bottleneck,
        "channel_breakdown": dict(channel_funnels),
    }


def generate_cap_recommendations(metrics, budget_total=None):
    """
    Generate CAP (capacity) planning recommendations based on funnel analysis.
    
    Identifies which stages need more traffic/capacity investment.
    """
    recommendations = []
    
    for m in metrics["stages"]:
        if m["conversion_rate"] is None:
            continue
        
        cr = m["conversion_rate"]
        stage = m["stage"]
        
        if cr < 50:
            priority = "HIGH"
            action = f"Investigate {stage} — severe drop-off ({cr:.1f}%)"
        elif cr < 70:
            priority = "MEDIUM"
            action = f"Optimize {stage} flow — moderate drop-off ({cr:.1f}%)"
        elif cr < 90:
            priority = "LOW"
            action = f"Fine-tune {stage} — minor improvement possible ({cr:.1f}%)"
        else:
            continue
        
        recommendations.append({
            "stage": stage,
            "priority": priority,
            "current_cr": cr,
            "action": action,
        })

    # Bottleneck-specific recommendation
    b = metrics["bottleneck"]
    if b:
        rec_text = (
            f"BOTTLENECK at '{b['stage']}' → {b['dropoff_rate']:.1f}% drop-off. "
            f"Recommend focusing optimization resources here first."
        )
        recommendations.insert(0, {
            "stage": b["stage"],
            "priority": "CRITICAL",
            "current_cr": b["conversion_rate"],
            "action": rec_text,
        })

    return recommendations


def print_report(metrics, recommendations):
    """Print formatted funnel analysis report."""
    print(f"\n{'='*65}")
    print(f"  Conversion Funnel Intelligence Report")
    print(f"{'='*65}")

    print(f"\n  {'Stage':<20} {'Count':>12} {'Conv Rate':>12} {'Drop-off':>12} {'Rating':>14}")
    print(f"  {'-'*68}")

    for m in metrics["stages"]:
        count_str = f"{m['total_count']:,}"
        cr_str = f"{m['conversion_rate']}%" if m["conversion_rate"] is not None else "—"
        do_str = f"{m['dropoff_rate']}%" if m["dropoff_rate"] is not None else "—"
        print(f"  {m['stage_label']:<20} {count_str:>12} {cr_str:>12} {do_str:>12}  {m['rating_label']}")

    print(f"\n  🎯 Bottleneck: ", end="")
    b = metrics["bottleneck"]
    if b:
        print(f"{b['stage_label']} ({b['dropoff_rate']:.1f}% drop-off)")
    else:
        print("None identified")

    if recommendations:
        print(f"\n  📋 CAP Recommendations:")
        for r in recommendations:
            icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡",
                    "LOW": "🟢"}.get(r["priority"], "⚪")
            print(f"    {icon} [{r['priority']}] {r['action']}")


def main():
    parser = argparse.ArgumentParser(description="Conversion Funnel Intelligence")
    parser.add_argument("-i", "--input", required=True,
                        help="CSV with funnel stage columns per row/channel")
    parser.add_argument("-o", "--output", default="./funnel_report.json",
                        help="Output JSON report path")
    parser.add_argument("--stages", default=None,
                        help="Comma-separated stage column names (default: standard funnel)")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Not found: {args.input}", file=sys.stderr); sys.exit(1)

    # Parse custom stages if provided
    stage_cols = None
    if args.stages:
        names = [s.strip() for s in args.stages.split(",")]
        stage_cols = [(n, n) for n in names]

    # Load data
    enc = "utf-8-sig"
    for e in ["utf-8-sig", "utf-8", "gbk"]:
        try:
            with open(args.input, "r", encoding=e) as f: f.read(100)
            enc = e; break
        except: pass

    rows = []
    with open(args.input, "r", encoding=enc, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)

    metrics = compute_funnel_metrics(rows, stage_cols)
    recommendations = generate_cap_recommendations(metrics)

    if not args.output.endswith(".csv"):
        Path(args.output).parent.mkdir(parents=True, exist_ok=True)
        with open(args.output, "w", encoding="utf-8") as f:
            json.dump({"metrics": metrics, "recommendations": recommendations}, f, indent=2, ensure_ascii=False)

    print_report(metrics, recommendations)
    print(f"\nReport saved to: {args.output}")


if __name__ == "__main__":
    main()
