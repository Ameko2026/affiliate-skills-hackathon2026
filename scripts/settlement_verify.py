#!/usr/bin/env python3
"""CRM Settlement Verification — 结算数据核对智能体"""

import argparse, csv, sys
from datetime import datetime
from pathlib import Path


def detect_encoding(filepath):
    for enc in ["utf-8-sig", "utf-8", "gbk", "latin-1"]:
        try:
            with open(filepath, "r", encoding=enc) as f: f.read(4096)
            return enc
        except (UnicodeDecodeError, UnicodeError): continue
    return "utf-8"


def parse_date(date_str):
    for fmt in ("%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%Y/%m/%d %H:%M:%S"):
        try: return datetime.strptime(date_str.strip(), fmt)
        except ValueError: continue
    return None


def verify_settlement(
    input_path, output_path,
    channel=None,
    promotion_start=None,
    promotion_end=None,
    event_name=None,
    dry_run=False,
):
    """
    Multi-step funnel validation:
      Step 1: Primary Attribution filter
      Step 2: Transaction ID validation
      Step 3: Channel match
      Step 4: Promotion window check
    """
    encoding = detect_encoding(input_path)
    promo_start = parse_date(promotion_start) if promotion_start else None
    promo_end = parse_date(promotion_end) if promotion_end else None

    # Funnel stats per step
    funnel = {
        "step0_total": 0,
        "step1_primary": 0,
        "step2_valid_tx": 0,
        "step3_channel": 0,
        "step4_window": 0,
    }
    valid_rows = []
    rejected = []  # (row, reason)

    with open(input_path, "r", encoding=encoding, newline="") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or []

        for row in reader:
            funnel["step0_total"] += 1

            # Step 1: Is Primary Attribution = true?
            attr_val = row.get("Is Primary Attribution", "") or row.get("is_primary", "")
            if attr_val.strip().lower() not in ("true", "1", "yes"):
                rejected.append((row, "Not primary attribution"))
                continue
            funnel["step1_primary"] += 1

            # Step 2: Event Value contains transaction_id?
            evt_val = row.get("Event Value", "") or row.get("event_value", "") or ""
            if not evt_val.strip():
                rejected.append((row, "Missing transaction ID"))
                continue
            funnel["step2_valid_tx"] += 1

            # Step 3: Channel matches target?
            if channel:
                ch_val = row.get("Channel", "") or row.get("channel", "") or ""
                if channel.lower() not in ch_val.lower():
                    rejected.append((row, f"Channel mismatch: {ch_val}"))
                    continue
            funnel["step3_channel"] += 1

            # Step 4: Event Time within promotion window?
            if promo_start or promo_end:
                time_val = row.get("Event Time", "") or row.get("event_time", "")
                evt_time = parse_date(time_val)
                if evt_time:
                    if promo_start and evt_time < promo_start:
                        rejected.append((row, f"Before promotion start: {time_val}"))
                        continue
                    if promo_end and evt_time > promo_end:
                        rejected.append((row, f"After promotion end: {time_val}"))
                        continue
            funnel["step4_window"] += 1
            valid_rows.append(row)

    # Write output
    if not dry_run and valid_rows:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="") as out:
            writer = csv.DictWriter(out, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(valid_rows)

    total = max(funnel["step0_total"], 1)
    report = {
        "funnel": funnel,
        "valid_count": len(valid_rows),
        "rejected_count": len(rejected),
        "pass_rate": round(len(valid_rows) / total * 100, 2),
        "output_file": output_path if not dry_run else "(dry run)",
    }
    return report


def print_report(report):
    f = report["funnel"]
    total = max(f["step0_total"], 1)
    print(f"\nSettlement Verification Report")
    print(f"{'='*50}")
    print(f"  Step 0 - Total Records:          {f['step0_total']:>8,}")
    print(f"  Step 1 - Primary Attribution:     {f['step1_primary']:>8,}  ({f['step1_primary']/total*100:>6.1f}%)")
    print(f"  Step 2 - Valid Transaction ID:    {f['step2_valid_tx']:>8,}  ({f['step2_valid_tx']/total*100:>6.1f}%)")
    print(f"  Step 3 - Channel Match:           {f['step3_channel']:>8,}  ({f['step3_channel']/total*100:>6.1f}%)")
    print(f"  Step 4 - Promotion Window OK:     {f['step4_window']:>8,}  ({f['step4_window']/total*100:>6.1f}%)")
    print(f"{'='*50}")
    print(f"  VALID records:   {report['valid_count']:>8,}")
    print(f"  REJECTED:        {report['rejected_count']:>8,}")
    print(f"  Pass Rate:       {report['pass_rate']:>8.2f}%")
    print(f"  Output:          {report['output_file']}")


def main():
    parser = argparse.ArgumentParser(description="Settlement Data Verification")
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--channel", help="Target channel name")
    parser.add_argument("--promotion-start", help="Promotion start date (YYYY-MM-DD HH:MM:SS)")
    parser.add_argument("--promotion-end", help="Promotion end date (YYYY-MM-DD HH:MM:SS)")
    parser.add_argument("--event-name", help="Event name to filter")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Not found: {args.input}", file=sys.stderr); sys.exit(1)

    report = verify_settlement(args.input, args.output, args.channel,
                                args.promotion_start, args.promotion_end,
                                args.event_name, args.dry_run)
    print_report(report)


if __name__ == "__main__":
    main()
