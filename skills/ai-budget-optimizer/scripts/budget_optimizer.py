#!/usr/bin/env python3
"""AI Budget Allocation Optimizer — 预算分配优化器"""

import argparse, csv, json, sys, math
from pathlib import Path


def load_performance_data(filepath):
    """Load historical channel performance data from CSV."""
    rows = []
    with open(filepath, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def compute_channel_score(row, decay_factor=0.9):
    """
    Compute weighted score for each channel based on:
      - ROI (higher is better)
      - Decay factor for recency
      - Quality score (if available)
      - Risk penalty (if available)
    """
    try:
        roi = float(row.get("ROI", row.get("roi", "0")))
    except (ValueError, TypeError):
        roi = 0.0

    quality = float(row.get("Quality_Score", row.get("quality_score", "0.5")))
    risk = float(row.get("Risk_Score", row.get("risk_score", "0")))

    # Weeks since last activity (for decay)
    weeks_active = int(row.get("Weeks_Active", row.get("weeks_active", "4")))
    recency_weight = decay_factor ** max(0, 8 - weeks_active)

    score = roi * recency_weight * quality * (1 - risk * 0.5)
    return round(score, 4)


def optimize_budget(channels_data, total_budget, min_pct=0.02, max_pct=0.35):
    """
    Distribute budget across channels using proportional scoring.
    
    Args:
        channels_data: list of dicts with channel metrics
        total_budget: total budget amount to allocate
        min_pct: minimum allocation per active channel (2%)
        max_pct: maximum single-channel allocation (35%)
    
    Returns:
        List of (channel, allocated_amount, percentage) tuples sorted by allocation.
    """
    # Compute scores
    scored = []
    for row in channels_data:
        ch_name = row.get("Channel", row.get("channel", "unknown"))
        score = compute_channel_score(row)
        scored.append({"channel": ch_name, "score": max(score, 0), "raw": row})

    # Filter zero/negative scores
    scored = [s for s in scored if s["score"] > 0]
    if not scored:
        return []

    total_score = sum(s["score"] for s in scored)

    # Initial proportional allocation
    allocations = []
    for s in scored:
        pct = s["score"] / total_score if total_score > 0 else 0
        pct = max(min_pct, min(pct, max_pct))
        allocations.append({
            "channel": s["channel"],
            "raw_score": round(s["score"], 4),
            "percentage": round(pct * 100, 2),
            "amount": round(pct * total_budget, 2),
        })

    # Normalize to exactly 100%
    current_total = sum(a["percentage"] for a in allocations)
    if abs(current_total - 100.0) > 0.01:
        scale = 100.0 / current_total
        for a in allocations:
            a["percentage"] = round(a["percentage"] * scale, 2)
            a["amount"] = round(a["percentage"] / 100 * total_budget, 2)

    # Sort by amount descending
    allocations.sort(key=lambda x: x["amount"], reverse=True)
    return allocations


def generate_report(allocations, total_budget):
    """Print formatted optimization report."""
    print(f"\n{'='*65}")
    print(f"  AI Budget Allocation Optimization Report")
    print(f"  Total Budget: ${total_budget:,.2f}")
    print(f"{'='*65}")
    print(f"  {'Rank':<5} {'Channel':<25} {'Score':<10} {'Alloc %':<10} {'Amount':>12}")
    print(f"  {'-'*63}")

    for i, a in enumerate(allocations, 1):
        print(f"  {i:<5} {a['channel']:<25} {a['raw_score']:<10.4f} "
              f"{a['percentage']:<9.2f}% ${a['amount']:>11,.2f}")

    print(f"  {'-'*63}")
    total_alloc = sum(a["amount"] for a in allocations)
    print(f"  {'TOTAL':<31}             100.00% ${total_alloc:>11,.2f}")


def main():
    parser = argparse.ArgumentParser(description="AI Budget Allocation Optimizer")
    parser.add_argument("-i", "--input", required=True,
                        help="CSV with historical channel performance data")
    parser.add_argument("-o", "--output", default="budget_allocation.json",
                        help="Output JSON path for allocation results")
    parser.add_argument("--budget", type=float, required=True,
                        help="Total budget amount to distribute")
    parser.add_argument("--min-pct", type=float, default=0.02,
                        help="Min allocation %% per channel (default 2%%)")
    parser.add_argument("--max-pct", type=float, default=0.35,
                        help="Max allocation %% per channel (default 35%%)")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Not found: {args.input}", file=sys.stderr); sys.exit(1)

    data = load_performance_data(args.input)
    if not data:
        print("No data loaded from input file.", file=sys.stderr); sys.exit(1)

    allocations = optimize_budget(data, args.budget, args.min_pct, args.max_pct)
    generate_report(allocations, args.budget)

    # Save JSON output
    Path(args.output).parent.mkdir(parents=True, exist_ok=True)
    with open(args.output, "w", encoding="utf-8") as f:
        json.dump({
            "total_budget": args.budget,
            "channels": allocations,
            "summary": {
                "total_channels": len(allocations),
                "total_allocated": sum(a["amount"] for a in allocations),
            }
        }, f, indent=2, ensure_ascii=False)
    print(f"\nResults saved to: {args.output}")


if __name__ == "__main__":
    main()
