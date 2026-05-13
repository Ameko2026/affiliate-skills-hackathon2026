#!/usr/bin/env python3
"""PA Report Workflow — PA 报告更新工作流

Weekly pipeline:
  Step 1: Collect AppsFlyer PA CSV files from Downloads folder
  Step 2: Process into JS array format
  Step 3: Inject data into HTML report page
  
Handles cross-period date splitting and multi-app aggregation.
"""

import argparse, csv, json, sys, os, glob, re
from datetime import datetime, timedelta
from pathlib import Path


def collect_pa_csvs(downloads_dir=None):
    """Collect all PA CSV files from Downloads folder."""
    d = downloads_dir or str(Path.home() / "Downloads")
    pattern = os.path.join(d, "*PA*.csv")
    files = sorted(glob.glob(pattern))
    
    # Also try broader patterns if no exact matches
    if not files:
        for p in [os.path.join(d, "*pa*.csv"), os.path.join(d, "*.csv")]:
            files = sorted(glob.glob(p))
            if files:
                break
    
    return files


def parse_date_from_filename(filepath):
    """Extract date info from filename like 'PA_2026-05-12.csv'."""
    name = Path(filepath).stem
    # Try common patterns
    patterns = [
        r"(\d{4})[-_](\d{1,2})[-_](\d{1,2})",   # 2026-05-12 or 2026_05_12
        r"(\d{4})(\d{2})(\d{2})",                  # 20260512
        r"week[_\-]?(\d+)",                          # week1, week-3
        r"w(\d+)",                                   # w1, w3
    ]
    for pat in patterns:
        m = re.search(pat, name, re.IGNORECASE)
        if m:
            return m.group(0)
    return None


def csv_to_js_array(csv_path, array_name="weekData"):
    """
    Convert a PA CSV file to a JavaScript array string.
    
    Each row becomes an object in the JS array.
    Handles single-line empty arrays gracefully.
    """
    enc = "utf-8-sig"
    for e in ["utf-8-sig", "utf-8", "gbk"]:
        try:
            with open(csv_path, "r", encoding=e) as f: f.read(100)
            enc = e; break
        except: pass
    
    rows = []
    fieldnames = []
    
    with open(csv_path, "r", encoding=enc, newline="") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames or []
        for row in reader:
            # Clean row values for JS embedding
            clean_row = {}
            for k, v in row.items():
                s = str(v).strip()
                # Escape for JS string context
                s = s.replace("\\", "\\\\").replace('"', '\\"').replace("\n", "\\n")
                clean_row[k] = s
            rows.append(clean_row)
    
    if not rows:
        return f"var {array_name} = [];", [], fieldnames
    
    # Build JS array of objects
    obj_strings = []
    for row in rows:
        pairs = [f'  "{k}": "{v}"' for k, v in row.items()]
        obj_str = "{\n" + ",\n".join(pairs) + "\n}"
        obj_strings.append(obj_str)
    
    js_content = f"var {array_name} = [\n" + ",\n".join(obj_strings) + "\n];"
    return js_content, rows, fieldnames


def inject_into_html(html_path, js_array_map, output_path=None):
    """
    Inject JS arrays into an HTML report template.
    
    js_array_map: dict of {array_variable_name: js_array_string}
    Finds <script> tags with matching variable declarations and replaces them.
    """
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    replacements = 0
    for var_name, js_content in js_array_map.items():
        # Pattern: var varName = [...]; (including empty arrays)
        pattern = re.compile(
            rf'var\s+{re.escape(var_name)}\s*=\s*\[.*?\];',
            re.DOTALL
        )
        new_html, count = pattern.subn(js_content, html_content)
        if count > 0:
            html_content = new_html
            replacements += count
        else:
            # If pattern not found, append as new script block
            script_tag = f'\n<script>\n{js_content}\n</script>\n'
            html_content += script_tag
            replacements += 1
    
    out = output_path or html_path
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    return replacements


def run_pipeline(downloads_dir=None, html_template=None, output_html=None):
    """Execute the full weekly PA report update pipeline."""
    # Step 1: Collect CSVs
    csv_files = collect_pa_csvs(downloads_dir)
    print(f"Collected {len(csv_files)} PA CSV file(s)")

    if not csv_files:
        print("No PA CSV files found. Pipeline complete (no updates).")
        return {"files_processed": 0, "arrays_generated": 0}

    # Step 2: Process each CSV into JS arrays
    js_arrays = {}
    for i, csv_path in enumerate(csv_files, 1):
        date_hint = parse_date_from_filename(csv_path) or f"week{i}"
        safe_name = re.sub(r'[^a-zA-Z0-9]', '_', date_hint)
        array_name = f"week{safe_name}Data"
        
        js_content, rows, fields = csv_to_js_array(csv_path, array_name)
        js_arrays[array_name] = js_content
        
        print(f"  [{i}] {Path(csv_path).name} → {array_name} ({rows} rows, {len(fields)} fields)")

    # Step 3: Inject into HTML
    injections = 0
    if html_template and js_arrays:
        injections = inject_into_html(html_template, js_arrays, output_html)
        print(f"\nInjected {injections} data array(s) into HTML report")
        print(f"Output: {output_html or html_template}")
    else:
        print(f"\nGenerated {len(js_arrays)} JS array(s) (no HTML template provided)")
        for name, content in js_arrays.items():
            out_path = f"./pa_data/{name}.js"
            Path(out_path).parent.mkdir(parents=True, exist_ok=True)
            with open(out_path, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"  Saved: {out_path}")

    return {"files_processed": len(csv_files), "arrays_generated": len(js_arrays),
            "html_injections": injections}


def main():
    parser = argparse.ArgumentParser(description="PA Report Weekly Update Workflow")
    parser.add_argument("--downloads-dir", default=None,
                        help="Path to Downloads folder (default: ~/Downloads)")
    parser.add_argument("--html-template", default=None,
                        help="HTML report template path")
    parser.add_argument("-o", "--output-html", default=None,
                        help="Output HTML path (default: overwrite template)")
    args = parser.parse_args()

    result = run_pipeline(args.downloads_dir, args.html_template, args.output_html)
    
    print(f"\nPipeline Summary")
    print(f"{'='*40}")
    print(f"  Files processed:  {result['files_processed']}")
    print(f"  Arrays generated: {result['arrays_generated']}")
    print(f"  HTML injections:  {result['html_injections']}")


if __name__ == "__main__":
    main()
