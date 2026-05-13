#!/usr/bin/env python3
"""Multi-MMP Attribution Engine — 多平台归因清洗引擎"""

import argparse, csv, json, sys
from pathlib import Path
from collections import defaultdict


# Source Bank: canonical name → variant mappings (extensible)
DEFAULT_SOURCE_BANK = {
    "Channel A": ["channel_a_mob", "channel_a_int", "Channel-A-Mobile",
                   "channel_a_mobile", "channel_a-ios"],
    "Channel B": ["channel_b_mob", "channel_b_int", "Channel-B-Mobile"],
    "Partner C": ["channel_c_mob", "channel_c_int", "partner_c",
                    "channel_c_alt", "goapproved_br"],
}


def load_source_bank(filepath=None):
    """Load source bank from JSON file or use defaults."""
    if filepath and Path(filepath).exists():
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    return DEFAULT_SOURCE_BANK


def build_reverse_map(source_bank):
    """Build variant → canonical reverse lookup."""
    reverse = {}
    for canonical, variants in source_bank.items():
        for v in variants:
            reverse[v.lower()] = canonical
        # Also map the canonical itself
        reverse[canonical.lower()] = canonical
    return reverse


def normalize_channel(channel_name, reverse_map):
    """Normalize a channel name to its canonical form."""
    if not channel_name or not channel_name.strip():
        return "Unknown"
    key = channel_name.strip().lower()
    return reverse_map.get(key, channel_name.strip())


def process_mmp_files(input_files, output_path, source_bank_file=None,
                      platform_col="Platform", channel_col="Channel",
                      installs_col="Installs"):
    """
    Process multiple MMP CSV files, deduplicate by normalized channel,
    and produce unified attribution dataset.
    """
    source_bank = load_source_bank(source_bank_file)
    reverse_map = build_reverse_map(source_bank)

    # Aggregate by normalized channel
    aggregated = defaultdict(lambda: {"installs": 0, "sources": {}})

    total_raw = 0

    for infile_path in input_files:
        if not Path(infile_path).exists():
            print(f"Warning: skipping missing file {infile_path}", file=sys.stderr)
            continue

        platform = Path(infile_path).stem  # Use filename as platform hint

        with open(infile_path, "r", encoding="utf-8-sig", newline="") as f:
            reader = csv.DictReader(f)
            for row in reader:
                total_raw += 1
                ch_name = row.get(channel_col, "")
                norm = normalize_channel(ch_name, reverse_map)

                try:
                    installs = int(float(row.get(installs_col, "0")))
                except (ValueError, TypeError):
                    installs = 0

                aggregated[norm]["installs"] += installs
                src = row.get(platform_col, platform)
                if src not in aggregated[norm]["sources"]:
                    aggregated[norm]["sources"][src] = 0
                aggregated[norm]["sources"][src] += installs

    # Write unified output
    rows = []
    for ch_name, data in sorted(aggregated.items(), key=lambda x: -x[1]["installs"]):
        top_source = max(data["sources"].items(), key=lambda x: x[1])[0] if data["sources"] else ""
        rows.append({
            "Channel": ch_name,
            "Total_Installs": data["installs"],
            "Top_Source": top_source,
            "Source_Count": len(data["sources"]),
            "Sources_Detail": json.dumps(data["sources"], ensure_ascii=False),
        })

    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        with open(output_path, "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=["Channel", "Total_Installs",
                                                    "Top_Source", "Source_Count",
                                                    "Sources_Detail"])
            writer.writeheader()
            writer.writerows(rows)

    return {"total_raw_records": total_raw, "normalized_channels": len(aggregated),
            "output_rows": len(rows), "output_file": output_path}


def print_summary(result):
    print(f"\nMulti-MMP Attribution Summary")
    print(f"{'='*50}")
    print(f"  Raw records (all platforms):   {result['total_raw_records']:,}")
    print(f"  Normalized unique channels:    {result['normalized_channels']}")
    print(f"  Output rows:                   {result['output_rows']:,}")
    print(f"  Output file:                   {result['output_file']}")


def main():
    parser = argparse.ArgumentParser(description="Multi-MMP Attribution Engine")
    parser.add_argument("-i", "--input", nargs="+", required=True,
                        help="Input MMP CSV files (one per platform)")
    parser.add_argument("-o", "--output", required=True,
                        help="Output unified CSV path")
    parser.add_argument("--source-bank", default=None,
                        help="Custom source bank JSON file")
    parser.add_argument("--platform-col", default="Platform",
                        help="Platform column name")
    parser.add_argument("--channel-col", default="Channel",
                        help="Channel column name")
    parser.add_argument("--installs-col", default="Installs",
                        help="Installs column name")
    args = parser.parse_args()

    result = process_mmp_files(args.input, args.output, args.source_bank,
                                args.platform_col, args.channel_col,
                                args.installs_col)
    print_summary(result)


if __name__ == "__main__":
    main()
