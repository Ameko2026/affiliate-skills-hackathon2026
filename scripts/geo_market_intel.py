#!/usr/bin/env python3
"""Geo Market Intelligence Engine — 区域市场情报引擎"""

import argparse, json, sys, re
from datetime import datetime
from pathlib import Path


# Regional market data template (extensible via config)
REGIONAL_TEMPLATES = {
    "MENA": {
        "top_categories": ["Fintech", "Gaming", "E-commerce", "Crypto"],
        "key_markets": ["Saudi Arabia", "UAE", "Egypt", "Qatar"],
        "trends": ["Digital payments adoption", "Gaming growth", "BNPL expansion"],
        "regulatory_notes": "SAMA/UAE CB regulations tightening on digital lending",
    },
    "LATAM": {
        "top_categories": ["Fintech", "Social", "Ride-hailing", "E-commerce"],
        "key_markets": ["Brazil", "Mexico", "Argentina", "Colombia"],
        "trends": ["Pix payment growth", "Super-app emergence", "Credit adoption"],
        "regulatory_notes": "BCB/CMV regulations on crypto and digital wallets",
    },
    "APAC": {
        "top_categories": ["Fintech", "Gaming", "Social", "E-commerce"],
        "key_markets": ["Japan", "Korea", "India", "Indonesia", "Thailand"],
        "trends": ["Super-app dominance", "Cross-border e-commerce", "Web3 exploration"],
        "regulatory_notes": "Varied: JP/KR strict, ID/TH more flexible",
    },
    "EU_US": {
        "top_categories": ["Fintech", "SaaS", "Health", "Productivity"],
        "key_markets": ["US", "UK", "Germany", "France"],
        "trends": ["AI integration", "Privacy-first products", "Subscription fatigue"],
        "regulatory_notes": "GDPR/DMA compliance critical; Apple ATT impact ongoing",
    },
}


class GeoMarketIntel:
    """Multi-region market intelligence aggregator."""

    def __init__(self, config_file=None):
        self.templates = REGIONAL_TEMPLATES.copy()
        if config_file and Path(config_file).exists():
            with open(config_file, "r") as f:
                custom = json.load(f)
                self.templates.update(custom)

    def generate_report(self, regions=None, output_path=None):
        """
        Generate market intelligence report for specified regions.
        
        In production, this would aggregate from:
          - App Store / Google Play ranking APIs
          - News feeds (RSS / web scraping)
          - Competitor monitoring tools
          - Regulatory databases
        
        For demo use, generates structured report from templates.
        """
        target_regions = regions or list(self.templates.keys())
        
        report = {
            "generated_at": datetime.now().isoformat(),
            "regions": {},
        }

        for region in target_regions:
            if region not in self.templates:
                continue
            
            tpl = self.templates[region]
            
            # Simulated top apps per category (placeholder for production API calls)
            top_apps = {}
            for cat in tpl.get("top_categories", []):
                top_apps[cat] = [
                    f"{cat} Leader {region}",
                    f"{cat} Challenger A",
                    f"{cat} Challenger B",
                ]

            report["regions"][region] = {
                "key_markets": tpl["key_markets"],
                "top_categories": tpl["top_categories"],
                "top_apps_by_category": top_apps,
                "trends": tpl["trends"],
                "regulatory_notes": tpl["regulatory_notes"],
                "opportunity_score": self._score_opportunity(region),
            }

        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(report, f, indent=2, ensure_ascii=False)

        return report

    def _score_opportunity(self, region):
        """Score market opportunity (1-10) based on template heuristics."""
        scores = {"MENA": 8.5, "LATAM": 9.0, "APAC": 7.5, "EU_US": 6.0}
        return scores.get(region, 5.0)

    def print_report(self, report):
        """Print formatted market intelligence briefing."""
        print(f"\n{'='*60}")
        print(f"  Geo Market Intelligence Briefing")
        print(f"  Generated: {report['generated_at'][:19]}")
        print(f"{'='*60}")

        for region, data in report["regions"].items():
            score = data["opportunity_score"]
            score_bar = "⭐" * int(score / 2) + "☆" * (5 - int(score / 2))
            
            print(f"\n  🌍 {region}  Opportunity: {score}/10  {score_bar}")
            print(f"  {'-'*50}")
            print(f"  Key Markets:     {', '.join(data['key_markets'])}")
            print(f"  Top Categories:  {', '.join(data['top_categories'])}")
            print(f"  Trends:")
            for t in data["trends"]:
                print(f"    → {t}")
            print(f"  Regulatory:      {data['regulatory_notes']}")


def main():
    parser = argparse.ArgumentParser(description="Geo Market Intelligence Engine")
    parser.add_argument("--regions", nargs="+",
                        help="Regions to include (MENA LATAM APAC EU_US)")
    parser.add_argument("-o", "--output", default="./market_intel.json",
                        help="Output JSON path")
    parser.add_argument("--config", default=None,
                        help="Custom regional config JSON")
    parser.add_argument("--json-only", action="store_true",
                        help="Only output JSON, no text report")
    args = parser.parse_args()

    intel = GeoMarketIntel(args.config)
    report = intel.generate_report(args.regions, args.output)

    if not args.json_only:
        intel.print_report(report)

    print(f"\nReport saved to: {args.output}")


if __name__ == "__main__":
    main()
