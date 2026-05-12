#!/usr/bin/env python3
"""Regional Wish Classifier — 区域 Wish 智能分类器"""

import argparse, csv, sys
from pathlib import Path


# Country → Region mapping (extensible)
COUNTRY_REGION_MAP = {
    # MENA
    "SA": "MENA", "AE": "MENA", "QA": "MENA", "KW": "MENA", "BH": "MENA",
    "OM": "MENA", "JO": "MENA", "EG": "MENA", "MA": "MENA", "TN": "MENA",
    "DZ": "MENA", "IQ": "MENA", "LB": "MENA", "SY": "MENA", "YE": "MENA",
    "saudi arabia": "MENA", "uae": "MENA", "qatar": "MENA", "kuwait": "MENA",
    "bahrain": "MENA", "oman": "MENA", "jordan": "MENA", "egypt": "MENA",
    "morocco": "MENA", "algeria": "MENA",
    # LATAM
    "BR": "LATAM", "MX": "LATAM", "AR": "LATAM", "CO": "LATAM", "CL": "LATAM",
    "PE": "LATAM", "VE": "LATAM", "EC": "LATAM", "BO": "LATAM", "PY": "LATAM",
    "UY": "LATAM", "PA": "LATAM", "CR": "LATAM", "DO": "LATAM", "GT": "LATAM",
    "brazil": "LATAM", "mexico": "LATAM", "argentina": "LATAM", "colombia": "LATAM",
    "chile": "LATAM", "peru": "LATAM", "venezuela": "LATAM",
    # APAC
    "JP": "APAC", "KR": "APAC", "IN": "APAC", "ID": "APAC", "TH": "APAC",
    "VN": "APAC", "PH": "APAC", "MY": "APAC", "SG": "APAC", "TW": "APAC",
    "HK": "APAC", "AU": "APAC", "NZ": "APAC", "PK": "APAC", "BD": "APAC",
    "japan": "APAC", "korea": "APAC", "india": "APAC", "indonesia": "APAC",
    "thailand": "APAC", "vietnam": "APAC", "philippines": "APAC", "malaysia": "APAC",
    "singapore": "APAC", "taiwan": "APAC", "australia": "APAC",
    # Europe & US
    "US": "EU_US", "GB": "EU_US", "DE": "EU_US", "FR": "EU_US", "IT": "EU_US",
    "ES": "EU_US", "NL": "EU_US", "PL": "EU_US", "SE": "EU_US", "NO": "EU_US",
    "DK": "EU_US", "FI": "EU_US", "AT": "EU_US", "BE": "EU_US", "IE": "EU_US",
    "PT": "EU_US", "GR": "EU_US", "CZ": "EU_US", "RO": "EU_US", "HU": "EU_US",
    "CA": "EU_US", "CH": "EU_US", "united states": "EU_US", "uk": "EU_US",
    "united kingdom": "EU_US", "germany": "EU_US", "france": "EU_US", "italy": "EU_US",
    "spain": "EU_US", "netherlands": "EU_US", "canada": "EU_US",
}

REGION_ORDER = ["MENA", "LATAM", "APAC", "EU_US", "Global"]


def classify_region(geo_value):
    """Classify a geo target string into a regional zone."""
    if not geo_value or not str(geo_value).strip():
        return "Global"
    
    key = str(geo_value).strip().lower()
    
    # Direct lookup
    if key in COUNTRY_REGION_MAP:
        return COUNTRY_REGION_MAP[key]
    
    # Check by country code (2-letter)
    code = key.upper()[:2] if len(key) >= 2 else ""
    if code in COUNTRY_REGION_MAP:
        return COUNTRY_REGION_MAP[code]
    
    # Keyword matching
    mena_kw = ["middle east", "arab", "gcc", "gulf"]
    latam_kw = ["latin america", "south america", "latam"]
    apac_kw = ["asia pacific", "asia-pacific", "southeast asia"]
    eu_us_kw = ["europe", "north america", "western"]
    
    for kws, region in [(mena_kw, "MENA"), (latam_kw, "LATAM"),
                         (apac_kw, "APAC"), (eu_us_kw, "EU_US")]:
        if any(kw in key for kw in kws):
            return region
    
    return "Global"


def classify_offers(input_path, output_dir, geo_column="Geo_Target"):
    """Classify offers by region and generate per-region spreadsheets."""
    enc = "utf-8-sig"
    for e in ["utf-8-sig", "utf-8", "gbk"]:
        try:
            with open(input_path, "r", encoding=e) as f: f.read(100)
            enc = e; break
        except: pass
    
    region_buckets = {r: [] for r in REGION_ORDER}
    fieldnames = []

    with open(input_path, "r", encoding=enc, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = list(reader.fieldnames or [])
        for row in reader:
            geo_val = row.get(geo_column, "") or row.get("Geo", "")
            region = classify_region(geo_val)
            row["_Region"] = region
            region_buckets[region].append(row)

    # Write per-region files + master with region column
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    all_fieldnames = fieldnames + ["_Region"]
    
    # Master file (all regions combined)
    master_path = f"{output_dir}/classified_master.csv"
    all_rows = []
    for r in REGION_ORDER:
        all_rows.extend(region_buckets[r])
    
    with open(master_path, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=all_fieldnames)
        w.writeheader(); w.writerows(all_rows)
    
    # Per-region files
    region_files = {}
    for region in REGION_ORDER:
        if not region_buckets[region]:
            continue
        rpath = f"{output_dir}/region_{region.lower()}.csv"
        with open(rpath, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=all_fieldnames)
            w.writeheader(); w.writerows(region_buckets[region])
        region_files[region] = rpath

    return {
        "total_offers": sum(len(v) for v in region_buckets.values()),
        "regions": {r: len(region_buckets[r]) for r in REGION_ORDER if region_buckets[r]},
        "master_file": master_path,
        "region_files": region_files,
    }


def main():
    parser = argparse.ArgumentParser(description="Regional Wish Classifier")
    parser.add_argument("-i", "--input", required=True, help="Input tracking CSV")
    parser.add_argument("-o", "--output-dir", default="./regional_output",
                        help="Output directory for classified files")
    parser.add_argument("--geo-column", default="Geo_Target",
                        help="Geo target column name")
    args = parser.parse_args()

    if not Path(args.input).exists():
        print(f"Not found: {args.input}", file=sys.stderr); sys.exit(1)

    result = classify_offers(args.input, args.output_dir, args.geo_column)

    print(f"\nRegional Classification Summary")
    print(f"{'='*40}")
    print(f"  Total offers:   {result['total_offers']}")
    print(f"  By region:")
    for region, count in result["regions"].items():
        bar = "#" * max(1, count // 2)
        print(f"    {region:<10} {count:>5}  {bar}")
    print(f"\n  Master file:    {result['master_file']}")
    print(f"  Region files:")
    for region, fpath in result["region_files"].items():
        print(f"    {region:<10} -> {fpath}")


if __name__ == "__main__":
    main()
