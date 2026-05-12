#!/usr/bin/env python3
"""Wish Intelligence Collector — 渠道 Wish 智能采集器"""

import argparse, csv, json, sys, re
from pathlib import Path


# Standardized 8-column tracking table schema
TRACKING_COLUMNS = [
    "Channel_Name",       # 渠道名称
    "App_ID",             # App ID / Package Name
    "Geo_Target",         # 目标国家/地区
    "Offer_Type",         # Offer 类型 (CPA/CPI/CPS/CPM)
    "Payout",             # 报价/佣金
    "Cap_Limit",          # CAP 上限
    "Tracking_Link",      # 追踪链接
    "Notes",              # 备注
]


def parse_text_wish(text_content):
    """Parse plain text Wish List into structured rows."""
    lines = [l.strip() for l in text_content.strip().split("\n") if l.strip()]
    rows = []
    current = {}

    for line in lines:
        # Try to detect key-value patterns
        for key_pattern, col in [
            (r"(?i)(channel|渠道|source|来源)", "Channel_Name"),
            (r"(?i)(app\s*id|package|包名|应用)", "App_ID"),
            (r"(?i)(geo|country|target|地区|国家)", "Geo_Target"),
            (r"(?i)(offer\s*type|type|类型)", "Offer_Type"),
            (r"(?i)(payout|price|报价|佣金|价格)", "Payout"),
            (r"(?i)(cap|limit|上限|量级)", "Cap_Limit"),
            (r"(?i)(link|url|tracking|链接|追踪)", "Tracking_Link"),
            (r"(?i)(note|remark|备注|说明)", "Notes"),
        ]:
            if re.search(key_pattern, line):
                # Extract value after colon/comma/etc
                parts = re.split(r"[:：,，]", line, maxsplit=1)
                if len(parts) >= 2:
                    current[col] = parts[1].strip()
                break
        else:
            # If no pattern matched and we have accumulated data,
            # this might be a new entry starting
            if current and any(current.values()):
                if len(current) >= 3:  # Need at least some fields to be valid
                    row = {col: current.get(col, "") for col in TRACKING_COLUMNS}
                    rows.append(row)
                current = {}
            # Treat as potential free-form data

    # Don't forget the last entry
    if current and any(current.values()) and len(current) >= 3:
        row = {col: current.get(col, "") for col in TRACKING_COLUMNS}
        rows.append(row)

    return rows


def parse_excel_wish(filepath):
    """Parse Excel-based Wish List."""
    try:
        import openpyxl
    except ImportError:
        print("Warning: openpyxl not installed, falling back to CSV parsing", file=sys.stderr)
        return parse_csv_wish(filepath)

    wb = openpyxl.load_workbook(filepath, read_only=True)
    ws = wb.active
    rows = []
    headers = None

    for row in ws.iter_rows(values_only=True):
        if headers is None:
            headers = [str(c or "") for c in row]
            continue
        if not any(row):
            continue
        
        record = dict(zip(headers, [str(v or "") for v in row]))
        mapped = {col: "" for col in TRACKING_COLUMNS}
        
        # Map known column names
        mapping = {
            "Channel_Name": ["channel", "Channel", "渠道", "Source"],
            "App_ID": ["app_id", "App ID", "AppID", "Package", "app", "应用"],
            "Geo_Target": ["geo", "Geo", "Country", "地区", "Target"],
            "Offer_Type": ["type", "Type", "Offer Type", "类型", "offer_type"],
            "Payout": ["payout", "Payout", "Price", "报价", "佣金", "price"],
            "Cap_Limit": ["cap", "Cap", "Limit", "上限", "CAP"],
            "Tracking_Link": ["link", "Link", "URL", "链接", "tracking", "url"],
            "Notes": ["notes", "Notes", "Remark", "备注", "note"],
        }
        
        for target_col, source_keys in mapping.items():
            for sk in source_keys:
                if sk in record and record[sk]:
                    mapped[target_col] = record[sk]
                    break
        
        if any(mapped.values()):
            rows.append(mapped)

    wb.close()
    return rows


def parse_csv_wish(filepath):
    """Parse CSV-based Wish List."""
    enc = "utf-8-sig"
    for e in ["utf-8-sig", "utf-8", "gbk"]:
        try:
            with open(filepath, "r", encoding=e) as f: f.read(100)
            enc = e; break
        except: pass
    
    rows = []
    with open(filepath, "r", encoding=enc, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            mapped = {col: row.get(col, "") for col in TRACKING_COLUMNS}
            if any(mapped.values()):
                rows.append(mapped)
    return rows


def save_tracking_table(rows, output_path):
    """Save standardized tracking table to CSV."""
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=TRACKING_COLUMNS)
        writer.writeheader()
        writer.writerows(rows)


def main():
    parser = argparse.ArgumentParser(description="Wish Intelligence Collector")
    parser.add_argument("-i", "--input", required=True,
                        help="Input file (txt/csv/xlsx) or '-' for stdin text")
    parser.add_argument("-o", "--output", default="./output/wish_tracking.csv",
                        help="Output tracking CSV path")
    args = parser.parse_args()

    if args.input == "-":
        text = sys.stdin.read()
        rows = parse_text_wish(text)
    elif not Path(args.input).exists():
        print(f"Not found: {args.input}", file=sys.stderr); sys.exit(1)
    else:
        suffix = Path(args.input).suffix.lower()
        if suffix in (".xlsx", ".xls"):
            rows = parse_excel_wish(args.input)
        elif suffix == ".csv":
            rows = parse_csv_wish(args.input)
        else:
            with open(args.input, "r", encoding="utf-8") as f:
                rows = parse_text_wish(f.read())

    save_tracking_table(rows, args.output)

    print(f"\nWish Intelligence Collection Summary")
    print(f"{'='*40}")
    print(f"  Offers parsed:     {len(rows)}")
    print(f"  Output file:       {args.output}")
    print(f"  Schema ({len(TRACKING_COLUMNS)} columns):")
    for c in TRACKING_COLUMNS:
        print(f"    - {c}")


if __name__ == "__main__":
    main()
