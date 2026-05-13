#!/usr/bin/env python3
"""Macroeconomic Monitoring Agent — 宏观经济监控智能体"""

import argparse, json, sys, time
from datetime import datetime
from pathlib import Path
from collections import defaultdict


# Default monitored indicators per region
DEFAULT_INDICATORS = {
    "MENA": {
        "currencies": ["SAR", "AED", "EGP", "BHD", "QAR"],
        "countries": ["SA", "AE", "EG", "QA"],
        "alert_thresholds": {"fx_change_pct": 2.0, "inflation_change": 0.5},
    },
    "LATAM": {
        "currencies": ["BRL", "MXN", "ARS", "CLP", "COP"],
        "countries": ["BR", "MX", "AR", "CL", "CO"],
        "alert_thresholds": {"fx_change_pct": 1.5, "inflation_change": 1.0},
    },
    "APAC": {
        "currencies": ["JPY", "KRW", "INR", "IDR", "THB", "VND"],
        "countries": ["JP", "KR", "IN", "ID", "TH", "VN"],
        "alert_thresholds": {"fx_change_pct": 1.0, "inflation_change": 0.3},
    },
}


class MacroMonitor:
    """Daily macroeconomic data monitoring and alerting system."""

    def __init__(self, config_file=None):
        self.config = DEFAULT_INDICATORS
        if config_file and Path(config_file).exists():
            with open(config_file, "r") as f:
                custom = json.load(f)
                self.config.update(custom)
        self.history_file = None

    def snapshot(self, output_path=None):
        """
        Generate a macroeconomic snapshot for all configured regions.
        
        In production, this would fetch from APIs (e.g., exchangerate-api,
        World Bank, central bank feeds). For demo/standalone use, it generates
        a template snapshot with placeholder values.
        """
        snapshot = {
            "timestamp": datetime.now().isoformat(),
            "regions": {},
            "alerts": [],
        }

        for region, cfg in self.config.items():
            region_data = {
                "currencies": {},
                "indicators": {},
                "alerts": [],
            }

            # Currency rates (placeholder - would be API-fetched in production)
            for currency in cfg.get("currencies", []):
                region_data["currencies"][currency] = {
                    "rate_to_usd": _mock_fx_rate(currency),
                    "change_24h_pct": _mock_change(),
                    "trend": _mock_trend(),
                }
                # Check alert threshold
                change = abs(region_data["currencies"][currency]["change_24h_pct"])
                threshold = cfg.get("alert_thresholds", {}).get("fx_change_pct", 2.0)
                if change > threshold:
                    alert = {
                        "level": "WARNING",
                        "type": "FX_VOLATILITY",
                        "region": region,
                        "currency": currency,
                        "change_pct": round(change, 2),
                        "message": f"{currency} moved {round(change, 2)}% in 24h (threshold: {threshold}%)",
                    }
                    region_data["alerts"].append(alert)
                    snapshot["alerts"].append(alert)

            # Economic indicators (placeholder)
            for country in cfg.get("countries", []):
                region_data["indicators"][country] = {
                    "cpi_monthly": round(_mock_change(0, 2), 2),
                    "inflation_yoy": round(_mock_change(1, 10), 2),
                    "interest_rate": round(_mock_change(2, 8), 2),
                }

            snapshot["regions"][region] = region_data

        # Save if path provided
        if output_path:
            Path(output_path).parent.mkdir(parents=True, exist_ok=True)
            with open(output_path, "w", encoding="utf-8") as f:
                json.dump(snapshot, f, indent=2, ensure_ascii=False)

        return snapshot

    def print_report(self, snapshot):
        """Print formatted monitoring report."""
        ts = snapshot["timestamp"]
        print(f"\n{'='*60}")
        print(f"  Macroeconomic Monitoring Report")
        print(f"  Generated: {ts[:19]}")
        print(f"{'='*60}")

        for region, data in snapshot["regions"].items():
            print(f"\n  🌍 {region}")
            print(f"  {'-'*50}")

            # Currencies
            print(f"  Currency Rates (to USD):")
            for curr, info in data["currencies"].items():
                trend_icon = {"up": "📈", "down": "📉", "stable": "➡️"}.get(
                    info["trend"], "➡️")
                chg = info["change_24h_pct"]
                chg_str = f"+{chg}%" if chg >= 0 else f"{chg}%"
                print(f"    {curr:<6}  {info['rate_to_usd']:>10.4f}  "
                      f"{trend_icon} {chg_str:>7}")

            # Alerts for this region
            if data["alerts"]:
                print(f"\n  ⚠️  ALERTS ({len(data['alerts'])}):")
                for a in data["alerts"]:
                    print(f"    [{a['level']}] {a['message']}")

        # Summary alerts
        total_alerts = len(snapshot["alerts"])
        if total_alerts > 0:
            print(f"\n  {'='*60}")
            print(f"  🚨 TOTAL ALERTS: {total_alerts}")
        else:
            print(f"\n  ✅ All indicators within normal range.")


def _mock_fx_rate(currency):
    """Mock FX rate for demo purposes."""
    base_rates = {
        "SAR": 3.75, "AED": 3.67, "EGP": 30.9, "BHD": 0.376, "QAR": 3.64,
        "BRL": 5.05, "MXN": 17.15, "ARS": 920.0, "CLP": 880.0, "COP": 3950.0,
        "JPY": 154.5, "KRW": 1370.0, "INR": 83.5, "IDR": 16200.0,
        "THB": 34.5, "VND": 25400.0,
    }
    import random
    base = base_rates.get(currency, 1.0)
    variation = base * random.uniform(-0.005, 0.005)
    return round(base + variation, 4)


def _mock_change(lo=0, hi=3):
    import random
    return round(random.uniform(lo, hi) * (1 if random.random() > 0.5 else -1), 2)


def _mock_trend():
    import random
    r = random.random()
    return "up" if r > 0.66 else ("down" if r < 0.33 else "stable")


def main():
    parser = argparse.ArgumentParser(description="Macroeconomic Monitoring Agent")
    parser.add_argument("-o", "--output", default="./macro_snapshot.json",
                        help="Output JSON snapshot path")
    parser.add_argument("--config", default=None,
                        help="Custom config JSON file")
    parser.add_argument("--json-only", action="store_true",
                        help="Only output JSON, no report text")
    args = parser.parse_args()

    monitor = MacroMonitor(args.config)
    snapshot = monitor.snapshot(args.output)

    if not args.json_only:
        monitor.print_report(snapshot)

    print(f"\nSnapshot saved: {args.output}")


if __name__ == "__main__":
    main()
