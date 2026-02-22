"""
Finance Agent - Lulebore Apartment 1 financial tracking.

Orchestrates: booking_loader -> airbnb_loader -> financial_calculator -> excel_generator
Outputs: financial_dashboard.xlsx, financial_report.md, financial_data.json
"""

import json
import sys
from datetime import datetime
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
sys.path.insert(0, str(PROJECT_ROOT))

from finance_skills.booking_loader import load_reservations as load_booking
from finance_skills.airbnb_loader import load_reservations as load_airbnb
from finance_skills.financial_calculator import compute_metrics
from finance_skills.excel_generator import generate_excel


def run():
    """Run the complete financial tracking pipeline."""
    print(f"\n{'=' * 70}")
    print(f"  FINANCE AGENT - Lulebore Apartment 1")
    print(f"  Run date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print(f"{'=' * 70}\n")

    all_issues = []

    # Step 1: Load Booking.com data
    print("  [1/4] Loading Booking.com data...")
    booking_result = load_booking()
    booking_reservations = booking_result["reservations"]
    all_issues.extend(booking_result["issues"])
    bs = booking_result["summary"]
    print(f"         + {bs.get('revenue_reservations', 0)} revenue reservations, "
          f"{bs.get('total_room_nights', 0)} nights")
    print(f"         + Gross: EUR {bs.get('total_gross_eur', 0):,.2f}  |  "
          f"Fees: EUR {bs.get('total_commission_eur', 0):,.2f}  |  "
          f"Net: EUR {bs.get('total_net_eur', 0):,.2f}")

    # Step 2: Load Airbnb data
    print("\n  [2/4] Loading Airbnb data...")
    airbnb_result = load_airbnb()
    airbnb_reservations = airbnb_result["reservations"]
    all_issues.extend(airbnb_result["issues"])
    ab = airbnb_result["summary"]
    if ab.get("total_reservations", 0) > 0:
        print(f"         + {ab['total_reservations']} reservations, "
              f"{ab['total_room_nights']} nights")
        print(f"         + Gross: EUR {ab.get('total_gross_eur', 0):,.2f}  |  "
              f"Fees: EUR {ab.get('total_commission_eur', 0):,.2f}  |  "
              f"Net: EUR {ab.get('total_net_eur', 0):,.2f}")
    else:
        print("         ! No Airbnb reservation data found")

    # Step 3: Calculate metrics
    print("\n  [3/4] Computing financial metrics...")
    metrics = compute_metrics(booking_reservations, airbnb_reservations)
    all_issues.extend(metrics["issues"])

    at = metrics["all_time"]
    print(f"         + {at['months_tracked']} months tracked ({at['date_range']})")
    print(f"         + Total Gross: EUR {at['total_gross']:,.2f}")
    print(f"         + Total Fees:  EUR {at['total_fees']:,.2f}")
    print(f"         + Total Net:   EUR {at['total_net']:,.2f}")

    # Step 4: Generate outputs
    print("\n  [4/4] Generating outputs...")

    # Excel
    booking_months = bs.get("months_covered", [])
    airbnb_months = ab.get("months_covered", [])
    excel_path = generate_excel(
        metrics, booking_reservations, airbnb_reservations,
        booking_months, airbnb_months,
    )
    print(f"         + {excel_path}")

    # Markdown report
    report_path = _generate_report(metrics, all_issues)
    print(f"         + {report_path}")

    # JSON data
    json_path = _generate_json(metrics, bs, ab, all_issues)
    print(f"         + {json_path}")

    # Print summary
    _print_summary(metrics, all_issues)

    return {
        "excel_path": excel_path,
        "report_path": report_path,
        "json_path": json_path,
        "metrics": metrics,
        "issues": all_issues,
    }


def _generate_report(metrics, issues):
    """Generate financial_report.md."""
    at = metrics["all_time"]
    lines = []
    lines.append("# Financial Report - Lulebore Apartment 1\n")
    lines.append(f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}\n")
    lines.append(f"**Data Period:** {at['date_range']} ({at['months_tracked']} months)\n")

    lines.append("\n## All-Time Totals\n")
    lines.append("| Metric | Booking.com | Airbnb | TOTAL |")
    lines.append("|--------|------------|--------|-------|")
    lines.append(f"| Gross Earnings | EUR {at['booking_gross']:,.2f} | EUR {at['airbnb_gross']:,.2f} | EUR {at['total_gross']:,.2f} |")
    lines.append(f"| Platform Fees | EUR {at['booking_fees']:,.2f} | EUR {at['airbnb_fees']:,.2f} | EUR {at['total_fees']:,.2f} |")
    lines.append(f"| Net Earnings | EUR {at['booking_net']:,.2f} | EUR {at['airbnb_net']:,.2f} | EUR {at['total_net']:,.2f} |")

    lines.append(f"\n| Metric | Value |")
    lines.append(f"|--------|-------|")
    lines.append(f"| Avg Monthly Gross | EUR {at['avg_monthly_gross']:,.2f} |")
    lines.append(f"| Avg Monthly Net | EUR {at['avg_monthly_net']:,.2f} |")
    lines.append(f"| Occupancy | {at['occupancy_pct']}% |")
    lines.append(f"| ADR | EUR {at['adr']:,.2f} |")
    lines.append(f"| Total Nights | {at['total_nights']} |")
    lines.append(f"| Total Bookings | {at['total_bookings']} |")
    lines.append(f"| Unique Guests | {at['unique_guests']} |")
    lines.append(f"| Best Month | {at['best_month']['label']} (EUR {at['best_month']['gross']:,.2f}) |")
    lines.append(f"| Worst Month | {at['worst_month']['label']} (EUR {at['worst_month']['gross']:,.2f}) |")

    lines.append("\n## Monthly Breakdown\n")
    lines.append("| Month | Booking Gross | Booking Fees | Booking Net | Airbnb Gross | Airbnb Fees | Airbnb Net | TOTAL Gross | TOTAL Fees | TOTAL Net |")
    lines.append("|-------|-------------|-------------|------------|-------------|------------|-----------|------------|-----------|----------|")
    for mk in sorted(metrics["monthly"].keys()):
        m = metrics["monthly"][mk]
        lines.append(
            f"| {m['month_label']} | {m['booking_gross']:,.2f} | {m['booking_fees']:,.2f} | {m['booking_net']:,.2f} | "
            f"{m['airbnb_gross']:,.2f} | {m['airbnb_fees']:,.2f} | {m['airbnb_net']:,.2f} | "
            f"{m['total_gross']:,.2f} | {m['total_fees']:,.2f} | {m['total_net']:,.2f} |"
        )

    lines.append("\n## Yearly Summary\n")
    lines.append("| Year | Booking Net | Airbnb Net | TOTAL Net | YoY Growth |")
    lines.append("|------|-----------|----------|----------|------------|")
    for year in sorted(metrics["yearly"].keys()):
        y = metrics["yearly"][year]
        growth = f"{y['yoy_growth_pct']:+.1f}%" if y["yoy_growth_pct"] is not None else "--"
        lines.append(f"| {year} | EUR {y['booking_net']:,.2f} | EUR {y['airbnb_net']:,.2f} | EUR {y['total_net']:,.2f} | {growth} |")

    if issues:
        lines.append("\n## Issues & Warnings\n")
        for issue in issues:
            lines.append(f"- **[{issue['severity']}]** {issue['message']}")

    lines.append(f"\n## Months Processed\n")
    lines.append(f"```\n{', '.join(metrics['months_processed'])}\n```\n")

    report = "\n".join(lines) + "\n"
    path = PROJECT_ROOT / "financial_report.md"
    path.write_text(report, encoding="utf-8")
    return str(path)


def _generate_json(metrics, booking_summary, airbnb_summary, issues):
    """Generate financial_data.json."""
    data = {
        "generated": datetime.now().isoformat(),
        "all_time": metrics["all_time"],
        "monthly": metrics["monthly"],
        "yearly": metrics["yearly"],
        "months_processed": metrics["months_processed"],
        "source_summaries": {
            "booking_com": booking_summary,
            "airbnb": airbnb_summary,
        },
        "issues": issues,
    }
    path = PROJECT_ROOT / "financial_data.json"
    path.write_text(json.dumps(data, indent=2, default=str), encoding="utf-8")
    return str(path)


def _print_summary(metrics, issues):
    at = metrics["all_time"]
    print(f"\n{'=' * 70}")
    print(f"  FINANCIAL SUMMARY")
    print(f"{'=' * 70}")
    print(f"  Period:          {at['date_range']} ({at['months_tracked']} months)")
    print(f"")
    hdr = f"  {'':>20} {'Booking.com':>14} {'Airbnb':>14} {'TOTAL':>14}"
    sep = f"  {'':>20} {'----------':>14} {'------':>14} {'-----':>14}"
    bg = f"EUR {at['booking_gross']:,.2f}"
    ag = f"EUR {at['airbnb_gross']:,.2f}"
    tg = f"EUR {at['total_gross']:,.2f}"
    bf = f"EUR {at['booking_fees']:,.2f}"
    af = f"EUR {at['airbnb_fees']:,.2f}"
    tf = f"EUR {at['total_fees']:,.2f}"
    bn = f"EUR {at['booking_net']:,.2f}"
    an = f"EUR {at['airbnb_net']:,.2f}"
    tn = f"EUR {at['total_net']:,.2f}"
    print(hdr)
    print(sep)
    print(f"  {'Gross Earnings':>20} {bg:>14} {ag:>14} {tg:>14}")
    print(f"  {'Platform Fees':>20} {bf:>14} {af:>14} {tf:>14}")
    print(f"  {'Net Earnings':>20} {bn:>14} {an:>14} {tn:>14}")

    print(f"\n  Occupancy: {at['occupancy_pct']}%  |  ADR: EUR {at['adr']:,.2f}  |  "
          f"Nights: {at['total_nights']}  |  Guests: {at['unique_guests']}")
    print(f"  Best: {at['best_month']['label']} (EUR {at['best_month']['gross']:,.2f})")

    if metrics["yearly"]:
        print(f"\n  YEARLY:")
        for year, y in sorted(metrics["yearly"].items()):
            growth = f" (YoY: {y['yoy_growth_pct']:+.1f}%)" if y["yoy_growth_pct"] is not None else ""
            print(f"    {year}: Booking EUR {y['booking_net']:,.2f} + Airbnb EUR {y['airbnb_net']:,.2f} "
                  f"= EUR {y['total_net']:,.2f} net{growth}")

    if issues:
        print(f"\n  ISSUES ({len(issues)}):")
        for issue in issues:
            print(f"    [{issue['severity']}] {issue['message']}")

    print(f"\n  Months processed: {', '.join(metrics['months_processed'])}")
    print(f"\n  OUTPUT FILES:")
    print(f"    - financial_dashboard.xlsx  (6-sheet Excel workbook)")
    print(f"    - financial_report.md       (markdown report)")
    print(f"    - financial_data.json       (machine-readable data)")
    print(f"{'=' * 70}\n")


if __name__ == "__main__":
    run()
