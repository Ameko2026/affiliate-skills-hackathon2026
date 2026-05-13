#!/usr/bin/env python3
"""CRM Channel Extraction — 渠道数据提取器"""

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
    for fmt in ("%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%m/%d/%Y"):
        try: return datetime.strptime(date_str.strip(), fmt)
        except ValueError: continue
    return None


def filter_channels(input_path, output_path, channel=None, media_source=None,
                    event_type=None, start_date=None, end_date=None,
                    attribution_type=None, dry_run=False):
    encoding = detect_encoding(input_path)
    sources = [s.strip().lower() for s in media_source.split(",")] if media_source else None
    start_dt = parse_date(start_date) if start_date else None
    end_dt = parse_date(end_date) if end_date else None
    stats = {"total_rows": 0, "matched_rows": 0, "filtered_out": 0}
    rows_written = []

    with open(input_path, "r", encoding=encoding, newline="") as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames or []
        for row in reader:
            stats["total_rows"] += 1
            keep = True

            if channel and keep:
                ch_val = row.get("Channel", "") or row.get("channel", "")
                if channel.lower() not in ch_val.lower(): keep = False

            if sources and keep:
                ms_val = row.get("Media Source", "") or row.get("media_source", "")
                if ms_val.lower().strip() not in sources: keep = False

            if event_type and keep:
                et_val = row.get("Event Name", "") or row.get("event_name", "")
                if event_type.lower() not in et_val.lower(): keep = False

            if attribution_type and keep:
                at_val = row.get("Attribution Type", "") or row.get("attribution_type", "")
                if attribution_type.lower() not in at_val.lower(): keep = False

            if (start_dt or end_dt) and keep:
                date_val = row.get("Event Time", "") or row.get("event_time", "") or row.get("Date", "")
                row_dt = parse_date(date_val)
                if row_dt:
                    if start_dt and row_dt < start_dt: keep = False
                    if end_dt and row_dt > end_dt: keep = False

            if keep:
                stats["matched_rows"] += 1
                rows_written.append(row)
            else:
                stats["filtered_out"] += 1

    if not dry_run and rows_written:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="") as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows_written)

    stats["output_file"] = output_path if not dry_run else "(dry run)"
    stats["match_rate"] = round(stats["matched_rows"] / max(stats["total_rows"], 1) * 100, 2)
    return stats


def main():
    parser = argparse.ArgumentParser(description="CRM Channel Data Extraction & Filter")
    parser.add_argument("-i", "--input", required=True)
    parser.add_argument("-o", "--output", required=True)
    parser.add_argument("--channel"); parser.add_argument("--media-source")
    parser.add_argument("--event-type"); parser.add_argument("--start-date")
    parser.add_argument("--end-date"); parser.add_argument("--attribution-type")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Input file not found: {args.input}", file=sys.stderr); sys.exit(1)

    stats = filter_channels(args.input, args.output, args.channel, args.media_source,
                            args.event_type, args.start_date, args.end_date,
                            args.attribution_type, args.dry_run)
    print(f"\nChannel Extraction Summary\n{'='*40}")
    print(f"  Total rows:     {stats['total_rows']:,}")
    print(f"  Matched rows:   {stats['matched_rows']:,}")
    print(f"  Filtered out:   {stats['filtered_out']:,}")
    print(f"  Match rate:     {stats['match_rate']}%")
    print(f"  Output:         {stats['output_file']}")


if __name__ == "__main__":
    main()
