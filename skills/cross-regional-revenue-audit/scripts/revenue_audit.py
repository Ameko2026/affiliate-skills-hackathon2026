#!/usr/bin/env python3
"""Cross-Regional Revenue Audit — 跨区域收入审计智能体"""

import argparse, csv, sys
from pathlib import Path
from datetime import datetime
from collections import defaultdict


def detect_encoding(filepath):
    for enc in ["utf-8-sig", "utf-8", "gbk", "latin-1"]:
        try:
            with open(filepath, "r", encoding=enc) as f: f.read(4096)
            return enc
        except (UnicodeDecodeError, UnicodeError): continue
    return "utf-8"


def parse_money(val):
    """Parse monetary value from string."""
    try:
        return float(str(val).replace(",", "").replace("$", "").strip())
    except (ValueError, TypeError):
        return 0.0


def run_audit(mmp_file, settlement_file, revenue_file, output_dir,
              region_col="Region", channel_col="Channel"):
    """
    Full P&L audit integrating MMP + settlement + revenue data.
    
    Generates a comprehensive audit report with ROI analysis per channel/region.
    """
    # Load all three data sources
    mmp_data = _load_csv(mmp_file)
    settlement_data = _load_csv(settlement_file)
    revenue_data = _load_csv(revenue_file)

    # Aggregate by region → channel
    pnl = defaultdict(lambda: {
        "installs": 0, "conversions": 0, "revenue": 0.0,
        "cost": 0.0, "settlement": 0.0, "events": [],
    })

    for row in mmp_data:
        region = row.get(region_col, "Unknown")
        ch = row.get(channel_col, "Unknown")
        key = (region, ch)
        try: pnl[key]["installs"] += int(float(row.get("Installs", "0")))
        except: pass
        try: pnl[key]["conversions"] += int(float(row.get("Conversions", "0")))
        except: pass

    for row in settlement_data:
        region = row.get(region_col, "Unknown")
        ch = row.get(channel_col, "Unknown")
        key = (region, ch)
        pnl[key]["cost"] += parse_money(row.get("Cost", row.get("cost", "0")))
        pnl[key]["settlement"] += parse_money(row.get("Settlement", row.get("settlement", "0")))

    for row in revenue_data:
        region = row.get(region_col, "Unknown")
        ch = row.get(channel_col, "Unknown")
        key = (region, ch)
        pnl[key]["revenue"] += parse_money(row.get("Revenue", row.get("revenue", "0")))

    # Compute ROI
    results = []
    for (region, ch), data in pnl.items():
        profit = data["revenue"] - data["cost"]
        roi = (profit / data["cost"] * 100) if data["cost"] > 0 else float("inf")
        results.append({
            "Region": region,
            "Channel": ch,
            "Installs": data["installs"],
            "Conversions": data["conversions"],
            "Cost": round(data["cost"], 2),
            "Revenue": round(data["revenue"], 2),
            "Profit": round(profit, 2),
            "ROI_pct": round(roi, 2) if roi != float("inf") else "N/A",
            "Status": "POSITIVE" if profit >= 0 else "NEGATIVE",
        })

    results.sort(key=lambda x: x["Profit"], reverse=True)

    # Write output
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Sheet 1: P&L Summary
    out_path = f"{output_dir}/pnl_summary.csv"
    if results:
        with open(out_path, "w", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, fieldnames=results[0].keys())
            w.writeheader(); w.writerows(results)

    # Print summary
    total_revenue = sum(r["Revenue"] for r in results)
    total_cost = sum(r["Cost"] for r in results)
    total_profit = sum(r["Profit"] for r in results)
    positive = sum(1 for r in results if r["Status"] == "POSITIVE")
    negative = len(results) - positive

    print(f"\nCross-Regional Revenue Audit Report")
    print(f"{'='*55}")
    print(f"  Total Channels Analyzed:      {len(results)}")
    print(f"  Total Revenue:               ${total_revenue:>14,.2f}")
    print(f"  Total Cost:                  ${total_cost:>14,.2f}")
    print(f"  Net Profit:                  ${total_profit:>14,.2f}")
    print(f"  ROI-Positive Channels:       {positive}")
    print(f"  ROI-Negative Channels:       {negative}")
    print(f"{'='*55}")

    if results:
        print(f"\n  {'Rank':<5} {'Region':<10} {'Channel':<20} {'Profit':>12} {'ROI':>10}")
        print(f"  {'-'*50}")
        for i, r in enumerate(results[:15], 1):
            roi_str = f"{r['ROI_pct']}%" if r['ROI_pct'] != "N/A" else " N/A"
            print(f"  {i:<5} {r['Region']:<10} {r['Channel']:<20} ${r['Profit']:>11,.2f} {roi_str:>9}")

    return {"channels": len(results), "positive": positive, "negative": negative,
            "total_profit": round(total_profit, 2), "output_dir": output_dir}


def _load_csv(filepath):
    rows = []
    if not Path(filepath).exists():
        return rows
    enc = detect_encoding(filepath)
    with open(filepath, "r", encoding=enc, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            rows.append(row)
    return rows


def main():
    parser = argparse.ArgumentParser(description="Cross-Regional Revenue Audit")
    parser.add_argument("--mmp", required=True, help="MMP install/conversion CSV")
    parser.add_argument("--settlement", required=True, help="Settlement cost CSV")
    parser.add_argument("--revenue", required=True, help="Revenue/payment CSV")
    parser.add_argument("-o", "--output-dir", default="./audit_output",
                        help="Output directory for reports")
    parser.add_argument("--region-col", default="Region")
    parser.add_argument("--channel-col", default="Channel")
    args = parser.parse_args()

    for fp in [args.mmp, args.settlement, args.revenue]:
        if not Path(fp).exists():
            print(f"Not found: {fp}", file=sys.stderr); sys.exit(1)

    report = run_audit(args.mmp, args.settlement, args.revenue,
                       args.output_dir, args.region_col, args.channel_col)
    print(f"\nReports saved to: {report['output_dir']}")


if __name__ == "__main__":
    main()
